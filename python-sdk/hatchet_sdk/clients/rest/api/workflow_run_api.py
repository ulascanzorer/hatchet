# coding: utf-8

"""
    Hatchet API

    The Hatchet API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field
from typing import Optional
from typing_extensions import Annotated
from hatchet_sdk.clients.rest.models.trigger_workflow_run_request import TriggerWorkflowRunRequest
from hatchet_sdk.clients.rest.models.workflow_run import WorkflowRun

from hatchet_sdk.clients.rest.api_client import ApiClient, RequestSerialized
from hatchet_sdk.clients.rest.api_response import ApiResponse
from hatchet_sdk.clients.rest.rest import RESTResponseType


class WorkflowRunApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def workflow_run_create(
        self,
        workflow: Annotated[str, Field(min_length=36, strict=True, max_length=36, description="The workflow id")],
        trigger_workflow_run_request: Annotated[TriggerWorkflowRunRequest, Field(description="The input to the workflow run")],
        version: Annotated[Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(description="The workflow version. If not supplied, the latest version is fetched.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> WorkflowRun:
        """Trigger workflow run

        Trigger a new workflow run for a tenant

        :param workflow: The workflow id (required)
        :type workflow: str
        :param trigger_workflow_run_request: The input to the workflow run (required)
        :type trigger_workflow_run_request: TriggerWorkflowRunRequest
        :param version: The workflow version. If not supplied, the latest version is fetched.
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._workflow_run_create_serialize(
            workflow=workflow,
            trigger_workflow_run_request=trigger_workflow_run_request,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkflowRun",
            '400': "APIErrors",
            '403': "APIErrors",
            '404': "APIErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def workflow_run_create_with_http_info(
        self,
        workflow: Annotated[str, Field(min_length=36, strict=True, max_length=36, description="The workflow id")],
        trigger_workflow_run_request: Annotated[TriggerWorkflowRunRequest, Field(description="The input to the workflow run")],
        version: Annotated[Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(description="The workflow version. If not supplied, the latest version is fetched.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[WorkflowRun]:
        """Trigger workflow run

        Trigger a new workflow run for a tenant

        :param workflow: The workflow id (required)
        :type workflow: str
        :param trigger_workflow_run_request: The input to the workflow run (required)
        :type trigger_workflow_run_request: TriggerWorkflowRunRequest
        :param version: The workflow version. If not supplied, the latest version is fetched.
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._workflow_run_create_serialize(
            workflow=workflow,
            trigger_workflow_run_request=trigger_workflow_run_request,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkflowRun",
            '400': "APIErrors",
            '403': "APIErrors",
            '404': "APIErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def workflow_run_create_without_preload_content(
        self,
        workflow: Annotated[str, Field(min_length=36, strict=True, max_length=36, description="The workflow id")],
        trigger_workflow_run_request: Annotated[TriggerWorkflowRunRequest, Field(description="The input to the workflow run")],
        version: Annotated[Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]], Field(description="The workflow version. If not supplied, the latest version is fetched.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Trigger workflow run

        Trigger a new workflow run for a tenant

        :param workflow: The workflow id (required)
        :type workflow: str
        :param trigger_workflow_run_request: The input to the workflow run (required)
        :type trigger_workflow_run_request: TriggerWorkflowRunRequest
        :param version: The workflow version. If not supplied, the latest version is fetched.
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._workflow_run_create_serialize(
            workflow=workflow,
            trigger_workflow_run_request=trigger_workflow_run_request,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "WorkflowRun",
            '400': "APIErrors",
            '403': "APIErrors",
            '404': "APIErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _workflow_run_create_serialize(
        self,
        workflow,
        trigger_workflow_run_request,
        version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if workflow is not None:
            _path_params['workflow'] = workflow
        # process the query parameters
        if version is not None:
            
            _query_params.append(('version', version))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if trigger_workflow_run_request is not None:
            _body_params = trigger_workflow_run_request


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'cookieAuth', 
            'bearerAuth'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v1/workflows/{workflow}/trigger',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

