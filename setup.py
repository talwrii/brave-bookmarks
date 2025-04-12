import setuptools
import distutils.core

setuptools.setup(
    name='brave-bookmarks',
    version="1.2.1",
    author='@readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='',
    license='MIT',
    keywords='bookmarks, brave, command-line',
    url='https://github.com/talwrii/brave-bookmarks',
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
