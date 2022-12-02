f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()


def calorie_calculator(file):
    calories = []
    temp_calories = 0
    for line in file:
        if line == "":
            calories.append(temp_calories)
            temp_calories = 0
            continue
        temp_calories += int(line)
    return calories


def part1(file):
    return max(calorie_calculator(file))


def part2(file):
    calories = calorie_calculator(file)
    calories.sort(reverse=True)
    return calories[0] + calories[1] + calories[2]


print(part1(lines))
print(part2(lines))
