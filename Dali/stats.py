from scipy.stats import norm, chi2
from numpy import sum, abs

def ModelCompatibility(measurements, theoretical, deviations, dof):
    val = [((m - t) / d) ** 2 for m, t, d in zip(measurements, theoretical, deviations)]
    chi0 = sum(val)

    return chi0, 1 - chi2(df = dof).cdf(chi0)

def DataCompatibility(first, second, deviation):
    t = abs(first - second) / deviation

    return t, (1 - (norm.cdf(t) - norm.cdf(-t)))

def EvalSquareResidues(measurements, theoretical, dof):
    residues = [((m - t) / dof) ** 2 for m, t in zip(measurements, theoretical)]
    return residues

def EvalResidues(measurements, theoretical, dof):
    residues = [(m - t) / dof for m, t in zip(measurements, theoretical)]
    return residues
