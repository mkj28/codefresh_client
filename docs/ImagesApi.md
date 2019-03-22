# codefresh_client.ImagesApi

All URIs are relative to *https://g.codefresh.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_add_from_external_source**](ImagesApi.md#images_add_from_external_source) | **POST** /images/external | Add from external source
[**images_delete_metadata**](ImagesApi.md#images_delete_metadata) | **DELETE** /images/{dockerImageId}/metadata/{keyName} | Delete metadata
[**images_get**](ImagesApi.md#images_get) | **GET** /images/{id} | Get
[**images_get_metadata**](ImagesApi.md#images_get_metadata) | **GET** /images/{dockerImageId}/metadata | Get metadata
[**images_get_tags**](ImagesApi.md#images_get_tags) | **GET** /images/{id}/tags | Get tags
[**images_list**](ImagesApi.md#images_list) | **GET** /images | List
[**images_tag**](ImagesApi.md#images_tag) | **POST** /images/{id}/tag/{tag} | Tag
[**images_untag**](ImagesApi.md#images_untag) | **DELETE** /images/{id}/tag/{tag} | Untag
[**images_upsert_metadata**](ImagesApi.md#images_upsert_metadata) | **POST** /images/{dockerImageId}/metadata | Upsert metadata


# **images_add_from_external_source**
> object images_add_from_external_source()

Add from external source

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))

try:
    # Add from external source
    api_response = api_instance.images_add_from_external_source()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_add_from_external_source: %s\n" % e)
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

# **images_delete_metadata**
> object images_delete_metadata(docker_image_id, key_name)

Delete metadata

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
docker_image_id = 'docker_image_id_example' # str | id of the Image from docker inspect
key_name = 'key_name_example' # str | name of the metadata key

try:
    # Delete metadata
    api_response = api_instance.images_delete_metadata(docker_image_id, key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_delete_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_image_id** | **str**| id of the Image from docker inspect | 
 **key_name** | **str**| name of the metadata key | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_get**
> object images_get(id)

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | id of the Image

try:
    # Get
    api_response = api_instance.images_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the Image | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_get_metadata**
> object images_get_metadata(docker_image_id)

Get metadata

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
docker_image_id = 'docker_image_id_example' # str | id of the Image (from docker inspect)

try:
    # Get metadata
    api_response = api_instance.images_get_metadata(docker_image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_image_id** | **str**| id of the Image (from docker inspect) | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_get_tags**
> object images_get_tags(id)

Get tags

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | name of the image

try:
    # Get tags
    api_response = api_instance.images_get_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name of the image | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_list**
> object images_list(limit=limit, offset=offset, metadata=metadata, tag=tag, type=type, branch=branch, image_display_name_regex=image_display_name_regex, select=select, sha=sha)

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
limit = 'limit_example' # str | Limit (optional)
offset = 'offset_example' # str | Offset (optional)
metadata = 'metadata_example' # str | Metadata (optional)
tag = 'tag_example' # str | Tag (optional)
type = 'type_example' # str | Type (optional)
branch = 'branch_example' # str | Branch (optional)
image_display_name_regex = 'image_display_name_regex_example' # str | Image display name regex (optional)
select = 'select_example' # str | Select (optional)
sha = 'sha_example' # str | Sha (optional)

try:
    # List
    api_response = api_instance.images_list(limit=limit, offset=offset, metadata=metadata, tag=tag, type=type, branch=branch, image_display_name_regex=image_display_name_regex, select=select, sha=sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Limit | [optional] 
 **offset** | **str**| Offset | [optional] 
 **metadata** | **str**| Metadata | [optional] 
 **tag** | **str**| Tag | [optional] 
 **type** | **str**| Type | [optional] 
 **branch** | **str**| Branch | [optional] 
 **image_display_name_regex** | **str**| Image display name regex | [optional] 
 **select** | **str**| Select | [optional] 
 **sha** | **str**| Sha | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_tag**
> object images_tag(id, tag)

Tag

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | image ObjectId
tag = 'tag_example' # str | tag

try:
    # Tag
    api_response = api_instance.images_tag(id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| image ObjectId | 
 **tag** | **str**| tag | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_untag**
> object images_untag(id, tag)

Untag

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
id = 'id_example' # str | image ObjectId
tag = 'tag_example' # str | tag ObjectId

try:
    # Untag
    api_response = api_instance.images_untag(id, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_untag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| image ObjectId | 
 **tag** | **str**| tag ObjectId | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_upsert_metadata**
> object images_upsert_metadata(docker_image_id, inline_object24=inline_object24)

Upsert metadata

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
api_instance = codefresh_client.ImagesApi(codefresh_client.ApiClient(configuration))
docker_image_id = 'docker_image_id_example' # str | id of the Image (from docker inspect)
inline_object24 = codefresh_client.InlineObject24() # InlineObject24 |  (optional)

try:
    # Upsert metadata
    api_response = api_instance.images_upsert_metadata(docker_image_id, inline_object24=inline_object24)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->images_upsert_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_image_id** | **str**| id of the Image (from docker inspect) | 
 **inline_object24** | [**InlineObject24**](InlineObject24.md)|  | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

