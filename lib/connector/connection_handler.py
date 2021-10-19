from lib.connector.connector_base import base_connect, ExceptionServerNotRespondingOrWrongCreds

def show_all_ok():
  message = "SUCCESS, CONNECTED"
  print(message)


def handle_ExceptionServerNotRespondingOrWrongCreds():
  message = """
==== ERROR ====
Either you entered the wrong credentials or the server is \
temporarily down.

Check your credentials and/or retry to connect later.
"""
  print(message)

def handle_connect(uname, password, routerip=None):
  try:
    base_connect(uname, password, routerip)
    show_all_ok()
  except ExceptionServerNotRespondingOrWrongCreds:
    handle_ExceptionServerNotRespondingOrWrongCreds()
