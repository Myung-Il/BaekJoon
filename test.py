import os
import re

# 절대 경로로 base_path 설정
base_path = r"C:\Users\Administrator\Desktop\BaekJoon\단계별_풀기"

for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)

    # 폴더가 디렉터리이고 이름이 '30_' 이상일 때만
    if os.path.isdir(folder_path) and re.match(r'^\d+_', folder_name):
        folder_num = int(folder_name.split('_')[0])
        if folder_num < 30:
            continue

        for filename in os.listdir(folder_path):
            # '인덱스_번호_이름.py' 형식만 매칭
            match = re.match(r'^\d+_(\d+_.+\.py)$', filename)
            if match:
                new_filename = match.group(1)
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)

                # 이름 바꾸기
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
