import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# خادم ويب وهمي للرد على طلبات UptimeRobot وإبقاء البوت مستيقظاً
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

# تشغيل خادم الويب في خلفية البرنامج لكي لا يعطل عمل البوت
t = threading.Thread(target=run_server)
t.daemon = True
t.start()

# --- (وهنا تضع الكود الأصلي لبوتك ليعمل بشكل طبيعي) ---
import requests , os  , sys , os , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say
import asyncio
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

OPEN_ID = "a39b437a6625085647115c08a72a9921"
ACCESS_TOKEN = "b3b56072c2b5b0df142991633646e5cfdd07381f3eac915354bc72c2715cdf39"
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
evo_cycle_running = False
evo_cycle_task = None

EVO_IDS = [
    909000063, 909000075, 909040010, 909000081, 909039011, 
    909045001, 909038012, 909042008, 909051003, 909035012, 
    909000098, 909033002, 909037011, 909049010, 909041005, 
    909038010, 909033001, 909035007, 909000090, 909000085, 
    909000068
]

LIKE_LIMIT_FILE = "like_limit.json"

if os.path.exists(LIKE_LIMIT_FILE):
    with open(LIKE_LIMIT_FILE, "r") as f:
        like_limit = json.load(f)
else:
    like_limit = {}

admin_uid = "3811627244"

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB54"}

def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 8
    major_login.client_version = "1.126.2"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "8"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 8
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 102000007
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2025060100"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 8
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "8"
    major_login.primary_platform_type = "8"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggpolarbear.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 
           
async def evo_gun_cycle(uids, evo_ids_list, key, iv, region):
    global evo_cycle_running, whisper_writer, online_writer
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Bắt đầu vòng lặp Evo Gun số #{cycle_count}")
        
        for emote_id in evo_ids_list:
            if not evo_cycle_running:
                break
                
            print(f"Đang gửi Evo Emote ID: {emote_id}")
            
            for uid_str in uids:
                try:
                    uid_int = int(uid_str)
                    H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                except Exception as e:
                    print(f"Lỗi gửi emote {emote_id} tới {uid_str}: {e}")
            if evo_cycle_running:
                for i in range(5):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
        
        if evo_cycle_running:
            print("Đã xong 1 vòng 21 khẩu. Chờ 2 giây rồi lặp lại...")
            await asyncio.sleep(2)
    
    print("Đã dừng vòng lặp Evo.")

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)

                        message = f'@a 13513476553 909047001'
                        P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                    except:
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)

                                message = f'Cool outfit!'
                                P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            except:
                                pass

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room, whisper_writer, spammer_uid, spam_chat_id, spam_uid, online_writer, chat_id, XX, uid, Spy, data2, Chat_Leave, evo_cycle_running, evo_cycle_task
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break  
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None

                    if response:
                        if inPuTMsG.startswith("/6"):
                            try:
                                uid = response.Data.uid
                                chat_id = response.Data.Chat_ID
                                chat_type = response.Data.chat_type
                                message = f"[B][C]{get_random_color()}\n\nVui lòng chấp nhận lời mời của tôi trong 3s!!\n\n"
                                P = await SEndMsG(chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                leave_pkt = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                await asyncio.sleep(0.5)
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                C = await cHSq(6, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                V = await SEnd_InV(6, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                await asyncio.sleep(3.5)
                                E = await ExiT(None, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)

                            except Exception as e:
                                print(f"Creating team 6: {e}")

                        if inPuTMsG.startswith("/5"):
                            try:
                                uid = response.Data.uid
                                chat_id = response.Data.Chat_ID
                                chat_type = response.Data.chat_type
                                message = f"[B][C]{get_random_color()}\n\nVui lòng chấp nhận lời mời của tôi trong 3s!!\n\n"
                                P = await SEndMsG(chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                leave_pkt = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                await asyncio.sleep(0.5)
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                C = await cHSq(5, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                V = await SEnd_InV(5, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                await asyncio.sleep(3.5)
                                E = await ExiT(None, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)

                            except Exception as e:
                                print(f"Creating team 5: {e}")

                        if inPuTMsG.startswith("/4"):
                            try:
                                uid = response.Data.uid
                                chat_id = response.Data.Chat_ID
                                chat_type = response.Data.chat_type
                                message = f"[B][C]{get_random_color()}\n\nVui lòng chấp nhận lời mời của tôi trong 3s!!\n\n"
                                P = await SEndMsG(chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                leave_pkt = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                await asyncio.sleep(0.5)
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                C = await cHSq(4, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                V = await SEnd_InV(4, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                await asyncio.sleep(3.5)
                                E = await ExiT(None, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)

                            except Exception as e:
                                print(f"Creating  team 4: {e}")

                        if inPuTMsG.startswith("/3"):
                            try:
                                uid = response.Data.uid
                                chat_id = response.Data.Chat_ID
                                chat_type = response.Data.chat_type
                                message = f"[B][C]{get_random_color()}\n\nVui lòng chấp nhận lời mời của tôi trong 3s!!\n\n"
                                P = await SEndMsG(chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                leave_pkt = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                await asyncio.sleep(0.5)
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                C = await cHSq(3, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                V = await SEnd_InV(3, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                await asyncio.sleep(3.5)
                                E = await ExiT(None, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)

                            except Exception as e:
                                print(f"Lỗi khi thực hiện lệnh team 3: {e}")

                        if inPuTMsG.startswith("/2"):
                            try:
                                uid = response.Data.uid
                                chat_id = response.Data.Chat_ID
                                chat_type = response.Data.chat_type
                                message = f"[B][C]{get_random_color()}\n\nVui lòng chấp nhận lời mời của tôi trong 3s!!\n\n"
                                P = await SEndMsG(chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                leave_pkt = await ExiT(uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                await asyncio.sleep(0.5)
                                PAc = await OpEnSq(key, iv, region)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                C = await cHSq(2, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                V = await SEnd_InV(2, uid, key, iv, region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                await asyncio.sleep(3.5)
                                E = await ExiT(None, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)

                            except Exception as e:
                                print(f"Lỗi khi thực hiện lệnh team 2: {e}")

                        if inPuTMsG.strip().startswith('/evos'):
                            try:
                                dd = chatdata['5']['data']['16']
                                message = f"[B][C]{get_random_color()}\n\nLệnh này chỉ hoạt động trong đội! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            except:
                                print('Processing evo cycle start command for evos in team')
                                parts = inPuTMsG.strip().split()
                                uids = [str(response.Data.uid)]
                                if len(parts) > 1:
                                    for part in parts[1:]:
                                        if part.isdigit() and len(part) >= 7:
                                            uids.append(part)
                                if evo_cycle_task and not evo_cycle_task.done():
                                    evo_cycle_running = False
                                    evo_cycle_task.cancel()
                                    await asyncio.sleep(0.5)
                                evo_cycle_running = True
                                evo_cycle_task = asyncio.create_task(evo_gun_cycle(uids, EVO_IDS, key, iv, region))
                                success_msg = f"[B][C]{get_random_color()}\n\n✅ Đã kích hoạt Evo Cycle\n\n"
                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        if inPuTMsG.strip() == '/sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C]{get_random_color()}\n\n✅ Đã dừng Evo Cycle thành công\n\n"
                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C]{get_random_color()}\n\n❌ Không có Evo Cycle nào đang chạy\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        if inPuTMsG.startswith('/spm '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()

                                api_response = requests.get(
                                    f"http://fr2.spaceify.eu:25680/spam_vip?uid={target_uid}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("status") == "started":
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"
                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        if inPuTMsG.startswith('/stp '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()
                                api_response = requests.get(
                                    f"http://fr2.spaceify.eu:25680/stop?uid={target_uid}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("status") == "stopped":
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        if inPuTMsG.startswith('/spm '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()
                                api_response = requests.get(
                                    f"https://hosting-xlonely-up.verecel.com/proxy/50010/spam?user_id={target_uid}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("status") == "success":
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)  
                                
                        if inPuTMsG.startswith('/stop '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()
                                api_response = requests.get(
                                    f"https://hosting-xlonely-up.verecel.com/proxy/50010/spam?user_id={target_uid}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("status") == "success":
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)  
                        
                        if inPuTMsG.startswith('/ghost '):
                            try:
                                args = inPuTMsG.split(' ', 2)
                                teamcode = args[1].strip()
                                name = args[2].strip()

                                api_response = requests.get(
                                    f"http://45.58.37.229:8017/api/ghost?teamcode={teamcode}&name={name}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("success") == True:
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                        if inPuTMsG.startswith('/lag '):
                            try:
                                args = inPuTMsG.split(' ', 2)
                                teamcode = args[1].strip()
                                name = args[2].strip()
                                api_response = requests.get(
                                    f"http://45.58.37.229:8017/api/ghost_attack?teamcode={teamcode}&name={name}",
                                    timeout=30)
                                data = api_response.json()
                                if data.get("success") == True:
                                    success_msg = f"[B][C]{get_random_color()}\n\nDoNe\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                        if inPuTMsG.startswith('/visit '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()
                                api_response = requests.get(
                                    f"https://ctx-team.duckdns.org/api/proxy/visits?uid={target_uid}",
                                    timeout=1)
                                data = api_response.json()
                                if data.get("status") == "success":
                                    success_msg = f"[B][C]{get_random_color()}\n\nSuccessfully sent {data.get('successful_visits', 0)} visits\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed to send visits.\n\n"
                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                        if inPuTMsG.startswith('/like '):
                            try:
                                target_uid = inPuTMsG.split(' ', 1)[1].strip()
                                today = datetime.now().strftime("%Y-%m-%d")

                                if str(uid) != admin_uid:
                                    if like_limit.get(str(uid)) == today:
                                        error_msg = f"[B][C]{get_random_color()}\n\nYou have already used your daily like.\n\n"
                                        P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                        continue
                                        
                                api_response = requests.get(
                                    f"https://lonelyprime-api-likes-production.up.railway.app/like?uid={target_uid}",
                                    timeout=10)
                                data = api_response.json()
                                if data.get("status") == 1:
                                    if str(uid) != admin_uid:
                                        like_limit[str(uid)] = today
                                        with open(LIKE_LIMIT_FILE, "w") as f:
                                            json.dump(like_limit, f)

                                    success_msg = f"[B][C]{get_random_color()}\n\nSuccessfully sent {data.get('LikesGivenByAPI', 0)} likes\n\n"
                                else:
                                    success_msg = f"[B][C]{get_random_color()}\n\nFailed\n\n"

                                P = await SEndMsG(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                            except Exception as e:
                                error_msg = f"[B][C]{get_random_color()}\n\n{str(e)}\n\n"
                                P = await SEndMsG(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                                
                        if inPuTMsG.startswith('/join '):
                            CodE = inPuTMsG.split('/join ')[1]
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                EM = await GenJoinSquadsPacket(CodE , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                                success_msg = f"[B][C]{get_random_color()}\n\nJoined The Squad\n\n"
                                P = await SEndMsG(response.Data.chat_type , success_msg , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                            except:
                                print('msg in squad')
                        
                            
                        if inPuTMsG.startswith('/exit'):
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            success_msg = f"[B][C]{get_random_color()}\n\nLeave The Squad\n\n"
                            P = await SEndMsG(response.Data.chat_type , success_msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                        if inPuTMsG.strip().startswith('/s'):
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)

                        if inPuTMsG.strip().startswith('/a'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nCommand Available OnLy In Team Chat Section! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except:
                                print('msg in Team')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'122809569'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    idT = int(parts[5])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                        H = await Emote_k(uid, idT, key, iv,region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                        if uid2:
                                            H = await Emote_k(uid2, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid3:
                                            H = await Emote_k(uid3, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid4:
                                            H = await Emote_k(uid4, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid5:
                                            H = await Emote_k(uid5, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        

                                    except Exception as e:
                                        pass
                                        
                        if inPuTMsG in ("/"):
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            msg1 = f"""
[b][c]{get_random_color()} عبود BOT 

[b][c]{get_random_color()}Fast • Powerful • Easy to Use

[b][c]{get_random_color()}Send
[b][c][FFFFFF]/help

[b][c]{get_random_color()} مو شكرا لأستخدام بوتي

[b][c][FFFFFF]Version 1.0
"""
                            P = await SEndMsG(response.Data.chat_type , msg1 , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                           
                        
                        if inPuTMsG.strip() == "/admin":
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            msg = f"""
[b][c]{get_random_color()} Welcome to عبوده BoT 

[b][c]{get_random_color()}لاتخربو البوت لأشلع عيونكم

[b][c]{get_random_color()}━━━━━━━━━━━━━━

[b][c]{get_random_color()} Developer

[b][c][FFFFFF]عبوده BoT 

[b][c]{get_random_color()} instagram

[b][c][FFFFFF]@hhi6

[b][c]{get_random_color()} مو شكرا لاستخدام بوتي
"""
                            P = await SEndMsG(response.Data.chat_type , msg , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            
                        if inPuTMsG.strip() == "/help":
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID

                            msg1 = f"""
[b][c]{get_random_color()}إنشاء سكواد 

[b][c][FFFFFF] --> /3 , /5 , /6 

[b][c]{get_random_color()} - ارسال سبام روم بدون توقف 

[b][c][FFFFFF] --> /spam <uid> 

[b][c]{get_random_color()} - ايقاف سبام روم

[b][c][FFFFFF] --> /stop <uid> 

[b][c]{get_random_color()} - ارسال زوار عبر ايدي

[b][c][FFFFFF] --> /visit <uid> 

[b][c]{get_random_color()} - معلومات مطور

[b][c][FFFFFF] --> /admin
"""

                            msg2 = f"""

[b][c]{get_random_color()} - مغادرة السكواد

[b][c][FFFFFF] --> /exit

[b][c]{get_random_color()} - ارسال لايكات

[b][c][FFFFFF] --> /like <uid>

[b][c]{get_random_color()} - وضع اللاعب بالمقبرة

[b][c][FFFFFF] --> /spm <uid>

[b][c]{get_random_color()} - حذف اللاعب من المقبرة

[b][c][FFFFFF] --> /stp <uid>

[b][c]{get_random_color()} ارسال اشباح 

[b][c][FFFFFF] --> /ghost  <code> <name>

[b][c]{get_random_color()} - تدمير السكواد عبر تيم كود

[b][c][FFFFFF] --> /lag <code> <name> 
"""

                            P = await SEndMsG(response.Data.chat_type , msg1 , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                            await asyncio.sleep(0.3)

                            P = await SEndMsG(response.Data.chat_type , msg2 , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                        response = None
                          
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"Lỗi - {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    open_id = OPEN_ID
    access_token = ACCESS_TOKEN
    
    if not open_id or not access_token:
        print("[-] No token provided in main.py!")
        return None

    print(f"\n[*] Starting connection...")

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print("[-] MajorLogin Failed! Token expired or invalid!")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    region = MajoRLoGinauTh.region
    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    LoGinDaTa = await GetLoginData(UrL , PyL , ToKen)
    if not LoGinDaTa: print("Lỗi - Không lấy được cổng (Port) từ dữ liệu đăng nhập!") ; return None
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP , OnLineporT = OnLinePorTs.split(":")
    ChaTiP , ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(ToKen)
    equie_emote(ToKen,UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT) , ToKen , int(timestamp) , key , iv)
    ready_event = asyncio.Event()
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT , AutHToKen , key , iv , LoGinDaTaUncRypTinG , ready_event ,region))
     
    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP , OnLineporT , key , iv , AutHToKen))
    print(render('TCP', colors=['white', 'green'], align='center'))
    print('')
    print(f" - Khu vực => {region}".format(region))
    print(f" - Bot đang online, id bot: {TarGeT} | Tên bot : {acc_name}\n")
    print(f" - Bot by | PLong TCP ! (:")        
    await asyncio.gather(task1 , task2)
    
async def StarTinG():
    while True:
        try: await asyncio.wait_for(MaiiiinE() , timeout = 7 * 60 * 60)
        except asyncio.TimeoutError: print("Token hết hạn !, Đang khởi động lại ...")
        except Exception as e: print(f"Lỗi - {e} => Đang khởi động lại ...")

if __name__ == '__main__':
    asyncio.run(StarTinG())
