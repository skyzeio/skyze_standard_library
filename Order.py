class Order(object):
  '''Order Class'''
  __average = None
  __datetime = None
  __fee = None
  __filled = None
  __id = None
  __info = {'avg_execution_price': None,
            'cid': None,
            'cid_date': None,
            'exchange': None,
            'executed_amount': None,
            'gid': None,
            'id': None,
            'is_cancelled': None,
            'is_hidden': None,
            'is_live': None,
            'oco_order': None,
            'order_id': None,
            'original_amount': None,
            'price': None,
            'remaining_amount': None,
            'side': None,
            'src': None,
            'symbol': None,
            'timestamp': None,
            'type': None,
            'was_forced': None}
  __price = None
  __remaining = None
  __side = None
  __status = None
  __symbol = None
  __timestamp = None
  __type = None
  __mike = None

  def __init__(self, dictionary):
    self.__dict__.update(dictionary)

  def getAverage(self):
    '''Getter'''
    return self.__average

  def getDatetime(self):
    '''Getter'''
    return self.__datetime

  def getFee(self):
    '''Getter'''
    return self.__fee

  def getFilled(self):
    '''Getter'''
    return self.__filled

  def getId(self):
    '''Getter'''
    return self.__id

  def getInfo(self):
    '''Getter'''
    return self.__info

  def getPrice(self):
    '''Getter'''
    return self.__price

  def getRemaining(self):
    '''Getter'''
    return self.__Remaining

  def getSide(self):
    '''Getter'''
    return self.__side

  def getStatus(self):
    '''Getter'''
    return self.__status

  def getSymbol(self):
    '''Getter'''
    return self.__symbol

  def getTimestamp(self):
    '''Getter'''
    return self.__timestamp

  def getType(self):
    '''Getter'''
    return self.__type
