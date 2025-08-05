# Talk To gpt-oss

> Run a simple voice assistant with Python that uses gpt-oss for the LLM.

## Overview

This guide walks you through the setup of talking to gpt-oss using LiveKit Agents for Python. In less than 2 minutes, you'll have a voice assistant that you can speak to in your terminal, browser, telephone, or native app.

## Requirements

The following sections describe the minimum requirements to get started.

### Python

LiveKit Agents requires Python 3.9 or later.

### LiveKit server

You need a LiveKit server instance to transport realtime media between user and agent. The easiest way to get started is with a free [LiveKit Cloud](https://cloud.livekit.io/) account. Create a project and use the API keys in the following steps. You may also [self-host LiveKit](https://docs.livekit.io/home/self-hosting/local.md) if you prefer.

## Setup

Use the instructions in the following sections to set up your new project.

### Packages


Install the following packages to build a complete voice AI agent with your STT-LLM-TTS pipeline, noise cancellation, and [turn detection](https://docs.livekit.io/agents/build/turns.md):

```shell
pip install \
  "livekit-agents[assemblyai,groq,cartesia,silero,turn-detector]~=1.0" \
  "livekit-plugins-noise-cancellation~=0.2" \
  "python-dotenv"

```

### Environment variables

Create a file named `.env` and add your LiveKit credentials along with the necessary API keys for your AI providers.

**STT-LLM-TTS pipeline**:

```shell
ASSEMBLYAI_API_KEY=<Your Deepgram API Key>
GROQ_API_KEY=<Your OpenAI API Key>
CARTESIA_API_KEY=<Your Cartesia API Key>
LIVEKIT_API_KEY=%{apiKey}%
LIVEKIT_API_SECRET=%{apiSecret}%
LIVEKIT_URL=%{wsURL}%

```

### Agent code

Use the `agent.py` file in this repo. 

## Download model files

You first need to download the model files for the `turn-detector`, `silero`, or `noise-cancellation` plugins:

```shell
python agent.py download-files

```

## Speak to your agent

Start your agent in `console` mode to run inside your terminal:

```shell
python agent.py console

```

Your agent speaks to you in the terminal, and you can speak to it as well.



## Connect to playground

Start your agent in `dev` mode to connect it to LiveKit and make it available from anywhere on the internet:

```shell
python agent.py dev

```

Use the [Agents playground](https://docs.livekit.io/agents/start/playground.md) to speak with your agent and explore its full range of multimodal capabilities.

Congratulations, your agent is up and running. Continue to use the playground or the `console` mode as you build and test your agent.

> 💡 **Agent CLI modes**
> 
> In the `console` mode, the agent runs locally and is only available within your terminal.
> 
> Run your agent in `dev` (development / debug) or `start` (production) mode to connect to LiveKit and join rooms.

## Next steps

Follow these guides bring your voice AI app to life in the real world.

- **[Web and mobile frontends](https://docs.livekit.io/agents/start/frontend.md)**: Put your agent in your pocket with a custom web or mobile app.

- **[Telephony integration](https://docs.livekit.io/agents/start/telephony.md)**: Your agent can place and receive calls with LiveKit's SIP integration.

- **[Testing your agent](https://docs.livekit.io/agents/build/testing.md)**: Add behavioral tests to fine-tune your agent's behavior.

- **[Building voice agents](https://docs.livekit.io/agents/build.md)**: Comprehensive documentation to build advanced voice AI apps with LiveKit.

- **[Worker lifecycle](https://docs.livekit.io/agents/worker.md)**: Learn how to manage your agents with workers and jobs.

- **[Deploying to production](https://docs.livekit.io/agents/ops/deployment.md)**: Guide to deploying your voice agent in a production environment.

- **[Integration guides](https://docs.livekit.io/agents/integrations.md)**: Explore the full list of AI providers available for LiveKit Agents.

- **[Recipes](https://docs.livekit.io/recipes.md)**: A comprehensive collection of examples, guides, and recipes for LiveKit Agents.

---

This document was rendered at 2025-08-05T23:20:56.508Z.
For the latest version of this document, see [https://docs.livekit.io/agents/start/voice-ai.md](https://docs.livekit.io/agents/start/voice-ai.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).