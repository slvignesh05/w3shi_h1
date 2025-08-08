from setuptools import setup

print("installed from package")

setup(
    name='w3shi_h1',
    version='0.0.1',
    packages=['w3shi_h1'],
    description='Demo package for PyPI publishing test',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/slvignesh05/w3shi_h1',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
