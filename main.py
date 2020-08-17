"""
********************************************************************
From the cli, this module will ask the user to input the following:
    1.) 'orchIP' - IP address of targeted Orchestrator
    2.) 'user' - username to login to targeted Orchestrator
    3.) 'password' - password to login to targeted Orchestrator
    4.) 'path' - path to directory, where YAML files are located 

This module will take the above user input and:
    1) login to specified Orchestrator.
    2) Read specified YAML configuration files and upload them
       to Orchestrator as preconfiguration files.
    3) Create necessary .iso files to enable cloudinit for ECV's.
********************************************************************
"""

import api
import os

# User defined input variables

orchIP = input("Orchestrator IP Address: ")
user = input("username: ")
password = input("password: ")

# path to directory of yaml preconfig files
# if files are located in current directory, you can uncomment and use 'path = os.getcwd()'
"""
path = os.getcwd()
"""
# to specify another path, input "<path>"

path = input("path: ")

# login to orchestrator and return session cookie

loginCookie = api.OrchLogin(orchIP, user, password)

# Read all YAML files in specified directory, and then return
# 'name', 'tag', and 'data' information

for entry in os.listdir(path):
    if entry.endswith('.yml'):
        filename = os.path.join(path, entry)
        result = api.readYAML(filename)

        # yamlConversion module will return 'name', 'tag' and 'data' in a tuple.  These values
        # can be called by using 'result[0], result[1], and result[2].  Those are used to
        # pass the 'name', 'tag' and 'data' values to the preconfigOrch module.

        upload = api.preconfigUpload(orchIP, loginCookie, result[0], result[1], result[2])

        # Create .iso files for cloudinit process

        isofile = api.spcustomCreate(result[0], result[1], path)

# end
