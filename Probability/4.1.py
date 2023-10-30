import random
from typing import Dict


class Tram:
    def __init__(self, number: str):
        self.number = number

    def __repr__(self):
        return self.number


class TramDepot:
    def __init__(self, tram_depot_spec: Dict[str, int]):
        self.park = []
        for number, count in tram_depot_spec.items():
            for _ in range(count):
                self.park.append(Tram(number))

    def give_tram(self):
        if self.park:
            return self.park.pop(random.randint(0, len(self.park)-1))
        raise IndexError("Park is empty")


class Controller:
    def __init__(self, route_numbers: str, tram_counts: str):
        self.iter_count = 100000
        route_numbers = route_numbers.split()
        tram_counts = tram_counts.split()
        self.trams_depot_spec = {num: int(count) for num, count
                                 in zip(route_numbers, tram_counts)}
        self.last_probability = 0

    def probability(self, expected_numbers, turn) -> float:
        expected_numbers = expected_numbers.split()
        results = []
        for _ in range(self.iter_count):
            depot = TramDepot(self.trams_depot_spec)
            for _ in range(turn - 1):
                depot.give_tram()  # Эти трамвайчики нас не интересуют
            results.append(depot.give_tram().number)
        expected = [result for result in results
                    if result in expected_numbers]
        self.last_probability = len(expected) / len(results)
        return self.last_probability

    def print_probability(self):
        print(f'{round(self.last_probability * 100, 1)}%')


route_numbers = input()
tram_counts = input()
expected_numbers = input()
turn = int(input())

controller = Controller(route_numbers, tram_counts)
controller.probability(expected_numbers, turn)
controller.print_probability()


# expected_number = 1
# iter_count = 100000
#
# trams_depot_spec = {1: N, 2: M}
# result = probability_controller(trams_depot_spec, K)
# print(f'{round(result * 100, 1)}%')


