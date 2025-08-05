for num in range(1, 1001):
    sum = 0
    temp = num
    while temp > 0:
        last = temp % 10
        fact = 1
        for i in range(1, last + 1):
            fact *= i
        sum += fact
        temp = temp // 10
    if sum == num:
        print(num, "is a strong number")
