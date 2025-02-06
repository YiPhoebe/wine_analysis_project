#!/bin/bash

# Shell 스크립트 시작

# 현재 디렉토리에서 analyze.py 실행 및 출력 로그 저장
python3 analyze.py > log.txt 2>&1

# 실행 완료 메시지 출력
echo "분석이 완료되었습니다. 로그는 log.txt에서 확인하세요."
