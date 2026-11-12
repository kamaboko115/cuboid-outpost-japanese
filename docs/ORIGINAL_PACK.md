# 簡単導入版に含む原版データ

原作: **CuboidDroid / Cuboid Outpost 1.1.2**

- [原版の配布ページ](https://www.curseforge.com/minecraft/modpacks/cuboid-outpost/files/3777734)
- [対応する公式ソース](https://github.com/CuboidDroid/cuboidoutpost/tree/3d2a0e9967818cc00faee8faf7d61b6833782fad/src/overrides)
- [公式ライセンス](https://github.com/CuboidDroid/cuboidoutpost/blob/3d2a0e9967818cc00faee8faf7d61b6833782fad/LICENSE) / [同梱GPL-3.0本文](../LICENSES/GPL-3.0.txt)

原版overridesの572ファイルは、上記公式ソースと内容が一致することを確認しました（241件はバイト一致、331件は改行コードだけの違い）。この公開リポジトリの `modpack-base/overrides/` には、そのうち559ファイルを収録しています。[ファイル一覧とSHA-256](UPSTREAM_FILES.json)

## 2026-11-12の変更

- 原版の138 MOD依存関係（projectID / fileID）は維持し、本体JARは同梱せずランチャーが配布元から取得する形式にしました。
- パック名・バージョン・作者表記に、非公式の日本語化版であることを追記しました。
- Minecraft 1.16.5 / Forge 36.2.26は維持し、推奨メモリー4,096MBをmanifestへ追加しました。
- 日本語リソースパックと、翻訳済みサーバーガイドを追加しました。ガイドの `book.json` は日本語版に置き換えます。
- 最小限の `options.txt` を追加し、Minecraftの言語を日本語、日本語リソースパックを有効にした初期設定としました。個人のキー設定やアカウント情報は含みません。
- 下記13個の生成物・未使用ファイルを省略しました。レシピ、クエスト判定、進行条件、開始拠点の本体テンプレートは維持しています。

## 省略した原版ファイル

- `config/fancymenu/locals/` の言語キャッシュ5ファイル
- `config/fancymenu/menu_identifiers.db`
- `config/konkrete/locals/` の言語キャッシュ4ファイル
- `config/skyblockbuilder/template.nbt.bak`（未使用バックアップ。本体 `template.nbt` は収録）
- `kubejs/assets/kubejs/textures/` にある未参照の `example_block.png` / `example_item.png`

FancyMenu・Konkreteの上記キャッシュはMOD自身が起動時に生成することを、対象バージョンの実装で確認しました。これらMOD由来のキャッシュを原版作者の独自作品として再配布しないために除外しています。

## ライセンスの範囲

原版のパック固有設定・スクリプト・素材には、公式ソースに付されたGPL-3.0を適用します。翻訳リソース内の各MOD翻訳は、それぞれのライセンスを維持します。詳細は [第三者表記](../THIRD_PARTY_NOTICES.md)を参照してください。

本配布は非公式の日本語化プリセットです。CuboidDroid本人のリリースを名乗るものではありません。
