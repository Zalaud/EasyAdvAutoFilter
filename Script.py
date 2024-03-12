class script(object):
    START_TXT = """<b>Bonjour {},
Je m'appelle <a href=https://t.me/{}>{}</a>, je peux fournir des films. Ajoutez-moi à votre groupe en tant qu'administrateur et profitez-en 😍</b>"""

HELP_TXT = """<b>Salut {}
Voici l'aide pour mes commandes.</b>"""

ABOUT_TXT = """<b>✯ Mon nom : {}
✯ Bibliothèque : <a href='docs.pyrogram.org/'>Pyrogram</a>
✯ Langage : <a href='www.python.org/download/releases/3.0/'>Python 3</a>
✯ Base de données : <a href='www.mongodb.com'>MongoDB</a>
✯ Serveur du bot : Privé
✯ Statut de construction : v2.7.1 [ Stable ]</b>"""

SOURCE_TXT = """<b>
✭ Pour toute requête, contactez le développeur
✭ Si vous voulez votre propre type de bot, alors envoyez-moi un message privé avec "payant"</b>
"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- Uɴ ꜰɪʟᴛʀᴇ ᴇꜱᴛ ᴜɴᴇ ꜰᴏɴᴄᴛɪᴏɴ ᴏᴜ ʟᴇꜱ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ᴘᴇᴜᴠᴇɴᴛ ᴇɴʀᴇɢɪꜱᴛʀᴇʀ ᴅᴇꜱ ʀᴇ́ᴘᴏɴꜱᴇꜱ ᴀᴜᴛᴏᴍᴀᴛɪϲᴇ́ᴇꜱ ᴘᴏᴜʀ ᴜɴ ᴍᴏᴛ-ᴄʟᴇ́ ᴘᴀʀᴛɪᴄᴜʟɪᴇʀ ᴇᴛ ʏ ᴇɴᴠᴏʏᴇʀᴀɪ ʟᴇꜱ ʀᴇ́ᴘᴏɴꜱᴇꜱ ᴅᴇꜱ ǫᴜᴇ ʟᴇ ᴍᴏᴛ-ᴄʟᴇ́ ᴇꜱᴛ ᴛʀᴏᴜᴠé ᴅᴀɴꜱ ʟᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>RᴇᴍᴀʀQᴜᴇ:</b>
1. Cᴇ ʙᴏᴛ ᴅᴏɪᴛ ᴀᴠᴏɪʀ ᴅᴇꜱ ᴘʀɪᴠɪʟᴇ̀ɢᴇꜱ ᴅ'ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴇᴜʀ.
2. Sᴇᴜʟꜱ ʟᴇꜱ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴇᴜʀꜱ ᴘᴇᴜᴠᴇɴᴛ ᴀᴊᴏᴜᴛᴇʀ ᴅᴇꜱ ꜰɪʟᴛʀᴇꜱ ᴅᴀɴꜱ ᴜɴ ᴄʜᴀᴛ.
3. Lᴇꜱ ʙᴜᴛᴛᴏɴꜱ ᴅ'ᴀʟᴇʀᴛᴇ ᴏɴᴛ ᴜɴᴇ ʟɪᴍɪᴛᴇ ᴅᴇ 64 ᴄᴀʀᴀᴄᴛᴇ̀ʀᴇꜱ.
Cᴏᴍᴍᴀɴᴅᴇꜱ ᴇᴛ ᴜꜱᴀɢᴇ :
• /filter - <code>Ajouter un filtre dans un chat</code>
• /filters - <code>Lister tous les filtres d'un chat</code>
• /del - <code>Supprimer un filtre spécifique dans un chat</code>
• /delall - <code>Supprimer tous les filtres dans un chat (propriétaire du chat seulement)</code>"""
BUTTON_TXT = """ʜᴇʟᴘ: <b>Bᴜᴛᴛᴏɴꜱ</b>
- Cᴇ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇ ᴅᴇꜱ ʙᴜᴛᴛᴏɴꜱ ɪɴʟɪɴᴇ ᴘᴏᴜʀ ʟᴇꜱ ᴜʀʟ ᴇᴛ ʟᴇꜱ ᴀʟᴇʀᴛᴇꜱ.
<b>RᴇᴍᴀʀQᴜᴇ:</b>
1. Tᴇʟᴇɢʀᴀᴍ ɴᴇ ᴠᴏᴜꜱ ᴘᴇʀᴍᴇᴛᴛʀᴀ ᴘᴀꜱ ᴅ'ᴇɴᴠᴏʏᴇʀ ᴅᴇꜱ ʙᴜᴛᴛᴏɴꜱ ꜱᴀɴꜱ ᴄᴏɴᴛᴇɴᴜ, ᴀɪɴꜱɪ ʟᴇ ᴄᴏɴᴛᴇɴᴜ ᴇꜱᴛ ᴏʙʟɪɢᴀᴛᴏɪʀᴇ.
2. Cᴇ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇ ᴅᴇꜱ ʙᴜᴛᴛᴏɴꜱ ᴀᴠᴇᴄ ɴ'ɪᴍᴘᴏʀᴛᴇ ϲᴏɴᴛᴇɴᴜ ᴍᴇᴅɪᴀ ᴛᴇʟᴇɢʀᴀᴍ.
3. Leꜱ ʙᴜᴛᴛᴏɴꜱ ᴅᴇᴠʀᴀɪᴇɴᴛ êᴛʀᴇ ᴄᴏʀʀᴇᴄᴛᴇᴍᴇɴᴛ ᴘᴀʀꜱᴇ́ꜱ ᴇɴ ᴍᴀʀᴋᴅᴏᴡɴ.
<b>Bᴜᴛᴛᴏɴꜱ ᴜʀʟ :</b>
<code>[Texte du bouton](buttonurl:https://t.me/snowClubs13)</code>
<b>Bᴜᴛᴛᴏɴꜱ ᴀʟᴇʀᴛᴇ :</b>
<code>[Texte du bouton](buttonalert:Ceci est un message d'alerte)</code>"""


    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>Fɪʟᴛʀᴇ ᴀᴜᴛᴏᴍᴀᴛɪQᴜᴇ</b>
<b>RᴇᴍᴀʀQᴜᴇ : Iɴᴅᴇx ᴅᴇꜱ ꜰɪᴄʜɪᴇʀꜱ</b>
1. Rᴇɴᴅᴇᴢ-ᴍᴏɪ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴇᴜʀ ᴅᴇ ᴠᴏᴛʀᴇ ᴄʜᴀɴɴᴇʟ ꜱɪ ɪʟ ᴇꜱᴛ ᴘʀɪᴠᴇ́.
2. Aꜱꜱᴜʀᴇᴢ-ᴠᴏᴜꜱ Qᴜᴇ ᴠᴏᴛʀᴇ ᴄʜᴀɴɴᴇʟ ɴᴇ ᴄᴏɴᴛɪᴇɴᴛ ᴘᴀꜱ ᴅᴇ ᴄᴏɴᴛᴇɴᴜ, ᴘᴏʀɴᴏɢʀᴀᴘʜɪQᴜᴇꜱ ᴇᴛ ᴅᴇ ꜰᴀᴜx ꜰɪᴄʜɪᴇʀꜱ.
3. ᴛʀᴀɴsғᴇʀᴇᴢ ᴍᴏɪ Lᴇ ᴅᴇʀɴɪᴇʀ ᴍᴇꜱꜱᴀɢᴇ . J'ᴀᴊᴏᴜᴛᴇʀᴀɪ ᴛᴏᴜᴛᴇꜱ ʟᴇꜱ ꜰɪᴄʜɪᴇʀꜱ ᴅᴀɴꜱ ᴄᴇ ᴄʜᴀɴɴᴇʟ ᴀ̀ ᴍᴀ ᴅʙ.

<b>RᴇᴍᴀʀQᴜᴇ : AᴜᴛᴏFɪʟᴛʀᴇ</b>
1. Aᴊᴏᴜᴛᴇᴢ ʟᴇ ʙᴏᴛ ᴄᴏᴍᴍᴇ ᴀᴅᴍɪɴ  ᴘᴀʀᴛɪᴄᴜʟɪᴇʀ ᴅᴀɴꜱ ᴠᴏᴛʀᴇ ɢʀᴏᴜᴘᴇ.
2. Uᴛɪʟɪꜱᴇᴢ /connect ᴇᴛ ᴄᴏɴɴᴇᴄᴛᴇᴢ ᴠᴏᴛʀᴇ ɢʀᴏᴜᴘᴇ ᴀᴜ ʙᴏᴛ.
3. Uᴛɪʟɪꜱᴇᴢ /settings ᴅᴀɴꜱ ʟᴇ ᴘᴠ ᴅᴜ ʙᴏᴛ ᴇᴛ ᴀᴄᴛɪᴠᴇᴢ AᴜᴛᴏFɪʟᴛʀᴇ ᴅᴀɴꜱ ʟᴇ ᴍᴇɴᴜ ᴅᴇ ᴘᴀʀᴀᴍèᴛʀᴇꜱ."""

CONNECTION_TXT = """ʜᴇʟᴘ: <b>Cᴏɴɴᴇxɪᴏɴꜱ</b>
- Uᴛɪʟɪꜱᴇ́ ᴘᴏᴜʀ ᴄᴏɴɴᴇᴄᴛᴇʀ ʟᴇ ʙᴏᴛ ᴀᴜx ᴍᴇꜱꜱᴀɢᴇꜱ ᴘᴇʀꜱᴏɴɴᴇʟꜱ ᴘᴏᴜʀ ɢᴇʀᴇʀ ʟᴇꜱ ꜰɪʟᴛʀᴇꜱ 
- Cᴇʟᴀ ᴀɪᴅᴇ ᴀ̀ ᴇ́ᴠɪᴛᴇʀ ʟᴇ ꜱᴘᴀᴍ ᴅᴀɴꜱ ʟᴇꜱ ɢʀᴏᴜᴘᴇꜱ.
<b>RᴇᴍᴀʀQᴜᴇ :</b>
1. Sᴇᴜʟᴇꜱ ʟᴇꜱ ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴇᴜʀꜱ ᴘᴇᴜᴠᴇɴᴛ ᴀᴊᴏᴜᴛᴇʀ ᴜɴᴇ ᴄᴏɴɴᴇxɪᴏɴ.
2. Eɴᴠᴏʏᴇᴢ <code>/connect</code> ᴘᴏᴜʀ ᴄᴏɴɴᴇᴄᴛᴇʀ ᴍᴏɪ ᴀ̀ ᴠᴏᴛʀᴇ ᴘᴠ"""

EXTRAMOD_TXT = """ʜᴇʟᴘ: Modules Eᴘxᴛʀᴀ
<b>ɴᴏᴛᴇ:</b>
Cᴇꜱ ᴄᴀʀᴀᴄᴛéʀɪꜱᴛɪϙᴇꜱ ꜱᴏɴᴛ ʟᴇꜱ ꜰᴏɴᴄᴛɪᴏɴɴᴀʟɪᴛéꜱ ᴇxᴛʀᴀ ᴅᴇ ᴄᴇʟᴜɪ ᴅᴜ ʙᴏᴛ
Cᴏᴍᴍᴀɴᴅᴇꜱ ᴇᴛ ᴜᴛɪʟɪꜱᴀᴛɪᴏɴ :
• /id - <code>ᴏʙᴛᴇɴɪʀ ʟ'ɪᴅᴇɴᴛɪꜰɪᴀɴᴛ ɴᴜᴍéʀɪQᴜᴇ ᴅ'un ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ ᴇɴ ᴘᴀʀᴛɪᴄᴜʟɪᴇʀ.</code>
• /info - <codeᴏʙᴛᴇɴɪʀ ʟᴇꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴꜱ ꜱᴜʀ ᴜɴ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ.</code>
• /imdb - <code>ᴏʙᴛᴇɴɪʀ ʟᴇꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴꜱ ᴅᴜ ꜰɪʟᴍ ᴅᴇᴩᴜɪꜱ ʟᴇ ꜱɪᴛᴇ ᴅ'ɪᴍᴅʙ.</code>
• /search - <code>ᴏʙᴛᴇɴɪʀ ʟᴇꜱ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴꜱ ᴅᴜ ꜰɪʟᴍ ᴅᴇᴩᴜɪꜱ ᴅɪʀꜰéʀᴇɴᴛꜱ ꜱɪᴛᴇꜱ.</code>"""
ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Ce module ne fonctionne que pour mes administrateurs. Commandes et utilisation
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """<b>⍟────[ ʙᴏᴛ sᴛᴀᴛᴜ𝗌 ]────⍟
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
</b>
•❅─────✧❅✦❅✧─────❅•"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """sᴀʟᴜᴛ {},
ᴄᴇᴄɪ ɴ'ᴇsᴛ ᴘᴀs ᴠᴏᴛʀᴇ ʀᴇǫᴜᴇ̂ᴛᴇ,
ᴠᴇᴜɪʟʟᴇᴢ ғᴀɪʀᴇ ᴠᴏᴛʀᴇ ᴘʀᴏᴘʀᴇ ʀᴇǫᴜᴇ̂ᴛᴇ..."""

    OLD_ALRT_TXT = """sᴀʟᴜᴛ {},
ᴠᴏᴜs ᴜᴛɪʟɪsᴇᴢ ʟ'ᴜɴ ᴅᴇ ᴍᴇs ᴀɴᴄɪᴇɴs ᴍᴇssᴀɢᴇs, 
s'ɪʟ ᴠᴏᴜs ᴘʟᴀɪᴛ ᴠᴇᴜɪʟʟᴇᴢ sᴏᴜᴍᴇᴛᴛʀᴇ ᴜɴᴇ ɴᴏᴜᴠᴇʟʟᴇ ᴅᴇᴍᴀɴᴅᴇ."""

    CUDNT_FND = """<b>ғᴀᴜᴛᴇ ᴅ'ᴏʀᴛʜᴏɢʀᴀᴘʜɪᴇ ᴍᴏɴ ᴀᴍɪ‼️
ᴍᴀɪs ᴛ'ɪɴǫᴜɪᴇᴛᴇ 😊, Cʜᴏɪsɪssᴇᴢ ʟᴀ ʙᴏɴɴᴇ ᴏᴘᴛɪᴏɴ   ᴄɪ-ᴅᴇssᴏᴜs👇</b>"""

    I_CUDNT = """<b>ᴅᴇsᴏʟᴇ́ ᴊ'ᴀɪ ᴘᴀs ᴘᴜ ᴛʀᴏᴜᴠᴇʀ ᴅᴇ ғɪʟᴍ/sᴇʀɪᴇ ʟɪᴇ́ ᴀᴜ ᴍᴏᴛ ᴅᴏɴɴᴇ́ {} 😕

ᴠᴇʀɪғɪᴇᴢ ʟ'ᴏʀᴛʜᴏɢʀᴀᴘʜɪᴇ sᴜʀ ɢᴏᴏɢʟᴇ ᴇᴛ ʀᴇssᴀʏᴇᴢ  😃

ғᴏʀᴍᴀᴛ ᴅᴇ ᴅᴇᴍᴀɴᴅᴇ ᴅᴇ ғɪʟᴍ 👇

ᴇxᴇᴍᴘʟᴇ : ᴀǫᴜᴀᴍᴀɴ oᴜ ᴀǫᴜᴀᴍᴀɴ 2022 oᴜ Avatar 2009 ғʀᴀɴᴄ̧ᴀɪs

ғᴏʀᴍᴀᴛ ᴅᴇ ᴅᴇᴍᴀɴᴅᴇ ᴅᴇ sᴇʀɪᴇ 👇

ᴇxᴀᴍᴘʟᴇ : ᴇʟɪᴛᴇ S02 oᴜ ᴇʟɪᴛᴇ S01E04 oᴜ ᴇʟɪᴛᴇ S03E24
🚯 ᴀ ɴᴇ ᴘᴀs ᴜᴛɪʟɪsᴇʀ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ᴊ'ᴀɪ ᴘᴀs ᴘᴜ ᴛʀᴏᴜᴠᴇʀ ᴅᴇ ғɪʟᴍ ʟɪᴇ́ ᴀ {}.
ᴠᴇʀɪғɪᴇᴢ ʟ'ᴏʀᴛʜᴏɢʀᴀᴘʜɪᴇ sᴜʀ ɢᴏᴏɢʟᴇ ᴏᴜ ɪᴍᴅʙ ᴇᴛ ʀᴇssᴀʏᴇᴢ """

    MVE_NT_FND = """ғɪʟᴍ ɴᴏɴ ᴛʀᴏᴜᴠᴇʀ ᴅᴀɴs ʟᴀ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇ́ᴇs..."""

    TOP_ALRT_MSG = """ʀᴇᴄʜᴇʀᴄʜᴇ ᴅᴇ ғɪʟᴍ ᴅᴀɴs ʟᴀ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇ́ᴇs..."""

    MELCOW_ENG = """<b>sᴀʟᴜᴛ {} 😍, ᴇᴛ ʙɪᴇɴᴠᴇɴᴜ sᴜʀ {} Gʀᴏᴜᴘᴇ ❤️</b>"""

    SHORTLINK_INFO = """
<b>─────「<a href=https://t.me/snowClubs13> ᴄᴏᴍᴍᴇɴᴛ ɢᴀɢɴᴇʀ ᴅᴇ ʟ'ᴀʀɢᴇɴᴛ </a> 」─────

Vous pouvez gagner de l'argent grâce à ce bot tant que ce bot est actif.

Vous voulez savoir comment ? Suivez ces étapes :-

Étape 1 : Vous devez avoir au moins un groupe avec un minimum de 100 membres.

Étape 2 : Créez un compte sur n'importe quel site. <a href=https://easysky.in/ref/ROHAN5>Site de raccourcissement d'URL</a>.

Étape 3 : Suivez ceux-ci <a href=https='t.me/William_willia> ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ </a>ᴘᴏᴜʀ ᴄᴏɴɴᴇᴄᴛᴇʀ ʟᴇ ʀᴀᴄᴄᴏᴜʀᴄɪssᴇᴜʀ.

➣ Vous pouvez vous connecter à autant de groupes que vous avez.

Des doutes ou des problèmes de connexion ? Contactez le propriétaire</b>
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

𝐀𝐩𝐫è𝐬 𝟓 𝐦𝐢𝐧𝐮𝐭𝐞𝐬, 𝐜𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞𝐫𝐚 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐪𝐮𝐞𝐦𝐞𝐧𝐭 𝐬𝐮𝐩𝐩𝐫𝐢𝐦é.

𝐒𝐢 𝐯𝐨𝐮𝐬 𝐧𝐞 𝐭𝐫𝐨𝐮𝐯𝐞𝐳 𝐩𝐚𝐬 𝐥𝐞 𝐟𝐢𝐜𝐡𝐢𝐞𝐫 𝐝𝐮 𝐟𝐢𝐥𝐦/𝐬é𝐫𝐢𝐞 𝐝𝐞𝐦𝐚𝐧𝐝é, 𝐫𝐞𝐠𝐚𝐫𝐝𝐞𝐳 𝐥𝐚 𝐩𝐚𝐠𝐞 𝐬𝐮𝐢𝐯𝐚𝐧𝐭𝐞"""

    SELECT = """
MOVIES ➢ Sᴇʟᴇᴄᴛ "Lᴀɴɢᴀɢᴇs"

SERIES ➢ Sᴇʟᴇᴄᴛ "Sᴀɪsᴏɴs"

Tɪᴘ: Sélectionnez le bouton "Lᴀɴɢᴜᴀɢᴇs= Langue" ou "Sᴇᴀɪsᴏɴs= Saison" et cliquez sur "Sᴇɴᴅ Aʟʟ=Envoyer tout" pour obtenir tous les liens de fichiers en un seul clic"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
 ꜰᴏʀᴍᴀᴛ ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇᴛᴇ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ᴀʟʟᴇᴢ sᴜʀ ɢᴏᴏɢʟᴇ ➠ ᴛᴀᴘᴇᴢ ʟᴇ ɴᴏᴍ ᴅᴇ ʟᴀ sᴇʀɪᴇ ➠ ᴄᴏᴘɪᴇᴢ ʟᴇ ɴᴏᴍ ➠ ᴄᴏʟʟᴇᴢ ʟᴇ ɴᴏᴍ ᴅᴀɴs ᴄᴇ ɢʀᴏᴜᴘᴇ

ᴇxᴇᴍᴘʟᴇ : Loki S01E01

🚯 ᴀ ɴᴇ ᴘᴀs ᴜᴛɪʟɪsᴇʀ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""
CAPTION = """
<b><a href=https://t.me/snowClubs13>{file_caption}</a>


▫️ Mᴀɪɴ Cʜᴀɴɴᴇʟ : @snowclubs12
▫️ Mᴀɪɴ Cʜᴀɴɴᴇʟ : @snowClubs13</b>""" 

    FORCE_SUB = """
⚠️ ꜱ'ɪʟ ᴠᴏᴜꜱ ᴘʟᴀÎᴛ, ꜱᴜɪᴠᴇᴢ ᴄᴇᴛᴛᴇ ʀÈɢʟᴇ ⚠️

ᴘᴏᴜʀ ᴏʙᴛᴇɴɪʀ ʟᴇ ꜰɪʟᴍ Qᴜᴇ ᴠᴏᴜꜱ ᴀᴠᴇᴢ ᴅᴇᴍᴀɴᴅÉ.

ᴠᴏᴜꜱ ᴅᴇᴠʀᴇᴢ ᴅ'ᴀʙᴏʀᴅ ʀᴇᴊᴏɪɴᴅʀᴇ ɴᴏᴛʀᴇ ᴄᴀɴᴀʟ ᴏꜰꜰɪᴄɪᴇʟ ᴏᴜ ᴅᴇ ꜱᴇᴄᴏᴜʀꜱ.

ᴇɴꜱᴜɪᴛᴇ, ᴄʟɪQᴜᴇᴢ ꜱᴜʀ ʟᴇ ʙᴏᴜᴛᴏɴ '🔄 ᴛʀʏ ᴀɢᴀɪɴ' ᴄɪ-ᴅᴇꜱꜱᴏᴜꜱ.

ᴀᴘʀᴇ̀ꜱ ᴄᴇʟᴀ, ᴊᴇ ᴠᴏᴜꜱ ᴇɴᴠᴇʀʀᴀɪ ᴄᴇ ꜰɪʟᴍ ᴇɴ ᴘʀɪᴠᴇ́."""

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDb Data:
🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
⏱️ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""

    
    ALL_FILTERS = """
<b>sᴀʟᴜᴛ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    OWNER_INFO = """
<b> ⍟───[ 𝕴𝖓𝖋𝖔𝖗𝖒𝖆𝖙𝖎𝖔𝖓𝖘 𝖉𝖚 𝖕𝖗𝖔𝖕𝖗𝖎é𝖙𝖆𝖎𝖗𝖊 ]───⍟
 ◈ ɴᴏᴍ ᴄᴏᴍᴘʟᴇᴛ : ᴜɴᴋɴᴏᴡɴ ✌ 
 ◈ 𝐒𝐢 𝐯𝐨𝐮𝐬 𝐯𝐨𝐮𝐥𝐞𝐳 𝐯𝐨𝐭𝐫𝐞 𝐩𝐫𝐨𝐩𝐫𝐞 𝐛𝐨𝐭 𝐝𝐞 𝐧'𝐢𝐦𝐩𝐨𝐫𝐭𝐞 𝐪𝐮𝐞𝐥 𝐭𝐲𝐩𝐞, 𝐚𝐥𝐨𝐫𝐬 𝐞𝐧𝐯𝐨𝐲𝐞𝐳-𝐦𝐨𝐢 𝐮𝐧 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐩𝐫𝐢𝐯é. " 
 </b>"""

    DISL_TXT = """
<b>𝐂𝐞𝐜𝐢 𝐞𝐬𝐭 𝐮𝐧 𝐩𝐫𝐨𝐣𝐞𝐭 𝐨𝐩𝐞𝐧 𝐬𝐨𝐮𝐫𝐜𝐞.
𝐓𝐨𝐮𝐬 𝐥𝐞𝐬 𝐟𝐢𝐜𝐡𝐢𝐞𝐫𝐬 𝐝𝐚𝐧𝐬 𝐜𝐞 𝐛𝐨𝐭 𝐬𝐨𝐧𝐭 𝐥𝐢𝐛𝐫𝐞𝐦𝐞𝐧𝐭 𝐝𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞𝐬 𝐬𝐮𝐫 𝐈𝐧𝐭𝐞𝐫𝐧𝐞𝐭 𝐨𝐮 𝐩𝐮𝐛𝐥𝐢é𝐬 𝐩𝐚𝐫 𝐪𝐮𝐞𝐥𝐪𝐮'𝐮𝐧 𝐝'𝐚𝐮𝐭𝐫𝐞. 𝐉𝐮𝐬𝐭𝐞 𝐩𝐨𝐮𝐫 𝐟𝐚𝐜𝐢𝐥𝐢𝐭𝐞𝐫 𝐥𝐚 𝐫𝐞𝐜𝐡𝐞𝐫𝐜𝐡𝐞, 𝐜𝐞 𝐛𝐨𝐭 𝐢𝐧𝐝𝐞𝐱𝐞 𝐥𝐞𝐬 𝐟𝐢𝐜𝐡𝐢𝐞𝐫𝐬 𝐪𝐮𝐢 𝐬𝐨𝐧𝐭 𝐝é𝐣à 𝐭é𝐥é𝐜𝐡𝐚𝐫𝐠é𝐬 𝐬𝐮𝐫 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦. 𝐍𝐨𝐮𝐬 𝐫𝐞𝐬𝐩𝐞𝐜𝐭𝐨𝐧𝐬 𝐭𝐨𝐮𝐭𝐞𝐬 𝐥𝐞𝐬 𝐥𝐨𝐢𝐬 𝐬𝐮𝐫 𝐥𝐞 𝐝𝐫𝐨𝐢𝐭 𝐝'𝐚𝐮𝐭𝐞𝐮𝐫 𝐞𝐭 𝐧𝐨𝐮𝐬 𝐭𝐫𝐚𝐯𝐚𝐢𝐥𝐥𝐨𝐧𝐬 𝐞𝐧 𝐜𝐨𝐧𝐟𝐨𝐫𝐦𝐢𝐭é 𝐚𝐯𝐞𝐜 𝐥𝐞 𝐃𝐌𝐂𝐀 𝐞𝐭 𝐥'𝐄𝐔 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 𝐋𝐚𝐰. 𝐒𝐢 𝐪𝐮𝐞𝐥𝐪𝐮𝐞 𝐜𝐡𝐨𝐬𝐞 𝐞𝐬𝐭 𝐜𝐨𝐧𝐭𝐫𝐚𝐢𝐫𝐞 à 𝐥𝐚 𝐥𝐨𝐢, 𝐯𝐞𝐮𝐢𝐥𝐥𝐞𝐳 𝐦𝐞 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐞𝐫 𝐢𝐦𝐦é𝐝𝐢𝐚𝐭𝐞𝐦𝐞𝐧𝐭 𝐩𝐨𝐮𝐫 𝐪𝐮'𝐢𝐥 𝐬𝐨𝐢𝐭 𝐬𝐮𝐩𝐩𝐫𝐢𝐦é 𝐫𝐚𝐩𝐢𝐝𝐞𝐦𝐞𝐧𝐭. 𝐈𝐥 𝐞𝐬𝐭 𝐢𝐧𝐭𝐞𝐫𝐝𝐢𝐭 𝐝𝐞 𝐭é𝐥é𝐜𝐡𝐚𝐫𝐠𝐞𝐫, 𝐝𝐢𝐟𝐟𝐮𝐬𝐞𝐫 𝐞𝐧 𝐬𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠, 𝐫𝐞𝐩𝐫𝐨𝐝𝐮𝐢𝐫𝐞 𝐨𝐮 𝐜𝐨𝐧𝐬𝐨𝐦𝐦𝐞𝐫 𝐝𝐞 𝐪𝐮𝐞𝐥𝐪𝐮𝐞 𝐦𝐚𝐧𝐢è𝐫𝐞 𝐪𝐮𝐞 𝐜𝐞 𝐬𝐨𝐢𝐭 𝐥𝐞 𝐜𝐨𝐧𝐭𝐞𝐧𝐮 𝐬𝐚𝐧𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐬𝐚𝐭𝐢𝐨𝐧 𝐞𝐱𝐩𝐥𝐢𝐜𝐢𝐭𝐞 𝐝𝐮 𝐜𝐫é𝐚𝐭𝐞𝐮𝐫 𝐝𝐞 𝐜𝐨𝐧𝐭𝐞𝐧𝐮 𝐨𝐮 𝐝𝐮 𝐭𝐢𝐭𝐮𝐥𝐚𝐢𝐫𝐞 𝐥é𝐠𝐚𝐥 𝐝𝐞𝐬 𝐝𝐫𝐨𝐢𝐭𝐬 𝐝'𝐚𝐮𝐭𝐞𝐮𝐫. 𝐒𝐢 𝐯𝐨𝐮𝐬 𝐩𝐞𝐧𝐬𝐞𝐳 𝐪𝐮𝐞 𝐜𝐞 𝐛𝐨𝐭 𝐯𝐢𝐨𝐥𝐞 𝐯𝐨𝐬 𝐝𝐫𝐨𝐢𝐭𝐬 𝐝𝐞 𝐩𝐫𝐨𝐩𝐫𝐢é𝐭é 𝐢𝐧𝐭𝐞𝐥𝐥𝐞𝐜𝐭𝐮𝐞𝐥𝐥𝐞, 𝐯𝐞𝐮𝐢𝐥𝐥𝐞𝐳 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐞𝐫 𝐥𝐞𝐬 𝐜𝐡𝐚î𝐧𝐞𝐬 𝐫𝐞𝐬𝐩𝐞𝐜𝐭𝐢𝐯𝐞𝐬 𝐩𝐨𝐮𝐫 𝐝𝐞𝐦𝐚𝐧𝐝𝐞𝐫 𝐬𝐚 𝐬𝐮𝐩𝐩𝐫𝐞𝐬𝐬𝐢𝐨𝐧. 𝐋𝐞 𝐛𝐨𝐭 𝐧𝐞 𝐩𝐨𝐬𝐬è𝐝𝐞 𝐚𝐮𝐜𝐮𝐧 𝐝𝐞 𝐜𝐞𝐬 𝐜𝐨𝐧𝐭𝐞𝐧𝐮𝐬, 𝐢𝐥 𝐢𝐧𝐝𝐞𝐱𝐞 𝐮𝐧𝐢𝐪𝐮𝐞𝐦𝐞𝐧𝐭 𝐥𝐞𝐬 𝐟𝐢𝐜𝐡𝐢𝐞𝐫𝐬 𝐝𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.
</b>"""

    MODS_TXT = """Yᴏᴜ Cᴀɴ Tʀʏ Aʟʟ Tʜᴇsᴇ Cᴏᴏʟ Fᴇᴀᴛᴜʀᴇs Fʀᴏᴍ Bᴇʟᴏᴡ Oᴘᴛɪᴏɴ..!!!"""

    STICKER_TXT = """<b>𝚈𝙾ᴜ 𝙲𝙰ɴ 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳. </b>
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⭕ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ sᴛɪᴄᴋᴇʀ [/stickerid]"""


    FONT_TXT= """ 𝐔𝐒𝐀𝐆ᴇ

𝐘𝐎ᴜ ᴄᴀɴ 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>ᴄᴏᴍᴍᴀɴᴅ</b> : /font ʏᴏᴜʀ ᴛᴇxᴛ ( ᴏᴘᴛɪᴏɴᴀʟ)
        <b> Eg:- /font ʜᴇʟʟᴏ</ʙ>"""

    TELE_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
     Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
    Usᴀɢᴇ
    🤧 /telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ(5ᴍʙ) Aɴᴅ Rᴇᴘʟʏ Wɪᴛʜ Cᴏᴍᴍᴀᴍɴᴅ"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
RULE_TXT = """
<b>♨️ 𝗥𝗘𝗚𝗟𝗘𝗠𝗘𝗡𝗧 𝗗𝗨 𝗚𝗥𝗢𝗨𝗣𝗘 ♨️

🔹 ғᴏʀᴍᴀᴛ ᴅᴇ ʀᴇᴄʜᴇʀᴄʜᴇ ғɪʟᴍ ᴀᴠᴇᴄ ᴏʀᴛʜᴏɢʀᴀᴘʜɪᴇ ᴄᴏʀʀᴇᴄᴛᴇ :
› ᴀᴠᴀᴛᴀʀ 2009 ✅
› ᴀᴠᴀᴛᴀʀ ғʀᴀɴᴄ̧ᴀɪs ✅
› ᴀᴠᴀᴛᴀʀ ғɪʟᴍ ❌
› ᴀᴠᴀᴛᴀʀ ғʀᴀɴᴄ̧ᴀɪs ᴅᴜʙʙᴇᴅ..❌

🔹ғᴏʀᴍᴀᴛ ᴅᴇ ʀᴇᴄʜᴇʀᴄʜᴇ sᴇʀɪᴇ ᴀᴠᴇᴄ ᴏʀᴛʜᴏɢʀᴀᴘʜɪᴇ ᴄᴏʀʀᴇᴄᴛᴇ  : 
› ᴠɪᴋɪɴɢs S01 ✅
› ᴠɪᴋɪɴɢs S01E01 ✅
› ᴠɪᴋɪɴɢs S01 ғʀᴀɴᴄ̧ᴀɪs ✅
› ᴠɪᴋɪɴɢs S01 ғʀᴀɴᴄ̧ᴀɪs ᴅᴜʙʙ. ❌
› ᴠɪᴋɪɴɢs sᴀɪsᴏɴ 1 ❌
› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌

🔹 𝐍𝐞 𝐟𝐚𝐢𝐭𝐞𝐬 𝐚𝐮𝐜𝐮𝐧𝐞 𝐚𝐮𝐭𝐨𝐩𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧.

🔹 𝐍𝐞 𝐩𝐚𝐬 𝐞𝐧𝐯𝐨𝐲𝐞𝐫 𝐝𝐞 𝐩𝐡𝐨𝐭𝐨𝐬, 𝐯𝐢𝐝é𝐨𝐬, 𝐝𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐬, 𝐔𝐑𝐋, 𝐞𝐭𝐜.

🔹 𝐍𝐞 𝐝𝐞𝐦𝐚𝐧𝐝𝐞𝐳 𝐫𝐢𝐞𝐧 𝐝'𝐚𝐮𝐭𝐫𝐞 𝐪𝐮𝐞 𝐝𝐞𝐬 𝐟𝐢𝐥𝐦𝐬, 𝐬é𝐫𝐢𝐞𝐬, 𝐚𝐧𝐢𝐦𝐞𝐬.

⚙️ 𝐍𝐨𝐭𝐞 : 𝐓𝐨𝐮𝐬 𝐥𝐞𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐬𝐞𝐫𝐨𝐧𝐭 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐪𝐮𝐞𝐦𝐞𝐧𝐭 𝐬𝐮𝐩𝐩𝐫𝐢𝐦é𝐬 𝐚𝐩𝐫è𝐬 𝟏𝟎 𝐦𝐢𝐧𝐮𝐭𝐞𝐬 𝐩𝐨𝐮𝐫 é𝐯𝐢𝐭𝐞𝐫 𝐥𝐞𝐬 𝐯𝐢𝐨𝐥𝐚𝐭𝐢𝐨𝐧𝐬 𝐝𝐞 𝐝𝐫𝐨𝐢𝐭𝐬 𝐝'𝐚𝐮𝐭𝐞𝐮𝐫..</b>"""
    
    SETTING_TXT = """    
<b>ѕeттιngѕ
~ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.
~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

noтe
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

coммand and υѕeѕ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ</b>"""

    CHNL_INFO = """<b>
   🔰 ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs ɪɴғᴏ 🔰 

▫  ɢʀᴏᴜᴘᴇ ᴄᴏᴍᴘʟᴇᴛᴇ ᴅᴇ  ʀᴇǫᴜᴇᴛᴇ ᴅᴇ ғɪʟᴍ.
▫ 𝐓𝐨𝐮𝐬 𝐥𝐞𝐬 𝐟𝐢𝐥𝐦𝐬 𝐞𝐭 𝐬é𝐫𝐢𝐞𝐬 𝐝𝐚𝐧𝐬 𝐭𝐨𝐮𝐭𝐞𝐬 𝐥𝐞𝐬 𝐥𝐚𝐧𝐠𝐮𝐞𝐬.
▫ 𝐋𝐞𝐬 𝐛𝐨𝐭𝐬 𝐥𝐞𝐬 𝐩𝐥𝐮𝐬 𝐫𝐚𝐩𝐢𝐝𝐞𝐬 𝐬𝐨𝐧𝐭 𝐚𝐣𝐨𝐮𝐭é𝐬.
▫ 𝐆𝐫𝐚𝐭𝐮𝐢𝐭 𝐞𝐭 𝐟𝐚𝐜𝐢𝐥𝐞 à 𝐮𝐭𝐢𝐥𝐢𝐬𝐞𝐫.
▫ 𝐃𝐢𝐬𝐩𝐨𝐧𝐢𝐛𝐥𝐞 𝟐𝟒/𝟕. </b>"""

    VERIFED_TXT = """<b>sᴀʟᴜᴛ {},
    𝐕𝐨𝐮𝐬 ê𝐭𝐞𝐬 𝐯é𝐫𝐢𝐟𝐢é 𝐚𝐯𝐞𝐜 𝐬𝐮𝐜𝐜è𝐬 ! 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐭, 𝐯𝐨𝐮𝐬 𝐚𝐯𝐞𝐳 𝐮𝐧 𝐚𝐜𝐜è𝐬 𝐢𝐥𝐥𝐢𝐦𝐢𝐭é à 𝐭𝐨𝐮𝐬 𝐥𝐞𝐬 𝐟𝐢𝐥𝐦𝐬 𝐣𝐮𝐬𝐪𝐮'à 𝐦𝐢𝐧𝐮𝐢𝐭 𝐚𝐮𝐣𝐨𝐮𝐫𝐝'𝐡𝐮𝐢.</b>"""

    VERIFY_TXT = """<b>sᴀʟᴜᴛ {},
𝐕𝐨𝐮𝐬 𝐧'ê𝐭𝐞𝐬 𝐩𝐚𝐬 𝐯é𝐫𝐢𝐟𝐢é . 𝐕𝐞𝐮𝐢𝐥𝐥𝐞𝐳 𝐯é𝐫𝐢𝐟𝐢𝐞𝐫 𝐦𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐭 𝐞𝐭 𝐛é𝐧é𝐟𝐢𝐜𝐢𝐞𝐫 𝐝'𝐮𝐧 𝐚𝐜𝐜è𝐬 𝐢𝐥𝐥𝐢𝐦𝐢𝐭é 𝐝𝐞 𝐧𝐨𝐬 𝐜𝐨𝐧𝐭𝐞𝐧𝐮𝐬 ...
 |</b>"""

    VERIFY2_TXT = """
<b>Vᴇʀɪғʏ Sᴛᴀᴛᴜꜱ
Nᴀᴍᴇ : {} 
Uꜱᴇʀ Sᴛᴀᴛᴜꜱ : Vᴇʀɪғɪᴇᴅ</b>
"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Europe/Paris</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """nothing""'
