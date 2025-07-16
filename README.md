# Intro
Python, you may have heard about the programming language python even if you are not a programmer!!!   
This language is a interpretered language which is very high level and is very understandable.    
The language is almost identical to typical english!! 

# Assignments

## Assignment 1 - Mathamatical tables
### 1a 
Create a program that generates mathamatical tables from 3 to 10.                                                            
First, dont need to use for loops for creating the table.                   
Just hardcode the values. After you have done that,    
create a new file and use for loops here.                       
Here is the sample outputs for the first stage and the second one which we have to achieve:    
#### Stage 1
```
1 3 3 
2 3 6 
3 3 9
```
#### Stage 2 
```
1x3=3 
2x3=3
3x3=9
...
```
In Stage 2, the tables should have 10 items in them. We should also generate from the 3 table to the 10 table.

### 1b
Take input from a file in1.txt containing 3 in first line and 8 in second line and generate the mathematical tables 3 8

### 1c 
Take input from a file in2.txt containing 3,8 in the first line and generate the mathematical tables 3,8

### 1d
Send the results to an output file out1.txt. Use "\n" wherever required to generate a new line.    
The file content should look same as the console output.


## Assignment 2 - Simple calculator
### 2a
Create a simple calculator that accepts 3 imputs:   
1. First number    
2. Second number                                    
3. Operation (What we want to do with the numbers)                              

In the third input, if the user enters an asterisk we have to multiply those numbers.               
if the user enters a plus symbol, we have to add those numbers.                                     
if the user enters a minus symbol, we have to subtract those numbers.                               
if the user enters a slash symbol, we have to divide those numbers                        
And lastly, if the user enters something else other than these, we have to give a print saying "Oopsie! You have entered an invalid input!! Please try again!!!!!"

## Assignment 3 - Password Generator
### 3a 
Create a password generator that generates a random three character password everytime we run it. The first char should be a lowercase letter, and then uppercase, and then a number. No need for shuffling here. Use 3 lists for storing all the lowercase and uppercase letters, and numbers respectively.

### 3b
Now create a similar password generator as before but this time, take the chars from one list that contains all the numbers, lowercase and uppercase letters. This will make the password shuffled.

### 3c
Now do the exact same as the above, except, create a function that accepts the length of the password and generates a password of that length.

### 3d
Now create another function that takes both the quantity of passwords, and the length of the password. generate the output as list that contains the passwords according to the function arguments.

