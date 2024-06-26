# Dagster

## Intro

一個workflow Orchestrator(工作編排器) 
可自動執行一系列步驟並追蹤結果。
使團隊能夠查看步驟運行需要多長時間或它們如何與其他步驟連接
且能夠了解問題何時、何地以及為何發生。

## Why Dagster?

- 提供了與AWS , GCP的整合。(Azure: Dagster-cloud)
- 有官方Image,使得Docker環境下可以簡易運行。
- Kubernetes支援

### asset

可以是持久性儲存的物件 , 可以是 

- Table / View 
- 檔案 or blob storage (Ex: S3 , GCS)
- 機器學習模組

編寫程式碼來描述您想要存在的資產，以及該資產派生自的任何其他資產，以及可運行以計算該資產內容的函數。

Example : 
該資產是一個名為 的資料集topstories，它依賴另一個名為 的資產topstory_ids。topstories取得 中計算出的 ID topstory_ids，然後取得每個 ID 的資料。
```python
@asset(deps=[topstory_ids])
def topstories() -> None:
    with open("data/topstory_ids.json", "r") as f:
        topstory_ids = json.load(f)

    results = []
    for item_id in topstory_ids:
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        ).json()
        results.append(item)

        if len(results) % 20 == 0:
            print(f"Got {len(results)} items so far.")

    df = pd.DataFrame(results)
    df.to_csv("data/topstories.csv")
```

### Build asset DAG
