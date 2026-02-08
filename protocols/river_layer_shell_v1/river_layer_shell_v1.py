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

from ..river_window_management_v1 import RiverOutputV1, RiverSeatV1
from .river_layer_shell_output_v1 import RiverLayerShellOutputV1
from .river_layer_shell_seat_v1 import RiverLayerShellSeatV1


class RiverLayerShellV1(Interface):
    """River layer shell global interface

    Binding this interface indicates that the window manager supports layer
    shell. If the window manager does not bind this interface, the compositor
    will close layer surfaces immediately.
    """

    name = "river_layer_shell_v1"
    version = 1

    class error(enum.IntEnum):
        object_already_created = 0


class RiverLayerShellV1Proxy(Proxy[RiverLayerShellV1]):
    interface = RiverLayerShellV1

    @RiverLayerShellV1.request()
    def destroy(self) -> None:
        self._marshal(0)
        self._destroy()

    @RiverLayerShellV1.request(
        Argument(ArgumentType.NewId, interface=RiverLayerShellOutputV1),
        Argument(ArgumentType.Object, interface=RiverOutputV1),
    )
    def get_output(self, output: RiverOutputV1) -> Proxy[RiverLayerShellOutputV1]:
        """Get layer shell output state."""
        id = self._marshal_constructor(1, RiverLayerShellOutputV1, output)
        return id

    @RiverLayerShellV1.request(
        Argument(ArgumentType.NewId, interface=RiverLayerShellSeatV1),
        Argument(ArgumentType.Object, interface=RiverSeatV1),
    )
    def get_seat(self, seat: RiverSeatV1) -> Proxy[RiverLayerShellSeatV1]:
        """Get layer shell seat state."""
        id = self._marshal_constructor(2, RiverLayerShellSeatV1, seat)
        return id


class RiverLayerShellV1Resource(Resource):
    interface = RiverLayerShellV1


class RiverLayerShellV1Global(Global):
    interface = RiverLayerShellV1


RiverLayerShellV1._gen_c()
RiverLayerShellV1.proxy_class = RiverLayerShellV1Proxy
RiverLayerShellV1.resource_class = RiverLayerShellV1Resource
RiverLayerShellV1.global_class = RiverLayerShellV1Global
