# 化學資訊學入門：用 Python 與 RDKit 動手學

目前收錄第 0 至 15 章，共 93 節與 83 份 notebook。

線上閱讀：https://517justin.github.io/cheminfo-intro/

**驗證進度**：所有 notebook 都已在本機（Python 3.12.13）執行通過；在 Colab 實機驗證則在進行中，目前完成第 5 章的 5.2、5.3、5.4、5.6、5.7，其中 5.5 計算量大，仍在調整，其餘小節陸續補上。遇到問題歡迎開 issue。

- [第 0 章　前言](book/chapters/ch00/index.qmd)
- [第 1 章　分子怎麼存進電腦](book/chapters/ch01/index.qmd)
- [第 2 章　RDKit 基本操作](book/chapters/ch02/index.qmd)
- [第 3 章　化學資料庫](book/chapters/ch03/index.qmd)
- [第 4 章　分子描述符](book/chapters/ch04/index.qmd)
- [第 5 章　量子化學計算](book/chapters/ch05/index.qmd)
- [第 6 章　分子指紋與相似度](book/chapters/ch06/index.qmd)
- [第 7 章　比較分子結構](book/chapters/ch07/index.qmd)
- [第 8 章　化學空間視覺化](book/chapters/ch08/index.qmd)
- [第 9 章　QSAR 與機器學習：模型篇](book/chapters/ch09/index.qmd)
- [第 10 章　QSAR 與機器學習：評估與可信度篇](book/chapters/ch10/index.qmd)
- [第 11 章　模型解釋](book/chapters/ch11/index.qmd)
- [第 12 章　資料不夠怎麼辦：小數據與實驗設計](book/chapters/ch12/index.qmd)
- [第 13 章　讓資料用得起來：研究資料管理](book/chapters/ch13/index.qmd)
- [第 14 章　實戰專題](book/chapters/ch14/index.qmd)
- [第 15 章　進階與展望](book/chapters/ch15/index.qmd)
- [下載或瀏覽 notebook](book/notebooks)
- 章末綜合練習：[第 0 章](book/chapters/ch00/exercises.qmd)、[第 1 章](book/chapters/ch01/exercises.qmd)、[第 2 章](book/chapters/ch02/exercises.qmd)、[第 3 章](book/chapters/ch03/exercises.qmd)、[第 4 章](book/chapters/ch04/exercises.qmd)、[第 5 章](book/chapters/ch05/exercises.qmd)、[第 6 章](book/chapters/ch06/exercises.qmd)、[第 7 章](book/chapters/ch07/exercises.qmd)、[第 8 章](book/chapters/ch08/exercises.qmd)、[第 9 章](book/chapters/ch09/exercises.qmd)、[第 10 章](book/chapters/ch10/exercises.qmd)、[第 11 章](book/chapters/ch11/exercises.qmd)、[第 12 章](book/chapters/ch12/exercises.qmd)、[第 13 章](book/chapters/ch13/exercises.qmd)、[第 14 章](book/chapters/ch14/exercises.qmd)

在專案根目錄執行 `quarto render book`，再用瀏覽器開啟 `book/_book/index.html` 可閱讀完整排版。書稿使用 Quarto 1.10.20 建置。Notebook 採用 Colab 2026.07（Python 3.12.13）；需要 Psi4、xTB 或 NVIDIA GPU 的小節，請依各 notebook 第一格設定環境。

第 13 章使用固定 ORD 真實反應資料；來源、資料授權與重建方式見 [資料說明](book/data/ch13/README.md)。

第 14 章包含 ChEMBL EGFR 候選排序與反應條件選點兩個專題；分析表、圖表及完整資料隨附。資料來源與授權見 [ChEMBL 資料說明](book/data/ch14/chembl/README.md) 及 [反應資料說明](book/data/ch14/reaction/README.md)。兩份 notebook 已於本機 Python 3.12.13 執行通過，Colab 尚待實機驗證。

第 15 章保留十節，以圖表與案例導讀介紹深度學習、分子生成、大型語言模型與實驗自動化；不另設 notebooks、小練習或章末綜合練習。進階技術與應用的詳細內容將另行規劃。

第 0 章包含五節入門導覽、五份 ESOL 實作 notebooks、五張圖與練習。本機 Python 3.12.13 執行通過；Colab 尚待實機驗證。

## 授權

書稿與程式碼採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hant)，署名 517justin。第 3、13、14 章隨附的資料（ORD 反應資料、ChEMBL 快照等）維持各自的授權，範圍與衍生物的處理方式見 [LICENSE](LICENSE)。
