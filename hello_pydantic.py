#!/usr/bin/env python
#
# hello_pydantic_ollama.py
#


from pydantic import BaseModel, Field

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.output import NativeOutput
from pydantic_ai.providers.ollama import OllamaProvider


# 1. Define the exact shape of the data you want back
class MovieReview(BaseModel):
    title: str = Field(description="The name of the movie")
    sentiment: str = Field(description="Must be either 'Positive', 'Negative', or 'Neutral'")
    summary: str = Field(description="A brief 1-sentence summary of the review")

# 2. Configure the Ollama model
# By default, this connects to http://localhost:11434/v1
#base_url = "http://localhost:11434/v1"

ollama_model = OllamaModel(
    model_name="qwen2.5:7b-instruct",
    provider=OllamaProvider(base_url='http://localhost:11434/v1'),
)

# 3. Define the agent and tell it exactly what type of structured output to yield
agent = Agent(
    model=ollama_model,
    output_type=NativeOutput(MovieReview),
    #result_type=MovieReview,  # Forces Ollama to conform strictly to this Pydantic schema
    system_prompt="You are an expert movie critic. Extract the core details from the provided review text."
)

# 4. Run the agent synchronously
review_text = "Honestly, Interstellar was a masterpiece. The visual effects were breathtaking and the score by Hans Zimmer was out of this world, even if the plot got a bit messy at the end."

result = agent.run_sync(user_prompt=review_text)

# 5. Access your fully-validated Pydantic data
print(f"output: {result.output}")
print()
print(f"Title: {result.output.title}")
print(f"Sentiment: {result.output.sentiment}")
print(f"Summary: {result.output.summary}")
print(f"\nFull validated model: {result.output.model_dump_json(indent=2)}")


