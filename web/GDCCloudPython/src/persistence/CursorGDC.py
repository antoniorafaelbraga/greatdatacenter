'''
Created on 18 de dez de 2016

@author: rafaelbraga
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
            '''

    import time
    import pymongo
    from persistence import Connection
    
    client = Connection.Connection('192.168.1.5', 27017)
    #client = pymongo.MongoClient()
    oplog = client.oplog.log
    first = oplog.find().sort('$natural', pymongo.ASCENDING).limit(-1).next()
    print(first)
    ts = first['id']
    
    while True:
        # For a regular capped collection CursorType.TAILABLE_AWAIT is the
        # only option required to create a tailable cursor. When querying the
        # oplog the oplog_replay option enables an optimization to quickly
        # find the 'ts' value we're looking for. The oplog_replay option
        # can only be used when querying the oplog.
        cursor = oplog.find({'id': {'$gt': ts}}, cursor_type=pymongo.CursorType.TAILABLE_AWAIT, oplog_replay=True)
        while cursor.alive:
            for doc in cursor:
                ts = doc['id']
                print(doc)
            # We end up here if the find() returned no documents or if the
            # tailable cursor timed out (no new documents were added to the
            # collection for more than 1 second).
            time.sleep(1)        