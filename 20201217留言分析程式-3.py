data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('總共有', len(data), '筆數據')

#留言數小於100字的留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100字')
#篩選含有good的留言
good =[]
for d in data:
	if 'good' in d:#易寫成data
		good.append(d)#易寫成data
print('一共有', len(good), '留言提到good')
print(good[0])

#篩選含有good的快寫法
good = [d for d in data if 'good' in d]
print(good[2])

good = [1 for d in data if 'good' in d]
print(good[2])

#篩選的快寫法要出現True or False
bad = ['bad' in d for d in data ]
print(bad)
#相當於
bad = []
for d in data:
	bad.append('bad' in d)
print(bad)










