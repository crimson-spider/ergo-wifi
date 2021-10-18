from lib.creds.rw_cred import MissingCredFile, read_credentials
from lib.creds.cred_updater import ask_update_credentials

CRED_FILE = ".creds.json"

def disp_creds_not_found_message():
  msg = "=== Credential file not found, asking ===\n"
  print(msg)

def maybe_ask_credentials(cred_file):
  try:
    uname, password = read_credentials(cred_file)
  except MissingCredFile:
    disp_creds_not_found_message()
    ask_update_credentials(cred_file)

def get_credentials() -> tuple[str,str]:
  maybe_ask_credentials(CRED_FILE)
  uname, password = read_credentials(CRED_FILE)
  return uname, password
