import reflex as rx
import my_youtube.api.yt_charts as yt_charts

class PageState(rx.State):
    
    texto = ""

    async def traer_videos(self):
        return await yt_charts.execute_chart()
    
