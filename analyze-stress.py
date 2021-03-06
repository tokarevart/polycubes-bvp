import sys
import math
from pathlib import Path


def stress_curve(ndir, r):
    with open(Path(ndir) / ('r' + str(r)) / 'bvp.key' / 'partout' / 'rvout.dat') as f:
        strain_stresses = f.readlines()[1:]
    return [float(ss.split()[1]) for ss in strain_stresses]

def stress_curves(ndir, rbeg, rend):
    rbeg, rend = int(rbeg), int(rend)
    return [stress_curve(ndir, r) for r in range(rbeg, rend + 1)]

def stress_mean_curve(ndir, rbeg, rend):
    return [sum(rs) / len(rs) for rs in list(zip(*stress_curves(ndir, rbeg, rend)))]

def stress_stddev_curve(ndir, rbeg, rend):
    rcurves = stress_curves(ndir, rbeg, rend)
    return [
        math.sqrt(sum((s - mean)**2 for s in rs) / (len(rs) - 1))
        for rs, mean in list(zip(list(zip(*rcurves)), [sum(rs) / len(rs) for rs in zip(*rcurves)]))
    ]

def stress_mean_curves(nbeg, nend, rbeg, rend):
    nbeg, nend = int(nbeg), int(nend)
    return [stress_mean_curve('n' + str(n), rbeg, rend) for n in range(nbeg, nend + 1)]

def stress_stddev_curves(nbeg, nend, rbeg, rend):
    nbeg, nend = int(nbeg), int(nend)
    return [stress_stddev_curve('n' + str(n), rbeg, rend) for n in range(nbeg, nend + 1)]

def analyze_stress(nbeg, nend, rbeg, rend):
    print('curves in columns')
    ft = '%20.16e'
    mean_curves = stress_mean_curves(nbeg, nend, rbeg, rend)
    print('means')
    for curve in zip(*mean_curves):
        print('\t'.join([ft % s for s in curve]))
    print('means tr')
    for curve in mean_curves:
        print('\t'.join([ft % s for s in curve]))

    stddev_curves = stress_stddev_curves(nbeg, nend, rbeg, rend)
    print('stddevs')
    for curve in zip(*stddev_curves):
        print('\t'.join([ft % s for s in curve]))
    print('stddevs tr')
    for curve in stddev_curves:
        print('\t'.join([ft % s for s in curve]))


def analyze_stress_fixn(ndir, rbeg, rend):
    rbeg, rend = int(rbeg), int(rend)
    mean_curve = stress_mean_curve(ndir, rbeg, rend)
    stddev_curve = stress_stddev_curve(ndir, rbeg, rend)
    ft = '%20.16e'
    print('\n'.join([(ft % m) + '\t' + (ft % d) for m, d in zip(mean_curve, stddev_curve)]))


def main():
    if len(sys.argv) == 4:
        analyze_stress_fixn(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        analyze_stress(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


main()
