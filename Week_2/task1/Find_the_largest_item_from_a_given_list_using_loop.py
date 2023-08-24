ls = [1,2,3,4,5,10,5,189,182,125,1238,123,1222]

max = ls[0]

for index,number in enumerate(ls):
    if max <= ls[index]:
        max = number
        
print(f"\nMax number = {max}")