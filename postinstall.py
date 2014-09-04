

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