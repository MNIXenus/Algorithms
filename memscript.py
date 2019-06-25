import numpy as np
input_file = open('input.txt', 'r')
arr = np.array(list(map(int, input_file.readline().split()))[1:])
sum_arr = np.sum(arr)
a = np.array(np.arange(2**len(arr)//2), dtype = np.uint8)
a = a.reshape(len(a), 1)
combs = np.unpackbits(a, axis=1)
pad = len(arr)-len(combs[0])
combs = np.pad(combs, pad, 'constant', constant_values = 0)[pad:-pad, :-pad]
pairs = np.vstack((sum_arr - np.sum(combs*arr, axis = 1), np.sum(combs*arr, axis = 1))).T
answer = np.min(np.max(pairs, axis = 1))
open('output.txt', 'w').write(str(answer))
