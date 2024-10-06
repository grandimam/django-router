# setup.py
from setuptools import setup, find_packages

setup(
    name='django-router',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2',
    ],
    description='A Django routing framework using decorators.',
    author='Grandimam',
    author_email='hi@grandimam.com',
    url='https://github.com/grandimam/django-router',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
