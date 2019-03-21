# codefresh_client.CodefreshRegistryApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codefresh_registry_generate_cfcr_token**](CodefreshRegistryApi.md#codefresh_registry_generate_cfcr_token) | **POST** /registry/auth/token | Generate cfcr token
[**registries_create**](CodefreshRegistryApi.md#registries_create) | **POST** /registries | Create
[**registries_delete**](CodefreshRegistryApi.md#registries_delete) | **DELETE** /registries/{registryId} | Delete
[**registries_list**](CodefreshRegistryApi.md#registries_list) | **GET** /registries | List registries
[**registries_test**](CodefreshRegistryApi.md#registries_test) | **POST** /registries/test | Test


# **codefresh_registry_generate_cfcr_token**
> codefresh_registry_generate_cfcr_token(inline_object26=inline_object26)

Generate cfcr token

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
api_instance = codefresh_client.CodefreshRegistryApi(codefresh_client.ApiClient(configuration))
inline_object26 = codefresh_client.InlineObject26() # InlineObject26 |  (optional)

try:
    # Generate cfcr token
    api_instance.codefresh_registry_generate_cfcr_token(inline_object26=inline_object26)
except ApiException as e:
    print("Exception when calling CodefreshRegistryApi->codefresh_registry_generate_cfcr_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object26** | [**InlineObject26**](InlineObject26.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_create**
> registries_create(inline_object27=inline_object27)

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
api_instance = codefresh_client.CodefreshRegistryApi(codefresh_client.ApiClient(configuration))
inline_object27 = codefresh_client.InlineObject27() # InlineObject27 |  (optional)

try:
    # Create
    api_instance.registries_create(inline_object27=inline_object27)
except ApiException as e:
    print("Exception when calling CodefreshRegistryApi->registries_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object27** | [**InlineObject27**](InlineObject27.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_delete**
> registries_delete(id)

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
api_instance = codefresh_client.CodefreshRegistryApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Delete
    api_instance.registries_delete(id)
except ApiException as e:
    print("Exception when calling CodefreshRegistryApi->registries_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_list**
> object registries_list()

List registries

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
api_instance = codefresh_client.CodefreshRegistryApi(codefresh_client.ApiClient(configuration))

try:
    # List registries
    api_response = api_instance.registries_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CodefreshRegistryApi->registries_list: %s\n" % e)
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

# **registries_test**
> registries_test(inline_object29=inline_object29)

Test

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
api_instance = codefresh_client.CodefreshRegistryApi(codefresh_client.ApiClient(configuration))
inline_object29 = codefresh_client.InlineObject29() # InlineObject29 |  (optional)

try:
    # Test
    api_instance.registries_test(inline_object29=inline_object29)
except ApiException as e:
    print("Exception when calling CodefreshRegistryApi->registries_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object29** | [**InlineObject29**](InlineObject29.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

