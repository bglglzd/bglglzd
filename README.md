<h1 align="center">bglglzd · AI Builder</h1>

<p align="center">
  Building private, local-first AI products for voice and developer workflows.
</p>

<p align="center">
  <a href="https://github.com/bglglzd?tab=followers"><img src="https://img.shields.io/github/followers/bglglzd?label=Follow&style=flat&logo=github" alt="GitHub followers"></a>
  <img src="https://img.shields.io/badge/focus-local--first%20AI-0ea5e9" alt="Local-first AI">
  <img src="https://img.shields.io/badge/values-privacy%20%2B%20craft-16a34a" alt="Privacy and craft">
  <img src="https://img.shields.io/badge/open%20source-active-f97316" alt="Open source active">
</p>

<p align="center">
  <a href="#featured-projects">Projects</a> ·
  <a href="#open-source-contributions">Open source</a> ·
  <a href="#how-i-build">Principles</a>
</p>

## What I build

I make AI tools useful in the real world: local data paths where possible, explicit privacy boundaries, reproducible engineering work, and interfaces people can trust every day.

<p>
  <img src="https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/Tauri-24C8DB?logo=tauri&logoColor=white" alt="Tauri">
  <img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?logo=kotlin&logoColor=white" alt="Kotlin">
  <img src="https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite">
</p>

## Featured projects

### [Auris](https://github.com/bglglzd/3uxo) — private meeting memory for Windows

[![Auris CI](https://github.com/bglglzd/3uxo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/bglglzd/3uxo/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/bglglzd/3uxo?label=release)](https://github.com/bglglzd/3uxo/releases)
[![License](https://img.shields.io/github/license/bglglzd/3uxo)](https://github.com/bglglzd/3uxo/blob/main/LICENSE)

Local-first call recording, on-device Whisper transcription, and AI notes through an OpenAI-compatible provider chosen by the user. Auris records microphone and system audio on separate tracks, then turns conversations into useful summaries and Q&A.

`Rust` · `Tauri` · `React` · `TypeScript` · `Whisper` · `SQLite`

[Explore Auris](https://github.com/bglglzd/3uxo) · [Download a release](https://github.com/bglglzd/3uxo/releases)

### [Agent Workflows](https://github.com/bglglzd/agent-workflows) — reliable prompts for coding agents

[![Validate](https://github.com/bglglzd/agent-workflows/actions/workflows/validate.yml/badge.svg)](https://github.com/bglglzd/agent-workflows/actions/workflows/validate.yml)
[![Latest release](https://img.shields.io/github/v/release/bglglzd/agent-workflows?label=release)](https://github.com/bglglzd/agent-workflows/releases)
[![Codex plugin](https://img.shields.io/badge/Codex-plugin-0ea5e9)](https://github.com/bglglzd/agent-workflows/tree/main/plugins/agent-workflows)

Portable Markdown workflows for three high-value moments: preserving session context, auditing a project safely, and interviewing an idea into a buildable plan. Includes an installable Codex plugin and tool-neutral prompt files.

[Browse workflows](https://github.com/bglglzd/agent-workflows) · [Install the plugin](https://github.com/bglglzd/agent-workflows#install-in-codex)

### [bugkit](https://github.com/bglglzd/bugkit) — context that helps AI fix bugs

[![Live demo](https://img.shields.io/badge/demo-live-16a34a)](https://bglglzd.github.io/bugkit/)
[![License](https://img.shields.io/github/license/bglglzd/bugkit)](https://github.com/bglglzd/bugkit/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/bglglzd/bugkit?style=flat)](https://github.com/bglglzd/bugkit/stargazers)

An AI-friendly bug-report workflow: users capture rich context, maintainers receive one concise technical brief, and coding agents can start investigating without losing the important details.

[Try bugkit](https://bglglzd.github.io/bugkit/) · [View repository](https://github.com/bglglzd/bugkit)

### [CipherBoard](https://github.com/bglglzd/CipherBoard) — offline-first secure keyboard for GrapheneOS

[![Latest release](https://img.shields.io/github/v/release/bglglzd/CipherBoard?label=release)](https://github.com/bglglzd/CipherBoard/releases)
[![License](https://img.shields.io/github/license/bglglzd/CipherBoard)](https://github.com/bglglzd/CipherBoard/blob/main/LICENSE)
[![GrapheneOS](https://img.shields.io/badge/GrapheneOS-offline--first-4b5563)](https://github.com/bglglzd/CipherBoard)

An encrypted Android keyboard built around physical QR pairing, Olm Double Ratchet, Android Keystore, and no network permission.

[Explore CipherBoard](https://github.com/bglglzd/CipherBoard) · [View releases](https://github.com/bglglzd/CipherBoard/releases)

## Open-source contributions

- [browser-use #5217](https://github.com/browser-use/browser-use/pull/5217) — preserve accessibility-name semantics in enhanced DOM handling.
- [prompts.chat #1223](https://github.com/f/prompts.chat/pull/1223) — add validation and sensible bounds to public API pagination.

I prefer a small number of scoped, reproducible contributions with tests and clear maintenance value over activity for its own sake.

## How I build

- **Local-first by default.** Keep sensitive audio, transcripts, and context with the user whenever possible.
- **AI should be composable.** Let people bring an OpenAI-compatible endpoint or key instead of locking them into one provider.
- **Evidence beats theatre.** Ship narrow changes, show validation, document trade-offs, and leave a project easier to understand than before.

## Now

Making [Auris](https://github.com/bglglzd/3uxo) a dependable private workflow for recording, transcription, and useful AI notes; expanding [Agent Workflows](https://github.com/bglglzd/agent-workflows) with reusable, safe patterns for coding agents.

Good feedback, focused issues, and thoughtful collaboration are always welcome.
