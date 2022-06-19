from setuptools import setup, find_packages

setup(
    name='ContourDetection',
    version='1.0.0',
    description='Detects and draws boundaries around non-slide areas + compares to a threshold',
    long_description='See README',
    author='Taylor Tam',
    author_email='taylor@taylortam.com',
    url='https://github.com/TaylorT52/ContourDetection',
    packages=find_packages(exclude=['*tests*']),
)