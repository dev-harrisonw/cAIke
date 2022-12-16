import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

class Cake:
    def __init__(self, flour, sugar, eggs, cake_type):
        self.flour = flour
        self.sugar = sugar
        self.eggs = eggs
        self.cake_type = cake_type
        
    def gather_ingredients(self):
        print(f"Gathering ingredients for a {self.cake_type} cake: {self.flour} cups of flour, {self.sugar} cups of sugar, and {self.eggs} eggs")
        
    def get_baking_instructions(self):
        # Use GPT-3 to generate baking instructions for the specified cake type
        prompt = f"How to bake a {self.cake_type} cake"
        model_engine = "text-davinci-002"
        completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
        message = completion.choices[0].text
        print(message)

# Define some premade cake objects
chocolate_cake = Cake(2, 1, 4, "chocolate")
vanilla_cake = Cake(2, 1, 3, "vanilla")
lemon_cake = Cake(3, 1.5, 4, "lemon")

# Ask the user to choose a cake
print("Please choose a cake:")
print("1. Chocolate Cake")
print("2. Vanilla Cake")
print("3. Lemon Cake")
choice = int(input())

# Choose the cake based on the user's input
if choice == 1:
    cake = chocolate_cake
elif choice == 2:
    cake = vanilla_cake
elif choice == 3:
    cake = lemon_cake
else:
    print("Invalid choice")

cake.gather_ingredients()
cake.get_baking_instructions()
