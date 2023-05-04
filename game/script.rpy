﻿# Определение персонажей игры.
define ks = Character('Ксения', color="#87CEFA")
define gr = Character('Гриша', color="#FFE4B5")
define lr = Character('Лера', color="#E08128")

# Определение второстепенных персонажей
define lr2 = Character('Неизвестно', color="#E08128")
define ks2 = Character('Неизвестно', color="#87CEFA")
define ka2 = Character('Неизвестно', color="#6609AD")
define di2 = Character('Неизвестно', color="#06CC48")
define children = Character('Ребенок', color="#808080")
define stopitsnotmymom = Character('Мать', color="#808080")

#Изображения
image closeeyes = "Backgrounds/closeeyes.png"
image closeeyes2 = "Backgrounds/closeeyes2.png"
image theatre = "Backgrounds/theatre.png"
image theatre2 = "Backgrounds/theatre2.png"
image taxinight = "Backgrounds/taxinight.png"
image prologe = "images/prologe.png"
image firstday = "images/firstday.png"
image grroom = "Backgrounds/ggroom.png"
image padik = "Backgrounds/padikgg.jpg"
image shop2out = "Backgrounds/shop2out.png"
image shop2 = "Backgrounds/shop2.png"
image city = "Backgrounds/city.png"
image noise = "Illustration/Noise.png"
image lrhorrorfull = "Illustration/LeraHorrorFull.png"
image quitdoor = "Illustration/QuitDoor.png"
image twodead = "Illustration/twodead.png"
image womanreverse = "Illustration/WomanReverse.png"
image travmaglaz = "Illustration/travmaglaz.png"
image mrakdoor = "Illustration/MrakDoor.png"
image inpadik = "Backgrounds/inpadik.png"
image inpadikday = "Backgrounds/inpadikday.png"
image grroomnight = "Backgrounds/ggroomnight.png"
image openeyes = "Illustration/openeyes.png"
image dvor = "Illustration/dvor.png"

#спрайты
image kseniaD = "Sprite/kseniaD.png" 
image kseniaN = "Sprite/kseniaN.png"
image kseniaP = "Sprite/kseniaP.png"
image lrsprite = "Sprite/lerasprite.png"
image lrhorror = "Sprite/lerahorror.png"
image katyaD = "Sprite/katya/katyaD.png"
image katyaN = "Sprite/katya/katyaN.png"

init-2:
    image mm_bg=Movie(play="images/rainmindmenu.mpg",size=(1920,1080))

screen map:
    modal True
    zorder 100
    fixed:
        xsize 1920 ysize 1080
        add "images/map/maptestchoice.png" align (.5,.5)
    fixed:
        xsize 1920 ysize 1080

    button:
        xpos 535 ypos 171
        xsize 119 ysize 120
        idle_background "images/map/icondv.png"
        hover_foreground "images/map/icondvact.png"
        focus_mask True
        tooltip "{b}Магазин{/b}{p}{i}{size=18}Дешевое всегда найдется!{/size}{/i}"
        action Hide("map"), Jump("dvlera")

# Игра начинается здесь:
label main_menu:
    $ renpy.movie_cutscene ('images/loading.ogv')
    scene mm_bg
jump main_menu_screen

label start:
    scene prologe with dissolve
    $ renpy.pause (3.0, hard=True)
    jump prologe
label prologe:
    stop music fadeout 1.0
    play music "audio/MoreThanHalf.mp3"
    scene closeeyes
    "Ночь"
    "Осела дымка на плацдарм"
    "Здесь скоро будет бой"
    "Осталось считанное время"
    "А я один, смолю себя и сигареты"
    "И страха нет, что скоро мне конец"
    "Осталось несколько секунд"
    "Три"
    "Два"
    "Один..."
    scene theatre
    hide closeeyes
    "Открыв глаза я медленно прошелся взглядом по площадке, от левого до правого конца"
    "Наша встреча должна была проходить на площади у городского театра"
    "Не знаю, стоило ли приходить. Попытки доказать себе, что я не трус и отвечаю за слова привели меня в такой пиздец"
    "Мне самому становится смешно, что я отстаиваю честь, перед пачкой лысой гопоты"
    "Я мог просто не придти и все б забыли через месяц"
    "Кто же виноват, что пацаны живут по старому. Не возрастом, они почти мои ровесники. Юмор, музыка и стиль, абсолютно всё совершенствуется. А им все за понятия и честь... да треки АК-47"
    "Интересно, что бы случилось, если бы один из этих типов попался в интернете на рикролл?"
    "Он бы пробил монитор?"
    "Хотя, он бы вряд-ли вообще что-то понял"
    "До таких чувачков ещё и старые мемы не дошли"
    scene closeeyes
    hide theatre
    "..."
    "На ощупь, я достал пачку сигарет из своих шароваров и решил скурить ещё одну сигарету, скорее всего на последок сегодняшней ночи"
    "Смысла оставаться здесь уже не имелось" 
    "Глубокий анализ ситуации, и время сколько я уже здесь стою дали мне понять, что стоило бы мне уже просто пойти в сторону дома и забыть про всю эту ситуацию"
    scene theatre2
    hide closeeyes
    play sound "audio/blesk.mp3"
    "Но в момент, я вновь открыл глаза и увидел яркий блеск по левой стороне театра"
    "Кто-то приближался, и похоже не с голыми руками"
    "В голове, что это могло быть, образовалось множество догадок"
    "Арматура, нож, кастет, телескопическая дубинка, или же бейсбольная бита"
    "Я четко видел силуэт, но распознать кто это мне удавалось"
    "Он приближался и становилось всё более напряжено"
    "Но, когда силуэт прошел ещё буквально 10 метров, мои нервы стали стали успокаиваться"
    scene theatre
    hide theatre2
    show kseniaP
    with dissolve
    "Этим таинственным страшным силуэтом оказалась Ксения, и огромная металлическая блямба её сумки"
    gr "Ксения, милая! Твой лик из тумана встает!"
    play sound "audio/siga.mp3"
    "Она не стала на это ничего отвечать мне, а лишь встала напротив и тоже закурила сигарету"
    "Ксения удивительный персонаж, на самом деле"
    "Раньше она была черезмерно правильной и отличницей, а сейчас хлынула во все тяжкие"
    "Компания сильно повлияла на неё, что порой её просто тяжело узнать"
    "Она стала уважать себя и делать все, что она буквально хочет"
    "Конечно, все в рамках закона и личного пространства"
    gr "Ну и где ваши друзья, Ксения?"
    ks "Мы давно знакомы, можешь себе позволить обратиться и на ты. - сказала она с легким негативом"
    gr "Да, но мы знакомы только в рамках того, что просто учились вместе несколько лет, и то не держали контакт между собой"
    ks "Гриша, блять"
    gr "Расслабься, просто я не ожидал что на «стрелу» придешь только ты одна, ещё и против меня"
    gr "В чем подвох?"
    gr "С какой стороны на меня сейчас налетит толпа? С этой или с той стороны?"
    ks "Нету никакого подвоха..."
    "Она сказала это одновременно выпуская дым из-за рта, из-за чего её голос приобретал чутка басовые волны"
    "При этом она сказала это так спокойно, будто убаюкивая"
    gr "Ну, и когда тогда прид..."
    "Ксения резко перебила меня, продолжая говорить также спокойно:"
    ks "Гриша..."
    ks "Вот скажи, сколько ты тут уже стоишь?"
    gr "Часа, наверное, полтора, чутка больше даже"
    ks "На сколько по времени вы «забивали стрелу»?"
    gr "На часа три ночи..."
    ks "Хорошо, ты же видишь, что их нету, чего стоишь то тут?"
    gr "Ну вот ты же пришла, значит и они сейчас прибудут"
    ks "Гриша, как бы ты это не воспринимал, эти парни пунктуальные"
    ks "Если они назначали время, они ещё и раньше могут приехать"
    "И тут я начал вставлять ей свои палки в колеса:"
    gr "Ну и где тогда твои друзья, почему тут только ты? Мне с тобой что-ли разбираться?"
    ks "Прекрати орать на меня и слушай"
    "Я правда повысил тон"
    "Не знаю от чего, от самой Ксюши или, что мои ожидания происходящего пошли коту под хвост"
    ks "Они приехали, остановились и смотрели, искали тебя"
    gr "Но, не нашли?"
    ks "Да, не нашли"
    gr "То есть это вы были в машине?"
    ks "Да..."
    "Ксюша указала на парковку справа от площади, где они высматривали меня из автомобиля"
    gr "Туман..."
    ks "Да... видимо"
    ks "Если ты, конечно, и правда стоишь тут так долго"
    gr "Почему вы не вышли и не посмотрели повнимательней?"
    ks "Емае, Гриша... Такое ощущение, как будто бы ты просто хотел, чтобы тебя отпиздели здесь"
    gr "Нет, я просто злюсь и хочу понять ситуацию"
    ks "Да, блять, посмотри вокруг, везде сыро, мокро, холодно ещё и туман этот ебучий"
    gr "Ладно, всё я понял"
    "По голосу Ксении было понятно, что она сама чем-то недовольно"
    "Её раздражало всё, хоть она и старалась это не показывать"
    gr "Вижу ты расстроенна чем-то. Ну как вижу... по-голосу понятно"
    ks "Да, поссорились. Больше тебе знать не надо"
    "И после этого, она решила придти ко мне? Ну, типо, чтобы меня наверняка убили, уже по двум причинам"
    "Первая, что я охренеть какой приколист, а вторая, что увожу девушку гопаря"
    gr "А зачем, ко мне-то вообще пришла? Типо на моей стороне теперь? Или все таки это... подстава?"
    "Я произносил это уже осторожно, я чувствовал, что уже достал её своими вопросами"
    ks "Гришь, мне просто домой нужно и всё..."
    ks "Я недалеко живу... через площадь пройти все равно бы пришлось, ну и ты тут стоишь..."
    gr "Понял"
    "После моего вопроса, она расстроилась ещё сильнее"
    "Я не знал, стоит ли её провожать, ибо ситуация сама по себе не очень, но и не хотелось бы, чтобы она попала, в какую-то передрягу"
    ks "Ладно, мне нужно идти, ты тоже давай домой топай, нету тут смысла тебе оставаться"
    gr "Может, тебя проводить?"
    ks "Даже не думай, я сама дойду... брат встретит"
    gr "Как скажешь... как скажешь"
    hide kseniaP
    "Ксения ушла ничего больше не сказав, я не стал идти вместе с ней, а послушался её"
    "Я давно не слышал Ксению, сразу после того как мы окончили школу наши линии разошлись"
    "Виделись лишь иногда, но не общались. Мы в целом не общались особо"
    "Тем временем, на часах было уже около четырех утра и следовало идти домой"
    "Мне не особо хотелось идти, поэтому лучшем решением было просто вызвать такси до моего дома"
    "Благо, ночью оно ещё и стоило дешевле"
    "После такой эмоциональной нагрузки пришло расслабление"
    "Моментальное «ничегонехочу» начало набирать вверх, и я клонился в сон"
    stop music
    play music "audio/gamestart.mp3"
    gr "А вот и моя карета..."
    scene taxinight
    hide theatre
    "Я сел в такси и мы начали мчать с таким же сонным водителем по дорогам нашего блеклого и одновременно яркого города"
    "В машине играл довольно приятный бит, который водитель включал из-за ярко выраженной бочки лезущей из динамиков, дабы заглушить желание уснуть"
    "Дороги были пусты, мы буквально мчались мимо панелек и торговых центров"
    "Через минут десять мы уже приближались к моему дому"
    "Мы не обменивались словами, мне и ему просто хотелось спокойствия и не более"
    "Поворот за поворотом. Заезд во двор. Ближе к подъезду"
    "Я дома."
    scene closeeyes
    hide taxinight
    "То как я вернулся, особо из себя ничего не представляло"
    "Я прошел весь путь от коридора до комнаты в темноте, дабы не будить всех лишний раз"
    "Я не стал переодеваться и плашмя упал на кровать"
    gr "Спокойной ночи, ночь"
    "..."
    stop music
    scene firstday with dissolve
    $ renpy.pause (3.0, hard=True)
    jump firstdaylvl

label firstdaylvl:
    play music "audio/day1start.mp3"
    scene closeeyes2
    hide firstday with dissolve
    lr2 "Мне важно, чтобы с тобой все было хорошо..."
    gr "Не переживай, все будет отлично"
    "..."
    ks2 "Тебе как обычно, ничего не понятно"
    gr "Замолчи, ты меня раздражаешь!"
    "..."
    ka2 "Знаешь, а ты неплох, но вкус у тебя дерьмовый"
    gr "Спасибо..."
    "..."
    di2 "Ну что, ещё по одной?"
    "..."
    scene grroom with dissolve
    hide closeeyes2
    gr "Нет... нет, я воздержусь..."
    "Эти сны... Они пролетали мгновенно, и лишь их отголоски оставались в моей голове"
    "Так бывает, люди часто забывают сны"
    "Я помню, что их было много, но о чём они, увы..."
    "Допустим то, что мне уже не важно, но мало ли, что это знак?"
    "Ведь сонники придумал не дурак"
    "А может и дурак..."
    "Не важно... важно то, что все что мне приснилось, я чисто на чисто забыл"
    "..."
    "В окно пробивались яркие лучи света, а на столе, не менее ярким и раздражительным звонком ревел будильник"
    "Но пенье птиц сильнее, скорей я проснулся от него"
    "Будильник пал в этой войне... хотя, красивее сказать - суицид"
    "От собственной вибрации он лихо прыгнул со скалы"
    "Хотя, мне было его жалко, такой советский милый аппарат"
    "Зато сейчас он замолчал, что радует меня"
    "..."
    "Сердцу не передать, как я не хотел вставать с кровати"
    "Но и стагнировать в кровати тоже не хотелось"
    "Первый день лета... Хотелось бы создать ощущение, что я не проебываю его"
    "Ещё где-то пять минут, я ворочился из стороны в сторону, пытаясь найти удобное не продавленное место на подушке"
    "А ещё через десять, я просто встал с кровати с пониманием того, что уснуть мне не получится"
    "Бедный будильник под моими ногами показывал на часах пол второго дня"
    "Поставив его обратно на стол, подальше от края стола, я пошел ближе к окну"
    "А там как и подобало мне, производился обряд по раскуру сладкой цибары"
    "Мыслей не было никаких, просто смотрел на проходящих по двору людей, детей бегающих по площадке"
    "И на крышу... Крышу небольшой котельной во дворе"
    "Из окна прекрасно видно, как на ней обитают одинокие игрушки и мячи"
    "Раз в квартал они обновлялись, там были и розовые, зелёные, голубые резиновые мячи, которые уже были подсдутые"
    "Иногда там виднелись и хорошие футбольные мячи"
    gr "Если моему ребёнку нужны будут игрушки, я знаю куда мне обратиться"
    "Бывало конечно, что доблестные рыцари двора подсаживали друг-друга, дабы пробраться навверх, и раздать всем добра с этой проклятой крыши"
    "Но происходило это редко, в частности, когда им самим нужно было достать то, что они не нароком туда закинули или пнули"
    gr "Бля"
    "Пепел упал с сигареты, и покатился по голову торсу"
    "Бывает, хули"
    "Процесс подходил к концу"
    "Не буду закрывать окно, пусть комната проветрится"
    "Надо перейти на электронку, не придется покупать ежедневно пачки по двести рублей, да и в целом вонять"
    "До меня как-всегда, се тренды доходят с опозданием"
    "Хотя, для меня курение вообще не являлось трендом"
    "Просто ошибка, даже не попытка кому-либо подрожать или выделится в кругу друзей"
    "..."
    "Дома я был один"
    "Родители уехали в деревню, для них это райский уголок или что-то типо того"
    "Мне там никогда не нравилось, у меня там нет друзей, да и горбатиться в огороде не самое лучшее"
    "Целый месяц я остаюсь в пустой квартире, а может даже и на два"
    "Всё зависит от того, захотят ли они в дальнейшем отпраится в другую область, ближе к границе с Финляндией"
    "В Петрозаводск, короче"
    "Они любят порыбачить и пошастать по хваойным пейзажам"
    "Типо духовное и культурное обогащение, рисовать пейзажи и наслаждаться природой"
    "..."
    "Желудок ворчал"
    "Нет, это не сигарета"
    "Я просто адски хотел кушать"
    "Идет буквально второй день моего голодания"
    "На днях я траванулся дешевым пойлом, облевал всю кухню, а после просто потерял аппетит ко всему съедобному"
    "Сегодня я чувствовал себя в разы лучше, головная боль и... прочие проблемы моего организма вроде как завершились"
    "Оставалось лишь только чего-то вкусно и плотно поесть"
    "Но, единственное, что оставалось в холодильнике, это беспонтовый салат"
    "Огурцы, помидор и салатный лук"
    "Ништяк, да?"
    "Я тоже думаю, что нет"
    "Кинув взгляд на кошелек, я принял решение, что все-таки нужно будет сходить в магазин и купить какого-нибудь джанка, или что-то нормальное"
    "Вообщем того, что я увижу в магазине и что вцепится мне в душу"
    "Буквально за двадцвать минут, я успел умыться и собраться. Прощаться было не с кем, домашних животных у меня не было"
    "Молча и тихо я покинул свою комнату, а затем квартиру..."
    "..."
    stop music
    scene padik
    hide grroom
    "Солнечный свет адски слепил меня"
    "Ну а хули, два дня сидеть дома, почти в темноте"
    "Сегодня один из теплых и ярких дней по прогнозу на этот месяц"
    "Такое случается достаточно редко в первые дни лета"
    "Ну как... всегда тепло, но сегодня особенно"
    "Машинальным движением, я потянулся к телефону и еле разглядев что-то на экране, я включил один из своих плейлистов"
    play music "audio/SelfControl.ogg"
    "И к счастью заиграл мою любимй трек"
    gr "А мне это нравится"
    "Во дворе царил хаос"
    "Дети, у которых только начались каникулы бегали туда сюда"
    "Хотя сорок минут тому назад их было здесь как на пальцах пересчитать"
    "Хотел бы я снова окунуться в то время, когда нет забот и носишь как угарелый"
    "Стоп, я же занимаюсь тем же самым..."
    "Ам..."
    "Наверное, не совсем"
    "Все-таки, я решаю какие-то вопросы своей жизни самостоятельно и принимаю важные решения"
    gr "Такие как сходить в магахин -смех-"
    "Ой, случайно сказал это в слух"
    "Рядом же никого не было?"
    "Я оглянулся по сторонам, даже назад себя, мало ли кто-то выходил из подъезда в этот момент"
    "Нет. Никого"
    gr "Ну, и слава Богу!"
    "Блять, опять"
    "Не опять, а снова"
    "Да ебанный рот, о чём я думаю"
    "Неужели у меня какие-то прояления шизофрении, или какие там есть ещё болезни"
    "Так все, хватит, проехали"
    "Сейчас ненароком начну спорить сам с собой в голове. Затем загонюсь и сяду в угол"
    "Уточню, в обоссанный угол падика"
    "Ай, всё"
    "Надо выдвигаться"
    "..."
    "Денег было не так уж и много, но это только в ближайшее время"
    "Родители обещали перевести потом ещё немного рублс"
    "Выбор в какой магазин я пойду был скромен, так как мне нужно экономить"
    "Мало ли, будет какая нибудь тусовка, а я без денег..."
    show screen map

label dvlera:
    scene shop2out
    "Пройдя через дворы, я приблизился ещё ближе к своей цели"
    "А именно, к магазину «Двоечка»"
    "Название, конечно, оставляло желать лучшеего, но тут были достаточно хорошие цены"
    "А ещё мой мой любимый лимонад, импорт из Польши «Dr.Depper»"
    "По сути, это обычная кола, но со вкусом вишни"
    "Раньше и у нас такую производили, но по каким-то неизвестным мне причинам, завод приостановил выпуск данного напитка в нашей стране"
    "Польская версия кажется менее газированной, чем наша"
    "Возможно, что это издержки перевозки товара"
    "Вообщем, хуй его знает"
    scene shop2
    hide shop2out
    "Войдя внутрь, я сразу же пошел к морозильникам"
    "Мне очень хотелось наггетсов"
    "Думал, пожарю их с макарошками, а после вместе с майонезом заточу салат, что остался дома"
    "Я пробирался через людей, помещение хоть и было большим, но пространства меж стелажей с товарами были узкими"
    "Все закупались продуктами для поездки. У кого-то угли, мясо, большие упаковки пива... радость вообщем"
    "Вообщем, наггетсов, которые я хотел купить не оказалось в магазине"
    "Они были по скидке и люди раскупили все, что только можно было"
    "Проклятие, я как знал что нужно было идти в другой магазин, заодно и прогулялся бы подольше"
    "Я начал просто шастать по магазину, смотреть чего я хочу, да и что в целом здесь есть"
    "Полка за полкой, холодильник за холодильником"
    "Лимонады, чипсы, бич-пакеты"
    "Все выглядело достаточно интересно"
    "Но с другой стороны, хотелось бы и чего-то более полезного, чем джанка"
    "..."
    "Потихоньку я начал двигаться ближе к кассе"
    "Я встал возле отдела с энергетиками, думал взять баночку, на вечерок этакий"
    "И тут кто-то похлопал меня по-плечу"
    stop music
    play music "audio/shop.mp3"
    lr2 "Молодой человек..."
    gr "А?"
    show lrsprite
    lr2 "Вы обронили кошелёк..."
    "Она протянула мне мой кошелёк"
    "На её месте, я бы просто присвоил его себе"
    "Просто, я бы не догадался, где я его посеял"
    "Так сказать, за всё время, что брожу от дома до магазина, я до него ни разу не докасался"
    gr "Спасибо большое!"
    "Девушка, что стояла рядом со мной, казалась мне немного знакомой"
    "Почему-то всплывало ощущение, что мы уже виделись, и довольно много раз"
    lr2 "ДА ВИДЕЛИСЬ"
    gr "Что?"
    lr2 "Я ничего не говорила"
    "Ой прости да, прости"
    gr "Прос...ти. Да прости"
    lr2 "-смех-"
    lr2 "Ты забавный"
    gr "Да, мне просто послышалось видимо"
    "Мне же не показалось?"
    "Бля, нихуя не понял"
    "Что это только что было? Она ответила мне? На мои мысли?"
    "Наверное бред, просто мысли вверх-дном и все, мозг сам выдал это, типо..."
    "Типо.... эмм..."
    "Не знаю"
    lr2 "Тебя как зовут то?"
    "Гриша"
    gr "Меня зовут Григорий"
    "Прищуривщись и улыбнувшись она ответила:"
    lr "А меня зовут Валерия, рада знакомству с вами!"
    "Официально"
    "Я понял, что она простебала меня только через секунду"
    gr "Эм, слушай, мы не могли с тобой уже где-то видеться?"
    lr "Могли, конечно"
    gr "Оу, значит не показалось"
    gr "А где?"
    lr "А с чего ты вообще взял, что я знаю - улыбнувшись ответила она"
    lr "Это же так, просто сказано, что все возможно"
    gr "А, я тебя понял"
    lr "Догнал, так сказать"
    gr "Да, догнал так сказать"
    "Значит, мы могли и не видеться, ну то есть ни я, ни она не помнит"
    lr "Ладно, шучу я, мы в одном доме живем"
    gr "Тогда это всё меняет, я то и думаю, что лицо знакомое"
    lr "Очередь"
    gr "А?"
    lr "Иди говорю, очередь твоя"
    "Разговорившись с ней, очереди не стало и я стал первым"
    hide lrsprite
    gr "Здравствуйте... Наличкой"
    gr "Вашей карты нет, и пакет пробейте обязательно"
    "..."
    "Оплатив товары, я посмотрел назад, на следующего покупателя"
    "Но это была не Лера"
    "Леры вообще не было в очереди"
    "Я не особо придал этому значение"
    "Встреча, конечно, вышла необычной, ещё и новое знакомство"
    "Она довольно симпатична"
    "..."
    "Я десять раз пожалел, что не взял с собой рюкзак"
    "Ненавижу ходить с пакетами"
    "Это самая главная моя ненависть"
    "Нет, блин, взять и закинуть все на плечи, нужно бросить портфель дома, отдать семь рублей за пакет и потом ходить с ним"
    "А мало ли он порвется?"
    "..."
    hide shop2
    stop music
    scene city
    play music "audio/Al90.mp3"
    "И вот иду я с этим пакетом и думаю, живу я здесь с самого рождения, никогда не переезжал, всё детство провёл во дворе, знакомых полный город"
    "А вот Леру вообще не знаю"
    "Даже никогда не слышал о ней из уст общих друзей"
    "Не отрицаю того, что она переехала сюда совсем недавно"
    "А может судьба так решила, чтобы мы вовсе не пересекались"
    "Только кошелёк мой плевал на всё эти заговоры и планы, разрушив их одним нелепым падением"
    "Стоп, с чего я взял, что нелепым?"
    "Может он круто упал..."
    "Ну экшен там..."
    "..."
    "С другой стороны, я уже давно не выбирался на стрит"
    "Учеба, домашний уют и компьютер"
    "Раньше, я обретал новые знакомства по щелчку пальцев, а главное, что со всеми я легко находил общий язык"
    "А сейчас со мной остались только близкие, и то каждая наша встреча это дегустация новой бутылочки пива, а по праздникам крепкого алкоголя"
    "С последним, я бы даже не сказал, что это дегустация"
    "Просто нажираемся да и всё, ну а что ещё нам делать"
    "Молодость..."
    "Губит ли она меня?"
    "Или оставляет счастливые воспоминания?"
    "Жить в удовольствие, а потом работать ради мечты?"
    "Или наоборот?"
    "Работать ради мечты, а потом жить в удовольствие?"
    "Не знаю, все это сложно"
    "Думаю все зависит от человека, его мотивации и способностей"
    "Мне всегда было страшно осознавать, что в какой-то момент мне придётся перешагнуть ещё одну линию своей жизни, за которой меня встретит ещё более суровая пора"
    "Если говорить точнее, то я продолжаю бояться этого"
    "А ведь остался год с лишним, ещё немного и вот я приближусь к этой линии"
    "Смогу ли я?"
    "Я верю, что да"
    "..."
jump firstdaygohome

label firstdaygohome:
    scene dvor
    hide city
    "На секунду я остановился"
    "Перед моими глазами был двор"
    "Двор моего детства"
    "Именно здесь образовались одни из самых счастливых воспоминаний моего детства"
    "Чего тут только не происходило"
    "Драки, первая любовь, карточные игры"
    "Друзья... из которых лишь пару остались до сих пор со мной"
    "Но сейчас этот двор мертв"
    "Старые скрипучие качели и мусор, разбросанный по всему периметру площадки"
    "Дети здесь больше не гуляют"
    "И вряд ли будут"
    "Скоро здесь построят новые парковочные места для местных жителей, и гулять здесь будут лишь автомобили...."
    "..."
    scene padik
    hide dvor
    "Минут через пять я уже стоял у своего подъезда, ёрзая руками по карманам в попытках найти свои ключи"
    "И знаешь..."
    "Я их даже нашел"
    "Это удивительно... Да..."
    "Я стал открывать дверь подъезда, но резко услышал пронзающий мои уши крик"
    "..."
    "Я начал терять равновесие и пал на землю, не понимаю что мне нужно прикрывать своими руками"
    "Руки держали то голову, то бегали по телу, но не касаясь его"
    "Полная дезориентация и страх, резкие позывы к тошноте"
    "Всё это усугубляли комментарии прохожих, которые я слышал через этот непонятный писк"
    children "Мам, что с ним? Почему он кричит? Давай поможем ему!"
    stopitsnotmymom "Не нужно, Матвей, это наркоман, вот что бывает, если будешь курить всякую дрянь"
    "Они отдалялись, я не знал винить их, или радоваться этому"
    "Я не хотел чтобы люди видели этот позор, но и не хотел умирать"
    "По спине стекали капли холодного пота и всё это подходило к концу"
    "Плавно, но достаточно быстро писклявый крик пропал, а я в тревоге смог овладеть своим телом и начал постепенно подниматься на ноги"
    "Оглянувшись вокруг и отряхнув свою жопу от песка и пыли, я понял что кроме этой семейки меня никто не видел"
    "По крайне мере, больше мне никто не попался на глаза, а те кто могли видеть - не подали виду"
    "Это хорошо"
    "Нет, стоп, нихуя это не хорошо"
    "Мне впервые стало страшно, я не понимал что мне делать"
    "В конечном итоге, я все таки вошёл в подъезд и побежал к себе домой как можно скорее"
    "..."
    scene grroom
    hide city
    "Войдя в квартиру, я легким движением ног сбросил с себя кроссовки и направился в свою комнату"
    "Сев на кровать я начал искать в интернете информацию по этому поводу"
    "Толком ничего полезного найти я не смог"
    "Информация разнилась на каждом ресурсе"
    "Кто-то заявлял о шизофрении, кто-то о сильном переутомлении, в связи с чем появляются галлюцинации"
    "Но все эти сайты объединяло одно - раздел о наркотиках"
    "Но это не могли быть они"
    "В своей жизни максимум, что я употреблял это травка, и то пару раз в своей жизни"
    "Я не стал звонить родителям рассказывая им о том, что произошло"
    "Я очень не хотел, чтобы они возвращались"
    "И чтобы над моим телом был вечный надзор, то есть мышью в клетке"
    "Паралелльно с этим, меня сильно клонило в сон, но я пытался сопротивляться"
    "Возможно это давление, или ещё что-то"
    "Вдруг, я сейчас упаду в обморок и просто умру"
    "Я бы не хотел чтобы меня нашли та..."
    "..."
    stop music
    scene closeeyes
    hide grroom
    play music "audio/HorrorVoice.mp3"
    play music2 "audio/HorrorMusic.mp3"
    lr2 "НЕ БЙСЯ"
    lr2 "ВСЕ БУДТ ХОРОШО"
    gr "Лера?"
    lr "Чего?"
    gr "Это ты?"
    show lrhorror
    play sound "audio/sfx/lera.mp3"
    lr "КОНЕЧНО"
    gr "Господи, что ты такое..."
    lr "Что!?"
    gr "Ты... ты кто такая?"
    lr "Я?"
    lr "Ты уже забыл?"
    hide lrhorror
    scene lrhorrorfull
    play sound "audio/sfx/fear1.mp3"
    lr "Я ЛЕРА"
    gr "Мать твою за ногу, свали отсюда!"
    scene closeeyes
    hide lrhorrorfull
    show lrhorror
    lr "Уже прогоняешь?"
    lr "Ой, смотри"
    lr "Я тебе кое-что покажу!"
    scene twodead
    hide closeeyes
    "..."
    lr "узн4ёшь?"
    gr "Убери... убери это!"
    lr "Правильно, это твои..."
    play sound "audio/sfx/skripka.mp3"
    hide lrhorror
    lr "М4М4 и П4П4"
    gr "Блять"
    stop sound
    "Я могу двигать руками? То есть, я могу двигаться?"
    scene closeeyes
    hide twodead
    "Резким движением я кинулся назад, пытаясь отдалиться от всего этого пиздеца"
    "Казалось, что у меня получается скрыться"
    "Мрак окутывал меня, я не видел своих ног"
    "Здесь было очень холодно, как в проруби зимой"
    "Но тело не сводило, а лишь щекотало"
    "Чей то голос играл без остановки, и говорил пугающие вещи"
    lr "ЧЕЙ?"
    "Похоже, что она не отставала"
    "Или это я попал в петлю..."
    show lrhorror
    play sound "audio/sfx/lera.mp3"
    lr "МОЖЕТ СТОИЛО В ДРУГУЮ СТОРОНУ?"
    lr "А!?"
    hide lrhorror
    "Повернув налево, а вместе с этим чуть не упав, я бежал... бежал как только мог"
    scene noise
    hide close
    "Но постепенно мрак менялся на шумы... да шумы"
    lr "Как в фотошопе?"
    gr "Да. Как в фотошопе"
    gr "Чтобы добавить зернистость в приложении Photoshop, перейдите в раздел Фильтр. Шум. Добавить Шум"
    lr "Мне кажется, тебе достаточно, и так глаза могут лопнуть..."
    "Что, мать его, происходит?"
    "Я не хотел этого говорить!"
    lr "Кстати, я показывала тебе лопнувшие глаза?"
    scene travmaglaz
    hide noise
    lr "Прекрасно, правда?"
    "Нет... Прошу хватит."
    play sound "audio/sfx/stop.mp3"
    lr "ПРОЦЕСС ПРИОСТАНОВЛЕН"
    scene closeeyes
    hide travmaglaz
    stop sound
    gr "Мне... мне тяжело и страшно"
    gr "Пожалуйста, хватит"
    show lrhorror
    play sound "audio/sfx/lera.mp3"
    lr "Ладно, мне правда стало жалко тебя"
    lr "Я вижу как ты страдаешь и убегаешь, не хочешь видеть этого"
    lr "Я понимаю, это больно"
    lr "Но, хочу сказать тебе правду"
    lr "Шутка зашла слишком далеко"
    lr "Один из тех трупов в пакете"
    lr "Это не твоя мама"
    "..."
    play sound "audio/sfx/stop.mp3"
    lr "Это перевернутая женщина"
    scene womanreverse
    hide closeeyes
    "..."
    stop sound
    lr "Почему ты всё ещё дрожишь?"
    lr "Я же сказала, ЭТО ШУТКА"
    lr "Но, доля правды в этом все-таки есть"
    lr "Вторым трупом в мешке был твой папа"
    lr "Но, я не отрицаю того, что перевернутая женщина и есть твоя мама"
    lr "Просто, я её никогда не видела"
    gr "Лера, отпусти меня пожалуйста"
    gr "Я хочу домой, в свою комнату... я хочу домой..."
    scene noise
    hide womanreverse
    lr "СЕГ0ДНЯ ТЫ НЕ ТАКОЙ ЗАБ4ВНЫЙ"
    lr "ИДИ"
    scene mrakdoor
    hide noise
    "Она исчезла, но оставила проход"
    "Он вёл меня из комнаты шумов в очередную комнату со мраком"
    scene closeeyes
    hide mrakdoor
    "И снова холод. Снова пустота. Снова голос"
    "Я слушал, что он говорит, но не мог ничего понять"
    "Это был набор случайных предложений, порой очень пугающих"
    "..."
    "Может так и выглядит смерть?"
    "А это, что то вроде, наказание за все грехи?"
    "Навряд ли, меня даже ещё не определили ни в рай, ни в ад"
    "Зачем так мучить душу... В пустоте"
    "Проверка на стойкость?"
    "Если это была она, то я провалил её"
    "Забавно, если я - душа, как я чувствую себя?"
    "Ну, йорканье сердца, ноги... руки"
    "Да и дышать тяжело."
    "Я всю жизнь думал, что душа бесплодна"
    lr "Так и есть"
    "И снова она здесь"
    stop music
    "Вместе с ней прекратились и голоса"
    lr "Чьи?"
    gr "Этого больного шизофреника"
    lr "Дак, это твой голос"
    gr "Мой?"
    lr "Да, твой"
    lr "Просто ты не замечаешь этого"
    lr "А что у тебя было на уме, этого мне не дано знать"
    lr "Говорил всякий бред, да и бог с ним, бывает и такое"
    gr "Но я же контролировал себя, а того нет..."
    lr "Ты бы не оказался здесь, если бы мог себя контролировать"
    gr "Я до сих пор ничего не понимаю"
    lr "Перестань курить всякую гадость, как ту что утром"
    lr "Я сразу почувствовал, что ты качаешь меня энтеогенами"
    gr "Всмысле?"
    lr "Спайса меньше кури, вот что..."
    gr "Но я никогда не курил спайс"
    gr "Подожди, так ты... это..."
    lr "Тебе пора, Гриша"
    lr "Нам пора..."
    scene quitdoor
    hide closeeyes
    stop music2
    "За моей спиной открылась яркая белая дверь"
    "Не успев закончить свой вопрос, Лера... ну или я, толкнули меня в проъём и я полетел..."
    "Так ты это я?"
    "..."
    gr "Так ты это я?"
    scene openeyes
    hide quitdoor
    lr "Гриша, не рановато ли?"
    play music "audio/chillout.mp3"
    scene inpadik
    show lrsprite
    hide openeyes
    "Над до мной была Лера, она смотрела в окно подъезда и видя, что я очнулся слегка улыбнулась"
    "К слову, на улице уже был вечер"
    gr "В подъезде?"
    lr "Ага. Хорошо, хоть не на улице где-то"
    "Я оглянул себя и её. Она была одета так же, как и при нашей последней встрече"
    lr "Гриша, хоть мы и не знакомцы друг для друга, но завязывай"
    lr "Ксюша говорила о тебе только хорошие вещи, не подставляй её"
    gr "Какая ещё Ксюша?"
    "К этому вопросу я уже полноценно встал на ноги"
    lr "Ксюша Перова, ну... одноклассница твоя"
    gr "Вы знакомы... я удивлён"
    gr "Ну, не прям совсем удивлён, но ты поняла"
    lr "Конечно"
    "Вокруг неё лежали бычки сигарет, некоторые из которых по прежнему дымились"
    gr "Меня лечишь и сама куришь?"
    lr "И я не без греха... но все таки это не наркота"
    "Я промолчал, но жестом показал, что тоже бы не отказался от сигареты и зажигалки."
    lr "Стоит ли?"
    gr "Не знаю сейчас и проверим"
    "Она посмотрела на меня с риском и легким недопониманием"
    lr "Ты забавный"
    gr "Спасибо..."
    hide lrsprite
    "Оставшиеся пять минут мы просто курили и смотрели в окно подъезда"
    "На ту самую котельную и подсдутые резиновые мячики"
    "Под конец, я спросил нужно ли её проводить, на что оказалось, что она живет этажом выше"
    "Я пытался придумать для неё отмазки, почему её так долго не было дома, на что узнал, что она тоже живет одна. Уже несколько лет"
    "Её родители погибли, а она живет квартире бабушки, которая досталась ей по наследству"
    "В конце, я дважды сказал ей спасибо. За то, что была рядом и за сигарету"
    "..."
    scene grroomnight
    hide inpadik
    "В остальном день заканчивался спокойно"
    "Я посидел ещё пару часов в комнате, осознавая какой пиздец произошел сегодня, и как такое могло произойти"
    "Ответ, я все-таки нашел"
    "Спасибо Тохе, и его чудо сигарете, которую он судя по всему положил мне в пачку, с тусовки двумя днями ранее"
    "Никогда раньше не мог подумать, что смерть может быть так близко"
    "А ещё что хуже, настать в самый не предсказуемый момент"
    "Спасибо, за то, что я все ещё здесь"
    scene closeeyes
    hide inpadik
    "Спокойной ночи."