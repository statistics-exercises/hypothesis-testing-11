import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_criticalRange(self) :
        u = scipy.stats.binom.ppf(0.95, 300, 0.9 )
        lll= criticalRange( 300, 0.9 )
        self.assertTrue( np.abs(u-lll)<1e-4)
        
    def test_hypothesisTest(self) :
        hhh = hypothesisTest( observation, nmeasurements, expected ) 
        self.assertTrue( hhh=="the null hypothesis is rejected in favour of the alternative", "The string returned from your hypothesis test code is incorrect.  This code should return the string the null hypothesis is rejected in favour of the alternative as the sample mean is within the critical region"  )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not contain an if statement" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("there is insufficient evidence to reject the null hypothesis")>0, "The hypothesis test function does not contain the string there is insufficient evidence to reject the null hypothesis.  This string should be present and output when the sample mean falls outside the critical region." ) 

    def test_variables(self) : 
        self.assertTrue( expected==0.9, "the variable expected has been set incorrectly" )
        self.assertTrue( observation==280, "the variable observation has been set incorrectly" )
        self.assertTrue( nmeasurements==300, "the variable nmeasurement has been set incorrectly" )
