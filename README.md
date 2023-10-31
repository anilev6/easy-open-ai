# _Welcome to my OpenAI Playground!_

_STILL ACTIVELY DEVELOPING_

## How to play

- `pip install easy-open-ai-anilev6`
- make `.env` with `OPENAI_API_KEY=`
- enjoy !
  - `get_picture(text, save=True)`
  - `correct_grammar(text)`
  - `get_answer(question)`
  - `get_answer_with_instruction(question,instruction`
  - `translate_text_to_Ukrainian(text)`
  - `get_n_pictures(text, n=3)`

## Main project requirements

- [ ] Make an [organization](https://platform.openai.com/docs/guides/production-best-practices)
- [x] Make this a package

*_General_*

- [x] Count ['tokens'](https://platform.openai.com/docs/guides/gpt/managing-tokens) for the user input
- [ ] Count [API calls](https://platform.openai.com/account/rate-limits) and limit them
- [ ] Handle [errors](https://platform.openai.com/docs/guides/error-codes)
- [x] Moderate input _(limited in other languages; API calls free of charge)_
- [x] Request a custom task

*_Specific project tasks_*

- [x] Translate text
- [x] Correct the grammar
- [x] Change the text tone
- [x] Rephrase text
- [x] Summarize

*_Additionally_*

- [x] Generate [an illustration](https://platform.openai.com/docs/api-reference/images) for the text
- [ ] [Edit](https://platform.openai.com/docs/api-reference/images/createEdit) an image using "mask"
- [ ] Stream [text being filled](https://cookbook.openai.com/examples/how_to_stream_completions)
- [ ] Autocomplete text

## Experience

- [ ] Return or stream different 'text-task' response options
- [ ] [Speech-to-text](https://platform.openai.com/docs/api-reference/audio) functionality
- [ ] Make a [chat plugin](https://platform.openai.com/docs/plugins)
- [ ] Try the [community library](https://github.com/OthersideAI/chronology) listed on the [official documentation page](https://platform.openai.com/docs/libraries/community-libraries)
- [ ] Try [embeddings](https://cookbook.openai.com/articles/text_comparison_examples)

## Useful Resources

- [OpenAI Examples](https://platform.openai.com/examples)
- [OpenAI Cookbook](https://cookbook.openai.com/about)
- [OpenAI Community](https://community.openai.com/)
