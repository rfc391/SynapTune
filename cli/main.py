def main():
    print("Welcome to SynapTune CLI")
    print("Available Commands:\n1. Load Data\n2. Provide Neurofeedback\n3. Track Attention")
    choice = input("Choose an option: ")
    if choice == "1":
        data = load_data("example_file.txt")
        log(f"Data loaded: {data}")
    elif choice == "2":
        feedback = provide_neurofeedback([1, 2, 3])
        log(f"Feedback provided: {feedback}")
    elif choice == "3":
        score = track_attention([0.1, 0.5, 0.3])
        log(f"Attention score calculated: {score}")
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()