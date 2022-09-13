from setuptools import setup, find_packages

setup(
    name='pymonitoring',
    version='0.0.1',
    python_requires='>=3.7',
    description="pymonitoring like pytest just for monitoring",
    author="Noa gradovitch",
    author_email="noahgrad@gmail.com",
    url="https://github.com/noahgrad/pymonitor",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
    ],
    zip_safe=False
)
