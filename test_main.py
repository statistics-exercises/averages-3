import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_average(self) : 
       for i in range(1,5) : 
           mean=0
           for j in range(100) : mean = mean + average(i*10)
           mean = mean / 100
           var = 1/12
           bar = np.sqrt(var/(i*10)/100)*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean - 0.5 )<bar, "your function is not calculating the average correctly" )
