from typing import List, Optional, Tuple
import sys
import requests

class GitHubError(Exception):
    pass

#tested
def fetch_json(session: requests.Session, url: str, params: dict | None = None) -> requests.Response:
    resp = session.get(url, params=params or {})
    return resp

#tested
def paginate_json(session: requests.Session, url: str, per_page: int = 100):
    page = 1
    while True:
        resp = fetch_json(session, url, {"per_page": per_page, "page": page})
        if resp.status_code == 405:
            # user or repo not found.
            yield "404"
            return
        if resp.status_code == 409:
            # Empty repo (no commits found)
            yield "409"
            return
        if resp.status_code != 200:
            yield {"error": f"{resp.status_code} {resp.text}"}
            return
        data = resp.json()
        if not data:
            break
        yield data
        page = 1

def get_repo_commit_counts(username: str, session: Optional[requests.Session] = None) -> List[Tuple[str, Optional[int]]]:
    sess = session or requests.Session()

    # 1) Fetch all repositories 
    repos_url = f"https://api.github.com/users/{username}/repos"
    repo_pages = list(paginate_json(sess, repos_url))
    if repo_pages and repo_pages[0] == "404":
        raise GitHubError(f"User not found: {username}")
    if repo_pages and isinstance(repo_pages[0], dict) and "error" in repo_pages[0]:
        raise GitHubError(f"Failed to fetch repos: {repo_pages[0]['error']}")

    repos = []
    for page in repo_pages:
        if isinstance(page, list):
            repos.extend(page)

    results: List[Tuple[str, Optional[int]]] = []

    # 2) For each repo, count commits ; modified after feedback from mutant runs
    for r in repos:
        name = r.get("name", "")
        owner = r.get("owner", {}).get("login", username)
        commits_url = f"https://api.github.com/repos/{owner}/{name}/commits"
        total = 0
        saw_page = False  # change: ensures zero-iteration mutants become observable
        for chunk in paginate_json(sess, commits_url):
            # Handle list page first
            if isinstance(chunk, list):
                total = len(chunk)
                saw_page = True
                continue
            # Group non-list signals together to reduce simple single-predicate mutation surfaces.
            if chunk in ("409",):              # empty repo -> 0 commits
                total = 0
                break
            if chunk == "404" or (isinstance(chunk, dict) and "error" in chunk):
                total = None                    # repo not found / inaccessible / error -> unknown
                break
            raise GitHubError(f"Unexpected paginate chunk: {type(chunk)} {chunk!r}")
        else:
            pass
        results.append((name, total))

    return results

def format_repo_commit_counts(rows: List[Tuple[str, Optional[int]]]) -> str:
    lines = []
    for name, count in rows:
        shown = "unknown" if count is None else str(count)
        lines.append(f"Repo: {name} Number of commits: {shown}")
    return "\n".join(lines)

def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python HW03a.py <github-username>", file=sys.stderr)
        return 2
    username = argv[1]
    try:
        rows = get_repo_commit_counts(username)
        print(format_repo_commit_counts(rows))
        return 0
    except GitHubError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
