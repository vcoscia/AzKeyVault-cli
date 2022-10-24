from setuptools import setup 
from setuptools import find_packages

def readRequirements():
  pkgs = []
  with open("requirements.txt",'r') as fp : 
    pkgs.append(fp.readline())
  return pkgs
setup(
  name='AzKeyVaultManager',
  version='1.0.0',
  description='Tool to manage a keyvault hosted on azure',
  author='Vincenzo Coscia',
  packages=find_packages(),
  python_requires=">=3.8, <4",
  install_requires=readRequirements(),
  entry_points={
    'console_scripts':[
        'AzKeyVault-cli = AzKeyVault.main:main',
    ],
  },
)


