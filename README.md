---
title: MailMind.ai
emoji: 📬
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
short_description: OpenEnv enterprise email triage simulator
---
# MailMind.ai — OpenEnv Enterprise Email Triage

OpenEnv-based reinforcement learning environment for enterprise email triage. Agents learn to classify, prioritize, route, and resolve inbound email under real SLA pressure, escalation risk, and reviewer workflow constraints.

## 🚀 Overview

Enterprise email operations are a real-world, high-stakes problem: support, HR, finance, security, and operations teams must process thousands of incoming messages with speed, accuracy, and business context.

This project is not a toy benchmark. It is a high-fidelity OpenEnv environment designed to train and evaluate agents on:

- multi-field email understanding
- priority and routing decisions
- SLA-aware workflow urgency
- escalation and human review
- queue and backlog pressure
- response drafting and ownership assignment

## 🎯 Problem Statement

Build an AI system where an agent can:

- understand email intent, tone, and urgency
- classify business category
- assign priority and route to the correct department
- detect spam and sentiment
- request human review when needed
- honor SLA deadlines and escalation policies
- optimize performance through reward-driven feedback

## ✨ Key Features

- Real-world enterprise workflow simulation
- Multi-turn email and threaded conversation support
- SLA-aware reward shaping
- Deterministic OpenEnv grading
- Modular architecture with backend, schemas, and UI
- Baseline agent and inference pipeline
- Docker + Hugging Face Spaces deployment support

## 🏗️ Architecture

### Backend

- FastAPI runtime in `backend/main.py`
- OpenEnv environment service in `backend/services/env_service.py`
- Baseline runner in `backend/services/baseline_service.py`
- OpenEnv adapter in `server/app.py`
- SQLite persistence in `backend/db/sqlite.py`

### Schemas

- Observation and action contracts in `backend/schemas/env.py`
- OpenEnv SDK compatibility in `backend/schemas/openenv_sdk.py`

### Dataset & training

- Synthetic dataset generator in `training/data_generator.py`
- Training pipeline in `train.py`
- Local inference engine in `backend/services/inference_engine.py`
- Saved evaluation metrics in `models/metrics.json`

### Frontend

- React + TypeScript + Tailwind dashboard in `ui`
- Zustand state management and Recharts analytics
- Inbox, decision, reviewer, and analytics panels

## 🔌 OpenEnv Contract

The environment exposes the standard OpenEnv interaction endpoints:

- `POST /reset`
- `POST /step`
- `GET /state`

Validator-facing endpoints:

- `GET /health`
- `GET /metadata`
- `GET /schema`
- `POST /mcp`

Root configuration is in `openenv.yaml`.

## 🧠 Observation / Action / Reward

### Observation

The typed observation model is `TriageObservation` in `backend/schemas/env.py`.

It includes operational state such as:

- `environment_id`, `episode_id`, `task_id`
- `difficulty`, `step_count`, `max_steps`
- `email`, `thread_messages`, `pending_actions`
- `sla_status`, `escalation_level`, `human_review_required`
- `queue_depth`, `reviewer_backlog`, `business_impact`
- `suggested_departments`, `ownership_status`, `completion_score`

### Action

The typed action model is `AgentAction` in `backend/schemas/env.py`.

Agent outputs include:

- `category`
- `priority`
- `department`
- `spam`
- `sentiment`
- `urgency`
- `response_draft`
- `escalation`
- `confidence`
- `internal_note`
- `request_human_review`
- `assigned_owner`
- `resolution_eta_hours`
- `customer_follow_up_required`
- `escalation_target`

### Reward

The typed reward model is `RewardSignal` in `backend/schemas/env.py`.

It produces:

- normalized `score` in `0.0-1.0`
- `score_breakdown`
- `matched`, `mistakes`, `partial_progress`
- `penalty_flags`

## 🧩 Tasks

### Task 1 — Easy

`task-email-classification-easy`

Objective: classify a single inbound message into the correct business category.

### Task 2 — Medium

`task-triage-medium`

Objective: classify, prioritize, and route an email while respecting SLA urgency.

### Task 3 — Hard

`task-full-enterprise-hard`

Objective: manage the full enterprise triage workflow, including spam, sentiment, SLA pressure, escalation, ownership, ETA planning, reviewer handoff, and queue-aware decision making.

## 🧮 Grading & Reward Design

Grading is deterministic in `graders/email_grader.py` and normalized to a valid OpenEnv score range.

The grader rewards:

- classification accuracy
- priority alignment
- routing correctness
- SLA-aware urgency handling
- spam detection
- escalation discipline
- review requests
- response quality on hard turns
- ownership and ETA realism

Penalties apply for SLA violations, incorrect routing, ignored urgency, and over-escalation.

## 📦 Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the environment:

```bash
python run.py --host 127.0.0.1 --port 8000
```

API is available at `http://127.0.0.1:8000`.

## 📊 Frontend Dashboard

Run locally:

```bash
cd ui
npm install
npm run dev
```

If the frontend runs separately:

```bash
VITE_API_BASE_URL=http://localhost:8000
```

## ⚡ Evaluation Pipeline

The submission pipeline is `inference.py`.

### Required environment variables

```bash
HF_TOKEN=<your_hugging_face_token>
API_BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=meta-llama/Meta-Llama-3-8B-Instruct
OPENAI_API_KEY=<optional>
```

### Run evaluation

```bash
python inference.py --task-id task-email-classification-easy --max-steps 5 --seed 42
```

### Output expectations

The entrypoint logs the OpenEnv-style evaluation summary and returns a normalized final score.

## ✅ Validation

Validate the OpenEnv contract from the repo root:

```bash
python -m openenv.cli validate
```

Use the lightweight helper before submission:

```bash
python prevalidate.py
```

## 🐳 Docker

Build and run locally:

```bash
docker build -t email-triage-openenv .
docker run -p 7860:7860 email-triage-openenv
```

The container boots the dataset and starts the API via `server/app.py`.

## 🌐 Deployment

This repository is ready for Docker deployment and Hugging Face Spaces.

Recommended Space variables:

- `API_BASE_URL`
- `MODEL_NAME`
- `HF_TOKEN`
- `OPENAI_API_KEY`
- `MODEL_BACKEND`

## 🧠 Why MailMind.ai Wins

- Realistic enterprise workflow modeling
- OpenEnv-native evaluation and grading
- Dense reward shaping for partial progress
- Multi-turn, escalation-aware task design
- Clear validation and deployment path

## 📍 Source Structure

- `backend/` — environment runtime, schemas, services
- `graders/` — deterministic scoring engine
- `training/` — dataset generation and training pipeline
- `server/` — OpenEnv API adapter
- `ui/` — React dashboard
- `inference.py` — submission evaluation pipeline
- `run.py` — local API launcher
- `prevalidate.py` — validation helper
