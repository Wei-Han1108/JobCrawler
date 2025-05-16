
from jobspy import scrape_jobs
import csv
from src.proxy_detector import get_working_proxies_concurrent

# 1. 获取 HTTP 代理列表
# proxies = get_working_proxies_concurrent(limit=10)

# 3. 使用 src 抓取数据
# jobs = scrape_jobs(
#     site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor", "google"],
#     search_term="software engineer",
#     results_wanted=10,
#     hours_old=24,
#     country_indeed='USA',
# )


jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "glassdoor", "google"],
    search_term="software engineer",
    google_search_term="software engineer jobs near San Francisco, CA since yesterday",
    location="San Francisco, CA",
    results_wanted=20,
    hours_old=72,
    country_indeed='USA',
    # proxies=proxies,
)

print(f"Found {len(jobs)} jobs")
print(jobs.head())

# save to csv
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
