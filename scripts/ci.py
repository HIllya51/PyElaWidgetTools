import os, subprocess
import sys
os.makedirs('collect')

for _d, _, _fs in os.walk("."):
    for _f in _fs:
        if not _f.endswith(".whl"):
            continue
        __f=os.path.join(_d, _f)
        os.rename(__f, f'collect/{_f}')
os.chdir('collect')
subprocess.run(f'twine upload -u __token__ -p {sys.argv[1]} ./*.whl')