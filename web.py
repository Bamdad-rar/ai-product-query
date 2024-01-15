#!/usr/bin/env python3
from typing import List, Tuple

from langchain.chains import ConversationChain
# from langchain.chat_models import ChatOpenAI
# from log_callback_handler import NiceGuiLogElementCallbackHandler
from langchain.llms.llamacpp import LlamaCpp
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from llama_cpp import Llama

prompt = """
Instruct: You are sqlite3 expert. Given an input question, you create only a syntactically correct sqlite3 query and nothing else. 
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

Use the following format:

Question: "Question here"
Output: "SQL Query to run"

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


llm = Llama(model_path="./phi-2.gguf", n_ctx=1024, verbose=True)



from nicegui import context, ui


@ui.page('/')
def main():

    messages: List[Tuple[str, str]] = []
    thinking: bool = False

    @ui.refreshable
    def chat_messages() -> None:
        for name, text in messages:
            ui.chat_message(text=text, name=name, sent=name == 'You')
        if thinking:
            ui.spinner(size='3rem').classes('self-center')
        

    async def send() -> None:
        nonlocal thinking
        message = text.value
        messages.append(('You', text.value))
        thinking = True
        text.value = ''
        chat_messages.refresh()

, cross_origin        thinking = False
        chat_messages.refresh()

    anchor_style = r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}'
    ui.add_head_html(f'<style>{anchor_style}</style>')

    # the queries below are used to expand the contend down to the footer (content can then use flex-grow to expand)
    ui.query('.q-page').classes('flex')
    ui.query('.nicegui-content').classes('w-full')

    with ui.tabs().classes('w-full') as tabs:
        chat_tab = ui.tab('Chat')
        # logs_tab = ui.tab('Logs')
    with ui.tab_panels(tabs, value=chat_tab).classes('w-full max-w-2xl mx-auto flex-grow items-stretch'):
        with ui.tab_panel(chat_tab).classes('items-stretch'):
            chat_messages()
        # with ui.tab_panel(logs_tab):
        #     log = ui.log().classes('w-full h-full')

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            placeholder = 'message'
            text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3') \
                .classes('w-full self-center').on('keydown.enter', send)


ui.run(title='Customer Support', port=6969)