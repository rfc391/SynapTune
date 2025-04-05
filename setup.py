
from setuptools import setup, find_packages

setup(
    name="synaptune",
    version="1.0.0",
    description="Military-grade signal analysis and neurofeedback engine",
    author="Apex Security Int Ltd",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "opencv-python",
        "protobuf",
        "grpcio",
        "influxdb",
        "psycopg2",
        "immudb-py",
        "ipfshttpclient",
        "quic-transport",
        "pycryptodome"
    ],
    entry_points={
        'console_scripts': [
            'synaptune=synaptune.cli.main:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
