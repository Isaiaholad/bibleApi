from setuptools import setup, find_packages

setup(
    name='bible_api',
    version='0.1.0',
    description='A Python package for querying and analyzing the Bible dataset',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='isaiaholad',
    author_email='isaiaholad@gmail.com',
    url='https://github.com/isaiaholad/bible_api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'wordcloud'
    ],
    entry_points={
        'console_scripts': [
            'bible_api=bible_api.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
