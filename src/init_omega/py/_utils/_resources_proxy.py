from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `init_omega.py.resources` module.

    This is used so that we can lazily import `init_omega.py.resources` only when
    needed *and* so that users can just import `init_omega.py` and reference `init_omega.py.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("init_omega.py.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
