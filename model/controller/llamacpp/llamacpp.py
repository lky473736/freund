# from llama_cpp import Llama
# llm = Llama(model_path="model/LLM/llama-cpp/selfrag_llama2_7b-q8_0.gguf")
# output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
# print(output)


# from llama_cpp import Llama

# llm = Llama(
#       model_path="/Users/alphastation/repository/freund/model/LLM/llama-cpp/selfrag_llama2_7b-q8_0.gguf",
#       # n_gpu_layers=-1, # Uncomment to use GPU acceleration
#       # seed=1337, # Uncomment to set a specific seed
#       # n_ctx=2048, # Uncomment to increase the context window
# )
# output = llm(
#       "Q: Name the planets in the solar system? A: ", # Prompt
#       max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
#       stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
#       echo=True # Echo the prompt back in the output
# ) # Generate a completion, can also call create_completion
# print(output)

from llama_cpp import Llama

llm = Llama(
            model_path="model/LLM/llama-cpp/selfrag_llama2_7b-q8_0.gguf",
)

def predict(instruction) :
      instruction = "Q : " + instruction + " A : "
      # print (instruction)
      output = llm(
            instruction, # Prompt
            max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
            stop=["Q :", "\n"], # Stop generating just before the model would generate a new question
            echo=True
      ) 
      
      return output

# from langchain.llms import LlamaCpp

# llm = LlamaCpp(
#     model_path="./llama-2-7b-chat.ggmlv3.q2_K.bin",
#     n_ctx=512,
#     n_batch=512,
#     n_gpu_layers=35,
#     verbose=True,
# )

# prompt = """
# Question: What are the names of the planets in the solar system? Answer:
# """
# print(llm(prompt))