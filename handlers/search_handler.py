from telegram import Update
from telegram.ext import ContextTypes
from utils.search_utils import fetch_free_nodes

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # 如果用户提供了自定义的URL，则使用该URL
        if context.args:
            custom_url = context.args[0]
        else:
            # 默认的免费节点API URL
            custom_url = "https://example.com/free-nodes-api"

        nodes = fetch_free_nodes(custom_url)
        if not nodes:
            await update.message.reply_text("No free nodes available.")
            return

        # 格式化并发送结果
        nodes_text = "\n".join(nodes)
        await update.message.reply_text(f"Available Free Nodes:\n{nodes_text}")
    except Exception as e:
        await update.message.reply_text(f"Error fetching free nodes: {e}")