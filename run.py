"""
Promotions RESTFUL service
Starts the service and initializes logging
"""

import os
from app import app, service

# Pull options from environment
HOST = os.getenv('HOST', '0.0.0.0')
DEBUG = (os.getenv('DEBUG', 'False') == 'True')
PORT = os.getenv('PORT', '5000')

######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print("****************************************")
    print(" P R O M O T I O N S  S E R V I C E   R U N N I N G")
    print("****************************************")
    # server.init_db()
    # service.initialize_logging()
    service.init_db()
    app.run(host=HOST, port=int(PORT), debug=DEBUG)
