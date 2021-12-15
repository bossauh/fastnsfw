from distutils.core import setup
setup(
    name="fastnsfw",
    packages=["fastnsfw"],
    version="0.1",
    license="MIT",
    description="NSFW Detection Library",
    author="Philippe Mathew",
    author_email="philmattdev@gmail.com",
    url="PUT",
    download_url="PUT",
    keywords=["nsfw", "detection"],
    install_requires=[
        "nsfw-model @ git+https://github.com/GantMan/nsfw_model.git",
        "fluxhelper",
        "pillow",
        "imagehash",
        "opencv-python"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
