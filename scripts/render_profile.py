"""Self-hosted profile graphics from public GitHub data. Standard library only."""
from collections import Counter
from datetime import datetime, timezone
from html import escape
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LOGIN = 'bglglzd'
COLORS = {'Rust':'#e7a77d','TypeScript':'#6da7fa','Kotlin':'#b89aff','Java':'#e9c46a','C++':'#73d8dc','Python':'#f1cf71','JavaScript':'#e6d962','Shell':'#89d99d','Other':'#78939e'}
THEMES = {
    'dark': {'bg':'#0d141b','fg':'#eef4f3','muted':'#9aadb4','line':'#283942','accent':'#b4f17e','blue':'#73d8dc'},
    'light': {'bg':'#f3f6ef','fg':'#162d27','muted':'#52665d','line':'#c6d4c4','accent':'#396e20','blue':'#137c83'},
}

def api(path):
    result = subprocess.run(['gh','api',path,'--paginate','--slurp'], check=True, capture_output=True, text=True, encoding='utf-8')
    pages = json.loads(result.stdout)
    return [item for page in pages for item in page] if pages and isinstance(pages[0],list) else pages[0]

def collect():
    # Explicit public endpoint; filters also protect local runs with broad tokens.
    repos = api(f'users/{LOGIN}/repos?type=owner&per_page=100')
    projects, languages = [], Counter()
    for repo in sorted(repos, key=lambda r:r['name'].lower()):
        if repo['private'] or repo['fork'] or repo['archived'] or repo['name']==LOGIN or repo['owner']['login']!=LOGIN:
            continue
        prefix = f"repos/{LOGIN}/{repo['name']}"
        langs = api(f'{prefix}/languages')
        releases = [r for r in api(f'{prefix}/releases?per_page=100') if not r['draft']]
        languages.update(langs)
        projects.append({'name':repo['name'],'url':repo['html_url'],'languages':langs,'releases':len(releases)})
    if not projects or not languages:
        raise ValueError('Incomplete public snapshot; keeping the last good graphics')
    return {'schema':1,'updated':datetime.now(timezone.utc).strftime('%Y-%m-%d'),'scope':'Public owned non-fork non-archived repositories; profile excluded','projects':projects,'languages':dict(languages.most_common())}

def text(x,y,value,size=16,fill='fg',weight=400,extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{{{fill}}}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'

def svg(body,theme,height,title,description,width=960):
    for key,value in THEMES[theme].items():
        body = body.replace('{'+key+'}',value)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc><g font-family="Segoe UI, Helvetica, Arial, sans-serif">{body}</g></svg>\n'

def hero(theme,compact=False):
    if compact:
        parts = ['<rect width="480" height="264" rx="16" fill="{bg}"/>',text(24,38,'bglglzd',16,'accent',600,'letter-spacing="2"'),text(24,98,'Local intelligence.',36,weight=650),text(24,142,'Useful software.',36,weight=650),text(24,181,'Voice tools / private workflows / dev experience',13,'muted'),'<path d="M24 204H456" stroke="{line}"/>',text(24,237,'RUST / TYPESCRIPT / KOTLIN / PYTHON',13,'muted',600)]
        return svg(''.join(parts),theme,264,'bglglzd — Local intelligence. Useful software.','Voice tools, private workflows and developer experience.',480)
    parts = ['<rect width="960" height="292" rx="18" fill="{bg}"/>']
    parts += [text(40,43,'bglglzd',16,'accent',600,'letter-spacing="2"'),
              text(40,110,'Local intelligence.',47,weight=650,extra='letter-spacing="-1.5"'),
              text(40,165,'Useful software.',47,weight=650,extra='letter-spacing="-1.5"'),
              text(42,202,'Voice tools / private workflows / developer experience',16,'muted'),
              '<path d="M40 226H566" stroke="{line}"/>',
              text(42,258,'RUST   /   TYPESCRIPT   /   KOTLIN   /   PYTHON',12,'muted',600,'letter-spacing="1.2"')]
    return svg(''.join(parts),theme,292,'bglglzd — Local intelligence. Useful software.','Voice tools, private workflows and developer experience. Rust, TypeScript, Kotlin and Python.')

def engineering(data,theme,compact=False):
    projects = data['projects']
    ranked = sorted(data['languages'].items(),key=lambda kv:(-kv[1],kv[0]))
    top = ranked[:5]
    if len(ranked)>5:
        top.append(('Other',sum(value for _,value in ranked[5:])))
    total = sum(data['languages'].values())
    stats = [(len(projects),'PUBLIC PROJECTS'),(sum(p['releases'] for p in projects),'PUBLISHED RELEASES'),(sum(p['releases']>0 for p in projects),'PROJECTS WITH RELEASES')]
    parts = ['<rect width="960" height="250" rx="18" fill="{bg}"/>',text(32,33,'PUBLIC ENGINEERING / SNAPSHOT',11,'muted',600,'letter-spacing="1.7"')]
    for i,(number,label) in enumerate(stats):
        x = 32+i*310
        parts += [text(x,89,number,42,weight=600),text(x,115,label,10,'muted',600,'letter-spacing="1.2"')]
        if i<2:
            parts.append(f'<path d="M{x+280} 55V120" stroke="{{line}}"/>')
    parts += ['<path d="M32 135H928" stroke="{line}"/>',text(32,159,'LANGUAGE MIX',10,'muted',600,'letter-spacing="1.5"'),text(928,159,'by GitHub language bytes',10,'muted',extra='text-anchor="end"')]
    x,desc = 32,[]
    for i,(language,value) in enumerate(top):
        width,color = value/total*896,COLORS.get(language,'#78939e')
        parts.append(f'<rect x="{x:.2f}" y="172" width="{width:.2f}" height="9" fill="{color}"/>')
        x += width
        percent,label_x = value/total*100,32+i*149
        parts += [f'<circle cx="{label_x+4}" cy="202" r="4" fill="{color}"/>',text(label_x+15,206,f'{language} {percent:.1f}%',12)]
        desc.append(f'{language}: {percent:.1f}%')
    parts += [text(32,232,'Owned public source repos · includes prereleases · excludes forks',10,'muted'),text(928,232,data['updated'],10,'muted',extra='text-anchor="end"')]
    description = '; '.join(f'{n} {label.lower()}' for n,label in stats)+'. Language mix by bytes: '+', '.join(desc)+'. Updated '+data['updated']+'.'
    if compact:
        parts = ['<rect width="480" height="342" rx="16" fill="{bg}"/>',text(24,32,'PUBLIC ENGINEERING',12,'muted',600,'letter-spacing="1.5"')]
        for i,((number,_),label) in enumerate(zip(stats,['Projects','Releases','With releases'])):
            parts += [text(24+i*152,83,number,36,weight=600),text(24+i*152,108,label,13,'muted')]
        parts += ['<path d="M24 130H456" stroke="{line}"/>',text(24,155,'LANGUAGE MIX / BY BYTES',12,'muted',600)]
        x=24
        for i,(language,value) in enumerate(top):
            width,color=value/total*432,COLORS.get(language,'#78939e')
            parts.append(f'<rect x="{x:.2f}" y="169" width="{width:.2f}" height="9" fill="{color}"/>')
            x+=width
            lx,ly=24+(i%2)*218,205+(i//2)*27
            parts += [f'<circle cx="{lx+4}" cy="{ly-4}" r="4" fill="{color}"/>',text(lx+16,ly,f'{language} {value/total*100:.1f}%',14)]
        parts += [text(24,298,'Public source repos · includes prereleases',12,'muted'),text(24,321,'Updated '+data['updated'],12,'muted')]
        return svg(''.join(parts),theme,342,'Public engineering snapshot',description,480)
    return svg(''.join(parts),theme,250,'Public engineering snapshot',description)

def validate(data):
    if data.get('schema')!=1 or not data['projects']:
        raise ValueError('Invalid snapshot')
    expected = Counter()
    for p in data['projects']:
        if p['url']!=f"https://github.com/{LOGIN}/{p['name']}" or p['name']==LOGIN or p['releases']<0:
            raise ValueError('Unexpected project scope')
        expected.update(p['languages'])
    if dict(expected)!=data['languages'] or any(v<=0 for v in expected.values()):
        raise ValueError('Language totals do not reconcile')

def render(data):
    validate(data)
    files = {'assets/public-metrics.json':json.dumps(data,indent=2)+'\n'}
    for theme in THEMES:
        files[f'assets/hero-text-{theme}.svg'] = hero(theme)
        files[f'assets/engineering-{theme}.svg'] = engineering(data,theme)
        files[f'assets/hero-{theme}-compact.svg'] = hero(theme,compact=True)
        files[f'assets/engineering-{theme}-compact.svg'] = engineering(data,theme,compact=True)
    # Fetch and render everything before replacing any working snapshot.
    for relative,content in files.items():
        path = ROOT/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content,encoding='utf-8')

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline',action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT/'assets/public-metrics.json').read_text(encoding='utf-8')) if args.offline else collect()
    render(data)
    print(f"Rendered light and dark graphics from {len(data['projects'])} public projects.")
