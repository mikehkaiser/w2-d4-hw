# define function
# for x in (string), if x = 'y' string.replace('y','y!') if x = 's' add period if x in 'wgWG' replace 'x' with x.upper()
def whiteboard(words):
    new = ""
    for letter in (words):
        if letter not in 'yswg':
            new += letter#add to new string as it is
        elif letter == 'y':
            new += 'y!'
        elif letter == 's':
            new += 's.'
        elif letter in 'w':
            new += 'W'
        elif letter == 'g':
            new += 'G'
    print(new)

whiteboard('Hey welcome to doing whiteboard problems get prepared to figure out a problem on the fly')
