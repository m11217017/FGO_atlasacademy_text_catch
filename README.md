# 🎌 FGO Atlas Academy 劇情文本採集器

一個專門用於從 [Atlas Academy](https://apps.atlasacademy.io) 下載 Fate/Grand Order 完整主線劇情文本的自動化工具。

## ✨ 功能特色

- 🚀 **完整覆蓋**: 支援 FGO 全部主線劇情（第一部 + 第二部）
- 📖 **智能下載**: 直接從 Atlas Academy API 獲取原始劇本檔案
- 🔄 **批量處理**: 支援單章節和批量下載模式
- 📊 **進度追蹤**: 實時顯示下載進度和統計資訊
- 📁 **檔案整理**: 自動按章節分類整理檔案
- 🛠️ **錯誤處理**: 智能重試和錯誤恢復機制
- ⏱️ **速率限制**: 內建延遲機制，避免對伺服器造成負擔

## 📚 支援內容

### 🔥 第一部 (特異點系列)
- ✅ 特異點F：燃燒污染都市 冬木
- ✅ 第一特異點：邪龍百年戰爭 奧爾良  
- ✅ 第二特異點：永續瘋狂帝國 七丘之城
- ✅ 第三特異點：封鎖終局四海 俄刻阿諾斯
- ✅ 第四特異點：死界魔霧都市 倫敦
- ✅ 第五特異點：北美神話大戰 合眾為一
- ✅ 第六特異點：神聖圓桌領域 卡美洛
- ✅ 第七特異點：絕對魔獸戰線 巴比倫尼亞
- ✅ 終局特異點：冠位時間神殿 所羅門

### 🌟 第二部 (Cosmos in the Lostbelt)

**亞種特異點 (4章)**
- ✅ 亞種特異點Ⅰ：惡性隔絕魔境 新宿
- ✅ 亞種特異點Ⅱ：傳承地底世界 雅戈泰
- ✅ 亞種平行世界：屍山血河舞台 下總國
- ✅ 亞種特異點Ⅳ：禁忌降臨庭園 塞勒姆

**第二部序章與Lostbelt (8章)**
- ✅ 序：2018年12月26日
- ✅ Lostbelt No.1：永久凍土帝國 安娜塔西亞
- ✅ Lostbelt No.2：無間冰焰世紀 諸神黃昏
- ✅ Lostbelt No.3：人智統合真國 SIN
- ✅ Lostbelt No.4：創世滅亡輪迴 宇迦剎多羅
- ✅ Lostbelt No.5：神代巨神海洋 亞特蘭提斯
- ✅ Lostbelt No.5：星間都市山脈 奧林帕斯
- ✅ Lostbelt No.6：妖精圓桌領域 阿瓦隆勒菲
- ✅ Lostbelt No.7：黃金樹海紀行 太陽紀米克特蘭

**特殊章節 (4章)**
- ✅ 地獄界曼荼羅：平安京
- ✅ 非靈長生存圈：通古斯聖域
- ✅ 死想顯現界域：Traum

**奏章 (3章)**
- ✅ 奏章 序
- ✅ Ordeal Call
- ✅ 虛數羅針內界：平面之月

## 📊 下載統計

- **總章節數**: 28個章節
- **總檔案數**: 2,177個劇情腳本檔案
- **檔案格式**: UTF-8 編碼的原始劇本文件 (.txt)

## 🛠️ 專案結構

```
FGO_atlasacademy_text_catch/
├── fgo_text_collector.ipynb    # 主要 Jupyter Notebook
├── story/                      # 下載的劇情檔案
│   ├── 特異點F_燃燒污染都市_冬木/
│   ├── 第一特異點_邪龍百年戰爭_奧爾良/
│   ├── ...
│   ├── 亞種特異點Ⅰ_惡性隔絕魔境_新宿/
│   ├── Lostbelt_No1_永久凍土帝國_安娜塔西亞/
│   └── ...
├── war_*_data.json            # 戰爭 API 數據快取
├── requirements.txt           # Python 依賴套件
└── README.md                  # 專案說明
```

## 🚀 快速開始

### 環境需求

- Python 3.7+
- Jupyter Notebook 或 VS Code
- 網路連接

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 使用方法

1. **打開 Jupyter Notebook**
   ```bash
   jupyter notebook fgo_text_collector.ipynb
   ```

2. **執行所有 cells 進行設定**

3. **選擇下載模式**：
   - **單章節下載**: 使用 `download_singularity_by_war_id(war_id, war_name)`
   - **第一部批量下載**: 使用 `download_all_singularities()`
   - **第二部批量下載**: 使用 `download_part2_all_chapters()`
   - **完整下載**: 使用 `download_complete_fgo_story()`

### 範例：下載特定章節

```python
# 下載特異點F
success, failed = download_singularity_by_war_id(100, "特異點F_燃燒污染都市_冬木")

# 下載 Lostbelt No.1
success, failed = download_singularity_by_war_id(301, "Lostbelt_No1_永久凍土帝國_安娜塔西亞")
```

### 範例：批量下載

```python
# 下載第一部所有章節
part1_results = download_all_singularities()

# 下載第二部所有章節
part2_results = download_part2_all_chapters()

# 下載完整主線劇情
complete_results = download_complete_fgo_story()
```

## 📋 依賴套件

- `requests`: HTTP 請求處理
- `pathlib`: 檔案路徑操作
- `json`: JSON 數據處理
- `time`: 延遲控制
- `re`: 正則表達式處理

## ⚙️ 技術細節

### API 端點
- **戰爭數據**: `https://api.atlasacademy.io/nice/TW/war/{war_id}`
- **劇本檔案**: `https://static.atlasacademy.io/TW/Script/{script_id[:2]}/{script_id}.txt`

### 檔案命名規則
- **目錄名稱**: 使用安全字符替換特殊符號
- **檔案名稱**: `raw_script_{script_id}.txt` 格式
- **腳本ID**: 10位數字格式 (例如: 0100000010)

### 速率限制
- 每次請求間隔 1.5 秒
- 自動重試機制
- 錯誤恢復處理

## 📈 使用統計

經測試，完整下載所有主線劇情約需：
- **執行時間**: 5-30 分鐘（取決於網路速度）
- **檔案大小**: 約 1-10 MB
- **成功率**: 99%+ （基於 Atlas Academy API 穩定性）

## 🤝 貢獻

歡迎提交 Pull Request 或回報問題！

### 如何貢獻
1. Fork 此專案
2. 創建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

## ⚠️ 注意事項

- 本工具僅供學習和研究用途
- 請遵守 Atlas Academy 的使用條款
- 下載大量檔案時請保持合理的請求頻率
- 建議在非高峰時段進行批量下載

## 📄 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

## 🙏 致謝

- [Atlas Academy](https://apps.atlasacademy.io) 提供的優秀 API 服務
- FGO 社群的支援和回饋
- 所有貢獻者的努力

---

**免責聲明**: 本工具與 TYPE-MOON、Aniplex 或 Lasengle 沒有官方關聯。Fate/Grand Order 是相關公司的註冊商標。
