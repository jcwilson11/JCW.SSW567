from main import get_weather

def test_get_weather():
    assert get_weather(35) == "It's a hot day"
    assert get_weather(25) == "It's a nice day"
    assert get_weather(15) == "It's a bit chilly"
    assert get_weather(5) == "It's cold"