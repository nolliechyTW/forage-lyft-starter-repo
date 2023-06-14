from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine

class carFactory: # create different types of car
    @staticmethod
    def create_calliope(current_date, last_service_date, current_milleage, last_service_mileage):
        engine = CapuletEngine(current_milleage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_milleage, last_service_mileage):
        engine = WilloughbyEngine(current_milleage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car   
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car   

    @staticmethod
    def create_rorschach(current_date, last_service_date, warning_light_is_on):
        engine = WilloughbyEngine(warning_light_is_on)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car   
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_milleage, last_service_mileage):
        engine = CapuletEngine(current_milleage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car   
    