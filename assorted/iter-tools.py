import itertools

# https://leetcode.com/problems/wiggle-subsequence/discuss/84921/3-lines-O(n)-Python-with-explanationproof

print "-- understanding group by ---"
nums=[4, 10, 7, 11, 13, 13, 17, 19, 23, 20, 17]
norep = [num for num, _ in itertools.groupby(nums)]
triples = zip(norep, norep[1:], norep[2:])