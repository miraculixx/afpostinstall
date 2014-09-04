'''
Created on Dec 17, 2013

@author: patrick
'''
import os
from setuptools import setup, find_packages
from extensions import PostInstaller

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

dist = setup(
    name='afpostinstall',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='commercial',  # example license
    description='appfog python post-pip installer',
    long_description=README,
    url='http://www.novapp.ch/',
    author='Patrick Senti',
    author_email='ps@novapp.ch',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Commercial', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # replace these appropriately if you are using Python 3 
        'Programming Language :: Python :: 2', 
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    setup_requires=[
        'psutil==2.1.1'
    ], 
    install_requires=[
        'psutil==2.1.1'
    ], 
    dependency_links=[
    ],
)

# note: this will always run, whether the install was successful or not!
PostInstaller(dist).run()
