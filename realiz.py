import os
import stat
import sys
import shutil
import subprocess
from pathlib import Path


def replace_line_in_file(path, pat, to):
    with open(path) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip() == pat:
            lines[i] = to + '\n'
    with open(path, 'w') as f:
        f.writelines(lines)


def run_realiz(ndir, rdir, num_thr, gpu_id):
    femdir_path = Path(os.environ['HOME']) / 'fem'
    fembindir_path = femdir_path / 'bin'
    tems_path = femdir_path / 'polycubes-bvp' / 'templates'
    femexe_path = fembindir_path / 'fem'
    config_path = tems_path / 'config'
    param_path = tems_path / 'param'

    prevwd = os.getcwd()
    os.chdir(ndir)
    rdir = Path(rdir)
    os.mkdir(rdir)

    with open('scale.cfg', 'r') as f:
        scale = f.readline().strip()

    shutil.copytree(config_path, rdir / 'config')
    shutil.copytree(param_path, rdir / 'param')
    shutil.copy(tems_path / 'input.inp', rdir)

    replace_line_in_file(rdir / 'config' / 'fem.cfg', 'NUM_THR', num_thr)
    replace_line_in_file(rdir / 'config' / 'slae.cfg', 'GPU_ID', gpu_id)
    replace_line_in_file(rdir / 'param' / 'solstat.prm', 'SCALE', scale)

    runfem_path = rdir / 'runfem.sh'
    with open(runfem_path, 'w') as f:
        st = os.stat(runfem_path)
        os.chmod(runfem_path, st.st_mode | stat.S_IEXEC)
        rfhead = (tems_path / 'runfem-head.sh').read_text()
        print(rfhead, file=f)
        print(
            str(femexe_path) + ' '
            + str(rdir.absolute()) + '/',
            file=f
        )

    runfemabs = runfem_path.absolute()
    os.chdir(rdir)
    subprocess.run([f'{runfemabs}'])
    shutil.rmtree('d3plot')
    os.chdir(prevwd)


if __name__ == '__main__':
    run_realiz(
        ndir=sys.argv[1], rdir=sys.argv[2],
        num_thr=sys.argv[3], gpu_id=sys.argv[4]
    )
