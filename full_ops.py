# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# Determines the output shape and operation count of a fully-connected layer
#
# Parameters:
#  c_in: input channel count (number of input features)
#  n_wv: number of weight vectors (number of neurons or output features)
#
# Output:
#  Prints the output channel count, output height, output width,
#  and the number of additions, multiplications, and divisions performed.
#
# Written by Nick Davis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# Import necessary modules
import sys
#import math

# Function to calculate fully-connected layer output and operations count
def fully_connected_ops(c_in, n_wv):
    # Output shape for fully connected layers:
    # Fully connected layers only deal with the number of neurons, so height and width are 1
    c_out = n_wv  # Output channel count is equal to the number of neurons (weight vectors)
    h_out = 1     # Height is 1 for fully-connected layers
    w_out = 1     # Width is 1 for fully-connected layers

    # Operations count
    muls = n_wv * c_in
    adds = muls # Accounting for Bias Term
    divs = 0

    return c_out, h_out, w_out, adds, muls, divs

# Parse script arguments
if len(sys.argv) == 3:
    c_in = int(sys.argv[1])
    n_wv = int(sys.argv[2])
else:
    print('Usage: python3 full_ops.py c_in n_wv')
    exit()

# Compute output shape and operations count
c_out, h_out, w_out, adds, muls, divs = fully_connected_ops(c_in, n_wv)

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
