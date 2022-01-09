#0
print("Don't forget to pull commits, to avoid working on the old version of your project.")

# 1
name_list = ["John", "Micheal", "Terry", "Eric", "Graham"]
name_dict = {name: len(name) for name in name_list}

print(name_dict.items())

# 2
num_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_list = []
for num in num_list:
    count = 2
    for j in range(2, num):
        if num % j == 0:
            count += 1
        if count > 2:
            break
    if count == 2:
        prime_list.append(num)
print(prime_list)

# 3
days_list = ['pon', 'śro', 'pią', 'sob']
days_list.insert(1, 'wto')
days_list.insert(3, 'czw')
days_list.insert(6, 'nie')
print(days_list)

# 4
steps_dict = {
    "Włącz czajnik.": 2,
    "Znajdź opakowanie herbaty.": 4,
    "Zalej herbatę.": 6,
    "Nalej wody do czajnika.": 1,
    "Wyjmij kubek": 3,
    "Włóż herbatę do kubka": 5
}

steps_sorted = sorted(steps_dict)
print(steps_sorted)

"""
steps_list = [
    "Włącz czajnik.", "Znajdź opakowanie herbaty.", "Zalej herbatę.",
    "Nalej wody do czajnika.", "Wyjmij kubek", "Włóż herbatę do kubka"
]
for i in range(len(steps_list)):
    step = steps_list[i]
    correct_step = steps_dict[i + 1]
    while step != correct_step:
        steps_list.remove(step)
        steps_list.append(step)
        step = steps_list[i]
print(steps_list)
"""
