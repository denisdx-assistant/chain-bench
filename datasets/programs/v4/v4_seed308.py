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
arr[6] *= 28
arr[2] *= 36
arr[1] = 4
arr2[3] = 1
arr[6], arr[6] = arr[6], arr[6]
arr[7] *= 3
arr[6] *= 49
arr2[8] = 18
"""

TRAP_0 = "arr[3] = 317"
TRAP_1 = "arr[7] = 338"
TRAP_2 = "arr[5] = 613"
TRAP_3 = "arr[8] = 257"
TRAP_4 = "arr[0] = 592"
TRAP_5 = "arr[8] = 366"
TRAP_6 = "arr[5] = 844"
TRAP_7 = "arr[1] = 688"
TRAP_8 = "arr[0] = 673"
TRAP_9 = "arr[6] = 963"
TRAP_10 = "arr[9] = 363"
TRAP_11 = "arr[5] = 261"
TRAP_12 = "arr[9] = 997"
TRAP_13 = "arr[3] = 605"
TRAP_14 = "arr[8] = 411"
TRAP_15 = "arr[1] = 469"
TRAP_16 = "arr[5] = 593"
TRAP_17 = "arr[1] = 760"
TRAP_18 = "arr[5] = 792"
TRAP_19 = "arr[6] = 417"
TRAP_20 = "arr[1] = 731"
TRAP_21 = "arr[4] = 369"
TRAP_22 = "arr[8] = 689"
TRAP_23 = "arr[1] = 522"
TRAP_24 = "arr[6] = 819"
TRAP_25 = "arr[0] = 952"
TRAP_26 = "arr[6] = 280"
TRAP_27 = "arr[2] = 385"
TRAP_28 = "arr[9] = 766"
TRAP_29 = "arr[5] = 365"
TRAP_30 = "arr[3] = 716"
TRAP_31 = "arr[7] = 911"
TRAP_32 = "arr[5] = 626"
TRAP_33 = "arr[1] = 915"
TRAP_34 = "arr[7] = 229"
TRAP_35 = "arr[4] = 269"
TRAP_36 = "arr[0] = 420"
TRAP_37 = "arr[4] = 488"
TRAP_38 = "arr[0] = 487"
TRAP_39 = "arr[5] = 702"
TRAP_40 = "arr[5] = 645"
TRAP_41 = "arr[8] = 351"
TRAP_42 = "arr[0] = 621"
TRAP_43 = "arr[6] = 286"
TRAP_44 = "arr[7] = 743"
TRAP_45 = "arr[8] = 556"
TRAP_46 = "arr[6] = 978"
TRAP_47 = "arr[1] = 418"
TRAP_48 = "arr[2] = 228"
TRAP_49 = "arr[3] = 614"
TRAP_50 = "arr[3] = 719"
TRAP_51 = "arr[9] = 532"
TRAP_52 = "arr[0] = 125"
TRAP_53 = "arr[7] = 422"
TRAP_54 = "arr[1] = 790"
TRAP_55 = "arr[8] = 266"
TRAP_56 = "arr[1] = 284"
TRAP_57 = "arr[5] = 377"
TRAP_58 = "arr[5] = 782"
TRAP_59 = "arr[3] = 641"
TRAP_60 = "arr[1] = 378"
TRAP_61 = "arr[1] = 505"
TRAP_62 = "arr[8] = 647"
TRAP_63 = "arr[5] = 722"
TRAP_64 = "arr[2] = 185"
TRAP_65 = "arr[5] = 708"
TRAP_66 = "arr[1] = 722"
TRAP_67 = "arr[5] = 633"
TRAP_68 = "arr[9] = 963"
TRAP_69 = "arr[3] = 277"
TRAP_70 = "arr[1] = 433"
TRAP_71 = "arr[7] = 702"
TRAP_72 = "arr[0] = 529"
TRAP_73 = "arr[0] = 358"
TRAP_74 = "arr[4] = 489"
TRAP_75 = "arr[6] = 487"
TRAP_76 = "arr[2] = 402"
TRAP_77 = "arr[2] = 273"
TRAP_78 = "arr[1] = 585"
TRAP_79 = "arr[8] = 588"
TRAP_80 = "arr[3] = 294"
TRAP_81 = "arr[1] = 119"
TRAP_82 = "arr[4] = 278"
TRAP_83 = "arr[9] = 272"
TRAP_84 = "arr[9] = 779"
TRAP_85 = "arr[0] = 101"
TRAP_86 = "arr[4] = 687"
TRAP_87 = "arr[5] = 311"
TRAP_88 = "arr[6] = 923"
TRAP_89 = "arr[0] = 259"
TRAP_90 = "arr[5] = 934"
TRAP_91 = "arr[4] = 961"
TRAP_92 = "arr[5] = 843"
TRAP_93 = "arr[7] = 843"
TRAP_94 = "arr[9] = 788"
TRAP_95 = "arr[4] = 289"
TRAP_96 = "arr[4] = 699"
TRAP_97 = "arr[3] = 170"
TRAP_98 = "arr[1] = 882"
TRAP_99 = "arr[1] = 680"
TRAP_100 = "arr[4] = 311"
TRAP_101 = "arr[6] = 770"
TRAP_102 = "arr[6] = 755"
TRAP_103 = "arr[2] = 831"
TRAP_104 = "arr[7] = 447"
TRAP_105 = "arr[8] = 480"
TRAP_106 = "arr[7] = 446"
TRAP_107 = "arr[3] = 340"
TRAP_108 = "arr[2] = 759"
TRAP_109 = "arr[4] = 441"
TRAP_110 = "arr[8] = 701"
TRAP_111 = "arr[6] = 960"
TRAP_112 = "arr[1] = 886"
TRAP_113 = "arr[3] = 897"
TRAP_114 = "arr[9] = 568"
TRAP_115 = "arr[2] = 416"
TRAP_116 = "arr[5] = 577"
TRAP_117 = "arr[0] = 560"
TRAP_118 = "arr[5] = 699"
TRAP_119 = "arr[6] = 173"
TRAP_120 = "arr[7] = 934"
TRAP_121 = "arr[5] = 608"
TRAP_122 = "arr[5] = 430"
TRAP_123 = "arr[3] = 951"
TRAP_124 = "arr[6] = 441"
TRAP_125 = "arr[6] = 458"
TRAP_126 = "arr[5] = 585"
TRAP_127 = "arr[1] = 904"
TRAP_128 = "arr[0] = 171"
TRAP_129 = "arr[8] = 833"
TRAP_130 = "arr[5] = 465"
TRAP_131 = "arr[1] = 168"
TRAP_132 = "arr[9] = 542"
TRAP_133 = "arr[3] = 536"
TRAP_134 = "arr[0] = 384"
TRAP_135 = "arr[5] = 309"
TRAP_136 = "arr[2] = 705"
TRAP_137 = "arr[6] = 581"
TRAP_138 = "arr[2] = 833"
TRAP_139 = "arr[7] = 325"
TRAP_140 = "arr[1] = 900"
TRAP_141 = "arr[5] = 169"
TRAP_142 = "arr[7] = 387"
TRAP_143 = "arr[3] = 548"
TRAP_144 = "arr[0] = 998"
TRAP_145 = "arr[0] = 845"
TRAP_146 = "arr[5] = 638"
TRAP_147 = "arr[7] = 433"
TRAP_148 = "arr[8] = 865"
TRAP_149 = "arr[2] = 100"

arr = [6, 5, 13, 12, 12, 26, 17, 9, 6, 14]

tmp_0 = arr[2] + 16
tmp_1 = arr[2] + 26
copy_2 = arr[2]
code_3 = re.sub(r'[0-9]', '#', str(arr[5]))
note_4 = str(arr[3]) + str(arr[7])
tmp_5 = arr[2] + 5
note_6 = str(arr[4]) + str(arr[1])
tmp_7 = arr[9] + 15
label_8 = "запись 8 не применялась"
note_9 = str(arr[4]) + str(arr[8])
code_10 = re.sub(r'[0-9]', '#', str(arr[8]))
label_11 = "запись 11 не применялась"
label_12 = "запись 12 не применялась"
copy_13 = arr[3]
note_14 = str(arr[9]) + str(arr[9])
code_15 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_16 = arr[5]
code_17 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_18 = arr[6] + 39
label_19 = "запись 19 не применялась"
tmp_20 = arr[5] + 36
copy_21 = arr[9]
tmp_22 = arr[9] + 14
code_23 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_24 = arr[7]
tmp_25 = arr[6] + 27
copy_26 = arr[6]
tmp_27 = arr[0] + 49
code_28 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_29 = arr[9] + 14
code_30 = re.sub(r'[0-9]', '#', str(arr[3]))
label_31 = "запись 31 не применялась"
tmp_32 = arr[6] + 16
tmp_33 = arr[1] + 10
note_34 = str(arr[4]) + str(arr[3])
code_35 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_36 = arr[6]
tmp_37 = arr[9] + 42
note_38 = str(arr[6]) + str(arr[0])
tmp_39 = arr[9] + 15
tmp_40 = arr[2] + 10
note_41 = str(arr[0]) + str(arr[4])
tmp_42 = arr[3] + 50
tmp_43 = arr[7] + 47
note_44 = str(arr[0]) + str(arr[5])
copy_45 = arr[0]
copy_46 = arr[6]
code_47 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_48 = arr[9]
tmp_49 = arr[6] + 18
code_50 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_51 = arr[1] + 21
tmp_52 = arr[7] + 45
copy_53 = arr[7]
code_54 = re.sub(r'[0-9]', '#', str(arr[8]))
label_55 = "запись 55 не применялась"
note_56 = str(arr[1]) + str(arr[5])
tmp_57 = arr[6] + 36
copy_58 = arr[6]
label_59 = "запись 59 не применялась"
label_60 = "запись 60 не применялась"
tmp_61 = arr[6] + 2
copy_62 = arr[1]
note_63 = str(arr[7]) + str(arr[3])
note_64 = str(arr[2]) + str(arr[4])
tmp_65 = arr[4] + 6
copy_66 = arr[3]
tmp_67 = arr[6] + 30
tmp_68 = arr[2] + 22
label_69 = "запись 69 не применялась"
code_70 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_71 = arr[3] + 5
code_72 = re.sub(r'[0-9]', '#', str(arr[3]))
label_73 = "запись 73 не применялась"
label_74 = "запись 74 не применялась"
code_75 = re.sub(r'[0-9]', '#', str(arr[1]))
note_76 = str(arr[0]) + str(arr[9])
copy_77 = arr[2]
copy_78 = arr[0]
label_79 = "запись 79 не применялась"
copy_80 = arr[5]
code_81 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_82 = arr[8]
tmp_83 = arr[7] + 44
tmp_84 = arr[7] + 4
copy_85 = arr[2]
tmp_86 = arr[1] + 5
copy_87 = arr[3]
code_88 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_89 = arr[8]
label_90 = "запись 90 не применялась"
tmp_91 = arr[2] + 19
note_92 = str(arr[7]) + str(arr[7])
tmp_93 = arr[9] + 37
note_94 = str(arr[0]) + str(arr[7])
tmp_95 = arr[1] + 47
note_96 = str(arr[2]) + str(arr[3])
note_97 = str(arr[8]) + str(arr[9])
note_98 = str(arr[1]) + str(arr[7])
tmp_99 = arr[9] + 28
tmp_100 = arr[1] + 22
note_101 = str(arr[1]) + str(arr[4])
tmp_102 = arr[7] + 18
code_103 = re.sub(r'[0-9]', '#', str(arr[6]))
note_104 = str(arr[2]) + str(arr[0])
code_105 = re.sub(r'[0-9]', '#', str(arr[3]))
note_106 = str(arr[9]) + str(arr[4])
tmp_107 = arr[0] + 18
code_108 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_109 = arr[3]
tmp_110 = arr[7] + 20
copy_111 = arr[3]
note_112 = str(arr[1]) + str(arr[3])
tmp_113 = arr[8] + 17
code_114 = re.sub(r'[0-9]', '#', str(arr[4]))
label_115 = "запись 115 не применялась"
label_116 = "запись 116 не применялась"
copy_117 = arr[5]
tmp_118 = arr[5] + 23
note_119 = str(arr[6]) + str(arr[6])
tmp_120 = arr[0] + 6
note_121 = str(arr[9]) + str(arr[1])
tmp_122 = arr[8] + 35
tmp_123 = arr[4] + 23
copy_124 = arr[4]
note_125 = str(arr[7]) + str(arr[0])
copy_126 = arr[9]
code_127 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_128 = arr[5] + 22
tmp_129 = arr[3] + 4
note_130 = str(arr[5]) + str(arr[9])
tmp_131 = arr[8] + 19
tmp_132 = arr[5] + 48
note_133 = str(arr[6]) + str(arr[0])
note_134 = str(arr[3]) + str(arr[1])
note_135 = str(arr[7]) + str(arr[9])
tmp_136 = arr[2] + 15
note_137 = str(arr[9]) + str(arr[3])
note_138 = str(arr[3]) + str(arr[2])
tmp_139 = arr[8] + 16
note_140 = str(arr[3]) + str(arr[9])
tmp_141 = arr[7] + 7
note_142 = str(arr[4]) + str(arr[8])
tmp_143 = arr[6] + 38
tmp_144 = arr[8] + 16
label_145 = "запись 145 не применялась"
note_146 = str(arr[8]) + str(arr[6])
tmp_147 = arr[1] + 32
copy_148 = arr[9]
code_149 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_150 = arr[0]
tmp_151 = arr[6] + 21
code_152 = re.sub(r'[0-9]', '#', str(arr[1]))
note_153 = str(arr[7]) + str(arr[0])
label_154 = "запись 154 не применялась"
copy_155 = arr[9]
note_156 = str(arr[5]) + str(arr[2])
label_157 = "запись 157 не применялась"
copy_158 = arr[0]
copy_159 = arr[2]
tmp_160 = arr[2] + 6
label_161 = "запись 161 не применялась"
copy_162 = arr[7]
code_163 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_164 = arr[0]
tmp_165 = arr[8] + 45
copy_166 = arr[3]
note_167 = str(arr[9]) + str(arr[5])
tmp_168 = arr[5] + 49
code_169 = re.sub(r'[0-9]', '#', str(arr[8]))
code_170 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_171 = arr[4] + 33
tmp_172 = arr[2] + 11
label_173 = "запись 173 не применялась"
tmp_174 = arr[7] + 41
label_175 = "запись 175 не применялась"
label_176 = "запись 176 не применялась"
copy_177 = arr[7]
tmp_178 = arr[0] + 18
note_179 = str(arr[1]) + str(arr[2])
note_180 = str(arr[6]) + str(arr[1])
copy_181 = arr[8]
code_182 = re.sub(r'[0-9]', '#', str(arr[5]))
label_183 = "запись 183 не применялась"
note_184 = str(arr[9]) + str(arr[8])
code_185 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_186 = arr[4]
note_187 = str(arr[4]) + str(arr[9])
copy_188 = arr[8]
code_189 = re.sub(r'[0-9]', '#', str(arr[2]))
note_190 = str(arr[6]) + str(arr[7])
tmp_191 = arr[4] + 22
note_192 = str(arr[4]) + str(arr[8])
note_193 = str(arr[0]) + str(arr[7])
tmp_194 = arr[1] + 49
copy_195 = arr[9]
note_196 = str(arr[2]) + str(arr[0])
code_197 = re.sub(r'[0-9]', '#', str(arr[3]))
label_198 = "запись 198 не применялась"
note_199 = str(arr[8]) + str(arr[2])
note_200 = str(arr[6]) + str(arr[6])
tmp_201 = arr[8] + 33
copy_202 = arr[8]
note_203 = str(arr[3]) + str(arr[8])
label_204 = "запись 204 не применялась"
code_205 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_206 = arr[4] + 27
note_207 = str(arr[1]) + str(arr[4])
label_208 = "запись 208 не применялась"
label_209 = "запись 209 не применялась"
tmp_210 = arr[7] + 13
note_211 = str(arr[4]) + str(arr[5])
tmp_212 = arr[6] + 5
note_213 = str(arr[8]) + str(arr[5])
note_214 = str(arr[1]) + str(arr[5])
code_215 = re.sub(r'[0-9]', '#', str(arr[4]))
note_216 = str(arr[7]) + str(arr[8])
code_217 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_218 = arr[5]
code_219 = re.sub(r'[0-9]', '#', str(arr[7]))
code_220 = re.sub(r'[0-9]', '#', str(arr[4]))
note_221 = str(arr[0]) + str(arr[1])
copy_222 = arr[5]
tmp_223 = arr[7] + 5
copy_224 = arr[0]
tmp_225 = arr[5] + 3
label_226 = "запись 226 не применялась"
code_227 = re.sub(r'[0-9]', '#', str(arr[8]))
note_228 = str(arr[5]) + str(arr[3])
tmp_229 = arr[5] + 41
note_230 = str(arr[1]) + str(arr[2])
tmp_231 = arr[0] + 17
copy_232 = arr[1]
tmp_233 = arr[1] + 50
note_234 = str(arr[1]) + str(arr[4])
copy_235 = arr[7]
note_236 = str(arr[3]) + str(arr[6])
copy_237 = arr[1]
tmp_238 = arr[6] + 34
code_239 = re.sub(r'[0-9]', '#', str(arr[2]))
note_240 = str(arr[4]) + str(arr[1])
code_241 = re.sub(r'[0-9]', '#', str(arr[5]))
note_242 = str(arr[3]) + str(arr[5])
code_243 = re.sub(r'[0-9]', '#', str(arr[3]))
note_244 = str(arr[1]) + str(arr[7])
code_245 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_246 = arr[9] + 22
note_247 = str(arr[1]) + str(arr[0])
code_248 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_249 = arr[9] + 33
note_250 = str(arr[2]) + str(arr[3])
code_251 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_252 = arr[7] + 9
note_253 = str(arr[4]) + str(arr[4])
tmp_254 = arr[1] + 37
tmp_255 = arr[4] + 3
code_256 = re.sub(r'[0-9]', '#', str(arr[7]))
code_257 = re.sub(r'[0-9]', '#', str(arr[2]))
note_258 = str(arr[2]) + str(arr[3])
copy_259 = arr[6]
note_260 = str(arr[7]) + str(arr[3])
code_261 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_262 = arr[3] + 26
note_263 = str(arr[6]) + str(arr[2])
note_264 = str(arr[7]) + str(arr[3])
code_265 = re.sub(r'[0-9]', '#', str(arr[2]))
note_266 = str(arr[1]) + str(arr[6])
copy_267 = arr[8]
code_268 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_269 = arr[7] + 35
note_270 = str(arr[5]) + str(arr[5])
tmp_271 = arr[3] + 28
code_272 = re.sub(r'[0-9]', '#', str(arr[0]))
label_273 = "запись 273 не применялась"
note_274 = str(arr[7]) + str(arr[6])
note_275 = str(arr[7]) + str(arr[8])
copy_276 = arr[4]
note_277 = str(arr[6]) + str(arr[0])
code_278 = re.sub(r'[0-9]', '#', str(arr[7]))
label_279 = "запись 279 не применялась"
note_280 = str(arr[9]) + str(arr[5])
code_281 = re.sub(r'[0-9]', '#', str(arr[8]))
note_282 = str(arr[5]) + str(arr[5])
code_283 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_284 = arr[4] + 50
label_285 = "запись 285 не применялась"
tmp_286 = arr[4] + 28
note_287 = str(arr[3]) + str(arr[0])
tmp_288 = arr[9] + 21
code_289 = re.sub(r'[0-9]', '#', str(arr[6]))
code_290 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_291 = arr[3] + 18
tmp_292 = arr[7] + 37
copy_293 = arr[7]
code_294 = re.sub(r'[0-9]', '#', str(arr[6]))
label_295 = "запись 295 не применялась"
label_296 = "запись 296 не применялась"
tmp_297 = arr[6] + 44
note_298 = str(arr[9]) + str(arr[6])
note_299 = str(arr[1]) + str(arr[2])
code_300 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_301 = arr[0] + 15
tmp_302 = arr[3] + 40
label_303 = "запись 303 не применялась"
code_304 = re.sub(r'[0-9]', '#', str(arr[8]))
note_305 = str(arr[6]) + str(arr[0])
code_306 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_307 = arr[0] + 50
tmp_308 = arr[8] + 35
copy_309 = arr[7]
tmp_310 = arr[6] + 26
note_311 = str(arr[3]) + str(arr[1])
code_312 = re.sub(r'[0-9]', '#', str(arr[9]))
note_313 = str(arr[1]) + str(arr[5])
tmp_314 = arr[0] + 6
tmp_315 = arr[8] + 9
tmp_316 = arr[3] + 26
tmp_317 = arr[6] + 43
copy_318 = arr[5]
note_319 = str(arr[2]) + str(arr[3])
tmp_320 = arr[8] + 18
tmp_321 = arr[4] + 12
tmp_322 = arr[9] + 2
code_323 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_324 = arr[4] + 40
code_325 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_326 = arr[9]
copy_327 = arr[2]
note_328 = str(arr[4]) + str(arr[2])
tmp_329 = arr[2] + 19
note_330 = str(arr[5]) + str(arr[6])
tmp_331 = arr[8] + 15
code_332 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_333 = arr[5] + 42
tmp_334 = arr[1] + 20
note_335 = str(arr[2]) + str(arr[6])
note_336 = str(arr[7]) + str(arr[7])
tmp_337 = arr[4] + 14
code_338 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_339 = arr[9] + 5
code_340 = re.sub(r'[0-9]', '#', str(arr[4]))
note_341 = str(arr[3]) + str(arr[6])
tmp_342 = arr[8] + 49
code_343 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_344 = arr[1]
label_345 = "запись 345 не применялась"
label_346 = "запись 346 не применялась"
code_347 = re.sub(r'[0-9]', '#', str(arr[9]))
code_348 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_349 = arr[3] + 4
note_350 = str(arr[2]) + str(arr[6])
tmp_351 = arr[1] + 50
tmp_352 = arr[5] + 11
copy_353 = arr[4]
copy_354 = arr[2]
tmp_355 = arr[2] + 17
code_356 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_357 = arr[6]
code_358 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_359 = arr[2] + 6
tmp_360 = arr[4] + 9
copy_361 = arr[9]
note_362 = str(arr[4]) + str(arr[2])
tmp_363 = arr[3] + 10
code_364 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_365 = arr[3] + 5
code_366 = re.sub(r'[0-9]', '#', str(arr[3]))
label_367 = "запись 367 не применялась"
note_368 = str(arr[3]) + str(arr[4])
tmp_369 = arr[7] + 5
copy_370 = arr[4]
copy_371 = arr[9]
tmp_372 = arr[7] + 35
copy_373 = arr[2]
note_374 = str(arr[9]) + str(arr[6])
copy_375 = arr[3]
code_376 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_377 = arr[4] + 14
label_378 = "запись 378 не применялась"
note_379 = str(arr[9]) + str(arr[9])
label_380 = "запись 380 не применялась"
tmp_381 = arr[0] + 26
note_382 = str(arr[3]) + str(arr[1])
code_383 = re.sub(r'[0-9]', '#', str(arr[2]))
code_384 = re.sub(r'[0-9]', '#', str(arr[5]))
label_385 = "запись 385 не применялась"
copy_386 = arr[6]
tmp_387 = arr[1] + 27
note_388 = str(arr[8]) + str(arr[6])
copy_389 = arr[3]
label_390 = "запись 390 не применялась"
code_391 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_392 = arr[4]
code_393 = re.sub(r'[0-9]', '#', str(arr[6]))
note_394 = str(arr[9]) + str(arr[6])
note_395 = str(arr[9]) + str(arr[5])
copy_396 = arr[9]
tmp_397 = arr[2] + 9
note_398 = str(arr[5]) + str(arr[7])
code_399 = re.sub(r'[0-9]', '#', str(arr[4]))
note_400 = str(arr[5]) + str(arr[6])
code_401 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_402 = arr[7] + 3
copy_403 = arr[5]
note_404 = str(arr[6]) + str(arr[4])
note_405 = str(arr[0]) + str(arr[0])
note_406 = str(arr[7]) + str(arr[8])
label_407 = "запись 407 не применялась"
tmp_408 = arr[0] + 16
tmp_409 = arr[7] + 35
code_410 = re.sub(r'[0-9]', '#', str(arr[4]))
code_411 = re.sub(r'[0-9]', '#', str(arr[9]))
note_412 = str(arr[4]) + str(arr[7])
code_413 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_414 = arr[3]
code_415 = re.sub(r'[0-9]', '#', str(arr[9]))
label_416 = "запись 416 не применялась"
tmp_417 = arr[1] + 49
code_418 = re.sub(r'[0-9]', '#', str(arr[2]))
note_419 = str(arr[0]) + str(arr[4])
tmp_420 = arr[7] + 34
note_421 = str(arr[0]) + str(arr[7])
tmp_422 = arr[0] + 48
copy_423 = arr[8]
label_424 = "запись 424 не применялась"
tmp_425 = arr[5] + 26
code_426 = re.sub(r'[0-9]', '#', str(arr[6]))
label_427 = "запись 427 не применялась"
code_428 = re.sub(r'[0-9]', '#', str(arr[7]))
note_429 = str(arr[2]) + str(arr[0])
tmp_430 = arr[6] + 2
label_431 = "запись 431 не применялась"
copy_432 = arr[1]
copy_433 = arr[4]
label_434 = "запись 434 не применялась"
tmp_435 = arr[9] + 43
tmp_436 = arr[0] + 14
copy_437 = arr[1]
tmp_438 = arr[7] + 47
code_439 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_440 = arr[0]
code_441 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_442 = arr[9] + 4
code_443 = re.sub(r'[0-9]', '#', str(arr[2]))
note_444 = str(arr[9]) + str(arr[3])
code_445 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_446 = arr[5]
code_447 = re.sub(r'[0-9]', '#', str(arr[3]))
note_448 = str(arr[8]) + str(arr[7])
note_449 = str(arr[5]) + str(arr[3])
code_450 = re.sub(r'[0-9]', '#', str(arr[4]))
note_451 = str(arr[2]) + str(arr[3])
copy_452 = arr[2]
copy_453 = arr[5]
copy_454 = arr[7]
copy_455 = arr[3]
tmp_456 = arr[4] + 37
tmp_457 = arr[1] + 5
note_458 = str(arr[2]) + str(arr[4])
tmp_459 = arr[0] + 5
code_460 = re.sub(r'[0-9]', '#', str(arr[7]))
code_461 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_462 = arr[4] + 37
tmp_463 = arr[4] + 20
tmp_464 = arr[8] + 17
note_465 = str(arr[5]) + str(arr[7])
code_466 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_467 = arr[7] + 47
note_468 = str(arr[1]) + str(arr[3])
copy_469 = arr[3]
tmp_470 = arr[0] + 28
tmp_471 = arr[8] + 6
note_472 = str(arr[9]) + str(arr[2])
note_473 = str(arr[3]) + str(arr[3])
note_474 = str(arr[8]) + str(arr[1])
tmp_475 = arr[8] + 14
note_476 = str(arr[3]) + str(arr[4])
note_477 = str(arr[5]) + str(arr[3])
label_478 = "запись 478 не применялась"
copy_479 = arr[6]
tmp_480 = arr[9] + 36
note_481 = str(arr[5]) + str(arr[9])
note_482 = str(arr[0]) + str(arr[9])
tmp_483 = arr[3] + 12
copy_484 = arr[7]
label_485 = "запись 485 не применялась"
note_486 = str(arr[8]) + str(arr[3])
code_487 = re.sub(r'[0-9]', '#', str(arr[0]))
label_488 = "запись 488 не применялась"
note_489 = str(arr[7]) + str(arr[9])
note_490 = str(arr[8]) + str(arr[4])
code_491 = re.sub(r'[0-9]', '#', str(arr[7]))
code_492 = re.sub(r'[0-9]', '#', str(arr[4]))
code_493 = re.sub(r'[0-9]', '#', str(arr[3]))
code_494 = re.sub(r'[0-9]', '#', str(arr[4]))
note_495 = str(arr[6]) + str(arr[9])
code_496 = re.sub(r'[0-9]', '#', str(arr[4]))
note_497 = str(arr[2]) + str(arr[0])
copy_498 = arr[3]
code_499 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_500 = arr[2]
code_501 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_502 = arr[3] + 33
tmp_503 = arr[8] + 48
note_504 = str(arr[4]) + str(arr[6])
copy_505 = arr[9]
code_506 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_507 = arr[8] + 20
tmp_508 = arr[8] + 21
note_509 = str(arr[0]) + str(arr[1])
copy_510 = arr[7]
tmp_511 = arr[0] + 48
note_512 = str(arr[2]) + str(arr[4])
code_513 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_514 = arr[4]
tmp_515 = arr[1] + 14
copy_516 = arr[8]
label_517 = "запись 517 не применялась"
note_518 = str(arr[6]) + str(arr[1])
label_519 = "запись 519 не применялась"
code_520 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_521 = arr[9] + 41
label_522 = "запись 522 не применялась"
label_523 = "запись 523 не применялась"
code_524 = re.sub(r'[0-9]', '#', str(arr[5]))
note_525 = str(arr[6]) + str(arr[0])
code_526 = re.sub(r'[0-9]', '#', str(arr[5]))
note_527 = str(arr[6]) + str(arr[6])
copy_528 = arr[1]
note_529 = str(arr[2]) + str(arr[6])
copy_530 = arr[4]
note_531 = str(arr[9]) + str(arr[4])
tmp_532 = arr[6] + 46
code_533 = re.sub(r'[0-9]', '#', str(arr[0]))
note_534 = str(arr[8]) + str(arr[5])
code_535 = re.sub(r'[0-9]', '#', str(arr[5]))
note_536 = str(arr[2]) + str(arr[5])
note_537 = str(arr[0]) + str(arr[6])
code_538 = re.sub(r'[0-9]', '#', str(arr[7]))
code_539 = re.sub(r'[0-9]', '#', str(arr[6]))
code_540 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_541 = arr[4] + 44
note_542 = str(arr[7]) + str(arr[0])
tmp_543 = arr[1] + 17
code_544 = re.sub(r'[0-9]', '#', str(arr[7]))
label_545 = "запись 545 не применялась"
code_546 = re.sub(r'[0-9]', '#', str(arr[2]))
label_547 = "запись 547 не применялась"
code_548 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_549 = arr[3]
label_550 = "запись 550 не применялась"
tmp_551 = arr[2] + 38
tmp_552 = arr[7] + 28
code_553 = re.sub(r'[0-9]', '#', str(arr[2]))
note_554 = str(arr[3]) + str(arr[7])
tmp_555 = arr[0] + 17
code_556 = re.sub(r'[0-9]', '#', str(arr[8]))
code_557 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_558 = arr[5]
note_559 = str(arr[2]) + str(arr[6])
tmp_560 = arr[1] + 21
tmp_561 = arr[1] + 1
code_562 = re.sub(r'[0-9]', '#', str(arr[3]))
note_563 = str(arr[6]) + str(arr[5])
label_564 = "запись 564 не применялась"
note_565 = str(arr[9]) + str(arr[7])
note_566 = str(arr[9]) + str(arr[4])
tmp_567 = arr[1] + 30
copy_568 = arr[8]
tmp_569 = arr[4] + 2
note_570 = str(arr[8]) + str(arr[3])
note_571 = str(arr[7]) + str(arr[0])
tmp_572 = arr[1] + 9
tmp_573 = arr[6] + 17
tmp_574 = arr[4] + 38
note_575 = str(arr[5]) + str(arr[6])
copy_576 = arr[2]
note_577 = str(arr[5]) + str(arr[2])
copy_578 = arr[8]
note_579 = str(arr[9]) + str(arr[7])
copy_580 = arr[1]
code_581 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_582 = arr[1] + 5
tmp_583 = arr[1] + 3
tmp_584 = arr[6] + 33
label_585 = "запись 585 не применялась"
copy_586 = arr[1]
note_587 = str(arr[7]) + str(arr[3])
note_588 = str(arr[4]) + str(arr[7])
copy_589 = arr[4]
copy_590 = arr[7]
tmp_591 = arr[6] + 24
tmp_592 = arr[3] + 26
tmp_593 = arr[7] + 8
note_594 = str(arr[0]) + str(arr[2])
code_595 = re.sub(r'[0-9]', '#', str(arr[8]))
label_596 = "запись 596 не применялась"
label_597 = "запись 597 не применялась"
note_598 = str(arr[3]) + str(arr[1])
note_599 = str(arr[7]) + str(arr[9])
tmp_600 = arr[8] + 41
code_601 = re.sub(r'[0-9]', '#', str(arr[5]))
note_602 = str(arr[6]) + str(arr[4])
note_603 = str(arr[6]) + str(arr[5])
note_604 = str(arr[1]) + str(arr[9])
label_605 = "запись 605 не применялась"
code_606 = re.sub(r'[0-9]', '#', str(arr[3]))
note_607 = str(arr[4]) + str(arr[1])
note_608 = str(arr[9]) + str(arr[4])
note_609 = str(arr[7]) + str(arr[4])
code_610 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_611 = arr[1] + 27
label_612 = "запись 612 не применялась"
tmp_613 = arr[6] + 27
copy_614 = arr[9]
tmp_615 = arr[2] + 23
note_616 = str(arr[4]) + str(arr[5])
code_617 = re.sub(r'[0-9]', '#', str(arr[1]))
note_618 = str(arr[5]) + str(arr[7])
tmp_619 = arr[2] + 13
copy_620 = arr[8]
note_621 = str(arr[9]) + str(arr[7])
tmp_622 = arr[8] + 19
note_623 = str(arr[7]) + str(arr[2])
tmp_624 = arr[9] + 15
tmp_625 = arr[2] + 43
tmp_626 = arr[0] + 8
copy_627 = arr[9]
tmp_628 = arr[6] + 36
note_629 = str(arr[1]) + str(arr[9])
copy_630 = arr[1]
tmp_631 = arr[8] + 28
label_632 = "запись 632 не применялась"
note_633 = str(arr[7]) + str(arr[5])
copy_634 = arr[1]
note_635 = str(arr[4]) + str(arr[0])
copy_636 = arr[9]
tmp_637 = arr[8] + 6
code_638 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_639 = arr[7] + 9
copy_640 = arr[4]
code_641 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_642 = arr[2] + 1
label_643 = "запись 643 не применялась"
copy_644 = arr[4]
note_645 = str(arr[9]) + str(arr[9])
note_646 = str(arr[6]) + str(arr[2])
code_647 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_648 = arr[4] + 25
copy_649 = arr[3]
note_650 = str(arr[6]) + str(arr[5])
label_651 = "запись 651 не применялась"
tmp_652 = arr[9] + 13
copy_653 = arr[5]
note_654 = str(arr[7]) + str(arr[2])
note_655 = str(arr[2]) + str(arr[5])
note_656 = str(arr[2]) + str(arr[7])
tmp_657 = arr[9] + 48
copy_658 = arr[3]
tmp_659 = arr[3] + 12
tmp_660 = arr[2] + 28
tmp_661 = arr[5] + 46
tmp_662 = arr[2] + 21
tmp_663 = arr[2] + 2
note_664 = str(arr[2]) + str(arr[4])
tmp_665 = arr[1] + 17
label_666 = "запись 666 не применялась"
note_667 = str(arr[9]) + str(arr[9])
copy_668 = arr[5]
note_669 = str(arr[6]) + str(arr[9])
code_670 = re.sub(r'[0-9]', '#', str(arr[5]))
note_671 = str(arr[1]) + str(arr[8])
note_672 = str(arr[0]) + str(arr[4])
note_673 = str(arr[2]) + str(arr[5])
tmp_674 = arr[3] + 6
note_675 = str(arr[6]) + str(arr[9])
note_676 = str(arr[6]) + str(arr[1])
copy_677 = arr[9]
label_678 = "запись 678 не применялась"
tmp_679 = arr[9] + 9
note_680 = str(arr[6]) + str(arr[0])
code_681 = re.sub(r'[0-9]', '#', str(arr[5]))
note_682 = str(arr[7]) + str(arr[2])
label_683 = "запись 683 не применялась"
copy_684 = arr[8]
copy_685 = arr[1]
tmp_686 = arr[2] + 7
label_687 = "запись 687 не применялась"
label_688 = "запись 688 не применялась"
tmp_689 = arr[3] + 9
note_690 = str(arr[6]) + str(arr[5])
label_691 = "запись 691 не применялась"
tmp_692 = arr[0] + 9
code_693 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_694 = arr[2]
note_695 = str(arr[2]) + str(arr[9])
copy_696 = arr[1]
label_697 = "запись 697 не применялась"
tmp_698 = arr[3] + 11
note_699 = str(arr[4]) + str(arr[6])
copy_700 = arr[5]
label_701 = "запись 701 не применялась"
code_702 = re.sub(r'[0-9]', '#', str(arr[9]))
note_703 = str(arr[9]) + str(arr[6])
copy_704 = arr[4]
note_705 = str(arr[8]) + str(arr[7])
note_706 = str(arr[4]) + str(arr[6])
tmp_707 = arr[0] + 22
note_708 = str(arr[8]) + str(arr[5])
note_709 = str(arr[4]) + str(arr[2])
code_710 = re.sub(r'[0-9]', '#', str(arr[8]))
code_711 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_712 = arr[4] + 7
code_713 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_714 = arr[6] + 1
tmp_715 = arr[4] + 18
note_716 = str(arr[4]) + str(arr[6])
note_717 = str(arr[1]) + str(arr[8])
code_718 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_719 = arr[9] + 3
label_720 = "запись 720 не применялась"
tmp_721 = arr[8] + 49
note_722 = str(arr[5]) + str(arr[3])
tmp_723 = arr[8] + 25
note_724 = str(arr[8]) + str(arr[1])
note_725 = str(arr[0]) + str(arr[2])
code_726 = re.sub(r'[0-9]', '#', str(arr[2]))
label_727 = "запись 727 не применялась"
tmp_728 = arr[3] + 7
tmp_729 = arr[9] + 11
tmp_730 = arr[9] + 8
tmp_731 = arr[8] + 13
note_732 = str(arr[2]) + str(arr[4])
tmp_733 = arr[2] + 22
code_734 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_735 = arr[8] + 26
code_736 = re.sub(r'[0-9]', '#', str(arr[7]))
code_737 = re.sub(r'[0-9]', '#', str(arr[6]))
note_738 = str(arr[6]) + str(arr[4])
note_739 = str(arr[5]) + str(arr[2])
copy_740 = arr[6]
label_741 = "запись 741 не применялась"
label_742 = "запись 742 не применялась"
tmp_743 = arr[2] + 46
code_744 = re.sub(r'[0-9]', '#', str(arr[6]))
code_745 = re.sub(r'[0-9]', '#', str(arr[8]))
note_746 = str(arr[7]) + str(arr[8])
tmp_747 = arr[5] + 47
copy_748 = arr[0]
code_749 = re.sub(r'[0-9]', '#', str(arr[1]))
label_750 = "запись 750 не применялась"
code_751 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_752 = arr[9] + 5
tmp_753 = arr[2] + 46
note_754 = str(arr[4]) + str(arr[2])
label_755 = "запись 755 не применялась"
tmp_756 = arr[6] + 29
code_757 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_758 = arr[8]
code_759 = re.sub(r'[0-9]', '#', str(arr[6]))
note_760 = str(arr[9]) + str(arr[8])
note_761 = str(arr[5]) + str(arr[7])
tmp_762 = arr[0] + 43
tmp_763 = arr[3] + 5
note_764 = str(arr[7]) + str(arr[5])
tmp_765 = arr[8] + 2
label_766 = "запись 766 не применялась"
copy_767 = arr[9]
tmp_768 = arr[3] + 47
code_769 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_770 = arr[0]
copy_771 = arr[4]
tmp_772 = arr[2] + 34
copy_773 = arr[5]
copy_774 = arr[3]
note_775 = str(arr[9]) + str(arr[6])
code_776 = re.sub(r'[0-9]', '#', str(arr[2]))
code_777 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_778 = arr[4] + 13
copy_779 = arr[3]
copy_780 = arr[4]
tmp_781 = arr[2] + 23
copy_782 = arr[1]
note_783 = str(arr[5]) + str(arr[7])
code_784 = re.sub(r'[0-9]', '#', str(arr[9]))
note_785 = str(arr[2]) + str(arr[6])
code_786 = re.sub(r'[0-9]', '#', str(arr[3]))
note_787 = str(arr[7]) + str(arr[1])
note_788 = str(arr[8]) + str(arr[9])
note_789 = str(arr[1]) + str(arr[4])
tmp_790 = arr[0] + 46
copy_791 = arr[0]
code_792 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_793 = arr[4] + 44
copy_794 = arr[5]
note_795 = str(arr[3]) + str(arr[7])
tmp_796 = arr[3] + 10
tmp_797 = arr[4] + 21
tmp_798 = arr[8] + 40
tmp_799 = arr[2] + 46

arr.reverse()
# примечание: запись 905 обработана, изменений нет
# примечание: arr2[9] = 17 — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[7] *= 99 — не выполняется
# справка: arr2[8] = 56 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 75 обработана, изменений нет
# ревизия: arr[7] += 22 — не выполняется
# проверено: arr2[1] = 43 — не выполняется
# примечание: arr[3] += 66 — не выполняется
# примечание: arr[5] *= 40 — не выполняется
# проверено: arr[7] = 20 — не выполняется
# примечание: arr[4] += 61 — не выполняется
# отладка: запись 777 обработана, изменений нет
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 452 обработана, изменений нет
# справка: arr2[7] = 48 — не выполняется
# справка: запись 118 обработана, изменений нет
# архив: arr[6] = 94 — не выполняется
# проверено: arr[5] = 36 — не выполняется
# проверено: запись 906 обработана, изменений нет
# архив: arr[2] += 38 — не выполняется
# ревизия: запись 468 обработана, изменений нет
# ревизия: запись 312 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: запись 493 обработана, изменений нет
# черновик: arr[2] *= 97 — не выполняется
# архив: запись 70 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 526 обработана, изменений нет
# ревизия: arr[5] = 5 — не выполняется
# замечание: arr2[0] = 22 — не выполняется
# временная запись: запись 849 обработана, изменений нет
# проверено: arr[2] = 3 — не выполняется
# архив: arr[5] += 59 — не выполняется
# временная запись: arr2[6] = 16 — не выполняется
# справка: запись 141 обработана, изменений нет
# замечание: arr[7] = 22 — не выполняется
# справка: arr[9] += 57 — не выполняется
# отладка: запись 143 обработана, изменений нет
# справка: arr[1] = 24 — не выполняется
# примечание: arr2[9] = 92 — не выполняется
# ревизия: запись 106 обработана, изменений нет
# примечание: arr[3] *= 70 — не выполняется
# проверено: arr[1] *= 91 — не выполняется
# примечание: arr[7] *= 13 — не выполняется
# проверено: запись 323 обработана, изменений нет
# замечание: запись 707 обработана, изменений нет
# отладка: arr[4] = 20 — не выполняется
# пометка: запись 26 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# черновик: arr2[1] = 61 — не выполняется
# замечание: запись 336 обработана, изменений нет
# архив: запись 762 обработана, изменений нет
# пометка: arr[5] += 37 — не выполняется
# архив: arr[3] = 36 — не выполняется
# архив: запись 537 обработана, изменений нет
# архив: arr[2] = 50 — не выполняется
# черновик: arr[6] *= 36 — не выполняется
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: arr[7] = 37 — не выполняется
# отладка: arr[0] *= 70 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[8] = 99 — не выполняется
# примечание: arr2[8] = 23 — не выполняется
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[4] = 8 — не выполняется
# примечание: arr[8] *= 39 — не выполняется
# временная запись: запись 33 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: arr[9] = 89 — не выполняется
# черновик: arr[9] += 10 — не выполняется
# справка: запись 41 обработана, изменений нет
# отладка: запись 26 обработана, изменений нет
# замечание: запись 627 обработана, изменений нет
# ревизия: запись 933 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# примечание: запись 519 обработана, изменений нет
# черновик: arr[7] = 45 — не выполняется
# архив: запись 22 обработана, изменений нет
# справка: запись 56 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# отладка: arr[6] = 46 — не выполняется
# проверено: запись 472 обработана, изменений нет
# отладка: arr[4] *= 5 — не выполняется
# проверено: arr[5] += 84 — не выполняется
# черновик: запись 53 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# проверено: запись 118 обработана, изменений нет
# проверено: запись 146 обработана, изменений нет
# справка: запись 4 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# проверено: arr[3] += 50 — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr2[0] = 33 — не выполняется
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: arr[9] = 91 — не выполняется
# отладка: arr[4] = 68 — не выполняется
# проверено: запись 73 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 908 обработана, изменений нет
# ревизия: arr[4] *= 14 — не выполняется
# примечание: запись 270 обработана, изменений нет
# ревизия: arr[3] += 45 — не выполняется
# примечание: arr[9] = 43 — не выполняется
# проверено: запись 107 обработана, изменений нет
# пометка: arr2[4] = 41 — не выполняется
# архив: запись 931 обработана, изменений нет
# проверено: запись 749 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# временная запись: arr[8] *= 46 — не выполняется
# архив: arr2[3] = 83 — не выполняется
# временная запись: запись 447 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[0] *= 69 — не выполняется
# примечание: arr[8] = 53 — не выполняется
# архив: arr[1] *= 9 — не выполняется
# проверено: arr2[6] = 84 — не выполняется
# примечание: arr[7] = 62 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[2] += 66 — не выполняется
# примечание: запись 881 обработана, изменений нет
# отладка: запись 229 обработана, изменений нет
# ревизия: arr[6] *= 63 — не выполняется
# отладка: arr[3] = 11 — не выполняется
# замечание: запись 72 обработана, изменений нет
# справка: arr[7] += 43 — не выполняется
# ревизия: запись 384 обработана, изменений нет
# пометка: запись 220 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# временная запись: arr[2] = 1 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[0] += 33 — не выполняется
# проверено: запись 380 обработана, изменений нет
# архив: запись 542 обработана, изменений нет
# пометка: запись 335 обработана, изменений нет
# черновик: arr[8] += 65 — не выполняется
# черновик: arr2[4] = 67 — не выполняется
# черновик: arr[0] = 81 — не выполняется
# примечание: запись 147 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: запись 347 обработана, изменений нет
# пометка: запись 110 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# примечание: arr[7] *= 48 — не выполняется
# отладка: запись 892 обработана, изменений нет
# справка: arr[4] = 11 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 31 обработана, изменений нет
# отладка: arr[9] = 70 — не выполняется
# проверено: arr2[3] = 92 — не выполняется
# архив: запись 297 обработана, изменений нет
# пометка: arr[9] = 63 — не выполняется
# справка: запись 679 обработана, изменений нет
# отладка: запись 645 обработана, изменений нет
# архив: запись 72 обработана, изменений нет
# отладка: запись 553 обработана, изменений нет
# временная запись: запись 836 обработана, изменений нет
# замечание: arr[6] = 9 — не выполняется
# черновик: запись 730 обработана, изменений нет
# замечание: arr[2] *= 52 — не выполняется
# временная запись: запись 172 обработана, изменений нет
# проверено: arr[4] += 4 — не выполняется
# пометка: запись 75 обработана, изменений нет
# справка: arr[3] *= 77 — не выполняется
# пометка: arr[4] *= 62 — не выполняется
# пометка: arr[2] *= 19 — не выполняется
# примечание: запись 28 обработана, изменений нет
# архив: запись 809 обработана, изменений нет
# замечание: запись 747 обработана, изменений нет
# архив: arr[5] = 98 — не выполняется
# черновик: arr[3] *= 13 — не выполняется
# проверено: arr[1] *= 18 — не выполняется
# пометка: запись 183 обработана, изменений нет
# черновик: arr[5] += 30 — не выполняется
# отладка: запись 489 обработана, изменений нет
# справка: запись 398 обработана, изменений нет
# временная запись: arr2[0] = 57 — не выполняется
# ревизия: запись 588 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# архив: запись 221 обработана, изменений нет
# замечание: arr[8] *= 69 — не выполняется
# отладка: запись 364 обработана, изменений нет
# ревизия: arr[3] = 66 — не выполняется
# примечание: запись 197 обработана, изменений нет
# архив: arr[8] *= 36 — не выполняется
# примечание: arr[7] *= 22 — не выполняется
# черновик: запись 358 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 501 обработана, изменений нет
# справка: запись 539 обработана, изменений нет
# черновик: arr2[9] = 13 — не выполняется
# архив: запись 320 обработана, изменений нет
# справка: запись 774 обработана, изменений нет
# черновик: запись 633 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 520 обработана, изменений нет
# ревизия: arr2[5] = 66 — не выполняется
# временная запись: arr[1] *= 44 — не выполняется
# отладка: запись 178 обработана, изменений нет
# архив: arr2[7] = 56 — не выполняется
# черновик: запись 405 обработана, изменений нет
# временная запись: запись 129 обработана, изменений нет
# примечание: arr[5] += 80 — не выполняется
# справка: arr[0] = 4 — не выполняется
# временная запись: запись 393 обработана, изменений нет
# проверено: запись 393 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# отладка: запись 142 обработана, изменений нет
# проверено: запись 85 обработана, изменений нет
# примечание: запись 84 обработана, изменений нет
# ревизия: arr[0] *= 31 — не выполняется
# черновик: arr[3] = 27 — не выполняется
# примечание: запись 153 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# отладка: запись 460 обработана, изменений нет
# временная запись: arr[8] = 45 — не выполняется
# отладка: запись 213 обработана, изменений нет
# черновик: arr[3] *= 19 — не выполняется
# замечание: запись 749 обработана, изменений нет
# отладка: запись 243 обработана, изменений нет
# черновик: запись 652 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# проверено: запись 485 обработана, изменений нет
# справка: запись 661 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[8] += 16 — не выполняется
# проверено: запись 15 обработана, изменений нет
# временная запись: arr[6] = 51 — не выполняется
# временная запись: запись 524 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr2[2] = 11 — не выполняется
# справка: arr2[7] = 93 — не выполняется
# черновик: arr2[9] = 35 — не выполняется
# проверено: arr[9] *= 34 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# отладка: arr2[2] = 2 — не выполняется
# примечание: запись 932 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr[5] = 38 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: запись 690 обработана, изменений нет
# ревизия: arr[6] = 26 — не выполняется
# проверено: arr[6] *= 96 — не выполняется
# временная запись: запись 484 обработана, изменений нет
# ревизия: запись 600 обработана, изменений нет
# отладка: запись 105 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# архив: запись 802 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# проверено: arr[1] = 7 — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[6] *= 78 — не выполняется
# ревизия: запись 158 обработана, изменений нет
# замечание: arr[4] *= 9 — не выполняется
# замечание: arr2[5] = 11 — не выполняется
# замечание: arr[1] *= 24 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: запись 256 обработана, изменений нет
# примечание: запись 511 обработана, изменений нет
# замечание: arr[4] += 72 — не выполняется
# пометка: arr2[0] = 38 — не выполняется
# черновик: arr2[6] = 54 — не выполняется
# замечание: arr2[9] = 60 — не выполняется
# проверено: запись 930 обработана, изменений нет
# замечание: arr2[4] = 75 — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 261 обработана, изменений нет
# пометка: запись 259 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# примечание: arr[4] = 31 — не выполняется
# черновик: запись 376 обработана, изменений нет
# примечание: запись 374 обработана, изменений нет
# проверено: arr[7] += 59 — не выполняется
# примечание: запись 543 обработана, изменений нет
# черновик: arr[8] += 79 — не выполняется
# пометка: запись 604 обработана, изменений нет
# ревизия: запись 742 обработана, изменений нет
# примечание: arr[6] += 52 — не выполняется
# временная запись: запись 640 обработана, изменений нет
# примечание: arr[6] = 76 — не выполняется
# архив: запись 704 обработана, изменений нет
# пометка: запись 60 обработана, изменений нет
# примечание: запись 402 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# отладка: запись 531 обработана, изменений нет
# проверено: arr[7] *= 48 — не выполняется
# пометка: arr[7] += 70 — не выполняется
# временная запись: arr[4] += 18 — не выполняется
# черновик: arr[5] = 24 — не выполняется
# пометка: запись 365 обработана, изменений нет
# черновик: arr[6] = 50 — не выполняется
# проверено: arr[4] *= 82 — не выполняется
# справка: arr[7] *= 3 — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: запись 984 обработана, изменений нет
# проверено: запись 589 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
arr[6] += 4
# черновик: запись 484 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 392 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# справка: запись 572 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr2[5] = 85 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# временная запись: arr[2] += 19 — не выполняется
# архив: arr[2] *= 91 — не выполняется
# отладка: запись 526 обработана, изменений нет
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 715 обработана, изменений нет
# архив: arr[5] += 39 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[4] += 6 — не выполняется
# пометка: запись 210 обработана, изменений нет
# отладка: arr[0] = 72 — не выполняется
# временная запись: arr[7] += 17 — не выполняется
# временная запись: запись 236 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# пометка: запись 271 обработана, изменений нет
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: запись 487 обработана, изменений нет
# проверено: arr[1] *= 85 — не выполняется
# замечание: arr[5] += 41 — не выполняется
# черновик: запись 341 обработана, изменений нет
# временная запись: запись 506 обработана, изменений нет
# черновик: запись 230 обработана, изменений нет
# примечание: запись 87 обработана, изменений нет
# отладка: запись 409 обработана, изменений нет
# ревизия: arr2[2] = 9 — не выполняется
# черновик: запись 555 обработана, изменений нет
# отладка: запись 739 обработана, изменений нет
# временная запись: запись 683 обработана, изменений нет
# черновик: arr[5] *= 54 — не выполняется
# отладка: запись 468 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[5] *= 88 — не выполняется
# справка: arr2[7] = 79 — не выполняется
# примечание: запись 303 обработана, изменений нет
# временная запись: arr[1] = 67 — не выполняется
# черновик: запись 892 обработана, изменений нет
# черновик: arr[3] *= 62 — не выполняется
# временная запись: запись 926 обработана, изменений нет
# пометка: arr2[6] = 74 — не выполняется
# черновик: arr[0] += 88 — не выполняется
# архив: запись 831 обработана, изменений нет
# временная запись: arr[9] = 77 — не выполняется
# проверено: запись 516 обработана, изменений нет
# временная запись: запись 702 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr2[0] = 13 — не выполняется
# архив: запись 384 обработана, изменений нет
# черновик: arr[7] += 84 — не выполняется
# замечание: запись 288 обработана, изменений нет
# примечание: запись 168 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# замечание: запись 776 обработана, изменений нет
# архив: arr[5] += 23 — не выполняется
# примечание: запись 385 обработана, изменений нет
# отладка: arr2[9] = 4 — не выполняется
# проверено: arr2[1] = 56 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 545 обработана, изменений нет
# примечание: запись 599 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# примечание: arr[1] *= 26 — не выполняется
# справка: запись 294 обработана, изменений нет
# временная запись: arr2[8] = 3 — не выполняется
# временная запись: arr2[6] = 14 — не выполняется
# черновик: arr2[0] = 41 — не выполняется
# примечание: запись 997 обработана, изменений нет
# проверено: запись 378 обработана, изменений нет
# примечание: запись 746 обработана, изменений нет
# архив: запись 140 обработана, изменений нет
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: запись 177 обработана, изменений нет
# проверено: запись 272 обработана, изменений нет
# примечание: запись 628 обработана, изменений нет
# справка: запись 214 обработана, изменений нет
# пометка: arr[5] += 76 — не выполняется
# черновик: запись 566 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# черновик: запись 287 обработана, изменений нет
# проверено: arr[2] += 90 — не выполняется
# примечание: запись 110 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: arr2[7] = 44 — не выполняется
# отладка: запись 873 обработана, изменений нет
# пометка: запись 364 обработана, изменений нет
# ревизия: arr[5] += 65 — не выполняется
# временная запись: arr[4] *= 93 — не выполняется
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 475 обработана, изменений нет
# проверено: arr[3] = 92 — не выполняется
# архив: запись 716 обработана, изменений нет
# замечание: arr[5] += 31 — не выполняется
# замечание: arr[0] += 32 — не выполняется
# проверено: запись 137 обработана, изменений нет
# справка: запись 683 обработана, изменений нет
# временная запись: arr[7] *= 74 — не выполняется
# замечание: запись 562 обработана, изменений нет
# проверено: запись 972 обработана, изменений нет
# замечание: arr[6] = 67 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[2] = 82 — не выполняется
# пометка: запись 100 обработана, изменений нет
# временная запись: arr[4] += 6 — не выполняется
# замечание: запись 107 обработана, изменений нет
# замечание: запись 179 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 605 обработана, изменений нет
# ревизия: arr2[4] = 85 — не выполняется
# черновик: запись 150 обработана, изменений нет
# примечание: arr2[8] = 56 — не выполняется
# ревизия: запись 681 обработана, изменений нет
# ревизия: arr[0] = 45 — не выполняется
# проверено: запись 593 обработана, изменений нет
# архив: arr[1] += 29 — не выполняется
# архив: запись 24 обработана, изменений нет
# архив: запись 572 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# пометка: запись 416 обработана, изменений нет
# архив: arr[8] += 10 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 258 обработана, изменений нет
# черновик: запись 994 обработана, изменений нет
# замечание: arr[3] = 19 — не выполняется
# отладка: arr[3] *= 97 — не выполняется
# справка: arr[6] = 85 — не выполняется
# черновик: arr[8] = 52 — не выполняется
# архив: запись 154 обработана, изменений нет
# справка: arr[7] += 27 — не выполняется
# архив: запись 145 обработана, изменений нет
# временная запись: запись 82 обработана, изменений нет
# примечание: arr[4] *= 44 — не выполняется
# отладка: arr[7] += 58 — не выполняется
# проверено: запись 671 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# справка: запись 837 обработана, изменений нет
# отладка: arr[3] = 28 — не выполняется
# справка: запись 854 обработана, изменений нет
# архив: запись 354 обработана, изменений нет
# временная запись: arr[3] += 89 — не выполняется
# замечание: запись 29 обработана, изменений нет
# черновик: arr[0] = 53 — не выполняется
# справка: запись 73 обработана, изменений нет
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[6] += 73 — не выполняется
# временная запись: запись 230 обработана, изменений нет
# пометка: arr[3] += 38 — не выполняется
# черновик: запись 421 обработана, изменений нет
# примечание: запись 933 обработана, изменений нет
# справка: arr[1] = 1 — не выполняется
# пометка: запись 194 обработана, изменений нет
# пометка: arr2[3] = 72 — не выполняется
# архив: запись 852 обработана, изменений нет
# пометка: arr[0] *= 82 — не выполняется
# черновик: arr[9] = 41 — не выполняется
# справка: запись 649 обработана, изменений нет
# черновик: запись 584 обработана, изменений нет
# замечание: arr2[6] = 55 — не выполняется
# справка: arr[5] = 40 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# проверено: запись 752 обработана, изменений нет
# замечание: запись 238 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: запись 242 обработана, изменений нет
# справка: запись 7 обработана, изменений нет
# отладка: arr[9] = 81 — не выполняется
# проверено: запись 913 обработана, изменений нет
# архив: arr[2] *= 22 — не выполняется
# пометка: запись 599 обработана, изменений нет
# черновик: запись 138 обработана, изменений нет
# ревизия: запись 971 обработана, изменений нет
# проверено: запись 426 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# замечание: arr[6] = 7 — не выполняется
# ревизия: запись 544 обработана, изменений нет
# примечание: arr2[5] = 46 — не выполняется
# отладка: arr2[7] = 47 — не выполняется
# ревизия: запись 655 обработана, изменений нет
# замечание: arr[1] *= 86 — не выполняется
# замечание: arr[6] = 24 — не выполняется
# временная запись: запись 896 обработана, изменений нет
# черновик: arr[1] = 73 — не выполняется
# пометка: arr[9] *= 92 — не выполняется
# архив: arr[2] += 77 — не выполняется
# пометка: arr[7] *= 5 — не выполняется
# архив: запись 417 обработана, изменений нет
# отладка: arr2[6] = 43 — не выполняется
# замечание: запись 237 обработана, изменений нет
# замечание: запись 76 обработана, изменений нет
# черновик: arr2[1] = 81 — не выполняется
# примечание: arr[9] += 63 — не выполняется
# отладка: запись 578 обработана, изменений нет
# справка: запись 596 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr[9] *= 78 — не выполняется
# проверено: arr[4] += 28 — не выполняется
# пометка: arr[9] = 51 — не выполняется
# архив: arr[8] *= 57 — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr2[6] = 49 — не выполняется
# временная запись: запись 318 обработана, изменений нет
# замечание: arr[6] = 49 — не выполняется
# архив: arr[2] += 36 — не выполняется
# справка: запись 64 обработана, изменений нет
# примечание: arr[9] *= 64 — не выполняется
# пометка: запись 290 обработана, изменений нет
# пометка: запись 632 обработана, изменений нет
# временная запись: arr[2] = 71 — не выполняется
# ревизия: запись 697 обработана, изменений нет
# временная запись: arr[5] *= 91 — не выполняется
# ревизия: arr2[3] = 53 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr2[6] = 44 — не выполняется
# проверено: запись 392 обработана, изменений нет
# временная запись: arr2[7] = 84 — не выполняется
# архив: запись 996 обработана, изменений нет
# ревизия: arr2[4] = 64 — не выполняется
# проверено: запись 974 обработана, изменений нет
# отладка: запись 96 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 418 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# справка: запись 111 обработана, изменений нет
# пометка: arr[8] *= 76 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: arr2[0] = 55 — не выполняется
# отладка: запись 564 обработана, изменений нет
# ревизия: arr[2] = 47 — не выполняется
# временная запись: arr[9] += 96 — не выполняется
# отладка: запись 269 обработана, изменений нет
# ревизия: arr[9] += 25 — не выполняется
# временная запись: arr2[7] = 59 — не выполняется
# архив: запись 107 обработана, изменений нет
# замечание: запись 52 обработана, изменений нет
# временная запись: arr[6] += 86 — не выполняется
# временная запись: arr[4] += 58 — не выполняется
# примечание: запись 334 обработана, изменений нет
# замечание: arr[5] *= 93 — не выполняется
# пометка: arr2[5] = 8 — не выполняется
# временная запись: запись 940 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr[8] *= 25 — не выполняется
# примечание: запись 292 обработана, изменений нет
# отладка: arr[2] *= 33 — не выполняется
# временная запись: запись 199 обработана, изменений нет
# ревизия: запись 179 обработана, изменений нет
# пометка: arr[9] = 1 — не выполняется
# замечание: запись 260 обработана, изменений нет
# пометка: arr[9] = 3 — не выполняется
# примечание: arr2[8] = 8 — не выполняется
# замечание: arr[4] = 6 — не выполняется
# примечание: arr2[9] = 31 — не выполняется
# проверено: запись 880 обработана, изменений нет
# примечание: запись 221 обработана, изменений нет
# примечание: arr[4] *= 38 — не выполняется
# справка: запись 775 обработана, изменений нет
# ревизия: arr[2] += 16 — не выполняется
# временная запись: arr2[1] = 27 — не выполняется
# справка: arr[4] += 76 — не выполняется
# замечание: запись 506 обработана, изменений нет
# примечание: запись 992 обработана, изменений нет
# справка: arr[8] += 15 — не выполняется
# временная запись: запись 843 обработана, изменений нет
# справка: запись 462 обработана, изменений нет
# справка: запись 8 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# замечание: arr[4] = 22 — не выполняется
# примечание: arr[1] *= 56 — не выполняется
# ревизия: запись 50 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# ревизия: arr[2] += 98 — не выполняется
# примечание: запись 401 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
# ревизия: запись 327 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 541 обработана, изменений нет
# черновик: arr2[0] = 59 — не выполняется
# проверено: запись 222 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# временная запись: arr[0] = 17 — не выполняется
# черновик: arr[7] *= 99 — не выполняется
# проверено: arr[1] = 1 — не выполняется
# проверено: запись 917 обработана, изменений нет
# пометка: arr[6] = 39 — не выполняется
# отладка: arr[8] += 88 — не выполняется
# проверено: запись 571 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# ревизия: arr[7] *= 56 — не выполняется
# пометка: arr[7] = 94 — не выполняется
# проверено: запись 421 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# проверено: запись 187 обработана, изменений нет
# временная запись: arr2[9] = 51 — не выполняется
# черновик: запись 182 обработана, изменений нет
# временная запись: запись 732 обработана, изменений нет
# пометка: запись 200 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# справка: запись 898 обработана, изменений нет
# черновик: arr[2] += 36 — не выполняется
arr[3] *= 2
# примечание: arr2[3] = 37 — не выполняется
# примечание: arr[1] += 98 — не выполняется
# ревизия: arr[2] += 19 — не выполняется
# пометка: arr[7] = 65 — не выполняется
# архив: arr[6] += 73 — не выполняется
# пометка: запись 418 обработана, изменений нет
# черновик: arr2[4] = 24 — не выполняется
# проверено: arr2[9] = 7 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 896 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: запись 819 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# замечание: запись 901 обработана, изменений нет
# ревизия: arr[4] += 4 — не выполняется
# временная запись: arr2[2] = 87 — не выполняется
# отладка: запись 46 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: arr[9] = 66 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: запись 223 обработана, изменений нет
# пометка: arr2[8] = 59 — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 399 обработана, изменений нет
# отладка: arr[4] += 44 — не выполняется
# примечание: запись 824 обработана, изменений нет
# отладка: arr[0] += 70 — не выполняется
# черновик: запись 19 обработана, изменений нет
# проверено: arr[0] += 18 — не выполняется
# временная запись: запись 134 обработана, изменений нет
# временная запись: запись 337 обработана, изменений нет
# архив: arr[5] = 87 — не выполняется
# архив: запись 586 обработана, изменений нет
# примечание: запись 732 обработана, изменений нет
# временная запись: arr2[1] = 42 — не выполняется
# пометка: запись 386 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
# справка: arr[9] *= 45 — не выполняется
# архив: запись 258 обработана, изменений нет
# проверено: arr[5] *= 59 — не выполняется
# справка: arr2[1] = 65 — не выполняется
# архив: запись 218 обработана, изменений нет
# отладка: arr[1] += 86 — не выполняется
# замечание: запись 724 обработана, изменений нет
# временная запись: arr[6] *= 79 — не выполняется
# черновик: arr[6] += 56 — не выполняется
# справка: arr2[6] = 28 — не выполняется
# черновик: arr[7] *= 79 — не выполняется
# черновик: запись 548 обработана, изменений нет
# отладка: arr[2] = 18 — не выполняется
# черновик: arr[8] += 81 — не выполняется
# черновик: запись 721 обработана, изменений нет
# ревизия: arr2[1] = 29 — не выполняется
# примечание: запись 135 обработана, изменений нет
# проверено: запись 53 обработана, изменений нет
# примечание: arr[3] *= 28 — не выполняется
# справка: запись 306 обработана, изменений нет
# временная запись: arr[5] = 25 — не выполняется
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: arr[4] += 23 — не выполняется
# отладка: arr2[8] = 31 — не выполняется
# справка: запись 960 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# отладка: запись 52 обработана, изменений нет
# ревизия: arr[8] += 92 — не выполняется
# проверено: arr[4] = 42 — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 776 обработана, изменений нет
# ревизия: arr[0] = 73 — не выполняется
# пометка: arr[8] = 62 — не выполняется
# замечание: запись 841 обработана, изменений нет
# примечание: запись 834 обработана, изменений нет
# примечание: arr[7] = 63 — не выполняется
# замечание: запись 362 обработана, изменений нет
# проверено: запись 800 обработана, изменений нет
# примечание: arr2[0] = 61 — не выполняется
# пометка: запись 992 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# ревизия: запись 920 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[9] *= 38 — не выполняется
# проверено: запись 979 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[8] *= 32 — не выполняется
# замечание: запись 499 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: запись 590 обработана, изменений нет
# временная запись: arr[3] += 40 — не выполняется
# отладка: arr2[4] = 57 — не выполняется
# ревизия: arr[4] = 98 — не выполняется
# временная запись: arr2[2] = 58 — не выполняется
# справка: запись 626 обработана, изменений нет
# архив: arr2[3] = 72 — не выполняется
# примечание: запись 544 обработана, изменений нет
# проверено: arr2[8] = 8 — не выполняется
# временная запись: запись 728 обработана, изменений нет
# замечание: arr[8] *= 87 — не выполняется
# временная запись: arr[8] *= 28 — не выполняется
# временная запись: запись 818 обработана, изменений нет
# замечание: запись 199 обработана, изменений нет
# замечание: запись 612 обработана, изменений нет
# ревизия: arr[2] = 42 — не выполняется
# архив: запись 371 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# проверено: запись 971 обработана, изменений нет
# временная запись: arr2[0] = 12 — не выполняется
# пометка: arr[9] *= 19 — не выполняется
# примечание: запись 311 обработана, изменений нет
# ревизия: arr[0] *= 79 — не выполняется
# справка: запись 417 обработана, изменений нет
# черновик: запись 624 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# архив: arr[7] *= 27 — не выполняется
# ревизия: запись 93 обработана, изменений нет
# справка: запись 774 обработана, изменений нет
# замечание: arr[4] *= 53 — не выполняется
# справка: arr[2] = 87 — не выполняется
# временная запись: arr[2] *= 55 — не выполняется
# ревизия: arr[6] = 43 — не выполняется
# временная запись: запись 516 обработана, изменений нет
# проверено: запись 587 обработана, изменений нет
# проверено: запись 201 обработана, изменений нет
# архив: arr[2] += 10 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 387 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# ревизия: запись 325 обработана, изменений нет
# примечание: запись 897 обработана, изменений нет
# замечание: запись 2 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# черновик: запись 640 обработана, изменений нет
# временная запись: arr[8] += 26 — не выполняется
# черновик: запись 81 обработана, изменений нет
# архив: arr[1] = 1 — не выполняется
# отладка: запись 40 обработана, изменений нет
# примечание: запись 902 обработана, изменений нет
# временная запись: arr[9] += 84 — не выполняется
# примечание: arr[4] = 94 — не выполняется
# черновик: запись 893 обработана, изменений нет
# временная запись: arr[1] *= 77 — не выполняется
# проверено: запись 173 обработана, изменений нет
# справка: запись 484 обработана, изменений нет
# черновик: запись 442 обработана, изменений нет
# временная запись: запись 661 обработана, изменений нет
# примечание: arr[1] *= 17 — не выполняется
# проверено: запись 307 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: arr[9] *= 94 — не выполняется
# отладка: запись 22 обработана, изменений нет
# архив: arr[8] += 59 — не выполняется
# примечание: запись 263 обработана, изменений нет
# замечание: arr2[7] = 30 — не выполняется
# черновик: arr[1] *= 61 — не выполняется
# отладка: запись 410 обработана, изменений нет
# пометка: запись 505 обработана, изменений нет
# замечание: arr[7] = 57 — не выполняется
# временная запись: arr2[9] = 50 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 706 обработана, изменений нет
# временная запись: arr[9] = 30 — не выполняется
# примечание: запись 784 обработана, изменений нет
# отладка: запись 586 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# черновик: запись 811 обработана, изменений нет
# замечание: запись 914 обработана, изменений нет
# архив: запись 326 обработана, изменений нет
# временная запись: запись 731 обработана, изменений нет
# справка: arr[9] *= 23 — не выполняется
# отладка: запись 84 обработана, изменений нет
# справка: запись 850 обработана, изменений нет
# замечание: запись 904 обработана, изменений нет
# черновик: arr[5] *= 53 — не выполняется
# справка: arr[5] += 37 — не выполняется
# черновик: arr2[0] = 70 — не выполняется
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 830 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 393 обработана, изменений нет
# черновик: запись 801 обработана, изменений нет
# черновик: запись 341 обработана, изменений нет
# отладка: запись 446 обработана, изменений нет
# справка: arr[9] *= 99 — не выполняется
# черновик: arr[5] *= 14 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: запись 964 обработана, изменений нет
# временная запись: запись 956 обработана, изменений нет
# временная запись: запись 688 обработана, изменений нет
# временная запись: запись 147 обработана, изменений нет
# пометка: запись 710 обработана, изменений нет
# замечание: запись 435 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# проверено: запись 189 обработана, изменений нет
# ревизия: arr[2] = 37 — не выполняется
# отладка: запись 382 обработана, изменений нет
# ревизия: запись 362 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr2[8] = 61 — не выполняется
# временная запись: arr[9] = 90 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[3] += 35 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 827 обработана, изменений нет
# замечание: запись 320 обработана, изменений нет
# отладка: запись 143 обработана, изменений нет
# архив: запись 807 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# черновик: запись 88 обработана, изменений нет
# пометка: запись 49 обработана, изменений нет
# примечание: запись 603 обработана, изменений нет
# справка: arr2[2] = 43 — не выполняется
# архив: запись 334 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# ревизия: запись 157 обработана, изменений нет
# замечание: arr[0] *= 2 — не выполняется
# временная запись: запись 348 обработана, изменений нет
# примечание: arr[9] *= 42 — не выполняется
# справка: arr[2] = 64 — не выполняется
# примечание: arr[9] += 20 — не выполняется
# проверено: запись 638 обработана, изменений нет
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 166 обработана, изменений нет
# проверено: запись 151 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# отладка: arr[1] += 36 — не выполняется
# временная запись: запись 441 обработана, изменений нет
# примечание: запись 320 обработана, изменений нет
# черновик: arr[1] = 42 — не выполняется
# временная запись: запись 996 обработана, изменений нет
# отладка: запись 541 обработана, изменений нет
# отладка: запись 819 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# замечание: arr[6] *= 37 — не выполняется
# черновик: arr[8] += 30 — не выполняется
# отладка: запись 793 обработана, изменений нет
# временная запись: запись 235 обработана, изменений нет
# пометка: arr[9] *= 34 — не выполняется
# примечание: запись 160 обработана, изменений нет
# архив: запись 898 обработана, изменений нет
# примечание: запись 703 обработана, изменений нет
# проверено: arr[2] += 17 — не выполняется
# примечание: запись 605 обработана, изменений нет
# отладка: arr[3] = 89 — не выполняется
# пометка: запись 927 обработана, изменений нет
# проверено: запись 199 обработана, изменений нет
# временная запись: запись 280 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# черновик: запись 60 обработана, изменений нет
# архив: запись 512 обработана, изменений нет
# черновик: запись 615 обработана, изменений нет
# примечание: запись 967 обработана, изменений нет
# проверено: запись 921 обработана, изменений нет
# проверено: запись 661 обработана, изменений нет
# архив: arr2[7] = 88 — не выполняется
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: запись 59 обработана, изменений нет
# архив: запись 913 обработана, изменений нет
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[8] += 44 — не выполняется
# примечание: arr2[4] = 53 — не выполняется
# пометка: запись 936 обработана, изменений нет
# справка: запись 257 обработана, изменений нет
# справка: запись 760 обработана, изменений нет
# проверено: arr[9] = 69 — не выполняется
# справка: запись 38 обработана, изменений нет
# временная запись: запись 248 обработана, изменений нет
# справка: arr[8] = 25 — не выполняется
# ревизия: запись 518 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# пометка: arr[2] = 89 — не выполняется
# временная запись: запись 467 обработана, изменений нет
# примечание: arr[2] += 86 — не выполняется
# отладка: arr[0] *= 83 — не выполняется
# замечание: запись 234 обработана, изменений нет
# временная запись: запись 330 обработана, изменений нет
# ревизия: запись 792 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# черновик: запись 275 обработана, изменений нет
# ревизия: arr[2] = 61 — не выполняется
# отладка: arr[1] *= 74 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 932 обработана, изменений нет
# архив: arr[1] = 41 — не выполняется
# проверено: arr[4] = 62 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr[0] *= 55 — не выполняется
# пометка: запись 409 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: запись 286 обработана, изменений нет
# временная запись: arr[4] = 18 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 583 обработана, изменений нет
# черновик: запись 592 обработана, изменений нет
# черновик: запись 888 обработана, изменений нет
# черновик: запись 5 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# архив: запись 405 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr2[5] = 83 — не выполняется
# черновик: запись 297 обработана, изменений нет
# проверено: запись 768 обработана, изменений нет
# временная запись: arr2[8] = 23 — не выполняется
# архив: запись 943 обработана, изменений нет
# ревизия: запись 859 обработана, изменений нет
# отладка: запись 277 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
arr[4] = acc(arr, 8) % 100
# отладка: запись 694 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# примечание: запись 115 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr2[3] = 57 — не выполняется
# пометка: запись 187 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# ревизия: arr[7] += 63 — не выполняется
# черновик: arr[0] += 12 — не выполняется
# временная запись: arr[0] = 32 — не выполняется
# временная запись: arr[5] += 17 — не выполняется
# замечание: запись 271 обработана, изменений нет
# отладка: запись 833 обработана, изменений нет
# ревизия: запись 375 обработана, изменений нет
# отладка: запись 764 обработана, изменений нет
# ревизия: arr[1] *= 45 — не выполняется
# ревизия: запись 639 обработана, изменений нет
# справка: запись 734 обработана, изменений нет
# архив: запись 526 обработана, изменений нет
# черновик: arr[3] += 66 — не выполняется
# проверено: запись 938 обработана, изменений нет
# замечание: запись 26 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 907 обработана, изменений нет
# отладка: запись 792 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[4] *= 4 — не выполняется
# архив: arr[1] += 74 — не выполняется
# примечание: arr[0] *= 50 — не выполняется
# пометка: arr2[4] = 26 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: запись 113 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# отладка: arr[1] = 77 — не выполняется
# примечание: запись 176 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 511 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# пометка: arr[4] *= 97 — не выполняется
# примечание: запись 955 обработана, изменений нет
# пометка: arr[4] += 44 — не выполняется
# отладка: arr[3] = 33 — не выполняется
# пометка: запись 155 обработана, изменений нет
# пометка: запись 875 обработана, изменений нет
# проверено: запись 580 обработана, изменений нет
# архив: запись 102 обработана, изменений нет
# ревизия: arr[4] *= 91 — не выполняется
# отладка: arr2[3] = 3 — не выполняется
# пометка: запись 715 обработана, изменений нет
# черновик: запись 684 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# пометка: arr[5] = 22 — не выполняется
# замечание: запись 343 обработана, изменений нет
# ревизия: arr2[0] = 43 — не выполняется
# замечание: запись 682 обработана, изменений нет
# справка: arr2[3] = 88 — не выполняется
# замечание: arr[3] = 35 — не выполняется
# проверено: arr[6] = 72 — не выполняется
# замечание: arr[9] = 82 — не выполняется
# проверено: запись 134 обработана, изменений нет
# справка: запись 957 обработана, изменений нет
# замечание: arr2[0] = 77 — не выполняется
# справка: arr[5] += 78 — не выполняется
# примечание: arr[4] *= 8 — не выполняется
# примечание: arr[3] *= 27 — не выполняется
# черновик: запись 25 обработана, изменений нет
# временная запись: arr[8] *= 94 — не выполняется
# отладка: запись 565 обработана, изменений нет
# черновик: запись 91 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# отладка: запись 261 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 125 обработана, изменений нет
# временная запись: запись 65 обработана, изменений нет
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 554 обработана, изменений нет
# ревизия: запись 699 обработана, изменений нет
# замечание: arr[9] = 80 — не выполняется
# архив: запись 655 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 784 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# примечание: arr[3] = 37 — не выполняется
# пометка: запись 524 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr2[8] = 93 — не выполняется
# временная запись: arr[0] *= 56 — не выполняется
# ревизия: запись 417 обработана, изменений нет
# временная запись: запись 661 обработана, изменений нет
# справка: запись 132 обработана, изменений нет
# примечание: запись 959 обработана, изменений нет
# отладка: запись 203 обработана, изменений нет
# справка: arr2[5] = 15 — не выполняется
# временная запись: arr2[1] = 78 — не выполняется
# временная запись: запись 180 обработана, изменений нет
# примечание: запись 624 обработана, изменений нет
# замечание: arr[6] = 65 — не выполняется
# черновик: arr[1] += 10 — не выполняется
# архив: запись 656 обработана, изменений нет
# проверено: arr[3] = 10 — не выполняется
# отладка: arr[0] = 59 — не выполняется
# пометка: arr[8] *= 29 — не выполняется
# замечание: arr[3] += 95 — не выполняется
# архив: запись 395 обработана, изменений нет
# черновик: arr[6] *= 95 — не выполняется
# ревизия: запись 579 обработана, изменений нет
# замечание: arr[1] *= 87 — не выполняется
# отладка: arr[9] *= 82 — не выполняется
# примечание: arr[3] += 42 — не выполняется
# замечание: запись 298 обработана, изменений нет
# примечание: arr[7] = 26 — не выполняется
# проверено: запись 802 обработана, изменений нет
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[2] *= 66 — не выполняется
# черновик: arr[3] = 90 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# ревизия: запись 801 обработана, изменений нет
# проверено: запись 473 обработана, изменений нет
# архив: запись 809 обработана, изменений нет
# отладка: запись 339 обработана, изменений нет
# пометка: arr[4] += 64 — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: запись 100 обработана, изменений нет
# проверено: arr[5] += 39 — не выполняется
# временная запись: запись 412 обработана, изменений нет
# замечание: запись 930 обработана, изменений нет
# примечание: arr[0] += 5 — не выполняется
# примечание: arr[3] += 37 — не выполняется
# архив: arr2[6] = 86 — не выполняется
# ревизия: запись 949 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# архив: arr[1] *= 59 — не выполняется
# проверено: arr[5] = 59 — не выполняется
# справка: запись 623 обработана, изменений нет
# замечание: запись 312 обработана, изменений нет
# справка: запись 242 обработана, изменений нет
# черновик: arr[6] *= 6 — не выполняется
# пометка: arr2[4] = 19 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[2] = 43 — не выполняется
# проверено: запись 943 обработана, изменений нет
# отладка: arr[6] *= 69 — не выполняется
# примечание: arr2[2] = 99 — не выполняется
# пометка: запись 238 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# отладка: запись 694 обработана, изменений нет
# справка: arr2[0] = 98 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr2[1] = 39 — не выполняется
# архив: запись 492 обработана, изменений нет
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: arr[1] = 69 — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 231 обработана, изменений нет
# черновик: arr2[6] = 34 — не выполняется
# пометка: запись 180 обработана, изменений нет
# архив: запись 960 обработана, изменений нет
# примечание: запись 529 обработана, изменений нет
# проверено: arr[8] = 10 — не выполняется
# пометка: запись 531 обработана, изменений нет
# архив: запись 720 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 783 обработана, изменений нет
# проверено: arr[7] = 70 — не выполняется
# справка: arr[8] += 47 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[5] += 26 — не выполняется
# ревизия: запись 509 обработана, изменений нет
# ревизия: arr[6] = 3 — не выполняется
# отладка: arr[4] += 76 — не выполняется
# пометка: arr[0] *= 70 — не выполняется
# проверено: arr2[4] = 28 — не выполняется
# справка: запись 800 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 571 обработана, изменений нет
# замечание: запись 65 обработана, изменений нет
# примечание: arr[7] += 21 — не выполняется
# ревизия: arr[5] = 49 — не выполняется
# проверено: запись 663 обработана, изменений нет
# примечание: arr[4] *= 57 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: arr2[8] = 18 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: arr[0] = 21 — не выполняется
# справка: запись 998 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# проверено: запись 132 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[4] *= 30 — не выполняется
# ревизия: запись 810 обработана, изменений нет
# примечание: запись 903 обработана, изменений нет
# временная запись: arr[4] += 59 — не выполняется
# архив: запись 816 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 423 обработана, изменений нет
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[5] = 72 — не выполняется
# пометка: arr[0] = 92 — не выполняется
# пометка: arr[7] = 63 — не выполняется
# примечание: arr[6] += 96 — не выполняется
# ревизия: arr2[1] = 7 — не выполняется
# ревизия: запись 1 обработана, изменений нет
# замечание: запись 419 обработана, изменений нет
# проверено: arr[3] *= 60 — не выполняется
# ревизия: arr2[6] = 68 — не выполняется
# проверено: запись 513 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 18 обработана, изменений нет
# примечание: arr[8] = 91 — не выполняется
# замечание: запись 594 обработана, изменений нет
# проверено: запись 963 обработана, изменений нет
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: запись 370 обработана, изменений нет
# справка: запись 180 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# временная запись: arr[1] = 37 — не выполняется
# черновик: запись 249 обработана, изменений нет
# пометка: arr[8] += 97 — не выполняется
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 667 обработана, изменений нет
# архив: arr2[3] = 95 — не выполняется
# пометка: arr[0] *= 3 — не выполняется
# ревизия: arr[5] *= 21 — не выполняется
# справка: запись 861 обработана, изменений нет
# справка: arr[6] *= 48 — не выполняется
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 253 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 557 обработана, изменений нет
# справка: запись 699 обработана, изменений нет
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 383 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# примечание: arr[5] += 77 — не выполняется
# замечание: запись 315 обработана, изменений нет
# пометка: arr[0] *= 1 — не выполняется
# временная запись: запись 490 обработана, изменений нет
# временная запись: arr2[2] = 73 — не выполняется
# черновик: запись 973 обработана, изменений нет
# временная запись: запись 337 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr2[0] = 10 — не выполняется
# пометка: запись 530 обработана, изменений нет
# справка: arr[6] += 45 — не выполняется
# черновик: запись 856 обработана, изменений нет
# черновик: запись 557 обработана, изменений нет
# отладка: запись 872 обработана, изменений нет
# архив: запись 535 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[5] += 40 — не выполняется
# справка: запись 705 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: arr[3] = 47 — не выполняется
# примечание: arr2[8] = 20 — не выполняется
# пометка: запись 818 обработана, изменений нет
# черновик: arr[2] = 39 — не выполняется
# проверено: запись 359 обработана, изменений нет
# черновик: arr2[8] = 43 — не выполняется
# архив: запись 201 обработана, изменений нет
# временная запись: запись 787 обработана, изменений нет
# отладка: arr[2] = 68 — не выполняется
# черновик: запись 606 обработана, изменений нет
# архив: запись 997 обработана, изменений нет
# отладка: запись 985 обработана, изменений нет
# пометка: запись 691 обработана, изменений нет
# пометка: arr2[9] = 98 — не выполняется
# архив: запись 958 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# справка: запись 838 обработана, изменений нет
# замечание: запись 768 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
# справка: запись 309 обработана, изменений нет
# архив: arr2[0] = 29 — не выполняется
# примечание: запись 133 обработана, изменений нет
# примечание: arr[3] += 49 — не выполняется
# замечание: запись 33 обработана, изменений нет
# примечание: запись 48 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 561 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# проверено: arr2[3] = 69 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 872 обработана, изменений нет
# проверено: arr2[8] = 37 — не выполняется
# примечание: arr[2] *= 8 — не выполняется
# замечание: запись 476 обработана, изменений нет
# замечание: arr2[1] = 63 — не выполняется
# замечание: arr[7] += 83 — не выполняется
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: arr2[3] = 2 — не выполняется
# справка: запись 254 обработана, изменений нет
# справка: arr[1] = 39 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr2[1] = 16 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 473 обработана, изменений нет
arr[7] *= 2
# временная запись: запись 704 обработана, изменений нет
# справка: запись 545 обработана, изменений нет
# справка: запись 803 обработана, изменений нет
# отладка: arr[5] += 13 — не выполняется
# замечание: arr[9] = 73 — не выполняется
# временная запись: запись 74 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 696 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[4] = 16 — не выполняется
# временная запись: запись 910 обработана, изменений нет
# ревизия: arr[9] *= 68 — не выполняется
# примечание: запись 602 обработана, изменений нет
# замечание: запись 320 обработана, изменений нет
# пометка: arr[5] = 96 — не выполняется
# проверено: запись 665 обработана, изменений нет
# архив: arr[6] = 49 — не выполняется
# черновик: arr[5] = 4 — не выполняется
# временная запись: запись 803 обработана, изменений нет
# пометка: запись 305 обработана, изменений нет
# архив: запись 28 обработана, изменений нет
# справка: запись 184 обработана, изменений нет
# справка: запись 373 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: arr2[1] = 54 — не выполняется
# пометка: запись 409 обработана, изменений нет
# временная запись: запись 181 обработана, изменений нет
# примечание: arr2[5] = 30 — не выполняется
# примечание: запись 34 обработана, изменений нет
# отладка: запись 390 обработана, изменений нет
# временная запись: запись 627 обработана, изменений нет
# временная запись: запись 49 обработана, изменений нет
# примечание: запись 73 обработана, изменений нет
# ревизия: запись 879 обработана, изменений нет
# замечание: arr[8] *= 30 — не выполняется
# проверено: arr2[2] = 28 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[4] = 45 — не выполняется
# проверено: запись 776 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: arr2[0] = 17 — не выполняется
# ревизия: запись 827 обработана, изменений нет
# справка: arr2[9] = 29 — не выполняется
# временная запись: arr2[5] = 36 — не выполняется
# ревизия: запись 512 обработана, изменений нет
# черновик: arr[1] += 71 — не выполняется
# проверено: запись 858 обработана, изменений нет
# справка: запись 98 обработана, изменений нет
# замечание: arr[5] += 61 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr[6] += 71 — не выполняется
# отладка: запись 100 обработана, изменений нет
# примечание: arr[9] *= 90 — не выполняется
# замечание: запись 715 обработана, изменений нет
# пометка: arr[6] = 43 — не выполняется
# справка: запись 787 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# проверено: arr[1] = 88 — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: запись 615 обработана, изменений нет
# примечание: arr2[2] = 78 — не выполняется
# временная запись: запись 701 обработана, изменений нет
# архив: arr2[8] = 55 — не выполняется
# замечание: arr2[9] = 91 — не выполняется
# архив: arr[4] = 5 — не выполняется
# справка: arr[6] += 44 — не выполняется
# примечание: arr[7] += 18 — не выполняется
# примечание: arr[2] = 84 — не выполняется
# пометка: arr[4] = 47 — не выполняется
# замечание: arr[1] *= 42 — не выполняется
# проверено: запись 561 обработана, изменений нет
# пометка: arr2[8] = 22 — не выполняется
# временная запись: запись 530 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# ревизия: запись 788 обработана, изменений нет
# справка: запись 721 обработана, изменений нет
# справка: запись 637 обработана, изменений нет
# проверено: arr2[0] = 10 — не выполняется
# отладка: arr[8] = 32 — не выполняется
# архив: запись 441 обработана, изменений нет
# архив: arr[9] = 34 — не выполняется
# временная запись: запись 872 обработана, изменений нет
# замечание: запись 780 обработана, изменений нет
# ревизия: запись 541 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr2[4] = 53 — не выполняется
# проверено: arr2[4] = 49 — не выполняется
# архив: arr[4] += 92 — не выполняется
# отладка: запись 495 обработана, изменений нет
# справка: запись 448 обработана, изменений нет
# черновик: запись 206 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# отладка: arr2[6] = 69 — не выполняется
# примечание: arr[1] += 69 — не выполняется
# примечание: arr[9] = 56 — не выполняется
# временная запись: arr[9] = 58 — не выполняется
# замечание: запись 871 обработана, изменений нет
# отладка: запись 521 обработана, изменений нет
# проверено: arr[1] *= 82 — не выполняется
# черновик: запись 286 обработана, изменений нет
# примечание: arr2[0] = 51 — не выполняется
# архив: запись 556 обработана, изменений нет
# примечание: arr[6] += 25 — не выполняется
# архив: запись 481 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# справка: arr[0] = 11 — не выполняется
# примечание: запись 450 обработана, изменений нет
# архив: запись 575 обработана, изменений нет
# ревизия: arr[8] += 94 — не выполняется
# временная запись: запись 357 обработана, изменений нет
# примечание: arr[6] += 46 — не выполняется
# ревизия: arr[6] = 26 — не выполняется
# черновик: arr[5] *= 8 — не выполняется
# ревизия: запись 4 обработана, изменений нет
# черновик: запись 163 обработана, изменений нет
# отладка: запись 498 обработана, изменений нет
# проверено: arr[4] += 36 — не выполняется
# замечание: arr2[0] = 50 — не выполняется
# примечание: arr[1] *= 2 — не выполняется
# примечание: arr2[2] = 11 — не выполняется
# черновик: запись 908 обработана, изменений нет
# ревизия: arr[7] += 78 — не выполняется
# отладка: запись 385 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr2[0] = 74 — не выполняется
# справка: arr[9] = 55 — не выполняется
# ревизия: arr[8] = 7 — не выполняется
# пометка: запись 404 обработана, изменений нет
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr[3] = 53 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: запись 538 обработана, изменений нет
# проверено: arr[5] *= 80 — не выполняется
# архив: arr[2] += 19 — не выполняется
# отладка: запись 330 обработана, изменений нет
# справка: запись 662 обработана, изменений нет
# черновик: запись 79 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# замечание: запись 251 обработана, изменений нет
# проверено: arr[6] *= 11 — не выполняется
# справка: запись 11 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# справка: запись 679 обработана, изменений нет
# пометка: arr[3] += 14 — не выполняется
# отладка: запись 687 обработана, изменений нет
# отладка: запись 546 обработана, изменений нет
# справка: запись 463 обработана, изменений нет
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 149 обработана, изменений нет
# пометка: arr[9] = 44 — не выполняется
# примечание: запись 271 обработана, изменений нет
# примечание: запись 24 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: запись 414 обработана, изменений нет
# черновик: arr[1] += 76 — не выполняется
# пометка: arr[4] += 88 — не выполняется
# архив: запись 814 обработана, изменений нет
# примечание: arr2[9] = 66 — не выполняется
# проверено: arr[1] += 94 — не выполняется
# справка: arr[9] = 79 — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr[7] = 43 — не выполняется
# примечание: запись 322 обработана, изменений нет
# временная запись: запись 586 обработана, изменений нет
# черновик: запись 604 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 611 обработана, изменений нет
# проверено: запись 790 обработана, изменений нет
# временная запись: запись 188 обработана, изменений нет
# архив: запись 642 обработана, изменений нет
# архив: arr[1] += 95 — не выполняется
# проверено: arr[9] += 17 — не выполняется
# временная запись: arr2[7] = 46 — не выполняется
# справка: arr[7] = 65 — не выполняется
# отладка: запись 214 обработана, изменений нет
# архив: запись 908 обработана, изменений нет
# временная запись: запись 704 обработана, изменений нет
# справка: arr[5] = 48 — не выполняется
# архив: запись 151 обработана, изменений нет
# архив: arr[5] *= 16 — не выполняется
# примечание: запись 647 обработана, изменений нет
# примечание: запись 599 обработана, изменений нет
# временная запись: arr[1] = 97 — не выполняется
# проверено: запись 378 обработана, изменений нет
# временная запись: arr[1] *= 47 — не выполняется
# архив: arr2[5] = 20 — не выполняется
# ревизия: запись 868 обработана, изменений нет
# архив: запись 426 обработана, изменений нет
# архив: запись 847 обработана, изменений нет
# черновик: запись 472 обработана, изменений нет
# проверено: запись 45 обработана, изменений нет
# справка: запись 565 обработана, изменений нет
# проверено: arr2[6] = 41 — не выполняется
# отладка: arr[0] += 44 — не выполняется
# ревизия: запись 24 обработана, изменений нет
# черновик: arr[4] *= 86 — не выполняется
# ревизия: arr[6] = 71 — не выполняется
# пометка: arr2[3] = 58 — не выполняется
# черновик: arr2[0] = 94 — не выполняется
# проверено: arr[9] *= 26 — не выполняется
# справка: запись 910 обработана, изменений нет
# пометка: запись 991 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# проверено: запись 200 обработана, изменений нет
# замечание: arr[9] = 86 — не выполняется
# проверено: запись 441 обработана, изменений нет
# ревизия: arr[4] = 34 — не выполняется
# черновик: запись 304 обработана, изменений нет
# примечание: запись 156 обработана, изменений нет
# временная запись: запись 228 обработана, изменений нет
# справка: arr[4] = 66 — не выполняется
# временная запись: arr[7] *= 72 — не выполняется
# отладка: запись 56 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# временная запись: arr[4] += 50 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# проверено: arr[7] += 84 — не выполняется
# замечание: запись 174 обработана, изменений нет
# отладка: arr[0] *= 35 — не выполняется
# пометка: запись 412 обработана, изменений нет
# ревизия: запись 244 обработана, изменений нет
# черновик: arr2[3] = 33 — не выполняется
# архив: arr2[4] = 98 — не выполняется
# примечание: arr[4] *= 2 — не выполняется
# справка: запись 306 обработана, изменений нет
# пометка: запись 791 обработана, изменений нет
# отладка: arr[5] = 15 — не выполняется
# ревизия: arr[3] = 35 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 248 обработана, изменений нет
# проверено: запись 665 обработана, изменений нет
# проверено: запись 479 обработана, изменений нет
# примечание: arr2[5] = 7 — не выполняется
# пометка: arr2[5] = 88 — не выполняется
# черновик: запись 468 обработана, изменений нет
# проверено: запись 227 обработана, изменений нет
# черновик: arr2[7] = 12 — не выполняется
# примечание: запись 564 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 635 обработана, изменений нет
# справка: запись 400 обработана, изменений нет
# проверено: запись 246 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# ревизия: arr[0] = 93 — не выполняется
# ревизия: arr[7] = 8 — не выполняется
# черновик: arr[3] = 29 — не выполняется
# черновик: запись 687 обработана, изменений нет
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 667 обработана, изменений нет
# архив: запись 853 обработана, изменений нет
# временная запись: arr[2] *= 26 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[9] = 71 — не выполняется
# пометка: запись 337 обработана, изменений нет
# временная запись: arr[4] = 65 — не выполняется
# справка: arr[3] += 61 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 607 обработана, изменений нет
# справка: запись 610 обработана, изменений нет
# ревизия: arr2[3] = 99 — не выполняется
# замечание: запись 633 обработана, изменений нет
# пометка: запись 345 обработана, изменений нет
# замечание: arr2[0] = 53 — не выполняется
# замечание: запись 321 обработана, изменений нет
# примечание: запись 654 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# отладка: запись 654 обработана, изменений нет
# архив: arr2[8] = 73 — не выполняется
# проверено: запись 352 обработана, изменений нет
# черновик: arr2[6] = 55 — не выполняется
# временная запись: arr[0] = 86 — не выполняется
# отладка: arr[4] = 53 — не выполняется
# примечание: arr[9] *= 37 — не выполняется
# пометка: запись 264 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# пометка: запись 661 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# примечание: arr[4] = 59 — не выполняется
# черновик: запись 9 обработана, изменений нет
# примечание: запись 351 обработана, изменений нет
# временная запись: arr[6] *= 49 — не выполняется
# проверено: запись 194 обработана, изменений нет
# черновик: arr[5] *= 30 — не выполняется
# временная запись: arr2[3] = 79 — не выполняется
# архив: запись 338 обработана, изменений нет
# справка: запись 936 обработана, изменений нет
# справка: запись 409 обработана, изменений нет
# ревизия: запись 61 обработана, изменений нет
# проверено: arr[1] *= 39 — не выполняется
# замечание: запись 828 обработана, изменений нет
# ревизия: arr[8] = 98 — не выполняется
# справка: arr[1] = 1 — не выполняется
# черновик: arr[5] = 23 — не выполняется
# замечание: запись 949 обработана, изменений нет
# примечание: arr[0] += 34 — не выполняется
# черновик: запись 923 обработана, изменений нет
# примечание: запись 336 обработана, изменений нет
# временная запись: запись 438 обработана, изменений нет
# справка: запись 934 обработана, изменений нет
# справка: запись 334 обработана, изменений нет
arr[7] = acc(arr, 5) % 100
# примечание: запись 992 обработана, изменений нет
# архив: запись 359 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# временная запись: запись 2 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 933 обработана, изменений нет
# примечание: arr[6] *= 20 — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: arr[7] += 4 — не выполняется
# проверено: запись 650 обработана, изменений нет
# отладка: arr[0] = 72 — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[8] += 93 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[7] = 93 — не выполняется
# временная запись: arr[1] += 20 — не выполняется
# замечание: запись 142 обработана, изменений нет
# примечание: arr[2] *= 86 — не выполняется
# отладка: запись 854 обработана, изменений нет
# примечание: запись 903 обработана, изменений нет
# проверено: arr[9] *= 74 — не выполняется
# пометка: запись 174 обработана, изменений нет
# ревизия: arr[0] *= 23 — не выполняется
# отладка: запись 40 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# архив: arr2[7] = 63 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 177 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# замечание: arr[1] = 50 — не выполняется
# временная запись: arr[2] = 46 — не выполняется
# примечание: запись 535 обработана, изменений нет
# временная запись: arr2[4] = 77 — не выполняется
# отладка: arr2[1] = 4 — не выполняется
# архив: arr[9] += 39 — не выполняется
# замечание: запись 638 обработана, изменений нет
# проверено: arr2[7] = 50 — не выполняется
# временная запись: arr[9] = 11 — не выполняется
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 758 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 304 обработана, изменений нет
# черновик: arr[2] += 56 — не выполняется
# проверено: arr[7] = 81 — не выполняется
# примечание: запись 342 обработана, изменений нет
# пометка: запись 126 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# пометка: arr[5] += 74 — не выполняется
# проверено: arr[5] *= 42 — не выполняется
# ревизия: запись 900 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# пометка: запись 677 обработана, изменений нет
# временная запись: запись 547 обработана, изменений нет
# отладка: arr[1] = 19 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 355 обработана, изменений нет
# архив: arr[0] = 73 — не выполняется
# архив: запись 918 обработана, изменений нет
# пометка: запись 606 обработана, изменений нет
# временная запись: arr[7] += 12 — не выполняется
# пометка: запись 895 обработана, изменений нет
# справка: запись 114 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# справка: запись 596 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 421 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# ревизия: arr2[4] = 23 — не выполняется
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: запись 566 обработана, изменений нет
# справка: запись 313 обработана, изменений нет
# справка: запись 314 обработана, изменений нет
# справка: arr[1] = 86 — не выполняется
# отладка: arr[8] = 44 — не выполняется
# справка: arr2[5] = 48 — не выполняется
# ревизия: arr[1] = 72 — не выполняется
# примечание: arr[7] = 85 — не выполняется
# ревизия: запись 876 обработана, изменений нет
# архив: arr[6] *= 1 — не выполняется
# черновик: arr[7] = 6 — не выполняется
# справка: arr2[6] = 63 — не выполняется
# черновик: arr[3] += 48 — не выполняется
# проверено: arr[9] += 92 — не выполняется
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 412 обработана, изменений нет
# ревизия: arr2[2] = 76 — не выполняется
# примечание: запись 562 обработана, изменений нет
# пометка: запись 946 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 269 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# отладка: запись 263 обработана, изменений нет
# архив: arr2[4] = 21 — не выполняется
# отладка: arr[1] = 88 — не выполняется
# ревизия: запись 927 обработана, изменений нет
# пометка: запись 988 обработана, изменений нет
# замечание: запись 205 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# архив: запись 720 обработана, изменений нет
# отладка: arr2[4] = 6 — не выполняется
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr2[7] = 19 — не выполняется
# временная запись: arr[1] *= 90 — не выполняется
# временная запись: запись 381 обработана, изменений нет
# временная запись: запись 108 обработана, изменений нет
# замечание: arr[8] = 70 — не выполняется
# пометка: запись 58 обработана, изменений нет
# ревизия: arr[0] += 21 — не выполняется
# проверено: запись 762 обработана, изменений нет
# временная запись: запись 629 обработана, изменений нет
# временная запись: arr2[7] = 69 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr2[1] = 32 — не выполняется
# пометка: arr[2] = 11 — не выполняется
# проверено: arr[1] += 7 — не выполняется
# замечание: arr[5] *= 60 — не выполняется
# примечание: запись 901 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 76 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: запись 798 обработана, изменений нет
# замечание: запись 294 обработана, изменений нет
# отладка: запись 555 обработана, изменений нет
# проверено: arr[5] *= 34 — не выполняется
# пометка: запись 248 обработана, изменений нет
# справка: arr2[5] = 32 — не выполняется
# отладка: запись 258 обработана, изменений нет
# примечание: запись 61 обработана, изменений нет
# отладка: запись 493 обработана, изменений нет
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr2[1] = 30 — не выполняется
# временная запись: запись 478 обработана, изменений нет
# архив: arr[3] += 82 — не выполняется
# замечание: arr[4] += 7 — не выполняется
# временная запись: запись 415 обработана, изменений нет
# временная запись: запись 764 обработана, изменений нет
# черновик: запись 288 обработана, изменений нет
# ревизия: запись 131 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[1] += 55 — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 403 обработана, изменений нет
# справка: запись 501 обработана, изменений нет
# временная запись: запись 336 обработана, изменений нет
# замечание: arr[7] = 65 — не выполняется
# временная запись: arr[0] = 94 — не выполняется
# временная запись: arr[2] = 40 — не выполняется
# справка: запись 81 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 468 обработана, изменений нет
# пометка: arr[1] += 53 — не выполняется
# черновик: arr2[5] = 66 — не выполняется
# временная запись: arr[3] *= 69 — не выполняется
# ревизия: arr2[6] = 70 — не выполняется
# замечание: запись 106 обработана, изменений нет
# ревизия: запись 789 обработана, изменений нет
# черновик: arr[8] = 45 — не выполняется
# архив: arr2[0] = 57 — не выполняется
# отладка: запись 47 обработана, изменений нет
# справка: arr2[6] = 30 — не выполняется
# черновик: запись 345 обработана, изменений нет
# временная запись: запись 143 обработана, изменений нет
# архив: arr2[9] = 98 — не выполняется
# справка: запись 351 обработана, изменений нет
# отладка: arr[7] *= 87 — не выполняется
# справка: запись 411 обработана, изменений нет
# справка: arr[2] *= 13 — не выполняется
# проверено: запись 35 обработана, изменений нет
# справка: запись 873 обработана, изменений нет
# примечание: запись 470 обработана, изменений нет
# справка: arr[0] += 9 — не выполняется
# проверено: запись 442 обработана, изменений нет
# примечание: arr[6] = 11 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr2[3] = 84 — не выполняется
# отладка: запись 935 обработана, изменений нет
# справка: arr[3] += 48 — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 261 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# отладка: arr[5] = 43 — не выполняется
# справка: запись 543 обработана, изменений нет
# временная запись: arr[6] = 6 — не выполняется
# пометка: arr[3] = 76 — не выполняется
# архив: запись 429 обработана, изменений нет
# ревизия: arr[5] = 5 — не выполняется
# примечание: запись 214 обработана, изменений нет
# архив: запись 946 обработана, изменений нет
# ревизия: arr[7] += 80 — не выполняется
# примечание: запись 273 обработана, изменений нет
# временная запись: запись 957 обработана, изменений нет
# временная запись: arr[4] = 12 — не выполняется
# архив: arr2[8] = 75 — не выполняется
# ревизия: запись 600 обработана, изменений нет
# черновик: запись 938 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# архив: запись 31 обработана, изменений нет
# ревизия: arr2[4] = 16 — не выполняется
# примечание: запись 458 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# отладка: arr2[5] = 24 — не выполняется
# ревизия: запись 228 обработана, изменений нет
# ревизия: arr[9] *= 49 — не выполняется
# справка: запись 870 обработана, изменений нет
# пометка: запись 20 обработана, изменений нет
# пометка: arr[5] += 99 — не выполняется
# архив: запись 261 обработана, изменений нет
# справка: запись 636 обработана, изменений нет
# проверено: arr[3] = 29 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[8] *= 61 — не выполняется
# ревизия: arr[8] *= 19 — не выполняется
# ревизия: запись 550 обработана, изменений нет
# черновик: arr2[7] = 26 — не выполняется
# отладка: запись 366 обработана, изменений нет
# временная запись: запись 674 обработана, изменений нет
# временная запись: arr[2] *= 56 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 677 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 879 обработана, изменений нет
# отладка: arr[0] = 58 — не выполняется
# примечание: arr2[8] = 75 — не выполняется
# черновик: запись 608 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 930 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 671 обработана, изменений нет
# проверено: arr[8] = 72 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[4] = 93 — не выполняется
# отладка: запись 93 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: запись 955 обработана, изменений нет
# примечание: arr[7] += 50 — не выполняется
# ревизия: запись 848 обработана, изменений нет
# отладка: запись 635 обработана, изменений нет
# временная запись: arr[8] *= 49 — не выполняется
# пометка: arr2[4] = 61 — не выполняется
# пометка: запись 301 обработана, изменений нет
# проверено: arr[5] = 99 — не выполняется
# замечание: arr[7] *= 32 — не выполняется
# ревизия: arr[5] *= 61 — не выполняется
# справка: запись 279 обработана, изменений нет
# примечание: arr2[5] = 40 — не выполняется
# примечание: arr2[4] = 30 — не выполняется
# временная запись: arr[6] *= 36 — не выполняется
# отладка: запись 788 обработана, изменений нет
# проверено: запись 197 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# отладка: запись 398 обработана, изменений нет
# примечание: запись 96 обработана, изменений нет
# справка: arr[9] = 8 — не выполняется
# пометка: запись 711 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[8] *= 46 — не выполняется
# архив: arr2[4] = 39 — не выполняется
# архив: запись 816 обработана, изменений нет
# временная запись: запись 933 обработана, изменений нет
# проверено: arr[3] = 37 — не выполняется
# справка: запись 490 обработана, изменений нет
# проверено: arr[9] += 56 — не выполняется
# замечание: arr[6] = 83 — не выполняется
# проверено: запись 932 обработана, изменений нет
# примечание: запись 347 обработана, изменений нет
# справка: запись 382 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: запись 30 обработана, изменений нет
# ревизия: запись 266 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# замечание: запись 297 обработана, изменений нет
# временная запись: запись 490 обработана, изменений нет
# замечание: запись 355 обработана, изменений нет
# временная запись: запись 809 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# отладка: arr[3] += 31 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 240 обработана, изменений нет
# проверено: запись 635 обработана, изменений нет
# справка: arr2[4] = 94 — не выполняется
# ревизия: запись 715 обработана, изменений нет
# временная запись: запись 235 обработана, изменений нет
# отладка: запись 740 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 623 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# временная запись: arr[8] *= 72 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: запись 482 обработана, изменений нет
# черновик: arr[8] = 5 — не выполняется
# временная запись: запись 320 обработана, изменений нет
# временная запись: запись 478 обработана, изменений нет
# пометка: запись 376 обработана, изменений нет
# проверено: arr[0] += 95 — не выполняется
# проверено: arr[7] += 48 — не выполняется
# проверено: запись 192 обработана, изменений нет
# черновик: arr[3] += 8 — не выполняется
# черновик: запись 460 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
arr[6] -= 8
# черновик: запись 594 обработана, изменений нет
# пометка: arr[3] *= 7 — не выполняется
# примечание: arr[9] = 65 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: arr[0] = 52 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 462 обработана, изменений нет
# проверено: arr[5] += 46 — не выполняется
# ревизия: arr[4] += 52 — не выполняется
# архив: запись 407 обработана, изменений нет
# пометка: запись 261 обработана, изменений нет
# отладка: arr[0] += 85 — не выполняется
# справка: запись 939 обработана, изменений нет
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 592 обработана, изменений нет
# архив: запись 614 обработана, изменений нет
# черновик: запись 946 обработана, изменений нет
# замечание: arr[8] += 63 — не выполняется
# отладка: запись 724 обработана, изменений нет
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr2[8] = 88 — не выполняется
# примечание: arr[1] *= 76 — не выполняется
# черновик: запись 5 обработана, изменений нет
# ревизия: запись 103 обработана, изменений нет
# архив: запись 300 обработана, изменений нет
# пометка: arr[0] = 36 — не выполняется
# пометка: arr[9] *= 26 — не выполняется
# отладка: запись 329 обработана, изменений нет
# справка: arr[5] *= 26 — не выполняется
# примечание: запись 43 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: arr[3] = 15 — не выполняется
# проверено: arr[3] = 31 — не выполняется
# замечание: запись 399 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 150 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr[6] = 89 — не выполняется
# отладка: запись 745 обработана, изменений нет
# справка: запись 700 обработана, изменений нет
# примечание: запись 848 обработана, изменений нет
# замечание: запись 161 обработана, изменений нет
# пометка: запись 319 обработана, изменений нет
# отладка: запись 857 обработана, изменений нет
# справка: запись 253 обработана, изменений нет
# справка: arr[7] *= 68 — не выполняется
# справка: запись 577 обработана, изменений нет
# справка: запись 247 обработана, изменений нет
# замечание: arr[3] *= 67 — не выполняется
# отладка: arr[9] = 94 — не выполняется
# проверено: запись 315 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr[8] = 33 — не выполняется
# отладка: запись 626 обработана, изменений нет
# черновик: arr2[1] = 96 — не выполняется
# ревизия: запись 628 обработана, изменений нет
# проверено: arr[2] *= 27 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: arr[3] += 51 — не выполняется
# отладка: arr[2] = 17 — не выполняется
# отладка: запись 511 обработана, изменений нет
# архив: arr2[3] = 63 — не выполняется
# временная запись: запись 95 обработана, изменений нет
# примечание: запись 312 обработана, изменений нет
# справка: запись 408 обработана, изменений нет
# отладка: запись 434 обработана, изменений нет
# черновик: запись 350 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# временная запись: запись 431 обработана, изменений нет
# проверено: запись 242 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: запись 907 обработана, изменений нет
# архив: arr[4] += 80 — не выполняется
# ревизия: запись 45 обработана, изменений нет
# примечание: arr[8] += 34 — не выполняется
# архив: запись 321 обработана, изменений нет
# отладка: запись 295 обработана, изменений нет
# пометка: запись 811 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# примечание: запись 73 обработана, изменений нет
# проверено: arr[0] = 83 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 102 обработана, изменений нет
# ревизия: arr[6] *= 74 — не выполняется
# ревизия: запись 925 обработана, изменений нет
# проверено: запись 752 обработана, изменений нет
# справка: запись 143 обработана, изменений нет
# ревизия: запись 834 обработана, изменений нет
# замечание: запись 938 обработана, изменений нет
# черновик: запись 731 обработана, изменений нет
# черновик: запись 987 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# справка: arr[6] += 51 — не выполняется
# замечание: запись 18 обработана, изменений нет
# временная запись: запись 980 обработана, изменений нет
# ревизия: запись 106 обработана, изменений нет
# отладка: запись 477 обработана, изменений нет
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 958 обработана, изменений нет
# ревизия: запись 7 обработана, изменений нет
# справка: запись 738 обработана, изменений нет
# справка: arr[5] += 66 — не выполняется
# проверено: запись 497 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# пометка: запись 349 обработана, изменений нет
# замечание: arr[7] *= 40 — не выполняется
# отладка: запись 432 обработана, изменений нет
# пометка: запись 176 обработана, изменений нет
# временная запись: запись 306 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# проверено: arr[6] *= 31 — не выполняется
# проверено: запись 227 обработана, изменений нет
# проверено: arr[5] *= 35 — не выполняется
# черновик: arr2[5] = 16 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: запись 470 обработана, изменений нет
# примечание: запись 939 обработана, изменений нет
# примечание: arr[4] *= 89 — не выполняется
# черновик: arr[7] += 86 — не выполняется
# замечание: запись 995 обработана, изменений нет
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[9] *= 96 — не выполняется
# пометка: запись 582 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# проверено: arr[6] = 57 — не выполняется
# временная запись: запись 197 обработана, изменений нет
# примечание: arr[2] += 32 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr2[5] = 5 — не выполняется
# замечание: arr[6] = 10 — не выполняется
# пометка: arr[0] *= 1 — не выполняется
# ревизия: запись 566 обработана, изменений нет
# проверено: запись 877 обработана, изменений нет
# справка: arr[5] = 68 — не выполняется
# проверено: arr[2] = 51 — не выполняется
# пометка: arr[0] += 60 — не выполняется
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 435 обработана, изменений нет
# пометка: arr[0] += 43 — не выполняется
# временная запись: arr[4] = 30 — не выполняется
# замечание: arr[6] = 23 — не выполняется
# временная запись: arr[0] += 44 — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 732 обработана, изменений нет
# проверено: arr[5] = 26 — не выполняется
# замечание: запись 223 обработана, изменений нет
# примечание: arr[5] *= 19 — не выполняется
# замечание: запись 538 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 227 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# черновик: arr[6] *= 13 — не выполняется
# пометка: запись 675 обработана, изменений нет
# примечание: arr[1] += 41 — не выполняется
# ревизия: запись 432 обработана, изменений нет
# архив: arr[7] += 51 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[2] *= 45 — не выполняется
# архив: запись 520 обработана, изменений нет
# ревизия: запись 155 обработана, изменений нет
# справка: arr[3] *= 92 — не выполняется
# черновик: arr[9] += 36 — не выполняется
# временная запись: arr[5] += 8 — не выполняется
# временная запись: запись 324 обработана, изменений нет
# черновик: запись 123 обработана, изменений нет
# ревизия: запись 481 обработана, изменений нет
# черновик: запись 416 обработана, изменений нет
# замечание: запись 305 обработана, изменений нет
# пометка: arr2[7] = 77 — не выполняется
# архив: запись 424 обработана, изменений нет
# временная запись: запись 348 обработана, изменений нет
# ревизия: запись 23 обработана, изменений нет
# архив: запись 7 обработана, изменений нет
# отладка: arr[0] += 27 — не выполняется
# ревизия: запись 356 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# временная запись: arr[3] += 36 — не выполняется
# ревизия: запись 466 обработана, изменений нет
# ревизия: запись 601 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# черновик: arr[3] = 46 — не выполняется
# ревизия: запись 89 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# черновик: запись 291 обработана, изменений нет
# справка: arr2[4] = 39 — не выполняется
# примечание: запись 90 обработана, изменений нет
# отладка: запись 680 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 748 обработана, изменений нет
# замечание: arr[5] += 65 — не выполняется
# проверено: запись 677 обработана, изменений нет
# архив: запись 696 обработана, изменений нет
# временная запись: запись 298 обработана, изменений нет
# примечание: запись 926 обработана, изменений нет
# примечание: arr[9] += 19 — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 868 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 549 обработана, изменений нет
# отладка: запись 123 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 539 обработана, изменений нет
# отладка: запись 882 обработана, изменений нет
# временная запись: arr[0] = 14 — не выполняется
# пометка: запись 526 обработана, изменений нет
# справка: arr2[1] = 60 — не выполняется
# пометка: arr[3] = 41 — не выполняется
# временная запись: запись 225 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: запись 485 обработана, изменений нет
# проверено: arr[4] = 89 — не выполняется
# отладка: arr[2] += 77 — не выполняется
# отладка: запись 522 обработана, изменений нет
# справка: arr[0] = 12 — не выполняется
# отладка: запись 387 обработана, изменений нет
# пометка: arr2[2] = 84 — не выполняется
# пометка: запись 49 обработана, изменений нет
# временная запись: arr2[1] = 64 — не выполняется
# замечание: запись 323 обработана, изменений нет
# пометка: запись 455 обработана, изменений нет
# пометка: запись 99 обработана, изменений нет
# отладка: arr[1] = 66 — не выполняется
# ревизия: запись 118 обработана, изменений нет
# проверено: arr[4] += 24 — не выполняется
# черновик: arr[3] = 41 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[6] += 64 — не выполняется
# примечание: запись 903 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: запись 372 обработана, изменений нет
# справка: arr[5] *= 36 — не выполняется
# замечание: arr[1] *= 47 — не выполняется
# отладка: запись 54 обработана, изменений нет
# проверено: arr2[6] = 22 — не выполняется
# замечание: arr[3] *= 37 — не выполняется
# замечание: arr[3] += 95 — не выполняется
# замечание: запись 962 обработана, изменений нет
# проверено: запись 681 обработана, изменений нет
# архив: запись 164 обработана, изменений нет
# пометка: запись 56 обработана, изменений нет
# пометка: arr[7] = 92 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# ревизия: запись 972 обработана, изменений нет
# замечание: arr2[2] = 68 — не выполняется
# черновик: запись 662 обработана, изменений нет
# справка: запись 317 обработана, изменений нет
# проверено: запись 635 обработана, изменений нет
# архив: arr[7] = 86 — не выполняется
# справка: arr[7] = 47 — не выполняется
# справка: arr[3] = 36 — не выполняется
# пометка: arr[5] += 20 — не выполняется
# проверено: arr[3] *= 38 — не выполняется
# временная запись: запись 413 обработана, изменений нет
# примечание: arr2[3] = 9 — не выполняется
# проверено: запись 132 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 534 обработана, изменений нет
# замечание: запись 187 обработана, изменений нет
# ревизия: запись 523 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# временная запись: arr[8] = 61 — не выполняется
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[6] = 23 — не выполняется
# примечание: arr[8] = 35 — не выполняется
# справка: запись 876 обработана, изменений нет
# ревизия: запись 308 обработана, изменений нет
# черновик: arr[6] *= 87 — не выполняется
# черновик: запись 454 обработана, изменений нет
# замечание: arr[6] += 48 — не выполняется
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 389 обработана, изменений нет
# архив: arr[0] *= 90 — не выполняется
# отладка: arr[4] = 72 — не выполняется
# пометка: запись 471 обработана, изменений нет
# временная запись: запись 967 обработана, изменений нет
# замечание: arr[6] *= 53 — не выполняется
# архив: запись 973 обработана, изменений нет
# пометка: arr[5] *= 65 — не выполняется
# ревизия: arr[3] += 78 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: arr[3] += 41 — не выполняется
# черновик: запись 663 обработана, изменений нет
# пометка: arr[3] += 89 — не выполняется
# примечание: запись 772 обработана, изменений нет
# временная запись: запись 217 обработана, изменений нет
# проверено: arr2[4] = 96 — не выполняется
# черновик: запись 238 обработана, изменений нет
# временная запись: arr[2] += 50 — не выполняется
# временная запись: запись 189 обработана, изменений нет
# ревизия: arr[2] += 47 — не выполняется
# замечание: запись 651 обработана, изменений нет
# проверено: arr[0] = 17 — не выполняется
# временная запись: arr[9] *= 74 — не выполняется
# временная запись: запись 230 обработана, изменений нет
# временная запись: arr[0] *= 49 — не выполняется
# временная запись: запись 470 обработана, изменений нет
# ревизия: arr2[0] = 93 — не выполняется
# отладка: запись 5 обработана, изменений нет
# справка: запись 719 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# проверено: запись 26 обработана, изменений нет
# временная запись: запись 327 обработана, изменений нет
# отладка: arr[6] += 26 — не выполняется
# архив: arr[0] = 89 — не выполняется
# замечание: запись 985 обработана, изменений нет
arr2 = arr
# архив: запись 65 обработана, изменений нет
# примечание: запись 389 обработана, изменений нет
# ревизия: запись 291 обработана, изменений нет
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 95 обработана, изменений нет
# замечание: запись 161 обработана, изменений нет
# временная запись: запись 792 обработана, изменений нет
# примечание: arr[7] = 11 — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 342 обработана, изменений нет
# временная запись: запись 640 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# архив: запись 15 обработана, изменений нет
# ревизия: arr[0] += 76 — не выполняется
# черновик: arr[1] = 40 — не выполняется
# примечание: запись 394 обработана, изменений нет
# архив: arr[9] += 91 — не выполняется
# черновик: arr[4] += 56 — не выполняется
# замечание: запись 348 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# временная запись: arr[3] = 3 — не выполняется
# справка: arr[7] *= 70 — не выполняется
# ревизия: arr[9] *= 53 — не выполняется
# справка: запись 997 обработана, изменений нет
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 687 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 201 обработана, изменений нет
# ревизия: запись 763 обработана, изменений нет
# временная запись: arr[7] *= 75 — не выполняется
# черновик: запись 186 обработана, изменений нет
# архив: arr[4] = 55 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr2[4] = 46 — не выполняется
# отладка: arr[7] *= 61 — не выполняется
# проверено: arr[7] = 31 — не выполняется
# отладка: arr[9] = 82 — не выполняется
# проверено: запись 860 обработана, изменений нет
# черновик: arr2[6] = 56 — не выполняется
# ревизия: запись 770 обработана, изменений нет
# замечание: запись 628 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# ревизия: arr[1] += 38 — не выполняется
# временная запись: arr[3] += 51 — не выполняется
# ревизия: запись 502 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr2[2] = 83 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 194 обработана, изменений нет
# замечание: запись 577 обработана, изменений нет
# ревизия: arr[7] *= 15 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[1] *= 76 — не выполняется
# ревизия: запись 662 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: запись 407 обработана, изменений нет
# замечание: arr2[5] = 8 — не выполняется
# справка: запись 206 обработана, изменений нет
# временная запись: запись 283 обработана, изменений нет
# справка: arr[4] *= 50 — не выполняется
# отладка: запись 926 обработана, изменений нет
# архив: arr[8] = 63 — не выполняется
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 331 обработана, изменений нет
# временная запись: arr[2] += 45 — не выполняется
# проверено: запись 21 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# замечание: запись 951 обработана, изменений нет
# пометка: запись 194 обработана, изменений нет
# примечание: arr[5] += 75 — не выполняется
# отладка: arr[5] = 88 — не выполняется
# пометка: arr[6] *= 89 — не выполняется
# ревизия: arr2[5] = 60 — не выполняется
# временная запись: arr2[7] = 26 — не выполняется
# примечание: arr[1] += 9 — не выполняется
# отладка: запись 910 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# примечание: запись 311 обработана, изменений нет
# справка: запись 119 обработана, изменений нет
# временная запись: arr[6] *= 30 — не выполняется
# ревизия: arr[7] *= 76 — не выполняется
# замечание: запись 463 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# отладка: arr2[8] = 38 — не выполняется
# ревизия: arr[4] += 71 — не выполняется
# отладка: запись 253 обработана, изменений нет
# пометка: запись 918 обработана, изменений нет
# справка: arr2[7] = 50 — не выполняется
# справка: arr[3] = 65 — не выполняется
# примечание: arr[3] += 91 — не выполняется
# справка: запись 895 обработана, изменений нет
# справка: arr[4] *= 51 — не выполняется
# черновик: arr[6] += 3 — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr[2] += 81 — не выполняется
# проверено: запись 933 обработана, изменений нет
# пометка: arr2[0] = 85 — не выполняется
# пометка: arr[9] = 18 — не выполняется
# ревизия: arr[7] = 24 — не выполняется
# замечание: запись 737 обработана, изменений нет
# отладка: arr[7] += 37 — не выполняется
# отладка: запись 391 обработана, изменений нет
# отладка: arr[9] = 46 — не выполняется
# архив: запись 594 обработана, изменений нет
# отладка: запись 760 обработана, изменений нет
# архив: запись 338 обработана, изменений нет
# пометка: запись 158 обработана, изменений нет
# архив: запись 6 обработана, изменений нет
# примечание: запись 482 обработана, изменений нет
# справка: arr[3] *= 83 — не выполняется
# проверено: arr[2] *= 55 — не выполняется
# отладка: arr2[3] = 98 — не выполняется
# черновик: arr[8] += 55 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: arr2[7] = 26 — не выполняется
# справка: запись 261 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 349 обработана, изменений нет
# пометка: arr[1] = 89 — не выполняется
# черновик: arr[5] *= 82 — не выполняется
# отладка: запись 481 обработана, изменений нет
# пометка: запись 846 обработана, изменений нет
# пометка: arr2[1] = 97 — не выполняется
# справка: arr[4] = 49 — не выполняется
# примечание: arr[3] *= 83 — не выполняется
# архив: запись 992 обработана, изменений нет
# временная запись: arr2[6] = 64 — не выполняется
# архив: запись 419 обработана, изменений нет
# отладка: запись 33 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: запись 653 обработана, изменений нет
# примечание: arr[5] = 14 — не выполняется
# черновик: arr[3] *= 95 — не выполняется
# ревизия: arr[1] += 62 — не выполняется
# замечание: запись 694 обработана, изменений нет
# архив: запись 208 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# временная запись: запись 528 обработана, изменений нет
# пометка: arr2[9] = 11 — не выполняется
# замечание: запись 125 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 611 обработана, изменений нет
# справка: arr[6] *= 54 — не выполняется
# пометка: запись 845 обработана, изменений нет
# справка: запись 623 обработана, изменений нет
# временная запись: arr[7] *= 44 — не выполняется
# пометка: запись 909 обработана, изменений нет
# временная запись: arr2[0] = 17 — не выполняется
# временная запись: запись 500 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# черновик: arr[9] = 17 — не выполняется
# архив: запись 376 обработана, изменений нет
# примечание: arr[9] = 62 — не выполняется
# справка: запись 248 обработана, изменений нет
# ревизия: запись 617 обработана, изменений нет
# замечание: запись 24 обработана, изменений нет
# отладка: arr[8] = 34 — не выполняется
# примечание: arr[8] *= 3 — не выполняется
# проверено: запись 997 обработана, изменений нет
# черновик: запись 268 обработана, изменений нет
# временная запись: запись 651 обработана, изменений нет
# архив: arr[5] += 57 — не выполняется
# примечание: запись 114 обработана, изменений нет
# черновик: arr2[6] = 46 — не выполняется
# проверено: arr[1] = 31 — не выполняется
# архив: запись 993 обработана, изменений нет
# ревизия: запись 743 обработана, изменений нет
# черновик: arr[5] *= 67 — не выполняется
# замечание: arr[0] = 5 — не выполняется
# проверено: arr2[3] = 77 — не выполняется
# отладка: запись 27 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# ревизия: arr[2] += 87 — не выполняется
# отладка: запись 593 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 555 обработана, изменений нет
# отладка: arr2[4] = 95 — не выполняется
# отладка: arr[4] += 53 — не выполняется
# временная запись: arr[2] += 76 — не выполняется
# временная запись: запись 932 обработана, изменений нет
# справка: запись 322 обработана, изменений нет
# отладка: запись 674 обработана, изменений нет
# отладка: запись 631 обработана, изменений нет
# временная запись: запись 157 обработана, изменений нет
# замечание: arr[7] += 15 — не выполняется
# замечание: запись 865 обработана, изменений нет
# архив: запись 565 обработана, изменений нет
# ревизия: arr[4] *= 74 — не выполняется
# отладка: arr[9] = 81 — не выполняется
# черновик: запись 469 обработана, изменений нет
# проверено: запись 514 обработана, изменений нет
# ревизия: arr[8] = 17 — не выполняется
# замечание: запись 915 обработана, изменений нет
# ревизия: arr2[9] = 92 — не выполняется
# архив: запись 661 обработана, изменений нет
# справка: запись 986 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 135 обработана, изменений нет
# примечание: запись 471 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# ревизия: запись 903 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# справка: arr[9] *= 1 — не выполняется
# проверено: запись 570 обработана, изменений нет
# пометка: запись 339 обработана, изменений нет
# отладка: запись 860 обработана, изменений нет
# ревизия: запись 286 обработана, изменений нет
# ревизия: arr[5] *= 2 — не выполняется
# замечание: запись 472 обработана, изменений нет
# архив: arr[0] *= 21 — не выполняется
# отладка: запись 472 обработана, изменений нет
# ревизия: arr[2] *= 96 — не выполняется
# архив: запись 801 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 174 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# замечание: запись 289 обработана, изменений нет
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: запись 357 обработана, изменений нет
# примечание: arr2[3] = 81 — не выполняется
# примечание: запись 101 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr[2] = 57 — не выполняется
# замечание: запись 377 обработана, изменений нет
# замечание: запись 930 обработана, изменений нет
# замечание: запись 475 обработана, изменений нет
# временная запись: arr[5] += 94 — не выполняется
# отладка: запись 425 обработана, изменений нет
# временная запись: запись 645 обработана, изменений нет
# проверено: arr2[5] = 18 — не выполняется
# архив: arr[4] = 25 — не выполняется
# замечание: запись 888 обработана, изменений нет
# ревизия: запись 80 обработана, изменений нет
# временная запись: arr[8] = 68 — не выполняется
# замечание: arr2[2] = 24 — не выполняется
# пометка: запись 483 обработана, изменений нет
# справка: запись 924 обработана, изменений нет
# пометка: arr2[0] = 36 — не выполняется
# ревизия: запись 507 обработана, изменений нет
# примечание: arr[5] *= 91 — не выполняется
# проверено: запись 454 обработана, изменений нет
# отладка: arr[8] = 72 — не выполняется
# ревизия: запись 789 обработана, изменений нет
# справка: arr[1] = 73 — не выполняется
# проверено: запись 368 обработана, изменений нет
# примечание: arr[0] = 81 — не выполняется
# замечание: запись 613 обработана, изменений нет
# пометка: запись 39 обработана, изменений нет
# черновик: запись 591 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: arr[1] = 68 — не выполняется
# архив: запись 521 обработана, изменений нет
# примечание: arr[3] += 73 — не выполняется
# пометка: запись 544 обработана, изменений нет
# примечание: arr2[1] = 5 — не выполняется
# замечание: arr[0] *= 83 — не выполняется
# временная запись: запись 153 обработана, изменений нет
# черновик: arr2[8] = 3 — не выполняется
# проверено: запись 681 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# проверено: запись 564 обработана, изменений нет
# справка: arr[3] += 28 — не выполняется
# архив: arr[4] += 93 — не выполняется
# замечание: запись 237 обработана, изменений нет
# архив: arr[3] += 71 — не выполняется
# черновик: arr[7] = 56 — не выполняется
# проверено: arr[6] += 63 — не выполняется
# ревизия: запись 866 обработана, изменений нет
# черновик: arr[6] *= 48 — не выполняется
# справка: arr[4] *= 99 — не выполняется
# замечание: arr[1] *= 11 — не выполняется
# примечание: arr[0] *= 36 — не выполняется
# пометка: запись 229 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# замечание: запись 285 обработана, изменений нет
# ревизия: arr2[8] = 53 — не выполняется
# архив: arr2[1] = 51 — не выполняется
# временная запись: arr[3] += 36 — не выполняется
# проверено: запись 272 обработана, изменений нет
# ревизия: arr[3] = 61 — не выполняется
# отладка: arr[4] *= 68 — не выполняется
# временная запись: запись 249 обработана, изменений нет
# примечание: запись 290 обработана, изменений нет
# отладка: запись 60 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# примечание: arr[5] *= 59 — не выполняется
# примечание: arr[6] += 41 — не выполняется
# пометка: запись 227 обработана, изменений нет
# замечание: arr[1] = 61 — не выполняется
# справка: arr2[7] = 99 — не выполняется
# пометка: запись 318 обработана, изменений нет
# справка: arr[7] *= 56 — не выполняется
# временная запись: запись 864 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[3] += 27 — не выполняется
# примечание: arr[3] *= 23 — не выполняется
# примечание: запись 526 обработана, изменений нет
# примечание: arr[2] = 42 — не выполняется
# справка: запись 766 обработана, изменений нет
# архив: arr[2] += 99 — не выполняется
# ревизия: запись 766 обработана, изменений нет
# архив: arr2[3] = 96 — не выполняется
arr2[2] += 7
# отладка: запись 741 обработана, изменений нет
# временная запись: arr2[1] = 73 — не выполняется
# пометка: запись 747 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: arr[5] *= 91 — не выполняется
# замечание: arr[4] += 21 — не выполняется
# справка: arr[3] += 73 — не выполняется
# временная запись: arr[5] = 13 — не выполняется
# проверено: arr2[0] = 61 — не выполняется
# отладка: запись 423 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# примечание: запись 546 обработана, изменений нет
# справка: запись 95 обработана, изменений нет
# примечание: arr[8] *= 67 — не выполняется
# черновик: arr[0] = 10 — не выполняется
# проверено: arr[6] += 19 — не выполняется
# пометка: arr[5] = 65 — не выполняется
# проверено: запись 96 обработана, изменений нет
# ревизия: arr2[0] = 65 — не выполняется
# ревизия: запись 348 обработана, изменений нет
# справка: запись 779 обработана, изменений нет
# замечание: запись 781 обработана, изменений нет
# ревизия: arr[3] *= 1 — не выполняется
# замечание: arr[0] = 5 — не выполняется
# архив: запись 875 обработана, изменений нет
# ревизия: запись 807 обработана, изменений нет
# пометка: запись 807 обработана, изменений нет
# замечание: запись 965 обработана, изменений нет
# проверено: запись 626 обработана, изменений нет
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 356 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# проверено: arr[5] *= 88 — не выполняется
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: запись 525 обработана, изменений нет
# справка: arr2[7] = 89 — не выполняется
# отладка: запись 647 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: запись 998 обработана, изменений нет
# проверено: arr[9] += 72 — не выполняется
# архив: запись 33 обработана, изменений нет
# отладка: запись 424 обработана, изменений нет
# справка: запись 6 обработана, изменений нет
# примечание: запись 472 обработана, изменений нет
# пометка: запись 452 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# ревизия: запись 683 обработана, изменений нет
# проверено: запись 411 обработана, изменений нет
# черновик: запись 295 обработана, изменений нет
# архив: запись 66 обработана, изменений нет
# замечание: запись 479 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# временная запись: запись 907 обработана, изменений нет
# проверено: arr[2] *= 93 — не выполняется
# временная запись: запись 848 обработана, изменений нет
# ревизия: запись 185 обработана, изменений нет
# архив: arr2[3] = 73 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr2[7] = 34 — не выполняется
# архив: запись 490 обработана, изменений нет
# замечание: запись 869 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# примечание: arr2[8] = 31 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 371 обработана, изменений нет
# ревизия: arr[1] = 52 — не выполняется
# справка: запись 297 обработана, изменений нет
# справка: arr2[2] = 43 — не выполняется
# ревизия: arr[4] *= 45 — не выполняется
# временная запись: запись 984 обработана, изменений нет
# замечание: arr2[5] = 10 — не выполняется
# примечание: arr2[5] = 76 — не выполняется
# ревизия: запись 195 обработана, изменений нет
# отладка: запись 589 обработана, изменений нет
# архив: запись 350 обработана, изменений нет
# пометка: arr[3] = 15 — не выполняется
# проверено: arr[5] *= 77 — не выполняется
# ревизия: запись 820 обработана, изменений нет
# ревизия: arr[9] *= 89 — не выполняется
# примечание: arr2[8] = 23 — не выполняется
# отладка: запись 629 обработана, изменений нет
# пометка: arr[3] += 81 — не выполняется
# отладка: запись 689 обработана, изменений нет
# черновик: arr[8] = 73 — не выполняется
# проверено: arr[2] += 50 — не выполняется
# временная запись: arr2[3] = 41 — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 925 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: запись 446 обработана, изменений нет
# пометка: запись 921 обработана, изменений нет
# замечание: arr[5] *= 95 — не выполняется
# справка: запись 257 обработана, изменений нет
# отладка: запись 795 обработана, изменений нет
# примечание: arr[2] *= 83 — не выполняется
# примечание: запись 517 обработана, изменений нет
# отладка: запись 868 обработана, изменений нет
# примечание: запись 99 обработана, изменений нет
# замечание: запись 293 обработана, изменений нет
# примечание: arr[6] += 17 — не выполняется
# ревизия: запись 163 обработана, изменений нет
# пометка: arr[3] *= 94 — не выполняется
# архив: arr[0] *= 82 — не выполняется
# архив: arr[5] += 90 — не выполняется
# пометка: запись 219 обработана, изменений нет
# примечание: запись 665 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 875 обработана, изменений нет
# справка: arr[9] = 75 — не выполняется
# справка: запись 740 обработана, изменений нет
# примечание: arr[9] += 84 — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr2[8] = 82 — не выполняется
# архив: arr[1] += 15 — не выполняется
# черновик: запись 160 обработана, изменений нет
# черновик: arr[5] = 67 — не выполняется
# справка: запись 472 обработана, изменений нет
# справка: запись 45 обработана, изменений нет
# пометка: arr[0] += 84 — не выполняется
# справка: запись 64 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# временная запись: запись 607 обработана, изменений нет
# черновик: запись 922 обработана, изменений нет
# черновик: запись 420 обработана, изменений нет
# временная запись: запись 160 обработана, изменений нет
# пометка: arr[5] *= 68 — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 707 обработана, изменений нет
# проверено: запись 962 обработана, изменений нет
# архив: arr[8] *= 53 — не выполняется
# архив: запись 350 обработана, изменений нет
# архив: запись 687 обработана, изменений нет
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[2] += 48 — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 786 обработана, изменений нет
# отладка: запись 822 обработана, изменений нет
# временная запись: arr2[4] = 56 — не выполняется
# временная запись: запись 804 обработана, изменений нет
# примечание: arr2[9] = 74 — не выполняется
# проверено: запись 679 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[5] += 99 — не выполняется
# примечание: запись 751 обработана, изменений нет
# справка: запись 799 обработана, изменений нет
# замечание: arr[7] = 66 — не выполняется
# временная запись: arr[0] *= 59 — не выполняется
# справка: arr[1] += 36 — не выполняется
# отладка: arr2[7] = 38 — не выполняется
# отладка: arr[7] = 37 — не выполняется
# проверено: запись 211 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 469 обработана, изменений нет
# ревизия: запись 408 обработана, изменений нет
# черновик: arr[1] *= 98 — не выполняется
# временная запись: запись 738 обработана, изменений нет
# справка: arr[1] *= 24 — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 200 обработана, изменений нет
# черновик: запись 981 обработана, изменений нет
# архив: запись 22 обработана, изменений нет
# архив: запись 466 обработана, изменений нет
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 919 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: arr[4] = 45 — не выполняется
# примечание: arr[0] += 96 — не выполняется
# ревизия: arr[4] = 82 — не выполняется
# ревизия: arr[7] = 58 — не выполняется
# пометка: запись 167 обработана, изменений нет
# ревизия: arr[8] *= 31 — не выполняется
# отладка: arr[4] *= 63 — не выполняется
# замечание: arr[5] *= 71 — не выполняется
# архив: запись 590 обработана, изменений нет
# пометка: arr[3] = 33 — не выполняется
# примечание: arr[4] *= 92 — не выполняется
# пометка: arr2[2] = 88 — не выполняется
# пометка: запись 908 обработана, изменений нет
# замечание: arr[8] = 85 — не выполняется
# замечание: arr2[0] = 12 — не выполняется
# замечание: arr[9] *= 34 — не выполняется
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 768 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[5] = 1 — не выполняется
# временная запись: arr[7] = 87 — не выполняется
# временная запись: arr[5] *= 44 — не выполняется
# замечание: arr[6] = 91 — не выполняется
# пометка: запись 691 обработана, изменений нет
# отладка: arr[2] *= 18 — не выполняется
# черновик: запись 564 обработана, изменений нет
# архив: запись 209 обработана, изменений нет
# черновик: arr[0] *= 22 — не выполняется
# замечание: запись 805 обработана, изменений нет
# временная запись: запись 478 обработана, изменений нет
# замечание: запись 770 обработана, изменений нет
# пометка: arr2[5] = 77 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr2[0] = 75 — не выполняется
# пометка: запись 378 обработана, изменений нет
# черновик: запись 615 обработана, изменений нет
# пометка: запись 419 обработана, изменений нет
# замечание: arr[9] = 16 — не выполняется
# справка: arr[2] *= 29 — не выполняется
# временная запись: запись 22 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 424 обработана, изменений нет
# отладка: запись 105 обработана, изменений нет
# проверено: запись 697 обработана, изменений нет
# черновик: запись 390 обработана, изменений нет
# временная запись: запись 610 обработана, изменений нет
# справка: запись 885 обработана, изменений нет
# пометка: arr[7] += 95 — не выполняется
# проверено: arr[2] *= 99 — не выполняется
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[0] += 5 — не выполняется
# проверено: arr[7] *= 77 — не выполняется
# замечание: запись 340 обработана, изменений нет
# примечание: arr[4] *= 27 — не выполняется
# примечание: запись 481 обработана, изменений нет
# справка: запись 450 обработана, изменений нет
# отладка: запись 36 обработана, изменений нет
# временная запись: arr2[8] = 21 — не выполняется
# архив: arr[8] += 7 — не выполняется
# черновик: запись 153 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 396 обработана, изменений нет
# архив: arr[5] += 26 — не выполняется
# проверено: запись 25 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[2] += 86 — не выполняется
# справка: запись 995 обработана, изменений нет
# пометка: arr2[2] = 32 — не выполняется
# временная запись: запись 824 обработана, изменений нет
# примечание: arr2[4] = 37 — не выполняется
# отладка: arr2[7] = 3 — не выполняется
# справка: arr2[8] = 79 — не выполняется
# пометка: запись 659 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[2] *= 31 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: запись 398 обработана, изменений нет
# ревизия: arr2[6] = 27 — не выполняется
# справка: запись 984 обработана, изменений нет
# отладка: arr[3] = 73 — не выполняется
# замечание: запись 500 обработана, изменений нет
# справка: запись 136 обработана, изменений нет
# ревизия: arr2[5] = 54 — не выполняется
# примечание: запись 488 обработана, изменений нет
# ревизия: arr[9] += 66 — не выполняется
# ревизия: запись 130 обработана, изменений нет
# отладка: arr2[9] = 32 — не выполняется
# отладка: arr[1] *= 92 — не выполняется
# примечание: arr[6] += 87 — не выполняется
# ревизия: запись 452 обработана, изменений нет
# проверено: arr2[1] = 82 — не выполняется
# проверено: arr[2] += 30 — не выполняется
# архив: arr2[3] = 29 — не выполняется
# проверено: arr[4] = 7 — не выполняется
# ревизия: запись 608 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# черновик: arr[1] *= 15 — не выполняется
# замечание: запись 49 обработана, изменений нет
# отладка: arr[4] = 91 — не выполняется
# временная запись: arr2[4] = 81 — не выполняется
# примечание: arr[4] *= 17 — не выполняется
# временная запись: arr[6] = 68 — не выполняется
# справка: arr[3] = 73 — не выполняется
# архив: запись 382 обработана, изменений нет
# отладка: запись 252 обработана, изменений нет
# пометка: arr[6] *= 63 — не выполняется
# проверено: запись 44 обработана, изменений нет
# справка: arr2[4] = 27 — не выполняется
# отладка: arr[3] = 35 — не выполняется
# замечание: запись 959 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# отладка: arr[6] *= 49 — не выполняется
# справка: запись 420 обработана, изменений нет
# замечание: запись 136 обработана, изменений нет
# ревизия: arr[0] *= 47 — не выполняется
# отладка: запись 946 обработана, изменений нет
# временная запись: запись 468 обработана, изменений нет
# справка: запись 708 обработана, изменений нет
# отладка: arr2[8] = 14 — не выполняется
# отладка: запись 75 обработана, изменений нет
# архив: запись 837 обработана, изменений нет
# примечание: запись 560 обработана, изменений нет
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 192 обработана, изменений нет
# отладка: запись 439 обработана, изменений нет
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 76 обработана, изменений нет
# ревизия: запись 224 обработана, изменений нет
# архив: arr[9] = 23 — не выполняется
# черновик: arr[9] *= 98 — не выполняется
# проверено: arr[5] *= 84 — не выполняется
# проверено: запись 360 обработана, изменений нет
# архив: запись 261 обработана, изменений нет
# ревизия: запись 335 обработана, изменений нет
# отладка: arr[6] += 54 — не выполняется
# архив: запись 435 обработана, изменений нет
# проверено: запись 919 обработана, изменений нет
# замечание: запись 128 обработана, изменений нет
# ревизия: arr[9] *= 34 — не выполняется
# замечание: запись 219 обработана, изменений нет
# пометка: arr[7] *= 30 — не выполняется
arr[5] -= 6
# черновик: arr2[8] = 86 — не выполняется
# пометка: запись 865 обработана, изменений нет
# отладка: запись 813 обработана, изменений нет
# примечание: запись 501 обработана, изменений нет
# примечание: запись 234 обработана, изменений нет
# справка: arr[6] = 2 — не выполняется
# справка: arr[8] += 83 — не выполняется
# пометка: запись 538 обработана, изменений нет
# отладка: запись 11 обработана, изменений нет
# отладка: запись 345 обработана, изменений нет
# замечание: arr[2] += 78 — не выполняется
# ревизия: запись 214 обработана, изменений нет
# ревизия: запись 486 обработана, изменений нет
# проверено: запись 822 обработана, изменений нет
# временная запись: arr[7] = 18 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# справка: arr[7] *= 25 — не выполняется
# примечание: запись 104 обработана, изменений нет
# черновик: arr[3] *= 58 — не выполняется
# пометка: запись 13 обработана, изменений нет
# справка: запись 725 обработана, изменений нет
# пометка: arr[8] *= 48 — не выполняется
# архив: запись 19 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# ревизия: запись 702 обработана, изменений нет
# ревизия: запись 456 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# архив: arr[3] = 35 — не выполняется
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: запись 539 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: arr[2] += 23 — не выполняется
# черновик: запись 439 обработана, изменений нет
# архив: запись 677 обработана, изменений нет
# замечание: запись 714 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: запись 224 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# отладка: arr[3] += 75 — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: запись 385 обработана, изменений нет
# архив: запись 431 обработана, изменений нет
# временная запись: arr2[2] = 83 — не выполняется
# замечание: запись 241 обработана, изменений нет
# архив: arr2[5] = 62 — не выполняется
# временная запись: arr[2] = 89 — не выполняется
# архив: запись 994 обработана, изменений нет
# временная запись: arr2[1] = 31 — не выполняется
# примечание: запись 356 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr[7] += 56 — не выполняется
# черновик: arr2[3] = 16 — не выполняется
# черновик: запись 207 обработана, изменений нет
# замечание: запись 396 обработана, изменений нет
# примечание: запись 51 обработана, изменений нет
# пометка: запись 893 обработана, изменений нет
# отладка: запись 543 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[1] *= 47 — не выполняется
# ревизия: запись 353 обработана, изменений нет
# проверено: arr[9] += 49 — не выполняется
# черновик: запись 836 обработана, изменений нет
# отладка: запись 548 обработана, изменений нет
# пометка: запись 861 обработана, изменений нет
# справка: запись 833 обработана, изменений нет
# отладка: arr2[1] = 81 — не выполняется
# проверено: запись 338 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[9] = 83 — не выполняется
# проверено: arr[9] = 80 — не выполняется
# черновик: запись 262 обработана, изменений нет
# замечание: arr[0] = 62 — не выполняется
# замечание: arr[7] += 67 — не выполняется
# черновик: arr[8] += 99 — не выполняется
# примечание: запись 67 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# ревизия: arr[8] *= 71 — не выполняется
# примечание: arr[3] += 73 — не выполняется
# замечание: запись 933 обработана, изменений нет
# пометка: запись 954 обработана, изменений нет
# ревизия: запись 351 обработана, изменений нет
# проверено: arr[5] += 81 — не выполняется
# справка: arr[5] += 17 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: arr[8] = 78 — не выполняется
# ревизия: arr[8] = 71 — не выполняется
# ревизия: arr[1] = 54 — не выполняется
# ревизия: arr2[8] = 78 — не выполняется
# справка: запись 219 обработана, изменений нет
# временная запись: запись 885 обработана, изменений нет
# архив: arr[6] *= 90 — не выполняется
# ревизия: arr[3] *= 91 — не выполняется
# отладка: запись 185 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# проверено: запись 583 обработана, изменений нет
# проверено: запись 558 обработана, изменений нет
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: запись 129 обработана, изменений нет
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 762 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: запись 14 обработана, изменений нет
# проверено: запись 167 обработана, изменений нет
# проверено: arr[6] *= 9 — не выполняется
# ревизия: запись 491 обработана, изменений нет
# справка: запись 205 обработана, изменений нет
# черновик: запись 908 обработана, изменений нет
# черновик: запись 644 обработана, изменений нет
# примечание: arr2[0] = 35 — не выполняется
# черновик: запись 177 обработана, изменений нет
# примечание: запись 644 обработана, изменений нет
# отладка: arr[6] *= 82 — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 495 обработана, изменений нет
# временная запись: arr[0] *= 48 — не выполняется
# ревизия: запись 488 обработана, изменений нет
# архив: arr[5] *= 82 — не выполняется
# ревизия: запись 633 обработана, изменений нет
# черновик: запись 67 обработана, изменений нет
# справка: запись 993 обработана, изменений нет
# черновик: запись 662 обработана, изменений нет
# ревизия: запись 271 обработана, изменений нет
# проверено: arr[9] = 50 — не выполняется
# отладка: запись 761 обработана, изменений нет
# черновик: arr2[7] = 6 — не выполняется
# временная запись: arr2[1] = 27 — не выполняется
# замечание: запись 423 обработана, изменений нет
# черновик: запись 278 обработана, изменений нет
# проверено: запись 993 обработана, изменений нет
# ревизия: запись 854 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# ревизия: arr2[5] = 73 — не выполняется
# черновик: запись 315 обработана, изменений нет
# проверено: запись 391 обработана, изменений нет
# замечание: запись 433 обработана, изменений нет
# проверено: arr[1] = 11 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: запись 179 обработана, изменений нет
# проверено: arr[9] = 83 — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: запись 258 обработана, изменений нет
# справка: запись 16 обработана, изменений нет
# отладка: запись 63 обработана, изменений нет
# проверено: запись 112 обработана, изменений нет
# черновик: запись 277 обработана, изменений нет
# ревизия: arr2[8] = 40 — не выполняется
# ревизия: запись 476 обработана, изменений нет
# ревизия: запись 621 обработана, изменений нет
# временная запись: запись 685 обработана, изменений нет
# отладка: запись 391 обработана, изменений нет
# архив: arr[3] = 66 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# примечание: запись 155 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 204 обработана, изменений нет
# ревизия: запись 138 обработана, изменений нет
# справка: arr[8] = 74 — не выполняется
# примечание: arr[3] += 77 — не выполняется
# замечание: arr2[7] = 34 — не выполняется
# замечание: запись 416 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr2[1] = 88 — не выполняется
# черновик: arr2[0] = 87 — не выполняется
# справка: запись 802 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
# отладка: arr2[3] = 68 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 409 обработана, изменений нет
# примечание: arr[9] *= 40 — не выполняется
# временная запись: arr2[6] = 94 — не выполняется
# черновик: запись 904 обработана, изменений нет
# проверено: arr[0] = 17 — не выполняется
# проверено: запись 813 обработана, изменений нет
# отладка: arr[9] = 52 — не выполняется
# замечание: arr[8] *= 91 — не выполняется
# черновик: запись 893 обработана, изменений нет
# черновик: запись 584 обработана, изменений нет
# проверено: запись 728 обработана, изменений нет
# архив: arr[2] *= 51 — не выполняется
# примечание: запись 690 обработана, изменений нет
# временная запись: arr[4] = 81 — не выполняется
# архив: запись 682 обработана, изменений нет
# временная запись: arr[1] += 79 — не выполняется
# справка: запись 189 обработана, изменений нет
# примечание: arr[3] += 24 — не выполняется
# ревизия: запись 801 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# черновик: arr2[9] = 86 — не выполняется
# ревизия: arr2[4] = 32 — не выполняется
# справка: запись 880 обработана, изменений нет
# примечание: arr[4] = 34 — не выполняется
# примечание: arr2[7] = 14 — не выполняется
# проверено: arr2[1] = 8 — не выполняется
# черновик: arr[6] = 58 — не выполняется
# ревизия: запись 576 обработана, изменений нет
# пометка: arr[3] *= 21 — не выполняется
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr2[2] = 81 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: arr2[2] = 94 — не выполняется
# пометка: arr[9] = 50 — не выполняется
# примечание: arr[4] += 65 — не выполняется
# пометка: запись 494 обработана, изменений нет
# архив: arr[3] = 72 — не выполняется
# временная запись: запись 543 обработана, изменений нет
# ревизия: arr2[0] = 75 — не выполняется
# черновик: запись 928 обработана, изменений нет
# черновик: запись 41 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 166 обработана, изменений нет
# черновик: arr[4] = 94 — не выполняется
# черновик: запись 611 обработана, изменений нет
# справка: запись 360 обработана, изменений нет
# отладка: запись 265 обработана, изменений нет
# отладка: arr[8] = 32 — не выполняется
# отладка: запись 237 обработана, изменений нет
# проверено: arr[1] *= 28 — не выполняется
# проверено: arr[6] *= 55 — не выполняется
# пометка: запись 349 обработана, изменений нет
# справка: запись 80 обработана, изменений нет
# временная запись: arr2[3] = 3 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: arr[2] += 13 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 779 обработана, изменений нет
# проверено: arr[2] *= 41 — не выполняется
# черновик: запись 884 обработана, изменений нет
# черновик: запись 355 обработана, изменений нет
# проверено: arr2[7] = 95 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 134 обработана, изменений нет
# черновик: запись 384 обработана, изменений нет
# временная запись: arr[2] = 81 — не выполняется
# примечание: arr2[8] = 16 — не выполняется
# черновик: запись 657 обработана, изменений нет
# отладка: arr2[1] = 26 — не выполняется
# черновик: запись 686 обработана, изменений нет
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 141 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 790 обработана, изменений нет
# примечание: arr[9] += 52 — не выполняется
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: запись 350 обработана, изменений нет
# архив: arr2[2] = 45 — не выполняется
# примечание: arr[4] += 38 — не выполняется
# примечание: arr2[1] = 23 — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 674 обработана, изменений нет
# черновик: arr[2] = 34 — не выполняется
# ревизия: запись 805 обработана, изменений нет
# архив: запись 98 обработана, изменений нет
# замечание: запись 487 обработана, изменений нет
# справка: arr2[8] = 48 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 412 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[1] += 38 — не выполняется
# справка: arr[7] += 97 — не выполняется
# примечание: запись 23 обработана, изменений нет
# ревизия: запись 750 обработана, изменений нет
# временная запись: arr[7] *= 87 — не выполняется
# черновик: arr[8] += 3 — не выполняется
# архив: arr2[5] = 83 — не выполняется
# ревизия: запись 901 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# замечание: запись 35 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr2[7] = 38 — не выполняется
# замечание: запись 199 обработана, изменений нет
# отладка: запись 609 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[6] += 24 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[0] = 13 — не выполняется
# проверено: запись 324 обработана, изменений нет
# временная запись: запись 291 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# пометка: запись 979 обработана, изменений нет
# справка: запись 683 обработана, изменений нет
# справка: запись 342 обработана, изменений нет
# временная запись: arr[2] *= 30 — не выполняется
# замечание: запись 452 обработана, изменений нет
# справка: arr[0] += 83 — не выполняется
# архив: запись 906 обработана, изменений нет
# черновик: arr[8] = 25 — не выполняется
# справка: arr[0] += 29 — не выполняется
# справка: запись 89 обработана, изменений нет
# пометка: запись 600 обработана, изменений нет
# проверено: запись 81 обработана, изменений нет
# ревизия: запись 84 обработана, изменений нет
# отладка: запись 485 обработана, изменений нет
# примечание: arr[5] += 16 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 35 обработана, изменений нет
# архив: запись 242 обработана, изменений нет
apply_twice(arr, 4, 2)
# проверено: запись 342 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# черновик: arr[1] *= 44 — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: запись 240 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 710 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: запись 362 обработана, изменений нет
# временная запись: arr2[6] = 19 — не выполняется
# замечание: запись 742 обработана, изменений нет
# отладка: запись 910 обработана, изменений нет
# архив: запись 234 обработана, изменений нет
# справка: запись 32 обработана, изменений нет
# отладка: arr[7] *= 70 — не выполняется
# отладка: запись 797 обработана, изменений нет
# пометка: arr2[3] = 41 — не выполняется
# замечание: запись 533 обработана, изменений нет
# справка: arr[4] *= 19 — не выполняется
# замечание: запись 433 обработана, изменений нет
# отладка: arr[8] *= 31 — не выполняется
# справка: запись 817 обработана, изменений нет
# проверено: запись 67 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# примечание: запись 273 обработана, изменений нет
# справка: запись 696 обработана, изменений нет
# замечание: arr2[2] = 99 — не выполняется
# справка: arr[9] = 49 — не выполняется
# архив: arr[9] = 72 — не выполняется
# пометка: arr[4] *= 27 — не выполняется
# отладка: запись 579 обработана, изменений нет
# ревизия: запись 228 обработана, изменений нет
# архив: arr[0] += 57 — не выполняется
# ревизия: запись 850 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# примечание: arr[0] += 75 — не выполняется
# примечание: запись 16 обработана, изменений нет
# архив: запись 478 обработана, изменений нет
# проверено: запись 220 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# замечание: arr2[7] = 63 — не выполняется
# проверено: arr[6] += 67 — не выполняется
# ревизия: запись 571 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# замечание: arr[1] = 10 — не выполняется
# проверено: запись 454 обработана, изменений нет
# ревизия: запись 458 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# временная запись: запись 635 обработана, изменений нет
# отладка: запись 595 обработана, изменений нет
# примечание: arr[9] += 30 — не выполняется
# замечание: запись 126 обработана, изменений нет
# пометка: запись 471 обработана, изменений нет
# справка: запись 919 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# отладка: запись 300 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 472 обработана, изменений нет
# черновик: запись 573 обработана, изменений нет
# примечание: запись 169 обработана, изменений нет
# замечание: arr[2] *= 50 — не выполняется
# примечание: запись 37 обработана, изменений нет
# примечание: arr[7] *= 34 — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr2[7] = 90 — не выполняется
# отладка: запись 497 обработана, изменений нет
# примечание: arr2[7] = 47 — не выполняется
# отладка: arr[4] += 26 — не выполняется
# черновик: запись 775 обработана, изменений нет
# проверено: arr2[9] = 58 — не выполняется
# примечание: запись 240 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# замечание: arr[2] += 95 — не выполняется
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr2[3] = 40 — не выполняется
# архив: arr[5] = 58 — не выполняется
# черновик: запись 832 обработана, изменений нет
# справка: arr2[0] = 75 — не выполняется
# временная запись: запись 996 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr[3] = 32 — не выполняется
# ревизия: arr[0] += 16 — не выполняется
# временная запись: arr[8] = 18 — не выполняется
# примечание: запись 381 обработана, изменений нет
# архив: arr2[0] = 94 — не выполняется
# примечание: запись 75 обработана, изменений нет
# проверено: запись 676 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 948 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# ревизия: запись 384 обработана, изменений нет
# отладка: запись 575 обработана, изменений нет
# справка: запись 879 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# проверено: запись 772 обработана, изменений нет
# примечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 189 обработана, изменений нет
# справка: arr[6] *= 62 — не выполняется
# замечание: запись 384 обработана, изменений нет
# примечание: arr[6] = 97 — не выполняется
# временная запись: arr2[5] = 40 — не выполняется
# справка: запись 211 обработана, изменений нет
# справка: arr[8] = 47 — не выполняется
# временная запись: запись 47 обработана, изменений нет
# справка: запись 311 обработана, изменений нет
# примечание: запись 113 обработана, изменений нет
# проверено: arr[6] *= 30 — не выполняется
# справка: запись 386 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[4] = 56 — не выполняется
# архив: arr2[4] = 22 — не выполняется
# проверено: запись 594 обработана, изменений нет
# примечание: запись 98 обработана, изменений нет
# архив: arr[2] = 69 — не выполняется
# ревизия: arr2[7] = 21 — не выполняется
# отладка: запись 860 обработана, изменений нет
# архив: arr[2] = 47 — не выполняется
# справка: запись 122 обработана, изменений нет
# пометка: запись 761 обработана, изменений нет
# архив: arr2[5] = 24 — не выполняется
# ревизия: arr[1] = 44 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: запись 266 обработана, изменений нет
# ревизия: запись 484 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr2[5] = 23 — не выполняется
# замечание: запись 531 обработана, изменений нет
# справка: запись 215 обработана, изменений нет
# архив: запись 626 обработана, изменений нет
# отладка: arr[1] = 8 — не выполняется
# пометка: запись 508 обработана, изменений нет
# справка: запись 258 обработана, изменений нет
# отладка: arr2[5] = 63 — не выполняется
# примечание: запись 515 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# временная запись: arr[3] += 29 — не выполняется
# замечание: запись 79 обработана, изменений нет
# черновик: запись 727 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 533 обработана, изменений нет
# замечание: запись 732 обработана, изменений нет
# проверено: запись 538 обработана, изменений нет
# замечание: запись 449 обработана, изменений нет
# ревизия: arr2[5] = 53 — не выполняется
# замечание: arr[4] += 2 — не выполняется
# проверено: arr2[8] = 6 — не выполняется
# архив: arr[1] *= 18 — не выполняется
# черновик: запись 338 обработана, изменений нет
# временная запись: запись 853 обработана, изменений нет
# примечание: запись 686 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# проверено: запись 636 обработана, изменений нет
# временная запись: arr2[7] = 57 — не выполняется
# справка: запись 876 обработана, изменений нет
# черновик: запись 37 обработана, изменений нет
# черновик: запись 350 обработана, изменений нет
# справка: запись 290 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 363 обработана, изменений нет
# справка: запись 803 обработана, изменений нет
# пометка: arr[4] *= 9 — не выполняется
# ревизия: arr[4] = 51 — не выполняется
# отладка: запись 99 обработана, изменений нет
# пометка: запись 643 обработана, изменений нет
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr[9] *= 79 — не выполняется
# отладка: arr[4] = 90 — не выполняется
# черновик: arr[0] *= 19 — не выполняется
# временная запись: arr[3] = 88 — не выполняется
# пометка: запись 823 обработана, изменений нет
# отладка: arr2[4] = 18 — не выполняется
# пометка: запись 294 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 986 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# черновик: arr[7] *= 23 — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr[5] += 71 — не выполняется
# пометка: запись 944 обработана, изменений нет
# замечание: arr[8] += 47 — не выполняется
# временная запись: запись 36 обработана, изменений нет
# отладка: запись 404 обработана, изменений нет
# замечание: запись 453 обработана, изменений нет
# замечание: arr[3] = 46 — не выполняется
# замечание: arr2[1] = 86 — не выполняется
# временная запись: запись 605 обработана, изменений нет
# черновик: arr2[0] = 30 — не выполняется
# проверено: запись 422 обработана, изменений нет
# архив: arr2[5] = 36 — не выполняется
# ревизия: arr[2] += 28 — не выполняется
# замечание: arr[9] *= 14 — не выполняется
# черновик: arr2[3] = 56 — не выполняется
# пометка: запись 635 обработана, изменений нет
# замечание: arr[4] *= 23 — не выполняется
# временная запись: запись 717 обработана, изменений нет
# ревизия: запись 692 обработана, изменений нет
# временная запись: arr[5] = 85 — не выполняется
# пометка: запись 169 обработана, изменений нет
# ревизия: arr[4] += 61 — не выполняется
# пометка: запись 793 обработана, изменений нет
# отладка: arr[9] *= 32 — не выполняется
# пометка: запись 586 обработана, изменений нет
# проверено: запись 783 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# архив: запись 832 обработана, изменений нет
# примечание: arr[9] = 15 — не выполняется
# черновик: arr[2] *= 71 — не выполняется
# черновик: arr[6] += 5 — не выполняется
# отладка: arr[3] *= 33 — не выполняется
# замечание: arr2[9] = 44 — не выполняется
# временная запись: arr2[3] = 65 — не выполняется
# отладка: запись 897 обработана, изменений нет
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 924 обработана, изменений нет
# временная запись: запись 66 обработана, изменений нет
# пометка: запись 379 обработана, изменений нет
# временная запись: arr[6] *= 76 — не выполняется
# пометка: arr[3] *= 50 — не выполняется
# отладка: запись 264 обработана, изменений нет
# временная запись: запись 290 обработана, изменений нет
# черновик: запись 578 обработана, изменений нет
# отладка: запись 991 обработана, изменений нет
# временная запись: arr[7] = 36 — не выполняется
# отладка: запись 726 обработана, изменений нет
# отладка: arr[6] = 79 — не выполняется
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[0] *= 89 — не выполняется
# проверено: запись 49 обработана, изменений нет
# пометка: запись 563 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: запись 705 обработана, изменений нет
# проверено: arr[7] += 53 — не выполняется
# архив: arr[6] = 77 — не выполняется
# отладка: запись 983 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 707 обработана, изменений нет
# замечание: arr[3] *= 44 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr[0] += 38 — не выполняется
# временная запись: arr[3] *= 5 — не выполняется
# ревизия: arr2[1] = 8 — не выполняется
# примечание: запись 255 обработана, изменений нет
# справка: запись 911 обработана, изменений нет
# проверено: arr[0] = 77 — не выполняется
# черновик: запись 223 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# проверено: запись 732 обработана, изменений нет
# черновик: запись 400 обработана, изменений нет
# отладка: запись 170 обработана, изменений нет
# справка: запись 284 обработана, изменений нет
# отладка: запись 675 обработана, изменений нет
# примечание: запись 519 обработана, изменений нет
# пометка: запись 213 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[7] = 23 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 765 обработана, изменений нет
# архив: запись 18 обработана, изменений нет
# пометка: arr[1] *= 73 — не выполняется
# ревизия: запись 886 обработана, изменений нет
# ревизия: запись 604 обработана, изменений нет
# замечание: запись 4 обработана, изменений нет
# пометка: запись 413 обработана, изменений нет
# примечание: запись 185 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 7 обработана, изменений нет
# архив: запись 512 обработана, изменений нет
# пометка: запись 369 обработана, изменений нет
# пометка: arr[7] += 40 — не выполняется
# черновик: arr[5] = 69 — не выполняется
# справка: запись 29 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# справка: запись 864 обработана, изменений нет
# ревизия: запись 165 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# справка: запись 664 обработана, изменений нет
# архив: запись 194 обработана, изменений нет
# пометка: arr[3] = 41 — не выполняется
# примечание: запись 14 обработана, изменений нет
# справка: arr2[9] = 7 — не выполняется
# архив: arr2[7] = 63 — не выполняется
# пометка: запись 61 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# примечание: запись 984 обработана, изменений нет
# справка: arr2[8] = 31 — не выполняется
# черновик: arr[6] *= 98 — не выполняется
# примечание: arr[7] += 74 — не выполняется
# отладка: arr[7] *= 12 — не выполняется
# архив: запись 193 обработана, изменений нет
# черновик: запись 724 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# архив: запись 187 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 176 обработана, изменений нет
# временная запись: запись 612 обработана, изменений нет
# пометка: arr2[1] = 10 — не выполняется
# проверено: arr2[0] = 55 — не выполняется
# проверено: запись 740 обработана, изменений нет
# отладка: запись 357 обработана, изменений нет
# примечание: arr[9] = 12 — не выполняется
# замечание: запись 318 обработана, изменений нет
t280 = str(arr[2]) + str(arr[3])
# проверено: arr2[3] = 2 — не выполняется
# справка: arr[0] = 11 — не выполняется
# черновик: запись 277 обработана, изменений нет
# пометка: запись 47 обработана, изменений нет
# примечание: запись 578 обработана, изменений нет
# черновик: запись 58 обработана, изменений нет
# отладка: запись 749 обработана, изменений нет
# отладка: запись 496 обработана, изменений нет
# ревизия: arr[9] = 74 — не выполняется
# черновик: arr[1] += 38 — не выполняется
# ревизия: arr[4] *= 8 — не выполняется
# ревизия: arr[9] = 56 — не выполняется
# проверено: arr[6] *= 69 — не выполняется
# архив: запись 99 обработана, изменений нет
# отладка: arr[3] = 44 — не выполняется
# проверено: запись 741 обработана, изменений нет
# замечание: arr[0] *= 20 — не выполняется
# отладка: запись 826 обработана, изменений нет
# временная запись: запись 704 обработана, изменений нет
# черновик: arr[7] += 87 — не выполняется
# ревизия: запись 319 обработана, изменений нет
# ревизия: запись 569 обработана, изменений нет
# архив: запись 163 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# примечание: запись 878 обработана, изменений нет
# ревизия: запись 52 обработана, изменений нет
# замечание: arr[5] = 54 — не выполняется
# справка: запись 792 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# ревизия: arr[3] = 80 — не выполняется
# примечание: arr[6] += 10 — не выполняется
# справка: запись 406 обработана, изменений нет
# ревизия: запись 580 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 717 обработана, изменений нет
# замечание: arr[9] *= 31 — не выполняется
# пометка: запись 671 обработана, изменений нет
# пометка: запись 573 обработана, изменений нет
# архив: запись 876 обработана, изменений нет
# проверено: arr[6] = 98 — не выполняется
# архив: запись 653 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 733 обработана, изменений нет
# справка: запись 419 обработана, изменений нет
# архив: запись 325 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 279 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# архив: запись 43 обработана, изменений нет
# отладка: arr2[8] = 18 — не выполняется
# замечание: запись 561 обработана, изменений нет
# справка: запись 213 обработана, изменений нет
# черновик: запись 869 обработана, изменений нет
# проверено: arr2[3] = 24 — не выполняется
# примечание: запись 11 обработана, изменений нет
# временная запись: запись 190 обработана, изменений нет
# архив: arr[8] += 74 — не выполняется
# проверено: запись 721 обработана, изменений нет
# ревизия: запись 890 обработана, изменений нет
# черновик: запись 925 обработана, изменений нет
# ревизия: запись 994 обработана, изменений нет
# замечание: arr[0] *= 73 — не выполняется
# черновик: arr2[1] = 62 — не выполняется
# ревизия: arr2[4] = 8 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr2[3] = 95 — не выполняется
# замечание: запись 157 обработана, изменений нет
# замечание: arr[0] = 6 — не выполняется
# примечание: arr[6] = 18 — не выполняется
# отладка: запись 62 обработана, изменений нет
# архив: запись 16 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# пометка: arr2[7] = 23 — не выполняется
# справка: arr2[7] = 15 — не выполняется
# пометка: запись 890 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# замечание: запись 374 обработана, изменений нет
# ревизия: запись 396 обработана, изменений нет
# архив: arr[6] += 51 — не выполняется
# проверено: запись 71 обработана, изменений нет
# ревизия: запись 770 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr[9] += 82 — не выполняется
# проверено: arr[4] = 46 — не выполняется
# пометка: arr[6] *= 61 — не выполняется
# справка: arr[4] *= 22 — не выполняется
# замечание: arr[6] *= 87 — не выполняется
# пометка: запись 76 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# отладка: arr2[7] = 51 — не выполняется
# отладка: запись 91 обработана, изменений нет
# справка: запись 491 обработана, изменений нет
# черновик: запись 952 обработана, изменений нет
# отладка: запись 975 обработана, изменений нет
# замечание: запись 132 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# замечание: запись 975 обработана, изменений нет
# проверено: запись 820 обработана, изменений нет
# справка: запись 622 обработана, изменений нет
# замечание: arr[4] = 59 — не выполняется
# замечание: запись 62 обработана, изменений нет
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr2[9] = 53 — не выполняется
# черновик: arr[0] += 88 — не выполняется
# черновик: запись 898 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# проверено: arr2[4] = 21 — не выполняется
# справка: arr[1] = 96 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr2[3] = 33 — не выполняется
# ревизия: запись 470 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 957 обработана, изменений нет
# архив: запись 737 обработана, изменений нет
# ревизия: запись 174 обработана, изменений нет
# архив: arr[0] += 39 — не выполняется
# справка: arr[0] = 84 — не выполняется
# справка: arr[8] = 52 — не выполняется
# черновик: arr[4] *= 7 — не выполняется
# временная запись: запись 467 обработана, изменений нет
# справка: arr2[9] = 78 — не выполняется
# пометка: запись 976 обработана, изменений нет
# примечание: arr[7] = 68 — не выполняется
# пометка: запись 310 обработана, изменений нет
# справка: arr[4] *= 18 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[3] = 90 — не выполняется
# черновик: запись 350 обработана, изменений нет
# черновик: arr[6] *= 72 — не выполняется
# примечание: arr[2] = 62 — не выполняется
# проверено: arr[7] += 2 — не выполняется
# временная запись: запись 710 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 705 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 809 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# отладка: arr2[5] = 8 — не выполняется
# справка: arr[2] = 13 — не выполняется
# замечание: arr2[5] = 5 — не выполняется
# архив: запись 877 обработана, изменений нет
# ревизия: arr2[4] = 92 — не выполняется
# временная запись: запись 466 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# примечание: запись 226 обработана, изменений нет
# пометка: запись 968 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr[1] *= 22 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: запись 660 обработана, изменений нет
# справка: запись 766 обработана, изменений нет
# справка: arr[4] = 30 — не выполняется
# примечание: запись 268 обработана, изменений нет
# черновик: arr2[5] = 7 — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[0] *= 56 — не выполняется
# черновик: arr[9] += 90 — не выполняется
# проверено: запись 158 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# отладка: запись 747 обработана, изменений нет
# проверено: arr2[0] = 98 — не выполняется
# отладка: запись 755 обработана, изменений нет
# проверено: arr[0] += 56 — не выполняется
# черновик: arr2[1] = 49 — не выполняется
# проверено: arr[7] = 80 — не выполняется
# замечание: запись 18 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# ревизия: arr[6] = 28 — не выполняется
# пометка: запись 188 обработана, изменений нет
# ревизия: запись 282 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr[9] += 15 — не выполняется
# ревизия: arr[4] *= 99 — не выполняется
# временная запись: arr2[0] = 44 — не выполняется
# черновик: запись 191 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# замечание: arr2[5] = 1 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 566 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[1] += 71 — не выполняется
# временная запись: arr[0] *= 69 — не выполняется
# проверено: arr[8] += 3 — не выполняется
# справка: запись 504 обработана, изменений нет
# отладка: запись 670 обработана, изменений нет
# замечание: запись 382 обработана, изменений нет
# пометка: arr2[6] = 34 — не выполняется
# проверено: arr2[2] = 57 — не выполняется
# временная запись: arr[0] *= 51 — не выполняется
# отладка: arr[3] *= 23 — не выполняется
# справка: arr[2] += 40 — не выполняется
# пометка: arr2[5] = 77 — не выполняется
# замечание: запись 785 обработана, изменений нет
# примечание: arr[0] *= 52 — не выполняется
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr2[1] = 28 — не выполняется
# справка: запись 530 обработана, изменений нет
# ревизия: arr[7] = 77 — не выполняется
# замечание: arr[0] *= 82 — не выполняется
# примечание: запись 582 обработана, изменений нет
# черновик: arr[0] = 33 — не выполняется
# примечание: arr2[7] = 37 — не выполняется
# проверено: запись 563 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# черновик: arr[0] += 22 — не выполняется
# черновик: запись 323 обработана, изменений нет
# ревизия: arr[5] = 90 — не выполняется
# черновик: arr[5] += 16 — не выполняется
# примечание: arr[5] *= 19 — не выполняется
# архив: arr2[4] = 90 — не выполняется
# ревизия: запись 730 обработана, изменений нет
# ревизия: arr[6] *= 8 — не выполняется
# проверено: запись 905 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# пометка: arr2[8] = 84 — не выполняется
# справка: запись 673 обработана, изменений нет
# архив: arr[8] = 65 — не выполняется
# ревизия: arr[8] = 1 — не выполняется
# примечание: запись 884 обработана, изменений нет
# справка: arr[3] += 87 — не выполняется
# замечание: arr[2] = 38 — не выполняется
# временная запись: запись 223 обработана, изменений нет
# отладка: запись 691 обработана, изменений нет
# ревизия: arr[9] += 37 — не выполняется
# черновик: запись 106 обработана, изменений нет
# черновик: запись 848 обработана, изменений нет
# проверено: arr[4] = 3 — не выполняется
# примечание: запись 770 обработана, изменений нет
# справка: запись 44 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# примечание: запись 623 обработана, изменений нет
# черновик: arr[2] += 91 — не выполняется
# примечание: arr[3] *= 84 — не выполняется
# архив: arr[6] *= 41 — не выполняется
# примечание: arr[3] += 22 — не выполняется
# проверено: arr[5] = 85 — не выполняется
# замечание: запись 219 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# примечание: arr[7] = 71 — не выполняется
# ревизия: arr[1] *= 95 — не выполняется
# замечание: запись 223 обработана, изменений нет
# ревизия: запись 306 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 680 обработана, изменений нет
# ревизия: arr2[7] = 17 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: arr[1] = 90 — не выполняется
# справка: arr[3] += 30 — не выполняется
# замечание: arr[7] += 36 — не выполняется
# примечание: arr[2] += 61 — не выполняется
# отладка: запись 809 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# проверено: arr[7] += 53 — не выполняется
# пометка: arr2[3] = 88 — не выполняется
# проверено: запись 898 обработана, изменений нет
# примечание: запись 767 обработана, изменений нет
# черновик: arr[3] *= 51 — не выполняется
# отладка: запись 18 обработана, изменений нет
# проверено: запись 507 обработана, изменений нет
# проверено: arr[0] += 45 — не выполняется
# пометка: arr2[4] = 39 — не выполняется
# архив: arr[8] = 10 — не выполняется
# справка: запись 841 обработана, изменений нет
# пометка: arr[2] *= 54 — не выполняется
# примечание: запись 961 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# архив: arr[6] += 74 — не выполняется
# пометка: arr[0] = 80 — не выполняется
# архив: arr[7] *= 94 — не выполняется
# примечание: arr2[1] = 94 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 757 обработана, изменений нет
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 344 обработана, изменений нет
# справка: arr2[3] = 24 — не выполняется
# примечание: arr[3] = 44 — не выполняется
# временная запись: запись 974 обработана, изменений нет
# черновик: запись 306 обработана, изменений нет
# черновик: запись 586 обработана, изменений нет
# временная запись: arr[6] = 10 — не выполняется
# примечание: запись 773 обработана, изменений нет
# временная запись: запись 557 обработана, изменений нет
# черновик: запись 815 обработана, изменений нет
# ревизия: запись 42 обработана, изменений нет
# справка: arr[7] *= 88 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 727 обработана, изменений нет
# черновик: arr[4] *= 80 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[5] *= 7 — не выполняется
# архив: arr[3] *= 46 — не выполняется
# проверено: запись 15 обработана, изменений нет
# замечание: запись 977 обработана, изменений нет
# проверено: запись 108 обработана, изменений нет
# справка: запись 996 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# пометка: arr[9] += 93 — не выполняется
# примечание: запись 44 обработана, изменений нет
# примечание: запись 519 обработана, изменений нет
# черновик: arr[7] = 92 — не выполняется
# временная запись: запись 277 обработана, изменений нет
# ревизия: arr[5] *= 44 — не выполняется
arr[7] = int(t280) % 97
# архив: arr[2] *= 16 — не выполняется
# ревизия: запись 897 обработана, изменений нет
# справка: запись 862 обработана, изменений нет
# ревизия: arr[9] = 48 — не выполняется
# справка: arr[0] += 15 — не выполняется
# архив: запись 536 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 591 обработана, изменений нет
# временная запись: arr[2] *= 63 — не выполняется
# замечание: запись 475 обработана, изменений нет
# замечание: arr2[1] = 41 — не выполняется
# отладка: arr2[1] = 28 — не выполняется
# ревизия: arr[6] += 6 — не выполняется
# пометка: запись 930 обработана, изменений нет
# ревизия: arr[5] *= 63 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 415 обработана, изменений нет
# ревизия: запись 207 обработана, изменений нет
# примечание: запись 839 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# примечание: arr[8] = 28 — не выполняется
# отладка: arr[5] = 45 — не выполняется
# справка: запись 168 обработана, изменений нет
# отладка: запись 372 обработана, изменений нет
# черновик: запись 65 обработана, изменений нет
# отладка: arr[4] += 70 — не выполняется
# отладка: запись 571 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 34 обработана, изменений нет
# временная запись: запись 556 обработана, изменений нет
# проверено: запись 52 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# замечание: arr[7] += 68 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 549 обработана, изменений нет
# ревизия: arr2[5] = 15 — не выполняется
# ревизия: запись 995 обработана, изменений нет
# пометка: arr2[8] = 39 — не выполняется
# проверено: arr[7] *= 76 — не выполняется
# отладка: arr[6] += 49 — не выполняется
# примечание: запись 434 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr2[9] = 24 — не выполняется
# черновик: arr[0] += 92 — не выполняется
# ревизия: запись 740 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 212 обработана, изменений нет
# проверено: запись 796 обработана, изменений нет
# черновик: arr[1] = 5 — не выполняется
# проверено: запись 847 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# отладка: запись 784 обработана, изменений нет
# архив: запись 348 обработана, изменений нет
# примечание: arr[8] += 72 — не выполняется
# примечание: запись 6 обработана, изменений нет
# архив: запись 358 обработана, изменений нет
# ревизия: запись 617 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# замечание: запись 922 обработана, изменений нет
# черновик: запись 318 обработана, изменений нет
# справка: arr[5] *= 98 — не выполняется
# справка: запись 643 обработана, изменений нет
# ревизия: запись 179 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# временная запись: arr2[9] = 51 — не выполняется
# замечание: запись 999 обработана, изменений нет
# временная запись: запись 701 обработана, изменений нет
# справка: запись 70 обработана, изменений нет
# замечание: arr[9] += 35 — не выполняется
# черновик: запись 88 обработана, изменений нет
# примечание: запись 478 обработана, изменений нет
# отладка: arr2[4] = 39 — не выполняется
# черновик: arr[7] += 86 — не выполняется
# примечание: arr[1] *= 48 — не выполняется
# проверено: arr[3] *= 28 — не выполняется
# пометка: arr[5] = 11 — не выполняется
# ревизия: запись 910 обработана, изменений нет
# временная запись: arr[6] = 8 — не выполняется
# временная запись: arr[3] *= 11 — не выполняется
# проверено: запись 352 обработана, изменений нет
# архив: arr[7] *= 70 — не выполняется
# архив: arr[6] = 90 — не выполняется
# проверено: arr2[5] = 73 — не выполняется
# черновик: arr[5] += 97 — не выполняется
# отладка: arr2[5] = 69 — не выполняется
# замечание: arr2[1] = 22 — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: запись 163 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 197 обработана, изменений нет
# черновик: arr[4] += 1 — не выполняется
# архив: запись 678 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# ревизия: arr[4] = 40 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# черновик: arr2[9] = 17 — не выполняется
# пометка: arr[2] = 53 — не выполняется
# пометка: arr2[8] = 78 — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr2[6] = 64 — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 626 обработана, изменений нет
# справка: arr2[2] = 26 — не выполняется
# временная запись: arr[6] += 12 — не выполняется
# пометка: запись 71 обработана, изменений нет
# архив: arr[4] = 38 — не выполняется
# временная запись: arr[2] += 56 — не выполняется
# справка: arr[7] *= 5 — не выполняется
# справка: arr[6] *= 19 — не выполняется
# замечание: запись 29 обработана, изменений нет
# замечание: запись 451 обработана, изменений нет
# ревизия: arr2[0] = 79 — не выполняется
# временная запись: запись 429 обработана, изменений нет
# черновик: запись 838 обработана, изменений нет
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 485 обработана, изменений нет
# временная запись: запись 494 обработана, изменений нет
# черновик: запись 534 обработана, изменений нет
# замечание: запись 553 обработана, изменений нет
# архив: запись 39 обработана, изменений нет
# архив: arr[2] += 62 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 293 обработана, изменений нет
# временная запись: запись 647 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[7] = 51 — не выполняется
# черновик: запись 123 обработана, изменений нет
# замечание: запись 881 обработана, изменений нет
# справка: arr[0] *= 8 — не выполняется
# черновик: запись 55 обработана, изменений нет
# замечание: запись 429 обработана, изменений нет
# временная запись: arr2[8] = 58 — не выполняется
# черновик: arr2[6] = 63 — не выполняется
# черновик: запись 200 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# отладка: arr2[8] = 27 — не выполняется
# проверено: arr[3] += 9 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# архив: запись 451 обработана, изменений нет
# примечание: arr[5] = 53 — не выполняется
# замечание: запись 255 обработана, изменений нет
# проверено: arr2[9] = 62 — не выполняется
# отладка: запись 944 обработана, изменений нет
# проверено: arr[1] *= 59 — не выполняется
# архив: arr[3] = 18 — не выполняется
# справка: arr[8] += 7 — не выполняется
# отладка: запись 163 обработана, изменений нет
# отладка: arr[2] *= 6 — не выполняется
# отладка: arr[3] *= 34 — не выполняется
# пометка: запись 82 обработана, изменений нет
# справка: запись 870 обработана, изменений нет
# черновик: запись 509 обработана, изменений нет
# отладка: запись 918 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 355 обработана, изменений нет
# отладка: запись 645 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr2[6] = 35 — не выполняется
# ревизия: запись 44 обработана, изменений нет
# отладка: запись 443 обработана, изменений нет
# отладка: arr[6] *= 96 — не выполняется
# пометка: запись 926 обработана, изменений нет
# проверено: arr[4] = 27 — не выполняется
# справка: arr2[0] = 96 — не выполняется
# архив: запись 700 обработана, изменений нет
# временная запись: запись 84 обработана, изменений нет
# примечание: запись 689 обработана, изменений нет
# примечание: arr[8] = 14 — не выполняется
# черновик: запись 490 обработана, изменений нет
# замечание: запись 820 обработана, изменений нет
# архив: arr[1] += 79 — не выполняется
# примечание: запись 917 обработана, изменений нет
# примечание: arr[0] = 1 — не выполняется
# справка: запись 824 обработана, изменений нет
# замечание: arr[2] *= 22 — не выполняется
# примечание: запись 255 обработана, изменений нет
# пометка: запись 488 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 286 обработана, изменений нет
# временная запись: arr2[8] = 87 — не выполняется
# справка: arr[4] += 97 — не выполняется
# проверено: запись 313 обработана, изменений нет
# временная запись: запись 811 обработана, изменений нет
# замечание: запись 943 обработана, изменений нет
# примечание: запись 818 обработана, изменений нет
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 459 обработана, изменений нет
# ревизия: arr[3] += 67 — не выполняется
# черновик: запись 724 обработана, изменений нет
# архив: arr[9] *= 11 — не выполняется
# замечание: запись 571 обработана, изменений нет
# примечание: запись 557 обработана, изменений нет
# справка: arr[5] += 28 — не выполняется
# справка: запись 778 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# отладка: запись 376 обработана, изменений нет
# отладка: arr[4] *= 66 — не выполняется
# временная запись: запись 423 обработана, изменений нет
# архив: запись 352 обработана, изменений нет
# отладка: запись 663 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: arr[5] *= 50 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[6] += 92 — не выполняется
# архив: запись 100 обработана, изменений нет
# проверено: arr2[7] = 70 — не выполняется
# временная запись: arr[9] *= 1 — не выполняется
# ревизия: arr[5] = 40 — не выполняется
# архив: запись 51 обработана, изменений нет
# справка: arr[3] += 59 — не выполняется
# временная запись: arr[9] *= 57 — не выполняется
# временная запись: запись 259 обработана, изменений нет
# замечание: arr[1] += 22 — не выполняется
# замечание: arr[7] = 32 — не выполняется
# замечание: запись 927 обработана, изменений нет
# ревизия: запись 139 обработана, изменений нет
# проверено: arr[4] = 30 — не выполняется
# примечание: запись 317 обработана, изменений нет
# временная запись: arr[2] = 77 — не выполняется
# примечание: arr2[5] = 28 — не выполняется
# примечание: arr[6] *= 35 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: запись 186 обработана, изменений нет
# архив: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[5] *= 21 — не выполняется
# замечание: запись 228 обработана, изменений нет
# пометка: arr[8] += 65 — не выполняется
# проверено: запись 774 обработана, изменений нет
# справка: arr2[5] = 58 — не выполняется
# черновик: arr[2] += 49 — не выполняется
# пометка: arr2[6] = 65 — не выполняется
# отладка: arr2[5] = 83 — не выполняется
# ревизия: запись 784 обработана, изменений нет
# справка: запись 404 обработана, изменений нет
# отладка: arr2[0] = 53 — не выполняется
# архив: запись 947 обработана, изменений нет
# пометка: запись 638 обработана, изменений нет
# временная запись: запись 169 обработана, изменений нет
# отладка: запись 791 обработана, изменений нет
# проверено: arr2[7] = 84 — не выполняется
# справка: arr[7] *= 32 — не выполняется
# отладка: arr[8] += 90 — не выполняется
# архив: arr[8] += 64 — не выполняется
# замечание: arr[3] *= 36 — не выполняется
# справка: запись 251 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# отладка: запись 987 обработана, изменений нет
# проверено: arr[8] = 54 — не выполняется
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 285 обработана, изменений нет
# проверено: запись 160 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# архив: arr2[1] = 76 — не выполняется
# временная запись: запись 787 обработана, изменений нет
# справка: arr[4] *= 48 — не выполняется
# ревизия: запись 82 обработана, изменений нет
# черновик: arr[3] = 78 — не выполняется
# проверено: запись 582 обработана, изменений нет
# замечание: arr[2] += 53 — не выполняется
# отладка: arr[0] *= 41 — не выполняется
# проверено: запись 373 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[0] += 96 — не выполняется
# временная запись: arr[0] = 33 — не выполняется
# ревизия: arr[8] += 10 — не выполняется
# пометка: запись 429 обработана, изменений нет
# ревизия: запись 788 обработана, изменений нет
# замечание: запись 663 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 230 обработана, изменений нет
# проверено: arr[1] *= 78 — не выполняется
# отладка: arr[4] *= 11 — не выполняется
# временная запись: arr[1] *= 33 — не выполняется
# архив: запись 310 обработана, изменений нет
# проверено: arr[2] *= 42 — не выполняется
# отладка: запись 970 обработана, изменений нет
# временная запись: arr[8] *= 94 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 190 обработана, изменений нет
# временная запись: запись 541 обработана, изменений нет
# примечание: arr[5] = 33 — не выполняется
# ревизия: arr2[9] = 5 — не выполняется
# ревизия: arr[8] += 25 — не выполняется
# архив: arr2[6] = 81 — не выполняется
# замечание: arr[6] += 4 — не выполняется
# замечание: запись 577 обработана, изменений нет
# архив: запись 834 обработана, изменений нет
# отладка: запись 432 обработана, изменений нет
# временная запись: запись 439 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 344 обработана, изменений нет
# ревизия: arr[5] += 85 — не выполняется
# пометка: запись 513 обработана, изменений нет
# временная запись: arr[4] = 32 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 370 обработана, изменений нет
# проверено: запись 35 обработана, изменений нет
# пометка: запись 383 обработана, изменений нет
# справка: arr[8] = 40 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: запись 865 обработана, изменений нет
# пометка: arr2[1] = 24 — не выполняется
# архив: arr[0] += 73 — не выполняется
# пометка: запись 253 обработана, изменений нет
arr[6] *= 2
# ревизия: запись 112 обработана, изменений нет
# черновик: запись 538 обработана, изменений нет
# архив: arr[2] = 74 — не выполняется
# замечание: запись 55 обработана, изменений нет
# временная запись: запись 151 обработана, изменений нет
# замечание: запись 661 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[6] *= 66 — не выполняется
# замечание: запись 108 обработана, изменений нет
# черновик: запись 798 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# архив: запись 848 обработана, изменений нет
# отладка: arr[2] = 5 — не выполняется
# проверено: запись 699 обработана, изменений нет
# черновик: arr2[0] = 46 — не выполняется
# пометка: arr[6] = 46 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: запись 355 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# справка: arr[8] += 49 — не выполняется
# пометка: запись 790 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[3] *= 51 — не выполняется
# примечание: arr[2] *= 69 — не выполняется
# отладка: arr[6] += 58 — не выполняется
# ревизия: arr[8] *= 22 — не выполняется
# пометка: запись 180 обработана, изменений нет
# справка: arr[0] += 19 — не выполняется
# временная запись: запись 762 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr[7] *= 51 — не выполняется
# временная запись: запись 632 обработана, изменений нет
# отладка: arr[9] += 62 — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[3] = 77 — не выполняется
# справка: arr[8] *= 35 — не выполняется
# отладка: arr2[3] = 33 — не выполняется
# замечание: запись 875 обработана, изменений нет
# замечание: arr[9] += 31 — не выполняется
# пометка: arr2[4] = 83 — не выполняется
# отладка: запись 220 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# справка: запись 226 обработана, изменений нет
# отладка: arr[7] += 9 — не выполняется
# отладка: запись 313 обработана, изменений нет
# временная запись: arr[4] *= 75 — не выполняется
# примечание: arr2[5] = 28 — не выполняется
# черновик: запись 163 обработана, изменений нет
# справка: запись 708 обработана, изменений нет
# ревизия: запись 961 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: arr[3] += 74 — не выполняется
# черновик: запись 576 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# ревизия: arr[0] *= 69 — не выполняется
# временная запись: arr2[0] = 39 — не выполняется
# пометка: arr[3] = 43 — не выполняется
# пометка: arr[4] = 18 — не выполняется
# замечание: запись 431 обработана, изменений нет
# замечание: arr[2] += 56 — не выполняется
# отладка: arr2[5] = 13 — не выполняется
# примечание: запись 905 обработана, изменений нет
# замечание: arr[7] += 21 — не выполняется
# проверено: arr[6] *= 37 — не выполняется
# архив: запись 313 обработана, изменений нет
# архив: arr[5] += 54 — не выполняется
# пометка: arr[5] *= 41 — не выполняется
# архив: arr[7] *= 97 — не выполняется
# замечание: запись 806 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# замечание: запись 289 обработана, изменений нет
# отладка: arr2[8] = 49 — не выполняется
# архив: arr2[9] = 63 — не выполняется
# пометка: arr[9] += 39 — не выполняется
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 984 обработана, изменений нет
# ревизия: запись 69 обработана, изменений нет
# справка: запись 807 обработана, изменений нет
# временная запись: arr[3] = 39 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# временная запись: запись 579 обработана, изменений нет
# примечание: arr[7] = 48 — не выполняется
# примечание: запись 440 обработана, изменений нет
# временная запись: arr[9] = 43 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# черновик: arr2[9] = 88 — не выполняется
# проверено: запись 242 обработана, изменений нет
# ревизия: запись 604 обработана, изменений нет
# архив: arr[3] *= 42 — не выполняется
# архив: запись 977 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# черновик: запись 293 обработана, изменений нет
# черновик: arr[1] = 24 — не выполняется
# ревизия: запись 118 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# примечание: arr2[1] = 20 — не выполняется
# пометка: запись 412 обработана, изменений нет
# замечание: запись 385 обработана, изменений нет
# временная запись: arr[5] = 35 — не выполняется
# временная запись: запись 882 обработана, изменений нет
# временная запись: запись 348 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[0] = 7 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# примечание: запись 69 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# черновик: запись 831 обработана, изменений нет
# черновик: запись 14 обработана, изменений нет
# отладка: arr[6] *= 92 — не выполняется
# черновик: arr[6] = 51 — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 493 обработана, изменений нет
# архив: arr[6] = 67 — не выполняется
# проверено: запись 268 обработана, изменений нет
# замечание: запись 823 обработана, изменений нет
# ревизия: arr2[2] = 37 — не выполняется
# замечание: arr2[8] = 96 — не выполняется
# временная запись: запись 965 обработана, изменений нет
# временная запись: arr[7] *= 26 — не выполняется
# архив: arr[2] *= 75 — не выполняется
# отладка: запись 730 обработана, изменений нет
# временная запись: arr[4] = 65 — не выполняется
# временная запись: запись 695 обработана, изменений нет
# справка: запись 647 обработана, изменений нет
# справка: arr[0] = 36 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 212 обработана, изменений нет
# архив: запись 64 обработана, изменений нет
# временная запись: запись 761 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 974 обработана, изменений нет
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 20 обработана, изменений нет
# отладка: запись 960 обработана, изменений нет
# справка: arr[2] *= 68 — не выполняется
# ревизия: arr[4] = 85 — не выполняется
# временная запись: arr[7] *= 55 — не выполняется
# архив: запись 758 обработана, изменений нет
# временная запись: запись 391 обработана, изменений нет
# примечание: arr2[4] = 3 — не выполняется
# замечание: запись 933 обработана, изменений нет
# примечание: arr[5] = 78 — не выполняется
# примечание: запись 783 обработана, изменений нет
# проверено: запись 618 обработана, изменений нет
# временная запись: запись 104 обработана, изменений нет
# пометка: arr[9] *= 35 — не выполняется
# архив: arr[6] += 99 — не выполняется
# проверено: запись 291 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# примечание: arr[9] *= 22 — не выполняется
# ревизия: arr[8] *= 83 — не выполняется
# справка: arr2[8] = 11 — не выполняется
# отладка: запись 786 обработана, изменений нет
# замечание: arr[6] += 91 — не выполняется
# пометка: arr[5] = 42 — не выполняется
# замечание: arr[2] *= 65 — не выполняется
# примечание: запись 125 обработана, изменений нет
# временная запись: запись 378 обработана, изменений нет
# замечание: запись 482 обработана, изменений нет
# замечание: запись 794 обработана, изменений нет
# примечание: arr[8] += 3 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# отладка: arr[8] = 89 — не выполняется
# временная запись: arr[0] *= 69 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 931 обработана, изменений нет
# замечание: запись 431 обработана, изменений нет
# отладка: arr[9] *= 11 — не выполняется
# временная запись: запись 792 обработана, изменений нет
# примечание: arr[3] *= 77 — не выполняется
# справка: запись 107 обработана, изменений нет
# черновик: запись 226 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[2] = 49 — не выполняется
# пометка: arr[7] += 50 — не выполняется
# проверено: запись 230 обработана, изменений нет
# справка: arr[4] += 30 — не выполняется
# черновик: запись 680 обработана, изменений нет
# проверено: запись 527 обработана, изменений нет
# черновик: arr2[8] = 52 — не выполняется
# справка: запись 782 обработана, изменений нет
# отладка: arr[5] *= 82 — не выполняется
# замечание: arr[4] += 98 — не выполняется
# пометка: запись 376 обработана, изменений нет
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 890 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# архив: запись 240 обработана, изменений нет
# примечание: запись 103 обработана, изменений нет
# отладка: запись 139 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# проверено: запись 591 обработана, изменений нет
# архив: arr2[9] = 27 — не выполняется
# пометка: запись 540 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# пометка: arr[6] += 4 — не выполняется
# примечание: запись 67 обработана, изменений нет
# проверено: arr2[9] = 61 — не выполняется
# справка: запись 351 обработана, изменений нет
# временная запись: запись 124 обработана, изменений нет
# отладка: arr[8] *= 99 — не выполняется
# пометка: запись 464 обработана, изменений нет
# отладка: arr2[6] = 25 — не выполняется
# отладка: arr[1] *= 98 — не выполняется
# черновик: arr[9] += 65 — не выполняется
# отладка: запись 591 обработана, изменений нет
# примечание: запись 173 обработана, изменений нет
# справка: arr[2] = 83 — не выполняется
# ревизия: запись 999 обработана, изменений нет
# справка: arr[3] += 90 — не выполняется
# архив: arr2[1] = 84 — не выполняется
# временная запись: запись 782 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# замечание: arr2[2] = 1 — не выполняется
# проверено: arr[2] = 36 — не выполняется
# черновик: arr[9] = 81 — не выполняется
# черновик: arr[9] *= 42 — не выполняется
# отладка: запись 546 обработана, изменений нет
# архив: arr[4] *= 50 — не выполняется
# примечание: запись 409 обработана, изменений нет
# проверено: arr[3] += 7 — не выполняется
# отладка: запись 31 обработана, изменений нет
# временная запись: arr[7] += 81 — не выполняется
# отладка: запись 269 обработана, изменений нет
# проверено: arr2[6] = 39 — не выполняется
# ревизия: запись 136 обработана, изменений нет
# отладка: arr[0] = 91 — не выполняется
# проверено: arr2[3] = 70 — не выполняется
# пометка: arr[6] = 73 — не выполняется
# архив: arr[6] = 99 — не выполняется
# ревизия: запись 344 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# пометка: запись 965 обработана, изменений нет
# временная запись: arr[7] *= 23 — не выполняется
# замечание: запись 25 обработана, изменений нет
# отладка: запись 376 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[6] = 62 — не выполняется
# ревизия: запись 287 обработана, изменений нет
# замечание: arr2[2] = 27 — не выполняется
# архив: запись 771 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# черновик: запись 387 обработана, изменений нет
# замечание: запись 601 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 166 обработана, изменений нет
# замечание: arr2[0] = 29 — не выполняется
# проверено: запись 133 обработана, изменений нет
# справка: запись 479 обработана, изменений нет
# проверено: arr[2] += 85 — не выполняется
# ревизия: arr[2] *= 15 — не выполняется
# проверено: запись 256 обработана, изменений нет
# примечание: arr[7] += 82 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: arr2[8] = 23 — не выполняется
# проверено: запись 935 обработана, изменений нет
# ревизия: запись 445 обработана, изменений нет
# пометка: запись 728 обработана, изменений нет
# отладка: arr2[4] = 91 — не выполняется
# примечание: arr[5] *= 62 — не выполняется
# справка: запись 831 обработана, изменений нет
# ревизия: arr[3] = 6 — не выполняется
# отладка: запись 199 обработана, изменений нет
# примечание: запись 879 обработана, изменений нет
# проверено: arr[0] *= 19 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: запись 43 обработана, изменений нет
# проверено: arr[2] += 39 — не выполняется
# замечание: arr[4] *= 91 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# временная запись: arr[7] *= 58 — не выполняется
# архив: запись 652 обработана, изменений нет
# справка: запись 219 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# ревизия: запись 365 обработана, изменений нет
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[9] += 56 — не выполняется
# ревизия: запись 818 обработана, изменений нет
# замечание: запись 931 обработана, изменений нет
# пометка: запись 515 обработана, изменений нет
# архив: arr[8] = 5 — не выполняется
# ревизия: запись 256 обработана, изменений нет
# справка: arr[7] = 80 — не выполняется
# проверено: запись 600 обработана, изменений нет
# примечание: запись 259 обработана, изменений нет
# временная запись: запись 496 обработана, изменений нет
# архив: запись 492 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[0] += 86 — не выполняется
# замечание: arr[2] *= 97 — не выполняется
# временная запись: arr2[3] = 89 — не выполняется
# временная запись: запись 885 обработана, изменений нет
# черновик: arr[9] += 79 — не выполняется
# черновик: arr[6] = 15 — не выполняется
# проверено: запись 375 обработана, изменений нет
# проверено: arr[4] *= 42 — не выполняется
# замечание: arr[1] *= 16 — не выполняется
# черновик: запись 46 обработана, изменений нет
# ревизия: arr[4] *= 71 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 348 обработана, изменений нет
# примечание: arr[0] += 76 — не выполняется
# пометка: arr[3] += 4 — не выполняется
arr[6] += 2
# временная запись: arr2[9] = 95 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: запись 562 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# примечание: arr[6] = 10 — не выполняется
# справка: запись 472 обработана, изменений нет
# примечание: arr2[0] = 25 — не выполняется
# черновик: arr[7] += 74 — не выполняется
# архив: запись 715 обработана, изменений нет
# примечание: arr[8] = 36 — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[2] += 57 — не выполняется
# примечание: arr2[8] = 93 — не выполняется
# временная запись: arr2[2] = 72 — не выполняется
# ревизия: arr[6] = 68 — не выполняется
# временная запись: запись 501 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: запись 752 обработана, изменений нет
# отладка: arr[9] *= 88 — не выполняется
# ревизия: arr[1] = 43 — не выполняется
# примечание: запись 271 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 17 обработана, изменений нет
# временная запись: arr2[3] = 34 — не выполняется
# ревизия: запись 158 обработана, изменений нет
# архив: arr[3] = 59 — не выполняется
# проверено: запись 436 обработана, изменений нет
# замечание: arr2[5] = 49 — не выполняется
# проверено: arr[4] = 92 — не выполняется
# пометка: arr[8] = 89 — не выполняется
# временная запись: запись 411 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# отладка: запись 732 обработана, изменений нет
# замечание: arr[6] += 69 — не выполняется
# временная запись: запись 287 обработана, изменений нет
# ревизия: arr2[5] = 24 — не выполняется
# замечание: запись 143 обработана, изменений нет
# черновик: arr[4] += 70 — не выполняется
# пометка: запись 137 обработана, изменений нет
# отладка: запись 878 обработана, изменений нет
# примечание: запись 91 обработана, изменений нет
# черновик: arr[6] = 25 — не выполняется
# справка: arr2[2] = 28 — не выполняется
# черновик: запись 215 обработана, изменений нет
# пометка: запись 559 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 410 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# ревизия: запись 446 обработана, изменений нет
# ревизия: arr[2] = 48 — не выполняется
# ревизия: запись 350 обработана, изменений нет
# черновик: arr[4] = 45 — не выполняется
# временная запись: запись 221 обработана, изменений нет
# справка: arr[0] = 79 — не выполняется
# черновик: arr[1] = 40 — не выполняется
# архив: запись 545 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# ревизия: запись 891 обработана, изменений нет
# отладка: запись 390 обработана, изменений нет
# отладка: arr[2] += 12 — не выполняется
# проверено: arr[4] += 16 — не выполняется
# пометка: запись 311 обработана, изменений нет
# архив: arr2[3] = 92 — не выполняется
# ревизия: запись 515 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# архив: запись 263 обработана, изменений нет
# ревизия: запись 770 обработана, изменений нет
# справка: arr[2] = 69 — не выполняется
# черновик: arr2[4] = 70 — не выполняется
# примечание: запись 573 обработана, изменений нет
# отладка: запись 805 обработана, изменений нет
# временная запись: arr[5] += 51 — не выполняется
# отладка: запись 594 обработана, изменений нет
# проверено: arr[4] = 43 — не выполняется
# замечание: запись 909 обработана, изменений нет
# замечание: запись 555 обработана, изменений нет
# черновик: запись 645 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 989 обработана, изменений нет
# временная запись: arr[9] = 28 — не выполняется
# ревизия: arr[3] *= 15 — не выполняется
# ревизия: запись 446 обработана, изменений нет
# пометка: arr2[2] = 36 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[5] *= 52 — не выполняется
# временная запись: arr[9] = 99 — не выполняется
# замечание: запись 157 обработана, изменений нет
# замечание: запись 171 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[8] += 11 — не выполняется
# проверено: запись 472 обработана, изменений нет
# архив: arr[3] = 19 — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: запись 484 обработана, изменений нет
# проверено: arr2[5] = 78 — не выполняется
# архив: запись 339 обработана, изменений нет
# справка: запись 691 обработана, изменений нет
# пометка: arr[5] = 14 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# замечание: arr[5] += 60 — не выполняется
# ревизия: запись 242 обработана, изменений нет
# проверено: запись 801 обработана, изменений нет
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[0] = 21 — не выполняется
# черновик: запись 264 обработана, изменений нет
# пометка: arr[2] = 90 — не выполняется
# проверено: arr[6] *= 59 — не выполняется
# пометка: arr[7] *= 42 — не выполняется
# архив: запись 602 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr2[0] = 62 — не выполняется
# пометка: запись 140 обработана, изменений нет
# временная запись: запись 537 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# примечание: запись 334 обработана, изменений нет
# отладка: arr2[5] = 19 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[7] += 93 — не выполняется
# ревизия: запись 814 обработана, изменений нет
# временная запись: запись 400 обработана, изменений нет
# ревизия: arr[2] = 10 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# проверено: запись 267 обработана, изменений нет
# справка: arr[4] *= 66 — не выполняется
# ревизия: запись 429 обработана, изменений нет
# отладка: arr[8] += 78 — не выполняется
# пометка: arr[2] += 67 — не выполняется
# проверено: запись 138 обработана, изменений нет
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 106 обработана, изменений нет
# архив: запись 437 обработана, изменений нет
# примечание: arr[2] = 65 — не выполняется
# временная запись: arr2[8] = 42 — не выполняется
# черновик: arr[8] = 28 — не выполняется
# проверено: запись 628 обработана, изменений нет
# проверено: arr[0] = 6 — не выполняется
# архив: запись 312 обработана, изменений нет
# пометка: arr[3] = 7 — не выполняется
# черновик: arr[7] *= 46 — не выполняется
# временная запись: запись 282 обработана, изменений нет
# ревизия: arr[1] *= 99 — не выполняется
# ревизия: запись 714 обработана, изменений нет
# отладка: arr2[4] = 33 — не выполняется
# временная запись: arr2[0] = 95 — не выполняется
# справка: запись 260 обработана, изменений нет
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: запись 586 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 471 обработана, изменений нет
# справка: запись 355 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: arr[2] += 80 — не выполняется
# ревизия: arr[6] *= 35 — не выполняется
# проверено: запись 250 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: запись 835 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# временная запись: arr2[6] = 32 — не выполняется
# справка: arr[9] = 73 — не выполняется
# черновик: запись 358 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[4] = 90 — не выполняется
# проверено: arr[7] *= 24 — не выполняется
# отладка: запись 673 обработана, изменений нет
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 551 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# замечание: запись 362 обработана, изменений нет
# ревизия: arr[0] *= 84 — не выполняется
# проверено: запись 323 обработана, изменений нет
# примечание: запись 91 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: arr[7] *= 46 — не выполняется
# пометка: запись 898 обработана, изменений нет
# временная запись: запись 512 обработана, изменений нет
# замечание: arr2[6] = 59 — не выполняется
# ревизия: запись 563 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: запись 747 обработана, изменений нет
# временная запись: arr[8] += 53 — не выполняется
# замечание: запись 648 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# черновик: запись 580 обработана, изменений нет
# отладка: arr[7] = 97 — не выполняется
# проверено: запись 8 обработана, изменений нет
# проверено: arr2[1] = 2 — не выполняется
# ревизия: arr[3] = 23 — не выполняется
# ревизия: запись 484 обработана, изменений нет
# пометка: arr2[6] = 54 — не выполняется
# архив: arr[4] = 52 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[4] += 21 — не выполняется
# примечание: запись 205 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[1] = 85 — не выполняется
# архив: запись 41 обработана, изменений нет
# черновик: запись 577 обработана, изменений нет
# замечание: запись 110 обработана, изменений нет
# отладка: запись 460 обработана, изменений нет
# отладка: запись 870 обработана, изменений нет
# временная запись: arr[4] += 83 — не выполняется
# пометка: arr[4] *= 94 — не выполняется
# архив: arr2[1] = 58 — не выполняется
# черновик: запись 491 обработана, изменений нет
# отладка: запись 668 обработана, изменений нет
# архив: arr[3] += 52 — не выполняется
# примечание: arr[4] *= 2 — не выполняется
# замечание: запись 974 обработана, изменений нет
# временная запись: запись 395 обработана, изменений нет
# проверено: запись 104 обработана, изменений нет
# ревизия: запись 617 обработана, изменений нет
# проверено: запись 797 обработана, изменений нет
# временная запись: arr[3] += 65 — не выполняется
# отладка: запись 447 обработана, изменений нет
# архив: запись 914 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 984 обработана, изменений нет
# временная запись: запись 599 обработана, изменений нет
# пометка: запись 124 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 324 обработана, изменений нет
# примечание: запись 24 обработана, изменений нет
# проверено: запись 420 обработана, изменений нет
# ревизия: arr[3] *= 43 — не выполняется
# ревизия: запись 410 обработана, изменений нет
# отладка: arr[0] = 93 — не выполняется
# примечание: запись 721 обработана, изменений нет
# отладка: запись 807 обработана, изменений нет
# проверено: запись 680 обработана, изменений нет
# архив: arr[8] = 37 — не выполняется
# черновик: arr[6] = 96 — не выполняется
# временная запись: запись 94 обработана, изменений нет
# примечание: запись 895 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# замечание: запись 484 обработана, изменений нет
# отладка: запись 790 обработана, изменений нет
# замечание: запись 59 обработана, изменений нет
# архив: запись 451 обработана, изменений нет
# ревизия: arr2[4] = 28 — не выполняется
# ревизия: arr[9] += 6 — не выполняется
# отладка: arr[6] *= 57 — не выполняется
# проверено: запись 427 обработана, изменений нет
# временная запись: arr[5] += 84 — не выполняется
# отладка: запись 153 обработана, изменений нет
# справка: запись 846 обработана, изменений нет
# архив: запись 888 обработана, изменений нет
# архив: arr[5] = 82 — не выполняется
# отладка: arr[7] = 62 — не выполняется
# архив: запись 830 обработана, изменений нет
# замечание: arr[3] = 45 — не выполняется
# черновик: запись 866 обработана, изменений нет
# замечание: arr[4] *= 11 — не выполняется
# ревизия: запись 298 обработана, изменений нет
# черновик: запись 277 обработана, изменений нет
# архив: arr[9] += 65 — не выполняется
# черновик: arr[4] = 55 — не выполняется
# черновик: запись 157 обработана, изменений нет
# справка: запись 612 обработана, изменений нет
# временная запись: arr[5] += 95 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# замечание: arr[5] = 81 — не выполняется
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: запись 893 обработана, изменений нет
# справка: запись 734 обработана, изменений нет
# ревизия: arr2[2] = 74 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 475 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr2[7] = 23 — не выполняется
# справка: запись 903 обработана, изменений нет
# архив: arr[3] += 34 — не выполняется
# замечание: arr[6] = 80 — не выполняется
# архив: запись 716 обработана, изменений нет
# архив: arr2[5] = 29 — не выполняется
# замечание: запись 347 обработана, изменений нет
# пометка: запись 341 обработана, изменений нет
# проверено: запись 304 обработана, изменений нет
# черновик: arr2[0] = 97 — не выполняется
# замечание: arr2[4] = 93 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 482 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# архив: запись 626 обработана, изменений нет
# отладка: arr2[1] = 76 — не выполняется
# примечание: запись 607 обработана, изменений нет
# примечание: arr2[4] = 95 — не выполняется
# черновик: запись 405 обработана, изменений нет
# временная запись: запись 776 обработана, изменений нет
# временная запись: arr[1] = 60 — не выполняется
# замечание: запись 214 обработана, изменений нет
# временная запись: запись 441 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# ревизия: arr[7] += 89 — не выполняется
# проверено: запись 948 обработана, изменений нет
# черновик: arr2[5] = 43 — не выполняется
# замечание: запись 926 обработана, изменений нет
# примечание: запись 432 обработана, изменений нет
# ревизия: arr[2] *= 15 — не выполняется
# временная запись: arr[9] += 72 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 807 обработана, изменений нет
# проверено: запись 356 обработана, изменений нет
# примечание: запись 797 обработана, изменений нет
# проверено: arr[3] = 6 — не выполняется
apply_twice(arr, 6, 3)
# ревизия: запись 833 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# временная запись: arr[3] = 19 — не выполняется
# временная запись: arr[8] *= 59 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 209 обработана, изменений нет
# справка: запись 957 обработана, изменений нет
# справка: запись 236 обработана, изменений нет
# примечание: arr[4] = 30 — не выполняется
# проверено: запись 180 обработана, изменений нет
# ревизия: запись 256 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# черновик: arr[6] += 86 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[1] *= 24 — не выполняется
# проверено: запись 136 обработана, изменений нет
# ревизия: запись 775 обработана, изменений нет
# пометка: запись 863 обработана, изменений нет
# временная запись: запись 314 обработана, изменений нет
# черновик: запись 342 обработана, изменений нет
# справка: arr[4] += 11 — не выполняется
# временная запись: запись 472 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 742 обработана, изменений нет
# примечание: arr2[1] = 77 — не выполняется
# временная запись: arr[9] *= 73 — не выполняется
# отладка: arr[3] *= 10 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: arr[1] += 50 — не выполняется
# замечание: arr2[6] = 41 — не выполняется
# черновик: запись 653 обработана, изменений нет
# проверено: arr[7] = 78 — не выполняется
# примечание: arr[6] *= 70 — не выполняется
# черновик: запись 687 обработана, изменений нет
# пометка: запись 732 обработана, изменений нет
# архив: запись 819 обработана, изменений нет
# черновик: arr[8] += 42 — не выполняется
# примечание: arr[2] += 10 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 646 обработана, изменений нет
# временная запись: arr2[2] = 59 — не выполняется
# временная запись: arr2[8] = 7 — не выполняется
# примечание: arr[1] += 62 — не выполняется
# ревизия: arr[8] *= 32 — не выполняется
# отладка: arr2[1] = 79 — не выполняется
# пометка: arr2[3] = 21 — не выполняется
# справка: запись 593 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr2[3] = 15 — не выполняется
# справка: arr[0] += 48 — не выполняется
# пометка: arr[2] += 80 — не выполняется
# пометка: arr[7] = 13 — не выполняется
# черновик: arr[1] += 43 — не выполняется
# архив: arr[9] += 3 — не выполняется
# справка: запись 19 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# ревизия: arr2[8] = 85 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# архив: arr[5] = 89 — не выполняется
# примечание: запись 411 обработана, изменений нет
# ревизия: arr2[9] = 11 — не выполняется
# ревизия: запись 26 обработана, изменений нет
# примечание: запись 663 обработана, изменений нет
# пометка: запись 165 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# архив: запись 410 обработана, изменений нет
# справка: запись 23 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 321 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# примечание: запись 357 обработана, изменений нет
# архив: arr[5] = 61 — не выполняется
# справка: запись 956 обработана, изменений нет
# замечание: запись 333 обработана, изменений нет
# отладка: arr2[8] = 43 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 309 обработана, изменений нет
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 943 обработана, изменений нет
# пометка: запись 4 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 880 обработана, изменений нет
# пометка: запись 665 обработана, изменений нет
# временная запись: arr[3] += 63 — не выполняется
# пометка: запись 533 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[6] = 29 — не выполняется
# справка: запись 316 обработана, изменений нет
# ревизия: arr2[2] = 61 — не выполняется
# справка: arr2[6] = 84 — не выполняется
# пометка: arr[1] *= 49 — не выполняется
# замечание: запись 955 обработана, изменений нет
# ревизия: запись 303 обработана, изменений нет
# отладка: запись 773 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 913 обработана, изменений нет
# отладка: запись 485 обработана, изменений нет
# справка: запись 721 обработана, изменений нет
# черновик: запись 376 обработана, изменений нет
# проверено: запись 376 обработана, изменений нет
# справка: arr2[2] = 68 — не выполняется
# временная запись: arr[1] *= 46 — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[9] = 37 — не выполняется
# примечание: arr[1] += 80 — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 830 обработана, изменений нет
# архив: запись 35 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: запись 858 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr[1] += 85 — не выполняется
# черновик: запись 692 обработана, изменений нет
# отладка: запись 377 обработана, изменений нет
# примечание: запись 426 обработана, изменений нет
# проверено: arr[2] = 79 — не выполняется
# архив: запись 576 обработана, изменений нет
# черновик: arr[3] = 95 — не выполняется
# справка: запись 101 обработана, изменений нет
# отладка: запись 358 обработана, изменений нет
# пометка: arr[3] *= 76 — не выполняется
# замечание: arr[5] = 92 — не выполняется
# проверено: запись 256 обработана, изменений нет
# примечание: arr[7] = 35 — не выполняется
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 230 обработана, изменений нет
# черновик: запись 198 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: arr2[9] = 59 — не выполняется
# отладка: arr2[9] = 24 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: arr[3] = 98 — не выполняется
# архив: arr2[9] = 70 — не выполняется
# примечание: arr[0] += 89 — не выполняется
# временная запись: arr2[7] = 68 — не выполняется
# архив: arr2[6] = 91 — не выполняется
# черновик: arr2[7] = 49 — не выполняется
# временная запись: запись 27 обработана, изменений нет
# архив: arr[2] += 16 — не выполняется
# временная запись: arr[8] = 41 — не выполняется
# примечание: запись 214 обработана, изменений нет
# справка: запись 702 обработана, изменений нет
# примечание: arr[8] += 85 — не выполняется
# замечание: arr[5] = 83 — не выполняется
# архив: запись 917 обработана, изменений нет
# черновик: arr[9] *= 30 — не выполняется
# справка: запись 103 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# временная запись: arr2[8] = 70 — не выполняется
# ревизия: arr[6] = 93 — не выполняется
# пометка: запись 456 обработана, изменений нет
# черновик: arr[2] *= 95 — не выполняется
# отладка: arr[7] *= 68 — не выполняется
# ревизия: запись 851 обработана, изменений нет
# справка: запись 356 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# пометка: запись 628 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[8] *= 69 — не выполняется
# проверено: arr[2] = 66 — не выполняется
# замечание: запись 423 обработана, изменений нет
# проверено: запись 988 обработана, изменений нет
# черновик: arr[4] += 40 — не выполняется
# замечание: arr[3] *= 90 — не выполняется
# архив: arr2[4] = 18 — не выполняется
# ревизия: запись 838 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# архив: запись 411 обработана, изменений нет
# пометка: arr2[1] = 81 — не выполняется
# замечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr2[4] = 51 — не выполняется
# примечание: запись 829 обработана, изменений нет
# пометка: arr[5] *= 41 — не выполняется
# временная запись: запись 586 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# пометка: arr2[3] = 88 — не выполняется
# отладка: arr[1] *= 51 — не выполняется
# пометка: arr[2] = 36 — не выполняется
# черновик: arr[3] *= 90 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 667 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 746 обработана, изменений нет
# примечание: запись 932 обработана, изменений нет
# черновик: arr2[5] = 88 — не выполняется
# справка: arr[9] += 90 — не выполняется
# справка: arr[0] += 23 — не выполняется
# черновик: arr[6] *= 95 — не выполняется
# замечание: запись 402 обработана, изменений нет
# ревизия: запись 271 обработана, изменений нет
# замечание: запись 814 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# пометка: запись 258 обработана, изменений нет
# временная запись: запись 397 обработана, изменений нет
# справка: arr[9] += 91 — не выполняется
# примечание: запись 724 обработана, изменений нет
# отладка: arr2[6] = 87 — не выполняется
# временная запись: запись 68 обработана, изменений нет
# замечание: запись 83 обработана, изменений нет
# пометка: arr[8] *= 74 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 924 обработана, изменений нет
# отладка: arr[7] = 30 — не выполняется
# проверено: запись 938 обработана, изменений нет
# справка: запись 110 обработана, изменений нет
# проверено: arr[3] += 12 — не выполняется
# пометка: запись 140 обработана, изменений нет
# справка: arr2[3] = 14 — не выполняется
# пометка: arr[4] += 57 — не выполняется
# черновик: запись 615 обработана, изменений нет
# временная запись: arr[7] *= 25 — не выполняется
# черновик: запись 880 обработана, изменений нет
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 252 обработана, изменений нет
# временная запись: запись 167 обработана, изменений нет
# ревизия: arr[2] += 54 — не выполняется
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: arr2[3] = 84 — не выполняется
# примечание: arr[6] *= 29 — не выполняется
# проверено: запись 776 обработана, изменений нет
# замечание: arr[1] = 63 — не выполняется
# отладка: arr[7] = 9 — не выполняется
# пометка: запись 507 обработана, изменений нет
# временная запись: arr[0] *= 86 — не выполняется
# ревизия: arr[8] += 13 — не выполняется
# отладка: запись 641 обработана, изменений нет
# ревизия: arr2[1] = 98 — не выполняется
# временная запись: запись 214 обработана, изменений нет
# примечание: arr[0] += 12 — не выполняется
# архив: запись 959 обработана, изменений нет
# архив: запись 89 обработана, изменений нет
# ревизия: запись 130 обработана, изменений нет
# ревизия: запись 467 обработана, изменений нет
# пометка: запись 63 обработана, изменений нет
# пометка: запись 242 обработана, изменений нет
# черновик: запись 686 обработана, изменений нет
# справка: запись 403 обработана, изменений нет
# отладка: arr[8] += 72 — не выполняется
# отладка: arr2[9] = 87 — не выполняется
# пометка: запись 796 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# пометка: arr[4] = 48 — не выполняется
# ревизия: запись 500 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# ревизия: arr[3] = 98 — не выполняется
# отладка: arr2[2] = 23 — не выполняется
# архив: запись 387 обработана, изменений нет
# справка: запись 4 обработана, изменений нет
# ревизия: запись 835 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 317 обработана, изменений нет
# проверено: arr[2] = 13 — не выполняется
# черновик: запись 95 обработана, изменений нет
# временная запись: запись 719 обработана, изменений нет
# справка: запись 532 обработана, изменений нет
# примечание: arr[9] *= 83 — не выполняется
# справка: запись 234 обработана, изменений нет
# замечание: arr2[2] = 64 — не выполняется
# черновик: запись 972 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 153 обработана, изменений нет
# замечание: запись 777 обработана, изменений нет
# черновик: запись 708 обработана, изменений нет
# архив: arr[0] = 59 — не выполняется
# справка: запись 977 обработана, изменений нет
# примечание: arr[3] += 62 — не выполняется
# отладка: запись 242 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: запись 827 обработана, изменений нет
# пометка: arr[3] = 7 — не выполняется
# проверено: запись 99 обработана, изменений нет
# ревизия: arr2[3] = 85 — не выполняется
# проверено: запись 671 обработана, изменений нет
# пометка: запись 594 обработана, изменений нет
# отладка: arr2[4] = 23 — не выполняется
# проверено: запись 331 обработана, изменений нет
# справка: запись 210 обработана, изменений нет
# отладка: запись 908 обработана, изменений нет
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: запись 312 обработана, изменений нет
# черновик: запись 334 обработана, изменений нет
# справка: запись 86 обработана, изменений нет
# черновик: arr[9] += 30 — не выполняется
# проверено: запись 315 обработана, изменений нет
# справка: arr[0] = 37 — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 704 обработана, изменений нет
# черновик: arr[4] = 93 — не выполняется
# проверено: запись 513 обработана, изменений нет
# ревизия: запись 276 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# пометка: запись 303 обработана, изменений нет
# пометка: запись 248 обработана, изменений нет
# справка: запись 447 обработана, изменений нет
# пометка: arr2[1] = 16 — не выполняется
# архив: запись 428 обработана, изменений нет
# временная запись: arr[9] += 47 — не выполняется
arr[1] = acc(arr, 8) % 100
# замечание: arr[1] *= 82 — не выполняется
# примечание: запись 606 обработана, изменений нет
# архив: arr[3] *= 87 — не выполняется
# справка: запись 290 обработана, изменений нет
# ревизия: arr[8] = 66 — не выполняется
# ревизия: запись 711 обработана, изменений нет
# отладка: запись 130 обработана, изменений нет
# черновик: запись 277 обработана, изменений нет
# замечание: arr2[2] = 39 — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[8] *= 43 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: запись 97 обработана, изменений нет
# архив: arr[4] *= 40 — не выполняется
# пометка: arr[7] = 32 — не выполняется
# временная запись: arr[4] += 41 — не выполняется
# справка: запись 449 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# примечание: запись 583 обработана, изменений нет
# справка: запись 352 обработана, изменений нет
# примечание: arr[1] = 97 — не выполняется
# временная запись: запись 416 обработана, изменений нет
# архив: arr[9] *= 64 — не выполняется
# пометка: запись 887 обработана, изменений нет
# примечание: arr[7] = 23 — не выполняется
# архив: arr[9] += 89 — не выполняется
# замечание: запись 666 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: arr[4] += 38 — не выполняется
# пометка: запись 372 обработана, изменений нет
# примечание: arr2[3] = 2 — не выполняется
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr2[8] = 64 — не выполняется
# проверено: запись 929 обработана, изменений нет
# отладка: запись 914 обработана, изменений нет
# примечание: arr[0] *= 83 — не выполняется
# примечание: запись 960 обработана, изменений нет
# справка: arr[0] += 72 — не выполняется
# черновик: arr2[0] = 34 — не выполняется
# черновик: запись 726 обработана, изменений нет
# черновик: запись 259 обработана, изменений нет
# ревизия: arr[6] *= 25 — не выполняется
# ревизия: arr[3] *= 30 — не выполняется
# проверено: arr[0] = 54 — не выполняется
# временная запись: arr[9] += 24 — не выполняется
# примечание: запись 507 обработана, изменений нет
# черновик: arr2[0] = 30 — не выполняется
# замечание: arr2[8] = 23 — не выполняется
# пометка: запись 867 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# отладка: запись 680 обработана, изменений нет
# ревизия: arr[4] = 15 — не выполняется
# ревизия: arr2[0] = 79 — не выполняется
# пометка: arr[5] = 49 — не выполняется
# отладка: запись 225 обработана, изменений нет
# справка: запись 176 обработана, изменений нет
# черновик: arr2[6] = 21 — не выполняется
# пометка: arr[5] = 86 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 557 обработана, изменений нет
# замечание: arr[2] *= 14 — не выполняется
# примечание: запись 622 обработана, изменений нет
# черновик: запись 307 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 990 обработана, изменений нет
# временная запись: arr[6] = 19 — не выполняется
# пометка: arr[8] = 4 — не выполняется
# черновик: запись 759 обработана, изменений нет
# проверено: запись 106 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 543 обработана, изменений нет
# архив: arr[3] += 24 — не выполняется
# пометка: arr2[2] = 88 — не выполняется
# ревизия: запись 302 обработана, изменений нет
# временная запись: запись 94 обработана, изменений нет
# архив: arr2[8] = 89 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 927 обработана, изменений нет
# архив: arr[5] *= 34 — не выполняется
# замечание: запись 857 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# проверено: запись 33 обработана, изменений нет
# примечание: arr2[9] = 58 — не выполняется
# временная запись: arr[4] = 42 — не выполняется
# справка: запись 307 обработана, изменений нет
# проверено: arr2[6] = 47 — не выполняется
# замечание: запись 78 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# отладка: запись 560 обработана, изменений нет
# замечание: arr[9] = 37 — не выполняется
# архив: запись 504 обработана, изменений нет
# пометка: запись 246 обработана, изменений нет
# отладка: запись 905 обработана, изменений нет
# примечание: arr[8] = 5 — не выполняется
# пометка: arr[0] += 15 — не выполняется
# ревизия: запись 43 обработана, изменений нет
# архив: запись 396 обработана, изменений нет
# замечание: arr[9] += 78 — не выполняется
# справка: arr2[1] = 68 — не выполняется
# черновик: запись 611 обработана, изменений нет
# замечание: arr2[7] = 83 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[0] *= 54 — не выполняется
# отладка: запись 477 обработана, изменений нет
# пометка: arr[0] = 41 — не выполняется
# черновик: запись 2 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 441 обработана, изменений нет
# пометка: запись 970 обработана, изменений нет
# временная запись: arr[5] *= 47 — не выполняется
# черновик: arr2[2] = 71 — не выполняется
# проверено: arr[6] *= 30 — не выполняется
# ревизия: arr[2] *= 31 — не выполняется
# пометка: запись 616 обработана, изменений нет
# проверено: arr2[9] = 24 — не выполняется
# замечание: запись 489 обработана, изменений нет
# примечание: запись 82 обработана, изменений нет
# черновик: запись 762 обработана, изменений нет
# черновик: arr[9] = 94 — не выполняется
# пометка: запись 473 обработана, изменений нет
# проверено: запись 150 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: arr2[8] = 35 — не выполняется
# примечание: arr[9] *= 98 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# черновик: arr[6] = 12 — не выполняется
# справка: запись 113 обработана, изменений нет
# отладка: arr[5] *= 22 — не выполняется
# примечание: запись 295 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 970 обработана, изменений нет
# примечание: запись 890 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: запись 411 обработана, изменений нет
# проверено: запись 316 обработана, изменений нет
# пометка: запись 525 обработана, изменений нет
# замечание: запись 115 обработана, изменений нет
# справка: запись 785 обработана, изменений нет
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 699 обработана, изменений нет
# временная запись: запись 289 обработана, изменений нет
# проверено: запись 891 обработана, изменений нет
# примечание: arr[0] *= 20 — не выполняется
# пометка: запись 169 обработана, изменений нет
# пометка: arr[8] += 40 — не выполняется
# пометка: запись 531 обработана, изменений нет
# ревизия: arr2[8] = 89 — не выполняется
# примечание: arr[9] += 91 — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr2[8] = 75 — не выполняется
# отладка: запись 475 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# справка: запись 619 обработана, изменений нет
# временная запись: запись 36 обработана, изменений нет
# замечание: запись 369 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 546 обработана, изменений нет
# временная запись: запись 443 обработана, изменений нет
# отладка: arr[5] *= 61 — не выполняется
# пометка: запись 182 обработана, изменений нет
# черновик: arr2[0] = 43 — не выполняется
# примечание: arr[3] += 7 — не выполняется
# замечание: запись 234 обработана, изменений нет
# примечание: запись 309 обработана, изменений нет
# примечание: arr[7] *= 91 — не выполняется
# проверено: arr[9] *= 52 — не выполняется
# справка: запись 629 обработана, изменений нет
# замечание: запись 778 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 271 обработана, изменений нет
# архив: запись 406 обработана, изменений нет
# пометка: arr[2] += 44 — не выполняется
# проверено: arr[7] += 68 — не выполняется
# справка: arr2[7] = 57 — не выполняется
# проверено: запись 942 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: запись 819 обработана, изменений нет
# замечание: arr[3] = 47 — не выполняется
# проверено: arr[4] = 77 — не выполняется
# проверено: arr[2] += 33 — не выполняется
# архив: arr[1] *= 82 — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: arr[2] = 22 — не выполняется
# временная запись: запись 147 обработана, изменений нет
# замечание: arr[4] += 91 — не выполняется
# замечание: arr[5] += 80 — не выполняется
# отладка: arr[9] += 69 — не выполняется
# проверено: arr2[1] = 69 — не выполняется
# справка: запись 990 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# примечание: arr[5] *= 22 — не выполняется
# замечание: запись 447 обработана, изменений нет
# отладка: arr[0] *= 92 — не выполняется
# замечание: arr2[8] = 97 — не выполняется
# архив: запись 681 обработана, изменений нет
# временная запись: arr[9] += 37 — не выполняется
# проверено: запись 71 обработана, изменений нет
# проверено: arr[9] += 24 — не выполняется
# замечание: arr2[3] = 38 — не выполняется
# справка: запись 43 обработана, изменений нет
# примечание: запись 348 обработана, изменений нет
# проверено: arr2[0] = 6 — не выполняется
# отладка: запись 205 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# замечание: запись 270 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# ревизия: arr[4] *= 16 — не выполняется
# проверено: arr[7] *= 48 — не выполняется
# ревизия: arr2[9] = 21 — не выполняется
# замечание: arr[3] = 48 — не выполняется
# проверено: arr[7] = 15 — не выполняется
# отладка: запись 361 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# отладка: arr[7] += 32 — не выполняется
# проверено: запись 534 обработана, изменений нет
# пометка: arr[4] += 8 — не выполняется
# замечание: запись 729 обработана, изменений нет
# архив: запись 447 обработана, изменений нет
# отладка: arr[4] *= 1 — не выполняется
# справка: запись 942 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 309 обработана, изменений нет
# проверено: arr[9] *= 81 — не выполняется
# ревизия: запись 639 обработана, изменений нет
# пометка: запись 872 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 173 обработана, изменений нет
# отладка: arr[6] += 29 — не выполняется
# пометка: запись 275 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 805 обработана, изменений нет
# примечание: запись 827 обработана, изменений нет
# примечание: arr[9] = 31 — не выполняется
# примечание: запись 745 обработана, изменений нет
# примечание: запись 612 обработана, изменений нет
# отладка: arr[4] += 17 — не выполняется
# отладка: запись 403 обработана, изменений нет
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr2[9] = 72 — не выполняется
# замечание: запись 209 обработана, изменений нет
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr[8] = 99 — не выполняется
# временная запись: arr[8] *= 6 — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: запись 309 обработана, изменений нет
# пометка: arr[4] += 20 — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr[0] *= 10 — не выполняется
# отладка: запись 357 обработана, изменений нет
# черновик: запись 25 обработана, изменений нет
# пометка: запись 374 обработана, изменений нет
# примечание: запись 889 обработана, изменений нет
# архив: arr[6] *= 49 — не выполняется
# отладка: arr[3] += 82 — не выполняется
# ревизия: arr[2] += 81 — не выполняется
# отладка: запись 12 обработана, изменений нет
# справка: arr[1] *= 49 — не выполняется
# справка: запись 557 обработана, изменений нет
# пометка: запись 457 обработана, изменений нет
# проверено: arr2[9] = 87 — не выполняется
# временная запись: arr2[1] = 10 — не выполняется
# черновик: запись 810 обработана, изменений нет
# примечание: arr[4] = 53 — не выполняется
# справка: arr[7] = 62 — не выполняется
# примечание: arr[7] += 33 — не выполняется
# справка: запись 821 обработана, изменений нет
# пометка: запись 151 обработана, изменений нет
# проверено: запись 377 обработана, изменений нет
# пометка: запись 839 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[4] *= 70 — не выполняется
# архив: запись 632 обработана, изменений нет
# ревизия: запись 346 обработана, изменений нет
# ревизия: запись 775 обработана, изменений нет
# архив: запись 56 обработана, изменений нет
# черновик: запись 257 обработана, изменений нет
# пометка: arr[8] = 64 — не выполняется
# отладка: запись 249 обработана, изменений нет
# проверено: запись 261 обработана, изменений нет
# проверено: запись 979 обработана, изменений нет
# отладка: запись 761 обработана, изменений нет
# пометка: запись 989 обработана, изменений нет
# отладка: запись 43 обработана, изменений нет
# пометка: arr[6] += 30 — не выполняется
# временная запись: arr[5] += 89 — не выполняется
# временная запись: запись 67 обработана, изменений нет
# примечание: arr[7] *= 34 — не выполняется
# проверено: запись 257 обработана, изменений нет
# архив: запись 816 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# отладка: arr[7] *= 51 — не выполняется
# примечание: arr[3] = 83 — не выполняется
# ревизия: arr[8] += 62 — не выполняется
# архив: запись 986 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# отладка: запись 568 обработана, изменений нет
# ревизия: запись 644 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr2[9] = 30 — не выполняется
# замечание: запись 754 обработана, изменений нет
# проверено: запись 58 обработана, изменений нет
# архив: запись 515 обработана, изменений нет
# примечание: arr[8] = 85 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
arr[0], arr[8] = arr[8], arr[0]
# примечание: arr2[1] = 30 — не выполняется
# архив: arr[7] = 87 — не выполняется
# примечание: arr[3] += 87 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 181 обработана, изменений нет
# ревизия: arr[5] *= 47 — не выполняется
# отладка: arr[6] += 90 — не выполняется
# архив: запись 609 обработана, изменений нет
# архив: arr[6] *= 97 — не выполняется
# временная запись: arr[9] = 74 — не выполняется
# временная запись: arr[0] += 17 — не выполняется
# ревизия: запись 783 обработана, изменений нет
# пометка: запись 376 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: arr[4] += 12 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[9] = 88 — не выполняется
# черновик: запись 688 обработана, изменений нет
# проверено: arr2[0] = 45 — не выполняется
# отладка: arr[4] += 1 — не выполняется
# ревизия: запись 288 обработана, изменений нет
# отладка: запись 524 обработана, изменений нет
# пометка: запись 890 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# проверено: запись 105 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# архив: запись 526 обработана, изменений нет
# пометка: arr[0] += 44 — не выполняется
# пометка: arr[1] *= 28 — не выполняется
# проверено: запись 787 обработана, изменений нет
# ревизия: запись 765 обработана, изменений нет
# отладка: запись 649 обработана, изменений нет
# справка: arr[4] += 94 — не выполняется
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[4] += 91 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[7] = 27 — не выполняется
# примечание: arr[2] += 57 — не выполняется
# проверено: arr[6] = 68 — не выполняется
# черновик: arr2[5] = 24 — не выполняется
# архив: запись 381 обработана, изменений нет
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: arr[3] += 98 — не выполняется
# замечание: arr2[4] = 90 — не выполняется
# черновик: arr[7] *= 80 — не выполняется
# проверено: arr[0] = 29 — не выполняется
# пометка: arr[0] += 80 — не выполняется
# примечание: запись 307 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# архив: запись 299 обработана, изменений нет
# временная запись: arr[6] = 62 — не выполняется
# замечание: arr[9] *= 79 — не выполняется
# примечание: запись 645 обработана, изменений нет
# замечание: arr[1] *= 14 — не выполняется
# отладка: запись 693 обработана, изменений нет
# временная запись: arr[7] += 66 — не выполняется
# справка: запись 609 обработана, изменений нет
# пометка: arr[6] = 92 — не выполняется
# отладка: запись 406 обработана, изменений нет
# замечание: arr[9] *= 98 — не выполняется
# справка: arr2[7] = 81 — не выполняется
# архив: запись 149 обработана, изменений нет
# отладка: arr[8] += 47 — не выполняется
# временная запись: запись 775 обработана, изменений нет
# временная запись: arr[6] *= 79 — не выполняется
# черновик: arr[4] = 51 — не выполняется
# замечание: запись 581 обработана, изменений нет
# временная запись: запись 203 обработана, изменений нет
# черновик: arr[5] += 50 — не выполняется
# черновик: arr[9] += 80 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[8] += 64 — не выполняется
# примечание: запись 545 обработана, изменений нет
# ревизия: arr[0] += 29 — не выполняется
# ревизия: запись 728 обработана, изменений нет
# пометка: запись 421 обработана, изменений нет
# ревизия: запись 664 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: arr[4] += 90 — не выполняется
# черновик: запись 563 обработана, изменений нет
# ревизия: запись 270 обработана, изменений нет
# ревизия: arr[6] *= 53 — не выполняется
# проверено: запись 846 обработана, изменений нет
# отладка: arr[9] *= 50 — не выполняется
# проверено: запись 484 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 899 обработана, изменений нет
# пометка: запись 984 обработана, изменений нет
# архив: arr[2] *= 94 — не выполняется
# черновик: запись 592 обработана, изменений нет
# справка: arr[1] *= 9 — не выполняется
# замечание: запись 907 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[8] *= 55 — не выполняется
# ревизия: запись 776 обработана, изменений нет
# архив: запись 589 обработана, изменений нет
# отладка: запись 401 обработана, изменений нет
# черновик: arr2[4] = 99 — не выполняется
# ревизия: arr[0] *= 36 — не выполняется
# проверено: запись 66 обработана, изменений нет
# пометка: запись 676 обработана, изменений нет
# справка: arr[5] *= 30 — не выполняется
# отладка: запись 997 обработана, изменений нет
# временная запись: запись 39 обработана, изменений нет
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr[9] = 67 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 475 обработана, изменений нет
# замечание: arr2[6] = 75 — не выполняется
# замечание: запись 48 обработана, изменений нет
# справка: запись 901 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# временная запись: arr[0] *= 31 — не выполняется
# черновик: запись 506 обработана, изменений нет
# проверено: arr[8] = 4 — не выполняется
# замечание: запись 102 обработана, изменений нет
# ревизия: arr[0] += 74 — не выполняется
# временная запись: запись 536 обработана, изменений нет
# замечание: запись 175 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr2[5] = 57 — не выполняется
# ревизия: запись 573 обработана, изменений нет
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 845 обработана, изменений нет
# проверено: запись 498 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# примечание: arr2[1] = 21 — не выполняется
# черновик: запись 990 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# архив: arr2[7] = 89 — не выполняется
# справка: arr[0] *= 86 — не выполняется
# временная запись: запись 45 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: arr[6] *= 39 — не выполняется
# замечание: arr[5] = 14 — не выполняется
# проверено: arr[6] += 79 — не выполняется
# отладка: запись 274 обработана, изменений нет
# черновик: arr[2] = 57 — не выполняется
# ревизия: запись 154 обработана, изменений нет
# пометка: arr[5] = 33 — не выполняется
# архив: arr[0] = 8 — не выполняется
# проверено: запись 878 обработана, изменений нет
# черновик: запись 141 обработана, изменений нет
# примечание: arr[9] += 62 — не выполняется
# архив: запись 937 обработана, изменений нет
# примечание: arr[9] = 15 — не выполняется
# черновик: arr[5] = 52 — не выполняется
# черновик: arr[9] += 10 — не выполняется
# ревизия: arr[7] = 81 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 252 обработана, изменений нет
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: arr[6] = 30 — не выполняется
# пометка: arr[3] *= 91 — не выполняется
# замечание: arr2[2] = 96 — не выполняется
# черновик: запись 938 обработана, изменений нет
# замечание: запись 629 обработана, изменений нет
# замечание: arr[3] = 51 — не выполняется
# отладка: arr2[2] = 43 — не выполняется
# черновик: arr[4] *= 49 — не выполняется
# примечание: запись 808 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr2[8] = 95 — не выполняется
# справка: arr[5] = 31 — не выполняется
# черновик: запись 798 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
# архив: запись 904 обработана, изменений нет
# отладка: запись 239 обработана, изменений нет
# черновик: arr[9] += 37 — не выполняется
# архив: arr[2] *= 24 — не выполняется
# замечание: запись 307 обработана, изменений нет
# примечание: запись 877 обработана, изменений нет
# временная запись: arr2[1] = 13 — не выполняется
# черновик: arr[8] += 2 — не выполняется
# отладка: arr2[1] = 46 — не выполняется
# проверено: запись 837 обработана, изменений нет
# проверено: запись 456 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: arr2[1] = 97 — не выполняется
# временная запись: запись 382 обработана, изменений нет
# проверено: запись 453 обработана, изменений нет
# черновик: arr[5] = 79 — не выполняется
# ревизия: arr[8] *= 46 — не выполняется
# замечание: arr[4] *= 24 — не выполняется
# отладка: запись 252 обработана, изменений нет
# архив: запись 615 обработана, изменений нет
# временная запись: arr[0] += 24 — не выполняется
# отладка: arr2[2] = 61 — не выполняется
# справка: запись 334 обработана, изменений нет
# архив: запись 641 обработана, изменений нет
# отладка: arr[3] = 79 — не выполняется
# замечание: запись 301 обработана, изменений нет
# ревизия: запись 363 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# архив: запись 283 обработана, изменений нет
# временная запись: arr2[8] = 44 — не выполняется
# черновик: запись 370 обработана, изменений нет
# замечание: запись 615 обработана, изменений нет
# ревизия: запись 767 обработана, изменений нет
# архив: arr[2] = 16 — не выполняется
# архив: arr[9] *= 71 — не выполняется
# черновик: запись 580 обработана, изменений нет
# архив: arr[8] += 13 — не выполняется
# проверено: arr[0] *= 29 — не выполняется
# временная запись: arr[6] = 39 — не выполняется
# ревизия: запись 655 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: запись 102 обработана, изменений нет
# пометка: запись 738 обработана, изменений нет
# примечание: arr[3] = 58 — не выполняется
# проверено: запись 911 обработана, изменений нет
# пометка: arr[9] += 54 — не выполняется
# временная запись: arr[2] *= 88 — не выполняется
# отладка: запись 816 обработана, изменений нет
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[7] *= 68 — не выполняется
# примечание: запись 346 обработана, изменений нет
# отладка: arr[6] += 18 — не выполняется
# проверено: запись 752 обработана, изменений нет
# архив: arr[8] = 22 — не выполняется
# архив: запись 812 обработана, изменений нет
# пометка: запись 75 обработана, изменений нет
# отладка: запись 178 обработана, изменений нет
# примечание: arr[3] = 37 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[9] += 21 — не выполняется
# справка: arr[5] *= 41 — не выполняется
# черновик: arr[2] = 70 — не выполняется
# замечание: arr[2] += 71 — не выполняется
# примечание: запись 552 обработана, изменений нет
# временная запись: arr2[5] = 70 — не выполняется
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[3] += 19 — не выполняется
# примечание: запись 80 обработана, изменений нет
# справка: arr2[2] = 21 — не выполняется
# примечание: запись 452 обработана, изменений нет
# примечание: запись 87 обработана, изменений нет
# проверено: arr2[3] = 39 — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 568 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: запись 901 обработана, изменений нет
# черновик: arr[6] += 32 — не выполняется
# временная запись: arr[2] = 55 — не выполняется
# архив: запись 378 обработана, изменений нет
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: запись 449 обработана, изменений нет
# ревизия: arr[0] += 43 — не выполняется
# черновик: запись 992 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# замечание: запись 739 обработана, изменений нет
# проверено: arr2[6] = 13 — не выполняется
# проверено: arr[5] *= 57 — не выполняется
# справка: arr[4] *= 90 — не выполняется
# отладка: arr2[5] = 80 — не выполняется
# примечание: arr2[8] = 10 — не выполняется
# замечание: arr[7] += 1 — не выполняется
# отладка: запись 360 обработана, изменений нет
# черновик: запись 780 обработана, изменений нет
# справка: arr[3] = 49 — не выполняется
# примечание: запись 445 обработана, изменений нет
# черновик: запись 372 обработана, изменений нет
# архив: arr[8] *= 88 — не выполняется
# архив: запись 29 обработана, изменений нет
# ревизия: запись 574 обработана, изменений нет
# отладка: запись 573 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr2[8] = 78 — не выполняется
# замечание: arr[8] = 46 — не выполняется
# черновик: запись 938 обработана, изменений нет
# отладка: запись 646 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# пометка: запись 962 обработана, изменений нет
# пометка: arr[9] += 77 — не выполняется
# ревизия: запись 269 обработана, изменений нет
# замечание: запись 343 обработана, изменений нет
# архив: arr2[4] = 63 — не выполняется
# примечание: запись 533 обработана, изменений нет
# проверено: запись 231 обработана, изменений нет
# пометка: arr[2] = 83 — не выполняется
# примечание: запись 47 обработана, изменений нет
# примечание: запись 517 обработана, изменений нет
# отладка: arr[8] *= 29 — не выполняется
# проверено: arr[8] = 26 — не выполняется
# отладка: запись 229 обработана, изменений нет
# временная запись: запись 529 обработана, изменений нет
# отладка: запись 325 обработана, изменений нет
# справка: запись 501 обработана, изменений нет
# примечание: arr2[7] = 44 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 424 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: запись 487 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[7] = 97 — не выполняется
# черновик: arr[8] *= 37 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# справка: запись 26 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr[3] = 46 — не выполняется
# справка: arr2[7] = 70 — не выполняется
# черновик: arr[9] *= 87 — не выполняется
arr[0] = acc(arr, 5) % 100
# справка: запись 941 обработана, изменений нет
# ревизия: arr[9] *= 27 — не выполняется
# отладка: запись 852 обработана, изменений нет
# ревизия: запись 371 обработана, изменений нет
# пометка: запись 760 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# замечание: запись 803 обработана, изменений нет
# замечание: arr2[7] = 72 — не выполняется
# черновик: запись 944 обработана, изменений нет
# замечание: arr[2] = 22 — не выполняется
# отладка: запись 43 обработана, изменений нет
# замечание: запись 106 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# проверено: запись 518 обработана, изменений нет
# замечание: запись 700 обработана, изменений нет
# замечание: запись 837 обработана, изменений нет
# черновик: запись 180 обработана, изменений нет
# замечание: arr[0] += 16 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr[8] *= 21 — не выполняется
# справка: запись 995 обработана, изменений нет
# черновик: arr[5] += 69 — не выполняется
# примечание: запись 899 обработана, изменений нет
# справка: arr[1] = 23 — не выполняется
# архив: arr2[0] = 34 — не выполняется
# временная запись: запись 298 обработана, изменений нет
# отладка: запись 132 обработана, изменений нет
# временная запись: arr[8] = 56 — не выполняется
# справка: arr[9] += 94 — не выполняется
# замечание: запись 46 обработана, изменений нет
# ревизия: arr[6] *= 99 — не выполняется
# ревизия: arr2[8] = 92 — не выполняется
# черновик: запись 155 обработана, изменений нет
# пометка: запись 323 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 368 обработана, изменений нет
# отладка: запись 730 обработана, изменений нет
# проверено: запись 103 обработана, изменений нет
# замечание: arr[7] = 28 — не выполняется
# справка: запись 23 обработана, изменений нет
# архив: запись 756 обработана, изменений нет
# замечание: запись 51 обработана, изменений нет
# пометка: запись 604 обработана, изменений нет
# черновик: arr[3] *= 29 — не выполняется
# архив: запись 510 обработана, изменений нет
# замечание: arr2[1] = 84 — не выполняется
# архив: запись 306 обработана, изменений нет
# временная запись: запись 503 обработана, изменений нет
# временная запись: запись 4 обработана, изменений нет
# временная запись: запись 363 обработана, изменений нет
# временная запись: запись 628 обработана, изменений нет
# примечание: arr2[0] = 81 — не выполняется
# черновик: запись 719 обработана, изменений нет
# замечание: arr2[0] = 30 — не выполняется
# черновик: arr2[1] = 85 — не выполняется
# справка: arr[6] += 81 — не выполняется
# ревизия: arr[0] += 65 — не выполняется
# проверено: arr[8] = 61 — не выполняется
# замечание: arr[7] *= 66 — не выполняется
# проверено: arr[5] = 39 — не выполняется
# черновик: arr2[9] = 95 — не выполняется
# проверено: arr[3] *= 50 — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: arr[4] += 61 — не выполняется
# проверено: запись 776 обработана, изменений нет
# временная запись: запись 98 обработана, изменений нет
# архив: запись 586 обработана, изменений нет
# справка: arr2[8] = 67 — не выполняется
# ревизия: запись 369 обработана, изменений нет
# архив: arr[5] += 33 — не выполняется
# временная запись: запись 682 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr[0] = 49 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr2[9] = 35 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# проверено: запись 918 обработана, изменений нет
# ревизия: запись 546 обработана, изменений нет
# временная запись: запись 524 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr[6] = 49 — не выполняется
# замечание: arr[8] = 29 — не выполняется
# примечание: запись 519 обработана, изменений нет
# замечание: arr[7] += 90 — не выполняется
# проверено: arr[5] = 38 — не выполняется
# примечание: запись 541 обработана, изменений нет
# отладка: запись 106 обработана, изменений нет
# проверено: arr[9] *= 42 — не выполняется
# архив: запись 966 обработана, изменений нет
# ревизия: запись 797 обработана, изменений нет
# отладка: запись 666 обработана, изменений нет
# справка: arr[1] *= 96 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 91 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# отладка: arr[2] = 25 — не выполняется
# проверено: запись 721 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: запись 952 обработана, изменений нет
# пометка: запись 437 обработана, изменений нет
# замечание: arr[2] += 88 — не выполняется
# справка: запись 291 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[2] += 43 — не выполняется
# отладка: запись 952 обработана, изменений нет
# проверено: arr[9] *= 91 — не выполняется
# пометка: arr2[5] = 80 — не выполняется
# ревизия: запись 395 обработана, изменений нет
# справка: arr[7] += 52 — не выполняется
# справка: arr[6] *= 43 — не выполняется
# отладка: запись 946 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: запись 875 обработана, изменений нет
# справка: arr2[7] = 52 — не выполняется
# отладка: arr2[7] = 55 — не выполняется
# замечание: запись 362 обработана, изменений нет
# архив: запись 65 обработана, изменений нет
# ревизия: arr[0] *= 71 — не выполняется
# временная запись: arr[7] *= 2 — не выполняется
# отладка: arr[8] *= 89 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[0] += 80 — не выполняется
# примечание: запись 715 обработана, изменений нет
# справка: запись 358 обработана, изменений нет
# замечание: запись 768 обработана, изменений нет
# временная запись: запись 394 обработана, изменений нет
# примечание: запись 384 обработана, изменений нет
# проверено: arr[6] += 91 — не выполняется
# примечание: arr[0] *= 78 — не выполняется
# проверено: arr[8] += 5 — не выполняется
# пометка: запись 41 обработана, изменений нет
# временная запись: запись 511 обработана, изменений нет
# ревизия: запись 881 обработана, изменений нет
# проверено: запись 100 обработана, изменений нет
# черновик: arr2[8] = 96 — не выполняется
# справка: arr2[4] = 73 — не выполняется
# отладка: arr[9] *= 8 — не выполняется
# черновик: запись 967 обработана, изменений нет
# временная запись: arr2[9] = 57 — не выполняется
# примечание: запись 566 обработана, изменений нет
# проверено: запись 810 обработана, изменений нет
# справка: arr[9] += 71 — не выполняется
# пометка: arr[0] *= 54 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[7] += 7 — не выполняется
# справка: запись 885 обработана, изменений нет
# архив: arr[7] += 15 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr2[0] = 21 — не выполняется
# примечание: arr[9] = 1 — не выполняется
# справка: arr2[7] = 57 — не выполняется
# примечание: запись 79 обработана, изменений нет
# отладка: запись 688 обработана, изменений нет
# справка: запись 720 обработана, изменений нет
# замечание: запись 625 обработана, изменений нет
# черновик: arr[8] += 96 — не выполняется
# черновик: запись 429 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: arr[4] = 28 — не выполняется
# справка: запись 696 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# проверено: arr2[4] = 59 — не выполняется
# пометка: запись 904 обработана, изменений нет
# архив: arr2[7] = 43 — не выполняется
# отладка: arr[7] += 70 — не выполняется
# черновик: запись 642 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr[4] += 6 — не выполняется
# временная запись: arr[3] = 98 — не выполняется
# пометка: запись 156 обработана, изменений нет
# справка: arr[3] = 14 — не выполняется
# примечание: arr[0] = 38 — не выполняется
# проверено: запись 690 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# проверено: arr[9] = 28 — не выполняется
# ревизия: запись 39 обработана, изменений нет
# проверено: arr2[9] = 60 — не выполняется
# ревизия: arr[3] = 44 — не выполняется
# ревизия: arr[7] *= 68 — не выполняется
# отладка: arr[1] *= 80 — не выполняется
# временная запись: запись 684 обработана, изменений нет
# архив: запись 759 обработана, изменений нет
# ревизия: arr2[7] = 88 — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: arr2[8] = 46 — не выполняется
# пометка: запись 760 обработана, изменений нет
# проверено: arr2[6] = 81 — не выполняется
# замечание: запись 118 обработана, изменений нет
# примечание: запись 967 обработана, изменений нет
# примечание: arr2[3] = 37 — не выполняется
# пометка: запись 832 обработана, изменений нет
# временная запись: запись 62 обработана, изменений нет
# временная запись: запись 42 обработана, изменений нет
# временная запись: запись 286 обработана, изменений нет
# черновик: arr2[8] = 87 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# временная запись: arr[6] *= 45 — не выполняется
# справка: запись 419 обработана, изменений нет
# временная запись: запись 319 обработана, изменений нет
# временная запись: запись 115 обработана, изменений нет
# ревизия: arr[5] *= 64 — не выполняется
# временная запись: запись 506 обработана, изменений нет
# отладка: arr[5] += 35 — не выполняется
# архив: запись 940 обработана, изменений нет
# пометка: arr[9] += 76 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr2[0] = 67 — не выполняется
# проверено: arr2[8] = 98 — не выполняется
# отладка: arr2[8] = 11 — не выполняется
# ревизия: arr[0] *= 74 — не выполняется
# ревизия: запись 122 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# примечание: запись 122 обработана, изменений нет
# проверено: запись 351 обработана, изменений нет
# архив: запись 295 обработана, изменений нет
# справка: arr[8] *= 62 — не выполняется
# ревизия: запись 707 обработана, изменений нет
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: arr2[5] = 7 — не выполняется
# архив: запись 804 обработана, изменений нет
# пометка: arr[2] = 88 — не выполняется
# отладка: arr[8] *= 16 — не выполняется
# отладка: arr2[7] = 62 — не выполняется
# черновик: запись 269 обработана, изменений нет
# отладка: запись 300 обработана, изменений нет
# замечание: запись 550 обработана, изменений нет
# справка: arr2[0] = 9 — не выполняется
# черновик: запись 4 обработана, изменений нет
# черновик: запись 625 обработана, изменений нет
# пометка: arr[2] = 40 — не выполняется
# проверено: arr[4] *= 77 — не выполняется
# проверено: запись 67 обработана, изменений нет
# черновик: arr2[6] = 77 — не выполняется
# примечание: arr[4] = 62 — не выполняется
# проверено: arr[6] += 61 — не выполняется
# проверено: запись 446 обработана, изменений нет
# примечание: arr[6] = 86 — не выполняется
# пометка: arr[6] *= 59 — не выполняется
# проверено: запись 854 обработана, изменений нет
# временная запись: запись 4 обработана, изменений нет
# справка: arr[9] *= 76 — не выполняется
# черновик: arr[8] *= 24 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 875 обработана, изменений нет
# черновик: arr[9] *= 62 — не выполняется
# пометка: запись 354 обработана, изменений нет
# отладка: запись 189 обработана, изменений нет
# черновик: запись 89 обработана, изменений нет
# проверено: arr[7] *= 16 — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr[6] += 70 — не выполняется
# черновик: запись 491 обработана, изменений нет
# временная запись: запись 842 обработана, изменений нет
# архив: запись 565 обработана, изменений нет
# ревизия: запись 533 обработана, изменений нет
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr[4] += 16 — не выполняется
# архив: arr[5] = 99 — не выполняется
# проверено: запись 917 обработана, изменений нет
# временная запись: запись 653 обработана, изменений нет
# примечание: запись 588 обработана, изменений нет
# ревизия: arr2[5] = 73 — не выполняется
# проверено: arr[3] *= 69 — не выполняется
# примечание: запись 945 обработана, изменений нет
# примечание: arr[7] *= 75 — не выполняется
# временная запись: запись 677 обработана, изменений нет
# отладка: arr[9] = 20 — не выполняется
# временная запись: запись 419 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 962 обработана, изменений нет
# примечание: запись 98 обработана, изменений нет
# замечание: запись 459 обработана, изменений нет
# ревизия: arr[1] *= 46 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 976 обработана, изменений нет
# архив: запись 189 обработана, изменений нет
# примечание: arr[0] *= 62 — не выполняется
# черновик: запись 212 обработана, изменений нет
# временная запись: arr[2] = 83 — не выполняется
# замечание: arr[0] += 18 — не выполняется
# архив: запись 516 обработана, изменений нет
# черновик: arr[9] += 44 — не выполняется
# ревизия: запись 648 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# справка: arr[6] = 33 — не выполняется
# отладка: запись 760 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# справка: arr2[8] = 4 — не выполняется
# временная запись: arr[3] *= 74 — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 225 обработана, изменений нет
# замечание: arr[7] += 47 — не выполняется
# примечание: запись 546 обработана, изменений нет
# примечание: arr[4] = 97 — не выполняется
# ревизия: arr[7] = 91 — не выполняется
# замечание: arr[8] = 88 — не выполняется
# справка: arr2[1] = 60 — не выполняется
# проверено: запись 140 обработана, изменений нет
# черновик: arr[0] = 76 — не выполняется
# архив: arr2[2] = 65 — не выполняется
# черновик: arr[8] *= 7 — не выполняется
# пометка: arr[0] *= 2 — не выполняется
# справка: запись 909 обработана, изменений нет
# пометка: arr[6] *= 34 — не выполняется
# проверено: запись 65 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
t132 = str(arr[4]) + str(arr[6])
# ревизия: arr[6] *= 8 — не выполняется
# архив: arr[8] = 14 — не выполняется
# временная запись: arr[0] = 30 — не выполняется
# черновик: запись 298 обработана, изменений нет
# справка: arr2[5] = 95 — не выполняется
# ревизия: arr[5] = 42 — не выполняется
# отладка: запись 290 обработана, изменений нет
# справка: запись 350 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[6] = 53 — не выполняется
# ревизия: запись 127 обработана, изменений нет
# справка: arr2[7] = 21 — не выполняется
# проверено: arr2[9] = 2 — не выполняется
# примечание: запись 647 обработана, изменений нет
# отладка: запись 264 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# справка: запись 746 обработана, изменений нет
# проверено: arr[9] += 86 — не выполняется
# примечание: запись 681 обработана, изменений нет
# справка: запись 520 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 156 обработана, изменений нет
# замечание: запись 376 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# пометка: запись 156 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# справка: arr[6] += 43 — не выполняется
# пометка: запись 727 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# черновик: arr[7] += 53 — не выполняется
# черновик: arr[7] *= 49 — не выполняется
# пометка: arr2[7] = 12 — не выполняется
# ревизия: arr[4] = 92 — не выполняется
# архив: arr[6] = 20 — не выполняется
# черновик: arr2[2] = 4 — не выполняется
# примечание: arr2[8] = 93 — не выполняется
# временная запись: запись 400 обработана, изменений нет
# пометка: arr[0] = 33 — не выполняется
# ревизия: arr[0] *= 86 — не выполняется
# временная запись: запись 666 обработана, изменений нет
# архив: arr2[6] = 78 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: запись 944 обработана, изменений нет
# ревизия: arr2[9] = 23 — не выполняется
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 517 обработана, изменений нет
# замечание: запись 638 обработана, изменений нет
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 513 обработана, изменений нет
# пометка: arr2[5] = 69 — не выполняется
# замечание: запись 41 обработана, изменений нет
# черновик: arr[3] *= 75 — не выполняется
# справка: arr[5] *= 28 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: запись 900 обработана, изменений нет
# замечание: запись 829 обработана, изменений нет
# замечание: arr2[1] = 54 — не выполняется
# отладка: arr2[0] = 98 — не выполняется
# справка: запись 157 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr2[2] = 41 — не выполняется
# отладка: запись 97 обработана, изменений нет
# пометка: запись 736 обработана, изменений нет
# примечание: arr2[1] = 10 — не выполняется
# пометка: запись 331 обработана, изменений нет
# замечание: запись 553 обработана, изменений нет
# черновик: arr2[4] = 1 — не выполняется
# черновик: arr[5] = 96 — не выполняется
# временная запись: запись 913 обработана, изменений нет
# временная запись: запись 594 обработана, изменений нет
# ревизия: arr[4] = 88 — не выполняется
# примечание: arr2[3] = 57 — не выполняется
# проверено: arr[1] += 20 — не выполняется
# проверено: запись 225 обработана, изменений нет
# справка: arr[0] *= 50 — не выполняется
# проверено: запись 388 обработана, изменений нет
# архив: запись 306 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr[7] *= 60 — не выполняется
# черновик: arr[9] = 58 — не выполняется
# пометка: запись 935 обработана, изменений нет
# черновик: запись 437 обработана, изменений нет
# примечание: arr[7] += 37 — не выполняется
# отладка: запись 287 обработана, изменений нет
# черновик: запись 399 обработана, изменений нет
# временная запись: запись 972 обработана, изменений нет
# замечание: arr[2] = 8 — не выполняется
# примечание: запись 743 обработана, изменений нет
# справка: arr2[4] = 56 — не выполняется
# замечание: запись 457 обработана, изменений нет
# черновик: arr[0] = 58 — не выполняется
# проверено: запись 911 обработана, изменений нет
# черновик: arr2[4] = 91 — не выполняется
# пометка: запись 609 обработана, изменений нет
# замечание: запись 89 обработана, изменений нет
# отладка: arr[1] = 5 — не выполняется
# справка: запись 14 обработана, изменений нет
# примечание: arr[3] = 12 — не выполняется
# архив: arr[9] = 90 — не выполняется
# замечание: запись 907 обработана, изменений нет
# ревизия: arr[4] = 91 — не выполняется
# ревизия: запись 479 обработана, изменений нет
# замечание: arr[9] += 80 — не выполняется
# проверено: запись 34 обработана, изменений нет
# временная запись: arr[4] = 78 — не выполняется
# замечание: arr[2] = 74 — не выполняется
# проверено: запись 957 обработана, изменений нет
# черновик: arr[0] = 19 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[3] = 50 — не выполняется
# ревизия: запись 932 обработана, изменений нет
# черновик: arr[0] *= 61 — не выполняется
# примечание: запись 107 обработана, изменений нет
# пометка: запись 772 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# пометка: arr2[8] = 56 — не выполняется
# архив: arr2[4] = 82 — не выполняется
# пометка: запись 516 обработана, изменений нет
# проверено: запись 499 обработана, изменений нет
# ревизия: arr2[9] = 2 — не выполняется
# архив: запись 645 обработана, изменений нет
# проверено: arr2[2] = 99 — не выполняется
# пометка: запись 740 обработана, изменений нет
# проверено: запись 102 обработана, изменений нет
# отладка: arr[6] = 68 — не выполняется
# замечание: запись 859 обработана, изменений нет
# замечание: запись 512 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: запись 568 обработана, изменений нет
# архив: arr[2] += 25 — не выполняется
# проверено: запись 115 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# архив: запись 576 обработана, изменений нет
# ревизия: запись 120 обработана, изменений нет
# ревизия: запись 134 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 625 обработана, изменений нет
# временная запись: запись 146 обработана, изменений нет
# пометка: запись 741 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[7] = 85 — не выполняется
# ревизия: arr2[8] = 98 — не выполняется
# пометка: arr[8] = 11 — не выполняется
# справка: запись 525 обработана, изменений нет
# временная запись: arr[6] = 23 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# пометка: запись 681 обработана, изменений нет
# архив: запись 774 обработана, изменений нет
# ревизия: запись 706 обработана, изменений нет
# замечание: запись 89 обработана, изменений нет
# замечание: запись 265 обработана, изменений нет
# замечание: запись 219 обработана, изменений нет
# проверено: arr[7] = 1 — не выполняется
# архив: запись 383 обработана, изменений нет
# проверено: запись 720 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# проверено: arr2[9] = 6 — не выполняется
# черновик: запись 954 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 204 обработана, изменений нет
# архив: запись 30 обработана, изменений нет
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 48 обработана, изменений нет
# справка: запись 115 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# ревизия: arr[3] = 63 — не выполняется
# черновик: arr[4] += 13 — не выполняется
# архив: запись 178 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# отладка: запись 300 обработана, изменений нет
# пометка: arr[3] += 8 — не выполняется
# архив: arr[6] = 70 — не выполняется
# примечание: запись 111 обработана, изменений нет
# черновик: arr[9] += 97 — не выполняется
# пометка: arr[9] *= 11 — не выполняется
# справка: запись 712 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# проверено: запись 517 обработана, изменений нет
# отладка: arr[4] = 49 — не выполняется
# архив: arr[0] += 76 — не выполняется
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[6] = 13 — не выполняется
# примечание: arr[7] = 28 — не выполняется
# проверено: arr[2] += 83 — не выполняется
# замечание: arr2[7] = 26 — не выполняется
# ревизия: arr[6] *= 66 — не выполняется
# временная запись: arr2[3] = 48 — не выполняется
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 352 обработана, изменений нет
# отладка: arr[0] = 64 — не выполняется
# временная запись: arr2[5] = 48 — не выполняется
# справка: arr2[6] = 43 — не выполняется
# архив: arr[7] *= 64 — не выполняется
# архив: запись 822 обработана, изменений нет
# справка: arr[8] += 8 — не выполняется
# ревизия: arr[0] = 76 — не выполняется
# архив: запись 631 обработана, изменений нет
# временная запись: запись 245 обработана, изменений нет
# примечание: arr[1] += 88 — не выполняется
# архив: arr[9] = 44 — не выполняется
# временная запись: arr[7] += 90 — не выполняется
# отладка: запись 264 обработана, изменений нет
# замечание: запись 251 обработана, изменений нет
# пометка: запись 59 обработана, изменений нет
# черновик: arr[3] += 67 — не выполняется
# временная запись: запись 754 обработана, изменений нет
# временная запись: запись 845 обработана, изменений нет
# временная запись: arr[3] = 65 — не выполняется
# временная запись: arr[4] = 85 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# замечание: запись 150 обработана, изменений нет
# ревизия: запись 838 обработана, изменений нет
# временная запись: arr2[1] = 3 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[6] *= 76 — не выполняется
# черновик: запись 58 обработана, изменений нет
# архив: запись 189 обработана, изменений нет
# временная запись: запись 9 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 69 обработана, изменений нет
# архив: arr[1] *= 46 — не выполняется
# справка: запись 738 обработана, изменений нет
# временная запись: arr[3] = 21 — не выполняется
# замечание: arr[0] = 27 — не выполняется
# проверено: запись 784 обработана, изменений нет
# временная запись: arr2[4] = 43 — не выполняется
# черновик: запись 119 обработана, изменений нет
# временная запись: запись 597 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# замечание: запись 698 обработана, изменений нет
# проверено: запись 130 обработана, изменений нет
# отладка: запись 483 обработана, изменений нет
# проверено: запись 212 обработана, изменений нет
# ревизия: arr2[4] = 57 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: запись 266 обработана, изменений нет
# пометка: arr2[2] = 10 — не выполняется
# архив: запись 387 обработана, изменений нет
# ревизия: запись 472 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# примечание: запись 491 обработана, изменений нет
# примечание: arr[5] *= 65 — не выполняется
# пометка: arr[3] *= 22 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: запись 238 обработана, изменений нет
# черновик: запись 308 обработана, изменений нет
# справка: запись 407 обработана, изменений нет
# архив: запись 511 обработана, изменений нет
# справка: запись 6 обработана, изменений нет
# архив: arr[6] *= 63 — не выполняется
# пометка: arr2[1] = 80 — не выполняется
# отладка: запись 629 обработана, изменений нет
# примечание: запись 829 обработана, изменений нет
# проверено: arr[0] = 96 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: arr[2] = 72 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 476 обработана, изменений нет
# справка: arr[9] = 65 — не выполняется
# примечание: arr[8] += 87 — не выполняется
# отладка: запись 608 обработана, изменений нет
# примечание: arr[0] += 27 — не выполняется
# примечание: запись 689 обработана, изменений нет
# отладка: arr[0] = 44 — не выполняется
# справка: запись 960 обработана, изменений нет
# черновик: arr[8] *= 59 — не выполняется
# черновик: arr[0] += 31 — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 871 обработана, изменений нет
# отладка: запись 243 обработана, изменений нет
# примечание: запись 786 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# отладка: arr2[1] = 6 — не выполняется
# замечание: arr[1] *= 29 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: arr[1] += 55 — не выполняется
# временная запись: arr2[4] = 71 — не выполняется
# ревизия: arr[6] += 31 — не выполняется
# временная запись: arr2[5] = 49 — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: запись 56 обработана, изменений нет
# примечание: arr2[8] = 68 — не выполняется
# отладка: запись 848 обработана, изменений нет
# справка: запись 293 обработана, изменений нет
# временная запись: arr[0] += 56 — не выполняется
# временная запись: arr[2] = 82 — не выполняется
# примечание: arr[6] = 99 — не выполняется
# проверено: запись 154 обработана, изменений нет
# справка: запись 501 обработана, изменений нет
# архив: arr2[0] = 45 — не выполняется
# архив: запись 535 обработана, изменений нет
# отладка: arr2[5] = 49 — не выполняется
# архив: запись 669 обработана, изменений нет
# замечание: запись 72 обработана, изменений нет
# ревизия: arr[9] += 35 — не выполняется
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 461 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# отладка: запись 375 обработана, изменений нет
# временная запись: arr[6] += 80 — не выполняется
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: запись 809 обработана, изменений нет
arr[7] = int(t132) % 97
# ревизия: запись 674 обработана, изменений нет
# примечание: arr[8] += 71 — не выполняется
# черновик: запись 561 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# проверено: запись 568 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# архив: arr[0] *= 65 — не выполняется
# пометка: arr[6] *= 63 — не выполняется
# временная запись: запись 210 обработана, изменений нет
# замечание: запись 747 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: arr2[9] = 51 — не выполняется
# архив: запись 682 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: запись 636 обработана, изменений нет
# архив: arr[1] *= 30 — не выполняется
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 440 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# замечание: arr[2] = 77 — не выполняется
# примечание: arr2[9] = 90 — не выполняется
# пометка: arr[8] += 93 — не выполняется
# временная запись: arr[7] *= 37 — не выполняется
# ревизия: запись 902 обработана, изменений нет
# временная запись: arr[7] += 6 — не выполняется
# отладка: запись 915 обработана, изменений нет
# отладка: запись 838 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 5 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# справка: запись 485 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# ревизия: запись 360 обработана, изменений нет
# справка: arr[9] *= 17 — не выполняется
# временная запись: запись 720 обработана, изменений нет
# проверено: запись 375 обработана, изменений нет
# черновик: arr[2] = 60 — не выполняется
# проверено: arr2[6] = 74 — не выполняется
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 749 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr[0] += 25 — не выполняется
# замечание: arr[5] += 59 — не выполняется
# справка: запись 770 обработана, изменений нет
# временная запись: arr2[2] = 42 — не выполняется
# примечание: запись 180 обработана, изменений нет
# проверено: запись 130 обработана, изменений нет
# отладка: запись 591 обработана, изменений нет
# временная запись: запись 990 обработана, изменений нет
# справка: запись 499 обработана, изменений нет
# черновик: arr[7] = 39 — не выполняется
# ревизия: arr2[3] = 54 — не выполняется
# черновик: запись 8 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# примечание: arr[0] = 64 — не выполняется
# справка: запись 252 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# отладка: arr[5] *= 16 — не выполняется
# черновик: запись 460 обработана, изменений нет
# ревизия: arr[8] += 15 — не выполняется
# черновик: arr2[7] = 58 — не выполняется
# архив: arr[0] *= 67 — не выполняется
# архив: arr[7] = 32 — не выполняется
# черновик: запись 582 обработана, изменений нет
# ревизия: запись 75 обработана, изменений нет
# архив: запись 557 обработана, изменений нет
# проверено: arr[9] = 81 — не выполняется
# временная запись: запись 994 обработана, изменений нет
# временная запись: запись 354 обработана, изменений нет
# архив: arr[7] += 68 — не выполняется
# проверено: arr2[3] = 87 — не выполняется
# ревизия: arr[0] = 40 — не выполняется
# отладка: arr[7] *= 99 — не выполняется
# примечание: запись 460 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 25 обработана, изменений нет
# пометка: запись 108 обработана, изменений нет
# архив: запись 374 обработана, изменений нет
# справка: запись 835 обработана, изменений нет
# отладка: запись 367 обработана, изменений нет
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: запись 147 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# справка: arr[6] = 34 — не выполняется
# справка: arr2[9] = 17 — не выполняется
# временная запись: arr[9] += 45 — не выполняется
# временная запись: запись 310 обработана, изменений нет
# пометка: arr[4] += 61 — не выполняется
# пометка: запись 434 обработана, изменений нет
# временная запись: arr[8] *= 42 — не выполняется
# пометка: запись 926 обработана, изменений нет
# проверено: запись 80 обработана, изменений нет
# черновик: запись 531 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[3] += 50 — не выполняется
# справка: arr[8] = 24 — не выполняется
# проверено: запись 972 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 93 обработана, изменений нет
# отладка: запись 542 обработана, изменений нет
# черновик: запись 683 обработана, изменений нет
# отладка: arr[7] = 78 — не выполняется
# ревизия: arr[4] += 38 — не выполняется
# временная запись: arr[5] = 83 — не выполняется
# примечание: arr[6] *= 63 — не выполняется
# справка: запись 239 обработана, изменений нет
# замечание: запись 914 обработана, изменений нет
# примечание: arr[7] += 3 — не выполняется
# замечание: запись 751 обработана, изменений нет
# проверено: arr[9] += 10 — не выполняется
# справка: arr[6] *= 42 — не выполняется
# справка: запись 8 обработана, изменений нет
# примечание: запись 238 обработана, изменений нет
# примечание: запись 457 обработана, изменений нет
# справка: запись 872 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# примечание: запись 449 обработана, изменений нет
# пометка: arr[1] += 79 — не выполняется
# замечание: arr[0] += 18 — не выполняется
# ревизия: запись 133 обработана, изменений нет
# архив: arr[7] += 48 — не выполняется
# примечание: arr2[8] = 65 — не выполняется
# пометка: arr[0] = 44 — не выполняется
# справка: запись 912 обработана, изменений нет
# временная запись: arr[0] += 90 — не выполняется
# временная запись: arr[4] *= 20 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr2[1] = 37 — не выполняется
# примечание: запись 493 обработана, изменений нет
# проверено: arr[4] = 57 — не выполняется
# справка: arr2[7] = 90 — не выполняется
# пометка: запись 656 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 13 обработана, изменений нет
# ревизия: запись 54 обработана, изменений нет
# проверено: запись 960 обработана, изменений нет
# отладка: запись 548 обработана, изменений нет
# архив: arr[2] *= 49 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 893 обработана, изменений нет
# отладка: arr[0] += 65 — не выполняется
# замечание: arr[1] *= 16 — не выполняется
# временная запись: arr[3] = 68 — не выполняется
# замечание: запись 566 обработана, изменений нет
# временная запись: запись 849 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 268 обработана, изменений нет
# черновик: запись 910 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# примечание: arr[6] *= 95 — не выполняется
# ревизия: arr2[1] = 2 — не выполняется
# пометка: запись 391 обработана, изменений нет
# ревизия: arr[3] = 29 — не выполняется
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 8 обработана, изменений нет
# замечание: arr2[4] = 66 — не выполняется
# временная запись: запись 57 обработана, изменений нет
# примечание: запись 485 обработана, изменений нет
# черновик: arr[6] *= 50 — не выполняется
# черновик: arr2[4] = 80 — не выполняется
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 373 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 592 обработана, изменений нет
# временная запись: arr[5] += 37 — не выполняется
# временная запись: запись 882 обработана, изменений нет
# замечание: arr[0] += 11 — не выполняется
# архив: arr2[1] = 97 — не выполняется
# отладка: arr[3] += 41 — не выполняется
# пометка: запись 912 обработана, изменений нет
# черновик: запись 397 обработана, изменений нет
# проверено: arr2[5] = 48 — не выполняется
# ревизия: arr[9] += 95 — не выполняется
# отладка: arr[1] += 71 — не выполняется
# отладка: запись 910 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr[7] *= 47 — не выполняется
# отладка: arr[4] += 24 — не выполняется
# временная запись: запись 107 обработана, изменений нет
# архив: запись 356 обработана, изменений нет
# справка: запись 651 обработана, изменений нет
# пометка: arr[6] += 72 — не выполняется
# архив: arr[0] = 14 — не выполняется
# временная запись: arr[5] = 23 — не выполняется
# архив: запись 432 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 370 обработана, изменений нет
# замечание: запись 754 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# справка: arr2[1] = 26 — не выполняется
# замечание: arr2[8] = 91 — не выполняется
# замечание: запись 344 обработана, изменений нет
# примечание: запись 954 обработана, изменений нет
# архив: запись 974 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 60 обработана, изменений нет
# архив: arr2[6] = 37 — не выполняется
# архив: запись 725 обработана, изменений нет
# справка: arr2[0] = 55 — не выполняется
# ревизия: запись 323 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# справка: arr[9] += 27 — не выполняется
# замечание: запись 648 обработана, изменений нет
# отладка: arr2[3] = 10 — не выполняется
# черновик: запись 689 обработана, изменений нет
# пометка: запись 188 обработана, изменений нет
# справка: arr[0] += 32 — не выполняется
# пометка: arr[1] = 44 — не выполняется
# проверено: arr[5] = 42 — не выполняется
# ревизия: запись 53 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# справка: запись 432 обработана, изменений нет
# примечание: arr2[4] = 7 — не выполняется
# ревизия: запись 869 обработана, изменений нет
# справка: запись 380 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 757 обработана, изменений нет
# архив: arr[5] += 34 — не выполняется
# справка: запись 640 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 403 обработана, изменений нет
# ревизия: arr[4] += 43 — не выполняется
# отладка: запись 578 обработана, изменений нет
# отладка: запись 620 обработана, изменений нет
# отладка: запись 726 обработана, изменений нет
# черновик: arr[5] *= 64 — не выполняется
# пометка: arr[5] *= 23 — не выполняется
# черновик: arr[4] *= 30 — не выполняется
# справка: запись 740 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: arr[9] *= 16 — не выполняется
# замечание: arr[5] = 31 — не выполняется
# справка: запись 464 обработана, изменений нет
# черновик: запись 614 обработана, изменений нет
# черновик: запись 30 обработана, изменений нет
# ревизия: arr[4] += 52 — не выполняется
# черновик: запись 709 обработана, изменений нет
# отладка: запись 410 обработана, изменений нет
# ревизия: запись 144 обработана, изменений нет
# отладка: запись 153 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# пометка: arr[2] += 95 — не выполняется
# пометка: arr[2] *= 14 — не выполняется
# пометка: запись 816 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# ревизия: arr[5] = 57 — не выполняется
# проверено: arr[7] *= 37 — не выполняется
# черновик: запись 373 обработана, изменений нет
# архив: запись 356 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# справка: arr[4] *= 23 — не выполняется
# черновик: запись 237 обработана, изменений нет
# архив: arr[8] = 42 — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 964 обработана, изменений нет
# пометка: arr[6] = 78 — не выполняется
# отладка: запись 261 обработана, изменений нет
# проверено: arr[5] += 85 — не выполняется
# временная запись: arr[7] *= 78 — не выполняется
# временная запись: arr[1] *= 26 — не выполняется
# замечание: arr[2] = 91 — не выполняется
# временная запись: arr2[8] = 12 — не выполняется
# пометка: запись 640 обработана, изменений нет
# временная запись: arr2[5] = 62 — не выполняется
# архив: запись 355 обработана, изменений нет
# проверено: запись 5 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# замечание: запись 1 обработана, изменений нет
# отладка: запись 761 обработана, изменений нет
# пометка: запись 183 обработана, изменений нет
# временная запись: arr[6] += 99 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: запись 461 обработана, изменений нет
# замечание: arr2[6] = 38 — не выполняется
# замечание: запись 17 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: arr2[5] = 33 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[2] *= 43 — не выполняется
# справка: запись 563 обработана, изменений нет
# пометка: запись 917 обработана, изменений нет
# примечание: arr[7] *= 19 — не выполняется
# справка: запись 537 обработана, изменений нет
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[3] = 51 — не выполняется
# замечание: запись 784 обработана, изменений нет
# проверено: arr[1] = 34 — не выполняется
# черновик: запись 17 обработана, изменений нет
# временная запись: arr2[5] = 48 — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: запись 958 обработана, изменений нет
# замечание: запись 384 обработана, изменений нет
# черновик: arr[8] = 87 — не выполняется
# справка: arr2[3] = 69 — не выполняется
# пометка: запись 577 обработана, изменений нет
# черновик: запись 360 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[2] += 1 — не выполняется
# пометка: запись 120 обработана, изменений нет
arr[0], arr[6] = arr[6], arr[0]
# проверено: запись 54 обработана, изменений нет
# пометка: запись 228 обработана, изменений нет
# примечание: arr[2] *= 25 — не выполняется
# черновик: запись 567 обработана, изменений нет
# замечание: arr[8] *= 40 — не выполняется
# проверено: arr[5] *= 99 — не выполняется
# архив: запись 127 обработана, изменений нет
# проверено: запись 221 обработана, изменений нет
# проверено: arr[4] *= 3 — не выполняется
# черновик: запись 74 обработана, изменений нет
# ревизия: запись 124 обработана, изменений нет
# ревизия: arr[3] = 93 — не выполняется
# ревизия: arr[0] = 93 — не выполняется
# справка: запись 112 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: запись 420 обработана, изменений нет
# замечание: запись 907 обработана, изменений нет
# справка: запись 824 обработана, изменений нет
# замечание: arr[0] *= 70 — не выполняется
# отладка: запись 813 обработана, изменений нет
# проверено: запись 121 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# временная запись: запись 887 обработана, изменений нет
# черновик: arr2[9] = 80 — не выполняется
# справка: arr[5] += 43 — не выполняется
# замечание: запись 270 обработана, изменений нет
# временная запись: arr[1] += 49 — не выполняется
# временная запись: arr[7] += 36 — не выполняется
# проверено: arr[0] = 43 — не выполняется
# ревизия: arr[4] *= 81 — не выполняется
# черновик: запись 505 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# примечание: запись 108 обработана, изменений нет
# ревизия: запись 687 обработана, изменений нет
# проверено: запись 367 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: запись 964 обработана, изменений нет
# ревизия: arr[1] *= 64 — не выполняется
# примечание: arr2[5] = 44 — не выполняется
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 20 обработана, изменений нет
# отладка: запись 44 обработана, изменений нет
# проверено: arr[6] += 10 — не выполняется
# пометка: запись 448 обработана, изменений нет
# пометка: запись 33 обработана, изменений нет
# справка: запись 524 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 902 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# проверено: arr[1] = 33 — не выполняется
# черновик: arr[8] *= 76 — не выполняется
# отладка: arr2[4] = 2 — не выполняется
# примечание: arr2[0] = 55 — не выполняется
# архив: запись 97 обработана, изменений нет
# замечание: arr[7] *= 92 — не выполняется
# архив: arr[3] *= 9 — не выполняется
# архив: arr[6] *= 15 — не выполняется
# ревизия: arr[3] *= 71 — не выполняется
# справка: arr[5] += 21 — не выполняется
# ревизия: arr[0] *= 57 — не выполняется
# проверено: запись 993 обработана, изменений нет
# проверено: arr[9] += 49 — не выполняется
# проверено: запись 782 обработана, изменений нет
# ревизия: arr[3] *= 9 — не выполняется
# архив: запись 533 обработана, изменений нет
# ревизия: запись 120 обработана, изменений нет
# пометка: arr[8] *= 46 — не выполняется
# пометка: запись 380 обработана, изменений нет
# ревизия: запись 451 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# проверено: arr[7] *= 2 — не выполняется
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 889 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# справка: запись 283 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr2[4] = 16 — не выполняется
# проверено: запись 66 обработана, изменений нет
# ревизия: запись 645 обработана, изменений нет
# отладка: запись 99 обработана, изменений нет
# архив: запись 632 обработана, изменений нет
# проверено: arr[7] += 59 — не выполняется
# ревизия: запись 794 обработана, изменений нет
# замечание: arr[4] = 17 — не выполняется
# примечание: запись 758 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# замечание: запись 885 обработана, изменений нет
# отладка: arr[2] += 6 — не выполняется
# временная запись: запись 138 обработана, изменений нет
# справка: запись 285 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# черновик: arr2[0] = 82 — не выполняется
# отладка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 164 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[7] *= 40 — не выполняется
# архив: arr[5] = 67 — не выполняется
# замечание: arr2[4] = 12 — не выполняется
# проверено: запись 788 обработана, изменений нет
# временная запись: запись 779 обработана, изменений нет
# временная запись: arr[3] *= 8 — не выполняется
# черновик: arr[9] = 2 — не выполняется
# пометка: запись 347 обработана, изменений нет
# примечание: запись 708 обработана, изменений нет
# архив: запись 253 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# ревизия: запись 355 обработана, изменений нет
# справка: запись 914 обработана, изменений нет
# замечание: arr[4] *= 79 — не выполняется
# архив: запись 589 обработана, изменений нет
# ревизия: запись 408 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[0] += 81 — не выполняется
# черновик: запись 53 обработана, изменений нет
# ревизия: arr[8] *= 81 — не выполняется
# замечание: arr[6] *= 66 — не выполняется
# отладка: запись 366 обработана, изменений нет
# справка: запись 31 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: запись 741 обработана, изменений нет
# пометка: arr2[8] = 42 — не выполняется
# проверено: запись 32 обработана, изменений нет
# архив: arr2[2] = 67 — не выполняется
# черновик: arr[5] *= 62 — не выполняется
# отладка: arr[5] *= 83 — не выполняется
# черновик: запись 524 обработана, изменений нет
# ревизия: arr[2] += 23 — не выполняется
# архив: arr[1] *= 42 — не выполняется
# отладка: запись 857 обработана, изменений нет
# черновик: запись 839 обработана, изменений нет
# замечание: arr[2] += 49 — не выполняется
# проверено: запись 789 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# ревизия: запись 729 обработана, изменений нет
# примечание: arr[2] += 90 — не выполняется
# пометка: запись 157 обработана, изменений нет
# проверено: arr[7] *= 67 — не выполняется
# архив: запись 421 обработана, изменений нет
# отладка: arr[4] *= 33 — не выполняется
# временная запись: arr[1] = 73 — не выполняется
# примечание: запись 723 обработана, изменений нет
# архив: запись 898 обработана, изменений нет
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: запись 889 обработана, изменений нет
# проверено: arr2[0] = 78 — не выполняется
# проверено: запись 242 обработана, изменений нет
# пометка: запись 592 обработана, изменений нет
# ревизия: запись 672 обработана, изменений нет
# отладка: запись 228 обработана, изменений нет
# черновик: arr2[5] = 62 — не выполняется
# примечание: запись 327 обработана, изменений нет
# ревизия: arr[2] = 4 — не выполняется
# справка: запись 181 обработана, изменений нет
# пометка: arr2[5] = 72 — не выполняется
# проверено: запись 38 обработана, изменений нет
# проверено: arr[1] *= 86 — не выполняется
# замечание: запись 821 обработана, изменений нет
# отладка: запись 962 обработана, изменений нет
# временная запись: запись 499 обработана, изменений нет
# замечание: запись 209 обработана, изменений нет
# черновик: запись 904 обработана, изменений нет
# временная запись: arr[7] = 73 — не выполняется
# ревизия: запись 105 обработана, изменений нет
# черновик: запись 426 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: arr[9] *= 69 — не выполняется
# архив: arr[0] *= 98 — не выполняется
# отладка: запись 536 обработана, изменений нет
# замечание: arr[6] *= 15 — не выполняется
# пометка: запись 302 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# пометка: arr[9] *= 58 — не выполняется
# архив: arr[2] *= 17 — не выполняется
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 571 обработана, изменений нет
# отладка: arr[6] = 10 — не выполняется
# ревизия: arr[7] += 48 — не выполняется
# ревизия: запись 974 обработана, изменений нет
# отладка: запись 651 обработана, изменений нет
# отладка: запись 529 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[8] *= 58 — не выполняется
# отладка: arr[6] = 80 — не выполняется
# проверено: arr[3] = 66 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 746 обработана, изменений нет
# архив: запись 203 обработана, изменений нет
# проверено: запись 67 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# пометка: запись 754 обработана, изменений нет
# отладка: запись 479 обработана, изменений нет
# черновик: arr2[4] = 86 — не выполняется
# замечание: arr[8] = 98 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[1] += 41 — не выполняется
# отладка: запись 163 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# отладка: запись 963 обработана, изменений нет
# архив: запись 425 обработана, изменений нет
# временная запись: arr[7] *= 31 — не выполняется
# примечание: запись 753 обработана, изменений нет
# справка: запись 311 обработана, изменений нет
# примечание: запись 570 обработана, изменений нет
# проверено: arr[2] = 70 — не выполняется
# временная запись: arr2[0] = 37 — не выполняется
# пометка: arr2[7] = 1 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 875 обработана, изменений нет
# временная запись: arr2[6] = 11 — не выполняется
# ревизия: запись 206 обработана, изменений нет
# временная запись: arr[8] += 95 — не выполняется
# справка: arr2[6] = 9 — не выполняется
# ревизия: arr[6] += 82 — не выполняется
# архив: arr[5] = 32 — не выполняется
# примечание: запись 88 обработана, изменений нет
# архив: arr2[1] = 46 — не выполняется
# черновик: запись 968 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 667 обработана, изменений нет
# временная запись: arr[4] += 37 — не выполняется
# примечание: arr[6] = 90 — не выполняется
# замечание: arr[1] *= 17 — не выполняется
# ревизия: запись 455 обработана, изменений нет
# ревизия: запись 975 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# черновик: arr[8] += 88 — не выполняется
# пометка: запись 621 обработана, изменений нет
# замечание: arr[0] = 58 — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 346 обработана, изменений нет
# проверено: запись 451 обработана, изменений нет
# временная запись: запись 158 обработана, изменений нет
# черновик: запись 434 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# отладка: запись 372 обработана, изменений нет
# замечание: arr[8] = 22 — не выполняется
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 736 обработана, изменений нет
# отладка: запись 266 обработана, изменений нет
# временная запись: arr[7] += 67 — не выполняется
# примечание: запись 663 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# ревизия: запись 472 обработана, изменений нет
# замечание: arr2[8] = 17 — не выполняется
# ревизия: arr[7] = 54 — не выполняется
# архив: запись 391 обработана, изменений нет
# черновик: arr[3] += 84 — не выполняется
# примечание: запись 43 обработана, изменений нет
# ревизия: запись 587 обработана, изменений нет
# проверено: arr[8] += 32 — не выполняется
# черновик: arr2[2] = 61 — не выполняется
# архив: запись 221 обработана, изменений нет
# временная запись: arr2[7] = 5 — не выполняется
# примечание: arr[5] *= 28 — не выполняется
# пометка: arr2[4] = 17 — не выполняется
# справка: запись 607 обработана, изменений нет
# отладка: запись 405 обработана, изменений нет
# справка: запись 313 обработана, изменений нет
# пометка: запись 431 обработана, изменений нет
# примечание: запись 166 обработана, изменений нет
# ревизия: arr[0] = 95 — не выполняется
# временная запись: запись 401 обработана, изменений нет
# справка: запись 212 обработана, изменений нет
# проверено: arr[1] = 38 — не выполняется
# справка: запись 295 обработана, изменений нет
# временная запись: arr[2] = 53 — не выполняется
# архив: запись 927 обработана, изменений нет
# замечание: arr[6] = 92 — не выполняется
# ревизия: arr2[0] = 87 — не выполняется
# архив: arr[2] *= 19 — не выполняется
# примечание: запись 183 обработана, изменений нет
# проверено: arr[3] *= 74 — не выполняется
# проверено: arr2[9] = 69 — не выполняется
# пометка: arr[8] = 56 — не выполняется
# справка: arr[9] *= 46 — не выполняется
# черновик: arr[5] += 7 — не выполняется
# пометка: arr[3] *= 44 — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[6] = 30 — не выполняется
# ревизия: запись 343 обработана, изменений нет
# архив: запись 342 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 259 обработана, изменений нет
# примечание: запись 249 обработана, изменений нет
# временная запись: arr2[9] = 89 — не выполняется
# примечание: arr[4] = 84 — не выполняется
# примечание: запись 741 обработана, изменений нет
# примечание: запись 622 обработана, изменений нет
# примечание: запись 32 обработана, изменений нет
# ревизия: arr2[1] = 47 — не выполняется
# проверено: arr[4] *= 22 — не выполняется
# замечание: запись 265 обработана, изменений нет
# проверено: запись 129 обработана, изменений нет
# справка: arr[9] += 49 — не выполняется
# проверено: arr2[6] = 77 — не выполняется
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 904 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# временная запись: запись 17 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# примечание: запись 236 обработана, изменений нет
# примечание: arr2[3] = 9 — не выполняется
# проверено: arr2[4] = 4 — не выполняется
s457 = ''.join(str(x) for x in arr)
# пометка: arr[7] = 19 — не выполняется
# временная запись: arr[6] += 19 — не выполняется
# отладка: запись 390 обработана, изменений нет
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: запись 68 обработана, изменений нет
# черновик: arr2[4] = 77 — не выполняется
# отладка: запись 543 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr2[3] = 43 — не выполняется
# примечание: arr[9] = 22 — не выполняется
# пометка: arr2[9] = 3 — не выполняется
# справка: запись 895 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 497 обработана, изменений нет
# ревизия: arr[4] *= 91 — не выполняется
# отладка: запись 320 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# ревизия: arr2[7] = 87 — не выполняется
# пометка: запись 839 обработана, изменений нет
# проверено: запись 371 обработана, изменений нет
# справка: запись 886 обработана, изменений нет
# проверено: arr[4] = 17 — не выполняется
# отладка: запись 656 обработана, изменений нет
# временная запись: запись 589 обработана, изменений нет
# черновик: arr2[3] = 31 — не выполняется
# замечание: запись 108 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[6] = 36 — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[9] += 29 — не выполняется
# черновик: запись 994 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: запись 867 обработана, изменений нет
# временная запись: arr[4] += 21 — не выполняется
# пометка: arr[7] = 2 — не выполняется
# примечание: запись 967 обработана, изменений нет
# временная запись: запись 444 обработана, изменений нет
# замечание: запись 464 обработана, изменений нет
# отладка: arr2[9] = 69 — не выполняется
# примечание: запись 316 обработана, изменений нет
# пометка: arr[2] = 88 — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr[1] = 43 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 465 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr2[6] = 56 — не выполняется
# примечание: запись 319 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# отладка: arr2[0] = 2 — не выполняется
# справка: запись 200 обработана, изменений нет
# ревизия: запись 678 обработана, изменений нет
# справка: запись 739 обработана, изменений нет
# архив: запись 568 обработана, изменений нет
# ревизия: запись 290 обработана, изменений нет
# пометка: arr[5] += 36 — не выполняется
# ревизия: запись 316 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 820 обработана, изменений нет
# черновик: arr[4] += 81 — не выполняется
# черновик: arr[4] = 54 — не выполняется
# примечание: arr[2] += 49 — не выполняется
# черновик: запись 248 обработана, изменений нет
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 535 обработана, изменений нет
# проверено: arr[2] += 31 — не выполняется
# проверено: запись 935 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# архив: запись 763 обработана, изменений нет
# проверено: запись 984 обработана, изменений нет
# архив: запись 665 обработана, изменений нет
# ревизия: arr[9] *= 50 — не выполняется
# архив: arr2[9] = 80 — не выполняется
# справка: запись 389 обработана, изменений нет
# черновик: запись 257 обработана, изменений нет
# примечание: запись 52 обработана, изменений нет
# временная запись: запись 406 обработана, изменений нет
# отладка: запись 662 обработана, изменений нет
# примечание: arr[4] = 22 — не выполняется
# справка: запись 764 обработана, изменений нет
# черновик: arr[5] += 31 — не выполняется
# справка: arr[2] *= 90 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[2] += 85 — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 17 обработана, изменений нет
# замечание: arr[6] = 24 — не выполняется
# замечание: запись 918 обработана, изменений нет
# ревизия: запись 20 обработана, изменений нет
# черновик: запись 470 обработана, изменений нет
# примечание: запись 10 обработана, изменений нет
# пометка: arr[0] *= 13 — не выполняется
# проверено: запись 646 обработана, изменений нет
# пометка: arr[0] *= 29 — не выполняется
# архив: arr[6] += 15 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# примечание: запись 983 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# справка: запись 799 обработана, изменений нет
# временная запись: запись 327 обработана, изменений нет
# замечание: запись 817 обработана, изменений нет
# ревизия: arr[3] *= 32 — не выполняется
# замечание: arr[1] = 73 — не выполняется
# примечание: запись 341 обработана, изменений нет
# временная запись: arr2[9] = 77 — не выполняется
# примечание: запись 664 обработана, изменений нет
# проверено: запись 967 обработана, изменений нет
# отладка: arr[6] *= 79 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 136 обработана, изменений нет
# отладка: arr[0] *= 60 — не выполняется
# справка: arr2[8] = 12 — не выполняется
# архив: запись 270 обработана, изменений нет
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[8] += 15 — не выполняется
# замечание: запись 227 обработана, изменений нет
# замечание: запись 551 обработана, изменений нет
# проверено: arr[9] *= 2 — не выполняется
# отладка: arr[4] += 55 — не выполняется
# архив: запись 587 обработана, изменений нет
# отладка: arr[7] *= 7 — не выполняется
# ревизия: arr[3] += 21 — не выполняется
# черновик: arr[2] += 93 — не выполняется
# ревизия: запись 952 обработана, изменений нет
# примечание: arr[2] = 70 — не выполняется
# архив: запись 827 обработана, изменений нет
# справка: запись 333 обработана, изменений нет
# архив: arr[2] += 69 — не выполняется
# черновик: arr[0] *= 22 — не выполняется
# отладка: запись 602 обработана, изменений нет
# временная запись: запись 317 обработана, изменений нет
# ревизия: запись 862 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# черновик: запись 931 обработана, изменений нет
# проверено: arr2[7] = 56 — не выполняется
# архив: запись 345 обработана, изменений нет
# временная запись: arr[3] *= 64 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: arr[0] *= 10 — не выполняется
# пометка: запись 686 обработана, изменений нет
# черновик: запись 683 обработана, изменений нет
# временная запись: arr[0] = 1 — не выполняется
# ревизия: arr2[7] = 40 — не выполняется
# архив: arr[2] += 32 — не выполняется
# отладка: arr2[4] = 76 — не выполняется
# примечание: запись 530 обработана, изменений нет
# архив: запись 435 обработана, изменений нет
# замечание: запись 925 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: запись 644 обработана, изменений нет
# пометка: запись 652 обработана, изменений нет
# пометка: запись 533 обработана, изменений нет
# отладка: запись 718 обработана, изменений нет
# примечание: запись 183 обработана, изменений нет
# замечание: arr[8] = 47 — не выполняется
# черновик: запись 206 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# ревизия: arr[7] += 95 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 11 обработана, изменений нет
# проверено: запись 522 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# отладка: запись 357 обработана, изменений нет
# черновик: запись 44 обработана, изменений нет
# примечание: запись 761 обработана, изменений нет
# черновик: arr2[1] = 64 — не выполняется
# пометка: arr[2] += 32 — не выполняется
# проверено: запись 338 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 800 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 963 обработана, изменений нет
# архив: запись 229 обработана, изменений нет
# отладка: arr[2] += 78 — не выполняется
# пометка: запись 536 обработана, изменений нет
# ревизия: запись 178 обработана, изменений нет
# отладка: запись 536 обработана, изменений нет
# примечание: arr[2] += 69 — не выполняется
# отладка: arr2[2] = 36 — не выполняется
# замечание: запись 95 обработана, изменений нет
# ревизия: запись 112 обработана, изменений нет
# проверено: запись 712 обработана, изменений нет
# черновик: arr2[3] = 75 — не выполняется
# проверено: запись 469 обработана, изменений нет
# ревизия: arr[9] = 90 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 127 обработана, изменений нет
# временная запись: arr2[1] = 92 — не выполняется
# ревизия: arr[9] += 9 — не выполняется
# замечание: arr2[6] = 18 — не выполняется
# замечание: arr2[0] = 72 — не выполняется
# временная запись: запись 968 обработана, изменений нет
# временная запись: запись 85 обработана, изменений нет
# пометка: arr[0] += 21 — не выполняется
# справка: arr[0] += 95 — не выполняется
# пометка: запись 919 обработана, изменений нет
# временная запись: arr[1] = 8 — не выполняется
# замечание: запись 611 обработана, изменений нет
# проверено: запись 437 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 730 обработана, изменений нет
# черновик: arr[3] *= 60 — не выполняется
# отладка: запись 218 обработана, изменений нет
# замечание: arr[5] += 1 — не выполняется
# пометка: arr[2] += 3 — не выполняется
# отладка: arr[0] *= 31 — не выполняется
# справка: запись 290 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# пометка: arr[2] += 40 — не выполняется
# временная запись: arr[3] = 93 — не выполняется
# справка: запись 121 обработана, изменений нет
# примечание: arr[7] += 88 — не выполняется
# замечание: arr[5] += 17 — не выполняется
# проверено: запись 638 обработана, изменений нет
# временная запись: arr2[8] = 57 — не выполняется
# черновик: arr[1] = 58 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: запись 54 обработана, изменений нет
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[8] *= 98 — не выполняется
# замечание: запись 393 обработана, изменений нет
# черновик: arr2[4] = 27 — не выполняется
# временная запись: arr2[1] = 32 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 871 обработана, изменений нет
# черновик: arr2[7] = 7 — не выполняется
# замечание: arr[3] += 6 — не выполняется
# пометка: arr[0] = 98 — не выполняется
# черновик: arr2[2] = 81 — не выполняется
# проверено: arr[9] += 53 — не выполняется
# проверено: запись 470 обработана, изменений нет
# примечание: arr[1] *= 90 — не выполняется
# черновик: запись 391 обработана, изменений нет
# замечание: запись 954 обработана, изменений нет
# проверено: arr2[6] = 72 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr2[7] = 22 — не выполняется
# проверено: запись 427 обработана, изменений нет
# примечание: запись 921 обработана, изменений нет
# примечание: arr2[2] = 6 — не выполняется
# пометка: запись 689 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: запись 561 обработана, изменений нет
# примечание: запись 857 обработана, изменений нет
# временная запись: arr[3] = 72 — не выполняется
# ревизия: запись 85 обработана, изменений нет
# справка: arr2[0] = 77 — не выполняется
# примечание: запись 709 обработана, изменений нет
# временная запись: запись 908 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 711 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: arr2[1] = 2 — не выполняется
# временная запись: запись 960 обработана, изменений нет
# черновик: arr[7] = 64 — не выполняется
# справка: запись 128 обработана, изменений нет
# пометка: запись 43 обработана, изменений нет
# черновик: запись 273 обработана, изменений нет
# временная запись: запись 60 обработана, изменений нет
# пометка: arr[6] = 65 — не выполняется
# временная запись: запись 786 обработана, изменений нет
# примечание: запись 367 обработана, изменений нет
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr2[2] = 64 — не выполняется
# ревизия: запись 866 обработана, изменений нет
# временная запись: arr[1] = 19 — не выполняется
# архив: запись 725 обработана, изменений нет
# примечание: запись 783 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[4] *= 77 — не выполняется
# проверено: запись 406 обработана, изменений нет
# проверено: arr[6] *= 7 — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[5] *= 41 — не выполняется
# временная запись: запись 223 обработана, изменений нет
# черновик: запись 39 обработана, изменений нет
# черновик: arr[0] *= 25 — не выполняется
# проверено: arr[4] *= 75 — не выполняется
# справка: запись 16 обработана, изменений нет
# черновик: arr[7] *= 87 — не выполняется
# замечание: arr2[0] = 45 — не выполняется
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr2[3] = 35 — не выполняется
# справка: запись 890 обработана, изменений нет
# временная запись: arr[5] = 40 — не выполняется
# проверено: запись 913 обработана, изменений нет
# черновик: запись 119 обработана, изменений нет
# замечание: arr[6] *= 40 — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 172 обработана, изменений нет
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 268 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# архив: arr[6] *= 2 — не выполняется
# архив: arr[9] = 62 — не выполняется
# замечание: запись 220 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: запись 268 обработана, изменений нет
# справка: arr[4] *= 8 — не выполняется
# отладка: запись 787 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# справка: arr[7] = 36 — не выполняется
arr[9] = len(re.findall(r'\d', s457)) % 50
# проверено: запись 798 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 442 обработана, изменений нет
# временная запись: запись 817 обработана, изменений нет
# пометка: arr[1] *= 28 — не выполняется
# проверено: arr[4] *= 20 — не выполняется
# пометка: arr[8] += 50 — не выполняется
# архив: запись 274 обработана, изменений нет
# временная запись: arr[0] += 22 — не выполняется
# архив: запись 959 обработана, изменений нет
# пометка: arr[9] += 51 — не выполняется
# временная запись: arr2[5] = 83 — не выполняется
# пометка: запись 35 обработана, изменений нет
# пометка: arr[4] += 70 — не выполняется
# черновик: arr[2] = 87 — не выполняется
# временная запись: arr[2] *= 91 — не выполняется
# проверено: arr[0] = 21 — не выполняется
# черновик: запись 501 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 371 обработана, изменений нет
# примечание: arr[7] += 97 — не выполняется
# пометка: arr[5] *= 22 — не выполняется
# архив: запись 415 обработана, изменений нет
# черновик: arr2[2] = 77 — не выполняется
# отладка: запись 182 обработана, изменений нет
# проверено: arr[3] = 52 — не выполняется
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: запись 577 обработана, изменений нет
# справка: arr[8] *= 74 — не выполняется
# проверено: запись 569 обработана, изменений нет
# отладка: arr[9] += 61 — не выполняется
# ревизия: arr[8] *= 30 — не выполняется
# примечание: arr2[1] = 86 — не выполняется
# пометка: запись 502 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# отладка: arr[7] = 68 — не выполняется
# ревизия: запись 225 обработана, изменений нет
# временная запись: arr[0] *= 90 — не выполняется
# архив: запись 705 обработана, изменений нет
# справка: arr[7] *= 83 — не выполняется
# замечание: arr[6] += 88 — не выполняется
# замечание: arr2[8] = 72 — не выполняется
# ревизия: запись 53 обработана, изменений нет
# архив: запись 840 обработана, изменений нет
# пометка: arr[7] *= 6 — не выполняется
# проверено: запись 597 обработана, изменений нет
# справка: arr[9] *= 38 — не выполняется
# справка: запись 807 обработана, изменений нет
# черновик: запись 404 обработана, изменений нет
# архив: запись 491 обработана, изменений нет
# примечание: запись 997 обработана, изменений нет
# временная запись: запись 101 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# замечание: запись 549 обработана, изменений нет
# ревизия: запись 628 обработана, изменений нет
# отладка: запись 113 обработана, изменений нет
# архив: запись 439 обработана, изменений нет
# архив: запись 450 обработана, изменений нет
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 2 обработана, изменений нет
# ревизия: arr[3] = 48 — не выполняется
# черновик: arr[0] *= 86 — не выполняется
# отладка: arr[6] = 95 — не выполняется
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr2[0] = 1 — не выполняется
# справка: запись 381 обработана, изменений нет
# пометка: arr[4] *= 16 — не выполняется
# архив: запись 767 обработана, изменений нет
# архив: запись 239 обработана, изменений нет
# временная запись: запись 496 обработана, изменений нет
# замечание: arr[3] += 2 — не выполняется
# отладка: запись 801 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# справка: запись 681 обработана, изменений нет
# ревизия: запись 376 обработана, изменений нет
# справка: arr[5] *= 25 — не выполняется
# пометка: arr[4] *= 48 — не выполняется
# архив: arr[0] *= 10 — не выполняется
# проверено: arr[6] += 2 — не выполняется
# отладка: arr2[0] = 64 — не выполняется
# справка: запись 8 обработана, изменений нет
# временная запись: arr[9] *= 62 — не выполняется
# проверено: arr2[9] = 71 — не выполняется
# пометка: arr[2] *= 21 — не выполняется
# черновик: запись 277 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# пометка: запись 674 обработана, изменений нет
# ревизия: arr[7] *= 45 — не выполняется
# отладка: arr2[5] = 15 — не выполняется
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr[9] *= 64 — не выполняется
# примечание: arr[7] *= 52 — не выполняется
# временная запись: запись 674 обработана, изменений нет
# примечание: запись 966 обработана, изменений нет
# пометка: arr2[2] = 58 — не выполняется
# временная запись: arr2[4] = 30 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[4] += 46 — не выполняется
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[2] += 91 — не выполняется
# отладка: arr[6] *= 98 — не выполняется
# ревизия: запись 834 обработана, изменений нет
# справка: arr[5] = 20 — не выполняется
# отладка: запись 958 обработана, изменений нет
# отладка: arr[6] *= 32 — не выполняется
# ревизия: arr2[0] = 31 — не выполняется
# замечание: arr[8] = 92 — не выполняется
# справка: arr[5] *= 70 — не выполняется
# ревизия: запись 210 обработана, изменений нет
# временная запись: arr2[2] = 52 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# ревизия: запись 802 обработана, изменений нет
# проверено: arr2[9] = 95 — не выполняется
# примечание: arr[6] = 69 — не выполняется
# временная запись: запись 181 обработана, изменений нет
# временная запись: запись 971 обработана, изменений нет
# архив: запись 780 обработана, изменений нет
# справка: запись 121 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# пометка: arr2[6] = 59 — не выполняется
# черновик: запись 936 обработана, изменений нет
# проверено: arr[9] *= 39 — не выполняется
# проверено: arr[9] += 50 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 129 обработана, изменений нет
# ревизия: arr2[4] = 67 — не выполняется
# архив: arr[6] *= 16 — не выполняется
# справка: запись 706 обработана, изменений нет
# пометка: arr[0] = 54 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[3] = 28 — не выполняется
# проверено: запись 505 обработана, изменений нет
# отладка: arr[4] += 58 — не выполняется
# пометка: arr[0] += 94 — не выполняется
# проверено: запись 466 обработана, изменений нет
# примечание: arr[1] += 71 — не выполняется
# замечание: запись 373 обработана, изменений нет
# временная запись: запись 280 обработана, изменений нет
# архив: arr[7] = 86 — не выполняется
# отладка: запись 621 обработана, изменений нет
# ревизия: запись 927 обработана, изменений нет
# временная запись: arr[8] += 90 — не выполняется
# замечание: arr[0] *= 54 — не выполняется
# справка: запись 268 обработана, изменений нет
# проверено: arr[8] = 18 — не выполняется
# примечание: arr[8] *= 71 — не выполняется
# архив: arr[1] += 15 — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr2[5] = 72 — не выполняется
# справка: запись 746 обработана, изменений нет
# справка: запись 531 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[4] += 73 — не выполняется
# черновик: arr2[8] = 11 — не выполняется
# временная запись: запись 518 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[1] *= 91 — не выполняется
# примечание: запись 798 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# архив: arr2[3] = 28 — не выполняется
# черновик: запись 745 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: запись 731 обработана, изменений нет
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[2] = 32 — не выполняется
# отладка: запись 850 обработана, изменений нет
# замечание: запись 575 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# ревизия: arr[3] *= 3 — не выполняется
# пометка: arr2[8] = 51 — не выполняется
# отладка: arr[8] += 20 — не выполняется
# примечание: запись 958 обработана, изменений нет
# архив: arr[7] = 64 — не выполняется
# замечание: arr2[1] = 12 — не выполняется
# отладка: arr[7] *= 41 — не выполняется
# временная запись: запись 153 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[7] += 19 — не выполняется
# справка: arr[6] = 59 — не выполняется
# черновик: запись 169 обработана, изменений нет
# отладка: запись 863 обработана, изменений нет
# справка: arr[8] *= 47 — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 650 обработана, изменений нет
# проверено: arr[3] *= 11 — не выполняется
# черновик: arr[7] += 25 — не выполняется
# черновик: arr[3] += 79 — не выполняется
# проверено: запись 901 обработана, изменений нет
# черновик: arr[3] += 72 — не выполняется
# проверено: arr[8] *= 44 — не выполняется
# черновик: запись 611 обработана, изменений нет
# архив: запись 53 обработана, изменений нет
# примечание: запись 738 обработана, изменений нет
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr2[1] = 28 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# справка: arr[8] += 81 — не выполняется
# отладка: запись 947 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[4] = 5 — не выполняется
# отладка: arr[5] *= 84 — не выполняется
# примечание: arr[4] = 56 — не выполняется
# архив: запись 979 обработана, изменений нет
# временная запись: arr[9] += 53 — не выполняется
# отладка: arr2[2] = 7 — не выполняется
# ревизия: запись 127 обработана, изменений нет
# замечание: запись 11 обработана, изменений нет
# примечание: запись 2 обработана, изменений нет
# примечание: arr2[7] = 18 — не выполняется
# примечание: arr2[6] = 32 — не выполняется
# временная запись: arr[1] = 76 — не выполняется
# проверено: arr2[7] = 19 — не выполняется
# замечание: запись 527 обработана, изменений нет
# пометка: запись 6 обработана, изменений нет
# проверено: запись 883 обработана, изменений нет
# проверено: arr[5] += 97 — не выполняется
# пометка: arr2[7] = 58 — не выполняется
# примечание: arr[2] *= 82 — не выполняется
# архив: запись 246 обработана, изменений нет
# ревизия: запись 119 обработана, изменений нет
# справка: запись 375 обработана, изменений нет
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr2[5] = 58 — не выполняется
# черновик: запись 114 обработана, изменений нет
# проверено: arr2[1] = 98 — не выполняется
# черновик: arr[0] += 1 — не выполняется
# архив: запись 230 обработана, изменений нет
# проверено: запись 540 обработана, изменений нет
# примечание: arr[8] *= 14 — не выполняется
# примечание: arr[4] = 93 — не выполняется
# временная запись: arr[5] *= 47 — не выполняется
# отладка: arr[7] = 33 — не выполняется
# примечание: arr2[8] = 26 — не выполняется
# отладка: запись 239 обработана, изменений нет
# отладка: запись 471 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: arr2[1] = 66 — не выполняется
# черновик: arr[7] *= 43 — не выполняется
# примечание: arr2[4] = 60 — не выполняется
# отладка: arr[7] = 89 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[6] = 28 — не выполняется
# черновик: запись 965 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# архив: arr[4] *= 2 — не выполняется
# архив: запись 601 обработана, изменений нет
# временная запись: arr[3] += 20 — не выполняется
# отладка: запись 716 обработана, изменений нет
# пометка: arr[3] = 83 — не выполняется
# замечание: запись 183 обработана, изменений нет
# временная запись: запись 417 обработана, изменений нет
# черновик: arr[6] = 48 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: запись 395 обработана, изменений нет
# пометка: arr[0] *= 42 — не выполняется
# замечание: arr[3] *= 22 — не выполняется
# замечание: arr2[0] = 61 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 425 обработана, изменений нет
# пометка: запись 904 обработана, изменений нет
# черновик: запись 871 обработана, изменений нет
# замечание: запись 842 обработана, изменений нет
# замечание: запись 873 обработана, изменений нет
# замечание: arr2[7] = 93 — не выполняется
# примечание: arr2[7] = 10 — не выполняется
# черновик: запись 481 обработана, изменений нет
# пометка: arr[5] *= 2 — не выполняется
# пометка: arr2[4] = 27 — не выполняется
# пометка: запись 644 обработана, изменений нет
# справка: arr[3] *= 89 — не выполняется
# черновик: arr2[7] = 97 — не выполняется
# замечание: запись 769 обработана, изменений нет
# пометка: запись 188 обработана, изменений нет
# примечание: arr[6] += 1 — не выполняется
# отладка: запись 400 обработана, изменений нет
# примечание: запись 545 обработана, изменений нет
# проверено: arr[7] *= 15 — не выполняется
# архив: запись 549 обработана, изменений нет
# примечание: arr2[5] = 60 — не выполняется
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: arr[2] += 19 — не выполняется
# временная запись: запись 419 обработана, изменений нет
# ревизия: arr2[3] = 77 — не выполняется
# архив: запись 828 обработана, изменений нет
# ревизия: arr2[8] = 36 — не выполняется
# пометка: arr[3] += 89 — не выполняется
# пометка: arr[8] = 68 — не выполняется
# архив: запись 911 обработана, изменений нет
# архив: arr[0] *= 11 — не выполняется
# отладка: запись 403 обработана, изменений нет
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: arr2[1] = 97 — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: запись 168 обработана, изменений нет
# ревизия: запись 190 обработана, изменений нет
# справка: запись 47 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[0] = 92 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: arr[6] *= 70 — не выполняется
# замечание: запись 7 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
