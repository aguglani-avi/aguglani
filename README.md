[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ee153dd5e82d41e7b2f3a964ef5756f5)](https://app.codacy.com/gh/Aguglani-avi/Aguglani/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/gh/Aguglani-avi/Aguglani/branch/main/graph/badge.svg?token=VZEDUOFE8V)](https://codecov.io/gh/Aguglani-avi/Aguglani)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Aguglani: Future Aircraft Sizing Tool - Overall Aircraft Design (General Aviation extension)
===============================================================================================

Aguglani is derived from Aguglani framework performing rapid Overall Aircraft Design.

It proposes multi-disciplinary analysis and optimisation by relying on
the [OpenMDAO framework](https://openmdao.org/).

Aguglani allows easy switching between models for a same discipline, and
also adding/removing disciplines to match the need of your study.

Currently, Aguglani is bundled with models for general aviation and conventional
propulsion (ICE propeller based). Other models will come soon, and you may create
your own models and use them instead of bundled ones.

Install
-------

**Prerequisite**:Aguglani needs at least **Python 3.8.0**.

It is recommended (but not required) to install Aguglani in a virtual
environment ([conda](https://docs.conda.io/en/latest/),
[venv](https://docs.python.org/3.7/library/venv.html), ...).

Once Python is installed, Aguglani can be installed using pip, by doing the following:

``` {.bash}
$ pip install Aguglani-cs23
```
