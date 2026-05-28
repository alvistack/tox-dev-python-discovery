from setuptools import setup

setup(
    name='python-discovery',
    version='1.3.2',
    description='Python interpreter discovery',
    maintainer_email='Bernát Gábor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    install_requires=[
        'filelock>=3.15.4',
        'platformdirs<5,>=4.3.6',
    ],
    extras_require={
        'docs': [
            'furo>=2025.12.19',
            'sphinx-autodoc-typehints>=3.6.3',
            'sphinx>=9.1',
            'sphinxcontrib-mermaid>=2',
            'sphinxcontrib-towncrier>=0.4',
            'towncrier>=25.8',
        ],
        'testing': [
            'covdefaults>=2.3',
            'coverage>=7.5.4',
            'pytest-mock>=3.14',
            'pytest>=8.3.5',
            'setuptools>=75.1',
        ],
    },
    packages=[
        'python_discovery',
        'python_discovery._windows',
    ],
    package_dir={'': 'src'},
)
