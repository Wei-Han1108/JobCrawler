# JobCrawler

一个强大的多源职位爬虫系统，支持从多个主流招聘网站和 Google 搜索获取职位信息。
## 输出csv文件
![image](https://github.com/user-attachments/assets/ccba4114-21aa-4a8a-bde6-9d795f31bb72)

## 功能特点

- 支持多个数据源：
  - LinkedIn
  - Indeed
  - Glassdoor
  - ZipRecruiter
  - Google Jobs


- 强大的搜索功能：
  - 关键词搜索
  - 地理位置过滤
  - 工作类型过滤
  - 时间范围过滤
  - 远程工作过滤
  - 自定义搜索条件

- 数据整合：
  - 自动去重
  - 统一数据格式
  - 多源数据合并
  - 支持导出为 CSV

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/JobCrawler.git
cd JobCrawler
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 基本使用

```python
from src import scrape_jobs

# 基本搜索
jobs = scrape_jobs(
    site_name=["google", "linkedin", "indeed"],
    search_term="python developer",
    results_wanted=10
)

# 保存结果
jobs.to_csv("jobs.csv", index=False)
```

### 高级使用

```python
from src import scrape_jobs

# 高级搜索
jobs = scrape_jobs(
    site_name=["google", "linkedin"],
    search_term="python developer",
    google_search_term="python developer jobs remote",  # 自定义 Google 搜索词
    location="New York",
    distance=50,  # 搜索半径（英里）
    is_remote=True,  # 仅远程工作
    job_type="fulltime",  # 工作类型
    results_wanted=20,
    hours_old=24,  # 24小时内的职位
    country_indeed='USA'
)
```

### ScraperAPI 配置

在 `src/util.py` 中配置 ScraperAPI：

```python
# ScraperAPI 配置
USE_SCRAPERAPI = True
SCRAPERAPI_KEY = "your_api_key_here"
```

## 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| site_name | str/list | 要搜索的网站列表 |
| search_term | str | 搜索关键词 |
| google_search_term | str | 自定义 Google 搜索词 |
| location | str | 地理位置 |
| distance | int | 搜索半径（英里） |
| is_remote | bool | 是否仅远程工作 |
| job_type | str | 工作类型 |
| results_wanted | int | 需要的结果数量 |
| hours_old | int | 职位发布时间范围（小时） |
| country_indeed | str | Indeed 网站国家 |

## 工作类型支持

- FULL_TIME（全职）
- PART_TIME（兼职）
- CONTRACT（合同工）
- TEMPORARY（临时工）
- INTERNSHIP（实习）
- PER_DIEM（按日计薪）
- NIGHTS（夜班）
- OTHER（其他）
- SUMMER（暑期工）
- VOLUNTEER（志愿者）

## 国家支持

支持多个国家的职位搜索，包括：
- USA
- UK
- Canada
- Australia
- Germany
- France
- India
- Japan
- 等更多国家

## 注意事项

1. 使用 ScraperAPI：
   - 需要有效的 API 密钥
   - 注意请求限制
   - 建议使用代理池

2. 数据使用：
   - 遵守网站的使用条款
   - 注意数据隐私
   - 合理控制请求频率

3. 性能优化：
   - 使用适当的并发数
   - 控制请求间隔
   - 合理设置超时时间

## 贡献

欢迎提交 Pull Request 或创建 Issue 来改进项目。

## 许可证

MIT License

## 免责声明

本项目仅供学习和研究使用，请遵守相关网站的使用条款和规定。使用本项目产生的任何后果由使用者自行承担。
