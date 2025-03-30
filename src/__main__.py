from src.CLI.main import CLI
from argparse import ArgumentParser


def main():
    # Create the argument parser
    parser = ArgumentParser(
        description="Gets the arguments to run the game with. Options are 'cli' or 'gui'."
    )

    # Add your arguments
    parser.add_argument(
        "--run_with",
        type=str,
        help="What to run the module with (CLI or GUI)",
        default="cli",
        choices=["cli", "gui"],
    )

    # Parse the arguments
    args = parser.parse_args()

    # Access the parsed arguments
    print(f"Received --args: {args.run_with}")

    CLI()


if __name__ == "__main__":
    main()
