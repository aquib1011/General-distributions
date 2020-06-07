from setuptools import setup
import pathlib

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(name='general_distribution',
      version='0.0.1',
      description='probability distribution is the mathematical function that gives the probabilities of occurrence',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/aquib1011/general-distribution",
      packages=['general_distribution'],
      author = 'Aquib Iqbal',
      license = 'MIT',
      zip_safe= False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ])
      