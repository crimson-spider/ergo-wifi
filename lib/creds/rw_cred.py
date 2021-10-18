"""
The credentials file should look like this:

{
  "uname" : "USRENAME",
  "password" : "PASSWORD"

}
"""
import json

_USERNAME_F = "uname"
_PASSWORD_F = "password"

class MissingCredFile(Exception):
  pass

def set_credentials(uname:str, password:str, cred_file:str) -> None:
  """writes credentials to given file"""
  with open(cred_file, 'w') as f:
    currjson = {}
    currjson[_USERNAME_F] = uname
    currjson[_PASSWORD_F] = password
    f.write(json.dumps(currjson))

def _read_credentials(cred_file) -> tuple[str, str]:
  """reads credentials from given file"""
  with open(cred_file, 'r') as f:
    currjson = json.loads(f.read())
    uname = currjson[_USERNAME_F]
    password = currjson[_PASSWORD_F]
    return uname, password

def read_credentials(cred_file:str):
  try:
    return _read_credentials(cred_file)
  except:
    raise MissingCredFile
