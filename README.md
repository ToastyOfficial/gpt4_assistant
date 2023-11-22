# OpenAI Assistant
![ai](https://i.imgur.com/xwNwqD9.png)<br><br>
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ToastyOfficial/gpt4_assistant?label=Version"> [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)  [![GitHub latest commit](https://badgen.net/github/last-commit/ToastyOfficial/gpt4_assistant)](https://GitHub.com/ToastyOfficial/gpt4_assistant/commit/) [![GitHub stars](https://badgen.net/github/stars/ToastyOfficial/gpt4_assistant)](https://GitHub.com/ToastyOfficial/gpt4_assistant/stargazers/) <br>
An AI assistant powered by OpenAI ChatGPT4<br>
> *Note that this branch may not be stable please use releases*<br>
- Type to `F.R.I.D.A.Y.` and get typed responses
- Talk to `F.R.I.D.A.Y.` and get verbal responses
### Known Bugs

- [X] Calling ai whisper models on an M1 or M2 Mac CPU outputs an error every time

### Next Patch
- [X] Fully offline assistant
- [ ] Basic action functions _(windows)_
- [ ] Model Training
- [X] Linux & MacOS documentation
- [X] Improved stabilty & permormance

## Installation

**1.** First, clone the the repo to your machine.
**2.** Next, install [Anaconda](https://www.anaconda.com/download) and run as `administrator` to install dependencies.
**3.** Then, install [GPT4All](https://gpt4all.io/) desktop app & dwonload `GPT4All Falcon` wait until done to continue.<br>


## Dependencies
### Install the `GPT4All` Library
```
python -m pip install gpt4all
```
### Install the `OpenAI Whisper` Library
```
python -m pip install openai-whisper
```
### Install the `Speech Recognition` Library
```
python -m pip install SpeechRecognition
```
### Install the `PlaySound` Library
```
python -m pip install playsound
```
### Install the `PyAudio` Library
```
python -m pip install PyAudio
```
### Install the `Sound File` Library
```
python -m pip install soundfile
```
### Install `ffmpeg` for Windows using Chocolatey
```
choco install ffmpeg
```
### For `MacOS` Users
```
brew install portaudio
```
### For `Windows/Linux` Users
```
python -m pip install pyttsx3
```


## Configuration
> To use Friday you need to app your OpenAI API Key `openai.api_key = "KEY_HERE"`

The `duration` variable can be raised for more time to respond to the AI. Default is 2 seconds
```py
def start_listening():
    with source as s:
        r.adjust_for_ambient_noise(s, duration=2)
        print('\nSay', wake_word, 'to get started. \n')
```
Got an issue? Submit a pull request or submit an issue!<br>
> **Developed by Toasty | Facekick x Dawnstar**
