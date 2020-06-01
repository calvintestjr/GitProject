list1 = [1, 2, 3]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            pass
        print(i * j)
    print("Outside the nested loop")