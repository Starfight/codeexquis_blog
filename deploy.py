# encoding: utf-8
"""
Déploiement sur serveur SSH pour pelican
author: Nicolas Drufin <nicolas.drufin@ensc.fr>
date: 2016-12-21
"""

# import 
from paramiko.rsakey import RSAKey
from paramiko.client import SSHClient, AutoAddPolicy
import getpass
import os
import sys
from configparser import ConfigParser
from scp import SCPClient

# const
CONFIG_SECTION = "CONFIG"
DIR_NAME="output"

def import_config(filename):
    # open config file
    try:
        config = ConfigParser()
        config.optionxform=str
        config.read(filename)
        return config
    except Exception as e:
        print("Unable to open config file {0}: {1}".format(sys.argv[1], str(e)))
        sys.exit(1)

def main(argv):
    """
    Main script function
    """
    # import config
    config = import_config(argv[0])
    user = config.get(CONFIG_SECTION, "USER")
    keyfile = config.get(CONFIG_SECTION, "KEYFILE")
    host = config.get(CONFIG_SECTION, "HOST")
    output = config.get(CONFIG_SECTION, "OUTPUT")
    servdir = config.get(CONFIG_SECTION, "SERVDIR")
    servuser = config.get(CONFIG_SECTION, "SERVUSER")
    
    # vérification fichier de clé
    if not os.path.isfile(keyfile):
        print("File {0} does not exist !".format(keyfile))
        sys.exit(1)
    key = RSAKey.from_private_key_file(keyfile)
        
    # défini le client
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    
    # initialise la connexion
    client.connect(host, pkey=key, username=user)
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')
    
    # charge les fichiers 
    scp = SCPClient(client.get_transport())
    print("Copie des fichiers en cours ...")
    scp.put(output, DIR_NAME, True)
    print("Terminé")
    
    # déplace les fichiers dans le fichier www
    stdin.write('''
    sudo su -c "rm {1}/* -rf" 
    sudo su -c "mv {0}/* {1}"
    sudo su -c "chown {2}. {1} -R"
    sudo su -c "chmod -R u+rwX,go+rX,go-w {1}"
    exit
    '''.format(DIR_NAME, servdir, servuser))
    print(stdout.read().decode('utf-8'))
    
    # fermeture des services
    scp.close()
    stdout.close()
    stdin.close()
    client.close()  


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))