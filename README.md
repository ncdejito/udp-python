## Instructions

1. (if different network) In both client and server, install zerotier
```
sudo snap install zerotier
sudo zerotier-cli info
snap connect zerotier:network-control
sudo zerotier-cli join abcdefg123456 # zerotier network ID
# in my.zerotier.com, check Auth
# address to ssh to is now in managed IPs
```

1. In client, change `ip.add.re.ss` in client.py

1. run terminal
```
sudo docker run -it --net=host --entrypoint /bin/bash pyfirmata
```

Sources:
* [client-server python](https://stackoverflow.com/a/27893987)
* [Zerotier install](https://www.youtube.com/watch?v=7C2AGnr9Q-w)