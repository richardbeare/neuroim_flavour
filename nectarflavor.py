from fabric.api import *
from fabric.contrib.files import *

from cloudbio.flavor import Flavor

from cloudbio.custom.shared import (_fetch_and_unpack)

class NectarFlavor(Flavor):
    """A VM flavor for running Boinc
    """
    def __init__(self, env):
        Flavor.__init__(self,env)
        self.name = "NeCTAR Flavor"

    def rewrite_config_items(self, name, packages):
        if name == 'packages':
          packages += [ 'nfs-common' ]
        # for package in packages:
        #   env.logger.info("Selected: "+name+" "+package)
        return packages

    def post_install(self):
        env.logger.info("Starting post-install")
        pass

env.flavor = NectarFlavor(env)
