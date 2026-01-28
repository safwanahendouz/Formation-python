#######################################################################
####################### For Loop
#######################################################################




#########################################################################
# Ex1   range(N):     N: Nombre de fois

# for number in range(20):
#     print('mon message !!! ', number)

# for number in range(20):
#     n = 19 - number 
#     print(n*"*")


#########################################################################
# Ex2   range(n,N) :  n: Nombre de debut   N:Nombre de fois

# for number in range(2, 10):
#     print('mon message !!! ', number)



#########################################################################
# Ex3   range(n,N, p) :  n:Nombre de debut   N:Nombre de fois   p: le pas

# for number in range(3, 48, 4):
#     print('mon message !!! ', number)




#########################################################################
# Ex4   range(n,N, p) :  Break and Continue

# for number in range(1, 12):
#     if number == 7:
#         break
#     print('mon message !!! ', number)

# print('Fin')

# second example :

# for number in range(1, 20):
#     if number==9 :
#         continue
#     elif number==7 :
#         break

#     print('Mon message' , number)


# #########################################################################
# Ex5
# numbers = [20, -45, -70, 100, 300, -4]

# for number in numbers:
#     if number >= 0:
#         print('positif : ', number)

# #####################second example#############################"" :

# numbers = [-40, 0, 19, 20, -45, -70, 100, 300, -4]

# for number in numbers :
#     if number >=0 :
#         print('number is positif', number)
#     # else :
#     #     print('number is negatif', number)

    
    

##########################################################################
# Ex6    :  Else

# numbers = [0, 1, 2, 3]

# for number in numbers:
#     print('mon message !!! ')
#     if number == 2:
#         break

# else:
#     print('else message ')




#########################################################################
# Ex7    :  Nested Loop

# for i in range(0,3):
#     for j in range(0,6):
#         print('(',i ,',', j,')')
#         # print(f"({i}, {j})")