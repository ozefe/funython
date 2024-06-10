# A program to find Pi using the sum of Leibniz-Madhava Series[0][1]
# 
# In mathematics, the Leibniz formula for Pi, named after Gottfried Leibniz, states
# that 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = Pi/4, an alternating series.
#
# [0] - https://en.wikipedia.org/w/index.php?title=Leibniz_series
# [1] - https://www.codebymath.com/index.php/welcome/challenge/pi-sum

print(f'\u03C0 = {4*sum((1, 0, -1)[n%-4]/n for n in range(1, 101, 2))}')
