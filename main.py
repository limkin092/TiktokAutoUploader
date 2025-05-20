from tiktok_uploader import tiktok
from tiktok_uploader.Config import Config

if __name__ == "__main__":
    _ = Config.load("./config.txt")

    cookie_name = "morbo"

    # tiktok.login(cookie_name)
    tiktok.upload_video(
        session_user="morbo",
        video="/Users/salimtekin/Documents/0_projects/code/galactic_news/src/final/vertical_reel.mp4",
        title="Join Morbo the Destroyer in a laughing fit over new sanctions on Russia! Oh, your puny species is DOOMED! #MorboReacts #EarthNews #GalacticNews#Sanctions #Russia #Futurama #Morbo #Doomed #PoliticalNews #EarthlingsFolly #Authoritarian #MorboNews #WorldAffairs #News #WorldNews #Satire #Futurama #AlienPerspective",
        schedule_time=0,
        allow_comment=1,
        allow_duet=0,
        allow_stitch=0,
        visibility_type=0,
        brand_organic_type=0,
        branded_content_type=0,
        ai_label=0,
        proxy=None,
    )
