__copyright__ = "Copyright (C) 2020 Nidhal Baccouri"


OPEN_AI_ENV_VAR = "OPEN_API_KEY"
DEEPL_ENV_VAR = "DEEPL_API_KEY"
LIBRE_ENV_VAR = "LIBRE_API_KEY"
MSFT_ENV_VAR = "MICROSOFT_API_KEY"
QCRI_ENV_VAR = "QCRI_API_KEY"
YANDEX_ENV_VAR = "YANDEX_API_KEY"
TENCENT_SECRET_ID_ENV_VAR = "TENCENT_SECRET_ID"
TENCENT_SECRET_KEY_ENV_VAR = "TENCENT_SECRET_KEY"
BAIDU_APPID_ENV_VAR = "BAIDU_APPID"
BAIDU_APPKEY_ENV_VAR = "BAIDU_APPKEY"


BASE_URLS = {
    "GOOGLE_TRANSLATE": "https://translate.google.com/m",
    "PONS": "https://en.pons.com/translate/",
    #"YANDEX": "https://translate.yandex.net/api/{version}/tr.json/{endpoint}",
    "YANDEX": "https://translate.api.cloud.yandex.net/translate",
    "LINGUEE": "https://www.linguee.com/",
    "MYMEMORY": "http://api.mymemory.translated.net/get",
    "QCRI": "https://mt.qcri.org/api/v1/{endpoint}?",
    "DEEPL": "https://api.deepl.com/{version}/",
    "DEEPL_FREE": "https://api-free.deepl.com/{version}/",
    "MICROSOFT_TRANSLATE": "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0",
    "PAPAGO": "https://papago.naver.com/",
    "PAPAGO_API": "https://openapi.naver.com/v1/papago/n2mt",
    "LIBRE": "https://libretranslate.com/",
    "LIBRE_FREE": "https://libretranslate.de/",
    "TENENT": "https://tmt.tencentcloudapi.com",
    "BAIDU": "https://fanyi-api.baidu.com/api/trans/vip/translate",
}

GOOGLE_LANGUAGES_TO_CODES = {
    "afrikaans": "af",
    "albanian": "sq",
    "amharic": "am",
    "arabic": "ar",
    "armenian": "hy",
    "assamese": "as",
    "aymara": "ay",
    "azerbaijani": "az",
    "bambara": "bm",
    "basque": "eu",
    "belarusian": "be",
    "bengali": "bn",
    "bhojpuri": "bho",
    "bosnian": "bs",
    "bulgarian": "bg",
    "catalan": "ca",
    "cebuano": "ceb",
    "chichewa": "ny",
    "chinese (simplified)": "zh-CN",
    "chinese (traditional)": "zh-TW",
    "corsican": "co",
    "croatian": "hr",
    "czech": "cs",
    "danish": "da",
    "dhivehi": "dv",
    "dogri": "doi",
    "dutch": "nl",
    "english": "en",
    "esperanto": "eo",
    "estonian": "et",
    "ewe": "ee",
    "filipino": "tl",
    "finnish": "fi",
    "french": "fr",
    "frisian": "fy",
    "galician": "gl",
    "georgian": "ka",
    "german": "de",
    "greek": "el",
    "guarani": "gn",
    "gujarati": "gu",
    "haitian creole": "ht",
    "hausa": "ha",
    "hawaiian": "haw",
    "hebrew": "iw",
    "hindi": "hi",
    "hmong": "hmn",
    "hungarian": "hu",
    "icelandic": "is",
    "igbo": "ig",
    "ilocano": "ilo",
    "indonesian": "id",
    "irish": "ga",
    "italian": "it",
    "japanese": "ja",
    "javanese": "jw",
    "kannada": "kn",
    "kazakh": "kk",
    "khmer": "km",
    "kinyarwanda": "rw",
    "konkani": "gom",
    "korean": "ko",
    "krio": "kri",
    "kurdish (kurmanji)": "ku",
    "kurdish (sorani)": "ckb",
    "kyrgyz": "ky",
    "lao": "lo",
    "latin": "la",
    "latvian": "lv",
    "lingala": "ln",
    "lithuanian": "lt",
    "luganda": "lg",
    "luxembourgish": "lb",
    "macedonian": "mk",
    "maithili": "mai",
    "malagasy": "mg",
    "malay": "ms",
    "malayalam": "ml",
    "maltese": "mt",
    "maori": "mi",
    "marathi": "mr",
    "meiteilon (manipuri)": "mni-Mtei",
    "mizo": "lus",
    "mongolian": "mn",
    "myanmar": "my",
    "nepali": "ne",
    "norwegian": "no",
    "odia (oriya)": "or",
    "oromo": "om",
    "pashto": "ps",
    "persian": "fa",
    "polish": "pl",
    "portuguese": "pt",
    "punjabi": "pa",
    "quechua": "qu",
    "romanian": "ro",
    "russian": "ru",
    "samoan": "sm",
    "sanskrit": "sa",
    "scots gaelic": "gd",
    "sepedi": "nso",
    "serbian": "sr",
    "sesotho": "st",
    "shona": "sn",
    "sindhi": "sd",
    "sinhala": "si",
    "slovak": "sk",
    "slovenian": "sl",
    "somali": "so",
    "spanish": "es",
    "sundanese": "su",
    "swahili": "sw",
    "swedish": "sv",
    "tajik": "tg",
    "tamil": "ta",
    "tatar": "tt",
    "telugu": "te",
    "thai": "th",
    "tigrinya": "ti",
    "tsonga": "ts",
    "turkish": "tr",
    "turkmen": "tk",
    "twi": "ak",
    "ukrainian": "uk",
    "urdu": "ur",
    "uyghur": "ug",
    "uzbek": "uz",
    "vietnamese": "vi",
    "welsh": "cy",
    "xhosa": "xh",
    "yiddish": "yi",
    "yoruba": "yo",
    "zulu": "zu",
}

PONS_CODES_TO_LANGUAGES = {
    "ar": "arabic",
    "bg": "bulgarian",
    "zh-cn": "chinese",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "fr": "french",
    "de": "german",
    "el": "greek",
    "hu": "hungarian",
    "it": "italian",
    "la": "latin",
    "no": "norwegian",
    "pl": "polish",
    "pt": "portuguese",
    "ru": "russian",
    "sl": "slovenian",
    "es": "spanish",
    "sv": "swedish",
    "tr": "turkish",
    "elv": "elvish",
}

LINGUEE_LANGUAGES_TO_CODES = {
    "maltese": "maltese",
    "english": "english",
    "german": "german",
    "bulgarian": "bulgarian",
    "polish": "polish",
    "portuguese": "portuguese",
    "hungarian": "hungarian",
    "romanian": "romanian",
    "russian": "russian",
    # "serbian": "sr",
    "dutch": "dutch",
    "slovakian": "slovakian",
    "greek": "greek",
    "slovenian": "slovenian",
    "danish": "danish",
    "italian": "italian",
    "spanish": "spanish",
    "finnish": "finnish",
    "chinese": "chinese",
    "french": "french",
    # "croatian": "hr",
    "czech": "czech",
    "laotian": "laotian",
    "swedish": "swedish",
    "latvian": "latvian",
    "estonian": "estonian",
    "japanese": "japanese",
}

MY_MEMORY_LANGUAGES_TO_CODES = {
    "acehnese": "ace-ID",
    "afrikaans": "af-ZA",
    "akan": "ak-GH",
    "albanian": "sq-AL",
    "amharic": "am-ET",
    "antigua and barbuda creole english": "aig-AG",
    "arabic": "ar-SA",
    "arabic egyptian": "ar-EG",
    "aragonese": "an-ES",
    "armenian": "hy-AM",
    "assamese": "as-IN",
    "asturian": "ast-ES",
    "austrian german": "de-AT",
    "awadhi": "awa-IN",
    "ayacucho quechua": "quy-PE",
    "azerbaijani": "az-AZ",
    "bahamas creole english": "bah-BS",
    "bajan": "bjs-BB",
    "balinese": "ban-ID",
    "balkan gipsy": "rm-RO",
    "bambara": "bm-ML",
    "banjar": "bjn-ID",
    "bashkir": "ba-RU",
    "basque": "eu-ES",
    "belarusian": "be-BY",
    "belgian french": "fr-BE",
    "bemba": "bem-ZM",
    "bengali": "bn-IN",
    "bhojpuri": "bho-IN",
    "bihari": "bh-IN",
    "bislama": "bi-VU",
    "borana": "gax-KE",
    "bosnian": "bs-BA",
    "bosnian (cyrillic)": "bs-Cyrl-BA",
    "breton": "br-FR",
    "buginese": "bug-ID",
    "bulgarian": "bg-BG",
    "burmese": "my-MM",
    "catalan": "ca-ES",
    "catalan valencian": "cav-ES",
    "cebuano": "ceb-PH",
    "central atlas tamazight": "tzm-MA",
    "central aymara": "ayr-BO",
    "central kanuri (latin script)": "knc-NG",
    "chadian arabic": "shu-TD",
    "chamorro": "ch-GU",
    "cherokee": "chr-US",
    "chhattisgarhi": "hne-IN",
    "chinese simplified": "zh-CN",
    "chinese trad. (hong kong)": "zh-HK",
    "chinese traditional": "zh-TW",
    "chinese traditional macau": "zh-MO",
    "chittagonian": "ctg-BD",
    "chokwe": "cjk-AO",
    "classical greek": "grc-GR",
    "comorian ngazidja": "zdj-KM",
    "coptic": "cop-EG",
    "crimean tatar": "crh-RU",
    "crioulo upper guinea": "pov-GW",
    "croatian": "hr-HR",
    "czech": "cs-CZ",
    "danish": "da-DK",
    "dari": "prs-AF",
    "dimli": "diq-TR",
    "dutch": "nl-NL",
    "dyula": "dyu-CI",
    "dzongkha": "dz-BT",
    "eastern yiddish": "ydd-US",
    "emakhuwa": "vmw-MZ",
    "english": "en-GB",
    "english australia": "en-AU",
    "english canada": "en-CA",
    "english india": "en-IN",
    "english ireland": "en-IE",
    "english new zealand": "en-NZ",
    "english singapore": "en-SG",
    "english south africa": "en-ZA",
    "english us": "en-US",
    "esperanto": "eo-EU",
    "estonian": "et-EE",
    "ewe": "ee-GH",
    "fanagalo": "fn-FNG",
    "faroese": "fo-FO",
    "fijian": "fj-FJ",
    "filipino": "fil-PH",
    "finnish": "fi-FI",
    "flemish": "nl-BE",
    "fon": "fon-BJ",
    "french": "fr-FR",
    "french canada": "fr-CA",
    "french swiss": "fr-CH",
    "friulian": "fur-IT",
    "fula": "ff-FUL",
    "galician": "gl-ES",
    "gamargu": "mfi-NG",
    "garo": "grt-IN",
    "georgian": "ka-GE",
    "german": "de-DE",
    "gilbertese": "gil-KI",
    "glavda": "glw-NG",
    "greek": "el-GR",
    "grenadian creole english": "gcl-GD",
    "guarani": "gn-PY",
    "gujarati": "gu-IN",
    "guyanese creole english": "gyn-GY",
    "haitian creole french": "ht-HT",
    "halh mongolian": "khk-MN",
    "hausa": "ha-NE",
    "hawaiian": "haw-US",
    "hebrew": "he-IL",
    "higi": "hig-NG",
    "hiligaynon": "hil-PH",
    "hill mari": "mrj-RU",
    "hindi": "hi-IN",
    "hmong": "hmn-CN",
    "hungarian": "hu-HU",
    "icelandic": "is-IS",
    "igbo ibo": "ibo-NG",
    "igbo ig": "ig-NG",
    "ilocano": "ilo-PH",
    "indonesian": "id-ID",
    "inuktitut greenlandic": "kl-GL",
    "irish gaelic": "ga-IE",
    "italian": "it-IT",
    "italian swiss": "it-CH",
    "jamaican creole english": "jam-JM",
    "japanese": "ja-JP",
    "javanese": "jv-ID",
    "jingpho": "kac-MM",
    "k'iche'": "quc-GT",
    "kabiyè": "kbp-TG",
    "kabuverdianu": "kea-CV",
    "kabylian": "kab-DZ",
    "kalenjin": "kln-KE",
    "kamba": "kam-KE",
    "kannada": "kn-IN",
    "kanuri": "kr-KAU",
    "karen": "kar-MM",
    "kashmiri (devanagari script)": "ks-IN",
    "kashmiri (arabic script)": "kas-IN",
    "kazakh": "kk-KZ",
    "khasi": "kha-IN",
    "khmer": "km-KH",
    "kikuyu kik": "kik-KE",
    "kikuyu ki": "ki-KE",
    "kimbundu": "kmb-AO",
    "kinyarwanda": "rw-RW",
    "kirundi": "rn-BI",
    "kisii": "guz-KE",
    "kongo": "kg-CG",
    "konkani": "kok-IN",
    "korean": "ko-KR",
    "northern kurdish": "kmr-TR",
    "kurdish sorani": "ckb-IQ",
    "kyrgyz": "ky-KG",
    "lao": "lo-LA",
    "latgalian": "ltg-LV",
    "latin": "la-XN",
    "latvian": "lv-LV",
    "ligurian": "lij-IT",
    "limburgish": "li-NL",
    "lingala": "ln-LIN",
    "lithuanian": "lt-LT",
    "lombard": "lmo-IT",
    "luba-kasai": "lua-CD",
    "luganda": "lg-UG",
    "luhya": "luy-KE",
    "luo": "luo-KE",
    "luxembourgish": "lb-LU",
    "maa": "mas-KE",
    "macedonian": "mk-MK",
    "magahi": "mag-IN",
    "maithili": "mai-IN",
    "malagasy": "mg-MG",
    "malay": "ms-MY",
    "malayalam": "ml-IN",
    "maldivian": "dv-MV",
    "maltese": "mt-MT",
    "mandara": "mfi-CM",
    "manipuri": "mni-IN",
    "manx gaelic": "gv-IM",
    "maori": "mi-NZ",
    "marathi": "mr-IN",
    "margi": "mrt-NG",
    "mari": "mhr-RU",
    "marshallese": "mh-MH",
    "mende": "men-SL",
    "meru": "mer-KE",
    "mijikenda": "nyf-KE",
    "minangkabau": "min-ID",
    "mizo": "lus-IN",
    "mongolian": "mn-MN",
    "montenegrin": "sr-ME",
    "morisyen": "mfe-MU",
    "moroccan arabic": "ar-MA",
    "mossi": "mos-BF",
    "ndau": "ndc-MZ",
    "ndebele": "nr-ZA",
    "nepali": "ne-NP",
    "nigerian fulfulde": "fuv-NG",
    "niuean": "niu-NU",
    "north azerbaijani": "azj-AZ",
    "sesotho": "nso-ZA",
    "northern uzbek": "uzn-UZ",
    "norwegian bokmål": "nb-NO",
    "norwegian nynorsk": "nn-NO",
    "nuer": "nus-SS",
    "nyanja": "ny-MW",
    "occitan": "oc-FR",
    "occitan aran": "oc-ES",
    "odia": "or-IN",
    "oriya": "ory-IN",
    "urdu": "ur-PK",
    "palauan": "pau-PW",
    "pali": "pi-IN",
    "pangasinan": "pag-PH",
    "papiamentu": "pap-CW",
    "pashto": "ps-PK",
    "persian": "fa-IR",
    "pijin": "pis-SB",
    "plateau malagasy": "plt-MG",
    "polish": "pl-PL",
    "portuguese": "pt-PT",
    "portuguese brazil": "pt-BR",
    "potawatomi": "pot-US",
    "punjabi": "pa-IN",
    "punjabi (pakistan)": "pnb-PK",
    "quechua": "qu-PE",
    "rohingya": "rhg-MM",
    "rohingyalish": "rhl-MM",
    "romanian": "ro-RO",
    "romansh": "roh-CH",
    "rundi": "run-BI",
    "russian": "ru-RU",
    "saint lucian creole french": "acf-LC",
    "samoan": "sm-WS",
    "sango": "sg-CF",
    "sanskrit": "sa-IN",
    "santali": "sat-IN",
    "sardinian": "sc-IT",
    "scots gaelic": "gd-GB",
    "sena": "seh-ZW",
    "serbian cyrillic": "sr-Cyrl-RS",
    "serbian latin": "sr-Latn-RS",
    "seselwa creole french": "crs-SC",
    "setswana (south africa)": "tn-ZA",
    "shan": "shn-MM",
    "shona": "sn-ZW",
    "sicilian": "scn-IT",
    "silesian": "szl-PL",
    "sindhi snd": "snd-PK",
    "sindhi sd": "sd-PK",
    "sinhala": "si-LK",
    "slovak": "sk-SK",
    "slovenian": "sl-SI",
    "somali": "so-SO",
    "sotho southern": "st-LS",
    "south azerbaijani": "azb-AZ",
    "southern pashto": "pbt-PK",
    "southwestern dinka": "dik-SS",
    "spanish": "es-ES",
    "spanish argentina": "es-AR",
    "spanish colombia": "es-CO",
    "spanish latin america": "es-419",
    "spanish mexico": "es-MX",
    "spanish united states": "es-US",
    "sranan tongo": "srn-SR",
    "standard latvian": "lvs-LV",
    "standard malay": "zsm-MY",
    "sundanese": "su-ID",
    "swahili": "sw-KE",
    "swati": "ss-SZ",
    "swedish": "sv-SE",
    "swiss german": "de-CH",
    "syriac (aramaic)": "syc-TR",
    "tagalog": "tl-PH",
    "tahitian": "ty-PF",
    "tajik": "tg-TJ",
    "tamashek (tuareg)": "tmh-DZ",
    "tamasheq": "taq-ML",
    "tamil india": "ta-IN",
    "tamil sri lanka": "ta-LK",
    "taroko": "trv-TW",
    "tatar": "tt-RU",
    "telugu": "te-IN",
    "tetum": "tet-TL",
    "thai": "th-TH",
    "tibetan": "bo-CN",
    "tigrinya": "ti-ET",
    "tok pisin": "tpi-PG",
    "tokelauan": "tkl-TK",
    "tongan": "to-TO",
    "tosk albanian": "als-AL",
    "tsonga": "ts-ZA",
    "tswa": "tsc-MZ",
    "tswana": "tn-BW",
    "tumbuka": "tum-MW",
    "turkish": "tr-TR",
    "turkmen": "tk-TM",
    "tuvaluan": "tvl-TV",
    "twi": "tw-GH",
    "udmurt": "udm-RU",
    "ukrainian": "uk-UA",
    "uma": "ppk-ID",
    "umbundu": "umb-AO",
    "uyghur uig": "uig-CN",
    "uyghur ug": "ug-CN",
    "uzbek": "uz-UZ",
    "venetian": "vec-IT",
    "vietnamese": "vi-VN",
    "vincentian creole english": "svc-VC",
    "virgin islands creole english": "vic-US",
    "wallisian": "wls-WF",
    "waray (philippines)": "war-PH",
    "welsh": "cy-GB",
    "west central oromo": "gaz-ET",
    "western persian": "pes-IR",
    "wolof": "wo-SN",
    "xhosa": "xh-ZA",
    "yiddish": "yi-YD",
    "yoruba": "yo-NG",
    "zulu": "zu-ZA",
}

DEEPL_LANGUAGE_TO_CODE = {
    "bulgarian": "bg",
    "czech": "cs",
    "danish": "da",
    "german": "de",
    "greek": "el",
    "english": "en",
    "spanish": "es",
    "estonian": "et",
    "finnish": "fi",
    "french": "fr",
    "hungarian": "hu",
    "indonesian": "id",
    "italian": "it",
    "japanese": "ja",
    "korean": "ko",
    "lithuanian": "lt",
    "latvian": "lv",
    "Norwegian": "no",
    "dutch": "nl",
    "polish": "pl",
    "portuguese": "pt",
    "romanian": "ro",
    "russian": "ru",
    "slovak": "sk",
    "slovenian": "sl",
    "swedish": "sv",
    "turkish": "tr",
    "ukrainian": "uk",
    "chinese": "zh",
}

PAPAGO_LANGUAGE_TO_CODE = {
    "ko": "Korean",
    "en": "English",
    "ja": "Japanese",
    "zh-CN": "Chinese",
    "zh-TW": "Chinese traditional",
    "es": "Spanish",
    "fr": "French",
    "vi": "Vietnamese",
    "th": "Thai",
    "id": "Indonesia",
}

QCRI_LANGUAGE_TO_CODE = {"Arabic": "ar", "English": "en", "Spanish": "es"}

LIBRE_LANGUAGES_TO_CODES = {
    "English": "en",
    "Arabic": "ar",
    "Chinese": "zh",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Turkish": "tr",
    "Vietnamese": "vi",
}

TENCENT_LANGUAGE_TO_CODE = {
    "arabic": "ar",
    "chinese (simplified)": "zh",
    "chinese (traditional)": "zh-TW",
    "english": "en",
    "french": "fr",
    "german": "de",
    "hindi": "hi",
    "indonesian": "id",
    "japanese": "ja",
    "korean": "ko",
    "malay": "ms",
    "portuguese": "pt",
    "russian": "ru",
    "spanish": "es",
    "thai": "th",
    "turkish": "tr",
    "vietnamese": "vi",
}

BAIDU_LANGUAGE_TO_CODE = {
    "arabic": "ara",
    "bulgarian": "bul",
    "chinese (classical)": "wyw",
    "chinese (simplified)": "zh",
    "chinese (traditional)": "cht",
    "czech": "cs",
    "danish": "dan",
    "dutch": "nl",
    "english": "en",
    "estonian": "est",
    "finnish": "fin",
    "french": "fra",
    "german": "de",
    "greek": "el",
    "hungarian": "hu",
    "italian": "it",
    "japanese": "jp",
    "korean": "kor",
    "polish": "pl",
    "portuguese": "pt",
    "romanian": "ro",
    "russian": "ru",
    "slovenian": "slo",
    "spanish": "spa",
    "swedish": "swe",
    "thai": "th",
    "vietnamese": "vie",
    "yueyu": "yue",
}
