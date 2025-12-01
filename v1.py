import random

roles = ["window", "shots", "milk", "linebuster"]

shift_start = int(input("When does your shift start? (24h): "))
shift_end = int(input("When does your shift end? (24h): "))

hours = shift_end - shift_start
hour_count = 0.00

for x in range(hours):
    role = random.choice(roles)
    hour_count += 1.00
    print(f'Hour {hour_count}')
    print(f'  {role}')
