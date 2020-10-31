# A second one tail test

In the previous exercise you did your first first one-tail hypothesis test using the method outlined in the flow chart given below:

![](hypo-testing.001.jpeg)

Let's consolidate what you did in the previous exercise by performing a second hypothesis test.  This time we are going to consider this question:

_The farmer from the previous question grows more confused as to what is going on with the trees in his far once he finishes harvesting his second orchard.  In the previous year, 90% of the trees in his farm produced fruit.  This year, however, 280 of the 300 trees in the two orchards harvested have produced crops.  He thus concludes that the apples are smaller because more trees are producing fruit and there is more stress on the soil.  Perform a statistical test at a 95% confidence limit to determine if the farmer is right to conclude that the number of fruit-producing trees is unusual._

__Your task in this exercise is to write code to answer this question.__  As always you need to follow the procedure outlined in the flow chart above.  I have written some functions to perform the tests for you to use to solve the problem.  In addition to completing the two functions, you need to also set some variables:

1. `expected` - should be set equal to the expectation of the distribution that is assumed under the __null hypothesis__
2. `observation` - should be set equal to the statistic the farmer has measured
3. `nmeasurements` - should be set equal to the number of measurements the farmer has used when calculating the __statistic__
