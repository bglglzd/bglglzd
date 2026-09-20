"""Regression tests for the public-data boundary and generated SVGs."""
import copy
import json
import unittest
from unittest.mock import patch
from xml.etree import ElementTree
import render_profile as profile

class PublicDataTests(unittest.TestCase):
    def test_private_fork_archived_and_foreign_projects_are_never_fetched(self):
        public={'name':'demo','private':False,'fork':False,'archived':False,'owner':{'login':'bglglzd'},'html_url':'https://github.com/bglglzd/demo'}
        repos=[public]
        for key in ['private','fork','archived']:
            item=copy.deepcopy(public); item.update({key:True,'name':key}); repos.append(item)
        for name,owner in [('bglglzd','bglglzd'),('foreign','someone-else')]:
            item=copy.deepcopy(public); item.update(name=name,owner={'login':owner}); repos.append(item)
        calls=[]
        def api(path):
            calls.append(path)
            if path.startswith('users/'): return repos
            if path.endswith('/languages'): return {'Rust':123}
            return [{'draft':False},{'draft':True}]
        with patch.object(profile,'api',side_effect=api):
            data=profile.collect()
        self.assertEqual([p['name'] for p in data['projects']],['demo'])
        self.assertEqual(data['projects'][0]['releases'],1)
        self.assertEqual(calls,['users/bglglzd/repos?type=owner&per_page=100','repos/bglglzd/demo/languages','repos/bglglzd/demo/releases?per_page=100'])

    def test_snapshot_totals_and_svg_safety(self):
        data=json.loads((profile.ROOT/'assets/public-metrics.json').read_text())
        profile.validate(data)
        ns={'s':'http://www.w3.org/2000/svg'}
        for theme in profile.THEMES:
            for compact in [False,True]:
                for graphic in [profile.hero(theme,compact),profile.engineering(data,theme,compact)]:
                    root=ElementTree.fromstring(graphic)
                    self.assertTrue(root.find('s:title',ns).text)
                    self.assertFalse(root.findall('.//s:script',ns))
                    self.assertNotIn('href=',graphic)
                    self.assertNotIn('foreignObject',graphic)
        data['languages']['Rust']+=1
        with self.assertRaises(ValueError): profile.validate(data)

if __name__=='__main__': unittest.main()
