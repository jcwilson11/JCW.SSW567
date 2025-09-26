import pytest
import requests
from HW03a import fetch_json

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

