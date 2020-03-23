import os
from setuptools import find_packages, setup

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sequential-uuids',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>=3',
    author='Moeen Zamani',
    author_email='moeen.zamani@gmail.com',
    license='MIT',
    description='Sequential UUID generator.',
    url='https://github.com/moeenz/sequential-uuids',
    classifiers=[
        'Environment :: Console',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography'
    ],
)
