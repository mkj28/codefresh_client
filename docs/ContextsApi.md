# codefresh_client.ContextsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contexts_create**](ContextsApi.md#contexts_create) | **POST** /contexts | Create
[**contexts_delete**](ContextsApi.md#contexts_delete) | **DELETE** /contexts/{name} | Delete
[**contexts_get**](ContextsApi.md#contexts_get) | **GET** /contexts/{name} | Get
[**contexts_list**](ContextsApi.md#contexts_list) | **GET** /contexts | List
[**contexts_patch**](ContextsApi.md#contexts_patch) | **PATCH** /contexts/{name} | Patch
[**contexts_patch_0**](ContextsApi.md#contexts_patch_0) | **PATCH** /contexts/{name}/default | Patch
[**contexts_replace**](ContextsApi.md#contexts_replace) | **PUT** /contexts/{name} | Replace


# **contexts_create**
> contexts_create(skip_validation=skip_validation, inline_object13=inline_object13)

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
skip_validation = 'skip_validation_example' # str |  (optional)
inline_object13 = codefresh_client.InlineObject13() # InlineObject13 |  (optional)

try:
    # Create
    api_instance.contexts_create(skip_validation=skip_validation, inline_object13=inline_object13)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_validation** | **str**|  | [optional] 
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_delete**
> contexts_delete(name)

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete
    api_instance.contexts_delete(name)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_get**
> object contexts_get(name, decrypt=decrypt)

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
decrypt = 'decrypt_example' # str |  (optional)

try:
    # Get
    api_response = api_instance.contexts_get(name, decrypt=decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **decrypt** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_list**
> object contexts_list(type=type, decrypt=decrypt)

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
type = 'type_example' # str |  (optional)
decrypt = 'decrypt_example' # str |  (optional)

try:
    # List
    api_response = api_instance.contexts_list(type=type, decrypt=decrypt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **decrypt** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_patch**
> contexts_patch(name, inline_object15=inline_object15)

Patch

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
inline_object15 = codefresh_client.InlineObject15() # InlineObject15 |  (optional)

try:
    # Patch
    api_instance.contexts_patch(name, inline_object15=inline_object15)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_patch_0**
> contexts_patch_0(name, inline_object16=inline_object16)

Patch

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
inline_object16 = codefresh_client.InlineObject16() # InlineObject16 |  (optional)

try:
    # Patch
    api_instance.contexts_patch_0(name, inline_object16=inline_object16)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_patch_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contexts_replace**
> contexts_replace(name, inline_object14=inline_object14)

Replace

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
api_instance = codefresh_client.ContextsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
inline_object14 = codefresh_client.InlineObject14() # InlineObject14 |  (optional)

try:
    # Replace
    api_instance.contexts_replace(name, inline_object14=inline_object14)
except ApiException as e:
    print("Exception when calling ContextsApi->contexts_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

