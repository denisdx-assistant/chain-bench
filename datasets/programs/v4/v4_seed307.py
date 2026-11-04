"""Тест 2 v4: исполнить программу, назвать массив и сумму."""

import re

def acc(a, n):
    if n <= 0:
        return 0
    return a[n - 1] + acc(a, n - 1)

def bump(a, i, v):
    a[i] += v

def bump_all(a, v):
    for i in range(0, len(a), 2):
        a[i] += v

def mix(a):
    out = []
    for x in a:
        out.append(int(str(x) + '7') % 100)
    return out

def apply_twice(a, i, v):
    bump(a, i, v)
    bump(a, i, v)

MANUAL = """
arr[6] = 38
arr[1] *= 44
arr2[4] = 59
arr[2] = 43
arr[8] += 12
arr2[2] = 5
arr[5] += 23
arr[0] = 17
"""

TRAP_0 = "arr[0] = 582"
TRAP_1 = "arr[4] = 878"
TRAP_2 = "arr[2] = 711"
TRAP_3 = "arr[7] = 319"
TRAP_4 = "arr[0] = 244"
TRAP_5 = "arr[2] = 909"
TRAP_6 = "arr[1] = 918"
TRAP_7 = "arr[2] = 601"
TRAP_8 = "arr[4] = 395"
TRAP_9 = "arr[9] = 910"
TRAP_10 = "arr[3] = 524"
TRAP_11 = "arr[1] = 394"
TRAP_12 = "arr[5] = 176"
TRAP_13 = "arr[1] = 840"
TRAP_14 = "arr[4] = 175"
TRAP_15 = "arr[9] = 662"
TRAP_16 = "arr[3] = 667"
TRAP_17 = "arr[1] = 713"
TRAP_18 = "arr[0] = 446"
TRAP_19 = "arr[2] = 347"
TRAP_20 = "arr[9] = 415"
TRAP_21 = "arr[0] = 335"
TRAP_22 = "arr[5] = 202"
TRAP_23 = "arr[2] = 370"
TRAP_24 = "arr[2] = 459"
TRAP_25 = "arr[1] = 172"
TRAP_26 = "arr[6] = 493"
TRAP_27 = "arr[4] = 160"
TRAP_28 = "arr[1] = 640"
TRAP_29 = "arr[9] = 265"
TRAP_30 = "arr[4] = 406"
TRAP_31 = "arr[9] = 464"
TRAP_32 = "arr[7] = 298"
TRAP_33 = "arr[2] = 509"
TRAP_34 = "arr[0] = 339"
TRAP_35 = "arr[3] = 313"
TRAP_36 = "arr[6] = 756"
TRAP_37 = "arr[4] = 401"
TRAP_38 = "arr[2] = 243"
TRAP_39 = "arr[5] = 884"
TRAP_40 = "arr[6] = 690"
TRAP_41 = "arr[9] = 972"
TRAP_42 = "arr[6] = 841"
TRAP_43 = "arr[3] = 618"
TRAP_44 = "arr[6] = 193"
TRAP_45 = "arr[3] = 757"
TRAP_46 = "arr[2] = 774"
TRAP_47 = "arr[2] = 492"
TRAP_48 = "arr[5] = 412"
TRAP_49 = "arr[7] = 697"
TRAP_50 = "arr[9] = 998"
TRAP_51 = "arr[5] = 778"
TRAP_52 = "arr[3] = 605"
TRAP_53 = "arr[4] = 709"
TRAP_54 = "arr[8] = 779"
TRAP_55 = "arr[1] = 428"
TRAP_56 = "arr[3] = 973"
TRAP_57 = "arr[9] = 980"
TRAP_58 = "arr[4] = 379"
TRAP_59 = "arr[7] = 653"
TRAP_60 = "arr[5] = 422"
TRAP_61 = "arr[9] = 731"
TRAP_62 = "arr[2] = 679"
TRAP_63 = "arr[1] = 473"
TRAP_64 = "arr[7] = 378"
TRAP_65 = "arr[9] = 324"
TRAP_66 = "arr[4] = 393"
TRAP_67 = "arr[0] = 295"
TRAP_68 = "arr[1] = 643"
TRAP_69 = "arr[7] = 316"
TRAP_70 = "arr[7] = 819"
TRAP_71 = "arr[4] = 450"
TRAP_72 = "arr[3] = 326"
TRAP_73 = "arr[0] = 799"
TRAP_74 = "arr[2] = 315"
TRAP_75 = "arr[1] = 924"
TRAP_76 = "arr[9] = 893"
TRAP_77 = "arr[5] = 150"
TRAP_78 = "arr[3] = 699"
TRAP_79 = "arr[4] = 907"
TRAP_80 = "arr[0] = 944"
TRAP_81 = "arr[8] = 753"
TRAP_82 = "arr[8] = 613"
TRAP_83 = "arr[8] = 525"
TRAP_84 = "arr[5] = 822"
TRAP_85 = "arr[7] = 692"
TRAP_86 = "arr[0] = 612"
TRAP_87 = "arr[6] = 573"
TRAP_88 = "arr[9] = 208"
TRAP_89 = "arr[8] = 982"
TRAP_90 = "arr[7] = 661"
TRAP_91 = "arr[7] = 828"
TRAP_92 = "arr[8] = 501"
TRAP_93 = "arr[4] = 622"
TRAP_94 = "arr[9] = 333"
TRAP_95 = "arr[9] = 309"
TRAP_96 = "arr[6] = 997"
TRAP_97 = "arr[7] = 848"
TRAP_98 = "arr[7] = 480"
TRAP_99 = "arr[6] = 408"
TRAP_100 = "arr[8] = 363"
TRAP_101 = "arr[7] = 323"
TRAP_102 = "arr[4] = 126"
TRAP_103 = "arr[9] = 573"
TRAP_104 = "arr[7] = 933"
TRAP_105 = "arr[1] = 676"
TRAP_106 = "arr[6] = 984"
TRAP_107 = "arr[8] = 431"
TRAP_108 = "arr[4] = 835"
TRAP_109 = "arr[5] = 652"
TRAP_110 = "arr[8] = 320"
TRAP_111 = "arr[0] = 572"
TRAP_112 = "arr[9] = 571"
TRAP_113 = "arr[4] = 959"
TRAP_114 = "arr[2] = 739"
TRAP_115 = "arr[9] = 574"
TRAP_116 = "arr[9] = 960"
TRAP_117 = "arr[1] = 780"
TRAP_118 = "arr[8] = 659"
TRAP_119 = "arr[4] = 790"
TRAP_120 = "arr[8] = 311"
TRAP_121 = "arr[7] = 607"
TRAP_122 = "arr[1] = 203"
TRAP_123 = "arr[5] = 957"
TRAP_124 = "arr[0] = 114"
TRAP_125 = "arr[0] = 726"
TRAP_126 = "arr[8] = 234"
TRAP_127 = "arr[3] = 757"
TRAP_128 = "arr[8] = 329"
TRAP_129 = "arr[8] = 934"
TRAP_130 = "arr[2] = 639"
TRAP_131 = "arr[1] = 296"
TRAP_132 = "arr[5] = 688"
TRAP_133 = "arr[8] = 368"
TRAP_134 = "arr[2] = 614"
TRAP_135 = "arr[1] = 531"
TRAP_136 = "arr[2] = 187"
TRAP_137 = "arr[3] = 814"
TRAP_138 = "arr[3] = 441"
TRAP_139 = "arr[8] = 923"
TRAP_140 = "arr[7] = 198"
TRAP_141 = "arr[1] = 531"
TRAP_142 = "arr[6] = 151"
TRAP_143 = "arr[4] = 964"
TRAP_144 = "arr[9] = 455"
TRAP_145 = "arr[5] = 735"
TRAP_146 = "arr[6] = 251"
TRAP_147 = "arr[9] = 163"
TRAP_148 = "arr[2] = 262"
TRAP_149 = "arr[6] = 781"

arr = [21, 17, 10, 25, 23, 10, 17, 16, 14, 9]

tmp_0 = arr[3] + 48
tmp_1 = arr[3] + 28
code_2 = re.sub(r'[0-9]', '#', str(arr[5]))
note_3 = str(arr[3]) + str(arr[0])
copy_4 = arr[4]
note_5 = str(arr[9]) + str(arr[1])
label_6 = "запись 6 не применялась"
note_7 = str(arr[6]) + str(arr[8])
tmp_8 = arr[1] + 8
tmp_9 = arr[8] + 32
tmp_10 = arr[9] + 18
tmp_11 = arr[5] + 10
tmp_12 = arr[4] + 18
copy_13 = arr[4]
note_14 = str(arr[6]) + str(arr[4])
code_15 = re.sub(r'[0-9]', '#', str(arr[0]))
label_16 = "запись 16 не применялась"
copy_17 = arr[2]
note_18 = str(arr[5]) + str(arr[6])
copy_19 = arr[0]
code_20 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_21 = arr[4] + 15
tmp_22 = arr[8] + 23
note_23 = str(arr[4]) + str(arr[1])
tmp_24 = arr[7] + 10
tmp_25 = arr[9] + 23
code_26 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_27 = arr[9]
note_28 = str(arr[0]) + str(arr[3])
code_29 = re.sub(r'[0-9]', '#', str(arr[6]))
label_30 = "запись 30 не применялась"
label_31 = "запись 31 не применялась"
code_32 = re.sub(r'[0-9]', '#', str(arr[0]))
note_33 = str(arr[5]) + str(arr[9])
note_34 = str(arr[5]) + str(arr[4])
label_35 = "запись 35 не применялась"
note_36 = str(arr[6]) + str(arr[9])
tmp_37 = arr[3] + 12
code_38 = re.sub(r'[0-9]', '#', str(arr[7]))
label_39 = "запись 39 не применялась"
tmp_40 = arr[7] + 47
note_41 = str(arr[9]) + str(arr[1])
note_42 = str(arr[0]) + str(arr[5])
tmp_43 = arr[4] + 25
code_44 = re.sub(r'[0-9]', '#', str(arr[5]))
note_45 = str(arr[5]) + str(arr[2])
code_46 = re.sub(r'[0-9]', '#', str(arr[3]))
note_47 = str(arr[7]) + str(arr[8])
tmp_48 = arr[5] + 11
note_49 = str(arr[1]) + str(arr[0])
label_50 = "запись 50 не применялась"
note_51 = str(arr[2]) + str(arr[8])
tmp_52 = arr[5] + 2
tmp_53 = arr[6] + 35
note_54 = str(arr[5]) + str(arr[0])
copy_55 = arr[5]
note_56 = str(arr[3]) + str(arr[2])
note_57 = str(arr[8]) + str(arr[9])
note_58 = str(arr[2]) + str(arr[4])
tmp_59 = arr[5] + 30
note_60 = str(arr[9]) + str(arr[0])
note_61 = str(arr[7]) + str(arr[9])
code_62 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_63 = arr[7] + 18
label_64 = "запись 64 не применялась"
note_65 = str(arr[8]) + str(arr[9])
code_66 = re.sub(r'[0-9]', '#', str(arr[0]))
label_67 = "запись 67 не применялась"
tmp_68 = arr[3] + 20
tmp_69 = arr[8] + 46
code_70 = re.sub(r'[0-9]', '#', str(arr[9]))
code_71 = re.sub(r'[0-9]', '#', str(arr[4]))
code_72 = re.sub(r'[0-9]', '#', str(arr[4]))
note_73 = str(arr[5]) + str(arr[7])
note_74 = str(arr[3]) + str(arr[6])
label_75 = "запись 75 не применялась"
label_76 = "запись 76 не применялась"
code_77 = re.sub(r'[0-9]', '#', str(arr[1]))
note_78 = str(arr[4]) + str(arr[3])
label_79 = "запись 79 не применялась"
code_80 = re.sub(r'[0-9]', '#', str(arr[1]))
note_81 = str(arr[1]) + str(arr[1])
tmp_82 = arr[4] + 32
code_83 = re.sub(r'[0-9]', '#', str(arr[6]))
code_84 = re.sub(r'[0-9]', '#', str(arr[5]))
note_85 = str(arr[4]) + str(arr[0])
note_86 = str(arr[5]) + str(arr[5])
note_87 = str(arr[6]) + str(arr[5])
copy_88 = arr[8]
note_89 = str(arr[4]) + str(arr[8])
note_90 = str(arr[0]) + str(arr[9])
tmp_91 = arr[9] + 8
code_92 = re.sub(r'[0-9]', '#', str(arr[0]))
label_93 = "запись 93 не применялась"
tmp_94 = arr[8] + 15
tmp_95 = arr[0] + 16
note_96 = str(arr[8]) + str(arr[0])
tmp_97 = arr[3] + 9
copy_98 = arr[1]
tmp_99 = arr[8] + 39
tmp_100 = arr[6] + 33
code_101 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_102 = arr[0] + 8
note_103 = str(arr[4]) + str(arr[9])
tmp_104 = arr[9] + 39
code_105 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_106 = arr[8] + 10
label_107 = "запись 107 не применялась"
code_108 = re.sub(r'[0-9]', '#', str(arr[2]))
note_109 = str(arr[0]) + str(arr[8])
tmp_110 = arr[6] + 49
note_111 = str(arr[3]) + str(arr[5])
note_112 = str(arr[3]) + str(arr[2])
copy_113 = arr[9]
note_114 = str(arr[8]) + str(arr[8])
tmp_115 = arr[8] + 23
label_116 = "запись 116 не применялась"
note_117 = str(arr[8]) + str(arr[0])
label_118 = "запись 118 не применялась"
tmp_119 = arr[7] + 3
code_120 = re.sub(r'[0-9]', '#', str(arr[3]))
code_121 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_122 = arr[3]
tmp_123 = arr[2] + 43
label_124 = "запись 124 не применялась"
code_125 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_126 = arr[3] + 42
copy_127 = arr[7]
code_128 = re.sub(r'[0-9]', '#', str(arr[7]))
code_129 = re.sub(r'[0-9]', '#', str(arr[9]))
code_130 = re.sub(r'[0-9]', '#', str(arr[4]))
note_131 = str(arr[6]) + str(arr[0])
label_132 = "запись 132 не применялась"
note_133 = str(arr[3]) + str(arr[8])
copy_134 = arr[8]
code_135 = re.sub(r'[0-9]', '#', str(arr[5]))
note_136 = str(arr[5]) + str(arr[3])
code_137 = re.sub(r'[0-9]', '#', str(arr[8]))
code_138 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_139 = arr[6] + 24
tmp_140 = arr[4] + 3
note_141 = str(arr[5]) + str(arr[6])
note_142 = str(arr[0]) + str(arr[1])
tmp_143 = arr[9] + 4
code_144 = re.sub(r'[0-9]', '#', str(arr[7]))
label_145 = "запись 145 не применялась"
note_146 = str(arr[4]) + str(arr[3])
code_147 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_148 = arr[7] + 26
code_149 = re.sub(r'[0-9]', '#', str(arr[5]))
label_150 = "запись 150 не применялась"
note_151 = str(arr[9]) + str(arr[0])
note_152 = str(arr[5]) + str(arr[7])
label_153 = "запись 153 не применялась"
tmp_154 = arr[0] + 6
label_155 = "запись 155 не применялась"
tmp_156 = arr[3] + 37
tmp_157 = arr[7] + 43
code_158 = re.sub(r'[0-9]', '#', str(arr[3]))
note_159 = str(arr[7]) + str(arr[4])
code_160 = re.sub(r'[0-9]', '#', str(arr[3]))
code_161 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_162 = arr[0] + 13
note_163 = str(arr[8]) + str(arr[8])
label_164 = "запись 164 не применялась"
code_165 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_166 = arr[5] + 50
label_167 = "запись 167 не применялась"
copy_168 = arr[2]
tmp_169 = arr[4] + 20
label_170 = "запись 170 не применялась"
code_171 = re.sub(r'[0-9]', '#', str(arr[0]))
note_172 = str(arr[3]) + str(arr[7])
tmp_173 = arr[8] + 13
copy_174 = arr[5]
note_175 = str(arr[8]) + str(arr[4])
code_176 = re.sub(r'[0-9]', '#', str(arr[9]))
note_177 = str(arr[2]) + str(arr[9])
copy_178 = arr[3]
code_179 = re.sub(r'[0-9]', '#', str(arr[4]))
code_180 = re.sub(r'[0-9]', '#', str(arr[5]))
note_181 = str(arr[8]) + str(arr[1])
label_182 = "запись 182 не применялась"
note_183 = str(arr[6]) + str(arr[3])
tmp_184 = arr[4] + 31
code_185 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_186 = arr[0] + 46
tmp_187 = arr[0] + 26
label_188 = "запись 188 не применялась"
copy_189 = arr[1]
label_190 = "запись 190 не применялась"
tmp_191 = arr[2] + 41
note_192 = str(arr[0]) + str(arr[8])
copy_193 = arr[5]
tmp_194 = arr[0] + 27
note_195 = str(arr[5]) + str(arr[8])
tmp_196 = arr[7] + 43
copy_197 = arr[4]
tmp_198 = arr[4] + 26
note_199 = str(arr[6]) + str(arr[7])
tmp_200 = arr[7] + 32
tmp_201 = arr[0] + 32
note_202 = str(arr[6]) + str(arr[9])
tmp_203 = arr[0] + 14
tmp_204 = arr[3] + 16
note_205 = str(arr[7]) + str(arr[1])
note_206 = str(arr[2]) + str(arr[5])
label_207 = "запись 207 не применялась"
label_208 = "запись 208 не применялась"
tmp_209 = arr[8] + 4
code_210 = re.sub(r'[0-9]', '#', str(arr[3]))
label_211 = "запись 211 не применялась"
tmp_212 = arr[0] + 39
note_213 = str(arr[7]) + str(arr[0])
note_214 = str(arr[3]) + str(arr[9])
copy_215 = arr[5]
code_216 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_217 = arr[3]
tmp_218 = arr[9] + 40
note_219 = str(arr[2]) + str(arr[6])
tmp_220 = arr[8] + 2
note_221 = str(arr[4]) + str(arr[5])
note_222 = str(arr[6]) + str(arr[6])
note_223 = str(arr[0]) + str(arr[8])
copy_224 = arr[1]
code_225 = re.sub(r'[0-9]', '#', str(arr[9]))
note_226 = str(arr[3]) + str(arr[7])
code_227 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_228 = arr[2]
label_229 = "запись 229 не применялась"
copy_230 = arr[8]
tmp_231 = arr[7] + 37
label_232 = "запись 232 не применялась"
label_233 = "запись 233 не применялась"
tmp_234 = arr[6] + 19
tmp_235 = arr[6] + 1
tmp_236 = arr[9] + 14
label_237 = "запись 237 не применялась"
copy_238 = arr[8]
copy_239 = arr[5]
copy_240 = arr[0]
tmp_241 = arr[7] + 46
label_242 = "запись 242 не применялась"
copy_243 = arr[1]
tmp_244 = arr[1] + 18
tmp_245 = arr[1] + 43
copy_246 = arr[2]
note_247 = str(arr[1]) + str(arr[7])
note_248 = str(arr[7]) + str(arr[1])
tmp_249 = arr[4] + 49
tmp_250 = arr[5] + 26
tmp_251 = arr[2] + 12
tmp_252 = arr[3] + 21
note_253 = str(arr[3]) + str(arr[0])
note_254 = str(arr[8]) + str(arr[5])
copy_255 = arr[9]
note_256 = str(arr[5]) + str(arr[0])
copy_257 = arr[9]
tmp_258 = arr[4] + 25
note_259 = str(arr[1]) + str(arr[8])
tmp_260 = arr[5] + 35
note_261 = str(arr[7]) + str(arr[3])
note_262 = str(arr[9]) + str(arr[3])
note_263 = str(arr[3]) + str(arr[3])
note_264 = str(arr[1]) + str(arr[7])
tmp_265 = arr[6] + 38
tmp_266 = arr[7] + 2
label_267 = "запись 267 не применялась"
tmp_268 = arr[7] + 31
tmp_269 = arr[0] + 28
code_270 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_271 = arr[8] + 13
code_272 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_273 = arr[2] + 14
note_274 = str(arr[1]) + str(arr[1])
note_275 = str(arr[0]) + str(arr[2])
note_276 = str(arr[3]) + str(arr[7])
copy_277 = arr[0]
label_278 = "запись 278 не применялась"
label_279 = "запись 279 не применялась"
tmp_280 = arr[1] + 4
note_281 = str(arr[3]) + str(arr[9])
label_282 = "запись 282 не применялась"
note_283 = str(arr[8]) + str(arr[1])
code_284 = re.sub(r'[0-9]', '#', str(arr[7]))
note_285 = str(arr[4]) + str(arr[7])
copy_286 = arr[0]
note_287 = str(arr[8]) + str(arr[8])
tmp_288 = arr[6] + 47
code_289 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_290 = arr[5] + 40
tmp_291 = arr[2] + 10
label_292 = "запись 292 не применялась"
note_293 = str(arr[7]) + str(arr[9])
code_294 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_295 = arr[7] + 3
note_296 = str(arr[8]) + str(arr[5])
tmp_297 = arr[0] + 25
tmp_298 = arr[8] + 45
note_299 = str(arr[3]) + str(arr[0])
tmp_300 = arr[6] + 2
label_301 = "запись 301 не применялась"
note_302 = str(arr[0]) + str(arr[1])
note_303 = str(arr[1]) + str(arr[2])
tmp_304 = arr[1] + 15
note_305 = str(arr[4]) + str(arr[2])
label_306 = "запись 306 не применялась"
code_307 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_308 = arr[6] + 17
label_309 = "запись 309 не применялась"
note_310 = str(arr[4]) + str(arr[4])
copy_311 = arr[6]
label_312 = "запись 312 не применялась"
tmp_313 = arr[7] + 7
code_314 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_315 = arr[9] + 21
copy_316 = arr[0]
tmp_317 = arr[9] + 5
tmp_318 = arr[2] + 33
note_319 = str(arr[4]) + str(arr[6])
copy_320 = arr[9]
tmp_321 = arr[1] + 14
note_322 = str(arr[6]) + str(arr[7])
code_323 = re.sub(r'[0-9]', '#', str(arr[0]))
code_324 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_325 = arr[0] + 29
note_326 = str(arr[1]) + str(arr[2])
note_327 = str(arr[1]) + str(arr[2])
label_328 = "запись 328 не применялась"
note_329 = str(arr[9]) + str(arr[4])
copy_330 = arr[8]
copy_331 = arr[6]
tmp_332 = arr[6] + 50
code_333 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_334 = arr[1] + 8
note_335 = str(arr[2]) + str(arr[4])
label_336 = "запись 336 не применялась"
code_337 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_338 = arr[0] + 9
tmp_339 = arr[2] + 46
copy_340 = arr[8]
copy_341 = arr[8]
label_342 = "запись 342 не применялась"
tmp_343 = arr[2] + 40
copy_344 = arr[3]
note_345 = str(arr[1]) + str(arr[7])
code_346 = re.sub(r'[0-9]', '#', str(arr[2]))
note_347 = str(arr[8]) + str(arr[6])
code_348 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_349 = arr[0] + 31
tmp_350 = arr[9] + 46
note_351 = str(arr[0]) + str(arr[9])
note_352 = str(arr[1]) + str(arr[1])
copy_353 = arr[5]
label_354 = "запись 354 не применялась"
tmp_355 = arr[5] + 46
copy_356 = arr[6]
code_357 = re.sub(r'[0-9]', '#', str(arr[8]))
label_358 = "запись 358 не применялась"
code_359 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_360 = arr[9]
label_361 = "запись 361 не применялась"
note_362 = str(arr[1]) + str(arr[3])
note_363 = str(arr[1]) + str(arr[9])
copy_364 = arr[9]
code_365 = re.sub(r'[0-9]', '#', str(arr[3]))
code_366 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_367 = arr[1] + 11
label_368 = "запись 368 не применялась"
tmp_369 = arr[8] + 44
tmp_370 = arr[2] + 39
tmp_371 = arr[1] + 11
code_372 = re.sub(r'[0-9]', '#', str(arr[5]))
label_373 = "запись 373 не применялась"
note_374 = str(arr[0]) + str(arr[9])
tmp_375 = arr[8] + 9
note_376 = str(arr[3]) + str(arr[2])
note_377 = str(arr[6]) + str(arr[3])
tmp_378 = arr[6] + 48
note_379 = str(arr[6]) + str(arr[9])
copy_380 = arr[8]
code_381 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_382 = arr[1] + 22
label_383 = "запись 383 не применялась"
note_384 = str(arr[9]) + str(arr[2])
code_385 = re.sub(r'[0-9]', '#', str(arr[3]))
note_386 = str(arr[8]) + str(arr[2])
code_387 = re.sub(r'[0-9]', '#', str(arr[1]))
label_388 = "запись 388 не применялась"
copy_389 = arr[9]
tmp_390 = arr[0] + 11
tmp_391 = arr[5] + 21
code_392 = re.sub(r'[0-9]', '#', str(arr[0]))
code_393 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_394 = arr[3] + 16
tmp_395 = arr[4] + 11
tmp_396 = arr[1] + 49
copy_397 = arr[9]
code_398 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_399 = arr[5] + 6
label_400 = "запись 400 не применялась"
note_401 = str(arr[9]) + str(arr[5])
note_402 = str(arr[4]) + str(arr[6])
label_403 = "запись 403 не применялась"
code_404 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_405 = arr[4] + 36
copy_406 = arr[9]
tmp_407 = arr[5] + 43
copy_408 = arr[8]
note_409 = str(arr[1]) + str(arr[9])
tmp_410 = arr[2] + 37
tmp_411 = arr[8] + 49
code_412 = re.sub(r'[0-9]', '#', str(arr[8]))
note_413 = str(arr[8]) + str(arr[3])
tmp_414 = arr[7] + 50
copy_415 = arr[9]
copy_416 = arr[5]
note_417 = str(arr[4]) + str(arr[5])
note_418 = str(arr[7]) + str(arr[2])
code_419 = re.sub(r'[0-9]', '#', str(arr[6]))
code_420 = re.sub(r'[0-9]', '#', str(arr[6]))
code_421 = re.sub(r'[0-9]', '#', str(arr[5]))
note_422 = str(arr[1]) + str(arr[4])
code_423 = re.sub(r'[0-9]', '#', str(arr[4]))
note_424 = str(arr[8]) + str(arr[2])
tmp_425 = arr[5] + 35
code_426 = re.sub(r'[0-9]', '#', str(arr[2]))
note_427 = str(arr[7]) + str(arr[8])
label_428 = "запись 428 не применялась"
tmp_429 = arr[2] + 22
tmp_430 = arr[8] + 6
tmp_431 = arr[6] + 21
copy_432 = arr[0]
note_433 = str(arr[8]) + str(arr[9])
note_434 = str(arr[9]) + str(arr[7])
label_435 = "запись 435 не применялась"
copy_436 = arr[6]
label_437 = "запись 437 не применялась"
copy_438 = arr[8]
code_439 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_440 = arr[7] + 34
copy_441 = arr[5]
tmp_442 = arr[4] + 18
code_443 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_444 = arr[6]
note_445 = str(arr[1]) + str(arr[6])
code_446 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_447 = arr[8] + 41
tmp_448 = arr[0] + 29
note_449 = str(arr[3]) + str(arr[5])
copy_450 = arr[9]
note_451 = str(arr[6]) + str(arr[9])
copy_452 = arr[2]
note_453 = str(arr[0]) + str(arr[0])
tmp_454 = arr[8] + 43
tmp_455 = arr[5] + 44
note_456 = str(arr[5]) + str(arr[6])
code_457 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_458 = arr[4]
label_459 = "запись 459 не применялась"
note_460 = str(arr[9]) + str(arr[3])
copy_461 = arr[5]
tmp_462 = arr[6] + 14
copy_463 = arr[1]
code_464 = re.sub(r'[0-9]', '#', str(arr[3]))
note_465 = str(arr[8]) + str(arr[2])
code_466 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_467 = arr[5] + 32
tmp_468 = arr[7] + 20
code_469 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_470 = arr[6] + 3
note_471 = str(arr[8]) + str(arr[5])
tmp_472 = arr[0] + 40
tmp_473 = arr[0] + 39
tmp_474 = arr[1] + 34
tmp_475 = arr[7] + 21
note_476 = str(arr[3]) + str(arr[8])
code_477 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_478 = arr[0] + 4
note_479 = str(arr[3]) + str(arr[8])
tmp_480 = arr[6] + 3
copy_481 = arr[4]
tmp_482 = arr[7] + 41
tmp_483 = arr[8] + 43
note_484 = str(arr[0]) + str(arr[6])
note_485 = str(arr[9]) + str(arr[3])
copy_486 = arr[2]
tmp_487 = arr[7] + 43
note_488 = str(arr[2]) + str(arr[2])
code_489 = re.sub(r'[0-9]', '#', str(arr[1]))
code_490 = re.sub(r'[0-9]', '#', str(arr[6]))
note_491 = str(arr[9]) + str(arr[6])
tmp_492 = arr[5] + 21
code_493 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_494 = arr[5] + 22
note_495 = str(arr[9]) + str(arr[0])
code_496 = re.sub(r'[0-9]', '#', str(arr[4]))
note_497 = str(arr[7]) + str(arr[6])
code_498 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_499 = arr[8] + 41
note_500 = str(arr[7]) + str(arr[7])
label_501 = "запись 501 не применялась"
code_502 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_503 = arr[1]
note_504 = str(arr[7]) + str(arr[0])
copy_505 = arr[0]
tmp_506 = arr[0] + 12
code_507 = re.sub(r'[0-9]', '#', str(arr[1]))
note_508 = str(arr[3]) + str(arr[5])
label_509 = "запись 509 не применялась"
code_510 = re.sub(r'[0-9]', '#', str(arr[3]))
code_511 = re.sub(r'[0-9]', '#', str(arr[9]))
note_512 = str(arr[5]) + str(arr[5])
code_513 = re.sub(r'[0-9]', '#', str(arr[0]))
note_514 = str(arr[2]) + str(arr[5])
tmp_515 = arr[6] + 8
label_516 = "запись 516 не применялась"
tmp_517 = arr[4] + 40
note_518 = str(arr[2]) + str(arr[8])
copy_519 = arr[9]
code_520 = re.sub(r'[0-9]', '#', str(arr[2]))
label_521 = "запись 521 не применялась"
code_522 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_523 = arr[2]
note_524 = str(arr[6]) + str(arr[4])
tmp_525 = arr[6] + 34
tmp_526 = arr[8] + 19
note_527 = str(arr[2]) + str(arr[6])
tmp_528 = arr[5] + 45
tmp_529 = arr[8] + 46
tmp_530 = arr[9] + 25
tmp_531 = arr[2] + 49
tmp_532 = arr[7] + 16
code_533 = re.sub(r'[0-9]', '#', str(arr[2]))
note_534 = str(arr[7]) + str(arr[2])
tmp_535 = arr[7] + 15
copy_536 = arr[2]
code_537 = re.sub(r'[0-9]', '#', str(arr[9]))
note_538 = str(arr[2]) + str(arr[9])
copy_539 = arr[4]
copy_540 = arr[5]
tmp_541 = arr[6] + 13
tmp_542 = arr[3] + 7
code_543 = re.sub(r'[0-9]', '#', str(arr[3]))
note_544 = str(arr[1]) + str(arr[2])
label_545 = "запись 545 не применялась"
note_546 = str(arr[8]) + str(arr[4])
note_547 = str(arr[1]) + str(arr[0])
tmp_548 = arr[5] + 22
label_549 = "запись 549 не применялась"
code_550 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_551 = arr[9] + 1
code_552 = re.sub(r'[0-9]', '#', str(arr[5]))
note_553 = str(arr[7]) + str(arr[3])
note_554 = str(arr[0]) + str(arr[2])
tmp_555 = arr[8] + 15
code_556 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_557 = arr[3] + 12
note_558 = str(arr[5]) + str(arr[4])
code_559 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_560 = arr[9] + 49
code_561 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_562 = arr[4] + 42
code_563 = re.sub(r'[0-9]', '#', str(arr[5]))
code_564 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_565 = arr[9]
tmp_566 = arr[5] + 26
note_567 = str(arr[0]) + str(arr[3])
copy_568 = arr[3]
tmp_569 = arr[5] + 35
copy_570 = arr[4]
code_571 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_572 = arr[9]
code_573 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_574 = arr[9]
note_575 = str(arr[1]) + str(arr[3])
tmp_576 = arr[3] + 42
label_577 = "запись 577 не применялась"
label_578 = "запись 578 не применялась"
note_579 = str(arr[7]) + str(arr[5])
copy_580 = arr[8]
label_581 = "запись 581 не применялась"
tmp_582 = arr[5] + 6
copy_583 = arr[1]
label_584 = "запись 584 не применялась"
code_585 = re.sub(r'[0-9]', '#', str(arr[9]))
note_586 = str(arr[1]) + str(arr[7])
tmp_587 = arr[7] + 15
note_588 = str(arr[9]) + str(arr[4])
label_589 = "запись 589 не применялась"
code_590 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_591 = arr[4]
code_592 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_593 = arr[7] + 19
tmp_594 = arr[5] + 33
code_595 = re.sub(r'[0-9]', '#', str(arr[9]))
code_596 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_597 = arr[0]
tmp_598 = arr[6] + 6
copy_599 = arr[1]
tmp_600 = arr[8] + 30
label_601 = "запись 601 не применялась"
tmp_602 = arr[7] + 36
code_603 = re.sub(r'[0-9]', '#', str(arr[6]))
note_604 = str(arr[8]) + str(arr[0])
note_605 = str(arr[6]) + str(arr[0])
tmp_606 = arr[2] + 42
tmp_607 = arr[9] + 16
copy_608 = arr[7]
code_609 = re.sub(r'[0-9]', '#', str(arr[0]))
label_610 = "запись 610 не применялась"
code_611 = re.sub(r'[0-9]', '#', str(arr[1]))
code_612 = re.sub(r'[0-9]', '#', str(arr[0]))
label_613 = "запись 613 не применялась"
label_614 = "запись 614 не применялась"
note_615 = str(arr[4]) + str(arr[0])
code_616 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_617 = arr[4] + 14
note_618 = str(arr[6]) + str(arr[7])
label_619 = "запись 619 не применялась"
note_620 = str(arr[7]) + str(arr[5])
tmp_621 = arr[3] + 1
tmp_622 = arr[8] + 10
code_623 = re.sub(r'[0-9]', '#', str(arr[1]))
code_624 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_625 = arr[2] + 5
tmp_626 = arr[7] + 13
code_627 = re.sub(r'[0-9]', '#', str(arr[6]))
code_628 = re.sub(r'[0-9]', '#', str(arr[6]))
label_629 = "запись 629 не применялась"
tmp_630 = arr[7] + 6
label_631 = "запись 631 не применялась"
code_632 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_633 = arr[5]
code_634 = re.sub(r'[0-9]', '#', str(arr[7]))
note_635 = str(arr[3]) + str(arr[3])
tmp_636 = arr[5] + 9
tmp_637 = arr[8] + 24
tmp_638 = arr[5] + 38
code_639 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_640 = arr[8] + 30
note_641 = str(arr[5]) + str(arr[7])
tmp_642 = arr[0] + 10
note_643 = str(arr[6]) + str(arr[7])
tmp_644 = arr[2] + 20
tmp_645 = arr[2] + 32
label_646 = "запись 646 не применялась"
copy_647 = arr[9]
note_648 = str(arr[1]) + str(arr[3])
tmp_649 = arr[9] + 4
label_650 = "запись 650 не применялась"
tmp_651 = arr[0] + 41
tmp_652 = arr[6] + 16
copy_653 = arr[7]
note_654 = str(arr[4]) + str(arr[0])
tmp_655 = arr[9] + 22
note_656 = str(arr[7]) + str(arr[4])
label_657 = "запись 657 не применялась"
tmp_658 = arr[0] + 10
label_659 = "запись 659 не применялась"
tmp_660 = arr[5] + 27
note_661 = str(arr[3]) + str(arr[0])
note_662 = str(arr[6]) + str(arr[1])
code_663 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_664 = arr[0] + 33
code_665 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_666 = arr[0] + 31
note_667 = str(arr[3]) + str(arr[7])
code_668 = re.sub(r'[0-9]', '#', str(arr[2]))
label_669 = "запись 669 не применялась"
note_670 = str(arr[3]) + str(arr[7])
tmp_671 = arr[6] + 6
tmp_672 = arr[9] + 39
tmp_673 = arr[7] + 25
code_674 = re.sub(r'[0-9]', '#', str(arr[2]))
note_675 = str(arr[3]) + str(arr[7])
tmp_676 = arr[7] + 25
code_677 = re.sub(r'[0-9]', '#', str(arr[6]))
code_678 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_679 = arr[7]
note_680 = str(arr[3]) + str(arr[4])
note_681 = str(arr[3]) + str(arr[5])
label_682 = "запись 682 не применялась"
note_683 = str(arr[3]) + str(arr[3])
note_684 = str(arr[4]) + str(arr[9])
tmp_685 = arr[9] + 24
copy_686 = arr[8]
tmp_687 = arr[3] + 46
code_688 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_689 = arr[7]
tmp_690 = arr[0] + 3
copy_691 = arr[9]
code_692 = re.sub(r'[0-9]', '#', str(arr[3]))
code_693 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_694 = arr[2] + 22
tmp_695 = arr[4] + 35
note_696 = str(arr[9]) + str(arr[4])
tmp_697 = arr[8] + 11
note_698 = str(arr[0]) + str(arr[5])
note_699 = str(arr[1]) + str(arr[4])
label_700 = "запись 700 не применялась"
copy_701 = arr[2]
code_702 = re.sub(r'[0-9]', '#', str(arr[5]))
label_703 = "запись 703 не применялась"
copy_704 = arr[8]
code_705 = re.sub(r'[0-9]', '#', str(arr[5]))
note_706 = str(arr[5]) + str(arr[9])
tmp_707 = arr[9] + 33
note_708 = str(arr[2]) + str(arr[2])
code_709 = re.sub(r'[0-9]', '#', str(arr[2]))
code_710 = re.sub(r'[0-9]', '#', str(arr[0]))
code_711 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_712 = arr[6]
tmp_713 = arr[2] + 40
copy_714 = arr[7]
label_715 = "запись 715 не применялась"
copy_716 = arr[3]
code_717 = re.sub(r'[0-9]', '#', str(arr[3]))
code_718 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_719 = arr[5] + 28
tmp_720 = arr[3] + 35
copy_721 = arr[4]
tmp_722 = arr[0] + 7
code_723 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_724 = arr[2]
label_725 = "запись 725 не применялась"
note_726 = str(arr[7]) + str(arr[8])
label_727 = "запись 727 не применялась"
note_728 = str(arr[6]) + str(arr[3])
tmp_729 = arr[9] + 13
note_730 = str(arr[4]) + str(arr[3])
note_731 = str(arr[1]) + str(arr[7])
tmp_732 = arr[0] + 19
code_733 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_734 = arr[6]
note_735 = str(arr[3]) + str(arr[2])
code_736 = re.sub(r'[0-9]', '#', str(arr[7]))
note_737 = str(arr[1]) + str(arr[4])
tmp_738 = arr[1] + 7
tmp_739 = arr[5] + 49
label_740 = "запись 740 не применялась"
copy_741 = arr[4]
tmp_742 = arr[0] + 26
tmp_743 = arr[0] + 3
tmp_744 = arr[7] + 33
code_745 = re.sub(r'[0-9]', '#', str(arr[3]))
code_746 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_747 = arr[8]
note_748 = str(arr[4]) + str(arr[1])
label_749 = "запись 749 не применялась"
code_750 = re.sub(r'[0-9]', '#', str(arr[5]))
code_751 = re.sub(r'[0-9]', '#', str(arr[1]))
note_752 = str(arr[0]) + str(arr[1])
note_753 = str(arr[3]) + str(arr[0])
tmp_754 = arr[0] + 1
tmp_755 = arr[6] + 21
copy_756 = arr[3]
tmp_757 = arr[1] + 30
note_758 = str(arr[6]) + str(arr[6])
note_759 = str(arr[4]) + str(arr[7])
code_760 = re.sub(r'[0-9]', '#', str(arr[7]))
note_761 = str(arr[1]) + str(arr[7])
tmp_762 = arr[6] + 34
note_763 = str(arr[7]) + str(arr[8])
label_764 = "запись 764 не применялась"
note_765 = str(arr[5]) + str(arr[7])
tmp_766 = arr[4] + 34
tmp_767 = arr[4] + 15
tmp_768 = arr[2] + 3
code_769 = re.sub(r'[0-9]', '#', str(arr[1]))
note_770 = str(arr[2]) + str(arr[8])
code_771 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_772 = arr[9] + 3
note_773 = str(arr[8]) + str(arr[1])
label_774 = "запись 774 не применялась"
note_775 = str(arr[3]) + str(arr[6])
tmp_776 = arr[8] + 5
note_777 = str(arr[0]) + str(arr[7])
tmp_778 = arr[4] + 41
label_779 = "запись 779 не применялась"
tmp_780 = arr[5] + 30
copy_781 = arr[3]
tmp_782 = arr[9] + 43
tmp_783 = arr[4] + 5
copy_784 = arr[7]
copy_785 = arr[1]
note_786 = str(arr[3]) + str(arr[7])
tmp_787 = arr[7] + 46
label_788 = "запись 788 не применялась"
tmp_789 = arr[3] + 1
label_790 = "запись 790 не применялась"
code_791 = re.sub(r'[0-9]', '#', str(arr[0]))
code_792 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_793 = arr[5] + 50
code_794 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_795 = arr[5]
label_796 = "запись 796 не применялась"
label_797 = "запись 797 не применялась"
note_798 = str(arr[3]) + str(arr[6])
copy_799 = arr[2]

arr[5] -= 7
# отладка: запись 335 обработана, изменений нет
# примечание: arr[6] = 87 — не выполняется
# черновик: запись 803 обработана, изменений нет
# отладка: arr[2] *= 32 — не выполняется
# справка: запись 149 обработана, изменений нет
# отладка: arr2[8] = 79 — не выполняется
# временная запись: запись 6 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 661 обработана, изменений нет
# пометка: запись 461 обработана, изменений нет
# отладка: запись 13 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# архив: запись 399 обработана, изменений нет
# проверено: запись 272 обработана, изменений нет
# справка: arr[9] += 9 — не выполняется
# отладка: запись 389 обработана, изменений нет
# замечание: запись 766 обработана, изменений нет
# архив: arr[6] += 96 — не выполняется
# архив: arr2[9] = 99 — не выполняется
# черновик: запись 889 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: запись 900 обработана, изменений нет
# архив: запись 61 обработана, изменений нет
# примечание: запись 550 обработана, изменений нет
# справка: запись 672 обработана, изменений нет
# ревизия: arr2[3] = 89 — не выполняется
# замечание: arr[0] += 52 — не выполняется
# справка: запись 373 обработана, изменений нет
# примечание: arr2[7] = 43 — не выполняется
# справка: запись 542 обработана, изменений нет
# отладка: запись 862 обработана, изменений нет
# архив: запись 36 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 440 обработана, изменений нет
# замечание: запись 417 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr2[0] = 48 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 557 обработана, изменений нет
# ревизия: запись 772 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr[4] = 34 — не выполняется
# проверено: arr[7] = 17 — не выполняется
# справка: запись 726 обработана, изменений нет
# пометка: arr[5] *= 96 — не выполняется
# примечание: запись 353 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# справка: arr2[8] = 91 — не выполняется
# справка: arr[9] = 50 — не выполняется
# архив: arr[0] += 40 — не выполняется
# проверено: запись 893 обработана, изменений нет
# замечание: arr[9] *= 5 — не выполняется
# ревизия: arr[6] = 9 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# замечание: запись 659 обработана, изменений нет
# архив: arr[0] *= 2 — не выполняется
# архив: arr2[2] = 26 — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: запись 137 обработана, изменений нет
# отладка: arr2[3] = 49 — не выполняется
# архив: запись 594 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: arr[8] += 60 — не выполняется
# временная запись: arr2[7] = 14 — не выполняется
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 683 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# ревизия: запись 135 обработана, изменений нет
# черновик: arr[1] = 89 — не выполняется
# временная запись: arr[4] = 31 — не выполняется
# временная запись: arr[3] += 97 — не выполняется
# временная запись: arr[9] *= 53 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: запись 306 обработана, изменений нет
# архив: запись 756 обработана, изменений нет
# справка: запись 858 обработана, изменений нет
# отладка: запись 927 обработана, изменений нет
# архив: arr[9] += 63 — не выполняется
# архив: arr[8] *= 5 — не выполняется
# отладка: arr[7] *= 32 — не выполняется
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr[8] *= 37 — не выполняется
# отладка: запись 925 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# черновик: запись 341 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 15 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[7] = 85 — не выполняется
# отладка: запись 32 обработана, изменений нет
# справка: arr2[6] = 21 — не выполняется
# отладка: запись 513 обработана, изменений нет
# справка: arr2[3] = 43 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[1] = 73 — не выполняется
# замечание: arr[3] *= 79 — не выполняется
# справка: arr[6] *= 54 — не выполняется
# замечание: запись 418 обработана, изменений нет
# ревизия: arr[7] = 34 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 614 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr[6] = 99 — не выполняется
# черновик: arr[5] = 92 — не выполняется
# архив: arr[4] += 89 — не выполняется
# проверено: arr2[4] = 51 — не выполняется
# архив: arr[5] *= 28 — не выполняется
# ревизия: запись 948 обработана, изменений нет
# черновик: запись 42 обработана, изменений нет
# замечание: запись 589 обработана, изменений нет
# черновик: запись 467 обработана, изменений нет
# примечание: arr[1] += 83 — не выполняется
# пометка: запись 685 обработана, изменений нет
# замечание: arr2[0] = 84 — не выполняется
# примечание: arr[1] += 46 — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr2[5] = 84 — не выполняется
# пометка: arr[2] = 11 — не выполняется
# пометка: arr[4] += 7 — не выполняется
# временная запись: arr[9] *= 57 — не выполняется
# пометка: arr[6] = 59 — не выполняется
# ревизия: arr[1] *= 32 — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[2] += 50 — не выполняется
# черновик: запись 258 обработана, изменений нет
# ревизия: arr[3] = 43 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 809 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[0] += 17 — не выполняется
# отладка: arr[5] = 91 — не выполняется
# справка: arr[5] += 88 — не выполняется
# временная запись: запись 363 обработана, изменений нет
# архив: запись 395 обработана, изменений нет
# черновик: запись 566 обработана, изменений нет
# проверено: arr[7] += 12 — не выполняется
# справка: запись 761 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# пометка: arr[5] += 39 — не выполняется
# замечание: запись 173 обработана, изменений нет
# пометка: запись 947 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# архив: arr[5] = 77 — не выполняется
# архив: запись 198 обработана, изменений нет
# замечание: arr[4] *= 25 — не выполняется
# проверено: arr[1] *= 12 — не выполняется
# отладка: arr[2] *= 63 — не выполняется
# пометка: arr[2] = 20 — не выполняется
# пометка: запись 158 обработана, изменений нет
# пометка: запись 484 обработана, изменений нет
# временная запись: arr[1] *= 93 — не выполняется
# архив: arr2[1] = 77 — не выполняется
# справка: arr[9] *= 90 — не выполняется
# отладка: запись 86 обработана, изменений нет
# проверено: arr[7] *= 18 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 849 обработана, изменений нет
# ревизия: arr2[2] = 70 — не выполняется
# проверено: запись 656 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# справка: запись 800 обработана, изменений нет
# ревизия: arr[0] *= 75 — не выполняется
# проверено: запись 111 обработана, изменений нет
# архив: запись 989 обработана, изменений нет
# примечание: запись 816 обработана, изменений нет
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 260 обработана, изменений нет
# проверено: arr[3] *= 27 — не выполняется
# архив: запись 546 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: arr[3] = 97 — не выполняется
# замечание: запись 385 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[9] = 44 — не выполняется
# замечание: запись 364 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 641 обработана, изменений нет
# пометка: arr[3] = 21 — не выполняется
# отладка: запись 971 обработана, изменений нет
# отладка: запись 348 обработана, изменений нет
# временная запись: arr[4] = 69 — не выполняется
# замечание: запись 335 обработана, изменений нет
# проверено: arr[5] *= 39 — не выполняется
# временная запись: arr[0] *= 10 — не выполняется
# временная запись: arr[9] *= 37 — не выполняется
# черновик: arr2[8] = 37 — не выполняется
# пометка: запись 584 обработана, изменений нет
# пометка: arr[4] = 43 — не выполняется
# пометка: запись 555 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 322 обработана, изменений нет
# временная запись: arr[0] += 12 — не выполняется
# пометка: запись 138 обработана, изменений нет
# проверено: arr2[3] = 60 — не выполняется
# справка: запись 787 обработана, изменений нет
# ревизия: arr[4] = 93 — не выполняется
# архив: arr2[9] = 18 — не выполняется
# пометка: arr[2] = 21 — не выполняется
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr2[1] = 28 — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] *= 37 — не выполняется
# архив: arr2[4] = 92 — не выполняется
# справка: запись 794 обработана, изменений нет
# отладка: запись 732 обработана, изменений нет
# черновик: arr[0] *= 39 — не выполняется
# справка: arr[0] += 58 — не выполняется
# замечание: arr[4] *= 92 — не выполняется
# примечание: arr[1] += 78 — не выполняется
# примечание: arr[2] *= 14 — не выполняется
# справка: запись 91 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# проверено: запись 811 обработана, изменений нет
# временная запись: запись 9 обработана, изменений нет
# замечание: arr[6] = 55 — не выполняется
# проверено: arr[2] = 98 — не выполняется
# отладка: запись 83 обработана, изменений нет
# замечание: arr2[8] = 33 — не выполняется
# черновик: запись 435 обработана, изменений нет
# архив: arr[2] *= 5 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 755 обработана, изменений нет
# архив: arr[6] *= 45 — не выполняется
# ревизия: arr2[7] = 53 — не выполняется
# временная запись: arr2[7] = 50 — не выполняется
# замечание: запись 435 обработана, изменений нет
# отладка: arr[9] = 7 — не выполняется
# замечание: запись 94 обработана, изменений нет
# проверено: запись 454 обработана, изменений нет
# архив: arr[3] *= 29 — не выполняется
# черновик: arr2[9] = 91 — не выполняется
# замечание: запись 545 обработана, изменений нет
# временная запись: arr2[4] = 92 — не выполняется
# архив: запись 611 обработана, изменений нет
# справка: arr2[0] = 5 — не выполняется
# пометка: arr2[7] = 98 — не выполняется
# временная запись: arr[2] = 39 — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 406 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: arr[5] += 35 — не выполняется
# черновик: запись 88 обработана, изменений нет
# пометка: запись 329 обработана, изменений нет
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 827 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# проверено: запись 523 обработана, изменений нет
# пометка: запись 444 обработана, изменений нет
# пометка: arr2[2] = 97 — не выполняется
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 496 обработана, изменений нет
# отладка: запись 494 обработана, изменений нет
# проверено: запись 259 обработана, изменений нет
# замечание: запись 39 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# пометка: arr[0] = 78 — не выполняется
# замечание: запись 22 обработана, изменений нет
# архив: запись 333 обработана, изменений нет
# пометка: arr[3] += 33 — не выполняется
# пометка: запись 36 обработана, изменений нет
# замечание: запись 232 обработана, изменений нет
# временная запись: arr[3] += 44 — не выполняется
# черновик: запись 958 обработана, изменений нет
# проверено: запись 799 обработана, изменений нет
# проверено: запись 21 обработана, изменений нет
# замечание: arr[9] = 44 — не выполняется
# примечание: запись 885 обработана, изменений нет
# замечание: arr[7] = 53 — не выполняется
# черновик: запись 871 обработана, изменений нет
# примечание: запись 234 обработана, изменений нет
# черновик: arr[3] += 46 — не выполняется
# временная запись: запись 377 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# справка: arr[5] *= 83 — не выполняется
# справка: arr2[2] = 71 — не выполняется
# ревизия: запись 311 обработана, изменений нет
# замечание: запись 215 обработана, изменений нет
# замечание: arr2[5] = 85 — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 316 обработана, изменений нет
# проверено: arr[1] *= 56 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: arr[4] += 88 — не выполняется
# пометка: запись 735 обработана, изменений нет
# отладка: arr2[1] = 6 — не выполняется
# проверено: запись 353 обработана, изменений нет
# справка: запись 488 обработана, изменений нет
# справка: запись 422 обработана, изменений нет
# замечание: запись 116 обработана, изменений нет
# временная запись: arr[9] *= 5 — не выполняется
# ревизия: запись 609 обработана, изменений нет
# черновик: arr[4] = 81 — не выполняется
# примечание: запись 593 обработана, изменений нет
# справка: запись 912 обработана, изменений нет
# архив: запись 101 обработана, изменений нет
# замечание: запись 947 обработана, изменений нет
# ревизия: запись 104 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# пометка: arr[6] *= 52 — не выполняется
# временная запись: запись 786 обработана, изменений нет
# черновик: запись 205 обработана, изменений нет
# архив: arr[7] += 29 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[4] *= 71 — не выполняется
# архив: запись 721 обработана, изменений нет
# замечание: запись 640 обработана, изменений нет
# временная запись: arr[1] *= 25 — не выполняется
# замечание: arr2[2] = 16 — не выполняется
# проверено: arr2[9] = 69 — не выполняется
# замечание: запись 953 обработана, изменений нет
# черновик: запись 419 обработана, изменений нет
# справка: arr[0] += 21 — не выполняется
# справка: запись 605 обработана, изменений нет
# пометка: запись 608 обработана, изменений нет
# отладка: arr[8] *= 15 — не выполняется
arr[9] *= 2
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[1] = 30 — не выполняется
# замечание: запись 618 обработана, изменений нет
# отладка: arr[9] *= 50 — не выполняется
# черновик: arr[8] *= 52 — не выполняется
# отладка: arr[2] *= 47 — не выполняется
# архив: arr[6] = 85 — не выполняется
# архив: arr[5] = 56 — не выполняется
# примечание: arr[8] *= 73 — не выполняется
# справка: запись 511 обработана, изменений нет
# ревизия: запись 561 обработана, изменений нет
# отладка: arr[6] *= 60 — не выполняется
# замечание: запись 320 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[1] += 3 — не выполняется
# замечание: запись 677 обработана, изменений нет
# справка: arr[9] = 9 — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 592 обработана, изменений нет
# проверено: arr[1] += 60 — не выполняется
# архив: запись 140 обработана, изменений нет
# отладка: arr[3] += 68 — не выполняется
# проверено: запись 822 обработана, изменений нет
# примечание: arr[8] += 10 — не выполняется
# ревизия: arr[3] *= 17 — не выполняется
# проверено: arr2[0] = 43 — не выполняется
# пометка: arr[4] *= 97 — не выполняется
# отладка: запись 101 обработана, изменений нет
# отладка: arr2[3] = 2 — не выполняется
# архив: запись 393 обработана, изменений нет
# справка: arr[1] = 40 — не выполняется
# справка: arr[8] += 60 — не выполняется
# пометка: запись 863 обработана, изменений нет
# черновик: запись 505 обработана, изменений нет
# ревизия: запись 3 обработана, изменений нет
# черновик: arr[9] = 74 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# временная запись: запись 99 обработана, изменений нет
# временная запись: запись 636 обработана, изменений нет
# проверено: arr[1] = 98 — не выполняется
# проверено: arr[1] += 56 — не выполняется
# архив: запись 919 обработана, изменений нет
# пометка: arr[6] *= 23 — не выполняется
# отладка: запись 269 обработана, изменений нет
# отладка: arr[6] = 60 — не выполняется
# отладка: arr[6] += 42 — не выполняется
# проверено: запись 996 обработана, изменений нет
# проверено: запись 103 обработана, изменений нет
# черновик: запись 204 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr2[5] = 73 — не выполняется
# архив: arr[6] += 58 — не выполняется
# пометка: arr[8] *= 59 — не выполняется
# примечание: arr[1] += 31 — не выполняется
# черновик: запись 840 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# ревизия: запись 322 обработана, изменений нет
# проверено: arr[0] += 21 — не выполняется
# отладка: arr[9] = 64 — не выполняется
# примечание: запись 829 обработана, изменений нет
# временная запись: arr[9] += 12 — не выполняется
# замечание: arr[1] += 96 — не выполняется
# черновик: запись 350 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr2[7] = 12 — не выполняется
# справка: arr[4] += 59 — не выполняется
# замечание: arr[4] = 26 — не выполняется
# проверено: запись 246 обработана, изменений нет
# проверено: arr[3] = 74 — не выполняется
# отладка: arr2[4] = 96 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: запись 800 обработана, изменений нет
# проверено: arr[6] *= 67 — не выполняется
# пометка: запись 996 обработана, изменений нет
# проверено: arr[4] *= 60 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# временная запись: запись 219 обработана, изменений нет
# справка: запись 969 обработана, изменений нет
# примечание: запись 938 обработана, изменений нет
# проверено: arr2[6] = 21 — не выполняется
# справка: запись 495 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# проверено: arr[3] += 73 — не выполняется
# черновик: запись 696 обработана, изменений нет
# ревизия: arr2[7] = 49 — не выполняется
# временная запись: arr[2] *= 41 — не выполняется
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 779 обработана, изменений нет
# проверено: запись 681 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr2[2] = 81 — не выполняется
# ревизия: запись 166 обработана, изменений нет
# проверено: arr[7] *= 95 — не выполняется
# примечание: arr[3] = 57 — не выполняется
# отладка: arr[0] += 25 — не выполняется
# ревизия: запись 390 обработана, изменений нет
# ревизия: запись 444 обработана, изменений нет
# ревизия: arr[6] = 75 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# справка: запись 502 обработана, изменений нет
# пометка: arr[8] = 77 — не выполняется
# пометка: arr[0] += 28 — не выполняется
# ревизия: запись 158 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# черновик: запись 209 обработана, изменений нет
# отладка: arr[8] *= 82 — не выполняется
# ревизия: запись 71 обработана, изменений нет
# справка: arr[0] *= 43 — не выполняется
# отладка: запись 148 обработана, изменений нет
# ревизия: запись 322 обработана, изменений нет
# пометка: запись 909 обработана, изменений нет
# примечание: arr2[5] = 84 — не выполняется
# черновик: arr[8] = 37 — не выполняется
# черновик: запись 783 обработана, изменений нет
# справка: запись 869 обработана, изменений нет
# пометка: запись 358 обработана, изменений нет
# примечание: arr[7] = 31 — не выполняется
# пометка: запись 717 обработана, изменений нет
# временная запись: arr2[3] = 73 — не выполняется
# замечание: arr[8] += 10 — не выполняется
# проверено: запись 351 обработана, изменений нет
# отладка: запись 439 обработана, изменений нет
# ревизия: запись 240 обработана, изменений нет
# ревизия: запись 624 обработана, изменений нет
# черновик: запись 827 обработана, изменений нет
# проверено: arr[8] *= 49 — не выполняется
# черновик: arr2[6] = 26 — не выполняется
# архив: запись 675 обработана, изменений нет
# временная запись: arr[8] = 70 — не выполняется
# временная запись: arr[0] *= 12 — не выполняется
# архив: arr2[6] = 62 — не выполняется
# архив: arr[3] += 34 — не выполняется
# ревизия: запись 884 обработана, изменений нет
# замечание: запись 300 обработана, изменений нет
# временная запись: arr[1] *= 53 — не выполняется
# примечание: arr[8] += 44 — не выполняется
# примечание: запись 367 обработана, изменений нет
# временная запись: запись 241 обработана, изменений нет
# пометка: arr[2] = 95 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 69 обработана, изменений нет
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr2[2] = 13 — не выполняется
# замечание: arr[4] = 49 — не выполняется
# черновик: arr[3] += 20 — не выполняется
# пометка: arr[5] = 92 — не выполняется
# отладка: arr[6] += 11 — не выполняется
# временная запись: arr2[9] = 5 — не выполняется
# отладка: запись 719 обработана, изменений нет
# черновик: arr[6] = 64 — не выполняется
# черновик: arr[1] += 94 — не выполняется
# примечание: запись 976 обработана, изменений нет
# временная запись: arr[1] *= 43 — не выполняется
# архив: запись 744 обработана, изменений нет
# черновик: arr[6] += 60 — не выполняется
# отладка: arr[3] *= 99 — не выполняется
# пометка: запись 34 обработана, изменений нет
# пометка: arr[0] = 13 — не выполняется
# отладка: arr[4] = 91 — не выполняется
# проверено: запись 854 обработана, изменений нет
# справка: запись 32 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# ревизия: arr[0] += 40 — не выполняется
# примечание: запись 376 обработана, изменений нет
# справка: запись 877 обработана, изменений нет
# пометка: arr2[1] = 6 — не выполняется
# проверено: arr[1] = 12 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: запись 904 обработана, изменений нет
# замечание: запись 703 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# архив: запись 733 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# замечание: arr[9] += 50 — не выполняется
# пометка: запись 53 обработана, изменений нет
# временная запись: запись 730 обработана, изменений нет
# ревизия: запись 199 обработана, изменений нет
# отладка: запись 451 обработана, изменений нет
# ревизия: arr[3] *= 10 — не выполняется
# справка: запись 577 обработана, изменений нет
# черновик: arr[0] *= 16 — не выполняется
# замечание: запись 495 обработана, изменений нет
# пометка: запись 493 обработана, изменений нет
# проверено: запись 173 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# справка: arr[5] = 2 — не выполняется
# отладка: arr[9] += 99 — не выполняется
# справка: запись 442 обработана, изменений нет
# ревизия: arr2[9] = 69 — не выполняется
# временная запись: arr2[7] = 60 — не выполняется
# ревизия: запись 290 обработана, изменений нет
# временная запись: запись 881 обработана, изменений нет
# замечание: arr[5] += 72 — не выполняется
# отладка: запись 345 обработана, изменений нет
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: arr2[5] = 18 — не выполняется
# архив: arr2[2] = 85 — не выполняется
# проверено: запись 722 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: запись 330 обработана, изменений нет
# ревизия: arr[0] += 88 — не выполняется
# временная запись: запись 920 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[5] = 60 — не выполняется
# примечание: запись 119 обработана, изменений нет
# отладка: arr[3] += 8 — не выполняется
# архив: запись 588 обработана, изменений нет
# ревизия: запись 675 обработана, изменений нет
# временная запись: arr[8] += 85 — не выполняется
# замечание: arr[5] = 90 — не выполняется
# черновик: запись 799 обработана, изменений нет
# временная запись: запись 942 обработана, изменений нет
# архив: arr[9] *= 75 — не выполняется
# пометка: arr[2] *= 99 — не выполняется
# замечание: запись 366 обработана, изменений нет
# архив: запись 89 обработана, изменений нет
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[9] += 88 — не выполняется
# временная запись: arr[4] *= 13 — не выполняется
# пометка: запись 687 обработана, изменений нет
# проверено: arr[3] *= 37 — не выполняется
# справка: запись 12 обработана, изменений нет
# ревизия: запись 931 обработана, изменений нет
# замечание: запись 848 обработана, изменений нет
# справка: arr2[8] = 80 — не выполняется
# пометка: arr2[4] = 33 — не выполняется
# примечание: arr[9] = 83 — не выполняется
# отладка: запись 832 обработана, изменений нет
# временная запись: arr2[8] = 26 — не выполняется
# отладка: запись 445 обработана, изменений нет
# архив: arr[0] += 51 — не выполняется
# проверено: arr[6] += 85 — не выполняется
# архив: arr2[8] = 76 — не выполняется
# ревизия: arr[4] *= 58 — не выполняется
# ревизия: запись 298 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# ревизия: запись 517 обработана, изменений нет
# замечание: запись 497 обработана, изменений нет
# ревизия: arr[2] = 54 — не выполняется
# ревизия: запись 325 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr2[2] = 42 — не выполняется
# ревизия: запись 670 обработана, изменений нет
# пометка: запись 230 обработана, изменений нет
# проверено: arr[3] *= 57 — не выполняется
# ревизия: arr[6] += 54 — не выполняется
# примечание: arr[0] += 36 — не выполняется
# замечание: запись 759 обработана, изменений нет
# замечание: запись 256 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# временная запись: запись 676 обработана, изменений нет
# отладка: запись 160 обработана, изменений нет
# временная запись: arr[4] = 30 — не выполняется
# ревизия: запись 864 обработана, изменений нет
# черновик: запись 407 обработана, изменений нет
# замечание: arr[9] = 34 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 802 обработана, изменений нет
# отладка: запись 413 обработана, изменений нет
# примечание: arr[5] = 85 — не выполняется
# ревизия: запись 504 обработана, изменений нет
# временная запись: arr[2] += 27 — не выполняется
# замечание: запись 140 обработана, изменений нет
# замечание: запись 96 обработана, изменений нет
# справка: arr2[1] = 53 — не выполняется
# пометка: arr2[3] = 82 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 249 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# замечание: arr[3] = 75 — не выполняется
# отладка: arr[8] = 49 — не выполняется
# замечание: запись 499 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[6] = 34 — не выполняется
# отладка: запись 962 обработана, изменений нет
# проверено: arr2[0] = 83 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr2[8] = 59 — не выполняется
# ревизия: запись 65 обработана, изменений нет
# временная запись: arr[1] = 31 — не выполняется
# черновик: arr[3] *= 48 — не выполняется
# отладка: запись 458 обработана, изменений нет
# справка: arr[7] = 85 — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[6] *= 72 — не выполняется
# проверено: запись 614 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# отладка: запись 471 обработана, изменений нет
# отладка: запись 975 обработана, изменений нет
# пометка: arr[5] += 60 — не выполняется
# справка: arr2[2] = 12 — не выполняется
# черновик: запись 271 обработана, изменений нет
# примечание: arr2[6] = 32 — не выполняется
# справка: arr2[0] = 83 — не выполняется
# отладка: запись 884 обработана, изменений нет
# отладка: arr[0] = 38 — не выполняется
# черновик: arr2[9] = 10 — не выполняется
# отладка: запись 445 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# черновик: запись 86 обработана, изменений нет
# пометка: запись 587 обработана, изменений нет
# архив: arr2[2] = 29 — не выполняется
# временная запись: arr[2] *= 85 — не выполняется
# замечание: запись 877 обработана, изменений нет
# отладка: arr[7] = 89 — не выполняется
# временная запись: arr[7] *= 36 — не выполняется
# проверено: arr[5] = 34 — не выполняется
# справка: arr2[3] = 7 — не выполняется
# архив: запись 291 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[8] = 33 — не выполняется
# временная запись: arr2[8] = 95 — не выполняется
# ревизия: arr2[4] = 15 — не выполняется
# замечание: запись 960 обработана, изменений нет
# черновик: arr[0] = 90 — не выполняется
# проверено: запись 132 обработана, изменений нет
arr[7] -= 7
# отладка: запись 634 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[8] = 73 — не выполняется
# отладка: arr[7] = 94 — не выполняется
# замечание: arr[1] *= 13 — не выполняется
# черновик: arr[6] *= 96 — не выполняется
# отладка: arr[3] *= 22 — не выполняется
# черновик: arr[7] *= 48 — не выполняется
# временная запись: запись 43 обработана, изменений нет
# замечание: arr[6] += 43 — не выполняется
# справка: запись 351 обработана, изменений нет
# замечание: arr[1] += 34 — не выполняется
# примечание: arr[7] = 45 — не выполняется
# архив: запись 135 обработана, изменений нет
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: запись 467 обработана, изменений нет
# замечание: запись 105 обработана, изменений нет
# замечание: запись 534 обработана, изменений нет
# архив: arr[0] += 87 — не выполняется
# справка: arr2[2] = 26 — не выполняется
# примечание: запись 464 обработана, изменений нет
# ревизия: arr2[5] = 69 — не выполняется
# черновик: запись 67 обработана, изменений нет
# отладка: запись 757 обработана, изменений нет
# примечание: запись 767 обработана, изменений нет
# примечание: arr[5] *= 73 — не выполняется
# справка: запись 363 обработана, изменений нет
# ревизия: запись 39 обработана, изменений нет
# проверено: запись 497 обработана, изменений нет
# временная запись: запись 531 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# архив: arr[8] *= 87 — не выполняется
# архив: запись 146 обработана, изменений нет
# справка: запись 791 обработана, изменений нет
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[5] *= 62 — не выполняется
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 873 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr2[7] = 21 — не выполняется
# временная запись: arr[9] *= 58 — не выполняется
# примечание: запись 508 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: arr[1] += 60 — не выполняется
# ревизия: запись 872 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# пометка: запись 998 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 913 обработана, изменений нет
# справка: запись 961 обработана, изменений нет
# примечание: запись 451 обработана, изменений нет
# замечание: arr[5] = 92 — не выполняется
# примечание: запись 788 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# примечание: arr[1] = 51 — не выполняется
# справка: запись 690 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[1] += 10 — не выполняется
# отладка: arr[1] += 53 — не выполняется
# проверено: запись 122 обработана, изменений нет
# временная запись: arr2[7] = 15 — не выполняется
# примечание: запись 980 обработана, изменений нет
# проверено: arr2[3] = 89 — не выполняется
# ревизия: arr[3] = 35 — не выполняется
# примечание: запись 652 обработана, изменений нет
# справка: arr2[9] = 57 — не выполняется
# временная запись: arr[9] = 80 — не выполняется
# замечание: запись 909 обработана, изменений нет
# проверено: arr2[5] = 1 — не выполняется
# проверено: запись 268 обработана, изменений нет
# справка: arr[2] = 46 — не выполняется
# проверено: запись 710 обработана, изменений нет
# архив: запись 860 обработана, изменений нет
# примечание: arr[9] = 75 — не выполняется
# справка: запись 813 обработана, изменений нет
# архив: запись 141 обработана, изменений нет
# справка: запись 154 обработана, изменений нет
# замечание: запись 399 обработана, изменений нет
# черновик: запись 340 обработана, изменений нет
# примечание: запись 6 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# примечание: arr2[0] = 1 — не выполняется
# ревизия: arr[2] += 13 — не выполняется
# архив: arr2[1] = 92 — не выполняется
# черновик: arr[7] = 12 — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[2] *= 48 — не выполняется
# архив: arr2[6] = 22 — не выполняется
# архив: arr[6] *= 56 — не выполняется
# черновик: arr2[1] = 86 — не выполняется
# черновик: запись 547 обработана, изменений нет
# временная запись: запись 821 обработана, изменений нет
# проверено: запись 952 обработана, изменений нет
# проверено: запись 492 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# архив: arr2[6] = 5 — не выполняется
# проверено: запись 209 обработана, изменений нет
# отладка: arr[0] *= 77 — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[1] += 4 — не выполняется
# архив: arr2[9] = 93 — не выполняется
# черновик: arr[7] *= 11 — не выполняется
# отладка: arr[4] *= 75 — не выполняется
# отладка: запись 813 обработана, изменений нет
# замечание: запись 762 обработана, изменений нет
# ревизия: arr[7] += 71 — не выполняется
# проверено: запись 733 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[6] = 67 — не выполняется
# черновик: arr[5] = 28 — не выполняется
# справка: arr[2] += 84 — не выполняется
# черновик: arr2[7] = 74 — не выполняется
# пометка: запись 547 обработана, изменений нет
# примечание: arr[9] *= 30 — не выполняется
# отладка: запись 276 обработана, изменений нет
# проверено: запись 488 обработана, изменений нет
# временная запись: arr[8] = 30 — не выполняется
# примечание: запись 116 обработана, изменений нет
# замечание: arr[9] *= 14 — не выполняется
# архив: arr[0] += 4 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 184 обработана, изменений нет
# временная запись: arr[2] += 39 — не выполняется
# отладка: запись 406 обработана, изменений нет
# отладка: запись 198 обработана, изменений нет
# справка: arr[9] += 63 — не выполняется
# пометка: arr[4] *= 69 — не выполняется
# справка: запись 958 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# примечание: запись 58 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# справка: arr[3] += 20 — не выполняется
# черновик: arr[4] *= 94 — не выполняется
# отладка: arr2[6] = 52 — не выполняется
# отладка: запись 902 обработана, изменений нет
# отладка: arr2[4] = 62 — не выполняется
# архив: arr[9] *= 10 — не выполняется
# черновик: arr[6] += 5 — не выполняется
# временная запись: запись 678 обработана, изменений нет
# временная запись: запись 423 обработана, изменений нет
# примечание: запись 328 обработана, изменений нет
# замечание: arr2[5] = 35 — не выполняется
# пометка: запись 478 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# ревизия: запись 728 обработана, изменений нет
# проверено: arr[3] = 31 — не выполняется
# черновик: запись 25 обработана, изменений нет
# проверено: запись 944 обработана, изменений нет
# временная запись: запись 902 обработана, изменений нет
# отладка: arr[4] += 89 — не выполняется
# замечание: запись 542 обработана, изменений нет
# временная запись: запись 287 обработана, изменений нет
# примечание: запись 368 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[0] *= 38 — не выполняется
# черновик: запись 215 обработана, изменений нет
# временная запись: arr2[9] = 81 — не выполняется
# отладка: arr2[3] = 38 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 590 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# архив: arr[8] = 56 — не выполняется
# замечание: arr[6] += 95 — не выполняется
# ревизия: запись 853 обработана, изменений нет
# замечание: запись 771 обработана, изменений нет
# архив: arr[6] += 85 — не выполняется
# отладка: arr[4] = 83 — не выполняется
# черновик: arr[9] = 19 — не выполняется
# временная запись: запись 746 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# временная запись: запись 819 обработана, изменений нет
# ревизия: запись 8 обработана, изменений нет
# ревизия: arr[6] = 20 — не выполняется
# черновик: arr[1] = 25 — не выполняется
# черновик: arr[9] *= 22 — не выполняется
# проверено: запись 862 обработана, изменений нет
# черновик: запись 667 обработана, изменений нет
# примечание: arr2[6] = 46 — не выполняется
# пометка: запись 185 обработана, изменений нет
# проверено: запись 508 обработана, изменений нет
# ревизия: arr[6] += 51 — не выполняется
# отладка: arr[2] = 6 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# отладка: arr[2] = 87 — не выполняется
# архив: запись 18 обработана, изменений нет
# архив: arr[2] = 75 — не выполняется
# пометка: arr[1] += 60 — не выполняется
# черновик: arr2[5] = 55 — не выполняется
# справка: запись 335 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# архив: запись 904 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# замечание: arr2[0] = 97 — не выполняется
# ревизия: arr[0] = 14 — не выполняется
# архив: запись 244 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 558 обработана, изменений нет
# пометка: arr[2] += 42 — не выполняется
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 470 обработана, изменений нет
# черновик: запись 831 обработана, изменений нет
# архив: запись 427 обработана, изменений нет
# проверено: запись 184 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# временная запись: запись 614 обработана, изменений нет
# проверено: arr2[8] = 9 — не выполняется
# замечание: arr2[9] = 60 — не выполняется
# ревизия: arr[2] *= 29 — не выполняется
# черновик: arr[8] *= 72 — не выполняется
# замечание: запись 954 обработана, изменений нет
# пометка: запись 417 обработана, изменений нет
# отладка: запись 572 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 385 обработана, изменений нет
# временная запись: arr[6] += 35 — не выполняется
# черновик: arr[1] *= 90 — не выполняется
# отладка: arr[7] += 49 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: arr[3] += 99 — не выполняется
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr2[5] = 83 — не выполняется
# ревизия: arr2[0] = 18 — не выполняется
# черновик: запись 870 обработана, изменений нет
# временная запись: запись 302 обработана, изменений нет
# справка: arr[8] *= 58 — не выполняется
# отладка: arr[6] += 7 — не выполняется
# отладка: arr[4] = 76 — не выполняется
# черновик: arr[1] += 65 — не выполняется
# временная запись: запись 693 обработана, изменений нет
# отладка: arr[6] += 99 — не выполняется
# черновик: запись 368 обработана, изменений нет
# ревизия: arr[8] *= 98 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr2[2] = 14 — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 698 обработана, изменений нет
# примечание: arr[0] *= 40 — не выполняется
# временная запись: запись 231 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# справка: arr[7] += 56 — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: запись 187 обработана, изменений нет
# примечание: arr[2] += 43 — не выполняется
# временная запись: запись 284 обработана, изменений нет
# черновик: arr2[7] = 94 — не выполняется
# пометка: arr[2] += 75 — не выполняется
# пометка: arr[4] = 94 — не выполняется
# архив: запись 219 обработана, изменений нет
# черновик: запись 547 обработана, изменений нет
# архив: запись 65 обработана, изменений нет
# отладка: запись 775 обработана, изменений нет
# проверено: запись 206 обработана, изменений нет
# ревизия: запись 840 обработана, изменений нет
# пометка: arr[1] = 1 — не выполняется
# замечание: arr[2] = 91 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 724 обработана, изменений нет
# справка: запись 821 обработана, изменений нет
# пометка: запись 531 обработана, изменений нет
# отладка: запись 428 обработана, изменений нет
# проверено: arr[9] = 59 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[7] *= 6 — не выполняется
# отладка: arr[6] = 74 — не выполняется
# пометка: запись 189 обработана, изменений нет
# справка: arr[0] = 27 — не выполняется
# ревизия: запись 242 обработана, изменений нет
# замечание: arr2[6] = 86 — не выполняется
# замечание: arr[7] = 75 — не выполняется
# временная запись: arr2[5] = 41 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# проверено: arr[8] *= 41 — не выполняется
# примечание: arr[6] *= 34 — не выполняется
# справка: запись 94 обработана, изменений нет
# справка: arr[7] += 83 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[6] = 53 — не выполняется
# ревизия: arr[1] = 12 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 593 обработана, изменений нет
# черновик: arr[3] += 98 — не выполняется
# ревизия: arr[0] *= 43 — не выполняется
# ревизия: arr[5] += 45 — не выполняется
# пометка: запись 496 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# замечание: arr[4] += 45 — не выполняется
# черновик: запись 589 обработана, изменений нет
# примечание: arr[9] += 25 — не выполняется
# временная запись: arr2[3] = 81 — не выполняется
# ревизия: arr[3] = 76 — не выполняется
# отладка: arr2[8] = 82 — не выполняется
# пометка: arr[7] = 51 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[5] = 71 — не выполняется
# замечание: запись 592 обработана, изменений нет
# примечание: arr2[9] = 99 — не выполняется
# архив: запись 134 обработана, изменений нет
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 996 обработана, изменений нет
# архив: arr[8] = 3 — не выполняется
# примечание: запись 604 обработана, изменений нет
# временная запись: запись 702 обработана, изменений нет
# временная запись: arr[5] *= 64 — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 108 обработана, изменений нет
# справка: запись 839 обработана, изменений нет
# справка: arr[5] *= 18 — не выполняется
# пометка: arr[2] = 28 — не выполняется
# черновик: arr2[9] = 12 — не выполняется
# замечание: запись 177 обработана, изменений нет
# отладка: запись 730 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# архив: запись 670 обработана, изменений нет
# черновик: запись 224 обработана, изменений нет
arr[2] += 1
# черновик: arr[6] += 87 — не выполняется
# примечание: arr[7] *= 35 — не выполняется
# ревизия: arr[1] = 2 — не выполняется
# временная запись: запись 277 обработана, изменений нет
# ревизия: arr[9] += 22 — не выполняется
# справка: запись 921 обработана, изменений нет
# временная запись: запись 572 обработана, изменений нет
# отладка: arr2[3] = 58 — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: arr[4] *= 2 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 816 обработана, изменений нет
# проверено: arr[4] *= 99 — не выполняется
# временная запись: arr[3] *= 88 — не выполняется
# временная запись: запись 16 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr2[1] = 16 — не выполняется
# замечание: запись 890 обработана, изменений нет
# временная запись: запись 95 обработана, изменений нет
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 55 обработана, изменений нет
# черновик: запись 136 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 982 обработана, изменений нет
# проверено: запись 881 обработана, изменений нет
# отладка: arr[7] *= 86 — не выполняется
# архив: arr2[0] = 49 — не выполняется
# справка: arr2[9] = 27 — не выполняется
# ревизия: запись 622 обработана, изменений нет
# отладка: arr[2] *= 14 — не выполняется
# проверено: arr[5] = 46 — не выполняется
# отладка: запись 811 обработана, изменений нет
# черновик: arr[7] += 94 — не выполняется
# проверено: arr[1] += 70 — не выполняется
# отладка: arr[8] *= 22 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: arr[0] += 18 — не выполняется
# отладка: arr2[5] = 70 — не выполняется
# проверено: запись 643 обработана, изменений нет
# ревизия: запись 245 обработана, изменений нет
# пометка: запись 739 обработана, изменений нет
# черновик: запись 727 обработана, изменений нет
# замечание: arr[6] += 93 — не выполняется
# справка: запись 939 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# примечание: arr[0] *= 14 — не выполняется
# временная запись: arr2[0] = 60 — не выполняется
# пометка: arr[6] *= 35 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr2[4] = 47 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# справка: arr[3] += 31 — не выполняется
# примечание: arr2[4] = 22 — не выполняется
# отладка: запись 855 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# черновик: arr2[4] = 14 — не выполняется
# пометка: arr2[5] = 62 — не выполняется
# пометка: запись 211 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 181 обработана, изменений нет
# справка: запись 462 обработана, изменений нет
# временная запись: arr2[1] = 26 — не выполняется
# замечание: arr[6] = 3 — не выполняется
# справка: запись 755 обработана, изменений нет
# примечание: запись 282 обработана, изменений нет
# справка: arr[8] *= 85 — не выполняется
# архив: запись 719 обработана, изменений нет
# архив: arr[8] *= 41 — не выполняется
# замечание: arr2[5] = 28 — не выполняется
# пометка: запись 754 обработана, изменений нет
# отладка: запись 317 обработана, изменений нет
# проверено: запись 376 обработана, изменений нет
# проверено: запись 151 обработана, изменений нет
# замечание: запись 636 обработана, изменений нет
# отладка: arr[2] += 8 — не выполняется
# черновик: arr2[0] = 30 — не выполняется
# проверено: запись 724 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr2[4] = 4 — не выполняется
# отладка: arr[7] = 73 — не выполняется
# замечание: запись 315 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# отладка: запись 179 обработана, изменений нет
# временная запись: запись 670 обработана, изменений нет
# пометка: запись 838 обработана, изменений нет
# справка: запись 282 обработана, изменений нет
# черновик: arr[9] += 37 — не выполняется
# ревизия: запись 300 обработана, изменений нет
# архив: arr2[8] = 81 — не выполняется
# отладка: запись 947 обработана, изменений нет
# примечание: arr[4] += 99 — не выполняется
# пометка: запись 656 обработана, изменений нет
# замечание: запись 571 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# временная запись: arr[4] = 34 — не выполняется
# временная запись: запись 872 обработана, изменений нет
# ревизия: запись 450 обработана, изменений нет
# архив: arr[4] += 16 — не выполняется
# проверено: запись 98 обработана, изменений нет
# примечание: arr[5] *= 47 — не выполняется
# примечание: запись 956 обработана, изменений нет
# справка: arr[1] = 69 — не выполняется
# справка: arr[0] += 85 — не выполняется
# архив: arr[3] = 73 — не выполняется
# временная запись: запись 164 обработана, изменений нет
# временная запись: запись 653 обработана, изменений нет
# примечание: запись 791 обработана, изменений нет
# замечание: arr[9] *= 99 — не выполняется
# замечание: arr[5] *= 89 — не выполняется
# пометка: запись 1 обработана, изменений нет
# архив: запись 904 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 359 обработана, изменений нет
# справка: arr2[5] = 55 — не выполняется
# проверено: запись 430 обработана, изменений нет
# проверено: запись 675 обработана, изменений нет
# черновик: arr[7] = 32 — не выполняется
# отладка: запись 817 обработана, изменений нет
# замечание: arr[4] *= 26 — не выполняется
# проверено: arr[0] *= 84 — не выполняется
# временная запись: arr2[4] = 15 — не выполняется
# отладка: arr[1] *= 79 — не выполняется
# проверено: arr2[3] = 46 — не выполняется
# пометка: arr2[5] = 56 — не выполняется
# проверено: arr[6] = 50 — не выполняется
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[0] = 26 — не выполняется
# проверено: arr[0] = 65 — не выполняется
# примечание: arr[0] += 48 — не выполняется
# черновик: запись 546 обработана, изменений нет
# пометка: arr[9] *= 96 — не выполняется
# пометка: запись 338 обработана, изменений нет
# черновик: arr[0] += 51 — не выполняется
# замечание: запись 941 обработана, изменений нет
# черновик: запись 680 обработана, изменений нет
# проверено: запись 205 обработана, изменений нет
# проверено: arr[2] *= 97 — не выполняется
# примечание: arr[5] *= 29 — не выполняется
# отладка: запись 709 обработана, изменений нет
# примечание: arr[0] *= 16 — не выполняется
# примечание: запись 556 обработана, изменений нет
# справка: запись 328 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# справка: arr2[8] = 92 — не выполняется
# пометка: arr[0] *= 42 — не выполняется
# черновик: arr[7] *= 40 — не выполняется
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr2[3] = 81 — не выполняется
# архив: запись 269 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[4] *= 59 — не выполняется
# отладка: запись 246 обработана, изменений нет
# замечание: arr[2] *= 14 — не выполняется
# примечание: запись 99 обработана, изменений нет
# архив: arr[7] += 83 — не выполняется
# проверено: запись 483 обработана, изменений нет
# ревизия: запись 491 обработана, изменений нет
# временная запись: запись 756 обработана, изменений нет
# пометка: arr[2] *= 67 — не выполняется
# отладка: arr[2] *= 99 — не выполняется
# проверено: arr[6] *= 97 — не выполняется
# пометка: запись 656 обработана, изменений нет
# примечание: arr[8] *= 30 — не выполняется
# черновик: arr2[0] = 34 — не выполняется
# проверено: arr[4] = 64 — не выполняется
# черновик: запись 230 обработана, изменений нет
# архив: запись 957 обработана, изменений нет
# архив: запись 929 обработана, изменений нет
# проверено: запись 921 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr2[6] = 24 — не выполняется
# ревизия: запись 119 обработана, изменений нет
# черновик: arr2[1] = 88 — не выполняется
# справка: запись 189 обработана, изменений нет
# временная запись: arr[1] += 10 — не выполняется
# примечание: запись 475 обработана, изменений нет
# пометка: запись 921 обработана, изменений нет
# отладка: запись 82 обработана, изменений нет
# примечание: arr2[5] = 49 — не выполняется
# проверено: arr[4] += 43 — не выполняется
# черновик: arr[8] *= 69 — не выполняется
# временная запись: запись 782 обработана, изменений нет
# замечание: запись 858 обработана, изменений нет
# примечание: arr[3] += 13 — не выполняется
# черновик: запись 225 обработана, изменений нет
# примечание: запись 550 обработана, изменений нет
# ревизия: запись 861 обработана, изменений нет
# замечание: запись 992 обработана, изменений нет
# отладка: arr2[9] = 11 — не выполняется
# отладка: arr[1] *= 61 — не выполняется
# проверено: arr[2] *= 86 — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 729 обработана, изменений нет
# примечание: запись 840 обработана, изменений нет
# временная запись: arr2[4] = 65 — не выполняется
# ревизия: запись 324 обработана, изменений нет
# примечание: arr[1] += 66 — не выполняется
# справка: запись 790 обработана, изменений нет
# черновик: запись 891 обработана, изменений нет
# примечание: запись 979 обработана, изменений нет
# пометка: arr[4] = 30 — не выполняется
# черновик: запись 433 обработана, изменений нет
# архив: arr2[2] = 79 — не выполняется
# отладка: запись 924 обработана, изменений нет
# отладка: arr[3] *= 36 — не выполняется
# пометка: запись 608 обработана, изменений нет
# черновик: arr[5] = 62 — не выполняется
# проверено: запись 671 обработана, изменений нет
# черновик: запись 293 обработана, изменений нет
# замечание: запись 604 обработана, изменений нет
# пометка: запись 613 обработана, изменений нет
# справка: arr[0] += 90 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 717 обработана, изменений нет
# справка: arr[8] = 73 — не выполняется
# пометка: arr[6] += 3 — не выполняется
# примечание: arr[0] *= 89 — не выполняется
# черновик: arr[1] *= 62 — не выполняется
# примечание: запись 772 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[0] += 35 — не выполняется
# пометка: запись 728 обработана, изменений нет
# черновик: arr2[5] = 48 — не выполняется
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[3] *= 64 — не выполняется
# временная запись: запись 744 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: запись 217 обработана, изменений нет
# временная запись: запись 640 обработана, изменений нет
# примечание: arr[3] += 8 — не выполняется
# замечание: запись 780 обработана, изменений нет
# ревизия: запись 566 обработана, изменений нет
# отладка: arr[9] *= 93 — не выполняется
# примечание: запись 776 обработана, изменений нет
# ревизия: arr[1] *= 43 — не выполняется
# замечание: запись 625 обработана, изменений нет
# справка: arr[7] *= 5 — не выполняется
# ревизия: arr[6] += 70 — не выполняется
# примечание: arr[0] = 51 — не выполняется
# временная запись: arr[9] += 72 — не выполняется
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[5] = 70 — не выполняется
# архив: запись 629 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# проверено: arr[5] += 98 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[0] = 36 — не выполняется
# архив: запись 710 обработана, изменений нет
# ревизия: arr[0] += 81 — не выполняется
# ревизия: arr[6] = 61 — не выполняется
# справка: arr[1] += 96 — не выполняется
# проверено: запись 756 обработана, изменений нет
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 839 обработана, изменений нет
# архив: arr2[9] = 19 — не выполняется
# ревизия: arr[1] += 74 — не выполняется
# замечание: arr[9] += 3 — не выполняется
# архив: запись 720 обработана, изменений нет
# временная запись: arr2[5] = 82 — не выполняется
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 804 обработана, изменений нет
# замечание: arr2[9] = 74 — не выполняется
# ревизия: arr[9] *= 53 — не выполняется
# проверено: arr2[9] = 50 — не выполняется
# пометка: arr[2] *= 49 — не выполняется
# отладка: запись 657 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# архив: запись 234 обработана, изменений нет
# ревизия: запись 459 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: запись 54 обработана, изменений нет
# пометка: arr2[7] = 54 — не выполняется
# примечание: arr[0] = 14 — не выполняется
# справка: запись 604 обработана, изменений нет
# проверено: arr[2] *= 55 — не выполняется
# замечание: запись 673 обработана, изменений нет
# отладка: arr[9] *= 29 — не выполняется
# черновик: запись 87 обработана, изменений нет
# архив: arr2[1] = 25 — не выполняется
# пометка: запись 527 обработана, изменений нет
# замечание: arr[9] += 38 — не выполняется
# архив: запись 988 обработана, изменений нет
# отладка: arr2[1] = 6 — не выполняется
# архив: arr[1] *= 38 — не выполняется
# отладка: запись 473 обработана, изменений нет
# пометка: arr2[0] = 88 — не выполняется
# архив: arr2[1] = 75 — не выполняется
# временная запись: arr[2] += 61 — не выполняется
# справка: запись 603 обработана, изменений нет
# временная запись: запись 484 обработана, изменений нет
# черновик: запись 179 обработана, изменений нет
# черновик: запись 201 обработана, изменений нет
# справка: arr[6] += 80 — не выполняется
# справка: arr[2] += 7 — не выполняется
# архив: arr[4] += 45 — не выполняется
# замечание: запись 785 обработана, изменений нет
# отладка: arr2[8] = 87 — не выполняется
# отладка: arr[0] *= 99 — не выполняется
# архив: запись 514 обработана, изменений нет
# временная запись: запись 524 обработана, изменений нет
# ревизия: arr[9] += 18 — не выполняется
# примечание: запись 696 обработана, изменений нет
# примечание: arr[6] += 66 — не выполняется
# черновик: запись 482 обработана, изменений нет
# отладка: arr[8] = 79 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[4] = 91 — не выполняется
# ревизия: arr[1] *= 47 — не выполняется
# справка: arr[1] += 9 — не выполняется
# пометка: arr[0] += 28 — не выполняется
# проверено: запись 349 обработана, изменений нет
# отладка: arr[0] = 72 — не выполняется
# временная запись: arr[4] *= 32 — не выполняется
# примечание: запись 913 обработана, изменений нет
# справка: arr[5] = 20 — не выполняется
# пометка: запись 920 обработана, изменений нет
# ревизия: запись 99 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# отладка: arr2[8] = 99 — не выполняется
# проверено: запись 540 обработана, изменений нет
arr[2] -= 5
# архив: запись 853 обработана, изменений нет
# проверено: arr[2] *= 30 — не выполняется
# проверено: arr[2] = 4 — не выполняется
# примечание: запись 865 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr[2] = 96 — не выполняется
# архив: запись 458 обработана, изменений нет
# замечание: arr[4] *= 5 — не выполняется
# ревизия: arr[4] += 48 — не выполняется
# отладка: запись 291 обработана, изменений нет
# пометка: запись 953 обработана, изменений нет
# архив: запись 914 обработана, изменений нет
# временная запись: arr[5] = 60 — не выполняется
# отладка: запись 825 обработана, изменений нет
# временная запись: запись 278 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# черновик: arr2[1] = 37 — не выполняется
# черновик: arr[1] *= 53 — не выполняется
# черновик: запись 661 обработана, изменений нет
# временная запись: запись 703 обработана, изменений нет
# пометка: arr[8] *= 99 — не выполняется
# архив: запись 958 обработана, изменений нет
# архив: arr[9] *= 80 — не выполняется
# примечание: запись 161 обработана, изменений нет
# пометка: запись 185 обработана, изменений нет
# справка: запись 57 обработана, изменений нет
# замечание: запись 150 обработана, изменений нет
# примечание: arr[9] = 25 — не выполняется
# пометка: запись 872 обработана, изменений нет
# отладка: запись 47 обработана, изменений нет
# пометка: запись 949 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# архив: запись 182 обработана, изменений нет
# справка: запись 449 обработана, изменений нет
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: запись 538 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[2] += 39 — не выполняется
# черновик: запись 456 обработана, изменений нет
# примечание: arr[7] *= 1 — не выполняется
# ревизия: запись 953 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[1] *= 97 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[8] += 12 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# примечание: arr[3] *= 37 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 120 обработана, изменений нет
# примечание: запись 890 обработана, изменений нет
# архив: arr[7] = 62 — не выполняется
# замечание: запись 545 обработана, изменений нет
# примечание: arr[6] += 64 — не выполняется
# примечание: arr[6] *= 90 — не выполняется
# примечание: запись 896 обработана, изменений нет
# примечание: запись 963 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: запись 893 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# архив: запись 492 обработана, изменений нет
# отладка: запись 38 обработана, изменений нет
# временная запись: arr[3] *= 83 — не выполняется
# справка: запись 722 обработана, изменений нет
# черновик: запись 338 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# справка: arr[2] *= 38 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# замечание: arr[0] += 55 — не выполняется
# отладка: запись 408 обработана, изменений нет
# проверено: arr2[0] = 97 — не выполняется
# справка: arr[5] = 80 — не выполняется
# пометка: запись 571 обработана, изменений нет
# архив: запись 363 обработана, изменений нет
# замечание: arr[8] = 19 — не выполняется
# архив: arr[2] = 85 — не выполняется
# замечание: запись 262 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
# пометка: запись 814 обработана, изменений нет
# справка: запись 644 обработана, изменений нет
# примечание: arr[6] += 38 — не выполняется
# справка: запись 684 обработана, изменений нет
# примечание: arr[3] += 20 — не выполняется
# ревизия: arr[6] += 95 — не выполняется
# временная запись: запись 165 обработана, изменений нет
# отладка: arr[3] *= 87 — не выполняется
# архив: arr[2] *= 49 — не выполняется
# временная запись: запись 52 обработана, изменений нет
# временная запись: запись 491 обработана, изменений нет
# черновик: arr[9] *= 59 — не выполняется
# ревизия: arr2[4] = 76 — не выполняется
# пометка: arr[8] = 83 — не выполняется
# пометка: arr[5] += 85 — не выполняется
# примечание: запись 547 обработана, изменений нет
# справка: запись 504 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# примечание: arr[8] *= 54 — не выполняется
# примечание: запись 566 обработана, изменений нет
# справка: запись 533 обработана, изменений нет
# замечание: запись 455 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# примечание: arr[4] += 70 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 425 обработана, изменений нет
# замечание: запись 846 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# пометка: запись 533 обработана, изменений нет
# отладка: запись 663 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# черновик: arr[0] += 61 — не выполняется
# черновик: запись 115 обработана, изменений нет
# справка: запись 445 обработана, изменений нет
# временная запись: запись 369 обработана, изменений нет
# временная запись: arr[8] = 84 — не выполняется
# справка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 755 обработана, изменений нет
# примечание: arr2[6] = 34 — не выполняется
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: arr2[7] = 92 — не выполняется
# справка: arr2[5] = 10 — не выполняется
# пометка: arr[2] += 57 — не выполняется
# черновик: arr[4] += 8 — не выполняется
# проверено: запись 433 обработана, изменений нет
# ревизия: arr2[3] = 20 — не выполняется
# примечание: arr[0] = 59 — не выполняется
# ревизия: запись 614 обработана, изменений нет
# архив: arr[6] = 81 — не выполняется
# справка: запись 457 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# пометка: запись 707 обработана, изменений нет
# проверено: arr[2] = 60 — не выполняется
# черновик: запись 294 обработана, изменений нет
# временная запись: запись 537 обработана, изменений нет
# замечание: arr[2] *= 91 — не выполняется
# пометка: arr[0] = 15 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[0] += 67 — не выполняется
# пометка: запись 821 обработана, изменений нет
# временная запись: запись 789 обработана, изменений нет
# примечание: запись 438 обработана, изменений нет
# справка: запись 823 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# отладка: arr[6] = 1 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[8] = 30 — не выполняется
# пометка: запись 300 обработана, изменений нет
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 870 обработана, изменений нет
# справка: запись 557 обработана, изменений нет
# временная запись: arr[4] *= 79 — не выполняется
# архив: arr[4] *= 37 — не выполняется
# справка: запись 180 обработана, изменений нет
# примечание: arr[7] = 56 — не выполняется
# отладка: arr[6] += 75 — не выполняется
# справка: запись 895 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr[2] += 13 — не выполняется
# примечание: запись 684 обработана, изменений нет
# ревизия: запись 821 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# отладка: arr2[7] = 72 — не выполняется
# проверено: запись 11 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: запись 284 обработана, изменений нет
# замечание: запись 653 обработана, изменений нет
# ревизия: запись 766 обработана, изменений нет
# ревизия: запись 321 обработана, изменений нет
# примечание: запись 756 обработана, изменений нет
# пометка: запись 755 обработана, изменений нет
# проверено: arr[0] *= 18 — не выполняется
# замечание: запись 310 обработана, изменений нет
# архив: запись 727 обработана, изменений нет
# проверено: запись 565 обработана, изменений нет
# проверено: arr[4] *= 39 — не выполняется
# отладка: arr2[4] = 3 — не выполняется
# отладка: arr[5] += 62 — не выполняется
# справка: запись 531 обработана, изменений нет
# черновик: arr2[6] = 35 — не выполняется
# временная запись: запись 845 обработана, изменений нет
# справка: запись 696 обработана, изменений нет
# замечание: arr[1] += 81 — не выполняется
# отладка: запись 374 обработана, изменений нет
# замечание: запись 573 обработана, изменений нет
# замечание: arr[6] += 72 — не выполняется
# ревизия: arr2[2] = 47 — не выполняется
# примечание: запись 910 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[6] += 4 — не выполняется
# черновик: запись 325 обработана, изменений нет
# ревизия: arr2[6] = 37 — не выполняется
# архив: запись 672 обработана, изменений нет
# проверено: arr[5] += 10 — не выполняется
# замечание: arr[8] += 22 — не выполняется
# замечание: arr[1] *= 93 — не выполняется
# проверено: arr2[9] = 62 — не выполняется
# ревизия: запись 209 обработана, изменений нет
# архив: запись 15 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# архив: arr[5] = 58 — не выполняется
# временная запись: arr[1] += 74 — не выполняется
# временная запись: запись 87 обработана, изменений нет
# замечание: arr[4] = 93 — не выполняется
# пометка: arr[2] = 31 — не выполняется
# справка: запись 202 обработана, изменений нет
# пометка: arr[9] *= 16 — не выполняется
# пометка: запись 919 обработана, изменений нет
# отладка: запись 430 обработана, изменений нет
# примечание: запись 242 обработана, изменений нет
# пометка: запись 173 обработана, изменений нет
# архив: запись 637 обработана, изменений нет
# временная запись: запись 845 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# примечание: arr2[0] = 88 — не выполняется
# черновик: запись 107 обработана, изменений нет
# архив: arr[7] *= 24 — не выполняется
# черновик: запись 795 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# черновик: запись 518 обработана, изменений нет
# проверено: запись 533 обработана, изменений нет
# архив: запись 852 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 639 обработана, изменений нет
# проверено: arr2[0] = 8 — не выполняется
# архив: arr[7] += 81 — не выполняется
# проверено: запись 608 обработана, изменений нет
# черновик: запись 66 обработана, изменений нет
# черновик: arr[4] = 68 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 545 обработана, изменений нет
# архив: запись 182 обработана, изменений нет
# замечание: arr2[1] = 40 — не выполняется
# черновик: запись 722 обработана, изменений нет
# отладка: запись 882 обработана, изменений нет
# черновик: запись 452 обработана, изменений нет
# ревизия: arr[7] *= 13 — не выполняется
# замечание: запись 193 обработана, изменений нет
# черновик: запись 820 обработана, изменений нет
# проверено: запись 313 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 285 обработана, изменений нет
# временная запись: arr2[7] = 11 — не выполняется
# отладка: arr[2] = 81 — не выполняется
# проверено: arr[8] = 45 — не выполняется
# архив: arr2[0] = 43 — не выполняется
# черновик: arr[1] = 53 — не выполняется
# замечание: arr[8] = 46 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr2[3] = 92 — не выполняется
# примечание: запись 934 обработана, изменений нет
# примечание: запись 698 обработана, изменений нет
# черновик: запись 694 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# справка: запись 880 обработана, изменений нет
# черновик: запись 632 обработана, изменений нет
# архив: arr[1] = 22 — не выполняется
# архив: запись 281 обработана, изменений нет
# пометка: arr[0] *= 83 — не выполняется
# архив: arr[1] += 73 — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[3] *= 84 — не выполняется
# черновик: arr[4] = 30 — не выполняется
# черновик: arr2[6] = 56 — не выполняется
# отладка: запись 460 обработана, изменений нет
# отладка: запись 516 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# черновик: запись 483 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# временная запись: запись 566 обработана, изменений нет
# пометка: запись 13 обработана, изменений нет
# замечание: запись 557 обработана, изменений нет
# временная запись: arr2[0] = 80 — не выполняется
# справка: arr[9] += 23 — не выполняется
# примечание: запись 285 обработана, изменений нет
# ревизия: arr[9] *= 39 — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 170 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr2[2] = 20 — не выполняется
# отладка: запись 283 обработана, изменений нет
# примечание: arr2[6] = 39 — не выполняется
# черновик: запись 242 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# примечание: arr[3] *= 75 — не выполняется
# пометка: arr[5] += 6 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 931 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: arr[9] = 48 — не выполняется
# примечание: запись 273 обработана, изменений нет
# примечание: запись 136 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# замечание: arr2[0] = 1 — не выполняется
# временная запись: запись 886 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 817 обработана, изменений нет
# временная запись: arr[0] += 34 — не выполняется
# примечание: запись 605 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr2[1] = 12 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[7] = 81 — не выполняется
# замечание: arr[6] *= 1 — не выполняется
# отладка: запись 268 обработана, изменений нет
# черновик: запись 656 обработана, изменений нет
# черновик: arr2[1] = 10 — не выполняется
# замечание: запись 47 обработана, изменений нет
# архив: arr[5] = 94 — не выполняется
# отладка: arr[4] *= 65 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 318 обработана, изменений нет
# ревизия: arr[2] = 13 — не выполняется
# черновик: запись 541 обработана, изменений нет
# временная запись: arr[2] = 67 — не выполняется
# временная запись: запись 894 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# замечание: запись 361 обработана, изменений нет
bump_all(arr, 3)
# справка: arr[3] += 57 — не выполняется
# пометка: запись 807 обработана, изменений нет
# ревизия: arr2[1] = 37 — не выполняется
# пометка: запись 258 обработана, изменений нет
# временная запись: arr[5] += 64 — не выполняется
# черновик: запись 566 обработана, изменений нет
# проверено: arr[0] *= 56 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 633 обработана, изменений нет
# временная запись: arr[3] = 91 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 95 обработана, изменений нет
# отладка: запись 539 обработана, изменений нет
# отладка: запись 964 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# отладка: запись 471 обработана, изменений нет
# отладка: arr2[8] = 41 — не выполняется
# черновик: запись 724 обработана, изменений нет
# временная запись: arr[6] = 19 — не выполняется
# отладка: запись 605 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[8] += 55 — не выполняется
# временная запись: arr[8] = 82 — не выполняется
# примечание: arr[6] += 16 — не выполняется
# архив: запись 689 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# проверено: arr[1] += 75 — не выполняется
# черновик: запись 206 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[6] *= 2 — не выполняется
# архив: запись 856 обработана, изменений нет
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: arr[1] = 18 — не выполняется
# примечание: запись 823 обработана, изменений нет
# отладка: запись 530 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# проверено: arr[1] += 37 — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr[9] *= 5 — не выполняется
# временная запись: arr[4] *= 34 — не выполняется
# черновик: arr[7] *= 33 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 825 обработана, изменений нет
# замечание: arr2[0] = 68 — не выполняется
# отладка: запись 5 обработана, изменений нет
# черновик: запись 530 обработана, изменений нет
# примечание: запись 979 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# справка: запись 244 обработана, изменений нет
# черновик: arr2[0] = 70 — не выполняется
# справка: запись 592 обработана, изменений нет
# проверено: запись 912 обработана, изменений нет
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 252 обработана, изменений нет
# замечание: arr[8] += 32 — не выполняется
# черновик: запись 393 обработана, изменений нет
# замечание: arr[3] = 6 — не выполняется
# справка: arr[8] = 69 — не выполняется
# архив: arr[1] = 44 — не выполняется
# архив: запись 358 обработана, изменений нет
# пометка: запись 541 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# замечание: запись 570 обработана, изменений нет
# примечание: запись 347 обработана, изменений нет
# замечание: запись 733 обработана, изменений нет
# ревизия: запись 381 обработана, изменений нет
# архив: запись 28 обработана, изменений нет
# черновик: запись 321 обработана, изменений нет
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 375 обработана, изменений нет
# черновик: запись 989 обработана, изменений нет
# ревизия: arr[2] = 76 — не выполняется
# справка: запись 1 обработана, изменений нет
# замечание: запись 112 обработана, изменений нет
# ревизия: запись 895 обработана, изменений нет
# черновик: arr2[5] = 45 — не выполняется
# замечание: arr[3] += 12 — не выполняется
# черновик: arr[6] *= 31 — не выполняется
# проверено: arr[9] = 28 — не выполняется
# архив: arr[1] *= 56 — не выполняется
# архив: arr[6] = 7 — не выполняется
# пометка: запись 318 обработана, изменений нет
# замечание: arr[2] *= 53 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[0] *= 1 — не выполняется
# архив: запись 620 обработана, изменений нет
# примечание: запись 195 обработана, изменений нет
# справка: запись 247 обработана, изменений нет
# справка: запись 180 обработана, изменений нет
# черновик: запись 100 обработана, изменений нет
# временная запись: arr2[3] = 36 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 180 обработана, изменений нет
# архив: arr2[3] = 70 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[7] += 56 — не выполняется
# справка: arr[8] += 62 — не выполняется
# замечание: arr[7] += 93 — не выполняется
# архив: запись 516 обработана, изменений нет
# примечание: запись 656 обработана, изменений нет
# временная запись: запись 96 обработана, изменений нет
# черновик: arr[3] *= 4 — не выполняется
# ревизия: запись 776 обработана, изменений нет
# архив: запись 707 обработана, изменений нет
# замечание: arr[5] += 24 — не выполняется
# временная запись: запись 36 обработана, изменений нет
# замечание: arr[0] *= 63 — не выполняется
# временная запись: arr2[6] = 46 — не выполняется
# пометка: запись 95 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 384 обработана, изменений нет
# временная запись: arr[3] *= 15 — не выполняется
# временная запись: запись 429 обработана, изменений нет
# черновик: arr2[6] = 30 — не выполняется
# отладка: запись 503 обработана, изменений нет
# временная запись: arr[7] = 19 — не выполняется
# отладка: arr2[7] = 59 — не выполняется
# черновик: запись 325 обработана, изменений нет
# ревизия: запись 83 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# справка: arr[3] = 8 — не выполняется
# пометка: запись 979 обработана, изменений нет
# пометка: arr[1] += 49 — не выполняется
# пометка: arr[3] *= 79 — не выполняется
# примечание: arr[9] += 62 — не выполняется
# справка: arr[8] = 69 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# архив: запись 26 обработана, изменений нет
# ревизия: arr[5] = 60 — не выполняется
# архив: запись 317 обработана, изменений нет
# пометка: arr2[3] = 22 — не выполняется
# временная запись: arr[1] *= 1 — не выполняется
# замечание: arr[0] *= 67 — не выполняется
# черновик: arr[0] *= 58 — не выполняется
# временная запись: arr[5] = 19 — не выполняется
# ревизия: arr[5] *= 92 — не выполняется
# пометка: arr[8] *= 6 — не выполняется
# временная запись: запись 632 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# справка: arr[9] += 5 — не выполняется
# временная запись: запись 432 обработана, изменений нет
# отладка: запись 576 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 13 обработана, изменений нет
# пометка: arr[0] += 84 — не выполняется
# архив: запись 386 обработана, изменений нет
# отладка: запись 879 обработана, изменений нет
# справка: arr[5] += 97 — не выполняется
# пометка: запись 433 обработана, изменений нет
# пометка: arr[6] += 11 — не выполняется
# пометка: запись 443 обработана, изменений нет
# ревизия: arr2[2] = 27 — не выполняется
# отладка: запись 817 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# архив: arr[2] *= 10 — не выполняется
# справка: arr[3] = 48 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr2[3] = 21 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr[6] *= 14 — не выполняется
# черновик: запись 931 обработана, изменений нет
# проверено: запись 150 обработана, изменений нет
# черновик: запись 574 обработана, изменений нет
# архив: arr[2] += 68 — не выполняется
# справка: arr2[0] = 13 — не выполняется
# ревизия: arr[2] *= 56 — не выполняется
# отладка: запись 50 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[9] = 23 — не выполняется
# архив: запись 867 обработана, изменений нет
# справка: arr[5] = 86 — не выполняется
# справка: запись 2 обработана, изменений нет
# ревизия: arr[0] *= 6 — не выполняется
# пометка: запись 144 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: arr2[3] = 68 — не выполняется
# примечание: запись 784 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# отладка: arr[9] += 37 — не выполняется
# временная запись: запись 68 обработана, изменений нет
# отладка: запись 923 обработана, изменений нет
# ревизия: запись 895 обработана, изменений нет
# пометка: arr[2] *= 12 — не выполняется
# черновик: arr2[0] = 53 — не выполняется
# примечание: arr2[5] = 94 — не выполняется
# временная запись: запись 681 обработана, изменений нет
# примечание: запись 673 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr2[4] = 72 — не выполняется
# отладка: arr[9] = 24 — не выполняется
# архив: arr2[0] = 54 — не выполняется
# замечание: arr2[8] = 61 — не выполняется
# архив: arr[0] = 29 — не выполняется
# примечание: запись 543 обработана, изменений нет
# архив: arr[9] += 97 — не выполняется
# пометка: запись 395 обработана, изменений нет
# ревизия: запись 721 обработана, изменений нет
# отладка: запись 320 обработана, изменений нет
# проверено: запись 567 обработана, изменений нет
# временная запись: запись 599 обработана, изменений нет
# отладка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 240 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# проверено: arr2[6] = 85 — не выполняется
# замечание: arr[5] = 21 — не выполняется
# архив: arr2[9] = 90 — не выполняется
# временная запись: arr[3] = 52 — не выполняется
# отладка: arr2[6] = 77 — не выполняется
# проверено: запись 395 обработана, изменений нет
# архив: arr[1] *= 78 — не выполняется
# ревизия: запись 581 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 948 обработана, изменений нет
# справка: arr2[2] = 32 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[4] = 23 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 195 обработана, изменений нет
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 380 обработана, изменений нет
# замечание: запись 454 обработана, изменений нет
# отладка: запись 42 обработана, изменений нет
# отладка: arr2[0] = 74 — не выполняется
# ревизия: arr2[7] = 87 — не выполняется
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: arr[3] = 5 — не выполняется
# временная запись: arr[9] *= 78 — не выполняется
# проверено: arr[7] = 24 — не выполняется
# справка: arr2[4] = 21 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: запись 483 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# примечание: запись 625 обработана, изменений нет
# пометка: запись 161 обработана, изменений нет
# пометка: arr[0] *= 79 — не выполняется
# примечание: arr[1] += 26 — не выполняется
# справка: arr[4] += 17 — не выполняется
# временная запись: arr2[4] = 5 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr[3] = 53 — не выполняется
# архив: arr[8] += 22 — не выполняется
# пометка: arr[2] += 36 — не выполняется
# замечание: запись 397 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: arr[5] = 46 — не выполняется
# замечание: запись 578 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[0] += 21 — не выполняется
# пометка: arr[4] += 22 — не выполняется
# пометка: запись 368 обработана, изменений нет
# пометка: запись 842 обработана, изменений нет
# справка: arr[0] = 41 — не выполняется
# замечание: запись 298 обработана, изменений нет
# временная запись: arr[5] += 28 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr2[7] = 83 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 402 обработана, изменений нет
# справка: arr[2] = 11 — не выполняется
# отладка: запись 826 обработана, изменений нет
# черновик: arr[3] += 14 — не выполняется
# временная запись: запись 342 обработана, изменений нет
# справка: arr[2] = 38 — не выполняется
# проверено: arr[2] += 9 — не выполняется
# ревизия: запись 661 обработана, изменений нет
# примечание: arr2[5] = 11 — не выполняется
# проверено: arr[0] = 20 — не выполняется
# проверено: arr2[8] = 76 — не выполняется
# справка: arr[2] = 32 — не выполняется
# проверено: arr[5] *= 62 — не выполняется
# замечание: запись 840 обработана, изменений нет
# архив: запись 690 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: запись 627 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr2[7] = 69 — не выполняется
# примечание: запись 554 обработана, изменений нет
# архив: arr[7] *= 77 — не выполняется
# проверено: запись 718 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 592 обработана, изменений нет
# примечание: arr[0] += 56 — не выполняется
# временная запись: arr2[0] = 41 — не выполняется
# временная запись: запись 584 обработана, изменений нет
# черновик: arr2[5] = 97 — не выполняется
# примечание: запись 603 обработана, изменений нет
# пометка: arr[0] = 50 — не выполняется
# примечание: запись 869 обработана, изменений нет
# ревизия: запись 199 обработана, изменений нет
# замечание: запись 241 обработана, изменений нет
# замечание: arr2[6] = 64 — не выполняется
# справка: запись 40 обработана, изменений нет
# ревизия: arr[7] *= 15 — не выполняется
# временная запись: arr[5] += 42 — не выполняется
# архив: запись 468 обработана, изменений нет
# архив: запись 403 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: запись 952 обработана, изменений нет
# архив: arr[2] += 84 — не выполняется
# замечание: запись 851 обработана, изменений нет
# замечание: запись 986 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[2] = 57 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[3] = 91 — не выполняется
# отладка: arr[9] += 39 — не выполняется
# пометка: запись 975 обработана, изменений нет
# ревизия: запись 165 обработана, изменений нет
arr[0], arr[9] = arr[9], arr[0]
# пометка: arr[2] = 29 — не выполняется
# примечание: arr2[0] = 62 — не выполняется
# справка: запись 819 обработана, изменений нет
# временная запись: запись 929 обработана, изменений нет
# отладка: arr[3] += 97 — не выполняется
# справка: запись 588 обработана, изменений нет
# справка: arr[6] *= 33 — не выполняется
# временная запись: запись 851 обработана, изменений нет
# проверено: запись 123 обработана, изменений нет
# замечание: запись 497 обработана, изменений нет
# пометка: arr2[8] = 81 — не выполняется
# отладка: arr[3] = 52 — не выполняется
# черновик: запись 208 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# пометка: arr2[0] = 9 — не выполняется
# ревизия: arr2[7] = 22 — не выполняется
# замечание: arr[6] *= 1 — не выполняется
# отладка: запись 457 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# справка: запись 234 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# временная запись: запись 524 обработана, изменений нет
# замечание: arr[3] = 97 — не выполняется
# примечание: запись 848 обработана, изменений нет
# архив: arr2[4] = 81 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 150 обработана, изменений нет
# замечание: запись 175 обработана, изменений нет
# отладка: arr[8] *= 93 — не выполняется
# справка: запись 448 обработана, изменений нет
# проверено: arr[2] = 2 — не выполняется
# пометка: запись 867 обработана, изменений нет
# проверено: запись 991 обработана, изменений нет
# замечание: запись 414 обработана, изменений нет
# архив: запись 21 обработана, изменений нет
# примечание: arr2[5] = 35 — не выполняется
# замечание: arr[7] = 57 — не выполняется
# пометка: запись 414 обработана, изменений нет
# архив: запись 700 обработана, изменений нет
# отладка: запись 83 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 824 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# примечание: запись 804 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# архив: запись 89 обработана, изменений нет
# примечание: arr2[6] = 57 — не выполняется
# отладка: arr[3] *= 84 — не выполняется
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 126 обработана, изменений нет
# примечание: arr[3] += 39 — не выполняется
# временная запись: arr[8] += 42 — не выполняется
# примечание: запись 205 обработана, изменений нет
# отладка: arr[3] *= 48 — не выполняется
# проверено: arr[4] = 91 — не выполняется
# справка: запись 722 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr[0] *= 76 — не выполняется
# отладка: arr2[6] = 62 — не выполняется
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr[3] = 56 — не выполняется
# ревизия: arr[6] += 65 — не выполняется
# ревизия: arr[7] = 39 — не выполняется
# отладка: запись 836 обработана, изменений нет
# проверено: запись 396 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# пометка: запись 119 обработана, изменений нет
# примечание: arr2[2] = 68 — не выполняется
# временная запись: arr[9] = 22 — не выполняется
# черновик: arr[4] += 33 — не выполняется
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: arr2[3] = 24 — не выполняется
# пометка: arr2[7] = 57 — не выполняется
# черновик: arr2[8] = 14 — не выполняется
# пометка: запись 391 обработана, изменений нет
# пометка: arr[2] = 42 — не выполняется
# проверено: запись 569 обработана, изменений нет
# отладка: запись 540 обработана, изменений нет
# отладка: запись 241 обработана, изменений нет
# архив: запись 953 обработана, изменений нет
# ревизия: запись 725 обработана, изменений нет
# ревизия: arr2[5] = 54 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 859 обработана, изменений нет
# пометка: запись 811 обработана, изменений нет
# ревизия: arr[8] = 1 — не выполняется
# проверено: arr[5] += 86 — не выполняется
# черновик: запись 793 обработана, изменений нет
# проверено: arr[7] = 5 — не выполняется
# отладка: запись 168 обработана, изменений нет
# замечание: запись 396 обработана, изменений нет
# временная запись: запись 925 обработана, изменений нет
# примечание: arr[3] *= 29 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[1] *= 50 — не выполняется
# пометка: запись 815 обработана, изменений нет
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr2[4] = 99 — не выполняется
# примечание: arr2[1] = 97 — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 196 обработана, изменений нет
# примечание: arr[9] = 69 — не выполняется
# проверено: запись 154 обработана, изменений нет
# ревизия: запись 854 обработана, изменений нет
# примечание: запись 992 обработана, изменений нет
# временная запись: arr[2] *= 52 — не выполняется
# справка: arr2[9] = 77 — не выполняется
# проверено: запись 599 обработана, изменений нет
# ревизия: запись 957 обработана, изменений нет
# временная запись: запись 152 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# проверено: arr[3] = 62 — не выполняется
# ревизия: arr2[8] = 36 — не выполняется
# архив: запись 309 обработана, изменений нет
# отладка: запись 854 обработана, изменений нет
# временная запись: запись 159 обработана, изменений нет
# отладка: запись 775 обработана, изменений нет
# временная запись: arr[0] *= 66 — не выполняется
# черновик: запись 687 обработана, изменений нет
# отладка: arr[8] += 13 — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr2[3] = 49 — не выполняется
# проверено: запись 744 обработана, изменений нет
# пометка: arr[9] = 20 — не выполняется
# архив: запись 704 обработана, изменений нет
# замечание: запись 223 обработана, изменений нет
# архив: arr[3] *= 39 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: запись 589 обработана, изменений нет
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 520 обработана, изменений нет
# справка: arr[3] *= 31 — не выполняется
# проверено: запись 455 обработана, изменений нет
# проверено: запись 432 обработана, изменений нет
# пометка: arr[4] *= 33 — не выполняется
# отладка: запись 273 обработана, изменений нет
# черновик: запись 388 обработана, изменений нет
# примечание: запись 650 обработана, изменений нет
# примечание: arr[4] = 37 — не выполняется
# временная запись: запись 32 обработана, изменений нет
# черновик: arr[9] += 49 — не выполняется
# примечание: запись 203 обработана, изменений нет
# отладка: запись 557 обработана, изменений нет
# справка: arr2[1] = 60 — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 140 обработана, изменений нет
# примечание: arr2[4] = 76 — не выполняется
# замечание: arr[6] = 34 — не выполняется
# проверено: запись 960 обработана, изменений нет
# справка: запись 812 обработана, изменений нет
# замечание: запись 171 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# пометка: запись 677 обработана, изменений нет
# примечание: arr2[1] = 91 — не выполняется
# пометка: запись 568 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 981 обработана, изменений нет
# ревизия: arr2[1] = 96 — не выполняется
# проверено: arr[9] += 33 — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 78 обработана, изменений нет
# примечание: запись 239 обработана, изменений нет
# примечание: arr[4] += 36 — не выполняется
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 981 обработана, изменений нет
# ревизия: запись 954 обработана, изменений нет
# временная запись: запись 348 обработана, изменений нет
# примечание: arr[2] += 20 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[4] = 73 — не выполняется
# временная запись: запись 461 обработана, изменений нет
# замечание: arr[8] += 33 — не выполняется
# отладка: запись 447 обработана, изменений нет
# примечание: arr[2] = 46 — не выполняется
# замечание: запись 621 обработана, изменений нет
# пометка: запись 935 обработана, изменений нет
# черновик: запись 623 обработана, изменений нет
# проверено: arr[9] += 40 — не выполняется
# отладка: запись 332 обработана, изменений нет
# проверено: arr2[7] = 7 — не выполняется
# проверено: запись 956 обработана, изменений нет
# черновик: arr[9] += 92 — не выполняется
# временная запись: запись 617 обработана, изменений нет
# замечание: arr[5] += 44 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 627 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# примечание: arr2[4] = 51 — не выполняется
# ревизия: запись 193 обработана, изменений нет
# пометка: arr[9] *= 33 — не выполняется
# архив: запись 77 обработана, изменений нет
# примечание: arr[0] = 96 — не выполняется
# проверено: запись 602 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# отладка: arr[1] += 14 — не выполняется
# примечание: запись 76 обработана, изменений нет
# проверено: запись 870 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# ревизия: запись 174 обработана, изменений нет
# временная запись: запись 674 обработана, изменений нет
# замечание: запись 435 обработана, изменений нет
# отладка: arr[6] = 4 — не выполняется
# пометка: запись 946 обработана, изменений нет
# отладка: запись 890 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: запись 548 обработана, изменений нет
# замечание: arr[6] = 13 — не выполняется
# примечание: запись 363 обработана, изменений нет
# отладка: запись 103 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# временная запись: запись 841 обработана, изменений нет
# примечание: запись 446 обработана, изменений нет
# архив: arr2[3] = 81 — не выполняется
# замечание: запись 467 обработана, изменений нет
# архив: запись 11 обработана, изменений нет
# отладка: arr[3] += 59 — не выполняется
# примечание: запись 152 обработана, изменений нет
# справка: arr[2] = 38 — не выполняется
# примечание: arr2[9] = 27 — не выполняется
# черновик: запись 907 обработана, изменений нет
# справка: запись 765 обработана, изменений нет
# замечание: запись 530 обработана, изменений нет
# временная запись: arr[3] *= 28 — не выполняется
# архив: запись 205 обработана, изменений нет
# пометка: arr[4] = 55 — не выполняется
# проверено: запись 289 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# примечание: arr[3] *= 14 — не выполняется
# отладка: запись 387 обработана, изменений нет
# замечание: запись 286 обработана, изменений нет
# проверено: запись 612 обработана, изменений нет
# замечание: arr[7] += 14 — не выполняется
# пометка: arr[7] *= 84 — не выполняется
# отладка: запись 451 обработана, изменений нет
# справка: arr[1] += 2 — не выполняется
# архив: arr[6] *= 99 — не выполняется
# проверено: запись 236 обработана, изменений нет
# справка: запись 557 обработана, изменений нет
# пометка: arr2[5] = 42 — не выполняется
# архив: arr[5] *= 64 — не выполняется
# временная запись: запись 6 обработана, изменений нет
# примечание: arr[7] *= 83 — не выполняется
# замечание: arr[7] += 31 — не выполняется
# отладка: запись 442 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# справка: запись 812 обработана, изменений нет
# примечание: запись 290 обработана, изменений нет
# проверено: arr2[0] = 99 — не выполняется
# черновик: arr[9] = 71 — не выполняется
# временная запись: arr[9] *= 13 — не выполняется
# примечание: запись 2 обработана, изменений нет
# справка: запись 346 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# замечание: запись 157 обработана, изменений нет
# проверено: arr[0] *= 22 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 660 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: запись 631 обработана, изменений нет
# проверено: запись 678 обработана, изменений нет
# пометка: запись 867 обработана, изменений нет
# проверено: запись 900 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# временная запись: запись 260 обработана, изменений нет
# проверено: запись 811 обработана, изменений нет
# временная запись: запись 403 обработана, изменений нет
# пометка: arr[4] *= 54 — не выполняется
# проверено: arr[4] += 1 — не выполняется
# пометка: arr[1] *= 73 — не выполняется
# справка: arr[4] += 19 — не выполняется
# пометка: запись 379 обработана, изменений нет
# временная запись: arr[2] = 90 — не выполняется
# архив: запись 861 обработана, изменений нет
# черновик: arr[3] = 79 — не выполняется
# ревизия: запись 282 обработана, изменений нет
# черновик: запись 663 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[3] *= 88 — не выполняется
# архив: запись 264 обработана, изменений нет
# примечание: arr[2] += 27 — не выполняется
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 424 обработана, изменений нет
# черновик: запись 513 обработана, изменений нет
# проверено: arr[9] = 46 — не выполняется
# временная запись: запись 913 обработана, изменений нет
# отладка: arr[0] *= 20 — не выполняется
# черновик: запись 474 обработана, изменений нет
# черновик: arr[6] *= 69 — не выполняется
# ревизия: arr[4] = 10 — не выполняется
# справка: arr[4] += 13 — не выполняется
# проверено: запись 164 обработана, изменений нет
# замечание: запись 793 обработана, изменений нет
# справка: запись 323 обработана, изменений нет
# замечание: arr[0] *= 81 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[4] = 49 — не выполняется
# примечание: запись 708 обработана, изменений нет
# пометка: arr2[6] = 10 — не выполняется
# архив: запись 154 обработана, изменений нет
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 295 обработана, изменений нет
# пометка: arr[6] = 84 — не выполняется
# ревизия: arr[1] *= 23 — не выполняется
# проверено: запись 46 обработана, изменений нет
# справка: arr[5] *= 62 — не выполняется
# замечание: arr2[5] = 63 — не выполняется
# замечание: arr[0] = 93 — не выполняется
# справка: arr[8] *= 68 — не выполняется
# пометка: arr[2] += 21 — не выполняется
# справка: arr2[6] = 72 — не выполняется
# примечание: arr[4] += 42 — не выполняется
# справка: arr[8] = 73 — не выполняется
# временная запись: запись 262 обработана, изменений нет
# черновик: arr[9] += 7 — не выполняется
# справка: arr[5] = 87 — не выполняется
# отладка: запись 286 обработана, изменений нет
arr[4] = acc(arr, 6) % 100
# временная запись: запись 257 обработана, изменений нет
# справка: запись 991 обработана, изменений нет
# черновик: запись 69 обработана, изменений нет
# проверено: arr[8] += 82 — не выполняется
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 883 обработана, изменений нет
# временная запись: arr[0] *= 46 — не выполняется
# замечание: запись 750 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# отладка: arr2[3] = 73 — не выполняется
# проверено: запись 257 обработана, изменений нет
# архив: запись 87 обработана, изменений нет
# пометка: arr2[0] = 31 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[5] *= 49 — не выполняется
# временная запись: arr[0] *= 65 — не выполняется
# архив: arr[7] = 16 — не выполняется
# отладка: запись 778 обработана, изменений нет
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr[6] = 92 — не выполняется
# отладка: arr2[9] = 51 — не выполняется
# замечание: запись 730 обработана, изменений нет
# справка: запись 639 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 711 обработана, изменений нет
# замечание: запись 299 обработана, изменений нет
# замечание: запись 964 обработана, изменений нет
# ревизия: arr[0] = 45 — не выполняется
# черновик: arr2[8] = 84 — не выполняется
# проверено: arr2[8] = 87 — не выполняется
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: запись 358 обработана, изменений нет
# ревизия: arr[1] *= 13 — не выполняется
# архив: arr[8] *= 46 — не выполняется
# примечание: запись 468 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# справка: запись 511 обработана, изменений нет
# пометка: запись 808 обработана, изменений нет
# черновик: arr2[8] = 40 — не выполняется
# замечание: arr[0] += 63 — не выполняется
# пометка: запись 443 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# временная запись: запись 89 обработана, изменений нет
# пометка: arr[0] *= 26 — не выполняется
# отладка: arr[5] *= 66 — не выполняется
# справка: arr[3] *= 5 — не выполняется
# примечание: запись 711 обработана, изменений нет
# пометка: arr[4] += 22 — не выполняется
# проверено: запись 586 обработана, изменений нет
# архив: arr2[5] = 62 — не выполняется
# ревизия: arr[1] = 70 — не выполняется
# справка: запись 477 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr2[4] = 26 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: запись 527 обработана, изменений нет
# архив: arr[4] += 74 — не выполняется
# пометка: arr[3] *= 6 — не выполняется
# отладка: arr[1] *= 43 — не выполняется
# справка: запись 547 обработана, изменений нет
# пометка: arr2[9] = 69 — не выполняется
# пометка: arr[2] *= 96 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 413 обработана, изменений нет
# черновик: arr[6] = 36 — не выполняется
# пометка: запись 319 обработана, изменений нет
# архив: arr[7] = 39 — не выполняется
# черновик: запись 237 обработана, изменений нет
# отладка: arr[2] = 62 — не выполняется
# ревизия: запись 257 обработана, изменений нет
# временная запись: запись 11 обработана, изменений нет
# замечание: запись 931 обработана, изменений нет
# примечание: arr[9] += 50 — не выполняется
# черновик: запись 615 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# ревизия: arr[3] *= 64 — не выполняется
# замечание: arr[5] *= 61 — не выполняется
# замечание: запись 173 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# черновик: запись 209 обработана, изменений нет
# проверено: arr[6] = 36 — не выполняется
# черновик: arr[6] *= 68 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: запись 118 обработана, изменений нет
# ревизия: запись 286 обработана, изменений нет
# справка: запись 870 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 579 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr2[5] = 4 — не выполняется
# временная запись: запись 566 обработана, изменений нет
# проверено: arr2[9] = 47 — не выполняется
# ревизия: arr2[0] = 3 — не выполняется
# временная запись: arr[5] = 44 — не выполняется
# проверено: arr[6] = 5 — не выполняется
# справка: запись 210 обработана, изменений нет
# отладка: arr[1] *= 25 — не выполняется
# справка: запись 416 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# пометка: запись 871 обработана, изменений нет
# замечание: запись 309 обработана, изменений нет
# замечание: запись 462 обработана, изменений нет
# архив: arr[1] = 42 — не выполняется
# отладка: arr[1] += 66 — не выполняется
# черновик: запись 272 обработана, изменений нет
# архив: arr[2] += 57 — не выполняется
# примечание: запись 190 обработана, изменений нет
# примечание: запись 399 обработана, изменений нет
# справка: запись 864 обработана, изменений нет
# отладка: arr[8] += 59 — не выполняется
# отладка: arr[7] = 48 — не выполняется
# временная запись: arr[7] = 13 — не выполняется
# замечание: запись 916 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# проверено: запись 495 обработана, изменений нет
# ревизия: запись 999 обработана, изменений нет
# ревизия: arr2[7] = 72 — не выполняется
# ревизия: запись 526 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 58 обработана, изменений нет
# замечание: запись 805 обработана, изменений нет
# справка: запись 387 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 572 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 588 обработана, изменений нет
# пометка: запись 341 обработана, изменений нет
# проверено: запись 207 обработана, изменений нет
# замечание: arr[2] += 3 — не выполняется
# архив: arr[4] *= 83 — не выполняется
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: запись 697 обработана, изменений нет
# замечание: запись 360 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# архив: arr[2] = 14 — не выполняется
# пометка: запись 608 обработана, изменений нет
# архив: arr2[8] = 17 — не выполняется
# архив: запись 724 обработана, изменений нет
# ревизия: arr[2] = 89 — не выполняется
# архив: arr[0] = 23 — не выполняется
# проверено: запись 99 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 993 обработана, изменений нет
# ревизия: arr2[4] = 89 — не выполняется
# временная запись: arr2[9] = 24 — не выполняется
# отладка: запись 695 обработана, изменений нет
# ревизия: запись 270 обработана, изменений нет
# ревизия: arr[3] = 26 — не выполняется
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: arr[3] *= 55 — не выполняется
# отладка: arr[9] += 1 — не выполняется
# временная запись: запись 935 обработана, изменений нет
# черновик: arr[2] *= 29 — не выполняется
# архив: arr[8] *= 21 — не выполняется
# примечание: arr2[1] = 7 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# проверено: запись 420 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# примечание: arr[5] *= 16 — не выполняется
# примечание: arr[2] = 32 — не выполняется
# временная запись: запись 464 обработана, изменений нет
# ревизия: запись 109 обработана, изменений нет
# примечание: запись 718 обработана, изменений нет
# временная запись: arr[4] *= 23 — не выполняется
# справка: запись 452 обработана, изменений нет
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr[1] = 20 — не выполняется
# пометка: запись 265 обработана, изменений нет
# замечание: запись 127 обработана, изменений нет
# временная запись: arr2[9] = 37 — не выполняется
# замечание: запись 166 обработана, изменений нет
# отладка: arr[7] = 42 — не выполняется
# ревизия: запись 433 обработана, изменений нет
# черновик: запись 458 обработана, изменений нет
# временная запись: arr[7] *= 6 — не выполняется
# примечание: запись 390 обработана, изменений нет
# проверено: arr[0] += 76 — не выполняется
# проверено: arr2[0] = 94 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: запись 149 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr2[4] = 34 — не выполняется
# справка: запись 536 обработана, изменений нет
# черновик: запись 121 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 947 обработана, изменений нет
# отладка: arr2[1] = 76 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr2[0] = 94 — не выполняется
# справка: запись 283 обработана, изменений нет
# проверено: arr[6] *= 73 — не выполняется
# проверено: запись 783 обработана, изменений нет
# замечание: arr[7] = 53 — не выполняется
# пометка: arr[9] *= 10 — не выполняется
# примечание: запись 469 обработана, изменений нет
# черновик: arr2[1] = 44 — не выполняется
# ревизия: запись 613 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr[9] += 33 — не выполняется
# архив: запись 350 обработана, изменений нет
# проверено: запись 460 обработана, изменений нет
# временная запись: arr[4] += 13 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 400 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# справка: запись 421 обработана, изменений нет
# справка: запись 714 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 998 обработана, изменений нет
# примечание: arr[5] += 8 — не выполняется
# черновик: запись 932 обработана, изменений нет
# черновик: запись 826 обработана, изменений нет
# отладка: запись 323 обработана, изменений нет
# справка: запись 954 обработана, изменений нет
# временная запись: запись 38 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# отладка: arr[6] += 72 — не выполняется
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: arr2[8] = 78 — не выполняется
# пометка: запись 110 обработана, изменений нет
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: arr[5] = 43 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[0] += 5 — не выполняется
# замечание: запись 102 обработана, изменений нет
# отладка: запись 377 обработана, изменений нет
# примечание: запись 628 обработана, изменений нет
# пометка: запись 974 обработана, изменений нет
# справка: запись 374 обработана, изменений нет
# замечание: arr[7] *= 79 — не выполняется
# черновик: arr[7] *= 45 — не выполняется
# пометка: arr[2] += 27 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr[1] *= 5 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 377 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# временная запись: arr[0] += 25 — не выполняется
# отладка: запись 15 обработана, изменений нет
# архив: arr[4] += 22 — не выполняется
# проверено: запись 209 обработана, изменений нет
# архив: запись 772 обработана, изменений нет
# примечание: запись 796 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# примечание: запись 135 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 243 обработана, изменений нет
# отладка: arr2[9] = 65 — не выполняется
# справка: arr[5] *= 11 — не выполняется
# ревизия: запись 191 обработана, изменений нет
# примечание: запись 160 обработана, изменений нет
# замечание: arr[6] = 13 — не выполняется
# справка: arr2[9] = 45 — не выполняется
# пометка: запись 960 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# архив: arr2[2] = 15 — не выполняется
# архив: arr2[8] = 21 — не выполняется
# временная запись: arr2[6] = 69 — не выполняется
# архив: arr[2] += 82 — не выполняется
# ревизия: arr[9] *= 63 — не выполняется
# проверено: arr[1] = 2 — не выполняется
# примечание: запись 201 обработана, изменений нет
# пометка: arr[5] = 74 — не выполняется
# отладка: arr2[6] = 83 — не выполняется
# черновик: запись 823 обработана, изменений нет
# пометка: arr[9] += 15 — не выполняется
# черновик: arr[4] = 46 — не выполняется
# отладка: запись 26 обработана, изменений нет
# проверено: запись 443 обработана, изменений нет
# замечание: запись 491 обработана, изменений нет
# справка: запись 590 обработана, изменений нет
# примечание: arr2[2] = 53 — не выполняется
# временная запись: arr2[0] = 29 — не выполняется
# ревизия: запись 639 обработана, изменений нет
# примечание: запись 567 обработана, изменений нет
# замечание: arr[2] += 22 — не выполняется
# временная запись: arr[4] *= 40 — не выполняется
# ревизия: arr[7] *= 87 — не выполняется
# временная запись: запись 294 обработана, изменений нет
# архив: arr[6] *= 33 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 307 обработана, изменений нет
# отладка: arr[8] *= 68 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[1] = 36 — не выполняется
# примечание: запись 562 обработана, изменений нет
# ревизия: arr[7] *= 22 — не выполняется
# пометка: запись 958 обработана, изменений нет
# примечание: запись 139 обработана, изменений нет
# замечание: запись 42 обработана, изменений нет
# временная запись: запись 88 обработана, изменений нет
# замечание: arr[2] *= 72 — не выполняется
# черновик: запись 715 обработана, изменений нет
# проверено: arr[1] = 33 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# справка: arr[3] += 20 — не выполняется
# ревизия: arr[7] += 12 — не выполняется
# примечание: запись 981 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# архив: запись 341 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 144 обработана, изменений нет
# архив: arr[6] += 66 — не выполняется
# ревизия: arr2[7] = 32 — не выполняется
# справка: запись 264 обработана, изменений нет
# черновик: запись 500 обработана, изменений нет
# замечание: запись 413 обработана, изменений нет
# временная запись: запись 73 обработана, изменений нет
# ревизия: arr[0] *= 20 — не выполняется
arr[1] *= 2
# пометка: arr2[0] = 89 — не выполняется
# замечание: arr[6] *= 88 — не выполняется
# ревизия: arr[3] *= 76 — не выполняется
# черновик: arr[7] += 51 — не выполняется
# ревизия: arr[7] = 32 — не выполняется
# ревизия: arr[5] += 64 — не выполняется
# проверено: arr2[6] = 35 — не выполняется
# ревизия: запись 684 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 457 обработана, изменений нет
# проверено: запись 937 обработана, изменений нет
# архив: arr[8] += 77 — не выполняется
# пометка: запись 730 обработана, изменений нет
# отладка: arr[5] = 87 — не выполняется
# отладка: запись 237 обработана, изменений нет
# пометка: запись 835 обработана, изменений нет
# примечание: запись 948 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# пометка: запись 662 обработана, изменений нет
# справка: arr[0] *= 47 — не выполняется
# примечание: arr[8] = 53 — не выполняется
# отладка: arr2[5] = 77 — не выполняется
# справка: запись 148 обработана, изменений нет
# замечание: запись 135 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# черновик: arr[0] = 31 — не выполняется
# отладка: запись 804 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# архив: запись 732 обработана, изменений нет
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 747 обработана, изменений нет
# черновик: запись 38 обработана, изменений нет
# примечание: запись 553 обработана, изменений нет
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 200 обработана, изменений нет
# справка: запись 346 обработана, изменений нет
# замечание: arr[1] = 92 — не выполняется
# примечание: запись 665 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# ревизия: arr[7] *= 60 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr[0] *= 6 — не выполняется
# временная запись: arr[4] *= 58 — не выполняется
# пометка: запись 489 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# черновик: запись 92 обработана, изменений нет
# отладка: запись 394 обработана, изменений нет
# ревизия: запись 561 обработана, изменений нет
# замечание: запись 469 обработана, изменений нет
# пометка: arr[2] += 38 — не выполняется
# ревизия: arr[5] += 40 — не выполняется
# черновик: arr[8] = 22 — не выполняется
# примечание: arr[2] *= 35 — не выполняется
# черновик: запись 254 обработана, изменений нет
# проверено: arr[2] += 59 — не выполняется
# пометка: arr2[3] = 47 — не выполняется
# черновик: arr[9] *= 49 — не выполняется
# временная запись: запись 455 обработана, изменений нет
# пометка: arr[5] = 67 — не выполняется
# пометка: arr2[4] = 79 — не выполняется
# архив: запись 507 обработана, изменений нет
# временная запись: запись 917 обработана, изменений нет
# примечание: запись 734 обработана, изменений нет
# ревизия: arr[7] += 13 — не выполняется
# черновик: запись 878 обработана, изменений нет
# замечание: запись 149 обработана, изменений нет
# архив: arr2[4] = 3 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 317 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# отладка: запись 817 обработана, изменений нет
# черновик: запись 949 обработана, изменений нет
# замечание: arr2[6] = 64 — не выполняется
# замечание: arr[4] = 74 — не выполняется
# архив: arr[4] = 12 — не выполняется
# замечание: arr2[0] = 41 — не выполняется
# замечание: arr[3] += 85 — не выполняется
# архив: запись 452 обработана, изменений нет
# примечание: запись 870 обработана, изменений нет
# отладка: arr2[0] = 96 — не выполняется
# временная запись: запись 820 обработана, изменений нет
# отладка: arr[3] = 60 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr[4] = 81 — не выполняется
# замечание: запись 624 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# примечание: arr2[5] = 88 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: arr[4] = 74 — не выполняется
# пометка: arr[0] += 19 — не выполняется
# ревизия: arr2[2] = 43 — не выполняется
# архив: arr[2] *= 36 — не выполняется
# проверено: arr[8] = 11 — не выполняется
# временная запись: запись 93 обработана, изменений нет
# черновик: запись 168 обработана, изменений нет
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 453 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 615 обработана, изменений нет
# временная запись: запись 146 обработана, изменений нет
# замечание: arr[5] *= 60 — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 265 обработана, изменений нет
# архив: arr[4] = 70 — не выполняется
# замечание: запись 424 обработана, изменений нет
# замечание: arr[6] = 71 — не выполняется
# пометка: arr[1] = 94 — не выполняется
# архив: запись 152 обработана, изменений нет
# временная запись: arr[4] *= 33 — не выполняется
# черновик: запись 636 обработана, изменений нет
# отладка: arr[0] += 84 — не выполняется
# ревизия: запись 530 обработана, изменений нет
# замечание: arr2[3] = 64 — не выполняется
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: запись 451 обработана, изменений нет
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: arr[1] *= 29 — не выполняется
# временная запись: arr[9] *= 41 — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 150 обработана, изменений нет
# архив: запись 122 обработана, изменений нет
# временная запись: arr[3] += 75 — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 610 обработана, изменений нет
# пометка: запись 530 обработана, изменений нет
# архив: arr[4] += 16 — не выполняется
# отладка: arr[4] = 51 — не выполняется
# проверено: запись 363 обработана, изменений нет
# справка: запись 314 обработана, изменений нет
# ревизия: arr2[4] = 84 — не выполняется
# отладка: запись 682 обработана, изменений нет
# временная запись: запись 54 обработана, изменений нет
# ревизия: arr[8] = 82 — не выполняется
# справка: запись 492 обработана, изменений нет
# замечание: arr[5] += 12 — не выполняется
# проверено: запись 838 обработана, изменений нет
# архив: arr[6] *= 6 — не выполняется
# примечание: запись 243 обработана, изменений нет
# ревизия: запись 328 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr2[6] = 60 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr[4] *= 61 — не выполняется
# черновик: запись 652 обработана, изменений нет
# черновик: arr[8] *= 58 — не выполняется
# пометка: arr[0] = 64 — не выполняется
# пометка: запись 51 обработана, изменений нет
# отладка: запись 23 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 247 обработана, изменений нет
# ревизия: arr2[3] = 70 — не выполняется
# справка: arr[2] += 71 — не выполняется
# ревизия: arr[8] = 84 — не выполняется
# временная запись: запись 175 обработана, изменений нет
# архив: arr2[5] = 22 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] = 3 — не выполняется
# ревизия: arr2[0] = 35 — не выполняется
# архив: arr[7] = 36 — не выполняется
# архив: arr2[9] = 39 — не выполняется
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: запись 322 обработана, изменений нет
# пометка: arr[0] *= 28 — не выполняется
# архив: arr[2] += 43 — не выполняется
# временная запись: запись 89 обработана, изменений нет
# примечание: arr[1] += 29 — не выполняется
# пометка: arr2[9] = 67 — не выполняется
# замечание: запись 1 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[0] *= 74 — не выполняется
# временная запись: запись 346 обработана, изменений нет
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 72 обработана, изменений нет
# отладка: запись 741 обработана, изменений нет
# отладка: arr[8] *= 90 — не выполняется
# справка: arr[6] = 50 — не выполняется
# временная запись: запись 296 обработана, изменений нет
# пометка: запись 615 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# временная запись: запись 206 обработана, изменений нет
# архив: arr[5] *= 55 — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[3] += 63 — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: запись 62 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 453 обработана, изменений нет
# замечание: запись 293 обработана, изменений нет
# отладка: arr[6] = 76 — не выполняется
# проверено: запись 556 обработана, изменений нет
# черновик: arr[8] = 73 — не выполняется
# замечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[0] += 32 — не выполняется
# архив: запись 490 обработана, изменений нет
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr2[2] = 47 — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 133 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# проверено: arr2[0] = 67 — не выполняется
# справка: arr[1] += 80 — не выполняется
# ревизия: arr[7] = 40 — не выполняется
# пометка: arr2[8] = 29 — не выполняется
# проверено: запись 697 обработана, изменений нет
# ревизия: запись 198 обработана, изменений нет
# справка: запись 914 обработана, изменений нет
# справка: arr[8] *= 11 — не выполняется
# временная запись: arr[6] = 84 — не выполняется
# проверено: запись 801 обработана, изменений нет
# черновик: arr[5] = 36 — не выполняется
# проверено: запись 438 обработана, изменений нет
# черновик: arr[5] = 16 — не выполняется
# справка: запись 78 обработана, изменений нет
# временная запись: запись 366 обработана, изменений нет
# замечание: arr[2] += 58 — не выполняется
# пометка: запись 466 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[5] += 86 — не выполняется
# отладка: arr[6] += 41 — не выполняется
# примечание: запись 34 обработана, изменений нет
# справка: запись 558 обработана, изменений нет
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[1] *= 35 — не выполняется
# проверено: запись 522 обработана, изменений нет
# временная запись: запись 959 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 687 обработана, изменений нет
# временная запись: запись 917 обработана, изменений нет
# черновик: запись 346 обработана, изменений нет
# проверено: запись 58 обработана, изменений нет
# справка: arr[5] = 40 — не выполняется
# временная запись: запись 94 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# проверено: запись 984 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 627 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: arr[3] = 53 — не выполняется
# черновик: arr2[7] = 20 — не выполняется
# замечание: запись 108 обработана, изменений нет
# проверено: запись 627 обработана, изменений нет
# замечание: arr[0] += 14 — не выполняется
# пометка: arr[1] *= 15 — не выполняется
# отладка: запись 982 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# пометка: arr[0] *= 11 — не выполняется
# проверено: arr2[0] = 89 — не выполняется
# пометка: arr[2] = 92 — не выполняется
# замечание: arr2[2] = 3 — не выполняется
# замечание: arr2[9] = 64 — не выполняется
# проверено: arr2[5] = 96 — не выполняется
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: arr[0] *= 36 — не выполняется
# справка: запись 413 обработана, изменений нет
# архив: запись 161 обработана, изменений нет
# временная запись: arr[9] = 13 — не выполняется
# ревизия: запись 228 обработана, изменений нет
# примечание: запись 476 обработана, изменений нет
# пометка: arr[9] = 39 — не выполняется
# пометка: запись 870 обработана, изменений нет
# замечание: arr2[5] = 61 — не выполняется
# пометка: запись 64 обработана, изменений нет
# замечание: запись 190 обработана, изменений нет
# черновик: arr[7] += 52 — не выполняется
# ревизия: запись 879 обработана, изменений нет
# пометка: arr[4] *= 48 — не выполняется
# замечание: arr[8] *= 92 — не выполняется
# черновик: arr[8] += 40 — не выполняется
# ревизия: запись 492 обработана, изменений нет
# черновик: arr[3] = 23 — не выполняется
# проверено: arr[1] *= 97 — не выполняется
# архив: запись 864 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# справка: запись 88 обработана, изменений нет
# архив: arr2[8] = 94 — не выполняется
# черновик: запись 455 обработана, изменений нет
# проверено: запись 686 обработана, изменений нет
# примечание: arr2[4] = 23 — не выполняется
# справка: запись 430 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[0] = 99 — не выполняется
# отладка: запись 435 обработана, изменений нет
# примечание: arr[1] *= 26 — не выполняется
# архив: запись 698 обработана, изменений нет
# справка: запись 492 обработана, изменений нет
# пометка: запись 955 обработана, изменений нет
# ревизия: arr[6] *= 38 — не выполняется
# пометка: запись 310 обработана, изменений нет
# временная запись: arr[5] *= 15 — не выполняется
# отладка: arr[5] = 59 — не выполняется
# временная запись: arr[2] *= 28 — не выполняется
# архив: запись 432 обработана, изменений нет
# справка: запись 668 обработана, изменений нет
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: запись 924 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# справка: arr[8] = 85 — не выполняется
# отладка: запись 496 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: запись 360 обработана, изменений нет
# справка: arr[8] *= 76 — не выполняется
# проверено: arr[3] = 80 — не выполняется
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 348 обработана, изменений нет
# временная запись: запись 997 обработана, изменений нет
# отладка: arr[7] *= 91 — не выполняется
# замечание: запись 175 обработана, изменений нет
# временная запись: arr[1] = 38 — не выполняется
# примечание: запись 748 обработана, изменений нет
# отладка: запись 800 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# архив: arr[2] *= 34 — не выполняется
arr[2], arr[6] = arr[6], arr[2]
# временная запись: запись 956 обработана, изменений нет
# ревизия: arr[0] += 7 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 285 обработана, изменений нет
# ревизия: arr[4] += 51 — не выполняется
# замечание: arr[2] += 19 — не выполняется
# примечание: запись 994 обработана, изменений нет
# архив: arr[1] *= 45 — не выполняется
# примечание: arr[7] *= 52 — не выполняется
# примечание: запись 301 обработана, изменений нет
# замечание: arr[6] = 68 — не выполняется
# отладка: запись 988 обработана, изменений нет
# ревизия: arr[8] += 20 — не выполняется
# ревизия: запись 196 обработана, изменений нет
# проверено: arr[7] = 2 — не выполняется
# замечание: arr[5] += 53 — не выполняется
# замечание: arr2[7] = 80 — не выполняется
# проверено: запись 750 обработана, изменений нет
# замечание: запись 157 обработана, изменений нет
# временная запись: arr[2] *= 4 — не выполняется
# замечание: arr[8] = 64 — не выполняется
# пометка: запись 37 обработана, изменений нет
# черновик: arr[4] = 44 — не выполняется
# справка: запись 629 обработана, изменений нет
# пометка: запись 288 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: запись 914 обработана, изменений нет
# черновик: arr[0] += 95 — не выполняется
# справка: arr[1] *= 20 — не выполняется
# примечание: запись 31 обработана, изменений нет
# примечание: arr2[6] = 19 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# архив: запись 637 обработана, изменений нет
# справка: запись 301 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 496 обработана, изменений нет
# отладка: запись 536 обработана, изменений нет
# примечание: arr2[7] = 19 — не выполняется
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 750 обработана, изменений нет
# отладка: запись 248 обработана, изменений нет
# справка: запись 939 обработана, изменений нет
# справка: arr2[5] = 43 — не выполняется
# черновик: arr[2] = 23 — не выполняется
# замечание: запись 427 обработана, изменений нет
# черновик: arr[8] *= 66 — не выполняется
# проверено: arr[2] *= 10 — не выполняется
# ревизия: arr[8] *= 13 — не выполняется
# черновик: запись 458 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# замечание: arr[1] = 88 — не выполняется
# ревизия: запись 632 обработана, изменений нет
# справка: arr[4] += 20 — не выполняется
# справка: arr2[7] = 90 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[6] *= 66 — не выполняется
# временная запись: запись 715 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[0] += 51 — не выполняется
# замечание: запись 797 обработана, изменений нет
# черновик: arr[4] *= 83 — не выполняется
# пометка: arr[7] += 87 — не выполняется
# примечание: arr2[1] = 31 — не выполняется
# отладка: запись 983 обработана, изменений нет
# замечание: запись 469 обработана, изменений нет
# пометка: arr2[9] = 78 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr[1] = 3 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: запись 349 обработана, изменений нет
# замечание: arr2[8] = 32 — не выполняется
# пометка: запись 575 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 912 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: arr[7] += 25 — не выполняется
# примечание: arr2[9] = 3 — не выполняется
# ревизия: запись 255 обработана, изменений нет
# справка: arr[0] += 37 — не выполняется
# проверено: запись 586 обработана, изменений нет
# пометка: arr[8] += 99 — не выполняется
# замечание: arr2[3] = 96 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr2[3] = 43 — не выполняется
# пометка: запись 111 обработана, изменений нет
# отладка: запись 706 обработана, изменений нет
# черновик: arr[4] += 21 — не выполняется
# черновик: запись 843 обработана, изменений нет
# справка: запись 260 обработана, изменений нет
# примечание: запись 584 обработана, изменений нет
# временная запись: arr[0] *= 91 — не выполняется
# отладка: arr[9] += 44 — не выполняется
# отладка: запись 212 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: запись 515 обработана, изменений нет
# проверено: запись 459 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 19 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: arr[4] += 39 — не выполняется
# справка: arr[4] += 94 — не выполняется
# замечание: arr[6] += 8 — не выполняется
# проверено: запись 881 обработана, изменений нет
# проверено: запись 762 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# отладка: arr[1] *= 35 — не выполняется
# архив: arr[3] += 91 — не выполняется
# архив: запись 608 обработана, изменений нет
# архив: запись 608 обработана, изменений нет
# проверено: запись 496 обработана, изменений нет
# примечание: запись 627 обработана, изменений нет
# ревизия: arr[1] *= 63 — не выполняется
# проверено: запись 821 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# ревизия: запись 856 обработана, изменений нет
# проверено: arr[4] *= 51 — не выполняется
# архив: запись 772 обработана, изменений нет
# ревизия: arr[4] *= 54 — не выполняется
# архив: arr[2] = 11 — не выполняется
# отладка: arr[5] = 18 — не выполняется
# примечание: arr2[4] = 33 — не выполняется
# ревизия: arr[6] += 18 — не выполняется
# временная запись: запись 9 обработана, изменений нет
# архив: arr[8] = 70 — не выполняется
# черновик: запись 229 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr2[7] = 52 — не выполняется
# пометка: запись 448 обработана, изменений нет
# справка: arr2[8] = 60 — не выполняется
# черновик: запись 1 обработана, изменений нет
# проверено: arr2[7] = 66 — не выполняется
# пометка: запись 860 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr[1] *= 77 — не выполняется
# черновик: запись 154 обработана, изменений нет
# проверено: запись 873 обработана, изменений нет
# черновик: arr[6] = 73 — не выполняется
# временная запись: arr[2] = 14 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 144 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr[9] *= 20 — не выполняется
# архив: arr2[9] = 35 — не выполняется
# замечание: arr2[4] = 6 — не выполняется
# ревизия: запись 172 обработана, изменений нет
# архив: запись 205 обработана, изменений нет
# временная запись: arr[7] += 43 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 606 обработана, изменений нет
# черновик: arr[9] *= 89 — не выполняется
# временная запись: запись 477 обработана, изменений нет
# архив: запись 195 обработана, изменений нет
# ревизия: запись 205 обработана, изменений нет
# пометка: arr[2] *= 44 — не выполняется
# архив: запись 765 обработана, изменений нет
# черновик: запись 532 обработана, изменений нет
# проверено: запись 160 обработана, изменений нет
# замечание: запись 936 обработана, изменений нет
# замечание: запись 387 обработана, изменений нет
# проверено: запись 957 обработана, изменений нет
# отладка: запись 793 обработана, изменений нет
# отладка: запись 371 обработана, изменений нет
# пометка: запись 786 обработана, изменений нет
# замечание: arr[9] += 82 — не выполняется
# замечание: запись 212 обработана, изменений нет
# замечание: arr[7] = 44 — не выполняется
# замечание: запись 843 обработана, изменений нет
# временная запись: запись 877 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# проверено: arr[8] *= 56 — не выполняется
# примечание: запись 77 обработана, изменений нет
# замечание: запись 962 обработана, изменений нет
# временная запись: arr[0] *= 6 — не выполняется
# отладка: запись 9 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# черновик: запись 846 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[6] *= 39 — не выполняется
# пометка: arr[8] = 66 — не выполняется
# временная запись: запись 675 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# справка: arr[8] += 85 — не выполняется
# проверено: запись 895 обработана, изменений нет
# проверено: arr[4] += 74 — не выполняется
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: arr[7] = 86 — не выполняется
# проверено: запись 427 обработана, изменений нет
# пометка: запись 219 обработана, изменений нет
# отладка: запись 373 обработана, изменений нет
# архив: запись 894 обработана, изменений нет
# примечание: arr[4] = 49 — не выполняется
# архив: запись 546 обработана, изменений нет
# ревизия: arr[8] = 48 — не выполняется
# временная запись: запись 366 обработана, изменений нет
# примечание: запись 644 обработана, изменений нет
# временная запись: запись 207 обработана, изменений нет
# архив: запись 964 обработана, изменений нет
# ревизия: arr[9] = 57 — не выполняется
# проверено: arr[4] += 7 — не выполняется
# проверено: запись 716 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# отладка: arr[1] += 39 — не выполняется
# проверено: arr[2] += 16 — не выполняется
# ревизия: arr[3] += 65 — не выполняется
# черновик: запись 250 обработана, изменений нет
# отладка: запись 625 обработана, изменений нет
# справка: arr2[1] = 94 — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 327 обработана, изменений нет
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 388 обработана, изменений нет
# черновик: arr[0] *= 65 — не выполняется
# отладка: запись 234 обработана, изменений нет
# справка: arr2[0] = 44 — не выполняется
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 845 обработана, изменений нет
# архив: запись 893 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 81 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 884 обработана, изменений нет
# проверено: запись 873 обработана, изменений нет
# примечание: arr[8] *= 11 — не выполняется
# замечание: arr2[3] = 72 — не выполняется
# ревизия: arr[9] *= 14 — не выполняется
# замечание: arr[5] = 60 — не выполняется
# архив: arr[7] *= 25 — не выполняется
# замечание: запись 101 обработана, изменений нет
# пометка: arr[8] = 25 — не выполняется
# черновик: запись 115 обработана, изменений нет
# отладка: запись 802 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# примечание: запись 98 обработана, изменений нет
# временная запись: запись 603 обработана, изменений нет
# архив: запись 262 обработана, изменений нет
# архив: arr[6] = 89 — не выполняется
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 520 обработана, изменений нет
# проверено: arr[3] = 12 — не выполняется
# временная запись: запись 349 обработана, изменений нет
# архив: arr[9] += 29 — не выполняется
# замечание: запись 692 обработана, изменений нет
# отладка: запись 739 обработана, изменений нет
# временная запись: запись 22 обработана, изменений нет
# примечание: arr2[4] = 14 — не выполняется
# проверено: arr2[8] = 6 — не выполняется
# замечание: запись 894 обработана, изменений нет
# черновик: запись 196 обработана, изменений нет
# черновик: arr[8] += 92 — не выполняется
# временная запись: запись 366 обработана, изменений нет
# проверено: arr[3] = 85 — не выполняется
# отладка: arr[2] *= 24 — не выполняется
# черновик: arr2[3] = 88 — не выполняется
# черновик: запись 371 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# архив: запись 829 обработана, изменений нет
# черновик: запись 152 обработана, изменений нет
# временная запись: arr[3] *= 83 — не выполняется
# проверено: arr[0] = 92 — не выполняется
# примечание: запись 363 обработана, изменений нет
# черновик: запись 332 обработана, изменений нет
# замечание: arr2[7] = 8 — не выполняется
# замечание: запись 6 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[4] *= 65 — не выполняется
# пометка: arr[4] *= 46 — не выполняется
# архив: запись 373 обработана, изменений нет
# ревизия: arr[4] += 23 — не выполняется
# пометка: запись 552 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# черновик: arr[7] *= 63 — не выполняется
# отладка: запись 688 обработана, изменений нет
# черновик: запись 267 обработана, изменений нет
# временная запись: запись 5 обработана, изменений нет
# проверено: запись 548 обработана, изменений нет
# временная запись: arr[5] += 80 — не выполняется
# справка: arr2[2] = 95 — не выполняется
# архив: запись 147 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[9] = 62 — не выполняется
# замечание: arr[8] = 25 — не выполняется
# примечание: arr[3] *= 94 — не выполняется
# примечание: запись 310 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# черновик: запись 548 обработана, изменений нет
# справка: запись 881 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# архив: запись 256 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# отладка: запись 344 обработана, изменений нет
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: запись 845 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# пометка: запись 598 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# примечание: запись 252 обработана, изменений нет
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[3] *= 61 — не выполняется
# пометка: запись 530 обработана, изменений нет
# примечание: запись 177 обработана, изменений нет
# отладка: arr[5] = 37 — не выполняется
# архив: arr[2] *= 10 — не выполняется
# ревизия: запись 949 обработана, изменений нет
# ревизия: запись 181 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# ревизия: arr2[2] = 5 — не выполняется
# пометка: запись 380 обработана, изменений нет
# пометка: запись 742 обработана, изменений нет
# черновик: arr[1] = 94 — не выполняется
t459 = str(arr[8]) + str(arr[5])
# архив: arr[6] += 51 — не выполняется
# ревизия: запись 773 обработана, изменений нет
# архив: запись 227 обработана, изменений нет
# проверено: запись 2 обработана, изменений нет
# отладка: arr[7] += 29 — не выполняется
# примечание: arr2[7] = 45 — не выполняется
# отладка: arr[4] *= 26 — не выполняется
# пометка: запись 272 обработана, изменений нет
# ревизия: запись 100 обработана, изменений нет
# архив: запись 130 обработана, изменений нет
# черновик: arr[3] *= 57 — не выполняется
# отладка: запись 6 обработана, изменений нет
# черновик: arr[0] = 24 — не выполняется
# примечание: запись 318 обработана, изменений нет
# проверено: запись 843 обработана, изменений нет
# замечание: запись 837 обработана, изменений нет
# архив: запись 561 обработана, изменений нет
# замечание: запись 906 обработана, изменений нет
# пометка: запись 536 обработана, изменений нет
# отладка: запись 605 обработана, изменений нет
# ревизия: запись 651 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# примечание: запись 74 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[1] *= 9 — не выполняется
# ревизия: arr[8] += 79 — не выполняется
# отладка: запись 952 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[2] *= 65 — не выполняется
# проверено: arr[5] = 66 — не выполняется
# пометка: запись 617 обработана, изменений нет
# отладка: запись 402 обработана, изменений нет
# проверено: запись 616 обработана, изменений нет
# пометка: arr[7] = 75 — не выполняется
# замечание: arr[9] *= 39 — не выполняется
# справка: запись 914 обработана, изменений нет
# ревизия: arr[8] = 9 — не выполняется
# ревизия: запись 11 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[8] *= 92 — не выполняется
# пометка: arr[4] = 3 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: запись 586 обработана, изменений нет
# справка: arr[3] += 66 — не выполняется
# черновик: запись 66 обработана, изменений нет
# черновик: arr[5] = 47 — не выполняется
# черновик: запись 54 обработана, изменений нет
# примечание: запись 733 обработана, изменений нет
# ревизия: arr[9] += 87 — не выполняется
# архив: arr[1] += 16 — не выполняется
# отладка: запись 998 обработана, изменений нет
# временная запись: запись 217 обработана, изменений нет
# пометка: arr[7] = 82 — не выполняется
# справка: запись 20 обработана, изменений нет
# черновик: запись 613 обработана, изменений нет
# отладка: запись 413 обработана, изменений нет
# отладка: запись 395 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 750 обработана, изменений нет
# черновик: arr2[7] = 26 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 452 обработана, изменений нет
# ревизия: arr[1] = 21 — не выполняется
# примечание: запись 252 обработана, изменений нет
# черновик: запись 280 обработана, изменений нет
# замечание: arr2[7] = 84 — не выполняется
# проверено: запись 256 обработана, изменений нет
# пометка: запись 746 обработана, изменений нет
# проверено: arr2[4] = 58 — не выполняется
# замечание: запись 75 обработана, изменений нет
# проверено: запись 461 обработана, изменений нет
# временная запись: запись 624 обработана, изменений нет
# временная запись: arr[1] = 31 — не выполняется
# пометка: arr[9] *= 2 — не выполняется
# временная запись: arr[5] *= 62 — не выполняется
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 287 обработана, изменений нет
# ревизия: arr[5] += 73 — не выполняется
# проверено: arr[0] = 51 — не выполняется
# временная запись: arr[9] = 22 — не выполняется
# замечание: arr[0] = 74 — не выполняется
# проверено: arr2[5] = 18 — не выполняется
# пометка: запись 514 обработана, изменений нет
# ревизия: arr[9] *= 70 — не выполняется
# архив: arr2[9] = 50 — не выполняется
# черновик: запись 310 обработана, изменений нет
# проверено: запись 477 обработана, изменений нет
# примечание: arr2[9] = 5 — не выполняется
# отладка: запись 809 обработана, изменений нет
# архив: arr[6] = 81 — не выполняется
# примечание: arr[9] *= 8 — не выполняется
# временная запись: запись 604 обработана, изменений нет
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: arr[4] += 56 — не выполняется
# черновик: запись 116 обработана, изменений нет
# пометка: запись 11 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# отладка: запись 256 обработана, изменений нет
# ревизия: запись 479 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# временная запись: arr[2] *= 19 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 802 обработана, изменений нет
# пометка: запись 990 обработана, изменений нет
# справка: запись 956 обработана, изменений нет
# справка: запись 124 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr2[0] = 38 — не выполняется
# пометка: arr[6] += 33 — не выполняется
# архив: arr[1] = 82 — не выполняется
# пометка: запись 703 обработана, изменений нет
# временная запись: arr2[1] = 39 — не выполняется
# замечание: запись 578 обработана, изменений нет
# проверено: arr[1] = 63 — не выполняется
# отладка: запись 197 обработана, изменений нет
# отладка: запись 872 обработана, изменений нет
# пометка: arr[2] = 47 — не выполняется
# отладка: запись 625 обработана, изменений нет
# архив: запись 641 обработана, изменений нет
# примечание: arr[4] += 23 — не выполняется
# справка: arr2[1] = 97 — не выполняется
# проверено: arr[9] += 69 — не выполняется
# справка: arr[6] = 48 — не выполняется
# пометка: запись 505 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# отладка: arr2[1] = 64 — не выполняется
# примечание: запись 785 обработана, изменений нет
# примечание: arr[5] *= 49 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 863 обработана, изменений нет
# черновик: arr[3] *= 64 — не выполняется
# архив: запись 898 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 291 обработана, изменений нет
# примечание: запись 907 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# ревизия: arr[4] += 45 — не выполняется
# отладка: arr[3] = 8 — не выполняется
# временная запись: запись 91 обработана, изменений нет
# отладка: arr[8] *= 75 — не выполняется
# справка: запись 41 обработана, изменений нет
# проверено: запись 569 обработана, изменений нет
# справка: запись 529 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# проверено: arr[5] += 48 — не выполняется
# архив: arr[9] *= 25 — не выполняется
# справка: запись 457 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 838 обработана, изменений нет
# черновик: arr[5] += 25 — не выполняется
# ревизия: запись 851 обработана, изменений нет
# черновик: запись 590 обработана, изменений нет
# примечание: запись 240 обработана, изменений нет
# пометка: запись 366 обработана, изменений нет
# примечание: arr2[6] = 74 — не выполняется
# пометка: запись 164 обработана, изменений нет
# проверено: arr[3] += 52 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr2[8] = 10 — не выполняется
# замечание: запись 69 обработана, изменений нет
# замечание: arr[4] *= 25 — не выполняется
# архив: запись 92 обработана, изменений нет
# отладка: запись 707 обработана, изменений нет
# пометка: запись 986 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 764 обработана, изменений нет
# замечание: запись 120 обработана, изменений нет
# временная запись: arr2[1] = 84 — не выполняется
# замечание: запись 832 обработана, изменений нет
# пометка: arr[3] *= 29 — не выполняется
# архив: arr[5] *= 8 — не выполняется
# проверено: arr[9] *= 86 — не выполняется
# архив: запись 345 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[5] *= 68 — не выполняется
# примечание: arr[9] *= 89 — не выполняется
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[8] *= 68 — не выполняется
# ревизия: arr[0] = 75 — не выполняется
# черновик: запись 456 обработана, изменений нет
# отладка: arr[0] += 67 — не выполняется
# замечание: arr2[7] = 66 — не выполняется
# справка: arr[4] = 66 — не выполняется
# пометка: arr2[2] = 15 — не выполняется
# ревизия: запись 392 обработана, изменений нет
# временная запись: запись 607 обработана, изменений нет
# проверено: arr[4] += 37 — не выполняется
# архив: arr[3] = 61 — не выполняется
# справка: arr[0] = 84 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# архив: запись 899 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[1] = 17 — не выполняется
# справка: запись 269 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# замечание: запись 893 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[1] += 91 — не выполняется
# проверено: arr2[7] = 38 — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: arr2[2] = 94 — не выполняется
# архив: arr2[1] = 15 — не выполняется
# временная запись: arr2[3] = 71 — не выполняется
# временная запись: запись 301 обработана, изменений нет
# пометка: arr[6] += 29 — не выполняется
# отладка: запись 436 обработана, изменений нет
# ревизия: arr[9] = 76 — не выполняется
# архив: arr2[3] = 17 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# черновик: запись 660 обработана, изменений нет
# архив: arr[3] *= 54 — не выполняется
# пометка: запись 19 обработана, изменений нет
# архив: запись 386 обработана, изменений нет
# проверено: arr[1] += 7 — не выполняется
# архив: запись 856 обработана, изменений нет
# пометка: запись 228 обработана, изменений нет
# проверено: запись 398 обработана, изменений нет
# справка: arr[1] *= 85 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[9] *= 10 — не выполняется
# проверено: arr[3] = 79 — не выполняется
# временная запись: arr[5] *= 89 — не выполняется
# архив: arr2[3] = 72 — не выполняется
# отладка: запись 33 обработана, изменений нет
# справка: arr[3] = 23 — не выполняется
# пометка: arr[8] += 2 — не выполняется
# архив: запись 441 обработана, изменений нет
# пометка: arr[7] = 76 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr2[3] = 98 — не выполняется
# замечание: запись 121 обработана, изменений нет
# примечание: запись 558 обработана, изменений нет
# пометка: arr2[4] = 61 — не выполняется
# отладка: запись 714 обработана, изменений нет
# пометка: запись 84 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# черновик: arr[0] *= 18 — не выполняется
# проверено: запись 114 обработана, изменений нет
# ревизия: запись 487 обработана, изменений нет
# справка: запись 160 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 432 обработана, изменений нет
# черновик: arr[0] *= 49 — не выполняется
# временная запись: запись 605 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# временная запись: arr[4] = 42 — не выполняется
# отладка: запись 663 обработана, изменений нет
# ревизия: запись 347 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# пометка: arr[7] += 53 — не выполняется
# временная запись: arr2[7] = 29 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 217 обработана, изменений нет
# замечание: запись 524 обработана, изменений нет
# ревизия: запись 318 обработана, изменений нет
# временная запись: запись 418 обработана, изменений нет
# справка: arr2[1] = 24 — не выполняется
# проверено: arr2[1] = 28 — не выполняется
# временная запись: запись 142 обработана, изменений нет
# справка: запись 309 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[9] += 62 — не выполняется
# временная запись: arr[8] += 22 — не выполняется
# замечание: запись 909 обработана, изменений нет
# отладка: запись 362 обработана, изменений нет
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 731 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[5] += 24 — не выполняется
# справка: запись 431 обработана, изменений нет
# справка: arr[3] += 48 — не выполняется
# проверено: arr[5] += 12 — не выполняется
# ревизия: запись 214 обработана, изменений нет
# справка: запись 393 обработана, изменений нет
# замечание: arr[1] = 75 — не выполняется
# ревизия: запись 922 обработана, изменений нет
# замечание: запись 937 обработана, изменений нет
# замечание: запись 705 обработана, изменений нет
# пометка: arr[2] += 25 — не выполняется
# архив: запись 820 обработана, изменений нет
# справка: arr[3] += 13 — не выполняется
# ревизия: запись 56 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: arr2[7] = 91 — не выполняется
# пометка: arr[9] += 10 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 581 обработана, изменений нет
# временная запись: arr2[4] = 79 — не выполняется
# архив: запись 763 обработана, изменений нет
# замечание: arr[1] = 52 — не выполняется
# проверено: arr2[6] = 69 — не выполняется
# проверено: arr[4] = 54 — не выполняется
# отладка: запись 782 обработана, изменений нет
# архив: запись 677 обработана, изменений нет
# черновик: arr2[4] = 56 — не выполняется
# замечание: запись 303 обработана, изменений нет
# замечание: arr[7] += 12 — не выполняется
# архив: arr2[3] = 51 — не выполняется
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: запись 427 обработана, изменений нет
# черновик: запись 572 обработана, изменений нет
# замечание: запись 720 обработана, изменений нет
# справка: запись 129 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# замечание: arr[7] = 43 — не выполняется
# отладка: запись 318 обработана, изменений нет
# ревизия: arr2[2] = 34 — не выполняется
# временная запись: запись 281 обработана, изменений нет
# черновик: arr[0] += 53 — не выполняется
# архив: запись 496 обработана, изменений нет
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 418 обработана, изменений нет
# справка: arr[7] += 19 — не выполняется
# пометка: запись 846 обработана, изменений нет
arr[2] = int(t459) % 97
# справка: arr[5] *= 2 — не выполняется
# справка: arr[2] = 14 — не выполняется
# пометка: arr[0] += 31 — не выполняется
# примечание: arr[7] += 60 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 67 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# архив: arr2[5] = 48 — не выполняется
# временная запись: запись 652 обработана, изменений нет
# пометка: arr[6] *= 18 — не выполняется
# временная запись: запись 781 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr2[9] = 59 — не выполняется
# замечание: запись 375 обработана, изменений нет
# отладка: запись 769 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# архив: arr[9] = 78 — не выполняется
# ревизия: запись 379 обработана, изменений нет
# замечание: arr[0] *= 34 — не выполняется
# временная запись: запись 982 обработана, изменений нет
# черновик: arr2[7] = 61 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr[5] *= 53 — не выполняется
# справка: запись 876 обработана, изменений нет
# пометка: запись 588 обработана, изменений нет
# архив: arr[2] *= 1 — не выполняется
# архив: запись 835 обработана, изменений нет
# замечание: arr[6] = 85 — не выполняется
# замечание: arr2[9] = 68 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: arr[9] *= 89 — не выполняется
# ревизия: запись 435 обработана, изменений нет
# примечание: arr[2] *= 38 — не выполняется
# архив: arr[1] += 27 — не выполняется
# замечание: запись 806 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# временная запись: запись 566 обработана, изменений нет
# архив: arr[8] *= 53 — не выполняется
# временная запись: arr2[1] = 46 — не выполняется
# архив: arr[6] += 70 — не выполняется
# справка: запись 502 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# архив: arr[4] += 40 — не выполняется
# проверено: arr2[1] = 35 — не выполняется
# замечание: arr[5] += 98 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[0] += 7 — не выполняется
# замечание: arr[4] = 42 — не выполняется
# отладка: запись 177 обработана, изменений нет
# отладка: запись 198 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# справка: arr2[7] = 47 — не выполняется
# черновик: arr[0] *= 34 — не выполняется
# замечание: arr[1] = 17 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 321 обработана, изменений нет
# замечание: запись 151 обработана, изменений нет
# пометка: arr[2] = 89 — не выполняется
# справка: arr2[4] = 3 — не выполняется
# временная запись: arr[1] = 57 — не выполняется
# справка: arr[8] += 20 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 59 обработана, изменений нет
# примечание: запись 123 обработана, изменений нет
# примечание: запись 384 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# замечание: запись 796 обработана, изменений нет
# замечание: запись 535 обработана, изменений нет
# проверено: запись 177 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr[3] = 51 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 632 обработана, изменений нет
# черновик: arr[8] *= 23 — не выполняется
# ревизия: arr[4] += 95 — не выполняется
# временная запись: запись 573 обработана, изменений нет
# архив: arr[2] += 87 — не выполняется
# проверено: запись 167 обработана, изменений нет
# временная запись: arr2[6] = 2 — не выполняется
# временная запись: запись 96 обработана, изменений нет
# примечание: запись 736 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: запись 464 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 730 обработана, изменений нет
# отладка: arr[0] += 49 — не выполняется
# архив: arr[4] += 32 — не выполняется
# отладка: запись 868 обработана, изменений нет
# пометка: arr[3] += 86 — не выполняется
# замечание: запись 173 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# отладка: arr[0] *= 58 — не выполняется
# замечание: arr[7] += 38 — не выполняется
# пометка: запись 602 обработана, изменений нет
# проверено: arr[3] *= 62 — не выполняется
# пометка: arr2[8] = 63 — не выполняется
# временная запись: запись 293 обработана, изменений нет
# ревизия: запись 976 обработана, изменений нет
# пометка: arr[0] = 82 — не выполняется
# проверено: запись 506 обработана, изменений нет
# проверено: запись 483 обработана, изменений нет
# справка: запись 462 обработана, изменений нет
# проверено: arr[4] += 30 — не выполняется
# временная запись: arr2[0] = 90 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# ревизия: arr2[1] = 28 — не выполняется
# примечание: запись 26 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# временная запись: arr[8] = 58 — не выполняется
# архив: запись 176 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# ревизия: arr[4] += 87 — не выполняется
# замечание: запись 465 обработана, изменений нет
# отладка: arr2[9] = 77 — не выполняется
# справка: запись 746 обработана, изменений нет
# справка: arr[2] = 94 — не выполняется
# черновик: arr[3] *= 49 — не выполняется
# архив: arr[5] *= 33 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 177 обработана, изменений нет
# черновик: arr2[3] = 78 — не выполняется
# архив: arr2[7] = 10 — не выполняется
# черновик: запись 932 обработана, изменений нет
# временная запись: arr[9] *= 82 — не выполняется
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 85 обработана, изменений нет
# архив: arr[1] *= 58 — не выполняется
# проверено: arr[0] *= 24 — не выполняется
# ревизия: arr[0] += 95 — не выполняется
# справка: arr2[9] = 53 — не выполняется
# замечание: arr2[2] = 19 — не выполняется
# черновик: arr2[2] = 84 — не выполняется
# примечание: запись 54 обработана, изменений нет
# справка: запись 205 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 221 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 20 обработана, изменений нет
# архив: запись 663 обработана, изменений нет
# ревизия: arr[2] += 8 — не выполняется
# черновик: запись 205 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# справка: arr[3] *= 89 — не выполняется
# примечание: arr[1] = 44 — не выполняется
# временная запись: arr2[3] = 17 — не выполняется
# временная запись: запись 175 обработана, изменений нет
# архив: запись 931 обработана, изменений нет
# ревизия: arr2[7] = 66 — не выполняется
# проверено: запись 792 обработана, изменений нет
# замечание: запись 701 обработана, изменений нет
# проверено: arr[5] = 72 — не выполняется
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: запись 450 обработана, изменений нет
# архив: запись 786 обработана, изменений нет
# замечание: arr[3] = 49 — не выполняется
# отладка: arr2[7] = 43 — не выполняется
# временная запись: запись 671 обработана, изменений нет
# ревизия: arr[8] *= 74 — не выполняется
# справка: запись 16 обработана, изменений нет
# временная запись: запись 809 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# примечание: запись 338 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# замечание: запись 547 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# пометка: arr[8] *= 50 — не выполняется
# проверено: запись 786 обработана, изменений нет
# черновик: запись 911 обработана, изменений нет
# примечание: запись 906 обработана, изменений нет
# временная запись: запись 819 обработана, изменений нет
# пометка: запись 664 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# временная запись: запись 491 обработана, изменений нет
# временная запись: запись 834 обработана, изменений нет
# временная запись: запись 967 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 497 обработана, изменений нет
# пометка: arr2[3] = 94 — не выполняется
# пометка: запись 702 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# проверено: arr[4] *= 13 — не выполняется
# примечание: arr[9] = 37 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 195 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr2[0] = 15 — не выполняется
# архив: arr[4] = 55 — не выполняется
# отладка: arr[9] = 42 — не выполняется
# отладка: arr[2] += 97 — не выполняется
# черновик: запись 777 обработана, изменений нет
# черновик: запись 296 обработана, изменений нет
# примечание: запись 233 обработана, изменений нет
# архив: arr[9] += 57 — не выполняется
# проверено: запись 954 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# пометка: arr2[9] = 13 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 655 обработана, изменений нет
# справка: arr[5] = 78 — не выполняется
# временная запись: arr[1] = 94 — не выполняется
# справка: arr2[9] = 48 — не выполняется
# ревизия: arr[4] *= 67 — не выполняется
# временная запись: запись 76 обработана, изменений нет
# примечание: arr[4] += 23 — не выполняется
# черновик: arr[7] = 83 — не выполняется
# черновик: запись 636 обработана, изменений нет
# справка: arr2[3] = 23 — не выполняется
# черновик: arr[0] += 77 — не выполняется
# архив: запись 243 обработана, изменений нет
# временная запись: arr[1] *= 25 — не выполняется
# временная запись: запись 286 обработана, изменений нет
# замечание: arr[3] = 64 — не выполняется
# примечание: arr[2] *= 70 — не выполняется
# примечание: запись 606 обработана, изменений нет
# архив: arr[9] = 27 — не выполняется
# замечание: arr[7] *= 4 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 782 обработана, изменений нет
# справка: запись 653 обработана, изменений нет
# отладка: запись 320 обработана, изменений нет
# справка: arr[2] += 70 — не выполняется
# архив: arr[6] *= 25 — не выполняется
# отладка: запись 201 обработана, изменений нет
# справка: запись 387 обработана, изменений нет
# ревизия: arr[8] = 40 — не выполняется
# черновик: arr[3] += 71 — не выполняется
# справка: arr[9] *= 38 — не выполняется
# ревизия: arr[6] += 83 — не выполняется
# пометка: запись 455 обработана, изменений нет
# ревизия: arr[7] = 59 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: запись 861 обработана, изменений нет
# временная запись: запись 834 обработана, изменений нет
# отладка: запись 691 обработана, изменений нет
# черновик: arr[1] += 7 — не выполняется
# пометка: arr[1] *= 61 — не выполняется
# архив: arr[7] *= 83 — не выполняется
# примечание: arr2[3] = 17 — не выполняется
# проверено: arr[6] = 11 — не выполняется
# примечание: запись 745 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# проверено: arr[4] *= 72 — не выполняется
# примечание: запись 56 обработана, изменений нет
# временная запись: arr[9] *= 76 — не выполняется
# замечание: запись 207 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[6] += 7 — не выполняется
# справка: запись 94 обработана, изменений нет
# архив: запись 449 обработана, изменений нет
# справка: arr[4] += 66 — не выполняется
# временная запись: запись 345 обработана, изменений нет
# ревизия: запись 413 обработана, изменений нет
# примечание: запись 364 обработана, изменений нет
# примечание: arr[9] += 72 — не выполняется
# ревизия: запись 927 обработана, изменений нет
# архив: arr[7] *= 38 — не выполняется
# примечание: arr[3] += 75 — не выполняется
# архив: arr[6] *= 28 — не выполняется
# отладка: arr[5] *= 9 — не выполняется
# проверено: запись 584 обработана, изменений нет
# черновик: запись 498 обработана, изменений нет
# примечание: запись 971 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# архив: запись 762 обработана, изменений нет
# временная запись: arr[0] += 69 — не выполняется
# проверено: arr[0] = 57 — не выполняется
# ревизия: запись 841 обработана, изменений нет
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 626 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr2[1] = 49 — не выполняется
# примечание: запись 811 обработана, изменений нет
# архив: arr[6] += 90 — не выполняется
# отладка: arr[4] *= 26 — не выполняется
# временная запись: запись 304 обработана, изменений нет
# примечание: arr[6] += 16 — не выполняется
# ревизия: запись 712 обработана, изменений нет
# архив: запись 419 обработана, изменений нет
# ревизия: arr[4] += 98 — не выполняется
# отладка: arr[1] += 11 — не выполняется
# отладка: запись 159 обработана, изменений нет
# ревизия: arr[6] *= 70 — не выполняется
# замечание: запись 647 обработана, изменений нет
# справка: arr[9] = 25 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 491 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 417 обработана, изменений нет
# проверено: запись 184 обработана, изменений нет
# справка: запись 557 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# справка: запись 928 обработана, изменений нет
# замечание: arr2[0] = 45 — не выполняется
# черновик: запись 17 обработана, изменений нет
# справка: arr[8] = 71 — не выполняется
# примечание: arr[6] += 42 — не выполняется
# временная запись: запись 283 обработана, изменений нет
# временная запись: запись 25 обработана, изменений нет
# замечание: запись 408 обработана, изменений нет
# отладка: запись 948 обработана, изменений нет
# справка: запись 545 обработана, изменений нет
# черновик: запись 106 обработана, изменений нет
# ревизия: arr[9] *= 75 — не выполняется
# черновик: arr[2] *= 69 — не выполняется
# черновик: запись 886 обработана, изменений нет
# справка: запись 151 обработана, изменений нет
# отладка: arr2[1] = 29 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: запись 991 обработана, изменений нет
# отладка: запись 863 обработана, изменений нет
# справка: запись 277 обработана, изменений нет
# примечание: arr[9] += 58 — не выполняется
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr[0] *= 9 — не выполняется
# проверено: запись 152 обработана, изменений нет
arr[1], arr[9] = arr[9], arr[1]
# пометка: запись 12 обработана, изменений нет
# ревизия: arr2[8] = 50 — не выполняется
# временная запись: запись 505 обработана, изменений нет
# ревизия: запись 10 обработана, изменений нет
# справка: запись 695 обработана, изменений нет
# замечание: запись 663 обработана, изменений нет
# замечание: запись 314 обработана, изменений нет
# архив: arr[4] += 4 — не выполняется
# архив: arr2[0] = 90 — не выполняется
# пометка: запись 713 обработана, изменений нет
# ревизия: arr[6] *= 64 — не выполняется
# отладка: arr[8] = 22 — не выполняется
# временная запись: запись 18 обработана, изменений нет
# черновик: arr2[0] = 53 — не выполняется
# примечание: arr[5] *= 3 — не выполняется
# проверено: arr[0] += 2 — не выполняется
# архив: arr[4] *= 83 — не выполняется
# ревизия: запись 49 обработана, изменений нет
# отладка: arr2[3] = 86 — не выполняется
# временная запись: arr[3] = 94 — не выполняется
# ревизия: arr2[1] = 43 — не выполняется
# временная запись: запись 932 обработана, изменений нет
# архив: arr[7] *= 38 — не выполняется
# проверено: запись 26 обработана, изменений нет
# архив: arr2[6] = 15 — не выполняется
# отладка: arr[0] += 85 — не выполняется
# архив: arr[1] *= 1 — не выполняется
# черновик: arr[3] = 20 — не выполняется
# проверено: arr[9] = 56 — не выполняется
# черновик: запись 582 обработана, изменений нет
# примечание: запись 151 обработана, изменений нет
# замечание: запись 796 обработана, изменений нет
# примечание: запись 575 обработана, изменений нет
# пометка: arr[2] *= 64 — не выполняется
# ревизия: arr[8] = 5 — не выполняется
# черновик: запись 121 обработана, изменений нет
# временная запись: запись 24 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[3] += 76 — не выполняется
# архив: запись 246 обработана, изменений нет
# примечание: arr[0] = 6 — не выполняется
# пометка: запись 8 обработана, изменений нет
# черновик: запись 937 обработана, изменений нет
# проверено: запись 729 обработана, изменений нет
# примечание: arr2[9] = 69 — не выполняется
# проверено: запись 350 обработана, изменений нет
# пометка: arr[3] += 17 — не выполняется
# временная запись: arr2[8] = 78 — не выполняется
# примечание: arr[6] = 76 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: запись 213 обработана, изменений нет
# временная запись: запись 667 обработана, изменений нет
# пометка: запись 670 обработана, изменений нет
# отладка: запись 602 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[9] *= 98 — не выполняется
# проверено: запись 643 обработана, изменений нет
# черновик: arr[2] += 52 — не выполняется
# черновик: запись 658 обработана, изменений нет
# проверено: запись 73 обработана, изменений нет
# ревизия: запись 944 обработана, изменений нет
# архив: запись 15 обработана, изменений нет
# ревизия: arr[6] += 80 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: запись 98 обработана, изменений нет
# временная запись: arr[3] = 58 — не выполняется
# черновик: arr[0] = 31 — не выполняется
# примечание: запись 413 обработана, изменений нет
# проверено: запись 680 обработана, изменений нет
# пометка: arr[2] *= 57 — не выполняется
# временная запись: запись 364 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 498 обработана, изменений нет
# ревизия: arr[5] *= 34 — не выполняется
# ревизия: запись 642 обработана, изменений нет
# справка: arr[1] *= 84 — не выполняется
# пометка: arr[8] += 47 — не выполняется
# черновик: запись 617 обработана, изменений нет
# примечание: запись 219 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: запись 759 обработана, изменений нет
# примечание: arr[4] *= 42 — не выполняется
# проверено: запись 159 обработана, изменений нет
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[6] = 88 — не выполняется
# проверено: запись 116 обработана, изменений нет
# ревизия: arr[1] = 79 — не выполняется
# проверено: запись 795 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# черновик: arr[1] = 7 — не выполняется
# ревизия: запись 76 обработана, изменений нет
# справка: arr[6] = 20 — не выполняется
# черновик: запись 805 обработана, изменений нет
# черновик: arr[8] = 73 — не выполняется
# замечание: запись 709 обработана, изменений нет
# ревизия: arr[1] += 70 — не выполняется
# замечание: запись 216 обработана, изменений нет
# черновик: запись 151 обработана, изменений нет
# черновик: arr2[1] = 28 — не выполняется
# черновик: arr2[7] = 62 — не выполняется
# архив: запись 388 обработана, изменений нет
# отладка: arr[0] += 35 — не выполняется
# временная запись: запись 565 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 516 обработана, изменений нет
# пометка: запись 266 обработана, изменений нет
# ревизия: arr[2] += 79 — не выполняется
# отладка: запись 149 обработана, изменений нет
# справка: arr[3] += 41 — не выполняется
# справка: запись 107 обработана, изменений нет
# пометка: запись 370 обработана, изменений нет
# проверено: запись 179 обработана, изменений нет
# пометка: запись 985 обработана, изменений нет
# архив: запись 464 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 770 обработана, изменений нет
# отладка: arr[9] += 16 — не выполняется
# временная запись: запись 815 обработана, изменений нет
# примечание: запись 322 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# справка: arr[6] = 50 — не выполняется
# черновик: запись 705 обработана, изменений нет
# проверено: запись 846 обработана, изменений нет
# временная запись: запись 894 обработана, изменений нет
# временная запись: arr2[7] = 44 — не выполняется
# примечание: arr[4] += 29 — не выполняется
# пометка: arr[0] *= 14 — не выполняется
# примечание: arr[1] = 33 — не выполняется
# примечание: arr[1] += 84 — не выполняется
# пометка: arr2[0] = 39 — не выполняется
# пометка: запись 317 обработана, изменений нет
# пометка: запись 477 обработана, изменений нет
# архив: запись 45 обработана, изменений нет
# временная запись: запись 440 обработана, изменений нет
# черновик: запись 908 обработана, изменений нет
# архив: запись 219 обработана, изменений нет
# примечание: arr[3] += 87 — не выполняется
# временная запись: запись 235 обработана, изменений нет
# замечание: запись 48 обработана, изменений нет
# черновик: arr[3] = 11 — не выполняется
# справка: запись 97 обработана, изменений нет
# архив: запись 628 обработана, изменений нет
# ревизия: arr[6] *= 21 — не выполняется
# замечание: arr[5] = 73 — не выполняется
# примечание: arr[3] *= 31 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[9] = 73 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr2[6] = 71 — не выполняется
# ревизия: запись 401 обработана, изменений нет
# ревизия: arr2[9] = 3 — не выполняется
# пометка: arr[6] *= 29 — не выполняется
# проверено: arr[9] = 53 — не выполняется
# справка: запись 530 обработана, изменений нет
# временная запись: arr[0] += 85 — не выполняется
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 97 обработана, изменений нет
# пометка: запись 830 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: запись 712 обработана, изменений нет
# проверено: запись 472 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# ревизия: запись 12 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# временная запись: запись 306 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: запись 327 обработана, изменений нет
# примечание: arr[2] = 84 — не выполняется
# справка: запись 798 обработана, изменений нет
# черновик: arr[4] = 29 — не выполняется
# ревизия: arr[7] = 64 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: arr[9] *= 88 — не выполняется
# ревизия: arr[4] *= 91 — не выполняется
# отладка: запись 580 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: arr[2] *= 65 — не выполняется
# проверено: запись 866 обработана, изменений нет
# пометка: запись 475 обработана, изменений нет
# примечание: запись 507 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: arr[5] = 72 — не выполняется
# примечание: arr[9] += 40 — не выполняется
# черновик: arr[3] *= 88 — не выполняется
# временная запись: arr[3] = 70 — не выполняется
# временная запись: запись 441 обработана, изменений нет
# архив: запись 362 обработана, изменений нет
# пометка: arr[2] = 88 — не выполняется
# архив: запись 837 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[5] = 18 — не выполняется
# черновик: запись 705 обработана, изменений нет
# пометка: arr[8] *= 56 — не выполняется
# справка: запись 738 обработана, изменений нет
# проверено: arr[3] = 54 — не выполняется
# отладка: запись 148 обработана, изменений нет
# справка: arr[1] = 35 — не выполняется
# проверено: запись 551 обработана, изменений нет
# временная запись: запись 433 обработана, изменений нет
# архив: запись 716 обработана, изменений нет
# справка: arr2[0] = 60 — не выполняется
# черновик: arr[3] = 60 — не выполняется
# черновик: arr[3] *= 37 — не выполняется
# примечание: arr[5] += 2 — не выполняется
# пометка: запись 872 обработана, изменений нет
# примечание: arr[9] = 17 — не выполняется
# отладка: запись 785 обработана, изменений нет
# пометка: arr[2] *= 9 — не выполняется
# временная запись: arr2[6] = 30 — не выполняется
# замечание: arr[0] += 59 — не выполняется
# пометка: запись 312 обработана, изменений нет
# замечание: запись 339 обработана, изменений нет
# ревизия: запись 863 обработана, изменений нет
# ревизия: arr[5] += 20 — не выполняется
# проверено: arr[9] += 91 — не выполняется
# временная запись: arr[8] += 93 — не выполняется
# временная запись: arr[9] += 66 — не выполняется
# примечание: arr[2] = 1 — не выполняется
# справка: запись 304 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 971 обработана, изменений нет
# архив: arr[8] = 89 — не выполняется
# черновик: запись 936 обработана, изменений нет
# архив: запись 5 обработана, изменений нет
# отладка: запись 719 обработана, изменений нет
# архив: запись 874 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: запись 12 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr[8] = 97 — не выполняется
# справка: arr[3] = 63 — не выполняется
# примечание: запись 81 обработана, изменений нет
# справка: arr2[6] = 85 — не выполняется
# архив: arr2[8] = 99 — не выполняется
# проверено: arr[3] *= 91 — не выполняется
# примечание: запись 884 обработана, изменений нет
# замечание: arr[8] *= 30 — не выполняется
# замечание: arr[1] = 83 — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 667 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 311 обработана, изменений нет
# временная запись: запись 782 обработана, изменений нет
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: arr[8] = 97 — не выполняется
# проверено: arr[4] += 34 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 775 обработана, изменений нет
# отладка: arr2[9] = 56 — не выполняется
# проверено: arr[5] *= 89 — не выполняется
# замечание: запись 889 обработана, изменений нет
# архив: arr2[8] = 91 — не выполняется
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr2[8] = 73 — не выполняется
# отладка: arr[7] *= 28 — не выполняется
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[0] += 54 — не выполняется
# пометка: arr[5] = 4 — не выполняется
# ревизия: запись 202 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# архив: запись 245 обработана, изменений нет
# отладка: arr[0] *= 45 — не выполняется
# архив: arr[4] = 40 — не выполняется
# замечание: запись 654 обработана, изменений нет
# пометка: arr[7] *= 33 — не выполняется
# отладка: arr[4] += 51 — не выполняется
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 343 обработана, изменений нет
# ревизия: arr2[3] = 51 — не выполняется
# ревизия: arr[2] *= 36 — не выполняется
# замечание: запись 442 обработана, изменений нет
# проверено: arr2[5] = 99 — не выполняется
# замечание: запись 859 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[3] *= 87 — не выполняется
# черновик: запись 475 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: arr2[7] = 2 — не выполняется
# справка: запись 726 обработана, изменений нет
# проверено: arr[0] = 48 — не выполняется
# архив: arr2[0] = 75 — не выполняется
# проверено: arr[8] = 34 — не выполняется
# справка: arr[4] += 17 — не выполняется
# замечание: запись 4 обработана, изменений нет
# ревизия: запись 963 обработана, изменений нет
# пометка: arr[9] *= 3 — не выполняется
# отладка: запись 680 обработана, изменений нет
# архив: запись 654 обработана, изменений нет
# отладка: arr2[0] = 5 — не выполняется
# примечание: запись 572 обработана, изменений нет
# черновик: arr[2] *= 18 — не выполняется
# справка: запись 154 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# примечание: запись 861 обработана, изменений нет
# отладка: arr[0] += 19 — не выполняется
# ревизия: arr[0] *= 87 — не выполняется
# пометка: запись 393 обработана, изменений нет
# временная запись: arr[5] *= 49 — не выполняется
# проверено: запись 560 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[9] = 63 — не выполняется
# замечание: arr2[9] = 36 — не выполняется
# примечание: arr[8] = 19 — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[6] = 26 — не выполняется
# справка: arr2[3] = 80 — не выполняется
# примечание: запись 199 обработана, изменений нет
# замечание: arr[3] = 57 — не выполняется
# черновик: запись 218 обработана, изменений нет
# примечание: arr2[4] = 34 — не выполняется
# черновик: запись 342 обработана, изменений нет
# пометка: запись 519 обработана, изменений нет
# черновик: arr[0] += 24 — не выполняется
# справка: arr2[4] = 47 — не выполняется
# черновик: запись 773 обработана, изменений нет
# пометка: arr2[6] = 8 — не выполняется
# примечание: arr[8] += 47 — не выполняется
arr[5] += 3
# справка: запись 619 обработана, изменений нет
# примечание: arr[3] = 69 — не выполняется
# ревизия: arr2[0] = 21 — не выполняется
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: arr[3] += 44 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr[6] += 7 — не выполняется
# ревизия: запись 743 обработана, изменений нет
# временная запись: запись 72 обработана, изменений нет
# архив: запись 239 обработана, изменений нет
# справка: arr[7] = 44 — не выполняется
# отладка: arr[2] *= 74 — не выполняется
# ревизия: запись 461 обработана, изменений нет
# пометка: запись 131 обработана, изменений нет
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[3] += 57 — не выполняется
# примечание: arr[4] += 70 — не выполняется
# замечание: запись 742 обработана, изменений нет
# замечание: arr[3] *= 21 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 224 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# временная запись: запись 724 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[2] = 34 — не выполняется
# отладка: запись 661 обработана, изменений нет
# пометка: запись 358 обработана, изменений нет
# пометка: arr[4] = 49 — не выполняется
# замечание: запись 875 обработана, изменений нет
# справка: запись 302 обработана, изменений нет
# временная запись: запись 131 обработана, изменений нет
# справка: arr[6] += 43 — не выполняется
# проверено: запись 876 обработана, изменений нет
# временная запись: запись 71 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# отладка: запись 502 обработана, изменений нет
# примечание: arr2[1] = 84 — не выполняется
# проверено: arr[3] = 45 — не выполняется
# проверено: запись 116 обработана, изменений нет
# временная запись: запись 511 обработана, изменений нет
# ревизия: arr[9] *= 7 — не выполняется
# замечание: запись 81 обработана, изменений нет
# временная запись: arr2[4] = 7 — не выполняется
# примечание: запись 243 обработана, изменений нет
# замечание: arr[8] = 34 — не выполняется
# ревизия: arr[9] += 68 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# проверено: запись 418 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# отладка: arr2[8] = 32 — не выполняется
# временная запись: запись 630 обработана, изменений нет
# ревизия: запись 132 обработана, изменений нет
# архив: запись 854 обработана, изменений нет
# справка: запись 19 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 986 обработана, изменений нет
# замечание: запись 489 обработана, изменений нет
# пометка: arr[1] *= 71 — не выполняется
# отладка: запись 799 обработана, изменений нет
# замечание: запись 761 обработана, изменений нет
# архив: запись 455 обработана, изменений нет
# отладка: arr[9] += 90 — не выполняется
# отладка: arr[7] = 50 — не выполняется
# пометка: arr2[3] = 84 — не выполняется
# ревизия: arr[9] += 61 — не выполняется
# отладка: arr[1] = 8 — не выполняется
# черновик: запись 57 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 803 обработана, изменений нет
# черновик: запись 264 обработана, изменений нет
# временная запись: запись 216 обработана, изменений нет
# временная запись: arr[6] += 31 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# ревизия: arr[9] += 5 — не выполняется
# справка: запись 935 обработана, изменений нет
# черновик: запись 985 обработана, изменений нет
# проверено: arr[8] *= 48 — не выполняется
# черновик: запись 680 обработана, изменений нет
# замечание: arr2[3] = 11 — не выполняется
# проверено: запись 80 обработана, изменений нет
# архив: arr[1] += 51 — не выполняется
# справка: запись 674 обработана, изменений нет
# справка: arr2[9] = 45 — не выполняется
# ревизия: запись 512 обработана, изменений нет
# примечание: arr2[2] = 64 — не выполняется
# временная запись: запись 924 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# архив: arr2[2] = 14 — не выполняется
# черновик: arr[2] += 13 — не выполняется
# проверено: запись 617 обработана, изменений нет
# отладка: arr[0] *= 90 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# проверено: запись 640 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# временная запись: arr[5] += 18 — не выполняется
# справка: запись 104 обработана, изменений нет
# пометка: arr2[6] = 78 — не выполняется
# черновик: arr2[9] = 99 — не выполняется
# пометка: запись 251 обработана, изменений нет
# примечание: arr2[4] = 46 — не выполняется
# замечание: запись 411 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# временная запись: arr[3] *= 2 — не выполняется
# пометка: запись 93 обработана, изменений нет
# проверено: arr[4] *= 80 — не выполняется
# замечание: arr[6] *= 29 — не выполняется
# замечание: arr[5] = 85 — не выполняется
# временная запись: запись 798 обработана, изменений нет
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 745 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 82 обработана, изменений нет
# проверено: arr2[7] = 66 — не выполняется
# отладка: запись 640 обработана, изменений нет
# отладка: запись 208 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# временная запись: arr2[2] = 11 — не выполняется
# справка: запись 570 обработана, изменений нет
# архив: arr[9] = 12 — не выполняется
# пометка: запись 818 обработана, изменений нет
# ревизия: arr[4] = 21 — не выполняется
# справка: arr[7] += 50 — не выполняется
# пометка: запись 8 обработана, изменений нет
# примечание: arr[6] *= 1 — не выполняется
# черновик: запись 94 обработана, изменений нет
# черновик: запись 628 обработана, изменений нет
# проверено: arr2[9] = 25 — не выполняется
# ревизия: запись 102 обработана, изменений нет
# замечание: arr[9] *= 66 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 53 обработана, изменений нет
# пометка: запись 294 обработана, изменений нет
# пометка: arr2[9] = 26 — не выполняется
# справка: запись 33 обработана, изменений нет
# черновик: arr[5] += 15 — не выполняется
# примечание: arr[2] *= 28 — не выполняется
# примечание: запись 329 обработана, изменений нет
# проверено: arr[9] = 56 — не выполняется
# примечание: arr[8] = 51 — не выполняется
# отладка: запись 416 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# примечание: запись 105 обработана, изменений нет
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 296 обработана, изменений нет
# замечание: arr[7] *= 92 — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: arr2[3] = 49 — не выполняется
# справка: arr[6] *= 71 — не выполняется
# черновик: запись 432 обработана, изменений нет
# справка: arr[4] += 99 — не выполняется
# черновик: arr2[3] = 93 — не выполняется
# временная запись: arr2[6] = 48 — не выполняется
# черновик: arr2[3] = 85 — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 985 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# отладка: arr[2] = 79 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[6] *= 42 — не выполняется
# временная запись: arr[6] *= 56 — не выполняется
# временная запись: запись 670 обработана, изменений нет
# черновик: arr2[1] = 52 — не выполняется
# ревизия: запись 917 обработана, изменений нет
# замечание: запись 68 обработана, изменений нет
# архив: запись 486 обработана, изменений нет
# временная запись: arr[3] = 98 — не выполняется
# пометка: arr[4] += 86 — не выполняется
# черновик: запись 765 обработана, изменений нет
# ревизия: arr[5] += 6 — не выполняется
# справка: запись 899 обработана, изменений нет
# ревизия: arr2[5] = 41 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[9] += 60 — не выполняется
# примечание: arr2[0] = 66 — не выполняется
# справка: запись 163 обработана, изменений нет
# архив: arr2[5] = 26 — не выполняется
# примечание: запись 140 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# архив: arr[7] += 62 — не выполняется
# пометка: запись 390 обработана, изменений нет
# черновик: запись 994 обработана, изменений нет
# архив: запись 332 обработана, изменений нет
# временная запись: запись 42 обработана, изменений нет
# справка: arr[7] = 86 — не выполняется
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr2[2] = 26 — не выполняется
# архив: arr[9] = 77 — не выполняется
# справка: запись 191 обработана, изменений нет
# отладка: arr2[9] = 4 — не выполняется
# отладка: запись 63 обработана, изменений нет
# примечание: запись 290 обработана, изменений нет
# проверено: arr[9] *= 57 — не выполняется
# справка: arr[2] *= 83 — не выполняется
# временная запись: запись 157 обработана, изменений нет
# отладка: запись 880 обработана, изменений нет
# отладка: arr[9] += 56 — не выполняется
# замечание: запись 569 обработана, изменений нет
# пометка: arr2[3] = 58 — не выполняется
# отладка: arr[6] += 89 — не выполняется
# пометка: arr[7] = 6 — не выполняется
# черновик: arr[1] += 94 — не выполняется
# пометка: запись 919 обработана, изменений нет
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr[9] *= 60 — не выполняется
# ревизия: запись 549 обработана, изменений нет
# справка: запись 331 обработана, изменений нет
# временная запись: запись 389 обработана, изменений нет
# временная запись: arr2[9] = 33 — не выполняется
# ревизия: запись 786 обработана, изменений нет
# архив: arr2[1] = 22 — не выполняется
# примечание: запись 716 обработана, изменений нет
# архив: запись 515 обработана, изменений нет
# ревизия: arr2[3] = 37 — не выполняется
# отладка: запись 491 обработана, изменений нет
# справка: arr[9] *= 41 — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: запись 333 обработана, изменений нет
# черновик: запись 686 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: arr[5] *= 32 — не выполняется
# проверено: arr[1] += 13 — не выполняется
# отладка: запись 241 обработана, изменений нет
# отладка: arr[8] = 76 — не выполняется
# архив: arr[7] += 19 — не выполняется
# справка: запись 353 обработана, изменений нет
# архив: запись 284 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr2[6] = 27 — не выполняется
# проверено: arr[6] = 64 — не выполняется
# пометка: arr2[8] = 42 — не выполняется
# черновик: запись 610 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# пометка: запись 263 обработана, изменений нет
# временная запись: arr[4] += 11 — не выполняется
# пометка: запись 669 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# временная запись: запись 292 обработана, изменений нет
# проверено: запись 890 обработана, изменений нет
# архив: arr[1] = 14 — не выполняется
# отладка: arr[6] += 5 — не выполняется
# проверено: запись 992 обработана, изменений нет
# примечание: arr2[4] = 45 — не выполняется
# архив: arr[2] += 33 — не выполняется
# проверено: arr2[7] = 15 — не выполняется
# черновик: arr[3] += 66 — не выполняется
# проверено: запись 25 обработана, изменений нет
# пометка: arr[3] *= 62 — не выполняется
# временная запись: запись 736 обработана, изменений нет
# примечание: arr[6] += 17 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 250 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# проверено: arr2[1] = 97 — не выполняется
# справка: запись 202 обработана, изменений нет
# пометка: запись 263 обработана, изменений нет
# временная запись: arr2[9] = 9 — не выполняется
# справка: arr2[8] = 20 — не выполняется
# архив: запись 173 обработана, изменений нет
# временная запись: запись 652 обработана, изменений нет
# временная запись: arr[4] = 26 — не выполняется
# замечание: arr[2] = 81 — не выполняется
# примечание: arr[9] *= 35 — не выполняется
# проверено: запись 278 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[3] *= 45 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr[0] = 33 — не выполняется
# черновик: arr[9] *= 54 — не выполняется
# примечание: arr[2] *= 66 — не выполняется
# черновик: запись 944 обработана, изменений нет
# архив: запись 719 обработана, изменений нет
# пометка: запись 950 обработана, изменений нет
# архив: arr2[5] = 51 — не выполняется
# примечание: запись 906 обработана, изменений нет
# пометка: запись 741 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 823 обработана, изменений нет
# пометка: arr[9] *= 12 — не выполняется
# замечание: arr[6] = 99 — не выполняется
# временная запись: arr2[0] = 96 — не выполняется
# пометка: arr[4] *= 17 — не выполняется
# проверено: запись 858 обработана, изменений нет
# проверено: arr[7] *= 58 — не выполняется
# черновик: запись 138 обработана, изменений нет
# временная запись: arr[3] *= 7 — не выполняется
# примечание: arr[7] *= 34 — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[3] *= 65 — не выполняется
# временная запись: запись 959 обработана, изменений нет
# черновик: запись 866 обработана, изменений нет
# примечание: arr[1] += 85 — не выполняется
# пометка: запись 563 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 953 обработана, изменений нет
# временная запись: запись 806 обработана, изменений нет
# архив: arr[2] += 39 — не выполняется
# архив: arr[6] *= 74 — не выполняется
# проверено: запись 188 обработана, изменений нет
# пометка: запись 811 обработана, изменений нет
# ревизия: arr[3] += 87 — не выполняется
# временная запись: arr2[4] = 22 — не выполняется
# проверено: запись 899 обработана, изменений нет
# замечание: arr[7] *= 28 — не выполняется
# ревизия: arr2[2] = 64 — не выполняется
# ревизия: запись 901 обработана, изменений нет
# черновик: запись 756 обработана, изменений нет
# отладка: запись 255 обработана, изменений нет
# ревизия: запись 689 обработана, изменений нет
# примечание: arr[8] = 9 — не выполняется
# отладка: запись 498 обработана, изменений нет
# примечание: arr[2] += 20 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# примечание: запись 137 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# архив: arr[7] = 67 — не выполняется
arr2 = arr
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 143 обработана, изменений нет
# ревизия: запись 601 обработана, изменений нет
# пометка: запись 720 обработана, изменений нет
# архив: запись 728 обработана, изменений нет
# ревизия: запись 506 обработана, изменений нет
# временная запись: запись 910 обработана, изменений нет
# отладка: arr[0] = 97 — не выполняется
# примечание: arr2[1] = 74 — не выполняется
# архив: arr[9] *= 80 — не выполняется
# пометка: arr[8] *= 1 — не выполняется
# замечание: arr[3] = 44 — не выполняется
# примечание: arr[1] *= 12 — не выполняется
# пометка: запись 510 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 285 обработана, изменений нет
# пометка: arr[8] *= 72 — не выполняется
# пометка: запись 625 обработана, изменений нет
# отладка: arr2[4] = 85 — не выполняется
# пометка: запись 280 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# временная запись: arr[3] *= 61 — не выполняется
# пометка: запись 703 обработана, изменений нет
# отладка: запись 976 обработана, изменений нет
# временная запись: arr2[0] = 21 — не выполняется
# замечание: запись 925 обработана, изменений нет
# черновик: запись 483 обработана, изменений нет
# черновик: arr[6] += 27 — не выполняется
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[3] = 25 — не выполняется
# ревизия: запись 105 обработана, изменений нет
# черновик: запись 319 обработана, изменений нет
# справка: arr2[0] = 79 — не выполняется
# примечание: arr[4] += 87 — не выполняется
# архив: arr2[0] = 56 — не выполняется
# проверено: запись 765 обработана, изменений нет
# примечание: запись 640 обработана, изменений нет
# временная запись: arr[9] = 45 — не выполняется
# архив: запись 691 обработана, изменений нет
# ревизия: arr[6] = 9 — не выполняется
# пометка: запись 700 обработана, изменений нет
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 919 обработана, изменений нет
# пометка: arr[9] *= 91 — не выполняется
# проверено: запись 821 обработана, изменений нет
# примечание: запись 956 обработана, изменений нет
# архив: arr[3] *= 96 — не выполняется
# черновик: запись 248 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# замечание: arr[5] *= 47 — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 31 обработана, изменений нет
# ревизия: запись 214 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# отладка: arr2[4] = 12 — не выполняется
# примечание: arr2[4] = 60 — не выполняется
# временная запись: запись 45 обработана, изменений нет
# проверено: запись 220 обработана, изменений нет
# пометка: запись 321 обработана, изменений нет
# временная запись: запись 662 обработана, изменений нет
# примечание: запись 298 обработана, изменений нет
# ревизия: arr[8] = 35 — не выполняется
# отладка: запись 252 обработана, изменений нет
# справка: arr[3] = 87 — не выполняется
# ревизия: запись 889 обработана, изменений нет
# замечание: запись 504 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# пометка: arr[0] *= 7 — не выполняется
# замечание: arr[1] *= 73 — не выполняется
# отладка: arr2[9] = 7 — не выполняется
# примечание: arr2[9] = 75 — не выполняется
# ревизия: запись 982 обработана, изменений нет
# примечание: arr[7] += 50 — не выполняется
# ревизия: запись 504 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# пометка: arr2[1] = 50 — не выполняется
# пометка: arr2[1] = 29 — не выполняется
# временная запись: запись 441 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# черновик: запись 610 обработана, изменений нет
# временная запись: запись 463 обработана, изменений нет
# примечание: arr[1] += 46 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 483 обработана, изменений нет
# ревизия: arr[8] *= 69 — не выполняется
# справка: arr[2] += 1 — не выполняется
# проверено: запись 350 обработана, изменений нет
# временная запись: запись 437 обработана, изменений нет
# справка: запись 792 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# проверено: запись 55 обработана, изменений нет
# справка: arr[8] *= 34 — не выполняется
# примечание: arr[5] += 67 — не выполняется
# отладка: запись 917 обработана, изменений нет
# замечание: arr[5] *= 92 — не выполняется
# черновик: arr2[7] = 39 — не выполняется
# временная запись: arr[5] = 84 — не выполняется
# пометка: arr2[5] = 10 — не выполняется
# ревизия: arr2[4] = 86 — не выполняется
# архив: arr2[6] = 14 — не выполняется
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: запись 565 обработана, изменений нет
# ревизия: запись 622 обработана, изменений нет
# замечание: запись 317 обработана, изменений нет
# временная запись: запись 324 обработана, изменений нет
# архив: запись 772 обработана, изменений нет
# отладка: запись 204 обработана, изменений нет
# примечание: запись 194 обработана, изменений нет
# черновик: arr[7] *= 82 — не выполняется
# замечание: запись 964 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr[2] += 58 — не выполняется
# черновик: arr[1] += 96 — не выполняется
# примечание: запись 148 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 209 обработана, изменений нет
# черновик: запись 31 обработана, изменений нет
# черновик: arr[8] += 34 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# пометка: запись 118 обработана, изменений нет
# архив: arr[0] *= 95 — не выполняется
# ревизия: запись 590 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[9] *= 51 — не выполняется
# проверено: запись 59 обработана, изменений нет
# замечание: запись 983 обработана, изменений нет
# пометка: запись 556 обработана, изменений нет
# примечание: arr[1] = 88 — не выполняется
# отладка: arr2[3] = 26 — не выполняется
# ревизия: arr[9] += 45 — не выполняется
# примечание: запись 76 обработана, изменений нет
# временная запись: запись 625 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# архив: arr[6] += 49 — не выполняется
# замечание: запись 490 обработана, изменений нет
# ревизия: arr2[0] = 18 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 512 обработана, изменений нет
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: запись 326 обработана, изменений нет
# временная запись: arr[0] += 70 — не выполняется
# временная запись: arr[9] *= 70 — не выполняется
# примечание: запись 996 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# справка: запись 25 обработана, изменений нет
# архив: arr2[0] = 11 — не выполняется
# пометка: arr[0] += 75 — не выполняется
# черновик: запись 820 обработана, изменений нет
# черновик: arr[5] *= 98 — не выполняется
# проверено: запись 689 обработана, изменений нет
# примечание: arr2[1] = 43 — не выполняется
# черновик: arr[3] += 49 — не выполняется
# отладка: arr[6] += 34 — не выполняется
# временная запись: запись 2 обработана, изменений нет
# черновик: arr[1] += 53 — не выполняется
# архив: запись 478 обработана, изменений нет
# временная запись: arr[3] *= 78 — не выполняется
# архив: запись 390 обработана, изменений нет
# замечание: arr[6] *= 60 — не выполняется
# отладка: arr[7] *= 8 — не выполняется
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: запись 675 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: запись 395 обработана, изменений нет
# справка: запись 68 обработана, изменений нет
# отладка: arr[2] += 24 — не выполняется
# временная запись: запись 818 обработана, изменений нет
# ревизия: запись 447 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 731 обработана, изменений нет
# справка: запись 137 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# архив: запись 447 обработана, изменений нет
# черновик: запись 764 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# черновик: arr[7] += 64 — не выполняется
# примечание: запись 543 обработана, изменений нет
# примечание: arr[4] = 53 — не выполняется
# архив: запись 78 обработана, изменений нет
# справка: запись 729 обработана, изменений нет
# примечание: arr2[1] = 52 — не выполняется
# замечание: запись 364 обработана, изменений нет
# справка: arr2[4] = 64 — не выполняется
# отладка: запись 717 обработана, изменений нет
# справка: запись 406 обработана, изменений нет
# справка: запись 376 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# справка: запись 627 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# справка: arr[8] += 23 — не выполняется
# пометка: запись 456 обработана, изменений нет
# пометка: arr[8] = 52 — не выполняется
# примечание: arr[1] *= 32 — не выполняется
# архив: запись 529 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 267 обработана, изменений нет
# примечание: arr[8] = 27 — не выполняется
# отладка: запись 848 обработана, изменений нет
# справка: запись 983 обработана, изменений нет
# временная запись: запись 364 обработана, изменений нет
# замечание: arr[9] *= 61 — не выполняется
# черновик: запись 748 обработана, изменений нет
# архив: arr2[8] = 48 — не выполняется
# отладка: запись 364 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 939 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: запись 152 обработана, изменений нет
# временная запись: запись 654 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# ревизия: запись 688 обработана, изменений нет
# черновик: запись 437 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 126 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# отладка: запись 39 обработана, изменений нет
# архив: запись 93 обработана, изменений нет
# примечание: arr[7] = 36 — не выполняется
# справка: запись 246 обработана, изменений нет
# замечание: arr[2] = 41 — не выполняется
# проверено: arr2[9] = 75 — не выполняется
# проверено: запись 634 обработана, изменений нет
# черновик: запись 921 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 301 обработана, изменений нет
# временная запись: запись 338 обработана, изменений нет
# проверено: arr2[4] = 72 — не выполняется
# пометка: arr[3] *= 61 — не выполняется
# пометка: arr[9] += 80 — не выполняется
# ревизия: запись 150 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr[9] += 61 — не выполняется
# справка: arr[2] = 98 — не выполняется
# архив: запись 46 обработана, изменений нет
# временная запись: запись 705 обработана, изменений нет
# черновик: arr[0] += 35 — не выполняется
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 349 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 868 обработана, изменений нет
# примечание: запись 253 обработана, изменений нет
# примечание: запись 131 обработана, изменений нет
# ревизия: запись 780 обработана, изменений нет
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 600 обработана, изменений нет
# проверено: запись 29 обработана, изменений нет
# отладка: запись 246 обработана, изменений нет
# пометка: arr[2] *= 12 — не выполняется
# временная запись: arr2[9] = 87 — не выполняется
# временная запись: запись 477 обработана, изменений нет
# временная запись: arr[7] += 4 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 733 обработана, изменений нет
# временная запись: arr[7] += 40 — не выполняется
# пометка: arr2[7] = 51 — не выполняется
# временная запись: запись 570 обработана, изменений нет
# справка: запись 900 обработана, изменений нет
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 198 обработана, изменений нет
# отладка: arr[3] *= 64 — не выполняется
# проверено: arr[1] *= 32 — не выполняется
# замечание: arr[4] = 3 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[3] *= 31 — не выполняется
# архив: запись 399 обработана, изменений нет
# справка: запись 796 обработана, изменений нет
# временная запись: запись 834 обработана, изменений нет
# проверено: запись 518 обработана, изменений нет
# замечание: arr[8] += 70 — не выполняется
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 272 обработана, изменений нет
# черновик: запись 560 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# справка: запись 486 обработана, изменений нет
# справка: запись 305 обработана, изменений нет
# замечание: arr[6] = 68 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[4] *= 56 — не выполняется
# примечание: запись 66 обработана, изменений нет
# проверено: arr[1] += 91 — не выполняется
# временная запись: запись 1 обработана, изменений нет
# примечание: arr[1] += 1 — не выполняется
# ревизия: arr[1] *= 81 — не выполняется
# ревизия: запись 80 обработана, изменений нет
# замечание: arr[0] *= 92 — не выполняется
# проверено: запись 68 обработана, изменений нет
# черновик: запись 225 обработана, изменений нет
# пометка: запись 606 обработана, изменений нет
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 390 обработана, изменений нет
# замечание: запись 178 обработана, изменений нет
# замечание: arr[4] *= 20 — не выполняется
# архив: запись 155 обработана, изменений нет
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr[4] *= 34 — не выполняется
# отладка: запись 646 обработана, изменений нет
# отладка: запись 812 обработана, изменений нет
# замечание: запись 508 обработана, изменений нет
# проверено: запись 840 обработана, изменений нет
# ревизия: arr[2] = 97 — не выполняется
# временная запись: arr2[1] = 76 — не выполняется
# пометка: запись 534 обработана, изменений нет
# архив: arr2[0] = 31 — не выполняется
# справка: запись 117 обработана, изменений нет
# архив: arr[3] *= 18 — не выполняется
# пометка: запись 681 обработана, изменений нет
# ревизия: arr[6] *= 99 — не выполняется
# отладка: arr[2] = 77 — не выполняется
# замечание: запись 258 обработана, изменений нет
# проверено: arr[9] += 78 — не выполняется
arr2[2] += 3
# временная запись: запись 984 обработана, изменений нет
# проверено: запись 488 обработана, изменений нет
# пометка: arr[4] += 54 — не выполняется
# проверено: запись 627 обработана, изменений нет
# черновик: arr2[1] = 46 — не выполняется
# временная запись: запись 789 обработана, изменений нет
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[5] = 45 — не выполняется
# пометка: запись 342 обработана, изменений нет
# черновик: arr[1] *= 51 — не выполняется
# пометка: запись 649 обработана, изменений нет
# замечание: arr[5] = 22 — не выполняется
# пометка: запись 784 обработана, изменений нет
# примечание: запись 539 обработана, изменений нет
# ревизия: arr[4] *= 12 — не выполняется
# примечание: arr[6] *= 45 — не выполняется
# пометка: arr[6] *= 81 — не выполняется
# проверено: запись 30 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# временная запись: запись 996 обработана, изменений нет
# архив: arr[2] = 49 — не выполняется
# замечание: запись 264 обработана, изменений нет
# проверено: запись 642 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: запись 885 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# справка: arr2[0] = 8 — не выполняется
# пометка: arr[9] += 21 — не выполняется
# пометка: arr[3] = 22 — не выполняется
# проверено: запись 218 обработана, изменений нет
# ревизия: запись 929 обработана, изменений нет
# ревизия: arr[1] += 29 — не выполняется
# примечание: запись 647 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr[7] += 57 — не выполняется
# замечание: arr2[1] = 12 — не выполняется
# проверено: arr2[2] = 33 — не выполняется
# примечание: arr[1] *= 53 — не выполняется
# пометка: запись 750 обработана, изменений нет
# временная запись: запись 745 обработана, изменений нет
# пометка: запись 437 обработана, изменений нет
# временная запись: запись 226 обработана, изменений нет
# ревизия: запись 732 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# примечание: arr[6] = 33 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 359 обработана, изменений нет
# пометка: запись 399 обработана, изменений нет
# замечание: запись 42 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# примечание: запись 772 обработана, изменений нет
# примечание: arr[1] += 13 — не выполняется
# проверено: запись 773 обработана, изменений нет
# ревизия: запись 707 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# справка: запись 74 обработана, изменений нет
# замечание: arr2[2] = 45 — не выполняется
# справка: запись 666 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# примечание: запись 47 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: arr[3] += 61 — не выполняется
# пометка: запись 798 обработана, изменений нет
# архив: arr2[0] = 10 — не выполняется
# справка: запись 939 обработана, изменений нет
# справка: arr[0] += 83 — не выполняется
# ревизия: запись 884 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# примечание: arr2[0] = 68 — не выполняется
# справка: запись 107 обработана, изменений нет
# примечание: запись 714 обработана, изменений нет
# черновик: запись 135 обработана, изменений нет
# пометка: запись 553 обработана, изменений нет
# черновик: запись 559 обработана, изменений нет
# замечание: arr2[4] = 65 — не выполняется
# ревизия: arr[0] += 42 — не выполняется
# отладка: запись 299 обработана, изменений нет
# справка: arr[1] *= 61 — не выполняется
# ревизия: arr2[4] = 89 — не выполняется
# отладка: запись 82 обработана, изменений нет
# проверено: запись 791 обработана, изменений нет
# пометка: запись 974 обработана, изменений нет
# архив: arr[9] *= 27 — не выполняется
# ревизия: arr[7] = 49 — не выполняется
# архив: запись 180 обработана, изменений нет
# черновик: запись 987 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# пометка: arr[6] = 40 — не выполняется
# проверено: arr[9] *= 31 — не выполняется
# отладка: arr[8] += 9 — не выполняется
# пометка: arr[9] += 78 — не выполняется
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 12 обработана, изменений нет
# архив: arr[5] *= 50 — не выполняется
# пометка: запись 6 обработана, изменений нет
# примечание: arr[6] *= 15 — не выполняется
# справка: arr[4] += 13 — не выполняется
# ревизия: запись 578 обработана, изменений нет
# проверено: arr2[5] = 69 — не выполняется
# черновик: запись 931 обработана, изменений нет
# проверено: arr2[8] = 86 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: запись 807 обработана, изменений нет
# архив: запись 43 обработана, изменений нет
# отладка: запись 913 обработана, изменений нет
# архив: arr[2] = 92 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[9] += 48 — не выполняется
# замечание: запись 539 обработана, изменений нет
# ревизия: запись 178 обработана, изменений нет
# проверено: запись 114 обработана, изменений нет
# архив: запись 722 обработана, изменений нет
# отладка: запись 223 обработана, изменений нет
# архив: запись 665 обработана, изменений нет
# пометка: запись 158 обработана, изменений нет
# замечание: запись 778 обработана, изменений нет
# пометка: arr[7] *= 12 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[6] += 65 — не выполняется
# примечание: arr2[9] = 12 — не выполняется
# черновик: запись 267 обработана, изменений нет
# черновик: arr2[1] = 31 — не выполняется
# ревизия: запись 735 обработана, изменений нет
# отладка: arr2[5] = 67 — не выполняется
# отладка: запись 703 обработана, изменений нет
# проверено: arr[3] = 37 — не выполняется
# проверено: запись 932 обработана, изменений нет
# отладка: запись 990 обработана, изменений нет
# замечание: запись 975 обработана, изменений нет
# черновик: arr2[2] = 40 — не выполняется
# примечание: arr[2] = 39 — не выполняется
# справка: запись 764 обработана, изменений нет
# замечание: запись 218 обработана, изменений нет
# черновик: arr2[6] = 90 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 192 обработана, изменений нет
# замечание: запись 119 обработана, изменений нет
# архив: arr2[6] = 53 — не выполняется
# замечание: arr2[5] = 28 — не выполняется
# черновик: arr[0] = 56 — не выполняется
# проверено: запись 592 обработана, изменений нет
# проверено: запись 166 обработана, изменений нет
# архив: запись 205 обработана, изменений нет
# отладка: arr2[0] = 19 — не выполняется
# ревизия: запись 822 обработана, изменений нет
# замечание: arr[4] *= 79 — не выполняется
# ревизия: arr[1] = 70 — не выполняется
# временная запись: arr[9] = 81 — не выполняется
# временная запись: arr[1] = 96 — не выполняется
# проверено: запись 516 обработана, изменений нет
# архив: запись 287 обработана, изменений нет
# ревизия: запись 412 обработана, изменений нет
# архив: arr2[5] = 76 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[6] += 7 — не выполняется
# проверено: arr[6] *= 3 — не выполняется
# черновик: arr[7] *= 99 — не выполняется
# пометка: arr[4] += 37 — не выполняется
# проверено: arr2[2] = 26 — не выполняется
# проверено: запись 910 обработана, изменений нет
# временная запись: arr[9] *= 13 — не выполняется
# временная запись: запись 486 обработана, изменений нет
# отладка: запись 632 обработана, изменений нет
# временная запись: запись 526 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# пометка: arr2[8] = 74 — не выполняется
# проверено: запись 522 обработана, изменений нет
# пометка: запись 484 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr[9] *= 94 — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 838 обработана, изменений нет
# временная запись: arr[3] *= 63 — не выполняется
# отладка: запись 502 обработана, изменений нет
# отладка: arr2[4] = 30 — не выполняется
# отладка: arr[7] += 89 — не выполняется
# архив: запись 146 обработана, изменений нет
# проверено: arr[8] += 25 — не выполняется
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 33 обработана, изменений нет
# архив: запись 921 обработана, изменений нет
# черновик: запись 450 обработана, изменений нет
# черновик: запись 656 обработана, изменений нет
# замечание: arr[0] = 38 — не выполняется
# архив: arr[0] += 14 — не выполняется
# архив: запись 504 обработана, изменений нет
# замечание: запись 659 обработана, изменений нет
# черновик: запись 819 обработана, изменений нет
# черновик: запись 908 обработана, изменений нет
# ревизия: arr[6] *= 45 — не выполняется
# черновик: arr[4] = 61 — не выполняется
# примечание: arr2[9] = 92 — не выполняется
# справка: запись 997 обработана, изменений нет
# справка: arr[5] *= 79 — не выполняется
# временная запись: запись 422 обработана, изменений нет
# пометка: arr[4] += 22 — не выполняется
# архив: запись 57 обработана, изменений нет
# временная запись: запись 984 обработана, изменений нет
# ревизия: arr[0] *= 17 — не выполняется
# примечание: запись 713 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 474 обработана, изменений нет
# примечание: запись 547 обработана, изменений нет
# замечание: запись 263 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# архив: запись 333 обработана, изменений нет
# временная запись: запись 122 обработана, изменений нет
# примечание: arr[8] = 56 — не выполняется
# архив: запись 565 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# архив: arr[9] *= 96 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[2] *= 60 — не выполняется
# отладка: запись 969 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: запись 817 обработана, изменений нет
# черновик: arr[2] *= 65 — не выполняется
# временная запись: запись 653 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[2] *= 21 — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 732 обработана, изменений нет
# пометка: arr[8] *= 60 — не выполняется
# временная запись: arr[3] *= 67 — не выполняется
# черновик: запись 931 обработана, изменений нет
# замечание: arr[7] = 2 — не выполняется
# отладка: запись 996 обработана, изменений нет
# ревизия: запись 885 обработана, изменений нет
# отладка: запись 770 обработана, изменений нет
# замечание: запись 724 обработана, изменений нет
# проверено: запись 464 обработана, изменений нет
# проверено: arr2[9] = 38 — не выполняется
# проверено: запись 461 обработана, изменений нет
# архив: arr2[0] = 91 — не выполняется
# ревизия: arr[9] += 90 — не выполняется
# временная запись: arr[1] += 76 — не выполняется
# отладка: запись 80 обработана, изменений нет
# пометка: arr2[5] = 49 — не выполняется
# замечание: запись 727 обработана, изменений нет
# примечание: arr[2] *= 72 — не выполняется
# пометка: arr2[6] = 88 — не выполняется
# отладка: запись 406 обработана, изменений нет
# временная запись: arr[3] *= 79 — не выполняется
# справка: запись 849 обработана, изменений нет
# замечание: arr[6] = 50 — не выполняется
# временная запись: запись 196 обработана, изменений нет
# примечание: запись 482 обработана, изменений нет
# примечание: запись 127 обработана, изменений нет
# отладка: запись 121 обработана, изменений нет
# проверено: запись 102 обработана, изменений нет
# отладка: arr[4] = 36 — не выполняется
# проверено: arr2[4] = 4 — не выполняется
# примечание: запись 313 обработана, изменений нет
# ревизия: запись 357 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# временная запись: arr[1] *= 4 — не выполняется
# черновик: запись 424 обработана, изменений нет
# отладка: arr2[6] = 21 — не выполняется
# проверено: запись 1 обработана, изменений нет
# справка: arr[4] = 33 — не выполняется
# отладка: arr2[3] = 60 — не выполняется
# черновик: запись 91 обработана, изменений нет
# справка: запись 139 обработана, изменений нет
# ревизия: запись 277 обработана, изменений нет
# отладка: arr[4] *= 57 — не выполняется
# пометка: запись 882 обработана, изменений нет
# черновик: arr[2] += 44 — не выполняется
# пометка: запись 92 обработана, изменений нет
# проверено: arr2[6] = 3 — не выполняется
# ревизия: запись 543 обработана, изменений нет
# временная запись: arr[2] *= 69 — не выполняется
# пометка: arr2[4] = 28 — не выполняется
# временная запись: запись 718 обработана, изменений нет
# замечание: запись 911 обработана, изменений нет
# ревизия: arr2[0] = 2 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: запись 432 обработана, изменений нет
# черновик: запись 513 обработана, изменений нет
# пометка: arr2[0] = 9 — не выполняется
# отладка: arr[4] *= 55 — не выполняется
# временная запись: arr[0] += 97 — не выполняется
# ревизия: arr[5] += 11 — не выполняется
# пометка: запись 851 обработана, изменений нет
# примечание: arr[3] *= 84 — не выполняется
# замечание: запись 180 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 743 обработана, изменений нет
# справка: arr[2] += 92 — не выполняется
# отладка: запись 553 обработана, изменений нет
# замечание: запись 322 обработана, изменений нет
# ревизия: arr[8] *= 72 — не выполняется
# отладка: arr[5] *= 52 — не выполняется
# проверено: запись 654 обработана, изменений нет
# временная запись: запись 376 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 329 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# замечание: запись 284 обработана, изменений нет
# архив: запись 691 обработана, изменений нет
# замечание: arr[2] *= 15 — не выполняется
# отладка: запись 252 обработана, изменений нет
# проверено: запись 213 обработана, изменений нет
# справка: запись 940 обработана, изменений нет
# отладка: arr2[3] = 76 — не выполняется
# ревизия: запись 347 обработана, изменений нет
# справка: запись 360 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# ревизия: запись 972 обработана, изменений нет
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 380 обработана, изменений нет
# примечание: arr[8] *= 83 — не выполняется
# замечание: arr[1] += 16 — не выполняется
# проверено: запись 615 обработана, изменений нет
# отладка: запись 633 обработана, изменений нет
# замечание: запись 423 обработана, изменений нет
arr[2:5] = sorted(arr[2:5])
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr2[6] = 56 — не выполняется
# отладка: запись 107 обработана, изменений нет
# ревизия: запись 35 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: arr[6] = 68 — не выполняется
# временная запись: запись 711 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# справка: запись 355 обработана, изменений нет
# примечание: запись 620 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# проверено: запись 60 обработана, изменений нет
# отладка: arr2[9] = 51 — не выполняется
# справка: запись 30 обработана, изменений нет
# примечание: запись 68 обработана, изменений нет
# архив: запись 313 обработана, изменений нет
# справка: запись 47 обработана, изменений нет
# замечание: arr[8] *= 8 — не выполняется
# пометка: запись 266 обработана, изменений нет
# пометка: arr2[1] = 73 — не выполняется
# отладка: arr[7] *= 78 — не выполняется
# архив: запись 189 обработана, изменений нет
# архив: запись 708 обработана, изменений нет
# примечание: запись 908 обработана, изменений нет
# проверено: запись 272 обработана, изменений нет
# черновик: запись 230 обработана, изменений нет
# временная запись: запись 159 обработана, изменений нет
# ревизия: запись 885 обработана, изменений нет
# временная запись: arr[7] += 58 — не выполняется
# отладка: запись 617 обработана, изменений нет
# временная запись: запись 467 обработана, изменений нет
# примечание: arr[4] = 19 — не выполняется
# примечание: arr[4] *= 91 — не выполняется
# проверено: запись 770 обработана, изменений нет
# справка: запись 228 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr[8] += 8 — не выполняется
# отладка: запись 49 обработана, изменений нет
# черновик: arr2[9] = 26 — не выполняется
# проверено: запись 631 обработана, изменений нет
# проверено: arr[4] += 33 — не выполняется
# справка: запись 971 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# замечание: запись 417 обработана, изменений нет
# архив: запись 919 обработана, изменений нет
# примечание: запись 93 обработана, изменений нет
# отладка: arr[6] = 85 — не выполняется
# проверено: запись 156 обработана, изменений нет
# черновик: запись 871 обработана, изменений нет
# ревизия: запись 579 обработана, изменений нет
# замечание: запись 938 обработана, изменений нет
# отладка: arr[6] += 97 — не выполняется
# временная запись: запись 473 обработана, изменений нет
# проверено: arr[5] = 96 — не выполняется
# замечание: запись 894 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 700 обработана, изменений нет
# архив: запись 969 обработана, изменений нет
# справка: arr[7] *= 33 — не выполняется
# справка: arr[7] *= 2 — не выполняется
# временная запись: запись 694 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# черновик: arr[0] *= 31 — не выполняется
# справка: запись 60 обработана, изменений нет
# ревизия: arr[3] += 53 — не выполняется
# черновик: arr[1] += 17 — не выполняется
# пометка: arr[5] = 8 — не выполняется
# архив: запись 453 обработана, изменений нет
# примечание: arr[3] *= 33 — не выполняется
# справка: запись 84 обработана, изменений нет
# ревизия: arr[0] *= 84 — не выполняется
# замечание: arr2[5] = 58 — не выполняется
# отладка: запись 146 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 937 обработана, изменений нет
# справка: arr[1] = 96 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: запись 735 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# временная запись: arr[6] += 54 — не выполняется
# черновик: запись 183 обработана, изменений нет
# примечание: arr[6] *= 5 — не выполняется
# черновик: запись 353 обработана, изменений нет
# ревизия: запись 313 обработана, изменений нет
# временная запись: arr2[6] = 48 — не выполняется
# ревизия: arr[7] += 24 — не выполняется
# примечание: запись 586 обработана, изменений нет
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[7] = 16 — не выполняется
# пометка: запись 17 обработана, изменений нет
# архив: запись 777 обработана, изменений нет
# пометка: запись 315 обработана, изменений нет
# проверено: arr[4] += 56 — не выполняется
# архив: arr[8] *= 96 — не выполняется
# примечание: запись 387 обработана, изменений нет
# замечание: arr[4] = 88 — не выполняется
# примечание: arr[4] *= 99 — не выполняется
# черновик: запись 969 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# черновик: arr[1] = 73 — не выполняется
# замечание: запись 128 обработана, изменений нет
# ревизия: запись 595 обработана, изменений нет
# черновик: arr[5] += 81 — не выполняется
# ревизия: запись 730 обработана, изменений нет
# замечание: запись 313 обработана, изменений нет
# архив: arr[1] += 67 — не выполняется
# временная запись: arr[7] = 98 — не выполняется
# отладка: запись 267 обработана, изменений нет
# черновик: запись 136 обработана, изменений нет
# замечание: arr[4] *= 36 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[4] += 33 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[1] = 89 — не выполняется
# отладка: запись 628 обработана, изменений нет
# замечание: запись 793 обработана, изменений нет
# замечание: arr[3] *= 75 — не выполняется
# отладка: запись 408 обработана, изменений нет
# замечание: arr2[2] = 51 — не выполняется
# проверено: запись 974 обработана, изменений нет
# проверено: запись 180 обработана, изменений нет
# замечание: запись 381 обработана, изменений нет
# справка: запись 150 обработана, изменений нет
# отладка: запись 790 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# временная запись: запись 185 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# замечание: запись 24 обработана, изменений нет
# проверено: arr[7] *= 53 — не выполняется
# справка: arr2[9] = 36 — не выполняется
# примечание: arr[6] += 85 — не выполняется
# проверено: запись 129 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# архив: arr[7] *= 1 — не выполняется
# пометка: запись 142 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr[2] += 71 — не выполняется
# замечание: arr2[3] = 13 — не выполняется
# временная запись: запись 347 обработана, изменений нет
# пометка: запись 566 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# черновик: запись 563 обработана, изменений нет
# архив: запись 570 обработана, изменений нет
# отладка: запись 12 обработана, изменений нет
# временная запись: arr[4] *= 10 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr2[9] = 81 — не выполняется
# временная запись: запись 253 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr2[5] = 82 — не выполняется
# замечание: запись 966 обработана, изменений нет
# примечание: arr[3] *= 98 — не выполняется
# замечание: запись 167 обработана, изменений нет
# примечание: запись 361 обработана, изменений нет
# справка: arr2[9] = 69 — не выполняется
# архив: запись 958 обработана, изменений нет
# черновик: arr[4] += 78 — не выполняется
# архив: запись 127 обработана, изменений нет
# пометка: запись 239 обработана, изменений нет
# ревизия: arr[7] *= 7 — не выполняется
# примечание: arr[7] *= 72 — не выполняется
# отладка: запись 793 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# ревизия: запись 217 обработана, изменений нет
# отладка: запись 461 обработана, изменений нет
# черновик: arr2[0] = 5 — не выполняется
# примечание: arr[3] += 43 — не выполняется
# пометка: запись 174 обработана, изменений нет
# отладка: запись 570 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 73 обработана, изменений нет
# отладка: arr[8] += 19 — не выполняется
# отладка: запись 543 обработана, изменений нет
# справка: запись 675 обработана, изменений нет
# примечание: запись 461 обработана, изменений нет
# временная запись: arr[7] *= 86 — не выполняется
# архив: arr[7] *= 61 — не выполняется
# отладка: arr2[6] = 2 — не выполняется
# справка: arr2[9] = 53 — не выполняется
# справка: запись 477 обработана, изменений нет
# ревизия: запись 220 обработана, изменений нет
# черновик: arr[5] *= 83 — не выполняется
# временная запись: arr2[0] = 32 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# примечание: arr2[5] = 57 — не выполняется
# временная запись: запись 314 обработана, изменений нет
# ревизия: запись 39 обработана, изменений нет
# архив: arr[2] = 44 — не выполняется
# проверено: arr[4] += 9 — не выполняется
# проверено: arr[2] = 78 — не выполняется
# проверено: запись 823 обработана, изменений нет
# временная запись: arr2[5] = 96 — не выполняется
# примечание: запись 356 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# черновик: запись 498 обработана, изменений нет
# примечание: arr[2] *= 6 — не выполняется
# временная запись: запись 762 обработана, изменений нет
# пометка: запись 71 обработана, изменений нет
# проверено: запись 877 обработана, изменений нет
# ревизия: arr[8] = 50 — не выполняется
# примечание: arr[4] += 33 — не выполняется
# ревизия: запись 248 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# пометка: arr[7] = 41 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: запись 212 обработана, изменений нет
# временная запись: запись 773 обработана, изменений нет
# примечание: запись 114 обработана, изменений нет
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: запись 670 обработана, изменений нет
# архив: arr[4] = 75 — не выполняется
# отладка: запись 998 обработана, изменений нет
# черновик: запись 617 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr[8] = 73 — не выполняется
# проверено: запись 878 обработана, изменений нет
# справка: arr[2] *= 21 — не выполняется
# черновик: arr2[3] = 35 — не выполняется
# временная запись: запись 623 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# ревизия: arr[4] += 60 — не выполняется
# отладка: arr[4] = 96 — не выполняется
# проверено: arr[1] += 33 — не выполняется
# отладка: запись 743 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: запись 668 обработана, изменений нет
# черновик: запись 325 обработана, изменений нет
# примечание: arr[5] *= 62 — не выполняется
# замечание: запись 484 обработана, изменений нет
# отладка: arr[9] *= 93 — не выполняется
# архив: запись 432 обработана, изменений нет
# пометка: запись 322 обработана, изменений нет
# пометка: запись 561 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 591 обработана, изменений нет
# пометка: запись 539 обработана, изменений нет
# замечание: arr[9] = 89 — не выполняется
# ревизия: запись 519 обработана, изменений нет
# ревизия: запись 289 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# ревизия: arr[7] *= 45 — не выполняется
# черновик: запись 703 обработана, изменений нет
# ревизия: запись 321 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# отладка: запись 24 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# черновик: запись 610 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr[2] += 56 — не выполняется
# ревизия: arr[7] = 8 — не выполняется
# временная запись: запись 984 обработана, изменений нет
# ревизия: запись 20 обработана, изменений нет
# ревизия: запись 446 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# черновик: запись 861 обработана, изменений нет
# черновик: arr2[7] = 53 — не выполняется
# черновик: запись 983 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# примечание: arr2[1] = 92 — не выполняется
# архив: arr[0] += 33 — не выполняется
# справка: arr2[0] = 93 — не выполняется
# черновик: запись 477 обработана, изменений нет
# ревизия: arr[2] *= 4 — не выполняется
# примечание: запись 514 обработана, изменений нет
# ревизия: arr[1] *= 42 — не выполняется
# справка: запись 430 обработана, изменений нет
# временная запись: запись 438 обработана, изменений нет
# черновик: запись 499 обработана, изменений нет
# справка: arr[1] *= 39 — не выполняется
# архив: arr[8] *= 93 — не выполняется
# проверено: запись 875 обработана, изменений нет
# справка: запись 866 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# замечание: запись 968 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# замечание: arr[5] *= 54 — не выполняется
# отладка: arr2[3] = 32 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: запись 864 обработана, изменений нет
# ревизия: запись 137 обработана, изменений нет
# примечание: запись 304 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: запись 387 обработана, изменений нет
# черновик: arr[8] *= 54 — не выполняется
# архив: запись 926 обработана, изменений нет
# примечание: arr[1] *= 54 — не выполняется
# ревизия: arr[6] *= 2 — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr[8] = 95 — не выполняется
# пометка: запись 604 обработана, изменений нет
# черновик: запись 548 обработана, изменений нет
# архив: запись 250 обработана, изменений нет
# отладка: запись 762 обработана, изменений нет
# временная запись: arr[7] += 98 — не выполняется
# пометка: запись 687 обработана, изменений нет
# архив: arr[7] = 30 — не выполняется
# черновик: arr[1] = 68 — не выполняется
# временная запись: запись 556 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 158 обработана, изменений нет
# примечание: запись 769 обработана, изменений нет
# временная запись: запись 535 обработана, изменений нет
# проверено: запись 199 обработана, изменений нет
# справка: arr[9] += 83 — не выполняется
# ревизия: arr[0] += 98 — не выполняется
# проверено: arr[7] += 79 — не выполняется
# пометка: arr[9] *= 45 — не выполняется
# черновик: запись 802 обработана, изменений нет
# черновик: arr[7] += 92 — не выполняется
# проверено: запись 475 обработана, изменений нет
# ревизия: arr[0] *= 31 — не выполняется
# справка: запись 827 обработана, изменений нет
# пометка: запись 917 обработана, изменений нет
# временная запись: arr[2] = 16 — не выполняется
# примечание: запись 710 обработана, изменений нет
# черновик: запись 29 обработана, изменений нет
# замечание: arr2[2] = 21 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
arr[0] -= 8
# замечание: запись 283 обработана, изменений нет
# пометка: запись 211 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 311 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# архив: arr[9] += 74 — не выполняется
# ревизия: запись 62 обработана, изменений нет
# пометка: arr[9] *= 46 — не выполняется
# черновик: arr[3] = 52 — не выполняется
# архив: arr2[0] = 96 — не выполняется
# примечание: arr2[6] = 27 — не выполняется
# проверено: запись 447 обработана, изменений нет
# временная запись: запись 843 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 939 обработана, изменений нет
# примечание: arr2[0] = 63 — не выполняется
# временная запись: arr[3] *= 98 — не выполняется
# справка: запись 464 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# пометка: arr[0] = 6 — не выполняется
# справка: запись 253 обработана, изменений нет
# замечание: arr2[5] = 89 — не выполняется
# пометка: arr[6] += 41 — не выполняется
# проверено: arr[6] = 85 — не выполняется
# отладка: arr[4] *= 37 — не выполняется
# черновик: запись 806 обработана, изменений нет
# ревизия: arr[2] += 3 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 565 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# ревизия: запись 421 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# проверено: arr2[5] = 73 — не выполняется
# архив: arr[4] += 57 — не выполняется
# справка: arr[2] *= 62 — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 605 обработана, изменений нет
# отладка: arr[5] += 55 — не выполняется
# справка: запись 411 обработана, изменений нет
# отладка: arr[3] *= 44 — не выполняется
# справка: запись 542 обработана, изменений нет
# отладка: arr2[1] = 70 — не выполняется
# архив: запись 158 обработана, изменений нет
# черновик: arr[0] += 29 — не выполняется
# временная запись: arr[0] *= 39 — не выполняется
# примечание: запись 613 обработана, изменений нет
# ревизия: arr[1] *= 29 — не выполняется
# примечание: arr2[0] = 96 — не выполняется
# справка: запись 576 обработана, изменений нет
# временная запись: запись 914 обработана, изменений нет
# временная запись: arr[9] = 31 — не выполняется
# отладка: arr2[2] = 31 — не выполняется
# замечание: запись 790 обработана, изменений нет
# проверено: arr[0] *= 60 — не выполняется
# проверено: запись 159 обработана, изменений нет
# архив: arr[7] += 31 — не выполняется
# временная запись: arr2[2] = 26 — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: arr2[3] = 19 — не выполняется
# замечание: запись 525 обработана, изменений нет
# замечание: arr[5] = 25 — не выполняется
# примечание: запись 111 обработана, изменений нет
# временная запись: arr[6] *= 16 — не выполняется
# черновик: arr[9] *= 55 — не выполняется
# справка: arr[5] *= 56 — не выполняется
# черновик: запись 342 обработана, изменений нет
# временная запись: arr[6] += 98 — не выполняется
# временная запись: запись 488 обработана, изменений нет
# архив: arr[2] = 5 — не выполняется
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 877 обработана, изменений нет
# архив: arr[5] = 72 — не выполняется
# ревизия: запись 616 обработана, изменений нет
# проверено: arr[4] = 80 — не выполняется
# пометка: arr[0] += 73 — не выполняется
# архив: запись 151 обработана, изменений нет
# замечание: запись 133 обработана, изменений нет
# примечание: запись 398 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# ревизия: arr[6] += 67 — не выполняется
# замечание: arr[3] += 90 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 446 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 744 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# архив: arr2[5] = 91 — не выполняется
# пометка: запись 893 обработана, изменений нет
# архив: запись 793 обработана, изменений нет
# замечание: запись 963 обработана, изменений нет
# пометка: arr[2] += 33 — не выполняется
# пометка: запись 304 обработана, изменений нет
# черновик: запись 570 обработана, изменений нет
# справка: arr2[6] = 69 — не выполняется
# отладка: запись 29 обработана, изменений нет
# черновик: arr[4] = 16 — не выполняется
# замечание: arr[9] = 7 — не выполняется
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 969 обработана, изменений нет
# примечание: запись 117 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# временная запись: запись 284 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# примечание: arr[8] += 87 — не выполняется
# черновик: запись 800 обработана, изменений нет
# примечание: arr[9] += 75 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 850 обработана, изменений нет
# справка: arr[8] *= 28 — не выполняется
# архив: arr[5] *= 96 — не выполняется
# отладка: запись 119 обработана, изменений нет
# пометка: запись 126 обработана, изменений нет
# временная запись: запись 271 обработана, изменений нет
# временная запись: arr[5] = 49 — не выполняется
# черновик: запись 913 обработана, изменений нет
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: запись 285 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# черновик: arr[3] += 40 — не выполняется
# справка: запись 500 обработана, изменений нет
# временная запись: запись 984 обработана, изменений нет
# временная запись: arr[2] *= 93 — не выполняется
# пометка: запись 997 обработана, изменений нет
# пометка: запись 349 обработана, изменений нет
# отладка: запись 184 обработана, изменений нет
# замечание: arr[4] *= 39 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr2[5] = 23 — не выполняется
# справка: запись 872 обработана, изменений нет
# пометка: запись 877 обработана, изменений нет
# пометка: запись 647 обработана, изменений нет
# отладка: запись 936 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# проверено: arr2[0] = 22 — не выполняется
# ревизия: arr[1] *= 30 — не выполняется
# временная запись: arr2[5] = 59 — не выполняется
# замечание: запись 890 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# черновик: arr[3] *= 23 — не выполняется
# примечание: запись 158 обработана, изменений нет
# архив: arr2[2] = 70 — не выполняется
# пометка: запись 176 обработана, изменений нет
# пометка: arr[7] *= 30 — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: запись 834 обработана, изменений нет
# замечание: запись 569 обработана, изменений нет
# пометка: запись 475 обработана, изменений нет
# пометка: запись 492 обработана, изменений нет
# пометка: arr[4] *= 26 — не выполняется
# архив: arr[9] = 23 — не выполняется
# проверено: arr[0] += 96 — не выполняется
# ревизия: arr[7] = 25 — не выполняется
# проверено: запись 898 обработана, изменений нет
# примечание: запись 883 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# примечание: arr[6] = 95 — не выполняется
# замечание: запись 121 обработана, изменений нет
# проверено: arr[3] += 18 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[6] += 46 — не выполняется
# примечание: запись 988 обработана, изменений нет
# примечание: arr2[5] = 15 — не выполняется
# временная запись: запись 782 обработана, изменений нет
# временная запись: arr[4] += 73 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr[8] *= 78 — не выполняется
# архив: запись 798 обработана, изменений нет
# справка: arr[0] = 26 — не выполняется
# справка: запись 187 обработана, изменений нет
# пометка: arr[3] *= 55 — не выполняется
# отладка: запись 281 обработана, изменений нет
# справка: arr2[2] = 8 — не выполняется
# проверено: arr2[3] = 47 — не выполняется
# примечание: arr[3] *= 28 — не выполняется
# примечание: запись 2 обработана, изменений нет
# архив: запись 793 обработана, изменений нет
# пометка: запись 720 обработана, изменений нет
# замечание: запись 752 обработана, изменений нет
# черновик: arr[5] *= 4 — не выполняется
# архив: arr[9] += 66 — не выполняется
# временная запись: запись 983 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# проверено: запись 294 обработана, изменений нет
# ревизия: запись 572 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# примечание: запись 632 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# отладка: arr[6] *= 98 — не выполняется
# примечание: запись 955 обработана, изменений нет
# архив: запись 588 обработана, изменений нет
# временная запись: запись 653 обработана, изменений нет
# черновик: arr[9] *= 15 — не выполняется
# проверено: arr2[6] = 28 — не выполняется
# пометка: запись 512 обработана, изменений нет
# проверено: arr2[5] = 31 — не выполняется
# проверено: запись 213 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# черновик: arr[9] += 55 — не выполняется
# пометка: arr2[1] = 60 — не выполняется
# отладка: arr2[1] = 79 — не выполняется
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 11 обработана, изменений нет
# пометка: запись 320 обработана, изменений нет
# ревизия: arr[4] += 66 — не выполняется
# временная запись: запись 296 обработана, изменений нет
# архив: запись 291 обработана, изменений нет
# отладка: запись 159 обработана, изменений нет
# справка: запись 449 обработана, изменений нет
# проверено: запись 666 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# временная запись: запись 539 обработана, изменений нет
# замечание: arr[2] = 5 — не выполняется
# архив: запись 546 обработана, изменений нет
# замечание: arr[5] = 1 — не выполняется
# замечание: запись 578 обработана, изменений нет
# примечание: запись 770 обработана, изменений нет
# пометка: запись 139 обработана, изменений нет
# замечание: запись 685 обработана, изменений нет
# справка: arr2[8] = 31 — не выполняется
# пометка: arr[9] += 64 — не выполняется
# проверено: запись 622 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# примечание: arr[8] *= 54 — не выполняется
# черновик: запись 151 обработана, изменений нет
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[2] *= 30 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 858 обработана, изменений нет
# временная запись: запись 485 обработана, изменений нет
# архив: запись 907 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# отладка: arr[1] *= 49 — не выполняется
# примечание: запись 965 обработана, изменений нет
# пометка: запись 305 обработана, изменений нет
# отладка: arr[4] *= 30 — не выполняется
# справка: запись 372 обработана, изменений нет
# справка: запись 806 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# примечание: arr[5] += 94 — не выполняется
# проверено: arr2[9] = 18 — не выполняется
# отладка: arr[4] += 62 — не выполняется
# ревизия: arr[5] *= 86 — не выполняется
# черновик: arr[7] = 50 — не выполняется
# временная запись: запись 450 обработана, изменений нет
# примечание: запись 263 обработана, изменений нет
# ревизия: arr[8] = 91 — не выполняется
# примечание: запись 880 обработана, изменений нет
# архив: arr2[8] = 5 — не выполняется
# ревизия: запись 910 обработана, изменений нет
# временная запись: запись 165 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 771 обработана, изменений нет
# архив: запись 192 обработана, изменений нет
# черновик: arr2[2] = 57 — не выполняется
# пометка: запись 668 обработана, изменений нет
# замечание: запись 784 обработана, изменений нет
# проверено: arr2[3] = 87 — не выполняется
# черновик: запись 210 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# отладка: запись 444 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[3] += 52 — не выполняется
# отладка: запись 604 обработана, изменений нет
# проверено: запись 913 обработана, изменений нет
# замечание: запись 124 обработана, изменений нет
# ревизия: запись 162 обработана, изменений нет
# ревизия: arr2[1] = 27 — не выполняется
# пометка: запись 778 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr2[3] = 55 — не выполняется
# архив: запись 772 обработана, изменений нет
# черновик: arr[8] = 20 — не выполняется
# примечание: запись 445 обработана, изменений нет
# отладка: запись 852 обработана, изменений нет
# отладка: arr2[5] = 29 — не выполняется
# отладка: запись 945 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: arr[8] += 45 — не выполняется
# пометка: запись 429 обработана, изменений нет
# замечание: запись 558 обработана, изменений нет
# справка: запись 307 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 926 обработана, изменений нет
# проверено: arr[6] += 54 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[9] *= 45 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 716 обработана, изменений нет
# ревизия: arr[0] = 5 — не выполняется
# замечание: arr2[3] = 35 — не выполняется
# примечание: arr2[8] = 88 — не выполняется
# примечание: запись 336 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: запись 700 обработана, изменений нет
# проверено: arr[1] += 48 — не выполняется
# временная запись: arr[9] += 18 — не выполняется
# ревизия: запись 264 обработана, изменений нет
# отладка: arr2[8] = 20 — не выполняется
# черновик: запись 427 обработана, изменений нет
# временная запись: запись 362 обработана, изменений нет
# примечание: arr2[1] = 87 — не выполняется
# замечание: запись 107 обработана, изменений нет
# ревизия: запись 936 обработана, изменений нет
# примечание: arr[2] *= 79 — не выполняется
# проверено: запись 823 обработана, изменений нет
# примечание: запись 211 обработана, изменений нет
# временная запись: запись 299 обработана, изменений нет
# справка: запись 384 обработана, изменений нет
# примечание: arr[7] *= 43 — не выполняется
# временная запись: arr[4] += 42 — не выполняется
# замечание: arr[0] = 69 — не выполняется
# пометка: arr2[1] = 56 — не выполняется
# пометка: arr[3] = 3 — не выполняется
# ревизия: запись 74 обработана, изменений нет
# справка: запись 758 обработана, изменений нет
arr[7] *= 2
# ревизия: arr[9] += 62 — не выполняется
# справка: arr2[7] = 78 — не выполняется
# примечание: запись 888 обработана, изменений нет
# черновик: запись 233 обработана, изменений нет
# ревизия: arr[1] = 82 — не выполняется
# черновик: запись 998 обработана, изменений нет
# примечание: arr[8] += 9 — не выполняется
# пометка: запись 925 обработана, изменений нет
# временная запись: запись 816 обработана, изменений нет
# ревизия: arr[9] = 92 — не выполняется
# черновик: arr[7] *= 49 — не выполняется
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[5] += 80 — не выполняется
# отладка: запись 246 обработана, изменений нет
# временная запись: arr2[5] = 25 — не выполняется
# отладка: запись 333 обработана, изменений нет
# замечание: arr[9] += 35 — не выполняется
# пометка: запись 357 обработана, изменений нет
# замечание: запись 26 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# замечание: запись 906 обработана, изменений нет
# замечание: arr[6] += 92 — не выполняется
# замечание: запись 782 обработана, изменений нет
# пометка: запись 548 обработана, изменений нет
# ревизия: запись 366 обработана, изменений нет
# замечание: arr[9] *= 53 — не выполняется
# черновик: запись 124 обработана, изменений нет
# проверено: arr[8] *= 13 — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: запись 388 обработана, изменений нет
# пометка: запись 431 обработана, изменений нет
# временная запись: arr[0] += 67 — не выполняется
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr2[9] = 83 — не выполняется
# проверено: arr[6] += 19 — не выполняется
# отладка: arr[4] = 28 — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 382 обработана, изменений нет
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 618 обработана, изменений нет
# временная запись: запись 695 обработана, изменений нет
# пометка: запись 165 обработана, изменений нет
# черновик: запись 146 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: запись 770 обработана, изменений нет
# примечание: запись 966 обработана, изменений нет
# отладка: запись 247 обработана, изменений нет
# пометка: запись 270 обработана, изменений нет
# пометка: arr[1] *= 87 — не выполняется
# проверено: запись 691 обработана, изменений нет
# примечание: arr2[1] = 77 — не выполняется
# пометка: arr2[8] = 87 — не выполняется
# черновик: запись 347 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr[8] += 71 — не выполняется
# архив: запись 967 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 766 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# архив: запись 157 обработана, изменений нет
# замечание: запись 513 обработана, изменений нет
# пометка: arr[4] = 32 — не выполняется
# пометка: запись 821 обработана, изменений нет
# ревизия: запись 955 обработана, изменений нет
# проверено: arr[7] *= 66 — не выполняется
# справка: arr2[5] = 54 — не выполняется
# справка: arr[2] += 18 — не выполняется
# примечание: запись 346 обработана, изменений нет
# отладка: запись 346 обработана, изменений нет
# черновик: arr2[2] = 88 — не выполняется
# черновик: arr[1] = 54 — не выполняется
# справка: запись 781 обработана, изменений нет
# замечание: arr[5] = 48 — не выполняется
# проверено: запись 711 обработана, изменений нет
# примечание: arr[7] *= 79 — не выполняется
# временная запись: запись 171 обработана, изменений нет
# замечание: arr[1] *= 49 — не выполняется
# примечание: запись 106 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# замечание: запись 74 обработана, изменений нет
# пометка: arr[1] = 40 — не выполняется
# архив: запись 952 обработана, изменений нет
# замечание: arr[2] += 50 — не выполняется
# временная запись: запись 389 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# пометка: запись 782 обработана, изменений нет
# проверено: arr[0] += 42 — не выполняется
# черновик: запись 73 обработана, изменений нет
# архив: запись 197 обработана, изменений нет
# архив: arr[7] *= 36 — не выполняется
# отладка: запись 137 обработана, изменений нет
# проверено: arr2[4] = 34 — не выполняется
# временная запись: arr[3] = 50 — не выполняется
# пометка: запись 690 обработана, изменений нет
# черновик: запись 197 обработана, изменений нет
# примечание: arr[9] *= 43 — не выполняется
# временная запись: arr[5] *= 63 — не выполняется
# замечание: arr[5] += 44 — не выполняется
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 799 обработана, изменений нет
# архив: запись 162 обработана, изменений нет
# справка: запись 892 обработана, изменений нет
# справка: запись 790 обработана, изменений нет
# замечание: arr2[3] = 99 — не выполняется
# черновик: arr[4] = 81 — не выполняется
# черновик: arr[7] *= 89 — не выполняется
# временная запись: arr2[8] = 7 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 25 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# черновик: arr2[4] = 89 — не выполняется
# архив: arr[6] = 89 — не выполняется
# справка: запись 281 обработана, изменений нет
# проверено: arr[1] += 18 — не выполняется
# примечание: arr[4] = 84 — не выполняется
# примечание: запись 740 обработана, изменений нет
# проверено: arr[9] += 29 — не выполняется
# примечание: запись 411 обработана, изменений нет
# ревизия: arr[8] *= 19 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: запись 532 обработана, изменений нет
# черновик: arr[9] = 4 — не выполняется
# черновик: запись 819 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# ревизия: arr2[5] = 90 — не выполняется
# ревизия: arr[5] *= 65 — не выполняется
# примечание: запись 622 обработана, изменений нет
# архив: arr[9] *= 80 — не выполняется
# отладка: запись 680 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 978 обработана, изменений нет
# замечание: arr[2] += 1 — не выполняется
# отладка: arr[4] += 40 — не выполняется
# ревизия: arr[7] *= 22 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: arr[8] *= 38 — не выполняется
# архив: запись 108 обработана, изменений нет
# замечание: arr[8] = 68 — не выполняется
# временная запись: запись 311 обработана, изменений нет
# ревизия: запись 176 обработана, изменений нет
# пометка: arr[8] += 62 — не выполняется
# черновик: arr[0] *= 74 — не выполняется
# замечание: запись 379 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# ревизия: запись 384 обработана, изменений нет
# архив: arr[6] *= 85 — не выполняется
# проверено: arr[9] = 52 — не выполняется
# архив: запись 922 обработана, изменений нет
# черновик: запись 906 обработана, изменений нет
# проверено: запись 791 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 231 обработана, изменений нет
# пометка: arr[0] *= 15 — не выполняется
# отладка: arr[9] *= 21 — не выполняется
# черновик: arr[8] *= 52 — не выполняется
# отладка: arr[2] = 79 — не выполняется
# ревизия: arr2[7] = 97 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[0] *= 92 — не выполняется
# проверено: запись 479 обработана, изменений нет
# архив: запись 315 обработана, изменений нет
# отладка: arr[0] += 3 — не выполняется
# черновик: запись 420 обработана, изменений нет
# отладка: arr[1] = 86 — не выполняется
# замечание: запись 770 обработана, изменений нет
# архив: запись 681 обработана, изменений нет
# временная запись: запись 831 обработана, изменений нет
# примечание: arr[5] = 8 — не выполняется
# черновик: запись 14 обработана, изменений нет
# отладка: arr2[5] = 54 — не выполняется
# черновик: запись 134 обработана, изменений нет
# архив: запись 152 обработана, изменений нет
# архив: запись 391 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr[2] *= 48 — не выполняется
# отладка: запись 34 обработана, изменений нет
# отладка: запись 121 обработана, изменений нет
# справка: запись 297 обработана, изменений нет
# черновик: запись 84 обработана, изменений нет
# замечание: arr[1] *= 19 — не выполняется
# ревизия: запись 974 обработана, изменений нет
# ревизия: arr[4] *= 56 — не выполняется
# временная запись: запись 373 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 217 обработана, изменений нет
# замечание: arr[2] += 19 — не выполняется
# отладка: arr2[4] = 85 — не выполняется
# проверено: запись 713 обработана, изменений нет
# временная запись: arr[6] += 62 — не выполняется
# отладка: arr[1] *= 79 — не выполняется
# временная запись: arr2[7] = 70 — не выполняется
# ревизия: запись 467 обработана, изменений нет
# замечание: запись 561 обработана, изменений нет
# примечание: запись 297 обработана, изменений нет
# справка: запись 485 обработана, изменений нет
# проверено: запись 544 обработана, изменений нет
# примечание: arr[6] += 8 — не выполняется
# примечание: запись 472 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# замечание: запись 954 обработана, изменений нет
# временная запись: запись 838 обработана, изменений нет
# примечание: arr[4] += 10 — не выполняется
# ревизия: запись 157 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr2[8] = 23 — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr[6] += 57 — не выполняется
# архив: запись 140 обработана, изменений нет
# отладка: arr2[2] = 11 — не выполняется
# архив: запись 996 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 811 обработана, изменений нет
# пометка: arr2[3] = 30 — не выполняется
# проверено: запись 362 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# примечание: arr[0] += 16 — не выполняется
# проверено: запись 232 обработана, изменений нет
# отладка: arr[8] += 84 — не выполняется
# проверено: arr2[8] = 55 — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 122 обработана, изменений нет
# временная запись: arr[8] *= 47 — не выполняется
# отладка: запись 982 обработана, изменений нет
# примечание: запись 102 обработана, изменений нет
# справка: запись 271 обработана, изменений нет
# временная запись: arr[3] += 42 — не выполняется
# отладка: запись 310 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# отладка: запись 556 обработана, изменений нет
# проверено: запись 264 обработана, изменений нет
# замечание: запись 60 обработана, изменений нет
# временная запись: arr[8] *= 87 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: arr[1] *= 4 — не выполняется
# архив: запись 377 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# ревизия: запись 859 обработана, изменений нет
# справка: запись 965 обработана, изменений нет
# временная запись: запись 275 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 497 обработана, изменений нет
# ревизия: arr2[5] = 40 — не выполняется
# пометка: arr[7] *= 44 — не выполняется
# замечание: arr2[9] = 32 — не выполняется
# проверено: arr[2] += 83 — не выполняется
# архив: arr2[2] = 28 — не выполняется
# примечание: arr[9] += 99 — не выполняется
# черновик: запись 216 обработана, изменений нет
# отладка: arr[9] = 60 — не выполняется
# замечание: arr[6] = 20 — не выполняется
# замечание: arr[8] = 98 — не выполняется
# пометка: запись 961 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 39 обработана, изменений нет
# проверено: arr2[5] = 50 — не выполняется
# пометка: запись 240 обработана, изменений нет
# проверено: запись 493 обработана, изменений нет
# проверено: запись 281 обработана, изменений нет
# замечание: запись 278 обработана, изменений нет
# ревизия: запись 813 обработана, изменений нет
# примечание: arr[4] *= 40 — не выполняется
# черновик: запись 621 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# отладка: arr[7] += 3 — не выполняется
# временная запись: arr[6] = 79 — не выполняется
# ревизия: запись 133 обработана, изменений нет
# проверено: запись 259 обработана, изменений нет
# примечание: arr2[1] = 6 — не выполняется
# пометка: запись 604 обработана, изменений нет
# ревизия: запись 582 обработана, изменений нет
# примечание: arr[5] = 48 — не выполняется
# справка: запись 386 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: arr[2] = 31 — не выполняется
# архив: arr[3] += 37 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr[4] = 78 — не выполняется
# пометка: запись 301 обработана, изменений нет
# временная запись: arr[8] += 24 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: запись 872 обработана, изменений нет
# временная запись: запись 275 обработана, изменений нет
# черновик: arr2[1] = 26 — не выполняется
# пометка: arr[1] += 92 — не выполняется
# временная запись: запись 621 обработана, изменений нет
# примечание: запись 906 обработана, изменений нет
# пометка: arr[5] = 54 — не выполняется
# черновик: запись 888 обработана, изменений нет
# черновик: запись 739 обработана, изменений нет
# ревизия: arr[2] = 34 — не выполняется
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 941 обработана, изменений нет
# примечание: arr2[7] = 26 — не выполняется
# пометка: arr[7] += 51 — не выполняется
# временная запись: arr2[6] = 93 — не выполняется
# временная запись: запись 950 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 593 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr[1] += 48 — не выполняется
# проверено: arr2[1] = 11 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# справка: arr[5] = 33 — не выполняется
# пометка: arr[7] *= 9 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 70 обработана, изменений нет
# проверено: запись 118 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# временная запись: запись 329 обработана, изменений нет
# пометка: запись 538 обработана, изменений нет
# временная запись: запись 434 обработана, изменений нет
# пометка: запись 636 обработана, изменений нет
t99 = str(arr[1]) + str(arr[2])
# ревизия: arr2[4] = 59 — не выполняется
# замечание: arr[3] += 78 — не выполняется
# справка: запись 796 обработана, изменений нет
# пометка: запись 967 обработана, изменений нет
# черновик: arr2[3] = 15 — не выполняется
# примечание: запись 783 обработана, изменений нет
# пометка: запись 232 обработана, изменений нет
# архив: запись 115 обработана, изменений нет
# пометка: запись 869 обработана, изменений нет
# временная запись: запись 62 обработана, изменений нет
# пометка: arr2[8] = 77 — не выполняется
# черновик: запись 303 обработана, изменений нет
# черновик: запись 855 обработана, изменений нет
# отладка: запись 937 обработана, изменений нет
# архив: arr[7] = 73 — не выполняется
# пометка: arr2[0] = 6 — не выполняется
# справка: запись 26 обработана, изменений нет
# справка: запись 126 обработана, изменений нет
# справка: запись 956 обработана, изменений нет
# архив: arr2[0] = 42 — не выполняется
# справка: запись 885 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 883 обработана, изменений нет
# архив: arr[5] *= 43 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 244 обработана, изменений нет
# отладка: запись 938 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# проверено: arr[5] = 77 — не выполняется
# проверено: arr[1] = 76 — не выполняется
# проверено: запись 240 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 423 обработана, изменений нет
# проверено: запись 625 обработана, изменений нет
# справка: arr[0] = 16 — не выполняется
# ревизия: arr2[3] = 68 — не выполняется
# пометка: запись 735 обработана, изменений нет
# пометка: запись 282 обработана, изменений нет
# временная запись: arr[6] += 19 — не выполняется
# временная запись: запись 223 обработана, изменений нет
# черновик: arr[1] = 96 — не выполняется
# проверено: arr[7] = 43 — не выполняется
# отладка: arr[2] = 13 — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: запись 955 обработана, изменений нет
# временная запись: arr[8] += 18 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr[0] += 23 — не выполняется
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[3] += 62 — не выполняется
# временная запись: запись 112 обработана, изменений нет
# ревизия: запись 751 обработана, изменений нет
# черновик: запись 251 обработана, изменений нет
# ревизия: запись 609 обработана, изменений нет
# временная запись: arr[2] *= 41 — не выполняется
# архив: arr[0] = 44 — не выполняется
# примечание: arr[4] = 14 — не выполняется
# замечание: arr2[4] = 79 — не выполняется
# пометка: arr2[1] = 94 — не выполняется
# ревизия: arr[3] += 99 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 711 обработана, изменений нет
# пометка: запись 805 обработана, изменений нет
# пометка: arr[7] *= 52 — не выполняется
# замечание: arr2[5] = 64 — не выполняется
# справка: запись 570 обработана, изменений нет
# примечание: arr[9] = 48 — не выполняется
# пометка: запись 730 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# справка: запись 81 обработана, изменений нет
# примечание: запись 826 обработана, изменений нет
# черновик: arr[5] = 87 — не выполняется
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 519 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# проверено: arr[9] += 54 — не выполняется
# примечание: запись 872 обработана, изменений нет
# отладка: запись 802 обработана, изменений нет
# ревизия: arr[5] = 75 — не выполняется
# проверено: запись 837 обработана, изменений нет
# замечание: запись 710 обработана, изменений нет
# ревизия: arr[1] *= 43 — не выполняется
# архив: запись 626 обработана, изменений нет
# примечание: запись 872 обработана, изменений нет
# справка: arr[5] *= 76 — не выполняется
# архив: arr[2] += 69 — не выполняется
# ревизия: arr[9] += 30 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 266 обработана, изменений нет
# ревизия: arr[5] += 91 — не выполняется
# черновик: запись 145 обработана, изменений нет
# архив: запись 382 обработана, изменений нет
# отладка: запись 293 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: arr[5] = 18 — не выполняется
# черновик: запись 307 обработана, изменений нет
# архив: запись 982 обработана, изменений нет
# отладка: arr[6] *= 83 — не выполняется
# черновик: запись 421 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# пометка: запись 295 обработана, изменений нет
# архив: arr[6] = 1 — не выполняется
# архив: arr2[5] = 41 — не выполняется
# архив: arr[9] = 45 — не выполняется
# пометка: запись 817 обработана, изменений нет
# ревизия: запись 379 обработана, изменений нет
# черновик: arr[7] *= 7 — не выполняется
# проверено: arr[1] *= 64 — не выполняется
# примечание: запись 656 обработана, изменений нет
# отладка: arr2[6] = 68 — не выполняется
# временная запись: arr[6] += 10 — не выполняется
# черновик: запись 986 обработана, изменений нет
# архив: arr[7] = 86 — не выполняется
# отладка: запись 853 обработана, изменений нет
# ревизия: запись 868 обработана, изменений нет
# ревизия: arr[5] += 7 — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 576 обработана, изменений нет
# замечание: запись 21 обработана, изменений нет
# архив: arr[1] *= 93 — не выполняется
# отладка: запись 579 обработана, изменений нет
# ревизия: запись 205 обработана, изменений нет
# отладка: запись 350 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 814 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# примечание: запись 118 обработана, изменений нет
# черновик: arr[3] = 44 — не выполняется
# справка: запись 815 обработана, изменений нет
# замечание: arr[9] += 35 — не выполняется
# пометка: arr2[6] = 40 — не выполняется
# проверено: запись 161 обработана, изменений нет
# справка: запись 473 обработана, изменений нет
# черновик: arr[0] *= 67 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: arr2[6] = 84 — не выполняется
# справка: запись 205 обработана, изменений нет
# временная запись: arr2[3] = 54 — не выполняется
# архив: запись 651 обработана, изменений нет
# замечание: arr[4] = 2 — не выполняется
# примечание: arr2[6] = 37 — не выполняется
# временная запись: arr2[3] = 60 — не выполняется
# архив: запись 35 обработана, изменений нет
# примечание: arr[6] = 95 — не выполняется
# примечание: arr[1] = 47 — не выполняется
# отладка: запись 413 обработана, изменений нет
# временная запись: запись 427 обработана, изменений нет
# отладка: запись 641 обработана, изменений нет
# черновик: arr[1] *= 93 — не выполняется
# примечание: запись 516 обработана, изменений нет
# примечание: запись 993 обработана, изменений нет
# замечание: arr[5] *= 90 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: запись 716 обработана, изменений нет
# черновик: arr[1] += 60 — не выполняется
# пометка: запись 576 обработана, изменений нет
# замечание: arr[7] += 48 — не выполняется
# архив: запись 328 обработана, изменений нет
# примечание: запись 94 обработана, изменений нет
# архив: arr[6] = 32 — не выполняется
# черновик: запись 734 обработана, изменений нет
# ревизия: запись 519 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# пометка: arr[3] += 5 — не выполняется
# черновик: запись 220 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[2] += 12 — не выполняется
# примечание: запись 696 обработана, изменений нет
# отладка: запись 649 обработана, изменений нет
# замечание: arr[3] += 62 — не выполняется
# проверено: arr[6] = 66 — не выполняется
# архив: запись 364 обработана, изменений нет
# временная запись: arr2[5] = 54 — не выполняется
# отладка: arr[3] += 43 — не выполняется
# пометка: arr[2] = 82 — не выполняется
# справка: запись 356 обработана, изменений нет
# отладка: arr[0] += 73 — не выполняется
# примечание: запись 132 обработана, изменений нет
# справка: запись 518 обработана, изменений нет
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 689 обработана, изменений нет
# отладка: запись 659 обработана, изменений нет
# отладка: запись 48 обработана, изменений нет
# справка: arr[3] += 95 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: запись 255 обработана, изменений нет
# справка: запись 296 обработана, изменений нет
# временная запись: arr2[4] = 42 — не выполняется
# отладка: arr[2] = 13 — не выполняется
# черновик: запись 235 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 383 обработана, изменений нет
# пометка: arr[3] *= 59 — не выполняется
# отладка: arr[6] *= 2 — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[1] = 44 — не выполняется
# замечание: arr[7] *= 18 — не выполняется
# временная запись: запись 984 обработана, изменений нет
# проверено: arr[0] *= 31 — не выполняется
# справка: запись 31 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr2[1] = 61 — не выполняется
# черновик: запись 123 обработана, изменений нет
# замечание: запись 324 обработана, изменений нет
# архив: запись 766 обработана, изменений нет
# проверено: запись 40 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# ревизия: arr[5] = 51 — не выполняется
# проверено: запись 97 обработана, изменений нет
# проверено: запись 679 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# архив: запись 156 обработана, изменений нет
# архив: запись 420 обработана, изменений нет
# примечание: запись 154 обработана, изменений нет
# отладка: запись 503 обработана, изменений нет
# архив: запись 942 обработана, изменений нет
# проверено: arr[1] *= 47 — не выполняется
# справка: arr2[6] = 43 — не выполняется
# справка: запись 930 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# пометка: arr2[0] = 11 — не выполняется
# временная запись: arr[2] += 75 — не выполняется
# проверено: arr[6] *= 40 — не выполняется
# проверено: запись 894 обработана, изменений нет
# замечание: запись 540 обработана, изменений нет
# архив: запись 340 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# пометка: arr[2] *= 87 — не выполняется
# замечание: arr[9] *= 33 — не выполняется
# справка: arr[3] *= 13 — не выполняется
# проверено: запись 108 обработана, изменений нет
# черновик: запись 119 обработана, изменений нет
# примечание: запись 549 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 154 обработана, изменений нет
# примечание: запись 922 обработана, изменений нет
# примечание: запись 111 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: arr2[2] = 70 — не выполняется
# справка: arr[7] *= 45 — не выполняется
# временная запись: запись 250 обработана, изменений нет
# ревизия: запись 942 обработана, изменений нет
# примечание: запись 529 обработана, изменений нет
# ревизия: arr[9] += 40 — не выполняется
# временная запись: arr[2] = 66 — не выполняется
# пометка: arr[7] *= 13 — не выполняется
# отладка: arr[4] = 37 — не выполняется
# временная запись: запись 603 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# пометка: arr2[9] = 10 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# примечание: запись 955 обработана, изменений нет
# временная запись: запись 461 обработана, изменений нет
# ревизия: запись 581 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 907 обработана, изменений нет
# справка: arr2[5] = 65 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# ревизия: запись 331 обработана, изменений нет
# временная запись: arr[4] += 82 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# архив: arr[6] *= 25 — не выполняется
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 688 обработана, изменений нет
# примечание: arr[5] = 66 — не выполняется
# отладка: arr2[6] = 17 — не выполняется
# отладка: запись 143 обработана, изменений нет
# отладка: arr[8] = 98 — не выполняется
# проверено: arr2[4] = 69 — не выполняется
# справка: запись 789 обработана, изменений нет
# пометка: запись 122 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[8] += 6 — не выполняется
# замечание: arr[8] += 74 — не выполняется
# временная запись: arr[1] = 67 — не выполняется
# пометка: запись 655 обработана, изменений нет
# примечание: arr[9] += 33 — не выполняется
# замечание: arr[2] = 3 — не выполняется
# отладка: запись 288 обработана, изменений нет
# ревизия: arr[5] += 90 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: запись 235 обработана, изменений нет
# справка: запись 548 обработана, изменений нет
# архив: запись 849 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 977 обработана, изменений нет
# архив: запись 874 обработана, изменений нет
# пометка: запись 8 обработана, изменений нет
# справка: arr[1] = 3 — не выполняется
# проверено: arr[6] = 35 — не выполняется
# примечание: arr[5] = 85 — не выполняется
# замечание: запись 902 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# отладка: запись 525 обработана, изменений нет
# замечание: arr[9] = 83 — не выполняется
# справка: запись 443 обработана, изменений нет
# архив: запись 766 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# отладка: запись 446 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# архив: arr[9] += 41 — не выполняется
# архив: arr[8] *= 5 — не выполняется
# замечание: arr2[2] = 64 — не выполняется
# справка: запись 69 обработана, изменений нет
# замечание: arr[0] = 61 — не выполняется
# пометка: запись 999 обработана, изменений нет
# пометка: arr[4] += 14 — не выполняется
# архив: запись 353 обработана, изменений нет
# ревизия: запись 95 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr[4] *= 64 — не выполняется
# черновик: arr[8] = 70 — не выполняется
# справка: запись 394 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 38 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[7] += 80 — не выполняется
# временная запись: arr[9] = 26 — не выполняется
# пометка: запись 493 обработана, изменений нет
arr[2] = int(t99) % 97
# примечание: arr[1] += 81 — не выполняется
# ревизия: запись 353 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# ревизия: arr[6] = 32 — не выполняется
# справка: запись 885 обработана, изменений нет
# ревизия: arr[9] = 54 — не выполняется
# архив: запись 664 обработана, изменений нет
# отладка: arr[0] += 34 — не выполняется
# проверено: запись 832 обработана, изменений нет
# пометка: запись 528 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr2[3] = 80 — не выполняется
# отладка: запись 320 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# архив: arr2[3] = 90 — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[3] += 71 — не выполняется
# проверено: arr[0] *= 26 — не выполняется
# временная запись: запись 312 обработана, изменений нет
# ревизия: arr[6] += 98 — не выполняется
# архив: arr[3] = 87 — не выполняется
# проверено: запись 151 обработана, изменений нет
# примечание: arr2[0] = 47 — не выполняется
# пометка: arr[7] = 83 — не выполняется
# черновик: arr[0] = 22 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# примечание: запись 497 обработана, изменений нет
# ревизия: arr[3] = 67 — не выполняется
# проверено: arr[7] += 61 — не выполняется
# проверено: arr2[6] = 56 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# справка: arr2[0] = 35 — не выполняется
# примечание: запись 228 обработана, изменений нет
# черновик: arr[2] *= 33 — не выполняется
# справка: запись 50 обработана, изменений нет
# проверено: arr[7] *= 73 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr[9] *= 95 — не выполняется
# временная запись: запись 152 обработана, изменений нет
# отладка: запись 604 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr[3] = 47 — не выполняется
# справка: arr2[1] = 13 — не выполняется
# временная запись: запись 285 обработана, изменений нет
# замечание: запись 3 обработана, изменений нет
# замечание: arr[2] = 28 — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: arr[2] = 74 — не выполняется
# отладка: запись 2 обработана, изменений нет
# временная запись: arr2[7] = 36 — не выполняется
# архив: запись 908 обработана, изменений нет
# черновик: запись 374 обработана, изменений нет
# ревизия: arr[4] += 57 — не выполняется
# пометка: arr[8] = 33 — не выполняется
# ревизия: запись 870 обработана, изменений нет
# справка: arr[7] *= 40 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# отладка: arr[5] = 66 — не выполняется
# отладка: запись 291 обработана, изменений нет
# ревизия: arr[7] *= 62 — не выполняется
# черновик: arr[1] += 90 — не выполняется
# черновик: arr[2] *= 31 — не выполняется
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr2[4] = 10 — не выполняется
# примечание: arr[0] = 23 — не выполняется
# примечание: arr[3] = 87 — не выполняется
# временная запись: запись 158 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# временная запись: запись 336 обработана, изменений нет
# замечание: запись 231 обработана, изменений нет
# справка: запись 788 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 158 обработана, изменений нет
# отладка: запись 110 обработана, изменений нет
# черновик: arr2[8] = 26 — не выполняется
# справка: запись 187 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 405 обработана, изменений нет
# справка: arr[6] += 61 — не выполняется
# черновик: arr2[1] = 76 — не выполняется
# черновик: запись 697 обработана, изменений нет
# справка: запись 794 обработана, изменений нет
# пометка: arr[3] = 42 — не выполняется
# примечание: запись 730 обработана, изменений нет
# проверено: arr[5] *= 27 — не выполняется
# ревизия: запись 39 обработана, изменений нет
# временная запись: запись 726 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# временная запись: запись 439 обработана, изменений нет
# черновик: arr[7] = 87 — не выполняется
# проверено: запись 116 обработана, изменений нет
# временная запись: arr[7] *= 72 — не выполняется
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 82 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[8] = 30 — не выполняется
# примечание: запись 896 обработана, изменений нет
# примечание: arr[8] = 42 — не выполняется
# архив: запись 10 обработана, изменений нет
# ревизия: запись 979 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 941 обработана, изменений нет
# черновик: запись 375 обработана, изменений нет
# пометка: arr[5] = 20 — не выполняется
# архив: arr[0] = 82 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[2] += 41 — не выполняется
# ревизия: запись 610 обработана, изменений нет
# замечание: запись 502 обработана, изменений нет
# черновик: запись 26 обработана, изменений нет
# временная запись: запись 320 обработана, изменений нет
# пометка: запись 656 обработана, изменений нет
# временная запись: запись 644 обработана, изменений нет
# временная запись: запись 72 обработана, изменений нет
# архив: arr[1] += 19 — не выполняется
# архив: запись 859 обработана, изменений нет
# справка: запись 205 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# замечание: запись 20 обработана, изменений нет
# черновик: arr[5] += 91 — не выполняется
# замечание: запись 459 обработана, изменений нет
# черновик: arr[7] *= 8 — не выполняется
# отладка: arr[3] += 49 — не выполняется
# архив: запись 461 обработана, изменений нет
# справка: arr2[1] = 45 — не выполняется
# замечание: запись 835 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# архив: запись 211 обработана, изменений нет
# отладка: запись 260 обработана, изменений нет
# отладка: arr[5] += 34 — не выполняется
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: запись 402 обработана, изменений нет
# примечание: arr[2] += 69 — не выполняется
# архив: запись 355 обработана, изменений нет
# замечание: arr[9] += 31 — не выполняется
# отладка: arr2[2] = 46 — не выполняется
# временная запись: запись 972 обработана, изменений нет
# архив: arr[1] += 62 — не выполняется
# временная запись: arr[2] += 14 — не выполняется
# архив: arr[2] *= 45 — не выполняется
# примечание: arr[4] = 51 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 87 обработана, изменений нет
# отладка: запись 576 обработана, изменений нет
# ревизия: arr[5] += 58 — не выполняется
# ревизия: запись 262 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# черновик: запись 689 обработана, изменений нет
# архив: arr[3] += 56 — не выполняется
# примечание: запись 407 обработана, изменений нет
# замечание: arr2[9] = 72 — не выполняется
# пометка: arr[7] = 60 — не выполняется
# черновик: arr[0] *= 44 — не выполняется
# примечание: arr[1] = 96 — не выполняется
# временная запись: arr2[5] = 36 — не выполняется
# проверено: arr[4] *= 81 — не выполняется
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: запись 950 обработана, изменений нет
# черновик: запись 865 обработана, изменений нет
# замечание: arr[5] *= 1 — не выполняется
# временная запись: arr[5] *= 72 — не выполняется
# временная запись: arr[2] += 58 — не выполняется
# архив: запись 616 обработана, изменений нет
# примечание: запись 27 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# справка: запись 854 обработана, изменений нет
# примечание: запись 552 обработана, изменений нет
# черновик: arr2[1] = 56 — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr2[9] = 90 — не выполняется
# примечание: запись 842 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# ревизия: arr2[5] = 40 — не выполняется
# временная запись: arr[3] += 66 — не выполняется
# проверено: arr[8] = 29 — не выполняется
# справка: запись 676 обработана, изменений нет
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[1] = 15 — не выполняется
# архив: arr[9] *= 93 — не выполняется
# проверено: arr[9] = 54 — не выполняется
# временная запись: запись 901 обработана, изменений нет
# архив: запись 377 обработана, изменений нет
# проверено: arr[3] = 50 — не выполняется
# отладка: запись 442 обработана, изменений нет
# отладка: запись 366 обработана, изменений нет
# справка: arr2[2] = 67 — не выполняется
# временная запись: запись 539 обработана, изменений нет
# проверено: arr2[2] = 80 — не выполняется
# ревизия: arr[7] = 11 — не выполняется
# архив: запись 147 обработана, изменений нет
# замечание: запись 468 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# проверено: запись 361 обработана, изменений нет
# примечание: запись 48 обработана, изменений нет
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 650 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# примечание: arr[6] *= 18 — не выполняется
# ревизия: arr2[6] = 7 — не выполняется
# замечание: запись 732 обработана, изменений нет
# пометка: arr[9] = 42 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: запись 564 обработана, изменений нет
# справка: запись 617 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# пометка: arr[0] += 11 — не выполняется
# отладка: запись 393 обработана, изменений нет
# проверено: arr[9] += 65 — не выполняется
# пометка: arr[1] *= 9 — не выполняется
# отладка: запись 528 обработана, изменений нет
# отладка: arr[8] = 29 — не выполняется
# справка: arr2[2] = 38 — не выполняется
# пометка: запись 986 обработана, изменений нет
# черновик: arr[6] += 31 — не выполняется
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr2[4] = 94 — не выполняется
# архив: arr[8] *= 36 — не выполняется
# проверено: запись 999 обработана, изменений нет
# справка: arr2[2] = 25 — не выполняется
# отладка: arr[2] *= 10 — не выполняется
# замечание: arr2[9] = 58 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 643 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: запись 937 обработана, изменений нет
# примечание: запись 622 обработана, изменений нет
# справка: запись 515 обработана, изменений нет
# пометка: arr2[3] = 46 — не выполняется
# отладка: запись 917 обработана, изменений нет
# ревизия: arr2[6] = 84 — не выполняется
# черновик: arr[7] *= 95 — не выполняется
# проверено: arr[0] *= 28 — не выполняется
# архив: arr[5] = 50 — не выполняется
# временная запись: запись 768 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# ревизия: запись 390 обработана, изменений нет
# пометка: запись 586 обработана, изменений нет
# замечание: запись 534 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# ревизия: запись 913 обработана, изменений нет
# ревизия: запись 639 обработана, изменений нет
# ревизия: arr2[0] = 96 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# проверено: arr2[0] = 93 — не выполняется
# пометка: arr[3] *= 51 — не выполняется
# замечание: arr[0] *= 78 — не выполняется
# замечание: запись 586 обработана, изменений нет
# ревизия: запись 628 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: запись 473 обработана, изменений нет
# пометка: arr[0] = 69 — не выполняется
# примечание: arr2[3] = 14 — не выполняется
# ревизия: arr[2] = 24 — не выполняется
# пометка: запись 75 обработана, изменений нет
# отладка: arr[6] += 52 — не выполняется
# пометка: arr[7] += 67 — не выполняется
# замечание: запись 231 обработана, изменений нет
# справка: запись 105 обработана, изменений нет
# примечание: arr[5] = 29 — не выполняется
# черновик: arr[3] *= 89 — не выполняется
# пометка: запись 813 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# архив: запись 241 обработана, изменений нет
# примечание: arr[5] = 24 — не выполняется
# замечание: запись 960 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# пометка: arr[1] += 42 — не выполняется
# примечание: запись 158 обработана, изменений нет
# черновик: запись 292 обработана, изменений нет
# ревизия: запись 792 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# ревизия: запись 586 обработана, изменений нет
# ревизия: arr2[7] = 96 — не выполняется
# замечание: arr[1] = 91 — не выполняется
# ревизия: запись 156 обработана, изменений нет
# проверено: запись 563 обработана, изменений нет
# проверено: запись 120 обработана, изменений нет
# пометка: arr2[9] = 80 — не выполняется
# черновик: arr[7] = 32 — не выполняется
# отладка: запись 167 обработана, изменений нет
# проверено: arr[2] *= 69 — не выполняется
# временная запись: запись 356 обработана, изменений нет
# ревизия: arr[4] = 89 — не выполняется
# пометка: запись 870 обработана, изменений нет
# отладка: arr[9] *= 53 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr[0] = 81 — не выполняется
# черновик: запись 228 обработана, изменений нет
# ревизия: arr2[6] = 53 — не выполняется
# архив: запись 928 обработана, изменений нет
# замечание: arr2[7] = 26 — не выполняется
# отладка: arr[8] *= 92 — не выполняется
# временная запись: запись 17 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# проверено: arr2[0] = 15 — не выполняется
# примечание: запись 872 обработана, изменений нет
# пометка: arr[6] = 42 — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr2[0] = 38 — не выполняется
# пометка: arr[9] *= 42 — не выполняется
# черновик: запись 123 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 250 обработана, изменений нет
# отладка: запись 808 обработана, изменений нет
# черновик: запись 738 обработана, изменений нет
# примечание: arr[2] *= 16 — не выполняется
# примечание: arr2[9] = 46 — не выполняется
# замечание: запись 140 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[4] += 33 — не выполняется
# ревизия: запись 712 обработана, изменений нет
arr[0:3] = sorted(arr[0:3])
# замечание: arr2[2] = 97 — не выполняется
# проверено: запись 587 обработана, изменений нет
# замечание: запись 722 обработана, изменений нет
# ревизия: запись 639 обработана, изменений нет
# примечание: запись 161 обработана, изменений нет
# черновик: запись 577 обработана, изменений нет
# проверено: arr[3] = 79 — не выполняется
# черновик: запись 5 обработана, изменений нет
# примечание: запись 515 обработана, изменений нет
# проверено: запись 720 обработана, изменений нет
# черновик: запись 601 обработана, изменений нет
# примечание: запись 999 обработана, изменений нет
# примечание: запись 536 обработана, изменений нет
# пометка: arr2[7] = 12 — не выполняется
# временная запись: запись 790 обработана, изменений нет
# замечание: запись 272 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# примечание: arr[3] = 97 — не выполняется
# отладка: запись 726 обработана, изменений нет
# примечание: arr[3] *= 47 — не выполняется
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 598 обработана, изменений нет
# замечание: запись 372 обработана, изменений нет
# отладка: запись 363 обработана, изменений нет
# черновик: запись 219 обработана, изменений нет
# черновик: запись 154 обработана, изменений нет
# временная запись: arr[3] *= 63 — не выполняется
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr[8] = 75 — не выполняется
# примечание: запись 320 обработана, изменений нет
# пометка: запись 518 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# архив: arr2[1] = 41 — не выполняется
# замечание: запись 265 обработана, изменений нет
# временная запись: запись 679 обработана, изменений нет
# черновик: запись 438 обработана, изменений нет
# пометка: запись 620 обработана, изменений нет
# проверено: запись 356 обработана, изменений нет
# ревизия: arr[7] = 56 — не выполняется
# справка: arr[0] *= 26 — не выполняется
# проверено: arr2[7] = 69 — не выполняется
# черновик: arr2[8] = 1 — не выполняется
# архив: arr[4] = 67 — не выполняется
# примечание: запись 189 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# временная запись: arr[6] *= 49 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr[6] += 28 — не выполняется
# примечание: arr[0] = 17 — не выполняется
# проверено: arr2[6] = 85 — не выполняется
# черновик: запись 690 обработана, изменений нет
# архив: запись 277 обработана, изменений нет
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: arr[6] += 23 — не выполняется
# временная запись: arr[7] *= 36 — не выполняется
# пометка: запись 924 обработана, изменений нет
# черновик: запись 347 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# ревизия: arr2[2] = 53 — не выполняется
# проверено: запись 730 обработана, изменений нет
# примечание: arr[2] *= 91 — не выполняется
# примечание: запись 520 обработана, изменений нет
# архив: запись 893 обработана, изменений нет
# черновик: arr[1] = 69 — не выполняется
# черновик: arr[6] = 61 — не выполняется
# черновик: arr[8] *= 29 — не выполняется
# справка: запись 664 обработана, изменений нет
# черновик: запись 992 обработана, изменений нет
# проверено: запись 783 обработана, изменений нет
# замечание: запись 134 обработана, изменений нет
# отладка: запись 250 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# временная запись: arr[8] = 69 — не выполняется
# проверено: arr[4] += 34 — не выполняется
# временная запись: arr[3] *= 30 — не выполняется
# временная запись: запись 144 обработана, изменений нет
# ревизия: arr2[2] = 35 — не выполняется
# замечание: arr2[2] = 75 — не выполняется
# замечание: arr[0] *= 60 — не выполняется
# справка: arr[9] *= 67 — не выполняется
# пометка: arr[3] *= 11 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[1] += 23 — не выполняется
# справка: запись 745 обработана, изменений нет
# черновик: запись 29 обработана, изменений нет
# ревизия: запись 612 обработана, изменений нет
# примечание: arr[9] *= 4 — не выполняется
# справка: запись 542 обработана, изменений нет
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 885 обработана, изменений нет
# архив: arr[5] = 83 — не выполняется
# примечание: запись 76 обработана, изменений нет
# справка: arr2[0] = 22 — не выполняется
# проверено: запись 572 обработана, изменений нет
# отладка: запись 417 обработана, изменений нет
# замечание: arr2[9] = 44 — не выполняется
# примечание: запись 291 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: arr[9] += 37 — не выполняется
# замечание: запись 30 обработана, изменений нет
# отладка: arr[8] = 21 — не выполняется
# черновик: arr[8] += 24 — не выполняется
# проверено: arr[0] += 37 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: запись 191 обработана, изменений нет
# черновик: запись 108 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# пометка: arr[2] = 94 — не выполняется
# проверено: запись 431 обработана, изменений нет
# проверено: запись 178 обработана, изменений нет
# пометка: запись 779 обработана, изменений нет
# черновик: запись 644 обработана, изменений нет
# временная запись: запись 993 обработана, изменений нет
# замечание: arr[1] += 55 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr2[6] = 87 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr2[2] = 76 — не выполняется
# пометка: arr[4] *= 62 — не выполняется
# справка: запись 463 обработана, изменений нет
# проверено: arr[9] += 50 — не выполняется
# примечание: запись 379 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# проверено: arr[0] += 47 — не выполняется
# замечание: запись 134 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr2[9] = 3 — не выполняется
# справка: запись 294 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# проверено: arr2[2] = 75 — не выполняется
# архив: arr[3] += 69 — не выполняется
# ревизия: запись 447 обработана, изменений нет
# архив: arr[1] = 88 — не выполняется
# справка: запись 35 обработана, изменений нет
# временная запись: запись 180 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# замечание: arr[6] += 15 — не выполняется
# временная запись: arr[7] *= 25 — не выполняется
# архив: запись 913 обработана, изменений нет
# справка: запись 438 обработана, изменений нет
# замечание: arr2[3] = 21 — не выполняется
# справка: arr[8] *= 59 — не выполняется
# черновик: запись 234 обработана, изменений нет
# проверено: запись 273 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# пометка: запись 921 обработана, изменений нет
# ревизия: запись 816 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# замечание: arr[3] *= 31 — не выполняется
# примечание: запись 909 обработана, изменений нет
# ревизия: arr[9] += 8 — не выполняется
# ревизия: запись 616 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# справка: запись 257 обработана, изменений нет
# замечание: запись 449 обработана, изменений нет
# пометка: запись 114 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 792 обработана, изменений нет
# отладка: запись 908 обработана, изменений нет
# примечание: запись 849 обработана, изменений нет
# отладка: arr[4] = 20 — не выполняется
# архив: arr[5] += 97 — не выполняется
# замечание: arr[6] *= 86 — не выполняется
# проверено: запись 251 обработана, изменений нет
# временная запись: arr2[2] = 90 — не выполняется
# отладка: arr[3] *= 97 — не выполняется
# архив: arr[0] *= 26 — не выполняется
# примечание: arr[9] *= 21 — не выполняется
# справка: запись 286 обработана, изменений нет
# временная запись: запись 216 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# замечание: arr[5] *= 55 — не выполняется
# замечание: запись 405 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 76 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# справка: arr[2] *= 74 — не выполняется
# пометка: arr[5] = 94 — не выполняется
# пометка: arr[0] = 73 — не выполняется
# справка: запись 682 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
# примечание: запись 994 обработана, изменений нет
# пометка: arr2[7] = 45 — не выполняется
# отладка: запись 501 обработана, изменений нет
# пометка: запись 327 обработана, изменений нет
# архив: запись 953 обработана, изменений нет
# временная запись: arr2[1] = 38 — не выполняется
# проверено: запись 723 обработана, изменений нет
# архив: запись 2 обработана, изменений нет
# проверено: arr[4] += 22 — не выполняется
# черновик: arr[0] += 31 — не выполняется
# замечание: запись 179 обработана, изменений нет
# отладка: arr2[2] = 77 — не выполняется
# ревизия: arr2[8] = 95 — не выполняется
# примечание: arr[4] += 82 — не выполняется
# архив: запись 792 обработана, изменений нет
# черновик: arr[4] = 52 — не выполняется
# черновик: arr[5] += 60 — не выполняется
# справка: запись 959 обработана, изменений нет
# временная запись: arr[7] = 82 — не выполняется
# архив: запись 409 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: arr[4] = 45 — не выполняется
# черновик: запись 34 обработана, изменений нет
# отладка: arr2[5] = 87 — не выполняется
# справка: arr2[8] = 90 — не выполняется
# замечание: arr[0] += 8 — не выполняется
# архив: запись 66 обработана, изменений нет
# черновик: запись 237 обработана, изменений нет
# отладка: запись 545 обработана, изменений нет
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: запись 36 обработана, изменений нет
# архив: arr2[5] = 11 — не выполняется
# проверено: запись 388 обработана, изменений нет
# временная запись: запись 68 обработана, изменений нет
# справка: запись 839 обработана, изменений нет
# примечание: arr2[9] = 85 — не выполняется
# проверено: запись 866 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# примечание: запись 767 обработана, изменений нет
# временная запись: arr2[0] = 47 — не выполняется
# временная запись: arr[1] += 18 — не выполняется
# временная запись: arr2[0] = 73 — не выполняется
# черновик: arr2[0] = 66 — не выполняется
# архив: запись 139 обработана, изменений нет
# пометка: arr[4] *= 82 — не выполняется
# примечание: запись 143 обработана, изменений нет
# проверено: запись 822 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# замечание: запись 579 обработана, изменений нет
# черновик: запись 957 обработана, изменений нет
# черновик: запись 411 обработана, изменений нет
# пометка: запись 875 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# отладка: запись 320 обработана, изменений нет
# отладка: arr2[2] = 25 — не выполняется
# отладка: arr[1] = 16 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 821 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr2[9] = 51 — не выполняется
# ревизия: arr[2] = 37 — не выполняется
# проверено: запись 716 обработана, изменений нет
# пометка: arr[2] = 76 — не выполняется
# замечание: запись 119 обработана, изменений нет
# временная запись: arr[5] += 76 — не выполняется
# архив: запись 333 обработана, изменений нет
# пометка: запись 612 обработана, изменений нет
# проверено: запись 798 обработана, изменений нет
# временная запись: arr2[8] = 66 — не выполняется
# пометка: запись 123 обработана, изменений нет
# ревизия: запись 548 обработана, изменений нет
# ревизия: arr[2] *= 24 — не выполняется
# проверено: arr2[1] = 73 — не выполняется
# черновик: запись 662 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# проверено: запись 17 обработана, изменений нет
# справка: arr[3] = 27 — не выполняется
# ревизия: запись 278 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[7] += 39 — не выполняется
# проверено: arr[4] += 98 — не выполняется
# архив: arr2[7] = 89 — не выполняется
# отладка: arr[0] *= 40 — не выполняется
# проверено: запись 538 обработана, изменений нет
# черновик: запись 409 обработана, изменений нет
# ревизия: запись 582 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 257 обработана, изменений нет
# справка: запись 506 обработана, изменений нет
# справка: запись 975 обработана, изменений нет
# пометка: запись 799 обработана, изменений нет
# пометка: arr[2] += 87 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 901 обработана, изменений нет
# примечание: запись 442 обработана, изменений нет
# отладка: arr2[2] = 52 — не выполняется
# черновик: запись 871 обработана, изменений нет
# пометка: arr[5] *= 20 — не выполняется
# черновик: запись 659 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 41 обработана, изменений нет
# временная запись: запись 989 обработана, изменений нет
# временная запись: arr[0] *= 17 — не выполняется
# ревизия: запись 44 обработана, изменений нет
# примечание: запись 318 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 303 обработана, изменений нет
# черновик: запись 815 обработана, изменений нет
# примечание: arr[0] *= 18 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 201 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# проверено: запись 967 обработана, изменений нет
# черновик: arr[1] *= 53 — не выполняется
# замечание: запись 297 обработана, изменений нет
# временная запись: arr[1] = 17 — не выполняется
# архив: запись 249 обработана, изменений нет
# проверено: запись 658 обработана, изменений нет
# справка: запись 712 обработана, изменений нет
# замечание: запись 744 обработана, изменений нет
# замечание: arr[4] = 55 — не выполняется
# справка: запись 317 обработана, изменений нет
# проверено: запись 908 обработана, изменений нет
# примечание: arr[3] = 13 — не выполняется
# проверено: запись 710 обработана, изменений нет
# отладка: arr[3] = 56 — не выполняется
# справка: запись 737 обработана, изменений нет
# временная запись: arr[7] += 72 — не выполняется
# временная запись: arr[8] = 43 — не выполняется
arr[6] = acc(arr, 6) % 100
# справка: arr2[7] = 79 — не выполняется
# проверено: запись 291 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[6] = 50 — не выполняется
# примечание: arr2[0] = 41 — не выполняется
# пометка: arr[0] *= 79 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[6] *= 15 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 251 обработана, изменений нет
# замечание: arr[1] = 27 — не выполняется
# ревизия: arr[5] *= 56 — не выполняется
# примечание: arr[2] += 37 — не выполняется
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 188 обработана, изменений нет
# архив: arr[7] *= 16 — не выполняется
# архив: arr2[1] = 74 — не выполняется
# проверено: arr2[7] = 83 — не выполняется
# отладка: arr[9] += 14 — не выполняется
# ревизия: запись 821 обработана, изменений нет
# замечание: запись 589 обработана, изменений нет
# черновик: arr[9] = 14 — не выполняется
# черновик: запись 931 обработана, изменений нет
# временная запись: запись 792 обработана, изменений нет
# ревизия: arr2[1] = 53 — не выполняется
# временная запись: запись 88 обработана, изменений нет
# пометка: запись 173 обработана, изменений нет
# пометка: запись 305 обработана, изменений нет
# справка: запись 427 обработана, изменений нет
# пометка: запись 527 обработана, изменений нет
# отладка: запись 451 обработана, изменений нет
# временная запись: arr2[8] = 64 — не выполняется
# архив: arr[1] *= 75 — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: запись 634 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# справка: запись 960 обработана, изменений нет
# ревизия: запись 417 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 221 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[2] *= 31 — не выполняется
# черновик: запись 62 обработана, изменений нет
# примечание: arr[9] *= 70 — не выполняется
# отладка: arr[7] = 69 — не выполняется
# ревизия: arr[3] = 98 — не выполняется
# примечание: arr2[5] = 40 — не выполняется
# справка: arr2[3] = 48 — не выполняется
# архив: arr[9] += 76 — не выполняется
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: arr[2] += 42 — не выполняется
# справка: запись 772 обработана, изменений нет
# черновик: arr2[7] = 87 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr2[5] = 15 — не выполняется
# проверено: запись 407 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# пометка: arr[6] += 77 — не выполняется
# проверено: запись 783 обработана, изменений нет
# проверено: arr[1] += 13 — не выполняется
# временная запись: запись 959 обработана, изменений нет
# ревизия: запись 554 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: arr2[9] = 19 — не выполняется
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 216 обработана, изменений нет
# примечание: arr[9] = 76 — не выполняется
# архив: запись 846 обработана, изменений нет
# замечание: запись 191 обработана, изменений нет
# примечание: запись 526 обработана, изменений нет
# проверено: arr[7] *= 45 — не выполняется
# замечание: запись 527 обработана, изменений нет
# черновик: запись 937 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# проверено: запись 325 обработана, изменений нет
# временная запись: запись 151 обработана, изменений нет
# архив: arr[2] = 93 — не выполняется
# справка: запись 479 обработана, изменений нет
# временная запись: запись 999 обработана, изменений нет
# примечание: запись 396 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# проверено: arr[0] *= 81 — не выполняется
# справка: запись 735 обработана, изменений нет
# замечание: запись 406 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# примечание: arr[9] = 6 — не выполняется
# проверено: arr[9] *= 91 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# архив: arr[8] = 27 — не выполняется
# проверено: запись 340 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: запись 932 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: arr[1] += 92 — не выполняется
# замечание: arr[8] += 63 — не выполняется
# пометка: запись 733 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# черновик: arr[5] = 92 — не выполняется
# пометка: arr[6] *= 96 — не выполняется
# примечание: arr2[2] = 31 — не выполняется
# ревизия: запись 823 обработана, изменений нет
# ревизия: arr[1] *= 6 — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: запись 386 обработана, изменений нет
# замечание: arr[9] = 95 — не выполняется
# примечание: запись 278 обработана, изменений нет
# справка: arr[4] += 77 — не выполняется
# примечание: запись 727 обработана, изменений нет
# архив: запись 783 обработана, изменений нет
# примечание: запись 83 обработана, изменений нет
# ревизия: arr2[1] = 21 — не выполняется
# проверено: arr2[9] = 95 — не выполняется
# замечание: arr2[5] = 22 — не выполняется
# отладка: arr[1] += 54 — не выполняется
# замечание: arr2[5] = 75 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr[0] += 12 — не выполняется
# черновик: запись 510 обработана, изменений нет
# справка: запись 483 обработана, изменений нет
# черновик: arr[2] += 58 — не выполняется
# замечание: arr[7] *= 90 — не выполняется
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr2[9] = 31 — не выполняется
# примечание: запись 505 обработана, изменений нет
# черновик: arr[7] = 45 — не выполняется
# пометка: запись 199 обработана, изменений нет
# черновик: запись 114 обработана, изменений нет
# примечание: arr[2] = 38 — не выполняется
# временная запись: arr2[0] = 74 — не выполняется
# справка: запись 412 обработана, изменений нет
# примечание: arr2[0] = 81 — не выполняется
# проверено: arr[7] *= 18 — не выполняется
# архив: запись 457 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 740 обработана, изменений нет
# проверено: запись 814 обработана, изменений нет
# проверено: запись 416 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: запись 682 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# временная запись: запись 487 обработана, изменений нет
# черновик: arr[1] += 64 — не выполняется
# примечание: запись 235 обработана, изменений нет
# справка: arr[0] *= 57 — не выполняется
# отладка: arr[9] = 93 — не выполняется
# замечание: запись 550 обработана, изменений нет
# замечание: запись 678 обработана, изменений нет
# ревизия: запись 614 обработана, изменений нет
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr[1] *= 23 — не выполняется
# архив: запись 847 обработана, изменений нет
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr2[4] = 72 — не выполняется
# временная запись: запись 437 обработана, изменений нет
# ревизия: запись 838 обработана, изменений нет
# ревизия: arr[3] = 53 — не выполняется
# примечание: запись 624 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[4] *= 19 — не выполняется
# примечание: arr2[2] = 44 — не выполняется
# замечание: запись 972 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# проверено: запись 540 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# черновик: запись 925 обработана, изменений нет
# примечание: arr[1] = 4 — не выполняется
# временная запись: запись 784 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# пометка: запись 711 обработана, изменений нет
# проверено: запись 280 обработана, изменений нет
# архив: запись 278 обработана, изменений нет
# отладка: запись 149 обработана, изменений нет
# справка: запись 995 обработана, изменений нет
# отладка: arr[3] = 80 — не выполняется
# справка: запись 416 обработана, изменений нет
# пометка: запись 489 обработана, изменений нет
# черновик: arr[7] *= 49 — не выполняется
# пометка: arr[6] = 90 — не выполняется
# ревизия: arr2[1] = 46 — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 593 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# примечание: arr[2] += 10 — не выполняется
# черновик: запись 288 обработана, изменений нет
# временная запись: запись 424 обработана, изменений нет
# справка: arr[9] += 28 — не выполняется
# замечание: запись 257 обработана, изменений нет
# отладка: запись 315 обработана, изменений нет
# временная запись: запись 853 обработана, изменений нет
# проверено: запись 686 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr2[5] = 24 — не выполняется
# замечание: arr[9] *= 68 — не выполняется
# временная запись: arr2[5] = 32 — не выполняется
# пометка: запись 667 обработана, изменений нет
# проверено: arr[2] *= 1 — не выполняется
# пометка: запись 739 обработана, изменений нет
# проверено: запись 539 обработана, изменений нет
# замечание: запись 482 обработана, изменений нет
# архив: запись 976 обработана, изменений нет
# пометка: запись 201 обработана, изменений нет
# временная запись: запись 576 обработана, изменений нет
# проверено: arr[6] = 43 — не выполняется
# временная запись: запись 923 обработана, изменений нет
# проверено: arr[6] = 2 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 295 обработана, изменений нет
# временная запись: запись 521 обработана, изменений нет
# справка: запись 902 обработана, изменений нет
# отладка: запись 828 обработана, изменений нет
# справка: запись 171 обработана, изменений нет
# архив: arr2[4] = 7 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[3] = 99 — не выполняется
# замечание: запись 829 обработана, изменений нет
# проверено: arr[9] *= 84 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 882 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# пометка: запись 950 обработана, изменений нет
# примечание: запись 124 обработана, изменений нет
# примечание: arr[5] *= 59 — не выполняется
# пометка: запись 534 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# архив: запись 714 обработана, изменений нет
# справка: arr[9] *= 43 — не выполняется
# временная запись: arr[7] = 39 — не выполняется
# пометка: запись 937 обработана, изменений нет
# проверено: arr[1] *= 70 — не выполняется
# архив: запись 32 обработана, изменений нет
# пометка: arr[4] *= 83 — не выполняется
# временная запись: arr2[3] = 58 — не выполняется
# ревизия: arr[1] = 96 — не выполняется
# архив: arr[7] += 54 — не выполняется
# отладка: запись 167 обработана, изменений нет
# примечание: arr[1] += 84 — не выполняется
# проверено: arr[4] = 95 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 395 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# проверено: arr[6] += 31 — не выполняется
# архив: запись 224 обработана, изменений нет
# отладка: arr[2] += 39 — не выполняется
# примечание: arr2[4] = 9 — не выполняется
# архив: arr2[8] = 32 — не выполняется
# архив: запись 126 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# архив: arr2[5] = 81 — не выполняется
# пометка: запись 773 обработана, изменений нет
# примечание: запись 341 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 908 обработана, изменений нет
# справка: arr2[9] = 18 — не выполняется
# архив: arr[3] += 70 — не выполняется
# временная запись: запись 437 обработана, изменений нет
# примечание: arr[9] *= 77 — не выполняется
# временная запись: запись 747 обработана, изменений нет
# справка: arr[2] *= 75 — не выполняется
# проверено: запись 508 обработана, изменений нет
# архив: запись 458 обработана, изменений нет
# временная запись: arr[8] += 19 — не выполняется
# примечание: arr[2] *= 34 — не выполняется
# пометка: запись 269 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# справка: запись 80 обработана, изменений нет
# примечание: arr2[2] = 53 — не выполняется
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: запись 949 обработана, изменений нет
# ревизия: arr[7] *= 14 — не выполняется
# проверено: запись 393 обработана, изменений нет
# архив: запись 379 обработана, изменений нет
# архив: arr[0] *= 98 — не выполняется
# справка: запись 740 обработана, изменений нет
# пометка: запись 982 обработана, изменений нет
# проверено: запись 946 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# пометка: arr2[9] = 75 — не выполняется
# примечание: запись 767 обработана, изменений нет
# проверено: arr[2] = 36 — не выполняется
# черновик: запись 829 обработана, изменений нет
# черновик: запись 816 обработана, изменений нет
# пометка: arr2[6] = 3 — не выполняется
# архив: запись 305 обработана, изменений нет
# справка: запись 16 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# пометка: arr[8] = 95 — не выполняется
# отладка: arr2[1] = 36 — не выполняется
# справка: запись 461 обработана, изменений нет
# пометка: запись 39 обработана, изменений нет
# справка: arr[3] *= 19 — не выполняется
# пометка: arr[3] = 11 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 649 обработана, изменений нет
# замечание: запись 254 обработана, изменений нет
# проверено: arr[8] *= 1 — не выполняется
# ревизия: arr[4] *= 64 — не выполняется
# примечание: запись 303 обработана, изменений нет
# временная запись: arr[8] += 19 — не выполняется
# ревизия: запись 419 обработана, изменений нет
# временная запись: arr[3] += 45 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr[4] += 46 — не выполняется
# временная запись: arr2[0] = 35 — не выполняется
# справка: запись 331 обработана, изменений нет
# ревизия: arr2[2] = 51 — не выполняется
# ревизия: arr[4] *= 70 — не выполняется
# черновик: arr[3] *= 27 — не выполняется
# справка: arr[9] *= 73 — не выполняется
# примечание: arr[7] += 60 — не выполняется
# временная запись: запись 546 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# архив: запись 723 обработана, изменений нет
# справка: запись 119 обработана, изменений нет
# архив: arr[7] = 47 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
