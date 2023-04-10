import logging
import graypy


logger = logging.getLogger('test from py')
logger.setLevel(logging.DEBUG)

handler = graypy.GELFTLSHandler('141.254.69.130', 12201, validate=True, ca_certs = '/etc/ssl/certs/ca-certificates.crt')
logger.addHandler(handler)



logger.debug("His this is a test message from thinkpad")

