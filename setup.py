from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='googlechatbot',
    version='1.1.0',
    description='A small package to simplify the creation of Google Chat Bots',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Javier Collado',
    author_email='javicv@gmail.com',
    url='https://github.com/javicv/googlechatbot',
    license="Apache License 2.0",
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=["requests"]
)
