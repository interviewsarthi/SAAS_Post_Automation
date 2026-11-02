"""Existing footage rotates across independent posting runs without paid generation."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from agent.creative import select_visual
from agent.history import History


class VisualRotationTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        for name in ('a', 'b', 'c'):
            (self.root / (name + '.mp4')).touch()
        self.catalog = {'themes': ['blue', 'jade'], 'clips': [
            {'id': name, 'path': name + '.mp4'} for name in ('a', 'b', 'c')]}
        for target, value in [('agent.creative.ROOT', self.root),
                              ('agent.creative.load_json', None)]:
            mock = patch(target, value) if value else patch(target, return_value=self.catalog)
            mock.start()
            self.addCleanup(mock.stop)
        self.history_path = self.root / 'history.json'

    def test_each_cycle_uses_every_clip_and_survives_runner_restarts(self):
        seen = []
        for i in range(30):
            history = History(self.history_path)
            visual = select_visual(history)
            self.assertNotIn(visual['clip_id'], seen[-1:])
            seen.append(visual['clip_id'])
            history.add({'id': str(i), 'format': 'reel', 'visual_clip': visual['clip_id']})
            history.save()
        for start in range(0, len(seen), 3):
            self.assertEqual(set(seen[start:start + 3]), {'a', 'b', 'c'})

    def test_random_choice_can_select_any_unused_clip(self):
        history = History(self.history_path)
        history.add({'id': 'last', 'visual_clip': 'a'})
        with patch('agent.creative.random.choice', side_effect=lambda clips: clips[-1]) as choose:
            self.assertEqual(select_visual(history)['clip_id'], 'c')
        self.assertEqual({c['id'] for c in choose.call_args.args[0]}, {'b', 'c'})

    def test_images_and_fresh_veo_do_not_consume_library_cycle(self):
        history = History(self.history_path)
        history.posts = [{'visual_clip': 'a', 'format': 'sales'},
                         {'visual_clip': 'b', 'format': 'image'},
                         {'visual_clip': 'c', 'format': 'carousel'},
                         {'visual_clip': 'veo-fresh', 'format': 'reel'}]
        with patch('agent.creative.random.choice', side_effect=lambda clips: clips[0]) as choose:
            select_visual(history)
        self.assertEqual({c['id'] for c in choose.call_args.args[0]}, {'b', 'c'})

    def test_missing_files_and_single_clip_library(self):
        (self.root / 'b.mp4').unlink()
        (self.root / 'c.mp4').unlink()
        history = History(self.history_path)
        history.posts = [{'visual_clip': 'a'}]
        self.assertEqual(select_visual(history)['clip_id'], 'a')
        (self.root / 'a.mp4').unlink()
        with self.assertRaisesRegex(RuntimeError, 'No verified motion footage'):
            select_visual(history)


if __name__ == '__main__':
    unittest.main()
