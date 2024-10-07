from setuptools import setup, find_packages
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="TranscriptAnalyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    description="A package for comparing YouTube transcripts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Distant Answer",
    author_email="distantanswer@gmail.com",
    url="https://github.com/cgallarno/TranscriptAnalyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

