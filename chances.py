import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
data = pd.read_csv('Data_Final.csv')


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return b_0, b_1


def plot(x, y, title, label_x, label_y):
    b = estimate_coef(x, y)
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)
    # predicted response vector
    y_pred = b[0] + b[1] * x
    # plotting the regression line
    plt.plot(x, y_pred, color="g")
    # putting labels
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    # function to show plot
    plt.show()


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
    if new_time > 24:
        new_time = new_time/10
    time_prob = float(time_d[new_time]/time_sum)
    x = np.array(list(time_d.keys()))
    y = np.array(list(time_d.values()))
    plot(x, y, "Accidents vs Time", "Time", "No. of Accidents")
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
    weeks = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for iterator in week_data:
        if iterator in range(1, 8):
            weeks[iterator] = weeks[iterator] + 1
    for x in week_data:
        if day_of_week == x:
            times = times + 1
    a, b = np.array(list(weeks.keys())), np.array(list(weeks.values()))
    plot(a, b, "Accidents vs Days of Week", "Week Day", "No. of Accidents")
    return float(times/len(week_data))


def light_effect():
    light_data, times = data.iloc[:, 7], 0
    light = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for iterator in light_data:
        if iterator in range(1, 7):
            light[iterator] = light[iterator] + 1
    for x in light_data:
        if x == light_condition:
            times = times + 1
    a, b = np.array(list(light.keys())), np.array(list(light.values()))
    plot(a, b, "Accidents vs Light Conditions", "Light Condition", "No. of Accidents")
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
final_chances = [time_effect(), alcohol_effect(), week_effect(), light_effect(), police_effect(), speed_effect()]
probability = max(final_chances) + 0.005
print("\n\nChances of accident = ", format(probability*100, '.2f'), end=" ")
if 0 < probability <= 0.10:
    print("\n Less chances of accident")
elif 0.10 < probability <= 0.20:
    print("\n Medium chances of accident")
else:
    print("\n High chances of accident")
factor = final_chances.index(max(final_chances))
switch = {1: "Drive Safely because you're entering peak traffic time",
          2: "You should not drink and drive",
          3: "Fridays - Sundays are busy traffic days",
          4: "Choose better lighting condition for driving",
          5: "Police Presence cause considerably less accidents",
          6: "Drive within the speed-limit to stay safe"}
probFactor = 1;
print("\n\nOur advice for you : ", switch[factor + probFactor], end="")
