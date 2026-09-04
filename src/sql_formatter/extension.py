from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class SqlFormatter(Extension):
    """SQL query formatting and dialect beautifier"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("SQL Formatter extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("SQL Formatter installed successfully.")
