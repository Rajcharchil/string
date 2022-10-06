
### dictionary

mydict = {
    "fast": "in a quick manner ",
    "charchil":"A CODER",
    "marks": [1,2,3],
     "anotherdict": {'charchil' : 'player'}

     }
print(mydict['fast'])
print(mydict['charchil'])
mydict["marks"]= [23,23]
print(mydict ["marks"])
print(mydict['anotherdict']['charchil'])

##dictonary method
print(type(mydict.keys())) #print the keys of the dictionary
print(mydict.values()) #print the keys of the dictionary
print(mydict.items()) # print the (key,value )for all content of the dictonary 
print(mydict)
''' can't add list and dictonary in list'''
updatedict = {
    "lovish":"friend",
    "divya": "friend",
    "subham": "friend",
}
mydict.update(updatedict)#update the dictonary by adding key-value ,pairs from update dict

print(mydict)
 
print(mydict.get("charchil2"))#returns none as charchil2 is not present in the dictionary 
#print(mydict["charchil2"])#throws an error as charchil2 is not persent in the dictionary 
