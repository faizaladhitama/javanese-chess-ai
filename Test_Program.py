import unittest

from Catur_Jawa import Human, Board, AI


class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self._human = Human()

    def test_human_pawn(self):
        for i in range(len(self._human.get_pawn())):
            with self.subTest(i=i):
                assert self._human.get_pawn()[i].get_controller() == 'Human'


class AITestCase(unittest.TestCase):
    def setUp(self):
        self._ai = AI()

    def test_ai_pawn(self):
        for i in range(len(self._ai.get_pawn())):
            with self.subTest(i=i):
                assert self._ai.get_pawn()[i].get_controller() == 'AI'


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._human = Human()
        self._ai = AI()
        self._board.assign_pawn_to_board(self._human, self._ai)

    def test_node(self):
        self.assertEqual(len(self._board.get_node_list()), 9, 'Incorrect numbers of node')

    def test_edge(self):
        self.assertEqual(len(self._board.get_edge_list()), 16, 'Incorrect numbers of edge')

    def test_node_in_edge(self):
        for i in range(len(self._board.get_edge_list())):
            with self.subTest(i=i):
                assert len(self._board.get_edge_list()[i].get_connection()) > 0

    def test_connection(self):
        for i in range(len(self._board.get_node_list())):
            with self.subTest(i=i):
                assert len(self._board.get_node_list()[i].get_connected_to()) > 0

    def test_node_assigned(self):
        for i in range(len(self._board.get_node_list())):
            with self.subTest(i=i):
                if self._board.get_node_list()[i].get_pawn() is not None:
                    assert self._board.get_node_list()[i].get_occupied() == True
                else:
                    assert self._board.get_node_list()[i].get_occupied() == False

    def test_possible_move(self):
        assert self._board.possible_move(self._board.select_node(0)) == ['3', '4']

    def test_transition(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(7))
        self.test_node_assigned()

    def test_column_win(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(3), self._board.select_node(6))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(0))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(1))
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(7))
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(8))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(0))
        assert self._board.check_column() == True

    def test_row_win(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(5))
        assert self._board.check_row() == True

    def test_diagonal_win(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(3), self._board.select_node(6))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(4))
        assert self._board.check_diagonal() == True

    def test_utility_human_win_diagonal(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(3), self._board.select_node(6))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(4))
        assert self._board.utility() == -1

    def test_utility_human_win_column(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(3), self._board.select_node(6))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(0))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(1))
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(7))
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(8))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(0))
        assert self._board.utility() == -1

    def test_utility_human_win_row(self):
        self._board.pawn_transition(self._board.select_node(0), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(5))
        assert self._board.utility() == -1

    def test_utility_neither_player_win(self):
        assert self._board.utility() == 0

    def test_utility_ai_win_row(self):
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(5))
        assert self._board.utility() == 1

    def test_utility_ai_win_column(self):
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(1), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(8))
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(1))
        self._board.pawn_transition(self._board.select_node(6), self._board.select_node(7))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(5), self._board.select_node(2))
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(8))
        assert self._board.utility() == 1

    def test_utility_ai_win_diagonal(self):
        self._board.pawn_transition(self._board.select_node(2), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(5), self._board.select_node(4))
        self._board.pawn_transition(self._board.select_node(4), self._board.select_node(3))
        self._board.pawn_transition(self._board.select_node(8), self._board.select_node(5))
        self._board.pawn_transition(self._board.select_node(5), self._board.select_node(2))
        self._board.pawn_transition(self._board.select_node(7), self._board.select_node(4))
        assert self._board.utility() == 1


if __name__ == '__main__':
    unittest.main()
