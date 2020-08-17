"""
************************************************************************

This module logs in to Orchestrator and returns the session 
cookie, for future API calls.

************************************************************************
"""

def OrchLogin(orchIP, user, password):
    import requests
    import sys

# Disable ssl inspection

    requests.packages.urllib3.disable_warnings()

# API call to login

    url = "https://{0}/gms/rest/authentication/login".format(orchIP)
    payload = "{{\r\n  \"user\": \"{0}\",\r\n  \"password\": \"{1}\",\r\n  \"token\": \"\",\r\n  \"loginType\": 0\r\n}}".format(user, password)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        print('Logged into Orchestrator successfully.')
    else:
        sys.exit('Failed to login to Orchestrator.')

# store login cookie, from API call, in "orchCookie" and return for future API calls

    orchCookie = response.cookies
    return(orchCookie)

#end
