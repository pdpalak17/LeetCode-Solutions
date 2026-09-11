from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        return len(set(
            a*100+b*10+c
            for a,b,c in permutations(digits,3)
            if a!=0 and c%2==0
        ))        