from setuptools import setup

setup(
    name='penc',
    version='0.1',
    license='MIT',
    description = 'A python command-line tool to encode and decode from hex and base64',
    author = 'William Borgeaud',
    author_email = 'williamborgeaud@gmail.com',
    url = 'https://github.com/wborgeaud/penc',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        penc=main:cli
    ''',
)
