'''
解题思路：
构件图，BFS遍历节点，每一层的节点不能有两种选择。

'''
from collections import deque
import functools
from typing import List


def sequenceReconstruction(org:List[int], seqs:List[List[int]]) -> bool:
    #edge case handle
    #the unique nodes are in org mush queal seqs 
    nodes = functools.reduce(set.union, seqs, set()) #reduce process for particular function
    if nodes != set(org):
        return False
    
    n = len(org)
    adj = [[] for _ in range(n+1)]
    indegrees = [0] * (n+1)

    for seq in seqs:
        for pre, cur in zip(seq, seq[1:]):
            adj[pre].append(cur)
            indegrees[cur] += 1
    
    q = deque([node for node in org if indegrees[node] == 0])
    order = []

    while q:
        
        #volitate the first level that has one selective node
        if len(q) != 1:
            return False
        node = q.popleft()
        order.append(node)

        for next_node in adj[node]:
            indegrees[next_node] -= 1
            if not indegrees[next_node]:
                q.append(next_node)
    return org == order


if __name__ == "__main__":
    org = [4,1,5,2,6,3]
    seqs = [[5,2,6,3], [4,1,5,2]]
    print(sequenceReconstruction(org, seqs))