# 論文のスクレイピング
主要論文を検索して、Abstractから重要な情報を抜き出す.
今回は、ナトリウムイオン電池のカソードの電極容量についてのデータを抜き出す. 

## 使い方
自分の環境にソースコードをクローンする.
```
git clone ""
cd WebScraping
#主要なライブラリインストール
./env.sh
#実行
python -m main.py
```

実行後、[Output](Output)にアクセスするとスクレイピング後の結果がjsonファイルとして出力される.
```json
{
    "id1": {
        "title": "Tuning local chemistry of P2 layered-oxide cathode for high energy and long cycles of sodium-ion battery | Nature Communications",
        "url": "https://www.nature.com/articles/s41467-021-22523-3",
        "publisher": "Nature",
        "capacity": {
            "id1": "240.5 mAh g\u22121"
        }
    },
    "id2": {
        "title": "Boron-doped sodium layered oxide for reversible oxygen redox reaction in Na-ion battery cathodes | Nature Communications",
        "url": "https://www.nature.com/articles/s41467-021-25610-7",
        "publisher": "Nature",
        "capacity": {
            "id1": "160.5 mAh g\u22121"
        }
    },
    "id3": {
        "title": "Advanced rechargeable aluminium ion battery with a high-quality natural graphite cathode | Nature Communications",
        "url": "https://www.nature.com/articles/ncomms14283",
        "publisher": "Nature",
        "capacity": {
            "id1": "110\u2009mAh\u2009g\u22121",
            "id2": "60\u2009mAh\u2009g\u22121"
        }
    },
    "id4": {
        "title": "Sustainability-inspired cell design for a fully recyclable sodium ion battery | Nature Communications",
        "url": "https://www.nature.com/articles/s41467-019-09933-0",
        "publisher": "Nature",
        "capacity": {}
    }
}
```