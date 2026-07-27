from setuptools import find_packages,setup 
from typing import List

hypen_e = '-e .'
def get_req(Filepath:str) -> List[str]:
    requirements = []
    with open(Filepath) as file :
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements

setup(
    name = 'Machine Learning Project 1',
    version = '0.0.1',
    author= 'Aditya kumar',
    author_email= 'adityakumaro12b@gmail.com',
    packages= find_packages(),
    install_requires= get_req('Requirements.txt')

)