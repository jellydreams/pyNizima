from setuptools import setup, find_packages

setup(
    name="pynizima",
    version="1.0",
    author="Jelly Dreams",
    description="Python library for interacting with the NizimaLIVE API via WebSocket",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jellydreams/pynizima",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    dependencies=[
        "websockets>=14.1",
    ]
)
