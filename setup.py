import setuptools
import distutils.core

setuptools.setup(
    name='brave-bookmarks',
    version="1.0.1",
    author='Author',
    long_description_content_type='text/markdown',
    author_email='Email',
    description='',
    license='MIT',
    keywords='bookmarks, brave, command-line',
    url='',
    packages=["brave_bookmarks"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'bravemarks=brave_bookmarks.main:bookmarks',
            'bravemark=brave_bookmarks.main:bookmark',
            'brave-bookmarks=brave_bookmarks.main:documentation',
            ]
        }
)
