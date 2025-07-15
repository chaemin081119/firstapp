import pandas as pd

# CSV 파일 경로 (현재 폴더 기준)
file_path = "CO2_Emissions.csv"

# CSV 파일 불러오기
df = pd.read_csv(file_path)

# 데이터프레임 기본 정보 출력
print("📋 데이터프레임 정보:")
print(df.info())

# 데이터 일부 미리 보기
print("\n🔍 상위 5개 행 미리보기:")
print(df.head())
