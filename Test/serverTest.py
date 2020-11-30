import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import Server

class TestServer(unittest.TestCase):
    
    def test_Is_Valid_Room(self):
        temp = Server.is_valid_room("")
        self.assertFalse(temp)
    
    def test_Start_Game(self):
        temp = Server.start_game("blah", "hello")
        self.assertEqual(len(Server.room_ready),1)

    def test_Is_Valid_Username(self):
        temp = Server.is_valid_username("", "hello")
        self.assertFalse(temp)

if __name__ == '__main__':
    unittest.main()