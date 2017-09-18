import random


class Node:
    def __init__(self, name):
        self._name = name
        self._occupied = False
        self._pawn = None
        self._connected_to = list()

    def __repr__(self):
        return self._name

    def get_name(self):
        return self._name

    def get_occupied(self):
        return self._occupied

    def set_pawn(self, pawn):
        self._pawn = pawn
        self._occupied = True

    def get_pawn(self):
        return self._pawn

    def get_connected_to(self):
        return self._connected_to

    def add_connection(self, edge):
        self._connected_to.append(edge)

    def remove_pawn(self):
        self._pawn = None
        self._occupied = False


class Edge:
    def __init__(self, a, b, name=""):
        self._connection = [a, b]
        self._name = name

    def check_if_connect(self, name):
        if self._connection[0].get_name() == name or self._connection[1].get_name() == name:
            return True
        return False

    def __repr__(self):
        return self._name

    def get_name(self):
        return self._name

    def get_connection(self):
        return self._connection


class Board:
    def __init__(self):
        self._node_list = list()
        self._edge_list = list()
        self._matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.generate_board()

    def generate_board(self):
        temp = Node("0")
        created = ""
        start = temp
        self._node_list.append(temp)
        edge_name = 'a'
        edge_int = ord(edge_name)
        for i in range(1, 8):
            created = Node(str(i))
            self._node_list.append(created)
            edge = Edge(created, temp, edge_name)
            created.add_connection(edge)
            temp.add_connection(edge)
            self._edge_list.append(edge)
            temp = created
            edge_int += 1
            edge_name = chr(edge_int)
        edge = Edge(created, start, edge_name)
        start.add_connection(edge)
        created.add_connection(edge)
        self._edge_list.append(edge)
        center_node = Node("8")
        self._node_list.append(center_node)

        for i in range(0, 8):
            edge_int += 1
            edge_name = chr(edge_int)
            edge = Edge(self._node_list[i], center_node, edge_name)
            center_node.add_connection(edge)
            self._node_list[i].add_connection(edge)
            self._edge_list.append(edge)

    def display_matrix(self):
        for i in self.get_node_list():
            if i.get_pawn() is None:
                num = int(i.get_name())
                if num == 0:
                    self._matrix[2][0] = 0
                elif num == 1:
                    self._matrix[2][1] = 0
                elif num == 2:
                    self._matrix[2][2] = 0
                elif num == 3:
                    self._matrix[1][2] = 0
                elif num == 4:
                    self._matrix[0][2] = 0
                elif num == 5:
                    self._matrix[0][1] = 0
                elif num == 6:
                    self._matrix[0][0] = 0
                elif num == 7:
                    self._matrix[1][0] = 0
                elif num == 8:
                    self._matrix[1][1] = 0
            else:
                tile_name = i.get_pawn().get_controller() + " " + i.get_pawn().get_name()
                num = int(i.get_name())
                if num == 0:
                    self._matrix[2][0] = tile_name
                elif num == 1:
                    self._matrix[2][1] = tile_name
                elif num == 2:
                    self._matrix[2][2] = tile_name
                elif num == 3:
                    self._matrix[1][2] = tile_name
                elif num == 4:
                    self._matrix[0][2] = tile_name
                elif num == 5:
                    self._matrix[0][1] = tile_name
                elif num == 6:
                    self._matrix[0][0] = tile_name
                elif num == 7:
                    self._matrix[1][0] = tile_name
                elif num == 8:
                    self._matrix[1][1] = tile_name
        for i in self._matrix:
            print(i)

    def assign_pawn_to_board(self, player1, player2):
        n = 0
        for i in range(len(player1.get_pawn())):
            self._node_list[n].set_pawn(player1.get_pawn()[n])
            self._node_list[n + 4].set_pawn(player2.get_pawn()[n])
            n += 1

    def possible_move(self, node):
        legal_edge = list()
        connection = node.get_connected_to()
        for i in connection:
            if i.get_connection()[0].get_name() == node.get_name():
                temp_node = i.get_connection()[1]
            else:
                temp_node = i.get_connection()[0]
            if temp_node.get_pawn() is None:
                legal_edge.append(temp_node.get_name())
        return legal_edge

    def pawn_transition(self, current_state, next_state, player=""):
        legal_edge = self.possible_move(current_state)
        if current_state.get_pawn() is None:
            raise Exception("That tile does not have any pawn")
        if next_state.get_pawn() is not None:
            raise Exception("Node is occupied")
        if player != "" and current_state.get_pawn().get_controller() != player:
            raise Exception("That is not your pawn !")
        if next_state.get_name() not in legal_edge:
            raise Exception("You cannot move your pawn to that tile")
        temp = current_state.get_pawn()
        current_state.remove_pawn()
        next_state.set_pawn(temp)

    def get_node_list(self):
        return self._node_list

    def get_edge_list(self):
        return self._edge_list

    def win_cond(self):
        if self.check_row():
            return True
        elif self.check_column():
            return True
        elif self.check_diagonal():
            return True
        return False

    def check_row(self):
        first = [0, 1, 2]
        second = [7, 8, 3]
        third = [6, 5, 4]

        row = [first, second, third]

        for i in range(len(row)):
            j = row[i]
            if i == 0 and self.initial_state("Human"):
                continue
            elif i == 2 and self.initial_state("AI"):
                continue
            else:
                temp_node = self.get_node_list()[j[0]].get_pawn()
                if temp_node is None:
                    continue
                controller_temp = temp_node.get_controller()
                if self.get_node_list()[j[1]].get_pawn() is not None and self.get_node_list()[
                    j[2]].get_pawn() is not None:
                    if controller_temp == str(
                            self.get_node_list()[j[1]].get_pawn().get_controller()) and controller_temp == str(
                        self.get_node_list()[j[2]].get_pawn().get_controller()):
                        return True
        return False

    def check_column(self):
        first = [0, 6, 7]
        second = [1, 5, 8]
        third = [2, 3, 4]

        column = [first, second, third]

        for i in column:
            temp_node = self.get_node_list()[i[0]].get_pawn()
            if temp_node is None:
                continue
            controller_temp = temp_node.get_controller()
            if self.get_node_list()[i[1]].get_pawn() is not None and self.get_node_list()[i[2]].get_pawn() is not None:
                if controller_temp == str(
                        self.get_node_list()[i[1]].get_pawn().get_controller()) and controller_temp == str(
                    self.get_node_list()[i[2]].get_pawn().get_controller()):
                    return True
        return False

    def check_diagonal(self):
        bottom_left_upper_right = [0, 4, 8]
        bottom_right_upper_left = [2, 6, 8]

        diagonal = [bottom_left_upper_right, bottom_right_upper_left]

        for i in diagonal:
            temp_node = self.get_node_list()[i[0]].get_pawn()
            if temp_node is None:
                continue
            controller_temp = temp_node.get_controller()
            if self.get_node_list()[i[1]].get_pawn() is not None and self.get_node_list()[i[2]].get_pawn() is not None:
                if controller_temp == str(
                        self.get_node_list()[i[1]].get_pawn().get_controller()) and controller_temp == str(
                    self.get_node_list()[i[2]].get_pawn().get_controller()):
                    return True
        return False

    def initial_state(self, player):
        human_player = [0, 1, 2]
        ai_player = [4, 5, 6]

        rng = human_player
        if player == "AI":
            rng = ai_player
        expected = ""
        for i in range(3):
            expected += player
        temp = ""
        for i in rng:
            if self.get_node_list()[i].get_pawn() is None:
                continue
            else:
                temp += self.get_node_list()[i].get_pawn().get_controller()
        if temp == expected:
            return True
        return False


class Pawn:
    def __init__(self, name, controller="None"):
        self._name = name
        self._controller = controller

    def get_name(self):
        return self._name

    def get_controller(self):
        return self._controller

    def __repr__(self):
        return self._name


class Player:
    _pawn_name = ['A', 'B', 'C']

    def __init__(self, controller=""):
        self._pawn_list = list()
        for i in self._pawn_name:
            self._pawn_list.append(Pawn(i, controller))

    def get_pawn(self):
        return self._pawn_list

    def test_pawn(self):
        for i in self._pawn_list:
            print(i.get_name() + " " + i.get_controller())


class Human(Player):
    def __init__(self):
        (super(Human, self).__init__("Human"))


class AI(Player):
    def __init__(self):
        (super(AI, self).__init__("AI"))


''''
board = Board()
print("Test Node : ")
board.test_node()
print("\nTest Edge : ")
board.test_edge()
print("\nTest each Node in Edge : ")
board.test_node_in_edge()
print("\nTest Connection each Node : ")
board.test_connection()

human = Human()
print("\nTest Human Pawn : ")
human.test_pawn()

ai = AI()
print("\nTest AI Pawn : ")
ai.test_pawn()

board.assign_pawn_to_board(human, ai)
print("\nTest Assign Pawn to Board : ")
board.test_node_assigned()

print("\nTest Possible Move : ")
board.test_possible_move()

print("\nTest Pawn Transition:")
board.pawn_transition(board.get_node_list()[0],board.get_node_list()[7])
board.test_node_assigned()

print(board.check_column())
print(board.check_diagonal())
print(board.check_row())

board.pawn_transition(board.get_node_list()[0], board.get_node_list()[7])
board.pawn_transition(board.get_node_list()[1], board.get_node_list()[8])
board.pawn_transition(board.get_node_list()[2], board.get_node_list()[3])
print(board.check_row())

board = temp_board
board.assign_pawn_to_board(human, ai)
board.pawn_transition(board.get_node_list()[0], board.get_node_list()[7])
board.pawn_transition(board.get_node_list()[6], board.get_node_list()[8])
board.pawn_transition(board.get_node_list()[7], board.get_node_list()[6])
board.pawn_transition(board.get_node_list()[8], board.get_node_list()[3])
board.pawn_transition(board.get_node_list()[1], board.get_node_list()[8])
print(board.check_diagonal())

board = temp_board
board.assign_pawn_to_board(human, ai)
board.pawn_transition(board.get_node_list()[0], board.get_node_list()[7])
board.pawn_transition(board.get_node_list()[6], board.get_node_list()[8])
board.pawn_transition(board.get_node_list()[7], board.get_node_list()[6])
board.pawn_transition(board.get_node_list()[8], board.get_node_list()[3])
board.pawn_transition(board.get_node_list()[1], board.get_node_list()[0])
board.pawn_transition(board.get_node_list()[5], board.get_node_list()[8])
board.pawn_transition(board.get_node_list()[2], board.get_node_list()[1])
board.pawn_transition(board.get_node_list()[4], board.get_node_list()[5])
board.pawn_transition(board.get_node_list()[0], board.get_node_list()[7])
board.pawn_transition(board.get_node_list()[5], board.get_node_list()[4])
board.pawn_transition(board.get_node_list()[1], board.get_node_list()[0])
print(board.check_column())
'''

board = Board()
temp_board = board
human = Human()
ai = AI()
board.assign_pawn_to_board(human, ai)


def main():
    first_turn = "Human"
    if random.random() > 0.5:
        first_turn = "AI"

    if first_turn == "Human":
        turn = ["Human", "AI"]
    else:
        turn = ["AI", "Human"]

    now = turn[0]
    while (True):
        print("Now is {} turn\n".format(now))
        board.display_matrix()
        current_tile = int(input("Choose your tile to move :"))
        next_tile = int(input("Choose your next tile :\n"))

        board.pawn_transition(board.get_node_list()[current_tile], board.get_node_list()[next_tile], now)

        if now == "Human":
            now = "AI"
        else:
            now = "Human"
