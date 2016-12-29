

# 表名是user是ok的   但是是users就有问题 很疑惑 待考究
import time,uuid

from ty_orm import Model,StringField,BooleanField,FloatField,TextField,IntegerField

def next_id():
    return '%15d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
    __talbe__ = 'users'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __talbe__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __talbe__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


