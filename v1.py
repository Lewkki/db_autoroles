import random

roles = ["window", "shots", "milk", "linebuster"]
workers = []

shift_start = int(input("When does your shift start? (24h): "))
shift_end = int(input("When does your shift end? (24h): "))
num_workers = int(input("How many people are on shift? "))

if num_workers == 5:
    roles = ["window", "shots", "milk", "linebuster", "pit"]
elif num_workers == 4:
    roles = ["window", "shots", "milk", "linebuster"]
elif num_workers == 3:
    roles = ["window", "shots", "milk"]
elif num_workers == 2:
    roles = ["window", "shots"]

for x in range(num_workers):
    user_input = input("Enter the name of the worker: ")
    workers.append(user_input)

hours = shift_end - shift_start
hour_count = 0.00

for x in range(hours):
    hour_count += 1.00
    print(f'Hour {hour_count}')
    for worker in workers:
        role = random.choice(roles)
        print(f'  {worker} -> {role}')
