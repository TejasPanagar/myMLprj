from setuptools import find_packages, setup
from typing import List

connector = '-e .'

def get_reqs(file_path: str) -> List[str]:
    reqs = []
    with open(file_path, "r") as file_obj:
        reqs = file_obj.readlines()  # ✅ Corrected `redaline()` to `readlines()`
        reqs = [req.replace("\n", "") for req in reqs]  # ✅ Fixed newline replacement
        if connector in reqs:
            reqs.remove(connector)  # ✅ Removes '-e .' from the list

    return reqs

setup(
    name='mlprj',
    version='3.11.7',
    author='tej',
    author_email='tejaskrishna4321@gmail.com',
    packages=find_packages(),
    install_requires=get_reqs('Reqs.txt')  # ✅ Fixed missing quotes and spelling error
)
