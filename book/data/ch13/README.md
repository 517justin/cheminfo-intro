# 第 13 章反應資料投影

來源：Perera et al., Science (2018), DOI [10.1126/science.aap9112](https://doi.org/10.1126/science.aap9112)；ORD：Kearnes et al., JACS (2021), DOI [10.1021/jacs.1c09820](https://doi.org/10.1021/jacs.1c09820)。

- 資料集：`ord_dataset-68cb8b4b2b384e3d85b5b1efae58b203`。
- 固定來源 commit：`2a6dff66c02f5d1c9b1589691f845b941c981a7a`（歷史快照）。
- [原始檔](https://github.com/open-reaction-database/ord-data/blob/2a6dff66c02f5d1c9b1589691f845b941c981a7a/data/68/ord_dataset-68cb8b4b2b384e3d85b5b1efae58b203.pb.gz)。
- 來源檔 SHA-256：`0cbcf613395e9bab0bd274f0ae81a73f4b230fbba557e4cf477d024407dcf8af`。
- 本資料投影 SHA-256：`02bacbe9789b2f818e82f75b2667396f236842e80bb48545f95ddaca367bb680`。

資料與此投影採 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)，全文附於 LICENSE.txt。保留全部 5,760 筆反應，選取 inputs、conditions、outcomes、DOI，以及 notes／observations 是否存在的旗標；移除提交者聯絡資訊。沒有補值、重新計算產率、加入虛構實驗或更正原始分析文字。這份投影不是完整原始檔，也不能替代原始色譜或實驗簿。

`extract_snapshot.py` 是作者重建工具，需另外安裝 ord-schema 0.9.6 與 protobuf 5.29.6；讀者 notebook 不需要這兩個套件。以 Python 3.12.13 執行：

```sh
python extract_snapshot.py source.pb.gz suzuki-ord-projection.json.gz
```

腳本會核對來源雜湊，再輸出固定排序與 gzip 時戳為零的 JSON 投影。四份 notebook 內嵌相同的 gzip/base64 資料並核對投影雜湊；每份都能獨立產生本節結果。Notebook 內的分析程式為本書新寫；嵌入的資料維持上述來源與資料授權。
