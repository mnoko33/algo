def solution(key, lock):
	global M, N
	M = len(key)
	N = len(lock)
	def get_extended_lock(lock):
		global M, N
		extended_N = N + (M - 1) * 2
		extended_lock = [[0] * extended_N for _ in range(extended_N)]
		for i in range(N):
			for j in range(N):
				extended_lock[i+M-1][j+M-1] = lock[i][j]
		return extended_lock

	def rotated_key_list(key):
		def rotate(arr):
			global M
			new_arr = [[0] * M for _ in range(M)]
			for i in range(M):
				for j in range(M):
					new_arr[j][M-1-i] = arr[i][j]
			return new_arr

		rotated_key_list = []
		for i in range(4):
			if i == 0:
				rotated_key_list.append(key)
			else:
				key = rotate(key)
				rotated_key_list.append(key)

		return rotated_key_list
	
	def check_lock_with_key(extended_lock, key):
		global M, N
		extended_N = N + (M - 1) * 2

		def copy_lock(lock):
			copied_lock = []
			for row in lock:
				copied_lock.append([x for x in row])

			return copied_lock

		def apply_key_and_ckech(r, c, copied_lock, key):
			# key 적용하기
			for i in range(M):
				for j in range(M):
					copied_lock[i+r][j+c] += key[i][j]
			# Lock의 빈곳이 모두 채워졌는지 체크
			for ii in range(M-1, M+N-1):
				for jj in range(M-1, M+N-1):
					if copied_lock[ii][jj] != 1:
						return False
			return True

		for r in range(extended_N - M + 1):
			for c in range(extended_N - M + 1):
				if apply_key_and_ckech(r, c, copy_lock(extended_lock), key):
					return True
		return False

	extended_lock = get_extended_lock(lock)
	keys = rotated_key_list(key)
	for key in keys:
		if check_lock_with_key(extended_lock, key):
			return True
	return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))