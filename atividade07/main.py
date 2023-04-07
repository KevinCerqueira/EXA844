from flask import Flask, request
import json
import time
import pymysql

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_http():
    request_json = request.get_json(silent=True)
    request_args = request.args

    response = {}
    if request_json and 'action' in request_json and request_json['action'] == "put":
        try:     
            conn = pymysql.connect(   
                host="172.106.0.111",
                port=3306,
                user="default_1337",
                password="J7O7xB19Vf67w1#s",
                db="uefs_calender",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:
                    message = request_json['message']
                    autor = request_json['autor']
                    date = time.strftime('%Y-%m-%d %H:%M:%S')                    
                    cursor.execute("INSERT INTO blog (message, autor, date) VALUES ('{}','{}','{}');".format(message, autor, date))
                    conn.commit()
                    response["message"] = "put executed successfully"     
        except Exception as e:
            response["message"] = 'Error: {}'.format(str(e))            
    elif request_args and 'action' in request_args and request_args['action'] == "get":
        try:     
            conn = pymysql.connect(   
                host="172.106.0.111",
                port=3306,
                user="default_1337",
                password="J7O7xB19Vf67w1#s",
                db="uefs_calender",
                cursorclass=pymysql.cursors.DictCursor
            )

            with conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM blog;")
                    result = cursor.fetchall()
                    if result:
                        for row in result:
                            row['date'] = row['date'].strftime('%Y-%m-%d %H:%M:%S')
                        response["result"] = json.dumps(result)
                    else:
                        response["message"] = "no results found"
        except Exception as e:
            response["message"] = 'Error: {}'.format(str(e))
    else:
        response["message"] = "action missing or with wrong value!"
    
    return json.dumps(response)

if __name__ == "__main__":
    app.run()
