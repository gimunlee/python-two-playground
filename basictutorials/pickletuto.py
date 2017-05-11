""" Pickling tutorial """
import pickle

T = [1, 2, 3]
REPR_T = pickle.dumps(T)
T2 = pickle.loads(REPR_T)
print T2

print T == T2
print T is T2
