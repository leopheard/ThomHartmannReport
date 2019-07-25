# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/thomhartmann
#------------------------------------------------------------
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.thomhartmannprogram'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "thomhartmann"

# Entry point
def run():
    plugintools.log("videorun.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass

    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("videorun.main_list "+repr(params))
#note below - some YTs are /user/xxx and some /channel/xxx
    plugintools.add_item( 
        #action="", 
        title="Thom Hartmann Program",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )

run()
