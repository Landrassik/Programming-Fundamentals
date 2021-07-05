def proper_positive_divisors(num):
    result_i = 0
    for i in range(1, num):

        if num % i == 0:
            result_i += i

    return result_i


numbers = int(input())
result = proper_positive_divisors(numbers)
if result == numbers:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")