import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mikes_toolbox',                           # should match the package folder
    packages=['mikes_toolbox'],                     # should match the package folder
    version='0.0.3',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='crypto hash',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Mike Huls',
    author_email='mikehuls42@gmail.com',
    url='https://github.com/akioguru/cryptohash', 
    project_urls = {                                # Optional
        "Bug Tracker": "https://github.com/akioguru/cryptohash/issues"
    },
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["python", "crypto", "hash", "mnemonic", "seed phrase", "ethereum", "wallet", "private key", "public key"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/akioguru/cryptohash/archive/refs/tags/0.0.3.tar.gz",
)