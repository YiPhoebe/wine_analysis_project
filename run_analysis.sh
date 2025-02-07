#!/bin/bash

# 실행 로그 파일 경로
LOG_FILE="wine_analysis_project/log.txt"

# 로그 파일 저장할 폴더가 없으면 생성
mkdir -p wine_analysis_project

# Python 분석 실행 및 로그 저장
echo "🚀 분석을 시작합니다..." | tee -a $LOG_FILE
python3 analyze.py 2>&1 | tee -a $LOG_FILE
echo "✅ 분석이 완료되었습니다. 로그는 '$LOG_FILE'에서 확인하세요!" | tee -a $LOG_FILE

# chmod +x run_analysis.sh  # 실행 권한 부여 (최초 1회만)
# ./run_analysis.sh  # 실행
