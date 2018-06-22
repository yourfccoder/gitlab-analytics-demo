from flask import Flask
import os
import random
import string
import datetime
from gitlab_analytics_models import *

app = Flask(__name__)


@app.route("/")
def hello():
    # handle gitlab webhook here, save the event data into DB
    commit_id = ''.join(random.choice(string.ascii_lowercase) for x in range(40))
    gc = GitlabCommits(project=2,
                       project_path="owen/test",
                       commit_id=commit_id,
                       title="test",
                       create_at=datetime.datetime.now(),
                       parent_ids=1,
                       message="test",
                       author_email="oylbin@gmail.com",
                       author_name="oylbin",
                       authored_date=datetime.datetime.now(),
                       commit=commit_id,
                       committed_date=datetime.datetime.now(),
                       committer_email="oylbin@gmail.com",
                       committer_name="oylbin",
                       created_at=datetime.datetime.now(),
                       ignore=0,
                       line_additions=1,
                       line_deletions=1,
                       line_total=2
                       )
    gc.save()
    return "Hello World!"


def init_mariadb():
    # all the env here are defined in docker-compose.yml
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_port = os.getenv("MYSQL_PORT")
    mysql_user = os.getenv("MYSQL_USER")
    mysql_password = os.getenv("MYSQL_PASSWORD")
    mysql_database = os.getenv("MYSQL_DATABASE")
    print("init_mariadb")
    print(mysql_host)

    database.database = mysql_database
    database.connect_params = {'host': mysql_host, 'port': int(mysql_port),
                               'user': mysql_user,
                               'password': str(mysql_password),
                               'charset': 'utf8', 'use_unicode': True}

if __name__ == '__main__':
    init_mariadb()
    port = os.getenv("PORT")
    app.run(debug=True, host='0.0.0.0', port=port)
