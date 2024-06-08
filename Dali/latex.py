import pandas as pd
from .algorithms import DetectPrecision, FormatData

buffer = []

def ExportDataTable(df, columnFormat = None, useBookTabs = False):
    if not columnFormat:
        columnFormat = '|' + 'c|' * df.shape[1]

    output = df.to_latex(index = False, escape = False, column_format=columnFormat)

    if not useBookTabs:
        output = output.replace("\\toprule", "\\hline")
        output = output.replace("\\midrule", "\\hline")
        output = output.replace("\\bottomrule", "\\hline")

    buffer.append('\n')
    buffer.append('\\begin{table}[H]\n')
    buffer.append('\\centering')
    buffer.append(output)
    buffer.append('\\caption{Enter a caption}')
    buffer.append('\\end{table}\n')

def DisplayQuantity(name: str, value: float, uncertainty: float, units: str, export = True, maxprec = 10):
    msg, texmsg = None, None

    if uncertainty != 0:
        precision = DetectPrecision(uncertainty, maxprec)

        msg = f'{name} = {FormatData(value, uncertainty, precision)} {units}'
        texmsg = f'{name} = {value:.{precision}f} \\pm {uncertainty:.{precision}f}~' + '\\mathrm{' + units + '}\\\\'
    else:
        precision = DetectPrecision(value, maxprec)

        msg = f'{name} = {value:.{precision}f} {units}'
        texmsg = f'{name} = {value:.{precision}f} ~' + '\\mathrm{' + units + '}\\\\'

    if export:
        buffer.append(texmsg)

    print(msg)

def ExportMeasurements(filename = 'export.txt'):
    with open(filename, 'w+') as f:
        for line in buffer:
            f.write(line + '\n')
