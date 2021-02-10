def distance(c, d):
    return abs(c[0] - d[0]) + abs(c[1] - d[1])


n = int(input())
cities = []
for _ in range(n):
    x, y = map(int, input().split())
    cities.append((x, y))
k = int(input())
a, b = map(int, input().split())
roads = 0
for i in range(b - a + 1):
    if distance(a, cities[i]) > k:
        pass