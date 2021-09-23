# LinkedIn-Connection-Bot
LinkedIn bot for automating connections using Selenium. Iterate through your desired connections page to automate adding new connections. This example's TARGET_CONNECTION_URL is 2nd level in a blank search, but it could be tweaked to be used anywhere the connection button is present. You may be able to speed up the speed by tuning the time.sleep(), but it is left at 2 to err on the side of caution.


## Setup
Ensure python 3.9 is installed.

Install the Selenium webdriver for your preferred browser. This is set up for chrome, but firefox works too. You will just need to change "Chrome" on line 8 to "Firefox" or "Edge" (does anyone use edge...?).

### Creating .env file
For this server to run, you must create a .env file within the package, setting the following parameters:
```bash
LINKEDIN_USERNAME=
LINKEDIN_PASSWORD=
PATH_TO_SELENIUM=
```
Set the Selenium path to the location of the webdriver on your machine, and the Linkedin credentials to the account you wish to use.

### Running the Server
```bash
python connection_bot.py
```

## Improvements

To Do:
- Add semi-customized messages to each invite
