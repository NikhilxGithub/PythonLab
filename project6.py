#create a list of 5 names
names=['anil','anmol','aditya','avi','alka']
print(names)
#insert a name 'anuj'before'aditya'
names.insert(2,'anuj')
print(names)
#append a name 'zulu'
names.append('zulu')
print(names)
#delete 'avi'from the list
names.remove('avi')
print(names)
#replace 'anil'with 'anilkumar'
i=names.index('anil')
names[i]='anilkumar'
print(names)
#sort all the names in the list
names.sort()
print(names)
#print reversed sorted list
names.reverse()
print(names)