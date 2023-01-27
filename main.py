import cohere


co = cohere.Client("API_KEY")

response = co.classify(
  model='large',
  examples=?,
  inputs=?
)

def random_func():
  print(Hi!)