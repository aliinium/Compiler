s = "Hello, How Are You?"

for letter in s:
    r = letter
    if r == " ":
        r = "\n"
    if r == "," or r == "?":
        r = ""
        
    print(r, end = "")