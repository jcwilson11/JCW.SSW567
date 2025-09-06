def get_weather(temp):
    if temp > 30:
        return "It's a hot day"
    elif temp > 20:
        return "It's a nice day"
    elif temp > 10:
        return "It's a bit chilly"
    else:
        return "It's cold"