import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-dieases-classification"
AUTHOR_USER_NAME = "smitpatel151"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "patelsmit151@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for CNN",
    long_description=long_description,
    long_description_content="text/markdown",
    url={
        "Bug Tracker":f'https://github.com/smitpatel151/Chicken-dieases-classification/issues'
    },
    package_dir={'':"src"},
    packages=setuptools.find_packages(where="src")
)