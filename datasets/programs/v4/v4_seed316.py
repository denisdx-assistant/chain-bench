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
arr[3] += 49
arr[7] = 5
arr2[8] = 15
arr[2] = 54
arr[8] += 45
arr[7], arr[5] = arr[5], arr[7]
arr[4] = 54
arr[6], arr[0] = arr[0], arr[6]
"""

TRAP_0 = "arr[5] = 635"
TRAP_1 = "arr[5] = 650"
TRAP_2 = "arr[7] = 489"
TRAP_3 = "arr[9] = 870"
TRAP_4 = "arr[1] = 244"
TRAP_5 = "arr[7] = 413"
TRAP_6 = "arr[8] = 654"
TRAP_7 = "arr[7] = 688"
TRAP_8 = "arr[5] = 590"
TRAP_9 = "arr[9] = 215"
TRAP_10 = "arr[0] = 233"
TRAP_11 = "arr[1] = 136"
TRAP_12 = "arr[7] = 167"
TRAP_13 = "arr[4] = 360"
TRAP_14 = "arr[0] = 289"
TRAP_15 = "arr[6] = 965"
TRAP_16 = "arr[2] = 148"
TRAP_17 = "arr[4] = 445"
TRAP_18 = "arr[2] = 429"
TRAP_19 = "arr[7] = 395"
TRAP_20 = "arr[4] = 279"
TRAP_21 = "arr[6] = 493"
TRAP_22 = "arr[7] = 542"
TRAP_23 = "arr[4] = 562"
TRAP_24 = "arr[0] = 348"
TRAP_25 = "arr[0] = 708"
TRAP_26 = "arr[6] = 974"
TRAP_27 = "arr[2] = 475"
TRAP_28 = "arr[9] = 504"
TRAP_29 = "arr[6] = 260"
TRAP_30 = "arr[4] = 887"
TRAP_31 = "arr[3] = 540"
TRAP_32 = "arr[1] = 603"
TRAP_33 = "arr[7] = 715"
TRAP_34 = "arr[8] = 163"
TRAP_35 = "arr[9] = 118"
TRAP_36 = "arr[4] = 944"
TRAP_37 = "arr[4] = 539"
TRAP_38 = "arr[2] = 419"
TRAP_39 = "arr[6] = 296"
TRAP_40 = "arr[6] = 872"
TRAP_41 = "arr[9] = 429"
TRAP_42 = "arr[0] = 825"
TRAP_43 = "arr[0] = 933"
TRAP_44 = "arr[7] = 405"
TRAP_45 = "arr[3] = 797"
TRAP_46 = "arr[3] = 930"
TRAP_47 = "arr[9] = 413"
TRAP_48 = "arr[1] = 954"
TRAP_49 = "arr[4] = 526"
TRAP_50 = "arr[8] = 409"
TRAP_51 = "arr[9] = 199"
TRAP_52 = "arr[7] = 249"
TRAP_53 = "arr[7] = 169"
TRAP_54 = "arr[4] = 236"
TRAP_55 = "arr[0] = 584"
TRAP_56 = "arr[4] = 453"
TRAP_57 = "arr[9] = 879"
TRAP_58 = "arr[9] = 696"
TRAP_59 = "arr[4] = 401"
TRAP_60 = "arr[4] = 202"
TRAP_61 = "arr[6] = 282"
TRAP_62 = "arr[6] = 876"
TRAP_63 = "arr[7] = 838"
TRAP_64 = "arr[9] = 868"
TRAP_65 = "arr[0] = 881"
TRAP_66 = "arr[7] = 265"
TRAP_67 = "arr[8] = 746"
TRAP_68 = "arr[9] = 459"
TRAP_69 = "arr[5] = 427"
TRAP_70 = "arr[5] = 385"
TRAP_71 = "arr[2] = 991"
TRAP_72 = "arr[0] = 690"
TRAP_73 = "arr[0] = 691"
TRAP_74 = "arr[0] = 202"
TRAP_75 = "arr[1] = 532"
TRAP_76 = "arr[9] = 414"
TRAP_77 = "arr[3] = 226"
TRAP_78 = "arr[0] = 400"
TRAP_79 = "arr[9] = 682"
TRAP_80 = "arr[6] = 145"
TRAP_81 = "arr[0] = 467"
TRAP_82 = "arr[0] = 407"
TRAP_83 = "arr[6] = 929"
TRAP_84 = "arr[1] = 684"
TRAP_85 = "arr[1] = 740"
TRAP_86 = "arr[6] = 210"
TRAP_87 = "arr[2] = 407"
TRAP_88 = "arr[9] = 995"
TRAP_89 = "arr[1] = 353"
TRAP_90 = "arr[7] = 542"
TRAP_91 = "arr[1] = 982"
TRAP_92 = "arr[9] = 466"
TRAP_93 = "arr[7] = 800"
TRAP_94 = "arr[1] = 404"
TRAP_95 = "arr[3] = 242"
TRAP_96 = "arr[3] = 528"
TRAP_97 = "arr[6] = 205"
TRAP_98 = "arr[7] = 884"
TRAP_99 = "arr[4] = 971"
TRAP_100 = "arr[2] = 170"
TRAP_101 = "arr[3] = 618"
TRAP_102 = "arr[4] = 477"
TRAP_103 = "arr[0] = 957"
TRAP_104 = "arr[2] = 717"
TRAP_105 = "arr[2] = 456"
TRAP_106 = "arr[6] = 436"
TRAP_107 = "arr[1] = 721"
TRAP_108 = "arr[1] = 903"
TRAP_109 = "arr[1] = 630"
TRAP_110 = "arr[2] = 382"
TRAP_111 = "arr[3] = 809"
TRAP_112 = "arr[2] = 482"
TRAP_113 = "arr[3] = 718"
TRAP_114 = "arr[0] = 532"
TRAP_115 = "arr[5] = 156"
TRAP_116 = "arr[1] = 636"
TRAP_117 = "arr[2] = 738"
TRAP_118 = "arr[3] = 749"
TRAP_119 = "arr[4] = 935"
TRAP_120 = "arr[2] = 879"
TRAP_121 = "arr[2] = 303"
TRAP_122 = "arr[5] = 502"
TRAP_123 = "arr[9] = 631"
TRAP_124 = "arr[6] = 474"
TRAP_125 = "arr[3] = 303"
TRAP_126 = "arr[3] = 615"
TRAP_127 = "arr[7] = 915"
TRAP_128 = "arr[4] = 489"
TRAP_129 = "arr[0] = 756"
TRAP_130 = "arr[2] = 557"
TRAP_131 = "arr[9] = 232"
TRAP_132 = "arr[8] = 104"
TRAP_133 = "arr[2] = 879"
TRAP_134 = "arr[7] = 331"
TRAP_135 = "arr[3] = 452"
TRAP_136 = "arr[0] = 580"
TRAP_137 = "arr[0] = 663"
TRAP_138 = "arr[3] = 766"
TRAP_139 = "arr[3] = 495"
TRAP_140 = "arr[7] = 412"
TRAP_141 = "arr[8] = 472"
TRAP_142 = "arr[3] = 781"
TRAP_143 = "arr[2] = 865"
TRAP_144 = "arr[5] = 982"
TRAP_145 = "arr[6] = 788"
TRAP_146 = "arr[9] = 455"
TRAP_147 = "arr[5] = 963"
TRAP_148 = "arr[8] = 609"
TRAP_149 = "arr[3] = 462"

arr = [1, 26, 28, 1, 26, 11, 29, 26, 1, 27]

copy_0 = arr[0]
code_1 = re.sub(r'[0-9]', '#', str(arr[9]))
code_2 = re.sub(r'[0-9]', '#', str(arr[2]))
note_3 = str(arr[0]) + str(arr[9])
code_4 = re.sub(r'[0-9]', '#', str(arr[8]))
code_5 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_6 = arr[6] + 30
tmp_7 = arr[1] + 6
code_8 = re.sub(r'[0-9]', '#', str(arr[3]))
note_9 = str(arr[8]) + str(arr[5])
tmp_10 = arr[8] + 6
note_11 = str(arr[0]) + str(arr[2])
note_12 = str(arr[4]) + str(arr[6])
note_13 = str(arr[1]) + str(arr[8])
note_14 = str(arr[5]) + str(arr[4])
tmp_15 = arr[4] + 9
copy_16 = arr[1]
copy_17 = arr[0]
note_18 = str(arr[3]) + str(arr[3])
tmp_19 = arr[1] + 8
note_20 = str(arr[4]) + str(arr[8])
copy_21 = arr[9]
note_22 = str(arr[3]) + str(arr[3])
note_23 = str(arr[6]) + str(arr[7])
copy_24 = arr[2]
note_25 = str(arr[2]) + str(arr[8])
tmp_26 = arr[4] + 13
tmp_27 = arr[3] + 43
tmp_28 = arr[5] + 39
tmp_29 = arr[7] + 44
copy_30 = arr[5]
copy_31 = arr[0]
note_32 = str(arr[2]) + str(arr[1])
tmp_33 = arr[3] + 22
note_34 = str(arr[8]) + str(arr[8])
copy_35 = arr[1]
note_36 = str(arr[3]) + str(arr[4])
tmp_37 = arr[4] + 11
tmp_38 = arr[8] + 45
copy_39 = arr[3]
note_40 = str(arr[6]) + str(arr[2])
note_41 = str(arr[3]) + str(arr[3])
note_42 = str(arr[7]) + str(arr[7])
note_43 = str(arr[3]) + str(arr[1])
tmp_44 = arr[0] + 47
code_45 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_46 = arr[7]
code_47 = re.sub(r'[0-9]', '#', str(arr[2]))
code_48 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_49 = arr[8]
code_50 = re.sub(r'[0-9]', '#', str(arr[6]))
code_51 = re.sub(r'[0-9]', '#', str(arr[0]))
label_52 = "запись 52 не применялась"
label_53 = "запись 53 не применялась"
tmp_54 = arr[4] + 22
label_55 = "запись 55 не применялась"
tmp_56 = arr[9] + 27
note_57 = str(arr[4]) + str(arr[6])
copy_58 = arr[1]
code_59 = re.sub(r'[0-9]', '#', str(arr[5]))
code_60 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_61 = arr[7] + 49
code_62 = re.sub(r'[0-9]', '#', str(arr[3]))
note_63 = str(arr[2]) + str(arr[3])
tmp_64 = arr[3] + 26
tmp_65 = arr[5] + 11
note_66 = str(arr[0]) + str(arr[0])
copy_67 = arr[1]
code_68 = re.sub(r'[0-9]', '#', str(arr[2]))
code_69 = re.sub(r'[0-9]', '#', str(arr[6]))
code_70 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_71 = arr[8]
code_72 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_73 = arr[0] + 34
note_74 = str(arr[6]) + str(arr[0])
copy_75 = arr[6]
note_76 = str(arr[7]) + str(arr[3])
note_77 = str(arr[0]) + str(arr[4])
code_78 = re.sub(r'[0-9]', '#', str(arr[1]))
note_79 = str(arr[5]) + str(arr[7])
tmp_80 = arr[7] + 12
tmp_81 = arr[1] + 36
copy_82 = arr[2]
tmp_83 = arr[7] + 13
note_84 = str(arr[7]) + str(arr[6])
code_85 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_86 = arr[0] + 30
copy_87 = arr[0]
label_88 = "запись 88 не применялась"
label_89 = "запись 89 не применялась"
copy_90 = arr[4]
copy_91 = arr[0]
note_92 = str(arr[8]) + str(arr[9])
label_93 = "запись 93 не применялась"
tmp_94 = arr[4] + 25
copy_95 = arr[4]
note_96 = str(arr[3]) + str(arr[3])
label_97 = "запись 97 не применялась"
code_98 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_99 = arr[3]
code_100 = re.sub(r'[0-9]', '#', str(arr[1]))
code_101 = re.sub(r'[0-9]', '#', str(arr[1]))
note_102 = str(arr[2]) + str(arr[5])
tmp_103 = arr[9] + 33
code_104 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_105 = arr[3] + 50
note_106 = str(arr[7]) + str(arr[0])
label_107 = "запись 107 не применялась"
copy_108 = arr[8]
copy_109 = arr[7]
code_110 = re.sub(r'[0-9]', '#', str(arr[2]))
code_111 = re.sub(r'[0-9]', '#', str(arr[4]))
code_112 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_113 = arr[3] + 25
note_114 = str(arr[5]) + str(arr[7])
code_115 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_116 = arr[8] + 12
code_117 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_118 = arr[4] + 13
code_119 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_120 = arr[3]
label_121 = "запись 121 не применялась"
tmp_122 = arr[4] + 23
note_123 = str(arr[7]) + str(arr[7])
note_124 = str(arr[4]) + str(arr[3])
label_125 = "запись 125 не применялась"
code_126 = re.sub(r'[0-9]', '#', str(arr[2]))
note_127 = str(arr[7]) + str(arr[3])
code_128 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_129 = arr[1] + 45
tmp_130 = arr[2] + 15
tmp_131 = arr[9] + 27
tmp_132 = arr[2] + 5
label_133 = "запись 133 не применялась"
code_134 = re.sub(r'[0-9]', '#', str(arr[6]))
note_135 = str(arr[7]) + str(arr[6])
tmp_136 = arr[7] + 29
copy_137 = arr[6]
code_138 = re.sub(r'[0-9]', '#', str(arr[9]))
label_139 = "запись 139 не применялась"
code_140 = re.sub(r'[0-9]', '#', str(arr[3]))
code_141 = re.sub(r'[0-9]', '#', str(arr[8]))
label_142 = "запись 142 не применялась"
note_143 = str(arr[7]) + str(arr[2])
label_144 = "запись 144 не применялась"
copy_145 = arr[8]
note_146 = str(arr[6]) + str(arr[2])
note_147 = str(arr[3]) + str(arr[0])
tmp_148 = arr[8] + 34
tmp_149 = arr[6] + 17
copy_150 = arr[3]
tmp_151 = arr[8] + 29
code_152 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_153 = arr[2] + 45
code_154 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_155 = arr[8] + 42
tmp_156 = arr[1] + 45
tmp_157 = arr[4] + 48
note_158 = str(arr[2]) + str(arr[3])
copy_159 = arr[5]
tmp_160 = arr[7] + 40
label_161 = "запись 161 не применялась"
tmp_162 = arr[2] + 31
copy_163 = arr[9]
label_164 = "запись 164 не применялась"
note_165 = str(arr[4]) + str(arr[3])
code_166 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_167 = arr[4]
tmp_168 = arr[4] + 48
copy_169 = arr[4]
tmp_170 = arr[1] + 26
copy_171 = arr[8]
tmp_172 = arr[8] + 22
tmp_173 = arr[2] + 2
tmp_174 = arr[1] + 38
note_175 = str(arr[4]) + str(arr[0])
tmp_176 = arr[2] + 28
note_177 = str(arr[1]) + str(arr[4])
label_178 = "запись 178 не применялась"
note_179 = str(arr[5]) + str(arr[1])
label_180 = "запись 180 не применялась"
code_181 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_182 = arr[0] + 22
note_183 = str(arr[0]) + str(arr[8])
copy_184 = arr[8]
code_185 = re.sub(r'[0-9]', '#', str(arr[2]))
label_186 = "запись 186 не применялась"
code_187 = re.sub(r'[0-9]', '#', str(arr[8]))
note_188 = str(arr[5]) + str(arr[1])
tmp_189 = arr[9] + 50
label_190 = "запись 190 не применялась"
label_191 = "запись 191 не применялась"
note_192 = str(arr[7]) + str(arr[2])
tmp_193 = arr[4] + 19
note_194 = str(arr[2]) + str(arr[4])
tmp_195 = arr[4] + 3
copy_196 = arr[0]
note_197 = str(arr[2]) + str(arr[2])
code_198 = re.sub(r'[0-9]', '#', str(arr[5]))
code_199 = re.sub(r'[0-9]', '#', str(arr[8]))
note_200 = str(arr[3]) + str(arr[4])
note_201 = str(arr[7]) + str(arr[3])
tmp_202 = arr[3] + 13
note_203 = str(arr[2]) + str(arr[5])
copy_204 = arr[8]
note_205 = str(arr[1]) + str(arr[1])
note_206 = str(arr[7]) + str(arr[2])
code_207 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_208 = arr[0] + 32
note_209 = str(arr[6]) + str(arr[9])
note_210 = str(arr[6]) + str(arr[0])
label_211 = "запись 211 не применялась"
label_212 = "запись 212 не применялась"
tmp_213 = arr[9] + 40
code_214 = re.sub(r'[0-9]', '#', str(arr[0]))
note_215 = str(arr[2]) + str(arr[4])
code_216 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_217 = arr[1] + 26
note_218 = str(arr[9]) + str(arr[2])
copy_219 = arr[6]
copy_220 = arr[4]
label_221 = "запись 221 не применялась"
note_222 = str(arr[9]) + str(arr[4])
label_223 = "запись 223 не применялась"
code_224 = re.sub(r'[0-9]', '#', str(arr[8]))
note_225 = str(arr[8]) + str(arr[1])
code_226 = re.sub(r'[0-9]', '#', str(arr[8]))
code_227 = re.sub(r'[0-9]', '#', str(arr[2]))
code_228 = re.sub(r'[0-9]', '#', str(arr[0]))
label_229 = "запись 229 не применялась"
note_230 = str(arr[8]) + str(arr[6])
copy_231 = arr[4]
tmp_232 = arr[3] + 39
label_233 = "запись 233 не применялась"
tmp_234 = arr[6] + 18
copy_235 = arr[2]
code_236 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_237 = arr[3]
code_238 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_239 = arr[9] + 36
code_240 = re.sub(r'[0-9]', '#', str(arr[7]))
note_241 = str(arr[6]) + str(arr[0])
code_242 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_243 = arr[8]
tmp_244 = arr[6] + 50
note_245 = str(arr[2]) + str(arr[8])
tmp_246 = arr[0] + 7
note_247 = str(arr[0]) + str(arr[5])
note_248 = str(arr[5]) + str(arr[7])
note_249 = str(arr[2]) + str(arr[5])
code_250 = re.sub(r'[0-9]', '#', str(arr[5]))
note_251 = str(arr[3]) + str(arr[3])
label_252 = "запись 252 не применялась"
code_253 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_254 = arr[0] + 16
tmp_255 = arr[1] + 41
copy_256 = arr[6]
code_257 = re.sub(r'[0-9]', '#', str(arr[5]))
note_258 = str(arr[1]) + str(arr[9])
code_259 = re.sub(r'[0-9]', '#', str(arr[6]))
code_260 = re.sub(r'[0-9]', '#', str(arr[7]))
label_261 = "запись 261 не применялась"
label_262 = "запись 262 не применялась"
copy_263 = arr[6]
tmp_264 = arr[2] + 36
copy_265 = arr[1]
code_266 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_267 = arr[5]
tmp_268 = arr[7] + 40
copy_269 = arr[9]
tmp_270 = arr[1] + 33
note_271 = str(arr[7]) + str(arr[2])
note_272 = str(arr[1]) + str(arr[6])
tmp_273 = arr[6] + 31
tmp_274 = arr[4] + 15
code_275 = re.sub(r'[0-9]', '#', str(arr[0]))
note_276 = str(arr[3]) + str(arr[9])
note_277 = str(arr[4]) + str(arr[6])
note_278 = str(arr[7]) + str(arr[8])
tmp_279 = arr[0] + 18
code_280 = re.sub(r'[0-9]', '#', str(arr[5]))
note_281 = str(arr[7]) + str(arr[8])
note_282 = str(arr[1]) + str(arr[0])
note_283 = str(arr[7]) + str(arr[2])
code_284 = re.sub(r'[0-9]', '#', str(arr[7]))
label_285 = "запись 285 не применялась"
tmp_286 = arr[0] + 34
label_287 = "запись 287 не применялась"
tmp_288 = arr[1] + 43
code_289 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_290 = arr[5]
note_291 = str(arr[3]) + str(arr[7])
tmp_292 = arr[2] + 26
tmp_293 = arr[0] + 49
code_294 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_295 = arr[9] + 43
label_296 = "запись 296 не применялась"
copy_297 = arr[6]
label_298 = "запись 298 не применялась"
tmp_299 = arr[3] + 17
note_300 = str(arr[7]) + str(arr[8])
label_301 = "запись 301 не применялась"
tmp_302 = arr[5] + 19
label_303 = "запись 303 не применялась"
tmp_304 = arr[6] + 30
code_305 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_306 = arr[8]
tmp_307 = arr[9] + 49
note_308 = str(arr[7]) + str(arr[0])
code_309 = re.sub(r'[0-9]', '#', str(arr[6]))
label_310 = "запись 310 не применялась"
label_311 = "запись 311 не применялась"
code_312 = re.sub(r'[0-9]', '#', str(arr[0]))
note_313 = str(arr[3]) + str(arr[5])
code_314 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_315 = arr[6]
tmp_316 = arr[5] + 48
tmp_317 = arr[7] + 7
code_318 = re.sub(r'[0-9]', '#', str(arr[5]))
note_319 = str(arr[1]) + str(arr[1])
copy_320 = arr[0]
tmp_321 = arr[9] + 8
note_322 = str(arr[7]) + str(arr[5])
tmp_323 = arr[6] + 18
note_324 = str(arr[5]) + str(arr[0])
tmp_325 = arr[4] + 36
note_326 = str(arr[6]) + str(arr[1])
tmp_327 = arr[1] + 27
tmp_328 = arr[2] + 44
note_329 = str(arr[2]) + str(arr[3])
tmp_330 = arr[1] + 15
note_331 = str(arr[2]) + str(arr[9])
code_332 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_333 = arr[6] + 31
note_334 = str(arr[2]) + str(arr[3])
label_335 = "запись 335 не применялась"
code_336 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_337 = arr[8] + 36
code_338 = re.sub(r'[0-9]', '#', str(arr[0]))
code_339 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_340 = arr[3] + 29
copy_341 = arr[9]
code_342 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_343 = arr[4] + 2
copy_344 = arr[7]
copy_345 = arr[6]
tmp_346 = arr[6] + 14
copy_347 = arr[8]
label_348 = "запись 348 не применялась"
tmp_349 = arr[8] + 9
tmp_350 = arr[0] + 33
label_351 = "запись 351 не применялась"
tmp_352 = arr[8] + 20
note_353 = str(arr[2]) + str(arr[3])
note_354 = str(arr[4]) + str(arr[0])
label_355 = "запись 355 не применялась"
note_356 = str(arr[5]) + str(arr[9])
code_357 = re.sub(r'[0-9]', '#', str(arr[9]))
note_358 = str(arr[9]) + str(arr[4])
note_359 = str(arr[0]) + str(arr[2])
label_360 = "запись 360 не применялась"
code_361 = re.sub(r'[0-9]', '#', str(arr[5]))
note_362 = str(arr[6]) + str(arr[8])
tmp_363 = arr[6] + 24
tmp_364 = arr[3] + 10
copy_365 = arr[3]
note_366 = str(arr[6]) + str(arr[7])
code_367 = re.sub(r'[0-9]', '#', str(arr[1]))
note_368 = str(arr[1]) + str(arr[1])
tmp_369 = arr[8] + 2
code_370 = re.sub(r'[0-9]', '#', str(arr[2]))
note_371 = str(arr[8]) + str(arr[2])
tmp_372 = arr[7] + 22
note_373 = str(arr[1]) + str(arr[0])
copy_374 = arr[5]
note_375 = str(arr[4]) + str(arr[5])
tmp_376 = arr[4] + 43
tmp_377 = arr[9] + 27
code_378 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_379 = arr[8]
copy_380 = arr[9]
code_381 = re.sub(r'[0-9]', '#', str(arr[3]))
note_382 = str(arr[2]) + str(arr[4])
tmp_383 = arr[2] + 6
tmp_384 = arr[1] + 16
code_385 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_386 = arr[2]
code_387 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_388 = arr[4] + 8
label_389 = "запись 389 не применялась"
note_390 = str(arr[9]) + str(arr[7])
copy_391 = arr[6]
copy_392 = arr[2]
tmp_393 = arr[8] + 37
label_394 = "запись 394 не применялась"
code_395 = re.sub(r'[0-9]', '#', str(arr[5]))
code_396 = re.sub(r'[0-9]', '#', str(arr[6]))
code_397 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_398 = arr[8]
tmp_399 = arr[4] + 40
note_400 = str(arr[9]) + str(arr[2])
code_401 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_402 = arr[0] + 36
note_403 = str(arr[7]) + str(arr[2])
note_404 = str(arr[2]) + str(arr[5])
copy_405 = arr[5]
code_406 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_407 = arr[7] + 33
label_408 = "запись 408 не применялась"
label_409 = "запись 409 не применялась"
tmp_410 = arr[3] + 3
label_411 = "запись 411 не применялась"
note_412 = str(arr[9]) + str(arr[6])
tmp_413 = arr[7] + 24
note_414 = str(arr[4]) + str(arr[0])
code_415 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_416 = arr[7] + 19
note_417 = str(arr[0]) + str(arr[1])
label_418 = "запись 418 не применялась"
tmp_419 = arr[5] + 18
note_420 = str(arr[6]) + str(arr[1])
tmp_421 = arr[0] + 15
code_422 = re.sub(r'[0-9]', '#', str(arr[7]))
note_423 = str(arr[9]) + str(arr[5])
code_424 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_425 = arr[2] + 33
label_426 = "запись 426 не применялась"
note_427 = str(arr[8]) + str(arr[7])
note_428 = str(arr[7]) + str(arr[5])
label_429 = "запись 429 не применялась"
code_430 = re.sub(r'[0-9]', '#', str(arr[8]))
code_431 = re.sub(r'[0-9]', '#', str(arr[9]))
note_432 = str(arr[3]) + str(arr[3])
code_433 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_434 = arr[5] + 36
code_435 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_436 = arr[7] + 2
copy_437 = arr[3]
tmp_438 = arr[9] + 18
label_439 = "запись 439 не применялась"
tmp_440 = arr[3] + 24
tmp_441 = arr[7] + 39
label_442 = "запись 442 не применялась"
note_443 = str(arr[8]) + str(arr[6])
tmp_444 = arr[2] + 20
note_445 = str(arr[3]) + str(arr[8])
code_446 = re.sub(r'[0-9]', '#', str(arr[2]))
code_447 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_448 = arr[8] + 3
tmp_449 = arr[7] + 14
note_450 = str(arr[5]) + str(arr[6])
code_451 = re.sub(r'[0-9]', '#', str(arr[5]))
code_452 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_453 = arr[6] + 41
copy_454 = arr[5]
copy_455 = arr[2]
note_456 = str(arr[9]) + str(arr[1])
tmp_457 = arr[7] + 34
code_458 = re.sub(r'[0-9]', '#', str(arr[5]))
note_459 = str(arr[0]) + str(arr[4])
tmp_460 = arr[7] + 43
tmp_461 = arr[0] + 23
tmp_462 = arr[4] + 29
code_463 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_464 = arr[0] + 31
note_465 = str(arr[6]) + str(arr[8])
note_466 = str(arr[3]) + str(arr[1])
code_467 = re.sub(r'[0-9]', '#', str(arr[7]))
label_468 = "запись 468 не применялась"
code_469 = re.sub(r'[0-9]', '#', str(arr[0]))
code_470 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_471 = arr[3] + 27
tmp_472 = arr[8] + 2
note_473 = str(arr[6]) + str(arr[5])
tmp_474 = arr[4] + 20
note_475 = str(arr[8]) + str(arr[0])
note_476 = str(arr[8]) + str(arr[9])
tmp_477 = arr[5] + 49
label_478 = "запись 478 не применялась"
note_479 = str(arr[1]) + str(arr[8])
tmp_480 = arr[6] + 5
code_481 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_482 = arr[7]
copy_483 = arr[2]
copy_484 = arr[3]
tmp_485 = arr[0] + 28
label_486 = "запись 486 не применялась"
tmp_487 = arr[2] + 46
tmp_488 = arr[4] + 40
code_489 = re.sub(r'[0-9]', '#', str(arr[5]))
code_490 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_491 = arr[2] + 29
code_492 = re.sub(r'[0-9]', '#', str(arr[0]))
note_493 = str(arr[5]) + str(arr[7])
note_494 = str(arr[8]) + str(arr[0])
code_495 = re.sub(r'[0-9]', '#', str(arr[5]))
label_496 = "запись 496 не применялась"
note_497 = str(arr[2]) + str(arr[9])
copy_498 = arr[2]
note_499 = str(arr[7]) + str(arr[8])
tmp_500 = arr[6] + 24
tmp_501 = arr[0] + 30
copy_502 = arr[0]
note_503 = str(arr[0]) + str(arr[9])
note_504 = str(arr[1]) + str(arr[4])
tmp_505 = arr[6] + 43
code_506 = re.sub(r'[0-9]', '#', str(arr[3]))
code_507 = re.sub(r'[0-9]', '#', str(arr[2]))
label_508 = "запись 508 не применялась"
tmp_509 = arr[2] + 32
note_510 = str(arr[3]) + str(arr[0])
label_511 = "запись 511 не применялась"
tmp_512 = arr[1] + 23
note_513 = str(arr[4]) + str(arr[4])
note_514 = str(arr[8]) + str(arr[2])
code_515 = re.sub(r'[0-9]', '#', str(arr[3]))
code_516 = re.sub(r'[0-9]', '#', str(arr[8]))
code_517 = re.sub(r'[0-9]', '#', str(arr[0]))
note_518 = str(arr[7]) + str(arr[4])
label_519 = "запись 519 не применялась"
code_520 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_521 = arr[4]
code_522 = re.sub(r'[0-9]', '#', str(arr[4]))
note_523 = str(arr[6]) + str(arr[1])
tmp_524 = arr[6] + 34
tmp_525 = arr[9] + 29
copy_526 = arr[5]
note_527 = str(arr[0]) + str(arr[5])
tmp_528 = arr[3] + 45
label_529 = "запись 529 не применялась"
code_530 = re.sub(r'[0-9]', '#', str(arr[7]))
note_531 = str(arr[4]) + str(arr[1])
copy_532 = arr[1]
note_533 = str(arr[3]) + str(arr[4])
note_534 = str(arr[1]) + str(arr[2])
note_535 = str(arr[0]) + str(arr[3])
tmp_536 = arr[7] + 37
note_537 = str(arr[0]) + str(arr[0])
code_538 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_539 = arr[2] + 44
code_540 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_541 = arr[9]
code_542 = re.sub(r'[0-9]', '#', str(arr[7]))
note_543 = str(arr[7]) + str(arr[5])
note_544 = str(arr[4]) + str(arr[3])
copy_545 = arr[4]
copy_546 = arr[2]
tmp_547 = arr[0] + 34
code_548 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_549 = arr[7]
note_550 = str(arr[1]) + str(arr[6])
label_551 = "запись 551 не применялась"
tmp_552 = arr[0] + 45
copy_553 = arr[0]
copy_554 = arr[6]
note_555 = str(arr[0]) + str(arr[7])
copy_556 = arr[0]
label_557 = "запись 557 не применялась"
copy_558 = arr[2]
note_559 = str(arr[0]) + str(arr[0])
copy_560 = arr[4]
note_561 = str(arr[8]) + str(arr[3])
tmp_562 = arr[0] + 38
label_563 = "запись 563 не применялась"
note_564 = str(arr[5]) + str(arr[0])
code_565 = re.sub(r'[0-9]', '#', str(arr[9]))
note_566 = str(arr[5]) + str(arr[0])
code_567 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_568 = arr[2] + 20
note_569 = str(arr[1]) + str(arr[9])
code_570 = re.sub(r'[0-9]', '#', str(arr[4]))
note_571 = str(arr[3]) + str(arr[6])
label_572 = "запись 572 не применялась"
code_573 = re.sub(r'[0-9]', '#', str(arr[7]))
code_574 = re.sub(r'[0-9]', '#', str(arr[7]))
label_575 = "запись 575 не применялась"
code_576 = re.sub(r'[0-9]', '#', str(arr[7]))
label_577 = "запись 577 не применялась"
tmp_578 = arr[4] + 27
copy_579 = arr[7]
tmp_580 = arr[7] + 49
copy_581 = arr[7]
copy_582 = arr[3]
tmp_583 = arr[9] + 46
tmp_584 = arr[3] + 42
note_585 = str(arr[7]) + str(arr[7])
copy_586 = arr[4]
code_587 = re.sub(r'[0-9]', '#', str(arr[7]))
code_588 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_589 = arr[5] + 11
tmp_590 = arr[0] + 4
note_591 = str(arr[1]) + str(arr[3])
tmp_592 = arr[6] + 31
label_593 = "запись 593 не применялась"
code_594 = re.sub(r'[0-9]', '#', str(arr[3]))
note_595 = str(arr[3]) + str(arr[1])
label_596 = "запись 596 не применялась"
tmp_597 = arr[1] + 30
note_598 = str(arr[9]) + str(arr[1])
note_599 = str(arr[6]) + str(arr[3])
note_600 = str(arr[9]) + str(arr[8])
code_601 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_602 = arr[2] + 40
code_603 = re.sub(r'[0-9]', '#', str(arr[1]))
label_604 = "запись 604 не применялась"
tmp_605 = arr[6] + 41
tmp_606 = arr[1] + 32
note_607 = str(arr[2]) + str(arr[9])
tmp_608 = arr[7] + 10
tmp_609 = arr[7] + 37
label_610 = "запись 610 не применялась"
tmp_611 = arr[0] + 34
tmp_612 = arr[5] + 33
tmp_613 = arr[8] + 21
tmp_614 = arr[4] + 40
label_615 = "запись 615 не применялась"
copy_616 = arr[5]
code_617 = re.sub(r'[0-9]', '#', str(arr[4]))
code_618 = re.sub(r'[0-9]', '#', str(arr[8]))
note_619 = str(arr[0]) + str(arr[4])
copy_620 = arr[7]
tmp_621 = arr[8] + 43
copy_622 = arr[5]
label_623 = "запись 623 не применялась"
note_624 = str(arr[9]) + str(arr[7])
note_625 = str(arr[1]) + str(arr[5])
code_626 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_627 = arr[3] + 10
label_628 = "запись 628 не применялась"
code_629 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_630 = arr[4] + 17
tmp_631 = arr[7] + 10
note_632 = str(arr[0]) + str(arr[9])
note_633 = str(arr[9]) + str(arr[9])
copy_634 = arr[6]
code_635 = re.sub(r'[0-9]', '#', str(arr[6]))
code_636 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_637 = arr[9]
note_638 = str(arr[8]) + str(arr[0])
tmp_639 = arr[3] + 37
note_640 = str(arr[4]) + str(arr[2])
tmp_641 = arr[6] + 25
label_642 = "запись 642 не применялась"
tmp_643 = arr[7] + 41
tmp_644 = arr[7] + 50
tmp_645 = arr[3] + 8
label_646 = "запись 646 не применялась"
tmp_647 = arr[7] + 45
code_648 = re.sub(r'[0-9]', '#', str(arr[9]))
code_649 = re.sub(r'[0-9]', '#', str(arr[2]))
code_650 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_651 = arr[4] + 45
copy_652 = arr[9]
note_653 = str(arr[1]) + str(arr[5])
tmp_654 = arr[0] + 40
note_655 = str(arr[3]) + str(arr[1])
copy_656 = arr[3]
note_657 = str(arr[1]) + str(arr[4])
copy_658 = arr[7]
label_659 = "запись 659 не применялась"
note_660 = str(arr[5]) + str(arr[7])
label_661 = "запись 661 не применялась"
label_662 = "запись 662 не применялась"
code_663 = re.sub(r'[0-9]', '#', str(arr[0]))
label_664 = "запись 664 не применялась"
code_665 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_666 = arr[1] + 44
tmp_667 = arr[7] + 43
code_668 = re.sub(r'[0-9]', '#', str(arr[5]))
label_669 = "запись 669 не применялась"
code_670 = re.sub(r'[0-9]', '#', str(arr[1]))
note_671 = str(arr[4]) + str(arr[4])
code_672 = re.sub(r'[0-9]', '#', str(arr[0]))
note_673 = str(arr[3]) + str(arr[3])
code_674 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_675 = arr[8]
note_676 = str(arr[4]) + str(arr[7])
tmp_677 = arr[7] + 34
tmp_678 = arr[8] + 19
copy_679 = arr[2]
tmp_680 = arr[0] + 4
label_681 = "запись 681 не применялась"
code_682 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_683 = arr[0] + 48
note_684 = str(arr[4]) + str(arr[6])
note_685 = str(arr[6]) + str(arr[7])
note_686 = str(arr[1]) + str(arr[3])
note_687 = str(arr[3]) + str(arr[0])
note_688 = str(arr[5]) + str(arr[0])
label_689 = "запись 689 не применялась"
copy_690 = arr[7]
note_691 = str(arr[6]) + str(arr[7])
note_692 = str(arr[7]) + str(arr[3])
code_693 = re.sub(r'[0-9]', '#', str(arr[3]))
note_694 = str(arr[0]) + str(arr[8])
copy_695 = arr[0]
code_696 = re.sub(r'[0-9]', '#', str(arr[6]))
label_697 = "запись 697 не применялась"
tmp_698 = arr[4] + 40
note_699 = str(arr[1]) + str(arr[3])
note_700 = str(arr[5]) + str(arr[3])
note_701 = str(arr[8]) + str(arr[4])
copy_702 = arr[9]
tmp_703 = arr[8] + 38
tmp_704 = arr[2] + 44
note_705 = str(arr[5]) + str(arr[0])
copy_706 = arr[8]
copy_707 = arr[2]
note_708 = str(arr[6]) + str(arr[4])
tmp_709 = arr[6] + 36
code_710 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_711 = arr[2] + 3
copy_712 = arr[9]
code_713 = re.sub(r'[0-9]', '#', str(arr[1]))
code_714 = re.sub(r'[0-9]', '#', str(arr[2]))
code_715 = re.sub(r'[0-9]', '#', str(arr[2]))
code_716 = re.sub(r'[0-9]', '#', str(arr[9]))
code_717 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_718 = arr[5]
note_719 = str(arr[3]) + str(arr[2])
tmp_720 = arr[5] + 8
note_721 = str(arr[9]) + str(arr[7])
copy_722 = arr[7]
code_723 = re.sub(r'[0-9]', '#', str(arr[8]))
note_724 = str(arr[7]) + str(arr[0])
copy_725 = arr[4]
code_726 = re.sub(r'[0-9]', '#', str(arr[8]))
code_727 = re.sub(r'[0-9]', '#', str(arr[5]))
label_728 = "запись 728 не применялась"
copy_729 = arr[7]
copy_730 = arr[8]
note_731 = str(arr[1]) + str(arr[5])
code_732 = re.sub(r'[0-9]', '#', str(arr[1]))
code_733 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_734 = arr[7]
label_735 = "запись 735 не применялась"
code_736 = re.sub(r'[0-9]', '#', str(arr[8]))
label_737 = "запись 737 не применялась"
tmp_738 = arr[4] + 31
tmp_739 = arr[2] + 11
tmp_740 = arr[1] + 26
note_741 = str(arr[2]) + str(arr[2])
code_742 = re.sub(r'[0-9]', '#', str(arr[8]))
code_743 = re.sub(r'[0-9]', '#', str(arr[5]))
note_744 = str(arr[5]) + str(arr[6])
copy_745 = arr[3]
note_746 = str(arr[9]) + str(arr[2])
note_747 = str(arr[6]) + str(arr[9])
tmp_748 = arr[4] + 19
note_749 = str(arr[6]) + str(arr[9])
tmp_750 = arr[7] + 31
label_751 = "запись 751 не применялась"
note_752 = str(arr[0]) + str(arr[0])
code_753 = re.sub(r'[0-9]', '#', str(arr[0]))
label_754 = "запись 754 не применялась"
copy_755 = arr[9]
copy_756 = arr[2]
code_757 = re.sub(r'[0-9]', '#', str(arr[5]))
note_758 = str(arr[1]) + str(arr[7])
tmp_759 = arr[7] + 43
copy_760 = arr[3]
tmp_761 = arr[9] + 39
copy_762 = arr[5]
note_763 = str(arr[9]) + str(arr[4])
tmp_764 = arr[2] + 39
code_765 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_766 = arr[3]
tmp_767 = arr[6] + 41
tmp_768 = arr[9] + 45
tmp_769 = arr[3] + 35
code_770 = re.sub(r'[0-9]', '#', str(arr[5]))
note_771 = str(arr[4]) + str(arr[8])
copy_772 = arr[8]
label_773 = "запись 773 не применялась"
note_774 = str(arr[4]) + str(arr[7])
tmp_775 = arr[2] + 31
tmp_776 = arr[1] + 38
note_777 = str(arr[1]) + str(arr[0])
tmp_778 = arr[1] + 34
copy_779 = arr[9]
copy_780 = arr[1]
copy_781 = arr[7]
code_782 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_783 = arr[5] + 14
tmp_784 = arr[0] + 19
code_785 = re.sub(r'[0-9]', '#', str(arr[1]))
code_786 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_787 = arr[8]
code_788 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_789 = arr[6] + 25
tmp_790 = arr[6] + 8
tmp_791 = arr[1] + 3
label_792 = "запись 792 не применялась"
tmp_793 = arr[5] + 5
tmp_794 = arr[3] + 41
copy_795 = arr[9]
label_796 = "запись 796 не применялась"
code_797 = re.sub(r'[0-9]', '#', str(arr[2]))
code_798 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_799 = arr[2] + 21

arr[0] = acc(arr, 7) % 100
# архив: запись 748 обработана, изменений нет
# справка: запись 33 обработана, изменений нет
# ревизия: запись 35 обработана, изменений нет
# замечание: arr[5] *= 69 — не выполняется
# пометка: arr2[0] = 60 — не выполняется
# замечание: arr2[2] = 17 — не выполняется
# замечание: arr2[4] = 14 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr[2] *= 67 — не выполняется
# архив: запись 1 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr2[6] = 67 — не выполняется
# архив: запись 326 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# пометка: arr[2] += 44 — не выполняется
# временная запись: arr[0] = 95 — не выполняется
# справка: запись 16 обработана, изменений нет
# временная запись: запись 420 обработана, изменений нет
# временная запись: запись 600 обработана, изменений нет
# черновик: arr[4] += 6 — не выполняется
# замечание: запись 933 обработана, изменений нет
# архив: запись 95 обработана, изменений нет
# справка: запись 912 обработана, изменений нет
# замечание: arr2[1] = 62 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 90 обработана, изменений нет
# примечание: запись 52 обработана, изменений нет
# пометка: запись 886 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: запись 499 обработана, изменений нет
# примечание: запись 555 обработана, изменений нет
# черновик: arr[9] += 4 — не выполняется
# ревизия: arr[5] = 85 — не выполняется
# справка: запись 585 обработана, изменений нет
# справка: запись 551 обработана, изменений нет
# отладка: arr[9] += 74 — не выполняется
# пометка: arr[7] += 87 — не выполняется
# справка: запись 255 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 983 обработана, изменений нет
# архив: arr[3] *= 74 — не выполняется
# черновик: arr[5] *= 57 — не выполняется
# замечание: arr2[1] = 76 — не выполняется
# проверено: запись 233 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: запись 172 обработана, изменений нет
# справка: запись 634 обработана, изменений нет
# черновик: arr[7] *= 46 — не выполняется
# архив: запись 472 обработана, изменений нет
# ревизия: arr[0] = 61 — не выполняется
# замечание: arr[0] += 27 — не выполняется
# справка: запись 370 обработана, изменений нет
# проверено: arr[9] += 16 — не выполняется
# отладка: arr2[1] = 54 — не выполняется
# примечание: arr2[7] = 68 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[5] = 11 — не выполняется
# ревизия: запись 641 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# проверено: arr[3] = 60 — не выполняется
# ревизия: arr[8] *= 10 — не выполняется
# ревизия: запись 722 обработана, изменений нет
# ревизия: arr2[3] = 60 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[1] += 10 — не выполняется
# пометка: запись 788 обработана, изменений нет
# отладка: arr[3] = 86 — не выполняется
# ревизия: запись 69 обработана, изменений нет
# пометка: запись 928 обработана, изменений нет
# справка: arr[5] += 59 — не выполняется
# замечание: arr[1] = 78 — не выполняется
# архив: запись 198 обработана, изменений нет
# архив: arr[6] *= 7 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr[1] += 93 — не выполняется
# пометка: запись 226 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: запись 725 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[0] *= 21 — не выполняется
# пометка: arr2[8] = 74 — не выполняется
# справка: arr[3] += 27 — не выполняется
# пометка: arr[2] *= 75 — не выполняется
# черновик: arr[4] *= 46 — не выполняется
# примечание: запись 544 обработана, изменений нет
# справка: запись 473 обработана, изменений нет
# архив: запись 54 обработана, изменений нет
# черновик: запись 21 обработана, изменений нет
# временная запись: arr[7] *= 98 — не выполняется
# отладка: запись 834 обработана, изменений нет
# временная запись: запись 404 обработана, изменений нет
# временная запись: запись 882 обработана, изменений нет
# ревизия: запись 382 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# примечание: запись 586 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# пометка: запись 402 обработана, изменений нет
# проверено: arr[7] += 83 — не выполняется
# проверено: arr[3] = 72 — не выполняется
# замечание: arr[6] += 15 — не выполняется
# примечание: запись 796 обработана, изменений нет
# пометка: запись 172 обработана, изменений нет
# замечание: запись 787 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# архив: запись 593 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# отладка: arr[1] *= 50 — не выполняется
# замечание: запись 385 обработана, изменений нет
# пометка: arr[4] += 11 — не выполняется
# отладка: запись 40 обработана, изменений нет
# черновик: запись 349 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# отладка: запись 950 обработана, изменений нет
# проверено: arr2[6] = 14 — не выполняется
# отладка: запись 558 обработана, изменений нет
# ревизия: arr2[3] = 55 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 804 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# временная запись: arr[8] += 82 — не выполняется
# черновик: arr2[7] = 30 — не выполняется
# примечание: arr[7] = 17 — не выполняется
# примечание: arr2[3] = 53 — не выполняется
# ревизия: запись 493 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# отладка: запись 786 обработана, изменений нет
# отладка: запись 669 обработана, изменений нет
# проверено: запись 583 обработана, изменений нет
# примечание: запись 629 обработана, изменений нет
# проверено: arr[5] *= 62 — не выполняется
# архив: arr[8] = 49 — не выполняется
# временная запись: arr[1] = 54 — не выполняется
# черновик: arr2[0] = 26 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 692 обработана, изменений нет
# замечание: запись 975 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 474 обработана, изменений нет
# справка: arr[7] = 99 — не выполняется
# замечание: запись 457 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# ревизия: arr[2] += 31 — не выполняется
# замечание: arr2[0] = 91 — не выполняется
# архив: arr[2] *= 64 — не выполняется
# временная запись: запись 638 обработана, изменений нет
# пометка: arr[4] += 55 — не выполняется
# архив: запись 296 обработана, изменений нет
# замечание: запись 473 обработана, изменений нет
# проверено: запись 306 обработана, изменений нет
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[4] += 16 — не выполняется
# пометка: arr[2] += 25 — не выполняется
# отладка: arr2[1] = 54 — не выполняется
# проверено: запись 287 обработана, изменений нет
# отладка: arr[2] = 70 — не выполняется
# замечание: arr[0] = 26 — не выполняется
# замечание: запись 156 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# отладка: arr2[7] = 53 — не выполняется
# проверено: запись 37 обработана, изменений нет
# временная запись: запись 932 обработана, изменений нет
# архив: запись 840 обработана, изменений нет
# ревизия: запись 348 обработана, изменений нет
# проверено: запись 197 обработана, изменений нет
# отладка: arr[2] = 55 — не выполняется
# временная запись: arr[5] *= 89 — не выполняется
# примечание: arr[8] += 81 — не выполняется
# архив: arr[6] *= 76 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 478 обработана, изменений нет
# примечание: запись 546 обработана, изменений нет
# справка: arr[5] = 57 — не выполняется
# временная запись: arr2[8] = 57 — не выполняется
# примечание: запись 916 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 836 обработана, изменений нет
# отладка: запись 642 обработана, изменений нет
# отладка: запись 353 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# ревизия: запись 98 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# проверено: запись 769 обработана, изменений нет
# пометка: arr2[0] = 53 — не выполняется
# ревизия: запись 181 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# пометка: arr2[9] = 63 — не выполняется
# справка: запись 994 обработана, изменений нет
# ревизия: запись 776 обработана, изменений нет
# справка: запись 346 обработана, изменений нет
# замечание: arr[9] *= 55 — не выполняется
# примечание: запись 135 обработана, изменений нет
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 845 обработана, изменений нет
# временная запись: arr[9] += 96 — не выполняется
# отладка: arr2[8] = 57 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr[7] *= 95 — не выполняется
# справка: запись 241 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# архив: запись 872 обработана, изменений нет
# временная запись: arr[9] = 66 — не выполняется
# пометка: arr[6] += 25 — не выполняется
# архив: arr2[7] = 63 — не выполняется
# архив: arr2[3] = 7 — не выполняется
# замечание: запись 426 обработана, изменений нет
# замечание: запись 431 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# отладка: arr[6] += 89 — не выполняется
# справка: запись 814 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# пометка: arr[7] *= 9 — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[1] = 42 — не выполняется
# пометка: запись 358 обработана, изменений нет
# отладка: запись 921 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# справка: запись 378 обработана, изменений нет
# временная запись: запись 660 обработана, изменений нет
# ревизия: arr[7] += 51 — не выполняется
# черновик: arr[1] *= 84 — не выполняется
# замечание: запись 853 обработана, изменений нет
# отладка: arr2[1] = 16 — не выполняется
# ревизия: arr[5] += 52 — не выполняется
# черновик: arr[2] *= 55 — не выполняется
# архив: запись 664 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# черновик: запись 265 обработана, изменений нет
# черновик: запись 380 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# справка: запись 727 обработана, изменений нет
# пометка: запись 507 обработана, изменений нет
# отладка: arr[8] = 35 — не выполняется
# ревизия: запись 542 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[5] *= 6 — не выполняется
# черновик: запись 558 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# замечание: arr[2] = 89 — не выполняется
# примечание: запись 889 обработана, изменений нет
# архив: arr[9] *= 83 — не выполняется
# проверено: запись 534 обработана, изменений нет
# отладка: arr[6] = 57 — не выполняется
# черновик: arr2[2] = 77 — не выполняется
# временная запись: запись 565 обработана, изменений нет
# черновик: запись 123 обработана, изменений нет
# временная запись: запись 267 обработана, изменений нет
# проверено: arr2[9] = 44 — не выполняется
# примечание: запись 259 обработана, изменений нет
# временная запись: arr[4] += 18 — не выполняется
# временная запись: запись 96 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr[0] *= 59 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 928 обработана, изменений нет
# черновик: запись 690 обработана, изменений нет
# архив: запись 515 обработана, изменений нет
# справка: arr[2] += 87 — не выполняется
# пометка: arr[9] += 26 — не выполняется
# ревизия: запись 105 обработана, изменений нет
# архив: запись 5 обработана, изменений нет
# ревизия: arr2[3] = 8 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr2[0] = 67 — не выполняется
# пометка: запись 84 обработана, изменений нет
# проверено: arr[2] += 28 — не выполняется
# пометка: запись 984 обработана, изменений нет
# пометка: arr[0] *= 17 — не выполняется
# архив: запись 903 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[3] += 46 — не выполняется
# временная запись: запись 917 обработана, изменений нет
# черновик: запись 834 обработана, изменений нет
# черновик: запись 137 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr2[9] = 25 — не выполняется
# пометка: arr[4] *= 97 — не выполняется
# ревизия: arr[9] = 28 — не выполняется
# архив: запись 475 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# ревизия: запись 446 обработана, изменений нет
# пометка: запись 413 обработана, изменений нет
# отладка: arr[4] *= 73 — не выполняется
# архив: arr[1] = 13 — не выполняется
# временная запись: запись 5 обработана, изменений нет
# временная запись: запись 599 обработана, изменений нет
# ревизия: arr[2] += 25 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 598 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# ревизия: arr[9] *= 18 — не выполняется
# ревизия: запись 304 обработана, изменений нет
# временная запись: arr[3] *= 63 — не выполняется
# отладка: запись 802 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# примечание: запись 875 обработана, изменений нет
# проверено: arr2[3] = 40 — не выполняется
# примечание: arr[7] *= 39 — не выполняется
# примечание: arr[3] *= 65 — не выполняется
# временная запись: запись 871 обработана, изменений нет
# ревизия: запись 176 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: запись 759 обработана, изменений нет
# замечание: запись 950 обработана, изменений нет
# черновик: запись 639 обработана, изменений нет
# ревизия: запись 886 обработана, изменений нет
# примечание: arr[8] = 18 — не выполняется
# временная запись: arr[4] *= 15 — не выполняется
# проверено: запись 205 обработана, изменений нет
# справка: arr[2] = 4 — не выполняется
# черновик: arr[5] *= 50 — не выполняется
# отладка: arr[3] = 55 — не выполняется
# замечание: arr[4] = 12 — не выполняется
# замечание: arr[5] *= 68 — не выполняется
# пометка: запись 408 обработана, изменений нет
# проверено: запись 401 обработана, изменений нет
# справка: arr2[4] = 42 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 517 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: arr2[5] = 82 — не выполняется
# пометка: arr[5] += 85 — не выполняется
# проверено: запись 572 обработана, изменений нет
# отладка: arr2[9] = 66 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 501 обработана, изменений нет
# ревизия: arr2[5] = 24 — не выполняется
# черновик: arr2[1] = 33 — не выполняется
# временная запись: запись 213 обработана, изменений нет
# примечание: запись 17 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr2[8] = 10 — не выполняется
# проверено: запись 268 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# черновик: запись 653 обработана, изменений нет
# отладка: запись 578 обработана, изменений нет
# справка: arr[8] *= 3 — не выполняется
# замечание: запись 714 обработана, изменений нет
# примечание: arr[6] *= 59 — не выполняется
# замечание: запись 420 обработана, изменений нет
# примечание: запись 918 обработана, изменений нет
# справка: arr[5] = 53 — не выполняется
# архив: arr2[9] = 99 — не выполняется
# ревизия: запись 152 обработана, изменений нет
# черновик: arr[0] = 35 — не выполняется
# примечание: запись 782 обработана, изменений нет
arr[0:3] = sorted(arr[0:3])
# примечание: запись 970 обработана, изменений нет
# справка: arr2[4] = 16 — не выполняется
# архив: запись 995 обработана, изменений нет
# справка: arr[3] = 76 — не выполняется
# примечание: запись 126 обработана, изменений нет
# отладка: запись 575 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# замечание: запись 967 обработана, изменений нет
# отладка: arr[7] = 39 — не выполняется
# замечание: arr2[3] = 10 — не выполняется
# справка: arr[0] = 93 — не выполняется
# пометка: arr[3] = 95 — не выполняется
# черновик: запись 470 обработана, изменений нет
# проверено: arr[5] += 34 — не выполняется
# архив: запись 215 обработана, изменений нет
# примечание: arr[3] += 92 — не выполняется
# временная запись: arr[4] += 53 — не выполняется
# пометка: запись 460 обработана, изменений нет
# временная запись: запись 259 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: запись 459 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[8] += 56 — не выполняется
# временная запись: arr[9] += 66 — не выполняется
# пометка: запись 56 обработана, изменений нет
# проверено: запись 902 обработана, изменений нет
# ревизия: arr2[5] = 84 — не выполняется
# замечание: arr[5] += 55 — не выполняется
# справка: arr[5] += 64 — не выполняется
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr2[0] = 58 — не выполняется
# черновик: запись 664 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: запись 477 обработана, изменений нет
# архив: arr[2] += 47 — не выполняется
# примечание: arr[4] *= 69 — не выполняется
# примечание: запись 473 обработана, изменений нет
# черновик: запись 868 обработана, изменений нет
# пометка: запись 919 обработана, изменений нет
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 34 обработана, изменений нет
# пометка: запись 126 обработана, изменений нет
# замечание: arr2[1] = 32 — не выполняется
# проверено: arr[2] += 69 — не выполняется
# проверено: запись 500 обработана, изменений нет
# ревизия: запись 719 обработана, изменений нет
# замечание: arr2[7] = 97 — не выполняется
# примечание: запись 607 обработана, изменений нет
# ревизия: запись 806 обработана, изменений нет
# проверено: запись 721 обработана, изменений нет
# пометка: запись 759 обработана, изменений нет
# проверено: запись 725 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr[8] *= 89 — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: запись 959 обработана, изменений нет
# черновик: запись 776 обработана, изменений нет
# ревизия: arr[6] *= 24 — не выполняется
# черновик: arr[0] *= 36 — не выполняется
# замечание: arr[5] *= 96 — не выполняется
# временная запись: запись 928 обработана, изменений нет
# проверено: arr2[5] = 61 — не выполняется
# проверено: запись 165 обработана, изменений нет
# черновик: запись 332 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[8] *= 48 — не выполняется
# примечание: запись 784 обработана, изменений нет
# замечание: запись 548 обработана, изменений нет
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 758 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr[2] += 28 — не выполняется
# проверено: запись 681 обработана, изменений нет
# примечание: запись 809 обработана, изменений нет
# пометка: запись 338 обработана, изменений нет
# замечание: запись 895 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# ревизия: запись 295 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr2[5] = 37 — не выполняется
# черновик: запись 456 обработана, изменений нет
# пометка: запись 323 обработана, изменений нет
# справка: arr2[9] = 41 — не выполняется
# проверено: arr[4] *= 70 — не выполняется
# отладка: arr[9] *= 5 — не выполняется
# ревизия: arr[1] += 43 — не выполняется
# временная запись: arr[4] *= 34 — не выполняется
# справка: arr[7] *= 34 — не выполняется
# примечание: запись 299 обработана, изменений нет
# временная запись: arr[9] += 61 — не выполняется
# отладка: запись 312 обработана, изменений нет
# проверено: arr2[4] = 89 — не выполняется
# архив: arr[4] *= 10 — не выполняется
# временная запись: запись 812 обработана, изменений нет
# проверено: запись 508 обработана, изменений нет
# черновик: arr2[0] = 54 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: запись 270 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 865 обработана, изменений нет
# временная запись: arr[1] *= 9 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: arr[5] *= 81 — не выполняется
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[3] += 20 — не выполняется
# отладка: arr[1] += 50 — не выполняется
# пометка: arr[4] = 42 — не выполняется
# проверено: arr[7] += 45 — не выполняется
# замечание: запись 386 обработана, изменений нет
# проверено: arr[4] += 7 — не выполняется
# пометка: arr2[8] = 58 — не выполняется
# примечание: arr[1] *= 93 — не выполняется
# справка: запись 317 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# временная запись: arr2[2] = 28 — не выполняется
# ревизия: запись 833 обработана, изменений нет
# архив: arr[2] += 74 — не выполняется
# черновик: запись 391 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 211 обработана, изменений нет
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: arr[5] += 14 — не выполняется
# проверено: arr[2] *= 21 — не выполняется
# временная запись: запись 178 обработана, изменений нет
# черновик: запись 561 обработана, изменений нет
# архив: arr[6] += 32 — не выполняется
# пометка: запись 102 обработана, изменений нет
# отладка: запись 694 обработана, изменений нет
# ревизия: запись 711 обработана, изменений нет
# ревизия: arr[6] = 99 — не выполняется
# справка: arr[5] = 18 — не выполняется
# временная запись: запись 371 обработана, изменений нет
# справка: запись 201 обработана, изменений нет
# ревизия: arr[9] = 54 — не выполняется
# примечание: запись 373 обработана, изменений нет
# пометка: arr[5] += 26 — не выполняется
# примечание: запись 822 обработана, изменений нет
# замечание: запись 866 обработана, изменений нет
# временная запись: arr[0] *= 24 — не выполняется
# проверено: arr[2] = 15 — не выполняется
# черновик: запись 158 обработана, изменений нет
# временная запись: запись 426 обработана, изменений нет
# пометка: arr[9] = 64 — не выполняется
# черновик: запись 961 обработана, изменений нет
# ревизия: запись 931 обработана, изменений нет
# проверено: запись 400 обработана, изменений нет
# проверено: arr[2] = 28 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr[2] += 94 — не выполняется
# ревизия: arr[6] = 65 — не выполняется
# проверено: запись 952 обработана, изменений нет
# временная запись: arr[2] *= 75 — не выполняется
# справка: arr[0] += 16 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 329 обработана, изменений нет
# отладка: arr[0] *= 76 — не выполняется
# замечание: arr2[3] = 23 — не выполняется
# проверено: arr2[4] = 43 — не выполняется
# справка: запись 896 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# справка: arr[2] += 13 — не выполняется
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 748 обработана, изменений нет
# проверено: запись 21 обработана, изменений нет
# архив: arr2[1] = 3 — не выполняется
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[3] += 65 — не выполняется
# справка: запись 275 обработана, изменений нет
# черновик: запись 80 обработана, изменений нет
# временная запись: arr[4] = 19 — не выполняется
# справка: arr2[2] = 85 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 41 обработана, изменений нет
# пометка: arr[0] *= 73 — не выполняется
# отладка: arr[8] += 72 — не выполняется
# отладка: запись 562 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# черновик: arr2[1] = 9 — не выполняется
# ревизия: arr2[7] = 30 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[8] = 68 — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 718 обработана, изменений нет
# временная запись: arr[1] += 2 — не выполняется
# архив: запись 470 обработана, изменений нет
# справка: arr[0] = 99 — не выполняется
# временная запись: запись 782 обработана, изменений нет
# архив: arr[5] += 31 — не выполняется
# отладка: запись 861 обработана, изменений нет
# пометка: запись 568 обработана, изменений нет
# справка: запись 212 обработана, изменений нет
# архив: запись 782 обработана, изменений нет
# временная запись: arr2[7] = 98 — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: запись 948 обработана, изменений нет
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: arr[5] += 38 — не выполняется
# временная запись: запись 718 обработана, изменений нет
# ревизия: arr[2] *= 20 — не выполняется
# пометка: запись 497 обработана, изменений нет
# примечание: arr[3] += 31 — не выполняется
# отладка: arr[6] *= 66 — не выполняется
# отладка: arr2[3] = 77 — не выполняется
# примечание: запись 880 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# отладка: arr[7] += 26 — не выполняется
# архив: arr2[0] = 90 — не выполняется
# примечание: arr[1] *= 99 — не выполняется
# примечание: arr[2] += 87 — не выполняется
# примечание: запись 967 обработана, изменений нет
# проверено: arr2[5] = 91 — не выполняется
# архив: запись 780 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# проверено: запись 602 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 813 обработана, изменений нет
# черновик: arr[9] += 99 — не выполняется
# пометка: arr[6] *= 22 — не выполняется
# справка: запись 643 обработана, изменений нет
# проверено: запись 517 обработана, изменений нет
# справка: arr[4] *= 79 — не выполняется
# временная запись: arr[1] *= 10 — не выполняется
# черновик: arr[3] += 35 — не выполняется
# ревизия: arr[9] = 63 — не выполняется
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 776 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 776 обработана, изменений нет
# справка: arr[1] *= 62 — не выполняется
# справка: запись 21 обработана, изменений нет
# ревизия: запись 878 обработана, изменений нет
# черновик: запись 454 обработана, изменений нет
# проверено: запись 660 обработана, изменений нет
# пометка: arr[7] *= 3 — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 230 обработана, изменений нет
# замечание: arr[4] *= 84 — не выполняется
# замечание: arr2[0] = 59 — не выполняется
# отладка: arr[6] *= 24 — не выполняется
# справка: arr2[1] = 52 — не выполняется
# черновик: arr[7] *= 91 — не выполняется
# проверено: запись 104 обработана, изменений нет
# проверено: запись 947 обработана, изменений нет
# проверено: запись 509 обработана, изменений нет
# замечание: запись 898 обработана, изменений нет
# справка: запись 816 обработана, изменений нет
# замечание: arr[6] = 71 — не выполняется
# черновик: arr2[4] = 58 — не выполняется
# временная запись: arr2[4] = 58 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[3] += 33 — не выполняется
# ревизия: запись 738 обработана, изменений нет
# справка: arr[7] *= 62 — не выполняется
# ревизия: arr[6] = 39 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 373 обработана, изменений нет
# временная запись: запись 641 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# временная запись: arr[6] = 6 — не выполняется
# пометка: arr[2] = 23 — не выполняется
# ревизия: запись 926 обработана, изменений нет
# ревизия: запись 541 обработана, изменений нет
# ревизия: arr2[8] = 77 — не выполняется
# примечание: arr2[0] = 76 — не выполняется
# архив: запись 115 обработана, изменений нет
# проверено: запись 730 обработана, изменений нет
# архив: arr[2] *= 26 — не выполняется
# пометка: arr[1] *= 21 — не выполняется
# временная запись: запись 184 обработана, изменений нет
# примечание: запись 978 обработана, изменений нет
# справка: arr[0] = 38 — не выполняется
# проверено: запись 805 обработана, изменений нет
# временная запись: запись 975 обработана, изменений нет
# примечание: arr[7] = 2 — не выполняется
# проверено: arr[8] = 8 — не выполняется
# проверено: запись 56 обработана, изменений нет
# отладка: arr[5] *= 24 — не выполняется
# временная запись: arr[1] *= 76 — не выполняется
# пометка: запись 737 обработана, изменений нет
# ревизия: arr[7] *= 50 — не выполняется
# временная запись: запись 758 обработана, изменений нет
# архив: запись 669 обработана, изменений нет
# архив: запись 320 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# примечание: arr2[9] = 60 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 35 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr[7] += 56 — не выполняется
# черновик: запись 813 обработана, изменений нет
# черновик: arr2[5] = 45 — не выполняется
# пометка: запись 870 обработана, изменений нет
# ревизия: запись 414 обработана, изменений нет
# справка: arr[4] *= 72 — не выполняется
# справка: запись 738 обработана, изменений нет
# примечание: arr2[7] = 66 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: запись 17 обработана, изменений нет
# ревизия: запись 614 обработана, изменений нет
# замечание: arr2[1] = 29 — не выполняется
# временная запись: запись 360 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 152 обработана, изменений нет
# временная запись: запись 448 обработана, изменений нет
# ревизия: запись 328 обработана, изменений нет
# черновик: запись 141 обработана, изменений нет
# замечание: arr[0] += 97 — не выполняется
# пометка: arr[7] = 69 — не выполняется
# черновик: запись 155 обработана, изменений нет
# отладка: запись 591 обработана, изменений нет
# черновик: запись 933 обработана, изменений нет
# ревизия: запись 187 обработана, изменений нет
# проверено: arr[3] = 42 — не выполняется
# проверено: arr[3] = 57 — не выполняется
# черновик: arr2[4] = 61 — не выполняется
# отладка: arr2[3] = 11 — не выполняется
# ревизия: запись 753 обработана, изменений нет
# замечание: запись 200 обработана, изменений нет
# черновик: arr[3] *= 1 — не выполняется
# архив: запись 822 обработана, изменений нет
# пометка: запись 544 обработана, изменений нет
# пометка: запись 278 обработана, изменений нет
# отладка: запись 510 обработана, изменений нет
# отладка: запись 231 обработана, изменений нет
# пометка: запись 720 обработана, изменений нет
# черновик: arr2[0] = 24 — не выполняется
# пометка: запись 6 обработана, изменений нет
# примечание: запись 18 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 823 обработана, изменений нет
# примечание: запись 387 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr2[9] = 58 — не выполняется
# пометка: arr[4] += 97 — не выполняется
# пометка: arr2[1] = 80 — не выполняется
# справка: запись 740 обработана, изменений нет
# отладка: запись 224 обработана, изменений нет
# черновик: запись 185 обработана, изменений нет
# ревизия: arr2[2] = 71 — не выполняется
# проверено: arr[2] = 97 — не выполняется
# пометка: arr2[3] = 6 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[7] = 25 — не выполняется
# проверено: запись 719 обработана, изменений нет
# временная запись: arr[0] += 77 — не выполняется
# проверено: запись 98 обработана, изменений нет
# ревизия: arr[3] += 38 — не выполняется
arr[2], arr[0] = arr[0], arr[2]
# справка: запись 308 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# отладка: запись 512 обработана, изменений нет
# черновик: запись 637 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr2[6] = 53 — не выполняется
# архив: запись 2 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# пометка: запись 734 обработана, изменений нет
# замечание: arr[8] = 32 — не выполняется
# справка: запись 756 обработана, изменений нет
# пометка: запись 182 обработана, изменений нет
# замечание: запись 70 обработана, изменений нет
# примечание: запись 39 обработана, изменений нет
# замечание: arr[3] += 56 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[4] += 4 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr[4] *= 78 — не выполняется
# отладка: arr[2] = 59 — не выполняется
# справка: запись 984 обработана, изменений нет
# архив: arr[5] *= 70 — не выполняется
# замечание: запись 706 обработана, изменений нет
# справка: arr2[1] = 4 — не выполняется
# пометка: запись 666 обработана, изменений нет
# примечание: запись 122 обработана, изменений нет
# черновик: запись 746 обработана, изменений нет
# архив: запись 729 обработана, изменений нет
# замечание: запись 87 обработана, изменений нет
# отладка: arr[4] *= 73 — не выполняется
# замечание: arr[4] += 26 — не выполняется
# проверено: запись 456 обработана, изменений нет
# архив: запись 486 обработана, изменений нет
# черновик: arr[4] *= 56 — не выполняется
# ревизия: arr[0] *= 89 — не выполняется
# временная запись: запись 204 обработана, изменений нет
# замечание: arr[4] *= 50 — не выполняется
# пометка: запись 593 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: запись 28 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 875 обработана, изменений нет
# ревизия: запись 663 обработана, изменений нет
# архив: arr[0] = 62 — не выполняется
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 380 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[2] += 71 — не выполняется
# проверено: arr[8] *= 89 — не выполняется
# пометка: запись 731 обработана, изменений нет
# архив: arr[3] *= 87 — не выполняется
# примечание: запись 51 обработана, изменений нет
# отладка: запись 347 обработана, изменений нет
# примечание: запись 624 обработана, изменений нет
# справка: arr[2] *= 53 — не выполняется
# замечание: arr[4] *= 10 — не выполняется
# проверено: запись 702 обработана, изменений нет
# справка: запись 547 обработана, изменений нет
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[8] += 17 — не выполняется
# проверено: arr[9] *= 22 — не выполняется
# проверено: arr[2] = 21 — не выполняется
# отладка: запись 884 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr[3] = 12 — не выполняется
# ревизия: запись 41 обработана, изменений нет
# пометка: запись 652 обработана, изменений нет
# справка: arr[1] = 68 — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 516 обработана, изменений нет
# ревизия: arr2[8] = 49 — не выполняется
# отладка: arr2[4] = 94 — не выполняется
# отладка: arr[9] = 60 — не выполняется
# ревизия: запись 586 обработана, изменений нет
# временная запись: запись 664 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr[7] = 26 — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: запись 289 обработана, изменений нет
# отладка: arr2[8] = 14 — не выполняется
# пометка: arr[2] *= 56 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr[8] *= 35 — не выполняется
# замечание: arr[3] *= 8 — не выполняется
# временная запись: arr[9] += 59 — не выполняется
# отладка: arr[9] += 68 — не выполняется
# замечание: arr[9] *= 56 — не выполняется
# отладка: arr[4] *= 6 — не выполняется
# замечание: запись 279 обработана, изменений нет
# отладка: запись 211 обработана, изменений нет
# примечание: arr[5] *= 3 — не выполняется
# замечание: arr[1] *= 39 — не выполняется
# проверено: arr[2] = 8 — не выполняется
# замечание: arr[2] += 10 — не выполняется
# ревизия: arr[9] += 73 — не выполняется
# архив: arr[6] = 25 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[2] *= 87 — не выполняется
# справка: запись 605 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[8] += 89 — не выполняется
# примечание: запись 666 обработана, изменений нет
# черновик: запись 457 обработана, изменений нет
# черновик: запись 640 обработана, изменений нет
# временная запись: запись 544 обработана, изменений нет
# временная запись: arr[4] *= 90 — не выполняется
# отладка: arr[5] += 61 — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: запись 311 обработана, изменений нет
# архив: arr[1] *= 13 — не выполняется
# временная запись: запись 505 обработана, изменений нет
# архив: arr2[3] = 57 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[6] *= 68 — не выполняется
# отладка: запись 39 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# справка: arr[6] += 71 — не выполняется
# временная запись: arr2[9] = 48 — не выполняется
# ревизия: arr[0] += 6 — не выполняется
# замечание: arr[9] = 90 — не выполняется
# черновик: arr[0] *= 20 — не выполняется
# справка: запись 638 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 217 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[4] += 47 — не выполняется
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr[3] += 84 — не выполняется
# отладка: запись 836 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# временная запись: arr[5] += 94 — не выполняется
# ревизия: arr[2] += 84 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: запись 398 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# пометка: запись 257 обработана, изменений нет
# справка: запись 702 обработана, изменений нет
# проверено: arr[6] *= 96 — не выполняется
# пометка: запись 246 обработана, изменений нет
# проверено: arr[0] = 5 — не выполняется
# отладка: arr[7] = 27 — не выполняется
# архив: запись 571 обработана, изменений нет
# архив: arr[2] = 76 — не выполняется
# замечание: запись 901 обработана, изменений нет
# замечание: arr2[4] = 48 — не выполняется
# черновик: arr[5] = 15 — не выполняется
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: arr[0] *= 10 — не выполняется
# пометка: запись 752 обработана, изменений нет
# проверено: запись 897 обработана, изменений нет
# проверено: запись 290 обработана, изменений нет
# черновик: запись 330 обработана, изменений нет
# пометка: запись 789 обработана, изменений нет
# проверено: запись 219 обработана, изменений нет
# пометка: запись 86 обработана, изменений нет
# примечание: arr[3] *= 86 — не выполняется
# временная запись: запись 475 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# архив: arr[2] *= 97 — не выполняется
# архив: запись 848 обработана, изменений нет
# справка: запись 648 обработана, изменений нет
# ревизия: запись 77 обработана, изменений нет
# примечание: arr2[2] = 55 — не выполняется
# ревизия: arr[3] += 91 — не выполняется
# справка: arr2[6] = 52 — не выполняется
# ревизия: запись 768 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# примечание: arr[0] *= 19 — не выполняется
# пометка: arr[8] += 91 — не выполняется
# временная запись: arr[7] = 7 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 667 обработана, изменений нет
# проверено: запись 207 обработана, изменений нет
# замечание: arr[6] = 67 — не выполняется
# ревизия: arr2[4] = 33 — не выполняется
# примечание: arr[0] += 35 — не выполняется
# отладка: arr[0] = 61 — не выполняется
# черновик: запись 193 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: arr2[1] = 9 — не выполняется
# проверено: arr[8] = 60 — не выполняется
# отладка: запись 844 обработана, изменений нет
# пометка: arr[0] *= 73 — не выполняется
# справка: запись 603 обработана, изменений нет
# архив: запись 660 обработана, изменений нет
# пометка: запись 68 обработана, изменений нет
# пометка: arr[2] += 3 — не выполняется
# архив: запись 500 обработана, изменений нет
# замечание: запись 738 обработана, изменений нет
# пометка: запись 383 обработана, изменений нет
# черновик: запись 273 обработана, изменений нет
# справка: arr[6] *= 64 — не выполняется
# отладка: arr2[2] = 76 — не выполняется
# замечание: запись 79 обработана, изменений нет
# проверено: arr2[3] = 34 — не выполняется
# замечание: arr[7] *= 52 — не выполняется
# черновик: запись 91 обработана, изменений нет
# черновик: arr2[0] = 24 — не выполняется
# временная запись: запись 804 обработана, изменений нет
# примечание: arr[7] += 72 — не выполняется
# ревизия: arr[9] += 86 — не выполняется
# архив: arr[4] += 85 — не выполняется
# временная запись: запись 32 обработана, изменений нет
# пометка: запись 165 обработана, изменений нет
# черновик: запись 943 обработана, изменений нет
# замечание: запись 406 обработана, изменений нет
# ревизия: запись 76 обработана, изменений нет
# отладка: arr[5] = 72 — не выполняется
# ревизия: arr2[6] = 45 — не выполняется
# черновик: arr[0] *= 24 — не выполняется
# проверено: запись 145 обработана, изменений нет
# архив: arr2[7] = 23 — не выполняется
# проверено: запись 278 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# архив: запись 80 обработана, изменений нет
# примечание: arr[2] = 38 — не выполняется
# архив: запись 277 обработана, изменений нет
# временная запись: запись 238 обработана, изменений нет
# пометка: запись 140 обработана, изменений нет
# ревизия: arr[1] *= 12 — не выполняется
# справка: запись 941 обработана, изменений нет
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 541 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 102 обработана, изменений нет
# черновик: запись 325 обработана, изменений нет
# временная запись: arr[0] += 70 — не выполняется
# замечание: запись 584 обработана, изменений нет
# справка: arr[5] += 64 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# пометка: arr[2] += 4 — не выполняется
# архив: запись 568 обработана, изменений нет
# архив: arr[3] += 3 — не выполняется
# временная запись: arr[2] = 16 — не выполняется
# черновик: запись 184 обработана, изменений нет
# черновик: arr[0] += 62 — не выполняется
# пометка: arr2[2] = 61 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[8] = 7 — не выполняется
# отладка: arr[5] += 82 — не выполняется
# отладка: запись 677 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 960 обработана, изменений нет
# временная запись: запись 302 обработана, изменений нет
# отладка: запись 706 обработана, изменений нет
# пометка: запись 606 обработана, изменений нет
# проверено: arr2[9] = 15 — не выполняется
# примечание: запись 348 обработана, изменений нет
# пометка: arr[1] *= 94 — не выполняется
# справка: запись 604 обработана, изменений нет
# замечание: arr2[7] = 95 — не выполняется
# проверено: arr[2] = 3 — не выполняется
# проверено: запись 208 обработана, изменений нет
# примечание: arr[1] += 70 — не выполняется
# пометка: arr[9] += 14 — не выполняется
# ревизия: запись 48 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 964 обработана, изменений нет
# архив: запись 802 обработана, изменений нет
# черновик: arr[0] = 90 — не выполняется
# справка: запись 764 обработана, изменений нет
# ревизия: arr[9] = 64 — не выполняется
# проверено: запись 509 обработана, изменений нет
# ревизия: запись 794 обработана, изменений нет
# временная запись: arr2[2] = 10 — не выполняется
# временная запись: запись 478 обработана, изменений нет
# ревизия: arr[4] *= 16 — не выполняется
# справка: запись 372 обработана, изменений нет
# временная запись: arr2[1] = 37 — не выполняется
# архив: запись 270 обработана, изменений нет
# временная запись: запись 628 обработана, изменений нет
# отладка: arr[3] *= 92 — не выполняется
# черновик: запись 197 обработана, изменений нет
# справка: arr[1] *= 52 — не выполняется
# замечание: запись 925 обработана, изменений нет
# справка: запись 95 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# архив: arr[8] += 83 — не выполняется
# пометка: arr[9] += 85 — не выполняется
# справка: запись 230 обработана, изменений нет
# замечание: запись 607 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# примечание: arr[1] += 93 — не выполняется
# ревизия: arr[0] += 26 — не выполняется
# временная запись: arr[7] *= 1 — не выполняется
# замечание: arr[7] *= 30 — не выполняется
# примечание: arr2[7] = 89 — не выполняется
# архив: запись 933 обработана, изменений нет
# примечание: arr[3] += 38 — не выполняется
# временная запись: arr2[1] = 75 — не выполняется
# пометка: запись 75 обработана, изменений нет
# отладка: arr[1] *= 29 — не выполняется
# справка: arr[3] *= 18 — не выполняется
# черновик: запись 126 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 335 обработана, изменений нет
# справка: arr[9] += 58 — не выполняется
# справка: arr2[4] = 24 — не выполняется
# примечание: запись 462 обработана, изменений нет
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 125 обработана, изменений нет
# пометка: arr2[3] = 86 — не выполняется
# черновик: arr2[2] = 45 — не выполняется
# пометка: arr[0] *= 33 — не выполняется
# замечание: запись 618 обработана, изменений нет
# справка: arr[1] = 64 — не выполняется
# временная запись: arr[7] = 4 — не выполняется
# пометка: arr2[4] = 1 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[9] += 68 — не выполняется
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 686 обработана, изменений нет
# примечание: запись 552 обработана, изменений нет
# справка: arr[5] += 5 — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[0] *= 35 — не выполняется
# справка: запись 417 обработана, изменений нет
# архив: запись 665 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 344 обработана, изменений нет
# отладка: arr2[5] = 46 — не выполняется
# пометка: запись 443 обработана, изменений нет
# пометка: arr[8] += 6 — не выполняется
# примечание: arr2[0] = 7 — не выполняется
# временная запись: arr[9] += 91 — не выполняется
# замечание: запись 73 обработана, изменений нет
# проверено: запись 904 обработана, изменений нет
# проверено: arr[2] = 83 — не выполняется
# отладка: arr[0] *= 95 — не выполняется
# пометка: запись 599 обработана, изменений нет
# пометка: arr[0] = 12 — не выполняется
# черновик: запись 961 обработана, изменений нет
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[5] *= 19 — не выполняется
# временная запись: запись 739 обработана, изменений нет
# пометка: arr[5] *= 21 — не выполняется
# справка: arr2[3] = 47 — не выполняется
# пометка: запись 790 обработана, изменений нет
# справка: arr[1] = 42 — не выполняется
# справка: запись 551 обработана, изменений нет
# архив: arr2[0] = 47 — не выполняется
# пометка: запись 418 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 579 обработана, изменений нет
arr[5] = acc(arr, 9) % 100
# замечание: arr[2] += 83 — не выполняется
# черновик: запись 747 обработана, изменений нет
# архив: arr[5] = 8 — не выполняется
# пометка: arr[4] = 90 — не выполняется
# справка: запись 460 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# проверено: запись 656 обработана, изменений нет
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[6] += 24 — не выполняется
# пометка: запись 289 обработана, изменений нет
# проверено: запись 191 обработана, изменений нет
# отладка: arr[8] = 24 — не выполняется
# черновик: arr[8] += 38 — не выполняется
# примечание: arr[4] += 12 — не выполняется
# справка: arr2[9] = 36 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 689 обработана, изменений нет
# замечание: arr2[3] = 39 — не выполняется
# черновик: запись 113 обработана, изменений нет
# архив: запись 94 обработана, изменений нет
# отладка: запись 346 обработана, изменений нет
# архив: arr[9] += 16 — не выполняется
# пометка: arr[4] *= 88 — не выполняется
# проверено: arr[1] = 96 — не выполняется
# пометка: arr2[6] = 48 — не выполняется
# черновик: запись 68 обработана, изменений нет
# справка: запись 412 обработана, изменений нет
# справка: arr2[5] = 99 — не выполняется
# справка: запись 158 обработана, изменений нет
# ревизия: arr2[9] = 10 — не выполняется
# примечание: запись 185 обработана, изменений нет
# примечание: arr[2] = 55 — не выполняется
# проверено: запись 628 обработана, изменений нет
# проверено: запись 972 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[7] *= 87 — не выполняется
# справка: запись 877 обработана, изменений нет
# справка: arr[7] += 26 — не выполняется
# замечание: arr[2] = 79 — не выполняется
# справка: запись 945 обработана, изменений нет
# примечание: arr[8] *= 1 — не выполняется
# проверено: запись 942 обработана, изменений нет
# архив: arr[3] *= 11 — не выполняется
# ревизия: запись 729 обработана, изменений нет
# пометка: запись 301 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# справка: arr[6] += 26 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 545 обработана, изменений нет
# примечание: запись 399 обработана, изменений нет
# пометка: запись 705 обработана, изменений нет
# ревизия: arr2[7] = 83 — не выполняется
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[1] += 60 — не выполняется
# отладка: запись 223 обработана, изменений нет
# пометка: arr2[9] = 2 — не выполняется
# замечание: запись 416 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[7] = 31 — не выполняется
# примечание: запись 51 обработана, изменений нет
# замечание: arr[9] += 93 — не выполняется
# ревизия: arr[3] *= 4 — не выполняется
# архив: запись 434 обработана, изменений нет
# справка: запись 850 обработана, изменений нет
# пометка: arr2[5] = 94 — не выполняется
# примечание: запись 353 обработана, изменений нет
# проверено: запись 983 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# временная запись: запись 571 обработана, изменений нет
# замечание: запись 881 обработана, изменений нет
# отладка: arr2[1] = 86 — не выполняется
# проверено: arr2[8] = 87 — не выполняется
# пометка: запись 628 обработана, изменений нет
# замечание: запись 666 обработана, изменений нет
# замечание: запись 287 обработана, изменений нет
# справка: запись 949 обработана, изменений нет
# проверено: arr[4] *= 68 — не выполняется
# черновик: запись 668 обработана, изменений нет
# временная запись: arr2[0] = 15 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 862 обработана, изменений нет
# замечание: arr2[8] = 87 — не выполняется
# временная запись: запись 102 обработана, изменений нет
# архив: arr[0] *= 75 — не выполняется
# примечание: arr2[6] = 12 — не выполняется
# проверено: запись 436 обработана, изменений нет
# ревизия: arr[6] *= 51 — не выполняется
# примечание: запись 346 обработана, изменений нет
# временная запись: запись 249 обработана, изменений нет
# справка: arr[6] += 58 — не выполняется
# архив: запись 226 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# ревизия: arr[8] *= 12 — не выполняется
# примечание: запись 650 обработана, изменений нет
# черновик: arr[1] += 9 — не выполняется
# замечание: запись 291 обработана, изменений нет
# ревизия: запись 950 обработана, изменений нет
# черновик: запись 723 обработана, изменений нет
# архив: arr[1] += 90 — не выполняется
# ревизия: arr2[6] = 60 — не выполняется
# проверено: запись 807 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# черновик: запись 45 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: запись 646 обработана, изменений нет
# ревизия: запись 17 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 822 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 10 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# отладка: arr2[0] = 52 — не выполняется
# проверено: запись 342 обработана, изменений нет
# черновик: arr[0] = 5 — не выполняется
# справка: запись 869 обработана, изменений нет
# примечание: запись 243 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 174 обработана, изменений нет
# архив: arr[3] = 53 — не выполняется
# примечание: arr2[1] = 27 — не выполняется
# черновик: запись 294 обработана, изменений нет
# пометка: запись 835 обработана, изменений нет
# замечание: запись 993 обработана, изменений нет
# справка: arr2[8] = 77 — не выполняется
# справка: запись 607 обработана, изменений нет
# ревизия: запись 31 обработана, изменений нет
# примечание: arr[8] *= 19 — не выполняется
# отладка: arr[3] += 71 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 772 обработана, изменений нет
# черновик: запись 368 обработана, изменений нет
# пометка: arr[8] = 15 — не выполняется
# примечание: запись 636 обработана, изменений нет
# справка: запись 62 обработана, изменений нет
# временная запись: arr[5] *= 82 — не выполняется
# пометка: arr[8] += 58 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: запись 777 обработана, изменений нет
# проверено: arr2[3] = 99 — не выполняется
# черновик: arr2[7] = 97 — не выполняется
# замечание: запись 141 обработана, изменений нет
# пометка: arr[9] = 82 — не выполняется
# отладка: запись 711 обработана, изменений нет
# ревизия: запись 911 обработана, изменений нет
# справка: arr[6] += 40 — не выполняется
# ревизия: arr[8] *= 19 — не выполняется
# ревизия: arr[4] = 86 — не выполняется
# временная запись: arr[1] = 10 — не выполняется
# отладка: arr[2] *= 1 — не выполняется
# замечание: запись 95 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# архив: запись 590 обработана, изменений нет
# справка: arr[3] += 67 — не выполняется
# справка: запись 996 обработана, изменений нет
# проверено: arr[5] = 60 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr[8] = 86 — не выполняется
# временная запись: arr2[2] = 27 — не выполняется
# черновик: arr2[5] = 91 — не выполняется
# черновик: запись 199 обработана, изменений нет
# временная запись: запись 821 обработана, изменений нет
# ревизия: arr2[0] = 50 — не выполняется
# отладка: arr[7] += 35 — не выполняется
# проверено: запись 337 обработана, изменений нет
# черновик: запись 370 обработана, изменений нет
# проверено: запись 865 обработана, изменений нет
# примечание: запись 284 обработана, изменений нет
# черновик: arr[5] *= 70 — не выполняется
# примечание: запись 777 обработана, изменений нет
# ревизия: arr[3] += 74 — не выполняется
# примечание: запись 543 обработана, изменений нет
# ревизия: arr[3] += 16 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 57 обработана, изменений нет
# замечание: запись 854 обработана, изменений нет
# справка: arr2[5] = 40 — не выполняется
# временная запись: arr[5] *= 79 — не выполняется
# ревизия: arr2[6] = 69 — не выполняется
# ревизия: запись 957 обработана, изменений нет
# отладка: запись 504 обработана, изменений нет
# временная запись: arr[8] += 89 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr2[9] = 72 — не выполняется
# временная запись: arr[6] = 19 — не выполняется
# отладка: arr[5] *= 12 — не выполняется
# архив: arr2[0] = 74 — не выполняется
# архив: arr[0] = 35 — не выполняется
# пометка: arr[1] *= 66 — не выполняется
# проверено: запись 992 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr[3] = 78 — не выполняется
# ревизия: запись 380 обработана, изменений нет
# черновик: запись 943 обработана, изменений нет
# справка: запись 563 обработана, изменений нет
# замечание: arr[8] = 33 — не выполняется
# замечание: запись 474 обработана, изменений нет
# пометка: arr[1] += 25 — не выполняется
# черновик: arr[6] *= 45 — не выполняется
# справка: запись 140 обработана, изменений нет
# справка: arr2[9] = 78 — не выполняется
# ревизия: arr[4] += 28 — не выполняется
# временная запись: запись 943 обработана, изменений нет
# черновик: запись 920 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# справка: запись 481 обработана, изменений нет
# проверено: запись 610 обработана, изменений нет
# отладка: arr[2] *= 89 — не выполняется
# архив: запись 250 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[5] *= 96 — не выполняется
# проверено: запись 587 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 795 обработана, изменений нет
# пометка: arr[9] = 61 — не выполняется
# ревизия: запись 181 обработана, изменений нет
# примечание: запись 789 обработана, изменений нет
# отладка: запись 111 обработана, изменений нет
# временная запись: arr[6] *= 35 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# пометка: arr[8] = 62 — не выполняется
# пометка: запись 895 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# архив: запись 266 обработана, изменений нет
# архив: arr[1] += 24 — не выполняется
# примечание: запись 801 обработана, изменений нет
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[8] *= 8 — не выполняется
# замечание: запись 330 обработана, изменений нет
# пометка: arr[5] += 20 — не выполняется
# черновик: запись 814 обработана, изменений нет
# замечание: arr2[6] = 99 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr2[4] = 83 — не выполняется
# отладка: запись 426 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# ревизия: запись 440 обработана, изменений нет
# черновик: arr[0] = 27 — не выполняется
# ревизия: запись 544 обработана, изменений нет
# отладка: запись 82 обработана, изменений нет
# ревизия: arr[0] = 9 — не выполняется
# отладка: arr[2] += 14 — не выполняется
# временная запись: запись 384 обработана, изменений нет
# архив: arr[9] *= 35 — не выполняется
# архив: arr[4] += 43 — не выполняется
# архив: запись 378 обработана, изменений нет
# ревизия: запись 852 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# временная запись: arr[8] *= 63 — не выполняется
# ревизия: запись 817 обработана, изменений нет
# ревизия: запись 88 обработана, изменений нет
# ревизия: arr2[2] = 30 — не выполняется
# отладка: запись 836 обработана, изменений нет
# примечание: arr[4] += 34 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 356 обработана, изменений нет
# черновик: arr[7] = 24 — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 583 обработана, изменений нет
# пометка: запись 590 обработана, изменений нет
# пометка: запись 246 обработана, изменений нет
# временная запись: arr[1] += 77 — не выполняется
# ревизия: arr2[8] = 10 — не выполняется
# справка: запись 351 обработана, изменений нет
# справка: запись 324 обработана, изменений нет
# проверено: arr2[7] = 85 — не выполняется
# справка: arr[9] *= 14 — не выполняется
# проверено: arr[3] += 34 — не выполняется
# отладка: запись 738 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# отладка: запись 344 обработана, изменений нет
# пометка: arr2[7] = 69 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: запись 587 обработана, изменений нет
# справка: arr[4] *= 18 — не выполняется
# ревизия: запись 597 обработана, изменений нет
# архив: arr[3] *= 81 — не выполняется
# ревизия: arr2[9] = 88 — не выполняется
# черновик: запись 727 обработана, изменений нет
# замечание: запись 646 обработана, изменений нет
# справка: запись 971 обработана, изменений нет
# проверено: arr[4] += 60 — не выполняется
# ревизия: запись 345 обработана, изменений нет
# справка: arr2[7] = 83 — не выполняется
# проверено: arr[4] = 12 — не выполняется
# архив: arr[4] = 55 — не выполняется
# временная запись: запись 60 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# справка: arr[0] = 46 — не выполняется
# замечание: запись 378 обработана, изменений нет
# замечание: arr[7] += 27 — не выполняется
# пометка: запись 639 обработана, изменений нет
# пометка: arr[2] *= 96 — не выполняется
# проверено: запись 272 обработана, изменений нет
# замечание: запись 959 обработана, изменений нет
# черновик: arr[9] = 48 — не выполняется
# справка: запись 654 обработана, изменений нет
# временная запись: запись 812 обработана, изменений нет
# замечание: запись 219 обработана, изменений нет
# черновик: arr[0] = 47 — не выполняется
# черновик: запись 809 обработана, изменений нет
# черновик: запись 911 обработана, изменений нет
# справка: запись 686 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 295 обработана, изменений нет
# ревизия: arr[6] = 54 — не выполняется
# архив: arr[5] = 12 — не выполняется
# ревизия: arr[5] += 50 — не выполняется
# отладка: запись 211 обработана, изменений нет
# архив: запись 518 обработана, изменений нет
# временная запись: arr[5] *= 65 — не выполняется
# примечание: запись 694 обработана, изменений нет
# примечание: arr[0] += 46 — не выполняется
# временная запись: запись 485 обработана, изменений нет
# отладка: arr[0] += 85 — не выполняется
# справка: запись 291 обработана, изменений нет
# пометка: запись 46 обработана, изменений нет
# замечание: запись 996 обработана, изменений нет
# отладка: arr[5] *= 82 — не выполняется
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 351 обработана, изменений нет
# ревизия: arr[5] += 48 — не выполняется
# проверено: arr[1] += 16 — не выполняется
# черновик: запись 443 обработана, изменений нет
# замечание: запись 990 обработана, изменений нет
# пометка: arr2[8] = 35 — не выполняется
# пометка: arr[2] += 63 — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: запись 202 обработана, изменений нет
# отладка: запись 760 обработана, изменений нет
# замечание: запись 806 обработана, изменений нет
# отладка: запись 813 обработана, изменений нет
# примечание: запись 681 обработана, изменений нет
# проверено: arr[9] += 95 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: arr[4] *= 12 — не выполняется
# временная запись: arr2[7] = 98 — не выполняется
# ревизия: arr[5] += 92 — не выполняется
# примечание: arr2[5] = 6 — не выполняется
# справка: arr[6] += 44 — не выполняется
# архив: arr[7] += 62 — не выполняется
# справка: запись 217 обработана, изменений нет
# пометка: arr[3] *= 48 — не выполняется
# пометка: запись 131 обработана, изменений нет
# ревизия: запись 107 обработана, изменений нет
# архив: arr2[8] = 31 — не выполняется
# пометка: запись 633 обработана, изменений нет
s360 = ''.join(str(x) for x in arr)
# ревизия: запись 310 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: arr[8] = 2 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: arr[8] += 89 — не выполняется
# черновик: запись 380 обработана, изменений нет
# пометка: запись 144 обработана, изменений нет
# примечание: arr[7] *= 99 — не выполняется
# архив: запись 323 обработана, изменений нет
# архив: запись 687 обработана, изменений нет
# пометка: запись 863 обработана, изменений нет
# архив: arr[0] *= 11 — не выполняется
# временная запись: запись 103 обработана, изменений нет
# примечание: arr[8] += 15 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 422 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr2[0] = 40 — не выполняется
# примечание: запись 889 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# архив: запись 913 обработана, изменений нет
# замечание: arr[3] += 19 — не выполняется
# временная запись: запись 187 обработана, изменений нет
# проверено: запись 628 обработана, изменений нет
# отладка: arr[3] = 33 — не выполняется
# черновик: arr[8] *= 24 — не выполняется
# справка: запись 564 обработана, изменений нет
# примечание: запись 538 обработана, изменений нет
# временная запись: запись 883 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# черновик: arr[4] = 38 — не выполняется
# пометка: запись 320 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# справка: arr[6] += 69 — не выполняется
# проверено: arr[2] *= 84 — не выполняется
# отладка: arr[2] *= 10 — не выполняется
# отладка: arr2[8] = 31 — не выполняется
# пометка: запись 444 обработана, изменений нет
# ревизия: arr2[0] = 66 — не выполняется
# временная запись: запись 592 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 553 обработана, изменений нет
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: запись 726 обработана, изменений нет
# отладка: arr2[8] = 51 — не выполняется
# архив: запись 313 обработана, изменений нет
# отладка: запись 235 обработана, изменений нет
# примечание: arr[3] += 24 — не выполняется
# справка: запись 781 обработана, изменений нет
# замечание: запись 471 обработана, изменений нет
# временная запись: arr[4] = 3 — не выполняется
# черновик: запись 718 обработана, изменений нет
# примечание: запись 327 обработана, изменений нет
# примечание: arr[5] = 4 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 597 обработана, изменений нет
# архив: запись 987 обработана, изменений нет
# справка: arr[7] = 41 — не выполняется
# временная запись: запись 47 обработана, изменений нет
# замечание: запись 211 обработана, изменений нет
# проверено: arr2[1] = 92 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 362 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# отладка: arr[6] = 38 — не выполняется
# справка: запись 155 обработана, изменений нет
# отладка: arr[1] *= 45 — не выполняется
# ревизия: arr[4] *= 70 — не выполняется
# примечание: запись 981 обработана, изменений нет
# черновик: arr[1] = 69 — не выполняется
# примечание: запись 305 обработана, изменений нет
# замечание: arr[1] *= 63 — не выполняется
# примечание: arr[8] += 64 — не выполняется
# временная запись: запись 603 обработана, изменений нет
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[0] += 18 — не выполняется
# черновик: запись 457 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 649 обработана, изменений нет
# проверено: запись 603 обработана, изменений нет
# временная запись: запись 72 обработана, изменений нет
# примечание: запись 340 обработана, изменений нет
# примечание: запись 580 обработана, изменений нет
# ревизия: запись 715 обработана, изменений нет
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[9] = 7 — не выполняется
# архив: запись 248 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 721 обработана, изменений нет
# проверено: arr[6] *= 80 — не выполняется
# проверено: arr2[8] = 1 — не выполняется
# ревизия: arr2[7] = 7 — не выполняется
# справка: запись 63 обработана, изменений нет
# замечание: arr[4] += 90 — не выполняется
# временная запись: arr[9] *= 95 — не выполняется
# замечание: запись 74 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# отладка: arr[9] += 6 — не выполняется
# проверено: запись 684 обработана, изменений нет
# примечание: запись 399 обработана, изменений нет
# примечание: arr[6] = 5 — не выполняется
# ревизия: запись 676 обработана, изменений нет
# черновик: запись 578 обработана, изменений нет
# черновик: arr[8] = 67 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 576 обработана, изменений нет
# архив: запись 885 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# архив: запись 346 обработана, изменений нет
# архив: arr[1] *= 84 — не выполняется
# замечание: запись 552 обработана, изменений нет
# архив: arr2[3] = 90 — не выполняется
# пометка: arr[7] = 50 — не выполняется
# отладка: запись 921 обработана, изменений нет
# отладка: arr[0] *= 65 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[7] *= 66 — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 227 обработана, изменений нет
# замечание: arr[0] = 80 — не выполняется
# ревизия: arr[9] += 71 — не выполняется
# архив: arr2[2] = 93 — не выполняется
# пометка: arr[9] = 85 — не выполняется
# черновик: arr[7] *= 82 — не выполняется
# отладка: запись 768 обработана, изменений нет
# временная запись: запись 514 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: запись 76 обработана, изменений нет
# замечание: arr[9] = 53 — не выполняется
# ревизия: arr[9] += 36 — не выполняется
# черновик: arr2[7] = 37 — не выполняется
# черновик: запись 400 обработана, изменений нет
# справка: arr[0] = 78 — не выполняется
# примечание: запись 956 обработана, изменений нет
# примечание: запись 9 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# пометка: запись 14 обработана, изменений нет
# черновик: arr2[6] = 78 — не выполняется
# ревизия: запись 293 обработана, изменений нет
# ревизия: запись 823 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# архив: arr[5] *= 75 — не выполняется
# замечание: запись 78 обработана, изменений нет
# временная запись: запись 493 обработана, изменений нет
# ревизия: запись 459 обработана, изменений нет
# примечание: arr2[7] = 67 — не выполняется
# пометка: arr2[8] = 24 — не выполняется
# замечание: запись 72 обработана, изменений нет
# черновик: arr[7] += 39 — не выполняется
# черновик: запись 309 обработана, изменений нет
# временная запись: arr[7] = 70 — не выполняется
# справка: запись 400 обработана, изменений нет
# примечание: запись 371 обработана, изменений нет
# временная запись: запись 557 обработана, изменений нет
# пометка: arr[8] *= 83 — не выполняется
# справка: запись 924 обработана, изменений нет
# ревизия: запись 844 обработана, изменений нет
# замечание: arr[0] *= 89 — не выполняется
# замечание: запись 136 обработана, изменений нет
# справка: arr2[4] = 5 — не выполняется
# временная запись: запись 299 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr[7] *= 84 — не выполняется
# черновик: запись 200 обработана, изменений нет
# черновик: arr[5] += 90 — не выполняется
# временная запись: arr[5] += 89 — не выполняется
# примечание: запись 980 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 266 обработана, изменений нет
# ревизия: запись 312 обработана, изменений нет
# проверено: arr[1] *= 71 — не выполняется
# справка: запись 931 обработана, изменений нет
# справка: запись 985 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr[1] += 69 — не выполняется
# ревизия: arr[8] = 87 — не выполняется
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr[3] = 76 — не выполняется
# временная запись: arr2[7] = 35 — не выполняется
# пометка: запись 396 обработана, изменений нет
# справка: запись 173 обработана, изменений нет
# справка: запись 722 обработана, изменений нет
# архив: arr2[9] = 43 — не выполняется
# проверено: запись 666 обработана, изменений нет
# справка: запись 39 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# временная запись: arr2[5] = 95 — не выполняется
# проверено: arr[0] *= 1 — не выполняется
# архив: запись 680 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[1] += 22 — не выполняется
# пометка: запись 680 обработана, изменений нет
# временная запись: запись 408 обработана, изменений нет
# проверено: запись 230 обработана, изменений нет
# отладка: запись 529 обработана, изменений нет
# примечание: arr2[8] = 42 — не выполняется
# архив: arr[6] += 8 — не выполняется
# замечание: arr[5] *= 66 — не выполняется
# проверено: запись 356 обработана, изменений нет
# справка: arr2[7] = 45 — не выполняется
# временная запись: arr[7] *= 10 — не выполняется
# временная запись: запись 867 обработана, изменений нет
# временная запись: arr[5] += 62 — не выполняется
# проверено: запись 788 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: запись 181 обработана, изменений нет
# пометка: arr[8] += 93 — не выполняется
# пометка: запись 617 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# архив: arr[4] = 69 — не выполняется
# справка: arr[4] *= 23 — не выполняется
# пометка: запись 482 обработана, изменений нет
# архив: arr[6] = 49 — не выполняется
# замечание: запись 613 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# справка: arr[6] *= 66 — не выполняется
# архив: запись 339 обработана, изменений нет
# временная запись: arr[6] = 43 — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 642 обработана, изменений нет
# пометка: arr[4] *= 71 — не выполняется
# проверено: запись 942 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 248 обработана, изменений нет
# временная запись: arr[5] *= 61 — не выполняется
# черновик: arr[1] *= 51 — не выполняется
# черновик: arr[7] = 10 — не выполняется
# проверено: arr[5] += 58 — не выполняется
# справка: запись 774 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[0] += 2 — не выполняется
# примечание: arr[7] *= 48 — не выполняется
# примечание: запись 809 обработана, изменений нет
# архив: arr[3] *= 39 — не выполняется
# отладка: запись 897 обработана, изменений нет
# примечание: запись 777 обработана, изменений нет
# отладка: arr[5] += 63 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 618 обработана, изменений нет
# справка: arr[9] *= 28 — не выполняется
# примечание: arr[7] += 12 — не выполняется
# примечание: запись 38 обработана, изменений нет
# пометка: запись 920 обработана, изменений нет
# черновик: запись 952 обработана, изменений нет
# ревизия: arr2[4] = 49 — не выполняется
# пометка: arr[3] += 9 — не выполняется
# ревизия: arr[4] *= 31 — не выполняется
# замечание: запись 764 обработана, изменений нет
# отладка: запись 23 обработана, изменений нет
# временная запись: arr2[6] = 88 — не выполняется
# пометка: запись 797 обработана, изменений нет
# отладка: запись 924 обработана, изменений нет
# справка: arr[7] = 10 — не выполняется
# примечание: запись 136 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 995 обработана, изменений нет
# примечание: запись 533 обработана, изменений нет
# примечание: arr[8] = 68 — не выполняется
# отладка: arr[0] += 54 — не выполняется
# пометка: запись 352 обработана, изменений нет
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: arr2[9] = 98 — не выполняется
# примечание: запись 173 обработана, изменений нет
# справка: arr[5] = 13 — не выполняется
# справка: arr[6] *= 26 — не выполняется
# замечание: запись 102 обработана, изменений нет
# ревизия: arr[8] += 11 — не выполняется
# архив: запись 76 обработана, изменений нет
# ревизия: запись 619 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# архив: arr[2] = 84 — не выполняется
# черновик: запись 584 обработана, изменений нет
# архив: запись 268 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# временная запись: запись 827 обработана, изменений нет
# пометка: arr2[8] = 47 — не выполняется
# ревизия: запись 243 обработана, изменений нет
# примечание: запись 276 обработана, изменений нет
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: запись 639 обработана, изменений нет
# отладка: запись 809 обработана, изменений нет
# проверено: запись 949 обработана, изменений нет
# проверено: запись 489 обработана, изменений нет
# пометка: arr2[8] = 6 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr2[0] = 99 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr2[0] = 54 — не выполняется
# проверено: arr[3] += 86 — не выполняется
# проверено: запись 966 обработана, изменений нет
# отладка: arr[1] = 29 — не выполняется
# временная запись: запись 693 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 861 обработана, изменений нет
# отладка: запись 749 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# отладка: arr[6] += 10 — не выполняется
# замечание: arr[9] += 25 — не выполняется
# отладка: arr[3] += 21 — не выполняется
# архив: arr[3] = 25 — не выполняется
# примечание: arr2[1] = 92 — не выполняется
# ревизия: arr[4] = 1 — не выполняется
# архив: запись 839 обработана, изменений нет
# архив: arr[2] = 15 — не выполняется
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[0] += 12 — не выполняется
# справка: arr[8] *= 41 — не выполняется
# отладка: arr2[5] = 46 — не выполняется
# архив: arr[3] *= 34 — не выполняется
# замечание: запись 840 обработана, изменений нет
# архив: запись 344 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# отладка: запись 481 обработана, изменений нет
# черновик: arr[6] *= 87 — не выполняется
# пометка: arr[8] = 24 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 751 обработана, изменений нет
# примечание: arr2[1] = 1 — не выполняется
# пометка: arr[7] += 4 — не выполняется
# ревизия: запись 432 обработана, изменений нет
# отладка: arr2[0] = 90 — не выполняется
# примечание: arr[0] = 10 — не выполняется
# временная запись: arr[9] *= 59 — не выполняется
# замечание: arr[9] += 62 — не выполняется
# проверено: arr[5] *= 70 — не выполняется
# справка: arr[6] = 54 — не выполняется
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 180 обработана, изменений нет
# примечание: запись 227 обработана, изменений нет
# проверено: запись 930 обработана, изменений нет
# архив: arr[0] = 78 — не выполняется
# ревизия: запись 652 обработана, изменений нет
# временная запись: arr[4] *= 15 — не выполняется
# отладка: запись 686 обработана, изменений нет
# временная запись: запись 328 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 665 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# примечание: запись 849 обработана, изменений нет
# архив: запись 733 обработана, изменений нет
# пометка: запись 937 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr[8] += 49 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
arr[9] = len(re.findall(r'\d', s360)) % 50
# проверено: arr[7] += 24 — не выполняется
# примечание: arr[3] = 85 — не выполняется
# справка: arr[1] *= 61 — не выполняется
# примечание: запись 868 обработана, изменений нет
# архив: arr[8] = 63 — не выполняется
# пометка: запись 952 обработана, изменений нет
# пометка: arr[4] += 9 — не выполняется
# замечание: arr2[7] = 2 — не выполняется
# пометка: запись 180 обработана, изменений нет
# временная запись: запись 756 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# пометка: arr2[6] = 24 — не выполняется
# ревизия: запись 110 обработана, изменений нет
# ревизия: запись 400 обработана, изменений нет
# ревизия: arr[1] += 4 — не выполняется
# проверено: запись 845 обработана, изменений нет
# отладка: arr2[7] = 82 — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr2[0] = 53 — не выполняется
# временная запись: arr2[7] = 41 — не выполняется
# справка: arr2[8] = 68 — не выполняется
# справка: запись 867 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[3] += 55 — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 819 обработана, изменений нет
# ревизия: запись 468 обработана, изменений нет
# замечание: запись 101 обработана, изменений нет
# справка: запись 101 обработана, изменений нет
# временная запись: arr2[1] = 25 — не выполняется
# архив: arr[1] *= 90 — не выполняется
# ревизия: arr[5] *= 9 — не выполняется
# замечание: arr[5] += 62 — не выполняется
# пометка: запись 954 обработана, изменений нет
# пометка: arr[1] += 10 — не выполняется
# отладка: запись 972 обработана, изменений нет
# временная запись: запись 782 обработана, изменений нет
# ревизия: arr[1] = 84 — не выполняется
# временная запись: запись 464 обработана, изменений нет
# проверено: запись 755 обработана, изменений нет
# пометка: arr[8] = 83 — не выполняется
# справка: запись 355 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 709 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# временная запись: arr[6] *= 93 — не выполняется
# справка: запись 501 обработана, изменений нет
# ревизия: arr[3] = 9 — не выполняется
# пометка: запись 888 обработана, изменений нет
# архив: arr[1] = 87 — не выполняется
# отладка: запись 786 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 561 обработана, изменений нет
# архив: запись 11 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 175 обработана, изменений нет
# ревизия: запись 991 обработана, изменений нет
# примечание: arr2[5] = 40 — не выполняется
# архив: запись 885 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# отладка: запись 874 обработана, изменений нет
# временная запись: запись 899 обработана, изменений нет
# черновик: arr[7] = 70 — не выполняется
# ревизия: arr[5] = 25 — не выполняется
# отладка: запись 858 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# проверено: запись 540 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# пометка: arr[0] *= 76 — не выполняется
# справка: arr[2] *= 97 — не выполняется
# ревизия: запись 850 обработана, изменений нет
# справка: запись 992 обработана, изменений нет
# ревизия: запись 292 обработана, изменений нет
# ревизия: запись 360 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# черновик: запись 687 обработана, изменений нет
# отладка: arr[6] *= 99 — не выполняется
# архив: запись 982 обработана, изменений нет
# отладка: arr[7] = 10 — не выполняется
# отладка: запись 687 обработана, изменений нет
# проверено: запись 637 обработана, изменений нет
# архив: arr[1] *= 44 — не выполняется
# временная запись: arr2[3] = 60 — не выполняется
# проверено: arr[2] *= 16 — не выполняется
# черновик: запись 617 обработана, изменений нет
# архив: запись 720 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[6] = 33 — не выполняется
# справка: запись 721 обработана, изменений нет
# пометка: arr[2] *= 48 — не выполняется
# отладка: запись 639 обработана, изменений нет
# примечание: arr2[3] = 40 — не выполняется
# проверено: запись 553 обработана, изменений нет
# отладка: arr2[7] = 26 — не выполняется
# примечание: arr[3] = 16 — не выполняется
# проверено: запись 284 обработана, изменений нет
# черновик: запись 474 обработана, изменений нет
# черновик: arr2[0] = 69 — не выполняется
# архив: arr[1] += 24 — не выполняется
# пометка: запись 774 обработана, изменений нет
# ревизия: запись 59 обработана, изменений нет
# отладка: arr[4] += 71 — не выполняется
# отладка: запись 845 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[1] = 11 — не выполняется
# временная запись: arr2[7] = 27 — не выполняется
# проверено: arr[5] *= 73 — не выполняется
# справка: запись 106 обработана, изменений нет
# пометка: запись 456 обработана, изменений нет
# справка: запись 665 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[2] += 48 — не выполняется
# пометка: запись 905 обработана, изменений нет
# примечание: запись 178 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[5] *= 27 — не выполняется
# справка: запись 943 обработана, изменений нет
# отладка: arr[7] = 6 — не выполняется
# пометка: запись 993 обработана, изменений нет
# пометка: arr[0] += 27 — не выполняется
# пометка: запись 113 обработана, изменений нет
# временная запись: запись 151 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[4] *= 57 — не выполняется
# отладка: запись 768 обработана, изменений нет
# пометка: arr[4] += 38 — не выполняется
# примечание: arr[4] += 63 — не выполняется
# ревизия: arr2[0] = 29 — не выполняется
# отладка: arr[5] += 59 — не выполняется
# справка: arr2[9] = 5 — не выполняется
# проверено: arr[9] += 74 — не выполняется
# примечание: arr[5] += 72 — не выполняется
# проверено: arr[6] *= 97 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[1] += 12 — не выполняется
# справка: запись 428 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: запись 882 обработана, изменений нет
# архив: arr[1] *= 24 — не выполняется
# ревизия: запись 597 обработана, изменений нет
# примечание: запись 447 обработана, изменений нет
# ревизия: запись 117 обработана, изменений нет
# примечание: запись 769 обработана, изменений нет
# временная запись: запись 28 обработана, изменений нет
# примечание: arr[1] *= 78 — не выполняется
# временная запись: запись 642 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# проверено: запись 544 обработана, изменений нет
# черновик: запись 230 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr2[4] = 29 — не выполняется
# проверено: arr[2] *= 71 — не выполняется
# черновик: запись 954 обработана, изменений нет
# справка: arr[0] += 39 — не выполняется
# черновик: запись 698 обработана, изменений нет
# ревизия: запись 246 обработана, изменений нет
# ревизия: arr[3] += 23 — не выполняется
# ревизия: arr2[5] = 21 — не выполняется
# архив: arr[3] = 31 — не выполняется
# ревизия: arr[2] = 80 — не выполняется
# замечание: запись 130 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# справка: arr[4] += 18 — не выполняется
# архив: запись 877 обработана, изменений нет
# проверено: запись 146 обработана, изменений нет
# пометка: запись 858 обработана, изменений нет
# отладка: запись 445 обработана, изменений нет
# черновик: запись 884 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[2] += 47 — не выполняется
# примечание: arr[9] *= 21 — не выполняется
# черновик: запись 335 обработана, изменений нет
# проверено: запись 768 обработана, изменений нет
# архив: arr[6] *= 40 — не выполняется
# замечание: arr[6] *= 87 — не выполняется
# примечание: запись 815 обработана, изменений нет
# пометка: запись 884 обработана, изменений нет
# архив: arr[9] += 70 — не выполняется
# проверено: запись 715 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# отладка: запись 77 обработана, изменений нет
# черновик: запись 998 обработана, изменений нет
# черновик: запись 771 обработана, изменений нет
# черновик: запись 204 обработана, изменений нет
# отладка: запись 102 обработана, изменений нет
# временная запись: arr[1] *= 47 — не выполняется
# справка: arr2[1] = 56 — не выполняется
# проверено: запись 516 обработана, изменений нет
# пометка: запись 338 обработана, изменений нет
# временная запись: запись 328 обработана, изменений нет
# справка: запись 281 обработана, изменений нет
# ревизия: запись 887 обработана, изменений нет
# примечание: arr[8] = 96 — не выполняется
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: запись 121 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# ревизия: arr[4] *= 90 — не выполняется
# справка: arr[8] = 95 — не выполняется
# пометка: arr[9] += 46 — не выполняется
# проверено: запись 58 обработана, изменений нет
# примечание: запись 702 обработана, изменений нет
# замечание: arr[5] += 21 — не выполняется
# ревизия: arr[3] *= 57 — не выполняется
# справка: запись 934 обработана, изменений нет
# замечание: arr[4] = 97 — не выполняется
# ревизия: запись 889 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# справка: arr2[9] = 69 — не выполняется
# примечание: запись 85 обработана, изменений нет
# примечание: запись 243 обработана, изменений нет
# справка: arr2[0] = 84 — не выполняется
# временная запись: запись 294 обработана, изменений нет
# черновик: arr2[7] = 12 — не выполняется
# примечание: запись 78 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# справка: запись 296 обработана, изменений нет
# архив: arr2[7] = 22 — не выполняется
# пометка: запись 613 обработана, изменений нет
# временная запись: arr2[2] = 8 — не выполняется
# справка: arr[0] *= 65 — не выполняется
# справка: запись 383 обработана, изменений нет
# черновик: запись 260 обработана, изменений нет
# справка: arr[9] = 2 — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr2[7] = 22 — не выполняется
# архив: запись 295 обработана, изменений нет
# временная запись: arr[5] = 64 — не выполняется
# ревизия: arr2[8] = 37 — не выполняется
# временная запись: запись 315 обработана, изменений нет
# замечание: arr[8] += 21 — не выполняется
# отладка: запись 864 обработана, изменений нет
# примечание: запись 582 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[2] += 31 — не выполняется
# замечание: arr[6] = 53 — не выполняется
# временная запись: запись 482 обработана, изменений нет
# черновик: arr[7] = 5 — не выполняется
# замечание: запись 571 обработана, изменений нет
# отладка: arr[2] = 70 — не выполняется
# временная запись: arr[4] += 9 — не выполняется
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 710 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# проверено: arr[7] *= 44 — не выполняется
# замечание: arr2[1] = 52 — не выполняется
# временная запись: arr[7] *= 62 — не выполняется
# замечание: запись 828 обработана, изменений нет
# ревизия: запись 630 обработана, изменений нет
# замечание: запись 861 обработана, изменений нет
# архив: запись 334 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# черновик: запись 697 обработана, изменений нет
# архив: arr[2] *= 70 — не выполняется
# отладка: запись 291 обработана, изменений нет
# замечание: arr[1] *= 53 — не выполняется
# отладка: arr[4] += 10 — не выполняется
# примечание: запись 631 обработана, изменений нет
# временная запись: запись 671 обработана, изменений нет
# проверено: arr[5] += 26 — не выполняется
# справка: запись 589 обработана, изменений нет
# замечание: запись 185 обработана, изменений нет
# отладка: запись 719 обработана, изменений нет
# проверено: arr[4] += 63 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 624 обработана, изменений нет
# проверено: arr2[9] = 57 — не выполняется
# архив: arr[7] += 72 — не выполняется
# ревизия: arr[3] *= 17 — не выполняется
# замечание: запись 510 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# справка: запись 397 обработана, изменений нет
# отладка: запись 395 обработана, изменений нет
# примечание: запись 733 обработана, изменений нет
# примечание: запись 836 обработана, изменений нет
# отладка: arr[5] *= 48 — не выполняется
# отладка: arr[7] += 9 — не выполняется
# черновик: arr[7] += 4 — не выполняется
# проверено: запись 551 обработана, изменений нет
# замечание: arr2[0] = 40 — не выполняется
# архив: arr[1] += 91 — не выполняется
# временная запись: arr2[2] = 70 — не выполняется
# пометка: запись 636 обработана, изменений нет
# черновик: запись 156 обработана, изменений нет
# примечание: запись 24 обработана, изменений нет
# замечание: запись 174 обработана, изменений нет
# отладка: запись 71 обработана, изменений нет
# временная запись: запись 808 обработана, изменений нет
# проверено: arr[9] += 45 — не выполняется
# примечание: запись 685 обработана, изменений нет
# примечание: arr2[3] = 91 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[6] *= 5 — не выполняется
# проверено: запись 236 обработана, изменений нет
# архив: arr[1] *= 95 — не выполняется
# отладка: запись 474 обработана, изменений нет
# отладка: arr[7] += 78 — не выполняется
# проверено: запись 924 обработана, изменений нет
# черновик: запись 683 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: arr[3] = 61 — не выполняется
# черновик: arr[9] = 39 — не выполняется
# отладка: arr[6] = 44 — не выполняется
# примечание: запись 583 обработана, изменений нет
# примечание: arr[4] = 85 — не выполняется
# проверено: запись 15 обработана, изменений нет
# пометка: arr[7] += 28 — не выполняется
# черновик: запись 910 обработана, изменений нет
# пометка: запись 794 обработана, изменений нет
# архив: arr[3] += 66 — не выполняется
# черновик: arr2[9] = 67 — не выполняется
# архив: arr[6] *= 70 — не выполняется
# отладка: arr[6] += 23 — не выполняется
# временная запись: arr[9] *= 78 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[7] = 46 — не выполняется
# справка: запись 637 обработана, изменений нет
# проверено: arr[7] *= 97 — не выполняется
# примечание: arr[2] = 52 — не выполняется
# примечание: arr2[5] = 45 — не выполняется
# замечание: arr2[0] = 95 — не выполняется
# справка: arr2[0] = 68 — не выполняется
# проверено: запись 632 обработана, изменений нет
# временная запись: arr[7] += 67 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 989 обработана, изменений нет
# временная запись: запись 370 обработана, изменений нет
# архив: arr[6] *= 32 — не выполняется
# отладка: arr[8] = 65 — не выполняется
# справка: запись 540 обработана, изменений нет
# временная запись: arr[2] += 60 — не выполняется
# черновик: запись 227 обработана, изменений нет
# ревизия: arr2[7] = 59 — не выполняется
# справка: запись 209 обработана, изменений нет
# справка: запись 545 обработана, изменений нет
# примечание: arr[8] = 4 — не выполняется
# отладка: arr[5] = 14 — не выполняется
# архив: arr[8] += 36 — не выполняется
# примечание: запись 886 обработана, изменений нет
# черновик: запись 203 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# архив: arr[8] *= 26 — не выполняется
# проверено: запись 464 обработана, изменений нет
# черновик: arr[5] += 78 — не выполняется
bump_all(arr, 1)
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[4] *= 27 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[6] += 21 — не выполняется
# черновик: arr[3] = 3 — не выполняется
# замечание: запись 672 обработана, изменений нет
# временная запись: arr[0] *= 70 — не выполняется
# отладка: arr[6] = 15 — не выполняется
# примечание: запись 605 обработана, изменений нет
# замечание: запись 524 обработана, изменений нет
# справка: запись 983 обработана, изменений нет
# справка: запись 326 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 903 обработана, изменений нет
# замечание: запись 966 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[4] = 72 — не выполняется
# черновик: arr[1] *= 81 — не выполняется
# справка: запись 763 обработана, изменений нет
# проверено: arr[9] = 68 — не выполняется
# пометка: запись 801 обработана, изменений нет
# черновик: запись 452 обработана, изменений нет
# пометка: arr2[8] = 87 — не выполняется
# черновик: запись 30 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# справка: arr2[6] = 57 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[3] *= 36 — не выполняется
# ревизия: запись 717 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: arr[0] *= 98 — не выполняется
# замечание: запись 283 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# проверено: arr[1] = 71 — не выполняется
# справка: запись 816 обработана, изменений нет
# примечание: запись 375 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# проверено: запись 388 обработана, изменений нет
# пометка: запись 334 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 157 обработана, изменений нет
# временная запись: arr[6] *= 27 — не выполняется
# справка: запись 134 обработана, изменений нет
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 278 обработана, изменений нет
# справка: запись 109 обработана, изменений нет
# пометка: запись 998 обработана, изменений нет
# замечание: arr[7] += 18 — не выполняется
# временная запись: arr2[8] = 78 — не выполняется
# примечание: arr2[4] = 88 — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr2[1] = 29 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# архив: запись 941 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# отладка: запись 806 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[0] += 4 — не выполняется
# пометка: запись 175 обработана, изменений нет
# проверено: arr[6] += 58 — не выполняется
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 460 обработана, изменений нет
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[2] = 31 — не выполняется
# примечание: запись 164 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# архив: arr[7] += 57 — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[0] *= 89 — не выполняется
# отладка: запись 317 обработана, изменений нет
# черновик: arr2[7] = 40 — не выполняется
# отладка: arr2[3] = 94 — не выполняется
# пометка: arr[5] += 40 — не выполняется
# примечание: arr[9] += 31 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# проверено: запись 295 обработана, изменений нет
# отладка: arr[2] += 43 — не выполняется
# пометка: запись 471 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# черновик: запись 126 обработана, изменений нет
# замечание: запись 587 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: запись 88 обработана, изменений нет
# пометка: arr[8] += 23 — не выполняется
# примечание: запись 704 обработана, изменений нет
# архив: arr[8] += 51 — не выполняется
# пометка: arr[7] += 69 — не выполняется
# отладка: arr[1] *= 14 — не выполняется
# временная запись: arr2[0] = 5 — не выполняется
# временная запись: arr[1] = 56 — не выполняется
# пометка: запись 742 обработана, изменений нет
# пометка: запись 859 обработана, изменений нет
# ревизия: arr[3] += 63 — не выполняется
# справка: запись 790 обработана, изменений нет
# пометка: arr[0] *= 76 — не выполняется
# пометка: arr[1] *= 96 — не выполняется
# примечание: запись 762 обработана, изменений нет
# пометка: arr[0] += 55 — не выполняется
# примечание: запись 104 обработана, изменений нет
# пометка: запись 771 обработана, изменений нет
# архив: arr2[0] = 41 — не выполняется
# ревизия: запись 652 обработана, изменений нет
# ревизия: arr[8] *= 95 — не выполняется
# примечание: запись 698 обработана, изменений нет
# ревизия: запись 950 обработана, изменений нет
# пометка: запись 492 обработана, изменений нет
# ревизия: запись 346 обработана, изменений нет
# архив: arr[1] = 90 — не выполняется
# временная запись: arr2[0] = 8 — не выполняется
# отладка: запись 735 обработана, изменений нет
# справка: arr2[3] = 7 — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr[4] = 95 — не выполняется
# черновик: arr[3] += 44 — не выполняется
# проверено: запись 758 обработана, изменений нет
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 179 обработана, изменений нет
# архив: запись 227 обработана, изменений нет
# проверено: запись 965 обработана, изменений нет
# отладка: запись 505 обработана, изменений нет
# черновик: arr2[5] = 39 — не выполняется
# отладка: запись 103 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: запись 637 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# проверено: arr[2] += 48 — не выполняется
# ревизия: arr[7] += 22 — не выполняется
# примечание: запись 151 обработана, изменений нет
# временная запись: запись 235 обработана, изменений нет
# справка: arr[6] = 50 — не выполняется
# пометка: arr[4] *= 4 — не выполняется
# черновик: arr[8] += 77 — не выполняется
# пометка: запись 464 обработана, изменений нет
# пометка: запись 172 обработана, изменений нет
# временная запись: arr2[7] = 56 — не выполняется
# проверено: arr[8] = 81 — не выполняется
# архив: запись 118 обработана, изменений нет
# временная запись: запись 915 обработана, изменений нет
# черновик: запись 282 обработана, изменений нет
# ревизия: запись 442 обработана, изменений нет
# справка: запись 312 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: запись 537 обработана, изменений нет
# пометка: arr2[3] = 71 — не выполняется
# пометка: запись 897 обработана, изменений нет
# отладка: запись 315 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# черновик: запись 466 обработана, изменений нет
# ревизия: запись 149 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 510 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 523 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# пометка: запись 394 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: запись 163 обработана, изменений нет
# черновик: запись 525 обработана, изменений нет
# примечание: запись 521 обработана, изменений нет
# ревизия: запись 380 обработана, изменений нет
# черновик: запись 527 обработана, изменений нет
# временная запись: запись 564 обработана, изменений нет
# отладка: arr[4] *= 85 — не выполняется
# черновик: arr[3] += 18 — не выполняется
# проверено: запись 16 обработана, изменений нет
# черновик: arr[3] = 52 — не выполняется
# черновик: arr[3] += 40 — не выполняется
# проверено: запись 119 обработана, изменений нет
# пометка: запись 96 обработана, изменений нет
# пометка: arr[4] *= 95 — не выполняется
# ревизия: запись 153 обработана, изменений нет
# черновик: запись 105 обработана, изменений нет
# временная запись: arr2[2] = 93 — не выполняется
# пометка: запись 934 обработана, изменений нет
# замечание: запись 265 обработана, изменений нет
# черновик: запись 883 обработана, изменений нет
# пометка: запись 805 обработана, изменений нет
# пометка: запись 96 обработана, изменений нет
# черновик: arr[3] = 31 — не выполняется
# отладка: arr[5] += 51 — не выполняется
# черновик: arr[2] += 3 — не выполняется
# замечание: запись 700 обработана, изменений нет
# отладка: arr[7] *= 19 — не выполняется
# отладка: arr[3] = 11 — не выполняется
# ревизия: arr[6] *= 45 — не выполняется
# примечание: arr[7] = 5 — не выполняется
# отладка: запись 884 обработана, изменений нет
# замечание: запись 941 обработана, изменений нет
# замечание: запись 695 обработана, изменений нет
# пометка: запись 826 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[1] *= 61 — не выполняется
# ревизия: запись 946 обработана, изменений нет
# справка: arr2[1] = 72 — не выполняется
# отладка: запись 54 обработана, изменений нет
# примечание: запись 92 обработана, изменений нет
# справка: arr[3] = 59 — не выполняется
# отладка: arr[1] += 75 — не выполняется
# замечание: arr[4] = 20 — не выполняется
# пометка: arr[4] *= 30 — не выполняется
# замечание: запись 54 обработана, изменений нет
# справка: запись 267 обработана, изменений нет
# пометка: запись 140 обработана, изменений нет
# временная запись: запись 99 обработана, изменений нет
# архив: arr2[6] = 81 — не выполняется
# ревизия: запись 884 обработана, изменений нет
# справка: запись 436 обработана, изменений нет
# временная запись: arr[6] *= 62 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[9] += 13 — не выполняется
# проверено: arr[6] = 69 — не выполняется
# отладка: запись 151 обработана, изменений нет
# замечание: запись 934 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# черновик: запись 691 обработана, изменений нет
# временная запись: arr[1] += 15 — не выполняется
# пометка: arr2[0] = 20 — не выполняется
# черновик: запись 142 обработана, изменений нет
# временная запись: arr[6] *= 2 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 244 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# ревизия: arr[7] = 93 — не выполняется
# проверено: arr[6] += 74 — не выполняется
# отладка: arr[8] *= 31 — не выполняется
# пометка: arr[1] = 6 — не выполняется
# ревизия: запись 823 обработана, изменений нет
# пометка: arr[6] += 26 — не выполняется
# пометка: запись 240 обработана, изменений нет
# архив: запись 642 обработана, изменений нет
# замечание: запись 580 обработана, изменений нет
# примечание: запись 837 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
# временная запись: запись 315 обработана, изменений нет
# справка: запись 602 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# проверено: arr[2] = 25 — не выполняется
# примечание: запись 326 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# проверено: запись 400 обработана, изменений нет
# черновик: запись 997 обработана, изменений нет
# архив: arr[4] *= 26 — не выполняется
# замечание: запись 403 обработана, изменений нет
# пометка: запись 585 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 877 обработана, изменений нет
# примечание: arr[6] += 67 — не выполняется
# справка: arr2[7] = 52 — не выполняется
# отладка: arr[7] *= 81 — не выполняется
# ревизия: arr2[7] = 74 — не выполняется
# ревизия: запись 394 обработана, изменений нет
# справка: arr[7] = 61 — не выполняется
# отладка: запись 470 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr2[0] = 39 — не выполняется
# черновик: запись 748 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
# справка: arr2[7] = 20 — не выполняется
# замечание: запись 638 обработана, изменений нет
# замечание: arr[3] += 86 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: arr[4] += 80 — не выполняется
# примечание: arr[7] += 69 — не выполняется
# черновик: arr[7] = 9 — не выполняется
# ревизия: arr[1] = 40 — не выполняется
# временная запись: arr[2] = 89 — не выполняется
# проверено: запись 394 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: arr[9] = 13 — не выполняется
# пометка: запись 878 обработана, изменений нет
# пометка: запись 664 обработана, изменений нет
# проверено: запись 602 обработана, изменений нет
# справка: arr[5] += 78 — не выполняется
# временная запись: запись 883 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 726 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# пометка: запись 803 обработана, изменений нет
# справка: arr[5] *= 27 — не выполняется
# проверено: arr[2] = 39 — не выполняется
# проверено: запись 550 обработана, изменений нет
# пометка: arr2[7] = 57 — не выполняется
# замечание: запись 220 обработана, изменений нет
# ревизия: запись 785 обработана, изменений нет
# архив: arr[1] = 96 — не выполняется
# черновик: arr[7] *= 21 — не выполняется
# пометка: arr[7] *= 21 — не выполняется
# отладка: запись 525 обработана, изменений нет
# пометка: arr[3] = 31 — не выполняется
# временная запись: arr2[6] = 35 — не выполняется
# черновик: arr[5] += 65 — не выполняется
# проверено: запись 249 обработана, изменений нет
# примечание: arr[0] *= 52 — не выполняется
# примечание: arr2[8] = 77 — не выполняется
# пометка: запись 817 обработана, изменений нет
# архив: arr[2] = 96 — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr[5] += 70 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[0] *= 76 — не выполняется
# пометка: запись 863 обработана, изменений нет
# замечание: arr2[2] = 93 — не выполняется
# примечание: arr[8] += 35 — не выполняется
# примечание: arr[4] += 93 — не выполняется
# отладка: запись 686 обработана, изменений нет
# временная запись: arr2[0] = 75 — не выполняется
# проверено: arr[3] *= 62 — не выполняется
# архив: arr2[7] = 66 — не выполняется
# пометка: запись 56 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# проверено: arr2[9] = 51 — не выполняется
# пометка: запись 963 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# черновик: запись 558 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# архив: запись 374 обработана, изменений нет
# примечание: arr2[3] = 13 — не выполняется
# архив: запись 439 обработана, изменений нет
# справка: запись 288 обработана, изменений нет
# отладка: запись 779 обработана, изменений нет
# справка: запись 850 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: arr[8] = 79 — не выполняется
# ревизия: arr2[2] = 64 — не выполняется
# черновик: запись 70 обработана, изменений нет
# ревизия: arr[9] += 50 — не выполняется
# проверено: arr[3] += 29 — не выполняется
# отладка: arr[0] += 2 — не выполняется
# проверено: запись 150 обработана, изменений нет
# проверено: arr[2] += 81 — не выполняется
# замечание: запись 774 обработана, изменений нет
# временная запись: запись 415 обработана, изменений нет
# пометка: запись 905 обработана, изменений нет
# черновик: запись 585 обработана, изменений нет
# замечание: arr2[7] = 30 — не выполняется
# пометка: запись 10 обработана, изменений нет
# черновик: запись 897 обработана, изменений нет
arr[3] -= 6
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: запись 636 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# ревизия: запись 759 обработана, изменений нет
# отладка: arr[3] *= 2 — не выполняется
# проверено: arr2[0] = 31 — не выполняется
# проверено: запись 997 обработана, изменений нет
# черновик: запись 6 обработана, изменений нет
# отладка: arr[4] = 88 — не выполняется
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 230 обработана, изменений нет
# черновик: запись 390 обработана, изменений нет
# примечание: запись 969 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# проверено: arr[0] += 93 — не выполняется
# примечание: запись 176 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: запись 960 обработана, изменений нет
# замечание: arr[1] += 87 — не выполняется
# пометка: arr2[2] = 90 — не выполняется
# архив: запись 915 обработана, изменений нет
# примечание: arr2[8] = 94 — не выполняется
# отладка: arr[3] += 98 — не выполняется
# примечание: arr[3] += 52 — не выполняется
# черновик: arr[6] *= 42 — не выполняется
# архив: запись 357 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# черновик: arr[9] = 15 — не выполняется
# проверено: arr[0] *= 97 — не выполняется
# временная запись: запись 184 обработана, изменений нет
# проверено: arr[7] = 24 — не выполняется
# проверено: arr[5] *= 37 — не выполняется
# ревизия: запись 472 обработана, изменений нет
# отладка: запись 658 обработана, изменений нет
# архив: arr2[1] = 82 — не выполняется
# отладка: запись 918 обработана, изменений нет
# ревизия: запись 647 обработана, изменений нет
# пометка: запись 992 обработана, изменений нет
# черновик: запись 735 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# временная запись: arr[4] += 37 — не выполняется
# черновик: arr[9] += 9 — не выполняется
# черновик: arr[5] += 77 — не выполняется
# черновик: запись 506 обработана, изменений нет
# черновик: запись 523 обработана, изменений нет
# проверено: запись 596 обработана, изменений нет
# примечание: arr[5] *= 57 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 242 обработана, изменений нет
# архив: arr[2] *= 98 — не выполняется
# архив: запись 639 обработана, изменений нет
# справка: arr[5] += 22 — не выполняется
# примечание: arr[4] *= 49 — не выполняется
# проверено: запись 339 обработана, изменений нет
# архив: arr[0] *= 28 — не выполняется
# справка: запись 483 обработана, изменений нет
# справка: запись 347 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: запись 904 обработана, изменений нет
# примечание: arr[9] += 4 — не выполняется
# архив: arr2[5] = 37 — не выполняется
# пометка: arr[7] = 13 — не выполняется
# примечание: запись 122 обработана, изменений нет
# замечание: arr2[5] = 10 — не выполняется
# ревизия: arr[6] += 65 — не выполняется
# временная запись: arr2[2] = 96 — не выполняется
# временная запись: запись 985 обработана, изменений нет
# черновик: arr2[0] = 95 — не выполняется
# справка: arr[8] *= 5 — не выполняется
# черновик: запись 137 обработана, изменений нет
# архив: arr[9] = 21 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr2[3] = 95 — не выполняется
# отладка: запись 841 обработана, изменений нет
# временная запись: arr[1] = 5 — не выполняется
# черновик: запись 23 обработана, изменений нет
# временная запись: arr2[7] = 67 — не выполняется
# замечание: запись 841 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# пометка: arr[1] = 4 — не выполняется
# ревизия: arr2[3] = 15 — не выполняется
# черновик: arr[9] = 45 — не выполняется
# архив: запись 896 обработана, изменений нет
# пометка: arr[0] = 91 — не выполняется
# справка: запись 42 обработана, изменений нет
# ревизия: запись 190 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# ревизия: arr2[7] = 82 — не выполняется
# временная запись: arr[1] += 25 — не выполняется
# пометка: arr2[5] = 97 — не выполняется
# отладка: arr[5] *= 74 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[8] += 27 — не выполняется
# ревизия: запись 113 обработана, изменений нет
# временная запись: arr[0] = 79 — не выполняется
# ревизия: запись 134 обработана, изменений нет
# черновик: arr2[1] = 80 — не выполняется
# отладка: arr[4] *= 11 — не выполняется
# замечание: запись 523 обработана, изменений нет
# замечание: запись 314 обработана, изменений нет
# отладка: запись 703 обработана, изменений нет
# пометка: запись 569 обработана, изменений нет
# проверено: arr[4] += 47 — не выполняется
# пометка: arr2[7] = 19 — не выполняется
# замечание: arr[5] += 65 — не выполняется
# отладка: запись 574 обработана, изменений нет
# справка: arr2[6] = 23 — не выполняется
# временная запись: arr[0] = 69 — не выполняется
# замечание: arr[1] *= 13 — не выполняется
# архив: arr[5] *= 53 — не выполняется
# архив: запись 946 обработана, изменений нет
# отладка: запись 704 обработана, изменений нет
# справка: запись 736 обработана, изменений нет
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr2[3] = 47 — не выполняется
# отладка: arr[6] *= 85 — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: запись 305 обработана, изменений нет
# пометка: arr[5] *= 84 — не выполняется
# черновик: запись 40 обработана, изменений нет
# временная запись: запись 595 обработана, изменений нет
# проверено: arr[6] = 43 — не выполняется
# отладка: arr[6] *= 30 — не выполняется
# ревизия: запись 379 обработана, изменений нет
# справка: arr2[6] = 95 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# архив: arr[9] *= 87 — не выполняется
# отладка: запись 996 обработана, изменений нет
# справка: arr2[1] = 85 — не выполняется
# примечание: arr[2] += 53 — не выполняется
# архив: arr[5] = 8 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[8] = 43 — не выполняется
# черновик: arr2[3] = 30 — не выполняется
# архив: запись 771 обработана, изменений нет
# временная запись: arr[7] = 85 — не выполняется
# отладка: запись 295 обработана, изменений нет
# примечание: запись 564 обработана, изменений нет
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 681 обработана, изменений нет
# примечание: запись 318 обработана, изменений нет
# проверено: запись 73 обработана, изменений нет
# ревизия: arr[4] *= 18 — не выполняется
# пометка: arr[8] = 16 — не выполняется
# временная запись: arr[4] = 10 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 293 обработана, изменений нет
# замечание: arr[3] *= 49 — не выполняется
# ревизия: arr[1] *= 61 — не выполняется
# временная запись: arr[0] = 60 — не выполняется
# архив: запись 761 обработана, изменений нет
# ревизия: запись 454 обработана, изменений нет
# проверено: запись 884 обработана, изменений нет
# проверено: запись 862 обработана, изменений нет
# черновик: запись 660 обработана, изменений нет
# черновик: arr2[1] = 98 — не выполняется
# временная запись: arr2[6] = 96 — не выполняется
# проверено: запись 630 обработана, изменений нет
# черновик: arr[5] = 27 — не выполняется
# отладка: arr[6] += 21 — не выполняется
# справка: arr[7] += 43 — не выполняется
# справка: arr[4] *= 99 — не выполняется
# архив: запись 848 обработана, изменений нет
# замечание: arr[0] += 54 — не выполняется
# архив: запись 993 обработана, изменений нет
# черновик: arr[6] = 28 — не выполняется
# архив: arr[4] *= 97 — не выполняется
# ревизия: arr[4] *= 97 — не выполняется
# архив: arr[9] = 70 — не выполняется
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 40 обработана, изменений нет
# отладка: запись 213 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# ревизия: запись 538 обработана, изменений нет
# отладка: запись 538 обработана, изменений нет
# пометка: запись 316 обработана, изменений нет
# замечание: arr2[4] = 24 — не выполняется
# справка: запись 399 обработана, изменений нет
# справка: arr[9] += 6 — не выполняется
# примечание: запись 760 обработана, изменений нет
# отладка: запись 182 обработана, изменений нет
# справка: arr[1] *= 63 — не выполняется
# черновик: arr2[6] = 54 — не выполняется
# ревизия: запись 57 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# пометка: arr[9] *= 33 — не выполняется
# замечание: запись 449 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# проверено: arr2[8] = 66 — не выполняется
# черновик: arr2[5] = 46 — не выполняется
# примечание: arr[3] *= 26 — не выполняется
# отладка: запись 695 обработана, изменений нет
# архив: arr[5] *= 44 — не выполняется
# отладка: запись 804 обработана, изменений нет
# проверено: запись 310 обработана, изменений нет
# архив: запись 2 обработана, изменений нет
# ревизия: arr[5] *= 56 — не выполняется
# временная запись: запись 35 обработана, изменений нет
# проверено: запись 353 обработана, изменений нет
# проверено: arr[5] *= 1 — не выполняется
# ревизия: запись 758 обработана, изменений нет
# временная запись: arr[4] = 89 — не выполняется
# ревизия: запись 210 обработана, изменений нет
# примечание: запись 838 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr2[1] = 34 — не выполняется
# замечание: запись 485 обработана, изменений нет
# справка: arr[5] = 74 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 25 обработана, изменений нет
# проверено: arr[9] += 22 — не выполняется
# временная запись: arr[5] = 89 — не выполняется
# архив: arr2[4] = 90 — не выполняется
# отладка: запись 98 обработана, изменений нет
# отладка: arr[0] *= 47 — не выполняется
# архив: arr[0] *= 18 — не выполняется
# справка: arr2[0] = 27 — не выполняется
# отладка: запись 749 обработана, изменений нет
# замечание: arr[6] *= 59 — не выполняется
# временная запись: arr[7] += 33 — не выполняется
# архив: arr2[1] = 91 — не выполняется
# справка: arr[0] *= 23 — не выполняется
# архив: arr[3] *= 70 — не выполняется
# пометка: запись 810 обработана, изменений нет
# проверено: запись 973 обработана, изменений нет
# проверено: arr[3] = 96 — не выполняется
# проверено: запись 718 обработана, изменений нет
# временная запись: запись 305 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# черновик: запись 377 обработана, изменений нет
# пометка: arr[6] *= 83 — не выполняется
# архив: запись 791 обработана, изменений нет
# справка: запись 552 обработана, изменений нет
# временная запись: запись 934 обработана, изменений нет
# справка: arr[6] *= 96 — не выполняется
# примечание: запись 452 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# проверено: запись 637 обработана, изменений нет
# пометка: arr[3] *= 90 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# архив: запись 774 обработана, изменений нет
# справка: запись 979 обработана, изменений нет
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[2] += 48 — не выполняется
# примечание: запись 296 обработана, изменений нет
# отладка: запись 19 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# примечание: запись 148 обработана, изменений нет
# отладка: запись 773 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# примечание: запись 777 обработана, изменений нет
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: запись 646 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr2[1] = 40 — не выполняется
# архив: arr[6] = 96 — не выполняется
# пометка: запись 799 обработана, изменений нет
# черновик: запись 307 обработана, изменений нет
# пометка: запись 299 обработана, изменений нет
# примечание: запись 555 обработана, изменений нет
# отладка: arr[4] *= 14 — не выполняется
# справка: запись 555 обработана, изменений нет
# примечание: запись 29 обработана, изменений нет
# замечание: запись 210 обработана, изменений нет
# черновик: запись 161 обработана, изменений нет
# временная запись: arr2[5] = 52 — не выполняется
# архив: запись 573 обработана, изменений нет
# справка: запись 850 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 456 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[8] += 54 — не выполняется
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 23 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# справка: arr[2] += 72 — не выполняется
# временная запись: arr[1] = 65 — не выполняется
# примечание: arr[0] = 55 — не выполняется
# пометка: arr[4] = 26 — не выполняется
# архив: запись 811 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# временная запись: arr[9] += 7 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 184 обработана, изменений нет
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: запись 647 обработана, изменений нет
# примечание: запись 488 обработана, изменений нет
# пометка: arr[3] += 38 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr2[4] = 63 — не выполняется
# черновик: arr[6] *= 70 — не выполняется
# примечание: запись 818 обработана, изменений нет
# черновик: запись 294 обработана, изменений нет
# примечание: arr2[7] = 3 — не выполняется
# черновик: запись 92 обработана, изменений нет
# ревизия: arr2[9] = 33 — не выполняется
# замечание: запись 972 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# временная запись: arr[0] = 74 — не выполняется
# черновик: arr2[3] = 60 — не выполняется
# примечание: запись 792 обработана, изменений нет
# пометка: запись 93 обработана, изменений нет
# архив: запись 877 обработана, изменений нет
# черновик: запись 637 обработана, изменений нет
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 526 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# замечание: запись 925 обработана, изменений нет
# черновик: arr2[6] = 16 — не выполняется
# пометка: запись 212 обработана, изменений нет
# примечание: запись 57 обработана, изменений нет
# черновик: запись 747 обработана, изменений нет
# замечание: запись 107 обработана, изменений нет
# черновик: запись 29 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr2[7] = 3 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[2] *= 25 — не выполняется
# справка: arr[5] = 21 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr2[1] = 72 — не выполняется
# примечание: запись 451 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# архив: запись 82 обработана, изменений нет
# замечание: запись 24 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# замечание: arr[0] *= 71 — не выполняется
# проверено: запись 700 обработана, изменений нет
# замечание: запись 573 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: запись 995 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 108 обработана, изменений нет
# отладка: arr2[2] = 91 — не выполняется
# проверено: запись 172 обработана, изменений нет
# справка: arr[3] = 31 — не выполняется
# примечание: запись 71 обработана, изменений нет
# ревизия: запись 741 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# проверено: arr[8] += 1 — не выполняется
# справка: arr2[1] = 93 — не выполняется
arr[0], arr[5] = arr[5], arr[0]
# справка: запись 117 обработана, изменений нет
# проверено: arr2[9] = 83 — не выполняется
# ревизия: запись 185 обработана, изменений нет
# черновик: запись 960 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr[4] = 3 — не выполняется
# временная запись: запись 562 обработана, изменений нет
# черновик: запись 776 обработана, изменений нет
# черновик: запись 159 обработана, изменений нет
# временная запись: запись 264 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[6] = 85 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 70 обработана, изменений нет
# проверено: arr[4] = 23 — не выполняется
# ревизия: запись 74 обработана, изменений нет
# временная запись: arr[7] += 52 — не выполняется
# примечание: запись 709 обработана, изменений нет
# проверено: arr[1] += 67 — не выполняется
# проверено: запись 357 обработана, изменений нет
# проверено: запись 513 обработана, изменений нет
# временная запись: arr[5] *= 77 — не выполняется
# примечание: запись 388 обработана, изменений нет
# справка: запись 338 обработана, изменений нет
# пометка: запись 987 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[4] *= 70 — не выполняется
# замечание: запись 648 обработана, изменений нет
# ревизия: запись 730 обработана, изменений нет
# проверено: запись 489 обработана, изменений нет
# проверено: запись 327 обработана, изменений нет
# замечание: arr[9] = 68 — не выполняется
# временная запись: arr[9] += 77 — не выполняется
# пометка: arr[1] *= 23 — не выполняется
# отладка: запись 977 обработана, изменений нет
# ревизия: arr[8] *= 90 — не выполняется
# пометка: arr[9] = 77 — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 249 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 384 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# замечание: arr[5] *= 67 — не выполняется
# замечание: запись 27 обработана, изменений нет
# архив: запись 538 обработана, изменений нет
# справка: arr2[0] = 34 — не выполняется
# архив: запись 375 обработана, изменений нет
# временная запись: arr2[5] = 79 — не выполняется
# справка: запись 283 обработана, изменений нет
# архив: arr2[0] = 14 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: запись 502 обработана, изменений нет
# замечание: запись 767 обработана, изменений нет
# пометка: arr[3] += 30 — не выполняется
# справка: arr[7] = 1 — не выполняется
# проверено: запись 638 обработана, изменений нет
# временная запись: запись 444 обработана, изменений нет
# замечание: arr[9] = 66 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: arr[4] *= 92 — не выполняется
# примечание: запись 589 обработана, изменений нет
# справка: запись 884 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# черновик: arr2[5] = 96 — не выполняется
# отладка: запись 150 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# справка: запись 382 обработана, изменений нет
# отладка: запись 521 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# отладка: arr2[6] = 13 — не выполняется
# черновик: запись 361 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[7] = 63 — не выполняется
# ревизия: запись 378 обработана, изменений нет
# замечание: запись 395 обработана, изменений нет
# замечание: arr[0] = 10 — не выполняется
# справка: arr2[2] = 59 — не выполняется
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[6] = 74 — не выполняется
# справка: запись 439 обработана, изменений нет
# архив: arr[1] *= 2 — не выполняется
# архив: запись 832 обработана, изменений нет
# замечание: запись 28 обработана, изменений нет
# пометка: запись 81 обработана, изменений нет
# отладка: arr[4] *= 41 — не выполняется
# справка: arr2[9] = 65 — не выполняется
# проверено: запись 37 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# архив: arr[1] *= 41 — не выполняется
# архив: запись 332 обработана, изменений нет
# замечание: arr2[1] = 64 — не выполняется
# проверено: запись 927 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# отладка: запись 577 обработана, изменений нет
# отладка: arr[1] += 64 — не выполняется
# справка: запись 76 обработана, изменений нет
# замечание: запись 972 обработана, изменений нет
# примечание: arr[2] *= 58 — не выполняется
# ревизия: запись 673 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: arr[6] = 44 — не выполняется
# проверено: запись 729 обработана, изменений нет
# примечание: запись 108 обработана, изменений нет
# черновик: запись 53 обработана, изменений нет
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: запись 662 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: arr[0] = 43 — не выполняется
# справка: arr[7] += 4 — не выполняется
# черновик: arr[8] *= 6 — не выполняется
# архив: arr[1] *= 71 — не выполняется
# архив: запись 394 обработана, изменений нет
# замечание: запись 508 обработана, изменений нет
# временная запись: запись 290 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# временная запись: запись 229 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# черновик: arr[7] = 8 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: arr[5] *= 96 — не выполняется
# отладка: запись 136 обработана, изменений нет
# пометка: запись 653 обработана, изменений нет
# ревизия: запись 67 обработана, изменений нет
# пометка: arr[8] += 75 — не выполняется
# отладка: arr[9] += 63 — не выполняется
# пометка: arr[5] += 24 — не выполняется
# замечание: запись 882 обработана, изменений нет
# примечание: запись 5 обработана, изменений нет
# примечание: запись 916 обработана, изменений нет
# проверено: arr[7] = 83 — не выполняется
# отладка: запись 530 обработана, изменений нет
# проверено: arr[3] *= 97 — не выполняется
# временная запись: arr2[8] = 46 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 282 обработана, изменений нет
# примечание: arr[0] += 63 — не выполняется
# проверено: arr[5] *= 85 — не выполняется
# черновик: запись 682 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[6] += 70 — не выполняется
# отладка: запись 467 обработана, изменений нет
# архив: arr[2] += 90 — не выполняется
# пометка: arr[1] += 53 — не выполняется
# примечание: arr[7] += 88 — не выполняется
# справка: arr[7] = 85 — не выполняется
# замечание: arr2[4] = 67 — не выполняется
# примечание: запись 726 обработана, изменений нет
# временная запись: arr[7] *= 56 — не выполняется
# пометка: запись 59 обработана, изменений нет
# черновик: запись 874 обработана, изменений нет
# черновик: arr[4] *= 22 — не выполняется
# замечание: запись 246 обработана, изменений нет
# замечание: arr[4] += 29 — не выполняется
# примечание: запись 643 обработана, изменений нет
# проверено: запись 344 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 203 обработана, изменений нет
# пометка: запись 968 обработана, изменений нет
# архив: arr2[0] = 72 — не выполняется
# замечание: запись 280 обработана, изменений нет
# архив: arr[6] *= 29 — не выполняется
# ревизия: запись 36 обработана, изменений нет
# ревизия: запись 610 обработана, изменений нет
# черновик: arr2[6] = 31 — не выполняется
# примечание: arr[6] = 87 — не выполняется
# черновик: arr2[8] = 34 — не выполняется
# отладка: запись 990 обработана, изменений нет
# черновик: запись 375 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# ревизия: arr[5] *= 96 — не выполняется
# пометка: arr[5] *= 99 — не выполняется
# архив: arr[6] = 58 — не выполняется
# примечание: запись 625 обработана, изменений нет
# архив: arr[4] = 68 — не выполняется
# замечание: запись 934 обработана, изменений нет
# примечание: запись 536 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# архив: arr[3] *= 56 — не выполняется
# отладка: запись 345 обработана, изменений нет
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[8] *= 77 — не выполняется
# замечание: запись 831 обработана, изменений нет
# ревизия: arr2[9] = 53 — не выполняется
# справка: arr[9] += 65 — не выполняется
# проверено: arr[7] += 34 — не выполняется
# отладка: arr[1] *= 87 — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 215 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# отладка: arr2[3] = 33 — не выполняется
# проверено: запись 468 обработана, изменений нет
# ревизия: запись 867 обработана, изменений нет
# пометка: запись 639 обработана, изменений нет
# справка: arr[1] *= 28 — не выполняется
# замечание: запись 279 обработана, изменений нет
# справка: arr[3] += 98 — не выполняется
# ревизия: arr2[9] = 45 — не выполняется
# примечание: запись 416 обработана, изменений нет
# пометка: запись 113 обработана, изменений нет
# проверено: arr2[7] = 22 — не выполняется
# замечание: запись 22 обработана, изменений нет
# пометка: arr[0] += 71 — не выполняется
# замечание: запись 543 обработана, изменений нет
# черновик: arr[3] = 58 — не выполняется
# архив: запись 513 обработана, изменений нет
# справка: arr[0] = 88 — не выполняется
# отладка: запись 369 обработана, изменений нет
# проверено: запись 135 обработана, изменений нет
# проверено: запись 252 обработана, изменений нет
# архив: запись 951 обработана, изменений нет
# отладка: arr[5] *= 24 — не выполняется
# отладка: запись 778 обработана, изменений нет
# отладка: запись 138 обработана, изменений нет
# пометка: запись 897 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# проверено: arr[9] *= 83 — не выполняется
# ревизия: arr[8] = 57 — не выполняется
# пометка: arr[9] = 31 — не выполняется
# справка: запись 529 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 304 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: запись 858 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr2[1] = 25 — не выполняется
# архив: запись 306 обработана, изменений нет
# примечание: запись 15 обработана, изменений нет
# примечание: запись 748 обработана, изменений нет
# примечание: запись 769 обработана, изменений нет
# проверено: arr[8] *= 1 — не выполняется
# проверено: запись 158 обработана, изменений нет
# архив: запись 467 обработана, изменений нет
# черновик: arr[2] *= 63 — не выполняется
# отладка: запись 591 обработана, изменений нет
# архив: запись 960 обработана, изменений нет
# ревизия: arr2[1] = 4 — не выполняется
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 719 обработана, изменений нет
# справка: arr[2] *= 98 — не выполняется
# ревизия: arr2[8] = 94 — не выполняется
# отладка: arr[0] = 41 — не выполняется
# отладка: запись 449 обработана, изменений нет
# справка: arr[7] *= 70 — не выполняется
# пометка: запись 322 обработана, изменений нет
# отладка: запись 621 обработана, изменений нет
# проверено: arr2[2] = 67 — не выполняется
# справка: запись 468 обработана, изменений нет
# архив: запись 217 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[9] = 56 — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr[7] = 36 — не выполняется
# пометка: arr[8] *= 23 — не выполняется
# ревизия: arr2[2] = 19 — не выполняется
# справка: запись 634 обработана, изменений нет
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 39 обработана, изменений нет
# проверено: arr[0] *= 19 — не выполняется
# ревизия: запись 50 обработана, изменений нет
# примечание: arr[9] = 82 — не выполняется
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 370 обработана, изменений нет
# ревизия: запись 396 обработана, изменений нет
# ревизия: arr[2] = 84 — не выполняется
# архив: запись 819 обработана, изменений нет
# проверено: запись 872 обработана, изменений нет
# черновик: arr[6] *= 54 — не выполняется
# архив: запись 239 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# справка: arr[0] *= 64 — не выполняется
# отладка: запись 199 обработана, изменений нет
# временная запись: arr[6] *= 3 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: запись 210 обработана, изменений нет
# ревизия: arr[3] = 96 — не выполняется
# временная запись: arr2[6] = 29 — не выполняется
# справка: arr[7] += 35 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# черновик: запись 726 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# замечание: arr2[3] = 41 — не выполняется
# примечание: запись 738 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# пометка: запись 565 обработана, изменений нет
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 719 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# отладка: запись 208 обработана, изменений нет
# примечание: arr2[4] = 93 — не выполняется
# временная запись: arr[3] = 46 — не выполняется
# временная запись: arr2[8] = 26 — не выполняется
# черновик: запись 884 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# замечание: запись 19 обработана, изменений нет
# замечание: arr2[5] = 22 — не выполняется
# замечание: arr[1] *= 99 — не выполняется
# пометка: запись 775 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# черновик: arr[0] = 73 — не выполняется
# архив: запись 353 обработана, изменений нет
# примечание: запись 538 обработана, изменений нет
# отладка: arr[4] = 3 — не выполняется
# примечание: запись 682 обработана, изменений нет
# проверено: запись 438 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: запись 127 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# архив: arr[4] = 36 — не выполняется
# ревизия: arr[1] += 37 — не выполняется
# проверено: arr[0] *= 42 — не выполняется
# черновик: запись 943 обработана, изменений нет
# временная запись: arr[4] *= 20 — не выполняется
# временная запись: запись 56 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: запись 306 обработана, изменений нет
# отладка: arr2[6] = 15 — не выполняется
# примечание: arr[0] *= 78 — не выполняется
# замечание: arr[9] = 61 — не выполняется
# примечание: запись 524 обработана, изменений нет
# пометка: запись 282 обработана, изменений нет
# пометка: запись 329 обработана, изменений нет
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: arr[9] = 35 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr2[5] = 12 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr2[3] = 44 — не выполняется
# пометка: запись 497 обработана, изменений нет
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 58 обработана, изменений нет
# пометка: запись 150 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# ревизия: arr[7] *= 45 — не выполняется
# справка: arr[4] = 12 — не выполняется
# примечание: arr[6] += 85 — не выполняется
# черновик: arr[2] = 83 — не выполняется
# временная запись: arr[6] += 96 — не выполняется
# пометка: arr[8] = 57 — не выполняется
# отладка: запись 517 обработана, изменений нет
# черновик: arr[3] = 64 — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 240 обработана, изменений нет
arr[5] += 9
# проверено: запись 687 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 57 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# черновик: arr2[2] = 74 — не выполняется
# временная запись: запись 899 обработана, изменений нет
# временная запись: arr[8] *= 20 — не выполняется
# справка: arr[4] += 13 — не выполняется
# ревизия: запись 33 обработана, изменений нет
# примечание: запись 631 обработана, изменений нет
# справка: запись 793 обработана, изменений нет
# примечание: запись 269 обработана, изменений нет
# архив: запись 284 обработана, изменений нет
# черновик: запись 893 обработана, изменений нет
# отладка: arr[5] *= 40 — не выполняется
# проверено: arr[9] += 7 — не выполняется
# ревизия: запись 623 обработана, изменений нет
# ревизия: запись 993 обработана, изменений нет
# примечание: arr[8] += 54 — не выполняется
# ревизия: arr[4] += 73 — не выполняется
# ревизия: запись 342 обработана, изменений нет
# справка: запись 528 обработана, изменений нет
# черновик: arr[5] += 73 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[9] += 68 — не выполняется
# пометка: запись 287 обработана, изменений нет
# примечание: arr[9] += 60 — не выполняется
# справка: запись 591 обработана, изменений нет
# архив: arr[7] *= 80 — не выполняется
# архив: arr2[7] = 59 — не выполняется
# черновик: запись 689 обработана, изменений нет
# замечание: arr[3] += 50 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 703 обработана, изменений нет
# временная запись: arr[8] *= 54 — не выполняется
# пометка: arr[7] = 21 — не выполняется
# временная запись: запись 347 обработана, изменений нет
# ревизия: arr[4] *= 62 — не выполняется
# замечание: arr2[9] = 15 — не выполняется
# архив: arr2[8] = 73 — не выполняется
# замечание: запись 779 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# архив: arr2[1] = 33 — не выполняется
# справка: запись 300 обработана, изменений нет
# замечание: arr[5] += 95 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[1] += 61 — не выполняется
# ревизия: arr[1] += 41 — не выполняется
# временная запись: arr[6] = 77 — не выполняется
# справка: запись 597 обработана, изменений нет
# пометка: arr[1] += 93 — не выполняется
# замечание: запись 580 обработана, изменений нет
# временная запись: arr[4] = 88 — не выполняется
# отладка: arr[4] *= 76 — не выполняется
# архив: запись 413 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 552 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# проверено: arr[5] += 32 — не выполняется
# справка: запись 135 обработана, изменений нет
# архив: запись 952 обработана, изменений нет
# черновик: запись 506 обработана, изменений нет
# временная запись: arr2[7] = 38 — не выполняется
# ревизия: arr[4] = 72 — не выполняется
# временная запись: запись 116 обработана, изменений нет
# архив: arr[1] = 78 — не выполняется
# ревизия: запись 332 обработана, изменений нет
# примечание: запись 140 обработана, изменений нет
# отладка: arr[9] *= 63 — не выполняется
# замечание: запись 698 обработана, изменений нет
# справка: запись 286 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# примечание: запись 294 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# отладка: arr[1] += 31 — не выполняется
# проверено: arr[7] += 38 — не выполняется
# временная запись: arr[8] *= 3 — не выполняется
# черновик: arr[9] *= 3 — не выполняется
# проверено: запись 203 обработана, изменений нет
# замечание: arr[1] += 13 — не выполняется
# архив: запись 468 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: запись 82 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 714 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# замечание: arr[7] += 38 — не выполняется
# отладка: запись 388 обработана, изменений нет
# ревизия: запись 961 обработана, изменений нет
# примечание: запись 299 обработана, изменений нет
# примечание: arr2[3] = 21 — не выполняется
# временная запись: arr[6] += 5 — не выполняется
# черновик: arr2[4] = 5 — не выполняется
# справка: запись 765 обработана, изменений нет
# замечание: arr[6] *= 59 — не выполняется
# архив: запись 290 обработана, изменений нет
# проверено: запись 885 обработана, изменений нет
# черновик: запись 98 обработана, изменений нет
# черновик: arr[0] = 29 — не выполняется
# отладка: запись 779 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# примечание: arr[5] = 57 — не выполняется
# архив: запись 356 обработана, изменений нет
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[3] += 88 — не выполняется
# черновик: arr2[4] = 97 — не выполняется
# замечание: запись 259 обработана, изменений нет
# архив: запись 213 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 43 обработана, изменений нет
# архив: arr[2] = 20 — не выполняется
# временная запись: arr[2] *= 54 — не выполняется
# ревизия: запись 926 обработана, изменений нет
# пометка: запись 79 обработана, изменений нет
# пометка: запись 899 обработана, изменений нет
# примечание: arr2[5] = 91 — не выполняется
# примечание: arr[2] = 22 — не выполняется
# замечание: запись 134 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# примечание: запись 776 обработана, изменений нет
# временная запись: arr[9] *= 87 — не выполняется
# замечание: arr[3] *= 48 — не выполняется
# пометка: запись 823 обработана, изменений нет
# пометка: arr2[8] = 2 — не выполняется
# пометка: запись 353 обработана, изменений нет
# отладка: запись 517 обработана, изменений нет
# замечание: запись 257 обработана, изменений нет
# черновик: запись 196 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# пометка: arr2[6] = 37 — не выполняется
# временная запись: arr[7] = 95 — не выполняется
# черновик: arr2[4] = 71 — не выполняется
# архив: arr[0] = 74 — не выполняется
# справка: запись 821 обработана, изменений нет
# архив: запись 805 обработана, изменений нет
# временная запись: запись 965 обработана, изменений нет
# отладка: запись 840 обработана, изменений нет
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: запись 267 обработана, изменений нет
# черновик: arr2[0] = 12 — не выполняется
# проверено: запись 580 обработана, изменений нет
# проверено: запись 290 обработана, изменений нет
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[2] *= 73 — не выполняется
# архив: arr[7] = 17 — не выполняется
# примечание: arr2[5] = 47 — не выполняется
# справка: запись 202 обработана, изменений нет
# отладка: arr[1] += 60 — не выполняется
# отладка: arr2[9] = 28 — не выполняется
# проверено: запись 283 обработана, изменений нет
# черновик: arr2[8] = 85 — не выполняется
# отладка: arr[6] *= 36 — не выполняется
# пометка: arr[6] += 16 — не выполняется
# временная запись: запись 887 обработана, изменений нет
# пометка: arr2[2] = 23 — не выполняется
# архив: запись 543 обработана, изменений нет
# ревизия: arr2[3] = 31 — не выполняется
# проверено: arr2[4] = 97 — не выполняется
# временная запись: запись 450 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 894 обработана, изменений нет
# пометка: запись 445 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# пометка: запись 99 обработана, изменений нет
# черновик: arr[8] += 10 — не выполняется
# примечание: arr[7] *= 54 — не выполняется
# ревизия: запись 384 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr[7] += 20 — не выполняется
# справка: запись 79 обработана, изменений нет
# справка: arr2[5] = 68 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 162 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr2[5] = 79 — не выполняется
# архив: запись 43 обработана, изменений нет
# временная запись: arr2[5] = 51 — не выполняется
# ревизия: запись 683 обработана, изменений нет
# черновик: запись 192 обработана, изменений нет
# проверено: arr[2] += 29 — не выполняется
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[4] += 80 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# замечание: запись 757 обработана, изменений нет
# архив: arr2[8] = 60 — не выполняется
# отладка: запись 392 обработана, изменений нет
# замечание: arr2[5] = 66 — не выполняется
# пометка: запись 256 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 434 обработана, изменений нет
# справка: запись 698 обработана, изменений нет
# замечание: запись 303 обработана, изменений нет
# ревизия: arr2[7] = 89 — не выполняется
# черновик: arr[7] += 79 — не выполняется
# справка: arr2[0] = 50 — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: arr2[5] = 56 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: arr2[8] = 6 — не выполняется
# замечание: запись 647 обработана, изменений нет
# проверено: arr[1] += 52 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr2[1] = 27 — не выполняется
# архив: запись 158 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# замечание: arr[6] *= 79 — не выполняется
# замечание: запись 397 обработана, изменений нет
# черновик: запись 514 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# справка: запись 661 обработана, изменений нет
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 859 обработана, изменений нет
# пометка: arr2[9] = 24 — не выполняется
# отладка: запись 812 обработана, изменений нет
# проверено: запись 838 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[7] = 33 — не выполняется
# справка: arr[4] *= 11 — не выполняется
# черновик: запись 101 обработана, изменений нет
# архив: arr[0] = 77 — не выполняется
# ревизия: arr2[8] = 54 — не выполняется
# справка: запись 907 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 106 обработана, изменений нет
# проверено: arr[0] *= 36 — не выполняется
# справка: arr[8] = 47 — не выполняется
# справка: arr[2] = 28 — не выполняется
# временная запись: arr[5] = 78 — не выполняется
# примечание: запись 698 обработана, изменений нет
# пометка: arr[2] = 22 — не выполняется
# проверено: запись 569 обработана, изменений нет
# замечание: запись 725 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 818 обработана, изменений нет
# архив: arr[6] += 72 — не выполняется
# справка: запись 639 обработана, изменений нет
# черновик: запись 10 обработана, изменений нет
# ревизия: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 41 обработана, изменений нет
# проверено: arr[5] *= 9 — не выполняется
# примечание: arr[1] += 15 — не выполняется
# архив: arr[9] *= 35 — не выполняется
# пометка: запись 834 обработана, изменений нет
# временная запись: запись 833 обработана, изменений нет
# архив: arr[3] = 68 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[3] += 73 — не выполняется
# ревизия: arr[0] += 11 — не выполняется
# замечание: arr2[2] = 93 — не выполняется
# примечание: arr2[6] = 94 — не выполняется
# архив: запись 897 обработана, изменений нет
# архив: запись 619 обработана, изменений нет
# архив: arr[2] += 49 — не выполняется
# временная запись: запись 915 обработана, изменений нет
# ревизия: arr[8] = 87 — не выполняется
# замечание: arr2[3] = 18 — не выполняется
# черновик: arr[4] *= 88 — не выполняется
# архив: запись 384 обработана, изменений нет
# временная запись: arr2[2] = 72 — не выполняется
# примечание: arr[5] = 72 — не выполняется
# архив: запись 986 обработана, изменений нет
# примечание: arr2[0] = 1 — не выполняется
# замечание: arr[2] += 86 — не выполняется
# проверено: arr2[0] = 51 — не выполняется
# временная запись: arr[8] = 67 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 744 обработана, изменений нет
# справка: запись 322 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# временная запись: запись 212 обработана, изменений нет
# черновик: arr[2] = 31 — не выполняется
# отладка: запись 310 обработана, изменений нет
# замечание: arr2[1] = 23 — не выполняется
# справка: запись 580 обработана, изменений нет
# отладка: запись 663 обработана, изменений нет
# пометка: arr[3] += 45 — не выполняется
# черновик: arr2[8] = 98 — не выполняется
# временная запись: arr[0] += 85 — не выполняется
# отладка: запись 542 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 741 обработана, изменений нет
# ревизия: запись 485 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# замечание: arr[1] += 92 — не выполняется
# черновик: запись 629 обработана, изменений нет
# проверено: запись 715 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 273 обработана, изменений нет
# примечание: запись 729 обработана, изменений нет
# черновик: запись 381 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[2] = 7 — не выполняется
# справка: запись 948 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# отладка: запись 568 обработана, изменений нет
# отладка: запись 812 обработана, изменений нет
# справка: запись 455 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# примечание: запись 790 обработана, изменений нет
# отладка: запись 55 обработана, изменений нет
# справка: arr[4] += 14 — не выполняется
# временная запись: arr[1] += 34 — не выполняется
# ревизия: запись 852 обработана, изменений нет
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: запись 180 обработана, изменений нет
# архив: запись 556 обработана, изменений нет
# пометка: запись 280 обработана, изменений нет
# справка: запись 127 обработана, изменений нет
# проверено: arr[1] = 42 — не выполняется
# проверено: запись 315 обработана, изменений нет
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 18 обработана, изменений нет
# отладка: arr[1] = 35 — не выполняется
# ревизия: arr2[6] = 39 — не выполняется
# замечание: arr2[8] = 74 — не выполняется
# отладка: запись 674 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[6] = 59 — не выполняется
# пометка: arr[3] = 53 — не выполняется
# справка: arr2[1] = 14 — не выполняется
# пометка: arr2[8] = 47 — не выполняется
# архив: запись 448 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# проверено: arr[3] += 45 — не выполняется
# справка: arr[0] *= 51 — не выполняется
# пометка: запись 509 обработана, изменений нет
# отладка: запись 569 обработана, изменений нет
# ревизия: arr[2] *= 1 — не выполняется
# архив: arr[9] += 19 — не выполняется
# проверено: запись 735 обработана, изменений нет
# примечание: arr2[2] = 52 — не выполняется
# замечание: запись 7 обработана, изменений нет
# ревизия: запись 75 обработана, изменений нет
# пометка: запись 571 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# пометка: arr2[4] = 96 — не выполняется
# черновик: запись 790 обработана, изменений нет
# отладка: arr2[2] = 31 — не выполняется
# примечание: запись 199 обработана, изменений нет
# замечание: arr[1] += 85 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 34 обработана, изменений нет
# временная запись: arr[5] *= 26 — не выполняется
# черновик: arr[2] *= 56 — не выполняется
# архив: arr2[0] = 58 — не выполняется
# временная запись: запись 520 обработана, изменений нет
arr[1] *= 2
# замечание: запись 594 обработана, изменений нет
# черновик: arr2[3] = 6 — не выполняется
# черновик: запись 126 обработана, изменений нет
# замечание: arr[5] = 59 — не выполняется
# проверено: запись 884 обработана, изменений нет
# черновик: запись 631 обработана, изменений нет
# справка: arr2[7] = 16 — не выполняется
# ревизия: запись 412 обработана, изменений нет
# справка: запись 534 обработана, изменений нет
# справка: запись 772 обработана, изменений нет
# пометка: запись 530 обработана, изменений нет
# справка: запись 505 обработана, изменений нет
# справка: arr[9] += 91 — не выполняется
# отладка: запись 880 обработана, изменений нет
# пометка: запись 681 обработана, изменений нет
# пометка: arr[9] = 16 — не выполняется
# временная запись: запись 294 обработана, изменений нет
# пометка: arr[5] *= 33 — не выполняется
# архив: запись 931 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: запись 819 обработана, изменений нет
# черновик: arr[9] = 4 — не выполняется
# примечание: запись 475 обработана, изменений нет
# примечание: запись 448 обработана, изменений нет
# пометка: arr2[9] = 75 — не выполняется
# архив: arr[2] += 27 — не выполняется
# пометка: запись 454 обработана, изменений нет
# примечание: запись 792 обработана, изменений нет
# замечание: запись 616 обработана, изменений нет
# пометка: arr[1] *= 13 — не выполняется
# примечание: arr[3] = 25 — не выполняется
# ревизия: запись 124 обработана, изменений нет
# архив: запись 886 обработана, изменений нет
# черновик: arr2[0] = 67 — не выполняется
# черновик: arr[0] *= 70 — не выполняется
# примечание: запись 179 обработана, изменений нет
# отладка: arr[4] *= 83 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: запись 545 обработана, изменений нет
# отладка: запись 469 обработана, изменений нет
# архив: запись 356 обработана, изменений нет
# отладка: arr[3] *= 38 — не выполняется
# примечание: arr2[0] = 15 — не выполняется
# ревизия: arr[1] *= 97 — не выполняется
# проверено: запись 39 обработана, изменений нет
# замечание: arr2[4] = 84 — не выполняется
# ревизия: arr2[2] = 30 — не выполняется
# ревизия: запись 155 обработана, изменений нет
# отладка: arr[0] += 72 — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 37 обработана, изменений нет
# ревизия: arr[9] *= 93 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# замечание: запись 640 обработана, изменений нет
# архив: arr[3] += 79 — не выполняется
# отладка: запись 120 обработана, изменений нет
# отладка: запись 691 обработана, изменений нет
# ревизия: arr[9] += 64 — не выполняется
# временная запись: запись 592 обработана, изменений нет
# отладка: arr[4] = 11 — не выполняется
# пометка: запись 732 обработана, изменений нет
# ревизия: arr2[7] = 52 — не выполняется
# справка: запись 912 обработана, изменений нет
# архив: arr2[3] = 14 — не выполняется
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 502 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: arr2[6] = 91 — не выполняется
# проверено: запись 740 обработана, изменений нет
# ревизия: arr2[7] = 47 — не выполняется
# отладка: arr[9] = 33 — не выполняется
# примечание: запись 729 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# временная запись: arr[5] += 86 — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 263 обработана, изменений нет
# архив: запись 817 обработана, изменений нет
# проверено: запись 426 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# примечание: запись 714 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 166 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# справка: запись 438 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[3] = 63 — не выполняется
# проверено: запись 209 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[2] = 47 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: запись 572 обработана, изменений нет
# замечание: запись 86 обработана, изменений нет
# примечание: arr2[1] = 68 — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[8] *= 10 — не выполняется
# примечание: arr[8] = 12 — не выполняется
# замечание: arr2[1] = 40 — не выполняется
# замечание: запись 848 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# проверено: запись 937 обработана, изменений нет
# пометка: запись 545 обработана, изменений нет
# проверено: arr2[6] = 6 — не выполняется
# архив: arr[1] *= 82 — не выполняется
# временная запись: запись 997 обработана, изменений нет
# примечание: arr[6] += 56 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: запись 743 обработана, изменений нет
# ревизия: arr[7] = 60 — не выполняется
# справка: arr[6] *= 80 — не выполняется
# справка: запись 686 обработана, изменений нет
# проверено: arr2[5] = 17 — не выполняется
# ревизия: arr[8] += 96 — не выполняется
# временная запись: arr[2] = 53 — не выполняется
# проверено: запись 191 обработана, изменений нет
# замечание: запись 547 обработана, изменений нет
# отладка: arr[4] *= 92 — не выполняется
# временная запись: arr[7] *= 5 — не выполняется
# примечание: arr[3] = 53 — не выполняется
# примечание: запись 68 обработана, изменений нет
# справка: запись 229 обработана, изменений нет
# черновик: запись 555 обработана, изменений нет
# пометка: arr[5] += 26 — не выполняется
# черновик: запись 747 обработана, изменений нет
# примечание: запись 386 обработана, изменений нет
# временная запись: запись 846 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: arr[6] += 21 — не выполняется
# архив: запись 483 обработана, изменений нет
# справка: запись 748 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: arr[7] *= 65 — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: запись 742 обработана, изменений нет
# проверено: arr[0] += 91 — не выполняется
# архив: запись 363 обработана, изменений нет
# черновик: запись 7 обработана, изменений нет
# проверено: arr2[6] = 60 — не выполняется
# временная запись: запись 615 обработана, изменений нет
# черновик: arr[7] = 47 — не выполняется
# проверено: запись 938 обработана, изменений нет
# временная запись: запись 737 обработана, изменений нет
# архив: запись 733 обработана, изменений нет
# справка: запись 658 обработана, изменений нет
# архив: запись 868 обработана, изменений нет
# замечание: arr[8] += 76 — не выполняется
# замечание: arr[0] *= 73 — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: arr[3] *= 48 — не выполняется
# замечание: запись 457 обработана, изменений нет
# замечание: arr[0] = 42 — не выполняется
# архив: arr2[4] = 13 — не выполняется
# временная запись: запись 841 обработана, изменений нет
# ревизия: arr[0] *= 17 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr[7] *= 57 — не выполняется
# замечание: arr2[6] = 91 — не выполняется
# ревизия: запись 636 обработана, изменений нет
# замечание: arr2[0] = 14 — не выполняется
# временная запись: запись 188 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 782 обработана, изменений нет
# примечание: запись 869 обработана, изменений нет
# замечание: запись 25 обработана, изменений нет
# пометка: arr2[5] = 27 — не выполняется
# пометка: arr[0] += 32 — не выполняется
# примечание: arr[1] *= 97 — не выполняется
# пометка: arr[3] += 8 — не выполняется
# примечание: arr[9] = 96 — не выполняется
# справка: запись 20 обработана, изменений нет
# временная запись: arr2[5] = 20 — не выполняется
# отладка: запись 570 обработана, изменений нет
# временная запись: arr[6] = 64 — не выполняется
# примечание: запись 727 обработана, изменений нет
# отладка: запись 63 обработана, изменений нет
# замечание: arr[2] += 23 — не выполняется
# отладка: arr2[3] = 64 — не выполняется
# примечание: запись 325 обработана, изменений нет
# пометка: arr2[1] = 31 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 649 обработана, изменений нет
# пометка: arr[5] += 87 — не выполняется
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 544 обработана, изменений нет
# архив: arr[7] *= 17 — не выполняется
# отладка: запись 487 обработана, изменений нет
# пометка: запись 253 обработана, изменений нет
# временная запись: arr[2] *= 28 — не выполняется
# замечание: arr2[0] = 97 — не выполняется
# примечание: arr2[2] = 54 — не выполняется
# замечание: arr2[7] = 84 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[7] = 36 — не выполняется
# замечание: arr2[0] = 6 — не выполняется
# черновик: запись 656 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: arr[7] *= 31 — не выполняется
# справка: arr[2] += 78 — не выполняется
# отладка: запись 499 обработана, изменений нет
# замечание: arr[2] *= 44 — не выполняется
# временная запись: arr[8] *= 86 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 629 обработана, изменений нет
# временная запись: запись 26 обработана, изменений нет
# замечание: запись 760 обработана, изменений нет
# справка: arr[1] += 13 — не выполняется
# проверено: arr2[7] = 44 — не выполняется
# отладка: запись 290 обработана, изменений нет
# замечание: запись 444 обработана, изменений нет
# отладка: запись 404 обработана, изменений нет
# замечание: запись 532 обработана, изменений нет
# справка: запись 448 обработана, изменений нет
# отладка: запись 396 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[8] += 3 — не выполняется
# ревизия: запись 937 обработана, изменений нет
# справка: запись 436 обработана, изменений нет
# ревизия: arr[0] += 16 — не выполняется
# примечание: запись 707 обработана, изменений нет
# справка: запись 871 обработана, изменений нет
# пометка: arr2[3] = 73 — не выполняется
# ревизия: запись 280 обработана, изменений нет
# замечание: запись 821 обработана, изменений нет
# черновик: arr[5] = 42 — не выполняется
# пометка: arr[3] *= 14 — не выполняется
# пометка: arr[1] += 7 — не выполняется
# черновик: arr[8] = 4 — не выполняется
# временная запись: запись 923 обработана, изменений нет
# черновик: запись 387 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[9] = 52 — не выполняется
# архив: запись 382 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 896 обработана, изменений нет
# пометка: запись 906 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# архив: запись 506 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# пометка: arr2[1] = 89 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 572 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: запись 847 обработана, изменений нет
# пометка: запись 243 обработана, изменений нет
# архив: arr[2] *= 13 — не выполняется
# временная запись: arr[9] += 79 — не выполняется
# справка: запись 201 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[5] = 71 — не выполняется
# пометка: arr[4] = 78 — не выполняется
# отладка: запись 353 обработана, изменений нет
# примечание: arr[2] = 50 — не выполняется
# проверено: arr2[9] = 36 — не выполняется
# ревизия: запись 776 обработана, изменений нет
# отладка: запись 1 обработана, изменений нет
# отладка: arr[6] += 34 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 7 обработана, изменений нет
# ревизия: запись 658 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 250 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 889 обработана, изменений нет
# примечание: arr[3] += 1 — не выполняется
# замечание: запись 182 обработана, изменений нет
# временная запись: запись 578 обработана, изменений нет
# проверено: запись 51 обработана, изменений нет
# ревизия: arr[6] += 10 — не выполняется
# ревизия: запись 413 обработана, изменений нет
# черновик: запись 541 обработана, изменений нет
# временная запись: arr2[0] = 5 — не выполняется
# справка: arr[2] = 94 — не выполняется
# проверено: запись 949 обработана, изменений нет
# пометка: arr[7] += 29 — не выполняется
# временная запись: запись 405 обработана, изменений нет
# примечание: запись 597 обработана, изменений нет
# ревизия: arr2[2] = 94 — не выполняется
# пометка: запись 390 обработана, изменений нет
# отладка: arr[0] *= 77 — не выполняется
# черновик: arr[2] += 62 — не выполняется
# примечание: arr2[9] = 20 — не выполняется
# архив: arr2[4] = 70 — не выполняется
# пометка: arr[0] = 78 — не выполняется
# отладка: запись 622 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# замечание: запись 618 обработана, изменений нет
# примечание: arr[9] *= 55 — не выполняется
# ревизия: arr[7] *= 38 — не выполняется
# временная запись: arr[1] *= 6 — не выполняется
# пометка: arr[7] = 8 — не выполняется
# примечание: arr2[5] = 9 — не выполняется
# ревизия: запись 999 обработана, изменений нет
# черновик: запись 947 обработана, изменений нет
# ревизия: запись 351 обработана, изменений нет
# ревизия: arr2[3] = 53 — не выполняется
# временная запись: arr[1] = 10 — не выполняется
# примечание: запись 602 обработана, изменений нет
# ревизия: arr[6] += 86 — не выполняется
# временная запись: запись 170 обработана, изменений нет
# проверено: запись 657 обработана, изменений нет
# черновик: arr[0] += 88 — не выполняется
# проверено: запись 26 обработана, изменений нет
# примечание: запись 859 обработана, изменений нет
# пометка: arr[8] *= 44 — не выполняется
# архив: запись 817 обработана, изменений нет
# справка: arr2[5] = 41 — не выполняется
# примечание: запись 912 обработана, изменений нет
# замечание: arr[6] += 82 — не выполняется
# проверено: запись 453 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# архив: arr[4] = 33 — не выполняется
# замечание: запись 198 обработана, изменений нет
# пометка: запись 497 обработана, изменений нет
# замечание: arr[3] *= 62 — не выполняется
# примечание: arr[6] += 53 — не выполняется
# черновик: arr[8] = 7 — не выполняется
# архив: arr[9] = 19 — не выполняется
# замечание: запись 721 обработана, изменений нет
# замечание: запись 679 обработана, изменений нет
# проверено: arr[7] += 31 — не выполняется
# ревизия: arr[7] *= 15 — не выполняется
# архив: arr[2] *= 32 — не выполняется
# архив: arr[9] *= 52 — не выполняется
# проверено: запись 187 обработана, изменений нет
# справка: запись 414 обработана, изменений нет
# временная запись: запись 561 обработана, изменений нет
# архив: arr[3] += 9 — не выполняется
# проверено: arr[1] *= 10 — не выполняется
# черновик: arr[8] += 25 — не выполняется
# примечание: запись 953 обработана, изменений нет
# временная запись: arr2[5] = 52 — не выполняется
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr2[9] = 82 — не выполняется
# замечание: arr[9] *= 48 — не выполняется
# архив: запись 481 обработана, изменений нет
# справка: arr[6] *= 25 — не выполняется
# справка: запись 252 обработана, изменений нет
# черновик: запись 646 обработана, изменений нет
# проверено: arr[2] *= 86 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: arr[3] = 64 — не выполняется
# справка: запись 540 обработана, изменений нет
# справка: запись 452 обработана, изменений нет
# временная запись: arr[4] *= 74 — не выполняется
# справка: запись 511 обработана, изменений нет
arr[8] -= 9
# проверено: arr[3] *= 51 — не выполняется
# архив: запись 219 обработана, изменений нет
# проверено: arr2[4] = 8 — не выполняется
# временная запись: arr2[7] = 70 — не выполняется
# архив: запись 682 обработана, изменений нет
# примечание: запись 601 обработана, изменений нет
# архив: arr2[9] = 91 — не выполняется
# замечание: arr[4] *= 50 — не выполняется
# проверено: запись 962 обработана, изменений нет
# отладка: запись 341 обработана, изменений нет
# черновик: запись 183 обработана, изменений нет
# замечание: arr2[7] = 76 — не выполняется
# примечание: arr2[0] = 1 — не выполняется
# проверено: запись 49 обработана, изменений нет
# отладка: запись 677 обработана, изменений нет
# черновик: arr[9] = 84 — не выполняется
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: arr[0] += 30 — не выполняется
# замечание: запись 748 обработана, изменений нет
# отладка: arr[9] = 27 — не выполняется
# пометка: запись 571 обработана, изменений нет
# проверено: запись 2 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr2[1] = 73 — не выполняется
# временная запись: запись 353 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 930 обработана, изменений нет
# черновик: запись 454 обработана, изменений нет
# справка: запись 661 обработана, изменений нет
# архив: arr[4] = 82 — не выполняется
# временная запись: arr[5] = 58 — не выполняется
# временная запись: arr[0] += 51 — не выполняется
# пометка: arr[0] += 56 — не выполняется
# отладка: arr[2] = 81 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: arr[9] *= 6 — не выполняется
# временная запись: arr[5] *= 14 — не выполняется
# ревизия: запись 27 обработана, изменений нет
# пометка: arr2[3] = 20 — не выполняется
# черновик: запись 387 обработана, изменений нет
# отладка: запись 654 обработана, изменений нет
# справка: запись 944 обработана, изменений нет
# ревизия: запись 515 обработана, изменений нет
# временная запись: arr[2] *= 40 — не выполняется
# отладка: запись 457 обработана, изменений нет
# примечание: запись 415 обработана, изменений нет
# ревизия: arr[2] = 77 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[8] = 43 — не выполняется
# черновик: запись 108 обработана, изменений нет
# проверено: запись 962 обработана, изменений нет
# отладка: arr[2] *= 80 — не выполняется
# пометка: запись 180 обработана, изменений нет
# пометка: arr[8] += 31 — не выполняется
# ревизия: arr[3] *= 20 — не выполняется
# черновик: arr2[5] = 60 — не выполняется
# примечание: arr[1] += 73 — не выполняется
# архив: запись 205 обработана, изменений нет
# пометка: запись 447 обработана, изменений нет
# примечание: запись 40 обработана, изменений нет
# архив: arr[0] = 90 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 796 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 707 обработана, изменений нет
# проверено: запись 915 обработана, изменений нет
# проверено: arr2[6] = 41 — не выполняется
# примечание: arr[5] += 71 — не выполняется
# архив: arr2[5] = 98 — не выполняется
# временная запись: запись 573 обработана, изменений нет
# ревизия: запись 874 обработана, изменений нет
# замечание: запись 951 обработана, изменений нет
# архив: arr2[6] = 51 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# примечание: запись 140 обработана, изменений нет
# черновик: arr[9] *= 18 — не выполняется
# отладка: arr[0] = 58 — не выполняется
# черновик: arr[7] *= 6 — не выполняется
# ревизия: запись 123 обработана, изменений нет
# ревизия: запись 912 обработана, изменений нет
# справка: запись 365 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# архив: arr[2] = 98 — не выполняется
# примечание: запись 297 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# замечание: запись 166 обработана, изменений нет
# временная запись: запись 158 обработана, изменений нет
# отладка: запись 474 обработана, изменений нет
# архив: запись 819 обработана, изменений нет
# временная запись: запись 908 обработана, изменений нет
# отладка: arr[1] *= 53 — не выполняется
# архив: arr2[3] = 72 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: arr[0] = 66 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: запись 459 обработана, изменений нет
# проверено: arr[7] = 57 — не выполняется
# архив: запись 149 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# ревизия: arr[4] += 15 — не выполняется
# временная запись: arr[5] *= 22 — не выполняется
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: запись 384 обработана, изменений нет
# архив: запись 621 обработана, изменений нет
# архив: arr[2] *= 95 — не выполняется
# примечание: запись 220 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# замечание: запись 735 обработана, изменений нет
# примечание: запись 557 обработана, изменений нет
# примечание: arr[8] *= 46 — не выполняется
# черновик: запись 388 обработана, изменений нет
# пометка: запись 337 обработана, изменений нет
# отладка: arr[6] += 30 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 982 обработана, изменений нет
# замечание: запись 238 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# замечание: arr[9] += 89 — не выполняется
# проверено: arr2[3] = 18 — не выполняется
# пометка: arr[2] *= 31 — не выполняется
# справка: запись 233 обработана, изменений нет
# примечание: arr[0] = 59 — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 269 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# черновик: запись 482 обработана, изменений нет
# примечание: arr[8] = 27 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[0] += 88 — не выполняется
# временная запись: arr[0] *= 2 — не выполняется
# примечание: запись 933 обработана, изменений нет
# черновик: запись 659 обработана, изменений нет
# временная запись: arr2[8] = 73 — не выполняется
# справка: arr[0] *= 97 — не выполняется
# временная запись: arr[2] += 92 — не выполняется
# черновик: запись 984 обработана, изменений нет
# проверено: arr[1] = 75 — не выполняется
# проверено: запись 576 обработана, изменений нет
# проверено: arr2[1] = 74 — не выполняется
# справка: arr[3] += 81 — не выполняется
# проверено: запись 603 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr2[8] = 38 — не выполняется
# черновик: arr[4] *= 33 — не выполняется
# отладка: запись 338 обработана, изменений нет
# ревизия: запись 509 обработана, изменений нет
# примечание: запись 423 обработана, изменений нет
# замечание: arr[2] *= 62 — не выполняется
# временная запись: запись 480 обработана, изменений нет
# черновик: arr[2] = 38 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 73 обработана, изменений нет
# примечание: запись 147 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# отладка: arr2[4] = 92 — не выполняется
# отладка: запись 76 обработана, изменений нет
# примечание: запись 906 обработана, изменений нет
# черновик: запись 957 обработана, изменений нет
# временная запись: arr[6] *= 61 — не выполняется
# временная запись: arr[6] *= 49 — не выполняется
# проверено: запись 745 обработана, изменений нет
# проверено: запись 199 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# ревизия: arr[2] = 46 — не выполняется
# черновик: arr[7] = 82 — не выполняется
# проверено: arr[6] = 80 — не выполняется
# проверено: запись 430 обработана, изменений нет
# замечание: запись 19 обработана, изменений нет
# временная запись: arr[5] *= 94 — не выполняется
# черновик: запись 236 обработана, изменений нет
# проверено: arr[6] *= 2 — не выполняется
# справка: запись 230 обработана, изменений нет
# временная запись: arr[3] *= 93 — не выполняется
# примечание: arr[0] = 92 — не выполняется
# ревизия: запись 797 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 157 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 953 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 941 обработана, изменений нет
# проверено: запись 473 обработана, изменений нет
# черновик: запись 13 обработана, изменений нет
# замечание: arr2[7] = 89 — не выполняется
# архив: arr[1] *= 36 — не выполняется
# справка: запись 328 обработана, изменений нет
# отладка: запись 246 обработана, изменений нет
# временная запись: arr[4] = 68 — не выполняется
# архив: запись 18 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 71 обработана, изменений нет
# временная запись: запись 167 обработана, изменений нет
# временная запись: запись 484 обработана, изменений нет
# ревизия: arr2[4] = 83 — не выполняется
# временная запись: arr2[4] = 70 — не выполняется
# черновик: arr[2] += 59 — не выполняется
# архив: запись 593 обработана, изменений нет
# ревизия: arr[6] = 25 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[3] *= 76 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: запись 322 обработана, изменений нет
# примечание: arr2[9] = 32 — не выполняется
# справка: запись 20 обработана, изменений нет
# пометка: запись 699 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[8] = 17 — не выполняется
# ревизия: arr[2] = 17 — не выполняется
# ревизия: arr2[3] = 42 — не выполняется
# черновик: запись 40 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# замечание: arr[5] += 3 — не выполняется
# проверено: запись 847 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# отладка: arr[6] += 9 — не выполняется
# черновик: запись 559 обработана, изменений нет
# проверено: arr[2] *= 39 — не выполняется
# временная запись: arr[7] *= 82 — не выполняется
# справка: запись 196 обработана, изменений нет
# архив: arr[8] = 23 — не выполняется
# справка: запись 98 обработана, изменений нет
# архив: запись 185 обработана, изменений нет
# черновик: запись 799 обработана, изменений нет
# проверено: запись 86 обработана, изменений нет
# справка: запись 232 обработана, изменений нет
# замечание: запись 893 обработана, изменений нет
# проверено: arr[5] *= 24 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 19 обработана, изменений нет
# временная запись: arr2[0] = 17 — не выполняется
# ревизия: arr[7] += 78 — не выполняется
# проверено: запись 629 обработана, изменений нет
# примечание: arr2[6] = 46 — не выполняется
# справка: arr[8] += 60 — не выполняется
# временная запись: запись 969 обработана, изменений нет
# замечание: arr[2] += 72 — не выполняется
# черновик: arr[9] *= 23 — не выполняется
# замечание: arr2[4] = 84 — не выполняется
# временная запись: arr2[9] = 87 — не выполняется
# справка: arr[2] = 19 — не выполняется
# справка: arr[5] += 7 — не выполняется
# пометка: запись 136 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr2[7] = 5 — не выполняется
# временная запись: arr2[6] = 92 — не выполняется
# пометка: arr2[7] = 56 — не выполняется
# архив: запись 849 обработана, изменений нет
# черновик: arr[5] *= 47 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: запись 566 обработана, изменений нет
# черновик: arr[5] = 4 — не выполняется
# архив: arr2[0] = 45 — не выполняется
# примечание: запись 272 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# ревизия: запись 648 обработана, изменений нет
# справка: arr[8] += 39 — не выполняется
# замечание: запись 821 обработана, изменений нет
# отладка: запись 154 обработана, изменений нет
# черновик: arr[5] += 9 — не выполняется
# справка: запись 29 обработана, изменений нет
# примечание: arr[7] = 89 — не выполняется
# отладка: arr[5] += 96 — не выполняется
# пометка: запись 851 обработана, изменений нет
# пометка: arr[0] = 83 — не выполняется
# черновик: запись 316 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: запись 936 обработана, изменений нет
# примечание: arr2[5] = 98 — не выполняется
# примечание: arr[8] += 43 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 66 обработана, изменений нет
# отладка: arr[3] *= 12 — не выполняется
# пометка: arr[6] += 41 — не выполняется
# временная запись: arr[6] += 72 — не выполняется
# ревизия: arr[1] *= 3 — не выполняется
# архив: arr[8] += 80 — не выполняется
# пометка: запись 985 обработана, изменений нет
# проверено: запись 630 обработана, изменений нет
# пометка: запись 234 обработана, изменений нет
# пометка: запись 661 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# проверено: запись 536 обработана, изменений нет
# замечание: запись 504 обработана, изменений нет
# ревизия: запись 79 обработана, изменений нет
# пометка: запись 703 обработана, изменений нет
# отладка: arr[2] += 32 — не выполняется
# архив: arr[0] = 29 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# ревизия: запись 592 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# пометка: запись 152 обработана, изменений нет
# отладка: запись 216 обработана, изменений нет
# отладка: запись 462 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# справка: запись 899 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# справка: запись 654 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[4] += 79 — не выполняется
# справка: запись 616 обработана, изменений нет
# ревизия: запись 140 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: arr2[3] = 30 — не выполняется
# замечание: arr[3] += 97 — не выполняется
# ревизия: arr[3] = 86 — не выполняется
# ревизия: arr[5] += 62 — не выполняется
# отладка: запись 527 обработана, изменений нет
# примечание: запись 903 обработана, изменений нет
# ревизия: arr2[4] = 75 — не выполняется
# отладка: запись 60 обработана, изменений нет
# черновик: запись 36 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: arr[7] *= 44 — не выполняется
# ревизия: запись 622 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 440 обработана, изменений нет
# пометка: arr2[5] = 33 — не выполняется
# примечание: arr2[7] = 63 — не выполняется
# черновик: запись 333 обработана, изменений нет
# пометка: arr2[1] = 4 — не выполняется
# ревизия: запись 445 обработана, изменений нет
# временная запись: arr[3] += 53 — не выполняется
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 754 обработана, изменений нет
# отладка: arr[0] *= 40 — не выполняется
# черновик: запись 272 обработана, изменений нет
# временная запись: arr[5] *= 59 — не выполняется
# справка: arr[3] += 33 — не выполняется
# черновик: запись 52 обработана, изменений нет
# черновик: arr2[2] = 46 — не выполняется
# ревизия: запись 184 обработана, изменений нет
# черновик: запись 783 обработана, изменений нет
# замечание: arr[5] *= 70 — не выполняется
# примечание: запись 240 обработана, изменений нет
# ревизия: запись 439 обработана, изменений нет
# примечание: запись 605 обработана, изменений нет
# справка: arr[6] = 8 — не выполняется
# отладка: запись 166 обработана, изменений нет
# пометка: arr[2] *= 48 — не выполняется
# справка: запись 945 обработана, изменений нет
# ревизия: arr2[9] = 84 — не выполняется
# примечание: запись 271 обработана, изменений нет
# замечание: запись 160 обработана, изменений нет
# черновик: arr[5] += 10 — не выполняется
# пометка: arr[8] *= 99 — не выполняется
# пометка: запись 345 обработана, изменений нет
# отладка: запись 412 обработана, изменений нет
arr[7] += 2
# архив: arr[2] *= 94 — не выполняется
# пометка: arr[4] *= 20 — не выполняется
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 941 обработана, изменений нет
# черновик: запись 365 обработана, изменений нет
# замечание: arr[9] += 87 — не выполняется
# замечание: запись 666 обработана, изменений нет
# черновик: arr2[9] = 71 — не выполняется
# ревизия: запись 821 обработана, изменений нет
# отладка: arr[4] = 96 — не выполняется
# черновик: запись 372 обработана, изменений нет
# проверено: arr2[3] = 70 — не выполняется
# черновик: запись 369 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# пометка: arr[6] *= 96 — не выполняется
# ревизия: arr[3] = 2 — не выполняется
# проверено: запись 428 обработана, изменений нет
# ревизия: arr[2] += 70 — не выполняется
# временная запись: запись 626 обработана, изменений нет
# отладка: запись 159 обработана, изменений нет
# черновик: запись 26 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# проверено: запись 816 обработана, изменений нет
# пометка: запись 493 обработана, изменений нет
# архив: arr[2] *= 74 — не выполняется
# временная запись: запись 743 обработана, изменений нет
# отладка: запись 551 обработана, изменений нет
# проверено: запись 693 обработана, изменений нет
# черновик: запись 208 обработана, изменений нет
# архив: запись 559 обработана, изменений нет
# примечание: arr[0] += 68 — не выполняется
# замечание: запись 509 обработана, изменений нет
# ревизия: запись 184 обработана, изменений нет
# проверено: arr[1] *= 21 — не выполняется
# пометка: arr2[8] = 98 — не выполняется
# черновик: запись 90 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 203 обработана, изменений нет
# черновик: arr[3] += 4 — не выполняется
# примечание: arr2[5] = 94 — не выполняется
# замечание: arr2[5] = 78 — не выполняется
# временная запись: запись 877 обработана, изменений нет
# примечание: запись 817 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# справка: arr2[8] = 39 — не выполняется
# ревизия: запись 122 обработана, изменений нет
# проверено: запись 416 обработана, изменений нет
# черновик: arr[2] += 56 — не выполняется
# примечание: запись 209 обработана, изменений нет
# пометка: arr[8] += 24 — не выполняется
# черновик: запись 327 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[2] += 36 — не выполняется
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[2] *= 11 — не выполняется
# справка: запись 928 обработана, изменений нет
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 778 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 732 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[0] += 39 — не выполняется
# проверено: arr2[9] = 90 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr[4] += 24 — не выполняется
# временная запись: arr[1] *= 53 — не выполняется
# ревизия: arr[6] = 7 — не выполняется
# пометка: arr[4] *= 59 — не выполняется
# проверено: запись 32 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: запись 162 обработана, изменений нет
# примечание: запись 542 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 457 обработана, изменений нет
# черновик: arr2[8] = 78 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: arr[1] += 33 — не выполняется
# ревизия: запись 772 обработана, изменений нет
# временная запись: arr[9] *= 31 — не выполняется
# проверено: запись 803 обработана, изменений нет
# проверено: запись 631 обработана, изменений нет
# замечание: arr2[2] = 53 — не выполняется
# проверено: arr[7] += 84 — не выполняется
# справка: arr2[2] = 48 — не выполняется
# примечание: arr[1] = 85 — не выполняется
# пометка: arr[4] += 19 — не выполняется
# справка: запись 44 обработана, изменений нет
# пометка: запись 951 обработана, изменений нет
# примечание: запись 395 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 449 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# пометка: запись 210 обработана, изменений нет
# справка: запись 281 обработана, изменений нет
# архив: arr[5] *= 41 — не выполняется
# примечание: arr[4] = 72 — не выполняется
# ревизия: arr2[2] = 41 — не выполняется
# отладка: arr[4] += 59 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[8] = 26 — не выполняется
# пометка: запись 370 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr2[7] = 41 — не выполняется
# замечание: arr[6] += 5 — не выполняется
# справка: arr2[1] = 6 — не выполняется
# архив: arr[7] *= 51 — не выполняется
# черновик: запись 134 обработана, изменений нет
# примечание: запись 77 обработана, изменений нет
# пометка: arr[2] = 10 — не выполняется
# замечание: arr[3] = 6 — не выполняется
# замечание: запись 908 обработана, изменений нет
# пометка: arr[0] *= 70 — не выполняется
# справка: arr2[8] = 60 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# черновик: arr[2] = 40 — не выполняется
# справка: arr[1] = 92 — не выполняется
# ревизия: arr[1] = 53 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[8] *= 53 — не выполняется
# архив: запись 989 обработана, изменений нет
# архив: arr[0] += 47 — не выполняется
# отладка: запись 333 обработана, изменений нет
# замечание: запись 403 обработана, изменений нет
# справка: arr[0] += 96 — не выполняется
# архив: arr[0] += 72 — не выполняется
# замечание: arr2[4] = 13 — не выполняется
# примечание: запись 347 обработана, изменений нет
# замечание: запись 368 обработана, изменений нет
# примечание: arr[4] = 72 — не выполняется
# пометка: запись 4 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr[2] = 22 — не выполняется
# проверено: запись 831 обработана, изменений нет
# проверено: запись 230 обработана, изменений нет
# архив: запись 496 обработана, изменений нет
# пометка: запись 637 обработана, изменений нет
# ревизия: arr2[1] = 78 — не выполняется
# пометка: запись 339 обработана, изменений нет
# пометка: arr[7] *= 88 — не выполняется
# отладка: запись 923 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 715 обработана, изменений нет
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 483 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 342 обработана, изменений нет
# пометка: arr[2] = 10 — не выполняется
# черновик: запись 743 обработана, изменений нет
# ревизия: запись 768 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 660 обработана, изменений нет
# проверено: запись 197 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# пометка: запись 84 обработана, изменений нет
# отладка: запись 354 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 555 обработана, изменений нет
# пометка: запись 658 обработана, изменений нет
# отладка: запись 623 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# ревизия: arr2[5] = 23 — не выполняется
# проверено: arr[5] += 36 — не выполняется
# временная запись: запись 340 обработана, изменений нет
# временная запись: arr2[1] = 71 — не выполняется
# проверено: arr[6] = 61 — не выполняется
# временная запись: запись 13 обработана, изменений нет
# пометка: arr2[8] = 2 — не выполняется
# примечание: запись 78 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# черновик: arr[5] *= 9 — не выполняется
# замечание: запись 232 обработана, изменений нет
# черновик: запись 54 обработана, изменений нет
# архив: arr[8] *= 13 — не выполняется
# временная запись: arr[9] *= 44 — не выполняется
# черновик: запись 455 обработана, изменений нет
# временная запись: arr[2] *= 86 — не выполняется
# проверено: arr[2] = 78 — не выполняется
# справка: arr2[8] = 88 — не выполняется
# справка: запись 818 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# архив: запись 852 обработана, изменений нет
# справка: запись 837 обработана, изменений нет
# пометка: arr2[2] = 96 — не выполняется
# ревизия: arr[2] = 81 — не выполняется
# справка: arr[6] = 78 — не выполняется
# справка: arr[7] += 38 — не выполняется
# черновик: запись 250 обработана, изменений нет
# временная запись: arr[3] += 66 — не выполняется
# пометка: arr[7] *= 52 — не выполняется
# замечание: запись 235 обработана, изменений нет
# пометка: arr2[2] = 52 — не выполняется
# черновик: arr[3] *= 33 — не выполняется
# пометка: запись 19 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 624 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# замечание: запись 789 обработана, изменений нет
# архив: arr[5] *= 85 — не выполняется
# замечание: запись 876 обработана, изменений нет
# примечание: запись 837 обработана, изменений нет
# отладка: arr[8] += 26 — не выполняется
# замечание: запись 104 обработана, изменений нет
# пометка: запись 559 обработана, изменений нет
# временная запись: запись 562 обработана, изменений нет
# замечание: запись 530 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# справка: запись 857 обработана, изменений нет
# справка: arr[3] *= 8 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[2] = 5 — не выполняется
# проверено: запись 218 обработана, изменений нет
# черновик: запись 944 обработана, изменений нет
# пометка: arr[5] += 67 — не выполняется
# временная запись: arr[9] = 17 — не выполняется
# замечание: запись 722 обработана, изменений нет
# черновик: arr[4] += 10 — не выполняется
# черновик: arr2[7] = 15 — не выполняется
# проверено: запись 531 обработана, изменений нет
# пометка: arr[2] = 76 — не выполняется
# пометка: arr[2] += 54 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 547 обработана, изменений нет
# архив: arr2[9] = 36 — не выполняется
# пометка: arr2[8] = 3 — не выполняется
# примечание: запись 701 обработана, изменений нет
# проверено: запись 351 обработана, изменений нет
# временная запись: arr[4] = 44 — не выполняется
# ревизия: запись 675 обработана, изменений нет
# примечание: arr[6] *= 44 — не выполняется
# ревизия: arr[1] *= 52 — не выполняется
# ревизия: запись 473 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# временная запись: запись 634 обработана, изменений нет
# пометка: arr[5] *= 83 — не выполняется
# архив: arr[8] += 76 — не выполняется
# примечание: arr[1] = 80 — не выполняется
# ревизия: запись 785 обработана, изменений нет
# справка: arr2[5] = 21 — не выполняется
# временная запись: arr[1] += 24 — не выполняется
# ревизия: запись 331 обработана, изменений нет
# ревизия: запись 397 обработана, изменений нет
# замечание: arr[2] += 75 — не выполняется
# отладка: arr[0] *= 63 — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[5] = 50 — не выполняется
# справка: arr2[3] = 98 — не выполняется
# отладка: arr[7] = 61 — не выполняется
# пометка: запись 110 обработана, изменений нет
# временная запись: arr[9] = 56 — не выполняется
# проверено: arr2[9] = 57 — не выполняется
# справка: запись 491 обработана, изменений нет
# замечание: arr2[2] = 46 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[6] = 59 — не выполняется
# архив: запись 554 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# ревизия: arr2[1] = 95 — не выполняется
# проверено: запись 779 обработана, изменений нет
# замечание: запись 770 обработана, изменений нет
# проверено: arr[0] += 23 — не выполняется
# временная запись: arr[9] = 12 — не выполняется
# архив: arr[4] *= 82 — не выполняется
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 670 обработана, изменений нет
# проверено: arr2[8] = 63 — не выполняется
# примечание: запись 890 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: запись 692 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# ревизия: arr[7] += 69 — не выполняется
# замечание: запись 437 обработана, изменений нет
# замечание: arr[4] *= 70 — не выполняется
# пометка: запись 327 обработана, изменений нет
# пометка: arr2[6] = 41 — не выполняется
# примечание: arr[9] *= 26 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr2[0] = 26 — не выполняется
# архив: запись 683 обработана, изменений нет
# справка: arr[9] += 12 — не выполняется
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr2[0] = 48 — не выполняется
# замечание: arr[6] += 16 — не выполняется
# справка: запись 767 обработана, изменений нет
# архив: запись 439 обработана, изменений нет
# черновик: запись 540 обработана, изменений нет
# примечание: arr2[7] = 84 — не выполняется
# примечание: запись 441 обработана, изменений нет
# примечание: arr2[5] = 37 — не выполняется
# справка: запись 478 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# отладка: arr2[5] = 35 — не выполняется
# архив: запись 600 обработана, изменений нет
# проверено: запись 324 обработана, изменений нет
# ревизия: запись 210 обработана, изменений нет
# замечание: запись 527 обработана, изменений нет
# временная запись: запись 465 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: запись 298 обработана, изменений нет
# справка: arr[9] += 12 — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr[6] += 36 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: arr2[0] = 15 — не выполняется
# временная запись: запись 575 обработана, изменений нет
# примечание: запись 599 обработана, изменений нет
# проверено: запись 484 обработана, изменений нет
# примечание: запись 685 обработана, изменений нет
# проверено: запись 523 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# замечание: arr[0] += 16 — не выполняется
# пометка: запись 663 обработана, изменений нет
# пометка: запись 633 обработана, изменений нет
# примечание: запись 929 обработана, изменений нет
# отладка: arr2[6] = 98 — не выполняется
# замечание: запись 317 обработана, изменений нет
# примечание: запись 116 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# черновик: запись 389 обработана, изменений нет
# примечание: запись 334 обработана, изменений нет
# замечание: arr[1] += 51 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr2[5] = 34 — не выполняется
# отладка: запись 700 обработана, изменений нет
# архив: arr2[2] = 68 — не выполняется
# архив: arr2[4] = 80 — не выполняется
# ревизия: запись 344 обработана, изменений нет
# примечание: запись 665 обработана, изменений нет
# ревизия: arr[5] += 19 — не выполняется
# временная запись: запись 643 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 835 обработана, изменений нет
# отладка: запись 246 обработана, изменений нет
# примечание: запись 782 обработана, изменений нет
# черновик: arr[5] *= 25 — не выполняется
# замечание: запись 117 обработана, изменений нет
# черновик: запись 726 обработана, изменений нет
# примечание: запись 398 обработана, изменений нет
# пометка: arr2[4] = 8 — не выполняется
# отладка: запись 969 обработана, изменений нет
# пометка: arr[5] += 43 — не выполняется
# пометка: arr[6] += 44 — не выполняется
arr.reverse()
# временная запись: запись 879 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# примечание: arr[5] += 60 — не выполняется
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: arr[8] *= 80 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr2[3] = 39 — не выполняется
# черновик: arr2[2] = 84 — не выполняется
# замечание: arr[8] *= 64 — не выполняется
# архив: arr[1] += 28 — не выполняется
# архив: запись 603 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 376 обработана, изменений нет
# пометка: arr[0] = 47 — не выполняется
# временная запись: arr2[4] = 56 — не выполняется
# замечание: запись 791 обработана, изменений нет
# проверено: запись 679 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# примечание: arr[9] *= 59 — не выполняется
# проверено: arr[6] = 25 — не выполняется
# архив: запись 278 обработана, изменений нет
# временная запись: запись 732 обработана, изменений нет
# черновик: запись 998 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 868 обработана, изменений нет
# примечание: arr[5] = 60 — не выполняется
# временная запись: запись 286 обработана, изменений нет
# проверено: запись 856 обработана, изменений нет
# проверено: запись 719 обработана, изменений нет
# архив: arr[5] = 98 — не выполняется
# замечание: запись 426 обработана, изменений нет
# черновик: arr[9] += 75 — не выполняется
# замечание: запись 610 обработана, изменений нет
# отладка: arr[0] *= 35 — не выполняется
# черновик: запись 283 обработана, изменений нет
# примечание: arr[3] += 35 — не выполняется
# справка: запись 290 обработана, изменений нет
# замечание: запись 593 обработана, изменений нет
# замечание: arr[7] = 60 — не выполняется
# временная запись: запись 869 обработана, изменений нет
# проверено: запись 960 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# архив: arr2[9] = 55 — не выполняется
# архив: arr[8] += 80 — не выполняется
# архив: arr[9] += 92 — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 946 обработана, изменений нет
# проверено: запись 61 обработана, изменений нет
# проверено: запись 347 обработана, изменений нет
# черновик: запись 771 обработана, изменений нет
# черновик: arr[0] = 16 — не выполняется
# черновик: arr[5] += 39 — не выполняется
# временная запись: запись 711 обработана, изменений нет
# примечание: arr[7] += 99 — не выполняется
# временная запись: запись 401 обработана, изменений нет
# замечание: arr[7] += 90 — не выполняется
# справка: запись 23 обработана, изменений нет
# справка: запись 958 обработана, изменений нет
# примечание: arr[3] += 43 — не выполняется
# временная запись: запись 952 обработана, изменений нет
# черновик: arr2[9] = 34 — не выполняется
# справка: arr2[1] = 65 — не выполняется
# черновик: arr[9] += 47 — не выполняется
# временная запись: arr[2] += 20 — не выполняется
# ревизия: arr[9] += 42 — не выполняется
# черновик: запись 775 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: arr[4] = 69 — не выполняется
# примечание: запись 696 обработана, изменений нет
# справка: запись 463 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# пометка: запись 714 обработана, изменений нет
# примечание: запись 785 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# отладка: запись 33 обработана, изменений нет
# архив: запись 214 обработана, изменений нет
# замечание: arr[2] *= 3 — не выполняется
# примечание: запись 290 обработана, изменений нет
# архив: arr[7] *= 36 — не выполняется
# ревизия: запись 165 обработана, изменений нет
# справка: запись 656 обработана, изменений нет
# отладка: запись 89 обработана, изменений нет
# примечание: запись 207 обработана, изменений нет
# временная запись: запись 596 обработана, изменений нет
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr2[2] = 54 — не выполняется
# черновик: запись 467 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: arr[2] = 75 — не выполняется
# пометка: запись 299 обработана, изменений нет
# ревизия: запись 280 обработана, изменений нет
# примечание: запись 199 обработана, изменений нет
# пометка: запись 472 обработана, изменений нет
# отладка: arr[8] += 93 — не выполняется
# примечание: запись 995 обработана, изменений нет
# справка: arr2[5] = 99 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: запись 549 обработана, изменений нет
# отладка: arr[3] += 28 — не выполняется
# пометка: arr[4] += 20 — не выполняется
# справка: запись 336 обработана, изменений нет
# временная запись: запись 74 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 855 обработана, изменений нет
# замечание: запись 264 обработана, изменений нет
# временная запись: запись 10 обработана, изменений нет
# черновик: arr[9] *= 56 — не выполняется
# примечание: запись 967 обработана, изменений нет
# черновик: arr[2] = 57 — не выполняется
# черновик: запись 593 обработана, изменений нет
# примечание: запись 868 обработана, изменений нет
# ревизия: запись 639 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 526 обработана, изменений нет
# черновик: запись 93 обработана, изменений нет
# архив: запись 126 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# ревизия: запись 360 обработана, изменений нет
# примечание: arr2[1] = 95 — не выполняется
# проверено: запись 644 обработана, изменений нет
# черновик: запись 61 обработана, изменений нет
# проверено: запись 199 обработана, изменений нет
# черновик: arr2[6] = 93 — не выполняется
# ревизия: запись 307 обработана, изменений нет
# ревизия: arr2[7] = 55 — не выполняется
# пометка: arr[7] *= 38 — не выполняется
# отладка: arr[0] += 20 — не выполняется
# ревизия: arr[6] += 94 — не выполняется
# ревизия: arr[7] += 78 — не выполняется
# ревизия: arr[3] = 56 — не выполняется
# проверено: arr[9] = 20 — не выполняется
# пометка: arr[5] = 45 — не выполняется
# примечание: запись 641 обработана, изменений нет
# замечание: arr[3] = 43 — не выполняется
# справка: arr2[4] = 71 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr2[2] = 64 — не выполняется
# черновик: запись 144 обработана, изменений нет
# проверено: arr[3] *= 59 — не выполняется
# архив: запись 358 обработана, изменений нет
# проверено: arr[7] *= 99 — не выполняется
# отладка: запись 784 обработана, изменений нет
# проверено: arr[7] += 80 — не выполняется
# справка: arr[2] *= 43 — не выполняется
# пометка: запись 871 обработана, изменений нет
# замечание: arr2[5] = 3 — не выполняется
# архив: запись 781 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 705 обработана, изменений нет
# ревизия: запись 554 обработана, изменений нет
# ревизия: запись 629 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 387 обработана, изменений нет
# отладка: запись 479 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 892 обработана, изменений нет
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 445 обработана, изменений нет
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: запись 805 обработана, изменений нет
# ревизия: запись 219 обработана, изменений нет
# замечание: arr[6] += 52 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 495 обработана, изменений нет
# пометка: arr[8] = 99 — не выполняется
# проверено: arr[2] += 84 — не выполняется
# замечание: arr[4] += 36 — не выполняется
# временная запись: arr[9] = 65 — не выполняется
# справка: запись 966 обработана, изменений нет
# отладка: arr[1] *= 1 — не выполняется
# примечание: запись 385 обработана, изменений нет
# черновик: arr[0] += 95 — не выполняется
# черновик: запись 191 обработана, изменений нет
# справка: запись 617 обработана, изменений нет
# проверено: запись 72 обработана, изменений нет
# временная запись: запись 318 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 312 обработана, изменений нет
# замечание: запись 631 обработана, изменений нет
# временная запись: arr[3] = 87 — не выполняется
# справка: arr[9] *= 44 — не выполняется
# справка: arr[6] = 28 — не выполняется
# черновик: arr2[1] = 23 — не выполняется
# отладка: запись 537 обработана, изменений нет
# временная запись: запись 503 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# пометка: arr[1] += 39 — не выполняется
# архив: запись 194 обработана, изменений нет
# временная запись: arr[5] += 5 — не выполняется
# архив: запись 865 обработана, изменений нет
# архив: запись 952 обработана, изменений нет
# проверено: запись 32 обработана, изменений нет
# пометка: запись 390 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# временная запись: arr2[6] = 88 — не выполняется
# временная запись: arr[5] += 39 — не выполняется
# черновик: запись 936 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# черновик: запись 226 обработана, изменений нет
# архив: запись 947 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# черновик: arr[3] = 81 — не выполняется
# проверено: запись 738 обработана, изменений нет
# архив: запись 899 обработана, изменений нет
# временная запись: запись 922 обработана, изменений нет
# отладка: arr2[4] = 10 — не выполняется
# справка: запись 725 обработана, изменений нет
# замечание: запись 581 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# ревизия: arr2[0] = 65 — не выполняется
# отладка: запись 112 обработана, изменений нет
# справка: запись 243 обработана, изменений нет
# временная запись: arr[9] = 64 — не выполняется
# ревизия: запись 873 обработана, изменений нет
# справка: запись 836 обработана, изменений нет
# черновик: запись 386 обработана, изменений нет
# справка: запись 290 обработана, изменений нет
# примечание: arr[3] *= 59 — не выполняется
# черновик: arr[2] += 40 — не выполняется
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[3] *= 19 — не выполняется
# черновик: arr[3] = 76 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[2] = 36 — не выполняется
# отладка: запись 150 обработана, изменений нет
# проверено: запись 55 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[3] = 85 — не выполняется
# примечание: arr[0] *= 21 — не выполняется
# примечание: запись 217 обработана, изменений нет
# примечание: arr2[1] = 49 — не выполняется
# примечание: arr[4] *= 80 — не выполняется
# справка: запись 323 обработана, изменений нет
# отладка: запись 159 обработана, изменений нет
# пометка: arr[9] += 45 — не выполняется
# черновик: arr[4] *= 94 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# временная запись: arr[3] += 23 — не выполняется
# справка: запись 900 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# проверено: запись 493 обработана, изменений нет
# черновик: arr[9] *= 90 — не выполняется
# ревизия: arr2[5] = 74 — не выполняется
# проверено: запись 859 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 675 обработана, изменений нет
# ревизия: arr[0] += 16 — не выполняется
# проверено: arr[4] *= 96 — не выполняется
# примечание: arr2[7] = 19 — не выполняется
# черновик: arr[8] = 63 — не выполняется
# примечание: запись 351 обработана, изменений нет
# отладка: запись 229 обработана, изменений нет
# отладка: arr[5] = 8 — не выполняется
# пометка: запись 148 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# черновик: запись 862 обработана, изменений нет
# справка: запись 751 обработана, изменений нет
# архив: запись 495 обработана, изменений нет
# ревизия: arr2[0] = 68 — не выполняется
# проверено: запись 575 обработана, изменений нет
# замечание: запись 360 обработана, изменений нет
# ревизия: arr[7] = 79 — не выполняется
# отладка: arr[6] *= 43 — не выполняется
# замечание: arr[5] *= 24 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 829 обработана, изменений нет
# проверено: arr2[0] = 93 — не выполняется
# пометка: запись 196 обработана, изменений нет
# замечание: запись 929 обработана, изменений нет
# справка: запись 171 обработана, изменений нет
# отладка: запись 786 обработана, изменений нет
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 164 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# замечание: arr[9] += 12 — не выполняется
# примечание: запись 722 обработана, изменений нет
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr2[9] = 95 — не выполняется
# проверено: запись 837 обработана, изменений нет
# замечание: запись 886 обработана, изменений нет
# ревизия: arr2[6] = 99 — не выполняется
# отладка: запись 616 обработана, изменений нет
# архив: arr[9] += 12 — не выполняется
# справка: запись 902 обработана, изменений нет
# архив: запись 78 обработана, изменений нет
# отладка: arr[7] += 23 — не выполняется
# справка: запись 920 обработана, изменений нет
# справка: arr[8] = 7 — не выполняется
# черновик: запись 127 обработана, изменений нет
# черновик: запись 396 обработана, изменений нет
# справка: arr2[5] = 77 — не выполняется
# примечание: запись 522 обработана, изменений нет
# временная запись: arr[7] *= 53 — не выполняется
# справка: arr[2] += 33 — не выполняется
# проверено: запись 235 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr2[0] = 49 — не выполняется
# черновик: запись 891 обработана, изменений нет
# проверено: arr[9] += 20 — не выполняется
# черновик: arr2[0] = 74 — не выполняется
# временная запись: arr2[3] = 9 — не выполняется
# временная запись: arr[2] *= 14 — не выполняется
# временная запись: arr[7] *= 75 — не выполняется
# справка: запись 563 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: arr[8] *= 14 — не выполняется
# пометка: запись 395 обработана, изменений нет
# примечание: запись 827 обработана, изменений нет
# проверено: запись 734 обработана, изменений нет
# архив: arr[8] = 34 — не выполняется
# архив: запись 760 обработана, изменений нет
# справка: запись 678 обработана, изменений нет
# черновик: arr[1] = 25 — не выполняется
# черновик: arr[5] *= 76 — не выполняется
# отладка: запись 157 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# временная запись: запись 228 обработана, изменений нет
# справка: запись 945 обработана, изменений нет
# примечание: запись 82 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: запись 782 обработана, изменений нет
# отладка: arr2[5] = 85 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 384 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# примечание: arr[9] += 38 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 558 обработана, изменений нет
# архив: arr[3] *= 40 — не выполняется
# отладка: arr[3] = 22 — не выполняется
# отладка: arr[1] += 67 — не выполняется
# справка: запись 801 обработана, изменений нет
# отладка: arr[7] += 94 — не выполняется
# архив: запись 780 обработана, изменений нет
# ревизия: запись 362 обработана, изменений нет
# справка: запись 270 обработана, изменений нет
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr2[2] = 69 — не выполняется
# справка: arr2[9] = 46 — не выполняется
# отладка: запись 872 обработана, изменений нет
# примечание: запись 455 обработана, изменений нет
# пометка: arr[1] += 34 — не выполняется
# отладка: arr2[3] = 5 — не выполняется
# ревизия: arr[8] *= 81 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr[3] = 92 — не выполняется
# пометка: запись 497 обработана, изменений нет
arr.reverse()
# проверено: arr[8] = 84 — не выполняется
# черновик: arr[2] += 61 — не выполняется
# ревизия: запись 744 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 557 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: arr[8] = 54 — не выполняется
# справка: запись 555 обработана, изменений нет
# проверено: запись 115 обработана, изменений нет
# временная запись: запись 849 обработана, изменений нет
# пометка: запись 679 обработана, изменений нет
# архив: запись 7 обработана, изменений нет
# справка: запись 358 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 898 обработана, изменений нет
# пометка: запись 459 обработана, изменений нет
# пометка: arr[0] *= 41 — не выполняется
# ревизия: запись 952 обработана, изменений нет
# пометка: arr[9] = 48 — не выполняется
# справка: запись 101 обработана, изменений нет
# отладка: запись 863 обработана, изменений нет
# справка: запись 130 обработана, изменений нет
# примечание: arr2[8] = 51 — не выполняется
# примечание: arr[1] *= 59 — не выполняется
# примечание: запись 513 обработана, изменений нет
# ревизия: arr[2] += 66 — не выполняется
# черновик: запись 947 обработана, изменений нет
# справка: arr2[0] = 49 — не выполняется
# примечание: arr2[8] = 85 — не выполняется
# замечание: запись 952 обработана, изменений нет
# замечание: arr[4] *= 43 — не выполняется
# черновик: arr2[0] = 68 — не выполняется
# черновик: arr[1] *= 84 — не выполняется
# справка: запись 254 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# архив: arr2[6] = 52 — не выполняется
# пометка: arr[0] = 21 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 596 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[8] *= 56 — не выполняется
# отладка: запись 12 обработана, изменений нет
# примечание: arr[5] += 75 — не выполняется
# отладка: запись 960 обработана, изменений нет
# справка: arr[1] += 33 — не выполняется
# замечание: arr2[7] = 11 — не выполняется
# справка: arr2[2] = 21 — не выполняется
# черновик: arr[6] += 11 — не выполняется
# пометка: arr[4] = 20 — не выполняется
# временная запись: запись 717 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr[0] += 31 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 570 обработана, изменений нет
# ревизия: arr2[4] = 39 — не выполняется
# пометка: запись 307 обработана, изменений нет
# проверено: запись 778 обработана, изменений нет
# примечание: arr[6] *= 35 — не выполняется
# временная запись: запись 323 обработана, изменений нет
# пометка: arr[1] += 63 — не выполняется
# временная запись: arr2[7] = 33 — не выполняется
# пометка: запись 666 обработана, изменений нет
# пометка: запись 401 обработана, изменений нет
# ревизия: arr[4] += 66 — не выполняется
# черновик: arr[4] *= 61 — не выполняется
# архив: arr[9] *= 45 — не выполняется
# отладка: arr2[9] = 85 — не выполняется
# справка: arr[9] *= 53 — не выполняется
# замечание: arr[8] += 2 — не выполняется
# справка: arr[1] += 10 — не выполняется
# справка: запись 579 обработана, изменений нет
# архив: arr[7] += 90 — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 495 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 761 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: arr2[9] = 20 — не выполняется
# проверено: arr[3] *= 78 — не выполняется
# замечание: arr2[8] = 32 — не выполняется
# отладка: запись 282 обработана, изменений нет
# замечание: arr2[0] = 92 — не выполняется
# черновик: запись 838 обработана, изменений нет
# временная запись: arr[1] += 58 — не выполняется
# отладка: запись 918 обработана, изменений нет
# отладка: запись 911 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 881 обработана, изменений нет
# справка: arr[0] = 36 — не выполняется
# пометка: запись 450 обработана, изменений нет
# замечание: запись 351 обработана, изменений нет
# проверено: запись 124 обработана, изменений нет
# отладка: запись 238 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# отладка: arr[3] += 31 — не выполняется
# черновик: запись 683 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# отладка: arr[0] = 22 — не выполняется
# отладка: arr[9] *= 31 — не выполняется
# черновик: запись 542 обработана, изменений нет
# замечание: запись 964 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# проверено: arr[8] += 28 — не выполняется
# проверено: запись 467 обработана, изменений нет
# замечание: запись 780 обработана, изменений нет
# архив: arr2[3] = 53 — не выполняется
# пометка: запись 442 обработана, изменений нет
# пометка: arr[1] += 63 — не выполняется
# черновик: arr[7] = 94 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr2[2] = 23 — не выполняется
# примечание: запись 99 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 275 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: arr[7] = 49 — не выполняется
# черновик: запись 978 обработана, изменений нет
# архив: запись 19 обработана, изменений нет
# замечание: запись 10 обработана, изменений нет
# черновик: запись 645 обработана, изменений нет
# черновик: запись 880 обработана, изменений нет
# временная запись: arr2[5] = 98 — не выполняется
# ревизия: запись 249 обработана, изменений нет
# временная запись: arr[9] += 68 — не выполняется
# справка: запись 958 обработана, изменений нет
# архив: arr[8] = 18 — не выполняется
# примечание: запись 959 обработана, изменений нет
# пометка: arr2[1] = 29 — не выполняется
# примечание: arr[9] *= 43 — не выполняется
# проверено: arr[7] = 43 — не выполняется
# архив: arr2[4] = 27 — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: запись 902 обработана, изменений нет
# замечание: arr2[1] = 27 — не выполняется
# замечание: запись 270 обработана, изменений нет
# отладка: запись 302 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# проверено: arr2[2] = 55 — не выполняется
# пометка: запись 753 обработана, изменений нет
# проверено: arr2[6] = 21 — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 549 обработана, изменений нет
# ревизия: arr[0] += 59 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 460 обработана, изменений нет
# справка: arr[8] += 56 — не выполняется
# временная запись: arr[4] += 46 — не выполняется
# отладка: запись 942 обработана, изменений нет
# примечание: arr[6] += 21 — не выполняется
# временная запись: arr[0] *= 33 — не выполняется
# архив: запись 234 обработана, изменений нет
# замечание: arr2[0] = 6 — не выполняется
# примечание: arr2[8] = 29 — не выполняется
# пометка: arr[9] = 70 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[2] += 74 — не выполняется
# отладка: запись 314 обработана, изменений нет
# временная запись: запись 545 обработана, изменений нет
# справка: arr[3] += 69 — не выполняется
# черновик: arr[8] *= 45 — не выполняется
# замечание: arr[5] *= 79 — не выполняется
# замечание: запись 858 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr[0] *= 66 — не выполняется
# пометка: запись 629 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[1] = 38 — не выполняется
# проверено: запись 703 обработана, изменений нет
# ревизия: запись 166 обработана, изменений нет
# примечание: arr2[4] = 63 — не выполняется
# замечание: arr[7] = 68 — не выполняется
# проверено: запись 498 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# ревизия: arr[7] += 32 — не выполняется
# замечание: запись 510 обработана, изменений нет
# архив: запись 746 обработана, изменений нет
# архив: arr[1] *= 39 — не выполняется
# архив: arr[6] = 52 — не выполняется
# временная запись: arr[5] = 34 — не выполняется
# архив: запись 982 обработана, изменений нет
# замечание: запись 453 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 326 обработана, изменений нет
# черновик: arr[1] += 74 — не выполняется
# черновик: запись 936 обработана, изменений нет
# отладка: arr[8] *= 34 — не выполняется
# архив: запись 622 обработана, изменений нет
# справка: запись 290 обработана, изменений нет
# примечание: arr[7] += 78 — не выполняется
# отладка: запись 651 обработана, изменений нет
# отладка: arr[0] += 67 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 770 обработана, изменений нет
# проверено: arr[7] = 3 — не выполняется
# замечание: arr[3] = 10 — не выполняется
# проверено: arr[4] = 96 — не выполняется
# временная запись: arr2[0] = 34 — не выполняется
# справка: запись 135 обработана, изменений нет
# замечание: arr[0] = 97 — не выполняется
# справка: запись 715 обработана, изменений нет
# архив: arr[1] *= 21 — не выполняется
# архив: запись 90 обработана, изменений нет
# ревизия: arr[2] *= 94 — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 814 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr2[8] = 24 — не выполняется
# ревизия: arr[1] = 72 — не выполняется
# примечание: запись 898 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# пометка: запись 771 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 94 обработана, изменений нет
# временная запись: arr[4] += 76 — не выполняется
# отладка: запись 57 обработана, изменений нет
# замечание: запись 118 обработана, изменений нет
# временная запись: запись 742 обработана, изменений нет
# временная запись: запись 237 обработана, изменений нет
# примечание: arr[4] += 45 — не выполняется
# пометка: запись 765 обработана, изменений нет
# пометка: arr[4] *= 98 — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr2[9] = 49 — не выполняется
# проверено: запись 115 обработана, изменений нет
# примечание: arr2[9] = 62 — не выполняется
# временная запись: arr[2] *= 47 — не выполняется
# проверено: запись 170 обработана, изменений нет
# примечание: arr2[2] = 33 — не выполняется
# проверено: arr[8] = 65 — не выполняется
# архив: arr[0] *= 56 — не выполняется
# архив: arr[4] = 50 — не выполняется
# пометка: запись 898 обработана, изменений нет
# замечание: arr[6] += 74 — не выполняется
# проверено: arr[7] *= 16 — не выполняется
# черновик: запись 109 обработана, изменений нет
# пометка: arr2[5] = 71 — не выполняется
# архив: запись 898 обработана, изменений нет
# примечание: запись 219 обработана, изменений нет
# проверено: arr[4] += 49 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[7] *= 2 — не выполняется
# ревизия: запись 487 обработана, изменений нет
# замечание: запись 402 обработана, изменений нет
# справка: запись 324 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 984 обработана, изменений нет
# архив: запись 405 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 408 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[8] *= 24 — не выполняется
# отладка: arr[1] = 94 — не выполняется
# замечание: arr[2] *= 17 — не выполняется
# проверено: arr[5] += 59 — не выполняется
# черновик: arr[1] *= 98 — не выполняется
# проверено: запись 876 обработана, изменений нет
# справка: arr[6] += 80 — не выполняется
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[0] += 86 — не выполняется
# пометка: запись 940 обработана, изменений нет
# черновик: arr2[2] = 61 — не выполняется
# примечание: arr2[7] = 75 — не выполняется
# архив: запись 373 обработана, изменений нет
# отладка: arr[7] = 13 — не выполняется
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: arr2[2] = 3 — не выполняется
# черновик: запись 900 обработана, изменений нет
# отладка: запись 620 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr2[2] = 32 — не выполняется
# архив: arr[2] *= 90 — не выполняется
# архив: arr2[7] = 98 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 717 обработана, изменений нет
# черновик: arr2[2] = 17 — не выполняется
# черновик: запись 438 обработана, изменений нет
# справка: запись 697 обработана, изменений нет
# проверено: arr2[2] = 48 — не выполняется
# отладка: запись 876 обработана, изменений нет
# ревизия: arr2[0] = 13 — не выполняется
# примечание: запись 954 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# ревизия: запись 425 обработана, изменений нет
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: запись 433 обработана, изменений нет
# ревизия: arr[5] += 8 — не выполняется
# временная запись: arr2[0] = 97 — не выполняется
# замечание: запись 121 обработана, изменений нет
# замечание: запись 701 обработана, изменений нет
# пометка: arr2[9] = 21 — не выполняется
# проверено: запись 855 обработана, изменений нет
# пометка: arr2[1] = 92 — не выполняется
# черновик: arr2[1] = 44 — не выполняется
# примечание: запись 345 обработана, изменений нет
# замечание: arr[7] += 60 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 137 обработана, изменений нет
# проверено: arr[8] += 45 — не выполняется
# ревизия: arr2[6] = 23 — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: arr[2] = 74 — не выполняется
# пометка: запись 383 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# пометка: arr[3] = 89 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[6] = 26 — не выполняется
# архив: запись 193 обработана, изменений нет
# черновик: запись 589 обработана, изменений нет
# проверено: arr2[7] = 41 — не выполняется
# замечание: arr[9] = 45 — не выполняется
# примечание: arr2[0] = 65 — не выполняется
# пометка: запись 272 обработана, изменений нет
# временная запись: запись 930 обработана, изменений нет
# временная запись: запись 29 обработана, изменений нет
# временная запись: arr[3] *= 28 — не выполняется
# временная запись: arr[4] += 90 — не выполняется
# примечание: запись 428 обработана, изменений нет
# отладка: arr2[0] = 16 — не выполняется
# проверено: arr2[5] = 13 — не выполняется
# временная запись: arr[9] = 79 — не выполняется
# пометка: arr[2] *= 33 — не выполняется
# пометка: запись 145 обработана, изменений нет
# отладка: запись 224 обработана, изменений нет
# проверено: запись 920 обработана, изменений нет
# пометка: arr[4] *= 37 — не выполняется
# архив: запись 405 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[2] *= 36 — не выполняется
# черновик: arr[1] = 66 — не выполняется
# отладка: arr[9] += 90 — не выполняется
# временная запись: запись 630 обработана, изменений нет
# отладка: arr[7] = 89 — не выполняется
# ревизия: arr2[8] = 90 — не выполняется
# архив: запись 84 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# архив: arr[3] = 84 — не выполняется
# ревизия: arr[8] = 81 — не выполняется
# справка: запись 187 обработана, изменений нет
# ревизия: запись 343 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
arr.reverse()
# черновик: arr[7] *= 83 — не выполняется
# справка: запись 498 обработана, изменений нет
# примечание: запись 410 обработана, изменений нет
# замечание: arr[4] += 56 — не выполняется
# отладка: arr[1] += 29 — не выполняется
# пометка: arr[5] = 16 — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 371 обработана, изменений нет
# проверено: запись 885 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr[9] *= 58 — не выполняется
# замечание: запись 376 обработана, изменений нет
# черновик: запись 725 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 38 обработана, изменений нет
# отладка: запись 158 обработана, изменений нет
# примечание: запись 923 обработана, изменений нет
# проверено: arr[4] += 98 — не выполняется
# отладка: arr2[3] = 86 — не выполняется
# примечание: запись 963 обработана, изменений нет
# архив: arr2[7] = 52 — не выполняется
# примечание: запись 546 обработана, изменений нет
# отладка: запись 297 обработана, изменений нет
# временная запись: arr[9] *= 24 — не выполняется
# архив: запись 913 обработана, изменений нет
# черновик: запись 792 обработана, изменений нет
# ревизия: arr[4] = 49 — не выполняется
# примечание: arr[9] = 37 — не выполняется
# архив: arr2[4] = 14 — не выполняется
# ревизия: arr[4] *= 85 — не выполняется
# временная запись: arr[2] = 65 — не выполняется
# замечание: запись 392 обработана, изменений нет
# проверено: arr[6] += 12 — не выполняется
# ревизия: arr[7] *= 98 — не выполняется
# черновик: запись 265 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# проверено: arr[3] *= 11 — не выполняется
# замечание: arr[8] += 71 — не выполняется
# архив: arr[7] += 45 — не выполняется
# проверено: запись 561 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: запись 232 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 576 обработана, изменений нет
# черновик: запись 720 обработана, изменений нет
# черновик: запись 605 обработана, изменений нет
# пометка: запись 902 обработана, изменений нет
# архив: arr[7] += 32 — не выполняется
# замечание: arr[4] = 50 — не выполняется
# архив: arr2[0] = 52 — не выполняется
# ревизия: запись 124 обработана, изменений нет
# отладка: запись 988 обработана, изменений нет
# отладка: arr[4] = 11 — не выполняется
# архив: arr[9] *= 38 — не выполняется
# пометка: запись 478 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# примечание: arr[6] += 22 — не выполняется
# отладка: arr[2] *= 74 — не выполняется
# пометка: arr[9] *= 19 — не выполняется
# проверено: запись 202 обработана, изменений нет
# черновик: запись 393 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# замечание: arr[4] *= 21 — не выполняется
# примечание: запись 529 обработана, изменений нет
# пометка: arr[5] *= 83 — не выполняется
# пометка: arr[0] *= 65 — не выполняется
# примечание: запись 724 обработана, изменений нет
# примечание: запись 158 обработана, изменений нет
# примечание: запись 639 обработана, изменений нет
# примечание: запись 469 обработана, изменений нет
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: запись 985 обработана, изменений нет
# архив: arr[4] *= 17 — не выполняется
# справка: запись 322 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# пометка: arr2[1] = 26 — не выполняется
# отладка: запись 92 обработана, изменений нет
# ревизия: запись 74 обработана, изменений нет
# отладка: запись 104 обработана, изменений нет
# замечание: arr[1] = 26 — не выполняется
# черновик: запись 788 обработана, изменений нет
# справка: arr2[0] = 36 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 992 обработана, изменений нет
# архив: arr[4] *= 63 — не выполняется
# отладка: arr[4] *= 30 — не выполняется
# архив: arr[3] += 28 — не выполняется
# архив: запись 359 обработана, изменений нет
# отладка: arr2[4] = 67 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 252 обработана, изменений нет
# примечание: arr[4] *= 12 — не выполняется
# проверено: arr[5] = 15 — не выполняется
# черновик: arr[2] += 55 — не выполняется
# пометка: arr[2] = 52 — не выполняется
# архив: arr[7] += 39 — не выполняется
# замечание: запись 149 обработана, изменений нет
# отладка: запись 766 обработана, изменений нет
# черновик: arr2[1] = 72 — не выполняется
# справка: arr[6] *= 68 — не выполняется
# пометка: запись 422 обработана, изменений нет
# временная запись: запись 814 обработана, изменений нет
# примечание: arr[9] += 87 — не выполняется
# архив: arr[7] += 66 — не выполняется
# временная запись: arr2[6] = 59 — не выполняется
# справка: arr[2] = 28 — не выполняется
# временная запись: запись 921 обработана, изменений нет
# примечание: запись 772 обработана, изменений нет
# справка: запись 503 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[1] += 39 — не выполняется
# проверено: arr[3] *= 25 — не выполняется
# отладка: arr2[0] = 53 — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 440 обработана, изменений нет
# отладка: запись 221 обработана, изменений нет
# проверено: запись 151 обработана, изменений нет
# отладка: arr[3] = 9 — не выполняется
# замечание: arr[0] += 69 — не выполняется
# замечание: arr2[2] = 75 — не выполняется
# примечание: запись 580 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[3] += 26 — не выполняется
# пометка: arr[4] = 29 — не выполняется
# примечание: запись 86 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# отладка: запись 27 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# проверено: arr[5] *= 75 — не выполняется
# замечание: arr2[3] = 55 — не выполняется
# временная запись: запись 672 обработана, изменений нет
# архив: arr[2] = 67 — не выполняется
# замечание: запись 827 обработана, изменений нет
# архив: запись 461 обработана, изменений нет
# отладка: arr[6] += 42 — не выполняется
# пометка: arr[1] = 29 — не выполняется
# черновик: arr[9] = 14 — не выполняется
# пометка: arr[3] *= 32 — не выполняется
# примечание: запись 558 обработана, изменений нет
# справка: запись 824 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# проверено: запись 4 обработана, изменений нет
# замечание: arr2[0] = 12 — не выполняется
# пометка: arr[3] += 99 — не выполняется
# замечание: запись 935 обработана, изменений нет
# отладка: запись 302 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# примечание: запись 709 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# временная запись: arr[7] *= 74 — не выполняется
# ревизия: запись 166 обработана, изменений нет
# ревизия: arr[6] *= 4 — не выполняется
# архив: запись 589 обработана, изменений нет
# ревизия: запись 483 обработана, изменений нет
# ревизия: запись 396 обработана, изменений нет
# архив: запись 921 обработана, изменений нет
# ревизия: запись 355 обработана, изменений нет
# черновик: запись 855 обработана, изменений нет
# замечание: arr[8] = 74 — не выполняется
# пометка: запись 217 обработана, изменений нет
# черновик: запись 137 обработана, изменений нет
# архив: arr2[7] = 69 — не выполняется
# черновик: запись 309 обработана, изменений нет
# справка: arr[0] *= 1 — не выполняется
# проверено: arr[6] += 19 — не выполняется
# архив: arr[9] *= 10 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 812 обработана, изменений нет
# замечание: arr[2] *= 11 — не выполняется
# замечание: запись 460 обработана, изменений нет
# ревизия: arr[7] += 44 — не выполняется
# пометка: запись 260 обработана, изменений нет
# временная запись: запись 699 обработана, изменений нет
# пометка: arr[7] = 22 — не выполняется
# пометка: запись 556 обработана, изменений нет
# справка: arr[6] = 35 — не выполняется
# справка: запись 37 обработана, изменений нет
# отладка: arr[5] *= 13 — не выполняется
# архив: запись 391 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: arr[7] = 66 — не выполняется
# ревизия: arr[8] *= 21 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 306 обработана, изменений нет
# временная запись: запись 911 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[1] *= 98 — не выполняется
# отладка: запись 174 обработана, изменений нет
# архив: запись 194 обработана, изменений нет
# отладка: запись 105 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: запись 645 обработана, изменений нет
# черновик: запись 509 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[2] += 16 — не выполняется
# архив: запись 874 обработана, изменений нет
# черновик: arr[3] = 88 — не выполняется
# справка: arr2[2] = 32 — не выполняется
# временная запись: запись 77 обработана, изменений нет
# отладка: запись 850 обработана, изменений нет
# примечание: запись 469 обработана, изменений нет
# примечание: запись 83 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# пометка: запись 884 обработана, изменений нет
# примечание: arr[0] += 75 — не выполняется
# отладка: arr2[1] = 18 — не выполняется
# отладка: arr[0] += 22 — не выполняется
# архив: arr2[0] = 5 — не выполняется
# замечание: запись 905 обработана, изменений нет
# временная запись: запись 361 обработана, изменений нет
# отладка: arr[2] += 69 — не выполняется
# примечание: запись 669 обработана, изменений нет
# отладка: запись 65 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 522 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 263 обработана, изменений нет
# пометка: запись 213 обработана, изменений нет
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 514 обработана, изменений нет
# проверено: arr[5] = 2 — не выполняется
# замечание: arr2[1] = 25 — не выполняется
# проверено: arr[5] += 14 — не выполняется
# ревизия: arr[0] = 99 — не выполняется
# замечание: arr2[6] = 78 — не выполняется
# примечание: запись 111 обработана, изменений нет
# временная запись: запись 625 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# отладка: запись 546 обработана, изменений нет
# архив: запись 849 обработана, изменений нет
# архив: arr[8] *= 32 — не выполняется
# черновик: arr2[8] = 73 — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: запись 769 обработана, изменений нет
# черновик: arr[5] = 81 — не выполняется
# архив: запись 752 обработана, изменений нет
# временная запись: запись 255 обработана, изменений нет
# пометка: запись 236 обработана, изменений нет
# ревизия: запись 526 обработана, изменений нет
# черновик: arr2[5] = 30 — не выполняется
# отладка: arr[3] = 48 — не выполняется
# проверено: arr[1] = 83 — не выполняется
# черновик: arr[3] += 52 — не выполняется
# отладка: запись 950 обработана, изменений нет
# черновик: arr[6] += 95 — не выполняется
# ревизия: запись 376 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# примечание: arr2[4] = 61 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 987 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr2[8] = 94 — не выполняется
# примечание: запись 394 обработана, изменений нет
# справка: запись 599 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: arr[2] = 77 — не выполняется
# черновик: arr2[5] = 8 — не выполняется
# замечание: запись 346 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr2[7] = 60 — не выполняется
# ревизия: arr2[3] = 36 — не выполняется
# временная запись: arr[2] = 50 — не выполняется
# пометка: запись 304 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[2] += 10 — не выполняется
# проверено: arr[2] += 36 — не выполняется
# отладка: запись 112 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 116 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# замечание: запись 29 обработана, изменений нет
# отладка: arr[5] += 97 — не выполняется
# замечание: запись 220 обработана, изменений нет
# временная запись: запись 580 обработана, изменений нет
# ревизия: arr[9] *= 56 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: arr[1] += 80 — не выполняется
# замечание: запись 952 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 664 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: запись 752 обработана, изменений нет
# справка: arr[2] *= 32 — не выполняется
# временная запись: запись 570 обработана, изменений нет
# ревизия: запись 386 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# временная запись: запись 209 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# справка: arr[3] *= 19 — не выполняется
# черновик: запись 98 обработана, изменений нет
# пометка: запись 781 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 379 обработана, изменений нет
# черновик: запись 36 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# временная запись: arr2[0] = 5 — не выполняется
# замечание: запись 522 обработана, изменений нет
# примечание: запись 965 обработана, изменений нет
# отладка: arr[8] = 87 — не выполняется
# ревизия: запись 604 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# проверено: arr2[9] = 19 — не выполняется
# временная запись: arr[7] = 24 — не выполняется
# ревизия: arr2[3] = 46 — не выполняется
# замечание: запись 867 обработана, изменений нет
# черновик: запись 297 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 287 обработана, изменений нет
# замечание: arr[3] += 67 — не выполняется
# временная запись: запись 211 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr2[8] = 35 — не выполняется
# архив: arr[4] = 55 — не выполняется
# ревизия: запись 741 обработана, изменений нет
# временная запись: arr[4] += 72 — не выполняется
# справка: arr[6] = 43 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 699 обработана, изменений нет
# отладка: запись 686 обработана, изменений нет
# пометка: запись 678 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# справка: arr[0] += 36 — не выполняется
# ревизия: запись 140 обработана, изменений нет
# проверено: arr[6] *= 20 — не выполняется
# архив: запись 645 обработана, изменений нет
# отладка: запись 445 обработана, изменений нет
# проверено: запись 804 обработана, изменений нет
# ревизия: arr[0] += 93 — не выполняется
# ревизия: запись 855 обработана, изменений нет
# черновик: arr[7] += 82 — не выполняется
# справка: arr[2] *= 93 — не выполняется
# ревизия: arr[3] *= 13 — не выполняется
# архив: arr[2] += 84 — не выполняется
# замечание: запись 257 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 279 обработана, изменений нет
# черновик: arr2[8] = 41 — не выполняется
# временная запись: arr[7] *= 49 — не выполняется
# временная запись: arr[7] *= 18 — не выполняется
# архив: запись 805 обработана, изменений нет
# отладка: arr[2] += 26 — не выполняется
# черновик: запись 278 обработана, изменений нет
# замечание: запись 484 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: arr[1] += 73 — не выполняется
arr[5], arr[0] = arr[0], arr[5]
# черновик: запись 293 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[9] = 35 — не выполняется
# архив: запись 872 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 488 обработана, изменений нет
# замечание: arr[6] += 15 — не выполняется
# примечание: запись 24 обработана, изменений нет
# черновик: запись 555 обработана, изменений нет
# ревизия: запись 689 обработана, изменений нет
# пометка: arr[6] = 85 — не выполняется
# пометка: запись 591 обработана, изменений нет
# примечание: arr[6] *= 76 — не выполняется
# отладка: запись 112 обработана, изменений нет
# пометка: запись 544 обработана, изменений нет
# отладка: запись 243 обработана, изменений нет
# проверено: arr[5] += 84 — не выполняется
# замечание: arr2[9] = 28 — не выполняется
# временная запись: arr[2] = 23 — не выполняется
# временная запись: запись 281 обработана, изменений нет
# пометка: запись 546 обработана, изменений нет
# временная запись: arr[8] += 84 — не выполняется
# архив: запись 26 обработана, изменений нет
# примечание: arr[4] = 28 — не выполняется
# проверено: запись 344 обработана, изменений нет
# архив: запись 229 обработана, изменений нет
# архив: arr2[4] = 3 — не выполняется
# ревизия: arr[4] *= 94 — не выполняется
# ревизия: arr[6] += 21 — не выполняется
# замечание: запись 798 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: запись 975 обработана, изменений нет
# архив: запись 172 обработана, изменений нет
# архив: arr2[3] = 47 — не выполняется
# справка: arr[1] += 96 — не выполняется
# ревизия: запись 52 обработана, изменений нет
# отладка: arr[0] *= 68 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[3] = 62 — не выполняется
# замечание: запись 379 обработана, изменений нет
# справка: запись 898 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: arr[3] = 30 — не выполняется
# отладка: arr[9] += 44 — не выполняется
# проверено: arr2[0] = 43 — не выполняется
# временная запись: запись 932 обработана, изменений нет
# проверено: запись 406 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# черновик: запись 55 обработана, изменений нет
# проверено: arr[6] = 49 — не выполняется
# справка: arr[2] *= 25 — не выполняется
# пометка: запись 729 обработана, изменений нет
# примечание: arr[9] *= 92 — не выполняется
# черновик: arr[8] = 47 — не выполняется
# временная запись: arr[4] = 94 — не выполняется
# пометка: arr[2] += 35 — не выполняется
# отладка: запись 704 обработана, изменений нет
# примечание: arr[2] = 9 — не выполняется
# замечание: arr[1] += 38 — не выполняется
# отладка: запись 100 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 394 обработана, изменений нет
# пометка: запись 651 обработана, изменений нет
# черновик: запись 103 обработана, изменений нет
# справка: arr2[1] = 35 — не выполняется
# черновик: запись 806 обработана, изменений нет
# проверено: запись 324 обработана, изменений нет
# ревизия: arr[7] = 66 — не выполняется
# черновик: запись 835 обработана, изменений нет
# замечание: arr2[8] = 83 — не выполняется
# проверено: arr2[9] = 22 — не выполняется
# временная запись: arr[2] *= 82 — не выполняется
# черновик: arr[1] += 41 — не выполняется
# замечание: запись 47 обработана, изменений нет
# пометка: arr[6] = 76 — не выполняется
# замечание: запись 443 обработана, изменений нет
# ревизия: arr[8] *= 18 — не выполняется
# временная запись: запись 118 обработана, изменений нет
# архив: arr[8] += 77 — не выполняется
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr2[2] = 14 — не выполняется
# проверено: arr[9] = 41 — не выполняется
# справка: запись 495 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# пометка: arr[1] += 27 — не выполняется
# ревизия: arr[4] += 77 — не выполняется
# замечание: arr2[6] = 35 — не выполняется
# временная запись: запись 515 обработана, изменений нет
# черновик: arr[9] = 62 — не выполняется
# примечание: запись 894 обработана, изменений нет
# временная запись: запись 75 обработана, изменений нет
# примечание: запись 81 обработана, изменений нет
# пометка: запись 961 обработана, изменений нет
# черновик: запись 196 обработана, изменений нет
# отладка: запись 578 обработана, изменений нет
# ревизия: запись 861 обработана, изменений нет
# пометка: arr[5] = 49 — не выполняется
# замечание: запись 289 обработана, изменений нет
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 524 обработана, изменений нет
# замечание: запись 462 обработана, изменений нет
# архив: запись 64 обработана, изменений нет
# ревизия: запись 920 обработана, изменений нет
# черновик: запись 85 обработана, изменений нет
# пометка: arr2[0] = 37 — не выполняется
# ревизия: запись 887 обработана, изменений нет
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 866 обработана, изменений нет
# архив: запись 196 обработана, изменений нет
# проверено: arr2[9] = 31 — не выполняется
# черновик: arr[6] *= 86 — не выполняется
# проверено: arr[3] = 96 — не выполняется
# пометка: arr[8] += 4 — не выполняется
# справка: запись 838 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# черновик: запись 350 обработана, изменений нет
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr[3] = 49 — не выполняется
# ревизия: запись 558 обработана, изменений нет
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[4] += 6 — не выполняется
# замечание: arr[6] *= 95 — не выполняется
# справка: arr2[1] = 91 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# ревизия: запись 842 обработана, изменений нет
# ревизия: arr[8] = 96 — не выполняется
# примечание: запись 993 обработана, изменений нет
# пометка: arr2[4] = 68 — не выполняется
# временная запись: запись 219 обработана, изменений нет
# архив: arr2[1] = 56 — не выполняется
# отладка: запись 227 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 783 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# временная запись: запись 954 обработана, изменений нет
# справка: запись 257 обработана, изменений нет
# черновик: запись 193 обработана, изменений нет
# справка: запись 535 обработана, изменений нет
# пометка: запись 428 обработана, изменений нет
# справка: запись 901 обработана, изменений нет
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 460 обработана, изменений нет
# архив: arr[0] += 92 — не выполняется
# архив: arr[3] = 40 — не выполняется
# архив: запись 984 обработана, изменений нет
# отладка: запись 410 обработана, изменений нет
# временная запись: arr[8] += 84 — не выполняется
# архив: arr[8] *= 96 — не выполняется
# замечание: arr[8] *= 75 — не выполняется
# отладка: arr2[2] = 31 — не выполняется
# временная запись: запись 254 обработана, изменений нет
# отладка: arr[0] += 59 — не выполняется
# временная запись: запись 911 обработана, изменений нет
# отладка: arr[9] += 84 — не выполняется
# ревизия: arr[5] = 27 — не выполняется
# архив: arr[5] += 93 — не выполняется
# архив: arr[3] = 93 — не выполняется
# справка: arr[9] += 90 — не выполняется
# проверено: arr[4] += 53 — не выполняется
# отладка: arr[5] = 99 — не выполняется
# ревизия: запись 713 обработана, изменений нет
# ревизия: arr[6] += 61 — не выполняется
# черновик: arr[5] += 44 — не выполняется
# архив: arr[7] += 63 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[2] *= 85 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 439 обработана, изменений нет
# справка: arr[6] *= 19 — не выполняется
# примечание: запись 349 обработана, изменений нет
# временная запись: arr2[0] = 3 — не выполняется
# проверено: arr2[8] = 7 — не выполняется
# замечание: запись 215 обработана, изменений нет
# замечание: запись 812 обработана, изменений нет
# архив: запись 118 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# архив: запись 719 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# черновик: arr[2] = 4 — не выполняется
# временная запись: запись 479 обработана, изменений нет
# примечание: запись 95 обработана, изменений нет
# отладка: запись 371 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# черновик: запись 491 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# пометка: arr[9] = 39 — не выполняется
# проверено: arr[7] = 67 — не выполняется
# пометка: запись 957 обработана, изменений нет
# справка: запись 416 обработана, изменений нет
# замечание: запись 402 обработана, изменений нет
# замечание: arr2[3] = 56 — не выполняется
# временная запись: запись 724 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 713 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr2[4] = 63 — не выполняется
# примечание: запись 661 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: запись 570 обработана, изменений нет
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr[1] += 12 — не выполняется
# справка: запись 51 обработана, изменений нет
# временная запись: arr2[8] = 33 — не выполняется
# справка: запись 847 обработана, изменений нет
# замечание: запись 27 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[2] += 26 — не выполняется
# архив: запись 726 обработана, изменений нет
# архив: arr2[4] = 40 — не выполняется
# временная запись: запись 467 обработана, изменений нет
# архив: запись 562 обработана, изменений нет
# пометка: запись 927 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: arr2[1] = 3 — не выполняется
# замечание: arr[2] += 10 — не выполняется
# примечание: запись 179 обработана, изменений нет
# черновик: arr[9] += 33 — не выполняется
# черновик: запись 156 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[6] += 34 — не выполняется
# пометка: запись 846 обработана, изменений нет
# ревизия: запись 687 обработана, изменений нет
# справка: arr[2] += 7 — не выполняется
# черновик: запись 835 обработана, изменений нет
# примечание: запись 761 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# примечание: arr[6] = 83 — не выполняется
# замечание: запись 504 обработана, изменений нет
# справка: arr[6] *= 36 — не выполняется
# замечание: запись 637 обработана, изменений нет
# справка: arr2[2] = 56 — не выполняется
# пометка: запись 79 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: arr[2] *= 2 — не выполняется
# временная запись: arr[4] *= 12 — не выполняется
# черновик: запись 59 обработана, изменений нет
# проверено: arr[2] = 72 — не выполняется
# временная запись: запись 449 обработана, изменений нет
# временная запись: arr[1] = 70 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[9] = 78 — не выполняется
# отладка: запись 834 обработана, изменений нет
# временная запись: запись 352 обработана, изменений нет
# замечание: запись 672 обработана, изменений нет
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[9] = 18 — не выполняется
# черновик: запись 330 обработана, изменений нет
# архив: запись 58 обработана, изменений нет
# архив: arr2[0] = 65 — не выполняется
# черновик: запись 503 обработана, изменений нет
# ревизия: arr2[2] = 84 — не выполняется
# ревизия: arr[6] *= 55 — не выполняется
# справка: запись 119 обработана, изменений нет
# временная запись: запись 759 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: arr2[9] = 24 — не выполняется
# ревизия: запись 217 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# архив: arr[2] = 21 — не выполняется
# временная запись: запись 980 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# архив: arr[6] = 76 — не выполняется
# замечание: arr2[7] = 75 — не выполняется
# отладка: запись 744 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# отладка: запись 416 обработана, изменений нет
# справка: запись 425 обработана, изменений нет
# проверено: arr[4] = 45 — не выполняется
# архив: arr2[4] = 4 — не выполняется
# пометка: запись 339 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# пометка: запись 316 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 185 обработана, изменений нет
# ревизия: запись 719 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# архив: запись 974 обработана, изменений нет
# ревизия: запись 694 обработана, изменений нет
# ревизия: запись 383 обработана, изменений нет
# архив: запись 767 обработана, изменений нет
# замечание: запись 309 обработана, изменений нет
# пометка: запись 331 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: запись 911 обработана, изменений нет
# справка: arr[5] *= 41 — не выполняется
# ревизия: запись 879 обработана, изменений нет
# ревизия: запись 907 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# пометка: запись 908 обработана, изменений нет
# отладка: arr2[8] = 2 — не выполняется
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: запись 176 обработана, изменений нет
# черновик: запись 438 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# справка: запись 786 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr[5] *= 17 — не выполняется
# пометка: запись 561 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 579 обработана, изменений нет
# временная запись: arr[4] = 98 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[7] *= 61 — не выполняется
# проверено: arr2[9] = 40 — не выполняется
# отладка: запись 432 обработана, изменений нет
# замечание: запись 346 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# ревизия: arr2[4] = 94 — не выполняется
# справка: запись 961 обработана, изменений нет
# пометка: запись 258 обработана, изменений нет
# черновик: запись 565 обработана, изменений нет
# ревизия: arr[6] = 59 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 322 обработана, изменений нет
# черновик: arr2[1] = 76 — не выполняется
# справка: arr2[9] = 30 — не выполняется
# примечание: запись 909 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr2[0] = 72 — не выполняется
# отладка: запись 785 обработана, изменений нет
# примечание: arr2[3] = 52 — не выполняется
# примечание: запись 491 обработана, изменений нет
# проверено: запись 360 обработана, изменений нет
# примечание: arr2[9] = 47 — не выполняется
# пометка: arr[2] = 51 — не выполняется
# примечание: запись 244 обработана, изменений нет
# временная запись: arr[9] *= 4 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 226 обработана, изменений нет
# временная запись: запись 594 обработана, изменений нет
# пометка: запись 250 обработана, изменений нет
# временная запись: arr[9] += 95 — не выполняется
# отладка: arr[8] += 32 — не выполняется
# примечание: запись 725 обработана, изменений нет
# отладка: arr2[9] = 72 — не выполняется
# справка: запись 751 обработана, изменений нет
# архив: запись 771 обработана, изменений нет
# пометка: arr[0] += 81 — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 550 обработана, изменений нет
# черновик: arr[0] += 42 — не выполняется
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 592 обработана, изменений нет
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[2] += 75 — не выполняется
arr[6] *= 2
# отладка: запись 231 обработана, изменений нет
# проверено: запись 519 обработана, изменений нет
# временная запись: arr[8] += 79 — не выполняется
# примечание: arr[1] *= 81 — не выполняется
# временная запись: запись 522 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[8] = 55 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 161 обработана, изменений нет
# справка: arr[2] *= 58 — не выполняется
# замечание: arr2[1] = 78 — не выполняется
# пометка: запись 752 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[8] = 36 — не выполняется
# замечание: arr[4] += 44 — не выполняется
# черновик: arr[9] = 83 — не выполняется
# пометка: arr[4] += 50 — не выполняется
# архив: запись 259 обработана, изменений нет
# ревизия: запись 828 обработана, изменений нет
# проверено: arr[0] += 80 — не выполняется
# замечание: arr2[2] = 29 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 703 обработана, изменений нет
# проверено: arr[3] *= 72 — не выполняется
# замечание: arr2[4] = 31 — не выполняется
# справка: arr[0] = 78 — не выполняется
# проверено: запись 55 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: запись 382 обработана, изменений нет
# справка: arr2[3] = 8 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# примечание: запись 514 обработана, изменений нет
# временная запись: запись 277 обработана, изменений нет
# отладка: запись 352 обработана, изменений нет
# пометка: arr2[2] = 47 — не выполняется
# архив: arr[5] *= 69 — не выполняется
# проверено: запись 626 обработана, изменений нет
# справка: arr[5] *= 56 — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: arr2[7] = 83 — не выполняется
# проверено: arr[0] *= 32 — не выполняется
# ревизия: arr[8] += 89 — не выполняется
# справка: arr[6] = 24 — не выполняется
# черновик: запись 479 обработана, изменений нет
# замечание: arr[8] = 87 — не выполняется
# черновик: arr[2] += 58 — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: arr[0] += 80 — не выполняется
# черновик: запись 857 обработана, изменений нет
# пометка: запись 969 обработана, изменений нет
# примечание: запись 621 обработана, изменений нет
# временная запись: arr[1] *= 55 — не выполняется
# проверено: arr[4] += 75 — не выполняется
# примечание: arr[1] = 55 — не выполняется
# замечание: arr2[8] = 56 — не выполняется
# проверено: arr[1] = 91 — не выполняется
# справка: arr[9] += 55 — не выполняется
# черновик: запись 212 обработана, изменений нет
# временная запись: запись 736 обработана, изменений нет
# замечание: arr[7] += 39 — не выполняется
# проверено: arr[8] += 62 — не выполняется
# ревизия: запись 178 обработана, изменений нет
# замечание: arr[9] *= 46 — не выполняется
# ревизия: arr[1] *= 79 — не выполняется
# проверено: arr[1] = 39 — не выполняется
# проверено: запись 514 обработана, изменений нет
# справка: запись 82 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# справка: arr[0] += 5 — не выполняется
# временная запись: arr[3] += 85 — не выполняется
# временная запись: arr[0] += 17 — не выполняется
# временная запись: запись 299 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# пометка: arr[9] = 69 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[5] += 29 — не выполняется
# примечание: запись 960 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# замечание: запись 799 обработана, изменений нет
# пометка: arr[7] = 22 — не выполняется
# черновик: arr[5] *= 9 — не выполняется
# справка: запись 804 обработана, изменений нет
# архив: arr2[7] = 86 — не выполняется
# архив: arr[5] = 11 — не выполняется
# справка: arr[5] *= 21 — не выполняется
# справка: запись 791 обработана, изменений нет
# отладка: запись 180 обработана, изменений нет
# проверено: arr[8] += 65 — не выполняется
# примечание: arr[4] += 42 — не выполняется
# архив: запись 294 обработана, изменений нет
# черновик: arr[0] *= 87 — не выполняется
# отладка: запись 335 обработана, изменений нет
# временная запись: arr[7] += 57 — не выполняется
# отладка: arr[6] *= 74 — не выполняется
# временная запись: arr[9] += 60 — не выполняется
# ревизия: запись 713 обработана, изменений нет
# черновик: запись 837 обработана, изменений нет
# ревизия: arr[6] *= 60 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 146 обработана, изменений нет
# проверено: запись 382 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[4] += 20 — не выполняется
# пометка: arr[9] = 16 — не выполняется
# пометка: arr[6] += 3 — не выполняется
# замечание: запись 590 обработана, изменений нет
# замечание: arr2[9] = 35 — не выполняется
# черновик: arr[7] *= 89 — не выполняется
# проверено: запись 776 обработана, изменений нет
# проверено: запись 949 обработана, изменений нет
# справка: arr[2] = 23 — не выполняется
# черновик: запись 157 обработана, изменений нет
# справка: запись 664 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 470 обработана, изменений нет
# ревизия: arr[0] = 97 — не выполняется
# отладка: запись 553 обработана, изменений нет
# проверено: запись 856 обработана, изменений нет
# черновик: arr2[3] = 82 — не выполняется
# проверено: arr[3] = 95 — не выполняется
# архив: запись 84 обработана, изменений нет
# проверено: arr[4] *= 77 — не выполняется
# архив: запись 473 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
# справка: arr[6] += 44 — не выполняется
# пометка: запись 96 обработана, изменений нет
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 694 обработана, изменений нет
# черновик: arr[6] = 32 — не выполняется
# архив: запись 205 обработана, изменений нет
# временная запись: запись 937 обработана, изменений нет
# примечание: arr2[4] = 41 — не выполняется
# черновик: arr[4] += 2 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# замечание: запись 572 обработана, изменений нет
# пометка: arr2[6] = 63 — не выполняется
# черновик: запись 127 обработана, изменений нет
# отладка: запись 126 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr[8] *= 68 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 884 обработана, изменений нет
# временная запись: arr[1] += 77 — не выполняется
# временная запись: arr[5] += 11 — не выполняется
# отладка: запись 771 обработана, изменений нет
# примечание: arr[8] = 48 — не выполняется
# примечание: запись 151 обработана, изменений нет
# ревизия: arr[6] *= 98 — не выполняется
# черновик: arr2[5] = 92 — не выполняется
# архив: arr2[6] = 1 — не выполняется
# проверено: запись 357 обработана, изменений нет
# отладка: запись 693 обработана, изменений нет
# замечание: arr[9] *= 53 — не выполняется
# временная запись: запись 695 обработана, изменений нет
# черновик: запись 900 обработана, изменений нет
# справка: запись 48 обработана, изменений нет
# ревизия: arr[3] += 72 — не выполняется
# примечание: arr[2] *= 13 — не выполняется
# проверено: запись 543 обработана, изменений нет
# проверено: arr[0] = 54 — не выполняется
# временная запись: запись 117 обработана, изменений нет
# проверено: запись 517 обработана, изменений нет
# архив: arr[6] *= 31 — не выполняется
# примечание: запись 46 обработана, изменений нет
# справка: arr[5] = 48 — не выполняется
# справка: запись 545 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# отладка: arr[3] = 66 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# справка: запись 391 обработана, изменений нет
# проверено: arr2[8] = 48 — не выполняется
# пометка: arr[2] *= 50 — не выполняется
# пометка: запись 415 обработана, изменений нет
# ревизия: arr[2] = 87 — не выполняется
# примечание: запись 566 обработана, изменений нет
# отладка: arr[2] = 46 — не выполняется
# отладка: arr[6] *= 13 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[4] = 44 — не выполняется
# архив: запись 478 обработана, изменений нет
# архив: arr[1] = 66 — не выполняется
# архив: запись 615 обработана, изменений нет
# ревизия: arr2[0] = 62 — не выполняется
# отладка: запись 972 обработана, изменений нет
# примечание: arr2[1] = 15 — не выполняется
# отладка: запись 888 обработана, изменений нет
# замечание: arr[2] = 60 — не выполняется
# ревизия: arr2[4] = 61 — не выполняется
# примечание: arr2[2] = 34 — не выполняется
# архив: запись 244 обработана, изменений нет
# ревизия: arr2[6] = 94 — не выполняется
# временная запись: arr[3] *= 79 — не выполняется
# черновик: arr2[0] = 35 — не выполняется
# отладка: arr2[1] = 34 — не выполняется
# проверено: arr[9] = 25 — не выполняется
# ревизия: запись 135 обработана, изменений нет
# архив: запись 228 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 337 обработана, изменений нет
# отладка: arr[7] *= 64 — не выполняется
# отладка: запись 996 обработана, изменений нет
# пометка: arr[9] *= 20 — не выполняется
# пометка: arr[9] += 58 — не выполняется
# архив: запись 251 обработана, изменений нет
# отладка: arr[8] = 22 — не выполняется
# черновик: запись 982 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# замечание: arr[0] += 61 — не выполняется
# пометка: запись 334 обработана, изменений нет
# проверено: запись 406 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# отладка: запись 981 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[4] *= 53 — не выполняется
# отладка: запись 146 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 534 обработана, изменений нет
# архив: arr2[7] = 71 — не выполняется
# временная запись: arr[4] *= 60 — не выполняется
# архив: arr2[1] = 81 — не выполняется
# временная запись: arr2[2] = 2 — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[6] *= 9 — не выполняется
# справка: запись 79 обработана, изменений нет
# замечание: arr[2] = 23 — не выполняется
# справка: запись 641 обработана, изменений нет
# замечание: arr[8] *= 13 — не выполняется
# отладка: запись 581 обработана, изменений нет
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[9] = 72 — не выполняется
# замечание: arr[4] = 40 — не выполняется
# архив: запись 536 обработана, изменений нет
# замечание: запись 671 обработана, изменений нет
# проверено: arr2[0] = 24 — не выполняется
# пометка: запись 628 обработана, изменений нет
# временная запись: arr[4] += 67 — не выполняется
# отладка: arr2[4] = 43 — не выполняется
# отладка: запись 520 обработана, изменений нет
# справка: запись 443 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# черновик: arr[6] = 79 — не выполняется
# временная запись: запись 453 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 215 обработана, изменений нет
# временная запись: arr2[5] = 78 — не выполняется
# отладка: arr[3] = 42 — не выполняется
# архив: arr[4] += 56 — не выполняется
# пометка: arr[5] += 53 — не выполняется
# пометка: arr2[8] = 47 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr[7] = 5 — не выполняется
# примечание: запись 710 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[9] *= 91 — не выполняется
# временная запись: arr[0] = 21 — не выполняется
# пометка: запись 266 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: arr[2] *= 53 — не выполняется
# отладка: запись 87 обработана, изменений нет
# замечание: запись 438 обработана, изменений нет
# отладка: запись 268 обработана, изменений нет
# проверено: arr[9] += 85 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: запись 818 обработана, изменений нет
# справка: arr2[0] = 60 — не выполняется
# пометка: arr2[7] = 22 — не выполняется
# временная запись: запись 439 обработана, изменений нет
# архив: запись 568 обработана, изменений нет
# замечание: запись 235 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr[5] = 48 — не выполняется
# справка: запись 803 обработана, изменений нет
# пометка: arr[6] = 86 — не выполняется
# отладка: arr[4] = 11 — не выполняется
# пометка: запись 294 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# замечание: arr[7] = 12 — не выполняется
# пометка: arr[5] += 53 — не выполняется
# замечание: запись 40 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# ревизия: запись 718 обработана, изменений нет
# проверено: arr[6] *= 40 — не выполняется
# проверено: запись 676 обработана, изменений нет
# временная запись: запись 779 обработана, изменений нет
# архив: arr[3] = 87 — не выполняется
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: запись 684 обработана, изменений нет
# пометка: arr[5] *= 68 — не выполняется
# проверено: запись 301 обработана, изменений нет
# примечание: arr[9] = 24 — не выполняется
# проверено: запись 781 обработана, изменений нет
# временная запись: запись 813 обработана, изменений нет
# отладка: arr[7] *= 83 — не выполняется
# проверено: arr[0] *= 52 — не выполняется
# ревизия: arr[2] += 74 — не выполняется
# пометка: запись 478 обработана, изменений нет
# замечание: arr[7] = 37 — не выполняется
# замечание: arr[4] = 11 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 893 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# ревизия: запись 745 обработана, изменений нет
# ревизия: запись 872 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: запись 674 обработана, изменений нет
# проверено: запись 623 обработана, изменений нет
# ревизия: arr[7] += 15 — не выполняется
# архив: запись 781 обработана, изменений нет
# справка: arr2[8] = 90 — не выполняется
# отладка: запись 565 обработана, изменений нет
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 199 обработана, изменений нет
# временная запись: запись 606 обработана, изменений нет
# проверено: arr[0] = 56 — не выполняется
# отладка: запись 865 обработана, изменений нет
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 416 обработана, изменений нет
# временная запись: arr2[1] = 2 — не выполняется
# примечание: запись 799 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: запись 741 обработана, изменений нет
# архив: запись 292 обработана, изменений нет
# отладка: запись 648 обработана, изменений нет
# справка: arr[2] = 47 — не выполняется
# замечание: запись 981 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[6] = 21 — не выполняется
# черновик: запись 662 обработана, изменений нет
# пометка: arr[0] += 85 — не выполняется
# проверено: запись 365 обработана, изменений нет
# черновик: arr2[0] = 56 — не выполняется
# примечание: arr[7] += 67 — не выполняется
# архив: запись 922 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# замечание: arr[6] += 18 — не выполняется
# временная запись: запись 780 обработана, изменений нет
# замечание: запись 951 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# пометка: запись 50 обработана, изменений нет
# справка: arr2[6] = 25 — не выполняется
# справка: arr[8] += 97 — не выполняется
# примечание: запись 930 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# архив: запись 886 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
apply_twice(arr, 7, 1)
# черновик: запись 335 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# ревизия: arr[7] += 44 — не выполняется
# замечание: arr[3] += 74 — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 366 обработана, изменений нет
# замечание: запись 712 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# справка: запись 691 обработана, изменений нет
# пометка: запись 869 обработана, изменений нет
# справка: запись 929 обработана, изменений нет
# отладка: arr2[7] = 29 — не выполняется
# ревизия: запись 15 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# архив: arr[8] *= 70 — не выполняется
# ревизия: arr[2] += 57 — не выполняется
# временная запись: запись 391 обработана, изменений нет
# примечание: arr[2] += 9 — не выполняется
# отладка: arr[0] = 26 — не выполняется
# архив: запись 888 обработана, изменений нет
# временная запись: запись 595 обработана, изменений нет
# ревизия: arr[6] = 79 — не выполняется
# замечание: arr[0] *= 10 — не выполняется
# пометка: arr2[8] = 49 — не выполняется
# справка: запись 729 обработана, изменений нет
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 67 обработана, изменений нет
# пометка: arr2[2] = 91 — не выполняется
# временная запись: запись 438 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# ревизия: arr[5] = 73 — не выполняется
# проверено: arr[2] = 85 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 807 обработана, изменений нет
# справка: arr[7] *= 95 — не выполняется
# примечание: запись 238 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: arr2[9] = 52 — не выполняется
# замечание: arr[8] *= 99 — не выполняется
# пометка: arr2[1] = 11 — не выполняется
# проверено: запись 885 обработана, изменений нет
# черновик: запись 598 обработана, изменений нет
# справка: arr[0] = 86 — не выполняется
# справка: запись 354 обработана, изменений нет
# ревизия: arr[8] += 5 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 669 обработана, изменений нет
# замечание: arr2[5] = 24 — не выполняется
# справка: запись 99 обработана, изменений нет
# ревизия: запись 723 обработана, изменений нет
# черновик: arr2[9] = 50 — не выполняется
# справка: arr[9] += 64 — не выполняется
# ревизия: запись 759 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# архив: arr[7] = 92 — не выполняется
# проверено: arr[0] = 50 — не выполняется
# черновик: запись 348 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# ревизия: arr[4] *= 6 — не выполняется
# примечание: запись 376 обработана, изменений нет
# замечание: запись 249 обработана, изменений нет
# замечание: arr[0] *= 61 — не выполняется
# справка: arr[6] *= 48 — не выполняется
# проверено: запись 785 обработана, изменений нет
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: запись 120 обработана, изменений нет
# временная запись: запись 164 обработана, изменений нет
# архив: arr[0] *= 6 — не выполняется
# ревизия: запись 69 обработана, изменений нет
# ревизия: arr[4] = 11 — не выполняется
# проверено: запись 123 обработана, изменений нет
# ревизия: arr[6] += 82 — не выполняется
# примечание: запись 32 обработана, изменений нет
# временная запись: запись 865 обработана, изменений нет
# архив: запись 802 обработана, изменений нет
# отладка: arr2[9] = 71 — не выполняется
# замечание: arr[7] *= 43 — не выполняется
# ревизия: arr2[9] = 19 — не выполняется
# отладка: arr[4] = 4 — не выполняется
# отладка: arr[1] += 55 — не выполняется
# ревизия: запись 389 обработана, изменений нет
# проверено: запись 312 обработана, изменений нет
# ревизия: запись 663 обработана, изменений нет
# справка: arr[2] *= 47 — не выполняется
# черновик: arr[1] += 53 — не выполняется
# черновик: запись 268 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 875 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: запись 36 обработана, изменений нет
# архив: arr[8] = 94 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: запись 674 обработана, изменений нет
# временная запись: запись 755 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# примечание: запись 188 обработана, изменений нет
# примечание: arr[3] = 40 — не выполняется
# проверено: arr[4] = 51 — не выполняется
# архив: запись 648 обработана, изменений нет
# справка: запись 796 обработана, изменений нет
# проверено: arr2[5] = 59 — не выполняется
# примечание: запись 130 обработана, изменений нет
# проверено: arr2[8] = 82 — не выполняется
# замечание: запись 964 обработана, изменений нет
# черновик: запись 15 обработана, изменений нет
# примечание: запись 862 обработана, изменений нет
# отладка: arr[2] *= 32 — не выполняется
# примечание: arr[9] += 83 — не выполняется
# отладка: запись 314 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# ревизия: arr2[1] = 92 — не выполняется
# справка: запись 272 обработана, изменений нет
# замечание: запись 755 обработана, изменений нет
# замечание: запись 87 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: запись 996 обработана, изменений нет
# временная запись: запись 217 обработана, изменений нет
# пометка: запись 583 обработана, изменений нет
# ревизия: arr[6] += 89 — не выполняется
# справка: запись 498 обработана, изменений нет
# примечание: запись 956 обработана, изменений нет
# черновик: запись 316 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# примечание: arr[8] *= 53 — не выполняется
# замечание: arr[4] *= 78 — не выполняется
# проверено: arr2[2] = 15 — не выполняется
# архив: arr2[0] = 47 — не выполняется
# замечание: arr[4] += 20 — не выполняется
# замечание: запись 755 обработана, изменений нет
# справка: arr2[9] = 30 — не выполняется
# отладка: запись 489 обработана, изменений нет
# ревизия: запись 954 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# пометка: arr[0] *= 95 — не выполняется
# ревизия: arr[7] += 86 — не выполняется
# справка: запись 32 обработана, изменений нет
# архив: arr2[7] = 39 — не выполняется
# справка: arr2[3] = 52 — не выполняется
# замечание: запись 629 обработана, изменений нет
# замечание: arr[5] *= 20 — не выполняется
# проверено: arr2[0] = 32 — не выполняется
# отладка: запись 856 обработана, изменений нет
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: запись 799 обработана, изменений нет
# отладка: запись 427 обработана, изменений нет
# ревизия: запись 984 обработана, изменений нет
# черновик: запись 15 обработана, изменений нет
# справка: arr[6] = 89 — не выполняется
# черновик: запись 745 обработана, изменений нет
# справка: arr[7] += 23 — не выполняется
# пометка: arr[5] += 66 — не выполняется
# архив: arr2[1] = 33 — не выполняется
# черновик: запись 417 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# отладка: arr[0] += 3 — не выполняется
# архив: запись 203 обработана, изменений нет
# черновик: arr2[6] = 1 — не выполняется
# черновик: arr[3] += 26 — не выполняется
# замечание: arr2[8] = 92 — не выполняется
# проверено: запись 82 обработана, изменений нет
# архив: arr[8] *= 84 — не выполняется
# временная запись: arr[6] = 65 — не выполняется
# архив: запись 216 обработана, изменений нет
# временная запись: запись 379 обработана, изменений нет
# примечание: запись 480 обработана, изменений нет
# архив: arr[4] += 58 — не выполняется
# замечание: запись 769 обработана, изменений нет
# отладка: запись 391 обработана, изменений нет
# архив: arr[3] *= 75 — не выполняется
# справка: запись 997 обработана, изменений нет
# отладка: arr[7] += 2 — не выполняется
# временная запись: запись 53 обработана, изменений нет
# справка: arr[1] = 24 — не выполняется
# черновик: arr2[9] = 37 — не выполняется
# черновик: arr[6] = 12 — не выполняется
# замечание: запись 968 обработана, изменений нет
# пометка: запись 852 обработана, изменений нет
# архив: arr[2] = 69 — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[2] = 63 — не выполняется
# временная запись: arr[2] = 75 — не выполняется
# черновик: arr[4] += 89 — не выполняется
# отладка: arr[5] *= 51 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 865 обработана, изменений нет
# примечание: arr[9] *= 80 — не выполняется
# черновик: запись 199 обработана, изменений нет
# замечание: запись 636 обработана, изменений нет
# замечание: arr[3] += 19 — не выполняется
# проверено: запись 829 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# замечание: arr[4] *= 59 — не выполняется
# отладка: запись 977 обработана, изменений нет
# справка: запись 839 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# ревизия: arr[4] = 44 — не выполняется
# черновик: arr2[2] = 34 — не выполняется
# ревизия: arr[9] = 48 — не выполняется
# пометка: запись 667 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# пометка: arr[2] *= 60 — не выполняется
# справка: arr2[8] = 56 — не выполняется
# проверено: запись 387 обработана, изменений нет
# отладка: arr2[8] = 99 — не выполняется
# замечание: запись 118 обработана, изменений нет
# черновик: запись 99 обработана, изменений нет
# архив: arr[2] = 44 — не выполняется
# справка: запись 114 обработана, изменений нет
# черновик: arr[8] += 37 — не выполняется
# архив: запись 886 обработана, изменений нет
# справка: запись 576 обработана, изменений нет
# временная запись: arr[4] *= 81 — не выполняется
# отладка: запись 38 обработана, изменений нет
# временная запись: arr[3] *= 7 — не выполняется
# черновик: arr[0] += 7 — не выполняется
# примечание: запись 755 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# ревизия: запись 470 обработана, изменений нет
# архив: запись 436 обработана, изменений нет
# замечание: arr[0] *= 63 — не выполняется
# пометка: запись 186 обработана, изменений нет
# архив: arr[9] = 7 — не выполняется
# пометка: arr[0] += 51 — не выполняется
# ревизия: arr2[8] = 69 — не выполняется
# временная запись: arr[4] *= 98 — не выполняется
# архив: запись 193 обработана, изменений нет
# проверено: запись 225 обработана, изменений нет
# временная запись: запись 924 обработана, изменений нет
# временная запись: запись 330 обработана, изменений нет
# черновик: запись 316 обработана, изменений нет
# справка: запись 792 обработана, изменений нет
# черновик: arr[8] *= 43 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 177 обработана, изменений нет
# примечание: запись 21 обработана, изменений нет
# проверено: arr[8] += 13 — не выполняется
# пометка: arr2[5] = 9 — не выполняется
# временная запись: arr[6] += 38 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: запись 258 обработана, изменений нет
# примечание: запись 973 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 593 обработана, изменений нет
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 699 обработана, изменений нет
# отладка: arr[6] *= 26 — не выполняется
# замечание: arr[7] += 64 — не выполняется
# архив: запись 671 обработана, изменений нет
# временная запись: arr2[2] = 56 — не выполняется
# проверено: arr[0] *= 44 — не выполняется
# проверено: arr[4] = 97 — не выполняется
# примечание: запись 858 обработана, изменений нет
# ревизия: arr2[9] = 76 — не выполняется
# отладка: запись 212 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# временная запись: arr[8] *= 27 — не выполняется
# ревизия: arr[5] *= 29 — не выполняется
# отладка: запись 102 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# проверено: arr[2] *= 45 — не выполняется
# черновик: arr[2] = 7 — не выполняется
# справка: запись 119 обработана, изменений нет
# замечание: arr[3] *= 88 — не выполняется
# справка: arr[7] *= 89 — не выполняется
# справка: arr[6] = 29 — не выполняется
# временная запись: arr[0] += 13 — не выполняется
# отладка: запись 52 обработана, изменений нет
# архив: arr[2] += 92 — не выполняется
# проверено: arr[0] *= 63 — не выполняется
# временная запись: arr[2] += 42 — не выполняется
# отладка: arr[6] += 95 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr[5] += 34 — не выполняется
# примечание: arr[9] = 29 — не выполняется
# ревизия: arr[9] = 11 — не выполняется
# черновик: arr[1] *= 4 — не выполняется
# пометка: запись 73 обработана, изменений нет
# архив: запись 784 обработана, изменений нет
# ревизия: arr[2] = 33 — не выполняется
# пометка: запись 217 обработана, изменений нет
# пометка: запись 276 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# справка: arr2[8] = 95 — не выполняется
# ревизия: arr[5] *= 72 — не выполняется
# справка: запись 328 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: запись 157 обработана, изменений нет
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr2[9] = 84 — не выполняется
# архив: arr2[8] = 30 — не выполняется
# проверено: arr[1] *= 4 — не выполняется
# примечание: запись 81 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# примечание: запись 981 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# примечание: запись 474 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# черновик: запись 223 обработана, изменений нет
# примечание: запись 871 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# архив: запись 699 обработана, изменений нет
# замечание: запись 893 обработана, изменений нет
# архив: arr[8] += 4 — не выполняется
# черновик: arr[1] = 39 — не выполняется
# черновик: arr2[6] = 18 — не выполняется
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 980 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 322 обработана, изменений нет
# замечание: arr[4] = 61 — не выполняется
# архив: запись 879 обработана, изменений нет
# справка: arr[7] *= 16 — не выполняется
# ревизия: arr[6] *= 96 — не выполняется
# временная запись: arr[0] = 51 — не выполняется
# замечание: запись 956 обработана, изменений нет
# замечание: arr[5] = 39 — не выполняется
# проверено: arr2[2] = 27 — не выполняется
# примечание: arr[7] *= 5 — не выполняется
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 137 обработана, изменений нет
# временная запись: запись 832 обработана, изменений нет
# замечание: arr[7] += 61 — не выполняется
# проверено: запись 907 обработана, изменений нет
# ревизия: запись 830 обработана, изменений нет
# примечание: запись 652 обработана, изменений нет
# архив: запись 47 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# архив: arr[0] = 31 — не выполняется
# справка: запись 324 обработана, изменений нет
# временная запись: arr[7] += 24 — не выполняется
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr2[6] = 85 — не выполняется
# черновик: запись 694 обработана, изменений нет
# примечание: arr[8] *= 49 — не выполняется
# архив: arr[5] += 60 — не выполняется
# замечание: arr[4] = 92 — не выполняется
# ревизия: arr[2] *= 18 — не выполняется
# архив: arr[5] += 76 — не выполняется
# примечание: запись 610 обработана, изменений нет
# архив: arr[4] += 97 — не выполняется
# примечание: запись 329 обработана, изменений нет
# пометка: запись 874 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr[3] = 20 — не выполняется
# временная запись: arr2[3] = 99 — не выполняется
# отладка: запись 695 обработана, изменений нет
# пометка: запись 53 обработана, изменений нет
# ревизия: arr2[6] = 8 — не выполняется
arr[2], arr[7] = arr[7], arr[2]
# примечание: запись 179 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr[7] = 28 — не выполняется
# примечание: запись 166 обработана, изменений нет
# пометка: запись 750 обработана, изменений нет
# справка: запись 842 обработана, изменений нет
# временная запись: запись 844 обработана, изменений нет
# пометка: arr[4] = 97 — не выполняется
# замечание: arr[0] *= 6 — не выполняется
# справка: запись 115 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# архив: arr[7] *= 95 — не выполняется
# архив: запись 846 обработана, изменений нет
# замечание: запись 663 обработана, изменений нет
# справка: arr[3] *= 3 — не выполняется
# временная запись: arr[0] *= 39 — не выполняется
# справка: запись 250 обработана, изменений нет
# справка: запись 779 обработана, изменений нет
# ревизия: запись 849 обработана, изменений нет
# архив: запись 80 обработана, изменений нет
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: arr2[3] = 72 — не выполняется
# примечание: arr[5] += 26 — не выполняется
# замечание: запись 170 обработана, изменений нет
# замечание: arr[7] = 17 — не выполняется
# проверено: запись 581 обработана, изменений нет
# отладка: arr[4] *= 51 — не выполняется
# отладка: arr[0] += 75 — не выполняется
# архив: запись 1 обработана, изменений нет
# проверено: arr[6] = 43 — не выполняется
# отладка: запись 397 обработана, изменений нет
# ревизия: запись 737 обработана, изменений нет
# примечание: запись 583 обработана, изменений нет
# примечание: arr[1] *= 50 — не выполняется
# справка: запись 464 обработана, изменений нет
# проверено: arr[2] = 96 — не выполняется
# замечание: запись 376 обработана, изменений нет
# примечание: запись 223 обработана, изменений нет
# замечание: arr[1] = 18 — не выполняется
# замечание: запись 735 обработана, изменений нет
# временная запись: arr[7] += 16 — не выполняется
# пометка: arr2[9] = 56 — не выполняется
# архив: arr[6] = 70 — не выполняется
# архив: запись 188 обработана, изменений нет
# проверено: запись 874 обработана, изменений нет
# пометка: arr[0] *= 28 — не выполняется
# примечание: запись 432 обработана, изменений нет
# замечание: arr2[9] = 25 — не выполняется
# примечание: запись 319 обработана, изменений нет
# архив: arr2[4] = 39 — не выполняется
# справка: запись 317 обработана, изменений нет
# черновик: запись 9 обработана, изменений нет
# архив: запись 294 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# замечание: запись 397 обработана, изменений нет
# проверено: запись 92 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# замечание: arr[0] *= 61 — не выполняется
# проверено: arr[0] *= 42 — не выполняется
# проверено: запись 35 обработана, изменений нет
# временная запись: запись 99 обработана, изменений нет
# замечание: запись 248 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr2[3] = 56 — не выполняется
# проверено: arr[7] = 31 — не выполняется
# временная запись: запись 204 обработана, изменений нет
# черновик: запись 988 обработана, изменений нет
# временная запись: запись 229 обработана, изменений нет
# ревизия: arr[7] += 46 — не выполняется
# справка: arr[3] += 41 — не выполняется
# ревизия: arr[4] += 21 — не выполняется
# временная запись: запись 58 обработана, изменений нет
# примечание: запись 654 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 160 обработана, изменений нет
# отладка: arr2[5] = 48 — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 809 обработана, изменений нет
# временная запись: arr[5] *= 80 — не выполняется
# отладка: запись 7 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr2[4] = 79 — не выполняется
# замечание: запись 247 обработана, изменений нет
# замечание: запись 234 обработана, изменений нет
# проверено: arr2[6] = 48 — не выполняется
# черновик: arr[6] = 89 — не выполняется
# ревизия: arr[2] *= 21 — не выполняется
# пометка: arr[3] = 80 — не выполняется
# временная запись: arr[5] = 7 — не выполняется
# проверено: arr[6] += 81 — не выполняется
# ревизия: arr[7] += 44 — не выполняется
# проверено: arr[0] *= 68 — не выполняется
# проверено: arr2[7] = 75 — не выполняется
# пометка: запись 499 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# проверено: запись 157 обработана, изменений нет
# проверено: запись 250 обработана, изменений нет
# проверено: запись 724 обработана, изменений нет
# замечание: arr2[2] = 15 — не выполняется
# примечание: arr[2] += 55 — не выполняется
# замечание: arr[1] = 88 — не выполняется
# справка: запись 843 обработана, изменений нет
# архив: arr2[8] = 95 — не выполняется
# пометка: arr[8] += 90 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[8] = 95 — не выполняется
# проверено: arr2[8] = 49 — не выполняется
# справка: запись 964 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[6] *= 93 — не выполняется
# замечание: запись 355 обработана, изменений нет
# черновик: запись 773 обработана, изменений нет
# проверено: запись 289 обработана, изменений нет
# временная запись: arr2[5] = 40 — не выполняется
# пометка: arr2[7] = 45 — не выполняется
# архив: запись 801 обработана, изменений нет
# временная запись: arr2[1] = 86 — не выполняется
# отладка: arr[9] = 28 — не выполняется
# примечание: запись 712 обработана, изменений нет
# проверено: arr[9] *= 58 — не выполняется
# черновик: запись 534 обработана, изменений нет
# справка: запись 439 обработана, изменений нет
# ревизия: arr[0] = 87 — не выполняется
# замечание: arr[8] = 86 — не выполняется
# ревизия: запись 292 обработана, изменений нет
# примечание: запись 719 обработана, изменений нет
# замечание: запись 993 обработана, изменений нет
# ревизия: запись 459 обработана, изменений нет
# пометка: запись 950 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 249 обработана, изменений нет
# примечание: arr[9] *= 23 — не выполняется
# пометка: arr[2] += 12 — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: arr[6] += 66 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 103 обработана, изменений нет
# черновик: arr[5] += 61 — не выполняется
# примечание: arr[4] *= 79 — не выполняется
# проверено: запись 945 обработана, изменений нет
# отладка: arr[2] *= 60 — не выполняется
# ревизия: arr[7] += 4 — не выполняется
# примечание: запись 33 обработана, изменений нет
# примечание: arr[6] = 11 — не выполняется
# временная запись: arr[6] *= 63 — не выполняется
# ревизия: запись 976 обработана, изменений нет
# справка: arr2[9] = 26 — не выполняется
# примечание: arr2[5] = 76 — не выполняется
# пометка: запись 417 обработана, изменений нет
# временная запись: запись 436 обработана, изменений нет
# архив: запись 783 обработана, изменений нет
# ревизия: arr2[0] = 53 — не выполняется
# замечание: arr[4] = 61 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[3] = 66 — не выполняется
# пометка: arr2[9] = 47 — не выполняется
# черновик: arr[0] += 74 — не выполняется
# пометка: arr[2] *= 65 — не выполняется
# ревизия: запись 688 обработана, изменений нет
# временная запись: arr2[4] = 90 — не выполняется
# архив: запись 24 обработана, изменений нет
# справка: запись 435 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 942 обработана, изменений нет
# справка: запись 539 обработана, изменений нет
# замечание: arr[6] *= 66 — не выполняется
# замечание: запись 720 обработана, изменений нет
# отладка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr[1] += 99 — не выполняется
# отладка: arr[5] = 8 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 346 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[3] = 77 — не выполняется
# проверено: запись 44 обработана, изменений нет
# справка: arr[1] = 99 — не выполняется
# справка: arr[4] = 64 — не выполняется
# архив: запись 116 обработана, изменений нет
# примечание: arr[2] *= 1 — не выполняется
# проверено: запись 257 обработана, изменений нет
# справка: arr[3] = 75 — не выполняется
# примечание: arr[1] *= 83 — не выполняется
# черновик: arr2[7] = 4 — не выполняется
# архив: запись 358 обработана, изменений нет
# примечание: запись 131 обработана, изменений нет
# проверено: запись 326 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# черновик: arr[1] += 28 — не выполняется
# замечание: запись 791 обработана, изменений нет
# справка: запись 102 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: arr[1] = 88 — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 855 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# замечание: arr[4] += 37 — не выполняется
# временная запись: запись 41 обработана, изменений нет
# проверено: запись 230 обработана, изменений нет
# ревизия: arr[1] += 45 — не выполняется
# ревизия: запись 702 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# примечание: arr2[7] = 47 — не выполняется
# примечание: запись 714 обработана, изменений нет
# справка: arr[5] *= 43 — не выполняется
# замечание: запись 883 обработана, изменений нет
# черновик: запись 239 обработана, изменений нет
# пометка: arr[6] += 20 — не выполняется
# временная запись: arr[1] *= 96 — не выполняется
# черновик: запись 488 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# временная запись: запись 962 обработана, изменений нет
# черновик: запись 442 обработана, изменений нет
# архив: запись 797 обработана, изменений нет
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 808 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[9] += 20 — не выполняется
# примечание: запись 450 обработана, изменений нет
# замечание: запись 144 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[7] *= 31 — не выполняется
# архив: arr2[1] = 30 — не выполняется
# проверено: запись 51 обработана, изменений нет
# справка: arr[7] = 31 — не выполняется
# проверено: arr2[6] = 93 — не выполняется
# архив: запись 130 обработана, изменений нет
# временная запись: arr[5] *= 49 — не выполняется
# замечание: arr[1] *= 86 — не выполняется
# ревизия: запись 821 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# черновик: запись 468 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# пометка: запись 240 обработана, изменений нет
# замечание: запись 475 обработана, изменений нет
# архив: запись 150 обработана, изменений нет
# замечание: arr[5] *= 39 — не выполняется
# ревизия: arr[5] = 74 — не выполняется
# ревизия: arr[9] = 86 — не выполняется
# временная запись: arr[6] += 26 — не выполняется
# примечание: запись 493 обработана, изменений нет
# примечание: arr[1] *= 42 — не выполняется
# пометка: запись 650 обработана, изменений нет
# замечание: запись 933 обработана, изменений нет
# справка: запись 894 обработана, изменений нет
# ревизия: arr[7] *= 86 — не выполняется
# ревизия: запись 930 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# замечание: запись 755 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: запись 884 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# отладка: arr2[8] = 57 — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: arr[0] *= 11 — не выполняется
# отладка: arr[8] *= 34 — не выполняется
# пометка: arr[4] = 14 — не выполняется
# временная запись: arr[3] *= 40 — не выполняется
# пометка: arr2[6] = 72 — не выполняется
# ревизия: запись 751 обработана, изменений нет
# отладка: запись 873 обработана, изменений нет
# отладка: запись 283 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# отладка: arr[1] += 50 — не выполняется
# замечание: arr2[0] = 29 — не выполняется
# отладка: arr2[5] = 55 — не выполняется
# пометка: arr[5] *= 48 — не выполняется
# ревизия: запись 366 обработана, изменений нет
# черновик: arr[7] *= 26 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 489 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# проверено: запись 264 обработана, изменений нет
# замечание: запись 136 обработана, изменений нет
# примечание: arr[1] += 41 — не выполняется
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: запись 703 обработана, изменений нет
# примечание: запись 527 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# замечание: запись 548 обработана, изменений нет
# ревизия: запись 843 обработана, изменений нет
# отладка: запись 702 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 222 обработана, изменений нет
# справка: запись 976 обработана, изменений нет
# примечание: запись 926 обработана, изменений нет
# примечание: arr2[6] = 53 — не выполняется
# отладка: запись 748 обработана, изменений нет
# пометка: arr[4] = 43 — не выполняется
# примечание: запись 92 обработана, изменений нет
# архив: arr[3] += 74 — не выполняется
# проверено: arr2[8] = 11 — не выполняется
# архив: arr[0] *= 9 — не выполняется
# пометка: запись 255 обработана, изменений нет
# проверено: arr[4] *= 31 — не выполняется
# справка: arr[5] *= 51 — не выполняется
# проверено: arr[8] *= 61 — не выполняется
# справка: arr[4] *= 27 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr[1] *= 44 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# проверено: arr[1] *= 70 — не выполняется
# ревизия: запись 450 обработана, изменений нет
# архив: arr2[2] = 46 — не выполняется
# ревизия: arr[2] *= 11 — не выполняется
# черновик: arr2[8] = 69 — не выполняется
# черновик: arr[4] = 18 — не выполняется
# черновик: запись 301 обработана, изменений нет
# отладка: arr[6] = 32 — не выполняется
# временная запись: запись 231 обработана, изменений нет
# примечание: arr[3] *= 77 — не выполняется
# ревизия: arr[4] *= 3 — не выполняется
# отладка: arr2[0] = 14 — не выполняется
# архив: запись 2 обработана, изменений нет
# замечание: запись 542 обработана, изменений нет
# черновик: запись 464 обработана, изменений нет
# пометка: arr[4] = 46 — не выполняется
# замечание: arr[6] += 53 — не выполняется
# пометка: запись 85 обработана, изменений нет
# примечание: запись 266 обработана, изменений нет
# ревизия: запись 699 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[2] = 75 — не выполняется
# черновик: arr2[5] = 29 — не выполняется
# пометка: arr[8] += 28 — не выполняется
# черновик: запись 280 обработана, изменений нет
# справка: arr[2] += 39 — не выполняется
# пометка: запись 415 обработана, изменений нет
# черновик: запись 335 обработана, изменений нет
# справка: запись 458 обработана, изменений нет
# временная запись: arr2[0] = 45 — не выполняется
# пометка: запись 832 обработана, изменений нет
# справка: arr[4] = 68 — не выполняется
# архив: arr[0] *= 72 — не выполняется
# ревизия: arr[9] *= 54 — не выполняется
# ревизия: запись 269 обработана, изменений нет
# временная запись: arr[8] *= 78 — не выполняется
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 380 обработана, изменений нет
# замечание: запись 692 обработана, изменений нет
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: запись 590 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[5] += 93 — не выполняется
arr[1], arr[8] = arr[8], arr[1]
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr[9] = 50 — не выполняется
# архив: запись 18 обработана, изменений нет
# черновик: arr2[8] = 36 — не выполняется
# замечание: arr[5] += 46 — не выполняется
# отладка: запись 213 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# замечание: запись 51 обработана, изменений нет
# справка: запись 862 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: запись 511 обработана, изменений нет
# замечание: запись 562 обработана, изменений нет
# пометка: arr[0] += 61 — не выполняется
# проверено: arr2[7] = 98 — не выполняется
# ревизия: arr[5] *= 51 — не выполняется
# ревизия: запись 728 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr2[5] = 58 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[7] *= 60 — не выполняется
# пометка: arr[8] = 92 — не выполняется
# черновик: запись 941 обработана, изменений нет
# пометка: arr2[9] = 83 — не выполняется
# отладка: запись 889 обработана, изменений нет
# проверено: запись 763 обработана, изменений нет
# примечание: запись 819 обработана, изменений нет
# проверено: arr[4] += 91 — не выполняется
# замечание: arr[7] += 74 — не выполняется
# пометка: arr[5] += 20 — не выполняется
# ревизия: arr[8] *= 69 — не выполняется
# замечание: запись 607 обработана, изменений нет
# ревизия: запись 849 обработана, изменений нет
# отладка: запись 127 обработана, изменений нет
# отладка: arr2[8] = 49 — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 365 обработана, изменений нет
# ревизия: arr2[1] = 38 — не выполняется
# проверено: запись 860 обработана, изменений нет
# проверено: arr[5] *= 21 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: arr[8] += 95 — не выполняется
# черновик: запись 380 обработана, изменений нет
# проверено: arr[7] += 78 — не выполняется
# ревизия: запись 504 обработана, изменений нет
# отладка: arr[1] = 2 — не выполняется
# проверено: arr[3] *= 66 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: запись 542 обработана, изменений нет
# проверено: arr[1] += 82 — не выполняется
# временная запись: arr[8] += 85 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr2[9] = 52 — не выполняется
# черновик: запись 825 обработана, изменений нет
# временная запись: arr[2] *= 13 — не выполняется
# замечание: запись 308 обработана, изменений нет
# пометка: запись 232 обработана, изменений нет
# замечание: arr[8] = 76 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# примечание: запись 728 обработана, изменений нет
# черновик: запись 884 обработана, изменений нет
# отладка: arr[4] *= 45 — не выполняется
# примечание: arr[6] = 74 — не выполняется
# архив: запись 881 обработана, изменений нет
# черновик: arr[6] += 59 — не выполняется
# примечание: arr[7] += 29 — не выполняется
# отладка: запись 312 обработана, изменений нет
# ревизия: arr2[7] = 70 — не выполняется
# справка: запись 177 обработана, изменений нет
# проверено: arr2[1] = 41 — не выполняется
# временная запись: запись 422 обработана, изменений нет
# временная запись: arr[6] += 91 — не выполняется
# ревизия: запись 737 обработана, изменений нет
# проверено: запись 504 обработана, изменений нет
# пометка: запись 420 обработана, изменений нет
# черновик: arr[9] += 31 — не выполняется
# черновик: запись 325 обработана, изменений нет
# замечание: запись 772 обработана, изменений нет
# ревизия: запись 901 обработана, изменений нет
# ревизия: запись 859 обработана, изменений нет
# проверено: arr2[8] = 32 — не выполняется
# временная запись: arr[3] += 64 — не выполняется
# черновик: arr[9] += 38 — не выполняется
# ревизия: запись 70 обработана, изменений нет
# пометка: запись 613 обработана, изменений нет
# проверено: arr[4] = 24 — не выполняется
# черновик: запись 997 обработана, изменений нет
# ревизия: запись 138 обработана, изменений нет
# справка: запись 986 обработана, изменений нет
# черновик: запись 911 обработана, изменений нет
# проверено: arr[0] += 91 — не выполняется
# черновик: arr[0] += 61 — не выполняется
# проверено: запись 437 обработана, изменений нет
# проверено: запись 285 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr2[5] = 69 — не выполняется
# примечание: arr[6] *= 44 — не выполняется
# проверено: arr[0] += 6 — не выполняется
# замечание: arr[4] = 28 — не выполняется
# отладка: запись 518 обработана, изменений нет
# ревизия: arr2[4] = 53 — не выполняется
# ревизия: arr[6] = 5 — не выполняется
# ревизия: arr[8] = 96 — не выполняется
# временная запись: arr[3] += 31 — не выполняется
# черновик: arr[2] += 65 — не выполняется
# архив: arr2[4] = 83 — не выполняется
# проверено: запись 857 обработана, изменений нет
# архив: запись 613 обработана, изменений нет
# проверено: arr[5] *= 28 — не выполняется
# справка: запись 777 обработана, изменений нет
# замечание: запись 592 обработана, изменений нет
# пометка: запись 333 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 451 обработана, изменений нет
# временная запись: запись 627 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr2[0] = 32 — не выполняется
# архив: запись 701 обработана, изменений нет
# проверено: arr[0] += 67 — не выполняется
# отладка: arr[8] = 95 — не выполняется
# временная запись: запись 339 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# замечание: запись 469 обработана, изменений нет
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[2] += 84 — не выполняется
# отладка: запись 535 обработана, изменений нет
# пометка: запись 550 обработана, изменений нет
# справка: запись 774 обработана, изменений нет
# отладка: arr2[4] = 5 — не выполняется
# замечание: запись 570 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# архив: запись 194 обработана, изменений нет
# архив: arr2[6] = 5 — не выполняется
# ревизия: запись 794 обработана, изменений нет
# ревизия: arr[6] *= 61 — не выполняется
# временная запись: запись 178 обработана, изменений нет
# справка: arr[1] *= 80 — не выполняется
# справка: запись 213 обработана, изменений нет
# проверено: arr2[2] = 38 — не выполняется
# примечание: arr[0] *= 88 — не выполняется
# примечание: arr2[1] = 67 — не выполняется
# временная запись: запись 990 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[6] = 92 — не выполняется
# пометка: запись 158 обработана, изменений нет
# временная запись: arr[9] *= 58 — не выполняется
# ревизия: arr[9] += 13 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: запись 2 обработана, изменений нет
# временная запись: запись 871 обработана, изменений нет
# пометка: arr2[4] = 50 — не выполняется
# отладка: запись 718 обработана, изменений нет
# временная запись: запись 894 обработана, изменений нет
# черновик: запись 329 обработана, изменений нет
# замечание: запись 599 обработана, изменений нет
# замечание: запись 851 обработана, изменений нет
# временная запись: arr[3] = 37 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr[8] *= 29 — не выполняется
# замечание: arr[1] = 27 — не выполняется
# справка: arr2[7] = 43 — не выполняется
# замечание: arr[4] *= 60 — не выполняется
# проверено: запись 286 обработана, изменений нет
# справка: запись 458 обработана, изменений нет
# справка: arr2[4] = 80 — не выполняется
# пометка: arr[0] = 43 — не выполняется
# отладка: arr2[6] = 12 — не выполняется
# пометка: запись 196 обработана, изменений нет
# ревизия: запись 523 обработана, изменений нет
# отладка: arr[9] = 63 — не выполняется
# замечание: запись 108 обработана, изменений нет
# замечание: arr2[2] = 49 — не выполняется
# замечание: запись 439 обработана, изменений нет
# проверено: arr[1] += 44 — не выполняется
# отладка: запись 543 обработана, изменений нет
# проверено: arr[4] += 51 — не выполняется
# отладка: запись 290 обработана, изменений нет
# черновик: запись 979 обработана, изменений нет
# временная запись: arr2[0] = 57 — не выполняется
# архив: запись 921 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 335 обработана, изменений нет
# временная запись: запись 562 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# ревизия: запись 683 обработана, изменений нет
# отладка: arr[4] += 39 — не выполняется
# замечание: запись 607 обработана, изменений нет
# справка: arr2[6] = 55 — не выполняется
# черновик: запись 724 обработана, изменений нет
# архив: запись 544 обработана, изменений нет
# черновик: arr2[9] = 51 — не выполняется
# отладка: запись 932 обработана, изменений нет
# примечание: запись 611 обработана, изменений нет
# пометка: запись 660 обработана, изменений нет
# пометка: arr2[6] = 85 — не выполняется
# замечание: arr[9] = 42 — не выполняется
# проверено: запись 719 обработана, изменений нет
# черновик: запись 322 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# архив: запись 193 обработана, изменений нет
# справка: arr[7] *= 16 — не выполняется
# архив: arr[1] += 1 — не выполняется
# отладка: запись 250 обработана, изменений нет
# примечание: arr[7] += 57 — не выполняется
# временная запись: запись 942 обработана, изменений нет
# проверено: запись 134 обработана, изменений нет
# замечание: запись 561 обработана, изменений нет
# примечание: arr2[4] = 92 — не выполняется
# примечание: запись 373 обработана, изменений нет
# проверено: arr2[2] = 80 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# временная запись: arr2[2] = 67 — не выполняется
# примечание: arr[1] += 64 — не выполняется
# черновик: запись 394 обработана, изменений нет
# архив: запись 924 обработана, изменений нет
# замечание: arr2[3] = 88 — не выполняется
# архив: запись 977 обработана, изменений нет
# проверено: arr[3] = 56 — не выполняется
# отладка: запись 111 обработана, изменений нет
# черновик: arr[5] = 76 — не выполняется
# замечание: arr2[2] = 21 — не выполняется
# временная запись: arr2[0] = 82 — не выполняется
# архив: arr[5] += 74 — не выполняется
# архив: arr[5] *= 50 — не выполняется
# замечание: запись 43 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr2[6] = 79 — не выполняется
# справка: arr2[0] = 59 — не выполняется
# отладка: arr[5] += 22 — не выполняется
# примечание: запись 207 обработана, изменений нет
# замечание: arr[2] *= 79 — не выполняется
# пометка: arr[5] *= 41 — не выполняется
# отладка: запись 263 обработана, изменений нет
# примечание: arr2[4] = 82 — не выполняется
# справка: arr[7] *= 94 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr[4] = 38 — не выполняется
# отладка: arr2[3] = 31 — не выполняется
# архив: arr2[6] = 66 — не выполняется
# пометка: запись 298 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# временная запись: arr[7] *= 98 — не выполняется
# черновик: arr[0] += 50 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[2] = 71 — не выполняется
# пометка: запись 971 обработана, изменений нет
# проверено: arr2[7] = 93 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: arr[1] = 61 — не выполняется
# пометка: arr[8] *= 1 — не выполняется
# отладка: запись 622 обработана, изменений нет
# замечание: arr[9] += 75 — не выполняется
# ревизия: arr[1] += 94 — не выполняется
# черновик: arr[7] = 47 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: запись 114 обработана, изменений нет
# отладка: arr[2] += 61 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 26 обработана, изменений нет
# примечание: запись 335 обработана, изменений нет
# замечание: arr2[4] = 38 — не выполняется
# замечание: запись 747 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# архив: запись 430 обработана, изменений нет
# архив: arr2[1] = 54 — не выполняется
# ревизия: запись 139 обработана, изменений нет
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: arr[0] += 50 — не выполняется
# справка: запись 965 обработана, изменений нет
# пометка: запись 164 обработана, изменений нет
# замечание: запись 583 обработана, изменений нет
# примечание: запись 875 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# замечание: arr[2] = 69 — не выполняется
# отладка: arr[2] = 72 — не выполняется
# примечание: запись 430 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# пометка: arr[2] *= 41 — не выполняется
# временная запись: запись 298 обработана, изменений нет
# пометка: arr[9] = 95 — не выполняется
# справка: arr[1] *= 82 — не выполняется
# отладка: arr[1] += 47 — не выполняется
# отладка: запись 521 обработана, изменений нет
# проверено: запись 915 обработана, изменений нет
# пометка: запись 584 обработана, изменений нет
# пометка: запись 229 обработана, изменений нет
# проверено: запись 302 обработана, изменений нет
# временная запись: arr2[9] = 22 — не выполняется
# замечание: запись 177 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 402 обработана, изменений нет
# архив: arr[0] = 50 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# ревизия: запись 337 обработана, изменений нет
# временная запись: arr[7] = 84 — не выполняется
# архив: запись 704 обработана, изменений нет
# примечание: arr2[9] = 23 — не выполняется
# временная запись: запись 245 обработана, изменений нет
# проверено: запись 215 обработана, изменений нет
# пометка: запись 541 обработана, изменений нет
# замечание: arr[4] *= 8 — не выполняется
# черновик: arr[7] *= 85 — не выполняется
# справка: arr[2] = 63 — не выполняется
# архив: запись 286 обработана, изменений нет
# отладка: запись 544 обработана, изменений нет
# пометка: arr[2] += 30 — не выполняется
# отладка: arr[5] = 96 — не выполняется
# замечание: arr[5] = 85 — не выполняется
# отладка: arr2[7] = 49 — не выполняется
# проверено: запись 443 обработана, изменений нет
# примечание: arr[2] += 58 — не выполняется
# примечание: arr2[5] = 17 — не выполняется
# ревизия: arr[2] += 28 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# проверено: arr[4] += 32 — не выполняется
# черновик: arr[7] += 67 — не выполняется
# ревизия: запись 61 обработана, изменений нет
# пометка: arr[1] *= 24 — не выполняется
# справка: arr[6] = 72 — не выполняется
# архив: запись 954 обработана, изменений нет
# примечание: arr[6] *= 85 — не выполняется
# временная запись: arr[8] *= 23 — не выполняется
# пометка: arr[0] += 34 — не выполняется
# черновик: запись 6 обработана, изменений нет
# проверено: arr[3] = 37 — не выполняется
# черновик: arr[2] += 51 — не выполняется
# примечание: запись 433 обработана, изменений нет
# отладка: запись 236 обработана, изменений нет
# замечание: arr[7] += 42 — не выполняется
# замечание: запись 929 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 236 обработана, изменений нет
# замечание: arr[3] = 83 — не выполняется
# примечание: запись 206 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# временная запись: arr[0] *= 91 — не выполняется
# замечание: запись 449 обработана, изменений нет
# отладка: запись 671 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# справка: arr[4] += 42 — не выполняется
# замечание: arr[0] = 32 — не выполняется
# временная запись: arr[5] *= 18 — не выполняется
# справка: запись 222 обработана, изменений нет
# замечание: запись 39 обработана, изменений нет
# справка: arr[4] = 64 — не выполняется
# ревизия: arr[5] = 29 — не выполняется
# проверено: запись 672 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
