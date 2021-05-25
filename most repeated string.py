#Code By Mark Thankappan
W= input('Please enter a string : mississippi ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(W))


output 
i=04
s=04
p=02
m=01
