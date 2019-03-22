# codefresh-client
Codefresh API openAPI 3.0 specification

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.2
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.codefresh.io](https://www.codefresh.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/mkj28/codefresh_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mkj28/codefresh_client.git`)

Then import the package:
```python
import codefresh_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import codefresh_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_response = api_instance.abac_list_by_resource(resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AbacApi->abac_list_by_resource: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://g.codefresh.io/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AbacApi* | [**abac_list_by_resource**](docs/AbacApi.md#abac_list_by_resource) | **GET** /abac/resource/{resource} | Get rules by resource
*AbacApi* | [**abac_list_by_team**](docs/AbacApi.md#abac_list_by_team) | **GET** /abac/team/{teamId} | Get rules by team id
*AbacApi* | [**abac_rules_create**](docs/AbacApi.md#abac_rules_create) | **POST** /abac | Create rule
*AbacApi* | [**abac_rules_create_in_batch**](docs/AbacApi.md#abac_rules_create_in_batch) | **POST** /abac/teamRules | Create rules in batch
*AbacApi* | [**abac_rules_create_or_delete**](docs/AbacApi.md#abac_rules_create_or_delete) | **POST** /abac/batch | Create or delete rules
*AbacApi* | [**abac_rules_delete**](docs/AbacApi.md#abac_rules_delete) | **DELETE** /abac/{rule} | Delete rule
*AbacApi* | [**abac_rules_get**](docs/AbacApi.md#abac_rules_get) | **GET** /abac/{rule} | Get rule
*AbacApi* | [**abac_rules_list**](docs/AbacApi.md#abac_rules_list) | **GET** /abac | List rules
*AbacApi* | [**abac_rules_tags_create**](docs/AbacApi.md#abac_rules_tags_create) | **POST** /abac/tags/rules | Create rules tags
*AbacApi* | [**abac_rules_tags_update**](docs/AbacApi.md#abac_rules_tags_update) | **POST** /abac/tags/rule/{rule} | Update rule tags
*AccountsApi* | [**accounts_add_account**](docs/AccountsApi.md#accounts_add_account) | **POST** /admin/accounts | Add account
*AccountsApi* | [**accounts_add_existing_user_to_account**](docs/AccountsApi.md#accounts_add_existing_user_to_account) | **POST** /accounts/{accountId}/{userId}/adduser | Add existing user to account
*AccountsApi* | [**accounts_add_pending_user_without_account**](docs/AccountsApi.md#accounts_add_pending_user_without_account) | **POST** /admin/accounts/addpendinguser | Add pending user without account
*AccountsApi* | [**accounts_add_user_to_account**](docs/AccountsApi.md#accounts_add_user_to_account) | **POST** /accounts/{accountId}/adduser | Add user to account
*AccountsApi* | [**accounts_delete_account**](docs/AccountsApi.md#accounts_delete_account) | **DELETE** /admin/accounts/{id} | Delete account
*AccountsApi* | [**accounts_delete_admin**](docs/AccountsApi.md#accounts_delete_admin) | **DELETE** /accounts/{accountId}/{userId}/admin | Delete admin
*AccountsApi* | [**accounts_delete_user_from_account**](docs/AccountsApi.md#accounts_delete_user_from_account) | **DELETE** /accounts/{accountId}/{userId} | Delete user from account
*AccountsApi* | [**accounts_get_by_id**](docs/AccountsApi.md#accounts_get_by_id) | **GET** /admin/accounts/{id} | Get by id
*AccountsApi* | [**accounts_get_users_for_account**](docs/AccountsApi.md#accounts_get_users_for_account) | **GET** /accounts/{accountId}/users | Get users for account
*AccountsApi* | [**accounts_list_accounts**](docs/AccountsApi.md#accounts_list_accounts) | **GET** /admin/accounts | List accounts
*AccountsApi* | [**accounts_resend_invite**](docs/AccountsApi.md#accounts_resend_invite) | **POST** /accounts/{accountId}/{userId}/resendInvite | Resend invite
*AccountsApi* | [**accounts_set_as_admin**](docs/AccountsApi.md#accounts_set_as_admin) | **POST** /accounts/{accountId}/{userId}/admin | Set as admin
*AccountsApi* | [**accounts_update_account**](docs/AccountsApi.md#accounts_update_account) | **POST** /admin/accounts/{id}/update | Update account
*AccountsApi* | [**accounts_update_account_public_settings**](docs/AccountsApi.md#accounts_update_account_public_settings) | **POST** /accounts/{accountId}/update | Update account public settings
*AccountsApi* | [**accounts_update_user_details**](docs/AccountsApi.md#accounts_update_user_details) | **POST** /accounts/{accountId}/{userId}/updateuser | Update user details
*BuildsApi* | [**workflows_get**](docs/BuildsApi.md#workflows_get) | **GET** /builds/{id} | Get
*BuildsApi* | [**workflows_list**](docs/BuildsApi.md#workflows_list) | **GET** /workflow | List
*BuildsApi* | [**workflows_restart**](docs/BuildsApi.md#workflows_restart) | **GET** /builds/rebuild/{id} | Restart
*ClustersApi* | [**clusters_delete**](docs/ClustersApi.md#clusters_delete) | **DELETE** /clusters/{provider}/cluster/{id} | Delete
*ClustersApi* | [**clusters_list**](docs/ClustersApi.md#clusters_list) | **GET** /clusters | List
*CodefreshRegistryApi* | [**codefresh_registry_generate_cfcr_token**](docs/CodefreshRegistryApi.md#codefresh_registry_generate_cfcr_token) | **POST** /registry/auth/token | Generate cfcr token
*CodefreshRegistryApi* | [**registries_create**](docs/CodefreshRegistryApi.md#registries_create) | **POST** /registries | Create
*CodefreshRegistryApi* | [**registries_default_patch**](docs/CodefreshRegistryApi.md#registries_default_patch) | **PATCH** /registries/{registryId}/default | Patch default
*CodefreshRegistryApi* | [**registries_delete**](docs/CodefreshRegistryApi.md#registries_delete) | **DELETE** /registries/{registryId} | Delete
*CodefreshRegistryApi* | [**registries_list**](docs/CodefreshRegistryApi.md#registries_list) | **GET** /registries | List registries
*CodefreshRegistryApi* | [**registries_patch**](docs/CodefreshRegistryApi.md#registries_patch) | **PATCH** /registries/{registryId} | Patch
*CodefreshRegistryApi* | [**registries_test**](docs/CodefreshRegistryApi.md#registries_test) | **POST** /registries/test | Test
*CompositionsApi* | [**compositions_create**](docs/CompositionsApi.md#compositions_create) | **POST** /compositions | Create
*CompositionsApi* | [**compositions_delete**](docs/CompositionsApi.md#compositions_delete) | **DELETE** /compositions/{id} | Delete
*CompositionsApi* | [**compositions_duplicate**](docs/CompositionsApi.md#compositions_duplicate) | **POST** /compositions/{id}/duplicate | Duplicate
*CompositionsApi* | [**compositions_get**](docs/CompositionsApi.md#compositions_get) | **GET** /compositions/{id} | Get
*CompositionsApi* | [**compositions_launch**](docs/CompositionsApi.md#compositions_launch) | **POST** /compositions/{id}/run | Launch
*CompositionsApi* | [**compositions_list**](docs/CompositionsApi.md#compositions_list) | **GET** /compositions | List
*CompositionsApi* | [**compositions_patch**](docs/CompositionsApi.md#compositions_patch) | **PATCH** /compositions/{id} | Patch
*CompositionsApi* | [**compositions_update**](docs/CompositionsApi.md#compositions_update) | **PUT** /compositions/{id} | Update
*ContextsApi* | [**contexts_create**](docs/ContextsApi.md#contexts_create) | **POST** /contexts | Create
*ContextsApi* | [**contexts_default_patch**](docs/ContextsApi.md#contexts_default_patch) | **PATCH** /contexts/{name}/default | Patch
*ContextsApi* | [**contexts_delete**](docs/ContextsApi.md#contexts_delete) | **DELETE** /contexts/{name} | Delete
*ContextsApi* | [**contexts_get**](docs/ContextsApi.md#contexts_get) | **GET** /contexts/{name} | Get
*ContextsApi* | [**contexts_list**](docs/ContextsApi.md#contexts_list) | **GET** /contexts | List
*ContextsApi* | [**contexts_patch**](docs/ContextsApi.md#contexts_patch) | **PATCH** /contexts/{name} | Patch
*ContextsApi* | [**contexts_replace**](docs/ContextsApi.md#contexts_replace) | **PUT** /contexts/{name} | Replace
*EnvironmentsApi* | [**envs_get**](docs/EnvironmentsApi.md#envs_get) | **GET** /environments/{id} | Get
*EnvironmentsApi* | [**envs_list**](docs/EnvironmentsApi.md#envs_list) | **GET** /environments | List
*EnvironmentsApi* | [**envs_pause**](docs/EnvironmentsApi.md#envs_pause) | **GET** /environments/{id}/pause | Pause
*EnvironmentsApi* | [**envs_rename**](docs/EnvironmentsApi.md#envs_rename) | **GET** /environments/{id}/rename/{newName} | Rename
*EnvironmentsApi* | [**envs_start**](docs/EnvironmentsApi.md#envs_start) | **GET** /environments/{id}/start | Start
*EnvironmentsApi* | [**envs_status**](docs/EnvironmentsApi.md#envs_status) | **GET** /environments/{id}/status | Status
*EnvironmentsApi* | [**envs_stop**](docs/EnvironmentsApi.md#envs_stop) | **GET** /environments/{id}/stop | Stop
*EnvironmentsApi* | [**envs_terminate**](docs/EnvironmentsApi.md#envs_terminate) | **GET** /environments/{id}/terminate | Terminate
*EnvironmentsApi* | [**envs_terminate_all**](docs/EnvironmentsApi.md#envs_terminate_all) | **GET** /environments/all/terminate | Terminate all
*EnvironmentsApi* | [**envs_unpause**](docs/EnvironmentsApi.md#envs_unpause) | **GET** /environments/{id}/unpause | Unpause
*FeaturesApi* | [**features_account**](docs/FeaturesApi.md#features_account) | **GET** /features/{accountId} | Account
*HelmBoardsApi* | [**helm_boards_create**](docs/HelmBoardsApi.md#helm_boards_create) | **POST** /helm/boards | Create
*HelmBoardsApi* | [**helm_boards_delete**](docs/HelmBoardsApi.md#helm_boards_delete) | **DELETE** /helm/boards/{id} | Delete
*HelmBoardsApi* | [**helm_boards_delete_all**](docs/HelmBoardsApi.md#helm_boards_delete_all) | **DELETE** /helm/boards | Delete all
*HelmBoardsApi* | [**helm_boards_get**](docs/HelmBoardsApi.md#helm_boards_get) | **GET** /helm/boards/{id} | Get
*HelmBoardsApi* | [**helm_boards_get_by_name**](docs/HelmBoardsApi.md#helm_boards_get_by_name) | **GET** /helm/boards/name/{name} | Get by name
*HelmBoardsApi* | [**helm_boards_list**](docs/HelmBoardsApi.md#helm_boards_list) | **GET** /helm/boards | List
*HelmBoardsApi* | [**helm_boards_patch**](docs/HelmBoardsApi.md#helm_boards_patch) | **PATCH** /helm/boards/{id} | Patch
*HelmBoardsApi* | [**helm_boards_update**](docs/HelmBoardsApi.md#helm_boards_update) | **PUT** /helm/boards/{id} | Update
*HelmChartsApi* | [**helm_charts_install**](docs/HelmChartsApi.md#helm_charts_install) | **POST** /kubernetes/chart/install | Install
*HelmChartsApi* | [**helm_charts_promote**](docs/HelmChartsApi.md#helm_charts_promote) | **POST** /kubernetes/chart/promote | Promote
*HelmReleasesApi* | [**helm_releases_delete**](docs/HelmReleasesApi.md#helm_releases_delete) | **POST** /kubernetes/releases/{releaseName}/delete | Delete
*HelmReleasesApi* | [**helm_releases_test**](docs/HelmReleasesApi.md#helm_releases_test) | **POST** /kubernetes/releases/{releaseName}/test | Test
*HelmReposApi* | [**helm_repos_create**](docs/HelmReposApi.md#helm_repos_create) | **POST** /helm/repos | Create
*HelmReposApi* | [**helm_repos_delete**](docs/HelmReposApi.md#helm_repos_delete) | **DELETE** /helm/repos/{name} | Delete
*HelmReposApi* | [**helm_repos_get**](docs/HelmReposApi.md#helm_repos_get) | **GET** /helm/repos/{name} | Get
*HelmReposApi* | [**helm_repos_list**](docs/HelmReposApi.md#helm_repos_list) | **GET** /helm/repos | List
*HelmReposApi* | [**helm_repos_update**](docs/HelmReposApi.md#helm_repos_update) | **PUT** /helm/repos/{name} | Update
*HelmSectionsApi* | [**helm_sections_create**](docs/HelmSectionsApi.md#helm_sections_create) | **POST** /helm/boards/sections | Create
*HelmSectionsApi* | [**helm_sections_delete**](docs/HelmSectionsApi.md#helm_sections_delete) | **DELETE** /helm/boards/sections/{id} | Delete
*HelmSectionsApi* | [**helm_sections_delete_all**](docs/HelmSectionsApi.md#helm_sections_delete_all) | **DELETE** /helm/boards/{boardId}/sections | Delete all
*HelmSectionsApi* | [**helm_sections_get**](docs/HelmSectionsApi.md#helm_sections_get) | **GET** /helm/boards/sections/{id} | Get
*HelmSectionsApi* | [**helm_sections_get_by_name**](docs/HelmSectionsApi.md#helm_sections_get_by_name) | **GET** /helm/boards/{boardId}/sections/name/{name} | Get by name
*HelmSectionsApi* | [**helm_sections_list**](docs/HelmSectionsApi.md#helm_sections_list) | **GET** /helm/boards/{boardId}/sections | List
*HelmSectionsApi* | [**helm_sections_patch**](docs/HelmSectionsApi.md#helm_sections_patch) | **PATCH** /helm/boards/sections/{id} | Patch
*HelmSectionsApi* | [**helm_sections_reorder**](docs/HelmSectionsApi.md#helm_sections_reorder) | **POST** /helm/boards/sections/reorder | Reorder
*HelmSectionsApi* | [**helm_sections_update**](docs/HelmSectionsApi.md#helm_sections_update) | **PUT** /helm/boards/sections/{id} | Update
*ImagesApi* | [**images_add_from_external_source**](docs/ImagesApi.md#images_add_from_external_source) | **POST** /images/external | Add from external source
*ImagesApi* | [**images_delete_metadata**](docs/ImagesApi.md#images_delete_metadata) | **DELETE** /images/{dockerImageId}/metadata/{keyName} | Delete metadata
*ImagesApi* | [**images_get**](docs/ImagesApi.md#images_get) | **GET** /images/{id} | Get
*ImagesApi* | [**images_get_metadata**](docs/ImagesApi.md#images_get_metadata) | **GET** /images/{dockerImageId}/metadata | Get metadata
*ImagesApi* | [**images_get_tags**](docs/ImagesApi.md#images_get_tags) | **GET** /images/{id}/tags | Get tags
*ImagesApi* | [**images_list**](docs/ImagesApi.md#images_list) | **GET** /images | List
*ImagesApi* | [**images_tag**](docs/ImagesApi.md#images_tag) | **POST** /images/{id}/tag/{tag} | Tag
*ImagesApi* | [**images_untag**](docs/ImagesApi.md#images_untag) | **DELETE** /images/{id}/tag/{tag} | Untag
*ImagesApi* | [**images_upsert_metadata**](docs/ImagesApi.md#images_upsert_metadata) | **POST** /images/{dockerImageId}/metadata | Upsert metadata
*KubernetesApi* | [**kubernetes_generate_image_pull_secret**](docs/KubernetesApi.md#kubernetes_generate_image_pull_secret) | **POST** /kubernetes/secrets/imagePullSecret | Generate image pull secret
*PipelinesApi* | [**pipelines_create**](docs/PipelinesApi.md#pipelines_create) | **POST** /pipelines | Create
*PipelinesApi* | [**pipelines_delete**](docs/PipelinesApi.md#pipelines_delete) | **DELETE** /pipelines/{name} | Delete
*PipelinesApi* | [**pipelines_get**](docs/PipelinesApi.md#pipelines_get) | **GET** /pipelines/{name} | Get
*PipelinesApi* | [**pipelines_list**](docs/PipelinesApi.md#pipelines_list) | **GET** /pipelines | List
*PipelinesApi* | [**pipelines_replace**](docs/PipelinesApi.md#pipelines_replace) | **PUT** /pipelines/{name} | Replace
*PipelinesApi* | [**pipelines_run**](docs/PipelinesApi.md#pipelines_run) | **POST** /pipelines/run/{name} | Run
*PipelinesApi* | [**pipelines_validate_yaml**](docs/PipelinesApi.md#pipelines_validate_yaml) | **POST** /pipelines/yaml/validator | Validate yaml
*PipelinesApi* | [**runtime_launch**](docs/PipelinesApi.md#runtime_launch) | **POST** /runtime/testit | Launch
*ProgressApi* | [**progress_download**](docs/ProgressApi.md#progress_download) | **GET** /progress/download/{id} | Download
*ProgressApi* | [**progress_get**](docs/ProgressApi.md#progress_get) | **GET** /progress/{id} | Get
*ProgressApi* | [**progress_terminate**](docs/ProgressApi.md#progress_terminate) | **DELETE** /progress/{id} | Terminate
*ReposApi* | [**repos_create**](docs/ReposApi.md#repos_create) | **POST** /services | Create
*ReposApi* | [**repos_delete**](docs/ReposApi.md#repos_delete) | **DELETE** /services/{name} | Delete
*ReposApi* | [**repos_get**](docs/ReposApi.md#repos_get) | **GET** /services/{name} | Get
*ReposApi* | [**repos_get_settings**](docs/ReposApi.md#repos_get_settings) | **GET** /repos/settings/{repoOwner}/{repoName} | Get settings
*ReposApi* | [**repos_git_get_repo**](docs/ReposApi.md#repos_git_get_repo) | **GET** /repos/{owner}/{repo} | Get git repo
*ReposApi* | [**repos_git_list**](docs/ReposApi.md#repos_git_list) | **GET** /repos | List git repos (github, bitbucket, etc)
*ReposApi* | [**repos_list**](docs/ReposApi.md#repos_list) | **GET** /repos/existing | List
*RuntimeEnvironmentsApi* | [**runtime_envs_delete**](docs/RuntimeEnvironmentsApi.md#runtime_envs_delete) | **DELETE** /runtime-environments/{runtimeEnvironmentName} | Delete
*RuntimeEnvironmentsApi* | [**runtime_envs_get**](docs/RuntimeEnvironmentsApi.md#runtime_envs_get) | **GET** /runtime-environments/{runtimeEnvironmentName} | Get
*RuntimeEnvironmentsApi* | [**runtime_envs_list**](docs/RuntimeEnvironmentsApi.md#runtime_envs_list) | **GET** /runtime-environments | List
*RuntimeEnvironmentsApi* | [**runtime_envs_set_default**](docs/RuntimeEnvironmentsApi.md#runtime_envs_set_default) | **PUT** /runtime-environments/default/{runtimeEnvironmentName} | Set default
*RuntimeEnvironmentsApi* | [**runtime_envs_update**](docs/RuntimeEnvironmentsApi.md#runtime_envs_update) | **PUT** /runtime-environments/{runtimeEnvironmentName} | Update
*RuntimeEnvironmentsApi* | [**on_prem_runtime_envs_list**](docs/RuntimeEnvironmentsApi.md#on_prem_runtime_envs_list) | **GET** /admin/runtime-environments | List
*RuntimeEnvironmentsApi* | [**on_prem_runtime_envs_plan_get**](docs/RuntimeEnvironmentsApi.md#on_prem_runtime_envs_plan_get) | **GET** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Get
*RuntimeEnvironmentsAccountApi* | [**on_prem_runtime_envs_account_delete**](docs/RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_delete) | **DELETE** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | Delete for account
*RuntimeEnvironmentsAccountApi* | [**on_prem_runtime_envs_account_list**](docs/RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_list) | **GET** /admin/runtime-environments/account/{account} | Get by account
*RuntimeEnvironmentsAccountApi* | [**on_prem_runtime_envs_account_modify**](docs/RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_modify) | **PUT** /admin/runtime-environments/account/modify/{runtimeEnvironmentName} | Add to account
*RuntimeEnvironmentsAccountApi* | [**on_prem_runtime_envs_account_set_default**](docs/RuntimeEnvironmentsAccountApi.md#on_prem_runtime_envs_account_set_default) | **PUT** /admin/runtime-environments/account/default/{account}/{runtimeEnvironmentName} | Set default for account
*RuntimeEnvironmentsPlanApi* | [**on_prem_runtime_envs_plan_delete**](docs/RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_delete) | **DELETE** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Delete
*RuntimeEnvironmentsPlanApi* | [**on_prem_runtime_envs_plan_set_default**](docs/RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_set_default) | **PUT** /admin/runtime-environments/default/{plan}/{runtimeEnvironmentName} | Set default
*RuntimeEnvironmentsPlanApi* | [**on_prem_runtime_envs_plan_update**](docs/RuntimeEnvironmentsPlanApi.md#on_prem_runtime_envs_plan_update) | **PUT** /admin/runtime-environments/{plan}/{runtimeEnvironmentName} | Update
*RuntimeEnvironmentsSystemApi* | [**on_prem_runtime_envs_system_delete**](docs/RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_delete) | **DELETE** /admin/runtime-environments/{runtimeEnvironmentName} | Delete sys re
*RuntimeEnvironmentsSystemApi* | [**on_prem_runtime_envs_system_get**](docs/RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_get) | **GET** /admin/runtime-environments/{runtimeEnvironmentName} | Get sys re
*RuntimeEnvironmentsSystemApi* | [**on_prem_runtime_envs_system_update**](docs/RuntimeEnvironmentsSystemApi.md#on_prem_runtime_envs_system_update) | **PUT** /admin/runtime-environments/{runtimeEnvironmentName} | Update sys re
*TeamsApi* | [**teams_add_user**](docs/TeamsApi.md#teams_add_user) | **PUT** /team/{teamId}/{userId}/assignUserToTeam | Add user
*TeamsApi* | [**teams_create**](docs/TeamsApi.md#teams_create) | **POST** /team | Create
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /team | List
*TeamsApi* | [**teams_list_by_user**](docs/TeamsApi.md#teams_list_by_user) | **GET** /team/{userId}/findTeamsByUser | List by user
*TeamsApi* | [**teams_remove_user**](docs/TeamsApi.md#teams_remove_user) | **PUT** /team/{teamId}/{userId}/deleteUserFromTeam | Remove user
*TeamsApi* | [**teams_synchronize_client_with_group**](docs/TeamsApi.md#teams_synchronize_client_with_group) | **GET** /team/group/synchronize/name/{name}/type/{type} | Synchronize client with group
*TokensApi* | [**tokens_delete**](docs/TokensApi.md#tokens_delete) | **DELETE** /auth/key/{id} | Delete
*TokensApi* | [**tokens_generate**](docs/TokensApi.md#tokens_generate) | **POST** /auth/key | Generate
*TokensApi* | [**tokens_list**](docs/TokensApi.md#tokens_list) | **GET** /auth/keys | List
*TriggersApi* | [**triggers_create**](docs/TriggersApi.md#triggers_create) | **POST** /hermes/triggers/{event}/{pipeline} | Create
*TriggersApi* | [**triggers_delete**](docs/TriggersApi.md#triggers_delete) | **DELETE** /hermes/triggers/{event}/{pipeline} | Delete
*TriggersApi* | [**triggers_get_event_triggers**](docs/TriggersApi.md#triggers_get_event_triggers) | **GET** /hermes/triggers/event/{event} | Get event triggers
*TriggersApi* | [**triggers_get_pipeline_triggers**](docs/TriggersApi.md#triggers_get_pipeline_triggers) | **GET** /hermes/triggers/pipeline/{pipeline} | Get pipeline triggers
*TriggersApi* | [**triggers_list**](docs/TriggersApi.md#triggers_list) | **GET** /hermes/triggers | List
*TriggersEventsApi* | [**triggers_events_create**](docs/TriggersEventsApi.md#triggers_events_create) | **POST** /hermes/events | Create
*TriggersEventsApi* | [**triggers_events_delete**](docs/TriggersEventsApi.md#triggers_events_delete) | **DELETE** /hermes/events/{event}/{context} | Delete
*TriggersEventsApi* | [**triggers_events_get**](docs/TriggersEventsApi.md#triggers_events_get) | **GET** /hermes/events/{event} | Get
*TriggersEventsApi* | [**triggers_events_list**](docs/TriggersEventsApi.md#triggers_events_list) | **GET** /hermes/events | List
*TriggersTypesApi* | [**triggers_types_get**](docs/TriggersTypesApi.md#triggers_types_get) | **GET** /hermes/types/{type}/{kind} | Get
*TriggersTypesApi* | [**triggers_types_list**](docs/TriggersTypesApi.md#triggers_types_list) | **GET** /hermes/types | List
*ChartsApi* | [**charts_list**](docs/ChartsApi.md#charts_list) | **GET** /charts/{repo} | Get charts by repo


## Documentation For Models

 - [Abac](docs/Abac.md)
 - [AccountsaccountIdupdateNotifications](docs/AccountsaccountIdupdateNotifications.md)
 - [AccountsaccountIdupdateSlack](docs/AccountsaccountIdupdateSlack.md)
 - [AccountsaccountIdupdateWebhook](docs/AccountsaccountIdupdateWebhook.md)
 - [AdminaccountsaddpendinguserProvider](docs/AdminaccountsaddpendinguserProvider.md)
 - [ContextsSpec](docs/ContextsSpec.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject10](docs/InlineObject10.md)
 - [InlineObject11](docs/InlineObject11.md)
 - [InlineObject12](docs/InlineObject12.md)
 - [InlineObject13](docs/InlineObject13.md)
 - [InlineObject14](docs/InlineObject14.md)
 - [InlineObject15](docs/InlineObject15.md)
 - [InlineObject16](docs/InlineObject16.md)
 - [InlineObject17](docs/InlineObject17.md)
 - [InlineObject18](docs/InlineObject18.md)
 - [InlineObject19](docs/InlineObject19.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject20](docs/InlineObject20.md)
 - [InlineObject21](docs/InlineObject21.md)
 - [InlineObject22](docs/InlineObject22.md)
 - [InlineObject23](docs/InlineObject23.md)
 - [InlineObject24](docs/InlineObject24.md)
 - [InlineObject25](docs/InlineObject25.md)
 - [InlineObject26](docs/InlineObject26.md)
 - [InlineObject27](docs/InlineObject27.md)
 - [InlineObject28](docs/InlineObject28.md)
 - [InlineObject29](docs/InlineObject29.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject30](docs/InlineObject30.md)
 - [InlineObject31](docs/InlineObject31.md)
 - [InlineObject32](docs/InlineObject32.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [InlineObject7](docs/InlineObject7.md)
 - [InlineObject8](docs/InlineObject8.md)
 - [InlineObject9](docs/InlineObject9.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2004Spec](docs/InlineResponse2004Spec.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [PipelinesnameMetadata](docs/PipelinesnameMetadata.md)
 - [PipelinesnameSpec](docs/PipelinesnameSpec.md)
 - [PipelinesnameSpecVariables](docs/PipelinesnameSpecVariables.md)
 - [RequestBody](docs/RequestBody.md)
 - [RuntimetestitRepoData](docs/RuntimetestitRepoData.md)
 - [RuntimetestitRepoDataUrl](docs/RuntimetestitRepoDataUrl.md)
 - [ServicesServiceDetails](docs/ServicesServiceDetails.md)
 - [ServicesServiceDetailsScm](docs/ServicesServiceDetailsScm.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




