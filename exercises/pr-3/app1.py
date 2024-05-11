def split(txt):
    word = ''
    state = 0
    final = []
    result = []
    
    for letter in txt:
        if (state == 0):  # Start
            if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z')): 
                word += letter
                state = 1
            
            elif ((letter >= '0' and letter <= '9') or (letter == '.')):
                word += letter
                state = 2
            
            elif (letter == "<") : 
                word = letter 
                state = 3
                
            elif (letter == '='):
                word = letter
                state = 4
            
            elif (letter == '\"'):
                if word.strip():
                    result.append(word)
                word = ''
                word += letter
                state = 5
                
            elif (letter == ' '):
                word = ''
                state = 0

        if (state == 1): # Alphabet
            if ((letter >= '0' and letter <= '9') or (letter == '.')):
                result.append(word)
                word = letter
                state = 2

    for item in result:
        if item :
            final.append(result)

    return final

with open("/Users/aliinium/Desktop/Uni-Assignments/compiler/pr-3/code.txt", "r") as file:
    f = file.read()

print(split(f))