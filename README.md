# bootstrap-tornado
Write a tornado app from a template

[python](https://python.org) + [tornado](http://www.tornadoweb.org) + [rethinkdb](https://www.rethinkdb.com/) + [vue](http://vuejs.org/)

# Install
```
npm i -g bower
bower install

# suggest use virtualenv
pip install -r requirements.txt
```

Install [rethinkdb](https://www.rethinkdb.com/docs/install/)

# Usage
```
python -u web.py --port 6000 # --debug
```

Environments can be used to set Rethinkdb, defaults are

```
- RDB_NAME=bootstrap-tornado
- RDB_HOST=localhost
- RDB_PORT=28015
- COOKIE_SECRET=""
```

See [settings.py](settings.py) for more details.

# Database
rethinkdb

# LICENSE
[MIT](LICENSE)