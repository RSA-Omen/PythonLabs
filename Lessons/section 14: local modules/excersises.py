def water_state(temperature):
    return "Solid" if temperature < 0 else "Liquid" if temperature > 100 else "Gas"

FREEZING_POINT = 0
BOILING_POINT = 100

def temperature(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"