#set
basket = {"orange","apple","mango","apple","orange"}
print(type(basket))
#dictiona
a={}
print(type(a))

print(basket)
a=set()
a.add(1)
a.add(2)
a.add(2)
print(a)

numbers=[1,2,3,4,2,3,4]
unique_numbers=set(numbers)
print(unique_numbers)
unique_numbers.add(5)
print(unique_numbers)

fs = frozenset(numbers)

x={"a","b","c"}
print("a" in x)
y={ "a", "g", "h"}
print(x|y)
print(x&y)
print(x-y)
print(x<y)
k = {"h","g"}
print(k<y)