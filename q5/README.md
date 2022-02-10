# Shell script to take third most CPU & Memory consuming process, this should output to output file with the following properties  
  a. Process Name  
  b. % CPU  used  
  c. % Memory used   
  d. PORT  
  e. PID

## Solution
`top` command is the most suitable candidate.  
but this poses problems due to the streaming nature of `top` output

we need to see how we can limit this behaviour by going through its manual with  `man top` command

this gives us some useful options:
```
-b  :Batch-mode operation
    Starts  top  in Batch mode, which could be useful for sending output from top to other programs or to a file.  In this mode, top will not accept input and runs until the iterations limit you've set with the `-n' command-line option or until killed.
-n  :Number-of-iterations limit as:  -n number
    Specifies the maximum number of iterations, or frames, top should produce before ending.
-o  :Override-sort-field as:  -o fieldname
    Specifies the name of the field on which tasks will be sorted, independent of what is reflected in the configuration file.  You can prepend a `+' or `-' to the field name to also  override  the
    sort direction.  A leading `+' will force sorting high to low, whereas a `-' will ensure a low to high ordering.
    This option exists primarily to support automated/scripted batch mode operation.

-O  :Output-field-names
    This  option acts as a form of help for the above -o option.  It will cause top to print each of the available field names on a separate line, then quit.  Such names are subject to nls translation.
```
with this we have our base command to be formatted

```
top -b -n1 -o%MEM
```

with a little head tail operation, we have isolated **third** most resource consuming processes
```
# top -b -n1 -o%MEM | head -n10 | tail -n4
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  592 ajay      20   0 11.009g 183628  39676 S   0.0  1.6   0:59.26 node
  436 root      20   0 1718500  86728  49852 S   0.0  0.8   0:01.66 dockerd
   41 ajay      20   0  961864  87840  31736 S   0.0  0.8   0:47.64 node

```
```
# top -b -n1 -o%MEM | head -n10 | tail -n4 | tail -n1
   41 ajay      20   0  961864  87840  31736 S   0.0  0.8   0:47.64 node
```

now we need to rearrange the columns.  
for this we will use `awk` command.
we will also use printf to be able to use formatting with tabs
```
# top -b -n1 -o%MEM | head -n10 | tail -n4 | tail -n1 | awk {'printf ("%s\n%s\n%s\n%s\n", $12, $9, $10, $1)'} 
node
0.0
0.8
41
```

but we still do not have the port our process is listening on. 
so we will use `netstat` command to get the port and then inject it in our awk expression.

```
# PID=41
# netstat -lntup | grep ${PID} | awk {'print $4'}
:::42463
```

this will make the expression to long, so we will wrap this in a function that takes pid as an input
```
get_port () {
    PID=$1
    sudo netstat -lntup | grep ${PID} | awk {'print $4'}
}

get_port 41
```
we can now use this function with our awk statement and write to the file
```
get_port () {
    PID=$1
    sudo netstat -lntup | grep ${PID} | awk {'print $4'}
}
top -b -n1 -o%MEM | head -n10 | tail -n4 | tail -n1 | awk {'printf ("%s\n%s\n%s\n%s", $12, $9, $10, $1)'} > out.txt
get_port $(cat out.txt | tail -n1) >> out.txt
```

get_port function may or maynot give an output based on the process, hence port in `out.txt` may be null