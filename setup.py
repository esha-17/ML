from setuptools import find_packages, setup
from typing import List
HYPEN_E_dot ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    requirement list
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]
        if HYPEN_E_dot in requirements:
            requirements.remove(HYPEN_E_dot)
    return requirements

setup(
name ='ML',
version ='0.0.1',
author ='Esha',
authour_email ='eshajaiswal905@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)