# codefresh_client.DefaultApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_user_id_resend_invite_post**](DefaultApi.md#accounts_account_id_user_id_resend_invite_post) | **POST** /accounts/{accountId}/{userId}/resendInvite | 
[**admin_runtime_environments_account_modify_runtime_environment_name_delete**](DefaultApi.md#admin_runtime_environments_account_modify_runtime_environment_name_delete) | **DELETE** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | 
[**admin_runtime_environments_account_modify_runtime_environment_name_put**](DefaultApi.md#admin_runtime_environments_account_modify_runtime_environment_name_put) | **PUT** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | 
[**registries_registry_id_default_patch**](DefaultApi.md#registries_registry_id_default_patch) | **PATCH** /registries/{registryId}/default | 
[**registries_registry_id_patch**](DefaultApi.md#registries_registry_id_patch) | **PATCH** /registries/{registryId} | 
[**user_onboarding_status_account_post**](DefaultApi.md#user_onboarding_status_account_post) | **POST** /user/onboarding-status/account | 
[**user_onboarding_status_user_post**](DefaultApi.md#user_onboarding_status_user_post) | **POST** /user/onboarding-status/user | 
[**user_post**](DefaultApi.md#user_post) | **POST** /user | 


# **accounts_account_id_user_id_resend_invite_post**
> accounts_account_id_user_id_resend_invite_post()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.accounts_account_id_user_id_resend_invite_post()
except ApiException as e:
    print("Exception when calling DefaultApi->accounts_account_id_user_id_resend_invite_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_runtime_environments_account_modify_runtime_environment_name_delete**
> admin_runtime_environments_account_modify_runtime_environment_name_delete()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.admin_runtime_environments_account_modify_runtime_environment_name_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->admin_runtime_environments_account_modify_runtime_environment_name_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_runtime_environments_account_modify_runtime_environment_name_put**
> admin_runtime_environments_account_modify_runtime_environment_name_put()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.admin_runtime_environments_account_modify_runtime_environment_name_put()
except ApiException as e:
    print("Exception when calling DefaultApi->admin_runtime_environments_account_modify_runtime_environment_name_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_registry_id_default_patch**
> registries_registry_id_default_patch()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.registries_registry_id_default_patch()
except ApiException as e:
    print("Exception when calling DefaultApi->registries_registry_id_default_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_registry_id_patch**
> registries_registry_id_patch(inline_object28=inline_object28)



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))
inline_object28 = codefresh_client.InlineObject28() # InlineObject28 |  (optional)

try:
    api_instance.registries_registry_id_patch(inline_object28=inline_object28)
except ApiException as e:
    print("Exception when calling DefaultApi->registries_registry_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object28** | [**InlineObject28**](InlineObject28.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_onboarding_status_account_post**
> user_onboarding_status_account_post()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.user_onboarding_status_account_post()
except ApiException as e:
    print("Exception when calling DefaultApi->user_onboarding_status_account_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_onboarding_status_user_post**
> user_onboarding_status_user_post()



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))

try:
    api_instance.user_onboarding_status_user_post()
except ApiException as e:
    print("Exception when calling DefaultApi->user_onboarding_status_user_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> user_post(inline_object33=inline_object33)



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
api_instance = codefresh_client.DefaultApi(codefresh_client.ApiClient(configuration))
inline_object33 = codefresh_client.InlineObject33() # InlineObject33 |  (optional)

try:
    api_instance.user_post(inline_object33=inline_object33)
except ApiException as e:
    print("Exception when calling DefaultApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object33** | [**InlineObject33**](InlineObject33.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

