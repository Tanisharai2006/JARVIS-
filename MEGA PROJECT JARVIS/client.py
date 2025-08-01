#defaults to getting the key using os.enviornment.get("OpenAI_API_KEY")
# if you saved the key under a different environment variable name ,you can do something like
#  client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME")),
# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)
