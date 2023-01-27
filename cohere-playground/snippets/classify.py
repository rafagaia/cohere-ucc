import os
import cohere

co = cohere.Client("VRDuaNCB4wqFReyPvaCdRT65Sd62ea8Dc4CdfGhl")

from cohere.classify import Example


examples=[
  Example("Example 1", "Label 1")
]

inputs=["Example Query 1",
        "Example Query 2"
        ]

response = co.classify(
    model='medium',
    inputs=inputs,
    examples=examples
)

print('Classification: {}'.format(response.classifications))

# if __name__ == '__main__':
#     