# Cuboid Outpost 日本語化

**Cuboid Outpost 1.1.2（通常版 / Minecraft 1.16.5）**向けの非公式日本語化です。クエスト、MODの画面・ツールチップ、Tinkers' Constructの説明書を日本語で読めるようにします。

**[簡単導入版をダウンロード](https://github.com/kamaboko115/cuboid-outpost-japanese/releases/download/v1.1.0/Cuboid-Outpost-1.1.2-Japanese-Easy-Import-v1.1.0.zip)** ・ [配布ファイル一覧](https://github.com/kamaboko115/cuboid-outpost-japanese/releases/latest)

原作は [CuboidDroid / Cuboid Outpost](https://www.curseforge.com/minecraft/modpacks/cuboid-outpost)。Minecraft 1.20.1のLuxury Editionには対応していません。

## 新しく始める人：Prismへ1回インポート

1. 上の **簡単導入版** ZIPをダウンロードします。解凍は不要です。
2. Prism Launcherの「インスタンスを追加」→「インポート」で、そのZIPを選びます。
3. 必要なMODの取得が終わったら起動します。

**原版パック、日本語表示、翻訳パックの有効化、サーバーガイドまで含めて設定されます。** 原版を先に入れたり、翻訳ファイルを別のフォルダーへコピーしたりする必要はありません。操作キーは原版の標準設定です。

これは新しいインスタンスを作るためのZIPです。すでに遊んでいるワールドへ適用する場合は、下の「既存パックに日本語化を追加」を使ってください。

MOD本体138個は原作者のCurseForge配布ファイルをPrismが取得します。配布元が外部ランチャーからの取得を制限している場合は、Prismの案内に従って対象ファイルをダウンロードしてください。ダウンロードや初回起動の所要時間は回線・PCによります。

Javaの自動選択を無効にしている場合はJava 8を使用してください。メモリー不足で起動できない場合は、インスタンスのメモリー上限を4～6GBに設定してください。

## 対応範囲

| 内容 | 公開版に含む翻訳 |
| --- | ---: |
| クエスト本文・タイトルなど | 4,421言語キー（1,511クエスト） |
| MODの表示・操作説明など | 5,646言語キー / 66名前空間 |
| Tinkers' Constructの説明書 | 386 JSONファイル |
| マルチ用サーバーガイド | 5ページ・分類ファイル + 表紙定義（簡単導入版に同梱、個別ZIPもあり） |

既存MODに同梱された日本語名を優先して用語を合わせています。独自素材・機械名などの固有名は、英語表記を残しているものがあります。

公開版には、翻訳の再配布条件を確認できたファイルを収録しています。**34名前空間の追加翻訳は未収録**です。[未収録一覧](docs/OMITTED_TRANSLATIONS.md)に理由を記載しています。該当MODは、元から同梱されている日本語または英語で表示されます。

未収録一覧にある `ftbquests` はMOD本体の追加UI翻訳です。**Cuboid Outpostのクエスト本文・タイトル4,421項目はすべて収録**しています。

## 既存パックに日本語化を追加

1. 先に[原版Cuboid Outpost 1.1.2](https://www.curseforge.com/minecraft/modpacks/cuboid-outpost/files/3777734)を導入してください。PrismではCurseForgeからの追加、または原版ZIPのインポートを使えます。
2. [Releases](https://github.com/kamaboko115/cuboid-outpost-japanese/releases/latest)の `Cuboid-Outpost-1.1.2-Japanese-v1.1.0.zip` をダウンロードします。
3. 対象インスタンスのMinecraftフォルダーにある `resourcepacks` へ、**解凍せず**に入れます。Prismのインスタンス用ZIPとしてインポートするファイルではありません。
4. ゲームを起動し、設定から言語を「日本語」にします。
5. リソースパック設定でこのパックを有効にし、他の翻訳パックより上に置きます。

クエスト判定・報酬・レシピやキー設定を変更する作業はありません。MOD本体やMinecraft本体はこの配布物には含まれません。

### サーバーガイドも日本語にする場合

**簡単導入版には導入済みです。** 既存パックへ個別に追加する場合は、外部Patchouliブックのためこちらの別ファイルを使います。マルチ参加者はそれぞれ導入してください。サーバー側にも導入する場合は管理者が同じ手順で配置します。

1. ゲーム（サーバーの場合はサーバー）を終了します。
2. 対象フォルダーの `patchouli_books/cuboidoutpost_server_guide` をバックアップします。
3. `Cuboid-Outpost-1.1.2-ServerGuide-Japanese-v1.1.0.zip` を解凍し、中の **`patchouli_books` フォルダー**をMinecraftフォルダー（サーバーならサーバーのルート）へコピーして統合します。
4. `book.json` の上書きを確認し、再起動します。

この別ZIPはリソースパックとして有効にするものではありません。表紙のタイトルと導入文は `book.json` の直接置換なので、英語設定でも日本語になります。

### 元に戻す

リソースパック設定で無効にし、必要ならZIPを削除してください。サーバーガイドは、ゲームを終了してから現在の `cuboidoutpost_server_guide` フォルダーを別の場所へ移し、バックアップしたフォルダーを元の位置に戻してください。上書きで統合するだけだと、追加した `ja_jp` フォルダーが残ります。

## 翻訳と確認

AIを使って原文から翻訳し、既存の日本語表記と照合しました。翻訳対象の言語キー、書式記号、参照先、書籍の構造を検査し、固有名が途中だけ訳される問題や章名の不一致などを修正しています。

元になったローカル版では起動・マルチ接続を確認し、利用者から実プレイで問題がなかったとの報告を受けています。公開版はそこから配布可能な翻訳を取り出したもので、収録した訳文は同一です。全ページの目視確認や全クエストのクリア検証は行っていません。[検証内容](docs/VALIDATION.md)も参照してください。

固有名、単位、コマンド、FancyMenuの編集画面などには英語が残ります。誤訳や表示の不具合は、このリポジトリの[Issues](https://github.com/kamaboko115/cuboid-outpost-japanese/issues)へ、章・クエスト名や表示文と一緒に報告してもらえると助かります。

## 編集・ビルド

日本語の翻訳データは `resourcepack/assets/` と `server-guide/patchouli_books/` にあるUTF-8のJSONです。修正したい文章を直接編集できます。

このリポジトリを取得し、そのルートでPython 3.10以降を使って次を実行すると、`dist/` に配布ZIPとSHA-256一覧を生成します。

```sh
python build.py
```

## 権利表記

本プロジェクトは原作者や各MOD作者の公式配布物ではありません。原文・元データ・既存翻訳の権利は各作者・貢献者に帰属します。

翻訳ファイルは、対応する原作のライセンス条件を引き継ぎます。ファイル群ごとの出典・作者・ライセンスは [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)、原文は `LICENSES/` に収録しています。[LICENSE.md](LICENSE.md)も参照してください。
