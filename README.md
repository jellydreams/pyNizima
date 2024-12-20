# PyNizima

A python library for interacting with [NizimaLIVE API](https://github.com/Live2D/nizimaLIVEPluginAPI/tree/develop)

## Quick Start
### Install

```shell
pip install pynizima
```

### Get Started

#### Exemple
📖 Read [tutorial](doc/tutorial.md) for more details
```python
from pynizima import NizimaRequest
import asyncio

async def main():
    nz = NizimaRequest()
    plugin_name = 'YourPluginName'
    token = await nz.register_plugin(plugin_name)
    connection_enabled = await nz.establish_connection(plugin_name, token)
    while connection_enabled:
        # do your plugin logic here

if __name__ == "__main__":
    asyncio.run(main())
```

_______

## List of Methods

📖 Read [methods documentation](doc/NizimaRequest.md) for more details. 

#### **Plugin Management**
- [register_plugin](doc/NizimaRequest.md#register_plugin)
- [establish_connection](doc/NizimaRequest.md#establish_connection)
- [register_plugin_path](doc/NizimaRequest.md#register_plugin_path)
- [get_connection_status](doc/NizimaRequest.md#get_connection_status)

#### **Parameter Control**
- [insert_live_parameters](doc/NizimaRequest.md#insert_live_parameters)
- [set_live_parameter_values](doc/NizimaRequest.md#set_live_parameter_values)
- [set_cubism_parameter_values](doc/NizimaRequest.md#set_cubism_parameter_values)
- [reset_cubism_parameter_values](doc/NizimaRequest.md#reset_cubism_parameter_values)
- [get_live_parameters](doc/NizimaRequest.md#get_live_parameters)
- [get_live_parameter_values](doc/NizimaRequest.md#get_live_parameter_values)
- [get_cubism_parameter_values](doc/NizimaRequest.md#get_cubism_parameter_values)
- [get_cubism_parameters](doc/NizimaRequest.md#get_cubism_parameters)

#### **Scene Management**
- [add_model](doc/NizimaRequest.md#add_model)
- [remove_model](doc/NizimaRequest.md#remove_model)
- [move_model](doc/NizimaRequest.md#move_model)
- [reset_pose](doc/NizimaRequest.md#reset_pose)
- [get_scenes](doc/NizimaRequest.md#get_scenes)
- [get_current_scene_id](doc/NizimaRequest.md#get_current_scene_id)

#### **Model Manipulation**
- [register_model](doc/NizimaRequest.md#register_model)

- [change_model](doc/NizimaRequest.md#change_model)
- [get_registered_model_icons](doc/NizimaRequest.md#get_registered_model_icons)
- [get_registered_models](doc/NizimaRequest.md#get_registered_models)
- [get_current_model_id](doc/NizimaRequest.md#get_current_model_id)
- [get_models](doc/NizimaRequest.md#get_models)

#### **Model Parts Manipulation**
- [set_drawables_color](doc/NizimaRequest.md#set_drawables_color)
- [set_parts_color](doc/NizimaRequest.md#set_parts_color)
- [set_model_color](doc/NizimaRequest.md#set_model_color)
- [get_drawables](doc/NizimaRequest.md#get_drawables)
- [get_parts](doc/NizimaRequest.md#get_parts)
- [get_parts_tree](doc/NizimaRequest.md#get_parts_tree)

#### **Item Management**
- [add_item](doc/NizimaRequest.md#add_item)
- [remove_item](doc/NizimaRequest.md#remove_item)
- [move_item](doc/NizimaRequest.md#move_item)
- [get_registered_items](doc/NizimaRequest.md#get_registered_items)
- [get_items](doc/NizimaRequest.md#get_items)

#### **Motion Control**
- [start_motion](doc/NizimaRequest.md#start_motion)
- [stop_motion](doc/NizimaRequest.md#stop_motion)
- [get_motions](doc/NizimaRequest.md#get_motions)

#### **Expression Management**
- [start_expression](doc/NizimaRequest.md#start_expression)
- [stop_expression](doc/NizimaRequest.md#stop_expression)
- [stop_all_expressions](doc/NizimaRequest.md#stop_all_expressions)
- [get_expressions](doc/NizimaRequest.md#get_expressions)
