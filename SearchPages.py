import sys
import os
import Parsing
import Common


# Parse the arguments and fill into search_paramaters
search_paramaters = Common.SearchParamaters()
search_paramaters = Parsing.parse_labels(sys.argv)

print(search_paramaters.per_page_max)
print(search_paramaters.ips_filename)

ip_folders = list()

ip_file = open(search_paramaters.ips_filename, 'r')
for line in ip_file:
    ip_folders.append(line.strip());

for first_two_quadrants in ip_folders:
    for third_quadrant in range(0, 255):
        for fourth_quadrant in range(0, 255):
            path_to_file = first_two_quadrants + '/' + first_two_quadrants + "." + str(third_quadrant) + "." + str(fourth_quadrant)
            if os.path.exists(path_to_file):
                webpage = open(path_to_file, 'r')
                try: 
                    for line in webpage:
                        if search_paramaters.search_phrase in line:
                            print(path_to_file)
                except UnicodeDecodeError as ude:
                    c = 6 #do nothin
                
print(ip_folders)