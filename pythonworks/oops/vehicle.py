class bike:
    def start(self):
        print("kicker start")
    def breaking(self):
        print("drum break")
class HeroHondaSplender(bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs breaking")
hobj=HeroHondaSplender()
hobj.start()