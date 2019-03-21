from setuptools import find_packages, setup
import ast
import re

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("graphql_django/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

tests_require = [
    "pytest>=3.6.3",
    "pytest-cov",
    "coveralls",
    "mock",
    "pytest-django>=3.3.2",
]
packages = find_packages()

setup(name='graphql_django',
      version=version,
      description='graphql graphene django dynamic implementation',
      url='http://github.com/graphql_django/graphql_django',
      author='Rigoberto Contreras',
      author_email='rigoberto.contreras@gmail.com',
      license='MIT',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: PyPy",
      ],
      install_requires=[
          "graphene>=2.1.0,<3",
          "graphene-django>=2.2.0,<3.0",
      ],
      setup_requires=["pytest-runner"],
      tests_require=tests_require,
      extras_require={"test": tests_require},
      include_package_data=True,
      packages=packages,
      zip_safe=False,
      platforms="any",
      )
