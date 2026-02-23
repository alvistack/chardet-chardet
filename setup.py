from setuptools import setup

setup(
    name='chardet',
    version='6.0.0.post1',
    description='Universal encoding detector for Python 3',
    author_email='Mark Pilgrim <mark@diveintomark.org>',
    maintainer='Ian Cordasco',
    maintainer_email='Dan Blanchard <dan.blanchard@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
    entry_points={
        'console_scripts': [
            'chardetect = chardet.cli.chardetect:main',
        ],
    },
    packages=[
        'chardet',
        'chardet.cli',
        'chardet.metadata',
    ],
)
