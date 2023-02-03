# Overview

‘coLink’ is an API-as-a-service bridge between clients and CohereAPI to scale NLP access to small and medium sized businesses in South America.
</br>


# Setup

- add file ".env" -> /cohere-playground/.env </br>
    -   with variable API_KEY=yourApiKeyToTestDemo </br>
</br>

# Run a coLink Sequence


</br>
</br>
--------------------------------------------
/POST /colink/sequence
--------------------------------------------</br>
Request body JSON {</br>
    "context_prompt": "adventures of Huckleberry Finn or as it is known in more recent editions, The Adventures of Huckleberry Finn, is a novel by American author Mark Twain, which was first published in the United Kingdom in December 1884 and in the United States in February 1885.",</br>
    "user_prompt": "text summarize Huckleberry Finn",</br>
    "seq": "[('pg',10)]",</br>
    "model_size": "medium"</br>
}</br>
Will perform 10 cycles of Cohere Generate.
</br>
Response: colink_id, use in GET request within few minutes for result
</br>
</br>
</br>
--------------------------------------------
/GET /colink/new?id=4
--------------------------------------------</br>
Response: your colink sequence response, of colink_id emitted from /POST /colink/sequence route
</br>
</br>
</br>



# Future work:
  - Sequence to allow layering:</br>
      [('pg',5), ('pc',1), ('pg',2), ('pe',1)]</br>
      Link text generate to a classification, to generate, to embedding

