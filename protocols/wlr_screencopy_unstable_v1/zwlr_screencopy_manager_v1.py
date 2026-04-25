from __future__ import annotations

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)

from ..wayland import WlOutput
from .zwlr_screencopy_frame_v1 import ZwlrScreencopyFrameV1


class ZwlrScreencopyManagerV1(Interface):
    """Manager to inform clients and begin capturing."""

    name = "zwlr_screencopy_manager_v1"
    version = 3


class ZwlrScreencopyManagerV1Proxy(Proxy[ZwlrScreencopyManagerV1]):
    interface = ZwlrScreencopyManagerV1

    @ZwlrScreencopyManagerV1.request(
        Argument(ArgumentType.NewId, interface=ZwlrScreencopyFrameV1),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def capture_output(self, overlay_cursor: int, output: WlOutput) -> Proxy[ZwlrScreencopyFrameV1]:
        """Capture the next frame of an entire output."""
        return self._marshal_constructor(0, ZwlrScreencopyFrameV1, overlay_cursor, output)

    @ZwlrScreencopyManagerV1.request()
    def destroy(self) -> None:
        """Destroy the manager."""
        self._marshal(1)


class ZwlrScreencopyManagerV1Global(Global):
    interface = ZwlrScreencopyManagerV1


ZwlrScreencopyManagerV1._gen_c()
ZwlrScreencopyManagerV1.proxy_class = ZwlrScreencopyManagerV1Proxy
