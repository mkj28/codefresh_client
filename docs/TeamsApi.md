# codefresh_client.TeamsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_add_user**](TeamsApi.md#teams_add_user) | **PUT** /team/{teamId}/{userId}/assignUserToTeam | Add user
[**teams_create**](TeamsApi.md#teams_create) | **POST** /team | Create
[**teams_list**](TeamsApi.md#teams_list) | **GET** /team | List
[**teams_list_by_user**](TeamsApi.md#teams_list_by_user) | **GET** /team/{userId}/findTeamsByUser | List by user
[**teams_remove_user**](TeamsApi.md#teams_remove_user) | **PUT** /team/{teamId}/{userId}/deleteUserFromTeam | Remove user
[**teams_synchronize_client_with_group**](TeamsApi.md#teams_synchronize_client_with_group) | **GET** /team/group/synchronize/name/{name}/type/{type} | Synchronize client with group


# **teams_add_user**
> teams_add_user(team_id, user_id)

Add user

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team
user_id = 'user_id_example' # str | The user id for assign

try:
    # Add user
    api_instance.teams_add_user(team_id, user_id)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
 **user_id** | **str**| The user id for assign | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create**
> teams_create(inline_object32=inline_object32)

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))
inline_object32 = codefresh_client.InlineObject32() # InlineObject32 |  (optional)

try:
    # Create
    api_instance.teams_create(inline_object32=inline_object32)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object32** | [**InlineObject32**](InlineObject32.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list**
> teams_list()

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))

try:
    # List
    api_instance.teams_list()
except ApiException as e:
    print("Exception when calling TeamsApi->teams_list: %s\n" % e)
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

# **teams_list_by_user**
> teams_list_by_user(user_id)

List by user

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # List by user
    api_instance.teams_list_by_user(user_id)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_list_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_user**
> teams_remove_user(team_id, user_id)

Remove user

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team
user_id = 'user_id_example' # str | The user id for assign

try:
    # Remove user
    api_instance.teams_remove_user(team_id, user_id)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
 **user_id** | **str**| The user id for assign | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_synchronize_client_with_group**
> teams_synchronize_client_with_group(name, type, access_token=access_token)

Synchronize client with group

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
api_instance = codefresh_client.TeamsApi(codefresh_client.ApiClient(configuration))
name = 'name_example' # str | 
type = 'type_example' # str | 
access_token = 'access_token_example' # str |  (optional)

try:
    # Synchronize client with group
    api_instance.teams_synchronize_client_with_group(name, type, access_token=access_token)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_synchronize_client_with_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | **str**|  | 
 **access_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

