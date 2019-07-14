import string   
alphabet = set(string.ascii_lowercase)   
def ispangram(string): 
    return set(string.lower()) >= alphabet 
string = input()
if(ispangram(string) == True): 
    print("yes") 
else: 
    print("no") 
