##
 # File for functions and globals relating to physically parsing input 
 # (the input of the command line or of the .fasta file input)
 #
##

import sys
import common


def parse_labels(system_arguments):
    # Storage for values parsed from the system arguments
    search_params = common.SearchParamaters()

    # Read in the per page max for number of matches length (if provided)
    if("-ppm" in system_arguments):
        ppm_index = system_arguments.index("-ppm")
        if((ppm_index+1 < len(system_arguments)) and (system_arguments[ppm_index+1].isdigit())):
            search_params.per_page_max = int(system_arguments[ppm_index+1])

    # Read in the name of the file of ips (required)
    if("-ips" in system_arguments):
        ips_filename = system_arguments.index("-ips")
        if(ips_filename+1 < len(system_arguments)):
            search_params.ips_filename = str(system_arguments[ips_filename+1])

    # Make sure the file of ips provided (it is required so terminate if not provided)
    if(search_params.ips_filename == ""):
        print("ERROR: Must specify file of ip addresses: '-ips filename'")
        sys.exit()

    return search_params