import sshtunnel
import pymongo

MONGO_URI = 'mongodb://127.0.0.1:37017'

SSH_SERVER = 'ssh.server.local'
SSH_PORT = 22
SSH_USERNAME = 'admin'
SSH_PASSWORD = 'password'

with sshtunnel.open_tunnel(
    (SSH_SERVER, SSH_PORT),
    ssh_username=SSH_USERNAME,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=('127.0.0.1', 27017),
    local_bind_address=('0.0.0.0', 37017)
  ) as tunnel:

    # print(tunnel.local_bind_port)

    # connect to mongo uri
    client = pymongo.MongoClient(MONGO_URI)

    # list database names
    names = client.list_database_names()
    print(names)