import setuptools

full_desc = ""

with open("README.md", 'r', encoding='utf-8') as fh:
    full_desc = fh.read()

setuptools.setup(
    name="Hemorrhagic_Volume_Assessment-HSUIRAD",
    version="1.0.0",
    author="Dariush Aligholizadeh",
    author_email="daligho1@umbc.edu",
    description="A very basic computer vision model to determine volume of intracranial stroke from MRI images (basic because relies almost entirely on user input, goal is to make it fully automatic feature detection regardless of color)",
    long_description=full_desc,
    long_description_content_type = 'text/markdown',
    url='https://github/com/Hsuirad/Hemorrhagic-Volume-Assessment',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires = ['sklearn', 'numpy', 'statsmodels', 'pillow', 'matplotlib', 'opencv-python', 'scipy'],
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
