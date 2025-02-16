import os
import csv
import cv2
import sys
from PIL import Image
from datetime import datetime

# デフォルトの対象ディレクトリを指定
DEFAULT_TARGET_DIR="/path/to/your/directory"

# コマンドライン引数から対象ディレクトリを取得
target_dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET_DIR

# 出力ファイルを指定
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"file_info_{timestamp}.csv"

# サポートされているファイル拡張子
VIDEO_EXTENSIONS = ['mp4', 'mov', 'avi', 'mkv']
IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

def get_image_resolution(file):
    try:
        img = Image.open(file)
        return f"{img.width} x {img.height}"
    except Exception:
        return ""

def get_video_info(file):
    try:
        cap = cv2.VideoCapture(file)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        return f"{width} x {height}", duration
    except Exception:
        return "", ""

with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([target_dir])
    writer.writerow(["フルパス", "フォルダ1", "フォルダ2", "フォルダ3", "フォルダ4", "ファイル名", "ファイル形式", "解像度", "ファイルサイズ", "動画時間"])

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            filename = os.path.basename(file_path)
            filetype = filename.split(".")[-1].lower() if "." in filename else ""
            filesize = os.path.getsize(file_path)
            
            if filetype in VIDEO_EXTENSIONS:
                resolution, duration = get_video_info(file_path)
            elif filetype in IMAGE_EXTENSIONS:
                resolution = get_image_resolution(file_path)
                duration = "N/A"
            else:
                continue  # 動画、画像ファイル以外はスキップ

            root_relative = os.path.relpath(file_path, target_dir)
            folder_parts = root_relative.split(os.sep)[:-1] # ファイル名を除いた部分を取得 
            if len(folder_parts) < 4:
                folder_parts += [""] * (4 - len(folder_parts))  # フォルダが4つ未満の場合は空文字で埋める
            else:
                folder_parts[3] = os.sep.join(folder_parts[3:])  # 余った部分をフォルダ4に結合
                folder_parts = folder_parts[:4]

            writer.writerow([root_relative] + folder_parts + [filename, filetype, resolution, filesize, duration])
