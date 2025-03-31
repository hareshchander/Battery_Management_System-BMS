def check_battery_status(voltage, temperature):
    if voltage < 3.0:
        return "Low Voltage - Charging Required"
    elif voltage > 4.2:
        return "High Voltage - Risk of Overcharge"
    elif temperature > 45:
        return "High Temperature - Cooling Required"
    else:
        return "Battery Status Normal"
