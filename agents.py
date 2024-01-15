

class SqlGenie:
    def __init__(self, database="sqlite3") -> None:
        self.number_of_answers = 3
        self.database = database
        self.parameters = {
            "temperature": 0.1
        }
    
        self.prompt = f"""You are an {self.database} expert. Given an input question, create a syntactically correct {database} query to run and nothing else, just the query. When the query is asking for {self.number_of_answers} closest row, you have to use this distance function to calculate distance to entity's array on vector column and order by the distance to retrieve relevant rows. *NOTICE*: `DISTANCE(column, array)` only accept an array column as its first argument and a `NeuralArray(entity)` as its second argument. You also need a user defined function called `NeuralArray(entity)` to retrieve the entity's array. Unless the user specifies in the question a specific number of examples to obtain, query for at most {self.number_of_answers} results using the LIMIT clause.You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.Pay attention to use today() function to get the current date, if the question involves "today". `ORDER BY` clause should always be after `WHERE` clause. DO NOT add semicolon to the end of SQL. Pay attention to the comment in table schema. Use the following format:
                    Question: "Question here"
                    SQLQuery: "SQL Query to run"
                    """
        
    def add_to_prompt(self, text):
        self.prompt += text
    
        
