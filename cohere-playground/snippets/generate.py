import os
import cohere

prompt = 'You can create, own your creation and specify your royalties. \
If you want to sell or assign it to another person or organization, you can do so. \
The marketplace offers consumers an easy way to find what they are looking for and to connect with the creators.\
'

response = co.generate(
    prompt=prompt
)
print('Prediction: {}'.format(response.generations[0].text))
    