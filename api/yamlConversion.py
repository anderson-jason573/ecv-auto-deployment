"""
***************************************************************************************

This module:

1) Reads a specified yaml file.
2) Finds the appliance name in the file, and place into the "name" and "tag" variables.
3) Takes the YAML configuration data and converts it to base64 format.
4) Returns the "name", "tag", and "data" variables from the function.

***************************************************************************************
"""

def readYAML(filename):
    import base64
    import yaml

    with open(filename, 'r') as file:
        dict = yaml.load(file, Loader=yaml.FullLoader)

# place hostname into "name" and "tag"

        name = (dict['applianceInfo']['hostname'])
        tag = (dict['applianceInfo']['hostname'])
        file.close()

# open and read yaml file as text into a string, so it can be converted to base64 encoding

        f = open(filename, "r")
        text = f.read()

# convert the string obatained from the yaml file to base64 encoding


        conversion = base64.b64encode(text.encode("utf-8"))

# decode base64 from bytes to string, to get rid of the " 'b' characters"

        data = conversion.decode()

        print('For ' + name +', YAML conversion to base64 completed.')

        return name, tag, data

def readTEST(path):
    import os
    import base64
    import yaml

    for entry in os.listdir(path):
        if entry.endswith('.yml'):
            filename = os.path.join(path, entry)
            with open(filename, 'r') as file:
                dict = yaml.load(file, Loader=yaml.FullLoader)

                # place hostname into "name" and "tag", to be used in API post later

                name = (dict['applianceInfo']['hostname'])
                tag = (dict['applianceInfo']['hostname'])
                file.close()

                # open and read yaml file as text into a string, so it can be converted to base64 encoding

                f = open(filename, "r")
                text = f.read()

                # convert the string obatained from the yaml file to base64 encoding

                conversion = base64.b64encode(text.encode("utf-8"))

                # decode base64 from bytes to string, to get rid of the " 'b' characters"

                data = conversion.decode()

                print('name: ' + name + ',' + ' tag: ' + tag + ' data: ' + data)
                print('For ' + name + ', YAML conversion to base64 completed.')

""" 
**********************************************************************************
For local testing Only
**********************************************************************************
"""

if __name__ == '__main__':

    print('\n ****************************************************************')
    print('\n    This module was ran directly. It is for testing only.')
    print('    It will read all .yml files within the specified directory')
    print('    No configurations will be uploaded to Orchestrator.')
    print('    This section can serve as an example for looping over many')
    print('    .yml files, in a \'main\' type function.')
    print('\n **************************************************************** \n')

    path = r'C:\Users\janderson.JANDERSON-W10\Box Sync\Jason Anderson\Sync\GitHub\lab-ecv-autoDeployment\lab-ecv-autoDeployment'
    readTEST(path)

"""
************************************************************ 
Example for 'main'

for entry in os.listdir(path):
            if entry.endswith('.yml'):
                filename = os.path.join(path, entry)
                result = api.readYAML(filename)
                print(result[0])
                print(result[1])
                print(result[2])
                print()
                
************************************************************
"""

#end
