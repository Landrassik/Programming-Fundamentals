def backward_as_forward(num):
   if num == num[::-1]:
       return True
   return False


line_at_numbers = input().split(', ')
for index_in_line in line_at_numbers:
    result = backward_as_forward(index_in_line)
    print(result)

