from __future__ import annotations

from pywayland.protocol_core import (
    Argument,
    ArgumentType,
    Global,
    Interface,
    Proxy,
    Resource,
)


class RiverLayerShellOutputV1(Interface):
    """Layer shell output state

    The lifetime of this object is tied to the corresponding river_output_v1.
    """

    name = "river_layer_shell_output_v1"
    version = 1


class RiverLayerShellOutputV1Proxy(Proxy[RiverLayerShellOutputV1]):
    interface = RiverLayerShellOutputV1

    @RiverLayerShellOutputV1.request()
    def destroy(self) -> None:
        self._marshal(0)
        self._destroy()

    @RiverLayerShellOutputV1.request()
    def set_default(self) -> None:
        """Mark this output as the default for new layer surfaces."""
        self._marshal(1)


class RiverLayerShellOutputV1Resource(Resource):
    interface = RiverLayerShellOutputV1

    @RiverLayerShellOutputV1.event(
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
        Argument(ArgumentType.Int),
    )
    def non_exclusive_area(self, x: int, y: int, width: int, height: int) -> None:
        """Area left after subtracting exclusive zones."""
        self._post_event(0, x, y, width, height)


class RiverLayerShellOutputV1Global(Global):
    interface = RiverLayerShellOutputV1


RiverLayerShellOutputV1._gen_c()
RiverLayerShellOutputV1.proxy_class = RiverLayerShellOutputV1Proxy
RiverLayerShellOutputV1.resource_class = RiverLayerShellOutputV1Resource
RiverLayerShellOutputV1.global_class = RiverLayerShellOutputV1Global
