# anthyをデバッグするには

## ファイルの場所

- ソースコード
    - https://salsa.debian.org/debian/anthy
- ドキュメント
    - https://salsa.debian.org/debian/anthy/-/tree/master/doc

## デバッグの仕方

### かな漢字変換のテスト方法

- anthy-agentを使う
    - https://salsa.debian.org/debian/anthy/-/blob/master/doc/MISC デバッグの方法

<pre>

$ echo -e "honjitsuohaisogasi(space) \nPRINT_CONTEXT" | anthy-agent | nkf
(3 ((UL RV) "本日" 0 3) ((UL) "おは" 0 6) ((UL) "急がし" 0 3))
(2 ((COMMIT) "本日おは急がし") ((UL) "鐚 -1 -1) cursor)

</pre>

## システム辞書の読み込み

- （後回し）

## ユーザ辞書の読み込み

- 調査中

## やり残している作業

- W: anthy: no-manual-page usr/bin/anthy-agent
- W: anthy: no-manual-page usr/bin/anthy-dic-tool

## 追加でできるようにしたいこと

- ユーザ辞書にUnicode-13.1の絵文字を設定しても変換できない文字がある
    - 詳細は調査中

