
import argparse
from neuro_signal.data_handler import load_data
from neuro_signal.neurofeedback import provide_neurofeedback
from neuro_signal.tracking import track_attention

def main():
    parser = argparse.ArgumentParser(description="SynapTune Command Line Interface")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Load Data
    parser_load = subparsers.add_parser("load", help="Load neuro signal data from a file")
    parser_load.add_argument("--file", required=True, help="Path to the signal data file")

    # Neurofeedback
    parser_feedback = subparsers.add_parser("feedback", help="Provide neurofeedback based on signal input")
    parser_feedback.add_argument("--input", nargs="+", type=float, required=True, help="Signal input values")

    # Attention Tracking
    parser_track = subparsers.add_parser("track", help="Track attention levels")
    parser_track.add_argument("--input", nargs="+", type=float, required=True, help="Attention signal values")

    args = parser.parse_args()

    if args.command == "load":
        result = load_data(args.file)
        print(f"Loaded data: {result}")
    elif args.command == "feedback":
        result = provide_neurofeedback(args.input)
        print(f"Feedback: {result}")
    elif args.command == "track":
        result = track_attention(args.input)
        print(f"Attention Score: {result}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
