import pandas as pd
import math
data = pd.read_csv('Data_Final.csv')


def time_effect():
    time_data, time_d, flag = data.iloc[:, 2], {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, 0
    for x in time_data:
        comp = int(x[0:2])
        if comp in range(0, 4):
            time_d[1] = time_d[1] + 1
        elif comp in range(4, 8):
            time_d[2] = time_d[2] + 1
        elif comp in range(8, 12):
            time_d[3] = time_d[3] + 1
        elif comp in range(12, 16):
            time_d[4] = time_d[4] + 1
        elif comp in range(16, 20):
            time_d[5] = time_d[5] + 1
        elif comp in range(20, 24):
            time_d[6] = time_d[6] + 1
    time_sum = sum(time_d.values())
    new_time = math.ceil(int(time[0:2])/4)
    time_prob = float(time_d[new_time]/time_sum)
    return time_prob


def alcohol_effect():
    alcohol_data, times, zeroes = data.iloc[:, 3], 0, 0
    for x in alcohol_data:
        if x == alcohol:
            times = times + 1
    alcohol_problem = float(times/len(alcohol_data))
    return alcohol_problem


def week_effect():
    week_data, times = data.iloc[:, 5], 0
    for x in week_data:
        if day_of_week == x:
            times = times + 1
    return float(times/len(week_data))


def light_effect():
    light_data, times = data.iloc[:, 7], 0
    for x in light_data:
        if x == light_condition:
            times = times + 1
    return float(times / len(light_data))


def police_effect():
    police_data, times = data.iloc[:, 8], 0
    for x in police_data:
        if x == police:
            times = times + 1
    return float(times / len(police_data))


def speed_effect():
    speed_data, times = data.iloc[:, 10], 0
    for x in speed_data:
        if x == speed_zone:
            times = times + 1
    return float(times / len(speed_data))


time = input("Enter the time of the day (in hours) : ")
alcohol = input("Consumed alcohol above restricted amount ? (No-0 / Yes-1) : ")
day_of_week = input("Day of week, Monday being 1 : ")
light_condition = input(" 1-6 from dawn - dark : ")
police = input("Was police present ? (No-0 / Yes-1) : ")
speed_zone = input("Speed Zone Limit (-1 for no limit) : ")

final_chances = [time_effect(), alcohol_effect(), week_effect(),
                 light_effect(), police_effect(), speed_effect()]
probability = 1
for z in final_chances:
    if z != 0:
        probability = probability * z

print(probability)

if 0 < probability <= 0.25:
    print("Less chances of accident")
elif 0.25 < probability <= 0.50:
    print("Medium chances of accident")
else:
    print("High chances of accident")
