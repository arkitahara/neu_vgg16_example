import os
import glob
from natsort import natsorted

def get_files(directory, extension='*.png'):
    """Fetch list of files with a given extension.
    Args:
        directory (string): path to directory to retrieve files
        extension (string): file extension of files to retrieve

    Returns:
        files (list): sorted list of files retrieved
    """
    
    files = glob.glob(os.path.join(directory, extension))
    return natsorted(files)