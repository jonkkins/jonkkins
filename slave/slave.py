import requests

res = requests.post(('%s://%s/login-slave' % (config()['schema'], config()['master-url']), data={
    "name": config()['name'],
    "password": config()['password']
});

if res.status_code == 200:
    config_update_password(json.loads(res.text))['new_password'])
    while true:
        sleep(0.1)

