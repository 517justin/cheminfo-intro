# 第 1 章 Colab 實機驗證（2026-11-17）

第 1 章四份 notebooks 最終皆通過，共 12 個程式格與四張圖。1.3 初次執行失敗，修正繪圖後端後重跑通過；其餘三份原樣執行通過。這是實際 Colab 執行結果，不是以本機結果代替。

| 小節 | 結果 | 執行時間 | 核對內容 |
|---|---|---|---|
| 1.1 從結構式到分子圖 | 通過 | 85.61 秒 | 乙醇 `C2H6O (2, ['C'], 1)`；二甲醚 `C2H6O (1, ['C', 'C'], 0)`；ESOL 找到 `CCO` |
| 1.2 SMILES | 通過 | 15.45 秒 | `CCO` 與 `OCC` 均轉為 `CCO`；芳香與 Kekulé 苯酚均得到六個芳香原子；立體標記保留與省略符合預期 |
| 1.3 InChI 與 InChIKey | 修正後通過 | 9.02 秒 | 乙醇兩種寫法識別碼相同；二甲醚連接層不同；乳酸對映體完整識別碼不同 |
| 1.4 Mol 檔與 SDF | 通過 | 8.87 秒 | 讀回三筆結構、名稱、RecordID、logS、Endpoint 與 2D 標記均通過 notebook 內的斷言；三個紀錄分隔符號 |

1.4 實際輸出：

```text
Phenol ESOL-row-114 7 7 0.0
Anisole ESOL-row-694 8 8 -1.85
p-Cresol ESOL-row-1000 8 8 -0.73
record separators: 3
```

四份 notebook 各有三個非空執行編號，最終儲存的輸出無 error，且各有一個 PNG 顯示輸出。四張 PNG 均經 Pillow 解碼檢查通過。程式碼雜湊已與本機最終版本逐一比對一致，見 [remote-checks.json](remote-checks.json)；完整本機檔案版本見 [source-manifest.json](source-manifest.json)。

## 環境與驗證範圍

使用 Colab 2026.07、CPU、Python 3.12.13，實際映像為 `release-colab-external-images_20260715-060047_RC00`，詳見 [environment.json](environment.json)。四份 notebook 在同一 VM 依序執行，使用不同工作目錄；1.1、1.3、1.4 共用 `/content/ch01-book-env`，1.2 使用 `/content/ch01-smiles-env`。不是四次獨立乾淨 VM 測試。

原始程式格透過 Colab IPython 核心依序執行，先清除原有輸出。保留每份程式自行進行的版本斷言、套件安裝及 `pip check`。第一份環境安裝時間包含在 85.61 秒內；1.3 的表列時間是修正後、既有環境中的重跑時間。這些時間不包含 VM 分配與人工操作，不宜拿來比較小節計算效能。

## 1.3 的失敗與修正

初次執行 1.3 用時 6.74 秒，在匯入 Matplotlib 時失敗：獨立 Python 環境繼承了 Colab 的 `MPLBACKEND=module://matplotlib_inline.backend_inline`，該後端不可用。已在匯入 Matplotlib 前加入：

```python
import os
# 使用適合輸出圖檔的繪圖後端，避免沿用 Colab 的顯示設定。
os.environ["MPLBACKEND"] = "Agg"
```

重跑 1.3 的三個程式格後通過，產生識別碼比較圖。化學識別碼的計算與比較邏輯未改變。[初次結果](initial-results.json)保留失敗原因；先前的失敗不列為最終通過結果。

## 紀錄保存狀態

本目錄的結果與環境 JSON 由 Colab 頁面顯示的輸出轉錄，程式碼雜湊另與本機版本核對。這些檔案不是下載回來的已執行 notebooks。Colab 中的驗證筆記本已確認儲存所有變更，保留首次執行、錯誤、修正重跑及完整性檢查輸出。

完整已執行 notebooks、四張圖、兩套環境的套件清單、結果與環境檔已在 Colab 打包為 `/content/ch01-verified-20261117.zip`。瀏覽器執行「下載 .ipynb」後未收到下載檔案，因此**完整輸出封存檔尚未保存到本機**。VM 中的 ZIP 會隨執行階段回收而消失。本次 1.4 的 SDF 依原 notebook 保存在記憶體並印出首筆紀錄，沒有另行宣稱匯出了三筆 SDF 檔案。

本機保留驗證用 notebook、初始與最終來源版本、初次結果及核對紀錄。作者已於 2026-11-17 確認本次結果，核准將 README、驗證紀錄與 1.3 修正發布至教材庫。
