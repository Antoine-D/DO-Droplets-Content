##
 # File for functions and globals relating to physically parsing input 
 # (the input of the command line or of the .fasta file input)
 #
##

import sys
import Common


def parse_labels(system_arguments):
    # Storage for values parsed from the system arguments
    search_params = Common.SearchParamaters()

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

    if((("-ips" in system_arguments) and (len(system_arguments) - 2) == system_arguments.index("-ips")) or (("-ppm" in system_arguments) and (len(system_arguments) - 2) == system_arguments.index("-ppm")) or (len(system_arguments) == 1)):
        print("ERROR: Must include phrase to search for at the end of the run command")
        sys.exit()

    #Set the last of the run command to be the search phrase
    search_params.search_phrase = system_arguments[len(system_arguments) - 1]

    # Make sure the file of ips provided (it is required so terminate if not provided)
    if(search_params.ips_filename == ""):
        print("ERROR: Must specify file of ip addresses: '-ips filename'")
        sys.exit()

    return search_params