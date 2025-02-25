# Tools to Learn About IPTV Services

This repository contains a set of Python tools designed to assist users of IPTV services in gaining detailed information about their services. All the tools are written in Python and are intended to be simple and user-friendly, allowing for easy modification and learning.

## Scripts and Tools

For more information on each specific tool and script, follow the links below:

1. [iptv-xstream-download.py](./README.iptv-xstream-download.md): This script is used to download all relevant files from an xtream provider and save them for future archiving or further processing.
2. [find-iptv-channels-details.py](./README.find-iptv-channels-details.md): This script queries an xtream provider’s live channel list and searches for specific channels or categories. It then notes the number of EPG programs available, whether they have catch-up capabilities, the codec and resolution for each channel, and the frame rate.

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


## Credits
https://github.com/estrellagus/ - thank you for the inspiration, also borrowed heavily from your README
