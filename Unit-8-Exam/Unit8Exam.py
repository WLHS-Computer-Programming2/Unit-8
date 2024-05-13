class AmusementParkAttraction:
    def __init__(self,name,ticket_cost):
        self.name=name
        self.ticket_cost=ticket_cost

    def __str__(self):
        return f'Name: {self.name}\nTicket Cost: {self.ticketCost}'

    def __repr__(self):
        return self.__str__()

class RollerCoaster(AmusementParkAttraction):

    def __init__(self,name,ticket_cost,num_loops):
        super().__init__(name,ticket_cost)
        self.num_loops=num_loops

    def __str__(self):
        return super().__str__()+f"\nNumber of loops: {self.num_loops}"

    def __repr__(self):
        return self.__str__()

class FerrisWheel(AmusementParkAttraction):
    def __init__(self,name,ticket_cost,height):
        super().__init__(name,ticket_cost)
        self.height=height

    def __str__(self):
        super().__str__()+f"\nHeight of the ferris wheel: {self.height}"