Analyzing Files Scraped From a Specified Set of IP Addresses.
=================

To use:

  1. Edit the [downloadAll.sh](downloadAll.sh) with the first two quadrants of the set of IPs you want to scrape. 

  2. Run the script (will take a long time, may want to run with nohup and in the background). Repeat 1 and 2 for all the sets of ips you wish to scrape.

  3. Edit [ips.txt](ips.txt) with the sets of IPs you scraped.
  
  4. You can now run: 
    1. ```python SearchPages.py "search term" -ips ips.txt``` to get the number of scraped pages containing "search term".    
    2. ```python SimilarPages.py -ips ips.txt``` to get a report on the most common pages scraped.
  
For my experiment [available here](http://antoinedahan.com/blog/ScrapingDigitalOceanDroplets), the following files were pulled from the following DigitalOcean droplets by IP:
	
	* 104.131.[0-255].[0-255]
	* 107.170.[0-255].[0-255]
	* 178.62.[0-255].[0-255]
	* 104.236.[0-255].[0-255]
	* 162.243.[0-255].[0-255]
