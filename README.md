# Description
Short python script that can be used in a bash script in order to be notfied when a long task end. You need to have credentials from your Google Cloud Platform (see [Linking Cloud Platform Project to Google Apps Script Project](https://gist.github.com/tanaikech/e945c10917fac34a9d5d58cad768832c#2-create-new-cloud-platform-project) for more details). This `JSON` file needs to be named `credentials.json`.<br/>

# Install dependancies 
```
pip3 install -r requirements.txt
```

## Command line exemple

```
python3 sender.py subject receiver msg_text
```

* subject: [string] it will be the subject of the mail
* receiver: [string] such as "address1@domain.com, address2@domain.com" or a [text file] with several address (one address for line, no comma divided)
* msg_text: [string] it will be the text of the mail



Source: [How to use Gmail API to send an email in Python](https://learndataanalysis.org/how-to-use-gmail-api-to-send-an-email-in-python/)
