import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bjoern",
    version = "0.1",
    author = "Fabian Yamaguchi",
    author_email = "fyamagu@gwdg.de",
    description = "A python interface to the code analysis tool bjoern.",
    license = "GPLv3",
    url = "http://github.com/fabsx00/",
    long_description = read('README.md'),
    packages = find_packages(),
    package_data={"joern": ['bjoernsteps/*.groovy',]},
    install_requires = ['py2neo-gremlin == 0.1'],
    dependency_links = ['https://github.com/fabsx00/py2neo-gremlin/tarball/master/#egg=py2neo-gremlin-0.1']
)
