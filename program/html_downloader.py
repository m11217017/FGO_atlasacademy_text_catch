#!/usr/bin/env python3
"""
HTML Downloader
下載指定網址的 HTML 內容並儲存到本地檔案
"""

import os
import requests
import urllib.parse
from pathlib import Path
import time
from typing import List, Optional
import hashlib


class HTMLDownloader:
    def __init__(self, save_dir: str = "./site_raw_html", delay: float = 1.0):
        """
        初始化 HTML 下載器
        
        Args:
            save_dir: 儲存目錄路徑
            delay: 請求間隔時間（秒）
        """
        self.save_dir = Path(save_dir)
        self.delay = delay
        self.session = requests.Session()
        
        # 設置 User-Agent 避免被網站封鎖
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # 創建儲存目錄
        self.save_dir.mkdir(parents=True, exist_ok=True)
        
    def generate_filename(self, url: str) -> str:
        """
        根據 URL 生成安全的檔案名稱
        
        Args:
            url: 網址
            
        Returns:
            安全的檔案名稱
        """
        # 解析 URL
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        path = parsed.path.strip('/')
        
        # 如果路徑為空，使用 index
        if not path:
            path = "index"
        
        # 替換不安全的字符
        safe_path = path.replace('/', '_').replace('\\', '_').replace(':', '_')
        safe_path = ''.join(c for c in safe_path if c.isalnum() or c in '._-')
        
        # 如果路徑太長，使用 hash
        if len(safe_path) > 50:
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            safe_path = f"{safe_path[:30]}_{url_hash}"
        
        # 組合域名和路徑
        filename = f"{domain}_{safe_path}.html"
        
        return filename
    
    def download_html(self, url: str) -> Optional[str]:
        """
        下載單個網頁的 HTML
        
        Args:
            url: 要下載的網址
            
        Returns:
            HTML 內容，失敗時返回 None
        """
        try:
            print(f"正在下載: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # 嘗試取得正確的編碼
            if response.encoding:
                html_content = response.text
            else:
                # 如果無法檢測編碼，嘗試 UTF-8
                html_content = response.content.decode('utf-8', errors='ignore')
            
            print(f"✅ 成功下載: {url} ({len(html_content)} 字元)")
            return html_content
            
        except requests.exceptions.RequestException as e:
            print(f"❌ 下載失敗: {url} - {str(e)}")
            return None
        except Exception as e:
            print(f"❌ 處理錯誤: {url} - {str(e)}")
            return None
    
    def save_html(self, url: str, html_content: str) -> bool:
        """
        儲存 HTML 內容到檔案
        
        Args:
            url: 原始網址
            html_content: HTML 內容
            
        Returns:
            是否成功儲存
        """
        try:
            filename = self.generate_filename(url)
            filepath = self.save_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"<!-- Downloaded from: {url} -->\n")
                f.write(f"<!-- Download time: {time.strftime('%Y-%m-%d %H:%M:%S')} -->\n\n")
                f.write(html_content)
            
            print(f"💾 已儲存: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ 儲存失敗: {url} - {str(e)}")
            return False
    
    def download_urls(self, urls: List[str]) -> dict:
        """
        批量下載多個網址的 HTML
        
        Args:
            urls: 網址列表
            
        Returns:
            下載結果統計
        """
        results = {
            'success': 0,
            'failed': 0,
            'total': len(urls),
            'failed_urls': []
        }
        
        print(f"開始下載 {len(urls)} 個網址...")
        print(f"儲存目錄: {self.save_dir.absolute()}")
        print("-" * 50)
        
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] ", end="")
            
            # 下載 HTML
            html_content = self.download_html(url)
            
            if html_content:
                # 儲存到檔案
                if self.save_html(url, html_content):
                    results['success'] += 1
                else:
                    results['failed'] += 1
                    results['failed_urls'].append(url)
            else:
                results['failed'] += 1
                results['failed_urls'].append(url)
            
            # 延遲避免請求過於頻繁
            if i < len(urls):
                time.sleep(self.delay)
        
        print("-" * 50)
        print(f"下載完成！成功: {results['success']}, 失敗: {results['failed']}")
        
        if results['failed_urls']:
            print("\n失敗的網址:")
            for url in results['failed_urls']:
                print(f"  - {url}")
        
        return results


def main():
    """主函數 - 示例用法"""
    
    # 示例網址列表
    urls = [
        "https://apps.atlasacademy.io/",
        "https://apps.atlasacademy.io/db/",
        "https://api.atlasacademy.io/docs/",
        # 您可以在這裡添加更多網址
    ]
    
    # 創建下載器
    downloader = HTMLDownloader(
        save_dir="./site_raw_html",
        delay=1.0  # 每次請求間隔 1 秒
    )
    
    # 開始下載
    results = downloader.download_urls(urls)
    
    return results


if __name__ == "__main__":
    main()
