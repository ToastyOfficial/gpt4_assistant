# OpenAI Assistant
![ai](https://i.imgur.com/xwNwqD9.png)<br><br>
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)  [![Latest release](https://badgen.net/github/release/ToastyOfficial/OpenAI_GPT4_Assistant)](https://github.com/ToastyOfficial/OpenAI_GPT4_Assistant/releases) [![GitHub latest commit](https://badgen.net/github/last-commit/ToastyOfficial/OpenAI_GPT4_Assistant)](https://GitHub.com/ToastyOfficial/OpenAI_GPT4_Assistant/commit/) [![GitHub stars](https://badgen.net/github/stars/ToastyOfficial/OpenAI_GPT4_Assistant)](https://GitHub.com/ToastyOfficial/OpenAI_GPT4_Assistant/stargazers/)<br>
An AI assistant powered by OpenAI ChatGPT4
- Type to `F.R.I.D.A.Y.` and get typed responses
- Talk to `F.R.I.D.A.Y.` and get verbal responses

## Dependencies
- Anaconda
- GPT4All Plugin
- Whisper Plugin
- Speech Recognition Plugin
- Play Sound Plugin
- PyAudio Plugin
- SoundFile Plugin

# Installation
First install Anaconda and run as `administrator`
```https://www.anaconda.com/download```
## Configuration
> To use Friday you need to app your OpenAI API Key
`openai.api_key = "KEY_HERE"`
## Times
The `duration` variable can be raised for more time to respond to the AI. Default is 2 seconds
```py
def start_listening():
    with source as s:
        r.adjust_for_ambient_noise(s, duration=2)
        print('\nSay', wake_word, 'to get started. \n')
```
Got an issue? Submit a pull request or submit an issue!<br>
> **Developed by Toasty | 614 eShop x Dawnstar**
