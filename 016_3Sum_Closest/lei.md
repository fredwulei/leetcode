Ideas
=====

Use a outer loop to fix the first number of the triplet. In order to find the last two numbers, start from the two ends of the remaining array respectively (i.e. i starts from beginning and j starts from ending), if sum is smaller than target, i moves forward, if sum is larger than target, the j moves backward, if sum equals to target, returns output.