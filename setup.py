from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'  # this string present in requirement.txt is used to map to setup.py and run simultaneously to build the package


def get_requirements(file_path: str) -> List[str]:
    # This function is used to fetch the important libraries which are specified in 'requirements.txt'
    # This function will return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  # as '\n' gets added at the end of every line

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    # Important parameters
    name='Ml-Project',   # name of Directory
    version='0.0.1',     # version can be updated, whenever the next version comes
    author='Manoj',
    author_email='shmanoj100@gmail.com',
    packages=find_packages(),  # powerful function which fetches the packages
    install_requires=get_requirements('requirements.txt')
)
