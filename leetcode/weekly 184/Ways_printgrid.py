# Number of Ways to Paint N × 3 Grid
# https://leetcode.com/contest/weekly-contest-184/problems/number-of-ways-to-paint-n-3-grid/

MOD = 10 ** 9 + 7

def numOfWays(self, n: int) -> int:
    s, d, sr, dr, ss, ds = 2, 2, 5, 4, 3, 2
    while n > 1:
        t1 = (s * ss) + (d * ds)
        t2 = (s * (sr - ss)) + (d * (dr - ds))
        s, d = t1, t2
        n -= 1
    return (s + d) * 3 % self.MOD