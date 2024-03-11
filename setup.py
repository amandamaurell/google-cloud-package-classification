from setuptools import setup
from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='penguin',
      description="package to exemplify how to use GC storage and GBQ",
      packages=find_packages(), # NEW: find packages automatically
      install_requires=requirements) # NEW
