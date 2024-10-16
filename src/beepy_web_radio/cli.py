import argparse
import traceback
from typing import Dict, List

import requests


def get_stations(query: str) -> List[Dict]:
    url = "https://radio.garden/api/search"
    params = {"q": query}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    filtered_stations = [
        station
        for station in data["hits"]["hits"]
        if station["_source"]["type"] == "channel" and station["_score"] > 150
    ]

    return [
        {
            "title": station["_source"]["title"],
            "subtitle": station["_source"]["subtitle"],
            "stream": station["_source"]["stream"],
        }
        for station in filtered_stations
    ]


def search_stations(query: str):
    try:
        stations = get_stations(query)
        if stations:
            print(f"Found {len(stations)} stations:")
            for station in stations:
                print(
                    f"- {station['title']} - {station['subtitle']} "
                    f"({station['stream']})"
                )
        else:
            print("No stations found matching the query.")
    except requests.RequestException as e:
        print(f"Error searching for stations: {e}")


def play_station(station: str):
    print(f"Playing station: {station}")
    # Implement station playback logic here


def stop_playback():
    print("Stopping playback")
    # Implement stop playback logic here


def main():
    parser = argparse.ArgumentParser(description="Beepy Web Radio CLI")
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    search_parser = subparsers.add_parser("search", help="Search for stations")
    search_parser.add_argument(
        "query", nargs="+", help="Search query (can be multiple words)"
    )

    play_parser = subparsers.add_parser("play", help="Play a station")
    play_parser.add_argument("station", help="Station to play")

    subparsers.add_parser("stop", help="Stop playback")

    args = parser.parse_args()

    try:
        if args.command == "search":
            query = " ".join(args.query)
            search_stations(query)
        elif args.command == "play":
            play_station(args.station)
        elif args.command == "stop":
            stop_playback()
        else:
            parser.print_help()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nDetailed exception information:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
