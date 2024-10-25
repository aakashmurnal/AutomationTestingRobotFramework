given_number=[1,0,6,-1,2,4,7,3]

missing_number=[]
for i in range(min(given_number), max(given_number)):
    if i not in given_number:
        missing_number=i
print(missing_number)

