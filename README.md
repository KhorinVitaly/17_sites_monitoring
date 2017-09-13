# Sites Monitoring Utility

With this python script you can check website status and domain expiration date.

# How to Install

Python 3 should be already installed. 

# How to Use

Fill the text file with urls, for example urls.txt 

```
https://devman.org
https://bitbucket.org
```

Launch check_sites_health.py in terminal. Transfer file path to text file as argument.
```
python3 check_sites_health.py -p urls.txt

https://devman.org
Server responded with HTTP 200 status
Domain is available for one month at least
https://bitbucket.org
Server responded with HTTP 200 status
Domain is available for one month at least
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
