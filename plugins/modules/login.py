# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

DOCUMENTATION = r'''
---
module: commvault.ansible.login
short_description: Login in to the Commcell with provided credentials or auth token.
description:
    - commvault.ansible.login can be used to login to Commcell using credentials or auth. token.
options:
 webserver_hostname:
  description:
  - Hostname of the Web Server.
  type: str
  required: true 
 webserver_username:
  description:
  - Webserver Username. 
  type: str
  required: false    
 webserver_password:
  description:
  - Webserver Password. 
  type: str
  required: false    
 auth_token:
  description:
  - A authentication token that can be used in place of webserver_username and webserver_password to login.
  type: str
  required: false
author:
- Commvault Systems Inc
'''

EXAMPLES = r'''
- name: Log in to the Commcell
  commvault.ansible.login:
    webserver_hostname: 'web_server_hostname' 
    webserver_username: 'user'
    webserver_password: 'password'
'''

RETURN = r'''
authtoken:
    description: The authentication token
    returned: On success
    type: str
    sample: QSDK value_of_token
'''

from ansible_collections.commvault.ansible.plugins.module_utils.cv_ansible_module import CVAnsibleModule
from ansible_collections.commvault.ansible.plugins.module_utils.login.pre_login import PreLogin


def main():
    """Main method for this module."""

    module_args = dict(
        webserver_hostname=dict(type=str, required=True),
        webserver_username=dict(type=str, required=False),
        webserver_password=dict(type=str, required=False),
        auth_token=dict(type=str, required=False)
    )

    # PERFORM PRE LOGIN STEPS
    pre_login = PreLogin()
    pre_login.clean_up()
    module = CVAnsibleModule(argument_spec=module_args)

    try:
        module.result['authtoken'] = module.commcell.auth_token
        module.result['changed'] = True

        module.exit_json(**module.result)

    except Exception as e:
        module.result['msg'] = str(e)
        module.fail_json(**module.result)


if __name__ == "__main__":
    main()
