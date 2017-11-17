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

    def generate_row(self, edge_name):
        for i in range(0, 3):
            for j in range(0, 2):
                edge_int = ord(edge_name)
                current = i * 3 + j
                next = i * 3 + j + 1
                current_node = self.get_node_list()[current]
                next_node = self.get_node_list()[next]
                edge = Edge(current_node, next_node, edge_name)
                current_node.add_connection(edge)
                next_node.add_connection(edge)
                self._edge_list.append(edge)
                edge_int += 1
                edge_name = chr(edge_int)
        return edge_name

    def generate_collumn(self, edge_name):
        for i in range(0, 3):
            for j in range(0, 2):
                edge_int = ord(edge_name)
                current = i + j * 3
                next = i + j * 3 + 3
                current_node = self.get_node_list()[current]
                next_node = self.get_node_list()[next]
                edge = Edge(current_node, next_node, edge_name)
                current_node.add_connection(edge)
                next_node.add_connection(edge)
                self._edge_list.append(edge)
                edge_int += 1
                edge_name = chr(edge_int)
        return edge_name

    def generate_diagonal(self, edge_name):
        for i in range(0, 2):
            edge_int = ord(edge_name)
            current = i * 4
            next = i * 4 + 4
            current_node = self.get_node_list()[current]
            next_node = self.get_node_list()[next]
            edge = Edge(current_node, next_node, edge_name)
            current_node.add_connection(edge)
            next_node.add_connection(edge)
            self._edge_list.append(edge)
            edge_int += 1
            edge_name = chr(edge_int)
        for i in range(0, 2):
            edge_int = ord(edge_name)
            current = i * 2 + 2
            next = i * 2 + 4
            current_node = self.get_node_list()[current]
            next_node = self.get_node_list()[next]
            edge = Edge(current_node, next_node, edge_name)
            current_node.add_connection(edge)
            next_node.add_connection(edge)
            self._edge_list.append(edge)
            edge_int += 1
            edge_name = chr(edge_int)
        return edge_name

    def generate_board(self):
        self.generate_node()
        edge_name = 'a'
        edge_name = self.generate_row(edge_name)
        edge_name = self.generate_collumn(edge_name)
        self.generate_diagonal(edge_name)
        for i in self.get_node_list():
            print(i, ":", i.get_connected_to())
        print()
        for i in self.get_edge_list():
            print(i, ":", i.get_connection())
        pass

    """
    def generate_board(self):
        
        #Create list of node and edge, append nodes to edges
        
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
    """

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
                    self._matrix[1][0] = 0
                elif num == 4:
                    self._matrix[1][1] = 0
                elif num == 5:
                    self._matrix[1][2] = 0
                elif num == 6:
                    self._matrix[0][0] = 0
                elif num == 7:
                    self._matrix[0][1] = 0
                elif num == 8:
                    self._matrix[0][2] = 0
            else:
                tile_name = i.get_pawn().get_controller()
                num = int(i.get_name())
                if num == 0:
                    self._matrix[2][0] = tile_name
                elif num == 1:
                    self._matrix[2][1] = tile_name
                elif num == 2:
                    self._matrix[2][2] = tile_name
                elif num == 3:
                    self._matrix[1][0] = tile_name
                elif num == 4:
                    self._matrix[1][1] = tile_name
                elif num == 5:
                    self._matrix[1][2] = tile_name
                elif num == 6:
                    self._matrix[0][0] = tile_name
                elif num == 7:
                    self._matrix[0][1] = tile_name
                elif num == 8:
                    self._matrix[0][2] = tile_name

        for i in self._matrix:
            print(i)

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
            # raise Exception("That tile does not have any pawn")
        if next_state.get_pawn() is not None:
            return "Node is occupied"
            # raise Exception("Node is occupied")
        if player != "" and current_state.get_pawn().get_controller() != player:
            # raise Exception("That is not your pawn !")
            return "That is not your pawn !"
        if next_state.get_name() not in legal_edge:
            return "You cannot move your pawn to that tile"
            # raise Exception("You cannot move your pawn to that tile")
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
            print("Check row :", row)
            column = self.check_column(True)
            print("Check column :", column)
            diagonal = self.check_diagonal(True)
            print("Check diagonal :", diagonal)
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
            return -1
        else:
            return 1

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

    def set_value(self,value):
        self._value = value

    def get_value(self,value):
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
    _test = 0

    def __init__(self):
        """Create human obj with pawns controller is AI"""
        (super(AI, self).__init__("AI"))
    
    def check_row_controller(self,rowOf,current_node,board):
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]
        row = []
        controllerValue= dict()
        controllerValue.update({'human':0,'AI':0})
        if(rowOf == "first"):
            row = first
        elif(rowOf == "second"):
            row = second
        elif(rowOf == "third"):
            row = third

        for i in row:
            if(i != ord(current_node)-48):
                if board.get_node_list()[i].get_pawn() is not None:
                    if(board.get_node_list()[i].get_pawn() == "Human"):
                        if(i != 0 or i != 1 or i != 2):
                            controllerValue['human']+=1
                    elif(board.get_node_list()[i].get_pawn() =="AI"):
                            controllerValue['AI']+=1
        print("row",controllerValue)
        return controllerValue

    def check_diagonal_controller(self,current_node,board):
        bottom_left_upper_right = [0, 4, 8]
        bottom_right_upper_left = [2, 4, 6]
        diagonal = [bottom_left_upper_right,bottom_right_upper_left]
        controllerValue= dict()
        controllerValue.update({'human':0,'AI':0})
        for i in diagonal:
            for j in i:
                if(j != ord(current_node)-48):
                    if board.get_node_list()[j].get_pawn() is not None:
                        print(j)
                        print("controller", board.get_node_list()[j].get_pawn().get_controller())
                        if(board.get_node_list()[j].get_pawn().get_controller() == "Human"):
                            controllerValue['human']+=1
                            print("Human",controllerValue['human'])
                        elif(board.get_node_list()[j].get_pawn().get_controller() =="AI"):
                            controllerValue['AI']+=1
                            print("AI",controllerValue['AI'])
        print("diagonal",controllerValue)
        return controllerValue

    def check_column_controller(self,columnOf,current_node,board):
        first = [0, 3, 6]
        second = [1, 4, 7]
        third = [2, 5, 8]
        column = []
        controllerValue= dict()
        controllerValue.update({'human':0,'AI':0})

        if(columnOf == "first"):
            column = first
        elif(columnOf == "second"):
            column = second
        elif(columnOf == "third"):
            column = third

        for i in column:
            if(i != ord(current_node)-48):
                if board.get_node_list()[i].get_pawn() is not None:
                    if(board.get_node_list()[i].get_pawn().get_controller() == "Human"):
                        controllerValue['human']+=1
                    elif(board.get_node_list()[i].get_pawn().get_controller() =="AI"):
                        controllerValue['AI']+=1
        print("column",controllerValue)
        return controllerValue

    def getBestMoveValue(self, nodeList, board):
        pawnValueDict = dict()
        for current_node,next_move in list(nodeList.items()):
            rowDict = dict()
            colDict = dict()
            diagonalDict = dict()
            if(current_node == '8'):
                rowDict = self.check_row_controller("third",current_node,board)
                diagonalDict = self.check_diagonal_controller(current_node,board)
            elif(current_node == '7'):
                rowDict = self.check_row_controller("second",current_node,board)
            elif(current_node == '6'):
                rowDict = self.check_column_controller("first",current_node,board)
                diagonalDict = self.check_diagonal_controller(current_node,board)
            elif(current_node == '5'):
                rowDict = self.check_row_controller("second",current_node,board)
                colDict = self.check_column_controller("third",current_node,board)
            elif(current_node == '4'):
                rowDict = self.check_row_controller("second",current_node,board)
                colDict = self.check_column_controller("second",current_node,board)
                diagonalDict = self.check_diagonal_controller(current_node,board)
            elif(current_node == '3'):
                rowDict = self.check_row_controller("second",current_node,board)
                colDict = self.check_column_controller("first",current_node,board)
            elif(current_node == '2'):
                rowDict = self.check_row_controller("first",current_node,board)
                colDict = self.check_column_controller("third",current_node,board)
                diagonalDict = self.check_diagonal_controller(current_node,board)
            elif(current_node == '1'):
                rowDict = self.check_row_controller("first",current_node,board)
                colDict = self.check_column_controller("second",current_node,board)
            elif(current_node == '0'):
                rowDict = self.check_row_controller("first",current_node,board)
                colDict = self.check_column_controller("first",current_node,board)
                diagonalDict = self.check_diagonal_controller(current_node,board)
            if not rowDict:
                rowDict.update({'human':0,'AI':0})
                print("norow")
            if not colDict:
                colDict.update({'human':0,'AI':0})
                print("nocol")
            if not diagonalDict:
                diagonalDict.update({'human':0,'AI':0})
                print("norow")
            pawnValueDict[current_node] = 2*(rowDict['AI']+colDict['AI']+diagonalDict['AI'])+(rowDict['human']+colDict['human']+diagonalDict['human'])
            print(pawnValueDict)
            print("rowAI",rowDict['AI'])
            print("colAI",colDict['AI'])
            print("diagonalAI",diagonalDict['AI'])
            print("rowhuman",rowDict['human'])
            print("colhuman",colDict['human'])
            print("diagonalhuman",diagonalDict['human'])
        bestValue=0
        bestPawn=None
        for current_node, value in list(pawnValueDict.items()): 
            if(bestPawn == None):
                bestPawn = current_node
            elif(bestValue<pawnValueDict[current_node]):
                bestValue = pawnValueDict[current_node]
                bestPawn = current_node
                print("value is different ",current_node)
            elif(bestValue == pawnValueDict[current_node]):
                bestPawnRand, bestValuerand = random.choice(list(pawnValueDict.items()))
                bestPawn = bestPawnRand
                print("has same value")
        return bestPawn,nodeList[bestPawn]

    def minimax(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        pawns = board.moveable_pawn(board.get_player())
        best_score = float('-inf')
        temp_board = copy.deepcopy(board)
        infinity = float('inf')
        best_move_score = -infinity
        current_node = 0
        very_best_move = 0
        for pawn in pawns:
            moves = board.pawn_moves(board.select_node(int(pawn.get_coordinate())))
            best_move = moves[0]
            node = board.select_node(int(pawn.get_coordinate()))
            for move in moves:
                next_node = board.select_node(int(move))
                temp_node = board.select_node(int(node.get_name()))
                board.pawn_transition(temp_node, next_node)
                move_score = self.min_play(board, limit - 1)
                print(move_score)
                if move_score > best_move_score:
                    best_move = move
                    best_move_score = move_score
                    current_node = node.get_name()
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            if best_move_score > best_score:
                very_best_move = best_move
                best_score = best_move_score
                current_node = node.get_name()
        return current_node, very_best_move

    def min_play(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            eval_num = board.win_cond(True)
            return eval_num
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
                print("Next :", next_node)
                print("Current :", temp_node)
                board.pawn_transition(temp_node, next_node)
                move_best_score = min(move_best_score, self.max_play(board, limit - 1))
                print(move_best_score)
                board.display_matrix()
                print("Win or not :", board.win_cond())
                print("Util :", board.win_cond(True))
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            print("Score :", move_best_score)
        return move_best_score

    def max_play(self, virtual_board, limit):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            eval_num = board.win_cond(True)
            return eval_num
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
        print(self._test)

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
                move_score = self.min_alpha_beta(board, limit, best_move_score, beta)
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
        print("Pawn moves :", best_move_each_pawn)
        if len(best_move_each_pawn) > 1:
            board.display_matrix()
            current_node, very_best_move = self.getBestMoveValue(best_move_each_pawn,board)
            print("best_move_each_pawn", best_move_each_pawn)
            print("Best score :", best_score)
            print("Random move :", current_node, very_best_move)
            board = copy.deepcopy(virtual_board)
            print(board.pawn_transition(board.select_node(int(current_node)), board.select_node(int(very_best_move))))
            while (self.min_play(board, 3) == -1 and len(best_move_each_pawn) > 1):
                best_move_each_pawn.pop(current_node)
                current_node, very_best_move = random.choice(list(best_move_each_pawn.items()))
                board = copy.deepcopy(virtual_board)
                board.pawn_transition(board.select_node(int(current_node)), board.select_node(int(very_best_move)))
                print(very_best_move)
                if len(best_move_each_pawn) > 1:
                    print("Re-Prediction")
        else:
            board = copy.deepcopy(virtual_board)
            print(board.pawn_transition(board.select_node(int(current_node)), board.select_node(int(very_best_move))))
            print("Result :", self.min_play(board, 3))
        return best_score, current_node, very_best_move

    def min_alpha_beta(self, virtual_board, limit, alpha, beta):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            eval_num = board.win_cond(True)
            return eval_num
        if limit <= 0:
            return 0
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
                move_best_score = min(move_best_score, self.max_alpha_beta(board, limit - 1, alpha, beta))
                if move_best_score <= alpha:
                    return move_best_score
                beta = min(beta, move_best_score)
                board = copy.deepcopy(temp_board)
            board = copy.deepcopy(temp_board)
            beta = temp_beta
        return move_best_score

    def max_alpha_beta(self, virtual_board, limit, alpha, beta):
        board = copy.deepcopy(virtual_board)
        board.next_turn()
        if board.win_cond():
            eval_num = board.win_cond(True)
            return eval_num
        if limit <= 0:
            return 0
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
                move_best_score = max(move_best_score, self.min_alpha_beta(board, limit - 1, alpha, beta))
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

        print()
        print("Current tile :", current_tile)
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
        print()
        print("Current tile :", current_tile)
        print("Next tile :", next_tile)
        return current_tile, next_tile


"""
def main():
    board = Board()
    human = Human()
    ai = AI()
    board.assign_pawn_to_board(human, ai)
    board.set_player({'Human': human, 'AI': ai})

    first_turn = "Human"
    if random.random() > 0.5:
        first_turn = "AI"

    if first_turn == "Human":
        turn = ["Human", "AI"]
    else:
        turn = ["AI", "Human"]

    now = turn[0]

    while not board.win_cond():
        board.set_turn(now)
        print("Now is {} turn\n".format(now))
        board.display_matrix()

        if now == "Human":
            pawn = board.moveable_pawn(human)
        else:
            pawn = board.moveable_pawn(ai)

        print("\nYour moveable pawns are on node :\n {} \n".format(board.print_list(pawn, True)))

        if now == "AI":
            # current_tile = int(pawn[int(math.floor(random.random() * len(pawn)))].get_coordinate())


            print("Test Minimax :")
            now_time = time.time()
            current_tile, next_tile = ai.test_minimax(board, 6)
            after_time = time.time()
            print(after_time - now_time)
            print()



            print("Test Alpha Beta Pruning :")
            now_time = time.time()
            current_tile, next_tile = ai.test_alpha_beta_pruning(board, 5)
            after_time = time.time()
            print(after_time - now_time)
            print()


            print("Choose your tile to move :\n {}".format(current_tile))
        else:
            current_tile = int(input("Choose your tile to move :"))

        possible_move = board.pawn_moves(board.select_node(int(current_tile)))

        print("\nYou can move your pawn to node:\n {} \n".format(board.print_list(possible_move)))

        if now == "AI":
            print("Choose your next tile :\n {}".format(next_tile))
        else:
            next_tile = int(input("Choose your next tile : "))

        board.pawn_transition(board.select_node(int(current_tile)), board.select_node(int(next_tile)), now)

        if now == "Human":
            now = "AI"
        else:
            now = "Human"
        print()
    if now == "Human":
        winner = "AI"
    else:
        winner = "Human"
    print("{} is a winner !".format(winner))
    """
