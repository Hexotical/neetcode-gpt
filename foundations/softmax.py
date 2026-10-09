import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        to_ret = []
        for elem in z:
            to_ret.append(np.round(1/(1+np.e**(-elem)), 5))
        return to_ret


    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        to_ret = []
        for elem in z:
            if elem <= 0:
                to_ret.append(np.float64(0))
            else:
                to_ret.append(elem)

        return to_ret
