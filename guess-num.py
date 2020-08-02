import random
start = input('請決定隨機數字開始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 #count = count + 1的快捷寫法
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('你猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')