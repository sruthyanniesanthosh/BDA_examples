from mpi4py import MPI
import numpy as np

#Getting the rank and size
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

#Initializing array
A = np.arange(72)
#print(len(A))

#Master worker splitting the array
if(rank ==0):
    array_split = np.array_split(A, size)
    print(len(array_split))
else:
    array_split = []

#Sending array to all workers using scatter
result = comm.scatter(array_split, root=0)
print("Array split recieved by rank {} , array-{}".format(rank,result))
