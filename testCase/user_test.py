import unittest  

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        setUp() method allows us to define instructions that will be executed before each test method
        """
        self.new_user = User("bettyweru","Betty345") #create user object

    def userSetUp(self):
        self.assertEqual(self.new_user.username,"bettyweru")
        self.assertEqual(self.new_user.password,"Betty345")

if __name__ =='__main__':
    unittest.main()

    # second testcase
    # a test to save User objects