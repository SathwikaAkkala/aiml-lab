import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x, self.y, self.parent = x, y, parent
        self.g = self.h = self.f = float('inf')
    
    def __lt__(self, other): return self.f < other.f

def astar(grid, s, g):
    def heuristic(a, b): return abs(a.x - b.x) + abs(a.y - b.y)
    
    rows, cols = len(grid), len(grid[0])
    open_set, closed_set = [], set()
    
    start, goal = Node(*s), Node(*g)
    start.g = start.f = heuristic(start, goal)
    
    heapq.heappush(open_set, start)
    
    while open_set:
        cur = heapq.heappop(open_set)
        if (cur.x, cur.y) == (goal.x, goal.y):
            path = []
            while cur:
                path.append((cur.x, cur.y))
                cur = cur.parent
            return path[::-1]
        
        closed_set.add((cur.x, cur.y))
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cur.x + dx, cur.y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not grid[nx][ny] and (nx, ny) not in closed_set:
                neighbor = Node(nx, ny, cur)
                t_g = cur.g + 1
                if t_g < neighbor.g:
                    neighbor.g, neighbor.h = t_g, heuristic(neighbor, goal)
                    neighbor.f = neighbor.g + neighbor.h
                    heapq.heappush(open_set, neighbor)
    return None

# Example usage
grid = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
print("Path found:", astar(grid, (0, 0), (4, 4)))
