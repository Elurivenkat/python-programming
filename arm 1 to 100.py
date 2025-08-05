# Loop through numbers from 1 to 100
for num in range(1, 101):
    sum = 0  # To store sum of divisors

    # Find divisors of num (excluding num itself)
    for i in range(1, num):
        if num % i == 0:  # If i is a divisor
            sum += i      # Add to sum

    # Check if the number is perfect
    if sum == num:
        print(num, "is a Perfect Number")

print("-------") 

strt = int(input("enter the number: "))
end = int(input("enter the number: "))

for num in range(strt, end + 1):
    sum = 0
    temp = num
    while num > 0:
        last = num % 10
        sum = sum + last * last * last
        num = num // 10
    if sum == temp:
        print(temp)

        

