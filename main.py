from flask import Flask, request, jsonify
from mysql.connector import Error
from datetime import datetime
import json
from db import add_db, get_data_by_date

def is_numeric(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def has_only_letters(input_string):
    return input_string.strip().isalpha()


def is_timestamp(input_string):
    try:
        datetime_obj = datetime.fromtimestamp(float(input_string))
        return True
    except ValueError:
        return False
    
    
def split_into_triplets(text):
    try:
        words = text.split()
        return [words[i:i + 3] for i in range(0, len(words), 3)]
    except ValueError:
        return False
        
app = Flask(__name__)

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.data.decode("utf-8")
    triple = split_into_triplets(data)
    
    if triple:
      for checking in triple:

         if len(checking)==3  and all([is_timestamp(checking[0]), has_only_letters(checking[1]), is_numeric(checking[2])]):
             pass
         else :
             return jsonify({"success": "False"}), 200
     
      if add_db(triple):      
         return jsonify({"success": "True"}), 200
      else :
         return jsonify({"success": "Can not connect to db"}), 200
    else:
          return jsonify({"success": "No Data"}), 200


@app.route("/data", methods=["GET"])
def send_data():
    to_ = request.args.get('to', '')
    from_ = request.args.get('from', '')  
    result=  get_data_by_date(from_,to_)
    json_data = []
    if result:
      for data in result:

         json_data.append({"time": str(data[1]), "name" :data[2],"value": data[3]})
    
      print(json_data)

      js_for_send = json.dumps(json_data)
      return  jsonify(json_data) , 200
    else:
      return jsonify({"success": "Cant connect to db"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
