import json
import difflib

# Load pre-set questions and answers from JSON file
def load_data():
    with open('qa_data.json', 'r') as file:
        return json.load(file)

# Save new question and answer to JSON file
def save_data(question, answer):
    data = load_data()
    data[question] = answer
    with open('qa_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Find best match for the user question
def find_best_match(question, data):
    best_match = difflib.get_close_matches(question, data.keys(), n=1, cutoff=0.99)
    if best_match:
        return data[best_match[0]]
    else:
        return None

# Main function to handle user interaction
def main():
    while True:
        data = load_data()
        x = 0

        # Run loop for 7 iterations
        while x < 7:
            user_question = input("You: ").lower()

            # Check if the question already exists in the data
            if user_question in data:
                print("Chatbot:", data[user_question])
            else:
                # Check for a best match if the question doesn't exist
                best_match_answer = find_best_match(user_question, data)
                if best_match_answer:
                    print("Chatbot: I'm not sure about that. Did you mean:", best_match_answer)
                else:
                    print("Chatbot: I'm not familiar with that question. Could you please teach me?")
                    user_answer = input("You: ")
                    save_data(user_question, user_answer)
                    print("Chatbot: Thank you! I'll remember that.")

            x += 1  # Increment after each interaction

        # Ask if the user wants to continue after 7 iterations
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            break  # Exit the main loop if the user says 'no'

if __name__ == "__main__":
    main()
