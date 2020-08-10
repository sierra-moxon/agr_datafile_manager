import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agr-datafile-manager-sierramoxon", # Replace with your own username
    version="0.0.1",
    author="Alliance",
    author_email="help@alliancegenome.org",
    description="A package used to download and process files from the FMS as well as store neo4j connection information",
    long_description="A package used to download and process files from the FMS as well as store neo4j connection information",
    long_description_content_type="text/markdown",
    url="https://github.com/sierramoxon/agr_datafile_manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
