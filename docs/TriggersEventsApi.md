# codefresh_client.TriggersEventsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_events_create**](TriggersEventsApi.md#triggers_events_create) | **POST** /hermes/events | Create
[**triggers_events_delete**](TriggersEventsApi.md#triggers_events_delete) | **DELETE** /hermes/events/{event}/{context} | Delete
[**triggers_events_get**](TriggersEventsApi.md#triggers_events_get) | **GET** /hermes/events/{event} | Get
[**triggers_events_list**](TriggersEventsApi.md#triggers_events_list) | **GET** /hermes/events | List


# **triggers_events_create**
> triggers_events_create(public=public, unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.TriggersEventsApi(codefresh_client.ApiClient(configuration))
public = 'public_example' # str |  (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Create
    api_instance.triggers_events_create(public=public, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->triggers_events_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public** | **str**|  | [optional] 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_events_delete**
> triggers_events_delete(event, context)

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
api_instance = codefresh_client.TriggersEventsApi(codefresh_client.ApiClient(configuration))
event = 'event_example' # str | 
context = 'context_example' # str | 

try:
    # Delete
    api_instance.triggers_events_delete(event, context)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->triggers_events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**|  | 
 **context** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_events_get**
> object triggers_events_get(event)

Get

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
api_instance = codefresh_client.TriggersEventsApi(codefresh_client.ApiClient(configuration))
event = 'event_example' # str | 

try:
    # Get
    api_response = api_instance.triggers_events_get(event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->triggers_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | **str**|  | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_events_list**
> object triggers_events_list(type=type, kind=kind, filter=filter, public=public)

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
api_instance = codefresh_client.TriggersEventsApi(codefresh_client.ApiClient(configuration))
type = 'type_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
public = 'public_example' # str |  (optional)

try:
    # List
    api_response = api_instance.triggers_events_list(type=type, kind=kind, filter=filter, public=public)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersEventsApi->triggers_events_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **public** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

