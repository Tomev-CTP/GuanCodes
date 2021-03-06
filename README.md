# Guan Codes

A simple package for generating Gray and Guan codes.

## Summary

  - [Getting Started](#getting-started)
  - [Running the tests](#running-the-tests)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

So far, to get the project one only needs to download it from the
[repository](https://github.com/Tomev-CTP/GuanCodes) (or any other source).

It's also possible to download it as a package with

`pip install guancodes`

which will download the package from [pypi](https://pypi.org/project/BoSS/).

### Prerequisites

To run the scripts there will be needed some version of Python. During the development
I'm using 3.8, but I believe that it will also work just fine with some earlier or newer
version (at least for now).

In some places I use `typing` package, that's why 3.8 version is desirable.

### Code style

Throughout this work PEP-8 will be used. There are several cases where this may go south.

* In some versions of the code matrices may be denoted by capital letters (as in
standard mathematical notation). In order to be more PEP-friendly I'll try to use prefix
m_ instead of capital letters, e.g. m_u would be the equivalent of U. Alternatively
explicit use of mathematical notation is also acceptable. 

## Running the tests

Just run all test in `tests` folder with `pytest`.

* Note that (for now) there are no unit tests. Just simple sanity check of returned
results.

## Versioning

I'll use [SemVer](http://semver.org/) for versioning and try to keep track of the version in the tags. 

## Authors

  - [Tomasz Rybotycki](https://github.com/Tomev)
  - [Billie Thompson](https://github.com/PurpleBooth) - *Provided README Template* 

## License

This project is licensed under the [Apache License, v.2.0](LICENSE.md).
See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

  - [CTP PAS](http://www.cft.edu.pl/new/public/pl) - This project was done
during my Ph.D. at CTP PAS.