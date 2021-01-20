# Question 1
# Write a Python Program to print all prime numbers in an interval

start = 100
end = 500

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)