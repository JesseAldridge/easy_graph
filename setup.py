from setuptools import setup, find_packages
import sys, os

version = '0.2.0'

setup(name='easygraph',
      version=version,
      description="Easily turn your python data into a flot graph in a static html file.",
      long_description="""""",
      classifiers=[],
      keywords='graph graphing plot',
      author='Jesse Aldridge',
      author_email='JesseAldridge@gmail.com',
      url='https://github.com/JesseAldridge/easy_graph',
      license='MIT',
      packages=['easygraph'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ]
      )
