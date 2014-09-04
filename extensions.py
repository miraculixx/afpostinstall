'''
Created on Sep 4, 2014

@author: patrick
'''
from setuptools.command.install import install as _install
import imp
import os
import sys
        
class PostInstaller(object):
    def __init__(self, dist=None):
        self.dist = dist
        
    """
    a post installer script for setup tools
    see http://stackoverflow.com/q/250038 for details
    """
    def get_install_dir(self):
        """
        return the installation directory. Technically this
        is the parent process' installation directory (e.g.
        pip)
        """
        # this must be run post-install, otherwise psutil might
        # note be available
        import psutil
        ppid = psutil.Process(os.getpid()).ppid()
        return psutil.Process(ppid).cwd() 
    
    def load_postinstall(self):
        #-- determine actual install dir
        self.install_dir = self.get_install_dir()
        # see if there is a post install, if so, load and run it
        try:
            file, path, descr = imp.find_module('postinstall', [self.install_dir])
            postinstaller = imp.load_module('postinstall', file, path, descr)
        except ImportError as e:
            # die nicely
            print "[ERROR] PostInstall failed, %s" % e
            return None
        else:
            return postinstaller
        
    def setup_django(self):
        """
        setup django, return settings for virtual env  
        """
        # see if we have a virtualenv, if so append to path
        if 'VIRTUAL_ENV' in os.environ:
            sys.path.append(get_python_lib())
            sys.path.append(postinstaller.get_install_dir())
            os.chdir(postinstaller.get_install_dir())
        return __import__('settings')
    
        
    def run(self):
        """
        run the installer and post installation script
        
        This will look for a postinstall.py in the installation
        directory, and if it exists will execute it.
        
        if you only want to run on install, set on = ['install']
        if you want to run always, set on = ['egg_info']
        """
        postinstaller = self.load_postinstall()
        if postinstaller and postinstaller.should_run(self.dist):
            postinstaller.run(self)