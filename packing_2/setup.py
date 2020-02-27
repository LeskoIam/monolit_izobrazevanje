from setuptools import setup, find_packages

with open("README.md", "r") as md_file:
    long_description = md_file.read()

setup(
    name='dict2list',
    version='1.0.0.',
    packages=find_packages(),
    # install_requires=[],
    url='',
    license='',
    author='Matevz',
    author_email='matevz@email.si',
    description='nekaj',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6"
)
