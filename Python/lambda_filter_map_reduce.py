# A Function without name also known as Anonymous function and also Lambda
# It's useful to create simple expression and single line of code
## Example
from functools import reduce
numbers=[2,3,1,4,9,6,7,8]

def even_number(n):
    return n%2==0

## With Filter
evens = list(filter(even_number,numbers))
print(f"With Filter Even Number Is: {evens}")

## With Filter and Lambda
evens = list(filter(lambda n : n%2==0,numbers))
print(f"With Filter and Lambda Even Number Is: {evens}")

## With Map and Lamda
multiple_data = list(map(lambda n : n * 2, evens))
print(f"With Map and Lambda Double Even Number Is: {multiple_data}")

## Reduce and Lamda
reduce_data = reduce(lambda a,b : a+b, multiple_data)
print(f"With Reduce and Lambda Sum of Doubled Even Number Is: {reduce_data}")
