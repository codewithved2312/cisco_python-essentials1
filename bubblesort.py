# bubble sort in py

demolist = []
swapped = True
num = int(input("enter no. of elements u wanna sort: "))

for i in range(num):
  elem = float(input("enter list element: "))
  demolist.append(elem)

while swapped:
  swapped = False
  for i in range(len(demolist)-1):
    if demolist[i]>demolist[i+1]:
      swapped = True
      demolist[i],demolist[i+1] = demolist[i+1],demolist[i]

print("\nsorted")
print(demolist)
    
