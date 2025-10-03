# Python SBOM 生成テスト環境

## 概要

このプロジェクトは,複数のSBOM（ソフトウェア部品表）生成ツールをテストし,比較・学習するための最小限のPython環境です.

依存関係が少ない2つのシンプルなライブラリ (`colorama` と `pyfiglet`) を利用し,各ツールで生成されるSBOMにパッケージ依存関係がどのように記録されるかを確認することを目的としています.

## ディレクトリ構成

```
.
├── sbom-output/              # 各ツールで生成されたSBOMの出力先
│   ├── dependency-graph/     # githubの依存関係グラフ
│   ├── sbom-tool/            # sbom-toolの出力
│   └── syft/                 # syftの出力
├── src/
│   └── main.py               # サンプルスクリプト
├── .gitignore
├── README.md
└── requirements.txt
```

## 前提条件

  * Python 3
  * pip
  * 各種SBOMツール (例: [Microsoft sbom-tool](https://github.com/microsoft/sbom-tool), [Syft](https://github.com/anchore/syft)) がインストールされ,パスが通っていること

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

### 1. Pythonスクリプトの実行

プロジェクトが正しくセットアップされているか確認するために,以下のコマンドでサンプルスクリプトを実行します.

```bash
python src/main.py
```

ターミナルに色付きのASCIIアートが表示されれば成功です.

### 2. SBOMの生成

#### 2.1. Microsoft sbom-tool

以下のコマンドを実行して,SBOMを生成します.

```bash
sbom-tool generate \
    -b src \
    -bc . \
    -pn sbom-python-test \
    -pv 1.0.0 \
    -ps "Moriwaki Y" \
    -nsb "https://github.com/MoriwakiYusuke/sbom-python-test" \
    -m sbom-output/sbom-tool \
    -D
```

  * `-b src`: スキャン対象のファイル群として`src`ディレクトリを指定します.
  * `-bc .`: 依存関係 (`requirements.txt`) の検出元としてプロジェクトルート (`.`) を指定します.
  * `-m sbom-output/sbom-tool`: SBOMの出力先として`sbom-output/sbom-tool`ディレクトリを指定します.

#### 2.2. Syft

以下のコマンドを実行して,SPDX-JSON形式のSBOMを生成します.

```bash
syft dir:./ --exclude './venv/**' -o spdx-json > sbom.json
```

## 生成されるファイル

コマンドが成功すると,`sbom-output/`ディレクトリの中に各ツールに応じたSBOMファイルが生成されます.

*   **sbom-tool:** `sbom-output/sbom-tool/_manifest/` 内にSPDX形式のファイルが生成されます.
*   **syft:** `./` 内に `sbom.json` が生成されます.