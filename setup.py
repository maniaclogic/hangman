from setuptools import setup

setup(
    # other arguments here...
    entry_points={
        'console_scripts': [
            'play = src.play:main',
        ],
    },
)