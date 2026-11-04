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
arr2[9] = 14
arr[1] *= 44
arr[9] += 23
arr[3] += 58
arr[9], arr[5] = arr[5], arr[9]
arr2[7] = 57
arr2[2] = 17
arr2[7] = 8
"""

TRAP_0 = "arr[8] = 577"
TRAP_1 = "arr[5] = 294"
TRAP_2 = "arr[6] = 647"
TRAP_3 = "arr[3] = 478"
TRAP_4 = "arr[8] = 796"
TRAP_5 = "arr[5] = 260"
TRAP_6 = "arr[7] = 361"
TRAP_7 = "arr[0] = 671"
TRAP_8 = "arr[5] = 512"
TRAP_9 = "arr[0] = 757"
TRAP_10 = "arr[2] = 582"
TRAP_11 = "arr[5] = 482"
TRAP_12 = "arr[2] = 818"
TRAP_13 = "arr[1] = 933"
TRAP_14 = "arr[8] = 529"
TRAP_15 = "arr[7] = 734"
TRAP_16 = "arr[4] = 697"
TRAP_17 = "arr[5] = 972"
TRAP_18 = "arr[1] = 829"
TRAP_19 = "arr[0] = 362"
TRAP_20 = "arr[8] = 899"
TRAP_21 = "arr[3] = 881"
TRAP_22 = "arr[0] = 456"
TRAP_23 = "arr[3] = 170"
TRAP_24 = "arr[3] = 480"
TRAP_25 = "arr[1] = 501"
TRAP_26 = "arr[2] = 541"
TRAP_27 = "arr[6] = 497"
TRAP_28 = "arr[6] = 561"
TRAP_29 = "arr[9] = 423"
TRAP_30 = "arr[9] = 692"
TRAP_31 = "arr[5] = 688"
TRAP_32 = "arr[3] = 116"
TRAP_33 = "arr[1] = 180"
TRAP_34 = "arr[0] = 185"
TRAP_35 = "arr[9] = 507"
TRAP_36 = "arr[6] = 371"
TRAP_37 = "arr[0] = 391"
TRAP_38 = "arr[8] = 599"
TRAP_39 = "arr[8] = 651"
TRAP_40 = "arr[3] = 467"
TRAP_41 = "arr[1] = 967"
TRAP_42 = "arr[5] = 334"
TRAP_43 = "arr[6] = 139"
TRAP_44 = "arr[5] = 334"
TRAP_45 = "arr[5] = 137"
TRAP_46 = "arr[1] = 140"
TRAP_47 = "arr[6] = 205"
TRAP_48 = "arr[3] = 207"
TRAP_49 = "arr[7] = 418"
TRAP_50 = "arr[1] = 882"
TRAP_51 = "arr[7] = 798"
TRAP_52 = "arr[8] = 444"
TRAP_53 = "arr[7] = 811"
TRAP_54 = "arr[6] = 555"
TRAP_55 = "arr[0] = 810"
TRAP_56 = "arr[2] = 790"
TRAP_57 = "arr[2] = 494"
TRAP_58 = "arr[5] = 309"
TRAP_59 = "arr[4] = 734"
TRAP_60 = "arr[9] = 404"
TRAP_61 = "arr[3] = 132"
TRAP_62 = "arr[3] = 857"
TRAP_63 = "arr[2] = 521"
TRAP_64 = "arr[5] = 754"
TRAP_65 = "arr[8] = 334"
TRAP_66 = "arr[9] = 543"
TRAP_67 = "arr[4] = 567"
TRAP_68 = "arr[7] = 330"
TRAP_69 = "arr[1] = 971"
TRAP_70 = "arr[2] = 421"
TRAP_71 = "arr[5] = 211"
TRAP_72 = "arr[1] = 314"
TRAP_73 = "arr[2] = 581"
TRAP_74 = "arr[0] = 852"
TRAP_75 = "arr[9] = 197"
TRAP_76 = "arr[3] = 864"
TRAP_77 = "arr[9] = 388"
TRAP_78 = "arr[7] = 733"
TRAP_79 = "arr[9] = 711"
TRAP_80 = "arr[5] = 499"
TRAP_81 = "arr[3] = 231"
TRAP_82 = "arr[4] = 214"
TRAP_83 = "arr[2] = 254"
TRAP_84 = "arr[2] = 531"
TRAP_85 = "arr[7] = 396"
TRAP_86 = "arr[0] = 479"
TRAP_87 = "arr[6] = 539"
TRAP_88 = "arr[4] = 293"
TRAP_89 = "arr[1] = 882"
TRAP_90 = "arr[4] = 204"
TRAP_91 = "arr[8] = 389"
TRAP_92 = "arr[2] = 437"
TRAP_93 = "arr[8] = 965"
TRAP_94 = "arr[3] = 329"
TRAP_95 = "arr[5] = 796"
TRAP_96 = "arr[9] = 827"
TRAP_97 = "arr[7] = 190"
TRAP_98 = "arr[7] = 286"
TRAP_99 = "arr[7] = 223"
TRAP_100 = "arr[4] = 557"
TRAP_101 = "arr[7] = 100"
TRAP_102 = "arr[4] = 852"
TRAP_103 = "arr[1] = 889"
TRAP_104 = "arr[2] = 443"
TRAP_105 = "arr[8] = 667"
TRAP_106 = "arr[0] = 429"
TRAP_107 = "arr[5] = 853"
TRAP_108 = "arr[4] = 338"
TRAP_109 = "arr[7] = 894"
TRAP_110 = "arr[3] = 264"
TRAP_111 = "arr[5] = 533"
TRAP_112 = "arr[8] = 647"
TRAP_113 = "arr[2] = 285"
TRAP_114 = "arr[5] = 573"
TRAP_115 = "arr[8] = 326"
TRAP_116 = "arr[0] = 547"
TRAP_117 = "arr[5] = 298"
TRAP_118 = "arr[3] = 435"
TRAP_119 = "arr[3] = 115"
TRAP_120 = "arr[8] = 110"
TRAP_121 = "arr[9] = 213"
TRAP_122 = "arr[3] = 161"
TRAP_123 = "arr[1] = 211"
TRAP_124 = "arr[0] = 555"
TRAP_125 = "arr[2] = 676"
TRAP_126 = "arr[2] = 838"
TRAP_127 = "arr[1] = 185"
TRAP_128 = "arr[4] = 889"
TRAP_129 = "arr[8] = 327"
TRAP_130 = "arr[7] = 668"
TRAP_131 = "arr[1] = 839"
TRAP_132 = "arr[1] = 303"
TRAP_133 = "arr[3] = 390"
TRAP_134 = "arr[6] = 736"
TRAP_135 = "arr[0] = 543"
TRAP_136 = "arr[2] = 380"
TRAP_137 = "arr[1] = 503"
TRAP_138 = "arr[2] = 766"
TRAP_139 = "arr[7] = 451"
TRAP_140 = "arr[2] = 870"
TRAP_141 = "arr[3] = 195"
TRAP_142 = "arr[9] = 472"
TRAP_143 = "arr[2] = 149"
TRAP_144 = "arr[9] = 908"
TRAP_145 = "arr[7] = 993"
TRAP_146 = "arr[4] = 573"
TRAP_147 = "arr[8] = 351"
TRAP_148 = "arr[8] = 607"
TRAP_149 = "arr[1] = 324"

arr = [6, 29, 30, 2, 26, 23, 18, 25, 20, 20]

tmp_0 = arr[4] + 5
code_1 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_2 = arr[7] + 20
copy_3 = arr[5]
label_4 = "запись 4 не применялась"
code_5 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_6 = arr[4]
tmp_7 = arr[1] + 33
code_8 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_9 = arr[1] + 26
note_10 = str(arr[8]) + str(arr[4])
copy_11 = arr[5]
tmp_12 = arr[6] + 41
code_13 = re.sub(r'[0-9]', '#', str(arr[1]))
note_14 = str(arr[1]) + str(arr[0])
tmp_15 = arr[0] + 47
copy_16 = arr[1]
tmp_17 = arr[5] + 46
tmp_18 = arr[9] + 29
label_19 = "запись 19 не применялась"
copy_20 = arr[9]
tmp_21 = arr[3] + 34
code_22 = re.sub(r'[0-9]', '#', str(arr[0]))
note_23 = str(arr[4]) + str(arr[2])
note_24 = str(arr[4]) + str(arr[0])
copy_25 = arr[0]
tmp_26 = arr[9] + 41
note_27 = str(arr[1]) + str(arr[4])
note_28 = str(arr[3]) + str(arr[5])
tmp_29 = arr[8] + 19
copy_30 = arr[5]
tmp_31 = arr[0] + 43
tmp_32 = arr[3] + 43
tmp_33 = arr[5] + 24
note_34 = str(arr[1]) + str(arr[5])
note_35 = str(arr[9]) + str(arr[3])
tmp_36 = arr[1] + 43
tmp_37 = arr[3] + 17
note_38 = str(arr[5]) + str(arr[5])
note_39 = str(arr[2]) + str(arr[3])
label_40 = "запись 40 не применялась"
tmp_41 = arr[2] + 15
note_42 = str(arr[1]) + str(arr[6])
code_43 = re.sub(r'[0-9]', '#', str(arr[4]))
label_44 = "запись 44 не применялась"
tmp_45 = arr[7] + 42
tmp_46 = arr[0] + 27
tmp_47 = arr[4] + 25
code_48 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_49 = arr[9] + 29
copy_50 = arr[6]
tmp_51 = arr[0] + 3
tmp_52 = arr[2] + 28
tmp_53 = arr[7] + 6
label_54 = "запись 54 не применялась"
label_55 = "запись 55 не применялась"
code_56 = re.sub(r'[0-9]', '#', str(arr[5]))
note_57 = str(arr[8]) + str(arr[9])
note_58 = str(arr[0]) + str(arr[6])
label_59 = "запись 59 не применялась"
code_60 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_61 = arr[8]
note_62 = str(arr[4]) + str(arr[8])
code_63 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_64 = arr[5]
code_65 = re.sub(r'[0-9]', '#', str(arr[6]))
note_66 = str(arr[1]) + str(arr[1])
code_67 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_68 = arr[2]
code_69 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_70 = arr[7] + 42
tmp_71 = arr[8] + 11
tmp_72 = arr[1] + 39
tmp_73 = arr[5] + 37
tmp_74 = arr[9] + 37
tmp_75 = arr[0] + 43
tmp_76 = arr[6] + 38
tmp_77 = arr[1] + 43
tmp_78 = arr[2] + 41
note_79 = str(arr[9]) + str(arr[2])
tmp_80 = arr[3] + 4
tmp_81 = arr[9] + 13
copy_82 = arr[9]
note_83 = str(arr[5]) + str(arr[0])
tmp_84 = arr[2] + 25
code_85 = re.sub(r'[0-9]', '#', str(arr[1]))
label_86 = "запись 86 не применялась"
code_87 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_88 = arr[4]
note_89 = str(arr[6]) + str(arr[8])
code_90 = re.sub(r'[0-9]', '#', str(arr[7]))
note_91 = str(arr[1]) + str(arr[0])
note_92 = str(arr[8]) + str(arr[5])
note_93 = str(arr[2]) + str(arr[2])
tmp_94 = arr[9] + 1
tmp_95 = arr[8] + 8
tmp_96 = arr[0] + 13
label_97 = "запись 97 не применялась"
note_98 = str(arr[6]) + str(arr[4])
tmp_99 = arr[3] + 27
copy_100 = arr[3]
note_101 = str(arr[2]) + str(arr[5])
copy_102 = arr[4]
tmp_103 = arr[6] + 23
label_104 = "запись 104 не применялась"
note_105 = str(arr[2]) + str(arr[9])
tmp_106 = arr[4] + 34
tmp_107 = arr[7] + 19
note_108 = str(arr[0]) + str(arr[0])
note_109 = str(arr[1]) + str(arr[8])
code_110 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_111 = arr[8] + 13
tmp_112 = arr[4] + 21
code_113 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_114 = arr[5] + 20
code_115 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_116 = arr[7] + 32
tmp_117 = arr[1] + 45
label_118 = "запись 118 не применялась"
tmp_119 = arr[7] + 9
tmp_120 = arr[6] + 29
copy_121 = arr[0]
copy_122 = arr[6]
note_123 = str(arr[9]) + str(arr[7])
note_124 = str(arr[4]) + str(arr[1])
note_125 = str(arr[4]) + str(arr[3])
code_126 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_127 = arr[0]
copy_128 = arr[9]
note_129 = str(arr[9]) + str(arr[9])
tmp_130 = arr[4] + 34
tmp_131 = arr[8] + 33
code_132 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_133 = arr[7] + 1
note_134 = str(arr[3]) + str(arr[0])
note_135 = str(arr[2]) + str(arr[4])
note_136 = str(arr[4]) + str(arr[3])
tmp_137 = arr[4] + 10
tmp_138 = arr[2] + 43
copy_139 = arr[9]
tmp_140 = arr[5] + 8
label_141 = "запись 141 не применялась"
tmp_142 = arr[0] + 44
code_143 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_144 = arr[5] + 43
note_145 = str(arr[5]) + str(arr[6])
note_146 = str(arr[1]) + str(arr[2])
note_147 = str(arr[7]) + str(arr[4])
note_148 = str(arr[7]) + str(arr[7])
note_149 = str(arr[3]) + str(arr[0])
label_150 = "запись 150 не применялась"
tmp_151 = arr[8] + 47
note_152 = str(arr[3]) + str(arr[5])
tmp_153 = arr[3] + 27
tmp_154 = arr[8] + 15
code_155 = re.sub(r'[0-9]', '#', str(arr[6]))
note_156 = str(arr[0]) + str(arr[0])
note_157 = str(arr[2]) + str(arr[3])
copy_158 = arr[8]
note_159 = str(arr[0]) + str(arr[7])
copy_160 = arr[3]
code_161 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_162 = arr[6] + 10
tmp_163 = arr[8] + 33
tmp_164 = arr[3] + 17
note_165 = str(arr[2]) + str(arr[5])
tmp_166 = arr[9] + 42
code_167 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_168 = arr[8] + 44
tmp_169 = arr[8] + 17
code_170 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_171 = arr[8] + 49
label_172 = "запись 172 не применялась"
tmp_173 = arr[1] + 34
tmp_174 = arr[5] + 1
tmp_175 = arr[9] + 42
code_176 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_177 = arr[3]
copy_178 = arr[3]
label_179 = "запись 179 не применялась"
label_180 = "запись 180 не применялась"
note_181 = str(arr[0]) + str(arr[8])
copy_182 = arr[2]
tmp_183 = arr[5] + 33
note_184 = str(arr[5]) + str(arr[0])
label_185 = "запись 185 не применялась"
note_186 = str(arr[2]) + str(arr[7])
code_187 = re.sub(r'[0-9]', '#', str(arr[3]))
code_188 = re.sub(r'[0-9]', '#', str(arr[1]))
code_189 = re.sub(r'[0-9]', '#', str(arr[7]))
note_190 = str(arr[1]) + str(arr[9])
copy_191 = arr[1]
tmp_192 = arr[8] + 31
copy_193 = arr[9]
tmp_194 = arr[2] + 46
note_195 = str(arr[7]) + str(arr[9])
code_196 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_197 = arr[8] + 31
note_198 = str(arr[1]) + str(arr[5])
code_199 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_200 = arr[9]
copy_201 = arr[5]
code_202 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_203 = arr[9] + 48
note_204 = str(arr[0]) + str(arr[5])
code_205 = re.sub(r'[0-9]', '#', str(arr[9]))
note_206 = str(arr[8]) + str(arr[9])
tmp_207 = arr[0] + 34
tmp_208 = arr[6] + 32
note_209 = str(arr[6]) + str(arr[5])
note_210 = str(arr[5]) + str(arr[0])
tmp_211 = arr[4] + 41
tmp_212 = arr[8] + 17
tmp_213 = arr[2] + 11
tmp_214 = arr[2] + 40
note_215 = str(arr[9]) + str(arr[7])
note_216 = str(arr[7]) + str(arr[0])
note_217 = str(arr[2]) + str(arr[4])
label_218 = "запись 218 не применялась"
tmp_219 = arr[6] + 11
label_220 = "запись 220 не применялась"
tmp_221 = arr[8] + 29
label_222 = "запись 222 не применялась"
label_223 = "запись 223 не применялась"
tmp_224 = arr[8] + 48
tmp_225 = arr[9] + 44
label_226 = "запись 226 не применялась"
note_227 = str(arr[6]) + str(arr[7])
code_228 = re.sub(r'[0-9]', '#', str(arr[4]))
code_229 = re.sub(r'[0-9]', '#', str(arr[0]))
label_230 = "запись 230 не применялась"
note_231 = str(arr[5]) + str(arr[5])
note_232 = str(arr[0]) + str(arr[2])
copy_233 = arr[7]
note_234 = str(arr[4]) + str(arr[2])
tmp_235 = arr[4] + 38
tmp_236 = arr[1] + 24
note_237 = str(arr[4]) + str(arr[9])
code_238 = re.sub(r'[0-9]', '#', str(arr[1]))
note_239 = str(arr[6]) + str(arr[6])
note_240 = str(arr[7]) + str(arr[5])
note_241 = str(arr[8]) + str(arr[2])
tmp_242 = arr[7] + 2
tmp_243 = arr[2] + 14
tmp_244 = arr[5] + 44
tmp_245 = arr[4] + 37
code_246 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_247 = arr[5]
copy_248 = arr[2]
code_249 = re.sub(r'[0-9]', '#', str(arr[7]))
note_250 = str(arr[2]) + str(arr[8])
tmp_251 = arr[5] + 15
code_252 = re.sub(r'[0-9]', '#', str(arr[7]))
label_253 = "запись 253 не применялась"
copy_254 = arr[7]
copy_255 = arr[8]
note_256 = str(arr[5]) + str(arr[3])
code_257 = re.sub(r'[0-9]', '#', str(arr[1]))
note_258 = str(arr[9]) + str(arr[8])
tmp_259 = arr[4] + 17
tmp_260 = arr[5] + 27
code_261 = re.sub(r'[0-9]', '#', str(arr[5]))
code_262 = re.sub(r'[0-9]', '#', str(arr[8]))
code_263 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_264 = arr[2] + 29
note_265 = str(arr[4]) + str(arr[9])
copy_266 = arr[9]
copy_267 = arr[3]
label_268 = "запись 268 не применялась"
tmp_269 = arr[5] + 20
label_270 = "запись 270 не применялась"
code_271 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_272 = arr[5] + 8
note_273 = str(arr[5]) + str(arr[3])
note_274 = str(arr[0]) + str(arr[2])
code_275 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_276 = arr[3]
tmp_277 = arr[4] + 37
note_278 = str(arr[4]) + str(arr[5])
note_279 = str(arr[4]) + str(arr[3])
tmp_280 = arr[4] + 45
tmp_281 = arr[3] + 30
code_282 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_283 = arr[7] + 26
tmp_284 = arr[8] + 17
code_285 = re.sub(r'[0-9]', '#', str(arr[4]))
note_286 = str(arr[1]) + str(arr[9])
note_287 = str(arr[4]) + str(arr[9])
tmp_288 = arr[0] + 35
code_289 = re.sub(r'[0-9]', '#', str(arr[0]))
code_290 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_291 = arr[7] + 14
code_292 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_293 = arr[2] + 15
note_294 = str(arr[0]) + str(arr[3])
note_295 = str(arr[5]) + str(arr[7])
label_296 = "запись 296 не применялась"
tmp_297 = arr[1] + 21
code_298 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_299 = arr[9] + 34
note_300 = str(arr[2]) + str(arr[0])
tmp_301 = arr[5] + 1
note_302 = str(arr[0]) + str(arr[5])
copy_303 = arr[1]
tmp_304 = arr[9] + 15
copy_305 = arr[1]
tmp_306 = arr[5] + 7
code_307 = re.sub(r'[0-9]', '#', str(arr[2]))
label_308 = "запись 308 не применялась"
tmp_309 = arr[6] + 28
copy_310 = arr[6]
code_311 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_312 = arr[3] + 34
copy_313 = arr[0]
code_314 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_315 = arr[0] + 5
tmp_316 = arr[4] + 46
tmp_317 = arr[4] + 16
copy_318 = arr[9]
copy_319 = arr[6]
label_320 = "запись 320 не применялась"
note_321 = str(arr[5]) + str(arr[1])
tmp_322 = arr[0] + 37
tmp_323 = arr[4] + 45
tmp_324 = arr[0] + 23
tmp_325 = arr[6] + 15
copy_326 = arr[3]
note_327 = str(arr[3]) + str(arr[1])
note_328 = str(arr[8]) + str(arr[2])
code_329 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_330 = arr[6] + 19
note_331 = str(arr[7]) + str(arr[6])
tmp_332 = arr[9] + 42
tmp_333 = arr[5] + 18
copy_334 = arr[9]
note_335 = str(arr[5]) + str(arr[6])
code_336 = re.sub(r'[0-9]', '#', str(arr[8]))
note_337 = str(arr[3]) + str(arr[4])
note_338 = str(arr[6]) + str(arr[4])
label_339 = "запись 339 не применялась"
label_340 = "запись 340 не применялась"
note_341 = str(arr[1]) + str(arr[2])
copy_342 = arr[6]
tmp_343 = arr[8] + 36
note_344 = str(arr[7]) + str(arr[8])
note_345 = str(arr[4]) + str(arr[0])
note_346 = str(arr[8]) + str(arr[2])
label_347 = "запись 347 не применялась"
code_348 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_349 = arr[4] + 29
tmp_350 = arr[9] + 31
note_351 = str(arr[3]) + str(arr[3])
tmp_352 = arr[0] + 38
tmp_353 = arr[2] + 27
label_354 = "запись 354 не применялась"
copy_355 = arr[8]
note_356 = str(arr[8]) + str(arr[8])
tmp_357 = arr[6] + 32
copy_358 = arr[4]
label_359 = "запись 359 не применялась"
label_360 = "запись 360 не применялась"
note_361 = str(arr[7]) + str(arr[1])
code_362 = re.sub(r'[0-9]', '#', str(arr[6]))
code_363 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_364 = arr[1]
tmp_365 = arr[4] + 16
copy_366 = arr[2]
note_367 = str(arr[0]) + str(arr[4])
label_368 = "запись 368 не применялась"
copy_369 = arr[7]
code_370 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_371 = arr[6]
note_372 = str(arr[5]) + str(arr[4])
tmp_373 = arr[8] + 42
copy_374 = arr[7]
tmp_375 = arr[1] + 46
note_376 = str(arr[9]) + str(arr[5])
code_377 = re.sub(r'[0-9]', '#', str(arr[1]))
note_378 = str(arr[7]) + str(arr[6])
tmp_379 = arr[9] + 11
note_380 = str(arr[8]) + str(arr[7])
note_381 = str(arr[5]) + str(arr[1])
label_382 = "запись 382 не применялась"
note_383 = str(arr[4]) + str(arr[5])
label_384 = "запись 384 не применялась"
label_385 = "запись 385 не применялась"
label_386 = "запись 386 не применялась"
note_387 = str(arr[6]) + str(arr[4])
code_388 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_389 = arr[6]
code_390 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_391 = arr[5] + 16
code_392 = re.sub(r'[0-9]', '#', str(arr[0]))
code_393 = re.sub(r'[0-9]', '#', str(arr[8]))
label_394 = "запись 394 не применялась"
copy_395 = arr[8]
tmp_396 = arr[4] + 13
code_397 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_398 = arr[6] + 7
copy_399 = arr[1]
code_400 = re.sub(r'[0-9]', '#', str(arr[1]))
label_401 = "запись 401 не применялась"
copy_402 = arr[8]
code_403 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_404 = arr[9] + 14
note_405 = str(arr[8]) + str(arr[6])
label_406 = "запись 406 не применялась"
tmp_407 = arr[9] + 28
copy_408 = arr[4]
copy_409 = arr[1]
tmp_410 = arr[2] + 50
note_411 = str(arr[5]) + str(arr[7])
code_412 = re.sub(r'[0-9]', '#', str(arr[3]))
note_413 = str(arr[8]) + str(arr[5])
note_414 = str(arr[2]) + str(arr[1])
code_415 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_416 = arr[1] + 27
code_417 = re.sub(r'[0-9]', '#', str(arr[7]))
code_418 = re.sub(r'[0-9]', '#', str(arr[7]))
label_419 = "запись 419 не применялась"
code_420 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_421 = arr[6] + 47
code_422 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_423 = arr[7] + 46
code_424 = re.sub(r'[0-9]', '#', str(arr[5]))
note_425 = str(arr[9]) + str(arr[1])
note_426 = str(arr[5]) + str(arr[3])
code_427 = re.sub(r'[0-9]', '#', str(arr[5]))
code_428 = re.sub(r'[0-9]', '#', str(arr[9]))
code_429 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_430 = arr[4] + 45
tmp_431 = arr[9] + 49
tmp_432 = arr[9] + 2
tmp_433 = arr[7] + 8
tmp_434 = arr[9] + 44
note_435 = str(arr[1]) + str(arr[0])
copy_436 = arr[9]
tmp_437 = arr[2] + 38
note_438 = str(arr[6]) + str(arr[8])
code_439 = re.sub(r'[0-9]', '#', str(arr[7]))
label_440 = "запись 440 не применялась"
note_441 = str(arr[9]) + str(arr[5])
code_442 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_443 = arr[7]
code_444 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_445 = arr[4] + 25
tmp_446 = arr[4] + 34
label_447 = "запись 447 не применялась"
note_448 = str(arr[3]) + str(arr[3])
tmp_449 = arr[2] + 7
note_450 = str(arr[1]) + str(arr[2])
copy_451 = arr[0]
note_452 = str(arr[5]) + str(arr[9])
tmp_453 = arr[9] + 31
tmp_454 = arr[0] + 12
copy_455 = arr[3]
code_456 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_457 = arr[2]
note_458 = str(arr[8]) + str(arr[0])
label_459 = "запись 459 не применялась"
tmp_460 = arr[7] + 26
tmp_461 = arr[9] + 4
tmp_462 = arr[7] + 46
note_463 = str(arr[8]) + str(arr[8])
code_464 = re.sub(r'[0-9]', '#', str(arr[3]))
code_465 = re.sub(r'[0-9]', '#', str(arr[6]))
note_466 = str(arr[0]) + str(arr[6])
code_467 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_468 = arr[6] + 44
label_469 = "запись 469 не применялась"
note_470 = str(arr[0]) + str(arr[5])
note_471 = str(arr[4]) + str(arr[5])
tmp_472 = arr[0] + 17
tmp_473 = arr[0] + 1
tmp_474 = arr[2] + 6
label_475 = "запись 475 не применялась"
copy_476 = arr[4]
code_477 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_478 = arr[9] + 4
code_479 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_480 = arr[1] + 29
code_481 = re.sub(r'[0-9]', '#', str(arr[6]))
code_482 = re.sub(r'[0-9]', '#', str(arr[9]))
label_483 = "запись 483 не применялась"
copy_484 = arr[1]
tmp_485 = arr[5] + 30
tmp_486 = arr[3] + 13
note_487 = str(arr[0]) + str(arr[8])
note_488 = str(arr[2]) + str(arr[2])
note_489 = str(arr[9]) + str(arr[6])
note_490 = str(arr[1]) + str(arr[3])
tmp_491 = arr[9] + 50
tmp_492 = arr[0] + 4
code_493 = re.sub(r'[0-9]', '#', str(arr[9]))
code_494 = re.sub(r'[0-9]', '#', str(arr[3]))
label_495 = "запись 495 не применялась"
label_496 = "запись 496 не применялась"
tmp_497 = arr[1] + 20
copy_498 = arr[2]
code_499 = re.sub(r'[0-9]', '#', str(arr[9]))
code_500 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_501 = arr[5] + 3
label_502 = "запись 502 не применялась"
code_503 = re.sub(r'[0-9]', '#', str(arr[4]))
code_504 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_505 = arr[6] + 34
code_506 = re.sub(r'[0-9]', '#', str(arr[4]))
note_507 = str(arr[5]) + str(arr[2])
note_508 = str(arr[3]) + str(arr[9])
tmp_509 = arr[8] + 31
note_510 = str(arr[6]) + str(arr[1])
note_511 = str(arr[4]) + str(arr[4])
copy_512 = arr[5]
note_513 = str(arr[1]) + str(arr[5])
code_514 = re.sub(r'[0-9]', '#', str(arr[3]))
note_515 = str(arr[7]) + str(arr[2])
code_516 = re.sub(r'[0-9]', '#', str(arr[0]))
note_517 = str(arr[8]) + str(arr[3])
note_518 = str(arr[4]) + str(arr[0])
tmp_519 = arr[6] + 31
note_520 = str(arr[1]) + str(arr[4])
tmp_521 = arr[6] + 16
note_522 = str(arr[1]) + str(arr[4])
copy_523 = arr[2]
note_524 = str(arr[1]) + str(arr[5])
note_525 = str(arr[7]) + str(arr[3])
code_526 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_527 = arr[9]
tmp_528 = arr[0] + 16
tmp_529 = arr[3] + 50
note_530 = str(arr[5]) + str(arr[2])
code_531 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_532 = arr[0] + 48
note_533 = str(arr[6]) + str(arr[9])
code_534 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_535 = arr[4] + 7
note_536 = str(arr[2]) + str(arr[4])
label_537 = "запись 537 не применялась"
tmp_538 = arr[2] + 15
tmp_539 = arr[2] + 21
note_540 = str(arr[7]) + str(arr[1])
copy_541 = arr[9]
copy_542 = arr[4]
tmp_543 = arr[3] + 3
tmp_544 = arr[4] + 30
tmp_545 = arr[3] + 20
tmp_546 = arr[7] + 26
tmp_547 = arr[0] + 15
code_548 = re.sub(r'[0-9]', '#', str(arr[5]))
code_549 = re.sub(r'[0-9]', '#', str(arr[0]))
code_550 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_551 = arr[9]
copy_552 = arr[4]
label_553 = "запись 553 не применялась"
copy_554 = arr[6]
tmp_555 = arr[1] + 30
copy_556 = arr[4]
copy_557 = arr[0]
copy_558 = arr[8]
copy_559 = arr[2]
code_560 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_561 = arr[0]
copy_562 = arr[1]
note_563 = str(arr[7]) + str(arr[5])
tmp_564 = arr[5] + 27
tmp_565 = arr[3] + 34
tmp_566 = arr[3] + 45
tmp_567 = arr[2] + 42
tmp_568 = arr[1] + 29
note_569 = str(arr[3]) + str(arr[6])
code_570 = re.sub(r'[0-9]', '#', str(arr[1]))
note_571 = str(arr[8]) + str(arr[1])
note_572 = str(arr[2]) + str(arr[3])
code_573 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_574 = arr[5] + 49
label_575 = "запись 575 не применялась"
note_576 = str(arr[8]) + str(arr[9])
note_577 = str(arr[3]) + str(arr[7])
tmp_578 = arr[0] + 24
note_579 = str(arr[4]) + str(arr[7])
code_580 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_581 = arr[7] + 15
note_582 = str(arr[2]) + str(arr[5])
code_583 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_584 = arr[1]
copy_585 = arr[6]
label_586 = "запись 586 не применялась"
note_587 = str(arr[7]) + str(arr[8])
tmp_588 = arr[3] + 48
label_589 = "запись 589 не применялась"
code_590 = re.sub(r'[0-9]', '#', str(arr[8]))
note_591 = str(arr[4]) + str(arr[7])
code_592 = re.sub(r'[0-9]', '#', str(arr[4]))
code_593 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_594 = arr[1] + 42
tmp_595 = arr[6] + 13
label_596 = "запись 596 не применялась"
note_597 = str(arr[4]) + str(arr[8])
code_598 = re.sub(r'[0-9]', '#', str(arr[1]))
code_599 = re.sub(r'[0-9]', '#', str(arr[6]))
code_600 = re.sub(r'[0-9]', '#', str(arr[5]))
label_601 = "запись 601 не применялась"
tmp_602 = arr[5] + 21
tmp_603 = arr[0] + 37
tmp_604 = arr[2] + 44
tmp_605 = arr[6] + 21
tmp_606 = arr[8] + 38
note_607 = str(arr[6]) + str(arr[9])
tmp_608 = arr[1] + 24
note_609 = str(arr[9]) + str(arr[9])
note_610 = str(arr[9]) + str(arr[7])
code_611 = re.sub(r'[0-9]', '#', str(arr[9]))
note_612 = str(arr[3]) + str(arr[2])
code_613 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_614 = arr[9] + 44
code_615 = re.sub(r'[0-9]', '#', str(arr[7]))
code_616 = re.sub(r'[0-9]', '#', str(arr[5]))
note_617 = str(arr[8]) + str(arr[9])
tmp_618 = arr[2] + 10
code_619 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_620 = arr[7] + 32
label_621 = "запись 621 не применялась"
code_622 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_623 = arr[1] + 35
note_624 = str(arr[0]) + str(arr[6])
tmp_625 = arr[1] + 18
note_626 = str(arr[3]) + str(arr[6])
tmp_627 = arr[7] + 35
code_628 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_629 = arr[0]
note_630 = str(arr[9]) + str(arr[6])
copy_631 = arr[5]
note_632 = str(arr[9]) + str(arr[3])
code_633 = re.sub(r'[0-9]', '#', str(arr[9]))
code_634 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_635 = arr[3] + 26
tmp_636 = arr[3] + 50
tmp_637 = arr[3] + 30
copy_638 = arr[4]
copy_639 = arr[5]
code_640 = re.sub(r'[0-9]', '#', str(arr[1]))
code_641 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_642 = arr[0] + 32
note_643 = str(arr[5]) + str(arr[0])
tmp_644 = arr[4] + 29
code_645 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_646 = arr[9] + 26
tmp_647 = arr[6] + 48
copy_648 = arr[8]
code_649 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_650 = arr[3]
copy_651 = arr[7]
tmp_652 = arr[0] + 12
tmp_653 = arr[1] + 34
code_654 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_655 = arr[5] + 48
tmp_656 = arr[7] + 12
code_657 = re.sub(r'[0-9]', '#', str(arr[4]))
code_658 = re.sub(r'[0-9]', '#', str(arr[6]))
label_659 = "запись 659 не применялась"
tmp_660 = arr[9] + 32
note_661 = str(arr[1]) + str(arr[4])
tmp_662 = arr[8] + 50
copy_663 = arr[0]
note_664 = str(arr[5]) + str(arr[2])
copy_665 = arr[7]
copy_666 = arr[9]
code_667 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_668 = arr[9] + 17
tmp_669 = arr[4] + 31
tmp_670 = arr[2] + 45
tmp_671 = arr[4] + 12
note_672 = str(arr[0]) + str(arr[6])
copy_673 = arr[6]
code_674 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_675 = arr[0] + 28
label_676 = "запись 676 не применялась"
note_677 = str(arr[2]) + str(arr[9])
tmp_678 = arr[4] + 28
copy_679 = arr[6]
code_680 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_681 = arr[1]
code_682 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_683 = arr[4]
note_684 = str(arr[3]) + str(arr[6])
tmp_685 = arr[0] + 40
code_686 = re.sub(r'[0-9]', '#', str(arr[5]))
note_687 = str(arr[2]) + str(arr[5])
code_688 = re.sub(r'[0-9]', '#', str(arr[3]))
code_689 = re.sub(r'[0-9]', '#', str(arr[8]))
label_690 = "запись 690 не применялась"
tmp_691 = arr[2] + 18
copy_692 = arr[8]
tmp_693 = arr[0] + 15
tmp_694 = arr[1] + 12
tmp_695 = arr[8] + 38
note_696 = str(arr[5]) + str(arr[6])
code_697 = re.sub(r'[0-9]', '#', str(arr[4]))
code_698 = re.sub(r'[0-9]', '#', str(arr[2]))
note_699 = str(arr[2]) + str(arr[1])
tmp_700 = arr[9] + 13
label_701 = "запись 701 не применялась"
code_702 = re.sub(r'[0-9]', '#', str(arr[0]))
code_703 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_704 = arr[3] + 44
code_705 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_706 = arr[7]
code_707 = re.sub(r'[0-9]', '#', str(arr[6]))
label_708 = "запись 708 не применялась"
tmp_709 = arr[2] + 3
note_710 = str(arr[6]) + str(arr[6])
note_711 = str(arr[9]) + str(arr[3])
tmp_712 = arr[7] + 12
code_713 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_714 = arr[6] + 43
label_715 = "запись 715 не применялась"
copy_716 = arr[9]
note_717 = str(arr[6]) + str(arr[2])
code_718 = re.sub(r'[0-9]', '#', str(arr[2]))
note_719 = str(arr[1]) + str(arr[9])
copy_720 = arr[0]
note_721 = str(arr[4]) + str(arr[1])
copy_722 = arr[5]
note_723 = str(arr[4]) + str(arr[1])
code_724 = re.sub(r'[0-9]', '#', str(arr[8]))
code_725 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_726 = arr[1]
copy_727 = arr[4]
note_728 = str(arr[8]) + str(arr[2])
code_729 = re.sub(r'[0-9]', '#', str(arr[3]))
note_730 = str(arr[6]) + str(arr[9])
code_731 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_732 = arr[3] + 25
note_733 = str(arr[1]) + str(arr[1])
note_734 = str(arr[0]) + str(arr[6])
code_735 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_736 = arr[2] + 35
code_737 = re.sub(r'[0-9]', '#', str(arr[2]))
note_738 = str(arr[0]) + str(arr[5])
tmp_739 = arr[5] + 4
tmp_740 = arr[8] + 12
tmp_741 = arr[0] + 3
tmp_742 = arr[1] + 28
tmp_743 = arr[4] + 46
note_744 = str(arr[2]) + str(arr[4])
note_745 = str(arr[7]) + str(arr[4])
note_746 = str(arr[9]) + str(arr[6])
copy_747 = arr[0]
code_748 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_749 = arr[1] + 4
note_750 = str(arr[3]) + str(arr[5])
tmp_751 = arr[0] + 26
label_752 = "запись 752 не применялась"
tmp_753 = arr[7] + 23
note_754 = str(arr[8]) + str(arr[6])
tmp_755 = arr[9] + 7
note_756 = str(arr[3]) + str(arr[5])
label_757 = "запись 757 не применялась"
note_758 = str(arr[8]) + str(arr[4])
tmp_759 = arr[8] + 48
label_760 = "запись 760 не применялась"
note_761 = str(arr[1]) + str(arr[7])
copy_762 = arr[6]
note_763 = str(arr[2]) + str(arr[4])
tmp_764 = arr[3] + 5
tmp_765 = arr[2] + 12
note_766 = str(arr[5]) + str(arr[3])
tmp_767 = arr[2] + 46
note_768 = str(arr[5]) + str(arr[5])
tmp_769 = arr[5] + 39
copy_770 = arr[8]
tmp_771 = arr[9] + 36
copy_772 = arr[3]
copy_773 = arr[3]
copy_774 = arr[0]
code_775 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_776 = arr[5] + 1
note_777 = str(arr[9]) + str(arr[6])
copy_778 = arr[8]
copy_779 = arr[9]
copy_780 = arr[5]
tmp_781 = arr[2] + 49
tmp_782 = arr[4] + 12
code_783 = re.sub(r'[0-9]', '#', str(arr[2]))
note_784 = str(arr[4]) + str(arr[9])
note_785 = str(arr[3]) + str(arr[9])
code_786 = re.sub(r'[0-9]', '#', str(arr[1]))
note_787 = str(arr[5]) + str(arr[9])
tmp_788 = arr[5] + 1
copy_789 = arr[9]
copy_790 = arr[5]
code_791 = re.sub(r'[0-9]', '#', str(arr[6]))
code_792 = re.sub(r'[0-9]', '#', str(arr[7]))
note_793 = str(arr[6]) + str(arr[5])
tmp_794 = arr[3] + 7
tmp_795 = arr[0] + 14
label_796 = "запись 796 не применялась"
note_797 = str(arr[3]) + str(arr[7])
code_798 = re.sub(r'[0-9]', '#', str(arr[2]))
note_799 = str(arr[9]) + str(arr[8])

arr[0] -= 9
# проверено: запись 189 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# временная запись: запись 974 обработана, изменений нет
# справка: arr[5] += 6 — не выполняется
# пометка: запись 373 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# пометка: arr[9] *= 68 — не выполняется
# отладка: arr2[8] = 76 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# временная запись: arr[9] += 80 — не выполняется
# проверено: arr[9] *= 34 — не выполняется
# справка: arr2[2] = 57 — не выполняется
# пометка: запись 914 обработана, изменений нет
# замечание: arr[0] *= 59 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: arr[1] += 4 — не выполняется
# временная запись: запись 439 обработана, изменений нет
# архив: arr[5] += 37 — не выполняется
# временная запись: запись 416 обработана, изменений нет
# временная запись: arr[7] = 75 — не выполняется
# примечание: запись 283 обработана, изменений нет
# архив: arr[0] = 47 — не выполняется
# архив: arr[4] += 2 — не выполняется
# отладка: запись 1 обработана, изменений нет
# справка: запись 781 обработана, изменений нет
# замечание: arr[9] *= 75 — не выполняется
# замечание: arr[2] += 11 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# временная запись: arr2[2] = 72 — не выполняется
# проверено: arr[7] = 56 — не выполняется
# замечание: arr[1] *= 87 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 539 обработана, изменений нет
# архив: arr[3] *= 53 — не выполняется
# отладка: arr[6] += 38 — не выполняется
# отладка: arr[1] += 22 — не выполняется
# пометка: arr[5] *= 53 — не выполняется
# замечание: arr[3] *= 39 — не выполняется
# отладка: запись 320 обработана, изменений нет
# справка: arr[2] = 11 — не выполняется
# ревизия: arr[1] += 58 — не выполняется
# пометка: запись 225 обработана, изменений нет
# пометка: запись 316 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# ревизия: запись 538 обработана, изменений нет
# пометка: arr[6] += 43 — не выполняется
# пометка: arr[9] = 55 — не выполняется
# замечание: arr[4] = 3 — не выполняется
# примечание: запись 187 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# справка: arr2[8] = 28 — не выполняется
# примечание: запись 843 обработана, изменений нет
# пометка: запись 478 обработана, изменений нет
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 123 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# архив: arr[7] += 60 — не выполняется
# пометка: запись 342 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# справка: arr[8] += 80 — не выполняется
# отладка: arr[1] = 91 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 124 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# справка: arr[4] = 38 — не выполняется
# пометка: запись 656 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[0] *= 89 — не выполняется
# пометка: запись 47 обработана, изменений нет
# пометка: запись 531 обработана, изменений нет
# справка: запись 361 обработана, изменений нет
# пометка: arr[9] += 94 — не выполняется
# архив: arr2[5] = 59 — не выполняется
# архив: запись 666 обработана, изменений нет
# пометка: запись 491 обработана, изменений нет
# проверено: arr[6] *= 67 — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 191 обработана, изменений нет
# замечание: arr[3] *= 26 — не выполняется
# ревизия: запись 338 обработана, изменений нет
# замечание: запись 81 обработана, изменений нет
# замечание: запись 212 обработана, изменений нет
# отладка: arr[1] += 4 — не выполняется
# замечание: arr[1] *= 16 — не выполняется
# примечание: arr[0] = 20 — не выполняется
# пометка: arr[0] = 56 — не выполняется
# пометка: arr[7] += 78 — не выполняется
# замечание: запись 222 обработана, изменений нет
# пометка: arr[6] *= 22 — не выполняется
# отладка: arr[6] *= 54 — не выполняется
# временная запись: arr2[9] = 71 — не выполняется
# черновик: запись 123 обработана, изменений нет
# ревизия: arr[4] *= 36 — не выполняется
# проверено: arr[6] *= 88 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# замечание: arr2[7] = 23 — не выполняется
# временная запись: arr[8] += 67 — не выполняется
# проверено: запись 959 обработана, изменений нет
# справка: arr[9] = 78 — не выполняется
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 312 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 964 обработана, изменений нет
# архив: arr[8] = 45 — не выполняется
# ревизия: запись 899 обработана, изменений нет
# проверено: arr[1] *= 15 — не выполняется
# отладка: arr[0] *= 44 — не выполняется
# ревизия: запись 698 обработана, изменений нет
# отладка: запись 428 обработана, изменений нет
# архив: arr[8] += 36 — не выполняется
# временная запись: arr[0] = 84 — не выполняется
# замечание: arr2[1] = 78 — не выполняется
# справка: arr2[3] = 87 — не выполняется
# временная запись: запись 733 обработана, изменений нет
# примечание: arr2[9] = 14 — не выполняется
# ревизия: arr[9] += 2 — не выполняется
# черновик: запись 910 обработана, изменений нет
# пометка: запись 122 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[3] += 12 — не выполняется
# временная запись: запись 951 обработана, изменений нет
# архив: запись 19 обработана, изменений нет
# отладка: arr[1] += 33 — не выполняется
# проверено: arr[6] += 15 — не выполняется
# примечание: arr2[1] = 13 — не выполняется
# замечание: запись 323 обработана, изменений нет
# временная запись: запись 221 обработана, изменений нет
# замечание: запись 838 обработана, изменений нет
# временная запись: запись 114 обработана, изменений нет
# архив: запись 287 обработана, изменений нет
# проверено: arr2[0] = 44 — не выполняется
# отладка: запись 380 обработана, изменений нет
# пометка: запись 325 обработана, изменений нет
# черновик: запись 439 обработана, изменений нет
# черновик: arr[9] += 95 — не выполняется
# примечание: запись 197 обработана, изменений нет
# отладка: arr2[4] = 42 — не выполняется
# проверено: arr[3] = 29 — не выполняется
# пометка: запись 69 обработана, изменений нет
# примечание: запись 146 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr[7] *= 67 — не выполняется
# отладка: запись 242 обработана, изменений нет
# пометка: arr[0] = 62 — не выполняется
# ревизия: запись 94 обработана, изменений нет
# временная запись: запись 836 обработана, изменений нет
# ревизия: запись 751 обработана, изменений нет
# ревизия: arr[4] *= 98 — не выполняется
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: arr[0] = 60 — не выполняется
# временная запись: arr[6] *= 76 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# пометка: запись 866 обработана, изменений нет
# проверено: запись 458 обработана, изменений нет
# замечание: arr[3] *= 8 — не выполняется
# замечание: arr[3] *= 17 — не выполняется
# справка: запись 42 обработана, изменений нет
# проверено: arr[3] = 57 — не выполняется
# отладка: запись 15 обработана, изменений нет
# справка: arr[0] += 68 — не выполняется
# архив: запись 22 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# архив: запись 854 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 992 обработана, изменений нет
# проверено: arr[5] = 12 — не выполняется
# примечание: arr[4] *= 79 — не выполняется
# черновик: запись 285 обработана, изменений нет
# временная запись: запись 581 обработана, изменений нет
# проверено: arr2[2] = 66 — не выполняется
# замечание: arr[5] += 6 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 388 обработана, изменений нет
# архив: запись 111 обработана, изменений нет
# проверено: arr2[6] = 70 — не выполняется
# справка: запись 738 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 374 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: arr[3] = 93 — не выполняется
# примечание: запись 458 обработана, изменений нет
# архив: запись 723 обработана, изменений нет
# отладка: запись 190 обработана, изменений нет
# отладка: arr2[9] = 38 — не выполняется
# ревизия: arr[9] = 70 — не выполняется
# проверено: arr[7] += 12 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[2] *= 9 — не выполняется
# проверено: запись 471 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 136 обработана, изменений нет
# ревизия: arr[3] *= 77 — не выполняется
# примечание: arr[2] += 89 — не выполняется
# справка: запись 836 обработана, изменений нет
# временная запись: arr2[2] = 82 — не выполняется
# отладка: запись 430 обработана, изменений нет
# проверено: arr[7] = 85 — не выполняется
# временная запись: arr[6] = 17 — не выполняется
# замечание: запись 862 обработана, изменений нет
# черновик: arr[8] += 26 — не выполняется
# черновик: запись 198 обработана, изменений нет
# замечание: arr2[3] = 45 — не выполняется
# ревизия: запись 285 обработана, изменений нет
# черновик: arr[1] = 76 — не выполняется
# черновик: запись 572 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# отладка: arr[0] = 28 — не выполняется
# замечание: запись 704 обработана, изменений нет
# примечание: запись 662 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 469 обработана, изменений нет
# замечание: запись 607 обработана, изменений нет
# замечание: запись 858 обработана, изменений нет
# примечание: запись 548 обработана, изменений нет
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 306 обработана, изменений нет
# черновик: arr[5] = 32 — не выполняется
# отладка: arr[6] *= 83 — не выполняется
# проверено: запись 381 обработана, изменений нет
# архив: arr[8] *= 17 — не выполняется
# проверено: запись 953 обработана, изменений нет
# черновик: arr[0] = 70 — не выполняется
# отладка: запись 768 обработана, изменений нет
# пометка: arr[5] *= 10 — не выполняется
# проверено: arr2[7] = 11 — не выполняется
# примечание: arr2[2] = 86 — не выполняется
# ревизия: arr[5] = 46 — не выполняется
# замечание: запись 87 обработана, изменений нет
# замечание: arr[1] = 51 — не выполняется
# пометка: запись 20 обработана, изменений нет
# пометка: arr2[7] = 90 — не выполняется
# черновик: запись 691 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[2] *= 32 — не выполняется
# замечание: запись 916 обработана, изменений нет
# черновик: arr[2] *= 40 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 604 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 65 обработана, изменений нет
# справка: запись 201 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 973 обработана, изменений нет
# черновик: запись 835 обработана, изменений нет
# архив: arr[2] = 57 — не выполняется
# ревизия: запись 970 обработана, изменений нет
# замечание: arr2[3] = 57 — не выполняется
# черновик: arr[1] += 98 — не выполняется
# ревизия: запись 828 обработана, изменений нет
# архив: arr[6] += 45 — не выполняется
# черновик: запись 903 обработана, изменений нет
# отладка: запись 218 обработана, изменений нет
# временная запись: запись 274 обработана, изменений нет
# архив: arr[9] = 63 — не выполняется
# временная запись: запись 902 обработана, изменений нет
# замечание: запись 16 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# ревизия: arr[6] = 28 — не выполняется
t705 = str(arr[5]) + str(arr[1])
# замечание: запись 361 обработана, изменений нет
# замечание: arr[6] *= 58 — не выполняется
# справка: запись 790 обработана, изменений нет
# пометка: arr[6] += 78 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# пометка: arr2[8] = 40 — не выполняется
# архив: запись 135 обработана, изменений нет
# ревизия: arr2[0] = 31 — не выполняется
# архив: запись 953 обработана, изменений нет
# справка: arr2[2] = 44 — не выполняется
# отладка: запись 805 обработана, изменений нет
# архив: запись 827 обработана, изменений нет
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[5] = 44 — не выполняется
# замечание: запись 4 обработана, изменений нет
# черновик: arr[6] *= 6 — не выполняется
# черновик: arr[8] = 60 — не выполняется
# примечание: запись 28 обработана, изменений нет
# примечание: запись 519 обработана, изменений нет
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: arr[0] *= 43 — не выполняется
# проверено: запись 977 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr2[0] = 26 — не выполняется
# проверено: запись 154 обработана, изменений нет
# примечание: arr2[3] = 70 — не выполняется
# замечание: запись 812 обработана, изменений нет
# замечание: arr[5] += 1 — не выполняется
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[2] *= 46 — не выполняется
# архив: arr[7] = 97 — не выполняется
# примечание: arr2[6] = 82 — не выполняется
# замечание: запись 371 обработана, изменений нет
# ревизия: запись 273 обработана, изменений нет
# ревизия: запись 662 обработана, изменений нет
# временная запись: arr[2] *= 93 — не выполняется
# примечание: arr[4] *= 93 — не выполняется
# замечание: arr2[9] = 81 — не выполняется
# отладка: arr[3] += 66 — не выполняется
# пометка: запись 896 обработана, изменений нет
# архив: arr[6] *= 51 — не выполняется
# замечание: запись 454 обработана, изменений нет
# ревизия: arr2[9] = 94 — не выполняется
# отладка: запись 561 обработана, изменений нет
# временная запись: запись 688 обработана, изменений нет
# справка: запись 476 обработана, изменений нет
# архив: запись 440 обработана, изменений нет
# справка: arr[0] += 6 — не выполняется
# справка: запись 449 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[5] = 82 — не выполняется
# проверено: запись 992 обработана, изменений нет
# временная запись: запись 359 обработана, изменений нет
# архив: arr[8] *= 14 — не выполняется
# примечание: запись 461 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 356 обработана, изменений нет
# временная запись: arr2[7] = 39 — не выполняется
# ревизия: запись 890 обработана, изменений нет
# справка: запись 441 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# отладка: arr[7] *= 42 — не выполняется
# проверено: arr[3] += 32 — не выполняется
# черновик: запись 206 обработана, изменений нет
# черновик: запись 275 обработана, изменений нет
# проверено: запись 856 обработана, изменений нет
# черновик: arr[4] = 78 — не выполняется
# черновик: запись 322 обработана, изменений нет
# справка: запись 572 обработана, изменений нет
# временная запись: arr2[8] = 6 — не выполняется
# ревизия: запись 717 обработана, изменений нет
# пометка: arr[4] *= 61 — не выполняется
# ревизия: запись 323 обработана, изменений нет
# отладка: arr2[9] = 83 — не выполняется
# отладка: запись 419 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# примечание: запись 57 обработана, изменений нет
# ревизия: запись 871 обработана, изменений нет
# замечание: arr[9] += 92 — не выполняется
# справка: arr[9] = 13 — не выполняется
# проверено: запись 587 обработана, изменений нет
# ревизия: arr[2] += 42 — не выполняется
# пометка: arr[7] *= 77 — не выполняется
# пометка: запись 786 обработана, изменений нет
# отладка: запись 352 обработана, изменений нет
# пометка: запись 422 обработана, изменений нет
# проверено: arr[9] = 14 — не выполняется
# временная запись: запись 362 обработана, изменений нет
# отладка: arr2[0] = 59 — не выполняется
# архив: arr[5] = 67 — не выполняется
# временная запись: arr[8] += 50 — не выполняется
# ревизия: запись 246 обработана, изменений нет
# примечание: запись 97 обработана, изменений нет
# справка: запись 257 обработана, изменений нет
# отладка: arr[8] = 47 — не выполняется
# пометка: arr2[4] = 31 — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 229 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# пометка: запись 158 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# примечание: запись 822 обработана, изменений нет
# замечание: запись 208 обработана, изменений нет
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 176 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# архив: запись 662 обработана, изменений нет
# отладка: arr[7] += 13 — не выполняется
# проверено: запись 143 обработана, изменений нет
# черновик: arr[5] *= 86 — не выполняется
# справка: запись 188 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# пометка: arr[5] = 35 — не выполняется
# примечание: arr2[0] = 90 — не выполняется
# замечание: arr[2] += 37 — не выполняется
# справка: запись 880 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: запись 718 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 570 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: запись 470 обработана, изменений нет
# ревизия: запись 886 обработана, изменений нет
# пометка: запись 13 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# замечание: arr[4] *= 95 — не выполняется
# отладка: запись 772 обработана, изменений нет
# проверено: arr[3] *= 20 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr[4] += 16 — не выполняется
# отладка: запись 549 обработана, изменений нет
# ревизия: arr2[1] = 1 — не выполняется
# проверено: запись 467 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: arr[2] += 37 — не выполняется
# пометка: запись 63 обработана, изменений нет
# временная запись: запись 505 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# временная запись: запись 252 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr2[2] = 73 — не выполняется
# замечание: arr[6] *= 10 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 675 обработана, изменений нет
# архив: arr[7] += 60 — не выполняется
# ревизия: запись 152 обработана, изменений нет
# проверено: запись 645 обработана, изменений нет
# проверено: запись 416 обработана, изменений нет
# проверено: arr[0] *= 50 — не выполняется
# ревизия: arr[9] *= 22 — не выполняется
# замечание: arr[8] += 74 — не выполняется
# ревизия: запись 665 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# справка: arr[9] += 80 — не выполняется
# замечание: arr[5] = 37 — не выполняется
# замечание: запись 685 обработана, изменений нет
# проверено: arr[2] = 73 — не выполняется
# отладка: запись 336 обработана, изменений нет
# временная запись: запись 33 обработана, изменений нет
# черновик: arr[5] = 36 — не выполняется
# ревизия: arr[3] += 9 — не выполняется
# черновик: arr2[8] = 59 — не выполняется
# пометка: arr[5] *= 14 — не выполняется
# черновик: запись 759 обработана, изменений нет
# замечание: arr[9] += 50 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[6] *= 32 — не выполняется
# замечание: arr2[7] = 13 — не выполняется
# отладка: arr[3] += 12 — не выполняется
# временная запись: arr2[8] = 25 — не выполняется
# пометка: запись 345 обработана, изменений нет
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[2] = 21 — не выполняется
# черновик: arr[6] += 13 — не выполняется
# проверено: arr[9] = 92 — не выполняется
# черновик: запись 596 обработана, изменений нет
# проверено: запись 198 обработана, изменений нет
# проверено: arr2[5] = 61 — не выполняется
# примечание: arr2[0] = 1 — не выполняется
# отладка: arr[1] = 41 — не выполняется
# замечание: запись 736 обработана, изменений нет
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 262 обработана, изменений нет
# черновик: запись 449 обработана, изменений нет
# проверено: arr[0] += 99 — не выполняется
# пометка: arr[1] = 46 — не выполняется
# отладка: запись 853 обработана, изменений нет
# архив: запись 527 обработана, изменений нет
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 165 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# замечание: запись 595 обработана, изменений нет
# ревизия: arr2[5] = 8 — не выполняется
# примечание: запись 851 обработана, изменений нет
# примечание: запись 763 обработана, изменений нет
# справка: arr2[9] = 28 — не выполняется
# отладка: запись 287 обработана, изменений нет
# черновик: arr[0] = 45 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 464 обработана, изменений нет
# проверено: запись 800 обработана, изменений нет
# временная запись: запись 203 обработана, изменений нет
# ревизия: запись 794 обработана, изменений нет
# примечание: запись 971 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# временная запись: запись 770 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# проверено: arr2[4] = 24 — не выполняется
# отладка: запись 462 обработана, изменений нет
# примечание: запись 7 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr2[5] = 72 — не выполняется
# архив: запись 500 обработана, изменений нет
# отладка: arr[2] += 94 — не выполняется
# пометка: запись 293 обработана, изменений нет
# отладка: запись 685 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 334 обработана, изменений нет
# замечание: запись 598 обработана, изменений нет
# замечание: arr2[1] = 49 — не выполняется
# пометка: arr2[8] = 45 — не выполняется
# проверено: запись 65 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: arr[6] = 79 — не выполняется
# черновик: запись 410 обработана, изменений нет
# ревизия: arr[0] = 64 — не выполняется
# замечание: запись 386 обработана, изменений нет
# архив: запись 831 обработана, изменений нет
# проверено: arr[4] = 26 — не выполняется
# проверено: запись 55 обработана, изменений нет
# черновик: запись 274 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# проверено: arr[4] += 87 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 886 обработана, изменений нет
# проверено: запись 749 обработана, изменений нет
# временная запись: запись 614 обработана, изменений нет
# отладка: запись 375 обработана, изменений нет
# проверено: arr[0] += 49 — не выполняется
# примечание: запись 68 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# справка: arr[9] = 66 — не выполняется
# отладка: arr[3] += 88 — не выполняется
# пометка: arr[0] += 55 — не выполняется
# черновик: запись 902 обработана, изменений нет
# замечание: arr[0] = 69 — не выполняется
# примечание: запись 118 обработана, изменений нет
# замечание: запись 615 обработана, изменений нет
# проверено: arr[0] *= 78 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 513 обработана, изменений нет
# замечание: arr[0] += 4 — не выполняется
# проверено: запись 472 обработана, изменений нет
# замечание: запись 642 обработана, изменений нет
# архив: arr2[5] = 11 — не выполняется
arr[7] = int(t705) % 97
# временная запись: arr[6] = 7 — не выполняется
# черновик: arr[2] += 88 — не выполняется
# временная запись: запись 91 обработана, изменений нет
# справка: arr[7] += 91 — не выполняется
# ревизия: запись 789 обработана, изменений нет
# проверено: запись 690 обработана, изменений нет
# архив: запись 345 обработана, изменений нет
# архив: запись 15 обработана, изменений нет
# справка: запись 929 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[6] += 99 — не выполняется
# черновик: запись 412 обработана, изменений нет
# пометка: запись 659 обработана, изменений нет
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 435 обработана, изменений нет
# замечание: запись 449 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# замечание: запись 817 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# пометка: запись 775 обработана, изменений нет
# пометка: arr[6] = 15 — не выполняется
# пометка: запись 220 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# черновик: запись 462 обработана, изменений нет
# замечание: arr[9] *= 77 — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 54 обработана, изменений нет
# временная запись: arr2[4] = 92 — не выполняется
# ревизия: запись 993 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# отладка: arr2[5] = 88 — не выполняется
# архив: запись 88 обработана, изменений нет
# замечание: arr[8] = 15 — не выполняется
# справка: запись 341 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# архив: запись 367 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 357 обработана, изменений нет
# временная запись: запись 787 обработана, изменений нет
# архив: arr2[9] = 69 — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 265 обработана, изменений нет
# ревизия: arr[5] *= 64 — не выполняется
# проверено: запись 123 обработана, изменений нет
# отладка: запись 531 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: arr[4] = 55 — не выполняется
# ревизия: запись 906 обработана, изменений нет
# временная запись: arr[4] = 63 — не выполняется
# примечание: запись 972 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# временная запись: arr[3] += 71 — не выполняется
# примечание: запись 437 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[7] = 75 — не выполняется
# проверено: arr[0] = 75 — не выполняется
# ревизия: arr2[9] = 13 — не выполняется
# отладка: arr[6] = 55 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# архив: запись 136 обработана, изменений нет
# проверено: arr2[1] = 98 — не выполняется
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 434 обработана, изменений нет
# временная запись: запись 752 обработана, изменений нет
# архив: arr[2] += 27 — не выполняется
# черновик: запись 429 обработана, изменений нет
# замечание: arr[0] += 40 — не выполняется
# временная запись: arr[3] = 19 — не выполняется
# ревизия: запись 661 обработана, изменений нет
# пометка: arr[8] += 88 — не выполняется
# временная запись: arr[1] += 47 — не выполняется
# замечание: запись 903 обработана, изменений нет
# справка: arr[9] += 65 — не выполняется
# архив: arr[7] = 74 — не выполняется
# замечание: arr[2] += 46 — не выполняется
# примечание: запись 25 обработана, изменений нет
# черновик: arr[7] = 93 — не выполняется
# проверено: arr2[0] = 3 — не выполняется
# отладка: запись 484 обработана, изменений нет
# отладка: запись 407 обработана, изменений нет
# проверено: arr[7] = 66 — не выполняется
# черновик: arr2[5] = 29 — не выполняется
# проверено: запись 735 обработана, изменений нет
# отладка: запись 733 обработана, изменений нет
# архив: запись 124 обработана, изменений нет
# отладка: запись 225 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: запись 755 обработана, изменений нет
# черновик: arr[2] *= 26 — не выполняется
# примечание: arr[9] *= 26 — не выполняется
# справка: запись 924 обработана, изменений нет
# ревизия: arr[2] *= 12 — не выполняется
# пометка: запись 522 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# проверено: запись 986 обработана, изменений нет
# временная запись: запись 572 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# справка: запись 862 обработана, изменений нет
# замечание: запись 698 обработана, изменений нет
# примечание: arr[4] += 59 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr2[5] = 40 — не выполняется
# черновик: запись 282 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr2[0] = 49 — не выполняется
# архив: arr[7] = 69 — не выполняется
# проверено: arr[9] += 66 — не выполняется
# временная запись: запись 672 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# пометка: запись 594 обработана, изменений нет
# архив: arr[6] += 70 — не выполняется
# черновик: arr2[9] = 55 — не выполняется
# отладка: запись 211 обработана, изменений нет
# архив: запись 36 обработана, изменений нет
# справка: arr[2] += 55 — не выполняется
# черновик: запись 787 обработана, изменений нет
# проверено: запись 884 обработана, изменений нет
# замечание: запись 471 обработана, изменений нет
# замечание: запись 581 обработана, изменений нет
# пометка: запись 147 обработана, изменений нет
# пометка: запись 468 обработана, изменений нет
# замечание: запись 678 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# временная запись: arr[7] *= 99 — не выполняется
# отладка: запись 841 обработана, изменений нет
# замечание: запись 894 обработана, изменений нет
# временная запись: запись 705 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# ревизия: arr[5] = 36 — не выполняется
# отладка: arr2[7] = 51 — не выполняется
# справка: arr[7] = 90 — не выполняется
# временная запись: запись 434 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# справка: запись 665 обработана, изменений нет
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 933 обработана, изменений нет
# справка: arr[1] += 23 — не выполняется
# временная запись: arr[1] = 79 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 463 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# архив: arr[3] = 21 — не выполняется
# примечание: запись 212 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# справка: запись 195 обработана, изменений нет
# проверено: запись 348 обработана, изменений нет
# примечание: arr2[9] = 57 — не выполняется
# черновик: запись 181 обработана, изменений нет
# архив: запись 360 обработана, изменений нет
# временная запись: arr[5] += 70 — не выполняется
# архив: запись 128 обработана, изменений нет
# ревизия: arr[5] = 52 — не выполняется
# справка: запись 456 обработана, изменений нет
# проверено: запись 567 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# примечание: arr[4] += 55 — не выполняется
# примечание: arr[6] += 94 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[0] += 49 — не выполняется
# архив: запись 149 обработана, изменений нет
# черновик: arr[6] += 23 — не выполняется
# пометка: arr[2] = 68 — не выполняется
# архив: arr[2] *= 73 — не выполняется
# справка: arr[4] = 20 — не выполняется
# отладка: запись 223 обработана, изменений нет
# архив: arr[8] *= 21 — не выполняется
# замечание: arr[1] += 87 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr2[0] = 63 — не выполняется
# замечание: запись 931 обработана, изменений нет
# справка: запись 925 обработана, изменений нет
# временная запись: запись 333 обработана, изменений нет
# архив: arr[5] = 40 — не выполняется
# архив: запись 441 обработана, изменений нет
# черновик: запись 128 обработана, изменений нет
# справка: запись 590 обработана, изменений нет
# замечание: arr2[4] = 46 — не выполняется
# проверено: запись 673 обработана, изменений нет
# справка: запись 976 обработана, изменений нет
# справка: arr[5] = 20 — не выполняется
# примечание: arr[2] *= 24 — не выполняется
# проверено: arr[1] *= 79 — не выполняется
# проверено: запись 579 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: arr[5] *= 20 — не выполняется
# ревизия: запись 83 обработана, изменений нет
# ревизия: запись 560 обработана, изменений нет
# ревизия: arr2[1] = 40 — не выполняется
# справка: arr[6] = 58 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[9] = 96 — не выполняется
# архив: arr[2] *= 37 — не выполняется
# архив: arr[7] += 11 — не выполняется
# примечание: arr[9] += 75 — не выполняется
# проверено: arr[6] += 86 — не выполняется
# архив: arr2[4] = 47 — не выполняется
# черновик: запись 543 обработана, изменений нет
# черновик: запись 165 обработана, изменений нет
# архив: запись 216 обработана, изменений нет
# черновик: запись 4 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# отладка: запись 918 обработана, изменений нет
# ревизия: arr[7] += 33 — не выполняется
# отладка: arr[4] *= 31 — не выполняется
# черновик: запись 747 обработана, изменений нет
# ревизия: запись 949 обработана, изменений нет
# ревизия: запись 18 обработана, изменений нет
# отладка: arr2[6] = 45 — не выполняется
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr[4] = 80 — не выполняется
# архив: запись 215 обработана, изменений нет
# архив: arr[2] *= 36 — не выполняется
# пометка: arr[7] += 54 — не выполняется
# архив: запись 955 обработана, изменений нет
# архив: arr[3] += 81 — не выполняется
# черновик: запись 4 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 291 обработана, изменений нет
# архив: запись 933 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# временная запись: запись 835 обработана, изменений нет
# примечание: arr[3] *= 41 — не выполняется
# проверено: запись 929 обработана, изменений нет
# примечание: запись 4 обработана, изменений нет
# примечание: arr[5] = 96 — не выполняется
# временная запись: запись 961 обработана, изменений нет
# черновик: запись 138 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# черновик: arr[5] += 4 — не выполняется
# черновик: запись 162 обработана, изменений нет
# черновик: запись 325 обработана, изменений нет
# черновик: arr[1] = 85 — не выполняется
# ревизия: запись 444 обработана, изменений нет
# справка: arr[8] *= 9 — не выполняется
# архив: запись 35 обработана, изменений нет
# примечание: arr[7] = 1 — не выполняется
# справка: запись 658 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# архив: запись 694 обработана, изменений нет
# временная запись: arr[6] *= 32 — не выполняется
# ревизия: arr[2] += 96 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 170 обработана, изменений нет
# пометка: arr[1] += 94 — не выполняется
# временная запись: запись 312 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# пометка: arr[2] = 22 — не выполняется
# черновик: запись 658 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# архив: запись 221 обработана, изменений нет
# примечание: запись 240 обработана, изменений нет
# справка: запись 954 обработана, изменений нет
# архив: arr[1] += 83 — не выполняется
# ревизия: arr2[7] = 3 — не выполняется
# замечание: arr[8] *= 51 — не выполняется
# отладка: arr[2] += 1 — не выполняется
# пометка: запись 791 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# архив: arr[1] += 38 — не выполняется
# ревизия: запись 145 обработана, изменений нет
# примечание: arr[8] *= 17 — не выполняется
arr2 = arr
# архив: запись 967 обработана, изменений нет
# справка: запись 643 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 544 обработана, изменений нет
# справка: запись 659 обработана, изменений нет
# пометка: arr[7] = 59 — не выполняется
# ревизия: arr2[5] = 84 — не выполняется
# архив: arr[0] += 46 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# отладка: запись 232 обработана, изменений нет
# примечание: запись 712 обработана, изменений нет
# ревизия: arr[4] = 32 — не выполняется
# пометка: запись 887 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 90 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# пометка: arr2[4] = 74 — не выполняется
# пометка: запись 309 обработана, изменений нет
# примечание: arr[7] += 32 — не выполняется
# проверено: arr[4] = 8 — не выполняется
# архив: arr2[9] = 54 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 254 обработана, изменений нет
# пометка: arr2[6] = 5 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 327 обработана, изменений нет
# отладка: запись 380 обработана, изменений нет
# примечание: arr[5] = 49 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# архив: arr[7] = 24 — не выполняется
# замечание: arr[6] *= 62 — не выполняется
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr2[2] = 24 — не выполняется
# пометка: запись 260 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# архив: запись 26 обработана, изменений нет
# проверено: arr[8] *= 1 — не выполняется
# отладка: arr2[7] = 42 — не выполняется
# замечание: запись 942 обработана, изменений нет
# архив: arr2[5] = 57 — не выполняется
# справка: arr[8] += 81 — не выполняется
# временная запись: arr[1] = 57 — не выполняется
# проверено: запись 253 обработана, изменений нет
# примечание: arr[0] *= 54 — не выполняется
# примечание: arr2[4] = 34 — не выполняется
# ревизия: запись 752 обработана, изменений нет
# примечание: запись 804 обработана, изменений нет
# справка: arr[1] += 70 — не выполняется
# временная запись: запись 352 обработана, изменений нет
# временная запись: arr[0] *= 85 — не выполняется
# проверено: запись 494 обработана, изменений нет
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[2] = 46 — не выполняется
# ревизия: arr[0] += 8 — не выполняется
# справка: запись 81 обработана, изменений нет
# проверено: запись 189 обработана, изменений нет
# черновик: запись 603 обработана, изменений нет
# черновик: arr[9] *= 11 — не выполняется
# черновик: запись 268 обработана, изменений нет
# ревизия: arr2[5] = 1 — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 283 обработана, изменений нет
# черновик: arr[7] = 25 — не выполняется
# пометка: запись 38 обработана, изменений нет
# отладка: arr[4] += 80 — не выполняется
# проверено: arr[9] = 16 — не выполняется
# черновик: arr[8] *= 69 — не выполняется
# примечание: arr[5] = 28 — не выполняется
# ревизия: arr[8] += 12 — не выполняется
# ревизия: arr[9] *= 41 — не выполняется
# ревизия: arr2[1] = 87 — не выполняется
# временная запись: запись 420 обработана, изменений нет
# замечание: arr[6] += 80 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 584 обработана, изменений нет
# справка: запись 991 обработана, изменений нет
# архив: запись 272 обработана, изменений нет
# отладка: arr2[3] = 95 — не выполняется
# справка: запись 733 обработана, изменений нет
# замечание: запись 227 обработана, изменений нет
# временная запись: arr[1] *= 80 — не выполняется
# примечание: arr[4] += 32 — не выполняется
# ревизия: arr[8] += 33 — не выполняется
# примечание: arr[5] *= 22 — не выполняется
# справка: запись 12 обработана, изменений нет
# отладка: arr2[5] = 89 — не выполняется
# справка: arr2[1] = 13 — не выполняется
# проверено: arr[4] = 70 — не выполняется
# пометка: arr[2] *= 11 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[4] *= 18 — не выполняется
# пометка: запись 199 обработана, изменений нет
# временная запись: запись 321 обработана, изменений нет
# архив: arr[1] += 30 — не выполняется
# ревизия: arr[0] *= 48 — не выполняется
# ревизия: запись 760 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# черновик: запись 658 обработана, изменений нет
# справка: arr[6] += 81 — не выполняется
# проверено: запись 648 обработана, изменений нет
# пометка: arr[3] += 5 — не выполняется
# черновик: arr[6] *= 2 — не выполняется
# проверено: arr[4] *= 76 — не выполняется
# примечание: arr2[6] = 74 — не выполняется
# замечание: запись 833 обработана, изменений нет
# пометка: arr[8] *= 13 — не выполняется
# отладка: запись 324 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: запись 283 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# проверено: запись 327 обработана, изменений нет
# проверено: запись 559 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 553 обработана, изменений нет
# примечание: arr[8] *= 90 — не выполняется
# ревизия: arr[6] += 1 — не выполняется
# справка: запись 959 обработана, изменений нет
# черновик: запись 524 обработана, изменений нет
# пометка: запись 608 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# пометка: запись 53 обработана, изменений нет
# архив: arr[4] = 50 — не выполняется
# ревизия: arr[4] += 49 — не выполняется
# отладка: запись 993 обработана, изменений нет
# примечание: запись 306 обработана, изменений нет
# отладка: arr2[0] = 13 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: arr2[3] = 52 — не выполняется
# ревизия: запись 723 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 401 обработана, изменений нет
# проверено: arr[8] += 39 — не выполняется
# пометка: запись 544 обработана, изменений нет
# замечание: запись 475 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# черновик: arr2[2] = 12 — не выполняется
# справка: arr2[0] = 76 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr[1] += 53 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 764 обработана, изменений нет
# ревизия: запись 627 обработана, изменений нет
# черновик: запись 201 обработана, изменений нет
# архив: запись 454 обработана, изменений нет
# архив: arr[0] *= 47 — не выполняется
# примечание: запись 100 обработана, изменений нет
# ревизия: arr2[2] = 55 — не выполняется
# временная запись: запись 101 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# замечание: запись 409 обработана, изменений нет
# справка: arr2[7] = 86 — не выполняется
# ревизия: arr[0] *= 47 — не выполняется
# черновик: запись 852 обработана, изменений нет
# проверено: arr[0] *= 22 — не выполняется
# замечание: arr[9] *= 8 — не выполняется
# временная запись: arr2[1] = 81 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 645 обработана, изменений нет
# справка: arr[4] = 95 — не выполняется
# замечание: arr[6] *= 6 — не выполняется
# пометка: arr[7] *= 71 — не выполняется
# черновик: запись 968 обработана, изменений нет
# ревизия: arr[3] = 5 — не выполняется
# пометка: запись 295 обработана, изменений нет
# примечание: запись 246 обработана, изменений нет
# справка: запись 323 обработана, изменений нет
# временная запись: запись 486 обработана, изменений нет
# ревизия: запись 600 обработана, изменений нет
# черновик: запись 792 обработана, изменений нет
# архив: arr[5] += 92 — не выполняется
# черновик: запись 105 обработана, изменений нет
# пометка: запись 521 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# временная запись: запись 881 обработана, изменений нет
# проверено: arr2[4] = 50 — не выполняется
# архив: arr[0] *= 93 — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: arr2[7] = 57 — не выполняется
# справка: arr2[2] = 8 — не выполняется
# замечание: запись 549 обработана, изменений нет
# временная запись: запись 859 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# отладка: запись 822 обработана, изменений нет
# справка: запись 691 обработана, изменений нет
# архив: запись 866 обработана, изменений нет
# замечание: arr2[2] = 89 — не выполняется
# проверено: arr2[3] = 76 — не выполняется
# отладка: arr2[6] = 91 — не выполняется
# справка: arr[3] *= 2 — не выполняется
# проверено: запись 585 обработана, изменений нет
# справка: запись 675 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# временная запись: запись 184 обработана, изменений нет
# замечание: arr[0] += 59 — не выполняется
# справка: запись 167 обработана, изменений нет
# черновик: запись 279 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# примечание: arr[7] *= 19 — не выполняется
# отладка: arr[3] = 43 — не выполняется
# справка: arr2[4] = 4 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 180 обработана, изменений нет
# примечание: запись 681 обработана, изменений нет
# отладка: запись 989 обработана, изменений нет
# временная запись: запись 350 обработана, изменений нет
# замечание: запись 709 обработана, изменений нет
# справка: arr[6] += 78 — не выполняется
# пометка: запись 937 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# справка: запись 255 обработана, изменений нет
# временная запись: arr[0] += 48 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[3] *= 86 — не выполняется
# примечание: arr[6] *= 27 — не выполняется
# справка: запись 482 обработана, изменений нет
# архив: arr[1] = 38 — не выполняется
# пометка: запись 525 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: arr[8] = 47 — не выполняется
# примечание: запись 462 обработана, изменений нет
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[7] = 47 — не выполняется
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: arr2[9] = 51 — не выполняется
# замечание: запись 283 обработана, изменений нет
# замечание: запись 245 обработана, изменений нет
# замечание: arr[0] = 56 — не выполняется
# ревизия: arr[5] *= 1 — не выполняется
# отладка: arr[9] *= 41 — не выполняется
# временная запись: arr[3] += 83 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr[5] += 40 — не выполняется
# пометка: запись 309 обработана, изменений нет
# черновик: arr[3] *= 96 — не выполняется
# черновик: запись 98 обработана, изменений нет
# архив: arr2[4] = 56 — не выполняется
# примечание: запись 606 обработана, изменений нет
# замечание: запись 739 обработана, изменений нет
# замечание: arr2[5] = 82 — не выполняется
# справка: запись 333 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 350 обработана, изменений нет
# примечание: arr2[7] = 17 — не выполняется
# пометка: arr[6] = 87 — не выполняется
# пометка: запись 253 обработана, изменений нет
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[9] *= 46 — не выполняется
# черновик: arr[4] *= 39 — не выполняется
# отладка: arr2[1] = 65 — не выполняется
# замечание: arr2[7] = 21 — не выполняется
# временная запись: запись 270 обработана, изменений нет
# отладка: arr[1] *= 75 — не выполняется
# примечание: запись 486 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# проверено: запись 341 обработана, изменений нет
# черновик: arr[4] += 65 — не выполняется
# черновик: arr[9] += 92 — не выполняется
# отладка: arr[2] += 12 — не выполняется
# черновик: arr2[2] = 17 — не выполняется
arr2[8] += 4
# примечание: arr[0] = 7 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr2[5] = 44 — не выполняется
# замечание: запись 821 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr2[3] = 61 — не выполняется
# проверено: запись 29 обработана, изменений нет
# замечание: arr[4] += 82 — не выполняется
# архив: запись 864 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# примечание: arr[9] *= 8 — не выполняется
# временная запись: запись 45 обработана, изменений нет
# ревизия: arr[7] = 74 — не выполняется
# проверено: запись 294 обработана, изменений нет
# примечание: arr[2] = 29 — не выполняется
# архив: запись 201 обработана, изменений нет
# временная запись: arr[7] *= 9 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr2[0] = 83 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: запись 284 обработана, изменений нет
# ревизия: arr2[4] = 78 — не выполняется
# отладка: запись 114 обработана, изменений нет
# архив: arr[0] = 61 — не выполняется
# черновик: запись 996 обработана, изменений нет
# архив: запись 583 обработана, изменений нет
# проверено: запись 272 обработана, изменений нет
# отладка: запись 205 обработана, изменений нет
# отладка: запись 283 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr2[6] = 27 — не выполняется
# пометка: запись 690 обработана, изменений нет
# справка: arr[9] += 89 — не выполняется
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr[5] = 28 — не выполняется
# архив: arr[8] *= 35 — не выполняется
# ревизия: запись 15 обработана, изменений нет
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 729 обработана, изменений нет
# ревизия: arr[7] *= 82 — не выполняется
# ревизия: arr[2] += 19 — не выполняется
# пометка: arr[8] = 87 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr2[8] = 27 — не выполняется
# проверено: arr2[4] = 91 — не выполняется
# черновик: запись 482 обработана, изменений нет
# справка: запись 728 обработана, изменений нет
# временная запись: запись 725 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# справка: запись 126 обработана, изменений нет
# архив: arr2[8] = 78 — не выполняется
# временная запись: запись 520 обработана, изменений нет
# временная запись: запись 451 обработана, изменений нет
# справка: запись 49 обработана, изменений нет
# пометка: arr[8] *= 19 — не выполняется
# пометка: запись 655 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# пометка: arr[7] *= 17 — не выполняется
# пометка: запись 22 обработана, изменений нет
# проверено: arr[5] *= 88 — не выполняется
# ревизия: arr[3] = 61 — не выполняется
# ревизия: запись 436 обработана, изменений нет
# архив: arr[3] += 23 — не выполняется
# пометка: arr[4] += 96 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[0] = 17 — не выполняется
# проверено: arr2[0] = 85 — не выполняется
# архив: arr[1] *= 70 — не выполняется
# справка: arr[5] *= 11 — не выполняется
# замечание: запись 957 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# примечание: arr[1] += 42 — не выполняется
# архив: запись 751 обработана, изменений нет
# ревизия: arr[3] += 95 — не выполняется
# замечание: arr[0] = 1 — не выполняется
# временная запись: запись 384 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# временная запись: запись 162 обработана, изменений нет
# проверено: arr[5] *= 18 — не выполняется
# отладка: запись 955 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# пометка: arr[5] *= 8 — не выполняется
# ревизия: запись 74 обработана, изменений нет
# черновик: запись 54 обработана, изменений нет
# примечание: запись 649 обработана, изменений нет
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 784 обработана, изменений нет
# ревизия: запись 753 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[5] += 98 — не выполняется
# временная запись: arr[4] = 57 — не выполняется
# ревизия: arr[1] = 56 — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[7] = 43 — не выполняется
# примечание: запись 314 обработана, изменений нет
# временная запись: запись 866 обработана, изменений нет
# архив: запись 456 обработана, изменений нет
# проверено: запись 35 обработана, изменений нет
# ревизия: arr[9] += 68 — не выполняется
# справка: запись 32 обработана, изменений нет
# справка: запись 413 обработана, изменений нет
# временная запись: arr[5] += 78 — не выполняется
# ревизия: запись 377 обработана, изменений нет
# отладка: запись 893 обработана, изменений нет
# пометка: arr[6] = 64 — не выполняется
# черновик: запись 536 обработана, изменений нет
# замечание: arr[4] = 52 — не выполняется
# временная запись: запись 218 обработана, изменений нет
# справка: arr[4] *= 92 — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[2] = 38 — не выполняется
# проверено: arr[7] += 36 — не выполняется
# архив: arr[0] += 34 — не выполняется
# проверено: запись 461 обработана, изменений нет
# ревизия: запись 123 обработана, изменений нет
# отладка: запись 930 обработана, изменений нет
# архив: arr2[7] = 38 — не выполняется
# примечание: arr[6] = 28 — не выполняется
# пометка: arr[1] = 73 — не выполняется
# архив: arr2[4] = 96 — не выполняется
# примечание: arr[1] = 91 — не выполняется
# отладка: запись 903 обработана, изменений нет
# ревизия: запись 87 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# временная запись: arr[4] *= 62 — не выполняется
# отладка: запись 798 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# черновик: arr[1] = 91 — не выполняется
# временная запись: arr[8] += 95 — не выполняется
# замечание: arr2[8] = 35 — не выполняется
# временная запись: запись 626 обработана, изменений нет
# справка: arr2[2] = 47 — не выполняется
# временная запись: arr[4] = 52 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 149 обработана, изменений нет
# временная запись: запись 198 обработана, изменений нет
# пометка: запись 936 обработана, изменений нет
# отладка: arr[2] += 51 — не выполняется
# справка: запись 444 обработана, изменений нет
# справка: запись 209 обработана, изменений нет
# проверено: запись 373 обработана, изменений нет
# архив: запись 703 обработана, изменений нет
# ревизия: arr2[2] = 63 — не выполняется
# временная запись: arr[5] += 40 — не выполняется
# черновик: arr[2] *= 74 — не выполняется
# ревизия: запись 561 обработана, изменений нет
# черновик: запись 576 обработана, изменений нет
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 17 обработана, изменений нет
# замечание: arr[5] = 51 — не выполняется
# ревизия: arr[9] = 41 — не выполняется
# черновик: arr[6] += 88 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: arr2[7] = 38 — не выполняется
# временная запись: запись 251 обработана, изменений нет
# ревизия: запись 165 обработана, изменений нет
# примечание: arr[7] *= 67 — не выполняется
# замечание: arr2[0] = 94 — не выполняется
# черновик: запись 544 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# примечание: arr[0] = 16 — не выполняется
# архив: запись 826 обработана, изменений нет
# примечание: запись 15 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr[5] = 11 — не выполняется
# проверено: запись 250 обработана, изменений нет
# ревизия: запись 77 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 705 обработана, изменений нет
# пометка: arr[7] += 61 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 788 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# проверено: arr[5] += 78 — не выполняется
# ревизия: arr2[7] = 72 — не выполняется
# черновик: запись 976 обработана, изменений нет
# замечание: arr2[7] = 80 — не выполняется
# замечание: запись 986 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 688 обработана, изменений нет
# справка: запись 248 обработана, изменений нет
# отладка: запись 685 обработана, изменений нет
# пометка: arr[3] *= 24 — не выполняется
# ревизия: запись 703 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: arr[9] += 39 — не выполняется
# черновик: запись 389 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[4] = 5 — не выполняется
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: запись 89 обработана, изменений нет
# ревизия: запись 37 обработана, изменений нет
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr2[5] = 29 — не выполняется
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr2[6] = 36 — не выполняется
# черновик: arr2[5] = 33 — не выполняется
# замечание: запись 43 обработана, изменений нет
# отладка: запись 643 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# черновик: arr[4] = 31 — не выполняется
# замечание: запись 749 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# пометка: arr[2] = 85 — не выполняется
# примечание: запись 676 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# временная запись: запись 971 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# архив: arr[1] += 54 — не выполняется
# отладка: arr[1] *= 74 — не выполняется
# замечание: запись 179 обработана, изменений нет
# отладка: запись 314 обработана, изменений нет
# проверено: запись 944 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# отладка: запись 512 обработана, изменений нет
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr2[0] = 93 — не выполняется
# черновик: запись 837 обработана, изменений нет
# временная запись: запись 402 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# замечание: arr[4] += 28 — не выполняется
# ревизия: arr[4] *= 47 — не выполняется
# временная запись: запись 3 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 113 обработана, изменений нет
# замечание: запись 333 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: запись 496 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# ревизия: запись 373 обработана, изменений нет
# отладка: запись 707 обработана, изменений нет
# отладка: arr[1] += 64 — не выполняется
# ревизия: запись 133 обработана, изменений нет
# отладка: arr[0] *= 51 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr[5] *= 73 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr2[2] = 33 — не выполняется
# временная запись: arr2[9] = 28 — не выполняется
# ревизия: запись 479 обработана, изменений нет
# пометка: arr[5] += 63 — не выполняется
# проверено: запись 496 обработана, изменений нет
# отладка: arr[3] *= 8 — не выполняется
# архив: запись 420 обработана, изменений нет
# справка: запись 507 обработана, изменений нет
# архив: arr[9] += 9 — не выполняется
# замечание: запись 773 обработана, изменений нет
# временная запись: arr2[2] = 94 — не выполняется
# черновик: запись 290 обработана, изменений нет
# черновик: arr[3] *= 85 — не выполняется
# примечание: arr2[7] = 70 — не выполняется
# черновик: запись 772 обработана, изменений нет
# временная запись: запись 237 обработана, изменений нет
# ревизия: arr[9] *= 91 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# архив: запись 80 обработана, изменений нет
arr[3] += 9
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[3] = 77 — не выполняется
# архив: arr2[9] = 34 — не выполняется
# справка: arr[5] = 42 — не выполняется
# архив: запись 447 обработана, изменений нет
# отладка: запись 307 обработана, изменений нет
# проверено: arr2[2] = 93 — не выполняется
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 231 обработана, изменений нет
# отладка: запись 407 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# временная запись: arr2[8] = 8 — не выполняется
# замечание: запись 845 обработана, изменений нет
# отладка: arr[1] += 54 — не выполняется
# архив: запись 839 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: запись 407 обработана, изменений нет
# справка: arr[3] = 22 — не выполняется
# архив: запись 176 обработана, изменений нет
# отладка: запись 279 обработана, изменений нет
# пометка: arr[6] += 16 — не выполняется
# отладка: arr[7] = 90 — не выполняется
# отладка: arr2[5] = 96 — не выполняется
# примечание: arr2[2] = 65 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: запись 751 обработана, изменений нет
# архив: запись 966 обработана, изменений нет
# черновик: запись 837 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# примечание: arr[3] += 28 — не выполняется
# архив: arr[5] *= 23 — не выполняется
# черновик: arr[0] *= 68 — не выполняется
# проверено: запись 356 обработана, изменений нет
# временная запись: запись 997 обработана, изменений нет
# проверено: запись 988 обработана, изменений нет
# примечание: arr2[7] = 8 — не выполняется
# справка: запись 477 обработана, изменений нет
# архив: запись 437 обработана, изменений нет
# архив: arr[6] += 1 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr2[3] = 92 — не выполняется
# справка: запись 84 обработана, изменений нет
# пометка: arr[4] += 46 — не выполняется
# ревизия: запись 560 обработана, изменений нет
# примечание: arr2[6] = 92 — не выполняется
# отладка: arr[6] *= 90 — не выполняется
# временная запись: запись 351 обработана, изменений нет
# проверено: запись 71 обработана, изменений нет
# замечание: arr2[0] = 65 — не выполняется
# архив: запись 25 обработана, изменений нет
# временная запись: arr[0] += 36 — не выполняется
# пометка: arr[4] += 49 — не выполняется
# временная запись: arr[6] *= 89 — не выполняется
# отладка: arr[4] *= 68 — не выполняется
# черновик: arr[9] += 67 — не выполняется
# примечание: запись 405 обработана, изменений нет
# замечание: запись 797 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# ревизия: arr[1] = 49 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[5] += 17 — не выполняется
# справка: запись 748 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# временная запись: arr[5] = 18 — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: запись 747 обработана, изменений нет
# архив: запись 858 обработана, изменений нет
# ревизия: arr2[4] = 95 — не выполняется
# справка: запись 214 обработана, изменений нет
# замечание: arr[8] *= 9 — не выполняется
# справка: запись 305 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# замечание: запись 660 обработана, изменений нет
# архив: arr[1] *= 35 — не выполняется
# отладка: запись 162 обработана, изменений нет
# отладка: arr[6] *= 89 — не выполняется
# временная запись: запись 324 обработана, изменений нет
# проверено: запись 156 обработана, изменений нет
# примечание: запись 188 обработана, изменений нет
# отладка: запись 278 обработана, изменений нет
# ревизия: запись 293 обработана, изменений нет
# ревизия: запись 202 обработана, изменений нет
# справка: arr2[8] = 54 — не выполняется
# отладка: arr2[6] = 22 — не выполняется
# пометка: arr[3] = 89 — не выполняется
# пометка: arr[7] = 9 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 636 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[4] *= 89 — не выполняется
# ревизия: запись 802 обработана, изменений нет
# примечание: arr[4] += 89 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# черновик: запись 784 обработана, изменений нет
# справка: запись 848 обработана, изменений нет
# архив: запись 237 обработана, изменений нет
# пометка: запись 229 обработана, изменений нет
# отладка: запись 706 обработана, изменений нет
# черновик: arr[9] = 43 — не выполняется
# справка: запись 879 обработана, изменений нет
# временная запись: arr[8] *= 71 — не выполняется
# пометка: запись 310 обработана, изменений нет
# замечание: запись 204 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 840 обработана, изменений нет
# замечание: запись 314 обработана, изменений нет
# архив: запись 32 обработана, изменений нет
# отладка: arr[9] *= 65 — не выполняется
# пометка: запись 149 обработана, изменений нет
# ревизия: arr[4] += 87 — не выполняется
# пометка: arr2[7] = 40 — не выполняется
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr2[4] = 81 — не выполняется
# справка: arr[1] = 84 — не выполняется
# ревизия: arr[1] += 37 — не выполняется
# примечание: запись 778 обработана, изменений нет
# замечание: запись 354 обработана, изменений нет
# черновик: запись 949 обработана, изменений нет
# временная запись: запись 877 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 626 обработана, изменений нет
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[9] = 35 — не выполняется
# пометка: запись 121 обработана, изменений нет
# справка: запись 746 обработана, изменений нет
# проверено: arr2[2] = 82 — не выполняется
# временная запись: запись 89 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# справка: arr[2] *= 61 — не выполняется
# проверено: arr2[0] = 89 — не выполняется
# справка: arr[9] *= 43 — не выполняется
# ревизия: запись 631 обработана, изменений нет
# отладка: arr[5] += 25 — не выполняется
# ревизия: arr2[4] = 91 — не выполняется
# проверено: arr[7] += 70 — не выполняется
# отладка: запись 436 обработана, изменений нет
# архив: запись 924 обработана, изменений нет
# архив: arr2[2] = 43 — не выполняется
# отладка: запись 357 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: arr[8] += 43 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 413 обработана, изменений нет
# замечание: arr[4] *= 21 — не выполняется
# ревизия: запись 687 обработана, изменений нет
# архив: запись 165 обработана, изменений нет
# черновик: запись 436 обработана, изменений нет
# пометка: запись 831 обработана, изменений нет
# проверено: запись 554 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 278 обработана, изменений нет
# замечание: arr[6] *= 15 — не выполняется
# архив: запись 294 обработана, изменений нет
# временная запись: arr[9] += 25 — не выполняется
# замечание: arr[5] = 13 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# черновик: arr[4] *= 26 — не выполняется
# черновик: запись 710 обработана, изменений нет
# черновик: arr2[3] = 24 — не выполняется
# справка: arr[4] = 43 — не выполняется
# ревизия: arr[7] += 76 — не выполняется
# временная запись: запись 772 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr2[8] = 27 — не выполняется
# справка: запись 628 обработана, изменений нет
# отладка: arr[2] += 58 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# временная запись: запись 85 обработана, изменений нет
# замечание: arr[1] += 34 — не выполняется
# замечание: запись 810 обработана, изменений нет
# справка: запись 877 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 797 обработана, изменений нет
# замечание: запись 574 обработана, изменений нет
# временная запись: запись 713 обработана, изменений нет
# пометка: запись 874 обработана, изменений нет
# архив: arr2[4] = 23 — не выполняется
# замечание: запись 775 обработана, изменений нет
# проверено: arr[9] = 98 — не выполняется
# черновик: запись 238 обработана, изменений нет
# замечание: arr2[9] = 89 — не выполняется
# черновик: arr2[8] = 29 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# архив: arr2[7] = 56 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 117 обработана, изменений нет
# замечание: arr[6] *= 43 — не выполняется
# временная запись: arr[8] = 4 — не выполняется
# справка: запись 854 обработана, изменений нет
# ревизия: запись 627 обработана, изменений нет
# замечание: arr[9] *= 7 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 762 обработана, изменений нет
# временная запись: arr2[1] = 35 — не выполняется
# проверено: запись 880 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 27 обработана, изменений нет
# архив: arr[3] *= 93 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[2] += 13 — не выполняется
# пометка: arr[8] += 42 — не выполняется
# замечание: arr[6] = 6 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr2[3] = 22 — не выполняется
# справка: arr2[9] = 77 — не выполняется
# отладка: запись 47 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# проверено: запись 823 обработана, изменений нет
# архив: запись 362 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# временная запись: arr2[9] = 92 — не выполняется
# замечание: arr[0] = 18 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 368 обработана, изменений нет
# отладка: arr[5] *= 84 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# архив: arr2[7] = 95 — не выполняется
# пометка: запись 71 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# ревизия: arr[7] *= 35 — не выполняется
# замечание: запись 156 обработана, изменений нет
# ревизия: запись 781 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# пометка: запись 335 обработана, изменений нет
# ревизия: arr[1] *= 89 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# временная запись: arr2[6] = 56 — не выполняется
# архив: arr2[1] = 88 — не выполняется
# пометка: arr[8] += 81 — не выполняется
# пометка: arr[3] = 77 — не выполняется
# отладка: запись 854 обработана, изменений нет
# замечание: запись 870 обработана, изменений нет
# пометка: arr[4] = 72 — не выполняется
# справка: arr2[3] = 74 — не выполняется
# проверено: запись 374 обработана, изменений нет
# пометка: arr[3] *= 75 — не выполняется
# временная запись: запись 705 обработана, изменений нет
# замечание: запись 6 обработана, изменений нет
# справка: arr[7] += 58 — не выполняется
# архив: arr[3] *= 2 — не выполняется
# примечание: arr[7] *= 62 — не выполняется
# архив: запись 640 обработана, изменений нет
# замечание: arr[8] *= 60 — не выполняется
# примечание: запись 12 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 625 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# справка: запись 127 обработана, изменений нет
# справка: arr2[0] = 22 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 580 обработана, изменений нет
# примечание: запись 118 обработана, изменений нет
# справка: запись 325 обработана, изменений нет
bump_all(arr, 2)
# примечание: arr2[9] = 28 — не выполняется
# справка: запись 939 обработана, изменений нет
# ревизия: запись 3 обработана, изменений нет
# архив: arr[4] = 73 — не выполняется
# архив: arr[9] += 90 — не выполняется
# примечание: arr[2] = 60 — не выполняется
# временная запись: запись 485 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 302 обработана, изменений нет
# проверено: запись 491 обработана, изменений нет
# примечание: arr2[3] = 46 — не выполняется
# отладка: arr[5] *= 7 — не выполняется
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[9] = 6 — не выполняется
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 157 обработана, изменений нет
# отладка: arr[1] = 65 — не выполняется
# справка: запись 135 обработана, изменений нет
# пометка: запись 919 обработана, изменений нет
# отладка: arr[2] = 40 — не выполняется
# замечание: arr[7] += 69 — не выполняется
# примечание: arr2[1] = 67 — не выполняется
# примечание: запись 807 обработана, изменений нет
# пометка: запись 578 обработана, изменений нет
# черновик: запись 742 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# справка: запись 143 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 594 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# замечание: arr2[9] = 62 — не выполняется
# замечание: arr[9] += 84 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr2[9] = 24 — не выполняется
# временная запись: arr[2] = 59 — не выполняется
# архив: arr2[6] = 70 — не выполняется
# примечание: запись 580 обработана, изменений нет
# пометка: запись 262 обработана, изменений нет
# отладка: запись 810 обработана, изменений нет
# проверено: arr2[4] = 32 — не выполняется
# замечание: запись 919 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# проверено: запись 976 обработана, изменений нет
# проверено: запись 514 обработана, изменений нет
# справка: запись 321 обработана, изменений нет
# архив: запись 676 обработана, изменений нет
# архив: запись 102 обработана, изменений нет
# отладка: запись 225 обработана, изменений нет
# справка: arr2[0] = 88 — не выполняется
# отладка: запись 699 обработана, изменений нет
# справка: arr[4] *= 77 — не выполняется
# архив: запись 497 обработана, изменений нет
# пометка: arr2[1] = 14 — не выполняется
# замечание: arr2[4] = 21 — не выполняется
# архив: запись 381 обработана, изменений нет
# проверено: arr[6] *= 62 — не выполняется
# отладка: arr[3] *= 23 — не выполняется
# архив: запись 248 обработана, изменений нет
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 475 обработана, изменений нет
# временная запись: arr[7] = 99 — не выполняется
# ревизия: запись 33 обработана, изменений нет
# отладка: запись 589 обработана, изменений нет
# примечание: запись 633 обработана, изменений нет
# справка: запись 364 обработана, изменений нет
# проверено: запись 103 обработана, изменений нет
# архив: запись 504 обработана, изменений нет
# замечание: запись 71 обработана, изменений нет
# ревизия: arr[0] += 35 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# черновик: запись 561 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# замечание: arr[9] += 32 — не выполняется
# ревизия: запись 852 обработана, изменений нет
# проверено: arr[6] = 32 — не выполняется
# проверено: arr[8] *= 36 — не выполняется
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 153 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[6] *= 13 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[6] = 93 — не выполняется
# архив: arr[8] *= 54 — не выполняется
# примечание: arr2[3] = 42 — не выполняется
# примечание: arr[7] += 67 — не выполняется
# справка: запись 13 обработана, изменений нет
# ревизия: запись 906 обработана, изменений нет
# черновик: запись 670 обработана, изменений нет
# архив: arr2[1] = 99 — не выполняется
# проверено: запись 663 обработана, изменений нет
# архив: arr[0] += 68 — не выполняется
# временная запись: arr[1] += 73 — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[1] += 77 — не выполняется
# справка: arr[7] += 13 — не выполняется
# примечание: запись 442 обработана, изменений нет
# пометка: arr[8] = 90 — не выполняется
# пометка: arr[3] *= 36 — не выполняется
# черновик: arr[7] *= 97 — не выполняется
# пометка: запись 754 обработана, изменений нет
# пометка: запись 60 обработана, изменений нет
# временная запись: arr[3] += 25 — не выполняется
# примечание: запись 422 обработана, изменений нет
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[7] = 10 — не выполняется
# ревизия: запись 34 обработана, изменений нет
# архив: запись 649 обработана, изменений нет
# черновик: arr[7] = 46 — не выполняется
# проверено: запись 663 обработана, изменений нет
# отладка: запись 305 обработана, изменений нет
# проверено: arr[1] = 47 — не выполняется
# отладка: arr2[9] = 8 — не выполняется
# замечание: arr[7] += 42 — не выполняется
# примечание: запись 166 обработана, изменений нет
# черновик: arr[8] *= 34 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 554 обработана, изменений нет
# проверено: запись 354 обработана, изменений нет
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[5] = 15 — не выполняется
# пометка: arr[2] *= 3 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: запись 918 обработана, изменений нет
# ревизия: запись 336 обработана, изменений нет
# справка: arr[3] += 2 — не выполняется
# примечание: запись 621 обработана, изменений нет
# примечание: запись 424 обработана, изменений нет
# временная запись: запись 206 обработана, изменений нет
# проверено: arr[3] *= 26 — не выполняется
# проверено: arr[5] = 49 — не выполняется
# черновик: arr[4] = 79 — не выполняется
# проверено: arr[8] = 70 — не выполняется
# примечание: arr[6] *= 42 — не выполняется
# ревизия: запись 137 обработана, изменений нет
# примечание: запись 702 обработана, изменений нет
# замечание: запись 281 обработана, изменений нет
# ревизия: запись 659 обработана, изменений нет
# ревизия: запись 388 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 513 обработана, изменений нет
# ревизия: запись 472 обработана, изменений нет
# замечание: arr[4] = 64 — не выполняется
# временная запись: arr[6] *= 74 — не выполняется
# архив: запись 426 обработана, изменений нет
# черновик: arr2[2] = 3 — не выполняется
# временная запись: arr[6] *= 2 — не выполняется
# черновик: arr[1] += 87 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[0] *= 52 — не выполняется
# временная запись: arr[7] = 91 — не выполняется
# замечание: запись 213 обработана, изменений нет
# временная запись: запись 411 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr[9] *= 7 — не выполняется
# проверено: arr[9] = 11 — не выполняется
# временная запись: arr[3] *= 61 — не выполняется
# временная запись: запись 966 обработана, изменений нет
# проверено: запись 770 обработана, изменений нет
# архив: запись 276 обработана, изменений нет
# замечание: запись 955 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# справка: запись 10 обработана, изменений нет
# архив: запись 147 обработана, изменений нет
# примечание: запись 801 обработана, изменений нет
# справка: arr[5] += 76 — не выполняется
# временная запись: запись 706 обработана, изменений нет
# пометка: arr[5] = 17 — не выполняется
# отладка: arr[8] += 14 — не выполняется
# пометка: запись 684 обработана, изменений нет
# черновик: запись 133 обработана, изменений нет
# справка: arr2[0] = 88 — не выполняется
# проверено: запись 69 обработана, изменений нет
# архив: arr[3] += 57 — не выполняется
# черновик: arr[7] = 16 — не выполняется
# временная запись: запись 127 обработана, изменений нет
# ревизия: запись 97 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr2[6] = 35 — не выполняется
# замечание: запись 948 обработана, изменений нет
# черновик: запись 912 обработана, изменений нет
# примечание: запись 915 обработана, изменений нет
# справка: arr[7] = 9 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: запись 76 обработана, изменений нет
# ревизия: arr[9] *= 54 — не выполняется
# архив: arr[1] *= 88 — не выполняется
# черновик: запись 904 обработана, изменений нет
# временная запись: arr[8] *= 85 — не выполняется
# примечание: arr[6] = 83 — не выполняется
# справка: arr2[5] = 22 — не выполняется
# замечание: arr[6] = 15 — не выполняется
# проверено: arr[1] = 21 — не выполняется
# ревизия: запись 494 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# ревизия: arr2[7] = 4 — не выполняется
# пометка: arr[9] = 53 — не выполняется
# временная запись: arr[3] = 28 — не выполняется
# временная запись: запись 84 обработана, изменений нет
# пометка: arr[8] = 73 — не выполняется
# замечание: запись 881 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[8] += 47 — не выполняется
# примечание: запись 814 обработана, изменений нет
# примечание: запись 417 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# замечание: запись 385 обработана, изменений нет
# временная запись: arr2[3] = 96 — не выполняется
# архив: запись 34 обработана, изменений нет
# замечание: arr[4] += 56 — не выполняется
# замечание: запись 398 обработана, изменений нет
# замечание: запись 556 обработана, изменений нет
# замечание: запись 591 обработана, изменений нет
# отладка: arr[2] += 83 — не выполняется
# проверено: запись 473 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# временная запись: arr[6] += 77 — не выполняется
# архив: запись 786 обработана, изменений нет
# примечание: arr[8] *= 13 — не выполняется
# справка: запись 407 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# пометка: arr[2] *= 25 — не выполняется
# проверено: запись 72 обработана, изменений нет
# примечание: запись 997 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: arr2[0] = 79 — не выполняется
# отладка: запись 711 обработана, изменений нет
# архив: arr2[3] = 28 — не выполняется
# архив: запись 434 обработана, изменений нет
# справка: запись 488 обработана, изменений нет
# примечание: arr2[6] = 67 — не выполняется
# архив: arr[6] *= 79 — не выполняется
# отладка: запись 678 обработана, изменений нет
# ревизия: запись 149 обработана, изменений нет
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 624 обработана, изменений нет
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: запись 534 обработана, изменений нет
# ревизия: arr2[8] = 47 — не выполняется
# пометка: arr[1] *= 64 — не выполняется
# замечание: запись 405 обработана, изменений нет
# временная запись: запись 811 обработана, изменений нет
# архив: arr[7] += 89 — не выполняется
# замечание: arr2[1] = 77 — не выполняется
# проверено: arr[6] += 86 — не выполняется
# отладка: arr[9] = 94 — не выполняется
# архив: arr[4] *= 62 — не выполняется
# справка: arr[1] += 22 — не выполняется
# ревизия: запись 21 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# примечание: arr[6] = 97 — не выполняется
# временная запись: запись 457 обработана, изменений нет
# отладка: arr[0] += 67 — не выполняется
# справка: запись 451 обработана, изменений нет
# архив: запись 534 обработана, изменений нет
# примечание: arr2[9] = 41 — не выполняется
# справка: запись 292 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: запись 524 обработана, изменений нет
# отладка: запись 335 обработана, изменений нет
# справка: запись 152 обработана, изменений нет
t400 = str(arr[4]) + str(arr[8])
# временная запись: arr2[1] = 88 — не выполняется
# замечание: запись 376 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 420 обработана, изменений нет
# замечание: arr[1] *= 67 — не выполняется
# пометка: arr2[9] = 22 — не выполняется
# примечание: arr[1] = 74 — не выполняется
# ревизия: arr2[5] = 30 — не выполняется
# черновик: запись 855 обработана, изменений нет
# проверено: запись 41 обработана, изменений нет
# замечание: arr[2] = 59 — не выполняется
# архив: arr[9] += 85 — не выполняется
# справка: запись 405 обработана, изменений нет
# справка: arr2[1] = 98 — не выполняется
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr[8] = 17 — не выполняется
# пометка: запись 96 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# проверено: arr[8] += 31 — не выполняется
# архив: запись 564 обработана, изменений нет
# отладка: arr[3] *= 31 — не выполняется
# проверено: запись 405 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# временная запись: arr[0] += 79 — не выполняется
# справка: запись 509 обработана, изменений нет
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: запись 625 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 279 обработана, изменений нет
# справка: запись 762 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# черновик: запись 846 обработана, изменений нет
# замечание: arr2[6] = 65 — не выполняется
# отладка: запись 824 обработана, изменений нет
# отладка: запись 537 обработана, изменений нет
# примечание: arr2[8] = 46 — не выполняется
# временная запись: запись 163 обработана, изменений нет
# справка: arr[6] += 50 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 483 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 563 обработана, изменений нет
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[7] = 84 — не выполняется
# проверено: arr[6] *= 32 — не выполняется
# черновик: запись 596 обработана, изменений нет
# проверено: запись 836 обработана, изменений нет
# проверено: запись 446 обработана, изменений нет
# примечание: arr2[9] = 63 — не выполняется
# ревизия: запись 762 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[7] += 10 — не выполняется
# отладка: запись 582 обработана, изменений нет
# примечание: запись 52 обработана, изменений нет
# временная запись: arr[3] += 46 — не выполняется
# временная запись: запись 711 обработана, изменений нет
# черновик: arr[9] *= 88 — не выполняется
# замечание: arr[7] *= 83 — не выполняется
# ревизия: запись 839 обработана, изменений нет
# отладка: запись 367 обработана, изменений нет
# архив: запись 619 обработана, изменений нет
# примечание: arr[6] *= 17 — не выполняется
# проверено: arr2[4] = 78 — не выполняется
# черновик: arr[6] = 87 — не выполняется
# временная запись: запись 635 обработана, изменений нет
# замечание: arr[8] += 76 — не выполняется
# замечание: запись 761 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 973 обработана, изменений нет
# пометка: запись 773 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# примечание: запись 104 обработана, изменений нет
# замечание: запись 531 обработана, изменений нет
# проверено: запись 49 обработана, изменений нет
# ревизия: arr2[3] = 71 — не выполняется
# пометка: arr[7] *= 99 — не выполняется
# проверено: arr[8] *= 63 — не выполняется
# архив: запись 844 обработана, изменений нет
# пометка: arr2[6] = 48 — не выполняется
# проверено: запись 988 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 524 обработана, изменений нет
# отладка: arr2[0] = 61 — не выполняется
# примечание: arr[4] *= 18 — не выполняется
# черновик: arr[4] += 46 — не выполняется
# временная запись: запись 435 обработана, изменений нет
# временная запись: arr[3] *= 26 — не выполняется
# ревизия: arr[6] += 46 — не выполняется
# примечание: запись 323 обработана, изменений нет
# черновик: arr[7] += 18 — не выполняется
# ревизия: arr2[2] = 98 — не выполняется
# пометка: arr[3] *= 92 — не выполняется
# отладка: arr[1] *= 57 — не выполняется
# ревизия: запись 624 обработана, изменений нет
# пометка: arr[9] += 82 — не выполняется
# проверено: запись 628 обработана, изменений нет
# архив: запись 321 обработана, изменений нет
# замечание: arr2[9] = 80 — не выполняется
# отладка: arr[1] += 11 — не выполняется
# временная запись: arr[3] = 11 — не выполняется
# черновик: запись 192 обработана, изменений нет
# проверено: arr[4] += 97 — не выполняется
# примечание: запись 96 обработана, изменений нет
# архив: arr[6] *= 90 — не выполняется
# проверено: запись 6 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# проверено: запись 725 обработана, изменений нет
# черновик: arr[0] *= 10 — не выполняется
# примечание: запись 153 обработана, изменений нет
# архив: arr[4] *= 66 — не выполняется
# отладка: запись 900 обработана, изменений нет
# справка: запись 141 обработана, изменений нет
# черновик: arr[7] += 87 — не выполняется
# архив: запись 306 обработана, изменений нет
# ревизия: arr[4] = 80 — не выполняется
# отладка: arr[6] *= 42 — не выполняется
# справка: arr[4] += 39 — не выполняется
# отладка: запись 173 обработана, изменений нет
# справка: arr2[1] = 7 — не выполняется
# архив: arr2[6] = 76 — не выполняется
# архив: arr[5] += 88 — не выполняется
# архив: запись 167 обработана, изменений нет
# ревизия: arr[5] += 21 — не выполняется
# временная запись: arr[9] = 1 — не выполняется
# справка: запись 707 обработана, изменений нет
# отладка: запись 880 обработана, изменений нет
# отладка: запись 177 обработана, изменений нет
# замечание: arr2[3] = 91 — не выполняется
# пометка: arr[0] *= 27 — не выполняется
# проверено: arr[0] += 77 — не выполняется
# справка: arr[5] = 94 — не выполняется
# ревизия: arr[9] = 2 — не выполняется
# справка: arr[1] = 58 — не выполняется
# пометка: запись 662 обработана, изменений нет
# справка: arr2[5] = 62 — не выполняется
# архив: arr[1] *= 49 — не выполняется
# черновик: arr2[5] = 85 — не выполняется
# временная запись: запись 48 обработана, изменений нет
# замечание: запись 44 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 673 обработана, изменений нет
# ревизия: запись 478 обработана, изменений нет
# временная запись: запись 567 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 152 обработана, изменений нет
# проверено: arr[8] *= 29 — не выполняется
# замечание: arr[4] += 74 — не выполняется
# справка: arr[3] = 55 — не выполняется
# отладка: запись 664 обработана, изменений нет
# ревизия: запись 376 обработана, изменений нет
# замечание: arr[2] += 16 — не выполняется
# пометка: запись 189 обработана, изменений нет
# временная запись: arr[8] *= 61 — не выполняется
# черновик: запись 298 обработана, изменений нет
# временная запись: запись 374 обработана, изменений нет
# справка: arr2[0] = 68 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 852 обработана, изменений нет
# справка: запись 896 обработана, изменений нет
# справка: запись 57 обработана, изменений нет
# временная запись: запись 669 обработана, изменений нет
# черновик: запись 690 обработана, изменений нет
# отладка: запись 553 обработана, изменений нет
# справка: arr[5] = 86 — не выполняется
# архив: запись 627 обработана, изменений нет
# временная запись: arr[0] += 84 — не выполняется
# черновик: arr[7] *= 26 — не выполняется
# проверено: запись 365 обработана, изменений нет
# пометка: запись 365 обработана, изменений нет
# ревизия: arr[3] *= 19 — не выполняется
# замечание: arr[8] = 60 — не выполняется
# архив: arr[7] = 55 — не выполняется
# черновик: arr2[7] = 59 — не выполняется
# архив: arr2[6] = 52 — не выполняется
# проверено: arr[2] += 96 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 847 обработана, изменений нет
# замечание: arr[2] *= 67 — не выполняется
# проверено: запись 854 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[8] = 41 — не выполняется
# справка: запись 959 обработана, изменений нет
# отладка: запись 423 обработана, изменений нет
# пометка: arr[2] = 79 — не выполняется
# ревизия: запись 584 обработана, изменений нет
# замечание: arr[6] += 67 — не выполняется
# временная запись: arr[5] *= 9 — не выполняется
# справка: запись 582 обработана, изменений нет
# ревизия: запись 195 обработана, изменений нет
# замечание: arr[5] += 23 — не выполняется
# проверено: запись 568 обработана, изменений нет
# отладка: arr[7] += 42 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 523 обработана, изменений нет
# справка: arr[1] = 9 — не выполняется
# пометка: arr2[8] = 99 — не выполняется
# архив: запись 478 обработана, изменений нет
# временная запись: arr[0] += 98 — не выполняется
# черновик: arr[1] = 2 — не выполняется
# архив: arr[1] *= 81 — не выполняется
# временная запись: запись 406 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# отладка: запись 154 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# архив: запись 113 обработана, изменений нет
# отладка: запись 798 обработана, изменений нет
# черновик: arr[7] = 81 — не выполняется
# архив: запись 548 обработана, изменений нет
# пометка: запись 199 обработана, изменений нет
# пометка: arr2[4] = 17 — не выполняется
# проверено: arr[8] = 96 — не выполняется
# справка: arr[9] = 93 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: arr[4] = 69 — не выполняется
# временная запись: запись 92 обработана, изменений нет
# ревизия: arr[4] += 40 — не выполняется
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr[4] += 75 — не выполняется
# справка: запись 907 обработана, изменений нет
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[9] = 14 — не выполняется
# ревизия: запись 619 обработана, изменений нет
# отладка: arr[4] *= 47 — не выполняется
# отладка: arr2[6] = 98 — не выполняется
# замечание: запись 886 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 318 обработана, изменений нет
# архив: arr2[0] = 58 — не выполняется
# примечание: arr2[9] = 97 — не выполняется
# отладка: запись 679 обработана, изменений нет
# архив: arr[0] += 2 — не выполняется
# замечание: запись 197 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[7] += 23 — не выполняется
# архив: запись 679 обработана, изменений нет
# черновик: запись 327 обработана, изменений нет
# справка: запись 599 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# справка: arr[0] *= 57 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# черновик: arr[0] = 18 — не выполняется
# ревизия: запись 132 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# справка: запись 176 обработана, изменений нет
# справка: запись 855 обработана, изменений нет
# примечание: запись 613 обработана, изменений нет
# отладка: запись 72 обработана, изменений нет
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 793 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# ревизия: arr[6] *= 42 — не выполняется
# проверено: arr[7] *= 94 — не выполняется
# отладка: запись 71 обработана, изменений нет
# пометка: arr[3] = 4 — не выполняется
# черновик: запись 726 обработана, изменений нет
# отладка: arr[2] *= 98 — не выполняется
# ревизия: arr[8] = 76 — не выполняется
# пометка: запись 618 обработана, изменений нет
arr[5] = int(t400) % 97
# черновик: запись 474 обработана, изменений нет
# отладка: запись 443 обработана, изменений нет
# справка: запись 532 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 459 обработана, изменений нет
# справка: запись 25 обработана, изменений нет
# замечание: arr[7] *= 70 — не выполняется
# ревизия: arr[6] += 61 — не выполняется
# отладка: запись 281 обработана, изменений нет
# ревизия: arr[5] += 72 — не выполняется
# проверено: запись 280 обработана, изменений нет
# отладка: arr2[2] = 71 — не выполняется
# отладка: arr2[8] = 49 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# справка: arr[5] *= 85 — не выполняется
# архив: arr[1] *= 29 — не выполняется
# архив: arr[9] *= 32 — не выполняется
# примечание: arr[9] += 24 — не выполняется
# пометка: arr[8] *= 24 — не выполняется
# справка: arr[1] *= 3 — не выполняется
# примечание: запись 947 обработана, изменений нет
# временная запись: arr[5] = 76 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 650 обработана, изменений нет
# пометка: запись 79 обработана, изменений нет
# архив: запись 991 обработана, изменений нет
# ревизия: запись 243 обработана, изменений нет
# справка: запись 336 обработана, изменений нет
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr[3] += 68 — не выполняется
# отладка: запись 731 обработана, изменений нет
# примечание: запись 465 обработана, изменений нет
# примечание: запись 924 обработана, изменений нет
# пометка: arr[9] += 43 — не выполняется
# проверено: arr[7] += 39 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 36 обработана, изменений нет
# пометка: запись 818 обработана, изменений нет
# черновик: запись 763 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# проверено: arr2[7] = 67 — не выполняется
# замечание: запись 808 обработана, изменений нет
# пометка: arr[0] += 79 — не выполняется
# ревизия: запись 982 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# временная запись: запись 185 обработана, изменений нет
# черновик: запись 599 обработана, изменений нет
# черновик: запись 108 обработана, изменений нет
# архив: запись 810 обработана, изменений нет
# отладка: запись 286 обработана, изменений нет
# ревизия: запись 67 обработана, изменений нет
# справка: запись 161 обработана, изменений нет
# пометка: запись 738 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[8] = 59 — не выполняется
# черновик: запись 744 обработана, изменений нет
# отладка: запись 626 обработана, изменений нет
# справка: запись 705 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# справка: запись 22 обработана, изменений нет
# замечание: запись 694 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# отладка: запись 115 обработана, изменений нет
# черновик: arr[0] = 9 — не выполняется
# отладка: запись 812 обработана, изменений нет
# пометка: запись 179 обработана, изменений нет
# ревизия: arr[1] *= 85 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: запись 887 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 163 обработана, изменений нет
# временная запись: arr[4] *= 71 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr[5] = 5 — не выполняется
# черновик: запись 121 обработана, изменений нет
# отладка: arr[7] *= 78 — не выполняется
# примечание: запись 760 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 469 обработана, изменений нет
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[6] += 88 — не выполняется
# отладка: запись 968 обработана, изменений нет
# отладка: запись 676 обработана, изменений нет
# временная запись: arr2[0] = 84 — не выполняется
# черновик: запись 879 обработана, изменений нет
# ревизия: запись 995 обработана, изменений нет
# пометка: arr[8] += 46 — не выполняется
# замечание: arr[8] *= 4 — не выполняется
# справка: запись 39 обработана, изменений нет
# черновик: запись 411 обработана, изменений нет
# ревизия: arr2[9] = 42 — не выполняется
# замечание: запись 861 обработана, изменений нет
# временная запись: arr2[6] = 4 — не выполняется
# пометка: arr[3] = 30 — не выполняется
# архив: запись 420 обработана, изменений нет
# замечание: запись 199 обработана, изменений нет
# архив: arr2[9] = 46 — не выполняется
# черновик: запись 639 обработана, изменений нет
# проверено: запись 907 обработана, изменений нет
# архив: arr[2] *= 88 — не выполняется
# справка: arr[1] *= 33 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# примечание: запись 893 обработана, изменений нет
# ревизия: запись 563 обработана, изменений нет
# временная запись: arr[5] += 6 — не выполняется
# черновик: arr[8] *= 95 — не выполняется
# пометка: запись 975 обработана, изменений нет
# пометка: arr[4] = 78 — не выполняется
# пометка: запись 460 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: arr[8] = 47 — не выполняется
# черновик: arr[5] += 22 — не выполняется
# черновик: запись 117 обработана, изменений нет
# черновик: запись 607 обработана, изменений нет
# архив: arr[2] *= 82 — не выполняется
# справка: arr[6] += 95 — не выполняется
# справка: arr[1] += 52 — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 365 обработана, изменений нет
# проверено: arr[0] += 10 — не выполняется
# примечание: запись 851 обработана, изменений нет
# пометка: arr[3] += 73 — не выполняется
# справка: запись 256 обработана, изменений нет
# примечание: запись 219 обработана, изменений нет
# примечание: arr[2] = 50 — не выполняется
# пометка: arr2[2] = 61 — не выполняется
# примечание: запись 798 обработана, изменений нет
# проверено: arr2[6] = 34 — не выполняется
# замечание: запись 49 обработана, изменений нет
# пометка: запись 284 обработана, изменений нет
# пометка: arr2[5] = 68 — не выполняется
# ревизия: запись 698 обработана, изменений нет
# справка: запись 629 обработана, изменений нет
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 797 обработана, изменений нет
# справка: запись 221 обработана, изменений нет
# отладка: запись 924 обработана, изменений нет
# справка: запись 753 обработана, изменений нет
# отладка: запись 269 обработана, изменений нет
# временная запись: запись 113 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# проверено: arr[3] += 8 — не выполняется
# замечание: запись 551 обработана, изменений нет
# архив: запись 831 обработана, изменений нет
# архив: arr[3] *= 21 — не выполняется
# справка: запись 598 обработана, изменений нет
# справка: запись 322 обработана, изменений нет
# черновик: запись 620 обработана, изменений нет
# ревизия: запись 811 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# отладка: запись 296 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# справка: запись 25 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: запись 435 обработана, изменений нет
# примечание: arr2[6] = 30 — не выполняется
# временная запись: запись 781 обработана, изменений нет
# примечание: arr2[4] = 84 — не выполняется
# отладка: запись 415 обработана, изменений нет
# проверено: arr[7] *= 82 — не выполняется
# замечание: запись 294 обработана, изменений нет
# временная запись: запись 481 обработана, изменений нет
# проверено: запись 609 обработана, изменений нет
# временная запись: запись 387 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# справка: arr[8] += 28 — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 220 обработана, изменений нет
# примечание: arr[9] *= 31 — не выполняется
# примечание: arr2[3] = 94 — не выполняется
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[1] = 34 — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: запись 380 обработана, изменений нет
# пометка: arr2[1] = 71 — не выполняется
# пометка: arr[5] *= 30 — не выполняется
# ревизия: arr[0] += 69 — не выполняется
# проверено: запись 168 обработана, изменений нет
# ревизия: arr[1] = 1 — не выполняется
# ревизия: arr[2] += 52 — не выполняется
# временная запись: запись 763 обработана, изменений нет
# черновик: запись 152 обработана, изменений нет
# проверено: arr2[4] = 45 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# пометка: arr[4] *= 89 — не выполняется
# проверено: запись 909 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 528 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 107 обработана, изменений нет
# замечание: arr[8] = 86 — не выполняется
# временная запись: arr[6] *= 10 — не выполняется
# примечание: запись 34 обработана, изменений нет
# справка: запись 738 обработана, изменений нет
# ревизия: запись 898 обработана, изменений нет
# архив: arr[8] += 86 — не выполняется
# временная запись: arr[5] *= 71 — не выполняется
# временная запись: arr2[7] = 20 — не выполняется
# ревизия: запись 514 обработана, изменений нет
# справка: запись 687 обработана, изменений нет
# пометка: запись 258 обработана, изменений нет
# отладка: arr[2] += 14 — не выполняется
# черновик: запись 549 обработана, изменений нет
# временная запись: arr2[9] = 61 — не выполняется
# замечание: запись 821 обработана, изменений нет
# отладка: запись 420 обработана, изменений нет
# временная запись: запись 285 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[5] += 21 — не выполняется
# отладка: arr[2] += 54 — не выполняется
# замечание: arr[1] *= 3 — не выполняется
# архив: arr[8] *= 7 — не выполняется
# проверено: запись 642 обработана, изменений нет
# пометка: запись 684 обработана, изменений нет
# замечание: запись 808 обработана, изменений нет
# архив: arr[0] = 39 — не выполняется
# замечание: arr[4] = 92 — не выполняется
# отладка: запись 188 обработана, изменений нет
# замечание: запись 828 обработана, изменений нет
# проверено: запись 471 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# пометка: запись 570 обработана, изменений нет
# ревизия: запись 354 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[3] = 59 — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 748 обработана, изменений нет
# черновик: запись 279 обработана, изменений нет
# проверено: запись 862 обработана, изменений нет
# замечание: запись 132 обработана, изменений нет
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: arr[8] += 69 — не выполняется
# примечание: запись 54 обработана, изменений нет
# ревизия: arr[2] *= 5 — не выполняется
# замечание: запись 162 обработана, изменений нет
# черновик: запись 576 обработана, изменений нет
# архив: arr[6] = 93 — не выполняется
# черновик: arr[3] += 74 — не выполняется
# отладка: arr[1] += 5 — не выполняется
# временная запись: запись 245 обработана, изменений нет
# временная запись: arr2[5] = 83 — не выполняется
# временная запись: запись 893 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: запись 848 обработана, изменений нет
# справка: arr[0] *= 69 — не выполняется
# ревизия: запись 537 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# пометка: arr[2] = 29 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[4] *= 9 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# справка: arr[6] *= 68 — не выполняется
# замечание: запись 77 обработана, изменений нет
arr[2] += 2
# проверено: arr[2] *= 42 — не выполняется
# примечание: arr[5] *= 12 — не выполняется
# архив: arr2[2] = 43 — не выполняется
# пометка: arr2[4] = 21 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[0] += 33 — не выполняется
# проверено: arr[5] *= 78 — не выполняется
# черновик: запись 418 обработана, изменений нет
# черновик: запись 622 обработана, изменений нет
# справка: arr[1] *= 64 — не выполняется
# проверено: arr[6] *= 85 — не выполняется
# черновик: arr[2] += 6 — не выполняется
# временная запись: arr[2] *= 4 — не выполняется
# ревизия: arr[8] += 7 — не выполняется
# ревизия: arr[4] = 38 — не выполняется
# справка: arr2[9] = 83 — не выполняется
# замечание: запись 701 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[9] *= 17 — не выполняется
# архив: arr[1] += 87 — не выполняется
# проверено: arr2[8] = 74 — не выполняется
# архив: arr[3] = 54 — не выполняется
# проверено: запись 757 обработана, изменений нет
# черновик: arr[4] = 50 — не выполняется
# отладка: arr[8] *= 22 — не выполняется
# пометка: запись 182 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# пометка: запись 871 обработана, изменений нет
# примечание: запись 204 обработана, изменений нет
# справка: arr[2] = 63 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 328 обработана, изменений нет
# примечание: arr2[9] = 1 — не выполняется
# черновик: запись 28 обработана, изменений нет
# справка: запись 634 обработана, изменений нет
# примечание: запись 994 обработана, изменений нет
# справка: запись 938 обработана, изменений нет
# справка: запись 971 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 124 обработана, изменений нет
# отладка: arr[2] *= 45 — не выполняется
# примечание: запись 735 обработана, изменений нет
# замечание: arr[1] *= 13 — не выполняется
# отладка: arr[1] *= 93 — не выполняется
# черновик: arr2[6] = 45 — не выполняется
# примечание: запись 378 обработана, изменений нет
# проверено: arr[7] *= 64 — не выполняется
# архив: arr[5] += 31 — не выполняется
# проверено: запись 395 обработана, изменений нет
# справка: запись 683 обработана, изменений нет
# черновик: запись 443 обработана, изменений нет
# архив: запись 784 обработана, изменений нет
# пометка: arr[2] = 73 — не выполняется
# пометка: запись 339 обработана, изменений нет
# проверено: запись 725 обработана, изменений нет
# отладка: arr2[4] = 20 — не выполняется
# архив: arr[2] *= 6 — не выполняется
# временная запись: запись 423 обработана, изменений нет
# ревизия: arr[1] = 17 — не выполняется
# примечание: arr2[8] = 74 — не выполняется
# проверено: arr[3] *= 60 — не выполняется
# отладка: запись 820 обработана, изменений нет
# примечание: arr[0] = 97 — не выполняется
# отладка: запись 478 обработана, изменений нет
# отладка: запись 721 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 219 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# справка: запись 168 обработана, изменений нет
# временная запись: arr[3] *= 41 — не выполняется
# замечание: запись 645 обработана, изменений нет
# замечание: запись 134 обработана, изменений нет
# ревизия: запись 549 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[2] += 62 — не выполняется
# архив: запись 252 обработана, изменений нет
# примечание: arr[0] *= 76 — не выполняется
# архив: запись 26 обработана, изменений нет
# отладка: arr[6] *= 3 — не выполняется
# черновик: запись 114 обработана, изменений нет
# пометка: запись 548 обработана, изменений нет
# пометка: arr[7] *= 18 — не выполняется
# ревизия: запись 132 обработана, изменений нет
# архив: arr[3] *= 68 — не выполняется
# проверено: запись 867 обработана, изменений нет
# отладка: arr2[6] = 80 — не выполняется
# черновик: запись 829 обработана, изменений нет
# архив: arr[2] *= 42 — не выполняется
# справка: запись 561 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 123 обработана, изменений нет
# пометка: arr[9] *= 50 — не выполняется
# справка: arr[1] *= 64 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 568 обработана, изменений нет
# проверено: запись 829 обработана, изменений нет
# черновик: запись 644 обработана, изменений нет
# отладка: arr[2] *= 35 — не выполняется
# черновик: запись 473 обработана, изменений нет
# примечание: запись 487 обработана, изменений нет
# временная запись: arr[8] *= 78 — не выполняется
# замечание: запись 325 обработана, изменений нет
# замечание: запись 216 обработана, изменений нет
# архив: arr[2] *= 82 — не выполняется
# ревизия: запись 647 обработана, изменений нет
# справка: arr[2] += 18 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# проверено: запись 708 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: arr[0] = 23 — не выполняется
# архив: запись 809 обработана, изменений нет
# ревизия: запись 523 обработана, изменений нет
# пометка: arr[8] *= 66 — не выполняется
# архив: запись 674 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# архив: запись 821 обработана, изменений нет
# архив: arr[5] += 94 — не выполняется
# примечание: запись 62 обработана, изменений нет
# отладка: запись 39 обработана, изменений нет
# замечание: запись 350 обработана, изменений нет
# проверено: arr2[4] = 56 — не выполняется
# справка: запись 381 обработана, изменений нет
# архив: arr[0] = 64 — не выполняется
# пометка: arr[9] += 24 — не выполняется
# черновик: arr[8] += 64 — не выполняется
# проверено: arr[2] *= 7 — не выполняется
# пометка: запись 614 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# замечание: arr[3] *= 10 — не выполняется
# проверено: запись 355 обработана, изменений нет
# справка: запись 138 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 172 обработана, изменений нет
# отладка: arr[1] += 84 — не выполняется
# примечание: запись 880 обработана, изменений нет
# архив: arr[4] += 28 — не выполняется
# временная запись: arr[5] = 25 — не выполняется
# примечание: arr[3] *= 66 — не выполняется
# черновик: arr[7] = 82 — не выполняется
# справка: запись 301 обработана, изменений нет
# ревизия: arr[0] *= 23 — не выполняется
# проверено: arr[9] = 36 — не выполняется
# справка: запись 480 обработана, изменений нет
# черновик: запись 936 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 953 обработана, изменений нет
# справка: запись 206 обработана, изменений нет
# временная запись: запись 872 обработана, изменений нет
# примечание: запись 926 обработана, изменений нет
# ревизия: arr[0] *= 10 — не выполняется
# черновик: запись 552 обработана, изменений нет
# временная запись: запись 20 обработана, изменений нет
# черновик: arr[5] = 61 — не выполняется
# отладка: arr[5] *= 13 — не выполняется
# справка: arr[7] += 17 — не выполняется
# примечание: arr[4] *= 45 — не выполняется
# пометка: запись 140 обработана, изменений нет
# отладка: arr2[5] = 99 — не выполняется
# отладка: запись 994 обработана, изменений нет
# примечание: запись 269 обработана, изменений нет
# временная запись: arr[0] *= 63 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[8] *= 78 — не выполняется
# отладка: arr[7] = 5 — не выполняется
# пометка: запись 592 обработана, изменений нет
# архив: запись 947 обработана, изменений нет
# проверено: запись 397 обработана, изменений нет
# справка: запись 765 обработана, изменений нет
# проверено: запись 717 обработана, изменений нет
# отладка: запись 850 обработана, изменений нет
# временная запись: arr[6] += 11 — не выполняется
# пометка: запись 481 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: arr[3] = 88 — не выполняется
# примечание: arr[3] += 88 — не выполняется
# проверено: arr[7] = 51 — не выполняется
# справка: запись 630 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# черновик: запись 198 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# архив: arr[4] += 8 — не выполняется
# пометка: запись 159 обработана, изменений нет
# временная запись: arr[2] += 80 — не выполняется
# архив: запись 864 обработана, изменений нет
# ревизия: запись 319 обработана, изменений нет
# ревизия: запись 433 обработана, изменений нет
# замечание: arr[3] += 85 — не выполняется
# ревизия: arr2[3] = 32 — не выполняется
# проверено: запись 98 обработана, изменений нет
# замечание: запись 430 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# проверено: arr[9] *= 81 — не выполняется
# справка: arr[3] *= 25 — не выполняется
# справка: запись 799 обработана, изменений нет
# пометка: arr[6] *= 3 — не выполняется
# примечание: arr[3] *= 74 — не выполняется
# примечание: запись 751 обработана, изменений нет
# черновик: arr[7] *= 48 — не выполняется
# черновик: запись 24 обработана, изменений нет
# замечание: arr2[1] = 90 — не выполняется
# ревизия: запись 702 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: arr[9] *= 61 — не выполняется
# примечание: arr[5] *= 68 — не выполняется
# пометка: запись 217 обработана, изменений нет
# проверено: запись 606 обработана, изменений нет
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr2[4] = 29 — не выполняется
# пометка: запись 822 обработана, изменений нет
# ревизия: arr[0] = 73 — не выполняется
# пометка: запись 790 обработана, изменений нет
# пометка: запись 371 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 448 обработана, изменений нет
# ревизия: arr[9] = 81 — не выполняется
# архив: arr2[9] = 17 — не выполняется
# справка: запись 418 обработана, изменений нет
# черновик: arr[5] *= 43 — не выполняется
# проверено: запись 442 обработана, изменений нет
# пометка: запись 346 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[5] += 23 — не выполняется
# ревизия: arr2[8] = 6 — не выполняется
# справка: arr[4] = 21 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: запись 431 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# временная запись: запись 395 обработана, изменений нет
# временная запись: arr[4] = 90 — не выполняется
# ревизия: arr[3] *= 38 — не выполняется
# примечание: arr2[0] = 74 — не выполняется
# временная запись: arr2[1] = 63 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[1] *= 9 — не выполняется
# черновик: запись 693 обработана, изменений нет
# замечание: запись 129 обработана, изменений нет
# проверено: запись 925 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 576 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# временная запись: запись 91 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 555 обработана, изменений нет
# справка: arr[4] = 61 — не выполняется
# примечание: запись 671 обработана, изменений нет
# справка: arr[8] *= 33 — не выполняется
# ревизия: запись 991 обработана, изменений нет
# проверено: arr[4] = 97 — не выполняется
# отладка: arr2[5] = 7 — не выполняется
# примечание: запись 64 обработана, изменений нет
# временная запись: запись 181 обработана, изменений нет
# справка: запись 985 обработана, изменений нет
# пометка: arr2[3] = 41 — не выполняется
# справка: запись 684 обработана, изменений нет
# ревизия: запись 645 обработана, изменений нет
# архив: запись 719 обработана, изменений нет
# временная запись: arr[5] += 44 — не выполняется
# архив: arr[5] += 32 — не выполняется
# черновик: запись 625 обработана, изменений нет
arr2 = arr
# временная запись: arr[1] = 3 — не выполняется
# ревизия: arr[0] += 55 — не выполняется
# архив: arr2[5] = 70 — не выполняется
# временная запись: запись 344 обработана, изменений нет
# проверено: arr[8] *= 47 — не выполняется
# архив: arr[6] += 93 — не выполняется
# справка: arr2[1] = 13 — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 991 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 950 обработана, изменений нет
# пометка: arr2[4] = 74 — не выполняется
# черновик: запись 733 обработана, изменений нет
# отладка: arr[9] *= 85 — не выполняется
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 328 обработана, изменений нет
# примечание: arr2[1] = 31 — не выполняется
# справка: arr2[7] = 28 — не выполняется
# примечание: запись 254 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 56 обработана, изменений нет
# ревизия: arr[8] *= 61 — не выполняется
# архив: arr[2] += 64 — не выполняется
# справка: запись 171 обработана, изменений нет
# отладка: arr[4] = 1 — не выполняется
# временная запись: запись 416 обработана, изменений нет
# ревизия: arr[6] *= 75 — не выполняется
# ревизия: запись 717 обработана, изменений нет
# ревизия: запись 777 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 291 обработана, изменений нет
# проверено: arr[1] += 77 — не выполняется
# временная запись: запись 765 обработана, изменений нет
# архив: arr[4] *= 86 — не выполняется
# справка: arr[6] += 65 — не выполняется
# архив: arr[9] *= 67 — не выполняется
# отладка: запись 137 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# отладка: arr[8] += 10 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[6] += 20 — не выполняется
# черновик: запись 431 обработана, изменений нет
# проверено: запись 913 обработана, изменений нет
# примечание: arr[6] *= 63 — не выполняется
# пометка: запись 785 обработана, изменений нет
# проверено: arr2[7] = 43 — не выполняется
# замечание: запись 285 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 423 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# архив: запись 530 обработана, изменений нет
# временная запись: arr[9] *= 42 — не выполняется
# ревизия: запись 65 обработана, изменений нет
# временная запись: запись 557 обработана, изменений нет
# замечание: запись 662 обработана, изменений нет
# проверено: запись 875 обработана, изменений нет
# архив: запись 889 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[3] = 30 — не выполняется
# пометка: arr2[0] = 32 — не выполняется
# проверено: arr[7] = 27 — не выполняется
# замечание: запись 167 обработана, изменений нет
# ревизия: запись 543 обработана, изменений нет
# черновик: запись 703 обработана, изменений нет
# замечание: запись 33 обработана, изменений нет
# проверено: arr2[9] = 70 — не выполняется
# черновик: arr[9] += 85 — не выполняется
# замечание: запись 782 обработана, изменений нет
# замечание: arr2[4] = 29 — не выполняется
# временная запись: arr2[2] = 40 — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: arr[0] = 58 — не выполняется
# примечание: arr[6] += 3 — не выполняется
# пометка: запись 20 обработана, изменений нет
# черновик: arr[1] = 33 — не выполняется
# примечание: arr[5] += 76 — не выполняется
# замечание: запись 259 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# ревизия: arr[1] += 94 — не выполняется
# примечание: arr[5] += 82 — не выполняется
# примечание: запись 432 обработана, изменений нет
# проверено: arr[7] *= 64 — не выполняется
# примечание: arr[7] *= 39 — не выполняется
# архив: запись 739 обработана, изменений нет
# пометка: arr[7] += 66 — не выполняется
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[8] += 58 — не выполняется
# черновик: запись 798 обработана, изменений нет
# архив: запись 55 обработана, изменений нет
# примечание: запись 840 обработана, изменений нет
# проверено: arr[2] += 32 — не выполняется
# проверено: запись 350 обработана, изменений нет
# пометка: запись 233 обработана, изменений нет
# черновик: запись 882 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# пометка: arr[9] = 32 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# пометка: arr[9] *= 51 — не выполняется
# проверено: arr[2] = 22 — не выполняется
# ревизия: запись 99 обработана, изменений нет
# замечание: arr2[0] = 17 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 525 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# черновик: arr[7] *= 5 — не выполняется
# примечание: запись 915 обработана, изменений нет
# пометка: запись 85 обработана, изменений нет
# замечание: запись 166 обработана, изменений нет
# проверено: запись 66 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: arr[9] += 90 — не выполняется
# ревизия: arr[6] += 88 — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr[8] = 20 — не выполняется
# черновик: запись 313 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# ревизия: запись 585 обработана, изменений нет
# примечание: arr[0] *= 43 — не выполняется
# справка: arr[9] += 42 — не выполняется
# ревизия: запись 123 обработана, изменений нет
# пометка: arr[5] *= 25 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[6] = 61 — не выполняется
# черновик: запись 979 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 810 обработана, изменений нет
# отладка: запись 925 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 686 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# архив: arr[7] = 76 — не выполняется
# ревизия: запись 328 обработана, изменений нет
# временная запись: arr[5] += 84 — не выполняется
# черновик: arr2[7] = 84 — не выполняется
# примечание: запись 3 обработана, изменений нет
# временная запись: arr[5] += 24 — не выполняется
# ревизия: arr[1] += 39 — не выполняется
# замечание: arr2[0] = 92 — не выполняется
# справка: запись 491 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# черновик: запись 530 обработана, изменений нет
# ревизия: arr[4] *= 9 — не выполняется
# справка: запись 965 обработана, изменений нет
# пометка: запись 236 обработана, изменений нет
# проверено: запись 717 обработана, изменений нет
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[4] += 72 — не выполняется
# отладка: запись 980 обработана, изменений нет
# архив: arr[1] *= 58 — не выполняется
# справка: arr[7] *= 55 — не выполняется
# примечание: arr[7] *= 89 — не выполняется
# временная запись: arr[8] *= 16 — не выполняется
# черновик: arr[6] *= 37 — не выполняется
# замечание: arr[3] = 43 — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[6] *= 1 — не выполняется
# отладка: запись 176 обработана, изменений нет
# пометка: запись 488 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# временная запись: запись 657 обработана, изменений нет
# архив: arr2[7] = 7 — не выполняется
# проверено: запись 235 обработана, изменений нет
# черновик: запись 235 обработана, изменений нет
# справка: arr2[1] = 45 — не выполняется
# справка: запись 638 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# справка: arr2[2] = 13 — не выполняется
# пометка: arr2[4] = 37 — не выполняется
# замечание: запись 871 обработана, изменений нет
# замечание: запись 919 обработана, изменений нет
# отладка: arr[1] *= 25 — не выполняется
# замечание: запись 442 обработана, изменений нет
# пометка: arr[0] = 44 — не выполняется
# временная запись: запись 27 обработана, изменений нет
# черновик: запись 267 обработана, изменений нет
# справка: arr2[6] = 24 — не выполняется
# пометка: запись 727 обработана, изменений нет
# архив: arr[2] += 84 — не выполняется
# отладка: arr[0] *= 99 — не выполняется
# ревизия: arr[9] = 69 — не выполняется
# черновик: arr[1] = 96 — не выполняется
# черновик: запись 768 обработана, изменений нет
# проверено: arr[6] = 92 — не выполняется
# временная запись: запись 941 обработана, изменений нет
# замечание: запись 245 обработана, изменений нет
# архив: запись 923 обработана, изменений нет
# временная запись: запись 270 обработана, изменений нет
# ревизия: arr[4] *= 21 — не выполняется
# временная запись: arr2[3] = 95 — не выполняется
# ревизия: arr[9] = 72 — не выполняется
# ревизия: arr[4] = 97 — не выполняется
# архив: arr2[8] = 82 — не выполняется
# замечание: arr2[9] = 37 — не выполняется
# замечание: запись 652 обработана, изменений нет
# архив: arr[5] += 74 — не выполняется
# архив: запись 278 обработана, изменений нет
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 196 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr[9] += 21 — не выполняется
# ревизия: arr[8] = 15 — не выполняется
# проверено: arr[9] *= 79 — не выполняется
# примечание: запись 908 обработана, изменений нет
# архив: arr[7] += 29 — не выполняется
# временная запись: запись 491 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 916 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# черновик: arr2[4] = 71 — не выполняется
# ревизия: запись 543 обработана, изменений нет
# отладка: arr[2] = 46 — не выполняется
# проверено: запись 357 обработана, изменений нет
# справка: arr[6] = 56 — не выполняется
# справка: запись 888 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# замечание: запись 110 обработана, изменений нет
# проверено: запись 54 обработана, изменений нет
# замечание: arr2[6] = 50 — не выполняется
# замечание: arr[1] += 7 — не выполняется
# временная запись: arr[2] = 61 — не выполняется
# проверено: arr[8] *= 94 — не выполняется
# примечание: arr[8] += 10 — не выполняется
# отладка: запись 113 обработана, изменений нет
# справка: arr[7] = 65 — не выполняется
# проверено: запись 800 обработана, изменений нет
# ревизия: arr[9] += 70 — не выполняется
# временная запись: запись 759 обработана, изменений нет
# отладка: запись 144 обработана, изменений нет
# отладка: запись 364 обработана, изменений нет
# черновик: запись 157 обработана, изменений нет
# ревизия: arr[9] = 40 — не выполняется
# отладка: запись 899 обработана, изменений нет
# отладка: arr[2] += 82 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 516 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# пометка: arr2[2] = 23 — не выполняется
# отладка: запись 99 обработана, изменений нет
# замечание: arr[7] = 82 — не выполняется
# архив: arr[4] += 31 — не выполняется
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 720 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 579 обработана, изменений нет
# справка: arr[4] = 30 — не выполняется
# архив: arr[7] *= 76 — не выполняется
# отладка: запись 152 обработана, изменений нет
# примечание: запись 302 обработана, изменений нет
# ревизия: arr2[6] = 68 — не выполняется
# пометка: arr2[8] = 23 — не выполняется
# черновик: arr[5] += 76 — не выполняется
# отладка: запись 209 обработана, изменений нет
# черновик: arr[3] *= 55 — не выполняется
# пометка: arr[7] += 27 — не выполняется
# черновик: запись 912 обработана, изменений нет
# проверено: запись 388 обработана, изменений нет
# временная запись: arr2[4] = 18 — не выполняется
# черновик: запись 601 обработана, изменений нет
# пометка: arr[0] += 43 — не выполняется
arr2[3] += 7
# ревизия: запись 709 обработана, изменений нет
# проверено: запись 414 обработана, изменений нет
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 850 обработана, изменений нет
# проверено: запись 489 обработана, изменений нет
# примечание: запись 234 обработана, изменений нет
# черновик: запись 292 обработана, изменений нет
# замечание: arr[9] = 19 — не выполняется
# отладка: запись 98 обработана, изменений нет
# ревизия: запись 842 обработана, изменений нет
# черновик: запись 884 обработана, изменений нет
# замечание: запись 486 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# проверено: запись 919 обработана, изменений нет
# временная запись: запись 721 обработана, изменений нет
# отладка: запись 638 обработана, изменений нет
# замечание: запись 134 обработана, изменений нет
# черновик: arr[9] *= 34 — не выполняется
# примечание: запись 340 обработана, изменений нет
# пометка: arr[8] *= 4 — не выполняется
# отладка: arr[1] += 91 — не выполняется
# архив: arr[5] = 51 — не выполняется
# временная запись: arr[3] *= 26 — не выполняется
# пометка: запись 263 обработана, изменений нет
# проверено: arr[1] *= 62 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: запись 135 обработана, изменений нет
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: arr[5] += 86 — не выполняется
# примечание: запись 789 обработана, изменений нет
# примечание: запись 125 обработана, изменений нет
# справка: запись 166 обработана, изменений нет
# черновик: запись 869 обработана, изменений нет
# проверено: arr[4] = 5 — не выполняется
# ревизия: arr[8] = 65 — не выполняется
# временная запись: запись 879 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: запись 181 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# архив: arr[0] *= 5 — не выполняется
# справка: запись 882 обработана, изменений нет
# ревизия: запись 764 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# проверено: arr[6] += 6 — не выполняется
# примечание: запись 765 обработана, изменений нет
# замечание: arr2[8] = 60 — не выполняется
# проверено: запись 88 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr2[3] = 77 — не выполняется
# отладка: запись 796 обработана, изменений нет
# справка: arr[1] *= 43 — не выполняется
# примечание: запись 500 обработана, изменений нет
# отладка: запись 10 обработана, изменений нет
# примечание: запись 774 обработана, изменений нет
# проверено: arr[4] += 67 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# черновик: запись 535 обработана, изменений нет
# отладка: arr[8] *= 91 — не выполняется
# временная запись: arr[0] += 13 — не выполняется
# архив: запись 701 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# справка: arr2[6] = 43 — не выполняется
# замечание: запись 170 обработана, изменений нет
# справка: запись 835 обработана, изменений нет
# примечание: arr[6] += 15 — не выполняется
# справка: arr[4] *= 55 — не выполняется
# проверено: запись 840 обработана, изменений нет
# пометка: запись 924 обработана, изменений нет
# ревизия: arr2[0] = 43 — не выполняется
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 742 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 409 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: запись 434 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 824 обработана, изменений нет
# временная запись: arr[2] *= 34 — не выполняется
# черновик: запись 367 обработана, изменений нет
# примечание: arr[6] *= 28 — не выполняется
# пометка: запись 488 обработана, изменений нет
# справка: arr[7] *= 52 — не выполняется
# пометка: запись 354 обработана, изменений нет
# примечание: запись 853 обработана, изменений нет
# примечание: arr2[0] = 37 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 59 обработана, изменений нет
# справка: arr[5] *= 25 — не выполняется
# пометка: запись 768 обработана, изменений нет
# пометка: arr[3] *= 1 — не выполняется
# ревизия: arr[6] += 89 — не выполняется
# примечание: запись 59 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# замечание: arr2[4] = 57 — не выполняется
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[9] *= 18 — не выполняется
# черновик: arr[1] = 68 — не выполняется
# примечание: arr[2] *= 62 — не выполняется
# временная запись: запись 252 обработана, изменений нет
# справка: arr2[8] = 8 — не выполняется
# справка: запись 439 обработана, изменений нет
# отладка: запись 656 обработана, изменений нет
# черновик: arr2[6] = 26 — не выполняется
# ревизия: arr[7] = 95 — не выполняется
# справка: arr[8] = 59 — не выполняется
# временная запись: запись 375 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: arr[9] *= 22 — не выполняется
# справка: запись 492 обработана, изменений нет
# черновик: запись 373 обработана, изменений нет
# ревизия: запись 934 обработана, изменений нет
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[7] *= 45 — не выполняется
# справка: запись 976 обработана, изменений нет
# ревизия: arr[3] = 77 — не выполняется
# черновик: arr[2] *= 60 — не выполняется
# примечание: arr2[4] = 80 — не выполняется
# отладка: arr[3] = 90 — не выполняется
# примечание: запись 378 обработана, изменений нет
# замечание: запись 530 обработана, изменений нет
# примечание: arr2[0] = 85 — не выполняется
# пометка: arr2[8] = 30 — не выполняется
# временная запись: запись 333 обработана, изменений нет
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 540 обработана, изменений нет
# пометка: arr2[8] = 85 — не выполняется
# временная запись: arr[1] *= 35 — не выполняется
# справка: запись 789 обработана, изменений нет
# справка: arr[5] *= 84 — не выполняется
# справка: запись 16 обработана, изменений нет
# временная запись: arr2[4] = 92 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[0] += 34 — не выполняется
# замечание: arr[3] *= 28 — не выполняется
# справка: arr2[0] = 38 — не выполняется
# замечание: arr[6] = 29 — не выполняется
# отладка: запись 133 обработана, изменений нет
# архив: запись 614 обработана, изменений нет
# временная запись: запись 308 обработана, изменений нет
# примечание: arr[7] = 21 — не выполняется
# пометка: arr[5] *= 95 — не выполняется
# отладка: arr[6] *= 56 — не выполняется
# проверено: запись 270 обработана, изменений нет
# отладка: запись 314 обработана, изменений нет
# ревизия: arr[1] = 90 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 193 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# архив: запись 640 обработана, изменений нет
# замечание: запись 560 обработана, изменений нет
# черновик: запись 42 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# проверено: запись 250 обработана, изменений нет
# ревизия: запись 746 обработана, изменений нет
# ревизия: запись 11 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[2] += 44 — не выполняется
# пометка: arr[7] += 5 — не выполняется
# отладка: arr[3] += 52 — не выполняется
# ревизия: запись 779 обработана, изменений нет
# ревизия: arr[3] += 66 — не выполняется
# ревизия: запись 952 обработана, изменений нет
# отладка: arr[0] += 79 — не выполняется
# архив: запись 305 обработана, изменений нет
# архив: arr[7] = 84 — не выполняется
# временная запись: запись 864 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr2[8] = 47 — не выполняется
# замечание: запись 865 обработана, изменений нет
# ревизия: arr[6] *= 44 — не выполняется
# замечание: запись 283 обработана, изменений нет
# отладка: arr[0] = 1 — не выполняется
# проверено: запись 131 обработана, изменений нет
# пометка: arr2[7] = 62 — не выполняется
# примечание: запись 738 обработана, изменений нет
# временная запись: arr2[5] = 57 — не выполняется
# архив: arr[4] *= 16 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: arr[6] += 54 — не выполняется
# ревизия: запись 901 обработана, изменений нет
# проверено: запись 997 обработана, изменений нет
# справка: запись 794 обработана, изменений нет
# черновик: запись 589 обработана, изменений нет
# черновик: запись 433 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[0] += 75 — не выполняется
# пометка: запись 836 обработана, изменений нет
# отладка: arr[6] = 91 — не выполняется
# замечание: запись 497 обработана, изменений нет
# отладка: arr[6] = 71 — не выполняется
# проверено: arr[8] *= 9 — не выполняется
# архив: запись 351 обработана, изменений нет
# ревизия: arr2[7] = 66 — не выполняется
# замечание: arr[7] *= 1 — не выполняется
# отладка: запись 794 обработана, изменений нет
# проверено: запись 719 обработана, изменений нет
# примечание: arr[9] *= 90 — не выполняется
# пометка: arr[2] *= 89 — не выполняется
# временная запись: запись 991 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 939 обработана, изменений нет
# примечание: arr[5] += 30 — не выполняется
# справка: запись 956 обработана, изменений нет
# архив: запись 996 обработана, изменений нет
# временная запись: запись 218 обработана, изменений нет
# замечание: запись 257 обработана, изменений нет
# ревизия: запись 21 обработана, изменений нет
# архив: arr[9] = 50 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# пометка: запись 384 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr2[5] = 27 — не выполняется
# черновик: запись 68 обработана, изменений нет
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr2[9] = 65 — не выполняется
# пометка: запись 172 обработана, изменений нет
# справка: запись 480 обработана, изменений нет
# отладка: arr[3] *= 38 — не выполняется
# справка: запись 218 обработана, изменений нет
# справка: arr[0] *= 26 — не выполняется
# замечание: arr[5] = 50 — не выполняется
# проверено: arr[4] = 7 — не выполняется
# проверено: запись 40 обработана, изменений нет
# справка: запись 931 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: arr2[2] = 43 — не выполняется
# пометка: запись 543 обработана, изменений нет
# отладка: запись 653 обработана, изменений нет
# временная запись: arr2[1] = 58 — не выполняется
# временная запись: arr[1] *= 44 — не выполняется
# архив: запись 730 обработана, изменений нет
# замечание: arr[7] += 87 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[6] *= 22 — не выполняется
# справка: arr[4] += 35 — не выполняется
# проверено: запись 262 обработана, изменений нет
# пометка: arr2[1] = 57 — не выполняется
# проверено: arr[5] *= 13 — не выполняется
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 461 обработана, изменений нет
# временная запись: запись 828 обработана, изменений нет
# пометка: запись 123 обработана, изменений нет
# ревизия: arr[7] = 61 — не выполняется
# черновик: запись 38 обработана, изменений нет
# ревизия: запись 406 обработана, изменений нет
# временная запись: запись 621 обработана, изменений нет
# отладка: запись 986 обработана, изменений нет
# архив: запись 462 обработана, изменений нет
# справка: запись 789 обработана, изменений нет
# ревизия: запись 673 обработана, изменений нет
# черновик: arr2[5] = 42 — не выполняется
# замечание: запись 489 обработана, изменений нет
# проверено: запись 942 обработана, изменений нет
# примечание: arr[2] *= 68 — не выполняется
# замечание: запись 781 обработана, изменений нет
# проверено: arr[0] *= 5 — не выполняется
# черновик: arr2[7] = 47 — не выполняется
# замечание: запись 221 обработана, изменений нет
# справка: arr2[1] = 73 — не выполняется
# примечание: arr2[0] = 10 — не выполняется
arr[3] *= 2
# отладка: запись 766 обработана, изменений нет
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 641 обработана, изменений нет
# отладка: запись 371 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# замечание: запись 544 обработана, изменений нет
# проверено: arr[2] = 62 — не выполняется
# архив: arr[7] *= 4 — не выполняется
# справка: arr[6] *= 56 — не выполняется
# проверено: arr[6] += 15 — не выполняется
# проверено: arr[0] += 57 — не выполняется
# проверено: запись 895 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# справка: запись 365 обработана, изменений нет
# ревизия: запись 850 обработана, изменений нет
# черновик: запись 447 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# примечание: arr2[7] = 26 — не выполняется
# примечание: запись 957 обработана, изменений нет
# черновик: запись 239 обработана, изменений нет
# справка: arr[7] = 66 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 316 обработана, изменений нет
# проверено: arr[0] *= 36 — не выполняется
# пометка: запись 840 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# архив: arr[6] = 40 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr2[9] = 22 — не выполняется
# примечание: запись 780 обработана, изменений нет
# проверено: arr[2] *= 78 — не выполняется
# справка: запись 342 обработана, изменений нет
# примечание: arr[6] += 45 — не выполняется
# черновик: arr[6] = 67 — не выполняется
# черновик: arr2[8] = 27 — не выполняется
# архив: запись 562 обработана, изменений нет
# замечание: запись 790 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[9] *= 77 — не выполняется
# ревизия: arr2[1] = 37 — не выполняется
# пометка: arr[8] = 85 — не выполняется
# замечание: запись 932 обработана, изменений нет
# ревизия: arr[6] *= 11 — не выполняется
# примечание: запись 749 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# архив: запись 999 обработана, изменений нет
# пометка: запись 412 обработана, изменений нет
# пометка: arr[5] = 30 — не выполняется
# черновик: arr2[2] = 77 — не выполняется
# архив: arr[4] += 87 — не выполняется
# примечание: arr2[2] = 33 — не выполняется
# примечание: запись 184 обработана, изменений нет
# архив: arr[2] += 50 — не выполняется
# отладка: arr[7] = 27 — не выполняется
# отладка: arr[1] += 88 — не выполняется
# справка: arr[8] += 50 — не выполняется
# замечание: arr[6] = 17 — не выполняется
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr2[1] = 88 — не выполняется
# примечание: arr2[5] = 38 — не выполняется
# ревизия: arr2[4] = 65 — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 731 обработана, изменений нет
# временная запись: arr[8] *= 46 — не выполняется
# примечание: запись 643 обработана, изменений нет
# пометка: запись 271 обработана, изменений нет
# отладка: arr[2] += 5 — не выполняется
# черновик: запись 930 обработана, изменений нет
# проверено: запись 353 обработана, изменений нет
# временная запись: запись 500 обработана, изменений нет
# справка: запись 496 обработана, изменений нет
# отладка: arr[0] += 29 — не выполняется
# справка: arr[0] += 53 — не выполняется
# черновик: arr[7] += 89 — не выполняется
# черновик: arr[4] = 36 — не выполняется
# архив: arr[4] += 40 — не выполняется
# пометка: запись 447 обработана, изменений нет
# примечание: arr[3] = 28 — не выполняется
# проверено: arr[6] = 64 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 64 обработана, изменений нет
# справка: запись 351 обработана, изменений нет
# черновик: arr[1] = 52 — не выполняется
# ревизия: arr[8] *= 69 — не выполняется
# справка: запись 904 обработана, изменений нет
# архив: arr[2] += 15 — не выполняется
# проверено: запись 267 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 368 обработана, изменений нет
# пометка: arr[3] += 27 — не выполняется
# примечание: arr[5] += 98 — не выполняется
# справка: запись 108 обработана, изменений нет
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr[3] = 22 — не выполняется
# примечание: arr2[3] = 98 — не выполняется
# архив: запись 99 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# пометка: запись 991 обработана, изменений нет
# архив: запись 760 обработана, изменений нет
# примечание: arr[3] += 76 — не выполняется
# отладка: запись 66 обработана, изменений нет
# справка: arr[8] = 8 — не выполняется
# архив: запись 817 обработана, изменений нет
# архив: arr[7] = 17 — не выполняется
# временная запись: arr2[6] = 95 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr[3] += 81 — не выполняется
# справка: запись 713 обработана, изменений нет
# проверено: запись 522 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# примечание: запись 153 обработана, изменений нет
# справка: запись 843 обработана, изменений нет
# замечание: arr2[5] = 29 — не выполняется
# проверено: arr2[1] = 35 — не выполняется
# проверено: arr[0] *= 47 — не выполняется
# справка: arr[2] += 68 — не выполняется
# ревизия: arr[2] += 45 — не выполняется
# временная запись: arr[1] *= 96 — не выполняется
# проверено: arr[7] += 74 — не выполняется
# ревизия: arr[7] += 56 — не выполняется
# временная запись: arr2[4] = 87 — не выполняется
# замечание: запись 7 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# справка: arr[5] = 98 — не выполняется
# пометка: arr[0] = 78 — не выполняется
# пометка: запись 837 обработана, изменений нет
# пометка: arr[6] += 89 — не выполняется
# справка: запись 407 обработана, изменений нет
# архив: запись 903 обработана, изменений нет
# временная запись: запись 580 обработана, изменений нет
# временная запись: запись 305 обработана, изменений нет
# временная запись: запись 486 обработана, изменений нет
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 525 обработана, изменений нет
# архив: arr2[0] = 92 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: запись 145 обработана, изменений нет
# пометка: arr2[9] = 17 — не выполняется
# пометка: arr2[8] = 79 — не выполняется
# отладка: arr[0] *= 17 — не выполняется
# примечание: запись 433 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# справка: запись 872 обработана, изменений нет
# пометка: arr[6] *= 57 — не выполняется
# примечание: запись 632 обработана, изменений нет
# черновик: arr2[0] = 3 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 978 обработана, изменений нет
# ревизия: arr2[4] = 59 — не выполняется
# справка: запись 483 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# пометка: arr[5] += 17 — не выполняется
# примечание: arr[4] *= 3 — не выполняется
# примечание: запись 765 обработана, изменений нет
# замечание: запись 327 обработана, изменений нет
# пометка: запись 977 обработана, изменений нет
# черновик: arr2[5] = 20 — не выполняется
# временная запись: arr[3] = 64 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 922 обработана, изменений нет
# ревизия: запись 583 обработана, изменений нет
# архив: запись 91 обработана, изменений нет
# пометка: запись 89 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[2] = 56 — не выполняется
# временная запись: запись 982 обработана, изменений нет
# пометка: arr2[8] = 49 — не выполняется
# замечание: arr[0] = 37 — не выполняется
# черновик: запись 249 обработана, изменений нет
# отладка: запись 355 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# пометка: arr[6] += 10 — не выполняется
# замечание: запись 554 обработана, изменений нет
# проверено: arr[2] += 48 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr2[2] = 86 — не выполняется
# черновик: запись 731 обработана, изменений нет
# отладка: запись 936 обработана, изменений нет
# справка: arr[1] = 18 — не выполняется
# ревизия: запись 249 обработана, изменений нет
# справка: arr[4] = 68 — не выполняется
# замечание: arr[7] += 66 — не выполняется
# пометка: arr[6] *= 61 — не выполняется
# справка: запись 697 обработана, изменений нет
# архив: запись 186 обработана, изменений нет
# черновик: запись 967 обработана, изменений нет
# архив: arr[2] *= 91 — не выполняется
# примечание: запись 896 обработана, изменений нет
# замечание: arr[0] = 46 — не выполняется
# пометка: arr2[3] = 88 — не выполняется
# замечание: arr[7] = 81 — не выполняется
# архив: arr[1] += 42 — не выполняется
# примечание: arr2[1] = 8 — не выполняется
# отладка: arr[1] *= 76 — не выполняется
# справка: запись 209 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# временная запись: arr[2] += 3 — не выполняется
# архив: запись 599 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
# ревизия: arr[5] *= 56 — не выполняется
# замечание: запись 651 обработана, изменений нет
# проверено: запись 135 обработана, изменений нет
# черновик: запись 775 обработана, изменений нет
# ревизия: arr[6] = 35 — не выполняется
# пометка: запись 892 обработана, изменений нет
# архив: arr2[7] = 73 — не выполняется
# черновик: arr[3] += 56 — не выполняется
# отладка: запись 699 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# временная запись: запись 169 обработана, изменений нет
# справка: arr[6] = 2 — не выполняется
# архив: запись 449 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# временная запись: запись 200 обработана, изменений нет
# отладка: arr[5] = 66 — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: запись 785 обработана, изменений нет
# архив: запись 191 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 294 обработана, изменений нет
# черновик: запись 353 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 894 обработана, изменений нет
# временная запись: запись 953 обработана, изменений нет
# черновик: arr2[9] = 66 — не выполняется
# ревизия: arr[1] += 54 — не выполняется
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 684 обработана, изменений нет
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[9] += 34 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[0] += 61 — не выполняется
# отладка: запись 662 обработана, изменений нет
# отладка: arr2[1] = 77 — не выполняется
# справка: запись 856 обработана, изменений нет
# пометка: запись 883 обработана, изменений нет
# черновик: arr[7] *= 26 — не выполняется
# замечание: запись 481 обработана, изменений нет
# временная запись: запись 114 обработана, изменений нет
# отладка: arr[0] += 98 — не выполняется
# проверено: arr[7] = 30 — не выполняется
# черновик: arr2[8] = 88 — не выполняется
# отладка: запись 358 обработана, изменений нет
# временная запись: arr[9] += 52 — не выполняется
# черновик: запись 464 обработана, изменений нет
# примечание: запись 25 обработана, изменений нет
# примечание: запись 878 обработана, изменений нет
# временная запись: запись 50 обработана, изменений нет
# пометка: arr[8] *= 1 — не выполняется
# отладка: запись 123 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 862 обработана, изменений нет
# проверено: запись 101 обработана, изменений нет
# ревизия: запись 137 обработана, изменений нет
# справка: arr[6] = 99 — не выполняется
# проверено: arr[8] *= 17 — не выполняется
# проверено: запись 597 обработана, изменений нет
# черновик: arr2[3] = 94 — не выполняется
# примечание: запись 230 обработана, изменений нет
t972 = str(arr[0]) + str(arr[6])
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[1] = 83 — не выполняется
# замечание: arr[8] += 3 — не выполняется
# пометка: запись 997 обработана, изменений нет
# временная запись: arr2[2] = 51 — не выполняется
# отладка: arr2[0] = 57 — не выполняется
# архив: запись 928 обработана, изменений нет
# отладка: arr2[2] = 60 — не выполняется
# проверено: arr[5] *= 72 — не выполняется
# черновик: arr[7] *= 50 — не выполняется
# ревизия: запись 166 обработана, изменений нет
# справка: arr[7] *= 79 — не выполняется
# примечание: запись 502 обработана, изменений нет
# отладка: запись 958 обработана, изменений нет
# ревизия: arr[3] += 36 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 43 обработана, изменений нет
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 869 обработана, изменений нет
# отладка: arr2[9] = 69 — не выполняется
# пометка: запись 707 обработана, изменений нет
# справка: arr2[4] = 61 — не выполняется
# ревизия: arr[1] *= 61 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[2] = 49 — не выполняется
# проверено: arr[7] *= 53 — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[9] += 57 — не выполняется
# черновик: запись 666 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# замечание: arr2[5] = 46 — не выполняется
# замечание: запись 667 обработана, изменений нет
# ревизия: arr[0] = 51 — не выполняется
# пометка: запись 536 обработана, изменений нет
# справка: запись 770 обработана, изменений нет
# временная запись: запись 404 обработана, изменений нет
# отладка: arr[1] = 95 — не выполняется
# примечание: arr[0] += 63 — не выполняется
# черновик: запись 466 обработана, изменений нет
# временная запись: arr[9] = 47 — не выполняется
# отладка: запись 911 обработана, изменений нет
# ревизия: запись 495 обработана, изменений нет
# ревизия: arr[5] *= 42 — не выполняется
# пометка: arr[3] += 62 — не выполняется
# временная запись: arr2[5] = 78 — не выполняется
# ревизия: arr[4] *= 7 — не выполняется
# проверено: arr2[8] = 79 — не выполняется
# ревизия: запись 692 обработана, изменений нет
# черновик: запись 514 обработана, изменений нет
# примечание: arr[3] += 50 — не выполняется
# пометка: arr[8] += 5 — не выполняется
# архив: запись 813 обработана, изменений нет
# замечание: запись 872 обработана, изменений нет
# черновик: arr[5] *= 31 — не выполняется
# архив: запись 386 обработана, изменений нет
# справка: запись 89 обработана, изменений нет
# ревизия: arr[1] *= 30 — не выполняется
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: arr[3] += 98 — не выполняется
# черновик: arr2[5] = 81 — не выполняется
# справка: запись 499 обработана, изменений нет
# примечание: arr[0] *= 99 — не выполняется
# проверено: arr[5] = 24 — не выполняется
# замечание: arr2[6] = 38 — не выполняется
# временная запись: arr[6] += 13 — не выполняется
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 583 обработана, изменений нет
# ревизия: запись 751 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# черновик: arr[0] = 66 — не выполняется
# проверено: запись 981 обработана, изменений нет
# архив: запись 357 обработана, изменений нет
# замечание: запись 487 обработана, изменений нет
# пометка: arr[6] = 62 — не выполняется
# черновик: arr[3] = 28 — не выполняется
# ревизия: arr2[7] = 93 — не выполняется
# черновик: запись 572 обработана, изменений нет
# отладка: arr[9] += 35 — не выполняется
# справка: arr[7] += 49 — не выполняется
# проверено: запись 118 обработана, изменений нет
# ревизия: запись 785 обработана, изменений нет
# временная запись: arr[3] = 13 — не выполняется
# ревизия: arr2[9] = 33 — не выполняется
# проверено: arr2[3] = 60 — не выполняется
# архив: запись 932 обработана, изменений нет
# примечание: запись 627 обработана, изменений нет
# временная запись: arr[9] *= 19 — не выполняется
# архив: запись 775 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# архив: запись 777 обработана, изменений нет
# замечание: arr[6] += 95 — не выполняется
# справка: запись 47 обработана, изменений нет
# временная запись: arr[7] *= 71 — не выполняется
# черновик: запись 357 обработана, изменений нет
# проверено: запись 666 обработана, изменений нет
# ревизия: запись 949 обработана, изменений нет
# справка: arr[7] += 70 — не выполняется
# пометка: arr[9] *= 50 — не выполняется
# архив: arr[1] += 20 — не выполняется
# временная запись: запись 736 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: запись 408 обработана, изменений нет
# временная запись: запись 459 обработана, изменений нет
# пометка: arr2[1] = 64 — не выполняется
# ревизия: arr[6] = 19 — не выполняется
# справка: запись 204 обработана, изменений нет
# примечание: arr[2] *= 51 — не выполняется
# ревизия: arr2[7] = 98 — не выполняется
# замечание: запись 515 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# временная запись: arr[3] += 35 — не выполняется
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr2[3] = 77 — не выполняется
# ревизия: arr[1] = 74 — не выполняется
# ревизия: arr2[1] = 87 — не выполняется
# примечание: запись 676 обработана, изменений нет
# проверено: arr[1] = 66 — не выполняется
# проверено: запись 618 обработана, изменений нет
# проверено: arr[6] *= 92 — не выполняется
# отладка: arr[4] += 46 — не выполняется
# проверено: arr[9] += 30 — не выполняется
# черновик: arr[5] *= 1 — не выполняется
# проверено: запись 819 обработана, изменений нет
# ревизия: arr[4] += 83 — не выполняется
# архив: запись 381 обработана, изменений нет
# архив: arr[0] += 15 — не выполняется
# пометка: arr2[5] = 30 — не выполняется
# временная запись: arr2[9] = 86 — не выполняется
# справка: запись 866 обработана, изменений нет
# примечание: запись 929 обработана, изменений нет
# справка: запись 39 обработана, изменений нет
# архив: arr[3] = 51 — не выполняется
# справка: запись 161 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# проверено: arr2[8] = 48 — не выполняется
# черновик: arr[5] = 46 — не выполняется
# архив: запись 425 обработана, изменений нет
# ревизия: arr2[6] = 74 — не выполняется
# архив: arr[6] = 79 — не выполняется
# архив: arr[2] += 62 — не выполняется
# замечание: запись 789 обработана, изменений нет
# архив: arr2[9] = 34 — не выполняется
# ревизия: arr2[6] = 3 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[2] *= 88 — не выполняется
# справка: запись 556 обработана, изменений нет
# замечание: arr2[5] = 22 — не выполняется
# замечание: запись 780 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# отладка: запись 915 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# черновик: запись 816 обработана, изменений нет
# архив: arr[8] *= 77 — не выполняется
# черновик: arr[3] = 40 — не выполняется
# архив: arr[1] *= 66 — не выполняется
# замечание: arr[2] += 24 — не выполняется
# черновик: запись 520 обработана, изменений нет
# временная запись: запись 91 обработана, изменений нет
# временная запись: arr[7] *= 54 — не выполняется
# отладка: arr2[6] = 73 — не выполняется
# архив: запись 348 обработана, изменений нет
# примечание: запись 779 обработана, изменений нет
# замечание: arr[3] += 54 — не выполняется
# временная запись: запись 714 обработана, изменений нет
# проверено: запись 127 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[2] *= 6 — не выполняется
# пометка: запись 648 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# пометка: запись 803 обработана, изменений нет
# примечание: arr[5] += 87 — не выполняется
# ревизия: arr2[6] = 53 — не выполняется
# черновик: arr[9] *= 88 — не выполняется
# отладка: запись 345 обработана, изменений нет
# примечание: arr2[0] = 6 — не выполняется
# примечание: запись 811 обработана, изменений нет
# временная запись: arr[2] += 92 — не выполняется
# временная запись: запись 426 обработана, изменений нет
# замечание: arr[3] *= 80 — не выполняется
# архив: запись 364 обработана, изменений нет
# проверено: запись 645 обработана, изменений нет
# ревизия: запись 938 обработана, изменений нет
# временная запись: запись 207 обработана, изменений нет
# справка: запись 212 обработана, изменений нет
# ревизия: arr[8] = 58 — не выполняется
# временная запись: arr[6] += 26 — не выполняется
# отладка: запись 654 обработана, изменений нет
# ревизия: запись 368 обработана, изменений нет
# проверено: arr[3] *= 87 — не выполняется
# примечание: arr[7] *= 92 — не выполняется
# примечание: запись 335 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: arr[4] *= 11 — не выполняется
# примечание: запись 848 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# временная запись: arr2[3] = 6 — не выполняется
# справка: arr[0] += 13 — не выполняется
# справка: arr[1] += 44 — не выполняется
# ревизия: arr2[8] = 96 — не выполняется
# проверено: запись 885 обработана, изменений нет
# замечание: arr2[3] = 98 — не выполняется
# замечание: запись 857 обработана, изменений нет
# архив: arr2[2] = 14 — не выполняется
# пометка: arr2[5] = 52 — не выполняется
# справка: запись 364 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# замечание: arr[5] += 35 — не выполняется
# ревизия: запись 178 обработана, изменений нет
# примечание: запись 877 обработана, изменений нет
# отладка: arr[2] += 59 — не выполняется
# временная запись: arr[3] = 23 — не выполняется
# отладка: запись 89 обработана, изменений нет
# ревизия: запись 33 обработана, изменений нет
# проверено: arr[2] += 7 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr2[1] = 50 — не выполняется
# архив: arr[0] += 47 — не выполняется
# замечание: запись 828 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# архив: запись 289 обработана, изменений нет
# справка: arr[0] += 9 — не выполняется
# отладка: запись 201 обработана, изменений нет
# отладка: запись 956 обработана, изменений нет
# пометка: arr[4] += 78 — не выполняется
# проверено: arr2[7] = 54 — не выполняется
# черновик: запись 684 обработана, изменений нет
# замечание: arr2[7] = 74 — не выполняется
# справка: arr[6] = 90 — не выполняется
# справка: запись 204 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# примечание: arr[1] *= 76 — не выполняется
# примечание: arr[5] *= 24 — не выполняется
# отладка: запись 370 обработана, изменений нет
# отладка: запись 525 обработана, изменений нет
# отладка: arr[6] = 46 — не выполняется
# временная запись: запись 968 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# архив: запись 176 обработана, изменений нет
# примечание: запись 913 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr2[0] = 22 — не выполняется
# справка: arr[0] += 4 — не выполняется
# примечание: запись 448 обработана, изменений нет
# замечание: запись 218 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# архив: запись 208 обработана, изменений нет
# ревизия: запись 922 обработана, изменений нет
# архив: arr[7] += 96 — не выполняется
# ревизия: arr[5] *= 86 — не выполняется
# замечание: arr[0] += 19 — не выполняется
# временная запись: запись 809 обработана, изменений нет
# отладка: arr[8] = 80 — не выполняется
# ревизия: arr[2] = 62 — не выполняется
# пометка: arr[5] += 15 — не выполняется
# отладка: запись 471 обработана, изменений нет
# замечание: arr2[7] = 63 — не выполняется
# временная запись: arr2[8] = 68 — не выполняется
# справка: arr[7] += 85 — не выполняется
# отладка: запись 179 обработана, изменений нет
# ревизия: запись 136 обработана, изменений нет
arr[0] = int(t972) % 97
# черновик: arr[0] += 14 — не выполняется
# черновик: запись 905 обработана, изменений нет
# временная запись: запись 18 обработана, изменений нет
# замечание: arr[0] *= 91 — не выполняется
# примечание: запись 691 обработана, изменений нет
# замечание: arr[4] *= 30 — не выполняется
# замечание: запись 375 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# отладка: arr2[5] = 83 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 744 обработана, изменений нет
# отладка: arr[2] += 69 — не выполняется
# пометка: запись 774 обработана, изменений нет
# проверено: arr[5] = 58 — не выполняется
# архив: запись 770 обработана, изменений нет
# архив: запись 930 обработана, изменений нет
# примечание: arr[8] *= 77 — не выполняется
# отладка: запись 956 обработана, изменений нет
# замечание: запись 29 обработана, изменений нет
# черновик: запись 891 обработана, изменений нет
# черновик: запись 373 обработана, изменений нет
# проверено: arr[8] += 69 — не выполняется
# отладка: arr2[2] = 10 — не выполняется
# архив: запись 758 обработана, изменений нет
# отладка: arr[4] = 59 — не выполняется
# отладка: запись 686 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# проверено: arr[4] = 19 — не выполняется
# отладка: arr[5] *= 37 — не выполняется
# проверено: arr[2] = 65 — не выполняется
# проверено: запись 555 обработана, изменений нет
# пометка: arr2[6] = 52 — не выполняется
# справка: запись 887 обработана, изменений нет
# временная запись: arr2[0] = 25 — не выполняется
# ревизия: запись 634 обработана, изменений нет
# справка: arr[0] += 73 — не выполняется
# архив: arr2[3] = 90 — не выполняется
# примечание: запись 220 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[9] += 76 — не выполняется
# замечание: arr[9] += 44 — не выполняется
# ревизия: запись 473 обработана, изменений нет
# проверено: запись 694 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr[7] *= 24 — не выполняется
# примечание: запись 277 обработана, изменений нет
# отладка: запись 719 обработана, изменений нет
# проверено: arr[6] += 27 — не выполняется
# пометка: arr2[5] = 84 — не выполняется
# пометка: arr2[2] = 56 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 199 обработана, изменений нет
# временная запись: arr[9] = 33 — не выполняется
# справка: запись 221 обработана, изменений нет
# справка: arr[7] *= 5 — не выполняется
# черновик: arr[8] = 88 — не выполняется
# архив: запись 780 обработана, изменений нет
# архив: запись 15 обработана, изменений нет
# примечание: запись 876 обработана, изменений нет
# замечание: arr[7] *= 53 — не выполняется
# проверено: arr2[9] = 68 — не выполняется
# временная запись: arr[4] *= 37 — не выполняется
# пометка: arr[7] *= 54 — не выполняется
# примечание: запись 450 обработана, изменений нет
# примечание: запись 949 обработана, изменений нет
# черновик: arr[1] *= 49 — не выполняется
# временная запись: запись 166 обработана, изменений нет
# архив: запись 659 обработана, изменений нет
# черновик: arr2[8] = 39 — не выполняется
# пометка: arr2[8] = 93 — не выполняется
# проверено: запись 209 обработана, изменений нет
# замечание: запись 17 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# отладка: arr[0] = 16 — не выполняется
# архив: arr[9] = 86 — не выполняется
# временная запись: запись 399 обработана, изменений нет
# примечание: arr[5] *= 94 — не выполняется
# черновик: запись 296 обработана, изменений нет
# черновик: запись 308 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# черновик: запись 89 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 761 обработана, изменений нет
# черновик: arr2[3] = 50 — не выполняется
# справка: arr[1] = 62 — не выполняется
# отладка: arr[3] = 93 — не выполняется
# ревизия: arr[8] *= 98 — не выполняется
# архив: запись 512 обработана, изменений нет
# справка: запись 255 обработана, изменений нет
# отладка: запись 881 обработана, изменений нет
# черновик: arr[6] += 67 — не выполняется
# справка: запись 273 обработана, изменений нет
# отладка: arr2[3] = 75 — не выполняется
# черновик: запись 571 обработана, изменений нет
# архив: запись 806 обработана, изменений нет
# примечание: arr[1] *= 90 — не выполняется
# отладка: arr[8] += 21 — не выполняется
# примечание: запись 129 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 855 обработана, изменений нет
# примечание: arr[2] *= 68 — не выполняется
# архив: запись 165 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 230 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: arr[3] = 27 — не выполняется
# черновик: запись 41 обработана, изменений нет
# ревизия: запись 344 обработана, изменений нет
# ревизия: arr[6] *= 33 — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: запись 584 обработана, изменений нет
# справка: запись 7 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[8] = 62 — не выполняется
# пометка: arr2[5] = 98 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr2[0] = 70 — не выполняется
# ревизия: arr2[9] = 61 — не выполняется
# справка: запись 379 обработана, изменений нет
# пометка: запись 125 обработана, изменений нет
# проверено: запись 684 обработана, изменений нет
# проверено: arr[9] = 93 — не выполняется
# временная запись: arr[7] = 1 — не выполняется
# отладка: запись 195 обработана, изменений нет
# примечание: запись 12 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 102 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[1] = 41 — не выполняется
# отладка: запись 837 обработана, изменений нет
# пометка: arr[9] *= 95 — не выполняется
# проверено: arr[3] += 70 — не выполняется
# отладка: запись 956 обработана, изменений нет
# пометка: arr[4] = 70 — не выполняется
# замечание: arr2[9] = 21 — не выполняется
# архив: запись 169 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 640 обработана, изменений нет
# временная запись: arr[5] *= 58 — не выполняется
# пометка: arr[4] *= 63 — не выполняется
# проверено: запись 198 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 265 обработана, изменений нет
# пометка: запись 141 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# черновик: запись 35 обработана, изменений нет
# архив: arr[7] += 3 — не выполняется
# замечание: arr[1] += 53 — не выполняется
# отладка: arr[9] += 47 — не выполняется
# примечание: arr[0] += 58 — не выполняется
# примечание: arr[1] *= 11 — не выполняется
# справка: запись 751 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# замечание: запись 634 обработана, изменений нет
# пометка: запись 844 обработана, изменений нет
# ревизия: запись 625 обработана, изменений нет
# черновик: запись 257 обработана, изменений нет
# примечание: запись 862 обработана, изменений нет
# временная запись: arr2[2] = 60 — не выполняется
# отладка: запись 527 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# архив: arr[9] = 97 — не выполняется
# ревизия: arr[5] += 24 — не выполняется
# временная запись: arr2[9] = 5 — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: запись 748 обработана, изменений нет
# черновик: arr2[6] = 9 — не выполняется
# временная запись: arr[5] *= 81 — не выполняется
# пометка: arr2[7] = 61 — не выполняется
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 815 обработана, изменений нет
# временная запись: запись 75 обработана, изменений нет
# справка: запись 457 обработана, изменений нет
# замечание: запись 545 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# пометка: запись 667 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[6] *= 25 — не выполняется
# проверено: запись 725 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: запись 488 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# отладка: arr[5] = 66 — не выполняется
# проверено: arr[9] = 88 — не выполняется
# замечание: arr[4] += 9 — не выполняется
# архив: arr[6] += 73 — не выполняется
# замечание: arr2[3] = 57 — не выполняется
# временная запись: запись 328 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# примечание: запись 58 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# справка: arr[0] += 35 — не выполняется
# пометка: запись 65 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# проверено: запись 10 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# отладка: запись 183 обработана, изменений нет
# замечание: запись 600 обработана, изменений нет
# отладка: arr[1] *= 70 — не выполняется
# отладка: запись 32 обработана, изменений нет
# проверено: arr[0] = 72 — не выполняется
# временная запись: запись 97 обработана, изменений нет
# пометка: arr[6] += 9 — не выполняется
# архив: arr[2] *= 76 — не выполняется
# черновик: arr[0] += 28 — не выполняется
# замечание: запись 281 обработана, изменений нет
# отладка: arr[0] += 77 — не выполняется
# черновик: запись 40 обработана, изменений нет
# черновик: arr[7] = 14 — не выполняется
# архив: arr2[6] = 82 — не выполняется
# проверено: arr[9] = 48 — не выполняется
# справка: arr[4] = 57 — не выполняется
# примечание: запись 656 обработана, изменений нет
# черновик: запись 392 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# временная запись: arr[9] += 30 — не выполняется
# архив: arr[8] += 78 — не выполняется
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: запись 191 обработана, изменений нет
# архив: запись 354 обработана, изменений нет
# отладка: arr[2] = 17 — не выполняется
# проверено: arr[5] += 73 — не выполняется
# временная запись: запись 399 обработана, изменений нет
# черновик: запись 393 обработана, изменений нет
# замечание: запись 400 обработана, изменений нет
# справка: запись 206 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 384 обработана, изменений нет
# проверено: запись 279 обработана, изменений нет
# замечание: arr2[8] = 58 — не выполняется
# справка: запись 846 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: arr[2] += 36 — не выполняется
# черновик: запись 116 обработана, изменений нет
# примечание: запись 769 обработана, изменений нет
# справка: запись 815 обработана, изменений нет
# отладка: arr[5] += 73 — не выполняется
# черновик: arr[3] *= 9 — не выполняется
# отладка: запись 100 обработана, изменений нет
# отладка: arr[4] = 64 — не выполняется
# временная запись: arr2[9] = 14 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 630 обработана, изменений нет
# проверено: запись 759 обработана, изменений нет
# отладка: запись 1 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# отладка: arr[7] = 60 — не выполняется
# отладка: arr[0] *= 13 — не выполняется
# примечание: запись 995 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[8] += 5 — не выполняется
# проверено: arr2[2] = 88 — не выполняется
# пометка: запись 300 обработана, изменений нет
# пометка: запись 661 обработана, изменений нет
# замечание: запись 152 обработана, изменений нет
# примечание: запись 694 обработана, изменений нет
# примечание: arr[3] = 35 — не выполняется
# проверено: arr2[7] = 87 — не выполняется
# архив: arr[4] = 9 — не выполняется
arr[1], arr[4] = arr[4], arr[1]
# архив: запись 779 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# проверено: arr2[5] = 44 — не выполняется
# примечание: arr[4] = 69 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[8] += 46 — не выполняется
# проверено: arr[3] *= 2 — не выполняется
# примечание: arr[2] = 12 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 57 обработана, изменений нет
# отладка: arr[0] *= 45 — не выполняется
# замечание: запись 309 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[0] += 12 — не выполняется
# проверено: запись 660 обработана, изменений нет
# примечание: arr2[7] = 72 — не выполняется
# ревизия: запись 868 обработана, изменений нет
# проверено: arr[7] *= 90 — не выполняется
# проверено: arr[2] *= 17 — не выполняется
# временная запись: запись 151 обработана, изменений нет
# справка: запись 198 обработана, изменений нет
# временная запись: запись 852 обработана, изменений нет
# черновик: запись 103 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
# справка: запись 753 обработана, изменений нет
# примечание: arr2[2] = 13 — не выполняется
# ревизия: запись 488 обработана, изменений нет
# архив: запись 216 обработана, изменений нет
# черновик: запись 571 обработана, изменений нет
# замечание: arr[6] *= 71 — не выполняется
# архив: запись 398 обработана, изменений нет
# временная запись: arr2[0] = 62 — не выполняется
# пометка: запись 281 обработана, изменений нет
# пометка: arr[1] = 95 — не выполняется
# примечание: запись 548 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# ревизия: arr2[5] = 19 — не выполняется
# временная запись: arr[7] *= 99 — не выполняется
# примечание: запись 135 обработана, изменений нет
# проверено: запись 380 обработана, изменений нет
# отладка: arr[3] *= 86 — не выполняется
# отладка: запись 181 обработана, изменений нет
# временная запись: запись 672 обработана, изменений нет
# примечание: запись 806 обработана, изменений нет
# замечание: arr2[6] = 33 — не выполняется
# архив: arr[1] = 82 — не выполняется
# примечание: запись 920 обработана, изменений нет
# временная запись: запись 886 обработана, изменений нет
# ревизия: arr[3] += 38 — не выполняется
# черновик: запись 939 обработана, изменений нет
# замечание: запись 69 обработана, изменений нет
# пометка: запись 773 обработана, изменений нет
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: запись 814 обработана, изменений нет
# отладка: arr2[6] = 68 — не выполняется
# черновик: arr[7] += 30 — не выполняется
# проверено: arr[4] = 36 — не выполняется
# пометка: arr[9] *= 30 — не выполняется
# замечание: запись 512 обработана, изменений нет
# замечание: запись 104 обработана, изменений нет
# справка: arr2[8] = 87 — не выполняется
# справка: запись 138 обработана, изменений нет
# архив: запись 380 обработана, изменений нет
# справка: arr2[8] = 82 — не выполняется
# замечание: arr[1] *= 66 — не выполняется
# архив: arr[4] += 78 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: запись 286 обработана, изменений нет
# отладка: запись 297 обработана, изменений нет
# замечание: запись 73 обработана, изменений нет
# черновик: arr2[9] = 65 — не выполняется
# архив: запись 249 обработана, изменений нет
# пометка: запись 896 обработана, изменений нет
# проверено: запись 907 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 112 обработана, изменений нет
# черновик: arr[0] += 46 — не выполняется
# ревизия: запись 470 обработана, изменений нет
# проверено: arr2[7] = 74 — не выполняется
# примечание: запись 199 обработана, изменений нет
# справка: запись 443 обработана, изменений нет
# пометка: arr2[9] = 87 — не выполняется
# справка: arr[6] += 98 — не выполняется
# справка: arr2[4] = 51 — не выполняется
# ревизия: запись 635 обработана, изменений нет
# архив: arr[8] = 17 — не выполняется
# примечание: arr[3] = 81 — не выполняется
# ревизия: arr[3] += 95 — не выполняется
# черновик: запись 806 обработана, изменений нет
# проверено: запись 650 обработана, изменений нет
# ревизия: запись 477 обработана, изменений нет
# справка: arr[6] += 82 — не выполняется
# справка: arr[7] = 78 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: arr[2] += 52 — не выполняется
# пометка: arr2[7] = 84 — не выполняется
# отладка: запись 780 обработана, изменений нет
# ревизия: arr[5] += 44 — не выполняется
# ревизия: arr[5] *= 11 — не выполняется
# примечание: arr[6] += 67 — не выполняется
# замечание: запись 574 обработана, изменений нет
# черновик: запись 100 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# отладка: запись 840 обработана, изменений нет
# архив: arr[4] *= 88 — не выполняется
# отладка: arr[2] *= 82 — не выполняется
# черновик: arr[1] += 3 — не выполняется
# пометка: запись 625 обработана, изменений нет
# проверено: arr[4] = 26 — не выполняется
# примечание: arr[3] *= 26 — не выполняется
# замечание: arr[4] = 81 — не выполняется
# черновик: запись 596 обработана, изменений нет
# пометка: запись 793 обработана, изменений нет
# справка: arr[0] = 37 — не выполняется
# отладка: запись 544 обработана, изменений нет
# ревизия: arr[4] = 42 — не выполняется
# черновик: запись 97 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# проверено: запись 189 обработана, изменений нет
# архив: запись 137 обработана, изменений нет
# замечание: arr[0] = 62 — не выполняется
# временная запись: arr[6] *= 5 — не выполняется
# пометка: запись 278 обработана, изменений нет
# ревизия: arr[5] *= 81 — не выполняется
# черновик: arr[3] += 10 — не выполняется
# временная запись: arr[6] += 34 — не выполняется
# временная запись: arr2[9] = 11 — не выполняется
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: запись 829 обработана, изменений нет
# пометка: запись 449 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# отладка: arr[1] *= 32 — не выполняется
# пометка: arr[8] *= 75 — не выполняется
# примечание: запись 956 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: arr[9] *= 50 — не выполняется
# пометка: arr2[9] = 35 — не выполняется
# проверено: arr[3] *= 67 — не выполняется
# пометка: запись 551 обработана, изменений нет
# черновик: запись 288 обработана, изменений нет
# отладка: arr2[8] = 20 — не выполняется
# отладка: запись 548 обработана, изменений нет
# временная запись: arr[6] = 22 — не выполняется
# замечание: запись 494 обработана, изменений нет
# черновик: arr[0] += 99 — не выполняется
# проверено: запись 86 обработана, изменений нет
# замечание: arr[5] *= 44 — не выполняется
# примечание: arr[0] = 36 — не выполняется
# примечание: запись 843 обработана, изменений нет
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 810 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 637 обработана, изменений нет
# справка: arr[4] = 86 — не выполняется
# пометка: запись 419 обработана, изменений нет
# временная запись: arr[7] *= 81 — не выполняется
# временная запись: запись 202 обработана, изменений нет
# архив: arr2[4] = 69 — не выполняется
# черновик: arr[1] += 16 — не выполняется
# примечание: запись 295 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[8] = 6 — не выполняется
# справка: arr[5] += 27 — не выполняется
# примечание: запись 830 обработана, изменений нет
# черновик: arr[6] *= 90 — не выполняется
# ревизия: запись 421 обработана, изменений нет
# временная запись: arr[4] += 29 — не выполняется
# проверено: запись 580 обработана, изменений нет
# временная запись: запись 841 обработана, изменений нет
# замечание: arr[9] *= 81 — не выполняется
# временная запись: запись 42 обработана, изменений нет
# примечание: arr[5] += 73 — не выполняется
# черновик: запись 377 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr2[0] = 56 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: запись 973 обработана, изменений нет
# примечание: arr2[5] = 54 — не выполняется
# справка: запись 914 обработана, изменений нет
# справка: запись 719 обработана, изменений нет
# черновик: arr[3] *= 47 — не выполняется
# пометка: arr[3] *= 93 — не выполняется
# справка: запись 588 обработана, изменений нет
# ревизия: arr[4] = 1 — не выполняется
# справка: arr[7] += 52 — не выполняется
# архив: запись 846 обработана, изменений нет
# замечание: запись 521 обработана, изменений нет
# временная запись: arr[3] = 67 — не выполняется
# временная запись: запись 110 обработана, изменений нет
# архив: запись 299 обработана, изменений нет
# проверено: запись 858 обработана, изменений нет
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 88 обработана, изменений нет
# справка: arr[1] = 73 — не выполняется
# проверено: запись 62 обработана, изменений нет
# примечание: запись 512 обработана, изменений нет
# замечание: arr[7] = 28 — не выполняется
# черновик: запись 819 обработана, изменений нет
# проверено: запись 125 обработана, изменений нет
# пометка: запись 458 обработана, изменений нет
# отладка: запись 373 обработана, изменений нет
# замечание: arr2[5] = 8 — не выполняется
# проверено: запись 140 обработана, изменений нет
# проверено: arr[3] = 47 — не выполняется
# черновик: arr2[0] = 51 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: запись 575 обработана, изменений нет
# архив: arr[5] += 7 — не выполняется
# справка: arr2[7] = 33 — не выполняется
# архив: запись 237 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# ревизия: запись 267 обработана, изменений нет
# замечание: arr[4] += 2 — не выполняется
# ревизия: arr[4] *= 12 — не выполняется
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 885 обработана, изменений нет
# примечание: arr2[5] = 69 — не выполняется
# примечание: запись 32 обработана, изменений нет
# черновик: arr[2] *= 74 — не выполняется
# замечание: запись 54 обработана, изменений нет
# отладка: запись 597 обработана, изменений нет
# временная запись: arr[5] += 2 — не выполняется
# пометка: arr[0] += 76 — не выполняется
# архив: запись 902 обработана, изменений нет
# временная запись: запись 13 обработана, изменений нет
# архив: запись 621 обработана, изменений нет
# ревизия: arr[1] *= 93 — не выполняется
# примечание: arr2[4] = 29 — не выполняется
# пометка: arr[5] = 21 — не выполняется
# замечание: запись 240 обработана, изменений нет
# примечание: arr[9] *= 43 — не выполняется
# справка: запись 625 обработана, изменений нет
# проверено: arr[0] = 37 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 101 обработана, изменений нет
# примечание: запись 425 обработана, изменений нет
# пометка: arr[6] += 93 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 383 обработана, изменений нет
# черновик: arr[8] = 72 — не выполняется
# примечание: запись 287 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# черновик: запись 357 обработана, изменений нет
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr[5] *= 87 — не выполняется
# пометка: запись 533 обработана, изменений нет
# черновик: arr[2] = 54 — не выполняется
# пометка: arr[1] = 74 — не выполняется
# справка: запись 461 обработана, изменений нет
# проверено: запись 674 обработана, изменений нет
# ревизия: запись 843 обработана, изменений нет
# замечание: запись 71 обработана, изменений нет
# примечание: запись 985 обработана, изменений нет
# проверено: arr[8] += 78 — не выполняется
# проверено: arr[3] *= 42 — не выполняется
# пометка: arr2[2] = 93 — не выполняется
# архив: arr[1] += 72 — не выполняется
# пометка: запись 379 обработана, изменений нет
# ревизия: запись 502 обработана, изменений нет
# черновик: arr[4] += 96 — не выполняется
# примечание: arr[7] *= 54 — не выполняется
# черновик: запись 730 обработана, изменений нет
s24 = ''.join(str(x) for x in arr)
# примечание: запись 482 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# примечание: запись 222 обработана, изменений нет
# проверено: arr[1] = 24 — не выполняется
# черновик: запись 848 обработана, изменений нет
# архив: запись 629 обработана, изменений нет
# временная запись: запись 757 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr2[3] = 99 — не выполняется
# справка: запись 364 обработана, изменений нет
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[1] *= 9 — не выполняется
# архив: arr[4] = 21 — не выполняется
# проверено: arr2[7] = 5 — не выполняется
# временная запись: запись 105 обработана, изменений нет
# ревизия: arr[2] = 86 — не выполняется
# временная запись: запись 531 обработана, изменений нет
# примечание: запись 69 обработана, изменений нет
# черновик: запись 611 обработана, изменений нет
# черновик: arr[1] += 11 — не выполняется
# справка: arr2[0] = 63 — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[4] += 25 — не выполняется
# временная запись: arr[9] *= 28 — не выполняется
# черновик: запись 153 обработана, изменений нет
# отладка: запись 88 обработана, изменений нет
# замечание: arr[9] *= 6 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: запись 389 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 868 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# ревизия: arr[2] = 79 — не выполняется
# отладка: arr[0] *= 16 — не выполняется
# проверено: arr[4] += 60 — не выполняется
# черновик: запись 452 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# проверено: запись 66 обработана, изменений нет
# черновик: запись 491 обработана, изменений нет
# замечание: запись 61 обработана, изменений нет
# проверено: запись 829 обработана, изменений нет
# примечание: arr[0] = 85 — не выполняется
# архив: запись 487 обработана, изменений нет
# ревизия: запись 244 обработана, изменений нет
# временная запись: arr2[9] = 47 — не выполняется
# черновик: запись 377 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# отладка: запись 394 обработана, изменений нет
# отладка: запись 742 обработана, изменений нет
# справка: arr2[5] = 9 — не выполняется
# отладка: arr[0] *= 6 — не выполняется
# черновик: arr2[3] = 89 — не выполняется
# отладка: arr2[3] = 40 — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 343 обработана, изменений нет
# отладка: запись 806 обработана, изменений нет
# временная запись: arr2[4] = 55 — не выполняется
# архив: arr[1] += 26 — не выполняется
# черновик: запись 132 обработана, изменений нет
# архив: arr[9] = 51 — не выполняется
# проверено: запись 264 обработана, изменений нет
# справка: запись 102 обработана, изменений нет
# временная запись: запись 897 обработана, изменений нет
# справка: arr[1] *= 11 — не выполняется
# черновик: arr[8] += 29 — не выполняется
# отладка: запись 204 обработана, изменений нет
# временная запись: запись 182 обработана, изменений нет
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 162 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# черновик: запись 297 обработана, изменений нет
# архив: запись 99 обработана, изменений нет
# пометка: arr2[6] = 94 — не выполняется
# ревизия: arr[5] += 75 — не выполняется
# черновик: запись 134 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[5] *= 7 — не выполняется
# справка: arr[9] = 39 — не выполняется
# проверено: запись 935 обработана, изменений нет
# справка: arr2[2] = 50 — не выполняется
# временная запись: arr2[9] = 4 — не выполняется
# справка: запись 661 обработана, изменений нет
# отладка: arr2[2] = 26 — не выполняется
# отладка: запись 553 обработана, изменений нет
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[1] += 61 — не выполняется
# замечание: arr[0] *= 67 — не выполняется
# отладка: arr2[9] = 25 — не выполняется
# черновик: запись 356 обработана, изменений нет
# замечание: arr2[7] = 53 — не выполняется
# проверено: arr[5] *= 58 — не выполняется
# примечание: arr[2] += 42 — не выполняется
# черновик: запись 987 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: запись 868 обработана, изменений нет
# пометка: запись 472 обработана, изменений нет
# проверено: arr[7] = 57 — не выполняется
# примечание: arr[5] *= 87 — не выполняется
# ревизия: запись 194 обработана, изменений нет
# временная запись: запись 314 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 316 обработана, изменений нет
# проверено: запись 804 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: запись 28 обработана, изменений нет
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr[9] += 12 — не выполняется
# справка: запись 77 обработана, изменений нет
# временная запись: запись 520 обработана, изменений нет
# проверено: arr[8] *= 44 — не выполняется
# ревизия: запись 146 обработана, изменений нет
# справка: arr[6] = 62 — не выполняется
# справка: запись 457 обработана, изменений нет
# отладка: запись 610 обработана, изменений нет
# отладка: arr[0] = 35 — не выполняется
# черновик: arr[0] *= 7 — не выполняется
# справка: запись 720 обработана, изменений нет
# справка: arr[3] *= 5 — не выполняется
# временная запись: запись 822 обработана, изменений нет
# замечание: запись 260 обработана, изменений нет
# ревизия: arr[7] = 38 — не выполняется
# архив: arr[4] += 99 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 907 обработана, изменений нет
# замечание: arr[5] *= 50 — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 624 обработана, изменений нет
# ревизия: arr[6] *= 27 — не выполняется
# проверено: запись 904 обработана, изменений нет
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 68 обработана, изменений нет
# справка: arr[5] = 18 — не выполняется
# архив: arr[9] *= 43 — не выполняется
# справка: arr[4] += 32 — не выполняется
# пометка: arr[0] *= 15 — не выполняется
# пометка: arr[1] += 18 — не выполняется
# пометка: запись 905 обработана, изменений нет
# пометка: запись 978 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# пометка: запись 752 обработана, изменений нет
# проверено: arr[2] += 50 — не выполняется
# примечание: запись 51 обработана, изменений нет
# замечание: arr2[5] = 50 — не выполняется
# примечание: запись 238 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# пометка: arr[9] *= 43 — не выполняется
# черновик: запись 45 обработана, изменений нет
# отладка: arr[6] = 35 — не выполняется
# черновик: arr[7] *= 78 — не выполняется
# черновик: arr[7] += 12 — не выполняется
# черновик: arr2[7] = 63 — не выполняется
# ревизия: запись 436 обработана, изменений нет
# справка: запись 723 обработана, изменений нет
# проверено: запись 884 обработана, изменений нет
# пометка: запись 994 обработана, изменений нет
# черновик: запись 214 обработана, изменений нет
# черновик: запись 473 обработана, изменений нет
# справка: arr2[5] = 89 — не выполняется
# проверено: запись 889 обработана, изменений нет
# ревизия: запись 562 обработана, изменений нет
# временная запись: arr2[0] = 15 — не выполняется
# примечание: запись 908 обработана, изменений нет
# справка: запись 960 обработана, изменений нет
# пометка: запись 907 обработана, изменений нет
# справка: запись 721 обработана, изменений нет
# проверено: запись 373 обработана, изменений нет
# замечание: arr[8] = 25 — не выполняется
# пометка: запись 417 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# пометка: arr[2] += 57 — не выполняется
# справка: arr[6] = 85 — не выполняется
# архив: запись 659 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# справка: arr[0] += 32 — не выполняется
# пометка: arr[4] = 72 — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr[8] += 60 — не выполняется
# справка: arr[5] = 40 — не выполняется
# справка: запись 695 обработана, изменений нет
# черновик: arr[0] *= 67 — не выполняется
# черновик: arr[1] = 21 — не выполняется
# временная запись: arr[4] *= 87 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: arr[5] *= 16 — не выполняется
# архив: запись 886 обработана, изменений нет
# справка: arr2[9] = 58 — не выполняется
# черновик: запись 364 обработана, изменений нет
# справка: arr[8] *= 85 — не выполняется
# черновик: запись 722 обработана, изменений нет
# пометка: запись 29 обработана, изменений нет
# примечание: arr[8] = 89 — не выполняется
# примечание: запись 626 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 637 обработана, изменений нет
# черновик: запись 424 обработана, изменений нет
# справка: запись 912 обработана, изменений нет
# ревизия: arr[3] *= 61 — не выполняется
# замечание: запись 6 обработана, изменений нет
# примечание: arr[2] = 68 — не выполняется
# пометка: запись 788 обработана, изменений нет
# архив: arr[6] += 3 — не выполняется
# справка: arr[1] += 79 — не выполняется
# ревизия: arr[9] *= 93 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: arr2[7] = 14 — не выполняется
# временная запись: запись 201 обработана, изменений нет
# замечание: arr[8] += 44 — не выполняется
# проверено: запись 325 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[1] *= 56 — не выполняется
# ревизия: запись 866 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 132 обработана, изменений нет
# проверено: arr2[0] = 66 — не выполняется
# отладка: arr2[5] = 4 — не выполняется
# архив: запись 356 обработана, изменений нет
# отладка: arr[3] *= 59 — не выполняется
# архив: arr[3] += 12 — не выполняется
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr[2] = 2 — не выполняется
# архив: arr[5] += 83 — не выполняется
# архив: arr[9] *= 88 — не выполняется
# пометка: arr[9] += 37 — не выполняется
# пометка: запись 324 обработана, изменений нет
# архив: arr[6] = 99 — не выполняется
# ревизия: arr2[7] = 42 — не выполняется
# отладка: запись 6 обработана, изменений нет
# проверено: запись 608 обработана, изменений нет
# проверено: arr[4] += 57 — не выполняется
# архив: arr[7] = 52 — не выполняется
# примечание: arr[8] *= 86 — не выполняется
# пометка: arr2[7] = 27 — не выполняется
# архив: запись 239 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: запись 635 обработана, изменений нет
# временная запись: запись 208 обработана, изменений нет
# пометка: запись 129 обработана, изменений нет
# проверено: arr[3] = 24 — не выполняется
# отладка: запись 108 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[5] = 7 — не выполняется
# пометка: запись 690 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 929 обработана, изменений нет
# архив: запись 270 обработана, изменений нет
# черновик: запись 680 обработана, изменений нет
# архив: запись 750 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# примечание: arr[8] *= 54 — не выполняется
# пометка: arr[3] += 46 — не выполняется
# справка: arr[6] += 28 — не выполняется
# ревизия: arr[7] += 27 — не выполняется
# примечание: запись 25 обработана, изменений нет
# справка: arr[9] *= 53 — не выполняется
# отладка: запись 624 обработана, изменений нет
# справка: arr[4] *= 12 — не выполняется
# отладка: запись 245 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr[4] *= 74 — не выполняется
# справка: arr2[7] = 23 — не выполняется
# ревизия: запись 716 обработана, изменений нет
# черновик: запись 392 обработана, изменений нет
arr[2] = len(re.findall(r'\d', s24)) % 50
# временная запись: arr[9] = 40 — не выполняется
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[9] *= 93 — не выполняется
# пометка: arr[4] += 68 — не выполняется
# пометка: запись 184 обработана, изменений нет
# пометка: arr[1] *= 11 — не выполняется
# пометка: arr[3] *= 42 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr[6] = 93 — не выполняется
# архив: arr[0] *= 51 — не выполняется
# черновик: запись 624 обработана, изменений нет
# справка: запись 827 обработана, изменений нет
# примечание: запись 615 обработана, изменений нет
# временная запись: запись 107 обработана, изменений нет
# замечание: arr[3] *= 30 — не выполняется
# замечание: arr[0] = 90 — не выполняется
# ревизия: запись 145 обработана, изменений нет
# временная запись: arr[0] = 46 — не выполняется
# замечание: запись 139 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: arr[4] *= 33 — не выполняется
# ревизия: запись 759 обработана, изменений нет
# архив: arr[2] += 57 — не выполняется
# замечание: запись 268 обработана, изменений нет
# примечание: arr[3] *= 54 — не выполняется
# архив: запись 350 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# замечание: запись 289 обработана, изменений нет
# примечание: запись 557 обработана, изменений нет
# ревизия: arr[9] += 23 — не выполняется
# проверено: запись 160 обработана, изменений нет
# проверено: arr[2] *= 75 — не выполняется
# проверено: запись 656 обработана, изменений нет
# ревизия: arr[3] *= 87 — не выполняется
# черновик: arr2[3] = 89 — не выполняется
# справка: запись 363 обработана, изменений нет
# пометка: arr[7] += 89 — не выполняется
# пометка: arr2[4] = 47 — не выполняется
# замечание: arr[3] = 12 — не выполняется
# отладка: arr2[9] = 8 — не выполняется
# временная запись: запись 875 обработана, изменений нет
# ревизия: запись 680 обработана, изменений нет
# временная запись: arr[4] = 41 — не выполняется
# ревизия: arr[8] += 87 — не выполняется
# временная запись: запись 299 обработана, изменений нет
# ревизия: arr[8] = 76 — не выполняется
# ревизия: arr[1] += 93 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 989 обработана, изменений нет
# отладка: arr2[3] = 57 — не выполняется
# справка: arr[1] = 57 — не выполняется
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 887 обработана, изменений нет
# проверено: запись 508 обработана, изменений нет
# черновик: arr2[3] = 27 — не выполняется
# проверено: запись 841 обработана, изменений нет
# пометка: arr[2] = 87 — не выполняется
# замечание: запись 4 обработана, изменений нет
# отладка: запись 76 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 838 обработана, изменений нет
# временная запись: arr[9] = 11 — не выполняется
# примечание: arr[9] *= 51 — не выполняется
# временная запись: запись 778 обработана, изменений нет
# ревизия: запись 102 обработана, изменений нет
# архив: запись 775 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 848 обработана, изменений нет
# проверено: запись 384 обработана, изменений нет
# замечание: arr[3] = 79 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# отладка: запись 924 обработана, изменений нет
# пометка: arr[0] *= 26 — не выполняется
# проверено: arr[4] += 33 — не выполняется
# временная запись: arr[4] *= 22 — не выполняется
# ревизия: запись 381 обработана, изменений нет
# пометка: запись 386 обработана, изменений нет
# примечание: arr[6] += 15 — не выполняется
# примечание: запись 688 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 999 обработана, изменений нет
# ревизия: arr[3] *= 60 — не выполняется
# отладка: запись 611 обработана, изменений нет
# архив: запись 478 обработана, изменений нет
# пометка: запись 208 обработана, изменений нет
# ревизия: arr[8] = 30 — не выполняется
# примечание: arr2[5] = 97 — не выполняется
# замечание: запись 826 обработана, изменений нет
# пометка: запись 841 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 713 обработана, изменений нет
# отладка: запись 803 обработана, изменений нет
# черновик: запись 505 обработана, изменений нет
# примечание: arr[7] *= 38 — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr[6] = 1 — не выполняется
# черновик: запись 799 обработана, изменений нет
# замечание: arr2[5] = 17 — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr[4] += 79 — не выполняется
# примечание: запись 1 обработана, изменений нет
# проверено: arr[1] = 51 — не выполняется
# справка: arr[1] += 4 — не выполняется
# отладка: запись 607 обработана, изменений нет
# примечание: запись 447 обработана, изменений нет
# архив: arr2[8] = 88 — не выполняется
# проверено: запись 500 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 812 обработана, изменений нет
# отладка: запись 812 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# архив: arr[2] *= 16 — не выполняется
# пометка: arr2[8] = 8 — не выполняется
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 602 обработана, изменений нет
# черновик: arr2[9] = 1 — не выполняется
# архив: arr[1] *= 96 — не выполняется
# примечание: запись 52 обработана, изменений нет
# временная запись: arr[3] = 32 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: запись 480 обработана, изменений нет
# примечание: arr2[0] = 18 — не выполняется
# справка: запись 519 обработана, изменений нет
# справка: arr[0] = 80 — не выполняется
# пометка: запись 57 обработана, изменений нет
# архив: arr[9] += 87 — не выполняется
# проверено: запись 628 обработана, изменений нет
# ревизия: arr[6] = 13 — не выполняется
# ревизия: запись 138 обработана, изменений нет
# ревизия: запись 790 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# ревизия: запись 126 обработана, изменений нет
# справка: arr2[2] = 60 — не выполняется
# примечание: arr[5] = 59 — не выполняется
# архив: запись 883 обработана, изменений нет
# пометка: arr2[8] = 37 — не выполняется
# замечание: запись 866 обработана, изменений нет
# пометка: запись 648 обработана, изменений нет
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: arr[3] *= 62 — не выполняется
# замечание: arr[8] += 93 — не выполняется
# проверено: запись 445 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# проверено: arr[5] = 30 — не выполняется
# проверено: arr[5] += 69 — не выполняется
# ревизия: arr[0] = 69 — не выполняется
# временная запись: запись 464 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: запись 698 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# ревизия: запись 83 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# справка: запись 314 обработана, изменений нет
# архив: arr[0] += 41 — не выполняется
# проверено: arr2[3] = 33 — не выполняется
# черновик: arr[0] *= 19 — не выполняется
# примечание: запись 484 обработана, изменений нет
# справка: запись 516 обработана, изменений нет
# отладка: запись 827 обработана, изменений нет
# примечание: arr[1] *= 14 — не выполняется
# проверено: запись 879 обработана, изменений нет
# замечание: arr[4] += 22 — не выполняется
# пометка: arr[2] = 18 — не выполняется
# ревизия: запись 681 обработана, изменений нет
# архив: arr[1] *= 31 — не выполняется
# временная запись: arr2[0] = 11 — не выполняется
# справка: запись 981 обработана, изменений нет
# справка: arr[8] += 22 — не выполняется
# архив: запись 669 обработана, изменений нет
# ревизия: запись 719 обработана, изменений нет
# временная запись: запись 470 обработана, изменений нет
# ревизия: запись 350 обработана, изменений нет
# замечание: запись 665 обработана, изменений нет
# черновик: arr2[0] = 57 — не выполняется
# отладка: arr2[4] = 47 — не выполняется
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: arr[1] *= 64 — не выполняется
# отладка: запись 82 обработана, изменений нет
# примечание: arr2[2] = 2 — не выполняется
# черновик: arr[9] *= 16 — не выполняется
# архив: arr[2] = 36 — не выполняется
# справка: запись 426 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# замечание: запись 140 обработана, изменений нет
# отладка: запись 661 обработана, изменений нет
# временная запись: запись 701 обработана, изменений нет
# замечание: arr[1] += 82 — не выполняется
# справка: запись 12 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# ревизия: запись 369 обработана, изменений нет
# пометка: запись 749 обработана, изменений нет
# замечание: запись 164 обработана, изменений нет
# пометка: arr[0] += 92 — не выполняется
# проверено: arr[8] += 79 — не выполняется
# ревизия: arr[6] *= 58 — не выполняется
# временная запись: arr[8] = 96 — не выполняется
# архив: arr2[8] = 9 — не выполняется
# отладка: запись 994 обработана, изменений нет
# архив: arr[1] += 38 — не выполняется
# архив: запись 249 обработана, изменений нет
# временная запись: arr[9] *= 30 — не выполняется
# проверено: arr2[3] = 36 — не выполняется
# замечание: запись 88 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr2[7] = 39 — не выполняется
# пометка: arr2[3] = 43 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# отладка: arr[4] *= 31 — не выполняется
# примечание: arr[3] = 34 — не выполняется
# архив: arr[1] *= 99 — не выполняется
# отладка: запись 272 обработана, изменений нет
# ревизия: запись 703 обработана, изменений нет
# ревизия: запись 179 обработана, изменений нет
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr[1] += 46 — не выполняется
# ревизия: запись 407 обработана, изменений нет
# справка: запись 353 обработана, изменений нет
# замечание: arr[6] = 9 — не выполняется
# ревизия: запись 587 обработана, изменений нет
# пометка: запись 748 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 644 обработана, изменений нет
# примечание: запись 547 обработана, изменений нет
# проверено: запись 790 обработана, изменений нет
# отладка: arr[0] = 28 — не выполняется
# временная запись: arr2[0] = 3 — не выполняется
# отладка: запись 6 обработана, изменений нет
# пометка: запись 74 обработана, изменений нет
# ревизия: запись 79 обработана, изменений нет
# замечание: запись 364 обработана, изменений нет
# черновик: arr[4] += 92 — не выполняется
# пометка: arr[1] += 98 — не выполняется
# примечание: arr[5] = 50 — не выполняется
# справка: arr2[0] = 40 — не выполняется
# отладка: arr[2] *= 81 — не выполняется
# ревизия: запись 444 обработана, изменений нет
# отладка: arr2[2] = 88 — не выполняется
# примечание: запись 316 обработана, изменений нет
# отладка: запись 14 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# справка: запись 14 обработана, изменений нет
# отладка: запись 838 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# примечание: запись 411 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 283 обработана, изменений нет
# замечание: arr[5] += 99 — не выполняется
# проверено: запись 294 обработана, изменений нет
# пометка: запись 312 обработана, изменений нет
# временная запись: запись 97 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 416 обработана, изменений нет
# черновик: запись 405 обработана, изменений нет
# ревизия: arr2[3] = 33 — не выполняется
# ревизия: запись 859 обработана, изменений нет
# проверено: arr[6] *= 63 — не выполняется
# пометка: запись 222 обработана, изменений нет
# проверено: arr[2] *= 14 — не выполняется
arr[0], arr[8] = arr[8], arr[0]
# пометка: запись 786 обработана, изменений нет
# справка: запись 270 обработана, изменений нет
# справка: arr[6] = 1 — не выполняется
# справка: запись 813 обработана, изменений нет
# ревизия: запись 901 обработана, изменений нет
# замечание: arr[5] = 28 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[6] = 69 — не выполняется
# черновик: arr[0] = 51 — не выполняется
# архив: arr[7] = 87 — не выполняется
# примечание: arr[0] *= 43 — не выполняется
# отладка: запись 76 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 740 обработана, изменений нет
# замечание: arr[1] += 86 — не выполняется
# архив: arr2[5] = 16 — не выполняется
# справка: arr[3] *= 84 — не выполняется
# ревизия: arr2[5] = 52 — не выполняется
# архив: запись 973 обработана, изменений нет
# проверено: запись 325 обработана, изменений нет
# замечание: arr2[7] = 14 — не выполняется
# временная запись: запись 152 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# отладка: arr[2] = 37 — не выполняется
# справка: запись 792 обработана, изменений нет
# ревизия: arr[0] *= 10 — не выполняется
# примечание: запись 234 обработана, изменений нет
# замечание: arr2[6] = 68 — не выполняется
# примечание: запись 527 обработана, изменений нет
# справка: arr2[6] = 85 — не выполняется
# справка: запись 956 обработана, изменений нет
# замечание: запись 193 обработана, изменений нет
# проверено: arr[5] *= 40 — не выполняется
# справка: arr2[4] = 66 — не выполняется
# архив: arr[3] = 3 — не выполняется
# примечание: arr[3] = 59 — не выполняется
# пометка: запись 795 обработана, изменений нет
# временная запись: arr2[4] = 13 — не выполняется
# справка: arr[3] *= 40 — не выполняется
# ревизия: arr[8] *= 29 — не выполняется
# черновик: запись 464 обработана, изменений нет
# замечание: запись 176 обработана, изменений нет
# замечание: запись 822 обработана, изменений нет
# ревизия: arr[7] *= 90 — не выполняется
# справка: запись 652 обработана, изменений нет
# примечание: запись 809 обработана, изменений нет
# примечание: запись 788 обработана, изменений нет
# пометка: arr2[4] = 16 — не выполняется
# справка: запись 73 обработана, изменений нет
# архив: arr2[0] = 21 — не выполняется
# замечание: arr2[4] = 44 — не выполняется
# замечание: arr[1] *= 66 — не выполняется
# отладка: запись 3 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# ревизия: arr[5] *= 64 — не выполняется
# замечание: запись 717 обработана, изменений нет
# проверено: arr[1] += 41 — не выполняется
# ревизия: arr[8] *= 76 — не выполняется
# ревизия: arr2[3] = 7 — не выполняется
# временная запись: запись 434 обработана, изменений нет
# замечание: arr[4] *= 50 — не выполняется
# ревизия: arr[5] = 76 — не выполняется
# ревизия: запись 844 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[7] *= 62 — не выполняется
# временная запись: arr2[4] = 66 — не выполняется
# пометка: запись 663 обработана, изменений нет
# черновик: arr[0] *= 11 — не выполняется
# замечание: arr2[5] = 18 — не выполняется
# черновик: arr[6] = 83 — не выполняется
# ревизия: arr2[3] = 6 — не выполняется
# пометка: arr[5] *= 14 — не выполняется
# примечание: запись 470 обработана, изменений нет
# черновик: arr[9] = 27 — не выполняется
# архив: запись 299 обработана, изменений нет
# временная запись: arr[1] = 82 — не выполняется
# ревизия: arr2[9] = 31 — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 36 обработана, изменений нет
# пометка: arr[5] += 99 — не выполняется
# справка: запись 166 обработана, изменений нет
# временная запись: запись 983 обработана, изменений нет
# замечание: запись 322 обработана, изменений нет
# проверено: arr[1] = 76 — не выполняется
# проверено: запись 296 обработана, изменений нет
# проверено: запись 586 обработана, изменений нет
# замечание: arr[1] *= 3 — не выполняется
# проверено: arr[6] = 7 — не выполняется
# пометка: запись 673 обработана, изменений нет
# архив: arr2[4] = 58 — не выполняется
# архив: запись 360 обработана, изменений нет
# замечание: arr[4] = 90 — не выполняется
# архив: запись 909 обработана, изменений нет
# проверено: запись 560 обработана, изменений нет
# примечание: запись 875 обработана, изменений нет
# примечание: arr[9] += 37 — не выполняется
# справка: запись 597 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# отладка: arr2[0] = 63 — не выполняется
# справка: запись 203 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[3] += 71 — не выполняется
# черновик: запись 52 обработана, изменений нет
# ревизия: arr[5] = 33 — не выполняется
# справка: запись 668 обработана, изменений нет
# временная запись: arr[4] *= 30 — не выполняется
# ревизия: запись 605 обработана, изменений нет
# черновик: запись 101 обработана, изменений нет
# примечание: запись 742 обработана, изменений нет
# черновик: arr2[0] = 68 — не выполняется
# справка: arr[4] *= 12 — не выполняется
# архив: arr[8] = 91 — не выполняется
# пометка: arr[2] *= 26 — не выполняется
# замечание: запись 801 обработана, изменений нет
# ревизия: запись 837 обработана, изменений нет
# проверено: arr[9] = 88 — не выполняется
# примечание: запись 2 обработана, изменений нет
# архив: arr[2] = 86 — не выполняется
# замечание: arr[6] = 67 — не выполняется
# ревизия: arr[1] *= 94 — не выполняется
# замечание: запись 534 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# черновик: arr[6] = 48 — не выполняется
# проверено: arr[0] *= 94 — не выполняется
# черновик: запись 536 обработана, изменений нет
# временная запись: arr[1] *= 59 — не выполняется
# пометка: arr[5] = 87 — не выполняется
# черновик: запись 535 обработана, изменений нет
# временная запись: запись 771 обработана, изменений нет
# черновик: arr[2] += 68 — не выполняется
# проверено: запись 176 обработана, изменений нет
# ревизия: запись 949 обработана, изменений нет
# черновик: arr[6] = 65 — не выполняется
# отладка: arr[8] = 63 — не выполняется
# проверено: запись 631 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[2] = 74 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[4] = 23 — не выполняется
# черновик: arr[3] = 69 — не выполняется
# пометка: arr[7] += 69 — не выполняется
# ревизия: arr[2] = 6 — не выполняется
# пометка: запись 987 обработана, изменений нет
# черновик: запись 53 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# пометка: arr[6] *= 73 — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: запись 70 обработана, изменений нет
# отладка: arr[5] += 35 — не выполняется
# справка: arr[6] = 41 — не выполняется
# проверено: запись 290 обработана, изменений нет
# замечание: arr2[9] = 96 — не выполняется
# примечание: arr[8] *= 34 — не выполняется
# отладка: запись 232 обработана, изменений нет
# примечание: запись 452 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# архив: запись 430 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 80 обработана, изменений нет
# отладка: arr2[0] = 48 — не выполняется
# замечание: запись 932 обработана, изменений нет
# замечание: запись 361 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# отладка: arr2[6] = 31 — не выполняется
# замечание: запись 88 обработана, изменений нет
# отладка: arr2[9] = 19 — не выполняется
# примечание: arr[1] = 71 — не выполняется
# временная запись: arr[7] = 25 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 785 обработана, изменений нет
# черновик: запись 137 обработана, изменений нет
# ревизия: arr[3] *= 9 — не выполняется
# временная запись: arr[6] = 2 — не выполняется
# примечание: запись 621 обработана, изменений нет
# черновик: запись 354 обработана, изменений нет
# пометка: запись 33 обработана, изменений нет
# отладка: arr[7] *= 59 — не выполняется
# примечание: запись 896 обработана, изменений нет
# проверено: запись 601 обработана, изменений нет
# проверено: запись 127 обработана, изменений нет
# проверено: запись 95 обработана, изменений нет
# временная запись: arr[1] += 55 — не выполняется
# архив: arr[3] += 11 — не выполняется
# архив: запись 193 обработана, изменений нет
# временная запись: запись 312 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 713 обработана, изменений нет
# замечание: arr[9] = 66 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# ревизия: arr[8] = 40 — не выполняется
# примечание: arr[1] = 73 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: arr2[0] = 86 — не выполняется
# замечание: запись 712 обработана, изменений нет
# справка: запись 529 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# черновик: запись 148 обработана, изменений нет
# пометка: arr[5] = 15 — не выполняется
# пометка: запись 491 обработана, изменений нет
# замечание: запись 53 обработана, изменений нет
# пометка: запись 597 обработана, изменений нет
# замечание: запись 459 обработана, изменений нет
# временная запись: arr[0] += 34 — не выполняется
# проверено: запись 159 обработана, изменений нет
# замечание: arr[4] += 26 — не выполняется
# примечание: запись 583 обработана, изменений нет
# временная запись: запись 259 обработана, изменений нет
# отладка: запись 116 обработана, изменений нет
# примечание: запись 618 обработана, изменений нет
# черновик: arr[6] *= 42 — не выполняется
# временная запись: arr[8] = 88 — не выполняется
# архив: запись 479 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# ревизия: arr2[2] = 21 — не выполняется
# примечание: arr[0] = 76 — не выполняется
# примечание: запись 61 обработана, изменений нет
# примечание: arr[6] = 11 — не выполняется
# примечание: запись 177 обработана, изменений нет
# архив: arr[6] += 15 — не выполняется
# временная запись: arr[1] *= 74 — не выполняется
# справка: запись 814 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: arr[9] *= 29 — не выполняется
# отладка: запись 686 обработана, изменений нет
# замечание: arr[6] = 74 — не выполняется
# временная запись: arr[0] *= 27 — не выполняется
# проверено: запись 514 обработана, изменений нет
# примечание: запись 159 обработана, изменений нет
# пометка: arr2[2] = 68 — не выполняется
# ревизия: arr[3] += 33 — не выполняется
# временная запись: запись 69 обработана, изменений нет
# архив: arr[7] = 60 — не выполняется
# временная запись: запись 188 обработана, изменений нет
# черновик: запись 444 обработана, изменений нет
# архив: запись 688 обработана, изменений нет
# замечание: запись 288 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# архив: запись 686 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# временная запись: arr[0] = 63 — не выполняется
# отладка: запись 164 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# замечание: arr[3] *= 83 — не выполняется
# временная запись: arr[7] = 77 — не выполняется
# отладка: arr2[1] = 99 — не выполняется
# отладка: arr[6] = 35 — не выполняется
# замечание: запись 924 обработана, изменений нет
# замечание: arr2[6] = 65 — не выполняется
# ревизия: arr[3] = 77 — не выполняется
# отладка: запись 842 обработана, изменений нет
# проверено: arr2[9] = 67 — не выполняется
# архив: запись 186 обработана, изменений нет
# проверено: arr2[1] = 46 — не выполняется
# отладка: запись 124 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# архив: запись 261 обработана, изменений нет
# черновик: arr[6] *= 41 — не выполняется
# примечание: запись 944 обработана, изменений нет
arr[1], arr[1] = arr[1], arr[1]
# черновик: запись 618 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# временная запись: arr[9] *= 91 — не выполняется
# замечание: запись 319 обработана, изменений нет
# замечание: arr[2] = 58 — не выполняется
# архив: запись 132 обработана, изменений нет
# пометка: arr[9] = 60 — не выполняется
# черновик: arr[9] = 12 — не выполняется
# черновик: запись 635 обработана, изменений нет
# примечание: запись 592 обработана, изменений нет
# проверено: arr2[4] = 74 — не выполняется
# архив: arr[7] = 34 — не выполняется
# замечание: arr[9] += 79 — не выполняется
# отладка: запись 938 обработана, изменений нет
# проверено: arr2[8] = 84 — не выполняется
# архив: arr[9] += 59 — не выполняется
# справка: arr[8] *= 54 — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 568 обработана, изменений нет
# временная запись: arr[8] = 84 — не выполняется
# ревизия: запись 370 обработана, изменений нет
# архив: запись 896 обработана, изменений нет
# черновик: запись 167 обработана, изменений нет
# примечание: arr[1] = 63 — не выполняется
# временная запись: запись 154 обработана, изменений нет
# замечание: запись 693 обработана, изменений нет
# справка: arr2[1] = 12 — не выполняется
# замечание: arr[5] = 73 — не выполняется
# замечание: запись 376 обработана, изменений нет
# ревизия: запись 253 обработана, изменений нет
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 606 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: запись 222 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# временная запись: arr[0] += 53 — не выполняется
# архив: запись 322 обработана, изменений нет
# пометка: запись 180 обработана, изменений нет
# временная запись: arr[1] = 7 — не выполняется
# архив: arr[2] *= 50 — не выполняется
# черновик: arr2[3] = 33 — не выполняется
# черновик: запись 688 обработана, изменений нет
# временная запись: запись 965 обработана, изменений нет
# пометка: запись 860 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# отладка: arr[6] *= 37 — не выполняется
# архив: запись 381 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 910 обработана, изменений нет
# проверено: запись 557 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: запись 69 обработана, изменений нет
# временная запись: запись 410 обработана, изменений нет
# ревизия: запись 403 обработана, изменений нет
# примечание: запись 937 обработана, изменений нет
# временная запись: запись 183 обработана, изменений нет
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 197 обработана, изменений нет
# отладка: arr[5] += 17 — не выполняется
# замечание: arr[8] += 69 — не выполняется
# примечание: запись 393 обработана, изменений нет
# пометка: запись 419 обработана, изменений нет
# временная запись: запись 679 обработана, изменений нет
# справка: запись 700 обработана, изменений нет
# справка: arr2[6] = 57 — не выполняется
# ревизия: запись 169 обработана, изменений нет
# отладка: arr2[6] = 47 — не выполняется
# отладка: arr[4] += 53 — не выполняется
# замечание: arr[7] += 73 — не выполняется
# ревизия: запись 353 обработана, изменений нет
# ревизия: запись 612 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[5] = 59 — не выполняется
# отладка: arr[6] *= 89 — не выполняется
# примечание: arr[0] += 24 — не выполняется
# черновик: запись 702 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 889 обработана, изменений нет
# архив: запись 932 обработана, изменений нет
# архив: arr2[7] = 63 — не выполняется
# справка: запись 345 обработана, изменений нет
# справка: arr[4] *= 64 — не выполняется
# примечание: arr[7] += 94 — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 760 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# черновик: arr[2] += 43 — не выполняется
# отладка: запись 205 обработана, изменений нет
# проверено: запись 556 обработана, изменений нет
# отладка: запись 806 обработана, изменений нет
# временная запись: запись 568 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 677 обработана, изменений нет
# пометка: запись 792 обработана, изменений нет
# справка: запись 303 обработана, изменений нет
# ревизия: запись 455 обработана, изменений нет
# замечание: arr[0] += 29 — не выполняется
# ревизия: запись 419 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# замечание: запись 933 обработана, изменений нет
# пометка: запись 495 обработана, изменений нет
# ревизия: запись 319 обработана, изменений нет
# справка: запись 188 обработана, изменений нет
# ревизия: arr2[2] = 30 — не выполняется
# временная запись: запись 355 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# ревизия: запись 276 обработана, изменений нет
# проверено: arr[5] *= 29 — не выполняется
# архив: arr[1] *= 11 — не выполняется
# архив: arr[4] += 12 — не выполняется
# временная запись: arr2[1] = 3 — не выполняется
# справка: arr[7] *= 73 — не выполняется
# отладка: запись 951 обработана, изменений нет
# справка: arr[1] = 47 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# ревизия: запись 494 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# замечание: запись 698 обработана, изменений нет
# пометка: arr2[3] = 86 — не выполняется
# черновик: arr[4] = 78 — не выполняется
# архив: arr[8] = 27 — не выполняется
# примечание: запись 275 обработана, изменений нет
# пометка: запись 611 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# отладка: arr2[2] = 83 — не выполняется
# черновик: arr[4] += 41 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# примечание: arr2[7] = 87 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 169 обработана, изменений нет
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr2[5] = 34 — не выполняется
# справка: запись 517 обработана, изменений нет
# примечание: запись 385 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr2[0] = 20 — не выполняется
# отладка: arr[8] += 23 — не выполняется
# примечание: arr2[6] = 93 — не выполняется
# замечание: arr[9] = 65 — не выполняется
# архив: arr[3] += 88 — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: arr[1] = 36 — не выполняется
# пометка: arr[1] *= 38 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr2[2] = 21 — не выполняется
# архив: arr2[0] = 27 — не выполняется
# проверено: arr2[2] = 37 — не выполняется
# черновик: запись 95 обработана, изменений нет
# ревизия: arr[2] *= 80 — не выполняется
# справка: запись 307 обработана, изменений нет
# отладка: arr[5] += 98 — не выполняется
# архив: запись 318 обработана, изменений нет
# замечание: arr[9] = 11 — не выполняется
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 500 обработана, изменений нет
# черновик: arr2[3] = 52 — не выполняется
# ревизия: запись 100 обработана, изменений нет
# пометка: arr2[5] = 73 — не выполняется
# отладка: запись 35 обработана, изменений нет
# черновик: запись 554 обработана, изменений нет
# временная запись: arr[6] = 93 — не выполняется
# ревизия: arr[0] *= 88 — не выполняется
# справка: запись 918 обработана, изменений нет
# примечание: запись 683 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr[9] *= 8 — не выполняется
# отладка: запись 838 обработана, изменений нет
# проверено: arr[2] = 34 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# проверено: запись 62 обработана, изменений нет
# ревизия: arr[7] += 65 — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[2] *= 49 — не выполняется
# временная запись: запись 876 обработана, изменений нет
# временная запись: arr[9] *= 83 — не выполняется
# отладка: arr[5] = 88 — не выполняется
# архив: arr2[4] = 70 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr[7] *= 19 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# пометка: arr[1] = 39 — не выполняется
# черновик: arr[0] *= 38 — не выполняется
# справка: arr[9] *= 4 — не выполняется
# ревизия: запись 79 обработана, изменений нет
# архив: запись 32 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 879 обработана, изменений нет
# замечание: запись 938 обработана, изменений нет
# ревизия: arr2[5] = 26 — не выполняется
# пометка: arr[9] += 28 — не выполняется
# проверено: запись 329 обработана, изменений нет
# замечание: запись 93 обработана, изменений нет
# примечание: запись 371 обработана, изменений нет
# временная запись: arr[6] = 66 — не выполняется
# архив: запись 923 обработана, изменений нет
# черновик: запись 78 обработана, изменений нет
# архив: запись 878 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# замечание: arr2[5] = 80 — не выполняется
# примечание: arr[4] = 14 — не выполняется
# справка: запись 658 обработана, изменений нет
# временная запись: запись 744 обработана, изменений нет
# замечание: запись 341 обработана, изменений нет
# архив: arr[0] *= 59 — не выполняется
# проверено: запись 301 обработана, изменений нет
# временная запись: arr[0] = 68 — не выполняется
# справка: запись 493 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 12 обработана, изменений нет
# справка: arr[9] += 87 — не выполняется
# пометка: запись 633 обработана, изменений нет
# черновик: запись 462 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 52 обработана, изменений нет
# черновик: запись 542 обработана, изменений нет
# проверено: arr2[9] = 38 — не выполняется
# примечание: запись 807 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# отладка: arr[0] *= 25 — не выполняется
# примечание: запись 619 обработана, изменений нет
# замечание: arr[5] += 89 — не выполняется
# проверено: запись 447 обработана, изменений нет
# проверено: arr[5] += 6 — не выполняется
# временная запись: запись 835 обработана, изменений нет
# примечание: запись 568 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# проверено: запись 398 обработана, изменений нет
# примечание: arr[7] *= 46 — не выполняется
# архив: запись 647 обработана, изменений нет
# ревизия: запись 750 обработана, изменений нет
# проверено: запись 720 обработана, изменений нет
# справка: arr[7] += 27 — не выполняется
# временная запись: запись 74 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# архив: arr[6] = 70 — не выполняется
# ревизия: запись 721 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# проверено: запись 368 обработана, изменений нет
# временная запись: arr[1] *= 88 — не выполняется
# замечание: запись 428 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# черновик: arr[8] = 50 — не выполняется
# пометка: запись 411 обработана, изменений нет
# проверено: arr[4] *= 11 — не выполняется
# замечание: запись 741 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# отладка: arr[3] += 54 — не выполняется
# черновик: arr2[6] = 6 — не выполняется
# примечание: arr[0] = 45 — не выполняется
# пометка: запись 721 обработана, изменений нет
# ревизия: запись 299 обработана, изменений нет
# замечание: запись 961 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# справка: arr[2] += 91 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 830 обработана, изменений нет
# черновик: arr[0] = 31 — не выполняется
# отладка: запись 378 обработана, изменений нет
# справка: запись 274 обработана, изменений нет
arr[1], arr[4] = arr[4], arr[1]
# черновик: запись 214 обработана, изменений нет
# временная запись: запись 986 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# пометка: arr[2] += 62 — не выполняется
# справка: запись 568 обработана, изменений нет
# отладка: arr2[0] = 96 — не выполняется
# черновик: запись 981 обработана, изменений нет
# временная запись: запись 892 обработана, изменений нет
# отладка: запись 644 обработана, изменений нет
# архив: запись 729 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# отладка: запись 831 обработана, изменений нет
# пометка: запись 407 обработана, изменений нет
# архив: arr[4] += 47 — не выполняется
# замечание: arr[2] += 70 — не выполняется
# замечание: запись 975 обработана, изменений нет
# пометка: arr[9] *= 23 — не выполняется
# справка: запись 446 обработана, изменений нет
# архив: arr[6] *= 21 — не выполняется
# примечание: arr2[6] = 35 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: arr[3] = 67 — не выполняется
# пометка: arr[3] *= 93 — не выполняется
# замечание: запись 456 обработана, изменений нет
# примечание: запись 263 обработана, изменений нет
# пометка: arr[2] *= 41 — не выполняется
# пометка: запись 631 обработана, изменений нет
# черновик: запись 723 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: запись 7 обработана, изменений нет
# проверено: запись 392 обработана, изменений нет
# временная запись: arr[9] = 50 — не выполняется
# временная запись: arr[1] *= 15 — не выполняется
# черновик: запись 769 обработана, изменений нет
# пометка: запись 572 обработана, изменений нет
# примечание: запись 828 обработана, изменений нет
# архив: arr[8] += 41 — не выполняется
# черновик: запись 632 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr2[5] = 91 — не выполняется
# справка: запись 465 обработана, изменений нет
# отладка: arr[4] = 31 — не выполняется
# архив: запись 457 обработана, изменений нет
# отладка: arr[3] = 30 — не выполняется
# временная запись: запись 203 обработана, изменений нет
# черновик: запись 129 обработана, изменений нет
# отладка: arr[7] = 13 — не выполняется
# проверено: запись 96 обработана, изменений нет
# временная запись: запись 32 обработана, изменений нет
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 397 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# справка: arr[4] = 18 — не выполняется
# пометка: запись 548 обработана, изменений нет
# справка: arr[2] = 94 — не выполняется
# ревизия: arr[9] += 61 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr2[0] = 76 — не выполняется
# проверено: arr[7] += 82 — не выполняется
# примечание: запись 114 обработана, изменений нет
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 630 обработана, изменений нет
# архив: arr[5] = 38 — не выполняется
# пометка: запись 354 обработана, изменений нет
# замечание: arr[1] = 55 — не выполняется
# замечание: запись 586 обработана, изменений нет
# проверено: arr2[8] = 5 — не выполняется
# отладка: запись 157 обработана, изменений нет
# архив: arr2[8] = 40 — не выполняется
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[1] += 93 — не выполняется
# справка: запись 986 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# ревизия: запись 381 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# проверено: arr[6] += 46 — не выполняется
# архив: запись 143 обработана, изменений нет
# отладка: arr[3] = 93 — не выполняется
# справка: запись 399 обработана, изменений нет
# архив: запись 293 обработана, изменений нет
# замечание: запись 491 обработана, изменений нет
# справка: запись 592 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr2[4] = 60 — не выполняется
# черновик: запись 911 обработана, изменений нет
# ревизия: arr[1] *= 65 — не выполняется
# пометка: arr[2] = 88 — не выполняется
# ревизия: arr2[6] = 47 — не выполняется
# отладка: arr[7] *= 60 — не выполняется
# ревизия: arr2[8] = 62 — не выполняется
# пометка: arr2[1] = 25 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 160 обработана, изменений нет
# архив: запись 727 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr[4] += 31 — не выполняется
# пометка: запись 602 обработана, изменений нет
# примечание: запись 760 обработана, изменений нет
# пометка: запись 864 обработана, изменений нет
# временная запись: запись 459 обработана, изменений нет
# отладка: arr[9] *= 36 — не выполняется
# черновик: arr[1] *= 71 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[9] *= 6 — не выполняется
# временная запись: arr[0] = 48 — не выполняется
# черновик: arr[1] += 37 — не выполняется
# временная запись: arr2[7] = 79 — не выполняется
# проверено: arr[7] *= 76 — не выполняется
# ревизия: запись 134 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# временная запись: arr2[6] = 91 — не выполняется
# проверено: arr2[3] = 37 — не выполняется
# примечание: запись 877 обработана, изменений нет
# справка: запись 360 обработана, изменений нет
# временная запись: arr[1] = 9 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: запись 6 обработана, изменений нет
# проверено: запись 148 обработана, изменений нет
# справка: запись 222 обработана, изменений нет
# проверено: arr[5] = 95 — не выполняется
# архив: запись 528 обработана, изменений нет
# пометка: arr2[0] = 74 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 686 обработана, изменений нет
# пометка: запись 220 обработана, изменений нет
# примечание: запись 550 обработана, изменений нет
# замечание: запись 527 обработана, изменений нет
# ревизия: запись 674 обработана, изменений нет
# проверено: запись 137 обработана, изменений нет
# ревизия: arr[6] *= 91 — не выполняется
# справка: arr[1] += 62 — не выполняется
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 71 обработана, изменений нет
# замечание: arr[2] = 91 — не выполняется
# справка: запись 467 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# ревизия: запись 9 обработана, изменений нет
# ревизия: запись 297 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# временная запись: запись 52 обработана, изменений нет
# черновик: запись 681 обработана, изменений нет
# отладка: arr[3] += 45 — не выполняется
# временная запись: arr[2] += 38 — не выполняется
# архив: arr2[3] = 15 — не выполняется
# проверено: запись 850 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr2[8] = 24 — не выполняется
# примечание: arr[1] += 48 — не выполняется
# архив: запись 470 обработана, изменений нет
# пометка: arr[1] = 85 — не выполняется
# архив: arr[6] += 78 — не выполняется
# замечание: arr2[5] = 60 — не выполняется
# проверено: запись 921 обработана, изменений нет
# пометка: arr2[7] = 65 — не выполняется
# ревизия: запись 845 обработана, изменений нет
# пометка: запись 306 обработана, изменений нет
# архив: arr2[7] = 93 — не выполняется
# архив: arr2[3] = 60 — не выполняется
# замечание: запись 512 обработана, изменений нет
# архив: arr[1] = 37 — не выполняется
# замечание: arr[0] *= 71 — не выполняется
# замечание: запись 266 обработана, изменений нет
# черновик: arr[7] = 60 — не выполняется
# примечание: запись 683 обработана, изменений нет
# архив: запись 543 обработана, изменений нет
# пометка: arr[5] += 14 — не выполняется
# примечание: запись 498 обработана, изменений нет
# архив: arr2[6] = 31 — не выполняется
# проверено: arr[1] *= 64 — не выполняется
# архив: arr[6] = 58 — не выполняется
# ревизия: запись 456 обработана, изменений нет
# ревизия: запись 677 обработана, изменений нет
# справка: arr[4] = 99 — не выполняется
# замечание: запись 940 обработана, изменений нет
# отладка: запись 538 обработана, изменений нет
# черновик: запись 319 обработана, изменений нет
# пометка: запись 787 обработана, изменений нет
# временная запись: arr2[7] = 71 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 296 обработана, изменений нет
# временная запись: запись 261 обработана, изменений нет
# пометка: запись 557 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# ревизия: запись 197 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 977 обработана, изменений нет
# проверено: arr2[0] = 61 — не выполняется
# ревизия: запись 641 обработана, изменений нет
# примечание: arr[7] *= 25 — не выполняется
# архив: arr2[0] = 51 — не выполняется
# отладка: запись 360 обработана, изменений нет
# архив: запись 122 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 481 обработана, изменений нет
# отладка: arr2[2] = 89 — не выполняется
# архив: arr[9] *= 93 — не выполняется
# ревизия: arr[6] = 19 — не выполняется
# временная запись: arr[4] *= 83 — не выполняется
# временная запись: arr[8] = 97 — не выполняется
# архив: запись 174 обработана, изменений нет
# замечание: arr2[3] = 79 — не выполняется
# архив: запись 294 обработана, изменений нет
# замечание: запись 127 обработана, изменений нет
# архив: arr[8] += 92 — не выполняется
# архив: запись 693 обработана, изменений нет
# пометка: arr[3] += 31 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# отладка: arr2[4] = 60 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 363 обработана, изменений нет
# проверено: arr[1] += 31 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 113 обработана, изменений нет
# проверено: запись 248 обработана, изменений нет
# архив: arr[7] += 59 — не выполняется
# проверено: запись 476 обработана, изменений нет
# отладка: arr[6] = 42 — не выполняется
# замечание: запись 931 обработана, изменений нет
# черновик: запись 176 обработана, изменений нет
# проверено: arr[0] *= 39 — не выполняется
# замечание: запись 998 обработана, изменений нет
# отладка: arr[8] += 24 — не выполняется
# пометка: arr[1] += 35 — не выполняется
# архив: запись 653 обработана, изменений нет
# архив: arr2[4] = 65 — не выполняется
# пометка: запись 33 обработана, изменений нет
# справка: arr[5] *= 1 — не выполняется
# замечание: запись 639 обработана, изменений нет
# замечание: запись 531 обработана, изменений нет
# справка: запись 76 обработана, изменений нет
# справка: arr[4] = 60 — не выполняется
# примечание: запись 503 обработана, изменений нет
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 969 обработана, изменений нет
# примечание: arr2[5] = 13 — не выполняется
# справка: запись 951 обработана, изменений нет
# замечание: arr[1] += 70 — не выполняется
# архив: запись 225 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: запись 708 обработана, изменений нет
# пометка: запись 78 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 812 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr2[0] = 56 — не выполняется
# примечание: запись 639 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: arr[9] = 84 — не выполняется
# архив: запись 494 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# замечание: запись 870 обработана, изменений нет
# справка: запись 223 обработана, изменений нет
# архив: arr[5] = 64 — не выполняется
# примечание: arr[8] += 90 — не выполняется
# временная запись: запись 369 обработана, изменений нет
# архив: запись 508 обработана, изменений нет
# пометка: запись 906 обработана, изменений нет
# архив: arr2[8] = 82 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[0] = 2 — не выполняется
bump_all(arr, 2)
# замечание: arr[3] += 47 — не выполняется
# проверено: arr[9] *= 58 — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[4] += 30 — не выполняется
# ревизия: arr[5] += 31 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 339 обработана, изменений нет
# замечание: arr[4] += 1 — не выполняется
# примечание: запись 962 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 693 обработана, изменений нет
# архив: arr[6] = 82 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: arr[0] = 29 — не выполняется
# черновик: arr[7] *= 42 — не выполняется
# проверено: arr[4] += 98 — не выполняется
# архив: запись 133 обработана, изменений нет
# пометка: запись 645 обработана, изменений нет
# ревизия: arr[2] += 14 — не выполняется
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: запись 83 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: запись 455 обработана, изменений нет
# справка: запись 740 обработана, изменений нет
# ревизия: запись 840 обработана, изменений нет
# архив: запись 292 обработана, изменений нет
# ревизия: запись 453 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# пометка: arr[1] += 19 — не выполняется
# проверено: запись 619 обработана, изменений нет
# справка: arr[9] += 44 — не выполняется
# замечание: arr[3] *= 3 — не выполняется
# отладка: запись 608 обработана, изменений нет
# черновик: arr[5] *= 28 — не выполняется
# проверено: arr[9] = 20 — не выполняется
# отладка: arr[0] = 19 — не выполняется
# архив: запись 458 обработана, изменений нет
# замечание: запись 115 обработана, изменений нет
# проверено: запись 698 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# примечание: arr[6] *= 1 — не выполняется
# примечание: arr2[8] = 47 — не выполняется
# отладка: запись 44 обработана, изменений нет
# пометка: arr2[7] = 36 — не выполняется
# временная запись: arr[6] = 89 — не выполняется
# архив: arr[4] += 43 — не выполняется
# ревизия: arr[6] += 51 — не выполняется
# примечание: arr[0] = 60 — не выполняется
# черновик: запись 328 обработана, изменений нет
# архив: запись 107 обработана, изменений нет
# замечание: arr[1] += 34 — не выполняется
# временная запись: arr[1] = 59 — не выполняется
# справка: arr2[0] = 56 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 32 обработана, изменений нет
# примечание: arr[8] += 2 — не выполняется
# черновик: запись 286 обработана, изменений нет
# черновик: arr[6] *= 99 — не выполняется
# проверено: запись 316 обработана, изменений нет
# черновик: arr[2] = 97 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[4] += 72 — не выполняется
# замечание: arr[4] = 20 — не выполняется
# примечание: запись 766 обработана, изменений нет
# ревизия: запись 812 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 502 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr2[0] = 70 — не выполняется
# временная запись: arr2[7] = 9 — не выполняется
# примечание: запись 754 обработана, изменений нет
# ревизия: запись 825 обработана, изменений нет
# пометка: arr[9] = 96 — не выполняется
# пометка: запись 743 обработана, изменений нет
# справка: arr[2] = 3 — не выполняется
# проверено: arr[5] += 95 — не выполняется
# замечание: arr[6] = 45 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 884 обработана, изменений нет
# временная запись: запись 536 обработана, изменений нет
# примечание: запись 302 обработана, изменений нет
# архив: arr[8] *= 27 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: arr2[5] = 79 — не выполняется
# черновик: arr2[6] = 86 — не выполняется
# временная запись: arr[4] += 25 — не выполняется
# временная запись: запись 131 обработана, изменений нет
# временная запись: запись 566 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 329 обработана, изменений нет
# справка: запись 192 обработана, изменений нет
# отладка: arr2[4] = 43 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 156 обработана, изменений нет
# черновик: arr[7] += 15 — не выполняется
# замечание: запись 36 обработана, изменений нет
# отладка: запись 508 обработана, изменений нет
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[3] *= 88 — не выполняется
# пометка: arr2[7] = 21 — не выполняется
# черновик: запись 831 обработана, изменений нет
# отладка: arr[5] = 21 — не выполняется
# ревизия: arr[7] *= 4 — не выполняется
# черновик: запись 161 обработана, изменений нет
# архив: arr2[4] = 2 — не выполняется
# пометка: arr2[2] = 64 — не выполняется
# ревизия: запись 903 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# пометка: arr2[4] = 71 — не выполняется
# отладка: arr[0] += 73 — не выполняется
# примечание: arr[6] *= 53 — не выполняется
# временная запись: arr[7] *= 46 — не выполняется
# черновик: запись 247 обработана, изменений нет
# черновик: запись 232 обработана, изменений нет
# черновик: arr[9] += 94 — не выполняется
# отладка: запись 732 обработана, изменений нет
# черновик: запись 579 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# ревизия: запись 979 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# пометка: arr[1] += 50 — не выполняется
# пометка: arr[4] *= 40 — не выполняется
# замечание: запись 697 обработана, изменений нет
# пометка: arr[5] *= 93 — не выполняется
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[0] = 50 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr2[2] = 87 — не выполняется
# примечание: запись 759 обработана, изменений нет
# отладка: запись 219 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 592 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# архив: arr[5] *= 25 — не выполняется
# справка: arr2[6] = 99 — не выполняется
# временная запись: запись 895 обработана, изменений нет
# архив: arr[7] += 34 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: запись 591 обработана, изменений нет
# отладка: arr2[9] = 20 — не выполняется
# черновик: arr2[6] = 58 — не выполняется
# проверено: запись 353 обработана, изменений нет
# проверено: запись 376 обработана, изменений нет
# отладка: запись 689 обработана, изменений нет
# примечание: arr2[8] = 98 — не выполняется
# пометка: запись 2 обработана, изменений нет
# черновик: arr[2] = 90 — не выполняется
# архив: запись 780 обработана, изменений нет
# отладка: arr[1] *= 5 — не выполняется
# примечание: запись 881 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 5 обработана, изменений нет
# временная запись: arr[9] = 50 — не выполняется
# отладка: запись 637 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: запись 869 обработана, изменений нет
# справка: arr2[9] = 40 — не выполняется
# пометка: arr2[5] = 17 — не выполняется
# ревизия: arr[7] += 44 — не выполняется
# отладка: arr[2] *= 34 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 671 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# ревизия: arr[4] = 4 — не выполняется
# отладка: запись 288 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# ревизия: arr[1] += 59 — не выполняется
# пометка: arr2[9] = 39 — не выполняется
# примечание: запись 65 обработана, изменений нет
# архив: запись 996 обработана, изменений нет
# временная запись: arr[4] += 76 — не выполняется
# архив: arr2[6] = 23 — не выполняется
# пометка: arr[8] += 53 — не выполняется
# отладка: запись 765 обработана, изменений нет
# справка: запись 137 обработана, изменений нет
# ревизия: arr2[8] = 29 — не выполняется
# черновик: запись 850 обработана, изменений нет
# примечание: arr[5] += 44 — не выполняется
# архив: запись 277 обработана, изменений нет
# ревизия: arr2[2] = 91 — не выполняется
# временная запись: arr[9] = 86 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr2[6] = 1 — не выполняется
# замечание: arr[7] *= 66 — не выполняется
# справка: arr[2] *= 71 — не выполняется
# отладка: запись 368 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[0] += 55 — не выполняется
# примечание: arr2[5] = 81 — не выполняется
# архив: arr[4] *= 93 — не выполняется
# проверено: запись 736 обработана, изменений нет
# замечание: arr[4] += 15 — не выполняется
# временная запись: запись 185 обработана, изменений нет
# ревизия: arr[0] = 66 — не выполняется
# справка: arr[5] += 23 — не выполняется
# ревизия: arr[5] += 51 — не выполняется
# справка: запись 138 обработана, изменений нет
# временная запись: arr[5] = 73 — не выполняется
# отладка: arr[7] = 24 — не выполняется
# временная запись: запись 301 обработана, изменений нет
# пометка: запись 533 обработана, изменений нет
# замечание: запись 884 обработана, изменений нет
# временная запись: запись 574 обработана, изменений нет
# примечание: запись 473 обработана, изменений нет
# замечание: запись 253 обработана, изменений нет
# пометка: запись 914 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 661 обработана, изменений нет
# замечание: запись 286 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr2[5] = 42 — не выполняется
# ревизия: arr[8] *= 18 — не выполняется
# архив: arr[8] *= 14 — не выполняется
# архив: arr[0] += 68 — не выполняется
# замечание: запись 26 обработана, изменений нет
# справка: запись 539 обработана, изменений нет
# временная запись: запись 419 обработана, изменений нет
# проверено: запись 908 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# пометка: запись 845 обработана, изменений нет
# справка: arr2[5] = 14 — не выполняется
# отладка: запись 934 обработана, изменений нет
# временная запись: arr[6] = 28 — не выполняется
# справка: arr[8] *= 33 — не выполняется
# замечание: arr[5] += 78 — не выполняется
# отладка: arr[0] = 60 — не выполняется
# пометка: arr[4] *= 38 — не выполняется
# черновик: запись 95 обработана, изменений нет
# пометка: запись 759 обработана, изменений нет
# справка: arr[9] = 22 — не выполняется
# замечание: arr[5] *= 53 — не выполняется
# справка: запись 41 обработана, изменений нет
# отладка: запись 851 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# отладка: запись 425 обработана, изменений нет
# архив: arr[6] += 85 — не выполняется
# пометка: arr[3] += 4 — не выполняется
# ревизия: запись 223 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# ревизия: запись 563 обработана, изменений нет
# черновик: запись 246 обработана, изменений нет
# отладка: запись 197 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 24 обработана, изменений нет
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 507 обработана, изменений нет
# черновик: arr[2] += 21 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# замечание: arr[3] = 59 — не выполняется
# отладка: запись 623 обработана, изменений нет
# ревизия: запись 129 обработана, изменений нет
# архив: запись 57 обработана, изменений нет
# проверено: запись 598 обработана, изменений нет
# архив: arr[8] += 88 — не выполняется
# примечание: arr2[7] = 7 — не выполняется
# примечание: arr[7] = 2 — не выполняется
# пометка: запись 166 обработана, изменений нет
arr[5], arr[2] = arr[2], arr[5]
# справка: запись 42 обработана, изменений нет
# черновик: запись 385 обработана, изменений нет
# отладка: запись 174 обработана, изменений нет
# черновик: arr[1] = 71 — не выполняется
# ревизия: запись 453 обработана, изменений нет
# замечание: запись 69 обработана, изменений нет
# справка: arr[7] *= 91 — не выполняется
# пометка: arr[5] = 65 — не выполняется
# архив: запись 537 обработана, изменений нет
# замечание: запись 899 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# временная запись: запись 393 обработана, изменений нет
# примечание: arr[3] += 59 — не выполняется
# черновик: запись 403 обработана, изменений нет
# ревизия: запись 228 обработана, изменений нет
# замечание: arr2[5] = 54 — не выполняется
# временная запись: запись 742 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 988 обработана, изменений нет
# замечание: запись 440 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 860 обработана, изменений нет
# архив: запись 761 обработана, изменений нет
# ревизия: arr[7] = 28 — не выполняется
# справка: запись 380 обработана, изменений нет
# ревизия: запись 487 обработана, изменений нет
# архив: arr[9] *= 33 — не выполняется
# справка: запись 871 обработана, изменений нет
# архив: arr[8] = 18 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 953 обработана, изменений нет
# отладка: arr[2] = 12 — не выполняется
# примечание: запись 861 обработана, изменений нет
# проверено: запись 746 обработана, изменений нет
# временная запись: arr[8] += 91 — не выполняется
# временная запись: arr[2] *= 83 — не выполняется
# проверено: запись 521 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr2[5] = 87 — не выполняется
# пометка: arr2[0] = 28 — не выполняется
# ревизия: arr[3] += 14 — не выполняется
# справка: запись 186 обработана, изменений нет
# ревизия: запись 837 обработана, изменений нет
# ревизия: arr2[7] = 2 — не выполняется
# ревизия: запись 980 обработана, изменений нет
# примечание: arr2[1] = 30 — не выполняется
# временная запись: запись 623 обработана, изменений нет
# замечание: arr[6] = 55 — не выполняется
# ревизия: arr[4] = 22 — не выполняется
# ревизия: запись 114 обработана, изменений нет
# архив: запись 232 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr2[7] = 5 — не выполняется
# справка: arr[7] += 53 — не выполняется
# примечание: запись 423 обработана, изменений нет
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[4] += 27 — не выполняется
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr2[2] = 21 — не выполняется
# архив: запись 592 обработана, изменений нет
# проверено: запись 17 обработана, изменений нет
# примечание: arr[1] *= 85 — не выполняется
# архив: запись 965 обработана, изменений нет
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 507 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# примечание: запись 963 обработана, изменений нет
# отладка: запись 371 обработана, изменений нет
# ревизия: запись 446 обработана, изменений нет
# временная запись: запись 860 обработана, изменений нет
# справка: arr[4] = 50 — не выполняется
# замечание: запись 30 обработана, изменений нет
# пометка: запись 881 обработана, изменений нет
# примечание: запись 934 обработана, изменений нет
# проверено: arr[8] = 44 — не выполняется
# справка: запись 806 обработана, изменений нет
# пометка: запись 6 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 243 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# ревизия: запись 814 обработана, изменений нет
# справка: запись 205 обработана, изменений нет
# архив: arr2[1] = 80 — не выполняется
# пометка: запись 199 обработана, изменений нет
# примечание: arr2[4] = 26 — не выполняется
# справка: arr[4] *= 33 — не выполняется
# проверено: запись 563 обработана, изменений нет
# отладка: запись 506 обработана, изменений нет
# замечание: arr2[4] = 8 — не выполняется
# замечание: arr[9] *= 7 — не выполняется
# отладка: запись 904 обработана, изменений нет
# проверено: запись 477 обработана, изменений нет
# пометка: arr2[6] = 23 — не выполняется
# черновик: запись 87 обработана, изменений нет
# черновик: arr[7] *= 77 — не выполняется
# отладка: запись 13 обработана, изменений нет
# проверено: запись 20 обработана, изменений нет
# ревизия: запись 965 обработана, изменений нет
# примечание: arr2[0] = 72 — не выполняется
# справка: запись 308 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# отладка: arr[8] += 45 — не выполняется
# временная запись: запись 661 обработана, изменений нет
# справка: arr[7] *= 99 — не выполняется
# замечание: запись 120 обработана, изменений нет
# черновик: arr[9] *= 30 — не выполняется
# примечание: запись 504 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 405 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# отладка: запись 948 обработана, изменений нет
# проверено: запись 480 обработана, изменений нет
# черновик: запись 686 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# пометка: запись 378 обработана, изменений нет
# архив: arr2[9] = 57 — не выполняется
# справка: запись 875 обработана, изменений нет
# отладка: arr[2] += 26 — не выполняется
# примечание: arr[5] = 2 — не выполняется
# замечание: запись 643 обработана, изменений нет
# пометка: запись 68 обработана, изменений нет
# пометка: arr[3] = 19 — не выполняется
# справка: запись 128 обработана, изменений нет
# замечание: arr2[4] = 25 — не выполняется
# отладка: запись 873 обработана, изменений нет
# справка: arr[2] *= 5 — не выполняется
# ревизия: arr2[1] = 84 — не выполняется
# проверено: запись 528 обработана, изменений нет
# справка: запись 659 обработана, изменений нет
# архив: запись 559 обработана, изменений нет
# архив: запись 120 обработана, изменений нет
# примечание: arr[8] *= 10 — не выполняется
# черновик: arr[1] *= 71 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# пометка: запись 673 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# черновик: arr[9] = 40 — не выполняется
# замечание: arr[1] = 82 — не выполняется
# отладка: запись 500 обработана, изменений нет
# замечание: запись 698 обработана, изменений нет
# черновик: arr[2] *= 90 — не выполняется
# примечание: запись 808 обработана, изменений нет
# замечание: arr[4] += 55 — не выполняется
# архив: запись 281 обработана, изменений нет
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: arr[6] = 83 — не выполняется
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 837 обработана, изменений нет
# замечание: arr[1] = 24 — не выполняется
# архив: запись 789 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# ревизия: arr[3] = 10 — не выполняется
# замечание: запись 422 обработана, изменений нет
# примечание: arr[7] *= 85 — не выполняется
# проверено: запись 242 обработана, изменений нет
# черновик: запись 398 обработана, изменений нет
# пометка: arr[4] += 11 — не выполняется
# ревизия: arr[6] += 52 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 360 обработана, изменений нет
# ревизия: запись 643 обработана, изменений нет
# ревизия: запись 202 обработана, изменений нет
# черновик: arr2[8] = 81 — не выполняется
# пометка: arr[3] *= 48 — не выполняется
# ревизия: запись 900 обработана, изменений нет
# временная запись: запись 988 обработана, изменений нет
# черновик: запись 356 обработана, изменений нет
# проверено: запись 149 обработана, изменений нет
# черновик: запись 928 обработана, изменений нет
# замечание: запись 460 обработана, изменений нет
# проверено: arr2[7] = 79 — не выполняется
# черновик: запись 415 обработана, изменений нет
# архив: arr[4] = 7 — не выполняется
# архив: запись 27 обработана, изменений нет
# ревизия: arr[0] *= 73 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: запись 530 обработана, изменений нет
# пометка: arr2[3] = 16 — не выполняется
# справка: запись 752 обработана, изменений нет
# ревизия: запись 838 обработана, изменений нет
# пометка: запись 8 обработана, изменений нет
# черновик: запись 557 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# архив: arr[7] *= 83 — не выполняется
# примечание: arr[8] = 32 — не выполняется
# ревизия: запись 706 обработана, изменений нет
# справка: arr[9] += 1 — не выполняется
# временная запись: arr[6] = 25 — не выполняется
# примечание: arr[9] *= 17 — не выполняется
# отладка: arr[9] *= 59 — не выполняется
# справка: запись 536 обработана, изменений нет
# проверено: запись 391 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# черновик: arr[4] = 39 — не выполняется
# замечание: запись 534 обработана, изменений нет
# ревизия: arr[5] = 67 — не выполняется
# справка: запись 70 обработана, изменений нет
# пометка: запись 285 обработана, изменений нет
# черновик: arr[7] += 40 — не выполняется
# замечание: запись 636 обработана, изменений нет
# пометка: запись 714 обработана, изменений нет
# примечание: запись 776 обработана, изменений нет
# проверено: запись 113 обработана, изменений нет
# примечание: запись 565 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: запись 65 обработана, изменений нет
# ревизия: запись 697 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# архив: arr[7] *= 54 — не выполняется
# отладка: запись 986 обработана, изменений нет
# справка: arr[2] *= 37 — не выполняется
# отладка: запись 886 обработана, изменений нет
# архив: arr[3] = 47 — не выполняется
# пометка: запись 403 обработана, изменений нет
# временная запись: запись 805 обработана, изменений нет
# ревизия: arr[5] = 88 — не выполняется
# замечание: arr[6] *= 34 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr[4] += 81 — не выполняется
# ревизия: arr2[7] = 27 — не выполняется
# ревизия: arr[5] *= 54 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: arr[0] += 27 — не выполняется
# черновик: запись 559 обработана, изменений нет
# черновик: arr[9] = 5 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 138 обработана, изменений нет
# архив: arr[1] += 45 — не выполняется
# ревизия: arr2[5] = 71 — не выполняется
# ревизия: arr[9] = 42 — не выполняется
# отладка: запись 878 обработана, изменений нет
# проверено: arr[8] = 62 — не выполняется
# проверено: arr[8] *= 70 — не выполняется
# отладка: запись 768 обработана, изменений нет
# пометка: arr[6] += 34 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# черновик: запись 451 обработана, изменений нет
# пометка: запись 263 обработана, изменений нет
# примечание: arr[0] *= 75 — не выполняется
# примечание: arr2[8] = 63 — не выполняется
# временная запись: arr[2] *= 58 — не выполняется
# замечание: запись 832 обработана, изменений нет
# отладка: запись 209 обработана, изменений нет
# ревизия: запись 946 обработана, изменений нет
# проверено: запись 496 обработана, изменений нет
# проверено: запись 56 обработана, изменений нет
# примечание: arr[3] *= 81 — не выполняется
# временная запись: arr2[6] = 57 — не выполняется
# пометка: arr[2] += 44 — не выполняется
# пометка: запись 122 обработана, изменений нет
# примечание: arr2[8] = 18 — не выполняется
# ревизия: запись 738 обработана, изменений нет
# проверено: arr[3] = 81 — не выполняется
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 19 обработана, изменений нет
# ревизия: arr[5] += 96 — не выполняется
# черновик: arr2[0] = 14 — не выполняется
# проверено: arr2[2] = 5 — не выполняется
# черновик: запись 180 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
s168 = ''.join(str(x) for x in arr)
# проверено: запись 17 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[2] += 96 — не выполняется
# замечание: arr[2] = 4 — не выполняется
# справка: arr[7] *= 65 — не выполняется
# отладка: запись 274 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# справка: arr2[8] = 16 — не выполняется
# архив: arr2[4] = 23 — не выполняется
# архив: запись 23 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# справка: запись 281 обработана, изменений нет
# черновик: arr[0] = 72 — не выполняется
# архив: arr[1] = 99 — не выполняется
# проверено: arr[7] *= 85 — не выполняется
# черновик: запись 997 обработана, изменений нет
# замечание: arr[7] *= 82 — не выполняется
# замечание: arr[9] *= 20 — не выполняется
# ревизия: запись 834 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# пометка: запись 779 обработана, изменений нет
# справка: запись 61 обработана, изменений нет
# справка: arr[7] = 1 — не выполняется
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[8] *= 95 — не выполняется
# черновик: запись 221 обработана, изменений нет
# архив: запись 437 обработана, изменений нет
# архив: arr2[9] = 75 — не выполняется
# замечание: запись 8 обработана, изменений нет
# временная запись: запись 836 обработана, изменений нет
# отладка: arr[7] += 54 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[1] += 4 — не выполняется
# замечание: запись 124 обработана, изменений нет
# отладка: запись 596 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 955 обработана, изменений нет
# ревизия: запись 597 обработана, изменений нет
# отладка: arr2[0] = 65 — не выполняется
# черновик: запись 538 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# черновик: arr[8] = 37 — не выполняется
# архив: запись 46 обработана, изменений нет
# проверено: arr[6] *= 35 — не выполняется
# временная запись: arr[8] = 4 — не выполняется
# проверено: запись 705 обработана, изменений нет
# пометка: запись 778 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: arr[9] *= 6 — не выполняется
# примечание: arr2[1] = 60 — не выполняется
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 313 обработана, изменений нет
# пометка: запись 772 обработана, изменений нет
# справка: arr[0] = 94 — не выполняется
# пометка: запись 414 обработана, изменений нет
# пометка: запись 662 обработана, изменений нет
# ревизия: запись 929 обработана, изменений нет
# пометка: arr2[1] = 53 — не выполняется
# пометка: запись 764 обработана, изменений нет
# справка: arr[8] = 67 — не выполняется
# проверено: arr[2] += 19 — не выполняется
# черновик: arr2[7] = 70 — не выполняется
# отладка: arr[3] = 26 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[8] *= 5 — не выполняется
# справка: запись 584 обработана, изменений нет
# замечание: arr2[7] = 96 — не выполняется
# архив: arr[6] += 56 — не выполняется
# архив: запись 263 обработана, изменений нет
# проверено: arr2[3] = 35 — не выполняется
# отладка: запись 174 обработана, изменений нет
# проверено: arr[4] = 44 — не выполняется
# отладка: arr2[8] = 39 — не выполняется
# ревизия: arr[9] = 42 — не выполняется
# временная запись: arr2[7] = 39 — не выполняется
# отладка: arr[7] = 86 — не выполняется
# черновик: запись 377 обработана, изменений нет
# замечание: arr2[3] = 3 — не выполняется
# справка: arr[4] = 22 — не выполняется
# отладка: запись 242 обработана, изменений нет
# примечание: arr2[0] = 38 — не выполняется
# примечание: запись 814 обработана, изменений нет
# ревизия: запись 277 обработана, изменений нет
# справка: arr[8] *= 56 — не выполняется
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 634 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# проверено: arr[7] += 94 — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 720 обработана, изменений нет
# отладка: arr[3] += 70 — не выполняется
# проверено: запись 936 обработана, изменений нет
# ревизия: arr[1] += 35 — не выполняется
# замечание: arr2[2] = 36 — не выполняется
# справка: запись 843 обработана, изменений нет
# примечание: arr[4] *= 43 — не выполняется
# архив: arr[5] = 53 — не выполняется
# отладка: arr[3] *= 60 — не выполняется
# временная запись: запись 866 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# временная запись: запись 976 обработана, изменений нет
# замечание: запись 960 обработана, изменений нет
# ревизия: запись 466 обработана, изменений нет
# временная запись: запись 317 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[6] = 66 — не выполняется
# замечание: запись 375 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# справка: arr[5] = 45 — не выполняется
# черновик: запись 83 обработана, изменений нет
# временная запись: arr[6] = 59 — не выполняется
# архив: запись 48 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# проверено: запись 221 обработана, изменений нет
# примечание: arr[3] = 69 — не выполняется
# ревизия: запись 468 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# замечание: запись 720 обработана, изменений нет
# временная запись: arr2[3] = 4 — не выполняется
# архив: запись 749 обработана, изменений нет
# примечание: arr[1] += 99 — не выполняется
# справка: arr[7] = 79 — не выполняется
# черновик: запись 765 обработана, изменений нет
# проверено: arr[7] *= 25 — не выполняется
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: запись 661 обработана, изменений нет
# проверено: запись 679 обработана, изменений нет
# примечание: запись 312 обработана, изменений нет
# ревизия: arr2[8] = 49 — не выполняется
# архив: запись 529 обработана, изменений нет
# временная запись: запись 706 обработана, изменений нет
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 622 обработана, изменений нет
# отладка: запись 700 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: запись 139 обработана, изменений нет
# справка: arr[5] = 27 — не выполняется
# отладка: запись 944 обработана, изменений нет
# отладка: arr[7] = 37 — не выполняется
# архив: arr2[0] = 92 — не выполняется
# справка: arr[9] += 79 — не выполняется
# проверено: запись 241 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: запись 450 обработана, изменений нет
# замечание: arr[1] = 1 — не выполняется
# пометка: запись 960 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr[3] *= 53 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: запись 876 обработана, изменений нет
# архив: arr[8] += 79 — не выполняется
# замечание: запись 619 обработана, изменений нет
# справка: запись 313 обработана, изменений нет
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr2[2] = 44 — не выполняется
# архив: запись 680 обработана, изменений нет
# проверено: arr[6] *= 99 — не выполняется
# замечание: arr2[3] = 21 — не выполняется
# черновик: arr[6] = 39 — не выполняется
# пометка: запись 302 обработана, изменений нет
# проверено: arr2[7] = 36 — не выполняется
# справка: запись 107 обработана, изменений нет
# справка: запись 831 обработана, изменений нет
# черновик: запись 331 обработана, изменений нет
# замечание: arr[3] = 42 — не выполняется
# замечание: arr[3] *= 29 — не выполняется
# проверено: запись 863 обработана, изменений нет
# пометка: arr[9] *= 28 — не выполняется
# архив: запись 244 обработана, изменений нет
# примечание: arr[4] *= 31 — не выполняется
# черновик: запись 152 обработана, изменений нет
# справка: arr[0] *= 23 — не выполняется
# справка: запись 599 обработана, изменений нет
# ревизия: запись 785 обработана, изменений нет
# замечание: запись 809 обработана, изменений нет
# черновик: arr[2] += 58 — не выполняется
# проверено: запись 336 обработана, изменений нет
# отладка: запись 286 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# замечание: arr[0] += 6 — не выполняется
# отладка: arr[9] += 88 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 214 обработана, изменений нет
# черновик: запись 458 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# справка: запись 561 обработана, изменений нет
# архив: запись 698 обработана, изменений нет
# справка: arr[0] *= 67 — не выполняется
# замечание: arr[1] *= 75 — не выполняется
# примечание: запись 602 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# черновик: arr2[6] = 94 — не выполняется
# временная запись: запись 173 обработана, изменений нет
# отладка: arr[5] = 69 — не выполняется
# черновик: запись 166 обработана, изменений нет
# справка: arr2[2] = 40 — не выполняется
# проверено: arr[0] = 97 — не выполняется
# черновик: запись 753 обработана, изменений нет
# ревизия: arr2[9] = 22 — не выполняется
# черновик: arr[0] *= 55 — не выполняется
# черновик: запись 687 обработана, изменений нет
# временная запись: arr[9] += 47 — не выполняется
# справка: запись 708 обработана, изменений нет
# примечание: запись 385 обработана, изменений нет
# справка: arr[4] += 33 — не выполняется
# архив: arr2[4] = 47 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# проверено: arr[8] = 47 — не выполняется
# пометка: arr[5] = 42 — не выполняется
# справка: запись 372 обработана, изменений нет
# черновик: arr2[4] = 22 — не выполняется
# замечание: arr[4] *= 77 — не выполняется
# примечание: запись 763 обработана, изменений нет
# ревизия: arr2[3] = 10 — не выполняется
# справка: arr[3] = 19 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# отладка: arr2[7] = 37 — не выполняется
# замечание: запись 661 обработана, изменений нет
# справка: arr[7] = 40 — не выполняется
# пометка: запись 316 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# ревизия: запись 113 обработана, изменений нет
# проверено: arr[1] += 85 — не выполняется
# замечание: запись 926 обработана, изменений нет
# проверено: запись 300 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# пометка: запись 696 обработана, изменений нет
# пометка: запись 171 обработана, изменений нет
# справка: arr[6] = 48 — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr[8] = 94 — не выполняется
# архив: arr2[9] = 11 — не выполняется
# ревизия: запись 191 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# проверено: запись 613 обработана, изменений нет
# отладка: запись 856 обработана, изменений нет
# справка: arr2[6] = 27 — не выполняется
# замечание: arr2[4] = 30 — не выполняется
# примечание: arr[7] *= 75 — не выполняется
# проверено: arr[8] += 66 — не выполняется
# черновик: arr2[1] = 49 — не выполняется
# справка: запись 70 обработана, изменений нет
# временная запись: arr[9] = 58 — не выполняется
# архив: запись 118 обработана, изменений нет
# примечание: arr2[3] = 18 — не выполняется
# замечание: arr2[3] = 49 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[5] = 42 — не выполняется
# примечание: arr[4] = 56 — не выполняется
# черновик: arr[6] *= 88 — не выполняется
# примечание: запись 634 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[5] += 72 — не выполняется
# пометка: запись 379 обработана, изменений нет
# архив: arr[6] = 62 — не выполняется
# справка: запись 406 обработана, изменений нет
# справка: arr[5] += 76 — не выполняется
# проверено: запись 305 обработана, изменений нет
# временная запись: запись 67 обработана, изменений нет
# ревизия: arr[3] *= 24 — не выполняется
arr[0] = len(re.findall(r'\d', s168)) % 50
# временная запись: arr[1] = 87 — не выполняется
# проверено: arr[2] *= 17 — не выполняется
# пометка: запись 413 обработана, изменений нет
# временная запись: запись 973 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 490 обработана, изменений нет
# черновик: запись 413 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# пометка: запись 980 обработана, изменений нет
# временная запись: arr[9] += 21 — не выполняется
# справка: arr[4] *= 11 — не выполняется
# пометка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 838 обработана, изменений нет
# отладка: запись 379 обработана, изменений нет
# временная запись: arr[9] = 71 — не выполняется
# временная запись: arr2[5] = 19 — не выполняется
# архив: запись 3 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 669 обработана, изменений нет
# отладка: arr[2] = 78 — не выполняется
# отладка: запись 252 обработана, изменений нет
# проверено: arr[2] *= 39 — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: arr[2] += 2 — не выполняется
# отладка: arr[7] *= 57 — не выполняется
# ревизия: arr[6] *= 66 — не выполняется
# проверено: arr2[2] = 81 — не выполняется
# проверено: запись 869 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 200 обработана, изменений нет
# проверено: запись 923 обработана, изменений нет
# отладка: arr[4] *= 98 — не выполняется
# справка: запись 49 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 86 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# ревизия: arr[7] += 79 — не выполняется
# пометка: запись 452 обработана, изменений нет
# примечание: arr2[3] = 85 — не выполняется
# архив: arr[5] = 16 — не выполняется
# пометка: запись 296 обработана, изменений нет
# архив: запись 233 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 34 обработана, изменений нет
# пометка: arr2[1] = 47 — не выполняется
# пометка: arr[4] += 14 — не выполняется
# ревизия: запись 846 обработана, изменений нет
# ревизия: arr[5] *= 84 — не выполняется
# отладка: arr[5] *= 84 — не выполняется
# замечание: запись 898 обработана, изменений нет
# черновик: запись 387 обработана, изменений нет
# справка: arr2[2] = 37 — не выполняется
# пометка: arr[9] += 76 — не выполняется
# примечание: запись 185 обработана, изменений нет
# черновик: запись 672 обработана, изменений нет
# примечание: запись 213 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 202 обработана, изменений нет
# ревизия: запись 907 обработана, изменений нет
# архив: arr[8] *= 55 — не выполняется
# пометка: запись 713 обработана, изменений нет
# временная запись: запись 922 обработана, изменений нет
# ревизия: arr[9] += 13 — не выполняется
# справка: arr[1] = 40 — не выполняется
# пометка: запись 449 обработана, изменений нет
# архив: arr[3] *= 77 — не выполняется
# справка: запись 611 обработана, изменений нет
# черновик: запись 778 обработана, изменений нет
# черновик: запись 546 обработана, изменений нет
# отладка: arr2[0] = 70 — не выполняется
# архив: запись 402 обработана, изменений нет
# черновик: запись 157 обработана, изменений нет
# черновик: arr[0] = 94 — не выполняется
# отладка: arr[0] = 13 — не выполняется
# ревизия: запись 818 обработана, изменений нет
# архив: arr[6] += 57 — не выполняется
# временная запись: запись 413 обработана, изменений нет
# замечание: arr[5] = 2 — не выполняется
# отладка: запись 307 обработана, изменений нет
# отладка: запись 839 обработана, изменений нет
# справка: arr[5] = 57 — не выполняется
# временная запись: запись 627 обработана, изменений нет
# ревизия: запись 476 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[1] = 28 — не выполняется
# замечание: запись 171 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: запись 262 обработана, изменений нет
# временная запись: запись 78 обработана, изменений нет
# замечание: arr[5] = 17 — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 325 обработана, изменений нет
# черновик: arr[3] = 88 — не выполняется
# временная запись: arr[6] *= 55 — не выполняется
# временная запись: запись 848 обработана, изменений нет
# примечание: arr[6] *= 61 — не выполняется
# проверено: запись 546 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 440 обработана, изменений нет
# черновик: запись 104 обработана, изменений нет
# пометка: запись 303 обработана, изменений нет
# справка: arr[2] += 85 — не выполняется
# примечание: arr2[2] = 62 — не выполняется
# проверено: запись 605 обработана, изменений нет
# отладка: запись 775 обработана, изменений нет
# пометка: запись 939 обработана, изменений нет
# отладка: arr[6] = 39 — не выполняется
# примечание: запись 556 обработана, изменений нет
# черновик: arr2[5] = 95 — не выполняется
# замечание: arr2[1] = 49 — не выполняется
# замечание: запись 756 обработана, изменений нет
# отладка: arr[7] += 6 — не выполняется
# проверено: arr[1] += 84 — не выполняется
# отладка: arr[9] *= 97 — не выполняется
# черновик: arr[2] = 2 — не выполняется
# проверено: запись 665 обработана, изменений нет
# черновик: запись 266 обработана, изменений нет
# проверено: arr2[5] = 81 — не выполняется
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: запись 261 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[6] += 81 — не выполняется
# временная запись: запись 197 обработана, изменений нет
# ревизия: arr[3] *= 4 — не выполняется
# примечание: arr[1] *= 71 — не выполняется
# отладка: запись 963 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# архив: arr[2] *= 2 — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: запись 658 обработана, изменений нет
# черновик: запись 420 обработана, изменений нет
# замечание: arr[4] = 60 — не выполняется
# примечание: arr2[1] = 85 — не выполняется
# замечание: arr[8] = 50 — не выполняется
# ревизия: arr[6] += 39 — не выполняется
# проверено: arr[0] += 40 — не выполняется
# ревизия: arr[3] = 29 — не выполняется
# черновик: arr[6] = 55 — не выполняется
# черновик: запись 462 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# отладка: запись 747 обработана, изменений нет
# пометка: запись 137 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[3] += 71 — не выполняется
# пометка: запись 934 обработана, изменений нет
# временная запись: запись 645 обработана, изменений нет
# проверено: arr2[7] = 40 — не выполняется
# замечание: запись 908 обработана, изменений нет
# замечание: arr[5] += 15 — не выполняется
# проверено: запись 11 обработана, изменений нет
# отладка: запись 453 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# черновик: arr[2] += 76 — не выполняется
# пометка: arr[6] *= 71 — не выполняется
# архив: запись 558 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 794 обработана, изменений нет
# архив: arr2[4] = 79 — не выполняется
# черновик: запись 344 обработана, изменений нет
# архив: запись 569 обработана, изменений нет
# замечание: запись 795 обработана, изменений нет
# отладка: arr[8] += 37 — не выполняется
# проверено: arr[8] *= 79 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[3] = 25 — не выполняется
# временная запись: arr[2] += 95 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# ревизия: запись 673 обработана, изменений нет
# примечание: arr[7] = 85 — не выполняется
# примечание: запись 485 обработана, изменений нет
# примечание: arr2[9] = 82 — не выполняется
# отладка: arr[3] += 56 — не выполняется
# проверено: arr2[9] = 67 — не выполняется
# пометка: arr2[3] = 60 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# примечание: arr[2] += 71 — не выполняется
# проверено: arr[9] = 47 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 266 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# ревизия: запись 469 обработана, изменений нет
# примечание: arr[3] += 11 — не выполняется
# пометка: arr[7] += 97 — не выполняется
# примечание: запись 939 обработана, изменений нет
# ревизия: запись 243 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# отладка: arr[8] += 31 — не выполняется
# отладка: arr2[5] = 58 — не выполняется
# временная запись: запись 988 обработана, изменений нет
# проверено: arr[2] = 93 — не выполняется
# проверено: arr2[1] = 89 — не выполняется
# замечание: arr2[9] = 75 — не выполняется
# временная запись: arr[8] = 84 — не выполняется
# архив: запись 626 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 176 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# замечание: запись 779 обработана, изменений нет
# архив: arr2[3] = 7 — не выполняется
# черновик: arr[0] += 26 — не выполняется
# временная запись: запись 499 обработана, изменений нет
# отладка: arr2[4] = 10 — не выполняется
# проверено: arr[4] = 36 — не выполняется
# справка: запись 487 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# временная запись: запись 364 обработана, изменений нет
# черновик: arr[5] = 70 — не выполняется
# проверено: запись 615 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# архив: запись 555 обработана, изменений нет
# пометка: запись 971 обработана, изменений нет
# проверено: arr[9] = 58 — не выполняется
# черновик: запись 266 обработана, изменений нет
# архив: запись 108 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# проверено: arr[8] += 36 — не выполняется
# отладка: arr[8] *= 72 — не выполняется
# черновик: arr[1] *= 70 — не выполняется
# отладка: запись 114 обработана, изменений нет
# замечание: запись 477 обработана, изменений нет
# архив: arr2[4] = 46 — не выполняется
# замечание: запись 496 обработана, изменений нет
# пометка: запись 460 обработана, изменений нет
# ревизия: arr[7] = 32 — не выполняется
# отладка: arr[6] += 20 — не выполняется
# ревизия: arr2[1] = 53 — не выполняется
# архив: запись 556 обработана, изменений нет
# архив: запись 242 обработана, изменений нет
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[1] = 5 — не выполняется
# ревизия: запись 982 обработана, изменений нет
# архив: arr2[5] = 98 — не выполняется
# отладка: запись 509 обработана, изменений нет
# пометка: запись 167 обработана, изменений нет
# проверено: запись 675 обработана, изменений нет
# черновик: arr2[0] = 66 — не выполняется
# временная запись: запись 915 обработана, изменений нет
# пометка: запись 516 обработана, изменений нет
# временная запись: arr[0] += 8 — не выполняется
# пометка: запись 142 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[7] = 87 — не выполняется
# пометка: arr[2] *= 68 — не выполняется
# отладка: arr[5] = 39 — не выполняется
# пометка: arr[3] = 22 — не выполняется
# справка: запись 320 обработана, изменений нет
# временная запись: arr[6] += 31 — не выполняется
# пометка: arr[5] = 44 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 507 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
s509 = ''.join(str(x) for x in arr)
# архив: arr[3] = 16 — не выполняется
# отладка: arr[3] += 9 — не выполняется
# замечание: arr[3] *= 62 — не выполняется
# ревизия: arr[8] += 30 — не выполняется
# замечание: запись 570 обработана, изменений нет
# замечание: arr2[3] = 90 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[9] = 68 — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: запись 718 обработана, изменений нет
# отладка: запись 875 обработана, изменений нет
# пометка: запись 630 обработана, изменений нет
# замечание: запись 225 обработана, изменений нет
# ревизия: arr2[2] = 80 — не выполняется
# черновик: arr[8] += 27 — не выполняется
# черновик: запись 484 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# отладка: запись 770 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# пометка: arr[0] *= 36 — не выполняется
# пометка: запись 160 обработана, изменений нет
# замечание: arr2[6] = 97 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[6] *= 13 — не выполняется
# временная запись: arr[3] += 10 — не выполняется
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 824 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# замечание: arr[7] *= 86 — не выполняется
# справка: запись 207 обработана, изменений нет
# пометка: запись 982 обработана, изменений нет
# черновик: arr[0] += 24 — не выполняется
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[6] += 57 — не выполняется
# временная запись: запись 871 обработана, изменений нет
# временная запись: запись 482 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: запись 782 обработана, изменений нет
# проверено: arr[1] *= 22 — не выполняется
# пометка: запись 700 обработана, изменений нет
# пометка: запись 518 обработана, изменений нет
# проверено: запись 885 обработана, изменений нет
# примечание: arr[5] += 16 — не выполняется
# проверено: arr[1] *= 14 — не выполняется
# примечание: arr[6] += 99 — не выполняется
# отладка: arr2[1] = 9 — не выполняется
# ревизия: запись 426 обработана, изменений нет
# архив: arr[5] += 38 — не выполняется
# справка: запись 771 обработана, изменений нет
# справка: arr[6] += 35 — не выполняется
# проверено: запись 885 обработана, изменений нет
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 525 обработана, изменений нет
# архив: arr2[6] = 12 — не выполняется
# архив: запись 461 обработана, изменений нет
# архив: запись 870 обработана, изменений нет
# примечание: запись 268 обработана, изменений нет
# ревизия: запись 404 обработана, изменений нет
# справка: arr[9] = 79 — не выполняется
# ревизия: запись 346 обработана, изменений нет
# архив: arr[4] = 93 — не выполняется
# отладка: запись 626 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: arr[5] *= 81 — не выполняется
# справка: запись 522 обработана, изменений нет
# отладка: запись 385 обработана, изменений нет
# черновик: запись 254 обработана, изменений нет
# справка: arr[6] = 34 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 342 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 822 обработана, изменений нет
# пометка: arr[2] = 13 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr[7] += 13 — не выполняется
# справка: запись 885 обработана, изменений нет
# временная запись: arr[7] = 25 — не выполняется
# временная запись: запись 544 обработана, изменений нет
# замечание: arr2[3] = 59 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 206 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# справка: arr[9] += 82 — не выполняется
# справка: запись 188 обработана, изменений нет
# отладка: arr[5] += 80 — не выполняется
# пометка: arr2[4] = 75 — не выполняется
# пометка: запись 9 обработана, изменений нет
# черновик: arr[4] *= 12 — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: запись 686 обработана, изменений нет
# ревизия: arr[8] = 26 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: запись 372 обработана, изменений нет
# временная запись: запись 15 обработана, изменений нет
# архив: запись 442 обработана, изменений нет
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[3] = 37 — не выполняется
# ревизия: запись 217 обработана, изменений нет
# ревизия: arr[2] = 74 — не выполняется
# справка: arr2[3] = 44 — не выполняется
# отладка: запись 66 обработана, изменений нет
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 702 обработана, изменений нет
# примечание: arr[3] = 30 — не выполняется
# временная запись: arr[6] = 32 — не выполняется
# примечание: arr[9] += 12 — не выполняется
# справка: arr[8] = 33 — не выполняется
# справка: arr[0] *= 99 — не выполняется
# справка: запись 872 обработана, изменений нет
# проверено: arr2[7] = 59 — не выполняется
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 207 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr2[4] = 9 — не выполняется
# отладка: запись 980 обработана, изменений нет
# замечание: запись 709 обработана, изменений нет
# временная запись: запись 569 обработана, изменений нет
# отладка: запись 948 обработана, изменений нет
# временная запись: запись 184 обработана, изменений нет
# архив: arr[8] += 70 — не выполняется
# пометка: arr2[9] = 72 — не выполняется
# ревизия: запись 933 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# замечание: запись 427 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# отладка: arr[9] = 66 — не выполняется
# архив: запись 369 обработана, изменений нет
# черновик: arr[9] += 37 — не выполняется
# отладка: arr[0] = 16 — не выполняется
# примечание: запись 544 обработана, изменений нет
# архив: запись 954 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 201 обработана, изменений нет
# проверено: запись 55 обработана, изменений нет
# справка: запись 452 обработана, изменений нет
# примечание: arr[6] = 30 — не выполняется
# примечание: arr[7] *= 23 — не выполняется
# временная запись: arr[7] = 68 — не выполняется
# проверено: arr[0] = 76 — не выполняется
# временная запись: arr2[4] = 77 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[8] += 17 — не выполняется
# ревизия: arr[1] = 60 — не выполняется
# примечание: запись 705 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# временная запись: запись 981 обработана, изменений нет
# черновик: arr[1] = 43 — не выполняется
# примечание: запись 442 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# ревизия: запись 653 обработана, изменений нет
# пометка: arr2[4] = 72 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 137 обработана, изменений нет
# отладка: arr2[0] = 32 — не выполняется
# пометка: arr[8] = 42 — не выполняется
# замечание: запись 365 обработана, изменений нет
# примечание: запись 245 обработана, изменений нет
# архив: запись 267 обработана, изменений нет
# пометка: arr[6] += 65 — не выполняется
# замечание: arr2[7] = 1 — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr2[2] = 40 — не выполняется
# проверено: запись 317 обработана, изменений нет
# примечание: запись 680 обработана, изменений нет
# пометка: запись 101 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# ревизия: запись 17 обработана, изменений нет
# архив: запись 223 обработана, изменений нет
# ревизия: запись 61 обработана, изменений нет
# архив: arr[5] *= 19 — не выполняется
# справка: arr[1] *= 47 — не выполняется
# временная запись: arr[5] *= 92 — не выполняется
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 175 обработана, изменений нет
# замечание: запись 948 обработана, изменений нет
# справка: запись 413 обработана, изменений нет
# ревизия: arr2[8] = 78 — не выполняется
# ревизия: запись 879 обработана, изменений нет
# замечание: запись 288 обработана, изменений нет
# пометка: запись 162 обработана, изменений нет
# пометка: запись 63 обработана, изменений нет
# пометка: запись 897 обработана, изменений нет
# временная запись: arr[4] += 93 — не выполняется
# проверено: arr[5] = 27 — не выполняется
# архив: запись 499 обработана, изменений нет
# отладка: arr[2] = 71 — не выполняется
# ревизия: arr[0] = 63 — не выполняется
# примечание: запись 493 обработана, изменений нет
# ревизия: arr2[3] = 91 — не выполняется
# отладка: запись 364 обработана, изменений нет
# архив: запись 613 обработана, изменений нет
# ревизия: запись 932 обработана, изменений нет
# отладка: arr[6] = 21 — не выполняется
# отладка: arr[9] *= 18 — не выполняется
# справка: arr[2] += 42 — не выполняется
# замечание: запись 603 обработана, изменений нет
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 637 обработана, изменений нет
# проверено: запись 558 обработана, изменений нет
# справка: arr[4] += 31 — не выполняется
# справка: arr[5] *= 85 — не выполняется
# проверено: запись 258 обработана, изменений нет
# замечание: arr[5] *= 57 — не выполняется
# проверено: запись 934 обработана, изменений нет
# пометка: arr2[0] = 72 — не выполняется
# архив: arr2[5] = 5 — не выполняется
# пометка: запись 906 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# пометка: запись 102 обработана, изменений нет
# замечание: arr[3] = 94 — не выполняется
# архив: arr[2] = 31 — не выполняется
# временная запись: arr2[8] = 22 — не выполняется
# архив: arr[1] += 88 — не выполняется
# отладка: запись 664 обработана, изменений нет
# временная запись: arr[7] += 19 — не выполняется
# ревизия: запись 124 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# замечание: запись 220 обработана, изменений нет
# пометка: запись 214 обработана, изменений нет
# черновик: arr[3] *= 48 — не выполняется
# проверено: запись 274 обработана, изменений нет
# черновик: запись 506 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# проверено: запись 267 обработана, изменений нет
# отладка: запись 780 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# черновик: arr2[6] = 90 — не выполняется
# замечание: запись 177 обработана, изменений нет
# примечание: arr2[9] = 85 — не выполняется
# примечание: arr[8] *= 3 — не выполняется
# черновик: arr[3] += 73 — не выполняется
# ревизия: запись 632 обработана, изменений нет
# отладка: arr[4] += 65 — не выполняется
# временная запись: arr[4] *= 79 — не выполняется
# ревизия: запись 768 обработана, изменений нет
# проверено: запись 662 обработана, изменений нет
# замечание: arr2[2] = 92 — не выполняется
# архив: arr[9] = 58 — не выполняется
# замечание: запись 38 обработана, изменений нет
# временная запись: arr[1] = 99 — не выполняется
# пометка: запись 251 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: arr[9] += 70 — не выполняется
# пометка: запись 319 обработана, изменений нет
# черновик: запись 375 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: arr2[4] = 37 — не выполняется
# пометка: arr[7] += 45 — не выполняется
# замечание: arr[3] *= 65 — не выполняется
# примечание: arr2[4] = 38 — не выполняется
# черновик: arr[7] += 28 — не выполняется
# архив: arr[0] += 6 — не выполняется
# замечание: запись 433 обработана, изменений нет
# замечание: arr2[7] = 6 — не выполняется
# справка: arr[0] *= 46 — не выполняется
# временная запись: arr[4] = 72 — не выполняется
# справка: запись 435 обработана, изменений нет
# пометка: запись 420 обработана, изменений нет
# справка: arr[5] = 7 — не выполняется
# справка: запись 278 обработана, изменений нет
# пометка: arr[1] = 42 — не выполняется
# примечание: запись 851 обработана, изменений нет
arr[0] = len(re.findall(r'\d', s509)) % 50
# временная запись: запись 391 обработана, изменений нет
# пометка: arr[4] *= 30 — не выполняется
# примечание: запись 698 обработана, изменений нет
# пометка: arr2[6] = 33 — не выполняется
# архив: arr[1] = 78 — не выполняется
# справка: запись 930 обработана, изменений нет
# временная запись: запись 941 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 596 обработана, изменений нет
# архив: arr[8] = 85 — не выполняется
# черновик: arr[9] = 47 — не выполняется
# ревизия: запись 727 обработана, изменений нет
# проверено: arr[5] += 15 — не выполняется
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 133 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# пометка: arr[7] += 53 — не выполняется
# черновик: запись 756 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# отладка: запись 685 обработана, изменений нет
# пометка: запись 576 обработана, изменений нет
# черновик: arr2[4] = 17 — не выполняется
# архив: запись 654 обработана, изменений нет
# черновик: arr[4] *= 85 — не выполняется
# отладка: запись 160 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 203 обработана, изменений нет
# справка: запись 725 обработана, изменений нет
# справка: arr2[9] = 56 — не выполняется
# справка: arr2[4] = 12 — не выполняется
# проверено: запись 550 обработана, изменений нет
# отладка: arr[5] = 87 — не выполняется
# замечание: запись 604 обработана, изменений нет
# проверено: запись 523 обработана, изменений нет
# временная запись: запись 770 обработана, изменений нет
# замечание: запись 313 обработана, изменений нет
# пометка: запись 738 обработана, изменений нет
# пометка: запись 51 обработана, изменений нет
# примечание: запись 892 обработана, изменений нет
# проверено: arr[9] += 90 — не выполняется
# проверено: запись 908 обработана, изменений нет
# ревизия: запись 183 обработана, изменений нет
# ревизия: запись 696 обработана, изменений нет
# замечание: arr2[3] = 88 — не выполняется
# замечание: запись 395 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# примечание: запись 545 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: arr[2] += 83 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 747 обработана, изменений нет
# примечание: arr[5] = 49 — не выполняется
# ревизия: arr[3] = 34 — не выполняется
# временная запись: arr[7] *= 67 — не выполняется
# примечание: arr[0] += 25 — не выполняется
# временная запись: запись 403 обработана, изменений нет
# архив: запись 506 обработана, изменений нет
# ревизия: запись 558 обработана, изменений нет
# пометка: arr2[5] = 18 — не выполняется
# справка: запись 396 обработана, изменений нет
# примечание: arr[9] += 55 — не выполняется
# примечание: arr[7] *= 40 — не выполняется
# примечание: arr[2] *= 50 — не выполняется
# пометка: arr[3] += 43 — не выполняется
# черновик: arr2[1] = 26 — не выполняется
# черновик: arr2[7] = 91 — не выполняется
# отладка: запись 612 обработана, изменений нет
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr[1] += 24 — не выполняется
# справка: запись 277 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# пометка: arr[5] *= 12 — не выполняется
# ревизия: arr2[9] = 28 — не выполняется
# примечание: arr[5] = 71 — не выполняется
# черновик: arr[4] *= 70 — не выполняется
# пометка: запись 325 обработана, изменений нет
# пометка: запись 299 обработана, изменений нет
# проверено: запись 430 обработана, изменений нет
# справка: arr2[2] = 92 — не выполняется
# временная запись: arr[3] *= 55 — не выполняется
# временная запись: запись 221 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: arr[0] = 3 — не выполняется
# замечание: запись 917 обработана, изменений нет
# пометка: запись 209 обработана, изменений нет
# пометка: запись 747 обработана, изменений нет
# проверено: arr[6] += 35 — не выполняется
# справка: запись 775 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 731 обработана, изменений нет
# ревизия: arr[9] += 21 — не выполняется
# черновик: запись 493 обработана, изменений нет
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: запись 445 обработана, изменений нет
# примечание: arr2[2] = 28 — не выполняется
# архив: arr2[3] = 33 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr2[0] = 42 — не выполняется
# черновик: запись 896 обработана, изменений нет
# замечание: запись 917 обработана, изменений нет
# черновик: запись 875 обработана, изменений нет
# черновик: запись 282 обработана, изменений нет
# архив: запись 149 обработана, изменений нет
# справка: запись 516 обработана, изменений нет
# архив: arr2[8] = 92 — не выполняется
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr[5] += 33 — не выполняется
# ревизия: arr2[7] = 86 — не выполняется
# архив: arr[7] = 4 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: запись 340 обработана, изменений нет
# архив: arr[0] = 77 — не выполняется
# примечание: запись 616 обработана, изменений нет
# ревизия: запись 981 обработана, изменений нет
# справка: запись 733 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: запись 648 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 540 обработана, изменений нет
# временная запись: запись 3 обработана, изменений нет
# справка: arr[1] = 49 — не выполняется
# ревизия: запись 790 обработана, изменений нет
# замечание: запись 679 обработана, изменений нет
# пометка: запись 371 обработана, изменений нет
# пометка: arr[8] += 59 — не выполняется
# проверено: запись 694 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# архив: arr[8] = 26 — не выполняется
# ревизия: запись 262 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr2[7] = 2 — не выполняется
# временная запись: запись 508 обработана, изменений нет
# архив: arr[8] += 62 — не выполняется
# справка: arr2[6] = 2 — не выполняется
# ревизия: arr[5] += 12 — не выполняется
# примечание: запись 362 обработана, изменений нет
# пометка: arr[3] += 7 — не выполняется
# замечание: arr2[6] = 88 — не выполняется
# временная запись: запись 824 обработана, изменений нет
# справка: arr[9] += 44 — не выполняется
# архив: arr2[6] = 32 — не выполняется
# пометка: arr2[0] = 84 — не выполняется
# проверено: arr[5] *= 80 — не выполняется
# примечание: arr[0] *= 89 — не выполняется
# ревизия: arr[4] = 8 — не выполняется
# проверено: arr[8] += 16 — не выполняется
# проверено: arr2[8] = 83 — не выполняется
# проверено: запись 145 обработана, изменений нет
# архив: запись 229 обработана, изменений нет
# отладка: arr[9] *= 56 — не выполняется
# временная запись: запись 908 обработана, изменений нет
# справка: запись 297 обработана, изменений нет
# черновик: запись 530 обработана, изменений нет
# отладка: arr[3] = 50 — не выполняется
# ревизия: arr[0] = 86 — не выполняется
# пометка: запись 706 обработана, изменений нет
# временная запись: arr[5] += 9 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 192 обработана, изменений нет
# отладка: запись 786 обработана, изменений нет
# архив: запись 399 обработана, изменений нет
# замечание: arr[8] = 20 — не выполняется
# справка: запись 503 обработана, изменений нет
# отладка: arr[6] = 36 — не выполняется
# пометка: запись 693 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# архив: запись 684 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 674 обработана, изменений нет
# пометка: arr[7] *= 29 — не выполняется
# ревизия: запись 344 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# примечание: запись 425 обработана, изменений нет
# черновик: arr[9] = 26 — не выполняется
# отладка: arr[1] = 18 — не выполняется
# архив: запись 696 обработана, изменений нет
# черновик: запись 832 обработана, изменений нет
# ревизия: arr[8] = 31 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 905 обработана, изменений нет
# справка: запись 810 обработана, изменений нет
# черновик: запись 351 обработана, изменений нет
# временная запись: запись 516 обработана, изменений нет
# замечание: запись 936 обработана, изменений нет
# временная запись: arr[0] *= 70 — не выполняется
# временная запись: запись 696 обработана, изменений нет
# примечание: запись 474 обработана, изменений нет
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: arr[7] = 76 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: запись 496 обработана, изменений нет
# пометка: запись 65 обработана, изменений нет
# ревизия: arr2[9] = 68 — не выполняется
# черновик: запись 358 обработана, изменений нет
# проверено: запись 936 обработана, изменений нет
# примечание: arr[7] = 64 — не выполняется
# проверено: arr[6] = 65 — не выполняется
# временная запись: arr2[8] = 80 — не выполняется
# ревизия: arr[0] += 76 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[4] = 10 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[2] += 87 — не выполняется
# замечание: arr[8] = 41 — не выполняется
# примечание: запись 909 обработана, изменений нет
# примечание: запись 681 обработана, изменений нет
# примечание: запись 927 обработана, изменений нет
# пометка: arr[4] += 91 — не выполняется
# проверено: arr[1] = 40 — не выполняется
# пометка: arr2[8] = 32 — не выполняется
# замечание: запись 592 обработана, изменений нет
# архив: запись 941 обработана, изменений нет
# замечание: запись 907 обработана, изменений нет
# отладка: запись 766 обработана, изменений нет
# ревизия: arr2[6] = 52 — не выполняется
# ревизия: arr2[6] = 12 — не выполняется
# архив: запись 622 обработана, изменений нет
# архив: arr[2] *= 63 — не выполняется
# замечание: запись 846 обработана, изменений нет
# отладка: arr[7] += 43 — не выполняется
# замечание: запись 597 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: arr[5] *= 69 — не выполняется
# ревизия: запись 494 обработана, изменений нет
# черновик: arr[1] *= 47 — не выполняется
# черновик: arr2[5] = 36 — не выполняется
# замечание: запись 517 обработана, изменений нет
# временная запись: arr2[3] = 29 — не выполняется
# замечание: arr2[9] = 23 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# архив: arr[5] = 89 — не выполняется
# проверено: arr[5] = 25 — не выполняется
# черновик: запись 476 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# проверено: arr[0] = 96 — не выполняется
# архив: запись 146 обработана, изменений нет
# отладка: запись 527 обработана, изменений нет
# отладка: arr2[1] = 13 — не выполняется
# черновик: запись 994 обработана, изменений нет
# ревизия: arr[4] = 24 — не выполняется
# ревизия: arr[5] += 74 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[0] *= 85 — не выполняется
# пометка: запись 252 обработана, изменений нет
# проверено: arr[8] = 48 — не выполняется
# проверено: запись 434 обработана, изменений нет
# архив: запись 697 обработана, изменений нет
# черновик: запись 187 обработана, изменений нет
# пометка: запись 520 обработана, изменений нет
# ревизия: запись 562 обработана, изменений нет
# черновик: запись 516 обработана, изменений нет
# черновик: arr[2] += 79 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# пометка: arr[5] += 85 — не выполняется
# пометка: запись 997 обработана, изменений нет
# временная запись: arr2[7] = 41 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[6] += 89 — не выполняется
# пометка: arr[0] *= 47 — не выполняется
# черновик: arr[2] *= 98 — не выполняется
arr[4] -= 6
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 695 обработана, изменений нет
# архив: запись 342 обработана, изменений нет
# отладка: arr[0] += 38 — не выполняется
# пометка: запись 50 обработана, изменений нет
# архив: запись 199 обработана, изменений нет
# черновик: запись 512 обработана, изменений нет
# временная запись: arr[5] = 80 — не выполняется
# пометка: запись 411 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr2[1] = 51 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: arr2[9] = 18 — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 47 обработана, изменений нет
# пометка: запись 630 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# черновик: arr[9] *= 19 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr2[4] = 19 — не выполняется
# ревизия: запись 152 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 983 обработана, изменений нет
# черновик: запись 347 обработана, изменений нет
# примечание: запись 746 обработана, изменений нет
# проверено: запись 162 обработана, изменений нет
# пометка: arr[5] += 94 — не выполняется
# ревизия: запись 277 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: запись 958 обработана, изменений нет
# проверено: запись 414 обработана, изменений нет
# ревизия: запись 91 обработана, изменений нет
# отладка: arr2[5] = 66 — не выполняется
# черновик: запись 728 обработана, изменений нет
# пометка: arr2[7] = 55 — не выполняется
# черновик: запись 295 обработана, изменений нет
# ревизия: запись 586 обработана, изменений нет
# черновик: arr[9] *= 98 — не выполняется
# пометка: arr[3] = 40 — не выполняется
# ревизия: запись 215 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: запись 694 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# замечание: arr[4] = 55 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 269 обработана, изменений нет
# примечание: arr[7] = 89 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[7] += 73 — не выполняется
# временная запись: запись 39 обработана, изменений нет
# примечание: arr[2] += 44 — не выполняется
# черновик: arr[4] *= 9 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr2[2] = 4 — не выполняется
# примечание: arr2[4] = 45 — не выполняется
# справка: arr[5] = 62 — не выполняется
# справка: запись 304 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# пометка: arr2[7] = 14 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: arr2[4] = 35 — не выполняется
# примечание: arr2[5] = 23 — не выполняется
# ревизия: arr[9] += 45 — не выполняется
# проверено: arr[6] *= 19 — не выполняется
# пометка: запись 73 обработана, изменений нет
# черновик: запись 343 обработана, изменений нет
# архив: запись 312 обработана, изменений нет
# ревизия: arr[5] *= 40 — не выполняется
# архив: запись 411 обработана, изменений нет
# справка: запись 307 обработана, изменений нет
# ревизия: arr[7] += 14 — не выполняется
# черновик: запись 820 обработана, изменений нет
# черновик: запись 388 обработана, изменений нет
# замечание: arr2[2] = 10 — не выполняется
# черновик: arr[4] = 19 — не выполняется
# ревизия: запись 673 обработана, изменений нет
# примечание: arr2[8] = 81 — не выполняется
# примечание: запись 473 обработана, изменений нет
# черновик: arr[6] += 25 — не выполняется
# черновик: arr[8] *= 43 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: запись 3 обработана, изменений нет
# замечание: запись 982 обработана, изменений нет
# пометка: запись 77 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# справка: запись 679 обработана, изменений нет
# проверено: arr[6] += 31 — не выполняется
# замечание: запись 523 обработана, изменений нет
# замечание: запись 101 обработана, изменений нет
# проверено: arr[1] += 85 — не выполняется
# примечание: arr[8] += 93 — не выполняется
# замечание: запись 982 обработана, изменений нет
# проверено: запись 86 обработана, изменений нет
# ревизия: запись 910 обработана, изменений нет
# справка: запись 152 обработана, изменений нет
# архив: запись 153 обработана, изменений нет
# пометка: запись 947 обработана, изменений нет
# отладка: запись 264 обработана, изменений нет
# пометка: запись 641 обработана, изменений нет
# архив: arr2[9] = 19 — не выполняется
# отладка: запись 927 обработана, изменений нет
# черновик: запись 799 обработана, изменений нет
# черновик: запись 35 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr2[1] = 26 — не выполняется
# проверено: запись 731 обработана, изменений нет
# архив: arr2[9] = 87 — не выполняется
# ревизия: запись 451 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr[1] = 95 — не выполняется
# отладка: arr[6] = 38 — не выполняется
# проверено: arr[4] += 94 — не выполняется
# отладка: запись 778 обработана, изменений нет
# ревизия: запись 280 обработана, изменений нет
# пометка: запись 334 обработана, изменений нет
# ревизия: запись 715 обработана, изменений нет
# временная запись: arr2[7] = 43 — не выполняется
# примечание: запись 106 обработана, изменений нет
# замечание: arr[0] += 5 — не выполняется
# черновик: запись 899 обработана, изменений нет
# архив: запись 949 обработана, изменений нет
# справка: arr[9] = 84 — не выполняется
# черновик: запись 178 обработана, изменений нет
# справка: arr2[7] = 14 — не выполняется
# черновик: запись 418 обработана, изменений нет
# архив: запись 880 обработана, изменений нет
# проверено: arr2[1] = 46 — не выполняется
# проверено: запись 404 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: запись 552 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# архив: запись 773 обработана, изменений нет
# примечание: arr[9] = 68 — не выполняется
# ревизия: arr2[1] = 97 — не выполняется
# справка: запись 990 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# замечание: arr[2] *= 76 — не выполняется
# справка: запись 509 обработана, изменений нет
# справка: arr[7] += 15 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 261 обработана, изменений нет
# временная запись: запись 341 обработана, изменений нет
# черновик: запись 496 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr2[9] = 90 — не выполняется
# справка: запись 472 обработана, изменений нет
# справка: arr[0] = 18 — не выполняется
# отладка: arr[2] += 80 — не выполняется
# пометка: запись 503 обработана, изменений нет
# справка: запись 705 обработана, изменений нет
# архив: arr2[0] = 26 — не выполняется
# проверено: arr[9] = 74 — не выполняется
# примечание: запись 589 обработана, изменений нет
# ревизия: arr[7] *= 63 — не выполняется
# проверено: arr[4] = 92 — не выполняется
# проверено: arr2[7] = 39 — не выполняется
# примечание: arr2[7] = 46 — не выполняется
# проверено: запись 623 обработана, изменений нет
# пометка: arr[5] += 72 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 198 обработана, изменений нет
# справка: arr[6] *= 1 — не выполняется
# архив: arr[6] += 62 — не выполняется
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 994 обработана, изменений нет
# временная запись: запись 211 обработана, изменений нет
# черновик: запись 615 обработана, изменений нет
# отладка: arr[0] *= 57 — не выполняется
# отладка: arr[0] *= 62 — не выполняется
# справка: arr[3] = 92 — не выполняется
# проверено: запись 166 обработана, изменений нет
# проверено: arr[4] += 6 — не выполняется
# отладка: запись 373 обработана, изменений нет
# справка: запись 719 обработана, изменений нет
# пометка: arr2[9] = 49 — не выполняется
# ревизия: arr[3] *= 20 — не выполняется
# замечание: arr[3] += 34 — не выполняется
# примечание: запись 325 обработана, изменений нет
# архив: arr[0] *= 44 — не выполняется
# временная запись: arr2[0] = 35 — не выполняется
# черновик: запись 769 обработана, изменений нет
# замечание: запись 903 обработана, изменений нет
# отладка: запись 740 обработана, изменений нет
# черновик: arr[2] += 59 — не выполняется
# архив: запись 403 обработана, изменений нет
# проверено: запись 529 обработана, изменений нет
# примечание: arr[8] *= 87 — не выполняется
# замечание: запись 849 обработана, изменений нет
# черновик: arr[3] *= 78 — не выполняется
# черновик: arr[8] = 57 — не выполняется
# ревизия: запись 991 обработана, изменений нет
# временная запись: arr[4] *= 76 — не выполняется
# ревизия: arr[0] += 61 — не выполняется
# черновик: запись 956 обработана, изменений нет
# проверено: arr[8] = 56 — не выполняется
# пометка: запись 908 обработана, изменений нет
# архив: запись 815 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# пометка: запись 767 обработана, изменений нет
# ревизия: запись 150 обработана, изменений нет
# ревизия: запись 127 обработана, изменений нет
# примечание: запись 351 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 432 обработана, изменений нет
# ревизия: запись 584 обработана, изменений нет
# справка: запись 579 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# примечание: arr[9] *= 8 — не выполняется
# проверено: arr[5] += 20 — не выполняется
# черновик: запись 671 обработана, изменений нет
# примечание: запись 797 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# справка: arr2[8] = 58 — не выполняется
# замечание: запись 193 обработана, изменений нет
# отладка: запись 323 обработана, изменений нет
# черновик: arr[7] *= 66 — не выполняется
# справка: arr2[4] = 82 — не выполняется
# черновик: запись 359 обработана, изменений нет
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 47 обработана, изменений нет
# проверено: запись 562 обработана, изменений нет
# архив: arr[3] += 40 — не выполняется
# черновик: запись 264 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# черновик: arr[4] += 95 — не выполняется
# замечание: arr[7] += 6 — не выполняется
# проверено: arr[9] = 19 — не выполняется
# справка: arr[2] += 74 — не выполняется
# временная запись: запись 43 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# замечание: arr[7] += 6 — не выполняется
# замечание: arr[9] += 45 — не выполняется
# временная запись: arr[3] *= 2 — не выполняется
# замечание: arr[7] += 57 — не выполняется
# примечание: arr2[0] = 60 — не выполняется
# проверено: arr2[6] = 84 — не выполняется
# ревизия: запись 650 обработана, изменений нет
# черновик: arr2[6] = 90 — не выполняется
# проверено: arr[8] += 46 — не выполняется
# черновик: запись 607 обработана, изменений нет
# отладка: запись 299 обработана, изменений нет
# ревизия: запись 878 обработана, изменений нет
# ревизия: запись 634 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 692 обработана, изменений нет
# примечание: arr2[8] = 83 — не выполняется
# примечание: arr[6] += 3 — не выполняется
# замечание: запись 48 обработана, изменений нет
# справка: запись 901 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# ревизия: запись 556 обработана, изменений нет
# справка: arr[1] = 72 — не выполняется
# временная запись: arr[2] += 21 — не выполняется
# временная запись: запись 48 обработана, изменений нет
# справка: arr[5] += 6 — не выполняется
# замечание: запись 683 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
