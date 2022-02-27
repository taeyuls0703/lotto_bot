import asyncio
import random
import time
import hikari
import lightbulb
import lottery, lotto_regen
import openpyxl
bot = lightbulb.BotApp(
    token="OTQ0MjIwNjE2MTAwMzAyODc5.Yg-b-Q.ezBXVXC_ssjMFhGssMQ1dUFNUT4"
)
color = "93DAFF  98DFFF  9DE4FF  A2E9FF  A7EEFF  ACF3FF  B0F7FF  B4FBFF  B9FFFF  C0FFFF  87CEFA  91D8FA  A5D8FA  AFDDFA  B9E2FA  C3E7FA  CDECFA  D7F1FA  E1F6FA  EBFBFF  00BFFF  0AC9FF  14D3FF  1EDDFF  28E7FF  32F1FF  3CFBFF  46FFFF  96FFFF  C8FFFF  00A5FF  00AFFF  00B9FF  00C3FF  00CDFF  00D7FF  00E1FF  00EBFF  00F5FF  00FFFF  1EA4FF  28AEFF  32B8FF  3CC2FF  46CCFF  50D6FF  5AE0FF  6EE0FF  6EEAFF  78F3FF  1E90FF  289AFF  32A4FF  3CAEFF  46B8FF  50C2FF  5ACCFF  64D6FF  6EE0FF  78EAFF  96A5FF  A0AFFF  AAB9FF  B4C3FF  BECDFF  C8D7FF  D2E1FF  DCEBFF  E8F5FF  F4FFFF  86A5FF  90AFFF  9AB9FF  A4C3FF  AECDFF  B8D7FF  CCE1FF  E0EBFF  EBF5FF  F9FFFF  6495ED  6E9FED  78A9ED  82B3ED  8CBDED  96C7ED  A0D1F7  AADBFF  B4E5FF  BEEFFF  0078FF  0A82FF  148CFF  1E96FF  28A0FF  32AAFF  3CB4FF  46BEFF  50C8FF  5AD2FF  0064FF  0A6EFF  1478FF  1E82FF  288CFF  3296FF  3CA0FF  46AAFF  50B4FF  5ABEFF  0000FF  3232FF  5050FF  646EFF  6478FF  6482FF  648CFF  6496FF  64A0FF  64AAFF  4169E1  4B73E1  557DE1  5F87E1  6991E1  739BE1  7DA5E1  87AFEB  91B9F5  9BC3FF  0064CD  0A6ECD  1478CD  1E82CD  288CD2  3296D7  3CA0E1  46AAEB  50B4F5  5ABEF5  5A5AFF  6464FF  6E6EFF  7878FF  8282FF  8C8CFF  A0A0FF  B4B4FF  C8C8FF  D2D2FF  7B68EE  8572EE  8F7CEE  9986EE  A390EE  AD9AEE  B7A4EE  C1AEEE  CBB8EE  D5C2EE  6A5ACD  7E6ECD  8878CD  9282CD  9C8CCD  A696CD  B0A0CD  BAAAD7  C4B4E1  CEBEE1  0000CD  2828CD  4646CD  6464CD  6E6ED7  7878E1  8282EB  8C8CF5  9696FF  A0A0FF  00008C  14148C  28288C  3C3C8C  50508C  646496  7878AA  8C8CBE  A0A0C8  B4B4DC  483D8B  52478B  5C518B  665B8B  70658B  7A6F95  84799F  8E83A9  988DB3  A297BD  000069  1E3269  323C73  3C467D  3C5087  3C5A91  46649B  506EA5  5A78AF  6482B9  3DFF92  47FF9C  51FFA6  5BFFB0  65FFBA  6FFFC4  79FFCE  75FFCA  7AFFCF  7FFFD4  55EE94  5FEE9E  69EEA8  73EEB2  7DEEBC  87EEC6  91F8D0  9BFFDA  A5FFE4  AFFFEE  66CDAA  70D2B4  7AD7BE  84DCC8  8EE1D2  98EBDC  9DF0E1  A2F5E6  A7FAEB  ACFFEF  AAEBAA  B4F0B4  BEF5BE  C8FAC8  D2FFD2  DCFFDC  E1FFE1  E6FFE6  EBFFEB  F0FFF0  80E12A  8AE634  94EB3E  9EF048  A8F552  B2FA5C  BCFF66  C1FF6B  C6FF70  CBFF75  52E252  5CE75C  66EC66  70F170  7AF67A  84FB84  89FB89  8EFB8E  93FB93  98FB98  64CD3C  6ED746  78E150  82EB5A  8CF064  96F56E  9BFA73  A0FA78  A5FA7D  AAFA82  13C7A3  18CCA8  1DD1AD  22D6B2  27DBB7  2CE0BC  31E0C1  36E0C6  3BE0CB  40E0D0  46B4B4  50BEBE  5AC8C8  64D2D2  6EDCDC  73E1E1  78E6E6  7DEBEB  82F0F0  87F5F5  20B2AA  2ABCB4  34C6BE  3ED0C8  48DAD2  52E4DC  57E9E1  5CEEE6  61F3EB  66F8F0  5F9EA0  69A8AA  73B2B4  7DBCBE  87C6C8  91D0D2  96D5D7  9BDADC  A0DFE1  A5E3E6  3CB371  46BD7B  50C785  5AD18F  64DB99  6EE5A3  73EAA8  78EFAD  7DF4B2  82F9B7  2E8B57  389561  429F6B  4CA975  56B37F  60BD89  65C28E  6AC793  6FCC98  74D19D  228B22  2C952C  369F36  40A940  4AB34A  54BD54  5EC75E  63CC63  68D168  6DD66D  497649  538053  5D8A5D  679467  719E71  7BA87B  80AD80  85B285  8AB78A  8FBC8F  006400  0A6E0A  147814  1E821E  288C28  329632  3CA03C  41A541  46AA46  4BAF4B  008C8C  0A9696  14A0A0  1EAAAA  28B4B4  32BEBE  37C3C3  3CC8C8  41CDCD  46D2D2  008080  0A8A8A  149494  1E9E9E  28A8A8  32B2B2  37B7B7  3CBCBC  41C1C1  46C6C6  FFB6C1  FFBBC6  FFC0CB  FFC5D0  FFCAD5  FFCFDA  FFD4DF  FFD9E4  FFDEE9  FFE3EE  FFAAAF  FFB4B9  FFBEC3  FFC8CD  FFD2D7  FFDCE1  FFE1E6  FFE6EB  FFEBF0  FFF0F5  FF9E9B  FFA8A5  FFB2AF  FFBCB9  FFC6C3  FFD0CD  FFD5D2  FFDAD7  FFDFDC  FFE4E1  FF7A85  FF848F  FF8E99  FF98A3  FFA2AD  FFACB7  FFB1BC  FFB6C1  FFBBC6  FFC0CB  FF5675  FF607F  FF6A89  FF7493  FF7E9D  FF88A7  FF92B1  FF9CBB  FFA6C5  FFB0CF  FF82FF  FF8CFF  FF96FF  FFA0FF  FFAAFF  FFB4FF  FFBEFF  FFC8FF  FFD2FF  FFDCFF  FF7DB4  FF87BE  FF91C8  FF9BD2  FFA5DC  FFAFE6  FFB4EB  FFB9F0  FFBEF5  FFC3FA  FF69B4  FF73BE  FF7DC8  FF87D2  FF91DC  FF9BE6  FFA5F0  FFAAF5  FFAFFA  FFB4FF  FF1493  FF1E9D  FF28A7  FF32B1  FF3CBB  FF46C5  FF50CF  FF5AD9  FF64E3  FF6EED  DB7093  DB7A9D  DB84A7  E08EB1  E598BB  EAA2C5  EAB1D4  EFACCF  F4BBDE  F4B6D9  D7567F  DC6089  E16A93  E6749D  EB7EA7  F088B1  F592BB  FA9CC5  FFA6CF  FFB0D9  C71585  C71F8F  C73399  C73DA3  CC47AD  D151B7  D65BC1  E065CB  EA6FD5  F479DF  CD1039  CD1F48  CD2E57  CD3861  CD426B  D24C75  D7567F  DC6089  E16A93  E6749D  B9062F  B91A4D  BE2457  C32E61  C8386B  CD4275  D24C7F  D75689  DC6093  E16A9D  FAEB78  FAF082  FAF58C  FAFA96  FAFAA0  FAFAAA  FAFAB4  FAFABE  FAFAD2  FAFAD2  FFDC3C  FFE146  FFE650  FFEB5A  FFF064  FFF56E  FFFA78  FFFA82  FFFF8C  FFFF96  FFC81E  FFD228  FFD732  FFDC3C  FFE146  FFE650  FFEB5A  FFF064  FFF56E  FFF978  FFB400  FFBE0A  FFC314  FFC81E  FFCD28  FFD232  FFD73C  FFDC46  FFE150  FFE65A  FDCD8C  FDD296  FDD7A0  FDDCAA  FDE1B4  FDE6BE  FDEBC8  FDF5D2  FDF5DC  FDF5E6  FAC87D  FACD87  FAD291  FAD79B  FADCA5  FAE1AF  FAE6B9  FAEBC3  FAEBCD  FAEBD7  FFA500  FFAF0A  FFB914  FFC31E  FFCD28  FFD732  FFDC37  FFE13C  FFE641  FFEB46  FF9100  FF9B00  FFA500  FFAF00  FFB900  FFC300  FFC800  FFCD00  FFD200  FFD700  FF8200  FF8C0A  FF9614  FFA01E  FFAA28  FFB432  FFB937  FFBE3C  FFC341  FFC846  FFA98F  FFB399  FFBDA3  FFC7AD  FFD1B7  FFDBC1  FFE0C6  FFE5CB  FFEAD0  FFEFD5  FFA374  FFAD7E  FFB788  FFC192  FFCB9C  FFD0A1  FFD5A6  FFDAAB  FFDFB0  FFE4B5  FF9473  FF9E7D  FFA887  FFB291  FFBC9B  FFC6A5  FFD0AF  FFD0AF  FFD5B4  FFDAB9  FF7F50  FF895A  FF9364  FF9D6E  FFA778  FFB182  FFBB8C  FFC091  FFC596  FFCA9B  CD853F  CD8F49  D29953  D7A35D  DCAD67  E1B771  E6C17B  EBC680  F0CB85  F5D08A  D2691E  D27328  D27D32  D7873C  DC9146  E19B50  E6A55A  EBAA5F  EBAF64  F0B469  AE5E1A  B86824  C2722E  CC7C38  D68642  E0904C  E59551  EA9A56  EF9F5B  F4A460  8B4513  8B4F1D  8B5927  8B6331  906D3B  957745  9F814F  A48654  A98B59  AE905E  FF9696  FFA0A0  FFAAAA  FFB4B4  FFBEBE  FFC8C8  FFD2D2  FFDCDC  FFE6E6  FFF0F0  F08080  F08A8A  F09494  F59E9E  FAA8A8  FAB2B2  FAB7B7  FABCBC  FAC1C1  FAC6C6  F56E6E  F57878  F58282  F58C8C  F59696  F5A0A0  F5AAAA  FAB4B4  FABEBE  FAC8C8  F06464  F06E6E  F07878  F08282  F08C8C  F09696  F4A0A0  F4AAAA  F4B4B4  FEBEBE  FF0000  FF3232  FF4646  FF5050  FF5A5A  FF6464  FF6E6E  FF7878  FF8282  FF8C8C  EB0000  EB3232  EB4646  EB5050  EB5A5A  EB6464  F06E6E  F57878  FA8282  FA8C8C  CD0000  CD3C3C  CD4646  CD5050  D25A5A  D76464  DC6E6E  E17878  E68282  EB8C8C  CD5C5C  CD6666  CD7070  CD7A7A  D28484  D78E8E  DC9898  E6A2A2  EBACAC  F0B6B6  B90000  B93232  B93C3C  B94646  B95050  BE5A5A  C35F5F  C86464  CD6969  D26E6E  B22222  B24040  B24A4A  B25454  B75E5E  BC6868  C17272  CB7776  CB7C7C  D08180  A52A2A  AA3E3E  AF4848  B45252  BE5C5C  C36666  CD7070  CD7A7A  D28484  D78E8E  800000  803232  853C3C  8F4646  945050  9E5A5A  A36464  AD6E6E  B77878  C18282  CD853F  CD8B45  CD904A  D2954F  D29A54  D79F59  D7A45E  E1A963  E1AE68  E6B36D  DB631F  E56D29  E57733  EA813D  EF8B47  EF904C  F49551  F49A56  F49F5B  F4A460  D2691E  D27328  D77D32  D7873C  DC9146  E19B50  E6A055  EBA55A  F0AA5F  F5AF64  A0522D  A05C37  A06641  A5704B  AA7A55  B4845F  B98E69  C39873  CDA27D  D7AC87  8B4513  8B4F1D  8B5927  8B6331  906D3B  9A7745  A4814F  AE8B59  B89563  C29F6D  DA70D6  DF75DB  E47AE0  E97FE5  EE84EA  F389EF  F88EF4  FD93F9  FF98FE  FF9DFF  BA55D3  BF5AD8  C45FDD  C964E2  CE69E7  D36EEC  D873F1  DD78F6  E27DFB  E782FF  9932CC  9E37D1  A33CD6  A841DB  AD46E0  B24BE5  B750EA  BC55EF  C15AF4  C65FF9  9400D3  9905D8  9E0ADD  A30FE2  A814E7  AD19EC  B21EF1  B723F6  BC28FB  C12DFF  942894  9E329E  A83CA8  B246B2  BC50BC  C65AC6  D064D0  DA6EDA  E478E4  EE82EE  8c008c  960a96  a014a0  aa1eaa  b428b4  be32be  c83cc8  d246d2  dc50dc  e65ae6  800080  8a0a8a  941494  9e1e9e  a828a8  b232b2  bc3cbc  c646c6  d050d0  da5ada  834683  8d508d  975a97  a164a1  ab6eab  b578b5  bf82bf  c98cc9  d396d3  dda0dd  828282  8c8c8c  969696  a0a0a0  aaaaaa  b4b4b4  bebebe  c8c8c8  d2d2d2  dcdcdc  000000  282828  323232  3c3c3c  464646  505050  5a5a5a  646464  6e6e6e  787878".split()
user = {}
lotto_append = []
lotto_user = []
user_build_time = {}
regen, regen_time = lotto_regen.regen()
user_turn = {}
user_build = {}
money_give = {}
botname = "금니봇"
bot_pre = "ㄱ"
last_regen = []
help = [f"`{botname} 가입`: {botname} 사용을 위해 가입합니다.\n`",
        f"{botname} 로또 [6개의 숫자(1~20)]`: 6개의 숫자를 확인해 뽑습니다.\n",
        f"`{botname} 공장`: 1분마다 자동으로 일정량의 금을 버는 공장을 건설합니다.\n",
        f"`{botname} 이익`: 공장을 이용해 얻은 금을 확인합니다.\n",
        f"`{botname} 정보`: 자신의 자산 정보를 확인합니다."]
build_list = {"병원":"`로또로 사용한 돈의 랜덤하게 (30~60)%를 회복함.`", "은행":"`로또로 받은 돈을 강화량 만큼 늘림.`", "공장":"`1시간마다 돈을 범.`"}
while True:
    async def lotto_res(event):
        str_reg = ""
        for i in regen:
            str_reg += (f"{str(i)}, ")
        str_reg = str_reg[:-2]
        print(lotto_append)
        ind = lotto_user.index(str(event.id))
        lotto_user.remove(str(event.id))
        user_choice = lotto_append[ind]
        lotto_append.remove(lotto_append[ind])
        get_money = user_turn.get(str(event.id))
        embed = hikari.Embed(title="로또 확인", description=f"1등번호:`{str_reg}`")
        channel = await event.fetch_self()
        await channel.send(embed=embed)
        if get_money:
            embed = hikari.Embed(title="로또 결과",
                                 description=f"{event}님의 선택:\n`{user_choice}`\n`당첨금: {get_money}금`! 축하합니다!🎉😆",
                                 color="0000FF")

        else:
            embed = hikari.Embed(title="로또 결과",
                                 description=f"{event}님의 선택:\n`{user_choice}`\n`당첨금: {get_money}금` 아쉽습니다...😥 \n다음엔 대박나길!😉",
                                 color="FF0000")
        user.update({str(event.id) : user.get(str(event.id)) + get_money})
        await channel.send(embed=embed)
        print(lotto_append)
        print(lotto_user)
    @bot.listen(hikari.StartedEvent)
    async def on_started(event):
        print('봇 시작')
    @bot.listen(hikari.MessageCreateEvent)
    async def print_message(event : hikari.MessageCreateEvent):
        print("{}님/{}/{}".format(event.author, event.author.id, event.content))
    @bot.listen()
    async def on_message(event: hikari.MessageCreateEvent) -> None:
        global regen, regen_time, user, user_turn, user_build, user_build_time, lotto_user, last_regen, lotto_append
        channel = await event.message.fetch_channel()
        if event.is_bot or not event.content:
            return None
        if event.content == f"{botname} 가입" or event.content == f"{bot_pre}가입":
            if not str(event.author.id) in user:
                await channel.send(f"{botname} 가입을 감사드립니다. {botname} 서버:")
                await channel.send(f"기본 돈 5000금.`{bot_pre}도움`")
                user.setdefault(str(event.author.id), 5000)
                print(user)
            else:
                await channel.send("이미 가입하셨습니다.")
        elif f"{botname} 로또 " in event.content or f"{bot_pre}로또" in event.content:
            if not str(event.author.id) in user:
                await channel.send(f"`{botname} 가입` 입력 후 진행해주세요")
            else:
                money_lotto = event.content[7:].split()

                for n in range(len(money_lotto)):
                    money_lotto[n] = int(money_lotto[n])
                print(money_lotto)
                for j in money_lotto:
                    if len(money_lotto) != 6:
                        await channel.send(f"{money_lotto} / 입력한 수의 갯수가 6개여야 합니다.")
                        break
                    if int(j) < 1 or int(j) > 20:
                        await channel.send(f"{int(j)}가 너무 작거나 큽니다.\n(1~20사이의 숫자 입력)")
                        break
                    if money_lotto.count(int(j)) > 1:
                        await channel.send(f"{j}를 중복해서 입력하셨습니다.\n(중복없이 입력)")
                        break
                if len(money_lotto) == 6:
                    if 2000 <= user.get(str(event.author.id)):
                        await channel.send(f"{event.author.mention}님, {time.strftime('%m월%d일')}/ 로또 구매 -2000금")
                        user.update({str(event.author.id): user.get(str(event.author.id)) - 2000})
                        print(user)
                        await channel.send("숫자를 뽑는중")
                        ans = lottery.check(money_lotto, regen)
                        old_ans = user.get(str(event.author.id))
                        ans = ans + old_ans
                        print(regen, "\n", regen_time)
                        user_turn.update({str(event.author.id): ans - old_ans})
                        lotto_user.append(str(event.author.id))
                        lotto_append.append(money_lotto)
                        t = int(time.strftime("%H"))
                        tm = int(time.strftime("%M"))
                        time_hour = 16
                        if t <= 23 and t > time_hour:
                            if regen == last_regen:
                                regen = lotto_regen.regen()
                            await asyncio.sleep(((int(time.strftime("%H")) - time_hour) * 3600 - (tm * 60)))
                        elif t < time_hour and t >= 0:
                            await asyncio.sleep((time_hour - int(time.strftime("%H"))) * 3600 - (tm * 60))
                        else:
                            pass
                        await lotto_res(event.author)
                    else:
                        await channel.send("금이 부족합니다.")
        elif event.content == f"{botname} 정보" or event.content == f"{bot_pre}정보":
            if str(event.author.id) in user:
                embed = hikari.Embed(title=f"{str(event.author)}님,", description=f'`{user.get(str(event.author.id))}금 소지 중`', color='9696FF')
                await channel.send(embed=embed)
        elif f"{bot_pre}공장 " in event.content:
            if str(event.author.id) in user:
                money = int(event.content[4:])

                if user.get(str(event.author.id)) >= money:
                    money_get = money * 0.01
                    if float(int(money_get)) == money_get:
                        if str(event.author.id) in user_build:
                            await channel.send(f"{money}금을 이용해 강화해 1분마다 {money_get + user_build.get(str(event.author.id))}금 만큼 생산합니다.")
                            user_build.update({str(event.author.id): money_get + user_build.get(str(event.author.id))})
                            user.update({str(event.author.id): user.get(str(event.author.id)) - money})
                            user_build_time.update({str(event.author.id): int(time.time())})
                        else:
                            await channel.send(f"{money}금을 내고 1분마다 {money_get}금 만큼 생산합니다.")
                            user_build.update({str(event.author.id): money_get})
                            user.update({str(event.author.id) : user.get(str(event.author.id)) - money})
                            user_build_time.update({str(event.author.id): int(time.time())})
                        await channel.send("공장을 건설했습니다.")
                    else:
                        await channel.send("분당 이익이 정수가 되어야 합니다.")
                else:
                    await channel.send(f"{money - user.get(str(event.author.id))}금이 더 필요합니다.")
            else:
                await channel.send(f"{botname} 가입을 하지 않았습니다. `{botname} 가입`을 통해 가입하세요.")
        elif event.content == f"{botname} 이익" or event.content == f"{bot_pre}이익":
            if str(event.author.id) in user and str(event.author.id) in user_build:
                money_add = int((time.time() - int(user_build_time.get(str(event.author.id)))) / 60)
                real_money = int(money_add) * user_build.get(str(event.author.id))
                money_get = real_money
                await channel.send(f"{money_get}금만큼 벌었습니다.")
                user_build_time.update({str(event.author.id) : int(time.time())})
                user.update({str(event.author.id) : user.get(str(event.author.id)) + int(real_money)})
            else:
                channel.send(f"{botname} 가입을 하지 않았거나 건설한 공장이 없습니다.")

        elif event.content == f"{botname} 도움" or event.content == f"{bot_pre}도움":
            msg = ""
            for i in help:
                msg += i
            embed = hikari.Embed(title=f"**{botname} 도움말**",description=msg
                                , color="#" + color[random.randint(0,len(color) - 1)])
            embed.set_image("lotto_rule.png")
            await channel.send(embed=embed)
        elif event.content == f"{botname} 돈" or event.content == f"{bot_pre}돈":
            if str(event.author.id) in user:
                if money_give.get(str(event.author.id)):
                    if time.time() >= (money_give.get(str(event.author.id)) + 86400):
                        money_ggongdon = random.randint(500, 1500)
                        await channel.send(f"+`{money_ggongdon}금`을 받았습니다.")
                        money_give.update({str(event.author.id):int(time.time())})
                        user.update({str(event.author.id) : user.get(str(event.author.id)) + money_ggongdon})
                    else:
                        tm = 86400 - (time.time() - money_give.get(str(event.author.id)))
                        if tm > 3600:
                            hour = int(tm / 3600)
                            minute = int(int(tm - hour * 3600) / 60)
                            second = int(int(tm - (hour * 3600 + minute * 60)))
                            await channel.send(f"`{hour}시간 {minute}분 {second}초`만큼 기다려주세요.\n**초간의 오차가 있을 수 있습니다.**")
                        elif 60 <= tm and tm < 3600:
                            minute = int(tm / 60)
                            second = int(int(tm - minute * 60))
                            await channel.send(f"`{tm}분 {second}초`만큼 기다려주세요.\n**초간의 오차가 있을 수 있습니다.**")
                        elif tm < 60:
                            second = int(tm)
                            await channel.send(f"`{second}초`만큼 기다려주세요.\n**초간의 오차가 있을 수 있습니다.**")
                        money_give.update({str(event.author.id) : int(time.time())})
                else:
                    money_ggongdon = random.randint(500, 1500)
                    await channel.send(f"+`{money_ggongdon}금`을 받았습니다.")
                    money_give.update({str(event.author.id): int(time.time())})
                    user.update({str(event.author.id): user.get(str(event.author.id)) + money_ggongdon})
            else:
                await channel.send(f"{event.author.mention}님 `ㄱ가입`을 통해 가입 후 진행해주세요.")

    t = None
    ans = None
    bot.run()