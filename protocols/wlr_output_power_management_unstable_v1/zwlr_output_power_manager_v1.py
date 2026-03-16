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
from .zwlr_output_power_v1 import ZwlrOutputPowerV1


class ZwlrOutputPowerManagerV1(Interface):
    """Manager to create per-output power management"""

    name = "zwlr_output_power_manager_v1"
    version = 1


class ZwlrOutputPowerManagerV1Proxy(Proxy[ZwlrOutputPowerManagerV1]):
    interface = ZwlrOutputPowerManagerV1

    @ZwlrOutputPowerManagerV1.request(
        Argument(ArgumentType.NewId, interface=ZwlrOutputPowerV1),
        Argument(ArgumentType.Object, interface=WlOutput),
    )
    def get_output_power(self, output: WlOutput) -> Proxy[ZwlrOutputPowerV1]:
        """Get a power management mode control for an output"""
        id = self._marshal_constructor(0, ZwlrOutputPowerV1, output)
        return id

    @ZwlrOutputPowerManagerV1.request()
    def destroy(self) -> None:
        """Destroy the manager"""
        self._marshal(1)
        self._destroy()


class ZwlrOutputPowerManagerV1Resource(Resource):
    interface = ZwlrOutputPowerManagerV1


class ZwlrOutputPowerManagerV1Global(Global):
    interface = ZwlrOutputPowerManagerV1


ZwlrOutputPowerManagerV1._gen_c()
ZwlrOutputPowerManagerV1.proxy_class = ZwlrOutputPowerManagerV1Proxy
ZwlrOutputPowerManagerV1.resource_class = ZwlrOutputPowerManagerV1Resource
ZwlrOutputPowerManagerV1.global_class = ZwlrOutputPowerManagerV1Global
