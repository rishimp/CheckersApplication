import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import game

class TestGame(unittest.TestCase):

    def test_Init__(self):
        temp = game.Game("test1", "test2")
        self.assertIsNone(temp.tentative_selection)

    def test_Is_Correct_Side(self):
        temp = game.Game("test1", "test2")
        test = temp.is_correct_side("test1", "b")
        self.assertTrue(test)

    def test_Make_Move(self):
        temp = game.Game("test1", "test2")
        temp.set_tentative_selection(3,2)
        temp.make_move("test1", 4, 3)
        self.assertEqual(temp.idle, "test1")

    def test_Get_Board(self):
        temp = game.Game("test1", "test2").get_board()
        self.assertIsNotNone(temp)

    def test_Get_Unhighlited_Board(self):
        temp = game.Game("test1", "test2").get_unhighlighted_board()
        self.assertIsNotNone(temp)
    


if __name__ == '__main__':
    unittest.main()