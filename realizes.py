import sys
import realiz


def realizes_fixn(ndir, rbeg, rend, num_thr, gpu_id):
    rbeg, rend = int(rbeg), int(rend)
    for r in range(rbeg, rend + 1):
        realiz.run_realiz(
            ndir, 'r' + str(r),
            num_thr, gpu_id
        )


def main():
    if len(sys.argv) == 6:
        realizes_fixn(
            ndir=sys.argv[1], rbeg=sys.argv[2], rend=sys.argv[3],
            num_thr=sys.argv[4], gpu_id=sys.argv[5]
        )
    else:
        nbeg, nend = int(sys.argv[1]), int(sys.argv[2])
        for n in range(nbeg, nend + 1):
            realizes_fixn(
                ndir='n' + str(n), rbeg=sys.argv[3],
                rend=sys.argv[4], num_thr=sys.argv[5],
                gpu_id=sys.argv[6]
            )


if __name__ == '__main__':
    main()
