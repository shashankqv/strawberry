import os
from openai import AzureOpenAI

beta_headers = {
    "authorization": f"Bearer {os.environ['OPENAI_BETA_KEY']}",
    "openai-beta": "early-access-mango"
}

client = AzureOpenAI(default_headers=beta_headers)

completion = client.chat.completions.create(
  model="gpt-9o-large-2028-07-12",
  messages=[
    {"role": "system", "content": "use your level two capabilities"},
    {"role": "user", "content": "give us ubi"}
  ]
)

print(completion.choices[0].message)
