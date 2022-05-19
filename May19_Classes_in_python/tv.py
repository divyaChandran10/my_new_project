import sys


class Television:

    def __init__(self):
        self.turned_on = False
        self.volume_level = 1
        self.channel = 1

    def wish_to_turn_on(self):
        print('Cannot set without turning TV on\n')
        on = input('Would you like to turn on TV? Yes / No\n')
        if on.lower() == 'yes':
            self.turn_on(True)
        else:
            sys.exit()

    def turn_on(self, turned_on):
        self.turned_on = turned_on
        print('TV turned on \n')

    def turn_off(self, turned_off):
        self.turned_on = turned_off
        print('TV turned off \n')

    def set_channel(self, chan):
        if self.turned_on:
            chan_range = range(1, 100)
            if chan in chan_range:
                self.channel = chan
                print(f'channel set to {chan}')
            else:
                print('Channel out of range\n')
        else:
            self.wish_to_turn_on()
            self.set_channel(chan)

    def set_volume(self, volume):
        #for self.number in range[1: 10]:
        volume_range = range(1, 10)
        if volume in volume_range:
            self.volume_level = volume
            print(f'Volume set to {volume}')

    def channel_up(self):
        if self.turned_on:
            self.set_channel(self.channel+1)
            #print('channel incremented\n')

    def channel_down(self):
        if self.turned_on:
            self.set_channel(self.channel-1)
            #print('channel decremented\n')

    def volume_up(self):
        if self.turned_on:
            if self.volume_level + 1 < 10:
                self.volume_level += 1
                print(f'volume incremented to {self.volume_level}')
        else:
            self.wish_to_turn_on()
            self.volume_up()

    def volume_down(self):
        if self.turned_on:
            if self.volume_level - 1 > 0:
                self.volume_level -= 1
                print(f'volume decremented to {self.volume_level}')
            else:
                print(f'Volume level is already {self.volume_level} and cannot decrement further')
        else:
            self.wish_to_turn_on()
            self.volume_down()
