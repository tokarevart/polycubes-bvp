import sys
from histogram import Histogram

def analyze_diameq(diameq_path, bars):
    with open(diameq_path, 'r') as f:
        diameqs = [float(d) for d in f.readlines()]

    inv_avg = len(diameqs) / sum(diameqs)
    diameqs = [d * inv_avg for d in diameqs]
    hist = Histogram(0.0, 2.7, bars)
    hist.add_from_list([d for d in diameqs if d <= 2.7])
    hist.normalize()

    ft = '%20.16e'
    print('\n'.join([(ft % a) + '\t' + (ft % h) for a, h in hist.pairs()]))

def main():
    analyze_diameq(sys.argv[1], sys.argv[2])


main()
