import argparse


def search_stations(query: str):
    print(f"Searching for stations with query: {query}")
    # Implement station search logic here


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
    search_parser.add_argument("query", help="Search query")

    play_parser = subparsers.add_parser("play", help="Play a station")
    play_parser.add_argument("station", help="Station to play")

    subparsers.add_parser("stop", help="Stop playback")

    args = parser.parse_args()

    if args.command == "search":
        search_stations(args.query)
    elif args.command == "play":
        play_station(args.station)
    elif args.command == "stop":
        stop_playback()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
