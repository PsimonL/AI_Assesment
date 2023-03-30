a = [1, 1, 1, 1, 2, 1]

try:
    for i in range(len(a)):
        if a[i] != 1:
            break
except ValueError:
    print("Not Passed")

