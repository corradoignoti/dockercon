#! env python3

# dockercon is an utility to switch docker contexts faster.
# Copyright 2022 Corrado Ignoti.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# 	http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import os

def create_context(cont_name, cont_stack, cont_host) -> bool:
    """Create a new docker context"""
    cmd_ret_code = 0
    try:
        cmd_ret_code = os.system(f"docker context create {cont_name} --default-stack-orchestrator={cont_stack} --docker host={cont_host}")
    except:
        return False
    else:
        if cmd_ret_code == 0:
            return True
        else:
            return False

def delete_context(cont_name):
    """Delete a docker context"""
    cmd_ret_code = 0
    try:
        cmd_ret_code = os.system(f"docker context rm {cont_name}")
    except:
        return False
    else:
        if cmd_ret_code == 0:
            return True
        else:
            return False

def set_context(context_name) -> bool:
    """Set the current docker context"""
    cmd_ret_code = 0
    try:
        cmd_ret_code = os.system(f"docker context use {context_name}")
    except:
        return False
    else:
        if cmd_ret_code == 0:
            return True
        else:
            return False

def list_context():
    """List all docker context"""
    cmd_ret_code = 0
    try:
        cmd_ret_code = os.system("docker context ls")
    except:
        return False
    else:
        if cmd_ret_code == 0:
            return True
        else:
            return False

#
# main
#

# Parse command line
parser = parser = argparse.ArgumentParser(description=" dockercon is a tool to switch between docker contexts faster.")
parser.add_argument("name", type=str, help="Switch to context '<NAME>'", nargs="?", default=None, metavar='<NAME>')
parser.add_argument("-d", type=str, help="delete context <NAME>", nargs=1, required=False, metavar='<NAME>')
parser.add_argument("-a", type=str, help="add context <NAME>", nargs=1, required=False, metavar='<NAME>')
parser.add_argument("--host", type=str, help="<HOST> to use with a new context", nargs=1, required=False, metavar='<HOST>')
parser.add_argument("--stack", type=str, help="orchestrator <STACK> to use with a new context", nargs=1, required=False, metavar='<STACK>')
args = parser.parse_args()


if args.a is not None:
    host = None
    stack = None
    name = args.a[0]
    if args.host is not None:
        host = args.host[0]
    else:
        print ("Please specify a <HOST> for the context")
        sys.exit(256)
    if args.stack is not None:
        stack = args.stack[0]
    else:
        print ("Please specify a <STACK> for the context")
        sys.exit(256)
    if create_context(name, stack, host):
        sys.exit(0)
    else:
        print ("Couldn't create context, sorry")
        sys.exit(256)

if args.d is not None:
    if delete_context(args.d[0]):
        print ("context deleted")
        sys.exit(0)
    else:
        sys.exit(256)

if args.name is None:
    list_context()
    sys.exit(0)
else:
    if set_context(args.name):
        print ("is now the dafult context")
        sys.exit(0)
    else:
        sys.exit(256)