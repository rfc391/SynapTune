from setuptools import setup, find_packages

setup(
    name='ADHD_Aid_NeuroSignal_Companion',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy', 'scipy', 'flask'],
)
