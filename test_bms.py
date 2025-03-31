import unittest
from bms_functions import check_battery_status

class TestBMS(unittest.TestCase):
    def test_low_voltage(self):
        self.assertEqual(check_battery_status(2.8, 30), "Low Voltage - Charging Required")

    def test_high_voltage(self):
        self.assertEqual(check_battery_status(4.5, 30), "High Voltage - Risk of Overcharge")

    def test_high_temperature(self):
        self.assertEqual(check_battery_status(3.6, 50), "High Temperature - Cooling Required")

    def test_normal(self):
        self.assertEqual(check_battery_status(3.7, 35), "Battery Status Normal")

if __name__ == '__main__':
    unittest.main()
