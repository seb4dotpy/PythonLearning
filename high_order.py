from functools import reduce 
##important import modules

#funtion in a function

#filter

listRandom = [1,2,3,4,5,6,7,8,9,10]
#only want unpair numbers, with filter()
odd = list(filter(lambda x: x%2 != 0 , listRandom))
print(odd)

#map

#we want numbers **2

square = list(map(lambda x: x**2, listRandom))
print(square)

#reduce

#multiplies all list elements


reduce_function = reduce(lambda a, b : a * b, listRandom)
print(reduce_function)