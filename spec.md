# River Window Manager Specification

## Key Points
- Build a window manager for River compositor (v0.4+) using river-window-management-v1 Wayland protocol
- Python 3 preferred
- Standalone Wayland client process communicating via river_window_manager_v1 protocol
- Two-phase commit model (manage → render)

## Protocol Objects
- river_window_manager_v1: Main interface; receives window/output/seat creation events
- river_window_v1: Represents a toplevel window; WM sets size, position, fullscreen state
- river_output_v1: Represents a monitor; provides usable dimensions
- river_seat_v1: Represents an input seat; WM binds keys, manages focus, pointer operations
- river_node_v1: Controls z-order / render stacking

## Features
- 4 desktops + floating overlay stack
- 3 layout modes per desktop: fullscreen, max, 2-split
- Keybindings via river_seat_v1
- Single monitor (multi-monitor is stretch goal)
- Optional TOML/YAML config file

## Need to get the protocol XML spec from River source tree
