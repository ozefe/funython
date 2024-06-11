# A program to show that sin(x)**2 + cos(x)**2 = 1 (Pythagorean Trigonometric Identity)[0][1]
# using the bruteforce-ish method of looping through x -> inf
#
# [0] - https://en.wikipedia.org/wiki/Pythagorean_trigonometric_identity
# [1] - https://www.codebymath.com/index.php/welcome/challenge/trig-identity

from math import sin, cos

print(*(f'{x} => {sin(x)**2 + cos(x)**2 = :.0f}'.replace('x', str(x)) for x in range(1000)), sep='\n')
