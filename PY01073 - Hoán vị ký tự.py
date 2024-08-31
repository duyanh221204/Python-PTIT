import sys
from itertools import permutations

s = input().strip()
ans = ["".join(i) for i in permutations(s)]
sys.stdout.write ("\n".join(ans))
