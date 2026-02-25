"""Daily heatmap capture and send task."""

from collectors import capture_heatmap
from notifiers import send_image_with_text


def run():
    """Capture heatmap and send to Lark."""
    print("Running daily heatmap task...")
    
    # Step 1: Capture
    image_path = capture_heatmap()
    
    # Step 2: Send
    send_image_with_text(image_path, "52ETF 热力图更新")
    
    print("Task completed.")


if __name__ == "__main__":
    run()
