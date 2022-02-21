import setuptools
import os


with open("README.md", "r") as fh:
    long_description = fh.read()


PATH = os.path.dirname(__file__)


def get_version():
    with open(os.path.join(PATH, "sagemaker_studio_autoshutdown", "VERSION")) as version_file:
        version = version_file.read().strip()
    return version


setuptools.setup(
    name="sagemaker_studio_autoshutdown",
    version=get_version(),
    author="Roman Kosobrodov",
    author_email="roman@kosobrodov.net",
    description="Jupyter Server Auto stop script",
    license="MIT",
    long_description=long_description,
    url="https://github.com/RomanKosobrodov/stoy",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    data_files=[
        (
            "etc/jupyter/jupyter_server_config.d",
            ["jupyter-config/jupyter_server_config.d/sagemaker_studio_autoshutdown.json"]
        ),
    ],
    package_data={
        'sagemaker_studio_autoshutdown': ["VERSION"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=["boto3>=1.10.44"]
)
