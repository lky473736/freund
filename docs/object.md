### Setting of object of 'freund'
- Date : 04. 30. 2024.
- writer : Gyuyeon Lim (lky473736, Procedure Institute)

-----

This project does totally needing and focussing on the AI model of voice detecting and recognizing the user's intension why users use this program. So, as like GPT, this machine have to react the user's command and do right thing of instructions.

**Object**

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

**mission**

- create the backlog (in this week)