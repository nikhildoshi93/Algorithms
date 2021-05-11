## Problem - https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-revisited-9e1091ea/
# In the country of HackerEarth, there are N cities and M bi - directional roads. We need to transport essential items from City 1  to all other cities. (There exists a path always)

# But every road has some positive amount of Toll Charge associated with it say C (it is not same for all roads). We need to find the minimum amount of charge that it required to deliver essential items for each city.

# Fortunately, to our rescue we have K special offers, which means while travelling from City 1 to any other city we can select at-most K roads and we will not be charged for using those roads. 

# Can you now find the minimum charge that we have to pay to deliver essential items for each city.

# (Remember we require to provide answers for each destination city separately i.e. we have K offers for every city and not as a whole)

# Input :
# 1. First line contain three integers N M K.
# 2. Next M lines contain three integers U V W, denoting a road between city U and city v with Toll Charge W.

# Constraints :





# Output :
# Print N space separated integers , denoting the minimum charge we require to pay for each city , where first integer represent cost for City 1, second for City 2 and so on.

# Sample Input
# 5 6 1
# 1 2 2
# 1 3 6
# 2 4 6
# 2 5 8
# 3 5 4
# 4 5 1
# Sample Output
# 0 0 0 2 2
# Time Limit: 3
# Memory Limit: 256
# Source Limit:
# Explanation
# For City 1 , we are already there charge is 0.
# For City 2 , we can reach with charge 0, by using 1 special offer for road 1 - 2.
# For City 3 , we can reach with charge 0, by using 1 special offer for road 1 - 3.
# For City 4 , we can reach with charge 2, by using path 1 - 2 - 4 , and using 1 offer for road 2 - 4.
# For City 5 , we can readh with charge 2, by using path 1 - 2 - 5 , and using 1 offer for road 2 - 5.



graph = {}

n, r, lim = [int(i) for i in raw_input().split(' ')]
while True:
    try:
        x, y, k = [int(i) for i in raw_input().split(' ')]
        x -= 1
        y -= 1
        graph[x] = [(y, k)] if (x not in graph) else (graph[x] + [(y, k)])
        graph[y] = [(x, k)] if (y not in graph) else (graph[y] + [(x, k)])
    except:
        break

# dp = {}
# def find_min(curr, dest, best, k, visited):
#     if curr == dest:
#         return best
#     if (curr, dest, k) in dp:
#         return dp[(curr, dest, k)]
#     roads = []
#     for v, cost in graph[curr]:
#         if v not in visited:
#             road_not_taken = find_min(v, dest, best + cost, k, visited + [v])
#             if k:
#                 road_taken = find_min(v, dest, best, k-1, visited + [v])
#                 roads.append((road_taken, curr, v, k-1))
#             roads.append((road_not_taken, curr, v, k))
#     if roads:
#         cost, a, b, c = min(roads)
#         dp[(a, b, c)] = cost
#         return cost
#     return float('inf')

# fees = "0"
# for v in range(1, n):
#     fees += " " + str(find_min(0, v, 0, lim, []))

# print(fees)



dist = [-1 for i in range(n)]
prev = [-1 for i in range(n)]
dist[0] = 0
prev[0] = 0

unvisited = list(range(n))

dp = {}
for i in range(0, lim + 1):
    dp[(0, i)] = 0

def find_min(lst):
    minVx = lst[0]
    currMin = dp.get((minVx, lim), float('inf'))

    for v in lst:
        if (currMin == float('inf') or
            (dp.get((v, lim), float('inf')) != float('inf') and dp.get((v, lim)) < currMin)):
            currMin = dp.get((v, lim), float('inf'))
            minVx = v
    return minVx

    # currMin = dist[minVx]

    # for v in lst:
    #     if (currMin == -1 or
    #         (dist[v] != -1 and dist[v] < currMin)):
    #         currMin = dist[v]
    #         minVx = v
    
    # return minVx


visited = []
queue = [0]
while queue:
    minVx = queue[0]
    queue = queue[1:]
    visited.append(minVx)
# while (unvisited):
#     minVx = find_min(unvisited)
#     # minVx, skips = unvisited[0]
#     # unvisited = unvisited[1:]
#     unvisited.remove(minVx)
    
    for v, k in graph[minVx]:
        if v not in visited:
            queue.append(v)
        doFor = list(range(1, lim + 1))
        doFor.reverse()
        for i in doFor:
            dp[(v, i)] = min(dp[(minVx, i - 1)], dp.get((v, i), float('inf')))
            dp[(v, i - 1)] = min(dp[(minVx, i - 1)] + k, dp.get((v, i - 1), float('inf')))
            
        
        # proposal = dist[minVx] + k
        # if (dist[v] == -1 or dist[v] > proposal):
        #     dist[v] = proposal
        #     prev[v] = minVx

# concession = []
# for v in range(n):
#     distances = []
#     curr = v
#     while (curr != 0):
#         distances.append(dist[curr])
#         curr = prev[curr]
#     distances.sort()

#     newSum = 0
#     for i in range(len(distances) - lim):
#         newSum += distances[i]
#     print(distances, v, newSum)
#     concession.append(newSum)


# print(prev)
# print(dist)
# print(concession)
# print(dp)

out = "0"
for i in range(1, n):
    out += " " + str(dp[i, lim])
    # if dp[i, lim] != 0:
    #     print(i)

# for i in range(lim+1):
#     print(dp[65, i])
print(out)
