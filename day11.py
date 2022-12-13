from __future__ import annotations
import numpy as np

with open("day11test.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def get_back_number(string:str):
    return int(string.split()[-1])

def part1():
    class MonkeyBusiness:
        def __init__(self) -> None:
            self.monkeys:list[Monkey] = []

        def add_monkey(self, starting_items:list[int], operation_string:str, divisible_test:int, true_monkey:int, false_monkey:int):
            self.monkeys.append(Monkey(self, starting_items, operation_string, divisible_test, true_monkey, false_monkey))

        def throw_item(self, item_worry_level:int, monkey_index:int):
            self.monkeys[monkey_index].item_worry_levels.append(item_worry_level)

        def do_round_of_business(self):
            for i, monkey in enumerate(self.monkeys):
                # print(i)
                # print(self.monkeys)
                monkey.do_business()

    class Monkey:
        def __init__(self, monkey_business:MonkeyBusiness, starting_items:list[int], operation_string:str, divisible_test:int, true_monkey:int, false_monkey:int) -> None:
            self.monkey_business = monkey_business
            self.item_worry_levels = starting_items
            self.operation_string = operation_string
            self.divisible_test = divisible_test
            self.true_monkey = true_monkey
            self.false_monkey = false_monkey

            self.inspection_count=0
        
        def __repr__(self) -> str:
            return f"Items: {self.item_worry_levels}"

        def do_business(self):
            while len(self.item_worry_levels)>0:
                item_worry_level = self.item_worry_levels.pop(0)
                self.inspection_count+=1
                old = item_worry_level
                new = eval(self.operation_string)
                new_worry_level = np.floor(new/3)

                if new_worry_level%self.divisible_test==0:
                    monkey_business.throw_item(new_worry_level, self.true_monkey)
                else:
                    monkey_business.throw_item(new_worry_level, self.false_monkey)

    monkeys_raws = [monkey.splitlines() for monkey in raw.split("\n\n")]
    
    monkey_business = MonkeyBusiness()

    for monkey_raw in monkeys_raws:
        starting_items = [int(item) for item in monkey_raw[1].split(":")[1].strip().split(",")]
        operation_string = monkey_raw[2].split("=")[-1].strip()
        divisible_test = get_back_number(monkey_raw[3])
        true_monkey = get_back_number(monkey_raw[4])
        false_monkey = get_back_number(monkey_raw[5])
        # print(f"{starting_items=}")
        # print(f"{operation_string=}")
        # print(f"{divisible_test=}")
        # print(f"{true_monkey=}")
        # print(f"{false_monkey=}")

        monkey_business.add_monkey(starting_items, operation_string, divisible_test, true_monkey, false_monkey)

    for _ in range(20):
        monkey_business.do_round_of_business()
    print(np.product(np.sort([monkey.inspection_count for monkey in monkey_business.monkeys])[::-1][0:2]))

def part2():
    class MonkeyBusiness:
        def __init__(self) -> None:
            self.monkeys:list[Monkey] = []
            self.divisible_test_prod = None

        def add_monkey(self, starting_items:list[int], operation_string:str, divisible_test:int, true_monkey:int, false_monkey:int):
            self.monkeys.append(Monkey(self, starting_items, operation_string, divisible_test, true_monkey, false_monkey))

        def throw_item(self, item_worry_level:int, monkey_index:int):
            self.monkeys[monkey_index].item_worry_levels.append(item_worry_level)

        def do_round_of_business(self):
            for i, monkey in enumerate(self.monkeys):
                # print(i)
                # print(self.monkeys)
                monkey.do_business()

        def get_divisible_test_prod(self):
            if self.divisible_test_prod:
                return self.divisible_test_prod
            else:
                self.divisible_test_prod = np.product([monkey.divisible_test for monkey in self.monkeys])
                return self.divisible_test_prod

    class Monkey:
        def __init__(self, monkey_business:MonkeyBusiness, starting_items:list[int], operation_string:str, divisible_test:int, true_monkey:int, false_monkey:int) -> None:
            self.monkey_business = monkey_business
            self.item_worry_levels = starting_items
            self.operation_string = operation_string
            self.divisible_test = divisible_test
            self.true_monkey = true_monkey
            self.false_monkey = false_monkey

            self.inspection_count=0
        
        def __repr__(self) -> str:
            return f"Items: {self.item_worry_levels}"

        def do_business(self):
            while len(self.item_worry_levels)>0:
                item_worry_level = self.item_worry_levels.pop(0)
                self.inspection_count+=1
                old = item_worry_level
                old %=monkey_business.get_divisible_test_prod()
                new_worry_level = eval(self.operation_string)

                if new_worry_level%self.divisible_test==0:
                    monkey_business.throw_item(new_worry_level, self.true_monkey)
                else:
                    monkey_business.throw_item(new_worry_level, self.false_monkey)

    monkeys_raws = [monkey.splitlines() for monkey in raw.split("\n\n")]
    
    monkey_business = MonkeyBusiness()

    for monkey_raw in monkeys_raws:
        starting_items = [int(item) for item in monkey_raw[1].split(":")[1].strip().split(",")]
        operation_string = monkey_raw[2].split("=")[-1].strip()
        divisible_test = get_back_number(monkey_raw[3])
        true_monkey = get_back_number(monkey_raw[4])
        false_monkey = get_back_number(monkey_raw[5])
        # print(f"{starting_items=}")
        # print(f"{operation_string=}")
        # print(f"{divisible_test=}")
        # print(f"{true_monkey=}")
        # print(f"{false_monkey=}")

        monkey_business.add_monkey(starting_items, operation_string, divisible_test, true_monkey, false_monkey)

    for _ in range(1000):
        monkey_business.do_round_of_business()
    print([monkey.inspection_count for monkey in monkey_business.monkeys])
    # print(np.product(np.sort([monkey.inspection_count for monkey in monkey_business.monkeys])[::-1][0:2]))

part2()