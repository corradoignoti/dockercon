
# Dockercon

dockercon is a tool to switch between docker contexts faster.

## How to install
Copy dockercon.py somewhere into your path
```bash
cp ./dockercon.py /usr/local/bin/dockercon
```

## How to use
To add a context:

```bash
dockercon -a mydockerhst-local --host ssh://user@192.168.1.1 --stack swarm
```

To switch to a context:

```bash
dockercon mydockerhst-local
```

To see the saved context:

```bash
$ dockercon
```

To get help:

```bash
$ dockercon -h

usage: dockercon [-h] [-d <NAME>] [-a <NAME>] [--host <HOST>] [--stack <STACK>] [<NAME>]

dockercon is a tool to switch between docker contexts faster.

positional arguments:
  <NAME>           Switch to context '<NAME>'

optional arguments:
  -h, --help       show this help message and exit
  -d <NAME>        delete context <NAME>
  -a <NAME>        add context <NAME>
  --host <HOST>    <HOST> to use with a new context
  --stack <STACK>  orchestrator <STACK> to use with a new context
```

## Author

- [@corradoignoti](https://github.com/corradoignoti)

