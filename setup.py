# [`src`][1] Copyright @[Angelo Gladding][2] 2020-
#
# This program is free software: it is distributed in the hope that it
# will be useful, but *without any warranty*; without even the implied
# warranty of merchantability or fitness for a particular purpose. You
# can redistribute it and/or modify it under the terms of the @@[GNU's
# Not Unix][3] %[Affero General Public License][4] as published by the
# @@[Free Software Foundation][5], either version 3 of the License, or
# any later version.
#
# *[GNU]: GNU's Not Unix
#
# [1]: https://github.com/angelogladding/src
# [2]: https://angelogladding.com
# [3]: https://gnu.org
# [4]: https://gnu.org/licenses/agpl
# [5]: https://fsf.org

"""Tools for metamodern software development."""

from setuptools import setup

setup(requires=["flake8", "flake8-docstring", "ghdiff", "gnupg", "ipython",
                "pep8-naming", "pss", "pytest", "pytest_cov", "pytest_pep8",
                "sh"],
      provides={"kt.extensions": ["sloc = src:count_sloc"],
                "term.apps": ["src = src.__main__:main"]},
      discover=__file__)
