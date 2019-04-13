from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pacemaker-mkeshav",
    version="0.2.0",
    author="Keshav Murthy",
    author_email="mkeshav@gmail.com",
    description="To keep the old heart ticking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkeshav/pace-maker.git",
    packages=find_packages(include=('pacemaker',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[]
)