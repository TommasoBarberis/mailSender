Short python script that can be used in a bash script in order to be notfied when a long task end.
Command line exemple:

```
python3 sender.py subject receiver msg_text
```

* subject: [string] it will be the subject of the mail
* receiver: [string] such as "address1@domain.com, address2@domain.com" or a [text file] with several address (one address for line, no comma divided)
* msg_text: [string] it will be the text of the mail
