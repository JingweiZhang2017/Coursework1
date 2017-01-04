from setuptools import setup, find_packages

setup(
    name = "greengraph",
    version = "1.0",
    author='Jingwei Zhang',
    author_email='jingwei.zhang.12@ucl.ac.uk',
    license='MIT',
    packages = find_packages(exclude=['*test']),
    install_requires = ['geopy', 'matplotlib', 'argparse', 'numpy', 'requests'],
    scripts = ['scripts/greengraph.py']
)