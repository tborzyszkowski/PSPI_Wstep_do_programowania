import pickle

dir(pickle)

x = 1 + 2j
print('x = ', x)
s = pickle.dumps(x)
print('s = ', s)
y = pickle.loads(s)
print('y = ', y, x is y, x == y)

