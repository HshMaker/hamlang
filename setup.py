from setuptools import setup, find_packages

setup(
    name='hamlang',
    version='0.7.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hamlang=hamlang.__main__:main'
        ]
    },
    author='HshMaker',
    author_email='hshmakerss@gmail.com',
    description="그냥 히읗이 많이 들어간 언어입니다.",
)