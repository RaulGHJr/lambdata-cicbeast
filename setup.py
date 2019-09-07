"""
lambdata-cicbeast - Collection of DS Helper Functions.
"""
import setuptools
REQUIRED = [
    "numpy",
    "pandas",
    "scipy.stats.chisquare"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
setuptools.setup(
    name="lambdata-cicbeast",
    version="0.0.3",
    author="cicbeast",
    description="Collection of DS helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/cicbeast/lambdata-cicbeast",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_required=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
