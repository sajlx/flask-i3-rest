# import setuptools
from setuptools import setup
from setuptools import find_packages


NAME = 'Flask-i3-rest-base'
VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'

AUTHOR = 'Ivan Bettarini'
AUTHOR_EMAIL = 'ivan.bettarini@gmail.com'

GITHUB_URL = 'https://github.com/sajlx/flask-i3-rest-base'
# LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    url=GITHUB_URL,
    project_urls={
        "Bug Tracker": f"{GITHUB_URL}/issues",
    },

    packages=find_packages(where="src"),
    package_dir={"": "src"},

    python_requires=">=3.7",

    keywords=['python', 'api', 'rest'],

    py_modules=['flask_i3_rest_base'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
