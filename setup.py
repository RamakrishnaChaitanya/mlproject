from setuptools import find_packages # finds the packages being used in our ML app adirectory
from setuptools import setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [reqs.replace("\n", " ") for reqs in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
        
        return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Ramakrishna",
    author_email="rkchaitanya02gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt'),

)







