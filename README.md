# overview

‘coLink’ is an API-as-a-service bridge between clients and CohereAPI to scale NLP access to small and medium sized businesses in South America.


# Run a colink sequence
...
------------------------------------------------
/POST /colink/sequence
------------------------------------------------
Requese body JSON {
    "context_prompt": "adventures of Huckleberry Finn or as it is known in more recent editions, The Adventures of Huckleberry Finn, is a novel by American author Mark Twain, which was first published in the United Kingdom in December 1884 and in the United States in February 1885.",
    "user_prompt": "text summarize Huckleberry Finn",
    "seq": "[('pg',10)]",
    "model_size": "medium"
}
Will perform 10 cycles of Cohere Generate.

Response: colink_id, use in GET request within few minutes for result
------------------------------------------------
...
------------------------------------------------
/GET /colink/new?id=4
------------------------------------------------

Response: your colink sequence response with colink_id
------------------------------------------------



# Future work:
  - Sequence to allow layering:
      [('pg',5), ('pc',1), ('pg',2), ('pe',1)]
      Link text generate to a classification, to generate, to embedding

