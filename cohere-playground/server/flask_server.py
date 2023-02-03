from flask import Flask, request, jsonify
from subprocess import Popen, PIPE
import multiprocessing
import os
from dotenv import load_dotenv

load_dotenv("./.env")
API_KEY = os.getenv("API_KEY")

import sys

sys.path.append("/Users/xperience/cohere-hackathon/cohere-playground/src")

from cohereService import cohere_start

app = Flask(__name__)

@app.route("/colink/sequence", methods=["POST"])
def colink_sequence():
    # Get the request payload
    data = request.get_json()
    
    # Extract the required values from the payload
    context_prompt = data.get("context_prompt")
    user_prompt = data.get("user_prompt")
    arr_prompts = [context_prompt, user_prompt]
    seq = [('pg', 2)]# data.get("seq")
    model_size = data.get("model_size")
    # print(f'context_prompt: {context_prompt}\nuser_prompt: {user_prompt}\nsequence:{seq}')
    
    print("forking process")
    colink_process = multiprocessing.Process(
        target=cohere_start,
        args=(API_KEY,model_size, seq, arr_prompts)
    )
    colink_process.start()
    # colink_process.join()

    # @TODO: based on colinkSequence complexity, can we provide an estimate wait time for the
    # user check back if result is ready?

    # Perform the colinkSequence function
    # result = colinkSequence(context_prompt, user_prompt, seq)
    status_code = 200
    result = { "colink_response": "We received your request. We're on it. Send a GET /colink/new?id=4 request in a few minutes to obtain results" }

    # Return the result
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181)
