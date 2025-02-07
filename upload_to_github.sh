#!/bin/bash

# GitHub 저장소 URL (사용자에 맞게 변경)
REPO_URL="https://github.com/YOUR_USERNAME/YOUR_REPO.git"

# 커밋 메시지 (현재 날짜 및 시간 포함)
COMMIT_MSG="🚀 자동 업로드: $(date +'%Y-%m-%d %H:%M:%S')"

echo "🔄 GitHub에 파일을 업로드합니다..."

# Git 설정 및 업로드
git add .
git commit -m "$COMMIT_MSG"
git push origin main

echo "✅ 업로드 완료! GitHub에서 확인하세요!"

# chmod +x upload_to_github.sh  # 실행 권한 부여 (최초 1회만)
# ./upload_to_github.sh  # 실행

# conda env create -f environment.yml  # 환경 생성
# conda activate wine_analysis  # 환경 활성화
