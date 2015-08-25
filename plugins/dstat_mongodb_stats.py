### Author: <gianfranco@mongodb.com>

global mongodb_user
mongodb_user = os.getenv('DSTAT_MONGODB_USER') or os.getenv('USER')

global mongodb_pwd
mongodb_pwd = os.getenv('DSTAT_MONGODB_PWD')

global mongodb_host
mongodb_host = os.getenv('DSTAT_MONGODB_HOST') or '127.0.0.1:27017'

class dstat_plugin(dstat):
  """
  Plugin for MongoDB commands.
  """
  def __init__(self):
    global pymongo
    import pymongo

    try:
      self.m = pymongo.MongoClient(mongodb_host)
      if mongodb_pwd:
        self.m.admin.authenticate(mongodb_user, mongodb_pwd)
      self.db = self.m.admin
    except Exception, e:
      raise Exception, 'Cannot interface with MongoDB server: %s' % e

    stats  = self.db.command("listDatabases")
    self.dbList = []
    for db in stats.get('databases'):
      self.dbList.append(db.get('name'))

    self.name    = 'mongodb stats'
    self.nick    = ('dsize', 'isize', 'ssize')
    self.vars    = ('dataSize', 'indexSize', 'storageSize')
    self.type    = 'd'
    self.width   = 5
    self.scale   = 2
    self.lastVal = {}


  def extract(self):
    self.set = {}

    for db in self.dbList:
      self.db = self.m.get_database(db)
      stats = self.db.command("dbStats")
      for name in self.vars:
        self.set[name] = long(stats.get(name)) / (1024 * 1024)
    self.val = self.set
