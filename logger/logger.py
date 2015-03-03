import logging
import sys
import threading

_formatter = '%(asctime)s - %(levelname)s:: %(caller)s:: %(message)s'
_dateformatter='%m/%d/%Y %I:%M:%S %p'
_handlers = [{'handler':'StreamHandler','format': None,'datefmt': None,'args':{'stream':None}}, 
             {'handler':'FileHandler','format': None,'datefmt': None,'args':{'filename':'log.log'}}
            ]
class Logger(object):
    """
    Logger level value, setting level all above levels make a log
    CRITICAL    50
    ERROR       40
    WARNING     30
    INFO        20  <--- Default level
    DEBUG       10
    NOTSET       0
    """
    
    staticLogger = None
    loggerLock = threading.Lock()
    
    def __init__(self, caller='Object', level=None, path=None):
        self.level = logging.INFO if level is None else level
        self.caller = caller  
        if Logger.staticLogger is None:
            self.logger = logging.getLogger('Logger')
            self.logger.setLevel(self.level)
            for han_opt in _handlers:
                self.addHandler(han_opt,path)
            Logger.staticLogger = self.logger
        else:
            self.logger = Logger.staticLogger 
        
    def addHandler(self,handler_opt=None,path=None):
        if handler_opt is not None:
            logModule = sys.modules['logging']
            fn  = getattr(logModule,handler_opt['handler'])
            if handler_opt['handler'] == 'FileHandler' and path is not None:
                new_handler = fn(filename=path)
            else:
                new_handler = fn(**handler_opt['args'])
            new_handler.setLevel(self.level)
            fmt = _formatter if handler_opt['format'] is None else handler_opt['format']
            datefmt = _dateformatter if handler_opt['datefmt'] is None else handler_opt['datefmt']
            formatter = logging.Formatter(fmt=fmt,datefmt=datefmt)
            new_handler.setFormatter(formatter)
            self.logger.addHandler(new_handler)
    
    def info(self,msg):
        Logger.loggerLock.acquire()
        self.logger.info(msg,extra={'caller':self.caller})
        Logger.loggerLock.release()
    
    def warn(self,msg):
        Logger.loggerLock.acquire()
        self.logger.warn(msg,extra={'caller':self.caller})
        Logger.loggerLock.release()
    
    def debug(self,msg):
        Logger.loggerLock.acquire()
        self.logger.debug(msg,extra={'caller':self.caller})
        Logger.loggerLock.release()
        
    def error(self,msg):
        Logger.loggerLock.acquire()
        self.logger.error(msg,extra={'caller':self.caller})
        Logger.loggerLock.release()
        
    def critical(self,msg):
        Logger.loggerLock.acquire()
        self.logger.critical(msg,extra={'caller':self.caller})
        Logger.loggerLock.release()