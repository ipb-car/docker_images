from setuptools import find_packages, setup
package_name = "rpi_time"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/" + package_name, ["package.xml"]),
    ],

    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Louis Wiesmann",
    maintainer_email="louis.wiesmann@igg.uni-bonn.de",
    description="Publisher for local time",
    license="MIT",
    entry_points={
        "console_scripts": ["rpi_time = rpi_time.rpi_time:main"],
    },
)
