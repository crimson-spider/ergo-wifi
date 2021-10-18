from lib.creds.rw_cred import set_credentials

def _ask_uname(ask_str:str = None) -> str:
  """Asks for username from console and gives the result.\
     ask_str will be displayed as the message if provided"""

  default_ask_str = "Plaese insert username:\n  "
  if ask_str == None:
    ask_str = default_ask_str

  uname = input(ask_str)
  return str(uname)


def _ask_password(ask_str:str = None) -> str:
  """Asks for password from console and gives the result.\
     ask_str will be displayed as the message if provided"""

  default_ask_str = "Plaese insert password:\n  "
  if ask_str == None:
    ask_str = default_ask_str

  password = input(ask_str)
  return str(password)


def ask_credentials() -> tuple[str, str]:
  """Asks user for username and password 
  and returns the provided values."""

  uname = _ask_uname()
  password = _ask_password()
  return uname, password


def ask_update_credentials(cred_file) -> None:
  """Asks user to update credentials"""
  
  uname, password = ask_credentials()
  set_credentials(uname, password, cred_file)


def _debug():
  print(ask_credentials())

if __name__ == "__main__":
  _debug()
