import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = []
test_requires = []

setup(name='pmonitor',
      version='0.0',
      description='',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Emmanuel Cazenave',
      author_email='contact@emcaz.fr',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite="",
      entry_points="""\
      [console_scripts]
      pmonitor = pmonitor.main:run
      pm-dummydaemon = pmonitor.testing:run
      """,
      )
