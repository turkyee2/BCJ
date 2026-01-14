#!/bin/bash

# 사용법: ./submit.sh [문제번호] [코멘트]
# 예시: ./submit.sh 1000 "DP 풀이"

# 1. 입력값 확인
if [ -z "$1" ]; then
  echo "오류: 문제 번호를 입력해주세요!"
  echo "사용법: ./submit.sh [문제번호]"
  exit 1
fi

PROBLEM_ID=$1
COMMENT=${2:-"문제 $1번 풀이 완료 (Python)"} # 코멘트 없으면 기본값

# 2. 저장할 폴더가 없으면 생성 (solutions 폴더)
mkdir -p solutions

# 3. main.py를 해당 문제 번호.py로 복사
cp main.py solutions/$PROBLEM_ID.py

# 4. Git 명령어로 업로드
git add solutions/$PROBLEM_ID.py
git commit -m "$COMMENT"
git push

echo "$PROBLEM_ID번(Python) 업로드 완료!"