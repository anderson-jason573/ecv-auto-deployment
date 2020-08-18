# ecv-auto-deployment

This module will aid in the provisioning of a Silver Peak EdgeConnect virtual machine (EC-V), 
by automating many of the manual processes necessary to deploy the VM. The module will use the 
modules defined in the 'silverpeak-api-pkg' package.  Several of those modules are 
included here, in the 'api' package.

The module will read one or more YAML configuration files, and upload them to the 
designated orchestrator for preconfiguration.  It will also create an
'spcustom.yml' file to facilitate cloudinit, for each corresponding appliance
designated in their respective YAML configuration file.
