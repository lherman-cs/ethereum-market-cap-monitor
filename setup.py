from distutils.core import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().strip().split('\n')

setup(
    name='ethereum-market-cap-monitor',
    version='1.0',
    packages=['ethereum_market_cap_monitor'],
    install_requires=requirements
)