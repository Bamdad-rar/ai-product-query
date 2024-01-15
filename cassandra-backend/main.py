from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama

sql_prompt = """
Instruction: You are sqlite3 expert. Given an input question, you create only a syntactically correct sqlite3 query and nothing else. 
Unless the user specifies in the question a specific number of examples to obtain, query for at most 3 results using the LIMIT clause.
You must query using all of the columns to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. 
Be careful to not query for columns that do not exist. 
Also, pay attention to which column is in which table.
Pay attention to use today() function to get the current date, if the question involves "today".
`ORDER BY` clause should always be after `WHERE` clause. 
DO NOT add semicolon to the end of SQL. 
Pay attention to the comment in table schema. 
Make sure the name of the tables and columns that you are using are from the table schema.
Make sure that you write only and only sql, nothing more nothing less.

=== Table Schema ===

CREATE TABLE "IrancellPackages" (
	"package_name"	TEXT,
	"package_id"	INTEGER,
	"validity_period_days"	INTEGER, -- the package is usable for this number of days
	"usable_time_start"	INTEGER, -- the start time of when the package becomes usable during the day
	"usable_time_end"	INTEGER, -- the end time of when the package becomes usable during the day
	"data_size_mb"	INTEGER, -- size of the package data in megabytes
	PRIMARY KEY("package_id")
);

Question: %s
Output:
"""

func_prompt = """
As an AI assistant, please select the most suitable function and parameters from the list of available functions below, based on the user's input. Provide your response in JSON format.

Input: I want to know how many times 'Python' is mentioned in my text file.

Available functions:
query_database:
  description: This function does selects on a table.
  params:
    action: The operation we want to perform on the data, such as "count_occurrences", "find_line", etc.
    filters:
      keyword: The word or phrase we want to search for.

"""


llm = Llama(model_path="./phi-2.gguf", n_ctx=2048, verbose=True)

app = Flask(__name__)

cors = CORS(app)

@app.route('/api/message', methods=['POST'])
def get_text():
    data = request.get_json()
    print(f"rcvd {data}")
    response = llm.create_completion(sql_prompt%data['msg'])
    
    resp_msg = response['choices'][0]['text']
    print(f"sending back [{resp_msg}]")
    return jsonify({'msg': resp_msg}), 201

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=6969)