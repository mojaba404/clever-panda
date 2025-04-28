from os import remove
import os

import time

os.environ['TZ'] = 'Asia/Tehran'
time.tzset()
from sansorchi import sansor
import jdatetime
import wikipedia
import random
from requests import get
from pyrogram.types import Message
from time import sleep
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import os
from pyrogram.enums import UserStatus
from io import StringIO
from googletrans import Translator, constants
from pprint import pprint
translator = Translator()
from pyrogram import enums
from random import choice
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from jsoner import *
from vip import *
from fontfile import font_numer,font_en,font_fa
from re import IGNORECASE
import sys
import contextlib

bot = Client('panda_helper',api_id = '00000',api_hash = '0000')

app = Client('panda',
api_id='00000',
                    api_hash='0000',bot_token='6337440978:000')
                    


"""

telegram channel : @pycode_hub



"""
admin = [00000,000]
nobalad = []
blok = []
mat = []
dast = []
rank = read_file('rank.json')
time_sleep = read_file('time_sleep.json')
lang = read_file('lang.json')
polite = []
block_group = []
sodo = [-1001732634318,-1001874085556]
member = [917449521,1051169788]
vip_group = get_gps()
bot_user = "@Clever_panda_bot"
with app:
      bh = open(f'member.txt', 'r')
      bj = open(f'member.txt', 'a+')
      h = bh.read()
      for i in h.split():
        if int(i) not in member:
       		member.append(int(i))
      bj.write(h)

with app:
      fh = open(f'blocklist.txt', 'r')
      bh = open(f'blocklist.txt', 'a+')
      h = fh.read()
      for i in h.split():
        if int(i) not in block_group:
       		block_group.append(int(i))
      bh.write(h)
@contextlib.contextmanager
def stdout_io(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

@app.on_message(filters.command("py") & filters.user(admin) & filters.chat(sodo) & ~filters.forwarded)
def exec_python(client,message):
    code = message.text[3:]
    try:
        with stdout_io() as s:
            exec(code)
        client.send_message(message.chat.id, s.getvalue())
    except Exception as e:
        client.send_message(message.chat.id, str(e))
    
@app.on_message(filters.command('send') & filters.chat(sodo))
def send_message(client, message):
        if message.reply_to_message:
            for d in member:
                    try:
                        message.reply_to_message.copy(d)
                        sleep(0.5)
                    except:
                        pass


@app.on_message(filters.command('forward') & filters.chat(sodo))
def forwardmessage(client, message):
          if message.reply_to_message:
            for d in member:
                    try:
                    	app.forward_messages(
                    	    d, message.chat.id, message.reply_to_message.id)
                    	sleep(0.5)
                    except:
                    	pass


@app.on_message(filters.command('left') & filters.chat(sodo))
def left_group(client, message):
  if len(message.command) == 2:
  	try:
  		  app.send_message(
  		    message.command[1], 'من به دستور مدیریت از این گروه لفت میدم بای بای👋')
  	except:
  		pass
  	try:
  		remove(f'text{message.chat.id}.txt')
  	except:
  		pass
  	try:
  		remove(f'gif{message.chat.id}.txt')
  	except:
  		pass
  	try:
  		remove(f'sticker{message.chat.id}.txt')
  	except:
  		pass
  	app.leave_chat(message.command[1])

@app.on_message(filters.command('tr') & filters.group,group=3)
def trans(client, message):
	if message.reply_to_message.text and len(message.command) == 2 and message.chat.id not in dast and message.chat.id in vip_group:
		dast.append(message.from_user.id)
		try:
		    	    admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
		    	    if message.from_user.id in admins or message.from_user.id in admin:
		    	    		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
		    	    			app.send_message(message.chat.id,translator.translate(message.reply_to_message.text, dest=message.command[1]).text)
		    	    		else:
		    	    			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
		except:
			pass
		sleep(2)
		dast.remove(message.from_user.id)

@app.on_message(filters.command(['font_en', f'font_en{bot_user}']) & filters.group)
def font_English(client, message):
   if message.from_user.id not in dast:
      dast.append(message.from_user.id)
      try:
      	print(app.get_users(message.from_user.id))
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      			try:
      				text= 'فونت های شما'
      				mssg = ''
      				for i in message.command[1:]:
      					mssg = mssg + ' ' + i
      				font_list = font_en(mssg)
      				for i in font_list:
      					text = text +'\n' + i
      				message.reply(text)
      			except Exception as e:
	       			message.reply_text(e)
      		else:
      				     	 	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      		pass
      sleep(2)
      dast.remove(message.from_user.id)
@app.on_message(filters.command('photo') & filters.group,group=3)
def photo(client, message):
 if len(message.command) != 1 and message.chat.id not in dast and message.chat.id in vip_group:
  dast.append(message.from_user.id)
  try:
           admins = [i.user.id for i in app.get_chat_members(
           message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
           if message.from_user.id in admins or message.from_user.id in admin:
             if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
               text = ''
               for i in message.command[1:]:
                  	text = text + i + ' '
               try:                  
                  r = bot.get_inline_bot_results("bing",query=text)
                  payam = bot.send_inline_bot_result(-1001879200567,r.query_id, random.choice(r.results).id)
                  app.copy_message(message.chat.id,-1001879200567,payam.updates[0].id)
               except:
               	app.send_message(message.chat.id,f'چیزی درباره {text} پیدا نشده است')
             else:
              message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  except:
   pass
  sleep(2)
  dast.remove(message.from_user.id)

@app.on_message(filters.command('music') & filters.group,group=3)
def music(client, message):
 if len(message.command) != 1 and message.chat.id not in dast and message.chat.id in vip_group:
  dast.append(message.from_user.id)
  try:
           admins = [i.user.id for i in app.get_chat_members(
           message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
           if message.from_user.id in admins or message.from_user.id in admin:
             if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
               text = ''
               for i in message.command[1:]:
                  	text = text + i + ' '
               try:                  
                  r = bot.get_inline_bot_results("vkmusic_bot",query=text)
                  payam = bot.send_inline_bot_result(-1001879200567,r.query_id, r.results[0].id)
                  app.copy_message(message.chat.id,-1001879200567,payam.updates[0].id)
               except:
               	app.send_message(message.chat.id,f'چیزی درباره {text} پیدا نشده است')
             else:
              message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  except:
   pass
  sleep(2)
  dast.remove(message.from_user.id)    
            
@app.on_message(filters.command(['font_number', f'font_number{bot_user}']) & filters.group)
def font_adad(client, message):
   if message.from_user.id not in dast:
      dast.append(message.from_user.id)
      try:
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      			try:
      				text= 'فونت های شما'
      				mssg = ''
      				for i in message.command[1:]:
      					mssg = mssg + ' ' + i
      				font_list = font_numer(mssg)
      				for i in font_list:
      					text = text +'\n' + i
      				message.reply(text)
      			except Exception as e:
	       			message.reply_text(e)
      		else:
      				     	 	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      		pass
      sleep(2)
      dast.remove(message.from_user.id)
      		
@app.on_message(filters.command(['fa_font', f'fa_font{bot_user}']) & filters.group)
def font_persain(client, message):
   if message.from_user.id not in dast:
      dast.append(message.from_user.id)
      print(1)
      try:
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      			try:
      				txt = ''
      				msg = ''
      				for i in message.command[1:]:
      					msg = msg + i + ' '
      				for j in font_fa.keys():
      					for i in msg:
      						txt += font_fa[j].get(i, i)
      					txt += '\n'
      				message.reply_text(txt)
      			except Exception as e:
	       			message.reply_text(e)
      		else:
      				     	 	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      		pass
      sleep(2)
      dast.remove(message.from_user.id)
      		
		
@app.on_message(filters.command(['proxy',f'proxy{bot_user}']) & filters.group)
def proxy(client, message):
      if message.from_user.id not in dast:
      	if len(message.command) == 1 and message.chat.id in vip_group:
      		dast.append(message.from_user.id)
      		try:
	      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
	      			text = 'لیست پروکسی ها:'
	      			a = bot.get_chat_history('ProxyMTProto',limit=10)
	      			msg = []
	      			for i in a:
	      				if a[0].reply_markup.inline_keyboard:
	      					msg.append(a[0].reply_markup.inline_keyboard[0][0].url)
	      			app.send_message(message.chat.id,text,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("proxy1",url=msg[0]),InlineKeyboardButton("proxy2",url=msg[1])],[InlineKeyboardButton("proxy3",url=msg[2]),InlineKeyboardButton("proxy4",url=msg[3])],[InlineKeyboardButton("proxy5",url=msg[4]),InlineKeyboardButton("proxy6",url=msg[5])],[InlineKeyboardButton("proxy7",url=msg[6]),InlineKeyboardButton("proxy8",url=msg[7])],[InlineKeyboardButton("proxy9",url=msg[8]),InlineKeyboardButton("proxy10",url=msg[9])]]))
	      		else:
	      			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      		except:
     			 pass
	      	sleep(2)
	      	dast.remove(message.from_user.id)

@app.on_message(filters.command(['info',f'info{bot_user}']) & filters.group)
def info(client, message):
  if message.reply_to_message:
      if message.from_user.id not in dast:
      	if len(message.command) == 1:
	      	dast.append(message.from_user.id)
      		try:
	      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
	      		  if len(rank[str(message.reply_to_message.from_user.id)]) == 0:
	      		  	if app.get_users(message.reply_to_message.from_user.id).username != None:
	      		  		app.send_message(message.chat.id, f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• یوزرنیم : @{app.get_users(message.reply_to_message.from_user.id).username}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}''')
	      		  	else:
	      		  		app.send_message(message.chat.id,f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}''')
	      		  else:
	      		  	ranklist = ''
	      		  	for i in rank[str(message.reply_to_message.from_user.id)]:
	      		  		ranklist = ranklist+i
	      		  	if app.get_users(message.reply_to_message.from_user.id).username != None:
	      		  		app.send_message(message.chat.id, f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• یوزرنیم : @{app.get_users(message.reply_to_message.from_user.id).username}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}
• مدال : {ranklist}''')
	      		  	else:
	      		  		app.send_message(message.chat.id,f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}
• مدال : {ranklist}''')
	      		else:
	      			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      		except:
      			try:
      				if app.get_users(message.reply_to_message.from_user.id).username != None:
	      		  		app.send_message(message.chat.id, f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• یوزرنیم : @{app.get_users(message.reply_to_message.from_user.id).username}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}''')
      				else:
	      		  		app.send_message(message.chat.id,f'''• آیدی عددی : {app.get_users(message.reply_to_message.from_user.id).id}
• نام کاربر : {app.get_users(message.reply_to_message.from_user.id).first_name}''')
      			except:
      				pass
	      	sleep(2)
	      	dast.remove(message.from_user.id)

@app.on_message(filters.command(['stupid', f'stupid{bot_user}']) & filters.group)
def Stupid(client, message):
   if message.from_user.id not in dast:
      if len(message.command) == 1:
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      		dast.append(message.from_user.id)
      		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      			try:
      				chat = message.chat.id
      				if chat not in nobalad:
      					message.reply_text("من از الان خنگ میشم هیچ کلمه ای رو یاد نمی گیرم")
      					nobalad.append(chat)
      				else:
      					message.reply_text("من از قبل هم خنگ بودم")
      			except Exception as e:
	       			pass
      		else:
      				     	 	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      		sleep(2)
      		dast.remove(message.from_user.id)


@app.on_message(filters.command(['clever', f'clever{bot_user}']) & filters.group)
def Clever(client, message):
  if message.from_user.id not in dast:
    dast.append(message.from_user.id)
    try:
      if len(message.command) == 1:
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      	  if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      	  	chat = message.chat.id
      	  	if chat in nobalad:
      	  		message.reply_text('چشم از الان پاندای زرنگی میشم و تمام کلمات رو یاد میگیرم')
      	  		nobalad.remove(chat)
      	  	else:
      	  		message.reply_text('شوخیت گرفته، اسم من پاندا زرنگه من همه کلمات رو یاد میگیرم')
      	  else:
      	  	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
    except:
      	  pass
    sleep(2)
    dast.remove(message.from_user.id)


p_startlistblok = []


@app.on_message(filters.command(['start', f'start{bot_user}']) & filters.private)
def statrt(client, message):
  	if message.chat.id not in p_startlistblok:
  		p_startlistblok.append(message.chat.id)
  		if message.chat.id not in member:
  			member.append(message.chat.id)
  			fh = open(f'member.txt', 'w')
  			bh = open(f'member.txt', 'r')
  			h = bh.read()
  			b = ''
  			for i in member:
  				b = b + '\n' + str(i)
  			fh.write(b)
  		if str(message.chat.id) not in rank:
  			rank[str(message.chat.id)] = []
  			write_file(rank,'rank.json')
  		username = app.get_me().username
  		app.send_message(message.chat.id, """سلام
من پاندای زرنگ هستم 🐼
حالا من چیکار میکنم؟
من از شما ها حرف زدن یاد میگیرم و باهاتون حرف می زنم 😅
منو تو گروهت اضافه کن تا همه رو بخندونم🐼""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🐼افزودن به گروه🐼", url=f"https://t.me/{username}?startgroup=add")]]))
  		sleep(2)
  		p_startlistblok.remove(message.chat.id)
  		
@app.on_message(filters.command('viplist') & filters.chat(sodo))
def viplist(client, message):
	if len(message.command) ==1:
		b = 'group list:'
		for i in vip_group:
			b = b + f'{i}' + ' ' + f'{app.get_chat(i).title}' +' ' + f'{get_time(i)}' + '\n'
		fh = open(f'viplist.txt', 'w+')
		fh.write(b)
		fh.close()
		app.send_document(message.chat.id,'viplist.txt')
		os.remove('viplist.txt')
@app.on_message(filters.command('addrank') & filters.chat(sodo))
def addrank(client, message):
	if len(message.command) == 3:
		if int(message.command[1]) in member and message.command[1] in rank:
					if message.command[2] not in rank[message.command[1]]:
						rank[str(message.command[1])].append(message.command[2])
						write_file(rank,'rank.json')
						message.reply('رنک کاربر با موفیقت ست شد')
					else:
						message.reply('این کاربر از قبل این رنک را دارا بوده است')
		else:
					message.reply('این کاربر جزو کاربران ربات نمی باشد')

@app.on_message(filters.command('delrank') & filters.chat(sodo))
def delrank(client, message):
	if len(message.command) == 3:
		if int(message.command[1]) in member and message.command[1] in rank:
					if message.command[2] in rank[message.command[1]]:
						rank[str(message.command[1])].remove(message.command[2])
						write_file(rank,'rank.json')
						message.reply('رنک کاربر با موفیقت حذف شد')
					else:
						message.reply('این کاربر این رنک را دارا نبوده است')
		else:
					message.reply('این کاربر جزو کاربران ربات نمی باشد')					
@app.on_message(filters.command(['polite', f'polite{bot_user}']) & filters.group)
def panda_polite(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group:
  	if len(message.command) == 1:
  	 dast.append(message.from_user.id)
  	 try:
  	 	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  	 	if message.from_user.id in admins or message.from_user.id in admin:
  	 		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	 			chat = message.chat.id
  	 			if chat not in polite:
  	 				message.reply_text('چشم از این به بعد فقط حرفای قشنگ رو یاد میگیرم')
  	 				polite.append(chat)
  	 			else:
  	 				message.reply_text('من از قبل هم هیچ حرف زشتی رو یاد نمی گرفتم')
  	 		else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  	 except:
	   	pass
  	 sleep(1)
  	 dast.remove(message.from_user.id)


@app.on_message(filters.command(['impolite', f'impolite{bot_user}']) & filters.group)
def panda_impolite(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group:
  	if len(message.command) == 1:
  	 dast.append(message.from_user.id)
  	 try:
  	     admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  	     if message.from_user.id in admins or message.from_user.id in admin:
  	     	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	     		chat = message.chat.id
  	     		if chat in polite:
  	     			message.reply_text('باشه از الان به بعد کلمات برام فرقی ندارن همه رو یاد میگیرم')
  	     			polite.remove(chat)
  	     		else:
  	     		 	message.reply_text(
  	 			    'من از قبل هم کلمات برام فرقی نداشت همه رو یاد می گرفتم')
  	     	else:
  	     		message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  	 except:
  	 	pass
  	 sleep(1.5)
  	 dast.remove(message.from_user.id)

@app.on_message(filters.text  & ~filters.forwarded & ~filters.me & filters.group, group=1)
def text_learn(client, message):
  if message.chat.id not in nobalad:
    if message.text[0] != '/' and len(message.text) > 1:
     if message.chat.id not in polite:
     	try:
	      b = ''
	      a = message.text.split()
	      fh = open(f'text{message.chat.id}.txt', 'a')
	      bh = open(f'text{message.chat.id}.txt', 'r')
	      h = bh.read()
	      for i in a:
	    	   if '/' not in i and i not in h:
       			b = b + '\n' + i
	      fh.write(b)
     	except Exception as e:
     		message.reply(e)
     elif message.chat.id in polite and message.chat.id in vip_group:
     	try:
	      b = ''
	      a = message.text.split()
	      fh = open(f'text{message.chat.id}.txt', 'a')
	      bh = open(f'text{message.chat.id}.txt', 'r')
	      h = bh.read()
	      for i in a:
	    	   if '/' not in i and i not in h and '*' not in sansor(i):
       			b = b + '\n' + i
	      fh.write(b)
     	except Exception as e:
     		message.reply(e)


@app.on_message(~filters.forwarded & ~filters.me & filters.group & ~filters.new_chat_members, group=2)
def Speak(client, message):
 if message.chat.id not in mat:
   mat.append(message.chat.id)
   try:
   	fh = open(f'text{message.chat.id}.txt', 'r')
   	h = fh.read()
   	c = []
   	f = ''
   	for i in h.splitlines():
	   	c.append(i)
   	chat = message.chat.id
   	if message.chat.id not in blok:
  		 x = random.randint(1, 13)
  		 if x == 1 or x == 2:
  		 	f = random.choice(c)
  		 elif x == 3 or x == 4 or x == 5:
  				a = random.choice(c)
  				c.remove(a)
  				a1 = random.choice(c)
  				f = a + ' ' + a1
  		 elif x == 6 or x == 7 or x == 8:
  		 	a = random.choice(c)
  		 	c.remove(a)
  		 	a1 = random.choice(c)
  		 	c.remove(a1)
  		 	a2 = random.choice(c)
  		 	f = a + ' ' + a1 + ' ' + a2
  		 elif x == 10 or x == 11:
  		 	a = random.choice(c)
  		 	c.remove(a)
  		 	a1 = random.choice(c)
  		 	c.remove(a1)
  		 	a2 = random.choice(c)
  		 	c.remove(a2)
  		 	a3 = random.choice(c)
  		 	f = a + ' ' + a1 + ' ' + a2 + ' ' + a3
  		 elif x == 12:
  	 		a = random.choice(c)
  		 	c.remove(a)
   			a1 = random.choice(c)
  	 		c.remove(a1)
  	 		a2 = random.choice(c)
  	 		c.remove(a2)
   			a3 = random.choice(c)
  	 		c.remove(a3)
   			a4 = random.choice(c)
   			f = a + ' ' + a1 + ' ' + a2 + ' ' + a3 + ' ' + a4
  		 elif x == 9 and message.chat.id in vip_group:
  		 	sgif = []
  		 	gi = open(f'gif{message.chat.id}.txt', 'r')
  		 	sd = gi.read()
  		 	for o in sd.splitlines():
  		 		sgif.append(o)
  	 		y = random.choice(sgif)
  	 		app.send_animation(message.chat.id, y)
  	 		sgif.clear()
  		 elif x == 13 and message.chat.id in vip_group:
  	 		stick = []
  		 	sik = open(f'sticker{message.chat.id}.txt', 'r')
  		 	sticke = sik.read()
  		 	for o in sticke.splitlines():
  		 		stick.append(o)
  	 		y = random.choice(stick)
  	 		app.send_sticker(message.chat.id, y)
  	 		stick.clear()
  		 c.clear()
  		 if len(f) > 1:
  		 	if message.chat.id in vip_group:
  		 		if str(message.chat.id) not in lang:
  		 			try:
  		 				msg1 = f'+{message.text}' + ' ' + '@#$_++&&(#(#+$)/@+_(#/#)_+_+#)#/$($(#)))$(_+_+_+$@/' + ' '+f'-{f}'
  		 				msg2 = translator.translate(msg1, dest='en').text
  		 				app.send_message(message.chat.id,translator.translate(msg2.split('@#$_++&&(#(#+$)/@+_(#/#)_+_+#)#/$($(#)))$(_+_+_+$@/')[1][1:],dest='fa').text)
  		 			except:
  		 				msg2 = translator.translate(f, dest='en').text
  		 				app.send_message(message.chat.id,translator.translate(msg2,dest='fa').text)
  		 		else:
  		 			try:
  		 				msg1 = f'+{message.text}' + ' ' + '@#$_++&&(#(#+$)/@+_(#/#)_+_+#)#/$($(#)))$(_+_+_+$@/' + ' '+f'-{f}'
  		 				msg2 = translator.translate(msg1, dest='en').text
  		 				app.send_message(message.chat.id,translator.translate(msg2.split('@#$_++&&(#(#+$)/@+_(#/#)_+_+#)#/$($(#)))$(_+_+_+$@/')[1][1:],dest=lang[str(message.chat.id)]).text)
  		 			except:
  		 				msg2 = translator.translate(f, dest='en').text
  		 				app.send_message(message.chat.id,translator.translate(msg2,dest=lang[str(message.chat.id)]).text)
  		 	else:
  		 		app.send_message(message.chat.id,f)
   except Exception as e:
   	   pass
   if str(message.chat.id) not in time_sleep or message.chat.id not in vip_group:
   	sleep(3)
   else:
   	sleep(time_sleep[str(message.chat.id)])
   mat.remove(message.chat.id)


@app.on_message(filters.animation & filters.group)
def gif_learn(client, message):
   if message.chat.id not in nobalad and message.chat.id in vip_group:
     try:
     	a = message.animation.file_id
     	fh = open(f'gif{message.chat.id}.txt', 'a')
     	bh = open(f'gif{message.chat.id}.txt', 'r')
     	h = bh.read()
     	c = []
     	for i in h.splitlines():
     		c.append(i)
     	if a not in h:
     		fh.write(f'{a}\n')
     	c.clear()
     except Exception as e:
	   		message.reply_text(e)


@app.on_message(filters.sticker & filters.group)
def sticker_learn(client, message):
	if message.chat.id not in nobalad and message.chat.id in vip_group:
	   try:
	   	a = message.sticker.file_id
	   	fh = open(f'sticker{message.chat.id}.txt', 'a')
	   	bh = open(f'sticker{message.chat.id}.txt', 'r')
	   	h = bh.read()
	   	c = []
	   	for i in h.splitlines():
	   		c.append(i)
	   	if a not in h:
	   		fh.write(f'{a}\n')
	   	c.clear()
	   except Exception as e:
	   	message.reply_text(e)

# done

@app.on_message(filters.command(['update']) & filters.group, group=6)
def panda_update(client, message):
 try:
    chat_id = message.chat.id
    if len(message.command) == 2 or message.from_user.id in admin:
        c = int(message.command[1])
        res = up_gp(chat_id, c)
        if res == 'this group is not valid!':
            app.send_message(message.chat.id,'این گروه اشتراک ویژه ندارد')
        else:
            app.send_message(message.chat.id,f'اشتراک گروه شما با موفیقت به مدت {message.command[1]} ماه تمدید شد')
    else:
        app.send_message(message.chat.id,'دستور وارد شده صحیح نمی باشد لطفا مقدار تعداد ماه افزوده را بعد از دستور وارد نمایید')
 except:
 	pass
 global vip_group
 vip_group = get_gps()
 
@app.on_message(filters.command(['addvip']) & filters.group, group=6)
def panda_add_vip(client, message):
 try:
  if len(message.command) == 2 and message.from_user.id in admin:
  	if add_gp(message.chat.id,int(message.command[1])) == 'ok added':
  		app.send_message(message.chat.id,'done')
  		app.send_message(message.chat.id,f'اشتراک گروه شما با موفیقت به مدت {message.command[1]} ماه فعال شد')
  	else:
  		app.send_message(message.chat.id,'این گروه از قبل اشتراک ویژه داشته') 
 except:
  pass
 global vip_group
 vip_group = get_gps()		
  
 
@app.on_message(filters.command(['delvip']) & filters.group, group=6)
def panda_del_vip(client, message):
 try:
  if len(message.command) == 1 and message.from_user.id in admin:
  	if del_gp(message.chat.id) == 'ok deleted.':
  		app.send_message(message.chat.id,'done')
  		app.send_message(message.chat.id,f'اشتراک گروه شما حذف شده است')
  	else:
  		app.send_message(message.chat.id,'این گروه اشتراک ویژه ندارد')
  elif len(message.command) == 2 and message.chat.id in sodo:
  		  	if del_gp(int(message.command[1])) == 'ok deleted.':
  		  		app.send_message(message.chat.id,'done')
  		  		app.send_message(int(message.command[1]),f'اشتراک گروه شما حذف شده است')
  		  	else:
  		  		app.send_message(message.chat.id,'این گروه اشتراک ویژه ندارد')
 except:
  				pass
 global vip_group
 vip_group = get_gps()
  				
@app.on_message(filters.command(['cleartext', f'cleartext{bot_user}']) & filters.group, group=6)
def text_clear(client, message):
	if len(message.command) == 1 and message.from_user.id not in dast:
		  try:
				 dast.append(message.from_user.id)
				 admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
				 if message.from_user.id in admins or message.from_user.id in admin:
						 if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
							 remove(f'text{message.chat.id}.txt')
							 app.send_message(
								 message.chat.id, 'لیست کلمات با موفیقت پاک شد')
						 else:
						 	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
		  except:
		  	pass
		  sleep(2)
		  dast.remove(message.from_user.id)
 	
@app.on_message(filters.command(['clearsticker',f'clearsticker{bot_user}']) & filters.group)
def sticker_clear(client, message):
      if len(message.command) ==1 and message.from_user.id not in dast:
      	try:
      			dast.append(message.from_user.id)
      			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      			if message.from_user.id in admins or message.from_user.id in admin:
      				if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      					remove(f'sticker{message.chat.id}.txt')
      					app.send_message(message.chat.id,'لیست استیکر ها با موفیقت پاکسازی شد')
      				else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      	except:
      	 		pass
      	sleep(2)
      	dast.remove(message.from_user.id)


# done
@app.on_message(filters.command(['cleargif',f'cleargif{bot_user}']) & filters.group)
def gif_clear(client, message):
    if len(message.command) == 1:
    		if message.from_user.id not in dast:
    			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    			if message.from_user.id in admins or message.from_user.id in admin:
    			  try:
    			  	dast.append(message.from_user.id)
    			  	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
    			  		remove(f'gif{message.chat.id}.txt')
    			  		app.send_message(message.chat.id,'لیست گیف ها با موفیقت پاکسازی شد')
    			  	else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
    			  except:
    			   	pass
    			  sleep(1.5)
    			  dast.remove(message.from_user.id)
 	
 	
# donenjjjjjjjfjjddjjdjdjdjdjdjdjdjsjjs
  			
@app.on_message(filters.command(['help',f'help{bot_user}'])& filters.group)
def command_help(client, message):
  	if message.from_user.id not in dast and len(message.command) == 1:
  		try:
  			dast.append(message.from_user.id)
  			app.send_message(message.chat.id,'''/silent سکوت کردن
/Talk شروع حرف زدن
/textlist دریافت لیست کلمات
/giflist دریافت فایل آیدی گیف ها
/stickerlist دریافت فایل استیکر ها
/left ترک گروه
/cleartext پاکسازی متن ها
* /cleargif پاکسازی گیف ها
* /clearsticker پاکسازی استیکر ها
/say متنی که در ادامه آن می نویسم توسط ربات نوشته می شود به شرطی که ادمین باشد
/stupid توقف یاد گیری
/clever شروع یادگیری
* /polite روشن کردن حالت با ادب
* /impolite خاموش کردن حالت با ادب
/ship شیپ کردن دو نفر
/shipall شیپ کردن کل گروه
/tag تگ کردن
* /search جستجو در‌ ویکی پدیا
/condition دریافت اطلاعات گروه
/info دریافت اطلاعات شخص
* /delword حذف کلمه
* /delsticker حذف استیکر 
* /delgif حذف گیف
* /settime تأیین زمان بین پیام دادن
/setwelcome تأیین پیام خوشآمد 
/welcome_on روشن کردن پیام خوشآمد
/welcome_off خاموش کردن پیام خوشآمد
/complete_help دریافت راهنمای کامل
* /proxy دریافت پروکسی
/fa_font فونت فارسی
/font_number فونت عدد 
/font_en فونت انگلیسی
* /tr ترجمه

دستوراتی که پشتشان ستاره وجود دارد برای گروه های ویژه است


my dev : Twilight group''')
  		except:
  			pass
  		sleep(1.5)
  		dast.remove(message.from_user.id)


@app.on_message(filters.command(['complete_help',f'complete_help{bot_user}'])& filters.group)
def command_help2(client, message):
  	if message.from_user.id not in dast and len(message.command) == 1:
  		dast.append(message.from_user.id)
  		try:
  			app.copy_message(message.chat.id, 'panda_help_command', 3)
  		except:
  			pass
  		sleep(1.5)
  		dast.remove(message.from_user.id)
  			
startlistblok = []
@app.on_message(filters.command(['start',f'start{bot_user}']) & filters.group)
def start(client, message):
  	if message.chat.id not in startlistblok and len(message.command) == 1:
  	 startlistblok.append(message.from_user.id)
  	 try:
  	 	username = app.get_me().username
  	 	app.send_message(message.chat.id,"""سلام
من پاندای زرنگ هستم 🐼
حالا من چیکار میکنم؟
من از شما ها حرف زدن یاد میگیرم و باهاتون حرف می زنم 😅
منو تو گروهت اضافه کن تا همه رو بخندونم🐼""",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🐼افزودن به گروه🐼",url=f"https://t.me/{username}?startgroup=add")]]))
  	 except:
  	 	pass
  	 sleep(2)
  	 startlistblok.remove(message.from_user.id)
  		
@app.on_message(filters.command(['say',f'say{bot_user}'])& filters.group)
def say_message(client, message):
  	if message.from_user.id not in dast:
  			if len(message.command) != 1:
  			  admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  			  if message.from_user.id in admins or message.from_user.id in admin:
  			  	dast.append(message.from_user.id)
  			  	try:
  			  		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  			  			message.delete()
  			  			mg = message.command[1:]
  			  			msg = ''
  			  			for i in mg:
  			 	 			msg = msg + ' '+i
  			 	 		app.send_message(message.chat.id,msg)
  			  		else:
  			  			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  			  	except:
  			  			try:
  			  				app.send_message(message.chat.id,'لطفا اول ربات را ادمین کنید و سپس دوباره تست کنید')
  			  			except:
  			  					pass
  			  	sleep(1)
  			  	dast.remove(message.from_user.id)




@app.on_message(filters.command('left')& filters.group)
def left_gp(client, message):
  if len(message.command) == 1:
  	if message.from_user.id in admin:
  		app.send_message(message.chat.id,'من به دستور مدیریت از گروه خارج میشم بای بای👋')
  		try:
  			remove(f'text{message.chat.id}.txt')
  		except:
  			pass
  		try:
  			remove(f'gif{message.chat.id}.txt')
  		except:
  			pass
  		try:
  			remove(f'sticker{message.chat.id}.txt')
  		except:
  			pass
  		app.leave_chat(message.chat.id)
 

# done
@app.on_message(filters.command(['giflist',f'giflist{bot_user}']) & filters.group)
def gif_list(client, message):
      if len(message.command) == 1 and message.from_user.id not in dast and message.chat.id in vip_group:
        	try:
     	  		dast.append(message.from_user.id)
     	  		admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
     	  		if message.from_user.id in admins or message.from_user.id in admin:
     	  			if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
     	  				app.send_document(message.chat.id,f'gif{message.chat.id}.txt')
     	  			else:
	     		 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
        	except:
        		pass
        	sleep(2)
        	dast.remove(message.from_user.id)
 
  
# done
@app.on_message(filters.command(['textlist',f'textlist{bot_user}']) & filters.group)
def texy_list(client, message):
  if len(message.command) == 1 and message.from_user.id not in dast:
    dast.append(message.from_user.id)
    try:
    	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    	if message.from_user.id in admins or message.from_user.id in admin:
    	   if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
    	   	app.send_document(message.chat.id,f'text{message.chat.id}.txt')
    	   else:
    	   	message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
    except:
           		pass
    sleep(1.5)
    dast.remove(message.from_user.id)
    	
# done
@app.on_message(filters.command(['stickerlist',f'stickerlist{bot_user}']) & filters.group)
def sticker_list(client, message):
   if message.from_user.id not in dast and message.chat.id in vip_group:
    dast.append(message.from_user.id)
    try:
    	 if len(message.command) == 1:
    		 admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    		 if message.from_user.id in admins or message.from_user.id in admin:
    			  if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
    			  	app.send_document(message.chat.id,f'sticker{message.chat.id}.txt')
    			  else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
    except:
    			pass
    sleep(2)
    dast.remove(message.from_user.id)
# done         
@app.on_message(filters.command(['silent',f'silent{bot_user}']) & filters.group)
def panda_silent(client, message):
   if message.from_user.id not in dast and len(message.command) == 1:
      dast.append(message.from_user.id)
      try:
      	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      	if message.from_user.id in admins or message.from_user.id in admin:
      	 		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      	 			chat = message.chat.id
      	 			if chat not in blok:
      		 			message.reply_text("چشم ساکت میشم")
      	 				blok.append(chat)
       				else:
       					message.reply_text('من از ابتدا ساکت بودم')
      	 		else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except Exception as e:
        print(e)
      sleep(2)
      dast.remove(message.from_user.id)
	       
# done  
@app.on_message(filters.command(['talk',f'talk{bot_user}']) & filters.group)
def panda_talk(client, message):
  if message.from_user.id not in dast and len(message.command) == 1:
     dast.append(message.from_user.id)
     try:
     	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
     	if message.from_user.id in admins or message.from_user.id in admin:
     		if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
     			chat = message.chat.id
     			if chat in blok:
     				message.reply_text('چشم حرف زدن رو شروع میکنم')
     				blok.remove(chat)
     			else:
     				message.reply_text('من از قبل هم حرف می زدم')
     		else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
     except:
     	pass
     sleep(2)
     dast.remove(message.from_user.id)

@app.on_message(filters.command(['tag',f'tag{bot_user}']) & filters.group)
def panda_tager(client, message):
 if message.chat.id not in dast:
  dast.append(message.chat.id)
  try:
  	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  	if message.from_user.id in admins or message.from_user.id in admin:
 	      if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
 	      	lim = message.command[1]
 	      	mg = message.command[2:]
 	      	x = message.chat.id
 	      	a = app.get_chat_members(x)
 	      	b = []
 	      	msg = ''
 	      	for i in mg:
 	      		msg = msg + ' '+i
 	      	for j in a:
 	      		  if j.user.first_name != None:
 	      		  	if not j.user.is_bot:
 	      		  		b.append('[{}](tg://user?id={})'.format(j.user.first_name, j.user.id))
 	      		  		if len(b) == int(lim):
 	      		  		  	b = '\n'.join(b)
 	      		  		  	app.send_message(message.chat.id, f'{b}\n{msg}')
 	      		  		  	sleep(1)
 	      		  		  	b = []
 	      else:
	     	 			message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
  except:
        pass
  sleep(2)
  dast.remove(message.chat.id)
        
                	
blok_ship =[]

@app.on_message(filters.command(['shipall',f'shipall{bot_user}']) & filters.group)
def panda_ship_all(client, message):
 if len(message.command) == 2 and message.chat.id not in blok_ship:
   blok_ship.append(message.chat.id)
   try:
   	admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
   	if message.from_user.id in admins or message.from_user.id in admin:
 	 	       if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
 	 	       	tedad = int(message.command[1])
 	 	       	users = [i.user for i in app.get_chat_members(message.chat.id) if not (i.user.is_bot or i.user.first_name==None) ]
 	 	       	if len(users) >= (tedad *2):
 	 	       		for i in range(tedad):
 	 	       			a = choice(users)
 	 	       			users.remove(a)
 	 	       			m = a.mention
 	 	       			m += ' ❤️ '
 	 	       			b = choice(users)
 	 	       			users.remove(b)
 	 	       			m += b.mention
 	 	       			app.send_message(message.chat.id,m)
 	 	       			sleep(1)
 	 	       	else:
 	 	       		mojaz = len(users) // 2
 	 	       		message.reply_text('حداکثر شیپ قابل قبول {} عدد میباشد'.format(mojaz))
 	 	       else:
 	 	       	message.reply('ابتدا ربات را استرات کنید و سپس دوباره تست کنید')
   except:
        pass 
   sleep(2)
   blok_ship.remove(message.chat.id)
        	
        
       
blok_ships =[]
                	
@app.on_message(filters.command(['ship',f'ship{bot_user}']) & filters.group)
def panda_ship(client, message):
  if message.from_user.id not in blok_ships:
   blok_ships.append(message.from_user.id)
   try:
   	  	  if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
   	  	  	x = message.chat.id
   	  	  	a = app.get_chat_members(x)
   	  	  	mem = []
   	  	  	for i in a:
   	  	  		if i.user.first_name != None:
   	  	  			if not i.user.is_bot:
   	  	  				mem.append(i)
   	  	  	rand = random.choice(mem)
   	  	  	mem.remove(rand)
   	  	  	rand1 = random.choice(mem)
   	  	  	mem.remove(rand1)
   	  	  	mention = '[{}](tg://user?id={})'.format(rand.user.first_name, rand.user.id)
   	  	  	mention1 = '[{}](tg://user?id={})'.format(rand1.user.first_name, rand1.user.id)
   	  	  	app.send_message(message.chat.id,f'{mention} ❤️ {mention1}')
   	  	  else:
      	 				message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
   except:
   	pass	     	 			
   sleep(1)
   blok_ships.remove(message.from_user.id)

serach_spam=[]
@app.on_message(filters.command(['search',f'search{bot_user}']) & filters.group)
def Search_Wikipedia(c,m):
  if m.from_user.id not in serach_spam:
    serach_spam.append(m.from_user.id)
    try:
     admins = [i.user.id for i in app.get_chat_members(
      	    m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
     if m.from_user.id in admins or m.from_user.id in admin and m.chat.id in vip_group:
      if m.from_user.id in member and app.get_users(m.from_user.id).status != UserStatus.LONG_AGO:
       try:
     	  if m.command[1] in ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'] :
    	   	n = m.command[2:]
  	     	b = ''
   	    	for i in n:
      	 		b = b+ i + ' '
 	      	wikipedia.set_lang(m.command[1])
       		Msg  = wikipedia.summary(b)
       		if len(Msg) < 4096:
       			app.send_message(m.chat.id,Msg)
       		elif len(Msg) > 4096 and len(Msg) < 8192:
     	  		app.send_message(m.chat.id,Msg[0:4096])
       			app.send_message(m.chat.id,Msg[4096:])
   	    	elif len(Msg) > 8192 and len(Msg) < 12288:
    	   		app.send_message(m.chat.id,Msg[0:4096])
       			app.send_message(m.chat.id,Msg[4096:8192])
 	      		app.send_message(m.chat.id,Msg[8192:])
     	  else:
	       	wikipedia.set_lang('fa')
   	    	la = m.command[1:]
   	    	l = ''
   	    	for i in la:
   	    		l = l + ' '+ i
     	  	Msg  = wikipedia.summary(l)
  	     	if len(Msg) < 4096:
      	 		app.send_message(m.chat.id,Msg)
   	    	elif len(Msg) > 4096 and len(Msg) < 8192:
    	   		app.send_message(m.chat.id,Msg[0:4096])
    	   		app.send_message(m.chat.id,Msg[4096:])
       		elif len(Msg) > 8192 and len(Msg) < 12288:
 	      		app.send_message(m.chat.id,Msg[0:4096])
  	     		app.send_message(m.chat.id,Msg[4096:8192])
      	 		app.send_message(m.chat.id,Msg[8192:])
       except Exception as e:
     	  if m.command[1] in ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']:
  	     	n = m.command[2:]
  	     	b = ''
   	    	for i in n:
    	   		b = b + ' '+  i
     	  	m.reply_text(f'چیزی در باره «{b}» یافت نشد')
     	  else:
	           n = m.command[1:]
	           b = ''
	           for i in n:
	           	b = b +' ' + i
	           m.reply_text(f'چیزی در باره «{b}» یافت نشد')
      else:
	     	 			m.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
    except Exception as e:
    	print(e)
    sleep(2)
    serach_spam.remove(m.from_user.id)


@app.on_message(filters.command(['condition',f'condition{bot_user}']) & filters.group)
def condition(client, message):
  if len(message.command) == 1 and message.from_user.id not in dast:
      dast.append(message.from_user.id)
      try:
      			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      			if message.from_user.id in admins or message.from_user.id in admin:
      				if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      					gap_name = app.get_chat(message.chat.id).title
      					tedad_member = app.get_chat_members_count(message.chat.id)
      					vip_mode = 'free'
      					if get_time(message.chat.id) != 'this group is not valid!':
      						vip_mode = 'vip'
      					if vip_mode != 'free':
      						app.send_message(message.chat.id,f'''نام گروه : {gap_name}
تعداد اعضا : {tedad_member}
تعداد پیام : {message.id}
آیدی گروه : {message.chat.id}
نوع اشتراک : vip
زمان پایان اشتراک : {get_time(message.chat.id)}''')
      					else:
      						app.send_message(message.chat.id,f'''نام گروه : {gap_name}
تعداد اعضا : {tedad_member}
تعداد پیام : {message.id}
آیدی گروه : {message.chat.id}
نوع اشتراک : free''')
      				else:
      					message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      	pass
      sleep(2)
      dast.remove(message.from_user.id)
  
 
wlc_message = read_file('welcome.json')
wlc_list = []
@app.on_message(filters.command(["setwelcome",f"setwelcome{bot_user}"]) & filters.group)
def setwlc(client,message):
  if len(message.command) == 1 and message.from_user.id not in dast:
      	dast.append(message.from_user.id)
      	try:
      			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      			if message.from_user.id in admins or message.from_user.id in admin:
      				if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      					chat_id = message.chat.id
      					if message.reply_to_message:
      						wlc_message[chat_id] = message.reply_to_message.text
      						message.reply_text('پیام خوش آمد برای گروه شما با تنظیم فعال شد')
      						write_file(wlc_message,'welcome.json')
      				else:
      					message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      	except:
      				pass
      	sleep(2)
      	dast.remove(message.from_user.id)
      				

@app.on_message(filters.new_chat_members)
def wlc(client,message):
    chat_id = message.chat.id
    try:
        if message.chat.id in wlc_list:
            try:
                message.reply_text(f'{wlc_message[chat_id]}')
            except KeyError:
                return
    except KeyError:
        return
        
@app.on_message(filters.command(["welcome_on",f"welcome_on{bot_user}"]) & filters.group)
def wlcon(clientt,message):
  if len(message.command) == 1 and message.from_user.id not in dast:
      dast.append(message.from_user.id)
      try:
      			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      			if message.from_user.id in admins or message.from_user.id in admin:
      				if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      					chat_id = message.chat.id
      					if message.chat.id not in wlc_list:
      						wlc_list.append(chat_id)
      						message.reply_text('پیام خوش آمد شما با موفیقت روشن شد')
      					else:
      						     message.reply_text('پیام خوش آمد گروه از ابتدا هم فعال بوده')
      				else:
      					message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      				pass
      sleep(2)
      dast.remove(message.from_user.id)
    
@app.on_message(filters.command(["welcome_off",f"welcome_off{bot_user}"]) & filters.group)
def wlcof(clientt,message):
  if len(message.command) == 1and message.from_user.id not in dast:
      dast.append(message.from_user.id)
      try:
      			admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
      			if message.from_user.id in admins or message.from_user.id in admin:
      				if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
      					chat_id = message.chat.id
      					if message.chat.id in wlc_list:
      						wlc_list.remove(chat_id)
      						message.reply_text('پیام خوش آمد شما با موفیقت خاموش شد')
      					else:
      						     message.reply_text('پیام خوش‌آمد گروه از ابتدا غیر فعال بوده است')
      				else:
      					message.reply('لطفا اول ربات را استارت کنید و دوباره امتحان کنید')
      except:
      	pass
      sleep(2)
      dast.remove(message.from_user.id)
      				
 

@app.on_message(filters.command(['settime', f'settime{bot_user}']) & filters.group)
def settime(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group:
    dast.append(message.from_user.id)
    try:
    	if len(message.command) == 2:
    	   admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    	   if message.from_user.id in admins or message.from_user.id in admin:
  	     	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	     	  if int(message.command[1]) > 1 and int(message.command[1]) < 300:
  	     	  	time_sleep[str(message.chat.id)] = int(message.command[1])
  	     	  	message.reply(f'زمان استراحت بین پیام به {message.command[1]} تغییر کرد')
  	     	  else:
  	     	  	message.reply(f'زمان استراحت بین پیام باید عددی بین 2 تا 300 باشد')
  	     	else:
  	     		message.reply('لطفا اول ربات را استارت کنید بعد دوباره تست کنید')
    except:
  	 	pass
    sleep(1.5)
    dast.remove(message.from_user.id)


@app.on_message(filters.command(['setlang', f'setlang{bot_user}']) & filters.group)
def settime(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group:
    dast.append(message.from_user.id)
    try:
    	if len(message.command) == 2:
    	   admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    	   if message.from_user.id in admins or message.from_user.id in admin:
  	     	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	     	  if message.command[1] in ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']:
  	     	  	lang[str(message.chat.id)] = message.command[1]
  	     	  	write_file(lang,'lang.json')
  	     	  	message.reply(f'زبان ربات با موفیقت به {message.command[1]} تغییر کرد')
  	     	  else:
  	     	  	message.reply(f'زبان مورد نظر اشتباه است')
  	     	else:
  	     		message.reply('لطفا اول ربات را استارت کنید بعد دوباره تست کنید')
    except:
  	 	pass
    sleep(1.5)
    dast.remove(message.from_user.id)
    
@app.on_message(filters.command(['delword', f'delword{bot_user}']) & filters.group)
def delword(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group:
    dast.append(message.from_user.id)
    try:
    	if len(message.command) == 2:
    	   admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
    	   if message.from_user.id in admin or message.from_user.id in admins:
    	   	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	     		bh = open(f'text{message.chat.id}.txt', 'r')
  	     		h = bh.read()
  	     		bj = open(f'text{message.chat.id}.txt', 'w+')
  	     		c = []
  	     		hld = ''
  	     		for i in h.split():
  	     			c.append(i)
  	     		try:
  	     			c.remove(message.command[1])
  	     		except:
  	     			pass
  	     		message.reply(f'کلمه {message.command[1]} با موفیقت حذف شد')
  	     		for i in c:
  	     			hld = hld + '\n' + i
  	     		bj.write(hld)
  	     	else:
  	     		message.reply('لطفا اول ربات را استارت کنید بعد دوباره تست کنید')
    except:
    	pass
    sleep(1.5)
    dast.remove(message.from_user.id)

@app.on_message(filters.command(['delsticker', f'delsticker{bot_user}']) & filters.group)
def delsticker(client, message):
  if message.from_user.id not in dast and message.chat.id in (vip_group) and len(message.command) == 1 and message.reply_to_message.sticker:
  	 dast.append(message.from_user.id)
  	 try:
  	     admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  	     if message.from_user.id in admins or message.from_user.id in admin:
  	     	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	     		bh = open(f'sticker{message.chat.id}.txt', 'r')
  	     		h = bh.read()
  	     		bj = open(f'sticker{message.chat.id}.txt', 'w+')
  	     		c = []
  	     		hld = ''
  	     		for i in h.split():
  	     			c.append(i)
  	     		try:
  	     			c.remove(message.reply_to_message.sticker.file_id)
  	     		except:
  	     			pass
  	     		message.reply(f'استیکر مورد نظر دیگر در لیست استیکر ها موجود نیست')
  	     		for i in c:
  	     			hld = hld + '\n' + i
  	     		bj.write(hld)
  	     	else:
  	     			message.reply('لطفا اول ربات را استارت کنید بعد دوباره تست کنید')
  	 except:
  	 	pass
  	 sleep(1.5)
  	 dast.remove(message.from_user.id)

@app.on_message(filters.command(['delgif', f'delgif{bot_user}']) & filters.group)
def delgif(client, message):
  if message.from_user.id not in dast and message.chat.id in vip_group and len(message.command) == 1 and message.reply_to_message.animation:
   dast.append(message.from_user.id)
   try:
  	 admins = [i.user.id for i in app.get_chat_members(
      	    message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
  	 if message.from_user.id in admins or message.from_user.id in admin:
  	 	if message.from_user.id in member and app.get_users(message.from_user.id).status != UserStatus.LONG_AGO:
  	 	 bh = open(f'gif{message.chat.id}.txt', 'r')
  	 	 h = bh.read()
  	 	 bj = open(f'gif{message.chat.id}.txt', 'w+')
  	 	 c = []
  	 	 hld = ''
  	 	 for i in h.split():
  	 	  			c.append(i)
  	 	 try:
  	 	 	c.remove(message.reply_to_message.animation.file_id)
  	 	 except:
  	 	 	pass
  	 	 message.reply('گیف مورد نظر دیگر موجود نمی باشد')
  	 	 for i in c:
  	 	 	hld = hld + '\n' + i
  	 	 bj.write(hld)
  	 	else:
  	 		message.reply('لطفا اول ربات را استارت کنید بعد دوباره تست کنید')
   except:
    	pass
   sleep(1.5)
   dast.remove(message.from_user.id)
  	 	    
@app.on_message(filters.command('block') & filters.group)
def block_group_77(client,message):
  	if len(message.command) == 2 and message.chat.id == sodo:
  		if message.chat.id not in block_group:
  			block_group.append(int(message.command[1]))
  			fh = open(f'blocklist.txt', 'w')
  			bh = open(f'blocklist.txt', 'r')
  			h = bh.read()
  			b = ''
  			for i in block_group:
  				b = b + '\n' + str(i)
  			fh.write(b)
  			fh.close()
  			app.leave_chat(int(message.command[1]))
  	elif len(message.command) == 1 and message.from_user.id in admin:
  		if message.chat.id not in block_group:
  			block_group.append(message.chat.id)
  			fhjd = open(f'blocklist.txt', 'w')
  			bhjd = open(f'blocklist.txt', 'r')
  			h = bhjd.read()
  			b = ''
  			for i in block_group:
  				b = b + '\n' + str(i)
  			fhjd.write(b)
  			fhjd.close()
  		app.leave_chat(message.chat.id)
  			
@app.on_message(filters.command('unblock') & filters.chat(sodo))
def unblock_group_77(client,message):
  	if len(message.command) == 2:
  		if int(message.command[1]) in block_group:
  			block_group.remove(int(message.command[1]))
  			fhif = open(f'blocklist.txt', 'w')
  			bhif = open(f'blocklist.txt', 'r')
  			h = bhif.read()
  			b = ''
  			for i in block_group:
  				b = b + '\n' + str(i)
  			fhif.write(b)
  			fhif.close()

@app.on_message(filters.new_chat_members,group=3)
def left_group_block(client,message):
    chat_id = message.chat.id
    try:
        if message.chat.id in block_group:
        	app.leave_chat(message.chat.id)        	
    except:
    	pass
    
 
dick = read_file('najva.json')
@app.on_inline_query()
async def answer(client, inline_query):
	dick['count'] += 1
	msg = ''
	for i in inline_query.query.split()[1:]:
		msg = msg + ' ' + i
	if len(msg) > 1:
		lname = inline_query.query.split()[0]
		if '+' not in inline_query.query.split()[0]:
			dick[str(dick['count'])] = [[str(inline_query.from_user.id),inline_query.query.split()[0]],msg]
			text = 'najva' + ' ' + str(dick['count'])
			write_file(dick,'najva.json')
			title = inline_query.query.split()[0]
		else:
			dick[str(dick['count'])] = [inline_query.query.split()[0].split('+'),msg]
			dick[str(dick['count'])][0].append(str(inline_query.from_user.id))
			text = 'najva' + ' ' + str(dick['count'])
			write_file(dick)
			title = inline_query.query.split()[0].split('+')[0]
			for i in inline_query.query.split()[0].split('+')[1:]:
				title = title + ' ' + 'و' + ' ' + i
		if lname.startswith('@'):
				await app.answer_inline_query(
		inline_query.id,
		results=[
            InlineQueryResultArticle(
                title=f"ارسال نجوا به {title}",
                input_message_content=InputTextMessageContent(f'''یک نجوا به {title}، فقط ایشان می‌تواند آن را باز کند.
                
@Cleverpandabot'''
                ),
                description='فقط ایشان می تواند آن را باز کند'
,reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "نمایش پیام",
                            callback_data= text
                        )]
                    ]
                )
            )])
		elif lname.isdigit():
			try:
				texty = app.get_users(inline_query.query.split()[0]).firstname
			except:
				texty = inline_query.query.split()[0]
			matn =f'<a herf="tg://user?id={inline_query.query.split()[0]}">{texty}</a>'
			await app.answer_inline_query(
		inline_query.id,
		results=[
            InlineQueryResultArticle(
                title=f"ارسال نجوا به {inline_query.query.split()[0]}",
                input_message_content=InputTextMessageContent(f'''یک نجوا به {matn}، فقط ایشان می‌تواند آن را باز کند.

@Cleverpandabot'''
               
                ),
                description='فقط ایشان می تواند آن را باز کند'
,reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "نمایش پیام",
                            callback_data= text
                        )]
                    ]
                )
            )])
		else:
						await app.answer_inline_query(
		inline_query.id,
		results=[
            InlineQueryResultArticle(
                title=f"نحوه ارسال نجوا",
                input_message_content=InputTextMessageContent(f'''قالب ارسال نجوا باید این گونه باشد
آیدی ربات + آیدی فرد + متن نجوا'''
                ),
                description='''قالب ارسال نجوا باید این گونه باشد
آیدی ربات + آیدی فرد + متن نجوا'''
                        )])

@app.on_callback_query(filters.regex('^najva'))
async def upppppp(client,qurey):
	   text = qurey.data.split()
	   if str(qurey.from_user.id) in dick[text[1]][0] or f'@{qurey.from_user.username}' in dick[text[1]][0]:
	   	await app.answer_callback_query(qurey.id, text=dick[text[1]][1], show_alert=True)

bot.start()
app.run()