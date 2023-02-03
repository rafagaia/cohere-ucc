from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/colink/sequence", methods=["POST"])
def colink_sequence():
    # Get the request payload
    data = request.get_json()
    
    # Extract the required values from the payload
    context_prompt = data.get("context_prompt")
    user_prompt = data.get("user_prompt")
    seq = data.get("seq")
    # print(f'context_prompt: {context_prompt}\nuser_prompt: {user_prompt}\nsequence:{seq}')
    
    # Perform the colinkSequence function
    result = colinkSequence(context_prompt, user_prompt, seq)
    status_code = 200
    result = { "colink_response": "yaaaay. This our P.R. for quickest time ever to spin up a local server. Thx, OpenAI GPT!!!" }

    # Return the result
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8181)
