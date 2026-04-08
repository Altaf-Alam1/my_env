---
title: myenv09
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# AI Customer Support Triage Environment

## Overview
This project simulates a real-world customer support workflow.

## Action Space
- category: Billing / Technical / Account
- priority: High / Low

## Observation Space
- text: user complaint

## Tasks
- Easy: classification
- Medium: priority assignment
- Hard: full triage

## Reward
Score between 0 and 1 with penalties for incorrect actions.

## Baseline
Simple heuristic agent using inference.py

## Run
python inference.py
