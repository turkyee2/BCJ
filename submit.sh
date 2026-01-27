#!/bin/bash

# 사용법: ./submit.sh [문제번호] [폴더명] [코멘트]
# 예시: ./submit.sh 1000 "DP" "피보나치 풀이"

# 1. 입력값 확인
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "오류: 문제 번호와 폴더명을 입력해주세요!"
  echo "사용법: ./submit.sh [문제번호] [폴더명] [코멘트]"
  exit 1
fi

PROBLEM_ID=$1
FOLDER_NAME=$2
COMMENT=${3:-"문제 $1번 풀이 완료 ($2)"} # 세 번째 인자가 코멘트가 됨

# 2. 계층 구조 폴더 생성 (solutions/폴더명)
# -p 옵션은 상위 폴더가 없으면 알아서 다 만들어줍니다.
TARGET_DIR="solutions/$FOLDER_NAME"
mkdir -p "$TARGET_DIR"

# 3. main.py를 해당 폴더 안의 문제 번호.py로 복사
cp main.py "$TARGET_DIR/$PROBLEM_ID.py"

# 4. Git 명령어로 업로드
git add "$TARGET_DIR/$PROBLEM_ID.py"
git commit -m "$COMMENT"
git push

echo "[$FOLDER_NAME] $PROBLEM_ID번 업로드 완료!"