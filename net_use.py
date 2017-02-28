import subprocess
import sys
import os
import datetime
import logging


logging.info("mapping "+driveLetter+ " to "+networkPath)

#Connect to map network drive to letter 
mapCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
    
logging.info('NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user )
try:
    output=subprocess.check_output(mapCMD, shell=True)
    logging.debug(output)
except subprocess.CalledProcessError, e:
    logging.error(e)
    logging.error(e.output)
        
# Disconnect anything on drive letter L
delCMD = 'NET USE ' + driveLetter + ' /d /Y'
logging.info(delCMD)
try:
    output=subprocess.check_output(delCMD, shell=True)
    logging.debug(output)
except subprocess.CalledProcessError, e:
    logging.error(e)
    logging.error(e.output)    
