from logger.logger import Logger

log1 = Logger(caller='ZBPServer',level='DEBUG',path="/tmp/test.log")
log2 = Logger(caller='SmartServices')
log1.info('Im a INFO log')
log2.info('Cloud Services started now...')
log1.debug('Hey Im a DEBUG log')
log1.warn('Take care, Im a WARNING log')
log1.error('Oppps! error message here')
log1.critical('critical message')