from Dali import *

def main():
    sigma = 0.3

    x = np.linspace(0, 10, 1000)
    y = LinearMap(x, 2, 0.2)
    y += np.random.randn(len(x)) * sigma

    p, cov = CurveFit(LinearMap, x, y, sigma=[sigma] * len(x), absolute_sigma=True)

    print(ModelCompatibility(y, LinearMap(x, *p), [sigma] * len(x), len(x) - 2))

    PlotErrorData(x, y, None, [sigma]*len(y), 'Data and best fit', 'Time [s]', 'Distance [cm]', legend = 'Data')
    PlotFit(x, LinearMap(x, *p))

    ChangePlotIndex(1)
    PlotHistogram(EvalSquareResidues(y, LinearMap(x, *p), len(x) - 2), 'Squared residues histogram', 'Squared distances [$\\sigma^2$]', 'Occurencies', bins = 20, legend=f'df = {len(x) - 2}')

    ChangePlotIndex(2)
    PlotHistogram(EvalResidues(y, LinearMap(x, *p), len(x) - 2), 'Residues histogram', 'Distances [$\\sigma$]', 'Frequencies', legend=f'df = {len(x) - 2}')

    ShowPlot()

if __name__ == '__main__':
    InitPlotMode(mode = 'trimosaic', figSize = (16, 8), palette = 'Funky')
    main()
