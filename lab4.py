

###1
## 
##x = input("Enter a string: ")
##l = len(x)
##count = 0
##counter = 0
##
##while count<l:
##    if x[count] == "a" or x[count] == "e" or x[count] == "i" or x[count] == "o" or x[count] == "u":
##        counter = counter+1
##        print("counter:",counter)
##        
##    count = count+1
##    print(count)
##
##print("Number of vowels is",counter)



#2

lol = [['a','b','c'],['d','e','f'],['g','h','i']]

#2-(a)
lala = "."
for i in lol:
    for j in i:
        lala+=".."
        j=lala+j
        print(j)

