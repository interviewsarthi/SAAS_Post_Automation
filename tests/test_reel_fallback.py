"""When a reel cannot be written (the model is unavailable), a slot still posts something of the same product."""
import os
import unittest
from unittest import mock

from agent import pipeline
from agent.config import Settings
from agent.llm import QuotaError


def settings():
    return Settings(gemini_api_key=None, gemini_models=["m"], meta_page_id=None, meta_page_token=None, ig_user_id=None,
                    yt_client_id=None, yt_client_secret=None, yt_refresh_token=None, yt_privacy="public",
                    cloudinary_url=None, graph_version="v21.0", dry_run=True)


class ReelFallback(unittest.TestCase):
    def test_an_apply_reel_falls_back_to_apply_s_own_job_list(self):
        with mock.patch.object(pipeline, "_create_written", side_effect=QuotaError("429 quota")), \
                mock.patch("agent.joblist.create_joblist", return_value={"format": "reel", "id": "x"}) as jl:
            out = pipeline.create(settings(), fmt="reel", product_id="apply_sarthi")
        jl.assert_called_once()
        self.assertEqual(out["substituted_for"], "reel")
        self.assertIn("substituted for a reel: QuotaError", out["notes"])

    def test_a_prep_reel_still_never_becomes_another_product(self):
        with mock.patch.object(pipeline, "_create_written", side_effect=QuotaError("429 quota")), \
                mock.patch("agent.joblist.create_joblist") as jl, mock.patch("agent.campaign.create_sales") as sales:
            with self.assertRaisesRegex(RuntimeError, "prep_sarthi reel could not be written"):
                pipeline.create(settings(), fmt="reel", product_id="prep_sarthi")
        jl.assert_not_called()
        sales.assert_not_called()

    def test_flash_lite_is_the_third_model(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("SCRIPT_MODELS", None); os.environ.pop("GEMINI_MODELS", None)
            self.assertEqual(Settings.from_env().gemini_models, ["gemini-3.8-flash", "gemini-3.5-flash", "gemini-3.5-flash-lite"])
        wf = open(os.path.join(os.path.dirname(__file__), "..", ".github", "workflows", "post.yml")).read()
        self.assertIn("gemini-3.8-flash,gemini-3.5-flash,gemini-3.5-flash-lite", wf)


if __name__ == "__main__":
    unittest.main()
