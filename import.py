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
import zulip, string, os, time, json, urllib
#import os
#import time
#import json
#import urllib

json_root = Path("./_json")
md_root = Path("archive")
md_index = Path("index.md")
html_root = Path("archive")
stream_blacklist = ['rss', 'travis']

# confic_file should point to a Zulip api config
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

def request_all(request):
    request['anchor'] = 0
    request['num_before'] = 0
    request['num_after'] = 1000
    response = safe_request(client.get_messages, [request])
    msgs = response['messages']
    while not response['found_newest']:
        request['anchor'] = response['messages'][-1]['id'] + 1
        response = safe_request(client.get_messages, [request])
        msgs = msgs + response['messages']
    response['messages'] = msgs 
    return response

def populate_all():
    streams = safe_request(client.get_streams, [])['streams']
    ind = []
    for s in (s for s in streams if s['name'] not in stream_blacklist):
        print(s['name'])
        topics = safe_request(client.get_stream_topics, [s['stream_id']])['topics']
        nind = {'name': s['name'], 'id': s['stream_id'], 'topics': topics}
        tpmap = {}
        for t in topics:
            out = open_outfile(json_root / Path(sanitize_stream(s['name'], s['stream_id'])), Path(sanitize_topic(t['name']) + '.json'), 'w')
            request = {
                'narrow': [{'operator': 'stream', 'operand': s['name']},
                           {'operator': 'topic', 'operand': t['name']}],
                'client_gravatar': True,
                'apply_markdown': False
            }
            m = request_all(request)
            tpmap[t['name']] = {'size': len(m['messages']), 'latest_date':m['messages'][-1]['timestamp']}
            json.dump(m, out, ensure_ascii=False)
            out.close()
        nind['topic_data'] = tpmap 
        ind.append(nind)
    out = open_outfile(json_root, Path('stream_index.json'), 'w')
    json.dump(ind, out, ensure_ascii = False)
    out.close()

## Display

def structure_link(stream_id, stream_name, topic_name, post_id):
    sanitized = urllib.parse.quote('{0}-{1}/topic/{2}/near/{3}'.format(stream_id, stream_name, topic_name, post_id))
    return 'https://leanprover.zulipchat.com/#narrow/stream/' + sanitized

def format_message(name, date, msg, link):
    return u'#### [{4} {0} ({1})]({3}):\n{2}'.format(name, date, msg, link, '![Click to go to Zulip](../../assets/img/zulip2.png)')

def write_topic(messages, stream_name, stream_id, topic_name, outfile):
    for c in messages:
        name = c['sender_full_name']
        date = datetime.fromtimestamp(c['timestamp']).strftime('%b %d %Y at %H:%M')
        msg = c['content']
        #if '{{' in msg:
        #    msg = "{% raw %}\n" + msg + "{% endraw %}"
        link = structure_link(stream_id, stream_name, topic_name, c['id'])
        outfile.write(format_message(name, date, msg, link))
        outfile.write('\n\n')

def write_topic_index(s): #(stream_name, topics):
    directory = md_root / Path(sanitize_stream(s['name'], s['id']))
    outfile = open_outfile(directory, md_index, 'w+')
    header = ("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive\npermalink: {2}/{1}/index.html\n---\n\n" + 
            "## Stream: [{0}](index.html)\n\n---\n\n### Topics:\n\n").format(s['name'], sanitize_stream(s['name'], s['id']), html_root)
    outfile.write(header)
    for t in s['topics']:
        outfile.write("* [{0}]({1}.html) ({2} message{4}, latest: {3})\n\n".format(
            t['name'], 
            sanitize_topic(t['name']), 
            s['topic_data'][t['name']]['size'],
            datetime.fromtimestamp(s['topic_data'][t['name']]['latest_date']).strftime('%b %d %Y at %H:%M'),
            '' if s['topic_data'][t['name']]['size'] == 1 else 's'
        ))
    outfile.close()

def write_stream_index(streams):
    outfile = open(md_root / md_index, 'w+', encoding='utf-8')
    outfile.write("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive\npermalink: {}/index.html\n---\n\n---\n\n## Streams:\n\n".format(html_root))
    for s in streams:
        outfile.write("* [{0}]({1}/index.html) ({2} topic{3})\n\n".format(
            s['name'], 
            sanitize_stream(s['name'], s['id']), 
            len(s['topics']),
            '' if len(s['topics']) == 1 else 's'))
    outfile.close()

def format_topic_header(stream, topic_name):
    return ("---\nlayout: page\ntitle: Lean Prover Zulip Chat Archive \npermalink: {4}/{2}/{3}.html\n---\n\n" + 
            "## Stream: [{0}](index.html)\n### Topic: [{1}]({3}.html)\n\n---\n\n").format(stream['name'], topic_name, sanitize_stream(stream['name'], stream['id']), sanitize_topic(topic_name), html_root)

def get_topic_and_write(stream, topic):
    json_path = json_root / Path(sanitize_stream(stream['name'], stream['id'])) / Path (sanitize_topic(topic['name']) + '.json')
    f = open(json_path, 'r', encoding='utf-8')
    messages = json.load(f)
    f.close()
    o = open_outfile(md_root / Path(sanitize_stream(stream['name'], stream['id'])), Path(sanitize_topic(topic['name']) + '.md'), 'w+')
    o.write(format_topic_header(stream, topic['name']))
    o.write('\n{% raw %}\n')
    write_topic(messages['messages'], stream['name'], stream['id'], topic['name'], o)
    o.write('\n{% endraw %}\n')
    o.close()

def write_markdown():
    f = open(json_root / Path('stream_index.json'), 'r', encoding='utf-8')
    streams = json.load(f, encoding='utf-8')
    f.close()
    write_stream_index(streams)
    for s in streams:
        print('building: ', s['name'])
        write_topic_index(s)
        for t in s['topics']:
            get_topic_and_write(s, t)

#populate_all()
write_markdown()