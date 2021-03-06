# skybriefing-dabs

Automated script to download PDFs from [skybriefing.com](https://www.skybriefing.com/) and send them via email.
Uses [Selenium](http://www.seleniumhq.org/) for simulating a browser, so the PDFs get created properly.

## Installation

### Mac OS X, Windows 7, Ubuntu
* Install Firefox via official Website
* Install Selenium: `pip install selenium`
* Install Geckodriver: `brew install geckodriver`

(Trust certificates: `pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install pyvirtualdisplay selenium`)

Additional step for Raspberry Pi: `sudo apt-get install iceweasel xvfb`. If you don't have `pip` installed on Windows, see [here](http://stackoverflow.com/q/4750806).

Copy the scripts to a folder, configure them as mentioned below and then run them each to check if they work on your system.

* `get_pdfs.py` simulates the browser to download the PDFs
* `send_email.py` sends the email via a gmail account
* `skybriefing_dabs.sh` is wrapper to execute both scripts, run this via cron

## Configuration

### Downloading PDFs

At the beginning of the script `get_pdfs.py` there is a config section in which you can specify login and some other data. The only mandatory parameter is `WITH_LOGIN`, set this to `True` if you have a login, or `False` if you just want the DABS report. If set to False, all other parameters will be ignored.

    WITH_LOGIN = True # Use script with login? if true, fill out info below
    USER = 'my_login'
    PW = 'my_password'
    FLUGPLATZ = 'LSZH'
    LOWER_FL = '000'
    UPPER_FL = '120'

### E-Mail

In `send_email.py`, you'll have to configure sender and recipient email addresses. Sender Email must be gmail, don't use your real address here.
Also make sure to allow ["access for less secure apps"](https://www.google.com/settings/security/lesssecureapps) to enable sending emails via script.

    SEND_TO = ['myemail1@gmail.com', 'myemail2@gmail.com']
    PDFS = 1 # set to 2 if you used a login on other script
    PDF_PATH = 'my path' # Mac OS X: '~/temp/', or on Raspi: '/home/pi/temp/'
    SENDER_EMAIL = 'sender-email@gmail.com'
    SENDER_PW = 'gmail-password'
    EMAIL_SUBJECT = 'skybriefing.com report'
    EMAIL_BODY = 'Sent from Raspberry Pi :)'
    
*Important*: Make sure the directory matches where the files are downloaded and that is temporary! The script will delete *all* files in the directory to clean up!

### Automate (Linux / Mac only)
Make file executable: `chmod +x skybriefing_dabs.sh`

Install crontab: Use `crontab -e` to open crontab.
Add the following entry:

    0 7 * * * ~/path/to/your/script/skybriefing_dabs.sh`
