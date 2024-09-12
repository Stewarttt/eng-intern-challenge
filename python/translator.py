#import libraries
import sys

#indicators for characters
indicators = {
    "capital": ".....O",  # capitalization indicator
    "decimal":  ".O...O",  # decimal indicator
    "number": ".O.OOO"  # number indicator
} #END indicators

#number characters
numbers = {
    "1": "O.....",  # 1 (same as 'a')
    "2": "O.O...",  # 2 (same as 'b')
    "3": "OO....",  # 3 (same as 'c')
    "4": "OO.O..",  # 4 (same as 'd')
    "5": "O..O..",  # 5 (same as 'e')
    "6": "OOO...",  # 6 (same as 'f')
    "7": "OOOO..",  # 7 (same as 'g')
    "8": "O.OO..",  # 8 (same as 'h')
    "9": ".OO...",  # 9 (same as 'i')
    "0": ".OOO.."   # 0 (same as 'j')
} #END numbers

#symbol characters
symbols = {
    "."  : "..OO.O",  # Period
    ","  : "..O...",  # Comma
    "?"  : "..O.OO",  # Question Mark
    "!"  : "..OOO.",  # Exclamation Point
    ":"  : "..OO..",  # Colon
    ";"  : "..O.O.",  # Semicolon
    "-"  : "....OO",  # Dash
    "/"  : ".O..O.",  # Slash
    "<"  : ".OO..O",  # Open 
    ">"  : "O..OO.",  # Hyphen
    "("  : "O.O..O",  # Opening parenthesis
    ")"  : ".O.OO.",  # Closing parenthesis
    " "  : "......"   # Space
} #END symbols

#alphabetic characters
alphabet = {
    "a": "O.....",  # a
    "b": "O.O...",  # b
    "c": "OO....",  # c
    "d": "OO.O..",  # d
    "e": "O..O..",  # e
    "f": "OOO...",  # f
    "g": "OOOO..",  # g
    "h": "O.OO..",  # h
    "i": ".OO...",  # i
    "j": ".OOO..",  # j
    "k": "O...O.",  # k
    "l": "O.O.O.",  # l
    "m": "OO..O.",  # m
    "n": "OO.OO.",  # n
    "o": "O..OO.",  # o
    "p": "OOO.O.",  # p
    "q": "OOOOO.",  # q
    "r": "O.OOO.",  # r
    "s": ".OO.O.",  # s
    "t": ".OOOO.",  # t
    "u": "O...OO",  # u
    "v": "O.O.OO",  # v
    "w": ".OOO.O",  # w
    "x": "OO..OO",  # x
    "y": "OO.OOO",  # y
    "z": "O..OOO"   # z
} #END alphabet

#check the size of the input space
if len(sys.argv) < 2 :
    print("NONE")
#END IF

output = ""
prevNum = False
prevDec = False
nextWord = False

#run through all the words in the space
for word in sys.argv[1:] :
    #check every character in the word
    for character in word :
        if character.isalpha() :
            if character.isupper() :
                #outputs that capital characters were used
                output += indicators["capital"]

                #output the character
                output += alphabet[character.lower()]
            else :
                #output the character
                output += alphabet[character]
            #END IF

            #flags that the previous character was not a number or decimal
            prevNum = False
            prevDec = False
        #END IF

        elif character.isdigit() :
            if prevNum == False :
                #outputs that numerical characters were used
                output += indicators["number"]
            #END IF

            if prevDec == True :
                #outputs that decimal characters were used
                output += indicators["decimal"]
                prevDec = False
            #END IF

            #output the character
            output += numbers[character]

            #flags that the previous character was a number
            prevNum = True
        #END IF

        #checks if the character is a period and the previous character was a number
        elif character == "." and prevNum and prevDec == False:
            #sets a decimal to print upon the next number
            prevDec = True

            #output the character
            output += symbols[character]
        else :
            #output the character
            output += symbols[character]

            #flags that the previous character was not a number or decimal
            prevNum = False
            prevDec = False
        #END IF
    #END FOR

    #checks if this is the last letter in the string
    if word is not sys.argv[-1] :
        #puts a space at the end of the string
        output += symbols[" "]
    #END IF
#END FOR
print(output)
