from setuptools import setup, find_packages

with open('README.txt', encoding='UTF-8') as f:
    readme = f.read
   
setup(
    name='pgbackup',
    version='0.1.0'
    description='Database backups to MS Azure'
    long_description=readme,
    author='Mehmet',
    author_email='mehmet@acloudguru.com'
    install_requries=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)