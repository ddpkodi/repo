

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.peketv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Pocoyo", "channel/UCs156bCTwCkfDypjJ8xxh5Q", 'https://yt3.ggpht.com/a-/AAuE7mB9bUhrmCR9G9MdQvs0BFM6Jqkcuq99Tm808A=s200-mo-c-c0xffffffff-rj-k-no'),
		("Peppa Pig", "channel/UCZdl3r-feGWZcfdUSIpZ61A", 'https://yt3.ggpht.com/a-/AAuE7mDpiU6MbXwIgtcunUq1YhXAnFL4kAO7T9iTCg=s200-mo-c-c0xffffffff-rj-k-no'),
		("Doraemon", "channel/UC5tS62gRTSdTv3-n1eOUsHg", 'https://yt3.ggpht.com/a-/AAuE7mCW5gxrCyHDbqEdNYJpqLeN-9_ri7P-wlLcbA=s288-mo-c-c0xffffffff-rj-k-no'),
		("Ben y Holly", "user/BenYHollyOficial", 'http://img2.rtve.es/imagenes/pequeno-reino-ben-holly/1417868917308.jpg'),
		("Zou", "channel/UCNRxSlbyvxgc0gI5cqB_0mg", 'https://yt3.ggpht.com/a-/AAuE7mBzD4TG3OjnmhvULYdNjPQEPAXiBucf2ZPsVQ=s288-mo-c-c0xffffffff-rj-k-no'),
		("Heidi", "channel/UCdEXcerFvd-Um_HETgu4lRA", 'https://yt3.ggpht.com/a-/AAuE7mDahaWU5GUyim3_f7lKWlvJAg-aMNIyMWeIzA=s288-mo-c-c0xffffffff-rj-k-no'),
		("Caillou", "channel/UC2snMV8Hhf9z9RXkrFEyu8w", 'https://yt3.ggpht.com/a-/AAuE7mAxuLNhMdzRpSPADwuhThvaAYDuQGA9sAXz-Q=s288-mo-c-c0xffffffff-rj-k-no'),
		("Jorge el Curioso", "channel/UCRsg6o_XHRmvGrwFujs2ywg", 'https://yt3.ggpht.com/a-/AAuE7mAio-9rMVivN_3nAwTxel-BkXQJxznzXWbFnw=s288-mo-c-c0xffffffff-rj-k-no'),
		("Los Teletubbies", "channel/UCOnprKBB5g8HgTAr0CBCzzg", 'https://yt3.ggpht.com/a-/AAuE7mAbFtsrZgdH4u6z3W89v8jqM5JtafIzCrckjA=s288-mo-c-c0xffffffff-rj-k-no'),
		("La Brujita Tatty", "channel/UCZE5p7Ht5kYdCDW7COKso3w", 'https://yt3.ggpht.com/a-/AAuE7mDX0RQf5x4-0U_wehfzLb6u4gTODL0QsZxYMA=s288-mo-c-c0xffffffff-rj-k-no'),
		("La Pantera Rosa", "channel/UCY3AW6KSQ3vboZgwyDYY33Q", 'https://yt3.ggpht.com/a-/AAuE7mAcYeEbt_PvtMYwklSq6-xX9oJbmHEa0P30Uw=s288-mo-c-c0xffffffff-rj-k-no'),
		("PJ Mask", "/channel/UCgCsnqSO7_oGkL3hdLZfnaQ", 'https://yt3.ggpht.com/a-/AAuE7mCH0iL28vEyHaScWP7O96tQ7yTA_YlU1edspg=s288-mo-c-c0xffffffff-rj-k-no'),
		("Los Pitufos", "channel/UCenlP5URcdwcuXPQ8I9aOZw", 'https://i.pinimg.com/236x/67/03/90/670390a5bb2f56258b240ffb5b00e0b2.jpg'),
		("El pajaro Loco", "channel/UCHtZ2_7hd1zy9aCqrrcaqcQ", 'https://yt3.ggpht.com/a-/AAuE7mACRmPDr9BdS3TGKeSrb8cm0BTK8EKkEZ-M=s288-mo-c-c0xffffffff-rj-k-no'),
		("Leo el Camion", "channel/UCuk_csKI_Y88lV0V51VpeuQ", 'https://yt3.ggpht.com/a-/AAuE7mByH8VDt1kJ-yI5gYFz4mkXe5h163VD_tYTmg=s288-mo-c-c0xffffffff-rj-k-no'),
		("Sherlock Jack", "channel/UCU8VbR_j-JYSyBjThtu_Zyw", 'http://img2.rtve.es/imagenes/sherlock-yack/1418807538550.png'),
		("Nene Leon", "user/videosneneleon", 'https://yt3.ggpht.com/a-/AAuE7mBqdV2gGijSNQgQV40ktZCFiRoPApKatT_YbQ=s288-mo-c-c0xffffffff-rj-k-no'),
		("Shin Chan", "channel/UCk0DXu69SBZpiF8Cgu1AJyg", 'http://images6.fanpop.com/image/photos/39000000/Shinchan-shinchan-39009000-189-181.png'),
		("Cuentos Infantiles", "channel/UCjgRtV0zjOfsCP0_i3DjA8A", 'https://yt3.ggpht.com/a-/AAuE7mDA-ip1cNGwQPY4OvlJHgXnf728HSpRIwhpYA=s288-mo-c-c0xffffffff-rj-k-no'),
		("Canciones Infantiles", "user/toycantando", 'https://yt3.ggpht.com/a-/AAuE7mCl5FIwpXPYRca9USn6JPeSgsRwkDX_n5AGRQ=s288-mo-c-c0xffffffff-rj-k-no'),
		("CantaJuego", "user/CantaJuegoVEVO", 'https://yt3.ggpht.com/a-/AAuE7mAAjqf_1kE1jVAY3Jz0bX4LqKkkc_CddpR97w=s288-mo-c-c0xffffffff-rj-k-no'),
		
		
]



# Entry point
def run():
    plugintools.log("peketv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("peketv.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()