
def should_run(dist):
    """
    sample should_run. Determine, given dist, if this
    should run. Must return True for run to run.
    
    This is to give the postinstall script more leeway
    in determining when to run 
    """
    return 'develop' in dist.commands

def run(dist):
    """
    a sample post installation script
    
    it receives the instance of the command that runs it.
    dist is the setuptools.Distribution object, including all
    metadata for the package
    """
    print "****"
    print "**** hello, this is the post installation script"
    print "****"