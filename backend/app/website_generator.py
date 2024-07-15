import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class WebsiteGenerator:
    def __init__(self, model_name="codellama/CodeLlama-7b-hf"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_code(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        output = self.model.generate(
            input_ids, 
            max_length=1000, 
            num_return_sequences=1, 
            temperature=0.7
        )

        generated_code = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_code