import pytest
import requests
from HW03a import fetch_json, paginate_json, get_repo_commit_counts, format_repo_commit_counts, GitHubError

def test_fetch_json_success(monkeypatch):
    class MockResponse:
        def __init__(self, status_code=200, json_data=None):
            self.status_code = status_code
            self._json = json_data or {}

        def json(self):
            return self._json

    def mock_get(self, url, params=None):
        assert url == "https://api.github.com/test"
        assert params == {"key": "value"}
        return MockResponse(json_data={"result": "ok"})

    monkeypatch.setattr(requests.Session, "get", mock_get)
    session = requests.Session()
    response = fetch_json(session, "https://api.github.com/test", {"key": "value"})
    # expected success
    assert response.json() == {"result": "ok"}
    # Status code sources: https://gist.github.com/subfuzion/669dfae1d1a27de83e69  
    assert response.status_code == 200
    assert response.status_code != 304
    assert response.status_code not in (400, 401, 403, 404, 405, 406, 409, 422, 429)
    assert response.status_code not in (500, 502, 503, 504) 
    #expected failure
    #assert response.status_code == 300 

def test_paginate_json_404(monkeypatch):
    def mock_fetch_json(session, url, params=None):
        class MockResponse:
            status_code = 404
        return MockResponse()
    
    monkeypatch.setattr("HW03a.fetch_json", mock_fetch_json)
    session = requests.Session()
    result = list(paginate_json(session, "https://api.github.com/fake"))
    assert result == ["404"]

def test_paginate_json_409(monkeypatch):
    def mock_fetch_json(session, url, params=None):
        class MockResponse:
            status_code = 409
        return MockResponse()
    
    monkeypatch.setattr("HW03a.fetch_json", mock_fetch_json)
    session = requests.Session()
    result = list(paginate_json(session, "https://api.github.com/fake"))
    assert result == ["409"]

def test_paginate_json_error(monkeypatch):
    def mock_fetch_json(session, url, params=None):
        class MockResponse:
            status_code = 500
            text = "Internal Server Error"
        return MockResponse()
    
    monkeypatch.setattr("HW03a.fetch_json", mock_fetch_json)
    session = requests.Session()
    result = list(paginate_json(session, "https://api.github.com/fake"))
    assert result == [{"error": "500 Internal Server Error"}]

def test_paginate_json_success(monkeypatch):
    responses = [
        [{"id": 1}, {"id": 2}],
        [{"id": 3}],
        []  # signals end of pagination
    ]
    call_count = {"count": 0}

    def mock_fetch_json(session, url, params=None):
        class MockResponse:
            status_code = 200
            def json(self):
                i = call_count["count"]
                call_count["count"] += 1
                return responses[i]
        return MockResponse()
    
    monkeypatch.setattr("HW03a.fetch_json", mock_fetch_json)
    session = requests.Session()
    result = list(paginate_json(session, "https://api.github.com/fake"))
    assert result == responses[:-1]  # exclude empty page


def test_get_repo_commit_counts_user_not_found(monkeypatch):
    def mock_paginate_json(session, url, per_page=100):
        return ["404"]

    monkeypatch.setattr("HW03a.paginate_json", mock_paginate_json)
    session = requests.Session()
    with pytest.raises(GitHubError, match="User not found: invaliduser"):
        get_repo_commit_counts("invaliduser", session)

def test_get_repo_commit_counts_repo_error(monkeypatch):
    def mock_paginate_json(session, url, per_page=100):
        return [{"error": "500 Internal Server Error"}]

    monkeypatch.setattr("HW03a.paginate_json", mock_paginate_json)
    session = requests.Session()
    with pytest.raises(GitHubError, match="Failed to fetch repos: 500 Internal Server Error"):
        get_repo_commit_counts("erroruser", session)

def test_get_repo_commit_counts_no_repos(monkeypatch):
    calls = {"urls": []}

    def mock_paginate_json(session, url, per_page=100):
        calls["urls"].append(url)
        if "/users/" in url and url.endswith("/repos"):
            return [[]]  # one page, zero repos
        raise AssertionError("Unexpected URL: " + url)

    monkeypatch.setattr("HW03a.paginate_json", mock_paginate_json)
    result = get_repo_commit_counts("someone")

    # passes
    assert isinstance(result, list)
    assert result == []  # empty list when there are no repos
    assert calls["urls"] == ["https://api.github.com/users/someone/repos"]  # only repo list was fetched

    # intentional fail; if the function incorrectly returns anything else
    #assert result is None
    #assert len(result) == 1

def test_format_repo_commit_counts_basic():
    input_data = [("repo1", 5), ("repo2", 0), ("repo3", None), ("repo4", 10)]
    expected_output = (
        "Repo: repo1 Number of commits: 5\n"
        "Repo: repo2 Number of commits: 0\n"
        "Repo: repo3 Number of commits: unknown"
        #"Repo: repo4 Number of commits: 9" # intentional fail
    )
    assert format_repo_commit_counts(input_data) == expected_output

