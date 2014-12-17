import sys
import common
import parsing


# Parse the arguments and fill into search_paramaters
search_paramaters = common.SearchParamaters()
search_paramaters = parsing.parse_labels(sys.argv)

print(search_paramaters.per_page_max)
print(search_paramaters.ips_filename)