nth_number = int(input("Enter the nth number: ").strip())
sum_evenNumber = 0
for num in range(1 , nth_number+1):
    if num % 2 == 0:
        sum_evenNumber += num

print(sum_evenNumber)