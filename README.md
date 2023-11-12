# _Welcome to my OpenAI Playground!_

Making `Open AI` even easier.

_STILL ACTIVELY DEVELOPING_

## How to play

- `pip install easy-open-ai`
- in your working folder, create `.env` file with `OPENAI_API_KEY=`, or make such environment variable
- enjoy! `from easy_open_ai import` ...

  #### Version 0.1.6

  + `get_picture(text, save=True)` *(as b64_json string)*
  + `get_n_pictures(text, n=3)`
  
  + `get_answer(question)`
  + `correct_grammar(text)`

  #### Version 0.1.7

  + `get_picture_url(text)` *(url lives 1 hour)*
  + `get_n_pictures_urls(text, n=3)`

  + `is_harmful_text(text)` *(sometimes ignores censorship escaping: '@' instead of 'a', etc)*
  + `how_many_text_tokens(text)` *(most of this package works with text no longer than 1024 text-tokens, it's recommended for validating the text length)*
  
  + `sum_up_as_haiku(text)`
  + `get_poem(text)`
  + `get_answer_as_poem(question)`
  + `autocomplete_text(text)`
  
  + `translate_text(text, language='Ukrainian')`
  + `get_answer_with_instruction(question,instruction,
            chaos_coefficient=0.5,
            model="gpt-3.5-turbo",
            max_tokens=1024)`

  #### Version 0.1.8

  *ADDED LIVE TEXT DISPLAYING*

  + `get_answer_with_instruction_stream(question)` *(it's a generator)*
  
  *to get chatGPT-like live text generation, add `_stream` to the name, for example, `aget_answer_as_poem_stream(question)`*

  **!not all of the available text functions have this yet**

#### Version 0.1.9

+ Automatic documentation for your function and **FastAPI endpoints** in a python file with `docstring file_name.py` terminal command (or `docstring path\to\file_name.py `). If the docstring is already present, it will **NOT** overwrite it.

More easy functions coming soon!

_For `async` version of a function, add `a` in front, for example, `aget_picture(text)` instead of `get_picture(text)`._
