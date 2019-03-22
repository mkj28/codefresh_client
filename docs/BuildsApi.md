# codefresh_client.BuildsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflows_get**](BuildsApi.md#workflows_get) | **GET** /builds/{id} | Get
[**workflows_list**](BuildsApi.md#workflows_list) | **GET** /workflow | List
[**workflows_restart**](BuildsApi.md#workflows_restart) | **GET** /builds/rebuild/{id} | Restart


# **workflows_get**
> object workflows_get(id)

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
api_instance = codefresh_client.BuildsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Get
    api_response = api_instance.workflows_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->workflows_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_list**
> object workflows_list(limit=limit, page=page, status=status, trigger=trigger, pipeline=pipeline)

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
api_instance = codefresh_client.BuildsApi(codefresh_client.ApiClient(configuration))
limit = 56 # int | Limit (optional)
page = 56 # int | Page (optional)
status = 'status_example' # str | Status (optional)
trigger = 'trigger_example' # str | Trigger (optional)
pipeline = 'pipeline_example' # str | Pipeline (optional)

try:
    # List
    api_response = api_instance.workflows_list(limit=limit, page=page, status=status, trigger=trigger, pipeline=pipeline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->workflows_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit | [optional] 
 **page** | **int**| Page | [optional] 
 **status** | **str**| Status | [optional] 
 **trigger** | **str**| Trigger | [optional] 
 **pipeline** | **str**| Pipeline | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_restart**
> object workflows_restart(id)

Restart

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
api_instance = codefresh_client.BuildsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Restart
    api_response = api_instance.workflows_restart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->workflows_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

