#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_storage_block
short_description: Configure IBM Cloud 'ibm_storage_block' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_storage_block' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.5.3
    - Terraform v0.12.20

options:
    allowed_virtual_guest_ids:
        description:
            - List of allowed virtual guest IDs
        required: False
        type: list
        elements: int
    notes:
        description:
            - Additional note info
        required: False
        type: str
    allowed_hardware_ids:
        description:
            - List of allowe hardware IDs
        required: False
        type: list
        elements: int
    allowed_ip_addresses:
        description:
            - Allowed IP addresses
        required: False
        type: list
        elements: str
    type:
        description:
            - (Required for new resource) Storage block type
        required: False
        type: str
    datacenter:
        description:
            - (Required for new resource) Datacenter name
        required: False
        type: str
    iops:
        description:
            - (Required for new resource) IOPS value required
        required: False
        type: float
    hostname:
        description:
            - Hostname
        required: False
        type: str
    hourly_billing:
        description:
            - Billing done hourly, if set to true
        required: False
        type: bool
        default: False
    target_address:
        description:
            - List of target Addresses
        required: False
        type: list
        elements: str
    capacity:
        description:
            - (Required for new resource) Storage block size
        required: False
        type: int
    os_format_type:
        description:
            - (Required for new resource) OS formatr type
        required: False
        type: str
    allowed_virtual_guest_info:
        description:
            - None
        required: False
        type: list
        elements: dict
    tags:
        description:
            - List of tags associated with the resource
        required: False
        type: list
        elements: str
    volumename:
        description:
            - Volume name
        required: False
        type: str
    allowed_hardware_info:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    snapshot_capacity:
        description:
            - Snapshot capacity in GB
        required: False
        type: int
    allowed_host_info:
        description:
            - None
        required: False
        type: list
        elements: dict
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance
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
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
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
    ('type', 'str'),
    ('datacenter', 'str'),
    ('iops', 'float'),
    ('capacity', 'int'),
    ('os_format_type', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'allowed_virtual_guest_ids',
    'notes',
    'allowed_hardware_ids',
    'allowed_ip_addresses',
    'type',
    'datacenter',
    'iops',
    'hostname',
    'hourly_billing',
    'target_address',
    'capacity',
    'os_format_type',
    'allowed_virtual_guest_info',
    'tags',
    'volumename',
    'allowed_hardware_info',
    'resource_name',
    'snapshot_capacity',
    'allowed_host_info',
    'resource_controller_url',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    allowed_virtual_guest_ids=dict(
        required=False,
        elements='',
        type='list'),
    notes=dict(
        required=False,
        type='str'),
    allowed_hardware_ids=dict(
        required=False,
        elements='',
        type='list'),
    allowed_ip_addresses=dict(
        required=False,
        elements='',
        type='list'),
    type=dict(
        required=False,
        type='str'),
    datacenter=dict(
        required=False,
        type='str'),
    iops=dict(
        required=False,
        type='float'),
    hostname=dict(
        required=False,
        type='str'),
    hourly_billing=dict(
        default=False,
        type='bool'),
    target_address=dict(
        required=False,
        elements='',
        type='list'),
    capacity=dict(
        required=False,
        type='int'),
    os_format_type=dict(
        required=False,
        type='str'),
    allowed_virtual_guest_info=dict(
        required=False,
        elements='',
        type='list'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    volumename=dict(
        required=False,
        type='str'),
    allowed_hardware_info=dict(
        required=False,
        elements='',
        type='list'),
    resource_name=dict(
        required=False,
        type='str'),
    snapshot_capacity=dict(
        required=False,
        type='int'),
    allowed_host_info=dict(
        required=False,
        elements='',
        type='list'),
    resource_controller_url=dict(
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
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
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

    result = ibmcloud_terraform(
        resource_type='ibm_storage_block',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.5.3',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()