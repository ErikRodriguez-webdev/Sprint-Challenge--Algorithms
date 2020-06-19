#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The runtime for this while loop would have to be O(n). The reason why is because the condition above has 'a' less than 'n _ n _ n'. To me, that would be O(n^3) but then in the line below I see 'a' declared inside loop meaning it would increase while 'n' would stay the same. I decided to cancel 'n's and was left with one 'n'.

b) The runtime for this while loop would have to be O(n^3). I arrived at this answer by giving the for loop a runtime of O(n) and the while loop a runtime of O(n^2). I add them up together to get o(n^3).

c) The runtime for this recursive function would have to be O(2^n). I gave this runtime because if bunnies argument passed in happens to be a negative value that would be best case scenario because this function seems to grow. However focusing on the worst case scenario if bunnies argument is a positive value and not zero it would pass the condition of not being zero and then add two to the bunnies and subtract 1, which means it would call the function again with a new value of bunnies plus one.

## Exercise II

- I'm not sure how finding the floor where eggs begin to break can minimize that, we have plenty of eggs. I would need more information to fully solve this.

-Assuming n story building is an integer...
-Assuming eggs are in a list...

eggs = [plenty]

    -for loop (i) through all n story floors starting at 1 ending at n the length of building

        -if i is current floor is less than f turning point of eggs starting to break:
            -remove one egg from plenty and egg is currently dropped NOT BROKEN

        -if i is current floor is greater than f turning point of eggs starting to break:
            -remove one egg from plenty and egg is BROKEN
