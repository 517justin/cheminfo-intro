# 14.2 反應選點回溯演練

資料來源：Perera et al. (2018), DOI [10.1126/science.aap9112](https://doi.org/10.1126/science.aap9112)；ORD：Kearnes et al. (2021), DOI [10.1021/jacs.1c09820](https://doi.org/10.1021/jacs.1c09820)。

沿用 `../../ch13/suzuki-ord-projection.json.gz`，並在 notebook 內嵌相同 gzip/base64 快照。原資料與投影採 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)，本目錄衍生資料維持相同授權，完整條款見 `../../ch13/LICENSE.txt`。程式為本書新寫，圖由 notebook 產生。

- ORD dataset：`ord_dataset-68cb8b4b2b384e3d85b5b1efae58b203`。
- 固定 commit：`2a6dff66c02f5d1c9b1589691f845b941c981a7a`。
- [原始檔](https://github.com/open-reaction-database/ord-data/blob/2a6dff66c02f5d1c9b1589691f845b941c981a7a/data/68/ord_dataset-68cb8b4b2b384e3d85b5b1efae58b203.pb.gz)。
- 原始 pb.gz SHA-256：`0cbcf613395e9bab0bd274f0ae81a73f4b230fbba557e4cf477d024407dcf8af`。
- 投影 gzip SHA-256：`02bacbe9789b2f818e82f75b2667396f236842e80bb48545f95ddaca367bb680`。

原投影保留 5,760 筆投入物、條件、結果與必要旗標，移除提交者聯絡資訊；沒有填補、重算或合成產率。本節從 15 組底物中，依兩個原始底物SMILES 的 tuple字典序取首組（不是按產率挑選），留下 384 筆。候選按 reaction_id 排序；12 種配體狀態 × 8 種鹼狀態 × 4 種主溶劑組合完整且唯一，None 分別有 32 及 48 筆。四種主溶劑股都固定 445.5 μL 有機溶劑及 49.5 μL 水；其他試劑股另帶溶劑，不能把此比例解讀為最終體積分率。溫度 100°C 及時間 1 分鐘固定。

預先固定：16 筆起始、總預算 48 筆、seed 0–9；GP 與 random共用起始索引。Random RNG seed 為 10000+seed。One-hot 共 24 欄，GP RBF長度尺度 1、alpha=0.01、optimizer=None、normalize_y=True；EI xi=0.01 百分點。每輪只用已觀察標籤。所有路徑完成才計算全網格最大值。沒有根據結果修改底物、預算、種子或模型設定。

輸出檔案：`candidate-conditions.csv`（候選索引依列順序，零起算）、`selection-log.csv`（10 seeds × 2 方法 × 48 步，共 960 列）、`seed-summary.csv`（48 筆結果）及 `summary.json`。資料欄位 yield_pct 和 best_observed 為分析產率百分比，difference_pp 為百分點。這些為既有結果的回溯選點紀錄，不是新增實驗；運行時間會依機器不同。

重現：以Python 3.12.13 執行 `book/notebooks/ch14/14-02-reaction-optimization.ipynb` 的全部四格。套件版本及 Colab 隔離安裝指令在首格；不需 ORD／protobuf、不需網路下載資料。本地已驗證，Colab 完整環境仍待實機確認。

「配體」沿用來源投入股分類；其中含兩個 AmPhos 膦片段與 Cl[Pd]Cl 的類別不是純游離配體。比較的是該股完整組成，不能將差異全歸因於配體本身。
