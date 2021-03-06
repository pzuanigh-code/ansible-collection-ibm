#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.19.0
    - Terraform v0.12.20

options:
    private_vlan_id:
        description:
            - Private VLAN ID
        required: False
        type: str
    force_delete_storage:
        description:
            - Force the removal of a cluster and its persistent storage. Deleted data cannot be recovered
        required: False
        type: bool
        default: False
    labels:
        description:
            - list of labels to the default worker pool
        required: False
        type: dict
        elements: str
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    name:
        description:
            - (Required for new resource) The cluster name
        required: True
        type: str
    public_vlan_id:
        description:
            - Public VLAN ID
        required: False
        type: str
    entitlement:
        description:
            - Entitlement option reduces additional OCP Licence cost in Openshift Clusters
        required: False
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    tags:
        description:
            - Tags for the resource
        required: False
        type: list
        elements: str
    kms_config:
        description:
            - Enables KMS on a given cluster
        required: False
        type: list
        elements: dict
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    hardware:
        description:
            - (Required for new resource) Hardware type
        required: True
        type: str
    machine_type:
        description:
            - Machine type
        required: False
        type: str
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    update_all_workers:
        description:
            - Updates all the woker nodes if sets to true
        required: False
        type: bool
        default: False
    no_subnet:
        description:
            - Boolean value set to true when subnet creation is not required.
        required: False
        type: bool
        default: False
    subnet_id:
        description:
            - List of subnet IDs
        required: False
        type: list
        elements: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: True
        type: str
    wait_for_worker_update:
        description:
            - Wait for worker node to update during kube version update.
        required: False
        type: bool
        default: True
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    disk_encryption:
        description:
            - disc encryption done, if set to true.
        required: False
        type: bool
        default: True
    kube_version:
        description:
            - Kubernetes version info
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('name', 'str'),
    ('hardware', 'str'),
    ('datacenter', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'private_vlan_id',
    'force_delete_storage',
    'labels',
    'private_service_endpoint',
    'name',
    'public_vlan_id',
    'entitlement',
    'webhook',
    'tags',
    'kms_config',
    'workers_info',
    'hardware',
    'machine_type',
    'gateway_enabled',
    'update_all_workers',
    'no_subnet',
    'subnet_id',
    'resource_group_id',
    'datacenter',
    'wait_for_worker_update',
    'public_service_endpoint',
    'default_pool_size',
    'disk_encryption',
    'kube_version',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'cluster_name_id',
    'alb_type',
    'region',
    'name',
    'resource_group_id',
    'list_bounded_services',
    'org_guid',
    'space_guid',
    'account_guid',
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    private_vlan_id=dict(
        required=False,
        type='str'),
    force_delete_storage=dict(
        required=False,
        type='bool'),
    labels=dict(
        required=False,
        elements='',
        type='dict'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    name=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='str'),
    entitlement=dict(
        required=False,
        type='str'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    kms_config=dict(
        required=False,
        elements='',
        type='list'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    hardware=dict(
        required=False,
        type='str'),
    machine_type=dict(
        required=False,
        type='str'),
    gateway_enabled=dict(
        required=False,
        type='bool'),
    update_all_workers=dict(
        required=False,
        type='bool'),
    no_subnet=dict(
        required=False,
        type='bool'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
    resource_group_id=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    wait_for_worker_update=dict(
        required=False,
        type='bool'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    default_pool_size=dict(
        required=False,
        type='int'),
    disk_encryption=dict(
        required=False,
        type='bool'),
    kube_version=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result_ds = ibmcloud_terraform(
        resource_type='ibm_container_cluster',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.19.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_container_cluster',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.19.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
