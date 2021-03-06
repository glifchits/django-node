from setuptools import setup

VERSION = '2.1.0'

setup(
    name='django-node',
    version=VERSION,
    packages=['django_node'],
    package_data={
        'django_node': [
            'tests/*.py',
            'tests/package.json',
        ]
    },
    install_requires=['django'],
    description='Bindings and utils for integrating Node.js and NPM into a Django application',
    long_description='Documentation at https://github.com/markfinger/django-node',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/django-node',
)