# codefresh_client.AccountsApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_add_account**](AccountsApi.md#accounts_add_account) | **POST** /admin/accounts | Add account
[**accounts_add_existing_user_to_account**](AccountsApi.md#accounts_add_existing_user_to_account) | **POST** /accounts/{accountId}/{userId}/adduser | Add existing user to account
[**accounts_add_pending_user_without_account**](AccountsApi.md#accounts_add_pending_user_without_account) | **POST** /admin/accounts/addpendinguser | Add pending user without account
[**accounts_add_user_to_account**](AccountsApi.md#accounts_add_user_to_account) | **POST** /accounts/{accountId}/adduser | Add user to account
[**accounts_delete_account**](AccountsApi.md#accounts_delete_account) | **DELETE** /admin/accounts/{id} | Delete account
[**accounts_delete_admin**](AccountsApi.md#accounts_delete_admin) | **DELETE** /accounts/{accountId}/{userId}/admin | Delete admin
[**accounts_delete_user_from_account**](AccountsApi.md#accounts_delete_user_from_account) | **DELETE** /accounts/{accountId}/{userId} | Delete user from account
[**accounts_get_by_id**](AccountsApi.md#accounts_get_by_id) | **GET** /admin/accounts/{id} | Get by id
[**accounts_get_users_for_account**](AccountsApi.md#accounts_get_users_for_account) | **GET** /accounts/{accountId}/users | Get users for account
[**accounts_list_accounts**](AccountsApi.md#accounts_list_accounts) | **GET** /admin/accounts | List accounts
[**accounts_set_as_admin**](AccountsApi.md#accounts_set_as_admin) | **POST** /accounts/{accountId}/{userId}/admin | Set as admin
[**accounts_update_account**](AccountsApi.md#accounts_update_account) | **POST** /admin/accounts/{id}/update | Update account
[**accounts_update_account_public_settings**](AccountsApi.md#accounts_update_account_public_settings) | **POST** /accounts/{accountId}/update | Update account public settings
[**accounts_update_user_details**](AccountsApi.md#accounts_update_user_details) | **POST** /accounts/{accountId}/{userId}/updateuser | Update user details


# **accounts_add_account**
> accounts_add_account(inline_object7=inline_object7)

Add account

Add new account. Receives an account object 

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
inline_object7 = codefresh_client.InlineObject7() # InlineObject7 |  (optional)

try:
    # Add account
    api_instance.accounts_add_account(inline_object7=inline_object7)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_add_existing_user_to_account**
> accounts_add_existing_user_to_account(account_id, user_id)

Add existing user to account

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
account_id = 'account_id_example' # str | id of an object
user_id = 'user_id_example' # str | id of an object

try:
    # Add existing user to account
    api_instance.accounts_add_existing_user_to_account(account_id, user_id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_add_existing_user_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| id of an object | 
 **user_id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_add_pending_user_without_account**
> accounts_add_pending_user_without_account(inline_object8=inline_object8)

Add pending user without account

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
inline_object8 = codefresh_client.InlineObject8() # InlineObject8 |  (optional)

try:
    # Add pending user without account
    api_instance.accounts_add_pending_user_without_account(inline_object8=inline_object8)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_add_pending_user_without_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_add_user_to_account**
> accounts_add_user_to_account(id, inline_object4=inline_object4)

Add user to account

Adds a not existing user to an account. the provider field is optional and if not provided it will be taken from the account model

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object4 = codefresh_client.InlineObject4() # InlineObject4 |  (optional)

try:
    # Add user to account
    api_instance.accounts_add_user_to_account(id, inline_object4=inline_object4)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_add_user_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_delete_account**
> accounts_delete_account(id)

Delete account

Not implemented yet

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Delete account
    api_instance.accounts_delete_account(id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_delete_admin**
> accounts_delete_admin(account_id, user_id)

Delete admin

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
account_id = 'account_id_example' # str | id of an object
user_id = 'user_id_example' # str | id of an object

try:
    # Delete admin
    api_instance.accounts_delete_admin(account_id, user_id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_delete_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| id of an object | 
 **user_id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_delete_user_from_account**
> accounts_delete_user_from_account(account_id, user_id)

Delete user from account

Not implemented yet

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
account_id = 'account_id_example' # str | id of an object
user_id = 'user_id_example' # str | id of an object

try:
    # Delete user from account
    api_instance.accounts_delete_user_from_account(account_id, user_id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_delete_user_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| id of an object | 
 **user_id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_by_id**
> accounts_get_by_id(id)

Get by id

Get an account by id

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Get by id
    api_instance.accounts_get_by_id(id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_users_for_account**
> accounts_get_users_for_account(id)

Get users for account

List users of an account

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object

try:
    # Get users for account
    api_instance.accounts_get_users_for_account(id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_users_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_list_accounts**
> object accounts_list_accounts()

List accounts

get all the accounts in the system

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))

try:
    # List accounts
    api_response = api_instance.accounts_list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_list_accounts: %s\n" % e)
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

# **accounts_set_as_admin**
> accounts_set_as_admin(account_id, user_id)

Set as admin

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
account_id = 'account_id_example' # str | id of an object
user_id = 'user_id_example' # str | id of an object

try:
    # Set as admin
    api_instance.accounts_set_as_admin(account_id, user_id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_set_as_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| id of an object | 
 **user_id** | **str**| id of an object | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_update_account**
> accounts_update_account(id, inline_object9=inline_object9)

Update account

Not implemented yet: Update the account info that only codefresh admins (codefresh employees, not account admin) can access

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object9 = codefresh_client.InlineObject9() # InlineObject9 |  (optional)

try:
    # Update account
    api_instance.accounts_update_account(id, inline_object9=inline_object9)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_update_account_public_settings**
> accounts_update_account_public_settings(id, inline_object5=inline_object5)

Update account public settings

Not implemented yet: update the user defined account fields. Receives a settings object (will be defined later)

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object5 = codefresh_client.InlineObject5() # InlineObject5 |  (optional)

try:
    # Update account public settings
    api_instance.accounts_update_account_public_settings(id, inline_object5=inline_object5)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_update_account_public_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_update_user_details**
> accounts_update_user_details(id, inline_object6=inline_object6)

Update user details

Not implemented yet

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
api_instance = codefresh_client.AccountsApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of an object
inline_object6 = codefresh_client.InlineObject6() # InlineObject6 |  (optional)

try:
    # Update user details
    api_instance.accounts_update_user_details(id, inline_object6=inline_object6)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_update_user_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an object | 
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

