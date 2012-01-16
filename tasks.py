import pymongo
import settings_remote as settings

def task_db():
    return pymongo.Connection(settings.MONGO_HOST, settings.MONGO_PORT)[settings.MONGO_DB]


def task_collection():
    print 'test'
    collection = task_db()['tasks']
    collection.ensure_index('uuid', unique=True)
    collection.ensure_index([('date', pymongo.DESCENDING)])
    return collection


def get_task(latest_count=10):
    try:
        cursor = task_collection().find(limit=latest_count, sort=[('date', pymongo.DESCENDING)])
        result = [el for el in cursor]
        for res in result:
            del res['_id']
        return result
    except Exception as ex:
        print ex
