#!/usr/bin/env python3
"""Stock Project - Main Entry Point"""

import argparse


def cmd_heatmap(args):
    """Capture and send heatmap."""
    from tasks import run_daily_heatmap
    run_daily_heatmap()


def cmd_bot(args):
    """Start Lark bot listener."""
    from bot import start_event_subscription
    start_event_subscription()


def main():
    parser = argparse.ArgumentParser(
        description="Stock Project CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # heatmap: capture + send
    p_heatmap = subparsers.add_parser("heatmap", help="Capture and send heatmap to Lark")
    p_heatmap.set_defaults(func=cmd_heatmap)
    
    # bot: start listener
    p_bot = subparsers.add_parser("bot", help="Start Lark bot event listener")
    p_bot.set_defaults(func=cmd_bot)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()
