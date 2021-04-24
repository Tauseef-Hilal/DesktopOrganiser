import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []
with open("Requirements.txt", "r", encoding="utf-8") as fh:
    for line in fh.readlines():
        requirements.append(line[:-1])

setuptools.setup(
    name="desktop-organiser-tht",
    version="0.0.1",
    author="Tauseef Hilal Tantary",
    author_email="tantary.tauseef@gmail.com",
    description="Desktop Organiser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tauseef-Hilal/DesktopOrganiser",
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/Tauseef-Hilal/DesktopOrganiser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["organiser"],
    include_package_data=True,
    install_requires=requirements,
    entry_points={"console_scripts": ["desktop=organiser.__main__:main"]},
)
