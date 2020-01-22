# Jonkkins
A copycat of Jenkins. Will be written in python.

## Initial Structure
Project will consist of modules `modules/{module}`. As of the
moment, the project will have one repository for now. Maybe we'll
have more than one repository. Let's see.



## Hmm
We need a production server. I don't like to focus on that one atm, so
for you contributors, plz research for:
  * uWSGI
  * nginx
  * integrate flask with uWSCGI and nginx
  * I think:
    * Every container will have nginx within python container.
    * We can have ENVIRONMENT as trigger.
    * SERVER_BUILD=DEV/PROD
      * If PROD, then instance will run on nginx
      * If DEV, then instance will run on flask's server


## Initial goal
* Create simple login, returns jwt claim (signed)
  - Simple login API, all json
* Front Server (nginx, hosts html files for UI)
  - Serves static html, javascript and images
* Front API
  - Serves dynamic content, in a form of json
* Master Server 
* Agent / Slave Client
