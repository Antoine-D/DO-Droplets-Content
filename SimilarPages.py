import sys
import os
import Parsing
import Common

# Parse the arguments and fill into search_paramaters
search_paramaters = Common.SearchParamaters()
search_paramaters = Parsing.parse_labels(sys.argv)

ip_folders = list()

ip_file = open(search_paramaters.ips_filename, 'r')
for line in ip_file:
    ip_folders.append(line.strip());

pages_content = list()
for first_two_quadrants in ip_folders:
    for third_quadrant in range(0, 255):
        for fourth_quadrant in range(0, 255):
            path_to_file = first_two_quadrants + '/' + first_two_quadrants + "." + str(third_quadrant) + "." + str(fourth_quadrant)
            if os.path.exists(path_to_file):
                enc = 'utf-8'
                with open(path_to_file, 'r', encoding = enc) as webpage:
                    try:
                        webpage_content = webpage.read()
                        whitespace_free_version = webpage_content.replace(" ", "")
                        if whitespace_free_version != "":
                            found_match = False
                            for page in pages_content:
                                if(page["content"] == webpage_content):
                                    page["occurences"] += 1
                                    found_match = True
                                    break
                            if not found_match:
                                pages_content.append({"content": webpage_content, "occurences": 1})
                    except UnicodeDecodeError as ude:
                        None

sorted_page_contents = sorted(pages_content, key=lambda k: k['occurences'])

rank = 1
for i in reversed(sorted_page_contents):
    if rank > 300:
        break
    print('>>> Rank: %d \t Occurences: %d' % (rank, i['occurences']))
    print(str(i['content']))

    rank+=1



