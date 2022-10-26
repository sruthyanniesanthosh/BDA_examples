from mpi4py import MPI
import numpy as np

#Getting the rank and size
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

#Initializing array
A = np.arange(336)
#print(len(A))

#Split sizes defined
split_size = [0,12,18,30,36,48,54,66,72]
array_split = []
#Master worker splitting the array
if(rank ==0):
    for i in range(len(split_size)-1):
        #getting the required elements according to size given
        elt = A[split_size[i]:split_size[i]+split_size[i+1]]
        array_split.append(elt) #appending the splits 
    print(len(array_split))
else:
    array_split = []

#Sending array to all workers using scatter
result = comm.scatter(array_split, root=0)
print("Array split recieved by rank {} , array-{} of length {}".format(rank,result, len(result)))
