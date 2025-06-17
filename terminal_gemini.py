import json
import subprocess
import sys

def check_for_key():
    try:
        with open("API.txt", "r") as file:
            api_key = file.readline().strip()
            if api_key:
                file.close()
                return api_key
    except FileNotFoundError:
        pass
    api_key = input("Paste your GEMINI API key (https://aistudio.google.com/apikey): \n").strip()
    with open("API.txt", "w") as file:
        file.write(api_key)
        file.close()
    return api_key

def build_prompt(input_text, api_key):
    prompt = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Explain how AI works in a few words"
                    }
                ]
            }
        ]
    }

    prompt["contents"][0]["parts"][0]["text"] = input_text
    call = f"""curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}" \\
    -H 'Content-Type: application/json' \\
    -X POST \\
    -d '{json.dumps(prompt)}'"""

    return call

def request_and_parse(call):
    try:
        result = subprocess.run(call, shell=True, capture_output=True, text=True)
        response_json = json.loads(result.stdout)
        text = response_json["candidates"][0]["content"]["parts"][0]["text"]
        return text
    except ConnectionError as e:
        print(e + " Exiting...")
    return None

def parse_args_for_output():
    output_file = None
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == "-o" and i + 1 < len(args):
            output_file = args[i + 1]
    return output_file


def parse_args():
    output_file = None
    prompt_text = None
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-o" and i + 1 < len(args):
            output_file = args[i + 1]
            i += 2
        else:
            prompt_text = args[i]
            i += 1
    return prompt_text, output_file

def main():
    
    api_key = check_for_key()    
    input_text, output_file = parse_args()
    
    if not input_text:
        print("""
████████╗    ██████╗ ███████╗███╗   ███╗██╗███╗   ██╗██╗
╚══██╔══╝   ██╔════╝ ██╔════╝████╗ ████║██║████╗  ██║██║
   ██║█████╗██║  ███╗█████╗  ██╔████╔██║██║██╔██╗ ██║██║
   ██║╚════╝██║   ██║██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║
   ██║      ╚██████╔╝███████╗██║ ╚═╝ ██║██║██║ ╚████║██║
   ╚═╝       ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ v1.0
                                                        
""")
        input_text = input("Prompt: ")   

    response = request_and_parse(build_prompt(input_text, api_key))
    print("\n" + response + "\n")

    if output_file:
        with open(output_file, "w") as file:
            file.write("Prompt: " + input_text + "\n\n" + "Response: " + response)
        file.close

if __name__ == "__main__":
    main()