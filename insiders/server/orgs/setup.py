from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="purplship.server.orgs",
    version="2021.11.5",
    description="Multi-carrier shipping API organization module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Purplship/purplship-server",
    author="purplship",
    author_email="hello@purplship.com",
    license="Purplship Enterprise",
    packages=find_namespace_packages(exclude=["tests.*", "tests"]),
    install_requires=[
        "django-extensions",
        "django-organizations",
        "purplship.server.core",
        "purplship.server.graph",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
    include_package_data=True,
)