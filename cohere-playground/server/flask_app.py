import os
import ast
import sys
import multiprocessing
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from subprocess import Popen, PIPE

load_dotenv("./.env")
API_KEY = os.getenv("API_KEY")

#@TODO apply relative path
sys.path.append("/Users/xperience/ucc-team/coLink/cohere-playground/src")

from cohereService import cohere_start

app = Flask(__name__)


@app.route("/colink/status/new", methods=["GET"])
def show_new_colink_result():
    data = request.get_json()

    # @TODO pass/read colink_id from params instead of request body
    colink_id = data.get("colink_id")
    # If sequence is completed, response will exist in database
    # else:
    status_code = 201
    if colink_id == 4:
        return jsonify({"bro":"Go take a shower", "sis": "go be more beautiful"}), status_code
    status_code = 404
    result = {"result": f'your colink response with id:{colink_id} is not yet ready. Check again in 2-3 minutes.'}
    return jsonify(result), status_code


@app.route("/colink/sequence", methods=["POST"])
def colink_sequence():
    # Get the request payload
    data = request.get_json()
    
    # Extract the required values from the payload
    context_prompt = data.get("context_prompt")
    user_prompt = data.get("user_prompt")
    arr_prompts = [context_prompt, user_prompt]
    seq = ast.literal_eval(data.get("seq"))
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
    #   user check back if result is ready?

    status_code = 200
    result = { "colink_response": "We received your request. We're on it. Send a GET /colink/new?id=4 request in a few minutes to obtain results" }

    # Return the result
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181)
