# codefresh_client.HelmBoardsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_boards_create**](HelmBoardsApi.md#helm_boards_create) | **POST** /helm/boards | Create
[**helm_boards_delete**](HelmBoardsApi.md#helm_boards_delete) | **DELETE** /helm/boards/{id} | Delete
[**helm_boards_delete_all**](HelmBoardsApi.md#helm_boards_delete_all) | **DELETE** /helm/boards | Delete all
[**helm_boards_get**](HelmBoardsApi.md#helm_boards_get) | **GET** /helm/boards/{id} | Get
[**helm_boards_get_by_name**](HelmBoardsApi.md#helm_boards_get_by_name) | **GET** /helm/boards/name/{name} | Get by name
[**helm_boards_list**](HelmBoardsApi.md#helm_boards_list) | **GET** /helm/boards | List
[**helm_boards_patch**](HelmBoardsApi.md#helm_boards_patch) | **PATCH** /helm/boards/{id} | Patch
[**helm_boards_update**](HelmBoardsApi.md#helm_boards_update) | **PUT** /helm/boards/{id} | Update


# **helm_boards_create**
> InlineResponse200 helm_boards_create(inline_object17=inline_object17)

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
inline_object17 = codefresh_client.InlineObject17() # InlineObject17 |  (optional)

try:
    # Create
    api_response = api_instance.helm_boards_create(inline_object17=inline_object17)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_delete**
> InlineResponse200 helm_boards_delete(id)

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Delete
    api_response = api_instance.helm_boards_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_delete_all**
> InlineResponse2001 helm_boards_delete_all()

Delete all

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))

try:
    # Delete all
    api_response = api_instance.helm_boards_delete_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_delete_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_get**
> InlineResponse200 helm_boards_get(id)

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Get
    api_response = api_instance.helm_boards_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_get_by_name**
> InlineResponse200 helm_boards_get_by_name(name, columns=columns)

Get by name

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | name of a board
columns = True # bool | include sections in response (optional)

try:
    # Get by name
    api_response = api_instance.helm_boards_get_by_name(name, columns=columns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of a board | 
 **columns** | **bool**| include sections in response | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_list**
> list[InlineResponse200] helm_boards_list()

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))

try:
    # List
    api_response = api_instance.helm_boards_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_patch**
> InlineResponse200 helm_boards_patch(id, inline_object23=inline_object23)

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object23 = codefresh_client.InlineObject23() # InlineObject23 |  (optional)

try:
    # Patch
    api_response = api_instance.helm_boards_patch(id, inline_object23=inline_object23)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object23** | [**InlineObject23**](InlineObject23.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_boards_update**
> InlineResponse200 helm_boards_update(id, inline_object22=inline_object22)

Update

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
api_instance = codefresh_client.HelmBoardsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object22 = codefresh_client.InlineObject22() # InlineObject22 |  (optional)

try:
    # Update
    api_response = api_instance.helm_boards_update(id, inline_object22=inline_object22)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmBoardsApi->helm_boards_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

