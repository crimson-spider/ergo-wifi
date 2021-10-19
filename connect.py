from lib.creds.cred_handler import get_credentials
from lib.connector import connection_handler as connector

def main():
  uname, password = get_credentials()
  connector.handle_connect(uname, password)

if __name__=="__main__":
  main()
