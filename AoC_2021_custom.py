def work(n): # function to calculate the divisor of a number
    divisors = []
    for i in range(1,n):#try all numbers between 2 and the number
        if n % i == 0:
            divisors.append(i)

    divisors[0] = 1 # the first divisor will always be one
    if n > 1: #only if the number is larger than 1 the last divisor will be the same number
        divisors.append(n)
    print(f"{n} -> {divisors}")
print("Advent of Code 2021: https://github.com/seldoncode/AdventOfCode2021/blob/main/days__option_A.ipynb ")
print("ROCÍO PERALES VALDÉS", "\n", "\n")
frange = int(input("Give me the first number of a range to extract divisors of: "))
lrange = int(input("Now please give me the last number of a range to extract divisors of: "))

for i in range(frange,lrange+1):
    work(i)