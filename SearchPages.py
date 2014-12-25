import sys
import os
import Parsing
import Common

# Parse the arguments and fill into search_paramaters
search_paramaters = Common.SearchParamaters()
search_paramaters = Parsing.parse_labels(sys.argv)

if(len(search_paramaters.search_phrases) == 0):
    print("ERROR: Must include phrase to search for at the end of the run command")
    sys.exit()

ip_folders = list()

ip_file = open(search_paramaters.ips_filename, 'r')
for line in ip_file:
    ip_folders.append(line.strip());

occurence_count = 0

for first_two_quadrants in ip_folders:
    for third_quadrant in range(0, 255):
        for fourth_quadrant in range(0, 255):
            path_to_file = first_two_quadrants + '/' + first_two_quadrants + "." + str(third_quadrant) + "." + str(fourth_quadrant)
            if os.path.exists(path_to_file):
                enc = 'utf-8'
                webpage = open(path_to_file, 'r', encoding = enc)
                try:
                    found = False
                    for line in webpage:
                        for search_phrase in search_paramaters.search_phrases:
                            if search_phrase in line.lower():
                                occurence_count+=1
                                found = True
                                break
                        # If found, go onto next file
                        if found:
                            break

                except UnicodeDecodeError as ude:
                    None

print(occurence_count)