# 3. Setup a python script that connects to remote servers over ssh and does the following:  
   a. Accept commands to be executed on all the remote machines at once  
   b. Wait for the execution to be completed on all the remote machines  
  c. Accept next input only once the previous execution is completed on all the machines (failed/successful)

use [typer](https://typer.tiangolo.com/) library as a learning opportunity

I developed this solution in 2 parts:
  a. [interactive cli](app.py) - with typer
  b. [core ssh handler](ssh_handler.py) - with ansible

I could have used paramiko for the ssh handler but it's a bit low-level and not very fun!

I chose `shell` module over `command` module in ansible task to support complicated instructions that we use in real life.

The app is simple cli wrapper that [prompts](app.py#L15) user each time a command needs to be run.
This command is then passed to a simple [task](ssh_handler.py#L101) wrapped in a minimal play.

The app also takes and optional argument for /path/to/hosts file, defaulting to `${PWD}/hosts`. This file must be an ansible compatible inventory file.
