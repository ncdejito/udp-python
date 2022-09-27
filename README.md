## Instructions
(same network)

1. In client, change `ip.add.re.ss` in client.py
1. In server, run terminal
```
sudo docker run -it --net=host --entrypoint /bin/bash pyfirmata
```

[Source](https://stackoverflow.com/a/27893987)