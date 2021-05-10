# Problem:
# N cities, M roads. M lines of roads-from followed by M lines of roads-to.
# Condition: For each road, if X < Y then X+1,X+2,...,Y-1 should be connected to X (need not be directly).
# Find minimum number of roads to be built to satisfy this condition.

def minRoads(lines):
    roads = []
    n = int(lines[0])
    m = int(lines[1])
    for i in range(m):
        roads += [(lines[i + 2], lines[m + i + 2])]
    newRoads = {}
    extensions = {}
    for i, j in roads:
        if i > j:
            i, j = j, i
        for k in range(i+1, j):
            if (k-1, k) not in roads and (k-1, k) not in extensions:
                newRoads[(k-1, k)] = 1
        extensions[(j-1, j)] = 1
    return len(newRoads)


print(minRoads([3, 1, 1, 3]))
print(minRoads([6, 2, 1, 2, 4, 6]))
print(minRoads([5, 3, 1, 2, 5, 3, 4, 3]))
print(minRoads([4, 3, 1, 2, 3, 2, 3, 4]))

# Answer: 1, 3, 1, 0
