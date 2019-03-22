# codefresh_client.TriggersTypesApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_types_get**](TriggersTypesApi.md#triggers_types_get) | **GET** /hermes/types/{type}/{kind} | Get
[**triggers_types_list**](TriggersTypesApi.md#triggers_types_list) | **GET** /hermes/types | List


# **triggers_types_get**
> object triggers_types_get(type, kind)

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
api_instance = codefresh_client.TriggersTypesApi(codefresh_client.ApiClient(configuration))
type = 'type_example' # str | Type
kind = 'kind_example' # str | Kind

try:
    # Get
    api_response = api_instance.triggers_types_get(type, kind)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersTypesApi->triggers_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type | 
 **kind** | **str**| Kind | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_types_list**
> object triggers_types_list()

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
api_instance = codefresh_client.TriggersTypesApi(codefresh_client.ApiClient(configuration))

try:
    # List
    api_response = api_instance.triggers_types_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersTypesApi->triggers_types_list: %s\n" % e)
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

