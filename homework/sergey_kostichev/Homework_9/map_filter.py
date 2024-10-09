def high_temperature(t):
    if t > 28:
        return t


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

high_temperatures = list(filter(high_temperature, temperatures))
average_value = round(sum(high_temperatures) / len(high_temperatures), 2)

print("The highest temperature is", max(high_temperatures))
print("The lowest temperature is", min(high_temperatures))
print("The average temperature is", average_value)
