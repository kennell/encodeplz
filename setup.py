from setuptools import setup, find_packages


setup(
    name = "encodeplz",
    version = "1.0.0",
    packages = find_packages(),
    author = "Kevin Kennell",
    author_email = "kevin@kennell.de",
    license = "MIT",
    url = "http://github.com/kennell/encodeplz",
    install_requires=[
        'flask',
        'celery',
        'click',
        'redis',
        'gunicorn'
    ],
    entry_points={
        'console_scripts': [
            'encodeplz = encodeplz.cli:main'
        ]
    }
)