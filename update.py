import start_me, Tastiere, callback_handler, message_handler, SQL, credentials, os

""" this module should work, but it doest lol
    obj: reload modules without stop and start back server
"""

def reloaded():
    reload(start_me)
    reload(Tastiere)
    reload(callback_handler)
    reload(message_handler)
    reload(SQL)
    reload(credentials)
    os.system('clear')
    print "Reload"
