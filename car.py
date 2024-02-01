class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()

