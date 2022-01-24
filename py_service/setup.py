from setuptools import setup

package_name = 'py_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pijuan Yu',
    maintainer_email='pijuanyu2020@gmail.com',
    description='This package is used to create a client and a service so that two intergers can be added',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = py_service.service_member_function:main',
            'client = py_service.client_member_function:main',
        ],
    },
)
