import argparse
import timeit
import resource
from collections import deque
from heapq import heappush, heappop, heapify
import itertools


class State:

    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map


goal_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]
initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
board_len = len(initial_state)
board_side = int(board_len**0.5)
max_frontier_size = 0
goal_node = State
max_search_depth = 0
nodes_expanded = 0
moves = list()


def dfs(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, stack = set(), list([State(start_state, None, None, 0, 0, 0)])
    while stack:
        node = stack.pop()
        explored.add(node.map)
        if node.state == goal_state:
            goal_node = node
            return stack
        neighbors = reversed(expand(node))
        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)
                if neighbor.depth > max_search_depth:
                    max_search_depth += 1
        if len(stack) > max_frontier_size:
            max_frontier_size = len(stack)


def expand(node):
    global nodes_expanded
    nodes_expanded += 1
    neighbors = list()
    neighbors.append(State(move(node.state, 1), node, 1,
                           node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 2), node, 2,
                           node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 3), node, 3,
                           node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 4), node, 4,
                           node.depth + 1, node.cost + 1, 0))
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes


def move(state, position):
    new_state = state[:]
    index = new_state.index(0)
    if position == 1:
        if index not in range(0, board_side):
            temp = new_state[index - board_side]
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 2:
        if index not in range(board_len - board_side, board_len):
            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 3:
        if index not in range(0, board_len, board_side):
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

    if position == 4:
        if index not in range(board_side - 1, board_len, board_side):
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None


def backtrace():
    current_node = goal_node
    while initial_state != current_node.state:
        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'
        moves.insert(0, movement)
        current_node = current_node.parent
    return moves


def export(frontier, time):
    global moves
    moves = backtrace()
    print(f'path to goal: {moves}')
    print(f'cost of path: {len(moves)}')
    print(f'nodes expanded: {nodes_expanded}')
    print(f'fringe_size: {len(frontier)}')
    print(f'max_fringe_size: {max_frontier_size}')
    print(f'search_depth: {goal_node.depth}')
    print(f'max_search_depth: {max_search_depth}')
    print(f'running_time: {time}')


if __name__ == '__main__':
    start = timeit.default_timer()
    frontier = dfs(initial_state)
    stop = timeit.default_timer()
    export(frontier, stop-start)
