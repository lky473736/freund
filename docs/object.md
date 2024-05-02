### Setting of object of 'freund'
- Date : 04. 30. 2024. ~ 05. 01. 2024.
- Writer : Gyuyeon Lim (lky473736 / Gachon University, AlphaMech_)

-----

This project does totally needing and focussing on the AI model of voice detecting and recognizing the user's intension why users use this program. So, as like GPT, this machine have to react the user's command and do right thing of instructions.

#### Object

- well-recognized human voice
    - use whisper (OpenAI / https://github.com/openai/whisper)
    - But, whisper is so slow that translate human voice to lang that will be write down on gpt model.
        - **whisper must be remanufactured.**
- well-understood human's intension 
    - 1. use GPT-2 or 3 (OpenAI / https://github.com/openai/gpt-2)
        - this situation, OpenAI only provides the data of training of GPT-3, so, if i use text-based NLP model, i should use ver 2.
    - 2. use Llama (Meta / https://llama.meta.com/)
        - the alternative the gpt
        - weak than gpt, but cheap counting
- user-friendly design about web frame
    - Flask, Django will give the solution (probably)
    - Maybe i have to use server side rendering then client side rendering because of the realtime reaction about feedback of GPT.

------

#### Classify the Infrastructure

- This diagram posted on 05. 01. 2024. 

![infrastructure](<infrastructure.png>)

- **Procedure (Pseudo Code)**
    - On (online)
    - Ready to get input data 
        - check AWS working
        - check token
        - check the blacklist, number of caution
        - check the ping
        - check the user's mic
        - check whisper to send sample to model
            - answer well -> go
            - no answer -> interrupt
        - check LLM to send sample to model
            - answer well -> go
            - no answer -> interrupt
    - Input data (on voice)
    - Voice recognization
        - real-time recognization
        - The situation of recognization humans' voice is able to show on screen.
    - Detecting, preparing the repliance
        - input the input datas to LLM
    - Reply

- **Control center**
    - This can control the all procedure of program to catch error or react undefined situations. 
    - Control log and user's information will be writen in terminal during the time that user is in here.
    - Trillionly, try-catch's paradox. (maybe should use recursion call)

- **whisper (OpenAI, remanufactured)** 
    - https://www.youtube.com/watch?v=71Xh_QQtdls
    - 

- **LLM**
    - Llama
    - GPT-2
    - GPT-3

--------

#### Gaunt Chart

![gantt](<gantt.png>)