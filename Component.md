# Component

### Dagster-Instance

Dagster實例定義了Dagster對單一部署所需的配置 

EX:儲存過去運行及其相關日誌的歷史記錄的位置，從操作計算函數流出原始日誌的位置，以及如何啟動新的task。

構成您的Dagster部署的所有進程和服務應共享一個名為 `dagster.yaml` 的實例配置文件，以便它們可以有效地共享信息。

### Default local behavior

當 Dagster process (webserver or Dagster CLI commands) 執行 , Dagster tries to load your instance. 

如果環境變數DAGSTER_HOME設定, Dagster looks for an 
instance config file at `$DAGSTER_HOME/dagster.yaml.`

This file contains the configuration settings that make up the instance.

如果沒有設定, Dagster tools will use a `temporary directory` for storage that is cleaned up when the process exits. 

This can be useful when using Dagster for temporary local development or testing, when you don't care about the results being persisted.

如果DAGSTER_HOME 設定了 , 但 dagster.yaml 不存在, 
Dagster will persist data on the local filesystem, structured like the following:

```
$DAGSTER_HOME
├── dagster.yaml
├── history
│   ├── runs
│   │   ├── 00636713-98a9-461c-a9ac-d049407059cd.db
│   │   └── ...
│   └── runs.db
└── storage
    ├── 00636713-98a9-461c-a9ac-d049407059cd
    │   └── compute_logs
    │       └── ...
    └── ...
```

