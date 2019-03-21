# codefresh_client.PipelinesApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pipelines_create**](PipelinesApi.md#pipelines_create) | **POST** /pipelines | Create
[**pipelines_delete**](PipelinesApi.md#pipelines_delete) | **DELETE** /pipelines/{name} | Delete
[**pipelines_get**](PipelinesApi.md#pipelines_get) | **GET** /pipelines/{name} | Get
[**pipelines_list**](PipelinesApi.md#pipelines_list) | **GET** /pipelines | List
[**pipelines_replace**](PipelinesApi.md#pipelines_replace) | **PUT** /pipelines/{name} | Replace
[**pipelines_run**](PipelinesApi.md#pipelines_run) | **POST** /pipelines/run/{name} | Run
[**pipelines_validate_yaml**](PipelinesApi.md#pipelines_validate_yaml) | **POST** /pipelines/yaml/validator | Validate yaml
[**runtime_launch**](PipelinesApi.md#runtime_launch) | **POST** /runtime/testit | Launch


# **pipelines_create**
> pipelines_create(unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Create
    api_instance.pipelines_create(unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_delete**
> pipelines_delete(name)

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name of pipeline

try:
    # Delete
    api_instance.pipelines_delete(name)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pipeline | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get**
> object pipelines_get(name, decrypt_variables=decrypt_variables)

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name of pipeline
decrypt_variables = 'decrypt_variables_example' # str |  (optional)

try:
    # Get
    api_response = api_instance.pipelines_get(name, decrypt_variables=decrypt_variables)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pipeline | 
 **decrypt_variables** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_list**
> object pipelines_list(offset=offset, id=id, limit=limit, labels=labels)

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
offset = 56 # int |  (optional)
id = 'id_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)
labels = 'labels_example' # str |  (optional)

try:
    # List
    api_response = api_instance.pipelines_list(offset=offset, id=id, limit=limit, labels=labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **id** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 
 **labels** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_replace**
> InlineResponse2004 pipelines_replace(name, inline_object25=inline_object25)

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name of pipeline
inline_object25 = codefresh_client.InlineObject25() # InlineObject25 |  (optional)

try:
    # Replace
    api_response = api_instance.pipelines_replace(name, inline_object25=inline_object25)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of pipeline | 
 **inline_object25** | [**InlineObject25**](InlineObject25.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_run**
> pipelines_run(name, unknown_base_type=unknown_base_type)

Run

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Run
    api_instance.pipelines_run(name, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_validate_yaml**
> pipelines_validate_yaml(unknown_base_type=unknown_base_type)

Validate yaml

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Validate yaml
    api_instance.pipelines_validate_yaml(unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PipelinesApi->pipelines_validate_yaml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_launch**
> runtime_launch(inline_object30=inline_object30)

Launch

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
api_instance = codefresh_client.PipelinesApi(codefresh_client.ApiClient(configuration))
inline_object30 = codefresh_client.InlineObject30() # InlineObject30 |  (optional)

try:
    # Launch
    api_instance.runtime_launch(inline_object30=inline_object30)
except ApiException as e:
    print("Exception when calling PipelinesApi->runtime_launch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object30** | [**InlineObject30**](InlineObject30.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

