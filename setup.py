
from setuptools import setup

setup(
    name = "biribiri.rpc.client",
    version = "0.1",
    description = 'Simple client class for accessing JSON rpc web-servers',
    author = 'Ilya Petrov',
    author_email = 'ilya.muromec@gmail.com',
    url = 'http://biribiri.enodev.org',
    packages = ['biribiri', 'biribiri.rpc', 'biribiri.rpc.client'],
    license = "BSDL",
    install_requires = ['simplejson',],
    scripts = [],
)
