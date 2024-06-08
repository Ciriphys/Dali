import pandas as pd
from numpy import mean, std, pad, nan

def Clusterize(x, y, size):
    if len(x) != len(y):
        raise ValueError('Lenghts mismatch!')

    n = int(len(x) / size)

    xc = []
    yc = []
    sxc = []
    syc = []

    for i in range(n - 1):
        xc.append(mean(x[i*size:(i+1)*size]))
        yc.append(mean(y[i*size:(i+1)*size]))

        sxc.append(x[(i+1)*size] - x[i*size])
        syc.append(std(y[i*size:(i+1)*size], ddof=1))

    return xc, yc, sxc, syc

def IntervalTimeData(xdata, tdata, t0, t1):
    time = []
    xv = []

    for x,t in zip(xdata, tdata):
        if t >= t0 and t <= t1:
            time.append(t)
            xv.append(x)

    return xv, time

def IntervalData(data, first, last):
    result = []

    for d in data:
        if d >= first and t <= last:
            result.append(d)

    return result

def GenerateDataframe(labels, *args):
    maxLen = max(len(arr) for arr in args)
    aligned = []

    for arr in args:
        alarr = pad(arr, (0, maxLen - len(arr)), constant_values=nan)
        aligned.append(alarr)

    df = pd.DataFrame({label: col for label, col in zip(labels, aligned)})

    return df

def CombineDataframes(dataDf, uncDf):
    if dataDf.shape[1] != uncDf.shape[1]:
        raise ValueError('Lengths mismatch!')

    combined = pd.DataFrame({
        col1: dataDf[col1].combine(uncDf[col2], FormatData)
        for col1, col2 in zip(dataDf.columns, uncDf.columns)
    })

    return combined

def ConcatenateDataframes(*args):
    return pd.concat(args, axis=1)

def DetectPrecision(value, maxprec = 10):
    precision = 1

    while round(value, precision) == 0 and precision < maxprec:
        precision += 1

    return precision

def ReadCsv(filename, label = None, separator = ','):
    df = pd.read_csv(filename, sep = separator)
    if label:
        df.columns = label

    return df

def FormatData(value, uncertainty, precision = -1):
    if precision < 0:
        precision = DetectPrecision(uncertainty)

    return f'{value:.{precision}f} ± {uncertainty:.{precision}f}'
