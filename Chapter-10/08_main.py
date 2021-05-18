class Train:
    def __init__(self, name, fare, seat) -> None:
        self.name = name
        self.fare = fare
        self.seat = seat

    def getstatus(self):
        print(f"The name of the train is {self.name}.\nThe fare of 1 seat is {self.fare}.\n{self.seat} seat is available")
    def booktickte(self):
        if (self.seat > 0):
            print(f'Your ticket has been booked and seat number is {self.seat}')
            self.seat = self.seat -1
        else:
            print('You cant book ticket\n To get more info type "more"\n or tyoe "exit"')
            ask = input('\n')
            while ask != 'exit':
                ask = input('\n')
                print('Because ticket is unavailable')
                print('type "exit" to exit')

intercity = Train('Inter city express', 20, 10)
intercity.getstatus()
intercity.booktickte()
intercity.getstatus()