import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moj_paket",
    version="1.1.1",
    packages=setuptools.find_packages(),
    install_requires=["requests>=2.22.0"],
    url="",
    license="",
    author="Matevz",
    author_email="",
    description="moj_paket primer pakiranja lastnih modulov",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6"
)
