from pandas import read_csv

buffer = []

def Clusterize(x, y, size):
    if len(x) != len(y):
        raise 'Lenghts mismatch!'

    n = int(len(x) / size)

    xc = []
    yc = []
    sxc = []
    syc = []

    for i in range(n - 1):
        xc.append(np.mean(x[i*size:(i+1)*size]))
        yc.append(np.mean(y[i*size:(i+1)*size]))

        sxc.append(x[(i+1)*size] - x[i*size])
        syc.append(np.std(y[i*size:(i+1)*size], ddof=1))

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

def ReadCsv(filename, label = None, separator = ','):
    df = read_csv(filename, sep = separator)
    if label:
        df.columns = label

    return df
