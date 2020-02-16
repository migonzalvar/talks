import setuptools

setuptools.setup(
    name="chove",
    version="0.0.1",
    author="Miguel González",
    author_email="migonzalvar@gmail.com",
    description="Check if it's rainning.",
    long_description="It uses Meteogalicia",
    py_modules=["chove"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
