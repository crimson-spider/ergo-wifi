import requests
import re

ROUTER_IP = "10.250.33.254"

class ExceptionServerNotRespondingOrWrongCreds(Exception):
  pass

def _raise_error_if_nedded(connection_response):
  matches = re.findall("RADIUS server is not responding", connection_response)
  if len(matches) != 0:
    raise ExceptionServerNotRespondingOrWrongCreds



def raw_connect(uname:str, password:str, routerip:str) -> str:
  data ={"username":uname, "password": password, "dst":"", "popup":"true"}
  resp = requests.post("https://"+routerip+"/login", data , verify=False)
  return resp.text


def base_connect(uname:str, password:str, routerip:str=None) -> None:
  if routerip == None:
    routerip = ROUTER_IP
  conn_resp =  raw_connect(uname, password, routerip)
  _raise_error_if_nedded(conn_resp)
