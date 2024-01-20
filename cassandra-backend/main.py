from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama
from transformers import AutoTokenizer




checkpoint = "HuggingFaceH4/zephyr-7b-beta"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


system_sql_prompt = """
You are an sql expert, given an input you will only create a syntactically correct query. you won't chat with the user you will only
create an appropriate sql query. you must query all of the columns using `*`. be careful not use names that don't exist in the table
schema described below. pay attention to the comments in the table schema.
make sure the name of the tables and columns that you are using are from the table schema.

the table schema:
CREATE TABLE "internetpackages" (
	"id"	INTEGER NOT NULL,
	"package_name"	VARCHAR(255) NOT NULL, -- name of the internet package
	"days_available"	INTEGER NOT NULL, -- number of days the package will be available after purchase
	"price"	INTEGER NOT NULL, -- price of the package in toman
	"data_size_in_mb"	INTEGER NOT NULL, -- size of the internet data in mega bytes.
	"vendor"	VARCHAR(255) NOT NULL, -- the vendor that is selling this internet package
	"number_of_purchases"	INTEGER NOT NULL, -- number of purchases for this package
	"price_per_mb"	REAL, -- price per mega byte ratio, showing how much the vendor is charging per mb
	PRIMARY KEY("id")
);

"""

system_func_prompt = """
Given the user's input you will return one of the functions below with its appropriate inputs in json format.
use the following format for the json you return:
{
  "function": "function name",
  "inputs": [
    "input name": "value"
  ]
}

=== Available functions ===
[
  {
    "function": "get_most_popular"
    "inputs" : None
  },
  {
    "function": "get_most_economic"
    "inputs" : None
  },
  {
    "function": "search_packages"
    "inputs" : [
      "days_available": "integer input like 3 or 4"
      "lowest_price": "lowest price the user wants, can be None or an integer",
      "highest_price": "highest price the user wants, can be None or an integer",
      "vendor": "the vendor that the user wants to buy from, can be None or string",
      "lowest_data_size": "lowest data size the user wants, should be in megabytes, can be None",
      "highest_data_size": "highest data size the user wants, should be in megabytes, can be None",
    ]
  },
  {
    "function": "general_info_on_packages",
    "inputs" None
  }
]

"""





llm = Llama(model_path="./zeph.gguf", n_ctx=5000, verbose=True)

app = Flask(__name__)

cors = CORS(app)

@app.route('/api/message', methods=['POST'])
def get_text():
    data = request.get_json()
    print(f"rcvd {data}")
    messages = [
      {
        "role": "system",
        "content": system_func_prompt
      },
      {
        "role": "user",
        "content": data['msg'] + ".don't explain and ONLY return the appropriate json. if there are no functions approriate for it say 'I'm sorry, I don't know'"
      }
    ]
    tokenized_chat = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
    preprocessed_chat = tokenizer.decode(tokenized_chat)
    print(f"giving the following prompt to the llm:\n{preprocessed_chat}")
    response = llm.create_completion(preprocessed_chat, max_tokens=128, temperature=0)
    print(f"llm response:\n{response}")
    resp_msg = response['choices'][0]['text']
    print(f"sending back [{resp_msg}]")
    return jsonify({'msg': resp_msg}), 201

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=6969)