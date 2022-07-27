from setuptools import setup

setup(
    name='sensor',
    version='1.0.0',
    packages=['sensor'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'twilio'
    ],
    tests_require=[
        'pytest',
    ]
)