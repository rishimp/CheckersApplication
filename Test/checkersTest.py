import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import checkers

class TestCheckers(unittest.TestCase):

    def test_Init(self):
        temp = checkers.Checkers()
        self.assertIsNotNone(temp)
    
    def test_Init_Board(self):
        temp = checkers.Checkers()
        self.assertIsNotNone(temp.board)
    
    def test_Get_Valid_Moves1(self):
        temp = checkers.Checkers()    
        self.assertIsNone(temp.get_valid_moves(0,0))

    def test_Get_Valid_Moves2(self):
        temp = checkers.Checkers()
        temp.board[0][0] = 1    
        self.assertIsNotNone(temp.get_valid_moves(0,0))

    def test_Get_Valid_Moves3(self):
        temp = checkers.Checkers()
        temp.board[0][0] = 3    
        self.assertIsNotNone(temp.get_valid_moves(0,0))

    def test_Get_Valid_Moves4(self):
        temp = checkers.Checkers()
        temp.board[0][0] = 5   
        self.assertIsNotNone(temp.get_valid_moves(0,0))
    
    def test_Clear_Highlighting(self):
        temp = checkers.Checkers()
        temp.clear_highlighting()
        self.assertEqual(temp.board[0][0], checkers.Square.INVALID)
    
    def test_To_Display_Data(self):
        temp = checkers.Checkers()
        self.assertIsNotNone(temp.to_display_data)

    def test_Make_Move(self):
        temp = checkers.Checkers()
        print(temp.get_valid_moves(3,2))
        temp.make_move(3,2,4,3)
        self.assertEqual(temp.board[1][2], checkers.Square.EMPTY)



if __name__ == '__main__':
    unittest.main()