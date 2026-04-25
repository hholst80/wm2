from __future__ import annotations

import enum

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)

from ..wayland import WlBuffer


class ZwlrScreencopyFrameV1(Interface):
    """A frame ready for copy."""

    name = "zwlr_screencopy_frame_v1"
    version = 3

    class error(enum.IntEnum):
        already_used = 0
        invalid_buffer = 1

    class flags_enum(enum.IntFlag):
        y_invert = 1


class ZwlrScreencopyFrameV1Proxy(Proxy[ZwlrScreencopyFrameV1]):
    interface = ZwlrScreencopyFrameV1

    @ZwlrScreencopyFrameV1.request(
        Argument(ArgumentType.Object, interface=WlBuffer),
    )
    def copy(self, buffer: WlBuffer) -> None:
        """Copy the frame to the supplied buffer."""
        self._marshal(0, buffer)

    @ZwlrScreencopyFrameV1.request()
    def destroy(self) -> None:
        """Delete this object."""
        self._marshal(1)

    @ZwlrScreencopyFrameV1.request(
        Argument(ArgumentType.Object, interface=WlBuffer),
    )
    def copy_with_damage(self, buffer: WlBuffer) -> None:
        """Same as copy, except it waits until there is damage."""
        self._marshal(2, buffer)


class ZwlrScreencopyFrameV1Resource(Resource):
    interface = ZwlrScreencopyFrameV1

    @ZwlrScreencopyFrameV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def buffer(self, format: int, width: int, height: int, stride: int) -> None:
        """wl_shm buffer information."""
        self._post_event(0, format, width, height, stride)

    @ZwlrScreencopyFrameV1.event(
        Argument(ArgumentType.Uint),
    )
    def flags(self, flags: int) -> None:
        """Frame flags."""
        self._post_event(1, flags)

    @ZwlrScreencopyFrameV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def ready(self, tv_sec_hi: int, tv_sec_lo: int, tv_nsec: int) -> None:
        """Frame is available for reading."""
        self._post_event(2, tv_sec_hi, tv_sec_lo, tv_nsec)

    @ZwlrScreencopyFrameV1.event()
    def failed(self) -> None:
        """Frame copy failed."""
        self._post_event(3)

    @ZwlrScreencopyFrameV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def damage(self, x: int, y: int, width: int, height: int) -> None:
        """Damaged region coordinates."""
        self._post_event(4, x, y, width, height)

    @ZwlrScreencopyFrameV1.event(
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
        Argument(ArgumentType.Uint),
    )
    def linux_dmabuf(self, format: int, width: int, height: int) -> None:
        """linux-dmabuf buffer information."""
        self._post_event(5, format, width, height)

    @ZwlrScreencopyFrameV1.event()
    def buffer_done(self) -> None:
        """All buffer types reported."""
        self._post_event(6)


class ZwlrScreencopyFrameV1Global(Global):
    interface = ZwlrScreencopyFrameV1


ZwlrScreencopyFrameV1._gen_c()
ZwlrScreencopyFrameV1.proxy_class = ZwlrScreencopyFrameV1Proxy
