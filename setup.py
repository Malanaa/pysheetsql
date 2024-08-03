from setuptools import setup, find_packages

setup(
    name='pysheetsql',
    version='0.0.1',
    description='A package for managing Google Sheets data with gspread',
    author='Malanaa',
    author_email='abdullahdotpy@gmail.com',
    packages=find_packages(),
    install_requires=[
        'gspread',
        'google-auth',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description='''
pysheetsql is cool and you should use it.
'''
)
