data = []
count = 0
total = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count%10000 == 0:
			print(len(data))

print('This text total has', len(data), 'files!')

for d in data:
	total = total + len(d)

print('Average: ',float(total/count))
#print('Average: ',float(total/len(data)))

new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print('There are total:', len(new), 'files length less than 100')
print(new[0])
print(new[1])