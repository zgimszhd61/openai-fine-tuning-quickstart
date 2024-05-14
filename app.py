from openai import OpenAI
import os,re
## 参考内容:https://platform.openai.com/docs/guides/fine-tuning/use-a-fine-tuned-model
os.environ["OPENAI_API_KEY"] = "sk-proj-"
client = OpenAI()

# response = client.files.create(
#   file=open("mydata.jsonl", "rb"),
#   purpose="fine-tune"
# )

# print(response)

# response2 = client.fine_tuning.jobs.create(
#   training_file="file-XLjt1MzshGC0ykf03de6XTXB", 
#   model="gpt-3.5-turbo"
# )

# print(response2)


# List 10 fine-tuning jobs
print(client.fine_tuning.jobs.list(limit=10))

# Retrieve the state of a fine-tune
# client.fine_tuning.jobs.retrieve("ftjob-abc123")