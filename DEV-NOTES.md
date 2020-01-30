# Jonkkins
A copycat of Jenkins. Will be written in python.

# NOTE
```
"""
Things to do:
  Reference: https://jwcrypto.readthedocs.io/en/latest/jwt.html

-- On the front side:
    - Once we receive the valid login jwt, we must store it somewhere.
    - And then, on every request we made, put the jwt on Authorization: Bearer <jwt>

-- Lastly,
    - Perform a check on header. It'll be in the middleware of every application that
      requires logged-in user.
    - Once the claim are determined to be correct, we can just use the data written here.
      No need to get the data from database, since it is signed, then it is less likely
      to be manipulated
    - We can consider adding another layer (encryption), thus, making it JWE (Json Web
      Token Encrypted)
"""
```

## Initial Structure
Project will consist of modules `modules/{module}`. As of the
moment, the project will have one repository for now. Maybe we'll
have more than one repository. Let's see.


## Note to chosen contributors
Please feel free to make a push. Better if you make your own branch first.
then do your own experiments that we have discussed recently.


### Important checklist of contributors atm:
 - [ ] NGINX -> ASGI -> Flask Stack, research and implementation
 - [x] Auto source code update when you make some changes in the code
       without rebuilding (research and implementation)
 - [ ] Core development

### Branch management
As of this moment, let's have our own branch. I'll own the master branch,
and please create dev-1 and dev-2, and so on, whoever comes first. Maybe
by Sunday January 25 2020, let's do a merge, if I'm available. Then let's
apply a merge request.

### Techstack
Boxes are to be checked, once items are initially proven integrated to
each other.
- [ ] NGINX
- [ ] Unicorn (ASGI)
- [x] Flask (Framework)
- [x] MongoDB as Database

### Core development initial goal
- [ ] Simple RESTFUL registration
  - [ ] Register user
  - [ ] Register slave
- [ ] Simple RESTFUL login, returns JWS Token, plain string
  - [X] POST /login
    - [x] Returns JSON containing msg and jws (if valid, otherwise, just msg)
    - [x] Token must expire every 15 minutes.
  - [ ] POST /login-slave
    - [ ] Implement similar to /login, difference is this is for
          slave clients.
- [ ] Simple SLAVE client
  - [ ] Slave should be able to connect to master
  - [ ] Slave should be able to receive files from master
  - [ ] Slave should be able to execute commands, issued by master
* Front Server (nginx, hosts html files for UI)
  - [ ] Serves static html, javascript and images (just initial stuff)
  - [ ] Develop login page
    - [ ] Perform request to login server /login
    - [ ] Client must store jws upon successful login to local-storage
  - [ ] Develop home page
    - [ ] Client must send auth token from local storage (Authorization: Bearer JWS-STRING)
    - [ ] Side bar consist of
      - [ ] Upper side panel (left)
        - [ ] New item
        - [ ] People
        - [ ] Manage Jonkkins
        - [ ] New View
      - [ ] Lower side panel (left)
        - [ ] Build Executor Status
          - [ ] List of connected agents / slaves
          - [ ] Number of executors (per agent)
- [ ] Simple MASTER server.
  - [ ] Must implement a middleware that always check for login
        by checking if jws is forged, and interpret the sent claim
        by the client.
  - [ ] All requests are authenticated. There are two users of master
    - [ ] Human client -- Validate
    - [ ] Slave client -- Validate
  - [ ] New job registration
    - [ ] Freestyle
  - [ ] Job action update
    - [ ] Enable parameters
    - [ ] Run shell command
      - [ ] Through `#!/some/header`, we must be able to run a script
            that we want. Like for example: `#!/usr/bin/env python` must
            allow us to treat the script as python. Or `#!/bin/bash` must
            treat the script as bash. Without header, we'll treat the
            script as a regular bash file, just like how jenkins do it.
    - [ ] Trigger another local job, parametized


### Slack channel
- Let's just use what we have now...

### Since this is a CI/CD Tool
What about, let's use this as it's own CI/CD tool. If we made the initial
of this project, let's deploy it to one of my servers and use itself as
it's very own CI/CD tool that:
  - Sends slack notification
  - Perform docker build and push to hub.docker.com

Nice goal right? :)
