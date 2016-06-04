import os
from irc3 import utils

from harvester import gyazo
from harvester import imgur
from harvester import ppomf
from harvester import bpaste
from harvester import dpaste
from harvester import infotomb
from harvester import prntscrn
from harvester import hastebin
from harvester import pastebin
from harvester import cubeupload
from os import environ


class Settings(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def getSettings(cls):
        dct = {}
        for key, value in cls.__dict__.items():
            if not key.startswith('__') and not callable(key):
                dct[key] = value
        return dct

class HarvesterSettings(Settings):

    # to put logs in bot folder, not ~/irc3 or some shit
    bot_basedir = os.path.split(os.path.dirname(__file__))[0]

    harvested_channels = [
        '#brotherBot'
    ]

    archive_base_path = os.path.join(bot_basedir, 'archive')

    service_regex_dict = {
        "^https?://pastebin\.com/((raw\.php\?i=)|(raw/))?[A-Za-z0-9]+": pastebin.get_content,
        # those are unfortunately dead :( RIP
        # '^https?://p\.pomf\.se/[\d.]+': ppomf.get_content,
        # '^https?://(?:infotomb\.com|itmb\.co)/[0-9a-zA-Z.]+': infotomb.get_content,
        '^https?://prntscr\.com/[0-9a-zA-Z]+': prntscrn.get_content,
        # dpaste doesnt get along with https, so we're not gonna bother
        '^http://dpaste\.com/[0-9a-zA-Z]+(.txt)?': dpaste.get_content,
        '^https?://bpaste\.net/(raw|show)/[0-9a-zA-Z]+': bpaste.get_content,
        '^https?://hastebin.com/([a-z]+(\.[a-z]+)|(raw/[a-z]+)|([a-z]+))': hastebin.get_content,
        # here come the image hosters
        '^https?://(i\.)?cubeupload\.com/(im/)?[a-zA-Z0-9.]+': cubeupload.get_content,
        '^https?://(cache\.|i\.)?gyazo.com/[a-z0-9]{32}(\.png)?': gyazo.get_content,
        '^https?://(i\.)?imgur\.com/(a/|gallery/)?[a-zA-Z0-9.,]+': imgur.get_content,
    }
