def sp(input):
    chars = {"!", ",", "?", ".", ":"}
    r = []
    word = ""

    for letter in input:
        if letter in chars:
            letter = ""
            
        word = word + letter
        
        if letter == " ":
            r.append(word)
            word = ""
    
    return r

str = "Hello , How Are You ?"

print(sp(str))