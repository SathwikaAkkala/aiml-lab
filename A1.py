import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = float('inf')  # Cost from start to this node
        self.h = 0  # Heuristic cost from this node to goal
        self.f = float('inf')  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)  # Manhattan distance

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()
    
    start_node = Node(start[0], start[1])
    start_node.g = 0
    start_node.h = heuristic(start_node, Node(goal[0], goal[1]))
    start_node.f = start_node.h
    
    goal_node = Node(goal[0], goal[1])
    
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if (current.x, current.y) == (goal_node.x, goal_node.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        
        closed_set.add((current.x, current.y))
        
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dx, dy in neighbors:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = Node(nx, ny, current)
                if (nx, ny) in closed_set:
                    continue
                
                tentative_g = current.g + 1
                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = heuristic(neighbor, goal_node)
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in open_set:
                        heapq.heappush(open_set, neighbor)
    
    return None

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
print("Path found:", path)
