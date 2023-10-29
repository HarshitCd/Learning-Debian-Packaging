from setuptools import setup, find_packages

setup(
    name="sample",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello = module_1.src.say_hello:main',
            'world = module_2.src.say_world:main',
        ],
    }
)