## Documentation NizimaRequest

These methods allow plugins to interact with the nizima LIVE software.
It enables plugin developers to create advanced integrations and precisely control models, scenes, elements, parameters, motions, and expressions.

See official for detail on requests: [documentation methods NizimaLive API](https://github.com/Live2D/nizimaLIVEPluginAPI/blob/develop/methods.md)

#### **Plugin Management**
- [register_plugin](#register_plugin)
- [establish_connection](#establish_connection)
- [register_plugin_path](#register_plugin_path)
- [get_connection_status](#get_connection_status)

#### **Parameter Control**
- [insert_live_parameters](#insert_live_parameters)
- [set_live_parameter_values](#set_live_parameter_values)
- [set_cubism_parameter_values](#set_cubism_parameter_values)
- [reset_cubism_parameter_values](#reset_cubism_parameter_values)
- [get_live_parameters](#get_live_parameters)
- [get_live_parameter_values](#get_live_parameter_values)
- [get_cubism_parameter_values](#get_cubism_parameter_values)
- [get_cubism_parameters](#get_cubism_parameters)

#### **Scene Management**
- [add_model](#add_model)
- [remove_model](#remove_model)
- [move_model](#move_model)
- [reset_pose](#reset_pose)
- [get_scenes](#get_scenes)
- [get_current_scene_id](#get_current_scene_id)

#### **Model Manipulation**
- [register_model](#register_model)

- [change_model](#change_model)
- [get_registered_model_icons](#get_registered_model_icons)
- [get_registered_models](#get_registered_models)
- [get_current_model_id](#get_current_model_id)
- [get_models](#get_models)

#### **Model Parts Manipulation**
- [set_drawables_color](#set_drawables_color)
- [set_parts_color](#set_parts_color)
- [set_model_color](#set_model_color)
- [get_drawables](#get_drawables)
- [get_parts](#get_parts)
- [get_parts_tree](#get_parts_tree)

#### **Item Management**
- [add_item](#add_item)
- [remove_item](#remove_item)
- [move_item](#move_item)
- [get_registered_items](#get_registered_items)
- [get_items](#get_items)

#### **Motion Control**
- [start_motion](#start_motion)
- [stop_motion](#stop_motion)
- [get_motions](#get_motions)

#### **Expression Management**
- [start_expression](#start_expression)
- [stop_expression](#stop_expression)
- [stop_all_expressions](#stop_all_expressions)
- [get_expressions](#get_expressions)



### \_\_init\_\_
_______
Create instance to send request to NizimaLIVE API

#### Parameters
 - **port** _(int, optional)_ -- name of the plugin, default `22022`
 - **ip** _(str, optional)_ -- developer of the plugin, default `localhost`
 - **debug** _(bool, optional)_ -- display print request and response when enabled, default `False`

#### Example

```python
from pynizima import NizimaRequest
nz = NizimaRequest()
```
You can specify detail of connection with:
```python
nz = NizimaRequest(port='22024', ip='0.0.0.0')
```

## **Plugin Management**

### register_plugin
_______
Registers a new plugin in nizima LIVE.

#### Parameters
 - **name** _(str)_ -- name of the plugin
 - **developer** _(str, optional)_ -- developer of the plugin
 - **version** _(str, optional)_ -- version of the plugin
 - **icon** _(str, optional)_ -- path icon plugin

#### Return
- **string** -- connection token

#### Example
```python
token = await nz.register_plugin(
    plugin_name='YourPluginName', 
    developer='YourDevName',
    version='0.0.0', # optional
    icon='path/to/icon' # optional
)
```

### establish_connection
_______
Establishes a reconnection to nizima LIVE using the plugin name and access token.

#### Parameters
 - **name** _(str)_ -- name of the plugin
 - **token** _(str)_ -- connection token
 - **version** _(str, optional)_ -- plugin version

#### Return
- boolean -- True if connection is enabled

```python
plugin_name = 'YourPluginName'
token = 'YourRegisterPluginToken'
connection_enabled = await self.nz.establish_connection(plugin_name, token)
```

### register_plugin_path
_______
Sets the executable file path for the plugin, allowing nizima LIVE to launch it.

#### Parameters
 - **plugin_path** _(str)_ -- path to the plugin executable

#### Example

```python
await nz.register_plugin_path('Path/to/plugin.exe')
```

### get_connection_status
_______
Checks the connection status to nizima LIVE.

#### Return
 - **dict** -- dictionary with key 'etablished' and 'enabled'

#### Example

```python
status = await self.nz.get_connection_status()
```

## **Parameter Control**

### insert_live_parameters
_______
Adds new Live2D parameters to the system.

#### Parameters
 - **live_parameters** _(list[dict])_ -- List of parameter with keys 'Id', 'Base', 'Min', 'Max'

#### Example
```python
live_parameters = [{
  "Id": "YourParameterName",
  "Group": "YourParameterGroup",
  "Base": 0, # default value
  "Max": 10, # maximum range
  "Min": -10, # minimal range
  "Repeat": True # Loop parameter
}]

await nz.insert_live_parameters(live_parameters)
```

### set_live_parameter_values
_______
Sets the Live2D parameter values for a model, or for all models if none are specified.

#### Parameters
 - **live_parameter_values** _(list[dict])_ -- List of parameter values with keys 'Id' and 'Value'

```python
parameter_values = [{'Id':'Yaw', 'Value': 1}]
await nz.set_live_parameter_values(parameter_values)
```


### get_live_parameters
_______
Gets the full list of available Live2D parameters with their properties, including their creator.

#### Parameters
 - **model_id** _(str)_ -- ID of the model

#### Return
- **list[dict]** -- list of parameter dictionaries with 'Id', 'Group', 'Base', 'Min', 'Max', 'Repeat', 'CreatedBy'
- 
#### Example
```python
parameters = await self.nz.get_live_parameter_values(model_id='777')
```

### get_live_parameter_values
_______
Retrieves the current Live2D parameter values for a model.

#### Parameters
 - **model_id** _(str)_ -- ID of the model
 - **parameter_ids** _(list[str], optional)_ -- list of parameter IDs to fetch. Fetches all if not specified

#### Return
- **list[dict]** -- List of parameter values

#### Example
```python
parameter_values = await nz.get_live_parameter_values(model_id='777')
```

### set_cubism_parameter_values
_______
Sets the Cubism parameter values for a model.

#### Parameters
 - **model_id** _(str)_ -- ID of the model
 - **parameter_values** _(list[dict])_ -- List of parameter dictionaries with 'Id' and 'Value'

```python
cubism_parameters = [{'Id': 'ArmLeft', 'Value': 1}]
await nz.set_cubism_parameter_values(model_id='777', parameter_values=cubism_parameters)
```

### reset_cubism_parameter_values
_______
Resets the Cubism parameters of a model to their default values.

#### Parameters
 - **model_id** _(str)_ -- ID of the model

```python
await nz.reset_cubism_parameter_values(model_id='777')
```

### get_cubism_parameters
_______
Gets the full list of Cubism parameters for a model along with their properties.

#### Parameters
 - **model_id** _(str)_ -- ID of the model

#### Return
- **list** -- List of parameter ids

```python
cubism_parameters = await nz.get_cubism_parameters(model_id='777')
```

### get_cubism_parameter_values
_______
Retrieves the current Cubism parameter values for a model.

#### Parameters
 - **model_id** _(str)_ -- ID of the model
 - **parameter_ids** _(list[str], optional)_ -- list of parameter IDs to fetch. Fetches all if not specified

#### Return
- **list[dict]** -- List of parameter values with keys 'Id' and 'Value'

```python
cubism_parameter_values = await nz.get_cubism_parameter_values(model_id='777')
```

## **Scene Management**

### add_model
_______
Adds a new model to a specific scene, or in a new window if no scene is specified.

#### Parameters
- **model_path** _(str)_ -- The path to the new model
- **scene_id** _(str, optional)_ -- The ID of the scene. Defaults to None (new window)

#### Return
- **str** -- The ID of the new model

```python
model_id = await nz.add_model(model_path='path/to/model', scene_id='42')
```

### remove_model
_______
Removes a model from current scene.
#### Parameters
- **model_id** _(str)_ -- The ID of the model to remove

#### Example

```python
await nz.add_model(model_id='777')
```

### move_model
_______
Moves a model within a scene by specifying its position, scale, rotation, delay, and interpolation type.

#### Parameters
- **model_id** _(str)_ -- The ID of the model to move
- **absolute** _(bool, optional)_ -- Use absolute positioning. Defaults to False
- **position_x** _(float, optional)_ -- The X position. Defaults to None
- **position_y** _(float, optional)_ -- The Y position. Defaults to None
- **scale** _(float, optional)_ -- The scale factor. Defaults to None
- **rotation** _(float, optional)_ -- The rotation angle in degrees. Defaults to None
- **delay** _(float, optional)_ -- The delay in seconds. Defaults to None
- **interpolation_type** _(str, optional)_ -- The interpolation type. Defaults to None

#### Example

```python
await nz.move_model(model_id='777')
```

### reset_pose
_______
Resets the pose of a model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model

#### Example
```python
await nz.reset_pose(model_id='777')
```

### get_scenes
Retrieves information about all scenes, including the models and elements they contain.

#### return

- **list** -- scenes with models and items information

```python
scenes = await nz.get_scenes()
```

### get_current_scene_id
Gets the ID of the focused scene.

#### Return
- **str** -- ID of the scene

#### Example
```python
scene_id = await nz.get_current_scene_id()
```

## **Model Manipulation**

### register_model
_______
Registers a model in nizima LIVE.

#### Parameters
- **model_path** _(str)_ -- The path to the new model
- **icon_path** _(str, optional)_ -- The path to the icon. Defaults to None

#### Return
- **str** -- The path of the registered model

#### Example
```python
scene_id = await nz.get_current_scene_id()
```

### change_model
_______
Replaces an existing model with another.

#### Parameters
- **model_id** _(str)_ -- The ID of the current model
- **model_path** _(str)_ -- The path to the new model

#### Return
- **str** -- The ID of the new model

#### Example
```python
new_model_id = await nz.change_model(model_id='777', model_path='path/to/model')
```


### get_registered_model_icons
_______
Retrieves the icon data for the specified models

#### Parameters
- **model_paths** _(list[str])_ --  A list of model paths

#### Return
- **list** -- A list of dictionaries containing model paths and base64-encoded icons

#### Example
```python
new_model_id = await nz.get_registered_model_icons(model_path=['path/to/model'])
```

### get_registered_models
_______
Retrieves the list of all models registered in nizima LIVE.

#### Return
- **list** -- A list of registered models with their properties.

#### Example
```python
models = await nz.get_registered_models()
```

### get_models
_______
Retrieves the list of all displayed models with their position and scaling information.

#### Return
- **list** -- A list of displayed models with their properties

#### Example
```python
models = await nz.get_models()
```

## **Model Parts Manipulation**

### set_drawables_color
_______
Changes the color of the specified model's drawables.

#### Parameters
- **model_id** _(str)_ -- The ID of the model
- **drawable_ids** _(list[str])_ -- The IDs of the drawables to modify
- **multiply_color** _(dict, optional)_ -- Multiply color data. Defaults to `None`
- **screen_color** _(dict, optional)_ -- Screen color data. Defaults to `None`

#### Returns
- **dict** -- An empty dictionary on success

#### Example
```python
await nz.set_drawables_color(
    model_id="777",
    drawable_ids=["drawable_1", "drawable_2"],
    multiply_color={"Red": 1, "Green": 1, "Blue": 0, "Float": True, "Alpha": 1},
    screen_color={"Red": 0.9, "Green": 0.6, "Blue": 0.6, "Float": True, "Alpha": 1}
)
```


### set_parts_color
_______
Changes the color of the specified model's parts.

#### Parameters
- **model_id** _(str)_  -- The ID of the model.
- **part_ids** _(list[str])_  -- The IDs of the parts to modify.
- **multiply_color** _(dict, optional)_  -- Multiply color data. Defaults to `None`
- **screen_color** _(dict, optional)_  -- Screen color data. Defaults to `None`


#### Example
```python
await nz.set_parts_color(
    model_id="777",
    part_ids=["part_1", "part_2"],
    multiply_color={"Red": 1, "Green": 1, "Blue": 0, "Float": True, "Alpha": 1},
    screen_color={"Red": 0.9, "Green": 0.6, "Blue": 0.6, "Float": True, "Alpha": 1}
)
```

### set_model_color
_______
Changes the color of the specified model.

#### Parameters
- **model_id** _(str)_: The ID of the model
- **multiply_color** _(dict, optional)_  -- Multiply color data. Defaults to `None`
- **screen_color** _(dict, optional)_  -- Screen color data. Defaults to `None`

#### Example
```python
await nz.set_model_color(
    model_id="777",
    multiply_color={"Red": 1, "Green": 1, "Blue": 0, "Float": True, "Alpha": 1},
    screen_color={"Red": 0.9, "Green": 0.6, "Blue": 0.6, "Float": True, "Alpha": 1}
)
```

### get_drawables
_______
Retrieves the list of drawables for the specified model.

#### Parameters
- **model_id** _(str)_  -- The ID of the model

#### Returns
- **list**  -- A list of drawable IDs

#### Example
```python
drawables = await nz.get_drawables(model_id='777')
```

### get_parts
_______
Retrieves the list of parts for the specified model

#### Parameters
- **model_id** _(str)_  -- The ID of the model

#### Returns
- **list**  -- A list of parts with their properties

#### Example
```python
parts = await nz.get_parts(model_id='777')
```


### get_parts_tree
_______
Retrieves the parts and drawables of the specified model as a tree structure.

#### Parameters
- **model_id** _(str)_  -- The ID of the model

#### Returns
- **dict**  -- The root node of the parts tree

#### Example
```python
parts_tree = await nz.get_parts_tree(model_id='777')
```


## **Item Management**

### add_item
_______
Adds a specified item to the given scene.

#### Parameters
- **scene_id** _(str)_ -- The ID of the scene
- **item_path** _(str)_ -- The path of the item to add

#### Example
```python
await nz.add_item(scene_id='42', item_path='path/to/item')
```


### remove_item
_______
Removes the specified item from the display.

#### Parameters
- **item_id** _(str)_ -- The ID of the item to remove

#### Example
```python
await nz.remove_item(item_id='2')
```


### move_item
_______
Moves the specified item.

#### Parameters
- **item_id** _(str)_ -- The ID of the item to move.
- **absolute** _(bool, optional)_ -- If true, use absolute positioning. Defaults to `False`
- **position_x** _(float, optional)_ -- The X position. Defaults to `None`
- **position_y** _(float, optional)_ -- The Y position. Defaults to `None`
- **scale** _(float, optional)_ -- The scale factor. Defaults to `None`
- **rotation** _(float, optional)_ -- The rotation angle in degrees. Defaults to `None`
- **delay** _(float, optional)_ -- The delay in seconds. Defaults to `None`
- **interpolation_type** _(str, optional)_ -- The interpolation type. Defaults to `None`

#### Example
```python
await nz.move_item(
    item_id="10002",
    position_x=100,
    position_y=200,
    scale=1.5,
    rotation=45,
    absolute=True
)
```


### get_registered_items
_______
Retrieves the list of items registered in Nizima LIVE.

#### Returns
- **list** -- A list of registered items with their properties

#### Example
```python
registered_items = await nz.get_registered_items()
```


### get_current_model_id
_______
Retrieves the ID of the last selected model.

#### Returns
- **str** -- model ID

#### Example
```python
model_id = await nz.get_current_model_id()
```


## **Motion Control**

### start_motion
_______
Starts the motion of the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model
- **motion_path** _(str)_ -- The path of the motion

#### Example
```python
await nz.start_motion(model_id='777', motion_path="/path/to/motion")
```


### stop_motion
_______
Stops the motion of the specified model.
To return to the state before motion playback, use `ResetPose` and `ResetCubismParameterValues`.

#### Parameters
- **model_id** _(str)_ -- The ID of the model

#### Example
```python
await nz.stop_motion(model_id='777')
```

### get_motions
_______
Retrieves the list of motions for the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model

#### Returns
- **list** -- A list of motions with their properties

#### Example
```python
motions = await nz.get_motions(model_id='777')
```


## **Expression Management**

### stop_all_expressions
_______
Stops all expressions of the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model

#### Example
```python
await nz.stop_all_expressions("model_123")
```


### start_expression
_______
Starts a specific expression for the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model.
- **expression_path** _(str)_ -- The path of the expression.


#### Example
```python
await nz.start_expression(model_id='777', expression_path="/path/to/expression")
```


### stop_expression
_______
Stops a specific expression of the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model
- **expression_path** _(str)_ -- The path of the expression

#### Example
```python
await nz.stop_expression(model_id='777', expression_path="/path/to/expression")
```

### get_expressions
_______
Retrieves the list of expressions for the specified model.

#### Parameters
- **model_id** _(str)_ -- The ID of the model.

#### Example
```python
expressions = await nz.get_expressions(model_id='777')
```