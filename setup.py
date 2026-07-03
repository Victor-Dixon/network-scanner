from setuptools import setup, find_packages

setup(
    name="network_scanner",
    version="1.0.0",
    author="Unknown",
    author_email="",
    description=(
        "Defensive Python network-security toolkit for authorized environments: "
        "ARP IPv4 discovery, port/banner helpers, vulnerability checks, "
        "AbuseIPDB lookup, and anomaly-detection experiments."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Victor-Dixon/network-scanner",
    packages=find_packages(),
    install_requires=[
        "requests",
        "packaging",
        "pandas",
        "numpy",
        "scapy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "network-scanner=network_scanner.__main__:main",  # Known stale metadata; see docs.
        ],
    },
)
