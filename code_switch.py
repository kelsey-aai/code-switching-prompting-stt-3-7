"""Code switching and contextual prompting on AssemblyAI-STT-3.7.

Usage:
    export ASSEMBLYAI_API_KEY=your_api_key_here
    python code_switch.py https://assembly.ai/code-switching-2
    python code_switch.py https://assembly.ai/prompt-8 --prompt "League of Legends roles"
    python code_switch.py interview.mp3 --languages en hi
"""
import argparse
import os
import sys

from assemblyai.prerecorded.v2 import Transcriber, TranscriptionConfig


def build_config(languages=None, prompt=None, keyterms=None):
    kwargs = {"speech_models": ["assemblyai-stt-3-7"]}
    if languages:
        kwargs["language_codes"] = languages  # code-switch only among these
    else:
        kwargs["language_detection"] = True  # code-switch across all 32 languages
    if prompt:
        kwargs["prompt"] = prompt  # describe the audio, in plain sentences
    if keyterms:
        kwargs["keyterms_prompt"] = keyterms  # names and terms to spell exactly
    return TranscriptionConfig(**kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", help="Local path or public URL")
    parser.add_argument("--languages", nargs="+", help="Language codes, e.g. en hi")
    parser.add_argument("--prompt", help="Plain-language description of the audio")
    parser.add_argument("--keyterms", nargs="+", help="Terms to spell exactly")
    args = parser.parse_args()

    api_key = os.environ.get("ASSEMBLYAI_API_KEY")
    if not api_key:
        sys.exit("Set ASSEMBLYAI_API_KEY first.")

    config = build_config(args.languages, args.prompt, args.keyterms)
    transcript = Transcriber(api_key=api_key, config=config).transcribe(args.audio)

    if transcript.status == "error":
        sys.exit(f"Transcription failed: {transcript.error}")

    print(f"Model used: {transcript.speech_model_used}")
    print(transcript.text)


if __name__ == "__main__":
    main()
