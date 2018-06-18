import setuptools

setuptools.setup(
    name="parfive",
    version="0.1.0",
    url="https://github.com/cadair/parfive",

    author="Stuart Mumford",

    description="A parallel file downloader using asyncio.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['aiohttp', 'tqdm'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
