from setuptools import setup
with open('README.md',"r") as f:
    long_description = f.read()
setup(
    name='pyapex',
    packages=['pyapex'],
    version='0.0.2',

    license='MIT',

    description='Create interactive html charts',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    author='nicodemus opon',
    author_email='hello@nicopon.me',

    url='https://github.com/nicodemus-opon/pyapex',

    download_url='https://github.com/nicodemus-opon/pyapex/archive/refs/tags/v_0.0.2.tar.gz',
    keywords=['chart', 'plotting'],
    install_requires=[
        'uuid'
    ],
    classifiers=[

        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
