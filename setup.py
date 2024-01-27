from setuptools import setup, find_packages

package_name = "lapa_database_structure"

setup(
    name=package_name,
    version="0.0.4",
    packages=find_packages(),
    package_data={
        package_name: [],
    },
    install_requires=[
        "sqlalchemy>=2.0.23",
    ],
    author="Amish Palkar, thePmSquare",
    author_email="amishpalkar302001@gmail.com, thepmsquare@gmail.com",
    description="database layer for my personal server.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/B21amish/{package_name}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
