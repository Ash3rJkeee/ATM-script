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
            def __init__(self, t1, t2, p1, p2, g, gp=None):
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

hf.rts_240 = hf.HeatSource(
    ta=find_param_by_id(dumps=dumps, id=2312494),
    t1=find_param_by_id(dumps=dumps, id=2312568),
    t2=find_param_by_id(dumps=dumps, id=2312570),
    p1=find_param_by_id(dumps=dumps, id=2312576),
    p2=find_param_by_id(dumps=dumps, id=2312578),
    g=find_param_by_id(dumps=dumps, id=2312546),
)
