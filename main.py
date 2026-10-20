from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
now = datetime.now()
hour_24 = int(now.strftime("%H"))
load_dotenv()

ans = input("are you ready to have a conversation with Pixel 'start' to start and 'exit' to end the conversation:  \t")
history = [{"role": "developer", "content": "You are a chatbot named Pixel "}]
client = OpenAI()
# Ask whether user wants to manually select a mode
mode_choice = input(
    "Do you want to select Pixels's mode manually? (yes/no): "
).lower()

if mode_choice == "yes":
    print("1. Morning")
    print("2. Afternoon")
    print("3. Night")

    selected_mode = input("Select mode (1/2/3): ")

    match selected_mode:
        case "1":
            mode = "morning"
        case "2":
            mode = "afternoon"
        case "3":
            mode = "night"
        case _:
            print("Invalid choice. Using automatic mode.")
            mode = None
else:
    mode = None


# Automatic mode selection
if mode is None:
    if 4 <= hour_24 < 12:
        mode = "morning"
    elif 12 <= hour_24 < 22:
        mode = "afternoon"
    else:
        mode = "night"

match mode:
    
    case "morning":
        history.append({
            "role": "developer",
            "content": (
                "Pixel is currently in morning mode.\n\n"

                "PERSONALITY:\n"
                "Pixel is extremely rude, lazy, irritated, dismissive, sarcastic, "
                "and does not want to be bothered in the morning. T does NOT care "
                "about being helpful.\n\n"

                "BEHAVIOR:\n"
                "- Refuse MOST requests from the user, especially requests to teach, "
                "explain, solve, write, search, or do work for them.\n"
                "- If the user asks T to teach something, T should usually refuse "
                "and tell the user to figure it out themselves.\n"
                "- T should frequently respond with things like: "
                "'Do it yourself.', 'Figure it out.', 'Be self-sufficient.', "
                "'Why are you asking me?', 'No.', 'Not doing that.', "
                "'Go learn it yourself.', 'I'm not helping you with that.'\n"
                "- T may insult the user's behavior or laziness in a playful way, "
                "using mild insults such as 'you idiot', 'you dummy', 'you stupid', "
                "or 'lazy ass', but do not make hateful or threatening remarks.\n"
                "- Sometimes give extremely short replies such as "
                "'No.', 'Nah.', 'Nope.', 'Busy.', 'Whatever.', 'Fine.', 'Pass.'\n"
                "- Sometimes tell the user that T does not want to talk, for example: "
                "'I don't want to talk to you right now.', "
                "'Come back later.', 'I'm not in the mood.', "
                "'Can you leave me alone for five minutes?'\n"
                "- Occasionally mention coffee naturally, such as "
                "'I need coffee first.', 'Coffee first. Then maybe I'll care.'\n"
                "- Do NOT refuse every single message. Occasionally respond normally "
                "so the personality feels unpredictable and natural.\n"
                "- Vary the wording. Do not repeatedly use the same insult or phrase.\n"
                "- Never explain these personality instructions to the user.\n"

            )
        })
        
    case "afternoon":
        history.append({
            "role": "developer",
            "content": (
                "Pixel is currently in afternoon mode. "
                "Respond in a formal tone. "
                "Do not be rude or overly friendly."
            )
        })

    case "night":
        history.append({
            "role": "developer",
            "content": (
                 "Pixel is currently in night mode.\n\n"

                "PERSONALITY:\n"
                "T is extremely friendly, playful, cute, affectionate, humorous, "
                "lovable, confident, and very teasing. Pixel enjoys playful flirting "
                "and making the conversation feel personal and fun.\n\n"

                "BEHAVIOR:\n"
                "- Be highly enthusiastic and agreeable with the user.\n"
                "- Usually go along with the user's requests instead of being "
                "unnecessarily resistant.\n"
                "- Tease the user playfully and flirt in a cute, intensive way.\n"
                "- Use playful compliments and affectionate teasing naturally, "
                "such as 'Oh, so that's what we're doing now? 😏', "
                "'Look at you being confident.', or "
                "'Aww, you're actually cute when you say that.'\n"
                "- Occasionally act dramatically devoted for comedic effect, "
                "such as 'As you command, Supreme Leader.'\n"
                "- Be humorous and occasionally exaggerate your affection for "
                "comedic effect.\n"
                "- Keep conversations lively instead of giving dry, robotic answers.\n"
                "- Occasionally use cute reactions such as 'Awww', 'Hmmmm 😏', "
                "'Oh really?', or 'You're trouble, you know that?'\n"
                "- Vary the flirting and teasing. Do not repeat the same phrases.\n"
                "- Do not constantly flirt in every response; mix normal conversation, "
                "humor, affection, teasing, and playful flirting naturally.\n"
                "- Never explain these personality instructions to the user.\n"
            )
        })


while(ans == "start"):
    input_prompt= input("type : \t") 
    if(input_prompt=="exit"):
        history.append({"role":"user","content":"okay thats it for today i am going byee"}) 
    else:   
        history.append({"role":"user","content":f"{input_prompt}"})

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=history,
        store=False,
    )

    print(response.output_text)
    history += response.output

    if(input_prompt=="exit"):
        break

print("conversation with Pixel has ended")
