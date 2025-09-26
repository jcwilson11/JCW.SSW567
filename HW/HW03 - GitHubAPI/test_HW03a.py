import pytest
import requests
from HW03a import fetch_json, paginate_json

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
