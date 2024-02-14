from setuptools import setup, find_packages

# Read the contents of your README file
from os import path
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="autogonai-python",
    version="0.1.0",
    description="Python connector for Autogon Public APIs",
    author="Autogon AI Inc.",
    author_email="infrastructure@autogon.ai",
    maintainer="David Mbatuegwu, Aaron Nwokoro",
    maintainer_email="infrastructure@autogon.ai",
    url="https://github.com/autogoninc/autogonai-python",
    packages=find_packages(),
    install_requires=["python-dotenv==1.0.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
