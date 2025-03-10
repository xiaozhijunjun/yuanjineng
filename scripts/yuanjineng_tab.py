import gradio as gr
from modules import script_callbacks
from modules.shared import opts
from modules import extensions

# Handy constants
YUANJINENG_MAIN_URL = "https://yuanjineng.cn/webui"
YUANJINENG_IFRAME_ID = "webui-yuanjineng-iframe"
YUANJINENG_IFRAME_HEIGHT = "100%"
YUANJINENG_IFRAME_WIDTH = "100%"


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as yuanjineng_tab:
        # Check if Controlnet is installed and enabled in settings, so we can show or hide the "Send to Controlnet" buttons.
        controlnet_exists = False
        for extension in extensions.active():
            if "controlnet" in extension.name:
                controlnet_exists = True
                break

        with gr.Row():
            # Add an iframe with YUANJINENG directly in the tab.
            gr.HTML(
                f"""<iframe id="{YUANJINENG_IFRAME_ID}" 
                src = "{YUANJINENG_MAIN_URL}" 
                width = "{YUANJINENG_IFRAME_WIDTH}" 
                height = "{YUANJINENG_IFRAME_HEIGHT}" style="border-radius:10px;width:97%;height:99%;display:block;background:#FFFFFF;border-bottom:1px dashed #666666;position:fixed;z-index:9999999"
                >"""
            )
    return [(yuanjineng_tab, "元技能-Yuanjineng", "YUANJINENG_embed")]


# Actually hooks up the tab to the WebUI tabs.
script_callbacks.on_ui_tabs(on_ui_tabs)
