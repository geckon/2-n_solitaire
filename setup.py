#  ___  _ __     _____       _ _ _        _
# |__ \| '_ \   / ____|     | (_) |      (_)
#    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___
#   / /         \___ \ / _ \| | | __/ _` | | '__/ _ \
#  / /_         ____) | (_) | | | || (_| | | | |  __/
# |____|       |_____/ \___/|_|_|\__\__,_|_|_|  \___|
#

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='twn-solitaire',
    version='0.1.0',
    packages=['twnsol', ],
    package_dir={'twnsol': 'twnsol'},
    package_data={'': ['LICENSE', 'assets/Jellee-Roman/*.txt'],
                  'twnsol': ['assets/Jellee-Roman/Jellee-Roman.otf']},
    scripts=['solitaire.py', ],
    url='https://github.com/geckon/2-n_solitaire',
    license='GNU GPL v3',
    description='Generic version of 2048 Solitaire. Simple, fun and '
                'satisfying game.',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[
        "pygame == 1.9.4",
        "toml == 0.10.0",
    ],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
