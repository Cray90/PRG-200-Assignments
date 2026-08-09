import math

station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    total = sum(temps)
    average = total / len(temps)
    return average


def get_deviation(temps):

    mean = get_average(temps)      # Local variable

    total = 0

    for temp in temps:
        total = total + (temp - mean) ** 2

    deviation = math.sqrt(total / len(temps))
    return deviation


def get_summary(temps):

    print(station_name)
    print("Minimum Temperature:", min(temps))
    print("Maximum Temperature:", max(temps))
    print("Average Temperature:", round(get_average(temps), 2))
    print("Standard Deviation:", round(get_deviation(temps), 2))


get_summary(temperatures)