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
> object teams_add_user(team_id, user_id)

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
    api_response = api_instance.teams_add_user(team_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
 **user_id** | **str**| The user id for assign | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create**
> object teams_create(inline_object32=inline_object32)

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
    api_response = api_instance.teams_create(inline_object32=inline_object32)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object32** | [**InlineObject32**](InlineObject32.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list**
> object teams_list()

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
    api_response = api_instance.teams_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_by_user**
> object teams_list_by_user(user_id)

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
user_id = 'user_id_example' # str | User id

try:
    # List by user
    api_response = api_instance.teams_list_by_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_list_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_user**
> object teams_remove_user(team_id, user_id)

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
    api_response = api_instance.teams_remove_user(team_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
 **user_id** | **str**| The user id for assign | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_synchronize_client_with_group**
> object teams_synchronize_client_with_group(name, type, access_token=access_token)

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
name = 'name_example' # str | Name
type = 'type_example' # str | Type
access_token = 'access_token_example' # str | Access token (optional)

try:
    # Synchronize client with group
    api_response = api_instance.teams_synchronize_client_with_group(name, type, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_synchronize_client_with_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **type** | **str**| Type | 
 **access_token** | **str**| Access token | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

