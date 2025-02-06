#!/bin/bash

# wine_analysis_project 디렉토리로 이동
cd wine_analysis_project

# 모든 변경사항 추가 및 푸시
git add .
commit_message="자동 커밋: $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_message"
git push origin main

echo "업로드가 완료되었습니다!"