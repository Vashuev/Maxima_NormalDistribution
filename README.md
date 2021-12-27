# Maxima_NormalDistribution

![alt text](https://drive.google.com/file/d/1-DtWvQgJH3E_aSmyApjWWZ75sJnZCf7a/view?usp=sharing)

# INTRODUCTION

It is a self learning algorithm which tells the maxima i.e Y by guessing value of X of a normal distribution graph. 
The approch is to randomaly generate value of X between two range and if their is not the maxima for Y, decrease the range using connected Nodes guess's values, and repeat it with every Nodes in every round until the value guessed by any node doesn't increase futher.

# WORKING

Run the graph.py file and the guessed values will be stored in the txt file guess.txt each time it runs.

# EXAMPLE

Here are showcase of 2 testcases
a mean = .5, standard deviation = 1

Please enter mean                         .5\
Please enter standard deviation           1\
Please enter Range for X i.e [min , max]  -5 5\
Enter no. of Nodes                       5\
Enter adjacent nodes of 1st NODE: 2 5\
Enter adjacent nodes of 2st NODE: 1 3 5\
Enter adjacent nodes of 3st NODE: 2 4\
Enter adjacent nodes of 4st NODE: 3 5\
Enter adjacent nodes of 5st NODE: 1 2 4


MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 1\
MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 2\
MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 3\
MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 4\
MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 5


 -------------------OUTPUT for file-------------------
Guess of 1 = [-2.0, 1.0, 0.5]\
Guess of 2 = [-0.3, 1.0, 0.5]\
Guess of 3 = [-0.7, 0.6, 0.5]\
Guess of 4 = [-3.0, 1.2, 0.5]\
Guess of 5 = [4.5, 0.3, 0.5]



b. mean = .5, standard deviation = 1

---------------------------------------------------------------------
Please enter mean                         0.5\
Please enter standard deviation           1\
Please enter Range for X i.e [min , max]  -3 4\
Enter no. of Nodes                       8\
Enter adjacent nodes of 1st NODE: 2 8\
Enter adjacent nodes of 2st NODE: 1 3 8\
Enter adjacent nodes of 3st NODE: 2 4\
Enter adjacent nodes of 4st NODE: 3 5 6\
Enter adjacent nodes of 5st NODE: 4 6\
Enter adjacent nodes of 6st NODE: 4 5 7\
Enter adjacent nodes of 7st NODE: 6 8\
Enter adjacent nodes of 8st NODE: 1 2 7


MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 3\
MaxValue = 0.3989422804014327 at 0.5 guessed By Node : 6


 -------------------OUTPUT for file-------------------
Guess of 1 = [-2.6, 0.7]\
Guess of 2 = [1.0, 0.8]\
Guess of 3 = [3.4, 0.5]\
Guess of 4 = [2.7, 1.2]\
Guess of 5 = [2.9, 0.7]\
Guess of 6 = [-1.9, 0.5]\
Guess of 7 = [-1.5, -1.1]\
Guess of 8 = [3.1, 0.8]
