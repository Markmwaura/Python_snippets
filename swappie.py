#Using python, have the function SwapCase(str) take the str parameter
#and swap the case of each character.
#For example: if str is "Hello World" the output should be hELLO wORLD.
#Let numbers and symbols stay the way they are.

#NB do not use the swapcase python method.

def SwapCase(str):

    for index in str:
        if(index == index.upper()):
            print index.lower()
        elif(index == index.lower()):
            print index.upper()
        #return str


SwapCase("Hello World")
