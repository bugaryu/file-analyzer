import os
import csv
import cv2
import sys
from PIL import Image
from datetime import datetime

# デフォルトの対象ディレクトリを指定
DEFAULT_TARGET_DIR="/path/to/your/directory"

# コマンドライン引数から対象ディレクトリを取得
target_dir = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else DEFAULT_TARGET_DIR

# 出力ファイルを指定
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"file_info_{timestamp}.csv"

# サポートされているファイル拡張子
IGNORE_PATH = ['folder']
IGNORE_PATH = []

with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([target_dir])
    writer.writerow(["no", "path", "フォルダパス", "フォルダ1", "フォルダ2", "フォルダ3", "フォルダ4", "ファイル名", "形式"])

    line = 0
    for root, dirs, files in os.walk(target_dir):
        # IGNORE_PATH に記載されたフォルダパス以下の階層は分析しない
        dirs[:] = [d for d in dirs if d not in IGNORE_PATH]
        # ファイルパスを出力
        for file in files:
            file_path = os.path.join(root, file)
            filename = os.path.basename(file_path)
            filetype = filename.split(".")[-1].lower() if "." in filename else ""

            root_relative = os.path.relpath(file_path, target_dir)
            folder_path = os.path.relpath(root, target_dir)  # フォルダパスを取得
            folder_parts = root_relative.split(os.sep)[:-1]  # ファイル名を除いた部分を取得
            if len(folder_parts) < 4:
                folder_parts += [""] * (4 - len(folder_parts))  # フォルダが4つ未満の場合は空文字で埋める
            else:
                folder_parts[3] = os.sep.join(folder_parts[3:])  # 余った部分をフォルダ4に結合
                folder_parts = folder_parts[:4]

            line += 1
            writer.writerow([line, root_relative, folder_path] + folder_parts + [filename, filetype])

