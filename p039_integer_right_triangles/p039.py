"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}`

For which value of p <= 1000, is the number of solutions maximised?
"""

from collections import defaultdict

if __name__ == '__main__':
    # initial thoughts
    # check for p in range(3, 1001)
    # store p, number of solutions
    # constraint is a + b + c = p
    # additional constraint is a^2 + b^2 = c^2

    solutions_by_p = defaultdict(lambda: 0)

    for p in range(3, 1001):
        for c in range(1, p-2):
            for a in range(1, c/2):
                b = p - c - a
                if a**2 + b**2 == c**2:
                    solutions_by_p[p] += 1

    sorted_solutions = sorted(solutions_by_p.items(), key=lambda x: x[1],
        reverse=True)
    print 'answer: {}'.format(sorted_solutions[0][0])
