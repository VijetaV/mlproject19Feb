from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    
    '''
    This function will return the list of the requirements.
    '''
    const='-e .'
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if const in requirements:
            requirements.remove(const)

setup(
name='mlproject',
version='0.0.1',
author='Vijeta',
author_email='vashishtha.vijeta@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")



)