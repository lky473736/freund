import transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "NousResearch/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(
    model_id
)
# model = AutoModelForCausalLM.from_pretrained(
#    model_id,
#     device_map="auto",
#     torch_dtype="auto",
# )
model = AutoModelForCausalLM.from_pretrained(model_id,
                                             return_dict=True,
                                             torch_dtype='auto',
                                             device_map='auto',
                                             do_sample=True,
                                             # load_in_8bit=True,
)

text = """
고양이의 조상이 어느 동물이야?
"""

chat = [
    { "role": "system", "content": " You are an artificial intelligence assistant that answers in Korean." },
    { "role": "user", "content": f"{text}" },
]

prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        max_new_tokens=256,
        eos_token_id=[
            tokenizer.eos_token_id,
            tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ],
    )
    
output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1) :], skip_special_tokens=True)

print(output)