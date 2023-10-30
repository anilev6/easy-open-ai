'''operations with texts up to 1024 tokens (around 500 words)'''
from text import BaseChatCompletion, GrammarCorrection, TranslateText

def get_answer_with_instruction(question:str,instruction:str)-> str:
    b = BaseChatCompletion(question)
    b.task_for_ai=instruction
    return b.chat_completion_task()

async def aget_answer_with_instruction(question:str,instruction:str)-> str:
    b = BaseChatCompletion(question)
    b.task_for_ai=instruction
    result= await b.async_chat_completion_task()
    return result

def get_answer(question:str)-> str:
    b = BaseChatCompletion(question)
    b.task_for_ai='You are a helpful assistant'
    b.temperature=0.5
    result= b.chat_completion_task()
    return result

# print(get_answer('what is internet'))

async def aget_answer(question:str)-> str:
    b = BaseChatCompletion(question)
    b.task_for_ai='You are a helpful assistant'
    b.temperature=0.5
    result= await b.async_chat_completion_task()
    return result

def correct_grammar(text:str)-> str:
    g=GrammarCorrection(text)
    result=g.chat_completion_task()
    return result

async def acorrect_grammar(text:str) -> str:
    g=GrammarCorrection(text)
    result= await g.async_chat_completion_task()
    return result

def translate_text_to_Ukrainian(text:str):
    t=TranslateText(text)
    result=t.chat_completion_task()
    return result

# print(translate_text_to_Ukrainian("I don't care"))

async def atranslate_text_to_Ukrainian(text:str):
    t=TranslateText(text)
    result= await t.async_chat_completion_task()
    return result

#add more from text.py!
