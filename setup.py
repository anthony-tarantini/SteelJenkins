from setuptools import setup, find_packages

setup(
    name="SteelJenkins",
    version='1.0.0',
    url='https://github.com/anthony-tarantini/SteelJenkins.git',
    license='MIT',
    description='Tie Your SteelSeries Mouse To Jenkins',
    author='Anthony Tarantini',
    author_email='anthony.tarantini@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools', 'requests'],
    entry_points={
        'console_scripts': [
            'src=src:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
    ]
)
