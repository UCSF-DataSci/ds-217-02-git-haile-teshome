limit = 1000

def sum_of_multiples(limit):
    return sum([num for num in range(limit) if num % 3 == 0 or num % 5 == 0])

result = sum_of_multiples(limit)
print(f"The sum of multiples of 3 or 5 at or below the {limit} is {result}")