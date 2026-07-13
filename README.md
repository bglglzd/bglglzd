# bglglzd

I build private, local-first AI tools for voice and developer workflows. My work combines practical AI features with the parts that make them trustworthy in daily use: local data, clear interfaces, reproducible bugs, and tested code.

## Flagship projects

### [Auris](https://github.com/bglglzd/3uxo) — local AI meeting memory

A Windows desktop app that records calls on separate tracks, transcribes them locally with Whisper, and turns transcripts into summaries and Q&A through an OpenAI-compatible provider the user chooses.

`Rust` · `Tauri` · `React` · `TypeScript` · `Whisper` · `SQLite` · `Windows`

The technical repository name remains [`3uxo`](https://github.com/bglglzd/3uxo) for updater compatibility. [View releases](https://github.com/bglglzd/3uxo/releases) · [Read the project](https://github.com/bglglzd/3uxo)

### [bugkit](https://github.com/bglglzd/bugkit) — context for AI-assisted fixes

An AI-friendly bug-report workflow: users capture rich, structured context; maintainers get one concise brief they can use with Claude Code, Copilot, or ChatGPT to investigate and ship a fix.

[Live demo](https://bglglzd.github.io/bugkit/) · [Repository](https://github.com/bglglzd/bugkit)

## Engineering principles

- **Local-first by default.** Audio, transcripts, and sensitive context stay with the user whenever possible.
- **AI is composable.** Users can bring their own OpenAI-compatible endpoint or key instead of being locked into one provider.
- **Useful over noisy.** I focus on scoped, reproducible changes, tests, and sustained maintenance—not contribution-graph theatre.

## Open-source work

- [browser-use #5217](https://github.com/browser-use/browser-use/pull/5217) — preserving accessibility-name semantics in enhanced DOM handling.
- [prompts.chat #1223](https://github.com/f/prompts.chat/pull/1223) — validation and bounds for public API pagination.

## Now

Making Auris a dependable private workflow for recording, local transcription, and useful AI notes. Feedback and well-scoped issues are welcome.
