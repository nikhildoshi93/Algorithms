# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        buffer = deque()                        
        td = {}
        
        for task in tasks:
            if task in td:
                td[task] += 1
            else:
                td[task] = 1
        
        hp = [(-v, k) for k,v in td.items()]
        heapq.heapify(hp)
        
        res = 0
        vals = len(tasks)
        penalty = 0
        while (len(hp) != 0 or vals != 0):
            if (len(buffer) > n):
                left = buffer.popleft()
                if left == -1:
                    penalty -= 1
                    continue
                elif left != 1:
                    heapq.heappush(hp, left)
                else:
                    continue
            if len(hp) >= 1:
                v, k = heapq.heappop(hp)
                v = -v
                if (v > 1):
                    buffer.append((-(v-1), k))
                else:
                    buffer.append(1)
                res += 1
                vals -= 1
            else:
                buffer.append(-1)
                res += 1
                penalty += 1
            
        return res
    
