---
title: Advanced Email Triage OpenEnv
sdk: docker
app_port: 7860
pinned: false
tags:
  - openenv
  - enterprise-ai
  - agent-training
  - email-triage
---

# Hugging Face Space Deployment

Push this repository to a Docker Space. The root `Dockerfile` builds the React dashboard and serves the FastAPI backend on port `7860`.

## Recommended Space Variables

- `MODEL_BACKEND=classical`
- `API_BASE_URL=https://api.openai.com/v1`
- `MODEL_NAME=gpt-4.1-mini`
- `HF_TOKEN=` or `OPENAI_API_KEY=` for `inference.py` and `/baseline`
- `CORS_ORIGINS=https://<your-space-subdomain>.hf.space`

## Startup

The container generates the synthetic dataset on boot and serves the complete OpenEnv-compatible environment with queue-aware, multi-turn enterprise email triage tasks.
