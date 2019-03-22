# codefresh_client.HelmReleasesApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_releases_delete**](HelmReleasesApi.md#helm_releases_delete) | **POST** /kubernetes/releases/{releaseName}/delete | Delete
[**helm_releases_test**](HelmReleasesApi.md#helm_releases_test) | **POST** /kubernetes/releases/{releaseName}/test | Test


# **helm_releases_delete**
> object helm_releases_delete(release_name, selector, tiller_namespace, unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.HelmReleasesApi(codefresh_client.ApiClient(configuration))
release_name = 'release_name_example' # str | Release name
selector = 'selector_example' # str | Selector
tiller_namespace = 'tiller_namespace_example' # str | Tiller namespace
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Delete
    api_response = api_instance.helm_releases_delete(release_name, selector, tiller_namespace, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReleasesApi->helm_releases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_name** | **str**| Release name | 
 **selector** | **str**| Selector | 
 **tiller_namespace** | **str**| Tiller namespace | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_releases_test**
> object helm_releases_test(release_name, selector=selector, unknown_base_type=unknown_base_type)

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
api_instance = codefresh_client.HelmReleasesApi(codefresh_client.ApiClient(configuration))
release_name = 'release_name_example' # str | Release name
selector = 'selector_example' # str | Selector (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Test
    api_response = api_instance.helm_releases_test(release_name, selector=selector, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelmReleasesApi->helm_releases_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_name** | **str**| Release name | 
 **selector** | **str**| Selector | [optional] 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

