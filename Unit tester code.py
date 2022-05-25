import unittest
from SortedList import SortedList 

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case. And create a SortedList object """
        self.testList = SortedList()

        self.testList.insertNode(2)
        self.testList.insertNode(1)
        self.testList.insertNode(5)
        self.testList.insertNode(3)
        

    def test1(self):
        """This test method checks for the getLength method"""

        if (self.testList.getLength() == 4):
            print("getLength() providing correct length of list")
        else:
            print("getLength() not providing correct length of list")

    def test2(self):
        """test case 2 checks for insertNode() method"""

        if (self.testList.insertNode(4) == 3):
            print("insertNode() adding new element correctly")
        else:
            print("insertNode() not adding new element correctly")

    def test3(self):
        """test case 3 checks for removeLowest() method"""

        supposedRemoved = self.testList.getFirst()

        if (self.testList.removeLowest() == supposedRemoved):
            print("removeLowest() removing lowest value correctly")
        else:
            print("removeLowest() not removing lowest value correctly")


    def test4(self):
        """test case 4 checks for removeHighest() method"""

        supposedRemoved = self.testList.getLast()

        if (self.testList.removeHighest() == supposedRemoved):
            print("removeHighest() removing hiughest value correctly")
        else:
            print("removeHighest() not removing hiughest value correctly")


    def test5(self):
        """test case 5 checks for isEmpty() method"""

        if (self.testList.isEmpty() == False):
            print("isEmpty() providing correct information about list")
        else:
            print("isEmpty() not providing correct information about list")



if __name__ == "__main__":

    tester = SimpleTestCase()

    tester.setUp()
    tester.test1()
    tester.test2()
    tester.test3()
    tester.test4()
    tester.test5()

    """ Now we run all cases in once """

    unittest.main()
