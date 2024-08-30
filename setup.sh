#!/bin/bash

# 프로젝트 루트 디렉토리 설정
PROJECT_ROOT="/root/src/ibm-project"
mkdir -p $PROJECT_ROOT

# .github 폴더 생성
mkdir -p $PROJECT_ROOT/.github

# 백엔드 폴더 및 파일 생성
mkdir -p $PROJECT_ROOT/backend/app
echo "FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [\"python\", \"app.py\"]

EXPOSE 5000" > $PROJECT_ROOT/backend/Dockerfile

echo "" > $PROJECT_ROOT/backend/requirements.txt

# AI 모델 폴더 및 파일 생성
mkdir -p $PROJECT_ROOT/ai/model
echo "FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [\"python\", \"model.py\"]

EXPOSE 8000" > $PROJECT_ROOT/ai/Dockerfile

echo "" > $PROJECT_ROOT/ai/requirements.txt

# .gitignore 파일 생성
echo "node_modules/
.env
__pycache__/
*.pyc
.DS_Store
*.log
.vscode/" > $PROJECT_ROOT/.gitignore

# README.md 파일 생성
echo "# Project Title

Project description and instructions." > $PROJECT_ROOT/README.md

# docker-compose.yml 파일 생성
echo "version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - \"5000:5000\"
  ai:
    build: ./ai
    ports:
      - \"8000:8000\"" > $PROJECT_ROOT/docker-compose.yml

echo "프로젝트 폴더 및 파일이 성공적으로 생성되었습니다."
