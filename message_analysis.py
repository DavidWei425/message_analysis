data = []
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
print('檔案讀取完了,總共有', len(data), '筆資料')