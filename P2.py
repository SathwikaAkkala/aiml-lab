import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, prev=None):
        self.board = board
        self.goal = goal
        self.blank_pos = board.index('*')
        self.moves = moves
        self.prev = prev

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def heuristic(self):
        """ Calculate Manhattan Distance """
        goal_positions = {i: (i // 3, i % 3) for i in range(1, 9)}
        goal_positions['*'] = (2, 2)  # The goal position for the empty tile
        distance = 0
        
        for i in range(9):
            tile = self.board[i]
            if tile == '*':
                continue
            tile = int(tile)  # Convert tile to integer for comparison
            goal_pos = goal_positions[tile]
            cur_pos = (i // 3, i % 3)
            distance += abs(cur_pos[0] - goal_pos[0]) + abs(cur_pos[1] - goal_pos[1])
        
        return distance

    def get_neighbors(self):
        """ Generate neighboring states by moving the blank tile """
        neighbors = []
        r, c = divmod(self.blank_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_blank_pos = nr * 3 + nc
                new_board = list(self.board)
                new_board[self.blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[self.blank_pos]
                neighbors.append(PuzzleState(tuple(new_board), self.goal, self.moves + 1, self))
        
        return neighbors

    def is_goal(self):
        return self.board == self.goal

    def __repr__(self):
        return '\n'.join([' '.join(map(str, self.board[i:i+3])) for i in range(0, 9, 3)])

def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, start_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        closed_set.add(current_state.board)

        for neighbor in current_state.get_neighbors():
            if neighbor.board in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def get_user_input(prompt):
    """ Get a state from user input with validation """
    print(prompt)
    input_str = input().strip()
    input_list = input_str.split()
    
    if len(input_list) != 9 or '*' not in input_list or len(set(input_list)) != 9:
        raise ValueError("Invalid input. Make sure you enter exactly 9 values with numbers 1-8 and one '*' for the empty space.")

    return tuple(input_list)

# Main execution
if __name__ == "__main__":
    try:
        start_board = get_user_input("Enter the start state (9 values with numbers 1-8 and '*' for empty space):")
        goal_board = get_user_input("Enter the goal state (9 values with numbers 1-8 and '*' for empty space):")

        if start_board == goal_board:
            raise ValueError("Start state cannot be the same as the goal state.")

        start = PuzzleState(start_board, goal_board)
        solution = a_star(start)

        if solution:
            path = []
            while solution:
                path.append(solution)
                solution = solution.prev
            for state in reversed(path):
                print(state)
                print()
        else:
            print("No solution found.")
    except ValueError as e:
        print(e)
