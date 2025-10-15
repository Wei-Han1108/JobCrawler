# JobCrawler

A powerful multi-source job scraping system that aggregates job listings from multiple major job boards and Google Search.

## CSV Output
![image](https://github.com/user-attachments/assets/ccba4114-21aa-4a8a-bde6-9d795f31bb72)

## Features

- **Multiple data sources:**
  - LinkedIn
  - Indeed
  - Glassdoor
  - ZipRecruiter
  - Google Jobs

- **Robust search options:**
  - Keyword search
  - Location filtering
  - Job type filtering
  - Time range filtering
  - Remote-only filtering
  - Custom search queries

- **Data consolidation:**
  - Automatic de-duplication
  - Unified data schema
  - Merge results from multiple sources
  - Export to CSV

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/JobCrawler.git
cd JobCrawler
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic usage
```bash
# Run the test.py script
cd JobCrawler
python test.py
```

The results will be saved to `JobCrawler/jobs.csv`.

## Parameters

| Parameter             | Type      | Description                                   |
|-----------------------|-----------|-----------------------------------------------|
| `site_name`           | str/list  | List of sites to search                       |
| `search_term`         | str       | Keyword(s) to search                          |
| `google_search_term`  | str       | Custom Google search query                    |
| `location`            | str       | Location filter                               |
| `distance`            | int       | Search radius (miles)                         |
| `is_remote`           | bool      | Remote-only filter                            |
| `job_type`            | str       | Job type                                      |
| `results_wanted`      | int       | Number of results desired                     |
| `hours_old`           | int       | Posted time window (hours)                    |
| `country_indeed`      | str       | Country code for the Indeed site              |

## Supported Job Types

- FULL_TIME
- PART_TIME
- CONTRACT
- TEMPORARY
- INTERNSHIP
- PER_DIEM
- NIGHTS
- OTHER
- SUMMER
- VOLUNTEER

## Supported Countries

Supports job searches in multiple countries, including (but not limited to):
- USA
- UK
- Canada
- Australia
- Germany
- France
- India
- Japan
- And more

## Notes

1. **Using ScraperAPI:**
   - Requires a valid API key
   - Respect request quotas/limits
   - A rotating proxy pool is recommended

2. **Data usage:**
   - Comply with each website’s Terms of Service
   - Respect data privacy
   - Throttle request rates appropriately

3. **Performance tuning:**
   - Choose a sensible level of concurrency
   - Control inter-request delays
   - Set reasonable timeouts

## Contributing

Contributions are welcome! Please open an Issue or submit a Pull Request.

## License

MIT License

## Disclaimer

This project is intended for learning and research purposes only. Please comply with the terms and policies of the websites you access. You assume full responsibility for any outcomes resulting from the use of this project.
