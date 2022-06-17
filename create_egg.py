import os
import shutil
from setuptools import setup


OUTPUT_DIR = 'output'
MODULE='contour_detection'

if __name__ == "__main__":
    setup(
        name=MODULE,
        packages=[MODULE],
        version="1.0",
        script_args=['--quiet', 'bdist_egg'], # to create egg-file only
    )

    egg_name = os.listdir('dist')[0]
    os.makedirs('dist', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    os.rename(
        os.path.join('dist', egg_name),
        os.path.join(OUTPUT_DIR, egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree(MODULE + '.egg-info')
