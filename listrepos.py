import pprint
import requests
import argparse
import json

# For readability of jsons during testing
# https://docs.python.org/3/library/pprint.html
pp = pprint.PrettyPrinter(indent=4)


endpoint = "https://api.github.com/users/USERNAME/repos"


# Parse the command line arguments - referenced from the link below
# https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1
parser = argparse.ArgumentParser(description='Please supply a user name by adding a "--user=<your-user-name>" flag!')
parser.add_argument("--user")
args = parser.parse_args()
user = args.user

# Check if the string is empty
# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
if not user:
    print "Please re-run this program & provide a valid username"
    # Exit if no user provided
    exit(0)
else:

    print "User: " +user
    endpoint = endpoint.replace("USERNAME",user)

    # Adding the below request parameters from API spec here
    # https://developer.github.com/v3/repos/#list-user-repositories
    data = { 'type':'all','sort':'updated','type':'desc'}
    print "Posting to endpoint: " +endpoint
    response = requests.get(endpoint,data)

    # Using this stackoverflow article as a guide to get json to list of repos
    # https://stackoverflow.com/a/34479722
    response_parsed = json.loads(response.text)

    # Used the pretty-printed json to inspect the response body visually
    # during development/testing to extract the needed json fields
    #pp.pprint(response_parsed)
    #print "Response: " +response.text

    #print response_parsed

    # Commentted this out, but this was code I used to get a better look at the json
    # and the values I could extract to solve the problem
    # Here are the docs for reference:
    # https://www.geeksforgeeks.org/type-isinstance-python/
    # https://www.geeksforgeeks.org/python-string-length-len/
    #print len(response_parsed)
    #print type(response_parsed)


    print "Repo name/url\n"
    for each_repo in response_parsed:
        print "" +each_repo['name'] +"/" +each_repo['url']
    print "\nDone"
