from flask_restx import Resource, Namespace
from datetime import datetime

server_ns = Namespace("Server")


@server_ns.route("/ping")
class Ping(Resource):
    def get(self):
        try:
            return {
                "status": "success",
                "message": "pong!",
            }, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500


@server_ns.route("/time")
class Time(Resource):
    def get(self):
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return {"status": "success", "server_time": current_time}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
