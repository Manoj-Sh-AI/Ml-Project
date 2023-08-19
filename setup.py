# WHEN THIS FILE IS EXECUTED IT INSTALLS ALL THE PACKAGES WHOSE NAMES ARE MENTIONED IN 'requirements.txt' AUTOMATICALLY THROUGH 'get_requirements()' FUNCTION

from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'  # this srting present in requirement.txt is used to map to setup.py and run simultaniously in order to build the package 


def get_requirements(file_path:str)->List[str]:
    # This function is used to fetch the important libraries which are specified in 'requirement.txt'
    # This function will return the list of requirements
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # as '\n' gets added at the end of every line

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
setup(
    # Important parameters
    name='Ml-Project',   # name of Directory
    version='0.0.1',     # verson can be updated, whenever next version comes
    author='Manoj',
    author_email='shmanoj100@gmail.com',
    packages= find_packages(),  # powerful function which fetches the packages
    # install_require=['pandas', 'numpy', 'seaborn', 'matplotlib'],  # automatically all these will be installed
    install_require = get_requirements('requirements.txt')

)