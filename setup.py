from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .' # this is for running the setup.py automatically in requirements.py

def get_requirements(file_path: str)-> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'mlproject_end2end',
    version='0.0.1',
    author='Neda',
    packages=find_packages(),
    requires= get_requirements('requirements.txt')
)
