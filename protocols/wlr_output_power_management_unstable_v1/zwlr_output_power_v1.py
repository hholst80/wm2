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


class ZwlrOutputPowerV1(Interface):
    """Adjust power management mode for an output"""

    name = "zwlr_output_power_v1"
    version = 1

    class mode(enum.IntEnum):
        off = 0
        on = 1

    class error(enum.IntEnum):
        invalid_mode = 1


class ZwlrOutputPowerV1Proxy(Proxy[ZwlrOutputPowerV1]):
    interface = ZwlrOutputPowerV1

    @ZwlrOutputPowerV1.request(
        Argument(ArgumentType.Uint),
    )
    def set_mode(self, mode: int) -> None:
        """Set an output's power save mode"""
        self._marshal(0, mode)

    @ZwlrOutputPowerV1.request()
    def destroy(self) -> None:
        """Destroy this power management"""
        self._marshal(1)
        self._destroy()


class ZwlrOutputPowerV1Resource(Resource):
    interface = ZwlrOutputPowerV1

    @ZwlrOutputPowerV1.event(
        Argument(ArgumentType.Uint),
    )
    def mode(self, mode: int) -> None:
        """Report a power management mode change"""
        self._post_event(0, mode)

    @ZwlrOutputPowerV1.event()
    def failed(self) -> None:
        """Object no longer valid"""
        self._post_event(1)


class ZwlrOutputPowerV1Global(Global):
    interface = ZwlrOutputPowerV1


ZwlrOutputPowerV1._gen_c()
ZwlrOutputPowerV1.proxy_class = ZwlrOutputPowerV1Proxy
ZwlrOutputPowerV1.resource_class = ZwlrOutputPowerV1Resource
ZwlrOutputPowerV1.global_class = ZwlrOutputPowerV1Global
