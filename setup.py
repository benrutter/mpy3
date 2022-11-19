from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='mpy3',
    version='1.1',
    author='benrutter',
    description='Ultra-minimal command line mp3 player for windows/linux/mac',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/benrutter/mpy3',
    packages=['mpy3'],
    entry_points={
        'console_scripts': [
            'mpy3 = mpy3.main:run_app',
        ],
    },
    install_requires=[
        'pygame',
        'typer',
        'rich',
    ],
)
