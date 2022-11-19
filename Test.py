#for i in range(10):
    #print(i)
data = input('please enter a range of data: \n')
for num in data:
    try:
        num = int(num)
        print(num, num*num, sep=' ')
    except ValueError as e:
        pass
