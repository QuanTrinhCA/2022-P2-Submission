numofint = int(input())
integers = input().split()
timeneed = int()

timeneed += (numofint - 1) * 7

for integer in integers:
    for character in integer:
        timeneed += 3
        if character == '0': timeneed += 19
        elif character == '1': timeneed += 17
        elif character == '2': timeneed += 15
        elif character == '3': timeneed += 13
        elif character == '4': timeneed += 11
        elif character == '5': timeneed += 9
        elif character == '6': timeneed += 11
        elif character == '7': timeneed += 13
        elif character == '8': timeneed += 15
        elif character == '9': timeneed += 17
    timeneed -= 3

print(str(timeneed))