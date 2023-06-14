import unittest
from tire.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_servive_true(self):
        tire_wear = 0.96
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_servive_false(self):
        tire_wear = 0.8
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())
        
