colorPalette = None

palette = {
    'Solaris':          ['#302b27', '#dc322f', '#268bd2', '#859900', '#b58900', '#6c71c4', '#2aa198', '#b58900'],
    'Enhance':          ['#f24c00', '#33a3d0', '#d3b88c', '#656256', '#230903', '#fe938c', '#b3b3b3', '#6a2e35'],
    'Funky':            ['#44af69', '#f8333c', '#2b9eb3', '#fcab10', '#0077b6', '#987774', '#beee62', '#f7717d'],
    'Lovely':           ['#bd4f6c', '#3caabb', '#694873', '#a1c084', '#136f63', '#f09d51', '#9f2042', '#43b929'],
    'Trisolaris':       ['#cb4b16', '#859900', '#7175c4', '#2aa198', '#298cd2', '#b58900', '#dc322f', '#d33682'],
    'Default':          ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
}

def SetPalette(pal = 'Funky'):
    colorPalette = palette[pal]
