#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime for this while loop would have to be O(n). The reason why is because the condition above has 'a' less than 'n _ n _ n'. To me, that would be O(n^3) but then in the line below I see 'a' declared inside loop meaning it would increase while 'n' would stay the same. I decided to cancel 'n's and was left with one 'n'.

b) The runtime for this for loop and nested while loop would have to be 0(n log n). I arrived at this answer by giving the for loop a runtime of O(n) and the while loop a runtime of O(log n) for j incrementing faster than O(n). I add them up together to get o(n log n).

c) The runtime for this recursive function would have to be O(n). Recursion works almost like a loop.

## Exercise II

Write out a binary search using iterative method. Using the n story building use a while loop to find the middle. Lowest being 0 and Highest being n story of building. Find the middle and if the egg does not break then we know we can cancel all floors before middle. Now we adjust lowest to one above old middle and find a new middle. We do this until we find the turning point floor where eggs begin to break.
