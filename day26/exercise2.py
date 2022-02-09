def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))  #1.5출력
print(avg_numbers(1, 2, 3, 4, 5))   #3.0출력