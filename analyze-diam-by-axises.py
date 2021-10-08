import sys

def analyze_diam_by_axises(diameq_path):
    xavg, yavg, zavg = 0.0, 0.0, 0.0
    with open(diameq_path, 'r') as f:
        lines = f.readlines()
        ngr = len(lines)
        for coors in lines:
            xmin, xmax, ymin, ymax, zmin, zmax = coors.split()
            xavg += float(xmax) - float(xmin)
            yavg += float(ymax) - float(ymin)
            zavg += float(zmax) - float(zmin)

    xavg /= ngr
    yavg /= ngr
    zavg /= ngr

    print(f'xavg={xavg}')
    print(f'yavg={yavg}')
    print(f'zavg={zavg}')

def main():
    analyze_diam_by_axises(sys.argv[1])


main()
