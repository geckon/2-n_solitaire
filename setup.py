#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

from setuptools import setup

setup(
    name='twn-solitaire',
    version='0.1.0',
    author='Tomáš Heger',
    packages=['twnsol',],
    scripts=['solitaire.py',],
    url='https://github.com/geckon/2-n_solitaire',
    license='LICENSE',
    description='Generic version of 2048 Solitaire. Simple, fun and satisfying game.',
    long_description=open('README.md').read(),
    install_requires=[
        "pygame == 1.9.4",
        "toml == 0.10.0",
    ],
)