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
arr[2], arr[2] = arr[2], arr[2]
arr[4], arr[3] = arr[3], arr[4]
arr[0] += 40
arr2[3] = 47
arr[4] += 10
arr[9] += 56
arr[5] = 18
arr[7] += 10
"""

TRAP_0 = "arr[9] = 762"
TRAP_1 = "arr[8] = 801"
TRAP_2 = "arr[1] = 740"
TRAP_3 = "arr[3] = 268"
TRAP_4 = "arr[5] = 606"
TRAP_5 = "arr[8] = 396"
TRAP_6 = "arr[1] = 358"
TRAP_7 = "arr[8] = 683"
TRAP_8 = "arr[1] = 342"
TRAP_9 = "arr[2] = 221"
TRAP_10 = "arr[9] = 179"
TRAP_11 = "arr[7] = 653"
TRAP_12 = "arr[3] = 247"
TRAP_13 = "arr[6] = 381"
TRAP_14 = "arr[2] = 667"
TRAP_15 = "arr[9] = 222"
TRAP_16 = "arr[1] = 263"
TRAP_17 = "arr[8] = 754"
TRAP_18 = "arr[5] = 406"
TRAP_19 = "arr[2] = 552"
TRAP_20 = "arr[1] = 971"
TRAP_21 = "arr[4] = 415"
TRAP_22 = "arr[7] = 461"
TRAP_23 = "arr[0] = 135"
TRAP_24 = "arr[8] = 241"
TRAP_25 = "arr[9] = 644"
TRAP_26 = "arr[4] = 384"
TRAP_27 = "arr[9] = 988"
TRAP_28 = "arr[2] = 810"
TRAP_29 = "arr[2] = 593"
TRAP_30 = "arr[2] = 251"
TRAP_31 = "arr[5] = 714"
TRAP_32 = "arr[0] = 265"
TRAP_33 = "arr[0] = 825"
TRAP_34 = "arr[6] = 612"
TRAP_35 = "arr[1] = 385"
TRAP_36 = "arr[3] = 135"
TRAP_37 = "arr[2] = 560"
TRAP_38 = "arr[7] = 898"
TRAP_39 = "arr[5] = 329"
TRAP_40 = "arr[7] = 500"
TRAP_41 = "arr[8] = 789"
TRAP_42 = "arr[4] = 883"
TRAP_43 = "arr[2] = 176"
TRAP_44 = "arr[5] = 337"
TRAP_45 = "arr[6] = 276"
TRAP_46 = "arr[5] = 818"
TRAP_47 = "arr[8] = 876"
TRAP_48 = "arr[2] = 510"
TRAP_49 = "arr[1] = 714"
TRAP_50 = "arr[4] = 887"
TRAP_51 = "arr[0] = 425"
TRAP_52 = "arr[6] = 951"
TRAP_53 = "arr[7] = 453"
TRAP_54 = "arr[1] = 631"
TRAP_55 = "arr[2] = 307"
TRAP_56 = "arr[1] = 347"
TRAP_57 = "arr[3] = 948"
TRAP_58 = "arr[6] = 757"
TRAP_59 = "arr[8] = 229"
TRAP_60 = "arr[9] = 128"
TRAP_61 = "arr[7] = 635"
TRAP_62 = "arr[0] = 316"
TRAP_63 = "arr[2] = 307"
TRAP_64 = "arr[7] = 573"
TRAP_65 = "arr[6] = 414"
TRAP_66 = "arr[6] = 829"
TRAP_67 = "arr[4] = 514"
TRAP_68 = "arr[9] = 563"
TRAP_69 = "arr[2] = 849"
TRAP_70 = "arr[3] = 960"
TRAP_71 = "arr[7] = 281"
TRAP_72 = "arr[4] = 975"
TRAP_73 = "arr[3] = 583"
TRAP_74 = "arr[2] = 763"
TRAP_75 = "arr[1] = 429"
TRAP_76 = "arr[0] = 784"
TRAP_77 = "arr[7] = 680"
TRAP_78 = "arr[3] = 355"
TRAP_79 = "arr[8] = 472"
TRAP_80 = "arr[6] = 957"
TRAP_81 = "arr[9] = 144"
TRAP_82 = "arr[2] = 166"
TRAP_83 = "arr[5] = 243"
TRAP_84 = "arr[5] = 738"
TRAP_85 = "arr[6] = 194"
TRAP_86 = "arr[7] = 501"
TRAP_87 = "arr[1] = 522"
TRAP_88 = "arr[3] = 170"
TRAP_89 = "arr[3] = 649"
TRAP_90 = "arr[1] = 803"
TRAP_91 = "arr[6] = 194"
TRAP_92 = "arr[4] = 736"
TRAP_93 = "arr[9] = 536"
TRAP_94 = "arr[5] = 986"
TRAP_95 = "arr[3] = 485"
TRAP_96 = "arr[5] = 316"
TRAP_97 = "arr[4] = 504"
TRAP_98 = "arr[9] = 660"
TRAP_99 = "arr[4] = 386"
TRAP_100 = "arr[3] = 102"
TRAP_101 = "arr[3] = 303"
TRAP_102 = "arr[3] = 829"
TRAP_103 = "arr[6] = 724"
TRAP_104 = "arr[7] = 238"
TRAP_105 = "arr[7] = 502"
TRAP_106 = "arr[9] = 796"
TRAP_107 = "arr[2] = 976"
TRAP_108 = "arr[1] = 273"
TRAP_109 = "arr[4] = 294"
TRAP_110 = "arr[0] = 261"
TRAP_111 = "arr[8] = 227"
TRAP_112 = "arr[2] = 368"
TRAP_113 = "arr[2] = 282"
TRAP_114 = "arr[4] = 432"
TRAP_115 = "arr[0] = 582"
TRAP_116 = "arr[7] = 806"
TRAP_117 = "arr[2] = 990"
TRAP_118 = "arr[4] = 720"
TRAP_119 = "arr[6] = 852"
TRAP_120 = "arr[2] = 635"
TRAP_121 = "arr[5] = 877"
TRAP_122 = "arr[6] = 805"
TRAP_123 = "arr[7] = 171"
TRAP_124 = "arr[4] = 718"
TRAP_125 = "arr[5] = 334"
TRAP_126 = "arr[7] = 941"
TRAP_127 = "arr[8] = 300"
TRAP_128 = "arr[7] = 954"
TRAP_129 = "arr[5] = 366"
TRAP_130 = "arr[5] = 964"
TRAP_131 = "arr[8] = 291"
TRAP_132 = "arr[8] = 850"
TRAP_133 = "arr[4] = 969"
TRAP_134 = "arr[9] = 778"
TRAP_135 = "arr[7] = 985"
TRAP_136 = "arr[7] = 639"
TRAP_137 = "arr[1] = 525"
TRAP_138 = "arr[4] = 140"
TRAP_139 = "arr[5] = 882"
TRAP_140 = "arr[2] = 557"
TRAP_141 = "arr[8] = 197"
TRAP_142 = "arr[4] = 830"
TRAP_143 = "arr[0] = 891"
TRAP_144 = "arr[6] = 787"
TRAP_145 = "arr[7] = 783"
TRAP_146 = "arr[4] = 336"
TRAP_147 = "arr[0] = 609"
TRAP_148 = "arr[0] = 971"
TRAP_149 = "arr[2] = 769"

arr = [6, 19, 19, 13, 21, 22, 10, 17, 6, 23]

tmp_0 = arr[4] + 33
label_1 = "запись 1 не применялась"
code_2 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_3 = arr[2]
tmp_4 = arr[4] + 15
tmp_5 = arr[1] + 46
note_6 = str(arr[4]) + str(arr[5])
note_7 = str(arr[7]) + str(arr[4])
tmp_8 = arr[6] + 26
tmp_9 = arr[1] + 22
copy_10 = arr[9]
tmp_11 = arr[8] + 26
copy_12 = arr[8]
tmp_13 = arr[4] + 47
label_14 = "запись 14 не применялась"
note_15 = str(arr[4]) + str(arr[1])
note_16 = str(arr[4]) + str(arr[1])
tmp_17 = arr[4] + 29
note_18 = str(arr[1]) + str(arr[1])
tmp_19 = arr[6] + 9
copy_20 = arr[4]
tmp_21 = arr[2] + 9
label_22 = "запись 22 не применялась"
note_23 = str(arr[8]) + str(arr[7])
tmp_24 = arr[1] + 40
code_25 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_26 = arr[5] + 40
note_27 = str(arr[9]) + str(arr[5])
note_28 = str(arr[2]) + str(arr[8])
tmp_29 = arr[6] + 19
tmp_30 = arr[0] + 27
code_31 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_32 = arr[3] + 12
copy_33 = arr[5]
tmp_34 = arr[3] + 29
copy_35 = arr[0]
code_36 = re.sub(r'[0-9]', '#', str(arr[3]))
note_37 = str(arr[3]) + str(arr[0])
code_38 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_39 = arr[7]
note_40 = str(arr[2]) + str(arr[0])
note_41 = str(arr[2]) + str(arr[0])
tmp_42 = arr[9] + 36
tmp_43 = arr[3] + 49
tmp_44 = arr[9] + 43
tmp_45 = arr[4] + 38
tmp_46 = arr[3] + 42
note_47 = str(arr[0]) + str(arr[3])
label_48 = "запись 48 не применялась"
note_49 = str(arr[0]) + str(arr[1])
tmp_50 = arr[1] + 29
copy_51 = arr[2]
tmp_52 = arr[9] + 18
label_53 = "запись 53 не применялась"
tmp_54 = arr[6] + 39
tmp_55 = arr[6] + 8
tmp_56 = arr[9] + 35
label_57 = "запись 57 не применялась"
code_58 = re.sub(r'[0-9]', '#', str(arr[4]))
note_59 = str(arr[9]) + str(arr[8])
copy_60 = arr[8]
code_61 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_62 = arr[1]
tmp_63 = arr[2] + 46
tmp_64 = arr[0] + 45
note_65 = str(arr[2]) + str(arr[8])
note_66 = str(arr[2]) + str(arr[5])
note_67 = str(arr[2]) + str(arr[7])
note_68 = str(arr[7]) + str(arr[1])
label_69 = "запись 69 не применялась"
tmp_70 = arr[7] + 12
note_71 = str(arr[5]) + str(arr[4])
note_72 = str(arr[8]) + str(arr[7])
note_73 = str(arr[2]) + str(arr[1])
label_74 = "запись 74 не применялась"
tmp_75 = arr[5] + 27
note_76 = str(arr[6]) + str(arr[2])
copy_77 = arr[8]
tmp_78 = arr[2] + 15
copy_79 = arr[6]
copy_80 = arr[2]
label_81 = "запись 81 не применялась"
note_82 = str(arr[0]) + str(arr[6])
tmp_83 = arr[9] + 49
note_84 = str(arr[8]) + str(arr[6])
note_85 = str(arr[4]) + str(arr[9])
tmp_86 = arr[8] + 24
note_87 = str(arr[8]) + str(arr[0])
code_88 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_89 = arr[1] + 38
copy_90 = arr[3]
label_91 = "запись 91 не применялась"
tmp_92 = arr[3] + 49
copy_93 = arr[3]
code_94 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_95 = arr[4]
code_96 = re.sub(r'[0-9]', '#', str(arr[4]))
code_97 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_98 = arr[5] + 49
copy_99 = arr[9]
copy_100 = arr[7]
copy_101 = arr[1]
note_102 = str(arr[1]) + str(arr[1])
label_103 = "запись 103 не применялась"
note_104 = str(arr[4]) + str(arr[4])
copy_105 = arr[8]
code_106 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_107 = arr[4]
label_108 = "запись 108 не применялась"
copy_109 = arr[5]
note_110 = str(arr[8]) + str(arr[7])
label_111 = "запись 111 не применялась"
tmp_112 = arr[9] + 31
label_113 = "запись 113 не применялась"
note_114 = str(arr[4]) + str(arr[8])
label_115 = "запись 115 не применялась"
copy_116 = arr[7]
code_117 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_118 = arr[4] + 36
note_119 = str(arr[6]) + str(arr[6])
label_120 = "запись 120 не применялась"
copy_121 = arr[4]
note_122 = str(arr[3]) + str(arr[1])
label_123 = "запись 123 не применялась"
tmp_124 = arr[2] + 49
note_125 = str(arr[4]) + str(arr[7])
note_126 = str(arr[6]) + str(arr[9])
code_127 = re.sub(r'[0-9]', '#', str(arr[2]))
note_128 = str(arr[4]) + str(arr[7])
tmp_129 = arr[8] + 34
code_130 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_131 = arr[8]
note_132 = str(arr[7]) + str(arr[1])
note_133 = str(arr[6]) + str(arr[1])
code_134 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_135 = arr[4]
copy_136 = arr[0]
code_137 = re.sub(r'[0-9]', '#', str(arr[6]))
code_138 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_139 = arr[7] + 23
note_140 = str(arr[9]) + str(arr[8])
note_141 = str(arr[3]) + str(arr[7])
tmp_142 = arr[2] + 42
label_143 = "запись 143 не применялась"
tmp_144 = arr[6] + 13
tmp_145 = arr[4] + 24
note_146 = str(arr[9]) + str(arr[0])
code_147 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_148 = arr[6]
tmp_149 = arr[2] + 16
copy_150 = arr[8]
copy_151 = arr[0]
tmp_152 = arr[2] + 43
note_153 = str(arr[7]) + str(arr[2])
label_154 = "запись 154 не применялась"
code_155 = re.sub(r'[0-9]', '#', str(arr[8]))
code_156 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_157 = arr[1] + 34
copy_158 = arr[1]
copy_159 = arr[4]
code_160 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_161 = arr[7] + 24
tmp_162 = arr[4] + 2
tmp_163 = arr[9] + 10
label_164 = "запись 164 не применялась"
tmp_165 = arr[8] + 48
tmp_166 = arr[5] + 30
note_167 = str(arr[7]) + str(arr[1])
code_168 = re.sub(r'[0-9]', '#', str(arr[0]))
note_169 = str(arr[5]) + str(arr[4])
note_170 = str(arr[1]) + str(arr[5])
note_171 = str(arr[8]) + str(arr[3])
note_172 = str(arr[4]) + str(arr[5])
tmp_173 = arr[0] + 10
tmp_174 = arr[9] + 18
copy_175 = arr[2]
copy_176 = arr[6]
copy_177 = arr[2]
code_178 = re.sub(r'[0-9]', '#', str(arr[4]))
note_179 = str(arr[9]) + str(arr[2])
code_180 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_181 = arr[9]
code_182 = re.sub(r'[0-9]', '#', str(arr[5]))
note_183 = str(arr[3]) + str(arr[7])
tmp_184 = arr[5] + 17
tmp_185 = arr[3] + 48
code_186 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_187 = arr[7]
tmp_188 = arr[6] + 23
tmp_189 = arr[3] + 21
tmp_190 = arr[1] + 38
note_191 = str(arr[4]) + str(arr[4])
copy_192 = arr[3]
note_193 = str(arr[3]) + str(arr[3])
note_194 = str(arr[1]) + str(arr[6])
note_195 = str(arr[8]) + str(arr[0])
code_196 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_197 = arr[0] + 23
note_198 = str(arr[6]) + str(arr[3])
copy_199 = arr[2]
tmp_200 = arr[0] + 44
copy_201 = arr[2]
copy_202 = arr[3]
code_203 = re.sub(r'[0-9]', '#', str(arr[1]))
code_204 = re.sub(r'[0-9]', '#', str(arr[3]))
code_205 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_206 = arr[1] + 50
tmp_207 = arr[9] + 39
copy_208 = arr[2]
copy_209 = arr[5]
copy_210 = arr[7]
copy_211 = arr[7]
tmp_212 = arr[3] + 22
code_213 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_214 = arr[0] + 30
copy_215 = arr[3]
tmp_216 = arr[9] + 40
label_217 = "запись 217 не применялась"
code_218 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_219 = arr[1] + 50
code_220 = re.sub(r'[0-9]', '#', str(arr[3]))
note_221 = str(arr[3]) + str(arr[3])
tmp_222 = arr[0] + 9
tmp_223 = arr[0] + 12
note_224 = str(arr[4]) + str(arr[1])
tmp_225 = arr[7] + 11
code_226 = re.sub(r'[0-9]', '#', str(arr[2]))
note_227 = str(arr[1]) + str(arr[8])
tmp_228 = arr[7] + 25
code_229 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_230 = arr[1]
copy_231 = arr[1]
code_232 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_233 = arr[7] + 32
code_234 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_235 = arr[5]
code_236 = re.sub(r'[0-9]', '#', str(arr[5]))
note_237 = str(arr[2]) + str(arr[5])
code_238 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_239 = arr[1]
code_240 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_241 = arr[6] + 36
note_242 = str(arr[2]) + str(arr[3])
copy_243 = arr[8]
note_244 = str(arr[7]) + str(arr[2])
tmp_245 = arr[5] + 5
label_246 = "запись 246 не применялась"
tmp_247 = arr[5] + 19
note_248 = str(arr[2]) + str(arr[2])
note_249 = str(arr[8]) + str(arr[6])
copy_250 = arr[9]
tmp_251 = arr[5] + 23
tmp_252 = arr[3] + 38
note_253 = str(arr[7]) + str(arr[0])
tmp_254 = arr[6] + 21
tmp_255 = arr[8] + 20
code_256 = re.sub(r'[0-9]', '#', str(arr[3]))
label_257 = "запись 257 не применялась"
label_258 = "запись 258 не применялась"
label_259 = "запись 259 не применялась"
tmp_260 = arr[7] + 21
copy_261 = arr[3]
tmp_262 = arr[6] + 33
copy_263 = arr[6]
code_264 = re.sub(r'[0-9]', '#', str(arr[4]))
code_265 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_266 = arr[3]
note_267 = str(arr[1]) + str(arr[0])
note_268 = str(arr[1]) + str(arr[2])
tmp_269 = arr[8] + 12
code_270 = re.sub(r'[0-9]', '#', str(arr[5]))
note_271 = str(arr[1]) + str(arr[7])
tmp_272 = arr[3] + 43
code_273 = re.sub(r'[0-9]', '#', str(arr[0]))
note_274 = str(arr[5]) + str(arr[2])
tmp_275 = arr[5] + 10
tmp_276 = arr[7] + 30
tmp_277 = arr[3] + 22
tmp_278 = arr[9] + 35
label_279 = "запись 279 не применялась"
note_280 = str(arr[4]) + str(arr[2])
note_281 = str(arr[7]) + str(arr[0])
copy_282 = arr[6]
label_283 = "запись 283 не применялась"
note_284 = str(arr[2]) + str(arr[6])
note_285 = str(arr[0]) + str(arr[4])
tmp_286 = arr[9] + 48
copy_287 = arr[4]
tmp_288 = arr[2] + 37
code_289 = re.sub(r'[0-9]', '#', str(arr[8]))
note_290 = str(arr[8]) + str(arr[7])
code_291 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_292 = arr[7]
note_293 = str(arr[6]) + str(arr[1])
label_294 = "запись 294 не применялась"
copy_295 = arr[2]
tmp_296 = arr[9] + 50
code_297 = re.sub(r'[0-9]', '#', str(arr[1]))
note_298 = str(arr[6]) + str(arr[6])
code_299 = re.sub(r'[0-9]', '#', str(arr[4]))
code_300 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_301 = arr[0] + 17
tmp_302 = arr[3] + 37
note_303 = str(arr[6]) + str(arr[1])
tmp_304 = arr[4] + 5
code_305 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_306 = arr[5]
copy_307 = arr[6]
copy_308 = arr[4]
code_309 = re.sub(r'[0-9]', '#', str(arr[5]))
code_310 = re.sub(r'[0-9]', '#', str(arr[3]))
label_311 = "запись 311 не применялась"
tmp_312 = arr[0] + 40
note_313 = str(arr[2]) + str(arr[2])
code_314 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_315 = arr[7]
note_316 = str(arr[4]) + str(arr[9])
label_317 = "запись 317 не применялась"
label_318 = "запись 318 не применялась"
tmp_319 = arr[6] + 1
tmp_320 = arr[3] + 32
copy_321 = arr[0]
label_322 = "запись 322 не применялась"
copy_323 = arr[9]
note_324 = str(arr[2]) + str(arr[7])
code_325 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_326 = arr[5] + 7
tmp_327 = arr[4] + 7
note_328 = str(arr[5]) + str(arr[2])
tmp_329 = arr[0] + 48
note_330 = str(arr[3]) + str(arr[9])
tmp_331 = arr[3] + 11
code_332 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_333 = arr[7] + 50
code_334 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_335 = arr[4] + 48
tmp_336 = arr[6] + 33
copy_337 = arr[8]
copy_338 = arr[8]
tmp_339 = arr[9] + 44
copy_340 = arr[7]
label_341 = "запись 341 не применялась"
note_342 = str(arr[2]) + str(arr[9])
tmp_343 = arr[5] + 34
code_344 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_345 = arr[0] + 41
tmp_346 = arr[2] + 17
tmp_347 = arr[3] + 31
note_348 = str(arr[7]) + str(arr[4])
code_349 = re.sub(r'[0-9]', '#', str(arr[2]))
note_350 = str(arr[8]) + str(arr[4])
copy_351 = arr[3]
tmp_352 = arr[5] + 21
copy_353 = arr[5]
code_354 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_355 = arr[2] + 33
label_356 = "запись 356 не применялась"
tmp_357 = arr[7] + 31
tmp_358 = arr[4] + 6
tmp_359 = arr[7] + 24
copy_360 = arr[3]
note_361 = str(arr[3]) + str(arr[9])
tmp_362 = arr[9] + 39
note_363 = str(arr[1]) + str(arr[0])
copy_364 = arr[3]
note_365 = str(arr[5]) + str(arr[3])
label_366 = "запись 366 не применялась"
code_367 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_368 = arr[2]
tmp_369 = arr[6] + 35
tmp_370 = arr[8] + 23
label_371 = "запись 371 не применялась"
code_372 = re.sub(r'[0-9]', '#', str(arr[0]))
code_373 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_374 = arr[6] + 40
label_375 = "запись 375 не применялась"
code_376 = re.sub(r'[0-9]', '#', str(arr[4]))
note_377 = str(arr[4]) + str(arr[2])
note_378 = str(arr[1]) + str(arr[6])
copy_379 = arr[5]
tmp_380 = arr[0] + 47
tmp_381 = arr[4] + 2
note_382 = str(arr[4]) + str(arr[8])
tmp_383 = arr[3] + 11
tmp_384 = arr[7] + 26
tmp_385 = arr[5] + 30
note_386 = str(arr[5]) + str(arr[8])
tmp_387 = arr[9] + 8
label_388 = "запись 388 не применялась"
code_389 = re.sub(r'[0-9]', '#', str(arr[4]))
code_390 = re.sub(r'[0-9]', '#', str(arr[9]))
code_391 = re.sub(r'[0-9]', '#', str(arr[1]))
note_392 = str(arr[8]) + str(arr[0])
tmp_393 = arr[7] + 46
copy_394 = arr[6]
code_395 = re.sub(r'[0-9]', '#', str(arr[0]))
note_396 = str(arr[9]) + str(arr[1])
note_397 = str(arr[1]) + str(arr[2])
code_398 = re.sub(r'[0-9]', '#', str(arr[9]))
note_399 = str(arr[6]) + str(arr[7])
tmp_400 = arr[0] + 41
tmp_401 = arr[3] + 7
note_402 = str(arr[5]) + str(arr[2])
tmp_403 = arr[6] + 15
note_404 = str(arr[8]) + str(arr[2])
copy_405 = arr[4]
label_406 = "запись 406 не применялась"
tmp_407 = arr[4] + 44
copy_408 = arr[2]
code_409 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_410 = arr[7] + 29
code_411 = re.sub(r'[0-9]', '#', str(arr[2]))
note_412 = str(arr[5]) + str(arr[6])
code_413 = re.sub(r'[0-9]', '#', str(arr[5]))
code_414 = re.sub(r'[0-9]', '#', str(arr[7]))
code_415 = re.sub(r'[0-9]', '#', str(arr[1]))
note_416 = str(arr[3]) + str(arr[9])
tmp_417 = arr[0] + 49
note_418 = str(arr[3]) + str(arr[3])
note_419 = str(arr[0]) + str(arr[2])
code_420 = re.sub(r'[0-9]', '#', str(arr[0]))
code_421 = re.sub(r'[0-9]', '#', str(arr[6]))
code_422 = re.sub(r'[0-9]', '#', str(arr[9]))
label_423 = "запись 423 не применялась"
tmp_424 = arr[3] + 9
tmp_425 = arr[6] + 5
code_426 = re.sub(r'[0-9]', '#', str(arr[5]))
label_427 = "запись 427 не применялась"
tmp_428 = arr[2] + 43
copy_429 = arr[0]
copy_430 = arr[5]
note_431 = str(arr[6]) + str(arr[7])
tmp_432 = arr[1] + 38
label_433 = "запись 433 не применялась"
label_434 = "запись 434 не применялась"
code_435 = re.sub(r'[0-9]', '#', str(arr[1]))
code_436 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_437 = arr[2] + 6
copy_438 = arr[3]
tmp_439 = arr[2] + 1
tmp_440 = arr[1] + 17
tmp_441 = arr[8] + 31
label_442 = "запись 442 не применялась"
label_443 = "запись 443 не применялась"
note_444 = str(arr[1]) + str(arr[7])
code_445 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_446 = arr[5]
code_447 = re.sub(r'[0-9]', '#', str(arr[6]))
note_448 = str(arr[6]) + str(arr[1])
code_449 = re.sub(r'[0-9]', '#', str(arr[9]))
note_450 = str(arr[5]) + str(arr[8])
note_451 = str(arr[0]) + str(arr[0])
note_452 = str(arr[0]) + str(arr[3])
code_453 = re.sub(r'[0-9]', '#', str(arr[5]))
code_454 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_455 = arr[1] + 8
copy_456 = arr[3]
code_457 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_458 = arr[2] + 47
tmp_459 = arr[1] + 13
code_460 = re.sub(r'[0-9]', '#', str(arr[6]))
label_461 = "запись 461 не применялась"
note_462 = str(arr[6]) + str(arr[8])
code_463 = re.sub(r'[0-9]', '#', str(arr[5]))
note_464 = str(arr[9]) + str(arr[2])
note_465 = str(arr[5]) + str(arr[7])
note_466 = str(arr[9]) + str(arr[8])
tmp_467 = arr[5] + 18
code_468 = re.sub(r'[0-9]', '#', str(arr[3]))
note_469 = str(arr[3]) + str(arr[9])
label_470 = "запись 470 не применялась"
tmp_471 = arr[6] + 23
code_472 = re.sub(r'[0-9]', '#', str(arr[9]))
note_473 = str(arr[6]) + str(arr[0])
note_474 = str(arr[9]) + str(arr[5])
note_475 = str(arr[4]) + str(arr[4])
tmp_476 = arr[9] + 6
label_477 = "запись 477 не применялась"
code_478 = re.sub(r'[0-9]', '#', str(arr[6]))
label_479 = "запись 479 не применялась"
tmp_480 = arr[0] + 36
code_481 = re.sub(r'[0-9]', '#', str(arr[0]))
code_482 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_483 = arr[6] + 12
copy_484 = arr[8]
note_485 = str(arr[7]) + str(arr[8])
tmp_486 = arr[3] + 47
note_487 = str(arr[9]) + str(arr[4])
code_488 = re.sub(r'[0-9]', '#', str(arr[1]))
code_489 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_490 = arr[1] + 37
code_491 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_492 = arr[6] + 18
tmp_493 = arr[1] + 6
tmp_494 = arr[2] + 47
code_495 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_496 = arr[2]
copy_497 = arr[1]
tmp_498 = arr[7] + 44
tmp_499 = arr[2] + 46
tmp_500 = arr[7] + 44
note_501 = str(arr[1]) + str(arr[0])
tmp_502 = arr[5] + 27
note_503 = str(arr[5]) + str(arr[0])
code_504 = re.sub(r'[0-9]', '#', str(arr[9]))
note_505 = str(arr[4]) + str(arr[6])
note_506 = str(arr[0]) + str(arr[8])
note_507 = str(arr[6]) + str(arr[4])
copy_508 = arr[2]
copy_509 = arr[9]
tmp_510 = arr[9] + 10
label_511 = "запись 511 не применялась"
code_512 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_513 = arr[3]
tmp_514 = arr[3] + 9
note_515 = str(arr[5]) + str(arr[5])
tmp_516 = arr[2] + 36
copy_517 = arr[7]
tmp_518 = arr[4] + 49
tmp_519 = arr[2] + 40
copy_520 = arr[7]
tmp_521 = arr[0] + 23
copy_522 = arr[6]
note_523 = str(arr[7]) + str(arr[2])
note_524 = str(arr[7]) + str(arr[7])
code_525 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_526 = arr[0] + 23
code_527 = re.sub(r'[0-9]', '#', str(arr[8]))
label_528 = "запись 528 не применялась"
tmp_529 = arr[1] + 11
label_530 = "запись 530 не применялась"
code_531 = re.sub(r'[0-9]', '#', str(arr[8]))
code_532 = re.sub(r'[0-9]', '#', str(arr[9]))
note_533 = str(arr[2]) + str(arr[8])
copy_534 = arr[0]
note_535 = str(arr[5]) + str(arr[3])
tmp_536 = arr[6] + 18
tmp_537 = arr[3] + 20
label_538 = "запись 538 не применялась"
tmp_539 = arr[5] + 10
note_540 = str(arr[2]) + str(arr[0])
note_541 = str(arr[1]) + str(arr[5])
code_542 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_543 = arr[8] + 1
code_544 = re.sub(r'[0-9]', '#', str(arr[4]))
note_545 = str(arr[1]) + str(arr[5])
tmp_546 = arr[0] + 12
note_547 = str(arr[0]) + str(arr[9])
tmp_548 = arr[0] + 36
note_549 = str(arr[4]) + str(arr[6])
tmp_550 = arr[0] + 6
label_551 = "запись 551 не применялась"
tmp_552 = arr[1] + 25
note_553 = str(arr[7]) + str(arr[1])
copy_554 = arr[6]
label_555 = "запись 555 не применялась"
note_556 = str(arr[7]) + str(arr[6])
tmp_557 = arr[4] + 36
note_558 = str(arr[2]) + str(arr[7])
note_559 = str(arr[7]) + str(arr[4])
copy_560 = arr[0]
label_561 = "запись 561 не применялась"
tmp_562 = arr[7] + 30
label_563 = "запись 563 не применялась"
copy_564 = arr[4]
tmp_565 = arr[9] + 12
note_566 = str(arr[9]) + str(arr[9])
note_567 = str(arr[1]) + str(arr[0])
note_568 = str(arr[4]) + str(arr[9])
note_569 = str(arr[8]) + str(arr[6])
tmp_570 = arr[9] + 6
copy_571 = arr[6]
note_572 = str(arr[2]) + str(arr[7])
note_573 = str(arr[7]) + str(arr[6])
tmp_574 = arr[9] + 16
tmp_575 = arr[6] + 25
code_576 = re.sub(r'[0-9]', '#', str(arr[9]))
code_577 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_578 = arr[6]
tmp_579 = arr[6] + 5
tmp_580 = arr[4] + 20
label_581 = "запись 581 не применялась"
label_582 = "запись 582 не применялась"
label_583 = "запись 583 не применялась"
copy_584 = arr[0]
note_585 = str(arr[2]) + str(arr[0])
note_586 = str(arr[0]) + str(arr[6])
tmp_587 = arr[1] + 2
tmp_588 = arr[1] + 44
code_589 = re.sub(r'[0-9]', '#', str(arr[6]))
label_590 = "запись 590 не применялась"
copy_591 = arr[7]
copy_592 = arr[6]
tmp_593 = arr[4] + 34
label_594 = "запись 594 не применялась"
tmp_595 = arr[3] + 29
code_596 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_597 = arr[2]
note_598 = str(arr[4]) + str(arr[1])
copy_599 = arr[3]
tmp_600 = arr[6] + 1
tmp_601 = arr[5] + 38
code_602 = re.sub(r'[0-9]', '#', str(arr[5]))
label_603 = "запись 603 не применялась"
copy_604 = arr[5]
tmp_605 = arr[0] + 3
note_606 = str(arr[6]) + str(arr[6])
tmp_607 = arr[1] + 27
label_608 = "запись 608 не применялась"
copy_609 = arr[0]
code_610 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_611 = arr[1] + 16
tmp_612 = arr[8] + 19
code_613 = re.sub(r'[0-9]', '#', str(arr[1]))
code_614 = re.sub(r'[0-9]', '#', str(arr[8]))
note_615 = str(arr[3]) + str(arr[4])
tmp_616 = arr[2] + 18
copy_617 = arr[6]
code_618 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_619 = arr[6] + 17
code_620 = re.sub(r'[0-9]', '#', str(arr[0]))
code_621 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_622 = arr[1] + 46
label_623 = "запись 623 не применялась"
label_624 = "запись 624 не применялась"
tmp_625 = arr[0] + 8
tmp_626 = arr[4] + 14
tmp_627 = arr[0] + 3
tmp_628 = arr[9] + 39
tmp_629 = arr[5] + 40
note_630 = str(arr[1]) + str(arr[9])
tmp_631 = arr[9] + 41
code_632 = re.sub(r'[0-9]', '#', str(arr[6]))
note_633 = str(arr[4]) + str(arr[8])
note_634 = str(arr[8]) + str(arr[1])
tmp_635 = arr[9] + 9
tmp_636 = arr[7] + 5
code_637 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_638 = arr[2] + 15
tmp_639 = arr[9] + 10
note_640 = str(arr[8]) + str(arr[2])
note_641 = str(arr[6]) + str(arr[4])
tmp_642 = arr[5] + 11
tmp_643 = arr[1] + 24
tmp_644 = arr[9] + 30
label_645 = "запись 645 не применялась"
tmp_646 = arr[2] + 19
tmp_647 = arr[6] + 14
tmp_648 = arr[8] + 17
note_649 = str(arr[4]) + str(arr[2])
code_650 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_651 = arr[3] + 22
tmp_652 = arr[0] + 27
code_653 = re.sub(r'[0-9]', '#', str(arr[0]))
code_654 = re.sub(r'[0-9]', '#', str(arr[8]))
label_655 = "запись 655 не применялась"
code_656 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_657 = arr[5]
tmp_658 = arr[1] + 4
tmp_659 = arr[8] + 44
tmp_660 = arr[0] + 43
tmp_661 = arr[7] + 23
copy_662 = arr[6]
copy_663 = arr[9]
copy_664 = arr[9]
tmp_665 = arr[4] + 9
note_666 = str(arr[0]) + str(arr[7])
code_667 = re.sub(r'[0-9]', '#', str(arr[0]))
note_668 = str(arr[7]) + str(arr[2])
tmp_669 = arr[6] + 9
note_670 = str(arr[8]) + str(arr[6])
copy_671 = arr[1]
tmp_672 = arr[8] + 10
tmp_673 = arr[3] + 47
code_674 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_675 = arr[0] + 12
code_676 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_677 = arr[9] + 9
label_678 = "запись 678 не применялась"
code_679 = re.sub(r'[0-9]', '#', str(arr[7]))
note_680 = str(arr[4]) + str(arr[3])
note_681 = str(arr[6]) + str(arr[0])
tmp_682 = arr[3] + 12
code_683 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_684 = arr[4]
tmp_685 = arr[2] + 28
tmp_686 = arr[7] + 21
tmp_687 = arr[2] + 6
tmp_688 = arr[1] + 49
label_689 = "запись 689 не применялась"
copy_690 = arr[9]
copy_691 = arr[1]
code_692 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_693 = arr[9]
code_694 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_695 = arr[3] + 32
note_696 = str(arr[0]) + str(arr[7])
tmp_697 = arr[6] + 9
label_698 = "запись 698 не применялась"
tmp_699 = arr[5] + 25
tmp_700 = arr[7] + 3
label_701 = "запись 701 не применялась"
code_702 = re.sub(r'[0-9]', '#', str(arr[6]))
note_703 = str(arr[8]) + str(arr[2])
copy_704 = arr[0]
note_705 = str(arr[8]) + str(arr[5])
code_706 = re.sub(r'[0-9]', '#', str(arr[8]))
note_707 = str(arr[0]) + str(arr[7])
tmp_708 = arr[7] + 1
code_709 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_710 = arr[1] + 7
copy_711 = arr[4]
note_712 = str(arr[0]) + str(arr[6])
note_713 = str(arr[1]) + str(arr[1])
copy_714 = arr[4]
label_715 = "запись 715 не применялась"
copy_716 = arr[9]
tmp_717 = arr[7] + 40
code_718 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_719 = arr[3]
copy_720 = arr[0]
note_721 = str(arr[6]) + str(arr[3])
tmp_722 = arr[3] + 30
code_723 = re.sub(r'[0-9]', '#', str(arr[7]))
note_724 = str(arr[8]) + str(arr[8])
note_725 = str(arr[1]) + str(arr[4])
code_726 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_727 = arr[8] + 3
tmp_728 = arr[2] + 15
copy_729 = arr[4]
tmp_730 = arr[0] + 4
code_731 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_732 = arr[2] + 18
note_733 = str(arr[0]) + str(arr[2])
code_734 = re.sub(r'[0-9]', '#', str(arr[7]))
code_735 = re.sub(r'[0-9]', '#', str(arr[8]))
code_736 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_737 = arr[0]
copy_738 = arr[8]
copy_739 = arr[4]
note_740 = str(arr[0]) + str(arr[8])
code_741 = re.sub(r'[0-9]', '#', str(arr[6]))
code_742 = re.sub(r'[0-9]', '#', str(arr[0]))
code_743 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_744 = arr[2]
tmp_745 = arr[7] + 1
tmp_746 = arr[7] + 13
code_747 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_748 = arr[1] + 12
label_749 = "запись 749 не применялась"
code_750 = re.sub(r'[0-9]', '#', str(arr[9]))
code_751 = re.sub(r'[0-9]', '#', str(arr[8]))
note_752 = str(arr[0]) + str(arr[8])
code_753 = re.sub(r'[0-9]', '#', str(arr[7]))
code_754 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_755 = arr[7] + 21
tmp_756 = arr[6] + 3
tmp_757 = arr[9] + 13
copy_758 = arr[3]
label_759 = "запись 759 не применялась"
note_760 = str(arr[6]) + str(arr[9])
tmp_761 = arr[6] + 29
note_762 = str(arr[5]) + str(arr[0])
note_763 = str(arr[9]) + str(arr[3])
tmp_764 = arr[7] + 25
tmp_765 = arr[6] + 46
note_766 = str(arr[8]) + str(arr[3])
tmp_767 = arr[3] + 46
copy_768 = arr[7]
tmp_769 = arr[9] + 26
tmp_770 = arr[5] + 3
tmp_771 = arr[9] + 21
note_772 = str(arr[3]) + str(arr[8])
label_773 = "запись 773 не применялась"
note_774 = str(arr[6]) + str(arr[6])
tmp_775 = arr[5] + 7
label_776 = "запись 776 не применялась"
note_777 = str(arr[2]) + str(arr[4])
code_778 = re.sub(r'[0-9]', '#', str(arr[5]))
code_779 = re.sub(r'[0-9]', '#', str(arr[1]))
note_780 = str(arr[5]) + str(arr[7])
label_781 = "запись 781 не применялась"
note_782 = str(arr[0]) + str(arr[1])
note_783 = str(arr[0]) + str(arr[9])
tmp_784 = arr[7] + 37
tmp_785 = arr[8] + 26
copy_786 = arr[5]
note_787 = str(arr[8]) + str(arr[7])
code_788 = re.sub(r'[0-9]', '#', str(arr[3]))
label_789 = "запись 789 не применялась"
note_790 = str(arr[9]) + str(arr[4])
note_791 = str(arr[9]) + str(arr[1])
code_792 = re.sub(r'[0-9]', '#', str(arr[6]))
note_793 = str(arr[7]) + str(arr[6])
copy_794 = arr[0]
tmp_795 = arr[3] + 1
code_796 = re.sub(r'[0-9]', '#', str(arr[5]))
note_797 = str(arr[0]) + str(arr[6])
copy_798 = arr[2]
note_799 = str(arr[2]) + str(arr[0])

t692 = str(arr[6]) + str(arr[0])
# пометка: запись 906 обработана, изменений нет
# архив: запись 634 обработана, изменений нет
# черновик: arr2[7] = 88 — не выполняется
# черновик: arr[6] += 48 — не выполняется
# временная запись: запись 787 обработана, изменений нет
# справка: запись 303 обработана, изменений нет
# отладка: arr[5] += 97 — не выполняется
# справка: запись 870 обработана, изменений нет
# архив: запись 169 обработана, изменений нет
# архив: запись 730 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 828 обработана, изменений нет
# проверено: arr[7] *= 40 — не выполняется
# проверено: запись 576 обработана, изменений нет
# временная запись: arr[7] = 60 — не выполняется
# ревизия: arr2[4] = 94 — не выполняется
# примечание: запись 11 обработана, изменений нет
# временная запись: arr[6] = 99 — не выполняется
# ревизия: arr[3] += 3 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 414 обработана, изменений нет
# справка: запись 599 обработана, изменений нет
# черновик: arr[2] *= 35 — не выполняется
# отладка: запись 25 обработана, изменений нет
# проверено: запись 237 обработана, изменений нет
# черновик: arr[6] = 11 — не выполняется
# временная запись: arr[8] = 31 — не выполняется
# отладка: запись 252 обработана, изменений нет
# черновик: arr[9] *= 74 — не выполняется
# отладка: запись 433 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# замечание: запись 813 обработана, изменений нет
# пометка: arr[1] = 75 — не выполняется
# черновик: запись 797 обработана, изменений нет
# проверено: запись 227 обработана, изменений нет
# ревизия: arr[3] *= 66 — не выполняется
# черновик: arr2[7] = 31 — не выполняется
# справка: запись 802 обработана, изменений нет
# пометка: запись 57 обработана, изменений нет
# пометка: запись 822 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr2[5] = 41 — не выполняется
# пометка: запись 854 обработана, изменений нет
# проверено: запись 682 обработана, изменений нет
# отладка: arr[6] += 8 — не выполняется
# проверено: запись 728 обработана, изменений нет
# примечание: запись 696 обработана, изменений нет
# черновик: arr2[7] = 74 — не выполняется
# ревизия: arr[9] *= 16 — не выполняется
# временная запись: запись 513 обработана, изменений нет
# черновик: запись 651 обработана, изменений нет
# отладка: arr2[2] = 94 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# ревизия: arr[2] = 57 — не выполняется
# примечание: запись 296 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# отладка: arr[3] = 67 — не выполняется
# отладка: запись 623 обработана, изменений нет
# архив: arr[1] = 27 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[3] *= 4 — не выполняется
# проверено: запись 90 обработана, изменений нет
# примечание: запись 291 обработана, изменений нет
# отладка: запись 985 обработана, изменений нет
# примечание: arr[1] = 68 — не выполняется
# проверено: запись 797 обработана, изменений нет
# примечание: запись 133 обработана, изменений нет
# ревизия: запись 536 обработана, изменений нет
# пометка: arr[0] *= 44 — не выполняется
# временная запись: запись 804 обработана, изменений нет
# временная запись: arr[8] += 9 — не выполняется
# пометка: запись 359 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 386 обработана, изменений нет
# примечание: arr[6] *= 94 — не выполняется
# пометка: arr2[9] = 83 — не выполняется
# отладка: arr[4] = 46 — не выполняется
# примечание: arr2[4] = 75 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 353 обработана, изменений нет
# замечание: arr[1] += 30 — не выполняется
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 566 обработана, изменений нет
# проверено: arr2[6] = 87 — не выполняется
# замечание: запись 839 обработана, изменений нет
# примечание: arr[4] = 66 — не выполняется
# временная запись: запись 516 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[2] = 87 — не выполняется
# проверено: arr2[1] = 63 — не выполняется
# проверено: arr[5] *= 66 — не выполняется
# черновик: arr[7] = 69 — не выполняется
# примечание: arr2[2] = 42 — не выполняется
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[0] *= 29 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: запись 745 обработана, изменений нет
# справка: запись 187 обработана, изменений нет
# ревизия: arr2[7] = 14 — не выполняется
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr[6] *= 73 — не выполняется
# ревизия: arr2[4] = 54 — не выполняется
# временная запись: arr[4] *= 75 — не выполняется
# замечание: запись 669 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# черновик: arr[7] *= 92 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# проверено: arr[3] = 87 — не выполняется
# временная запись: arr2[2] = 30 — не выполняется
# примечание: arr[3] += 99 — не выполняется
# проверено: arr[3] += 35 — не выполняется
# архив: запись 305 обработана, изменений нет
# проверено: запись 352 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# справка: arr[5] = 74 — не выполняется
# временная запись: запись 382 обработана, изменений нет
# черновик: запись 501 обработана, изменений нет
# пометка: arr[8] *= 83 — не выполняется
# примечание: arr[2] = 44 — не выполняется
# замечание: запись 518 обработана, изменений нет
# черновик: arr[6] = 7 — не выполняется
# проверено: arr2[7] = 79 — не выполняется
# ревизия: arr2[6] = 88 — не выполняется
# примечание: запись 122 обработана, изменений нет
# замечание: arr[7] *= 79 — не выполняется
# замечание: запись 38 обработана, изменений нет
# отладка: arr[7] *= 77 — не выполняется
# замечание: запись 729 обработана, изменений нет
# черновик: arr[1] *= 45 — не выполняется
# справка: запись 341 обработана, изменений нет
# замечание: запись 551 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: запись 682 обработана, изменений нет
# отладка: запись 836 обработана, изменений нет
# примечание: запись 826 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 521 обработана, изменений нет
# временная запись: arr[1] = 12 — не выполняется
# отладка: arr[6] = 2 — не выполняется
# архив: запись 751 обработана, изменений нет
# примечание: arr2[2] = 66 — не выполняется
# пометка: arr2[7] = 15 — не выполняется
# черновик: запись 706 обработана, изменений нет
# проверено: запись 566 обработана, изменений нет
# черновик: запись 276 обработана, изменений нет
# отладка: arr[5] *= 26 — не выполняется
# пометка: arr[3] *= 93 — не выполняется
# замечание: arr[1] *= 61 — не выполняется
# проверено: arr[0] += 4 — не выполняется
# архив: arr2[2] = 82 — не выполняется
# архив: arr2[0] = 61 — не выполняется
# временная запись: запись 338 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# отладка: запись 722 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# справка: запись 827 обработана, изменений нет
# проверено: запись 443 обработана, изменений нет
# пометка: запись 799 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# отладка: запись 297 обработана, изменений нет
# замечание: arr[4] += 56 — не выполняется
# черновик: запись 226 обработана, изменений нет
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[9] *= 69 — не выполняется
# ревизия: arr2[6] = 26 — не выполняется
# пометка: запись 338 обработана, изменений нет
# примечание: arr[2] += 44 — не выполняется
# примечание: запись 383 обработана, изменений нет
# временная запись: arr[9] = 23 — не выполняется
# временная запись: запись 689 обработана, изменений нет
# временная запись: arr2[7] = 68 — не выполняется
# временная запись: arr2[9] = 91 — не выполняется
# проверено: arr[8] += 44 — не выполняется
# ревизия: запись 183 обработана, изменений нет
# справка: запись 916 обработана, изменений нет
# замечание: запись 816 обработана, изменений нет
# пометка: arr2[0] = 16 — не выполняется
# пометка: arr[9] += 78 — не выполняется
# замечание: arr[4] += 80 — не выполняется
# черновик: запись 774 обработана, изменений нет
# отладка: arr2[2] = 99 — не выполняется
# ревизия: запись 334 обработана, изменений нет
# проверено: arr[4] += 24 — не выполняется
# архив: arr[3] = 72 — не выполняется
# замечание: arr[5] *= 76 — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[5] = 34 — не выполняется
# черновик: arr[8] *= 68 — не выполняется
# черновик: запись 611 обработана, изменений нет
# временная запись: запись 729 обработана, изменений нет
# черновик: arr[5] = 84 — не выполняется
# примечание: запись 289 обработана, изменений нет
# ревизия: запись 919 обработана, изменений нет
# замечание: arr[6] += 3 — не выполняется
# примечание: запись 950 обработана, изменений нет
# замечание: запись 944 обработана, изменений нет
# ревизия: arr[2] += 11 — не выполняется
# временная запись: запись 372 обработана, изменений нет
# пометка: запись 913 обработана, изменений нет
# отладка: запись 372 обработана, изменений нет
# отладка: arr[1] = 67 — не выполняется
# примечание: arr[5] = 83 — не выполняется
# архив: arr[8] *= 17 — не выполняется
# пометка: запись 524 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 631 обработана, изменений нет
# архив: запись 542 обработана, изменений нет
# примечание: arr[7] += 67 — не выполняется
# замечание: arr[8] = 40 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 404 обработана, изменений нет
# ревизия: запись 599 обработана, изменений нет
# справка: запись 338 обработана, изменений нет
# черновик: arr2[9] = 55 — не выполняется
# справка: arr[6] *= 5 — не выполняется
# пометка: запись 537 обработана, изменений нет
# замечание: arr[5] = 14 — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 615 обработана, изменений нет
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: arr[8] *= 97 — не выполняется
# черновик: запись 270 обработана, изменений нет
# пометка: запись 47 обработана, изменений нет
# архив: arr[5] *= 25 — не выполняется
# справка: arr2[4] = 43 — не выполняется
# пометка: запись 435 обработана, изменений нет
# пометка: запись 870 обработана, изменений нет
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 15 обработана, изменений нет
# примечание: arr[7] *= 87 — не выполняется
# справка: запись 137 обработана, изменений нет
# справка: arr2[9] = 96 — не выполняется
# временная запись: arr[1] *= 51 — не выполняется
# справка: запись 349 обработана, изменений нет
# ревизия: arr[1] += 77 — не выполняется
# отладка: запись 958 обработана, изменений нет
# примечание: запись 332 обработана, изменений нет
# примечание: arr[4] = 94 — не выполняется
# отладка: запись 856 обработана, изменений нет
# замечание: запись 896 обработана, изменений нет
# черновик: запись 976 обработана, изменений нет
# архив: запись 678 обработана, изменений нет
# временная запись: запись 397 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[7] += 67 — не выполняется
# проверено: запись 85 обработана, изменений нет
# архив: arr[2] = 30 — не выполняется
# отладка: arr[4] += 15 — не выполняется
# примечание: arr[6] += 57 — не выполняется
# проверено: arr[5] *= 81 — не выполняется
# черновик: arr2[3] = 45 — не выполняется
# отладка: запись 775 обработана, изменений нет
# архив: запись 538 обработана, изменений нет
# ревизия: arr[3] += 38 — не выполняется
# замечание: запись 224 обработана, изменений нет
# отладка: arr[8] *= 79 — не выполняется
# проверено: arr[6] = 2 — не выполняется
# пометка: запись 110 обработана, изменений нет
# примечание: arr[9] += 62 — не выполняется
# черновик: запись 292 обработана, изменений нет
# архив: запись 178 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[4] += 84 — не выполняется
# ревизия: arr2[9] = 71 — не выполняется
# отладка: запись 409 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr2[2] = 94 — не выполняется
# черновик: запись 20 обработана, изменений нет
# черновик: arr[9] += 89 — не выполняется
# временная запись: запись 49 обработана, изменений нет
# архив: запись 43 обработана, изменений нет
# временная запись: запись 226 обработана, изменений нет
# архив: запись 417 обработана, изменений нет
# черновик: arr[9] = 67 — не выполняется
# архив: запись 869 обработана, изменений нет
# справка: запись 977 обработана, изменений нет
# ревизия: запись 620 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 664 обработана, изменений нет
# замечание: arr2[6] = 43 — не выполняется
# ревизия: запись 132 обработана, изменений нет
# архив: запись 552 обработана, изменений нет
# пометка: запись 424 обработана, изменений нет
# пометка: запись 148 обработана, изменений нет
# пометка: запись 715 обработана, изменений нет
# замечание: arr2[6] = 18 — не выполняется
# временная запись: arr[6] *= 89 — не выполняется
# проверено: запись 520 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
arr[4] = int(t692) % 97
# пометка: запись 908 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
# архив: arr2[5] = 40 — не выполняется
# примечание: запись 481 обработана, изменений нет
# отладка: запись 9 обработана, изменений нет
# пометка: arr2[5] = 10 — не выполняется
# примечание: запись 990 обработана, изменений нет
# архив: запись 137 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# временная запись: запись 978 обработана, изменений нет
# отладка: arr[4] += 84 — не выполняется
# отладка: запись 146 обработана, изменений нет
# пометка: запись 183 обработана, изменений нет
# черновик: запись 97 обработана, изменений нет
# отладка: запись 149 обработана, изменений нет
# пометка: запись 391 обработана, изменений нет
# проверено: запись 743 обработана, изменений нет
# отладка: arr[8] = 5 — не выполняется
# примечание: arr2[6] = 59 — не выполняется
# ревизия: arr[2] += 11 — не выполняется
# черновик: запись 103 обработана, изменений нет
# архив: arr[7] = 65 — не выполняется
# архив: arr[5] = 31 — не выполняется
# отладка: arr[9] += 28 — не выполняется
# черновик: запись 766 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# черновик: запись 787 обработана, изменений нет
# черновик: запись 635 обработана, изменений нет
# пометка: arr[5] *= 36 — не выполняется
# черновик: запись 45 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[2] *= 18 — не выполняется
# справка: запись 846 обработана, изменений нет
# отладка: запись 38 обработана, изменений нет
# справка: arr[1] += 16 — не выполняется
# черновик: запись 129 обработана, изменений нет
# ревизия: запись 871 обработана, изменений нет
# замечание: arr[6] = 56 — не выполняется
# пометка: запись 478 обработана, изменений нет
# временная запись: arr[2] *= 64 — не выполняется
# замечание: arr[3] = 72 — не выполняется
# ревизия: запись 807 обработана, изменений нет
# справка: arr[5] += 79 — не выполняется
# проверено: запись 229 обработана, изменений нет
# замечание: запись 502 обработана, изменений нет
# архив: запись 696 обработана, изменений нет
# пометка: arr[5] = 46 — не выполняется
# проверено: запись 942 обработана, изменений нет
# справка: запись 64 обработана, изменений нет
# черновик: arr[4] += 1 — не выполняется
# справка: arr2[4] = 43 — не выполняется
# проверено: arr[9] += 14 — не выполняется
# пометка: запись 498 обработана, изменений нет
# примечание: arr[8] *= 70 — не выполняется
# отладка: arr[0] += 42 — не выполняется
# замечание: запись 710 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# замечание: запись 127 обработана, изменений нет
# отладка: запись 86 обработана, изменений нет
# пометка: arr[2] *= 32 — не выполняется
# черновик: запись 552 обработана, изменений нет
# примечание: запись 586 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# пометка: запись 799 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 287 обработана, изменений нет
# архив: запись 661 обработана, изменений нет
# архив: запись 330 обработана, изменений нет
# замечание: arr2[5] = 67 — не выполняется
# черновик: запись 348 обработана, изменений нет
# справка: arr[4] += 62 — не выполняется
# отладка: arr2[2] = 86 — не выполняется
# черновик: запись 200 обработана, изменений нет
# архив: запись 194 обработана, изменений нет
# замечание: запись 887 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# справка: запись 872 обработана, изменений нет
# справка: arr[9] += 18 — не выполняется
# временная запись: arr[5] += 3 — не выполняется
# пометка: запись 447 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: arr[5] += 50 — не выполняется
# замечание: запись 479 обработана, изменений нет
# примечание: arr[7] *= 31 — не выполняется
# пометка: запись 249 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# замечание: arr2[1] = 29 — не выполняется
# справка: запись 179 обработана, изменений нет
# архив: arr2[1] = 70 — не выполняется
# временная запись: запись 489 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# примечание: arr[9] *= 95 — не выполняется
# примечание: запись 867 обработана, изменений нет
# черновик: arr[2] = 78 — не выполняется
# отладка: запись 210 обработана, изменений нет
# черновик: arr2[8] = 1 — не выполняется
# примечание: arr[8] *= 70 — не выполняется
# примечание: запись 558 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# справка: запись 131 обработана, изменений нет
# архив: arr[5] = 47 — не выполняется
# замечание: запись 561 обработана, изменений нет
# ревизия: запись 945 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[5] = 99 — не выполняется
# отладка: arr2[1] = 33 — не выполняется
# черновик: arr2[6] = 1 — не выполняется
# отладка: запись 718 обработана, изменений нет
# архив: запись 461 обработана, изменений нет
# архив: запись 294 обработана, изменений нет
# черновик: запись 163 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[9] *= 47 — не выполняется
# ревизия: запись 268 обработана, изменений нет
# пометка: arr[6] *= 16 — не выполняется
# пометка: запись 307 обработана, изменений нет
# черновик: запись 962 обработана, изменений нет
# пометка: arr[4] *= 9 — не выполняется
# ревизия: запись 530 обработана, изменений нет
# замечание: arr[7] = 23 — не выполняется
# примечание: arr[7] *= 46 — не выполняется
# отладка: запись 437 обработана, изменений нет
# архив: запись 277 обработана, изменений нет
# примечание: arr[5] = 35 — не выполняется
# архив: запись 577 обработана, изменений нет
# архив: запись 78 обработана, изменений нет
# проверено: arr2[3] = 10 — не выполняется
# временная запись: запись 807 обработана, изменений нет
# примечание: arr[2] = 17 — не выполняется
# черновик: arr[9] *= 84 — не выполняется
# временная запись: arr[3] *= 24 — не выполняется
# временная запись: arr[5] += 49 — не выполняется
# отладка: запись 471 обработана, изменений нет
# примечание: запись 294 обработана, изменений нет
# пометка: запись 819 обработана, изменений нет
# черновик: arr[2] = 13 — не выполняется
# справка: arr[2] += 5 — не выполняется
# черновик: запись 62 обработана, изменений нет
# примечание: arr2[2] = 60 — не выполняется
# отладка: arr[1] *= 17 — не выполняется
# временная запись: запись 360 обработана, изменений нет
# проверено: arr[4] += 63 — не выполняется
# справка: arr[5] += 58 — не выполняется
# черновик: arr[7] *= 45 — не выполняется
# примечание: запись 901 обработана, изменений нет
# проверено: arr2[4] = 2 — не выполняется
# проверено: arr[4] *= 73 — не выполняется
# отладка: arr[0] = 65 — не выполняется
# ревизия: запись 338 обработана, изменений нет
# проверено: запись 699 обработана, изменений нет
# проверено: запись 648 обработана, изменений нет
# примечание: запись 297 обработана, изменений нет
# справка: arr[9] *= 1 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# черновик: arr[8] += 38 — не выполняется
# отладка: arr[4] = 88 — не выполняется
# отладка: arr[8] += 21 — не выполняется
# ревизия: запись 478 обработана, изменений нет
# ревизия: запись 127 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# пометка: запись 701 обработана, изменений нет
# пометка: запись 856 обработана, изменений нет
# архив: arr2[2] = 44 — не выполняется
# примечание: arr[8] = 67 — не выполняется
# архив: arr[7] *= 33 — не выполняется
# ревизия: запись 61 обработана, изменений нет
# отладка: запись 788 обработана, изменений нет
# замечание: arr[9] *= 23 — не выполняется
# примечание: arr[7] = 19 — не выполняется
# ревизия: arr[4] *= 34 — не выполняется
# черновик: запись 521 обработана, изменений нет
# ревизия: arr[7] = 11 — не выполняется
# черновик: arr2[0] = 91 — не выполняется
# черновик: запись 462 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# замечание: arr[0] += 29 — не выполняется
# пометка: arr2[2] = 56 — не выполняется
# пометка: arr2[8] = 46 — не выполняется
# черновик: arr[2] *= 15 — не выполняется
# замечание: arr[7] = 41 — не выполняется
# замечание: запись 733 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr2[0] = 18 — не выполняется
# справка: arr[6] = 26 — не выполняется
# проверено: arr2[6] = 7 — не выполняется
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: запись 197 обработана, изменений нет
# ревизия: запись 535 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 762 обработана, изменений нет
# пометка: запись 59 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 25 обработана, изменений нет
# ревизия: arr[6] += 47 — не выполняется
# ревизия: arr[7] *= 58 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr2[2] = 1 — не выполняется
# временная запись: arr[9] *= 4 — не выполняется
# отладка: запись 270 обработана, изменений нет
# пометка: запись 120 обработана, изменений нет
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 523 обработана, изменений нет
# ревизия: arr2[5] = 72 — не выполняется
# справка: arr[0] += 14 — не выполняется
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[7] *= 70 — не выполняется
# примечание: запись 695 обработана, изменений нет
# черновик: arr2[3] = 98 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 997 обработана, изменений нет
# проверено: запись 141 обработана, изменений нет
# черновик: запись 527 обработана, изменений нет
# ревизия: запись 956 обработана, изменений нет
# временная запись: запись 130 обработана, изменений нет
# замечание: arr[7] *= 76 — не выполняется
# отладка: запись 653 обработана, изменений нет
# отладка: запись 775 обработана, изменений нет
# временная запись: запись 918 обработана, изменений нет
# архив: arr[9] += 69 — не выполняется
# справка: запись 900 обработана, изменений нет
# отладка: arr[7] += 30 — не выполняется
# черновик: arr[0] = 83 — не выполняется
# черновик: запись 484 обработана, изменений нет
# замечание: arr[6] += 56 — не выполняется
# справка: запись 102 обработана, изменений нет
# архив: запись 930 обработана, изменений нет
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 155 обработана, изменений нет
# замечание: запись 785 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 497 обработана, изменений нет
# примечание: arr[7] = 95 — не выполняется
# справка: запись 544 обработана, изменений нет
# справка: запись 807 обработана, изменений нет
# пометка: arr[2] *= 85 — не выполняется
# примечание: arr[6] = 35 — не выполняется
# временная запись: запись 564 обработана, изменений нет
# замечание: запись 159 обработана, изменений нет
# проверено: запись 447 обработана, изменений нет
# примечание: запись 83 обработана, изменений нет
# черновик: arr[2] = 49 — не выполняется
# справка: arr[8] *= 27 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# проверено: запись 435 обработана, изменений нет
# примечание: arr[4] *= 37 — не выполняется
# архив: arr[0] *= 87 — не выполняется
# пометка: arr[5] = 95 — не выполняется
# черновик: запись 670 обработана, изменений нет
# примечание: запись 147 обработана, изменений нет
# замечание: запись 267 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr2[8] = 93 — не выполняется
# черновик: запись 840 обработана, изменений нет
# справка: запись 867 обработана, изменений нет
# ревизия: arr[6] += 44 — не выполняется
# примечание: запись 922 обработана, изменений нет
# проверено: arr2[9] = 23 — не выполняется
# пометка: запись 738 обработана, изменений нет
# справка: arr[3] += 79 — не выполняется
# временная запись: запись 860 обработана, изменений нет
# замечание: запись 588 обработана, изменений нет
# отладка: arr2[0] = 27 — не выполняется
# примечание: запись 48 обработана, изменений нет
# замечание: arr[2] *= 40 — не выполняется
# справка: запись 877 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# архив: arr[6] *= 2 — не выполняется
# черновик: запись 390 обработана, изменений нет
# временная запись: запись 269 обработана, изменений нет
# временная запись: запись 38 обработана, изменений нет
# черновик: запись 223 обработана, изменений нет
# черновик: arr[1] = 57 — не выполняется
# пометка: arr[6] += 56 — не выполняется
# архив: запись 762 обработана, изменений нет
# проверено: запись 920 обработана, изменений нет
# архив: запись 984 обработана, изменений нет
# отладка: запись 534 обработана, изменений нет
# пометка: запись 302 обработана, изменений нет
# справка: запись 47 обработана, изменений нет
# примечание: запись 853 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr[7] += 26 — не выполняется
# проверено: arr[2] = 74 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 107 обработана, изменений нет
arr[8] -= 1
# замечание: arr[0] += 39 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 595 обработана, изменений нет
# пометка: arr[9] *= 24 — не выполняется
# архив: запись 670 обработана, изменений нет
# временная запись: arr[0] += 51 — не выполняется
# примечание: запись 404 обработана, изменений нет
# отладка: запись 186 обработана, изменений нет
# пометка: запись 778 обработана, изменений нет
# пометка: arr[2] *= 46 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 105 обработана, изменений нет
# временная запись: arr[4] = 45 — не выполняется
# справка: arr[3] *= 40 — не выполняется
# проверено: arr[0] = 89 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# архив: arr[7] *= 54 — не выполняется
# замечание: arr2[7] = 15 — не выполняется
# примечание: arr[6] = 99 — не выполняется
# примечание: запись 505 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# пометка: arr[9] = 55 — не выполняется
# черновик: запись 368 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# архив: arr2[3] = 81 — не выполняется
# замечание: arr2[3] = 20 — не выполняется
# ревизия: запись 967 обработана, изменений нет
# архив: arr[9] *= 99 — не выполняется
# справка: arr2[5] = 97 — не выполняется
# отладка: arr[1] += 12 — не выполняется
# черновик: arr[8] = 53 — не выполняется
# справка: запись 150 обработана, изменений нет
# справка: запись 953 обработана, изменений нет
# временная запись: arr[8] += 38 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 571 обработана, изменений нет
# ревизия: запись 752 обработана, изменений нет
# примечание: arr[6] = 13 — не выполняется
# проверено: arr[2] *= 64 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 615 обработана, изменений нет
# отладка: запись 308 обработана, изменений нет
# отладка: запись 685 обработана, изменений нет
# черновик: запись 518 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# отладка: запись 59 обработана, изменений нет
# замечание: arr2[3] = 98 — не выполняется
# отладка: arr[0] = 93 — не выполняется
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: arr[0] += 71 — не выполняется
# проверено: arr[4] = 60 — не выполняется
# черновик: запись 375 обработана, изменений нет
# замечание: запись 838 обработана, изменений нет
# отладка: запись 214 обработана, изменений нет
# ревизия: arr2[5] = 46 — не выполняется
# архив: arr[4] = 87 — не выполняется
# черновик: запись 773 обработана, изменений нет
# ревизия: arr[9] += 18 — не выполняется
# проверено: arr2[3] = 59 — не выполняется
# пометка: arr[9] = 50 — не выполняется
# архив: arr[0] = 31 — не выполняется
# примечание: arr[0] += 2 — не выполняется
# замечание: запись 981 обработана, изменений нет
# справка: запись 374 обработана, изменений нет
# архив: arr[2] += 2 — не выполняется
# временная запись: запись 825 обработана, изменений нет
# справка: arr2[4] = 93 — не выполняется
# пометка: запись 513 обработана, изменений нет
# замечание: arr[8] *= 86 — не выполняется
# пометка: arr2[1] = 7 — не выполняется
# проверено: запись 752 обработана, изменений нет
# архив: запись 361 обработана, изменений нет
# справка: запись 464 обработана, изменений нет
# отладка: arr2[9] = 58 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: запись 175 обработана, изменений нет
# отладка: запись 649 обработана, изменений нет
# временная запись: запись 513 обработана, изменений нет
# временная запись: запись 553 обработана, изменений нет
# ревизия: запись 107 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# пометка: запись 389 обработана, изменений нет
# ревизия: запись 18 обработана, изменений нет
# справка: запись 538 обработана, изменений нет
# ревизия: arr[6] += 50 — не выполняется
# замечание: arr[2] = 91 — не выполняется
# временная запись: arr[1] = 13 — не выполняется
# пометка: запись 864 обработана, изменений нет
# справка: arr2[1] = 13 — не выполняется
# замечание: arr[8] = 19 — не выполняется
# проверено: arr[0] *= 46 — не выполняется
# черновик: запись 804 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr[8] = 39 — не выполняется
# отладка: arr[7] = 47 — не выполняется
# отладка: arr[7] += 25 — не выполняется
# замечание: arr[4] *= 66 — не выполняется
# справка: arr[7] += 84 — не выполняется
# замечание: запись 894 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# примечание: запись 749 обработана, изменений нет
# ревизия: arr2[4] = 63 — не выполняется
# проверено: запись 408 обработана, изменений нет
# архив: запись 290 обработана, изменений нет
# ревизия: запись 885 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# проверено: arr[8] *= 83 — не выполняется
# замечание: arr[9] += 67 — не выполняется
# пометка: запись 691 обработана, изменений нет
# ревизия: arr2[3] = 91 — не выполняется
# пометка: запись 91 обработана, изменений нет
# замечание: arr[2] += 89 — не выполняется
# пометка: запись 420 обработана, изменений нет
# черновик: arr2[3] = 82 — не выполняется
# замечание: arr[6] = 55 — не выполняется
# проверено: запись 739 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# справка: arr[3] *= 41 — не выполняется
# справка: запись 619 обработана, изменений нет
# пометка: запись 363 обработана, изменений нет
# архив: arr[5] += 42 — не выполняется
# ревизия: arr[3] += 75 — не выполняется
# временная запись: arr[9] += 8 — не выполняется
# черновик: запись 912 обработана, изменений нет
# архив: arr[6] = 24 — не выполняется
# черновик: запись 123 обработана, изменений нет
# замечание: запись 716 обработана, изменений нет
# ревизия: arr2[5] = 43 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: arr2[6] = 24 — не выполняется
# пометка: arr[4] *= 70 — не выполняется
# справка: запись 697 обработана, изменений нет
# примечание: arr[3] = 49 — не выполняется
# пометка: arr[5] *= 93 — не выполняется
# проверено: arr[4] = 90 — не выполняется
# справка: arr[6] = 50 — не выполняется
# примечание: arr2[1] = 87 — не выполняется
# отладка: arr2[0] = 71 — не выполняется
# проверено: запись 251 обработана, изменений нет
# примечание: arr2[2] = 99 — не выполняется
# примечание: запись 764 обработана, изменений нет
# ревизия: arr[9] = 91 — не выполняется
# пометка: запись 474 обработана, изменений нет
# пометка: arr[9] = 63 — не выполняется
# архив: запись 675 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# справка: запись 651 обработана, изменений нет
# пометка: запись 522 обработана, изменений нет
# черновик: arr[3] *= 63 — не выполняется
# отладка: arr2[1] = 79 — не выполняется
# справка: arr[8] = 80 — не выполняется
# примечание: запись 897 обработана, изменений нет
# проверено: arr[9] = 48 — не выполняется
# пометка: запись 571 обработана, изменений нет
# проверено: запись 876 обработана, изменений нет
# временная запись: arr[9] += 37 — не выполняется
# отладка: запись 427 обработана, изменений нет
# проверено: запись 18 обработана, изменений нет
# пометка: arr[0] += 41 — не выполняется
# примечание: запись 748 обработана, изменений нет
# ревизия: arr[8] += 39 — не выполняется
# ревизия: arr2[8] = 10 — не выполняется
# справка: запись 444 обработана, изменений нет
# справка: arr[8] += 36 — не выполняется
# архив: arr[0] += 5 — не выполняется
# архив: arr[1] = 47 — не выполняется
# отладка: arr[1] += 53 — не выполняется
# архив: запись 36 обработана, изменений нет
# архив: запись 564 обработана, изменений нет
# черновик: arr2[9] = 51 — не выполняется
# черновик: запись 169 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: запись 724 обработана, изменений нет
# замечание: запись 526 обработана, изменений нет
# ревизия: запись 54 обработана, изменений нет
# отладка: arr[9] *= 67 — не выполняется
# отладка: запись 243 обработана, изменений нет
# пометка: запись 621 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[8] += 37 — не выполняется
# временная запись: запись 256 обработана, изменений нет
# проверено: arr[8] *= 11 — не выполняется
# справка: запись 292 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 299 обработана, изменений нет
# ревизия: запись 115 обработана, изменений нет
# пометка: запись 777 обработана, изменений нет
# проверено: запись 305 обработана, изменений нет
# отладка: arr[8] += 1 — не выполняется
# замечание: arr[6] += 8 — не выполняется
# отладка: arr[8] += 61 — не выполняется
# отладка: arr[8] += 43 — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 296 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# отладка: запись 475 обработана, изменений нет
# временная запись: arr[1] += 30 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr[4] = 96 — не выполняется
# замечание: arr[6] += 35 — не выполняется
# ревизия: запись 131 обработана, изменений нет
# временная запись: arr[4] += 14 — не выполняется
# проверено: запись 48 обработана, изменений нет
# проверено: arr[1] *= 28 — не выполняется
# отладка: запись 457 обработана, изменений нет
# архив: запись 25 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# черновик: arr[3] *= 87 — не выполняется
# черновик: arr[8] += 71 — не выполняется
# примечание: запись 778 обработана, изменений нет
# замечание: arr[4] += 47 — не выполняется
# временная запись: запись 143 обработана, изменений нет
# черновик: запись 253 обработана, изменений нет
# ревизия: arr[1] += 99 — не выполняется
# черновик: arr[4] = 21 — не выполняется
# замечание: arr[8] += 64 — не выполняется
# замечание: arr2[2] = 85 — не выполняется
# примечание: запись 124 обработана, изменений нет
# пометка: arr[2] *= 83 — не выполняется
# временная запись: запись 837 обработана, изменений нет
# черновик: arr[7] *= 41 — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 439 обработана, изменений нет
# ревизия: arr[5] += 59 — не выполняется
# ревизия: arr2[5] = 8 — не выполняется
# ревизия: arr2[3] = 99 — не выполняется
# справка: arr[9] += 52 — не выполняется
# проверено: arr[3] += 68 — не выполняется
# проверено: запись 300 обработана, изменений нет
# справка: запись 122 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# архив: запись 29 обработана, изменений нет
# отладка: arr2[0] = 57 — не выполняется
# черновик: запись 826 обработана, изменений нет
# примечание: запись 53 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# черновик: запись 39 обработана, изменений нет
# замечание: arr[8] = 28 — не выполняется
# справка: запись 391 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# архив: запись 367 обработана, изменений нет
# ревизия: запись 328 обработана, изменений нет
# временная запись: запись 63 обработана, изменений нет
# замечание: arr[4] += 34 — не выполняется
# справка: запись 60 обработана, изменений нет
# примечание: arr[7] += 77 — не выполняется
# черновик: arr[2] *= 4 — не выполняется
# отладка: arr[7] += 36 — не выполняется
# архив: arr[0] += 4 — не выполняется
# справка: arr[0] += 5 — не выполняется
# замечание: arr[9] = 12 — не выполняется
# проверено: запись 673 обработана, изменений нет
# пометка: запись 263 обработана, изменений нет
# ревизия: arr[8] = 60 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[8] += 40 — не выполняется
# черновик: arr2[1] = 49 — не выполняется
# архив: запись 469 обработана, изменений нет
# пометка: arr[5] *= 1 — не выполняется
# замечание: arr[0] = 72 — не выполняется
# справка: arr[7] += 43 — не выполняется
# архив: запись 768 обработана, изменений нет
# ревизия: запись 911 обработана, изменений нет
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 992 обработана, изменений нет
# замечание: запись 362 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# справка: arr[6] = 83 — не выполняется
# временная запись: arr2[9] = 32 — не выполняется
# временная запись: arr[5] += 39 — не выполняется
# архив: запись 196 обработана, изменений нет
# проверено: arr[6] *= 74 — не выполняется
# временная запись: запись 875 обработана, изменений нет
# архив: arr[3] = 89 — не выполняется
# замечание: запись 368 обработана, изменений нет
# черновик: запись 75 обработана, изменений нет
# пометка: запись 410 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# временная запись: запись 170 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# справка: запись 932 обработана, изменений нет
# черновик: запись 451 обработана, изменений нет
# отладка: arr2[7] = 47 — не выполняется
# временная запись: запись 746 обработана, изменений нет
# ревизия: arr[5] += 58 — не выполняется
# замечание: запись 737 обработана, изменений нет
# черновик: запись 781 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# отладка: arr[1] += 69 — не выполняется
# справка: arr2[3] = 70 — не выполняется
# примечание: arr[7] = 4 — не выполняется
# пометка: запись 217 обработана, изменений нет
arr2 = arr
# отладка: запись 448 обработана, изменений нет
# замечание: запись 13 обработана, изменений нет
# черновик: arr[7] *= 85 — не выполняется
# замечание: запись 305 обработана, изменений нет
# временная запись: arr[4] *= 8 — не выполняется
# пометка: arr[9] = 51 — не выполняется
# архив: arr[4] *= 25 — не выполняется
# пометка: arr[0] = 66 — не выполняется
# замечание: arr[6] = 75 — не выполняется
# проверено: arr[4] = 87 — не выполняется
# примечание: arr2[3] = 84 — не выполняется
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[4] += 17 — не выполняется
# проверено: запись 601 обработана, изменений нет
# архив: запись 609 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr2[6] = 42 — не выполняется
# архив: запись 867 обработана, изменений нет
# архив: запись 53 обработана, изменений нет
# архив: arr[9] *= 39 — не выполняется
# пометка: запись 944 обработана, изменений нет
# черновик: arr[3] += 49 — не выполняется
# черновик: arr2[3] = 42 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# черновик: запись 658 обработана, изменений нет
# временная запись: запись 524 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# проверено: запись 138 обработана, изменений нет
# черновик: arr[4] += 89 — не выполняется
# пометка: arr[5] = 3 — не выполняется
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[2] += 8 — не выполняется
# примечание: запись 475 обработана, изменений нет
# черновик: запись 368 обработана, изменений нет
# архив: запись 113 обработана, изменений нет
# пометка: arr[5] += 65 — не выполняется
# ревизия: запись 4 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[1] *= 41 — не выполняется
# ревизия: запись 29 обработана, изменений нет
# справка: запись 280 обработана, изменений нет
# замечание: arr[5] = 46 — не выполняется
# отладка: запись 574 обработана, изменений нет
# примечание: arr[9] *= 66 — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: запись 637 обработана, изменений нет
# архив: запись 917 обработана, изменений нет
# черновик: запись 825 обработана, изменений нет
# временная запись: запись 508 обработана, изменений нет
# замечание: запись 671 обработана, изменений нет
# справка: запись 85 обработана, изменений нет
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[3] += 70 — не выполняется
# примечание: запись 130 обработана, изменений нет
# архив: запись 182 обработана, изменений нет
# пометка: arr2[8] = 19 — не выполняется
# примечание: запись 464 обработана, изменений нет
# ревизия: запись 689 обработана, изменений нет
# временная запись: запись 578 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 399 обработана, изменений нет
# архив: запись 606 обработана, изменений нет
# архив: arr[9] *= 11 — не выполняется
# пометка: arr[5] += 16 — не выполняется
# отладка: запись 304 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 903 обработана, изменений нет
# отладка: запись 502 обработана, изменений нет
# замечание: запись 713 обработана, изменений нет
# черновик: arr2[3] = 20 — не выполняется
# черновик: arr[6] += 69 — не выполняется
# пометка: запись 255 обработана, изменений нет
# проверено: arr[8] += 67 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 250 обработана, изменений нет
# ревизия: arr[6] = 99 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[6] += 21 — не выполняется
# справка: запись 796 обработана, изменений нет
# замечание: arr[3] *= 21 — не выполняется
# справка: запись 584 обработана, изменений нет
# архив: arr[2] = 62 — не выполняется
# замечание: запись 833 обработана, изменений нет
# замечание: запись 516 обработана, изменений нет
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 833 обработана, изменений нет
# отладка: arr[8] += 70 — не выполняется
# ревизия: запись 921 обработана, изменений нет
# пометка: arr2[5] = 87 — не выполняется
# черновик: запись 291 обработана, изменений нет
# справка: arr2[6] = 51 — не выполняется
# временная запись: запись 780 обработана, изменений нет
# проверено: arr[1] += 29 — не выполняется
# пометка: arr[2] = 96 — не выполняется
# черновик: arr[4] = 13 — не выполняется
# отладка: запись 736 обработана, изменений нет
# пометка: запись 842 обработана, изменений нет
# проверено: запись 222 обработана, изменений нет
# черновик: arr2[9] = 47 — не выполняется
# архив: запись 249 обработана, изменений нет
# архив: arr2[2] = 21 — не выполняется
# ревизия: arr[2] += 75 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 962 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# отладка: запись 816 обработана, изменений нет
# архив: запись 693 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 821 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr2[7] = 24 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 557 обработана, изменений нет
# ревизия: arr[6] = 8 — не выполняется
# отладка: запись 163 обработана, изменений нет
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[7] *= 65 — не выполняется
# отладка: arr2[1] = 48 — не выполняется
# архив: arr2[4] = 78 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: запись 233 обработана, изменений нет
# черновик: arr2[8] = 10 — не выполняется
# черновик: запись 930 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# примечание: arr2[6] = 56 — не выполняется
# архив: arr[2] *= 18 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: запись 411 обработана, изменений нет
# черновик: arr[1] = 56 — не выполняется
# проверено: запись 493 обработана, изменений нет
# проверено: запись 85 обработана, изменений нет
# отладка: arr[1] = 29 — не выполняется
# замечание: arr[4] *= 19 — не выполняется
# архив: arr2[0] = 51 — не выполняется
# архив: arr[2] += 41 — не выполняется
# архив: arr2[2] = 38 — не выполняется
# проверено: запись 396 обработана, изменений нет
# справка: arr2[2] = 31 — не выполняется
# замечание: arr[8] = 20 — не выполняется
# пометка: запись 890 обработана, изменений нет
# архив: запись 657 обработана, изменений нет
# временная запись: запись 669 обработана, изменений нет
# временная запись: arr2[5] = 96 — не выполняется
# отладка: запись 606 обработана, изменений нет
# архив: arr[2] *= 52 — не выполняется
# черновик: запись 626 обработана, изменений нет
# примечание: arr[9] += 41 — не выполняется
# архив: запись 134 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# пометка: запись 618 обработана, изменений нет
# справка: arr[0] = 30 — не выполняется
# архив: arr[0] = 7 — не выполняется
# справка: запись 308 обработана, изменений нет
# справка: запись 280 обработана, изменений нет
# черновик: arr[3] += 27 — не выполняется
# проверено: arr[2] *= 52 — не выполняется
# ревизия: arr[3] = 84 — не выполняется
# временная запись: запись 766 обработана, изменений нет
# замечание: запись 726 обработана, изменений нет
# временная запись: запись 862 обработана, изменений нет
# примечание: запись 938 обработана, изменений нет
# справка: запись 882 обработана, изменений нет
# отладка: arr2[3] = 69 — не выполняется
# пометка: запись 250 обработана, изменений нет
# отладка: arr[3] *= 60 — не выполняется
# отладка: arr[9] = 27 — не выполняется
# временная запись: запись 187 обработана, изменений нет
# проверено: запись 386 обработана, изменений нет
# отладка: arr2[7] = 36 — не выполняется
# архив: запись 89 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# ревизия: запись 278 обработана, изменений нет
# черновик: arr[1] *= 28 — не выполняется
# пометка: запись 243 обработана, изменений нет
# справка: запись 113 обработана, изменений нет
# замечание: arr[8] += 17 — не выполняется
# проверено: запись 381 обработана, изменений нет
# проверено: запись 8 обработана, изменений нет
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 399 обработана, изменений нет
# черновик: arr2[8] = 27 — не выполняется
# отладка: arr[6] = 49 — не выполняется
# справка: запись 80 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# пометка: запись 991 обработана, изменений нет
# ревизия: запись 778 обработана, изменений нет
# временная запись: arr[6] = 25 — не выполняется
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr[5] += 70 — не выполняется
# отладка: запись 138 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# примечание: запись 824 обработана, изменений нет
# пометка: запись 782 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 37 обработана, изменений нет
# архив: arr[4] += 1 — не выполняется
# справка: запись 295 обработана, изменений нет
# пометка: arr[7] *= 73 — не выполняется
# ревизия: запись 71 обработана, изменений нет
# примечание: запись 943 обработана, изменений нет
# справка: arr[4] = 73 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 467 обработана, изменений нет
# временная запись: arr2[6] = 39 — не выполняется
# пометка: запись 697 обработана, изменений нет
# примечание: запись 487 обработана, изменений нет
# черновик: arr[8] = 41 — не выполняется
# отладка: запись 268 обработана, изменений нет
# проверено: arr[5] = 41 — не выполняется
# временная запись: arr[4] = 57 — не выполняется
# замечание: arr[9] += 35 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: запись 250 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr[9] += 79 — не выполняется
# архив: arr[2] += 48 — не выполняется
# пометка: запись 914 обработана, изменений нет
# отладка: arr[5] += 6 — не выполняется
# проверено: запись 941 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# примечание: arr[7] = 80 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 759 обработана, изменений нет
# архив: arr[9] = 27 — не выполняется
# ревизия: arr[3] += 3 — не выполняется
# временная запись: arr[7] = 29 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 777 обработана, изменений нет
# отладка: запись 913 обработана, изменений нет
# примечание: arr[4] *= 97 — не выполняется
# черновик: запись 363 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# отладка: arr[9] *= 97 — не выполняется
# примечание: запись 893 обработана, изменений нет
# ревизия: arr2[6] = 63 — не выполняется
# отладка: запись 402 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 6 обработана, изменений нет
# архив: arr[3] = 44 — не выполняется
# проверено: запись 605 обработана, изменений нет
# примечание: arr[7] += 61 — не выполняется
# проверено: запись 605 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# черновик: запись 185 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# примечание: arr2[7] = 54 — не выполняется
# проверено: arr2[5] = 6 — не выполняется
# временная запись: arr[9] = 34 — не выполняется
# замечание: arr[6] += 92 — не выполняется
# черновик: arr2[0] = 69 — не выполняется
# замечание: arr[4] *= 7 — не выполняется
# ревизия: запись 69 обработана, изменений нет
# замечание: arr2[8] = 27 — не выполняется
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: запись 377 обработана, изменений нет
# архив: запись 76 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 999 обработана, изменений нет
# пометка: arr[7] += 87 — не выполняется
# черновик: запись 96 обработана, изменений нет
# пометка: arr[3] += 97 — не выполняется
# пометка: arr[4] += 9 — не выполняется
# замечание: запись 128 обработана, изменений нет
# справка: запись 59 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# архив: запись 314 обработана, изменений нет
# справка: arr[9] *= 40 — не выполняется
# отладка: arr2[8] = 23 — не выполняется
# отладка: запись 501 обработана, изменений нет
# справка: запись 40 обработана, изменений нет
# справка: запись 495 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# архив: arr[4] += 8 — не выполняется
# проверено: arr[6] += 77 — не выполняется
# пометка: запись 779 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[1] *= 78 — не выполняется
# замечание: запись 479 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: arr[7] += 31 — не выполняется
# проверено: запись 396 обработана, изменений нет
# проверено: запись 206 обработана, изменений нет
# справка: запись 842 обработана, изменений нет
# проверено: arr[0] += 52 — не выполняется
# черновик: arr2[0] = 15 — не выполняется
# ревизия: запись 757 обработана, изменений нет
# замечание: arr[3] *= 21 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[9] = 46 — не выполняется
# отладка: запись 886 обработана, изменений нет
# пометка: arr[4] += 12 — не выполняется
# замечание: запись 412 обработана, изменений нет
arr2[7] += 1
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 654 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# примечание: запись 940 обработана, изменений нет
# замечание: arr2[5] = 8 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[1] = 78 — не выполняется
# черновик: запись 424 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 433 обработана, изменений нет
# замечание: arr[5] += 57 — не выполняется
# пометка: запись 762 обработана, изменений нет
# проверено: arr[1] *= 20 — не выполняется
# проверено: запись 957 обработана, изменений нет
# проверено: arr[7] *= 96 — не выполняется
# справка: запись 732 обработана, изменений нет
# справка: arr[4] = 33 — не выполняется
# замечание: arr[6] = 68 — не выполняется
# архив: arr[6] *= 70 — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 893 обработана, изменений нет
# справка: запись 364 обработана, изменений нет
# проверено: arr2[0] = 54 — не выполняется
# временная запись: запись 709 обработана, изменений нет
# справка: запись 765 обработана, изменений нет
# справка: arr[6] = 74 — не выполняется
# справка: arr2[0] = 69 — не выполняется
# отладка: arr[3] *= 50 — не выполняется
# отладка: запись 836 обработана, изменений нет
# пометка: запись 615 обработана, изменений нет
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 152 обработана, изменений нет
# временная запись: запись 922 обработана, изменений нет
# проверено: arr2[3] = 77 — не выполняется
# замечание: запись 711 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: arr[1] += 54 — не выполняется
# временная запись: запись 809 обработана, изменений нет
# ревизия: arr[6] = 41 — не выполняется
# отладка: запись 814 обработана, изменений нет
# пометка: arr[7] *= 99 — не выполняется
# примечание: запись 873 обработана, изменений нет
# архив: запись 540 обработана, изменений нет
# примечание: arr[0] += 61 — не выполняется
# временная запись: arr[3] = 73 — не выполняется
# замечание: arr[4] += 94 — не выполняется
# справка: запись 794 обработана, изменений нет
# замечание: arr[9] = 17 — не выполняется
# отладка: запись 338 обработана, изменений нет
# архив: arr2[8] = 70 — не выполняется
# справка: arr[3] *= 49 — не выполняется
# справка: запись 760 обработана, изменений нет
# отладка: запись 678 обработана, изменений нет
# замечание: arr[1] += 38 — не выполняется
# пометка: arr[3] *= 79 — не выполняется
# черновик: arr[5] += 42 — не выполняется
# справка: запись 513 обработана, изменений нет
# проверено: arr[2] = 61 — не выполняется
# примечание: arr[0] += 33 — не выполняется
# замечание: arr[3] = 10 — не выполняется
# проверено: arr[5] += 61 — не выполняется
# пометка: arr[1] = 1 — не выполняется
# проверено: запись 911 обработана, изменений нет
# временная запись: запись 518 обработана, изменений нет
# отладка: arr[5] = 64 — не выполняется
# отладка: arr[8] += 1 — не выполняется
# пометка: arr2[5] = 95 — не выполняется
# примечание: запись 748 обработана, изменений нет
# проверено: запись 58 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# черновик: arr[5] += 4 — не выполняется
# справка: запись 257 обработана, изменений нет
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: запись 225 обработана, изменений нет
# черновик: arr2[6] = 61 — не выполняется
# пометка: arr2[0] = 63 — не выполняется
# черновик: запись 508 обработана, изменений нет
# проверено: arr2[2] = 88 — не выполняется
# пометка: arr2[7] = 10 — не выполняется
# замечание: запись 384 обработана, изменений нет
# проверено: arr[2] += 64 — не выполняется
# пометка: запись 565 обработана, изменений нет
# справка: запись 973 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[9] *= 34 — не выполняется
# справка: запись 144 обработана, изменений нет
# примечание: arr[9] += 53 — не выполняется
# черновик: запись 610 обработана, изменений нет
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr[1] = 32 — не выполняется
# замечание: arr[3] += 19 — не выполняется
# проверено: arr[1] = 96 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[3] = 1 — не выполняется
# архив: запись 909 обработана, изменений нет
# черновик: запись 661 обработана, изменений нет
# временная запись: arr2[8] = 72 — не выполняется
# черновик: запись 194 обработана, изменений нет
# архив: arr[1] *= 94 — не выполняется
# пометка: arr[7] = 71 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 999 обработана, изменений нет
# замечание: arr[6] *= 41 — не выполняется
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: запись 709 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 816 обработана, изменений нет
# временная запись: arr[6] = 88 — не выполняется
# примечание: arr2[4] = 85 — не выполняется
# справка: запись 880 обработана, изменений нет
# пометка: запись 121 обработана, изменений нет
# временная запись: arr[4] = 32 — не выполняется
# черновик: запись 181 обработана, изменений нет
# архив: arr[5] += 97 — не выполняется
# проверено: запись 196 обработана, изменений нет
# справка: arr[5] *= 55 — не выполняется
# ревизия: запись 823 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# справка: arr[5] += 73 — не выполняется
# справка: arr[0] = 18 — не выполняется
# ревизия: arr[7] *= 67 — не выполняется
# замечание: arr[6] = 57 — не выполняется
# примечание: запись 64 обработана, изменений нет
# проверено: запись 814 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# отладка: arr[3] += 87 — не выполняется
# пометка: запись 482 обработана, изменений нет
# примечание: запись 891 обработана, изменений нет
# примечание: запись 78 обработана, изменений нет
# архив: arr[6] *= 23 — не выполняется
# справка: запись 398 обработана, изменений нет
# примечание: запись 916 обработана, изменений нет
# проверено: arr[3] = 63 — не выполняется
# пометка: запись 201 обработана, изменений нет
# ревизия: запись 823 обработана, изменений нет
# замечание: запись 256 обработана, изменений нет
# справка: запись 246 обработана, изменений нет
# примечание: запись 188 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# архив: запись 314 обработана, изменений нет
# черновик: arr2[0] = 41 — не выполняется
# замечание: запись 890 обработана, изменений нет
# черновик: arr2[2] = 13 — не выполняется
# справка: запись 548 обработана, изменений нет
# примечание: arr[4] = 67 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 892 обработана, изменений нет
# примечание: arr[8] = 72 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr2[4] = 19 — не выполняется
# временная запись: запись 977 обработана, изменений нет
# замечание: запись 947 обработана, изменений нет
# пометка: запись 405 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr[7] *= 58 — не выполняется
# временная запись: запись 602 обработана, изменений нет
# временная запись: запись 865 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr2[3] = 72 — не выполняется
# временная запись: arr[1] *= 70 — не выполняется
# проверено: arr[0] *= 11 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr2[4] = 6 — не выполняется
# справка: запись 934 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# примечание: arr2[4] = 29 — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[0] = 48 — не выполняется
# архив: arr[8] *= 72 — не выполняется
# замечание: arr[8] *= 58 — не выполняется
# ревизия: запись 558 обработана, изменений нет
# замечание: arr[3] = 60 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# справка: запись 122 обработана, изменений нет
# временная запись: arr[7] *= 50 — не выполняется
# проверено: запись 274 обработана, изменений нет
# замечание: запись 511 обработана, изменений нет
# ревизия: запись 784 обработана, изменений нет
# примечание: arr[0] = 14 — не выполняется
# архив: запись 853 обработана, изменений нет
# пометка: arr2[8] = 85 — не выполняется
# отладка: arr[8] = 28 — не выполняется
# замечание: arr2[0] = 66 — не выполняется
# проверено: запись 765 обработана, изменений нет
# примечание: arr[6] += 9 — не выполняется
# замечание: запись 289 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# архив: arr[7] = 61 — не выполняется
# проверено: запись 409 обработана, изменений нет
# отладка: arr2[1] = 53 — не выполняется
# примечание: arr[7] = 60 — не выполняется
# примечание: arr[8] *= 79 — не выполняется
# справка: запись 162 обработана, изменений нет
# примечание: запись 314 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# проверено: запись 691 обработана, изменений нет
# временная запись: запись 882 обработана, изменений нет
# справка: запись 166 обработана, изменений нет
# отладка: arr2[2] = 56 — не выполняется
# временная запись: запись 178 обработана, изменений нет
# архив: запись 636 обработана, изменений нет
# замечание: запись 640 обработана, изменений нет
# отладка: запись 197 обработана, изменений нет
# архив: запись 431 обработана, изменений нет
# временная запись: запись 20 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# примечание: запись 136 обработана, изменений нет
# ревизия: запись 397 обработана, изменений нет
# временная запись: запись 122 обработана, изменений нет
# проверено: arr[9] = 57 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr2[8] = 84 — не выполняется
# архив: запись 573 обработана, изменений нет
# отладка: запись 263 обработана, изменений нет
# черновик: запись 251 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# ревизия: запись 732 обработана, изменений нет
# справка: arr[8] *= 35 — не выполняется
# пометка: arr2[6] = 58 — не выполняется
# примечание: запись 664 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# черновик: запись 18 обработана, изменений нет
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: arr2[2] = 32 — не выполняется
# отладка: запись 879 обработана, изменений нет
# замечание: запись 643 обработана, изменений нет
# примечание: запись 164 обработана, изменений нет
# пометка: arr2[8] = 47 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[8] *= 57 — не выполняется
# черновик: arr[9] *= 22 — не выполняется
# архив: запись 497 обработана, изменений нет
# архив: запись 781 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# замечание: arr[9] += 61 — не выполняется
# справка: запись 188 обработана, изменений нет
# отладка: запись 189 обработана, изменений нет
# временная запись: arr[1] = 98 — не выполняется
# примечание: запись 831 обработана, изменений нет
# справка: arr[2] += 29 — не выполняется
# временная запись: запись 222 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# ревизия: arr[0] += 36 — не выполняется
# замечание: arr[7] += 82 — не выполняется
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 980 обработана, изменений нет
# замечание: запись 136 обработана, изменений нет
# справка: запись 283 обработана, изменений нет
# примечание: arr[8] += 6 — не выполняется
# временная запись: запись 459 обработана, изменений нет
# временная запись: arr2[0] = 6 — не выполняется
# примечание: запись 654 обработана, изменений нет
# примечание: arr[8] = 35 — не выполняется
# временная запись: запись 189 обработана, изменений нет
# примечание: arr2[2] = 44 — не выполняется
# примечание: запись 383 обработана, изменений нет
# примечание: запись 997 обработана, изменений нет
# пометка: запись 294 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# отладка: arr2[8] = 36 — не выполняется
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 367 обработана, изменений нет
# ревизия: arr[8] *= 90 — не выполняется
# черновик: запись 314 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: arr[8] *= 26 — не выполняется
# ревизия: запись 276 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# ревизия: arr[0] += 49 — не выполняется
# пометка: arr[3] *= 9 — не выполняется
# проверено: arr[8] *= 14 — не выполняется
# проверено: arr[8] *= 38 — не выполняется
# ревизия: запись 672 обработана, изменений нет
# пометка: arr[1] = 27 — не выполняется
# справка: запись 97 обработана, изменений нет
# черновик: запись 146 обработана, изменений нет
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: запись 344 обработана, изменений нет
# черновик: arr2[2] = 97 — не выполняется
# черновик: arr[8] = 95 — не выполняется
# временная запись: запись 367 обработана, изменений нет
# ревизия: запись 663 обработана, изменений нет
# отладка: arr2[8] = 23 — не выполняется
# примечание: запись 954 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# отладка: запись 514 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
s356 = ''.join(str(x) for x in arr)
# проверено: запись 658 обработана, изменений нет
# черновик: arr2[5] = 50 — не выполняется
# архив: запись 37 обработана, изменений нет
# замечание: arr[5] = 96 — не выполняется
# черновик: запись 680 обработана, изменений нет
# ревизия: arr2[0] = 90 — не выполняется
# справка: запись 984 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: arr[2] = 41 — не выполняется
# архив: arr2[0] = 12 — не выполняется
# отладка: запись 28 обработана, изменений нет
# отладка: arr[5] += 74 — не выполняется
# ревизия: запись 715 обработана, изменений нет
# ревизия: запись 332 обработана, изменений нет
# примечание: запись 27 обработана, изменений нет
# временная запись: arr[7] = 58 — не выполняется
# архив: arr[8] += 39 — не выполняется
# справка: запись 418 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[6] = 24 — не выполняется
# ревизия: arr2[2] = 48 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# отладка: запись 982 обработана, изменений нет
# справка: arr[6] *= 73 — не выполняется
# пометка: запись 16 обработана, изменений нет
# примечание: arr[8] *= 91 — не выполняется
# пометка: запись 704 обработана, изменений нет
# справка: arr[6] += 21 — не выполняется
# черновик: arr[8] += 50 — не выполняется
# черновик: запись 723 обработана, изменений нет
# временная запись: arr[6] = 26 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 771 обработана, изменений нет
# временная запись: arr[9] *= 34 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 525 обработана, изменений нет
# проверено: arr[0] *= 47 — не выполняется
# ревизия: запись 767 обработана, изменений нет
# примечание: arr[8] *= 28 — не выполняется
# отладка: arr[6] += 14 — не выполняется
# временная запись: arr2[7] = 48 — не выполняется
# примечание: arr2[6] = 57 — не выполняется
# примечание: запись 637 обработана, изменений нет
# черновик: arr[1] = 35 — не выполняется
# ревизия: запись 813 обработана, изменений нет
# черновик: запись 107 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr[0] += 79 — не выполняется
# черновик: запись 56 обработана, изменений нет
# пометка: запись 708 обработана, изменений нет
# справка: arr2[8] = 9 — не выполняется
# ревизия: запись 415 обработана, изменений нет
# справка: запись 449 обработана, изменений нет
# примечание: запись 957 обработана, изменений нет
# пометка: arr2[2] = 33 — не выполняется
# отладка: запись 70 обработана, изменений нет
# замечание: arr[8] += 60 — не выполняется
# временная запись: запись 633 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# справка: запись 931 обработана, изменений нет
# ревизия: запись 192 обработана, изменений нет
# отладка: arr2[5] = 62 — не выполняется
# ревизия: arr[4] += 90 — не выполняется
# пометка: запись 945 обработана, изменений нет
# проверено: запись 939 обработана, изменений нет
# примечание: arr[9] = 91 — не выполняется
# замечание: arr2[7] = 89 — не выполняется
# справка: запись 690 обработана, изменений нет
# проверено: запись 906 обработана, изменений нет
# временная запись: запись 503 обработана, изменений нет
# пометка: arr[2] *= 58 — не выполняется
# пометка: arr2[2] = 2 — не выполняется
# пометка: запись 470 обработана, изменений нет
# справка: запись 939 обработана, изменений нет
# архив: arr2[1] = 98 — не выполняется
# замечание: arr[9] += 40 — не выполняется
# черновик: запись 407 обработана, изменений нет
# замечание: запись 53 обработана, изменений нет
# пометка: arr[3] += 8 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# пометка: запись 789 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 14 обработана, изменений нет
# архив: arr2[3] = 6 — не выполняется
# архив: запись 429 обработана, изменений нет
# замечание: запись 373 обработана, изменений нет
# пометка: arr2[0] = 45 — не выполняется
# временная запись: запись 400 обработана, изменений нет
# проверено: запись 105 обработана, изменений нет
# отладка: запись 76 обработана, изменений нет
# примечание: запись 941 обработана, изменений нет
# черновик: arr2[4] = 20 — не выполняется
# замечание: запись 732 обработана, изменений нет
# временная запись: arr2[2] = 56 — не выполняется
# черновик: запись 422 обработана, изменений нет
# замечание: запись 941 обработана, изменений нет
# примечание: arr[9] = 83 — не выполняется
# примечание: запись 881 обработана, изменений нет
# проверено: arr[8] = 35 — не выполняется
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[5] *= 63 — не выполняется
# пометка: запись 488 обработана, изменений нет
# примечание: arr[6] += 52 — не выполняется
# справка: запись 26 обработана, изменений нет
# черновик: arr2[4] = 51 — не выполняется
# ревизия: arr[5] *= 30 — не выполняется
# архив: запись 692 обработана, изменений нет
# замечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 382 обработана, изменений нет
# черновик: запись 773 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# проверено: arr[7] = 45 — не выполняется
# справка: запись 298 обработана, изменений нет
# примечание: запись 497 обработана, изменений нет
# архив: arr[9] *= 24 — не выполняется
# ревизия: запись 608 обработана, изменений нет
# временная запись: arr[2] += 31 — не выполняется
# ревизия: запись 455 обработана, изменений нет
# ревизия: arr2[6] = 98 — не выполняется
# замечание: запись 500 обработана, изменений нет
# ревизия: arr[7] *= 77 — не выполняется
# черновик: arr2[7] = 1 — не выполняется
# черновик: arr[8] += 74 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: запись 359 обработана, изменений нет
# пометка: arr[5] += 1 — не выполняется
# проверено: запись 410 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# отладка: запись 38 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[0] = 5 — не выполняется
# примечание: запись 532 обработана, изменений нет
# временная запись: запись 951 обработана, изменений нет
# проверено: arr2[8] = 97 — не выполняется
# примечание: arr[0] *= 55 — не выполняется
# справка: запись 812 обработана, изменений нет
# ревизия: запись 235 обработана, изменений нет
# архив: arr2[4] = 52 — не выполняется
# архив: запись 928 обработана, изменений нет
# проверено: запись 661 обработана, изменений нет
# черновик: arr[4] *= 8 — не выполняется
# черновик: arr[0] += 87 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[4] += 83 — не выполняется
# черновик: arr[2] = 4 — не выполняется
# временная запись: запись 772 обработана, изменений нет
# черновик: arr[2] += 47 — не выполняется
# ревизия: запись 338 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: запись 914 обработана, изменений нет
# справка: arr[9] = 5 — не выполняется
# черновик: arr2[4] = 72 — не выполняется
# замечание: запись 664 обработана, изменений нет
# замечание: arr[6] = 75 — не выполняется
# временная запись: запись 848 обработана, изменений нет
# примечание: запись 81 обработана, изменений нет
# примечание: запись 828 обработана, изменений нет
# примечание: arr[8] += 68 — не выполняется
# отладка: arr[1] += 76 — не выполняется
# примечание: запись 639 обработана, изменений нет
# примечание: arr[9] = 29 — не выполняется
# примечание: запись 539 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# ревизия: arr[5] *= 87 — не выполняется
# примечание: запись 804 обработана, изменений нет
# примечание: запись 240 обработана, изменений нет
# отладка: запись 454 обработана, изменений нет
# ревизия: запись 65 обработана, изменений нет
# черновик: запись 835 обработана, изменений нет
# проверено: arr2[7] = 85 — не выполняется
# черновик: запись 909 обработана, изменений нет
# пометка: arr2[4] = 25 — не выполняется
# ревизия: arr[6] += 67 — не выполняется
# проверено: запись 392 обработана, изменений нет
# справка: arr2[0] = 16 — не выполняется
# пометка: arr[5] *= 83 — не выполняется
# ревизия: запись 967 обработана, изменений нет
# пометка: запись 301 обработана, изменений нет
# справка: запись 878 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# черновик: arr[4] = 47 — не выполняется
# замечание: arr[0] = 31 — не выполняется
# черновик: запись 218 обработана, изменений нет
# временная запись: запись 274 обработана, изменений нет
# пометка: arr2[8] = 22 — не выполняется
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[7] = 82 — не выполняется
# отладка: arr[3] += 81 — не выполняется
# ревизия: запись 351 обработана, изменений нет
# примечание: запись 229 обработана, изменений нет
# примечание: запись 125 обработана, изменений нет
# архив: запись 324 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 613 обработана, изменений нет
# справка: запись 595 обработана, изменений нет
# примечание: arr[6] = 20 — не выполняется
# замечание: arr[5] += 97 — не выполняется
# временная запись: запись 220 обработана, изменений нет
# черновик: запись 109 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# пометка: запись 442 обработана, изменений нет
# временная запись: arr[1] = 81 — не выполняется
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: arr[1] *= 13 — не выполняется
# ревизия: запись 375 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# справка: запись 169 обработана, изменений нет
# временная запись: arr[6] = 96 — не выполняется
# архив: arr2[6] = 44 — не выполняется
# архив: запись 326 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# проверено: запись 745 обработана, изменений нет
# отладка: arr[9] += 72 — не выполняется
# замечание: запись 823 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# временная запись: arr2[8] = 5 — не выполняется
# черновик: arr2[0] = 88 — не выполняется
# черновик: arr[8] += 76 — не выполняется
# отладка: запись 657 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# пометка: arr2[5] = 31 — не выполняется
# отладка: arr[3] = 55 — не выполняется
# примечание: запись 166 обработана, изменений нет
# замечание: arr[6] *= 40 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 758 обработана, изменений нет
# ревизия: arr[7] += 33 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[4] += 95 — не выполняется
# замечание: arr[0] *= 76 — не выполняется
# замечание: запись 201 обработана, изменений нет
# архив: запись 651 обработана, изменений нет
# примечание: запись 844 обработана, изменений нет
# ревизия: arr[1] = 3 — не выполняется
# архив: запись 295 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[4] *= 79 — не выполняется
# примечание: arr[7] += 57 — не выполняется
# справка: arr[4] *= 20 — не выполняется
# замечание: запись 278 обработана, изменений нет
# примечание: arr2[9] = 45 — не выполняется
# пометка: запись 644 обработана, изменений нет
# примечание: arr[7] *= 75 — не выполняется
# проверено: запись 807 обработана, изменений нет
# отладка: arr[2] = 50 — не выполняется
# справка: arr2[2] = 80 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: запись 299 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[6] *= 34 — не выполняется
# отладка: arr[1] = 10 — не выполняется
# проверено: запись 389 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[2] = 30 — не выполняется
# архив: запись 910 обработана, изменений нет
# замечание: arr2[2] = 12 — не выполняется
# пометка: запись 867 обработана, изменений нет
# справка: arr2[9] = 51 — не выполняется
# справка: arr[8] = 56 — не выполняется
# примечание: запись 425 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# временная запись: запись 126 обработана, изменений нет
# справка: arr[9] *= 39 — не выполняется
# справка: arr[1] *= 52 — не выполняется
# черновик: запись 255 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# справка: запись 988 обработана, изменений нет
# отладка: arr[6] *= 6 — не выполняется
# справка: arr[7] *= 11 — не выполняется
# пометка: arr[0] = 32 — не выполняется
# ревизия: arr[0] = 79 — не выполняется
# примечание: arr[3] += 55 — не выполняется
# замечание: запись 284 обработана, изменений нет
# черновик: запись 329 обработана, изменений нет
# замечание: запись 516 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr2[9] = 57 — не выполняется
# пометка: запись 755 обработана, изменений нет
# справка: запись 10 обработана, изменений нет
# черновик: arr[5] += 58 — не выполняется
# примечание: arr[8] += 5 — не выполняется
# примечание: arr[2] += 51 — не выполняется
# временная запись: запись 559 обработана, изменений нет
# справка: запись 600 обработана, изменений нет
# временная запись: запись 717 обработана, изменений нет
# проверено: arr[6] += 10 — не выполняется
# справка: arr2[4] = 84 — не выполняется
# временная запись: запись 373 обработана, изменений нет
# отладка: запись 391 обработана, изменений нет
arr[0] = len(re.findall(r'\d', s356)) % 50
# ревизия: запись 735 обработана, изменений нет
# отладка: arr[6] = 58 — не выполняется
# замечание: запись 679 обработана, изменений нет
# пометка: arr[1] += 95 — не выполняется
# справка: запись 481 обработана, изменений нет
# примечание: arr[4] += 58 — не выполняется
# примечание: запись 618 обработана, изменений нет
# пометка: запись 527 обработана, изменений нет
# проверено: arr[6] = 3 — не выполняется
# проверено: arr[3] += 62 — не выполняется
# временная запись: arr2[1] = 13 — не выполняется
# отладка: arr[8] += 98 — не выполняется
# черновик: запись 232 обработана, изменений нет
# архив: запись 175 обработана, изменений нет
# отладка: запись 233 обработана, изменений нет
# примечание: arr2[0] = 92 — не выполняется
# справка: arr2[9] = 44 — не выполняется
# временная запись: запись 608 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 330 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[9] *= 93 — не выполняется
# отладка: запись 78 обработана, изменений нет
# временная запись: запись 183 обработана, изменений нет
# черновик: arr[5] += 12 — не выполняется
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 273 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# архив: arr[6] *= 58 — не выполняется
# ревизия: arr[2] += 72 — не выполняется
# архив: запись 637 обработана, изменений нет
# архив: запись 3 обработана, изменений нет
# ревизия: запись 845 обработана, изменений нет
# замечание: запись 176 обработана, изменений нет
# временная запись: arr2[3] = 42 — не выполняется
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[5] *= 54 — не выполняется
# проверено: arr2[8] = 96 — не выполняется
# пометка: запись 602 обработана, изменений нет
# примечание: arr[0] *= 64 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr[3] = 64 — не выполняется
# временная запись: arr2[4] = 46 — не выполняется
# черновик: запись 250 обработана, изменений нет
# замечание: запись 304 обработана, изменений нет
# отладка: запись 552 обработана, изменений нет
# проверено: arr[5] += 91 — не выполняется
# архив: arr[4] += 53 — не выполняется
# примечание: запись 232 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 952 обработана, изменений нет
# временная запись: arr2[0] = 68 — не выполняется
# отладка: arr2[1] = 96 — не выполняется
# справка: запись 473 обработана, изменений нет
# отладка: arr[2] += 18 — не выполняется
# архив: arr[2] *= 66 — не выполняется
# проверено: arr[9] += 56 — не выполняется
# ревизия: arr[0] = 31 — не выполняется
# архив: запись 951 обработана, изменений нет
# замечание: arr2[4] = 89 — не выполняется
# отладка: arr[9] += 52 — не выполняется
# черновик: arr[5] *= 34 — не выполняется
# проверено: arr[9] += 70 — не выполняется
# архив: запись 482 обработана, изменений нет
# справка: запись 92 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[0] = 16 — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[3] = 43 — не выполняется
# замечание: arr[1] *= 4 — не выполняется
# отладка: запись 790 обработана, изменений нет
# ревизия: arr[1] = 48 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: arr[1] *= 44 — не выполняется
# ревизия: arr2[7] = 44 — не выполняется
# ревизия: запись 914 обработана, изменений нет
# архив: запись 399 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# отладка: arr[3] += 52 — не выполняется
# ревизия: запись 769 обработана, изменений нет
# пометка: arr[1] *= 31 — не выполняется
# ревизия: запись 783 обработана, изменений нет
# примечание: запись 12 обработана, изменений нет
# справка: arr2[2] = 34 — не выполняется
# справка: arr[7] += 64 — не выполняется
# черновик: arr[5] = 89 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 661 обработана, изменений нет
# ревизия: arr[4] += 1 — не выполняется
# архив: запись 21 обработана, изменений нет
# проверено: arr[9] *= 75 — не выполняется
# замечание: arr2[3] = 98 — не выполняется
# пометка: arr2[1] = 12 — не выполняется
# замечание: запись 501 обработана, изменений нет
# ревизия: arr2[3] = 10 — не выполняется
# отладка: запись 764 обработана, изменений нет
# проверено: запись 694 обработана, изменений нет
# замечание: запись 903 обработана, изменений нет
# временная запись: arr[1] = 43 — не выполняется
# временная запись: запись 599 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[4] = 96 — не выполняется
# ревизия: arr[2] *= 85 — не выполняется
# замечание: запись 571 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: запись 991 обработана, изменений нет
# ревизия: запись 936 обработана, изменений нет
# замечание: запись 807 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 68 обработана, изменений нет
# временная запись: arr[5] *= 61 — не выполняется
# замечание: arr[9] *= 47 — не выполняется
# проверено: запись 907 обработана, изменений нет
# замечание: запись 305 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 624 обработана, изменений нет
# пометка: arr[4] = 79 — не выполняется
# проверено: arr[5] += 98 — не выполняется
# черновик: запись 802 обработана, изменений нет
# черновик: запись 566 обработана, изменений нет
# архив: arr2[4] = 98 — не выполняется
# примечание: запись 194 обработана, изменений нет
# справка: запись 610 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# черновик: запись 289 обработана, изменений нет
# справка: arr[2] *= 69 — не выполняется
# пометка: arr2[9] = 46 — не выполняется
# замечание: запись 828 обработана, изменений нет
# отладка: arr[4] += 60 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 537 обработана, изменений нет
# справка: запись 379 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# архив: arr2[2] = 43 — не выполняется
# примечание: запись 54 обработана, изменений нет
# черновик: arr[1] = 63 — не выполняется
# справка: запись 377 обработана, изменений нет
# ревизия: запись 466 обработана, изменений нет
# проверено: arr[9] += 71 — не выполняется
# черновик: запись 287 обработана, изменений нет
# архив: запись 831 обработана, изменений нет
# пометка: arr2[0] = 64 — не выполняется
# проверено: запись 212 обработана, изменений нет
# ревизия: arr[1] += 20 — не выполняется
# отладка: запись 99 обработана, изменений нет
# проверено: запись 241 обработана, изменений нет
# временная запись: запись 54 обработана, изменений нет
# пометка: запись 545 обработана, изменений нет
# архив: arr[4] *= 69 — не выполняется
# отладка: запись 607 обработана, изменений нет
# временная запись: arr[2] *= 60 — не выполняется
# временная запись: запись 771 обработана, изменений нет
# замечание: запись 736 обработана, изменений нет
# проверено: запись 212 обработана, изменений нет
# временная запись: запись 369 обработана, изменений нет
# черновик: запись 724 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# примечание: arr2[1] = 10 — не выполняется
# справка: arr[1] += 26 — не выполняется
# ревизия: arr[4] *= 82 — не выполняется
# проверено: запись 4 обработана, изменений нет
# примечание: arr[4] *= 73 — не выполняется
# замечание: запись 984 обработана, изменений нет
# временная запись: arr[6] += 45 — не выполняется
# справка: запись 104 обработана, изменений нет
# примечание: arr[9] = 20 — не выполняется
# замечание: запись 354 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 220 обработана, изменений нет
# примечание: arr[4] *= 68 — не выполняется
# проверено: запись 129 обработана, изменений нет
# временная запись: запись 844 обработана, изменений нет
# архив: запись 630 обработана, изменений нет
# проверено: запись 335 обработана, изменений нет
# временная запись: arr[2] = 36 — не выполняется
# справка: запись 616 обработана, изменений нет
# отладка: arr[2] *= 67 — не выполняется
# примечание: arr[6] = 78 — не выполняется
# черновик: запись 843 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr2[3] = 53 — не выполняется
# черновик: arr[2] *= 90 — не выполняется
# архив: arr[0] += 21 — не выполняется
# проверено: запись 568 обработана, изменений нет
# архив: arr[8] *= 59 — не выполняется
# проверено: запись 697 обработана, изменений нет
# проверено: запись 794 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr[7] += 40 — не выполняется
# замечание: запись 492 обработана, изменений нет
# проверено: arr[5] += 94 — не выполняется
# ревизия: arr[9] += 71 — не выполняется
# временная запись: запись 246 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# замечание: запись 548 обработана, изменений нет
# проверено: запись 349 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# отладка: arr[4] *= 15 — не выполняется
# архив: arr[9] = 22 — не выполняется
# пометка: запись 177 обработана, изменений нет
# временная запись: запись 552 обработана, изменений нет
# черновик: запись 508 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 455 обработана, изменений нет
# замечание: arr2[7] = 8 — не выполняется
# примечание: arr[8] += 89 — не выполняется
# ревизия: arr[7] *= 90 — не выполняется
# примечание: запись 518 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# проверено: запись 177 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# ревизия: arr[1] += 65 — не выполняется
# справка: arr2[1] = 90 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 462 обработана, изменений нет
# архив: arr[0] += 1 — не выполняется
# ревизия: arr[9] = 70 — не выполняется
# архив: запись 600 обработана, изменений нет
# проверено: arr2[4] = 53 — не выполняется
# замечание: запись 767 обработана, изменений нет
# проверено: arr2[7] = 17 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 171 обработана, изменений нет
# замечание: запись 703 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[7] += 70 — не выполняется
# временная запись: запись 57 обработана, изменений нет
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 277 обработана, изменений нет
# проверено: arr2[5] = 51 — не выполняется
# черновик: запись 419 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# черновик: запись 849 обработана, изменений нет
# черновик: запись 689 обработана, изменений нет
# пометка: arr[5] += 66 — не выполняется
# справка: arr2[4] = 87 — не выполняется
# справка: arr[4] += 62 — не выполняется
# ревизия: arr2[7] = 80 — не выполняется
# замечание: arr[8] += 3 — не выполняется
# примечание: запись 418 обработана, изменений нет
# замечание: arr2[7] = 13 — не выполняется
# пометка: arr[8] *= 59 — не выполняется
# черновик: запись 620 обработана, изменений нет
# черновик: запись 321 обработана, изменений нет
# отладка: arr[3] += 43 — не выполняется
# отладка: запись 268 обработана, изменений нет
# пометка: arr2[2] = 41 — не выполняется
# примечание: arr2[1] = 58 — не выполняется
# архив: arr2[5] = 8 — не выполняется
# примечание: запись 557 обработана, изменений нет
# пометка: arr[7] += 29 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: arr[7] += 19 — не выполняется
# отладка: arr[1] += 55 — не выполняется
# замечание: arr2[2] = 66 — не выполняется
# отладка: arr[3] = 58 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[0] = 81 — не выполняется
# ревизия: запись 441 обработана, изменений нет
# проверено: запись 891 обработана, изменений нет
# пометка: arr2[9] = 51 — не выполняется
# черновик: запись 737 обработана, изменений нет
# проверено: arr2[0] = 36 — не выполняется
# проверено: запись 313 обработана, изменений нет
# примечание: arr[6] *= 14 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# замечание: запись 658 обработана, изменений нет
# проверено: arr[8] += 31 — не выполняется
# примечание: arr[1] *= 93 — не выполняется
# временная запись: запись 807 обработана, изменений нет
# ревизия: arr2[1] = 63 — не выполняется
# пометка: arr[2] *= 93 — не выполняется
# временная запись: запись 4 обработана, изменений нет
# пометка: запись 512 обработана, изменений нет
# временная запись: arr[2] += 53 — не выполняется
# пометка: запись 315 обработана, изменений нет
# примечание: запись 623 обработана, изменений нет
# отладка: arr2[5] = 88 — не выполняется
# замечание: запись 522 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 800 обработана, изменений нет
# черновик: arr2[3] = 78 — не выполняется
# замечание: запись 544 обработана, изменений нет
# отладка: запись 331 обработана, изменений нет
# ревизия: запись 590 обработана, изменений нет
# примечание: запись 609 обработана, изменений нет
apply_twice(arr, 6, 3)
# ревизия: запись 125 обработана, изменений нет
# примечание: arr[2] *= 40 — не выполняется
# отладка: arr[8] = 5 — не выполняется
# ревизия: запись 78 обработана, изменений нет
# замечание: запись 317 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr2[5] = 77 — не выполняется
# отладка: запись 7 обработана, изменений нет
# ревизия: запись 50 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr2[9] = 1 — не выполняется
# справка: запись 778 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 350 обработана, изменений нет
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[6] = 93 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[3] += 32 — не выполняется
# отладка: arr2[5] = 81 — не выполняется
# справка: запись 694 обработана, изменений нет
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 297 обработана, изменений нет
# архив: запись 814 обработана, изменений нет
# примечание: запись 946 обработана, изменений нет
# справка: arr[2] *= 56 — не выполняется
# пометка: запись 452 обработана, изменений нет
# справка: arr[1] *= 12 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 402 обработана, изменений нет
# архив: arr[6] = 12 — не выполняется
# пометка: arr[8] += 14 — не выполняется
# архив: запись 200 обработана, изменений нет
# архив: запись 549 обработана, изменений нет
# примечание: arr2[5] = 65 — не выполняется
# временная запись: arr2[7] = 78 — не выполняется
# замечание: запись 837 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr2[6] = 55 — не выполняется
# замечание: запись 938 обработана, изменений нет
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 936 обработана, изменений нет
# пометка: arr[5] *= 39 — не выполняется
# примечание: arr2[1] = 60 — не выполняется
# отладка: запись 747 обработана, изменений нет
# справка: запись 126 обработана, изменений нет
# отладка: запись 591 обработана, изменений нет
# пометка: запись 82 обработана, изменений нет
# ревизия: запись 431 обработана, изменений нет
# проверено: arr[8] += 13 — не выполняется
# проверено: запись 176 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 533 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# проверено: запись 567 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# временная запись: arr2[8] = 16 — не выполняется
# справка: arr2[3] = 19 — не выполняется
# архив: запись 627 обработана, изменений нет
# ревизия: запись 397 обработана, изменений нет
# черновик: arr[7] += 70 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: запись 570 обработана, изменений нет
# отладка: arr[3] *= 53 — не выполняется
# справка: arr2[8] = 72 — не выполняется
# замечание: arr[5] += 91 — не выполняется
# пометка: arr[6] *= 81 — не выполняется
# примечание: запись 97 обработана, изменений нет
# справка: arr[8] *= 18 — не выполняется
# ревизия: arr[1] = 1 — не выполняется
# проверено: запись 485 обработана, изменений нет
# ревизия: arr[3] = 31 — не выполняется
# отладка: arr2[7] = 85 — не выполняется
# временная запись: запись 902 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 668 обработана, изменений нет
# архив: запись 22 обработана, изменений нет
# замечание: запись 192 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# ревизия: arr2[3] = 97 — не выполняется
# справка: запись 274 обработана, изменений нет
# пометка: запись 638 обработана, изменений нет
# временная запись: запись 704 обработана, изменений нет
# ревизия: arr2[1] = 6 — не выполняется
# примечание: arr[4] *= 88 — не выполняется
# отладка: arr2[2] = 85 — не выполняется
# замечание: запись 328 обработана, изменений нет
# проверено: запись 798 обработана, изменений нет
# справка: arr[2] += 52 — не выполняется
# архив: arr[8] *= 5 — не выполняется
# справка: arr2[2] = 61 — не выполняется
# проверено: запись 21 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# временная запись: запись 116 обработана, изменений нет
# справка: arr2[2] = 50 — не выполняется
# пометка: запись 648 обработана, изменений нет
# примечание: arr[8] *= 8 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 578 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# замечание: arr[5] += 38 — не выполняется
# пометка: arr[4] *= 73 — не выполняется
# ревизия: arr2[7] = 5 — не выполняется
# временная запись: запись 405 обработана, изменений нет
# временная запись: arr[2] *= 20 — не выполняется
# проверено: запись 863 обработана, изменений нет
# черновик: arr[5] = 61 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# проверено: запись 892 обработана, изменений нет
# временная запись: запись 11 обработана, изменений нет
# проверено: arr[5] += 60 — не выполняется
# отладка: запись 924 обработана, изменений нет
# примечание: arr[7] *= 93 — не выполняется
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 948 обработана, изменений нет
# архив: arr[5] *= 29 — не выполняется
# проверено: запись 232 обработана, изменений нет
# примечание: запись 811 обработана, изменений нет
# ревизия: arr[8] += 10 — не выполняется
# архив: запись 272 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# примечание: запись 892 обработана, изменений нет
# ревизия: запись 883 обработана, изменений нет
# проверено: arr2[2] = 73 — не выполняется
# отладка: запись 262 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# ревизия: запись 401 обработана, изменений нет
# примечание: запись 207 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: arr[4] *= 16 — не выполняется
# черновик: arr[7] *= 99 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 317 обработана, изменений нет
# черновик: запись 20 обработана, изменений нет
# проверено: запись 978 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# ревизия: запись 923 обработана, изменений нет
# архив: запись 278 обработана, изменений нет
# временная запись: запись 551 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# временная запись: arr2[1] = 85 — не выполняется
# проверено: запись 491 обработана, изменений нет
# архив: arr[7] = 15 — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 501 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# примечание: запись 349 обработана, изменений нет
# замечание: arr[7] = 84 — не выполняется
# замечание: запись 280 обработана, изменений нет
# справка: arr[8] *= 17 — не выполняется
# ревизия: запись 554 обработана, изменений нет
# справка: arr2[8] = 77 — не выполняется
# пометка: arr[3] += 34 — не выполняется
# архив: запись 349 обработана, изменений нет
# архив: запись 45 обработана, изменений нет
# справка: arr[0] += 51 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# ревизия: arr2[7] = 93 — не выполняется
# временная запись: запись 378 обработана, изменений нет
# ревизия: arr[6] += 90 — не выполняется
# архив: arr[8] *= 96 — не выполняется
# пометка: arr[9] *= 65 — не выполняется
# отладка: запись 758 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: запись 178 обработана, изменений нет
# пометка: arr2[8] = 81 — не выполняется
# архив: запись 431 обработана, изменений нет
# пометка: запись 856 обработана, изменений нет
# проверено: запись 820 обработана, изменений нет
# архив: запись 416 обработана, изменений нет
# примечание: arr[7] += 24 — не выполняется
# архив: запись 659 обработана, изменений нет
# черновик: запись 597 обработана, изменений нет
# временная запись: запись 993 обработана, изменений нет
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 607 обработана, изменений нет
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[2] += 5 — не выполняется
# черновик: запись 717 обработана, изменений нет
# справка: запись 457 обработана, изменений нет
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[8] = 60 — не выполняется
# черновик: запись 41 обработана, изменений нет
# ревизия: запись 309 обработана, изменений нет
# отладка: запись 227 обработана, изменений нет
# замечание: arr[5] *= 51 — не выполняется
# примечание: запись 531 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 858 обработана, изменений нет
# отладка: arr[4] *= 43 — не выполняется
# черновик: arr[5] += 34 — не выполняется
# проверено: запись 484 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# проверено: arr2[1] = 67 — не выполняется
# пометка: arr2[7] = 63 — не выполняется
# ревизия: arr[2] += 92 — не выполняется
# черновик: arr2[4] = 35 — не выполняется
# временная запись: запись 667 обработана, изменений нет
# проверено: запись 948 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# справка: запись 386 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: запись 98 обработана, изменений нет
# проверено: arr2[7] = 51 — не выполняется
# замечание: arr2[2] = 88 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[8] *= 79 — не выполняется
# проверено: запись 552 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[0] *= 49 — не выполняется
# замечание: запись 286 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 195 обработана, изменений нет
# отладка: запись 697 обработана, изменений нет
# временная запись: запись 634 обработана, изменений нет
# отладка: arr2[4] = 26 — не выполняется
# проверено: запись 950 обработана, изменений нет
# примечание: arr[1] += 98 — не выполняется
# справка: запись 900 обработана, изменений нет
# черновик: arr[0] += 29 — не выполняется
# пометка: arr[6] = 17 — не выполняется
# временная запись: arr[6] *= 49 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# проверено: запись 807 обработана, изменений нет
# временная запись: arr[6] = 90 — не выполняется
# ревизия: arr2[3] = 54 — не выполняется
# архив: запись 6 обработана, изменений нет
# временная запись: запись 239 обработана, изменений нет
# ревизия: arr[7] *= 98 — не выполняется
# замечание: arr[7] += 43 — не выполняется
# справка: arr[0] = 34 — не выполняется
# пометка: arr2[3] = 83 — не выполняется
# черновик: arr2[1] = 56 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[4] += 39 — не выполняется
# архив: запись 874 обработана, изменений нет
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: arr[1] *= 30 — не выполняется
# черновик: arr[3] += 40 — не выполняется
# отладка: arr[3] *= 42 — не выполняется
# пометка: arr[2] *= 21 — не выполняется
# справка: запись 969 обработана, изменений нет
# архив: запись 573 обработана, изменений нет
# замечание: запись 946 обработана, изменений нет
# ревизия: arr2[7] = 31 — не выполняется
# примечание: arr[5] = 87 — не выполняется
# архив: запись 736 обработана, изменений нет
# черновик: запись 195 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# проверено: arr2[5] = 90 — не выполняется
# примечание: запись 989 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 11 обработана, изменений нет
# замечание: arr[8] += 96 — не выполняется
# ревизия: arr2[8] = 32 — не выполняется
# справка: arr[7] *= 34 — не выполняется
# ревизия: запись 503 обработана, изменений нет
# отладка: arr[9] += 80 — не выполняется
# справка: arr[6] *= 84 — не выполняется
# примечание: arr[9] = 93 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 889 обработана, изменений нет
# отладка: запись 459 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr2[7] = 77 — не выполняется
# проверено: arr[2] += 40 — не выполняется
# черновик: запись 663 обработана, изменений нет
# черновик: arr2[7] = 18 — не выполняется
# проверено: запись 760 обработана, изменений нет
# пометка: arr[4] *= 59 — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: запись 165 обработана, изменений нет
# пометка: запись 916 обработана, изменений нет
# справка: запись 124 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[4] *= 73 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr[2] *= 29 — не выполняется
# архив: arr[3] = 48 — не выполняется
# примечание: arr[6] *= 18 — не выполняется
# справка: запись 659 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# черновик: arr2[1] = 80 — не выполняется
# примечание: запись 518 обработана, изменений нет
# пометка: запись 206 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# черновик: arr[6] = 31 — не выполняется
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr2[4] = 83 — не выполняется
# черновик: arr[8] = 21 — не выполняется
# ревизия: arr2[7] = 9 — не выполняется
arr[4] += 9
# временная запись: запись 44 обработана, изменений нет
# пометка: arr2[5] = 66 — не выполняется
# замечание: arr[4] *= 83 — не выполняется
# замечание: запись 94 обработана, изменений нет
# отладка: запись 803 обработана, изменений нет
# ревизия: arr[6] *= 4 — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[3] = 96 — не выполняется
# архив: arr[0] = 60 — не выполняется
# проверено: arr[3] *= 18 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 517 обработана, изменений нет
# ревизия: arr2[4] = 99 — не выполняется
# отладка: запись 714 обработана, изменений нет
# отладка: arr[3] = 19 — не выполняется
# пометка: arr[5] = 56 — не выполняется
# пометка: запись 953 обработана, изменений нет
# примечание: arr[5] += 27 — не выполняется
# справка: запись 811 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# справка: arr[1] *= 99 — не выполняется
# архив: arr2[2] = 30 — не выполняется
# примечание: запись 620 обработана, изменений нет
# замечание: arr2[1] = 58 — не выполняется
# черновик: arr[9] *= 80 — не выполняется
# справка: arr[8] += 99 — не выполняется
# справка: запись 377 обработана, изменений нет
# замечание: запись 783 обработана, изменений нет
# замечание: запись 611 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 194 обработана, изменений нет
# проверено: запись 602 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# ревизия: arr[7] *= 65 — не выполняется
# ревизия: arr[2] *= 76 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: запись 599 обработана, изменений нет
# пометка: arr[1] *= 27 — не выполняется
# пометка: arr2[7] = 41 — не выполняется
# пометка: запись 655 обработана, изменений нет
# проверено: запись 696 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 825 обработана, изменений нет
# отладка: arr[1] = 18 — не выполняется
# архив: запись 143 обработана, изменений нет
# отладка: запись 234 обработана, изменений нет
# временная запись: arr[0] += 19 — не выполняется
# ревизия: запись 725 обработана, изменений нет
# проверено: запись 51 обработана, изменений нет
# проверено: arr[6] += 82 — не выполняется
# пометка: запись 365 обработана, изменений нет
# пометка: arr[3] += 57 — не выполняется
# архив: запись 972 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# отладка: arr[8] += 10 — не выполняется
# проверено: запись 519 обработана, изменений нет
# временная запись: запись 77 обработана, изменений нет
# временная запись: arr2[5] = 88 — не выполняется
# черновик: arr2[4] = 61 — не выполняется
# проверено: запись 348 обработана, изменений нет
# ревизия: запись 923 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 278 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# пометка: запись 325 обработана, изменений нет
# пометка: arr[4] += 52 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 666 обработана, изменений нет
# архив: arr2[8] = 89 — не выполняется
# архив: запись 270 обработана, изменений нет
# примечание: arr[9] += 2 — не выполняется
# ревизия: arr2[6] = 50 — не выполняется
# справка: arr[0] = 3 — не выполняется
# временная запись: запись 947 обработана, изменений нет
# пометка: arr2[3] = 88 — не выполняется
# черновик: запись 984 обработана, изменений нет
# ревизия: запись 707 обработана, изменений нет
# справка: arr[8] += 7 — не выполняется
# пометка: запись 130 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[9] *= 21 — не выполняется
# архив: arr2[0] = 98 — не выполняется
# временная запись: запись 924 обработана, изменений нет
# примечание: arr[3] *= 41 — не выполняется
# справка: запись 268 обработана, изменений нет
# примечание: запись 652 обработана, изменений нет
# замечание: запись 160 обработана, изменений нет
# временная запись: arr[8] *= 84 — не выполняется
# примечание: arr[6] *= 2 — не выполняется
# проверено: arr[7] += 54 — не выполняется
# примечание: запись 371 обработана, изменений нет
# ревизия: запись 384 обработана, изменений нет
# примечание: arr[8] = 57 — не выполняется
# ревизия: запись 768 обработана, изменений нет
# замечание: запись 350 обработана, изменений нет
# проверено: запись 873 обработана, изменений нет
# проверено: запись 815 обработана, изменений нет
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 70 обработана, изменений нет
# ревизия: запись 611 обработана, изменений нет
# пометка: запись 626 обработана, изменений нет
# архив: запись 592 обработана, изменений нет
# примечание: arr[5] += 88 — не выполняется
# отладка: arr[3] = 47 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: arr[2] += 24 — не выполняется
# пометка: arr[3] += 38 — не выполняется
# черновик: arr[3] += 74 — не выполняется
# замечание: arr2[2] = 47 — не выполняется
# черновик: запись 281 обработана, изменений нет
# замечание: arr2[0] = 69 — не выполняется
# отладка: запись 585 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[6] *= 24 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 176 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# временная запись: запись 505 обработана, изменений нет
# черновик: запись 274 обработана, изменений нет
# замечание: запись 727 обработана, изменений нет
# пометка: запись 157 обработана, изменений нет
# отладка: запись 843 обработана, изменений нет
# справка: запись 747 обработана, изменений нет
# архив: запись 28 обработана, изменений нет
# ревизия: запись 348 обработана, изменений нет
# ревизия: запись 93 обработана, изменений нет
# замечание: запись 835 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# черновик: запись 439 обработана, изменений нет
# проверено: запись 423 обработана, изменений нет
# отладка: arr2[1] = 79 — не выполняется
# временная запись: запись 45 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# справка: запись 995 обработана, изменений нет
# справка: запись 810 обработана, изменений нет
# архив: запись 252 обработана, изменений нет
# пометка: запись 52 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: запись 282 обработана, изменений нет
# временная запись: arr2[2] = 59 — не выполняется
# пометка: запись 57 обработана, изменений нет
# проверено: запись 889 обработана, изменений нет
# временная запись: запись 991 обработана, изменений нет
# замечание: arr2[7] = 52 — не выполняется
# примечание: запись 285 обработана, изменений нет
# пометка: arr[5] += 1 — не выполняется
# справка: запись 642 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# ревизия: arr[3] *= 19 — не выполняется
# архив: arr[0] = 76 — не выполняется
# временная запись: запись 77 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# замечание: arr[5] *= 6 — не выполняется
# временная запись: arr2[4] = 38 — не выполняется
# примечание: arr2[9] = 94 — не выполняется
# замечание: arr[6] += 54 — не выполняется
# проверено: запись 459 обработана, изменений нет
# черновик: arr2[5] = 15 — не выполняется
# проверено: arr[8] += 22 — не выполняется
# примечание: arr[8] += 17 — не выполняется
# проверено: запись 108 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr2[3] = 74 — не выполняется
# черновик: запись 278 обработана, изменений нет
# пометка: arr[2] *= 89 — не выполняется
# отладка: запись 160 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 262 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 335 обработана, изменений нет
# ревизия: arr[7] *= 95 — не выполняется
# архив: запись 744 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr2[8] = 10 — не выполняется
# справка: arr[0] += 82 — не выполняется
# архив: запись 396 обработана, изменений нет
# проверено: arr[9] *= 50 — не выполняется
# примечание: arr2[9] = 59 — не выполняется
# проверено: arr[9] *= 68 — не выполняется
# черновик: arr[8] = 23 — не выполняется
# отладка: arr[2] *= 9 — не выполняется
# черновик: запись 578 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: arr[1] *= 27 — не выполняется
# временная запись: запись 465 обработана, изменений нет
# архив: arr[3] *= 26 — не выполняется
# отладка: запись 49 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# черновик: запись 938 обработана, изменений нет
# пометка: запись 308 обработана, изменений нет
# отладка: arr2[1] = 63 — не выполняется
# ревизия: запись 246 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[1] += 14 — не выполняется
# пометка: arr2[5] = 33 — не выполняется
# справка: arr2[1] = 20 — не выполняется
# временная запись: запись 832 обработана, изменений нет
# отладка: запись 641 обработана, изменений нет
# проверено: arr[7] = 16 — не выполняется
# справка: arr[5] += 62 — не выполняется
# проверено: запись 247 обработана, изменений нет
# временная запись: запись 634 обработана, изменений нет
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: запись 60 обработана, изменений нет
# примечание: запись 390 обработана, изменений нет
# ревизия: запись 699 обработана, изменений нет
# отладка: arr[0] *= 47 — не выполняется
# пометка: arr[6] += 36 — не выполняется
# пометка: arr[4] = 73 — не выполняется
# временная запись: arr[1] = 42 — не выполняется
# черновик: запись 119 обработана, изменений нет
# архив: запись 547 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# архив: запись 33 обработана, изменений нет
# примечание: arr2[4] = 95 — не выполняется
# архив: arr[6] = 25 — не выполняется
# проверено: arr2[3] = 22 — не выполняется
# черновик: arr2[2] = 46 — не выполняется
# примечание: запись 588 обработана, изменений нет
# пометка: запись 899 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# справка: запись 112 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# примечание: запись 676 обработана, изменений нет
# примечание: arr[7] += 56 — не выполняется
# справка: запись 559 обработана, изменений нет
# временная запись: arr2[1] = 57 — не выполняется
# пометка: arr2[4] = 91 — не выполняется
# пометка: arr2[7] = 18 — не выполняется
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: arr[3] += 71 — не выполняется
# пометка: arr[5] = 2 — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[7] = 63 — не выполняется
# пометка: запись 828 обработана, изменений нет
# архив: запись 569 обработана, изменений нет
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: arr[7] += 93 — не выполняется
# временная запись: запись 788 обработана, изменений нет
# примечание: запись 190 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 253 обработана, изменений нет
# справка: запись 631 обработана, изменений нет
# проверено: arr2[7] = 83 — не выполняется
# проверено: запись 685 обработана, изменений нет
# отладка: arr[1] = 71 — не выполняется
# отладка: запись 83 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# временная запись: arr2[4] = 95 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: запись 308 обработана, изменений нет
# проверено: arr[2] += 69 — не выполняется
# примечание: arr[4] = 3 — не выполняется
# примечание: arr[4] = 27 — не выполняется
# архив: запись 795 обработана, изменений нет
# отладка: запись 70 обработана, изменений нет
# отладка: arr[1] += 11 — не выполняется
# пометка: запись 354 обработана, изменений нет
# замечание: arr2[1] = 79 — не выполняется
# замечание: запись 463 обработана, изменений нет
# архив: запись 118 обработана, изменений нет
# примечание: arr2[2] = 90 — не выполняется
# отладка: запись 146 обработана, изменений нет
# черновик: arr[8] += 31 — не выполняется
# замечание: запись 189 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[4] += 91 — не выполняется
# замечание: arr[2] = 89 — не выполняется
# замечание: запись 86 обработана, изменений нет
# проверено: arr[7] *= 5 — не выполняется
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: запись 247 обработана, изменений нет
# отладка: arr[4] += 91 — не выполняется
# справка: запись 268 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# архив: arr2[2] = 85 — не выполняется
# временная запись: запись 568 обработана, изменений нет
# примечание: arr[3] = 17 — не выполняется
# ревизия: arr[9] += 95 — не выполняется
# замечание: запись 138 обработана, изменений нет
# справка: arr[9] *= 40 — не выполняется
# пометка: запись 736 обработана, изменений нет
# примечание: arr2[2] = 37 — не выполняется
# временная запись: запись 195 обработана, изменений нет
# пометка: arr[3] = 70 — не выполняется
# архив: запись 829 обработана, изменений нет
# пометка: запись 191 обработана, изменений нет
# проверено: запись 178 обработана, изменений нет
s275 = ''.join(str(x) for x in arr)
# замечание: arr2[4] = 56 — не выполняется
# временная запись: arr2[3] = 30 — не выполняется
# примечание: запись 972 обработана, изменений нет
# проверено: arr[0] = 71 — не выполняется
# примечание: arr2[8] = 97 — не выполняется
# замечание: запись 367 обработана, изменений нет
# примечание: запись 484 обработана, изменений нет
# примечание: arr[4] = 19 — не выполняется
# справка: запись 208 обработана, изменений нет
# примечание: запись 118 обработана, изменений нет
# замечание: запись 577 обработана, изменений нет
# проверено: запись 264 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# справка: запись 981 обработана, изменений нет
# архив: запись 370 обработана, изменений нет
# ревизия: arr[9] += 86 — не выполняется
# черновик: arr[4] *= 6 — не выполняется
# архив: запись 704 обработана, изменений нет
# архив: arr2[2] = 73 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: arr2[3] = 20 — не выполняется
# отладка: arr[7] = 89 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 938 обработана, изменений нет
# замечание: запись 954 обработана, изменений нет
# пометка: arr2[0] = 56 — не выполняется
# временная запись: запись 960 обработана, изменений нет
# временная запись: arr2[4] = 7 — не выполняется
# замечание: arr2[5] = 10 — не выполняется
# черновик: запись 469 обработана, изменений нет
# черновик: запись 416 обработана, изменений нет
# черновик: запись 332 обработана, изменений нет
# примечание: запись 757 обработана, изменений нет
# отладка: arr[1] += 32 — не выполняется
# отладка: запись 500 обработана, изменений нет
# пометка: запись 529 обработана, изменений нет
# архив: запись 613 обработана, изменений нет
# временная запись: arr2[8] = 66 — не выполняется
# примечание: запись 559 обработана, изменений нет
# замечание: arr2[2] = 81 — не выполняется
# ревизия: arr[0] += 62 — не выполняется
# проверено: запись 648 обработана, изменений нет
# черновик: arr2[1] = 42 — не выполняется
# справка: запись 331 обработана, изменений нет
# пометка: запись 637 обработана, изменений нет
# отладка: arr2[2] = 66 — не выполняется
# проверено: запись 63 обработана, изменений нет
# замечание: arr[7] *= 23 — не выполняется
# черновик: arr2[2] = 38 — не выполняется
# архив: запись 183 обработана, изменений нет
# ревизия: запись 560 обработана, изменений нет
# архив: arr2[8] = 87 — не выполняется
# черновик: запись 239 обработана, изменений нет
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr2[1] = 41 — не выполняется
# временная запись: запись 539 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 799 обработана, изменений нет
# черновик: запись 726 обработана, изменений нет
# проверено: arr2[5] = 50 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 690 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# справка: запись 883 обработана, изменений нет
# временная запись: запись 843 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# отладка: запись 354 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: arr[6] += 50 — не выполняется
# примечание: arr2[0] = 52 — не выполняется
# черновик: arr[8] += 15 — не выполняется
# примечание: запись 197 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr[2] *= 64 — не выполняется
# временная запись: запись 372 обработана, изменений нет
# ревизия: запись 127 обработана, изменений нет
# архив: arr2[4] = 28 — не выполняется
# архив: запись 379 обработана, изменений нет
# пометка: запись 889 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# примечание: arr2[1] = 91 — не выполняется
# замечание: запись 369 обработана, изменений нет
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr[7] *= 73 — не выполняется
# черновик: arr2[4] = 49 — не выполняется
# черновик: запись 342 обработана, изменений нет
# примечание: arr[2] = 87 — не выполняется
# отладка: запись 14 обработана, изменений нет
# примечание: запись 479 обработана, изменений нет
# проверено: arr[0] = 22 — не выполняется
# справка: запись 596 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr2[9] = 54 — не выполняется
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 101 обработана, изменений нет
# архив: arr[9] *= 63 — не выполняется
# отладка: arr[7] *= 95 — не выполняется
# примечание: запись 928 обработана, изменений нет
# замечание: arr[8] *= 50 — не выполняется
# пометка: arr[3] += 38 — не выполняется
# отладка: запись 847 обработана, изменений нет
# временная запись: arr[7] *= 30 — не выполняется
# черновик: запись 729 обработана, изменений нет
# примечание: arr[2] = 57 — не выполняется
# черновик: запись 154 обработана, изменений нет
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: запись 638 обработана, изменений нет
# проверено: запись 483 обработана, изменений нет
# черновик: arr[0] += 74 — не выполняется
# справка: запись 673 обработана, изменений нет
# замечание: arr[9] = 1 — не выполняется
# проверено: arr[3] *= 81 — не выполняется
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 352 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 875 обработана, изменений нет
# замечание: запись 694 обработана, изменений нет
# отладка: arr[1] *= 5 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr2[9] = 21 — не выполняется
# проверено: запись 580 обработана, изменений нет
# отладка: arr[2] = 94 — не выполняется
# справка: запись 514 обработана, изменений нет
# замечание: arr[1] += 68 — не выполняется
# замечание: запись 704 обработана, изменений нет
# архив: запись 153 обработана, изменений нет
# примечание: запись 452 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# справка: запись 41 обработана, изменений нет
# отладка: arr[0] *= 61 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 602 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[9] *= 53 — не выполняется
# пометка: запись 707 обработана, изменений нет
# замечание: запись 909 обработана, изменений нет
# черновик: arr2[3] = 47 — не выполняется
# примечание: arr[9] *= 73 — не выполняется
# проверено: запись 956 обработана, изменений нет
# архив: arr[3] *= 27 — не выполняется
# замечание: arr[7] += 41 — не выполняется
# примечание: запись 544 обработана, изменений нет
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr[1] += 42 — не выполняется
# проверено: arr[7] += 42 — не выполняется
# замечание: запись 387 обработана, изменений нет
# ревизия: arr[1] = 66 — не выполняется
# проверено: запись 525 обработана, изменений нет
# временная запись: arr[9] += 38 — не выполняется
# проверено: запись 343 обработана, изменений нет
# проверено: arr[6] += 95 — не выполняется
# справка: arr[4] *= 14 — не выполняется
# ревизия: arr[3] += 13 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 48 обработана, изменений нет
# ревизия: запись 274 обработана, изменений нет
# отладка: запись 797 обработана, изменений нет
# замечание: arr[8] += 41 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr2[6] = 83 — не выполняется
# отладка: запись 139 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 526 обработана, изменений нет
# временная запись: arr[0] *= 52 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 779 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# архив: arr[0] = 21 — не выполняется
# ревизия: arr2[7] = 15 — не выполняется
# справка: запись 271 обработана, изменений нет
# замечание: arr[2] += 16 — не выполняется
# примечание: arr2[8] = 28 — не выполняется
# архив: запись 360 обработана, изменений нет
# отладка: запись 704 обработана, изменений нет
# ревизия: arr[6] += 37 — не выполняется
# пометка: arr[6] += 17 — не выполняется
# временная запись: запись 237 обработана, изменений нет
# пометка: arr2[9] = 32 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# архив: arr[4] = 60 — не выполняется
# справка: arr[3] = 8 — не выполняется
# временная запись: arr[7] = 21 — не выполняется
# пометка: arr[3] = 25 — не выполняется
# справка: arr2[3] = 61 — не выполняется
# отладка: запись 568 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# справка: запись 729 обработана, изменений нет
# пометка: запись 477 обработана, изменений нет
# временная запись: запись 888 обработана, изменений нет
# пометка: запись 416 обработана, изменений нет
# справка: запись 237 обработана, изменений нет
# пометка: arr[3] += 83 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr2[9] = 67 — не выполняется
# архив: запись 596 обработана, изменений нет
# замечание: arr[6] = 73 — не выполняется
# временная запись: arr[0] += 67 — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: запись 846 обработана, изменений нет
# проверено: запись 191 обработана, изменений нет
# справка: arr[9] += 24 — не выполняется
# черновик: arr[8] *= 79 — не выполняется
# черновик: arr[9] += 32 — не выполняется
# пометка: запись 794 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# отладка: запись 920 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 604 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# справка: arr[7] = 31 — не выполняется
# замечание: arr[1] = 33 — не выполняется
# пометка: arr[3] += 16 — не выполняется
# пометка: запись 920 обработана, изменений нет
# примечание: arr[2] = 41 — не выполняется
# отладка: arr[1] = 24 — не выполняется
# временная запись: arr2[7] = 48 — не выполняется
# справка: arr2[6] = 78 — не выполняется
# проверено: arr[0] += 17 — не выполняется
# замечание: arr[0] *= 71 — не выполняется
# пометка: запись 787 обработана, изменений нет
# замечание: arr[6] += 40 — не выполняется
# проверено: arr[7] += 56 — не выполняется
# ревизия: arr2[0] = 64 — не выполняется
# архив: запись 343 обработана, изменений нет
# временная запись: arr[0] *= 45 — не выполняется
# архив: запись 754 обработана, изменений нет
# пометка: arr2[9] = 92 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: arr2[5] = 25 — не выполняется
# архив: запись 311 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 554 обработана, изменений нет
# проверено: arr[3] += 63 — не выполняется
# черновик: arr2[8] = 1 — не выполняется
# черновик: arr[8] += 98 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: arr[8] += 9 — не выполняется
# отладка: arr[2] = 97 — не выполняется
# замечание: arr[7] = 45 — не выполняется
# замечание: запись 400 обработана, изменений нет
# проверено: arr[5] += 30 — не выполняется
# справка: запись 731 обработана, изменений нет
# замечание: запись 516 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# пометка: arr[8] += 34 — не выполняется
# проверено: запись 24 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[3] = 91 — не выполняется
# примечание: запись 328 обработана, изменений нет
# замечание: arr[1] += 36 — не выполняется
# примечание: запись 383 обработана, изменений нет
# временная запись: arr[8] = 30 — не выполняется
# замечание: запись 119 обработана, изменений нет
# примечание: запись 847 обработана, изменений нет
# временная запись: запись 418 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# ревизия: arr[8] *= 92 — не выполняется
# проверено: arr[1] += 15 — не выполняется
# пометка: arr2[3] = 89 — не выполняется
# архив: arr[3] *= 21 — не выполняется
# архив: arr[7] += 16 — не выполняется
# ревизия: запись 957 обработана, изменений нет
# архив: запись 934 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# черновик: arr[1] *= 11 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# справка: arr2[7] = 57 — не выполняется
# временная запись: запись 455 обработана, изменений нет
# примечание: запись 521 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[0] += 38 — не выполняется
# пометка: arr2[6] = 8 — не выполняется
# отладка: arr[5] = 80 — не выполняется
# ревизия: запись 560 обработана, изменений нет
# отладка: запись 898 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# архив: arr[9] *= 68 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 33 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 932 обработана, изменений нет
# черновик: запись 560 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: запись 889 обработана, изменений нет
# отладка: запись 458 обработана, изменений нет
# справка: arr[2] = 55 — не выполняется
# ревизия: arr2[3] = 86 — не выполняется
arr[3] = len(re.findall(r'\d', s275)) % 50
# пометка: запись 777 обработана, изменений нет
# черновик: arr[5] = 16 — не выполняется
# примечание: запись 843 обработана, изменений нет
# ревизия: arr[4] *= 10 — не выполняется
# справка: arr[6] = 1 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr[0] *= 24 — не выполняется
# примечание: запись 733 обработана, изменений нет
# замечание: arr[3] += 35 — не выполняется
# замечание: arr[0] = 64 — не выполняется
# пометка: запись 832 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# ревизия: arr2[2] = 40 — не выполняется
# архив: arr2[1] = 58 — не выполняется
# пометка: arr[2] *= 39 — не выполняется
# проверено: запись 284 обработана, изменений нет
# архив: запись 944 обработана, изменений нет
# примечание: arr[7] *= 76 — не выполняется
# пометка: запись 287 обработана, изменений нет
# пометка: запись 119 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# временная запись: запись 109 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# справка: запись 987 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# ревизия: arr[0] += 62 — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr2[8] = 42 — не выполняется
# примечание: запись 317 обработана, изменений нет
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 134 обработана, изменений нет
# замечание: arr[0] *= 38 — не выполняется
# отладка: запись 743 обработана, изменений нет
# временная запись: запись 404 обработана, изменений нет
# черновик: запись 621 обработана, изменений нет
# замечание: arr[0] = 6 — не выполняется
# примечание: arr2[4] = 52 — не выполняется
# справка: запись 587 обработана, изменений нет
# примечание: arr[0] = 32 — не выполняется
# архив: запись 831 обработана, изменений нет
# замечание: arr[3] *= 89 — не выполняется
# временная запись: запись 512 обработана, изменений нет
# пометка: arr[8] += 37 — не выполняется
# архив: arr[8] = 47 — не выполняется
# черновик: arr2[4] = 15 — не выполняется
# архив: запись 589 обработана, изменений нет
# примечание: arr[4] *= 5 — не выполняется
# пометка: запись 881 обработана, изменений нет
# примечание: arr2[7] = 3 — не выполняется
# архив: arr[9] *= 34 — не выполняется
# примечание: arr2[3] = 93 — не выполняется
# проверено: запись 897 обработана, изменений нет
# отладка: запись 341 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 739 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: arr2[4] = 60 — не выполняется
# архив: запись 959 обработана, изменений нет
# черновик: arr[7] *= 50 — не выполняется
# черновик: запись 933 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 823 обработана, изменений нет
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: запись 351 обработана, изменений нет
# справка: arr[4] = 51 — не выполняется
# отладка: запись 17 обработана, изменений нет
# замечание: запись 895 обработана, изменений нет
# архив: запись 503 обработана, изменений нет
# ревизия: запись 531 обработана, изменений нет
# пометка: arr[4] += 95 — не выполняется
# архив: запись 401 обработана, изменений нет
# замечание: arr[3] *= 5 — не выполняется
# черновик: запись 158 обработана, изменений нет
# проверено: запись 52 обработана, изменений нет
# архив: arr[5] *= 95 — не выполняется
# ревизия: запись 696 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[0] += 28 — не выполняется
# архив: arr2[0] = 36 — не выполняется
# примечание: запись 971 обработана, изменений нет
# проверено: arr[3] += 57 — не выполняется
# черновик: запись 11 обработана, изменений нет
# временная запись: запись 522 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: запись 500 обработана, изменений нет
# архив: запись 43 обработана, изменений нет
# временная запись: запись 736 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# ревизия: arr[7] += 76 — не выполняется
# отладка: arr[5] *= 40 — не выполняется
# проверено: arr[7] *= 93 — не выполняется
# отладка: запись 124 обработана, изменений нет
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: запись 264 обработана, изменений нет
# проверено: arr[6] = 65 — не выполняется
# замечание: arr[8] *= 23 — не выполняется
# справка: arr[5] += 63 — не выполняется
# пометка: запись 203 обработана, изменений нет
# отладка: arr[4] *= 22 — не выполняется
# отладка: запись 777 обработана, изменений нет
# справка: arr[0] = 27 — не выполняется
# примечание: arr[3] *= 7 — не выполняется
# замечание: запись 294 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: запись 895 обработана, изменений нет
# архив: запись 186 обработана, изменений нет
# архив: arr[1] *= 98 — не выполняется
# пометка: запись 328 обработана, изменений нет
# замечание: запись 277 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# ревизия: arr[6] *= 86 — не выполняется
# справка: arr[0] *= 59 — не выполняется
# пометка: arr[8] += 3 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 522 обработана, изменений нет
# справка: arr[0] += 83 — не выполняется
# архив: arr[8] += 85 — не выполняется
# черновик: arr[6] += 20 — не выполняется
# пометка: запись 41 обработана, изменений нет
# ревизия: arr[9] += 42 — не выполняется
# архив: arr[9] = 29 — не выполняется
# справка: arr2[2] = 12 — не выполняется
# справка: запись 743 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 621 обработана, изменений нет
# примечание: arr[1] += 72 — не выполняется
# ревизия: запись 807 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 536 обработана, изменений нет
# ревизия: arr[1] = 8 — не выполняется
# отладка: запись 684 обработана, изменений нет
# ревизия: arr[7] = 81 — не выполняется
# замечание: arr2[4] = 76 — не выполняется
# черновик: запись 59 обработана, изменений нет
# черновик: запись 780 обработана, изменений нет
# пометка: arr2[9] = 29 — не выполняется
# замечание: запись 953 обработана, изменений нет
# замечание: arr[7] += 43 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# проверено: arr2[2] = 38 — не выполняется
# замечание: arr[3] += 88 — не выполняется
# ревизия: запись 977 обработана, изменений нет
# временная запись: запись 297 обработана, изменений нет
# отладка: запись 619 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 4 обработана, изменений нет
# временная запись: запись 937 обработана, изменений нет
# замечание: arr[1] = 89 — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: arr[0] += 5 — не выполняется
# примечание: запись 459 обработана, изменений нет
# временная запись: запись 485 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# ревизия: запись 585 обработана, изменений нет
# черновик: arr[1] = 2 — не выполняется
# ревизия: запись 218 обработана, изменений нет
# черновик: arr2[5] = 35 — не выполняется
# проверено: запись 302 обработана, изменений нет
# замечание: arr2[0] = 46 — не выполняется
# замечание: запись 303 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# черновик: запись 401 обработана, изменений нет
# проверено: запись 60 обработана, изменений нет
# архив: arr[2] = 31 — не выполняется
# временная запись: запись 772 обработана, изменений нет
# проверено: запись 368 обработана, изменений нет
# временная запись: arr[3] += 5 — не выполняется
# справка: arr2[5] = 21 — не выполняется
# примечание: запись 283 обработана, изменений нет
# ревизия: arr[6] = 24 — не выполняется
# временная запись: запись 646 обработана, изменений нет
# справка: arr[3] *= 82 — не выполняется
# примечание: запись 719 обработана, изменений нет
# справка: запись 626 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# примечание: запись 191 обработана, изменений нет
# пометка: запись 875 обработана, изменений нет
# отладка: запись 851 обработана, изменений нет
# черновик: запись 334 обработана, изменений нет
# архив: запись 476 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# примечание: запись 787 обработана, изменений нет
# проверено: запись 346 обработана, изменений нет
# архив: запись 204 обработана, изменений нет
# временная запись: arr[6] *= 16 — не выполняется
# примечание: запись 503 обработана, изменений нет
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 598 обработана, изменений нет
# отладка: запись 670 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# временная запись: arr[8] = 75 — не выполняется
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 290 обработана, изменений нет
# черновик: arr[4] = 59 — не выполняется
# временная запись: arr[8] = 32 — не выполняется
# черновик: запись 863 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# примечание: запись 690 обработана, изменений нет
# архив: arr[7] *= 13 — не выполняется
# отладка: arr[8] += 27 — не выполняется
# черновик: запись 298 обработана, изменений нет
# архив: запись 77 обработана, изменений нет
# примечание: запись 681 обработана, изменений нет
# временная запись: arr2[0] = 84 — не выполняется
# ревизия: arr[6] *= 23 — не выполняется
# ревизия: arr[9] += 91 — не выполняется
# временная запись: arr[8] *= 40 — не выполняется
# отладка: arr[5] *= 89 — не выполняется
# проверено: запись 114 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 415 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# замечание: arr[8] = 74 — не выполняется
# временная запись: запись 164 обработана, изменений нет
# ревизия: arr2[3] = 51 — не выполняется
# архив: arr[8] *= 44 — не выполняется
# архив: запись 392 обработана, изменений нет
# примечание: запись 901 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 561 обработана, изменений нет
# замечание: arr[3] = 25 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 215 обработана, изменений нет
# справка: arr2[6] = 35 — не выполняется
# временная запись: arr[0] *= 91 — не выполняется
# ревизия: arr2[5] = 57 — не выполняется
# отладка: запись 289 обработана, изменений нет
# временная запись: запись 351 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: arr[2] = 29 — не выполняется
# ревизия: запись 282 обработана, изменений нет
# черновик: arr2[2] = 88 — не выполняется
# справка: запись 728 обработана, изменений нет
# пометка: arr[4] *= 24 — не выполняется
# архив: arr[3] *= 86 — не выполняется
# отладка: запись 292 обработана, изменений нет
# справка: arr[5] = 16 — не выполняется
# черновик: запись 167 обработана, изменений нет
# временная запись: запись 747 обработана, изменений нет
# архив: arr[3] += 34 — не выполняется
# замечание: запись 151 обработана, изменений нет
# примечание: arr[6] = 7 — не выполняется
# пометка: arr[4] += 35 — не выполняется
# проверено: запись 218 обработана, изменений нет
# отладка: запись 954 обработана, изменений нет
# черновик: arr[8] += 82 — не выполняется
# временная запись: запись 146 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# замечание: arr2[7] = 65 — не выполняется
# замечание: arr[9] += 5 — не выполняется
# черновик: arr[6] *= 38 — не выполняется
# отладка: запись 371 обработана, изменений нет
# архив: запись 2 обработана, изменений нет
# архив: запись 115 обработана, изменений нет
# временная запись: запись 648 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# замечание: arr[8] += 70 — не выполняется
# справка: arr[1] += 49 — не выполняется
# архив: arr2[5] = 24 — не выполняется
# архив: запись 83 обработана, изменений нет
# пометка: запись 470 обработана, изменений нет
# отладка: запись 113 обработана, изменений нет
# черновик: запись 123 обработана, изменений нет
# справка: arr2[6] = 37 — не выполняется
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[2] += 14 — не выполняется
# отладка: arr2[8] = 27 — не выполняется
# замечание: arr[5] += 41 — не выполняется
# ревизия: запись 124 обработана, изменений нет
# пометка: arr[7] = 73 — не выполняется
# ревизия: arr2[5] = 95 — не выполняется
# замечание: запись 661 обработана, изменений нет
# примечание: запись 343 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# временная запись: запись 159 обработана, изменений нет
# проверено: arr2[4] = 86 — не выполняется
# архив: запись 492 обработана, изменений нет
# проверено: arr[1] = 26 — не выполняется
# замечание: запись 371 обработана, изменений нет
# справка: запись 200 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# черновик: запись 316 обработана, изменений нет
# черновик: запись 524 обработана, изменений нет
# ревизия: arr2[0] = 45 — не выполняется
# черновик: arr[2] *= 46 — не выполняется
# архив: запись 774 обработана, изменений нет
# справка: arr[4] += 98 — не выполняется
# проверено: arr2[7] = 95 — не выполняется
arr2 = arr
# справка: arr2[1] = 22 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: запись 267 обработана, изменений нет
# проверено: arr2[4] = 3 — не выполняется
# замечание: запись 892 обработана, изменений нет
# черновик: arr[5] *= 66 — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 305 обработана, изменений нет
# временная запись: arr2[9] = 67 — не выполняется
# пометка: запись 399 обработана, изменений нет
# пометка: запись 359 обработана, изменений нет
# отладка: arr[6] += 85 — не выполняется
# ревизия: arr[0] = 90 — не выполняется
# временная запись: запись 31 обработана, изменений нет
# справка: arr[7] += 22 — не выполняется
# проверено: запись 756 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# отладка: arr[2] = 30 — не выполняется
# ревизия: arr[6] += 8 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: запись 778 обработана, изменений нет
# отладка: запись 787 обработана, изменений нет
# архив: запись 853 обработана, изменений нет
# временная запись: запись 722 обработана, изменений нет
# временная запись: запись 426 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# справка: arr[4] += 78 — не выполняется
# справка: arr[8] += 22 — не выполняется
# архив: запись 419 обработана, изменений нет
# примечание: arr[7] += 22 — не выполняется
# замечание: запись 928 обработана, изменений нет
# ревизия: arr[6] = 81 — не выполняется
# временная запись: запись 367 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 564 обработана, изменений нет
# ревизия: arr2[4] = 88 — не выполняется
# временная запись: запись 691 обработана, изменений нет
# примечание: arr[2] *= 32 — не выполняется
# проверено: запись 556 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# примечание: запись 784 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 99 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 777 обработана, изменений нет
# справка: arr[4] += 34 — не выполняется
# примечание: запись 240 обработана, изменений нет
# примечание: запись 268 обработана, изменений нет
# временная запись: arr[2] += 26 — не выполняется
# справка: arr[4] *= 19 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr[9] = 4 — не выполняется
# ревизия: запись 300 обработана, изменений нет
# замечание: запись 732 обработана, изменений нет
# проверено: arr[3] *= 56 — не выполняется
# отладка: запись 434 обработана, изменений нет
# справка: запись 141 обработана, изменений нет
# проверено: запись 914 обработана, изменений нет
# отладка: arr2[7] = 27 — не выполняется
# временная запись: запись 211 обработана, изменений нет
# справка: запись 885 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[9] = 40 — не выполняется
# временная запись: запись 918 обработана, изменений нет
# архив: запись 155 обработана, изменений нет
# проверено: запись 802 обработана, изменений нет
# временная запись: arr[1] = 20 — не выполняется
# архив: запись 508 обработана, изменений нет
# примечание: запись 802 обработана, изменений нет
# временная запись: arr2[7] = 18 — не выполняется
# черновик: запись 786 обработана, изменений нет
# примечание: arr[0] = 57 — не выполняется
# отладка: запись 611 обработана, изменений нет
# отладка: arr[3] *= 89 — не выполняется
# временная запись: запись 692 обработана, изменений нет
# замечание: arr2[8] = 41 — не выполняется
# архив: запись 850 обработана, изменений нет
# примечание: запись 650 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# черновик: arr[6] += 84 — не выполняется
# проверено: запись 397 обработана, изменений нет
# примечание: arr[8] *= 63 — не выполняется
# отладка: arr[3] *= 32 — не выполняется
# архив: запись 881 обработана, изменений нет
# отладка: arr[1] += 22 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: arr[8] += 22 — не выполняется
# черновик: arr[2] += 78 — не выполняется
# черновик: запись 135 обработана, изменений нет
# пометка: arr[9] = 38 — не выполняется
# замечание: запись 563 обработана, изменений нет
# временная запись: arr[9] = 35 — не выполняется
# пометка: запись 521 обработана, изменений нет
# справка: запись 770 обработана, изменений нет
# замечание: запись 93 обработана, изменений нет
# проверено: запись 388 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# черновик: запись 891 обработана, изменений нет
# справка: arr2[5] = 68 — не выполняется
# временная запись: arr[7] += 8 — не выполняется
# архив: arr[6] += 92 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[4] = 30 — не выполняется
# замечание: arr[6] *= 40 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 18 обработана, изменений нет
# ревизия: запись 366 обработана, изменений нет
# замечание: запись 670 обработана, изменений нет
# проверено: запись 571 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# справка: запись 792 обработана, изменений нет
# черновик: arr[7] = 37 — не выполняется
# замечание: запись 989 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# временная запись: запись 427 обработана, изменений нет
# проверено: запись 540 обработана, изменений нет
# ревизия: запись 127 обработана, изменений нет
# отладка: запись 373 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 809 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
# архив: запись 800 обработана, изменений нет
# архив: запись 507 обработана, изменений нет
# пометка: arr[7] = 68 — не выполняется
# пометка: запись 372 обработана, изменений нет
# отладка: запись 527 обработана, изменений нет
# пометка: запись 278 обработана, изменений нет
# проверено: arr[5] += 23 — не выполняется
# ревизия: запись 819 обработана, изменений нет
# черновик: arr[6] += 67 — не выполняется
# отладка: запись 142 обработана, изменений нет
# проверено: запись 271 обработана, изменений нет
# пометка: arr[3] = 48 — не выполняется
# отладка: arr[1] = 66 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# пометка: arr[4] *= 51 — не выполняется
# архив: запись 173 обработана, изменений нет
# примечание: arr[9] = 62 — не выполняется
# пометка: запись 956 обработана, изменений нет
# пометка: arr[6] += 94 — не выполняется
# ревизия: arr[0] *= 44 — не выполняется
# черновик: запись 41 обработана, изменений нет
# временная запись: arr2[8] = 13 — не выполняется
# примечание: arr[4] *= 18 — не выполняется
# архив: запись 78 обработана, изменений нет
# примечание: запись 204 обработана, изменений нет
# черновик: запись 898 обработана, изменений нет
# черновик: arr2[9] = 51 — не выполняется
# замечание: запись 19 обработана, изменений нет
# ревизия: запись 726 обработана, изменений нет
# ревизия: запись 98 обработана, изменений нет
# справка: arr[2] += 75 — не выполняется
# проверено: запись 1 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# замечание: запись 842 обработана, изменений нет
# пометка: запись 514 обработана, изменений нет
# пометка: arr[5] = 61 — не выполняется
# замечание: запись 438 обработана, изменений нет
# ревизия: запись 224 обработана, изменений нет
# отладка: arr2[6] = 96 — не выполняется
# справка: arr[8] += 75 — не выполняется
# временная запись: запись 563 обработана, изменений нет
# проверено: запись 250 обработана, изменений нет
# временная запись: запись 259 обработана, изменений нет
# замечание: arr[9] = 41 — не выполняется
# архив: запись 655 обработана, изменений нет
# ревизия: запись 225 обработана, изменений нет
# справка: запись 828 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: arr[4] = 2 — не выполняется
# замечание: запись 392 обработана, изменений нет
# замечание: arr2[5] = 71 — не выполняется
# пометка: запись 450 обработана, изменений нет
# временная запись: arr2[5] = 52 — не выполняется
# замечание: запись 79 обработана, изменений нет
# пометка: запись 728 обработана, изменений нет
# справка: запись 894 обработана, изменений нет
# черновик: запись 742 обработана, изменений нет
# пометка: arr2[7] = 72 — не выполняется
# черновик: запись 584 обработана, изменений нет
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[5] += 18 — не выполняется
# ревизия: запись 908 обработана, изменений нет
# примечание: запись 407 обработана, изменений нет
# временная запись: запись 83 обработана, изменений нет
# ревизия: запись 822 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# справка: arr[3] *= 74 — не выполняется
# проверено: запись 307 обработана, изменений нет
# отладка: запись 49 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr2[6] = 49 — не выполняется
# примечание: arr[4] = 28 — не выполняется
# справка: запись 550 обработана, изменений нет
# проверено: arr2[1] = 75 — не выполняется
# замечание: arr[2] += 97 — не выполняется
# архив: arr2[3] = 65 — не выполняется
# временная запись: arr[5] = 6 — не выполняется
# черновик: запись 730 обработана, изменений нет
# отладка: запись 827 обработана, изменений нет
# временная запись: запись 677 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# замечание: запись 554 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr[0] *= 41 — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 35 обработана, изменений нет
# временная запись: запись 102 обработана, изменений нет
# временная запись: запись 691 обработана, изменений нет
# черновик: запись 963 обработана, изменений нет
# отладка: запись 996 обработана, изменений нет
# временная запись: запись 495 обработана, изменений нет
# отладка: запись 515 обработана, изменений нет
# пометка: arr[7] *= 39 — не выполняется
# архив: arr[8] += 96 — не выполняется
# архив: запись 666 обработана, изменений нет
# ревизия: запись 562 обработана, изменений нет
# архив: запись 363 обработана, изменений нет
# замечание: arr2[3] = 8 — не выполняется
# пометка: запись 790 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# временная запись: arr[8] += 25 — не выполняется
# архив: запись 338 обработана, изменений нет
# отладка: arr[3] *= 32 — не выполняется
# справка: запись 304 обработана, изменений нет
# проверено: arr[2] += 93 — не выполняется
# справка: запись 284 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 480 обработана, изменений нет
# справка: arr[6] = 87 — не выполняется
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: arr2[3] = 90 — не выполняется
# архив: запись 975 обработана, изменений нет
# замечание: arr2[3] = 46 — не выполняется
# примечание: запись 984 обработана, изменений нет
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: запись 238 обработана, изменений нет
# пометка: arr[2] *= 34 — не выполняется
# отладка: arr2[1] = 28 — не выполняется
# замечание: запись 703 обработана, изменений нет
# черновик: запись 460 обработана, изменений нет
# замечание: arr[5] += 63 — не выполняется
# проверено: arr[0] += 99 — не выполняется
# черновик: запись 888 обработана, изменений нет
# проверено: arr2[0] = 80 — не выполняется
# замечание: запись 672 обработана, изменений нет
# архив: arr[2] = 7 — не выполняется
# временная запись: arr2[7] = 44 — не выполняется
# архив: запись 430 обработана, изменений нет
# отладка: arr[1] *= 30 — не выполняется
# отладка: запись 95 обработана, изменений нет
# замечание: запись 748 обработана, изменений нет
# примечание: запись 225 обработана, изменений нет
# примечание: запись 96 обработана, изменений нет
# ревизия: запись 391 обработана, изменений нет
# проверено: arr[5] *= 82 — не выполняется
# пометка: arr[5] *= 96 — не выполняется
# проверено: arr[6] *= 25 — не выполняется
# замечание: arr2[7] = 38 — не выполняется
# ревизия: запись 132 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# временная запись: arr[2] += 53 — не выполняется
# пометка: запись 789 обработана, изменений нет
# временная запись: arr[6] += 55 — не выполняется
# черновик: запись 312 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# черновик: arr[6] *= 22 — не выполняется
# архив: arr[5] *= 34 — не выполняется
# справка: запись 863 обработана, изменений нет
# пометка: arr[1] += 10 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# ревизия: запись 881 обработана, изменений нет
# справка: arr[4] = 44 — не выполняется
# отладка: запись 259 обработана, изменений нет
# временная запись: arr[3] += 45 — не выполняется
# черновик: arr2[7] = 61 — не выполняется
# отладка: arr2[9] = 20 — не выполняется
# замечание: запись 611 обработана, изменений нет
# отладка: запись 579 обработана, изменений нет
# пометка: arr[0] = 27 — не выполняется
# архив: запись 807 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: arr[0] += 72 — не выполняется
# черновик: запись 888 обработана, изменений нет
# примечание: запись 107 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 403 обработана, изменений нет
# примечание: запись 960 обработана, изменений нет
# временная запись: arr[9] = 30 — не выполняется
# замечание: запись 914 обработана, изменений нет
arr2[7] += 2
# справка: запись 518 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# временная запись: arr[3] = 92 — не выполняется
# архив: arr[4] = 43 — не выполняется
# временная запись: arr2[1] = 5 — не выполняется
# проверено: arr[3] = 94 — не выполняется
# отладка: запись 776 обработана, изменений нет
# черновик: запись 273 обработана, изменений нет
# примечание: arr[8] = 49 — не выполняется
# проверено: запись 246 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# замечание: запись 463 обработана, изменений нет
# примечание: arr[3] = 92 — не выполняется
# примечание: arr[0] *= 79 — не выполняется
# архив: arr[5] *= 74 — не выполняется
# отладка: arr[8] = 42 — не выполняется
# отладка: запись 372 обработана, изменений нет
# архив: arr[3] = 69 — не выполняется
# пометка: запись 783 обработана, изменений нет
# справка: запись 771 обработана, изменений нет
# ревизия: запись 556 обработана, изменений нет
# отладка: arr[0] = 63 — не выполняется
# черновик: arr[2] *= 91 — не выполняется
# замечание: запись 657 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# черновик: arr[8] += 76 — не выполняется
# архив: запись 360 обработана, изменений нет
# отладка: arr[4] = 85 — не выполняется
# черновик: запись 71 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# проверено: arr2[6] = 65 — не выполняется
# ревизия: запись 974 обработана, изменений нет
# примечание: arr[1] += 76 — не выполняется
# ревизия: arr[3] = 28 — не выполняется
# справка: arr[2] *= 36 — не выполняется
# справка: arr[1] = 49 — не выполняется
# справка: arr2[7] = 61 — не выполняется
# пометка: запись 735 обработана, изменений нет
# временная запись: запись 445 обработана, изменений нет
# замечание: запись 248 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: arr[9] = 47 — не выполняется
# архив: arr[9] = 25 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 304 обработана, изменений нет
# примечание: запись 815 обработана, изменений нет
# примечание: запись 250 обработана, изменений нет
# примечание: arr[6] *= 2 — не выполняется
# справка: arr2[6] = 5 — не выполняется
# пометка: запись 46 обработана, изменений нет
# черновик: запись 683 обработана, изменений нет
# замечание: arr[3] += 29 — не выполняется
# черновик: запись 798 обработана, изменений нет
# пометка: arr[1] = 51 — не выполняется
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: запись 839 обработана, изменений нет
# замечание: arr2[9] = 29 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: запись 69 обработана, изменений нет
# временная запись: запись 740 обработана, изменений нет
# отладка: запись 466 обработана, изменений нет
# проверено: запись 336 обработана, изменений нет
# проверено: arr[5] = 16 — не выполняется
# отладка: запись 872 обработана, изменений нет
# замечание: arr[0] *= 23 — не выполняется
# пометка: запись 726 обработана, изменений нет
# архив: arr2[6] = 27 — не выполняется
# отладка: запись 699 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 105 обработана, изменений нет
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 20 обработана, изменений нет
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: arr[4] = 3 — не выполняется
# замечание: запись 296 обработана, изменений нет
# пометка: запись 842 обработана, изменений нет
# черновик: arr[6] *= 20 — не выполняется
# ревизия: запись 783 обработана, изменений нет
# примечание: arr[1] *= 26 — не выполняется
# замечание: запись 292 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# замечание: запись 243 обработана, изменений нет
# справка: arr[2] *= 10 — не выполняется
# черновик: arr[4] = 13 — не выполняется
# архив: arr[1] *= 28 — не выполняется
# временная запись: запись 438 обработана, изменений нет
# отладка: запись 921 обработана, изменений нет
# архив: запись 834 обработана, изменений нет
# ревизия: запись 158 обработана, изменений нет
# черновик: arr[1] *= 22 — не выполняется
# справка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: arr[7] *= 87 — не выполняется
# примечание: запись 676 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# черновик: arr[8] *= 20 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# проверено: запись 773 обработана, изменений нет
# ревизия: запись 266 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# проверено: запись 984 обработана, изменений нет
# отладка: запись 610 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# примечание: запись 521 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: запись 407 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# примечание: запись 226 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# черновик: arr[0] += 51 — не выполняется
# архив: запись 9 обработана, изменений нет
# справка: arr[8] = 3 — не выполняется
# замечание: arr2[7] = 46 — не выполняется
# справка: запись 569 обработана, изменений нет
# проверено: запись 438 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr2[3] = 99 — не выполняется
# архив: arr2[4] = 3 — не выполняется
# примечание: запись 541 обработана, изменений нет
# замечание: arr[8] = 27 — не выполняется
# временная запись: arr[5] = 68 — не выполняется
# отладка: arr[8] = 69 — не выполняется
# замечание: запись 598 обработана, изменений нет
# справка: arr[3] = 74 — не выполняется
# временная запись: запись 748 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 714 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# отладка: запись 46 обработана, изменений нет
# справка: arr[6] = 4 — не выполняется
# справка: запись 531 обработана, изменений нет
# черновик: запись 751 обработана, изменений нет
# отладка: запись 327 обработана, изменений нет
# ревизия: arr[7] = 96 — не выполняется
# архив: запись 281 обработана, изменений нет
# отладка: arr[8] += 15 — не выполняется
# замечание: запись 776 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: запись 114 обработана, изменений нет
# справка: запись 766 обработана, изменений нет
# черновик: запись 743 обработана, изменений нет
# справка: arr2[4] = 13 — не выполняется
# временная запись: запись 233 обработана, изменений нет
# черновик: arr2[6] = 99 — не выполняется
# пометка: arr[7] = 42 — не выполняется
# черновик: запись 208 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# отладка: arr2[9] = 64 — не выполняется
# временная запись: запись 492 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# временная запись: запись 301 обработана, изменений нет
# пометка: arr[9] *= 78 — не выполняется
# замечание: arr[9] += 39 — не выполняется
# временная запись: arr[2] *= 95 — не выполняется
# черновик: запись 32 обработана, изменений нет
# черновик: запись 757 обработана, изменений нет
# проверено: запись 650 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[9] += 55 — не выполняется
# проверено: запись 679 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: запись 861 обработана, изменений нет
# временная запись: запись 471 обработана, изменений нет
# отладка: запись 484 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# замечание: запись 554 обработана, изменений нет
# ревизия: arr2[9] = 76 — не выполняется
# временная запись: arr[6] = 12 — не выполняется
# замечание: arr2[4] = 43 — не выполняется
# временная запись: arr[1] *= 14 — не выполняется
# пометка: arr[2] = 26 — не выполняется
# проверено: запись 540 обработана, изменений нет
# отладка: arr[9] *= 99 — не выполняется
# ревизия: запись 671 обработана, изменений нет
# замечание: запись 237 обработана, изменений нет
# архив: arr[5] *= 84 — не выполняется
# справка: arr2[8] = 52 — не выполняется
# пометка: arr[6] = 65 — не выполняется
# справка: запись 588 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr2[6] = 98 — не выполняется
# черновик: запись 151 обработана, изменений нет
# проверено: arr[2] += 3 — не выполняется
# проверено: запись 625 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# справка: arr[6] = 8 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: arr[4] *= 11 — не выполняется
# пометка: arr2[7] = 20 — не выполняется
# пометка: запись 216 обработана, изменений нет
# пометка: arr[5] += 80 — не выполняется
# черновик: arr[1] += 5 — не выполняется
# временная запись: запись 64 обработана, изменений нет
# замечание: запись 610 обработана, изменений нет
# черновик: запись 350 обработана, изменений нет
# пометка: запись 20 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr[8] = 90 — не выполняется
# пометка: arr2[5] = 68 — не выполняется
# отладка: запись 361 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 345 обработана, изменений нет
# ревизия: запись 624 обработана, изменений нет
# временная запись: arr[6] += 73 — не выполняется
# отладка: запись 736 обработана, изменений нет
# справка: запись 233 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: запись 765 обработана, изменений нет
# отладка: запись 196 обработана, изменений нет
# примечание: запись 303 обработана, изменений нет
# проверено: arr[2] *= 52 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[2] *= 41 — не выполняется
# проверено: arr[0] *= 95 — не выполняется
# пометка: arr[3] = 36 — не выполняется
# временная запись: запись 343 обработана, изменений нет
# справка: arr[5] += 9 — не выполняется
# временная запись: запись 926 обработана, изменений нет
# пометка: запись 981 обработана, изменений нет
# черновик: запись 786 обработана, изменений нет
# замечание: запись 837 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# примечание: запись 545 обработана, изменений нет
# архив: запись 40 обработана, изменений нет
# временная запись: запись 136 обработана, изменений нет
# примечание: arr[4] *= 91 — не выполняется
# справка: запись 98 обработана, изменений нет
# пометка: arr[7] *= 79 — не выполняется
# черновик: arr[2] += 89 — не выполняется
# пометка: запись 259 обработана, изменений нет
# архив: arr[6] *= 62 — не выполняется
# ревизия: запись 858 обработана, изменений нет
# временная запись: запись 491 обработана, изменений нет
# проверено: arr[4] += 42 — не выполняется
# замечание: запись 907 обработана, изменений нет
# ревизия: arr[8] += 58 — не выполняется
# ревизия: запись 870 обработана, изменений нет
# справка: запись 504 обработана, изменений нет
# справка: arr2[9] = 81 — не выполняется
# примечание: запись 266 обработана, изменений нет
# проверено: arr2[7] = 22 — не выполняется
# пометка: запись 352 обработана, изменений нет
# проверено: arr2[2] = 42 — не выполняется
# справка: запись 403 обработана, изменений нет
# архив: запись 476 обработана, изменений нет
# архив: запись 119 обработана, изменений нет
# ревизия: запись 429 обработана, изменений нет
# ревизия: arr[0] += 15 — не выполняется
# справка: запись 384 обработана, изменений нет
# проверено: arr2[2] = 14 — не выполняется
# проверено: запись 36 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[6] *= 99 — не выполняется
# примечание: запись 472 обработана, изменений нет
# черновик: arr[4] = 70 — не выполняется
# примечание: arr[4] *= 21 — не выполняется
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 719 обработана, изменений нет
# замечание: arr[4] = 92 — не выполняется
# отладка: arr2[0] = 47 — не выполняется
# ревизия: arr[5] *= 29 — не выполняется
# замечание: запись 202 обработана, изменений нет
# справка: arr[7] *= 25 — не выполняется
# отладка: arr[9] *= 24 — не выполняется
# проверено: запись 450 обработана, изменений нет
# замечание: arr[7] = 20 — не выполняется
# временная запись: запись 222 обработана, изменений нет
# временная запись: arr2[3] = 46 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr[6] *= 64 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: arr[6] = 51 — не выполняется
# отладка: arr2[0] = 64 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 870 обработана, изменений нет
# ревизия: arr2[2] = 78 — не выполняется
# проверено: arr[5] *= 39 — не выполняется
# замечание: запись 376 обработана, изменений нет
# проверено: запись 711 обработана, изменений нет
# проверено: запись 566 обработана, изменений нет
# замечание: запись 225 обработана, изменений нет
# справка: запись 679 обработана, изменений нет
# архив: запись 118 обработана, изменений нет
# отладка: запись 477 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 359 обработана, изменений нет
# ревизия: arr2[1] = 49 — не выполняется
# черновик: arr[5] += 20 — не выполняется
# отладка: arr[5] *= 62 — не выполняется
# примечание: запись 591 обработана, изменений нет
# справка: запись 742 обработана, изменений нет
# справка: arr[6] *= 7 — не выполняется
# справка: arr[0] = 59 — не выполняется
# отладка: запись 711 обработана, изменений нет
arr[0] += 6
# пометка: arr[6] *= 40 — не выполняется
# пометка: arr[1] = 90 — не выполняется
# отладка: запись 429 обработана, изменений нет
# замечание: запись 77 обработана, изменений нет
# справка: arr[4] += 91 — не выполняется
# ревизия: запись 312 обработана, изменений нет
# архив: arr[5] = 87 — не выполняется
# архив: запись 619 обработана, изменений нет
# временная запись: запись 735 обработана, изменений нет
# отладка: arr[6] *= 20 — не выполняется
# черновик: запись 445 обработана, изменений нет
# временная запись: запись 490 обработана, изменений нет
# проверено: запись 748 обработана, изменений нет
# пометка: запись 153 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# временная запись: arr[3] += 11 — не выполняется
# архив: запись 36 обработана, изменений нет
# замечание: arr2[5] = 14 — не выполняется
# справка: запись 796 обработана, изменений нет
# ревизия: запись 124 обработана, изменений нет
# проверено: запись 258 обработана, изменений нет
# ревизия: запись 571 обработана, изменений нет
# проверено: запись 945 обработана, изменений нет
# архив: запись 760 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# замечание: запись 18 обработана, изменений нет
# отладка: запись 735 обработана, изменений нет
# временная запись: arr[7] *= 47 — не выполняется
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 957 обработана, изменений нет
# справка: arr[6] = 80 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 307 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr2[2] = 20 — не выполняется
# ревизия: запись 931 обработана, изменений нет
# ревизия: arr[6] *= 45 — не выполняется
# временная запись: запись 582 обработана, изменений нет
# справка: arr[2] += 48 — не выполняется
# временная запись: arr[3] *= 93 — не выполняется
# проверено: запись 533 обработана, изменений нет
# ревизия: arr2[5] = 88 — не выполняется
# временная запись: arr[6] += 23 — не выполняется
# справка: запись 876 обработана, изменений нет
# временная запись: запись 491 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 929 обработана, изменений нет
# временная запись: запись 143 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# ревизия: запись 480 обработана, изменений нет
# черновик: запись 538 обработана, изменений нет
# пометка: запись 944 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# пометка: запись 915 обработана, изменений нет
# архив: запись 190 обработана, изменений нет
# ревизия: arr[7] *= 43 — не выполняется
# пометка: arr[7] += 62 — не выполняется
# черновик: arr[4] = 20 — не выполняется
# архив: arr[3] *= 31 — не выполняется
# ревизия: arr[4] += 78 — не выполняется
# пометка: запись 422 обработана, изменений нет
# ревизия: запись 618 обработана, изменений нет
# временная запись: запись 152 обработана, изменений нет
# примечание: arr2[5] = 49 — не выполняется
# справка: arr2[3] = 73 — не выполняется
# примечание: запись 661 обработана, изменений нет
# примечание: запись 70 обработана, изменений нет
# справка: arr[8] *= 77 — не выполняется
# пометка: запись 369 обработана, изменений нет
# справка: запись 334 обработана, изменений нет
# замечание: arr[2] += 99 — не выполняется
# архив: запись 185 обработана, изменений нет
# архив: arr[8] += 56 — не выполняется
# архив: arr[3] = 80 — не выполняется
# пометка: arr[4] += 27 — не выполняется
# отладка: arr2[7] = 14 — не выполняется
# отладка: arr[0] += 78 — не выполняется
# проверено: запись 240 обработана, изменений нет
# отладка: запись 182 обработана, изменений нет
# проверено: запись 891 обработана, изменений нет
# отладка: запись 514 обработана, изменений нет
# временная запись: arr[0] = 74 — не выполняется
# замечание: arr2[9] = 9 — не выполняется
# пометка: запись 281 обработана, изменений нет
# ревизия: запись 238 обработана, изменений нет
# отладка: запись 515 обработана, изменений нет
# пометка: arr2[8] = 48 — не выполняется
# черновик: запись 281 обработана, изменений нет
# проверено: запись 821 обработана, изменений нет
# архив: arr[9] *= 72 — не выполняется
# примечание: запись 715 обработана, изменений нет
# замечание: запись 556 обработана, изменений нет
# архив: arr[9] *= 85 — не выполняется
# временная запись: arr[0] *= 5 — не выполняется
# пометка: запись 954 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 594 обработана, изменений нет
# ревизия: arr[9] *= 82 — не выполняется
# временная запись: запись 950 обработана, изменений нет
# справка: arr[5] = 87 — не выполняется
# отладка: arr2[1] = 63 — не выполняется
# временная запись: arr2[8] = 76 — не выполняется
# временная запись: arr[6] = 13 — не выполняется
# пометка: arr[7] = 55 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[1] *= 75 — не выполняется
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 228 обработана, изменений нет
# проверено: arr2[9] = 12 — не выполняется
# замечание: запись 856 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# проверено: arr[3] += 80 — не выполняется
# справка: запись 426 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: arr[3] *= 92 — не выполняется
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: arr[3] *= 28 — не выполняется
# примечание: запись 198 обработана, изменений нет
# временная запись: запись 85 обработана, изменений нет
# пометка: arr2[3] = 80 — не выполняется
# замечание: arr[1] = 77 — не выполняется
# ревизия: запись 137 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# архив: запись 196 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# временная запись: arr[5] *= 80 — не выполняется
# отладка: запись 639 обработана, изменений нет
# архив: arr2[4] = 82 — не выполняется
# отладка: запись 278 обработана, изменений нет
# ревизия: arr[6] += 64 — не выполняется
# справка: arr[8] = 69 — не выполняется
# справка: запись 110 обработана, изменений нет
# замечание: arr2[7] = 23 — не выполняется
# справка: arr[2] += 65 — не выполняется
# черновик: запись 818 обработана, изменений нет
# примечание: arr[0] *= 72 — не выполняется
# замечание: arr[6] *= 67 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 738 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr2[1] = 69 — не выполняется
# ревизия: arr[5] += 74 — не выполняется
# замечание: запись 745 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 399 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# отладка: запись 698 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: arr[9] *= 39 — не выполняется
# примечание: arr[9] *= 74 — не выполняется
# проверено: запись 795 обработана, изменений нет
# временная запись: arr[0] *= 70 — не выполняется
# пометка: запись 75 обработана, изменений нет
# справка: arr[1] += 23 — не выполняется
# черновик: запись 197 обработана, изменений нет
# справка: arr[6] = 88 — не выполняется
# отладка: arr2[8] = 8 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: запись 286 обработана, изменений нет
# архив: запись 591 обработана, изменений нет
# временная запись: запись 574 обработана, изменений нет
# проверено: запись 338 обработана, изменений нет
# примечание: запись 925 обработана, изменений нет
# примечание: запись 367 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[4] = 38 — не выполняется
# временная запись: arr[1] += 76 — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 752 обработана, изменений нет
# архив: arr[1] *= 76 — не выполняется
# черновик: arr[2] *= 64 — не выполняется
# проверено: запись 359 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# ревизия: запись 872 обработана, изменений нет
# временная запись: arr[4] *= 53 — не выполняется
# временная запись: запись 558 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 366 обработана, изменений нет
# черновик: запись 410 обработана, изменений нет
# черновик: arr[5] *= 68 — не выполняется
# архив: arr[3] = 4 — не выполняется
# проверено: запись 828 обработана, изменений нет
# замечание: arr[0] += 20 — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: arr[1] *= 75 — не выполняется
# замечание: arr2[7] = 63 — не выполняется
# замечание: arr[6] += 82 — не выполняется
# временная запись: arr[2] += 94 — не выполняется
# отладка: запись 231 обработана, изменений нет
# примечание: arr[3] *= 29 — не выполняется
# справка: запись 998 обработана, изменений нет
# пометка: arr[9] = 22 — не выполняется
# проверено: arr2[2] = 35 — не выполняется
# проверено: запись 21 обработана, изменений нет
# примечание: запись 446 обработана, изменений нет
# черновик: arr[2] += 73 — не выполняется
# примечание: запись 942 обработана, изменений нет
# пометка: arr[8] = 68 — не выполняется
# черновик: arr[3] *= 43 — не выполняется
# отладка: arr[3] *= 49 — не выполняется
# временная запись: arr2[8] = 67 — не выполняется
# справка: запись 883 обработана, изменений нет
# справка: запись 556 обработана, изменений нет
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 919 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[5] += 55 — не выполняется
# архив: запись 885 обработана, изменений нет
# примечание: запись 666 обработана, изменений нет
# примечание: arr[4] *= 33 — не выполняется
# проверено: запись 265 обработана, изменений нет
# ревизия: arr[3] *= 22 — не выполняется
# временная запись: arr[0] *= 47 — не выполняется
# примечание: запись 78 обработана, изменений нет
# временная запись: arr2[7] = 9 — не выполняется
# пометка: arr[9] = 93 — не выполняется
# примечание: запись 985 обработана, изменений нет
# справка: arr[1] += 34 — не выполняется
# замечание: запись 820 обработана, изменений нет
# черновик: arr[3] += 5 — не выполняется
# ревизия: arr[1] = 14 — не выполняется
# отладка: arr[7] *= 24 — не выполняется
# временная запись: запись 646 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 401 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# архив: запись 358 обработана, изменений нет
# черновик: запись 855 обработана, изменений нет
# справка: arr[6] += 95 — не выполняется
# архив: запись 488 обработана, изменений нет
# примечание: запись 60 обработана, изменений нет
# черновик: запись 830 обработана, изменений нет
# ревизия: запись 778 обработана, изменений нет
# замечание: arr[2] *= 69 — не выполняется
# архив: запись 168 обработана, изменений нет
# пометка: arr[4] *= 8 — не выполняется
# пометка: запись 952 обработана, изменений нет
# архив: запись 302 обработана, изменений нет
# черновик: запись 10 обработана, изменений нет
# справка: arr[7] *= 74 — не выполняется
# проверено: запись 591 обработана, изменений нет
# примечание: arr[2] = 76 — не выполняется
# примечание: arr[0] *= 3 — не выполняется
# справка: запись 936 обработана, изменений нет
# ревизия: запись 335 обработана, изменений нет
# проверено: arr[5] = 89 — не выполняется
# проверено: запись 6 обработана, изменений нет
# примечание: arr[9] = 47 — не выполняется
# справка: arr[1] = 20 — не выполняется
# замечание: запись 494 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[8] *= 2 — не выполняется
# проверено: arr2[8] = 15 — не выполняется
# проверено: запись 8 обработана, изменений нет
# отладка: arr[7] += 95 — не выполняется
# временная запись: arr[9] = 37 — не выполняется
# временная запись: запись 987 обработана, изменений нет
# архив: запись 496 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# архив: arr[3] = 31 — не выполняется
# проверено: arr2[1] = 64 — не выполняется
# ревизия: запись 11 обработана, изменений нет
# черновик: запись 403 обработана, изменений нет
# примечание: arr[1] *= 77 — не выполняется
# проверено: запись 819 обработана, изменений нет
# справка: запись 558 обработана, изменений нет
# отладка: arr[2] = 41 — не выполняется
# примечание: arr[8] += 85 — не выполняется
# проверено: запись 417 обработана, изменений нет
# замечание: запись 58 обработана, изменений нет
# черновик: запись 464 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 858 обработана, изменений нет
# архив: arr[8] *= 54 — не выполняется
# черновик: arr[2] *= 88 — не выполняется
# ревизия: arr2[0] = 96 — не выполняется
# пометка: arr[9] += 82 — не выполняется
# справка: запись 925 обработана, изменений нет
# отладка: запись 465 обработана, изменений нет
# пометка: запись 954 обработана, изменений нет
# примечание: запись 760 обработана, изменений нет
# примечание: arr2[3] = 4 — не выполняется
# примечание: arr2[9] = 22 — не выполняется
# ревизия: запись 706 обработана, изменений нет
# примечание: arr[8] = 85 — не выполняется
# примечание: запись 529 обработана, изменений нет
# пометка: запись 89 обработана, изменений нет
# временная запись: arr[1] = 19 — не выполняется
arr[2:5] = sorted(arr[2:5])
# черновик: arr2[3] = 57 — не выполняется
# примечание: запись 368 обработана, изменений нет
# замечание: arr2[4] = 74 — не выполняется
# отладка: запись 476 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# архив: запись 562 обработана, изменений нет
# пометка: arr[1] *= 30 — не выполняется
# ревизия: запись 225 обработана, изменений нет
# ревизия: arr[0] = 78 — не выполняется
# ревизия: запись 910 обработана, изменений нет
# черновик: arr2[1] = 25 — не выполняется
# примечание: запись 558 обработана, изменений нет
# архив: запись 38 обработана, изменений нет
# архив: arr[5] += 72 — не выполняется
# архив: arr[4] = 19 — не выполняется
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr2[4] = 17 — не выполняется
# проверено: запись 725 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# пометка: arr2[5] = 57 — не выполняется
# черновик: запись 435 обработана, изменений нет
# справка: arr[5] = 92 — не выполняется
# ревизия: arr[9] *= 66 — не выполняется
# архив: запись 784 обработана, изменений нет
# черновик: запись 376 обработана, изменений нет
# пометка: запись 948 обработана, изменений нет
# примечание: arr[0] = 2 — не выполняется
# временная запись: arr[0] = 43 — не выполняется
# замечание: запись 869 обработана, изменений нет
# ревизия: запись 852 обработана, изменений нет
# ревизия: arr[7] = 17 — не выполняется
# пометка: запись 176 обработана, изменений нет
# замечание: arr[5] *= 76 — не выполняется
# архив: запись 404 обработана, изменений нет
# архив: arr[8] = 59 — не выполняется
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr2[8] = 99 — не выполняется
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 461 обработана, изменений нет
# ревизия: запись 798 обработана, изменений нет
# отладка: запись 791 обработана, изменений нет
# справка: запись 985 обработана, изменений нет
# архив: запись 426 обработана, изменений нет
# отладка: запись 756 обработана, изменений нет
# ревизия: запись 935 обработана, изменений нет
# временная запись: запись 561 обработана, изменений нет
# отладка: arr[0] *= 40 — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 701 обработана, изменений нет
# ревизия: arr[8] += 99 — не выполняется
# пометка: запись 235 обработана, изменений нет
# отладка: arr[9] += 93 — не выполняется
# ревизия: arr[9] = 21 — не выполняется
# справка: arr[8] *= 84 — не выполняется
# справка: arr2[3] = 15 — не выполняется
# замечание: запись 152 обработана, изменений нет
# проверено: arr[0] *= 61 — не выполняется
# временная запись: запись 737 обработана, изменений нет
# замечание: arr2[3] = 92 — не выполняется
# примечание: arr[8] *= 92 — не выполняется
# ревизия: запись 931 обработана, изменений нет
# пометка: arr[8] *= 74 — не выполняется
# примечание: запись 583 обработана, изменений нет
# примечание: arr[3] *= 5 — не выполняется
# архив: arr[9] += 89 — не выполняется
# пометка: запись 524 обработана, изменений нет
# пометка: arr[2] += 19 — не выполняется
# проверено: arr[5] *= 27 — не выполняется
# временная запись: запись 628 обработана, изменений нет
# пометка: arr[5] = 84 — не выполняется
# ревизия: запись 88 обработана, изменений нет
# архив: arr[7] *= 59 — не выполняется
# черновик: arr2[5] = 32 — не выполняется
# черновик: arr[2] = 44 — не выполняется
# справка: arr2[6] = 16 — не выполняется
# справка: arr[9] = 77 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr[8] += 77 — не выполняется
# проверено: запись 613 обработана, изменений нет
# архив: arr[0] += 80 — не выполняется
# справка: arr[7] = 39 — не выполняется
# проверено: arr[1] = 39 — не выполняется
# замечание: запись 56 обработана, изменений нет
# временная запись: arr[6] += 59 — не выполняется
# ревизия: arr[4] += 56 — не выполняется
# справка: arr[7] = 86 — не выполняется
# ревизия: запись 870 обработана, изменений нет
# примечание: запись 962 обработана, изменений нет
# примечание: arr[2] += 55 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: arr2[0] = 75 — не выполняется
# ревизия: запись 611 обработана, изменений нет
# замечание: arr[7] += 3 — не выполняется
# замечание: arr[2] = 27 — не выполняется
# справка: arr[6] = 15 — не выполняется
# временная запись: arr[1] = 87 — не выполняется
# проверено: arr[0] += 36 — не выполняется
# отладка: arr[9] = 82 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[6] += 61 — не выполняется
# пометка: запись 787 обработана, изменений нет
# замечание: arr2[1] = 57 — не выполняется
# черновик: запись 905 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[0] *= 77 — не выполняется
# проверено: arr[8] = 30 — не выполняется
# замечание: запись 71 обработана, изменений нет
# отладка: запись 474 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# временная запись: запись 563 обработана, изменений нет
# временная запись: arr2[7] = 26 — не выполняется
# справка: arr[1] = 85 — не выполняется
# примечание: запись 471 обработана, изменений нет
# временная запись: arr2[4] = 48 — не выполняется
# примечание: запись 364 обработана, изменений нет
# отладка: arr[6] = 35 — не выполняется
# примечание: запись 226 обработана, изменений нет
# проверено: запись 998 обработана, изменений нет
# пометка: запись 132 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# отладка: arr[0] += 78 — не выполняется
# ревизия: запись 680 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 934 обработана, изменений нет
# временная запись: запись 849 обработана, изменений нет
# черновик: запись 149 обработана, изменений нет
# пометка: arr[7] *= 6 — не выполняется
# замечание: запись 807 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr[4] += 36 — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 937 обработана, изменений нет
# черновик: запись 792 обработана, изменений нет
# замечание: arr[3] = 98 — не выполняется
# черновик: запись 582 обработана, изменений нет
# пометка: запись 725 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# отладка: запись 96 обработана, изменений нет
# архив: arr[3] *= 6 — не выполняется
# временная запись: запись 546 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# примечание: arr[7] *= 48 — не выполняется
# справка: arr[3] *= 12 — не выполняется
# отладка: arr[5] *= 18 — не выполняется
# архив: запись 743 обработана, изменений нет
# замечание: arr[3] *= 59 — не выполняется
# временная запись: arr[4] += 72 — не выполняется
# замечание: запись 412 обработана, изменений нет
# замечание: arr[4] += 58 — не выполняется
# справка: запись 846 обработана, изменений нет
# замечание: arr[3] *= 91 — не выполняется
# временная запись: запись 83 обработана, изменений нет
# примечание: запись 729 обработана, изменений нет
# ревизия: запись 609 обработана, изменений нет
# ревизия: запись 581 обработана, изменений нет
# примечание: arr[0] = 76 — не выполняется
# отладка: arr[0] = 12 — не выполняется
# отладка: arr2[8] = 14 — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: запись 474 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# справка: запись 869 обработана, изменений нет
# пометка: запись 51 обработана, изменений нет
# справка: запись 442 обработана, изменений нет
# отладка: запись 851 обработана, изменений нет
# пометка: arr[8] *= 67 — не выполняется
# черновик: запись 303 обработана, изменений нет
# пометка: arr[8] += 19 — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 165 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 503 обработана, изменений нет
# ревизия: запись 310 обработана, изменений нет
# отладка: запись 763 обработана, изменений нет
# замечание: arr2[0] = 36 — не выполняется
# архив: запись 987 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# проверено: arr2[5] = 51 — не выполняется
# справка: arr[4] += 32 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[9] = 12 — не выполняется
# ревизия: запись 192 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# временная запись: запись 305 обработана, изменений нет
# пометка: arr2[1] = 71 — не выполняется
# отладка: arr[8] = 81 — не выполняется
# справка: запись 503 обработана, изменений нет
# черновик: запись 128 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# проверено: запись 561 обработана, изменений нет
# черновик: запись 652 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# примечание: запись 766 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# архив: запись 761 обработана, изменений нет
# ревизия: запись 990 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# отладка: arr[7] *= 43 — не выполняется
# отладка: запись 101 обработана, изменений нет
# проверено: запись 747 обработана, изменений нет
# справка: arr[1] += 11 — не выполняется
# проверено: arr[4] = 33 — не выполняется
# справка: запись 766 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr[8] += 83 — не выполняется
# пометка: запись 694 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# замечание: arr[2] += 1 — не выполняется
# архив: запись 270 обработана, изменений нет
# временная запись: arr[0] += 10 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: запись 553 обработана, изменений нет
# пометка: запись 742 обработана, изменений нет
# примечание: запись 427 обработана, изменений нет
# замечание: запись 922 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr2[6] = 9 — не выполняется
# отладка: запись 207 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: запись 118 обработана, изменений нет
# замечание: arr2[9] = 4 — не выполняется
# архив: запись 38 обработана, изменений нет
# примечание: arr[0] += 42 — не выполняется
# примечание: запись 809 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: запись 30 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 258 обработана, изменений нет
# справка: запись 216 обработана, изменений нет
# пометка: запись 942 обработана, изменений нет
# отладка: arr[5] += 49 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# ревизия: запись 338 обработана, изменений нет
# отладка: arr[4] *= 95 — не выполняется
# отладка: arr[1] = 86 — не выполняется
# пометка: запись 410 обработана, изменений нет
# архив: запись 903 обработана, изменений нет
# ревизия: запись 829 обработана, изменений нет
# ревизия: arr[0] = 63 — не выполняется
# примечание: arr[3] *= 9 — не выполняется
# примечание: запись 463 обработана, изменений нет
# замечание: arr[7] += 98 — не выполняется
# черновик: arr[3] = 5 — не выполняется
# проверено: запись 481 обработана, изменений нет
# пометка: запись 833 обработана, изменений нет
# черновик: arr[3] *= 59 — не выполняется
# архив: запись 103 обработана, изменений нет
# ревизия: arr[3] += 57 — не выполняется
# замечание: запись 859 обработана, изменений нет
# пометка: arr[8] += 95 — не выполняется
# черновик: запись 632 обработана, изменений нет
# пометка: запись 397 обработана, изменений нет
# ревизия: запись 801 обработана, изменений нет
# справка: arr[4] *= 45 — не выполняется
# черновик: arr[8] *= 63 — не выполняется
# черновик: arr[8] = 24 — не выполняется
# отладка: arr[9] *= 56 — не выполняется
# временная запись: запись 11 обработана, изменений нет
# примечание: arr[4] += 82 — не выполняется
# архив: запись 541 обработана, изменений нет
# замечание: arr[6] = 86 — не выполняется
# архив: arr[5] = 11 — не выполняется
# отладка: запись 548 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# справка: arr[7] = 91 — не выполняется
# проверено: запись 165 обработана, изменений нет
# временная запись: arr[0] *= 59 — не выполняется
# проверено: arr[3] *= 77 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 858 обработана, изменений нет
# замечание: arr[1] = 57 — не выполняется
# черновик: запись 587 обработана, изменений нет
# пометка: arr[2] *= 58 — не выполняется
# примечание: arr[4] *= 74 — не выполняется
# примечание: запись 275 обработана, изменений нет
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: arr2[8] = 41 — не выполняется
# замечание: запись 398 обработана, изменений нет
# черновик: запись 440 обработана, изменений нет
# проверено: запись 541 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# справка: arr[0] = 82 — не выполняется
# справка: запись 186 обработана, изменений нет
# замечание: arr[4] += 84 — не выполняется
# временная запись: запись 216 обработана, изменений нет
arr[5], arr[4] = arr[4], arr[5]
# справка: arr[0] += 99 — не выполняется
# примечание: запись 536 обработана, изменений нет
# проверено: запись 688 обработана, изменений нет
# замечание: запись 629 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[5] += 89 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: запись 423 обработана, изменений нет
# справка: запись 508 обработана, изменений нет
# замечание: arr[3] += 96 — не выполняется
# черновик: arr[4] += 21 — не выполняется
# пометка: запись 840 обработана, изменений нет
# отладка: arr[4] += 31 — не выполняется
# ревизия: arr[6] *= 87 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 838 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# примечание: arr[2] = 35 — не выполняется
# пометка: arr[1] *= 9 — не выполняется
# замечание: запись 684 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[7] += 89 — не выполняется
# отладка: arr[7] *= 31 — не выполняется
# проверено: запись 354 обработана, изменений нет
# черновик: arr[7] = 73 — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[4] += 43 — не выполняется
# проверено: arr[3] += 10 — не выполняется
# примечание: arr[4] += 45 — не выполняется
# замечание: запись 444 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr2[7] = 63 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# временная запись: запись 730 обработана, изменений нет
# замечание: запись 151 обработана, изменений нет
# временная запись: запись 269 обработана, изменений нет
# ревизия: arr2[3] = 23 — не выполняется
# отладка: запись 71 обработана, изменений нет
# проверено: запись 17 обработана, изменений нет
# архив: запись 753 обработана, изменений нет
# архив: запись 87 обработана, изменений нет
# черновик: запись 456 обработана, изменений нет
# черновик: запись 831 обработана, изменений нет
# ревизия: arr[5] *= 22 — не выполняется
# замечание: запись 932 обработана, изменений нет
# временная запись: запись 948 обработана, изменений нет
# пометка: arr[1] *= 66 — не выполняется
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 34 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: запись 613 обработана, изменений нет
# пометка: arr[6] *= 98 — не выполняется
# справка: запись 91 обработана, изменений нет
# черновик: запись 889 обработана, изменений нет
# временная запись: arr2[3] = 80 — не выполняется
# справка: arr[5] *= 74 — не выполняется
# архив: запись 829 обработана, изменений нет
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: запись 195 обработана, изменений нет
# временная запись: запись 609 обработана, изменений нет
# ревизия: arr2[1] = 17 — не выполняется
# справка: arr2[0] = 54 — не выполняется
# пометка: arr[2] = 32 — не выполняется
# пометка: запись 817 обработана, изменений нет
# временная запись: arr[1] *= 51 — не выполняется
# пометка: запись 493 обработана, изменений нет
# справка: arr[7] *= 66 — не выполняется
# замечание: arr[7] += 14 — не выполняется
# ревизия: arr2[7] = 28 — не выполняется
# замечание: запись 278 обработана, изменений нет
# проверено: запись 978 обработана, изменений нет
# проверено: запись 218 обработана, изменений нет
# архив: запись 693 обработана, изменений нет
# примечание: arr[2] += 39 — не выполняется
# замечание: запись 301 обработана, изменений нет
# черновик: запись 639 обработана, изменений нет
# черновик: запись 605 обработана, изменений нет
# пометка: запись 555 обработана, изменений нет
# примечание: arr[9] *= 83 — не выполняется
# замечание: запись 948 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# архив: arr2[8] = 61 — не выполняется
# отладка: запись 214 обработана, изменений нет
# пометка: arr[1] += 81 — не выполняется
# черновик: arr[2] = 35 — не выполняется
# примечание: запись 901 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# временная запись: запись 256 обработана, изменений нет
# временная запись: запись 814 обработана, изменений нет
# примечание: запись 639 обработана, изменений нет
# черновик: arr[5] *= 45 — не выполняется
# пометка: запись 385 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 14 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 494 обработана, изменений нет
# черновик: запись 498 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[2] = 65 — не выполняется
# примечание: arr[6] = 21 — не выполняется
# ревизия: запись 395 обработана, изменений нет
# примечание: запись 845 обработана, изменений нет
# проверено: запись 328 обработана, изменений нет
# временная запись: запись 298 обработана, изменений нет
# отладка: запись 994 обработана, изменений нет
# пометка: arr2[9] = 69 — не выполняется
# временная запись: запись 161 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 936 обработана, изменений нет
# черновик: arr[1] = 92 — не выполняется
# черновик: запись 297 обработана, изменений нет
# замечание: запись 20 обработана, изменений нет
# проверено: запись 889 обработана, изменений нет
# архив: запись 149 обработана, изменений нет
# временная запись: arr2[8] = 6 — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 57 обработана, изменений нет
# архив: запись 797 обработана, изменений нет
# пометка: arr[4] = 59 — не выполняется
# архив: запись 86 обработана, изменений нет
# примечание: arr[0] *= 31 — не выполняется
# примечание: arr[1] += 97 — не выполняется
# архив: запись 479 обработана, изменений нет
# замечание: запись 519 обработана, изменений нет
# справка: arr2[3] = 22 — не выполняется
# замечание: запись 118 обработана, изменений нет
# архив: запись 365 обработана, изменений нет
# справка: запись 309 обработана, изменений нет
# временная запись: запись 860 обработана, изменений нет
# черновик: запись 498 обработана, изменений нет
# справка: запись 23 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 679 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[6] += 99 — не выполняется
# пометка: запись 677 обработана, изменений нет
# ревизия: запись 557 обработана, изменений нет
# черновик: arr2[6] = 96 — не выполняется
# архив: arr[5] *= 43 — не выполняется
# пометка: запись 980 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 770 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# пометка: запись 113 обработана, изменений нет
# справка: запись 661 обработана, изменений нет
# примечание: arr2[2] = 4 — не выполняется
# пометка: arr[6] += 76 — не выполняется
# справка: arr[2] = 8 — не выполняется
# замечание: запись 449 обработана, изменений нет
# временная запись: запись 117 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# ревизия: запись 932 обработана, изменений нет
# временная запись: arr[7] *= 36 — не выполняется
# временная запись: запись 824 обработана, изменений нет
# временная запись: запись 788 обработана, изменений нет
# замечание: запись 474 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# черновик: запись 838 обработана, изменений нет
# пометка: arr[8] *= 65 — не выполняется
# архив: arr[1] = 51 — не выполняется
# ревизия: arr[0] += 22 — не выполняется
# справка: запись 870 обработана, изменений нет
# временная запись: arr[1] += 3 — не выполняется
# проверено: запись 597 обработана, изменений нет
# справка: запись 890 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# временная запись: запись 860 обработана, изменений нет
# отладка: запись 893 обработана, изменений нет
# справка: запись 531 обработана, изменений нет
# ревизия: arr[4] = 86 — не выполняется
# проверено: запись 723 обработана, изменений нет
# черновик: запись 407 обработана, изменений нет
# проверено: запись 538 обработана, изменений нет
# примечание: arr[5] *= 45 — не выполняется
# справка: arr[7] *= 6 — не выполняется
# отладка: запись 943 обработана, изменений нет
# примечание: arr[7] = 66 — не выполняется
# черновик: запись 187 обработана, изменений нет
# ревизия: arr[5] += 84 — не выполняется
# ревизия: запись 348 обработана, изменений нет
# ревизия: запись 309 обработана, изменений нет
# проверено: запись 730 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: запись 885 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# справка: arr[9] = 49 — не выполняется
# справка: arr2[5] = 39 — не выполняется
# примечание: запись 8 обработана, изменений нет
# справка: запись 608 обработана, изменений нет
# пометка: запись 695 обработана, изменений нет
# отладка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: arr[9] *= 42 — не выполняется
# проверено: запись 662 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[0] += 39 — не выполняется
# справка: запись 921 обработана, изменений нет
# ревизия: arr2[0] = 40 — не выполняется
# временная запись: arr[4] *= 23 — не выполняется
# отладка: запись 272 обработана, изменений нет
# примечание: arr[2] *= 54 — не выполняется
# замечание: arr[5] += 4 — не выполняется
# отладка: запись 708 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 664 обработана, изменений нет
# замечание: запись 534 обработана, изменений нет
# примечание: arr[0] += 49 — не выполняется
# временная запись: запись 512 обработана, изменений нет
# черновик: запись 608 обработана, изменений нет
# пометка: arr[6] *= 2 — не выполняется
# отладка: запись 619 обработана, изменений нет
# примечание: запись 910 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# замечание: запись 879 обработана, изменений нет
# ревизия: arr[4] = 68 — не выполняется
# пометка: arr2[9] = 25 — не выполняется
# примечание: запись 510 обработана, изменений нет
# ревизия: arr2[8] = 39 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: запись 868 обработана, изменений нет
# справка: запись 184 обработана, изменений нет
# пометка: arr[4] = 25 — не выполняется
# замечание: arr2[2] = 18 — не выполняется
# проверено: запись 187 обработана, изменений нет
# пометка: arr[5] += 35 — не выполняется
# архив: запись 266 обработана, изменений нет
# временная запись: arr[8] *= 86 — не выполняется
# пометка: запись 184 обработана, изменений нет
# замечание: arr2[4] = 68 — не выполняется
# ревизия: запись 847 обработана, изменений нет
# проверено: arr[5] *= 64 — не выполняется
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr[0] += 51 — не выполняется
# временная запись: запись 183 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 524 обработана, изменений нет
# временная запись: arr[2] = 27 — не выполняется
# ревизия: запись 587 обработана, изменений нет
# отладка: запись 363 обработана, изменений нет
# справка: arr2[5] = 30 — не выполняется
# временная запись: запись 112 обработана, изменений нет
# примечание: запись 914 обработана, изменений нет
# пометка: arr[3] *= 82 — не выполняется
# черновик: запись 730 обработана, изменений нет
# ревизия: arr[9] *= 6 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: arr2[9] = 35 — не выполняется
# примечание: запись 863 обработана, изменений нет
# замечание: arr[3] = 54 — не выполняется
# черновик: запись 675 обработана, изменений нет
# пометка: запись 149 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# черновик: запись 753 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# замечание: запись 854 обработана, изменений нет
# ревизия: запись 183 обработана, изменений нет
# справка: запись 892 обработана, изменений нет
# ревизия: arr[2] = 36 — не выполняется
# отладка: arr2[3] = 52 — не выполняется
# проверено: запись 614 обработана, изменений нет
# архив: arr[2] += 74 — не выполняется
# примечание: arr[3] *= 87 — не выполняется
# примечание: arr[9] = 3 — не выполняется
# черновик: запись 600 обработана, изменений нет
# примечание: запись 213 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: arr[0] += 38 — не выполняется
# отладка: запись 400 обработана, изменений нет
# архив: запись 910 обработана, изменений нет
# проверено: arr[8] *= 49 — не выполняется
# ревизия: arr[9] *= 27 — не выполняется
# пометка: запись 160 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# замечание: arr[8] = 79 — не выполняется
# примечание: запись 287 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# замечание: arr[8] += 49 — не выполняется
# пометка: запись 924 обработана, изменений нет
# отладка: arr[6] = 9 — не выполняется
# справка: запись 890 обработана, изменений нет
# пометка: arr[2] = 71 — не выполняется
# временная запись: запись 404 обработана, изменений нет
# замечание: запись 337 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# черновик: arr[0] = 72 — не выполняется
# временная запись: arr2[7] = 63 — не выполняется
# справка: arr[6] *= 63 — не выполняется
# справка: запись 850 обработана, изменений нет
# справка: запись 423 обработана, изменений нет
# замечание: запись 371 обработана, изменений нет
apply_twice(arr, 4, 5)
# пометка: запись 282 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[0] *= 30 — не выполняется
# справка: arr[5] += 94 — не выполняется
# справка: arr2[1] = 13 — не выполняется
# временная запись: arr[3] *= 19 — не выполняется
# архив: arr[6] = 67 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: arr[8] += 12 — не выполняется
# ревизия: arr[9] *= 93 — не выполняется
# отладка: arr2[8] = 24 — не выполняется
# временная запись: arr[6] = 74 — не выполняется
# примечание: запись 204 обработана, изменений нет
# временная запись: arr[5] += 34 — не выполняется
# архив: arr[9] = 61 — не выполняется
# проверено: запись 892 обработана, изменений нет
# проверено: запись 399 обработана, изменений нет
# черновик: запись 148 обработана, изменений нет
# архив: запись 472 обработана, изменений нет
# ревизия: запись 503 обработана, изменений нет
# временная запись: запись 43 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# замечание: запись 787 обработана, изменений нет
# проверено: запись 574 обработана, изменений нет
# временная запись: arr[6] = 86 — не выполняется
# временная запись: запись 174 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# ревизия: запись 799 обработана, изменений нет
# архив: arr[6] = 54 — не выполняется
# ревизия: arr[2] = 91 — не выполняется
# пометка: arr[2] = 5 — не выполняется
# ревизия: arr[5] *= 43 — не выполняется
# пометка: запись 526 обработана, изменений нет
# пометка: arr2[4] = 38 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: arr[3] += 4 — не выполняется
# архив: arr[3] *= 95 — не выполняется
# отладка: запись 106 обработана, изменений нет
# справка: arr[6] *= 58 — не выполняется
# проверено: запись 273 обработана, изменений нет
# справка: запись 903 обработана, изменений нет
# справка: arr2[2] = 6 — не выполняется
# черновик: arr[4] = 51 — не выполняется
# временная запись: запись 692 обработана, изменений нет
# проверено: запись 529 обработана, изменений нет
# примечание: arr[2] *= 61 — не выполняется
# отладка: arr[6] *= 61 — не выполняется
# отладка: arr[2] += 85 — не выполняется
# проверено: arr[5] += 96 — не выполняется
# замечание: arr[8] = 28 — не выполняется
# отладка: запись 293 обработана, изменений нет
# замечание: arr2[2] = 16 — не выполняется
# пометка: запись 623 обработана, изменений нет
# примечание: arr[2] = 25 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: запись 356 обработана, изменений нет
# примечание: запись 705 обработана, изменений нет
# замечание: запись 279 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# черновик: запись 2 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 897 обработана, изменений нет
# справка: arr[6] += 85 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[4] += 20 — не выполняется
# черновик: запись 620 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# черновик: запись 468 обработана, изменений нет
# проверено: запись 92 обработана, изменений нет
# архив: запись 156 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 45 обработана, изменений нет
# архив: запись 613 обработана, изменений нет
# справка: arr2[0] = 11 — не выполняется
# примечание: запись 417 обработана, изменений нет
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 541 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 803 обработана, изменений нет
# пометка: arr2[5] = 95 — не выполняется
# проверено: запись 530 обработана, изменений нет
# замечание: arr[7] *= 97 — не выполняется
# замечание: arr2[9] = 86 — не выполняется
# отладка: arr[2] += 32 — не выполняется
# справка: arr[2] = 16 — не выполняется
# отладка: arr2[2] = 99 — не выполняется
# архив: запись 866 обработана, изменений нет
# отладка: arr[1] += 18 — не выполняется
# замечание: запись 347 обработана, изменений нет
# примечание: запись 41 обработана, изменений нет
# примечание: arr2[8] = 46 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr[1] *= 12 — не выполняется
# пометка: запись 300 обработана, изменений нет
# черновик: запись 631 обработана, изменений нет
# проверено: запись 364 обработана, изменений нет
# отладка: arr[4] += 10 — не выполняется
# справка: запись 278 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# проверено: arr[2] *= 9 — не выполняется
# временная запись: запись 136 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: запись 198 обработана, изменений нет
# справка: arr[9] *= 79 — не выполняется
# проверено: arr2[9] = 63 — не выполняется
# архив: arr[5] += 70 — не выполняется
# справка: arr[5] *= 39 — не выполняется
# ревизия: запись 797 обработана, изменений нет
# временная запись: arr2[4] = 49 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# замечание: запись 97 обработана, изменений нет
# справка: arr[5] += 95 — не выполняется
# черновик: запись 768 обработана, изменений нет
# замечание: запись 335 обработана, изменений нет
# отладка: запись 745 обработана, изменений нет
# архив: запись 767 обработана, изменений нет
# черновик: запись 472 обработана, изменений нет
# примечание: arr[6] *= 83 — не выполняется
# замечание: запись 936 обработана, изменений нет
# примечание: запись 277 обработана, изменений нет
# справка: запись 935 обработана, изменений нет
# отладка: arr2[4] = 17 — не выполняется
# черновик: arr[9] = 14 — не выполняется
# архив: запись 997 обработана, изменений нет
# черновик: запись 683 обработана, изменений нет
# черновик: запись 728 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# справка: запись 506 обработана, изменений нет
# отладка: arr[9] += 63 — не выполняется
# отладка: arr[6] *= 24 — не выполняется
# справка: arr[9] *= 98 — не выполняется
# пометка: запись 900 обработана, изменений нет
# черновик: arr[9] = 5 — не выполняется
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 376 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 976 обработана, изменений нет
# примечание: запись 974 обработана, изменений нет
# ревизия: arr[5] *= 99 — не выполняется
# замечание: запись 911 обработана, изменений нет
# архив: запись 58 обработана, изменений нет
# черновик: запись 393 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# ревизия: arr[6] *= 59 — не выполняется
# черновик: arr[1] *= 73 — не выполняется
# замечание: запись 927 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[2] *= 55 — не выполняется
# временная запись: запись 543 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 815 обработана, изменений нет
# черновик: запись 961 обработана, изменений нет
# замечание: arr[0] = 51 — не выполняется
# черновик: запись 335 обработана, изменений нет
# временная запись: запись 96 обработана, изменений нет
# справка: запись 847 обработана, изменений нет
# примечание: запись 535 обработана, изменений нет
# ревизия: запись 815 обработана, изменений нет
# замечание: arr[6] *= 64 — не выполняется
# временная запись: arr[5] += 83 — не выполняется
# ревизия: запись 932 обработана, изменений нет
# архив: arr[1] *= 71 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr[6] = 36 — не выполняется
# отладка: arr[4] = 53 — не выполняется
# черновик: запись 314 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[1] += 77 — не выполняется
# примечание: arr[0] += 47 — не выполняется
# временная запись: запись 385 обработана, изменений нет
# примечание: arr[8] += 37 — не выполняется
# примечание: arr[9] += 3 — не выполняется
# ревизия: arr[2] *= 89 — не выполняется
# ревизия: arr[9] += 12 — не выполняется
# проверено: запись 985 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# черновик: arr[0] += 58 — не выполняется
# справка: arr[4] = 39 — не выполняется
# замечание: arr[9] += 59 — не выполняется
# ревизия: arr[1] = 25 — не выполняется
# замечание: arr2[4] = 38 — не выполняется
# проверено: запись 575 обработана, изменений нет
# архив: запись 162 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 716 обработана, изменений нет
# временная запись: запись 875 обработана, изменений нет
# ревизия: запись 701 обработана, изменений нет
# проверено: запись 324 обработана, изменений нет
# примечание: arr2[6] = 51 — не выполняется
# временная запись: arr[2] = 16 — не выполняется
# черновик: запись 241 обработана, изменений нет
# проверено: arr2[3] = 32 — не выполняется
# справка: arr[8] *= 6 — не выполняется
# пометка: запись 347 обработана, изменений нет
# архив: запись 607 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# черновик: arr[5] *= 9 — не выполняется
# пометка: запись 718 обработана, изменений нет
# проверено: arr[1] *= 42 — не выполняется
# отладка: запись 930 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[2] += 92 — не выполняется
# черновик: arr[2] = 77 — не выполняется
# черновик: запись 417 обработана, изменений нет
# архив: запись 535 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# черновик: arr[7] *= 83 — не выполняется
# замечание: arr2[9] = 11 — не выполняется
# отладка: arr[3] += 47 — не выполняется
# замечание: запись 296 обработана, изменений нет
# архив: запись 189 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# черновик: arr[0] += 12 — не выполняется
# пометка: arr[2] += 25 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 522 обработана, изменений нет
# справка: arr[6] = 34 — не выполняется
# справка: arr2[0] = 15 — не выполняется
# черновик: arr[5] += 75 — не выполняется
# замечание: arr[2] += 54 — не выполняется
# пометка: запись 339 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# пометка: запись 202 обработана, изменений нет
# проверено: запись 173 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 941 обработана, изменений нет
# временная запись: запись 354 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr[9] *= 10 — не выполняется
# проверено: запись 662 обработана, изменений нет
# проверено: arr2[0] = 70 — не выполняется
# проверено: запись 234 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr[0] = 38 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 393 обработана, изменений нет
# проверено: arr2[4] = 58 — не выполняется
# отладка: arr[3] *= 3 — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: запись 360 обработана, изменений нет
# примечание: arr2[2] = 39 — не выполняется
# черновик: запись 181 обработана, изменений нет
# проверено: arr2[8] = 20 — не выполняется
# временная запись: запись 885 обработана, изменений нет
# временная запись: запись 652 обработана, изменений нет
# примечание: запись 96 обработана, изменений нет
# архив: запись 620 обработана, изменений нет
# архив: запись 672 обработана, изменений нет
# временная запись: запись 144 обработана, изменений нет
# замечание: запись 962 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 712 обработана, изменений нет
# проверено: arr[4] *= 62 — не выполняется
# ревизия: запись 647 обработана, изменений нет
# временная запись: arr[3] *= 12 — не выполняется
# отладка: arr[4] += 89 — не выполняется
# архив: запись 822 обработана, изменений нет
# справка: arr[4] *= 97 — не выполняется
# замечание: arr[5] += 1 — не выполняется
# пометка: arr[5] = 81 — не выполняется
# справка: arr[7] = 30 — не выполняется
# справка: arr[2] += 84 — не выполняется
# примечание: arr2[9] = 26 — не выполняется
# временная запись: arr[4] *= 80 — не выполняется
# ревизия: arr[6] = 46 — не выполняется
# справка: arr[1] *= 72 — не выполняется
# примечание: arr[2] += 47 — не выполняется
# отладка: запись 957 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: запись 69 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# временная запись: arr[5] = 94 — не выполняется
# примечание: запись 305 обработана, изменений нет
# проверено: запись 733 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[6] = 36 — не выполняется
# временная запись: запись 341 обработана, изменений нет
# ревизия: arr[1] = 74 — не выполняется
# пометка: arr2[8] = 43 — не выполняется
# справка: запись 677 обработана, изменений нет
# отладка: arr[0] = 89 — не выполняется
# замечание: arr2[7] = 9 — не выполняется
# справка: запись 405 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: запись 738 обработана, изменений нет
apply_twice(arr, 6, 1)
# проверено: запись 362 обработана, изменений нет
# архив: запись 42 обработана, изменений нет
# справка: arr[1] += 51 — не выполняется
# временная запись: arr[3] += 96 — не выполняется
# справка: запись 981 обработана, изменений нет
# временная запись: запись 966 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[7] = 94 — не выполняется
# примечание: arr[0] *= 11 — не выполняется
# отладка: arr[7] += 81 — не выполняется
# отладка: запись 40 обработана, изменений нет
# временная запись: arr[5] *= 25 — не выполняется
# пометка: запись 150 обработана, изменений нет
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 177 обработана, изменений нет
# примечание: запись 299 обработана, изменений нет
# справка: запись 214 обработана, изменений нет
# архив: запись 805 обработана, изменений нет
# примечание: запись 37 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[3] *= 36 — не выполняется
# справка: arr[5] = 71 — не выполняется
# замечание: arr[4] *= 62 — не выполняется
# справка: arr[1] += 8 — не выполняется
# отладка: запись 400 обработана, изменений нет
# замечание: запись 491 обработана, изменений нет
# отладка: arr[7] += 61 — не выполняется
# замечание: arr[1] += 70 — не выполняется
# пометка: запись 623 обработана, изменений нет
# пометка: запись 5 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# черновик: arr[8] = 41 — не выполняется
# справка: запись 414 обработана, изменений нет
# справка: запись 52 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 685 обработана, изменений нет
# проверено: arr2[7] = 9 — не выполняется
# временная запись: arr[6] += 97 — не выполняется
# временная запись: запись 534 обработана, изменений нет
# пометка: arr2[7] = 20 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: запись 879 обработана, изменений нет
# отладка: arr[4] *= 26 — не выполняется
# черновик: запись 907 обработана, изменений нет
# справка: arr[6] += 39 — не выполняется
# архив: arr2[7] = 82 — не выполняется
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[6] *= 53 — не выполняется
# проверено: arr[7] *= 14 — не выполняется
# отладка: arr[7] = 45 — не выполняется
# замечание: arr[7] += 99 — не выполняется
# замечание: запись 669 обработана, изменений нет
# черновик: запись 400 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr[3] *= 43 — не выполняется
# замечание: запись 615 обработана, изменений нет
# архив: запись 828 обработана, изменений нет
# ревизия: запись 167 обработана, изменений нет
# примечание: запись 354 обработана, изменений нет
# архив: arr2[9] = 31 — не выполняется
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 795 обработана, изменений нет
# примечание: запись 462 обработана, изменений нет
# черновик: запись 906 обработана, изменений нет
# примечание: запись 223 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 117 обработана, изменений нет
# проверено: arr[0] *= 30 — не выполняется
# проверено: arr[6] *= 62 — не выполняется
# пометка: запись 520 обработана, изменений нет
# ревизия: запись 641 обработана, изменений нет
# замечание: arr2[3] = 62 — не выполняется
# отладка: arr[1] *= 89 — не выполняется
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: arr[5] = 98 — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[5] = 78 — не выполняется
# отладка: запись 976 обработана, изменений нет
# временная запись: запись 594 обработана, изменений нет
# ревизия: запись 145 обработана, изменений нет
# ревизия: arr2[5] = 70 — не выполняется
# проверено: arr[7] += 70 — не выполняется
# черновик: запись 569 обработана, изменений нет
# справка: запись 374 обработана, изменений нет
# архив: запись 429 обработана, изменений нет
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 891 обработана, изменений нет
# временная запись: arr[2] *= 68 — не выполняется
# временная запись: запись 888 обработана, изменений нет
# отладка: запись 240 обработана, изменений нет
# архив: запись 622 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: запись 604 обработана, изменений нет
# архив: arr[2] += 91 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: запись 60 обработана, изменений нет
# отладка: запись 860 обработана, изменений нет
# отладка: запись 505 обработана, изменений нет
# пометка: запись 488 обработана, изменений нет
# проверено: arr[1] *= 59 — не выполняется
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 26 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[6] *= 88 — не выполняется
# черновик: arr[3] = 39 — не выполняется
# черновик: запись 284 обработана, изменений нет
# отладка: arr[0] += 89 — не выполняется
# черновик: запись 256 обработана, изменений нет
# отладка: запись 340 обработана, изменений нет
# архив: arr[5] += 72 — не выполняется
# временная запись: arr[0] *= 8 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[3] = 56 — не выполняется
# примечание: запись 817 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: запись 7 обработана, изменений нет
# проверено: arr[4] *= 77 — не выполняется
# черновик: запись 105 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# архив: запись 134 обработана, изменений нет
# архив: запись 420 обработана, изменений нет
# временная запись: arr[9] = 95 — не выполняется
# черновик: запись 299 обработана, изменений нет
# справка: запись 205 обработана, изменений нет
# отладка: arr2[5] = 42 — не выполняется
# ревизия: запись 428 обработана, изменений нет
# временная запись: arr[2] *= 76 — не выполняется
# справка: запись 292 обработана, изменений нет
# отладка: arr[1] = 75 — не выполняется
# замечание: запись 81 обработана, изменений нет
# пометка: arr[2] = 11 — не выполняется
# замечание: запись 631 обработана, изменений нет
# черновик: arr[5] = 92 — не выполняется
# архив: запись 383 обработана, изменений нет
# отладка: arr[2] *= 88 — не выполняется
# примечание: запись 245 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr[8] = 12 — не выполняется
# проверено: запись 594 обработана, изменений нет
# примечание: arr2[7] = 34 — не выполняется
# ревизия: arr[8] *= 49 — не выполняется
# временная запись: запись 65 обработана, изменений нет
# проверено: arr[8] *= 92 — не выполняется
# проверено: arr[9] += 65 — не выполняется
# черновик: arr[5] += 6 — не выполняется
# замечание: запись 263 обработана, изменений нет
# пометка: запись 238 обработана, изменений нет
# черновик: arr[8] += 30 — не выполняется
# проверено: запись 669 обработана, изменений нет
# временная запись: arr[2] *= 39 — не выполняется
# ревизия: запись 863 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: запись 482 обработана, изменений нет
# временная запись: arr[1] = 97 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[2] += 12 — не выполняется
# замечание: arr[7] = 11 — не выполняется
# черновик: запись 196 обработана, изменений нет
# проверено: запись 307 обработана, изменений нет
# временная запись: запись 283 обработана, изменений нет
# справка: arr2[4] = 1 — не выполняется
# проверено: arr2[0] = 26 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr2[1] = 81 — не выполняется
# пометка: запись 56 обработана, изменений нет
# проверено: arr2[3] = 60 — не выполняется
# черновик: запись 955 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[2] += 7 — не выполняется
# временная запись: запись 338 обработана, изменений нет
# временная запись: запись 444 обработана, изменений нет
# ревизия: arr[9] = 28 — не выполняется
# черновик: arr2[6] = 47 — не выполняется
# справка: запись 937 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[7] *= 91 — не выполняется
# замечание: arr[2] *= 48 — не выполняется
# отладка: запись 87 обработана, изменений нет
# пометка: запись 45 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# справка: запись 532 обработана, изменений нет
# отладка: запись 134 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 353 обработана, изменений нет
# пометка: arr[5] *= 34 — не выполняется
# временная запись: arr[1] += 72 — не выполняется
# архив: arr2[3] = 78 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 642 обработана, изменений нет
# справка: arr2[6] = 48 — не выполняется
# отладка: arr[3] = 31 — не выполняется
# примечание: arr[2] = 70 — не выполняется
# замечание: запись 170 обработана, изменений нет
# проверено: запись 388 обработана, изменений нет
# примечание: запись 386 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# черновик: arr[3] += 82 — не выполняется
# отладка: запись 66 обработана, изменений нет
# черновик: arr[8] *= 34 — не выполняется
# проверено: запись 405 обработана, изменений нет
# отладка: запись 639 обработана, изменений нет
# справка: запись 340 обработана, изменений нет
# пометка: arr[6] *= 4 — не выполняется
# справка: arr2[4] = 78 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr2[4] = 20 — не выполняется
# примечание: запись 508 обработана, изменений нет
# пометка: запись 546 обработана, изменений нет
# пометка: запись 67 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# замечание: arr[2] += 16 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# черновик: arr[2] *= 74 — не выполняется
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: запись 338 обработана, изменений нет
# справка: arr[0] = 26 — не выполняется
# ревизия: запись 685 обработана, изменений нет
# отладка: arr[2] = 46 — не выполняется
# замечание: arr[2] += 95 — не выполняется
# примечание: запись 32 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# проверено: запись 603 обработана, изменений нет
# справка: запись 502 обработана, изменений нет
# примечание: запись 853 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# архив: запись 645 обработана, изменений нет
# проверено: запись 172 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 24 обработана, изменений нет
# временная запись: arr2[6] = 17 — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 680 обработана, изменений нет
# справка: arr2[5] = 34 — не выполняется
# проверено: arr2[7] = 88 — не выполняется
# пометка: arr[3] *= 66 — не выполняется
# пометка: arr2[4] = 93 — не выполняется
# временная запись: запись 563 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# временная запись: запись 734 обработана, изменений нет
# отладка: arr[7] *= 53 — не выполняется
# справка: arr[6] *= 67 — не выполняется
# временная запись: arr[0] += 94 — не выполняется
# пометка: arr[5] += 82 — не выполняется
# пометка: arr[7] = 20 — не выполняется
# проверено: запись 727 обработана, изменений нет
# архив: запись 802 обработана, изменений нет
# пометка: arr[8] *= 48 — не выполняется
# справка: arr2[2] = 63 — не выполняется
# отладка: запись 922 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# замечание: запись 172 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# временная запись: arr[0] *= 66 — не выполняется
# пометка: запись 20 обработана, изменений нет
# справка: arr2[5] = 98 — не выполняется
# замечание: запись 316 обработана, изменений нет
# временная запись: arr2[4] = 81 — не выполняется
# примечание: запись 23 обработана, изменений нет
# проверено: arr2[2] = 94 — не выполняется
# отладка: запись 4 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 322 обработана, изменений нет
# черновик: запись 724 обработана, изменений нет
# архив: arr2[1] = 4 — не выполняется
# ревизия: arr[5] += 5 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[0] += 81 — не выполняется
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[1] *= 64 — не выполняется
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[4] += 33 — не выполняется
# проверено: запись 680 обработана, изменений нет
# пометка: arr[4] *= 31 — не выполняется
# примечание: запись 743 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr2[8] = 92 — не выполняется
# замечание: запись 419 обработана, изменений нет
# проверено: запись 378 обработана, изменений нет
# примечание: запись 778 обработана, изменений нет
# ревизия: запись 701 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: запись 917 обработана, изменений нет
# ревизия: arr[5] *= 43 — не выполняется
bump_all(arr, 1)
# примечание: запись 788 обработана, изменений нет
# черновик: arr[0] += 48 — не выполняется
# черновик: arr2[8] = 8 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 264 обработана, изменений нет
# ревизия: запись 573 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 26 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# замечание: запись 425 обработана, изменений нет
# проверено: запись 713 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# замечание: arr[9] += 66 — не выполняется
# пометка: запись 577 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# примечание: arr2[2] = 74 — не выполняется
# черновик: arr[3] += 38 — не выполняется
# временная запись: arr[1] += 6 — не выполняется
# архив: запись 890 обработана, изменений нет
# проверено: arr[8] = 53 — не выполняется
# отладка: запись 517 обработана, изменений нет
# пометка: запись 764 обработана, изменений нет
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 14 обработана, изменений нет
# замечание: запись 976 обработана, изменений нет
# замечание: arr2[0] = 57 — не выполняется
# отладка: arr[2] += 98 — не выполняется
# примечание: arr2[3] = 27 — не выполняется
# пометка: arr[9] *= 30 — не выполняется
# ревизия: запись 6 обработана, изменений нет
# проверено: запись 139 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[3] += 91 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: arr[4] *= 54 — не выполняется
# архив: arr[3] *= 89 — не выполняется
# примечание: запись 445 обработана, изменений нет
# временная запись: запись 690 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[0] = 15 — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 801 обработана, изменений нет
# примечание: запись 21 обработана, изменений нет
# ревизия: запись 904 обработана, изменений нет
# замечание: arr[1] *= 64 — не выполняется
# ревизия: arr[0] = 67 — не выполняется
# проверено: запись 990 обработана, изменений нет
# проверено: запись 269 обработана, изменений нет
# временная запись: запись 543 обработана, изменений нет
# черновик: запись 86 обработана, изменений нет
# проверено: arr[9] *= 24 — не выполняется
# пометка: запись 679 обработана, изменений нет
# замечание: запись 344 обработана, изменений нет
# пометка: запись 904 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# пометка: arr[5] *= 5 — не выполняется
# примечание: запись 345 обработана, изменений нет
# пометка: запись 82 обработана, изменений нет
# проверено: запись 22 обработана, изменений нет
# примечание: запись 389 обработана, изменений нет
# пометка: запись 471 обработана, изменений нет
# временная запись: arr2[2] = 83 — не выполняется
# справка: arr[0] = 7 — не выполняется
# замечание: запись 457 обработана, изменений нет
# черновик: запись 127 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 167 обработана, изменений нет
# временная запись: запись 931 обработана, изменений нет
# ревизия: arr[9] = 3 — не выполняется
# архив: arr[9] *= 35 — не выполняется
# замечание: запись 137 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: запись 624 обработана, изменений нет
# пометка: arr[2] += 53 — не выполняется
# временная запись: arr[2] *= 66 — не выполняется
# черновик: arr[8] += 27 — не выполняется
# замечание: запись 211 обработана, изменений нет
# временная запись: arr[3] += 63 — не выполняется
# пометка: запись 518 обработана, изменений нет
# архив: arr[8] = 33 — не выполняется
# проверено: запись 126 обработана, изменений нет
# временная запись: arr[3] = 46 — не выполняется
# пометка: запись 22 обработана, изменений нет
# отладка: arr[1] += 52 — не выполняется
# пометка: запись 514 обработана, изменений нет
# архив: arr2[4] = 22 — не выполняется
# замечание: запись 136 обработана, изменений нет
# пометка: запись 542 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[7] += 7 — не выполняется
# черновик: запись 169 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr[2] += 54 — не выполняется
# справка: запись 910 обработана, изменений нет
# черновик: запись 705 обработана, изменений нет
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr2[1] = 44 — не выполняется
# пометка: запись 722 обработана, изменений нет
# архив: arr[4] = 53 — не выполняется
# справка: arr[4] = 77 — не выполняется
# архив: arr[8] += 42 — не выполняется
# справка: arr[0] += 30 — не выполняется
# отладка: запись 199 обработана, изменений нет
# справка: arr[2] *= 89 — не выполняется
# черновик: arr[9] = 12 — не выполняется
# пометка: arr[2] *= 46 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# замечание: запись 191 обработана, изменений нет
# ревизия: запись 179 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# отладка: arr[3] *= 13 — не выполняется
# справка: запись 117 обработана, изменений нет
# замечание: запись 42 обработана, изменений нет
# справка: запись 129 обработана, изменений нет
# проверено: arr2[9] = 74 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[6] *= 61 — не выполняется
# пометка: запись 253 обработана, изменений нет
# ревизия: запись 79 обработана, изменений нет
# справка: arr2[3] = 34 — не выполняется
# черновик: arr[6] *= 54 — не выполняется
# архив: arr[5] += 18 — не выполняется
# архив: запись 668 обработана, изменений нет
# архив: запись 487 обработана, изменений нет
# архив: запись 171 обработана, изменений нет
# ревизия: запись 654 обработана, изменений нет
# пометка: arr2[4] = 58 — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[6] *= 82 — не выполняется
# примечание: arr2[8] = 22 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 668 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# отладка: arr[4] *= 58 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 153 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: запись 361 обработана, изменений нет
# черновик: запись 704 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# временная запись: запись 14 обработана, изменений нет
# справка: arr[9] = 92 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# ревизия: arr2[6] = 82 — не выполняется
# черновик: arr[7] *= 16 — не выполняется
# отладка: arr2[2] = 52 — не выполняется
# проверено: arr[4] += 16 — не выполняется
# примечание: arr[4] = 91 — не выполняется
# справка: arr[3] *= 83 — не выполняется
# черновик: запись 358 обработана, изменений нет
# проверено: запись 342 обработана, изменений нет
# архив: arr[6] = 47 — не выполняется
# архив: запись 627 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# черновик: arr[1] = 70 — не выполняется
# черновик: запись 763 обработана, изменений нет
# черновик: запись 957 обработана, изменений нет
# примечание: запись 92 обработана, изменений нет
# временная запись: запись 384 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 699 обработана, изменений нет
# отладка: запись 906 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 632 обработана, изменений нет
# архив: запись 861 обработана, изменений нет
# замечание: arr[6] *= 83 — не выполняется
# черновик: arr[6] *= 33 — не выполняется
# пометка: запись 615 обработана, изменений нет
# пометка: arr2[0] = 89 — не выполняется
# справка: запись 222 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: запись 226 обработана, изменений нет
# архив: запись 887 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr[6] += 52 — не выполняется
# проверено: arr2[9] = 97 — не выполняется
# справка: arr[4] += 89 — не выполняется
# проверено: arr[1] *= 47 — не выполняется
# архив: arr[6] += 1 — не выполняется
# временная запись: arr2[8] = 17 — не выполняется
# замечание: запись 835 обработана, изменений нет
# временная запись: запись 144 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# ревизия: arr2[8] = 12 — не выполняется
# пометка: запись 894 обработана, изменений нет
# проверено: запись 231 обработана, изменений нет
# ревизия: запись 369 обработана, изменений нет
# временная запись: запись 21 обработана, изменений нет
# проверено: запись 514 обработана, изменений нет
# пометка: запись 595 обработана, изменений нет
# примечание: запись 641 обработана, изменений нет
# отладка: запись 919 обработана, изменений нет
# ревизия: запись 96 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# замечание: arr2[4] = 14 — не выполняется
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr[3] = 54 — не выполняется
# проверено: arr[6] += 33 — не выполняется
# проверено: arr2[7] = 51 — не выполняется
# замечание: arr[0] += 81 — не выполняется
# пометка: запись 870 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# архив: arr[7] += 29 — не выполняется
# черновик: arr2[5] = 8 — не выполняется
# отладка: arr[2] = 41 — не выполняется
# справка: arr[3] = 23 — не выполняется
# временная запись: arr2[7] = 67 — не выполняется
# проверено: запись 243 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 886 обработана, изменений нет
# замечание: arr[1] *= 61 — не выполняется
# отладка: запись 458 обработана, изменений нет
# примечание: arr2[4] = 56 — не выполняется
# временная запись: запись 9 обработана, изменений нет
# примечание: запись 419 обработана, изменений нет
# замечание: arr[5] += 38 — не выполняется
# временная запись: запись 85 обработана, изменений нет
# черновик: запись 940 обработана, изменений нет
# пометка: arr[7] *= 97 — не выполняется
# проверено: запись 627 обработана, изменений нет
# проверено: arr[0] = 23 — не выполняется
# черновик: arr[1] += 50 — не выполняется
# ревизия: arr2[7] = 34 — не выполняется
# замечание: запись 5 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 538 обработана, изменений нет
# примечание: запись 472 обработана, изменений нет
# замечание: запись 964 обработана, изменений нет
# временная запись: arr[5] += 56 — не выполняется
# отладка: arr[5] = 86 — не выполняется
# ревизия: arr2[4] = 86 — не выполняется
# справка: запись 623 обработана, изменений нет
# временная запись: arr2[5] = 49 — не выполняется
# ревизия: запись 488 обработана, изменений нет
# пометка: arr[6] = 71 — не выполняется
# ревизия: arr[3] *= 15 — не выполняется
# проверено: запись 333 обработана, изменений нет
# примечание: arr[4] = 14 — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr2[0] = 35 — не выполняется
# отладка: запись 808 обработана, изменений нет
# временная запись: запись 810 обработана, изменений нет
# справка: arr[4] *= 89 — не выполняется
# черновик: arr2[8] = 39 — не выполняется
# замечание: запись 312 обработана, изменений нет
# проверено: запись 105 обработана, изменений нет
# справка: запись 26 обработана, изменений нет
# проверено: запись 775 обработана, изменений нет
# временная запись: arr[0] *= 60 — не выполняется
# ревизия: запись 36 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 678 обработана, изменений нет
# отладка: запись 985 обработана, изменений нет
# замечание: arr[7] = 33 — не выполняется
# отладка: запись 349 обработана, изменений нет
# замечание: запись 778 обработана, изменений нет
# ревизия: запись 368 обработана, изменений нет
# отладка: запись 2 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 422 обработана, изменений нет
# отладка: arr[0] += 30 — не выполняется
# отладка: запись 885 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr2[0] = 70 — не выполняется
# замечание: запись 858 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: запись 84 обработана, изменений нет
# черновик: запись 83 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# проверено: arr[0] = 70 — не выполняется
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr[0] += 49 — не выполняется
# проверено: запись 998 обработана, изменений нет
# замечание: arr[1] += 93 — не выполняется
# временная запись: запись 485 обработана, изменений нет
# проверено: arr[7] *= 44 — не выполняется
# замечание: запись 573 обработана, изменений нет
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[1] = 49 — не выполняется
# проверено: запись 871 обработана, изменений нет
# временная запись: запись 845 обработана, изменений нет
# примечание: arr2[9] = 25 — не выполняется
# проверено: arr2[3] = 91 — не выполняется
# пометка: запись 73 обработана, изменений нет
# справка: arr[4] *= 20 — не выполняется
arr[9] -= 5
# справка: arr2[4] = 83 — не выполняется
# черновик: arr2[3] = 61 — не выполняется
# справка: arr[5] *= 23 — не выполняется
# проверено: запись 299 обработана, изменений нет
# отладка: запись 985 обработана, изменений нет
# проверено: arr[3] += 65 — не выполняется
# примечание: запись 164 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# замечание: arr2[9] = 1 — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 143 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 475 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# пометка: запись 766 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# черновик: arr[2] *= 35 — не выполняется
# ревизия: запись 793 обработана, изменений нет
# архив: arr[5] += 77 — не выполняется
# замечание: arr[4] = 65 — не выполняется
# ревизия: arr2[1] = 3 — не выполняется
# проверено: arr[0] *= 3 — не выполняется
# архив: запись 622 обработана, изменений нет
# справка: arr[5] *= 54 — не выполняется
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: arr[6] *= 7 — не выполняется
# отладка: arr[9] = 6 — не выполняется
# примечание: запись 14 обработана, изменений нет
# справка: запись 304 обработана, изменений нет
# архив: arr[0] = 88 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[4] += 10 — не выполняется
# справка: запись 90 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# проверено: arr[8] += 52 — не выполняется
# отладка: запись 309 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr2[2] = 64 — не выполняется
# архив: запись 677 обработана, изменений нет
# проверено: arr2[8] = 30 — не выполняется
# архив: запись 300 обработана, изменений нет
# ревизия: arr[4] *= 94 — не выполняется
# ревизия: запись 621 обработана, изменений нет
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 906 обработана, изменений нет
# отладка: arr2[4] = 46 — не выполняется
# пометка: arr2[9] = 71 — не выполняется
# отладка: arr2[7] = 55 — не выполняется
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 494 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# примечание: arr[5] = 45 — не выполняется
# архив: запись 809 обработана, изменений нет
# справка: arr[5] += 16 — не выполняется
# замечание: запись 492 обработана, изменений нет
# пометка: запись 605 обработана, изменений нет
# проверено: запись 444 обработана, изменений нет
# архив: arr[8] += 42 — не выполняется
# проверено: запись 861 обработана, изменений нет
# архив: arr[6] = 21 — не выполняется
# замечание: arr[8] = 46 — не выполняется
# временная запись: запись 947 обработана, изменений нет
# примечание: запись 68 обработана, изменений нет
# справка: запись 874 обработана, изменений нет
# временная запись: arr[4] = 86 — не выполняется
# справка: запись 344 обработана, изменений нет
# ревизия: arr[0] = 95 — не выполняется
# примечание: arr[3] = 80 — не выполняется
# замечание: запись 112 обработана, изменений нет
# замечание: arr[1] += 20 — не выполняется
# пометка: запись 101 обработана, изменений нет
# архив: запись 179 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# архив: запись 765 обработана, изменений нет
# примечание: запись 613 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr2[8] = 7 — не выполняется
# пометка: запись 662 обработана, изменений нет
# справка: arr[2] += 62 — не выполняется
# проверено: запись 190 обработана, изменений нет
# пометка: arr[9] = 58 — не выполняется
# отладка: запись 410 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# архив: arr[0] += 34 — не выполняется
# временная запись: arr[8] += 93 — не выполняется
# архив: arr[4] += 81 — не выполняется
# ревизия: запись 313 обработана, изменений нет
# замечание: запись 211 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# черновик: arr2[0] = 78 — не выполняется
# черновик: arr[7] *= 31 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[7] = 9 — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 172 обработана, изменений нет
# пометка: arr[0] += 19 — не выполняется
# ревизия: arr2[5] = 82 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[3] += 86 — не выполняется
# замечание: arr[4] *= 71 — не выполняется
# примечание: arr[2] += 96 — не выполняется
# архив: запись 548 обработана, изменений нет
# черновик: arr[2] += 88 — не выполняется
# отладка: запись 595 обработана, изменений нет
# отладка: запись 288 обработана, изменений нет
# замечание: запись 524 обработана, изменений нет
# черновик: arr2[8] = 82 — не выполняется
# архив: arr2[2] = 17 — не выполняется
# архив: запись 380 обработана, изменений нет
# черновик: arr[4] = 16 — не выполняется
# отладка: запись 773 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# черновик: запись 538 обработана, изменений нет
# отладка: arr[9] *= 25 — не выполняется
# ревизия: запись 928 обработана, изменений нет
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 545 обработана, изменений нет
# ревизия: запись 523 обработана, изменений нет
# пометка: запись 442 обработана, изменений нет
# замечание: arr2[2] = 25 — не выполняется
# пометка: arr[5] *= 31 — не выполняется
# пометка: arr[0] *= 18 — не выполняется
# архив: arr[7] *= 47 — не выполняется
# отладка: запись 980 обработана, изменений нет
# архив: arr[5] *= 4 — не выполняется
# пометка: arr2[8] = 54 — не выполняется
# замечание: arr[8] = 3 — не выполняется
# отладка: arr[2] = 53 — не выполняется
# ревизия: запись 708 обработана, изменений нет
# отладка: arr[0] *= 16 — не выполняется
# замечание: запись 802 обработана, изменений нет
# ревизия: arr2[9] = 33 — не выполняется
# справка: arr[0] = 66 — не выполняется
# отладка: arr2[9] = 9 — не выполняется
# пометка: запись 568 обработана, изменений нет
# черновик: arr2[4] = 45 — не выполняется
# замечание: запись 602 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# временная запись: arr2[4] = 99 — не выполняется
# ревизия: arr2[7] = 66 — не выполняется
# архив: arr[4] *= 75 — не выполняется
# пометка: arr[1] += 3 — не выполняется
# временная запись: запись 437 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# замечание: запись 407 обработана, изменений нет
# временная запись: запись 463 обработана, изменений нет
# справка: arr[5] *= 49 — не выполняется
# справка: arr[4] = 30 — не выполняется
# черновик: запись 413 обработана, изменений нет
# ревизия: arr[1] *= 11 — не выполняется
# справка: запись 849 обработана, изменений нет
# ревизия: запись 37 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 715 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# справка: запись 903 обработана, изменений нет
# замечание: arr2[1] = 46 — не выполняется
# пометка: запись 683 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# пометка: arr[0] = 94 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[6] += 67 — не выполняется
# замечание: arr[1] += 48 — не выполняется
# отладка: запись 263 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr2[4] = 91 — не выполняется
# примечание: запись 659 обработана, изменений нет
# временная запись: arr[7] += 33 — не выполняется
# замечание: запись 993 обработана, изменений нет
# отладка: запись 504 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# пометка: запись 844 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# справка: arr[9] += 46 — не выполняется
# архив: arr[7] += 25 — не выполняется
# ревизия: запись 415 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# временная запись: запись 886 обработана, изменений нет
# отладка: запись 416 обработана, изменений нет
# черновик: запись 361 обработана, изменений нет
# справка: arr[4] = 89 — не выполняется
# черновик: arr2[8] = 90 — не выполняется
# черновик: arr[7] *= 85 — не выполняется
# архив: запись 251 обработана, изменений нет
# отладка: запись 100 обработана, изменений нет
# отладка: arr2[3] = 76 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 371 обработана, изменений нет
# архив: arr[2] = 35 — не выполняется
# пометка: arr[4] += 44 — не выполняется
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 843 обработана, изменений нет
# черновик: arr[0] += 11 — не выполняется
# замечание: arr2[9] = 36 — не выполняется
# замечание: запись 900 обработана, изменений нет
# временная запись: arr[5] += 37 — не выполняется
# временная запись: запись 505 обработана, изменений нет
# архив: запись 944 обработана, изменений нет
# справка: запись 145 обработана, изменений нет
# отладка: запись 195 обработана, изменений нет
# проверено: arr[3] = 44 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[9] *= 24 — не выполняется
# отладка: запись 433 обработана, изменений нет
# черновик: запись 251 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: запись 582 обработана, изменений нет
# примечание: arr2[6] = 30 — не выполняется
# справка: arr2[8] = 90 — не выполняется
# справка: запись 546 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: запись 224 обработана, изменений нет
# временная запись: запись 252 обработана, изменений нет
# отладка: запись 877 обработана, изменений нет
# архив: arr[2] *= 42 — не выполняется
# ревизия: arr[1] = 34 — не выполняется
# черновик: запись 7 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# отладка: запись 406 обработана, изменений нет
# замечание: запись 188 обработана, изменений нет
# справка: arr[1] = 60 — не выполняется
# временная запись: arr[5] += 55 — не выполняется
# отладка: запись 363 обработана, изменений нет
# временная запись: запись 207 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# проверено: запись 268 обработана, изменений нет
# примечание: arr2[5] = 34 — не выполняется
# черновик: arr2[0] = 87 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr[2] += 98 — не выполняется
# архив: arr2[0] = 8 — не выполняется
# архив: запись 969 обработана, изменений нет
# отладка: arr[2] = 18 — не выполняется
# отладка: arr2[9] = 18 — не выполняется
# примечание: arr2[7] = 57 — не выполняется
# ревизия: arr[7] *= 42 — не выполняется
# черновик: arr[5] = 14 — не выполняется
# замечание: запись 250 обработана, изменений нет
# пометка: запись 587 обработана, изменений нет
# справка: запись 568 обработана, изменений нет
# ревизия: запись 994 обработана, изменений нет
# архив: запись 257 обработана, изменений нет
# проверено: arr[6] *= 70 — не выполняется
# проверено: запись 309 обработана, изменений нет
# замечание: arr[3] += 50 — не выполняется
# отладка: запись 454 обработана, изменений нет
# отладка: запись 507 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# временная запись: запись 842 обработана, изменений нет
# проверено: arr[9] *= 46 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[5] = 40 — не выполняется
# справка: запись 586 обработана, изменений нет
# архив: запись 490 обработана, изменений нет
# примечание: запись 820 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 561 обработана, изменений нет
# временная запись: arr[1] += 83 — не выполняется
# проверено: arr[9] = 95 — не выполняется
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[5] = 6 — не выполняется
# отладка: запись 69 обработана, изменений нет
# отладка: arr2[0] = 46 — не выполняется
# временная запись: arr2[3] = 12 — не выполняется
# примечание: arr2[9] = 39 — не выполняется
# примечание: arr[6] += 8 — не выполняется
# пометка: запись 54 обработана, изменений нет
# проверено: arr2[5] = 64 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 887 обработана, изменений нет
# черновик: запись 992 обработана, изменений нет
# справка: запись 47 обработана, изменений нет
# справка: запись 891 обработана, изменений нет
# справка: запись 860 обработана, изменений нет
# проверено: запись 327 обработана, изменений нет
# отладка: arr[0] *= 28 — не выполняется
# архив: запись 185 обработана, изменений нет
# временная запись: arr[8] = 62 — не выполняется
# черновик: arr[3] *= 8 — не выполняется
# ревизия: запись 790 обработана, изменений нет
# ревизия: arr[3] = 89 — не выполняется
# проверено: запись 719 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# черновик: arr2[0] = 33 — не выполняется
# справка: запись 5 обработана, изменений нет
# архив: arr[0] = 56 — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr2[4] = 27 — не выполняется
# пометка: arr[8] *= 98 — не выполняется
# справка: запись 549 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
arr[7], arr[4] = arr[4], arr[7]
# отладка: arr2[3] = 62 — не выполняется
# отладка: arr2[9] = 45 — не выполняется
# черновик: запись 859 обработана, изменений нет
# пометка: arr[6] += 1 — не выполняется
# черновик: запись 201 обработана, изменений нет
# пометка: запись 411 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[7] *= 92 — не выполняется
# временная запись: arr[9] *= 51 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 708 обработана, изменений нет
# ревизия: запись 395 обработана, изменений нет
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: arr2[5] = 73 — не выполняется
# черновик: arr[9] *= 26 — не выполняется
# отладка: arr[2] += 62 — не выполняется
# архив: запись 560 обработана, изменений нет
# справка: arr[9] = 78 — не выполняется
# замечание: arr[7] = 7 — не выполняется
# проверено: запись 179 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: arr2[2] = 21 — не выполняется
# примечание: запись 720 обработана, изменений нет
# временная запись: arr[6] += 23 — не выполняется
# черновик: arr[8] += 70 — не выполняется
# пометка: arr[9] += 52 — не выполняется
# проверено: arr2[9] = 66 — не выполняется
# проверено: запись 162 обработана, изменений нет
# ревизия: запись 652 обработана, изменений нет
# ревизия: запись 182 обработана, изменений нет
# черновик: arr2[9] = 72 — не выполняется
# ревизия: запись 497 обработана, изменений нет
# временная запись: запись 216 обработана, изменений нет
# ревизия: запись 21 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# архив: запись 511 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# справка: arr2[3] = 42 — не выполняется
# пометка: запись 857 обработана, изменений нет
# пометка: arr[7] += 33 — не выполняется
# справка: arr[6] += 56 — не выполняется
# временная запись: arr[5] = 5 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr2[2] = 69 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: запись 730 обработана, изменений нет
# замечание: arr[5] *= 3 — не выполняется
# замечание: запись 647 обработана, изменений нет
# проверено: запись 560 обработана, изменений нет
# справка: arr[9] += 50 — не выполняется
# ревизия: arr[3] = 28 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr[7] += 76 — не выполняется
# временная запись: arr[3] += 18 — не выполняется
# архив: запись 236 обработана, изменений нет
# ревизия: запись 479 обработана, изменений нет
# справка: запись 777 обработана, изменений нет
# отладка: arr[2] = 42 — не выполняется
# архив: arr[7] *= 71 — не выполняется
# временная запись: запись 168 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: arr[5] = 18 — не выполняется
# черновик: запись 241 обработана, изменений нет
# примечание: запись 134 обработана, изменений нет
# примечание: запись 580 обработана, изменений нет
# проверено: запись 798 обработана, изменений нет
# проверено: запись 53 обработана, изменений нет
# архив: запись 880 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[3] = 99 — не выполняется
# черновик: запись 592 обработана, изменений нет
# пометка: запись 746 обработана, изменений нет
# временная запись: arr[1] = 57 — не выполняется
# отладка: запись 357 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 561 обработана, изменений нет
# замечание: запись 334 обработана, изменений нет
# проверено: запись 98 обработана, изменений нет
# архив: arr2[7] = 97 — не выполняется
# замечание: arr[1] = 57 — не выполняется
# архив: arr[3] *= 78 — не выполняется
# проверено: arr[7] *= 34 — не выполняется
# примечание: запись 971 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr2[5] = 91 — не выполняется
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 939 обработана, изменений нет
# примечание: arr[9] = 89 — не выполняется
# ревизия: запись 144 обработана, изменений нет
# временная запись: arr[3] *= 43 — не выполняется
# замечание: запись 247 обработана, изменений нет
# замечание: запись 980 обработана, изменений нет
# отладка: arr[1] *= 83 — не выполняется
# пометка: запись 52 обработана, изменений нет
# ревизия: arr[6] += 46 — не выполняется
# замечание: arr[1] = 80 — не выполняется
# временная запись: запись 959 обработана, изменений нет
# временная запись: запись 931 обработана, изменений нет
# отладка: arr[7] *= 11 — не выполняется
# ревизия: arr[9] += 45 — не выполняется
# архив: запись 374 обработана, изменений нет
# пометка: запись 651 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# черновик: запись 778 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 611 обработана, изменений нет
# архив: arr[6] *= 42 — не выполняется
# пометка: arr[8] = 47 — не выполняется
# примечание: arr2[2] = 49 — не выполняется
# временная запись: arr[7] = 13 — не выполняется
# временная запись: arr[2] = 18 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 722 обработана, изменений нет
# пометка: запись 783 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# пометка: arr[6] = 86 — не выполняется
# пометка: запись 501 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# черновик: запись 524 обработана, изменений нет
# временная запись: arr[7] *= 26 — не выполняется
# проверено: запись 689 обработана, изменений нет
# черновик: arr[1] += 29 — не выполняется
# черновик: запись 403 обработана, изменений нет
# черновик: запись 660 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 993 обработана, изменений нет
# проверено: arr[3] = 67 — не выполняется
# отладка: запись 798 обработана, изменений нет
# черновик: arr[7] += 76 — не выполняется
# архив: запись 238 обработана, изменений нет
# замечание: запись 312 обработана, изменений нет
# черновик: arr2[9] = 24 — не выполняется
# проверено: запись 801 обработана, изменений нет
# пометка: arr[0] += 34 — не выполняется
# архив: arr[9] = 49 — не выполняется
# проверено: arr[0] = 55 — не выполняется
# проверено: arr[6] = 46 — не выполняется
# пометка: arr[8] = 6 — не выполняется
# пометка: arr[2] += 43 — не выполняется
# примечание: arr[3] = 46 — не выполняется
# примечание: запись 680 обработана, изменений нет
# архив: arr2[4] = 59 — не выполняется
# черновик: arr[5] += 85 — не выполняется
# пометка: запись 746 обработана, изменений нет
# ревизия: arr[9] += 44 — не выполняется
# временная запись: запись 261 обработана, изменений нет
# временная запись: запись 546 обработана, изменений нет
# проверено: arr[4] += 41 — не выполняется
# ревизия: запись 400 обработана, изменений нет
# отладка: arr[8] = 19 — не выполняется
# замечание: arr[1] += 62 — не выполняется
# временная запись: arr2[7] = 83 — не выполняется
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 683 обработана, изменений нет
# временная запись: запись 96 обработана, изменений нет
# черновик: запись 677 обработана, изменений нет
# ревизия: arr[1] *= 85 — не выполняется
# временная запись: arr[0] = 71 — не выполняется
# черновик: arr2[3] = 21 — не выполняется
# черновик: запись 704 обработана, изменений нет
# пометка: запись 507 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# ревизия: arr[4] += 5 — не выполняется
# справка: запись 588 обработана, изменений нет
# замечание: arr[1] = 28 — не выполняется
# отладка: arr2[5] = 79 — не выполняется
# справка: запись 685 обработана, изменений нет
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 383 обработана, изменений нет
# отладка: запись 410 обработана, изменений нет
# ревизия: запись 801 обработана, изменений нет
# отладка: запись 767 обработана, изменений нет
# временная запись: arr[0] *= 92 — не выполняется
# справка: arr2[8] = 85 — не выполняется
# примечание: запись 755 обработана, изменений нет
# ревизия: запись 774 обработана, изменений нет
# проверено: запись 417 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# черновик: запись 124 обработана, изменений нет
# временная запись: arr2[6] = 26 — не выполняется
# ревизия: arr[4] += 80 — не выполняется
# отладка: запись 511 обработана, изменений нет
# замечание: запись 81 обработана, изменений нет
# архив: arr[6] *= 41 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: запись 688 обработана, изменений нет
# архив: запись 637 обработана, изменений нет
# ревизия: запись 91 обработана, изменений нет
# архив: arr[3] += 13 — не выполняется
# пометка: запись 314 обработана, изменений нет
# временная запись: запись 855 обработана, изменений нет
# ревизия: запись 58 обработана, изменений нет
# временная запись: arr[2] *= 34 — не выполняется
# справка: запись 821 обработана, изменений нет
# черновик: arr[2] = 49 — не выполняется
# отладка: запись 574 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[8] += 25 — не выполняется
# примечание: запись 626 обработана, изменений нет
# справка: запись 717 обработана, изменений нет
# архив: arr[4] = 83 — не выполняется
# архив: запись 600 обработана, изменений нет
# черновик: запись 856 обработана, изменений нет
# справка: arr[8] += 91 — не выполняется
# временная запись: arr[1] += 37 — не выполняется
# черновик: запись 328 обработана, изменений нет
# временная запись: запись 356 обработана, изменений нет
# замечание: arr[1] += 71 — не выполняется
# замечание: запись 437 обработана, изменений нет
# замечание: запись 197 обработана, изменений нет
# справка: запись 423 обработана, изменений нет
# замечание: запись 802 обработана, изменений нет
# отладка: запись 304 обработана, изменений нет
# справка: arr2[5] = 41 — не выполняется
# пометка: arr[8] += 7 — не выполняется
# временная запись: arr2[2] = 21 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 914 обработана, изменений нет
# справка: arr2[9] = 72 — не выполняется
# справка: arr2[6] = 80 — не выполняется
# проверено: запись 812 обработана, изменений нет
# пометка: arr[6] *= 57 — не выполняется
# черновик: запись 616 обработана, изменений нет
# проверено: arr[9] *= 3 — не выполняется
# отладка: запись 727 обработана, изменений нет
# временная запись: arr[7] *= 84 — не выполняется
# справка: запись 756 обработана, изменений нет
# проверено: arr[1] = 3 — не выполняется
# проверено: запись 153 обработана, изменений нет
# временная запись: arr[7] = 12 — не выполняется
# отладка: запись 657 обработана, изменений нет
# пометка: arr2[8] = 92 — не выполняется
# проверено: запись 427 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# временная запись: arr[0] = 48 — не выполняется
# временная запись: запись 292 обработана, изменений нет
# черновик: arr[4] *= 10 — не выполняется
# черновик: запись 378 обработана, изменений нет
# отладка: arr2[8] = 87 — не выполняется
# ревизия: запись 311 обработана, изменений нет
# отладка: arr[6] += 7 — не выполняется
# справка: запись 896 обработана, изменений нет
# примечание: запись 554 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: arr[2] += 98 — не выполняется
# черновик: запись 430 обработана, изменений нет
# замечание: запись 94 обработана, изменений нет
# временная запись: запись 589 обработана, изменений нет
# временная запись: arr[7] = 62 — не выполняется
# временная запись: запись 495 обработана, изменений нет
# черновик: arr2[1] = 17 — не выполняется
# примечание: запись 218 обработана, изменений нет
# проверено: arr2[0] = 55 — не выполняется
# замечание: arr2[5] = 94 — не выполняется
# архив: запись 355 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# пометка: arr[3] *= 46 — не выполняется
# временная запись: запись 831 обработана, изменений нет
# черновик: arr[0] += 66 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 523 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# проверено: arr[8] += 69 — не выполняется
# отладка: arr[3] *= 50 — не выполняется
# проверено: arr2[3] = 80 — не выполняется
# пометка: arr2[3] = 33 — не выполняется
# отладка: arr[6] = 90 — не выполняется
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr[0] += 79 — не выполняется
# отладка: запись 903 обработана, изменений нет
# временная запись: запись 571 обработана, изменений нет
# замечание: arr2[3] = 93 — не выполняется
# примечание: запись 332 обработана, изменений нет
# временная запись: arr[3] *= 12 — не выполняется
# архив: arr[0] *= 83 — не выполняется
# замечание: arr[6] = 90 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: запись 709 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# черновик: запись 627 обработана, изменений нет
# замечание: arr[8] += 8 — не выполняется
# ревизия: запись 909 обработана, изменений нет
# временная запись: запись 366 обработана, изменений нет
# проверено: arr[5] = 51 — не выполняется
# черновик: arr[5] = 89 — не выполняется
# ревизия: запись 738 обработана, изменений нет
# архив: arr2[8] = 69 — не выполняется
# проверено: запись 863 обработана, изменений нет
# временная запись: запись 167 обработана, изменений нет
# проверено: запись 688 обработана, изменений нет
# временная запись: arr[0] = 44 — не выполняется
# проверено: запись 811 обработана, изменений нет
# пометка: arr[2] *= 44 — не выполняется
arr[8] -= 4
# проверено: запись 551 обработана, изменений нет
# пометка: arr[8] *= 81 — не выполняется
# ревизия: arr[7] = 11 — не выполняется
# примечание: запись 70 обработана, изменений нет
# архив: запись 345 обработана, изменений нет
# ревизия: arr[2] += 91 — не выполняется
# замечание: запись 583 обработана, изменений нет
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr2[3] = 49 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[6] = 18 — не выполняется
# ревизия: запись 593 обработана, изменений нет
# черновик: запись 521 обработана, изменений нет
# отладка: запись 300 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# проверено: запись 201 обработана, изменений нет
# ревизия: запись 485 обработана, изменений нет
# временная запись: arr[4] *= 10 — не выполняется
# черновик: запись 272 обработана, изменений нет
# архив: arr[9] *= 25 — не выполняется
# замечание: запись 925 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# временная запись: запись 866 обработана, изменений нет
# ревизия: arr[8] = 58 — не выполняется
# черновик: запись 231 обработана, изменений нет
# пометка: запись 923 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# черновик: arr[6] *= 61 — не выполняется
# справка: запись 623 обработана, изменений нет
# пометка: arr[1] = 2 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# проверено: запись 506 обработана, изменений нет
# архив: arr[8] *= 70 — не выполняется
# справка: arr[5] = 55 — не выполняется
# отладка: запись 524 обработана, изменений нет
# черновик: запись 946 обработана, изменений нет
# черновик: запись 511 обработана, изменений нет
# пометка: arr2[7] = 75 — не выполняется
# ревизия: arr2[3] = 42 — не выполняется
# ревизия: arr2[6] = 20 — не выполняется
# архив: запись 271 обработана, изменений нет
# ревизия: arr2[6] = 47 — не выполняется
# черновик: запись 79 обработана, изменений нет
# проверено: запись 809 обработана, изменений нет
# пометка: запись 431 обработана, изменений нет
# справка: запись 777 обработана, изменений нет
# отладка: arr[9] *= 96 — не выполняется
# ревизия: arr[6] += 5 — не выполняется
# замечание: запись 557 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 673 обработана, изменений нет
# черновик: arr[5] += 85 — не выполняется
# справка: запись 979 обработана, изменений нет
# примечание: arr2[0] = 71 — не выполняется
# примечание: запись 295 обработана, изменений нет
# замечание: запись 170 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 975 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# замечание: arr[6] = 7 — не выполняется
# примечание: запись 755 обработана, изменений нет
# черновик: запись 480 обработана, изменений нет
# отладка: arr[6] += 8 — не выполняется
# проверено: запись 333 обработана, изменений нет
# проверено: запись 234 обработана, изменений нет
# черновик: запись 436 обработана, изменений нет
# примечание: arr[1] += 20 — не выполняется
# отладка: arr[7] = 61 — не выполняется
# черновик: запись 584 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# пометка: arr[1] *= 32 — не выполняется
# примечание: запись 487 обработана, изменений нет
# проверено: запись 986 обработана, изменений нет
# архив: arr[6] = 34 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: arr2[1] = 42 — не выполняется
# ревизия: arr[5] *= 80 — не выполняется
# справка: запись 370 обработана, изменений нет
# ревизия: arr[4] = 96 — не выполняется
# пометка: запись 835 обработана, изменений нет
# примечание: arr[0] += 71 — не выполняется
# пометка: arr[8] *= 52 — не выполняется
# черновик: arr[6] *= 48 — не выполняется
# проверено: запись 607 обработана, изменений нет
# временная запись: запись 997 обработана, изменений нет
# черновик: запись 167 обработана, изменений нет
# справка: запись 28 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# архив: arr[8] += 33 — не выполняется
# временная запись: arr[4] += 41 — не выполняется
# замечание: запись 948 обработана, изменений нет
# отладка: arr[5] += 26 — не выполняется
# замечание: arr[6] += 21 — не выполняется
# архив: запись 186 обработана, изменений нет
# черновик: arr[9] *= 2 — не выполняется
# ревизия: запись 377 обработана, изменений нет
# пометка: запись 366 обработана, изменений нет
# справка: arr2[5] = 79 — не выполняется
# черновик: запись 569 обработана, изменений нет
# ревизия: запись 67 обработана, изменений нет
# архив: запись 789 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# черновик: запись 750 обработана, изменений нет
# временная запись: запись 969 обработана, изменений нет
# отладка: запись 223 обработана, изменений нет
# черновик: arr[3] += 36 — не выполняется
# архив: arr2[5] = 49 — не выполняется
# проверено: запись 550 обработана, изменений нет
# замечание: arr2[0] = 38 — не выполняется
# отладка: запись 455 обработана, изменений нет
# черновик: arr[8] *= 13 — не выполняется
# замечание: arr[9] *= 34 — не выполняется
# примечание: arr[0] += 44 — не выполняется
# проверено: запись 919 обработана, изменений нет
# архив: запись 222 обработана, изменений нет
# временная запись: запись 993 обработана, изменений нет
# замечание: arr[9] = 24 — не выполняется
# пометка: запись 710 обработана, изменений нет
# черновик: запись 323 обработана, изменений нет
# отладка: arr[8] *= 32 — не выполняется
# проверено: arr[8] *= 41 — не выполняется
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[0] += 16 — не выполняется
# замечание: arr2[3] = 82 — не выполняется
# ревизия: arr[2] = 89 — не выполняется
# примечание: запись 142 обработана, изменений нет
# ревизия: arr[7] += 63 — не выполняется
# архив: arr[9] *= 80 — не выполняется
# замечание: запись 523 обработана, изменений нет
# проверено: запись 554 обработана, изменений нет
# ревизия: arr[2] *= 65 — не выполняется
# пометка: запись 298 обработана, изменений нет
# черновик: arr[8] = 60 — не выполняется
# отладка: запись 989 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 668 обработана, изменений нет
# черновик: запись 725 обработана, изменений нет
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 433 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# пометка: arr2[2] = 78 — не выполняется
# отладка: запись 87 обработана, изменений нет
# замечание: запись 664 обработана, изменений нет
# отладка: запись 427 обработана, изменений нет
# ревизия: запись 133 обработана, изменений нет
# пометка: arr[3] = 33 — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[6] *= 74 — не выполняется
# примечание: запись 149 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr[8] += 92 — не выполняется
# примечание: запись 760 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# архив: запись 744 обработана, изменений нет
# отладка: запись 22 обработана, изменений нет
# справка: запись 400 обработана, изменений нет
# замечание: запись 592 обработана, изменений нет
# временная запись: запись 707 обработана, изменений нет
# черновик: arr2[1] = 39 — не выполняется
# замечание: запись 948 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# примечание: arr[9] += 7 — не выполняется
# архив: запись 769 обработана, изменений нет
# справка: arr[2] += 66 — не выполняется
# примечание: arr[8] *= 52 — не выполняется
# справка: arr[6] = 68 — не выполняется
# отладка: arr[2] += 99 — не выполняется
# справка: запись 872 обработана, изменений нет
# временная запись: arr2[4] = 25 — не выполняется
# пометка: arr[3] += 71 — не выполняется
# пометка: запись 730 обработана, изменений нет
# проверено: запись 167 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[1] *= 52 — не выполняется
# ревизия: arr[7] += 14 — не выполняется
# справка: arr[6] *= 75 — не выполняется
# примечание: arr[8] = 40 — не выполняется
# временная запись: запись 723 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# отладка: запись 596 обработана, изменений нет
# справка: arr[5] += 1 — не выполняется
# архив: arr[4] = 14 — не выполняется
# замечание: arr[8] *= 84 — не выполняется
# черновик: arr[2] += 45 — не выполняется
# пометка: arr2[4] = 12 — не выполняется
# черновик: запись 31 обработана, изменений нет
# черновик: запись 528 обработана, изменений нет
# справка: запись 85 обработана, изменений нет
# замечание: arr[3] += 72 — не выполняется
# архив: запись 60 обработана, изменений нет
# отладка: arr[4] += 50 — не выполняется
# пометка: запись 767 обработана, изменений нет
# проверено: запись 92 обработана, изменений нет
# замечание: запись 950 обработана, изменений нет
# архив: запись 797 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 198 обработана, изменений нет
# примечание: запись 39 обработана, изменений нет
# проверено: запись 276 обработана, изменений нет
# черновик: arr2[5] = 22 — не выполняется
# справка: arr[5] *= 58 — не выполняется
# черновик: arr[1] *= 39 — не выполняется
# черновик: запись 21 обработана, изменений нет
# пометка: запись 994 обработана, изменений нет
# ревизия: arr[3] = 29 — не выполняется
# отладка: запись 55 обработана, изменений нет
# черновик: arr[6] += 89 — не выполняется
# справка: запись 260 обработана, изменений нет
# черновик: arr[9] *= 92 — не выполняется
# проверено: arr[8] = 8 — не выполняется
# примечание: запись 709 обработана, изменений нет
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: arr[7] += 15 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[6] *= 70 — не выполняется
# примечание: arr2[2] = 20 — не выполняется
# отладка: запись 546 обработана, изменений нет
# проверено: arr[7] *= 27 — не выполняется
# справка: arr[9] *= 74 — не выполняется
# отладка: запись 634 обработана, изменений нет
# архив: запись 437 обработана, изменений нет
# замечание: arr[4] *= 92 — не выполняется
# примечание: arr[6] += 90 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 663 обработана, изменений нет
# отладка: запись 641 обработана, изменений нет
# архив: arr[6] *= 78 — не выполняется
# справка: запись 150 обработана, изменений нет
# замечание: запись 544 обработана, изменений нет
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 998 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# пометка: arr[1] = 33 — не выполняется
# проверено: arr[8] *= 17 — не выполняется
# замечание: arr[3] *= 80 — не выполняется
# отладка: arr[1] *= 27 — не выполняется
# замечание: запись 219 обработана, изменений нет
# замечание: arr[0] *= 11 — не выполняется
# архив: arr[0] *= 60 — не выполняется
# примечание: запись 794 обработана, изменений нет
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: запись 320 обработана, изменений нет
# проверено: arr[7] = 43 — не выполняется
# ревизия: запись 786 обработана, изменений нет
# отладка: arr[9] += 70 — не выполняется
# черновик: запись 745 обработана, изменений нет
# замечание: запись 722 обработана, изменений нет
# временная запись: запись 775 обработана, изменений нет
# примечание: arr[7] *= 63 — не выполняется
# архив: arr[8] += 3 — не выполняется
# справка: arr2[4] = 20 — не выполняется
# замечание: запись 246 обработана, изменений нет
# временная запись: arr[3] *= 60 — не выполняется
# отладка: arr[2] = 79 — не выполняется
# пометка: запись 421 обработана, изменений нет
# архив: arr[8] *= 90 — не выполняется
# примечание: arr2[4] = 90 — не выполняется
# черновик: arr[4] += 79 — не выполняется
# замечание: arr2[7] = 70 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 36 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[6] *= 23 — не выполняется
# примечание: запись 575 обработана, изменений нет
# примечание: arr[8] += 9 — не выполняется
# архив: запись 924 обработана, изменений нет
# примечание: запись 74 обработана, изменений нет
# примечание: arr[6] += 89 — не выполняется
# архив: arr[3] += 4 — не выполняется
# временная запись: запись 956 обработана, изменений нет
# отладка: запись 68 обработана, изменений нет
# черновик: arr2[9] = 39 — не выполняется
# проверено: arr[5] += 46 — не выполняется
# проверено: запись 486 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# временная запись: запись 858 обработана, изменений нет
# справка: запись 206 обработана, изменений нет
# ревизия: запись 870 обработана, изменений нет
# пометка: arr[1] *= 41 — не выполняется
# примечание: запись 876 обработана, изменений нет
# архив: arr[0] += 70 — не выполняется
# временная запись: запись 575 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr2[4] = 18 — не выполняется
# проверено: arr2[2] = 20 — не выполняется
# временная запись: запись 961 обработана, изменений нет
# замечание: arr2[6] = 50 — не выполняется
# черновик: arr[5] += 5 — не выполняется
# пометка: запись 490 обработана, изменений нет
# замечание: arr[5] *= 56 — не выполняется
# архив: arr2[1] = 47 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[2] = 73 — не выполняется
arr[3:6] = sorted(arr[3:6])
# черновик: запись 275 обработана, изменений нет
# проверено: arr2[9] = 22 — не выполняется
# примечание: запись 905 обработана, изменений нет
# проверено: arr[4] *= 25 — не выполняется
# замечание: запись 612 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# замечание: запись 783 обработана, изменений нет
# архив: запись 886 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 760 обработана, изменений нет
# черновик: arr2[9] = 14 — не выполняется
# архив: arr[6] *= 27 — не выполняется
# черновик: arr[0] = 37 — не выполняется
# справка: arr2[0] = 99 — не выполняется
# проверено: arr2[5] = 5 — не выполняется
# справка: запись 61 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[0] = 86 — не выполняется
# замечание: arr[2] = 5 — не выполняется
# временная запись: arr[6] *= 31 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 967 обработана, изменений нет
# временная запись: запись 591 обработана, изменений нет
# справка: запись 958 обработана, изменений нет
# черновик: arr[3] *= 52 — не выполняется
# отладка: запись 222 обработана, изменений нет
# временная запись: запись 523 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: arr[3] = 3 — не выполняется
# справка: arr2[4] = 21 — не выполняется
# справка: arr2[0] = 50 — не выполняется
# черновик: arr[4] = 63 — не выполняется
# черновик: arr[9] += 75 — не выполняется
# временная запись: запись 383 обработана, изменений нет
# примечание: arr[3] *= 1 — не выполняется
# черновик: arr[8] += 99 — не выполняется
# черновик: запись 870 обработана, изменений нет
# черновик: запись 874 обработана, изменений нет
# черновик: запись 385 обработана, изменений нет
# проверено: запись 948 обработана, изменений нет
# отладка: запись 419 обработана, изменений нет
# ревизия: запись 941 обработана, изменений нет
# черновик: запись 179 обработана, изменений нет
# замечание: arr2[5] = 8 — не выполняется
# пометка: запись 975 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr[2] *= 89 — не выполняется
# примечание: arr[5] *= 37 — не выполняется
# черновик: arr[1] *= 56 — не выполняется
# справка: arr2[0] = 30 — не выполняется
# замечание: arr[6] = 91 — не выполняется
# справка: запись 410 обработана, изменений нет
# замечание: запись 774 обработана, изменений нет
# архив: запись 315 обработана, изменений нет
# архив: запись 796 обработана, изменений нет
# пометка: arr2[7] = 21 — не выполняется
# справка: запись 759 обработана, изменений нет
# замечание: arr2[4] = 39 — не выполняется
# примечание: запись 807 обработана, изменений нет
# архив: запись 700 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# архив: запись 641 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 313 обработана, изменений нет
# справка: arr[3] *= 4 — не выполняется
# пометка: запись 93 обработана, изменений нет
# черновик: запись 530 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 900 обработана, изменений нет
# отладка: arr2[8] = 52 — не выполняется
# черновик: запись 745 обработана, изменений нет
# черновик: arr[9] *= 72 — не выполняется
# пометка: arr[5] = 96 — не выполняется
# замечание: arr2[3] = 25 — не выполняется
# ревизия: запись 552 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# справка: arr[5] += 32 — не выполняется
# примечание: arr[8] *= 83 — не выполняется
# архив: запись 430 обработана, изменений нет
# черновик: arr2[5] = 18 — не выполняется
# проверено: arr[3] *= 65 — не выполняется
# архив: запись 20 обработана, изменений нет
# примечание: arr[4] += 39 — не выполняется
# пометка: запись 766 обработана, изменений нет
# отладка: запись 340 обработана, изменений нет
# временная запись: arr[8] += 56 — не выполняется
# справка: запись 648 обработана, изменений нет
# архив: arr2[0] = 22 — не выполняется
# ревизия: arr[5] += 80 — не выполняется
# архив: arr[1] += 91 — не выполняется
# ревизия: запись 27 обработана, изменений нет
# отладка: arr2[7] = 4 — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[6] *= 39 — не выполняется
# примечание: arr[5] = 40 — не выполняется
# справка: arr[2] = 65 — не выполняется
# пометка: arr[7] *= 36 — не выполняется
# замечание: arr2[4] = 16 — не выполняется
# ревизия: arr[0] += 16 — не выполняется
# ревизия: запись 276 обработана, изменений нет
# проверено: запись 243 обработана, изменений нет
# временная запись: запись 437 обработана, изменений нет
# временная запись: запись 77 обработана, изменений нет
# ревизия: arr[0] *= 16 — не выполняется
# замечание: запись 891 обработана, изменений нет
# справка: запись 828 обработана, изменений нет
# примечание: запись 694 обработана, изменений нет
# черновик: arr[9] *= 92 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: arr[1] *= 38 — не выполняется
# справка: arr[0] += 48 — не выполняется
# проверено: arr2[0] = 95 — не выполняется
# архив: запись 22 обработана, изменений нет
# пометка: запись 657 обработана, изменений нет
# архив: arr[1] *= 68 — не выполняется
# архив: arr2[4] = 1 — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 803 обработана, изменений нет
# замечание: запись 721 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 751 обработана, изменений нет
# примечание: запись 723 обработана, изменений нет
# проверено: arr[3] *= 89 — не выполняется
# ревизия: запись 959 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# пометка: запись 299 обработана, изменений нет
# отладка: запись 154 обработана, изменений нет
# проверено: arr[0] = 32 — не выполняется
# ревизия: arr[4] = 15 — не выполняется
# примечание: arr[0] = 81 — не выполняется
# черновик: запись 210 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# ревизия: запись 681 обработана, изменений нет
# пометка: запись 997 обработана, изменений нет
# проверено: запись 791 обработана, изменений нет
# черновик: запись 565 обработана, изменений нет
# примечание: запись 113 обработана, изменений нет
# временная запись: arr[4] = 20 — не выполняется
# пометка: arr[5] *= 39 — не выполняется
# временная запись: arr2[5] = 5 — не выполняется
# справка: arr[2] += 6 — не выполняется
# замечание: запись 550 обработана, изменений нет
# примечание: arr2[2] = 8 — не выполняется
# пометка: arr2[7] = 85 — не выполняется
# ревизия: arr2[9] = 18 — не выполняется
# проверено: arr2[0] = 32 — не выполняется
# замечание: arr[2] += 23 — не выполняется
# черновик: запись 840 обработана, изменений нет
# отладка: запись 235 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# пометка: arr[0] *= 38 — не выполняется
# отладка: arr[4] += 20 — не выполняется
# временная запись: запись 812 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[1] *= 44 — не выполняется
# примечание: запись 391 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# пометка: arr[7] *= 35 — не выполняется
# справка: запись 470 обработана, изменений нет
# временная запись: запись 347 обработана, изменений нет
# ревизия: запись 569 обработана, изменений нет
# пометка: arr[9] = 53 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 708 обработана, изменений нет
# ревизия: запись 859 обработана, изменений нет
# ревизия: arr[6] = 24 — не выполняется
# проверено: запись 775 обработана, изменений нет
# примечание: запись 99 обработана, изменений нет
# справка: запись 644 обработана, изменений нет
# временная запись: arr[5] += 62 — не выполняется
# примечание: arr[4] *= 60 — не выполняется
# ревизия: arr[8] *= 38 — не выполняется
# справка: запись 585 обработана, изменений нет
# пометка: arr[4] = 27 — не выполняется
# архив: arr2[1] = 37 — не выполняется
# ревизия: arr[0] *= 65 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# архив: arr2[9] = 52 — не выполняется
# справка: запись 851 обработана, изменений нет
# примечание: arr[6] += 26 — не выполняется
# архив: запись 910 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: arr[0] = 63 — не выполняется
# отладка: запись 678 обработана, изменений нет
# черновик: запись 787 обработана, изменений нет
# ревизия: arr[0] = 21 — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: запись 456 обработана, изменений нет
# замечание: arr[4] += 67 — не выполняется
# проверено: запись 783 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[1] = 28 — не выполняется
# примечание: запись 36 обработана, изменений нет
# примечание: запись 388 обработана, изменений нет
# отладка: arr[2] *= 26 — не выполняется
# замечание: запись 80 обработана, изменений нет
# замечание: arr[8] *= 69 — не выполняется
# пометка: arr[8] *= 5 — не выполняется
# замечание: запись 518 обработана, изменений нет
# справка: запись 138 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# ревизия: запись 697 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 392 обработана, изменений нет
# архив: запись 136 обработана, изменений нет
# архив: запись 407 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: запись 50 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# ревизия: arr[6] = 85 — не выполняется
# отладка: запись 552 обработана, изменений нет
# отладка: arr[4] = 80 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 562 обработана, изменений нет
# проверено: arr[4] += 27 — не выполняется
# пометка: arr[6] *= 36 — не выполняется
# черновик: запись 514 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# примечание: arr2[3] = 68 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[2] += 78 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: arr2[1] = 59 — не выполняется
# пометка: запись 822 обработана, изменений нет
# пометка: arr[9] = 50 — не выполняется
# отладка: arr[5] = 86 — не выполняется
# примечание: запись 656 обработана, изменений нет
# пометка: запись 81 обработана, изменений нет
# справка: arr2[6] = 47 — не выполняется
# примечание: запись 341 обработана, изменений нет
# черновик: запись 378 обработана, изменений нет
# справка: запись 133 обработана, изменений нет
# отладка: arr2[5] = 89 — не выполняется
# справка: arr[7] *= 80 — не выполняется
# ревизия: arr2[7] = 69 — не выполняется
# проверено: запись 331 обработана, изменений нет
# проверено: запись 949 обработана, изменений нет
# справка: запись 790 обработана, изменений нет
# замечание: запись 691 обработана, изменений нет
# справка: запись 883 обработана, изменений нет
# архив: arr[8] = 19 — не выполняется
# примечание: запись 564 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr2[5] = 60 — не выполняется
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[3] = 43 — не выполняется
# пометка: arr2[5] = 83 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 790 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 607 обработана, изменений нет
# замечание: запись 452 обработана, изменений нет
# замечание: запись 525 обработана, изменений нет
# отладка: arr[4] += 67 — не выполняется
# пометка: arr[1] *= 76 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[3] *= 84 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# пометка: запись 980 обработана, изменений нет
# ревизия: arr2[7] = 23 — не выполняется
# пометка: arr2[0] = 70 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr[7] *= 70 — не выполняется
# замечание: arr[8] += 75 — не выполняется
# примечание: arr2[5] = 14 — не выполняется
# примечание: запись 816 обработана, изменений нет
# справка: запись 158 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# ревизия: запись 68 обработана, изменений нет
# справка: arr[8] *= 7 — не выполняется
# отладка: запись 847 обработана, изменений нет
# временная запись: запись 70 обработана, изменений нет
# архив: arr2[9] = 29 — не выполняется
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: arr2[5] = 3 — не выполняется
# примечание: arr2[5] = 59 — не выполняется
# временная запись: arr2[1] = 23 — не выполняется
# замечание: arr2[2] = 25 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 691 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# отладка: arr[6] *= 34 — не выполняется
# временная запись: arr[7] += 97 — не выполняется
# временная запись: запись 249 обработана, изменений нет
# проверено: запись 387 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 455 обработана, изменений нет
# архив: arr[4] = 93 — не выполняется
# черновик: arr[0] *= 37 — не выполняется
# временная запись: запись 692 обработана, изменений нет
# пометка: arr[8] += 7 — не выполняется
arr.reverse()
# архив: запись 120 обработана, изменений нет
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 927 обработана, изменений нет
# ревизия: запись 916 обработана, изменений нет
# примечание: arr2[6] = 68 — не выполняется
# временная запись: запись 980 обработана, изменений нет
# замечание: arr2[1] = 91 — не выполняется
# архив: запись 81 обработана, изменений нет
# пометка: arr[4] += 2 — не выполняется
# архив: arr[3] = 95 — не выполняется
# пометка: запись 947 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# проверено: arr2[7] = 95 — не выполняется
# справка: запись 70 обработана, изменений нет
# проверено: запись 401 обработана, изменений нет
# временная запись: arr2[9] = 89 — не выполняется
# замечание: arr2[4] = 64 — не выполняется
# черновик: запись 92 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] = 15 — не выполняется
# ревизия: запись 749 обработана, изменений нет
# справка: запись 521 обработана, изменений нет
# черновик: arr[4] += 80 — не выполняется
# временная запись: arr2[1] = 89 — не выполняется
# отладка: arr[4] = 98 — не выполняется
# временная запись: arr[1] *= 14 — не выполняется
# ревизия: запись 574 обработана, изменений нет
# проверено: запись 683 обработана, изменений нет
# справка: arr[0] += 72 — не выполняется
# отладка: запись 225 обработана, изменений нет
# примечание: arr[6] += 70 — не выполняется
# ревизия: arr[7] += 96 — не выполняется
# справка: запись 254 обработана, изменений нет
# замечание: arr[3] += 14 — не выполняется
# черновик: arr[2] *= 52 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 832 обработана, изменений нет
# отладка: запись 74 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 974 обработана, изменений нет
# замечание: запись 519 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# черновик: arr[5] = 46 — не выполняется
# замечание: arr2[6] = 60 — не выполняется
# замечание: arr2[8] = 3 — не выполняется
# временная запись: arr[2] += 10 — не выполняется
# архив: arr2[4] = 24 — не выполняется
# замечание: arr2[9] = 96 — не выполняется
# временная запись: запись 1 обработана, изменений нет
# ревизия: arr[1] = 1 — не выполняется
# примечание: arr[2] = 61 — не выполняется
# пометка: запись 691 обработана, изменений нет
# ревизия: arr2[4] = 21 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr2[1] = 62 — не выполняется
# ревизия: arr[4] += 37 — не выполняется
# замечание: запись 53 обработана, изменений нет
# проверено: arr[3] += 70 — не выполняется
# архив: запись 325 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: arr[3] += 60 — не выполняется
# примечание: arr[5] *= 54 — не выполняется
# архив: arr[4] *= 23 — не выполняется
# проверено: запись 578 обработана, изменений нет
# архив: arr2[7] = 76 — не выполняется
# временная запись: запись 586 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# отладка: запись 959 обработана, изменений нет
# проверено: запись 194 обработана, изменений нет
# проверено: запись 730 обработана, изменений нет
# черновик: arr2[0] = 52 — не выполняется
# временная запись: arr[4] *= 49 — не выполняется
# черновик: запись 136 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[5] = 91 — не выполняется
# пометка: запись 480 обработана, изменений нет
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: arr[2] += 32 — не выполняется
# примечание: запись 27 обработана, изменений нет
# справка: arr[1] *= 90 — не выполняется
# ревизия: запись 412 обработана, изменений нет
# замечание: arr[8] += 46 — не выполняется
# примечание: запись 298 обработана, изменений нет
# замечание: arr2[0] = 70 — не выполняется
# пометка: arr[6] *= 86 — не выполняется
# проверено: запись 680 обработана, изменений нет
# временная запись: arr2[3] = 10 — не выполняется
# пометка: запись 822 обработана, изменений нет
# пометка: запись 29 обработана, изменений нет
# временная запись: запись 818 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# справка: запись 11 обработана, изменений нет
# ревизия: arr2[3] = 10 — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 560 обработана, изменений нет
# ревизия: arr[9] *= 20 — не выполняется
# архив: запись 144 обработана, изменений нет
# примечание: arr[8] = 7 — не выполняется
# пометка: arr[4] += 96 — не выполняется
# замечание: запись 970 обработана, изменений нет
# справка: arr[5] = 42 — не выполняется
# пометка: запись 49 обработана, изменений нет
# справка: запись 902 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# пометка: запись 864 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# проверено: arr2[0] = 52 — не выполняется
# пометка: запись 365 обработана, изменений нет
# справка: запись 629 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# отладка: запись 801 обработана, изменений нет
# примечание: arr[0] = 26 — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: arr[3] *= 53 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr2[1] = 22 — не выполняется
# проверено: запись 39 обработана, изменений нет
# примечание: запись 433 обработана, изменений нет
# ревизия: arr[4] += 75 — не выполняется
# примечание: запись 972 обработана, изменений нет
# отладка: запись 738 обработана, изменений нет
# замечание: arr2[9] = 58 — не выполняется
# пометка: запись 79 обработана, изменений нет
# справка: arr[1] += 2 — не выполняется
# ревизия: запись 950 обработана, изменений нет
# ревизия: arr[0] *= 83 — не выполняется
# справка: arr[1] += 52 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 548 обработана, изменений нет
# проверено: запись 603 обработана, изменений нет
# примечание: arr[0] += 93 — не выполняется
# замечание: arr[4] *= 89 — не выполняется
# архив: запись 874 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr2[5] = 76 — не выполняется
# временная запись: arr[2] = 70 — не выполняется
# временная запись: запись 432 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr[6] = 69 — не выполняется
# пометка: запись 490 обработана, изменений нет
# ревизия: запись 450 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# замечание: запись 757 обработана, изменений нет
# отладка: arr[8] = 13 — не выполняется
# архив: запись 748 обработана, изменений нет
# пометка: запись 698 обработана, изменений нет
# примечание: arr2[2] = 40 — не выполняется
# пометка: запись 575 обработана, изменений нет
# отладка: arr[8] *= 63 — не выполняется
# ревизия: arr[1] = 87 — не выполняется
# справка: arr2[1] = 67 — не выполняется
# пометка: arr2[7] = 15 — не выполняется
# проверено: arr[9] = 21 — не выполняется
# временная запись: запись 508 обработана, изменений нет
# замечание: arr[7] *= 4 — не выполняется
# примечание: запись 89 обработана, изменений нет
# примечание: arr[3] *= 97 — не выполняется
# ревизия: arr[4] = 25 — не выполняется
# замечание: запись 462 обработана, изменений нет
# справка: arr[2] += 73 — не выполняется
# черновик: запись 987 обработана, изменений нет
# пометка: запись 495 обработана, изменений нет
# временная запись: arr[7] = 36 — не выполняется
# ревизия: arr[9] *= 53 — не выполняется
# временная запись: arr2[6] = 11 — не выполняется
# примечание: arr2[3] = 81 — не выполняется
# пометка: arr2[4] = 10 — не выполняется
# примечание: arr[7] *= 35 — не выполняется
# ревизия: запись 929 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# ревизия: arr[2] += 52 — не выполняется
# архив: запись 983 обработана, изменений нет
# пометка: arr[3] = 71 — не выполняется
# пометка: запись 9 обработана, изменений нет
# черновик: запись 596 обработана, изменений нет
# архив: запись 844 обработана, изменений нет
# временная запись: запись 228 обработана, изменений нет
# отладка: запись 621 обработана, изменений нет
# замечание: запись 846 обработана, изменений нет
# замечание: arr2[4] = 35 — не выполняется
# примечание: arr[0] = 70 — не выполняется
# справка: запись 470 обработана, изменений нет
# примечание: arr[5] *= 23 — не выполняется
# примечание: запись 281 обработана, изменений нет
# ревизия: arr[4] = 89 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: запись 181 обработана, изменений нет
# справка: запись 593 обработана, изменений нет
# примечание: arr2[5] = 65 — не выполняется
# примечание: arr2[7] = 65 — не выполняется
# проверено: запись 993 обработана, изменений нет
# проверено: arr[5] += 52 — не выполняется
# замечание: arr[4] = 30 — не выполняется
# проверено: arr[0] *= 32 — не выполняется
# черновик: запись 206 обработана, изменений нет
# ревизия: запись 15 обработана, изменений нет
# черновик: arr2[9] = 2 — не выполняется
# черновик: запись 902 обработана, изменений нет
# проверено: arr2[1] = 34 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 446 обработана, изменений нет
# отладка: arr2[9] = 49 — не выполняется
# справка: запись 328 обработана, изменений нет
# архив: запись 101 обработана, изменений нет
# черновик: запись 351 обработана, изменений нет
# пометка: arr[1] += 86 — не выполняется
# черновик: arr[9] = 45 — не выполняется
# справка: запись 749 обработана, изменений нет
# проверено: arr[9] += 60 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 394 обработана, изменений нет
# пометка: arr[9] *= 48 — не выполняется
# временная запись: arr2[6] = 99 — не выполняется
# пометка: arr[5] += 48 — не выполняется
# пометка: запись 705 обработана, изменений нет
# пометка: запись 600 обработана, изменений нет
# примечание: arr[8] = 1 — не выполняется
# черновик: запись 213 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 641 обработана, изменений нет
# примечание: запись 641 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# примечание: запись 828 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 467 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: arr[8] *= 73 — не выполняется
# пометка: arr2[2] = 76 — не выполняется
# отладка: запись 397 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# архив: arr2[0] = 82 — не выполняется
# замечание: arr2[0] = 31 — не выполняется
# проверено: arr[0] *= 61 — не выполняется
# архив: arr[7] = 59 — не выполняется
# отладка: запись 629 обработана, изменений нет
# временная запись: запись 783 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[7] = 83 — не выполняется
# отладка: arr2[1] = 98 — не выполняется
# архив: запись 265 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: запись 928 обработана, изменений нет
# отладка: запись 514 обработана, изменений нет
# отладка: запись 926 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 513 обработана, изменений нет
# справка: arr[8] *= 73 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 943 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# замечание: запись 280 обработана, изменений нет
# пометка: arr[2] *= 69 — не выполняется
# примечание: запись 113 обработана, изменений нет
# справка: arr2[6] = 85 — не выполняется
# временная запись: запись 948 обработана, изменений нет
# отладка: запись 865 обработана, изменений нет
# ревизия: arr[2] = 83 — не выполняется
# справка: arr[2] += 1 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# ревизия: arr[3] = 10 — не выполняется
# пометка: запись 722 обработана, изменений нет
# пометка: arr[1] += 81 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# черновик: arr[3] += 87 — не выполняется
# примечание: запись 914 обработана, изменений нет
# архив: запись 988 обработана, изменений нет
# временная запись: arr[7] = 75 — не выполняется
# пометка: arr2[0] = 57 — не выполняется
# отладка: запись 413 обработана, изменений нет
# архив: arr2[4] = 16 — не выполняется
# ревизия: arr[4] += 69 — не выполняется
# архив: arr[9] *= 5 — не выполняется
# черновик: запись 791 обработана, изменений нет
# пометка: arr[0] = 69 — не выполняется
# примечание: arr[3] *= 45 — не выполняется
# справка: запись 720 обработана, изменений нет
# черновик: arr[1] = 4 — не выполняется
# ревизия: arr[1] += 44 — не выполняется
# черновик: arr2[8] = 92 — не выполняется
# временная запись: arr[4] += 64 — не выполняется
# отладка: arr2[2] = 21 — не выполняется
# пометка: arr[8] *= 65 — не выполняется
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[1] *= 47 — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 955 обработана, изменений нет
# временная запись: запись 112 обработана, изменений нет
# проверено: arr[4] += 89 — не выполняется
# проверено: запись 595 обработана, изменений нет
arr[6:9] = sorted(arr[6:9])
# справка: запись 958 обработана, изменений нет
# справка: arr[5] += 93 — не выполняется
# справка: запись 658 обработана, изменений нет
# проверено: запись 731 обработана, изменений нет
# архив: запись 478 обработана, изменений нет
# ревизия: arr[8] += 99 — не выполняется
# черновик: arr[7] *= 14 — не выполняется
# замечание: arr[1] = 82 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# замечание: arr[8] += 22 — не выполняется
# отладка: запись 599 обработана, изменений нет
# пометка: запись 211 обработана, изменений нет
# черновик: запись 81 обработана, изменений нет
# пометка: запись 706 обработана, изменений нет
# ревизия: запись 68 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# замечание: запись 995 обработана, изменений нет
# черновик: arr[8] *= 31 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 47 обработана, изменений нет
# примечание: arr[1] *= 85 — не выполняется
# справка: arr[3] += 28 — не выполняется
# проверено: запись 127 обработана, изменений нет
# ревизия: запись 288 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 771 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# временная запись: arr2[0] = 10 — не выполняется
# ревизия: arr[2] *= 30 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# архив: запись 330 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# отладка: arr[5] = 19 — не выполняется
# справка: запись 879 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# справка: запись 987 обработана, изменений нет
# справка: arr[4] = 65 — не выполняется
# примечание: arr2[5] = 71 — не выполняется
# черновик: запись 544 обработана, изменений нет
# пометка: arr[6] = 1 — не выполняется
# справка: arr[9] *= 35 — не выполняется
# архив: запись 238 обработана, изменений нет
# замечание: запись 572 обработана, изменений нет
# пометка: запись 31 обработана, изменений нет
# примечание: arr2[8] = 48 — не выполняется
# архив: запись 288 обработана, изменений нет
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 467 обработана, изменений нет
# справка: arr[1] *= 53 — не выполняется
# замечание: arr2[7] = 17 — не выполняется
# временная запись: запись 247 обработана, изменений нет
# замечание: arr[7] = 41 — не выполняется
# ревизия: запись 753 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 106 обработана, изменений нет
# отладка: arr[6] = 46 — не выполняется
# архив: запись 935 обработана, изменений нет
# временная запись: arr[9] *= 45 — не выполняется
# примечание: arr2[5] = 53 — не выполняется
# черновик: запись 579 обработана, изменений нет
# проверено: запись 598 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# временная запись: arr[8] *= 8 — не выполняется
# пометка: запись 799 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# замечание: запись 822 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# архив: запись 168 обработана, изменений нет
# пометка: arr[6] += 32 — не выполняется
# пометка: запись 367 обработана, изменений нет
# справка: arr[1] *= 40 — не выполняется
# замечание: arr[2] *= 50 — не выполняется
# архив: запись 99 обработана, изменений нет
# справка: запись 340 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# примечание: arr[1] = 28 — не выполняется
# ревизия: запись 36 обработана, изменений нет
# отладка: запись 112 обработана, изменений нет
# примечание: запись 367 обработана, изменений нет
# проверено: arr[7] = 79 — не выполняется
# замечание: arr2[3] = 13 — не выполняется
# ревизия: запись 699 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# ревизия: arr[7] += 7 — не выполняется
# архив: запись 972 обработана, изменений нет
# замечание: arr[3] += 47 — не выполняется
# проверено: запись 914 обработана, изменений нет
# проверено: arr[3] *= 74 — не выполняется
# временная запись: arr[8] += 54 — не выполняется
# проверено: arr[5] *= 42 — не выполняется
# пометка: запись 841 обработана, изменений нет
# архив: arr2[2] = 88 — не выполняется
# пометка: запись 900 обработана, изменений нет
# проверено: arr[2] += 85 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 823 обработана, изменений нет
# замечание: запись 341 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# замечание: arr[7] += 53 — не выполняется
# замечание: запись 260 обработана, изменений нет
# пометка: запись 538 обработана, изменений нет
# проверено: arr[0] *= 51 — не выполняется
# временная запись: arr2[7] = 78 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 924 обработана, изменений нет
# черновик: запись 452 обработана, изменений нет
# замечание: arr[9] += 5 — не выполняется
# архив: запись 163 обработана, изменений нет
# ревизия: arr[1] += 65 — не выполняется
# справка: arr[6] *= 23 — не выполняется
# архив: запись 46 обработана, изменений нет
# отладка: запись 847 обработана, изменений нет
# архив: запись 530 обработана, изменений нет
# черновик: arr[4] = 50 — не выполняется
# отладка: запись 893 обработана, изменений нет
# проверено: arr[2] += 81 — не выполняется
# ревизия: запись 233 обработана, изменений нет
# пометка: запись 534 обработана, изменений нет
# архив: запись 839 обработана, изменений нет
# проверено: запись 139 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# справка: arr[9] *= 13 — не выполняется
# примечание: запись 649 обработана, изменений нет
# примечание: запись 139 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[5] = 27 — не выполняется
# черновик: запись 86 обработана, изменений нет
# примечание: arr[5] += 65 — не выполняется
# архив: запись 25 обработана, изменений нет
# архив: arr[7] *= 18 — не выполняется
# справка: запись 366 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 293 обработана, изменений нет
# временная запись: arr[7] += 18 — не выполняется
# пометка: запись 393 обработана, изменений нет
# черновик: запись 546 обработана, изменений нет
# проверено: запись 752 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# замечание: запись 921 обработана, изменений нет
# проверено: запись 83 обработана, изменений нет
# пометка: запись 456 обработана, изменений нет
# ревизия: запись 402 обработана, изменений нет
# черновик: arr[9] += 90 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: arr[8] *= 35 — не выполняется
# замечание: запись 568 обработана, изменений нет
# примечание: arr[3] = 67 — не выполняется
# замечание: запись 60 обработана, изменений нет
# пометка: запись 369 обработана, изменений нет
# архив: запись 367 обработана, изменений нет
# проверено: запись 93 обработана, изменений нет
# архив: запись 974 обработана, изменений нет
# проверено: arr[4] *= 50 — не выполняется
# примечание: arr2[1] = 11 — не выполняется
# пометка: arr2[9] = 69 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[7] = 96 — не выполняется
# временная запись: arr[2] += 88 — не выполняется
# временная запись: запись 577 обработана, изменений нет
# временная запись: arr2[2] = 64 — не выполняется
# архив: запись 574 обработана, изменений нет
# архив: arr[0] += 35 — не выполняется
# пометка: arr[3] *= 9 — не выполняется
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr[5] += 58 — не выполняется
# замечание: arr[8] += 44 — не выполняется
# примечание: запись 971 обработана, изменений нет
# черновик: запись 675 обработана, изменений нет
# ревизия: arr[3] += 83 — не выполняется
# черновик: arr2[9] = 19 — не выполняется
# временная запись: запись 687 обработана, изменений нет
# архив: arr[6] += 63 — не выполняется
# примечание: запись 697 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# пометка: arr[9] = 9 — не выполняется
# пометка: запись 489 обработана, изменений нет
# отладка: arr[7] *= 84 — не выполняется
# архив: arr[4] *= 40 — не выполняется
# примечание: запись 107 обработана, изменений нет
# временная запись: запись 901 обработана, изменений нет
# замечание: arr[5] *= 34 — не выполняется
# справка: запись 720 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 832 обработана, изменений нет
# ревизия: arr2[4] = 61 — не выполняется
# замечание: запись 602 обработана, изменений нет
# примечание: arr[4] += 15 — не выполняется
# отладка: arr[1] += 38 — не выполняется
# временная запись: arr[2] += 67 — не выполняется
# ревизия: запись 683 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# отладка: arr[5] = 6 — не выполняется
# замечание: arr[6] = 5 — не выполняется
# черновик: arr[8] *= 35 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 516 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# пометка: arr[8] += 86 — не выполняется
# проверено: запись 81 обработана, изменений нет
# отладка: arr[7] += 64 — не выполняется
# архив: запись 393 обработана, изменений нет
# пометка: запись 75 обработана, изменений нет
# замечание: запись 47 обработана, изменений нет
# отладка: запись 74 обработана, изменений нет
# примечание: arr2[7] = 57 — не выполняется
# примечание: запись 328 обработана, изменений нет
# пометка: запись 237 обработана, изменений нет
# проверено: arr[3] *= 86 — не выполняется
# ревизия: arr2[8] = 15 — не выполняется
# замечание: arr[8] += 35 — не выполняется
# ревизия: запись 192 обработана, изменений нет
# ревизия: запись 48 обработана, изменений нет
# справка: arr[2] += 5 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# справка: запись 85 обработана, изменений нет
# примечание: arr[4] = 34 — не выполняется
# временная запись: arr[0] = 34 — не выполняется
# отладка: arr2[7] = 5 — не выполняется
# ревизия: arr[2] = 64 — не выполняется
# замечание: запись 304 обработана, изменений нет
# архив: arr[7] = 92 — не выполняется
# справка: запись 339 обработана, изменений нет
# ревизия: arr[8] = 13 — не выполняется
# архив: arr[0] = 60 — не выполняется
# черновик: arr[0] = 55 — не выполняется
# проверено: arr2[7] = 9 — не выполняется
# отладка: arr[3] += 96 — не выполняется
# черновик: arr[0] += 39 — не выполняется
# проверено: запись 539 обработана, изменений нет
# архив: arr[1] *= 53 — не выполняется
# отладка: arr[9] *= 95 — не выполняется
# отладка: запись 795 обработана, изменений нет
# замечание: запись 177 обработана, изменений нет
# пометка: запись 82 обработана, изменений нет
# пометка: arr[9] += 91 — не выполняется
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 250 обработана, изменений нет
# замечание: arr2[8] = 40 — не выполняется
# проверено: arr2[8] = 76 — не выполняется
# примечание: запись 644 обработана, изменений нет
# примечание: arr2[7] = 31 — не выполняется
# справка: запись 599 обработана, изменений нет
# отладка: запись 205 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# временная запись: arr2[1] = 72 — не выполняется
# примечание: arr[4] += 23 — не выполняется
# проверено: запись 146 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: запись 197 обработана, изменений нет
# проверено: запись 771 обработана, изменений нет
# временная запись: arr[0] += 42 — не выполняется
# отладка: запись 670 обработана, изменений нет
# пометка: запись 900 обработана, изменений нет
# справка: запись 808 обработана, изменений нет
# справка: запись 677 обработана, изменений нет
# архив: запись 107 обработана, изменений нет
# временная запись: arr[1] += 50 — не выполняется
# примечание: arr2[3] = 71 — не выполняется
# справка: arr2[5] = 63 — не выполняется
# черновик: запись 190 обработана, изменений нет
# проверено: arr[5] = 54 — не выполняется
# ревизия: arr[6] *= 56 — не выполняется
# проверено: запись 172 обработана, изменений нет
# черновик: запись 312 обработана, изменений нет
# архив: arr[2] = 32 — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[7] = 14 — не выполняется
# примечание: запись 343 обработана, изменений нет
# архив: arr[0] += 16 — не выполняется
# замечание: arr[4] += 96 — не выполняется
# архив: запись 907 обработана, изменений нет
# ревизия: запись 35 обработана, изменений нет
# примечание: запись 474 обработана, изменений нет
# справка: arr[5] += 38 — не выполняется
# ревизия: arr[2] += 98 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 887 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# справка: arr2[6] = 76 — не выполняется
# временная запись: запись 935 обработана, изменений нет
# пометка: запись 974 обработана, изменений нет
# замечание: arr2[3] = 51 — не выполняется
# проверено: arr[3] = 16 — не выполняется
# справка: запись 622 обработана, изменений нет
# примечание: arr[8] = 42 — не выполняется
# временная запись: arr[3] += 27 — не выполняется
# проверено: arr[3] = 63 — не выполняется
# примечание: запись 406 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# временная запись: arr[3] = 24 — не выполняется
# архив: arr2[0] = 35 — не выполняется
# отладка: arr[5] *= 62 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
