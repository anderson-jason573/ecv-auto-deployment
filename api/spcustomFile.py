"""
**********************************************************************

This module creates files to make iso files for ECV cloudinit boot.

**********************************************************************
"""

def spcustomCreate(name, tag, path):

    import os

# Create directory for specific appliance and its cloudinit file

    directory = os.path.join(path, name)
    try:
      os.mkdir(directory)
    except OSError:
      print("Creation of directory %s has failed" % directory)
    else:
      print("Successfully created directory %s" % directory)

# Create cloudinit file for specific appliance

    with open(os.path.join(directory, 'spcustom.yml'), 'w') as file:
    
        file.write("silverpeak_vxoa_init:\n")
        file.write("  config_vars:\n")
        file.write("      HOSTNAME: {0}\n".format(name))
        file.write("      ACCNAME: \"Silver Peak SE - Jason Anderson\"\n")
        file.write("      ACCKEY: \"95tzEHscBr7ctR2QcmNL2er9js8pr43q\"\n")
        file.write("      SYS_TAG: \"{0}\"\n".format(tag))
        file.write("\n")
        file.write("  pre_mgmtd_tasks:\n")
        file.write("    - \"configdb:/system/hostname,hostname,_$HOSTNAME$\"\n")
        file.write("    - \"configdb:/cn/tunneld/portal/config/registration/account,string,_$ACCNAME$\"\n")
        file.write("    - \"configdb:/cn/tunneld/portal/config/registration/key,string,_$ACCKEY$\"\n")
        file.write("    - \"configdb:/cn/tunneld/portal/config/registration/site,string,_$SYS_TAG$\"\n")
        file.write("\n")
        file.write("  post_mgmtd_tasks:\n")
        file.write("     - \"cli:en;conf t;ip name-server 1.1.1.1\"\n")
        file.write("     - \"cli:en;conf t;system auto-mac-configure enable\"\n")
        file.write("     - \"cli:en;conf t;write memory;reboot nonconfirm\"\n")
        file.write("# end\n")
        file.close()
        print("Succesfully created spcustom.yml created in %s" % directory)

if __name__ == '__main__':

    print('\n ****************************************************************')
    print('\n    This module was ran directly. It is for testing only.')
    print('\n **************************************************************** \n')

    name = '<appliance name>' # replace with appliance name #
    tag = '<appliance tag>' # replace with appliance tag #
    path = r'<path to YAML configuration files' # replace with path to YAML configuration files #
    spcustomCreate(name, tag, path)

#end
