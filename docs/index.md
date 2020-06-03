# Mod7 - Files & Exceptions
**Dev:** *Jeff Nelson*  
**Date:** *2020-06-02*

## Intro  
I will go over a few interesting and important items to remember that I learned from this week’s lecture. Lastly, I will show a program that uses pickling to read and write binary files and an example of error handling. 

## Week 7 Learnings
This week I learned more about file handling, pickling, and structured error handling. When working with text files you can perform three different types of functions open(), write(), and close(). When the file open function is called you can have it in three different modes, write “w”, read “r” or append “a”. Python allows for a few different ways to read in data from a file. The first function is *readline()*, which reads one line of data and then moves to the next line. 
![Readline Example](https://github.com/jnelson22/IntroToProg-Python-Mod07/blob/master/docs/Fig%201.jpg "Readline Example")    
Figure 1: Readline Example

The next function is *readlines()*, which reads all the lines in a file, and returns a list. This is helpful when you want to read in all your data at one time into a list. 
![Readlines Example](https://github.com/jnelson22/IntroToProg-Python-Mod07/blob/master/docs/Fig%202.png "Readlines Example")    
Figure 2: Readlines Example

Using loops is a great way to capture data from a file. The for and while loops can both be used to iterate through file. For loop has a nice feature that it will automatically close the file once done.
![Read File For Loop Example](https://github.com/jnelson22/IntroToProg-Python-Mod07/blob/master/docs/Fig%203.jpg "Read File For Loop Example")    
Figure 3: Readlines Example

One other file format is binary. In Python saving to that type is called pickling. Using the pickling function allows you to store data in binary format which obscures the content of the file and can reduce the file’s size. It is important to note that the file is not encrypted but rather obscure. See Figure 4 and https://wiki.python.org/moin/UsingPickle for an example of pickling in Python. 
![Example of Pickle Function](https://github.com/jnelson22/IntroToProg-Python-Mod07/blob/master/docs/fig%204.png "Example of Pickle Function")    
Figure 4: Example of Pickle Function



## Adding on to To-do List Python Program

## Summary
