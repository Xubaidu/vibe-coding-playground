"""Capture 52ETF heatmap screenshot."""

from playwright.sync_api import sync_playwright
from config import COLLECTORS

_config = COLLECTORS.get("etf_heatmap", {})
URL = _config.get("url", "https://52etf.site/")
OUTPUT_PATH = _config.get("output_path", "/tmp/52etf-share.png")


def capture_heatmap(output_path: str = None) -> str:
    """
    Capture heatmap from 52etf.site via share button download.
    
    Returns:
        Path to the saved image
    """
    output = output_path or OUTPUT_PATH
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2,
            ignore_https_errors=True
        )
        page = context.new_page()
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(5000)  # wait for heatmap to render

        # Click "截图分享" button
        page.get_by_text("截图分享").click()

        # Wait for dialog
        page.wait_for_timeout(3000)

        # Download via "下载保存" button
        with page.expect_download() as download_info:
            page.get_by_text("下载保存").click()
        download = download_info.value

        # Save
        download.save_as(output)
        browser.close()
        
    print(f"Heatmap saved to {output}")
    return output


if __name__ == "__main__":
    capture_heatmap()
