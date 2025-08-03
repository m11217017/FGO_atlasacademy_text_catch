#!/usr/bin/env python3
"""
使用範例 - 如何使用 HTML Downloader
"""

from program.html_downloader import HTMLDownloader


def example_usage():
    """使用範例"""
    
    # 要下載的網址列表
    urls = [
        "https://apps.atlasacademy.io/",
        "https://apps.atlasacademy.io/db/",
        "https://api.atlasacademy.io/docs/",
        "https://apps.atlasacademy.io/db/JP/servant",
        "https://apps.atlasacademy.io/db/NA/servant",
        # 您可以在這裡添加更多網址
    ]
    
    # 創建 HTML 下載器
    # save_dir: 儲存目錄
    # delay: 請求間隔（秒）
    downloader = HTMLDownloader(
        save_dir="./site_raw_html",
        delay=1.5  # 間隔 1.5 秒避免請求過於頻繁
    )
    
    # 開始批量下載
    print("=== HTML 下載器 ===")
    results = downloader.download_urls(urls)
    
    # 顯示結果
    print(f"\n總共: {results['total']} 個網址")
    print(f"成功: {results['success']} 個")
    print(f"失敗: {results['failed']} 個")
    
    if results['failed_urls']:
        print(f"\n失敗的網址:")
        for url in results['failed_urls']:
            print(f"  - {url}")


if __name__ == "__main__":
    example_usage()
