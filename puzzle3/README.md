# PrecalcPuzzle_3

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/puzzle3/images/problem.png' width=400>

Well, to figure out an equation, it might help to try and establish a sequence, and perhaps to also solve for the total number of solutions excluding the diagnol. 

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/puzzle3/images/3.JPG' width=400>

Utilizing python's itertools permutations feature, we can find all possible combinations

I admit I got stuck at this point. I didn't understand how to filter out the solutions that crossed the diagnol. I conferred with my peers to try and get an idea, and, my friend, Tin Škorić, managed to recognize a pattern: Solutions = (totalSolutions / (n+1))

And amazingly, it works! Unfortunately it didn't help filter out which solutions those crossed out were, so it isn't helpful for drawing the solutions.

And even ignoring that part of the problem, in practice, the current solution is just too slow.  If I can only solve for the number of the solutions (which admittedly, is the problem statement) I want it to be fast. A timeout error for an n as low as 6 is unacceptable.

But the solutions reminded me of a program I worked on earlier: Derriving pascal's triangle. 

Implementing my code, I was very confused. 
<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/puzzle3/images/triangle.png' width=500>
This is because solving for pascal's triangle isn't a uniform thing. I realized that my solutions for pascal's triangle only solved the triangular and tetrahedral numbers, but currently, I needed to solve for the center numbers.

Thankfully, solving for the center isn't difficult! The position of center numbers in the general equation for pascal's triangle is simply [2n,n]

<img src="https://github.com/daminals/PrecalcSummerPuzzles/blob/master/puzzle3/images/1.png" width="400"> 

After implementing the solution in code, I wrote an equation for it on paper and concluded the problem

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/puzzle3/images/2.JPG' width=400>

Maybe in the future I could revisit this project and try to implement the turtle following all the possible solutions to the problem
