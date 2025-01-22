from setuptools import setup, find_packages

setup(
    
    name='csv2sql',             
    version='0.2',               
    packages=find_packages(),
    
    url='https://github.com/Dev8-Community/csv2sql', 
    license='MPL-2.0', 
    
    author='Sean Francis N. Ballais',
    author_email='sean@seanballais.com',
    
   
    description='csv2sql creates an SQLite database out of a CSV file for use primarily by Dev8.',
    
    entry_points={
        'console_scripts': ['csv2sql = csv2sql.__main__:main']
    }
)
