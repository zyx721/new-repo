List =[2200,2350,2600,2130,2190]
print(List[1]-List[0])
a = sum(List[:3])
print(a)
for i in range (5):
    if List[i]==2000:
        print("in this mounth"+int(i)+"you spent 2000 dollres exactly")
else:
    print("didnt spent 2000 exactly")
List.append(1980)
List[3]=List[3]-200
print(List)