# ファイルアナライザー

このプログラムは、指定されたディレクトリ内の画像および動画ファイルの情報を収集し、CSVファイルに出力します。収集する情報には、ファイルパス、フォルダ階層、ファイル名、ファイル形式、解像度、ファイルサイズ、および動画の長さが含まれます。

## インストール

必要なライブラリをインストールするには、以下のコマンドを実行してください:

```bash
pip install -r requirements.txt
```

## 使用方法

1. `analyze_media_file.py` スクリプトを実行します。対象ディレクトリを引数として指定することもできます。
    ```bash
    python analyze_media_file.py /path/to/your/directory
    ```
    引数を指定しない場合、デフォルトのディレクトリが使用されます。
2. スクリプトは指定されたディレクトリ内のサブディレクトリも含めてすべての画像および動画ファイルを検索し、情報を収集します。
3. 収集された情報は `file_info_<timestamp>.csv` ファイルに出力されます。

## 出力例

`file_info_<timestamp>.csv` ファイルには以下のような情報が含まれます:

```
フルパス, フォルダ1, フォルダ2, フォルダ3, フォルダ4, ファイル名, ファイル形式, 解像度, ファイルサイズ, 動画時間
/path/to/file, folder1, folder2, folder3, folder4, example.jpg, jpg, 1920 x 1080, 204800, N/A
/path/to/file, folder1, folder2, folder3, folder4, example.mp4, mp4, 1920 x 1080, 1048576, 60.0
```
