buffer = []

def DisplayQuantity(name: str, value: float, uncertainty: float, units: str, precision = 3, export = True):
    msg, texmsg = None, None

    if uncertainty != 0:
        msg = f'{name} = {round(value, precision)} ± {round(uncertainty, precision)} {units}'
        texmsg = f'{name} = {round(value, precision)} \\pm {round(uncertainty, precision)}~' + '\\mathrm{' + units + '}'
    else:
        msg = f'{name} = {round(value, precision)} {units}'
        texmsg = f'{name} = {round(value, precision)} ~' + '\\mathrm{' + units + '}'

    if export:
        buffer.append(texmsg)

    print(msg)

def ExportMeasurements(filename = 'export.txt'):
    with open(filename, 'w+') as f:
        for line in buffer:
            f.write(line + '\n')
