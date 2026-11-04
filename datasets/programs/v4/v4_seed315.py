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
arr[4] += 44
arr[1] *= 2
arr[8] = 14
arr[1], arr[4] = arr[4], arr[1]
arr[6], arr[1] = arr[1], arr[6]
arr[0] *= 30
arr[5] = 3
arr[3] = 15
"""

TRAP_0 = "arr[1] = 330"
TRAP_1 = "arr[0] = 394"
TRAP_2 = "arr[2] = 246"
TRAP_3 = "arr[9] = 201"
TRAP_4 = "arr[5] = 780"
TRAP_5 = "arr[0] = 801"
TRAP_6 = "arr[5] = 483"
TRAP_7 = "arr[8] = 944"
TRAP_8 = "arr[7] = 392"
TRAP_9 = "arr[0] = 866"
TRAP_10 = "arr[6] = 922"
TRAP_11 = "arr[7] = 671"
TRAP_12 = "arr[6] = 578"
TRAP_13 = "arr[9] = 577"
TRAP_14 = "arr[1] = 297"
TRAP_15 = "arr[4] = 114"
TRAP_16 = "arr[1] = 536"
TRAP_17 = "arr[3] = 309"
TRAP_18 = "arr[2] = 775"
TRAP_19 = "arr[0] = 912"
TRAP_20 = "arr[2] = 462"
TRAP_21 = "arr[3] = 451"
TRAP_22 = "arr[4] = 208"
TRAP_23 = "arr[6] = 376"
TRAP_24 = "arr[9] = 707"
TRAP_25 = "arr[1] = 331"
TRAP_26 = "arr[0] = 655"
TRAP_27 = "arr[5] = 109"
TRAP_28 = "arr[8] = 974"
TRAP_29 = "arr[3] = 446"
TRAP_30 = "arr[0] = 838"
TRAP_31 = "arr[9] = 595"
TRAP_32 = "arr[4] = 247"
TRAP_33 = "arr[5] = 903"
TRAP_34 = "arr[0] = 226"
TRAP_35 = "arr[3] = 791"
TRAP_36 = "arr[4] = 422"
TRAP_37 = "arr[7] = 297"
TRAP_38 = "arr[5] = 932"
TRAP_39 = "arr[2] = 998"
TRAP_40 = "arr[2] = 922"
TRAP_41 = "arr[2] = 420"
TRAP_42 = "arr[6] = 911"
TRAP_43 = "arr[7] = 333"
TRAP_44 = "arr[1] = 631"
TRAP_45 = "arr[3] = 371"
TRAP_46 = "arr[4] = 502"
TRAP_47 = "arr[0] = 583"
TRAP_48 = "arr[9] = 363"
TRAP_49 = "arr[5] = 613"
TRAP_50 = "arr[8] = 160"
TRAP_51 = "arr[7] = 748"
TRAP_52 = "arr[5] = 360"
TRAP_53 = "arr[6] = 300"
TRAP_54 = "arr[9] = 156"
TRAP_55 = "arr[6] = 335"
TRAP_56 = "arr[3] = 618"
TRAP_57 = "arr[6] = 209"
TRAP_58 = "arr[9] = 787"
TRAP_59 = "arr[8] = 923"
TRAP_60 = "arr[3] = 724"
TRAP_61 = "arr[3] = 563"
TRAP_62 = "arr[7] = 328"
TRAP_63 = "arr[8] = 626"
TRAP_64 = "arr[6] = 443"
TRAP_65 = "arr[3] = 903"
TRAP_66 = "arr[4] = 964"
TRAP_67 = "arr[0] = 617"
TRAP_68 = "arr[6] = 314"
TRAP_69 = "arr[8] = 377"
TRAP_70 = "arr[3] = 176"
TRAP_71 = "arr[6] = 838"
TRAP_72 = "arr[6] = 420"
TRAP_73 = "arr[0] = 246"
TRAP_74 = "arr[4] = 594"
TRAP_75 = "arr[8] = 313"
TRAP_76 = "arr[2] = 447"
TRAP_77 = "arr[4] = 188"
TRAP_78 = "arr[0] = 389"
TRAP_79 = "arr[8] = 944"
TRAP_80 = "arr[7] = 811"
TRAP_81 = "arr[2] = 803"
TRAP_82 = "arr[3] = 588"
TRAP_83 = "arr[5] = 432"
TRAP_84 = "arr[8] = 319"
TRAP_85 = "arr[1] = 774"
TRAP_86 = "arr[5] = 389"
TRAP_87 = "arr[7] = 447"
TRAP_88 = "arr[2] = 225"
TRAP_89 = "arr[4] = 277"
TRAP_90 = "arr[8] = 217"
TRAP_91 = "arr[2] = 984"
TRAP_92 = "arr[3] = 532"
TRAP_93 = "arr[1] = 148"
TRAP_94 = "arr[4] = 327"
TRAP_95 = "arr[3] = 719"
TRAP_96 = "arr[2] = 671"
TRAP_97 = "arr[8] = 115"
TRAP_98 = "arr[8] = 907"
TRAP_99 = "arr[9] = 307"
TRAP_100 = "arr[2] = 224"
TRAP_101 = "arr[5] = 146"
TRAP_102 = "arr[6] = 215"
TRAP_103 = "arr[0] = 451"
TRAP_104 = "arr[2] = 856"
TRAP_105 = "arr[5] = 567"
TRAP_106 = "arr[1] = 196"
TRAP_107 = "arr[0] = 313"
TRAP_108 = "arr[0] = 772"
TRAP_109 = "arr[9] = 218"
TRAP_110 = "arr[2] = 185"
TRAP_111 = "arr[7] = 284"
TRAP_112 = "arr[9] = 544"
TRAP_113 = "arr[3] = 396"
TRAP_114 = "arr[8] = 622"
TRAP_115 = "arr[2] = 249"
TRAP_116 = "arr[5] = 519"
TRAP_117 = "arr[0] = 127"
TRAP_118 = "arr[2] = 990"
TRAP_119 = "arr[4] = 161"
TRAP_120 = "arr[3] = 152"
TRAP_121 = "arr[6] = 714"
TRAP_122 = "arr[1] = 684"
TRAP_123 = "arr[2] = 667"
TRAP_124 = "arr[8] = 913"
TRAP_125 = "arr[6] = 372"
TRAP_126 = "arr[7] = 800"
TRAP_127 = "arr[8] = 543"
TRAP_128 = "arr[6] = 283"
TRAP_129 = "arr[7] = 992"
TRAP_130 = "arr[7] = 638"
TRAP_131 = "arr[5] = 579"
TRAP_132 = "arr[9] = 290"
TRAP_133 = "arr[7] = 780"
TRAP_134 = "arr[5] = 720"
TRAP_135 = "arr[7] = 666"
TRAP_136 = "arr[1] = 647"
TRAP_137 = "arr[0] = 292"
TRAP_138 = "arr[3] = 849"
TRAP_139 = "arr[8] = 658"
TRAP_140 = "arr[8] = 433"
TRAP_141 = "arr[0] = 121"
TRAP_142 = "arr[0] = 232"
TRAP_143 = "arr[0] = 524"
TRAP_144 = "arr[0] = 292"
TRAP_145 = "arr[9] = 502"
TRAP_146 = "arr[2] = 900"
TRAP_147 = "arr[6] = 469"
TRAP_148 = "arr[4] = 829"
TRAP_149 = "arr[3] = 636"

arr = [14, 23, 14, 11, 1, 12, 19, 21, 2, 3]

tmp_0 = arr[0] + 40
tmp_1 = arr[4] + 23
tmp_2 = arr[2] + 50
tmp_3 = arr[9] + 16
tmp_4 = arr[8] + 43
note_5 = str(arr[4]) + str(arr[4])
code_6 = re.sub(r'[0-9]', '#', str(arr[6]))
label_7 = "запись 7 не применялась"
note_8 = str(arr[7]) + str(arr[2])
tmp_9 = arr[1] + 30
copy_10 = arr[0]
note_11 = str(arr[4]) + str(arr[3])
note_12 = str(arr[6]) + str(arr[9])
code_13 = re.sub(r'[0-9]', '#', str(arr[0]))
code_14 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_15 = arr[0]
copy_16 = arr[8]
note_17 = str(arr[8]) + str(arr[8])
code_18 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_19 = arr[9] + 41
tmp_20 = arr[2] + 25
note_21 = str(arr[8]) + str(arr[9])
note_22 = str(arr[7]) + str(arr[2])
note_23 = str(arr[0]) + str(arr[4])
tmp_24 = arr[0] + 10
note_25 = str(arr[5]) + str(arr[3])
note_26 = str(arr[0]) + str(arr[2])
tmp_27 = arr[3] + 12
copy_28 = arr[2]
label_29 = "запись 29 не применялась"
note_30 = str(arr[1]) + str(arr[8])
note_31 = str(arr[0]) + str(arr[1])
tmp_32 = arr[5] + 44
code_33 = re.sub(r'[0-9]', '#', str(arr[5]))
note_34 = str(arr[6]) + str(arr[9])
copy_35 = arr[2]
tmp_36 = arr[4] + 21
code_37 = re.sub(r'[0-9]', '#', str(arr[9]))
note_38 = str(arr[1]) + str(arr[1])
label_39 = "запись 39 не применялась"
label_40 = "запись 40 не применялась"
tmp_41 = arr[9] + 31
label_42 = "запись 42 не применялась"
copy_43 = arr[2]
note_44 = str(arr[2]) + str(arr[7])
note_45 = str(arr[1]) + str(arr[0])
tmp_46 = arr[4] + 30
tmp_47 = arr[8] + 42
note_48 = str(arr[6]) + str(arr[4])
code_49 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_50 = arr[6] + 21
note_51 = str(arr[4]) + str(arr[1])
tmp_52 = arr[2] + 23
note_53 = str(arr[8]) + str(arr[2])
tmp_54 = arr[2] + 13
tmp_55 = arr[3] + 31
label_56 = "запись 56 не применялась"
code_57 = re.sub(r'[0-9]', '#', str(arr[9]))
code_58 = re.sub(r'[0-9]', '#', str(arr[5]))
note_59 = str(arr[4]) + str(arr[1])
tmp_60 = arr[5] + 37
tmp_61 = arr[2] + 3
note_62 = str(arr[4]) + str(arr[1])
note_63 = str(arr[6]) + str(arr[8])
copy_64 = arr[8]
copy_65 = arr[5]
tmp_66 = arr[4] + 14
note_67 = str(arr[0]) + str(arr[7])
label_68 = "запись 68 не применялась"
label_69 = "запись 69 не применялась"
note_70 = str(arr[0]) + str(arr[7])
copy_71 = arr[7]
tmp_72 = arr[1] + 15
copy_73 = arr[3]
tmp_74 = arr[6] + 5
copy_75 = arr[7]
label_76 = "запись 76 не применялась"
note_77 = str(arr[1]) + str(arr[4])
note_78 = str(arr[6]) + str(arr[1])
label_79 = "запись 79 не применялась"
note_80 = str(arr[0]) + str(arr[9])
code_81 = re.sub(r'[0-9]', '#', str(arr[7]))
label_82 = "запись 82 не применялась"
tmp_83 = arr[2] + 13
note_84 = str(arr[1]) + str(arr[4])
code_85 = re.sub(r'[0-9]', '#', str(arr[4]))
note_86 = str(arr[6]) + str(arr[5])
copy_87 = arr[4]
label_88 = "запись 88 не применялась"
note_89 = str(arr[0]) + str(arr[6])
code_90 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_91 = arr[9] + 27
tmp_92 = arr[5] + 42
copy_93 = arr[0]
code_94 = re.sub(r'[0-9]', '#', str(arr[1]))
label_95 = "запись 95 не применялась"
note_96 = str(arr[6]) + str(arr[6])
tmp_97 = arr[3] + 7
label_98 = "запись 98 не применялась"
note_99 = str(arr[1]) + str(arr[1])
label_100 = "запись 100 не применялась"
code_101 = re.sub(r'[0-9]', '#', str(arr[8]))
note_102 = str(arr[8]) + str(arr[5])
code_103 = re.sub(r'[0-9]', '#', str(arr[6]))
note_104 = str(arr[4]) + str(arr[3])
note_105 = str(arr[8]) + str(arr[0])
code_106 = re.sub(r'[0-9]', '#', str(arr[9]))
code_107 = re.sub(r'[0-9]', '#', str(arr[6]))
note_108 = str(arr[2]) + str(arr[6])
note_109 = str(arr[7]) + str(arr[5])
code_110 = re.sub(r'[0-9]', '#', str(arr[0]))
code_111 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_112 = arr[9] + 38
tmp_113 = arr[9] + 7
label_114 = "запись 114 не применялась"
code_115 = re.sub(r'[0-9]', '#', str(arr[9]))
code_116 = re.sub(r'[0-9]', '#', str(arr[1]))
note_117 = str(arr[0]) + str(arr[1])
note_118 = str(arr[2]) + str(arr[6])
code_119 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_120 = arr[8] + 23
copy_121 = arr[7]
code_122 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_123 = arr[1]
tmp_124 = arr[2] + 21
note_125 = str(arr[7]) + str(arr[3])
tmp_126 = arr[1] + 20
tmp_127 = arr[5] + 28
code_128 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_129 = arr[5] + 37
note_130 = str(arr[8]) + str(arr[1])
tmp_131 = arr[5] + 34
note_132 = str(arr[3]) + str(arr[9])
code_133 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_134 = arr[4] + 33
label_135 = "запись 135 не применялась"
label_136 = "запись 136 не применялась"
note_137 = str(arr[0]) + str(arr[5])
note_138 = str(arr[6]) + str(arr[5])
tmp_139 = arr[0] + 7
label_140 = "запись 140 не применялась"
note_141 = str(arr[1]) + str(arr[1])
tmp_142 = arr[8] + 31
code_143 = re.sub(r'[0-9]', '#', str(arr[7]))
note_144 = str(arr[1]) + str(arr[8])
copy_145 = arr[6]
tmp_146 = arr[5] + 29
tmp_147 = arr[8] + 28
code_148 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_149 = arr[0] + 32
note_150 = str(arr[8]) + str(arr[8])
copy_151 = arr[8]
tmp_152 = arr[1] + 12
note_153 = str(arr[6]) + str(arr[8])
tmp_154 = arr[4] + 49
copy_155 = arr[6]
tmp_156 = arr[7] + 47
note_157 = str(arr[8]) + str(arr[5])
tmp_158 = arr[3] + 28
label_159 = "запись 159 не применялась"
tmp_160 = arr[7] + 7
copy_161 = arr[6]
note_162 = str(arr[5]) + str(arr[4])
note_163 = str(arr[7]) + str(arr[4])
tmp_164 = arr[3] + 28
tmp_165 = arr[8] + 38
code_166 = re.sub(r'[0-9]', '#', str(arr[4]))
label_167 = "запись 167 не применялась"
note_168 = str(arr[2]) + str(arr[9])
code_169 = re.sub(r'[0-9]', '#', str(arr[9]))
note_170 = str(arr[3]) + str(arr[4])
copy_171 = arr[9]
note_172 = str(arr[2]) + str(arr[6])
copy_173 = arr[6]
note_174 = str(arr[2]) + str(arr[9])
note_175 = str(arr[1]) + str(arr[5])
note_176 = str(arr[4]) + str(arr[5])
tmp_177 = arr[7] + 6
code_178 = re.sub(r'[0-9]', '#', str(arr[3]))
code_179 = re.sub(r'[0-9]', '#', str(arr[8]))
note_180 = str(arr[4]) + str(arr[5])
tmp_181 = arr[6] + 29
copy_182 = arr[3]
tmp_183 = arr[9] + 33
note_184 = str(arr[5]) + str(arr[5])
code_185 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_186 = arr[8] + 44
tmp_187 = arr[6] + 17
copy_188 = arr[3]
tmp_189 = arr[6] + 20
note_190 = str(arr[6]) + str(arr[0])
copy_191 = arr[6]
label_192 = "запись 192 не применялась"
label_193 = "запись 193 не применялась"
code_194 = re.sub(r'[0-9]', '#', str(arr[4]))
label_195 = "запись 195 не применялась"
code_196 = re.sub(r'[0-9]', '#', str(arr[2]))
code_197 = re.sub(r'[0-9]', '#', str(arr[6]))
code_198 = re.sub(r'[0-9]', '#', str(arr[6]))
code_199 = re.sub(r'[0-9]', '#', str(arr[8]))
note_200 = str(arr[8]) + str(arr[0])
copy_201 = arr[5]
tmp_202 = arr[7] + 5
code_203 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_204 = arr[5]
label_205 = "запись 205 не применялась"
note_206 = str(arr[8]) + str(arr[8])
label_207 = "запись 207 не применялась"
label_208 = "запись 208 не применялась"
code_209 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_210 = arr[7] + 4
tmp_211 = arr[4] + 49
copy_212 = arr[0]
note_213 = str(arr[6]) + str(arr[6])
label_214 = "запись 214 не применялась"
label_215 = "запись 215 не применялась"
label_216 = "запись 216 не применялась"
note_217 = str(arr[0]) + str(arr[8])
tmp_218 = arr[0] + 44
tmp_219 = arr[3] + 23
code_220 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_221 = arr[6] + 26
code_222 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_223 = arr[9] + 34
copy_224 = arr[8]
tmp_225 = arr[1] + 37
tmp_226 = arr[7] + 42
copy_227 = arr[4]
tmp_228 = arr[8] + 42
copy_229 = arr[6]
code_230 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_231 = arr[7] + 28
note_232 = str(arr[7]) + str(arr[9])
code_233 = re.sub(r'[0-9]', '#', str(arr[2]))
note_234 = str(arr[3]) + str(arr[8])
copy_235 = arr[5]
note_236 = str(arr[5]) + str(arr[1])
tmp_237 = arr[6] + 12
code_238 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_239 = arr[6] + 25
copy_240 = arr[7]
note_241 = str(arr[1]) + str(arr[6])
copy_242 = arr[9]
tmp_243 = arr[8] + 30
tmp_244 = arr[4] + 28
note_245 = str(arr[0]) + str(arr[4])
code_246 = re.sub(r'[0-9]', '#', str(arr[4]))
note_247 = str(arr[1]) + str(arr[9])
note_248 = str(arr[8]) + str(arr[0])
code_249 = re.sub(r'[0-9]', '#', str(arr[4]))
label_250 = "запись 250 не применялась"
code_251 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_252 = arr[8]
tmp_253 = arr[7] + 25
note_254 = str(arr[3]) + str(arr[9])
label_255 = "запись 255 не применялась"
note_256 = str(arr[4]) + str(arr[3])
label_257 = "запись 257 не применялась"
note_258 = str(arr[7]) + str(arr[2])
code_259 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_260 = arr[5]
tmp_261 = arr[2] + 48
tmp_262 = arr[2] + 26
copy_263 = arr[8]
code_264 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_265 = arr[3] + 16
code_266 = re.sub(r'[0-9]', '#', str(arr[1]))
note_267 = str(arr[1]) + str(arr[9])
note_268 = str(arr[1]) + str(arr[6])
copy_269 = arr[0]
copy_270 = arr[7]
note_271 = str(arr[0]) + str(arr[7])
tmp_272 = arr[8] + 7
code_273 = re.sub(r'[0-9]', '#', str(arr[4]))
code_274 = re.sub(r'[0-9]', '#', str(arr[8]))
note_275 = str(arr[7]) + str(arr[9])
note_276 = str(arr[6]) + str(arr[1])
tmp_277 = arr[5] + 35
tmp_278 = arr[3] + 17
tmp_279 = arr[0] + 11
code_280 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_281 = arr[9] + 21
note_282 = str(arr[3]) + str(arr[4])
code_283 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_284 = arr[9] + 18
note_285 = str(arr[3]) + str(arr[1])
label_286 = "запись 286 не применялась"
note_287 = str(arr[5]) + str(arr[2])
tmp_288 = arr[1] + 15
note_289 = str(arr[2]) + str(arr[2])
code_290 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_291 = arr[2] + 44
note_292 = str(arr[0]) + str(arr[7])
tmp_293 = arr[6] + 30
tmp_294 = arr[7] + 50
tmp_295 = arr[7] + 21
tmp_296 = arr[4] + 47
code_297 = re.sub(r'[0-9]', '#', str(arr[9]))
label_298 = "запись 298 не применялась"
code_299 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_300 = arr[3]
tmp_301 = arr[6] + 4
copy_302 = arr[9]
note_303 = str(arr[7]) + str(arr[7])
label_304 = "запись 304 не применялась"
tmp_305 = arr[1] + 5
label_306 = "запись 306 не применялась"
code_307 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_308 = arr[8] + 38
tmp_309 = arr[8] + 2
code_310 = re.sub(r'[0-9]', '#', str(arr[4]))
code_311 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_312 = arr[6] + 22
note_313 = str(arr[3]) + str(arr[2])
tmp_314 = arr[6] + 23
label_315 = "запись 315 не применялась"
tmp_316 = arr[6] + 30
note_317 = str(arr[2]) + str(arr[5])
copy_318 = arr[7]
code_319 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_320 = arr[9] + 9
tmp_321 = arr[5] + 27
code_322 = re.sub(r'[0-9]', '#', str(arr[7]))
note_323 = str(arr[3]) + str(arr[1])
tmp_324 = arr[2] + 38
note_325 = str(arr[1]) + str(arr[7])
note_326 = str(arr[9]) + str(arr[5])
copy_327 = arr[5]
label_328 = "запись 328 не применялась"
code_329 = re.sub(r'[0-9]', '#', str(arr[4]))
label_330 = "запись 330 не применялась"
copy_331 = arr[1]
note_332 = str(arr[2]) + str(arr[2])
tmp_333 = arr[3] + 13
label_334 = "запись 334 не применялась"
copy_335 = arr[3]
note_336 = str(arr[5]) + str(arr[8])
note_337 = str(arr[3]) + str(arr[8])
code_338 = re.sub(r'[0-9]', '#', str(arr[1]))
note_339 = str(arr[8]) + str(arr[1])
tmp_340 = arr[5] + 11
tmp_341 = arr[9] + 40
note_342 = str(arr[0]) + str(arr[5])
copy_343 = arr[8]
note_344 = str(arr[6]) + str(arr[9])
tmp_345 = arr[9] + 44
label_346 = "запись 346 не применялась"
tmp_347 = arr[9] + 19
copy_348 = arr[2]
tmp_349 = arr[9] + 37
tmp_350 = arr[4] + 38
tmp_351 = arr[2] + 17
copy_352 = arr[1]
note_353 = str(arr[1]) + str(arr[0])
tmp_354 = arr[0] + 37
tmp_355 = arr[8] + 3
code_356 = re.sub(r'[0-9]', '#', str(arr[9]))
code_357 = re.sub(r'[0-9]', '#', str(arr[3]))
code_358 = re.sub(r'[0-9]', '#', str(arr[8]))
note_359 = str(arr[9]) + str(arr[8])
note_360 = str(arr[9]) + str(arr[6])
label_361 = "запись 361 не применялась"
note_362 = str(arr[1]) + str(arr[8])
copy_363 = arr[0]
tmp_364 = arr[9] + 30
note_365 = str(arr[1]) + str(arr[3])
note_366 = str(arr[4]) + str(arr[4])
note_367 = str(arr[8]) + str(arr[1])
copy_368 = arr[5]
note_369 = str(arr[7]) + str(arr[1])
copy_370 = arr[5]
code_371 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_372 = arr[3]
note_373 = str(arr[9]) + str(arr[3])
tmp_374 = arr[3] + 10
note_375 = str(arr[9]) + str(arr[1])
tmp_376 = arr[3] + 20
code_377 = re.sub(r'[0-9]', '#', str(arr[2]))
code_378 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_379 = arr[5] + 45
label_380 = "запись 380 не применялась"
tmp_381 = arr[9] + 29
tmp_382 = arr[9] + 48
copy_383 = arr[6]
label_384 = "запись 384 не применялась"
note_385 = str(arr[5]) + str(arr[2])
copy_386 = arr[0]
copy_387 = arr[8]
note_388 = str(arr[6]) + str(arr[1])
copy_389 = arr[9]
note_390 = str(arr[4]) + str(arr[7])
label_391 = "запись 391 не применялась"
tmp_392 = arr[0] + 7
note_393 = str(arr[8]) + str(arr[6])
code_394 = re.sub(r'[0-9]', '#', str(arr[8]))
note_395 = str(arr[9]) + str(arr[8])
code_396 = re.sub(r'[0-9]', '#', str(arr[1]))
code_397 = re.sub(r'[0-9]', '#', str(arr[1]))
label_398 = "запись 398 не применялась"
note_399 = str(arr[5]) + str(arr[0])
tmp_400 = arr[3] + 35
code_401 = re.sub(r'[0-9]', '#', str(arr[4]))
note_402 = str(arr[4]) + str(arr[1])
note_403 = str(arr[6]) + str(arr[1])
copy_404 = arr[1]
code_405 = re.sub(r'[0-9]', '#', str(arr[1]))
note_406 = str(arr[2]) + str(arr[7])
note_407 = str(arr[9]) + str(arr[5])
label_408 = "запись 408 не применялась"
tmp_409 = arr[9] + 4
tmp_410 = arr[2] + 22
code_411 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_412 = arr[5]
code_413 = re.sub(r'[0-9]', '#', str(arr[8]))
code_414 = re.sub(r'[0-9]', '#', str(arr[1]))
note_415 = str(arr[0]) + str(arr[0])
code_416 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_417 = arr[5]
tmp_418 = arr[2] + 49
note_419 = str(arr[3]) + str(arr[6])
tmp_420 = arr[3] + 43
note_421 = str(arr[7]) + str(arr[4])
tmp_422 = arr[8] + 22
tmp_423 = arr[8] + 42
tmp_424 = arr[4] + 14
code_425 = re.sub(r'[0-9]', '#', str(arr[6]))
note_426 = str(arr[7]) + str(arr[4])
note_427 = str(arr[2]) + str(arr[0])
note_428 = str(arr[5]) + str(arr[6])
note_429 = str(arr[9]) + str(arr[9])
label_430 = "запись 430 не применялась"
code_431 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_432 = arr[8]
label_433 = "запись 433 не применялась"
note_434 = str(arr[2]) + str(arr[5])
tmp_435 = arr[2] + 2
label_436 = "запись 436 не применялась"
copy_437 = arr[0]
note_438 = str(arr[6]) + str(arr[1])
note_439 = str(arr[6]) + str(arr[2])
label_440 = "запись 440 не применялась"
tmp_441 = arr[8] + 17
tmp_442 = arr[6] + 3
note_443 = str(arr[4]) + str(arr[3])
code_444 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_445 = arr[9] + 8
note_446 = str(arr[2]) + str(arr[0])
code_447 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_448 = arr[6] + 26
code_449 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_450 = arr[1] + 41
note_451 = str(arr[7]) + str(arr[8])
label_452 = "запись 452 не применялась"
code_453 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_454 = arr[9] + 49
code_455 = re.sub(r'[0-9]', '#', str(arr[8]))
note_456 = str(arr[3]) + str(arr[4])
tmp_457 = arr[6] + 23
copy_458 = arr[3]
tmp_459 = arr[7] + 49
label_460 = "запись 460 не применялась"
note_461 = str(arr[3]) + str(arr[2])
label_462 = "запись 462 не применялась"
code_463 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_464 = arr[0] + 22
tmp_465 = arr[5] + 12
label_466 = "запись 466 не применялась"
code_467 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_468 = arr[6] + 17
tmp_469 = arr[2] + 33
code_470 = re.sub(r'[0-9]', '#', str(arr[9]))
note_471 = str(arr[0]) + str(arr[7])
tmp_472 = arr[5] + 4
note_473 = str(arr[6]) + str(arr[1])
note_474 = str(arr[2]) + str(arr[7])
code_475 = re.sub(r'[0-9]', '#', str(arr[2]))
note_476 = str(arr[7]) + str(arr[7])
note_477 = str(arr[6]) + str(arr[3])
tmp_478 = arr[9] + 34
tmp_479 = arr[3] + 48
copy_480 = arr[8]
code_481 = re.sub(r'[0-9]', '#', str(arr[3]))
label_482 = "запись 482 не применялась"
label_483 = "запись 483 не применялась"
note_484 = str(arr[7]) + str(arr[3])
copy_485 = arr[2]
code_486 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_487 = arr[5] + 11
code_488 = re.sub(r'[0-9]', '#', str(arr[3]))
note_489 = str(arr[4]) + str(arr[6])
note_490 = str(arr[4]) + str(arr[8])
code_491 = re.sub(r'[0-9]', '#', str(arr[0]))
code_492 = re.sub(r'[0-9]', '#', str(arr[1]))
note_493 = str(arr[3]) + str(arr[5])
label_494 = "запись 494 не применялась"
copy_495 = arr[8]
code_496 = re.sub(r'[0-9]', '#', str(arr[3]))
note_497 = str(arr[7]) + str(arr[2])
note_498 = str(arr[4]) + str(arr[4])
copy_499 = arr[0]
code_500 = re.sub(r'[0-9]', '#', str(arr[9]))
label_501 = "запись 501 не применялась"
tmp_502 = arr[5] + 11
label_503 = "запись 503 не применялась"
copy_504 = arr[2]
code_505 = re.sub(r'[0-9]', '#', str(arr[8]))
code_506 = re.sub(r'[0-9]', '#', str(arr[8]))
label_507 = "запись 507 не применялась"
note_508 = str(arr[7]) + str(arr[4])
code_509 = re.sub(r'[0-9]', '#', str(arr[6]))
note_510 = str(arr[7]) + str(arr[6])
label_511 = "запись 511 не применялась"
code_512 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_513 = arr[4]
tmp_514 = arr[8] + 1
label_515 = "запись 515 не применялась"
note_516 = str(arr[9]) + str(arr[3])
tmp_517 = arr[0] + 8
label_518 = "запись 518 не применялась"
tmp_519 = arr[5] + 41
tmp_520 = arr[5] + 27
tmp_521 = arr[0] + 4
label_522 = "запись 522 не применялась"
note_523 = str(arr[2]) + str(arr[7])
tmp_524 = arr[4] + 2
label_525 = "запись 525 не применялась"
note_526 = str(arr[4]) + str(arr[5])
label_527 = "запись 527 не применялась"
tmp_528 = arr[3] + 9
tmp_529 = arr[8] + 25
note_530 = str(arr[9]) + str(arr[5])
note_531 = str(arr[6]) + str(arr[6])
copy_532 = arr[6]
tmp_533 = arr[7] + 18
note_534 = str(arr[1]) + str(arr[3])
note_535 = str(arr[3]) + str(arr[0])
tmp_536 = arr[0] + 40
note_537 = str(arr[1]) + str(arr[6])
label_538 = "запись 538 не применялась"
tmp_539 = arr[8] + 44
tmp_540 = arr[9] + 20
tmp_541 = arr[3] + 43
tmp_542 = arr[9] + 2
copy_543 = arr[8]
tmp_544 = arr[3] + 12
label_545 = "запись 545 не применялась"
tmp_546 = arr[9] + 48
note_547 = str(arr[8]) + str(arr[4])
tmp_548 = arr[5] + 13
note_549 = str(arr[9]) + str(arr[5])
label_550 = "запись 550 не применялась"
note_551 = str(arr[6]) + str(arr[0])
tmp_552 = arr[5] + 41
tmp_553 = arr[8] + 50
code_554 = re.sub(r'[0-9]', '#', str(arr[7]))
note_555 = str(arr[8]) + str(arr[2])
label_556 = "запись 556 не применялась"
tmp_557 = arr[0] + 47
tmp_558 = arr[6] + 21
tmp_559 = arr[0] + 25
tmp_560 = arr[5] + 22
note_561 = str(arr[9]) + str(arr[8])
note_562 = str(arr[0]) + str(arr[0])
tmp_563 = arr[0] + 42
tmp_564 = arr[8] + 25
tmp_565 = arr[8] + 24
tmp_566 = arr[1] + 32
note_567 = str(arr[6]) + str(arr[2])
code_568 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_569 = arr[5] + 28
note_570 = str(arr[6]) + str(arr[2])
tmp_571 = arr[3] + 31
tmp_572 = arr[9] + 30
copy_573 = arr[6]
code_574 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_575 = arr[1]
note_576 = str(arr[7]) + str(arr[6])
code_577 = re.sub(r'[0-9]', '#', str(arr[2]))
code_578 = re.sub(r'[0-9]', '#', str(arr[0]))
code_579 = re.sub(r'[0-9]', '#', str(arr[3]))
note_580 = str(arr[2]) + str(arr[3])
tmp_581 = arr[5] + 26
tmp_582 = arr[4] + 39
tmp_583 = arr[1] + 50
code_584 = re.sub(r'[0-9]', '#', str(arr[8]))
note_585 = str(arr[9]) + str(arr[1])
tmp_586 = arr[5] + 9
tmp_587 = arr[7] + 37
note_588 = str(arr[2]) + str(arr[3])
copy_589 = arr[4]
code_590 = re.sub(r'[0-9]', '#', str(arr[2]))
code_591 = re.sub(r'[0-9]', '#', str(arr[0]))
note_592 = str(arr[2]) + str(arr[0])
note_593 = str(arr[0]) + str(arr[5])
tmp_594 = arr[2] + 50
code_595 = re.sub(r'[0-9]', '#', str(arr[5]))
code_596 = re.sub(r'[0-9]', '#', str(arr[9]))
label_597 = "запись 597 не применялась"
copy_598 = arr[7]
copy_599 = arr[1]
tmp_600 = arr[6] + 46
code_601 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_602 = arr[9] + 35
note_603 = str(arr[6]) + str(arr[3])
code_604 = re.sub(r'[0-9]', '#', str(arr[3]))
code_605 = re.sub(r'[0-9]', '#', str(arr[5]))
label_606 = "запись 606 не применялась"
tmp_607 = arr[2] + 33
tmp_608 = arr[7] + 35
note_609 = str(arr[3]) + str(arr[8])
note_610 = str(arr[4]) + str(arr[8])
copy_611 = arr[6]
tmp_612 = arr[6] + 11
code_613 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_614 = arr[5] + 14
note_615 = str(arr[5]) + str(arr[3])
note_616 = str(arr[1]) + str(arr[5])
note_617 = str(arr[5]) + str(arr[8])
copy_618 = arr[5]
code_619 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_620 = arr[9]
note_621 = str(arr[0]) + str(arr[8])
copy_622 = arr[3]
code_623 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_624 = arr[5] + 44
tmp_625 = arr[8] + 7
label_626 = "запись 626 не применялась"
note_627 = str(arr[0]) + str(arr[0])
tmp_628 = arr[9] + 46
note_629 = str(arr[5]) + str(arr[8])
copy_630 = arr[5]
copy_631 = arr[2]
tmp_632 = arr[9] + 19
label_633 = "запись 633 не применялась"
tmp_634 = arr[7] + 35
tmp_635 = arr[9] + 43
tmp_636 = arr[5] + 22
label_637 = "запись 637 не применялась"
note_638 = str(arr[8]) + str(arr[8])
tmp_639 = arr[1] + 3
copy_640 = arr[6]
code_641 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_642 = arr[4]
copy_643 = arr[3]
tmp_644 = arr[6] + 43
tmp_645 = arr[4] + 40
code_646 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_647 = arr[4]
copy_648 = arr[4]
code_649 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_650 = arr[6]
tmp_651 = arr[2] + 4
label_652 = "запись 652 не применялась"
tmp_653 = arr[3] + 50
code_654 = re.sub(r'[0-9]', '#', str(arr[0]))
note_655 = str(arr[1]) + str(arr[6])
code_656 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_657 = arr[6] + 9
note_658 = str(arr[1]) + str(arr[3])
note_659 = str(arr[0]) + str(arr[0])
tmp_660 = arr[0] + 5
note_661 = str(arr[7]) + str(arr[9])
tmp_662 = arr[9] + 7
tmp_663 = arr[8] + 35
label_664 = "запись 664 не применялась"
label_665 = "запись 665 не применялась"
code_666 = re.sub(r'[0-9]', '#', str(arr[9]))
note_667 = str(arr[4]) + str(arr[8])
code_668 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_669 = arr[0] + 20
label_670 = "запись 670 не применялась"
copy_671 = arr[1]
note_672 = str(arr[9]) + str(arr[2])
note_673 = str(arr[4]) + str(arr[5])
tmp_674 = arr[3] + 22
note_675 = str(arr[0]) + str(arr[6])
note_676 = str(arr[4]) + str(arr[2])
label_677 = "запись 677 не применялась"
tmp_678 = arr[0] + 5
code_679 = re.sub(r'[0-9]', '#', str(arr[8]))
note_680 = str(arr[8]) + str(arr[4])
note_681 = str(arr[1]) + str(arr[1])
code_682 = re.sub(r'[0-9]', '#', str(arr[2]))
note_683 = str(arr[2]) + str(arr[5])
tmp_684 = arr[2] + 26
tmp_685 = arr[9] + 39
label_686 = "запись 686 не применялась"
note_687 = str(arr[3]) + str(arr[8])
tmp_688 = arr[5] + 24
copy_689 = arr[7]
note_690 = str(arr[2]) + str(arr[9])
tmp_691 = arr[1] + 13
note_692 = str(arr[5]) + str(arr[2])
copy_693 = arr[3]
note_694 = str(arr[9]) + str(arr[3])
tmp_695 = arr[1] + 24
note_696 = str(arr[6]) + str(arr[8])
tmp_697 = arr[9] + 43
code_698 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_699 = arr[4] + 36
copy_700 = arr[7]
code_701 = re.sub(r'[0-9]', '#', str(arr[9]))
code_702 = re.sub(r'[0-9]', '#', str(arr[4]))
code_703 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_704 = arr[9] + 4
label_705 = "запись 705 не применялась"
tmp_706 = arr[1] + 2
copy_707 = arr[7]
code_708 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_709 = arr[1]
tmp_710 = arr[0] + 9
note_711 = str(arr[3]) + str(arr[5])
tmp_712 = arr[6] + 41
code_713 = re.sub(r'[0-9]', '#', str(arr[4]))
note_714 = str(arr[9]) + str(arr[5])
note_715 = str(arr[6]) + str(arr[9])
tmp_716 = arr[7] + 11
tmp_717 = arr[5] + 16
code_718 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_719 = arr[3] + 17
tmp_720 = arr[3] + 37
label_721 = "запись 721 не применялась"
note_722 = str(arr[1]) + str(arr[8])
label_723 = "запись 723 не применялась"
note_724 = str(arr[9]) + str(arr[0])
tmp_725 = arr[0] + 38
copy_726 = arr[3]
tmp_727 = arr[9] + 20
code_728 = re.sub(r'[0-9]', '#', str(arr[7]))
code_729 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_730 = arr[0]
note_731 = str(arr[1]) + str(arr[3])
code_732 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_733 = arr[8] + 2
code_734 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_735 = arr[3] + 43
label_736 = "запись 736 не применялась"
code_737 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_738 = arr[5] + 6
label_739 = "запись 739 не применялась"
tmp_740 = arr[3] + 40
tmp_741 = arr[8] + 27
note_742 = str(arr[0]) + str(arr[9])
note_743 = str(arr[5]) + str(arr[3])
tmp_744 = arr[5] + 44
label_745 = "запись 745 не применялась"
note_746 = str(arr[0]) + str(arr[4])
label_747 = "запись 747 не применялась"
copy_748 = arr[5]
note_749 = str(arr[3]) + str(arr[1])
tmp_750 = arr[3] + 2
copy_751 = arr[2]
copy_752 = arr[3]
copy_753 = arr[8]
note_754 = str(arr[8]) + str(arr[6])
code_755 = re.sub(r'[0-9]', '#', str(arr[7]))
code_756 = re.sub(r'[0-9]', '#', str(arr[5]))
label_757 = "запись 757 не применялась"
copy_758 = arr[8]
note_759 = str(arr[3]) + str(arr[8])
tmp_760 = arr[9] + 39
copy_761 = arr[2]
code_762 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_763 = arr[0] + 3
tmp_764 = arr[7] + 33
tmp_765 = arr[3] + 5
note_766 = str(arr[9]) + str(arr[7])
note_767 = str(arr[0]) + str(arr[4])
note_768 = str(arr[7]) + str(arr[0])
copy_769 = arr[0]
note_770 = str(arr[2]) + str(arr[5])
note_771 = str(arr[6]) + str(arr[4])
label_772 = "запись 772 не применялась"
copy_773 = arr[1]
tmp_774 = arr[3] + 7
copy_775 = arr[5]
tmp_776 = arr[8] + 42
note_777 = str(arr[0]) + str(arr[2])
label_778 = "запись 778 не применялась"
label_779 = "запись 779 не применялась"
code_780 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_781 = arr[3] + 32
label_782 = "запись 782 не применялась"
note_783 = str(arr[4]) + str(arr[5])
copy_784 = arr[8]
code_785 = re.sub(r'[0-9]', '#', str(arr[1]))
code_786 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_787 = arr[8]
copy_788 = arr[5]
copy_789 = arr[1]
note_790 = str(arr[2]) + str(arr[0])
note_791 = str(arr[1]) + str(arr[4])
code_792 = re.sub(r'[0-9]', '#', str(arr[0]))
code_793 = re.sub(r'[0-9]', '#', str(arr[8]))
note_794 = str(arr[4]) + str(arr[9])
note_795 = str(arr[6]) + str(arr[1])
note_796 = str(arr[6]) + str(arr[8])
label_797 = "запись 797 не применялась"
tmp_798 = arr[1] + 10
tmp_799 = arr[9] + 9

t109 = str(arr[7]) + str(arr[4])
# примечание: запись 666 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[7] = 50 — не выполняется
# временная запись: запись 101 обработана, изменений нет
# ревизия: запись 338 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# архив: запись 610 обработана, изменений нет
# замечание: запись 335 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# отладка: запись 465 обработана, изменений нет
# черновик: arr[7] += 24 — не выполняется
# ревизия: arr2[3] = 97 — не выполняется
# архив: запись 478 обработана, изменений нет
# архив: arr[4] *= 56 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[0] *= 35 — не выполняется
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: запись 178 обработана, изменений нет
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr2[8] = 33 — не выполняется
# пометка: arr2[0] = 82 — не выполняется
# отладка: запись 428 обработана, изменений нет
# примечание: arr2[7] = 75 — не выполняется
# ревизия: запись 700 обработана, изменений нет
# черновик: arr[3] *= 41 — не выполняется
# черновик: arr[5] = 39 — не выполняется
# отладка: запись 265 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# пометка: arr2[4] = 12 — не выполняется
# отладка: запись 556 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[2] *= 6 — не выполняется
# архив: запись 394 обработана, изменений нет
# черновик: arr[6] *= 33 — не выполняется
# архив: arr[5] *= 14 — не выполняется
# отладка: arr2[3] = 48 — не выполняется
# замечание: arr[8] = 79 — не выполняется
# черновик: arr[7] *= 99 — не выполняется
# примечание: запись 793 обработана, изменений нет
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[2] *= 9 — не выполняется
# справка: запись 685 обработана, изменений нет
# временная запись: arr[1] += 51 — не выполняется
# архив: запись 502 обработана, изменений нет
# черновик: arr[2] *= 21 — не выполняется
# архив: arr[3] *= 3 — не выполняется
# пометка: arr2[1] = 20 — не выполняется
# временная запись: arr[3] = 20 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: запись 29 обработана, изменений нет
# черновик: arr[0] *= 8 — не выполняется
# отладка: arr[4] *= 99 — не выполняется
# справка: arr[8] += 63 — не выполняется
# проверено: arr[1] = 67 — не выполняется
# замечание: arr[7] += 18 — не выполняется
# временная запись: arr[8] *= 5 — не выполняется
# проверено: запись 138 обработана, изменений нет
# отладка: arr2[9] = 18 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: arr[2] += 53 — не выполняется
# временная запись: запись 782 обработана, изменений нет
# замечание: arr[3] *= 37 — не выполняется
# архив: запись 121 обработана, изменений нет
# примечание: запись 824 обработана, изменений нет
# ревизия: запись 456 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# справка: запись 638 обработана, изменений нет
# пометка: arr[6] *= 62 — не выполняется
# пометка: запись 326 обработана, изменений нет
# черновик: arr[8] *= 20 — не выполняется
# отладка: запись 496 обработана, изменений нет
# архив: arr[6] += 76 — не выполняется
# архив: arr2[2] = 28 — не выполняется
# пометка: запись 825 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# ревизия: arr[5] = 33 — не выполняется
# пометка: arr[6] = 46 — не выполняется
# отладка: запись 490 обработана, изменений нет
# замечание: запись 530 обработана, изменений нет
# пометка: запись 920 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: arr2[2] = 94 — не выполняется
# черновик: запись 507 обработана, изменений нет
# отладка: запись 189 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# архив: запись 746 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 838 обработана, изменений нет
# черновик: запись 633 обработана, изменений нет
# проверено: запись 217 обработана, изменений нет
# отладка: arr[4] = 36 — не выполняется
# пометка: запись 754 обработана, изменений нет
# черновик: запись 769 обработана, изменений нет
# пометка: запись 270 обработана, изменений нет
# пометка: arr2[6] = 89 — не выполняется
# ревизия: arr2[9] = 45 — не выполняется
# примечание: arr[3] += 15 — не выполняется
# проверено: arr[1] = 14 — не выполняется
# примечание: запись 127 обработана, изменений нет
# примечание: arr2[1] = 27 — не выполняется
# ревизия: запись 253 обработана, изменений нет
# ревизия: arr[7] = 63 — не выполняется
# справка: запись 579 обработана, изменений нет
# пометка: arr[5] *= 19 — не выполняется
# архив: запись 79 обработана, изменений нет
# отладка: запись 793 обработана, изменений нет
# архив: запись 452 обработана, изменений нет
# временная запись: запись 897 обработана, изменений нет
# пометка: arr[4] *= 66 — не выполняется
# черновик: arr[9] += 21 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr2[3] = 51 — не выполняется
# замечание: запись 834 обработана, изменений нет
# проверено: arr[9] += 10 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# пометка: arr2[4] = 88 — не выполняется
# справка: arr[7] += 57 — не выполняется
# замечание: arr2[4] = 9 — не выполняется
# отладка: запись 141 обработана, изменений нет
# проверено: запись 214 обработана, изменений нет
# справка: запись 245 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: запись 98 обработана, изменений нет
# замечание: arr[3] = 27 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 122 обработана, изменений нет
# временная запись: arr[8] = 44 — не выполняется
# черновик: arr2[5] = 3 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr2[3] = 79 — не выполняется
# архив: запись 585 обработана, изменений нет
# черновик: arr[5] *= 33 — не выполняется
# временная запись: запись 665 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 869 обработана, изменений нет
# временная запись: запись 24 обработана, изменений нет
# проверено: arr[8] = 46 — не выполняется
# замечание: arr[7] += 1 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 244 обработана, изменений нет
# пометка: запись 59 обработана, изменений нет
# пометка: arr2[4] = 20 — не выполняется
# замечание: arr[9] += 69 — не выполняется
# пометка: запись 951 обработана, изменений нет
# проверено: arr[4] *= 55 — не выполняется
# примечание: запись 880 обработана, изменений нет
# справка: arr2[4] = 58 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 743 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: запись 537 обработана, изменений нет
# ревизия: arr[6] *= 85 — не выполняется
# пометка: запись 181 обработана, изменений нет
# проверено: запись 629 обработана, изменений нет
# архив: arr[0] *= 84 — не выполняется
# ревизия: запись 944 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# архив: arr[1] *= 50 — не выполняется
# отладка: запись 233 обработана, изменений нет
# замечание: запись 839 обработана, изменений нет
# ревизия: arr[8] = 68 — не выполняется
# проверено: arr[6] *= 64 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr2[5] = 33 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[2] *= 82 — не выполняется
# пометка: запись 23 обработана, изменений нет
# примечание: arr2[5] = 62 — не выполняется
# ревизия: arr2[3] = 44 — не выполняется
# справка: arr2[9] = 42 — не выполняется
# черновик: запись 124 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# примечание: запись 433 обработана, изменений нет
# пометка: arr[5] = 70 — не выполняется
# ревизия: запись 882 обработана, изменений нет
# пометка: arr[2] = 91 — не выполняется
# архив: запись 976 обработана, изменений нет
# примечание: запись 775 обработана, изменений нет
# пометка: запись 630 обработана, изменений нет
# отладка: arr[9] *= 19 — не выполняется
# справка: arr[1] = 97 — не выполняется
# временная запись: arr2[0] = 71 — не выполняется
# проверено: запись 81 обработана, изменений нет
# справка: arr[7] *= 13 — не выполняется
# замечание: arr[5] = 91 — не выполняется
# отладка: arr[8] = 75 — не выполняется
# примечание: arr[3] += 29 — не выполняется
# отладка: запись 626 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 295 обработана, изменений нет
# пометка: arr[1] = 46 — не выполняется
# примечание: запись 972 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[9] += 15 — не выполняется
# отладка: arr[5] *= 3 — не выполняется
# примечание: arr[0] = 95 — не выполняется
# пометка: запись 970 обработана, изменений нет
# замечание: запись 967 обработана, изменений нет
# проверено: запись 234 обработана, изменений нет
# замечание: arr[7] = 37 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[5] += 81 — не выполняется
# архив: запись 211 обработана, изменений нет
# замечание: arr[0] = 22 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# временная запись: arr[6] = 94 — не выполняется
# ревизия: arr2[1] = 26 — не выполняется
# ревизия: arr[5] += 28 — не выполняется
# замечание: запись 856 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# проверено: запись 586 обработана, изменений нет
# примечание: arr[5] += 36 — не выполняется
# замечание: запись 245 обработана, изменений нет
# примечание: запись 862 обработана, изменений нет
# пометка: arr[4] += 56 — не выполняется
# замечание: arr[7] *= 38 — не выполняется
# замечание: arr[7] = 47 — не выполняется
# проверено: arr2[4] = 44 — не выполняется
# примечание: arr[0] *= 3 — не выполняется
# ревизия: arr[8] *= 34 — не выполняется
# справка: arr[9] = 91 — не выполняется
# архив: arr[3] += 22 — не выполняется
# примечание: запись 185 обработана, изменений нет
# архив: запись 445 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[2] = 54 — не выполняется
# архив: arr[8] += 31 — не выполняется
# отладка: запись 781 обработана, изменений нет
# отладка: запись 387 обработана, изменений нет
# замечание: arr[1] = 81 — не выполняется
# отладка: запись 235 обработана, изменений нет
# временная запись: запись 327 обработана, изменений нет
# справка: arr[0] = 99 — не выполняется
# ревизия: arr[7] = 51 — не выполняется
# архив: arr2[5] = 93 — не выполняется
# черновик: arr2[2] = 81 — не выполняется
# проверено: запись 600 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# пометка: запись 359 обработана, изменений нет
# замечание: arr[4] *= 55 — не выполняется
# пометка: arr[9] *= 48 — не выполняется
# замечание: arr[1] += 25 — не выполняется
# отладка: arr[0] = 46 — не выполняется
# отладка: arr[9] *= 26 — не выполняется
# замечание: arr2[3] = 69 — не выполняется
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[2] += 32 — не выполняется
# отладка: запись 957 обработана, изменений нет
arr[0] = int(t109) % 97
# проверено: запись 937 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# примечание: arr[5] = 17 — не выполняется
# примечание: arr[5] += 57 — не выполняется
# ревизия: arr2[9] = 76 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# временная запись: запись 487 обработана, изменений нет
# временная запись: arr[9] *= 4 — не выполняется
# отладка: запись 19 обработана, изменений нет
# черновик: arr[2] += 90 — не выполняется
# архив: запись 79 обработана, изменений нет
# архив: arr2[0] = 53 — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[2] *= 4 — не выполняется
# пометка: arr[8] *= 90 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# примечание: arr[8] += 25 — не выполняется
# отладка: arr2[1] = 74 — не выполняется
# черновик: запись 217 обработана, изменений нет
# временная запись: arr[7] += 34 — не выполняется
# проверено: запись 324 обработана, изменений нет
# ревизия: arr[3] += 8 — не выполняется
# справка: arr[4] *= 47 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr[1] = 25 — не выполняется
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: запись 605 обработана, изменений нет
# ревизия: запись 959 обработана, изменений нет
# пометка: запись 666 обработана, изменений нет
# отладка: запись 694 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 696 обработана, изменений нет
# проверено: arr[8] *= 44 — не выполняется
# справка: arr[5] *= 58 — не выполняется
# черновик: запись 570 обработана, изменений нет
# архив: запись 181 обработана, изменений нет
# черновик: arr[8] = 5 — не выполняется
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr2[5] = 54 — не выполняется
# замечание: запись 150 обработана, изменений нет
# ревизия: запись 876 обработана, изменений нет
# пометка: arr[1] *= 16 — не выполняется
# замечание: запись 468 обработана, изменений нет
# проверено: запись 755 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr2[2] = 34 — не выполняется
# пометка: arr[9] *= 40 — не выполняется
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: запись 14 обработана, изменений нет
# архив: запись 285 обработана, изменений нет
# черновик: arr[4] *= 62 — не выполняется
# временная запись: arr[5] += 82 — не выполняется
# проверено: arr[1] *= 86 — не выполняется
# справка: arr[4] = 45 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[4] = 83 — не выполняется
# замечание: запись 387 обработана, изменений нет
# проверено: запись 601 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# черновик: arr[7] *= 7 — не выполняется
# пометка: arr[2] = 17 — не выполняется
# черновик: запись 289 обработана, изменений нет
# ревизия: arr2[6] = 79 — не выполняется
# примечание: arr[7] += 83 — не выполняется
# архив: arr[9] = 6 — не выполняется
# проверено: arr[6] *= 53 — не выполняется
# ревизия: arr[6] = 67 — не выполняется
# замечание: arr[7] *= 23 — не выполняется
# отладка: запись 595 обработана, изменений нет
# отладка: запись 666 обработана, изменений нет
# пометка: запись 567 обработана, изменений нет
# временная запись: запись 96 обработана, изменений нет
# замечание: arr2[9] = 8 — не выполняется
# примечание: arr2[2] = 96 — не выполняется
# справка: arr[5] *= 38 — не выполняется
# архив: arr[6] = 11 — не выполняется
# временная запись: arr[7] += 57 — не выполняется
# проверено: запись 68 обработана, изменений нет
# черновик: arr[1] *= 28 — не выполняется
# справка: arr2[6] = 4 — не выполняется
# черновик: arr[9] += 60 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr2[7] = 48 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 758 обработана, изменений нет
# проверено: arr2[4] = 29 — не выполняется
# проверено: arr2[2] = 90 — не выполняется
# архив: запись 539 обработана, изменений нет
# архив: запись 617 обработана, изменений нет
# архив: запись 280 обработана, изменений нет
# архив: arr[9] = 61 — не выполняется
# проверено: запись 450 обработана, изменений нет
# замечание: arr[6] = 82 — не выполняется
# временная запись: arr[5] = 40 — не выполняется
# примечание: arr[2] *= 29 — не выполняется
# черновик: arr[6] += 37 — не выполняется
# временная запись: запись 567 обработана, изменений нет
# архив: запись 466 обработана, изменений нет
# справка: arr2[4] = 72 — не выполняется
# черновик: запись 127 обработана, изменений нет
# ревизия: arr[6] = 53 — не выполняется
# примечание: запись 341 обработана, изменений нет
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 490 обработана, изменений нет
# замечание: arr[5] += 28 — не выполняется
# замечание: запись 844 обработана, изменений нет
# черновик: arr2[5] = 4 — не выполняется
# справка: запись 549 обработана, изменений нет
# ревизия: arr[6] += 36 — не выполняется
# архив: запись 274 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# замечание: запись 379 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# примечание: запись 350 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 740 обработана, изменений нет
# замечание: arr[5] *= 2 — не выполняется
# замечание: arr[8] = 33 — не выполняется
# временная запись: arr[8] *= 32 — не выполняется
# ревизия: arr[6] = 48 — не выполняется
# замечание: запись 613 обработана, изменений нет
# архив: arr[0] += 69 — не выполняется
# пометка: запись 495 обработана, изменений нет
# отладка: arr[5] += 51 — не выполняется
# черновик: arr2[2] = 29 — не выполняется
# отладка: запись 220 обработана, изменений нет
# архив: запись 913 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 412 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 837 обработана, изменений нет
# примечание: arr[4] += 21 — не выполняется
# черновик: arr[3] += 83 — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[6] = 29 — не выполняется
# справка: запись 890 обработана, изменений нет
# черновик: запись 769 обработана, изменений нет
# отладка: запись 624 обработана, изменений нет
# замечание: arr[2] += 41 — не выполняется
# замечание: запись 305 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# отладка: запись 440 обработана, изменений нет
# черновик: arr[5] = 38 — не выполняется
# примечание: запись 397 обработана, изменений нет
# черновик: arr[2] = 73 — не выполняется
# справка: arr[2] = 91 — не выполняется
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: запись 995 обработана, изменений нет
# отладка: arr[4] += 71 — не выполняется
# ревизия: arr[4] += 66 — не выполняется
# справка: arr[5] = 86 — не выполняется
# архив: запись 35 обработана, изменений нет
# архив: запись 786 обработана, изменений нет
# справка: arr[8] *= 20 — не выполняется
# архив: запись 396 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# черновик: arr[7] += 81 — не выполняется
# временная запись: запись 549 обработана, изменений нет
# проверено: запись 934 обработана, изменений нет
# архив: arr2[9] = 5 — не выполняется
# отладка: arr[6] = 30 — не выполняется
# справка: arr[3] += 66 — не выполняется
# временная запись: arr[2] *= 49 — не выполняется
# проверено: arr[8] += 6 — не выполняется
# временная запись: запись 425 обработана, изменений нет
# примечание: запись 286 обработана, изменений нет
# архив: arr[9] += 84 — не выполняется
# проверено: запись 719 обработана, изменений нет
# пометка: запись 907 обработана, изменений нет
# справка: arr[9] += 55 — не выполняется
# замечание: запись 257 обработана, изменений нет
# временная запись: запись 745 обработана, изменений нет
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: запись 895 обработана, изменений нет
# пометка: arr[9] *= 73 — не выполняется
# отладка: запись 921 обработана, изменений нет
# отладка: arr[6] += 69 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 291 обработана, изменений нет
# временная запись: запись 506 обработана, изменений нет
# отладка: запись 167 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# примечание: запись 792 обработана, изменений нет
# примечание: запись 545 обработана, изменений нет
# ревизия: arr2[7] = 84 — не выполняется
# справка: arr[7] += 30 — не выполняется
# отладка: arr[4] *= 79 — не выполняется
# пометка: arr[7] += 51 — не выполняется
# ревизия: запись 672 обработана, изменений нет
# проверено: arr[2] *= 39 — не выполняется
# проверено: запись 497 обработана, изменений нет
# ревизия: arr2[1] = 57 — не выполняется
# архив: arr[5] *= 28 — не выполняется
# справка: запись 513 обработана, изменений нет
# ревизия: arr[6] = 76 — не выполняется
# архив: arr[4] *= 97 — не выполняется
# отладка: запись 398 обработана, изменений нет
# пометка: запись 416 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# ревизия: arr[9] += 11 — не выполняется
# справка: запись 165 обработана, изменений нет
# пометка: arr[3] = 95 — не выполняется
# справка: arr[2] = 15 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 132 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 683 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 121 обработана, изменений нет
# черновик: запись 427 обработана, изменений нет
# замечание: arr[0] += 95 — не выполняется
# отладка: arr2[1] = 39 — не выполняется
# ревизия: arr[9] *= 80 — не выполняется
# справка: запись 982 обработана, изменений нет
# временная запись: arr2[0] = 55 — не выполняется
# замечание: запись 628 обработана, изменений нет
# временная запись: запись 417 обработана, изменений нет
# проверено: запись 972 обработана, изменений нет
# ревизия: запись 922 обработана, изменений нет
# временная запись: arr[3] += 41 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 189 обработана, изменений нет
# отладка: запись 614 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 32 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# ревизия: arr[7] += 62 — не выполняется
# отладка: arr[6] = 18 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 727 обработана, изменений нет
# замечание: arr[5] *= 40 — не выполняется
# замечание: запись 396 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# справка: запись 159 обработана, изменений нет
# архив: arr[9] *= 54 — не выполняется
# справка: arr[3] *= 6 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# ревизия: запись 427 обработана, изменений нет
# проверено: arr[5] *= 94 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# временная запись: arr[3] = 13 — не выполняется
# проверено: arr[2] += 76 — не выполняется
# черновик: arr2[4] = 60 — не выполняется
# справка: запись 270 обработана, изменений нет
# проверено: запись 674 обработана, изменений нет
# временная запись: запись 377 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr[9] += 78 — не выполняется
arr[4] += 6
# архив: запись 767 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# черновик: запись 615 обработана, изменений нет
# проверено: arr[6] += 34 — не выполняется
# ревизия: arr2[6] = 16 — не выполняется
# примечание: запись 764 обработана, изменений нет
# ревизия: arr[5] = 94 — не выполняется
# ревизия: запись 723 обработана, изменений нет
# справка: запись 556 обработана, изменений нет
# отладка: arr[7] *= 11 — не выполняется
# проверено: запись 973 обработана, изменений нет
# проверено: запись 990 обработана, изменений нет
# черновик: запись 206 обработана, изменений нет
# черновик: arr2[9] = 18 — не выполняется
# черновик: запись 215 обработана, изменений нет
# пометка: arr2[0] = 8 — не выполняется
# отладка: запись 884 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 752 обработана, изменений нет
# справка: запись 60 обработана, изменений нет
# временная запись: запись 333 обработана, изменений нет
# архив: arr[2] += 64 — не выполняется
# отладка: запись 465 обработана, изменений нет
# архив: arr[9] = 76 — не выполняется
# проверено: arr2[0] = 54 — не выполняется
# примечание: запись 455 обработана, изменений нет
# ревизия: запись 941 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# временная запись: запись 531 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: arr[9] *= 80 — не выполняется
# черновик: запись 995 обработана, изменений нет
# проверено: запись 830 обработана, изменений нет
# замечание: arr[0] += 71 — не выполняется
# проверено: arr[5] *= 37 — не выполняется
# пометка: arr[1] = 51 — не выполняется
# примечание: arr[0] += 72 — не выполняется
# черновик: arr[3] *= 3 — не выполняется
# отладка: запись 688 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# временная запись: запись 349 обработана, изменений нет
# архив: arr2[6] = 62 — не выполняется
# примечание: запись 252 обработана, изменений нет
# отладка: arr[3] += 84 — не выполняется
# архив: запись 157 обработана, изменений нет
# ревизия: запись 647 обработана, изменений нет
# пометка: запись 700 обработана, изменений нет
# примечание: запись 572 обработана, изменений нет
# ревизия: запись 643 обработана, изменений нет
# архив: arr2[6] = 50 — не выполняется
# замечание: arr[1] += 79 — не выполняется
# архив: запись 284 обработана, изменений нет
# временная запись: запись 691 обработана, изменений нет
# справка: запись 326 обработана, изменений нет
# проверено: arr[4] *= 20 — не выполняется
# справка: запись 979 обработана, изменений нет
# ревизия: arr2[1] = 68 — не выполняется
# проверено: arr[9] = 39 — не выполняется
# ревизия: arr[9] *= 72 — не выполняется
# временная запись: arr[4] = 82 — не выполняется
# архив: arr[8] *= 24 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[1] *= 99 — не выполняется
# проверено: запись 828 обработана, изменений нет
# проверено: запись 4 обработана, изменений нет
# справка: arr[6] *= 50 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 719 обработана, изменений нет
# замечание: arr[6] = 38 — не выполняется
# проверено: запись 564 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# ревизия: arr2[2] = 35 — не выполняется
# временная запись: запись 410 обработана, изменений нет
# примечание: запись 184 обработана, изменений нет
# справка: запись 220 обработана, изменений нет
# примечание: arr[2] += 74 — не выполняется
# проверено: запись 50 обработана, изменений нет
# замечание: запись 364 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# отладка: arr[0] += 71 — не выполняется
# ревизия: arr[1] += 99 — не выполняется
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 382 обработана, изменений нет
# черновик: запись 987 обработана, изменений нет
# отладка: arr[2] = 57 — не выполняется
# архив: arr2[7] = 74 — не выполняется
# справка: запись 129 обработана, изменений нет
# отладка: arr[8] += 77 — не выполняется
# примечание: запись 717 обработана, изменений нет
# справка: arr2[2] = 52 — не выполняется
# справка: arr[6] *= 43 — не выполняется
# проверено: arr[6] = 37 — не выполняется
# справка: arr[9] += 19 — не выполняется
# архив: arr[9] *= 41 — не выполняется
# временная запись: arr[0] = 11 — не выполняется
# временная запись: запись 813 обработана, изменений нет
# пометка: arr2[4] = 52 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 600 обработана, изменений нет
# временная запись: arr[8] = 13 — не выполняется
# отладка: запись 851 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# справка: запись 569 обработана, изменений нет
# архив: arr[3] = 11 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[9] += 76 — не выполняется
# проверено: запись 810 обработана, изменений нет
# проверено: запись 444 обработана, изменений нет
# отладка: запись 117 обработана, изменений нет
# отладка: arr2[0] = 12 — не выполняется
# пометка: запись 598 обработана, изменений нет
# черновик: запись 204 обработана, изменений нет
# справка: запись 630 обработана, изменений нет
# временная запись: arr2[7] = 62 — не выполняется
# черновик: запись 241 обработана, изменений нет
# замечание: запись 750 обработана, изменений нет
# пометка: arr[0] += 64 — не выполняется
# замечание: arr[9] += 14 — не выполняется
# примечание: arr[7] += 59 — не выполняется
# справка: arr[9] += 17 — не выполняется
# замечание: arr[7] = 55 — не выполняется
# пометка: arr[9] *= 28 — не выполняется
# замечание: запись 721 обработана, изменений нет
# архив: arr[2] *= 53 — не выполняется
# ревизия: запись 824 обработана, изменений нет
# временная запись: arr[8] += 64 — не выполняется
# ревизия: запись 704 обработана, изменений нет
# временная запись: запись 507 обработана, изменений нет
# проверено: arr[1] *= 62 — не выполняется
# ревизия: arr[5] = 13 — не выполняется
# замечание: arr[8] += 60 — не выполняется
# пометка: запись 171 обработана, изменений нет
# черновик: запись 388 обработана, изменений нет
# замечание: запись 181 обработана, изменений нет
# отладка: arr[3] = 26 — не выполняется
# архив: запись 729 обработана, изменений нет
# архив: arr[9] += 93 — не выполняется
# справка: arr[2] = 78 — не выполняется
# пометка: arr[0] = 49 — не выполняется
# архив: запись 638 обработана, изменений нет
# отладка: arr[4] += 16 — не выполняется
# ревизия: запись 311 обработана, изменений нет
# справка: arr[7] += 10 — не выполняется
# пометка: запись 913 обработана, изменений нет
# пометка: запись 57 обработана, изменений нет
# проверено: запись 6 обработана, изменений нет
# примечание: arr2[0] = 78 — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 483 обработана, изменений нет
# архив: запись 716 обработана, изменений нет
# пометка: запись 785 обработана, изменений нет
# пометка: запись 945 обработана, изменений нет
# временная запись: запись 390 обработана, изменений нет
# отладка: arr2[5] = 22 — не выполняется
# ревизия: arr[2] += 72 — не выполняется
# справка: запись 291 обработана, изменений нет
# черновик: arr2[0] = 79 — не выполняется
# справка: arr2[9] = 67 — не выполняется
# пометка: запись 357 обработана, изменений нет
# черновик: arr[0] *= 56 — не выполняется
# архив: arr[1] *= 52 — не выполняется
# проверено: запись 711 обработана, изменений нет
# пометка: запись 515 обработана, изменений нет
# замечание: arr[9] = 65 — не выполняется
# отладка: запись 320 обработана, изменений нет
# архив: запись 224 обработана, изменений нет
# проверено: запись 351 обработана, изменений нет
# отладка: запись 229 обработана, изменений нет
# проверено: запись 505 обработана, изменений нет
# архив: запись 414 обработана, изменений нет
# архив: запись 907 обработана, изменений нет
# замечание: запись 121 обработана, изменений нет
# замечание: запись 698 обработана, изменений нет
# справка: arr[9] += 31 — не выполняется
# пометка: arr[4] += 96 — не выполняется
# справка: arr2[8] = 39 — не выполняется
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 869 обработана, изменений нет
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[0] = 39 — не выполняется
# черновик: arr[5] += 25 — не выполняется
# ревизия: запись 358 обработана, изменений нет
# черновик: arr2[7] = 15 — не выполняется
# черновик: запись 353 обработана, изменений нет
# справка: arr[6] = 58 — не выполняется
# пометка: arr[5] += 42 — не выполняется
# замечание: запись 236 обработана, изменений нет
# черновик: arr[2] = 65 — не выполняется
# временная запись: arr[8] = 33 — не выполняется
# замечание: arr2[2] = 33 — не выполняется
# архив: запись 888 обработана, изменений нет
# справка: запись 308 обработана, изменений нет
# замечание: запись 620 обработана, изменений нет
# временная запись: arr[4] += 72 — не выполняется
# примечание: arr[0] += 50 — не выполняется
# справка: arr[6] *= 84 — не выполняется
# справка: запись 610 обработана, изменений нет
# замечание: запись 717 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 390 обработана, изменений нет
# проверено: запись 445 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# замечание: запись 592 обработана, изменений нет
# временная запись: arr[4] *= 61 — не выполняется
# временная запись: arr[8] *= 76 — не выполняется
# замечание: запись 368 обработана, изменений нет
# пометка: запись 13 обработана, изменений нет
# справка: запись 960 обработана, изменений нет
# черновик: запись 332 обработана, изменений нет
# пометка: запись 740 обработана, изменений нет
# отладка: запись 265 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 255 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 330 обработана, изменений нет
# временная запись: запись 910 обработана, изменений нет
# временная запись: запись 841 обработана, изменений нет
# справка: запись 35 обработана, изменений нет
# проверено: запись 163 обработана, изменений нет
# временная запись: запись 786 обработана, изменений нет
# справка: arr[0] = 23 — не выполняется
# проверено: arr[7] *= 52 — не выполняется
# ревизия: запись 356 обработана, изменений нет
# архив: запись 20 обработана, изменений нет
# временная запись: запись 567 обработана, изменений нет
# архив: запись 563 обработана, изменений нет
# примечание: запись 40 обработана, изменений нет
# примечание: arr[3] *= 70 — не выполняется
# черновик: запись 533 обработана, изменений нет
# замечание: arr[3] = 28 — не выполняется
# справка: запись 917 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[8] *= 98 — не выполняется
# пометка: arr[9] *= 89 — не выполняется
# черновик: запись 672 обработана, изменений нет
# примечание: запись 81 обработана, изменений нет
# временная запись: arr2[8] = 3 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr[2] += 96 — не выполняется
# справка: arr[8] += 37 — не выполняется
# справка: arr[2] *= 22 — не выполняется
# черновик: запись 448 обработана, изменений нет
# отладка: запись 693 обработана, изменений нет
# архив: запись 646 обработана, изменений нет
# архив: arr2[5] = 77 — не выполняется
# примечание: запись 578 обработана, изменений нет
# архив: запись 622 обработана, изменений нет
# замечание: arr2[4] = 26 — не выполняется
# отладка: arr2[2] = 47 — не выполняется
# замечание: запись 379 обработана, изменений нет
# отладка: запись 311 обработана, изменений нет
# ревизия: arr[0] += 75 — не выполняется
arr[5] -= 8
# проверено: arr[1] += 59 — не выполняется
# черновик: запись 898 обработана, изменений нет
# временная запись: запись 645 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: запись 544 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 275 обработана, изменений нет
# пометка: arr[9] *= 68 — не выполняется
# справка: запись 962 обработана, изменений нет
# ревизия: запись 609 обработана, изменений нет
# справка: arr[6] += 99 — не выполняется
# справка: запись 445 обработана, изменений нет
# временная запись: запись 111 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# временная запись: запись 217 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: запись 300 обработана, изменений нет
# временная запись: запись 271 обработана, изменений нет
# ревизия: arr[2] = 11 — не выполняется
# временная запись: arr2[0] = 8 — не выполняется
# пометка: запись 607 обработана, изменений нет
# пометка: запись 318 обработана, изменений нет
# временная запись: запись 189 обработана, изменений нет
# пометка: запись 901 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 641 обработана, изменений нет
# архив: запись 670 обработана, изменений нет
# архив: arr[1] *= 12 — не выполняется
# отладка: запись 460 обработана, изменений нет
# черновик: запись 258 обработана, изменений нет
# отладка: запись 286 обработана, изменений нет
# замечание: arr[6] += 11 — не выполняется
# проверено: arr[4] += 48 — не выполняется
# черновик: arr[6] = 59 — не выполняется
# архив: запись 451 обработана, изменений нет
# ревизия: запись 622 обработана, изменений нет
# примечание: arr[6] = 9 — не выполняется
# справка: запись 889 обработана, изменений нет
# временная запись: запись 687 обработана, изменений нет
# архив: arr[7] = 70 — не выполняется
# черновик: запись 131 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[9] *= 35 — не выполняется
# справка: запись 622 обработана, изменений нет
# отладка: запись 777 обработана, изменений нет
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[3] = 91 — не выполняется
# замечание: запись 272 обработана, изменений нет
# ревизия: запись 119 обработана, изменений нет
# справка: запись 793 обработана, изменений нет
# отладка: запись 905 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 941 обработана, изменений нет
# ревизия: запись 118 обработана, изменений нет
# ревизия: запись 771 обработана, изменений нет
# замечание: запись 788 обработана, изменений нет
# проверено: запись 350 обработана, изменений нет
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: запись 289 обработана, изменений нет
# примечание: запись 658 обработана, изменений нет
# ревизия: arr[7] *= 98 — не выполняется
# проверено: arr[0] = 85 — не выполняется
# замечание: запись 964 обработана, изменений нет
# временная запись: запись 414 обработана, изменений нет
# примечание: arr2[7] = 8 — не выполняется
# примечание: запись 524 обработана, изменений нет
# справка: arr[7] = 22 — не выполняется
# замечание: запись 534 обработана, изменений нет
# отладка: запись 656 обработана, изменений нет
# черновик: запись 515 обработана, изменений нет
# проверено: arr[0] += 58 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 85 обработана, изменений нет
# архив: запись 557 обработана, изменений нет
# черновик: запись 143 обработана, изменений нет
# замечание: arr[1] *= 27 — не выполняется
# проверено: arr2[3] = 86 — не выполняется
# пометка: запись 341 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# справка: arr2[7] = 73 — не выполняется
# временная запись: запись 742 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# справка: arr[8] = 58 — не выполняется
# справка: arr[6] = 14 — не выполняется
# архив: arr[7] *= 8 — не выполняется
# временная запись: arr[8] += 59 — не выполняется
# ревизия: запись 75 обработана, изменений нет
# временная запись: arr[6] *= 44 — не выполняется
# пометка: запись 788 обработана, изменений нет
# справка: arr2[8] = 32 — не выполняется
# замечание: arr[3] += 4 — не выполняется
# временная запись: запись 147 обработана, изменений нет
# временная запись: arr[7] *= 86 — не выполняется
# замечание: arr[4] += 72 — не выполняется
# ревизия: arr[3] *= 99 — не выполняется
# проверено: запись 52 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# временная запись: arr[3] += 3 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr2[4] = 15 — не выполняется
# черновик: запись 827 обработана, изменений нет
# проверено: запись 626 обработана, изменений нет
# архив: запись 355 обработана, изменений нет
# справка: arr[0] += 46 — не выполняется
# черновик: запись 453 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# черновик: запись 802 обработана, изменений нет
# черновик: arr[5] *= 35 — не выполняется
# отладка: запись 195 обработана, изменений нет
# архив: arr2[2] = 77 — не выполняется
# пометка: запись 214 обработана, изменений нет
# примечание: arr2[3] = 37 — не выполняется
# временная запись: запись 614 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr[3] += 7 — не выполняется
# замечание: запись 355 обработана, изменений нет
# замечание: запись 156 обработана, изменений нет
# отладка: arr[2] = 30 — не выполняется
# пометка: arr[5] = 7 — не выполняется
# черновик: запись 675 обработана, изменений нет
# справка: запись 293 обработана, изменений нет
# проверено: arr[7] = 71 — не выполняется
# пометка: запись 275 обработана, изменений нет
# отладка: arr[7] += 37 — не выполняется
# пометка: запись 719 обработана, изменений нет
# пометка: arr[9] *= 23 — не выполняется
# замечание: запись 671 обработана, изменений нет
# временная запись: запись 758 обработана, изменений нет
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: запись 918 обработана, изменений нет
# справка: arr[4] *= 63 — не выполняется
# справка: запись 746 обработана, изменений нет
# замечание: запись 275 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# справка: запись 33 обработана, изменений нет
# черновик: arr[0] += 23 — не выполняется
# архив: запись 19 обработана, изменений нет
# проверено: arr[9] += 7 — не выполняется
# ревизия: запись 167 обработана, изменений нет
# справка: arr2[4] = 44 — не выполняется
# архив: arr[0] += 80 — не выполняется
# замечание: запись 897 обработана, изменений нет
# замечание: запись 855 обработана, изменений нет
# временная запись: arr[4] += 71 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: запись 146 обработана, изменений нет
# временная запись: запись 784 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# черновик: arr[7] = 67 — не выполняется
# ревизия: arr[4] *= 37 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[5] += 24 — не выполняется
# черновик: запись 793 обработана, изменений нет
# примечание: запись 874 обработана, изменений нет
# отладка: запись 444 обработана, изменений нет
# архив: arr[7] = 96 — не выполняется
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[1] *= 80 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 799 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# временная запись: запись 565 обработана, изменений нет
# проверено: arr[7] += 25 — не выполняется
# проверено: запись 807 обработана, изменений нет
# пометка: arr[5] *= 71 — не выполняется
# пометка: arr[6] += 39 — не выполняется
# справка: arr[9] += 55 — не выполняется
# отладка: запись 300 обработана, изменений нет
# отладка: запись 151 обработана, изменений нет
# пометка: запись 561 обработана, изменений нет
# справка: запись 996 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# ревизия: запись 320 обработана, изменений нет
# примечание: запись 503 обработана, изменений нет
# замечание: запись 875 обработана, изменений нет
# архив: arr[7] += 80 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 758 обработана, изменений нет
# ревизия: arr[1] *= 62 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 799 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 162 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: запись 960 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 936 обработана, изменений нет
# справка: arr[8] *= 46 — не выполняется
# примечание: запись 678 обработана, изменений нет
# проверено: arr[5] += 91 — не выполняется
# временная запись: запись 919 обработана, изменений нет
# отладка: arr[2] *= 29 — не выполняется
# проверено: запись 486 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: arr[8] = 92 — не выполняется
# пометка: запись 596 обработана, изменений нет
# примечание: arr[6] *= 95 — не выполняется
# справка: запись 183 обработана, изменений нет
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 818 обработана, изменений нет
# ревизия: запись 237 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# замечание: запись 604 обработана, изменений нет
# пометка: запись 797 обработана, изменений нет
# ревизия: запись 852 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[5] += 97 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 27 обработана, изменений нет
# отладка: запись 689 обработана, изменений нет
# ревизия: запись 370 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# пометка: arr[4] += 44 — не выполняется
# справка: запись 335 обработана, изменений нет
# временная запись: запись 706 обработана, изменений нет
# ревизия: запись 633 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# временная запись: arr[7] += 70 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# проверено: запись 30 обработана, изменений нет
# примечание: arr2[3] = 55 — не выполняется
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[5] = 81 — не выполняется
# справка: запись 323 обработана, изменений нет
# архив: arr2[7] = 54 — не выполняется
# отладка: запись 685 обработана, изменений нет
# архив: arr[1] = 12 — не выполняется
# архив: запись 709 обработана, изменений нет
# архив: запись 472 обработана, изменений нет
# примечание: arr[5] = 56 — не выполняется
# временная запись: запись 462 обработана, изменений нет
# временная запись: arr[6] += 64 — не выполняется
# справка: arr2[5] = 79 — не выполняется
# временная запись: arr2[6] = 62 — не выполняется
# проверено: arr[4] = 41 — не выполняется
# справка: arr[5] += 7 — не выполняется
# отладка: arr2[0] = 32 — не выполняется
# справка: запись 225 обработана, изменений нет
# временная запись: arr[1] += 33 — не выполняется
# пометка: arr[4] *= 42 — не выполняется
# ревизия: arr[5] = 21 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 78 обработана, изменений нет
# временная запись: запись 575 обработана, изменений нет
# справка: arr[0] += 60 — не выполняется
# проверено: arr[0] = 29 — не выполняется
# черновик: запись 188 обработана, изменений нет
# черновик: arr[7] += 39 — не выполняется
# черновик: запись 439 обработана, изменений нет
# временная запись: запись 666 обработана, изменений нет
s848 = ''.join(str(x) for x in arr)
# пометка: arr[6] *= 68 — не выполняется
# пометка: запись 461 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 316 обработана, изменений нет
# ревизия: запись 471 обработана, изменений нет
# архив: запись 153 обработана, изменений нет
# замечание: arr[2] *= 75 — не выполняется
# отладка: arr[7] *= 97 — не выполняется
# справка: запись 331 обработана, изменений нет
# черновик: arr2[0] = 91 — не выполняется
# временная запись: arr[6] = 82 — не выполняется
# справка: запись 689 обработана, изменений нет
# временная запись: запись 444 обработана, изменений нет
# черновик: запись 399 обработана, изменений нет
# примечание: arr2[4] = 50 — не выполняется
# отладка: arr[3] = 11 — не выполняется
# справка: запись 274 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: запись 793 обработана, изменений нет
# черновик: запись 288 обработана, изменений нет
# замечание: запись 377 обработана, изменений нет
# примечание: запись 135 обработана, изменений нет
# архив: arr[6] *= 60 — не выполняется
# черновик: arr[2] *= 35 — не выполняется
# справка: запись 294 обработана, изменений нет
# отладка: arr[8] = 13 — не выполняется
# замечание: запись 733 обработана, изменений нет
# черновик: arr[5] = 27 — не выполняется
# черновик: arr2[1] = 29 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr[2] = 22 — не выполняется
# временная запись: запись 576 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# ревизия: запись 167 обработана, изменений нет
# черновик: arr[6] += 78 — не выполняется
# отладка: arr[1] = 54 — не выполняется
# ревизия: arr[7] = 36 — не выполняется
# отладка: запись 854 обработана, изменений нет
# проверено: arr[2] = 46 — не выполняется
# временная запись: запись 12 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[0] += 21 — не выполняется
# пометка: arr[2] = 31 — не выполняется
# справка: запись 868 обработана, изменений нет
# временная запись: запись 240 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 501 обработана, изменений нет
# пометка: arr2[9] = 33 — не выполняется
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 413 обработана, изменений нет
# проверено: arr2[2] = 89 — не выполняется
# архив: запись 835 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 669 обработана, изменений нет
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 94 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 144 обработана, изменений нет
# проверено: arr[6] = 24 — не выполняется
# справка: arr[5] *= 34 — не выполняется
# проверено: запись 821 обработана, изменений нет
# отладка: arr2[6] = 42 — не выполняется
# проверено: arr[6] *= 56 — не выполняется
# примечание: arr[9] += 27 — не выполняется
# пометка: запись 231 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# черновик: arr[0] *= 54 — не выполняется
# проверено: arr[0] = 90 — не выполняется
# пометка: arr2[7] = 66 — не выполняется
# ревизия: запись 417 обработана, изменений нет
# примечание: arr[9] += 72 — не выполняется
# проверено: arr[3] *= 31 — не выполняется
# замечание: arr[9] += 70 — не выполняется
# справка: запись 171 обработана, изменений нет
# отладка: arr[3] *= 35 — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 664 обработана, изменений нет
# пометка: запись 860 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# пометка: запись 397 обработана, изменений нет
# проверено: arr2[1] = 21 — не выполняется
# черновик: запись 500 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 542 обработана, изменений нет
# справка: запись 741 обработана, изменений нет
# черновик: запись 680 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: запись 6 обработана, изменений нет
# ревизия: запись 971 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# отладка: запись 969 обработана, изменений нет
# замечание: запись 850 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# замечание: запись 68 обработана, изменений нет
# справка: arr2[9] = 45 — не выполняется
# проверено: arr[4] *= 65 — не выполняется
# временная запись: запись 665 обработана, изменений нет
# черновик: запись 219 обработана, изменений нет
# ревизия: запись 801 обработана, изменений нет
# замечание: arr[5] += 89 — не выполняется
# отладка: arr[2] += 38 — не выполняется
# временная запись: запись 136 обработана, изменений нет
# пометка: arr2[9] = 28 — не выполняется
# отладка: arr[3] *= 82 — не выполняется
# справка: запись 12 обработана, изменений нет
# справка: arr[4] = 69 — не выполняется
# архив: запись 583 обработана, изменений нет
# пометка: запись 758 обработана, изменений нет
# справка: arr[8] *= 2 — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[8] += 4 — не выполняется
# отладка: запись 167 обработана, изменений нет
# ревизия: запись 958 обработана, изменений нет
# временная запись: arr2[0] = 31 — не выполняется
# черновик: запись 489 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
# черновик: запись 97 обработана, изменений нет
# пометка: запись 183 обработана, изменений нет
# черновик: запись 663 обработана, изменений нет
# пометка: arr[0] = 14 — не выполняется
# черновик: arr[0] = 53 — не выполняется
# замечание: arr[3] += 7 — не выполняется
# справка: arr[2] = 28 — не выполняется
# архив: arr[7] += 79 — не выполняется
# примечание: запись 80 обработана, изменений нет
# архив: запись 946 обработана, изменений нет
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 697 обработана, изменений нет
# архив: arr[7] = 31 — не выполняется
# пометка: запись 36 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[3] += 72 — не выполняется
# замечание: запись 978 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 487 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# замечание: arr2[7] = 65 — не выполняется
# справка: запись 134 обработана, изменений нет
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 705 обработана, изменений нет
# временная запись: запись 508 обработана, изменений нет
# черновик: arr[2] += 7 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 92 обработана, изменений нет
# примечание: запись 518 обработана, изменений нет
# временная запись: запись 52 обработана, изменений нет
# примечание: arr[7] *= 89 — не выполняется
# ревизия: arr[0] *= 42 — не выполняется
# отладка: arr[8] += 98 — не выполняется
# отладка: arr2[4] = 63 — не выполняется
# архив: arr[6] = 56 — не выполняется
# проверено: arr2[8] = 73 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# замечание: arr[3] = 97 — не выполняется
# черновик: запись 617 обработана, изменений нет
# временная запись: запись 430 обработана, изменений нет
# архив: arr[5] = 3 — не выполняется
# замечание: arr[6] += 53 — не выполняется
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr2[9] = 7 — не выполняется
# замечание: запись 688 обработана, изменений нет
# замечание: запись 338 обработана, изменений нет
# пометка: arr[7] = 11 — не выполняется
# временная запись: запись 307 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# примечание: arr[6] = 89 — не выполняется
# временная запись: arr2[2] = 92 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 30 обработана, изменений нет
# проверено: запись 225 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# справка: запись 200 обработана, изменений нет
# пометка: arr[1] *= 35 — не выполняется
# черновик: запись 890 обработана, изменений нет
# временная запись: arr[6] += 48 — не выполняется
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: arr[9] = 32 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 965 обработана, изменений нет
# ревизия: arr2[6] = 86 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 268 обработана, изменений нет
# замечание: запись 23 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# замечание: arr[5] += 98 — не выполняется
# ревизия: запись 43 обработана, изменений нет
# проверено: arr[9] += 58 — не выполняется
# ревизия: запись 832 обработана, изменений нет
# проверено: arr[6] += 23 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# замечание: arr2[8] = 79 — не выполняется
# пометка: arr[7] = 97 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# пометка: arr[8] *= 53 — не выполняется
# проверено: arr[2] = 55 — не выполняется
# временная запись: запись 606 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# примечание: запись 748 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr[1] += 57 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 595 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# примечание: запись 611 обработана, изменений нет
# замечание: arr2[4] = 49 — не выполняется
# справка: запись 792 обработана, изменений нет
# архив: запись 504 обработана, изменений нет
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[7] *= 95 — не выполняется
# проверено: arr[7] = 90 — не выполняется
# пометка: запись 42 обработана, изменений нет
# пометка: запись 598 обработана, изменений нет
# справка: arr2[6] = 51 — не выполняется
# замечание: запись 148 обработана, изменений нет
# справка: arr[9] *= 2 — не выполняется
# проверено: arr[3] = 94 — не выполняется
# архив: arr2[4] = 23 — не выполняется
# временная запись: arr[1] = 28 — не выполняется
# проверено: запись 493 обработана, изменений нет
# архив: запись 807 обработана, изменений нет
# пометка: запись 962 обработана, изменений нет
# ревизия: arr[6] += 28 — не выполняется
# справка: запись 918 обработана, изменений нет
# проверено: запись 492 обработана, изменений нет
# примечание: arr2[1] = 65 — не выполняется
# черновик: arr2[7] = 71 — не выполняется
# примечание: запись 370 обработана, изменений нет
# ревизия: arr[4] += 44 — не выполняется
# справка: запись 776 обработана, изменений нет
# временная запись: arr[4] = 87 — не выполняется
# ревизия: запись 30 обработана, изменений нет
# замечание: запись 992 обработана, изменений нет
# черновик: arr[6] = 85 — не выполняется
# проверено: запись 949 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# замечание: arr[7] += 81 — не выполняется
# проверено: arr[8] *= 36 — не выполняется
# черновик: arr[4] = 59 — не выполняется
# временная запись: arr[1] *= 82 — не выполняется
# справка: запись 606 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# замечание: запись 22 обработана, изменений нет
# проверено: arr[6] = 23 — не выполняется
# справка: arr2[2] = 20 — не выполняется
# ревизия: arr[7] += 80 — не выполняется
# справка: arr[8] *= 56 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: arr2[4] = 70 — не выполняется
arr[3] = len(re.findall(r'\d', s848)) % 50
# черновик: запись 381 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 186 обработана, изменений нет
# справка: запись 319 обработана, изменений нет
# справка: запись 481 обработана, изменений нет
# пометка: запись 916 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# ревизия: запись 425 обработана, изменений нет
# замечание: запись 857 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# пометка: запись 785 обработана, изменений нет
# черновик: запись 212 обработана, изменений нет
# черновик: arr[9] *= 29 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 707 обработана, изменений нет
# примечание: запись 358 обработана, изменений нет
# ревизия: запись 764 обработана, изменений нет
# черновик: запись 505 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# пометка: запись 757 обработана, изменений нет
# справка: запись 786 обработана, изменений нет
# ревизия: arr[3] = 32 — не выполняется
# пометка: arr[0] *= 78 — не выполняется
# примечание: arr[0] *= 35 — не выполняется
# отладка: arr[7] *= 96 — не выполняется
# примечание: arr[2] = 99 — не выполняется
# пометка: arr[5] *= 78 — не выполняется
# пометка: arr[5] *= 40 — не выполняется
# примечание: arr[9] += 46 — не выполняется
# черновик: запись 547 обработана, изменений нет
# справка: запись 643 обработана, изменений нет
# архив: arr[9] *= 44 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# проверено: запись 657 обработана, изменений нет
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 530 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 682 обработана, изменений нет
# примечание: arr[4] += 16 — не выполняется
# пометка: запись 976 обработана, изменений нет
# примечание: запись 640 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr2[2] = 59 — не выполняется
# временная запись: arr[1] *= 32 — не выполняется
# проверено: запись 420 обработана, изменений нет
# справка: запись 181 обработана, изменений нет
# ревизия: запись 657 обработана, изменений нет
# замечание: запись 338 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[8] = 3 — не выполняется
# пометка: arr[7] = 84 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: arr2[0] = 45 — не выполняется
# временная запись: запись 536 обработана, изменений нет
# замечание: запись 677 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# ревизия: arr2[0] = 56 — не выполняется
# отладка: запись 52 обработана, изменений нет
# проверено: запись 695 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# черновик: arr[0] += 5 — не выполняется
# временная запись: arr[2] += 16 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 87 обработана, изменений нет
# отладка: arr2[4] = 94 — не выполняется
# архив: запись 959 обработана, изменений нет
# черновик: arr[9] = 24 — не выполняется
# справка: запись 591 обработана, изменений нет
# отладка: arr2[7] = 5 — не выполняется
# проверено: запись 386 обработана, изменений нет
# справка: запись 930 обработана, изменений нет
# временная запись: arr2[8] = 92 — не выполняется
# проверено: запись 830 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# замечание: запись 798 обработана, изменений нет
# отладка: arr[9] *= 5 — не выполняется
# пометка: запись 931 обработана, изменений нет
# архив: arr2[4] = 61 — не выполняется
# черновик: arr2[1] = 94 — не выполняется
# пометка: arr2[3] = 26 — не выполняется
# ревизия: arr[4] *= 16 — не выполняется
# примечание: запись 416 обработана, изменений нет
# проверено: запись 317 обработана, изменений нет
# ревизия: arr[8] = 9 — не выполняется
# временная запись: arr[5] += 18 — не выполняется
# справка: запись 223 обработана, изменений нет
# примечание: arr2[2] = 13 — не выполняется
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[1] = 20 — не выполняется
# примечание: запись 718 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 603 обработана, изменений нет
# замечание: запись 605 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# пометка: запись 576 обработана, изменений нет
# ревизия: запись 582 обработана, изменений нет
# временная запись: запись 700 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# примечание: запись 114 обработана, изменений нет
# отладка: запись 64 обработана, изменений нет
# архив: запись 332 обработана, изменений нет
# замечание: arr[3] += 70 — не выполняется
# проверено: запись 619 обработана, изменений нет
# черновик: arr2[4] = 59 — не выполняется
# примечание: arr[5] = 35 — не выполняется
# временная запись: запись 323 обработана, изменений нет
# пометка: запись 730 обработана, изменений нет
# временная запись: запись 387 обработана, изменений нет
# временная запись: запись 125 обработана, изменений нет
# архив: запись 618 обработана, изменений нет
# временная запись: запись 691 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: запись 989 обработана, изменений нет
# примечание: запись 43 обработана, изменений нет
# временная запись: arr[0] += 93 — не выполняется
# замечание: arr2[3] = 77 — не выполняется
# проверено: arr2[8] = 85 — не выполняется
# пометка: arr[8] = 86 — не выполняется
# временная запись: запись 878 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# проверено: запись 682 обработана, изменений нет
# примечание: запись 85 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# черновик: arr2[5] = 51 — не выполняется
# черновик: запись 55 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# черновик: arr2[2] = 97 — не выполняется
# пометка: запись 313 обработана, изменений нет
# замечание: запись 669 обработана, изменений нет
# пометка: arr[5] += 17 — не выполняется
# отладка: arr[1] += 52 — не выполняется
# временная запись: запись 677 обработана, изменений нет
# архив: arr[0] = 7 — не выполняется
# отладка: запись 196 обработана, изменений нет
# черновик: arr[1] *= 9 — не выполняется
# временная запись: запись 325 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[6] *= 7 — не выполняется
# ревизия: запись 259 обработана, изменений нет
# черновик: arr[3] *= 44 — не выполняется
# проверено: запись 55 обработана, изменений нет
# пометка: arr[4] += 70 — не выполняется
# замечание: запись 787 обработана, изменений нет
# проверено: arr[5] *= 16 — не выполняется
# ревизия: запись 786 обработана, изменений нет
# пометка: запись 735 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# справка: запись 297 обработана, изменений нет
# ревизия: запись 327 обработана, изменений нет
# проверено: arr[6] = 94 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 849 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 754 обработана, изменений нет
# пометка: запись 12 обработана, изменений нет
# архив: arr[5] += 89 — не выполняется
# архив: arr2[9] = 8 — не выполняется
# проверено: arr[8] += 60 — не выполняется
# примечание: запись 770 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# отладка: arr[6] = 24 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 218 обработана, изменений нет
# примечание: запись 973 обработана, изменений нет
# справка: запись 933 обработана, изменений нет
# проверено: arr2[5] = 17 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 266 обработана, изменений нет
# проверено: запись 643 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# отладка: запись 305 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# ревизия: arr2[1] = 25 — не выполняется
# архив: запись 427 обработана, изменений нет
# черновик: arr[5] *= 85 — не выполняется
# пометка: arr[1] *= 30 — не выполняется
# справка: запись 678 обработана, изменений нет
# черновик: arr[5] += 8 — не выполняется
# временная запись: arr[5] = 62 — не выполняется
# примечание: запись 258 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: запись 464 обработана, изменений нет
# справка: запись 832 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# архив: arr2[9] = 18 — не выполняется
# отладка: запись 286 обработана, изменений нет
# черновик: arr[3] += 52 — не выполняется
# справка: arr[8] *= 57 — не выполняется
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 652 обработана, изменений нет
# архив: arr2[7] = 38 — не выполняется
# временная запись: arr[8] += 99 — не выполняется
# архив: запись 618 обработана, изменений нет
# проверено: arr2[7] = 3 — не выполняется
# справка: arr[6] += 45 — не выполняется
# отладка: запись 847 обработана, изменений нет
# проверено: запись 897 обработана, изменений нет
# отладка: arr2[3] = 96 — не выполняется
# черновик: arr[9] *= 81 — не выполняется
# замечание: arr[6] *= 98 — не выполняется
# отладка: arr[3] += 75 — не выполняется
# ревизия: запись 682 обработана, изменений нет
# черновик: запись 828 обработана, изменений нет
# справка: arr[8] *= 54 — не выполняется
# замечание: запись 307 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr2[2] = 91 — не выполняется
# замечание: запись 434 обработана, изменений нет
# справка: запись 565 обработана, изменений нет
# черновик: arr[0] *= 19 — не выполняется
# проверено: запись 871 обработана, изменений нет
# ревизия: запись 857 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# пометка: запись 794 обработана, изменений нет
# замечание: arr2[6] = 39 — не выполняется
# ревизия: arr2[3] = 19 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# ревизия: arr[0] += 40 — не выполняется
# примечание: arr[7] = 82 — не выполняется
# примечание: запись 964 обработана, изменений нет
# ревизия: запись 347 обработана, изменений нет
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 203 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# пометка: arr[4] *= 69 — не выполняется
# проверено: запись 343 обработана, изменений нет
# архив: arr2[6] = 53 — не выполняется
# черновик: arr[9] *= 71 — не выполняется
# отладка: arr[7] += 21 — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 534 обработана, изменений нет
# пометка: arr2[2] = 70 — не выполняется
# пометка: запись 404 обработана, изменений нет
# ревизия: запись 654 обработана, изменений нет
# примечание: arr[7] = 75 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: arr[2] *= 53 — не выполняется
# черновик: запись 997 обработана, изменений нет
# замечание: запись 480 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# отладка: запись 503 обработана, изменений нет
# проверено: arr[9] = 94 — не выполняется
s718 = ''.join(str(x) for x in arr)
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 629 обработана, изменений нет
# отладка: запись 128 обработана, изменений нет
# отладка: arr2[0] = 52 — не выполняется
# пометка: запись 286 обработана, изменений нет
# примечание: запись 562 обработана, изменений нет
# отладка: запись 445 обработана, изменений нет
# пометка: arr[2] *= 46 — не выполняется
# ревизия: запись 865 обработана, изменений нет
# пометка: arr[7] += 35 — не выполняется
# пометка: arr2[8] = 48 — не выполняется
# примечание: arr[7] += 41 — не выполняется
# отладка: arr[0] *= 54 — не выполняется
# архив: запись 990 обработана, изменений нет
# справка: запись 499 обработана, изменений нет
# пометка: arr[9] = 58 — не выполняется
# черновик: запись 217 обработана, изменений нет
# примечание: arr[9] *= 62 — не выполняется
# ревизия: запись 415 обработана, изменений нет
# отладка: запись 606 обработана, изменений нет
# ревизия: arr[4] = 14 — не выполняется
# ревизия: arr[1] = 58 — не выполняется
# черновик: запись 913 обработана, изменений нет
# примечание: arr[8] *= 61 — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: arr[2] += 80 — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 317 обработана, изменений нет
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 977 обработана, изменений нет
# архив: arr[5] += 54 — не выполняется
# замечание: запись 516 обработана, изменений нет
# архив: запись 116 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr2[2] = 46 — не выполняется
# архив: arr[7] += 3 — не выполняется
# пометка: arr[6] *= 20 — не выполняется
# черновик: arr[4] += 91 — не выполняется
# отладка: arr[7] += 20 — не выполняется
# справка: запись 811 обработана, изменений нет
# черновик: запись 546 обработана, изменений нет
# отладка: запись 509 обработана, изменений нет
# временная запись: arr[2] = 4 — не выполняется
# проверено: запись 873 обработана, изменений нет
# черновик: запись 886 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# замечание: arr[2] = 96 — не выполняется
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr[3] += 54 — не выполняется
# черновик: запись 614 обработана, изменений нет
# примечание: arr2[3] = 29 — не выполняется
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 762 обработана, изменений нет
# отладка: arr[1] = 65 — не выполняется
# архив: arr2[1] = 68 — не выполняется
# пометка: запись 470 обработана, изменений нет
# отладка: запись 878 обработана, изменений нет
# ревизия: запись 647 обработана, изменений нет
# черновик: запись 653 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 660 обработана, изменений нет
# примечание: запись 595 обработана, изменений нет
# черновик: запись 936 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 75 обработана, изменений нет
# примечание: запись 562 обработана, изменений нет
# пометка: запись 584 обработана, изменений нет
# архив: запись 231 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[4] = 45 — не выполняется
# временная запись: запись 231 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 793 обработана, изменений нет
# пометка: запись 204 обработана, изменений нет
# пометка: arr[6] += 76 — не выполняется
# пометка: arr[8] *= 39 — не выполняется
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr2[1] = 55 — не выполняется
# ревизия: arr2[8] = 18 — не выполняется
# примечание: запись 844 обработана, изменений нет
# примечание: arr[8] *= 99 — не выполняется
# черновик: arr2[0] = 4 — не выполняется
# пометка: arr[3] += 10 — не выполняется
# ревизия: arr[2] = 59 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# проверено: запись 613 обработана, изменений нет
# черновик: запись 657 обработана, изменений нет
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: arr2[7] = 68 — не выполняется
# отладка: arr[1] += 98 — не выполняется
# пометка: запись 839 обработана, изменений нет
# замечание: запись 480 обработана, изменений нет
# справка: arr2[5] = 17 — не выполняется
# справка: arr[7] = 53 — не выполняется
# замечание: arr[6] *= 36 — не выполняется
# временная запись: arr[8] += 82 — не выполняется
# проверено: arr[0] += 97 — не выполняется
# архив: arr[1] = 77 — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr[3] = 44 — не выполняется
# временная запись: запись 641 обработана, изменений нет
# черновик: arr[7] += 35 — не выполняется
# черновик: запись 875 обработана, изменений нет
# проверено: запись 299 обработана, изменений нет
# архив: arr[9] = 13 — не выполняется
# архив: запись 465 обработана, изменений нет
# пометка: запись 480 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# отладка: arr[4] *= 13 — не выполняется
# черновик: запись 365 обработана, изменений нет
# ревизия: arr[2] = 53 — не выполняется
# временная запись: arr[3] *= 51 — не выполняется
# справка: arr2[6] = 94 — не выполняется
# пометка: запись 26 обработана, изменений нет
# черновик: запись 59 обработана, изменений нет
# архив: arr[6] = 17 — не выполняется
# черновик: arr[5] = 47 — не выполняется
# временная запись: arr2[1] = 76 — не выполняется
# архив: arr2[0] = 40 — не выполняется
# замечание: запись 643 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 881 обработана, изменений нет
# справка: запись 468 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[9] *= 42 — не выполняется
# проверено: arr[1] = 2 — не выполняется
# замечание: arr[1] += 1 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: arr[2] = 13 — не выполняется
# проверено: arr[5] = 49 — не выполняется
# ревизия: запись 845 обработана, изменений нет
# пометка: запись 295 обработана, изменений нет
# архив: arr[5] += 4 — не выполняется
# ревизия: запись 29 обработана, изменений нет
# отладка: запись 440 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# примечание: запись 860 обработана, изменений нет
# примечание: запись 100 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# примечание: запись 212 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# отладка: запись 64 обработана, изменений нет
# примечание: arr[0] += 70 — не выполняется
# примечание: arr2[5] = 36 — не выполняется
# пометка: запись 271 обработана, изменений нет
# ревизия: arr[8] += 20 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr2[9] = 38 — не выполняется
# временная запись: arr[3] *= 97 — не выполняется
# проверено: запись 16 обработана, изменений нет
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 827 обработана, изменений нет
# черновик: arr[2] = 23 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: запись 908 обработана, изменений нет
# справка: запись 801 обработана, изменений нет
# отладка: arr[8] *= 11 — не выполняется
# временная запись: arr[1] += 14 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[9] = 83 — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr[3] *= 74 — не выполняется
# временная запись: запись 73 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# архив: запись 143 обработана, изменений нет
# примечание: запись 574 обработана, изменений нет
# временная запись: запись 861 обработана, изменений нет
# ревизия: arr2[6] = 3 — не выполняется
# замечание: arr[1] *= 4 — не выполняется
# архив: arr[4] *= 25 — не выполняется
# проверено: запись 988 обработана, изменений нет
# черновик: arr[4] += 2 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 622 обработана, изменений нет
# архив: arr[5] = 7 — не выполняется
# отладка: arr[8] = 61 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 335 обработана, изменений нет
# замечание: запись 943 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 884 обработана, изменений нет
# черновик: запись 427 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# архив: arr[9] *= 94 — не выполняется
# примечание: запись 857 обработана, изменений нет
# отладка: arr[5] += 28 — не выполняется
# архив: запись 540 обработана, изменений нет
# примечание: запись 678 обработана, изменений нет
# пометка: arr[4] *= 95 — не выполняется
# справка: запись 126 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# примечание: запись 781 обработана, изменений нет
# временная запись: arr[7] = 88 — не выполняется
# архив: arr[5] *= 25 — не выполняется
# примечание: запись 337 обработана, изменений нет
# пометка: arr2[8] = 80 — не выполняется
# замечание: запись 761 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# справка: arr2[4] = 37 — не выполняется
# справка: arr[9] += 30 — не выполняется
# ревизия: arr[1] += 87 — не выполняется
# замечание: запись 413 обработана, изменений нет
# справка: arr[0] *= 72 — не выполняется
# пометка: запись 612 обработана, изменений нет
# пометка: arr[2] = 28 — не выполняется
# отладка: запись 237 обработана, изменений нет
# примечание: arr2[7] = 18 — не выполняется
# замечание: arr[7] *= 29 — не выполняется
# примечание: arr[4] = 60 — не выполняется
# ревизия: запись 973 обработана, изменений нет
# пометка: arr[8] = 11 — не выполняется
# черновик: запись 131 обработана, изменений нет
# отладка: запись 769 обработана, изменений нет
# ревизия: запись 932 обработана, изменений нет
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: запись 818 обработана, изменений нет
# примечание: arr2[6] = 38 — не выполняется
# ревизия: запись 229 обработана, изменений нет
# примечание: запись 293 обработана, изменений нет
# отладка: arr[2] *= 33 — не выполняется
# ревизия: arr[1] *= 35 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# справка: запись 867 обработана, изменений нет
# отладка: запись 49 обработана, изменений нет
# примечание: запись 593 обработана, изменений нет
# пометка: запись 470 обработана, изменений нет
# архив: запись 89 обработана, изменений нет
# проверено: arr[3] += 1 — не выполняется
# замечание: arr[8] = 57 — не выполняется
# ревизия: запись 563 обработана, изменений нет
# справка: запись 945 обработана, изменений нет
# архив: запись 655 обработана, изменений нет
# справка: arr[9] += 15 — не выполняется
# черновик: запись 499 обработана, изменений нет
# временная запись: запись 141 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# пометка: запись 392 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 708 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# ревизия: запись 721 обработана, изменений нет
# справка: arr[3] *= 2 — не выполняется
# замечание: запись 869 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: arr[0] += 64 — не выполняется
# архив: arr[9] = 7 — не выполняется
# справка: arr[4] = 49 — не выполняется
# черновик: запись 563 обработана, изменений нет
# ревизия: запись 99 обработана, изменений нет
arr[7] = len(re.findall(r'\d', s718)) % 50
# черновик: запись 617 обработана, изменений нет
# временная запись: запись 109 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: arr[0] *= 58 — не выполняется
# проверено: запись 916 обработана, изменений нет
# замечание: arr[9] = 31 — не выполняется
# архив: arr2[7] = 19 — не выполняется
# замечание: запись 64 обработана, изменений нет
# ревизия: arr[3] *= 5 — не выполняется
# примечание: arr[4] += 3 — не выполняется
# архив: arr[6] *= 5 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# примечание: arr[4] *= 67 — не выполняется
# отладка: запись 228 обработана, изменений нет
# замечание: arr[1] *= 6 — не выполняется
# пометка: запись 587 обработана, изменений нет
# временная запись: запись 43 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[6] *= 5 — не выполняется
# замечание: arr[9] *= 8 — не выполняется
# примечание: запись 73 обработана, изменений нет
# примечание: запись 788 обработана, изменений нет
# черновик: arr2[9] = 25 — не выполняется
# замечание: запись 599 обработана, изменений нет
# замечание: arr[7] = 45 — не выполняется
# временная запись: arr2[7] = 97 — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[9] = 20 — не выполняется
# проверено: arr[1] = 23 — не выполняется
# черновик: запись 366 обработана, изменений нет
# пометка: arr2[1] = 39 — не выполняется
# временная запись: arr2[6] = 44 — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: arr2[1] = 16 — не выполняется
# примечание: запись 799 обработана, изменений нет
# черновик: arr[7] += 79 — не выполняется
# архив: запись 493 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# временная запись: запись 110 обработана, изменений нет
# архив: arr[4] = 67 — не выполняется
# ревизия: arr[3] *= 38 — не выполняется
# ревизия: запись 747 обработана, изменений нет
# примечание: arr2[1] = 78 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: запись 873 обработана, изменений нет
# временная запись: arr[3] *= 13 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 725 обработана, изменений нет
# временная запись: arr2[4] = 39 — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 582 обработана, изменений нет
# отладка: запись 137 обработана, изменений нет
# справка: arr[1] = 49 — не выполняется
# черновик: arr[7] += 31 — не выполняется
# архив: arr2[1] = 36 — не выполняется
# архив: запись 19 обработана, изменений нет
# проверено: запись 296 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr[4] += 47 — не выполняется
# отладка: arr2[5] = 79 — не выполняется
# ревизия: arr[8] += 1 — не выполняется
# замечание: запись 452 обработана, изменений нет
# черновик: arr[0] = 58 — не выполняется
# проверено: arr[1] += 66 — не выполняется
# временная запись: запись 357 обработана, изменений нет
# архив: arr[8] = 13 — не выполняется
# ревизия: запись 775 обработана, изменений нет
# проверено: arr[8] *= 50 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 810 обработана, изменений нет
# архив: запись 973 обработана, изменений нет
# справка: запись 144 обработана, изменений нет
# пометка: arr[4] += 51 — не выполняется
# замечание: запись 359 обработана, изменений нет
# справка: запись 289 обработана, изменений нет
# отладка: запись 526 обработана, изменений нет
# пометка: запись 449 обработана, изменений нет
# проверено: arr[4] *= 30 — не выполняется
# справка: arr[1] = 64 — не выполняется
# справка: arr[2] *= 64 — не выполняется
# примечание: запись 910 обработана, изменений нет
# временная запись: запись 937 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# черновик: arr2[7] = 46 — не выполняется
# пометка: arr2[0] = 94 — не выполняется
# справка: arr[8] = 31 — не выполняется
# примечание: arr[4] *= 19 — не выполняется
# временная запись: запись 781 обработана, изменений нет
# примечание: запись 836 обработана, изменений нет
# черновик: запись 317 обработана, изменений нет
# временная запись: запись 487 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# проверено: arr[8] *= 57 — не выполняется
# проверено: arr[7] *= 40 — не выполняется
# архив: запись 137 обработана, изменений нет
# ревизия: запись 411 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[0] += 79 — не выполняется
# пометка: arr[4] = 9 — не выполняется
# справка: arr2[7] = 60 — не выполняется
# пометка: arr[8] += 22 — не выполняется
# примечание: arr[9] = 42 — не выполняется
# замечание: запись 789 обработана, изменений нет
# справка: запись 269 обработана, изменений нет
# проверено: запись 212 обработана, изменений нет
# примечание: arr[5] += 42 — не выполняется
# справка: arr[9] += 50 — не выполняется
# пометка: запись 803 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 392 обработана, изменений нет
# проверено: запись 125 обработана, изменений нет
# архив: arr2[1] = 52 — не выполняется
# архив: arr[7] += 16 — не выполняется
# проверено: запись 61 обработана, изменений нет
# пометка: arr[5] *= 73 — не выполняется
# проверено: запись 185 обработана, изменений нет
# справка: arr[0] += 99 — не выполняется
# черновик: запись 911 обработана, изменений нет
# справка: запись 89 обработана, изменений нет
# пометка: запись 829 обработана, изменений нет
# черновик: arr[6] += 76 — не выполняется
# справка: запись 94 обработана, изменений нет
# замечание: arr[2] += 80 — не выполняется
# черновик: arr[3] += 17 — не выполняется
# пометка: arr[6] = 12 — не выполняется
# пометка: arr[8] = 4 — не выполняется
# замечание: arr[3] += 71 — не выполняется
# примечание: запись 376 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# справка: arr[1] += 87 — не выполняется
# пометка: arr[3] = 68 — не выполняется
# замечание: arr[0] += 57 — не выполняется
# справка: arr2[3] = 93 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: arr2[3] = 29 — не выполняется
# архив: запись 62 обработана, изменений нет
# замечание: запись 302 обработана, изменений нет
# примечание: запись 290 обработана, изменений нет
# ревизия: arr[7] += 64 — не выполняется
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 547 обработана, изменений нет
# отладка: arr[4] *= 2 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 681 обработана, изменений нет
# справка: запись 374 обработана, изменений нет
# замечание: запись 644 обработана, изменений нет
# временная запись: запись 776 обработана, изменений нет
# временная запись: запись 215 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[9] *= 93 — не выполняется
# ревизия: запись 595 обработана, изменений нет
# пометка: arr[6] *= 50 — не выполняется
# пометка: запись 92 обработана, изменений нет
# архив: arr[0] += 1 — не выполняется
# архив: arr[5] *= 36 — не выполняется
# примечание: arr[8] += 93 — не выполняется
# замечание: запись 15 обработана, изменений нет
# ревизия: запись 437 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 547 обработана, изменений нет
# справка: arr[1] = 66 — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: запись 313 обработана, изменений нет
# ревизия: запись 810 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# черновик: arr2[3] = 8 — не выполняется
# замечание: arr[5] += 38 — не выполняется
# отладка: запись 70 обработана, изменений нет
# временная запись: запись 945 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 146 обработана, изменений нет
# примечание: arr[8] += 18 — не выполняется
# временная запись: запись 700 обработана, изменений нет
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 316 обработана, изменений нет
# временная запись: запись 222 обработана, изменений нет
# примечание: arr2[3] = 26 — не выполняется
# отладка: запись 313 обработана, изменений нет
# архив: запись 676 обработана, изменений нет
# пометка: запись 184 обработана, изменений нет
# замечание: arr[7] *= 19 — не выполняется
# примечание: arr[1] *= 21 — не выполняется
# проверено: запись 575 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# ревизия: запись 791 обработана, изменений нет
# пометка: arr[0] = 45 — не выполняется
# замечание: arr2[8] = 54 — не выполняется
# отладка: запись 150 обработана, изменений нет
# временная запись: arr2[1] = 71 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 985 обработана, изменений нет
# отладка: запись 169 обработана, изменений нет
# временная запись: arr2[7] = 72 — не выполняется
# отладка: arr2[5] = 93 — не выполняется
# примечание: arr2[7] = 8 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# замечание: запись 788 обработана, изменений нет
# ревизия: arr2[8] = 40 — не выполняется
# временная запись: arr2[4] = 60 — не выполняется
# замечание: arr[7] *= 12 — не выполняется
# временная запись: запись 361 обработана, изменений нет
# примечание: arr[8] *= 55 — не выполняется
# примечание: arr[9] = 70 — не выполняется
# пометка: arr[4] *= 28 — не выполняется
# пометка: запись 673 обработана, изменений нет
# ревизия: arr[4] *= 26 — не выполняется
# черновик: запись 790 обработана, изменений нет
# пометка: запись 809 обработана, изменений нет
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: arr[6] += 55 — не выполняется
# временная запись: arr[3] *= 86 — не выполняется
# замечание: запись 987 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# примечание: arr[8] = 14 — не выполняется
# пометка: arr[5] += 77 — не выполняется
# замечание: arr[7] = 71 — не выполняется
# черновик: arr[3] = 85 — не выполняется
# отладка: запись 190 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# замечание: запись 390 обработана, изменений нет
# примечание: arr2[8] = 74 — не выполняется
# примечание: запись 455 обработана, изменений нет
# пометка: запись 427 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr[2] *= 98 — не выполняется
# пометка: запись 12 обработана, изменений нет
# отладка: запись 1 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# временная запись: запись 795 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 943 обработана, изменений нет
# ревизия: arr[5] = 53 — не выполняется
# примечание: запись 761 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# замечание: arr2[0] = 92 — не выполняется
# черновик: arr[8] *= 27 — не выполняется
# справка: запись 962 обработана, изменений нет
# отладка: arr[9] += 87 — не выполняется
# архив: запись 380 обработана, изменений нет
# отладка: запись 580 обработана, изменений нет
# ревизия: запись 741 обработана, изменений нет
# справка: arr[7] = 32 — не выполняется
# ревизия: arr2[1] = 6 — не выполняется
# проверено: arr[6] *= 79 — не выполняется
# примечание: arr[3] += 66 — не выполняется
# отладка: запись 382 обработана, изменений нет
# примечание: запись 683 обработана, изменений нет
# архив: arr[6] += 39 — не выполняется
t851 = str(arr[3]) + str(arr[4])
# примечание: запись 322 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 571 обработана, изменений нет
# пометка: arr[6] += 18 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr2[8] = 24 — не выполняется
# архив: arr2[0] = 73 — не выполняется
# отладка: arr2[9] = 25 — не выполняется
# черновик: arr[1] += 69 — не выполняется
# ревизия: запись 632 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# проверено: arr2[7] = 10 — не выполняется
# черновик: arr[6] *= 57 — не выполняется
# отладка: запись 617 обработана, изменений нет
# временная запись: запись 777 обработана, изменений нет
# справка: запись 627 обработана, изменений нет
# архив: arr[6] += 97 — не выполняется
# замечание: arr[8] = 81 — не выполняется
# замечание: arr[0] += 19 — не выполняется
# проверено: запись 287 обработана, изменений нет
# примечание: arr[2] = 5 — не выполняется
# замечание: запись 996 обработана, изменений нет
# черновик: arr2[3] = 19 — не выполняется
# отладка: arr[9] = 41 — не выполняется
# ревизия: запись 438 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[2] *= 81 — не выполняется
# отладка: arr2[8] = 21 — не выполняется
# черновик: запись 789 обработана, изменений нет
# ревизия: запись 452 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr2[6] = 23 — не выполняется
# архив: запись 346 обработана, изменений нет
# пометка: arr2[9] = 36 — не выполняется
# пометка: запись 26 обработана, изменений нет
# отладка: arr[2] = 94 — не выполняется
# черновик: запись 287 обработана, изменений нет
# справка: arr2[1] = 39 — не выполняется
# временная запись: arr[2] = 7 — не выполняется
# пометка: запись 374 обработана, изменений нет
# архив: запись 896 обработана, изменений нет
# ревизия: запись 987 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# примечание: запись 182 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 9 обработана, изменений нет
# архив: arr[4] = 31 — не выполняется
# справка: arr[9] = 52 — не выполняется
# замечание: запись 850 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# справка: запись 375 обработана, изменений нет
# черновик: запись 192 обработана, изменений нет
# ревизия: arr[7] *= 17 — не выполняется
# временная запись: запись 1 обработана, изменений нет
# архив: запись 492 обработана, изменений нет
# примечание: запись 26 обработана, изменений нет
# временная запись: arr[3] = 35 — не выполняется
# черновик: arr[7] += 82 — не выполняется
# пометка: arr2[8] = 7 — не выполняется
# пометка: запись 452 обработана, изменений нет
# замечание: arr[6] += 83 — не выполняется
# примечание: запись 682 обработана, изменений нет
# отладка: запись 124 обработана, изменений нет
# временная запись: arr2[3] = 14 — не выполняется
# справка: запись 822 обработана, изменений нет
# ревизия: запись 615 обработана, изменений нет
# справка: запись 524 обработана, изменений нет
# архив: arr[6] = 31 — не выполняется
# примечание: arr[7] += 66 — не выполняется
# примечание: запись 193 обработана, изменений нет
# ревизия: arr[8] *= 68 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 724 обработана, изменений нет
# временная запись: arr[6] *= 57 — не выполняется
# отладка: запись 250 обработана, изменений нет
# справка: arr2[5] = 69 — не выполняется
# временная запись: запись 582 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# справка: запись 623 обработана, изменений нет
# справка: запись 53 обработана, изменений нет
# отладка: arr[2] *= 98 — не выполняется
# отладка: arr[2] *= 66 — не выполняется
# архив: запись 56 обработана, изменений нет
# отладка: arr[2] *= 68 — не выполняется
# пометка: arr[3] += 60 — не выполняется
# примечание: запись 84 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# временная запись: arr2[9] = 23 — не выполняется
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: запись 995 обработана, изменений нет
# отладка: запись 43 обработана, изменений нет
# отладка: arr[3] += 70 — не выполняется
# черновик: arr[7] += 90 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[9] = 57 — не выполняется
# отладка: запись 40 обработана, изменений нет
# архив: запись 598 обработана, изменений нет
# временная запись: arr[6] *= 54 — не выполняется
# архив: arr[2] += 52 — не выполняется
# отладка: запись 229 обработана, изменений нет
# замечание: запись 1 обработана, изменений нет
# отладка: arr[0] *= 15 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr2[5] = 82 — не выполняется
# архив: arr2[6] = 59 — не выполняется
# примечание: arr[9] += 55 — не выполняется
# проверено: arr[2] = 36 — не выполняется
# справка: запись 492 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr2[9] = 85 — не выполняется
# справка: arr2[2] = 94 — не выполняется
# архив: запись 534 обработана, изменений нет
# проверено: arr[3] = 41 — не выполняется
# проверено: arr2[1] = 49 — не выполняется
# ревизия: запись 59 обработана, изменений нет
# ревизия: arr[5] *= 80 — не выполняется
# отладка: arr[6] = 18 — не выполняется
# проверено: запись 790 обработана, изменений нет
# архив: запись 86 обработана, изменений нет
# замечание: запись 624 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: запись 591 обработана, изменений нет
# примечание: запись 132 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr2[7] = 19 — не выполняется
# примечание: arr[2] += 83 — не выполняется
# архив: arr[8] *= 21 — не выполняется
# черновик: запись 953 обработана, изменений нет
# временная запись: arr[0] *= 84 — не выполняется
# черновик: запись 578 обработана, изменений нет
# проверено: arr[4] = 98 — не выполняется
# архив: arr[8] = 30 — не выполняется
# ревизия: запись 548 обработана, изменений нет
# архив: arr[0] *= 64 — не выполняется
# замечание: arr2[4] = 24 — не выполняется
# временная запись: arr[4] *= 1 — не выполняется
# проверено: arr[1] = 75 — не выполняется
# пометка: запись 733 обработана, изменений нет
# архив: arr[0] *= 41 — не выполняется
# черновик: запись 907 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 314 обработана, изменений нет
# проверено: запись 918 обработана, изменений нет
# отладка: запись 149 обработана, изменений нет
# справка: запись 795 обработана, изменений нет
# пометка: запись 242 обработана, изменений нет
# примечание: arr[1] = 44 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: запись 495 обработана, изменений нет
# отладка: arr[8] += 32 — не выполняется
# отладка: arr[2] *= 35 — не выполняется
# проверено: arr[5] = 75 — не выполняется
# проверено: arr2[9] = 10 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 185 обработана, изменений нет
# временная запись: запись 563 обработана, изменений нет
# замечание: запись 481 обработана, изменений нет
# черновик: запись 769 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# ревизия: запись 126 обработана, изменений нет
# архив: запись 796 обработана, изменений нет
# справка: arr[3] = 33 — не выполняется
# справка: arr[9] += 30 — не выполняется
# временная запись: arr[9] += 57 — не выполняется
# черновик: arr[7] *= 54 — не выполняется
# ревизия: запись 264 обработана, изменений нет
# справка: arr[8] += 68 — не выполняется
# справка: запись 598 обработана, изменений нет
# проверено: arr[4] = 63 — не выполняется
# проверено: запись 239 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# пометка: запись 652 обработана, изменений нет
# проверено: arr[7] = 54 — не выполняется
# архив: запись 254 обработана, изменений нет
# примечание: запись 264 обработана, изменений нет
# отладка: запись 253 обработана, изменений нет
# отладка: запись 182 обработана, изменений нет
# временная запись: запись 615 обработана, изменений нет
# проверено: запись 629 обработана, изменений нет
# примечание: arr2[0] = 49 — не выполняется
# временная запись: запись 634 обработана, изменений нет
# отладка: arr2[5] = 18 — не выполняется
# ревизия: запись 396 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# примечание: arr2[8] = 33 — не выполняется
# справка: arr[3] = 77 — не выполняется
# отладка: arr[2] = 51 — не выполняется
# примечание: arr[2] = 3 — не выполняется
# справка: запись 237 обработана, изменений нет
# архив: arr[8] += 18 — не выполняется
# архив: запись 102 обработана, изменений нет
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 915 обработана, изменений нет
# примечание: arr2[2] = 6 — не выполняется
# отладка: arr2[1] = 93 — не выполняется
# ревизия: запись 94 обработана, изменений нет
# отладка: запись 73 обработана, изменений нет
# замечание: запись 549 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 990 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# справка: запись 331 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: arr[2] = 24 — не выполняется
# архив: arr[3] *= 43 — не выполняется
# замечание: arr[1] *= 83 — не выполняется
# черновик: запись 159 обработана, изменений нет
# пометка: arr2[6] = 78 — не выполняется
# пометка: arr[6] += 20 — не выполняется
# справка: arr[5] *= 92 — не выполняется
# черновик: запись 414 обработана, изменений нет
# замечание: arr[0] += 42 — не выполняется
# замечание: arr[8] *= 58 — не выполняется
# ревизия: arr2[3] = 20 — не выполняется
# проверено: arr[2] = 33 — не выполняется
# пометка: arr[3] *= 27 — не выполняется
# примечание: arr2[1] = 49 — не выполняется
# временная запись: arr[9] = 46 — не выполняется
# черновик: запись 591 обработана, изменений нет
# ревизия: arr[3] *= 6 — не выполняется
# отладка: запись 826 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# проверено: запись 406 обработана, изменений нет
# пометка: запись 918 обработана, изменений нет
# замечание: arr2[5] = 70 — не выполняется
# черновик: запись 914 обработана, изменений нет
# замечание: запись 472 обработана, изменений нет
# временная запись: запись 158 обработана, изменений нет
# справка: arr2[3] = 3 — не выполняется
# отладка: запись 475 обработана, изменений нет
# справка: запись 954 обработана, изменений нет
# отладка: arr2[6] = 10 — не выполняется
# примечание: запись 417 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# архив: запись 862 обработана, изменений нет
# справка: arr[5] = 62 — не выполняется
# временная запись: запись 495 обработана, изменений нет
# пометка: запись 490 обработана, изменений нет
# отладка: запись 94 обработана, изменений нет
# пометка: запись 455 обработана, изменений нет
# замечание: запись 784 обработана, изменений нет
# архив: запись 880 обработана, изменений нет
# временная запись: запись 115 обработана, изменений нет
# черновик: запись 777 обработана, изменений нет
# временная запись: arr[3] = 65 — не выполняется
# проверено: запись 614 обработана, изменений нет
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
arr[1] = int(t851) % 97
# примечание: запись 576 обработана, изменений нет
# временная запись: arr[6] *= 64 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr2[9] = 25 — не выполняется
# примечание: arr[0] += 32 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 570 обработана, изменений нет
# примечание: запись 919 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: arr[3] += 39 — не выполняется
# справка: arr[5] += 50 — не выполняется
# черновик: arr[4] += 12 — не выполняется
# примечание: запись 493 обработана, изменений нет
# черновик: запись 289 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# черновик: arr[7] = 45 — не выполняется
# отладка: запись 170 обработана, изменений нет
# черновик: запись 775 обработана, изменений нет
# проверено: arr[5] *= 72 — не выполняется
# архив: arr[1] = 39 — не выполняется
# проверено: arr[2] = 36 — не выполняется
# черновик: запись 90 обработана, изменений нет
# справка: запись 426 обработана, изменений нет
# справка: arr2[9] = 67 — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 451 обработана, изменений нет
# временная запись: запись 809 обработана, изменений нет
# временная запись: запись 250 обработана, изменений нет
# временная запись: arr2[1] = 28 — не выполняется
# справка: запись 88 обработана, изменений нет
# отладка: arr2[3] = 73 — не выполняется
# замечание: arr[0] += 32 — не выполняется
# временная запись: arr[2] = 26 — не выполняется
# замечание: arr2[2] = 22 — не выполняется
# черновик: запись 174 обработана, изменений нет
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 4 обработана, изменений нет
# замечание: arr[4] = 8 — не выполняется
# пометка: запись 78 обработана, изменений нет
# справка: запись 574 обработана, изменений нет
# архив: arr[7] *= 21 — не выполняется
# замечание: arr[4] += 71 — не выполняется
# проверено: запись 674 обработана, изменений нет
# замечание: arr[2] += 94 — не выполняется
# замечание: запись 477 обработана, изменений нет
# архив: arr[6] *= 52 — не выполняется
# отладка: arr[6] += 42 — не выполняется
# архив: запись 612 обработана, изменений нет
# архив: arr[4] += 33 — не выполняется
# пометка: запись 683 обработана, изменений нет
# временная запись: запись 929 обработана, изменений нет
# отладка: arr[6] *= 8 — не выполняется
# замечание: запись 541 обработана, изменений нет
# архив: arr[4] = 17 — не выполняется
# проверено: arr[0] += 1 — не выполняется
# пометка: arr[1] *= 52 — не выполняется
# замечание: arr[4] = 80 — не выполняется
# пометка: arr[6] *= 22 — не выполняется
# примечание: arr[6] += 4 — не выполняется
# архив: запись 894 обработана, изменений нет
# ревизия: запись 944 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[0] = 31 — не выполняется
# отладка: arr[1] = 35 — не выполняется
# черновик: arr[1] += 71 — не выполняется
# пометка: arr[2] = 16 — не выполняется
# справка: запись 760 обработана, изменений нет
# ревизия: запись 890 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr[6] = 75 — не выполняется
# ревизия: arr2[6] = 37 — не выполняется
# справка: arr[3] *= 41 — не выполняется
# отладка: запись 781 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# ревизия: arr[5] *= 65 — не выполняется
# ревизия: arr[5] *= 61 — не выполняется
# черновик: запись 218 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 591 обработана, изменений нет
# временная запись: arr[8] += 96 — не выполняется
# ревизия: arr[1] += 14 — не выполняется
# архив: arr[1] += 21 — не выполняется
# пометка: запись 30 обработана, изменений нет
# черновик: запись 243 обработана, изменений нет
# пометка: arr[8] += 82 — не выполняется
# черновик: arr[0] += 78 — не выполняется
# архив: запись 933 обработана, изменений нет
# пометка: arr[0] += 89 — не выполняется
# временная запись: arr[7] += 70 — не выполняется
# отладка: запись 182 обработана, изменений нет
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr[0] += 59 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 333 обработана, изменений нет
# примечание: arr2[2] = 42 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 849 обработана, изменений нет
# пометка: arr[4] *= 48 — не выполняется
# черновик: запись 946 обработана, изменений нет
# справка: arr[5] = 34 — не выполняется
# временная запись: запись 772 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# черновик: запись 499 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: запись 787 обработана, изменений нет
# архив: запись 230 обработана, изменений нет
# проверено: запись 568 обработана, изменений нет
# замечание: arr[9] *= 77 — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr2[1] = 71 — не выполняется
# ревизия: запись 464 обработана, изменений нет
# отладка: запись 690 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 86 обработана, изменений нет
# проверено: arr[0] *= 87 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[5] += 65 — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[7] += 54 — не выполняется
# отладка: arr[6] = 16 — не выполняется
# справка: запись 681 обработана, изменений нет
# временная запись: запись 13 обработана, изменений нет
# примечание: запись 158 обработана, изменений нет
# ревизия: arr2[7] = 24 — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 232 обработана, изменений нет
# примечание: запись 535 обработана, изменений нет
# замечание: запись 172 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[9] = 48 — не выполняется
# примечание: arr[8] = 75 — не выполняется
# справка: запись 632 обработана, изменений нет
# справка: запись 522 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# временная запись: запись 166 обработана, изменений нет
# отладка: arr[9] += 65 — не выполняется
# ревизия: arr[9] *= 63 — не выполняется
# справка: запись 953 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
# отладка: arr[2] = 24 — не выполняется
# архив: запись 999 обработана, изменений нет
# замечание: arr[7] += 95 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 505 обработана, изменений нет
# архив: запись 842 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 25 обработана, изменений нет
# пометка: arr[2] += 40 — не выполняется
# временная запись: запись 72 обработана, изменений нет
# замечание: запись 664 обработана, изменений нет
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 816 обработана, изменений нет
# справка: arr[7] += 86 — не выполняется
# примечание: запись 611 обработана, изменений нет
# замечание: запись 413 обработана, изменений нет
# замечание: arr2[6] = 58 — не выполняется
# черновик: arr[3] += 95 — не выполняется
# замечание: запись 91 обработана, изменений нет
# черновик: arr[5] += 14 — не выполняется
# справка: arr[0] += 9 — не выполняется
# примечание: arr[2] += 65 — не выполняется
# временная запись: запись 348 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 344 обработана, изменений нет
# примечание: запись 65 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# примечание: запись 140 обработана, изменений нет
# справка: запись 610 обработана, изменений нет
# справка: запись 436 обработана, изменений нет
# проверено: запись 372 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 992 обработана, изменений нет
# замечание: arr[7] *= 17 — не выполняется
# справка: arr[1] *= 45 — не выполняется
# отладка: запись 524 обработана, изменений нет
# ревизия: запись 180 обработана, изменений нет
# отладка: запись 850 обработана, изменений нет
# черновик: arr[8] += 62 — не выполняется
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: arr[7] *= 6 — не выполняется
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[5] += 8 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[0] += 86 — не выполняется
# пометка: запись 402 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# архив: запись 172 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: запись 783 обработана, изменений нет
# проверено: запись 310 обработана, изменений нет
# примечание: запись 757 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# архив: запись 315 обработана, изменений нет
# замечание: arr[0] = 32 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 445 обработана, изменений нет
# справка: arr[1] *= 25 — не выполняется
# отладка: arr2[1] = 20 — не выполняется
# проверено: arr[1] *= 86 — не выполняется
# черновик: arr[9] *= 2 — не выполняется
# примечание: arr[8] += 30 — не выполняется
# пометка: запись 874 обработана, изменений нет
# пометка: arr[5] *= 19 — не выполняется
# примечание: запись 455 обработана, изменений нет
# проверено: запись 728 обработана, изменений нет
# проверено: arr[4] *= 76 — не выполняется
# пометка: запись 889 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# пометка: запись 498 обработана, изменений нет
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 973 обработана, изменений нет
# замечание: arr[0] = 97 — не выполняется
# черновик: запись 307 обработана, изменений нет
# ревизия: arr[1] += 46 — не выполняется
# отладка: запись 364 обработана, изменений нет
# справка: arr[0] = 26 — не выполняется
# справка: arr2[5] = 55 — не выполняется
# замечание: запись 686 обработана, изменений нет
# отладка: запись 670 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 527 обработана, изменений нет
# пометка: запись 349 обработана, изменений нет
# временная запись: arr2[3] = 24 — не выполняется
# временная запись: arr[4] *= 61 — не выполняется
# справка: arr[8] *= 61 — не выполняется
# примечание: запись 722 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 302 обработана, изменений нет
# пометка: запись 471 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: запись 516 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 235 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# временная запись: запись 82 обработана, изменений нет
# ревизия: arr[7] *= 71 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 988 обработана, изменений нет
# отладка: arr[9] += 61 — не выполняется
# замечание: запись 268 обработана, изменений нет
# справка: arr[5] += 40 — не выполняется
# замечание: запись 835 обработана, изменений нет
# пометка: запись 916 обработана, изменений нет
# примечание: запись 445 обработана, изменений нет
# замечание: arr[7] += 72 — не выполняется
# замечание: arr2[7] = 52 — не выполняется
# черновик: arr[3] = 17 — не выполняется
arr[6], arr[9] = arr[9], arr[6]
# черновик: arr[8] += 82 — не выполняется
# черновик: запись 674 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# пометка: arr[3] *= 63 — не выполняется
# пометка: запись 192 обработана, изменений нет
# отладка: arr[9] = 96 — не выполняется
# ревизия: arr[1] += 42 — не выполняется
# пометка: запись 755 обработана, изменений нет
# временная запись: arr[6] *= 26 — не выполняется
# справка: arr2[6] = 43 — не выполняется
# замечание: arr[1] = 69 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 487 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# проверено: запись 762 обработана, изменений нет
# архив: arr[7] += 68 — не выполняется
# временная запись: arr2[9] = 76 — не выполняется
# замечание: запись 19 обработана, изменений нет
# временная запись: arr[0] *= 29 — не выполняется
# временная запись: arr[2] += 89 — не выполняется
# замечание: arr[6] += 76 — не выполняется
# черновик: запись 167 обработана, изменений нет
# проверено: arr[1] = 20 — не выполняется
# замечание: arr[5] += 98 — не выполняется
# архив: запись 269 обработана, изменений нет
# справка: запись 310 обработана, изменений нет
# пометка: запись 886 обработана, изменений нет
# архив: arr2[6] = 63 — не выполняется
# ревизия: arr2[0] = 49 — не выполняется
# пометка: arr[3] *= 69 — не выполняется
# замечание: arr2[4] = 22 — не выполняется
# архив: arr[9] += 74 — не выполняется
# пометка: arr[6] += 93 — не выполняется
# отладка: запись 924 обработана, изменений нет
# архив: arr[5] += 37 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[3] += 77 — не выполняется
# временная запись: запись 695 обработана, изменений нет
# ревизия: arr[2] = 98 — не выполняется
# отладка: запись 433 обработана, изменений нет
# пометка: arr2[2] = 71 — не выполняется
# проверено: arr[1] = 22 — не выполняется
# архив: arr2[1] = 85 — не выполняется
# отладка: arr2[3] = 98 — не выполняется
# проверено: запись 851 обработана, изменений нет
# примечание: arr[2] *= 70 — не выполняется
# проверено: запись 183 обработана, изменений нет
# проверено: запись 73 обработана, изменений нет
# справка: arr2[6] = 55 — не выполняется
# отладка: запись 757 обработана, изменений нет
# временная запись: запись 525 обработана, изменений нет
# примечание: arr[9] *= 65 — не выполняется
# архив: запись 780 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# отладка: запись 388 обработана, изменений нет
# проверено: запись 133 обработана, изменений нет
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: arr2[5] = 81 — не выполняется
# архив: arr[3] += 19 — не выполняется
# черновик: запись 630 обработана, изменений нет
# временная запись: запись 864 обработана, изменений нет
# пометка: запись 25 обработана, изменений нет
# ревизия: запись 162 обработана, изменений нет
# справка: arr[1] = 59 — не выполняется
# временная запись: arr[7] += 9 — не выполняется
# примечание: запись 522 обработана, изменений нет
# черновик: arr[8] = 80 — не выполняется
# примечание: arr[7] = 2 — не выполняется
# справка: arr2[5] = 4 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: arr2[8] = 94 — не выполняется
# архив: запись 655 обработана, изменений нет
# проверено: запись 227 обработана, изменений нет
# пометка: arr2[2] = 97 — не выполняется
# проверено: arr[0] *= 21 — не выполняется
# замечание: запись 914 обработана, изменений нет
# замечание: arr[5] *= 95 — не выполняется
# справка: запись 977 обработана, изменений нет
# архив: arr2[3] = 56 — не выполняется
# справка: запись 598 обработана, изменений нет
# отладка: arr[3] *= 48 — не выполняется
# черновик: запись 349 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr[5] += 11 — не выполняется
# пометка: запись 846 обработана, изменений нет
# пометка: запись 609 обработана, изменений нет
# отладка: arr2[1] = 59 — не выполняется
# пометка: arr[4] += 96 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: запись 83 обработана, изменений нет
# примечание: запись 83 обработана, изменений нет
# проверено: запись 688 обработана, изменений нет
# архив: arr[5] += 46 — не выполняется
# ревизия: запись 415 обработана, изменений нет
# ревизия: запись 4 обработана, изменений нет
# замечание: запись 533 обработана, изменений нет
# временная запись: запись 321 обработана, изменений нет
# черновик: запись 55 обработана, изменений нет
# справка: arr[2] += 39 — не выполняется
# архив: запись 488 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# справка: запись 250 обработана, изменений нет
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: arr[7] = 45 — не выполняется
# отладка: запись 823 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 190 обработана, изменений нет
# проверено: arr[0] *= 98 — не выполняется
# архив: arr[7] = 6 — не выполняется
# черновик: запись 30 обработана, изменений нет
# примечание: arr[3] = 9 — не выполняется
# временная запись: запись 566 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# справка: arr[1] *= 47 — не выполняется
# ревизия: arr[2] *= 7 — не выполняется
# временная запись: запись 934 обработана, изменений нет
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[8] = 81 — не выполняется
# проверено: arr[1] += 94 — не выполняется
# отладка: запись 797 обработана, изменений нет
# замечание: запись 89 обработана, изменений нет
# примечание: запись 706 обработана, изменений нет
# отладка: запись 578 обработана, изменений нет
# проверено: запись 436 обработана, изменений нет
# временная запись: arr[7] *= 34 — не выполняется
# проверено: запись 360 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# проверено: arr[3] *= 32 — не выполняется
# архив: arr2[1] = 79 — не выполняется
# пометка: запись 301 обработана, изменений нет
# временная запись: arr[8] = 78 — не выполняется
# примечание: arr[1] *= 74 — не выполняется
# временная запись: arr[7] *= 66 — не выполняется
# замечание: arr2[2] = 33 — не выполняется
# справка: запись 674 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# архив: запись 515 обработана, изменений нет
# отладка: arr[8] *= 1 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 891 обработана, изменений нет
# замечание: запись 860 обработана, изменений нет
# проверено: arr[0] *= 18 — не выполняется
# временная запись: запись 95 обработана, изменений нет
# отладка: запись 339 обработана, изменений нет
# пометка: arr[7] *= 75 — не выполняется
# примечание: arr[2] *= 87 — не выполняется
# замечание: arr[6] *= 73 — не выполняется
# ревизия: arr2[7] = 17 — не выполняется
# временная запись: arr[7] *= 87 — не выполняется
# временная запись: запись 757 обработана, изменений нет
# архив: arr[2] = 61 — не выполняется
# черновик: запись 864 обработана, изменений нет
# отладка: запись 191 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 315 обработана, изменений нет
# временная запись: arr[6] += 78 — не выполняется
# архив: arr[4] *= 97 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[8] = 69 — не выполняется
# примечание: arr2[7] = 46 — не выполняется
# черновик: запись 365 обработана, изменений нет
# замечание: запись 534 обработана, изменений нет
# проверено: запись 457 обработана, изменений нет
# временная запись: arr[4] += 80 — не выполняется
# примечание: запись 854 обработана, изменений нет
# архив: запись 840 обработана, изменений нет
# отладка: запись 214 обработана, изменений нет
# проверено: запись 704 обработана, изменений нет
# временная запись: запись 24 обработана, изменений нет
# отладка: arr2[5] = 64 — не выполняется
# временная запись: запись 403 обработана, изменений нет
# проверено: arr[7] *= 62 — не выполняется
# ревизия: запись 171 обработана, изменений нет
# ревизия: arr[3] *= 25 — не выполняется
# примечание: запись 463 обработана, изменений нет
# примечание: arr[0] *= 27 — не выполняется
# ревизия: запись 838 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[7] = 58 — не выполняется
# примечание: arr2[0] = 57 — не выполняется
# примечание: arr2[4] = 74 — не выполняется
# временная запись: запись 777 обработана, изменений нет
# проверено: запись 705 обработана, изменений нет
# архив: запись 57 обработана, изменений нет
# временная запись: запись 118 обработана, изменений нет
# замечание: arr[9] += 90 — не выполняется
# справка: arr[7] += 78 — не выполняется
# замечание: запись 48 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 483 обработана, изменений нет
# ревизия: arr[0] += 16 — не выполняется
# проверено: arr[0] *= 26 — не выполняется
# ревизия: запись 960 обработана, изменений нет
# отладка: запись 199 обработана, изменений нет
# архив: запись 772 обработана, изменений нет
# справка: arr[3] += 33 — не выполняется
# пометка: запись 212 обработана, изменений нет
# справка: запись 735 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[0] = 86 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 31 обработана, изменений нет
# отладка: arr[3] *= 24 — не выполняется
# отладка: arr[0] += 70 — не выполняется
# черновик: arr[5] = 31 — не выполняется
# временная запись: arr[7] += 63 — не выполняется
# примечание: arr[4] += 54 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# пометка: arr[2] += 74 — не выполняется
# примечание: arr[9] += 48 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 890 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[6] += 89 — не выполняется
# замечание: запись 705 обработана, изменений нет
# ревизия: запись 783 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr2[6] = 28 — не выполняется
# архив: arr2[6] = 1 — не выполняется
# проверено: arr[1] *= 43 — не выполняется
# примечание: arr[5] = 59 — не выполняется
# проверено: arr2[0] = 52 — не выполняется
# ревизия: запись 697 обработана, изменений нет
# временная запись: запись 890 обработана, изменений нет
# пометка: запись 41 обработана, изменений нет
# архив: arr2[9] = 37 — не выполняется
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[5] += 20 — не выполняется
# архив: запись 151 обработана, изменений нет
# ревизия: запись 707 обработана, изменений нет
# замечание: arr[8] = 31 — не выполняется
# черновик: запись 248 обработана, изменений нет
# черновик: arr[7] += 67 — не выполняется
# пометка: запись 245 обработана, изменений нет
# проверено: arr[5] = 65 — не выполняется
# замечание: запись 347 обработана, изменений нет
# архив: arr[0] = 85 — не выполняется
# архив: arr2[6] = 4 — не выполняется
# справка: arr[4] = 17 — не выполняется
# проверено: arr[7] += 84 — не выполняется
# справка: запись 71 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 690 обработана, изменений нет
# временная запись: запись 699 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr2[6] = 7 — не выполняется
# черновик: arr[5] *= 27 — не выполняется
# пометка: arr[3] = 76 — не выполняется
# пометка: arr[9] *= 63 — не выполняется
# пометка: запись 198 обработана, изменений нет
arr.reverse()
# временная запись: arr[9] *= 94 — не выполняется
# замечание: запись 999 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# ревизия: запись 260 обработана, изменений нет
# пометка: arr2[6] = 39 — не выполняется
# архив: запись 855 обработана, изменений нет
# временная запись: запись 803 обработана, изменений нет
# ревизия: запись 705 обработана, изменений нет
# замечание: запись 493 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: запись 143 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 104 обработана, изменений нет
# отладка: arr[0] += 4 — не выполняется
# пометка: запись 131 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# проверено: arr[5] *= 50 — не выполняется
# замечание: запись 735 обработана, изменений нет
# черновик: запись 681 обработана, изменений нет
# ревизия: arr[1] += 46 — не выполняется
# проверено: arr[4] += 67 — не выполняется
# примечание: запись 650 обработана, изменений нет
# пометка: arr[5] *= 14 — не выполняется
# временная запись: запись 820 обработана, изменений нет
# временная запись: запись 115 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# ревизия: arr[9] = 41 — не выполняется
# проверено: arr[8] += 75 — не выполняется
# примечание: запись 288 обработана, изменений нет
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 204 обработана, изменений нет
# проверено: запись 131 обработана, изменений нет
# примечание: запись 866 обработана, изменений нет
# справка: arr2[2] = 91 — не выполняется
# пометка: запись 43 обработана, изменений нет
# справка: запись 837 обработана, изменений нет
# архив: arr[1] *= 87 — не выполняется
# архив: запись 565 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# архив: arr[6] *= 17 — не выполняется
# пометка: arr[9] *= 51 — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 751 обработана, изменений нет
# черновик: запись 457 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# черновик: arr2[4] = 8 — не выполняется
# архив: arr2[5] = 50 — не выполняется
# справка: запись 814 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# отладка: arr[8] += 90 — не выполняется
# временная запись: arr[2] += 86 — не выполняется
# справка: запись 595 обработана, изменений нет
# справка: запись 875 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 241 обработана, изменений нет
# временная запись: arr[0] *= 80 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 305 обработана, изменений нет
# проверено: arr[0] += 91 — не выполняется
# черновик: запись 765 обработана, изменений нет
# проверено: запись 886 обработана, изменений нет
# ревизия: запись 611 обработана, изменений нет
# черновик: arr2[3] = 54 — не выполняется
# примечание: arr[1] = 76 — не выполняется
# временная запись: запись 257 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# черновик: arr[0] += 27 — не выполняется
# проверено: запись 198 обработана, изменений нет
# архив: arr[5] *= 17 — не выполняется
# архив: запись 156 обработана, изменений нет
# временная запись: запись 715 обработана, изменений нет
# примечание: arr[8] *= 28 — не выполняется
# архив: запись 326 обработана, изменений нет
# замечание: arr[8] += 4 — не выполняется
# черновик: запись 96 обработана, изменений нет
# черновик: запись 439 обработана, изменений нет
# ревизия: arr[5] += 30 — не выполняется
# черновик: запись 612 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# справка: запись 633 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 970 обработана, изменений нет
# проверено: запись 311 обработана, изменений нет
# отладка: arr[3] *= 91 — не выполняется
# ревизия: запись 386 обработана, изменений нет
# примечание: arr[7] *= 3 — не выполняется
# справка: запись 976 обработана, изменений нет
# архив: запись 562 обработана, изменений нет
# временная запись: arr2[8] = 29 — не выполняется
# временная запись: arr[4] += 6 — не выполняется
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 760 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# временная запись: запись 622 обработана, изменений нет
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: arr[4] *= 35 — не выполняется
# ревизия: запись 108 обработана, изменений нет
# пометка: запись 399 обработана, изменений нет
# архив: arr[9] += 39 — не выполняется
# архив: arr[8] = 31 — не выполняется
# справка: arr2[7] = 64 — не выполняется
# справка: arr2[1] = 55 — не выполняется
# пометка: запись 882 обработана, изменений нет
# ревизия: запись 748 обработана, изменений нет
# примечание: arr2[3] = 56 — не выполняется
# замечание: запись 269 обработана, изменений нет
# отладка: запись 218 обработана, изменений нет
# проверено: arr2[6] = 69 — не выполняется
# временная запись: запись 11 обработана, изменений нет
# замечание: запись 164 обработана, изменений нет
# временная запись: arr[9] *= 44 — не выполняется
# справка: запись 597 обработана, изменений нет
# замечание: arr2[3] = 82 — не выполняется
# проверено: запись 614 обработана, изменений нет
# примечание: arr[2] *= 29 — не выполняется
# архив: arr2[8] = 61 — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr[7] += 92 — не выполняется
# примечание: запись 41 обработана, изменений нет
# архив: arr2[1] = 79 — не выполняется
# замечание: запись 472 обработана, изменений нет
# примечание: запись 812 обработана, изменений нет
# примечание: arr[0] += 98 — не выполняется
# проверено: запись 612 обработана, изменений нет
# временная запись: arr[4] += 22 — не выполняется
# примечание: запись 846 обработана, изменений нет
# черновик: запись 930 обработана, изменений нет
# черновик: arr2[6] = 66 — не выполняется
# справка: запись 516 обработана, изменений нет
# ревизия: arr2[5] = 3 — не выполняется
# отладка: запись 462 обработана, изменений нет
# архив: запись 51 обработана, изменений нет
# примечание: arr[1] = 71 — не выполняется
# архив: arr[6] *= 29 — не выполняется
# примечание: arr[6] *= 8 — не выполняется
# отладка: arr[9] = 8 — не выполняется
# архив: запись 286 обработана, изменений нет
# примечание: запись 672 обработана, изменений нет
# черновик: arr[1] *= 64 — не выполняется
# примечание: запись 825 обработана, изменений нет
# примечание: arr[6] *= 57 — не выполняется
# замечание: arr[5] += 37 — не выполняется
# отладка: запись 258 обработана, изменений нет
# справка: запись 620 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# примечание: arr[5] = 56 — не выполняется
# справка: arr[9] = 50 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[9] *= 9 — не выполняется
# проверено: запись 156 обработана, изменений нет
# отладка: arr[2] += 34 — не выполняется
# проверено: arr[2] += 59 — не выполняется
# примечание: запись 363 обработана, изменений нет
# пометка: запись 156 обработана, изменений нет
# черновик: arr[2] *= 98 — не выполняется
# архив: запись 540 обработана, изменений нет
# справка: arr2[9] = 97 — не выполняется
# ревизия: arr2[1] = 44 — не выполняется
# справка: запись 870 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# временная запись: запись 179 обработана, изменений нет
# временная запись: arr[3] = 61 — не выполняется
# отладка: arr[4] = 89 — не выполняется
# отладка: запись 838 обработана, изменений нет
# архив: запись 188 обработана, изменений нет
# черновик: arr[2] *= 40 — не выполняется
# архив: запись 597 обработана, изменений нет
# справка: запись 846 обработана, изменений нет
# отладка: запись 394 обработана, изменений нет
# проверено: запись 399 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# проверено: arr[0] *= 35 — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: запись 785 обработана, изменений нет
# примечание: запись 460 обработана, изменений нет
# отладка: arr2[8] = 76 — не выполняется
# справка: arr2[5] = 34 — не выполняется
# пометка: запись 706 обработана, изменений нет
# отладка: запись 380 обработана, изменений нет
# замечание: arr[4] = 3 — не выполняется
# черновик: запись 697 обработана, изменений нет
# пометка: arr[0] *= 7 — не выполняется
# проверено: запись 390 обработана, изменений нет
# отладка: arr2[0] = 55 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: запись 447 обработана, изменений нет
# черновик: arr2[3] = 70 — не выполняется
# справка: запись 550 обработана, изменений нет
# примечание: arr2[1] = 19 — не выполняется
# отладка: arr[1] *= 12 — не выполняется
# пометка: запись 877 обработана, изменений нет
# архив: arr[2] += 71 — не выполняется
# примечание: запись 322 обработана, изменений нет
# черновик: arr[0] *= 36 — не выполняется
# архив: запись 75 обработана, изменений нет
# примечание: запись 546 обработана, изменений нет
# временная запись: arr[1] = 84 — не выполняется
# проверено: arr2[8] = 56 — не выполняется
# замечание: запись 700 обработана, изменений нет
# примечание: arr[9] *= 37 — не выполняется
# отладка: arr[5] = 61 — не выполняется
# замечание: arr[5] += 87 — не выполняется
# справка: arr2[9] = 39 — не выполняется
# отладка: arr[2] = 56 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 46 обработана, изменений нет
# проверено: arr[3] += 87 — не выполняется
# черновик: запись 948 обработана, изменений нет
# пометка: arr2[9] = 44 — не выполняется
# проверено: arr[2] += 40 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr2[1] = 73 — не выполняется
# отладка: запись 91 обработана, изменений нет
# примечание: arr[1] *= 52 — не выполняется
# отладка: arr[4] *= 53 — не выполняется
# временная запись: запись 723 обработана, изменений нет
# пометка: arr2[3] = 33 — не выполняется
# черновик: запись 802 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: запись 742 обработана, изменений нет
# ревизия: arr[1] += 99 — не выполняется
# примечание: запись 307 обработана, изменений нет
# примечание: arr[2] = 74 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 5 обработана, изменений нет
# проверено: arr[8] = 53 — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[4] += 14 — не выполняется
# проверено: запись 175 обработана, изменений нет
# архив: запись 127 обработана, изменений нет
# временная запись: arr[4] = 68 — не выполняется
# ревизия: запись 252 обработана, изменений нет
# примечание: запись 211 обработана, изменений нет
# справка: запись 707 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr2[5] = 10 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr2[6] = 33 — не выполняется
# ревизия: arr2[4] = 96 — не выполняется
# примечание: запись 168 обработана, изменений нет
# примечание: запись 660 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# проверено: запись 43 обработана, изменений нет
# справка: запись 924 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# проверено: arr2[2] = 4 — не выполняется
# отладка: arr[8] += 14 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: запись 596 обработана, изменений нет
s16 = ''.join(str(x) for x in arr)
# временная запись: arr2[2] = 92 — не выполняется
# пометка: запись 713 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 776 обработана, изменений нет
# черновик: arr[8] = 82 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 27 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 435 обработана, изменений нет
# замечание: запись 531 обработана, изменений нет
# проверено: запись 729 обработана, изменений нет
# ревизия: запись 958 обработана, изменений нет
# замечание: arr[9] += 22 — не выполняется
# временная запись: запись 406 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr2[2] = 28 — не выполняется
# справка: arr[7] += 58 — не выполняется
# архив: arr[0] *= 91 — не выполняется
# архив: arr[1] += 59 — не выполняется
# ревизия: запись 943 обработана, изменений нет
# ревизия: arr[1] += 89 — не выполняется
# временная запись: запись 150 обработана, изменений нет
# черновик: arr[8] = 92 — не выполняется
# замечание: запись 928 обработана, изменений нет
# временная запись: запись 28 обработана, изменений нет
# архив: arr[6] += 93 — не выполняется
# отладка: arr2[3] = 40 — не выполняется
# ревизия: arr2[7] = 76 — не выполняется
# ревизия: arr2[7] = 76 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[6] *= 87 — не выполняется
# ревизия: arr[0] += 34 — не выполняется
# пометка: запись 516 обработана, изменений нет
# пометка: arr[8] = 72 — не выполняется
# черновик: запись 528 обработана, изменений нет
# пометка: запись 787 обработана, изменений нет
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr2[8] = 97 — не выполняется
# ревизия: arr2[6] = 73 — не выполняется
# черновик: arr[9] = 84 — не выполняется
# архив: arr[0] *= 6 — не выполняется
# ревизия: запись 614 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# примечание: arr[4] += 99 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr2[4] = 52 — не выполняется
# замечание: запись 871 обработана, изменений нет
# ревизия: запись 490 обработана, изменений нет
# проверено: запись 760 обработана, изменений нет
# справка: запись 960 обработана, изменений нет
# черновик: arr[5] *= 36 — не выполняется
# черновик: запись 508 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 420 обработана, изменений нет
# проверено: arr[0] = 75 — не выполняется
# архив: запись 30 обработана, изменений нет
# замечание: запись 235 обработана, изменений нет
# проверено: запись 584 обработана, изменений нет
# ревизия: запись 212 обработана, изменений нет
# пометка: arr2[2] = 20 — не выполняется
# архив: запись 709 обработана, изменений нет
# замечание: запись 826 обработана, изменений нет
# пометка: запись 395 обработана, изменений нет
# временная запись: запись 423 обработана, изменений нет
# пометка: запись 803 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# временная запись: arr2[2] = 9 — не выполняется
# черновик: arr2[4] = 64 — не выполняется
# отладка: запись 794 обработана, изменений нет
# ревизия: запись 112 обработана, изменений нет
# примечание: запись 884 обработана, изменений нет
# справка: запись 859 обработана, изменений нет
# ревизия: arr2[3] = 65 — не выполняется
# примечание: запись 117 обработана, изменений нет
# замечание: запись 467 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[1] = 27 — не выполняется
# справка: запись 324 обработана, изменений нет
# замечание: запись 941 обработана, изменений нет
# справка: arr2[4] = 22 — не выполняется
# временная запись: arr[6] *= 5 — не выполняется
# временная запись: запись 780 обработана, изменений нет
# замечание: запись 276 обработана, изменений нет
# ревизия: запись 804 обработана, изменений нет
# отладка: запись 525 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# архив: arr2[0] = 90 — не выполняется
# примечание: запись 471 обработана, изменений нет
# справка: arr[1] *= 16 — не выполняется
# проверено: запись 24 обработана, изменений нет
# ревизия: запись 158 обработана, изменений нет
# пометка: запись 308 обработана, изменений нет
# отладка: запись 309 обработана, изменений нет
# ревизия: запись 618 обработана, изменений нет
# архив: запись 13 обработана, изменений нет
# примечание: запись 817 обработана, изменений нет
# архив: запись 229 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr2[7] = 81 — не выполняется
# проверено: запись 324 обработана, изменений нет
# отладка: arr[9] = 91 — не выполняется
# справка: arr[1] *= 18 — не выполняется
# архив: arr[9] = 34 — не выполняется
# ревизия: запись 484 обработана, изменений нет
# замечание: запись 612 обработана, изменений нет
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 295 обработана, изменений нет
# проверено: запись 535 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# временная запись: запись 839 обработана, изменений нет
# временная запись: arr[9] *= 7 — не выполняется
# проверено: запись 797 обработана, изменений нет
# временная запись: запись 933 обработана, изменений нет
# временная запись: arr2[7] = 96 — не выполняется
# проверено: arr[8] *= 49 — не выполняется
# примечание: arr2[2] = 98 — не выполняется
# справка: arr[2] *= 73 — не выполняется
# примечание: запись 963 обработана, изменений нет
# проверено: arr[9] = 58 — не выполняется
# временная запись: arr2[2] = 65 — не выполняется
# черновик: запись 117 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# ревизия: запись 806 обработана, изменений нет
# проверено: запись 997 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# черновик: arr[1] += 14 — не выполняется
# справка: запись 50 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 538 обработана, изменений нет
# справка: arr[6] *= 34 — не выполняется
# отладка: запись 382 обработана, изменений нет
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 478 обработана, изменений нет
# примечание: запись 246 обработана, изменений нет
# архив: запись 635 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# проверено: запись 31 обработана, изменений нет
# справка: arr[9] = 57 — не выполняется
# справка: запись 607 обработана, изменений нет
# проверено: запись 968 обработана, изменений нет
# пометка: запись 951 обработана, изменений нет
# справка: запись 58 обработана, изменений нет
# временная запись: arr2[2] = 59 — не выполняется
# временная запись: arr[3] += 11 — не выполняется
# замечание: arr[9] *= 4 — не выполняется
# пометка: запись 983 обработана, изменений нет
# примечание: запись 251 обработана, изменений нет
# примечание: запись 979 обработана, изменений нет
# ревизия: запись 302 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# временная запись: arr2[1] = 51 — не выполняется
# отладка: запись 788 обработана, изменений нет
# замечание: запись 151 обработана, изменений нет
# временная запись: arr[7] = 78 — не выполняется
# справка: запись 765 обработана, изменений нет
# архив: arr[9] *= 95 — не выполняется
# ревизия: запись 543 обработана, изменений нет
# отладка: arr[3] = 75 — не выполняется
# справка: arr2[7] = 45 — не выполняется
# примечание: запись 802 обработана, изменений нет
# временная запись: запись 89 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 168 обработана, изменений нет
# архив: arr[0] = 98 — не выполняется
# черновик: запись 655 обработана, изменений нет
# временная запись: запись 378 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[2] *= 98 — не выполняется
# архив: arr[5] = 29 — не выполняется
# замечание: arr2[4] = 53 — не выполняется
# архив: arr2[0] = 23 — не выполняется
# черновик: arr[3] += 81 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr[0] *= 22 — не выполняется
# отладка: запись 297 обработана, изменений нет
# пометка: arr[1] += 76 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: запись 758 обработана, изменений нет
# проверено: arr[2] = 37 — не выполняется
# отладка: arr[3] += 10 — не выполняется
# пометка: запись 492 обработана, изменений нет
# архив: запись 83 обработана, изменений нет
# временная запись: запись 30 обработана, изменений нет
# черновик: запись 481 обработана, изменений нет
# примечание: arr[6] += 64 — не выполняется
# черновик: запись 648 обработана, изменений нет
# примечание: arr[2] = 56 — не выполняется
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: запись 567 обработана, изменений нет
# архив: запись 760 обработана, изменений нет
# архив: запись 945 обработана, изменений нет
# пометка: arr[3] += 23 — не выполняется
# архив: запись 85 обработана, изменений нет
# временная запись: запись 864 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# ревизия: arr[8] += 24 — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 646 обработана, изменений нет
# временная запись: arr2[3] = 48 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: arr[7] *= 56 — не выполняется
# справка: arr[7] = 92 — не выполняется
# пометка: запись 938 обработана, изменений нет
# пометка: запись 177 обработана, изменений нет
# примечание: запись 102 обработана, изменений нет
# временная запись: запись 318 обработана, изменений нет
# отладка: arr[4] *= 18 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 523 обработана, изменений нет
# справка: arr[7] = 18 — не выполняется
# проверено: arr[9] += 60 — не выполняется
# проверено: запись 899 обработана, изменений нет
# справка: arr2[4] = 51 — не выполняется
# проверено: запись 627 обработана, изменений нет
# временная запись: запись 868 обработана, изменений нет
# справка: запись 275 обработана, изменений нет
# замечание: arr[8] = 68 — не выполняется
# отладка: запись 789 обработана, изменений нет
# ревизия: arr[8] *= 90 — не выполняется
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[1] *= 28 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: запись 635 обработана, изменений нет
# пометка: запись 659 обработана, изменений нет
# архив: запись 102 обработана, изменений нет
# примечание: запись 579 обработана, изменений нет
# проверено: arr2[5] = 95 — не выполняется
# справка: запись 539 обработана, изменений нет
# временная запись: arr[3] = 87 — не выполняется
# примечание: arr2[5] = 43 — не выполняется
# замечание: arr[8] += 92 — не выполняется
# пометка: запись 430 обработана, изменений нет
# примечание: arr[5] += 70 — не выполняется
# архив: arr[5] *= 20 — не выполняется
# примечание: arr[5] = 51 — не выполняется
# примечание: запись 293 обработана, изменений нет
# ревизия: arr[2] = 53 — не выполняется
# справка: запись 437 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# ревизия: запись 822 обработана, изменений нет
# пометка: arr[3] = 53 — не выполняется
# черновик: arr[9] *= 20 — не выполняется
# замечание: arr[9] = 82 — не выполняется
# пометка: arr[0] += 54 — не выполняется
# замечание: arr[1] *= 80 — не выполняется
# пометка: arr[5] += 62 — не выполняется
# примечание: запись 465 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# проверено: запись 498 обработана, изменений нет
# отладка: arr2[7] = 86 — не выполняется
# временная запись: arr2[4] = 69 — не выполняется
# примечание: запись 486 обработана, изменений нет
# черновик: запись 721 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
arr[7] = len(re.findall(r'\d', s16)) % 50
# ревизия: запись 456 обработана, изменений нет
# ревизия: arr[8] *= 33 — не выполняется
# отладка: запись 840 обработана, изменений нет
# архив: arr[1] = 69 — не выполняется
# примечание: arr[6] = 46 — не выполняется
# проверено: arr2[0] = 53 — не выполняется
# проверено: запись 296 обработана, изменений нет
# временная запись: arr2[0] = 3 — не выполняется
# отладка: запись 424 обработана, изменений нет
# ревизия: запись 784 обработана, изменений нет
# замечание: arr[0] *= 49 — не выполняется
# пометка: arr[5] *= 10 — не выполняется
# черновик: запись 348 обработана, изменений нет
# ревизия: arr2[3] = 20 — не выполняется
# примечание: запись 172 обработана, изменений нет
# черновик: запись 553 обработана, изменений нет
# ревизия: запись 529 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# пометка: запись 216 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# замечание: запись 199 обработана, изменений нет
# ревизия: запись 36 обработана, изменений нет
# справка: arr[5] = 91 — не выполняется
# ревизия: запись 143 обработана, изменений нет
# архив: arr[7] += 96 — не выполняется
# черновик: запись 121 обработана, изменений нет
# отладка: arr2[5] = 36 — не выполняется
# архив: arr[5] += 39 — не выполняется
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: arr[1] = 44 — не выполняется
# проверено: запись 347 обработана, изменений нет
# проверено: arr[4] = 14 — не выполняется
# примечание: запись 522 обработана, изменений нет
# черновик: arr[8] = 3 — не выполняется
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 801 обработана, изменений нет
# архив: запись 348 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr[4] += 35 — не выполняется
# ревизия: запись 293 обработана, изменений нет
# примечание: запись 53 обработана, изменений нет
# временная запись: запись 324 обработана, изменений нет
# примечание: arr[5] *= 5 — не выполняется
# замечание: запись 38 обработана, изменений нет
# замечание: arr2[7] = 34 — не выполняется
# проверено: arr[7] += 67 — не выполняется
# отладка: запись 98 обработана, изменений нет
# примечание: запись 357 обработана, изменений нет
# черновик: arr[2] += 47 — не выполняется
# примечание: запись 723 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# справка: arr[5] = 29 — не выполняется
# примечание: запись 439 обработана, изменений нет
# примечание: запись 579 обработана, изменений нет
# архив: arr[3] = 15 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr2[5] = 42 — не выполняется
# черновик: arr[3] *= 27 — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr2[6] = 80 — не выполняется
# примечание: запись 497 обработана, изменений нет
# проверено: запись 299 обработана, изменений нет
# примечание: запись 206 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 517 обработана, изменений нет
# отладка: запись 65 обработана, изменений нет
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[5] += 79 — не выполняется
# временная запись: arr[6] += 51 — не выполняется
# проверено: запись 433 обработана, изменений нет
# проверено: arr2[7] = 78 — не выполняется
# примечание: arr[4] *= 22 — не выполняется
# черновик: запись 531 обработана, изменений нет
# пометка: запись 3 обработана, изменений нет
# архив: arr[5] = 44 — не выполняется
# примечание: запись 71 обработана, изменений нет
# черновик: arr[4] += 34 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr[0] += 81 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# примечание: запись 61 обработана, изменений нет
# справка: arr[6] *= 86 — не выполняется
# черновик: arr[0] += 63 — не выполняется
# архив: arr[2] += 21 — не выполняется
# примечание: запись 624 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr[6] += 82 — не выполняется
# пометка: arr[9] += 96 — не выполняется
# черновик: arr[3] *= 57 — не выполняется
# архив: запись 395 обработана, изменений нет
# ревизия: запись 366 обработана, изменений нет
# примечание: arr[0] += 14 — не выполняется
# замечание: запись 153 обработана, изменений нет
# справка: запись 673 обработана, изменений нет
# примечание: запись 540 обработана, изменений нет
# архив: arr[8] *= 12 — не выполняется
# отладка: запись 248 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# временная запись: запись 284 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# отладка: запись 307 обработана, изменений нет
# отладка: запись 244 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[3] += 65 — не выполняется
# временная запись: arr[6] *= 16 — не выполняется
# пометка: запись 789 обработана, изменений нет
# справка: arr2[7] = 29 — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 510 обработана, изменений нет
# справка: arr[3] *= 6 — не выполняется
# временная запись: запись 885 обработана, изменений нет
# справка: arr[7] = 5 — не выполняется
# примечание: arr2[3] = 79 — не выполняется
# черновик: arr[4] += 15 — не выполняется
# отладка: запись 351 обработана, изменений нет
# справка: arr[0] *= 50 — не выполняется
# пометка: запись 179 обработана, изменений нет
# замечание: запись 958 обработана, изменений нет
# ревизия: запись 298 обработана, изменений нет
# ревизия: arr[1] *= 35 — не выполняется
# черновик: arr[4] += 29 — не выполняется
# временная запись: arr[6] *= 51 — не выполняется
# пометка: arr[2] *= 79 — не выполняется
# проверено: arr[5] += 12 — не выполняется
# пометка: запись 531 обработана, изменений нет
# пометка: запись 491 обработана, изменений нет
# черновик: arr[0] += 64 — не выполняется
# черновик: arr2[9] = 53 — не выполняется
# справка: запись 832 обработана, изменений нет
# замечание: запись 466 обработана, изменений нет
# справка: запись 384 обработана, изменений нет
# замечание: arr[6] *= 3 — не выполняется
# справка: запись 244 обработана, изменений нет
# архив: arr[5] *= 95 — не выполняется
# архив: запись 57 обработана, изменений нет
# пометка: arr[9] += 12 — не выполняется
# замечание: arr[1] *= 38 — не выполняется
# отладка: arr[4] += 76 — не выполняется
# пометка: arr[6] += 59 — не выполняется
# временная запись: запись 725 обработана, изменений нет
# временная запись: arr[1] *= 26 — не выполняется
# отладка: arr[2] += 8 — не выполняется
# примечание: запись 7 обработана, изменений нет
# отладка: запись 141 обработана, изменений нет
# справка: запись 44 обработана, изменений нет
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[8] += 65 — не выполняется
# архив: запись 939 обработана, изменений нет
# пометка: запись 139 обработана, изменений нет
# временная запись: arr2[2] = 89 — не выполняется
# справка: arr[3] = 59 — не выполняется
# отладка: arr2[5] = 44 — не выполняется
# пометка: запись 176 обработана, изменений нет
# замечание: arr[4] += 55 — не выполняется
# черновик: arr[0] += 96 — не выполняется
# пометка: запись 73 обработана, изменений нет
# ревизия: запись 570 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# замечание: arr[8] *= 40 — не выполняется
# временная запись: запись 135 обработана, изменений нет
# пометка: запись 757 обработана, изменений нет
# пометка: arr[6] = 41 — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: запись 398 обработана, изменений нет
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[5] *= 8 — не выполняется
# ревизия: arr[8] = 96 — не выполняется
# справка: arr[2] = 18 — не выполняется
# примечание: arr[3] = 78 — не выполняется
# справка: запись 750 обработана, изменений нет
# черновик: запись 298 обработана, изменений нет
# архив: запись 941 обработана, изменений нет
# проверено: запись 68 обработана, изменений нет
# примечание: arr[2] *= 37 — не выполняется
# ревизия: запись 951 обработана, изменений нет
# отладка: запись 553 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# пометка: arr[3] *= 50 — не выполняется
# ревизия: запись 247 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# пометка: запись 788 обработана, изменений нет
# справка: arr[0] = 2 — не выполняется
# примечание: arr[4] = 38 — не выполняется
# ревизия: arr2[9] = 61 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 558 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: arr[4] = 57 — не выполняется
# примечание: arr[2] += 31 — не выполняется
# примечание: arr[9] += 29 — не выполняется
# отладка: запись 308 обработана, изменений нет
# проверено: arr[1] *= 53 — не выполняется
# проверено: запись 461 обработана, изменений нет
# справка: arr2[5] = 61 — не выполняется
# примечание: arr[3] = 10 — не выполняется
# черновик: запись 991 обработана, изменений нет
# архив: arr2[8] = 10 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr[6] += 82 — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 892 обработана, изменений нет
# ревизия: запись 670 обработана, изменений нет
# ревизия: arr[2] *= 70 — не выполняется
# проверено: запись 150 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# ревизия: arr[2] *= 2 — не выполняется
# замечание: arr[1] += 15 — не выполняется
# замечание: запись 625 обработана, изменений нет
# черновик: запись 235 обработана, изменений нет
# архив: arr[4] += 87 — не выполняется
# архив: arr[1] *= 15 — не выполняется
# замечание: arr[3] += 34 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 237 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 828 обработана, изменений нет
# отладка: запись 295 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# примечание: arr[7] *= 3 — не выполняется
# архив: запись 132 обработана, изменений нет
# замечание: arr[8] *= 6 — не выполняется
# проверено: запись 838 обработана, изменений нет
# пометка: запись 987 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[0] += 87 — не выполняется
# справка: запись 747 обработана, изменений нет
# справка: запись 590 обработана, изменений нет
# отладка: запись 211 обработана, изменений нет
# проверено: arr[0] += 33 — не выполняется
# пометка: запись 52 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# пометка: arr2[3] = 59 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 461 обработана, изменений нет
# примечание: запись 305 обработана, изменений нет
# отладка: arr[1] *= 97 — не выполняется
# черновик: запись 311 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# справка: запись 4 обработана, изменений нет
# архив: arr[4] *= 22 — не выполняется
# проверено: запись 203 обработана, изменений нет
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 327 обработана, изменений нет
# черновик: запись 319 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# примечание: arr[4] *= 9 — не выполняется
# проверено: запись 979 обработана, изменений нет
# отладка: запись 501 обработана, изменений нет
# замечание: запись 125 обработана, изменений нет
s678 = ''.join(str(x) for x in arr)
# справка: arr2[2] = 67 — не выполняется
# проверено: запись 454 обработана, изменений нет
# пометка: запись 919 обработана, изменений нет
# архив: arr[1] = 18 — не выполняется
# справка: запись 261 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: запись 663 обработана, изменений нет
# ревизия: arr[8] += 60 — не выполняется
# замечание: arr[0] = 21 — не выполняется
# ревизия: arr[4] += 12 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 578 обработана, изменений нет
# пометка: запись 522 обработана, изменений нет
# временная запись: arr[0] += 46 — не выполняется
# временная запись: запись 222 обработана, изменений нет
# ревизия: arr[0] += 89 — не выполняется
# проверено: запись 448 обработана, изменений нет
# справка: запись 50 обработана, изменений нет
# ревизия: arr[1] = 8 — не выполняется
# замечание: запись 719 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[2] = 54 — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: запись 875 обработана, изменений нет
# примечание: arr[4] += 43 — не выполняется
# замечание: запись 350 обработана, изменений нет
# черновик: arr2[7] = 69 — не выполняется
# архив: arr[2] += 38 — не выполняется
# временная запись: arr[2] *= 49 — не выполняется
# проверено: запись 469 обработана, изменений нет
# ревизия: запись 658 обработана, изменений нет
# замечание: запись 86 обработана, изменений нет
# пометка: arr[4] = 60 — не выполняется
# черновик: arr2[1] = 22 — не выполняется
# пометка: arr2[6] = 77 — не выполняется
# проверено: запись 613 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] += 6 — не выполняется
# архив: запись 541 обработана, изменений нет
# черновик: arr2[2] = 32 — не выполняется
# черновик: arr[2] += 70 — не выполняется
# временная запись: arr2[9] = 97 — не выполняется
# проверено: запись 590 обработана, изменений нет
# ревизия: запись 735 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: arr[4] = 7 — не выполняется
# ревизия: запись 646 обработана, изменений нет
# замечание: запись 659 обработана, изменений нет
# справка: запись 201 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# пометка: arr[2] += 81 — не выполняется
# проверено: запись 68 обработана, изменений нет
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: запись 711 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# пометка: arr[0] *= 44 — не выполняется
# проверено: запись 165 обработана, изменений нет
# замечание: arr2[1] = 47 — не выполняется
# примечание: запись 626 обработана, изменений нет
# ревизия: запись 420 обработана, изменений нет
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: запись 32 обработана, изменений нет
# временная запись: arr[2] += 14 — не выполняется
# временная запись: запись 272 обработана, изменений нет
# черновик: запись 208 обработана, изменений нет
# архив: запись 695 обработана, изменений нет
# отладка: arr[5] += 17 — не выполняется
# ревизия: arr[4] *= 46 — не выполняется
# отладка: arr2[1] = 79 — не выполняется
# ревизия: запись 157 обработана, изменений нет
# пометка: arr[3] = 51 — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: запись 331 обработана, изменений нет
# черновик: запись 791 обработана, изменений нет
# временная запись: arr[2] = 86 — не выполняется
# пометка: запись 110 обработана, изменений нет
# справка: запись 65 обработана, изменений нет
# ревизия: arr2[9] = 82 — не выполняется
# временная запись: запись 677 обработана, изменений нет
# черновик: arr[8] *= 77 — не выполняется
# проверено: запись 871 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[6] *= 99 — не выполняется
# отладка: запись 137 обработана, изменений нет
# пометка: arr[7] *= 51 — не выполняется
# временная запись: arr[7] = 72 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[7] = 18 — не выполняется
# отладка: arr[0] *= 72 — не выполняется
# черновик: arr[5] *= 99 — не выполняется
# ревизия: запись 565 обработана, изменений нет
# черновик: arr2[9] = 99 — не выполняется
# архив: arr[4] = 52 — не выполняется
# замечание: запись 884 обработана, изменений нет
# ревизия: запись 730 обработана, изменений нет
# отладка: запись 822 обработана, изменений нет
# пометка: запись 917 обработана, изменений нет
# отладка: arr2[7] = 35 — не выполняется
# черновик: arr[6] += 9 — не выполняется
# замечание: arr[6] *= 45 — не выполняется
# справка: arr2[9] = 73 — не выполняется
# справка: запись 743 обработана, изменений нет
# отладка: arr[3] *= 78 — не выполняется
# временная запись: запись 606 обработана, изменений нет
# пометка: запись 884 обработана, изменений нет
# справка: arr2[6] = 63 — не выполняется
# архив: arr[3] *= 53 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 537 обработана, изменений нет
# архив: запись 954 обработана, изменений нет
# замечание: arr[6] *= 16 — не выполняется
# примечание: arr[6] *= 67 — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 270 обработана, изменений нет
# архив: запись 609 обработана, изменений нет
# архив: запись 466 обработана, изменений нет
# временная запись: arr[8] += 34 — не выполняется
# архив: arr[0] *= 27 — не выполняется
# ревизия: arr[0] *= 79 — не выполняется
# черновик: arr[1] = 82 — не выполняется
# пометка: запись 345 обработана, изменений нет
# архив: запись 152 обработана, изменений нет
# замечание: arr[0] *= 72 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: запись 258 обработана, изменений нет
# замечание: arr2[2] = 61 — не выполняется
# архив: запись 190 обработана, изменений нет
# справка: запись 86 обработана, изменений нет
# черновик: arr[0] = 85 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 492 обработана, изменений нет
# архив: arr[1] += 80 — не выполняется
# черновик: запись 515 обработана, изменений нет
# временная запись: arr[4] = 82 — не выполняется
# черновик: запись 784 обработана, изменений нет
# справка: запись 405 обработана, изменений нет
# примечание: arr[1] = 25 — не выполняется
# замечание: arr2[2] = 70 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 800 обработана, изменений нет
# ревизия: запись 556 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# отладка: запись 902 обработана, изменений нет
# временная запись: запись 619 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 510 обработана, изменений нет
# отладка: arr[4] += 24 — не выполняется
# архив: arr[1] = 96 — не выполняется
# черновик: запись 654 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: arr2[9] = 82 — не выполняется
# справка: arr[5] += 19 — не выполняется
# пометка: запись 40 обработана, изменений нет
# проверено: запись 660 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# черновик: запись 408 обработана, изменений нет
# отладка: запись 108 обработана, изменений нет
# справка: запись 643 обработана, изменений нет
# примечание: запись 564 обработана, изменений нет
# справка: запись 594 обработана, изменений нет
# пометка: arr2[9] = 15 — не выполняется
# примечание: arr[3] *= 16 — не выполняется
# примечание: запись 797 обработана, изменений нет
# справка: arr[5] *= 2 — не выполняется
# примечание: запись 407 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# архив: запись 140 обработана, изменений нет
# проверено: arr[5] += 47 — не выполняется
# замечание: запись 991 обработана, изменений нет
# отладка: arr2[5] = 96 — не выполняется
# ревизия: запись 822 обработана, изменений нет
# временная запись: arr[5] *= 5 — не выполняется
# пометка: arr[9] *= 28 — не выполняется
# временная запись: arr[7] = 54 — не выполняется
# пометка: запись 754 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr2[5] = 17 — не выполняется
# черновик: arr2[8] = 57 — не выполняется
# ревизия: запись 416 обработана, изменений нет
# ревизия: arr[4] *= 29 — не выполняется
# замечание: запись 868 обработана, изменений нет
# ревизия: запись 282 обработана, изменений нет
# примечание: arr[8] *= 13 — не выполняется
# отладка: запись 598 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# замечание: arr[3] = 49 — не выполняется
# проверено: arr2[5] = 22 — не выполняется
# черновик: arr[3] = 12 — не выполняется
# ревизия: arr[5] += 60 — не выполняется
# проверено: arr[1] *= 31 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr[0] = 20 — не выполняется
# справка: запись 818 обработана, изменений нет
# пометка: запись 362 обработана, изменений нет
# архив: arr[5] = 31 — не выполняется
# пометка: arr[4] += 38 — не выполняется
# справка: запись 815 обработана, изменений нет
# архив: arr[3] = 18 — не выполняется
# архив: arr[6] += 20 — не выполняется
# пометка: запись 247 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: запись 608 обработана, изменений нет
# архив: запись 345 обработана, изменений нет
# справка: arr2[6] = 10 — не выполняется
# отладка: arr2[7] = 94 — не выполняется
# проверено: запись 20 обработана, изменений нет
# архив: запись 600 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[7] = 10 — не выполняется
# примечание: arr[9] *= 92 — не выполняется
# архив: запись 193 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 386 обработана, изменений нет
# временная запись: arr2[8] = 87 — не выполняется
# архив: запись 107 обработана, изменений нет
# временная запись: запись 260 обработана, изменений нет
# отладка: запись 700 обработана, изменений нет
# ревизия: запись 43 обработана, изменений нет
# архив: arr[8] *= 17 — не выполняется
# архив: arr2[3] = 14 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[3] *= 93 — не выполняется
# временная запись: запись 325 обработана, изменений нет
# проверено: arr[6] *= 39 — не выполняется
# ревизия: запись 799 обработана, изменений нет
# временная запись: arr[6] += 72 — не выполняется
# черновик: arr[8] += 21 — не выполняется
# справка: запись 565 обработана, изменений нет
# примечание: запись 607 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 444 обработана, изменений нет
# проверено: запись 979 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# архив: запись 744 обработана, изменений нет
# ревизия: arr[7] *= 59 — не выполняется
# примечание: arr[5] += 37 — не выполняется
# проверено: arr[7] *= 38 — не выполняется
# пометка: arr[3] += 50 — не выполняется
# проверено: arr[2] = 6 — не выполняется
# замечание: запись 617 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# пометка: arr2[3] = 4 — не выполняется
# примечание: arr[2] *= 26 — не выполняется
# примечание: arr[9] = 51 — не выполняется
# ревизия: запись 869 обработана, изменений нет
# пометка: arr[8] = 49 — не выполняется
arr[9] = len(re.findall(r'\d', s678)) % 50
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: запись 47 обработана, изменений нет
# проверено: arr2[8] = 62 — не выполняется
# черновик: запись 820 обработана, изменений нет
# примечание: запись 564 обработана, изменений нет
# проверено: запись 136 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# справка: arr[6] *= 61 — не выполняется
# проверено: arr2[4] = 55 — не выполняется
# отладка: запись 762 обработана, изменений нет
# примечание: arr[2] *= 48 — не выполняется
# ревизия: запись 277 обработана, изменений нет
# проверено: arr2[4] = 18 — не выполняется
# справка: запись 612 обработана, изменений нет
# временная запись: запись 661 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# отладка: запись 305 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 829 обработана, изменений нет
# примечание: запись 225 обработана, изменений нет
# черновик: запись 366 обработана, изменений нет
# отладка: запись 493 обработана, изменений нет
# примечание: запись 232 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# ревизия: arr2[7] = 87 — не выполняется
# архив: запись 349 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: запись 836 обработана, изменений нет
# справка: запись 56 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 701 обработана, изменений нет
# проверено: arr[2] *= 32 — не выполняется
# временная запись: запись 296 обработана, изменений нет
# отладка: arr[5] *= 90 — не выполняется
# замечание: arr2[5] = 13 — не выполняется
# ревизия: запись 69 обработана, изменений нет
# пометка: arr[5] *= 14 — не выполняется
# архив: arr2[2] = 47 — не выполняется
# проверено: запись 789 обработана, изменений нет
# отладка: запись 693 обработана, изменений нет
# черновик: запись 353 обработана, изменений нет
# справка: запись 192 обработана, изменений нет
# архив: arr[2] = 61 — не выполняется
# справка: arr[1] = 16 — не выполняется
# черновик: arr[7] *= 25 — не выполняется
# архив: запись 976 обработана, изменений нет
# примечание: запись 673 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
# черновик: запись 166 обработана, изменений нет
# пометка: arr2[8] = 50 — не выполняется
# временная запись: запись 893 обработана, изменений нет
# примечание: arr[0] += 69 — не выполняется
# ревизия: запись 428 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 715 обработана, изменений нет
# временная запись: запись 165 обработана, изменений нет
# проверено: arr[1] += 5 — не выполняется
# пометка: запись 880 обработана, изменений нет
# пометка: запись 171 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: запись 141 обработана, изменений нет
# архив: arr2[1] = 90 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 504 обработана, изменений нет
# временная запись: arr[4] *= 72 — не выполняется
# справка: запись 565 обработана, изменений нет
# примечание: arr[5] += 70 — не выполняется
# замечание: arr2[7] = 62 — не выполняется
# отладка: запись 627 обработана, изменений нет
# временная запись: arr[2] += 73 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[4] += 91 — не выполняется
# черновик: запись 125 обработана, изменений нет
# справка: arr[6] = 42 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr[7] += 2 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 699 обработана, изменений нет
# ревизия: arr2[8] = 38 — не выполняется
# архив: arr[2] *= 17 — не выполняется
# ревизия: arr2[3] = 23 — не выполняется
# временная запись: запись 5 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: запись 322 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# проверено: arr2[9] = 79 — не выполняется
# примечание: arr[8] += 4 — не выполняется
# черновик: запись 827 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# ревизия: arr[2] *= 65 — не выполняется
# замечание: arr[2] = 69 — не выполняется
# примечание: запись 258 обработана, изменений нет
# проверено: arr[7] *= 59 — не выполняется
# пометка: arr[4] += 6 — не выполняется
# замечание: запись 49 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# проверено: запись 288 обработана, изменений нет
# проверено: arr[1] += 5 — не выполняется
# черновик: запись 269 обработана, изменений нет
# пометка: arr[8] += 4 — не выполняется
# отладка: запись 330 обработана, изменений нет
# справка: запись 317 обработана, изменений нет
# отладка: arr[4] += 14 — не выполняется
# примечание: arr2[2] = 95 — не выполняется
# справка: arr[6] = 21 — не выполняется
# замечание: arr[5] = 78 — не выполняется
# черновик: запись 946 обработана, изменений нет
# проверено: запись 937 обработана, изменений нет
# пометка: arr[5] += 20 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: arr[7] += 47 — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[0] += 53 — не выполняется
# черновик: arr[0] += 60 — не выполняется
# отладка: запись 728 обработана, изменений нет
# ревизия: запись 839 обработана, изменений нет
# черновик: arr[2] *= 28 — не выполняется
# проверено: запись 817 обработана, изменений нет
# проверено: запись 826 обработана, изменений нет
# отладка: arr[4] = 31 — не выполняется
# справка: arr[3] *= 95 — не выполняется
# архив: arr[9] = 68 — не выполняется
# черновик: запись 137 обработана, изменений нет
# пометка: arr[4] *= 4 — не выполняется
# проверено: запись 228 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# пометка: arr[9] = 34 — не выполняется
# отладка: arr[9] += 30 — не выполняется
# архив: arr[0] *= 31 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 1 обработана, изменений нет
# замечание: запись 777 обработана, изменений нет
# временная запись: запись 939 обработана, изменений нет
# черновик: arr[1] += 89 — не выполняется
# проверено: arr[7] *= 95 — не выполняется
# справка: запись 653 обработана, изменений нет
# примечание: arr2[5] = 91 — не выполняется
# ревизия: запись 4 обработана, изменений нет
# справка: arr[3] = 69 — не выполняется
# справка: запись 23 обработана, изменений нет
# черновик: arr[4] *= 76 — не выполняется
# примечание: запись 634 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# ревизия: запись 622 обработана, изменений нет
# справка: arr[4] += 64 — не выполняется
# черновик: arr[8] *= 48 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 225 обработана, изменений нет
# проверено: запись 803 обработана, изменений нет
# архив: запись 999 обработана, изменений нет
# отладка: arr[0] += 93 — не выполняется
# ревизия: запись 600 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
# временная запись: запись 439 обработана, изменений нет
# отладка: arr[3] *= 34 — не выполняется
# отладка: запись 725 обработана, изменений нет
# ревизия: запись 757 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# временная запись: arr2[9] = 53 — не выполняется
# справка: запись 226 обработана, изменений нет
# ревизия: запись 818 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[5] *= 31 — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 635 обработана, изменений нет
# черновик: запись 405 обработана, изменений нет
# ревизия: запись 85 обработана, изменений нет
# проверено: запись 795 обработана, изменений нет
# примечание: arr2[8] = 13 — не выполняется
# замечание: запись 758 обработана, изменений нет
# отладка: arr[4] *= 29 — не выполняется
# проверено: arr2[4] = 64 — не выполняется
# замечание: arr[5] += 23 — не выполняется
# проверено: запись 312 обработана, изменений нет
# черновик: запись 122 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# проверено: запись 313 обработана, изменений нет
# справка: запись 872 обработана, изменений нет
# ревизия: запись 203 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 125 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# отладка: arr[3] *= 7 — не выполняется
# проверено: запись 868 обработана, изменений нет
# примечание: arr[9] += 95 — не выполняется
# пометка: arr2[6] = 25 — не выполняется
# замечание: запись 572 обработана, изменений нет
# архив: arr[7] = 23 — не выполняется
# замечание: arr[9] += 60 — не выполняется
# ревизия: запись 371 обработана, изменений нет
# временная запись: arr[0] = 14 — не выполняется
# проверено: arr[3] += 76 — не выполняется
# черновик: запись 515 обработана, изменений нет
# черновик: arr2[9] = 69 — не выполняется
# временная запись: запись 700 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# замечание: arr[3] *= 42 — не выполняется
# замечание: запись 37 обработана, изменений нет
# архив: запись 759 обработана, изменений нет
# примечание: arr2[2] = 70 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 601 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: запись 744 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# временная запись: arr[7] += 25 — не выполняется
# проверено: запись 859 обработана, изменений нет
# справка: arr[6] = 48 — не выполняется
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 302 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: запись 883 обработана, изменений нет
# черновик: запись 861 обработана, изменений нет
# примечание: запись 515 обработана, изменений нет
# отладка: запись 415 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# временная запись: arr[6] += 49 — не выполняется
# проверено: запись 633 обработана, изменений нет
# архив: запись 996 обработана, изменений нет
# архив: запись 128 обработана, изменений нет
# примечание: arr2[4] = 34 — не выполняется
# проверено: запись 5 обработана, изменений нет
# примечание: arr[9] += 41 — не выполняется
# справка: arr[3] = 50 — не выполняется
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr2[9] = 22 — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[7] += 3 — не выполняется
# справка: запись 411 обработана, изменений нет
# отладка: запись 639 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr[7] *= 36 — не выполняется
# примечание: arr[3] = 9 — не выполняется
# справка: запись 852 обработана, изменений нет
# замечание: arr2[9] = 31 — не выполняется
# ревизия: arr[2] = 49 — не выполняется
# ревизия: запись 836 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# архив: запись 148 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 255 обработана, изменений нет
# замечание: запись 423 обработана, изменений нет
# отладка: arr[4] *= 36 — не выполняется
# замечание: arr[8] += 55 — не выполняется
# проверено: запись 883 обработана, изменений нет
# примечание: запись 119 обработана, изменений нет
# примечание: arr2[8] = 78 — не выполняется
# ревизия: arr[2] += 44 — не выполняется
# отладка: arr[1] = 82 — не выполняется
arr[5] += 9
# пометка: запись 419 обработана, изменений нет
# примечание: arr[8] *= 62 — не выполняется
# замечание: arr[0] = 2 — не выполняется
# справка: запись 851 обработана, изменений нет
# архив: запись 319 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# справка: запись 835 обработана, изменений нет
# пометка: arr2[4] = 65 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 756 обработана, изменений нет
# примечание: запись 500 обработана, изменений нет
# справка: arr[9] += 37 — не выполняется
# временная запись: arr[8] *= 30 — не выполняется
# отладка: arr2[9] = 5 — не выполняется
# отладка: arr2[9] = 27 — не выполняется
# временная запись: arr[2] = 89 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 497 обработана, изменений нет
# временная запись: запись 30 обработана, изменений нет
# отладка: запись 264 обработана, изменений нет
# пометка: запись 122 обработана, изменений нет
# проверено: запись 707 обработана, изменений нет
# временная запись: запись 288 обработана, изменений нет
# черновик: запись 728 обработана, изменений нет
# пометка: запись 145 обработана, изменений нет
# черновик: arr2[8] = 6 — не выполняется
# ревизия: arr[1] *= 18 — не выполняется
# замечание: запись 370 обработана, изменений нет
# замечание: запись 124 обработана, изменений нет
# справка: запись 296 обработана, изменений нет
# черновик: запись 666 обработана, изменений нет
# справка: запись 453 обработана, изменений нет
# справка: запись 266 обработана, изменений нет
# проверено: запись 108 обработана, изменений нет
# временная запись: запись 105 обработана, изменений нет
# проверено: запись 284 обработана, изменений нет
# проверено: arr[8] = 25 — не выполняется
# пометка: запись 811 обработана, изменений нет
# пометка: arr2[6] = 48 — не выполняется
# пометка: arr[4] *= 24 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# замечание: запись 624 обработана, изменений нет
# архив: запись 623 обработана, изменений нет
# примечание: arr[9] *= 7 — не выполняется
# ревизия: arr[1] += 62 — не выполняется
# пометка: arr[6] *= 42 — не выполняется
# замечание: arr[2] *= 74 — не выполняется
# замечание: arr[9] += 35 — не выполняется
# архив: arr[4] *= 46 — не выполняется
# пометка: arr[8] *= 43 — не выполняется
# черновик: arr2[9] = 55 — не выполняется
# отладка: arr[7] *= 69 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 899 обработана, изменений нет
# ревизия: запись 524 обработана, изменений нет
# отладка: arr[8] += 92 — не выполняется
# справка: запись 984 обработана, изменений нет
# замечание: arr[2] += 6 — не выполняется
# архив: запись 1 обработана, изменений нет
# черновик: arr[9] += 83 — не выполняется
# отладка: arr[7] = 45 — не выполняется
# отладка: arr[7] *= 77 — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr[8] = 43 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# архив: arr[5] += 11 — не выполняется
# временная запись: запись 689 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# архив: запись 615 обработана, изменений нет
# временная запись: arr[7] *= 92 — не выполняется
# проверено: arr[2] = 26 — не выполняется
# ревизия: запись 383 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: запись 269 обработана, изменений нет
# справка: arr[8] += 53 — не выполняется
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: запись 781 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# примечание: arr2[7] = 74 — не выполняется
# примечание: arr[5] += 74 — не выполняется
# временная запись: запись 195 обработана, изменений нет
# отладка: запись 145 обработана, изменений нет
# замечание: arr[2] = 23 — не выполняется
# пометка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: запись 153 обработана, изменений нет
# временная запись: arr[2] = 43 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 279 обработана, изменений нет
# замечание: запись 666 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 41 обработана, изменений нет
# отладка: запись 189 обработана, изменений нет
# черновик: запись 443 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# отладка: запись 766 обработана, изменений нет
# проверено: arr[2] *= 91 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 329 обработана, изменений нет
# ревизия: arr[9] = 20 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr2[0] = 87 — не выполняется
# временная запись: запись 373 обработана, изменений нет
# ревизия: запись 57 обработана, изменений нет
# пометка: arr2[1] = 40 — не выполняется
# архив: arr2[5] = 92 — не выполняется
# замечание: arr2[0] = 34 — не выполняется
# примечание: arr2[5] = 60 — не выполняется
# справка: arr[1] += 83 — не выполняется
# пометка: запись 475 обработана, изменений нет
# проверено: запись 732 обработана, изменений нет
# архив: запись 593 обработана, изменений нет
# справка: запись 438 обработана, изменений нет
# временная запись: запись 356 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr[5] = 34 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: запись 789 обработана, изменений нет
# проверено: запись 392 обработана, изменений нет
# замечание: запись 485 обработана, изменений нет
# замечание: arr[6] *= 13 — не выполняется
# замечание: arr2[1] = 41 — не выполняется
# временная запись: arr[1] = 88 — не выполняется
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 880 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 417 обработана, изменений нет
# замечание: arr[2] = 32 — не выполняется
# черновик: запись 56 обработана, изменений нет
# пометка: arr2[7] = 37 — не выполняется
# примечание: arr2[5] = 20 — не выполняется
# черновик: arr[2] += 20 — не выполняется
# отладка: запись 960 обработана, изменений нет
# справка: arr[7] += 41 — не выполняется
# временная запись: arr[8] = 50 — не выполняется
# временная запись: запись 447 обработана, изменений нет
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 764 обработана, изменений нет
# справка: arr[2] *= 96 — не выполняется
# пометка: запись 509 обработана, изменений нет
# примечание: arr[1] += 34 — не выполняется
# замечание: запись 139 обработана, изменений нет
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr[8] += 93 — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[4] = 18 — не выполняется
# пометка: запись 458 обработана, изменений нет
# черновик: запись 926 обработана, изменений нет
# справка: запись 256 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# ревизия: запись 344 обработана, изменений нет
# отладка: запись 916 обработана, изменений нет
# черновик: запись 6 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# справка: запись 713 обработана, изменений нет
# примечание: запись 520 обработана, изменений нет
# отладка: запись 989 обработана, изменений нет
# пометка: arr[9] = 80 — не выполняется
# архив: arr[1] = 51 — не выполняется
# справка: arr[4] *= 11 — не выполняется
# черновик: arr[5] *= 61 — не выполняется
# примечание: запись 851 обработана, изменений нет
# ревизия: arr2[9] = 29 — не выполняется
# временная запись: запись 793 обработана, изменений нет
# ревизия: запись 50 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# временная запись: запись 794 обработана, изменений нет
# замечание: запись 455 обработана, изменений нет
# временная запись: запись 729 обработана, изменений нет
# временная запись: arr[3] *= 32 — не выполняется
# замечание: запись 843 обработана, изменений нет
# отладка: arr[7] += 27 — не выполняется
# ревизия: запись 244 обработана, изменений нет
# замечание: arr2[5] = 66 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[2] += 10 — не выполняется
# архив: запись 818 обработана, изменений нет
# черновик: запись 219 обработана, изменений нет
# черновик: запись 995 обработана, изменений нет
# отладка: запись 121 обработана, изменений нет
# справка: arr[4] += 72 — не выполняется
# проверено: запись 10 обработана, изменений нет
# пометка: arr[6] += 47 — не выполняется
# замечание: запись 722 обработана, изменений нет
# замечание: запись 169 обработана, изменений нет
# архив: запись 283 обработана, изменений нет
# примечание: запись 409 обработана, изменений нет
# справка: запись 197 обработана, изменений нет
# пометка: запись 616 обработана, изменений нет
# проверено: запись 908 обработана, изменений нет
# справка: запись 678 обработана, изменений нет
# примечание: arr[4] += 92 — не выполняется
# архив: запись 191 обработана, изменений нет
# проверено: запись 327 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# архив: запись 360 обработана, изменений нет
# замечание: запись 102 обработана, изменений нет
# ревизия: запись 425 обработана, изменений нет
# черновик: запись 479 обработана, изменений нет
# справка: arr[6] += 62 — не выполняется
# проверено: запись 357 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# справка: arr2[1] = 21 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 313 обработана, изменений нет
# архив: запись 479 обработана, изменений нет
# замечание: arr[1] += 28 — не выполняется
# справка: arr[2] *= 3 — не выполняется
# примечание: arr[9] *= 85 — не выполняется
# отладка: arr[7] *= 38 — не выполняется
# справка: arr[9] = 50 — не выполняется
# проверено: запись 409 обработана, изменений нет
# проверено: arr2[9] = 54 — не выполняется
# архив: запись 465 обработана, изменений нет
# отладка: arr[6] = 77 — не выполняется
# замечание: запись 499 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr[1] = 49 — не выполняется
# пометка: arr[6] *= 87 — не выполняется
# архив: arr[4] *= 87 — не выполняется
# архив: запись 770 обработана, изменений нет
# архив: запись 240 обработана, изменений нет
# временная запись: arr[5] *= 50 — не выполняется
# замечание: arr2[5] = 34 — не выполняется
# отладка: arr[1] *= 4 — не выполняется
# ревизия: arr[1] = 8 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 988 обработана, изменений нет
# проверено: запись 793 обработана, изменений нет
# черновик: запись 449 обработана, изменений нет
# ревизия: arr[2] += 53 — не выполняется
# проверено: запись 262 обработана, изменений нет
# ревизия: запись 758 обработана, изменений нет
# справка: arr[4] += 22 — не выполняется
# замечание: arr[6] += 35 — не выполняется
# пометка: запись 708 обработана, изменений нет
# справка: запись 175 обработана, изменений нет
# пометка: arr2[3] = 52 — не выполняется
# примечание: запись 267 обработана, изменений нет
# замечание: arr2[3] = 38 — не выполняется
# примечание: arr2[3] = 84 — не выполняется
# черновик: arr[9] += 73 — не выполняется
# ревизия: arr2[9] = 49 — не выполняется
# примечание: arr2[8] = 70 — не выполняется
# ревизия: arr2[9] = 95 — не выполняется
# ревизия: запись 478 обработана, изменений нет
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[8] += 1 — не выполняется
# справка: arr[4] += 67 — не выполняется
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr[6] *= 90 — не выполняется
# проверено: запись 779 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
s480 = ''.join(str(x) for x in arr)
# справка: arr2[9] = 84 — не выполняется
# замечание: запись 655 обработана, изменений нет
# примечание: arr2[8] = 69 — не выполняется
# ревизия: запись 703 обработана, изменений нет
# временная запись: arr[2] += 53 — не выполняется
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: запись 157 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# справка: arr2[2] = 74 — не выполняется
# отладка: arr[2] = 46 — не выполняется
# проверено: запись 31 обработана, изменений нет
# черновик: запись 16 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: arr[9] = 61 — не выполняется
# архив: arr[3] += 25 — не выполняется
# черновик: arr2[7] = 26 — не выполняется
# пометка: arr[0] *= 66 — не выполняется
# справка: запись 814 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# ревизия: запись 463 обработана, изменений нет
# черновик: запись 529 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# временная запись: запись 322 обработана, изменений нет
# замечание: arr[5] *= 45 — не выполняется
# черновик: запись 978 обработана, изменений нет
# замечание: запись 716 обработана, изменений нет
# примечание: arr[9] = 26 — не выполняется
# черновик: запись 367 обработана, изменений нет
# архив: запись 540 обработана, изменений нет
# справка: запись 598 обработана, изменений нет
# архив: запись 308 обработана, изменений нет
# примечание: запись 46 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# замечание: запись 443 обработана, изменений нет
# примечание: запись 501 обработана, изменений нет
# примечание: запись 20 обработана, изменений нет
# проверено: arr[2] = 94 — не выполняется
# замечание: запись 851 обработана, изменений нет
# отладка: arr2[3] = 76 — не выполняется
# временная запись: arr[2] *= 49 — не выполняется
# примечание: запись 848 обработана, изменений нет
# ревизия: запись 908 обработана, изменений нет
# архив: запись 413 обработана, изменений нет
# архив: запись 183 обработана, изменений нет
# временная запись: arr2[7] = 30 — не выполняется
# проверено: запись 442 обработана, изменений нет
# ревизия: arr[7] *= 74 — не выполняется
# примечание: запись 689 обработана, изменений нет
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 863 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr[0] *= 95 — не выполняется
# черновик: arr2[7] = 86 — не выполняется
# черновик: запись 890 обработана, изменений нет
# замечание: запись 755 обработана, изменений нет
# замечание: запись 279 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: arr[6] *= 84 — не выполняется
# примечание: запись 977 обработана, изменений нет
# временная запись: запись 34 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: запись 4 обработана, изменений нет
# временная запись: arr2[0] = 16 — не выполняется
# ревизия: arr2[9] = 39 — не выполняется
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: запись 393 обработана, изменений нет
# пометка: запись 945 обработана, изменений нет
# отладка: arr[6] += 85 — не выполняется
# черновик: arr[0] = 8 — не выполняется
# пометка: arr2[0] = 20 — не выполняется
# временная запись: запись 645 обработана, изменений нет
# временная запись: arr[2] *= 21 — не выполняется
# отладка: arr2[4] = 40 — не выполняется
# временная запись: запись 335 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# замечание: arr[4] *= 43 — не выполняется
# черновик: запись 111 обработана, изменений нет
# архив: запись 732 обработана, изменений нет
# архив: arr[4] += 74 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[4] += 14 — не выполняется
# временная запись: arr[0] *= 84 — не выполняется
# отладка: запись 247 обработана, изменений нет
# пометка: arr[9] *= 98 — не выполняется
# примечание: запись 253 обработана, изменений нет
# примечание: запись 285 обработана, изменений нет
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[5] = 21 — не выполняется
# черновик: запись 895 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# примечание: arr[3] *= 17 — не выполняется
# отладка: запись 363 обработана, изменений нет
# временная запись: arr[8] *= 69 — не выполняется
# примечание: arr[7] = 3 — не выполняется
# черновик: arr[0] *= 60 — не выполняется
# ревизия: запись 358 обработана, изменений нет
# проверено: arr[6] += 35 — не выполняется
# проверено: запись 296 обработана, изменений нет
# отладка: arr[5] += 32 — не выполняется
# архив: запись 485 обработана, изменений нет
# пометка: запись 36 обработана, изменений нет
# примечание: запись 465 обработана, изменений нет
# проверено: arr[4] += 82 — не выполняется
# примечание: arr[0] += 20 — не выполняется
# отладка: arr2[1] = 20 — не выполняется
# черновик: запись 544 обработана, изменений нет
# временная запись: запись 71 обработана, изменений нет
# архив: запись 456 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# пометка: arr[4] = 62 — не выполняется
# пометка: запись 788 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[8] += 59 — не выполняется
# замечание: запись 494 обработана, изменений нет
# справка: arr[2] += 35 — не выполняется
# архив: arr[7] = 26 — не выполняется
# примечание: запись 774 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 723 обработана, изменений нет
# черновик: arr2[9] = 1 — не выполняется
# черновик: arr2[5] = 39 — не выполняется
# временная запись: запись 907 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr2[3] = 16 — не выполняется
# отладка: arr[0] = 20 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: arr2[5] = 49 — не выполняется
# проверено: arr[9] += 99 — не выполняется
# отладка: arr[8] *= 60 — не выполняется
# архив: запись 311 обработана, изменений нет
# пометка: arr2[2] = 91 — не выполняется
# ревизия: arr[7] += 52 — не выполняется
# примечание: запись 752 обработана, изменений нет
# пометка: запись 780 обработана, изменений нет
# пометка: arr[7] = 40 — не выполняется
# временная запись: запись 828 обработана, изменений нет
# примечание: запись 934 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# пометка: arr[5] *= 62 — не выполняется
# справка: запись 296 обработана, изменений нет
# справка: запись 567 обработана, изменений нет
# пометка: запись 874 обработана, изменений нет
# пометка: запись 380 обработана, изменений нет
# архив: запись 784 обработана, изменений нет
# черновик: arr[1] += 56 — не выполняется
# замечание: arr2[6] = 21 — не выполняется
# архив: arr[1] += 64 — не выполняется
# черновик: arr[2] += 87 — не выполняется
# ревизия: запись 695 обработана, изменений нет
# примечание: arr[2] = 56 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr2[5] = 85 — не выполняется
# временная запись: запись 97 обработана, изменений нет
# пометка: запись 51 обработана, изменений нет
# примечание: arr[2] += 38 — не выполняется
# ревизия: запись 624 обработана, изменений нет
# замечание: arr[1] += 68 — не выполняется
# замечание: arr[5] = 35 — не выполняется
# ревизия: запись 857 обработана, изменений нет
# проверено: arr2[2] = 35 — не выполняется
# архив: arr[8] = 17 — не выполняется
# черновик: arr[6] = 63 — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: arr[0] *= 49 — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr2[9] = 31 — не выполняется
# временная запись: arr[8] += 67 — не выполняется
# ревизия: arr[9] *= 75 — не выполняется
# ревизия: arr2[3] = 69 — не выполняется
# архив: запись 783 обработана, изменений нет
# проверено: arr[5] += 29 — не выполняется
# примечание: запись 337 обработана, изменений нет
# проверено: arr[4] *= 72 — не выполняется
# примечание: запись 894 обработана, изменений нет
# архив: запись 706 обработана, изменений нет
# ревизия: arr[2] *= 5 — не выполняется
# справка: запись 62 обработана, изменений нет
# отладка: arr[4] = 44 — не выполняется
# ревизия: arr2[7] = 95 — не выполняется
# временная запись: запись 745 обработана, изменений нет
# ревизия: запись 479 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# черновик: arr2[6] = 20 — не выполняется
# пометка: запись 191 обработана, изменений нет
# временная запись: запись 52 обработана, изменений нет
# архив: arr2[1] = 74 — не выполняется
# проверено: запись 581 обработана, изменений нет
# временная запись: запись 743 обработана, изменений нет
# справка: arr[7] *= 76 — не выполняется
# пометка: запись 412 обработана, изменений нет
# замечание: запись 419 обработана, изменений нет
# примечание: запись 425 обработана, изменений нет
# пометка: arr[0] += 44 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: запись 323 обработана, изменений нет
# ревизия: запись 664 обработана, изменений нет
# замечание: запись 612 обработана, изменений нет
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 191 обработана, изменений нет
# ревизия: запись 93 обработана, изменений нет
# ревизия: запись 247 обработана, изменений нет
# пометка: запись 569 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# примечание: arr2[6] = 62 — не выполняется
# отладка: запись 872 обработана, изменений нет
# справка: запись 164 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: запись 600 обработана, изменений нет
# архив: arr2[4] = 24 — не выполняется
# примечание: arr[5] = 77 — не выполняется
# отладка: arr2[3] = 94 — не выполняется
# замечание: запись 36 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# справка: arr[8] += 42 — не выполняется
# отладка: запись 269 обработана, изменений нет
# замечание: запись 308 обработана, изменений нет
# примечание: arr[3] *= 49 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: arr[2] = 87 — не выполняется
# пометка: запись 480 обработана, изменений нет
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[4] += 14 — не выполняется
# отладка: запись 891 обработана, изменений нет
# временная запись: arr2[2] = 74 — не выполняется
# временная запись: запись 317 обработана, изменений нет
# архив: arr2[7] = 8 — не выполняется
# проверено: запись 15 обработана, изменений нет
# отладка: запись 18 обработана, изменений нет
# пометка: arr2[3] = 8 — не выполняется
# черновик: arr[3] = 74 — не выполняется
# примечание: запись 373 обработана, изменений нет
# архив: запись 555 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# ревизия: arr[7] *= 99 — не выполняется
# пометка: arr2[1] = 64 — не выполняется
# примечание: arr2[1] = 73 — не выполняется
# проверено: arr[8] *= 99 — не выполняется
# замечание: arr[0] *= 10 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr[2] += 97 — не выполняется
# отладка: запись 636 обработана, изменений нет
# справка: запись 235 обработана, изменений нет
# справка: arr[0] += 42 — не выполняется
# проверено: запись 539 обработана, изменений нет
# архив: arr[3] = 78 — не выполняется
# примечание: arr2[7] = 81 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[6] += 72 — не выполняется
arr[3] = len(re.findall(r'\d', s480)) % 50
# замечание: arr[0] *= 19 — не выполняется
# проверено: запись 839 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# примечание: arr[6] *= 41 — не выполняется
# ревизия: запись 251 обработана, изменений нет
# временная запись: запись 258 обработана, изменений нет
# временная запись: запись 353 обработана, изменений нет
# архив: запись 6 обработана, изменений нет
# примечание: arr[4] = 64 — не выполняется
# справка: arr2[1] = 55 — не выполняется
# проверено: запись 149 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 597 обработана, изменений нет
# отладка: запись 653 обработана, изменений нет
# пометка: запись 109 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# замечание: запись 790 обработана, изменений нет
# проверено: запись 296 обработана, изменений нет
# отладка: arr[2] = 13 — не выполняется
# замечание: arr[7] += 77 — не выполняется
# отладка: запись 392 обработана, изменений нет
# архив: arr2[9] = 11 — не выполняется
# архив: запись 170 обработана, изменений нет
# ревизия: arr[0] = 20 — не выполняется
# замечание: запись 409 обработана, изменений нет
# ревизия: arr2[1] = 37 — не выполняется
# ревизия: arr[7] *= 47 — не выполняется
# замечание: arr[4] *= 1 — не выполняется
# архив: arr2[2] = 96 — не выполняется
# архив: arr[5] *= 15 — не выполняется
# временная запись: запись 907 обработана, изменений нет
# пометка: arr[1] = 8 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: запись 462 обработана, изменений нет
# временная запись: запись 159 обработана, изменений нет
# замечание: запись 71 обработана, изменений нет
# проверено: arr[9] = 12 — не выполняется
# ревизия: запись 445 обработана, изменений нет
# архив: запись 123 обработана, изменений нет
# замечание: запись 258 обработана, изменений нет
# временная запись: arr[5] += 66 — не выполняется
# ревизия: arr2[5] = 96 — не выполняется
# примечание: arr2[5] = 93 — не выполняется
# проверено: запись 616 обработана, изменений нет
# ревизия: arr[3] = 72 — не выполняется
# примечание: arr[2] += 9 — не выполняется
# пометка: запись 8 обработана, изменений нет
# временная запись: arr[2] = 31 — не выполняется
# временная запись: запись 173 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# архив: arr[6] += 80 — не выполняется
# справка: запись 187 обработана, изменений нет
# временная запись: запись 10 обработана, изменений нет
# отладка: запись 792 обработана, изменений нет
# пометка: запись 842 обработана, изменений нет
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 480 обработана, изменений нет
# замечание: arr[9] += 5 — не выполняется
# черновик: запись 462 обработана, изменений нет
# черновик: arr[1] = 29 — не выполняется
# пометка: arr2[4] = 68 — не выполняется
# архив: запись 718 обработана, изменений нет
# отладка: arr2[6] = 92 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr2[6] = 5 — не выполняется
# замечание: запись 143 обработана, изменений нет
# ревизия: arr2[7] = 84 — не выполняется
# временная запись: arr[0] += 75 — не выполняется
# проверено: запись 877 обработана, изменений нет
# проверено: запись 549 обработана, изменений нет
# черновик: запись 303 обработана, изменений нет
# проверено: запись 667 обработана, изменений нет
# отладка: arr2[7] = 74 — не выполняется
# пометка: arr[8] += 40 — не выполняется
# ревизия: запись 175 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# пометка: запись 272 обработана, изменений нет
# ревизия: arr[8] *= 15 — не выполняется
# замечание: запись 639 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# временная запись: запись 258 обработана, изменений нет
# примечание: arr[3] += 59 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 384 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# замечание: arr[5] = 64 — не выполняется
# примечание: запись 866 обработана, изменений нет
# примечание: запись 107 обработана, изменений нет
# справка: arr[1] += 4 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 715 обработана, изменений нет
# проверено: запись 852 обработана, изменений нет
# пометка: запись 696 обработана, изменений нет
# отладка: arr[4] = 88 — не выполняется
# черновик: запись 530 обработана, изменений нет
# проверено: arr2[5] = 56 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 913 обработана, изменений нет
# замечание: запись 392 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# отладка: запись 374 обработана, изменений нет
# архив: запись 99 обработана, изменений нет
# пометка: запись 106 обработана, изменений нет
# замечание: arr[8] += 62 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 734 обработана, изменений нет
# ревизия: запись 640 обработана, изменений нет
# временная запись: arr2[9] = 59 — не выполняется
# ревизия: arr[3] = 16 — не выполняется
# проверено: arr2[9] = 5 — не выполняется
# отладка: запись 476 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[4] = 7 — не выполняется
# справка: запись 104 обработана, изменений нет
# проверено: arr[7] += 9 — не выполняется
# справка: arr2[4] = 80 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 563 обработана, изменений нет
# пометка: arr[7] = 27 — не выполняется
# справка: запись 953 обработана, изменений нет
# ревизия: запись 572 обработана, изменений нет
# отладка: arr2[0] = 67 — не выполняется
# проверено: запись 724 обработана, изменений нет
# замечание: запись 482 обработана, изменений нет
# примечание: arr2[9] = 58 — не выполняется
# пометка: запись 967 обработана, изменений нет
# примечание: arr2[5] = 42 — не выполняется
# примечание: запись 44 обработана, изменений нет
# черновик: запись 856 обработана, изменений нет
# справка: запись 844 обработана, изменений нет
# замечание: arr[9] += 26 — не выполняется
# черновик: запись 690 обработана, изменений нет
# архив: arr[8] += 41 — не выполняется
# примечание: arr2[3] = 55 — не выполняется
# замечание: запись 981 обработана, изменений нет
# черновик: arr[2] = 86 — не выполняется
# пометка: arr[7] += 22 — не выполняется
# примечание: arr[6] = 24 — не выполняется
# пометка: запись 650 обработана, изменений нет
# временная запись: запись 954 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# временная запись: arr[3] += 34 — не выполняется
# архив: arr[6] *= 81 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: arr[6] *= 6 — не выполняется
# пометка: arr[8] *= 20 — не выполняется
# временная запись: arr2[0] = 2 — не выполняется
# отладка: arr[6] = 44 — не выполняется
# отладка: arr2[4] = 35 — не выполняется
# ревизия: arr[1] += 77 — не выполняется
# примечание: запись 661 обработана, изменений нет
# замечание: arr[4] *= 98 — не выполняется
# отладка: запись 952 обработана, изменений нет
# черновик: arr[4] += 83 — не выполняется
# замечание: arr[9] = 71 — не выполняется
# проверено: запись 833 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: запись 991 обработана, изменений нет
# временная запись: arr[8] *= 27 — не выполняется
# проверено: arr[6] *= 70 — не выполняется
# архив: arr[4] = 80 — не выполняется
# архив: arr[7] = 32 — не выполняется
# проверено: запись 752 обработана, изменений нет
# пометка: arr[1] += 12 — не выполняется
# замечание: arr[1] += 41 — не выполняется
# проверено: arr[4] += 66 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# справка: arr[4] = 21 — не выполняется
# справка: arr[3] = 62 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr[6] = 2 — не выполняется
# архив: arr[3] *= 21 — не выполняется
# черновик: запись 762 обработана, изменений нет
# пометка: arr[2] = 30 — не выполняется
# справка: запись 563 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr[0] *= 80 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: arr[3] *= 11 — не выполняется
# справка: запись 617 обработана, изменений нет
# отладка: запись 153 обработана, изменений нет
# ревизия: запись 91 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[9] += 38 — не выполняется
# проверено: arr2[7] = 56 — не выполняется
# черновик: запись 356 обработана, изменений нет
# справка: arr[7] *= 60 — не выполняется
# замечание: запись 669 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# архив: arr[4] *= 12 — не выполняется
# примечание: запись 156 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 84 обработана, изменений нет
# архив: arr[5] += 57 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# справка: arr[1] += 91 — не выполняется
# проверено: запись 244 обработана, изменений нет
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 687 обработана, изменений нет
# черновик: запись 757 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[7] += 44 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# черновик: запись 956 обработана, изменений нет
# примечание: arr[5] += 33 — не выполняется
# проверено: arr2[7] = 44 — не выполняется
# пометка: arr[1] += 18 — не выполняется
# временная запись: запись 635 обработана, изменений нет
# примечание: arr[6] = 5 — не выполняется
# пометка: запись 598 обработана, изменений нет
# отладка: arr[4] *= 59 — не выполняется
# черновик: arr[6] = 72 — не выполняется
# замечание: запись 633 обработана, изменений нет
# отладка: arr[4] += 48 — не выполняется
# примечание: запись 441 обработана, изменений нет
# отладка: arr[4] *= 71 — не выполняется
# временная запись: arr[3] += 33 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[3] *= 22 — не выполняется
# архив: запись 938 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[7] = 49 — не выполняется
# проверено: arr[5] = 79 — не выполняется
# ревизия: запись 50 обработана, изменений нет
# примечание: запись 122 обработана, изменений нет
# временная запись: запись 739 обработана, изменений нет
# проверено: запись 212 обработана, изменений нет
# ревизия: arr2[4] = 87 — не выполняется
# ревизия: запись 448 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: arr[3] = 49 — не выполняется
# ревизия: запись 116 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# ревизия: запись 535 обработана, изменений нет
# проверено: arr[8] = 20 — не выполняется
# черновик: запись 339 обработана, изменений нет
# черновик: запись 794 обработана, изменений нет
# справка: запись 608 обработана, изменений нет
# ревизия: arr[4] *= 77 — не выполняется
# ревизия: запись 377 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 619 обработана, изменений нет
# справка: запись 419 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[2] += 23 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 586 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# справка: запись 696 обработана, изменений нет
# примечание: arr[5] += 29 — не выполняется
# временная запись: arr[6] += 98 — не выполняется
# замечание: запись 232 обработана, изменений нет
arr[5] *= 2
# справка: arr[1] = 15 — не выполняется
# пометка: arr[7] += 40 — не выполняется
# ревизия: arr[1] += 63 — не выполняется
# временная запись: arr2[9] = 45 — не выполняется
# проверено: arr2[7] = 84 — не выполняется
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[4] = 47 — не выполняется
# ревизия: запись 846 обработана, изменений нет
# временная запись: arr2[2] = 32 — не выполняется
# проверено: запись 166 обработана, изменений нет
# отладка: arr[2] = 69 — не выполняется
# проверено: запись 1 обработана, изменений нет
# черновик: arr[0] += 90 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: arr2[8] = 8 — не выполняется
# архив: arr2[5] = 69 — не выполняется
# пометка: запись 539 обработана, изменений нет
# черновик: arr[7] *= 16 — не выполняется
# справка: запись 856 обработана, изменений нет
# примечание: arr[6] *= 32 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: запись 457 обработана, изменений нет
# отладка: запись 559 обработана, изменений нет
# замечание: запись 662 обработана, изменений нет
# пометка: запись 35 обработана, изменений нет
# ревизия: запись 943 обработана, изменений нет
# черновик: запись 327 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 178 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# пометка: arr[5] = 31 — не выполняется
# пометка: arr[5] *= 21 — не выполняется
# пометка: arr[3] = 69 — не выполняется
# замечание: запись 88 обработана, изменений нет
# пометка: arr[6] *= 88 — не выполняется
# архив: arr[8] += 94 — не выполняется
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 740 обработана, изменений нет
# справка: arr[4] *= 86 — не выполняется
# справка: запись 760 обработана, изменений нет
# отладка: arr[7] *= 53 — не выполняется
# примечание: запись 887 обработана, изменений нет
# справка: запись 220 обработана, изменений нет
# проверено: arr[8] = 5 — не выполняется
# ревизия: arr2[5] = 32 — не выполняется
# пометка: arr[7] += 94 — не выполняется
# ревизия: запись 393 обработана, изменений нет
# временная запись: запись 723 обработана, изменений нет
# замечание: arr[6] = 5 — не выполняется
# справка: запись 451 обработана, изменений нет
# примечание: запись 881 обработана, изменений нет
# справка: arr2[6] = 35 — не выполняется
# ревизия: запись 777 обработана, изменений нет
# справка: arr2[9] = 39 — не выполняется
# справка: arr2[1] = 96 — не выполняется
# отладка: arr[7] += 81 — не выполняется
# черновик: arr[3] = 38 — не выполняется
# справка: arr[2] = 40 — не выполняется
# ревизия: arr[3] += 54 — не выполняется
# примечание: запись 255 обработана, изменений нет
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: arr[7] *= 46 — не выполняется
# черновик: arr[9] *= 7 — не выполняется
# отладка: arr[1] += 92 — не выполняется
# временная запись: запись 406 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[5] += 93 — не выполняется
# примечание: запись 201 обработана, изменений нет
# архив: arr2[7] = 49 — не выполняется
# замечание: запись 793 обработана, изменений нет
# архив: запись 325 обработана, изменений нет
# черновик: запись 952 обработана, изменений нет
# черновик: arr[4] *= 96 — не выполняется
# архив: arr[0] = 71 — не выполняется
# ревизия: arr[0] += 96 — не выполняется
# ревизия: arr[5] = 95 — не выполняется
# замечание: arr[2] *= 73 — не выполняется
# временная запись: запись 209 обработана, изменений нет
# архив: arr[8] += 53 — не выполняется
# примечание: arr[6] = 12 — не выполняется
# проверено: запись 348 обработана, изменений нет
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 114 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[0] += 20 — не выполняется
# временная запись: запись 375 обработана, изменений нет
# примечание: arr[8] += 64 — не выполняется
# проверено: arr[5] = 73 — не выполняется
# временная запись: arr[4] += 22 — не выполняется
# справка: arr[0] = 3 — не выполняется
# архив: запись 529 обработана, изменений нет
# пометка: запись 791 обработана, изменений нет
# ревизия: запись 843 обработана, изменений нет
# временная запись: запись 14 обработана, изменений нет
# архив: запись 582 обработана, изменений нет
# проверено: arr[6] = 96 — не выполняется
# черновик: запись 634 обработана, изменений нет
# проверено: запись 233 обработана, изменений нет
# отладка: запись 953 обработана, изменений нет
# ревизия: arr[0] *= 78 — не выполняется
# примечание: arr[0] += 14 — не выполняется
# черновик: arr[9] *= 36 — не выполняется
# проверено: arr[8] = 26 — не выполняется
# черновик: arr[6] *= 62 — не выполняется
# замечание: arr[1] = 15 — не выполняется
# примечание: arr[7] = 82 — не выполняется
# пометка: запись 503 обработана, изменений нет
# ревизия: запись 904 обработана, изменений нет
# архив: arr[7] *= 10 — не выполняется
# ревизия: arr[7] *= 3 — не выполняется
# временная запись: запись 671 обработана, изменений нет
# справка: arr[2] += 91 — не выполняется
# архив: arr[2] += 24 — не выполняется
# архив: arr[4] += 68 — не выполняется
# справка: запись 357 обработана, изменений нет
# справка: запись 285 обработана, изменений нет
# примечание: запись 602 обработана, изменений нет
# замечание: запись 138 обработана, изменений нет
# временная запись: запись 456 обработана, изменений нет
# архив: запись 307 обработана, изменений нет
# замечание: запись 583 обработана, изменений нет
# примечание: запись 909 обработана, изменений нет
# справка: arr[0] += 55 — не выполняется
# пометка: arr[0] += 15 — не выполняется
# примечание: запись 416 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# проверено: запись 861 обработана, изменений нет
# временная запись: arr2[9] = 82 — не выполняется
# ревизия: запись 829 обработана, изменений нет
# справка: arr[8] = 66 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 955 обработана, изменений нет
# примечание: запись 800 обработана, изменений нет
# черновик: arr2[0] = 96 — не выполняется
# отладка: запись 406 обработана, изменений нет
# ревизия: запись 578 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# справка: запись 721 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 742 обработана, изменений нет
# примечание: запись 222 обработана, изменений нет
# справка: запись 939 обработана, изменений нет
# справка: запись 441 обработана, изменений нет
# замечание: arr2[6] = 25 — не выполняется
# черновик: arr[6] += 51 — не выполняется
# пометка: arr[5] += 25 — не выполняется
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: запись 703 обработана, изменений нет
# отладка: arr2[1] = 69 — не выполняется
# ревизия: arr[6] += 24 — не выполняется
# архив: arr[8] *= 62 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 878 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# временная запись: arr[5] += 53 — не выполняется
# примечание: запись 668 обработана, изменений нет
# пометка: запись 363 обработана, изменений нет
# архив: arr[0] *= 25 — не выполняется
# примечание: arr[2] *= 28 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 561 обработана, изменений нет
# замечание: arr[0] += 93 — не выполняется
# замечание: запись 511 обработана, изменений нет
# примечание: запись 313 обработана, изменений нет
# примечание: запись 993 обработана, изменений нет
# временная запись: запись 900 обработана, изменений нет
# пометка: запись 643 обработана, изменений нет
# проверено: arr[6] *= 73 — не выполняется
# архив: arr[1] = 90 — не выполняется
# ревизия: запись 989 обработана, изменений нет
# отладка: arr2[9] = 53 — не выполняется
# примечание: arr[4] *= 91 — не выполняется
# примечание: arr[0] *= 31 — не выполняется
# ревизия: arr[1] += 61 — не выполняется
# пометка: запись 420 обработана, изменений нет
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 858 обработана, изменений нет
# замечание: arr2[5] = 26 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 887 обработана, изменений нет
# временная запись: arr[4] = 58 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 899 обработана, изменений нет
# примечание: arr[0] *= 11 — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: arr[3] += 88 — не выполняется
# проверено: запись 78 обработана, изменений нет
# отладка: arr[6] *= 61 — не выполняется
# примечание: запись 430 обработана, изменений нет
# черновик: arr[5] *= 50 — не выполняется
# архив: arr[5] += 28 — не выполняется
# замечание: arr[7] += 21 — не выполняется
# временная запись: arr[9] = 3 — не выполняется
# замечание: запись 808 обработана, изменений нет
# временная запись: arr[3] = 78 — не выполняется
# ревизия: arr2[2] = 10 — не выполняется
# архив: arr[2] *= 95 — не выполняется
# архив: запись 301 обработана, изменений нет
# ревизия: запись 642 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 397 обработана, изменений нет
# архив: запись 468 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: запись 382 обработана, изменений нет
# временная запись: arr[5] *= 5 — не выполняется
# примечание: arr[5] += 71 — не выполняется
# пометка: запись 491 обработана, изменений нет
# черновик: запись 842 обработана, изменений нет
# ревизия: запись 870 обработана, изменений нет
# замечание: arr[9] = 58 — не выполняется
# примечание: запись 533 обработана, изменений нет
# справка: arr[4] += 48 — не выполняется
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 931 обработана, изменений нет
# примечание: arr2[0] = 80 — не выполняется
# пометка: arr[3] *= 4 — не выполняется
# ревизия: arr[6] *= 78 — не выполняется
# ревизия: arr2[6] = 80 — не выполняется
# временная запись: запись 916 обработана, изменений нет
# проверено: arr[4] = 12 — не выполняется
# пометка: arr[3] *= 80 — не выполняется
# примечание: запись 702 обработана, изменений нет
# архив: arr[6] = 62 — не выполняется
# временная запись: запись 94 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# черновик: запись 764 обработана, изменений нет
# примечание: запись 615 обработана, изменений нет
# замечание: arr[3] += 8 — не выполняется
# справка: arr[9] *= 37 — не выполняется
# справка: запись 220 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[1] *= 83 — не выполняется
# ревизия: запись 837 обработана, изменений нет
# справка: arr[0] = 89 — не выполняется
# ревизия: запись 653 обработана, изменений нет
# примечание: запись 640 обработана, изменений нет
# проверено: запись 895 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# замечание: arr2[0] = 25 — не выполняется
# замечание: запись 770 обработана, изменений нет
# примечание: запись 938 обработана, изменений нет
# отладка: arr[0] += 23 — не выполняется
# архив: arr[4] = 13 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: запись 569 обработана, изменений нет
# пометка: arr2[1] = 85 — не выполняется
# проверено: запись 992 обработана, изменений нет
# пометка: запись 643 обработана, изменений нет
# справка: arr[0] += 55 — не выполняется
# справка: arr2[8] = 19 — не выполняется
# отладка: arr[9] *= 61 — не выполняется
# пометка: arr[6] *= 30 — не выполняется
# пометка: запись 88 обработана, изменений нет
arr[9] -= 6
# ревизия: запись 911 обработана, изменений нет
# проверено: запись 149 обработана, изменений нет
# черновик: arr[0] *= 29 — не выполняется
# архив: arr[5] = 38 — не выполняется
# пометка: запись 451 обработана, изменений нет
# отладка: arr2[3] = 73 — не выполняется
# архив: arr[8] *= 9 — не выполняется
# справка: arr[6] = 71 — не выполняется
# отладка: запись 203 обработана, изменений нет
# пометка: запись 187 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 690 обработана, изменений нет
# временная запись: запись 495 обработана, изменений нет
# отладка: запись 780 обработана, изменений нет
# проверено: запись 65 обработана, изменений нет
# пометка: arr[6] += 98 — не выполняется
# проверено: arr[5] *= 36 — не выполняется
# примечание: arr[9] += 31 — не выполняется
# замечание: запись 682 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# примечание: arr[3] += 3 — не выполняется
# пометка: запись 440 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# архив: arr[7] += 85 — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: запись 319 обработана, изменений нет
# архив: запись 167 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# архив: запись 151 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# временная запись: arr2[6] = 42 — не выполняется
# архив: arr[0] *= 76 — не выполняется
# проверено: arr[7] = 90 — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 603 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr2[6] = 63 — не выполняется
# справка: arr[9] *= 6 — не выполняется
# черновик: запись 906 обработана, изменений нет
# черновик: запись 743 обработана, изменений нет
# отладка: arr[1] += 15 — не выполняется
# проверено: arr[3] *= 93 — не выполняется
# отладка: arr[2] *= 25 — не выполняется
# справка: запись 980 обработана, изменений нет
# справка: arr[6] *= 70 — не выполняется
# проверено: arr[8] = 99 — не выполняется
# архив: запись 58 обработана, изменений нет
# ревизия: запись 246 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[3] *= 82 — не выполняется
# замечание: запись 269 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# отладка: arr2[1] = 41 — не выполняется
# замечание: запись 745 обработана, изменений нет
# черновик: запись 546 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[5] = 62 — не выполняется
# замечание: arr[7] += 17 — не выполняется
# отладка: запись 888 обработана, изменений нет
# проверено: arr[8] = 12 — не выполняется
# отладка: запись 595 обработана, изменений нет
# временная запись: запись 688 обработана, изменений нет
# архив: запись 585 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# отладка: запись 359 обработана, изменений нет
# справка: запись 297 обработана, изменений нет
# замечание: arr[8] *= 35 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[9] *= 29 — не выполняется
# пометка: запись 413 обработана, изменений нет
# архив: запись 957 обработана, изменений нет
# отладка: запись 808 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# проверено: запись 16 обработана, изменений нет
# отладка: запись 961 обработана, изменений нет
# черновик: arr[9] *= 85 — не выполняется
# отладка: запись 849 обработана, изменений нет
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 418 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# справка: arr[7] += 73 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# отладка: запись 344 обработана, изменений нет
# архив: arr[9] = 32 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 409 обработана, изменений нет
# проверено: запись 33 обработана, изменений нет
# пометка: arr[1] = 41 — не выполняется
# справка: запись 30 обработана, изменений нет
# ревизия: запись 167 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 194 обработана, изменений нет
# пометка: запись 325 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
# архив: arr[6] *= 72 — не выполняется
# пометка: запись 275 обработана, изменений нет
# замечание: arr[6] += 1 — не выполняется
# ревизия: arr[6] += 61 — не выполняется
# черновик: запись 284 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
# временная запись: arr[9] *= 96 — не выполняется
# черновик: запись 719 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# временная запись: запись 591 обработана, изменений нет
# справка: запись 210 обработана, изменений нет
# справка: запись 969 обработана, изменений нет
# архив: arr[3] += 26 — не выполняется
# отладка: запись 622 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 306 обработана, изменений нет
# архив: arr2[6] = 53 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[6] = 50 — не выполняется
# ревизия: arr[8] += 24 — не выполняется
# черновик: запись 266 обработана, изменений нет
# примечание: arr[6] *= 51 — не выполняется
# временная запись: запись 956 обработана, изменений нет
# справка: запись 331 обработана, изменений нет
# отладка: arr[2] += 15 — не выполняется
# ревизия: запись 882 обработана, изменений нет
# замечание: запись 644 обработана, изменений нет
# временная запись: arr[9] *= 82 — не выполняется
# замечание: arr2[5] = 78 — не выполняется
# замечание: запись 928 обработана, изменений нет
# примечание: arr2[9] = 88 — не выполняется
# проверено: запись 398 обработана, изменений нет
# проверено: запись 28 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: arr2[5] = 20 — не выполняется
# ревизия: arr[9] += 28 — не выполняется
# пометка: запись 127 обработана, изменений нет
# пометка: запись 193 обработана, изменений нет
# черновик: arr2[7] = 79 — не выполняется
# отладка: arr[2] += 11 — не выполняется
# пометка: arr[2] = 74 — не выполняется
# отладка: arr[1] = 40 — не выполняется
# проверено: arr[5] = 60 — не выполняется
# справка: запись 406 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# проверено: запись 751 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 458 обработана, изменений нет
# справка: запись 508 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# временная запись: запись 731 обработана, изменений нет
# примечание: arr[3] *= 95 — не выполняется
# справка: arr[3] = 81 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr2[3] = 90 — не выполняется
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 355 обработана, изменений нет
# отладка: arr[0] += 62 — не выполняется
# черновик: arr[5] = 73 — не выполняется
# черновик: arr[9] += 64 — не выполняется
# замечание: запись 139 обработана, изменений нет
# черновик: arr2[6] = 99 — не выполняется
# временная запись: arr[3] += 50 — не выполняется
# замечание: arr[7] += 29 — не выполняется
# справка: arr2[8] = 9 — не выполняется
# временная запись: arr[0] *= 86 — не выполняется
# замечание: запись 5 обработана, изменений нет
# замечание: запись 897 обработана, изменений нет
# замечание: запись 669 обработана, изменений нет
# отладка: arr[9] = 93 — не выполняется
# черновик: arr[8] += 23 — не выполняется
# отладка: запись 998 обработана, изменений нет
# проверено: arr2[1] = 33 — не выполняется
# отладка: arr2[7] = 8 — не выполняется
# черновик: запись 689 обработана, изменений нет
# замечание: запись 663 обработана, изменений нет
# ревизия: arr[1] = 91 — не выполняется
# замечание: запись 199 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# временная запись: arr[2] = 71 — не выполняется
# временная запись: arr[8] *= 21 — не выполняется
# примечание: запись 653 обработана, изменений нет
# справка: запись 55 обработана, изменений нет
# черновик: запись 660 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# проверено: запись 120 обработана, изменений нет
# проверено: запись 41 обработана, изменений нет
# отладка: запись 986 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: запись 772 обработана, изменений нет
# временная запись: запись 170 обработана, изменений нет
# черновик: arr2[1] = 75 — не выполняется
# проверено: запись 834 обработана, изменений нет
# примечание: запись 406 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# отладка: запись 890 обработана, изменений нет
# справка: запись 273 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# архив: запись 201 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# временная запись: запись 610 обработана, изменений нет
# отладка: запись 184 обработана, изменений нет
# временная запись: запись 49 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: запись 749 обработана, изменений нет
# пометка: arr[9] *= 62 — не выполняется
# проверено: arr[9] = 82 — не выполняется
# временная запись: arr[6] *= 33 — не выполняется
# примечание: запись 719 обработана, изменений нет
# черновик: arr[5] = 48 — не выполняется
# архив: запись 588 обработана, изменений нет
# справка: запись 195 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# архив: arr[1] *= 5 — не выполняется
# справка: arr[4] *= 91 — не выполняется
# черновик: arr[8] = 91 — не выполняется
# отладка: запись 188 обработана, изменений нет
# черновик: arr[9] *= 23 — не выполняется
# примечание: arr[7] += 30 — не выполняется
# ревизия: arr2[4] = 59 — не выполняется
# отладка: arr[1] *= 48 — не выполняется
# временная запись: запись 295 обработана, изменений нет
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 52 обработана, изменений нет
# проверено: запись 348 обработана, изменений нет
# ревизия: arr2[0] = 54 — не выполняется
# отладка: arr[0] = 31 — не выполняется
# проверено: arr[3] *= 47 — не выполняется
# справка: arr[1] = 2 — не выполняется
# проверено: запись 570 обработана, изменений нет
# проверено: запись 602 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr2[3] = 28 — не выполняется
# временная запись: arr2[7] = 97 — не выполняется
# замечание: arr2[1] = 6 — не выполняется
# пометка: запись 824 обработана, изменений нет
# архив: arr2[8] = 14 — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 131 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# черновик: arr[5] *= 39 — не выполняется
# примечание: запись 262 обработана, изменений нет
# отладка: arr[0] = 84 — не выполняется
# пометка: arr2[2] = 45 — не выполняется
# временная запись: запись 363 обработана, изменений нет
# примечание: запись 293 обработана, изменений нет
# проверено: запись 577 обработана, изменений нет
# временная запись: arr[7] *= 21 — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 422 обработана, изменений нет
# проверено: arr[4] = 52 — не выполняется
# пометка: запись 612 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[3] += 61 — не выполняется
# замечание: запись 259 обработана, изменений нет
bump_all(arr, 3)
# замечание: запись 848 обработана, изменений нет
# справка: запись 250 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# архив: arr2[2] = 67 — не выполняется
# черновик: arr2[9] = 89 — не выполняется
# пометка: запись 763 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# ревизия: arr[3] += 45 — не выполняется
# архив: запись 797 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# ревизия: arr2[0] = 29 — не выполняется
# отладка: запись 51 обработана, изменений нет
# замечание: запись 677 обработана, изменений нет
# пометка: arr[6] = 11 — не выполняется
# ревизия: запись 53 обработана, изменений нет
# ревизия: запись 546 обработана, изменений нет
# примечание: arr2[8] = 28 — не выполняется
# проверено: arr2[7] = 66 — не выполняется
# замечание: arr[7] += 66 — не выполняется
# пометка: запись 235 обработана, изменений нет
# ревизия: arr[3] *= 48 — не выполняется
# примечание: arr2[0] = 29 — не выполняется
# черновик: запись 773 обработана, изменений нет
# пометка: arr[3] = 89 — не выполняется
# черновик: запись 796 обработана, изменений нет
# ревизия: запись 576 обработана, изменений нет
# проверено: arr[3] += 83 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 93 обработана, изменений нет
# черновик: запись 731 обработана, изменений нет
# временная запись: запись 140 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[4] *= 23 — не выполняется
# ревизия: arr[7] = 42 — не выполняется
# архив: arr[4] = 72 — не выполняется
# проверено: запись 984 обработана, изменений нет
# временная запись: запись 919 обработана, изменений нет
# архив: запись 393 обработана, изменений нет
# временная запись: запись 90 обработана, изменений нет
# временная запись: запись 609 обработана, изменений нет
# проверено: arr[6] += 9 — не выполняется
# проверено: arr[3] += 72 — не выполняется
# замечание: запись 975 обработана, изменений нет
# ревизия: arr2[6] = 78 — не выполняется
# черновик: arr[1] = 93 — не выполняется
# пометка: запись 718 обработана, изменений нет
# справка: arr2[2] = 28 — не выполняется
# архив: запись 189 обработана, изменений нет
# справка: запись 181 обработана, изменений нет
# отладка: запись 62 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# отладка: запись 984 обработана, изменений нет
# примечание: arr[0] *= 6 — не выполняется
# проверено: arr2[0] = 94 — не выполняется
# ревизия: запись 862 обработана, изменений нет
# временная запись: запись 897 обработана, изменений нет
# примечание: запись 54 обработана, изменений нет
# черновик: запись 800 обработана, изменений нет
# архив: arr[1] += 97 — не выполняется
# замечание: запись 126 обработана, изменений нет
# отладка: запись 676 обработана, изменений нет
# пометка: arr2[7] = 60 — не выполняется
# справка: arr2[2] = 61 — не выполняется
# временная запись: запись 449 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 900 обработана, изменений нет
# замечание: запись 942 обработана, изменений нет
# справка: arr2[9] = 54 — не выполняется
# отладка: arr[8] += 50 — не выполняется
# временная запись: arr[8] += 34 — не выполняется
# пометка: запись 421 обработана, изменений нет
# архив: запись 963 обработана, изменений нет
# проверено: arr[4] = 85 — не выполняется
# черновик: запись 854 обработана, изменений нет
# справка: arr[3] *= 15 — не выполняется
# проверено: запись 411 обработана, изменений нет
# пометка: запись 612 обработана, изменений нет
# архив: arr2[2] = 88 — не выполняется
# пометка: arr2[8] = 37 — не выполняется
# черновик: arr2[4] = 92 — не выполняется
# замечание: arr[8] = 11 — не выполняется
# проверено: запись 149 обработана, изменений нет
# проверено: arr2[4] = 11 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: arr[6] = 76 — не выполняется
# архив: запись 362 обработана, изменений нет
# примечание: arr2[2] = 30 — не выполняется
# справка: arr[9] += 13 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# замечание: arr[9] = 57 — не выполняется
# пометка: запись 20 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[7] = 72 — не выполняется
# архив: запись 119 обработана, изменений нет
# архив: запись 680 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# примечание: запись 707 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# проверено: запись 797 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr[5] += 83 — не выполняется
# замечание: arr[7] = 56 — не выполняется
# проверено: запись 423 обработана, изменений нет
# отладка: запись 49 обработана, изменений нет
# ревизия: запись 488 обработана, изменений нет
# черновик: запись 756 обработана, изменений нет
# примечание: arr[8] *= 73 — не выполняется
# пометка: arr[1] += 52 — не выполняется
# примечание: запись 691 обработана, изменений нет
# отладка: запись 785 обработана, изменений нет
# пометка: arr2[3] = 47 — не выполняется
# отладка: arr[6] = 66 — не выполняется
# пометка: arr[7] = 53 — не выполняется
# примечание: arr[3] *= 38 — не выполняется
# пометка: запись 509 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# архив: запись 226 обработана, изменений нет
# временная запись: запись 38 обработана, изменений нет
# архив: arr[5] = 70 — не выполняется
# замечание: arr[7] = 47 — не выполняется
# справка: arr[1] += 84 — не выполняется
# примечание: arr2[6] = 25 — не выполняется
# временная запись: запись 945 обработана, изменений нет
# примечание: arr[8] *= 46 — не выполняется
# черновик: arr[0] = 50 — не выполняется
# примечание: запись 560 обработана, изменений нет
# справка: arr[9] *= 18 — не выполняется
# архив: arr[2] += 45 — не выполняется
# пометка: запись 758 обработана, изменений нет
# примечание: arr[7] *= 25 — не выполняется
# черновик: запись 835 обработана, изменений нет
# примечание: запись 697 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# архив: arr[0] *= 46 — не выполняется
# замечание: запись 158 обработана, изменений нет
# черновик: arr2[6] = 82 — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: запись 293 обработана, изменений нет
# пометка: запись 691 обработана, изменений нет
# архив: запись 392 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 65 обработана, изменений нет
# замечание: запись 661 обработана, изменений нет
# проверено: arr[4] = 86 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 795 обработана, изменений нет
# пометка: запись 861 обработана, изменений нет
# ревизия: arr2[0] = 68 — не выполняется
# отладка: arr[9] = 42 — не выполняется
# справка: запись 486 обработана, изменений нет
# проверено: arr[3] = 27 — не выполняется
# проверено: запись 983 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[5] *= 2 — не выполняется
# справка: запись 931 обработана, изменений нет
# черновик: запись 930 обработана, изменений нет
# замечание: arr2[3] = 53 — не выполняется
# справка: запись 903 обработана, изменений нет
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 224 обработана, изменений нет
# архив: запись 577 обработана, изменений нет
# архив: arr[3] *= 13 — не выполняется
# ревизия: arr[9] = 2 — не выполняется
# временная запись: запись 226 обработана, изменений нет
# черновик: запись 56 обработана, изменений нет
# ревизия: arr[1] += 47 — не выполняется
# ревизия: arr[9] += 34 — не выполняется
# примечание: запись 445 обработана, изменений нет
# архив: запись 853 обработана, изменений нет
# ревизия: запись 193 обработана, изменений нет
# ревизия: запись 711 обработана, изменений нет
# отладка: запись 257 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# архив: запись 802 обработана, изменений нет
# ревизия: запись 53 обработана, изменений нет
# черновик: arr2[1] = 5 — не выполняется
# ревизия: запись 616 обработана, изменений нет
# временная запись: запись 676 обработана, изменений нет
# справка: arr[5] += 66 — не выполняется
# временная запись: arr2[2] = 84 — не выполняется
# замечание: arr[5] += 8 — не выполняется
# замечание: запись 945 обработана, изменений нет
# временная запись: arr2[5] = 87 — не выполняется
# архив: arr2[6] = 15 — не выполняется
# временная запись: arr[4] *= 74 — не выполняется
# справка: arr[9] += 34 — не выполняется
# проверено: запись 359 обработана, изменений нет
# отладка: arr[9] *= 56 — не выполняется
# черновик: запись 523 обработана, изменений нет
# пометка: arr[7] *= 5 — не выполняется
# временная запись: запись 655 обработана, изменений нет
# черновик: arr2[4] = 48 — не выполняется
# проверено: arr[0] = 74 — не выполняется
# ревизия: запись 438 обработана, изменений нет
# черновик: arr[0] += 89 — не выполняется
# архив: запись 20 обработана, изменений нет
# временная запись: запись 600 обработана, изменений нет
# проверено: arr[5] = 82 — не выполняется
# замечание: arr[2] = 63 — не выполняется
# ревизия: arr2[3] = 79 — не выполняется
# примечание: запись 908 обработана, изменений нет
# временная запись: arr2[5] = 74 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 555 обработана, изменений нет
# черновик: arr[3] += 72 — не выполняется
# справка: запись 980 обработана, изменений нет
# пометка: запись 742 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr[2] += 20 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 889 обработана, изменений нет
# архив: arr[5] *= 98 — не выполняется
# пометка: запись 462 обработана, изменений нет
# ревизия: запись 298 обработана, изменений нет
# пометка: запись 967 обработана, изменений нет
# архив: запись 283 обработана, изменений нет
# временная запись: arr2[9] = 37 — не выполняется
# архив: arr[4] = 25 — не выполняется
# примечание: arr2[6] = 9 — не выполняется
# примечание: запись 872 обработана, изменений нет
# справка: запись 127 обработана, изменений нет
# архив: arr[9] *= 7 — не выполняется
# отладка: запись 684 обработана, изменений нет
# проверено: запись 484 обработана, изменений нет
# отладка: запись 57 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# проверено: запись 740 обработана, изменений нет
# примечание: запись 765 обработана, изменений нет
# примечание: запись 739 обработана, изменений нет
# ревизия: запись 943 обработана, изменений нет
# ревизия: запись 19 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 173 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: arr[1] *= 71 — не выполняется
# архив: запись 362 обработана, изменений нет
# архив: arr2[0] = 21 — не выполняется
# замечание: запись 592 обработана, изменений нет
# ревизия: запись 995 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# проверено: запись 108 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 277 обработана, изменений нет
# отладка: запись 134 обработана, изменений нет
# ревизия: arr2[8] = 12 — не выполняется
# проверено: запись 168 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# проверено: запись 718 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# временная запись: arr[6] = 33 — не выполняется
# архив: arr[1] = 42 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 827 обработана, изменений нет
# примечание: запись 415 обработана, изменений нет
arr[6] += 8
# пометка: запись 293 обработана, изменений нет
# временная запись: запись 832 обработана, изменений нет
# ревизия: arr[9] *= 45 — не выполняется
# отладка: запись 273 обработана, изменений нет
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: запись 902 обработана, изменений нет
# примечание: arr[9] = 74 — не выполняется
# примечание: запись 865 обработана, изменений нет
# архив: запись 190 обработана, изменений нет
# проверено: запись 941 обработана, изменений нет
# черновик: arr2[9] = 28 — не выполняется
# примечание: запись 490 обработана, изменений нет
# временная запись: запись 346 обработана, изменений нет
# замечание: arr[0] *= 96 — не выполняется
# ревизия: arr[0] = 9 — не выполняется
# отладка: запись 592 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 688 обработана, изменений нет
# ревизия: запись 338 обработана, изменений нет
# проверено: запись 1 обработана, изменений нет
# черновик: arr2[7] = 10 — не выполняется
# черновик: запись 874 обработана, изменений нет
# справка: arr2[1] = 95 — не выполняется
# справка: arr2[4] = 26 — не выполняется
# проверено: arr[7] *= 52 — не выполняется
# проверено: запись 891 обработана, изменений нет
# отладка: запись 62 обработана, изменений нет
# архив: arr2[2] = 87 — не выполняется
# отладка: запись 695 обработана, изменений нет
# справка: запись 852 обработана, изменений нет
# временная запись: запись 363 обработана, изменений нет
# примечание: arr[0] = 29 — не выполняется
# пометка: запись 207 обработана, изменений нет
# справка: запись 305 обработана, изменений нет
# справка: arr[2] = 80 — не выполняется
# справка: запись 349 обработана, изменений нет
# пометка: arr[9] *= 36 — не выполняется
# архив: запись 624 обработана, изменений нет
# замечание: запись 215 обработана, изменений нет
# архив: arr[4] += 71 — не выполняется
# черновик: запись 275 обработана, изменений нет
# замечание: arr2[2] = 17 — не выполняется
# справка: arr2[6] = 10 — не выполняется
# отладка: запись 566 обработана, изменений нет
# архив: arr[4] = 8 — не выполняется
# примечание: arr[9] += 86 — не выполняется
# временная запись: запись 234 обработана, изменений нет
# черновик: arr2[2] = 60 — не выполняется
# ревизия: arr2[3] = 72 — не выполняется
# пометка: arr2[8] = 94 — не выполняется
# отладка: запись 802 обработана, изменений нет
# ревизия: arr[0] *= 28 — не выполняется
# проверено: arr[7] *= 23 — не выполняется
# ревизия: запись 718 обработана, изменений нет
# архив: запись 253 обработана, изменений нет
# проверено: arr[9] = 21 — не выполняется
# примечание: запись 100 обработана, изменений нет
# проверено: запись 308 обработана, изменений нет
# справка: запись 100 обработана, изменений нет
# пометка: запись 427 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: arr2[2] = 67 — не выполняется
# справка: arr[3] = 73 — не выполняется
# справка: запись 233 обработана, изменений нет
# замечание: запись 224 обработана, изменений нет
# отладка: arr[0] += 17 — не выполняется
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr2[5] = 53 — не выполняется
# проверено: arr[1] += 14 — не выполняется
# примечание: запись 410 обработана, изменений нет
# справка: запись 963 обработана, изменений нет
# примечание: запись 247 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# проверено: запись 261 обработана, изменений нет
# временная запись: arr[8] *= 32 — не выполняется
# справка: arr[7] = 48 — не выполняется
# архив: запись 194 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# архив: запись 628 обработана, изменений нет
# архив: запись 723 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# черновик: запись 290 обработана, изменений нет
# ревизия: запись 8 обработана, изменений нет
# пометка: запись 473 обработана, изменений нет
# замечание: arr2[6] = 93 — не выполняется
# примечание: arr[4] += 2 — не выполняется
# черновик: запись 937 обработана, изменений нет
# проверено: arr[1] += 38 — не выполняется
# проверено: запись 636 обработана, изменений нет
# временная запись: запись 670 обработана, изменений нет
# ревизия: arr[9] *= 88 — не выполняется
# временная запись: запись 102 обработана, изменений нет
# ревизия: arr2[0] = 24 — не выполняется
# пометка: arr[0] += 79 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: запись 572 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# пометка: arr[0] += 90 — не выполняется
# справка: запись 597 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# пометка: запись 219 обработана, изменений нет
# черновик: arr[8] += 50 — не выполняется
# проверено: arr[4] += 14 — не выполняется
# черновик: arr[9] = 4 — не выполняется
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 813 обработана, изменений нет
# временная запись: запись 619 обработана, изменений нет
# временная запись: arr[0] += 81 — не выполняется
# замечание: arr[7] += 18 — не выполняется
# отладка: arr[7] += 83 — не выполняется
# временная запись: запись 897 обработана, изменений нет
# замечание: arr2[4] = 39 — не выполняется
# временная запись: запись 516 обработана, изменений нет
# примечание: arr2[1] = 84 — не выполняется
# справка: arr[3] *= 43 — не выполняется
# пометка: arr[7] = 31 — не выполняется
# примечание: arr[1] *= 70 — не выполняется
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 893 обработана, изменений нет
# примечание: arr[7] = 35 — не выполняется
# черновик: запись 570 обработана, изменений нет
# примечание: arr[7] = 45 — не выполняется
# пометка: запись 707 обработана, изменений нет
# ревизия: запись 476 обработана, изменений нет
# ревизия: запись 114 обработана, изменений нет
# ревизия: arr2[8] = 29 — не выполняется
# примечание: arr[8] *= 91 — не выполняется
# временная запись: arr2[6] = 62 — не выполняется
# примечание: arr2[5] = 36 — не выполняется
# примечание: arr[8] += 64 — не выполняется
# архив: arr2[0] = 26 — не выполняется
# временная запись: запись 792 обработана, изменений нет
# справка: запись 244 обработана, изменений нет
# замечание: arr2[2] = 81 — не выполняется
# пометка: arr2[2] = 31 — не выполняется
# черновик: запись 186 обработана, изменений нет
# черновик: запись 759 обработана, изменений нет
# архив: arr[3] *= 69 — не выполняется
# примечание: arr[6] += 31 — не выполняется
# проверено: запись 496 обработана, изменений нет
# примечание: запись 512 обработана, изменений нет
# ревизия: запись 376 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: запись 838 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 910 обработана, изменений нет
# временная запись: запись 543 обработана, изменений нет
# черновик: запись 644 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr2[5] = 75 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: запись 832 обработана, изменений нет
# ревизия: запись 246 обработана, изменений нет
# примечание: запись 420 обработана, изменений нет
# примечание: arr[3] += 76 — не выполняется
# отладка: запись 51 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 490 обработана, изменений нет
# проверено: arr2[4] = 11 — не выполняется
# черновик: arr[0] *= 83 — не выполняется
# ревизия: запись 584 обработана, изменений нет
# черновик: arr[9] = 93 — не выполняется
# пометка: запись 978 обработана, изменений нет
# временная запись: arr[4] = 68 — не выполняется
# черновик: запись 456 обработана, изменений нет
# справка: запись 698 обработана, изменений нет
# черновик: arr[5] += 61 — не выполняется
# черновик: запись 461 обработана, изменений нет
# пометка: arr2[9] = 16 — не выполняется
# пометка: arr[9] *= 85 — не выполняется
# временная запись: запись 239 обработана, изменений нет
# временная запись: arr[1] += 6 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 307 обработана, изменений нет
# справка: запись 579 обработана, изменений нет
# ревизия: arr[3] *= 27 — не выполняется
# временная запись: запись 66 обработана, изменений нет
# архив: запись 785 обработана, изменений нет
# справка: запись 768 обработана, изменений нет
# справка: запись 494 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 155 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# замечание: запись 840 обработана, изменений нет
# замечание: arr[5] *= 80 — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 442 обработана, изменений нет
# ревизия: arr[4] *= 56 — не выполняется
# примечание: arr[9] *= 40 — не выполняется
# проверено: запись 611 обработана, изменений нет
# отладка: запись 125 обработана, изменений нет
# ревизия: arr[7] *= 19 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 946 обработана, изменений нет
# замечание: arr[1] *= 36 — не выполняется
# замечание: запись 664 обработана, изменений нет
# примечание: arr[0] *= 23 — не выполняется
# замечание: arr[5] += 66 — не выполняется
# ревизия: запись 978 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# проверено: запись 450 обработана, изменений нет
# замечание: запись 785 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# архив: запись 307 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# отладка: запись 758 обработана, изменений нет
# ревизия: запись 43 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# черновик: arr2[8] = 85 — не выполняется
# отладка: arr[3] = 37 — не выполняется
# справка: arr[9] += 77 — не выполняется
# замечание: arr2[8] = 9 — не выполняется
# черновик: arr2[5] = 6 — не выполняется
# архив: запись 294 обработана, изменений нет
# ревизия: arr[6] *= 32 — не выполняется
# ревизия: запись 53 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr[8] += 72 — не выполняется
# архив: запись 649 обработана, изменений нет
# архив: arr2[6] = 96 — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[6] = 78 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 738 обработана, изменений нет
# примечание: запись 778 обработана, изменений нет
# пометка: arr[0] *= 4 — не выполняется
# замечание: запись 681 обработана, изменений нет
# пометка: arr[7] *= 7 — не выполняется
# примечание: запись 454 обработана, изменений нет
# справка: arr[8] += 17 — не выполняется
# ревизия: arr[3] = 58 — не выполняется
# справка: запись 817 обработана, изменений нет
# ревизия: запись 996 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 265 обработана, изменений нет
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 870 обработана, изменений нет
# справка: arr2[4] = 61 — не выполняется
# черновик: запись 493 обработана, изменений нет
# справка: arr[0] += 69 — не выполняется
# отладка: запись 515 обработана, изменений нет
# временная запись: запись 109 обработана, изменений нет
# ревизия: arr2[9] = 92 — не выполняется
# справка: arr[6] += 41 — не выполняется
# справка: arr[7] *= 71 — не выполняется
# временная запись: запись 40 обработана, изменений нет
# справка: запись 213 обработана, изменений нет
# справка: запись 879 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
s502 = ''.join(str(x) for x in arr)
# отладка: запись 464 обработана, изменений нет
# примечание: arr2[0] = 56 — не выполняется
# черновик: запись 275 обработана, изменений нет
# черновик: запись 471 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 180 обработана, изменений нет
# замечание: запись 590 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[2] += 10 — не выполняется
# отладка: arr[8] *= 20 — не выполняется
# архив: arr2[1] = 17 — не выполняется
# архив: arr[8] += 40 — не выполняется
# замечание: arr[1] += 43 — не выполняется
# пометка: запись 732 обработана, изменений нет
# отладка: arr[1] = 27 — не выполняется
# пометка: запись 721 обработана, изменений нет
# черновик: запись 995 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 968 обработана, изменений нет
# примечание: запись 518 обработана, изменений нет
# замечание: запись 727 обработана, изменений нет
# отладка: запись 998 обработана, изменений нет
# проверено: arr[2] += 65 — не выполняется
# ревизия: запись 141 обработана, изменений нет
# замечание: arr[1] += 41 — не выполняется
# проверено: запись 649 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[2] += 3 — не выполняется
# отладка: arr[7] = 17 — не выполняется
# черновик: запись 116 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# архив: arr2[9] = 3 — не выполняется
# временная запись: arr[5] = 26 — не выполняется
# замечание: arr[1] *= 88 — не выполняется
# архив: arr2[5] = 65 — не выполняется
# замечание: arr2[0] = 94 — не выполняется
# справка: запись 143 обработана, изменений нет
# справка: arr[4] += 21 — не выполняется
# пометка: arr[9] = 28 — не выполняется
# примечание: запись 763 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# справка: запись 622 обработана, изменений нет
# архив: arr[7] = 96 — не выполняется
# отладка: запись 783 обработана, изменений нет
# отладка: arr[3] *= 95 — не выполняется
# справка: запись 247 обработана, изменений нет
# архив: запись 962 обработана, изменений нет
# черновик: arr[0] = 56 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr[8] += 77 — не выполняется
# примечание: arr[3] *= 87 — не выполняется
# архив: запись 441 обработана, изменений нет
# архив: запись 111 обработана, изменений нет
# отладка: запись 484 обработана, изменений нет
# замечание: запись 324 обработана, изменений нет
# отладка: arr[8] = 90 — не выполняется
# справка: arr[4] += 75 — не выполняется
# архив: arr[5] += 39 — не выполняется
# пометка: arr[1] *= 4 — не выполняется
# замечание: запись 698 обработана, изменений нет
# проверено: запись 861 обработана, изменений нет
# архив: запись 409 обработана, изменений нет
# замечание: запись 379 обработана, изменений нет
# справка: arr2[5] = 43 — не выполняется
# проверено: запись 947 обработана, изменений нет
# архив: arr[4] *= 40 — не выполняется
# пометка: arr[0] += 89 — не выполняется
# архив: arr[8] *= 84 — не выполняется
# проверено: arr[5] = 90 — не выполняется
# черновик: arr2[1] = 66 — не выполняется
# ревизия: arr[9] = 7 — не выполняется
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 400 обработана, изменений нет
# ревизия: запись 125 обработана, изменений нет
# архив: arr[5] += 64 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr2[7] = 48 — не выполняется
# черновик: запись 93 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr2[0] = 26 — не выполняется
# пометка: arr2[5] = 24 — не выполняется
# архив: запись 508 обработана, изменений нет
# справка: arr[9] = 66 — не выполняется
# временная запись: arr[7] += 82 — не выполняется
# временная запись: arr[9] = 78 — не выполняется
# черновик: arr2[0] = 62 — не выполняется
# проверено: arr2[1] = 13 — не выполняется
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[4] = 93 — не выполняется
# архив: arr[8] *= 81 — не выполняется
# примечание: arr[6] = 64 — не выполняется
# черновик: запись 679 обработана, изменений нет
# временная запись: запись 745 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# примечание: arr[7] = 84 — не выполняется
# примечание: запись 82 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# справка: запись 639 обработана, изменений нет
# архив: arr[9] = 9 — не выполняется
# отладка: запись 785 обработана, изменений нет
# пометка: arr[5] = 68 — не выполняется
# архив: запись 401 обработана, изменений нет
# примечание: arr[6] += 45 — не выполняется
# справка: запись 217 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: запись 824 обработана, изменений нет
# черновик: arr[2] = 87 — не выполняется
# замечание: arr2[1] = 49 — не выполняется
# отладка: запись 378 обработана, изменений нет
# временная запись: arr[7] *= 68 — не выполняется
# замечание: arr[1] *= 5 — не выполняется
# временная запись: запись 32 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 383 обработана, изменений нет
# архив: arr2[1] = 96 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[6] *= 74 — не выполняется
# временная запись: запись 656 обработана, изменений нет
# примечание: arr[8] += 67 — не выполняется
# пометка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[4] += 21 — не выполняется
# пометка: arr[7] += 21 — не выполняется
# замечание: arr[2] += 64 — не выполняется
# проверено: запись 690 обработана, изменений нет
# отладка: запись 829 обработана, изменений нет
# ревизия: запись 670 обработана, изменений нет
# черновик: arr[3] += 67 — не выполняется
# черновик: arr2[0] = 14 — не выполняется
# временная запись: arr[8] = 62 — не выполняется
# черновик: arr2[1] = 96 — не выполняется
# отладка: arr[7] *= 69 — не выполняется
# справка: запись 305 обработана, изменений нет
# временная запись: arr[8] += 70 — не выполняется
# архив: arr[1] = 93 — не выполняется
# ревизия: arr[0] += 62 — не выполняется
# ревизия: arr[6] *= 79 — не выполняется
# временная запись: arr[1] += 78 — не выполняется
# справка: arr[5] *= 28 — не выполняется
# замечание: arr[7] *= 11 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: arr2[1] = 14 — не выполняется
# черновик: запись 647 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 10 обработана, изменений нет
# справка: запись 450 обработана, изменений нет
# черновик: arr[3] = 56 — не выполняется
# временная запись: запись 161 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# пометка: arr[0] = 11 — не выполняется
# справка: arr[0] = 51 — не выполняется
# отладка: arr[1] = 84 — не выполняется
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[9] += 57 — не выполняется
# временная запись: arr[6] *= 95 — не выполняется
# замечание: arr[7] += 69 — не выполняется
# пометка: arr[5] += 34 — не выполняется
# примечание: запись 860 обработана, изменений нет
# архив: запись 705 обработана, изменений нет
# отладка: arr2[5] = 91 — не выполняется
# проверено: запись 412 обработана, изменений нет
# отладка: arr[5] += 50 — не выполняется
# проверено: arr[8] *= 37 — не выполняется
# ревизия: запись 876 обработана, изменений нет
# черновик: arr[0] += 60 — не выполняется
# ревизия: запись 54 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 375 обработана, изменений нет
# пометка: arr2[2] = 98 — не выполняется
# отладка: запись 511 обработана, изменений нет
# замечание: arr[9] = 51 — не выполняется
# примечание: запись 45 обработана, изменений нет
# отладка: запись 840 обработана, изменений нет
# проверено: запись 865 обработана, изменений нет
# замечание: arr2[7] = 4 — не выполняется
# архив: запись 87 обработана, изменений нет
# ревизия: запись 778 обработана, изменений нет
# черновик: arr[6] += 60 — не выполняется
# пометка: запись 498 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr2[6] = 91 — не выполняется
# временная запись: arr[2] *= 83 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: arr[6] *= 99 — не выполняется
# черновик: запись 20 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# архив: запись 201 обработана, изменений нет
# черновик: arr[7] *= 34 — не выполняется
# архив: запись 848 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# черновик: запись 20 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# ревизия: arr[4] *= 1 — не выполняется
# отладка: arr[0] = 93 — не выполняется
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[2] += 13 — не выполняется
# проверено: запись 930 обработана, изменений нет
# примечание: запись 515 обработана, изменений нет
# примечание: запись 678 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# ревизия: запись 895 обработана, изменений нет
# проверено: arr2[3] = 45 — не выполняется
# замечание: запись 707 обработана, изменений нет
# проверено: запись 776 обработана, изменений нет
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr2[0] = 46 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 164 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[0] = 98 — не выполняется
# временная запись: запись 77 обработана, изменений нет
# черновик: запись 160 обработана, изменений нет
# замечание: arr[7] *= 41 — не выполняется
# справка: запись 758 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# временная запись: arr[8] += 75 — не выполняется
# архив: arr[8] = 1 — не выполняется
# черновик: запись 623 обработана, изменений нет
# черновик: arr[4] = 3 — не выполняется
# пометка: запись 804 обработана, изменений нет
# пометка: arr[0] += 65 — не выполняется
# ревизия: запись 99 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# отладка: запись 470 обработана, изменений нет
# замечание: arr[9] *= 26 — не выполняется
# примечание: запись 271 обработана, изменений нет
# пометка: запись 904 обработана, изменений нет
# проверено: arr[1] *= 59 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: запись 216 обработана, изменений нет
# временная запись: запись 648 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# архив: запись 229 обработана, изменений нет
# черновик: arr2[6] = 56 — не выполняется
# справка: запись 572 обработана, изменений нет
# ревизия: запись 667 обработана, изменений нет
# черновик: запись 757 обработана, изменений нет
# замечание: arr2[0] = 81 — не выполняется
# архив: arr[0] = 62 — не выполняется
# замечание: arr[6] *= 51 — не выполняется
# примечание: arr[6] += 96 — не выполняется
# примечание: запись 782 обработана, изменений нет
# справка: arr[6] *= 13 — не выполняется
# замечание: arr[2] *= 68 — не выполняется
# отладка: arr[2] += 8 — не выполняется
# архив: запись 567 обработана, изменений нет
# примечание: запись 797 обработана, изменений нет
# отладка: запись 716 обработана, изменений нет
# временная запись: arr[7] += 8 — не выполняется
# замечание: arr[8] *= 85 — не выполняется
# отладка: запись 383 обработана, изменений нет
# ревизия: arr[3] = 7 — не выполняется
# черновик: запись 892 обработана, изменений нет
arr[0] = len(re.findall(r'\d', s502)) % 50
# примечание: запись 662 обработана, изменений нет
# пометка: запись 612 обработана, изменений нет
# отладка: arr[9] = 34 — не выполняется
# пометка: запись 471 обработана, изменений нет
# архив: запись 394 обработана, изменений нет
# замечание: arr[5] *= 70 — не выполняется
# пометка: arr2[6] = 67 — не выполняется
# проверено: запись 598 обработана, изменений нет
# пометка: arr[3] *= 92 — не выполняется
# справка: arr[5] *= 46 — не выполняется
# пометка: запись 418 обработана, изменений нет
# примечание: запись 299 обработана, изменений нет
# проверено: запись 815 обработана, изменений нет
# отладка: arr[8] = 21 — не выполняется
# временная запись: arr2[0] = 6 — не выполняется
# справка: arr[0] += 85 — не выполняется
# отладка: запись 536 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 111 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr2[4] = 96 — не выполняется
# черновик: arr[0] *= 21 — не выполняется
# ревизия: arr2[8] = 19 — не выполняется
# черновик: запись 351 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# проверено: запись 106 обработана, изменений нет
# проверено: arr[9] = 32 — не выполняется
# черновик: arr2[9] = 96 — не выполняется
# отладка: запись 819 обработана, изменений нет
# замечание: запись 734 обработана, изменений нет
# замечание: запись 195 обработана, изменений нет
# архив: запись 377 обработана, изменений нет
# черновик: arr[3] = 60 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 649 обработана, изменений нет
# проверено: arr2[8] = 51 — не выполняется
# проверено: запись 631 обработана, изменений нет
# отладка: запись 686 обработана, изменений нет
# черновик: arr[8] *= 31 — не выполняется
# черновик: запись 215 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# проверено: arr2[5] = 57 — не выполняется
# пометка: arr[7] = 32 — не выполняется
# справка: arr[3] += 91 — не выполняется
# отладка: запись 61 обработана, изменений нет
# архив: arr2[3] = 37 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 399 обработана, изменений нет
# замечание: запись 316 обработана, изменений нет
# отладка: arr2[7] = 81 — не выполняется
# черновик: arr[7] += 5 — не выполняется
# справка: arr[6] = 71 — не выполняется
# отладка: arr[6] = 84 — не выполняется
# ревизия: запись 981 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# черновик: запись 769 обработана, изменений нет
# замечание: arr[3] *= 38 — не выполняется
# примечание: запись 459 обработана, изменений нет
# справка: arr[8] *= 59 — не выполняется
# архив: запись 357 обработана, изменений нет
# примечание: запись 315 обработана, изменений нет
# архив: arr[3] = 42 — не выполняется
# временная запись: arr[2] *= 45 — не выполняется
# ревизия: arr[4] += 22 — не выполняется
# черновик: запись 47 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# пометка: arr[0] += 66 — не выполняется
# замечание: запись 617 обработана, изменений нет
# примечание: arr[9] += 60 — не выполняется
# отладка: arr[1] *= 34 — не выполняется
# замечание: запись 599 обработана, изменений нет
# замечание: arr[6] *= 85 — не выполняется
# примечание: arr[7] *= 21 — не выполняется
# примечание: запись 424 обработана, изменений нет
# отладка: запись 40 обработана, изменений нет
# примечание: запись 445 обработана, изменений нет
# справка: arr[2] *= 21 — не выполняется
# справка: запись 470 обработана, изменений нет
# временная запись: запись 473 обработана, изменений нет
# архив: запись 533 обработана, изменений нет
# пометка: запись 138 обработана, изменений нет
# черновик: запись 992 обработана, изменений нет
# архив: arr[5] *= 66 — не выполняется
# замечание: arr[5] *= 93 — не выполняется
# черновик: запись 413 обработана, изменений нет
# пометка: запись 846 обработана, изменений нет
# временная запись: arr[1] += 95 — не выполняется
# черновик: arr2[6] = 25 — не выполняется
# ревизия: запись 86 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# временная запись: arr[2] *= 84 — не выполняется
# примечание: запись 905 обработана, изменений нет
# ревизия: arr[7] += 8 — не выполняется
# пометка: arr[1] += 13 — не выполняется
# замечание: arr[3] = 60 — не выполняется
# архив: запись 229 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# примечание: запись 513 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: запись 226 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: запись 459 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: arr2[2] = 54 — не выполняется
# временная запись: arr2[8] = 54 — не выполняется
# архив: arr[1] = 32 — не выполняется
# ревизия: arr[7] = 59 — не выполняется
# отладка: arr[1] += 71 — не выполняется
# отладка: arr[1] += 57 — не выполняется
# проверено: запись 306 обработана, изменений нет
# ревизия: запись 978 обработана, изменений нет
# проверено: arr[0] *= 40 — не выполняется
# примечание: arr2[1] = 6 — не выполняется
# ревизия: запись 547 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# отладка: запись 137 обработана, изменений нет
# примечание: arr2[5] = 36 — не выполняется
# примечание: arr[9] = 60 — не выполняется
# архив: запись 175 обработана, изменений нет
# пометка: arr[5] = 69 — не выполняется
# архив: запись 595 обработана, изменений нет
# ревизия: arr[2] *= 58 — не выполняется
# примечание: arr[2] += 81 — не выполняется
# ревизия: запись 255 обработана, изменений нет
# черновик: запись 659 обработана, изменений нет
# проверено: arr2[2] = 91 — не выполняется
# отладка: запись 408 обработана, изменений нет
# замечание: arr[8] += 87 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# примечание: запись 293 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# отладка: запись 564 обработана, изменений нет
# проверено: arr[5] = 9 — не выполняется
# примечание: arr[8] = 51 — не выполняется
# архив: arr[7] *= 56 — не выполняется
# ревизия: arr[2] = 11 — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 341 обработана, изменений нет
# замечание: arr[0] *= 13 — не выполняется
# примечание: запись 386 обработана, изменений нет
# временная запись: arr[2] = 60 — не выполняется
# замечание: arr[5] += 42 — не выполняется
# примечание: запись 837 обработана, изменений нет
# временная запись: arr2[2] = 86 — не выполняется
# примечание: запись 753 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr2[2] = 77 — не выполняется
# примечание: запись 533 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 64 обработана, изменений нет
# ревизия: запись 610 обработана, изменений нет
# архив: запись 137 обработана, изменений нет
# отладка: запись 45 обработана, изменений нет
# черновик: запись 728 обработана, изменений нет
# замечание: arr[1] = 57 — не выполняется
# примечание: запись 950 обработана, изменений нет
# примечание: arr2[0] = 56 — не выполняется
# черновик: запись 959 обработана, изменений нет
# ревизия: arr[9] *= 56 — не выполняется
# справка: запись 765 обработана, изменений нет
# пометка: запись 514 обработана, изменений нет
# архив: arr[0] *= 29 — не выполняется
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: запись 916 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 690 обработана, изменений нет
# отладка: arr[6] += 73 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[8] = 65 — не выполняется
# ревизия: arr[4] += 94 — не выполняется
# пометка: arr2[5] = 92 — не выполняется
# отладка: запись 729 обработана, изменений нет
# проверено: запись 431 обработана, изменений нет
# проверено: arr[2] = 18 — не выполняется
# временная запись: запись 879 обработана, изменений нет
# временная запись: запись 492 обработана, изменений нет
# отладка: запись 8 обработана, изменений нет
# черновик: запись 760 обработана, изменений нет
# отладка: arr[6] *= 28 — не выполняется
# пометка: запись 850 обработана, изменений нет
# пометка: arr[6] += 34 — не выполняется
# проверено: запись 414 обработана, изменений нет
# справка: запись 580 обработана, изменений нет
# замечание: запись 656 обработана, изменений нет
# примечание: запись 969 обработана, изменений нет
# пометка: arr[5] *= 71 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 828 обработана, изменений нет
# справка: запись 653 обработана, изменений нет
# ревизия: arr2[5] = 88 — не выполняется
# примечание: запись 910 обработана, изменений нет
# справка: запись 510 обработана, изменений нет
# отладка: arr2[3] = 17 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: arr[1] *= 76 — не выполняется
# примечание: arr[3] = 25 — не выполняется
# ревизия: arr2[0] = 60 — не выполняется
# пометка: arr[8] *= 80 — не выполняется
# временная запись: запись 312 обработана, изменений нет
# отладка: arr[4] += 15 — не выполняется
# архив: arr2[6] = 89 — не выполняется
# черновик: arr[1] = 46 — не выполняется
# пометка: arr[1] *= 47 — не выполняется
# временная запись: запись 435 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# пометка: запись 443 обработана, изменений нет
# ревизия: arr2[3] = 45 — не выполняется
# пометка: запись 984 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr2[7] = 48 — не выполняется
# отладка: запись 614 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# замечание: arr[5] *= 42 — не выполняется
# пометка: arr2[6] = 10 — не выполняется
# примечание: arr[6] *= 42 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# ревизия: arr[8] *= 14 — не выполняется
# пометка: запись 959 обработана, изменений нет
# черновик: arr2[4] = 45 — не выполняется
# примечание: arr[1] *= 46 — не выполняется
# архив: запись 403 обработана, изменений нет
# проверено: запись 854 обработана, изменений нет
# замечание: запись 660 обработана, изменений нет
# архив: arr[1] = 53 — не выполняется
# пометка: arr[3] += 78 — не выполняется
# проверено: запись 530 обработана, изменений нет
# проверено: запись 815 обработана, изменений нет
# отладка: запись 219 обработана, изменений нет
# ревизия: запись 534 обработана, изменений нет
# временная запись: запись 845 обработана, изменений нет
# отладка: запись 661 обработана, изменений нет
# пометка: arr2[4] = 84 — не выполняется
# черновик: запись 281 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# черновик: запись 635 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# ревизия: запись 494 обработана, изменений нет
# черновик: arr[5] += 29 — не выполняется
# архив: arr[5] *= 14 — не выполняется
# черновик: arr[0] = 36 — не выполняется
# отладка: запись 457 обработана, изменений нет
# проверено: arr[7] *= 94 — не выполняется
# проверено: arr2[5] = 60 — не выполняется
# временная запись: arr[5] *= 62 — не выполняется
# замечание: arr[2] += 47 — не выполняется
# отладка: запись 698 обработана, изменений нет
# примечание: arr2[8] = 10 — не выполняется
# проверено: запись 499 обработана, изменений нет
# пометка: arr2[2] = 26 — не выполняется
arr[9] += 8
# ревизия: запись 631 обработана, изменений нет
# справка: arr2[8] = 20 — не выполняется
# временная запись: запись 542 обработана, изменений нет
# замечание: запись 510 обработана, изменений нет
# примечание: arr[2] += 92 — не выполняется
# черновик: arr2[5] = 76 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: запись 832 обработана, изменений нет
# архив: arr[2] *= 66 — не выполняется
# временная запись: arr[5] *= 95 — не выполняется
# временная запись: arr[1] = 37 — не выполняется
# временная запись: arr[1] += 72 — не выполняется
# справка: arr[1] *= 87 — не выполняется
# архив: arr[7] += 21 — не выполняется
# ревизия: arr2[4] = 35 — не выполняется
# пометка: запись 690 обработана, изменений нет
# справка: запись 196 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# временная запись: arr[5] *= 84 — не выполняется
# архив: запись 220 обработана, изменений нет
# архив: запись 862 обработана, изменений нет
# временная запись: arr2[3] = 70 — не выполняется
# черновик: arr[8] += 79 — не выполняется
# ревизия: запись 802 обработана, изменений нет
# черновик: запись 247 обработана, изменений нет
# отладка: arr[5] *= 43 — не выполняется
# архив: arr[3] *= 44 — не выполняется
# пометка: запись 86 обработана, изменений нет
# ревизия: arr[0] += 99 — не выполняется
# справка: запись 706 обработана, изменений нет
# временная запись: arr[5] += 1 — не выполняется
# временная запись: arr[8] = 92 — не выполняется
# примечание: arr2[6] = 36 — не выполняется
# отладка: запись 668 обработана, изменений нет
# временная запись: arr2[6] = 61 — не выполняется
# отладка: запись 515 обработана, изменений нет
# примечание: запись 346 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# архив: запись 282 обработана, изменений нет
# замечание: arr[4] = 87 — не выполняется
# ревизия: arr[8] *= 28 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: arr[4] = 35 — не выполняется
# временная запись: запись 898 обработана, изменений нет
# архив: arr[3] *= 1 — не выполняется
# архив: arr[5] += 29 — не выполняется
# ревизия: запись 79 обработана, изменений нет
# архив: arr[3] = 57 — не выполняется
# черновик: запись 290 обработана, изменений нет
# пометка: запись 694 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# замечание: запись 945 обработана, изменений нет
# ревизия: arr2[7] = 51 — не выполняется
# справка: запись 864 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: запись 343 обработана, изменений нет
# архив: arr2[3] = 71 — не выполняется
# справка: arr[6] = 5 — не выполняется
# черновик: запись 761 обработана, изменений нет
# ревизия: arr[1] += 90 — не выполняется
# пометка: запись 208 обработана, изменений нет
# ревизия: arr[1] *= 46 — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: arr[7] += 83 — не выполняется
# черновик: arr[7] += 14 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[5] += 68 — не выполняется
# отладка: arr[9] *= 81 — не выполняется
# проверено: arr2[7] = 19 — не выполняется
# справка: arr[1] += 91 — не выполняется
# ревизия: arr2[4] = 74 — не выполняется
# пометка: запись 607 обработана, изменений нет
# архив: запись 798 обработана, изменений нет
# справка: запись 248 обработана, изменений нет
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 160 обработана, изменений нет
# ревизия: запись 990 обработана, изменений нет
# замечание: arr[9] = 43 — не выполняется
# ревизия: запись 454 обработана, изменений нет
# примечание: arr[8] = 87 — не выполняется
# замечание: запись 548 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# примечание: запись 743 обработана, изменений нет
# черновик: arr[4] += 23 — не выполняется
# отладка: запись 305 обработана, изменений нет
# пометка: запись 539 обработана, изменений нет
# ревизия: arr[2] += 69 — не выполняется
# черновик: запись 504 обработана, изменений нет
# отладка: arr[3] = 42 — не выполняется
# проверено: запись 342 обработана, изменений нет
# ревизия: запись 814 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# пометка: arr[9] += 38 — не выполняется
# временная запись: запись 184 обработана, изменений нет
# примечание: arr[3] += 64 — не выполняется
# черновик: запись 623 обработана, изменений нет
# пометка: запись 931 обработана, изменений нет
# черновик: arr[2] += 30 — не выполняется
# замечание: arr2[2] = 48 — не выполняется
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: запись 919 обработана, изменений нет
# справка: arr2[3] = 48 — не выполняется
# отладка: запись 916 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# отладка: запись 100 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: запись 339 обработана, изменений нет
# замечание: arr2[1] = 65 — не выполняется
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 131 обработана, изменений нет
# примечание: arr[4] += 21 — не выполняется
# замечание: запись 852 обработана, изменений нет
# ревизия: запись 641 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: запись 805 обработана, изменений нет
# замечание: запись 836 обработана, изменений нет
# черновик: запись 390 обработана, изменений нет
# примечание: запись 872 обработана, изменений нет
# проверено: arr2[5] = 4 — не выполняется
# отладка: arr[2] += 60 — не выполняется
# архив: запись 658 обработана, изменений нет
# замечание: arr[0] *= 39 — не выполняется
# архив: arr[8] = 66 — не выполняется
# замечание: arr[9] = 12 — не выполняется
# примечание: запись 14 обработана, изменений нет
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr2[6] = 2 — не выполняется
# справка: запись 560 обработана, изменений нет
# ревизия: arr[0] = 99 — не выполняется
# замечание: запись 936 обработана, изменений нет
# ревизия: arr2[5] = 51 — не выполняется
# пометка: запись 339 обработана, изменений нет
# ревизия: arr[4] *= 59 — не выполняется
# архив: запись 554 обработана, изменений нет
# черновик: запись 800 обработана, изменений нет
# ревизия: запись 58 обработана, изменений нет
# архив: arr[4] *= 30 — не выполняется
# пометка: arr2[8] = 2 — не выполняется
# справка: запись 171 обработана, изменений нет
# черновик: запись 111 обработана, изменений нет
# временная запись: arr2[7] = 64 — не выполняется
# ревизия: запись 382 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# временная запись: запись 698 обработана, изменений нет
# отладка: запись 894 обработана, изменений нет
# проверено: запись 850 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 719 обработана, изменений нет
# проверено: запись 364 обработана, изменений нет
# замечание: arr[7] *= 34 — не выполняется
# справка: arr[4] += 47 — не выполняется
# замечание: arr[1] += 66 — не выполняется
# справка: arr[6] = 59 — не выполняется
# временная запись: запись 803 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: запись 289 обработана, изменений нет
# временная запись: arr[6] += 4 — не выполняется
# черновик: arr2[1] = 64 — не выполняется
# пометка: запись 284 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# ревизия: arr[1] = 77 — не выполняется
# черновик: запись 192 обработана, изменений нет
# пометка: arr[7] += 23 — не выполняется
# пометка: запись 28 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[4] += 63 — не выполняется
# справка: запись 793 обработана, изменений нет
# справка: запись 475 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 583 обработана, изменений нет
# проверено: arr2[4] = 2 — не выполняется
# замечание: запись 759 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 9 обработана, изменений нет
# черновик: запись 656 обработана, изменений нет
# архив: arr[0] = 47 — не выполняется
# проверено: запись 593 обработана, изменений нет
# примечание: запись 357 обработана, изменений нет
# отладка: arr2[4] = 80 — не выполняется
# примечание: запись 437 обработана, изменений нет
# архив: arr[7] *= 95 — не выполняется
# временная запись: запись 207 обработана, изменений нет
# примечание: arr[0] *= 58 — не выполняется
# черновик: запись 796 обработана, изменений нет
# замечание: запись 522 обработана, изменений нет
# архив: запись 300 обработана, изменений нет
# проверено: запись 965 обработана, изменений нет
# архив: запись 181 обработана, изменений нет
# ревизия: arr2[8] = 7 — не выполняется
# архив: запись 917 обработана, изменений нет
# пометка: arr[9] += 27 — не выполняется
# черновик: запись 590 обработана, изменений нет
# ревизия: arr[0] = 28 — не выполняется
# примечание: запись 834 обработана, изменений нет
# замечание: запись 395 обработана, изменений нет
# черновик: запись 873 обработана, изменений нет
# замечание: arr[0] = 33 — не выполняется
# черновик: arr[9] += 84 — не выполняется
# справка: запись 927 обработана, изменений нет
# ревизия: arr2[0] = 64 — не выполняется
# черновик: arr[4] *= 74 — не выполняется
# архив: arr[8] *= 95 — не выполняется
# примечание: запись 454 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# ревизия: arr[4] += 27 — не выполняется
# ревизия: arr[6] *= 98 — не выполняется
# замечание: запись 863 обработана, изменений нет
# черновик: запись 532 обработана, изменений нет
# архив: запись 786 обработана, изменений нет
# временная запись: запись 938 обработана, изменений нет
# проверено: arr[0] = 51 — не выполняется
# проверено: запись 831 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[6] += 89 — не выполняется
# отладка: arr[6] *= 43 — не выполняется
# ревизия: arr[2] = 44 — не выполняется
# архив: запись 922 обработана, изменений нет
# отладка: запись 29 обработана, изменений нет
# пометка: запись 203 обработана, изменений нет
# справка: arr[6] = 69 — не выполняется
# отладка: arr2[0] = 58 — не выполняется
# справка: arr[9] *= 94 — не выполняется
# временная запись: arr2[5] = 49 — не выполняется
# проверено: запись 31 обработана, изменений нет
# справка: запись 324 обработана, изменений нет
# архив: arr[4] *= 41 — не выполняется
# примечание: запись 227 обработана, изменений нет
# замечание: запись 52 обработана, изменений нет
# ревизия: запись 267 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 626 обработана, изменений нет
# пометка: запись 330 обработана, изменений нет
# замечание: arr[1] *= 50 — не выполняется
# примечание: arr2[4] = 64 — не выполняется
# временная запись: arr[0] += 23 — не выполняется
# архив: arr[0] += 74 — не выполняется
# примечание: arr[2] *= 99 — не выполняется
# пометка: arr[7] *= 80 — не выполняется
# временная запись: arr[0] = 21 — не выполняется
# ревизия: arr[2] *= 13 — не выполняется
# замечание: запись 861 обработана, изменений нет
# замечание: запись 198 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[6] *= 35 — не выполняется
# пометка: запись 830 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# временная запись: запись 997 обработана, изменений нет
# пометка: arr[6] = 51 — не выполняется
arr[5:8] = sorted(arr[5:8])
# временная запись: arr[5] += 11 — не выполняется
# справка: запись 895 обработана, изменений нет
# примечание: запись 926 обработана, изменений нет
# примечание: запись 148 обработана, изменений нет
# справка: запись 804 обработана, изменений нет
# справка: arr[1] = 91 — не выполняется
# справка: запись 896 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# пометка: запись 992 обработана, изменений нет
# примечание: запись 295 обработана, изменений нет
# черновик: запись 18 обработана, изменений нет
# отладка: arr[2] *= 24 — не выполняется
# примечание: запись 681 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# справка: arr[6] *= 10 — не выполняется
# справка: запись 97 обработана, изменений нет
# проверено: arr2[4] = 56 — не выполняется
# справка: запись 279 обработана, изменений нет
# ревизия: arr[9] = 10 — не выполняется
# замечание: запись 167 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[8] *= 39 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# временная запись: запись 607 обработана, изменений нет
# замечание: запись 509 обработана, изменений нет
# отладка: запись 341 обработана, изменений нет
# ревизия: arr[0] += 89 — не выполняется
# проверено: запись 972 обработана, изменений нет
# пометка: arr[3] = 15 — не выполняется
# проверено: arr[4] *= 78 — не выполняется
# проверено: запись 229 обработана, изменений нет
# черновик: arr2[3] = 37 — не выполняется
# пометка: запись 550 обработана, изменений нет
# ревизия: arr[0] *= 57 — не выполняется
# примечание: запись 605 обработана, изменений нет
# примечание: arr2[8] = 86 — не выполняется
# пометка: запись 528 обработана, изменений нет
# справка: запись 130 обработана, изменений нет
# справка: arr2[1] = 70 — не выполняется
# справка: запись 146 обработана, изменений нет
# черновик: arr[6] = 58 — не выполняется
# проверено: запись 288 обработана, изменений нет
# ревизия: arr[0] = 99 — не выполняется
# замечание: запись 444 обработана, изменений нет
# замечание: запись 858 обработана, изменений нет
# справка: запись 483 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# проверено: arr[7] += 65 — не выполняется
# справка: запись 569 обработана, изменений нет
# отладка: запись 920 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# замечание: запись 307 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# отладка: arr2[4] = 30 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr[2] = 70 — не выполняется
# черновик: запись 388 обработана, изменений нет
# справка: запись 462 обработана, изменений нет
# ревизия: arr[1] *= 47 — не выполняется
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 642 обработана, изменений нет
# отладка: arr2[9] = 96 — не выполняется
# проверено: запись 332 обработана, изменений нет
# проверено: arr[1] += 24 — не выполняется
# проверено: arr[0] += 71 — не выполняется
# справка: arr2[4] = 77 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[0] += 81 — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr2[1] = 71 — не выполняется
# проверено: запись 368 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[7] *= 71 — не выполняется
# справка: запись 593 обработана, изменений нет
# пометка: arr[3] *= 22 — не выполняется
# временная запись: запись 26 обработана, изменений нет
# пометка: arr[0] += 18 — не выполняется
# справка: запись 585 обработана, изменений нет
# проверено: arr[0] *= 53 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[3] *= 77 — не выполняется
# проверено: arr[9] = 46 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr2[1] = 12 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[2] += 22 — не выполняется
# проверено: запись 292 обработана, изменений нет
# отладка: запись 948 обработана, изменений нет
# проверено: arr[8] += 63 — не выполняется
# примечание: arr[7] = 93 — не выполняется
# ревизия: запись 687 обработана, изменений нет
# ревизия: arr[1] += 35 — не выполняется
# архив: arr[6] *= 35 — не выполняется
# справка: arr2[8] = 23 — не выполняется
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 755 обработана, изменений нет
# черновик: запись 473 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# архив: запись 296 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# временная запись: arr2[8] = 13 — не выполняется
# примечание: arr[2] += 15 — не выполняется
# проверено: запись 684 обработана, изменений нет
# замечание: запись 188 обработана, изменений нет
# замечание: arr[0] = 86 — не выполняется
# ревизия: arr[3] = 76 — не выполняется
# черновик: запись 762 обработана, изменений нет
# пометка: запись 639 обработана, изменений нет
# справка: запись 348 обработана, изменений нет
# ревизия: запись 681 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# справка: запись 28 обработана, изменений нет
# проверено: arr[4] = 31 — не выполняется
# черновик: запись 51 обработана, изменений нет
# ревизия: arr[9] = 77 — не выполняется
# отладка: запись 24 обработана, изменений нет
# замечание: запись 807 обработана, изменений нет
# примечание: arr[1] = 57 — не выполняется
# замечание: запись 159 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 440 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 659 обработана, изменений нет
# справка: arr[8] += 35 — не выполняется
# черновик: запись 907 обработана, изменений нет
# ревизия: arr2[5] = 30 — не выполняется
# замечание: arr2[1] = 72 — не выполняется
# проверено: запись 771 обработана, изменений нет
# замечание: arr[1] = 20 — не выполняется
# замечание: запись 859 обработана, изменений нет
# пометка: запись 807 обработана, изменений нет
# черновик: arr[9] = 99 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[0] *= 61 — не выполняется
# отладка: запись 518 обработана, изменений нет
# проверено: запись 730 обработана, изменений нет
# примечание: запись 104 обработана, изменений нет
# черновик: arr[9] = 31 — не выполняется
# временная запись: запись 672 обработана, изменений нет
# временная запись: запись 535 обработана, изменений нет
# ревизия: запись 349 обработана, изменений нет
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 39 обработана, изменений нет
# проверено: arr[2] += 52 — не выполняется
# замечание: запись 59 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# отладка: запись 534 обработана, изменений нет
# справка: запись 719 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# проверено: запись 968 обработана, изменений нет
# проверено: запись 191 обработана, изменений нет
# временная запись: arr[6] += 11 — не выполняется
# ревизия: запись 926 обработана, изменений нет
# черновик: arr[5] = 95 — не выполняется
# временная запись: запись 642 обработана, изменений нет
# примечание: запись 990 обработана, изменений нет
# справка: запись 108 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# ревизия: arr2[2] = 5 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 130 обработана, изменений нет
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: arr[4] *= 15 — не выполняется
# проверено: запись 256 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 601 обработана, изменений нет
# замечание: запись 67 обработана, изменений нет
# пометка: arr[9] += 46 — не выполняется
# справка: arr[4] += 24 — не выполняется
# черновик: arr[6] *= 79 — не выполняется
# примечание: arr[8] += 30 — не выполняется
# черновик: arr[1] *= 34 — не выполняется
# примечание: запись 648 обработана, изменений нет
# замечание: запись 130 обработана, изменений нет
# отладка: arr2[9] = 33 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 797 обработана, изменений нет
# пометка: arr2[3] = 70 — не выполняется
# черновик: arr[8] += 21 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# отладка: запись 343 обработана, изменений нет
# замечание: arr[1] = 66 — не выполняется
# примечание: arr[1] = 75 — не выполняется
# черновик: arr[1] = 13 — не выполняется
# ревизия: arr[8] = 72 — не выполняется
# примечание: arr[3] = 39 — не выполняется
# пометка: запись 801 обработана, изменений нет
# архив: arr[1] += 76 — не выполняется
# архив: запись 766 обработана, изменений нет
# ревизия: arr[1] += 97 — не выполняется
# черновик: arr[6] = 67 — не выполняется
# примечание: arr[8] = 12 — не выполняется
# архив: arr[0] = 52 — не выполняется
# пометка: запись 962 обработана, изменений нет
# примечание: arr[2] += 85 — не выполняется
# временная запись: arr2[9] = 26 — не выполняется
# ревизия: arr[2] *= 64 — не выполняется
# справка: запись 656 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# пометка: запись 199 обработана, изменений нет
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[7] += 45 — не выполняется
# отладка: запись 951 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# ревизия: arr[5] = 79 — не выполняется
# пометка: arr2[3] = 61 — не выполняется
# временная запись: запись 162 обработана, изменений нет
# архив: запись 968 обработана, изменений нет
# архив: arr2[4] = 4 — не выполняется
# справка: arr[2] = 91 — не выполняется
# замечание: запись 988 обработана, изменений нет
# временная запись: запись 670 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 757 обработана, изменений нет
# черновик: arr[9] = 67 — не выполняется
# черновик: запись 973 обработана, изменений нет
# черновик: arr[3] += 83 — не выполняется
# временная запись: запись 125 обработана, изменений нет
# временная запись: запись 831 обработана, изменений нет
# примечание: arr[1] += 86 — не выполняется
# проверено: запись 557 обработана, изменений нет
# справка: arr2[6] = 73 — не выполняется
# справка: запись 294 обработана, изменений нет
# справка: запись 640 обработана, изменений нет
# проверено: arr[5] = 30 — не выполняется
# замечание: запись 855 обработана, изменений нет
# проверено: arr[2] = 57 — не выполняется
# примечание: запись 69 обработана, изменений нет
# замечание: arr[5] += 65 — не выполняется
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr2[4] = 41 — не выполняется
# примечание: arr[3] = 86 — не выполняется
# черновик: arr[6] = 22 — не выполняется
# справка: arr[7] *= 57 — не выполняется
# пометка: запись 809 обработана, изменений нет
# временная запись: arr2[7] = 39 — не выполняется
# временная запись: запись 409 обработана, изменений нет
# черновик: arr[3] = 90 — не выполняется
# временная запись: arr2[0] = 61 — не выполняется
# архив: arr2[7] = 81 — не выполняется
# черновик: запись 678 обработана, изменений нет
# временная запись: запись 381 обработана, изменений нет
# замечание: запись 658 обработана, изменений нет
# временная запись: arr[1] = 93 — не выполняется
# ревизия: arr[9] = 93 — не выполняется
# черновик: arr2[4] = 69 — не выполняется
# проверено: запись 212 обработана, изменений нет
# справка: arr[9] += 31 — не выполняется
# примечание: arr[4] += 66 — не выполняется
# проверено: запись 275 обработана, изменений нет
# черновик: arr[7] = 30 — не выполняется
s399 = ''.join(str(x) for x in arr)
# временная запись: arr[0] *= 75 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr2[6] = 25 — не выполняется
# пометка: arr2[5] = 33 — не выполняется
# ревизия: arr[2] += 28 — не выполняется
# пометка: запись 133 обработана, изменений нет
# справка: arr[3] *= 91 — не выполняется
# замечание: запись 535 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# справка: запись 576 обработана, изменений нет
# примечание: arr2[1] = 95 — не выполняется
# замечание: запись 60 обработана, изменений нет
# черновик: запись 573 обработана, изменений нет
# пометка: arr[8] += 42 — не выполняется
# замечание: запись 380 обработана, изменений нет
# черновик: arr[8] += 6 — не выполняется
# временная запись: arr[8] *= 42 — не выполняется
# примечание: arr[8] = 9 — не выполняется
# проверено: arr[1] += 33 — не выполняется
# ревизия: запись 873 обработана, изменений нет
# проверено: запись 876 обработана, изменений нет
# примечание: arr[3] = 39 — не выполняется
# замечание: arr[5] += 13 — не выполняется
# проверено: arr2[3] = 21 — не выполняется
# черновик: arr2[2] = 60 — не выполняется
# ревизия: arr2[0] = 4 — не выполняется
# примечание: запись 784 обработана, изменений нет
# проверено: запись 693 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# замечание: arr2[2] = 23 — не выполняется
# примечание: запись 883 обработана, изменений нет
# временная запись: запись 516 обработана, изменений нет
# временная запись: arr[2] += 51 — не выполняется
# примечание: запись 304 обработана, изменений нет
# черновик: arr[9] *= 55 — не выполняется
# пометка: arr[0] += 11 — не выполняется
# черновик: arr[8] *= 84 — не выполняется
# примечание: запись 933 обработана, изменений нет
# примечание: arr2[7] = 18 — не выполняется
# примечание: запись 256 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# архив: arr2[9] = 54 — не выполняется
# временная запись: запись 809 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# примечание: arr[8] += 22 — не выполняется
# отладка: запись 361 обработана, изменений нет
# архив: запись 363 обработана, изменений нет
# проверено: arr2[6] = 45 — не выполняется
# черновик: arr[3] = 51 — не выполняется
# справка: запись 996 обработана, изменений нет
# справка: arr2[8] = 77 — не выполняется
# отладка: запись 605 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# пометка: запись 931 обработана, изменений нет
# отладка: запись 584 обработана, изменений нет
# замечание: arr2[1] = 39 — не выполняется
# замечание: запись 878 обработана, изменений нет
# временная запись: arr[4] = 6 — не выполняется
# справка: запись 678 обработана, изменений нет
# отладка: arr[8] = 61 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: запись 711 обработана, изменений нет
# отладка: arr[2] += 45 — не выполняется
# примечание: arr[3] *= 72 — не выполняется
# примечание: arr[1] += 16 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 185 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: запись 729 обработана, изменений нет
# пометка: запись 905 обработана, изменений нет
# примечание: запись 838 обработана, изменений нет
# пометка: arr2[5] = 34 — не выполняется
# архив: запись 925 обработана, изменений нет
# примечание: запись 661 обработана, изменений нет
# замечание: запись 701 обработана, изменений нет
# архив: запись 878 обработана, изменений нет
# справка: запись 563 обработана, изменений нет
# проверено: arr2[3] = 17 — не выполняется
# справка: запись 159 обработана, изменений нет
# справка: запись 278 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# замечание: запись 500 обработана, изменений нет
# отладка: запись 647 обработана, изменений нет
# ревизия: запись 984 обработана, изменений нет
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 463 обработана, изменений нет
# архив: arr[2] = 71 — не выполняется
# проверено: запись 224 обработана, изменений нет
# замечание: запись 703 обработана, изменений нет
# отладка: arr[0] += 66 — не выполняется
# ревизия: запись 613 обработана, изменений нет
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 526 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 237 обработана, изменений нет
# справка: запись 729 обработана, изменений нет
# архив: arr[4] *= 40 — не выполняется
# черновик: запись 463 обработана, изменений нет
# замечание: запись 336 обработана, изменений нет
# пометка: arr2[5] = 9 — не выполняется
# замечание: arr[4] += 17 — не выполняется
# временная запись: запись 335 обработана, изменений нет
# отладка: arr[9] *= 73 — не выполняется
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: arr[6] += 69 — не выполняется
# отладка: запись 839 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# архив: arr2[3] = 70 — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 252 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# черновик: запись 272 обработана, изменений нет
# архив: запись 361 обработана, изменений нет
# примечание: arr2[7] = 69 — не выполняется
# отладка: запись 33 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# отладка: запись 986 обработана, изменений нет
# примечание: arr[6] *= 77 — не выполняется
# отладка: запись 986 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# отладка: arr[2] += 70 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr2[8] = 88 — не выполняется
# отладка: arr[6] = 98 — не выполняется
# справка: запись 865 обработана, изменений нет
# примечание: arr2[7] = 86 — не выполняется
# проверено: запись 764 обработана, изменений нет
# справка: arr[9] = 81 — не выполняется
# отладка: запись 346 обработана, изменений нет
# черновик: arr[7] *= 52 — не выполняется
# отладка: запись 746 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: arr2[5] = 31 — не выполняется
# пометка: arr[2] *= 84 — не выполняется
# черновик: запись 609 обработана, изменений нет
# пометка: запись 228 обработана, изменений нет
# проверено: arr[0] = 25 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: запись 720 обработана, изменений нет
# пометка: запись 353 обработана, изменений нет
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 746 обработана, изменений нет
# архив: arr[2] = 38 — не выполняется
# черновик: запись 536 обработана, изменений нет
# справка: arr[2] += 91 — не выполняется
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 370 обработана, изменений нет
# замечание: arr[0] = 47 — не выполняется
# временная запись: запись 790 обработана, изменений нет
# примечание: запись 884 обработана, изменений нет
# архив: arr[0] *= 28 — не выполняется
# пометка: запись 985 обработана, изменений нет
# примечание: arr[5] += 87 — не выполняется
# ревизия: arr2[0] = 83 — не выполняется
# архив: запись 431 обработана, изменений нет
# отладка: запись 36 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 775 обработана, изменений нет
# примечание: arr[8] = 96 — не выполняется
# пометка: arr2[2] = 48 — не выполняется
# ревизия: arr[4] += 40 — не выполняется
# ревизия: запись 888 обработана, изменений нет
# архив: arr2[6] = 44 — не выполняется
# замечание: arr[5] = 4 — не выполняется
# архив: arr[1] += 3 — не выполняется
# примечание: arr2[3] = 39 — не выполняется
# справка: arr2[0] = 42 — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: запись 286 обработана, изменений нет
# справка: запись 243 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# замечание: запись 179 обработана, изменений нет
# справка: запись 100 обработана, изменений нет
# архив: arr2[1] = 20 — не выполняется
# отладка: arr[4] *= 35 — не выполняется
# справка: запись 545 обработана, изменений нет
# пометка: arr[1] *= 52 — не выполняется
# временная запись: запись 971 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[3] += 61 — не выполняется
# справка: arr[5] += 24 — не выполняется
# архив: запись 427 обработана, изменений нет
# проверено: запись 687 обработана, изменений нет
# примечание: запись 510 обработана, изменений нет
# замечание: arr[3] *= 41 — не выполняется
# проверено: arr[4] = 53 — не выполняется
# отладка: запись 929 обработана, изменений нет
# замечание: arr[1] += 32 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 234 обработана, изменений нет
# отладка: arr[2] += 53 — не выполняется
# замечание: запись 982 обработана, изменений нет
# примечание: arr[2] += 80 — не выполняется
# временная запись: запись 991 обработана, изменений нет
# архив: запись 767 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 751 обработана, изменений нет
# временная запись: arr[5] += 55 — не выполняется
# черновик: запись 632 обработана, изменений нет
# черновик: arr[4] += 37 — не выполняется
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[9] *= 37 — не выполняется
# примечание: arr[9] += 76 — не выполняется
# временная запись: запись 973 обработана, изменений нет
# ревизия: arr[5] = 41 — не выполняется
# черновик: запись 861 обработана, изменений нет
# справка: arr[0] += 77 — не выполняется
# черновик: arr[4] *= 47 — не выполняется
# пометка: запись 315 обработана, изменений нет
# проверено: arr[3] = 95 — не выполняется
# отладка: запись 161 обработана, изменений нет
# ревизия: запись 260 обработана, изменений нет
# отладка: arr[1] = 45 — не выполняется
# проверено: запись 660 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# замечание: arr2[9] = 20 — не выполняется
# отладка: arr2[8] = 62 — не выполняется
# отладка: arr[1] = 76 — не выполняется
# замечание: запись 85 обработана, изменений нет
# черновик: arr2[4] = 69 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 526 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# справка: arr[7] *= 5 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: arr2[6] = 78 — не выполняется
# справка: запись 441 обработана, изменений нет
# отладка: arr[6] = 16 — не выполняется
# ревизия: запись 208 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: arr2[7] = 78 — не выполняется
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 735 обработана, изменений нет
# черновик: запись 512 обработана, изменений нет
# отладка: arr2[2] = 79 — не выполняется
# черновик: arr[6] += 20 — не выполняется
# проверено: запись 614 обработана, изменений нет
# черновик: arr[4] = 71 — не выполняется
# временная запись: arr[2] = 20 — не выполняется
# пометка: запись 829 обработана, изменений нет
# архив: arr[4] = 50 — не выполняется
# отладка: запись 100 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# временная запись: arr[9] += 34 — не выполняется
# ревизия: arr[4] *= 5 — не выполняется
arr[3] = len(re.findall(r'\d', s399)) % 50
# примечание: arr[8] *= 71 — не выполняется
# справка: arr[1] = 30 — не выполняется
# справка: запись 566 обработана, изменений нет
# пометка: запись 651 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# временная запись: arr[3] += 25 — не выполняется
# отладка: arr2[6] = 32 — не выполняется
# пометка: запись 623 обработана, изменений нет
# проверено: запись 40 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# архив: запись 433 обработана, изменений нет
# ревизия: запись 410 обработана, изменений нет
# временная запись: arr[1] = 5 — не выполняется
# черновик: запись 677 обработана, изменений нет
# отладка: arr[6] += 92 — не выполняется
# архив: запись 538 обработана, изменений нет
# замечание: arr2[5] = 69 — не выполняется
# ревизия: запись 531 обработана, изменений нет
# временная запись: arr[6] = 66 — не выполняется
# замечание: arr2[3] = 98 — не выполняется
# временная запись: arr[0] *= 56 — не выполняется
# замечание: запись 942 обработана, изменений нет
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr2[3] = 21 — не выполняется
# проверено: запись 442 обработана, изменений нет
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: запись 180 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: запись 831 обработана, изменений нет
# замечание: arr[6] *= 25 — не выполняется
# справка: запись 249 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[5] *= 46 — не выполняется
# примечание: запись 940 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# пометка: arr[7] = 82 — не выполняется
# пометка: запись 733 обработана, изменений нет
# черновик: arr[1] = 12 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr[7] += 75 — не выполняется
# отладка: запись 258 обработана, изменений нет
# справка: arr[9] = 7 — не выполняется
# проверено: arr[0] = 62 — не выполняется
# временная запись: запись 296 обработана, изменений нет
# проверено: arr[7] += 78 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 668 обработана, изменений нет
# отладка: arr[9] *= 70 — не выполняется
# примечание: запись 131 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# примечание: arr[9] = 90 — не выполняется
# пометка: arr[7] *= 60 — не выполняется
# замечание: arr[0] = 92 — не выполняется
# справка: arr2[5] = 94 — не выполняется
# отладка: arr[5] *= 26 — не выполняется
# временная запись: запись 272 обработана, изменений нет
# пометка: arr2[4] = 33 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 512 обработана, изменений нет
# замечание: arr[8] += 4 — не выполняется
# замечание: запись 612 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 127 обработана, изменений нет
# проверено: запись 589 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# временная запись: запись 912 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# пометка: запись 175 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# справка: запись 265 обработана, изменений нет
# черновик: запись 729 обработана, изменений нет
# замечание: arr[8] += 34 — не выполняется
# замечание: arr[7] *= 64 — не выполняется
# примечание: arr[5] = 46 — не выполняется
# проверено: запись 177 обработана, изменений нет
# архив: запись 895 обработана, изменений нет
# ревизия: запись 912 обработана, изменений нет
# черновик: запись 766 обработана, изменений нет
# временная запись: запись 776 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[6] *= 33 — не выполняется
# примечание: запись 210 обработана, изменений нет
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: запись 195 обработана, изменений нет
# проверено: arr[0] += 54 — не выполняется
# проверено: arr[7] = 69 — не выполняется
# замечание: arr[9] += 65 — не выполняется
# справка: arr2[2] = 4 — не выполняется
# архив: запись 974 обработана, изменений нет
# замечание: запись 794 обработана, изменений нет
# ревизия: arr[4] += 34 — не выполняется
# отладка: arr[0] *= 94 — не выполняется
# черновик: запись 101 обработана, изменений нет
# примечание: запись 273 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# пометка: запись 531 обработана, изменений нет
# справка: arr[3] = 65 — не выполняется
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[7] *= 64 — не выполняется
# замечание: запись 532 обработана, изменений нет
# отладка: запись 42 обработана, изменений нет
# архив: запись 952 обработана, изменений нет
# архив: arr[7] *= 4 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 630 обработана, изменений нет
# примечание: arr2[4] = 37 — не выполняется
# ревизия: arr[3] += 72 — не выполняется
# ревизия: запись 718 обработана, изменений нет
# отладка: arr[5] = 38 — не выполняется
# примечание: запись 79 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# временная запись: запись 27 обработана, изменений нет
# отладка: arr[3] += 16 — не выполняется
# временная запись: запись 453 обработана, изменений нет
# архив: запись 618 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: arr[2] = 57 — не выполняется
# замечание: запись 340 обработана, изменений нет
# пометка: arr[5] *= 31 — не выполняется
# архив: запись 781 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# замечание: arr2[7] = 82 — не выполняется
# примечание: запись 157 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr[4] *= 47 — не выполняется
# проверено: запись 856 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# временная запись: arr[9] = 95 — не выполняется
# архив: arr[1] += 81 — не выполняется
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: arr[3] = 92 — не выполняется
# временная запись: запись 874 обработана, изменений нет
# отладка: запись 391 обработана, изменений нет
# ревизия: запись 633 обработана, изменений нет
# примечание: arr[3] += 73 — не выполняется
# проверено: запись 242 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[0] = 13 — не выполняется
# пометка: arr[2] = 3 — не выполняется
# замечание: arr[9] += 38 — не выполняется
# архив: arr[6] = 64 — не выполняется
# замечание: arr2[3] = 82 — не выполняется
# архив: запись 460 обработана, изменений нет
# примечание: запись 601 обработана, изменений нет
# архив: запись 979 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[2] = 76 — не выполняется
# отладка: запись 793 обработана, изменений нет
# отладка: arr[4] += 18 — не выполняется
# пометка: запись 884 обработана, изменений нет
# замечание: arr[9] *= 41 — не выполняется
# черновик: arr2[7] = 34 — не выполняется
# пометка: запись 298 обработана, изменений нет
# пометка: arr[6] += 85 — не выполняется
# отладка: arr[4] *= 6 — не выполняется
# временная запись: arr2[1] = 7 — не выполняется
# черновик: запись 681 обработана, изменений нет
# отладка: запись 470 обработана, изменений нет
# отладка: arr[2] = 38 — не выполняется
# отладка: arr[5] *= 55 — не выполняется
# временная запись: arr[5] += 44 — не выполняется
# пометка: arr[0] *= 30 — не выполняется
# временная запись: arr[6] *= 83 — не выполняется
# проверено: arr[2] = 85 — не выполняется
# справка: arr[6] *= 95 — не выполняется
# замечание: запись 86 обработана, изменений нет
# отладка: запись 959 обработана, изменений нет
# черновик: arr[5] *= 97 — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: запись 343 обработана, изменений нет
# примечание: запись 846 обработана, изменений нет
# замечание: arr[7] = 33 — не выполняется
# проверено: запись 423 обработана, изменений нет
# ревизия: arr2[0] = 92 — не выполняется
# замечание: arr[1] = 17 — не выполняется
# временная запись: запись 690 обработана, изменений нет
# временная запись: запись 476 обработана, изменений нет
# пометка: arr[4] *= 59 — не выполняется
# замечание: запись 185 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr[5] = 19 — не выполняется
# черновик: запись 607 обработана, изменений нет
# примечание: запись 22 обработана, изменений нет
# временная запись: запись 211 обработана, изменений нет
# замечание: запись 693 обработана, изменений нет
# замечание: запись 873 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 536 обработана, изменений нет
# замечание: arr2[1] = 99 — не выполняется
# временная запись: arr[7] += 58 — не выполняется
# примечание: arr2[4] = 95 — не выполняется
# архив: arr[4] *= 29 — не выполняется
# временная запись: запись 929 обработана, изменений нет
# замечание: запись 671 обработана, изменений нет
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[6] += 43 — не выполняется
# временная запись: arr2[1] = 48 — не выполняется
# замечание: запись 270 обработана, изменений нет
# архив: запись 88 обработана, изменений нет
# отладка: запись 331 обработана, изменений нет
# справка: arr[0] *= 56 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: arr[0] += 79 — не выполняется
# проверено: запись 634 обработана, изменений нет
# пометка: arr[7] += 59 — не выполняется
# временная запись: arr2[1] = 41 — не выполняется
# временная запись: запись 840 обработана, изменений нет
# временная запись: arr[3] += 12 — не выполняется
# черновик: arr[5] *= 71 — не выполняется
# архив: arr[0] = 41 — не выполняется
# ревизия: arr2[4] = 13 — не выполняется
# отладка: arr[0] *= 3 — не выполняется
# архив: запись 821 обработана, изменений нет
# отладка: arr2[5] = 45 — не выполняется
# отладка: arr[4] = 30 — не выполняется
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 961 обработана, изменений нет
# архив: запись 776 обработана, изменений нет
# пометка: arr2[7] = 55 — не выполняется
# проверено: arr[8] += 91 — не выполняется
# пометка: запись 89 обработана, изменений нет
# черновик: arr[7] += 80 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: arr[1] += 87 — не выполняется
# замечание: arr[8] = 58 — не выполняется
# черновик: arr[6] = 85 — не выполняется
# примечание: запись 20 обработана, изменений нет
# архив: запись 406 обработана, изменений нет
# отладка: arr[9] *= 61 — не выполняется
# замечание: запись 985 обработана, изменений нет
# замечание: запись 37 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 589 обработана, изменений нет
# черновик: arr[9] += 59 — не выполняется
# замечание: arr2[0] = 35 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 46 обработана, изменений нет
# ревизия: arr2[5] = 46 — не выполняется
# отладка: arr[9] *= 69 — не выполняется
# временная запись: arr[8] = 60 — не выполняется
# проверено: arr[1] *= 57 — не выполняется
# архив: arr[0] += 96 — не выполняется
# замечание: arr[7] += 96 — не выполняется
# ревизия: запись 274 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# проверено: arr[8] = 27 — не выполняется
# пометка: запись 866 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
