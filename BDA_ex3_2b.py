from mpi4py import MPI
import numpy as np

#Getting the rank and size
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
name = MPI.Get_processor_name()

#Initializing array
A = np.arange(10000)

#Initializing an integer to pass
integer = 5
prev = rank -1
next = rank + 1

#Master worker 
if(rank ==0):
    prev = size - 1 #setting the previous one to form a cycle
    
    comm.isend(integer, dest = next)
    data = comm.irecv(source = prev)
    print("Rank {} recieved data from rank {}".format(rank,prev))
elif (rank == size-1):
    next = 0 #since last one sends to 0th worker
    
    data = comm.irecv(source = prev)
    comm.isend(integer, dest = next)
    print("Rank {} recieved data from rank {}".format(rank,prev))
else:
    data = comm.irecv( source = prev)
    comm.isend(integer, dest = next)
    
    print("Rank {} recieved data from rank {}".format(rank,prev))

