lst = [2, 4, 5, 9, 11, 19, 23]

N = len(lst)

# def f():
# 	for i in range(N):
# 		if lst[i] == 11:
# 			return i
#
# print(f())

def binarySearch(a, N, key):
	# 구간 초기화
	start = 0
	end = N-1
	while start <= end:				# 검색 구간이 유효하면 반복
		middle = (start+end)//2		# 중앙원소 인덱스
		if a[middle] == key:			# 검색 성공
			return middle
		elif a[middle] > key:		# 중앙값이 키보다 크면
			end = middle - 1
		else:						# 키보다 작으면
			start = middle + 1
	return -1						# 검색 실패

print(binarySearch(lst, N, 11))
