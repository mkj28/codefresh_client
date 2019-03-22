# codefresh_client.TriggersApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_create**](TriggersApi.md#triggers_create) | **POST** /hermes/triggers/{event}/{pipeline} | Create
[**triggers_delete**](TriggersApi.md#triggers_delete) | **DELETE** /hermes/triggers/{event}/{pipeline} | Delete
[**triggers_get_event_triggers**](TriggersApi.md#triggers_get_event_triggers) | **GET** /hermes/triggers/event/{event} | Get event triggers
[**triggers_get_pipeline_triggers**](TriggersApi.md#triggers_get_pipeline_triggers) | **GET** /hermes/triggers/pipeline/{pipeline} | Get pipeline triggers
[**triggers_list**](TriggersApi.md#triggers_list) | **GET** /hermes/triggers | List


# **triggers_create**
> object triggers_create(event, pipeline, unknown_base_type=unknown_base_type)

Create

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.TriggersApi(codefresh_client.ApiClient(configuration))
event = 'event_example' # str | Event
pipeline = 'pipeline_example' # str | Pipeline
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Create
    api_response = api_instance.triggers_create(event, pipeline, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->triggers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event | 
 **pipeline** | **str**| Pipeline | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_delete**
> object triggers_delete(event, pipeline)

Delete

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.TriggersApi(codefresh_client.ApiClient(configuration))
event = 'event_example' # str | Event
pipeline = 'pipeline_example' # str | Pipeline

try:
    # Delete
    api_response = api_instance.triggers_delete(event, pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->triggers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event | 
 **pipeline** | **str**| Pipeline | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_get_event_triggers**
> object triggers_get_event_triggers(event)

Get event triggers

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.TriggersApi(codefresh_client.ApiClient(configuration))
event = 'event_example' # str | Event

try:
    # Get event triggers
    api_response = api_instance.triggers_get_event_triggers(event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->triggers_get_event_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**| Event | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_get_pipeline_triggers**
> object triggers_get_pipeline_triggers(pipeline)

Get pipeline triggers

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.TriggersApi(codefresh_client.ApiClient(configuration))
pipeline = 'pipeline_example' # str | Pipeline

try:
    # Get pipeline triggers
    api_response = api_instance.triggers_get_pipeline_triggers(pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->triggers_get_pipeline_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | **str**| Pipeline | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_list**
> object triggers_list()

List

### Example

* Api Key Authentication (apiKey): 
```python
from __future__ import print_function
import time
import codefresh_client
from codefresh_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = codefresh_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codefresh_client.TriggersApi(codefresh_client.ApiClient(configuration))

try:
    # List
    api_response = api_instance.triggers_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->triggers_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

