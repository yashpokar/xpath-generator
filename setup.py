from setuptools import find_packages, setup

setup(
    name='xpath_generator',
    description='',
    version='0.0.1alpha',
    packages=find_packages(),
    install_requires=[
        'lxml',
        'requests',
    ],
    entry_points={
        'console_scripts': ['genxpath = xpath_generator.cmd:execute'],
    },
)
