

from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("./ds4q.gguf", model_type="gguf")

print(llm("AI is going to"))