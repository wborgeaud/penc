from setuptools import setup, find_packages

setup(
    name='penc',
    version='0.2',
    license='MIT',
    description = 'A python command-line tool to encode and decode from hex and base64',
    author = 'William Borgeaud',
    author_email = 'williamborgeaud@gmail.com',
    url = 'https://github.com/wborgeaud/penc',
    install_requires=[
        'Click',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        penc=src.main:cli
    ''',
)
