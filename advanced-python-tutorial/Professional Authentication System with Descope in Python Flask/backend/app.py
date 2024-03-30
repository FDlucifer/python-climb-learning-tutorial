# https://www.descope.com/
# https://github.com/descope-sample-apps/react-python-sample-app
# npx create-react-app frontend
# npm install --save @descope/react-sdk
# pip install flask flask_cors descope

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from descope import REFRESH_SESSION_TOKEN_NAME, SESSION_TOKEN_NAME, DescopeClient

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "hello world, this is public information"

@app.route("/protected", methods=["GET"])
def protected_assets():
    session_token = request.headers["Authorization"].split(" ")[1]
    try:
        descope_client = DescopeClient(project_id="P2OpNC7JkEtqRncpogUpR8KR74sO")
        descope_client.validate_session(session_token=session_token)
        print("successful validation!!!")

        response = make_response(
            jsonify(
                {"message": "secret code: descope rocks", "serverity": "danger"}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    except:
        print("validation failed")
        response = make_response(
            jsonify(
                {"message": "not allowd", "serverity": "danger"}
            ),
            401,
        )
        response.headers["Content-Type"] = "application/json"
        return response

if __name__ == "__main__":
    app.run(port=8080)

