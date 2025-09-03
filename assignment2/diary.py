# diary.py
import traceback

def main():
    try:
        with open("diary.txt", "a") as f:
            prompt = "What happened today? "
            while True:
                line = input(prompt)
                f.write(line + "\n")
                if line == "done for now":
                    break
                prompt = "What else? "
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

if __name__ == "__main__":
    main()

