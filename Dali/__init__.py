# Import required third-party packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy.stats import norm, chi2, t, poisson

from scipy.optimize import curve_fit as CurveFit

from .stats import *
from .fit import *
from .color import *
from .fonts import *
from .plotting import *
from .algorithms import *
from .latex import *

__all__ = ['np', 'pd', 'plt', 'norm', 'chi2', 't', 'poisson', 'CurveFit', 'LinearMap', 'ParabolicMap', 'ArmonicMap', 'ModelCompatibility',
           'DataCompatibility', 'InitPlotMode', 'SetPlotMode', 'ChangePlotIndex', 'SetPalette', 'SetFontFamily', 'EvalResidues',
           'EvalSquareResidues', 'PlotHistogram', 'PlotData', 'PlotErrorData', 'PlotFit', 'ShowPlot', 'Clusterize', 'IntervalTimeData',
           'IntervalData', 'ReadCsv', 'DisplayQuantity', 'ExportMeasurements', 'DetectPrecision', 'ExportDataTable', 'GenerateDataframe',
           'CombineDataframes', 'ConcatenateDataframes']
