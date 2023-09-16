# HappyNumber
A Python program that concludes whether a two digit number is 'happy' or 'sad'.

A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit. 
A sad number is a number which never reaches 1, and gets stuck in an endless cycle.

My program uses a loop where the digits of the number are split, the digits are squared and added together, and then conditioned against a list to see if the result has been repeated (making the number sad) and against a value of 1 (making the number happy). If both conditions test false, the digits of the result are split and the process is repeated until a happiness/sadness conclusion is made.
