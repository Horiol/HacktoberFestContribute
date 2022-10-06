# Replace this with your own array.
arr = [1, 1, 0, 2, 3, 0, 1, 0]
zeroCounter = 0
newArr = []
for num in arr:
	if num == 0:
		zeroCounter+=1
	else:
		newArr.append(num)
newArr.extend(0 for _ in range(zeroCounter))
print(newArr)
