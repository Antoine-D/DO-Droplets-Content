Run:
    python SearchPages.py "search term" 

Can also specify arguments from the following:
	* -ppm
	  * Specifies the per-page maximum matches to report, for exampe -ppm 1 will only report one match per page
	* -ips
	  * specifies the file with the list of droplet's files to search 

Files were pulled from the following DigitalOcean droplets by IP:
	
	* 104.131.[0-255].[0-255]
	* 107.170.[0-255].[0-255]
	* 178.62.[0-255].[0-255]
	* 104.236.[0-255].[0-255]
	* 162.243.[0-255].[0-255]

The file pulled from each droplet is stored in a directory named by first two octets of its IP address 
(for example file pulled from **104.131.37.241** would be located at: **104.131/104.131.37.241**)

