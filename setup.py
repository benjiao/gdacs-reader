import setuptools


setuptools.setup(
    name='gdacs-reader',
    keywords=['GDACS'],
    version='0.1.0',
    url='https://github.com/benjiao/gdacs-reader',
    license='BSD',
    author='Benjie Jiao',
    author_email='hi@benjie.me',
    description='An unofficial Python library for fetching updates from the Global Disaster Alert and Coordination System',
    long_description='An unofficial Python library for fetching updates from the Global Disaster Alert and Coordination System',
    packages=setuptools.find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=['requests', 'geojson'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
