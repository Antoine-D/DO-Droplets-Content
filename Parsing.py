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

    # Read in the name of the file of ips (required)
    if("-ips" in system_arguments):
        ips_filename = system_arguments.index("-ips")
        if(ips_filename+1 < len(system_arguments)):
            search_params.ips_filename = str(system_arguments[ips_filename+1])

    #Set the last of the run command to be the search phrase
    if((("-ips" not in system_arguments) or (len(system_arguments) - 2) != system_arguments.index("-ips")) and (len(system_arguments) > 1)):
        search_params.search_phrases = system_arguments[len(system_arguments) - 1].lower().split("_/_")

    # Make sure the file of ips provided (it is required so terminate if not provided)
    if(search_params.ips_filename == ""):
        print("ERROR: Must specify file of ip addresses: '-ips filename'")
        sys.exit()

    return search_params