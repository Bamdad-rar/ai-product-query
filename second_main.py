from repo import get_table_schema
from agents import SqlGenie
from llama_cpp import Llama

sql_agent = SqlGenie()

db_name = "test.db"
db_table = "IrancellPackages"


schema = get_table_schema(db_name,db_table)

table_info = f"---table {db_table}---\n"

for column, data_type in schema.items():
    table_info+=f"{column}: {data_type}\n"
table_info+= f"---end of table {db_table}---"
sql_agent.add_to_prompt(table_info)


# llm = Llama(model_path="./phi-2.gguf", n_ctx=1024)




# output = llm.create_completion(
#     sql_agent.prompt + "\nQuestion: I want a package for 3 days. SQLQuery:",
# )
