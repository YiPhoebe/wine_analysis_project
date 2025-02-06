#!/bin/bash

# Git 상태 확인
echo "현재 디렉토리의 Git 상태 확인..."
git status

# 모든 변경사항 추가
echo "모든 변경된 파일을 스테이징합니다..."
git add .

# 커밋 메시지 생성 (현재 시간 포함)
commit_message="자동 커밋: $(date '+%Y-%m-%d %H:%M:%S')"
echo "커밋 메시지: $commit_message"

git commit -m "$commit_message"

# 원격 저장소에 푸시
echo "변경 사항을 원격 저장소에 푸시합니다..."
git push origin main

# 완료 메시지 출력
echo "업로드가 완료되었습니다!"
