import argparse
import requests
from rich.console import Console
from rich import print
import json
import sys

console = Console() #instantiate the console object

def check_login_and_display_info(server, provider, username, password):
    """Checks login and displays user/server info if successful."""
    url = f"{server}/player_api.php?username={username}&password={password}"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data["user_info"]["auth"] == 0 or data["user_info"]["status"] == "Disabled":
            print(f"[bright_red]Failed[/bright_red] login for [bright_cyan]{provider}[/bright_cyan] - Invalid credentials.")
        elif "user_info" in data and "server_info" in data:
            print(f"[bright_green]Success[/bright_green] login for [bright_cyan]{provider}[/bright_cyan]")
            console.print_json(data=data) 
            data = requests.get(url+"&action=get_live_streams", headers=headers).json()
            count = len(data)
            print(f"Found [bright_green]{count}[/bright_green] live streams for [bright_cyan]{provider}[/bright_cyan].")
        else:
            print(f"[bright_red]Failed[/bright_red] login for [bright_cyan]{provider}[/bright_cyan] - Unknown error.")

    except requests.exceptions.HTTPError as e:
        print(f"[bright_red]Failed[/bright_red] login for [bright_cyan]{provider}[/bright_cyan] - {e.response.status_code} {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"[bright_red]Failed[/bright_red] login for [bright_cyan]{provider}[/bright_cyan] - {type(e).__name__}: {e}")
    except json.JSONDecodeError:
        print(f"Login successful, but response was [yellow]not valid JSON[/yellow] for [bright_cyan]{provider}[/bright_cyan] - {e}")

def main():
    parser = argparse.ArgumentParser(description="Check logins against IPTV providers.")
    parser.add_argument("--providers", required=True, help="Path to the providers JSON file.")
    parser.add_argument("--user", required=True, help="Username for authentication.")
    parser.add_argument("--pw", required=True, help="Password for authentication.")

    args = parser.parse_args()

    try:
        with open(args.providers, "r") as f:
            providers = json.load(f)
    except FileNotFoundError:
        print(f"Error: Providers file '{args.providers}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Providers file '{args.providers}' is not valid JSON.")
        sys.exit(1)

    results = {}

    for provider, server in providers.items():
        check_login_and_display_info(server, provider, args.user, args.pw)

if __name__ == "__main__":
    main()
