"""
A 4x4 grid contains the numbers 1 to 16. Write a program to populate the grid with unique
numbers between 1 and 16 inclusive. The population of the grid should be random every time the program is executed
"""
import random #Importing random function
def randomArray(lst):
    arr,sub=[],[] #Create two lists
    while lst:
        val=random.choice(lst) #Select random element from list
        lst.remove(val) #Remove selected element from list
        sub.append(val) #Append selected element to sub list
        if len(sub)==4: #Check if the length of sublist is 4,if yes add it to other list
            arr.append(sub)
            sub=[]
        else:
            continue
    print(arr)
if __name__ == "__main__":
    randomArray([i for i in range(1,17)])
