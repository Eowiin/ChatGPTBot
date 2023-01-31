import os
import openai

API_KEY = os.getenv("OPENAI_APIKEY")
MODEL = "text-davinci-003"
TEMPERATURE = 1
MAX_TOKEN = 256
TOP_P = 1
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0

def displayResponse(response):
    print("Response :")
    if "choices" in response.keys():
        for text in response["choices"]:
            print(text["text"])
    else:
        print("Choices key missing, no output.")

def getResponse(userInput):
    response = openai.Completion.create(
        model=MODEL,
        prompt=userInput,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKEN,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY
    )
    return response

def formatInputUser(userInput):
    formatInput = '"""\n' + userInput + '\n"""'
    return formatInput

def getInputUser():
    while (True):
        try:
            userInput = input()
        except:
            break
        userInput = formatInputUser(userInput)
        response = getResponse(userInput)
        displayResponse(response)

def main():
    openai.api_key = API_KEY
    getInputUser()

if __name__ == "__main__":
    main()