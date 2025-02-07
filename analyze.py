# 수학 numpy , 데이터 pandas 라이브러리를 불러옴
# pip install scikit-learn 설치 후에 sklearn 프롬해서 임포트 와인 데이터셋

import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_wine

# 와인 데이터셋 로드 (여러특성 alcohol, malic acid 등 라벨이 포함된 데이터셋 객체를 반환)
data = load_wine()

# 와인 데이터를 pandas 데이터프레임 형태로 변환
df = pd.DataFrame(data.data, columns=data.feature_names)  # 각 열에 와인 특성의 이름 붙여줌                   

# 1. 데이터셋의 행(row)과 열(column) 개수 확인
num_rows, num_columns = df.shape

# 2. 각 컬럼별 평균(mean)과 표준편차(std) 계산
mean_std_info = df.aggregate(['mean', 'std']).T    #.T: 결과를 전치(transpose)해서 보기 쉽게 행과 열을 뒤집어 출력

# 3. 'alcohol' 특성의 최대값과 최소값 구하기
alcohol_max = df['alcohol'].max()
alcohol_min = df['alcohol'].min()

# 저장할 폴더 생성 (없으면 자동 생성)
output_dir = "wine_analysis_project"
os.makedirs(output_dir, exist_ok=True)

# 결과 저장 파일 경로
output_file = os.path.join(output_dir, "output.txt")

# 출력할 텍스트 준비
# 각 분석 결과(데이터셋 크기, 평균과 표준편차, 알코올 최대·최소값)를 output_text에 문자열로 저장
output_text = (
    f"데이터셋 크기 : {num_rows}개의 행, {num_columns}개의 열\n\n"
    "각 특성의 평균 및 표준편차 : \n"
    f"{mean_std_info}\n\n"
    f"알코올(alcohol) 특성 : \n 최대값 : {alcohol_max}\n 최소값 : {alcohol_min}\n"
)

# 결과를 텍스트 파일에 저장
# open('output.txt', 'w'): 텍스트 파일을 쓰기 모드로 열는법
# 결과를 output.txt 파일에 저장
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(output_text)

print(f"분석이 완료되었습니다. 결과는 '{output_file}'에 저장되었습니다.")