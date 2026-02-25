from setuptools import find_packages,setup
from typing import List


hypen_e_dot='-e .'


def get_requirements(file_path:str)->List[str]:
    """
    THIS FUNCTION WILL RETURN LIST OF REQUIREMENTS
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name="ml_project",                
    version="0.0.1",                  
    author="SAKSHAM ARORA",            
    author_email="saksham0666@gmail.com",
    description="END TO END ML PROJECT",
    packages=find_packages(),             
    install_requires=get_requirements('requirements.txt'),           
)