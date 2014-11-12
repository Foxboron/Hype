#! /usr/bin/env python
## adderall - miniKanren in Hy
## Copyright (C) 2014  Gergely Nagy <algernon@madhouse-project.org>
##
## This library is free software: you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation, either version 3 of
## the License, or (at your option) any later version.
##
## This library is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public
## License along with this program. If not, see <http://www.gnu.org/licenses/>.

from setuptools import find_packages, setup

setup(
    name="hype",
    version="0.1.0",
    install_requires = ['hy>=0.10','typeannotations>=1.0.0'],
    dependency_links = [
        'http://github.com/ceronman/typeannotations/tarball/master#egg=typeannotations-1.0.0',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={
        'hype': ['*.hy'],
    },
    author="Morten Linderud",
    author_email="Morten@Linderud.pw",
    long_description="Function Annotations library for Hylang.",
    license="",
    url="https://github.com/Foxboron/hype",
    platforms=['any'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Lisp",
        "Topic :: Software Development :: Libraries",
    ]
)
