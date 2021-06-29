from setuptools import setup

setup(
    name = 'treasure',
    version = '0.1',
    py_modules = ['treasure'],
    install_requires = [
        'Click',
        'requests',
    ],
    entry_points = '''
        [console_scripts]
        treasure = treasure:treasure
    '''
)