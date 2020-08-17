"""
***************************************************************

This module initializes the 'api' package, when it is imported.
It imports all of the functions from the modules in the api 
package, so they can be called by using 'api.<function>'.

***************************************************************
"""

from .login import OrchLogin
from .yamlConversion import readYAML
from .preconfigOrch import preconfigUpload
from .spcustomFile import spcustomCreate
from .applianceInfo import applianceINFO

#end
