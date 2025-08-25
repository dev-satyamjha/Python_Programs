def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def median(numbers):
    numbers.sort()

    n = len(numbers)
    if n%2 == 1:
        return numbers[n//2]
    else:
        mid1 = numbers[n//2 - 1]
        mid2 = numbers[n//2]
        return(mid1+mid2)/2
    
nums = read_numbers("num.txt")
print(median(nums))
