import numpy as np

def HistToPDF(data, bins = 10):
    return np.histogram(data, bins = bins, density = True)
