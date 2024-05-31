import numpy as np

def multiply(x = 1, y = 2):
    output = np.multiply(np.array([x]), np.array([y]))
    return output


if __name__ == "__main__":
    print(multiply(1,2))
    