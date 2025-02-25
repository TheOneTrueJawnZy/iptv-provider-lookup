# Tool to attempt to determine what service a reseller is providing

A resellers will provide you with a username, password, and host for Xtream. 
You can use the same login with a different URL to see if it's the same provider.


## Usage

```bash
python providers-lookup.py --providers providers.json --user USERNAME --pw PASSWORD
```

### Sameple output

```
Failed login for Provider1 - Invalid credentials.
Failed login for Provider2 - 404 Not Found
Failed login for Strong - 513
Failed login for MEGA - 404 Not Found
Failed login for Eagle - 403 Forbidden
Success login for MAX
{
  "user_info": {
    "username": "REDACTED",
    "password": "REDACTED",
    "message": "Happy days!",
    "auth": 1,
    "exp_date": "REDACTED",
    "is_trial": "0",
    "active_cons": "0",
    "created_at": "",
    "max_connections": "1",
    "allowed_output_formats": [
      "m3u8",
      "ts"
    ],
    "status": "Active"
  },
  "server_info": {
    "url": "REDACTED",
    "port": "80",
    "https_port": "443",
    "server_protocol": "http",
    "rtmp_port": "8001",
    "timezone": "Europe/London",
    "timestamp_now": REDACTED,
    "time_now": "2025-02-01 01:01:55"
  }
}
Found 18070 live streams for MAX.
Failed login for B1G - 512
```


When it gets a successful login, it outputs the `user_info` and `server_info` to the command line. 
It then checks the `get_live_streams` endpoint, and outputs how many `Live Channels` the server reports

### response codes

|  Error | Meaning  |
| ------------ | ------------ |
| Invalid Credentials  | Self Explanitory |
| 404 Not Found | Probably a bad URL for the provider |
|512|Unused HTTP response code, I assume it means bad login | 
|513|Unused HTTP response code, I assume it means bad login | 
|403 Forbidden| Bad Login|


### providers.json

At strong suggestion from the [IPTVGroupBuy Subreddit](https://www.reddit.com/r/IPTVGroupBuy) I will not be providing a list of providers, and I find it unlikely that you will see a list anywhere. It's just a bad idea to post such a thing- it will get them shut down.

As such, you will need to source your own providers urls in order to use this service. What's provided in the code repository is a DUMMY file so you have the correct json format. You will need to replace it!

## How to get your Login from a M3U ([credit to /u/1989guy on Reddit](https://www.reddit.com/r/IPTVGroupBuy/comments/1hwyfao/how_to_find_out_xtream_code_from_m3u_and_viceversa/))

```
Here is an example M3U link
M3U Link:  http://website-Url.xyz/get.php?username=abcdefgh1234&password=1234qwerty&type=m3u&output=mpegts
Simplified as URL + /get.php? + username=YOUR_USERNAME + password=YOUR_PASSWORD + &type=m3u&output=mpegts

To get Xtream Code, you just need to extract the URL, username and password from the above example.

* URL: http://website-Url.xyz
* username: abcdefgh1234
* password: 1234qwerty
```


## Install

1. Ensure that Python is installed and accessible from the command line. You can test this by running the following command and ensuring that the version numebr is printed out:

```bash
python3 —version
```

it's also possible that it may just be called python, but the version reply myust be python 3.x (written and tested with Python 3.12.8)

```bash
python --version
```

2. Clone the repository using the following command:

```bash
git clone https://github.com/TheOneTrueJawnZy/iptv-provider-lookup/
cd iptv-provider-lookup/
```

you can also just download the code as a zip file - https://github.com/TheOneTrueJawnZy/iptv-provider-lookup/archive/refs/heads/main.zip

```bash
unzip main.zip
cd iptv-provider-lookup/
```

3. Create a virtual environment and activate it using the following commands (reminder: you may need to use python instead of python3 here):

on Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

on Windows:
```bash
python -m venv venv
./venv/Scrpits/activate
```

4. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```



## Potential Security Concerns

I felt that this tool was better self-hosted than as a webpage because I don't want to be responsible for anyone elses logins. Even if I didn't intentionally try and steal logins, it would very likely still show up in various logs. It's possible it could be written in a way where it would run entirely locally in someone's browser, but my suspicion is that most users wouldn't know how to audit that safely.

The way it is written does still potentially have two security flaws.

The first exists anywhere that you're using IPTV. If your provider's server doesn't use HTTPS, then your username and password could be seen by any number of snooping. This is already an inherent issue with the internet, and it's WHY https should be used everywhere.

The second issue is that a reseller could POTENTIALLY setup a honeypot on their login server. Actually, they likely have logging on by default, and so it does get recorded. In theory, this means they could search through logins that failed their system, and then try them at other providers (exactly like we're doing!).


These are just hypothetical concerns I thought of. If this was something important like banking, PHI, or other sensative information, I'd actually be concerned, but I did want to share the possibility so others are aware.

## Credits
https://github.com/estrellagus/ - thank you for the inspiration, also borrowed heavily from your README

https://www.reddit.com/r/IPTVGroupBuy/comments/1hwyfao/how_to_find_out_xtream_code_from_m3u_and_viceversa/
