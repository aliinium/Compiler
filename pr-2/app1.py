def sp(input):
    chars = {"!", ",", "?", ".", ":"}
    r = []
    word = ""

    for letter in input:
        if letter in chars:
            letter = ""
            
        word = word + letter
        
        if letter == " ":
            letter = ""
            r.append(word)
            word = ""
    
    return r

with open("/Users/aliinium/Desktop/w/compiler/pr-2/code.txt", "r") as file:
    f = file.read()

print(sp(f))