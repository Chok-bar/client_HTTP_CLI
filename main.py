import argparse
import requests
import json


def send_request(action, additional_data=None):
    url = "http://localhost:9999"
    payload = {"action": action}

    if additional_data:
        payload.update(additional_data)

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(json.dumps(response.json(), indent=4))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="HTTP Client CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: list
    subparsers.add_parser("list", help="List available games")

    # Command: subscribe
    subscribe_parser = subparsers.add_parser("subscribe", help="Subscribe to a game")
    subscribe_parser.add_argument(
        "--id_game", type=int, required=True, help="ID of the game to subscribe to"
    )

    args = parser.parse_args()

    if args.command == "list":
        send_request("list")
    elif args.command == "subscribe":
        send_request("subscribe", {"id_game": args.id_game})
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
