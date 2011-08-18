from setuptools import setup, find_packages


setup(
    name='pygsm_gateway',
    version='0.0.1',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={
        '': ['*.sql', '*.pyc'],
    },
    url='https://github.com/caktus/pygsm-gateway',
    license='LICENSE.txt',
    description='Simple HTTP gateway to PyGSM',
    long_description=open('README.rst').read(),
)
