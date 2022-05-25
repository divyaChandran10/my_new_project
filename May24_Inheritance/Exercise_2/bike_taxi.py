from bike import Bike

from public_transport import PublicTransport


class BikeTaxi(PublicTransport, Bike):

    def __init__(self, **kwargs):
        super().__init__()
        self.motorized = kwargs.get("motorized", False)
        self.__current_passengers = kwargs.get("num", 0)
        if self.motorized:
            self.speed = 30
            self.max_passengers = 4
        else:
            self.speed = 18
            self.max_passengers = 2
    #  TODO: Make BikeTaxi subclass Bike and PublicTransport classes.
    """def __init__(self, motorized, **kwargs):
        self._mileage_until_next_repair = 200
        #PublicTransport.__init__(self, **kwargs)
        #Bike.__init__(self, **kwargs)
        self.__current_passengers = 0
        self.motorized = motorized
        #self.motorized = kwargs.get("motorized")

        super().__init__(**kwargs)
        print('///////////////////')
        print(kwargs.get('motorized'))
        #self.maximum_mileage = kwargs["maximum_mileage"]
        #self.speed = kwargs["speed"]
        if self.motorized:
        #if kwargs["motorized"]:
            self.speed = 30
            #PublicTransport.__init__(self, **kwargs)
        else:
            self.speed = 18
            #Bike.__init__(self, **kwargs)

        #super().__init__(**kwargs)

        # kwargs["motorized"] = True
        # super().__init__(**kwargs)
"""

    def repair(self):
        super().repair()
        # print("The "
        # + type(self).__name__
        # + " has been repaired.")
        # self._mileage_until_next_repair = 200

    def drive(self, km: int) -> bool:
        return super().drive(km)
        # if self._mileage_until_next_repair < 0:
        #     print(
        #         "The "
        #         + type(self).__name__
        #         + " needs to be repaired before it can go any further."
        #     )
        #     return False
        # if super().drive(km):
        #     self._mileage_until_next_repair -= km
        #     return True
        # return False

    def enter_passengers(self, num: int):
        #print(str(num) + " passengers are entering.")
        #self.__current_passengers += num

        if self.get_current_passengers() + num > self.max_passengers:
            print('Cannot load more passengers at this time.')
        else:
            PublicTransport.enter_passengers(self, num)

        # if self.__current_passengers > 2:
        #     print('Cannot load more passengers at this time.')
        # else:
        #     Bike.enter_passengers(self, num)

    def exit_passengers(self, num: int):
        #print(str(num) + " passengers are exiting.")
        #self.__current_passengers -= num
        PublicTransport.exit_passengers(self, num)

    def get_current_passengers(self) -> int:
        return PublicTransport.get_current_passengers(self)
