list_1=[1,2,3,4,5]
list_2=list_1.copy()

list_2[0]=100
print(list_1,list_2)
#copy method we use to update only one elemet .copy() this method just copy
#from list 1 and past to list 2 if i update my list 2 it does not affact list 1
#if i dont use this .copy() and update list 2 list 1 automatically updated 