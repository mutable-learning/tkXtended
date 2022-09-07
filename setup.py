import setuptools

with open("README.md", "r") as readme:
    description = readme.read()

setuptools.setup(
    name="tkXtended",
    version="0.0.1",
    author="Mutable-Learning",
    author_email="mutablelearning@duck.com",
    packages=["tkXtended"],
    description="Tkinter widget library",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/mutable-learning/tkXtended",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        'pillow',
    ]
)
