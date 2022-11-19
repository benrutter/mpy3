from setuptools import setup

setup(
    name='mpy3',
    version='1.0',
    author='benrutter',
    description='Ultra-minimal command line mp3 player for windows/linux/mac',
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
