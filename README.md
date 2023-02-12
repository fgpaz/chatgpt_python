# chatgpt_python

## Minimal requirements

* Python 3.10/3.11 already installed
* Have an API Key in [OpenAI API](openai.com/api) created

## Instructions for setting up the Script

1. Clone this Repo

2. Create an `.env` file in repository root:

    Ask me for the enviromental variables file or create one in [OpenAI API](openai.com/api) and create one `.env` file your own following `example.env` file as an example

3. Install requirements:

    ```bash
    pip3 install -r requirements.txt
    ```

    If it doesn't work use:

    ```bash
    pip3 install git+https://github.com/openai/openai-python.git dotenv
    ```

4. Run the script:

    ```bash
    python -u chatgpt.py
    ```

    To stop the script type

    ```bash
    exit
    ```

    or use `Ctrl+C`
