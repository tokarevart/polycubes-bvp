import sys
from histogram import Histogram

def analyze_diameq(diameq_path, bars):
    with open(diameq_path, 'r') as f:
        diameqs = [float(d) for d in f.readlines()]

    dmin, dmax = min(diameqs), max(diameqs)
    hist = Histogram(0.0, 2.7, bars)
    hist.add_from_list([d / dmax * 2.7 for d in diameqs])
    hist.normalize()

    ft = '%20.16e'
    print('\n'.join([(ft % a) + '\t' + (ft % h) for a, h in hist.pairs()]))

def main():
    analyze_diameq(sys.argv[1], sys.argv[2])


main()
