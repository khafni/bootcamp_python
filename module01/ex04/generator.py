import random

def list_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[j], lst[i] = lst[i], lst[j]
    return lst

def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        yield "ERROR"
        return
    l = text.split(sep)
    if option == "shuffle":
        l = list_shuffle(l)
    elif option == "unique":
        seen = set()
        l = [e for e in l if e not in seen and not seen.add(e)] 
    elif option == "ordered":
        l.sort()
    else:
        yield "ERROR"
        return
    for word in l:
        yield word

text = "Le Lorem Ipsum est simplement du faux texte."

""" for word in generator(text, sep=" "):
    print(word)
print("----------------------------") """
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
""" print("---------------------------")   
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print("---------------------------")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
print("---------------------------")
text = 1.0
for word in generator(text, sep="."):
    print(word) """