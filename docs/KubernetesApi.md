# codefresh_client.KubernetesApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kubernetes_generate_image_pull_secret**](KubernetesApi.md#kubernetes_generate_image_pull_secret) | **POST** /kubernetes/secrets/imagePullSecret | Generate image pull secret


# **kubernetes_generate_image_pull_secret**
> kubernetes_generate_image_pull_secret(namespace, selector, unknown_base_type=unknown_base_type)

Generate image pull secret

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
api_instance = codefresh_client.KubernetesApi(codefresh_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
selector = 'selector_example' # str | 
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Generate image pull secret
    api_instance.kubernetes_generate_image_pull_secret(namespace, selector, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling KubernetesApi->kubernetes_generate_image_pull_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **selector** | **str**|  | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

