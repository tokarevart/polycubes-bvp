import sys
from pathlib import Path
from histogram import Histogram


def stress_curve(ndir, r):
    with open(Path(ndir) / ('r' + str(r)) / 'bvp.key' / 'partout' / 'rvout.dat') as f:
        strain_stresses = f.readlines()[1:]
    return [float(ss.split()[1]) for ss in strain_stresses]

def stress_curves(ndir, rbeg, rend):
    rbeg, rend = int(rbeg), int(rend)
    return [stress_curve(ndir, r) for r in range(rbeg, rend + 1)]

def stress_curve_of_realiz(ndir, rbeg, rend):
    rbeg, rend = int(rbeg), int(rend)
    return list(zip(*stress_curves(ndir, rbeg, rend)))

def analyze_distr(ndir, rbeg, rend, bars):
    rbeg, rend, bars = int(rbeg), int(rend), int(bars)

    rscurve = stress_curve_of_realiz(ndir, rbeg, rend)
    realizes = rscurve[1]
    rmin, rmax = min(realizes), max(realizes)
    hist = Histogram(rmin, rmax, bars)
    hist.add_from_list(realizes)
    hist.normalize()

    ft = '%20.16e'
    print('\n'.join([(ft % a) + '\t' + (ft % h) for a, h in hist.pairs()]))

def main():
    analyze_distr(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


main()
