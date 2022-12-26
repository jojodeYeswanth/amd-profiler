import os
from setuptools import setup,find_packages
import wrapper

with open('requirement.txt') as fp:
    install_requires = fp.read()
setup(name='WrapperCode',version='0.0.1',packages=find_packages(),description='It is wrapper team project',install_requires=['pandas==1.5.2','pyinstaller==5.7.0','requests==2.22.0','tqdm==4.64.1'])
