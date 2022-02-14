from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fcm_interface',
    packages=find_packages(include=['fcm_interface']),
    version='0.1.0',
    description='FCM Interface',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchAngel776/fcm_interface",
    license='MIT'
)