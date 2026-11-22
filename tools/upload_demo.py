"""One-time upload of the product walkthrough video to the brand's channels.

    python tools/upload_demo.py check|youtube|facebook|instagram|linkedin MEDIA_DIR
"""
from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from agent.config import Settings                     # noqa: E402
from agent.publish import buffer, youtube             # noqa: E402
from agent.publish.meta import Meta                   # noqa: E402

RAW = "https://raw.githubusercontent.com/interviewsarthi/SAAS_Post_Automation/demo-video/"


def main(target: str, folder: str) -> None:
    s = Settings.from_env()
    media = pathlib.Path(folder)
    text = json.loads((media / "meta.json").read_text(encoding="utf-8"))
    meta = Meta(s.meta_page_id, s.meta_page_token, s.ig_user_id, s.graph_version)
    if target == "check":
        for name, read in (("youtube", lambda: youtube.channel_title(s)), ("meta", meta.whoami),
                           ("linkedin", lambda: bool(buffer.channel_id(s)))):
            try:
                print("CHECK", name, read())
            except Exception as exc:
                print("CHECK", name, "failed:", type(exc).__name__, str(exc)[:200])
    elif target == "youtube":
        from googleapiclient.http import MediaFileUpload
        api = youtube._service(s)
        y = text["youtube"]
        request = api.videos().insert(
            part="snippet,status",
            body={"snippet": {"title": y["title"], "description": y["description"], "tags": y["tags"],
                              "categoryId": "27", "defaultLanguage": "en", "defaultAudioLanguage": "en-IN"},
                  "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False, "embeddable": True,
                             "containsSyntheticMedia": True}},
            media_body=MediaFileUpload(str(media / "full.mp4"), mimetype="video/mp4", resumable=True))
        done = None
        while done is None:
            _, done = request.next_chunk(num_retries=5)
        print("RESULT youtube", "https://www.youtube.com/watch?v=" + done["id"], done.get("status"))
        try:
            api.thumbnails().set(videoId=done["id"],
                                 media_body=MediaFileUpload(str(media / "thumb.jpg"), mimetype="image/jpeg")).execute()
            print("RESULT thumbnail set")
        except Exception as exc:
            print("RESULT thumbnail not set:", type(exc).__name__, str(exc)[:200])
    elif target == "facebook":
        video = meta.fb_video(media / "full.mp4", text["facebook"]["text"])
        print("RESULT facebook", "https://www.facebook.com/watch/?v=" + str(video))
    elif target == "instagram":
        post = meta.ig_reel(RAW + "short.mp4", text["instagram"]["text"], cover_url=RAW + "cover.jpg")
        print("RESULT instagram", post, meta.ig_permalink(post))
    elif target == "linkedin":
        post = buffer.post(s, text["linkedin"]["text"], None, video_url=RAW + "full.mp4")
        print("RESULT linkedin", post)
        import time
        for _ in range(20):
            time.sleep(15)
            state = buffer.inspect_post(s, post)
            if state.get("externalLink") or str(state.get("status")).lower() in ("sent", "error", "failed"):
                break
        print("RESULT linkedin state", state.get("status"), state.get("externalLink"))
    else:
        raise SystemExit(f"unknown target {target}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
