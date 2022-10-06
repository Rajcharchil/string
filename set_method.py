#creating an empty set
b = set()
print(type(b))

#adding valu to an empty set 
b.add(4)
b.add(4)
b.add(5)#adding a value repeatedly dose not  change a set 
b.add((4,5,6))

#b.add({4:5})#cannot add list and dictionary to list 
print(b)

print(len(b))#prints the length of this sets 

# removel an item 
b.remove(5)#remove 5 from set b
#b.remove(15)##output:key error  ## throw an error while trying  to remove 15(which is not present in set )
print(b)

print(b.pop()) ## remove an arbitrary elements from the set and returns the element removed
print(b)

print(b.union())#returns a net set with all items from sets = {4,5,6}
print(b)

print(b.intersection())#return a set which contain only item in both sets = {5}
print(b)