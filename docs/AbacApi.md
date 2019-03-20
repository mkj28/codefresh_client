# codefresh_client.AbacApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abac_list_by_resource**](AbacApi.md#abac_list_by_resource) | **GET** /abac/resource/{resource} | Get rules by resource
[**abac_list_by_team**](AbacApi.md#abac_list_by_team) | **GET** /abac/team/{teamId} | Get rules by team id
[**abac_rules_create**](AbacApi.md#abac_rules_create) | **POST** /abac | Create rule
[**abac_rules_create_in_batch**](AbacApi.md#abac_rules_create_in_batch) | **POST** /abac/teamRules | Create rules in batch
[**abac_rules_create_or_delete**](AbacApi.md#abac_rules_create_or_delete) | **POST** /abac/batch | Create or delete rules
[**abac_rules_delete**](AbacApi.md#abac_rules_delete) | **DELETE** /abac/{rule} | Delete rule
[**abac_rules_get**](AbacApi.md#abac_rules_get) | **GET** /abac/{rule} | Get rule
[**abac_rules_list**](AbacApi.md#abac_rules_list) | **GET** /abac | List rules
[**abac_rules_tags_create**](AbacApi.md#abac_rules_tags_create) | **POST** /abac/tags/rules | Create rules tags
[**abac_rules_tags_update**](AbacApi.md#abac_rules_tags_update) | **POST** /abac/tags/rule/{rule} | Update rule tags


# **abac_list_by_resource**
> abac_list_by_resource(resource)

Get rules by resource

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
resource = 'resource_example' # str | The id of the resource

try:
    # Get rules by resource
    api_instance.abac_list_by_resource(resource)
except ApiException as e:
    print("Exception when calling AbacApi->abac_list_by_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| The id of the resource | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_list_by_team**
> abac_list_by_team(team_id)

Get rules by team id

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team

try:
    # Get rules by team id
    api_instance.abac_list_by_team(team_id)
except ApiException as e:
    print("Exception when calling AbacApi->abac_list_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_create**
> abac_rules_create(inline_object=inline_object)

Create rule

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
inline_object = codefresh_client.InlineObject() # InlineObject |  (optional)

try:
    # Create rule
    api_instance.abac_rules_create(inline_object=inline_object)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_create_in_batch**
> abac_rules_create_in_batch(unknown_base_type)

Create rules in batch

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
unknown_base_type = codefresh_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    # Create rules in batch
    api_instance.abac_rules_create_in_batch(unknown_base_type)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_create_in_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_create_or_delete**
> abac_rules_create_or_delete(inline_object1=inline_object1)

Create or delete rules

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
inline_object1 = codefresh_client.InlineObject1() # InlineObject1 |  (optional)

try:
    # Create or delete rules
    api_instance.abac_rules_create_or_delete(inline_object1=inline_object1)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_create_or_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_delete**
> abac_rules_delete(rule)

Delete rule

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
rule = 'rule_example' # str | The id of the rule

try:
    # Delete rule
    api_instance.abac_rules_delete(rule)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The id of the rule | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_get**
> abac_rules_get(rule)

Get rule

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
rule = 'rule_example' # str | The id of the rule

try:
    # Get rule
    api_instance.abac_rules_get(rule)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The id of the rule | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_list**
> abac_rules_list()

List rules

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))

try:
    # List rules
    api_instance.abac_rules_list()
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_list: %s\n" % e)
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

# **abac_rules_tags_create**
> abac_rules_tags_create(inline_object3=inline_object3)

Create rules tags

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
inline_object3 = codefresh_client.InlineObject3() # InlineObject3 |  (optional)

try:
    # Create rules tags
    api_instance.abac_rules_tags_create(inline_object3=inline_object3)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abac_rules_tags_update**
> abac_rules_tags_update(rule, inline_object2=inline_object2)

Update rule tags

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
api_instance = codefresh_client.AbacApi(codefresh_client.ApiClient(configuration))
rule = 'rule_example' # str | The id of the rule
inline_object2 = codefresh_client.InlineObject2() # InlineObject2 |  (optional)

try:
    # Update rule tags
    api_instance.abac_rules_tags_update(rule, inline_object2=inline_object2)
except ApiException as e:
    print("Exception when calling AbacApi->abac_rules_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The id of the rule | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

