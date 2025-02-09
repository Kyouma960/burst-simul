from flask import Flask, request, jsonify
import transaction, endorse
from utils.verify import signature_verify, wallet_verify
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def handle_post():

    data =request.get_json()
    if not data:
        return 400

    if not (signature_verify.is_valid(data) and wallet_verify.is_valid(data)):
        return 400

    response = {
            "message": "Recieved",
            }

    if (data.get("type")=="transaction"):
       transaction.transact(data) 


    elif (data.get("type")=="endorse"):
        endorse(data) 

    else:
        response = {
                "message": "Incorrect format",
                }

    return jsonify(response), 200


#@app.route('/get', methods=['GET'])
#def handle_get():



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4757)
