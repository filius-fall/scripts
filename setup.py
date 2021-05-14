from setuptools import setup,find_packages

setup(
    name = 'pomodora',
    versrion = '0.1',
    py_modules = find_packages(),
    inculde_package_data = True,
    install_requires = [
        'Click',
    ],
    entry_points = {
        'console_scripts':[
            'pomodora = pomodora.pomodora:timer'
        ]
    }
    
)