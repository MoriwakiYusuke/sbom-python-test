# Python SBOM 生成テスト環境

## 概要

このプロジェクトは,Microsoftの `sbom-tool` を使ってソフトウェア部品表 (SBOM) を生成するテストと学習のための,最小限のPython環境です.

依存関係が少ない2つのシンプルなライブラリ (`colorama` と `pyfiglet`) を利用し,最終的なSBOMにパッケージ依存関係がどのように記録されるかを確認することを目的としています.

## 前提条件

  * Python 3
  * pip
  * [Microsoft sbom-tool](https://github.com/microsoft/sbom-tool) がインストールされ,パスが通っていること

## セットアップ手順

1.  **リポジトリをクローンします.**

    ```bash
    git clone https://github.com/MoriwakiYusuke/sbom-python-test.git
    cd sbom-python-test
    ```

2.  **Pythonの仮想環境を作成し,有効化します.**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **必要なライブラリをインストールします.**

    ```bash
    pip install -r requirements.txt
    ```

## 使い方

### 1\. Pythonスクリプトの実行

プロジェクトが正しくセットアップされているか確認するために,以下のコマンドでサンプルスクリプトを実行します.

```bash
python src/main.py
```

ターミナルに色付きのASCIIアートが表示されれば成功です.

### 2\. SBOMの生成

以下のコマンドを実行して,SBOMを生成します.

```bash
sbom-tool generate \
    -b src \
    -bc . \
    -pn sbom-python-test \
    -pv 1.0.0 \
    -ps "Moriwaki Y" \
    -nsb "https://github.com/MoriwakiYusuke/sbom-python-test" \
    -m sbom-output \
    -D
```

  * `-b src`: スキャン対象のファイル群として`src`ディレクトリを指定します.
  * `-bc .`: 依存関係 (`requirements.txt`) の検出元としてプロジェクトルート (`.`) を指定します.
  * `-m sbom-output`: SBOMの出力先として`sbom-output`ディレクトリを指定します.

## 生成されるファイル

コマンドが成功すると,`sbom-output/_manifest/`ディレクトリの中にSPDX形式のSBOMファイルが生成されます.