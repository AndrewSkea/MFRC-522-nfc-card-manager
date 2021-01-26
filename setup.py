import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfrc522-card-manager",
    version="0.0.1",
    author="Andrew Skea",
    author_email="andrewskea.as@gmail.com",
    description="Card Manager package for MFRC-522 Rfid cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/AndrewSkea/mfrc-522-card-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)