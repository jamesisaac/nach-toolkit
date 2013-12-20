"""
An example script which can be run locally to automatically update a
tracker logging number of Instagram followers
"""
import json
import re
import urllib2

# Your instagram username
instagram = ''
# Your NAch API key
nach_key = ''
# Your NAch tracker ID
nach_tracker = 1

def get_instagram_count():
    """Find the follower count via a regex query"""
    response = urllib2.urlopen('http://instagram.com/%s' % instagram).read()
    matchObj = re.match( r'.*"followed_by":(\d+),.*', response, re.S )
    if matchObj:
        count = matchObj.group(1)
        print 'Follower count: ' + count
        return count
    else:
        print "ERROR: No regex match"

def save_reading(count):
    """POST the reading to NAch via the API"""
    url = 'https://nachapp.com/api/trackers/%s/measures?_key=%s' % (nach_tracker, nach_key)
    print 'Launching ' + url
    
    # Create a POST request
    values = { 'value': count }
    req = urllib2.Request(url, json.dumps(values))
    
    # Send to the server and print the response
    response = urllib2.urlopen(req)
    print 'Response: ' + response.read()
        
def main():    
    count = get_instagram_count()
    if count:
        save_reading(count)

if __name__ == '__main__':
    main()