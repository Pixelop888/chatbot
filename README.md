# Pixel: A Time-Based Chatbot

Pixel is a command-line chatbot written in Python that changes its behaviour based on the time of day. It runs in one of three modes (morning, afternoon, night), either picked automatically from your system clock or chosen manually at startup.

## Features

- **Time-aware modes:** Morning, Afternoon and Night, each with its own behaviour.
- **Automatic mode selection:** Reads the current hour from your system clock.
- **Manual override:** Choose a mode yourself when the program starts.
- **Conversation memory:** Full chat history is sent with every request, so Pixel remembers the conversation.
- **Clean exit:** Type `exit` and Pixel says goodbye before the session ends.

## Requirements

- Python 3.10+ (uses `match` statements)
- An OpenAI API key

Packages:

```bash
pip install openai python-dotenv
```

## Setup

1. Clone the repo and open the project folder.
2. Create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Make sure `.env` is listed in `.gitignore` so your key is never pushed.

## Usage

```bash
python main.py
```

1. Type `start` to begin the conversation (anything else exits immediately).
2. Choose whether to select a mode manually (`yes` / `no`).
   - `yes`: pick 1 (Morning), 2 (Afternoon) or 3 (Night).
   - `no`: Pixel picks a mode from the current hour.
3. Chat at the `type :` prompt.
4. Type `exit` to end the conversation.

## Project Structure

```
chatbot/
├── main.py       # Chatbot logic
├── .env          # API key (not committed)
└── .gitignore
```

## How It Works

1. Reads the current hour with `datetime`.
2. Selects a mode (manual or automatic).
3. Sets up the mode's behaviour for Pixel.
4. Loops: takes your input, appends it to the history, sends the history to the model, prints the reply, and stores the reply back into the history.

## What I Learned

- **Calling an LLM API from Python:** setting up the OpenAI client and sending requests with the Responses API.
- **Managing secrets safely:** keeping the API key in a `.env` file, loading it with `python-dotenv`, and keeping it out of Git with `.gitignore`.
- **Conversation memory:** the model is stateless, so the full message history (with `developer` and `user` roles) has to be resent on every request, and the model's output appended back into it.
- **Working with `datetime`:** reading the current time and extracting the hour with `strftime` to drive program behaviour.
- **Structural pattern matching:** using `match` / `case` for mode selection, including a default case for invalid input.
- **Control flow for interactive programs:** building a `while` loop with start and exit conditions.
- **Prompt design:** shaping a chatbot's personality and behaviour through its instructions.


## Future Improvements

- Handle invalid input at the `start` prompt gracefully.
- Move mode prompts into a separate config file.
- Add error handling for network and API failures.
- Save chat history to a file between sessions.

  
## Author

**Deevyank Jain**
[GitHub]((https://github.com/Pixelop888)) | [LinkedIn]((https://www.linkedin.com/in/deevyank-jain-4759a3364/))
