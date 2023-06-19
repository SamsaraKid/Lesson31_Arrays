students = ['Ivanov', 'Petrov', 'Smith']
mark = [5, 4, 3]
pet = ['cat', 'dog', 'turtle']

for i in range(len(students)):
    print(students[i], '\t', mark[i])

newzip = list(zip(students, mark, pet))
print(newzip)

# newzip.pop(1)
# print(newzip)

newstud, newmark, newpet = zip(*newzip)
print(newstud, newmark, newpet)


nums = [1,2,3,4,5]
nums3 = []

def f1():
    for i in nums:
        nums3.append(i*3)

f1()
print(nums3)

print('##############################')
nums = [1,2,3,4,5]
nums3 = []

def f2(i):
    return i*3

for i in nums:
    res = f2(i)
    nums3.append(res)
print(nums3)
print('##############################')

nums = [1,2,3,4,5]
nums3 = []

nums3 = list(map(f2, nums))
print(nums3)


print('##############################')

nums = [2,4,6,8]
nums1 = list(map(lambda x: x + 100, nums))
print(nums1)
print('##############################')

marka = ['bmw', 'audi', 'niva']
yr = ['2008', '2009', '1999']
num = ['qwe123', 'asd456', 'zxc789']
cars = list(zip(marka, yr, num))

for i in range(len(cars)):
    for j in range(len(cars[i])):
        print(cars[i][j], end=' \t')
    print()


for x,y,z in cars:
    print(x,'-',y,'-',z)

print('##############################')
nums11 = [15,22,33,5]

def f11(i):
    if i%5 == 0:
        return True

newnums11 = list(filter(f11, nums11))
print(newnums11)