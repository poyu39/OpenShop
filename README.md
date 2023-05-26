# OpenShop

## 設定環境

### Vscode Python 虛擬環境

### 建立虛擬環境
```
python -m venv venv
```

#### 啟動虛擬環境
```
.\venv\Scripts\Activate.ps1
```

#### 安裝套件
```
pip install -r .\env\requirements.txt
```

#### 關閉虛擬環境
```
deactivate
```

### Python 套件清單

#### pip 生成 requirements.txt

```
pip freeze > .\env\requirements.txt
```

#### pip 使用 requirements.txt

```
pip install -r .\env\requirements.txt
```

### Django 設定

#### 使用 XAMPP MySQL

### 建立資料庫與使用者

檔案路徑: `framework\baykeshop\conf\default.py`

建議新增 `openshop` 資料庫與 `openshop` 使用者

使用者需設定密碼

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'openshop',
        'USER': 'openshop',
        'PASSWORD': '9239',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```