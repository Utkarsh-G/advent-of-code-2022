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
        "num": monkey_number,
        "items": starting_items,
        "worry_operation": worry_operation,
        "divisibility_test": divisibility_test,
        "true_target": true_target,
        "false_target": false_target,
        "inspection_count": 0,
    }

def build_mod_list(monkeys):
    test_list = [monkey["divisibility_test"] for monkey in monkeys]
    for monkey in monkeys:
        monkey["item_mod_list"] = []
        for item in monkey["items"]:
            monkey["item_mod_list"].append([{test: item%test} for test in test_list ])
        

with open(sys.argv[1], 'r') as f:
    text = f.read()

    monkeys_str = text.split("\n\n")

    number_of_monkeys = len(monkeys_str)

    monkeys = [process_monkey_text(x) for x in monkeys_str]

def examine_and_throw_items_mods(monkey, all_monkeys):
    for i in range(len(monkey["item_mod_list"])):
        item_mod_list = monkey["item_mod_list"][i]
        mod_for_throw_check = 0
        for item_mod in item_mod_list:
            #print(item_mod)
            for test, old in item_mod.items():
                item_mod[test] = int(eval(monkey["worry_operation"])) % test
                if test == monkey["divisibility_test"]:
                    print(f"post eval: {item_mod}")
                    mod_for_throw_check = item_mod[test]
                    print(f"and test mod is: {mod_for_throw_check}")
            #monkey["item_mod_list"][i][item_mod.key]
        #new_value = int(eval(monkey["worry_operation"])) # examine and get bored
        monkey["inspection_count"] += 1
        #monkey["item_mod_list"][i]
        #item = monkey["items"][i] 
        #this
        if mod_for_throw_check == 0: #(new_value % monkey["divisibility_test"]) == 0:
            all_monkeys[monkey["true_target"]]["item_mod_list"].append(item_mod_list)
            all_monkeys[monkey["true_target"]]["items"].append(monkey["items"][i])
            
            print(f"{monkey['num']} is throwing {monkey['items'][i]} over to {monkey['true_target']}")
        else:
            all_monkeys[monkey["false_target"]]["item_mod_list"].append(item_mod_list)
            all_monkeys[monkey["false_target"]]["items"].append(monkey["items"][i])

            print(f"{monkey['num']} is throwing {monkey['items'][i]} over to {monkey['false_target']}")
            
    monkey["item_mod_list"] = []
    monkey["items"] = []
    #num = monkey["monkey_number"]
    print(f"\nfor next monkey processed:\n")
    print(monkeys)



build_mod_list(monkeys)
print(monkeys)

for i in range(1):
    for monkey in monkeys:
        examine_and_throw_items_mods(monkey, monkeys)

counts = [m["inspection_count"] for m in monkeys]
print(counts)
counts.sort()

print(counts[-2:])
print(counts[-2]*counts[-1])
#print(monkeys)    