import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

# 와인 데이터셋 로드
data = load_wine

# 데이터프레임으로 변환
df = pd.DataFrame(data.data, columns=data.feature_names)

# 1. 데이터셋의 행(row)과 열(column) 개수 확인
num_rows, num_columns = df.shape

# 2. 각 컬럼별 평균(mean)과 표준편차(std) 계산
mean_std_info = df.aggregate(['mean', 'std']).T

# 3. 'alcohol' 특성의 최대값과 최소값 구하기
alcohol_max = df['alcohol'].max()
alcohol_min = df['alcohol'].min()

# 출력할 텍스트 준비
outout_text = (
    f"데이터셋 크기 : {num_rows}개의 행, {num_columns}개의 열\n\n"
    "각 특성의 평균 및 표준편차 : \n"
    f"{mean_std_info}\n\n"
    f"알코올(alcohol) 특성 : \n  최대값 : {alcohol_max}\n 최소값 : {alcohol_min}\n"
)

# 결과를 텍스트 파일에 저장
with open('output.txt', 'w') as file:
    file.write(outout_text)

print("분석이 완료되었습니다.결과는 'output.txt에 저장되었습니다.")