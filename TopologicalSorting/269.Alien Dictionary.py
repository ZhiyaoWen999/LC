
'''
这道题关键在于如何建图
'''
import collections
from typing import List

def alienOrder(words: List[str]) -> str:
    adj = collections.defaultdict(set)
    
    indegrees = {}

    for word in words:
        for c in word:
            if c in indegrees:
                continue
            indegrees[c] = 0

    for pre, cur in zip(words, words[1:]):
        for c, d in zip(pre, cur):
            if c != d:
                
                if d not in adj[c]:
                    adj[c].add(d)
                    indegrees[d] += 1
        else:
            # check if the second word is none
            if len(cur) < len(pre):
                return ""
            
    q = collections.deque()
    for k, v in indegrees.items():
        if v == 0:
            q.append(k)

    res = []

    while q:
        c = q.popleft()
        res.append(c)

        for d in adj[c]:
            indegrees[d] -= 1
            if indegrees[d] == 0:
                q.append(d)

    # if there is cycle, which means indegrees is not 0 before, so res will < indegrees
    if len(res) < len(indegrees):
        return ""
    
    return "".join(res)