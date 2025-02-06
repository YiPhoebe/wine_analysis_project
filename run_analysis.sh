#!/bin/bash

# wine_analysis_project 디렉토리로 이동
cd wine_analysis_project

# analyze.py 실행 및 로그 저장
python3 analyze.py > log.txt 2>&1

echo "분석이 완료되었습니다. 로그는 wine_analysis_project/log.txt에서 확인하세요."