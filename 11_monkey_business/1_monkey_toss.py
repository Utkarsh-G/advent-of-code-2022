import sys

def process_monkey_text(text):
    monkey = {}
    split_text = text.split("\n")
    monkey_number = int(split_text[0].split(" ")[1][0])
    starting_items =  [int(x) for x in split_text[1].strip().split(": ")[1].split(", ")]
    worry_operation = split_text[2].strip().split("= ")[1]
    divisibility_test = int(split_text[3].strip().split(" ")[-1])
    true_target = int(split_text[4].strip().split(" ")[-1])
    false_target = int(split_text[5].strip().split(" ")[-1])

    return {starting_items, worry_operation, divisibility_test, true_target, false_target}

with open(sys.argv[1], 'r') as f:
    text = f.read()

    monkeys_str = text.split("\n\n")

    number_of_monkeys = len(monkeys_str)

    monkeys = []

    [process_monkey_text(x) for x in monkeys_str]




    