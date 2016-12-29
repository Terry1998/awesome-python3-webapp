import logging
import asyncio
import aiomysql
import sys
import ty_orm
import time,uuid


def log(sql,args=()):
    logging.info('SQL:%s'%sql)


@asyncio.coroutine
def destory_pool():
    global __pool
    if __pool is not None :
        __pool.close()
        yield from __pool.wait_closed()

#创建连接池
@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connetion pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw.get('user','root'),
        password=kw.get('password','791123'),
        db=kw.get('db','awesome'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

def next_id():
    return '%15d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(ty_orm.Model):
    __talbe__ = 'users'

    id = ty_orm.StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email = ty_orm.StringField(ddl='varchar(50)')
    passwd = ty_orm.StringField(ddl='varchar(50)')
    admin = ty_orm.BooleanField()
    name = ty_orm.StringField(ddl='varchar(50)')
    image = ty_orm.StringField(ddl='varchar(500)')
    # create_at = ty_orm.FloatField(default=time.time)

loop = asyncio.get_event_loop()
@asyncio.coroutine
def test():
    yield from create_pool(loop=loop)

    all = yield from User.findAll()
    print(all)

    yield from destory_pool()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)


