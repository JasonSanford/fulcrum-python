try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['requests>=2.1.0']

setup(
    name='fulcrum',
    version='0.0.1',
    description='Python wrapper for the Fulcrum API',
    author='Jason Sanford',
    author_email='jasonsanford@gmail.com',
    url='https://github.com/JasonSanford/fulcrum-python',
    packages= ['fulcrum',],
    install_requires=requires,
    license='Apache License',
)