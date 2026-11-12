# 確認した範囲

## 翻訳の元になったローカル版

- 対象は Cuboid Outpost 1.1.2 / Minecraft 1.16.5 / Forge 36.2.26。
- クライアントとサーバーの原版MOD、レシピ・スクリプト・クエスト定義を各293ファイル照合し、変更がないことを確認。
- 起動および認証付きマルチ接続のスモークテストを実施。
- その後の翻訳不具合修正では、固有名保護・色コード・章名参照・書式引数の順序・書籍の表示フィールドに関する9件の回帰テストを実施し、すべて通過。
- 修正後のパックを読み込んでメニュー到達・正常終了を確認。言語JSONや設定の読み込みエラーは検出されず。
- 利用者から「実際にプレイして問題がなかった」との報告あり。プレイ範囲・到達地点は未確認。

接続テストは翻訳不具合修正前の版、修正後はクライアント起動確認です。全クエストのクリアや全説明書ページの目視確認ではありません。

## 今回の公開版

上記ローカル版から、再配布条件を確認できた翻訳を選んで収録しています。公開版として改めてゲーム全体をプレイしたわけではありません。

- 収録した言語JSON・Tinkers書籍JSONは、ローカル版とバイト単位で一致。
- 別ZIPのサーバーガイド6ファイルは、ローカル版とJSON内容が一致。
- 未収録にした名前空間のデータやMOD本体が含まれないことを確認。
- JSONの読み込み、ZIPのCRC、配布ファイルのSHA-256、文書のローカルリンクを検査。
- 個人のPCパス・アカウントメール・認証トークン・ワールド・ログを含まないことを検査。

配布物のハッシュはReleaseに添付した `SHA256SUMS.txt` を参照してください。公開版では一部の追加MOD翻訳を省いているため、ローカル版より英語表示が多くなる場合があります。

## 1.1.0 簡単導入版

- 元の配布manifestと138件のprojectID / fileIDが完全一致。
- 原版overrides 572ファイルを公式ソースと照合。生成キャッシュ等13件を省き、559件をそのまま収録。サーバーガイドの表紙定義のみビルド時に既存の日本語版を重ねる。
- 日本語パックの内包、有効化設定、Minecraft設定のデータバージョン2586、ガイド6ファイル、開始拠点のtemplate.nbtを検査。
- Prism 11.1.1の公式実装で、CurseForge manifestの認識、overrides/options.txtの保持、recommendedRamによる4GB指定を確認。
- `python build.py` と `python verify_import.py` で、ファイル配置・原版ハッシュ・ZIPのCRC・SHA-256を検査可能。
- 簡単導入ZIPそのものをPrismへ新規インポートし、全MOD取得からゲーム起動まで行う実機テストは未実施。

仕様確認の出典: [manifestパーサー](https://github.com/PrismLauncher/PrismLauncher/blob/11.1.1/launcher/modplatform/flame/PackManifest.cpp)、[overridesとメモリー設定](https://github.com/PrismLauncher/PrismLauncher/blob/11.1.1/launcher/modplatform/flame/FlameInstanceCreationTask.cpp)、[ZIP形式判定](https://github.com/PrismLauncher/PrismLauncher/blob/11.1.1/launcher/InstanceImportTask.cpp)。
