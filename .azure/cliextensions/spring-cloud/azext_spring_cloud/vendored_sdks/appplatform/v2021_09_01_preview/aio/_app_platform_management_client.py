# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AppPlatformManagementClientConfiguration
from .operations import ServicesOperations
from .operations import ConfigServersOperations
from .operations import MonitoringSettingsOperations
from .operations import AppsOperations
from .operations import BindingsOperations
from .operations import StoragesOperations
from .operations import CertificatesOperations
from .operations import CustomDomainsOperations
from .operations import DeploymentsOperations
from .operations import Operations
from .operations import RuntimeVersionsOperations
from .operations import SkusOperations
from .. import models


class AppPlatformManagementClient(object):
    """REST API for Azure Spring Cloud.

    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.ServicesOperations
    :ivar config_servers: ConfigServersOperations operations
    :vartype config_servers: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.ConfigServersOperations
    :ivar monitoring_settings: MonitoringSettingsOperations operations
    :vartype monitoring_settings: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.MonitoringSettingsOperations
    :ivar apps: AppsOperations operations
    :vartype apps: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.AppsOperations
    :ivar bindings: BindingsOperations operations
    :vartype bindings: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.BindingsOperations
    :ivar storages: StoragesOperations operations
    :vartype storages: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.StoragesOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.CertificatesOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.CustomDomainsOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.Operations
    :ivar runtime_versions: RuntimeVersionsOperations operations
    :vartype runtime_versions: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.RuntimeVersionsOperations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.appplatform.v2021_09_01_preview.aio.operations.SkusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AppPlatformManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.services = ServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.config_servers = ConfigServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitoring_settings = MonitoringSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.bindings = BindingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storages = StoragesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.runtime_versions = RuntimeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AppPlatformManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
