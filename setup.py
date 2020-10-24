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

from pkg.discover import discover
from pkg.install import add

requirements = ["keyring", "pyxdg", "wheel", "flake8", "flake8-docstring",
                "ghdiff", "gnupg", "ipython", "pep8-naming", "pss",
                "pytest", "pytest_cov", "pytest_pep8", "sh"]
add(*requirements)

setup(requires=requirements + ["pip"],
      provides={"distutils.setup_keywords": ["discover = pkg:auto_discover"],
                "setuptools.file_finders": ["git = pkg:get_repo_files"],
                "kt.extensions": ["sloc = src:count_sloc"],
                "term.apps": ["pkg = pkg.__main__:main",
                              "src = src.__main__:main"]},
      **discover(__file__))
