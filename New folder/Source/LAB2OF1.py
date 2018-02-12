import  numpy as np

rand_array = np.random.randint(0,20,(1,15))
print(rand_array)
print("Frequency of the random array is")
unique, counts = np.unique(rand_array, return_counts=True)

print (np.asarray((unique, counts)).T)