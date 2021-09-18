from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import *

#tugmalar
menu = ReplyKeyboardMarkup([['🌅 Fasl'],['🧾 Oy'],['🌇Kun']], resize_keyboard=True)

faslar = ReplyKeyboardMarkup([['  🌄 Bohor  '], [' 🏖️ Yoz '], [' 🗻 Kuz '], [' 🌨️ Qish '],['👈Orqaga']], resize_keyboard=True)

oyla=ReplyKeyboardMarkup([['Yanvar'], ['Fevral'], ['Mart'], ['Aprel'],['May'],['Iyun'],['Iyul'],['Avgust'],['Sentabr'],['Oktabr'],['Noyabr'],['Dekabr'],['👈Orqaga']], resize_keyboard=True)

back=ReplyKeyboardMarkup([['👈Orqaga']], resize_keyboard=True)

kunla=ReplyKeyboardMarkup([['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31'],['👈Orqaga']], resize_keyboard=True)

#funksiya
def orqa(update,context):
    update.message.reply_text('Orqaga', reply_markup=menu)
    
def bosh(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(f'Assalom alaykum {update.effective_user.first_name} \n Botimizga Xush kelibsiz Psixalogiyangizni bilish uchun<b> 🌅 Fasl - 🧾 Oy - 🌇Kun </b> malumotlarni kiritib bilib olishingiz mumkin' , reply_markup=menu)
    return 1

def fasl(update, context):
    update.message.reply_text('⭕ Hurmatli foydalanuvchi iltimos qaysi Faslda tug\'ilgansz ?' ,reply_markup=faslar)

def bahor(update, context):
	update.message.reply_text('BAHOR 🌸 \n Bahor oshuftalari juda quvnoq va hayotga chanqoq insonlardir. Xushchaqchaqligi va hazilkashligi sabab dostlarining hamisha ardogida yuradilar. Hayotiy shiorlari: buncha gozal bu olam, bir qara! Jamoaning joni bolish bilan birga, turli hiyla-nayranglarni uyushtirishga ham usta. Bir joyda otirishlari qiyin, sayohat jonu dili. Tez oshiq bolib qoladilar, ammo ayriliqlarni hech qanday gazabu nafratsiz, engil otkazadilar. Ularni sodiq dost sifatida qabul qilmaslik kerak, chunki munosabatlari vaziyat taqozosiga kora ozgarib turadi. Istalgan daqiqada umuman kozdan goyib bolib, sizni unutib yuborishlari mumkin. Birovga boglanib qolish ular uchun qadriyat emas. Vujudida bir vaqtning ozida ehtiros, xudbinlik, romantika, talabchanlik va begamlik josh urgan bu insonlar vada berishga, ayniqsa, uni bajarmaslikka usta. Lekin ular bilan zeikmaysiz.', reply_markup=back)

def yoz(update, context):
	update.message.reply_text('YOZ 🌻\nBu faslni yaxshi koradiganlar etakchilik, ilgorlik sifatlariga ega. Ozlari yonib, atrofdagilarni ham yondirib yurishadi. Ular bilan muloqot juda qiziqarli kechadi. Hech qachon tushkunlikka tushmaydilar va hamisha nekbin kayfiyatda yuradilar. Bunday kimsalar har doim yangidan-yangi goyalar oylab topib, amalga oshiradi. Yoz fasli ishtiyoqmandlarining ishdagi osishi ham tez suratda bolib, yuqori martabalarga erishadilar, yaxshi rahbarlik sifatlari bilan ajralib turishadi. Hayotiy shiorlari: qatiyat va mehnat. Ayni paytda etarli darajada murosasoz bolib, zarur orinda yon berishni ham bilishadi. Ularning shaxsiy hayotlari ham havas qilsa arzigulik. Chunki aqlni yoqotar darajada sevish va juftlariga bir umr sodiq qolishni biladilar. Atrofdagilarning kamchiliklariga nisbatan anchayin sabrli va ozlariga nisbatan talabchan bolgan bunday insonlardan yaxshi dost chiqadi. Chunki dostlarini shodlikda ham, gamda ham yolgiz qoldirmaydilar. Birgina kamchiliklari bor: haddan ortiq arazchi bolganlari holda kechimli emas.',reply_markup=back)
	
def kuz(update, context):
	update.message.reply_text('KUZ 🍁 \n Kuzni sevadiganlar tinchlik, yolgizlik va osoyishtalikni xush koradi. Kopchilikni sevmaganlari holda odamlar orasida ozlarini noqulay his etmaydilar ham. Shunchaki jamoaning ular uchun ahamiyati yoq. Hayotiy shiori: meni tinch qoying! Kayfiyatlari juda beqaror: bir qarasangiz, xandon otib yuradi, bir qarasangiz, hech qanday sababsiz xomrayib oladi. Xuddi kuz havosiga oxshab. Begonalarning nekbinligiyu zafarlari kopincha gashlariga tegadi. Biroq kuzni yaxshi koradigan odamlar juda istedodli bolishadi. Tasviriy sanat, sheriyat va nasrda katta muvaffaqiyatlarga erishishlari mumkin. Fikrlashlari ham boshqalardan farq qiladi. Muhabbatda juda vafodor: faqat bir insonni sevib otadilar. Bir bora va butun umrga! Agar muhabbatiga etisha olmasa olguncha azoblanadi va bu azob ularga ilhom manbai bolib qoladi. Ular tabiat va jonzotlar bilan muloqot chogidagina ozlarini topadilar. Biroq muhabbatiga javob berib, sevib ardoqlaydigan insonni uchratsalar, haqiqiy oilaparvarga aylanadi.',reply_markup=back)
	
def qish(update, context):
	update.message.reply_text('QISH ❄️ \n Bu faslni sevadiganlar, odatda, oziga ishongan va mustaqil insonlardir. Hayotiy shiorlari: faqat ozingga ishon! Katta davralarni xush korishmaydi. Dostu tanishlari juda oz. Ammo shu ozgina odamlarga qattiq ishonishadi. Ishonmasa, ularni yaqin yolatmagan bolishardi. Juda qatiyatli bu kimsalar oz rejalarini birovga oshkor qilmay, yolgiz amalga oshirish yoki hayot oqimini maqsadlariga boysundirishni biladilar. Qishni yaxshi koradigan insonlar kamgap bolishadi. Sorasangiz, javob beradilar, ammo ozlari hech qachon birinchi bolib gap qotmaydilar. Pul ishlab topishni bilishadi, qulaylik va farovonlikni qadrlashadi. Ozlariga qadrli insonlar uchun kop narsadan voz kechishlari mumkin. Kamchiliklari: xasislik va pismiqlik. Shuningdek, bunday insonlar kechirishni bilmaydi. ',reply_markup=back)

def oy(update, context):
    update.message.reply_text('⭕ Hurmatli foydalanuvchi iltimos qaysi oyda tug\'ilgansz ?' ,reply_markup=oyla)

def yan(update,context):
    update.message.reply_text('Yanvar \n shu oyda tugilgan bolsangiz, demak, u muloyim va juda tasirchan. Dost-birodalardan yordamini ayashmaydi. Kongilsizliklardan togri xulosa chiqarishga harakat qilishsa, omad qushi ularni tark etmaydi. Biroz sabrsizliklari sabab munosabatlarda tushunmovchilik kuzatilishi mumkin.',reply_markup=back)

def fev(update,context):
    update.message.reply_text('Fevral \n Oziga ishongan, uyim-joyim deydigan, zakovatli erkaklar aynan shu oyda tugilarkan. Ayriliqdan qorqishadi. Doim oila davrasiga shoshishadi. Ular uchun eng muhimi, oilaviy baxt. Bitta kamchiliklari kurashuvchanmas. Maqsadlari yolida kichik muammo sabab ham hammasiga qol siltab ketishadi.',reply_markup=back)

def mar(update,context):
    update.message.reply_text('Mart \n Bahorning ilk oyida tugilgan erkaklar soglom firklaydigan bolisharkan. Shu bilan birga, juda tejamkor ham. Pullarini tiyin-tiyinlab yiqqanlari uchun ham katta rejalarni bemalol amalga oshirishadi. Salbiy tomonlari – muammoli vaziyat tugilganda quyon bolishga usta.',reply_markup=back)
    
def ap(update,context):
    update.message.reply_text('Aprel \n Katta bolsa-da, bolaligini qoymagan erkaklar tadbirkor va gapga ton kiydiradiganlardan. Aynan shu xususiyatlari sabab ular atrofdagilarni oz soziga ishontira olishadi va pul borasida omadlari chopadi. Masuliyatli bolishsa, hayotda kop narsaga erisha olishardi.',reply_markup=back)

def may(update,context):
    update.message.reply_text('May \n Vahimakashligini hisobga olmasak, aqli va topqirligi tahsinga loyiq. Xotirjamlik ular uchun juda muhim. Shuning uchun shovqin-suronga yoqlar. hayotlari bir maromda kechishini istashadi. Ozgarishlardan chochishadi.',reply_markup=back)
    
def iy(update,context):
    update.message.reply_text('Iyun \n Mazkur oyda tavallud topgan erkaklar barchaga birdek yaxshilik istashadi, qoldan kelgancha atrofdagilarga yordam qilishadi. Bu oyda tugilganlar bilan taqdiringizni boglasangiz, hayotingiz farovon kechadi. Chunki ular har qanday vaziyatda ham oltin ortalikni topa olishadi. Salbiy jihatlari, salomataliklariga befarqligi.',reply_markup=back)

def il(update,context):
    update.message.reply_text('Iyul \n Favqulodda iqtidor egalari ayni shu oyda dunyoga kelishar ekan. Biroz xayolparatsliklari ham shundan. Ular mashhurlikka va boylikka intilishadi. Agar maqsadlari sari tinmay harakat qilishsa, erishishadi ham. Faqat uni doim olga undab turishingiz kerak.',reply_markup=back)
    
def av(update,context):
    update.message.reply_text('Avgust \n Erkinlikni xush korishadi. Oziga xon – kolankasi maydon, bolib yurishni istaydi doim. Shu sabab osmirligi ota-onalar bilan muammolar kuzatiladi. Omadlari chopishi yanada oziga bolgan ishonchni oshiradi.',reply_markup=back)
    
def sen(update,context):
    update.message.reply_text('Sentyabr \n Kuzning ilk oyida tugilgan erkaklarning ham taqiqlarga xushi yoq. Xolis va ezgulik istovchi bolishadi. Manfaat kozlamaydigan dostdir ular. Faqat birovlarning fikri bilan ish tutishi yaxshimas.',reply_markup=back)
    
def ok(update,context):
    update.message.reply_text('Oktabr \n Oilasining, yaqinlarining tashvishi bilan yonib-kuyadiganlar. Ishonuvchanliklar bazida pand berib qoladi. Tuygulariga quloq tutishadi. Vafodorliklari esa tahsinga loyiq.',reply_markup=back)
    
def no(update,context):
    update.message.reply_text('Noyabr \n Ushbu oy vakillari dono, hajviyaga usta va ishning kozini biladigan bolishadi. Karera pogonalarining choqqisini zabt etishadi. Chunki ular masuliyatli va mehnatkash. Birovlarning manfaatini deb, o`zining imkoniyatlarini cheklashlari zarariga ishlaydi',reply_markup=back)
    
def dek(update,context):
    update.message.reply_text('Dekabr \n Kezi kelganda, juda qattiqqol. Ilm qilishga moyil bolishadi. Notanishlar bilan tez til topishishadi. Karera borasida ham oshigi olchi, faqat shuhratga berilib, manmanlik qilishmasa, bas. Jahli chiqqanda, olovga yog sepmay, jim turishingiz shart',reply_markup=back)
    
def kun(update, context):
    update.message.reply_text('⭕ Hurmatli foydalanuvchi iltimos qaysi kunda tug\'ilgansz ?' ,reply_markup=kunla)

def k1(update,context):
    update.message.reply_text('Bu kuni tugilganlarning xotirasi pastroq bolib, ayrim voqealarni unutib qoyadi. Turmush qurishda doimo baxti yurishavermaydi. Agar turmush orogi mahkam turmasa uyi buzilib ketsa ham parvo qilmaydi.',reply_markup=back)
    
def k2(update,context):
    update.message.reply_text('Bu kuni tug\'ilganlar kongliga yaqin odami bilan ruhan yaqinlashishga moyil boladi. Sevgiga aql bilan yondoshadilar. Oziga ruhan yaqinlar bilan turmush qurishni xohlaydilar.', reply_markup=back)
    
def k3(update,context):
    update.message.reply_text('Bu kun tugilganlar ozlarining shiddatkorliklari bilan ajralib turadilar. Kongilxushlik jonu-dili. Nafsni qondirmaguncha tinchimaydilar. Doimo ozlarini boshqalardan bir pogona ustun qoyadilar.', reply_markup=back)
    
def k4(update,context):
    update.message.reply_text('Bu kun tugilganlar boshqalar bilan munosabatda qiynalishadi, shuningdek ular bilan ham oldi-berdi qilish qiyin. Intim munosabatda juda sust. Tushkunlikka beriluvchan, oziga sodiq odamni qollab turishga doim muhtoj va qizganchiq bolishadi. Unaqalar bilan yashash uchun sabr-bardoshli bolish kerak.', reply_markup=back)
    
def k5(update,context):
    update.message.reply_text('Shu kuni tugilganlar pulni juda yaxshi korishadi. Ozlariga bino qoygan boladilar. Ozlariga uncha qaramasalarda, pul topib boyish payida boladilar.', reply_markup=back)
    
def k6(update,context):
    update.message.reply_text('Bu kunda tugilganlar hissiyotli, xayolparast, oz etiqodlariga sodiq boladilar. kopincha oz hissiyotlari uygunlashtirib yuboradilar.', reply_markup=back)
   
def k7(update,context):
    update.message.reply_text('Shu kuni tugilganlar bilan ehtiyotkorroq bolish zarur. Chunki ularning fikri tez-tez ozgarib turadi. Bir joyda turolmaydilar, doim yaxshi sherik axtarib yuradilar, shuning uchun ham ikkinchi bor yostiqdoshlarini almashtirishga togri keladi.', reply_markup=back)
    
def k8(update,context):
    update.message.reply_text('Bu kunda tugilganlar hissiyotli, oz dostlariga sodiq boladilar. Lekin ularni kopincha eng ishonganlari ham sotadi. Ularni tushunish va sevish murakkab bolib, agar ular sevsalar qattiq sevadilar.', reply_markup=back)
    
def k9(update,context):
    update.message.reply_text('Bu odamlar hohishni bayon qilishga ojiz boladilar. Toqqizinchida tugilganlar kamdan-kam sevib qoladilar, ammo sevsalar bir umrga vafodor boladilar. Ular bir marta xato qiladilar. Ozlariga mos kishjilar bilan tez kirishib ketadilar. ', reply_markup=back)
    
def k10(update,context):
    update.message.reply_text('Bu kun juda yaxshi va baxtli kun. Shu kuni tugilganlar ham oziga oxshagan qobiliyatli sherik izlaydilar. Ular bilan kelishish oson.', reply_markup=back)
    
def k11(update,context):
    update.message.reply_text('Bu kuni tugilganlarning kongli ochiq va sadoqatli boladilar. Sotqinlik va maglubiyatni kotara olmaydilar. Ular mustaqillikka intiladilar, lekin mustaqil yashashga qodir emaslar. Ularning hayoti doimo kurashdan iborat.', reply_markup=back)
    
def k12(update,context):
    update.message.reply_text('Ular bilan yashash oson, kongli ochiq, ozlariga oxshaganlarni izlab yuradilar, yumshoq xarakterli, ularga qattiq gapirib ish bitkazib bolmaydi. Ularga muhabbat bilan yumshoq sozlar muomila qilib kop narsaga erishish mumkin.', reply_markup=back)
    
def k13(update,context):
    update.message.reply_text('Ular hissiyotida qiyinchiliklar bor. Bunaqa odamlar ichki tomondan doimo birortasini qollashga muhtoj. Ular bilan doim birga yashash qiyin.', reply_markup=back)
    
def k14(update,context):
    update.message.reply_text('Bu kun tugilganlarga sherik bolish uchun boy odam bolish kerak. Munosabati sovuq. Ularni sevib qolish ham mushkul, lekin oziga tortadigan ohangrabosi bor.', reply_markup=back)
    
def k15(update,context):
    update.message.reply_text('Oyning 15-da tugilganlar xayolparast, sal narsaga lovullab yonadi, shuncha tez ochadi. Yaxshi taminlangan puldor odamlar bilan tez chiqishib ketadi. Agar uni yostiqdoshi tushunsa oilasi mustahkam boladi', reply_markup=back)
    
def k16(update,context):
    update.message.reply_text('Bu kun tugilganlar kimgadir qattiq boglanib qolish xususiyatiga ega. Lekin kop kishi bilan koproq bolish ham joniga tegadi. Turmushni turli tomonlarini totib korishga ishqiboz. Ishqiy munosabatda ehtirosga ega lekin kongli bosh.', reply_markup=back)
   
def k17(update,context):
    update.message.reply_text('Hissiyoti kayfiyatiga qarab ozgarib turadi. Agar sherigi pand bersa, aloqani butunlay uzadi. Turmushi kamdan-kam buziladi.', reply_markup=back)
    
def k18(update,context):
    update.message.reply_text('Juda ehtirosli bolsalarda, ozlaridagi moyillikni aytishga uyaladi. Buning uchun ozlarini koyib yuradilar. Yumshoq momilali, juda kam janjallashadi.', reply_markup=back)
    
def k19(update,context):
    update.message.reply_text('Bu kuni tugilganlar ozimniki togri deydigan, churt kesar, boshqalar uning uchun xizmat qilishni xohlaydigan felga ega. Biror masalani kopchilik bilan hal etishni istamaydi, yolgiz ozi hal qilishni xohlaydi.', reply_markup=back)
    
def k20(update,context):
    update.message.reply_text('Bu kuni tugilganlar ruhlar dunyosi bilan yashaydi. Shuning uchun ham sevgan kishisi shunday bolishini xohlaydi.', reply_markup=back)
    
def k21(update,context):
    update.message.reply_text('Bu kuni tugilganlar ham ruhan yaqinlikka moyil boladi. Ular juda beriluvchan bo\'lishadi.', reply_markup=back)
    
def k22(update,context):
    update.message.reply_text('Bu kuni tugilganlarning hissiyotlari kuchli emas. Agar sevib qolsalar bir umr vafodor boladilar. Qizganchiq, kongli yarim kishilar. Arazchan, ularni doim qollab turishi kerak.', reply_markup=back)
    
def k23(update,context):
    update.message.reply_text('Sherigiga oz tazyiqini otkazishni yoqtiradigan, ehtirosli va unga boysunuvchan sherik topmoqchi. Agar shunday sherik topsa turmushi yaxshi boladi.', reply_markup=back)
    
def k24(update,context):
    update.message.reply_text('Jismonan zaif, orzular dunyosida yashaydi. Ehtiros bilan sevadi, har xil ish bajarishni yaxshi koradi.', reply_markup=back)
    
def k25(update,context):
    update.message.reply_text('Shu kuni tugilganlar koproq moddiy tomondan taminlangan odamlar bilan birga birga bolishni yoqtiradilar.', reply_markup=back)
    
def k26(update,context):
    update.message.reply_text('Juda sezgir boladilar, ruhan yaqinlikka muhtoj, sevgan kishilari uchun qurbon bolishga ham tayyor kongilchangligiidan foydalanib turishadi. Lekin qatiyatli', reply_markup=back)
   
def k27(update,context):
    update.message.reply_text('Ozgaruvchan, pulga yoki narsaga och bolganligi uchun ham ogmachi, oziga oxshaganlarni yaxshi koradi, kop kishi bilan kelishib ketadi, aqlli, kuchli xarakterga ega.', reply_markup=back)
    
def k28(update,context):
    update.message.reply_text('Chin yurakdan sherigiga sadoqatli, kamtar, ruhan yaqinlikka moyil, yumshoq, sherigi bilan kelishmasa voz kechishi oson. Ular bilan turmush qursa baxtli bola oladilar.', reply_markup=back)
    
def k29(update,context):
    update.message.reply_text('Bu kuni tugilganlar oziga yoqqanlarni maqtanishni xush koradilar. Uni bazida kimdir yonaltirib turish kerak. Bu kuni tugilganlar ozgaruvchan boladilar.', reply_markup=back)
    
def k30(update,context):
    update.message.reply_text('Ular oz hukmini otkazishni yaxshi koradilar. Shuning uchun ularga yumshoq soz, yon beruvchi sherik zarur boladi. Oziga yoqqan narsani orqasidan quvib yuradi va unga erishmaguncha qoymaydi, sherigi uning yoliga qanday yurganini ham sezmay qoladi. Oziga boysunuvchilar bilan aloqada bolishni koproq yoqtiradilar.', reply_markup=back)
    
def k31(update,context):
    update.message.reply_text('Sadoqatli va kongli toza, sevgiga sodiq boladilar. Ular juda jahldor va injiq bolishlari ham mumkin. Xarakterlari juda ogir, bunaqa odamlarni ko`nliga qarab yashaydigan odamlargina baxtli qila oladilar.', reply_markup=back)

#bot_token
updater = Updater('token')

#handler
conv_handler = ConversationHandler(entry_points = [CommandHandler('start', bosh)],
    states={
        1: [ MessageHandler(Filters.regex('^(🌅 Fasl)$'), fasl),
        MessageHandler(Filters.regex('^(🧾 Oy)$'), oy),
        MessageHandler(Filters.regex('^(🌇Kun)$'), kun),
        MessageHandler(Filters.regex('^(🌄 Bohor)$'), bahor),
        MessageHandler(Filters.regex('^(🏖️ Yoz)$'), yoz),
        MessageHandler(Filters.regex('^(🗻 Kuz)$'), kuz),
        MessageHandler(Filters.regex('^(🌨️ Qish)$'), qish),
        MessageHandler(Filters.regex('^(Yanvar)$'), yan),
        MessageHandler(Filters.regex('^(Fevral)$'), fev),
        MessageHandler(Filters.regex('^(Mart)$'), mar),
        MessageHandler(Filters.regex('^(Aprel)$'), ap),
        MessageHandler(Filters.regex('^(May)$'), may),
        MessageHandler(Filters.regex('^(Iyun)$'),iy),
        MessageHandler(Filters.regex('^(Iyul)$'), il),
        MessageHandler(Filters.regex('^(Avgust)$'), av),
        MessageHandler(Filters.regex('^(Sentabr)$'), sen),
        MessageHandler(Filters.regex('^(Oktabr)$'), ok),
        MessageHandler(Filters.regex('^(Noyabr)$'), no),
        MessageHandler(Filters.regex('^(Dekabr)$'), dek),

        MessageHandler(Filters.regex('^(👈Orqaga)$'), orqa),

        MessageHandler(Filters.regex('^(1)$'), k1),
        MessageHandler(Filters.regex('^(2)$'), k2),
        MessageHandler(Filters.regex('^(3)$'), k3),
        MessageHandler(Filters.regex('^(4)$'), k4),
        MessageHandler(Filters.regex('^(5)$'), k5),
        MessageHandler(Filters.regex('^(6)$'), k6),
        MessageHandler(Filters.regex('^(7)$'), k7),
        MessageHandler(Filters.regex('^(8)$'), k8),
        MessageHandler(Filters.regex('^(9)$'), k9),
        MessageHandler(Filters.regex('^(10)$'), k10),
        MessageHandler(Filters.regex('^(11)$'), k11),
        MessageHandler(Filters.regex('^(12)$'), k12),
        MessageHandler(Filters.regex('^(13)$'), k13),
        MessageHandler(Filters.regex('^(14)$'), k14),
        MessageHandler(Filters.regex('^(15)$'), k15),
        MessageHandler(Filters.regex('^(16)$'), k16),
        MessageHandler(Filters.regex('^(17)$'), k17),
        MessageHandler(Filters.regex('^(18)$'), k18),
        MessageHandler(Filters.regex('^(19)$'), k19),
        MessageHandler(Filters.regex('^(20)$'), k20),
        MessageHandler(Filters.regex('^(21)$'), k21),
        MessageHandler(Filters.regex('^(22)$'), k22),
        MessageHandler(Filters.regex('^(23)$'), k23),
        MessageHandler(Filters.regex('^(24)$'), k24),
        MessageHandler(Filters.regex('^(25)$'), k25),
        MessageHandler(Filters.regex('^(26)$'), k26),
        MessageHandler(Filters.regex('^(27)$'), k27),
        MessageHandler(Filters.regex('^(28)$'), k28),
        MessageHandler(Filters.regex('^(29)$'), k29),
        MessageHandler(Filters.regex('^(30)$'), k30),
        MessageHandler(Filters.regex('^(31)$'), k31),
        ]
        },
    fallbacks=[MessageHandler(Filters.text, menu)]
)


updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
