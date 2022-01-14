from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="renko",
    version="0.0.10",
    description="Renko chart creator.",
    py_modules=["renko"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/aticio/renko",
    author="Özgür Atıcı",
    author_email="aticiozgur@gmail.com",
)
