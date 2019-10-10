from Person import Person

def compare(a: Person, b: Person):
    if (a.uid < b.uid):
        return -1
    
    if (a.uid == b.uid):
        return 0
    
    if (a.uid > b.uid):
        return 1