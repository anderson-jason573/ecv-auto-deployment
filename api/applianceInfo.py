"""
***********************************************************

This module retrieves information on all appliances, and 
returns the json response.

***********************************************************
"""

def applianceINFO(orchIP, loginCookie):

    import requests
    import json
    import sys

    print('Retrieving appliance data from Orchestrator.')

# Surpress ssl certificate verifcation warnings

    requests.packages.urllib3.disable_warnings()

# Request for appliance info - all

    url = "https://{0}/gms/rest/appliance".format(orchIP)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers, cookies=loginCookie, verify=False)

    if response.status_code == 200:
        print('Appliance information retrieved successfully.')
    else:
        sys.exit('Retrieval of appliance information has failed.')

# Deserialize json from API call to 'json_response'

    json_response = json.loads(response.text)

    return json_response

"""
********************************************************************************
For Testing Only
********************************************************************************
"""

if __name__ == "__main__":

    print('\n ****************************************************************')
    print('\n    This module was ran directly. It is for testing only.')
    print('\n **************************************************************** \n')

    from login import OrchLogin
    orchIP = input("Orchestrator IP Address: ")
    user = input("username: ")
    password = input("password: ")

    loginCookie = OrchLogin(orchIP, user, password)

    info = applianceINFO(orchIP, loginCookie)

    print(info)

#end
