import copy
import random

"""
Catur Jawa Gameplay

There are Node, Edge, Board, Pawn, Player, Human, and AI class

Using Node and Edge to construct Graph.
Board use graph data structure 
"""


class Node:
    """This is Node class"""

    def __init__(self, name):
        """Node has name, bool occupied, pawn, and edge connected to this node"""
        self._name = name
        self._occupied = False
        self._pawn = None
        self._connected_to = list()
        self._value = 0

    def __repr__(self):
        """Return node name"""
        return self._name

    def getPlayerClick(self):
        return self.player_click

    def setPlayerClick(self, hadClicked):
        self.player_click = hadClicked

    def get_name(self):
        """Return node name"""
        return self._name

    def get_occupied(self):
        """Return bool occupied"""
        return self._occupied

    def set_pawn(self, pawn):
        """Set pawn to this node"""
        self._pawn = pawn
        self._occupied = True

    def get_pawn(self):
        """Return pawn object attached to this node"""
        return self._pawn

    def get_connected_to(self):
        """Return list of edge that connected to this node"""
        return self._connected_to

    def add_connection(self, edge):
        """Add connection to edge"""
        self._connected_to.append(edge)

    def remove_pawn(self):
        """Remove pawn from this node"""
        self._pawn = None
        self._occupied = False


class Edge:
    """This is edge class"""

    def __init__(self, a, b, name=""):
        """Edge connect 2 node and has name"""
        self._connection = [a, b]
        self._name = name

    def check_if_connect(self, name):
        """Return True if connected to node with name same as name in parameter"""
        if self._connection[0].get_name() == name or self._connection[1].get_name() == name:
            return True
        return False

    def __repr__(self):
        """Return edge name"""
        return self._name

    def get_name(self):
        """Return edge name"""
        return self._name

    def get_connection(self):
        """Return list of 2 node"""
        return self._connection


class Board:
    """This is Board class"""

    def __init__(self):
        """
        Board has array of edge and nodes, matrix representation
        After init, generate board
        """
        self._node_list = list()
        self._edge_list = list()
        self._player = dict()
        self._matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self._turn = ""
        self.generate_board()

    def checkEmptyNode(self, node, player):
        nodeCheck = self.select_node(node).get_pawn()
        if (nodeCheck is None):
            return "That tile does not have any pawn"
        elif (nodeCheck.get_controller() != player):
            return "That is not your pawn !"
        else:
            return "Good!"

    def generate_node(self):
        for i in range(0, 9):
            node = Node(str(i))
            self._node_list.append(node)

    def get_latest_edge(self, current, next, edge_int):
        current_node = self.get_node_list()[current]
        next_node = self.get_node_list()[next]
        edge = Edge(current_node, next_node, chr(edge_int))
        current_node.add_connection(edge)
        next_node.add_connection(edge)
        self._edge_list.append(edge)
        edge_int += 1
        return chr(edge_int)

    def generate_row(self, edge_name):
        for i in range(0, 3):
            for j in range(0, 2):
                current = i * 3 + j
                next = i * 3 + j + 1
                edge_name = self.get_latest_edge(current, next, ord(edge_name))
        return edge_name

    def generate_collumn(self, edge_name):
        for i in range(0, 3):
            for j in range(0, 2):
                current = i + j * 3
                next = i + j * 3 + 3
                edge_name = self.get_latest_edge(current, next, ord(edge_name))
        return edge_name

    def generate_diagonal(self, edge_name):
        for i in range(0, 2):
            current = i * 4
            next = i * 4 + 4
            edge_name = self.get_latest_edge(current, next, ord(edge_name))
        for i in range(0, 2):
            current = i * 2 + 2
            next = i * 2 + 4
            edge_name = self.get_latest_edge(current, next, ord(edge_name))
        return edge_name

    def generate_board(self):
        self.generate_node()
        edge_name = 'a'
        edge_name = self.generate_row(edge_name)
        edge_name = self.generate_collumn(edge_name)
        self.generate_diagonal(edge_name)

    def set_turn(self, turn):
        self._turn = turn

    def next_turn(self):
        if self._turn == "Human":
            self._turn = "AI"
        else:
            self._turn = "Human"

    def set_player(self, player_dict):
        self._player = player_dict

    def get_player(self):
        if self._turn == "Human":
            return self._player['Human']
        return self._player['AI']

    def display_matrix(self):
        """Print matrix representation"""

        for i in range(len(self.get_node_list())):
            node = self.get_node_list()[i]
            if node.get_pawn() is None:
                self._matrix[2 - int(i / 3)][i % 3] = 0
            else:
                tile_name = node.get_pawn().get_controller()
                self._matrix[2 - int(i / 3)][i % 3] = tile_name

        return self._matrix

    def assign_pawn_to_board(self, player1, player2):
        """Add pawn to node"""
        n = 0
        for i in range(len(player1.get_pawn())):
            player1.get_pawn()[n].set_coordinate(n)
            player2.get_pawn()[n].set_coordinate(n + 6)
            self._node_list[n].set_pawn(player1.get_pawn()[n])
            self._node_list[n + 6].set_pawn(player2.get_pawn()[n])
            n += 1

    def select_node(self, number):
        """Using number to return selected node from list of node index-number"""
        return self.get_node_list()[number]

    def possible_move(self, node):
        """Return array of node that can be placed with pawn"""
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

    def pawn_moves(self, node):
        """Return array of nodes that can be placed with pawn"""
        return self.possible_move(node)

    def pawn_transition(self, current_state, next_state, player=""):
        """Move player pawn from current node to next node"""
        legal_edge = self.possible_move(current_state)
        if current_state.get_pawn() is None:
            return "That tile does not have any pawn"
        if next_state.get_pawn() is not None:
            return "Node is occupied"
        if player != "" and current_state.get_pawn().get_controller() != player:
            return "That is not your pawn !"
        if next_state.get_name() not in legal_edge:
            return "You cannot move your pawn to that tile"
        temp = current_state.get_pawn()
        temp.set_coordinate(next_state.get_name())
        current_state.remove_pawn()
        next_state.set_pawn(temp)
        return "Good!"

    def get_node_list(self):
        """Return list of node"""
        return self._node_list

    def get_edge_list(self):
        """Return list of edge"""
        return self._edge_list

    def utility(self):
        """Utility for AI"""
        return self.win_cond(True)

    def win_cond(self, isUtility=False):
        """Return integer for utility and bool for check win"""
        if isUtility == True:
            row = self.check_row(True)
            column = self.check_column(True)
            diagonal = self.check_diagonal(True)
            if row[0]:
                return self.controller_checker(row[1])
            elif column[0]:
                return self.controller_checker(column[1])
            elif diagonal[0]:
                return self.controller_checker(diagonal[1])
            return 0
        else:
            if self.check_row():
                return True
            elif self.check_column():
                return True
            elif self.check_diagonal():
                return True
            return False

    def controller_checker(self, controller):
        """Return -1 if human win and 1 if AI win"""
        if controller == "Human":
            return -100
        else:
            return 100

    def check_row(self, isUtility=False):
        """Return True if game ended with row win"""
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]

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
                check_all_same = self.all_same_one_line(j, controller_temp, isUtility)
                if isUtility:
                    if check_all_same[0] != False:
                        return check_all_same
                else:
                    if check_all_same != False:
                        return check_all_same

        if isUtility:
            return [False]
        return False

    def check_column(self, isUtility=False):
        """Return True if game ended with column win"""
        first = [0, 3, 6]
        second = [1, 4, 7]
        third = [2, 5, 8]

        column = [first, second, third]
        return self.line_loop(column, isUtility)

    def check_diagonal(self, isUtility=False):
        """Return True if game ended with diagonal win"""
        bottom_left_upper_right = [0, 4, 8]
        bottom_right_upper_left = [2, 4, 6]

        diagonal = [bottom_left_upper_right, bottom_right_upper_left]
        return self.line_loop(diagonal, isUtility)

    def line_loop(self, lines, isUtility):
        """Return True if game ended with type of lines win"""

        for i in lines:
            temp_node = self.get_node_list()[i[0]].get_pawn()
            if temp_node is None:
                continue
            controller_temp = temp_node.get_controller()

            check_all_same = self.all_same_one_line(i, controller_temp, isUtility)
            if isUtility:
                if check_all_same[0] != False:
                    return check_all_same
            else:
                if check_all_same != False:
                    return check_all_same

        if isUtility:
            return [False]
        return False

    def all_same_one_line(self, i, controller_temp, isUtility):
        """Return True if in one line, 3 pawns have same controller"""
        if self.get_node_list()[i[1]].get_pawn() is not None and self.get_node_list()[i[2]].get_pawn() is not None:
            if controller_temp == str(
                    self.get_node_list()[i[1]].get_pawn().get_controller()) == str(
                self.get_node_list()[i[2]].get_pawn().get_controller()):
                if isUtility:
                    return [True, controller_temp]
                return True
        if isUtility:
            return [False, controller_temp]
        return False

    def initial_state(self, player):
        """Return True if pawns in initial state"""
        human_player = [0, 1, 2]
        ai_player = [6, 7, 8]

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

    @staticmethod
    def print_list(pawn, isPawn=False):
        """Return string from array"""
        pawns = ""
        for i in pawn:
            temp = i
            if isPawn:
                temp = i.get_coordinate()
            pawns += str(temp) + " "
        return pawns

    def moveable_pawn(self, player):
        """Return moveable player pawn"""
        pawn = player.get_pawn()
        nodes = list()
        for i in pawn:
            coordinate = int(i.get_coordinate())
            temp_node = self.select_node(coordinate)
            total_move = len(self.possible_move(temp_node))
            if total_move > 0:
                nodes.append(temp_node.get_pawn())
        return nodes


class Pawn:
    """This is Pawn class"""

    def __init__(self, name, controller="None"):
        """Create obj that have name, controller, and coordinate"""
        self._name = name
        self._controller = controller
        self._coordinate = ""

    def get_name(self):
        """Return pawn name"""
        return self._name

    def get_controller(self):
        """Return pawn controller"""
        return self._controller

    def set_coordinate(self, coordinate):
        """Set coordinate of pawn"""
        self._coordinate = coordinate

    def get_coordinate(self):
        """Return pawn coordinate"""
        return self._coordinate

    def __repr__(self):
        """Return pawn name"""
        return self._name


class Player:
    """This is Player class"""
    _pawn_name = ['A', 'B', 'C']

    def __init__(self, controller=""):
        """Create player obj with pawns controller is sub class obj"""
        self._pawn_list = list()

        for i in self._pawn_name:
            self._pawn_list.append(Pawn(i, controller))

    def get_pawn(self):
        """Return player name"""
        return self._pawn_list

    def set_value(self, value):
        self._value = value

    def get_value(self, value):
        return self._value

    def test_pawn(self):
        """Print player pawn"""
        for i in self._pawn_list:
            print(i.get_name() + " " + i.get_controller())

    def check_pawn(self):
        """Return coordinate for each pawn"""
        nodes = ""
        for i in self.get_pawn():
            nodes += str(i.get_coordinate()) + " "
        return nodes


class Human(Player):
    """This is Human class inherit Player"""

    def __init__(self):
        """Create human obj with pawns controller is Human"""
        (super(Human, self).__init__("Human"))


class AI(Player):
    """This is AI class inherit Player"""

    def __init__(self):
        """Create human obj with pawns controller is AI"""
        (super(AI, self).__init__("AI"))

    def check_row_controller(self, rowOf, current_node, board, controllerValue):
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]
        rows = [first, second, third]
        row = rows[rowOf]
        for i in row:
            if (i != int(current_node)):
                node_pawn = board.get_node_list()[i].get_pawn()
                if node_pawn is not None:
                    pawn_controller = node_pawn.get_controller()
                    if (pawn_controller == "Human"):
                        if (i != 0 or i != 1 or i != 2):
                            controllerValue['human'] += 1
                    elif (pawn_controller == "AI"):
                        if (i != 6 or i != 7 or i != 8):
                            controllerValue['AI'] += 1
        return controllerValue

    def check_diagonal_controller(self, diagonalOf, current_node, board, controllerValue):
        bottom_left_upper_right = [0, 4, 8]
        bottom_right_upper_left = [2, 4, 6]
        diagonals = [bottom_left_upper_right, bottom_right_upper_left]
        diagonal = diagonals[diagonalOf]
        for i in diagonal:
            if (i != int(current_node)):
                node_pawn = board.get_node_list()[i].get_pawn()
                if board.get_node_list()[i].get_pawn() is not None:
                    pawn_controller = node_pawn.get_controller()
                    if (pawn_controller == "Human"):
                        controllerValue['human'] += 1
                    elif (pawn_controller == "AI"):
                        controllerValue['AI'] += 1
        return controllerValue

    def check_column_controller(self, columnOf, current_node, board, controllerValue):
        first = [0, 3, 6]
        second = [1, 4, 7]
        third = [2, 5, 8]
        columns = [first, second, third]

        column = columns[columnOf]
        for i in column:
            if (i != int(current_node)):
                node_pawn = board.get_node_list()[i].get_pawn()
                if node_pawn is not None:
                    pawn_controller = node_pawn.get_controller()
                    if (pawn_controller == "Human"):
                        controllerValue['human'] += 1
                    elif (pawn_controller == "AI"):
                        controllerValue['AI'] += 1
        return controllerValue

    def check_diagonal_helper(self, current_node, board, controllerValue):
        node_num = int(str(current_node))
        if node_num in [0, 2, 6, 8]:
            if node_num % 8 == 0:
                return self.check_diagonal_controller(0, current_node, board, controllerValue)
            return self.check_diagonal_controller(1, current_node, board, controllerValue)
        else:
            firstDict = self.check_diagonal_controller(0, current_node, board, controllerValue)
            secondDict = self.check_diagonal_controller(1, current_node, board, controllerValue)
            firstDict.update(secondDict)
            return firstDict

    def check_controller(self, current_node, board):
        diag = [0, 4, 8, 2, 6]
        node_num = int(str(current_node))
        current_node = str(current_node)
        diagonalDict = {'human': 0, 'AI': 0}
        controllerValue = {'human': 0, 'AI': 0}
        if node_num in diag:
            diagonalDict = self.check_diagonal_helper(current_node, board, controllerValue)
        rowDict = self.check_row_controller(int(node_num / 3), current_node, board, controllerValue)
        colDict = self.check_column_controller(int(node_num % 3), current_node, board, controllerValue)
        total = 2* (3 * rowDict['AI'] + 3 * colDict['AI'] + 2 * diagonalDict['AI']) + -1*(
            3 * rowDict['human'] + 3 * colDict['human'] + 2 * diagonalDict['human'])
        return total

    def getBestMoveValue(self, nodeList, board):
        pawnValueDict = dict()
        for current_node, next_move in list(nodeList.items()):
            pawnValueDict[current_node] = self.check_controller(current_node, board)
        bestValue = 0
        bestPawn = None
        for current_node, value in list(pawnValueDict.items()):
            if (bestPawn == None):
                bestPawn = current_node
            elif (bestValue < pawnValueDict[current_node]):
                bestValue = pawnValueDict[current_node]
                bestPawn = current_node
            elif (bestValue == pawnValueDict[current_node]):
                bestPawnRand, bestValuerand = random.choice(list(pawnValueDict.items()))
                bestPawn = bestPawnRand
        return bestPawn, nodeList[bestPawn]

    def minimax(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        pawns = board.moveable_pawn(board.get_player())
        infinity = float('inf')
        best_score = -infinity
        temp_board = copy.deepcopy(board)
        current_node = very_best_move = 0
        best_move_each_pawn = dict()
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            best_move = moves[0]
            node = board.select_node(int(pawn.get_coordinate()))
            best_move_score = -infinity
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_score = self.min_play(board, limit)
                if move_score > best_move_score:
                    best_move = move
                    best_move_score = move_score
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            if best_move_score > best_score:
                very_best_move = best_move
                best_score = best_move_score
                current_node = node.get_name()
                best_move_each_pawn = dict()
                best_move_each_pawn[current_node] = best_move
            elif best_move_score == best_score:
                current_node = node.get_name()
                best_move_each_pawn[current_node] = best_move
        return best_score, current_node, very_best_move

    def min_play(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            return board.win_cond(True)
        if limit <= 0:
            return 0
        pawns = board.moveable_pawn(board.get_player())
        temp_board = copy.deepcopy(board)
        move_best_score = float('inf')
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            node = board.select_node(int(pawn.get_coordinate()))
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_best_score = min(move_best_score, self.max_play(board, limit - 1))
                board.display_matrix()
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
        return move_best_score

    def max_play(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            return board.win_cond(True)
        if limit <= 0:
            return 0
        pawns = board.moveable_pawn(board.get_player())
        temp_board = copy.deepcopy(board)
        infinity = float('inf')
        move_best_score = -infinity
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            node = board.select_node(int(pawn.get_coordinate()))
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_best_score = max(move_best_score, self.min_play(board, limit - 1))
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
        return move_best_score

    def test_minimax(self, board, limit):
        virtual_board = copy.deepcopy(board)

        current_tile, next_tile = self.minimax(virtual_board, limit)

        print("Current tile :", current_tile)
        print("Next tile :", next_tile)
        return current_tile, next_tile

    def alpha_beta_pruning(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        pawns = board.moveable_pawn(board.get_player())
        infinity = float('inf')
        best_score = -infinity
        temp_board = copy.deepcopy(board)
        current_node = 0
        very_best_move = 0
        best_move_each_pawn = dict()
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            best_move = moves[0]
            beta = infinity
            node = board.select_node(int(pawn.get_coordinate()))
            best_move_score = -infinity
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_score = self.min_alpha_beta(board, limit, best_move_score, beta, next_node)
                if move_score > best_move_score:
                    best_move = move
                    best_move_score = move_score
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            if best_move_score > best_score:
                very_best_move = best_move
                best_score = best_move_score
                current_node = node.get_name()
                best_move_each_pawn = dict()
                best_move_each_pawn[current_node] = best_move
            elif best_move_score == best_score:
                current_node = node.get_name()
                best_move_each_pawn[current_node] = best_move

        current_node, very_best_move = self.getBestMoveValue(best_move_each_pawn, board)

        return best_score, current_node, very_best_move

    def min_alpha_beta(self, virtual_board, limit, alpha, beta, next_node):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            return board.win_cond(True)
        if limit <= 0:
            return self.check_controller(next_node, board)
        pawns = board.moveable_pawn(board.get_player())
        temp_board = copy.deepcopy(board)
        infinity = float('inf')
        move_best_score = infinity
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            node = board.select_node(int(pawn.get_coordinate()))
            temp_beta = beta
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_best_score = min(move_best_score, self.max_alpha_beta(board, limit - 1, alpha, beta, next_node))
                if move_best_score <= alpha:
                    return move_best_score
                beta = min(beta, move_best_score)
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            beta = temp_beta
        return move_best_score

    def max_alpha_beta(self, virtual_board, limit, alpha, beta, next_node):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            return board.win_cond(True)
        if limit <= 0:
            return self.check_controller(next_node, board)
        pawns = board.moveable_pawn(board.get_player())
        temp_board = copy.deepcopy(board)
        infinity = float('inf')
        move_best_score = -infinity
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            node = board.select_node(int(pawn.get_coordinate()))
            temp_alpha = alpha
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_best_score = max(move_best_score, self.min_alpha_beta(board, limit - 1, alpha, beta, next_node))
                if move_best_score >= beta:
                    return move_best_score
                alpha = max(alpha, move_best_score)
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            alpha = temp_alpha
        return move_best_score

    def test_alpha_beta_pruning(self, board, limit):
        virtual_board = copy.deepcopy(board)

        score, current_tile, next_tile = self.alpha_beta_pruning(virtual_board, limit)

        print("\nCurrent tile :", current_tile)
        print("Next tile :", next_tile)
        return current_tile, next_tile

    def test_iterative_deepning_alpha_beta_pruning(self, board, limits):
        virtual_board = copy.deepcopy(board)
        current_tile, next_tile = 0, 0
        infinity = float('inf')
        curently_best = -infinity
        for limit in range(limits):
            score_temp, current_temp, next_temp = self.alpha_beta_pruning(virtual_board, limit)
            if score_temp == 1:
                current_tile = current_temp
                next_tile = next_temp
                break
            if score_temp > curently_best:
                curently_best = score_temp
                current_tile = current_temp
                next_tile = next_temp
        print("\nCurrent tile :", current_tile)
        print("Next tile :", next_tile)
        return current_tile, next_tile