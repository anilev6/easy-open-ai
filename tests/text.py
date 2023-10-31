from icecream import ic
import asyncio

#------------------------------------------------------Operations with text------------------------------------------------------------

from easy_open_ai.models.text import BaseChatCompletion, GrammarCorrection
from easy_open_ai.models.text import IsHarmfulText, num_tokens_from_string

async def test_async_custom_task():
    instructions_and_inputs=[('Reply me as a poet in rhymes','How are you today?')]
    for i in instructions_and_inputs:
        ic(i)
        b=BaseChatCompletion(i[1])
        b.temperature=0.85
        b.task_for_ai=i[0]
        result = await b.async_chat_completion_task()
        ic(result)

def try_all():
    all_sync_tests=(test_correct_grammar,)
    for t in all_sync_tests:
        t()

def test_correct_grammar():
    test_messages=['I is doing well, thnk you fp asking.']
    for test_message in test_messages:
        ic(test_message)
        ic(GrammarCorrection(test_message).chat_completion_task())

def test_change_tone():
    pass

# need to add more tests! 

#------------------------------------------------------Validation------------------------------------------------------------

def test_is_harmful_text():
    test_messages=['I is doing well, fuck you fp asking.']
    for test_message in test_messages:
        ic(test_message)
        ic(IsHarmfulText(test_message).validation_task())

def test_count_tokens():
    test_messages=['I is doing well, fuck you fp asking.']
    for test_message in test_messages:
        ic(test_message)
        ic(num_tokens_from_string(test_message))


if __name__=='__main__':
    asyncio.run(test_async_custom_task())
    # test_correct_grammar()
    # test_is_harmful_text()
    # test_count_tokens()