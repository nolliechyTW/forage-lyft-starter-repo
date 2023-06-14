from serviceable import Serviceable


class Car(Serviceable): # Car inherits from the Serviceable abstract base class
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self): # abstract method inherited from the Serviceable
        return self.engine.needs_service or self.battery.needs_service