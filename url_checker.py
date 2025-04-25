import argparse
import requests
from rich.console import Console
from rich import print
import json
import sys

console = Console() #instantiate the console object

def check_url_against_logins(url, logins):
    """Checks if any of the provided logins are valid for the given URL."""
    valid_logins = {}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

    for provider, credentials in logins.items():
        username = credentials.get("username")
        password = credentials.get("password")
        if username and password:
            check_url = f"{url}/player_api.php?username={username}&password={password}"
            try:
                response = requests.get(check_url, timeout=10, headers=headers)
                response.raise_for_status()
                data = response.json()

                if "user_info" in data and data["user_info"].get("auth") == 1 and data["user_info"].get("status") != "Disabled":
                    print(f"[bright_green]Valid[/bright_green] login found for [bright_cyan]{provider}[/bright_cyan] on [link={url}]{url}[/link]")
                    valid_logins[provider] = {"username": username, "password": password}
                else:
                    print(f"[bright_red]Invalid[/bright_red] login for [bright_cyan]{provider}[/bright_cyan] on [link={url}]{url}[/link].")

            except requests.exceptions.HTTPError as e:
                print(f"[yellow]Error[/yellow] checking [bright_cyan]{provider}[/bright_cyan] on [link={url}]{url}[/link]: {e.response.status_code} {e.response.reason}")
            except requests.exceptions.RequestException as e:
                print(f"[yellow]Error[/yellow] checking [bright_cyan]{provider}[/bright_cyan] on [link={url}]{url}[/link]: {type(e).__name__}: {e}")
            except json.JSONDecodeError:
                print(f"[yellow]Warning[/yellow]: Non-JSON response from [link={url}]{url}[/link] for [bright_cyan]{provider}[/bright_cyan].")
        else:
            print(f"[yellow]Warning[/yellow]: Missing username or password for [bright_cyan]{provider}[/bright_cyan]. Skipping.")

    return valid_logins

def main():
    parser = argparse.ArgumentParser(description="Check a URL against a file of provider logins.")
    parser.add_argument("--logins", required=True, help="Path to the JSON file containing provider logins.")
    parser.add_argument("--url", required=True, help="The base URL to check against.")

    args = parser.parse_args()

    try:
        with open(args.logins, "r") as f:
            logins_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Logins file '{args.logins}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Logins file '{args.logins}' is not valid JSON.")
        sys.exit(1)

    print(f"Checking URL: [link={args.url}]{args.url}[/link] against logins...")
    valid_logins = check_url_against_logins(args.url, logins_data)

    if valid_logins:
        print("\n[bright_green]Valid Logins Found:[/bright_green]")
        console.print_json(data=valid_logins)
    else:
        print("\n[bright_red]No valid logins found for the provided URL.[/bright_red]")

if __name__ == "__main__":
    main()
