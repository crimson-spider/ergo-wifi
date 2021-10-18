from lib.creds.cred_handler import get_credentials

def main():
  uname, password = get_credentials()
  connector.connect(uname, password)

if __name__=="__main__":
  main()
