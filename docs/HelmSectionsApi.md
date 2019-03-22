# codefresh_client.HelmSectionsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_sections_create**](HelmSectionsApi.md#helm_sections_create) | **POST** /helm/boards/sections | Create
[**helm_sections_delete**](HelmSectionsApi.md#helm_sections_delete) | **DELETE** /helm/boards/sections/{id} | Delete
[**helm_sections_delete_all**](HelmSectionsApi.md#helm_sections_delete_all) | **DELETE** /helm/boards/{boardId}/sections | Delete all
[**helm_sections_get**](HelmSectionsApi.md#helm_sections_get) | **GET** /helm/boards/sections/{id} | Get
[**helm_sections_get_by_name**](HelmSectionsApi.md#helm_sections_get_by_name) | **GET** /helm/boards/{boardId}/sections/name/{name} | Get by name
[**helm_sections_list**](HelmSectionsApi.md#helm_sections_list) | **GET** /helm/boards/{boardId}/sections | List
[**helm_sections_patch**](HelmSectionsApi.md#helm_sections_patch) | **PATCH** /helm/boards/sections/{id} | Patch
[**helm_sections_reorder**](HelmSectionsApi.md#helm_sections_reorder) | **POST** /helm/boards/sections/reorder | Reorder
[**helm_sections_update**](HelmSectionsApi.md#helm_sections_update) | **PUT** /helm/boards/sections/{id} | Update


# **helm_sections_create**
> InlineResponse2002 helm_sections_create(inline_object18=inline_object18)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
inline_object18 = codefresh_client.InlineObject18() # InlineObject18 |  (optional)

try:
    # Create
    api_response = api_instance.helm_sections_create(inline_object18=inline_object18)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_delete**
> InlineResponse2002 helm_sections_delete(id)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Delete
    api_response = api_instance.helm_sections_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_delete_all**
> InlineResponse2001 helm_sections_delete_all(board_id)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
board_id = 'board_id_example' # str | id of a board

try:
    # Delete all
    api_response = api_instance.helm_sections_delete_all(board_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_delete_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| id of a board | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_get**
> InlineResponse200 helm_sections_get(id)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Get
    api_response = api_instance.helm_sections_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_get: %s\n" % e)
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

# **helm_sections_get_by_name**
> InlineResponse200 helm_sections_get_by_name(board_id, name)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
board_id = 'board_id_example' # str | id of a board
name = 'name_example' # str | name of a section

try:
    # Get by name
    api_response = api_instance.helm_sections_get_by_name(board_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| id of a board | 
 **name** | **str**| name of a section | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_list**
> InlineResponse2002 helm_sections_list(board_id)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
board_id = 'board_id_example' # str | id of a board

try:
    # List
    api_response = api_instance.helm_sections_list(board_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**| id of a board | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_patch**
> InlineResponse2003 helm_sections_patch(id, inline_object21=inline_object21)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object21 = codefresh_client.InlineObject21() # InlineObject21 |  (optional)

try:
    # Patch
    api_response = api_instance.helm_sections_patch(id, inline_object21=inline_object21)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_reorder**
> object helm_sections_reorder(inline_object19=inline_object19)

Reorder

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
inline_object19 = codefresh_client.InlineObject19() # InlineObject19 |  (optional)

try:
    # Reorder
    api_response = api_instance.helm_sections_reorder(inline_object19=inline_object19)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_sections_update**
> InlineResponse2003 helm_sections_update(id, inline_object20=inline_object20)

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
api_instance = codefresh_client.HelmSectionsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object20 = codefresh_client.InlineObject20() # InlineObject20 |  (optional)

try:
    # Update
    api_response = api_instance.helm_sections_update(id, inline_object20=inline_object20)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmSectionsApi->helm_sections_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

