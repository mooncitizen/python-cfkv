from setuptools import setup find_packages

VERSION = '1.0.0'
AUTHOR = "Paul Gardiner"
AUTHOR_EMAIL = "franticstone@gmail.com"
APP_NAME = "cfkv"
DESCRIPTION = "A Python wrapper for the Cloudflare KV Cache API"
LONG_DESCRIPTION = "A Python wrapper for the Cloudflare KV Cache API that provides a simple interface to the Cloudflare KV Cache."

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR
    author_email=AUTHOR_EMAIL,
    license='MIT',
    packages=find_packages(),
    install_requires=[]
    keywords=['cloudflare', 'kv', 'cache', 'api', 'cloudflare workers'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)