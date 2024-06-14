# A program that calculates sum of the squares of the first 100 integers and
# subtracts the squares of the sum of the same integers[0]
#
# [0] - https://www.codebymath.com/index.php/welcome/challenge/sum-square-difference

print(sum(r := range(1, 101))**2 - sum([i**2 for i in r]))
