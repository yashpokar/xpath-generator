from setuptools import find_packages, setup

setup(
    name='xpath-generator',
    description='Automatic xpath & spider generator',
    version='0.0.1-dev',
    packages=find_packages(),
    author='Yash Pokar',
    author_email='hello@yashpokar.com',
    install_requires=[
        'lxml',
        'requests',
    ],
    entry_points={
        'console_scripts': ['genxpath = xpath_generator.cmd:execute'],
    },
    zip_safe=False,
)
