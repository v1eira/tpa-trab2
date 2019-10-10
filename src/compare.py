from Person import Person

def compare(a: Person, b: Person):
    if (a.uid < b.uid):
        return True
    
    return False