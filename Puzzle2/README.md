# PrecalcPuzzle_2

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Weekly%20Puzzle%20Challenge.png' width=400>

So, how to go about solving this problem?
Firstly, it is necessary to solve for x, which was 0.5 +- i√(3)/2
From there, the sequence [1,-1,-2,-1,1,2,1,-1...] was derrived-- And encoded onto a python file to derrive a sequence with as many terms as I desired

I tried various different methods unsuccessfully, attempting to utilize previous sequences knowledge from the precalculus course.
Here are several methods I used:

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Hand_origin.jpg' width=300>

While these did not work, the more time I spent with the sequence the more I realized that I have seen this pattern before. This is clearly some sort of sine/cosine wave, due to its pattern of points.

I went onto desmos and tried to test this theory:

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Desmos%20wave.png' width=400>

After which I coded it as well:

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Original%20Solution.png' width=400>


However, this solution left me feeling unsatisfied. Sure, it is close, but guess and check can only give me an approximation. I tried to revist the problem algebriacally, armed with new knowledge-- namely, it is a cosine wave, and the amplitude must be 2

My new math now marked in green:

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Hand.JPG' width=400>

Alright! Now we are getting somewhere!

<img src='https://github.com/daminals/PrecalcSummerPuzzles/blob/master/Puzzle2/pictures/Desmos%20Graph.png' width=400>

Incredible!
So now, the solution has been found.
The pattern for this sequence is 2cos(1/3πx)=y!
And it is also coded in the main.py file
