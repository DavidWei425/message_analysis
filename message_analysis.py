data = []
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
print('檔案讀取完了,總共有', len(data), '筆資料')
total = 0
for x in range(0,len(data)):
	total += len(data[x])
	avg = total / len(data)
print('每句留言的平均長度為 : ', avg)
#或是以下寫法
#sum_len = 0
#for d in data:
#	sum_len += len(d)
#avg = sum_len / len(data)
#print('留言的平均長度為 : ', avg)

#計算留言長度小於100的數量
m100 = []
for d in data:
	if len(d) < 100:
		m100.append(d)
print('長度小於100的留言有', len(m100), '則')