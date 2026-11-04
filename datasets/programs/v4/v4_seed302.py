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
arr2[3] = 50
arr2[5] = 43
arr[0], arr[3] = arr[3], arr[0]
arr[8] += 44
arr[1], arr[5] = arr[5], arr[1]
arr2[7] = 35
arr2[6] = 47
arr[1] += 49
"""

TRAP_0 = "arr[4] = 300"
TRAP_1 = "arr[6] = 396"
TRAP_2 = "arr[3] = 963"
TRAP_3 = "arr[4] = 659"
TRAP_4 = "arr[6] = 745"
TRAP_5 = "arr[3] = 240"
TRAP_6 = "arr[0] = 353"
TRAP_7 = "arr[0] = 111"
TRAP_8 = "arr[7] = 511"
TRAP_9 = "arr[1] = 632"
TRAP_10 = "arr[7] = 267"
TRAP_11 = "arr[4] = 161"
TRAP_12 = "arr[7] = 328"
TRAP_13 = "arr[9] = 981"
TRAP_14 = "arr[2] = 893"
TRAP_15 = "arr[3] = 367"
TRAP_16 = "arr[1] = 295"
TRAP_17 = "arr[9] = 661"
TRAP_18 = "arr[2] = 595"
TRAP_19 = "arr[8] = 265"
TRAP_20 = "arr[4] = 141"
TRAP_21 = "arr[0] = 769"
TRAP_22 = "arr[7] = 141"
TRAP_23 = "arr[5] = 984"
TRAP_24 = "arr[6] = 406"
TRAP_25 = "arr[2] = 431"
TRAP_26 = "arr[9] = 826"
TRAP_27 = "arr[4] = 505"
TRAP_28 = "arr[7] = 166"
TRAP_29 = "arr[2] = 380"
TRAP_30 = "arr[6] = 419"
TRAP_31 = "arr[7] = 815"
TRAP_32 = "arr[2] = 566"
TRAP_33 = "arr[3] = 556"
TRAP_34 = "arr[5] = 658"
TRAP_35 = "arr[3] = 992"
TRAP_36 = "arr[5] = 671"
TRAP_37 = "arr[2] = 583"
TRAP_38 = "arr[0] = 790"
TRAP_39 = "arr[9] = 811"
TRAP_40 = "arr[6] = 349"
TRAP_41 = "arr[9] = 987"
TRAP_42 = "arr[8] = 886"
TRAP_43 = "arr[5] = 964"
TRAP_44 = "arr[7] = 335"
TRAP_45 = "arr[4] = 484"
TRAP_46 = "arr[0] = 579"
TRAP_47 = "arr[1] = 804"
TRAP_48 = "arr[6] = 225"
TRAP_49 = "arr[1] = 916"
TRAP_50 = "arr[0] = 157"
TRAP_51 = "arr[9] = 540"
TRAP_52 = "arr[8] = 925"
TRAP_53 = "arr[4] = 660"
TRAP_54 = "arr[1] = 113"
TRAP_55 = "arr[3] = 540"
TRAP_56 = "arr[8] = 852"
TRAP_57 = "arr[7] = 674"
TRAP_58 = "arr[9] = 302"
TRAP_59 = "arr[5] = 921"
TRAP_60 = "arr[8] = 238"
TRAP_61 = "arr[5] = 807"
TRAP_62 = "arr[7] = 604"
TRAP_63 = "arr[1] = 288"
TRAP_64 = "arr[4] = 599"
TRAP_65 = "arr[9] = 867"
TRAP_66 = "arr[4] = 420"
TRAP_67 = "arr[9] = 149"
TRAP_68 = "arr[5] = 167"
TRAP_69 = "arr[0] = 502"
TRAP_70 = "arr[0] = 408"
TRAP_71 = "arr[5] = 570"
TRAP_72 = "arr[0] = 820"
TRAP_73 = "arr[2] = 699"
TRAP_74 = "arr[4] = 512"
TRAP_75 = "arr[2] = 996"
TRAP_76 = "arr[6] = 843"
TRAP_77 = "arr[1] = 773"
TRAP_78 = "arr[2] = 851"
TRAP_79 = "arr[8] = 851"
TRAP_80 = "arr[7] = 762"
TRAP_81 = "arr[5] = 511"
TRAP_82 = "arr[2] = 903"
TRAP_83 = "arr[6] = 590"
TRAP_84 = "arr[8] = 367"
TRAP_85 = "arr[3] = 345"
TRAP_86 = "arr[8] = 539"
TRAP_87 = "arr[5] = 239"
TRAP_88 = "arr[4] = 453"
TRAP_89 = "arr[1] = 444"
TRAP_90 = "arr[6] = 501"
TRAP_91 = "arr[4] = 955"
TRAP_92 = "arr[7] = 169"
TRAP_93 = "arr[4] = 444"
TRAP_94 = "arr[8] = 697"
TRAP_95 = "arr[3] = 200"
TRAP_96 = "arr[3] = 360"
TRAP_97 = "arr[4] = 795"
TRAP_98 = "arr[1] = 143"
TRAP_99 = "arr[5] = 220"
TRAP_100 = "arr[1] = 517"
TRAP_101 = "arr[3] = 940"
TRAP_102 = "arr[6] = 324"
TRAP_103 = "arr[6] = 907"
TRAP_104 = "arr[2] = 163"
TRAP_105 = "arr[5] = 808"
TRAP_106 = "arr[2] = 740"
TRAP_107 = "arr[1] = 616"
TRAP_108 = "arr[9] = 199"
TRAP_109 = "arr[8] = 391"
TRAP_110 = "arr[1] = 910"
TRAP_111 = "arr[4] = 903"
TRAP_112 = "arr[2] = 442"
TRAP_113 = "arr[4] = 107"
TRAP_114 = "arr[8] = 594"
TRAP_115 = "arr[9] = 398"
TRAP_116 = "arr[9] = 428"
TRAP_117 = "arr[2] = 597"
TRAP_118 = "arr[2] = 822"
TRAP_119 = "arr[4] = 190"
TRAP_120 = "arr[1] = 776"
TRAP_121 = "arr[6] = 301"
TRAP_122 = "arr[5] = 418"
TRAP_123 = "arr[7] = 464"
TRAP_124 = "arr[9] = 739"
TRAP_125 = "arr[7] = 711"
TRAP_126 = "arr[9] = 661"
TRAP_127 = "arr[9] = 413"
TRAP_128 = "arr[0] = 418"
TRAP_129 = "arr[3] = 798"
TRAP_130 = "arr[9] = 928"
TRAP_131 = "arr[3] = 809"
TRAP_132 = "arr[3] = 764"
TRAP_133 = "arr[2] = 551"
TRAP_134 = "arr[5] = 888"
TRAP_135 = "arr[4] = 277"
TRAP_136 = "arr[2] = 769"
TRAP_137 = "arr[8] = 174"
TRAP_138 = "arr[4] = 172"
TRAP_139 = "arr[5] = 384"
TRAP_140 = "arr[7] = 827"
TRAP_141 = "arr[3] = 498"
TRAP_142 = "arr[5] = 900"
TRAP_143 = "arr[2] = 626"
TRAP_144 = "arr[6] = 687"
TRAP_145 = "arr[0] = 738"
TRAP_146 = "arr[4] = 555"
TRAP_147 = "arr[5] = 680"
TRAP_148 = "arr[6] = 722"
TRAP_149 = "arr[8] = 824"

arr = [18, 18, 28, 18, 14, 16, 7, 27, 2, 13]

tmp_0 = arr[8] + 48
code_1 = re.sub(r'[0-9]', '#', str(arr[2]))
code_2 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_3 = arr[2]
code_4 = re.sub(r'[0-9]', '#', str(arr[2]))
code_5 = re.sub(r'[0-9]', '#', str(arr[9]))
label_6 = "запись 6 не применялась"
label_7 = "запись 7 не применялась"
copy_8 = arr[8]
copy_9 = arr[2]
code_10 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_11 = arr[6] + 37
note_12 = str(arr[7]) + str(arr[5])
code_13 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_14 = arr[7] + 26
code_15 = re.sub(r'[0-9]', '#', str(arr[4]))
note_16 = str(arr[8]) + str(arr[7])
tmp_17 = arr[4] + 9
tmp_18 = arr[5] + 20
code_19 = re.sub(r'[0-9]', '#', str(arr[7]))
label_20 = "запись 20 не применялась"
note_21 = str(arr[4]) + str(arr[5])
label_22 = "запись 22 не применялась"
code_23 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_24 = arr[9]
copy_25 = arr[8]
note_26 = str(arr[2]) + str(arr[5])
code_27 = re.sub(r'[0-9]', '#', str(arr[2]))
label_28 = "запись 28 не применялась"
code_29 = re.sub(r'[0-9]', '#', str(arr[8]))
note_30 = str(arr[3]) + str(arr[4])
note_31 = str(arr[0]) + str(arr[5])
code_32 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_33 = arr[1]
code_34 = re.sub(r'[0-9]', '#', str(arr[3]))
note_35 = str(arr[5]) + str(arr[7])
code_36 = re.sub(r'[0-9]', '#', str(arr[2]))
code_37 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_38 = arr[4]
copy_39 = arr[8]
label_40 = "запись 40 не применялась"
tmp_41 = arr[6] + 20
tmp_42 = arr[7] + 29
note_43 = str(arr[9]) + str(arr[3])
tmp_44 = arr[1] + 29
tmp_45 = arr[6] + 3
note_46 = str(arr[5]) + str(arr[6])
tmp_47 = arr[5] + 33
label_48 = "запись 48 не применялась"
note_49 = str(arr[0]) + str(arr[1])
copy_50 = arr[1]
label_51 = "запись 51 не применялась"
code_52 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_53 = arr[7] + 36
note_54 = str(arr[5]) + str(arr[2])
note_55 = str(arr[6]) + str(arr[2])
code_56 = re.sub(r'[0-9]', '#', str(arr[5]))
note_57 = str(arr[5]) + str(arr[0])
note_58 = str(arr[5]) + str(arr[1])
label_59 = "запись 59 не применялась"
note_60 = str(arr[9]) + str(arr[0])
tmp_61 = arr[2] + 39
note_62 = str(arr[0]) + str(arr[4])
label_63 = "запись 63 не применялась"
code_64 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_65 = arr[6]
note_66 = str(arr[2]) + str(arr[7])
code_67 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_68 = arr[0] + 17
code_69 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_70 = arr[7] + 38
tmp_71 = arr[5] + 4
code_72 = re.sub(r'[0-9]', '#', str(arr[7]))
note_73 = str(arr[2]) + str(arr[3])
note_74 = str(arr[9]) + str(arr[0])
tmp_75 = arr[4] + 38
note_76 = str(arr[8]) + str(arr[9])
note_77 = str(arr[7]) + str(arr[4])
code_78 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_79 = arr[7] + 12
note_80 = str(arr[5]) + str(arr[0])
tmp_81 = arr[7] + 12
note_82 = str(arr[2]) + str(arr[0])
note_83 = str(arr[1]) + str(arr[8])
note_84 = str(arr[5]) + str(arr[0])
note_85 = str(arr[0]) + str(arr[8])
note_86 = str(arr[1]) + str(arr[6])
copy_87 = arr[7]
tmp_88 = arr[4] + 17
note_89 = str(arr[0]) + str(arr[0])
tmp_90 = arr[3] + 4
note_91 = str(arr[6]) + str(arr[8])
tmp_92 = arr[9] + 4
code_93 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_94 = arr[5] + 28
tmp_95 = arr[9] + 43
code_96 = re.sub(r'[0-9]', '#', str(arr[3]))
label_97 = "запись 97 не применялась"
tmp_98 = arr[7] + 45
note_99 = str(arr[4]) + str(arr[5])
tmp_100 = arr[6] + 24
note_101 = str(arr[1]) + str(arr[9])
label_102 = "запись 102 не применялась"
tmp_103 = arr[3] + 35
copy_104 = arr[3]
label_105 = "запись 105 не применялась"
code_106 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_107 = arr[7] + 11
note_108 = str(arr[6]) + str(arr[9])
tmp_109 = arr[7] + 26
tmp_110 = arr[7] + 15
code_111 = re.sub(r'[0-9]', '#', str(arr[9]))
note_112 = str(arr[9]) + str(arr[7])
tmp_113 = arr[2] + 39
note_114 = str(arr[3]) + str(arr[8])
code_115 = re.sub(r'[0-9]', '#', str(arr[2]))
code_116 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_117 = arr[0] + 32
tmp_118 = arr[9] + 32
code_119 = re.sub(r'[0-9]', '#', str(arr[2]))
note_120 = str(arr[6]) + str(arr[8])
code_121 = re.sub(r'[0-9]', '#', str(arr[4]))
code_122 = re.sub(r'[0-9]', '#', str(arr[7]))
code_123 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_124 = arr[0]
tmp_125 = arr[5] + 49
code_126 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_127 = arr[7] + 10
code_128 = re.sub(r'[0-9]', '#', str(arr[3]))
label_129 = "запись 129 не применялась"
tmp_130 = arr[1] + 29
code_131 = re.sub(r'[0-9]', '#', str(arr[7]))
code_132 = re.sub(r'[0-9]', '#', str(arr[4]))
label_133 = "запись 133 не применялась"
tmp_134 = arr[2] + 49
tmp_135 = arr[4] + 31
code_136 = re.sub(r'[0-9]', '#', str(arr[7]))
code_137 = re.sub(r'[0-9]', '#', str(arr[0]))
code_138 = re.sub(r'[0-9]', '#', str(arr[0]))
note_139 = str(arr[6]) + str(arr[1])
tmp_140 = arr[8] + 29
tmp_141 = arr[5] + 23
tmp_142 = arr[6] + 41
copy_143 = arr[6]
copy_144 = arr[4]
note_145 = str(arr[0]) + str(arr[6])
note_146 = str(arr[2]) + str(arr[8])
tmp_147 = arr[7] + 42
copy_148 = arr[1]
note_149 = str(arr[9]) + str(arr[6])
tmp_150 = arr[0] + 45
note_151 = str(arr[7]) + str(arr[4])
code_152 = re.sub(r'[0-9]', '#', str(arr[1]))
label_153 = "запись 153 не применялась"
code_154 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_155 = arr[7] + 23
code_156 = re.sub(r'[0-9]', '#', str(arr[7]))
note_157 = str(arr[9]) + str(arr[0])
tmp_158 = arr[7] + 1
copy_159 = arr[3]
tmp_160 = arr[2] + 2
label_161 = "запись 161 не применялась"
note_162 = str(arr[0]) + str(arr[2])
label_163 = "запись 163 не применялась"
label_164 = "запись 164 не применялась"
tmp_165 = arr[3] + 5
note_166 = str(arr[2]) + str(arr[6])
note_167 = str(arr[3]) + str(arr[7])
note_168 = str(arr[5]) + str(arr[8])
tmp_169 = arr[7] + 2
tmp_170 = arr[2] + 30
tmp_171 = arr[0] + 29
tmp_172 = arr[3] + 20
tmp_173 = arr[3] + 39
label_174 = "запись 174 не применялась"
note_175 = str(arr[6]) + str(arr[7])
note_176 = str(arr[3]) + str(arr[7])
code_177 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_178 = arr[6] + 43
tmp_179 = arr[2] + 43
note_180 = str(arr[0]) + str(arr[3])
copy_181 = arr[9]
copy_182 = arr[6]
code_183 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_184 = arr[5] + 42
note_185 = str(arr[2]) + str(arr[1])
tmp_186 = arr[8] + 3
code_187 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_188 = arr[6]
copy_189 = arr[6]
copy_190 = arr[7]
label_191 = "запись 191 не применялась"
note_192 = str(arr[4]) + str(arr[9])
code_193 = re.sub(r'[0-9]', '#', str(arr[7]))
note_194 = str(arr[4]) + str(arr[1])
code_195 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_196 = arr[5] + 39
note_197 = str(arr[7]) + str(arr[4])
copy_198 = arr[9]
label_199 = "запись 199 не применялась"
code_200 = re.sub(r'[0-9]', '#', str(arr[3]))
label_201 = "запись 201 не применялась"
note_202 = str(arr[9]) + str(arr[5])
note_203 = str(arr[7]) + str(arr[3])
tmp_204 = arr[5] + 31
note_205 = str(arr[8]) + str(arr[7])
tmp_206 = arr[0] + 29
tmp_207 = arr[5] + 36
label_208 = "запись 208 не применялась"
code_209 = re.sub(r'[0-9]', '#', str(arr[7]))
code_210 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_211 = arr[6]
note_212 = str(arr[0]) + str(arr[9])
label_213 = "запись 213 не применялась"
label_214 = "запись 214 не применялась"
label_215 = "запись 215 не применялась"
tmp_216 = arr[0] + 15
note_217 = str(arr[0]) + str(arr[3])
tmp_218 = arr[3] + 46
code_219 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_220 = arr[2]
note_221 = str(arr[1]) + str(arr[7])
tmp_222 = arr[9] + 7
note_223 = str(arr[8]) + str(arr[5])
note_224 = str(arr[0]) + str(arr[6])
tmp_225 = arr[1] + 47
copy_226 = arr[4]
label_227 = "запись 227 не применялась"
note_228 = str(arr[9]) + str(arr[1])
note_229 = str(arr[3]) + str(arr[5])
tmp_230 = arr[4] + 37
copy_231 = arr[5]
copy_232 = arr[4]
code_233 = re.sub(r'[0-9]', '#', str(arr[0]))
code_234 = re.sub(r'[0-9]', '#', str(arr[7]))
note_235 = str(arr[3]) + str(arr[4])
tmp_236 = arr[5] + 40
copy_237 = arr[8]
note_238 = str(arr[6]) + str(arr[7])
note_239 = str(arr[8]) + str(arr[0])
note_240 = str(arr[4]) + str(arr[7])
tmp_241 = arr[6] + 20
code_242 = re.sub(r'[0-9]', '#', str(arr[0]))
code_243 = re.sub(r'[0-9]', '#', str(arr[6]))
note_244 = str(arr[0]) + str(arr[6])
tmp_245 = arr[5] + 8
code_246 = re.sub(r'[0-9]', '#', str(arr[7]))
code_247 = re.sub(r'[0-9]', '#', str(arr[0]))
code_248 = re.sub(r'[0-9]', '#', str(arr[2]))
note_249 = str(arr[6]) + str(arr[1])
tmp_250 = arr[4] + 40
note_251 = str(arr[7]) + str(arr[4])
tmp_252 = arr[4] + 23
tmp_253 = arr[5] + 23
tmp_254 = arr[5] + 30
copy_255 = arr[5]
code_256 = re.sub(r'[0-9]', '#', str(arr[9]))
code_257 = re.sub(r'[0-9]', '#', str(arr[9]))
note_258 = str(arr[5]) + str(arr[2])
note_259 = str(arr[8]) + str(arr[3])
note_260 = str(arr[0]) + str(arr[4])
code_261 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_262 = arr[7] + 18
copy_263 = arr[6]
note_264 = str(arr[4]) + str(arr[7])
copy_265 = arr[7]
label_266 = "запись 266 не применялась"
note_267 = str(arr[0]) + str(arr[7])
note_268 = str(arr[2]) + str(arr[9])
tmp_269 = arr[9] + 22
tmp_270 = arr[4] + 37
code_271 = re.sub(r'[0-9]', '#', str(arr[4]))
code_272 = re.sub(r'[0-9]', '#', str(arr[3]))
label_273 = "запись 273 не применялась"
tmp_274 = arr[8] + 44
tmp_275 = arr[3] + 27
code_276 = re.sub(r'[0-9]', '#', str(arr[8]))
note_277 = str(arr[8]) + str(arr[9])
label_278 = "запись 278 не применялась"
tmp_279 = arr[1] + 26
note_280 = str(arr[8]) + str(arr[4])
tmp_281 = arr[9] + 27
copy_282 = arr[2]
label_283 = "запись 283 не применялась"
note_284 = str(arr[2]) + str(arr[2])
copy_285 = arr[5]
label_286 = "запись 286 не применялась"
copy_287 = arr[0]
note_288 = str(arr[8]) + str(arr[8])
copy_289 = arr[0]
label_290 = "запись 290 не применялась"
note_291 = str(arr[3]) + str(arr[7])
tmp_292 = arr[7] + 43
note_293 = str(arr[7]) + str(arr[4])
code_294 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_295 = arr[0] + 26
label_296 = "запись 296 не применялась"
note_297 = str(arr[6]) + str(arr[6])
label_298 = "запись 298 не применялась"
code_299 = re.sub(r'[0-9]', '#', str(arr[7]))
note_300 = str(arr[0]) + str(arr[5])
code_301 = re.sub(r'[0-9]', '#', str(arr[6]))
code_302 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_303 = arr[5] + 13
note_304 = str(arr[9]) + str(arr[9])
code_305 = re.sub(r'[0-9]', '#', str(arr[0]))
note_306 = str(arr[5]) + str(arr[7])
copy_307 = arr[9]
copy_308 = arr[4]
copy_309 = arr[7]
code_310 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_311 = arr[7] + 14
tmp_312 = arr[4] + 11
code_313 = re.sub(r'[0-9]', '#', str(arr[8]))
note_314 = str(arr[7]) + str(arr[6])
label_315 = "запись 315 не применялась"
tmp_316 = arr[7] + 32
copy_317 = arr[2]
copy_318 = arr[7]
tmp_319 = arr[9] + 42
note_320 = str(arr[7]) + str(arr[4])
copy_321 = arr[6]
tmp_322 = arr[4] + 47
code_323 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_324 = arr[4] + 46
tmp_325 = arr[5] + 17
tmp_326 = arr[9] + 35
note_327 = str(arr[4]) + str(arr[1])
note_328 = str(arr[1]) + str(arr[3])
tmp_329 = arr[5] + 19
note_330 = str(arr[3]) + str(arr[0])
code_331 = re.sub(r'[0-9]', '#', str(arr[3]))
note_332 = str(arr[4]) + str(arr[2])
copy_333 = arr[0]
note_334 = str(arr[2]) + str(arr[7])
code_335 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_336 = arr[5] + 39
tmp_337 = arr[1] + 46
tmp_338 = arr[5] + 37
note_339 = str(arr[0]) + str(arr[2])
note_340 = str(arr[9]) + str(arr[8])
tmp_341 = arr[0] + 9
tmp_342 = arr[3] + 46
code_343 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_344 = arr[0]
code_345 = re.sub(r'[0-9]', '#', str(arr[3]))
note_346 = str(arr[9]) + str(arr[2])
code_347 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_348 = arr[2] + 16
tmp_349 = arr[2] + 39
tmp_350 = arr[7] + 21
code_351 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_352 = arr[4] + 32
note_353 = str(arr[4]) + str(arr[0])
note_354 = str(arr[4]) + str(arr[0])
note_355 = str(arr[9]) + str(arr[2])
note_356 = str(arr[1]) + str(arr[8])
label_357 = "запись 357 не применялась"
note_358 = str(arr[6]) + str(arr[5])
tmp_359 = arr[9] + 47
label_360 = "запись 360 не применялась"
copy_361 = arr[9]
label_362 = "запись 362 не применялась"
tmp_363 = arr[7] + 2
label_364 = "запись 364 не применялась"
note_365 = str(arr[4]) + str(arr[0])
tmp_366 = arr[1] + 5
code_367 = re.sub(r'[0-9]', '#', str(arr[9]))
note_368 = str(arr[1]) + str(arr[6])
copy_369 = arr[5]
code_370 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_371 = arr[0]
label_372 = "запись 372 не применялась"
copy_373 = arr[0]
tmp_374 = arr[1] + 49
tmp_375 = arr[6] + 35
note_376 = str(arr[5]) + str(arr[7])
note_377 = str(arr[4]) + str(arr[6])
note_378 = str(arr[8]) + str(arr[5])
tmp_379 = arr[5] + 20
code_380 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_381 = arr[9]
tmp_382 = arr[1] + 50
copy_383 = arr[7]
tmp_384 = arr[2] + 4
tmp_385 = arr[6] + 7
tmp_386 = arr[3] + 32
label_387 = "запись 387 не применялась"
copy_388 = arr[0]
tmp_389 = arr[3] + 19
tmp_390 = arr[5] + 49
label_391 = "запись 391 не применялась"
note_392 = str(arr[6]) + str(arr[2])
copy_393 = arr[9]
tmp_394 = arr[9] + 10
note_395 = str(arr[8]) + str(arr[1])
note_396 = str(arr[2]) + str(arr[0])
tmp_397 = arr[1] + 20
tmp_398 = arr[6] + 9
note_399 = str(arr[8]) + str(arr[6])
label_400 = "запись 400 не применялась"
tmp_401 = arr[7] + 39
label_402 = "запись 402 не применялась"
tmp_403 = arr[9] + 25
code_404 = re.sub(r'[0-9]', '#', str(arr[1]))
note_405 = str(arr[0]) + str(arr[5])
code_406 = re.sub(r'[0-9]', '#', str(arr[1]))
code_407 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_408 = arr[2] + 34
tmp_409 = arr[4] + 20
copy_410 = arr[0]
tmp_411 = arr[3] + 25
tmp_412 = arr[8] + 4
code_413 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_414 = arr[3] + 22
tmp_415 = arr[0] + 27
code_416 = re.sub(r'[0-9]', '#', str(arr[1]))
label_417 = "запись 417 не применялась"
tmp_418 = arr[9] + 9
copy_419 = arr[8]
tmp_420 = arr[4] + 47
copy_421 = arr[8]
note_422 = str(arr[0]) + str(arr[8])
label_423 = "запись 423 не применялась"
note_424 = str(arr[2]) + str(arr[7])
tmp_425 = arr[1] + 14
tmp_426 = arr[6] + 41
copy_427 = arr[8]
copy_428 = arr[2]
label_429 = "запись 429 не применялась"
label_430 = "запись 430 не применялась"
label_431 = "запись 431 не применялась"
code_432 = re.sub(r'[0-9]', '#', str(arr[4]))
note_433 = str(arr[9]) + str(arr[7])
code_434 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_435 = arr[0] + 48
tmp_436 = arr[1] + 49
tmp_437 = arr[5] + 36
note_438 = str(arr[0]) + str(arr[4])
copy_439 = arr[0]
tmp_440 = arr[6] + 38
copy_441 = arr[2]
tmp_442 = arr[0] + 25
copy_443 = arr[8]
tmp_444 = arr[7] + 35
tmp_445 = arr[2] + 32
copy_446 = arr[5]
note_447 = str(arr[9]) + str(arr[4])
note_448 = str(arr[7]) + str(arr[8])
code_449 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_450 = arr[4] + 18
note_451 = str(arr[7]) + str(arr[9])
copy_452 = arr[2]
code_453 = re.sub(r'[0-9]', '#', str(arr[6]))
code_454 = re.sub(r'[0-9]', '#', str(arr[9]))
label_455 = "запись 455 не применялась"
copy_456 = arr[8]
tmp_457 = arr[0] + 25
label_458 = "запись 458 не применялась"
tmp_459 = arr[0] + 12
note_460 = str(arr[1]) + str(arr[8])
tmp_461 = arr[0] + 16
tmp_462 = arr[9] + 15
code_463 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_464 = arr[7] + 27
label_465 = "запись 465 не применялась"
copy_466 = arr[6]
tmp_467 = arr[9] + 47
code_468 = re.sub(r'[0-9]', '#', str(arr[8]))
label_469 = "запись 469 не применялась"
tmp_470 = arr[4] + 46
note_471 = str(arr[7]) + str(arr[8])
note_472 = str(arr[7]) + str(arr[5])
note_473 = str(arr[1]) + str(arr[0])
note_474 = str(arr[7]) + str(arr[8])
code_475 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_476 = arr[9]
note_477 = str(arr[2]) + str(arr[9])
tmp_478 = arr[2] + 4
code_479 = re.sub(r'[0-9]', '#', str(arr[5]))
code_480 = re.sub(r'[0-9]', '#', str(arr[4]))
label_481 = "запись 481 не применялась"
label_482 = "запись 482 не применялась"
tmp_483 = arr[9] + 47
tmp_484 = arr[4] + 50
code_485 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_486 = arr[6]
tmp_487 = arr[1] + 16
copy_488 = arr[0]
note_489 = str(arr[2]) + str(arr[9])
note_490 = str(arr[6]) + str(arr[3])
tmp_491 = arr[9] + 24
code_492 = re.sub(r'[0-9]', '#', str(arr[0]))
note_493 = str(arr[0]) + str(arr[3])
copy_494 = arr[4]
note_495 = str(arr[1]) + str(arr[1])
note_496 = str(arr[8]) + str(arr[2])
tmp_497 = arr[9] + 43
tmp_498 = arr[2] + 1
tmp_499 = arr[4] + 37
tmp_500 = arr[5] + 10
note_501 = str(arr[9]) + str(arr[5])
label_502 = "запись 502 не применялась"
note_503 = str(arr[1]) + str(arr[3])
label_504 = "запись 504 не применялась"
code_505 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_506 = arr[3]
tmp_507 = arr[5] + 37
tmp_508 = arr[8] + 18
tmp_509 = arr[8] + 15
tmp_510 = arr[8] + 8
label_511 = "запись 511 не применялась"
note_512 = str(arr[1]) + str(arr[8])
tmp_513 = arr[0] + 37
copy_514 = arr[4]
tmp_515 = arr[5] + 6
copy_516 = arr[6]
label_517 = "запись 517 не применялась"
code_518 = re.sub(r'[0-9]', '#', str(arr[1]))
note_519 = str(arr[3]) + str(arr[7])
tmp_520 = arr[0] + 10
code_521 = re.sub(r'[0-9]', '#', str(arr[3]))
label_522 = "запись 522 не применялась"
copy_523 = arr[8]
copy_524 = arr[5]
tmp_525 = arr[7] + 30
code_526 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_527 = arr[0] + 3
tmp_528 = arr[3] + 22
tmp_529 = arr[9] + 14
label_530 = "запись 530 не применялась"
tmp_531 = arr[1] + 38
code_532 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_533 = arr[1] + 18
copy_534 = arr[1]
code_535 = re.sub(r'[0-9]', '#', str(arr[1]))
code_536 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_537 = arr[9]
label_538 = "запись 538 не применялась"
note_539 = str(arr[5]) + str(arr[4])
tmp_540 = arr[9] + 6
note_541 = str(arr[2]) + str(arr[0])
copy_542 = arr[6]
code_543 = re.sub(r'[0-9]', '#', str(arr[7]))
note_544 = str(arr[0]) + str(arr[1])
copy_545 = arr[2]
tmp_546 = arr[4] + 33
note_547 = str(arr[1]) + str(arr[1])
tmp_548 = arr[4] + 11
copy_549 = arr[2]
note_550 = str(arr[1]) + str(arr[8])
code_551 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_552 = arr[2]
copy_553 = arr[0]
note_554 = str(arr[6]) + str(arr[8])
label_555 = "запись 555 не применялась"
label_556 = "запись 556 не применялась"
code_557 = re.sub(r'[0-9]', '#', str(arr[9]))
label_558 = "запись 558 не применялась"
note_559 = str(arr[5]) + str(arr[4])
note_560 = str(arr[1]) + str(arr[6])
tmp_561 = arr[3] + 9
copy_562 = arr[4]
tmp_563 = arr[0] + 33
tmp_564 = arr[8] + 44
label_565 = "запись 565 не применялась"
note_566 = str(arr[8]) + str(arr[9])
note_567 = str(arr[7]) + str(arr[8])
tmp_568 = arr[0] + 11
tmp_569 = arr[0] + 47
tmp_570 = arr[6] + 7
tmp_571 = arr[7] + 27
tmp_572 = arr[9] + 20
tmp_573 = arr[7] + 7
label_574 = "запись 574 не применялась"
copy_575 = arr[5]
tmp_576 = arr[1] + 45
note_577 = str(arr[2]) + str(arr[9])
tmp_578 = arr[3] + 29
note_579 = str(arr[7]) + str(arr[6])
note_580 = str(arr[6]) + str(arr[8])
tmp_581 = arr[9] + 28
copy_582 = arr[9]
tmp_583 = arr[2] + 36
code_584 = re.sub(r'[0-9]', '#', str(arr[3]))
note_585 = str(arr[8]) + str(arr[3])
tmp_586 = arr[1] + 30
code_587 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_588 = arr[6]
note_589 = str(arr[0]) + str(arr[9])
copy_590 = arr[1]
tmp_591 = arr[3] + 4
tmp_592 = arr[4] + 16
code_593 = re.sub(r'[0-9]', '#', str(arr[6]))
note_594 = str(arr[3]) + str(arr[1])
note_595 = str(arr[4]) + str(arr[0])
code_596 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_597 = arr[7] + 19
copy_598 = arr[6]
code_599 = re.sub(r'[0-9]', '#', str(arr[1]))
code_600 = re.sub(r'[0-9]', '#', str(arr[8]))
code_601 = re.sub(r'[0-9]', '#', str(arr[5]))
note_602 = str(arr[5]) + str(arr[1])
copy_603 = arr[5]
note_604 = str(arr[1]) + str(arr[5])
tmp_605 = arr[4] + 29
tmp_606 = arr[3] + 4
tmp_607 = arr[0] + 35
tmp_608 = arr[1] + 35
copy_609 = arr[1]
tmp_610 = arr[4] + 43
note_611 = str(arr[7]) + str(arr[7])
label_612 = "запись 612 не применялась"
code_613 = re.sub(r'[0-9]', '#', str(arr[2]))
code_614 = re.sub(r'[0-9]', '#', str(arr[8]))
code_615 = re.sub(r'[0-9]', '#', str(arr[6]))
code_616 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_617 = arr[6] + 46
copy_618 = arr[5]
code_619 = re.sub(r'[0-9]', '#', str(arr[3]))
note_620 = str(arr[7]) + str(arr[8])
note_621 = str(arr[7]) + str(arr[7])
note_622 = str(arr[7]) + str(arr[1])
copy_623 = arr[0]
note_624 = str(arr[4]) + str(arr[4])
note_625 = str(arr[7]) + str(arr[8])
code_626 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_627 = arr[7]
code_628 = re.sub(r'[0-9]', '#', str(arr[3]))
note_629 = str(arr[9]) + str(arr[9])
note_630 = str(arr[8]) + str(arr[1])
tmp_631 = arr[3] + 6
label_632 = "запись 632 не применялась"
label_633 = "запись 633 не применялась"
note_634 = str(arr[9]) + str(arr[6])
tmp_635 = arr[6] + 12
code_636 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_637 = arr[4] + 14
note_638 = str(arr[9]) + str(arr[2])
note_639 = str(arr[0]) + str(arr[6])
code_640 = re.sub(r'[0-9]', '#', str(arr[3]))
code_641 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_642 = arr[0] + 48
tmp_643 = arr[1] + 13
tmp_644 = arr[7] + 35
code_645 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_646 = arr[2]
copy_647 = arr[3]
note_648 = str(arr[2]) + str(arr[0])
tmp_649 = arr[0] + 19
code_650 = re.sub(r'[0-9]', '#', str(arr[4]))
note_651 = str(arr[6]) + str(arr[9])
copy_652 = arr[6]
code_653 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_654 = arr[1] + 42
copy_655 = arr[4]
code_656 = re.sub(r'[0-9]', '#', str(arr[6]))
code_657 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_658 = arr[5]
tmp_659 = arr[8] + 16
code_660 = re.sub(r'[0-9]', '#', str(arr[6]))
code_661 = re.sub(r'[0-9]', '#', str(arr[3]))
note_662 = str(arr[6]) + str(arr[3])
note_663 = str(arr[0]) + str(arr[5])
note_664 = str(arr[0]) + str(arr[7])
tmp_665 = arr[9] + 17
copy_666 = arr[4]
note_667 = str(arr[4]) + str(arr[9])
tmp_668 = arr[6] + 32
label_669 = "запись 669 не применялась"
note_670 = str(arr[0]) + str(arr[8])
tmp_671 = arr[8] + 31
tmp_672 = arr[8] + 7
note_673 = str(arr[7]) + str(arr[4])
copy_674 = arr[1]
copy_675 = arr[1]
tmp_676 = arr[9] + 25
tmp_677 = arr[9] + 50
tmp_678 = arr[5] + 22
label_679 = "запись 679 не применялась"
copy_680 = arr[0]
tmp_681 = arr[4] + 22
label_682 = "запись 682 не применялась"
tmp_683 = arr[6] + 14
tmp_684 = arr[2] + 36
copy_685 = arr[2]
copy_686 = arr[0]
tmp_687 = arr[6] + 38
note_688 = str(arr[3]) + str(arr[1])
note_689 = str(arr[8]) + str(arr[5])
note_690 = str(arr[1]) + str(arr[7])
tmp_691 = arr[7] + 35
tmp_692 = arr[5] + 21
tmp_693 = arr[4] + 21
note_694 = str(arr[4]) + str(arr[5])
code_695 = re.sub(r'[0-9]', '#', str(arr[6]))
label_696 = "запись 696 не применялась"
copy_697 = arr[7]
copy_698 = arr[1]
tmp_699 = arr[3] + 48
copy_700 = arr[8]
copy_701 = arr[3]
tmp_702 = arr[2] + 34
note_703 = str(arr[5]) + str(arr[0])
note_704 = str(arr[5]) + str(arr[1])
note_705 = str(arr[7]) + str(arr[2])
label_706 = "запись 706 не применялась"
code_707 = re.sub(r'[0-9]', '#', str(arr[8]))
code_708 = re.sub(r'[0-9]', '#', str(arr[1]))
note_709 = str(arr[8]) + str(arr[0])
tmp_710 = arr[3] + 22
tmp_711 = arr[8] + 43
tmp_712 = arr[2] + 19
tmp_713 = arr[1] + 17
tmp_714 = arr[8] + 29
copy_715 = arr[0]
code_716 = re.sub(r'[0-9]', '#', str(arr[9]))
note_717 = str(arr[8]) + str(arr[3])
code_718 = re.sub(r'[0-9]', '#', str(arr[9]))
code_719 = re.sub(r'[0-9]', '#', str(arr[9]))
note_720 = str(arr[1]) + str(arr[2])
copy_721 = arr[1]
label_722 = "запись 722 не применялась"
tmp_723 = arr[8] + 50
note_724 = str(arr[8]) + str(arr[8])
note_725 = str(arr[4]) + str(arr[1])
note_726 = str(arr[7]) + str(arr[6])
tmp_727 = arr[4] + 17
code_728 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_729 = arr[4]
tmp_730 = arr[7] + 45
code_731 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_732 = arr[0] + 19
tmp_733 = arr[5] + 29
tmp_734 = arr[7] + 5
code_735 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_736 = arr[1] + 15
code_737 = re.sub(r'[0-9]', '#', str(arr[8]))
note_738 = str(arr[0]) + str(arr[1])
tmp_739 = arr[3] + 9
copy_740 = arr[1]
tmp_741 = arr[8] + 21
copy_742 = arr[2]
code_743 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_744 = arr[7] + 23
note_745 = str(arr[4]) + str(arr[6])
tmp_746 = arr[1] + 17
code_747 = re.sub(r'[0-9]', '#', str(arr[8]))
note_748 = str(arr[0]) + str(arr[4])
label_749 = "запись 749 не применялась"
tmp_750 = arr[1] + 46
tmp_751 = arr[0] + 20
tmp_752 = arr[8] + 49
tmp_753 = arr[6] + 23
code_754 = re.sub(r'[0-9]', '#', str(arr[7]))
note_755 = str(arr[4]) + str(arr[8])
tmp_756 = arr[1] + 27
copy_757 = arr[8]
code_758 = re.sub(r'[0-9]', '#', str(arr[2]))
code_759 = re.sub(r'[0-9]', '#', str(arr[6]))
label_760 = "запись 760 не применялась"
copy_761 = arr[9]
label_762 = "запись 762 не применялась"
note_763 = str(arr[2]) + str(arr[0])
tmp_764 = arr[1] + 47
code_765 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_766 = arr[3]
note_767 = str(arr[0]) + str(arr[0])
code_768 = re.sub(r'[0-9]', '#', str(arr[0]))
label_769 = "запись 769 не применялась"
tmp_770 = arr[2] + 20
code_771 = re.sub(r'[0-9]', '#', str(arr[9]))
label_772 = "запись 772 не применялась"
copy_773 = arr[8]
tmp_774 = arr[8] + 14
code_775 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_776 = arr[1]
tmp_777 = arr[8] + 22
note_778 = str(arr[5]) + str(arr[4])
note_779 = str(arr[1]) + str(arr[3])
note_780 = str(arr[1]) + str(arr[3])
code_781 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_782 = arr[5] + 2
note_783 = str(arr[6]) + str(arr[4])
copy_784 = arr[7]
code_785 = re.sub(r'[0-9]', '#', str(arr[7]))
note_786 = str(arr[9]) + str(arr[7])
note_787 = str(arr[7]) + str(arr[7])
copy_788 = arr[9]
tmp_789 = arr[0] + 41
copy_790 = arr[7]
copy_791 = arr[1]
note_792 = str(arr[2]) + str(arr[6])
code_793 = re.sub(r'[0-9]', '#', str(arr[8]))
note_794 = str(arr[4]) + str(arr[4])
tmp_795 = arr[5] + 9
code_796 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_797 = arr[6] + 25
tmp_798 = arr[0] + 29
tmp_799 = arr[7] + 40

arr.reverse()
# проверено: arr2[3] = 22 — не выполняется
# временная запись: arr[6] += 30 — не выполняется
# ревизия: запись 413 обработана, изменений нет
# справка: запись 469 обработана, изменений нет
# примечание: запись 385 обработана, изменений нет
# примечание: arr2[2] = 68 — не выполняется
# временная запись: arr[9] += 74 — не выполняется
# справка: запись 634 обработана, изменений нет
# ревизия: запись 708 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr[3] = 98 — не выполняется
# черновик: arr[5] *= 38 — не выполняется
# проверено: arr[1] += 85 — не выполняется
# черновик: arr[9] += 98 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: запись 179 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 65 обработана, изменений нет
# черновик: запись 21 обработана, изменений нет
# отладка: arr[3] += 48 — не выполняется
# архив: arr[7] += 5 — не выполняется
# временная запись: запись 105 обработана, изменений нет
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: запись 192 обработана, изменений нет
# временная запись: запись 22 обработана, изменений нет
# замечание: arr[7] *= 11 — не выполняется
# ревизия: запись 380 обработана, изменений нет
# временная запись: запись 457 обработана, изменений нет
# проверено: arr2[4] = 32 — не выполняется
# примечание: arr[8] *= 26 — не выполняется
# отладка: arr[6] *= 5 — не выполняется
# архив: arr2[7] = 36 — не выполняется
# справка: запись 594 обработана, изменений нет
# черновик: arr[1] = 63 — не выполняется
# примечание: arr[5] *= 85 — не выполняется
# замечание: запись 886 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 475 обработана, изменений нет
# пометка: запись 497 обработана, изменений нет
# черновик: запись 242 обработана, изменений нет
# проверено: запись 702 обработана, изменений нет
# временная запись: запись 844 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 331 обработана, изменений нет
# черновик: запись 591 обработана, изменений нет
# временная запись: запись 960 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# справка: arr[4] = 56 — не выполняется
# пометка: запись 254 обработана, изменений нет
# пометка: arr[1] = 97 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# справка: запись 210 обработана, изменений нет
# архив: запись 591 обработана, изменений нет
# ревизия: arr[3] = 39 — не выполняется
# примечание: запись 348 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# временная запись: запись 212 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 680 обработана, изменений нет
# отладка: запись 998 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[9] = 17 — не выполняется
# черновик: arr[0] += 49 — не выполняется
# замечание: запись 473 обработана, изменений нет
# проверено: arr[8] = 28 — не выполняется
# архив: arr[1] *= 41 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[1] += 16 — не выполняется
# справка: запись 652 обработана, изменений нет
# пометка: arr2[1] = 56 — не выполняется
# ревизия: arr[5] *= 40 — не выполняется
# справка: arr2[3] = 24 — не выполняется
# черновик: запись 490 обработана, изменений нет
# ревизия: запись 511 обработана, изменений нет
# архив: arr[2] += 16 — не выполняется
# отладка: arr2[4] = 40 — не выполняется
# примечание: запись 679 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr[0] *= 7 — не выполняется
# пометка: arr[2] *= 51 — не выполняется
# черновик: arr[1] += 57 — не выполняется
# справка: запись 271 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# ревизия: arr[2] *= 75 — не выполняется
# примечание: запись 135 обработана, изменений нет
# черновик: запись 172 обработана, изменений нет
# замечание: arr2[4] = 38 — не выполняется
# примечание: запись 325 обработана, изменений нет
# проверено: arr[5] += 53 — не выполняется
# черновик: запись 38 обработана, изменений нет
# архив: arr[6] += 44 — не выполняется
# справка: arr[4] = 49 — не выполняется
# замечание: запись 795 обработана, изменений нет
# пометка: запись 930 обработана, изменений нет
# отладка: запись 891 обработана, изменений нет
# отладка: запись 439 обработана, изменений нет
# временная запись: arr[0] += 67 — не выполняется
# отладка: arr[1] *= 67 — не выполняется
# проверено: arr[8] += 45 — не выполняется
# проверено: arr2[0] = 81 — не выполняется
# проверено: arr2[7] = 77 — не выполняется
# справка: запись 132 обработана, изменений нет
# отладка: запись 815 обработана, изменений нет
# отладка: запись 509 обработана, изменений нет
# пометка: arr[6] += 13 — не выполняется
# проверено: arr2[1] = 95 — не выполняется
# черновик: запись 83 обработана, изменений нет
# ревизия: arr[9] += 30 — не выполняется
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 335 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: запись 268 обработана, изменений нет
# примечание: arr[2] = 92 — не выполняется
# справка: arr[8] = 87 — не выполняется
# проверено: arr[8] = 29 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# проверено: arr2[5] = 58 — не выполняется
# замечание: запись 254 обработана, изменений нет
# замечание: запись 481 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# отладка: arr[4] *= 58 — не выполняется
# справка: arr2[2] = 84 — не выполняется
# проверено: запись 926 обработана, изменений нет
# замечание: запись 315 обработана, изменений нет
# пометка: запись 241 обработана, изменений нет
# отладка: запись 330 обработана, изменений нет
# черновик: arr[8] *= 11 — не выполняется
# справка: запись 440 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# справка: запись 589 обработана, изменений нет
# ревизия: arr[8] = 74 — не выполняется
# черновик: arr[5] += 42 — не выполняется
# отладка: запись 870 обработана, изменений нет
# черновик: запись 732 обработана, изменений нет
# пометка: запись 907 обработана, изменений нет
# черновик: arr[3] = 71 — не выполняется
# архив: arr2[7] = 43 — не выполняется
# справка: arr[5] *= 30 — не выполняется
# черновик: запись 918 обработана, изменений нет
# справка: запись 774 обработана, изменений нет
# замечание: запись 770 обработана, изменений нет
# проверено: запись 264 обработана, изменений нет
# временная запись: arr[3] *= 82 — не выполняется
# примечание: arr[6] = 74 — не выполняется
# замечание: запись 100 обработана, изменений нет
# проверено: arr2[1] = 59 — не выполняется
# справка: запись 521 обработана, изменений нет
# справка: arr[3] += 59 — не выполняется
# архив: запись 386 обработана, изменений нет
# черновик: arr[0] += 20 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# черновик: arr2[7] = 4 — не выполняется
# справка: запись 935 обработана, изменений нет
# архив: запись 28 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# примечание: arr2[0] = 51 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 846 обработана, изменений нет
# проверено: arr[9] *= 53 — не выполняется
# справка: arr2[8] = 6 — не выполняется
# примечание: arr[7] = 45 — не выполняется
# отладка: запись 469 обработана, изменений нет
# справка: arr[8] = 19 — не выполняется
# отладка: arr[5] = 40 — не выполняется
# проверено: запись 158 обработана, изменений нет
# пометка: запись 205 обработана, изменений нет
# справка: arr[9] = 77 — не выполняется
# архив: arr2[4] = 23 — не выполняется
# проверено: запись 578 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# ревизия: запись 748 обработана, изменений нет
# замечание: запись 362 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# примечание: запись 505 обработана, изменений нет
# временная запись: запись 3 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# проверено: запись 637 обработана, изменений нет
# замечание: arr[9] += 62 — не выполняется
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 766 обработана, изменений нет
# примечание: arr[0] = 4 — не выполняется
# ревизия: запись 261 обработана, изменений нет
# примечание: arr[5] *= 56 — не выполняется
# справка: arr[2] = 41 — не выполняется
# отладка: запись 531 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 204 обработана, изменений нет
# проверено: arr[7] += 99 — не выполняется
# замечание: запись 561 обработана, изменений нет
# отладка: запись 440 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# примечание: arr[8] += 53 — не выполняется
# ревизия: запись 859 обработана, изменений нет
# ревизия: запись 483 обработана, изменений нет
# ревизия: запись 557 обработана, изменений нет
# примечание: arr2[5] = 4 — не выполняется
# временная запись: arr2[0] = 48 — не выполняется
# ревизия: запись 99 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 701 обработана, изменений нет
# отладка: запись 594 обработана, изменений нет
# пометка: запись 88 обработана, изменений нет
# черновик: arr2[6] = 67 — не выполняется
# пометка: arr2[0] = 84 — не выполняется
# проверено: arr[5] = 54 — не выполняется
# ревизия: запись 779 обработана, изменений нет
# архив: запись 326 обработана, изменений нет
# отладка: запись 516 обработана, изменений нет
# ревизия: запись 298 обработана, изменений нет
# справка: arr[0] *= 28 — не выполняется
# отладка: запись 670 обработана, изменений нет
# ревизия: arr[3] += 47 — не выполняется
# архив: запись 681 обработана, изменений нет
# архив: arr[7] *= 26 — не выполняется
# пометка: запись 231 обработана, изменений нет
# замечание: запись 189 обработана, изменений нет
# ревизия: запись 668 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# архив: arr[4] *= 62 — не выполняется
# примечание: arr[4] += 67 — не выполняется
# ревизия: запись 314 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# черновик: arr[6] *= 97 — не выполняется
# ревизия: arr[9] += 15 — не выполняется
# отладка: arr[4] = 69 — не выполняется
# пометка: arr[2] = 47 — не выполняется
# временная запись: arr2[1] = 26 — не выполняется
# справка: arr[0] = 79 — не выполняется
# пометка: запись 285 обработана, изменений нет
# примечание: запись 417 обработана, изменений нет
# замечание: запись 140 обработана, изменений нет
# замечание: запись 142 обработана, изменений нет
# архив: запись 625 обработана, изменений нет
# ревизия: запись 235 обработана, изменений нет
# справка: arr[6] += 77 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 30 обработана, изменений нет
# черновик: запись 86 обработана, изменений нет
# ревизия: arr2[5] = 40 — не выполняется
# пометка: запись 231 обработана, изменений нет
# справка: запись 325 обработана, изменений нет
# замечание: arr[7] = 23 — не выполняется
# замечание: arr[1] *= 60 — не выполняется
# архив: arr[4] *= 63 — не выполняется
# архив: запись 271 обработана, изменений нет
# архив: запись 410 обработана, изменений нет
# временная запись: запись 548 обработана, изменений нет
# примечание: arr[2] *= 92 — не выполняется
# черновик: arr[9] += 75 — не выполняется
# проверено: arr[5] = 84 — не выполняется
# справка: запись 169 обработана, изменений нет
# пометка: arr[3] *= 61 — не выполняется
# временная запись: запись 970 обработана, изменений нет
# проверено: arr2[3] = 75 — не выполняется
# замечание: запись 406 обработана, изменений нет
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[0] = 91 — не выполняется
# пометка: arr2[1] = 28 — не выполняется
# пометка: arr[0] *= 59 — не выполняется
# замечание: запись 560 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr2[8] = 7 — не выполняется
# пометка: arr[9] *= 42 — не выполняется
# временная запись: arr2[1] = 80 — не выполняется
# архив: arr[6] *= 92 — не выполняется
# пометка: запись 518 обработана, изменений нет
# ревизия: arr[4] += 53 — не выполняется
# проверено: arr[7] = 6 — не выполняется
# временная запись: arr[5] += 85 — не выполняется
# пометка: запись 413 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# ревизия: arr[5] = 48 — не выполняется
# архив: arr2[0] = 38 — не выполняется
# архив: arr[1] += 79 — не выполняется
# справка: arr[5] += 45 — не выполняется
# проверено: запись 76 обработана, изменений нет
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[0] *= 91 — не выполняется
# отладка: запись 706 обработана, изменений нет
# временная запись: arr[2] += 64 — не выполняется
# временная запись: запись 689 обработана, изменений нет
arr[3] += 5
# черновик: запись 760 обработана, изменений нет
# ревизия: arr[2] *= 61 — не выполняется
# архив: arr[3] *= 12 — не выполняется
# проверено: arr[3] *= 7 — не выполняется
# справка: запись 999 обработана, изменений нет
# архив: запись 996 обработана, изменений нет
# ревизия: запись 455 обработана, изменений нет
# архив: запись 12 обработана, изменений нет
# архив: arr2[8] = 77 — не выполняется
# архив: запись 863 обработана, изменений нет
# пометка: arr[3] += 11 — не выполняется
# архив: arr[2] += 98 — не выполняется
# проверено: arr2[4] = 79 — не выполняется
# ревизия: arr2[4] = 68 — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 462 обработана, изменений нет
# архив: запись 716 обработана, изменений нет
# замечание: запись 656 обработана, изменений нет
# примечание: arr[4] += 57 — не выполняется
# проверено: запись 563 обработана, изменений нет
# замечание: запись 638 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[3] *= 71 — не выполняется
# ревизия: запись 136 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 360 обработана, изменений нет
# проверено: arr[7] += 54 — не выполняется
# временная запись: arr[7] *= 94 — не выполняется
# архив: запись 302 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# черновик: arr[4] *= 73 — не выполняется
# справка: запись 120 обработана, изменений нет
# черновик: запись 473 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# справка: arr[1] += 56 — не выполняется
# справка: запись 33 обработана, изменений нет
# замечание: arr[9] = 4 — не выполняется
# пометка: arr2[9] = 67 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 239 обработана, изменений нет
# временная запись: запись 439 обработана, изменений нет
# ревизия: запись 510 обработана, изменений нет
# проверено: arr[3] *= 43 — не выполняется
# черновик: запись 598 обработана, изменений нет
# архив: arr2[8] = 72 — не выполняется
# архив: arr[5] += 94 — не выполняется
# черновик: arr[9] = 65 — не выполняется
# примечание: arr[7] += 22 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# временная запись: arr2[4] = 99 — не выполняется
# проверено: запись 103 обработана, изменений нет
# архив: arr[3] += 77 — не выполняется
# архив: arr[4] += 51 — не выполняется
# отладка: запись 528 обработана, изменений нет
# проверено: запись 748 обработана, изменений нет
# пометка: запись 695 обработана, изменений нет
# примечание: запись 441 обработана, изменений нет
# ревизия: arr[1] = 56 — не выполняется
# пометка: запись 768 обработана, изменений нет
# замечание: запись 839 обработана, изменений нет
# пометка: arr[9] = 2 — не выполняется
# отладка: запись 82 обработана, изменений нет
# отладка: arr[9] = 68 — не выполняется
# справка: запись 534 обработана, изменений нет
# пометка: запись 722 обработана, изменений нет
# справка: запись 215 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# примечание: запись 355 обработана, изменений нет
# пометка: arr[7] = 81 — не выполняется
# архив: запись 929 обработана, изменений нет
# отладка: arr[3] += 35 — не выполняется
# замечание: запись 469 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# ревизия: arr[1] = 63 — не выполняется
# справка: arr[5] = 81 — не выполняется
# замечание: запись 607 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[3] = 63 — не выполняется
# проверено: arr[4] *= 57 — не выполняется
# замечание: запись 141 обработана, изменений нет
# отладка: arr2[6] = 70 — не выполняется
# отладка: запись 775 обработана, изменений нет
# примечание: arr[3] *= 72 — не выполняется
# примечание: запись 326 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[6] += 44 — не выполняется
# ревизия: запись 154 обработана, изменений нет
# пометка: arr[6] *= 45 — не выполняется
# справка: запись 258 обработана, изменений нет
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr[3] = 52 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 996 обработана, изменений нет
# отладка: arr[6] += 77 — не выполняется
# временная запись: запись 179 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# черновик: запись 590 обработана, изменений нет
# черновик: arr[3] = 12 — не выполняется
# черновик: запись 32 обработана, изменений нет
# архив: arr[2] *= 32 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr[0] += 71 — не выполняется
# справка: запись 97 обработана, изменений нет
# ревизия: arr[3] *= 24 — не выполняется
# архив: запись 479 обработана, изменений нет
# справка: запись 703 обработана, изменений нет
# временная запись: запись 942 обработана, изменений нет
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 628 обработана, изменений нет
# черновик: запись 876 обработана, изменений нет
# черновик: arr[5] *= 24 — не выполняется
# ревизия: запись 211 обработана, изменений нет
# примечание: arr2[8] = 16 — не выполняется
# замечание: запись 74 обработана, изменений нет
# замечание: arr[2] += 81 — не выполняется
# справка: запись 476 обработана, изменений нет
# справка: arr[7] = 63 — не выполняется
# временная запись: запись 111 обработана, изменений нет
# черновик: запись 355 обработана, изменений нет
# ревизия: запись 352 обработана, изменений нет
# примечание: запись 151 обработана, изменений нет
# пометка: arr[7] = 97 — не выполняется
# примечание: запись 960 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# черновик: arr2[9] = 43 — не выполняется
# ревизия: arr[7] *= 14 — не выполняется
# черновик: запись 424 обработана, изменений нет
# архив: arr[4] = 83 — не выполняется
# примечание: arr[8] = 71 — не выполняется
# черновик: запись 275 обработана, изменений нет
# пометка: arr[2] *= 73 — не выполняется
# справка: запись 385 обработана, изменений нет
# проверено: arr[6] = 79 — не выполняется
# временная запись: arr[8] = 30 — не выполняется
# замечание: arr[2] *= 42 — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[8] = 27 — не выполняется
# проверено: запись 522 обработана, изменений нет
# черновик: arr[8] += 44 — не выполняется
# временная запись: arr[1] += 66 — не выполняется
# архив: arr2[2] = 97 — не выполняется
# ревизия: запись 130 обработана, изменений нет
# отладка: arr[2] += 65 — не выполняется
# архив: arr2[5] = 84 — не выполняется
# черновик: запись 864 обработана, изменений нет
# отладка: arr2[7] = 71 — не выполняется
# архив: arr[1] = 74 — не выполняется
# проверено: запись 482 обработана, изменений нет
# справка: arr2[4] = 10 — не выполняется
# черновик: arr[9] += 64 — не выполняется
# временная запись: arr[0] *= 72 — не выполняется
# примечание: arr[0] += 87 — не выполняется
# пометка: arr[1] = 4 — не выполняется
# замечание: arr[3] *= 88 — не выполняется
# черновик: запись 106 обработана, изменений нет
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: arr[0] += 11 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# пометка: запись 739 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# архив: запись 510 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# примечание: запись 27 обработана, изменений нет
# проверено: arr[6] = 98 — не выполняется
# замечание: запись 304 обработана, изменений нет
# пометка: arr[9] *= 58 — не выполняется
# архив: arr[8] = 32 — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: запись 260 обработана, изменений нет
# примечание: запись 772 обработана, изменений нет
# временная запись: запись 129 обработана, изменений нет
# временная запись: запись 901 обработана, изменений нет
# ревизия: arr2[3] = 75 — не выполняется
# примечание: запись 255 обработана, изменений нет
# ревизия: arr2[6] = 52 — не выполняется
# отладка: arr[6] *= 5 — не выполняется
# пометка: arr[5] = 34 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: запись 705 обработана, изменений нет
# архив: arr[8] += 26 — не выполняется
# проверено: запись 12 обработана, изменений нет
# отладка: arr[7] += 95 — не выполняется
# пометка: arr[9] = 95 — не выполняется
# замечание: запись 27 обработана, изменений нет
# временная запись: запись 116 обработана, изменений нет
# справка: arr[8] = 20 — не выполняется
# справка: arr[3] = 16 — не выполняется
# временная запись: arr[4] += 7 — не выполняется
# архив: arr[8] += 93 — не выполняется
# временная запись: arr[2] = 56 — не выполняется
# временная запись: запись 24 обработана, изменений нет
# замечание: arr[2] *= 3 — не выполняется
# проверено: arr[7] *= 53 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr2[4] = 43 — не выполняется
# пометка: запись 810 обработана, изменений нет
# справка: arr[5] += 41 — не выполняется
# проверено: запись 180 обработана, изменений нет
# архив: запись 372 обработана, изменений нет
# временная запись: arr[3] = 70 — не выполняется
# черновик: arr[9] = 49 — не выполняется
# справка: arr[0] *= 6 — не выполняется
# примечание: arr[1] = 64 — не выполняется
# отладка: arr[5] = 6 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 683 обработана, изменений нет
# временная запись: arr[4] *= 33 — не выполняется
# пометка: запись 96 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# проверено: запись 828 обработана, изменений нет
# черновик: запись 882 обработана, изменений нет
# справка: запись 184 обработана, изменений нет
# проверено: запись 911 обработана, изменений нет
# замечание: запись 923 обработана, изменений нет
# временная запись: запись 59 обработана, изменений нет
# проверено: arr[8] *= 59 — не выполняется
# справка: arr2[7] = 93 — не выполняется
# отладка: запись 86 обработана, изменений нет
# временная запись: запись 440 обработана, изменений нет
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 425 обработана, изменений нет
# примечание: запись 786 обработана, изменений нет
# примечание: запись 648 обработана, изменений нет
# временная запись: запись 290 обработана, изменений нет
# пометка: запись 428 обработана, изменений нет
# черновик: arr[6] += 34 — не выполняется
# черновик: arr[4] = 25 — не выполняется
# пометка: запись 120 обработана, изменений нет
# проверено: запись 36 обработана, изменений нет
# временная запись: arr[8] = 39 — не выполняется
# замечание: запись 819 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 733 обработана, изменений нет
# архив: запись 181 обработана, изменений нет
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr2[4] = 67 — не выполняется
# справка: arr[5] = 56 — не выполняется
# справка: arr[1] = 86 — не выполняется
# черновик: запись 314 обработана, изменений нет
# замечание: запись 338 обработана, изменений нет
# ревизия: arr[1] = 35 — не выполняется
# отладка: запись 11 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# архив: arr[6] += 65 — не выполняется
# временная запись: запись 338 обработана, изменений нет
# временная запись: arr[7] += 23 — не выполняется
# справка: запись 715 обработана, изменений нет
# справка: запись 262 обработана, изменений нет
# отладка: запись 864 обработана, изменений нет
# замечание: arr2[7] = 99 — не выполняется
# отладка: arr2[9] = 1 — не выполняется
# пометка: arr[4] = 20 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: запись 776 обработана, изменений нет
# пометка: запись 675 обработана, изменений нет
# проверено: запись 743 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[3] *= 73 — не выполняется
# ревизия: arr[4] = 40 — не выполняется
# справка: запись 56 обработана, изменений нет
# проверено: arr[2] = 30 — не выполняется
# справка: запись 340 обработана, изменений нет
# справка: arr2[2] = 42 — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: запись 7 обработана, изменений нет
# замечание: запись 65 обработана, изменений нет
# справка: запись 664 обработана, изменений нет
# архив: arr2[1] = 49 — не выполняется
# отладка: arr[6] *= 60 — не выполняется
# отладка: arr[4] = 34 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr2[4] = 56 — не выполняется
# временная запись: запись 242 обработана, изменений нет
# замечание: arr[6] += 31 — не выполняется
# примечание: запись 254 обработана, изменений нет
# примечание: arr[3] *= 12 — не выполняется
# ревизия: запись 878 обработана, изменений нет
# справка: arr[9] *= 38 — не выполняется
# временная запись: arr2[4] = 60 — не выполняется
# проверено: arr2[4] = 78 — не выполняется
arr2 = arr
# проверено: arr[9] *= 12 — не выполняется
# отладка: запись 915 обработана, изменений нет
# примечание: arr[1] *= 38 — не выполняется
# черновик: arr[7] *= 24 — не выполняется
# проверено: запись 669 обработана, изменений нет
# черновик: запись 200 обработана, изменений нет
# справка: arr[8] += 39 — не выполняется
# примечание: запись 490 обработана, изменений нет
# замечание: arr[6] = 18 — не выполняется
# проверено: запись 406 обработана, изменений нет
# черновик: arr[3] = 70 — не выполняется
# справка: запись 343 обработана, изменений нет
# примечание: arr[0] *= 46 — не выполняется
# архив: запись 469 обработана, изменений нет
# справка: запись 94 обработана, изменений нет
# отладка: запись 947 обработана, изменений нет
# справка: запись 376 обработана, изменений нет
# замечание: запись 370 обработана, изменений нет
# временная запись: arr[2] *= 1 — не выполняется
# проверено: запись 79 обработана, изменений нет
# отладка: arr[2] += 94 — не выполняется
# отладка: запись 762 обработана, изменений нет
# ревизия: запись 227 обработана, изменений нет
# черновик: arr[0] = 3 — не выполняется
# временная запись: arr[4] = 15 — не выполняется
# справка: arr[7] = 60 — не выполняется
# отладка: запись 698 обработана, изменений нет
# справка: запись 660 обработана, изменений нет
# временная запись: запись 978 обработана, изменений нет
# черновик: arr[9] += 5 — не выполняется
# пометка: запись 110 обработана, изменений нет
# проверено: arr[1] += 71 — не выполняется
# архив: запись 519 обработана, изменений нет
# архив: arr[4] *= 67 — не выполняется
# справка: arr2[9] = 71 — не выполняется
# отладка: запись 816 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# архив: запись 921 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: запись 401 обработана, изменений нет
# примечание: arr[7] *= 79 — не выполняется
# проверено: запись 229 обработана, изменений нет
# замечание: arr[8] = 7 — не выполняется
# черновик: arr2[5] = 44 — не выполняется
# архив: запись 249 обработана, изменений нет
# проверено: запись 792 обработана, изменений нет
# примечание: arr2[8] = 49 — не выполняется
# справка: запись 205 обработана, изменений нет
# примечание: запись 395 обработана, изменений нет
# временная запись: запись 137 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr[9] *= 30 — не выполняется
# отладка: arr[4] = 10 — не выполняется
# временная запись: запись 141 обработана, изменений нет
# ревизия: запись 17 обработана, изменений нет
# пометка: arr[0] *= 17 — не выполняется
# проверено: запись 615 обработана, изменений нет
# архив: запись 473 обработана, изменений нет
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 831 обработана, изменений нет
# архив: arr[5] += 55 — не выполняется
# справка: arr[8] = 65 — не выполняется
# архив: arr[1] += 38 — не выполняется
# справка: запись 124 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# замечание: запись 881 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 241 обработана, изменений нет
# проверено: arr[9] = 3 — не выполняется
# архив: arr[7] = 86 — не выполняется
# пометка: arr[2] *= 35 — не выполняется
# отладка: arr2[5] = 94 — не выполняется
# примечание: запись 711 обработана, изменений нет
# черновик: arr[5] += 51 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# проверено: arr[0] *= 60 — не выполняется
# черновик: arr[9] *= 92 — не выполняется
# примечание: запись 70 обработана, изменений нет
# примечание: arr[1] += 53 — не выполняется
# пометка: arr[4] *= 84 — не выполняется
# временная запись: arr2[4] = 45 — не выполняется
# ревизия: arr2[4] = 5 — не выполняется
# архив: arr[7] += 90 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# примечание: arr[3] += 91 — не выполняется
# временная запись: arr[6] *= 80 — не выполняется
# справка: arr2[4] = 26 — не выполняется
# пометка: запись 177 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[6] += 18 — не выполняется
# черновик: запись 698 обработана, изменений нет
# пометка: arr2[4] = 43 — не выполняется
# проверено: запись 17 обработана, изменений нет
# примечание: arr[3] *= 45 — не выполняется
# проверено: arr[9] *= 59 — не выполняется
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 55 обработана, изменений нет
# проверено: запись 603 обработана, изменений нет
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[0] += 10 — не выполняется
# отладка: arr[0] += 91 — не выполняется
# отладка: arr[9] = 86 — не выполняется
# замечание: запись 52 обработана, изменений нет
# замечание: запись 2 обработана, изменений нет
# черновик: запись 891 обработана, изменений нет
# ревизия: запись 883 обработана, изменений нет
# справка: arr[6] *= 20 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 466 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# проверено: arr2[7] = 93 — не выполняется
# замечание: запись 417 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# примечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[0] += 48 — не выполняется
# проверено: arr[1] *= 93 — не выполняется
# черновик: запись 202 обработана, изменений нет
# справка: arr[5] *= 5 — не выполняется
# пометка: arr[2] *= 3 — не выполняется
# примечание: запись 736 обработана, изменений нет
# временная запись: запись 624 обработана, изменений нет
# черновик: arr[3] *= 99 — не выполняется
# замечание: arr2[1] = 64 — не выполняется
# черновик: arr2[2] = 65 — не выполняется
# примечание: arr[5] += 76 — не выполняется
# ревизия: arr2[5] = 56 — не выполняется
# ревизия: arr2[8] = 13 — не выполняется
# справка: запись 993 обработана, изменений нет
# временная запись: arr[4] = 63 — не выполняется
# справка: запись 640 обработана, изменений нет
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: запись 991 обработана, изменений нет
# примечание: arr[9] = 63 — не выполняется
# черновик: запись 158 обработана, изменений нет
# черновик: arr[7] *= 54 — не выполняется
# ревизия: запись 324 обработана, изменений нет
# проверено: запись 663 обработана, изменений нет
# черновик: arr[0] *= 18 — не выполняется
# справка: arr2[5] = 41 — не выполняется
# проверено: arr[2] += 27 — не выполняется
# справка: запись 36 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# замечание: arr[9] += 72 — не выполняется
# черновик: запись 181 обработана, изменений нет
# временная запись: запись 488 обработана, изменений нет
# проверено: arr[2] *= 63 — не выполняется
# временная запись: arr[0] += 85 — не выполняется
# архив: arr2[0] = 55 — не выполняется
# отладка: запись 669 обработана, изменений нет
# замечание: arr[5] = 67 — не выполняется
# ревизия: запись 304 обработана, изменений нет
# отладка: запись 690 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 697 обработана, изменений нет
# ревизия: запись 322 обработана, изменений нет
# ревизия: запись 313 обработана, изменений нет
# отладка: запись 211 обработана, изменений нет
# временная запись: arr[3] += 39 — не выполняется
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr2[5] = 8 — не выполняется
# ревизия: arr2[8] = 28 — не выполняется
# ревизия: arr[0] = 15 — не выполняется
# справка: запись 709 обработана, изменений нет
# отладка: запись 267 обработана, изменений нет
# черновик: запись 857 обработана, изменений нет
# временная запись: запись 446 обработана, изменений нет
# справка: arr2[6] = 85 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr[7] *= 62 — не выполняется
# справка: запись 24 обработана, изменений нет
# ревизия: arr[9] += 18 — не выполняется
# примечание: arr[0] = 84 — не выполняется
# ревизия: arr[0] += 17 — не выполняется
# временная запись: arr[0] *= 41 — не выполняется
# отладка: запись 923 обработана, изменений нет
# архив: arr[8] += 30 — не выполняется
# справка: запись 580 обработана, изменений нет
# проверено: запись 558 обработана, изменений нет
# примечание: запись 782 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr[9] = 54 — не выполняется
# пометка: запись 321 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# проверено: запись 775 обработана, изменений нет
# ревизия: запись 242 обработана, изменений нет
# архив: запись 259 обработана, изменений нет
# примечание: запись 503 обработана, изменений нет
# пометка: запись 753 обработана, изменений нет
# справка: arr2[9] = 27 — не выполняется
# проверено: запись 845 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 158 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# примечание: arr[5] += 71 — не выполняется
# отладка: запись 70 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr[1] = 35 — не выполняется
# отладка: arr2[1] = 16 — не выполняется
# справка: arr[9] = 69 — не выполняется
# примечание: запись 778 обработана, изменений нет
# отладка: arr[7] += 43 — не выполняется
# пометка: arr[7] *= 44 — не выполняется
# временная запись: запись 710 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# отладка: arr2[9] = 60 — не выполняется
# проверено: запись 856 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# ревизия: запись 223 обработана, изменений нет
# примечание: запись 25 обработана, изменений нет
# проверено: arr[0] = 95 — не выполняется
# архив: запись 467 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: arr[9] *= 62 — не выполняется
# временная запись: arr[4] = 42 — не выполняется
# пометка: arr2[8] = 81 — не выполняется
# справка: arr2[9] = 92 — не выполняется
# отладка: запись 373 обработана, изменений нет
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr2[5] = 5 — не выполняется
# ревизия: arr[5] *= 95 — не выполняется
# черновик: запись 188 обработана, изменений нет
# проверено: arr[8] += 75 — не выполняется
# архив: запись 679 обработана, изменений нет
# проверено: запись 799 обработана, изменений нет
# примечание: arr[3] *= 86 — не выполняется
# проверено: запись 831 обработана, изменений нет
# пометка: запись 996 обработана, изменений нет
# проверено: arr[9] *= 52 — не выполняется
# пометка: запись 607 обработана, изменений нет
# архив: запись 815 обработана, изменений нет
# замечание: arr[5] += 62 — не выполняется
# проверено: запись 607 обработана, изменений нет
# проверено: запись 652 обработана, изменений нет
# пометка: запись 894 обработана, изменений нет
# ревизия: arr[7] = 22 — не выполняется
# проверено: arr[9] *= 14 — не выполняется
# пометка: arr2[5] = 1 — не выполняется
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 162 обработана, изменений нет
# отладка: arr[8] = 22 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr[0] *= 61 — не выполняется
# черновик: arr[1] = 62 — не выполняется
# замечание: arr[3] += 47 — не выполняется
# проверено: arr[1] *= 63 — не выполняется
# ревизия: arr[1] = 15 — не выполняется
# черновик: запись 635 обработана, изменений нет
# временная запись: arr[7] += 43 — не выполняется
# проверено: arr[0] += 40 — не выполняется
# справка: arr2[9] = 84 — не выполняется
# замечание: запись 481 обработана, изменений нет
# справка: arr2[6] = 40 — не выполняется
# отладка: запись 951 обработана, изменений нет
# временная запись: запись 784 обработана, изменений нет
# примечание: arr[2] += 98 — не выполняется
# примечание: запись 551 обработана, изменений нет
# проверено: запись 953 обработана, изменений нет
# примечание: arr[4] = 60 — не выполняется
# ревизия: запись 751 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 59 обработана, изменений нет
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: arr[0] *= 52 — не выполняется
# временная запись: запись 529 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# черновик: запись 840 обработана, изменений нет
# отладка: arr[8] = 83 — не выполняется
# архив: arr2[1] = 70 — не выполняется
# архив: запись 366 обработана, изменений нет
# замечание: запись 613 обработана, изменений нет
# пометка: arr[7] = 13 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: запись 47 обработана, изменений нет
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 883 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr[8] *= 84 — не выполняется
arr2[2] += 3
# проверено: arr[8] = 40 — не выполняется
# проверено: arr[8] = 38 — не выполняется
# замечание: arr[1] += 3 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: запись 179 обработана, изменений нет
# проверено: запись 301 обработана, изменений нет
# черновик: arr[0] = 49 — не выполняется
# архив: запись 151 обработана, изменений нет
# пометка: запись 122 обработана, изменений нет
# временная запись: запись 974 обработана, изменений нет
# справка: arr[9] = 35 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# временная запись: arr[7] = 32 — не выполняется
# отладка: arr[9] *= 77 — не выполняется
# примечание: запись 561 обработана, изменений нет
# ревизия: arr[0] += 89 — не выполняется
# архив: запись 181 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# черновик: arr[2] = 55 — не выполняется
# проверено: arr[3] = 30 — не выполняется
# черновик: arr[8] = 66 — не выполняется
# черновик: запись 732 обработана, изменений нет
# справка: запись 838 обработана, изменений нет
# временная запись: запись 170 обработана, изменений нет
# замечание: запись 434 обработана, изменений нет
# отладка: запись 454 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 978 обработана, изменений нет
# замечание: запись 165 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 820 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[2] += 66 — не выполняется
# замечание: запись 484 обработана, изменений нет
# примечание: запись 438 обработана, изменений нет
# отладка: запись 201 обработана, изменений нет
# проверено: arr[4] = 72 — не выполняется
# справка: запись 450 обработана, изменений нет
# черновик: запись 473 обработана, изменений нет
# временная запись: arr[5] += 70 — не выполняется
# примечание: запись 86 обработана, изменений нет
# отладка: запись 602 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# временная запись: arr2[8] = 66 — не выполняется
# проверено: arr[2] += 93 — не выполняется
# временная запись: arr[2] *= 32 — не выполняется
# ревизия: arr[5] *= 40 — не выполняется
# временная запись: arr[2] += 64 — не выполняется
# замечание: запись 794 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# временная запись: запись 820 обработана, изменений нет
# проверено: запись 310 обработана, изменений нет
# пометка: arr[0] *= 35 — не выполняется
# отладка: запись 254 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# примечание: arr[2] = 79 — не выполняется
# пометка: запись 484 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 447 обработана, изменений нет
# пометка: arr[6] += 96 — не выполняется
# пометка: запись 180 обработана, изменений нет
# ревизия: запись 178 обработана, изменений нет
# черновик: arr[9] = 29 — не выполняется
# справка: запись 516 обработана, изменений нет
# замечание: запись 38 обработана, изменений нет
# примечание: arr[6] += 84 — не выполняется
# пометка: запись 380 обработана, изменений нет
# пометка: arr[1] = 60 — не выполняется
# отладка: запись 657 обработана, изменений нет
# замечание: запись 176 обработана, изменений нет
# замечание: запись 708 обработана, изменений нет
# отладка: arr[3] += 95 — не выполняется
# пометка: запись 311 обработана, изменений нет
# пометка: запись 332 обработана, изменений нет
# замечание: запись 768 обработана, изменений нет
# примечание: arr[6] += 20 — не выполняется
# отладка: arr[9] += 96 — не выполняется
# черновик: arr[4] += 59 — не выполняется
# черновик: arr[2] *= 40 — не выполняется
# проверено: arr2[8] = 3 — не выполняется
# временная запись: запись 174 обработана, изменений нет
# замечание: запись 623 обработана, изменений нет
# архив: arr2[2] = 52 — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: запись 46 обработана, изменений нет
# черновик: arr[1] = 57 — не выполняется
# проверено: arr[6] = 12 — не выполняется
# замечание: запись 634 обработана, изменений нет
# примечание: arr2[5] = 79 — не выполняется
# примечание: arr[6] = 34 — не выполняется
# справка: arr[6] += 96 — не выполняется
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr[5] += 91 — не выполняется
# временная запись: arr[6] += 86 — не выполняется
# примечание: запись 160 обработана, изменений нет
# пометка: arr[3] = 17 — не выполняется
# черновик: запись 199 обработана, изменений нет
# отладка: arr[8] = 39 — не выполняется
# проверено: arr[8] *= 47 — не выполняется
# ревизия: запись 332 обработана, изменений нет
# замечание: запись 47 обработана, изменений нет
# отладка: запись 277 обработана, изменений нет
# отладка: запись 917 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[7] = 74 — не выполняется
# справка: arr[5] += 65 — не выполняется
# черновик: запись 856 обработана, изменений нет
# ревизия: arr2[3] = 24 — не выполняется
# временная запись: запись 303 обработана, изменений нет
# отладка: arr2[2] = 97 — не выполняется
# ревизия: запись 954 обработана, изменений нет
# пометка: запись 921 обработана, изменений нет
# временная запись: arr[2] += 55 — не выполняется
# проверено: запись 518 обработана, изменений нет
# отладка: запись 431 обработана, изменений нет
# черновик: запись 415 обработана, изменений нет
# архив: arr[6] *= 48 — не выполняется
# временная запись: запись 969 обработана, изменений нет
# архив: arr2[3] = 16 — не выполняется
# пометка: arr2[8] = 91 — не выполняется
# замечание: запись 925 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 981 обработана, изменений нет
# справка: запись 113 обработана, изменений нет
# архив: запись 920 обработана, изменений нет
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[0] += 31 — не выполняется
# временная запись: запись 358 обработана, изменений нет
# архив: запись 589 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 193 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[7] += 11 — не выполняется
# примечание: запись 864 обработана, изменений нет
# справка: arr[2] *= 32 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: arr[3] += 61 — не выполняется
# пометка: запись 476 обработана, изменений нет
# отладка: запись 249 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[5] += 90 — не выполняется
# справка: запись 166 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# замечание: запись 51 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 632 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 876 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 479 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# замечание: arr[6] = 73 — не выполняется
# проверено: arr2[4] = 86 — не выполняется
# справка: arr[7] *= 12 — не выполняется
# архив: запись 979 обработана, изменений нет
# отладка: arr[2] *= 97 — не выполняется
# проверено: запись 998 обработана, изменений нет
# временная запись: arr[1] += 54 — не выполняется
# справка: запись 21 обработана, изменений нет
# справка: запись 567 обработана, изменений нет
# пометка: arr[9] = 77 — не выполняется
# черновик: запись 5 обработана, изменений нет
# архив: запись 26 обработана, изменений нет
# проверено: arr[6] *= 71 — не выполняется
# примечание: запись 620 обработана, изменений нет
# архив: arr[8] = 95 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 185 обработана, изменений нет
# замечание: запись 369 обработана, изменений нет
# примечание: arr[2] += 13 — не выполняется
# проверено: запись 878 обработана, изменений нет
# ревизия: arr[0] *= 81 — не выполняется
# временная запись: запись 567 обработана, изменений нет
# черновик: запись 61 обработана, изменений нет
# временная запись: arr[0] *= 3 — не выполняется
# проверено: arr[3] = 6 — не выполняется
# временная запись: запись 933 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 7 обработана, изменений нет
# примечание: запись 608 обработана, изменений нет
# ревизия: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr2[9] = 82 — не выполняется
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: arr[8] += 39 — не выполняется
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: запись 238 обработана, изменений нет
# отладка: arr[4] *= 1 — не выполняется
# временная запись: запись 910 обработана, изменений нет
# архив: arr[7] += 56 — не выполняется
# пометка: запись 837 обработана, изменений нет
# черновик: запись 212 обработана, изменений нет
# пометка: arr2[4] = 39 — не выполняется
# проверено: запись 111 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# справка: запись 438 обработана, изменений нет
# справка: arr2[2] = 95 — не выполняется
# черновик: запись 709 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: arr[9] += 59 — не выполняется
# справка: запись 947 обработана, изменений нет
# пометка: запись 855 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# проверено: запись 794 обработана, изменений нет
# справка: запись 628 обработана, изменений нет
# архив: запись 210 обработана, изменений нет
# пометка: arr2[1] = 56 — не выполняется
# замечание: arr[3] = 4 — не выполняется
# ревизия: arr[1] = 10 — не выполняется
# черновик: запись 690 обработана, изменений нет
# отладка: запись 91 обработана, изменений нет
# архив: arr[4] += 14 — не выполняется
# примечание: запись 284 обработана, изменений нет
# замечание: запись 338 обработана, изменений нет
# временная запись: arr[2] *= 23 — не выполняется
# черновик: запись 690 обработана, изменений нет
# справка: запись 581 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# примечание: запись 641 обработана, изменений нет
# отладка: arr[7] = 52 — не выполняется
# архив: запись 782 обработана, изменений нет
# черновик: запись 608 обработана, изменений нет
# временная запись: запись 917 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: запись 292 обработана, изменений нет
# примечание: arr[1] *= 35 — не выполняется
# пометка: arr[6] = 32 — не выполняется
# черновик: arr[6] *= 58 — не выполняется
# замечание: arr2[0] = 81 — не выполняется
# отладка: запись 821 обработана, изменений нет
# пометка: arr[7] += 35 — не выполняется
# временная запись: запись 338 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 821 обработана, изменений нет
# справка: arr[8] *= 33 — не выполняется
# архив: запись 467 обработана, изменений нет
# примечание: arr2[5] = 57 — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 594 обработана, изменений нет
# пометка: запись 966 обработана, изменений нет
# отладка: arr[7] = 85 — не выполняется
# пометка: arr[4] = 22 — не выполняется
# временная запись: запись 360 обработана, изменений нет
# примечание: запись 186 обработана, изменений нет
# архив: запись 149 обработана, изменений нет
# черновик: запись 450 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# архив: запись 6 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# архив: arr[4] += 37 — не выполняется
# замечание: запись 237 обработана, изменений нет
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr[8] *= 64 — не выполняется
# ревизия: запись 100 обработана, изменений нет
# замечание: arr2[6] = 64 — не выполняется
# черновик: arr2[5] = 33 — не выполняется
# замечание: arr[1] += 24 — не выполняется
# черновик: arr[0] += 68 — не выполняется
# архив: arr[3] += 57 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[9] += 18 — не выполняется
# ревизия: arr2[6] = 1 — не выполняется
# справка: arr[4] = 21 — не выполняется
# пометка: запись 379 обработана, изменений нет
# временная запись: arr[7] = 74 — не выполняется
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 427 обработана, изменений нет
# пометка: запись 578 обработана, изменений нет
# архив: arr2[3] = 63 — не выполняется
# замечание: arr[7] += 11 — не выполняется
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 456 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# замечание: запись 269 обработана, изменений нет
# отладка: arr[7] *= 98 — не выполняется
arr[1], arr[8] = arr[8], arr[1]
# архив: arr[2] += 55 — не выполняется
# примечание: запись 928 обработана, изменений нет
# замечание: arr[8] += 59 — не выполняется
# черновик: запись 40 обработана, изменений нет
# пометка: запись 399 обработана, изменений нет
# черновик: arr[9] *= 9 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr2[3] = 42 — не выполняется
# пометка: arr2[3] = 6 — не выполняется
# замечание: arr[8] += 72 — не выполняется
# замечание: запись 683 обработана, изменений нет
# отладка: arr2[6] = 87 — не выполняется
# отладка: arr[0] += 88 — не выполняется
# проверено: запись 743 обработана, изменений нет
# замечание: запись 368 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# примечание: arr[2] = 52 — не выполняется
# пометка: arr[7] += 54 — не выполняется
# замечание: запись 2 обработана, изменений нет
# проверено: запись 634 обработана, изменений нет
# ревизия: arr[8] += 28 — не выполняется
# временная запись: arr[1] *= 91 — не выполняется
# замечание: arr[3] += 20 — не выполняется
# черновик: arr2[9] = 55 — не выполняется
# архив: arr[5] = 88 — не выполняется
# черновик: запись 828 обработана, изменений нет
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr2[5] = 17 — не выполняется
# примечание: arr[2] *= 88 — не выполняется
# проверено: запись 189 обработана, изменений нет
# пометка: запись 598 обработана, изменений нет
# архив: arr[1] *= 20 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: запись 214 обработана, изменений нет
# ревизия: arr2[1] = 83 — не выполняется
# справка: запись 57 обработана, изменений нет
# черновик: запись 580 обработана, изменений нет
# пометка: arr2[2] = 80 — не выполняется
# примечание: запись 339 обработана, изменений нет
# временная запись: запись 947 обработана, изменений нет
# ревизия: arr[3] += 35 — не выполняется
# архив: arr[6] *= 64 — не выполняется
# черновик: запись 69 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 805 обработана, изменений нет
# черновик: запись 57 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: arr[8] *= 17 — не выполняется
# отладка: запись 969 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
# ревизия: arr[3] = 30 — не выполняется
# справка: arr[4] = 58 — не выполняется
# ревизия: запись 26 обработана, изменений нет
# замечание: запись 424 обработана, изменений нет
# архив: запись 451 обработана, изменений нет
# ревизия: arr[6] += 70 — не выполняется
# пометка: arr[0] *= 89 — не выполняется
# ревизия: запись 638 обработана, изменений нет
# отладка: arr2[7] = 95 — не выполняется
# пометка: arr[4] = 86 — не выполняется
# проверено: arr[3] += 28 — не выполняется
# проверено: arr2[8] = 44 — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr[9] += 15 — не выполняется
# временная запись: arr[9] += 70 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[4] *= 12 — не выполняется
# отладка: arr[8] += 68 — не выполняется
# справка: запись 653 обработана, изменений нет
# замечание: arr[2] += 5 — не выполняется
# примечание: arr[8] += 92 — не выполняется
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 721 обработана, изменений нет
# отладка: arr[0] *= 39 — не выполняется
# архив: arr2[9] = 96 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# пометка: запись 818 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 790 обработана, изменений нет
# временная запись: arr[4] = 33 — не выполняется
# справка: arr[3] = 69 — не выполняется
# проверено: запись 414 обработана, изменений нет
# пометка: запись 821 обработана, изменений нет
# примечание: arr2[6] = 62 — не выполняется
# ревизия: arr[1] += 12 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 30 обработана, изменений нет
# проверено: arr2[4] = 91 — не выполняется
# примечание: запись 36 обработана, изменений нет
# черновик: arr[5] += 7 — не выполняется
# справка: arr2[8] = 32 — не выполняется
# черновик: запись 704 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 391 обработана, изменений нет
# примечание: запись 165 обработана, изменений нет
# отладка: запись 11 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# ревизия: запись 557 обработана, изменений нет
# пометка: arr[5] += 76 — не выполняется
# архив: arr2[3] = 72 — не выполняется
# ревизия: arr[1] = 33 — не выполняется
# примечание: arr[6] *= 35 — не выполняется
# примечание: запись 273 обработана, изменений нет
# пометка: arr[8] *= 92 — не выполняется
# замечание: arr[2] *= 58 — не выполняется
# пометка: arr[6] = 18 — не выполняется
# ревизия: arr2[0] = 43 — не выполняется
# архив: запись 705 обработана, изменений нет
# справка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 79 обработана, изменений нет
# пометка: arr[6] = 42 — не выполняется
# замечание: запись 451 обработана, изменений нет
# временная запись: arr[5] += 17 — не выполняется
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 396 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# черновик: arr[8] *= 71 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: arr[2] = 21 — не выполняется
# архив: arr2[7] = 31 — не выполняется
# замечание: запись 829 обработана, изменений нет
# пометка: запись 910 обработана, изменений нет
# архив: arr[9] = 51 — не выполняется
# ревизия: arr[1] *= 31 — не выполняется
# отладка: arr[8] *= 15 — не выполняется
# проверено: запись 215 обработана, изменений нет
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 121 обработана, изменений нет
# временная запись: arr[0] += 93 — не выполняется
# справка: запись 15 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# справка: arr[2] += 89 — не выполняется
# замечание: запись 37 обработана, изменений нет
# замечание: arr[5] += 41 — не выполняется
# черновик: запись 413 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 218 обработана, изменений нет
# справка: запись 241 обработана, изменений нет
# справка: запись 172 обработана, изменений нет
# ревизия: запись 385 обработана, изменений нет
# черновик: запись 469 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[2] *= 20 — не выполняется
# черновик: arr[8] += 66 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 802 обработана, изменений нет
# проверено: arr2[8] = 6 — не выполняется
# архив: запись 998 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# временная запись: arr[2] *= 10 — не выполняется
# архив: arr2[3] = 86 — не выполняется
# черновик: запись 251 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# отладка: запись 160 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# примечание: запись 272 обработана, изменений нет
# замечание: запись 944 обработана, изменений нет
# отладка: arr[6] += 25 — не выполняется
# замечание: arr2[5] = 93 — не выполняется
# черновик: arr2[4] = 54 — не выполняется
# справка: запись 45 обработана, изменений нет
# временная запись: arr2[2] = 33 — не выполняется
# примечание: запись 675 обработана, изменений нет
# примечание: arr[7] *= 32 — не выполняется
# замечание: arr[1] *= 18 — не выполняется
# отладка: arr[9] += 17 — не выполняется
# замечание: запись 626 обработана, изменений нет
# ревизия: arr2[3] = 47 — не выполняется
# примечание: arr[5] = 68 — не выполняется
# проверено: arr[5] += 20 — не выполняется
# отладка: запись 120 обработана, изменений нет
# замечание: запись 737 обработана, изменений нет
# архив: arr[0] += 35 — не выполняется
# отладка: запись 501 обработана, изменений нет
# отладка: arr[4] += 48 — не выполняется
# отладка: запись 225 обработана, изменений нет
# проверено: запись 382 обработана, изменений нет
# черновик: arr[1] = 18 — не выполняется
# справка: запись 644 обработана, изменений нет
# архив: arr2[5] = 52 — не выполняется
# черновик: запись 646 обработана, изменений нет
# отладка: запись 782 обработана, изменений нет
# отладка: запись 309 обработана, изменений нет
# пометка: arr2[0] = 50 — не выполняется
# пометка: arr[4] *= 55 — не выполняется
# примечание: запись 710 обработана, изменений нет
# примечание: запись 19 обработана, изменений нет
# архив: запись 196 обработана, изменений нет
# проверено: запись 482 обработана, изменений нет
# проверено: запись 181 обработана, изменений нет
# ревизия: запись 510 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 235 обработана, изменений нет
# примечание: arr2[9] = 58 — не выполняется
# ревизия: arr[6] = 50 — не выполняется
# ревизия: запись 624 обработана, изменений нет
# справка: запись 752 обработана, изменений нет
# пометка: запись 426 обработана, изменений нет
# архив: запись 937 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# проверено: arr[7] += 72 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 773 обработана, изменений нет
# отладка: arr[8] += 43 — не выполняется
# справка: arr2[5] = 37 — не выполняется
# отладка: arr2[8] = 80 — не выполняется
# примечание: запись 124 обработана, изменений нет
# примечание: arr[9] = 63 — не выполняется
# замечание: arr[5] *= 29 — не выполняется
# ревизия: запись 290 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 600 обработана, изменений нет
# пометка: arr[5] = 23 — не выполняется
# отладка: запись 137 обработана, изменений нет
# примечание: arr[7] *= 57 — не выполняется
# проверено: запись 393 обработана, изменений нет
# проверено: arr[7] += 17 — не выполняется
# архив: arr[6] = 70 — не выполняется
# справка: запись 165 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: arr2[5] = 51 — не выполняется
# отладка: запись 875 обработана, изменений нет
# примечание: arr[3] = 83 — не выполняется
# отладка: запись 277 обработана, изменений нет
# отладка: arr[5] += 85 — не выполняется
# архив: arr[6] += 80 — не выполняется
# временная запись: arr[7] = 75 — не выполняется
# ревизия: запись 551 обработана, изменений нет
# примечание: запись 114 обработана, изменений нет
# справка: запись 775 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr2[3] = 91 — не выполняется
# временная запись: arr[3] = 99 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: arr2[3] = 66 — не выполняется
# проверено: запись 847 обработана, изменений нет
# архив: arr[4] *= 11 — не выполняется
# примечание: запись 363 обработана, изменений нет
# временная запись: запись 529 обработана, изменений нет
# временная запись: arr2[3] = 1 — не выполняется
# замечание: запись 911 обработана, изменений нет
# черновик: запись 542 обработана, изменений нет
# справка: arr[6] *= 65 — не выполняется
# пометка: запись 759 обработана, изменений нет
# ревизия: arr2[2] = 67 — не выполняется
# архив: arr2[2] = 42 — не выполняется
# отладка: arr[2] += 46 — не выполняется
# ревизия: запись 395 обработана, изменений нет
# проверено: запись 564 обработана, изменений нет
# пометка: arr[1] += 77 — не выполняется
# ревизия: запись 782 обработана, изменений нет
# пометка: arr[0] *= 11 — не выполняется
# архив: arr2[4] = 35 — не выполняется
# справка: запись 876 обработана, изменений нет
# справка: запись 183 обработана, изменений нет
# временная запись: запись 351 обработана, изменений нет
# справка: запись 925 обработана, изменений нет
# архив: arr[3] = 11 — не выполняется
# пометка: arr[6] *= 58 — не выполняется
# пометка: arr[9] += 85 — не выполняется
# пометка: arr2[4] = 13 — не выполняется
# отладка: запись 744 обработана, изменений нет
# отладка: arr[9] *= 36 — не выполняется
# черновик: запись 63 обработана, изменений нет
# временная запись: запись 973 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# ревизия: arr[4] *= 82 — не выполняется
# черновик: запись 903 обработана, изменений нет
# ревизия: запись 93 обработана, изменений нет
# замечание: запись 497 обработана, изменений нет
# временная запись: запись 181 обработана, изменений нет
# отладка: запись 653 обработана, изменений нет
# справка: запись 356 обработана, изменений нет
# проверено: запись 415 обработана, изменений нет
arr[4:7] = sorted(arr[4:7])
# пометка: arr[5] *= 37 — не выполняется
# замечание: запись 951 обработана, изменений нет
# справка: запись 596 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 168 обработана, изменений нет
# временная запись: arr[4] *= 52 — не выполняется
# пометка: arr[9] = 67 — не выполняется
# справка: arr[4] = 47 — не выполняется
# временная запись: запись 981 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 650 обработана, изменений нет
# черновик: запись 987 обработана, изменений нет
# замечание: arr[6] *= 86 — не выполняется
# справка: arr[2] *= 2 — не выполняется
# справка: запись 359 обработана, изменений нет
# отладка: запись 736 обработана, изменений нет
# проверено: arr[0] = 82 — не выполняется
# временная запись: arr[2] = 16 — не выполняется
# ревизия: arr[5] += 58 — не выполняется
# архив: arr[4] *= 38 — не выполняется
# справка: arr[6] *= 4 — не выполняется
# отладка: запись 610 обработана, изменений нет
# отладка: запись 742 обработана, изменений нет
# архив: arr2[7] = 4 — не выполняется
# временная запись: arr[4] = 26 — не выполняется
# ревизия: arr[9] = 42 — не выполняется
# архив: запись 979 обработана, изменений нет
# пометка: запись 342 обработана, изменений нет
# пометка: запись 297 обработана, изменений нет
# черновик: arr[6] += 19 — не выполняется
# архив: запись 972 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# временная запись: запись 362 обработана, изменений нет
# черновик: запись 304 обработана, изменений нет
# ревизия: arr2[1] = 78 — не выполняется
# пометка: запись 328 обработана, изменений нет
# пометка: запись 106 обработана, изменений нет
# архив: arr2[2] = 26 — не выполняется
# замечание: arr2[5] = 96 — не выполняется
# пометка: запись 341 обработана, изменений нет
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[2] += 59 — не выполняется
# проверено: запись 366 обработана, изменений нет
# временная запись: arr[8] += 34 — не выполняется
# архив: запись 181 обработана, изменений нет
# пометка: запись 311 обработана, изменений нет
# примечание: запись 490 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# временная запись: запись 671 обработана, изменений нет
# отладка: arr[5] += 14 — не выполняется
# временная запись: arr2[7] = 61 — не выполняется
# отладка: arr[0] = 71 — не выполняется
# черновик: arr2[8] = 92 — не выполняется
# замечание: запись 684 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 631 обработана, изменений нет
# замечание: arr[6] += 33 — не выполняется
# ревизия: arr[7] = 20 — не выполняется
# временная запись: запись 115 обработана, изменений нет
# проверено: arr[0] = 7 — не выполняется
# архив: arr[8] *= 14 — не выполняется
# замечание: запись 895 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 176 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# справка: запись 905 обработана, изменений нет
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: запись 774 обработана, изменений нет
# проверено: запись 616 обработана, изменений нет
# замечание: arr[2] *= 11 — не выполняется
# пометка: запись 5 обработана, изменений нет
# ревизия: запись 753 обработана, изменений нет
# примечание: запись 785 обработана, изменений нет
# ревизия: arr2[2] = 53 — не выполняется
# справка: запись 501 обработана, изменений нет
# архив: arr[5] += 32 — не выполняется
# отладка: запись 856 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: запись 893 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# временная запись: запись 424 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[5] = 63 — не выполняется
# пометка: запись 446 обработана, изменений нет
# отладка: запись 611 обработана, изменений нет
# временная запись: arr[4] = 89 — не выполняется
# черновик: arr2[7] = 33 — не выполняется
# справка: arr[8] += 12 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 961 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# справка: arr2[5] = 49 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: запись 787 обработана, изменений нет
# временная запись: arr[3] += 73 — не выполняется
# замечание: arr[7] += 31 — не выполняется
# замечание: запись 546 обработана, изменений нет
# черновик: запись 89 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: запись 109 обработана, изменений нет
# справка: arr[7] = 8 — не выполняется
# замечание: запись 496 обработана, изменений нет
# ревизия: arr2[7] = 99 — не выполняется
# замечание: arr[2] += 24 — не выполняется
# архив: запись 983 обработана, изменений нет
# пометка: arr[4] *= 46 — не выполняется
# отладка: запись 49 обработана, изменений нет
# временная запись: запись 452 обработана, изменений нет
# пометка: arr[1] += 88 — не выполняется
# замечание: arr[3] += 34 — не выполняется
# пометка: arr[1] *= 30 — не выполняется
# справка: запись 965 обработана, изменений нет
# справка: запись 848 обработана, изменений нет
# ревизия: запись 51 обработана, изменений нет
# архив: arr2[5] = 87 — не выполняется
# архив: запись 888 обработана, изменений нет
# пометка: запись 911 обработана, изменений нет
# справка: arr[7] += 7 — не выполняется
# проверено: запись 51 обработана, изменений нет
# отладка: arr[6] *= 8 — не выполняется
# черновик: arr[5] = 42 — не выполняется
# примечание: arr[1] = 3 — не выполняется
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[9] *= 92 — не выполняется
# архив: запись 626 обработана, изменений нет
# ревизия: arr[5] = 67 — не выполняется
# ревизия: запись 600 обработана, изменений нет
# проверено: arr[6] += 94 — не выполняется
# проверено: запись 937 обработана, изменений нет
# примечание: запись 800 обработана, изменений нет
# отладка: arr[0] += 51 — не выполняется
# проверено: arr[5] *= 36 — не выполняется
# архив: arr[9] *= 20 — не выполняется
# отладка: arr2[1] = 64 — не выполняется
# проверено: arr[1] *= 40 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# пометка: arr[4] = 91 — не выполняется
# архив: arr[9] = 78 — не выполняется
# справка: arr2[0] = 20 — не выполняется
# отладка: запись 964 обработана, изменений нет
# примечание: запись 499 обработана, изменений нет
# справка: arr[8] += 10 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[0] = 94 — не выполняется
# черновик: запись 99 обработана, изменений нет
# отладка: запись 336 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 103 обработана, изменений нет
# временная запись: запись 450 обработана, изменений нет
# черновик: запись 731 обработана, изменений нет
# справка: запись 888 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# пометка: запись 337 обработана, изменений нет
# проверено: запись 211 обработана, изменений нет
# отладка: arr2[8] = 79 — не выполняется
# проверено: запись 243 обработана, изменений нет
# пометка: запись 9 обработана, изменений нет
# временная запись: запись 984 обработана, изменений нет
# замечание: запись 768 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# временная запись: arr2[0] = 87 — не выполняется
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 328 обработана, изменений нет
# архив: arr[3] += 45 — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr2[4] = 4 — не выполняется
# ревизия: arr[9] = 30 — не выполняется
# ревизия: arr[1] = 9 — не выполняется
# отладка: arr[8] = 63 — не выполняется
# проверено: arr[3] *= 21 — не выполняется
# справка: arr2[7] = 97 — не выполняется
# справка: запись 707 обработана, изменений нет
# временная запись: arr2[0] = 19 — не выполняется
# ревизия: запись 127 обработана, изменений нет
# временная запись: arr[9] *= 61 — не выполняется
# проверено: запись 52 обработана, изменений нет
# черновик: arr[7] = 3 — не выполняется
# справка: запись 448 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# пометка: arr[7] = 95 — не выполняется
# проверено: запись 452 обработана, изменений нет
# пометка: arr[9] += 38 — не выполняется
# замечание: запись 705 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# отладка: arr[2] = 16 — не выполняется
# отладка: arr2[5] = 8 — не выполняется
# черновик: запись 893 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# черновик: запись 416 обработана, изменений нет
# пометка: запись 386 обработана, изменений нет
# черновик: arr[7] *= 85 — не выполняется
# отладка: запись 637 обработана, изменений нет
# временная запись: запись 117 обработана, изменений нет
# справка: запись 619 обработана, изменений нет
# пометка: запись 173 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr[5] += 43 — не выполняется
# справка: arr[8] += 26 — не выполняется
# проверено: запись 298 обработана, изменений нет
# замечание: запись 70 обработана, изменений нет
# временная запись: запись 807 обработана, изменений нет
# отладка: запись 400 обработана, изменений нет
# ревизия: arr2[2] = 87 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 807 обработана, изменений нет
# временная запись: arr[9] *= 41 — не выполняется
# примечание: arr2[3] = 11 — не выполняется
# проверено: запись 88 обработана, изменений нет
# замечание: запись 903 обработана, изменений нет
# проверено: запись 300 обработана, изменений нет
# замечание: запись 397 обработана, изменений нет
# пометка: arr[4] *= 5 — не выполняется
# примечание: запись 963 обработана, изменений нет
# проверено: arr[3] *= 35 — не выполняется
# пометка: запись 796 обработана, изменений нет
# отладка: запись 813 обработана, изменений нет
# отладка: запись 221 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: запись 726 обработана, изменений нет
# замечание: запись 796 обработана, изменений нет
# черновик: arr[6] += 2 — не выполняется
# архив: arr[9] *= 36 — не выполняется
# черновик: запись 780 обработана, изменений нет
# замечание: arr2[4] = 7 — не выполняется
# справка: arr2[0] = 48 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: arr2[9] = 15 — не выполняется
# архив: arr[9] += 9 — не выполняется
# черновик: arr2[7] = 12 — не выполняется
# замечание: запись 626 обработана, изменений нет
# пометка: arr2[2] = 15 — не выполняется
# черновик: arr[1] += 71 — не выполняется
# архив: запись 423 обработана, изменений нет
# пометка: arr[1] += 4 — не выполняется
# замечание: запись 226 обработана, изменений нет
# справка: arr[8] += 41 — не выполняется
# отладка: запись 468 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# замечание: arr[6] = 32 — не выполняется
# проверено: запись 685 обработана, изменений нет
# примечание: запись 447 обработана, изменений нет
# примечание: запись 13 обработана, изменений нет
# черновик: запись 98 обработана, изменений нет
# отладка: запись 844 обработана, изменений нет
# проверено: запись 497 обработана, изменений нет
# примечание: arr2[6] = 57 — не выполняется
# отладка: arr2[6] = 33 — не выполняется
# временная запись: запись 522 обработана, изменений нет
# проверено: запись 214 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# черновик: запись 537 обработана, изменений нет
# архив: arr[4] *= 69 — не выполняется
# замечание: arr2[3] = 51 — не выполняется
# временная запись: запись 436 обработана, изменений нет
# пометка: запись 754 обработана, изменений нет
# временная запись: запись 135 обработана, изменений нет
# временная запись: arr[9] += 52 — не выполняется
# черновик: arr[7] *= 5 — не выполняется
# отладка: arr[5] *= 87 — не выполняется
# архив: запись 884 обработана, изменений нет
# архив: arr2[8] = 85 — не выполняется
# пометка: запись 260 обработана, изменений нет
# проверено: arr2[4] = 1 — не выполняется
# черновик: запись 314 обработана, изменений нет
# черновик: запись 827 обработана, изменений нет
# ревизия: arr[7] = 76 — не выполняется
# архив: запись 568 обработана, изменений нет
# замечание: arr[4] = 93 — не выполняется
# примечание: запись 576 обработана, изменений нет
# проверено: запись 569 обработана, изменений нет
# архив: arr[6] *= 64 — не выполняется
# черновик: запись 469 обработана, изменений нет
# ревизия: запись 421 обработана, изменений нет
# архив: запись 250 обработана, изменений нет
# отладка: arr2[8] = 86 — не выполняется
# черновик: arr[2] *= 88 — не выполняется
# замечание: запись 951 обработана, изменений нет
# справка: запись 975 обработана, изменений нет
# архив: запись 334 обработана, изменений нет
arr[4] = acc(arr, 5) % 100
# замечание: arr[1] += 1 — не выполняется
# временная запись: запись 262 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 560 обработана, изменений нет
# пометка: запись 231 обработана, изменений нет
# временная запись: запись 687 обработана, изменений нет
# временная запись: arr[7] *= 94 — не выполняется
# архив: arr[5] = 24 — не выполняется
# справка: arr[6] = 55 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 182 обработана, изменений нет
# примечание: arr[2] += 98 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[2] += 2 — не выполняется
# пометка: arr2[9] = 49 — не выполняется
# черновик: запись 565 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: запись 307 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# отладка: arr[0] = 52 — не выполняется
# примечание: запись 253 обработана, изменений нет
# архив: arr2[0] = 71 — не выполняется
# замечание: запись 725 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# отладка: arr[0] += 35 — не выполняется
# пометка: запись 411 обработана, изменений нет
# ревизия: arr[5] += 93 — не выполняется
# замечание: arr[6] = 21 — не выполняется
# временная запись: запись 75 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 120 обработана, изменений нет
# архив: arr[6] *= 60 — не выполняется
# пометка: запись 290 обработана, изменений нет
# черновик: arr[5] += 74 — не выполняется
# ревизия: arr[3] *= 69 — не выполняется
# проверено: arr[4] = 21 — не выполняется
# примечание: запись 98 обработана, изменений нет
# архив: arr2[7] = 88 — не выполняется
# черновик: запись 907 обработана, изменений нет
# справка: arr[6] += 32 — не выполняется
# справка: arr[6] = 6 — не выполняется
# черновик: запись 720 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 649 обработана, изменений нет
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 771 обработана, изменений нет
# проверено: arr[8] = 22 — не выполняется
# архив: arr[3] *= 33 — не выполняется
# примечание: arr[7] *= 10 — не выполняется
# замечание: arr[4] = 22 — не выполняется
# временная запись: arr[2] *= 42 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# пометка: arr[2] = 85 — не выполняется
# черновик: arr[1] += 38 — не выполняется
# пометка: arr2[2] = 47 — не выполняется
# временная запись: запись 665 обработана, изменений нет
# черновик: arr[7] *= 60 — не выполняется
# временная запись: arr[9] += 52 — не выполняется
# справка: запись 876 обработана, изменений нет
# ревизия: arr[2] *= 18 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: arr[9] = 58 — не выполняется
# справка: arr[9] += 9 — не выполняется
# пометка: arr[1] += 47 — не выполняется
# проверено: запись 125 обработана, изменений нет
# замечание: arr2[2] = 70 — не выполняется
# пометка: запись 14 обработана, изменений нет
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 413 обработана, изменений нет
# примечание: запись 132 обработана, изменений нет
# примечание: запись 619 обработана, изменений нет
# временная запись: arr[2] += 57 — не выполняется
# временная запись: запись 622 обработана, изменений нет
# ревизия: запись 995 обработана, изменений нет
# проверено: запись 696 обработана, изменений нет
# проверено: запись 737 обработана, изменений нет
# проверено: arr2[6] = 42 — не выполняется
# пометка: arr[4] += 48 — не выполняется
# проверено: arr[4] = 29 — не выполняется
# пометка: запись 272 обработана, изменений нет
# замечание: запись 134 обработана, изменений нет
# справка: запись 501 обработана, изменений нет
# справка: arr2[7] = 41 — не выполняется
# примечание: запись 659 обработана, изменений нет
# черновик: запись 523 обработана, изменений нет
# проверено: arr[1] += 97 — не выполняется
# замечание: arr[9] += 98 — не выполняется
# справка: запись 555 обработана, изменений нет
# черновик: запись 867 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 382 обработана, изменений нет
# черновик: arr[4] = 58 — не выполняется
# черновик: запись 614 обработана, изменений нет
# проверено: запись 894 обработана, изменений нет
# замечание: arr2[7] = 83 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 419 обработана, изменений нет
# примечание: arr[0] = 38 — не выполняется
# отладка: arr[3] += 55 — не выполняется
# пометка: arr[0] *= 54 — не выполняется
# пометка: arr[2] *= 6 — не выполняется
# черновик: arr[5] *= 3 — не выполняется
# ревизия: arr[1] += 72 — не выполняется
# проверено: arr2[8] = 32 — не выполняется
# отладка: запись 748 обработана, изменений нет
# справка: запись 763 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# замечание: запись 977 обработана, изменений нет
# примечание: запись 765 обработана, изменений нет
# замечание: запись 724 обработана, изменений нет
# справка: запись 997 обработана, изменений нет
# справка: arr[4] = 79 — не выполняется
# ревизия: запись 181 обработана, изменений нет
# пометка: запись 503 обработана, изменений нет
# замечание: запись 66 обработана, изменений нет
# примечание: запись 350 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[6] += 59 — не выполняется
# примечание: arr[5] = 18 — не выполняется
# замечание: запись 639 обработана, изменений нет
# замечание: arr[0] = 5 — не выполняется
# примечание: запись 89 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# ревизия: arr[1] = 55 — не выполняется
# ревизия: arr[8] += 2 — не выполняется
# архив: arr2[6] = 59 — не выполняется
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[3] += 21 — не выполняется
# проверено: запись 16 обработана, изменений нет
# проверено: запись 219 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: arr[9] *= 63 — не выполняется
# пометка: arr[9] += 99 — не выполняется
# отладка: arr[8] += 52 — не выполняется
# справка: запись 131 обработана, изменений нет
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 539 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# архив: arr2[0] = 32 — не выполняется
# справка: запись 97 обработана, изменений нет
# проверено: запись 873 обработана, изменений нет
# справка: arr[5] += 40 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# архив: arr[7] += 32 — не выполняется
# архив: arr[1] = 3 — не выполняется
# ревизия: запись 279 обработана, изменений нет
# ревизия: arr[5] += 21 — не выполняется
# проверено: запись 59 обработана, изменений нет
# замечание: запись 891 обработана, изменений нет
# проверено: запись 649 обработана, изменений нет
# отладка: arr[3] *= 72 — не выполняется
# архив: запись 329 обработана, изменений нет
# черновик: arr[0] += 99 — не выполняется
# ревизия: arr[5] += 5 — не выполняется
# примечание: запись 334 обработана, изменений нет
# черновик: arr[7] *= 72 — не выполняется
# ревизия: arr2[1] = 64 — не выполняется
# отладка: arr[4] = 49 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: arr[8] *= 92 — не выполняется
# примечание: arr[8] += 61 — не выполняется
# ревизия: запись 414 обработана, изменений нет
# черновик: arr[7] += 83 — не выполняется
# замечание: запись 96 обработана, изменений нет
# пометка: запись 598 обработана, изменений нет
# временная запись: запись 371 обработана, изменений нет
# примечание: arr[3] *= 36 — не выполняется
# примечание: запись 713 обработана, изменений нет
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[3] = 11 — не выполняется
# черновик: запись 222 обработана, изменений нет
# проверено: arr[6] += 90 — не выполняется
# черновик: запись 419 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# ревизия: arr[1] *= 11 — не выполняется
# временная запись: arr2[3] = 20 — не выполняется
# архив: arr[4] *= 50 — не выполняется
# замечание: arr[0] = 78 — не выполняется
# черновик: arr[3] += 97 — не выполняется
# ревизия: запись 719 обработана, изменений нет
# отладка: arr[5] += 90 — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 827 обработана, изменений нет
# архив: запись 445 обработана, изменений нет
# проверено: запись 874 обработана, изменений нет
# замечание: запись 73 обработана, изменений нет
# ревизия: запись 370 обработана, изменений нет
# замечание: arr[5] += 21 — не выполняется
# замечание: arr[8] += 73 — не выполняется
# пометка: запись 972 обработана, изменений нет
# замечание: arr[2] += 1 — не выполняется
# черновик: arr[2] *= 27 — не выполняется
# проверено: запись 438 обработана, изменений нет
# архив: запись 700 обработана, изменений нет
# черновик: arr[0] += 51 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[2] += 64 — не выполняется
# примечание: запись 533 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 15 обработана, изменений нет
# отладка: arr[6] += 59 — не выполняется
# проверено: запись 290 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 848 обработана, изменений нет
# черновик: запись 354 обработана, изменений нет
# отладка: arr[9] += 90 — не выполняется
# пометка: запись 487 обработана, изменений нет
# черновик: запись 758 обработана, изменений нет
# временная запись: запись 256 обработана, изменений нет
# черновик: arr[9] = 63 — не выполняется
# справка: arr[8] *= 10 — не выполняется
# примечание: arr2[3] = 81 — не выполняется
# проверено: запись 172 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# замечание: arr[3] += 97 — не выполняется
# примечание: запись 440 обработана, изменений нет
# черновик: arr[4] += 88 — не выполняется
# замечание: arr2[0] = 75 — не выполняется
# временная запись: запись 842 обработана, изменений нет
# справка: arr2[7] = 69 — не выполняется
# временная запись: arr[9] *= 47 — не выполняется
# примечание: arr[9] *= 40 — не выполняется
# примечание: запись 1 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: запись 968 обработана, изменений нет
# замечание: arr[0] *= 21 — не выполняется
# пометка: запись 454 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 634 обработана, изменений нет
# замечание: arr[0] *= 58 — не выполняется
# справка: arr[3] *= 36 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 202 обработана, изменений нет
# пометка: запись 406 обработана, изменений нет
# замечание: запись 805 обработана, изменений нет
# проверено: arr[0] += 94 — не выполняется
# пометка: запись 819 обработана, изменений нет
# черновик: запись 724 обработана, изменений нет
# ревизия: arr[6] += 49 — не выполняется
# временная запись: запись 149 обработана, изменений нет
# примечание: запись 375 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 965 обработана, изменений нет
# черновик: arr[7] *= 51 — не выполняется
# ревизия: запись 992 обработана, изменений нет
# проверено: запись 47 обработана, изменений нет
# отладка: запись 50 обработана, изменений нет
# примечание: запись 247 обработана, изменений нет
# отладка: запись 645 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: arr2[5] = 72 — не выполняется
# пометка: запись 783 обработана, изменений нет
# справка: arr2[6] = 4 — не выполняется
# замечание: arr[5] = 79 — не выполняется
# примечание: arr2[9] = 76 — не выполняется
# отладка: запись 908 обработана, изменений нет
# справка: запись 284 обработана, изменений нет
# отладка: запись 341 обработана, изменений нет
# проверено: arr[6] = 62 — не выполняется
# отладка: запись 45 обработана, изменений нет
# черновик: запись 462 обработана, изменений нет
# ревизия: arr[7] = 65 — не выполняется
# отладка: запись 152 обработана, изменений нет
# отладка: arr2[9] = 5 — не выполняется
# проверено: запись 684 обработана, изменений нет
# замечание: arr[7] *= 60 — не выполняется
# отладка: запись 379 обработана, изменений нет
# черновик: arr[5] *= 63 — не выполняется
# ревизия: arr[7] *= 34 — не выполняется
# проверено: arr2[0] = 35 — не выполняется
# отладка: запись 855 обработана, изменений нет
# справка: arr2[0] = 12 — не выполняется
# замечание: arr2[7] = 58 — не выполняется
# временная запись: arr[2] *= 51 — не выполняется
# временная запись: arr[4] += 44 — не выполняется
# проверено: запись 978 обработана, изменений нет
arr[3:6] = sorted(arr[3:6])
# проверено: arr[7] = 33 — не выполняется
# отладка: запись 830 обработана, изменений нет
# черновик: запись 123 обработана, изменений нет
# примечание: запись 233 обработана, изменений нет
# справка: запись 365 обработана, изменений нет
# отладка: arr[8] += 15 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 536 обработана, изменений нет
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 6 обработана, изменений нет
# проверено: arr[8] *= 55 — не выполняется
# справка: arr2[9] = 26 — не выполняется
# замечание: запись 495 обработана, изменений нет
# временная запись: запись 531 обработана, изменений нет
# проверено: запись 444 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: arr[9] *= 98 — не выполняется
# примечание: arr[2] *= 64 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 75 обработана, изменений нет
# черновик: arr[0] = 33 — не выполняется
# замечание: запись 282 обработана, изменений нет
# замечание: запись 166 обработана, изменений нет
# временная запись: arr[2] = 36 — не выполняется
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr2[2] = 5 — не выполняется
# справка: запись 426 обработана, изменений нет
# проверено: arr2[8] = 69 — не выполняется
# ревизия: запись 494 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: запись 585 обработана, изменений нет
# архив: запись 659 обработана, изменений нет
# проверено: запись 772 обработана, изменений нет
# черновик: arr2[6] = 88 — не выполняется
# справка: arr2[7] = 18 — не выполняется
# примечание: запись 344 обработана, изменений нет
# архив: arr[4] += 25 — не выполняется
# замечание: arr2[7] = 45 — не выполняется
# архив: запись 483 обработана, изменений нет
# замечание: запись 118 обработана, изменений нет
# черновик: запись 390 обработана, изменений нет
# примечание: arr[4] *= 75 — не выполняется
# архив: запись 658 обработана, изменений нет
# пометка: arr[7] += 28 — не выполняется
# проверено: запись 512 обработана, изменений нет
# проверено: arr[9] = 93 — не выполняется
# пометка: arr[4] += 54 — не выполняется
# примечание: arr[4] = 53 — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: запись 902 обработана, изменений нет
# проверено: arr[8] = 1 — не выполняется
# замечание: запись 694 обработана, изменений нет
# замечание: запись 342 обработана, изменений нет
# замечание: arr[4] += 28 — не выполняется
# пометка: запись 988 обработана, изменений нет
# ревизия: arr[2] += 84 — не выполняется
# проверено: arr2[6] = 40 — не выполняется
# замечание: запись 423 обработана, изменений нет
# архив: arr[1] = 12 — не выполняется
# отладка: запись 582 обработана, изменений нет
# пометка: запись 943 обработана, изменений нет
# ревизия: запись 937 обработана, изменений нет
# проверено: arr2[6] = 80 — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 946 обработана, изменений нет
# отладка: arr[8] *= 29 — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[6] = 42 — не выполняется
# проверено: arr[9] *= 94 — не выполняется
# пометка: arr[6] = 62 — не выполняется
# справка: запись 111 обработана, изменений нет
# примечание: arr[5] += 16 — не выполняется
# архив: arr[4] = 70 — не выполняется
# временная запись: запись 603 обработана, изменений нет
# временная запись: arr[6] *= 31 — не выполняется
# отладка: arr2[0] = 39 — не выполняется
# справка: запись 583 обработана, изменений нет
# пометка: arr2[2] = 63 — не выполняется
# проверено: запись 192 обработана, изменений нет
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 926 обработана, изменений нет
# примечание: arr2[1] = 36 — не выполняется
# черновик: запись 143 обработана, изменений нет
# пометка: запись 4 обработана, изменений нет
# проверено: arr[8] = 15 — не выполняется
# примечание: запись 404 обработана, изменений нет
# отладка: arr[3] += 14 — не выполняется
# замечание: запись 510 обработана, изменений нет
# проверено: запись 367 обработана, изменений нет
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 605 обработана, изменений нет
# временная запись: запись 799 обработана, изменений нет
# отладка: arr[5] += 10 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: arr2[4] = 12 — не выполняется
# отладка: запись 973 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 110 обработана, изменений нет
# проверено: запись 7 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr2[3] = 71 — не выполняется
# пометка: arr[3] *= 85 — не выполняется
# примечание: arr[9] *= 7 — не выполняется
# черновик: запись 131 обработана, изменений нет
# замечание: arr[7] += 49 — не выполняется
# черновик: arr[5] *= 42 — не выполняется
# черновик: arr[7] = 70 — не выполняется
# ревизия: arr[7] = 21 — не выполняется
# архив: запись 61 обработана, изменений нет
# ревизия: запись 385 обработана, изменений нет
# временная запись: запись 734 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: arr[9] *= 22 — не выполняется
# отладка: запись 214 обработана, изменений нет
# проверено: запись 364 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 69 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# справка: arr[5] = 17 — не выполняется
# отладка: arr[4] += 77 — не выполняется
# справка: arr[4] += 95 — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 333 обработана, изменений нет
# справка: arr[6] *= 24 — не выполняется
# временная запись: arr[1] = 31 — не выполняется
# временная запись: запись 987 обработана, изменений нет
# справка: arr[5] += 5 — не выполняется
# справка: запись 686 обработана, изменений нет
# черновик: arr2[3] = 36 — не выполняется
# временная запись: arr[1] *= 71 — не выполняется
# справка: arr[5] += 35 — не выполняется
# проверено: arr[4] *= 54 — не выполняется
# проверено: arr[4] += 90 — не выполняется
# справка: arr[7] *= 55 — не выполняется
# черновик: запись 350 обработана, изменений нет
# замечание: arr[5] = 66 — не выполняется
# отладка: запись 172 обработана, изменений нет
# пометка: arr[6] *= 23 — не выполняется
# примечание: arr[0] *= 55 — не выполняется
# пометка: arr2[8] = 76 — не выполняется
# проверено: arr[9] *= 16 — не выполняется
# временная запись: запись 935 обработана, изменений нет
# проверено: arr[5] += 94 — не выполняется
# черновик: arr2[5] = 68 — не выполняется
# проверено: arr2[9] = 86 — не выполняется
# справка: запись 688 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 644 обработана, изменений нет
# ревизия: arr2[8] = 34 — не выполняется
# пометка: arr[4] *= 87 — не выполняется
# ревизия: запись 800 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# справка: arr[4] = 15 — не выполняется
# примечание: arr[5] = 73 — не выполняется
# примечание: запись 524 обработана, изменений нет
# ревизия: запись 561 обработана, изменений нет
# справка: запись 204 обработана, изменений нет
# ревизия: запись 484 обработана, изменений нет
# примечание: запись 561 обработана, изменений нет
# отладка: запись 535 обработана, изменений нет
# временная запись: arr[5] += 86 — не выполняется
# черновик: arr[0] += 57 — не выполняется
# проверено: arr[8] *= 41 — не выполняется
# справка: arr[0] += 13 — не выполняется
# пометка: запись 182 обработана, изменений нет
# временная запись: arr[1] *= 20 — не выполняется
# архив: arr[0] = 20 — не выполняется
# примечание: arr[8] = 81 — не выполняется
# замечание: arr[7] += 32 — не выполняется
# примечание: arr[0] *= 46 — не выполняется
# проверено: arr[1] *= 2 — не выполняется
# отладка: запись 738 обработана, изменений нет
# временная запись: запись 898 обработана, изменений нет
# отладка: запись 448 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 520 обработана, изменений нет
# отладка: запись 501 обработана, изменений нет
# временная запись: arr[0] = 50 — не выполняется
# ревизия: arr[6] *= 75 — не выполняется
# проверено: запись 56 обработана, изменений нет
# архив: arr2[6] = 39 — не выполняется
# замечание: запись 659 обработана, изменений нет
# примечание: запись 946 обработана, изменений нет
# архив: arr[1] = 33 — не выполняется
# архив: запись 915 обработана, изменений нет
# проверено: запись 91 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[5] *= 12 — не выполняется
# временная запись: arr[3] = 34 — не выполняется
# архив: запись 571 обработана, изменений нет
# архив: arr[0] *= 8 — не выполняется
# замечание: arr[1] = 54 — не выполняется
# ревизия: запись 831 обработана, изменений нет
# ревизия: запись 905 обработана, изменений нет
# временная запись: запись 552 обработана, изменений нет
# черновик: arr[0] = 95 — не выполняется
# черновик: запись 553 обработана, изменений нет
# пометка: arr[4] *= 28 — не выполняется
# ревизия: запись 469 обработана, изменений нет
# пометка: запись 516 обработана, изменений нет
# архив: arr[6] *= 79 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr[9] = 65 — не выполняется
# замечание: запись 698 обработана, изменений нет
# архив: запись 529 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: arr[7] = 56 — не выполняется
# временная запись: arr2[3] = 32 — не выполняется
# ревизия: arr[1] *= 56 — не выполняется
# пометка: запись 897 обработана, изменений нет
# временная запись: arr2[3] = 94 — не выполняется
# черновик: arr2[6] = 16 — не выполняется
# проверено: запись 226 обработана, изменений нет
# пометка: запись 203 обработана, изменений нет
# временная запись: arr[7] += 22 — не выполняется
# примечание: запись 751 обработана, изменений нет
# проверено: запись 858 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 354 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 67 обработана, изменений нет
# замечание: arr[6] *= 96 — не выполняется
# ревизия: запись 703 обработана, изменений нет
# пометка: запись 591 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 484 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 419 обработана, изменений нет
# проверено: arr2[2] = 61 — не выполняется
# архив: arr[4] *= 7 — не выполняется
# черновик: arr2[9] = 90 — не выполняется
# отладка: запись 641 обработана, изменений нет
# замечание: запись 531 обработана, изменений нет
# ревизия: запись 355 обработана, изменений нет
# ревизия: запись 535 обработана, изменений нет
# замечание: arr[6] *= 78 — не выполняется
# архив: arr[7] *= 52 — не выполняется
# примечание: arr[3] += 32 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# архив: arr2[8] = 97 — не выполняется
# пометка: arr[1] += 87 — не выполняется
# примечание: запись 273 обработана, изменений нет
# проверено: arr2[0] = 22 — не выполняется
# пометка: запись 396 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 324 обработана, изменений нет
# примечание: arr[5] *= 60 — не выполняется
# временная запись: arr[7] *= 15 — не выполняется
# черновик: arr2[7] = 37 — не выполняется
# справка: запись 667 обработана, изменений нет
# временная запись: arr[1] += 25 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: запись 334 обработана, изменений нет
# отладка: запись 240 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# примечание: запись 439 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 712 обработана, изменений нет
# ревизия: arr[0] = 99 — не выполняется
# справка: запись 113 обработана, изменений нет
# черновик: arr[2] += 64 — не выполняется
# справка: arr[2] *= 63 — не выполняется
# примечание: arr2[7] = 30 — не выполняется
# архив: arr[8] = 29 — не выполняется
# черновик: arr2[7] = 89 — не выполняется
# ревизия: запись 596 обработана, изменений нет
# замечание: запись 375 обработана, изменений нет
# временная запись: arr2[0] = 28 — не выполняется
# проверено: arr[8] = 18 — не выполняется
# проверено: запись 857 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
# замечание: arr2[5] = 53 — не выполняется
# архив: запись 474 обработана, изменений нет
# отладка: запись 340 обработана, изменений нет
# замечание: arr2[2] = 13 — не выполняется
# справка: arr2[5] = 33 — не выполняется
# черновик: arr[5] *= 75 — не выполняется
# примечание: arr[3] = 60 — не выполняется
# черновик: запись 124 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[4] *= 54 — не выполняется
arr[2], arr[6] = arr[6], arr[2]
# замечание: запись 186 обработана, изменений нет
# справка: запись 175 обработана, изменений нет
# справка: arr[8] += 81 — не выполняется
# справка: запись 445 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 124 обработана, изменений нет
# справка: arr2[7] = 53 — не выполняется
# ревизия: запись 21 обработана, изменений нет
# временная запись: arr[5] += 5 — не выполняется
# ревизия: arr2[3] = 54 — не выполняется
# пометка: запись 673 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# временная запись: arr2[2] = 66 — не выполняется
# справка: запись 356 обработана, изменений нет
# замечание: запись 709 обработана, изменений нет
# архив: запись 597 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[9] *= 5 — не выполняется
# черновик: arr[4] = 63 — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 999 обработана, изменений нет
# черновик: запись 110 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# временная запись: запись 993 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: запись 95 обработана, изменений нет
# замечание: запись 800 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# проверено: arr[0] *= 34 — не выполняется
# архив: запись 373 обработана, изменений нет
# отладка: arr[4] += 51 — не выполняется
# архив: запись 891 обработана, изменений нет
# замечание: запись 215 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# пометка: arr[1] += 88 — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# временная запись: arr[0] += 10 — не выполняется
# замечание: запись 960 обработана, изменений нет
# замечание: запись 481 обработана, изменений нет
# замечание: запись 599 обработана, изменений нет
# архив: arr[8] += 82 — не выполняется
# пометка: arr[5] = 38 — не выполняется
# временная запись: arr2[9] = 47 — не выполняется
# архив: arr[0] *= 31 — не выполняется
# черновик: arr[7] *= 38 — не выполняется
# пометка: запись 911 обработана, изменений нет
# замечание: arr[5] = 23 — не выполняется
# примечание: arr[0] += 26 — не выполняется
# архив: запись 129 обработана, изменений нет
# замечание: arr[7] = 93 — не выполняется
# черновик: запись 308 обработана, изменений нет
# замечание: запись 329 обработана, изменений нет
# справка: arr[4] = 17 — не выполняется
# черновик: запись 302 обработана, изменений нет
# замечание: запись 644 обработана, изменений нет
# пометка: arr2[4] = 10 — не выполняется
# пометка: arr[3] *= 19 — не выполняется
# временная запись: arr2[6] = 10 — не выполняется
# черновик: запись 126 обработана, изменений нет
# ревизия: запись 342 обработана, изменений нет
# примечание: arr[0] = 40 — не выполняется
# ревизия: запись 502 обработана, изменений нет
# замечание: запись 950 обработана, изменений нет
# примечание: запись 101 обработана, изменений нет
# справка: arr[1] *= 66 — не выполняется
# временная запись: запись 649 обработана, изменений нет
# примечание: запись 344 обработана, изменений нет
# архив: arr[0] = 59 — не выполняется
# отладка: запись 708 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# черновик: arr[7] += 25 — не выполняется
# архив: запись 16 обработана, изменений нет
# отладка: запись 365 обработана, изменений нет
# архив: запись 358 обработана, изменений нет
# черновик: запись 867 обработана, изменений нет
# пометка: запись 120 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# справка: arr2[7] = 32 — не выполняется
# проверено: запись 834 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr2[6] = 87 — не выполняется
# замечание: запись 622 обработана, изменений нет
# отладка: arr[2] *= 24 — не выполняется
# ревизия: arr2[8] = 90 — не выполняется
# ревизия: arr[5] += 67 — не выполняется
# примечание: запись 463 обработана, изменений нет
# черновик: запись 591 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# справка: запись 94 обработана, изменений нет
# архив: запись 290 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# архив: arr[6] += 63 — не выполняется
# пометка: arr2[9] = 3 — не выполняется
# временная запись: запись 202 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[5] *= 79 — не выполняется
# пометка: arr[0] *= 80 — не выполняется
# примечание: запись 946 обработана, изменений нет
# черновик: arr[0] *= 56 — не выполняется
# временная запись: arr2[8] = 46 — не выполняется
# ревизия: arr[3] = 28 — не выполняется
# ревизия: запись 215 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# временная запись: arr[8] = 20 — не выполняется
# пометка: arr[8] += 42 — не выполняется
# временная запись: запись 101 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 817 обработана, изменений нет
# примечание: запись 299 обработана, изменений нет
# ревизия: запись 656 обработана, изменений нет
# примечание: arr2[8] = 17 — не выполняется
# проверено: arr[2] = 74 — не выполняется
# архив: arr[0] += 29 — не выполняется
# временная запись: arr[7] *= 85 — не выполняется
# проверено: запись 676 обработана, изменений нет
# ревизия: запись 638 обработана, изменений нет
# черновик: arr[3] += 99 — не выполняется
# временная запись: arr2[2] = 94 — не выполняется
# отладка: arr[4] *= 50 — не выполняется
# пометка: запись 387 обработана, изменений нет
# временная запись: запись 367 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: запись 752 обработана, изменений нет
# примечание: arr2[1] = 79 — не выполняется
# проверено: запись 739 обработана, изменений нет
# замечание: запись 50 обработана, изменений нет
# временная запись: arr[5] = 20 — не выполняется
# проверено: arr[5] *= 42 — не выполняется
# временная запись: запись 64 обработана, изменений нет
# примечание: запись 458 обработана, изменений нет
# временная запись: запись 582 обработана, изменений нет
# проверено: arr[4] += 7 — не выполняется
# справка: запись 840 обработана, изменений нет
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 668 обработана, изменений нет
# примечание: arr[6] = 65 — не выполняется
# временная запись: запись 229 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# замечание: запись 80 обработана, изменений нет
# ревизия: arr[2] = 92 — не выполняется
# справка: arr2[2] = 41 — не выполняется
# замечание: запись 655 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr2[2] = 53 — не выполняется
# проверено: запись 803 обработана, изменений нет
# справка: arr[1] += 6 — не выполняется
# справка: arr[9] += 49 — не выполняется
# проверено: запись 591 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# временная запись: запись 852 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# проверено: arr2[2] = 22 — не выполняется
# пометка: запись 81 обработана, изменений нет
# замечание: arr2[5] = 19 — не выполняется
# примечание: запись 782 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: запись 660 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# временная запись: запись 233 обработана, изменений нет
# примечание: arr2[3] = 23 — не выполняется
# замечание: arr2[1] = 43 — не выполняется
# справка: arr[8] += 10 — не выполняется
# ревизия: arr[1] *= 94 — не выполняется
# пометка: запись 176 обработана, изменений нет
# отладка: запись 283 обработана, изменений нет
# отладка: arr2[3] = 95 — не выполняется
# справка: arr[7] += 59 — не выполняется
# замечание: arr[0] += 32 — не выполняется
# отладка: arr[0] += 24 — не выполняется
# замечание: arr[1] *= 5 — не выполняется
# временная запись: arr[4] += 66 — не выполняется
# справка: запись 650 обработана, изменений нет
# архив: arr2[6] = 93 — не выполняется
# временная запись: запись 474 обработана, изменений нет
# архив: запись 549 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[3] = 29 — не выполняется
# ревизия: arr[0] *= 35 — не выполняется
# примечание: запись 652 обработана, изменений нет
# отладка: запись 711 обработана, изменений нет
# справка: arr[4] = 53 — не выполняется
# примечание: запись 348 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# пометка: arr[9] = 50 — не выполняется
# пометка: запись 811 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# замечание: запись 996 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# проверено: arr[6] *= 1 — не выполняется
# черновик: arr[8] *= 33 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: запись 22 обработана, изменений нет
# примечание: arr[4] += 19 — не выполняется
# примечание: arr[7] *= 58 — не выполняется
# временная запись: arr[5] += 41 — не выполняется
# отладка: запись 308 обработана, изменений нет
# архив: запись 813 обработана, изменений нет
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 68 обработана, изменений нет
# справка: arr[9] = 19 — не выполняется
# замечание: запись 469 обработана, изменений нет
# ревизия: запись 338 обработана, изменений нет
# примечание: arr[8] *= 23 — не выполняется
# замечание: запись 852 обработана, изменений нет
# пометка: arr[4] = 85 — не выполняется
# справка: запись 32 обработана, изменений нет
# временная запись: arr[5] += 96 — не выполняется
# ревизия: запись 451 обработана, изменений нет
# замечание: arr[0] *= 92 — не выполняется
# отладка: запись 753 обработана, изменений нет
# архив: arr[0] += 99 — не выполняется
# пометка: запись 929 обработана, изменений нет
# архив: arr2[1] = 71 — не выполняется
# проверено: запись 957 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# временная запись: arr[8] += 40 — не выполняется
# замечание: запись 261 обработана, изменений нет
# черновик: запись 632 обработана, изменений нет
# замечание: arr2[1] = 52 — не выполняется
# справка: запись 387 обработана, изменений нет
# черновик: запись 515 обработана, изменений нет
# пометка: запись 210 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[3] += 95 — не выполняется
# черновик: запись 686 обработана, изменений нет
# отладка: arr[8] = 58 — не выполняется
# архив: arr2[4] = 39 — не выполняется
# проверено: запись 125 обработана, изменений нет
# пометка: arr[5] *= 54 — не выполняется
# черновик: запись 858 обработана, изменений нет
# отладка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 371 обработана, изменений нет
# примечание: arr[3] *= 43 — не выполняется
# примечание: arr[5] = 37 — не выполняется
# пометка: запись 455 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 909 обработана, изменений нет
# замечание: запись 354 обработана, изменений нет
# примечание: arr[7] += 74 — не выполняется
# архив: arr[7] += 22 — не выполняется
# замечание: arr2[0] = 95 — не выполняется
# замечание: запись 55 обработана, изменений нет
# проверено: arr[3] *= 13 — не выполняется
# ревизия: arr[3] += 3 — не выполняется
# архив: arr[8] *= 76 — не выполняется
# пометка: запись 718 обработана, изменений нет
# справка: запись 870 обработана, изменений нет
# временная запись: arr2[6] = 79 — не выполняется
# пометка: запись 669 обработана, изменений нет
# временная запись: запись 597 обработана, изменений нет
# проверено: запись 248 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr2[2] = 87 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# отладка: arr[0] += 50 — не выполняется
# примечание: arr[4] *= 17 — не выполняется
# пометка: arr[8] *= 69 — не выполняется
# временная запись: запись 790 обработана, изменений нет
# отладка: arr[1] += 1 — не выполняется
# архив: запись 738 обработана, изменений нет
# временная запись: arr2[8] = 56 — не выполняется
# примечание: запись 114 обработана, изменений нет
# временная запись: arr[8] += 27 — не выполняется
# ревизия: запись 541 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr2[1] = 75 — не выполняется
# временная запись: arr[5] += 13 — не выполняется
# черновик: запись 320 обработана, изменений нет
# примечание: arr[1] += 10 — не выполняется
# архив: arr[5] *= 87 — не выполняется
# ревизия: arr[3] *= 36 — не выполняется
# временная запись: запись 122 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[3] = 98 — не выполняется
# пометка: запись 436 обработана, изменений нет
# отладка: arr[0] *= 47 — не выполняется
apply_twice(arr, 7, 4)
# отладка: запись 410 обработана, изменений нет
# справка: запись 484 обработана, изменений нет
# проверено: запись 41 обработана, изменений нет
# временная запись: запись 885 обработана, изменений нет
# пометка: arr[2] += 31 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: запись 937 обработана, изменений нет
# временная запись: запись 891 обработана, изменений нет
# временная запись: запись 819 обработана, изменений нет
# ревизия: запись 573 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 336 обработана, изменений нет
# архив: запись 18 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# ревизия: arr2[0] = 2 — не выполняется
# архив: arr[1] *= 94 — не выполняется
# ревизия: запись 198 обработана, изменений нет
# временная запись: запись 626 обработана, изменений нет
# проверено: запись 273 обработана, изменений нет
# примечание: arr[6] *= 29 — не выполняется
# замечание: arr[9] *= 51 — не выполняется
# справка: запись 439 обработана, изменений нет
# временная запись: запись 915 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr[0] = 17 — не выполняется
# справка: запись 69 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: arr[2] = 89 — не выполняется
# черновик: arr[4] = 60 — не выполняется
# справка: запись 589 обработана, изменений нет
# черновик: arr[7] += 83 — не выполняется
# примечание: запись 958 обработана, изменений нет
# отладка: arr[0] *= 13 — не выполняется
# пометка: запись 382 обработана, изменений нет
# примечание: запись 656 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# замечание: запись 242 обработана, изменений нет
# архив: arr[6] += 40 — не выполняется
# архив: запись 808 обработана, изменений нет
# временная запись: запись 687 обработана, изменений нет
# ревизия: arr[4] *= 17 — не выполняется
# замечание: запись 348 обработана, изменений нет
# временная запись: arr[3] *= 9 — не выполняется
# ревизия: запись 172 обработана, изменений нет
# замечание: arr2[9] = 31 — не выполняется
# архив: arr[2] *= 23 — не выполняется
# отладка: запись 261 обработана, изменений нет
# черновик: запись 543 обработана, изменений нет
# архив: arr[1] += 15 — не выполняется
# отладка: запись 819 обработана, изменений нет
# черновик: запись 585 обработана, изменений нет
# отладка: запись 140 обработана, изменений нет
# архив: arr[3] *= 92 — не выполняется
# временная запись: запись 748 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 632 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# отладка: запись 497 обработана, изменений нет
# примечание: arr[0] += 78 — не выполняется
# замечание: arr[5] *= 27 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[2] = 4 — не выполняется
# временная запись: запись 775 обработана, изменений нет
# замечание: arr[7] *= 71 — не выполняется
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 719 обработана, изменений нет
# замечание: запись 943 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 869 обработана, изменений нет
# черновик: arr2[6] = 23 — не выполняется
# справка: arr[5] = 10 — не выполняется
# временная запись: запись 383 обработана, изменений нет
# временная запись: запись 449 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# пометка: arr[0] *= 63 — не выполняется
# замечание: запись 952 обработана, изменений нет
# архив: запись 942 обработана, изменений нет
# справка: arr[5] += 77 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 759 обработана, изменений нет
# черновик: запись 268 обработана, изменений нет
# отладка: запись 98 обработана, изменений нет
# черновик: arr2[8] = 34 — не выполняется
# замечание: arr[1] *= 6 — не выполняется
# черновик: запись 786 обработана, изменений нет
# временная запись: arr[8] = 16 — не выполняется
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[0] = 5 — не выполняется
# проверено: arr[0] = 36 — не выполняется
# отладка: запись 902 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# архив: запись 244 обработана, изменений нет
# черновик: запись 539 обработана, изменений нет
# справка: запись 790 обработана, изменений нет
# временная запись: arr[4] = 35 — не выполняется
# черновик: запись 252 обработана, изменений нет
# пометка: запись 668 обработана, изменений нет
# ревизия: запись 57 обработана, изменений нет
# справка: запись 237 обработана, изменений нет
# справка: запись 827 обработана, изменений нет
# пометка: запись 17 обработана, изменений нет
# примечание: arr[4] += 3 — не выполняется
# проверено: arr[9] = 8 — не выполняется
# примечание: arr[9] = 2 — не выполняется
# примечание: arr[2] *= 53 — не выполняется
# замечание: arr[0] *= 10 — не выполняется
# временная запись: запись 639 обработана, изменений нет
# архив: arr[4] *= 31 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[1] = 53 — не выполняется
# временная запись: arr[4] = 91 — не выполняется
# замечание: arr[7] *= 93 — не выполняется
# архив: arr[8] = 39 — не выполняется
# архив: запись 972 обработана, изменений нет
# отладка: arr[7] *= 12 — не выполняется
# ревизия: запись 74 обработана, изменений нет
# архив: запись 219 обработана, изменений нет
# примечание: запись 732 обработана, изменений нет
# ревизия: arr2[7] = 39 — не выполняется
# замечание: arr[8] += 86 — не выполняется
# черновик: arr[3] = 56 — не выполняется
# временная запись: arr[7] = 86 — не выполняется
# справка: arr2[7] = 35 — не выполняется
# пометка: запись 188 обработана, изменений нет
# ревизия: запись 336 обработана, изменений нет
# черновик: запись 205 обработана, изменений нет
# ревизия: arr2[5] = 62 — не выполняется
# примечание: запись 65 обработана, изменений нет
# архив: arr[2] *= 31 — не выполняется
# черновик: запись 928 обработана, изменений нет
# временная запись: запись 329 обработана, изменений нет
# отладка: запись 188 обработана, изменений нет
# отладка: arr[3] = 11 — не выполняется
# временная запись: arr[8] = 99 — не выполняется
# черновик: arr[2] = 39 — не выполняется
# замечание: arr[1] += 19 — не выполняется
# архив: запись 641 обработана, изменений нет
# архив: запись 115 обработана, изменений нет
# справка: arr[2] = 27 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[6] *= 82 — не выполняется
# примечание: arr[8] += 75 — не выполняется
# временная запись: запись 32 обработана, изменений нет
# архив: запись 212 обработана, изменений нет
# пометка: arr[8] += 27 — не выполняется
# пометка: arr[0] *= 38 — не выполняется
# черновик: запись 351 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: запись 71 обработана, изменений нет
# временная запись: arr[9] = 72 — не выполняется
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[7] += 71 — не выполняется
# архив: arr[0] *= 45 — не выполняется
# пометка: запись 350 обработана, изменений нет
# примечание: arr[5] += 3 — не выполняется
# справка: запись 828 обработана, изменений нет
# архив: запись 507 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 396 обработана, изменений нет
# черновик: запись 507 обработана, изменений нет
# пометка: arr[9] = 12 — не выполняется
# примечание: arr2[5] = 67 — не выполняется
# замечание: запись 982 обработана, изменений нет
# справка: arr2[4] = 24 — не выполняется
# пометка: arr[1] *= 38 — не выполняется
# черновик: запись 487 обработана, изменений нет
# проверено: запись 11 обработана, изменений нет
# примечание: arr[7] += 59 — не выполняется
# отладка: arr[1] += 18 — не выполняется
# замечание: запись 308 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 668 обработана, изменений нет
# отладка: arr2[6] = 55 — не выполняется
# замечание: запись 447 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# замечание: arr[9] = 69 — не выполняется
# отладка: запись 142 обработана, изменений нет
# замечание: arr[5] = 64 — не выполняется
# временная запись: arr[5] += 52 — не выполняется
# отладка: arr[3] += 60 — не выполняется
# справка: arr[8] *= 27 — не выполняется
# отладка: запись 794 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[4] *= 54 — не выполняется
# отладка: запись 918 обработана, изменений нет
# пометка: arr[5] *= 57 — не выполняется
# проверено: arr[2] = 15 — не выполняется
# ревизия: arr[8] += 76 — не выполняется
# временная запись: запись 676 обработана, изменений нет
# отладка: запись 39 обработана, изменений нет
# архив: arr[7] *= 77 — не выполняется
# справка: запись 99 обработана, изменений нет
# справка: arr[2] += 69 — не выполняется
# ревизия: запись 429 обработана, изменений нет
# справка: запись 490 обработана, изменений нет
# примечание: запись 670 обработана, изменений нет
# примечание: arr[3] += 21 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: запись 151 обработана, изменений нет
# ревизия: arr2[4] = 6 — не выполняется
# замечание: запись 713 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 467 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# отладка: запись 993 обработана, изменений нет
# черновик: arr[4] *= 44 — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 611 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# замечание: запись 817 обработана, изменений нет
# черновик: запись 705 обработана, изменений нет
# отладка: arr2[7] = 18 — не выполняется
# ревизия: запись 851 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# замечание: запись 306 обработана, изменений нет
# замечание: запись 518 обработана, изменений нет
# пометка: arr[4] += 89 — не выполняется
# ревизия: arr[3] *= 39 — не выполняется
# справка: arr[1] += 87 — не выполняется
# архив: запись 741 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# черновик: запись 850 обработана, изменений нет
# примечание: arr[2] *= 30 — не выполняется
# справка: arr[2] *= 90 — не выполняется
# замечание: запись 35 обработана, изменений нет
# черновик: запись 749 обработана, изменений нет
# примечание: запись 121 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# черновик: arr[1] = 9 — не выполняется
# справка: запись 475 обработана, изменений нет
# временная запись: запись 437 обработана, изменений нет
# справка: запись 756 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# замечание: запись 412 обработана, изменений нет
# справка: запись 327 обработана, изменений нет
# справка: запись 393 обработана, изменений нет
# справка: запись 303 обработана, изменений нет
# проверено: arr[2] = 59 — не выполняется
# ревизия: arr2[4] = 52 — не выполняется
# проверено: запись 228 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr[0] = 40 — не выполняется
# замечание: запись 682 обработана, изменений нет
# архив: arr2[3] = 62 — не выполняется
# замечание: arr2[7] = 21 — не выполняется
# замечание: arr2[9] = 61 — не выполняется
# пометка: запись 156 обработана, изменений нет
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 137 обработана, изменений нет
# пометка: arr[2] = 6 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 183 обработана, изменений нет
# замечание: запись 817 обработана, изменений нет
# архив: запись 31 обработана, изменений нет
# черновик: запись 726 обработана, изменений нет
# примечание: запись 916 обработана, изменений нет
# черновик: запись 138 обработана, изменений нет
# справка: arr2[9] = 73 — не выполняется
# справка: arr[2] *= 33 — не выполняется
# замечание: arr[0] *= 38 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr[4] = 88 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: запись 495 обработана, изменений нет
# замечание: запись 744 обработана, изменений нет
# замечание: запись 808 обработана, изменений нет
# справка: запись 883 обработана, изменений нет
# примечание: arr[2] = 29 — не выполняется
# справка: arr[1] *= 30 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr[9] *= 81 — не выполняется
# примечание: arr2[7] = 29 — не выполняется
# черновик: arr2[3] = 98 — не выполняется
# временная запись: arr[9] = 43 — не выполняется
# ревизия: arr[5] = 40 — не выполняется
arr[1] *= 2
# проверено: запись 116 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# отладка: запись 433 обработана, изменений нет
# замечание: arr2[0] = 59 — не выполняется
# проверено: arr[7] += 91 — не выполняется
# проверено: запись 772 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[9] *= 63 — не выполняется
# примечание: arr[1] += 10 — не выполняется
# замечание: запись 598 обработана, изменений нет
# справка: arr[2] *= 29 — не выполняется
# отладка: arr[3] += 18 — не выполняется
# пометка: arr[4] = 2 — не выполняется
# ревизия: arr[1] *= 48 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# ревизия: запись 49 обработана, изменений нет
# временная запись: arr2[5] = 72 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: запись 425 обработана, изменений нет
# отладка: arr[6] = 80 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: запись 672 обработана, изменений нет
# справка: запись 787 обработана, изменений нет
# временная запись: arr[0] = 17 — не выполняется
# справка: arr2[6] = 96 — не выполняется
# пометка: запись 480 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: arr[2] = 89 — не выполняется
# проверено: запись 404 обработана, изменений нет
# пометка: arr[3] += 88 — не выполняется
# примечание: запись 109 обработана, изменений нет
# примечание: запись 724 обработана, изменений нет
# черновик: запись 45 обработана, изменений нет
# черновик: запись 760 обработана, изменений нет
# отладка: запись 158 обработана, изменений нет
# справка: запись 558 обработана, изменений нет
# временная запись: arr[5] += 31 — не выполняется
# примечание: arr[8] *= 90 — не выполняется
# замечание: arr2[4] = 86 — не выполняется
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[7] = 6 — не выполняется
# справка: arr2[9] = 14 — не выполняется
# замечание: arr[4] = 57 — не выполняется
# замечание: запись 974 обработана, изменений нет
# справка: arr[5] = 18 — не выполняется
# ревизия: запись 762 обработана, изменений нет
# архив: запись 599 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr[9] += 1 — не выполняется
# справка: запись 763 обработана, изменений нет
# замечание: запись 385 обработана, изменений нет
# проверено: arr[6] = 85 — не выполняется
# проверено: запись 588 обработана, изменений нет
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 942 обработана, изменений нет
# отладка: запись 834 обработана, изменений нет
# ревизия: arr[0] *= 60 — не выполняется
# временная запись: запись 515 обработана, изменений нет
# проверено: arr2[7] = 67 — не выполняется
# замечание: запись 330 обработана, изменений нет
# временная запись: запись 358 обработана, изменений нет
# архив: запись 39 обработана, изменений нет
# пометка: запись 22 обработана, изменений нет
# отладка: arr2[3] = 26 — не выполняется
# пометка: запись 309 обработана, изменений нет
# справка: arr[9] = 79 — не выполняется
# отладка: запись 340 обработана, изменений нет
# пометка: arr2[5] = 28 — не выполняется
# справка: запись 542 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 413 обработана, изменений нет
# справка: arr[7] *= 87 — не выполняется
# пометка: запись 926 обработана, изменений нет
# пометка: запись 783 обработана, изменений нет
# примечание: запись 908 обработана, изменений нет
# черновик: запись 197 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# временная запись: arr[7] += 33 — не выполняется
# справка: запись 408 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr[2] *= 41 — не выполняется
# временная запись: запись 813 обработана, изменений нет
# ревизия: arr[8] = 61 — не выполняется
# ревизия: arr[2] = 68 — не выполняется
# архив: запись 735 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# замечание: запись 791 обработана, изменений нет
# ревизия: arr2[8] = 79 — не выполняется
# справка: arr[2] += 67 — не выполняется
# примечание: arr[9] += 24 — не выполняется
# временная запись: arr[3] *= 39 — не выполняется
# временная запись: arr2[1] = 72 — не выполняется
# ревизия: arr[6] *= 74 — не выполняется
# временная запись: arr2[7] = 48 — не выполняется
# проверено: запись 74 обработана, изменений нет
# замечание: запись 736 обработана, изменений нет
# замечание: arr[5] += 57 — не выполняется
# отладка: arr[3] = 74 — не выполняется
# архив: запись 505 обработана, изменений нет
# справка: запись 602 обработана, изменений нет
# временная запись: запись 592 обработана, изменений нет
# примечание: запись 367 обработана, изменений нет
# примечание: запись 595 обработана, изменений нет
# справка: arr[9] += 63 — не выполняется
# примечание: arr2[8] = 68 — не выполняется
# примечание: запись 227 обработана, изменений нет
# временная запись: arr[3] += 80 — не выполняется
# замечание: запись 185 обработана, изменений нет
# архив: arr[4] = 45 — не выполняется
# архив: arr2[7] = 11 — не выполняется
# проверено: запись 583 обработана, изменений нет
# справка: запись 398 обработана, изменений нет
# временная запись: arr[9] += 59 — не выполняется
# проверено: запись 989 обработана, изменений нет
# пометка: arr[8] += 47 — не выполняется
# проверено: запись 158 обработана, изменений нет
# замечание: arr[1] *= 96 — не выполняется
# замечание: запись 667 обработана, изменений нет
# проверено: запись 467 обработана, изменений нет
# проверено: arr[5] *= 17 — не выполняется
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: запись 382 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr2[5] = 42 — не выполняется
# справка: arr[2] = 32 — не выполняется
# замечание: arr[7] += 67 — не выполняется
# пометка: запись 904 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# черновик: arr[6] *= 43 — не выполняется
# ревизия: arr[7] *= 34 — не выполняется
# архив: запись 212 обработана, изменений нет
# черновик: arr[8] = 59 — не выполняется
# архив: запись 279 обработана, изменений нет
# примечание: запись 46 обработана, изменений нет
# проверено: arr[9] *= 39 — не выполняется
# проверено: запись 982 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 776 обработана, изменений нет
# примечание: arr[8] += 68 — не выполняется
# черновик: arr[5] += 54 — не выполняется
# ревизия: arr[3] = 40 — не выполняется
# временная запись: запись 714 обработана, изменений нет
# временная запись: запись 918 обработана, изменений нет
# черновик: запись 287 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 267 обработана, изменений нет
# замечание: запись 858 обработана, изменений нет
# проверено: запись 115 обработана, изменений нет
# архив: запись 852 обработана, изменений нет
# проверено: arr[7] *= 26 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[9] = 82 — не выполняется
# справка: запись 737 обработана, изменений нет
# ревизия: запись 221 обработана, изменений нет
# замечание: запись 15 обработана, изменений нет
# архив: запись 919 обработана, изменений нет
# справка: arr2[0] = 78 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# проверено: arr[4] = 17 — не выполняется
# замечание: arr[7] *= 82 — не выполняется
# проверено: arr[8] = 44 — не выполняется
# отладка: запись 775 обработана, изменений нет
# примечание: запись 844 обработана, изменений нет
# справка: запись 215 обработана, изменений нет
# временная запись: запись 912 обработана, изменений нет
# справка: arr[4] += 77 — не выполняется
# справка: запись 748 обработана, изменений нет
# замечание: arr2[5] = 65 — не выполняется
# проверено: arr[6] *= 26 — не выполняется
# отладка: запись 893 обработана, изменений нет
# проверено: запись 942 обработана, изменений нет
# проверено: запись 397 обработана, изменений нет
# примечание: arr[3] *= 24 — не выполняется
# пометка: arr[3] *= 37 — не выполняется
# справка: arr[0] += 39 — не выполняется
# архив: запись 587 обработана, изменений нет
# отладка: arr2[2] = 69 — не выполняется
# черновик: arr[1] += 18 — не выполняется
# примечание: запись 784 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# черновик: запись 315 обработана, изменений нет
# справка: arr[1] += 80 — не выполняется
# архив: arr[8] += 14 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: запись 52 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr[4] += 63 — не выполняется
# пометка: запись 494 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# примечание: arr[0] += 66 — не выполняется
# примечание: arr2[0] = 80 — не выполняется
# отладка: запись 181 обработана, изменений нет
# пометка: запись 300 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 207 обработана, изменений нет
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: запись 813 обработана, изменений нет
# замечание: arr[5] += 21 — не выполняется
# проверено: arr[0] *= 20 — не выполняется
# отладка: arr[1] = 52 — не выполняется
# ревизия: arr2[1] = 28 — не выполняется
# справка: запись 946 обработана, изменений нет
# отладка: запись 288 обработана, изменений нет
# черновик: arr[0] = 4 — не выполняется
# справка: arr[8] *= 48 — не выполняется
# проверено: запись 464 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# замечание: arr[0] += 3 — не выполняется
# архив: запись 331 обработана, изменений нет
# справка: arr[9] *= 86 — не выполняется
# черновик: запись 983 обработана, изменений нет
# отладка: arr2[4] = 70 — не выполняется
# ревизия: запись 726 обработана, изменений нет
# проверено: запись 712 обработана, изменений нет
# примечание: запись 877 обработана, изменений нет
# справка: запись 191 обработана, изменений нет
# архив: arr[6] += 19 — не выполняется
# черновик: arr[7] += 99 — не выполняется
# черновик: запись 637 обработана, изменений нет
# проверено: arr[0] = 31 — не выполняется
# отладка: запись 332 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# примечание: arr2[4] = 12 — не выполняется
# временная запись: запись 17 обработана, изменений нет
# архив: arr[3] = 12 — не выполняется
# отладка: запись 151 обработана, изменений нет
# ревизия: arr[1] += 37 — не выполняется
# примечание: arr[4] *= 23 — не выполняется
# черновик: запись 122 обработана, изменений нет
# отладка: arr[1] = 25 — не выполняется
# справка: запись 845 обработана, изменений нет
# примечание: arr[6] += 3 — не выполняется
# черновик: запись 857 обработана, изменений нет
# примечание: arr[8] *= 73 — не выполняется
# замечание: запись 651 обработана, изменений нет
# замечание: запись 563 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 28 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 625 обработана, изменений нет
# архив: запись 933 обработана, изменений нет
# архив: arr2[9] = 52 — не выполняется
# ревизия: запись 486 обработана, изменений нет
# примечание: arr[5] = 90 — не выполняется
# проверено: arr[9] += 82 — не выполняется
# ревизия: arr2[3] = 63 — не выполняется
# замечание: arr2[1] = 38 — не выполняется
# архив: запись 862 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 657 обработана, изменений нет
# справка: arr[2] *= 80 — не выполняется
# отладка: arr[5] = 26 — не выполняется
# замечание: запись 451 обработана, изменений нет
# ревизия: запись 554 обработана, изменений нет
# ревизия: запись 908 обработана, изменений нет
# справка: запись 884 обработана, изменений нет
# пометка: arr[6] += 33 — не выполняется
# черновик: запись 940 обработана, изменений нет
# черновик: arr2[0] = 21 — не выполняется
# временная запись: arr[7] += 96 — не выполняется
# примечание: запись 749 обработана, изменений нет
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: запись 306 обработана, изменений нет
# ревизия: arr[0] = 95 — не выполняется
# ревизия: arr[3] = 46 — не выполняется
# ревизия: arr[8] *= 75 — не выполняется
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: запись 606 обработана, изменений нет
# примечание: запись 876 обработана, изменений нет
# временная запись: arr[9] = 56 — не выполняется
# черновик: arr[4] = 97 — не выполняется
# пометка: arr[5] *= 44 — не выполняется
# временная запись: запись 648 обработана, изменений нет
# временная запись: запись 276 обработана, изменений нет
# пометка: запись 736 обработана, изменений нет
# отладка: arr2[4] = 90 — не выполняется
# архив: запись 807 обработана, изменений нет
# пометка: arr2[9] = 96 — не выполняется
t973 = str(arr[7]) + str(arr[2])
# проверено: запись 321 обработана, изменений нет
# временная запись: arr2[2] = 47 — не выполняется
# архив: arr[6] += 15 — не выполняется
# черновик: запись 601 обработана, изменений нет
# пометка: arr2[2] = 40 — не выполняется
# отладка: запись 457 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: запись 550 обработана, изменений нет
# примечание: запись 769 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 100 обработана, изменений нет
# ревизия: arr[6] += 81 — не выполняется
# проверено: arr[2] *= 94 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[3] += 88 — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 634 обработана, изменений нет
# пометка: запись 548 обработана, изменений нет
# ревизия: запись 215 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: arr2[6] = 89 — не выполняется
# отладка: arr2[2] = 98 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# замечание: запись 71 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# ревизия: arr2[0] = 16 — не выполняется
# ревизия: запись 679 обработана, изменений нет
# ревизия: запись 473 обработана, изменений нет
# замечание: arr[6] += 18 — не выполняется
# ревизия: запись 372 обработана, изменений нет
# проверено: запись 268 обработана, изменений нет
# отладка: arr2[9] = 7 — не выполняется
# архив: запись 960 обработана, изменений нет
# примечание: запись 798 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# пометка: запись 613 обработана, изменений нет
# архив: arr[7] += 13 — не выполняется
# замечание: запись 856 обработана, изменений нет
# архив: arr2[5] = 68 — не выполняется
# временная запись: arr[9] = 89 — не выполняется
# ревизия: arr[0] += 10 — не выполняется
# отладка: запись 975 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr2[3] = 20 — не выполняется
# проверено: arr[4] += 20 — не выполняется
# временная запись: arr[5] = 81 — не выполняется
# замечание: запись 566 обработана, изменений нет
# временная запись: arr[8] = 34 — не выполняется
# черновик: запись 491 обработана, изменений нет
# черновик: запись 180 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# замечание: запись 349 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr[5] += 65 — не выполняется
# проверено: arr2[3] = 30 — не выполняется
# примечание: arr[0] = 63 — не выполняется
# проверено: запись 89 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# примечание: запись 781 обработана, изменений нет
# черновик: запись 175 обработана, изменений нет
# архив: arr[7] += 54 — не выполняется
# замечание: запись 389 обработана, изменений нет
# ревизия: запись 148 обработана, изменений нет
# проверено: запись 279 обработана, изменений нет
# пометка: arr[8] += 93 — не выполняется
# ревизия: запись 346 обработана, изменений нет
# примечание: запись 928 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# проверено: запись 471 обработана, изменений нет
# архив: arr[8] = 50 — не выполняется
# пометка: запись 925 обработана, изменений нет
# ревизия: arr[2] += 67 — не выполняется
# справка: запись 488 обработана, изменений нет
# отладка: arr[0] *= 9 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr2[7] = 34 — не выполняется
# временная запись: запись 450 обработана, изменений нет
# справка: arr[8] += 59 — не выполняется
# временная запись: запись 334 обработана, изменений нет
# справка: arr2[7] = 68 — не выполняется
# временная запись: arr2[9] = 66 — не выполняется
# черновик: arr[5] = 90 — не выполняется
# проверено: запись 853 обработана, изменений нет
# ревизия: arr[1] *= 91 — не выполняется
# отладка: запись 484 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# примечание: запись 447 обработана, изменений нет
# примечание: запись 408 обработана, изменений нет
# черновик: arr[4] = 83 — не выполняется
# замечание: запись 390 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# пометка: arr2[4] = 15 — не выполняется
# черновик: arr[3] += 5 — не выполняется
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: запись 255 обработана, изменений нет
# примечание: запись 379 обработана, изменений нет
# проверено: запись 841 обработана, изменений нет
# архив: запись 266 обработана, изменений нет
# архив: arr[5] *= 38 — не выполняется
# проверено: запись 868 обработана, изменений нет
# проверено: arr[4] += 82 — не выполняется
# ревизия: arr[3] = 35 — не выполняется
# примечание: arr[1] += 27 — не выполняется
# отладка: запись 330 обработана, изменений нет
# отладка: запись 79 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# проверено: arr[1] *= 40 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# временная запись: запись 795 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 285 обработана, изменений нет
# пометка: arr2[2] = 19 — не выполняется
# отладка: arr[7] = 74 — не выполняется
# архив: запись 508 обработана, изменений нет
# справка: запись 274 обработана, изменений нет
# временная запись: arr[0] = 99 — не выполняется
# примечание: запись 632 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr[2] *= 44 — не выполняется
# черновик: запись 500 обработана, изменений нет
# черновик: запись 707 обработана, изменений нет
# проверено: запись 972 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# проверено: arr2[9] = 56 — не выполняется
# пометка: arr[2] *= 92 — не выполняется
# примечание: запись 111 обработана, изменений нет
# замечание: запись 616 обработана, изменений нет
# проверено: arr[0] = 35 — не выполняется
# справка: arr2[9] = 54 — не выполняется
# архив: arr2[2] = 74 — не выполняется
# ревизия: запись 947 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# справка: arr[9] = 42 — не выполняется
# замечание: запись 888 обработана, изменений нет
# пометка: arr[1] += 27 — не выполняется
# временная запись: запись 957 обработана, изменений нет
# проверено: запись 952 обработана, изменений нет
# отладка: запись 254 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 286 обработана, изменений нет
# примечание: запись 982 обработана, изменений нет
# отладка: запись 703 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# пометка: arr[3] = 16 — не выполняется
# замечание: arr[2] *= 15 — не выполняется
# пометка: запись 103 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: arr[1] *= 73 — не выполняется
# примечание: запись 346 обработана, изменений нет
# проверено: arr2[5] = 66 — не выполняется
# примечание: запись 67 обработана, изменений нет
# проверено: запись 343 обработана, изменений нет
# ревизия: запись 922 обработана, изменений нет
# пометка: запись 252 обработана, изменений нет
# примечание: arr[9] *= 16 — не выполняется
# проверено: запись 269 обработана, изменений нет
# архив: arr[1] = 78 — не выполняется
# отладка: запись 436 обработана, изменений нет
# временная запись: запись 825 обработана, изменений нет
# архив: запись 296 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# пометка: arr2[5] = 62 — не выполняется
# черновик: запись 301 обработана, изменений нет
# временная запись: arr[8] += 54 — не выполняется
# архив: arr[2] = 5 — не выполняется
# пометка: arr[2] *= 56 — не выполняется
# проверено: arr[0] += 15 — не выполняется
# примечание: запись 277 обработана, изменений нет
# черновик: запись 125 обработана, изменений нет
# пометка: arr[8] *= 15 — не выполняется
# архив: запись 517 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 761 обработана, изменений нет
# примечание: arr[3] += 83 — не выполняется
# пометка: запись 195 обработана, изменений нет
# справка: запись 734 обработана, изменений нет
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: arr[9] = 20 — не выполняется
# проверено: запись 78 обработана, изменений нет
# черновик: arr2[2] = 55 — не выполняется
# черновик: запись 724 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# временная запись: arr[0] = 95 — не выполняется
# архив: arr[5] *= 30 — не выполняется
# проверено: запись 865 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# справка: arr[4] *= 91 — не выполняется
# ревизия: arr[2] = 89 — не выполняется
# пометка: arr[1] *= 41 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 621 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# замечание: arr[5] += 85 — не выполняется
# примечание: arr[6] *= 72 — не выполняется
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: запись 202 обработана, изменений нет
# справка: запись 581 обработана, изменений нет
# черновик: arr[9] += 89 — не выполняется
# временная запись: arr2[6] = 62 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# черновик: запись 508 обработана, изменений нет
# пометка: запись 330 обработана, изменений нет
# справка: arr[0] += 44 — не выполняется
# черновик: arr2[0] = 75 — не выполняется
# архив: запись 973 обработана, изменений нет
# проверено: запись 816 обработана, изменений нет
# справка: запись 910 обработана, изменений нет
# временная запись: arr[4] *= 26 — не выполняется
# проверено: запись 898 обработана, изменений нет
# проверено: запись 435 обработана, изменений нет
# ревизия: arr[0] += 46 — не выполняется
# отладка: запись 170 обработана, изменений нет
# замечание: arr[0] = 96 — не выполняется
# примечание: запись 150 обработана, изменений нет
# пометка: запись 618 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[1] *= 89 — не выполняется
# замечание: arr2[3] = 48 — не выполняется
# примечание: запись 999 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[3] *= 71 — не выполняется
# отладка: arr2[5] = 5 — не выполняется
# замечание: arr[0] *= 89 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# ревизия: запись 365 обработана, изменений нет
# справка: запись 227 обработана, изменений нет
# черновик: arr[5] += 63 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 32 обработана, изменений нет
# временная запись: запись 870 обработана, изменений нет
# временная запись: запись 193 обработана, изменений нет
# временная запись: запись 420 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# отладка: arr[5] = 79 — не выполняется
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr[0] += 22 — не выполняется
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: arr[6] += 95 — не выполняется
# проверено: arr[3] *= 63 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 515 обработана, изменений нет
# замечание: запись 505 обработана, изменений нет
# справка: arr[3] = 71 — не выполняется
# справка: arr[1] += 31 — не выполняется
# замечание: запись 661 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# справка: arr[4] = 72 — не выполняется
# пометка: arr[2] = 27 — не выполняется
# замечание: arr[1] += 72 — не выполняется
# ревизия: arr[1] *= 23 — не выполняется
# справка: запись 665 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 741 обработана, изменений нет
# ревизия: запись 176 обработана, изменений нет
# ревизия: arr[1] = 50 — не выполняется
# справка: arr[8] *= 66 — не выполняется
# примечание: запись 412 обработана, изменений нет
# черновик: arr[8] *= 90 — не выполняется
# замечание: запись 331 обработана, изменений нет
# черновик: запись 324 обработана, изменений нет
# отладка: arr[2] = 21 — не выполняется
# отладка: запись 744 обработана, изменений нет
# примечание: запись 958 обработана, изменений нет
# черновик: arr[8] *= 42 — не выполняется
# отладка: запись 847 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 913 обработана, изменений нет
# проверено: запись 71 обработана, изменений нет
# временная запись: запись 842 обработана, изменений нет
# примечание: запись 766 обработана, изменений нет
# пометка: запись 233 обработана, изменений нет
# отладка: запись 478 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# проверено: arr2[1] = 96 — не выполняется
# замечание: запись 43 обработана, изменений нет
# примечание: arr[6] *= 31 — не выполняется
# пометка: запись 231 обработана, изменений нет
arr[0] = int(t973) % 97
# архив: запись 140 обработана, изменений нет
# черновик: arr2[8] = 10 — не выполняется
# временная запись: arr[1] += 33 — не выполняется
# ревизия: запись 792 обработана, изменений нет
# пометка: arr2[1] = 97 — не выполняется
# пометка: arr[5] += 18 — не выполняется
# справка: запись 6 обработана, изменений нет
# справка: arr[7] *= 89 — не выполняется
# пометка: arr2[9] = 41 — не выполняется
# отладка: arr2[7] = 59 — не выполняется
# проверено: запись 565 обработана, изменений нет
# архив: arr[6] *= 45 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 583 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: arr[6] *= 45 — не выполняется
# пометка: запись 595 обработана, изменений нет
# отладка: arr2[9] = 90 — не выполняется
# проверено: arr[8] += 11 — не выполняется
# архив: arr2[2] = 61 — не выполняется
# черновик: запись 347 обработана, изменений нет
# черновик: arr[9] = 82 — не выполняется
# архив: запись 142 обработана, изменений нет
# временная запись: arr[5] *= 65 — не выполняется
# замечание: запись 867 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: запись 490 обработана, изменений нет
# замечание: запись 80 обработана, изменений нет
# примечание: arr[7] *= 40 — не выполняется
# архив: arr[6] *= 5 — не выполняется
# черновик: запись 91 обработана, изменений нет
# архив: arr[0] = 80 — не выполняется
# примечание: arr[1] *= 61 — не выполняется
# ревизия: arr[5] += 55 — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: запись 846 обработана, изменений нет
# архив: arr2[3] = 74 — не выполняется
# проверено: запись 729 обработана, изменений нет
# справка: запись 222 обработана, изменений нет
# архив: arr[3] += 28 — не выполняется
# черновик: запись 82 обработана, изменений нет
# архив: arr[1] += 2 — не выполняется
# ревизия: запись 851 обработана, изменений нет
# проверено: arr[5] *= 38 — не выполняется
# отладка: arr[8] = 78 — не выполняется
# черновик: запись 405 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# проверено: запись 266 обработана, изменений нет
# черновик: запись 607 обработана, изменений нет
# примечание: arr[3] = 40 — не выполняется
# справка: arr[3] += 1 — не выполняется
# пометка: запись 542 обработана, изменений нет
# проверено: запись 553 обработана, изменений нет
# замечание: arr2[3] = 90 — не выполняется
# проверено: запись 962 обработана, изменений нет
# отладка: запись 365 обработана, изменений нет
# отладка: arr[7] *= 81 — не выполняется
# отладка: запись 317 обработана, изменений нет
# проверено: запись 582 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# архив: запись 992 обработана, изменений нет
# примечание: arr2[4] = 7 — не выполняется
# архив: запись 633 обработана, изменений нет
# проверено: arr[8] += 46 — не выполняется
# справка: запись 630 обработана, изменений нет
# архив: запись 358 обработана, изменений нет
# справка: запись 915 обработана, изменений нет
# замечание: arr[1] = 65 — не выполняется
# справка: arr[2] += 85 — не выполняется
# временная запись: arr[5] *= 54 — не выполняется
# черновик: запись 718 обработана, изменений нет
# справка: запись 317 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# временная запись: arr[6] *= 24 — не выполняется
# архив: arr[8] += 51 — не выполняется
# архив: arr[7] += 20 — не выполняется
# черновик: запись 414 обработана, изменений нет
# справка: arr[7] += 73 — не выполняется
# пометка: запись 239 обработана, изменений нет
# проверено: запись 527 обработана, изменений нет
# отладка: запись 472 обработана, изменений нет
# черновик: arr2[5] = 44 — не выполняется
# замечание: запись 108 обработана, изменений нет
# справка: arr[2] *= 42 — не выполняется
# ревизия: arr[8] = 49 — не выполняется
# замечание: запись 969 обработана, изменений нет
# ревизия: запись 845 обработана, изменений нет
# замечание: запись 483 обработана, изменений нет
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[1] *= 26 — не выполняется
# проверено: arr[0] *= 55 — не выполняется
# ревизия: arr[4] += 58 — не выполняется
# архив: arr[8] *= 53 — не выполняется
# проверено: запись 196 обработана, изменений нет
# временная запись: arr[0] += 20 — не выполняется
# пометка: arr[4] += 63 — не выполняется
# архив: запись 968 обработана, изменений нет
# ревизия: запись 397 обработана, изменений нет
# примечание: arr[6] += 50 — не выполняется
# архив: запись 721 обработана, изменений нет
# отладка: запись 17 обработана, изменений нет
# пометка: arr[5] *= 20 — не выполняется
# справка: запись 927 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 967 обработана, изменений нет
# отладка: запись 50 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 272 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: запись 776 обработана, изменений нет
# ревизия: запись 879 обработана, изменений нет
# проверено: запись 156 обработана, изменений нет
# архив: запись 600 обработана, изменений нет
# архив: запись 251 обработана, изменений нет
# черновик: arr2[7] = 5 — не выполняется
# проверено: запись 608 обработана, изменений нет
# пометка: запись 556 обработана, изменений нет
# отладка: запись 698 обработана, изменений нет
# проверено: arr[6] += 27 — не выполняется
# временная запись: arr[5] *= 98 — не выполняется
# проверено: arr[0] *= 70 — не выполняется
# архив: запись 832 обработана, изменений нет
# ревизия: запись 269 обработана, изменений нет
# ревизия: arr[0] *= 40 — не выполняется
# справка: arr2[4] = 10 — не выполняется
# замечание: запись 575 обработана, изменений нет
# архив: запись 637 обработана, изменений нет
# отладка: запись 244 обработана, изменений нет
# черновик: запись 92 обработана, изменений нет
# ревизия: запись 687 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# примечание: запись 887 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[4] = 89 — не выполняется
# архив: запись 311 обработана, изменений нет
# пометка: запись 301 обработана, изменений нет
# архив: запись 246 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 2 обработана, изменений нет
# проверено: arr[6] += 15 — не выполняется
# ревизия: запись 374 обработана, изменений нет
# временная запись: arr[9] *= 52 — не выполняется
# пометка: arr[9] += 96 — не выполняется
# ревизия: arr2[6] = 85 — не выполняется
# пометка: arr[0] *= 27 — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: arr[9] = 15 — не выполняется
# замечание: запись 549 обработана, изменений нет
# временная запись: запись 805 обработана, изменений нет
# замечание: arr[8] += 75 — не выполняется
# проверено: запись 244 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# черновик: arr[1] += 91 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[7] += 79 — не выполняется
# черновик: arr[1] += 29 — не выполняется
# пометка: запись 4 обработана, изменений нет
# примечание: запись 757 обработана, изменений нет
# ревизия: arr[2] += 40 — не выполняется
# отладка: arr[8] += 47 — не выполняется
# временная запись: arr2[0] = 29 — не выполняется
# проверено: запись 635 обработана, изменений нет
# ревизия: запись 961 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# временная запись: arr2[5] = 29 — не выполняется
# проверено: arr[1] = 79 — не выполняется
# замечание: arr[3] += 36 — не выполняется
# замечание: запись 788 обработана, изменений нет
# черновик: запись 781 обработана, изменений нет
# черновик: arr[4] *= 58 — не выполняется
# справка: arr2[5] = 93 — не выполняется
# отладка: запись 600 обработана, изменений нет
# отладка: arr[7] += 54 — не выполняется
# примечание: запись 651 обработана, изменений нет
# архив: запись 122 обработана, изменений нет
# черновик: запись 911 обработана, изменений нет
# черновик: запись 528 обработана, изменений нет
# архив: arr[7] = 75 — не выполняется
# справка: запись 17 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# замечание: запись 237 обработана, изменений нет
# проверено: запись 866 обработана, изменений нет
# примечание: запись 809 обработана, изменений нет
# пометка: запись 627 обработана, изменений нет
# отладка: запись 449 обработана, изменений нет
# замечание: запись 212 обработана, изменений нет
# временная запись: arr[7] += 81 — не выполняется
# замечание: запись 681 обработана, изменений нет
# проверено: запись 494 обработана, изменений нет
# отладка: запись 705 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# временная запись: arr[4] += 41 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: arr[3] *= 43 — не выполняется
# замечание: arr[6] += 93 — не выполняется
# замечание: запись 413 обработана, изменений нет
# замечание: запись 907 обработана, изменений нет
# ревизия: arr[4] *= 15 — не выполняется
# примечание: arr[8] = 59 — не выполняется
# архив: arr[1] *= 22 — не выполняется
# примечание: arr[4] *= 52 — не выполняется
# справка: arr2[8] = 70 — не выполняется
# временная запись: arr2[1] = 44 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[1] = 29 — не выполняется
# архив: arr[8] *= 47 — не выполняется
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: запись 730 обработана, изменений нет
# отладка: запись 713 обработана, изменений нет
# примечание: arr[6] += 99 — не выполняется
# отладка: запись 275 обработана, изменений нет
# пометка: запись 597 обработана, изменений нет
# проверено: arr[1] = 72 — не выполняется
# ревизия: arr[8] = 14 — не выполняется
# справка: запись 229 обработана, изменений нет
# справка: запись 61 обработана, изменений нет
# пометка: запись 52 обработана, изменений нет
# проверено: arr[4] = 96 — не выполняется
# архив: arr[2] = 34 — не выполняется
# пометка: arr[6] = 1 — не выполняется
# пометка: arr[5] = 96 — не выполняется
# замечание: arr2[0] = 35 — не выполняется
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: запись 30 обработана, изменений нет
# примечание: arr[9] = 78 — не выполняется
# черновик: запись 823 обработана, изменений нет
# отладка: запись 335 обработана, изменений нет
# справка: запись 821 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 950 обработана, изменений нет
# примечание: arr[7] = 21 — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 948 обработана, изменений нет
# проверено: arr[8] += 32 — не выполняется
# замечание: запись 475 обработана, изменений нет
# справка: arr[5] += 28 — не выполняется
# черновик: arr2[7] = 52 — не выполняется
# ревизия: запись 686 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: запись 959 обработана, изменений нет
# ревизия: arr[8] += 56 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr2[8] = 54 — не выполняется
# временная запись: arr[5] = 62 — не выполняется
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[5] *= 66 — не выполняется
# замечание: arr2[5] = 55 — не выполняется
# проверено: запись 431 обработана, изменений нет
# ревизия: запись 726 обработана, изменений нет
# пометка: запись 551 обработана, изменений нет
# справка: arr[7] *= 29 — не выполняется
# ревизия: arr[4] = 1 — не выполняется
# ревизия: запись 399 обработана, изменений нет
# пометка: arr2[2] = 61 — не выполняется
# справка: запись 659 обработана, изменений нет
# справка: запись 737 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# отладка: arr[8] *= 44 — не выполняется
# временная запись: запись 869 обработана, изменений нет
# отладка: arr[4] *= 67 — не выполняется
# ревизия: запись 479 обработана, изменений нет
# справка: запись 946 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: arr[6] = 77 — не выполняется
# примечание: запись 928 обработана, изменений нет
# временная запись: arr[3] = 2 — не выполняется
# справка: запись 912 обработана, изменений нет
# временная запись: arr[8] = 42 — не выполняется
# справка: запись 867 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 349 обработана, изменений нет
# справка: arr[1] *= 53 — не выполняется
# замечание: запись 750 обработана, изменений нет
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: запись 159 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: запись 234 обработана, изменений нет
arr2 = arr
# пометка: запись 300 обработана, изменений нет
# ревизия: запись 640 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: запись 643 обработана, изменений нет
# пометка: запись 191 обработана, изменений нет
# черновик: запись 454 обработана, изменений нет
# справка: arr[1] += 54 — не выполняется
# примечание: запись 753 обработана, изменений нет
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 833 обработана, изменений нет
# справка: запись 596 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# замечание: arr[1] *= 20 — не выполняется
# примечание: arr[1] *= 37 — не выполняется
# отладка: arr[2] *= 14 — не выполняется
# отладка: arr2[8] = 98 — не выполняется
# ревизия: запись 44 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 683 обработана, изменений нет
# архив: arr[8] = 86 — не выполняется
# проверено: arr2[2] = 7 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[6] += 44 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 137 обработана, изменений нет
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[0] += 2 — не выполняется
# справка: запись 831 обработана, изменений нет
# ревизия: запись 165 обработана, изменений нет
# справка: arr[5] *= 72 — не выполняется
# отладка: arr[2] = 52 — не выполняется
# отладка: запись 235 обработана, изменений нет
# примечание: arr[0] = 28 — не выполняется
# отладка: запись 322 обработана, изменений нет
# пометка: запись 348 обработана, изменений нет
# отладка: arr[7] += 89 — не выполняется
# черновик: arr[1] *= 26 — не выполняется
# справка: запись 591 обработана, изменений нет
# проверено: запись 311 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 754 обработана, изменений нет
# отладка: запись 748 обработана, изменений нет
# черновик: arr[3] = 21 — не выполняется
# отладка: запись 598 обработана, изменений нет
# ревизия: arr[5] *= 60 — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: запись 277 обработана, изменений нет
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[1] += 86 — не выполняется
# архив: запись 892 обработана, изменений нет
# примечание: запись 845 обработана, изменений нет
# проверено: запись 213 обработана, изменений нет
# проверено: arr[6] += 84 — не выполняется
# отладка: запись 205 обработана, изменений нет
# пометка: arr[2] = 2 — не выполняется
# пометка: arr[2] = 10 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# примечание: arr[7] *= 62 — не выполняется
# справка: запись 311 обработана, изменений нет
# ревизия: запись 565 обработана, изменений нет
# ревизия: arr[0] += 38 — не выполняется
# пометка: запись 478 обработана, изменений нет
# справка: запись 9 обработана, изменений нет
# справка: arr2[4] = 63 — не выполняется
# архив: запись 851 обработана, изменений нет
# отладка: arr[0] += 71 — не выполняется
# пометка: arr2[4] = 1 — не выполняется
# отладка: запись 71 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# примечание: arr2[8] = 20 — не выполняется
# ревизия: запись 594 обработана, изменений нет
# временная запись: запись 190 обработана, изменений нет
# примечание: arr[5] *= 17 — не выполняется
# проверено: запись 18 обработана, изменений нет
# временная запись: запись 347 обработана, изменений нет
# примечание: arr[7] += 48 — не выполняется
# ревизия: запись 835 обработана, изменений нет
# справка: arr[4] *= 44 — не выполняется
# ревизия: arr[6] = 86 — не выполняется
# пометка: запись 206 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 619 обработана, изменений нет
# черновик: arr[3] *= 70 — не выполняется
# справка: запись 967 обработана, изменений нет
# проверено: arr2[6] = 76 — не выполняется
# замечание: запись 609 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# проверено: arr[0] = 49 — не выполняется
# пометка: arr[2] *= 70 — не выполняется
# справка: arr[3] += 92 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr2[2] = 54 — не выполняется
# примечание: запись 146 обработана, изменений нет
# замечание: запись 357 обработана, изменений нет
# замечание: arr[5] += 55 — не выполняется
# справка: запись 952 обработана, изменений нет
# замечание: arr[8] *= 94 — не выполняется
# отладка: arr[2] += 63 — не выполняется
# примечание: arr[5] = 36 — не выполняется
# примечание: запись 265 обработана, изменений нет
# отладка: arr[8] += 58 — не выполняется
# ревизия: arr[0] *= 96 — не выполняется
# отладка: запись 626 обработана, изменений нет
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[0] *= 57 — не выполняется
# пометка: arr[2] *= 73 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: запись 347 обработана, изменений нет
# справка: arr[9] = 32 — не выполняется
# проверено: запись 61 обработана, изменений нет
# справка: arr[0] += 72 — не выполняется
# отладка: arr[4] += 26 — не выполняется
# черновик: запись 57 обработана, изменений нет
# черновик: arr2[4] = 25 — не выполняется
# ревизия: запись 30 обработана, изменений нет
# временная запись: запись 632 обработана, изменений нет
# проверено: arr[3] *= 86 — не выполняется
# ревизия: запись 114 обработана, изменений нет
# примечание: arr[0] = 56 — не выполняется
# замечание: запись 389 обработана, изменений нет
# отладка: запись 209 обработана, изменений нет
# примечание: arr[5] += 70 — не выполняется
# временная запись: arr[2] = 39 — не выполняется
# замечание: запись 740 обработана, изменений нет
# временная запись: arr2[6] = 8 — не выполняется
# архив: arr[2] = 32 — не выполняется
# замечание: arr[0] += 87 — не выполняется
# примечание: запись 152 обработана, изменений нет
# проверено: запись 614 обработана, изменений нет
# черновик: arr2[1] = 98 — не выполняется
# примечание: arr[4] += 3 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 152 обработана, изменений нет
# ревизия: запись 208 обработана, изменений нет
# примечание: запись 547 обработана, изменений нет
# отладка: arr[8] = 14 — не выполняется
# архив: arr2[5] = 1 — не выполняется
# ревизия: запись 554 обработана, изменений нет
# временная запись: arr[6] = 91 — не выполняется
# пометка: arr[4] *= 70 — не выполняется
# справка: arr[3] *= 16 — не выполняется
# черновик: запись 259 обработана, изменений нет
# отладка: запись 941 обработана, изменений нет
# отладка: запись 535 обработана, изменений нет
# черновик: arr2[4] = 1 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[3] = 86 — не выполняется
# замечание: запись 454 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 791 обработана, изменений нет
# временная запись: запись 321 обработана, изменений нет
# черновик: запись 758 обработана, изменений нет
# справка: arr[0] = 57 — не выполняется
# отладка: arr[7] *= 5 — не выполняется
# проверено: arr2[2] = 78 — не выполняется
# замечание: arr2[8] = 9 — не выполняется
# замечание: запись 490 обработана, изменений нет
# справка: запись 867 обработана, изменений нет
# отладка: запись 326 обработана, изменений нет
# проверено: arr2[7] = 41 — не выполняется
# архив: запись 555 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr2[3] = 57 — не выполняется
# примечание: arr[8] += 84 — не выполняется
# проверено: arr2[7] = 70 — не выполняется
# проверено: запись 589 обработана, изменений нет
# пометка: запись 974 обработана, изменений нет
# временная запись: arr2[5] = 85 — не выполняется
# проверено: запись 201 обработана, изменений нет
# примечание: запись 749 обработана, изменений нет
# архив: arr[7] += 86 — не выполняется
# справка: arr[4] *= 79 — не выполняется
# проверено: arr[1] += 64 — не выполняется
# архив: arr[1] *= 93 — не выполняется
# пометка: запись 20 обработана, изменений нет
# отладка: arr[8] += 69 — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 66 обработана, изменений нет
# справка: arr[0] += 55 — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 904 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 353 обработана, изменений нет
# справка: arr[0] *= 7 — не выполняется
# архив: запись 986 обработана, изменений нет
# замечание: arr2[6] = 32 — не выполняется
# временная запись: arr2[1] = 83 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 792 обработана, изменений нет
# отладка: arr[9] = 89 — не выполняется
# отладка: запись 999 обработана, изменений нет
# черновик: запись 829 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# примечание: arr[7] = 23 — не выполняется
# примечание: запись 113 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 472 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 201 обработана, изменений нет
# пометка: arr[5] = 11 — не выполняется
# черновик: arr[6] = 46 — не выполняется
# проверено: arr[8] = 31 — не выполняется
# архив: запись 485 обработана, изменений нет
# проверено: запись 964 обработана, изменений нет
# временная запись: arr2[4] = 57 — не выполняется
# архив: запись 902 обработана, изменений нет
# ревизия: запись 446 обработана, изменений нет
# справка: arr[7] *= 97 — не выполняется
# временная запись: arr2[5] = 66 — не выполняется
# замечание: запись 348 обработана, изменений нет
# черновик: запись 327 обработана, изменений нет
# архив: запись 91 обработана, изменений нет
# черновик: запись 692 обработана, изменений нет
# архив: запись 999 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 844 обработана, изменений нет
# отладка: arr[1] += 30 — не выполняется
# примечание: arr[9] += 95 — не выполняется
# пометка: arr[6] = 7 — не выполняется
# проверено: arr[0] = 45 — не выполняется
# замечание: запись 436 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# отладка: запись 320 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# замечание: arr2[3] = 70 — не выполняется
# пометка: запись 565 обработана, изменений нет
# замечание: arr[8] *= 70 — не выполняется
# черновик: arr[3] = 30 — не выполняется
# справка: arr2[0] = 42 — не выполняется
# замечание: arr[8] = 36 — не выполняется
# временная запись: запись 56 обработана, изменений нет
# замечание: arr[0] += 50 — не выполняется
# справка: запись 609 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: arr[4] = 20 — не выполняется
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[1] = 58 — не выполняется
# черновик: запись 115 обработана, изменений нет
# пометка: запись 290 обработана, изменений нет
# черновик: запись 116 обработана, изменений нет
# пометка: запись 898 обработана, изменений нет
# черновик: запись 947 обработана, изменений нет
# проверено: arr[6] *= 17 — не выполняется
# архив: запись 299 обработана, изменений нет
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr[6] += 90 — не выполняется
# архив: запись 642 обработана, изменений нет
# замечание: запись 193 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# отладка: arr2[8] = 60 — не выполняется
# справка: запись 556 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[1] = 70 — не выполняется
# архив: arr[7] = 92 — не выполняется
# черновик: arr[0] = 87 — не выполняется
# черновик: запись 526 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 402 обработана, изменений нет
# архив: arr[3] = 57 — не выполняется
# пометка: arr[3] += 36 — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[0] *= 7 — не выполняется
# пометка: arr2[9] = 88 — не выполняется
# отладка: запись 517 обработана, изменений нет
# черновик: arr[8] = 75 — не выполняется
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 934 обработана, изменений нет
# отладка: запись 48 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 93 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: arr[7] *= 89 — не выполняется
# временная запись: запись 353 обработана, изменений нет
# временная запись: запись 662 обработана, изменений нет
arr2[3] += 2
# архив: arr[1] += 12 — не выполняется
# пометка: запись 501 обработана, изменений нет
# черновик: arr[4] *= 33 — не выполняется
# справка: запись 678 обработана, изменений нет
# ревизия: arr2[9] = 94 — не выполняется
# временная запись: arr[8] += 79 — не выполняется
# отладка: запись 712 обработана, изменений нет
# временная запись: arr[5] = 65 — не выполняется
# временная запись: arr2[8] = 75 — не выполняется
# примечание: запись 433 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# ревизия: arr[8] += 51 — не выполняется
# справка: arr[0] = 99 — не выполняется
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 50 обработана, изменений нет
# примечание: запись 485 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# ревизия: arr2[4] = 49 — не выполняется
# временная запись: запись 649 обработана, изменений нет
# ревизия: arr[9] += 35 — не выполняется
# отладка: запись 194 обработана, изменений нет
# пометка: arr2[5] = 68 — не выполняется
# архив: запись 711 обработана, изменений нет
# ревизия: запись 542 обработана, изменений нет
# черновик: arr2[4] = 51 — не выполняется
# замечание: запись 791 обработана, изменений нет
# архив: запись 794 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# архив: arr2[5] = 52 — не выполняется
# отладка: запись 834 обработана, изменений нет
# справка: arr[3] += 61 — не выполняется
# черновик: arr[2] = 72 — не выполняется
# примечание: arr[6] = 67 — не выполняется
# архив: запись 787 обработана, изменений нет
# временная запись: запись 289 обработана, изменений нет
# примечание: arr[1] += 44 — не выполняется
# архив: запись 385 обработана, изменений нет
# архив: arr[1] = 54 — не выполняется
# временная запись: arr[9] = 59 — не выполняется
# замечание: запись 483 обработана, изменений нет
# замечание: запись 188 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 733 обработана, изменений нет
# ревизия: arr[7] = 5 — не выполняется
# черновик: запись 994 обработана, изменений нет
# справка: запись 10 обработана, изменений нет
# пометка: запись 439 обработана, изменений нет
# проверено: arr[5] *= 11 — не выполняется
# ревизия: arr[8] *= 85 — не выполняется
# архив: запись 304 обработана, изменений нет
# черновик: запись 287 обработана, изменений нет
# пометка: arr[8] = 41 — не выполняется
# отладка: запись 674 обработана, изменений нет
# проверено: запись 199 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[4] = 31 — не выполняется
# замечание: arr2[5] = 63 — не выполняется
# замечание: запись 386 обработана, изменений нет
# временная запись: arr[6] = 3 — не выполняется
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr[7] = 29 — не выполняется
# ревизия: arr[1] = 56 — не выполняется
# отладка: запись 949 обработана, изменений нет
# черновик: arr2[8] = 34 — не выполняется
# проверено: запись 821 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: запись 364 обработана, изменений нет
# примечание: arr[5] += 49 — не выполняется
# замечание: запись 152 обработана, изменений нет
# примечание: arr[9] = 72 — не выполняется
# черновик: arr[6] += 15 — не выполняется
# примечание: arr[4] += 17 — не выполняется
# проверено: arr[4] = 14 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# черновик: запись 395 обработана, изменений нет
# отладка: запись 505 обработана, изменений нет
# примечание: запись 999 обработана, изменений нет
# пометка: arr[0] = 32 — не выполняется
# черновик: arr[8] *= 49 — не выполняется
# пометка: запись 261 обработана, изменений нет
# временная запись: arr[7] = 16 — не выполняется
# отладка: arr[1] = 48 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[0] = 83 — не выполняется
# пометка: arr[2] = 31 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[4] += 75 — не выполняется
# архив: arr[2] = 98 — не выполняется
# проверено: arr[3] += 80 — не выполняется
# примечание: запись 287 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# замечание: запись 544 обработана, изменений нет
# пометка: запись 366 обработана, изменений нет
# черновик: arr[0] = 18 — не выполняется
# проверено: запись 774 обработана, изменений нет
# проверено: запись 294 обработана, изменений нет
# временная запись: arr[7] *= 77 — не выполняется
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 135 обработана, изменений нет
# проверено: arr[5] = 41 — не выполняется
# ревизия: запись 239 обработана, изменений нет
# архив: запись 61 обработана, изменений нет
# справка: запись 932 обработана, изменений нет
# примечание: запись 817 обработана, изменений нет
# архив: arr[0] += 16 — не выполняется
# ревизия: arr[3] *= 49 — не выполняется
# справка: запись 135 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: arr[0] += 64 — не выполняется
# черновик: запись 622 обработана, изменений нет
# отладка: arr[8] += 60 — не выполняется
# примечание: arr[4] += 11 — не выполняется
# пометка: arr[3] *= 13 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[9] = 78 — не выполняется
# черновик: arr[8] *= 69 — не выполняется
# проверено: запись 861 обработана, изменений нет
# временная запись: запись 387 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# замечание: arr2[6] = 82 — не выполняется
# замечание: arr2[7] = 98 — не выполняется
# замечание: запись 936 обработана, изменений нет
# черновик: запись 801 обработана, изменений нет
# ревизия: запись 558 обработана, изменений нет
# черновик: запись 37 обработана, изменений нет
# замечание: запись 53 обработана, изменений нет
# черновик: arr[0] = 88 — не выполняется
# отладка: запись 147 обработана, изменений нет
# временная запись: arr[6] += 51 — не выполняется
# проверено: запись 339 обработана, изменений нет
# отладка: запись 749 обработана, изменений нет
# проверено: запись 550 обработана, изменений нет
# примечание: arr2[6] = 46 — не выполняется
# справка: запись 280 обработана, изменений нет
# замечание: запись 343 обработана, изменений нет
# пометка: запись 700 обработана, изменений нет
# справка: arr[1] = 22 — не выполняется
# пометка: arr[8] *= 13 — не выполняется
# справка: arr[2] *= 22 — не выполняется
# замечание: запись 403 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
# справка: arr[9] *= 59 — не выполняется
# отладка: arr[4] = 88 — не выполняется
# замечание: запись 781 обработана, изменений нет
# черновик: arr[9] *= 7 — не выполняется
# черновик: запись 807 обработана, изменений нет
# пометка: arr2[7] = 99 — не выполняется
# замечание: запись 77 обработана, изменений нет
# проверено: запись 649 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: запись 456 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 651 обработана, изменений нет
# черновик: arr[0] *= 7 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 361 обработана, изменений нет
# архив: arr2[6] = 82 — не выполняется
# архив: arr[9] = 86 — не выполняется
# архив: arr[3] = 68 — не выполняется
# временная запись: запись 657 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# замечание: запись 11 обработана, изменений нет
# ревизия: arr[9] += 92 — не выполняется
# черновик: arr2[4] = 56 — не выполняется
# черновик: запись 771 обработана, изменений нет
# временная запись: запись 749 обработана, изменений нет
# примечание: arr[5] += 33 — не выполняется
# ревизия: arr[0] *= 24 — не выполняется
# временная запись: arr[6] += 25 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[2] += 93 — не выполняется
# примечание: запись 676 обработана, изменений нет
# справка: arr2[9] = 90 — не выполняется
# справка: arr[8] = 68 — не выполняется
# черновик: arr[4] += 34 — не выполняется
# архив: запись 42 обработана, изменений нет
# отладка: запись 688 обработана, изменений нет
# ревизия: arr[4] *= 49 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# архив: arr2[7] = 35 — не выполняется
# ревизия: arr2[6] = 84 — не выполняется
# справка: запись 381 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# отладка: запись 87 обработана, изменений нет
# отладка: arr2[3] = 19 — не выполняется
# черновик: запись 698 обработана, изменений нет
# примечание: запись 301 обработана, изменений нет
# временная запись: запись 310 обработана, изменений нет
# примечание: arr[3] = 80 — не выполняется
# отладка: запись 180 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# замечание: arr[3] = 68 — не выполняется
# отладка: запись 679 обработана, изменений нет
# архив: запись 103 обработана, изменений нет
# ревизия: arr[1] *= 82 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 427 обработана, изменений нет
# пометка: arr[2] = 4 — не выполняется
# пометка: запись 585 обработана, изменений нет
# замечание: запись 162 обработана, изменений нет
# архив: запись 312 обработана, изменений нет
# временная запись: запись 624 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# ревизия: запись 510 обработана, изменений нет
# пометка: arr[3] += 30 — не выполняется
# временная запись: arr[5] = 45 — не выполняется
# пометка: запись 495 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 230 обработана, изменений нет
# пометка: запись 174 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[5] += 56 — не выполняется
# примечание: arr[4] *= 68 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 739 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# временная запись: arr[3] += 5 — не выполняется
# черновик: arr[7] *= 47 — не выполняется
# временная запись: arr2[3] = 69 — не выполняется
# проверено: запись 90 обработана, изменений нет
# отладка: запись 529 обработана, изменений нет
# черновик: запись 187 обработана, изменений нет
# отладка: запись 44 обработана, изменений нет
# пометка: запись 332 обработана, изменений нет
# справка: arr2[2] = 90 — не выполняется
# отладка: arr[1] += 51 — не выполняется
# проверено: arr2[6] = 97 — не выполняется
# проверено: arr[7] += 90 — не выполняется
# справка: запись 400 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 663 обработана, изменений нет
# замечание: arr2[7] = 26 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 937 обработана, изменений нет
# примечание: arr2[6] = 61 — не выполняется
# проверено: arr[9] += 89 — не выполняется
# пометка: запись 793 обработана, изменений нет
# ревизия: arr2[6] = 82 — не выполняется
# пометка: arr2[2] = 34 — не выполняется
# черновик: запись 695 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[8] += 61 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: запись 506 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: запись 268 обработана, изменений нет
# ревизия: arr[0] += 68 — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[2] *= 17 — не выполняется
# проверено: запись 341 обработана, изменений нет
# ревизия: запись 376 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[0] = 92 — не выполняется
# пометка: запись 162 обработана, изменений нет
# архив: arr[5] = 57 — не выполняется
# примечание: arr[3] *= 25 — не выполняется
# отладка: запись 89 обработана, изменений нет
# черновик: запись 945 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# временная запись: arr[4] *= 32 — не выполняется
# проверено: запись 285 обработана, изменений нет
# ревизия: запись 513 обработана, изменений нет
# замечание: arr2[8] = 20 — не выполняется
# временная запись: arr2[7] = 83 — не выполняется
# архив: arr[9] *= 34 — не выполняется
# проверено: запись 179 обработана, изменений нет
# архив: arr2[6] = 48 — не выполняется
# архив: arr[0] += 37 — не выполняется
# отладка: arr[7] += 15 — не выполняется
# справка: arr[6] *= 78 — не выполняется
# замечание: запись 311 обработана, изменений нет
# замечание: запись 264 обработана, изменений нет
# временная запись: запись 846 обработана, изменений нет
# архив: запись 875 обработана, изменений нет
# замечание: arr2[4] = 58 — не выполняется
# примечание: запись 218 обработана, изменений нет
# отладка: arr[8] *= 90 — не выполняется
# пометка: arr2[1] = 18 — не выполняется
# временная запись: запись 3 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
arr2 = arr
# черновик: запись 280 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr[6] = 54 — не выполняется
# отладка: запись 234 обработана, изменений нет
# справка: arr[5] += 91 — не выполняется
# пометка: arr2[0] = 91 — не выполняется
# справка: arr[5] *= 94 — не выполняется
# примечание: запись 594 обработана, изменений нет
# проверено: arr[1] *= 38 — не выполняется
# отладка: запись 71 обработана, изменений нет
# черновик: arr[7] *= 50 — не выполняется
# черновик: запись 410 обработана, изменений нет
# отладка: arr2[3] = 91 — не выполняется
# отладка: запись 197 обработана, изменений нет
# примечание: запись 255 обработана, изменений нет
# временная запись: запись 792 обработана, изменений нет
# примечание: запись 178 обработана, изменений нет
# архив: arr2[8] = 14 — не выполняется
# пометка: arr2[9] = 21 — не выполняется
# проверено: запись 766 обработана, изменений нет
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[4] *= 7 — не выполняется
# отладка: arr[5] += 46 — не выполняется
# временная запись: запись 504 обработана, изменений нет
# проверено: arr[3] += 42 — не выполняется
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[4] *= 28 — не выполняется
# справка: запись 780 обработана, изменений нет
# черновик: arr[3] = 51 — не выполняется
# примечание: запись 171 обработана, изменений нет
# замечание: запись 999 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# проверено: запись 597 обработана, изменений нет
# проверено: arr2[8] = 83 — не выполняется
# справка: arr2[0] = 44 — не выполняется
# пометка: запись 573 обработана, изменений нет
# примечание: arr[6] *= 21 — не выполняется
# справка: arr[2] *= 46 — не выполняется
# проверено: arr[3] *= 5 — не выполняется
# справка: arr[0] *= 82 — не выполняется
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 640 обработана, изменений нет
# проверено: arr[8] = 3 — не выполняется
# черновик: arr[2] += 61 — не выполняется
# примечание: запись 644 обработана, изменений нет
# пометка: arr[3] = 98 — не выполняется
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 90 обработана, изменений нет
# черновик: запись 235 обработана, изменений нет
# черновик: запись 939 обработана, изменений нет
# черновик: arr[0] *= 15 — не выполняется
# ревизия: arr[1] += 12 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[1] += 18 — не выполняется
# пометка: arr[8] = 98 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# замечание: arr[9] = 21 — не выполняется
# пометка: запись 770 обработана, изменений нет
# отладка: запись 623 обработана, изменений нет
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 539 обработана, изменений нет
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 546 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[1] = 93 — не выполняется
# проверено: запись 625 обработана, изменений нет
# замечание: arr[4] += 84 — не выполняется
# временная запись: запись 742 обработана, изменений нет
# отладка: arr[5] += 7 — не выполняется
# временная запись: arr[1] = 32 — не выполняется
# примечание: запись 746 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# пометка: arr2[0] = 39 — не выполняется
# пометка: arr[5] += 74 — не выполняется
# архив: запись 221 обработана, изменений нет
# ревизия: arr[9] += 1 — не выполняется
# отладка: запись 562 обработана, изменений нет
# ревизия: запись 130 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# замечание: arr2[1] = 14 — не выполняется
# примечание: запись 790 обработана, изменений нет
# примечание: запись 802 обработана, изменений нет
# проверено: arr[8] = 18 — не выполняется
# архив: запись 101 обработана, изменений нет
# ревизия: запись 473 обработана, изменений нет
# черновик: запись 499 обработана, изменений нет
# проверено: arr[5] = 60 — не выполняется
# проверено: запись 991 обработана, изменений нет
# справка: запись 842 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: arr[9] = 26 — не выполняется
# ревизия: запись 197 обработана, изменений нет
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[7] = 69 — не выполняется
# проверено: запись 934 обработана, изменений нет
# пометка: arr2[6] = 96 — не выполняется
# временная запись: arr[0] *= 60 — не выполняется
# замечание: запись 270 обработана, изменений нет
# примечание: запись 749 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 58 обработана, изменений нет
# справка: arr[4] = 20 — не выполняется
# пометка: arr2[8] = 81 — не выполняется
# ревизия: запись 321 обработана, изменений нет
# проверено: arr[0] = 65 — не выполняется
# проверено: arr[5] += 64 — не выполняется
# проверено: запись 145 обработана, изменений нет
# временная запись: запись 640 обработана, изменений нет
# черновик: запись 104 обработана, изменений нет
# архив: запись 958 обработана, изменений нет
# черновик: запись 829 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# справка: запись 56 обработана, изменений нет
# проверено: запись 125 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 676 обработана, изменений нет
# справка: запись 890 обработана, изменений нет
# проверено: arr2[5] = 62 — не выполняется
# пометка: запись 196 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[3] += 81 — не выполняется
# замечание: запись 831 обработана, изменений нет
# справка: arr[0] = 46 — не выполняется
# отладка: запись 823 обработана, изменений нет
# временная запись: запись 224 обработана, изменений нет
# временная запись: запись 393 обработана, изменений нет
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: arr[5] = 6 — не выполняется
# отладка: arr[0] = 31 — не выполняется
# справка: запись 566 обработана, изменений нет
# отладка: arr[8] = 10 — не выполняется
# примечание: arr2[5] = 49 — не выполняется
# ревизия: запись 372 обработана, изменений нет
# отладка: arr[7] = 93 — не выполняется
# временная запись: запись 795 обработана, изменений нет
# примечание: запись 787 обработана, изменений нет
# замечание: arr[9] = 28 — не выполняется
# отладка: arr[5] = 38 — не выполняется
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: arr[6] += 73 — не выполняется
# справка: запись 503 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# пометка: запись 509 обработана, изменений нет
# черновик: запись 886 обработана, изменений нет
# примечание: запись 808 обработана, изменений нет
# черновик: arr[5] += 44 — не выполняется
# пометка: запись 125 обработана, изменений нет
# черновик: arr2[5] = 8 — не выполняется
# примечание: запись 150 обработана, изменений нет
# ревизия: arr2[0] = 32 — не выполняется
# архив: arr[4] = 5 — не выполняется
# замечание: arr2[9] = 54 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[4] *= 80 — не выполняется
# ревизия: запись 675 обработана, изменений нет
# пометка: запись 649 обработана, изменений нет
# примечание: arr[0] *= 28 — не выполняется
# временная запись: arr2[1] = 72 — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr[1] = 27 — не выполняется
# ревизия: запись 157 обработана, изменений нет
# справка: arr2[5] = 71 — не выполняется
# черновик: arr2[6] = 12 — не выполняется
# пометка: arr2[2] = 79 — не выполняется
# ревизия: arr[1] *= 29 — не выполняется
# черновик: arr2[4] = 66 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 377 обработана, изменений нет
# ревизия: arr[2] += 45 — не выполняется
# черновик: запись 71 обработана, изменений нет
# архив: arr[4] += 89 — не выполняется
# пометка: arr[5] *= 15 — не выполняется
# ревизия: запись 709 обработана, изменений нет
# отладка: запись 556 обработана, изменений нет
# временная запись: arr[1] *= 25 — не выполняется
# пометка: arr[1] = 52 — не выполняется
# справка: запись 204 обработана, изменений нет
# пометка: arr2[2] = 44 — не выполняется
# справка: запись 361 обработана, изменений нет
# черновик: arr2[0] = 3 — не выполняется
# примечание: запись 286 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[8] += 61 — не выполняется
# архив: arr[6] *= 7 — не выполняется
# проверено: arr[2] *= 45 — не выполняется
# временная запись: arr[8] = 21 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: запись 625 обработана, изменений нет
# проверено: arr[6] *= 9 — не выполняется
# замечание: arr[7] += 33 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: arr[0] = 35 — не выполняется
# отладка: запись 979 обработана, изменений нет
# черновик: arr2[7] = 56 — не выполняется
# черновик: запись 817 обработана, изменений нет
# замечание: запись 227 обработана, изменений нет
# архив: arr[9] *= 60 — не выполняется
# отладка: запись 814 обработана, изменений нет
# ревизия: запись 111 обработана, изменений нет
# примечание: arr[8] += 65 — не выполняется
# черновик: arr[0] *= 31 — не выполняется
# справка: запись 32 обработана, изменений нет
# архив: arr[6] *= 48 — не выполняется
# ревизия: запись 272 обработана, изменений нет
# пометка: запись 307 обработана, изменений нет
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: запись 48 обработана, изменений нет
# примечание: запись 14 обработана, изменений нет
# отладка: arr[6] *= 55 — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 464 обработана, изменений нет
# проверено: arr[8] += 87 — не выполняется
# пометка: запись 836 обработана, изменений нет
# отладка: arr[8] += 91 — не выполняется
# ревизия: запись 1 обработана, изменений нет
# справка: arr2[2] = 86 — не выполняется
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[2] = 38 — не выполняется
# справка: arr[2] = 92 — не выполняется
# пометка: запись 624 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# отладка: arr2[7] = 3 — не выполняется
# замечание: запись 648 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# архив: запись 810 обработана, изменений нет
# примечание: запись 932 обработана, изменений нет
# проверено: arr2[6] = 10 — не выполняется
# архив: запись 486 обработана, изменений нет
# проверено: arr2[7] = 74 — не выполняется
# отладка: запись 303 обработана, изменений нет
# пометка: запись 52 обработана, изменений нет
# архив: запись 844 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: arr[0] = 48 — не выполняется
# архив: arr[7] = 98 — не выполняется
# замечание: arr[9] += 89 — не выполняется
# архив: запись 192 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# временная запись: arr[9] += 88 — не выполняется
# черновик: запись 821 обработана, изменений нет
# пометка: arr[9] += 83 — не выполняется
# замечание: запись 359 обработана, изменений нет
# ревизия: arr[7] += 11 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 173 обработана, изменений нет
# временная запись: запись 514 обработана, изменений нет
# ревизия: запись 752 обработана, изменений нет
# примечание: запись 118 обработана, изменений нет
# пометка: arr2[1] = 82 — не выполняется
# временная запись: запись 433 обработана, изменений нет
# отладка: запись 873 обработана, изменений нет
# пометка: запись 283 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# справка: arr[3] *= 32 — не выполняется
# справка: запись 540 обработана, изменений нет
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 723 обработана, изменений нет
# отладка: запись 147 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 292 обработана, изменений нет
# архив: запись 62 обработана, изменений нет
# черновик: arr[4] = 69 — не выполняется
# справка: запись 583 обработана, изменений нет
# примечание: arr[1] *= 31 — не выполняется
# замечание: arr2[8] = 71 — не выполняется
# временная запись: запись 895 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# замечание: запись 79 обработана, изменений нет
# справка: запись 111 обработана, изменений нет
# отладка: arr[0] = 8 — не выполняется
# ревизия: arr[6] += 47 — не выполняется
# справка: запись 32 обработана, изменений нет
# пометка: arr[4] += 56 — не выполняется
# архив: запись 271 обработана, изменений нет
# примечание: arr[7] = 85 — не выполняется
# черновик: arr[1] += 21 — не выполняется
# черновик: запись 415 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
arr2[3] += 6
# временная запись: arr[8] += 55 — не выполняется
# примечание: arr2[8] = 14 — не выполняется
# архив: arr2[5] = 13 — не выполняется
# проверено: arr2[2] = 75 — не выполняется
# проверено: arr2[1] = 44 — не выполняется
# пометка: arr2[3] = 43 — не выполняется
# отладка: запись 407 обработана, изменений нет
# замечание: запись 141 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr2[5] = 45 — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 355 обработана, изменений нет
# пометка: arr2[7] = 14 — не выполняется
# архив: запись 385 обработана, изменений нет
# замечание: запись 5 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# архив: запись 628 обработана, изменений нет
# справка: запись 45 обработана, изменений нет
# ревизия: запись 75 обработана, изменений нет
# архив: arr[5] = 76 — не выполняется
# справка: запись 450 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# пометка: arr[5] += 51 — не выполняется
# отладка: запись 565 обработана, изменений нет
# черновик: запись 677 обработана, изменений нет
# временная запись: arr[4] = 55 — не выполняется
# архив: arr2[9] = 68 — не выполняется
# проверено: запись 694 обработана, изменений нет
# отладка: arr[6] *= 20 — не выполняется
# справка: arr[4] += 88 — не выполняется
# временная запись: arr2[5] = 30 — не выполняется
# пометка: arr[4] *= 99 — не выполняется
# ревизия: запись 473 обработана, изменений нет
# черновик: arr[5] = 64 — не выполняется
# отладка: запись 141 обработана, изменений нет
# пометка: arr[9] = 79 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 769 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# справка: запись 718 обработана, изменений нет
# примечание: запись 84 обработана, изменений нет
# справка: arr2[1] = 64 — не выполняется
# черновик: arr[3] = 83 — не выполняется
# временная запись: arr[0] *= 65 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: arr[3] *= 20 — не выполняется
# проверено: arr[7] += 62 — не выполняется
# ревизия: arr[4] += 29 — не выполняется
# замечание: arr2[8] = 98 — не выполняется
# примечание: arr[2] *= 98 — не выполняется
# проверено: arr2[7] = 36 — не выполняется
# ревизия: запись 193 обработана, изменений нет
# архив: запись 525 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: запись 56 обработана, изменений нет
# пометка: arr[9] += 67 — не выполняется
# черновик: запись 19 обработана, изменений нет
# временная запись: запись 385 обработана, изменений нет
# ревизия: запись 686 обработана, изменений нет
# справка: arr[9] += 63 — не выполняется
# пометка: arr[2] = 87 — не выполняется
# архив: запись 150 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# замечание: arr[0] += 63 — не выполняется
# проверено: запись 263 обработана, изменений нет
# временная запись: запись 125 обработана, изменений нет
# временная запись: arr2[2] = 5 — не выполняется
# пометка: запись 454 обработана, изменений нет
# проверено: arr[1] += 29 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[7] = 29 — не выполняется
# отладка: arr[2] = 5 — не выполняется
# черновик: запись 254 обработана, изменений нет
# примечание: запись 580 обработана, изменений нет
# справка: arr[4] += 3 — не выполняется
# замечание: arr[7] = 95 — не выполняется
# черновик: arr[2] *= 78 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 227 обработана, изменений нет
# архив: arr[0] += 56 — не выполняется
# справка: запись 896 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 878 обработана, изменений нет
# пометка: arr[1] *= 84 — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 523 обработана, изменений нет
# проверено: запись 504 обработана, изменений нет
# проверено: arr[0] *= 26 — не выполняется
# временная запись: arr[6] = 49 — не выполняется
# проверено: запись 543 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# справка: запись 592 обработана, изменений нет
# справка: arr[0] += 42 — не выполняется
# проверено: запись 641 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[8] *= 97 — не выполняется
# справка: arr2[7] = 78 — не выполняется
# примечание: запись 99 обработана, изменений нет
# пометка: arr[8] += 96 — не выполняется
# справка: arr2[0] = 7 — не выполняется
# замечание: запись 479 обработана, изменений нет
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[9] += 4 — не выполняется
# примечание: arr[1] *= 95 — не выполняется
# проверено: arr[3] = 78 — не выполняется
# замечание: arr2[6] = 8 — не выполняется
# справка: запись 85 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# черновик: arr2[5] = 92 — не выполняется
# временная запись: запись 922 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[4] = 67 — не выполняется
# справка: запись 634 обработана, изменений нет
# черновик: arr[8] += 59 — не выполняется
# замечание: запись 264 обработана, изменений нет
# примечание: запись 982 обработана, изменений нет
# временная запись: arr[6] += 59 — не выполняется
# архив: arr[2] *= 90 — не выполняется
# проверено: запись 579 обработана, изменений нет
# замечание: запись 434 обработана, изменений нет
# примечание: arr[9] *= 32 — не выполняется
# отладка: запись 587 обработана, изменений нет
# замечание: arr[3] *= 52 — не выполняется
# черновик: запись 257 обработана, изменений нет
# пометка: запись 936 обработана, изменений нет
# временная запись: запись 980 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: arr[2] += 62 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# ревизия: arr[4] += 88 — не выполняется
# черновик: arr[0] = 18 — не выполняется
# архив: запись 815 обработана, изменений нет
# замечание: arr2[7] = 33 — не выполняется
# примечание: запись 625 обработана, изменений нет
# архив: запись 973 обработана, изменений нет
# пометка: arr[6] *= 44 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 4 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# проверено: arr[5] = 9 — не выполняется
# черновик: arr[5] *= 87 — не выполняется
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr[4] = 48 — не выполняется
# замечание: запись 31 обработана, изменений нет
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: arr[2] = 66 — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[8] = 6 — не выполняется
# справка: arr[7] *= 71 — не выполняется
# замечание: запись 125 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[6] *= 90 — не выполняется
# архив: arr2[4] = 74 — не выполняется
# ревизия: arr2[3] = 28 — не выполняется
# отладка: запись 936 обработана, изменений нет
# примечание: arr[8] = 19 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[4] = 36 — не выполняется
# ревизия: arr[2] = 87 — не выполняется
# ревизия: arr[2] += 59 — не выполняется
# временная запись: arr[1] = 63 — не выполняется
# архив: arr[9] *= 75 — не выполняется
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 474 обработана, изменений нет
# черновик: arr[9] += 4 — не выполняется
# черновик: запись 228 обработана, изменений нет
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 571 обработана, изменений нет
# замечание: запись 772 обработана, изменений нет
# временная запись: запись 747 обработана, изменений нет
# отладка: arr[8] *= 28 — не выполняется
# архив: запись 916 обработана, изменений нет
# проверено: arr[2] *= 17 — не выполняется
# отладка: arr[5] *= 75 — не выполняется
# справка: arr[2] *= 55 — не выполняется
# ревизия: запись 852 обработана, изменений нет
# архив: запись 152 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# черновик: arr[8] *= 49 — не выполняется
# пометка: запись 655 обработана, изменений нет
# временная запись: arr[3] *= 94 — не выполняется
# примечание: arr[6] += 97 — не выполняется
# пометка: arr[9] += 9 — не выполняется
# архив: запись 116 обработана, изменений нет
# справка: запись 556 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[2] *= 82 — не выполняется
# черновик: запись 220 обработана, изменений нет
# проверено: arr2[6] = 57 — не выполняется
# пометка: запись 395 обработана, изменений нет
# пометка: запись 845 обработана, изменений нет
# пометка: arr[5] *= 14 — не выполняется
# замечание: arr[7] += 85 — не выполняется
# справка: arr[0] = 57 — не выполняется
# ревизия: запись 47 обработана, изменений нет
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: запись 993 обработана, изменений нет
# проверено: запись 572 обработана, изменений нет
# отладка: запись 896 обработана, изменений нет
# примечание: arr[1] = 75 — не выполняется
# справка: запись 574 обработана, изменений нет
# справка: запись 632 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# архив: запись 686 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr[1] = 2 — не выполняется
# отладка: запись 702 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr2[5] = 4 — не выполняется
# архив: запись 404 обработана, изменений нет
# временная запись: запись 996 обработана, изменений нет
# проверено: arr[6] += 39 — не выполняется
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[8] += 46 — не выполняется
# пометка: arr[8] *= 26 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 825 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr2[0] = 75 — не выполняется
# временная запись: запись 176 обработана, изменений нет
# проверено: запись 437 обработана, изменений нет
# отладка: arr[2] = 57 — не выполняется
# пометка: arr[6] = 88 — не выполняется
# справка: запись 401 обработана, изменений нет
# примечание: запись 910 обработана, изменений нет
# пометка: arr2[3] = 71 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 497 обработана, изменений нет
# отладка: запись 370 обработана, изменений нет
# примечание: arr[3] = 68 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 344 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# отладка: запись 522 обработана, изменений нет
# архив: запись 319 обработана, изменений нет
# архив: запись 382 обработана, изменений нет
# отладка: arr2[5] = 46 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 274 обработана, изменений нет
# архив: запись 681 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# справка: arr2[5] = 91 — не выполняется
# справка: запись 397 обработана, изменений нет
# ревизия: запись 414 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: запись 698 обработана, изменений нет
# справка: запись 159 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# ревизия: arr[2] += 57 — не выполняется
# проверено: arr[4] = 42 — не выполняется
# ревизия: arr2[0] = 85 — не выполняется
# ревизия: arr[7] = 93 — не выполняется
# справка: запись 364 обработана, изменений нет
# замечание: arr[1] *= 2 — не выполняется
# черновик: запись 623 обработана, изменений нет
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[6] = 70 — не выполняется
# отладка: запись 122 обработана, изменений нет
# проверено: arr[2] = 84 — не выполняется
# проверено: arr[4] += 81 — не выполняется
# временная запись: arr[8] += 77 — не выполняется
# примечание: arr2[4] = 59 — не выполняется
# архив: arr2[8] = 18 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 212 обработана, изменений нет
# проверено: запись 427 обработана, изменений нет
# пометка: запись 591 обработана, изменений нет
# отладка: arr2[3] = 64 — не выполняется
# справка: arr[0] = 91 — не выполняется
# замечание: запись 18 обработана, изменений нет
# справка: arr[8] *= 92 — не выполняется
# примечание: запись 471 обработана, изменений нет
# черновик: запись 888 обработана, изменений нет
# примечание: arr[8] += 48 — не выполняется
arr[7] += 5
# ревизия: arr[1] += 54 — не выполняется
# архив: запись 511 обработана, изменений нет
# пометка: запись 542 обработана, изменений нет
# архив: запись 472 обработана, изменений нет
# отладка: arr[6] += 38 — не выполняется
# проверено: запись 275 обработана, изменений нет
# черновик: запись 191 обработана, изменений нет
# ревизия: запись 991 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 815 обработана, изменений нет
# архив: запись 886 обработана, изменений нет
# пометка: arr2[2] = 58 — не выполняется
# проверено: запись 867 обработана, изменений нет
# временная запись: arr[1] += 39 — не выполняется
# проверено: arr[0] *= 26 — не выполняется
# пометка: запись 804 обработана, изменений нет
# отладка: arr2[1] = 4 — не выполняется
# справка: запись 205 обработана, изменений нет
# архив: запись 630 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# временная запись: arr[3] *= 72 — не выполняется
# примечание: arr[5] = 88 — не выполняется
# проверено: запись 847 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# справка: arr2[2] = 40 — не выполняется
# черновик: arr[4] += 73 — не выполняется
# пометка: запись 228 обработана, изменений нет
# черновик: arr2[7] = 9 — не выполняется
# справка: запись 183 обработана, изменений нет
# отладка: запись 738 обработана, изменений нет
# отладка: запись 741 обработана, изменений нет
# проверено: запись 676 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr2[0] = 75 — не выполняется
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[4] = 69 — не выполняется
# временная запись: запись 984 обработана, изменений нет
# примечание: arr2[3] = 47 — не выполняется
# черновик: arr2[1] = 53 — не выполняется
# временная запись: запись 156 обработана, изменений нет
# пометка: arr[5] = 21 — не выполняется
# ревизия: запись 513 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr[1] = 55 — не выполняется
# черновик: arr[0] *= 48 — не выполняется
# архив: запись 537 обработана, изменений нет
# отладка: arr2[8] = 72 — не выполняется
# пометка: запись 169 обработана, изменений нет
# архив: arr[6] += 10 — не выполняется
# пометка: arr[7] *= 57 — не выполняется
# черновик: запись 511 обработана, изменений нет
# пометка: запись 176 обработана, изменений нет
# ревизия: запись 791 обработана, изменений нет
# временная запись: arr2[5] = 44 — не выполняется
# пометка: запись 409 обработана, изменений нет
# черновик: запись 645 обработана, изменений нет
# временная запись: arr[8] *= 28 — не выполняется
# отладка: arr[6] += 78 — не выполняется
# черновик: запись 337 обработана, изменений нет
# отладка: запись 208 обработана, изменений нет
# проверено: запись 904 обработана, изменений нет
# справка: arr[1] *= 54 — не выполняется
# архив: arr2[8] = 87 — не выполняется
# справка: arr[3] = 53 — не выполняется
# замечание: запись 226 обработана, изменений нет
# черновик: arr2[2] = 23 — не выполняется
# отладка: запись 469 обработана, изменений нет
# отладка: arr[7] = 49 — не выполняется
# архив: arr[6] += 4 — не выполняется
# временная запись: запись 784 обработана, изменений нет
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[8] *= 33 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: запись 230 обработана, изменений нет
# временная запись: arr[5] += 18 — не выполняется
# примечание: запись 542 обработана, изменений нет
# архив: arr[6] += 84 — не выполняется
# справка: arr[3] += 2 — не выполняется
# черновик: arr[1] = 38 — не выполняется
# архив: запись 158 обработана, изменений нет
# черновик: arr[2] *= 12 — не выполняется
# проверено: arr[0] = 32 — не выполняется
# черновик: arr[3] += 7 — не выполняется
# проверено: запись 26 обработана, изменений нет
# справка: arr[6] = 28 — не выполняется
# пометка: запись 675 обработана, изменений нет
# примечание: запись 7 обработана, изменений нет
# примечание: запись 631 обработана, изменений нет
# примечание: запись 672 обработана, изменений нет
# отладка: arr[4] += 2 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[1] *= 40 — не выполняется
# справка: запись 871 обработана, изменений нет
# архив: запись 316 обработана, изменений нет
# проверено: arr2[3] = 15 — не выполняется
# замечание: arr2[0] = 54 — не выполняется
# черновик: запись 881 обработана, изменений нет
# примечание: запись 486 обработана, изменений нет
# примечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[9] = 74 — не выполняется
# пометка: запись 150 обработана, изменений нет
# ревизия: arr2[0] = 5 — не выполняется
# справка: arr[2] = 90 — не выполняется
# справка: запись 989 обработана, изменений нет
# временная запись: запись 953 обработана, изменений нет
# проверено: запись 17 обработана, изменений нет
# временная запись: запись 352 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 71 обработана, изменений нет
# проверено: arr[0] *= 65 — не выполняется
# отладка: запись 130 обработана, изменений нет
# ревизия: запись 656 обработана, изменений нет
# архив: arr[9] = 36 — не выполняется
# справка: запись 436 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# справка: запись 249 обработана, изменений нет
# примечание: запись 101 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# временная запись: arr[0] *= 17 — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr2[8] = 60 — не выполняется
# архив: запись 802 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# справка: запись 554 обработана, изменений нет
# временная запись: запись 441 обработана, изменений нет
# справка: arr[8] *= 73 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: запись 98 обработана, изменений нет
# проверено: запись 152 обработана, изменений нет
# черновик: запись 556 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# ревизия: arr2[7] = 43 — не выполняется
# справка: arr[6] += 41 — не выполняется
# пометка: запись 449 обработана, изменений нет
# архив: запись 326 обработана, изменений нет
# временная запись: запись 263 обработана, изменений нет
# архив: arr[3] += 93 — не выполняется
# черновик: запись 110 обработана, изменений нет
# справка: arr[0] = 50 — не выполняется
# черновик: arr2[5] = 43 — не выполняется
# примечание: arr2[0] = 57 — не выполняется
# справка: запись 556 обработана, изменений нет
# пометка: запись 967 обработана, изменений нет
# отладка: arr2[4] = 7 — не выполняется
# отладка: arr[3] = 43 — не выполняется
# временная запись: запись 195 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: запись 602 обработана, изменений нет
# справка: arr[7] *= 53 — не выполняется
# ревизия: запись 949 обработана, изменений нет
# примечание: arr[2] *= 82 — не выполняется
# справка: arr[8] = 11 — не выполняется
# ревизия: arr[2] += 49 — не выполняется
# временная запись: arr2[9] = 69 — не выполняется
# черновик: arr[3] = 66 — не выполняется
# архив: arr2[5] = 15 — не выполняется
# отладка: запись 35 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# замечание: запись 570 обработана, изменений нет
# пометка: запись 417 обработана, изменений нет
# замечание: arr[9] *= 18 — не выполняется
# замечание: arr[3] *= 2 — не выполняется
# пометка: запись 898 обработана, изменений нет
# проверено: запись 114 обработана, изменений нет
# замечание: запись 801 обработана, изменений нет
# ревизия: запись 325 обработана, изменений нет
# пометка: запись 939 обработана, изменений нет
# архив: arr[9] = 82 — не выполняется
# архив: запись 288 обработана, изменений нет
# ревизия: запись 5 обработана, изменений нет
# временная запись: arr[2] = 55 — не выполняется
# замечание: arr2[8] = 95 — не выполняется
# черновик: arr[7] = 68 — не выполняется
# черновик: запись 646 обработана, изменений нет
# временная запись: запись 958 обработана, изменений нет
# черновик: arr2[6] = 93 — не выполняется
# черновик: запись 121 обработана, изменений нет
# замечание: запись 939 обработана, изменений нет
# черновик: запись 419 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# черновик: arr[7] += 39 — не выполняется
# ревизия: запись 469 обработана, изменений нет
# замечание: arr[1] *= 65 — не выполняется
# ревизия: arr[1] += 81 — не выполняется
# замечание: запись 322 обработана, изменений нет
# архив: запись 590 обработана, изменений нет
# архив: запись 895 обработана, изменений нет
# ревизия: запись 45 обработана, изменений нет
# проверено: arr[4] = 70 — не выполняется
# проверено: запись 811 обработана, изменений нет
# справка: запись 492 обработана, изменений нет
# временная запись: запись 236 обработана, изменений нет
# отладка: arr[8] = 64 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[0] = 58 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 98 обработана, изменений нет
# замечание: запись 467 обработана, изменений нет
# черновик: arr[7] = 60 — не выполняется
# архив: arr[0] = 53 — не выполняется
# справка: запись 894 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 849 обработана, изменений нет
# отладка: arr2[4] = 60 — не выполняется
# ревизия: arr2[6] = 34 — не выполняется
# временная запись: arr2[0] = 22 — не выполняется
# ревизия: arr[3] += 75 — не выполняется
# отладка: запись 786 обработана, изменений нет
# черновик: запись 484 обработана, изменений нет
# временная запись: arr[4] = 57 — не выполняется
# проверено: arr2[7] = 40 — не выполняется
# временная запись: запись 779 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# справка: запись 544 обработана, изменений нет
# черновик: запись 19 обработана, изменений нет
# проверено: arr[1] *= 30 — не выполняется
# отладка: запись 277 обработана, изменений нет
# архив: запись 623 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[1] *= 79 — не выполняется
# замечание: arr[7] += 7 — не выполняется
# ревизия: arr[7] = 89 — не выполняется
# ревизия: arr[0] *= 32 — не выполняется
# черновик: arr[9] *= 59 — не выполняется
# архив: arr2[0] = 97 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr2[3] = 99 — не выполняется
# проверено: запись 318 обработана, изменений нет
# замечание: запись 649 обработана, изменений нет
# замечание: arr2[7] = 90 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 803 обработана, изменений нет
# временная запись: arr[2] *= 63 — не выполняется
# пометка: arr[2] += 12 — не выполняется
# архив: arr[4] += 26 — не выполняется
# архив: arr2[1] = 44 — не выполняется
# временная запись: arr[7] *= 18 — не выполняется
# архив: arr[8] = 84 — не выполняется
# черновик: arr[2] = 89 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 921 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# временная запись: запись 113 обработана, изменений нет
# справка: arr2[3] = 94 — не выполняется
# замечание: запись 270 обработана, изменений нет
# ревизия: запись 590 обработана, изменений нет
# черновик: arr[5] *= 98 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[6] = 90 — не выполняется
# черновик: запись 48 обработана, изменений нет
# замечание: arr2[3] = 37 — не выполняется
# замечание: запись 377 обработана, изменений нет
# черновик: arr[8] = 9 — не выполняется
# отладка: запись 367 обработана, изменений нет
# ревизия: arr[6] += 18 — не выполняется
# примечание: запись 529 обработана, изменений нет
# проверено: arr[3] *= 2 — не выполняется
# архив: arr[4] *= 84 — не выполняется
# справка: запись 19 обработана, изменений нет
# отладка: arr2[8] = 67 — не выполняется
# примечание: запись 872 обработана, изменений нет
# отладка: arr[3] = 32 — не выполняется
# примечание: arr[8] *= 43 — не выполняется
# архив: запись 252 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 991 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: arr[3] *= 42 — не выполняется
# черновик: запись 754 обработана, изменений нет
# проверено: запись 629 обработана, изменений нет
# черновик: запись 934 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# ревизия: arr[3] += 64 — не выполняется
# проверено: запись 641 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# проверено: arr2[1] = 53 — не выполняется
# пометка: запись 424 обработана, изменений нет
t58 = str(arr[1]) + str(arr[4])
# ревизия: запись 64 обработана, изменений нет
# пометка: arr[3] *= 25 — не выполняется
# черновик: запись 642 обработана, изменений нет
# отладка: запись 937 обработана, изменений нет
# архив: запись 933 обработана, изменений нет
# ревизия: запись 898 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# проверено: запись 847 обработана, изменений нет
# ревизия: arr[4] += 93 — не выполняется
# пометка: arr[1] += 89 — не выполняется
# архив: запись 633 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# пометка: arr[5] = 27 — не выполняется
# архив: arr[8] += 15 — не выполняется
# архив: arr[1] *= 49 — не выполняется
# архив: arr2[0] = 83 — не выполняется
# временная запись: запись 468 обработана, изменений нет
# примечание: запись 26 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: запись 549 обработана, изменений нет
# архив: запись 150 обработана, изменений нет
# пометка: запись 751 обработана, изменений нет
# замечание: запись 832 обработана, изменений нет
# проверено: запись 345 обработана, изменений нет
# ревизия: arr[3] = 24 — не выполняется
# ревизия: запись 249 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 429 обработана, изменений нет
# черновик: arr[2] *= 68 — не выполняется
# справка: запись 924 обработана, изменений нет
# архив: запись 922 обработана, изменений нет
# временная запись: запись 639 обработана, изменений нет
# отладка: arr[0] = 65 — не выполняется
# примечание: arr2[5] = 46 — не выполняется
# ревизия: arr2[0] = 9 — не выполняется
# справка: arr[5] += 18 — не выполняется
# ревизия: arr2[4] = 62 — не выполняется
# примечание: запись 80 обработана, изменений нет
# архив: запись 897 обработана, изменений нет
# черновик: запись 439 обработана, изменений нет
# пометка: запись 735 обработана, изменений нет
# замечание: arr[9] += 10 — не выполняется
# проверено: запись 725 обработана, изменений нет
# отладка: запись 108 обработана, изменений нет
# временная запись: arr2[6] = 81 — не выполняется
# примечание: запись 863 обработана, изменений нет
# ревизия: запись 556 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[6] += 93 — не выполняется
# примечание: запись 861 обработана, изменений нет
# временная запись: arr2[2] = 27 — не выполняется
# примечание: запись 464 обработана, изменений нет
# замечание: запись 48 обработана, изменений нет
# ревизия: arr[2] *= 62 — не выполняется
# примечание: запись 427 обработана, изменений нет
# примечание: arr2[8] = 51 — не выполняется
# проверено: arr[1] = 82 — не выполняется
# примечание: запись 945 обработана, изменений нет
# справка: arr[2] += 4 — не выполняется
# замечание: запись 648 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# временная запись: запись 462 обработана, изменений нет
# архив: запись 297 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[4] = 83 — не выполняется
# архив: arr[6] *= 95 — не выполняется
# ревизия: запись 889 обработана, изменений нет
# проверено: arr2[1] = 78 — не выполняется
# черновик: arr2[5] = 16 — не выполняется
# ревизия: arr2[1] = 80 — не выполняется
# архив: запись 554 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 486 обработана, изменений нет
# черновик: запись 906 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# примечание: запись 539 обработана, изменений нет
# примечание: arr[1] += 28 — не выполняется
# проверено: arr[8] *= 88 — не выполняется
# проверено: запись 91 обработана, изменений нет
# архив: запись 579 обработана, изменений нет
# замечание: arr[7] = 18 — не выполняется
# примечание: запись 606 обработана, изменений нет
# архив: arr2[2] = 69 — не выполняется
# временная запись: arr[1] *= 71 — не выполняется
# временная запись: запись 135 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr[6] = 65 — не выполняется
# примечание: arr[1] += 45 — не выполняется
# временная запись: arr[9] += 67 — не выполняется
# временная запись: arr[5] = 26 — не выполняется
# замечание: запись 849 обработана, изменений нет
# замечание: запись 960 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# пометка: запись 25 обработана, изменений нет
# пометка: arr[1] = 7 — не выполняется
# справка: arr2[1] = 7 — не выполняется
# архив: arr[4] = 17 — не выполняется
# черновик: arr[1] += 16 — не выполняется
# примечание: arr[1] += 50 — не выполняется
# справка: arr[7] = 40 — не выполняется
# справка: arr[9] *= 1 — не выполняется
# примечание: запись 110 обработана, изменений нет
# справка: запись 783 обработана, изменений нет
# замечание: arr2[7] = 81 — не выполняется
# черновик: запись 141 обработана, изменений нет
# замечание: запись 572 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 156 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# отладка: arr[1] *= 90 — не выполняется
# временная запись: запись 905 обработана, изменений нет
# отладка: arr2[7] = 80 — не выполняется
# ревизия: arr[6] *= 47 — не выполняется
# ревизия: arr[4] += 97 — не выполняется
# примечание: arr[8] += 63 — не выполняется
# проверено: запись 327 обработана, изменений нет
# черновик: arr[6] *= 66 — не выполняется
# замечание: запись 690 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 263 обработана, изменений нет
# ревизия: arr[6] *= 29 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[5] *= 51 — не выполняется
# примечание: запись 888 обработана, изменений нет
# проверено: запись 465 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: запись 743 обработана, изменений нет
# примечание: запись 755 обработана, изменений нет
# черновик: arr2[1] = 90 — не выполняется
# проверено: arr2[7] = 40 — не выполняется
# временная запись: запись 640 обработана, изменений нет
# временная запись: arr[1] *= 57 — не выполняется
# черновик: arr[2] = 57 — не выполняется
# замечание: запись 137 обработана, изменений нет
# пометка: запись 859 обработана, изменений нет
# проверено: arr[9] *= 46 — не выполняется
# архив: запись 352 обработана, изменений нет
# черновик: arr2[9] = 65 — не выполняется
# архив: arr[0] = 83 — не выполняется
# ревизия: запись 201 обработана, изменений нет
# архив: arr[7] = 58 — не выполняется
# черновик: запись 558 обработана, изменений нет
# замечание: arr[7] += 31 — не выполняется
# пометка: запись 761 обработана, изменений нет
# справка: запись 652 обработана, изменений нет
# пометка: запись 914 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# пометка: запись 384 обработана, изменений нет
# примечание: arr2[0] = 31 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# справка: запись 45 обработана, изменений нет
# отладка: запись 369 обработана, изменений нет
# пометка: запись 357 обработана, изменений нет
# пометка: arr2[5] = 16 — не выполняется
# ревизия: arr2[9] = 43 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 118 обработана, изменений нет
# замечание: arr[5] = 50 — не выполняется
# временная запись: запись 315 обработана, изменений нет
# ревизия: arr[3] *= 88 — не выполняется
# примечание: запись 638 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 214 обработана, изменений нет
# черновик: arr[5] = 73 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: arr[7] = 5 — не выполняется
# замечание: arr[5] = 37 — не выполняется
# архив: запись 853 обработана, изменений нет
# замечание: запись 610 обработана, изменений нет
# черновик: запись 604 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: arr2[0] = 2 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr[5] += 46 — не выполняется
# примечание: запись 400 обработана, изменений нет
# ревизия: запись 912 обработана, изменений нет
# справка: запись 675 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# временная запись: arr2[0] = 53 — не выполняется
# ревизия: arr[0] *= 46 — не выполняется
# пометка: запись 333 обработана, изменений нет
# отладка: запись 13 обработана, изменений нет
# замечание: запись 151 обработана, изменений нет
# временная запись: arr[2] *= 10 — не выполняется
# замечание: запись 229 обработана, изменений нет
# замечание: arr[1] += 46 — не выполняется
# замечание: arr[1] = 71 — не выполняется
# временная запись: arr2[2] = 66 — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 73 обработана, изменений нет
# отладка: запись 352 обработана, изменений нет
# справка: запись 664 обработана, изменений нет
# замечание: запись 345 обработана, изменений нет
# примечание: запись 31 обработана, изменений нет
# временная запись: запись 340 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 359 обработана, изменений нет
# ревизия: запись 410 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# проверено: запись 220 обработана, изменений нет
# пометка: arr2[0] = 50 — не выполняется
# справка: arr[8] *= 83 — не выполняется
# проверено: arr[3] = 42 — не выполняется
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr2[7] = 91 — не выполняется
# черновик: запись 971 обработана, изменений нет
# черновик: запись 619 обработана, изменений нет
# временная запись: arr[5] *= 69 — не выполняется
# временная запись: arr2[6] = 36 — не выполняется
# архив: arr[2] += 31 — не выполняется
# проверено: arr2[0] = 11 — не выполняется
# справка: запись 86 обработана, изменений нет
# архив: arr[6] += 13 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[2] *= 10 — не выполняется
# замечание: запись 946 обработана, изменений нет
# замечание: запись 638 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr2[1] = 31 — не выполняется
# отладка: запись 104 обработана, изменений нет
# временная запись: arr[2] *= 80 — не выполняется
# архив: запись 854 обработана, изменений нет
# черновик: arr[7] += 58 — не выполняется
# проверено: arr[5] = 11 — не выполняется
# архив: запись 326 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# отладка: запись 264 обработана, изменений нет
# отладка: arr2[6] = 48 — не выполняется
# пометка: arr[0] = 80 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 498 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# архив: запись 718 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 956 обработана, изменений нет
# пометка: arr[2] *= 91 — не выполняется
# справка: arr2[2] = 61 — не выполняется
# отладка: запись 12 обработана, изменений нет
# проверено: arr[2] = 31 — не выполняется
# замечание: запись 867 обработана, изменений нет
# проверено: запись 820 обработана, изменений нет
# замечание: arr[9] += 16 — не выполняется
# пометка: запись 525 обработана, изменений нет
# временная запись: arr[8] *= 65 — не выполняется
# ревизия: arr[5] *= 24 — не выполняется
# отладка: arr[4] += 64 — не выполняется
# отладка: arr[0] += 69 — не выполняется
# черновик: запись 233 обработана, изменений нет
# примечание: запись 968 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 705 обработана, изменений нет
# отладка: запись 714 обработана, изменений нет
# временная запись: запись 699 обработана, изменений нет
# временная запись: запись 7 обработана, изменений нет
# пометка: запись 505 обработана, изменений нет
# замечание: arr2[6] = 48 — не выполняется
# замечание: arr[8] *= 50 — не выполняется
# архив: arr[9] += 1 — не выполняется
# временная запись: запись 353 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 125 обработана, изменений нет
# черновик: запись 960 обработана, изменений нет
# пометка: запись 496 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr2[5] = 77 — не выполняется
# справка: arr[1] *= 93 — не выполняется
# архив: arr2[5] = 14 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 573 обработана, изменений нет
# проверено: arr[4] *= 56 — не выполняется
# временная запись: arr2[2] = 50 — не выполняется
# замечание: arr[0] = 82 — не выполняется
# временная запись: запись 868 обработана, изменений нет
# справка: arr[4] += 26 — не выполняется
# пометка: arr[7] += 78 — не выполняется
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
arr[0] = int(t58) % 97
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[6] += 30 — не выполняется
# ревизия: arr[5] *= 97 — не выполняется
# замечание: arr2[6] = 16 — не выполняется
# временная запись: запись 35 обработана, изменений нет
# черновик: arr2[4] = 21 — не выполняется
# пометка: запись 428 обработана, изменений нет
# пометка: arr[6] *= 49 — не выполняется
# черновик: запись 956 обработана, изменений нет
# примечание: запись 882 обработана, изменений нет
# справка: arr[7] = 21 — не выполняется
# замечание: запись 694 обработана, изменений нет
# черновик: arr[4] += 31 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 81 обработана, изменений нет
# замечание: arr[7] += 93 — не выполняется
# черновик: запись 264 обработана, изменений нет
# ревизия: arr[6] = 90 — не выполняется
# справка: arr[6] = 7 — не выполняется
# черновик: запись 832 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# архив: запись 134 обработана, изменений нет
# черновик: arr2[4] = 50 — не выполняется
# справка: запись 630 обработана, изменений нет
# примечание: arr[3] = 45 — не выполняется
# справка: запись 460 обработана, изменений нет
# пометка: запись 987 обработана, изменений нет
# черновик: arr[8] *= 15 — не выполняется
# ревизия: запись 514 обработана, изменений нет
# временная запись: arr2[4] = 48 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 695 обработана, изменений нет
# ревизия: arr[3] += 81 — не выполняется
# отладка: запись 25 обработана, изменений нет
# справка: arr2[5] = 67 — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[6] += 4 — не выполняется
# временная запись: arr[4] *= 39 — не выполняется
# черновик: запись 832 обработана, изменений нет
# отладка: запись 40 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 424 обработана, изменений нет
# проверено: arr2[8] = 37 — не выполняется
# отладка: запись 810 обработана, изменений нет
# примечание: запись 563 обработана, изменений нет
# замечание: arr[9] *= 83 — не выполняется
# черновик: запись 611 обработана, изменений нет
# ревизия: arr[5] += 15 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[9] += 5 — не выполняется
# черновик: запись 917 обработана, изменений нет
# примечание: arr[1] += 8 — не выполняется
# пометка: запись 564 обработана, изменений нет
# проверено: arr2[1] = 45 — не выполняется
# временная запись: arr[5] += 74 — не выполняется
# справка: arr[8] = 93 — не выполняется
# пометка: запись 706 обработана, изменений нет
# проверено: arr[8] *= 49 — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 582 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 84 обработана, изменений нет
# справка: arr[0] *= 68 — не выполняется
# пометка: arr[0] = 13 — не выполняется
# проверено: arr2[2] = 92 — не выполняется
# проверено: запись 394 обработана, изменений нет
# черновик: запись 888 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# отладка: arr[4] *= 23 — не выполняется
# временная запись: запись 409 обработана, изменений нет
# ревизия: arr[5] *= 33 — не выполняется
# пометка: запись 440 обработана, изменений нет
# справка: запись 904 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[9] = 26 — не выполняется
# пометка: запись 529 обработана, изменений нет
# примечание: arr[0] += 57 — не выполняется
# архив: запись 128 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[5] = 27 — не выполняется
# проверено: запись 109 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# справка: запись 209 обработана, изменений нет
# отладка: arr[1] *= 46 — не выполняется
# временная запись: arr[9] += 9 — не выполняется
# примечание: arr[5] *= 47 — не выполняется
# отладка: запись 905 обработана, изменений нет
# черновик: arr2[1] = 4 — не выполняется
# ревизия: arr[7] = 78 — не выполняется
# черновик: arr[3] *= 35 — не выполняется
# пометка: arr[1] += 11 — не выполняется
# временная запись: запись 657 обработана, изменений нет
# временная запись: arr[8] += 47 — не выполняется
# ревизия: запись 903 обработана, изменений нет
# проверено: arr[1] *= 60 — не выполняется
# ревизия: arr[3] += 83 — не выполняется
# отладка: запись 200 обработана, изменений нет
# пометка: arr2[9] = 75 — не выполняется
# отладка: запись 609 обработана, изменений нет
# справка: arr[2] *= 31 — не выполняется
# замечание: arr[0] = 22 — не выполняется
# отладка: запись 954 обработана, изменений нет
# ревизия: запись 490 обработана, изменений нет
# проверено: arr[6] += 10 — не выполняется
# проверено: запись 942 обработана, изменений нет
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 658 обработана, изменений нет
# временная запись: arr[6] += 97 — не выполняется
# замечание: запись 462 обработана, изменений нет
# временная запись: запись 636 обработана, изменений нет
# отладка: запись 501 обработана, изменений нет
# архив: arr[7] = 33 — не выполняется
# примечание: arr[6] *= 95 — не выполняется
# отладка: запись 740 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# отладка: запись 19 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 147 обработана, изменений нет
# справка: запись 533 обработана, изменений нет
# черновик: arr[7] = 3 — не выполняется
# замечание: arr[1] *= 46 — не выполняется
# проверено: arr[3] = 56 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: arr[9] = 2 — не выполняется
# примечание: запись 285 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 346 обработана, изменений нет
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 184 обработана, изменений нет
# замечание: arr[5] += 97 — не выполняется
# архив: arr2[8] = 27 — не выполняется
# временная запись: arr[8] += 98 — не выполняется
# проверено: arr2[9] = 45 — не выполняется
# справка: запись 541 обработана, изменений нет
# отладка: arr[4] += 55 — не выполняется
# пометка: запись 427 обработана, изменений нет
# справка: arr[2] += 76 — не выполняется
# пометка: arr2[4] = 88 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 353 обработана, изменений нет
# замечание: arr2[2] = 41 — не выполняется
# отладка: arr[5] += 42 — не выполняется
# пометка: arr2[8] = 81 — не выполняется
# пометка: arr2[0] = 59 — не выполняется
# временная запись: arr[7] += 13 — не выполняется
# временная запись: запись 817 обработана, изменений нет
# черновик: arr2[9] = 54 — не выполняется
# отладка: запись 954 обработана, изменений нет
# примечание: arr[6] = 37 — не выполняется
# справка: запись 589 обработана, изменений нет
# черновик: arr[4] = 4 — не выполняется
# отладка: запись 715 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# отладка: запись 594 обработана, изменений нет
# примечание: arr[9] *= 22 — не выполняется
# замечание: запись 487 обработана, изменений нет
# черновик: запись 527 обработана, изменений нет
# примечание: запись 268 обработана, изменений нет
# пометка: arr[5] += 36 — не выполняется
# примечание: arr2[5] = 86 — не выполняется
# проверено: arr[4] *= 25 — не выполняется
# проверено: запись 17 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# отладка: запись 371 обработана, изменений нет
# ревизия: arr[0] = 77 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 830 обработана, изменений нет
# примечание: arr2[3] = 58 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 908 обработана, изменений нет
# пометка: arr[4] += 51 — не выполняется
# архив: arr[3] = 76 — не выполняется
# справка: arr[5] += 91 — не выполняется
# ревизия: arr[0] = 84 — не выполняется
# черновик: arr[5] *= 94 — не выполняется
# проверено: запись 634 обработана, изменений нет
# архив: arr[9] *= 81 — не выполняется
# справка: запись 984 обработана, изменений нет
# черновик: запись 243 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# отладка: запись 412 обработана, изменений нет
# черновик: запись 17 обработана, изменений нет
# замечание: arr[5] = 70 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 135 обработана, изменений нет
# отладка: запись 376 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr[3] *= 1 — не выполняется
# проверено: arr2[6] = 66 — не выполняется
# черновик: arr[2] += 85 — не выполняется
# отладка: arr[2] = 99 — не выполняется
# справка: arr[2] *= 86 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: запись 181 обработана, изменений нет
# временная запись: запись 830 обработана, изменений нет
# черновик: запись 827 обработана, изменений нет
# проверено: arr[3] *= 80 — не выполняется
# черновик: запись 268 обработана, изменений нет
# отладка: arr[5] = 98 — не выполняется
# проверено: arr[1] *= 31 — не выполняется
# проверено: запись 188 обработана, изменений нет
# архив: запись 936 обработана, изменений нет
# черновик: запись 489 обработана, изменений нет
# черновик: arr[1] = 48 — не выполняется
# черновик: запись 936 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[6] = 71 — не выполняется
# пометка: arr[9] += 12 — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr[6] += 48 — не выполняется
# ревизия: arr[9] *= 89 — не выполняется
# ревизия: запись 519 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# примечание: arr[6] += 29 — не выполняется
# замечание: arr[6] += 83 — не выполняется
# архив: arr[5] *= 30 — не выполняется
# справка: arr[8] *= 35 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 470 обработана, изменений нет
# замечание: arr[3] += 6 — не выполняется
# справка: arr2[7] = 30 — не выполняется
# справка: запись 981 обработана, изменений нет
# примечание: arr[9] += 16 — не выполняется
# пометка: arr[9] += 81 — не выполняется
# архив: запись 456 обработана, изменений нет
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[1] = 73 — не выполняется
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 148 обработана, изменений нет
# архив: arr[0] *= 28 — не выполняется
# проверено: запись 184 обработана, изменений нет
# архив: arr[9] += 94 — не выполняется
# проверено: запись 699 обработана, изменений нет
# отладка: запись 958 обработана, изменений нет
# замечание: arr[3] *= 34 — не выполняется
# справка: запись 844 обработана, изменений нет
# архив: запись 25 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# временная запись: запись 137 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# замечание: запись 982 обработана, изменений нет
# пометка: запись 783 обработана, изменений нет
# проверено: запись 559 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# ревизия: запись 616 обработана, изменений нет
# справка: arr[1] += 68 — не выполняется
# проверено: arr[8] += 31 — не выполняется
# черновик: запись 545 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# отладка: arr[5] = 92 — не выполняется
# ревизия: arr[2] *= 74 — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 2 обработана, изменений нет
# отладка: запись 787 обработана, изменений нет
# проверено: запись 859 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 820 обработана, изменений нет
# справка: arr[9] += 12 — не выполняется
# временная запись: запись 137 обработана, изменений нет
# справка: arr2[8] = 33 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 375 обработана, изменений нет
# черновик: arr2[5] = 16 — не выполняется
# справка: запись 542 обработана, изменений нет
# черновик: запись 284 обработана, изменений нет
# ревизия: запись 990 обработана, изменений нет
# архив: запись 182 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 32 обработана, изменений нет
# справка: arr[9] = 59 — не выполняется
# черновик: запись 185 обработана, изменений нет
# архив: запись 654 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# справка: запись 826 обработана, изменений нет
arr[8] += 1
# пометка: запись 822 обработана, изменений нет
# черновик: arr[0] += 48 — не выполняется
# отладка: запись 910 обработана, изменений нет
# проверено: запись 284 обработана, изменений нет
# справка: запись 631 обработана, изменений нет
# архив: arr[2] = 49 — не выполняется
# примечание: запись 502 обработана, изменений нет
# примечание: запись 231 обработана, изменений нет
# примечание: arr[5] += 37 — не выполняется
# примечание: arr[2] *= 80 — не выполняется
# справка: запись 949 обработана, изменений нет
# черновик: arr[5] += 26 — не выполняется
# пометка: запись 927 обработана, изменений нет
# отладка: запись 623 обработана, изменений нет
# черновик: arr[9] *= 53 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 568 обработана, изменений нет
# ревизия: arr[8] += 97 — не выполняется
# примечание: запись 811 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 222 обработана, изменений нет
# пометка: arr[7] += 72 — не выполняется
# ревизия: arr[2] += 88 — не выполняется
# архив: запись 450 обработана, изменений нет
# справка: arr2[0] = 57 — не выполняется
# проверено: arr[7] *= 41 — не выполняется
# примечание: arr[8] += 16 — не выполняется
# замечание: arr[8] *= 90 — не выполняется
# временная запись: arr[5] = 43 — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 704 обработана, изменений нет
# пометка: запись 847 обработана, изменений нет
# замечание: arr[0] = 33 — не выполняется
# справка: arr[2] *= 31 — не выполняется
# временная запись: arr[1] = 16 — не выполняется
# ревизия: arr[0] = 28 — не выполняется
# черновик: запись 405 обработана, изменений нет
# архив: запись 768 обработана, изменений нет
# примечание: arr2[0] = 73 — не выполняется
# временная запись: запись 540 обработана, изменений нет
# ревизия: запись 767 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 154 обработана, изменений нет
# ревизия: запись 768 обработана, изменений нет
# черновик: arr[6] *= 49 — не выполняется
# ревизия: arr[3] += 66 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: запись 223 обработана, изменений нет
# черновик: запись 941 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 740 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 433 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# архив: запись 481 обработана, изменений нет
# примечание: запись 591 обработана, изменений нет
# черновик: запись 328 обработана, изменений нет
# временная запись: запись 801 обработана, изменений нет
# черновик: arr[1] *= 43 — не выполняется
# замечание: запись 809 обработана, изменений нет
# ревизия: arr[6] *= 51 — не выполняется
# архив: arr2[3] = 79 — не выполняется
# отладка: arr2[7] = 83 — не выполняется
# справка: запись 348 обработана, изменений нет
# проверено: запись 368 обработана, изменений нет
# временная запись: запись 75 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[7] += 48 — не выполняется
# справка: arr[6] *= 72 — не выполняется
# временная запись: arr[2] += 6 — не выполняется
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 799 обработана, изменений нет
# проверено: arr[2] += 1 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr2[6] = 57 — не выполняется
# примечание: запись 93 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 19 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# проверено: arr2[7] = 82 — не выполняется
# проверено: запись 271 обработана, изменений нет
# временная запись: запись 13 обработана, изменений нет
# проверено: arr[1] *= 44 — не выполняется
# временная запись: запись 936 обработана, изменений нет
# отладка: запись 790 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# пометка: arr2[0] = 79 — не выполняется
# черновик: запись 313 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: запись 221 обработана, изменений нет
# ревизия: arr[2] += 71 — не выполняется
# временная запись: запись 410 обработана, изменений нет
# пометка: запись 971 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 119 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# временная запись: запись 64 обработана, изменений нет
# пометка: запись 243 обработана, изменений нет
# ревизия: запись 423 обработана, изменений нет
# пометка: arr[7] *= 32 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[6] = 9 — не выполняется
# архив: запись 315 обработана, изменений нет
# проверено: запись 457 обработана, изменений нет
# отладка: запись 871 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: запись 210 обработана, изменений нет
# замечание: запись 379 обработана, изменений нет
# временная запись: запись 519 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# пометка: arr[7] += 79 — не выполняется
# временная запись: arr[0] = 29 — не выполняется
# замечание: запись 848 обработана, изменений нет
# временная запись: arr[8] *= 96 — не выполняется
# архив: запись 532 обработана, изменений нет
# черновик: arr[3] *= 72 — не выполняется
# временная запись: arr2[4] = 29 — не выполняется
# пометка: arr[5] *= 3 — не выполняется
# отладка: arr[8] *= 55 — не выполняется
# проверено: запись 701 обработана, изменений нет
# примечание: arr[5] += 51 — не выполняется
# временная запись: запись 669 обработана, изменений нет
# примечание: arr[0] = 52 — не выполняется
# пометка: arr[4] = 97 — не выполняется
# примечание: arr[1] = 74 — не выполняется
# пометка: arr2[0] = 41 — не выполняется
# пометка: запись 796 обработана, изменений нет
# отладка: arr[8] *= 28 — не выполняется
# замечание: запись 761 обработана, изменений нет
# проверено: arr2[6] = 31 — не выполняется
# временная запись: arr2[8] = 20 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# справка: запись 430 обработана, изменений нет
# примечание: запись 851 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# справка: arr[1] *= 66 — не выполняется
# архив: arr[8] += 59 — не выполняется
# пометка: arr2[1] = 33 — не выполняется
# замечание: arr[1] += 24 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: arr2[2] = 97 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 813 обработана, изменений нет
# справка: запись 588 обработана, изменений нет
# ревизия: arr[8] *= 49 — не выполняется
# черновик: arr[7] *= 45 — не выполняется
# пометка: запись 23 обработана, изменений нет
# ревизия: запись 512 обработана, изменений нет
# ревизия: arr[1] = 76 — не выполняется
# замечание: запись 589 обработана, изменений нет
# архив: arr[1] *= 41 — не выполняется
# временная запись: arr[7] = 7 — не выполняется
# черновик: запись 422 обработана, изменений нет
# архив: arr2[9] = 17 — не выполняется
# справка: запись 947 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 718 обработана, изменений нет
# черновик: arr[9] = 48 — не выполняется
# отладка: arr2[6] = 48 — не выполняется
# проверено: запись 546 обработана, изменений нет
# ревизия: запись 992 обработана, изменений нет
# отладка: запись 484 обработана, изменений нет
# пометка: arr[6] += 55 — не выполняется
# замечание: запись 68 обработана, изменений нет
# пометка: запись 184 обработана, изменений нет
# примечание: запись 847 обработана, изменений нет
# ревизия: запись 689 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# ревизия: arr[8] = 39 — не выполняется
# черновик: запись 210 обработана, изменений нет
# черновик: arr2[6] = 3 — не выполняется
# справка: arr2[8] = 20 — не выполняется
# справка: запись 638 обработана, изменений нет
# справка: arr2[4] = 53 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 295 обработана, изменений нет
# проверено: запись 549 обработана, изменений нет
# справка: arr[8] += 53 — не выполняется
# пометка: запись 845 обработана, изменений нет
# ревизия: arr2[2] = 66 — не выполняется
# временная запись: arr2[5] = 89 — не выполняется
# архив: arr2[8] = 29 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 120 обработана, изменений нет
# временная запись: запись 129 обработана, изменений нет
# пометка: arr2[5] = 79 — не выполняется
# справка: arr[8] *= 27 — не выполняется
# пометка: запись 873 обработана, изменений нет
# ревизия: arr2[8] = 38 — не выполняется
# справка: запись 295 обработана, изменений нет
# проверено: запись 893 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# примечание: arr[3] += 17 — не выполняется
# замечание: запись 398 обработана, изменений нет
# черновик: arr[8] = 64 — не выполняется
# пометка: arr[7] += 15 — не выполняется
# ревизия: запись 974 обработана, изменений нет
# черновик: arr[5] *= 62 — не выполняется
# черновик: запись 21 обработана, изменений нет
# проверено: запись 415 обработана, изменений нет
# пометка: arr2[6] = 31 — не выполняется
# пометка: arr2[3] = 6 — не выполняется
# временная запись: запись 706 обработана, изменений нет
# временная запись: arr[5] *= 72 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: arr[6] *= 86 — не выполняется
# временная запись: запись 76 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 454 обработана, изменений нет
# архив: запись 913 обработана, изменений нет
# временная запись: запись 10 обработана, изменений нет
# замечание: arr[8] *= 13 — не выполняется
# справка: arr[6] *= 54 — не выполняется
# архив: arr[9] += 81 — не выполняется
# пометка: arr[8] *= 42 — не выполняется
# проверено: arr2[6] = 77 — не выполняется
# черновик: запись 751 обработана, изменений нет
# архив: запись 642 обработана, изменений нет
# замечание: запись 726 обработана, изменений нет
# временная запись: arr[8] = 42 — не выполняется
# ревизия: запись 822 обработана, изменений нет
# временная запись: запись 403 обработана, изменений нет
# замечание: запись 160 обработана, изменений нет
# замечание: запись 780 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# временная запись: arr2[8] = 95 — не выполняется
# черновик: arr[6] *= 16 — не выполняется
# ревизия: arr[7] += 22 — не выполняется
# временная запись: запись 512 обработана, изменений нет
# замечание: запись 282 обработана, изменений нет
# справка: arr[2] = 8 — не выполняется
# ревизия: arr[9] = 75 — не выполняется
# архив: запись 906 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[7] = 14 — не выполняется
# примечание: запись 885 обработана, изменений нет
# отладка: arr[8] *= 77 — не выполняется
# пометка: arr[0] *= 43 — не выполняется
# ревизия: arr[6] += 28 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: запись 675 обработана, изменений нет
# отладка: запись 804 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# архив: arr[7] = 23 — не выполняется
# проверено: arr2[4] = 83 — не выполняется
# отладка: arr[3] = 18 — не выполняется
# временная запись: arr2[1] = 90 — не выполняется
# черновик: arr2[1] = 57 — не выполняется
# архив: запись 572 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# черновик: arr2[5] = 72 — не выполняется
# ревизия: запись 379 обработана, изменений нет
# замечание: запись 520 обработана, изменений нет
# проверено: arr2[0] = 38 — не выполняется
# ревизия: запись 418 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# архив: arr[7] *= 14 — не выполняется
# пометка: arr[0] = 59 — не выполняется
# архив: запись 226 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr[5] *= 1 — не выполняется
# примечание: запись 449 обработана, изменений нет
# временная запись: arr[0] += 26 — не выполняется
# временная запись: запись 591 обработана, изменений нет
# справка: arr[4] += 43 — не выполняется
# справка: arr[9] = 74 — не выполняется
# черновик: запись 962 обработана, изменений нет
# замечание: arr[8] += 49 — не выполняется
# примечание: arr[7] = 94 — не выполняется
# черновик: arr2[3] = 24 — не выполняется
# замечание: запись 686 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: arr[5] = 84 — не выполняется
# отладка: arr[0] *= 97 — не выполняется
# временная запись: запись 604 обработана, изменений нет
# пометка: arr[6] += 23 — не выполняется
bump_all(arr, 5)
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: запись 973 обработана, изменений нет
# ревизия: запись 457 обработана, изменений нет
# пометка: arr[6] += 98 — не выполняется
# отладка: запись 848 обработана, изменений нет
# ревизия: запись 80 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# архив: arr[6] += 87 — не выполняется
# архив: запись 690 обработана, изменений нет
# замечание: arr2[2] = 68 — не выполняется
# архив: запись 738 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# пометка: arr[2] += 92 — не выполняется
# замечание: запись 603 обработана, изменений нет
# архив: arr2[4] = 75 — не выполняется
# примечание: запись 267 обработана, изменений нет
# ревизия: запись 742 обработана, изменений нет
# архив: запись 641 обработана, изменений нет
# черновик: arr2[2] = 26 — не выполняется
# отладка: запись 938 обработана, изменений нет
# справка: запись 659 обработана, изменений нет
# примечание: запись 634 обработана, изменений нет
# замечание: запись 479 обработана, изменений нет
# справка: запись 258 обработана, изменений нет
# справка: запись 791 обработана, изменений нет
# проверено: запись 26 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# отладка: запись 236 обработана, изменений нет
# ревизия: arr[8] = 30 — не выполняется
# замечание: запись 544 обработана, изменений нет
# отладка: запись 273 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[2] *= 77 — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr[9] += 16 — не выполняется
# справка: arr[3] = 19 — не выполняется
# пометка: запись 692 обработана, изменений нет
# примечание: arr[3] *= 65 — не выполняется
# замечание: запись 442 обработана, изменений нет
# черновик: arr[3] += 98 — не выполняется
# ревизия: запись 977 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# справка: arr[1] *= 8 — не выполняется
# ревизия: запись 191 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# примечание: запись 908 обработана, изменений нет
# архив: запись 417 обработана, изменений нет
# проверено: запись 722 обработана, изменений нет
# проверено: запись 922 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# черновик: arr[3] += 86 — не выполняется
# архив: запись 165 обработана, изменений нет
# справка: запись 888 обработана, изменений нет
# справка: запись 41 обработана, изменений нет
# архив: запись 624 обработана, изменений нет
# ревизия: arr[1] *= 24 — не выполняется
# черновик: arr[5] = 41 — не выполняется
# архив: запись 510 обработана, изменений нет
# пометка: arr[3] *= 27 — не выполняется
# ревизия: arr[0] = 56 — не выполняется
# справка: запись 427 обработана, изменений нет
# примечание: arr[6] = 1 — не выполняется
# замечание: arr[1] = 46 — не выполняется
# ревизия: arr[6] *= 1 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[6] += 74 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 787 обработана, изменений нет
# замечание: запись 80 обработана, изменений нет
# примечание: arr2[0] = 4 — не выполняется
# черновик: arr[6] = 97 — не выполняется
# ревизия: запись 50 обработана, изменений нет
# ревизия: arr[5] += 25 — не выполняется
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 246 обработана, изменений нет
# примечание: запись 332 обработана, изменений нет
# проверено: arr2[7] = 52 — не выполняется
# архив: arr[0] *= 86 — не выполняется
# пометка: запись 175 обработана, изменений нет
# замечание: запись 92 обработана, изменений нет
# проверено: arr[9] += 92 — не выполняется
# справка: arr2[9] = 97 — не выполняется
# проверено: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 610 обработана, изменений нет
# примечание: arr2[4] = 51 — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 278 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: arr[6] = 19 — не выполняется
# ревизия: arr[6] = 6 — не выполняется
# черновик: запись 389 обработана, изменений нет
# пометка: запись 278 обработана, изменений нет
# ревизия: arr[6] *= 42 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 249 обработана, изменений нет
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[9] *= 67 — не выполняется
# проверено: запись 801 обработана, изменений нет
# пометка: arr2[6] = 51 — не выполняется
# черновик: запись 315 обработана, изменений нет
# пометка: arr[7] *= 96 — не выполняется
# черновик: запись 71 обработана, изменений нет
# ревизия: запись 769 обработана, изменений нет
# справка: запись 187 обработана, изменений нет
# временная запись: arr[3] = 91 — не выполняется
# архив: arr2[2] = 48 — не выполняется
# замечание: запись 801 обработана, изменений нет
# проверено: arr[2] *= 66 — не выполняется
# архив: arr2[4] = 33 — не выполняется
# отладка: запись 752 обработана, изменений нет
# справка: arr[8] += 76 — не выполняется
# архив: запись 434 обработана, изменений нет
# примечание: arr2[2] = 36 — не выполняется
# справка: arr2[6] = 4 — не выполняется
# архив: запись 292 обработана, изменений нет
# справка: arr2[6] = 24 — не выполняется
# пометка: запись 358 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# проверено: запись 237 обработана, изменений нет
# черновик: arr[0] += 76 — не выполняется
# ревизия: запись 223 обработана, изменений нет
# пометка: arr[8] = 62 — не выполняется
# временная запись: arr[7] = 84 — не выполняется
# черновик: arr[2] = 58 — не выполняется
# отладка: arr[5] += 13 — не выполняется
# проверено: arr[4] *= 97 — не выполняется
# пометка: arr[3] += 63 — не выполняется
# временная запись: запись 986 обработана, изменений нет
# ревизия: arr2[5] = 15 — не выполняется
# пометка: arr[7] += 87 — не выполняется
# проверено: запись 61 обработана, изменений нет
# временная запись: запись 463 обработана, изменений нет
# пометка: запись 115 обработана, изменений нет
# отладка: запись 834 обработана, изменений нет
# отладка: запись 956 обработана, изменений нет
# справка: arr[2] = 8 — не выполняется
# отладка: arr[9] += 17 — не выполняется
# черновик: запись 166 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# проверено: запись 784 обработана, изменений нет
# черновик: запись 346 обработана, изменений нет
# примечание: arr[6] *= 33 — не выполняется
# архив: запись 292 обработана, изменений нет
# справка: arr2[9] = 68 — не выполняется
# справка: arr[5] += 91 — не выполняется
# ревизия: arr[6] += 99 — не выполняется
# примечание: запись 39 обработана, изменений нет
# проверено: arr[6] *= 40 — не выполняется
# примечание: запись 914 обработана, изменений нет
# справка: arr[1] += 72 — не выполняется
# архив: запись 103 обработана, изменений нет
# проверено: arr[2] *= 26 — не выполняется
# примечание: arr2[4] = 8 — не выполняется
# черновик: запись 488 обработана, изменений нет
# архив: запись 664 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr[4] += 76 — не выполняется
# временная запись: запись 272 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# ревизия: запись 748 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# временная запись: arr[8] *= 19 — не выполняется
# временная запись: arr[3] *= 37 — не выполняется
# отладка: запись 42 обработана, изменений нет
# отладка: запись 72 обработана, изменений нет
# временная запись: запись 953 обработана, изменений нет
# проверено: запись 155 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# пометка: arr[8] += 38 — не выполняется
# примечание: запись 770 обработана, изменений нет
# временная запись: запись 976 обработана, изменений нет
# замечание: запись 349 обработана, изменений нет
# примечание: запись 68 обработана, изменений нет
# временная запись: arr[5] += 55 — не выполняется
# черновик: arr[4] *= 40 — не выполняется
# отладка: запись 814 обработана, изменений нет
# временная запись: запись 97 обработана, изменений нет
# черновик: запись 471 обработана, изменений нет
# примечание: запись 158 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[5] *= 27 — не выполняется
# справка: запись 467 обработана, изменений нет
# архив: arr[4] *= 88 — не выполняется
# пометка: запись 362 обработана, изменений нет
# архив: запись 458 обработана, изменений нет
# архив: запись 79 обработана, изменений нет
# отладка: arr[5] = 20 — не выполняется
# замечание: запись 489 обработана, изменений нет
# архив: arr[2] += 54 — не выполняется
# архив: arr[3] = 17 — не выполняется
# отладка: запись 456 обработана, изменений нет
# временная запись: arr[9] *= 61 — не выполняется
# справка: запись 221 обработана, изменений нет
# замечание: запись 863 обработана, изменений нет
# ревизия: запись 319 обработана, изменений нет
# замечание: arr[0] = 5 — не выполняется
# справка: запись 431 обработана, изменений нет
# пометка: запись 793 обработана, изменений нет
# архив: запись 864 обработана, изменений нет
# замечание: arr2[2] = 29 — не выполняется
# временная запись: запись 51 обработана, изменений нет
# ревизия: запись 780 обработана, изменений нет
# ревизия: запись 694 обработана, изменений нет
# замечание: arr[7] *= 18 — не выполняется
# замечание: arr[7] *= 72 — не выполняется
# примечание: arr2[9] = 74 — не выполняется
# проверено: запись 935 обработана, изменений нет
# замечание: arr2[1] = 84 — не выполняется
# черновик: arr[6] *= 1 — не выполняется
# примечание: запись 706 обработана, изменений нет
# пометка: arr[4] = 56 — не выполняется
# отладка: arr[8] = 14 — не выполняется
# отладка: arr[3] += 70 — не выполняется
# отладка: запись 542 обработана, изменений нет
# ревизия: запись 595 обработана, изменений нет
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 758 обработана, изменений нет
# архив: arr2[5] = 14 — не выполняется
# архив: запись 217 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# замечание: запись 450 обработана, изменений нет
# примечание: arr[1] += 85 — не выполняется
# временная запись: arr[5] += 45 — не выполняется
# проверено: arr2[9] = 52 — не выполняется
# примечание: arr[3] *= 31 — не выполняется
# черновик: запись 658 обработана, изменений нет
# черновик: запись 786 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 611 обработана, изменений нет
# пометка: запись 799 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 523 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# пометка: arr[5] *= 54 — не выполняется
# временная запись: запись 214 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# пометка: arr2[1] = 22 — не выполняется
# черновик: запись 996 обработана, изменений нет
# справка: запись 591 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr[7] += 11 — не выполняется
# отладка: arr[8] = 46 — не выполняется
# справка: arr[1] *= 73 — не выполняется
# пометка: arr[1] = 38 — не выполняется
# архив: arr[9] *= 70 — не выполняется
# отладка: запись 198 обработана, изменений нет
# архив: запись 214 обработана, изменений нет
# справка: arr2[2] = 59 — не выполняется
# пометка: arr[4] = 35 — не выполняется
# примечание: запись 521 обработана, изменений нет
# ревизия: запись 953 обработана, изменений нет
# замечание: запись 431 обработана, изменений нет
# примечание: запись 265 обработана, изменений нет
# примечание: arr[5] = 18 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: запись 272 обработана, изменений нет
# черновик: arr[1] = 99 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr[0] += 68 — не выполняется
# замечание: arr[2] += 25 — не выполняется
# проверено: запись 41 обработана, изменений нет
# проверено: arr[5] *= 20 — не выполняется
# справка: запись 499 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# замечание: запись 367 обработана, изменений нет
# справка: arr[8] += 92 — не выполняется
# замечание: запись 38 обработана, изменений нет
# примечание: arr[0] *= 42 — не выполняется
# пометка: запись 99 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# проверено: запись 726 обработана, изменений нет
# ревизия: запись 208 обработана, изменений нет
# пометка: arr2[0] = 7 — не выполняется
# ревизия: arr[0] += 38 — не выполняется
# пометка: запись 190 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 303 обработана, изменений нет
# справка: arr[4] *= 47 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 483 обработана, изменений нет
arr[2] *= 2
# ревизия: запись 172 обработана, изменений нет
# пометка: arr2[0] = 14 — не выполняется
# архив: arr[1] *= 10 — не выполняется
# отладка: arr[5] = 19 — не выполняется
# замечание: запись 839 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# справка: arr[7] += 26 — не выполняется
# архив: запись 908 обработана, изменений нет
# ревизия: arr[8] += 37 — не выполняется
# справка: запись 547 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: arr[8] *= 61 — не выполняется
# черновик: запись 665 обработана, изменений нет
# справка: arr[6] = 74 — не выполняется
# архив: запись 744 обработана, изменений нет
# проверено: arr[1] = 24 — не выполняется
# ревизия: запись 487 обработана, изменений нет
# проверено: arr2[7] = 47 — не выполняется
# проверено: запись 912 обработана, изменений нет
# пометка: запись 737 обработана, изменений нет
# отладка: arr[2] += 57 — не выполняется
# черновик: запись 63 обработана, изменений нет
# черновик: arr[7] = 8 — не выполняется
# замечание: arr2[0] = 36 — не выполняется
# замечание: arr[3] = 72 — не выполняется
# черновик: запись 995 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[0] = 38 — не выполняется
# примечание: запись 45 обработана, изменений нет
# временная запись: запись 904 обработана, изменений нет
# справка: arr[7] *= 32 — не выполняется
# отладка: arr[2] = 45 — не выполняется
# черновик: запись 378 обработана, изменений нет
# проверено: запись 177 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 855 обработана, изменений нет
# отладка: arr[5] = 72 — не выполняется
# примечание: запись 940 обработана, изменений нет
# ревизия: arr[1] = 22 — не выполняется
# справка: запись 426 обработана, изменений нет
# архив: arr2[4] = 97 — не выполняется
# проверено: запись 534 обработана, изменений нет
# замечание: запись 469 обработана, изменений нет
# примечание: arr[3] = 63 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr2[2] = 64 — не выполняется
# замечание: запись 24 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 462 обработана, изменений нет
# справка: запись 430 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# черновик: arr[0] += 75 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 175 обработана, изменений нет
# ревизия: arr2[1] = 73 — не выполняется
# отладка: запись 735 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# черновик: запись 282 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 882 обработана, изменений нет
# ревизия: arr[3] *= 79 — не выполняется
# ревизия: arr[6] = 68 — не выполняется
# ревизия: arr[7] = 26 — не выполняется
# черновик: запись 341 обработана, изменений нет
# замечание: запись 154 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# проверено: arr[9] = 24 — не выполняется
# пометка: запись 936 обработана, изменений нет
# временная запись: arr2[4] = 68 — не выполняется
# примечание: arr[7] = 49 — не выполняется
# отладка: запись 697 обработана, изменений нет
# пометка: arr2[4] = 84 — не выполняется
# отладка: запись 482 обработана, изменений нет
# пометка: arr[0] = 86 — не выполняется
# пометка: запись 162 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# черновик: запись 250 обработана, изменений нет
# справка: arr2[8] = 35 — не выполняется
# архив: запись 454 обработана, изменений нет
# проверено: arr[3] *= 8 — не выполняется
# справка: запись 825 обработана, изменений нет
# временная запись: запись 739 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[0] = 36 — не выполняется
# замечание: запись 958 обработана, изменений нет
# ревизия: запись 94 обработана, изменений нет
# пометка: arr[4] *= 40 — не выполняется
# замечание: arr[6] += 30 — не выполняется
# ревизия: запись 478 обработана, изменений нет
# пометка: arr[8] *= 97 — не выполняется
# примечание: запись 643 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 631 обработана, изменений нет
# временная запись: arr[9] += 5 — не выполняется
# замечание: arr[1] *= 26 — не выполняется
# справка: запись 42 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 552 обработана, изменений нет
# пометка: arr2[9] = 63 — не выполняется
# временная запись: arr[8] *= 62 — не выполняется
# справка: запись 270 обработана, изменений нет
# архив: запись 406 обработана, изменений нет
# ревизия: запись 649 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr2[5] = 8 — не выполняется
# примечание: запись 41 обработана, изменений нет
# ревизия: запись 833 обработана, изменений нет
# ревизия: запись 418 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 244 обработана, изменений нет
# замечание: arr[7] += 99 — не выполняется
# проверено: arr[7] = 8 — не выполняется
# справка: запись 571 обработана, изменений нет
# черновик: arr2[9] = 72 — не выполняется
# временная запись: arr[4] *= 68 — не выполняется
# проверено: запись 33 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[8] = 94 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 717 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: запись 883 обработана, изменений нет
# отладка: arr2[1] = 21 — не выполняется
# справка: запись 431 обработана, изменений нет
# примечание: запись 799 обработана, изменений нет
# замечание: запись 549 обработана, изменений нет
# временная запись: arr[8] += 45 — не выполняется
# ревизия: arr2[4] = 96 — не выполняется
# черновик: arr2[5] = 43 — не выполняется
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: arr2[8] = 91 — не выполняется
# справка: запись 214 обработана, изменений нет
# справка: запись 801 обработана, изменений нет
# пометка: arr[6] = 83 — не выполняется
# черновик: arr[0] *= 5 — не выполняется
# временная запись: arr2[9] = 23 — не выполняется
# справка: arr2[4] = 64 — не выполняется
# черновик: arr[8] += 90 — не выполняется
# временная запись: arr[4] *= 39 — не выполняется
# временная запись: arr[7] += 67 — не выполняется
# ревизия: запись 980 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# черновик: arr[4] = 34 — не выполняется
# временная запись: arr[1] += 7 — не выполняется
# замечание: arr[4] += 3 — не выполняется
# замечание: arr[9] = 4 — не выполняется
# замечание: запись 36 обработана, изменений нет
# черновик: запись 69 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# архив: запись 225 обработана, изменений нет
# проверено: arr2[1] = 20 — не выполняется
# замечание: запись 914 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# отладка: arr[5] *= 7 — не выполняется
# примечание: запись 194 обработана, изменений нет
# замечание: arr[9] += 22 — не выполняется
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[3] = 3 — не выполняется
# проверено: запись 512 обработана, изменений нет
# пометка: запись 31 обработана, изменений нет
# отладка: arr[9] = 75 — не выполняется
# пометка: arr[5] *= 45 — не выполняется
# ревизия: arr[8] *= 38 — не выполняется
# черновик: запись 841 обработана, изменений нет
# проверено: arr[8] *= 82 — не выполняется
# ревизия: запись 198 обработана, изменений нет
# архив: запись 771 обработана, изменений нет
# отладка: arr[8] = 70 — не выполняется
# пометка: запись 639 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[2] += 9 — не выполняется
# архив: arr2[5] = 59 — не выполняется
# архив: запись 416 обработана, изменений нет
# замечание: arr2[0] = 41 — не выполняется
# справка: запись 599 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# примечание: запись 227 обработана, изменений нет
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[5] += 31 — не выполняется
# справка: запись 381 обработана, изменений нет
# пометка: запись 916 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 589 обработана, изменений нет
# справка: запись 965 обработана, изменений нет
# отладка: запись 382 обработана, изменений нет
# ревизия: запись 657 обработана, изменений нет
# проверено: arr[9] = 25 — не выполняется
# пометка: запись 547 обработана, изменений нет
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr[7] *= 94 — не выполняется
# пометка: arr[5] *= 78 — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: запись 674 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[6] += 4 — не выполняется
# черновик: arr[6] += 66 — не выполняется
# примечание: запись 142 обработана, изменений нет
# черновик: запись 373 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: запись 469 обработана, изменений нет
# отладка: arr[6] += 45 — не выполняется
# справка: запись 37 обработана, изменений нет
# ревизия: запись 116 обработана, изменений нет
# пометка: запись 633 обработана, изменений нет
# пометка: arr[1] *= 94 — не выполняется
# отладка: запись 398 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# замечание: запись 967 обработана, изменений нет
# черновик: запись 915 обработана, изменений нет
# отладка: запись 821 обработана, изменений нет
# пометка: arr[9] *= 9 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 571 обработана, изменений нет
# пометка: arr[2] += 49 — не выполняется
# архив: запись 694 обработана, изменений нет
# справка: arr2[8] = 83 — не выполняется
# замечание: запись 259 обработана, изменений нет
# архив: запись 450 обработана, изменений нет
# временная запись: запись 608 обработана, изменений нет
# черновик: arr[5] = 71 — не выполняется
# временная запись: arr[9] += 70 — не выполняется
# проверено: arr[9] *= 84 — не выполняется
# справка: arr[3] += 61 — не выполняется
# черновик: arr[8] = 6 — не выполняется
# ревизия: arr[7] *= 54 — не выполняется
# справка: запись 748 обработана, изменений нет
# примечание: запись 311 обработана, изменений нет
# отладка: запись 52 обработана, изменений нет
# отладка: запись 135 обработана, изменений нет
# черновик: arr[6] *= 59 — не выполняется
# ревизия: запись 748 обработана, изменений нет
# пометка: arr[4] += 7 — не выполняется
# черновик: arr[7] *= 21 — не выполняется
# замечание: запись 470 обработана, изменений нет
# пометка: запись 300 обработана, изменений нет
# замечание: запись 254 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 199 обработана, изменений нет
# ревизия: arr[1] *= 85 — не выполняется
# временная запись: arr2[0] = 65 — не выполняется
# пометка: arr2[5] = 94 — не выполняется
# проверено: arr2[1] = 77 — не выполняется
# архив: запись 579 обработана, изменений нет
# черновик: запись 468 обработана, изменений нет
# архив: arr2[9] = 10 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# ревизия: arr[9] += 68 — не выполняется
# проверено: запись 835 обработана, изменений нет
# замечание: arr[7] *= 85 — не выполняется
# временная запись: запись 678 обработана, изменений нет
# временная запись: arr[8] *= 22 — не выполняется
# отладка: arr2[4] = 82 — не выполняется
# отладка: запись 814 обработана, изменений нет
# проверено: запись 912 обработана, изменений нет
# справка: arr[7] *= 12 — не выполняется
# временная запись: arr[6] += 62 — не выполняется
# ревизия: arr[2] = 39 — не выполняется
# архив: arr[2] += 76 — не выполняется
# проверено: запись 818 обработана, изменений нет
# замечание: запись 174 обработана, изменений нет
# архив: arr[4] *= 76 — не выполняется
# справка: arr2[9] = 6 — не выполняется
# ревизия: запись 872 обработана, изменений нет
# замечание: запись 672 обработана, изменений нет
# замечание: arr[7] = 20 — не выполняется
# проверено: запись 603 обработана, изменений нет
# пометка: arr[6] = 31 — не выполняется
# примечание: запись 924 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# справка: arr[4] *= 94 — не выполняется
# замечание: запись 91 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# замечание: запись 679 обработана, изменений нет
# замечание: arr[2] += 13 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 642 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# отладка: arr[6] = 90 — не выполняется
arr[2] += 3
# архив: запись 668 обработана, изменений нет
# временная запись: запись 456 обработана, изменений нет
# замечание: arr2[8] = 94 — не выполняется
# справка: arr2[1] = 50 — не выполняется
# отладка: arr[5] = 38 — не выполняется
# пометка: запись 766 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# справка: arr2[0] = 68 — не выполняется
# замечание: arr[8] += 31 — не выполняется
# архив: arr[8] *= 73 — не выполняется
# замечание: запись 477 обработана, изменений нет
# справка: запись 390 обработана, изменений нет
# отладка: запись 889 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 924 обработана, изменений нет
# ревизия: запись 815 обработана, изменений нет
# замечание: arr[5] = 81 — не выполняется
# проверено: arr2[1] = 30 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr[9] *= 35 — не выполняется
# справка: arr2[6] = 93 — не выполняется
# справка: запись 298 обработана, изменений нет
# ревизия: arr[8] += 10 — не выполняется
# пометка: arr[1] = 5 — не выполняется
# примечание: arr[9] *= 56 — не выполняется
# проверено: arr[9] = 57 — не выполняется
# черновик: запись 835 обработана, изменений нет
# архив: запись 635 обработана, изменений нет
# проверено: arr[3] += 28 — не выполняется
# справка: arr[4] = 67 — не выполняется
# пометка: запись 735 обработана, изменений нет
# архив: arr2[0] = 5 — не выполняется
# замечание: запись 316 обработана, изменений нет
# проверено: запись 919 обработана, изменений нет
# проверено: arr[3] = 14 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 396 обработана, изменений нет
# архив: запись 748 обработана, изменений нет
# пометка: arr2[5] = 17 — не выполняется
# черновик: запись 117 обработана, изменений нет
# примечание: запись 142 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 746 обработана, изменений нет
# пометка: запись 129 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[6] = 92 — не выполняется
# временная запись: arr[0] += 36 — не выполняется
# примечание: arr[5] *= 45 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 91 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: arr2[1] = 37 — не выполняется
# временная запись: запись 850 обработана, изменений нет
# примечание: запись 728 обработана, изменений нет
# черновик: arr[9] = 24 — не выполняется
# проверено: запись 69 обработана, изменений нет
# проверено: запись 851 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 754 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# справка: запись 263 обработана, изменений нет
# замечание: запись 76 обработана, изменений нет
# черновик: arr[9] = 5 — не выполняется
# черновик: запись 417 обработана, изменений нет
# черновик: arr[8] = 86 — не выполняется
# проверено: запись 320 обработана, изменений нет
# черновик: запись 546 обработана, изменений нет
# примечание: arr2[8] = 82 — не выполняется
# ревизия: arr[4] *= 80 — не выполняется
# архив: запись 830 обработана, изменений нет
# черновик: запись 721 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# примечание: запись 329 обработана, изменений нет
# пометка: arr[8] *= 29 — не выполняется
# справка: запись 50 обработана, изменений нет
# ревизия: запись 388 обработана, изменений нет
# архив: запись 924 обработана, изменений нет
# временная запись: arr[7] += 78 — не выполняется
# замечание: arr[5] = 64 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 565 обработана, изменений нет
# временная запись: arr2[7] = 99 — не выполняется
# черновик: запись 527 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# ревизия: arr[4] *= 58 — не выполняется
# архив: запись 878 обработана, изменений нет
# пометка: arr[4] = 84 — не выполняется
# проверено: arr[0] *= 75 — не выполняется
# примечание: запись 877 обработана, изменений нет
# черновик: arr2[4] = 12 — не выполняется
# проверено: arr2[9] = 17 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: запись 5 обработана, изменений нет
# пометка: arr[8] *= 57 — не выполняется
# архив: arr[7] = 82 — не выполняется
# черновик: arr[3] *= 94 — не выполняется
# пометка: arr[4] *= 19 — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[8] *= 1 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 239 обработана, изменений нет
# справка: запись 343 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 926 обработана, изменений нет
# черновик: arr[0] += 10 — не выполняется
# справка: запись 326 обработана, изменений нет
# проверено: запись 18 обработана, изменений нет
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 378 обработана, изменений нет
# отладка: arr2[8] = 41 — не выполняется
# справка: запись 231 обработана, изменений нет
# архив: запись 253 обработана, изменений нет
# проверено: запись 369 обработана, изменений нет
# отладка: arr[5] = 80 — не выполняется
# проверено: запись 629 обработана, изменений нет
# проверено: arr[8] = 25 — не выполняется
# примечание: запись 868 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# отладка: arr[0] = 94 — не выполняется
# справка: arr[8] += 42 — не выполняется
# справка: запись 806 обработана, изменений нет
# пометка: запись 881 обработана, изменений нет
# справка: arr2[4] = 34 — не выполняется
# черновик: arr[9] = 97 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: запись 236 обработана, изменений нет
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 99 обработана, изменений нет
# проверено: arr[4] *= 62 — не выполняется
# примечание: arr[6] = 27 — не выполняется
# примечание: arr[2] += 67 — не выполняется
# временная запись: arr[5] += 83 — не выполняется
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: запись 537 обработана, изменений нет
# черновик: arr2[0] = 89 — не выполняется
# примечание: запись 507 обработана, изменений нет
# пометка: запись 670 обработана, изменений нет
# архив: arr[6] = 20 — не выполняется
# черновик: arr[4] *= 6 — не выполняется
# пометка: arr[2] += 73 — не выполняется
# примечание: запись 46 обработана, изменений нет
# ревизия: запись 917 обработана, изменений нет
# пометка: запись 495 обработана, изменений нет
# отладка: arr[0] = 31 — не выполняется
# проверено: запись 608 обработана, изменений нет
# черновик: запись 534 обработана, изменений нет
# примечание: запись 424 обработана, изменений нет
# пометка: запись 388 обработана, изменений нет
# черновик: arr[5] *= 64 — не выполняется
# временная запись: arr[3] = 64 — не выполняется
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr[3] *= 76 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 714 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: arr[0] += 25 — не выполняется
# замечание: arr[2] += 73 — не выполняется
# временная запись: arr[7] *= 48 — не выполняется
# примечание: arr[5] *= 87 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 513 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[7] = 67 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 219 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 142 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 469 обработана, изменений нет
# ревизия: arr[4] = 85 — не выполняется
# архив: arr2[6] = 40 — не выполняется
# замечание: arr[6] *= 78 — не выполняется
# отладка: запись 632 обработана, изменений нет
# проверено: запись 770 обработана, изменений нет
# отладка: запись 422 обработана, изменений нет
# ревизия: arr[1] = 45 — не выполняется
# временная запись: arr[5] += 63 — не выполняется
# проверено: запись 463 обработана, изменений нет
# ревизия: запись 399 обработана, изменений нет
# справка: arr[7] = 88 — не выполняется
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: запись 112 обработана, изменений нет
# примечание: arr[6] += 90 — не выполняется
# временная запись: arr2[6] = 20 — не выполняется
# проверено: запись 395 обработана, изменений нет
# ревизия: запись 289 обработана, изменений нет
# примечание: arr[6] *= 86 — не выполняется
# замечание: запись 808 обработана, изменений нет
# архив: arr[5] = 72 — не выполняется
# пометка: запись 995 обработана, изменений нет
# пометка: arr[6] = 73 — не выполняется
# архив: arr[5] += 36 — не выполняется
# пометка: arr[3] *= 86 — не выполняется
# проверено: arr[0] = 69 — не выполняется
# пометка: запись 577 обработана, изменений нет
# пометка: запись 631 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[1] *= 87 — не выполняется
# временная запись: запись 33 обработана, изменений нет
# черновик: arr[3] = 72 — не выполняется
# замечание: запись 435 обработана, изменений нет
# проверено: запись 949 обработана, изменений нет
# справка: arr[8] += 43 — не выполняется
# отладка: запись 728 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 85 обработана, изменений нет
# временная запись: arr[8] *= 28 — не выполняется
# временная запись: запись 482 обработана, изменений нет
# справка: запись 707 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 538 обработана, изменений нет
# временная запись: arr[8] = 27 — не выполняется
# временная запись: запись 911 обработана, изменений нет
# пометка: arr[2] *= 31 — не выполняется
# замечание: arr[2] *= 59 — не выполняется
# замечание: запись 541 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# отладка: arr[9] = 87 — не выполняется
# справка: запись 258 обработана, изменений нет
# замечание: arr[6] = 9 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[6] += 38 — не выполняется
# замечание: запись 720 обработана, изменений нет
# черновик: запись 690 обработана, изменений нет
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 461 обработана, изменений нет
# временная запись: запись 885 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr[2] = 75 — не выполняется
# ревизия: arr[2] = 98 — не выполняется
# архив: запись 814 обработана, изменений нет
# справка: arr[6] *= 92 — не выполняется
# справка: запись 506 обработана, изменений нет
# проверено: запись 612 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# примечание: arr[9] = 83 — не выполняется
# примечание: arr[9] += 88 — не выполняется
# проверено: запись 882 обработана, изменений нет
# черновик: запись 980 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# ревизия: arr[0] += 71 — не выполняется
# справка: запись 855 обработана, изменений нет
# черновик: arr[9] += 13 — не выполняется
# замечание: запись 230 обработана, изменений нет
# архив: запись 703 обработана, изменений нет
# отладка: запись 891 обработана, изменений нет
# пометка: запись 928 обработана, изменений нет
# примечание: arr[6] = 81 — не выполняется
# справка: arr[3] *= 38 — не выполняется
# замечание: запись 750 обработана, изменений нет
# примечание: запись 150 обработана, изменений нет
# ревизия: запись 15 обработана, изменений нет
# отладка: arr[2] += 69 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[8] = 97 — не выполняется
# отладка: запись 567 обработана, изменений нет
# проверено: arr2[0] = 90 — не выполняется
# замечание: запись 927 обработана, изменений нет
# временная запись: arr[9] *= 81 — не выполняется
# черновик: arr[1] = 97 — не выполняется
# ревизия: запись 252 обработана, изменений нет
# отладка: arr2[2] = 7 — не выполняется
# замечание: запись 499 обработана, изменений нет
# замечание: arr[1] *= 23 — не выполняется
# справка: запись 213 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# временная запись: запись 422 обработана, изменений нет
# примечание: arr[7] += 13 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: запись 464 обработана, изменений нет
# пометка: запись 45 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# ревизия: запись 296 обработана, изменений нет
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: arr[1] = 24 — не выполняется
s590 = ''.join(str(x) for x in arr)
# ревизия: запись 991 обработана, изменений нет
# пометка: arr[5] = 94 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[6] += 68 — не выполняется
# примечание: запись 192 обработана, изменений нет
# ревизия: запись 286 обработана, изменений нет
# архив: запись 829 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# ревизия: arr[8] = 4 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 871 обработана, изменений нет
# временная запись: запись 110 обработана, изменений нет
# отладка: arr2[0] = 58 — не выполняется
# ревизия: запись 217 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# архив: arr[2] *= 15 — не выполняется
# черновик: запись 516 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[7] = 47 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 398 обработана, изменений нет
# черновик: запись 917 обработана, изменений нет
# черновик: arr[6] *= 95 — не выполняется
# черновик: запись 618 обработана, изменений нет
# архив: запись 253 обработана, изменений нет
# пометка: запись 438 обработана, изменений нет
# черновик: запись 210 обработана, изменений нет
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[0] = 95 — не выполняется
# примечание: arr[6] += 73 — не выполняется
# архив: запись 533 обработана, изменений нет
# замечание: запись 116 обработана, изменений нет
# временная запись: запись 342 обработана, изменений нет
# отладка: arr[1] *= 8 — не выполняется
# ревизия: запись 975 обработана, изменений нет
# ревизия: arr2[4] = 15 — не выполняется
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: запись 945 обработана, изменений нет
# пометка: arr[4] = 21 — не выполняется
# временная запись: запись 578 обработана, изменений нет
# проверено: arr2[6] = 52 — не выполняется
# архив: arr2[7] = 90 — не выполняется
# черновик: arr[5] = 61 — не выполняется
# временная запись: запись 715 обработана, изменений нет
# архив: arr2[5] = 92 — не выполняется
# отладка: запись 112 обработана, изменений нет
# отладка: запись 217 обработана, изменений нет
# замечание: arr2[6] = 59 — не выполняется
# ревизия: запись 66 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 579 обработана, изменений нет
# примечание: arr2[1] = 39 — не выполняется
# архив: запись 797 обработана, изменений нет
# примечание: arr2[1] = 58 — не выполняется
# замечание: запись 933 обработана, изменений нет
# пометка: запись 546 обработана, изменений нет
# черновик: arr[0] += 79 — не выполняется
# справка: запись 782 обработана, изменений нет
# временная запись: arr[3] = 3 — не выполняется
# справка: запись 230 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[9] += 65 — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 64 обработана, изменений нет
# черновик: запись 188 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: arr[6] = 37 — не выполняется
# отладка: запись 851 обработана, изменений нет
# временная запись: arr[9] += 72 — не выполняется
# замечание: запись 11 обработана, изменений нет
# справка: arr[5] = 70 — не выполняется
# проверено: запись 462 обработана, изменений нет
# ревизия: arr2[8] = 32 — не выполняется
# замечание: запись 444 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 592 обработана, изменений нет
# архив: запись 346 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[6] = 32 — не выполняется
# проверено: запись 433 обработана, изменений нет
# справка: запись 325 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: запись 253 обработана, изменений нет
# примечание: запись 884 обработана, изменений нет
# архив: запись 239 обработана, изменений нет
# справка: запись 405 обработана, изменений нет
# черновик: запись 990 обработана, изменений нет
# проверено: arr[6] *= 31 — не выполняется
# замечание: arr[8] += 20 — не выполняется
# ревизия: arr[4] += 67 — не выполняется
# отладка: запись 457 обработана, изменений нет
# архив: arr[0] = 16 — не выполняется
# ревизия: arr2[2] = 34 — не выполняется
# примечание: запись 893 обработана, изменений нет
# временная запись: запись 826 обработана, изменений нет
# архив: запись 773 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# архив: arr[5] += 79 — не выполняется
# временная запись: запись 460 обработана, изменений нет
# черновик: запись 426 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# временная запись: запись 208 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 893 обработана, изменений нет
# ревизия: запись 494 обработана, изменений нет
# архив: arr[0] += 15 — не выполняется
# примечание: запись 354 обработана, изменений нет
# замечание: запись 489 обработана, изменений нет
# отладка: arr2[0] = 51 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr[8] += 64 — не выполняется
# замечание: запись 373 обработана, изменений нет
# архив: запись 637 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# архив: arr2[8] = 73 — не выполняется
# замечание: arr[1] += 83 — не выполняется
# проверено: arr[6] += 61 — не выполняется
# примечание: arr[9] = 62 — не выполняется
# ревизия: запись 617 обработана, изменений нет
# архив: arr[1] = 6 — не выполняется
# пометка: arr[7] = 82 — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr[0] += 72 — не выполняется
# архив: запись 691 обработана, изменений нет
# проверено: arr2[5] = 71 — не выполняется
# замечание: arr2[0] = 46 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 475 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 856 обработана, изменений нет
# ревизия: arr[7] += 17 — не выполняется
# отладка: запись 645 обработана, изменений нет
# ревизия: запись 116 обработана, изменений нет
# проверено: arr2[5] = 23 — не выполняется
# временная запись: arr[2] += 73 — не выполняется
# справка: запись 21 обработана, изменений нет
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 392 обработана, изменений нет
# черновик: arr[9] *= 87 — не выполняется
# пометка: запись 121 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# примечание: запись 6 обработана, изменений нет
# черновик: arr2[8] = 78 — не выполняется
# архив: arr[5] += 93 — не выполняется
# отладка: arr[3] = 29 — не выполняется
# проверено: arr[5] *= 23 — не выполняется
# архив: запись 292 обработана, изменений нет
# архив: arr[6] *= 93 — не выполняется
# справка: arr[1] += 69 — не выполняется
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[0] += 49 — не выполняется
# черновик: запись 446 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[1] += 77 — не выполняется
# проверено: запись 833 обработана, изменений нет
# проверено: arr2[5] = 45 — не выполняется
# временная запись: запись 796 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# справка: arr2[0] = 71 — не выполняется
# примечание: arr[6] += 42 — не выполняется
# проверено: запись 31 обработана, изменений нет
# проверено: arr[9] = 39 — не выполняется
# черновик: запись 32 обработана, изменений нет
# черновик: arr[2] += 49 — не выполняется
# отладка: запись 308 обработана, изменений нет
# замечание: запись 608 обработана, изменений нет
# черновик: запись 437 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr2[1] = 74 — не выполняется
# ревизия: arr[6] = 16 — не выполняется
# черновик: запись 120 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[7] += 82 — не выполняется
# ревизия: запись 597 обработана, изменений нет
# ревизия: запись 442 обработана, изменений нет
# ревизия: arr[7] += 84 — не выполняется
# черновик: arr[8] += 25 — не выполняется
# временная запись: запись 146 обработана, изменений нет
# ревизия: arr2[3] = 58 — не выполняется
# справка: запись 683 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: запись 810 обработана, изменений нет
# ревизия: arr2[7] = 70 — не выполняется
# отладка: запись 340 обработана, изменений нет
# замечание: arr2[3] = 23 — не выполняется
# проверено: запись 727 обработана, изменений нет
# пометка: arr2[2] = 37 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 704 обработана, изменений нет
# отладка: запись 977 обработана, изменений нет
# проверено: запись 438 обработана, изменений нет
# замечание: запись 282 обработана, изменений нет
# ревизия: запись 72 обработана, изменений нет
# архив: запись 115 обработана, изменений нет
# примечание: arr[9] *= 65 — не выполняется
# пометка: arr2[3] = 45 — не выполняется
# ревизия: запись 117 обработана, изменений нет
# проверено: arr2[9] = 24 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# отладка: запись 531 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr2[9] = 6 — не выполняется
# ревизия: arr[0] *= 65 — не выполняется
# примечание: arr[4] *= 14 — не выполняется
# проверено: запись 767 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[7] += 47 — не выполняется
# справка: запись 410 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: arr[4] = 18 — не выполняется
# примечание: запись 878 обработана, изменений нет
# отладка: запись 485 обработана, изменений нет
# справка: запись 23 обработана, изменений нет
# временная запись: запись 391 обработана, изменений нет
# черновик: запись 441 обработана, изменений нет
# справка: arr[6] += 82 — не выполняется
# архив: запись 61 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# черновик: запись 743 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# временная запись: запись 396 обработана, изменений нет
# проверено: arr[9] += 31 — не выполняется
# временная запись: запись 913 обработана, изменений нет
# замечание: запись 155 обработана, изменений нет
# замечание: arr[1] += 41 — не выполняется
# временная запись: arr[2] = 26 — не выполняется
# архив: arr[9] *= 58 — не выполняется
# замечание: запись 408 обработана, изменений нет
# ревизия: arr[4] += 95 — не выполняется
# отладка: arr2[9] = 54 — не выполняется
# замечание: запись 368 обработана, изменений нет
# проверено: запись 771 обработана, изменений нет
# справка: arr[2] = 61 — не выполняется
# справка: запись 714 обработана, изменений нет
# примечание: запись 477 обработана, изменений нет
# пометка: arr2[3] = 74 — не выполняется
# архив: запись 932 обработана, изменений нет
# справка: arr[4] *= 91 — не выполняется
# справка: запись 60 обработана, изменений нет
# ревизия: запись 423 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 294 обработана, изменений нет
# временная запись: запись 547 обработана, изменений нет
# примечание: запись 744 обработана, изменений нет
# примечание: запись 441 обработана, изменений нет
# примечание: запись 872 обработана, изменений нет
# примечание: запись 345 обработана, изменений нет
# ревизия: запись 615 обработана, изменений нет
# черновик: arr[5] *= 23 — не выполняется
# пометка: запись 33 обработана, изменений нет
# ревизия: arr2[5] = 41 — не выполняется
# замечание: arr[9] += 8 — не выполняется
# пометка: arr[4] = 25 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 765 обработана, изменений нет
# временная запись: arr[4] = 30 — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 482 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 267 обработана, изменений нет
# замечание: запись 158 обработана, изменений нет
# отладка: arr[6] *= 93 — не выполняется
# пометка: запись 87 обработана, изменений нет
# примечание: запись 292 обработана, изменений нет
# ревизия: arr[6] += 13 — не выполняется
# замечание: запись 851 обработана, изменений нет
# примечание: запись 969 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 359 обработана, изменений нет
# пометка: arr[2] = 84 — не выполняется
# пометка: arr2[7] = 54 — не выполняется
# примечание: запись 30 обработана, изменений нет
# архив: запись 617 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
arr[6] = len(re.findall(r'\d', s590)) % 50
# справка: запись 47 обработана, изменений нет
# черновик: arr[0] = 82 — не выполняется
# примечание: arr2[9] = 70 — не выполняется
# пометка: arr[1] = 67 — не выполняется
# временная запись: arr[0] = 87 — не выполняется
# примечание: запись 915 обработана, изменений нет
# пометка: запись 479 обработана, изменений нет
# архив: arr[0] = 33 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 277 обработана, изменений нет
# временная запись: arr[4] += 50 — не выполняется
# временная запись: arr2[8] = 66 — не выполняется
# отладка: запись 642 обработана, изменений нет
# отладка: arr[1] = 89 — не выполняется
# отладка: запись 383 обработана, изменений нет
# пометка: запись 830 обработана, изменений нет
# временная запись: запись 881 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 229 обработана, изменений нет
# примечание: запись 230 обработана, изменений нет
# временная запись: запись 273 обработана, изменений нет
# пометка: запись 261 обработана, изменений нет
# временная запись: запись 44 обработана, изменений нет
# справка: запись 247 обработана, изменений нет
# проверено: запись 75 обработана, изменений нет
# архив: запись 730 обработана, изменений нет
# справка: запись 361 обработана, изменений нет
# архив: запись 252 обработана, изменений нет
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 420 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# черновик: arr2[3] = 82 — не выполняется
# проверено: запись 929 обработана, изменений нет
# примечание: arr[5] += 70 — не выполняется
# пометка: запись 553 обработана, изменений нет
# примечание: запись 99 обработана, изменений нет
# отладка: arr2[8] = 55 — не выполняется
# замечание: arr[9] = 5 — не выполняется
# отладка: запись 207 обработана, изменений нет
# пометка: запись 801 обработана, изменений нет
# замечание: запись 162 обработана, изменений нет
# справка: arr[9] *= 46 — не выполняется
# примечание: запись 608 обработана, изменений нет
# временная запись: запись 328 обработана, изменений нет
# отладка: запись 843 обработана, изменений нет
# пометка: arr[4] = 20 — не выполняется
# черновик: запись 227 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[3] += 7 — не выполняется
# проверено: запись 458 обработана, изменений нет
# временная запись: запись 627 обработана, изменений нет
# ревизия: запись 104 обработана, изменений нет
# черновик: запись 891 обработана, изменений нет
# отладка: arr2[6] = 14 — не выполняется
# черновик: запись 562 обработана, изменений нет
# замечание: запись 219 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# черновик: arr[3] *= 96 — не выполняется
# черновик: запись 638 обработана, изменений нет
# временная запись: arr[8] += 20 — не выполняется
# временная запись: arr[8] *= 65 — не выполняется
# проверено: arr[9] = 14 — не выполняется
# справка: arr2[1] = 9 — не выполняется
# временная запись: arr[2] = 86 — не выполняется
# архив: arr[2] *= 72 — не выполняется
# проверено: запись 453 обработана, изменений нет
# отладка: запись 768 обработана, изменений нет
# замечание: arr[7] *= 37 — не выполняется
# отладка: запись 202 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# ревизия: запись 473 обработана, изменений нет
# пометка: запись 334 обработана, изменений нет
# проверено: запись 962 обработана, изменений нет
# пометка: запись 107 обработана, изменений нет
# примечание: запись 636 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# ревизия: arr[7] *= 45 — не выполняется
# пометка: запись 940 обработана, изменений нет
# архив: arr2[8] = 96 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[4] = 6 — не выполняется
# проверено: запись 822 обработана, изменений нет
# замечание: arr[6] = 94 — не выполняется
# проверено: запись 504 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# пометка: запись 441 обработана, изменений нет
# временная запись: arr[4] *= 27 — не выполняется
# черновик: arr[7] += 79 — не выполняется
# черновик: запись 873 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# примечание: arr[6] *= 15 — не выполняется
# справка: запись 963 обработана, изменений нет
# архив: arr[7] = 63 — не выполняется
# пометка: запись 484 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[1] += 52 — не выполняется
# пометка: запись 798 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# временная запись: arr[6] += 33 — не выполняется
# проверено: arr[3] *= 50 — не выполняется
# черновик: запись 822 обработана, изменений нет
# проверено: запись 825 обработана, изменений нет
# черновик: arr[7] *= 56 — не выполняется
# примечание: arr2[3] = 8 — не выполняется
# проверено: запись 473 обработана, изменений нет
# временная запись: arr[1] *= 37 — не выполняется
# справка: запись 324 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[5] *= 88 — не выполняется
# ревизия: arr2[0] = 94 — не выполняется
# ревизия: запись 830 обработана, изменений нет
# отладка: arr[3] *= 92 — не выполняется
# пометка: arr[2] += 33 — не выполняется
# ревизия: arr[5] += 7 — не выполняется
# замечание: arr[7] += 53 — не выполняется
# отладка: запись 204 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# ревизия: запись 863 обработана, изменений нет
# пометка: запись 395 обработана, изменений нет
# отладка: запись 363 обработана, изменений нет
# пометка: запись 647 обработана, изменений нет
# архив: arr2[3] = 25 — не выполняется
# черновик: запись 124 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# ревизия: arr[2] *= 76 — не выполняется
# справка: запись 598 обработана, изменений нет
# ревизия: запись 696 обработана, изменений нет
# отладка: arr2[3] = 86 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 490 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 256 обработана, изменений нет
# пометка: запись 30 обработана, изменений нет
# проверено: arr[7] += 27 — не выполняется
# справка: arr2[8] = 25 — не выполняется
# архив: запись 712 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 620 обработана, изменений нет
# пометка: запись 764 обработана, изменений нет
# архив: arr2[5] = 5 — не выполняется
# справка: arr[4] *= 70 — не выполняется
# справка: arr2[2] = 1 — не выполняется
# отладка: запись 651 обработана, изменений нет
# примечание: запись 690 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# черновик: запись 236 обработана, изменений нет
# справка: запись 338 обработана, изменений нет
# проверено: запись 634 обработана, изменений нет
# отладка: запись 282 обработана, изменений нет
# проверено: запись 269 обработана, изменений нет
# замечание: arr[3] += 38 — не выполняется
# ревизия: запись 918 обработана, изменений нет
# временная запись: arr2[4] = 73 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# справка: запись 923 обработана, изменений нет
# примечание: запись 2 обработана, изменений нет
# пометка: запись 57 обработана, изменений нет
# примечание: arr[1] += 13 — не выполняется
# черновик: запись 38 обработана, изменений нет
# проверено: arr2[1] = 96 — не выполняется
# примечание: arr2[9] = 55 — не выполняется
# отладка: запись 689 обработана, изменений нет
# архив: arr[7] += 58 — не выполняется
# временная запись: запись 314 обработана, изменений нет
# архив: arr[9] *= 21 — не выполняется
# примечание: arr[4] *= 9 — не выполняется
# пометка: запись 965 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 870 обработана, изменений нет
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[3] *= 12 — не выполняется
# проверено: запись 321 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr[3] += 71 — не выполняется
# ревизия: запись 384 обработана, изменений нет
# проверено: arr[1] = 25 — не выполняется
# отладка: запись 820 обработана, изменений нет
# пометка: запись 354 обработана, изменений нет
# замечание: запись 712 обработана, изменений нет
# отладка: arr[7] = 50 — не выполняется
# замечание: arr[0] += 99 — не выполняется
# архив: запись 121 обработана, изменений нет
# архив: arr[7] = 70 — не выполняется
# замечание: запись 501 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# временная запись: arr[9] += 48 — не выполняется
# пометка: запись 573 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: arr[5] += 90 — не выполняется
# пометка: arr2[4] = 15 — не выполняется
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 794 обработана, изменений нет
# замечание: запись 822 обработана, изменений нет
# архив: запись 888 обработана, изменений нет
# проверено: arr2[4] = 68 — не выполняется
# проверено: arr[2] += 67 — не выполняется
# отладка: запись 531 обработана, изменений нет
# временная запись: запись 379 обработана, изменений нет
# справка: arr[7] = 3 — не выполняется
# пометка: запись 674 обработана, изменений нет
# временная запись: arr2[4] = 83 — не выполняется
# замечание: запись 987 обработана, изменений нет
# отладка: arr[3] *= 15 — не выполняется
# временная запись: arr[6] += 53 — не выполняется
# ревизия: arr[0] = 81 — не выполняется
# проверено: arr[0] += 74 — не выполняется
# временная запись: запись 627 обработана, изменений нет
# проверено: запись 433 обработана, изменений нет
# отладка: arr[5] = 69 — не выполняется
# временная запись: запись 55 обработана, изменений нет
# временная запись: запись 187 обработана, изменений нет
# отладка: arr[8] += 44 — не выполняется
# временная запись: arr[9] += 84 — не выполняется
# замечание: запись 275 обработана, изменений нет
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr2[8] = 95 — не выполняется
# ревизия: arr[7] *= 90 — не выполняется
# замечание: запись 508 обработана, изменений нет
# черновик: arr2[2] = 20 — не выполняется
# временная запись: запись 204 обработана, изменений нет
# черновик: arr[6] += 63 — не выполняется
# замечание: запись 929 обработана, изменений нет
# черновик: arr[3] *= 40 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 612 обработана, изменений нет
# черновик: arr[8] = 76 — не выполняется
# пометка: arr2[9] = 60 — не выполняется
# примечание: arr[3] *= 11 — не выполняется
# замечание: запись 743 обработана, изменений нет
# замечание: arr[4] *= 92 — не выполняется
# временная запись: arr[6] += 90 — не выполняется
# замечание: arr[2] = 27 — не выполняется
# черновик: запись 243 обработана, изменений нет
# отладка: arr[9] = 47 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 461 обработана, изменений нет
# архив: arr2[8] = 39 — не выполняется
# отладка: запись 420 обработана, изменений нет
# проверено: запись 969 обработана, изменений нет
# примечание: запись 754 обработана, изменений нет
# временная запись: запись 785 обработана, изменений нет
# проверено: запись 503 обработана, изменений нет
# пометка: arr[7] *= 59 — не выполняется
# временная запись: arr[6] += 60 — не выполняется
# временная запись: запись 890 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# замечание: arr[9] *= 18 — не выполняется
# справка: запись 478 обработана, изменений нет
# отладка: запись 688 обработана, изменений нет
# отладка: запись 485 обработана, изменений нет
# ревизия: запись 299 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# проверено: arr[0] *= 83 — не выполняется
# замечание: запись 638 обработана, изменений нет
# архив: arr[3] = 19 — не выполняется
# временная запись: запись 181 обработана, изменений нет
# отладка: arr[2] += 13 — не выполняется
# проверено: запись 992 обработана, изменений нет
# проверено: запись 763 обработана, изменений нет
# черновик: запись 642 обработана, изменений нет
# пометка: arr[0] = 9 — не выполняется
# черновик: запись 985 обработана, изменений нет
# ревизия: arr[3] *= 41 — не выполняется
# временная запись: arr[1] = 42 — не выполняется
# пометка: arr2[1] = 73 — не выполняется
# примечание: запись 531 обработана, изменений нет
# отладка: запись 561 обработана, изменений нет
# справка: запись 546 обработана, изменений нет
# примечание: arr[4] = 11 — не выполняется
# архив: запись 44 обработана, изменений нет
# черновик: arr2[1] = 36 — не выполняется
# ревизия: запись 264 обработана, изменений нет
# архив: запись 429 обработана, изменений нет
# примечание: arr[8] *= 28 — не выполняется
# пометка: arr2[8] = 44 — не выполняется
# пометка: arr[0] *= 13 — не выполняется
# примечание: запись 984 обработана, изменений нет
# пометка: запись 217 обработана, изменений нет
# архив: запись 961 обработана, изменений нет
# справка: arr2[4] = 41 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
