import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from Models.square import Square
import unittest

class MyTestClass(unittest.TestCase): 

  square = Square(5)

  # initialization logic for the test suite declared in the test module
  # code that is executed before all tests in one test run
  @classmethod
  def setUpClass(cls):
       pass 

  # clean up logic for the test suite declared in the test module
  # code that is executed after all tests in one test run
  @classmethod
  def tearDownClass(cls):
       pass 

  # initialization logic
  # code that is executed before each test
  def setUp(self):
    pass 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    pass 

  # test method
  def test_get_area(self):
    self.assertEqual(self.square.getArea(), 25) 

  # test method
  def test_get_perimeter(self):
    self.assertEqual(self.square.getPerimeter(), 20) 

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()