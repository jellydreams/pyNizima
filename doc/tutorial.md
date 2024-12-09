# How to Use the Pynizima Library

### Installation

To install the **pynizima** library, run the following command:

```
pip install pynizima
```

### Import Libraries

You need to import the necessary modules before starting your code. 

```python
from pynizima import NizimaRequest
import asyncio
```

### Creating an Instance

To interact with Nizima, create an instance of `NizimaRequest`. This instance will allow you to send requests.

```python
nz = NizimaRequest()
```

By default, the connection address is `localhost:22022`, but you can specify a custom address if needed:

```python
nz = NizimaRequest(port=22024, ip="0.0.0.0")
```

### Registering a Plugin

Before you can connect, you need to create a plugin in **Nizima**. This process will give you a **token** that is required for establishing a connection.

```python
token = await nz.register_plugin('PluginName', 'YourDevName')
```

### Establishing a Connection

Once you have your token, you can use it to establish a connection with **Nizima LIVE**.

```python
connection_enabled = await nz.establish_connection('PluginName', token)
if connection_enabled:
    # Once connected, you can send requests
    # Continue with your logic here
```

### Sending Requests

After successfully connecting, you can start sending requests. For example, to retrieve live parameters, you can use the following code:

```python
if connection_enabled:
    parameters = await nz.get_live_parameters()
    print(parameters)
```

### Full Example Code

Here is the complete code putting everything together:

```python
from pynizima import NizimaRequest
import asyncio

async def main():
    plugin_name = 'YourPluginName'
    developer_name = 'YourDevName'
    
    # Create instance of NizimaRequest
    nz = NizimaRequest()
    
    # Register your plugin and get the token
    token = await nz.register_plugin(plugin_name, developer_name)
    
    # Establish connection to Nizima LIVE
    connection_enabled = await nz.establish_connection(plugin_name, token)
    
    if connection_enabled:
        # Once connected, you can send your requests
        parameters = await nz.get_live_parameters()
        print(parameters)

if __name__ == "__main__":
    asyncio.run(main())
```

### Available Methods

For a full list of available methods and their descriptions, check the [methods documentation](NizimaRequest.md).


