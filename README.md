# Code switching and contextual prompting with AssemblyAI-STT-3.7

Companion code for the AssemblyAI blog post
[Code switching and contextual prompting on AssemblyAI-STT-3.7](https://www.assemblyai.com/blog/universal-3-5-pro-code-switching-contextual-prompting).

`code_switch.py` transcribes a recorded file with `speech_models=["assemblyai-stt-3-7"]`.

- No flags: `language_detection=True`, so the model code-switches across its 32 languages.
- `--languages en hi`: `language_codes` limits switching to the languages you list. English isn't required.
- `--prompt "..."`: contextual prompting. Describe the audio in plain sentences.
- `--keyterms A B`: keyterms prompting for names and terms that must be spelled exactly.

## Run it

Requires Python 3.9+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ASSEMBLYAI_API_KEY=your_api_key_here
python code_switch.py https://assembly.ai/code-switching-2
python code_switch.py https://assembly.ai/prompt-8 --prompt "League of Legends roles"
```

The sample clips are the ones used in the AssemblyAI docs.

## Pricing

AssemblyAI-STT-3.7 is $0.21/hr. On it, prompting and keyterms prompting are $0.05/hr add-ons each.
See [pricing](https://www.assemblyai.com/pricing).
