sen = input().strip()
sen = sen.upper()
word = set(sen)
m = 0
result = None
check = True
for wor in word:
	num = sen.count(wor)
	if num > m:
		m = num
		result = wor
	elif num == m:
		result = '?'
	
print(result)
