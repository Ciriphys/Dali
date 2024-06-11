import matplotlib.pyplot as plt
import os

from . import fonts as f
from . import color as c

currentColorIndex = 0
zOrder = 3
showLegend = False
labelFontSize = 0
titleFontSize = 0

plotExists = False

figure = None
axes = None

maxPlotIndex = 0
currentPlotIndex = 0

folderPath = None

plotMode = ['normal', 'bimosaic', 'trimosaic']

def InitPlotMode(style = 'seaborn-v0_8-whitegrid', palette = 'Funky', fontFamily = f.HelveticaFF, fontSizeL = 12, fontSizeT = 14, figSize = (10, 6), mode = 'normal', path = 'Images/'):
    global labelFontSize
    global titleFontSize
    global folderPath
    global figure
    global axes

    if style:
        plt.style.use(style)

    c.colorPalette = c.palette[palette]
    f.defaultFontFamily = fontFamily

    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['font.weight'] = 'regular'

    labelFontSize = fontSizeL
    titleFontSize = fontSizeT

    folderPath = path

    SetPlotMode(mode, figSize)

def SetPlotMode(mode = 'normal', figSize = (10, 6)):
    global maxPlotIndex
    global figure
    global axes

    if plotExists:
        ShowPlot()

    if mode == 'bimosaic':
        figure, axes = plt.subplots(1, 2, figsize = figSize)
        maxPlotIndex = 2

    elif mode == 'trimosaic':
        figure, axes = plt.subplots(1, 3, figsize = figSize)
        maxPlotIndex = 3

    else:
        plt.figure(figsize = figSize)
        figure, axes = None, None

def PlotData(x, y, title = None, xlabel = None, ylabel = None, marker = '.', legend = None, xLogScale = False, yLogScale = False, xLim = None, yLim = None):
    global currentColorIndex
    global showLegend
    global zOrder
    global plotExists

    plotExists = True
    SetMetadata(title, xlabel, ylabel)

    if figure:
        if xLogScale:
            axes[currentPlotIndex].set_xscale('log')
        if yLogScale:
            axes[currentPlotIndex].set_yscale('log')
        if xLim:
            axes[currentPlotIndex].set_xlim(*xLim)
        if yLim:
            axes[currentPlotIndex].set_ylim(*yLim)
        axes[currentPlotIndex].plot(x, y, marker, label=legend, color = c.colorPalette[currentColorIndex], zorder = zOrder)
        zOrder += 1
    else:
        if xLogScale:
            plt.xscale('log')
        if yLogScale:
            plt.yscale('log')
        if xLim:
            plt.xlim(*xLim)
        if yLim:
            plt.ylim(*yLim)
        plt.plot(x, y, marker, label=legend, color = c.colorPalette[currentColorIndex], zorder = zOrder)
        zOrder += 1

    if legend:
        showLegend = True

    currentColorIndex = 0 if currentColorIndex > 6 else currentColorIndex + 1

def PlotHistogram(x, title = None, xlabel = None, ylabel = None, legend = None, wBin = 0.8, bins = 10, xLogScale = False, yLogScale = False, xLim = None, yLim = None):
    global currentColorIndex
    global showLegend
    global zOrder
    global plotExists

    plotExists = True
    SetMetadata(title, xlabel, ylabel)

    if figure:
        if xLogScale:
            axes[currentPlotIndex].set_xscale('log')
        if yLogScale:
            axes[currentPlotIndex].set_yscale('log')
        if xLim:
            axes[currentPlotIndex].set_xlim(*xLim)
        if yLim:
            axes[currentPlotIndex].set_ylim(*yLim)
        axes[currentPlotIndex].hist(x, rwidth = wBin, bins = bins, color = c.colorPalette[currentColorIndex], label = legend)
    else:
        if xLogScale:
            plt.xscale('log')
        if yLogScale:
            plt.yscale('log')
        plt.hist(x, rwidth = wBin, bins = bins, color = c.colorPalette[currentColorIndex], label = legend)
        if xLim:
            plt.xlim(*xLim)
        if yLim:
            plt.ylim(*yLim)

    if legend:
        showLegend = True

    currentColorIndex = 0 if currentColorIndex > 6 else currentColorIndex + 1

def PlotErrorData(x, y, xerr = None, yerr = None, title = None, xlabel = None, ylabel = None, marker = '.', legend = None, xLogScale = False, yLogScale = False, xLim = None, yLim = None):
    global currentColorIndex
    global showLegend
    global zOrder
    global plotExists

    plotExists = True
    SetMetadata(title, xlabel, ylabel)

    if figure:
        if xLogScale:
            axes[currentPlotIndex].set_xscale('log')
        if yLogScale:
            axes[currentPlotIndex].set_yscale('log')
        if xLim:
            axes[currentPlotIndex].set_xlim(*xLim)
        if yLim:
            axes[currentPlotIndex].set_ylim(*yLim)
        axes[currentPlotIndex].errorbar(x, y, xerr=xerr, yerr=yerr, fmt=marker, label=legend, color = c.colorPalette[currentColorIndex], zorder = zOrder)
        zOrder += 1
    else:
        if xLogScale:
            plt.xscale('log')
        if yLogScale:
            plt.yscale('log')
        if xLim:
            plt.xlim(*xLim)
        if yLim:
            plt.ylim(*yLim)
        plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt=marker, label=legend, color = c.colorPalette[currentColorIndex], zorder = zOrder)
        zOrder += 1

    if legend:
        showLegend = True

    currentColorIndex = 0 if currentColorIndex > 6 else currentColorIndex + 1

def ChangePlotIndex(index):
    global currentPlotIndex
    global showLegend

    if showLegend:
        ShowLegend()

    if index < maxPlotIndex and index >= 0:
        currentPlotIndex = index

def PlotFit(x, y, title = None, xlabel = None, ylabel = None, marker = '-', legend = 'Best fit', xLogScale = False, yLogScale = False, xLim = None, yLim = None):
    PlotData(x, y, title, xlabel, ylabel, marker, legend, xLogScale, yLogScale, xLim, yLim)

def ShowPlot(filename = None):
    global zOrder
    global plotExists
    global showLegend

    plotExists = False

    if filename:
        if not os.path.exists(folderPath):
            os.mkdir(folderPath)
        plt.savefig(folderPath + filename)

    if showLegend:
        ShowLegend()

    plt.show()
    zOrder = 3
    currentColorIndex = 0

def SetMetadata(title, xlabel, ylabel):
     if figure:
        if title:
            if f.defaultFontFamily:
                axes[currentPlotIndex].set_title(title, **f.defaultFontFamily, fontsize = titleFontSize)
            else:
                axes[currentPlotIndex].set_title(title, fontsize = titleFontSize)

        if xlabel:
            if f.defaultFontFamily:
                axes[currentPlotIndex].set_xlabel(xlabel, **f.defaultFontFamily, fontsize = labelFontSize)
            else:
                axes[currentPlotIndex].set_xlabel(xlabel, fontsize = labelFontSize)

        if ylabel:
            if f.defaultFontFamily:
                axes[currentPlotIndex].set_ylabel(ylabel, **f.defaultFontFamily, fontsize = labelFontSize)
            else:
                axes[currentPlotIndex].set_ylabel(ylabel, fontsize = labelFontSize)
     else:
        if title:
            if f.defaultFontFamily:
                plt.title(title, **f.defaultFontFamily, fontsize = titleFontSize)
            else:
                plt.title(title, fontsize = titleFontSize)

        if xlabel:
            if f.defaultFontFamily:
                plt.xlabel(xlabel, **f.defaultFontFamily, fontsize = labelFontSize)
            else:
                plt.xlabel(xlabel, fontsize = labelFontSize)

        if ylabel:
            if f.defaultFontFamily:
                plt.ylabel(ylabel, **f.defaultFontFamily, fontsize = labelFontSize)
            else:
                plt.ylabel(ylabel, fontsize = labelFontSize)

def ShowLegend():
    global showLegend

    if figure:
        axes[currentPlotIndex].legend(fancybox = True, framealpha=1.0, frameon = True)
    else:
        plt.legend(fancybox = True, framealpha=1.0, frameon = True)

    showLegend = False
