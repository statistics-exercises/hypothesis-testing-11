import numpy as np
import scipy.stats
  
def criticalRange( n, p ) : 
  # Your code to calculate the critical region should go here
  
  
  
def hypothesisTest( data, n, p ) : 
  l = criticalRange( n, p )
  # You need to use the l value that is returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  

# You need to set these three variables using the information in the question  
expected = 
observation =
nmeasurements = 
print( hypothesisTest( observation, nmeasurements, expected ) )
