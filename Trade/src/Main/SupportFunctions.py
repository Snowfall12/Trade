'''
Created on 8 nov. 2018

@author: loicb
'''

def install_needed_packages(Pkg_list):
    import subprocess
    
    for i in Pkg_list:
        try:
            import i
        
        except ImportError:
            subprocess.call(['pip','install',i])
    
    return "All packages have been successfully imported"

