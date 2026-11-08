# 第14.1節：ChEMBL單一EGFR assay快照

資料供應者：ChEMBL / EMBL-EBI。原研究：Apsel B, Blair JA, Gonzalez B, Nazif TM, Feldman ME, Aizenstein B, Hoffman R, Williams RL, Shokat KM, Knight ZA. (2008). Targeted polypharmacology: discovery of dual inhibitors of tyrosine and phosphoinositide kinases. Nature Chemical Biology 4:691–699. DOI: https://doi.org/10.1038/nchembio.117 。

資料及本資料夾的整理投影採 **Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)**，https://creativecommons.org/licenses/by-sa/3.0/ 。授權來源：https://chembl.gitbook.io/chembl-interface-documentation/about 。這項授權標記適用於 ChEMBL 資料及衍生表格，不把原始論文全文或補充資料重新授權；本資料夾不收錄它們。

取得日：2026-11-06。API status回報 ChEMBL_37、release date 2026-05-01。這是下載日的固定投影，未宣稱整個遠端API永遠不變。保存資訊包含activities全部209筆（next=null）、來源文件欄位、assay欄位與API版本。原始摘要與聯絡欄位未納入。

## 來源

- 全量活動：https://www.ebi.ac.uk/chembl/api/data/activity.json?assay_chembl_id=CHEMBL1243977&limit=1000
- Assay：https://www.ebi.ac.uk/chembl/api/data/assay/CHEMBL1243977.json
- 文件：https://www.ebi.ac.uk/chembl/api/data/document/CHEMBL1240340.json
- 版本：https://www.ebi.ac.uk/chembl/api/data/status.json
- 原文方法：https://pmc.ncbi.nlm.nih.gov/articles/PMC2880455/ （In vitro kinase assays）

snapshot.json SHA-256：`a04b7320b86681ece8c6649723eb63d5a399879eef738d0b23c22f156432cad7`。

## 可比性與限制

單一重組EGFR、放射性磷酸轉移測試、10 µM ATP。ChEMBL格式為single protein format；confidence_score=8、relationship_type=H（homologous assignment），assay物種空白、variant_sequence=null。不可補寫已確認human wild-type，不把其他assay、細胞、物種或突變資料合併。原文另有細胞實驗，未納入。

API單一assay ID並非可比性的充分條件：初查的CHEMBL944276屬2009計算/QSAR研究，可能彙整舊文獻，因此未選。大assay CHEMBL5736995描述同時含兩種ATP/酵素濃度，未選。正式選用來源有明確生化方法及公開原文；仍無法由投影驗證每筆酵素批號、溫度與重複量測。

## 轉換與檔案

可獨立重現的程式在 `../../../notebooks/ch14/14-01-chembl-case-study.ipynb`。Notebook內嵌相同snapshot，核對SHA後執行。

`filter_audit.csv`：每活動一列，按程式檢查順序只記首個排除原因。209→缺數值39→非等號3→高於原文範圍30→137；沒有其他排除。原文濃度範圍0.001–50 µM，故保守只留1–50000 nM；低於下限的等號值為0筆。超範圍值保留原值，不擅自改為設限符號。排除缺值/設限/高濃度值造成選擇偏差，結果不是全候選庫評估。

`curated.csv`：FragmentParent、Uncharger、SanitizeMol後的isomeric canonical SMILES；未合併互變異構體。按整理後結構聚合中位pIC50，保留活動ID、筆數及範圍。本例137結構、50骨架，未發生結構聚合。這是另建分析欄位，原SMILES留在snapshot。

`metrics.csv`：固定三模型、只依validation MAE選定Random forest。train/valid/test = 95/14/28分子，30/10/10骨架，種子42/43。沒有看test改seed或參數，也沒有選完後重訓。原始資料核對時曾因試驗範圍問題修正清理規則；修正依據是原文方法，不是模型分數。

`ranking_before_reveal.csv`：不含測試標籤的固定排名；預測降冪、化合物ID升冪。`ranking_after_reveal.csv`：同名單、同順序加入觀測值與誤差。相似度提示為train內leave-one-out最近鄰Tanimoto第10百分位0.6607425441；不作為信賴區間。

`summary.json`：模型與分組摘要。前五名平均觀測pIC50=5.935927，全池=6.069936；前五名沒有pIC50≥7分子，全池有3個。門檻7只在揭露後描述，未用於選點或調參。此排序沒有顯示成功富集；並非新化合物發現。

所有圖由notebook產生，未使用論文圖片。
