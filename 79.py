class MediumPowerBattery:
    charge = 100
    maxUsageRate = 50 

    def use(self, chargeUsed):
        if chargeUsed <= self.maxUsageRate:
            self.charge -= chargeUsed 
            return chargeUsed

        return 0
    
    def checkCharge(self):
        return self.charge

class NonDI_Toy:
    battery = MediumPowerBattery()

    def run(self):
        if self.battery.checkCharge() > 0:
            self.battery.use(50)
            print("Running!")
            return 
        print("Battery dead...")

toy1 = NonDI_Toy()
toy1.run()
toy1.run()
toy1.run()
print() # For a line break

# The problem with the class NonDI_Toy is that if we wanted 
# to swap out the battery for a more powerful battery battery or test it with a mock battery,
# it is not that easy because we have to modify the class itself and all its usages. 
# Here is where Dependency Injection is really useful

class MegaPowerBattery:
    charge = 10000
    maxUsageRate = 500

    def use(self, chargeUsed):
        if chargeUsed <= self.maxUsageRate:
            self.charge -= chargeUsed 
            return chargeUsed

        return 0
    
    def checkCharge(self):
        return self.charge


class DI_Toy:
    battery = None 

    def init(self, battery):
        self.battery = battery

    def run(self):
        if self.battery.checkCharge() > 0:
            self.battery.use(50)
            print("Running!")
            return 
        print("Battery dead...")

toy1 = DI_Toy()
battery1 = MegaPowerBattery()
toy1.init(battery1)
toy1.run()
toy1.run()
toy1.run()
toy1.run()
toy1.run()

# Here, the DI_Toy class uses Dependency Injection to make testing and reusablity better.
# The init function inside the DI_Toy class doesn't care what the class that we passed is. 
# It just wants the class to have two methods, one is checkCharge() and another one is use()
# Here, as you can see, we have swapped out the default MediumPowerBattery with a much more 
# powerful battery very easily without having to change the class definition and usages.


