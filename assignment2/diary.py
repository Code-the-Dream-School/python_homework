import traceback

def main():
 try:
    with open('diary.txt', 'a') as file:
        prompt = 'What happened today?'
        while True:
            line = input(prompt)
            file.write(line + "\n")
            if line.strip() == 'done for now':
             break
            prompt= "What else?"
 except Exception as e:
    print("An exception occurred")
    print(f"Exception type: {type(e).__name__}")
    traceback.print_exc()

if __name__ == "__main__":
        main()