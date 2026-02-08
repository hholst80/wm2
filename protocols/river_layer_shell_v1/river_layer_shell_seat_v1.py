from __future__ import annotations

from pywayland.protocol_core import (
    Global,
    Interface,
    Proxy,
    Resource,
)


class RiverLayerShellSeatV1(Interface):
    """Layer shell seat state

    The lifetime of this object is tied to the corresponding river_seat_v1.
    """

    name = "river_layer_shell_seat_v1"
    version = 1


class RiverLayerShellSeatV1Proxy(Proxy[RiverLayerShellSeatV1]):
    interface = RiverLayerShellSeatV1

    @RiverLayerShellSeatV1.request()
    def destroy(self) -> None:
        self._marshal(0)
        self._destroy()


class RiverLayerShellSeatV1Resource(Resource):
    interface = RiverLayerShellSeatV1

    @RiverLayerShellSeatV1.event()
    def focus_exclusive(self) -> None:
        """A layer surface will be given exclusive keyboard focus."""
        self._post_event(0)

    @RiverLayerShellSeatV1.event()
    def focus_non_exclusive(self) -> None:
        """A layer surface will be given non-exclusive keyboard focus."""
        self._post_event(1)

    @RiverLayerShellSeatV1.event()
    def focus_none(self) -> None:
        """No layer shell surface will have keyboard focus."""
        self._post_event(2)


class RiverLayerShellSeatV1Global(Global):
    interface = RiverLayerShellSeatV1


RiverLayerShellSeatV1._gen_c()
RiverLayerShellSeatV1.proxy_class = RiverLayerShellSeatV1Proxy
RiverLayerShellSeatV1.resource_class = RiverLayerShellSeatV1Resource
RiverLayerShellSeatV1.global_class = RiverLayerShellSeatV1Global
