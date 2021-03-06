# solvegrid.py
# This solves the total number of possible solutions
# Daniel Kogan, 07/09/2020

import itertools,math

def solved_(n):
    num = len(solve(n))
    return int(num/(n+1))


def solve(n): # slow
    directions = [0, 1] * n
    dup_sol = list(itertools.permutations(directions))
    sol = []
    [sol.append(x) for x in dup_sol if x not in sol] # filters out duplicates
    #sol = [x for x in sol if not x[0] == 1] # filters out solutions starting with 1
    return sol


def solved_efficient(n):
    num = pascal(2*n,n)
    return int(num/(n+1))


def pascal(n,k): # Solves the center of the pascal triangle, which we need
    top = math.factorial(n)
    k_fac = math.factorial(k)
    bottom = (k_fac)*math.factorial(n-k)
    return (top/bottom)

if __name__ == '__main__':
    for n in range(1,20):
        print(f"for a {n}x{n} grid, there are {solved_efficient(n)} possible solutions")
