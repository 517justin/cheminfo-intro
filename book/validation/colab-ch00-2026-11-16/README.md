# 第 0 章 Colab 實機驗證（2026-11-16）

五份 notebook、共 15 個程式格皆執行通過。驗證的是本次修正後的教材程式；各份程式碼的 SHA-256 已與本機教材逐一比對一致，見 [檢查結果](remote-checks.json)。

| 小節 | 結果 | 本次重跑時間 | 核對內容 |
| --- | --- | --- | --- |
| 0.1 什麼是化學資訊學 | 通過 | 14.23 秒 | ESOL 1,128 筆；前三筆紀錄及結構圖 |
| 0.2 應用領域 | 通過 | 10.94 秒 | 1,128 筆；MW 範圍 16.043–780.949；logS 範圍 −11.6–1.58 |
| 0.3 研究痛點 | 通過 | 11.22 秒 | 1,128 筆皆可解析；1,117 種標準化結構；22 筆紀錄涉及重複結構 |
| 0.4 閱讀指南 | 通過 | 10.35 秒 | 依條件從 1,128 筆選出 331 筆 |
| 0.5 用 Colab 免安裝開始 | 通過 | 10.23 秒 | 前三筆結構圖與 `first-molecules.csv`；欄位為 row_id、smiles、MW、logS |

五張 PNG 均已在 Colab 以 Pillow 解碼檢查通過。CSV 已在 Colab 讀回，確認包含表頭與三筆資料。MW 為分子量，數值對應 g/mol；logS 為以 mol/L 表示溶解度後取以 10 為底的對數。

## 環境與範圍

- Colab CPU，選擇 2026.07；Python 3.12.13。
- 實際映像：`release-colab-external-images_20260715-060047_RC00`。
- RDKit 2026.9.1、DeepChem 2.8.1.dev20260821122258、NumPy 1.26.4、pandas 3.0.6、Matplotlib 3.11.2、SciPy 1.17.1、scikit-learn 1.9.1。
- 五份 notebook 的程式格依原順序透過實際 Colab IPython 核心執行，先清除舊輸出。各份使用不同工作目錄，但共用同一 CPU 執行階段及 `/content/ch00-book-env` 套件環境，並非五次獨立乾淨安裝。
- 表列時間為修正後、已有套件環境的重跑時間，包含各份 notebook 的環境檢查，不含首次安裝、執行階段分配與人工操作時間；不作為不同模型或平台的效能比較。

## 本次修正

初次驗證時，Colab 的 `MPLBACKEND=module://matplotlib_inline.backend_inline` 被傳入獨立 Python 環境，使 Matplotlib 在載入時中止。五份 notebook 均改為在匯入 Matplotlib **之前**設定 `MPLBACKEND=Agg`，再重跑通過。原本在匯入後呼叫 `matplotlib.use("Agg")` 無法處理這個載入階段錯誤。資料處理與分析條件未變更。

驗證工具也修正了 notebook JSON 的讀取方式：先前直接讀成物件，未把分行 source 轉為程式字串；此工具錯誤發生於教材程式執行之前，修正後才進行上述驗證。

## 紀錄保存狀態

本目錄的 JSON 是從 Colab 顯示的檢查結果轉錄，再與本機程式碼核對的紀錄，不是下載回來的已執行 notebook。`source-manifest.json` 記錄本機驗證版本的檔案雜湊。

完整已執行 notebooks、圖檔、CSV、環境與套件清單已在 Colab 封存為 `/content/ch00-verified-20261116.zip`。本次瀏覽器安全政策阻擋 data URL 下載，**完整封存檔尚未保存到本機或納入教材庫**；Colab 執行階段結束後，暫存檔可能消失。此限制不影響已觀察到的執行與完整性檢查結果，但不能把本目錄當作完整原始輸出封存。
