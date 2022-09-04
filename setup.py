from setuptools import setup

from credit_card_validator.version import VERSION

setup(
    name="credit-card-validator",
    version=VERSION,
    description="A simple yet effective credit card validator",
    long_description="A simple yet effective credit card validator without using any library nor regex",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Environment :: MacOS X",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    author="Bastien BO",
    author_email="bastien.bo@free.fr",
    url="https://github.com/Bastien-BO/credit-card-validator",
    license="MIT",
    packages=["credit_card_validator"],
    python_requires=">=3.7",
)
