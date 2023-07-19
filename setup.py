import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pcm2adpcm",
    version="0.1.3",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="16bit raw PCM to ADPCM converter for xmkmcs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/pcm2adpcm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pcm2adpcm=pcm2adpcm.pcm2adpcm:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    setup_requires=["setuptools"],
    install_requires=[],
)
