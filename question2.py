import numpy as np

# Create the random vector
random_vec = np.random.uniform(1,20,20)

print(random_vec)

# Reshape the array to 4 by 5
reshaped_array = np.reshape(random_vec, (4,5))

# Replace the max in each row by 0
max_index = np.argmax(reshaped_array, axis = 1)
reshaped_array[np.arange(len(max_index)), max_index] = 0

print(reshaped_array)