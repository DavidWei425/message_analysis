
def read_file(filename):
	data = []
	with open(filename, 'r') as r:
		for line in r:
			data.append(line)
	return data


def avg_len(data):
	total = 0
	for x in range(0,len(data)):
		total += len(data[x])
		avg = total / len(data)
	return avg
#或是以下寫法
#sum_len = 0
#for d in data:
#	sum_len += len(d)
#avg = sum_len / len(data)
#print('留言的平均長度為 : ', avg)

#計算留言長度小於100的數量
def count_len100(data):
	m100 = []
	for d in data:
		if len(d) < 100:
			m100.append(d)
	return len(m100)
	

def word_counting(data):
	word_count = {}
	for words in data:
		z = words.split(' ')
		for word in z:
			if word in word_count:
				word_count[word] += 1
			else:
				word_count[word] = 1
	return(word_count)#統計每個字出現的次數


data = read_file('reviews.txt')
print('檔案讀取完了,總共有', len(data), '筆資料')
print('每句留言的平均長度為 : ', avg_len(data))
print('長度小於100的留言有', count_len100(data), '則')
wc = word_counting(data)
while True:
	word = input('請輸入想查詢之單字 : ')
	if word == 'q':
		break
	if word in wc: 
		print(word + '的出現次數為 : ', wc[word], '次')
	else:
		print('此單字沒出現過')
print('感謝使用本查詢功能')

