import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_raw_proxies(url="https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"):
    try:
        resp = requests.get(url, timeout=10)
        return ["http://" + line.strip() for line in resp.text.splitlines() if line.strip()]
    except Exception as e:
        print("❌ 下载代理失败:", e)
        return []

def is_proxy_working(proxy):
    test_url = "https://httpbin.org/ip"
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"✅ 有效代理: {proxy}")
            return proxy
    except:
        pass
    print(f"❌ 无效代理: {proxy}")
    return None

def get_working_proxies_concurrent(limit=10, max_workers=50):
    print("🚀 正在下载并测试代理...")
    raw_proxies = get_raw_proxies()
    working = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(is_proxy_working, proxy): proxy for proxy in raw_proxies}
        for future in as_completed(futures):
            result = future.result()
            if result:
                working.append(result)
                if len(working) >= limit:
                    break
    return working

# 示例用法
if __name__ == "__main__":
    good_proxies = get_working_proxies_concurrent(limit=10)
    print("\n✅ 最终可用代理列表：")
    print(good_proxies)
