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
arr[3] *= 48
arr[0] += 19
arr[1] *= 25
arr[2] += 30
arr[5], arr[9] = arr[9], arr[5]
arr[9] *= 30
arr[1] *= 18
arr[5], arr[8] = arr[8], arr[5]
"""

TRAP_0 = "arr[7] = 919"
TRAP_1 = "arr[1] = 461"
TRAP_2 = "arr[9] = 313"
TRAP_3 = "arr[4] = 280"
TRAP_4 = "arr[4] = 994"
TRAP_5 = "arr[6] = 169"
TRAP_6 = "arr[1] = 102"
TRAP_7 = "arr[4] = 576"
TRAP_8 = "arr[0] = 505"
TRAP_9 = "arr[5] = 480"
TRAP_10 = "arr[3] = 296"
TRAP_11 = "arr[2] = 930"
TRAP_12 = "arr[5] = 882"
TRAP_13 = "arr[2] = 382"
TRAP_14 = "arr[7] = 215"
TRAP_15 = "arr[0] = 330"
TRAP_16 = "arr[9] = 321"
TRAP_17 = "arr[0] = 183"
TRAP_18 = "arr[2] = 943"
TRAP_19 = "arr[7] = 632"
TRAP_20 = "arr[2] = 126"
TRAP_21 = "arr[0] = 462"
TRAP_22 = "arr[7] = 515"
TRAP_23 = "arr[0] = 485"
TRAP_24 = "arr[0] = 611"
TRAP_25 = "arr[7] = 710"
TRAP_26 = "arr[9] = 403"
TRAP_27 = "arr[8] = 777"
TRAP_28 = "arr[2] = 145"
TRAP_29 = "arr[7] = 168"
TRAP_30 = "arr[3] = 195"
TRAP_31 = "arr[9] = 512"
TRAP_32 = "arr[9] = 332"
TRAP_33 = "arr[9] = 769"
TRAP_34 = "arr[0] = 136"
TRAP_35 = "arr[2] = 284"
TRAP_36 = "arr[4] = 755"
TRAP_37 = "arr[2] = 925"
TRAP_38 = "arr[4] = 414"
TRAP_39 = "arr[4] = 165"
TRAP_40 = "arr[6] = 330"
TRAP_41 = "arr[1] = 875"
TRAP_42 = "arr[4] = 927"
TRAP_43 = "arr[3] = 260"
TRAP_44 = "arr[0] = 912"
TRAP_45 = "arr[0] = 489"
TRAP_46 = "arr[1] = 398"
TRAP_47 = "arr[9] = 999"
TRAP_48 = "arr[9] = 778"
TRAP_49 = "arr[0] = 232"
TRAP_50 = "arr[4] = 280"
TRAP_51 = "arr[8] = 370"
TRAP_52 = "arr[6] = 877"
TRAP_53 = "arr[8] = 507"
TRAP_54 = "arr[4] = 238"
TRAP_55 = "arr[1] = 916"
TRAP_56 = "arr[8] = 392"
TRAP_57 = "arr[2] = 210"
TRAP_58 = "arr[6] = 600"
TRAP_59 = "arr[5] = 654"
TRAP_60 = "arr[7] = 770"
TRAP_61 = "arr[6] = 701"
TRAP_62 = "arr[7] = 587"
TRAP_63 = "arr[0] = 410"
TRAP_64 = "arr[7] = 716"
TRAP_65 = "arr[3] = 992"
TRAP_66 = "arr[2] = 124"
TRAP_67 = "arr[5] = 582"
TRAP_68 = "arr[5] = 464"
TRAP_69 = "arr[9] = 277"
TRAP_70 = "arr[4] = 707"
TRAP_71 = "arr[8] = 303"
TRAP_72 = "arr[8] = 346"
TRAP_73 = "arr[0] = 520"
TRAP_74 = "arr[6] = 923"
TRAP_75 = "arr[3] = 386"
TRAP_76 = "arr[6] = 160"
TRAP_77 = "arr[1] = 203"
TRAP_78 = "arr[9] = 595"
TRAP_79 = "arr[1] = 186"
TRAP_80 = "arr[6] = 568"
TRAP_81 = "arr[1] = 907"
TRAP_82 = "arr[8] = 767"
TRAP_83 = "arr[7] = 246"
TRAP_84 = "arr[0] = 315"
TRAP_85 = "arr[5] = 680"
TRAP_86 = "arr[2] = 960"
TRAP_87 = "arr[8] = 432"
TRAP_88 = "arr[5] = 794"
TRAP_89 = "arr[8] = 813"
TRAP_90 = "arr[6] = 583"
TRAP_91 = "arr[1] = 392"
TRAP_92 = "arr[8] = 464"
TRAP_93 = "arr[9] = 282"
TRAP_94 = "arr[6] = 533"
TRAP_95 = "arr[7] = 901"
TRAP_96 = "arr[3] = 455"
TRAP_97 = "arr[0] = 332"
TRAP_98 = "arr[9] = 800"
TRAP_99 = "arr[9] = 741"
TRAP_100 = "arr[7] = 233"
TRAP_101 = "arr[3] = 894"
TRAP_102 = "arr[1] = 765"
TRAP_103 = "arr[9] = 639"
TRAP_104 = "arr[2] = 376"
TRAP_105 = "arr[5] = 621"
TRAP_106 = "arr[1] = 253"
TRAP_107 = "arr[1] = 660"
TRAP_108 = "arr[8] = 596"
TRAP_109 = "arr[2] = 877"
TRAP_110 = "arr[2] = 299"
TRAP_111 = "arr[8] = 329"
TRAP_112 = "arr[2] = 618"
TRAP_113 = "arr[1] = 490"
TRAP_114 = "arr[2] = 454"
TRAP_115 = "arr[7] = 753"
TRAP_116 = "arr[5] = 183"
TRAP_117 = "arr[5] = 327"
TRAP_118 = "arr[7] = 706"
TRAP_119 = "arr[3] = 743"
TRAP_120 = "arr[1] = 547"
TRAP_121 = "arr[2] = 638"
TRAP_122 = "arr[4] = 444"
TRAP_123 = "arr[1] = 536"
TRAP_124 = "arr[8] = 737"
TRAP_125 = "arr[4] = 709"
TRAP_126 = "arr[5] = 287"
TRAP_127 = "arr[6] = 328"
TRAP_128 = "arr[7] = 181"
TRAP_129 = "arr[9] = 427"
TRAP_130 = "arr[5] = 252"
TRAP_131 = "arr[1] = 910"
TRAP_132 = "arr[1] = 946"
TRAP_133 = "arr[8] = 503"
TRAP_134 = "arr[0] = 300"
TRAP_135 = "arr[2] = 752"
TRAP_136 = "arr[1] = 507"
TRAP_137 = "arr[3] = 163"
TRAP_138 = "arr[1] = 486"
TRAP_139 = "arr[2] = 401"
TRAP_140 = "arr[7] = 602"
TRAP_141 = "arr[6] = 144"
TRAP_142 = "arr[8] = 899"
TRAP_143 = "arr[4] = 257"
TRAP_144 = "arr[8] = 212"
TRAP_145 = "arr[5] = 760"
TRAP_146 = "arr[6] = 564"
TRAP_147 = "arr[4] = 797"
TRAP_148 = "arr[9] = 208"
TRAP_149 = "arr[2] = 660"

arr = [5, 7, 14, 17, 28, 15, 2, 8, 26, 22]

tmp_0 = arr[2] + 36
note_1 = str(arr[4]) + str(arr[3])
label_2 = "запись 2 не применялась"
tmp_3 = arr[3] + 46
note_4 = str(arr[2]) + str(arr[5])
tmp_5 = arr[3] + 47
note_6 = str(arr[5]) + str(arr[9])
tmp_7 = arr[8] + 16
note_8 = str(arr[2]) + str(arr[1])
copy_9 = arr[8]
tmp_10 = arr[0] + 9
label_11 = "запись 11 не применялась"
code_12 = re.sub(r'[0-9]', '#', str(arr[9]))
note_13 = str(arr[0]) + str(arr[7])
tmp_14 = arr[6] + 44
copy_15 = arr[6]
code_16 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_17 = arr[4] + 2
label_18 = "запись 18 не применялась"
tmp_19 = arr[7] + 11
label_20 = "запись 20 не применялась"
label_21 = "запись 21 не применялась"
tmp_22 = arr[5] + 37
note_23 = str(arr[3]) + str(arr[2])
tmp_24 = arr[3] + 17
note_25 = str(arr[3]) + str(arr[9])
copy_26 = arr[9]
code_27 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_28 = arr[0]
note_29 = str(arr[4]) + str(arr[4])
tmp_30 = arr[4] + 15
label_31 = "запись 31 не применялась"
tmp_32 = arr[7] + 3
copy_33 = arr[0]
label_34 = "запись 34 не применялась"
label_35 = "запись 35 не применялась"
note_36 = str(arr[7]) + str(arr[9])
tmp_37 = arr[6] + 40
tmp_38 = arr[5] + 38
note_39 = str(arr[4]) + str(arr[9])
note_40 = str(arr[9]) + str(arr[8])
note_41 = str(arr[4]) + str(arr[6])
tmp_42 = arr[8] + 41
code_43 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_44 = arr[6] + 18
tmp_45 = arr[4] + 6
tmp_46 = arr[4] + 35
code_47 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_48 = arr[2]
tmp_49 = arr[3] + 10
note_50 = str(arr[9]) + str(arr[1])
note_51 = str(arr[3]) + str(arr[8])
tmp_52 = arr[5] + 7
copy_53 = arr[3]
tmp_54 = arr[1] + 5
note_55 = str(arr[5]) + str(arr[7])
tmp_56 = arr[5] + 6
label_57 = "запись 57 не применялась"
tmp_58 = arr[1] + 39
note_59 = str(arr[6]) + str(arr[1])
tmp_60 = arr[1] + 22
tmp_61 = arr[1] + 9
copy_62 = arr[6]
tmp_63 = arr[4] + 22
code_64 = re.sub(r'[0-9]', '#', str(arr[9]))
code_65 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_66 = arr[8] + 24
tmp_67 = arr[4] + 30
copy_68 = arr[6]
code_69 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_70 = arr[4] + 2
tmp_71 = arr[2] + 17
note_72 = str(arr[1]) + str(arr[9])
tmp_73 = arr[3] + 6
code_74 = re.sub(r'[0-9]', '#', str(arr[6]))
code_75 = re.sub(r'[0-9]', '#', str(arr[5]))
note_76 = str(arr[3]) + str(arr[1])
code_77 = re.sub(r'[0-9]', '#', str(arr[7]))
label_78 = "запись 78 не применялась"
code_79 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_80 = arr[3] + 45
note_81 = str(arr[5]) + str(arr[1])
code_82 = re.sub(r'[0-9]', '#', str(arr[5]))
code_83 = re.sub(r'[0-9]', '#', str(arr[2]))
label_84 = "запись 84 не применялась"
label_85 = "запись 85 не применялась"
tmp_86 = arr[0] + 1
note_87 = str(arr[7]) + str(arr[9])
tmp_88 = arr[6] + 49
code_89 = re.sub(r'[0-9]', '#', str(arr[6]))
note_90 = str(arr[5]) + str(arr[0])
note_91 = str(arr[5]) + str(arr[1])
note_92 = str(arr[8]) + str(arr[2])
code_93 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_94 = arr[1]
note_95 = str(arr[1]) + str(arr[2])
code_96 = re.sub(r'[0-9]', '#', str(arr[3]))
code_97 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_98 = arr[2]
note_99 = str(arr[2]) + str(arr[4])
code_100 = re.sub(r'[0-9]', '#', str(arr[3]))
note_101 = str(arr[0]) + str(arr[3])
code_102 = re.sub(r'[0-9]', '#', str(arr[1]))
code_103 = re.sub(r'[0-9]', '#', str(arr[6]))
note_104 = str(arr[9]) + str(arr[3])
tmp_105 = arr[8] + 45
note_106 = str(arr[4]) + str(arr[8])
copy_107 = arr[0]
code_108 = re.sub(r'[0-9]', '#', str(arr[2]))
code_109 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_110 = arr[7] + 11
code_111 = re.sub(r'[0-9]', '#', str(arr[8]))
note_112 = str(arr[9]) + str(arr[8])
code_113 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_114 = arr[8] + 40
copy_115 = arr[6]
tmp_116 = arr[7] + 32
code_117 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_118 = arr[2]
tmp_119 = arr[7] + 25
code_120 = re.sub(r'[0-9]', '#', str(arr[3]))
note_121 = str(arr[0]) + str(arr[1])
copy_122 = arr[6]
note_123 = str(arr[5]) + str(arr[4])
label_124 = "запись 124 не применялась"
copy_125 = arr[6]
note_126 = str(arr[1]) + str(arr[1])
label_127 = "запись 127 не применялась"
note_128 = str(arr[9]) + str(arr[9])
note_129 = str(arr[9]) + str(arr[3])
note_130 = str(arr[0]) + str(arr[3])
tmp_131 = arr[5] + 32
tmp_132 = arr[3] + 5
note_133 = str(arr[5]) + str(arr[6])
tmp_134 = arr[0] + 30
tmp_135 = arr[0] + 25
code_136 = re.sub(r'[0-9]', '#', str(arr[0]))
code_137 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_138 = arr[6] + 34
code_139 = re.sub(r'[0-9]', '#', str(arr[2]))
note_140 = str(arr[6]) + str(arr[5])
note_141 = str(arr[7]) + str(arr[5])
note_142 = str(arr[2]) + str(arr[3])
code_143 = re.sub(r'[0-9]', '#', str(arr[9]))
note_144 = str(arr[6]) + str(arr[5])
code_145 = re.sub(r'[0-9]', '#', str(arr[2]))
code_146 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_147 = arr[9] + 42
tmp_148 = arr[5] + 49
note_149 = str(arr[7]) + str(arr[2])
tmp_150 = arr[3] + 27
tmp_151 = arr[6] + 49
code_152 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_153 = arr[7] + 26
tmp_154 = arr[4] + 42
code_155 = re.sub(r'[0-9]', '#', str(arr[7]))
note_156 = str(arr[3]) + str(arr[6])
copy_157 = arr[2]
note_158 = str(arr[5]) + str(arr[7])
tmp_159 = arr[3] + 36
code_160 = re.sub(r'[0-9]', '#', str(arr[5]))
label_161 = "запись 161 не применялась"
label_162 = "запись 162 не применялась"
note_163 = str(arr[8]) + str(arr[4])
tmp_164 = arr[5] + 31
copy_165 = arr[7]
tmp_166 = arr[6] + 39
code_167 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_168 = arr[7]
tmp_169 = arr[1] + 43
note_170 = str(arr[4]) + str(arr[3])
code_171 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_172 = arr[0]
tmp_173 = arr[3] + 13
tmp_174 = arr[7] + 46
copy_175 = arr[3]
label_176 = "запись 176 не применялась"
code_177 = re.sub(r'[0-9]', '#', str(arr[7]))
code_178 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_179 = arr[1] + 40
note_180 = str(arr[7]) + str(arr[4])
code_181 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_182 = arr[8]
label_183 = "запись 183 не применялась"
note_184 = str(arr[8]) + str(arr[4])
code_185 = re.sub(r'[0-9]', '#', str(arr[6]))
note_186 = str(arr[5]) + str(arr[1])
code_187 = re.sub(r'[0-9]', '#', str(arr[6]))
note_188 = str(arr[5]) + str(arr[7])
tmp_189 = arr[2] + 39
copy_190 = arr[4]
tmp_191 = arr[3] + 40
label_192 = "запись 192 не применялась"
code_193 = re.sub(r'[0-9]', '#', str(arr[5]))
code_194 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_195 = arr[0]
copy_196 = arr[1]
copy_197 = arr[4]
note_198 = str(arr[1]) + str(arr[2])
code_199 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_200 = arr[2] + 42
note_201 = str(arr[7]) + str(arr[3])
copy_202 = arr[5]
note_203 = str(arr[4]) + str(arr[1])
tmp_204 = arr[6] + 7
note_205 = str(arr[1]) + str(arr[0])
label_206 = "запись 206 не применялась"
copy_207 = arr[2]
copy_208 = arr[2]
copy_209 = arr[6]
tmp_210 = arr[3] + 24
code_211 = re.sub(r'[0-9]', '#', str(arr[4]))
note_212 = str(arr[6]) + str(arr[0])
copy_213 = arr[7]
note_214 = str(arr[6]) + str(arr[6])
note_215 = str(arr[7]) + str(arr[6])
tmp_216 = arr[9] + 37
code_217 = re.sub(r'[0-9]', '#', str(arr[4]))
note_218 = str(arr[4]) + str(arr[5])
tmp_219 = arr[6] + 11
label_220 = "запись 220 не применялась"
note_221 = str(arr[8]) + str(arr[2])
tmp_222 = arr[9] + 34
tmp_223 = arr[4] + 2
tmp_224 = arr[9] + 21
copy_225 = arr[6]
code_226 = re.sub(r'[0-9]', '#', str(arr[1]))
code_227 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_228 = arr[7] + 4
tmp_229 = arr[8] + 19
note_230 = str(arr[8]) + str(arr[3])
tmp_231 = arr[2] + 30
code_232 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_233 = arr[3] + 21
tmp_234 = arr[3] + 27
code_235 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_236 = arr[2] + 34
tmp_237 = arr[4] + 29
label_238 = "запись 238 не применялась"
label_239 = "запись 239 не применялась"
tmp_240 = arr[7] + 17
code_241 = re.sub(r'[0-9]', '#', str(arr[6]))
note_242 = str(arr[8]) + str(arr[7])
tmp_243 = arr[4] + 26
note_244 = str(arr[6]) + str(arr[2])
tmp_245 = arr[6] + 29
note_246 = str(arr[0]) + str(arr[9])
tmp_247 = arr[5] + 44
tmp_248 = arr[6] + 43
note_249 = str(arr[2]) + str(arr[3])
tmp_250 = arr[2] + 46
copy_251 = arr[9]
tmp_252 = arr[6] + 18
code_253 = re.sub(r'[0-9]', '#', str(arr[6]))
note_254 = str(arr[9]) + str(arr[3])
note_255 = str(arr[4]) + str(arr[4])
copy_256 = arr[1]
tmp_257 = arr[5] + 13
label_258 = "запись 258 не применялась"
tmp_259 = arr[8] + 29
note_260 = str(arr[9]) + str(arr[2])
code_261 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_262 = arr[8] + 9
code_263 = re.sub(r'[0-9]', '#', str(arr[1]))
note_264 = str(arr[9]) + str(arr[6])
copy_265 = arr[5]
copy_266 = arr[0]
note_267 = str(arr[5]) + str(arr[7])
note_268 = str(arr[0]) + str(arr[6])
tmp_269 = arr[8] + 13
note_270 = str(arr[0]) + str(arr[6])
code_271 = re.sub(r'[0-9]', '#', str(arr[6]))
code_272 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_273 = arr[4]
code_274 = re.sub(r'[0-9]', '#', str(arr[1]))
code_275 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_276 = arr[8] + 43
copy_277 = arr[4]
tmp_278 = arr[2] + 34
label_279 = "запись 279 не применялась"
note_280 = str(arr[5]) + str(arr[3])
tmp_281 = arr[0] + 22
tmp_282 = arr[3] + 38
tmp_283 = arr[8] + 2
note_284 = str(arr[5]) + str(arr[0])
label_285 = "запись 285 не применялась"
note_286 = str(arr[3]) + str(arr[6])
code_287 = re.sub(r'[0-9]', '#', str(arr[7]))
note_288 = str(arr[6]) + str(arr[0])
code_289 = re.sub(r'[0-9]', '#', str(arr[9]))
label_290 = "запись 290 не применялась"
tmp_291 = arr[2] + 29
tmp_292 = arr[3] + 22
tmp_293 = arr[8] + 5
tmp_294 = arr[8] + 29
tmp_295 = arr[6] + 14
code_296 = re.sub(r'[0-9]', '#', str(arr[2]))
note_297 = str(arr[1]) + str(arr[2])
copy_298 = arr[0]
tmp_299 = arr[8] + 34
note_300 = str(arr[2]) + str(arr[1])
label_301 = "запись 301 не применялась"
code_302 = re.sub(r'[0-9]', '#', str(arr[6]))
note_303 = str(arr[2]) + str(arr[0])
code_304 = re.sub(r'[0-9]', '#', str(arr[8]))
note_305 = str(arr[1]) + str(arr[8])
tmp_306 = arr[6] + 48
copy_307 = arr[8]
note_308 = str(arr[3]) + str(arr[8])
note_309 = str(arr[2]) + str(arr[6])
tmp_310 = arr[3] + 45
code_311 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_312 = arr[4] + 42
tmp_313 = arr[4] + 35
code_314 = re.sub(r'[0-9]', '#', str(arr[4]))
code_315 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_316 = arr[5] + 26
tmp_317 = arr[3] + 22
copy_318 = arr[4]
tmp_319 = arr[5] + 24
code_320 = re.sub(r'[0-9]', '#', str(arr[6]))
code_321 = re.sub(r'[0-9]', '#', str(arr[6]))
code_322 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_323 = arr[7] + 7
code_324 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_325 = arr[4] + 49
tmp_326 = arr[1] + 10
code_327 = re.sub(r'[0-9]', '#', str(arr[9]))
code_328 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_329 = arr[5] + 17
copy_330 = arr[1]
label_331 = "запись 331 не применялась"
copy_332 = arr[6]
tmp_333 = arr[3] + 14
label_334 = "запись 334 не применялась"
tmp_335 = arr[7] + 37
tmp_336 = arr[0] + 46
label_337 = "запись 337 не применялась"
copy_338 = arr[7]
note_339 = str(arr[7]) + str(arr[6])
note_340 = str(arr[1]) + str(arr[2])
label_341 = "запись 341 не применялась"
code_342 = re.sub(r'[0-9]', '#', str(arr[2]))
note_343 = str(arr[4]) + str(arr[1])
note_344 = str(arr[7]) + str(arr[7])
note_345 = str(arr[7]) + str(arr[5])
note_346 = str(arr[0]) + str(arr[4])
note_347 = str(arr[5]) + str(arr[9])
tmp_348 = arr[2] + 38
code_349 = re.sub(r'[0-9]', '#', str(arr[2]))
note_350 = str(arr[3]) + str(arr[1])
tmp_351 = arr[7] + 2
tmp_352 = arr[3] + 17
copy_353 = arr[9]
tmp_354 = arr[5] + 37
tmp_355 = arr[6] + 33
note_356 = str(arr[0]) + str(arr[5])
tmp_357 = arr[0] + 29
copy_358 = arr[8]
code_359 = re.sub(r'[0-9]', '#', str(arr[3]))
note_360 = str(arr[5]) + str(arr[2])
copy_361 = arr[0]
tmp_362 = arr[9] + 7
tmp_363 = arr[7] + 12
note_364 = str(arr[1]) + str(arr[9])
note_365 = str(arr[0]) + str(arr[3])
tmp_366 = arr[2] + 29
tmp_367 = arr[7] + 49
label_368 = "запись 368 не применялась"
note_369 = str(arr[4]) + str(arr[8])
copy_370 = arr[7]
tmp_371 = arr[0] + 38
label_372 = "запись 372 не применялась"
code_373 = re.sub(r'[0-9]', '#', str(arr[0]))
note_374 = str(arr[7]) + str(arr[7])
note_375 = str(arr[0]) + str(arr[7])
tmp_376 = arr[4] + 37
label_377 = "запись 377 не применялась"
label_378 = "запись 378 не применялась"
note_379 = str(arr[5]) + str(arr[7])
tmp_380 = arr[4] + 29
tmp_381 = arr[9] + 4
label_382 = "запись 382 не применялась"
note_383 = str(arr[6]) + str(arr[6])
note_384 = str(arr[9]) + str(arr[6])
note_385 = str(arr[6]) + str(arr[4])
note_386 = str(arr[8]) + str(arr[5])
copy_387 = arr[5]
label_388 = "запись 388 не применялась"
note_389 = str(arr[9]) + str(arr[6])
note_390 = str(arr[8]) + str(arr[1])
copy_391 = arr[2]
tmp_392 = arr[6] + 39
code_393 = re.sub(r'[0-9]', '#', str(arr[1]))
label_394 = "запись 394 не применялась"
tmp_395 = arr[5] + 5
tmp_396 = arr[6] + 29
code_397 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_398 = arr[5] + 48
note_399 = str(arr[7]) + str(arr[8])
tmp_400 = arr[3] + 14
code_401 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_402 = arr[6] + 26
tmp_403 = arr[9] + 41
note_404 = str(arr[7]) + str(arr[4])
tmp_405 = arr[0] + 9
code_406 = re.sub(r'[0-9]', '#', str(arr[2]))
label_407 = "запись 407 не применялась"
note_408 = str(arr[9]) + str(arr[2])
copy_409 = arr[1]
note_410 = str(arr[9]) + str(arr[9])
code_411 = re.sub(r'[0-9]', '#', str(arr[3]))
label_412 = "запись 412 не применялась"
tmp_413 = arr[7] + 20
note_414 = str(arr[6]) + str(arr[7])
label_415 = "запись 415 не применялась"
tmp_416 = arr[4] + 4
tmp_417 = arr[5] + 23
note_418 = str(arr[8]) + str(arr[0])
code_419 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_420 = arr[1]
note_421 = str(arr[5]) + str(arr[7])
label_422 = "запись 422 не применялась"
note_423 = str(arr[5]) + str(arr[7])
code_424 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_425 = arr[6] + 39
copy_426 = arr[0]
note_427 = str(arr[4]) + str(arr[6])
copy_428 = arr[9]
code_429 = re.sub(r'[0-9]', '#', str(arr[6]))
note_430 = str(arr[9]) + str(arr[8])
tmp_431 = arr[2] + 12
tmp_432 = arr[2] + 26
note_433 = str(arr[8]) + str(arr[9])
code_434 = re.sub(r'[0-9]', '#', str(arr[8]))
note_435 = str(arr[2]) + str(arr[1])
note_436 = str(arr[9]) + str(arr[0])
label_437 = "запись 437 не применялась"
note_438 = str(arr[1]) + str(arr[0])
tmp_439 = arr[7] + 37
tmp_440 = arr[0] + 35
tmp_441 = arr[1] + 34
tmp_442 = arr[0] + 47
note_443 = str(arr[8]) + str(arr[3])
note_444 = str(arr[0]) + str(arr[1])
note_445 = str(arr[1]) + str(arr[1])
note_446 = str(arr[4]) + str(arr[0])
label_447 = "запись 447 не применялась"
note_448 = str(arr[2]) + str(arr[6])
code_449 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_450 = arr[5] + 24
tmp_451 = arr[3] + 2
note_452 = str(arr[3]) + str(arr[6])
copy_453 = arr[7]
code_454 = re.sub(r'[0-9]', '#', str(arr[5]))
note_455 = str(arr[9]) + str(arr[5])
tmp_456 = arr[0] + 19
code_457 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_458 = arr[5] + 29
code_459 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_460 = arr[6] + 28
note_461 = str(arr[7]) + str(arr[9])
note_462 = str(arr[3]) + str(arr[1])
tmp_463 = arr[7] + 25
note_464 = str(arr[0]) + str(arr[3])
code_465 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_466 = arr[1] + 23
note_467 = str(arr[8]) + str(arr[1])
tmp_468 = arr[1] + 16
note_469 = str(arr[4]) + str(arr[3])
label_470 = "запись 470 не применялась"
label_471 = "запись 471 не применялась"
note_472 = str(arr[3]) + str(arr[7])
code_473 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_474 = arr[1]
note_475 = str(arr[6]) + str(arr[2])
code_476 = re.sub(r'[0-9]', '#', str(arr[1]))
code_477 = re.sub(r'[0-9]', '#', str(arr[5]))
code_478 = re.sub(r'[0-9]', '#', str(arr[0]))
code_479 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_480 = arr[0]
label_481 = "запись 481 не применялась"
tmp_482 = arr[9] + 45
label_483 = "запись 483 не применялась"
note_484 = str(arr[3]) + str(arr[6])
code_485 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_486 = arr[4]
code_487 = re.sub(r'[0-9]', '#', str(arr[2]))
note_488 = str(arr[0]) + str(arr[3])
tmp_489 = arr[2] + 49
label_490 = "запись 490 не применялась"
code_491 = re.sub(r'[0-9]', '#', str(arr[5]))
code_492 = re.sub(r'[0-9]', '#', str(arr[0]))
code_493 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_494 = arr[4] + 48
tmp_495 = arr[8] + 32
note_496 = str(arr[6]) + str(arr[7])
note_497 = str(arr[5]) + str(arr[7])
code_498 = re.sub(r'[0-9]', '#', str(arr[6]))
label_499 = "запись 499 не применялась"
code_500 = re.sub(r'[0-9]', '#', str(arr[3]))
code_501 = re.sub(r'[0-9]', '#', str(arr[8]))
note_502 = str(arr[1]) + str(arr[4])
copy_503 = arr[0]
note_504 = str(arr[5]) + str(arr[0])
code_505 = re.sub(r'[0-9]', '#', str(arr[9]))
code_506 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_507 = arr[6] + 10
tmp_508 = arr[4] + 21
copy_509 = arr[7]
tmp_510 = arr[6] + 40
note_511 = str(arr[1]) + str(arr[1])
copy_512 = arr[9]
copy_513 = arr[2]
note_514 = str(arr[0]) + str(arr[6])
note_515 = str(arr[2]) + str(arr[9])
code_516 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_517 = arr[8]
tmp_518 = arr[8] + 29
tmp_519 = arr[1] + 47
tmp_520 = arr[9] + 43
note_521 = str(arr[5]) + str(arr[8])
note_522 = str(arr[9]) + str(arr[5])
note_523 = str(arr[7]) + str(arr[9])
tmp_524 = arr[8] + 41
code_525 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_526 = arr[1] + 26
tmp_527 = arr[9] + 13
copy_528 = arr[5]
code_529 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_530 = arr[9] + 7
note_531 = str(arr[2]) + str(arr[7])
tmp_532 = arr[8] + 25
note_533 = str(arr[3]) + str(arr[2])
tmp_534 = arr[0] + 32
code_535 = re.sub(r'[0-9]', '#', str(arr[5]))
note_536 = str(arr[5]) + str(arr[9])
note_537 = str(arr[5]) + str(arr[3])
tmp_538 = arr[2] + 38
code_539 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_540 = arr[4]
tmp_541 = arr[2] + 25
code_542 = re.sub(r'[0-9]', '#', str(arr[6]))
code_543 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_544 = arr[6]
tmp_545 = arr[7] + 16
code_546 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_547 = arr[9] + 13
label_548 = "запись 548 не применялась"
label_549 = "запись 549 не применялась"
code_550 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_551 = arr[3] + 19
tmp_552 = arr[2] + 4
code_553 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_554 = arr[8] + 25
copy_555 = arr[3]
code_556 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_557 = arr[7] + 49
label_558 = "запись 558 не применялась"
tmp_559 = arr[2] + 3
code_560 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_561 = arr[9] + 5
note_562 = str(arr[8]) + str(arr[0])
note_563 = str(arr[1]) + str(arr[0])
tmp_564 = arr[8] + 24
label_565 = "запись 565 не применялась"
code_566 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_567 = arr[3]
note_568 = str(arr[9]) + str(arr[5])
label_569 = "запись 569 не применялась"
label_570 = "запись 570 не применялась"
copy_571 = arr[9]
code_572 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_573 = arr[8]
copy_574 = arr[9]
label_575 = "запись 575 не применялась"
tmp_576 = arr[4] + 47
copy_577 = arr[9]
label_578 = "запись 578 не применялась"
label_579 = "запись 579 не применялась"
label_580 = "запись 580 не применялась"
copy_581 = arr[1]
copy_582 = arr[1]
tmp_583 = arr[5] + 42
note_584 = str(arr[9]) + str(arr[1])
note_585 = str(arr[0]) + str(arr[5])
tmp_586 = arr[9] + 22
label_587 = "запись 587 не применялась"
tmp_588 = arr[6] + 45
tmp_589 = arr[6] + 43
code_590 = re.sub(r'[0-9]', '#', str(arr[8]))
note_591 = str(arr[1]) + str(arr[1])
tmp_592 = arr[8] + 44
tmp_593 = arr[6] + 46
label_594 = "запись 594 не применялась"
code_595 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_596 = arr[8] + 2
copy_597 = arr[0]
tmp_598 = arr[4] + 38
label_599 = "запись 599 не применялась"
tmp_600 = arr[6] + 30
code_601 = re.sub(r'[0-9]', '#', str(arr[6]))
code_602 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_603 = arr[9] + 4
label_604 = "запись 604 не применялась"
code_605 = re.sub(r'[0-9]', '#', str(arr[2]))
note_606 = str(arr[9]) + str(arr[5])
copy_607 = arr[2]
code_608 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_609 = arr[3] + 2
tmp_610 = arr[7] + 25
copy_611 = arr[9]
copy_612 = arr[2]
code_613 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_614 = arr[8] + 21
label_615 = "запись 615 не применялась"
note_616 = str(arr[5]) + str(arr[6])
copy_617 = arr[9]
label_618 = "запись 618 не применялась"
label_619 = "запись 619 не применялась"
code_620 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_621 = arr[6] + 21
note_622 = str(arr[8]) + str(arr[1])
tmp_623 = arr[5] + 47
tmp_624 = arr[0] + 1
label_625 = "запись 625 не применялась"
copy_626 = arr[8]
code_627 = re.sub(r'[0-9]', '#', str(arr[2]))
note_628 = str(arr[6]) + str(arr[1])
label_629 = "запись 629 не применялась"
tmp_630 = arr[1] + 50
code_631 = re.sub(r'[0-9]', '#', str(arr[2]))
code_632 = re.sub(r'[0-9]', '#', str(arr[2]))
code_633 = re.sub(r'[0-9]', '#', str(arr[0]))
code_634 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_635 = arr[3] + 22
note_636 = str(arr[9]) + str(arr[4])
note_637 = str(arr[7]) + str(arr[3])
code_638 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_639 = arr[0] + 35
note_640 = str(arr[6]) + str(arr[2])
code_641 = re.sub(r'[0-9]', '#', str(arr[9]))
label_642 = "запись 642 не применялась"
tmp_643 = arr[3] + 18
tmp_644 = arr[6] + 22
tmp_645 = arr[2] + 22
copy_646 = arr[5]
note_647 = str(arr[5]) + str(arr[1])
code_648 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_649 = arr[8]
tmp_650 = arr[9] + 47
copy_651 = arr[0]
tmp_652 = arr[0] + 13
tmp_653 = arr[7] + 38
tmp_654 = arr[2] + 17
note_655 = str(arr[4]) + str(arr[3])
note_656 = str(arr[4]) + str(arr[4])
note_657 = str(arr[1]) + str(arr[3])
note_658 = str(arr[7]) + str(arr[4])
tmp_659 = arr[2] + 6
code_660 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_661 = arr[4] + 25
note_662 = str(arr[4]) + str(arr[0])
code_663 = re.sub(r'[0-9]', '#', str(arr[5]))
code_664 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_665 = arr[1]
copy_666 = arr[6]
note_667 = str(arr[8]) + str(arr[6])
tmp_668 = arr[9] + 21
code_669 = re.sub(r'[0-9]', '#', str(arr[1]))
note_670 = str(arr[3]) + str(arr[9])
copy_671 = arr[6]
tmp_672 = arr[5] + 22
tmp_673 = arr[8] + 29
tmp_674 = arr[5] + 18
copy_675 = arr[1]
code_676 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_677 = arr[0] + 47
tmp_678 = arr[1] + 2
tmp_679 = arr[5] + 20
code_680 = re.sub(r'[0-9]', '#', str(arr[9]))
note_681 = str(arr[2]) + str(arr[7])
copy_682 = arr[1]
tmp_683 = arr[2] + 32
tmp_684 = arr[5] + 18
note_685 = str(arr[0]) + str(arr[9])
copy_686 = arr[2]
code_687 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_688 = arr[1]
copy_689 = arr[0]
code_690 = re.sub(r'[0-9]', '#', str(arr[1]))
code_691 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_692 = arr[1]
code_693 = re.sub(r'[0-9]', '#', str(arr[6]))
code_694 = re.sub(r'[0-9]', '#', str(arr[6]))
code_695 = re.sub(r'[0-9]', '#', str(arr[7]))
note_696 = str(arr[6]) + str(arr[0])
code_697 = re.sub(r'[0-9]', '#', str(arr[5]))
label_698 = "запись 698 не применялась"
tmp_699 = arr[1] + 20
note_700 = str(arr[2]) + str(arr[4])
copy_701 = arr[8]
label_702 = "запись 702 не применялась"
label_703 = "запись 703 не применялась"
tmp_704 = arr[9] + 29
note_705 = str(arr[3]) + str(arr[8])
tmp_706 = arr[6] + 30
label_707 = "запись 707 не применялась"
tmp_708 = arr[9] + 2
label_709 = "запись 709 не применялась"
tmp_710 = arr[6] + 22
tmp_711 = arr[7] + 50
label_712 = "запись 712 не применялась"
code_713 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_714 = arr[9] + 45
copy_715 = arr[4]
copy_716 = arr[6]
tmp_717 = arr[8] + 24
label_718 = "запись 718 не применялась"
code_719 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_720 = arr[3] + 6
tmp_721 = arr[1] + 23
tmp_722 = arr[7] + 12
tmp_723 = arr[1] + 24
tmp_724 = arr[8] + 28
note_725 = str(arr[2]) + str(arr[6])
code_726 = re.sub(r'[0-9]', '#', str(arr[4]))
note_727 = str(arr[5]) + str(arr[7])
note_728 = str(arr[0]) + str(arr[9])
note_729 = str(arr[1]) + str(arr[4])
note_730 = str(arr[1]) + str(arr[3])
label_731 = "запись 731 не применялась"
tmp_732 = arr[3] + 28
code_733 = re.sub(r'[0-9]', '#', str(arr[0]))
code_734 = re.sub(r'[0-9]', '#', str(arr[4]))
note_735 = str(arr[7]) + str(arr[0])
tmp_736 = arr[2] + 37
note_737 = str(arr[0]) + str(arr[6])
tmp_738 = arr[9] + 1
code_739 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_740 = arr[7] + 11
copy_741 = arr[5]
code_742 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_743 = arr[0] + 42
note_744 = str(arr[6]) + str(arr[3])
note_745 = str(arr[6]) + str(arr[0])
label_746 = "запись 746 не применялась"
tmp_747 = arr[1] + 26
tmp_748 = arr[2] + 12
code_749 = re.sub(r'[0-9]', '#', str(arr[0]))
note_750 = str(arr[7]) + str(arr[6])
code_751 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_752 = arr[4] + 6
label_753 = "запись 753 не применялась"
note_754 = str(arr[1]) + str(arr[4])
note_755 = str(arr[3]) + str(arr[4])
note_756 = str(arr[2]) + str(arr[5])
label_757 = "запись 757 не применялась"
copy_758 = arr[4]
note_759 = str(arr[1]) + str(arr[5])
tmp_760 = arr[7] + 36
note_761 = str(arr[7]) + str(arr[7])
label_762 = "запись 762 не применялась"
note_763 = str(arr[7]) + str(arr[7])
tmp_764 = arr[0] + 36
note_765 = str(arr[3]) + str(arr[1])
code_766 = re.sub(r'[0-9]', '#', str(arr[7]))
code_767 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_768 = arr[1] + 47
tmp_769 = arr[6] + 38
tmp_770 = arr[2] + 17
code_771 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_772 = arr[6]
tmp_773 = arr[4] + 50
copy_774 = arr[0]
copy_775 = arr[9]
code_776 = re.sub(r'[0-9]', '#', str(arr[3]))
note_777 = str(arr[5]) + str(arr[8])
code_778 = re.sub(r'[0-9]', '#', str(arr[9]))
note_779 = str(arr[6]) + str(arr[3])
note_780 = str(arr[3]) + str(arr[6])
tmp_781 = arr[5] + 15
code_782 = re.sub(r'[0-9]', '#', str(arr[3]))
label_783 = "запись 783 не применялась"
copy_784 = arr[6]
code_785 = re.sub(r'[0-9]', '#', str(arr[9]))
note_786 = str(arr[6]) + str(arr[6])
tmp_787 = arr[5] + 13
copy_788 = arr[9]
note_789 = str(arr[8]) + str(arr[9])
tmp_790 = arr[6] + 47
tmp_791 = arr[9] + 47
tmp_792 = arr[3] + 37
label_793 = "запись 793 не применялась"
label_794 = "запись 794 не применялась"
note_795 = str(arr[5]) + str(arr[1])
note_796 = str(arr[8]) + str(arr[0])
copy_797 = arr[0]
label_798 = "запись 798 не применялась"
note_799 = str(arr[0]) + str(arr[9])

t588 = str(arr[7]) + str(arr[2])
# справка: arr2[6] = 70 — не выполняется
# архив: arr[8] = 3 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr[1] = 65 — не выполняется
# отладка: запись 633 обработана, изменений нет
# отладка: запись 461 обработана, изменений нет
# проверено: запись 716 обработана, изменений нет
# архив: запись 138 обработана, изменений нет
# справка: запись 550 обработана, изменений нет
# пометка: запись 128 обработана, изменений нет
# отладка: запись 598 обработана, изменений нет
# временная запись: запись 31 обработана, изменений нет
# архив: запись 265 обработана, изменений нет
# архив: arr[8] += 52 — не выполняется
# архив: запись 130 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# справка: запись 961 обработана, изменений нет
# примечание: запись 810 обработана, изменений нет
# черновик: запись 527 обработана, изменений нет
# справка: запись 929 обработана, изменений нет
# ревизия: arr[1] *= 28 — не выполняется
# пометка: arr[4] += 35 — не выполняется
# замечание: запись 347 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# проверено: arr[4] = 79 — не выполняется
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 115 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 585 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[0] = 79 — не выполняется
# отладка: запись 39 обработана, изменений нет
# архив: arr[9] = 32 — не выполняется
# архив: arr[0] *= 88 — не выполняется
# временная запись: запись 708 обработана, изменений нет
# архив: arr2[3] = 27 — не выполняется
# архив: запись 7 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# примечание: запись 21 обработана, изменений нет
# проверено: запись 676 обработана, изменений нет
# примечание: arr[0] += 88 — не выполняется
# временная запись: запись 406 обработана, изменений нет
# пометка: arr[6] = 1 — не выполняется
# временная запись: запись 835 обработана, изменений нет
# отладка: arr2[7] = 80 — не выполняется
# замечание: arr2[2] = 17 — не выполняется
# черновик: arr[8] *= 98 — не выполняется
# проверено: arr[0] += 19 — не выполняется
# справка: arr2[6] = 97 — не выполняется
# проверено: arr[2] = 23 — не выполняется
# ревизия: запись 295 обработана, изменений нет
# пометка: arr[0] *= 68 — не выполняется
# примечание: запись 52 обработана, изменений нет
# проверено: arr[9] += 84 — не выполняется
# замечание: arr[9] = 87 — не выполняется
# архив: запись 209 обработана, изменений нет
# замечание: запись 350 обработана, изменений нет
# справка: запись 182 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[1] += 67 — не выполняется
# замечание: arr[5] *= 21 — не выполняется
# проверено: запись 960 обработана, изменений нет
# черновик: arr[5] += 71 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: arr[5] *= 23 — не выполняется
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr[9] *= 89 — не выполняется
# отладка: arr[0] *= 57 — не выполняется
# отладка: arr2[8] = 6 — не выполняется
# ревизия: запись 543 обработана, изменений нет
# справка: arr[9] += 4 — не выполняется
# ревизия: arr[6] += 54 — не выполняется
# примечание: arr[9] += 71 — не выполняется
# пометка: arr[2] = 80 — не выполняется
# отладка: arr[6] *= 73 — не выполняется
# отладка: запись 206 обработана, изменений нет
# справка: запись 308 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr2[6] = 48 — не выполняется
# черновик: запись 158 обработана, изменений нет
# черновик: запись 650 обработана, изменений нет
# архив: запись 478 обработана, изменений нет
# черновик: запись 113 обработана, изменений нет
# справка: arr[4] = 58 — не выполняется
# замечание: arr[4] *= 20 — не выполняется
# замечание: arr[0] *= 32 — не выполняется
# отладка: запись 597 обработана, изменений нет
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 837 обработана, изменений нет
# пометка: запись 501 обработана, изменений нет
# ревизия: запись 543 обработана, изменений нет
# пометка: запись 310 обработана, изменений нет
# проверено: arr[7] += 92 — не выполняется
# пометка: запись 243 обработана, изменений нет
# черновик: arr[1] += 64 — не выполняется
# черновик: запись 896 обработана, изменений нет
# черновик: запись 645 обработана, изменений нет
# временная запись: arr[2] *= 26 — не выполняется
# примечание: запись 161 обработана, изменений нет
# пометка: arr[0] += 62 — не выполняется
# архив: arr[5] *= 82 — не выполняется
# замечание: arr[2] += 12 — не выполняется
# примечание: arr[5] = 13 — не выполняется
# пометка: arr2[4] = 58 — не выполняется
# пометка: arr[6] *= 95 — не выполняется
# примечание: arr[6] += 23 — не выполняется
# временная запись: arr[0] = 10 — не выполняется
# архив: запись 263 обработана, изменений нет
# ревизия: запись 416 обработана, изменений нет
# примечание: запись 153 обработана, изменений нет
# примечание: запись 461 обработана, изменений нет
# временная запись: arr[4] = 82 — не выполняется
# временная запись: запись 306 обработана, изменений нет
# справка: arr2[1] = 96 — не выполняется
# пометка: запись 174 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# временная запись: запись 747 обработана, изменений нет
# черновик: запись 358 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 406 обработана, изменений нет
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[8] = 68 — не выполняется
# ревизия: запись 864 обработана, изменений нет
# ревизия: запись 3 обработана, изменений нет
# ревизия: arr[8] = 85 — не выполняется
# временная запись: запись 964 обработана, изменений нет
# справка: arr2[0] = 66 — не выполняется
# временная запись: arr[2] = 20 — не выполняется
# примечание: arr[5] += 4 — не выполняется
# проверено: запись 356 обработана, изменений нет
# замечание: запись 665 обработана, изменений нет
# временная запись: arr2[9] = 75 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: запись 689 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# отладка: arr[2] += 34 — не выполняется
# пометка: запись 593 обработана, изменений нет
# черновик: arr[2] += 63 — не выполняется
# примечание: arr2[3] = 98 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: запись 38 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 697 обработана, изменений нет
# черновик: запись 495 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 494 обработана, изменений нет
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 42 обработана, изменений нет
# черновик: arr[9] = 40 — не выполняется
# замечание: запись 768 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[7] += 37 — не выполняется
# замечание: запись 343 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr[2] *= 66 — не выполняется
# черновик: запись 366 обработана, изменений нет
# временная запись: arr2[9] = 81 — не выполняется
# черновик: запись 391 обработана, изменений нет
# ревизия: запись 940 обработана, изменений нет
# архив: запись 988 обработана, изменений нет
# примечание: arr[2] = 66 — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 159 обработана, изменений нет
# пометка: запись 947 обработана, изменений нет
# отладка: arr[7] += 50 — не выполняется
# ревизия: запись 75 обработана, изменений нет
# замечание: arr[4] += 31 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# пометка: запись 592 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# временная запись: запись 7 обработана, изменений нет
# пометка: arr[6] = 33 — не выполняется
# замечание: запись 383 обработана, изменений нет
# справка: arr[9] *= 1 — не выполняется
# примечание: arr2[2] = 62 — не выполняется
# архив: arr[7] *= 76 — не выполняется
# временная запись: запись 875 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 959 обработана, изменений нет
# справка: запись 943 обработана, изменений нет
# ревизия: arr[1] = 85 — не выполняется
# черновик: запись 509 обработана, изменений нет
# примечание: запись 273 обработана, изменений нет
# пометка: запись 139 обработана, изменений нет
# черновик: запись 6 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# черновик: arr[4] *= 59 — не выполняется
# пометка: arr[6] = 26 — не выполняется
# замечание: запись 922 обработана, изменений нет
# справка: запись 120 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# временная запись: arr[0] += 89 — не выполняется
# черновик: запись 559 обработана, изменений нет
# временная запись: arr[2] *= 80 — не выполняется
# отладка: arr[8] *= 40 — не выполняется
# пометка: запись 395 обработана, изменений нет
# черновик: arr2[4] = 39 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 932 обработана, изменений нет
# справка: arr[4] *= 60 — не выполняется
# черновик: arr[7] = 30 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: запись 584 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: запись 415 обработана, изменений нет
# замечание: arr[5] *= 44 — не выполняется
# пометка: запись 396 обработана, изменений нет
# пометка: запись 384 обработана, изменений нет
# ревизия: arr[1] *= 99 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: запись 26 обработана, изменений нет
# проверено: запись 803 обработана, изменений нет
# примечание: запись 323 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[7] *= 9 — не выполняется
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 546 обработана, изменений нет
# ревизия: arr[5] *= 3 — не выполняется
# примечание: arr[1] = 53 — не выполняется
# пометка: arr[9] *= 98 — не выполняется
# справка: arr2[8] = 62 — не выполняется
# пометка: запись 949 обработана, изменений нет
# справка: запись 842 обработана, изменений нет
# пометка: arr[1] *= 23 — не выполняется
# проверено: запись 240 обработана, изменений нет
# черновик: arr[5] += 70 — не выполняется
# пометка: запись 693 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[7] = 46 — не выполняется
# черновик: запись 566 обработана, изменений нет
# примечание: запись 254 обработана, изменений нет
# проверено: запись 6 обработана, изменений нет
# ревизия: запись 21 обработана, изменений нет
# справка: arr2[1] = 82 — не выполняется
# замечание: arr[6] = 3 — не выполняется
# черновик: запись 131 обработана, изменений нет
# отладка: arr[2] += 53 — не выполняется
# пометка: arr2[7] = 53 — не выполняется
# отладка: arr[8] = 96 — не выполняется
# справка: запись 487 обработана, изменений нет
# примечание: запись 867 обработана, изменений нет
# архив: arr[2] = 69 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr2[4] = 17 — не выполняется
# справка: запись 62 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# замечание: запись 673 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# отладка: arr[8] *= 51 — не выполняется
# справка: запись 45 обработана, изменений нет
# ревизия: arr2[4] = 25 — не выполняется
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: arr[2] += 42 — не выполняется
# архив: запись 686 обработана, изменений нет
# отладка: запись 570 обработана, изменений нет
# замечание: запись 311 обработана, изменений нет
# справка: arr[1] *= 39 — не выполняется
# примечание: запись 242 обработана, изменений нет
# ревизия: запись 824 обработана, изменений нет
# проверено: arr[7] = 3 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: запись 433 обработана, изменений нет
# замечание: arr[1] = 98 — не выполняется
# справка: arr[8] *= 68 — не выполняется
# примечание: запись 193 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# проверено: запись 177 обработана, изменений нет
# примечание: arr2[2] = 71 — не выполняется
# примечание: запись 759 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr[0] += 88 — не выполняется
# временная запись: arr[9] += 9 — не выполняется
# пометка: arr[4] = 95 — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[1] = 88 — не выполняется
# замечание: запись 354 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# черновик: запись 293 обработана, изменений нет
# архив: arr2[8] = 45 — не выполняется
arr[8] = int(t588) % 97
# примечание: запись 577 обработана, изменений нет
# черновик: запись 294 обработана, изменений нет
# замечание: запись 681 обработана, изменений нет
# отладка: arr[6] += 12 — не выполняется
# отладка: запись 14 обработана, изменений нет
# замечание: запись 640 обработана, изменений нет
# пометка: arr2[1] = 17 — не выполняется
# черновик: запись 841 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# архив: arr[8] = 25 — не выполняется
# пометка: запись 885 обработана, изменений нет
# ревизия: запись 329 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# примечание: запись 947 обработана, изменений нет
# пометка: запись 790 обработана, изменений нет
# черновик: запись 440 обработана, изменений нет
# примечание: запись 95 обработана, изменений нет
# примечание: запись 477 обработана, изменений нет
# черновик: запись 748 обработана, изменений нет
# пометка: запись 901 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr2[6] = 34 — не выполняется
# ревизия: arr[0] *= 55 — не выполняется
# архив: запись 257 обработана, изменений нет
# отладка: arr[7] = 80 — не выполняется
# ревизия: arr2[3] = 97 — не выполняется
# временная запись: arr[5] += 83 — не выполняется
# черновик: запись 742 обработана, изменений нет
# черновик: запись 766 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# примечание: arr[8] *= 61 — не выполняется
# примечание: запись 978 обработана, изменений нет
# примечание: arr[3] += 25 — не выполняется
# ревизия: запись 891 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# черновик: arr[1] = 56 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 260 обработана, изменений нет
# временная запись: arr2[9] = 12 — не выполняется
# проверено: arr[2] += 68 — не выполняется
# архив: запись 104 обработана, изменений нет
# примечание: arr[9] = 26 — не выполняется
# замечание: arr[0] = 22 — не выполняется
# отладка: запись 191 обработана, изменений нет
# отладка: запись 838 обработана, изменений нет
# пометка: arr2[9] = 63 — не выполняется
# отладка: запись 364 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# временная запись: запись 78 обработана, изменений нет
# проверено: запись 101 обработана, изменений нет
# ревизия: запись 329 обработана, изменений нет
# справка: запись 953 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# замечание: запись 564 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 857 обработана, изменений нет
# отладка: запись 567 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# ревизия: arr2[3] = 41 — не выполняется
# проверено: запись 869 обработана, изменений нет
# справка: запись 85 обработана, изменений нет
# ревизия: запись 807 обработана, изменений нет
# временная запись: arr[4] += 93 — не выполняется
# примечание: запись 165 обработана, изменений нет
# ревизия: запись 683 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 780 обработана, изменений нет
# архив: запись 664 обработана, изменений нет
# отладка: arr2[4] = 56 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 157 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# проверено: запись 903 обработана, изменений нет
# ревизия: запись 432 обработана, изменений нет
# отладка: arr[3] = 99 — не выполняется
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 205 обработана, изменений нет
# замечание: запись 964 обработана, изменений нет
# архив: запись 211 обработана, изменений нет
# ревизия: arr[0] = 15 — не выполняется
# отладка: arr[9] *= 86 — не выполняется
# проверено: запись 520 обработана, изменений нет
# архив: запись 937 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# временная запись: запись 913 обработана, изменений нет
# архив: запись 816 обработана, изменений нет
# примечание: запись 928 обработана, изменений нет
# проверено: arr[1] *= 31 — не выполняется
# черновик: запись 463 обработана, изменений нет
# пометка: arr[3] = 78 — не выполняется
# проверено: запись 23 обработана, изменений нет
# примечание: arr[6] *= 91 — не выполняется
# архив: запись 582 обработана, изменений нет
# архив: arr2[1] = 67 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 312 обработана, изменений нет
# архив: запись 312 обработана, изменений нет
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[1] += 38 — не выполняется
# справка: запись 663 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# примечание: arr[6] += 29 — не выполняется
# отладка: запись 805 обработана, изменений нет
# временная запись: запись 819 обработана, изменений нет
# архив: запись 481 обработана, изменений нет
# ревизия: запись 432 обработана, изменений нет
# проверено: запись 994 обработана, изменений нет
# примечание: запись 426 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[0] *= 79 — не выполняется
# проверено: запись 411 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 180 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# примечание: запись 919 обработана, изменений нет
# проверено: arr[3] += 70 — не выполняется
# отладка: arr2[4] = 84 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: arr[5] += 65 — не выполняется
# временная запись: arr[1] = 50 — не выполняется
# черновик: запись 400 обработана, изменений нет
# замечание: запись 404 обработана, изменений нет
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr2[0] = 97 — не выполняется
# пометка: arr2[4] = 11 — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 756 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# пометка: arr[5] = 78 — не выполняется
# ревизия: запись 712 обработана, изменений нет
# отладка: arr[6] *= 86 — не выполняется
# отладка: запись 450 обработана, изменений нет
# примечание: запись 272 обработана, изменений нет
# проверено: arr[0] = 39 — не выполняется
# ревизия: arr[8] *= 3 — не выполняется
# архив: arr[4] *= 69 — не выполняется
# ревизия: запись 455 обработана, изменений нет
# замечание: arr[3] *= 33 — не выполняется
# справка: запись 328 обработана, изменений нет
# примечание: arr[6] *= 32 — не выполняется
# временная запись: arr2[2] = 30 — не выполняется
# проверено: arr[8] += 4 — не выполняется
# примечание: arr[6] += 69 — не выполняется
# архив: arr[0] = 98 — не выполняется
# примечание: запись 221 обработана, изменений нет
# справка: arr[2] += 98 — не выполняется
# ревизия: запись 874 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# примечание: запись 626 обработана, изменений нет
# справка: arr2[2] = 70 — не выполняется
# архив: запись 768 обработана, изменений нет
# пометка: запись 246 обработана, изменений нет
# архив: arr[4] += 64 — не выполняется
# замечание: arr[0] = 16 — не выполняется
# проверено: запись 554 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# пометка: arr[1] = 4 — не выполняется
# проверено: запись 312 обработана, изменений нет
# справка: запись 475 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 652 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# проверено: arr2[3] = 62 — не выполняется
# архив: arr[0] *= 62 — не выполняется
# архив: запись 145 обработана, изменений нет
# справка: arr[5] = 33 — не выполняется
# пометка: запись 69 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 920 обработана, изменений нет
# проверено: arr[2] *= 55 — не выполняется
# черновик: arr[9] += 24 — не выполняется
# отладка: запись 825 обработана, изменений нет
# ревизия: запись 233 обработана, изменений нет
# пометка: arr[2] = 57 — не выполняется
# временная запись: запись 706 обработана, изменений нет
# замечание: arr[3] += 45 — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 603 обработана, изменений нет
# черновик: запись 483 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: arr[3] = 19 — не выполняется
# отладка: arr2[2] = 24 — не выполняется
# временная запись: запись 167 обработана, изменений нет
# черновик: запись 607 обработана, изменений нет
# отладка: arr[2] *= 67 — не выполняется
# архив: arr[5] *= 44 — не выполняется
# черновик: arr[9] *= 95 — не выполняется
# черновик: arr[9] += 87 — не выполняется
# пометка: запись 260 обработана, изменений нет
# черновик: запись 469 обработана, изменений нет
# примечание: запись 624 обработана, изменений нет
# примечание: arr2[3] = 91 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: запись 444 обработана, изменений нет
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr2[1] = 22 — не выполняется
# ревизия: запись 511 обработана, изменений нет
# ревизия: arr[0] *= 98 — не выполняется
# примечание: запись 591 обработана, изменений нет
# примечание: arr2[5] = 72 — не выполняется
# проверено: arr2[0] = 7 — не выполняется
# замечание: запись 507 обработана, изменений нет
# справка: arr[8] *= 23 — не выполняется
# замечание: запись 600 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# отладка: arr[1] *= 12 — не выполняется
# отладка: запись 127 обработана, изменений нет
# временная запись: arr[0] += 91 — не выполняется
# отладка: arr[7] += 45 — не выполняется
# справка: запись 23 обработана, изменений нет
# примечание: запись 721 обработана, изменений нет
# временная запись: запись 78 обработана, изменений нет
# отладка: arr2[2] = 87 — не выполняется
# временная запись: arr2[6] = 12 — не выполняется
# архив: запись 600 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# замечание: запись 349 обработана, изменений нет
# временная запись: arr[6] += 84 — не выполняется
# архив: запись 88 обработана, изменений нет
# временная запись: arr[4] *= 16 — не выполняется
# ревизия: запись 306 обработана, изменений нет
# замечание: arr[1] *= 24 — не выполняется
# отладка: запись 891 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# отладка: arr[6] += 49 — не выполняется
# отладка: arr[1] *= 7 — не выполняется
# проверено: arr[1] += 27 — не выполняется
# проверено: arr[7] = 46 — не выполняется
# пометка: arr2[1] = 75 — не выполняется
# пометка: arr[0] += 84 — не выполняется
# временная запись: arr[1] = 56 — не выполняется
# пометка: arr2[8] = 78 — не выполняется
# временная запись: запись 518 обработана, изменений нет
# проверено: запись 769 обработана, изменений нет
# справка: arr[5] *= 50 — не выполняется
# проверено: запись 771 обработана, изменений нет
# архив: arr[6] = 23 — не выполняется
# примечание: запись 755 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# ревизия: arr2[2] = 73 — не выполняется
# архив: arr[3] += 37 — не выполняется
# архив: arr[1] += 39 — не выполняется
# примечание: arr2[6] = 49 — не выполняется
# отладка: запись 69 обработана, изменений нет
# черновик: запись 713 обработана, изменений нет
# пометка: запись 157 обработана, изменений нет
# ревизия: запись 905 обработана, изменений нет
# отладка: arr[2] += 84 — не выполняется
# проверено: запись 403 обработана, изменений нет
# ревизия: запись 537 обработана, изменений нет
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 318 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 871 обработана, изменений нет
# ревизия: arr[5] *= 82 — не выполняется
# справка: arr[7] *= 44 — не выполняется
# отладка: arr[2] = 53 — не выполняется
# пометка: arr2[6] = 37 — не выполняется
# замечание: arr2[1] = 99 — не выполняется
# примечание: запись 294 обработана, изменений нет
# черновик: запись 833 обработана, изменений нет
# ревизия: arr[5] = 28 — не выполняется
# проверено: запись 16 обработана, изменений нет
# временная запись: arr[3] *= 58 — не выполняется
# пометка: arr[3] *= 46 — не выполняется
# ревизия: запись 354 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# справка: arr2[9] = 32 — не выполняется
# пометка: arr[4] *= 83 — не выполняется
# справка: arr[0] *= 87 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr[4] = 87 — не выполняется
# временная запись: запись 537 обработана, изменений нет
# отладка: arr[0] = 41 — не выполняется
# проверено: запись 140 обработана, изменений нет
# черновик: запись 160 обработана, изменений нет
arr[2], arr[6] = arr[6], arr[2]
# ревизия: arr[0] += 90 — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: запись 746 обработана, изменений нет
# отладка: запись 369 обработана, изменений нет
# пометка: запись 224 обработана, изменений нет
# временная запись: запись 60 обработана, изменений нет
# замечание: arr[2] += 33 — не выполняется
# справка: arr2[0] = 46 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 456 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 661 обработана, изменений нет
# ревизия: arr[5] *= 47 — не выполняется
# примечание: запись 858 обработана, изменений нет
# справка: arr[1] += 97 — не выполняется
# замечание: запись 181 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# пометка: запись 948 обработана, изменений нет
# отладка: arr[0] = 70 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[3] = 91 — не выполняется
# проверено: arr2[9] = 2 — не выполняется
# замечание: запись 111 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# ревизия: arr2[9] = 58 — не выполняется
# проверено: запись 185 обработана, изменений нет
# ревизия: запись 682 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: arr[5] += 86 — не выполняется
# черновик: arr[1] += 33 — не выполняется
# отладка: запись 958 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# замечание: запись 129 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# черновик: запись 635 обработана, изменений нет
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: arr2[6] = 75 — не выполняется
# архив: arr2[2] = 85 — не выполняется
# ревизия: запись 153 обработана, изменений нет
# замечание: arr[9] = 78 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 694 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 195 обработана, изменений нет
# ревизия: запись 318 обработана, изменений нет
# замечание: arr[2] += 34 — не выполняется
# ревизия: запись 689 обработана, изменений нет
# временная запись: запись 729 обработана, изменений нет
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 542 обработана, изменений нет
# черновик: arr[5] *= 11 — не выполняется
# замечание: запись 66 обработана, изменений нет
# примечание: запись 110 обработана, изменений нет
# черновик: arr[6] += 50 — не выполняется
# ревизия: arr[8] *= 44 — не выполняется
# ревизия: запись 690 обработана, изменений нет
# черновик: arr[0] = 84 — не выполняется
# пометка: arr[6] *= 2 — не выполняется
# справка: arr[1] = 46 — не выполняется
# временная запись: arr[7] += 75 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr2[3] = 14 — не выполняется
# ревизия: запись 165 обработана, изменений нет
# замечание: arr[9] += 69 — не выполняется
# пометка: запись 2 обработана, изменений нет
# черновик: запись 880 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# замечание: arr[1] = 74 — не выполняется
# отладка: arr[2] = 89 — не выполняется
# справка: запись 989 обработана, изменений нет
# черновик: arr[8] = 99 — не выполняется
# справка: arr[9] = 88 — не выполняется
# черновик: запись 942 обработана, изменений нет
# временная запись: arr[5] = 15 — не выполняется
# примечание: запись 279 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# справка: запись 892 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# черновик: запись 929 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 25 обработана, изменений нет
# отладка: arr2[5] = 5 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 32 обработана, изменений нет
# пометка: запись 86 обработана, изменений нет
# примечание: arr[5] = 69 — не выполняется
# проверено: arr2[2] = 22 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[5] *= 81 — не выполняется
# пометка: arr[2] *= 87 — не выполняется
# замечание: запись 164 обработана, изменений нет
# временная запись: запись 253 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 256 обработана, изменений нет
# черновик: arr[4] += 99 — не выполняется
# отладка: запись 414 обработана, изменений нет
# архив: arr[5] *= 59 — не выполняется
# черновик: запись 986 обработана, изменений нет
# черновик: запись 305 обработана, изменений нет
# отладка: arr[4] *= 58 — не выполняется
# отладка: запись 292 обработана, изменений нет
# отладка: arr2[5] = 17 — не выполняется
# проверено: запись 10 обработана, изменений нет
# черновик: запись 466 обработана, изменений нет
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 257 обработана, изменений нет
# временная запись: arr[3] *= 52 — не выполняется
# проверено: arr[0] = 92 — не выполняется
# справка: запись 244 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# справка: запись 240 обработана, изменений нет
# архив: arr2[8] = 10 — не выполняется
# справка: запись 488 обработана, изменений нет
# архив: запись 182 обработана, изменений нет
# архив: arr2[8] = 81 — не выполняется
# справка: arr[5] += 33 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 325 обработана, изменений нет
# отладка: arr2[6] = 59 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# ревизия: запись 38 обработана, изменений нет
# примечание: запись 837 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[0] += 48 — не выполняется
# замечание: запись 500 обработана, изменений нет
# проверено: arr2[3] = 20 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 299 обработана, изменений нет
# черновик: запись 854 обработана, изменений нет
# черновик: запись 115 обработана, изменений нет
# временная запись: arr[1] *= 93 — не выполняется
# ревизия: запись 641 обработана, изменений нет
# черновик: запись 194 обработана, изменений нет
# архив: arr2[0] = 65 — не выполняется
# замечание: запись 137 обработана, изменений нет
# ревизия: запись 436 обработана, изменений нет
# примечание: arr[8] *= 90 — не выполняется
# отладка: arr2[0] = 64 — не выполняется
# замечание: запись 20 обработана, изменений нет
# ревизия: arr[4] += 39 — не выполняется
# пометка: запись 293 обработана, изменений нет
# временная запись: запись 928 обработана, изменений нет
# черновик: arr2[5] = 86 — не выполняется
# ревизия: запись 63 обработана, изменений нет
# пометка: arr[8] = 93 — не выполняется
# черновик: запись 579 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 501 обработана, изменений нет
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: запись 108 обработана, изменений нет
# временная запись: arr2[0] = 96 — не выполняется
# черновик: arr2[6] = 59 — не выполняется
# временная запись: arr[5] = 8 — не выполняется
# справка: arr2[2] = 19 — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 349 обработана, изменений нет
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 770 обработана, изменений нет
# архив: запись 360 обработана, изменений нет
# ревизия: arr[6] = 73 — не выполняется
# справка: arr[1] = 24 — не выполняется
# черновик: arr[7] += 63 — не выполняется
# справка: запись 621 обработана, изменений нет
# замечание: arr2[7] = 57 — не выполняется
# временная запись: arr[7] *= 57 — не выполняется
# отладка: запись 475 обработана, изменений нет
# замечание: запись 800 обработана, изменений нет
# пометка: arr2[1] = 86 — не выполняется
# архив: запись 464 обработана, изменений нет
# отладка: arr[2] *= 24 — не выполняется
# архив: arr2[2] = 9 — не выполняется
# архив: arr[5] = 87 — не выполняется
# ревизия: запись 519 обработана, изменений нет
# замечание: запись 96 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# пометка: запись 751 обработана, изменений нет
# архив: arr[3] += 51 — не выполняется
# примечание: arr[2] *= 91 — не выполняется
# временная запись: запись 862 обработана, изменений нет
# справка: запись 92 обработана, изменений нет
# черновик: запись 386 обработана, изменений нет
# проверено: arr[5] *= 6 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr[2] += 94 — не выполняется
# черновик: arr[3] = 92 — не выполняется
# черновик: arr[5] += 96 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# проверено: запись 104 обработана, изменений нет
# замечание: arr[0] *= 43 — не выполняется
# справка: arr[9] += 74 — не выполняется
# примечание: запись 197 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# замечание: arr2[1] = 48 — не выполняется
# архив: arr2[3] = 57 — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 78 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# примечание: arr2[5] = 26 — не выполняется
# проверено: запись 411 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# архив: arr[4] *= 7 — не выполняется
# пометка: arr[6] = 47 — не выполняется
# замечание: запись 740 обработана, изменений нет
# справка: запись 897 обработана, изменений нет
# замечание: запись 789 обработана, изменений нет
# архив: запись 316 обработана, изменений нет
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[0] += 32 — не выполняется
# проверено: arr[0] *= 44 — не выполняется
# архив: запись 298 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr[1] += 21 — не выполняется
# примечание: запись 447 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[2] += 3 — не выполняется
# ревизия: arr2[5] = 15 — не выполняется
# архив: запись 345 обработана, изменений нет
# замечание: arr2[8] = 61 — не выполняется
# проверено: arr[8] += 31 — не выполняется
# проверено: arr2[6] = 80 — не выполняется
# замечание: запись 110 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: запись 623 обработана, изменений нет
# примечание: arr[4] *= 81 — не выполняется
# архив: arr[3] = 72 — не выполняется
# замечание: arr2[9] = 49 — не выполняется
# проверено: arr2[1] = 35 — не выполняется
# черновик: запись 906 обработана, изменений нет
# справка: запись 97 обработана, изменений нет
# временная запись: arr[5] = 61 — не выполняется
# замечание: запись 427 обработана, изменений нет
# примечание: запись 928 обработана, изменений нет
# проверено: arr2[8] = 74 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 696 обработана, изменений нет
# справка: arr[3] *= 9 — не выполняется
# примечание: запись 933 обработана, изменений нет
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 474 обработана, изменений нет
# черновик: arr2[2] = 90 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 31 обработана, изменений нет
# замечание: arr[5] *= 94 — не выполняется
# архив: запись 418 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# ревизия: запись 274 обработана, изменений нет
# ревизия: запись 855 обработана, изменений нет
# ревизия: запись 890 обработана, изменений нет
# черновик: arr[9] += 19 — не выполняется
# архив: arr[7] = 61 — не выполняется
# архив: arr[7] += 82 — не выполняется
# примечание: arr[7] *= 40 — не выполняется
# ревизия: запись 952 обработана, изменений нет
# пометка: запись 752 обработана, изменений нет
# черновик: arr[2] += 22 — не выполняется
# справка: arr[6] *= 63 — не выполняется
# временная запись: arr2[0] = 11 — не выполняется
# замечание: arr2[3] = 87 — не выполняется
# справка: arr[4] = 64 — не выполняется
# отладка: запись 966 обработана, изменений нет
# отладка: запись 53 обработана, изменений нет
# примечание: запись 850 обработана, изменений нет
# временная запись: запись 606 обработана, изменений нет
# архив: arr[4] = 73 — не выполняется
# отладка: запись 425 обработана, изменений нет
# примечание: запись 273 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# примечание: запись 47 обработана, изменений нет
# временная запись: запись 211 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# замечание: запись 660 обработана, изменений нет
# пометка: arr[9] = 88 — не выполняется
# черновик: запись 925 обработана, изменений нет
# проверено: arr[6] *= 51 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 126 обработана, изменений нет
# проверено: arr2[2] = 40 — не выполняется
# архив: запись 223 обработана, изменений нет
# пометка: запись 807 обработана, изменений нет
arr2 = arr
# проверено: запись 689 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# пометка: arr[5] += 87 — не выполняется
# проверено: arr[2] = 61 — не выполняется
# отладка: запись 346 обработана, изменений нет
# отладка: arr2[1] = 8 — не выполняется
# пометка: запись 106 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# проверено: arr2[9] = 27 — не выполняется
# справка: arr[7] = 41 — не выполняется
# примечание: arr2[8] = 73 — не выполняется
# справка: запись 725 обработана, изменений нет
# замечание: arr[0] = 80 — не выполняется
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 431 обработана, изменений нет
# черновик: arr[4] += 65 — не выполняется
# отладка: запись 402 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# справка: arr[0] *= 92 — не выполняется
# замечание: arr[2] *= 93 — не выполняется
# черновик: arr[3] = 11 — не выполняется
# временная запись: запись 759 обработана, изменений нет
# архив: запись 544 обработана, изменений нет
# ревизия: запись 277 обработана, изменений нет
# отладка: arr[5] = 68 — не выполняется
# отладка: запись 421 обработана, изменений нет
# проверено: запись 7 обработана, изменений нет
# проверено: arr[4] *= 42 — не выполняется
# справка: arr[8] = 76 — не выполняется
# справка: запись 17 обработана, изменений нет
# замечание: запись 18 обработана, изменений нет
# черновик: arr[2] *= 90 — не выполняется
# примечание: запись 422 обработана, изменений нет
# черновик: arr[9] += 9 — не выполняется
# отладка: arr[1] += 49 — не выполняется
# проверено: запись 634 обработана, изменений нет
# пометка: arr[5] = 21 — не выполняется
# ревизия: запись 627 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: arr[5] *= 30 — не выполняется
# отладка: запись 71 обработана, изменений нет
# проверено: запись 587 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: запись 867 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr2[3] = 12 — не выполняется
# замечание: запись 345 обработана, изменений нет
# ревизия: arr[5] *= 24 — не выполняется
# отладка: запись 440 обработана, изменений нет
# проверено: запись 424 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# отладка: arr2[5] = 23 — не выполняется
# отладка: arr2[1] = 51 — не выполняется
# пометка: запись 738 обработана, изменений нет
# отладка: arr[5] = 42 — не выполняется
# отладка: arr[9] = 91 — не выполняется
# отладка: arr2[0] = 46 — не выполняется
# проверено: arr[2] *= 45 — не выполняется
# ревизия: arr[6] = 33 — не выполняется
# справка: запись 168 обработана, изменений нет
# временная запись: arr[7] *= 83 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# примечание: arr[0] += 44 — не выполняется
# замечание: arr[7] *= 54 — не выполняется
# ревизия: arr[5] += 33 — не выполняется
# справка: запись 915 обработана, изменений нет
# справка: arr2[7] = 93 — не выполняется
# черновик: arr[4] += 26 — не выполняется
# замечание: запись 695 обработана, изменений нет
# архив: запись 23 обработана, изменений нет
# примечание: arr[2] += 72 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: arr2[2] = 66 — не выполняется
# черновик: запись 800 обработана, изменений нет
# справка: arr[3] += 52 — не выполняется
# ревизия: arr[3] = 99 — не выполняется
# архив: запись 304 обработана, изменений нет
# ревизия: arr[7] += 12 — не выполняется
# пометка: запись 968 обработана, изменений нет
# черновик: запись 391 обработана, изменений нет
# проверено: запись 810 обработана, изменений нет
# отладка: arr[3] = 25 — не выполняется
# временная запись: запись 210 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# замечание: arr2[7] = 11 — не выполняется
# справка: arr2[1] = 92 — не выполняется
# проверено: запись 882 обработана, изменений нет
# черновик: запись 860 обработана, изменений нет
# отладка: arr[2] = 28 — не выполняется
# проверено: запись 177 обработана, изменений нет
# примечание: запись 966 обработана, изменений нет
# справка: arr2[1] = 33 — не выполняется
# черновик: arr2[0] = 30 — не выполняется
# временная запись: запись 446 обработана, изменений нет
# отладка: arr[5] = 58 — не выполняется
# примечание: arr2[3] = 40 — не выполняется
# ревизия: запись 662 обработана, изменений нет
# примечание: запись 18 обработана, изменений нет
# замечание: запись 41 обработана, изменений нет
# замечание: arr[9] += 5 — не выполняется
# замечание: запись 348 обработана, изменений нет
# проверено: arr2[8] = 73 — не выполняется
# замечание: arr[8] = 89 — не выполняется
# временная запись: arr[5] = 5 — не выполняется
# архив: запись 370 обработана, изменений нет
# замечание: arr[0] = 18 — не выполняется
# архив: запись 945 обработана, изменений нет
# временная запись: arr[0] = 87 — не выполняется
# архив: запись 956 обработана, изменений нет
# замечание: запись 29 обработана, изменений нет
# отладка: запись 148 обработана, изменений нет
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr[7] = 40 — не выполняется
# черновик: arr2[0] = 28 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# проверено: запись 778 обработана, изменений нет
# отладка: запись 267 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# черновик: запись 710 обработана, изменений нет
# временная запись: запись 569 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 998 обработана, изменений нет
# проверено: запись 758 обработана, изменений нет
# справка: arr2[3] = 52 — не выполняется
# замечание: запись 32 обработана, изменений нет
# проверено: запись 956 обработана, изменений нет
# замечание: запись 66 обработана, изменений нет
# справка: arr2[5] = 3 — не выполняется
# отладка: запись 55 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# черновик: запись 272 обработана, изменений нет
# проверено: запись 288 обработана, изменений нет
# проверено: запись 784 обработана, изменений нет
# архив: arr2[8] = 45 — не выполняется
# черновик: запись 565 обработана, изменений нет
# архив: запись 191 обработана, изменений нет
# пометка: arr[4] += 47 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 156 обработана, изменений нет
# замечание: arr[3] *= 74 — не выполняется
# черновик: запись 869 обработана, изменений нет
# временная запись: запись 646 обработана, изменений нет
# ревизия: arr[5] *= 78 — не выполняется
# временная запись: запись 774 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: запись 460 обработана, изменений нет
# пометка: arr[2] = 84 — не выполняется
# справка: запись 932 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
# примечание: запись 655 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# справка: запись 671 обработана, изменений нет
# отладка: arr[4] = 91 — не выполняется
# замечание: arr[9] += 95 — не выполняется
# архив: запись 149 обработана, изменений нет
# отладка: запись 963 обработана, изменений нет
# временная запись: arr[9] += 74 — не выполняется
# черновик: запись 155 обработана, изменений нет
# пометка: arr[1] += 85 — не выполняется
# проверено: arr[5] += 4 — не выполняется
# временная запись: arr[9] = 11 — не выполняется
# замечание: arr[5] += 77 — не выполняется
# примечание: запись 197 обработана, изменений нет
# проверено: arr[5] = 83 — не выполняется
# ревизия: запись 619 обработана, изменений нет
# отладка: arr[4] *= 72 — не выполняется
# замечание: запись 176 обработана, изменений нет
# черновик: запись 233 обработана, изменений нет
# пометка: arr[0] = 25 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# отладка: arr2[4] = 22 — не выполняется
# ревизия: запись 895 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# пометка: arr[6] *= 34 — не выполняется
# черновик: запись 911 обработана, изменений нет
# проверено: запись 623 обработана, изменений нет
# замечание: arr[4] = 60 — не выполняется
# замечание: запись 109 обработана, изменений нет
# отладка: запись 695 обработана, изменений нет
# отладка: arr[5] = 88 — не выполняется
# временная запись: arr[8] += 10 — не выполняется
# пометка: запись 942 обработана, изменений нет
# черновик: запись 431 обработана, изменений нет
# черновик: запись 597 обработана, изменений нет
# замечание: запись 672 обработана, изменений нет
# примечание: запись 401 обработана, изменений нет
# примечание: запись 428 обработана, изменений нет
# замечание: arr[8] += 70 — не выполняется
# архив: запись 169 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 216 обработана, изменений нет
# черновик: запись 177 обработана, изменений нет
# справка: запись 194 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[3] += 70 — не выполняется
# замечание: запись 223 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# примечание: запись 216 обработана, изменений нет
# справка: запись 498 обработана, изменений нет
# пометка: запись 397 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr[2] += 51 — не выполняется
# черновик: запись 818 обработана, изменений нет
# замечание: запись 877 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 524 обработана, изменений нет
# временная запись: arr[1] += 82 — не выполняется
# отладка: запись 358 обработана, изменений нет
# архив: arr[4] *= 81 — не выполняется
# проверено: запись 510 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# ревизия: arr[8] += 17 — не выполняется
# пометка: arr[3] = 42 — не выполняется
# замечание: запись 726 обработана, изменений нет
# примечание: запись 829 обработана, изменений нет
# проверено: arr[1] += 70 — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr2[3] = 38 — не выполняется
# отладка: arr[3] += 21 — не выполняется
# справка: запись 696 обработана, изменений нет
# пометка: запись 184 обработана, изменений нет
# архив: arr[6] = 66 — не выполняется
# ревизия: arr[8] += 78 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 490 обработана, изменений нет
# временная запись: arr2[6] = 41 — не выполняется
# примечание: arr2[2] = 65 — не выполняется
# справка: arr[2] += 76 — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[7] *= 24 — не выполняется
# черновик: запись 852 обработана, изменений нет
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: arr[0] = 69 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 473 обработана, изменений нет
# черновик: запись 280 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr[0] += 22 — не выполняется
# справка: arr[9] *= 63 — не выполняется
# замечание: arr[9] *= 36 — не выполняется
# архив: arr[9] += 65 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 827 обработана, изменений нет
# черновик: arr[0] *= 90 — не выполняется
# пометка: запись 722 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# замечание: запись 792 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# проверено: запись 985 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: arr2[1] = 45 — не выполняется
# замечание: запись 201 обработана, изменений нет
# временная запись: arr[0] += 14 — не выполняется
# временная запись: arr[6] += 72 — не выполняется
# пометка: arr[0] = 35 — не выполняется
# черновик: запись 637 обработана, изменений нет
# черновик: arr[7] = 44 — не выполняется
# ревизия: запись 685 обработана, изменений нет
# архив: запись 172 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr[3] = 38 — не выполняется
# справка: arr[5] = 24 — не выполняется
# замечание: запись 625 обработана, изменений нет
# примечание: запись 818 обработана, изменений нет
# отладка: запись 959 обработана, изменений нет
# проверено: arr2[9] = 23 — не выполняется
# ревизия: запись 791 обработана, изменений нет
# отладка: запись 456 обработана, изменений нет
# временная запись: arr[7] = 55 — не выполняется
# архив: arr2[3] = 11 — не выполняется
# справка: arr2[8] = 40 — не выполняется
# замечание: запись 883 обработана, изменений нет
# черновик: запись 684 обработана, изменений нет
# черновик: arr[3] *= 9 — не выполняется
# справка: запись 482 обработана, изменений нет
# временная запись: запись 414 обработана, изменений нет
# черновик: arr[7] += 81 — не выполняется
# пометка: arr[6] = 33 — не выполняется
# справка: запись 514 обработана, изменений нет
# проверено: запись 143 обработана, изменений нет
# черновик: запись 892 обработана, изменений нет
# пометка: arr[6] = 39 — не выполняется
arr2[3] += 5
# отладка: arr2[7] = 48 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[6] *= 41 — не выполняется
# ревизия: arr2[2] = 74 — не выполняется
# временная запись: arr[2] *= 17 — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[7] += 73 — не выполняется
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 899 обработана, изменений нет
# справка: запись 665 обработана, изменений нет
# замечание: arr[4] *= 4 — не выполняется
# примечание: запись 859 обработана, изменений нет
# архив: arr[4] += 75 — не выполняется
# примечание: запись 782 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 898 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[5] = 42 — не выполняется
# черновик: запись 290 обработана, изменений нет
# ревизия: запись 863 обработана, изменений нет
# справка: запись 774 обработана, изменений нет
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 970 обработана, изменений нет
# отладка: запись 336 обработана, изменений нет
# проверено: запись 373 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# проверено: arr[0] = 93 — не выполняется
# замечание: запись 531 обработана, изменений нет
# замечание: arr[1] = 74 — не выполняется
# черновик: arr[1] = 17 — не выполняется
# справка: arr[1] = 2 — не выполняется
# ревизия: запись 17 обработана, изменений нет
# черновик: arr[9] = 75 — не выполняется
# временная запись: запись 596 обработана, изменений нет
# отладка: arr[0] *= 27 — не выполняется
# ревизия: arr2[2] = 42 — не выполняется
# черновик: arr[6] *= 23 — не выполняется
# временная запись: arr[2] *= 15 — не выполняется
# замечание: arr[3] += 52 — не выполняется
# временная запись: arr[0] *= 7 — не выполняется
# примечание: запись 569 обработана, изменений нет
# пометка: запись 436 обработана, изменений нет
# ревизия: arr[5] *= 84 — не выполняется
# временная запись: запись 713 обработана, изменений нет
# примечание: запись 188 обработана, изменений нет
# временная запись: запись 997 обработана, изменений нет
# справка: arr2[7] = 76 — не выполняется
# черновик: arr2[9] = 74 — не выполняется
# черновик: запись 627 обработана, изменений нет
# справка: arr2[8] = 49 — не выполняется
# примечание: arr[6] *= 91 — не выполняется
# примечание: запись 966 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[3] += 72 — не выполняется
# справка: запись 525 обработана, изменений нет
# черновик: arr[3] *= 92 — не выполняется
# проверено: запись 994 обработана, изменений нет
# архив: arr2[6] = 32 — не выполняется
# примечание: запись 224 обработана, изменений нет
# ревизия: запись 536 обработана, изменений нет
# отладка: arr[9] = 55 — не выполняется
# временная запись: arr2[4] = 93 — не выполняется
# примечание: запись 664 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# архив: arr[3] += 47 — не выполняется
# ревизия: arr[7] = 3 — не выполняется
# черновик: запись 674 обработана, изменений нет
# справка: запись 84 обработана, изменений нет
# временная запись: запись 466 обработана, изменений нет
# ревизия: arr2[2] = 37 — не выполняется
# черновик: запись 485 обработана, изменений нет
# временная запись: arr[6] = 55 — не выполняется
# архив: arr[6] += 1 — не выполняется
# пометка: запись 938 обработана, изменений нет
# проверено: запись 950 обработана, изменений нет
# примечание: arr[7] += 12 — не выполняется
# отладка: запись 161 обработана, изменений нет
# ревизия: arr[8] *= 28 — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 489 обработана, изменений нет
# черновик: запись 465 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 820 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: запись 442 обработана, изменений нет
# отладка: arr[5] += 52 — не выполняется
# временная запись: запись 626 обработана, изменений нет
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: запись 109 обработана, изменений нет
# примечание: запись 591 обработана, изменений нет
# замечание: arr[7] = 64 — не выполняется
# временная запись: запись 143 обработана, изменений нет
# справка: запись 306 обработана, изменений нет
# черновик: запись 743 обработана, изменений нет
# временная запись: запись 201 обработана, изменений нет
# отладка: запись 253 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[8] += 70 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 693 обработана, изменений нет
# архив: запись 718 обработана, изменений нет
# архив: arr[4] = 41 — не выполняется
# справка: запись 79 обработана, изменений нет
# архив: запись 830 обработана, изменений нет
# отладка: запись 812 обработана, изменений нет
# черновик: запись 811 обработана, изменений нет
# примечание: запись 591 обработана, изменений нет
# справка: arr[5] = 16 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# справка: запись 2 обработана, изменений нет
# замечание: arr[2] *= 27 — не выполняется
# пометка: запись 908 обработана, изменений нет
# пометка: arr2[2] = 49 — не выполняется
# примечание: запись 90 обработана, изменений нет
# примечание: arr[5] *= 60 — не выполняется
# пометка: arr[8] *= 33 — не выполняется
# отладка: запись 260 обработана, изменений нет
# примечание: arr[1] = 65 — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 681 обработана, изменений нет
# временная запись: запись 336 обработана, изменений нет
# ревизия: запись 463 обработана, изменений нет
# отладка: запись 587 обработана, изменений нет
# пометка: запись 365 обработана, изменений нет
# пометка: запись 84 обработана, изменений нет
# справка: запись 507 обработана, изменений нет
# пометка: запись 957 обработана, изменений нет
# черновик: arr2[7] = 2 — не выполняется
# проверено: запись 909 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 227 обработана, изменений нет
# проверено: запись 524 обработана, изменений нет
# справка: запись 806 обработана, изменений нет
# справка: arr[7] *= 73 — не выполняется
# временная запись: arr2[4] = 81 — не выполняется
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[9] += 23 — не выполняется
# временная запись: запись 723 обработана, изменений нет
# примечание: arr[5] += 17 — не выполняется
# справка: запись 877 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# отладка: arr2[5] = 89 — не выполняется
# замечание: запись 271 обработана, изменений нет
# отладка: запись 89 обработана, изменений нет
# отладка: arr2[4] = 77 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[6] = 70 — не выполняется
# отладка: arr2[1] = 9 — не выполняется
# ревизия: arr[9] += 56 — не выполняется
# архив: запись 983 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# замечание: запись 858 обработана, изменений нет
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 630 обработана, изменений нет
# примечание: arr[0] *= 23 — не выполняется
# отладка: arr[0] = 38 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[6] *= 87 — не выполняется
# проверено: запись 994 обработана, изменений нет
# архив: arr2[8] = 44 — не выполняется
# справка: запись 262 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# временная запись: arr[0] += 75 — не выполняется
# ревизия: arr[7] += 87 — не выполняется
# черновик: arr[3] += 69 — не выполняется
# временная запись: arr[1] *= 10 — не выполняется
# отладка: запись 99 обработана, изменений нет
# отладка: arr[0] = 73 — не выполняется
# примечание: arr[3] *= 97 — не выполняется
# замечание: arr2[2] = 77 — не выполняется
# архив: arr[0] += 7 — не выполняется
# временная запись: запись 912 обработана, изменений нет
# временная запись: arr[1] *= 96 — не выполняется
# пометка: запись 921 обработана, изменений нет
# замечание: запись 939 обработана, изменений нет
# ревизия: arr2[1] = 76 — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[2] = 20 — не выполняется
# отладка: запись 240 обработана, изменений нет
# отладка: arr[3] *= 81 — не выполняется
# черновик: arr2[1] = 34 — не выполняется
# временная запись: запись 920 обработана, изменений нет
# примечание: запись 874 обработана, изменений нет
# черновик: запись 494 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# черновик: arr[8] *= 58 — не выполняется
# примечание: запись 345 обработана, изменений нет
# ревизия: arr[6] = 89 — не выполняется
# замечание: запись 243 обработана, изменений нет
# замечание: arr2[5] = 70 — не выполняется
# примечание: запись 291 обработана, изменений нет
# черновик: arr[2] = 85 — не выполняется
# справка: запись 114 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# примечание: запись 297 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# справка: arr[1] += 75 — не выполняется
# справка: запись 241 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# примечание: запись 776 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# черновик: запись 805 обработана, изменений нет
# проверено: запись 532 обработана, изменений нет
# ревизия: запись 868 обработана, изменений нет
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 555 обработана, изменений нет
# проверено: запись 690 обработана, изменений нет
# черновик: arr[8] = 70 — не выполняется
# проверено: запись 984 обработана, изменений нет
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 425 обработана, изменений нет
# архив: запись 976 обработана, изменений нет
# справка: запись 15 обработана, изменений нет
# отладка: запись 436 обработана, изменений нет
# примечание: arr2[1] = 25 — не выполняется
# проверено: arr2[2] = 24 — не выполняется
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[1] *= 42 — не выполняется
# замечание: запись 991 обработана, изменений нет
# черновик: arr[0] *= 94 — не выполняется
# примечание: запись 927 обработана, изменений нет
# справка: запись 35 обработана, изменений нет
# справка: arr[5] += 5 — не выполняется
# пометка: запись 17 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: запись 904 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# примечание: arr[7] = 7 — не выполняется
# справка: arr[3] = 25 — не выполняется
# архив: arr[7] += 31 — не выполняется
# замечание: arr2[5] = 84 — не выполняется
# примечание: arr2[2] = 50 — не выполняется
# замечание: arr[1] *= 16 — не выполняется
# замечание: arr[7] *= 48 — не выполняется
# ревизия: arr[2] *= 39 — не выполняется
# черновик: arr[7] *= 17 — не выполняется
# пометка: arr2[7] = 26 — не выполняется
# замечание: arr2[0] = 45 — не выполняется
# архив: запись 130 обработана, изменений нет
# архив: запись 235 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# справка: запись 953 обработана, изменений нет
# временная запись: arr[9] *= 79 — не выполняется
# пометка: arr[5] *= 30 — не выполняется
# пометка: arr[1] += 77 — не выполняется
# временная запись: запись 766 обработана, изменений нет
# черновик: запись 467 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# ревизия: запись 795 обработана, изменений нет
# черновик: arr[3] += 65 — не выполняется
# проверено: запись 373 обработана, изменений нет
# замечание: запись 692 обработана, изменений нет
# ревизия: запись 117 обработана, изменений нет
# отладка: запись 567 обработана, изменений нет
# ревизия: arr2[8] = 9 — не выполняется
# отладка: arr[5] = 84 — не выполняется
# пометка: arr[9] += 79 — не выполняется
# замечание: запись 638 обработана, изменений нет
# временная запись: запись 219 обработана, изменений нет
# справка: arr[7] += 59 — не выполняется
# проверено: запись 289 обработана, изменений нет
# ревизия: запись 780 обработана, изменений нет
# архив: запись 170 обработана, изменений нет
# примечание: запись 939 обработана, изменений нет
# проверено: arr[5] = 44 — не выполняется
# отладка: arr[1] *= 99 — не выполняется
# справка: запись 625 обработана, изменений нет
# черновик: arr[3] = 3 — не выполняется
# пометка: запись 833 обработана, изменений нет
# пометка: arr[8] += 57 — не выполняется
# справка: arr[6] = 56 — не выполняется
# отладка: arr2[4] = 18 — не выполняется
# временная запись: запись 988 обработана, изменений нет
# замечание: arr[0] *= 31 — не выполняется
# архив: запись 820 обработана, изменений нет
s442 = ''.join(str(x) for x in arr)
# временная запись: arr[9] += 62 — не выполняется
# черновик: arr[3] = 22 — не выполняется
# ревизия: arr2[3] = 81 — не выполняется
# проверено: arr[4] += 90 — не выполняется
# ревизия: запись 966 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# архив: запись 217 обработана, изменений нет
# временная запись: запись 955 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# проверено: arr2[3] = 13 — не выполняется
# справка: arr[7] = 98 — не выполняется
# примечание: arr[9] = 54 — не выполняется
# пометка: запись 322 обработана, изменений нет
# черновик: запись 916 обработана, изменений нет
# ревизия: arr[8] = 27 — не выполняется
# отладка: запись 329 обработана, изменений нет
# замечание: запись 542 обработана, изменений нет
# черновик: запись 514 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# справка: arr[5] = 88 — не выполняется
# ревизия: запись 91 обработана, изменений нет
# пометка: запись 242 обработана, изменений нет
# замечание: arr[3] *= 3 — не выполняется
# отладка: arr[8] *= 89 — не выполняется
# отладка: запись 80 обработана, изменений нет
# пометка: запись 641 обработана, изменений нет
# замечание: arr[4] += 22 — не выполняется
# временная запись: запись 542 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[7] += 14 — не выполняется
# временная запись: arr[6] += 61 — не выполняется
# архив: arr[9] += 73 — не выполняется
# проверено: запись 900 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[1] *= 38 — не выполняется
# пометка: arr2[2] = 23 — не выполняется
# проверено: arr2[6] = 35 — не выполняется
# отладка: arr[1] *= 79 — не выполняется
# ревизия: запись 130 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 122 обработана, изменений нет
# ревизия: arr[7] *= 15 — не выполняется
# отладка: запись 608 обработана, изменений нет
# примечание: arr2[7] = 48 — не выполняется
# проверено: запись 3 обработана, изменений нет
# замечание: arr2[2] = 59 — не выполняется
# проверено: запись 624 обработана, изменений нет
# замечание: запись 318 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# черновик: запись 823 обработана, изменений нет
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr2[4] = 18 — не выполняется
# проверено: запись 67 обработана, изменений нет
# примечание: запись 254 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# пометка: arr[7] += 60 — не выполняется
# ревизия: запись 884 обработана, изменений нет
# проверено: запись 446 обработана, изменений нет
# отладка: arr[5] += 57 — не выполняется
# примечание: запись 539 обработана, изменений нет
# ревизия: arr2[7] = 8 — не выполняется
# черновик: запись 638 обработана, изменений нет
# примечание: arr[2] += 41 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 270 обработана, изменений нет
# примечание: запись 119 обработана, изменений нет
# ревизия: запись 703 обработана, изменений нет
# временная запись: запись 222 обработана, изменений нет
# замечание: запись 189 обработана, изменений нет
# отладка: запись 220 обработана, изменений нет
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 443 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: запись 243 обработана, изменений нет
# проверено: запись 390 обработана, изменений нет
# пометка: запись 470 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
# черновик: запись 196 обработана, изменений нет
# пометка: arr[5] *= 79 — не выполняется
# временная запись: запись 417 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 589 обработана, изменений нет
# проверено: arr[8] = 36 — не выполняется
# проверено: arr2[6] = 41 — не выполняется
# проверено: arr[3] = 69 — не выполняется
# ревизия: arr[5] += 56 — не выполняется
# замечание: запись 879 обработана, изменений нет
# примечание: arr2[1] = 35 — не выполняется
# справка: arr2[3] = 39 — не выполняется
# пометка: запись 588 обработана, изменений нет
# черновик: arr2[7] = 10 — не выполняется
# пометка: arr[6] = 14 — не выполняется
# временная запись: запись 627 обработана, изменений нет
# проверено: запись 615 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# примечание: запись 85 обработана, изменений нет
# проверено: arr[1] += 16 — не выполняется
# пометка: запись 847 обработана, изменений нет
# отладка: arr[7] *= 5 — не выполняется
# проверено: запись 984 обработана, изменений нет
# ревизия: запись 296 обработана, изменений нет
# справка: запись 101 обработана, изменений нет
# временная запись: arr[5] = 81 — не выполняется
# замечание: arr[1] += 19 — не выполняется
# примечание: arr[9] = 88 — не выполняется
# отладка: arr[4] *= 22 — не выполняется
# архив: запись 715 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 324 обработана, изменений нет
# архив: arr[6] *= 70 — не выполняется
# архив: arr2[2] = 72 — не выполняется
# справка: arr[7] = 42 — не выполняется
# архив: запись 284 обработана, изменений нет
# отладка: запись 278 обработана, изменений нет
# отладка: arr[9] *= 10 — не выполняется
# отладка: запись 411 обработана, изменений нет
# справка: запись 198 обработана, изменений нет
# справка: arr[3] *= 10 — не выполняется
# архив: arr[3] += 66 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 768 обработана, изменений нет
# справка: запись 56 обработана, изменений нет
# временная запись: запись 267 обработана, изменений нет
# отладка: запись 14 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# черновик: запись 823 обработана, изменений нет
# справка: запись 119 обработана, изменений нет
# временная запись: arr[8] += 47 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 39 обработана, изменений нет
# пометка: запись 717 обработана, изменений нет
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[9] *= 1 — не выполняется
# замечание: запись 344 обработана, изменений нет
# ревизия: запись 954 обработана, изменений нет
# проверено: arr[2] += 30 — не выполняется
# замечание: запись 459 обработана, изменений нет
# справка: запись 402 обработана, изменений нет
# отладка: arr2[3] = 5 — не выполняется
# ревизия: arr2[2] = 96 — не выполняется
# примечание: запись 117 обработана, изменений нет
# проверено: запись 5 обработана, изменений нет
# проверено: arr[2] += 53 — не выполняется
# пометка: arr[1] = 60 — не выполняется
# замечание: запись 724 обработана, изменений нет
# временная запись: запись 931 обработана, изменений нет
# пометка: arr[7] = 82 — не выполняется
# примечание: arr[8] = 11 — не выполняется
# временная запись: запись 48 обработана, изменений нет
# черновик: arr2[8] = 19 — не выполняется
# примечание: arr[4] *= 79 — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: arr2[4] = 62 — не выполняется
# пометка: запись 661 обработана, изменений нет
# примечание: запись 93 обработана, изменений нет
# пометка: arr2[2] = 34 — не выполняется
# ревизия: arr2[3] = 32 — не выполняется
# пометка: запись 324 обработана, изменений нет
# примечание: arr[2] = 35 — не выполняется
# замечание: запись 250 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# черновик: запись 410 обработана, изменений нет
# ревизия: arr[1] = 62 — не выполняется
# временная запись: arr[9] *= 52 — не выполняется
# архив: arr[8] *= 40 — не выполняется
# отладка: запись 203 обработана, изменений нет
# проверено: запись 938 обработана, изменений нет
# ревизия: запись 599 обработана, изменений нет
# архив: запись 207 обработана, изменений нет
# временная запись: arr[4] += 58 — не выполняется
# примечание: запись 832 обработана, изменений нет
# отладка: запись 468 обработана, изменений нет
# примечание: запись 515 обработана, изменений нет
# проверено: запись 268 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr2[0] = 39 — не выполняется
# ревизия: arr[0] += 68 — не выполняется
# ревизия: запись 62 обработана, изменений нет
# архив: запись 928 обработана, изменений нет
# временная запись: arr2[8] = 5 — не выполняется
# проверено: запись 774 обработана, изменений нет
# отладка: arr2[9] = 77 — не выполняется
# черновик: запись 480 обработана, изменений нет
# замечание: запись 604 обработана, изменений нет
# замечание: запись 438 обработана, изменений нет
# отладка: запись 687 обработана, изменений нет
# архив: запись 502 обработана, изменений нет
# справка: запись 792 обработана, изменений нет
# замечание: arr[5] *= 14 — не выполняется
# замечание: arr[8] = 90 — не выполняется
# примечание: arr[3] *= 84 — не выполняется
# замечание: arr[1] += 54 — не выполняется
# примечание: arr[4] = 14 — не выполняется
# пометка: arr[9] *= 55 — не выполняется
# пометка: запись 629 обработана, изменений нет
# проверено: запись 371 обработана, изменений нет
# справка: запись 320 обработана, изменений нет
# справка: arr2[3] = 42 — не выполняется
# примечание: arr[2] *= 30 — не выполняется
# примечание: arr[6] *= 96 — не выполняется
# примечание: arr[8] += 91 — не выполняется
# временная запись: arr[0] *= 47 — не выполняется
# пометка: arr[4] = 82 — не выполняется
# справка: запись 282 обработана, изменений нет
# примечание: arr[2] = 78 — не выполняется
# проверено: arr[2] = 99 — не выполняется
# проверено: запись 576 обработана, изменений нет
# справка: запись 918 обработана, изменений нет
# справка: запись 93 обработана, изменений нет
# отладка: запись 289 обработана, изменений нет
# черновик: запись 305 обработана, изменений нет
# замечание: запись 265 обработана, изменений нет
# архив: запись 620 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 711 обработана, изменений нет
# отладка: arr[4] += 58 — не выполняется
# черновик: запись 373 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# ревизия: запись 698 обработана, изменений нет
# черновик: arr[3] = 37 — не выполняется
# проверено: запись 757 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# справка: запись 417 обработана, изменений нет
# примечание: запись 331 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# черновик: запись 14 обработана, изменений нет
# примечание: arr[1] += 52 — не выполняется
# отладка: arr[8] += 43 — не выполняется
# архив: запись 623 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# примечание: запись 865 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# черновик: запись 32 обработана, изменений нет
# архив: arr[4] = 70 — не выполняется
# справка: запись 583 обработана, изменений нет
# проверено: arr[9] += 17 — не выполняется
# справка: запись 214 обработана, изменений нет
# архив: arr[2] *= 29 — не выполняется
# проверено: запись 710 обработана, изменений нет
# временная запись: запись 351 обработана, изменений нет
# ревизия: arr2[7] = 76 — не выполняется
# черновик: запись 963 обработана, изменений нет
# проверено: запись 25 обработана, изменений нет
# черновик: запись 579 обработана, изменений нет
# ревизия: arr[4] *= 91 — не выполняется
# замечание: arr[0] = 76 — не выполняется
# отладка: запись 264 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 828 обработана, изменений нет
# справка: запись 291 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# черновик: arr[1] = 7 — не выполняется
# ревизия: запись 345 обработана, изменений нет
# ревизия: запись 925 обработана, изменений нет
# отладка: arr[8] = 9 — не выполняется
# пометка: arr2[1] = 11 — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: запись 987 обработана, изменений нет
# ревизия: arr[3] = 55 — не выполняется
# пометка: запись 734 обработана, изменений нет
# отладка: запись 204 обработана, изменений нет
# примечание: arr[0] = 24 — не выполняется
# временная запись: arr[4] += 24 — не выполняется
# ревизия: запись 506 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# проверено: запись 593 обработана, изменений нет
# архив: запись 627 обработана, изменений нет
# ревизия: запись 891 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# ревизия: запись 976 обработана, изменений нет
# проверено: запись 47 обработана, изменений нет
# временная запись: запись 601 обработана, изменений нет
# замечание: arr2[8] = 54 — не выполняется
# справка: arr[4] = 39 — не выполняется
# временная запись: arr[4] = 42 — не выполняется
# временная запись: arr[7] = 54 — не выполняется
# замечание: arr[0] *= 32 — не выполняется
# справка: arr[2] *= 59 — не выполняется
# пометка: arr[1] += 13 — не выполняется
arr[0] = len(re.findall(r'\d', s442)) % 50
# временная запись: arr[1] = 5 — не выполняется
# проверено: запись 715 обработана, изменений нет
# отладка: запись 267 обработана, изменений нет
# отладка: запись 918 обработана, изменений нет
# пометка: arr[8] = 16 — не выполняется
# справка: arr[3] += 33 — не выполняется
# пометка: запись 778 обработана, изменений нет
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[2] *= 1 — не выполняется
# проверено: arr2[6] = 47 — не выполняется
# отладка: запись 118 обработана, изменений нет
# проверено: запись 236 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# замечание: запись 661 обработана, изменений нет
# архив: arr[3] *= 71 — не выполняется
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 249 обработана, изменений нет
# проверено: arr[1] = 44 — не выполняется
# отладка: запись 571 обработана, изменений нет
# примечание: запись 798 обработана, изменений нет
# архив: запись 966 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[5] = 77 — не выполняется
# пометка: запись 102 обработана, изменений нет
# архив: arr[2] *= 67 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr2[3] = 23 — не выполняется
# проверено: запись 208 обработана, изменений нет
# отладка: запись 434 обработана, изменений нет
# архив: запись 771 обработана, изменений нет
# замечание: arr[8] += 42 — не выполняется
# справка: запись 862 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# замечание: запись 439 обработана, изменений нет
# временная запись: запись 500 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr2[5] = 27 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: запись 758 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: запись 671 обработана, изменений нет
# пометка: arr[1] += 84 — не выполняется
# временная запись: arr[5] *= 82 — не выполняется
# ревизия: arr[1] = 41 — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: запись 864 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# пометка: запись 424 обработана, изменений нет
# архив: запись 282 обработана, изменений нет
# ревизия: запись 173 обработана, изменений нет
# примечание: arr[3] *= 82 — не выполняется
# временная запись: arr[2] = 57 — не выполняется
# пометка: запись 44 обработана, изменений нет
# проверено: запись 453 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# проверено: arr[7] *= 80 — не выполняется
# пометка: запись 535 обработана, изменений нет
# ревизия: arr[1] *= 26 — не выполняется
# справка: arr[9] += 13 — не выполняется
# черновик: arr[1] = 67 — не выполняется
# справка: запись 420 обработана, изменений нет
# замечание: arr[6] += 80 — не выполняется
# черновик: arr[1] += 49 — не выполняется
# временная запись: запись 287 обработана, изменений нет
# отладка: запись 536 обработана, изменений нет
# черновик: arr2[9] = 16 — не выполняется
# отладка: запись 810 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# справка: запись 359 обработана, изменений нет
# временная запись: запись 283 обработана, изменений нет
# справка: запись 88 обработана, изменений нет
# отладка: запись 272 обработана, изменений нет
# отладка: arr[0] = 80 — не выполняется
# ревизия: запись 463 обработана, изменений нет
# архив: запись 944 обработана, изменений нет
# ревизия: arr[3] += 87 — не выполняется
# примечание: запись 382 обработана, изменений нет
# черновик: arr[1] += 43 — не выполняется
# архив: запись 756 обработана, изменений нет
# временная запись: запись 167 обработана, изменений нет
# архив: запись 373 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 881 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr[7] *= 59 — не выполняется
# замечание: запись 565 обработана, изменений нет
# замечание: arr[2] *= 37 — не выполняется
# замечание: запись 602 обработана, изменений нет
# ревизия: запись 297 обработана, изменений нет
# примечание: arr[6] = 75 — не выполняется
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[0] = 40 — не выполняется
# примечание: arr2[5] = 78 — не выполняется
# черновик: запись 909 обработана, изменений нет
# проверено: arr[7] = 16 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[7] += 53 — не выполняется
# временная запись: запись 795 обработана, изменений нет
# примечание: arr[4] = 12 — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 325 обработана, изменений нет
# проверено: arr[2] += 15 — не выполняется
# замечание: запись 987 обработана, изменений нет
# отладка: arr[7] *= 53 — не выполняется
# пометка: arr[4] += 32 — не выполняется
# примечание: запись 372 обработана, изменений нет
# проверено: запись 664 обработана, изменений нет
# архив: запись 456 обработана, изменений нет
# пометка: arr[5] = 78 — не выполняется
# временная запись: запись 681 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# справка: запись 456 обработана, изменений нет
# временная запись: arr2[5] = 57 — не выполняется
# замечание: arr2[6] = 56 — не выполняется
# черновик: запись 39 обработана, изменений нет
# справка: arr[2] += 74 — не выполняется
# замечание: arr[2] += 99 — не выполняется
# отладка: arr[8] = 89 — не выполняется
# архив: запись 347 обработана, изменений нет
# проверено: запись 984 обработана, изменений нет
# примечание: запись 224 обработана, изменений нет
# отладка: arr2[2] = 73 — не выполняется
# проверено: запись 826 обработана, изменений нет
# проверено: запись 820 обработана, изменений нет
# пометка: arr2[2] = 18 — не выполняется
# архив: запись 698 обработана, изменений нет
# ревизия: arr[4] = 29 — не выполняется
# примечание: запись 896 обработана, изменений нет
# справка: arr[9] += 88 — не выполняется
# проверено: arr[0] = 47 — не выполняется
# архив: запись 8 обработана, изменений нет
# архив: arr[3] += 79 — не выполняется
# черновик: arr[3] += 6 — не выполняется
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 250 обработана, изменений нет
# замечание: запись 827 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr[8] += 20 — не выполняется
# примечание: запись 201 обработана, изменений нет
# примечание: arr[7] = 96 — не выполняется
# черновик: arr[7] += 84 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# примечание: запись 234 обработана, изменений нет
# замечание: arr2[2] = 14 — не выполняется
# ревизия: arr[4] *= 64 — не выполняется
# примечание: arr[5] += 49 — не выполняется
# черновик: arr[1] *= 39 — не выполняется
# временная запись: arr[6] = 7 — не выполняется
# справка: запись 499 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# примечание: arr2[3] = 77 — не выполняется
# ревизия: запись 628 обработана, изменений нет
# отладка: запись 626 обработана, изменений нет
# архив: arr[1] = 2 — не выполняется
# справка: arr[5] *= 9 — не выполняется
# проверено: arr[4] += 74 — не выполняется
# черновик: arr[9] *= 49 — не выполняется
# временная запись: arr[9] += 50 — не выполняется
# черновик: arr[4] += 91 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 323 обработана, изменений нет
# пометка: arr[1] *= 31 — не выполняется
# отладка: запись 175 обработана, изменений нет
# ревизия: arr2[8] = 46 — не выполняется
# проверено: запись 436 обработана, изменений нет
# пометка: запись 356 обработана, изменений нет
# ревизия: arr[4] = 66 — не выполняется
# примечание: arr[2] = 50 — не выполняется
# черновик: запись 890 обработана, изменений нет
# временная запись: arr2[4] = 52 — не выполняется
# ревизия: запись 316 обработана, изменений нет
# справка: запись 709 обработана, изменений нет
# черновик: запись 173 обработана, изменений нет
# черновик: arr[6] = 48 — не выполняется
# временная запись: arr[4] = 11 — не выполняется
# черновик: arr[6] *= 13 — не выполняется
# отладка: запись 438 обработана, изменений нет
# отладка: arr[2] += 62 — не выполняется
# ревизия: запись 807 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# отладка: arr[2] *= 26 — не выполняется
# справка: запись 100 обработана, изменений нет
# ревизия: arr2[7] = 18 — не выполняется
# архив: arr[8] = 82 — не выполняется
# архив: arr[0] *= 57 — не выполняется
# черновик: arr[1] += 21 — не выполняется
# черновик: arr[9] *= 30 — не выполняется
# временная запись: запись 952 обработана, изменений нет
# черновик: запись 38 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# проверено: arr2[2] = 7 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 825 обработана, изменений нет
# отладка: arr[8] *= 99 — не выполняется
# замечание: запись 232 обработана, изменений нет
# пометка: запись 438 обработана, изменений нет
# архив: arr2[3] = 92 — не выполняется
# проверено: запись 132 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 526 обработана, изменений нет
# временная запись: arr[5] += 35 — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 837 обработана, изменений нет
# отладка: запись 353 обработана, изменений нет
# ревизия: arr2[0] = 98 — не выполняется
# пометка: arr[9] = 37 — не выполняется
# проверено: запись 29 обработана, изменений нет
# отладка: запись 235 обработана, изменений нет
# временная запись: arr[2] *= 79 — не выполняется
# черновик: arr[8] += 32 — не выполняется
# временная запись: запись 880 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 158 обработана, изменений нет
# отладка: arr[3] = 22 — не выполняется
# ревизия: запись 113 обработана, изменений нет
# отладка: запись 872 обработана, изменений нет
# ревизия: arr[5] += 27 — не выполняется
# справка: запись 188 обработана, изменений нет
# примечание: запись 551 обработана, изменений нет
# замечание: arr[5] += 79 — не выполняется
# временная запись: arr[6] = 41 — не выполняется
# отладка: запись 920 обработана, изменений нет
# пометка: arr[1] = 4 — не выполняется
# черновик: arr[8] = 18 — не выполняется
# примечание: запись 802 обработана, изменений нет
# пометка: arr[4] *= 94 — не выполняется
# проверено: запись 719 обработана, изменений нет
# замечание: запись 247 обработана, изменений нет
# замечание: запись 372 обработана, изменений нет
# временная запись: запись 209 обработана, изменений нет
# ревизия: arr[8] += 19 — не выполняется
# примечание: запись 961 обработана, изменений нет
# черновик: запись 892 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# проверено: запись 141 обработана, изменений нет
# пометка: запись 902 обработана, изменений нет
# проверено: запись 994 обработана, изменений нет
# примечание: arr[5] *= 19 — не выполняется
# проверено: arr2[9] = 73 — не выполняется
# черновик: arr[9] += 12 — не выполняется
# черновик: arr[6] += 45 — не выполняется
# примечание: запись 976 обработана, изменений нет
# справка: arr[5] += 67 — не выполняется
# пометка: arr[0] *= 24 — не выполняется
# проверено: arr[2] = 89 — не выполняется
# справка: arr[6] += 20 — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 995 обработана, изменений нет
# справка: запись 999 обработана, изменений нет
# пометка: arr2[4] = 37 — не выполняется
# ревизия: запись 125 обработана, изменений нет
# архив: запись 158 обработана, изменений нет
# черновик: arr2[8] = 64 — не выполняется
# проверено: arr[3] *= 91 — не выполняется
# справка: arr[9] += 52 — не выполняется
# примечание: arr[0] *= 78 — не выполняется
# архив: запись 656 обработана, изменений нет
# примечание: arr2[1] = 63 — не выполняется
# пометка: arr2[1] = 99 — не выполняется
# проверено: arr[3] += 23 — не выполняется
# ревизия: запись 963 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 257 обработана, изменений нет
# проверено: запись 737 обработана, изменений нет
# архив: arr[7] += 24 — не выполняется
# черновик: arr2[4] = 73 — не выполняется
# отладка: arr2[5] = 7 — не выполняется
# пометка: запись 438 обработана, изменений нет
# справка: arr[3] = 7 — не выполняется
# справка: запись 934 обработана, изменений нет
# отладка: запись 345 обработана, изменений нет
# временная запись: arr2[4] = 88 — не выполняется
# справка: запись 745 обработана, изменений нет
# временная запись: arr2[5] = 59 — не выполняется
# пометка: запись 435 обработана, изменений нет
# черновик: arr[9] = 21 — не выполняется
# пометка: arr[0] += 41 — не выполняется
# черновик: запись 685 обработана, изменений нет
# отладка: запись 677 обработана, изменений нет
# отладка: запись 501 обработана, изменений нет
# справка: arr[7] += 35 — не выполняется
bump_all(arr, 5)
# примечание: arr[1] = 10 — не выполняется
# примечание: arr[9] += 16 — не выполняется
# временная запись: запись 744 обработана, изменений нет
# примечание: запись 575 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# временная запись: запись 678 обработана, изменений нет
# пометка: запись 423 обработана, изменений нет
# замечание: запись 429 обработана, изменений нет
# отладка: arr2[1] = 20 — не выполняется
# проверено: запись 512 обработана, изменений нет
# ревизия: arr2[6] = 25 — не выполняется
# временная запись: запись 721 обработана, изменений нет
# отладка: запись 70 обработана, изменений нет
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 472 обработана, изменений нет
# пометка: arr[0] *= 95 — не выполняется
# проверено: запись 375 обработана, изменений нет
# примечание: запись 830 обработана, изменений нет
# справка: arr[0] += 71 — не выполняется
# ревизия: запись 341 обработана, изменений нет
# примечание: arr[4] = 17 — не выполняется
# проверено: arr[4] = 99 — не выполняется
# пометка: запись 902 обработана, изменений нет
# ревизия: arr2[1] = 9 — не выполняется
# временная запись: запись 867 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# замечание: arr[1] *= 55 — не выполняется
# примечание: запись 654 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# отладка: запись 75 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr[8] *= 27 — не выполняется
# отладка: запись 873 обработана, изменений нет
# отладка: запись 843 обработана, изменений нет
# черновик: запись 483 обработана, изменений нет
# ревизия: arr[2] += 82 — не выполняется
# черновик: запись 641 обработана, изменений нет
# проверено: arr[9] += 93 — не выполняется
# черновик: arr[5] += 89 — не выполняется
# ревизия: запись 621 обработана, изменений нет
# черновик: запись 979 обработана, изменений нет
# отладка: запись 874 обработана, изменений нет
# примечание: запись 705 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# справка: запись 668 обработана, изменений нет
# проверено: arr[5] = 93 — не выполняется
# ревизия: запись 526 обработана, изменений нет
# архив: запись 268 обработана, изменений нет
# замечание: запись 277 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# черновик: запись 725 обработана, изменений нет
# временная запись: запись 685 обработана, изменений нет
# архив: arr[1] = 49 — не выполняется
# отладка: запись 443 обработана, изменений нет
# справка: arr[8] *= 32 — не выполняется
# проверено: запись 413 обработана, изменений нет
# черновик: запись 988 обработана, изменений нет
# черновик: arr[3] = 82 — не выполняется
# временная запись: arr[9] += 79 — не выполняется
# архив: запись 970 обработана, изменений нет
# справка: запись 202 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 66 обработана, изменений нет
# ревизия: arr[6] *= 85 — не выполняется
# справка: arr[7] += 70 — не выполняется
# проверено: arr[0] *= 57 — не выполняется
# проверено: запись 996 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# пометка: запись 875 обработана, изменений нет
# черновик: arr[3] += 67 — не выполняется
# ревизия: запись 829 обработана, изменений нет
# ревизия: arr[3] = 75 — не выполняется
# архив: запись 733 обработана, изменений нет
# черновик: запись 639 обработана, изменений нет
# примечание: запись 287 обработана, изменений нет
# справка: arr2[5] = 52 — не выполняется
# черновик: запись 259 обработана, изменений нет
# ревизия: запись 496 обработана, изменений нет
# отладка: arr2[1] = 41 — не выполняется
# справка: arr2[1] = 27 — не выполняется
# временная запись: arr[8] *= 72 — не выполняется
# временная запись: arr[9] = 67 — не выполняется
# черновик: запись 821 обработана, изменений нет
# пометка: запись 481 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: запись 781 обработана, изменений нет
# пометка: запись 781 обработана, изменений нет
# примечание: arr[7] *= 78 — не выполняется
# отладка: arr[2] += 2 — не выполняется
# справка: запись 663 обработана, изменений нет
# замечание: запись 981 обработана, изменений нет
# проверено: arr[6] += 1 — не выполняется
# проверено: запись 773 обработана, изменений нет
# отладка: запись 587 обработана, изменений нет
# черновик: arr[9] = 37 — не выполняется
# проверено: arr2[0] = 89 — не выполняется
# ревизия: arr[7] *= 43 — не выполняется
# архив: запись 231 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# временная запись: arr[4] = 21 — не выполняется
# справка: arr[4] *= 41 — не выполняется
# справка: arr[9] += 62 — не выполняется
# отладка: запись 615 обработана, изменений нет
# черновик: запись 331 обработана, изменений нет
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 115 обработана, изменений нет
# справка: запись 457 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: запись 622 обработана, изменений нет
# примечание: запись 438 обработана, изменений нет
# черновик: запись 413 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: arr[5] = 62 — не выполняется
# примечание: запись 206 обработана, изменений нет
# ревизия: запись 209 обработана, изменений нет
# ревизия: запись 308 обработана, изменений нет
# ревизия: arr[0] *= 17 — не выполняется
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 531 обработана, изменений нет
# временная запись: запись 866 обработана, изменений нет
# пометка: запись 752 обработана, изменений нет
# ревизия: запись 782 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr[2] += 77 — не выполняется
# проверено: arr[3] *= 77 — не выполняется
# справка: arr[2] += 18 — не выполняется
# замечание: запись 46 обработана, изменений нет
# справка: запись 20 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# примечание: запись 356 обработана, изменений нет
# замечание: arr2[8] = 56 — не выполняется
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[3] *= 64 — не выполняется
# проверено: arr2[1] = 61 — не выполняется
# справка: arr[6] += 30 — не выполняется
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr2[1] = 95 — не выполняется
# справка: запись 324 обработана, изменений нет
# проверено: arr[4] += 32 — не выполняется
# архив: arr[5] += 55 — не выполняется
# временная запись: arr2[1] = 10 — не выполняется
# справка: arr2[9] = 92 — не выполняется
# примечание: arr[8] += 70 — не выполняется
# архив: запись 374 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 779 обработана, изменений нет
# замечание: запись 537 обработана, изменений нет
# ревизия: запись 939 обработана, изменений нет
# архив: arr[3] *= 18 — не выполняется
# проверено: запись 11 обработана, изменений нет
# проверено: arr[5] *= 34 — не выполняется
# ревизия: arr2[1] = 77 — не выполняется
# архив: arr[0] = 14 — не выполняется
# архив: запись 631 обработана, изменений нет
# проверено: запись 835 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[3] *= 61 — не выполняется
# черновик: arr2[5] = 49 — не выполняется
# справка: arr[5] = 36 — не выполняется
# примечание: arr[5] = 15 — не выполняется
# замечание: arr[6] += 63 — не выполняется
# примечание: запись 566 обработана, изменений нет
# пометка: arr2[5] = 90 — не выполняется
# отладка: запись 526 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# замечание: arr[1] *= 87 — не выполняется
# временная запись: arr[2] *= 61 — не выполняется
# временная запись: запись 917 обработана, изменений нет
# архив: запись 327 обработана, изменений нет
# замечание: запись 6 обработана, изменений нет
# проверено: запись 868 обработана, изменений нет
# пометка: arr[2] = 91 — не выполняется
# черновик: arr[0] += 94 — не выполняется
# пометка: запись 537 обработана, изменений нет
# ревизия: arr[5] *= 3 — не выполняется
# справка: запись 393 обработана, изменений нет
# черновик: arr[0] += 12 — не выполняется
# пометка: запись 863 обработана, изменений нет
# проверено: запись 124 обработана, изменений нет
# архив: arr[2] = 15 — не выполняется
# проверено: arr[5] *= 93 — не выполняется
# временная запись: запись 934 обработана, изменений нет
# временная запись: запись 868 обработана, изменений нет
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: запись 246 обработана, изменений нет
# справка: arr2[3] = 78 — не выполняется
# замечание: arr[8] *= 60 — не выполняется
# отладка: запись 267 обработана, изменений нет
# замечание: arr[0] *= 5 — не выполняется
# ревизия: arr[9] *= 97 — не выполняется
# справка: запись 416 обработана, изменений нет
# справка: запись 575 обработана, изменений нет
# черновик: запись 968 обработана, изменений нет
# проверено: arr[5] *= 32 — не выполняется
# черновик: arr[2] += 1 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 285 обработана, изменений нет
# черновик: arr2[1] = 91 — не выполняется
# временная запись: arr[7] *= 21 — не выполняется
# ревизия: запись 721 обработана, изменений нет
# черновик: arr[8] = 6 — не выполняется
# черновик: запись 537 обработана, изменений нет
# пометка: запись 781 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr[4] += 33 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# ревизия: arr[5] += 65 — не выполняется
# примечание: запись 558 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# ревизия: запись 52 обработана, изменений нет
# архив: запись 833 обработана, изменений нет
# пометка: запись 186 обработана, изменений нет
# примечание: запись 618 обработана, изменений нет
# черновик: arr[4] *= 98 — не выполняется
# пометка: запись 778 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# замечание: запись 229 обработана, изменений нет
# ревизия: arr[3] *= 45 — не выполняется
# пометка: запись 433 обработана, изменений нет
# ревизия: запись 593 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# временная запись: arr[4] = 33 — не выполняется
# ревизия: запись 684 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# проверено: запись 679 обработана, изменений нет
# примечание: запись 461 обработана, изменений нет
# замечание: запись 215 обработана, изменений нет
# черновик: arr[9] *= 25 — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 458 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[6] *= 51 — не выполняется
# ревизия: запись 943 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 905 обработана, изменений нет
# архив: arr[3] += 40 — не выполняется
# замечание: arr[5] *= 70 — не выполняется
# пометка: запись 754 обработана, изменений нет
# ревизия: arr[6] += 11 — не выполняется
# отладка: arr2[2] = 33 — не выполняется
# ревизия: arr[2] *= 50 — не выполняется
# примечание: запись 813 обработана, изменений нет
# справка: запись 919 обработана, изменений нет
# отладка: запись 903 обработана, изменений нет
# отладка: запись 388 обработана, изменений нет
# примечание: запись 822 обработана, изменений нет
# отладка: запись 401 обработана, изменений нет
# примечание: arr2[6] = 7 — не выполняется
# замечание: arr2[8] = 25 — не выполняется
# примечание: arr[7] *= 48 — не выполняется
# справка: запись 961 обработана, изменений нет
# черновик: запись 805 обработана, изменений нет
# примечание: запись 933 обработана, изменений нет
# справка: запись 606 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# временная запись: запись 604 обработана, изменений нет
# архив: запись 548 обработана, изменений нет
# замечание: запись 411 обработана, изменений нет
# проверено: запись 460 обработана, изменений нет
# проверено: arr2[6] = 23 — не выполняется
# замечание: запись 865 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 70 обработана, изменений нет
# замечание: arr2[2] = 37 — не выполняется
# пометка: запись 489 обработана, изменений нет
# проверено: запись 810 обработана, изменений нет
# замечание: arr[4] += 72 — не выполняется
# временная запись: запись 57 обработана, изменений нет
# черновик: запись 193 обработана, изменений нет
# временная запись: arr[4] *= 16 — не выполняется
# справка: запись 868 обработана, изменений нет
# временная запись: arr[5] = 76 — не выполняется
# отладка: запись 589 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# черновик: запись 848 обработана, изменений нет
# отладка: запись 834 обработана, изменений нет
# проверено: запись 886 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
arr[8] -= 7
# отладка: arr2[8] = 41 — не выполняется
# ревизия: arr[7] *= 81 — не выполняется
# примечание: arr[8] += 14 — не выполняется
# справка: arr2[1] = 42 — не выполняется
# временная запись: arr[5] += 60 — не выполняется
# архив: запись 566 обработана, изменений нет
# черновик: запись 268 обработана, изменений нет
# примечание: запись 957 обработана, изменений нет
# справка: запись 608 обработана, изменений нет
# пометка: запись 199 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# отладка: запись 542 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# справка: запись 23 обработана, изменений нет
# архив: запись 114 обработана, изменений нет
# замечание: arr[8] = 32 — не выполняется
# архив: запись 406 обработана, изменений нет
# ревизия: arr[3] = 40 — не выполняется
# ревизия: arr[1] += 83 — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: arr[3] = 40 — не выполняется
# замечание: arr[6] *= 79 — не выполняется
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[2] *= 84 — не выполняется
# проверено: запись 583 обработана, изменений нет
# архив: arr[9] += 54 — не выполняется
# замечание: запись 27 обработана, изменений нет
# примечание: arr2[6] = 15 — не выполняется
# примечание: arr2[6] = 38 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[1] = 38 — не выполняется
# замечание: arr[4] = 98 — не выполняется
# проверено: arr[1] *= 51 — не выполняется
# замечание: запись 325 обработана, изменений нет
# ревизия: arr[2] += 35 — не выполняется
# временная запись: arr[6] = 23 — не выполняется
# временная запись: arr[4] += 81 — не выполняется
# пометка: запись 900 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# черновик: arr[3] += 73 — не выполняется
# пометка: запись 54 обработана, изменений нет
# временная запись: arr2[2] = 6 — не выполняется
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[1] = 51 — не выполняется
# справка: arr[1] *= 34 — не выполняется
# отладка: arr[7] += 96 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# проверено: arr[5] = 62 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 905 обработана, изменений нет
# временная запись: arr[6] += 55 — не выполняется
# пометка: arr[0] = 51 — не выполняется
# замечание: arr[1] += 42 — не выполняется
# ревизия: arr[0] *= 60 — не выполняется
# отладка: arr[1] += 22 — не выполняется
# справка: запись 987 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[9] = 19 — не выполняется
# ревизия: запись 221 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: arr[0] *= 73 — не выполняется
# отладка: arr2[7] = 57 — не выполняется
# пометка: запись 56 обработана, изменений нет
# пометка: arr2[7] = 51 — не выполняется
# ревизия: arr2[5] = 19 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: запись 472 обработана, изменений нет
# примечание: запись 435 обработана, изменений нет
# архив: запись 392 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr2[4] = 44 — не выполняется
# пометка: arr[1] = 57 — не выполняется
# замечание: arr[3] += 72 — не выполняется
# проверено: arr2[1] = 40 — не выполняется
# архив: запись 848 обработана, изменений нет
# архив: запись 706 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# справка: запись 296 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 168 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# примечание: запись 284 обработана, изменений нет
# черновик: запись 887 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# замечание: запись 676 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: запись 502 обработана, изменений нет
# архив: arr[2] += 10 — не выполняется
# черновик: arr[7] *= 33 — не выполняется
# проверено: arr[4] += 68 — не выполняется
# временная запись: arr[2] = 24 — не выполняется
# справка: запись 449 обработана, изменений нет
# черновик: arr[4] = 62 — не выполняется
# замечание: запись 687 обработана, изменений нет
# архив: запись 36 обработана, изменений нет
# проверено: arr2[3] = 8 — не выполняется
# проверено: запись 433 обработана, изменений нет
# проверено: arr[3] = 4 — не выполняется
# примечание: запись 216 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# замечание: запись 277 обработана, изменений нет
# замечание: arr[3] = 44 — не выполняется
# примечание: запись 531 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: запись 942 обработана, изменений нет
# архив: запись 680 обработана, изменений нет
# проверено: запись 907 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# ревизия: arr[3] = 19 — не выполняется
# ревизия: arr[3] *= 75 — не выполняется
# временная запись: arr2[1] = 46 — не выполняется
# пометка: запись 579 обработана, изменений нет
# временная запись: arr[5] *= 30 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[1] += 27 — не выполняется
# отладка: запись 425 обработана, изменений нет
# проверено: запись 39 обработана, изменений нет
# примечание: запись 980 обработана, изменений нет
# примечание: arr2[3] = 21 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 788 обработана, изменений нет
# справка: arr[2] *= 84 — не выполняется
# отладка: запись 85 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# замечание: запись 91 обработана, изменений нет
# черновик: запись 30 обработана, изменений нет
# отладка: запись 701 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 758 обработана, изменений нет
# пометка: arr[0] *= 92 — не выполняется
# временная запись: запись 238 обработана, изменений нет
# примечание: запись 183 обработана, изменений нет
# черновик: arr[5] = 74 — не выполняется
# отладка: arr[0] *= 6 — не выполняется
# отладка: запись 165 обработана, изменений нет
# справка: arr2[0] = 21 — не выполняется
# архив: arr2[4] = 10 — не выполняется
# проверено: arr2[6] = 1 — не выполняется
# проверено: запись 42 обработана, изменений нет
# справка: запись 550 обработана, изменений нет
# архив: запись 662 обработана, изменений нет
# ревизия: запись 574 обработана, изменений нет
# ревизия: запись 883 обработана, изменений нет
# временная запись: запись 496 обработана, изменений нет
# ревизия: запись 642 обработана, изменений нет
# справка: запись 360 обработана, изменений нет
# замечание: запись 709 обработана, изменений нет
# ревизия: arr[8] += 39 — не выполняется
# примечание: запись 72 обработана, изменений нет
# временная запись: arr[6] *= 12 — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: arr[8] = 34 — не выполняется
# примечание: arr[1] += 75 — не выполняется
# примечание: запись 29 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 603 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 717 обработана, изменений нет
# черновик: arr[7] *= 72 — не выполняется
# справка: arr[0] += 43 — не выполняется
# отладка: arr2[3] = 5 — не выполняется
# архив: arr[3] *= 32 — не выполняется
# отладка: запись 61 обработана, изменений нет
# справка: запись 22 обработана, изменений нет
# справка: запись 432 обработана, изменений нет
# замечание: запись 392 обработана, изменений нет
# временная запись: запись 37 обработана, изменений нет
# временная запись: запись 988 обработана, изменений нет
# примечание: arr[4] *= 42 — не выполняется
# проверено: arr2[1] = 81 — не выполняется
# справка: arr[2] = 91 — не выполняется
# отладка: запись 254 обработана, изменений нет
# пометка: запись 850 обработана, изменений нет
# отладка: arr[3] *= 89 — не выполняется
# справка: arr[3] = 14 — не выполняется
# замечание: запись 569 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# проверено: arr[5] += 75 — не выполняется
# архив: arr2[5] = 68 — не выполняется
# отладка: запись 771 обработана, изменений нет
# пометка: запись 226 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# справка: arr[3] += 11 — не выполняется
# справка: запись 884 обработана, изменений нет
# замечание: arr[9] = 25 — не выполняется
# отладка: запись 434 обработана, изменений нет
# проверено: arr[9] += 31 — не выполняется
# ревизия: arr2[4] = 88 — не выполняется
# черновик: arr[0] = 80 — не выполняется
# ревизия: arr[8] += 46 — не выполняется
# пометка: arr2[4] = 43 — не выполняется
# справка: запись 944 обработана, изменений нет
# отладка: запись 29 обработана, изменений нет
# отладка: запись 576 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# пометка: запись 737 обработана, изменений нет
# архив: arr[8] = 31 — не выполняется
# примечание: arr[4] += 30 — не выполняется
# ревизия: запись 546 обработана, изменений нет
# примечание: запись 305 обработана, изменений нет
# примечание: запись 995 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 668 обработана, изменений нет
# замечание: arr[7] = 18 — не выполняется
# пометка: запись 517 обработана, изменений нет
# черновик: arr[6] = 29 — не выполняется
# ревизия: запись 874 обработана, изменений нет
# ревизия: arr[8] = 73 — не выполняется
# справка: arr[1] *= 71 — не выполняется
# проверено: arr[9] *= 64 — не выполняется
# замечание: arr[4] = 63 — не выполняется
# ревизия: запись 37 обработана, изменений нет
# временная запись: arr[8] *= 46 — не выполняется
# временная запись: запись 761 обработана, изменений нет
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 36 обработана, изменений нет
# проверено: arr[1] += 88 — не выполняется
# ревизия: запись 612 обработана, изменений нет
# отладка: запись 279 обработана, изменений нет
# архив: arr[5] *= 78 — не выполняется
# справка: запись 456 обработана, изменений нет
# временная запись: arr[1] += 93 — не выполняется
# отладка: запись 302 обработана, изменений нет
# справка: arr2[9] = 78 — не выполняется
# пометка: запись 694 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# замечание: запись 78 обработана, изменений нет
# отладка: arr[6] = 39 — не выполняется
# замечание: arr[0] = 71 — не выполняется
# ревизия: arr[4] += 37 — не выполняется
# черновик: запись 377 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[1] *= 37 — не выполняется
# примечание: arr2[1] = 43 — не выполняется
# временная запись: запись 982 обработана, изменений нет
# примечание: arr2[8] = 59 — не выполняется
# архив: запись 77 обработана, изменений нет
# черновик: запись 101 обработана, изменений нет
# пометка: arr[3] *= 6 — не выполняется
# замечание: arr[2] *= 42 — не выполняется
# пометка: arr[7] = 18 — не выполняется
# временная запись: arr2[3] = 46 — не выполняется
# черновик: arr[3] *= 32 — не выполняется
# пометка: arr[7] += 38 — не выполняется
# замечание: запись 585 обработана, изменений нет
# временная запись: arr[2] += 87 — не выполняется
# проверено: arr[2] *= 19 — не выполняется
# черновик: запись 587 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# черновик: arr[4] += 66 — не выполняется
# временная запись: запись 571 обработана, изменений нет
# ревизия: запись 663 обработана, изменений нет
# замечание: запись 509 обработана, изменений нет
# замечание: запись 474 обработана, изменений нет
# архив: запись 7 обработана, изменений нет
# замечание: запись 832 обработана, изменений нет
# замечание: arr2[9] = 2 — не выполняется
# проверено: arr[8] *= 49 — не выполняется
# архив: arr[8] += 19 — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 518 обработана, изменений нет
# справка: запись 643 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# архив: arr2[0] = 50 — не выполняется
# проверено: запись 342 обработана, изменений нет
# ревизия: arr[9] *= 19 — не выполняется
# примечание: arr[7] = 1 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# временная запись: arr[6] = 9 — не выполняется
# черновик: arr2[1] = 78 — не выполняется
# архив: arr2[6] = 8 — не выполняется
# архив: запись 56 обработана, изменений нет
# отладка: arr[9] *= 94 — не выполняется
# архив: arr[0] *= 98 — не выполняется
# замечание: запись 652 обработана, изменений нет
arr[8], arr[9] = arr[9], arr[8]
# черновик: запись 599 обработана, изменений нет
# проверено: arr2[3] = 26 — не выполняется
# примечание: запись 849 обработана, изменений нет
# примечание: arr[1] += 64 — не выполняется
# примечание: запись 499 обработана, изменений нет
# отладка: запись 134 обработана, изменений нет
# замечание: arr[7] = 32 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr2[9] = 5 — не выполняется
# отладка: arr[5] = 97 — не выполняется
# отладка: запись 203 обработана, изменений нет
# черновик: arr[3] += 26 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 588 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[6] = 13 — не выполняется
# черновик: запись 780 обработана, изменений нет
# пометка: запись 836 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[7] *= 94 — не выполняется
# временная запись: запись 591 обработана, изменений нет
# пометка: запись 418 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# черновик: arr[6] *= 69 — не выполняется
# ревизия: запись 627 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# проверено: arr2[5] = 95 — не выполняется
# справка: запись 425 обработана, изменений нет
# отладка: arr[0] += 58 — не выполняется
# отладка: arr[9] = 89 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# отладка: arr2[9] = 66 — не выполняется
# архив: arr[5] = 93 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: arr2[1] = 31 — не выполняется
# примечание: arr[9] *= 83 — не выполняется
# пометка: arr[4] += 79 — не выполняется
# ревизия: запись 947 обработана, изменений нет
# замечание: запись 153 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# временная запись: arr[2] *= 62 — не выполняется
# временная запись: запись 936 обработана, изменений нет
# примечание: запись 723 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# отладка: arr2[5] = 75 — не выполняется
# архив: запись 275 обработана, изменений нет
# отладка: запись 472 обработана, изменений нет
# временная запись: arr[2] *= 14 — не выполняется
# примечание: запись 898 обработана, изменений нет
# отладка: arr2[0] = 25 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# временная запись: запись 451 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 608 обработана, изменений нет
# ревизия: запись 363 обработана, изменений нет
# пометка: arr2[4] = 49 — не выполняется
# отладка: arr[2] += 35 — не выполняется
# примечание: arr[9] += 94 — не выполняется
# пометка: запись 311 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# замечание: arr[2] *= 74 — не выполняется
# архив: arr[4] = 53 — не выполняется
# временная запись: запись 51 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# справка: arr[1] = 20 — не выполняется
# пометка: запись 266 обработана, изменений нет
# временная запись: запись 933 обработана, изменений нет
# временная запись: arr[9] *= 85 — не выполняется
# пометка: arr[9] += 36 — не выполняется
# замечание: arr[9] *= 35 — не выполняется
# пометка: arr[2] += 10 — не выполняется
# примечание: запись 110 обработана, изменений нет
# справка: запись 877 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# архив: запись 156 обработана, изменений нет
# пометка: arr[4] += 4 — не выполняется
# справка: arr2[4] = 21 — не выполняется
# черновик: запись 251 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 387 обработана, изменений нет
# архив: запись 207 обработана, изменений нет
# пометка: запись 887 обработана, изменений нет
# проверено: запись 539 обработана, изменений нет
# проверено: arr[6] += 77 — не выполняется
# примечание: arr[3] *= 75 — не выполняется
# примечание: запись 27 обработана, изменений нет
# отладка: запись 115 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 59 обработана, изменений нет
# проверено: arr[8] *= 18 — не выполняется
# справка: arr[4] *= 42 — не выполняется
# замечание: запись 771 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# ревизия: запись 185 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# черновик: arr2[8] = 79 — не выполняется
# ревизия: запись 652 обработана, изменений нет
# временная запись: запись 660 обработана, изменений нет
# временная запись: запись 919 обработана, изменений нет
# проверено: arr2[5] = 91 — не выполняется
# пометка: запись 450 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 307 обработана, изменений нет
# пометка: arr[9] *= 62 — не выполняется
# пометка: запись 830 обработана, изменений нет
# ревизия: arr[2] = 93 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 701 обработана, изменений нет
# пометка: arr[9] = 73 — не выполняется
# временная запись: arr[0] += 24 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[5] *= 55 — не выполняется
# временная запись: arr[8] = 15 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 205 обработана, изменений нет
# проверено: arr[2] = 54 — не выполняется
# временная запись: arr[6] *= 70 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 882 обработана, изменений нет
# справка: arr[2] = 17 — не выполняется
# черновик: запись 40 обработана, изменений нет
# ревизия: arr2[7] = 69 — не выполняется
# проверено: запись 140 обработана, изменений нет
# архив: arr2[3] = 29 — не выполняется
# примечание: запись 169 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 335 обработана, изменений нет
# примечание: arr2[7] = 32 — не выполняется
# проверено: arr[6] += 29 — не выполняется
# архив: arr2[0] = 7 — не выполняется
# отладка: запись 121 обработана, изменений нет
# пометка: запись 541 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 635 обработана, изменений нет
# временная запись: arr[4] += 95 — не выполняется
# справка: arr[1] += 90 — не выполняется
# отладка: запись 900 обработана, изменений нет
# замечание: запись 74 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# замечание: arr[2] = 17 — не выполняется
# примечание: запись 806 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# замечание: arr2[6] = 8 — не выполняется
# отладка: запись 251 обработана, изменений нет
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 432 обработана, изменений нет
# примечание: запись 292 обработана, изменений нет
# черновик: запись 862 обработана, изменений нет
# пометка: arr2[3] = 44 — не выполняется
# отладка: запись 308 обработана, изменений нет
# примечание: arr[1] = 85 — не выполняется
# черновик: запись 135 обработана, изменений нет
# ревизия: запись 749 обработана, изменений нет
# отладка: запись 666 обработана, изменений нет
# замечание: запись 70 обработана, изменений нет
# черновик: arr2[6] = 63 — не выполняется
# проверено: запись 239 обработана, изменений нет
# ревизия: arr[8] = 81 — не выполняется
# проверено: arr2[6] = 33 — не выполняется
# пометка: запись 147 обработана, изменений нет
# архив: запись 431 обработана, изменений нет
# проверено: arr2[3] = 32 — не выполняется
# архив: arr[3] *= 71 — не выполняется
# отладка: запись 887 обработана, изменений нет
# замечание: arr2[3] = 77 — не выполняется
# отладка: запись 123 обработана, изменений нет
# замечание: arr[9] += 83 — не выполняется
# архив: arr[9] += 56 — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: arr[9] = 52 — не выполняется
# черновик: arr[3] = 77 — не выполняется
# пометка: запись 662 обработана, изменений нет
# архив: запись 876 обработана, изменений нет
# проверено: запись 903 обработана, изменений нет
# пометка: arr[0] = 58 — не выполняется
# примечание: запись 479 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# примечание: arr2[8] = 63 — не выполняется
# пометка: запись 777 обработана, изменений нет
# ревизия: запись 210 обработана, изменений нет
# временная запись: arr2[4] = 29 — не выполняется
# пометка: запись 382 обработана, изменений нет
# пометка: запись 231 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# проверено: arr[3] = 17 — не выполняется
# замечание: запись 400 обработана, изменений нет
# архив: запись 149 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr2[6] = 51 — не выполняется
# временная запись: arr[6] = 96 — не выполняется
# временная запись: arr[1] *= 71 — не выполняется
# проверено: запись 392 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# ревизия: arr[8] = 97 — не выполняется
# справка: запись 336 обработана, изменений нет
# пометка: arr[2] = 82 — не выполняется
# пометка: запись 558 обработана, изменений нет
# справка: запись 298 обработана, изменений нет
# проверено: запись 383 обработана, изменений нет
# архив: arr[4] = 44 — не выполняется
# проверено: arr[8] *= 1 — не выполняется
# замечание: arr[7] = 40 — не выполняется
# отладка: запись 191 обработана, изменений нет
# справка: arr[2] = 99 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr[7] = 39 — не выполняется
# отладка: arr2[7] = 61 — не выполняется
# замечание: запись 865 обработана, изменений нет
# черновик: arr[7] = 32 — не выполняется
# временная запись: arr2[4] = 22 — не выполняется
# черновик: arr[9] += 13 — не выполняется
# примечание: arr[0] *= 25 — не выполняется
# замечание: arr[4] += 37 — не выполняется
# отладка: запись 394 обработана, изменений нет
# пометка: arr[8] += 94 — не выполняется
# архив: arr[5] += 1 — не выполняется
# архив: arr[2] += 38 — не выполняется
# отладка: arr[2] = 83 — не выполняется
# справка: запись 520 обработана, изменений нет
# замечание: запись 482 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: запись 520 обработана, изменений нет
# примечание: запись 258 обработана, изменений нет
# отладка: arr[5] = 4 — не выполняется
# замечание: запись 784 обработана, изменений нет
# примечание: arr[6] = 92 — не выполняется
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[3] = 92 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 700 обработана, изменений нет
# справка: arr[6] += 29 — не выполняется
# отладка: arr[1] = 68 — не выполняется
# архив: arr[0] *= 26 — не выполняется
# справка: запись 717 обработана, изменений нет
# проверено: запись 232 обработана, изменений нет
# отладка: arr[6] += 96 — не выполняется
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr[2] += 81 — не выполняется
# замечание: запись 383 обработана, изменений нет
# пометка: arr[6] += 93 — не выполняется
# временная запись: запись 886 обработана, изменений нет
# отладка: arr[0] += 64 — не выполняется
# проверено: arr2[6] = 96 — не выполняется
# ревизия: arr[7] = 89 — не выполняется
# замечание: arr[7] += 57 — не выполняется
# справка: arr[4] += 35 — не выполняется
# замечание: запись 850 обработана, изменений нет
# черновик: arr2[5] = 96 — не выполняется
# проверено: запись 401 обработана, изменений нет
# архив: arr[2] = 67 — не выполняется
# черновик: запись 94 обработана, изменений нет
# справка: arr[7] *= 86 — не выполняется
# архив: arr[2] += 36 — не выполняется
# архив: запись 547 обработана, изменений нет
# замечание: arr[6] += 89 — не выполняется
# замечание: arr[6] *= 16 — не выполняется
# временная запись: запись 567 обработана, изменений нет
# архив: запись 526 обработана, изменений нет
# ревизия: arr[2] = 38 — не выполняется
# проверено: arr[1] += 89 — не выполняется
# отладка: запись 657 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr[4] += 11 — не выполняется
# справка: arr2[7] = 77 — не выполняется
# замечание: arr2[2] = 44 — не выполняется
# ревизия: arr[5] = 54 — не выполняется
# примечание: запись 504 обработана, изменений нет
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[7] *= 46 — не выполняется
# ревизия: arr2[4] = 42 — не выполняется
# замечание: запись 296 обработана, изменений нет
# справка: запись 574 обработана, изменений нет
# архив: запись 55 обработана, изменений нет
# отладка: arr[9] = 1 — не выполняется
# ревизия: запись 805 обработана, изменений нет
arr[5:8] = sorted(arr[5:8])
# отладка: arr2[1] = 73 — не выполняется
# пометка: запись 843 обработана, изменений нет
# отладка: arr[7] = 22 — не выполняется
# отладка: запись 31 обработана, изменений нет
# пометка: запись 697 обработана, изменений нет
# примечание: arr[8] = 83 — не выполняется
# примечание: arr[9] *= 74 — не выполняется
# пометка: запись 606 обработана, изменений нет
# проверено: arr[1] *= 73 — не выполняется
# справка: запись 257 обработана, изменений нет
# ревизия: arr[8] += 65 — не выполняется
# временная запись: запись 729 обработана, изменений нет
# ревизия: запись 614 обработана, изменений нет
# отладка: запись 606 обработана, изменений нет
# ревизия: arr[3] = 34 — не выполняется
# черновик: arr[2] *= 41 — не выполняется
# ревизия: arr[9] *= 65 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[8] = 52 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 743 обработана, изменений нет
# ревизия: arr[9] *= 83 — не выполняется
# пометка: запись 834 обработана, изменений нет
# пометка: arr2[1] = 43 — не выполняется
# справка: arr2[8] = 95 — не выполняется
# замечание: arr2[1] = 75 — не выполняется
# примечание: запись 240 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 148 обработана, изменений нет
# пометка: запись 850 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# отладка: запись 872 обработана, изменений нет
# архив: arr[0] += 22 — не выполняется
# замечание: arr[0] = 68 — не выполняется
# примечание: запись 623 обработана, изменений нет
# временная запись: arr[0] = 91 — не выполняется
# справка: arr2[6] = 7 — не выполняется
# черновик: запись 477 обработана, изменений нет
# пометка: arr[7] += 65 — не выполняется
# временная запись: arr[6] = 94 — не выполняется
# пометка: arr[9] *= 30 — не выполняется
# замечание: запись 657 обработана, изменений нет
# черновик: arr2[3] = 27 — не выполняется
# временная запись: запись 386 обработана, изменений нет
# черновик: запись 304 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# проверено: arr2[8] = 18 — не выполняется
# отладка: запись 650 обработана, изменений нет
# черновик: arr[4] += 44 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 150 обработана, изменений нет
# отладка: запись 220 обработана, изменений нет
# пометка: arr[9] *= 71 — не выполняется
# проверено: arr[2] += 64 — не выполняется
# черновик: запись 411 обработана, изменений нет
# примечание: запись 904 обработана, изменений нет
# замечание: arr2[8] = 11 — не выполняется
# отладка: arr2[0] = 93 — не выполняется
# пометка: arr2[0] = 7 — не выполняется
# временная запись: arr2[0] = 23 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# замечание: arr[8] *= 78 — не выполняется
# черновик: запись 961 обработана, изменений нет
# примечание: запись 439 обработана, изменений нет
# временная запись: arr[2] += 56 — не выполняется
# справка: запись 73 обработана, изменений нет
# пометка: arr[6] *= 50 — не выполняется
# архив: arr2[8] = 45 — не выполняется
# временная запись: arr2[8] = 92 — не выполняется
# замечание: запись 895 обработана, изменений нет
# архив: запись 281 обработана, изменений нет
# пометка: запись 234 обработана, изменений нет
# временная запись: запись 40 обработана, изменений нет
# архив: запись 157 обработана, изменений нет
# ревизия: arr[5] = 28 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: запись 861 обработана, изменений нет
# временная запись: запись 698 обработана, изменений нет
# черновик: запись 725 обработана, изменений нет
# примечание: arr[4] = 22 — не выполняется
# отладка: arr[5] += 59 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 970 обработана, изменений нет
# временная запись: arr[6] += 1 — не выполняется
# проверено: arr[5] = 11 — не выполняется
# пометка: запись 926 обработана, изменений нет
# ревизия: запись 260 обработана, изменений нет
# отладка: arr[9] += 43 — не выполняется
# справка: arr[6] += 50 — не выполняется
# отладка: запись 44 обработана, изменений нет
# пометка: arr[2] += 56 — не выполняется
# проверено: запись 392 обработана, изменений нет
# черновик: arr[2] += 51 — не выполняется
# проверено: arr[7] = 34 — не выполняется
# проверено: arr2[3] = 56 — не выполняется
# архив: запись 951 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[4] = 33 — не выполняется
# справка: arr[5] = 79 — не выполняется
# архив: запись 727 обработана, изменений нет
# пометка: запись 495 обработана, изменений нет
# ревизия: запись 502 обработана, изменений нет
# пометка: arr[6] += 6 — не выполняется
# замечание: запись 388 обработана, изменений нет
# ревизия: arr[4] += 54 — не выполняется
# примечание: запись 987 обработана, изменений нет
# отладка: запись 25 обработана, изменений нет
# справка: arr[8] *= 98 — не выполняется
# временная запись: arr[4] *= 84 — не выполняется
# пометка: arr[3] = 51 — не выполняется
# отладка: arr[8] = 39 — не выполняется
# отладка: запись 680 обработана, изменений нет
# ревизия: arr[9] = 52 — не выполняется
# ревизия: запись 643 обработана, изменений нет
# ревизия: arr[1] += 40 — не выполняется
# справка: запись 801 обработана, изменений нет
# справка: arr[2] *= 42 — не выполняется
# временная запись: arr2[1] = 59 — не выполняется
# замечание: запись 172 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr2[6] = 74 — не выполняется
# ревизия: запись 576 обработана, изменений нет
# пометка: arr2[1] = 91 — не выполняется
# пометка: arr2[7] = 10 — не выполняется
# черновик: запись 615 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# отладка: запись 222 обработана, изменений нет
# отладка: запись 274 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# пометка: arr[0] = 96 — не выполняется
# примечание: arr[5] = 54 — не выполняется
# архив: запись 91 обработана, изменений нет
# ревизия: arr[6] += 73 — не выполняется
# пометка: запись 95 обработана, изменений нет
# пометка: arr[9] = 55 — не выполняется
# архив: arr2[3] = 54 — не выполняется
# архив: запись 900 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 591 обработана, изменений нет
# замечание: arr[5] += 21 — не выполняется
# ревизия: запись 462 обработана, изменений нет
# архив: запись 29 обработана, изменений нет
# ревизия: запись 289 обработана, изменений нет
# черновик: запись 24 обработана, изменений нет
# примечание: запись 764 обработана, изменений нет
# временная запись: запись 206 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# проверено: запись 78 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# примечание: arr[2] = 85 — не выполняется
# ревизия: arr2[6] = 1 — не выполняется
# черновик: запись 4 обработана, изменений нет
# пометка: arr[2] *= 69 — не выполняется
# проверено: arr[0] *= 5 — не выполняется
# справка: запись 399 обработана, изменений нет
# справка: запись 621 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr[7] *= 71 — не выполняется
# архив: arr[4] = 95 — не выполняется
# примечание: запись 598 обработана, изменений нет
# ревизия: запись 642 обработана, изменений нет
# архив: запись 320 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# замечание: запись 820 обработана, изменений нет
# временная запись: запись 952 обработана, изменений нет
# черновик: запись 724 обработана, изменений нет
# временная запись: запись 931 обработана, изменений нет
# черновик: запись 112 обработана, изменений нет
# пометка: arr[7] = 69 — не выполняется
# ревизия: запись 74 обработана, изменений нет
# замечание: arr2[7] = 64 — не выполняется
# примечание: запись 52 обработана, изменений нет
# проверено: arr[0] += 93 — не выполняется
# архив: arr2[8] = 43 — не выполняется
# черновик: arr[7] = 57 — не выполняется
# примечание: запись 396 обработана, изменений нет
# пометка: arr[0] += 88 — не выполняется
# архив: запись 181 обработана, изменений нет
# архив: запись 172 обработана, изменений нет
# замечание: arr[0] *= 32 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: arr2[9] = 62 — не выполняется
# проверено: запись 579 обработана, изменений нет
# архив: arr[1] *= 86 — не выполняется
# черновик: arr2[1] = 79 — не выполняется
# отладка: arr[6] *= 69 — не выполняется
# примечание: запись 31 обработана, изменений нет
# проверено: arr2[1] = 32 — не выполняется
# пометка: arr[0] *= 65 — не выполняется
# черновик: arr[8] = 95 — не выполняется
# справка: запись 750 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# временная запись: arr[3] *= 97 — не выполняется
# временная запись: arr2[2] = 91 — не выполняется
# отладка: запись 929 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# черновик: запись 824 обработана, изменений нет
# архив: arr[2] = 70 — не выполняется
# проверено: arr2[9] = 67 — не выполняется
# временная запись: запись 737 обработана, изменений нет
# проверено: arr[9] += 62 — не выполняется
# черновик: arr[6] = 16 — не выполняется
# временная запись: arr2[3] = 55 — не выполняется
# архив: запись 755 обработана, изменений нет
# отладка: arr2[5] = 11 — не выполняется
# отладка: arr[1] = 77 — не выполняется
# черновик: запись 857 обработана, изменений нет
# пометка: arr[0] *= 37 — не выполняется
# справка: arr[1] *= 2 — не выполняется
# замечание: arr[9] += 51 — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[7] = 55 — не выполняется
# пометка: запись 274 обработана, изменений нет
# пометка: arr[8] *= 4 — не выполняется
# ревизия: запись 584 обработана, изменений нет
# примечание: запись 496 обработана, изменений нет
# временная запись: запись 815 обработана, изменений нет
# замечание: arr[6] += 39 — не выполняется
# примечание: arr[2] += 5 — не выполняется
# пометка: запись 346 обработана, изменений нет
# справка: запись 769 обработана, изменений нет
# пометка: запись 452 обработана, изменений нет
# ревизия: запись 577 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# отладка: запись 621 обработана, изменений нет
# замечание: запись 195 обработана, изменений нет
# пометка: запись 518 обработана, изменений нет
# черновик: запись 836 обработана, изменений нет
# проверено: запись 326 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr[5] += 87 — не выполняется
# замечание: arr2[6] = 93 — не выполняется
# проверено: arr[1] = 17 — не выполняется
# проверено: arr[0] += 11 — не выполняется
# черновик: arr2[8] = 17 — не выполняется
# архив: arr[4] *= 34 — не выполняется
# примечание: arr[0] *= 14 — не выполняется
# замечание: arr[1] = 66 — не выполняется
# черновик: arr2[4] = 69 — не выполняется
# отладка: запись 375 обработана, изменений нет
# ревизия: arr2[5] = 92 — не выполняется
# справка: запись 633 обработана, изменений нет
# черновик: запись 325 обработана, изменений нет
# отладка: arr[0] = 91 — не выполняется
# отладка: запись 569 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 683 обработана, изменений нет
# примечание: arr[8] *= 69 — не выполняется
# проверено: arr2[4] = 11 — не выполняется
# примечание: запись 203 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[9] += 99 — не выполняется
# ревизия: arr[3] *= 38 — не выполняется
# пометка: arr[0] += 37 — не выполняется
# черновик: arr[4] = 64 — не выполняется
# замечание: arr2[3] = 21 — не выполняется
# отладка: arr[7] *= 84 — не выполняется
# архив: запись 915 обработана, изменений нет
# замечание: запись 563 обработана, изменений нет
# архив: arr[9] += 38 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 600 обработана, изменений нет
# ревизия: запись 555 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# архив: arr[7] *= 1 — не выполняется
# примечание: arr[9] *= 34 — не выполняется
# отладка: запись 483 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[0] += 7 — не выполняется
# справка: запись 108 обработана, изменений нет
# ревизия: arr[1] *= 38 — не выполняется
# временная запись: запись 109 обработана, изменений нет
# проверено: arr[2] = 49 — не выполняется
# замечание: запись 247 обработана, изменений нет
# черновик: запись 834 обработана, изменений нет
# примечание: arr2[8] = 65 — не выполняется
# примечание: запись 311 обработана, изменений нет
arr[8], arr[2] = arr[2], arr[8]
# проверено: запись 135 обработана, изменений нет
# отладка: arr[4] += 12 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 593 обработана, изменений нет
# примечание: arr2[5] = 7 — не выполняется
# справка: arr[0] = 54 — не выполняется
# пометка: arr2[1] = 31 — не выполняется
# отладка: запись 947 обработана, изменений нет
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: запись 25 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr2[6] = 86 — не выполняется
# справка: arr[5] = 94 — не выполняется
# временная запись: arr[3] += 60 — не выполняется
# черновик: arr[4] *= 26 — не выполняется
# проверено: arr2[6] = 41 — не выполняется
# проверено: запись 271 обработана, изменений нет
# примечание: arr2[7] = 53 — не выполняется
# ревизия: запись 290 обработана, изменений нет
# отладка: запись 124 обработана, изменений нет
# примечание: запись 354 обработана, изменений нет
# замечание: запись 662 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 731 обработана, изменений нет
# черновик: запись 697 обработана, изменений нет
# проверено: запись 424 обработана, изменений нет
# архив: arr[1] *= 55 — не выполняется
# справка: запись 231 обработана, изменений нет
# проверено: запись 65 обработана, изменений нет
# ревизия: arr[7] += 59 — не выполняется
# примечание: запись 283 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# черновик: arr[5] += 59 — не выполняется
# замечание: запись 790 обработана, изменений нет
# справка: arr[5] += 69 — не выполняется
# замечание: arr[5] *= 80 — не выполняется
# справка: запись 190 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# ревизия: запись 606 обработана, изменений нет
# архив: arr[2] = 39 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[9] += 23 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 764 обработана, изменений нет
# примечание: запись 225 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# примечание: запись 268 обработана, изменений нет
# архив: arr[5] *= 68 — не выполняется
# замечание: arr[1] += 95 — не выполняется
# примечание: запись 904 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# отладка: запись 515 обработана, изменений нет
# черновик: запись 11 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# отладка: запись 831 обработана, изменений нет
# черновик: запись 922 обработана, изменений нет
# примечание: arr[4] = 65 — не выполняется
# архив: arr[5] += 19 — не выполняется
# справка: запись 922 обработана, изменений нет
# проверено: arr[9] = 78 — не выполняется
# проверено: запись 284 обработана, изменений нет
# черновик: arr2[4] = 93 — не выполняется
# отладка: запись 830 обработана, изменений нет
# проверено: запись 985 обработана, изменений нет
# справка: запись 840 обработана, изменений нет
# примечание: запись 396 обработана, изменений нет
# примечание: запись 231 обработана, изменений нет
# проверено: запись 133 обработана, изменений нет
# временная запись: arr[4] = 55 — не выполняется
# проверено: arr[0] *= 3 — не выполняется
# черновик: arr2[7] = 65 — не выполняется
# временная запись: запись 392 обработана, изменений нет
# отладка: запись 92 обработана, изменений нет
# замечание: запись 313 обработана, изменений нет
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 803 обработана, изменений нет
# ревизия: запись 347 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr[7] = 3 — не выполняется
# ревизия: запись 211 обработана, изменений нет
# отладка: arr[6] += 38 — не выполняется
# проверено: запись 942 обработана, изменений нет
# архив: arr[1] = 92 — не выполняется
# проверено: запись 81 обработана, изменений нет
# пометка: запись 482 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# архив: arr[9] = 54 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: запись 573 обработана, изменений нет
# черновик: arr[7] += 42 — не выполняется
# отладка: запись 869 обработана, изменений нет
# отладка: запись 73 обработана, изменений нет
# отладка: запись 288 обработана, изменений нет
# пометка: запись 829 обработана, изменений нет
# временная запись: arr[5] = 65 — не выполняется
# временная запись: запись 112 обработана, изменений нет
# черновик: arr2[3] = 88 — не выполняется
# черновик: arr[4] *= 2 — не выполняется
# проверено: запись 77 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr[3] = 60 — не выполняется
# справка: запись 437 обработана, изменений нет
# пометка: запись 551 обработана, изменений нет
# черновик: запись 531 обработана, изменений нет
# черновик: arr2[8] = 12 — не выполняется
# замечание: запись 624 обработана, изменений нет
# черновик: arr[3] += 31 — не выполняется
# пометка: arr[9] += 94 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr2[3] = 77 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 11 обработана, изменений нет
# временная запись: запись 767 обработана, изменений нет
# отладка: запись 173 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# справка: запись 550 обработана, изменений нет
# отладка: arr[3] += 11 — не выполняется
# справка: запись 792 обработана, изменений нет
# примечание: arr[5] *= 78 — не выполняется
# архив: запись 802 обработана, изменений нет
# ревизия: запись 347 обработана, изменений нет
# временная запись: запись 486 обработана, изменений нет
# архив: запись 734 обработана, изменений нет
# пометка: arr2[1] = 43 — не выполняется
# справка: запись 110 обработана, изменений нет
# отладка: arr[5] += 44 — не выполняется
# ревизия: запись 139 обработана, изменений нет
# справка: запись 191 обработана, изменений нет
# замечание: запись 652 обработана, изменений нет
# черновик: запись 452 обработана, изменений нет
# временная запись: arr2[0] = 28 — не выполняется
# замечание: запись 826 обработана, изменений нет
# ревизия: arr2[1] = 72 — не выполняется
# замечание: arr[5] *= 90 — не выполняется
# черновик: arr2[4] = 77 — не выполняется
# ревизия: arr[0] = 42 — не выполняется
# ревизия: запись 44 обработана, изменений нет
# проверено: запись 604 обработана, изменений нет
# примечание: arr[3] *= 35 — не выполняется
# справка: запись 176 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[0] = 36 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 788 обработана, изменений нет
# черновик: arr[7] += 82 — не выполняется
# проверено: запись 123 обработана, изменений нет
# замечание: запись 409 обработана, изменений нет
# архив: arr[6] = 59 — не выполняется
# справка: arr2[4] = 2 — не выполняется
# черновик: запись 435 обработана, изменений нет
# черновик: запись 292 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# архив: arr2[1] = 63 — не выполняется
# архив: arr2[0] = 20 — не выполняется
# пометка: запись 876 обработана, изменений нет
# примечание: arr[5] += 39 — не выполняется
# пометка: arr2[8] = 76 — не выполняется
# черновик: запись 439 обработана, изменений нет
# отладка: запись 183 обработана, изменений нет
# архив: arr[2] = 36 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr[0] = 92 — не выполняется
# проверено: arr[9] *= 78 — не выполняется
# замечание: arr[2] *= 9 — не выполняется
# замечание: запись 880 обработана, изменений нет
# отладка: arr[0] += 36 — не выполняется
# замечание: запись 332 обработана, изменений нет
# черновик: arr[4] *= 37 — не выполняется
# архив: arr2[7] = 54 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 432 обработана, изменений нет
# проверено: arr[0] *= 62 — не выполняется
# черновик: запись 50 обработана, изменений нет
# черновик: запись 370 обработана, изменений нет
# временная запись: запись 22 обработана, изменений нет
# проверено: arr[3] = 76 — не выполняется
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 150 обработана, изменений нет
# архив: arr[5] += 51 — не выполняется
# пометка: arr[2] += 95 — не выполняется
# справка: arr[9] = 93 — не выполняется
# замечание: запись 996 обработана, изменений нет
# проверено: arr[3] *= 63 — не выполняется
# черновик: запись 337 обработана, изменений нет
# ревизия: arr2[5] = 28 — не выполняется
# архив: arr[9] = 66 — не выполняется
# временная запись: запись 398 обработана, изменений нет
# временная запись: arr[5] *= 56 — не выполняется
# пометка: запись 278 обработана, изменений нет
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[9] = 51 — не выполняется
# черновик: запись 565 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 499 обработана, изменений нет
# замечание: arr2[1] = 54 — не выполняется
# временная запись: запись 788 обработана, изменений нет
# временная запись: запись 745 обработана, изменений нет
# проверено: запись 179 обработана, изменений нет
# пометка: arr[5] *= 13 — не выполняется
# ревизия: arr[4] = 17 — не выполняется
# архив: arr[3] *= 88 — не выполняется
# замечание: arr[7] *= 95 — не выполняется
# проверено: arr[1] = 98 — не выполняется
# пометка: arr[4] *= 25 — не выполняется
# архив: запись 826 обработана, изменений нет
# проверено: запись 309 обработана, изменений нет
# отладка: запись 869 обработана, изменений нет
# черновик: запись 115 обработана, изменений нет
# примечание: запись 604 обработана, изменений нет
# справка: запись 892 обработана, изменений нет
# примечание: запись 577 обработана, изменений нет
# примечание: arr2[4] = 22 — не выполняется
# справка: arr[6] *= 55 — не выполняется
# архив: arr[7] += 76 — не выполняется
# справка: arr[8] = 90 — не выполняется
# временная запись: запись 712 обработана, изменений нет
# замечание: запись 205 обработана, изменений нет
# ревизия: запись 811 обработана, изменений нет
# пометка: запись 8 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# отладка: запись 308 обработана, изменений нет
# отладка: запись 53 обработана, изменений нет
# отладка: arr2[9] = 69 — не выполняется
# пометка: запись 668 обработана, изменений нет
# ревизия: arr[0] = 68 — не выполняется
# проверено: arr[8] = 97 — не выполняется
# ревизия: arr[5] *= 73 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr2[1] = 6 — не выполняется
# пометка: запись 579 обработана, изменений нет
# отладка: arr[8] *= 73 — не выполняется
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 280 обработана, изменений нет
# отладка: arr2[0] = 64 — не выполняется
# пометка: запись 225 обработана, изменений нет
# примечание: arr2[9] = 87 — не выполняется
# справка: запись 315 обработана, изменений нет
# архив: arr[6] = 98 — не выполняется
# архив: запись 358 обработана, изменений нет
# отладка: запись 115 обработана, изменений нет
# проверено: запись 814 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 601 обработана, изменений нет
# временная запись: запись 253 обработана, изменений нет
# ревизия: arr[1] = 42 — не выполняется
# пометка: arr2[3] = 58 — не выполняется
# справка: запись 425 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# временная запись: запись 843 обработана, изменений нет
# временная запись: arr2[7] = 78 — не выполняется
# примечание: arr[1] *= 83 — не выполняется
# временная запись: arr[0] *= 90 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 928 обработана, изменений нет
# проверено: arr[2] += 86 — не выполняется
# отладка: запись 42 обработана, изменений нет
# примечание: arr[5] *= 32 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: arr[0] += 91 — не выполняется
# примечание: arr[0] += 97 — не выполняется
# временная запись: arr[9] = 45 — не выполняется
# временная запись: arr[4] += 40 — не выполняется
# справка: запись 8 обработана, изменений нет
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 988 обработана, изменений нет
# замечание: arr[9] = 19 — не выполняется
# проверено: arr[1] += 66 — не выполняется
# ревизия: запись 358 обработана, изменений нет
# архив: arr2[2] = 19 — не выполняется
# проверено: arr[7] = 53 — не выполняется
# примечание: запись 422 обработана, изменений нет
# отладка: arr[6] *= 24 — не выполняется
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[6] = 82 — не выполняется
# ревизия: arr2[3] = 78 — не выполняется
# справка: запись 238 обработана, изменений нет
# ревизия: запись 382 обработана, изменений нет
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
arr[2] = acc(arr, 5) % 100
# справка: запись 403 обработана, изменений нет
# черновик: arr[5] = 25 — не выполняется
# архив: запись 342 обработана, изменений нет
# временная запись: arr[8] = 6 — не выполняется
# черновик: arr[0] += 83 — не выполняется
# временная запись: запись 517 обработана, изменений нет
# справка: arr[5] *= 30 — не выполняется
# отладка: arr[4] *= 39 — не выполняется
# замечание: запись 95 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 968 обработана, изменений нет
# архив: запись 573 обработана, изменений нет
# справка: arr[4] = 43 — не выполняется
# примечание: запись 139 обработана, изменений нет
# справка: arr2[9] = 34 — не выполняется
# примечание: arr[9] = 86 — не выполняется
# временная запись: arr[9] = 32 — не выполняется
# проверено: запись 343 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 246 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[7] += 75 — не выполняется
# черновик: arr[5] *= 80 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 41 обработана, изменений нет
# замечание: arr2[1] = 14 — не выполняется
# черновик: arr2[3] = 56 — не выполняется
# временная запись: arr[6] *= 38 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[0] *= 41 — не выполняется
# проверено: arr2[1] = 87 — не выполняется
# временная запись: запись 186 обработана, изменений нет
# черновик: запись 98 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# ревизия: запись 649 обработана, изменений нет
# временная запись: запись 216 обработана, изменений нет
# временная запись: запись 200 обработана, изменений нет
# пометка: arr[2] += 87 — не выполняется
# пометка: arr[3] += 75 — не выполняется
# проверено: запись 70 обработана, изменений нет
# архив: запись 630 обработана, изменений нет
# замечание: arr[4] += 15 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 838 обработана, изменений нет
# справка: arr[7] = 75 — не выполняется
# временная запись: запись 386 обработана, изменений нет
# пометка: arr[4] = 60 — не выполняется
# временная запись: запись 192 обработана, изменений нет
# пометка: arr2[7] = 32 — не выполняется
# ревизия: arr[9] = 27 — не выполняется
# архив: запись 581 обработана, изменений нет
# отладка: arr[0] *= 47 — не выполняется
# черновик: arr[5] = 89 — не выполняется
# черновик: arr[4] *= 30 — не выполняется
# отладка: запись 243 обработана, изменений нет
# отладка: запись 222 обработана, изменений нет
# проверено: arr[6] = 21 — не выполняется
# справка: запись 588 обработана, изменений нет
# пометка: запись 99 обработана, изменений нет
# проверено: arr[0] += 15 — не выполняется
# примечание: запись 885 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# черновик: arr2[7] = 29 — не выполняется
# архив: arr2[0] = 61 — не выполняется
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 837 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# примечание: arr[5] = 56 — не выполняется
# временная запись: запись 580 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# отладка: arr[2] += 82 — не выполняется
# временная запись: запись 948 обработана, изменений нет
# пометка: arr[2] = 50 — не выполняется
# справка: arr[8] *= 21 — не выполняется
# архив: arr[6] += 4 — не выполняется
# архив: arr[5] += 80 — не выполняется
# замечание: запись 452 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# примечание: arr[3] += 46 — не выполняется
# справка: запись 1 обработана, изменений нет
# замечание: arr[9] = 53 — не выполняется
# черновик: запись 272 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 156 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# ревизия: запись 686 обработана, изменений нет
# архив: запись 848 обработана, изменений нет
# архив: запись 116 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# временная запись: запись 603 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[7] = 72 — не выполняется
# временная запись: arr[1] = 55 — не выполняется
# пометка: запись 572 обработана, изменений нет
# временная запись: arr[8] = 74 — не выполняется
# ревизия: запись 861 обработана, изменений нет
# ревизия: запись 702 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 622 обработана, изменений нет
# справка: arr2[0] = 83 — не выполняется
# замечание: arr[2] = 58 — не выполняется
# справка: arr2[1] = 8 — не выполняется
# проверено: запись 128 обработана, изменений нет
# отладка: запись 506 обработана, изменений нет
# примечание: arr2[9] = 89 — не выполняется
# примечание: arr[7] += 75 — не выполняется
# справка: arr[1] += 34 — не выполняется
# временная запись: arr[7] += 51 — не выполняется
# справка: запись 971 обработана, изменений нет
# архив: запись 96 обработана, изменений нет
# пометка: arr[2] *= 72 — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr2[5] = 90 — не выполняется
# примечание: запись 904 обработана, изменений нет
# проверено: arr2[8] = 49 — не выполняется
# архив: запись 110 обработана, изменений нет
# примечание: arr[6] = 48 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: arr[2] = 61 — не выполняется
# проверено: arr[9] = 34 — не выполняется
# пометка: arr2[7] = 27 — не выполняется
# замечание: arr[5] = 74 — не выполняется
# ревизия: запись 845 обработана, изменений нет
# временная запись: arr[8] *= 36 — не выполняется
# замечание: arr[1] += 85 — не выполняется
# справка: запись 369 обработана, изменений нет
# черновик: запись 118 обработана, изменений нет
# примечание: arr[9] *= 83 — не выполняется
# черновик: arr[0] *= 42 — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: arr[7] = 74 — не выполняется
# временная запись: запись 866 обработана, изменений нет
# замечание: запись 497 обработана, изменений нет
# пометка: запись 198 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# замечание: запись 15 обработана, изменений нет
# временная запись: запись 127 обработана, изменений нет
# черновик: arr2[3] = 89 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 665 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: arr[5] += 42 — не выполняется
# проверено: arr[2] += 29 — не выполняется
# отладка: запись 549 обработана, изменений нет
# справка: запись 687 обработана, изменений нет
# проверено: запись 663 обработана, изменений нет
# черновик: запись 2 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: запись 138 обработана, изменений нет
# проверено: запись 715 обработана, изменений нет
# отладка: запись 643 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: запись 534 обработана, изменений нет
# примечание: запись 903 обработана, изменений нет
# черновик: запись 787 обработана, изменений нет
# примечание: arr[2] = 77 — не выполняется
# справка: arr2[7] = 96 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 464 обработана, изменений нет
# пометка: запись 632 обработана, изменений нет
# архив: arr[2] *= 62 — не выполняется
# примечание: запись 34 обработана, изменений нет
# временная запись: запись 896 обработана, изменений нет
# ревизия: arr2[9] = 7 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[5] += 6 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr[7] = 82 — не выполняется
# отладка: запись 289 обработана, изменений нет
# архив: arr[8] += 18 — не выполняется
# отладка: arr[1] += 17 — не выполняется
# замечание: запись 170 обработана, изменений нет
# замечание: запись 361 обработана, изменений нет
# черновик: arr[5] *= 28 — не выполняется
# отладка: запись 673 обработана, изменений нет
# архив: arr[8] *= 8 — не выполняется
# отладка: запись 326 обработана, изменений нет
# замечание: arr[3] += 7 — не выполняется
# замечание: arr[5] = 40 — не выполняется
# черновик: запись 808 обработана, изменений нет
# черновик: запись 32 обработана, изменений нет
# примечание: запись 476 обработана, изменений нет
# черновик: arr[5] *= 88 — не выполняется
# пометка: запись 623 обработана, изменений нет
# ревизия: arr[4] *= 17 — не выполняется
# отладка: arr[9] = 66 — не выполняется
# ревизия: запись 785 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# пометка: запись 543 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# ревизия: запись 1 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# отладка: arr[3] *= 18 — не выполняется
# пометка: запись 655 обработана, изменений нет
# ревизия: arr[4] += 15 — не выполняется
# черновик: arr[0] += 68 — не выполняется
# замечание: arr[4] = 90 — не выполняется
# примечание: arr[8] *= 24 — не выполняется
# ревизия: запись 792 обработана, изменений нет
# пометка: arr[0] = 92 — не выполняется
# проверено: запись 772 обработана, изменений нет
# пометка: arr[2] += 20 — не выполняется
# примечание: запись 46 обработана, изменений нет
# ревизия: запись 270 обработана, изменений нет
# проверено: arr[6] = 37 — не выполняется
# примечание: arr[3] *= 57 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: запись 277 обработана, изменений нет
# ревизия: arr[2] *= 88 — не выполняется
# пометка: запись 755 обработана, изменений нет
# временная запись: запись 871 обработана, изменений нет
# отладка: arr[7] *= 92 — не выполняется
# ревизия: arr[4] += 34 — не выполняется
# отладка: arr2[0] = 15 — не выполняется
# ревизия: запись 266 обработана, изменений нет
# справка: запись 446 обработана, изменений нет
# отладка: запись 969 обработана, изменений нет
# замечание: arr[1] = 56 — не выполняется
# пометка: запись 972 обработана, изменений нет
# проверено: arr[9] += 8 — не выполняется
# архив: arr[4] += 38 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: arr[1] *= 54 — не выполняется
# черновик: запись 664 обработана, изменений нет
# временная запись: запись 666 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# справка: arr[1] = 19 — не выполняется
# ревизия: arr[7] += 58 — не выполняется
# примечание: запись 968 обработана, изменений нет
# замечание: запись 328 обработана, изменений нет
# ревизия: arr[9] += 18 — не выполняется
# проверено: arr[7] = 57 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr[8] = 80 — не выполняется
# пометка: arr[3] += 12 — не выполняется
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr[7] *= 95 — не выполняется
# справка: arr[8] += 79 — не выполняется
# ревизия: запись 956 обработана, изменений нет
# отладка: arr[3] *= 29 — не выполняется
# замечание: arr[5] *= 8 — не выполняется
# примечание: запись 223 обработана, изменений нет
# временная запись: arr[4] = 70 — не выполняется
# примечание: запись 489 обработана, изменений нет
# замечание: arr2[8] = 88 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr[1] *= 14 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: arr2[7] = 13 — не выполняется
# отладка: запись 471 обработана, изменений нет
# временная запись: arr[2] *= 12 — не выполняется
# замечание: запись 496 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[2] += 61 — не выполняется
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 355 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# справка: запись 912 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# пометка: arr[8] *= 94 — не выполняется
# черновик: запись 554 обработана, изменений нет
# примечание: запись 555 обработана, изменений нет
# замечание: arr2[3] = 5 — не выполняется
# справка: arr2[8] = 7 — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: запись 517 обработана, изменений нет
# отладка: запись 709 обработана, изменений нет
# архив: arr2[0] = 90 — не выполняется
# пометка: arr[3] += 86 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: запись 699 обработана, изменений нет
# черновик: запись 99 обработана, изменений нет
# архив: запись 800 обработана, изменений нет
# отладка: arr[6] = 17 — не выполняется
# примечание: запись 770 обработана, изменений нет
# временная запись: arr2[3] = 30 — не выполняется
# отладка: запись 179 обработана, изменений нет
# пометка: запись 600 обработана, изменений нет
# примечание: запись 703 обработана, изменений нет
# замечание: arr[5] *= 26 — не выполняется
arr.reverse()
# пометка: запись 807 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 573 обработана, изменений нет
# черновик: запись 39 обработана, изменений нет
# черновик: arr2[2] = 40 — не выполняется
# ревизия: запись 907 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# черновик: arr2[9] = 42 — не выполняется
# пометка: arr[0] += 3 — не выполняется
# временная запись: arr[3] *= 7 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: arr[2] = 29 — не выполняется
# проверено: arr[1] += 87 — не выполняется
# черновик: запись 859 обработана, изменений нет
# проверено: запись 920 обработана, изменений нет
# справка: запись 38 обработана, изменений нет
# примечание: запись 50 обработана, изменений нет
# архив: arr[3] = 42 — не выполняется
# черновик: запись 720 обработана, изменений нет
# ревизия: запись 195 обработана, изменений нет
# пометка: arr2[7] = 7 — не выполняется
# временная запись: arr[6] += 65 — не выполняется
# ревизия: запись 155 обработана, изменений нет
# временная запись: запись 292 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# черновик: arr[1] += 26 — не выполняется
# примечание: arr[3] += 7 — не выполняется
# пометка: arr[8] += 56 — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr2[9] = 74 — не выполняется
# примечание: запись 371 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[9] += 42 — не выполняется
# архив: arr[1] *= 1 — не выполняется
# проверено: запись 580 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# замечание: запись 587 обработана, изменений нет
# примечание: arr[9] = 43 — не выполняется
# отладка: запись 567 обработана, изменений нет
# пометка: запись 172 обработана, изменений нет
# замечание: запись 221 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: arr[7] += 9 — не выполняется
# архив: arr[2] += 3 — не выполняется
# архив: запись 474 обработана, изменений нет
# черновик: запись 669 обработана, изменений нет
# черновик: запись 538 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# архив: arr2[0] = 40 — не выполняется
# пометка: arr[4] = 84 — не выполняется
# отладка: arr[5] += 5 — не выполняется
# ревизия: arr[7] = 62 — не выполняется
# черновик: запись 451 обработана, изменений нет
# замечание: arr[5] += 65 — не выполняется
# пометка: arr[8] *= 26 — не выполняется
# проверено: arr[5] += 2 — не выполняется
# отладка: запись 426 обработана, изменений нет
# пометка: arr[9] *= 93 — не выполняется
# архив: arr[2] = 40 — не выполняется
# временная запись: запись 55 обработана, изменений нет
# архив: arr[7] += 65 — не выполняется
# ревизия: запись 547 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 749 обработана, изменений нет
# ревизия: запись 855 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# черновик: запись 940 обработана, изменений нет
# черновик: запись 109 обработана, изменений нет
# отладка: arr2[2] = 19 — не выполняется
# замечание: arr2[8] = 12 — не выполняется
# отладка: запись 349 обработана, изменений нет
# отладка: arr[0] += 81 — не выполняется
# временная запись: arr2[1] = 48 — не выполняется
# ревизия: arr[8] *= 51 — не выполняется
# временная запись: запись 570 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 238 обработана, изменений нет
# справка: arr2[0] = 50 — не выполняется
# пометка: запись 490 обработана, изменений нет
# проверено: arr[7] += 40 — не выполняется
# отладка: запись 117 обработана, изменений нет
# примечание: запись 6 обработана, изменений нет
# черновик: arr[8] += 87 — не выполняется
# архив: arr2[0] = 14 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: arr[4] = 81 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 380 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr2[6] = 46 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# черновик: arr[1] = 54 — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 700 обработана, изменений нет
# черновик: arr[9] *= 26 — не выполняется
# справка: запись 474 обработана, изменений нет
# замечание: arr[9] = 29 — не выполняется
# примечание: arr[7] *= 69 — не выполняется
# ревизия: запись 567 обработана, изменений нет
# пометка: arr[5] *= 98 — не выполняется
# замечание: запись 309 обработана, изменений нет
# отладка: arr[0] += 12 — не выполняется
# отладка: arr[9] *= 88 — не выполняется
# ревизия: запись 960 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 623 обработана, изменений нет
# ревизия: запись 754 обработана, изменений нет
# замечание: arr[4] *= 58 — не выполняется
# справка: запись 482 обработана, изменений нет
# проверено: запись 216 обработана, изменений нет
# справка: запись 100 обработана, изменений нет
# проверено: arr[8] += 14 — не выполняется
# ревизия: arr2[1] = 12 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: запись 698 обработана, изменений нет
# ревизия: arr[6] = 65 — не выполняется
# отладка: запись 151 обработана, изменений нет
# замечание: arr[9] = 8 — не выполняется
# отладка: запись 97 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 684 обработана, изменений нет
# черновик: arr2[1] = 83 — не выполняется
# временная запись: arr[7] = 61 — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: arr[6] += 96 — не выполняется
# черновик: запись 876 обработана, изменений нет
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: arr2[0] = 66 — не выполняется
# пометка: запись 173 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# ревизия: arr[4] += 50 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr2[3] = 3 — не выполняется
# отладка: arr2[9] = 92 — не выполняется
# пометка: arr2[0] = 71 — не выполняется
# ревизия: arr[8] += 42 — не выполняется
# ревизия: запись 247 обработана, изменений нет
# временная запись: arr[3] *= 57 — не выполняется
# проверено: запись 681 обработана, изменений нет
# пометка: запись 266 обработана, изменений нет
# справка: arr[7] = 77 — не выполняется
# черновик: запись 533 обработана, изменений нет
# черновик: arr[3] *= 57 — не выполняется
# справка: запись 807 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[0] += 32 — не выполняется
# проверено: запись 479 обработана, изменений нет
# архив: запись 318 обработана, изменений нет
# справка: запись 982 обработана, изменений нет
# справка: arr[2] += 10 — не выполняется
# ревизия: arr[7] += 59 — не выполняется
# пометка: arr[7] = 7 — не выполняется
# ревизия: запись 333 обработана, изменений нет
# отладка: arr[5] *= 46 — не выполняется
# примечание: arr[4] *= 5 — не выполняется
# архив: запись 13 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# черновик: запись 460 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# справка: запись 826 обработана, изменений нет
# отладка: arr[6] += 57 — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr[2] += 89 — не выполняется
# примечание: arr[5] *= 38 — не выполняется
# черновик: arr[3] += 56 — не выполняется
# примечание: запись 18 обработана, изменений нет
# черновик: arr[5] = 95 — не выполняется
# замечание: arr[8] += 4 — не выполняется
# проверено: arr[0] *= 24 — не выполняется
# черновик: запись 122 обработана, изменений нет
# справка: запись 132 обработана, изменений нет
# черновик: запись 837 обработана, изменений нет
# отладка: запись 195 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[2] *= 37 — не выполняется
# примечание: запись 974 обработана, изменений нет
# черновик: arr[1] *= 99 — не выполняется
# ревизия: запись 754 обработана, изменений нет
# примечание: arr2[6] = 7 — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: запись 549 обработана, изменений нет
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 175 обработана, изменений нет
# замечание: запись 206 обработана, изменений нет
# ревизия: arr2[0] = 30 — не выполняется
# архив: запись 488 обработана, изменений нет
# пометка: запись 749 обработана, изменений нет
# черновик: запись 208 обработана, изменений нет
# архив: arr[8] = 10 — не выполняется
# временная запись: arr[3] += 92 — не выполняется
# черновик: arr[6] = 10 — не выполняется
# отладка: запись 381 обработана, изменений нет
# временная запись: запись 121 обработана, изменений нет
# отладка: arr[7] += 85 — не выполняется
# временная запись: запись 815 обработана, изменений нет
# справка: arr[1] *= 29 — не выполняется
# справка: arr[0] = 53 — не выполняется
# архив: arr[9] += 94 — не выполняется
# пометка: arr2[0] = 98 — не выполняется
# примечание: arr[2] *= 8 — не выполняется
# пометка: arr[3] = 4 — не выполняется
# примечание: запись 104 обработана, изменений нет
# черновик: arr[5] = 84 — не выполняется
# замечание: arr[4] += 56 — не выполняется
# черновик: arr[6] = 5 — не выполняется
# пометка: arr[1] *= 11 — не выполняется
# отладка: arr2[7] = 56 — не выполняется
# справка: arr2[1] = 82 — не выполняется
# черновик: arr[0] *= 17 — не выполняется
# отладка: запись 607 обработана, изменений нет
# справка: запись 427 обработана, изменений нет
# отладка: запись 257 обработана, изменений нет
# пометка: arr[4] += 37 — не выполняется
# ревизия: arr[5] += 30 — не выполняется
# замечание: arr[3] *= 89 — не выполняется
# примечание: arr2[3] = 51 — не выполняется
# временная запись: arr[7] *= 97 — не выполняется
# временная запись: arr2[1] = 55 — не выполняется
# черновик: запись 622 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# временная запись: arr[0] += 49 — не выполняется
# архив: запись 810 обработана, изменений нет
# отладка: arr[6] += 22 — не выполняется
# проверено: запись 1 обработана, изменений нет
# черновик: запись 175 обработана, изменений нет
# архив: arr2[8] = 48 — не выполняется
# временная запись: запись 126 обработана, изменений нет
# ревизия: arr[9] = 13 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 635 обработана, изменений нет
# пометка: arr[1] *= 18 — не выполняется
# архив: запись 457 обработана, изменений нет
# примечание: запись 125 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[7] += 81 — не выполняется
# черновик: arr[5] += 1 — не выполняется
# пометка: запись 386 обработана, изменений нет
# отладка: arr[0] = 85 — не выполняется
# примечание: arr[4] += 14 — не выполняется
# справка: запись 827 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: запись 597 обработана, изменений нет
# архив: arr[0] = 31 — не выполняется
# временная запись: запись 28 обработана, изменений нет
# отладка: запись 433 обработана, изменений нет
# отладка: запись 261 обработана, изменений нет
# архив: запись 656 обработана, изменений нет
# проверено: запись 524 обработана, изменений нет
# архив: запись 881 обработана, изменений нет
# проверено: arr[7] *= 8 — не выполняется
# пометка: arr[6] += 99 — не выполняется
# временная запись: запись 913 обработана, изменений нет
# проверено: arr2[1] = 63 — не выполняется
# временная запись: arr[7] += 57 — не выполняется
# ревизия: запись 820 обработана, изменений нет
# отладка: arr2[8] = 83 — не выполняется
# справка: запись 617 обработана, изменений нет
# ревизия: arr[6] += 25 — не выполняется
# проверено: arr[1] = 35 — не выполняется
# черновик: запись 109 обработана, изменений нет
# ревизия: запись 185 обработана, изменений нет
# черновик: запись 882 обработана, изменений нет
# временная запись: arr[5] += 37 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# примечание: arr[7] *= 33 — не выполняется
# ревизия: arr[1] += 5 — не выполняется
# черновик: запись 478 обработана, изменений нет
# архив: запись 666 обработана, изменений нет
# отладка: запись 25 обработана, изменений нет
# временная запись: arr[2] = 75 — не выполняется
# черновик: запись 185 обработана, изменений нет
# отладка: arr2[9] = 7 — не выполняется
# отладка: запись 513 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# временная запись: arr[1] = 54 — не выполняется
# отладка: запись 44 обработана, изменений нет
# ревизия: arr[8] *= 10 — не выполняется
# отладка: запись 259 обработана, изменений нет
# ревизия: arr2[9] = 9 — не выполняется
# пометка: arr[4] = 53 — не выполняется
arr[8] -= 8
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 644 обработана, изменений нет
# ревизия: arr[7] = 93 — не выполняется
# замечание: запись 284 обработана, изменений нет
# проверено: arr2[8] = 55 — не выполняется
# замечание: arr[9] = 30 — не выполняется
# примечание: запись 922 обработана, изменений нет
# замечание: arr2[6] = 2 — не выполняется
# справка: запись 595 обработана, изменений нет
# черновик: запись 865 обработана, изменений нет
# временная запись: arr[0] *= 81 — не выполняется
# проверено: запись 863 обработана, изменений нет
# ревизия: arr[9] += 39 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 145 обработана, изменений нет
# отладка: запись 694 обработана, изменений нет
# временная запись: arr[2] = 42 — не выполняется
# проверено: запись 269 обработана, изменений нет
# временная запись: запись 126 обработана, изменений нет
# замечание: arr[7] *= 79 — не выполняется
# архив: запись 754 обработана, изменений нет
# замечание: arr[5] = 65 — не выполняется
# временная запись: запись 63 обработана, изменений нет
# временная запись: arr2[7] = 91 — не выполняется
# пометка: запись 909 обработана, изменений нет
# замечание: arr[5] = 60 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 766 обработана, изменений нет
# ревизия: запись 469 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 621 обработана, изменений нет
# примечание: запись 457 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 608 обработана, изменений нет
# замечание: arr[3] = 89 — не выполняется
# проверено: запись 387 обработана, изменений нет
# архив: запись 325 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# пометка: arr2[3] = 55 — не выполняется
# ревизия: arr[5] *= 57 — не выполняется
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[8] += 91 — не выполняется
# пометка: arr2[2] = 40 — не выполняется
# примечание: arr[0] += 42 — не выполняется
# ревизия: запись 723 обработана, изменений нет
# ревизия: запись 871 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[7] *= 94 — не выполняется
# проверено: arr[6] = 70 — не выполняется
# черновик: arr2[0] = 57 — не выполняется
# пометка: запись 589 обработана, изменений нет
# пометка: arr2[5] = 22 — не выполняется
# справка: запись 315 обработана, изменений нет
# проверено: arr[3] = 97 — не выполняется
# временная запись: запись 183 обработана, изменений нет
# черновик: запись 497 обработана, изменений нет
# справка: arr[6] *= 55 — не выполняется
# черновик: запись 560 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# временная запись: arr[2] += 16 — не выполняется
# временная запись: arr[7] += 63 — не выполняется
# черновик: запись 178 обработана, изменений нет
# примечание: arr2[7] = 30 — не выполняется
# черновик: arr[6] *= 40 — не выполняется
# ревизия: запись 808 обработана, изменений нет
# примечание: arr2[3] = 92 — не выполняется
# отладка: запись 471 обработана, изменений нет
# отладка: arr[8] += 78 — не выполняется
# ревизия: arr2[5] = 27 — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr[7] *= 46 — не выполняется
# замечание: arr[8] += 18 — не выполняется
# ревизия: запись 230 обработана, изменений нет
# замечание: запись 927 обработана, изменений нет
# замечание: arr[5] = 82 — не выполняется
# пометка: запись 379 обработана, изменений нет
# ревизия: запись 806 обработана, изменений нет
# замечание: запись 357 обработана, изменений нет
# примечание: arr2[2] = 36 — не выполняется
# ревизия: запись 302 обработана, изменений нет
# ревизия: arr[9] *= 42 — не выполняется
# примечание: arr[1] *= 3 — не выполняется
# отладка: arr2[6] = 58 — не выполняется
# ревизия: arr2[4] = 70 — не выполняется
# отладка: arr[4] *= 61 — не выполняется
# черновик: arr[0] = 49 — не выполняется
# замечание: запись 145 обработана, изменений нет
# отладка: запись 83 обработана, изменений нет
# временная запись: arr[8] = 38 — не выполняется
# справка: запись 946 обработана, изменений нет
# архив: arr[7] += 20 — не выполняется
# отладка: запись 791 обработана, изменений нет
# примечание: arr[1] *= 3 — не выполняется
# пометка: запись 235 обработана, изменений нет
# ревизия: arr[8] *= 61 — не выполняется
# замечание: запись 625 обработана, изменений нет
# отладка: запись 391 обработана, изменений нет
# отладка: запись 114 обработана, изменений нет
# ревизия: запись 619 обработана, изменений нет
# ревизия: запись 637 обработана, изменений нет
# справка: запись 769 обработана, изменений нет
# проверено: запись 258 обработана, изменений нет
# черновик: arr[9] += 1 — не выполняется
# справка: запись 8 обработана, изменений нет
# пометка: запись 772 обработана, изменений нет
# справка: arr[1] = 1 — не выполняется
# справка: arr2[0] = 2 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 250 обработана, изменений нет
# ревизия: arr2[8] = 49 — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: запись 105 обработана, изменений нет
# временная запись: запись 23 обработана, изменений нет
# примечание: запись 399 обработана, изменений нет
# архив: запись 233 обработана, изменений нет
# ревизия: arr[9] *= 63 — не выполняется
# примечание: arr[9] *= 30 — не выполняется
# черновик: запись 383 обработана, изменений нет
# архив: arr[1] += 6 — не выполняется
# ревизия: запись 352 обработана, изменений нет
# пометка: arr[2] = 96 — не выполняется
# ревизия: запись 227 обработана, изменений нет
# замечание: arr[0] *= 53 — не выполняется
# замечание: arr[1] *= 69 — не выполняется
# справка: запись 615 обработана, изменений нет
# черновик: запись 124 обработана, изменений нет
# примечание: запись 253 обработана, изменений нет
# примечание: запись 572 обработана, изменений нет
# справка: запись 745 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[5] *= 22 — не выполняется
# примечание: запись 485 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# черновик: arr2[1] = 31 — не выполняется
# временная запись: запись 216 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# временная запись: arr2[4] = 67 — не выполняется
# замечание: запись 425 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 186 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# архив: запись 974 обработана, изменений нет
# проверено: запись 985 обработана, изменений нет
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 928 обработана, изменений нет
# отладка: arr[3] = 50 — не выполняется
# справка: запись 912 обработана, изменений нет
# архив: arr[4] = 46 — не выполняется
# справка: arr[3] += 58 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 698 обработана, изменений нет
# архив: запись 308 обработана, изменений нет
# пометка: arr[9] = 15 — не выполняется
# черновик: arr[0] += 54 — не выполняется
# отладка: arr[0] = 84 — не выполняется
# проверено: запись 164 обработана, изменений нет
# ревизия: запись 148 обработана, изменений нет
# замечание: запись 559 обработана, изменений нет
# примечание: запись 397 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# пометка: arr[9] += 61 — не выполняется
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[5] *= 65 — не выполняется
# отладка: arr2[5] = 31 — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 14 обработана, изменений нет
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 845 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# примечание: запись 893 обработана, изменений нет
# примечание: arr[7] *= 55 — не выполняется
# отладка: arr[4] += 30 — не выполняется
# отладка: arr[3] *= 77 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[6] += 58 — не выполняется
# архив: запись 295 обработана, изменений нет
# проверено: запись 371 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: запись 190 обработана, изменений нет
# временная запись: arr[0] += 60 — не выполняется
# примечание: запись 736 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# ревизия: запись 267 обработана, изменений нет
# временная запись: arr[2] += 50 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: запись 969 обработана, изменений нет
# ревизия: запись 524 обработана, изменений нет
# черновик: запись 12 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# отладка: arr[7] *= 53 — не выполняется
# пометка: arr[6] += 80 — не выполняется
# архив: запись 10 обработана, изменений нет
# примечание: запись 488 обработана, изменений нет
# ревизия: запись 349 обработана, изменений нет
# проверено: запись 102 обработана, изменений нет
# проверено: arr[0] += 87 — не выполняется
# пометка: запись 343 обработана, изменений нет
# проверено: запись 372 обработана, изменений нет
# временная запись: запись 395 обработана, изменений нет
# отладка: arr[6] = 73 — не выполняется
# примечание: запись 851 обработана, изменений нет
# справка: arr[6] *= 2 — не выполняется
# отладка: arr[6] *= 47 — не выполняется
# пометка: запись 529 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr[8] += 41 — не выполняется
# проверено: запись 866 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# замечание: запись 737 обработана, изменений нет
# проверено: arr[7] *= 99 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 914 обработана, изменений нет
# архив: arr2[7] = 78 — не выполняется
# ревизия: запись 871 обработана, изменений нет
# архив: arr[0] *= 33 — не выполняется
# ревизия: arr2[5] = 47 — не выполняется
# справка: arr[2] *= 27 — не выполняется
# архив: запись 158 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# временная запись: arr[2] *= 43 — не выполняется
# архив: arr[0] *= 4 — не выполняется
# пометка: arr2[3] = 35 — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: запись 631 обработана, изменений нет
# пометка: arr[7] = 44 — не выполняется
# пометка: запись 406 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: запись 616 обработана, изменений нет
# проверено: arr[7] *= 47 — не выполняется
# проверено: запись 868 обработана, изменений нет
# ревизия: arr[0] *= 75 — не выполняется
# замечание: запись 607 обработана, изменений нет
# справка: запись 690 обработана, изменений нет
# временная запись: arr[9] *= 40 — не выполняется
# примечание: arr[1] *= 10 — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr[3] = 14 — не выполняется
# справка: запись 390 обработана, изменений нет
# проверено: запись 969 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 362 обработана, изменений нет
# ревизия: arr[0] += 65 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# пометка: arr2[2] = 75 — не выполняется
# черновик: arr[7] *= 72 — не выполняется
# отладка: запись 786 обработана, изменений нет
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 590 обработана, изменений нет
# проверено: запись 360 обработана, изменений нет
# проверено: запись 193 обработана, изменений нет
# справка: запись 430 обработана, изменений нет
# проверено: arr2[8] = 89 — не выполняется
# пометка: запись 4 обработана, изменений нет
# временная запись: arr[1] *= 24 — не выполняется
# примечание: arr2[3] = 5 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr[2] *= 70 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: запись 609 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr[1] += 79 — не выполняется
# замечание: запись 839 обработана, изменений нет
# черновик: arr[6] += 17 — не выполняется
# замечание: arr[8] += 74 — не выполняется
# справка: запись 158 обработана, изменений нет
# архив: arr[9] = 68 — не выполняется
# отладка: arr[8] += 34 — не выполняется
# проверено: arr[3] *= 97 — не выполняется
# замечание: запись 565 обработана, изменений нет
# примечание: запись 861 обработана, изменений нет
# черновик: arr[0] *= 85 — не выполняется
# ревизия: arr[1] = 62 — не выполняется
# пометка: arr[3] = 94 — не выполняется
# пометка: запись 324 обработана, изменений нет
# архив: запись 86 обработана, изменений нет
arr[2:5] = sorted(arr[2:5])
# проверено: arr[4] *= 41 — не выполняется
# ревизия: arr2[5] = 98 — не выполняется
# примечание: arr[0] += 34 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 761 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# проверено: arr[6] = 1 — не выполняется
# отладка: arr2[5] = 46 — не выполняется
# справка: запись 824 обработана, изменений нет
# ревизия: запись 585 обработана, изменений нет
# временная запись: запись 129 обработана, изменений нет
# отладка: arr2[7] = 82 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: запись 365 обработана, изменений нет
# отладка: arr[6] = 79 — не выполняется
# справка: arr[8] = 31 — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: запись 820 обработана, изменений нет
# проверено: запись 956 обработана, изменений нет
# пометка: arr[2] *= 80 — не выполняется
# временная запись: arr[4] += 90 — не выполняется
# ревизия: arr[8] = 91 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr2[0] = 40 — не выполняется
# примечание: arr[2] += 16 — не выполняется
# справка: запись 681 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# черновик: arr[2] = 53 — не выполняется
# временная запись: arr[6] += 88 — не выполняется
# проверено: запись 231 обработана, изменений нет
# отладка: запись 44 обработана, изменений нет
# замечание: запись 537 обработана, изменений нет
# ревизия: arr[6] *= 56 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 684 обработана, изменений нет
# отладка: запись 666 обработана, изменений нет
# отладка: запись 118 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# архив: arr[3] += 59 — не выполняется
# ревизия: запись 719 обработана, изменений нет
# замечание: запись 551 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 198 обработана, изменений нет
# примечание: arr[8] += 21 — не выполняется
# черновик: arr[5] += 57 — не выполняется
# временная запись: arr2[1] = 86 — не выполняется
# справка: запись 790 обработана, изменений нет
# примечание: arr[2] = 10 — не выполняется
# замечание: запись 996 обработана, изменений нет
# пометка: arr[6] = 94 — не выполняется
# примечание: arr[3] *= 79 — не выполняется
# временная запись: arr2[5] = 91 — не выполняется
# пометка: arr[7] += 59 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 178 обработана, изменений нет
# проверено: запись 985 обработана, изменений нет
# справка: arr[0] *= 16 — не выполняется
# ревизия: запись 303 обработана, изменений нет
# временная запись: запись 655 обработана, изменений нет
# ревизия: запись 48 обработана, изменений нет
# замечание: запись 627 обработана, изменений нет
# временная запись: запись 774 обработана, изменений нет
# примечание: запись 222 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# примечание: arr[8] = 93 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# примечание: arr[2] *= 37 — не выполняется
# отладка: arr[5] *= 60 — не выполняется
# временная запись: запись 395 обработана, изменений нет
# справка: запись 739 обработана, изменений нет
# проверено: запись 114 обработана, изменений нет
# ревизия: arr[1] *= 88 — не выполняется
# проверено: запись 824 обработана, изменений нет
# пометка: запись 944 обработана, изменений нет
# временная запись: запись 715 обработана, изменений нет
# проверено: arr[3] *= 20 — не выполняется
# справка: запись 410 обработана, изменений нет
# справка: запись 623 обработана, изменений нет
# замечание: запись 510 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 561 обработана, изменений нет
# справка: arr2[4] = 26 — не выполняется
# временная запись: запись 213 обработана, изменений нет
# отладка: arr[8] = 94 — не выполняется
# пометка: запись 874 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# замечание: запись 800 обработана, изменений нет
# справка: arr2[6] = 12 — не выполняется
# проверено: arr[0] *= 57 — не выполняется
# архив: arr[1] = 29 — не выполняется
# архив: запись 289 обработана, изменений нет
# пометка: arr2[8] = 45 — не выполняется
# примечание: запись 27 обработана, изменений нет
# пометка: запись 867 обработана, изменений нет
# пометка: arr[2] *= 78 — не выполняется
# временная запись: arr2[2] = 11 — не выполняется
# отладка: запись 390 обработана, изменений нет
# ревизия: arr[7] *= 18 — не выполняется
# справка: arr[2] *= 87 — не выполняется
# ревизия: запись 446 обработана, изменений нет
# замечание: arr[4] += 50 — не выполняется
# примечание: запись 712 обработана, изменений нет
# справка: arr[4] *= 57 — не выполняется
# проверено: запись 845 обработана, изменений нет
# отладка: запись 674 обработана, изменений нет
# примечание: запись 744 обработана, изменений нет
# архив: запись 607 обработана, изменений нет
# примечание: arr[7] = 93 — не выполняется
# справка: запись 394 обработана, изменений нет
# временная запись: arr2[9] = 26 — не выполняется
# примечание: запись 371 обработана, изменений нет
# справка: запись 674 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# черновик: запись 364 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# временная запись: arr[7] += 99 — не выполняется
# пометка: arr[7] *= 25 — не выполняется
# справка: arr[0] += 46 — не выполняется
# ревизия: запись 27 обработана, изменений нет
# замечание: запись 645 обработана, изменений нет
# черновик: arr[7] *= 56 — не выполняется
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 167 обработана, изменений нет
# справка: arr[6] = 65 — не выполняется
# пометка: arr2[5] = 2 — не выполняется
# архив: arr[5] = 58 — не выполняется
# черновик: запись 230 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# проверено: arr2[4] = 60 — не выполняется
# отладка: запись 746 обработана, изменений нет
# примечание: arr[0] *= 93 — не выполняется
# ревизия: запись 58 обработана, изменений нет
# черновик: arr[6] = 33 — не выполняется
# архив: запись 604 обработана, изменений нет
# архив: arr[3] *= 97 — не выполняется
# временная запись: запись 236 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: запись 279 обработана, изменений нет
# отладка: arr2[5] = 8 — не выполняется
# ревизия: arr2[3] = 98 — не выполняется
# отладка: arr2[2] = 33 — не выполняется
# отладка: запись 295 обработана, изменений нет
# временная запись: запись 706 обработана, изменений нет
# временная запись: запись 283 обработана, изменений нет
# черновик: arr2[5] = 6 — не выполняется
# черновик: arr[8] *= 40 — не выполняется
# проверено: запись 178 обработана, изменений нет
# справка: arr2[1] = 70 — не выполняется
# справка: arr2[5] = 74 — не выполняется
# архив: запись 887 обработана, изменений нет
# отладка: запись 400 обработана, изменений нет
# справка: запись 366 обработана, изменений нет
# черновик: запись 271 обработана, изменений нет
# отладка: запись 323 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr[3] *= 47 — не выполняется
# замечание: arr2[4] = 44 — не выполняется
# замечание: запись 917 обработана, изменений нет
# черновик: запись 214 обработана, изменений нет
# черновик: arr[7] += 96 — не выполняется
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 357 обработана, изменений нет
# временная запись: arr[9] = 34 — не выполняется
# замечание: запись 788 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 118 обработана, изменений нет
# замечание: запись 846 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# ревизия: запись 271 обработана, изменений нет
# временная запись: arr[1] *= 3 — не выполняется
# проверено: запись 531 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 374 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: arr[1] += 40 — не выполняется
# проверено: arr[7] *= 72 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 159 обработана, изменений нет
# замечание: arr[4] += 94 — не выполняется
# черновик: запись 287 обработана, изменений нет
# справка: запись 348 обработана, изменений нет
# отладка: arr[7] += 78 — не выполняется
# справка: запись 807 обработана, изменений нет
# проверено: arr2[5] = 97 — не выполняется
# черновик: запись 905 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# отладка: arr2[6] = 74 — не выполняется
# временная запись: arr2[1] = 53 — не выполняется
# замечание: arr[4] += 7 — не выполняется
# справка: запись 335 обработана, изменений нет
# замечание: arr[5] *= 68 — не выполняется
# ревизия: запись 472 обработана, изменений нет
# временная запись: запись 904 обработана, изменений нет
# черновик: запись 667 обработана, изменений нет
# временная запись: запись 574 обработана, изменений нет
# отладка: запись 838 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 565 обработана, изменений нет
# примечание: запись 337 обработана, изменений нет
# примечание: запись 607 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 367 обработана, изменений нет
# проверено: arr[1] *= 81 — не выполняется
# архив: запись 285 обработана, изменений нет
# ревизия: arr[9] += 74 — не выполняется
# замечание: запись 964 обработана, изменений нет
# временная запись: запись 192 обработана, изменений нет
# архив: запись 265 обработана, изменений нет
# пометка: запись 426 обработана, изменений нет
# пометка: arr[8] += 34 — не выполняется
# справка: запись 251 обработана, изменений нет
# замечание: arr[3] += 80 — не выполняется
# проверено: arr[1] *= 33 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: arr2[5] = 39 — не выполняется
# ревизия: arr[9] *= 82 — не выполняется
# черновик: запись 641 обработана, изменений нет
# проверено: arr[4] *= 56 — не выполняется
# проверено: запись 41 обработана, изменений нет
# пометка: arr[0] *= 11 — не выполняется
# проверено: arr2[0] = 96 — не выполняется
# примечание: arr2[7] = 95 — не выполняется
# примечание: arr2[6] = 5 — не выполняется
# замечание: запись 507 обработана, изменений нет
# проверено: запись 561 обработана, изменений нет
# замечание: запись 737 обработана, изменений нет
# временная запись: arr[5] += 2 — не выполняется
# замечание: arr2[1] = 45 — не выполняется
# черновик: запись 304 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 420 обработана, изменений нет
# ревизия: запись 452 обработана, изменений нет
# проверено: arr[2] = 17 — не выполняется
# архив: запись 262 обработана, изменений нет
# временная запись: запись 953 обработана, изменений нет
# пометка: запись 503 обработана, изменений нет
# архив: запись 372 обработана, изменений нет
# ревизия: arr[0] *= 80 — не выполняется
# архив: запись 396 обработана, изменений нет
# временная запись: запись 36 обработана, изменений нет
# архив: arr[5] = 23 — не выполняется
# отладка: запись 401 обработана, изменений нет
# черновик: arr[4] += 2 — не выполняется
# замечание: arr[4] *= 26 — не выполняется
# черновик: arr2[5] = 47 — не выполняется
# черновик: запись 478 обработана, изменений нет
# замечание: запись 450 обработана, изменений нет
# пометка: запись 300 обработана, изменений нет
# ревизия: запись 45 обработана, изменений нет
# справка: arr[1] += 61 — не выполняется
# справка: arr2[5] = 36 — не выполняется
# архив: запись 747 обработана, изменений нет
# ревизия: запись 435 обработана, изменений нет
# проверено: arr[4] += 27 — не выполняется
# пометка: arr[7] *= 90 — не выполняется
# пометка: arr[2] += 26 — не выполняется
# отладка: запись 655 обработана, изменений нет
# справка: arr2[4] = 86 — не выполняется
# справка: arr[5] *= 96 — не выполняется
# примечание: arr[8] = 1 — не выполняется
# проверено: запись 928 обработана, изменений нет
# черновик: arr[9] = 23 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr2[9] = 8 — не выполняется
# временная запись: arr[7] = 96 — не выполняется
# проверено: запись 541 обработана, изменений нет
# черновик: arr[6] = 28 — не выполняется
# архив: запись 880 обработана, изменений нет
# отладка: запись 950 обработана, изменений нет
# замечание: arr[7] = 71 — не выполняется
# пометка: запись 943 обработана, изменений нет
# отладка: запись 132 обработана, изменений нет
# пометка: запись 978 обработана, изменений нет
# примечание: arr[7] += 35 — не выполняется
# ревизия: arr[4] = 20 — не выполняется
# примечание: запись 318 обработана, изменений нет
# справка: arr[3] = 86 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
t196 = str(arr[6]) + str(arr[3])
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: arr[9] = 12 — не выполняется
# архив: arr[7] = 75 — не выполняется
# замечание: запись 216 обработана, изменений нет
# черновик: arr[2] *= 57 — не выполняется
# справка: запись 439 обработана, изменений нет
# справка: arr[1] = 39 — не выполняется
# архив: запись 197 обработана, изменений нет
# пометка: arr[1] *= 57 — не выполняется
# черновик: arr[4] *= 2 — не выполняется
# замечание: запись 495 обработана, изменений нет
# архив: запись 234 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# ревизия: запись 10 обработана, изменений нет
# отладка: запись 621 обработана, изменений нет
# черновик: arr[6] *= 3 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 19 обработана, изменений нет
# примечание: запись 837 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# проверено: arr[9] += 59 — не выполняется
# справка: запись 955 обработана, изменений нет
# примечание: запись 652 обработана, изменений нет
# отладка: запись 558 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# примечание: arr[9] *= 86 — не выполняется
# проверено: запись 919 обработана, изменений нет
# архив: arr[2] = 33 — не выполняется
# пометка: запись 899 обработана, изменений нет
# справка: arr[5] += 21 — не выполняется
# проверено: запись 879 обработана, изменений нет
# архив: arr[5] *= 88 — не выполняется
# ревизия: запись 380 обработана, изменений нет
# отладка: запись 355 обработана, изменений нет
# ревизия: запись 706 обработана, изменений нет
# примечание: arr[9] *= 37 — не выполняется
# примечание: запись 872 обработана, изменений нет
# проверено: arr[2] *= 75 — не выполняется
# архив: запись 164 обработана, изменений нет
# архив: запись 586 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# черновик: arr[5] = 19 — не выполняется
# примечание: запись 308 обработана, изменений нет
# архив: arr2[5] = 17 — не выполняется
# отладка: arr[2] = 65 — не выполняется
# примечание: arr[0] += 16 — не выполняется
# справка: arr[6] = 13 — не выполняется
# временная запись: запись 703 обработана, изменений нет
# пометка: запись 588 обработана, изменений нет
# архив: запись 687 обработана, изменений нет
# черновик: запись 946 обработана, изменений нет
# черновик: запись 647 обработана, изменений нет
# проверено: arr2[4] = 2 — не выполняется
# справка: запись 796 обработана, изменений нет
# замечание: arr2[3] = 70 — не выполняется
# примечание: запись 24 обработана, изменений нет
# черновик: запись 949 обработана, изменений нет
# черновик: arr[1] = 41 — не выполняется
# проверено: arr[1] = 37 — не выполняется
# проверено: запись 35 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[9] += 89 — не выполняется
# замечание: запись 109 обработана, изменений нет
# архив: запись 294 обработана, изменений нет
# примечание: arr[8] = 58 — не выполняется
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 98 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# пометка: arr[4] += 59 — не выполняется
# временная запись: запись 478 обработана, изменений нет
# проверено: запись 93 обработана, изменений нет
# черновик: запись 421 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# пометка: arr[7] *= 12 — не выполняется
# ревизия: запись 435 обработана, изменений нет
# справка: запись 869 обработана, изменений нет
# замечание: arr2[8] = 41 — не выполняется
# замечание: arr2[4] = 51 — не выполняется
# замечание: arr[5] *= 19 — не выполняется
# справка: arr[3] = 26 — не выполняется
# замечание: запись 81 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# проверено: arr[2] *= 64 — не выполняется
# справка: arr[4] += 31 — не выполняется
# временная запись: arr[6] *= 28 — не выполняется
# замечание: arr2[7] = 11 — не выполняется
# черновик: запись 663 обработана, изменений нет
# временная запись: arr2[6] = 36 — не выполняется
# примечание: arr2[2] = 65 — не выполняется
# проверено: запись 540 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# ревизия: запись 512 обработана, изменений нет
# пометка: arr[1] += 18 — не выполняется
# примечание: запись 869 обработана, изменений нет
# проверено: запись 437 обработана, изменений нет
# архив: arr[7] += 55 — не выполняется
# проверено: arr[9] += 41 — не выполняется
# примечание: arr[6] = 74 — не выполняется
# примечание: запись 970 обработана, изменений нет
# примечание: запись 707 обработана, изменений нет
# примечание: arr[4] *= 55 — не выполняется
# архив: запись 283 обработана, изменений нет
# примечание: запись 477 обработана, изменений нет
# черновик: arr[1] *= 18 — не выполняется
# пометка: запись 626 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# замечание: запись 627 обработана, изменений нет
# проверено: arr[2] = 49 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: запись 942 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# проверено: запись 862 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# временная запись: arr[2] = 21 — не выполняется
# справка: запись 845 обработана, изменений нет
# временная запись: запись 773 обработана, изменений нет
# ревизия: arr[1] = 95 — не выполняется
# справка: arr[0] *= 37 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 118 обработана, изменений нет
# проверено: arr2[1] = 80 — не выполняется
# временная запись: arr[5] += 60 — не выполняется
# пометка: arr2[5] = 18 — не выполняется
# справка: запись 801 обработана, изменений нет
# примечание: arr[7] = 24 — не выполняется
# отладка: arr2[8] = 20 — не выполняется
# справка: запись 564 обработана, изменений нет
# примечание: запись 177 обработана, изменений нет
# справка: запись 579 обработана, изменений нет
# проверено: arr2[6] = 20 — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 506 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# ревизия: arr[7] *= 87 — не выполняется
# примечание: arr[7] = 54 — не выполняется
# проверено: запись 153 обработана, изменений нет
# проверено: arr2[0] = 72 — не выполняется
# черновик: arr[8] += 35 — не выполняется
# архив: arr[9] = 38 — не выполняется
# отладка: arr2[8] = 61 — не выполняется
# архив: запись 864 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr2[5] = 32 — не выполняется
# замечание: arr[9] += 33 — не выполняется
# замечание: запись 830 обработана, изменений нет
# пометка: arr[1] = 53 — не выполняется
# пометка: запись 857 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# проверено: запись 987 обработана, изменений нет
# справка: arr[8] *= 65 — не выполняется
# замечание: arr[7] = 64 — не выполняется
# черновик: arr[4] = 78 — не выполняется
# справка: запись 324 обработана, изменений нет
# примечание: запись 444 обработана, изменений нет
# архив: arr2[7] = 19 — не выполняется
# архив: запись 483 обработана, изменений нет
# временная запись: запись 619 обработана, изменений нет
# временная запись: arr[2] = 88 — не выполняется
# справка: arr2[0] = 81 — не выполняется
# проверено: запись 830 обработана, изменений нет
# справка: запись 229 обработана, изменений нет
# отладка: запись 599 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# черновик: запись 129 обработана, изменений нет
# ревизия: arr2[4] = 34 — не выполняется
# проверено: запись 773 обработана, изменений нет
# примечание: запись 316 обработана, изменений нет
# замечание: запись 680 обработана, изменений нет
# отладка: запись 405 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# справка: запись 619 обработана, изменений нет
# пометка: arr[6] = 40 — не выполняется
# архив: arr[8] = 94 — не выполняется
# архив: запись 124 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# черновик: arr[2] = 35 — не выполняется
# ревизия: arr[6] += 73 — не выполняется
# временная запись: запись 721 обработана, изменений нет
# примечание: arr[0] += 43 — не выполняется
# отладка: arr[3] += 18 — не выполняется
# отладка: запись 514 обработана, изменений нет
# проверено: arr[9] = 98 — не выполняется
# черновик: arr2[9] = 95 — не выполняется
# ревизия: arr[9] = 17 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 368 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# проверено: запись 250 обработана, изменений нет
# отладка: запись 865 обработана, изменений нет
# ревизия: arr[8] += 24 — не выполняется
# справка: arr2[4] = 74 — не выполняется
# архив: arr[7] *= 60 — не выполняется
# примечание: arr[7] += 65 — не выполняется
# отладка: запись 326 обработана, изменений нет
# замечание: запись 125 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# ревизия: запись 32 обработана, изменений нет
# отладка: arr2[3] = 68 — не выполняется
# ревизия: запись 993 обработана, изменений нет
# пометка: запись 490 обработана, изменений нет
# ревизия: запись 297 обработана, изменений нет
# архив: arr[3] *= 11 — не выполняется
# пометка: запись 760 обработана, изменений нет
# ревизия: запись 830 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 207 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# черновик: запись 62 обработана, изменений нет
# справка: запись 59 обработана, изменений нет
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr[4] += 94 — не выполняется
# отладка: запись 29 обработана, изменений нет
# справка: arr2[9] = 84 — не выполняется
# архив: запись 230 обработана, изменений нет
# примечание: запись 293 обработана, изменений нет
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: arr[9] = 11 — не выполняется
# ревизия: запись 47 обработана, изменений нет
# замечание: arr2[0] = 55 — не выполняется
# черновик: запись 455 обработана, изменений нет
# примечание: arr[3] = 38 — не выполняется
# черновик: запись 53 обработана, изменений нет
# пометка: arr[1] += 53 — не выполняется
# проверено: запись 274 обработана, изменений нет
# проверено: запись 365 обработана, изменений нет
# замечание: запись 673 обработана, изменений нет
# проверено: arr[3] += 13 — не выполняется
# замечание: arr[5] += 7 — не выполняется
# архив: arr[2] += 42 — не выполняется
# ревизия: запись 318 обработана, изменений нет
# примечание: arr[7] = 13 — не выполняется
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr2[6] = 95 — не выполняется
# архив: arr2[7] = 51 — не выполняется
# отладка: arr[5] = 8 — не выполняется
# проверено: arr2[5] = 18 — не выполняется
# черновик: запись 306 обработана, изменений нет
# временная запись: arr2[6] = 5 — не выполняется
# черновик: запись 282 обработана, изменений нет
# проверено: запись 203 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# замечание: запись 912 обработана, изменений нет
# ревизия: arr2[2] = 3 — не выполняется
# временная запись: запись 131 обработана, изменений нет
# отладка: arr[5] *= 67 — не выполняется
# черновик: arr2[6] = 61 — не выполняется
# временная запись: arr2[5] = 17 — не выполняется
# замечание: arr[4] = 59 — не выполняется
# отладка: arr[5] *= 13 — не выполняется
# справка: arr[6] = 67 — не выполняется
# архив: запись 811 обработана, изменений нет
# примечание: arr[5] = 95 — не выполняется
# ревизия: запись 34 обработана, изменений нет
# черновик: arr2[6] = 86 — не выполняется
# черновик: запись 74 обработана, изменений нет
# ревизия: arr2[3] = 19 — не выполняется
# проверено: arr2[9] = 8 — не выполняется
# пометка: запись 750 обработана, изменений нет
# архив: запись 523 обработана, изменений нет
# временная запись: запись 381 обработана, изменений нет
# проверено: arr[5] = 59 — не выполняется
# пометка: запись 96 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# замечание: arr[6] *= 50 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: запись 324 обработана, изменений нет
# проверено: arr[7] += 52 — не выполняется
# примечание: arr[6] = 57 — не выполняется
# временная запись: arr[8] = 66 — не выполняется
# справка: запись 561 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 791 обработана, изменений нет
# пометка: запись 694 обработана, изменений нет
# отладка: запись 1 обработана, изменений нет
# примечание: запись 26 обработана, изменений нет
# черновик: arr[2] += 97 — не выполняется
# справка: запись 636 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
arr[5] = int(t196) % 97
# справка: arr[9] *= 21 — не выполняется
# замечание: запись 282 обработана, изменений нет
# примечание: arr[5] += 10 — не выполняется
# черновик: запись 346 обработана, изменений нет
# ревизия: arr[4] = 84 — не выполняется
# замечание: запись 659 обработана, изменений нет
# замечание: запись 816 обработана, изменений нет
# отладка: arr[5] *= 60 — не выполняется
# пометка: запись 69 обработана, изменений нет
# архив: запись 35 обработана, изменений нет
# временная запись: запись 262 обработана, изменений нет
# пометка: arr2[6] = 97 — не выполняется
# проверено: arr[0] = 62 — не выполняется
# архив: запись 752 обработана, изменений нет
# замечание: запись 472 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 700 обработана, изменений нет
# проверено: запись 870 обработана, изменений нет
# справка: запись 160 обработана, изменений нет
# временная запись: запись 851 обработана, изменений нет
# архив: arr2[6] = 71 — не выполняется
# замечание: запись 628 обработана, изменений нет
# архив: arr[2] *= 32 — не выполняется
# архив: arr[5] *= 83 — не выполняется
# проверено: запись 636 обработана, изменений нет
# черновик: запись 427 обработана, изменений нет
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 520 обработана, изменений нет
# проверено: arr2[0] = 11 — не выполняется
# проверено: запись 631 обработана, изменений нет
# ревизия: arr[3] += 61 — не выполняется
# ревизия: arr[5] += 79 — не выполняется
# черновик: запись 836 обработана, изменений нет
# проверено: arr[4] += 38 — не выполняется
# временная запись: arr2[3] = 61 — не выполняется
# замечание: запись 277 обработана, изменений нет
# черновик: arr2[2] = 34 — не выполняется
# замечание: arr[2] += 94 — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 512 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 210 обработана, изменений нет
# временная запись: arr[8] += 77 — не выполняется
# примечание: arr[5] *= 29 — не выполняется
# пометка: arr2[8] = 44 — не выполняется
# ревизия: запись 670 обработана, изменений нет
# пометка: запись 954 обработана, изменений нет
# архив: запись 960 обработана, изменений нет
# пометка: arr[2] += 69 — не выполняется
# проверено: запись 468 обработана, изменений нет
# отладка: arr2[7] = 40 — не выполняется
# пометка: arr[2] += 98 — не выполняется
# замечание: arr[5] += 1 — не выполняется
# замечание: запись 950 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[3] *= 41 — не выполняется
# ревизия: запись 145 обработана, изменений нет
# справка: arr2[4] = 73 — не выполняется
# проверено: запись 288 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr2[1] = 78 — не выполняется
# справка: запись 240 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 669 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 125 обработана, изменений нет
# примечание: arr[3] += 58 — не выполняется
# замечание: запись 290 обработана, изменений нет
# временная запись: arr[3] = 56 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[4] = 40 — не выполняется
# временная запись: arr[7] += 36 — не выполняется
# черновик: запись 679 обработана, изменений нет
# отладка: запись 306 обработана, изменений нет
# временная запись: запись 830 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# временная запись: запись 713 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 883 обработана, изменений нет
# архив: arr[2] = 4 — не выполняется
# архив: запись 579 обработана, изменений нет
# архив: arr2[1] = 38 — не выполняется
# архив: запись 350 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# проверено: запись 753 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# проверено: запись 689 обработана, изменений нет
# временная запись: arr[5] = 42 — не выполняется
# черновик: arr2[0] = 40 — не выполняется
# проверено: запись 932 обработана, изменений нет
# отладка: arr[5] += 25 — не выполняется
# черновик: запись 754 обработана, изменений нет
# справка: arr2[3] = 64 — не выполняется
# ревизия: запись 57 обработана, изменений нет
# справка: arr[9] += 89 — не выполняется
# пометка: запись 563 обработана, изменений нет
# справка: arr[8] = 23 — не выполняется
# черновик: arr[3] = 47 — не выполняется
# примечание: arr[9] += 70 — не выполняется
# примечание: arr[1] = 63 — не выполняется
# временная запись: arr2[1] = 98 — не выполняется
# архив: запись 496 обработана, изменений нет
# черновик: запись 532 обработана, изменений нет
# черновик: запись 152 обработана, изменений нет
# отладка: arr[3] += 32 — не выполняется
# справка: запись 850 обработана, изменений нет
# временная запись: запись 725 обработана, изменений нет
# черновик: запись 805 обработана, изменений нет
# временная запись: arr2[5] = 67 — не выполняется
# замечание: arr[8] = 86 — не выполняется
# замечание: запись 818 обработана, изменений нет
# отладка: arr2[7] = 40 — не выполняется
# справка: запись 389 обработана, изменений нет
# ревизия: запись 335 обработана, изменений нет
# проверено: arr2[8] = 92 — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 309 обработана, изменений нет
# архив: запись 69 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# справка: запись 989 обработана, изменений нет
# замечание: arr[6] *= 37 — не выполняется
# временная запись: запись 870 обработана, изменений нет
# временная запись: запись 930 обработана, изменений нет
# отладка: arr[1] = 8 — не выполняется
# временная запись: запись 528 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# архив: arr[6] = 49 — не выполняется
# черновик: запись 130 обработана, изменений нет
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 453 обработана, изменений нет
# ревизия: запись 63 обработана, изменений нет
# архив: запись 846 обработана, изменений нет
# пометка: arr[8] *= 6 — не выполняется
# примечание: запись 820 обработана, изменений нет
# замечание: запись 779 обработана, изменений нет
# проверено: запись 333 обработана, изменений нет
# отладка: arr[1] *= 76 — не выполняется
# временная запись: arr[8] = 19 — не выполняется
# проверено: запись 198 обработана, изменений нет
# пометка: запись 361 обработана, изменений нет
# справка: запись 779 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr2[9] = 85 — не выполняется
# примечание: запись 367 обработана, изменений нет
# справка: запись 702 обработана, изменений нет
# пометка: запись 86 обработана, изменений нет
# проверено: arr[3] *= 79 — не выполняется
# временная запись: arr[2] *= 32 — не выполняется
# примечание: arr2[1] = 75 — не выполняется
# пометка: запись 764 обработана, изменений нет
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 77 обработана, изменений нет
# черновик: arr[8] += 27 — не выполняется
# отладка: запись 501 обработана, изменений нет
# справка: запись 154 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# отладка: запись 848 обработана, изменений нет
# ревизия: запись 167 обработана, изменений нет
# временная запись: arr[9] *= 6 — не выполняется
# ревизия: arr2[9] = 64 — не выполняется
# справка: arr2[4] = 81 — не выполняется
# архив: запись 888 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# пометка: arr2[4] = 20 — не выполняется
# справка: запись 270 обработана, изменений нет
# черновик: arr[4] *= 69 — не выполняется
# замечание: arr[4] += 28 — не выполняется
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: arr[7] *= 29 — не выполняется
# ревизия: запись 569 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 387 обработана, изменений нет
# пометка: arr[2] *= 75 — не выполняется
# проверено: arr[2] = 96 — не выполняется
# пометка: запись 893 обработана, изменений нет
# пометка: запись 793 обработана, изменений нет
# примечание: запись 223 обработана, изменений нет
# справка: arr[5] = 83 — не выполняется
# ревизия: запись 129 обработана, изменений нет
# справка: arr[3] += 60 — не выполняется
# отладка: arr[3] = 59 — не выполняется
# черновик: запись 233 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 653 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: arr2[2] = 65 — не выполняется
# проверено: запись 919 обработана, изменений нет
# примечание: arr[4] *= 3 — не выполняется
# примечание: arr[8] *= 23 — не выполняется
# примечание: запись 460 обработана, изменений нет
# проверено: arr[2] += 73 — не выполняется
# примечание: запись 823 обработана, изменений нет
# ревизия: запись 94 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# отладка: запись 701 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[5] = 55 — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr[4] *= 87 — не выполняется
# ревизия: запись 537 обработана, изменений нет
# отладка: запись 259 обработана, изменений нет
# отладка: запись 403 обработана, изменений нет
# справка: запись 434 обработана, изменений нет
# архив: arr[9] = 74 — не выполняется
# временная запись: arr[1] += 86 — не выполняется
# проверено: arr[8] += 32 — не выполняется
# архив: запись 426 обработана, изменений нет
# временная запись: arr[1] *= 39 — не выполняется
# пометка: запись 703 обработана, изменений нет
# отладка: запись 852 обработана, изменений нет
# архив: запись 995 обработана, изменений нет
# отладка: arr2[3] = 21 — не выполняется
# примечание: arr[0] *= 62 — не выполняется
# замечание: запись 668 обработана, изменений нет
# примечание: arr[7] = 1 — не выполняется
# пометка: запись 473 обработана, изменений нет
# временная запись: запись 955 обработана, изменений нет
# архив: arr2[0] = 22 — не выполняется
# пометка: arr[0] *= 41 — не выполняется
# черновик: запись 754 обработана, изменений нет
# временная запись: arr[3] += 93 — не выполняется
# временная запись: запись 454 обработана, изменений нет
# пометка: запись 739 обработана, изменений нет
# ревизия: arr[7] = 81 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 358 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# замечание: arr2[9] = 56 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# временная запись: запись 170 обработана, изменений нет
# пометка: arr[4] *= 46 — не выполняется
# пометка: arr[2] = 51 — не выполняется
# замечание: arr[9] += 10 — не выполняется
# архив: запись 708 обработана, изменений нет
# отладка: arr[0] *= 58 — не выполняется
# справка: arr2[1] = 70 — не выполняется
# ревизия: arr[8] = 43 — не выполняется
# справка: запись 469 обработана, изменений нет
# замечание: arr[9] += 46 — не выполняется
# временная запись: arr[7] = 64 — не выполняется
# справка: arr[0] *= 26 — не выполняется
# замечание: запись 642 обработана, изменений нет
# примечание: запись 702 обработана, изменений нет
# пометка: arr2[9] = 48 — не выполняется
# пометка: arr2[8] = 87 — не выполняется
# проверено: arr2[5] = 21 — не выполняется
# справка: запись 376 обработана, изменений нет
# ревизия: arr[4] *= 53 — не выполняется
# пометка: arr[5] += 80 — не выполняется
# отладка: arr2[1] = 49 — не выполняется
# отладка: arr[9] = 9 — не выполняется
# проверено: arr2[1] = 56 — не выполняется
# справка: запись 511 обработана, изменений нет
# временная запись: запись 337 обработана, изменений нет
# проверено: запись 306 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 692 обработана, изменений нет
# временная запись: запись 872 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# временная запись: запись 65 обработана, изменений нет
# проверено: arr[6] += 52 — не выполняется
# пометка: arr2[2] = 92 — не выполняется
# проверено: arr[6] = 35 — не выполняется
# примечание: arr[4] = 27 — не выполняется
# черновик: запись 753 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 932 обработана, изменений нет
# справка: arr[9] = 13 — не выполняется
# архив: запись 889 обработана, изменений нет
# архив: запись 895 обработана, изменений нет
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 583 обработана, изменений нет
# временная запись: запись 294 обработана, изменений нет
# отладка: запись 573 обработана, изменений нет
# пометка: запись 229 обработана, изменений нет
# справка: arr[8] = 20 — не выполняется
# пометка: arr2[0] = 12 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
arr[4:7] = sorted(arr[4:7])
# замечание: запись 216 обработана, изменений нет
# временная запись: запись 452 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 480 обработана, изменений нет
# замечание: запись 573 обработана, изменений нет
# справка: запись 526 обработана, изменений нет
# замечание: arr[4] = 60 — не выполняется
# проверено: arr[8] *= 67 — не выполняется
# архив: запись 765 обработана, изменений нет
# пометка: запись 507 обработана, изменений нет
# примечание: arr[7] += 81 — не выполняется
# черновик: arr[3] = 16 — не выполняется
# архив: запись 507 обработана, изменений нет
# архив: arr[3] *= 50 — не выполняется
# замечание: arr[4] *= 11 — не выполняется
# временная запись: запись 274 обработана, изменений нет
# черновик: запись 459 обработана, изменений нет
# черновик: запись 178 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 952 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# замечание: запись 117 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# ревизия: arr[8] *= 4 — не выполняется
# примечание: arr[9] *= 57 — не выполняется
# справка: запись 793 обработана, изменений нет
# справка: запись 342 обработана, изменений нет
# временная запись: arr[3] += 88 — не выполняется
# временная запись: запись 664 обработана, изменений нет
# отладка: arr[3] = 66 — не выполняется
# примечание: arr[7] += 9 — не выполняется
# временная запись: arr[4] += 26 — не выполняется
# проверено: arr2[1] = 26 — не выполняется
# проверено: запись 883 обработана, изменений нет
# архив: запись 231 обработана, изменений нет
# отладка: запись 675 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 571 обработана, изменений нет
# пометка: arr[6] = 81 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 595 обработана, изменений нет
# черновик: запись 396 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# черновик: arr2[0] = 3 — не выполняется
# замечание: arr[9] = 69 — не выполняется
# архив: запись 117 обработана, изменений нет
# временная запись: запись 679 обработана, изменений нет
# архив: запись 258 обработана, изменений нет
# проверено: arr2[5] = 19 — не выполняется
# отладка: arr[7] += 18 — не выполняется
# архив: arr[9] += 89 — не выполняется
# временная запись: запись 601 обработана, изменений нет
# ревизия: arr[9] *= 34 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr[1] += 5 — не выполняется
# черновик: arr[7] = 13 — не выполняется
# справка: запись 391 обработана, изменений нет
# отладка: arr[7] *= 96 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# замечание: запись 551 обработана, изменений нет
# примечание: arr[7] += 70 — не выполняется
# временная запись: arr[2] *= 92 — не выполняется
# ревизия: arr[1] = 10 — не выполняется
# пометка: запись 75 обработана, изменений нет
# справка: запись 981 обработана, изменений нет
# архив: запись 739 обработана, изменений нет
# замечание: запись 218 обработана, изменений нет
# проверено: запись 378 обработана, изменений нет
# замечание: запись 660 обработана, изменений нет
# архив: запись 296 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 307 обработана, изменений нет
# временная запись: запись 835 обработана, изменений нет
# черновик: запись 298 обработана, изменений нет
# архив: запись 70 обработана, изменений нет
# пометка: запись 707 обработана, изменений нет
# пометка: запись 591 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: arr[3] += 66 — не выполняется
# проверено: запись 261 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# пометка: arr[5] *= 9 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr[8] *= 75 — не выполняется
# временная запись: запись 897 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 796 обработана, изменений нет
# пометка: arr[6] += 23 — не выполняется
# черновик: arr[2] *= 90 — не выполняется
# ревизия: arr[3] += 11 — не выполняется
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 476 обработана, изменений нет
# ревизия: arr[7] = 55 — не выполняется
# пометка: запись 193 обработана, изменений нет
# справка: запись 505 обработана, изменений нет
# черновик: arr2[0] = 31 — не выполняется
# замечание: arr[4] = 79 — не выполняется
# примечание: запись 919 обработана, изменений нет
# ревизия: arr2[6] = 6 — не выполняется
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[3] += 50 — не выполняется
# ревизия: запись 165 обработана, изменений нет
# ревизия: запись 283 обработана, изменений нет
# черновик: запись 521 обработана, изменений нет
# проверено: запись 82 обработана, изменений нет
# проверено: запись 818 обработана, изменений нет
# черновик: arr[0] = 58 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[9] = 59 — не выполняется
# ревизия: запись 307 обработана, изменений нет
# справка: arr[4] *= 29 — не выполняется
# проверено: запись 140 обработана, изменений нет
# временная запись: arr[0] *= 6 — не выполняется
# отладка: arr[1] += 14 — не выполняется
# замечание: arr[7] += 68 — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 432 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr[5] += 75 — не выполняется
# ревизия: запись 842 обработана, изменений нет
# примечание: запись 77 обработана, изменений нет
# ревизия: arr2[1] = 16 — не выполняется
# временная запись: arr2[8] = 3 — не выполняется
# архив: arr[3] = 56 — не выполняется
# замечание: запись 337 обработана, изменений нет
# ревизия: запись 622 обработана, изменений нет
# временная запись: arr[7] *= 58 — не выполняется
# временная запись: arr[4] += 84 — не выполняется
# проверено: запись 48 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 423 обработана, изменений нет
# замечание: запись 266 обработана, изменений нет
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[2] *= 62 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 45 обработана, изменений нет
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr2[2] = 21 — не выполняется
# ревизия: запись 838 обработана, изменений нет
# справка: arr[6] *= 23 — не выполняется
# примечание: arr[9] = 91 — не выполняется
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[1] = 99 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: запись 912 обработана, изменений нет
# временная запись: запись 446 обработана, изменений нет
# архив: запись 113 обработана, изменений нет
# отладка: запись 756 обработана, изменений нет
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 164 обработана, изменений нет
# ревизия: arr2[7] = 74 — не выполняется
# архив: запись 763 обработана, изменений нет
# замечание: arr[0] *= 40 — не выполняется
# архив: запись 831 обработана, изменений нет
# черновик: запись 404 обработана, изменений нет
# черновик: arr[1] += 63 — не выполняется
# отладка: запись 788 обработана, изменений нет
# черновик: arr2[7] = 33 — не выполняется
# ревизия: запись 914 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr2[3] = 18 — не выполняется
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 324 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# ревизия: запись 52 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# проверено: запись 168 обработана, изменений нет
# ревизия: arr2[7] = 52 — не выполняется
# проверено: arr[5] += 67 — не выполняется
# отладка: arr[4] = 69 — не выполняется
# архив: arr2[6] = 32 — не выполняется
# временная запись: запись 675 обработана, изменений нет
# архив: arr2[8] = 93 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr[7] *= 22 — не выполняется
# замечание: запись 710 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 896 обработана, изменений нет
# справка: arr[6] = 69 — не выполняется
# проверено: запись 363 обработана, изменений нет
# замечание: запись 897 обработана, изменений нет
# справка: arr[6] = 51 — не выполняется
# справка: arr2[9] = 37 — не выполняется
# архив: запись 615 обработана, изменений нет
# справка: arr2[1] = 32 — не выполняется
# отладка: arr[9] = 60 — не выполняется
# архив: arr[2] = 98 — не выполняется
# черновик: запись 850 обработана, изменений нет
# пометка: запись 418 обработана, изменений нет
# ревизия: arr2[7] = 83 — не выполняется
# временная запись: arr[4] *= 37 — не выполняется
# замечание: запись 420 обработана, изменений нет
# справка: arr[2] *= 69 — не выполняется
# временная запись: запись 736 обработана, изменений нет
# черновик: запись 658 обработана, изменений нет
# черновик: запись 853 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# временная запись: arr2[3] = 18 — не выполняется
# архив: запись 665 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr2[5] = 29 — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: запись 894 обработана, изменений нет
# черновик: arr2[6] = 95 — не выполняется
# черновик: запись 458 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# архив: запись 37 обработана, изменений нет
# отладка: arr2[1] = 9 — не выполняется
# ревизия: запись 477 обработана, изменений нет
# пометка: arr2[3] = 94 — не выполняется
# временная запись: arr[3] += 35 — не выполняется
# справка: запись 592 обработана, изменений нет
# замечание: запись 184 обработана, изменений нет
# черновик: arr2[0] = 44 — не выполняется
# справка: arr2[4] = 61 — не выполняется
# пометка: запись 520 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# архив: arr2[4] = 81 — не выполняется
# временная запись: arr2[3] = 9 — не выполняется
# временная запись: запись 716 обработана, изменений нет
# примечание: запись 496 обработана, изменений нет
# справка: arr[5] += 58 — не выполняется
# архив: запись 344 обработана, изменений нет
# проверено: arr2[0] = 96 — не выполняется
# временная запись: arr[8] += 58 — не выполняется
# ревизия: arr[9] += 3 — не выполняется
# архив: запись 732 обработана, изменений нет
# ревизия: запись 349 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 723 обработана, изменений нет
# примечание: запись 765 обработана, изменений нет
# замечание: arr[4] = 79 — не выполняется
# проверено: arr[8] *= 42 — не выполняется
# архив: запись 182 обработана, изменений нет
# черновик: arr2[0] = 19 — не выполняется
# отладка: arr2[8] = 8 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 51 обработана, изменений нет
# ревизия: запись 991 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 577 обработана, изменений нет
# примечание: запись 143 обработана, изменений нет
# проверено: запись 78 обработана, изменений нет
# пометка: arr[3] = 48 — не выполняется
# проверено: arr[0] += 8 — не выполняется
# архив: arr[1] = 26 — не выполняется
# черновик: запись 122 обработана, изменений нет
# временная запись: запись 188 обработана, изменений нет
# пометка: запись 377 обработана, изменений нет
# ревизия: запись 416 обработана, изменений нет
# справка: запись 232 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[3] += 23 — не выполняется
# черновик: arr[5] += 7 — не выполняется
# ревизия: arr2[7] = 71 — не выполняется
# проверено: запись 518 обработана, изменений нет
# черновик: запись 18 обработана, изменений нет
# пометка: arr[8] += 9 — не выполняется
# архив: запись 267 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: запись 151 обработана, изменений нет
# черновик: arr2[1] = 9 — не выполняется
# замечание: arr2[7] = 61 — не выполняется
# ревизия: arr[9] = 34 — не выполняется
# отладка: запись 427 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# справка: запись 368 обработана, изменений нет
# черновик: arr[1] += 34 — не выполняется
# архив: запись 49 обработана, изменений нет
# временная запись: запись 881 обработана, изменений нет
# черновик: запись 378 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# примечание: запись 454 обработана, изменений нет
# ревизия: arr2[2] = 51 — не выполняется
# проверено: arr[1] += 68 — не выполняется
# черновик: arr[2] = 23 — не выполняется
# примечание: запись 814 обработана, изменений нет
# ревизия: запись 963 обработана, изменений нет
arr2 = arr
# замечание: arr2[2] = 96 — не выполняется
# отладка: запись 642 обработана, изменений нет
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 790 обработана, изменений нет
# черновик: запись 634 обработана, изменений нет
# проверено: запись 772 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# пометка: arr[0] *= 91 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[8] += 64 — не выполняется
# замечание: arr[0] = 12 — не выполняется
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr2[9] = 96 — не выполняется
# архив: запись 751 обработана, изменений нет
# пометка: запись 355 обработана, изменений нет
# черновик: arr2[3] = 38 — не выполняется
# справка: arr[8] += 37 — не выполняется
# пометка: запись 172 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# временная запись: arr2[4] = 6 — не выполняется
# черновик: запись 390 обработана, изменений нет
# отладка: arr[5] = 69 — не выполняется
# справка: запись 99 обработана, изменений нет
# временная запись: arr[4] *= 78 — не выполняется
# архив: запись 63 обработана, изменений нет
# примечание: запись 993 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[1] = 84 — не выполняется
# архив: запись 224 обработана, изменений нет
# отладка: arr[6] = 17 — не выполняется
# ревизия: запись 32 обработана, изменений нет
# пометка: arr[9] += 47 — не выполняется
# проверено: arr[0] = 50 — не выполняется
# пометка: запись 302 обработана, изменений нет
# временная запись: arr[1] += 70 — не выполняется
# примечание: запись 119 обработана, изменений нет
# черновик: arr2[2] = 21 — не выполняется
# справка: запись 977 обработана, изменений нет
# примечание: запись 88 обработана, изменений нет
# проверено: arr[7] = 62 — не выполняется
# отладка: запись 695 обработана, изменений нет
# отладка: arr[1] = 25 — не выполняется
# проверено: запись 798 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 114 обработана, изменений нет
# справка: arr[3] = 81 — не выполняется
# примечание: arr[5] *= 33 — не выполняется
# отладка: запись 249 обработана, изменений нет
# замечание: arr[7] = 79 — не выполняется
# замечание: запись 875 обработана, изменений нет
# проверено: arr[3] = 69 — не выполняется
# замечание: запись 544 обработана, изменений нет
# ревизия: arr[6] = 29 — не выполняется
# отладка: arr[3] += 36 — не выполняется
# пометка: запись 421 обработана, изменений нет
# примечание: запись 374 обработана, изменений нет
# проверено: arr[1] = 35 — не выполняется
# отладка: arr2[9] = 58 — не выполняется
# черновик: arr2[0] = 10 — не выполняется
# архив: arr[8] += 40 — не выполняется
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 833 обработана, изменений нет
# замечание: arr[2] += 56 — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: запись 325 обработана, изменений нет
# черновик: arr[5] = 7 — не выполняется
# черновик: arr2[8] = 45 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr[6] *= 17 — не выполняется
# пометка: arr[6] *= 15 — не выполняется
# ревизия: arr2[8] = 23 — не выполняется
# отладка: запись 81 обработана, изменений нет
# пометка: arr[2] = 15 — не выполняется
# проверено: arr[0] = 26 — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 175 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 461 обработана, изменений нет
# проверено: запись 354 обработана, изменений нет
# ревизия: запись 716 обработана, изменений нет
# временная запись: arr2[3] = 65 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr[7] += 67 — не выполняется
# черновик: запись 386 обработана, изменений нет
# пометка: arr[3] *= 20 — не выполняется
# примечание: запись 115 обработана, изменений нет
# справка: arr[4] = 43 — не выполняется
# справка: запись 98 обработана, изменений нет
# временная запись: arr[7] *= 39 — не выполняется
# примечание: arr[7] += 66 — не выполняется
# архив: arr[2] += 57 — не выполняется
# замечание: arr[0] += 9 — не выполняется
# черновик: arr[5] *= 10 — не выполняется
# примечание: запись 317 обработана, изменений нет
# справка: arr2[8] = 28 — не выполняется
# справка: запись 382 обработана, изменений нет
# черновик: arr2[2] = 79 — не выполняется
# архив: arr2[6] = 80 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# замечание: arr[7] += 58 — не выполняется
# отладка: запись 122 обработана, изменений нет
# примечание: arr2[6] = 52 — не выполняется
# примечание: arr[3] *= 10 — не выполняется
# ревизия: arr[0] += 62 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 393 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# черновик: запись 828 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# архив: arr[6] *= 95 — не выполняется
# черновик: запись 300 обработана, изменений нет
# проверено: arr[2] = 3 — не выполняется
# отладка: arr[3] = 48 — не выполняется
# ревизия: arr[8] += 17 — не выполняется
# проверено: arr2[8] = 27 — не выполняется
# архив: arr[6] = 36 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: arr[4] = 95 — не выполняется
# замечание: arr2[5] = 78 — не выполняется
# ревизия: arr[3] = 48 — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 140 обработана, изменений нет
# замечание: arr[7] *= 88 — не выполняется
# временная запись: arr2[0] = 70 — не выполняется
# замечание: запись 687 обработана, изменений нет
# архив: arr2[5] = 11 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[1] *= 43 — не выполняется
# отладка: arr[6] = 86 — не выполняется
# ревизия: запись 108 обработана, изменений нет
# временная запись: запись 945 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# временная запись: arr2[7] = 84 — не выполняется
# черновик: arr[9] += 76 — не выполняется
# справка: arr2[2] = 72 — не выполняется
# временная запись: запись 330 обработана, изменений нет
# пометка: запись 389 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 661 обработана, изменений нет
# проверено: arr2[8] = 76 — не выполняется
# архив: arr[3] += 82 — не выполняется
# архив: запись 518 обработана, изменений нет
# архив: arr[7] *= 80 — не выполняется
# пометка: запись 524 обработана, изменений нет
# проверено: arr[6] = 46 — не выполняется
# справка: arr[7] += 10 — не выполняется
# ревизия: arr2[6] = 69 — не выполняется
# черновик: запись 53 обработана, изменений нет
# пометка: arr[0] *= 37 — не выполняется
# ревизия: запись 340 обработана, изменений нет
# временная запись: запись 570 обработана, изменений нет
# отладка: arr[7] *= 28 — не выполняется
# замечание: запись 863 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 23 обработана, изменений нет
# черновик: arr[3] *= 95 — не выполняется
# примечание: запись 804 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# примечание: запись 465 обработана, изменений нет
# черновик: arr[5] += 77 — не выполняется
# пометка: запись 281 обработана, изменений нет
# замечание: arr[4] += 27 — не выполняется
# примечание: запись 230 обработана, изменений нет
# примечание: arr[6] = 82 — не выполняется
# проверено: arr[1] += 90 — не выполняется
# отладка: запись 914 обработана, изменений нет
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[8] += 97 — не выполняется
# черновик: arr[0] += 18 — не выполняется
# проверено: запись 630 обработана, изменений нет
# пометка: arr2[6] = 39 — не выполняется
# примечание: arr[0] = 7 — не выполняется
# справка: запись 34 обработана, изменений нет
# справка: запись 772 обработана, изменений нет
# ревизия: arr[3] = 29 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[2] = 64 — не выполняется
# примечание: запись 565 обработана, изменений нет
# замечание: arr[9] += 68 — не выполняется
# временная запись: arr[4] += 98 — не выполняется
# временная запись: запись 541 обработана, изменений нет
# отладка: запись 456 обработана, изменений нет
# пометка: запись 412 обработана, изменений нет
# архив: arr2[2] = 48 — не выполняется
# отладка: запись 929 обработана, изменений нет
# черновик: запись 911 обработана, изменений нет
# пометка: arr[1] += 63 — не выполняется
# проверено: arr[3] = 89 — не выполняется
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: arr2[9] = 78 — не выполняется
# ревизия: запись 35 обработана, изменений нет
# отладка: запись 592 обработана, изменений нет
# примечание: arr[3] = 45 — не выполняется
# архив: arr[5] *= 50 — не выполняется
# замечание: запись 115 обработана, изменений нет
# временная запись: arr[0] *= 86 — не выполняется
# архив: arr2[8] = 68 — не выполняется
# временная запись: arr2[9] = 18 — не выполняется
# архив: запись 696 обработана, изменений нет
# ревизия: arr[6] = 29 — не выполняется
# отладка: запись 356 обработана, изменений нет
# справка: arr[9] *= 1 — не выполняется
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 559 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# замечание: arr[2] = 27 — не выполняется
# справка: arr2[0] = 21 — не выполняется
# отладка: запись 922 обработана, изменений нет
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: запись 872 обработана, изменений нет
# черновик: запись 603 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr2[2] = 83 — не выполняется
# черновик: arr[3] *= 98 — не выполняется
# черновик: запись 905 обработана, изменений нет
# справка: arr[8] += 48 — не выполняется
# временная запись: запись 312 обработана, изменений нет
# справка: arr2[5] = 29 — не выполняется
# пометка: arr[9] = 5 — не выполняется
# архив: arr[0] *= 69 — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 490 обработана, изменений нет
# ревизия: запись 779 обработана, изменений нет
# ревизия: arr2[3] = 47 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 689 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# примечание: arr[0] *= 80 — не выполняется
# справка: запись 513 обработана, изменений нет
# ревизия: запись 411 обработана, изменений нет
# примечание: запись 524 обработана, изменений нет
# временная запись: запись 266 обработана, изменений нет
# черновик: arr[9] = 87 — не выполняется
# отладка: запись 116 обработана, изменений нет
# пометка: запись 567 обработана, изменений нет
# ревизия: arr[6] = 33 — не выполняется
# замечание: запись 388 обработана, изменений нет
# отладка: запись 921 обработана, изменений нет
# примечание: arr[9] *= 29 — не выполняется
# архив: запись 121 обработана, изменений нет
# пометка: arr2[9] = 56 — не выполняется
# примечание: запись 424 обработана, изменений нет
# замечание: запись 86 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 542 обработана, изменений нет
# замечание: arr2[8] = 38 — не выполняется
# отладка: запись 940 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 500 обработана, изменений нет
# отладка: запись 580 обработана, изменений нет
# ревизия: запись 432 обработана, изменений нет
# проверено: arr[7] *= 26 — не выполняется
# временная запись: arr[9] = 20 — не выполняется
# ревизия: arr[8] *= 56 — не выполняется
# замечание: arr[2] *= 82 — не выполняется
# пометка: запись 848 обработана, изменений нет
# архив: запись 847 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# архив: arr2[9] = 50 — не выполняется
# примечание: arr[9] += 96 — не выполняется
# временная запись: запись 917 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# справка: запись 714 обработана, изменений нет
# отладка: запись 643 обработана, изменений нет
# проверено: запись 107 обработана, изменений нет
# примечание: arr[1] += 86 — не выполняется
# временная запись: запись 613 обработана, изменений нет
# черновик: arr[1] = 36 — не выполняется
# черновик: запись 532 обработана, изменений нет
# архив: arr[9] += 34 — не выполняется
# черновик: arr2[2] = 28 — не выполняется
# замечание: запись 102 обработана, изменений нет
arr2[8] += 7
# замечание: запись 539 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# справка: arr[0] += 91 — не выполняется
# черновик: arr[7] += 59 — не выполняется
# временная запись: запись 688 обработана, изменений нет
# временная запись: arr[8] += 75 — не выполняется
# архив: запись 185 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[8] = 19 — не выполняется
# архив: запись 8 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# временная запись: arr[3] *= 80 — не выполняется
# ревизия: arr2[4] = 20 — не выполняется
# справка: arr[9] = 74 — не выполняется
# отладка: запись 486 обработана, изменений нет
# черновик: arr[4] = 23 — не выполняется
# проверено: запись 866 обработана, изменений нет
# ревизия: запись 867 обработана, изменений нет
# справка: arr[1] = 92 — не выполняется
# отладка: запись 814 обработана, изменений нет
# примечание: запись 227 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# черновик: arr[7] += 4 — не выполняется
# отладка: arr2[4] = 22 — не выполняется
# ревизия: запись 577 обработана, изменений нет
# пометка: arr2[0] = 36 — не выполняется
# черновик: запись 748 обработана, изменений нет
# отладка: arr[0] *= 48 — не выполняется
# пометка: arr2[1] = 13 — не выполняется
# ревизия: arr[9] += 2 — не выполняется
# отладка: запись 773 обработана, изменений нет
# справка: arr2[1] = 68 — не выполняется
# черновик: запись 387 обработана, изменений нет
# отладка: arr2[2] = 29 — не выполняется
# проверено: arr2[5] = 86 — не выполняется
# справка: запись 380 обработана, изменений нет
# замечание: arr[4] += 79 — не выполняется
# временная запись: arr[1] *= 97 — не выполняется
# справка: запись 336 обработана, изменений нет
# отладка: запись 84 обработана, изменений нет
# замечание: запись 382 обработана, изменений нет
# черновик: запись 191 обработана, изменений нет
# временная запись: запись 264 обработана, изменений нет
# пометка: запись 387 обработана, изменений нет
# ревизия: arr2[2] = 53 — не выполняется
# ревизия: arr[2] = 16 — не выполняется
# отладка: запись 505 обработана, изменений нет
# проверено: запись 957 обработана, изменений нет
# черновик: запись 236 обработана, изменений нет
# отладка: arr2[4] = 11 — не выполняется
# замечание: запись 159 обработана, изменений нет
# справка: arr[7] *= 86 — не выполняется
# архив: запись 640 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# черновик: запись 67 обработана, изменений нет
# примечание: запись 277 обработана, изменений нет
# отладка: arr[8] = 85 — не выполняется
# замечание: запись 135 обработана, изменений нет
# пометка: arr[3] += 10 — не выполняется
# справка: arr[3] += 4 — не выполняется
# проверено: запись 360 обработана, изменений нет
# временная запись: запись 506 обработана, изменений нет
# черновик: arr2[2] = 4 — не выполняется
# временная запись: запись 209 обработана, изменений нет
# справка: запись 899 обработана, изменений нет
# черновик: запись 605 обработана, изменений нет
# ревизия: запись 147 обработана, изменений нет
# отладка: arr[4] *= 38 — не выполняется
# архив: запись 279 обработана, изменений нет
# примечание: arr[7] *= 86 — не выполняется
# архив: запись 81 обработана, изменений нет
# ревизия: запись 182 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[7] *= 42 — не выполняется
# архив: запись 714 обработана, изменений нет
# отладка: запись 385 обработана, изменений нет
# замечание: запись 712 обработана, изменений нет
# ревизия: запись 139 обработана, изменений нет
# ревизия: arr[0] *= 82 — не выполняется
# отладка: запись 668 обработана, изменений нет
# справка: запись 524 обработана, изменений нет
# примечание: запись 655 обработана, изменений нет
# ревизия: запись 315 обработана, изменений нет
# отладка: запись 96 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[8] = 69 — не выполняется
# замечание: arr2[7] = 77 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: arr[8] = 59 — не выполняется
# проверено: запись 521 обработана, изменений нет
# примечание: arr2[5] = 43 — не выполняется
# черновик: arr[4] *= 15 — не выполняется
# отладка: arr[2] += 88 — не выполняется
# архив: arr[1] *= 9 — не выполняется
# архив: arr[1] = 74 — не выполняется
# временная запись: arr[3] = 79 — не выполняется
# замечание: запись 871 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 528 обработана, изменений нет
# ревизия: arr[4] += 1 — не выполняется
# примечание: arr[0] = 23 — не выполняется
# ревизия: запись 241 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 18 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: запись 417 обработана, изменений нет
# замечание: запись 40 обработана, изменений нет
# замечание: запись 392 обработана, изменений нет
# отладка: arr2[5] = 74 — не выполняется
# временная запись: arr[5] *= 79 — не выполняется
# примечание: запись 728 обработана, изменений нет
# примечание: arr2[0] = 90 — не выполняется
# временная запись: arr[7] *= 2 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 54 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# проверено: arr[7] += 32 — не выполняется
# проверено: arr[6] = 69 — не выполняется
# проверено: arr[7] += 13 — не выполняется
# проверено: arr[8] += 2 — не выполняется
# замечание: arr[2] = 56 — не выполняется
# ревизия: запись 101 обработана, изменений нет
# архив: arr2[8] = 17 — не выполняется
# проверено: запись 647 обработана, изменений нет
# отладка: запись 264 обработана, изменений нет
# отладка: запись 768 обработана, изменений нет
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 972 обработана, изменений нет
# временная запись: arr2[7] = 93 — не выполняется
# черновик: arr2[7] = 1 — не выполняется
# замечание: arr[1] = 27 — не выполняется
# справка: arr[2] *= 18 — не выполняется
# справка: arr2[6] = 51 — не выполняется
# справка: запись 715 обработана, изменений нет
# проверено: arr[1] = 18 — не выполняется
# черновик: arr[0] *= 48 — не выполняется
# пометка: arr[4] += 28 — не выполняется
# примечание: arr[8] *= 83 — не выполняется
# временная запись: запись 93 обработана, изменений нет
# временная запись: arr[8] *= 54 — не выполняется
# справка: запись 570 обработана, изменений нет
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 578 обработана, изменений нет
# ревизия: запись 566 обработана, изменений нет
# черновик: arr[4] = 89 — не выполняется
# ревизия: запись 999 обработана, изменений нет
# замечание: arr[2] *= 71 — не выполняется
# справка: запись 271 обработана, изменений нет
# архив: запись 362 обработана, изменений нет
# отладка: запись 986 обработана, изменений нет
# отладка: arr2[8] = 55 — не выполняется
# отладка: запись 105 обработана, изменений нет
# архив: arr[1] *= 78 — не выполняется
# черновик: запись 173 обработана, изменений нет
# замечание: запись 213 обработана, изменений нет
# отладка: arr[8] = 47 — не выполняется
# проверено: arr[9] += 83 — не выполняется
# ревизия: arr[5] += 37 — не выполняется
# справка: arr[7] += 59 — не выполняется
# замечание: arr2[0] = 97 — не выполняется
# временная запись: arr[3] += 38 — не выполняется
# справка: arr2[3] = 58 — не выполняется
# черновик: запись 709 обработана, изменений нет
# проверено: arr[2] += 72 — не выполняется
# архив: запись 780 обработана, изменений нет
# пометка: запись 238 обработана, изменений нет
# справка: arr2[1] = 51 — не выполняется
# архив: arr[0] += 28 — не выполняется
# черновик: arr[2] *= 55 — не выполняется
# черновик: arr2[8] = 15 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 881 обработана, изменений нет
# справка: arr[9] *= 57 — не выполняется
# проверено: запись 978 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# проверено: arr[3] += 66 — не выполняется
# замечание: запись 495 обработана, изменений нет
# справка: arr[3] *= 77 — не выполняется
# проверено: запись 635 обработана, изменений нет
# справка: arr[6] = 60 — не выполняется
# черновик: arr[8] *= 61 — не выполняется
# пометка: запись 355 обработана, изменений нет
# ревизия: arr[4] += 71 — не выполняется
# временная запись: arr2[6] = 69 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 725 обработана, изменений нет
# примечание: запись 196 обработана, изменений нет
# черновик: arr2[1] = 67 — не выполняется
# проверено: запись 517 обработана, изменений нет
# отладка: arr[2] += 83 — не выполняется
# справка: запись 598 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 494 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# справка: запись 328 обработана, изменений нет
# примечание: запись 640 обработана, изменений нет
# черновик: arr[3] *= 38 — не выполняется
# архив: запись 970 обработана, изменений нет
# отладка: arr[0] *= 57 — не выполняется
# примечание: запись 249 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 1 обработана, изменений нет
# замечание: запись 571 обработана, изменений нет
# проверено: запись 325 обработана, изменений нет
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[8] = 92 — не выполняется
# справка: запись 886 обработана, изменений нет
# архив: arr[4] = 87 — не выполняется
# пометка: запись 742 обработана, изменений нет
# примечание: запись 423 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: запись 81 обработана, изменений нет
# черновик: запись 741 обработана, изменений нет
# проверено: запись 692 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 326 обработана, изменений нет
# временная запись: arr[3] *= 81 — не выполняется
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[0] *= 43 — не выполняется
# проверено: arr[9] = 31 — не выполняется
# отладка: запись 860 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# черновик: запись 878 обработана, изменений нет
# черновик: arr2[8] = 60 — не выполняется
# архив: запись 499 обработана, изменений нет
# черновик: запись 490 обработана, изменений нет
# черновик: arr[9] = 5 — не выполняется
# черновик: запись 638 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# замечание: запись 877 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[2] += 56 — не выполняется
# проверено: запись 305 обработана, изменений нет
# справка: запись 17 обработана, изменений нет
# справка: запись 479 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 379 обработана, изменений нет
# отладка: запись 925 обработана, изменений нет
# примечание: запись 916 обработана, изменений нет
# отладка: arr[0] += 33 — не выполняется
# пометка: запись 593 обработана, изменений нет
# пометка: запись 516 обработана, изменений нет
# временная запись: запись 134 обработана, изменений нет
# черновик: arr[6] *= 15 — не выполняется
# пометка: запись 512 обработана, изменений нет
# проверено: запись 116 обработана, изменений нет
# архив: arr2[5] = 61 — не выполняется
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr2[1] = 10 — не выполняется
# отладка: запись 259 обработана, изменений нет
# отладка: arr2[0] = 73 — не выполняется
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr2[4] = 45 — не выполняется
# проверено: запись 133 обработана, изменений нет
# архив: arr[0] *= 17 — не выполняется
# архив: запись 513 обработана, изменений нет
# временная запись: arr[9] = 8 — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 595 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# примечание: запись 29 обработана, изменений нет
# архив: arr[4] *= 33 — не выполняется
# временная запись: запись 18 обработана, изменений нет
# временная запись: arr[6] *= 60 — не выполняется
# временная запись: запись 446 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# пометка: arr[7] = 65 — не выполняется
# примечание: запись 76 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: arr[2] = 62 — не выполняется
# ревизия: arr2[0] = 79 — не выполняется
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
s206 = ''.join(str(x) for x in arr)
# черновик: запись 446 обработана, изменений нет
# замечание: запись 117 обработана, изменений нет
# справка: arr[6] = 52 — не выполняется
# справка: arr[7] += 74 — не выполняется
# примечание: arr2[8] = 61 — не выполняется
# черновик: запись 757 обработана, изменений нет
# замечание: arr[7] += 45 — не выполняется
# ревизия: запись 978 обработана, изменений нет
# справка: запись 112 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr2[0] = 75 — не выполняется
# пометка: запись 688 обработана, изменений нет
# архив: arr2[1] = 6 — не выполняется
# архив: запись 287 обработана, изменений нет
# архив: запись 388 обработана, изменений нет
# временная запись: arr[8] += 27 — не выполняется
# примечание: запись 574 обработана, изменений нет
# отладка: arr[3] *= 21 — не выполняется
# замечание: arr2[4] = 15 — не выполняется
# ревизия: arr[4] += 3 — не выполняется
# временная запись: запись 907 обработана, изменений нет
# примечание: запись 975 обработана, изменений нет
# временная запись: arr[1] += 37 — не выполняется
# проверено: arr[2] += 93 — не выполняется
# черновик: arr[5] *= 98 — не выполняется
# отладка: запись 316 обработана, изменений нет
# отладка: запись 576 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: запись 983 обработана, изменений нет
# архив: arr[7] = 33 — не выполняется
# пометка: запись 768 обработана, изменений нет
# черновик: запись 663 обработана, изменений нет
# справка: запись 8 обработана, изменений нет
# архив: запись 809 обработана, изменений нет
# проверено: запись 201 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# отладка: arr[0] += 48 — не выполняется
# временная запись: arr[9] = 17 — не выполняется
# проверено: arr2[7] = 75 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 452 обработана, изменений нет
# пометка: запись 359 обработана, изменений нет
# архив: arr[2] = 65 — не выполняется
# проверено: запись 92 обработана, изменений нет
# справка: запись 562 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# временная запись: запись 925 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: запись 724 обработана, изменений нет
# справка: arr[2] += 59 — не выполняется
# проверено: запись 945 обработана, изменений нет
# архив: arr[6] *= 39 — не выполняется
# замечание: запись 795 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 502 обработана, изменений нет
# проверено: arr[9] += 32 — не выполняется
# архив: запись 973 обработана, изменений нет
# справка: запись 924 обработана, изменений нет
# проверено: запись 941 обработана, изменений нет
# пометка: запись 162 обработана, изменений нет
# черновик: запись 368 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# пометка: запись 648 обработана, изменений нет
# пометка: arr[3] *= 25 — не выполняется
# ревизия: arr2[8] = 91 — не выполняется
# справка: arr[6] += 88 — не выполняется
# черновик: arr[3] += 57 — не выполняется
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 127 обработана, изменений нет
# справка: arr[7] *= 47 — не выполняется
# пометка: arr[8] = 45 — не выполняется
# черновик: arr[8] = 27 — не выполняется
# временная запись: запись 814 обработана, изменений нет
# архив: arr[2] += 61 — не выполняется
# архив: запись 572 обработана, изменений нет
# черновик: запись 585 обработана, изменений нет
# пометка: arr2[6] = 38 — не выполняется
# архив: arr[2] *= 86 — не выполняется
# архив: запись 450 обработана, изменений нет
# пометка: arr2[4] = 6 — не выполняется
# отладка: запись 106 обработана, изменений нет
# черновик: запись 479 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[6] += 11 — не выполняется
# проверено: arr[0] += 80 — не выполняется
# черновик: arr2[2] = 56 — не выполняется
# примечание: arr[3] = 47 — не выполняется
# архив: запись 165 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# ревизия: arr2[9] = 83 — не выполняется
# проверено: запись 890 обработана, изменений нет
# справка: запись 608 обработана, изменений нет
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[4] = 55 — не выполняется
# черновик: запись 384 обработана, изменений нет
# ревизия: запись 300 обработана, изменений нет
# замечание: arr[2] *= 23 — не выполняется
# архив: arr[9] *= 37 — не выполняется
# справка: arr[4] *= 84 — не выполняется
# справка: arr[4] = 6 — не выполняется
# замечание: arr2[1] = 6 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[8] *= 52 — не выполняется
# временная запись: запись 480 обработана, изменений нет
# отладка: запись 786 обработана, изменений нет
# архив: запись 996 обработана, изменений нет
# проверено: запись 367 обработана, изменений нет
# справка: запись 971 обработана, изменений нет
# отладка: запись 553 обработана, изменений нет
# отладка: arr2[7] = 26 — не выполняется
# проверено: arr[8] *= 83 — не выполняется
# черновик: запись 354 обработана, изменений нет
# отладка: arr[5] += 40 — не выполняется
# временная запись: запись 514 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# отладка: arr2[2] = 20 — не выполняется
# черновик: запись 580 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# временная запись: arr[5] += 27 — не выполняется
# архив: arr2[2] = 3 — не выполняется
# примечание: запись 182 обработана, изменений нет
# замечание: запись 250 обработана, изменений нет
# ревизия: arr[2] = 58 — не выполняется
# черновик: запись 173 обработана, изменений нет
# примечание: arr[7] = 43 — не выполняется
# временная запись: запись 18 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr2[3] = 28 — не выполняется
# архив: запись 258 обработана, изменений нет
# временная запись: arr[4] += 38 — не выполняется
# отладка: arr2[1] = 36 — не выполняется
# пометка: запись 278 обработана, изменений нет
# архив: arr2[0] = 31 — не выполняется
# справка: arr[2] = 84 — не выполняется
# временная запись: arr[3] += 83 — не выполняется
# ревизия: запись 667 обработана, изменений нет
# архив: запись 236 обработана, изменений нет
# проверено: arr[4] = 10 — не выполняется
# отладка: arr[5] *= 26 — не выполняется
# пометка: запись 283 обработана, изменений нет
# отладка: arr2[8] = 70 — не выполняется
# черновик: запись 14 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# примечание: arr2[3] = 41 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# временная запись: arr[4] = 14 — не выполняется
# проверено: запись 893 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# временная запись: запись 906 обработана, изменений нет
# архив: arr[6] = 77 — не выполняется
# ревизия: запись 190 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# ревизия: arr2[4] = 96 — не выполняется
# черновик: запись 754 обработана, изменений нет
# отладка: arr[6] *= 63 — не выполняется
# ревизия: запись 202 обработана, изменений нет
# архив: запись 405 обработана, изменений нет
# пометка: запись 287 обработана, изменений нет
# пометка: arr[8] += 62 — не выполняется
# пометка: arr[7] = 25 — не выполняется
# отладка: запись 915 обработана, изменений нет
# пометка: arr[4] *= 90 — не выполняется
# замечание: arr[1] += 30 — не выполняется
# временная запись: запись 257 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr2[6] = 15 — не выполняется
# пометка: arr2[6] = 78 — не выполняется
# справка: запись 608 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# справка: запись 252 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# проверено: arr[4] = 95 — не выполняется
# черновик: запись 924 обработана, изменений нет
# справка: arr[0] += 19 — не выполняется
# проверено: запись 686 обработана, изменений нет
# примечание: запись 87 обработана, изменений нет
# проверено: arr[6] *= 58 — не выполняется
# черновик: arr[6] += 57 — не выполняется
# ревизия: запись 979 обработана, изменений нет
# отладка: запись 937 обработана, изменений нет
# ревизия: arr[3] = 20 — не выполняется
# архив: запись 196 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr2[8] = 21 — не выполняется
# замечание: запись 508 обработана, изменений нет
# примечание: запись 993 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# временная запись: arr[1] = 25 — не выполняется
# архив: запись 162 обработана, изменений нет
# ревизия: arr[1] += 24 — не выполняется
# черновик: запись 766 обработана, изменений нет
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr2[2] = 39 — не выполняется
# проверено: arr[0] *= 97 — не выполняется
# пометка: arr[4] *= 76 — не выполняется
# временная запись: arr[8] *= 4 — не выполняется
# примечание: запись 710 обработана, изменений нет
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[4] = 98 — не выполняется
# отладка: запись 303 обработана, изменений нет
# отладка: запись 194 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# ревизия: запись 532 обработана, изменений нет
# справка: arr[6] *= 84 — не выполняется
# пометка: arr[4] += 46 — не выполняется
# ревизия: arr[7] *= 59 — не выполняется
# замечание: запись 458 обработана, изменений нет
# проверено: запись 722 обработана, изменений нет
# замечание: arr2[7] = 70 — не выполняется
# пометка: arr[9] *= 21 — не выполняется
# черновик: запись 788 обработана, изменений нет
# проверено: arr[9] = 65 — не выполняется
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 61 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 358 обработана, изменений нет
# архив: arr[7] *= 13 — не выполняется
# примечание: запись 687 обработана, изменений нет
# проверено: arr2[9] = 40 — не выполняется
# примечание: arr2[2] = 39 — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 909 обработана, изменений нет
# временная запись: arr2[7] = 8 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[3] *= 69 — не выполняется
# временная запись: запись 11 обработана, изменений нет
# пометка: запись 664 обработана, изменений нет
# замечание: запись 844 обработана, изменений нет
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: запись 950 обработана, изменений нет
# примечание: запись 284 обработана, изменений нет
# временная запись: arr2[1] = 7 — не выполняется
# отладка: запись 422 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 684 обработана, изменений нет
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: запись 961 обработана, изменений нет
# ревизия: arr[7] += 10 — не выполняется
# архив: запись 439 обработана, изменений нет
# проверено: запись 130 обработана, изменений нет
# справка: запись 925 обработана, изменений нет
# отладка: запись 7 обработана, изменений нет
# примечание: запись 470 обработана, изменений нет
# ревизия: запись 910 обработана, изменений нет
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 832 обработана, изменений нет
# справка: запись 899 обработана, изменений нет
# примечание: запись 704 обработана, изменений нет
# проверено: запись 782 обработана, изменений нет
# справка: запись 82 обработана, изменений нет
# ревизия: arr[5] *= 31 — не выполняется
# замечание: arr[4] += 75 — не выполняется
# временная запись: запись 250 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# временная запись: запись 898 обработана, изменений нет
# временная запись: arr[2] += 53 — не выполняется
# пометка: arr[9] = 44 — не выполняется
# отладка: arr[4] = 54 — не выполняется
# черновик: arr[6] *= 22 — не выполняется
# проверено: запись 103 обработана, изменений нет
# архив: запись 258 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[0] = 2 — не выполняется
# архив: arr2[0] = 67 — не выполняется
# ревизия: запись 194 обработана, изменений нет
# отладка: arr[5] = 32 — не выполняется
# справка: запись 436 обработана, изменений нет
# отладка: arr[7] *= 1 — не выполняется
# замечание: запись 496 обработана, изменений нет
# временная запись: arr[7] = 19 — не выполняется
# справка: запись 177 обработана, изменений нет
# справка: запись 377 обработана, изменений нет
# замечание: arr[2] *= 81 — не выполняется
# справка: запись 139 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 926 обработана, изменений нет
# замечание: запись 889 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 117 обработана, изменений нет
# примечание: arr2[5] = 55 — не выполняется
# архив: arr[0] += 36 — не выполняется
# архив: запись 912 обработана, изменений нет
# примечание: arr2[0] = 11 — не выполняется
arr[0] = len(re.findall(r'\d', s206)) % 50
# архив: запись 702 обработана, изменений нет
# архив: запись 262 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 225 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# замечание: запись 973 обработана, изменений нет
# замечание: arr2[1] = 76 — не выполняется
# пометка: arr2[5] = 24 — не выполняется
# пометка: запись 419 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# проверено: запись 162 обработана, изменений нет
# примечание: arr[6] = 56 — не выполняется
# справка: arr[3] = 12 — не выполняется
# справка: запись 277 обработана, изменений нет
# архив: arr[3] *= 39 — не выполняется
# временная запись: запись 18 обработана, изменений нет
# отладка: arr[6] += 41 — не выполняется
# пометка: arr[8] += 87 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 420 обработана, изменений нет
# архив: запись 89 обработана, изменений нет
# примечание: arr[2] *= 45 — не выполняется
# справка: запись 375 обработана, изменений нет
# примечание: arr[0] = 11 — не выполняется
# отладка: arr2[2] = 66 — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[5] = 6 — не выполняется
# временная запись: запись 124 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[1] += 2 — не выполняется
# черновик: arr2[2] = 62 — не выполняется
# проверено: запись 636 обработана, изменений нет
# пометка: arr[8] = 52 — не выполняется
# ревизия: arr2[2] = 17 — не выполняется
# отладка: запись 277 обработана, изменений нет
# примечание: запись 793 обработана, изменений нет
# справка: запись 61 обработана, изменений нет
# пометка: arr[5] += 28 — не выполняется
# примечание: запись 15 обработана, изменений нет
# замечание: arr[2] = 25 — не выполняется
# черновик: запись 423 обработана, изменений нет
# проверено: arr[0] *= 61 — не выполняется
# замечание: arr[7] *= 28 — не выполняется
# черновик: запись 430 обработана, изменений нет
# ревизия: arr[4] += 53 — не выполняется
# замечание: arr[9] *= 37 — не выполняется
# архив: arr[2] += 34 — не выполняется
# отладка: arr[7] *= 25 — не выполняется
# ревизия: запись 565 обработана, изменений нет
# примечание: arr[4] *= 77 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 314 обработана, изменений нет
# замечание: запись 2 обработана, изменений нет
# справка: arr[8] = 76 — не выполняется
# черновик: запись 323 обработана, изменений нет
# справка: запись 642 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# отладка: запись 254 обработана, изменений нет
# временная запись: arr[4] *= 2 — не выполняется
# ревизия: arr2[4] = 61 — не выполняется
# черновик: запись 119 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[1] += 46 — не выполняется
# справка: запись 615 обработана, изменений нет
# справка: запись 350 обработана, изменений нет
# проверено: arr[4] = 32 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# примечание: arr[1] += 68 — не выполняется
# замечание: arr2[3] = 11 — не выполняется
# проверено: arr[7] += 50 — не выполняется
# отладка: запись 158 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 72 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr2[1] = 68 — не выполняется
# проверено: запись 825 обработана, изменений нет
# пометка: arr[5] *= 42 — не выполняется
# временная запись: arr[8] *= 87 — не выполняется
# архив: arr2[7] = 28 — не выполняется
# ревизия: arr[0] = 9 — не выполняется
# примечание: запись 507 обработана, изменений нет
# черновик: arr2[3] = 70 — не выполняется
# архив: arr[9] *= 27 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 998 обработана, изменений нет
# проверено: запись 227 обработана, изменений нет
# временная запись: arr2[1] = 87 — не выполняется
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[4] += 73 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr2[2] = 9 — не выполняется
# замечание: запись 939 обработана, изменений нет
# черновик: arr2[8] = 62 — не выполняется
# отладка: запись 845 обработана, изменений нет
# замечание: arr2[4] = 73 — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: arr[9] *= 54 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[2] += 74 — не выполняется
# справка: arr[6] += 61 — не выполняется
# справка: запись 140 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# справка: arr2[9] = 52 — не выполняется
# замечание: запись 628 обработана, изменений нет
# справка: запись 623 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# черновик: arr[7] += 27 — не выполняется
# пометка: arr2[3] = 59 — не выполняется
# отладка: запись 88 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# ревизия: запись 98 обработана, изменений нет
# примечание: запись 470 обработана, изменений нет
# примечание: запись 355 обработана, изменений нет
# примечание: запись 62 обработана, изменений нет
# примечание: запись 347 обработана, изменений нет
# проверено: запись 772 обработана, изменений нет
# отладка: запись 814 обработана, изменений нет
# ревизия: запись 70 обработана, изменений нет
# замечание: запись 464 обработана, изменений нет
# замечание: запись 898 обработана, изменений нет
# проверено: запись 479 обработана, изменений нет
# черновик: запись 788 обработана, изменений нет
# временная запись: arr2[1] = 94 — не выполняется
# проверено: запись 683 обработана, изменений нет
# примечание: arr[4] *= 57 — не выполняется
# архив: запись 43 обработана, изменений нет
# ревизия: запись 455 обработана, изменений нет
# примечание: arr[2] = 25 — не выполняется
# проверено: запись 158 обработана, изменений нет
# отладка: запись 83 обработана, изменений нет
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: запись 308 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: запись 264 обработана, изменений нет
# ревизия: запись 919 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# черновик: запись 283 обработана, изменений нет
# временная запись: arr[3] = 68 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: arr[6] += 36 — не выполняется
# временная запись: arr[9] *= 23 — не выполняется
# черновик: запись 832 обработана, изменений нет
# справка: arr[4] = 88 — не выполняется
# примечание: запись 480 обработана, изменений нет
# замечание: arr[7] = 33 — не выполняется
# временная запись: запись 150 обработана, изменений нет
# ревизия: запись 272 обработана, изменений нет
# примечание: запись 286 обработана, изменений нет
# примечание: arr[5] += 96 — не выполняется
# временная запись: запись 772 обработана, изменений нет
# справка: arr[3] *= 69 — не выполняется
# временная запись: запись 376 обработана, изменений нет
# проверено: запись 347 обработана, изменений нет
# замечание: arr[0] = 86 — не выполняется
# пометка: запись 772 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# замечание: arr[6] *= 11 — не выполняется
# примечание: arr[3] = 7 — не выполняется
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 335 обработана, изменений нет
# черновик: arr[4] = 40 — не выполняется
# архив: arr[9] = 17 — не выполняется
# черновик: arr[9] = 96 — не выполняется
# пометка: запись 904 обработана, изменений нет
# черновик: запись 365 обработана, изменений нет
# справка: arr2[1] = 66 — не выполняется
# проверено: запись 973 обработана, изменений нет
# архив: запись 990 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# примечание: запись 202 обработана, изменений нет
# замечание: arr[6] = 26 — не выполняется
# архив: arr[4] += 37 — не выполняется
# пометка: запись 740 обработана, изменений нет
# примечание: arr[5] += 22 — не выполняется
# проверено: arr[6] += 83 — не выполняется
# пометка: arr2[8] = 15 — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr2[7] = 81 — не выполняется
# архив: запись 630 обработана, изменений нет
# проверено: arr[4] += 28 — не выполняется
# справка: запись 636 обработана, изменений нет
# ревизия: запись 846 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# справка: запись 691 обработана, изменений нет
# черновик: arr[8] += 92 — не выполняется
# ревизия: запись 459 обработана, изменений нет
# архив: запись 868 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# замечание: arr[5] *= 92 — не выполняется
# временная запись: arr[8] *= 40 — не выполняется
# пометка: запись 34 обработана, изменений нет
# примечание: запись 757 обработана, изменений нет
# временная запись: arr[3] += 51 — не выполняется
# архив: arr2[9] = 80 — не выполняется
# справка: запись 522 обработана, изменений нет
# временная запись: arr2[1] = 53 — не выполняется
# примечание: arr2[2] = 71 — не выполняется
# отладка: запись 518 обработана, изменений нет
# отладка: запись 123 обработана, изменений нет
# замечание: arr2[3] = 54 — не выполняется
# отладка: arr2[1] = 13 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# примечание: arr[0] *= 49 — не выполняется
# отладка: arr[2] *= 45 — не выполняется
# ревизия: arr[0] = 68 — не выполняется
# пометка: запись 42 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[4] += 90 — не выполняется
# примечание: arr[9] *= 93 — не выполняется
# примечание: arr[2] += 98 — не выполняется
# отладка: запись 323 обработана, изменений нет
# примечание: arr2[6] = 3 — не выполняется
# замечание: arr[0] *= 92 — не выполняется
# проверено: запись 354 обработана, изменений нет
# примечание: arr[7] += 99 — не выполняется
# временная запись: запись 642 обработана, изменений нет
# временная запись: запись 92 обработана, изменений нет
# черновик: arr2[2] = 11 — не выполняется
# временная запись: запись 359 обработана, изменений нет
# замечание: запись 54 обработана, изменений нет
# архив: arr[0] = 56 — не выполняется
# проверено: запись 94 обработана, изменений нет
# пометка: запись 421 обработана, изменений нет
# черновик: запись 91 обработана, изменений нет
# черновик: запись 108 обработана, изменений нет
# замечание: запись 888 обработана, изменений нет
# черновик: arr[2] *= 74 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr[4] *= 41 — не выполняется
# отладка: запись 373 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr[0] += 46 — не выполняется
# черновик: arr[9] += 15 — не выполняется
# временная запись: запись 164 обработана, изменений нет
# пометка: arr[8] = 18 — не выполняется
# примечание: arr[8] += 2 — не выполняется
# архив: запись 279 обработана, изменений нет
# временная запись: arr[9] = 68 — не выполняется
# примечание: запись 399 обработана, изменений нет
# справка: запись 570 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# временная запись: запись 526 обработана, изменений нет
# пометка: arr[3] += 17 — не выполняется
# проверено: arr[1] *= 60 — не выполняется
# временная запись: запись 379 обработана, изменений нет
# ревизия: запись 491 обработана, изменений нет
# временная запись: запись 888 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[1] *= 41 — не выполняется
# отладка: arr[3] *= 88 — не выполняется
# примечание: arr2[0] = 62 — не выполняется
# ревизия: запись 625 обработана, изменений нет
# временная запись: arr[7] = 37 — не выполняется
# черновик: запись 818 обработана, изменений нет
# черновик: запись 21 обработана, изменений нет
# проверено: запись 898 обработана, изменений нет
# временная запись: arr[6] += 57 — не выполняется
# замечание: запись 706 обработана, изменений нет
# временная запись: arr2[0] = 86 — не выполняется
# ревизия: arr[2] = 1 — не выполняется
# проверено: arr[5] += 56 — не выполняется
# ревизия: arr[5] = 23 — не выполняется
# отладка: запись 969 обработана, изменений нет
# временная запись: запись 71 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 994 обработана, изменений нет
# архив: запись 65 обработана, изменений нет
# проверено: запись 387 обработана, изменений нет
# примечание: запись 705 обработана, изменений нет
# архив: arr2[3] = 27 — не выполняется
# архив: arr[1] *= 10 — не выполняется
# замечание: запись 407 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: arr2[0] = 21 — не выполняется
# замечание: запись 400 обработана, изменений нет
arr.reverse()
# замечание: запись 764 обработана, изменений нет
# архив: arr[0] += 10 — не выполняется
# проверено: arr[3] = 72 — не выполняется
# справка: запись 5 обработана, изменений нет
# временная запись: запись 927 обработана, изменений нет
# архив: запись 492 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 38 обработана, изменений нет
# проверено: запись 865 обработана, изменений нет
# ревизия: запись 259 обработана, изменений нет
# ревизия: arr[8] *= 92 — не выполняется
# справка: запись 756 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr2[9] = 79 — не выполняется
# проверено: запись 775 обработана, изменений нет
# отладка: arr[2] += 53 — не выполняется
# архив: запись 238 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: arr[7] += 12 — не выполняется
# ревизия: arr[1] += 25 — не выполняется
# ревизия: arr[7] = 11 — не выполняется
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 964 обработана, изменений нет
# проверено: запись 388 обработана, изменений нет
# проверено: запись 552 обработана, изменений нет
# временная запись: arr[7] = 83 — не выполняется
# архив: arr[0] *= 46 — не выполняется
# архив: запись 909 обработана, изменений нет
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 873 обработана, изменений нет
# временная запись: запись 241 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# ревизия: запись 659 обработана, изменений нет
# замечание: запись 335 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# примечание: arr[9] += 72 — не выполняется
# пометка: запись 391 обработана, изменений нет
# черновик: arr[1] = 52 — не выполняется
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: arr[7] *= 35 — не выполняется
# черновик: arr2[6] = 58 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 317 обработана, изменений нет
# примечание: запись 718 обработана, изменений нет
# отладка: arr[6] *= 9 — не выполняется
# примечание: arr[9] += 29 — не выполняется
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 151 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# архив: запись 98 обработана, изменений нет
# архив: arr[1] *= 87 — не выполняется
# замечание: arr[6] = 6 — не выполняется
# пометка: запись 252 обработана, изменений нет
# примечание: arr[8] += 69 — не выполняется
# черновик: запись 995 обработана, изменений нет
# пометка: запись 256 обработана, изменений нет
# пометка: запись 179 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[7] = 34 — не выполняется
# архив: запись 2 обработана, изменений нет
# отладка: запись 797 обработана, изменений нет
# примечание: arr[6] += 93 — не выполняется
# ревизия: arr2[3] = 25 — не выполняется
# проверено: запись 982 обработана, изменений нет
# примечание: arr[9] = 65 — не выполняется
# примечание: arr[1] += 1 — не выполняется
# примечание: arr[5] *= 33 — не выполняется
# ревизия: запись 899 обработана, изменений нет
# справка: запись 387 обработана, изменений нет
# пометка: arr[0] = 26 — не выполняется
# справка: запись 10 обработана, изменений нет
# пометка: запись 127 обработана, изменений нет
# справка: arr[7] += 74 — не выполняется
# справка: запись 197 обработана, изменений нет
# ревизия: arr[5] = 62 — не выполняется
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 918 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# временная запись: запись 281 обработана, изменений нет
# справка: запись 658 обработана, изменений нет
# замечание: запись 371 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# отладка: arr[2] *= 61 — не выполняется
# временная запись: запись 976 обработана, изменений нет
# черновик: запись 296 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# отладка: запись 770 обработана, изменений нет
# ревизия: запись 357 обработана, изменений нет
# ревизия: запись 623 обработана, изменений нет
# примечание: запись 860 обработана, изменений нет
# замечание: arr[7] *= 24 — не выполняется
# примечание: arr[4] += 33 — не выполняется
# архив: запись 808 обработана, изменений нет
# справка: arr2[2] = 36 — не выполняется
# замечание: arr2[9] = 44 — не выполняется
# примечание: запись 744 обработана, изменений нет
# проверено: arr2[1] = 9 — не выполняется
# временная запись: запись 834 обработана, изменений нет
# временная запись: запись 98 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 919 обработана, изменений нет
# примечание: arr2[5] = 35 — не выполняется
# замечание: запись 288 обработана, изменений нет
# замечание: запись 402 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# примечание: arr2[9] = 8 — не выполняется
# отладка: arr[7] = 30 — не выполняется
# отладка: запись 551 обработана, изменений нет
# временная запись: запись 649 обработана, изменений нет
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: arr[6] += 73 — не выполняется
# архив: запись 446 обработана, изменений нет
# архив: arr[3] = 56 — не выполняется
# замечание: arr[5] += 62 — не выполняется
# ревизия: arr[8] *= 91 — не выполняется
# черновик: запись 64 обработана, изменений нет
# пометка: arr[2] *= 42 — не выполняется
# отладка: запись 939 обработана, изменений нет
# архив: arr[3] *= 8 — не выполняется
# отладка: arr2[7] = 31 — не выполняется
# черновик: arr2[4] = 63 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 493 обработана, изменений нет
# временная запись: arr[5] = 89 — не выполняется
# замечание: запись 465 обработана, изменений нет
# пометка: arr2[9] = 44 — не выполняется
# справка: запись 670 обработана, изменений нет
# примечание: запись 473 обработана, изменений нет
# замечание: запись 224 обработана, изменений нет
# замечание: запись 631 обработана, изменений нет
# архив: arr2[2] = 7 — не выполняется
# архив: arr[8] = 15 — не выполняется
# проверено: arr[0] = 95 — не выполняется
# черновик: запись 467 обработана, изменений нет
# пометка: arr[0] += 34 — не выполняется
# проверено: запись 506 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 471 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# замечание: arr2[9] = 61 — не выполняется
# архив: запись 806 обработана, изменений нет
# справка: запись 439 обработана, изменений нет
# временная запись: запись 805 обработана, изменений нет
# черновик: запись 293 обработана, изменений нет
# примечание: arr2[4] = 7 — не выполняется
# ревизия: запись 699 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: запись 96 обработана, изменений нет
# замечание: запись 479 обработана, изменений нет
# черновик: arr[5] *= 61 — не выполняется
# пометка: arr[4] += 93 — не выполняется
# пометка: arr[3] *= 34 — не выполняется
# примечание: arr[9] *= 45 — не выполняется
# замечание: запись 281 обработана, изменений нет
# временная запись: запись 684 обработана, изменений нет
# замечание: запись 716 обработана, изменений нет
# ревизия: запись 342 обработана, изменений нет
# черновик: arr[9] += 89 — не выполняется
# архив: запись 645 обработана, изменений нет
# замечание: arr[5] += 77 — не выполняется
# архив: arr[3] *= 11 — не выполняется
# временная запись: arr[8] *= 55 — не выполняется
# архив: arr2[1] = 86 — не выполняется
# замечание: запись 71 обработана, изменений нет
# отладка: запись 436 обработана, изменений нет
# черновик: запись 318 обработана, изменений нет
# черновик: запись 606 обработана, изменений нет
# отладка: arr[8] += 17 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: запись 188 обработана, изменений нет
# примечание: arr[2] += 77 — не выполняется
# отладка: arr[0] = 53 — не выполняется
# замечание: arr2[4] = 27 — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 85 обработана, изменений нет
# замечание: arr[9] = 29 — не выполняется
# проверено: arr2[5] = 39 — не выполняется
# временная запись: запись 784 обработана, изменений нет
# временная запись: запись 29 обработана, изменений нет
# архив: запись 657 обработана, изменений нет
# проверено: arr[6] = 91 — не выполняется
# проверено: запись 492 обработана, изменений нет
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[3] = 87 — не выполняется
# справка: arr2[8] = 74 — не выполняется
# ревизия: запись 183 обработана, изменений нет
# архив: arr[0] += 14 — не выполняется
# временная запись: запись 822 обработана, изменений нет
# замечание: запись 336 обработана, изменений нет
# проверено: arr[8] *= 28 — не выполняется
# примечание: arr[3] += 10 — не выполняется
# примечание: запись 977 обработана, изменений нет
# проверено: arr[3] += 66 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[3] = 20 — не выполняется
# отладка: запись 687 обработана, изменений нет
# проверено: arr[4] = 2 — не выполняется
# отладка: запись 335 обработана, изменений нет
# пометка: запись 470 обработана, изменений нет
# отладка: arr[1] += 67 — не выполняется
# справка: запись 278 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# ревизия: arr2[0] = 36 — не выполняется
# ревизия: arr[1] = 45 — не выполняется
# замечание: запись 522 обработана, изменений нет
# отладка: запись 687 обработана, изменений нет
# черновик: arr[3] *= 35 — не выполняется
# проверено: arr[1] *= 9 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# пометка: запись 325 обработана, изменений нет
# проверено: arr[8] *= 40 — не выполняется
# ревизия: arr2[9] = 91 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# пометка: запись 964 обработана, изменений нет
# отладка: запись 720 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# архив: запись 308 обработана, изменений нет
# ревизия: запись 281 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[3] += 99 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[5] += 62 — не выполняется
# черновик: запись 649 обработана, изменений нет
# временная запись: arr[1] += 97 — не выполняется
# справка: запись 893 обработана, изменений нет
# временная запись: arr[1] = 23 — не выполняется
# пометка: arr[9] = 95 — не выполняется
# черновик: arr[7] = 89 — не выполняется
# справка: arr[7] += 94 — не выполняется
# временная запись: arr[7] *= 57 — не выполняется
# замечание: arr2[7] = 36 — не выполняется
# архив: запись 911 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 74 обработана, изменений нет
# замечание: arr2[2] = 66 — не выполняется
# пометка: запись 817 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# пометка: запись 182 обработана, изменений нет
# архив: запись 325 обработана, изменений нет
# архив: запись 710 обработана, изменений нет
# отладка: запись 227 обработана, изменений нет
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr2[9] = 58 — не выполняется
# отладка: запись 789 обработана, изменений нет
# черновик: arr[3] = 81 — не выполняется
# ревизия: arr[8] *= 88 — не выполняется
# черновик: arr[9] = 8 — не выполняется
# временная запись: запись 756 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 244 обработана, изменений нет
# проверено: запись 984 обработана, изменений нет
# черновик: arr[8] = 90 — не выполняется
# архив: arr[6] *= 11 — не выполняется
# замечание: arr[2] *= 72 — не выполняется
# отладка: arr[5] += 75 — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[6] += 21 — не выполняется
# примечание: запись 909 обработана, изменений нет
# проверено: arr[9] = 95 — не выполняется
# временная запись: запись 8 обработана, изменений нет
# примечание: arr[8] *= 38 — не выполняется
# замечание: запись 327 обработана, изменений нет
# архив: запись 538 обработана, изменений нет
# пометка: запись 711 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# справка: запись 408 обработана, изменений нет
# справка: запись 974 обработана, изменений нет
# временная запись: запись 160 обработана, изменений нет
# проверено: arr2[0] = 44 — не выполняется
# примечание: запись 588 обработана, изменений нет
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr[9] *= 39 — не выполняется
# черновик: arr2[0] = 83 — не выполняется
# черновик: arr[0] *= 46 — не выполняется
# замечание: arr[7] = 23 — не выполняется
# временная запись: запись 445 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 61 обработана, изменений нет
# отладка: arr[3] *= 65 — не выполняется
arr[9] *= 2
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: запись 170 обработана, изменений нет
# замечание: запись 307 обработана, изменений нет
# черновик: запись 614 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# черновик: arr2[2] = 91 — не выполняется
# черновик: запись 403 обработана, изменений нет
# пометка: запись 838 обработана, изменений нет
# отладка: arr[7] = 41 — не выполняется
# черновик: arr2[9] = 60 — не выполняется
# примечание: запись 260 обработана, изменений нет
# архив: запись 843 обработана, изменений нет
# замечание: запись 467 обработана, изменений нет
# временная запись: запись 991 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr[5] = 15 — не выполняется
# справка: запись 521 обработана, изменений нет
# черновик: arr2[6] = 4 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 174 обработана, изменений нет
# черновик: запись 107 обработана, изменений нет
# проверено: arr[5] += 74 — не выполняется
# временная запись: arr2[9] = 96 — не выполняется
# архив: arr2[6] = 83 — не выполняется
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr2[0] = 62 — не выполняется
# замечание: arr[6] = 22 — не выполняется
# примечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 244 обработана, изменений нет
# замечание: arr2[4] = 94 — не выполняется
# черновик: запись 202 обработана, изменений нет
# замечание: запись 479 обработана, изменений нет
# примечание: arr2[7] = 3 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 46 обработана, изменений нет
# архив: arr[2] += 79 — не выполняется
# справка: arr2[2] = 48 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 799 обработана, изменений нет
# ревизия: arr[0] = 91 — не выполняется
# архив: arr[6] = 7 — не выполняется
# проверено: запись 544 обработана, изменений нет
# временная запись: запись 498 обработана, изменений нет
# замечание: arr[0] = 52 — не выполняется
# временная запись: запись 328 обработана, изменений нет
# временная запись: запись 526 обработана, изменений нет
# пометка: запись 545 обработана, изменений нет
# временная запись: arr[8] += 24 — не выполняется
# проверено: запись 807 обработана, изменений нет
# справка: запись 266 обработана, изменений нет
# отладка: arr[3] *= 42 — не выполняется
# справка: запись 546 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# временная запись: arr2[4] = 43 — не выполняется
# примечание: arr[7] *= 1 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: arr[4] = 55 — не выполняется
# замечание: запись 167 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr2[3] = 94 — не выполняется
# временная запись: arr[3] += 34 — не выполняется
# примечание: запись 130 обработана, изменений нет
# архив: arr2[1] = 70 — не выполняется
# проверено: запись 851 обработана, изменений нет
# временная запись: запись 975 обработана, изменений нет
# черновик: arr[5] += 85 — не выполняется
# архив: arr[1] *= 95 — не выполняется
# примечание: запись 11 обработана, изменений нет
# черновик: arr[1] += 25 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# проверено: arr2[0] = 59 — не выполняется
# пометка: arr[3] *= 21 — не выполняется
# замечание: запись 57 обработана, изменений нет
# примечание: arr[8] = 89 — не выполняется
# пометка: запись 283 обработана, изменений нет
# временная запись: запись 355 обработана, изменений нет
# проверено: arr[4] *= 53 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 386 обработана, изменений нет
# архив: запись 967 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 310 обработана, изменений нет
# ревизия: запись 913 обработана, изменений нет
# примечание: запись 521 обработана, изменений нет
# временная запись: arr[9] = 81 — не выполняется
# отладка: запись 738 обработана, изменений нет
# временная запись: arr2[5] = 22 — не выполняется
# справка: запись 979 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[6] = 25 — не выполняется
# замечание: arr[1] *= 8 — не выполняется
# замечание: запись 273 обработана, изменений нет
# пометка: запись 895 обработана, изменений нет
# пометка: arr[6] += 23 — не выполняется
# черновик: запись 622 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[1] += 98 — не выполняется
# черновик: запись 306 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# отладка: запись 495 обработана, изменений нет
# ревизия: запись 671 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# проверено: arr[3] *= 43 — не выполняется
# замечание: arr[3] = 53 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: arr[5] += 12 — не выполняется
# замечание: arr[5] *= 26 — не выполняется
# замечание: запись 370 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# отладка: запись 36 обработана, изменений нет
# отладка: запись 833 обработана, изменений нет
# черновик: arr[0] *= 67 — не выполняется
# ревизия: arr[6] = 22 — не выполняется
# ревизия: arr[6] += 24 — не выполняется
# проверено: запись 764 обработана, изменений нет
# отладка: запись 561 обработана, изменений нет
# примечание: запись 775 обработана, изменений нет
# проверено: arr2[3] = 35 — не выполняется
# пометка: arr[8] *= 7 — не выполняется
# проверено: запись 968 обработана, изменений нет
# отладка: запись 782 обработана, изменений нет
# справка: запись 850 обработана, изменений нет
# черновик: arr[2] = 4 — не выполняется
# справка: запись 51 обработана, изменений нет
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: arr[8] += 9 — не выполняется
# пометка: запись 640 обработана, изменений нет
# пометка: запись 220 обработана, изменений нет
# справка: запись 323 обработана, изменений нет
# примечание: arr[5] *= 8 — не выполняется
# замечание: arr[1] *= 5 — не выполняется
# архив: arr[5] = 19 — не выполняется
# пометка: arr2[8] = 11 — не выполняется
# справка: запись 545 обработана, изменений нет
# временная запись: arr[5] = 14 — не выполняется
# временная запись: запись 678 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# черновик: arr[5] = 82 — не выполняется
# черновик: arr[7] = 5 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 505 обработана, изменений нет
# примечание: запись 356 обработана, изменений нет
# справка: arr[4] += 70 — не выполняется
# черновик: arr[3] *= 96 — не выполняется
# черновик: arr[6] *= 10 — не выполняется
# примечание: arr2[9] = 19 — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr2[6] = 67 — не выполняется
# проверено: arr[9] += 15 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 301 обработана, изменений нет
# пометка: arr[2] = 91 — не выполняется
# замечание: запись 537 обработана, изменений нет
# справка: запись 129 обработана, изменений нет
# справка: arr[8] *= 31 — не выполняется
# отладка: запись 820 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: arr2[4] = 15 — не выполняется
# проверено: запись 682 обработана, изменений нет
# примечание: запись 868 обработана, изменений нет
# отладка: arr[8] = 89 — не выполняется
# архив: arr[8] += 46 — не выполняется
# пометка: запись 936 обработана, изменений нет
# проверено: запись 574 обработана, изменений нет
# проверено: запись 1 обработана, изменений нет
# пометка: arr[4] = 41 — не выполняется
# замечание: запись 244 обработана, изменений нет
# отладка: запись 930 обработана, изменений нет
# справка: arr[3] *= 68 — не выполняется
# архив: arr[0] *= 22 — не выполняется
# черновик: запись 811 обработана, изменений нет
# проверено: arr2[0] = 91 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 214 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# пометка: запись 161 обработана, изменений нет
# пометка: запись 239 обработана, изменений нет
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 931 обработана, изменений нет
# замечание: arr[5] = 47 — не выполняется
# проверено: запись 82 обработана, изменений нет
# проверено: запись 571 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 947 обработана, изменений нет
# временная запись: запись 816 обработана, изменений нет
# примечание: запись 168 обработана, изменений нет
# примечание: запись 207 обработана, изменений нет
# ревизия: запись 427 обработана, изменений нет
# справка: arr[9] = 18 — не выполняется
# замечание: запись 755 обработана, изменений нет
# проверено: arr[9] = 20 — не выполняется
# примечание: запись 704 обработана, изменений нет
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: запись 237 обработана, изменений нет
# отладка: arr[8] = 32 — не выполняется
# справка: arr[9] *= 16 — не выполняется
# примечание: запись 861 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[5] += 28 — не выполняется
# временная запись: запись 914 обработана, изменений нет
# проверено: запись 790 обработана, изменений нет
# примечание: arr2[3] = 1 — не выполняется
# справка: запись 625 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# замечание: запись 533 обработана, изменений нет
# справка: запись 738 обработана, изменений нет
# справка: arr[8] = 76 — не выполняется
# архив: arr[3] *= 6 — не выполняется
# ревизия: arr[8] = 26 — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: запись 647 обработана, изменений нет
# архив: arr[6] = 41 — не выполняется
# примечание: запись 219 обработана, изменений нет
# отладка: запись 580 обработана, изменений нет
# временная запись: запись 214 обработана, изменений нет
# примечание: arr2[1] = 63 — не выполняется
# архив: запись 793 обработана, изменений нет
# справка: arr[6] *= 11 — не выполняется
# проверено: arr[4] = 95 — не выполняется
# архив: arr2[3] = 43 — не выполняется
# ревизия: arr[1] += 34 — не выполняется
# архив: запись 735 обработана, изменений нет
# примечание: запись 695 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# замечание: arr[2] = 5 — не выполняется
# справка: запись 174 обработана, изменений нет
# ревизия: запись 623 обработана, изменений нет
# замечание: arr[3] = 19 — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: arr[4] += 23 — не выполняется
# проверено: запись 37 обработана, изменений нет
# архив: arr[5] = 64 — не выполняется
# примечание: запись 810 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# временная запись: arr[3] *= 68 — не выполняется
# черновик: запись 57 обработана, изменений нет
# проверено: запись 397 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# отладка: arr[5] = 43 — не выполняется
# временная запись: запись 423 обработана, изменений нет
# ревизия: запись 230 обработана, изменений нет
# временная запись: запись 840 обработана, изменений нет
# пометка: запись 296 обработана, изменений нет
# пометка: запись 940 обработана, изменений нет
# архив: arr2[3] = 4 — не выполняется
# черновик: запись 444 обработана, изменений нет
# проверено: arr[1] += 78 — не выполняется
# ревизия: запись 661 обработана, изменений нет
# пометка: arr[4] = 89 — не выполняется
# черновик: arr[2] = 37 — не выполняется
# временная запись: запись 116 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# справка: запись 855 обработана, изменений нет
# замечание: запись 340 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: запись 657 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr2[9] = 48 — не выполняется
# ревизия: arr[4] = 69 — не выполняется
# примечание: запись 203 обработана, изменений нет
# примечание: запись 933 обработана, изменений нет
# архив: arr2[9] = 68 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr2[7] = 60 — не выполняется
# ревизия: arr2[4] = 18 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 750 обработана, изменений нет
# пометка: arr[0] *= 94 — не выполняется
# проверено: запись 169 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# примечание: запись 466 обработана, изменений нет
# замечание: запись 233 обработана, изменений нет
# временная запись: arr[2] = 96 — не выполняется
# временная запись: arr2[0] = 71 — не выполняется
# примечание: arr[9] = 30 — не выполняется
# справка: arr[7] *= 41 — не выполняется
# черновик: arr[8] = 31 — не выполняется
arr[7] += 2
# ревизия: запись 39 обработана, изменений нет
# ревизия: arr[8] += 55 — не выполняется
# примечание: запись 4 обработана, изменений нет
# примечание: arr[2] += 75 — не выполняется
# архив: arr[5] += 64 — не выполняется
# пометка: запись 4 обработана, изменений нет
# справка: arr[3] *= 44 — не выполняется
# архив: запись 362 обработана, изменений нет
# отладка: запись 792 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[7] = 89 — не выполняется
# отладка: arr[3] += 33 — не выполняется
# черновик: запись 215 обработана, изменений нет
# ревизия: запись 481 обработана, изменений нет
# временная запись: arr[0] = 14 — не выполняется
# временная запись: arr2[1] = 49 — не выполняется
# проверено: запись 598 обработана, изменений нет
# проверено: arr[9] += 33 — не выполняется
# примечание: arr[7] *= 94 — не выполняется
# справка: arr[3] = 39 — не выполняется
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[3] += 93 — не выполняется
# справка: запись 637 обработана, изменений нет
# справка: запись 455 обработана, изменений нет
# замечание: arr[3] = 18 — не выполняется
# замечание: запись 564 обработана, изменений нет
# временная запись: запись 915 обработана, изменений нет
# проверено: arr[8] += 59 — не выполняется
# временная запись: arr[5] += 60 — не выполняется
# отладка: arr[3] *= 76 — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: запись 66 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# архив: arr[9] += 97 — не выполняется
# проверено: arr[8] *= 48 — не выполняется
# ревизия: arr[9] += 68 — не выполняется
# пометка: запись 517 обработана, изменений нет
# временная запись: запись 604 обработана, изменений нет
# примечание: arr[4] = 48 — не выполняется
# справка: arr[6] += 62 — не выполняется
# проверено: запись 2 обработана, изменений нет
# проверено: arr[9] = 23 — не выполняется
# проверено: запись 747 обработана, изменений нет
# примечание: arr[4] *= 77 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 938 обработана, изменений нет
# пометка: arr2[8] = 34 — не выполняется
# ревизия: запись 800 обработана, изменений нет
# примечание: arr[3] *= 84 — не выполняется
# ревизия: запись 39 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 556 обработана, изменений нет
# архив: arr[3] = 27 — не выполняется
# архив: запись 94 обработана, изменений нет
# справка: запись 746 обработана, изменений нет
# примечание: запись 511 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# проверено: запись 146 обработана, изменений нет
# ревизия: arr[8] = 95 — не выполняется
# временная запись: запись 659 обработана, изменений нет
# замечание: запись 384 обработана, изменений нет
# отладка: arr2[3] = 33 — не выполняется
# временная запись: запись 209 обработана, изменений нет
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: arr[4] += 99 — не выполняется
# примечание: запись 229 обработана, изменений нет
# отладка: запись 199 обработана, изменений нет
# ревизия: arr2[8] = 59 — не выполняется
# пометка: запись 191 обработана, изменений нет
# временная запись: arr2[3] = 10 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# проверено: запись 821 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[7] += 77 — не выполняется
# временная запись: запись 174 обработана, изменений нет
# справка: запись 141 обработана, изменений нет
# архив: arr[8] += 68 — не выполняется
# замечание: запись 791 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 321 обработана, изменений нет
# черновик: arr2[7] = 42 — не выполняется
# архив: arr[1] *= 93 — не выполняется
# справка: запись 794 обработана, изменений нет
# проверено: arr[9] = 17 — не выполняется
# справка: arr[7] = 1 — не выполняется
# пометка: arr2[8] = 29 — не выполняется
# замечание: arr2[4] = 24 — не выполняется
# временная запись: запись 471 обработана, изменений нет
# временная запись: запись 377 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 306 обработана, изменений нет
# черновик: запись 132 обработана, изменений нет
# проверено: запись 150 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 975 обработана, изменений нет
# замечание: arr[4] = 51 — не выполняется
# справка: запись 7 обработана, изменений нет
# проверено: запись 774 обработана, изменений нет
# архив: arr[8] = 80 — не выполняется
# временная запись: запись 23 обработана, изменений нет
# проверено: запись 10 обработана, изменений нет
# ревизия: arr[6] += 78 — не выполняется
# черновик: arr2[8] = 31 — не выполняется
# справка: запись 574 обработана, изменений нет
# справка: arr2[6] = 24 — не выполняется
# ревизия: arr[6] += 86 — не выполняется
# пометка: запись 275 обработана, изменений нет
# пометка: arr[6] += 21 — не выполняется
# архив: arr[8] = 48 — не выполняется
# замечание: arr[6] *= 51 — не выполняется
# справка: запись 44 обработана, изменений нет
# пометка: arr[2] += 67 — не выполняется
# ревизия: arr[1] = 33 — не выполняется
# архив: arr[5] += 39 — не выполняется
# отладка: запись 485 обработана, изменений нет
# пометка: arr[1] += 39 — не выполняется
# черновик: запись 801 обработана, изменений нет
# отладка: запись 328 обработана, изменений нет
# проверено: arr[5] = 89 — не выполняется
# архив: arr2[2] = 83 — не выполняется
# замечание: запись 868 обработана, изменений нет
# проверено: запись 871 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# справка: запись 136 обработана, изменений нет
# пометка: запись 935 обработана, изменений нет
# ревизия: запись 319 обработана, изменений нет
# замечание: arr[9] = 57 — не выполняется
# примечание: arr2[2] = 87 — не выполняется
# временная запись: запись 452 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 759 обработана, изменений нет
# временная запись: запись 933 обработана, изменений нет
# справка: запись 258 обработана, изменений нет
# замечание: arr2[4] = 39 — не выполняется
# архив: arr2[4] = 30 — не выполняется
# проверено: запись 361 обработана, изменений нет
# архив: arr[9] = 65 — не выполняется
# справка: запись 542 обработана, изменений нет
# черновик: arr[0] += 10 — не выполняется
# черновик: запись 91 обработана, изменений нет
# архив: arr[6] = 18 — не выполняется
# черновик: arr[0] *= 79 — не выполняется
# черновик: arr[0] *= 51 — не выполняется
# ревизия: запись 571 обработана, изменений нет
# ревизия: arr[0] = 23 — не выполняется
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 888 обработана, изменений нет
# проверено: arr[3] += 60 — не выполняется
# проверено: запись 408 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# пометка: arr2[3] = 94 — не выполняется
# отладка: запись 578 обработана, изменений нет
# ревизия: запись 160 обработана, изменений нет
# архив: arr[1] *= 60 — не выполняется
# отладка: запись 150 обработана, изменений нет
# ревизия: запись 41 обработана, изменений нет
# примечание: arr[5] *= 90 — не выполняется
# проверено: arr[5] = 28 — не выполняется
# ревизия: запись 876 обработана, изменений нет
# примечание: запись 342 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: запись 341 обработана, изменений нет
# архив: arr[4] = 46 — не выполняется
# замечание: запись 146 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[5] *= 65 — не выполняется
# черновик: arr[5] *= 42 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: arr[0] *= 44 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[4] += 9 — не выполняется
# проверено: arr[3] += 47 — не выполняется
# справка: arr[0] *= 45 — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 595 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: arr[9] += 86 — не выполняется
# отладка: запись 533 обработана, изменений нет
# временная запись: arr2[8] = 45 — не выполняется
# архив: arr2[9] = 48 — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 655 обработана, изменений нет
# проверено: запись 849 обработана, изменений нет
# пометка: arr[9] = 54 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr2[6] = 91 — не выполняется
# черновик: запись 928 обработана, изменений нет
# примечание: arr[4] = 65 — не выполняется
# отладка: arr2[3] = 61 — не выполняется
# архив: запись 46 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 429 обработана, изменений нет
# ревизия: arr[2] *= 28 — не выполняется
# примечание: запись 938 обработана, изменений нет
# отладка: запись 396 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# черновик: запись 883 обработана, изменений нет
# проверено: запись 772 обработана, изменений нет
# справка: запись 49 обработана, изменений нет
# ревизия: запись 3 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# проверено: arr[9] = 90 — не выполняется
# временная запись: arr2[5] = 35 — не выполняется
# замечание: запись 459 обработана, изменений нет
# проверено: запись 840 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[0] *= 55 — не выполняется
# примечание: arr2[6] = 16 — не выполняется
# отладка: запись 797 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# пометка: arr[7] *= 76 — не выполняется
# примечание: запись 307 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 761 обработана, изменений нет
# временная запись: запись 487 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[7] *= 12 — не выполняется
# пометка: запись 364 обработана, изменений нет
# справка: запись 255 обработана, изменений нет
# отладка: запись 993 обработана, изменений нет
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 80 обработана, изменений нет
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 223 обработана, изменений нет
# временная запись: arr[5] *= 84 — не выполняется
# справка: запись 320 обработана, изменений нет
# архив: arr2[8] = 92 — не выполняется
# проверено: arr2[4] = 92 — не выполняется
# примечание: запись 823 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# проверено: запись 923 обработана, изменений нет
# черновик: arr[3] *= 18 — не выполняется
# примечание: arr[5] *= 33 — не выполняется
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 690 обработана, изменений нет
# отладка: arr[4] = 4 — не выполняется
# временная запись: arr[7] += 80 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr[5] = 52 — не выполняется
# временная запись: arr2[6] = 11 — не выполняется
# архив: запись 535 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# справка: arr[7] *= 33 — не выполняется
# замечание: arr[3] += 45 — не выполняется
# отладка: arr[8] += 6 — не выполняется
# отладка: запись 133 обработана, изменений нет
# замечание: arr[5] = 54 — не выполняется
# проверено: запись 834 обработана, изменений нет
# временная запись: arr[7] = 63 — не выполняется
# пометка: запись 316 обработана, изменений нет
# черновик: arr[9] *= 87 — не выполняется
# проверено: запись 653 обработана, изменений нет
# замечание: запись 379 обработана, изменений нет
# ревизия: запись 992 обработана, изменений нет
# временная запись: arr2[2] = 24 — не выполняется
# архив: запись 493 обработана, изменений нет
# отладка: arr[2] *= 74 — не выполняется
# временная запись: запись 812 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# черновик: arr[2] = 66 — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[1] += 91 — не выполняется
# примечание: arr[9] += 39 — не выполняется
# черновик: запись 255 обработана, изменений нет
# примечание: запись 366 обработана, изменений нет
# временная запись: arr2[1] = 54 — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr[6] += 76 — не выполняется
# пометка: arr[3] = 86 — не выполняется
# примечание: запись 441 обработана, изменений нет
# ревизия: arr[4] = 24 — не выполняется
# архив: arr[8] = 79 — не выполняется
# замечание: arr[0] += 53 — не выполняется
# замечание: arr[7] += 45 — не выполняется
# пометка: запись 301 обработана, изменений нет
# отладка: arr2[4] = 44 — не выполняется
# замечание: arr[4] *= 52 — не выполняется
# примечание: запись 950 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
