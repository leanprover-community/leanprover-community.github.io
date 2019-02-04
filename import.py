# requires python 3
# The workflow:
# - populate_all() builds a json file in `json_root` for each topic, containing message data,
#   and an index json file mapping streams to their topics.
#   This uses the Zulip API and takes ~10 minutes to crawl the whole chat.
# - write_markdown() builds markdown files in `md_index` from the json. This takes ~15 seconds.
# - This markdown can be pushed directly to GitHub or built locally with `jekyll serve --incremental`.
#   Building locally takes about 1 minute.
#
# TODO(Rob): The json archive needs to be updated incrementally (only download and add unseen posts)

from datetime import date, datetime
from pathlib import Path
from zlib import adler32
from operator import attrgetter
import zulip, string, os, time, json, urllib

json_root = Path("./_json")
md_root = Path("archive")
md_index = Path("index.md")
html_root = Path("archive")
last_updated_path = Path("_includes/archive_update.html")
site_url = "https://leanprover-community.github.io/"
stream_blacklist = ['rss', 'travis', 'announce']

# config_file should point to a Zulip api config
client = zulip.Client(config_file="./.zuliprc")

def sanitize(s):
    return "".join(filter(str.isalnum, s.encode('ascii', 'ignore').decode('utf-8')))

def sanitize_topic(topic_name):
    i = str(adler32(topic_name.encode('utf-8')) % (10 ** 5)).zfill(5)
    return i + sanitize(topic_name)

def sanitize_stream(stream_name, stream_id):
    return str(stream_id) + sanitize(stream_name)

# retrieve information from Zulip

def safe_request(cmd, args):
    rsp = cmd(*args)
    while rsp['result'] == 'error':
        print("timeout hit: {}".format(rsp['retry-after']))
        time.sleep(float(rsp['retry-after']) + 1)
        rsp = cmd(*args)
    return rsp

def open_outfile(dir, filename, mode):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return open(dir / filename, mode, encoding='utf-8')

def request_all(request, anchor=0):
    request['anchor'] = anchor
    request['num_before'] = 0
    request['num_after'] = 1000
    response = safe_request(client.get_messages, [request])
    msgs = response['messages']
    while not response['found_newest']:
        request['anchor'] = response['messages'][-1]['id'] + 1
        response = safe_request(client.get_messages, [request])
        msgs = msgs + response['messages']
    #response['messages'] = msgs 
    return msgs #response

def separate_results(list):
    map = {}
    for m in list:
        if m['subject'] not in map:
            map[m['subject']] = [m]
        else:
            map[m['subject']].append(m)
    return map

# stream_index: {'time':update_time, 'streams':{name:{'id':stream_id, 'latest_id':id, 'topic_data':{topic_name:{topic_size:2, latest_date:date}}}}}
def populate_incremental():
    streams = safe_request(client.get_streams, [])['streams']
    f = open(json_root / Path('stream_index.json'), 'r', encoding='utf-8')
    stream_index = json.load(f, encoding='utf-8')
    f.close()
    for s in (s for s in streams if s['name'] not in stream_blacklist):
        print(s['name'])
        if s['name'] not in stream_index['streams']:
            stream_index['streams'][s['name']] = {'id':s['stream_id'], 'latest_id':0, 'topic_data':{}}
        request = {'narrow':[{'operator':'stream', 'operand':s['name']}], 'client_gravatar': True,
                   'apply_markdown': True}
        new_msgs = request_all(request, stream_index['streams'][s['name']]['latest_id']+1)
        if len(new_msgs) > 0:
            stream_index['streams'][s['name']]['latest_id'] = new_msgs[-1]['id']
        nm = separate_results(new_msgs)
        for t in nm:
            p = json_root / Path(sanitize_stream(s['name'], s['stream_id'])) / Path(sanitize_topic(t) + '.json')
            topic_exists = p.exists()
            old = []
            if topic_exists:
                f = open(p, 'r', encoding='utf-8')
                old = json.load(f)
                f.close()
            m = nm[t]
            new_topic_data = {'size': len(m)+len(old), 
                                'latest_date': m[-1]['timestamp']}
            stream_index['streams'][s['name']]['topic_data'][t] = new_topic_data
            out = open_outfile(json_root / Path(sanitize_stream(s['name'], s['stream_id'])), 
                               Path(sanitize_topic(t) + '.json'), 'w')
            json.dump(old+m, out, ensure_ascii=False)
            out.close() 
    stream_index['time'] = datetime.utcfromtimestamp(time.time()).strftime('%b %d %Y at %H:%M %z')
    out = open_outfile(json_root, Path('stream_index.json'), 'w')
    json.dump(stream_index, out, ensure_ascii = False)
    out.close()

def populate_all():
    streams = safe_request(client.get_streams, [])['streams']
    ind = {}
    for s in (s for s in streams if s['name'] not in stream_blacklist):
        print(s['name'])
        topics = safe_request(client.get_stream_topics, [s['stream_id']])['topics']
        nind = {'id': s['stream_id'], 'latest_id':0}
        tpmap = {}
        for t in topics:
            request = {
                'narrow': [{'operator': 'stream', 'operand': s['name']},
                           {'operator': 'topic', 'operand': t['name']}],
                'client_gravatar': True,
                'apply_markdown': True
            }
            m = request_all(request)
            tpmap[t['name']] = {'size': len(m), 
                                'latest_date': m[-1]['timestamp']}
            nind['latest_id'] = max(nind['latest_id'], m[-1]['id'])
            out = open_outfile(json_root / Path(sanitize_stream(s['name'], s['stream_id'])), 
                               Path(sanitize_topic(t['name']) + '.json'), 'w')
            json.dump(m, out, ensure_ascii=False)
            out.close()
        nind['topic_data'] = tpmap 
        ind[s['name']] = nind
    js = {'streams':ind, 'time':datetime.utcfromtimestamp(time.time()).strftime('%b %d %Y at %H:%M %z')}
    out = open_outfile(json_root, Path('stream_index.json'), 'w')
    json.dump(js, out, ensure_ascii = False)
    out.close()

## Display

def structure_link(stream_id, stream_name, topic_name, post_id):
    sanitized = urllib.parse.quote(
        '{0}-{1}/topic/{2}/near/{3}'.format(stream_id, stream_name, topic_name, post_id))
    return 'https://leanprover.zulipchat.com/#narrow/stream/' + sanitized

def format_stream_url(stream_id, stream_name):
    return site_url + str(html_root) + '/' + sanitize_stream(stream_name, stream_id)

def format_message(name, date, msg, link):
    return u'#### [{4} {0} ({1})]({3}):\n{2}'.format(name, date, msg, link, '') 

def write_topic(messages, stream_name, stream_id, topic_name, outfile):
    for c in messages:
        name = c['sender_full_name']
        date = datetime.fromtimestamp(c['timestamp']).strftime('%b %d %Y at %H:%M')
        msg = c['content']
        link = structure_link(stream_id, stream_name, topic_name, c['id'])
        outfile.write(format_message(name, date, msg, link))
        outfile.write('\n\n')

def write_topic_index(s_name, s):
    directory = md_root / Path(sanitize_stream(s_name, s['id']))
    outfile = open_outfile(directory, md_index, 'w+')
    header = ("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive\npermalink: {2}/{1}/index.html\n---\n\n" + 
            "## Stream: [{0}]({3}/index.html)\n\n---\n\n### Topics:\n\n").format(
                s_name, 
                sanitize_stream(s_name, s['id']), 
                html_root, 
                format_stream_url(s['id'], s_name))
    outfile.write(header)
    for topic_name in s['topic_data']:
        t = s['topic_data'][topic_name]
        outfile.write("* [{0}]({1}.html) ({2} message{4}, latest: {3})\n\n".format(
            topic_name, 
            sanitize_topic(topic_name), 
            t['size'],
            datetime.fromtimestamp(t['latest_date']).strftime('%b %d %Y at %H:%M'),
            '' if t['size'] == 1 else 's'
        ))
    outfile.write('\n{% include archive_update.html %}')
    outfile.close()

def write_stream_index(streams):
    outfile = open(md_root / md_index, 'w+', encoding='utf-8')
    outfile.write("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive\npermalink: {}/index.html\n---\n\n---\n\n## Streams:\n\n".format(html_root))
    for s in sorted(streams, key=lambda s: len(streams[s]['topic_data']), reverse=True):
        num_topics = len(streams[s]['topic_data'])
        outfile.write("* [{0}]({1}/index.html) ({2} topic{3})\n\n".format(
            s, 
            sanitize_stream(s, streams[s]['id']), 
            num_topics,
            '' if num_topics == 1 else 's'))
    outfile.write('\n{% include archive_update.html %}')
    outfile.close()

def format_topic_header(stream_name, stream_id, topic_name):
    return ("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive \npermalink: {4}/{2}/{3}.html\n---\n\n" + 
            '## Stream: [{0}]({5}/index.html)\n### Topic: [{1}]({5}/{3}.html)\n\n---\n\n<base href="https://leanprover.zulipchat.com">').format(
                stream_name,
                topic_name, 
                sanitize_stream(stream_name, stream_id), 
                sanitize_topic(topic_name), 
                html_root,
                format_stream_url(stream_id, stream_name))

def get_topic_and_write(stream_name, stream, topic):
    json_path = json_root / Path(sanitize_stream(stream_name, stream['id'])) / Path (sanitize_topic(topic) + '.json')
    f = open(json_path, 'r', encoding='utf-8')
    messages = json.load(f)
    f.close()
    o = open_outfile(md_root / Path(sanitize_stream(stream_name, stream['id'])), Path(sanitize_topic(topic) + '.md'), 'w+')
    o.write(format_topic_header(stream_name, stream['id'], topic))
    o.write('\n{% raw %}\n')
    write_topic(messages, stream_name, stream['id'], topic, o)
    o.write('\n{% endraw %}\n')
    o.close()

def write_last_updated(t):
    f = open(last_updated_path, 'w+')
    f.write('<p>Last updated: {} UTC</p>'.format(t))
    f.close()

def write_markdown():
    f = open(json_root / Path('stream_index.json'), 'r', encoding='utf-8')
    stream_info = json.load(f, encoding='utf-8')
    f.close()
    streams = stream_info['streams']
    write_last_updated(str(stream_info['time'])) #(datetime.utcfromtimestamp(time.time()))
    write_stream_index(streams)
    for s in streams:
        print('building: ', s)
        write_topic_index(s, streams[s]) 
        for t in streams[s]['topic_data']:
            get_topic_and_write(s, streams[s], t)

#populate_all()
populate_incremental()
write_markdown()