#!/usr/bin/env python3

import json
import requests
import sys
import time


# Functions ------------------------------------------
def get_password(password_file):
    with open(password_file, 'r') as password_file:
        return password_file.read().strip()


def set_password(password_file, new_password):
    with open(password_file, 'w') as password_file:
        password_file.write(new_password)
# End of functions -----------------------------------

try:
    # Check if required parameters are set
    if len(sys.argv) < 5:
        print('Usage:')
        print('%s schema host name password-path')
        print('schema         - Either http or https')
        print('host           - Domain / Hostname / IP of master')
        print('name           - Name of agent')
        print('password-path  - Path to password file')
        exit(-1)

    # Initial variables set from command line
    schema = sys.argv[1]
    url = sys.argv[2]
    name = sys.argv[3]
    password_file = sys.argv[4]

    # URLs
    base_url = '%s://%s' % (schema, url)
    login_url = base_url + '/login-agent'

    # Attempts to login for 5 times, then exits itself if login has failed for 5 consecutive times.
    login_attempt = 0
    while login_attempt < 5:

        data = {"name": name, "password": get_password(password_file)}

        print('Logging in to master: ' + login_url)

        # Performs basic login
        res = requests.post(login_url, data=data)

        # Checks if our login request was accepted
        if res.status_code == 200:
            print('Agent has been connected.')

            # Resets login attempt
            login_attempt = 0

            # Updates password (random password)
            set_password(password_file, json.loads(res.text)['new_password'])

            # Program loop that receives command from the master
            while True:
                # No code yet ...

                # Sleeps for 1 second.
                time.sleep(1)

        print('Error: ' + json.loads(res.text)['msg'])

        # Increment login attempt
        login_attempt = login_attempt + 1

        # Sleeps for 5 seconds to reattempt login
        time.sleep(5)

except KeyboardInterrupt:
    print('')
    print('Now closing the agent...')
