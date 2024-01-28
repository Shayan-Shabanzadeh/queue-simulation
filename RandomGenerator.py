import numpy as np


class RandomLCGGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.state = ((self.a * self.state + self.c) % self.m) / m
        return self.state


class RandomVariateGenerator:

    # This function is to create normal variate from uniform(0,1) distribution
    @staticmethod
    def randomBoxMullerGenerator(u1, u2, mean, variance):
        z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2 * np.pi * u2)
        random_number = mean + np.sqrt(variance) * z0
        return random_number

    # This function is to create exp variate from uniform(0,1) distribution
    @staticmethod
    def randomExpVariateGenerator(u, lambda_parameter):
        return -np.log(1 - u) / lambda_parameter
