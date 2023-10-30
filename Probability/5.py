import random


class Ticket:
    def __init__(self, number: int):
        self.number = number

    def __repr__(self):
        return str(self.number)


class Box:
    def __init__(self, ticket_count):
        self.tickets = [Ticket(num) for num in range(1, ticket_count+1)]

    def give_ticket(self):
        if self.tickets:
            return self.tickets.pop(random.randint(0, len(self.tickets)-1))
        raise IndexError("Box is empty")

    def __iter__(self):
        return self

    def __next__(self):
        if self.tickets:
            return self.give_ticket()
        raise StopIteration


class Controller:
    def __init__(self, ticket_count: int):
        self.iter_count = 100000
        self.ticket_count = ticket_count
        self.last_probability = 0

    def probability(self) -> float:

        results = []
        for _ in range(self.iter_count):
            box = Box(self.ticket_count)
            expected_done = 0
            for i, ticket in enumerate(box, start=1):
                if ticket.number == i:
                    expected_done += 1
            if expected_done:
                results.append(expected_done)
        self.last_probability = len(results) / self.iter_count
        return self.last_probability

    def print_probability(self):
        print(f'{round(self.last_probability * 100, 1)}%')


ticket_count = int(input())

controller = Controller(ticket_count)
controller.probability()
controller.print_probability()