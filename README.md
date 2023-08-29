# Purpose

This current piece of code is meant to split a table of generated text into blocks and spaces 

eventually it'll be used in a from-scratch 3D renderer

# issue

 line 16, in generateString
    for i, x in table:
TypeError: cannot unpack non-iterable int object

line 31, in <module>      
    generateString(testTable[0])
