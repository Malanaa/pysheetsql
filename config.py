from setuptools import setup, find_packages

setup(
    name='pysheetsql',
    version='1.0.1',
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
# PySheetsQL

`pysheetsql` is a simple Python library I made to automate logging data to Google Sheets. I have designed the library to perform basic CRUD operations and use it as a small-scale database for static side projects.

## Installation

To install `pysheetsql`, use pip:

```bash
pip install pysheetsql
```

# Getting Started

## Google API Credentials

To use `pysheetsql`, you need to obtain Google Sheets API credentials. Follow these steps to get your `credentials.json` file:

1. **Create a Google Cloud Project:**
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on "Select a project" and then "New Project".
   - Enter a project name and click "Create".

2. **Enable APIs:**
   - Navigate to the [API Library](https://console.cloud.google.com/apis/library).
   - Search for and enable the Google Sheets API.
   - Also, enable the Google Docs API.

3. **Create Credentials:**
   - Go to the [Credentials](https://console.cloud.google.com/apis/credentials) page.
   - Click on "Create Credentials" and select "Service account".
   - Follow the prompts to set up the service account.
   - After creating the service account, click "Create Key" and choose JSON format. This will download your `credentials.json` file.

## Setup

To interact with Google Sheets using `pysheetsql`:

```python
from pysheetsql.start import SheetClient
```

```python
client = SheetClient(
    scopes=["https://www.googleapis.com/auth/spreadsheets"],
    credentials_file_path="path/to/credentials.json"
)
```

Replace `path/to/credentials.json` with the actual path to your downloaded `credentials.json` file.

For more usage information, visit the [PySheetsQL Documentation](https://malanaa.github.io/pysheetsql/).

''',
long_description_content_type='text/markdown',
)
