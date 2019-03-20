# codefresh_client.HelmChartsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_charts_install**](HelmChartsApi.md#helm_charts_install) | **POST** /kubernetes/chart/install | Install
[**helm_charts_promote**](HelmChartsApi.md#helm_charts_promote) | **POST** /kubernetes/chart/promote | Promote


# **helm_charts_install**
> helm_charts_install(selector, tiller_namespace, unknown_base_type=unknown_base_type)

Install

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
api_instance = codefresh_client.HelmChartsApi(codefresh_client.ApiClient(configuration))
selector = 'selector_example' # str | 
tiller_namespace = 'tiller_namespace_example' # str | 
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Install
    api_instance.helm_charts_install(selector, tiller_namespace, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling HelmChartsApi->helm_charts_install: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **selector** | **str**|  | 
 **tiller_namespace** | **str**|  | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_charts_promote**
> helm_charts_promote(tiller_namespace, selector=selector, unknown_base_type=unknown_base_type)

Promote

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
api_instance = codefresh_client.HelmChartsApi(codefresh_client.ApiClient(configuration))
tiller_namespace = 'tiller_namespace_example' # str | 
selector = 'selector_example' # str |  (optional)
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Promote
    api_instance.helm_charts_promote(tiller_namespace, selector=selector, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling HelmChartsApi->helm_charts_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tiller_namespace** | **str**|  | 
 **selector** | **str**|  | [optional] 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

