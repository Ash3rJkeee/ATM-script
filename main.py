import requests
import json

URL = "http://tsk-mosenergo.1sim.online:81"
URL_TO_GET_TOKEN = f"{URL}/api2/auth/open"
URL_TO_GET_COMPANIES = f"{URL}/api2/company"
URL_TO_GET_VALUES = f"{URL}/api2/values"


class Branch:
    class HeatSource:
        """Класс описания источника теплоснабжения"""
        def __init__(self, ta=None, t1=None, t2=None, p1=None, p2=None, g=None, gp=None):
            self.ta = ta
            self.t1 = t1
            self.t2 = t2
            self.p1 = p1
            self.p2 = p2
            self.g = g
            self.gp = gp

        class Pipe:
            """Класс описания вывода источника"""
            def __init__(self,  t1, t2, p1, p2, g, ta=None, gp=None):
                self.ta = ta
                self.t1 = t1
                self.t2 = t2
                self.p1 = p1
                self.p2 = p2
                self.g = g
                self.gp = gp


def find_param_by_id(dumps: json, id: int):
    """Ищет значение параметра в json по его id """
    for dump_object in dumps:
        if dump_object["id"] == id:
            return dump_object["val"]


payload = {
  "login": "a.ryadinskih@tsk-mosenergo.ru",
  "password": "Sfrffccc2511"
}

# Получение токена на доступ к API
response = requests.post(url=URL_TO_GET_TOKEN, params=payload)
token = response.json()["token"]
# print(token)

headers = {
    "Authorization": f"Bearer {token}",
}
# передача данных из файла запроса в параметр "payload" строки запроса
with open('request.txt', "r") as file:
    payload = file.read()

# получение ответа от сервера АТМ
response = requests.get(URL_TO_GET_VALUES, headers=headers, data=payload)

# print(json.dumps(response.json()[2], ensure_ascii=False, sort_keys=True, indent=2))

# запись ответа от сервера в тхт файл
with open('response.txt', 'w') as file:
    json.dump(response.json(), file, ensure_ascii=False, sort_keys=True, indent=2)

dumps = json.loads(response.text)
# print(json_find_param_by_id(dumps=dumps, id=1113025))

zf = Branch()
hf = Branch()
ef = Branch()
pf = Branch()
sf = Branch()

# Зеленоградский филиал РТС-1
zf.rts_1 = zf.HeatSource(ta=find_param_by_id(dumps=dumps, id=2288272))
zf.rts_1.pipe_1 = zf.rts_1.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2289146),
    t2=find_param_by_id(dumps=dumps, id=2289148),
    p1=find_param_by_id(dumps=dumps, id=2289156),
    p2=find_param_by_id(dumps=dumps, id=2289158),
    g=find_param_by_id(dumps=dumps, id=2289134),
)

zf.rts_1.pipe_2 = zf.rts_1.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2288342),
    t2=find_param_by_id(dumps=dumps, id=2288344),
    p1=find_param_by_id(dumps=dumps, id=2288352),
    p2=find_param_by_id(dumps=dumps, id=2288354),
    g=find_param_by_id(dumps=dumps, id=2288330),
)

# Зеленоградский филиал РТС-2
zf.rts_2 = zf.HeatSource(ta=find_param_by_id(dumps=dumps, id=2289886))
zf.rts_2.pipe_1 = zf.rts_2.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2289952),
    t2=find_param_by_id(dumps=dumps, id=2289954),
    p1=find_param_by_id(dumps=dumps, id=2289962),
    p2=find_param_by_id(dumps=dumps, id=2289964),
    g=find_param_by_id(dumps=dumps, id=2289940),
)

zf.rts_2.pipe_2 = zf.rts_2.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2290760),
    t2=find_param_by_id(dumps=dumps, id=2290762),
    p1=find_param_by_id(dumps=dumps, id=2290770),
    p2=find_param_by_id(dumps=dumps, id=2290772),
    g=find_param_by_id(dumps=dumps, id=2290748),
)

zf.rts_2.pipe_3 = zf.rts_2.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2291564),
    t2=find_param_by_id(dumps=dumps, id=2291566),
    p1=find_param_by_id(dumps=dumps, id=2291574),
    p2=find_param_by_id(dumps=dumps, id=2291576),
    g=find_param_by_id(dumps=dumps, id=2291552),
)

# Зеленоградский филиал РТС-3
zf.rts_3 = zf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2226554),
    t1=find_param_by_id(dumps=dumps, id=2275588),
    t2=find_param_by_id(dumps=dumps, id=2275618),
    p1=find_param_by_id(dumps=dumps, id=2275604),
    p2=find_param_by_id(dumps=dumps, id=2275628),
    g=find_param_by_id(dumps=dumps, id=2275614),
)

# Зеленоградский филиал РТС-4
zf.rts_4 = zf.HeatSource(ta=find_param_by_id(dumps=dumps, id=2293106))

zf.rts_4.pipe_1 = zf.rts_4.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2293172),
    t2=find_param_by_id(dumps=dumps, id=2293174),
    p1=find_param_by_id(dumps=dumps, id=2293182),
    p2=find_param_by_id(dumps=dumps, id=2293184),
    g=find_param_by_id(dumps=dumps, id=2293160),
)

zf.rts_4.pipe_2 = zf.rts_4.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2292368),
    t2=find_param_by_id(dumps=dumps, id=2292370),
    p1=find_param_by_id(dumps=dumps, id=2292378),
    p2=find_param_by_id(dumps=dumps, id=2292380),
    g=find_param_by_id(dumps=dumps, id=2292356),
)

zf.rts_4.pipe_3 = zf.rts_4.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2293976),
    t2=find_param_by_id(dumps=dumps, id=2293978),
    p1=find_param_by_id(dumps=dumps, id=2293986),
    p2=find_param_by_id(dumps=dumps, id=2293988),
    g=find_param_by_id(dumps=dumps, id=2293964),
)

# ХФ РТС-240
hf.rts_240 = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2312494),
    t1=find_param_by_id(dumps=dumps, id=2312568),
    t2=find_param_by_id(dumps=dumps, id=2312570),
    p1=find_param_by_id(dumps=dumps, id=2312576),
    p2=find_param_by_id(dumps=dumps, id=2312578),
    g=find_param_by_id(dumps=dumps, id=2312546),
)

# ХФ КТС-Лавочкина
hf.kts_lavochkina = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1112949),
    t1=find_param_by_id(dumps=dumps, id=1113025),
    t2=find_param_by_id(dumps=dumps, id=1113040),
    p1=find_param_by_id(dumps=dumps, id=1113026),
    p2=find_param_by_id(dumps=dumps, id=1113041),
    g=find_param_by_id(dumps=dumps, id=1113028),
    gp=find_param_by_id(dumps=dumps, id=1845173),
)

# ХФ КТС-Кольцевая
hf.kts_kolcevaya = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1115461),
    t1=find_param_by_id(dumps=dumps, id=1115537),
    t2=find_param_by_id(dumps=dumps, id=1115552),
    p1=find_param_by_id(dumps=dumps, id=1115538),
    p2=find_param_by_id(dumps=dumps, id=1115553),
    g=find_param_by_id(dumps=dumps, id=1115540),
    gp=find_param_by_id(dumps=dumps, id=1840894),
)

# ХФ КТС-Мичурина
hf.kts_michurina = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1112351),
    t1=find_param_by_id(dumps=dumps, id=1112313),
    t2=find_param_by_id(dumps=dumps, id=1112314),
    p1=find_param_by_id(dumps=dumps, id=1112317),
    p2=find_param_by_id(dumps=dumps, id=1112318),
    g=find_param_by_id(dumps=dumps, id=1112319)
)

# ХФ КТС-Октябрьская
hf.kts_oktyabrskaya = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2129258),
    t1=find_param_by_id(dumps=dumps, id=2129272),
    t2=find_param_by_id(dumps=dumps, id=2129273),
    p1=find_param_by_id(dumps=dumps, id=2129270),
    p2=find_param_by_id(dumps=dumps, id=2129271),
    g=find_param_by_id(dumps=dumps, id=2129269)
)

# ХФ КТС-Банный
hf.kts_bannyi = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1859393),
    t1=find_param_by_id(dumps=dumps, id=1859469),
    t2=find_param_by_id(dumps=dumps, id=1859484),
    p1=find_param_by_id(dumps=dumps, id=1859470),
    p2=find_param_by_id(dumps=dumps, id=1859485),
    g=find_param_by_id(dumps=dumps, id=1859472)
)

# ХФ КТС-Мира
hf.kts_mira = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1005770),
    t1=find_param_by_id(dumps=dumps, id=1005775),
    t2=find_param_by_id(dumps=dumps, id=1005776),
    p1=find_param_by_id(dumps=dumps, id=1005782),
    p2=find_param_by_id(dumps=dumps, id=1005783),
    g=find_param_by_id(dumps=dumps, id=1005772)
)

# ХФ КТС-Фрунзе
hf.kts_frunze = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2314872)
)

# ХФ КТС-Речная
hf.kts_rechnaya = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=1864136),
    t1=find_param_by_id(dumps=dumps, id=1864141),
    t2=find_param_by_id(dumps=dumps, id=1864142),
    p1=find_param_by_id(dumps=dumps, id=1864148),
    p2=find_param_by_id(dumps=dumps, id=1864149),
    g=find_param_by_id(dumps=dumps, id=1864138)
)

# Электрогорский фиилал
ef.gres_3 = ef.HeatSource()

ef.gres_3.el_nip = ef.gres_3.Pipe(
    t1=find_param_by_id(dumps=dumps, id=2244106),
    t2=find_param_by_id(dumps=dumps, id=2244108),
    p1=find_param_by_id(dumps=dumps, id=2244086),
    p2=find_param_by_id(dumps=dumps, id=2244090),
    g=find_param_by_id(dumps=dumps, id=2244046),
)

ef.gres_3.el_nip = ef.gres_3.Pipe(
    ta=find_param_by_id(dumps=dumps, id=2244010),
    t1=find_param_by_id(dumps=dumps, id=2244106),
    t2=find_param_by_id(dumps=dumps, id=2244108),
    p1=find_param_by_id(dumps=dumps, id=2244086),
    p2=find_param_by_id(dumps=dumps, id=2244090),
    g=find_param_by_id(dumps=dumps, id=2244046),
)

ef.gres_3.g_1 = ef.gres_3.Pipe(
    ta=find_param_by_id(dumps=dumps, id=2242826),
    t1=find_param_by_id(dumps=dumps, id=2242908),
    t2=find_param_by_id(dumps=dumps, id=2242910),
    p1=find_param_by_id(dumps=dumps, id=2242888),
    p2=find_param_by_id(dumps=dumps, id=2242892),
    g=find_param_by_id(dumps=dumps, id=2242862),
)

ef.gres_3.g_2 = ef.gres_3.Pipe(
    ta=find_param_by_id(dumps=dumps, id=2243522),
    t1=find_param_by_id(dumps=dumps, id=2243618),
    t2=find_param_by_id(dumps=dumps, id=2243620),
    p1=find_param_by_id(dumps=dumps, id=2243598),
    p2=find_param_by_id(dumps=dumps, id=2243602),
    g=find_param_by_id(dumps=dumps, id=2243558),
)

ef.gres_3.l_1 = ef.gres_3.Pipe(
    ta=find_param_by_id(dumps=dumps, id=2228460),
    t1=find_param_by_id(dumps=dumps, id=2228556),
    t2=find_param_by_id(dumps=dumps, id=2228558),
    p1=find_param_by_id(dumps=dumps, id=2228536),
    p2=find_param_by_id(dumps=dumps, id=2228540),
    g=find_param_by_id(dumps=dumps, id=2228496),
)

ef.gres_3.s_1 = ef.gres_3.Pipe(
    ta=find_param_by_id(dumps=dumps, id=2243766),
    t1=find_param_by_id(dumps=dumps, id=2243862),
    t2=find_param_by_id(dumps=dumps, id=2243864),
    p1=find_param_by_id(dumps=dumps, id=2243842),
    p2=find_param_by_id(dumps=dumps, id=2243846),
    g=find_param_by_id(dumps=dumps, id=2243802),
)

# ПФ КТС-Отрадное
pf.kts_otradnoe = pf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2305740),
    t1=find_param_by_id(dumps=dumps, id=2305806),
    t2=find_param_by_id(dumps=dumps, id=2305808),
    p1=find_param_by_id(dumps=dumps, id=2305816),
    p2=find_param_by_id(dumps=dumps, id=2305818),
    g=find_param_by_id(dumps=dumps, id=2305794),
)

