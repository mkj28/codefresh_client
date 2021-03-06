# codefresh_client.HelmReposApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_repos_create**](HelmReposApi.md#helm_repos_create) | **POST** /helm/repos | Create
[**helm_repos_delete**](HelmReposApi.md#helm_repos_delete) | **DELETE** /helm/repos/{name} | Delete
[**helm_repos_get**](HelmReposApi.md#helm_repos_get) | **GET** /helm/repos/{name} | Get
[**helm_repos_list**](HelmReposApi.md#helm_repos_list) | **GET** /helm/repos | List
[**helm_repos_update**](HelmReposApi.md#helm_repos_update) | **PUT** /helm/repos/{name} | Update


# **helm_repos_create**
> object helm_repos_create(unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.HelmReposApi(codefresh_client.ApiClient(configuration))
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Create
    api_response = api_instance.helm_repos_create(unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReposApi->helm_repos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repos_delete**
> object helm_repos_delete(name)

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
api_instance = codefresh_client.HelmReposApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name

try:
    # Delete
    api_response = api_instance.helm_repos_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReposApi->helm_repos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repos_get**
> object helm_repos_get(name)

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
api_instance = codefresh_client.HelmReposApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name

try:
    # Get
    api_response = api_instance.helm_repos_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReposApi->helm_repos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repos_list**
> object helm_repos_list(query=query)

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
api_instance = codefresh_client.HelmReposApi(codefresh_client.ApiClient(configuration))
query = 'query_example' # str | Query (optional)

try:
    # List
    api_response = api_instance.helm_repos_list(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReposApi->helm_repos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repos_update**
> object helm_repos_update(name, unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.HelmReposApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | Name
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Update
    api_response = api_instance.helm_repos_update(name, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReposApi->helm_repos_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

