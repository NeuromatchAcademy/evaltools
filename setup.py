import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evaltools",
    version="0.0.1",
    author="Byron Galbraith",
    author_email="byron.galbraith@gmail.com",
    description="Utility tools for evaluation and diagnostics of NMA content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeuromatchAcademy/evaltools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.7',
)
