class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        row,coins_sum=1,1
        while n>coins_sum:
            row+=1
            coins_sum=coins_sum+row
        if n==coins_sum:
            return row
        return row-1