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

    return {
        "items": starting_items,
        "worry_operation": worry_operation,
        "divisibility_test": divisibility_test,
        "true_target": true_target,
        "false_target": false_target,
        "inspection_count": 0,
    }

with open(sys.argv[1], 'r') as f:
    text = f.read()

    monkeys_str = text.split("\n\n")

    number_of_monkeys = len(monkeys_str)

    monkeys = [process_monkey_text(x) for x in monkeys_str]

def examine_and_throw_items(monkey, all_monkeys):
    for i in range(len(monkey["items"])):
        old = monkey["items"][i]
        new_value = int(eval(monkey["worry_operation"]) / 3) # examine and get bored
        monkey["inspection_count"] += 1
        if (new_value % monkey["divisibility_test"]) == 0:
            all_monkeys[monkey["true_target"]]["items"].append(new_value)
        else:
            all_monkeys[monkey["false_target"]]["items"].append(new_value)
    monkey["items"] = []

for i in range(20):
    for monkey in monkeys:
        examine_and_throw_items(monkey, monkeys)

counts = [m["inspection_count"] for m in monkeys]
counts.sort()

print(counts[-2:])
print(counts[-2]*counts[-1])
    