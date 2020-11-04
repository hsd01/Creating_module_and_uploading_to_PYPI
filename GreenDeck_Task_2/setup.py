import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plot_chart_HSD", # Replace with your own username
    version="0.4.0",
    author="HSD",
    author_email="ashuhemantsingh@gmail.com",
    description="A basic operations with arithmetic operators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
