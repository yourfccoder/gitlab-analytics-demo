from peewee import *

database = MySQLDatabase('gitlab_analytics', **{'charset': 'utf8', 'use_unicode': True, 'host': 'chat.youle.game', 'user': 'oylbin', 'password': 'ix[ob$kcyZg3I2se'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class GitlabCommits(BaseModel):
    author_email = CharField(index=True)
    author_name = CharField(index=True)
    authored_date = DateTimeField()
    commit = CharField(column_name='commit_id')
    committed_date = DateTimeField()
    committer_email = CharField()
    committer_name = CharField()
    created_at = DateTimeField()
    ignore = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    line_additions = IntegerField(null=True)
    line_deletions = IntegerField(null=True)
    line_total = IntegerField(null=True)
    message = CharField()
    parent_ids = IntegerField()
    project = IntegerField(column_name='project_id')
    project_path = CharField()
    title = CharField()

    class Meta:
        table_name = 'gitlab_commits'
        indexes = (
            (('commit', 'project'), True),
        )

