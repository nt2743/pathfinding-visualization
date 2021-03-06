from Node import Node
import math
import random

class Board:
    def __init__(self, rows, columns):
        self.rows = (rows)
        self.columns = (columns)
        self.nodes = [[Node(row, column, "node") for column in
                      range(self.columns)] for row in range(self.rows)]

        self.start_row = math.floor(self.rows / 2)
        self.start_column = math.floor(self.columns / 4)
        self.start_node = Node(self.start_row, self.start_column, "start")
        self.nodes[self.start_row][self.start_column] = self.start_node

        self.finish_row = math.floor(self.rows / 2)
        self.finish_column = math.floor(self.columns / 4 * 3)
        self.finish_node = Node(self.finish_row, self.finish_column, "finish")
        self.nodes[self.finish_row][self.finish_column] = self.finish_node

    def get_neighbors(self, node):
        neighbors = []
        row = node.row
        column = node.column
        if row > 0: neighbors.append(self.nodes[row - 1][column])
        if row < self.rows - 1: neighbors.append(self.nodes[row + 1][column])
        if column > 0: neighbors.append(self.nodes[row][column - 1])
        if column < self.columns - 1: neighbors.append(self.nodes[row][column + 1])
        return neighbors

    def calculate_distance_to_finish(self, node):
        node.distance_to_finish = int(math.fabs(self.finish_row - node.row) + math.fabs(self.finish_column - node.column))

    def create_border(self):
        border = []
        for row in range(self.rows):
            self.nodes[row][0].state = "wall"
            border.append(self.nodes[row][0])
            self.nodes[row][self.columns-1].state = "wall"
            border.append(self.nodes[row][self.columns-1])
        for column in range(self.columns):
            self.nodes[0][column].state = "wall"
            border.append(self.nodes[0][column])
            self.nodes[self.rows-1][column].state = "wall"
            border.append(self.nodes[self.rows-1][column])
        return border

    def create_random_maze_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.nodes[row][column].state != "start" and self.nodes[row][column].state != "finish":
                    random_number = random.uniform(0, 1)
                    if random_number > 0.7:
                        self.nodes[row][column].state = "wall"
                    else:
                        self.nodes[row][column].state = "node"

    def reset_after_algorithm(self):
        for row in range(self.rows):
            for column in range(self.columns):
                node = self.nodes[row][column]
                node.is_visited = False
                node.previous_node = None
                node.distance_to_finish = math.inf
                if node.state == "visited" or node.state == "path":
                    node.state = "node"