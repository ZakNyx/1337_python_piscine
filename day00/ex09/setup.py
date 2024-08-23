from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='zihirri',
    author_email='zihirri@student.1337.ma',
    url="https://github.com/ZakNyx/1337_python_piscine/tree/main/day00/ex09",
    description='A sample test package',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [],
    },
)