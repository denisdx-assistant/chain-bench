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
arr2[2] = 31
arr[1], arr[4] = arr[4], arr[1]
arr[0], arr[9] = arr[9], arr[0]
arr[6] = 32
arr[0] *= 44
arr2[4] = 15
arr[5] += 11
arr[9] += 51
"""

TRAP_0 = "arr[1] = 818"
TRAP_1 = "arr[3] = 947"
TRAP_2 = "arr[8] = 768"
TRAP_3 = "arr[4] = 638"
TRAP_4 = "arr[3] = 922"
TRAP_5 = "arr[0] = 378"
TRAP_6 = "arr[4] = 931"
TRAP_7 = "arr[2] = 905"
TRAP_8 = "arr[5] = 173"
TRAP_9 = "arr[7] = 272"
TRAP_10 = "arr[4] = 666"
TRAP_11 = "arr[2] = 996"
TRAP_12 = "arr[1] = 961"
TRAP_13 = "arr[2] = 596"
TRAP_14 = "arr[1] = 287"
TRAP_15 = "arr[6] = 139"
TRAP_16 = "arr[5] = 689"
TRAP_17 = "arr[3] = 269"
TRAP_18 = "arr[1] = 822"
TRAP_19 = "arr[6] = 102"
TRAP_20 = "arr[1] = 431"
TRAP_21 = "arr[2] = 272"
TRAP_22 = "arr[4] = 296"
TRAP_23 = "arr[0] = 737"
TRAP_24 = "arr[8] = 745"
TRAP_25 = "arr[0] = 364"
TRAP_26 = "arr[8] = 831"
TRAP_27 = "arr[0] = 164"
TRAP_28 = "arr[4] = 297"
TRAP_29 = "arr[8] = 805"
TRAP_30 = "arr[2] = 791"
TRAP_31 = "arr[6] = 140"
TRAP_32 = "arr[7] = 612"
TRAP_33 = "arr[2] = 691"
TRAP_34 = "arr[2] = 767"
TRAP_35 = "arr[9] = 165"
TRAP_36 = "arr[1] = 597"
TRAP_37 = "arr[6] = 253"
TRAP_38 = "arr[3] = 628"
TRAP_39 = "arr[7] = 786"
TRAP_40 = "arr[5] = 613"
TRAP_41 = "arr[6] = 990"
TRAP_42 = "arr[5] = 139"
TRAP_43 = "arr[7] = 773"
TRAP_44 = "arr[7] = 530"
TRAP_45 = "arr[0] = 641"
TRAP_46 = "arr[4] = 999"
TRAP_47 = "arr[6] = 543"
TRAP_48 = "arr[1] = 306"
TRAP_49 = "arr[7] = 616"
TRAP_50 = "arr[2] = 424"
TRAP_51 = "arr[8] = 669"
TRAP_52 = "arr[7] = 650"
TRAP_53 = "arr[1] = 362"
TRAP_54 = "arr[2] = 252"
TRAP_55 = "arr[5] = 962"
TRAP_56 = "arr[4] = 759"
TRAP_57 = "arr[5] = 767"
TRAP_58 = "arr[3] = 468"
TRAP_59 = "arr[7] = 917"
TRAP_60 = "arr[4] = 144"
TRAP_61 = "arr[9] = 932"
TRAP_62 = "arr[4] = 326"
TRAP_63 = "arr[5] = 786"
TRAP_64 = "arr[4] = 620"
TRAP_65 = "arr[2] = 664"
TRAP_66 = "arr[5] = 362"
TRAP_67 = "arr[6] = 645"
TRAP_68 = "arr[0] = 259"
TRAP_69 = "arr[0] = 764"
TRAP_70 = "arr[1] = 946"
TRAP_71 = "arr[4] = 769"
TRAP_72 = "arr[4] = 715"
TRAP_73 = "arr[0] = 529"
TRAP_74 = "arr[6] = 915"
TRAP_75 = "arr[3] = 980"
TRAP_76 = "arr[0] = 408"
TRAP_77 = "arr[2] = 372"
TRAP_78 = "arr[8] = 281"
TRAP_79 = "arr[6] = 425"
TRAP_80 = "arr[1] = 264"
TRAP_81 = "arr[7] = 835"
TRAP_82 = "arr[4] = 616"
TRAP_83 = "arr[5] = 844"
TRAP_84 = "arr[2] = 831"
TRAP_85 = "arr[6] = 954"
TRAP_86 = "arr[5] = 662"
TRAP_87 = "arr[2] = 897"
TRAP_88 = "arr[9] = 535"
TRAP_89 = "arr[1] = 120"
TRAP_90 = "arr[0] = 341"
TRAP_91 = "arr[7] = 902"
TRAP_92 = "arr[5] = 822"
TRAP_93 = "arr[6] = 879"
TRAP_94 = "arr[8] = 849"
TRAP_95 = "arr[8] = 324"
TRAP_96 = "arr[7] = 891"
TRAP_97 = "arr[1] = 574"
TRAP_98 = "arr[4] = 883"
TRAP_99 = "arr[4] = 239"
TRAP_100 = "arr[6] = 867"
TRAP_101 = "arr[7] = 565"
TRAP_102 = "arr[8] = 238"
TRAP_103 = "arr[2] = 804"
TRAP_104 = "arr[8] = 343"
TRAP_105 = "arr[0] = 820"
TRAP_106 = "arr[1] = 605"
TRAP_107 = "arr[2] = 216"
TRAP_108 = "arr[1] = 564"
TRAP_109 = "arr[5] = 682"
TRAP_110 = "arr[6] = 446"
TRAP_111 = "arr[0] = 177"
TRAP_112 = "arr[1] = 375"
TRAP_113 = "arr[7] = 229"
TRAP_114 = "arr[1] = 514"
TRAP_115 = "arr[6] = 741"
TRAP_116 = "arr[5] = 130"
TRAP_117 = "arr[8] = 782"
TRAP_118 = "arr[4] = 355"
TRAP_119 = "arr[7] = 741"
TRAP_120 = "arr[7] = 449"
TRAP_121 = "arr[1] = 738"
TRAP_122 = "arr[0] = 170"
TRAP_123 = "arr[1] = 432"
TRAP_124 = "arr[2] = 216"
TRAP_125 = "arr[9] = 249"
TRAP_126 = "arr[9] = 740"
TRAP_127 = "arr[3] = 311"
TRAP_128 = "arr[1] = 181"
TRAP_129 = "arr[4] = 376"
TRAP_130 = "arr[9] = 725"
TRAP_131 = "arr[9] = 415"
TRAP_132 = "arr[6] = 708"
TRAP_133 = "arr[6] = 930"
TRAP_134 = "arr[2] = 312"
TRAP_135 = "arr[5] = 594"
TRAP_136 = "arr[6] = 881"
TRAP_137 = "arr[2] = 553"
TRAP_138 = "arr[6] = 472"
TRAP_139 = "arr[9] = 466"
TRAP_140 = "arr[3] = 870"
TRAP_141 = "arr[5] = 838"
TRAP_142 = "arr[4] = 460"
TRAP_143 = "arr[7] = 260"
TRAP_144 = "arr[3] = 626"
TRAP_145 = "arr[5] = 790"
TRAP_146 = "arr[5] = 941"
TRAP_147 = "arr[6] = 689"
TRAP_148 = "arr[4] = 137"
TRAP_149 = "arr[5] = 375"

arr = [2, 8, 24, 7, 3, 19, 20, 9, 19, 17]

note_0 = str(arr[9]) + str(arr[8])
code_1 = re.sub(r'[0-9]', '#', str(arr[2]))
note_2 = str(arr[6]) + str(arr[0])
code_3 = re.sub(r'[0-9]', '#', str(arr[2]))
note_4 = str(arr[3]) + str(arr[0])
tmp_5 = arr[1] + 20
tmp_6 = arr[1] + 44
tmp_7 = arr[8] + 23
note_8 = str(arr[3]) + str(arr[4])
note_9 = str(arr[2]) + str(arr[9])
tmp_10 = arr[9] + 47
label_11 = "запись 11 не применялась"
tmp_12 = arr[4] + 21
note_13 = str(arr[6]) + str(arr[0])
label_14 = "запись 14 не применялась"
copy_15 = arr[4]
copy_16 = arr[8]
note_17 = str(arr[6]) + str(arr[0])
copy_18 = arr[7]
copy_19 = arr[9]
tmp_20 = arr[0] + 6
tmp_21 = arr[1] + 36
note_22 = str(arr[7]) + str(arr[2])
code_23 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_24 = arr[3] + 14
code_25 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_26 = arr[8]
copy_27 = arr[5]
label_28 = "запись 28 не применялась"
note_29 = str(arr[2]) + str(arr[0])
tmp_30 = arr[6] + 45
note_31 = str(arr[0]) + str(arr[5])
code_32 = re.sub(r'[0-9]', '#', str(arr[1]))
code_33 = re.sub(r'[0-9]', '#', str(arr[8]))
label_34 = "запись 34 не применялась"
code_35 = re.sub(r'[0-9]', '#', str(arr[4]))
note_36 = str(arr[8]) + str(arr[8])
tmp_37 = arr[3] + 34
code_38 = re.sub(r'[0-9]', '#', str(arr[7]))
code_39 = re.sub(r'[0-9]', '#', str(arr[5]))
note_40 = str(arr[1]) + str(arr[4])
tmp_41 = arr[0] + 37
label_42 = "запись 42 не применялась"
code_43 = re.sub(r'[0-9]', '#', str(arr[7]))
note_44 = str(arr[8]) + str(arr[3])
code_45 = re.sub(r'[0-9]', '#', str(arr[2]))
code_46 = re.sub(r'[0-9]', '#', str(arr[1]))
label_47 = "запись 47 не применялась"
label_48 = "запись 48 не применялась"
note_49 = str(arr[6]) + str(arr[2])
code_50 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_51 = arr[4]
note_52 = str(arr[1]) + str(arr[8])
tmp_53 = arr[1] + 13
code_54 = re.sub(r'[0-9]', '#', str(arr[7]))
note_55 = str(arr[6]) + str(arr[8])
label_56 = "запись 56 не применялась"
tmp_57 = arr[9] + 6
copy_58 = arr[8]
label_59 = "запись 59 не применялась"
tmp_60 = arr[0] + 17
code_61 = re.sub(r'[0-9]', '#', str(arr[2]))
code_62 = re.sub(r'[0-9]', '#', str(arr[7]))
code_63 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_64 = arr[2]
code_65 = re.sub(r'[0-9]', '#', str(arr[5]))
code_66 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_67 = arr[5] + 44
code_68 = re.sub(r'[0-9]', '#', str(arr[4]))
code_69 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_70 = arr[3] + 43
copy_71 = arr[4]
copy_72 = arr[2]
tmp_73 = arr[5] + 12
copy_74 = arr[9]
copy_75 = arr[3]
copy_76 = arr[3]
code_77 = re.sub(r'[0-9]', '#', str(arr[9]))
note_78 = str(arr[2]) + str(arr[2])
code_79 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_80 = arr[2]
copy_81 = arr[7]
label_82 = "запись 82 не применялась"
note_83 = str(arr[8]) + str(arr[2])
note_84 = str(arr[2]) + str(arr[4])
tmp_85 = arr[9] + 15
tmp_86 = arr[2] + 6
copy_87 = arr[3]
label_88 = "запись 88 не применялась"
code_89 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_90 = arr[5]
note_91 = str(arr[3]) + str(arr[5])
tmp_92 = arr[0] + 5
note_93 = str(arr[9]) + str(arr[6])
tmp_94 = arr[9] + 44
note_95 = str(arr[2]) + str(arr[3])
note_96 = str(arr[1]) + str(arr[4])
code_97 = re.sub(r'[0-9]', '#', str(arr[3]))
code_98 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_99 = arr[1]
tmp_100 = arr[0] + 11
tmp_101 = arr[6] + 15
label_102 = "запись 102 не применялась"
code_103 = re.sub(r'[0-9]', '#', str(arr[2]))
code_104 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_105 = arr[6] + 7
note_106 = str(arr[3]) + str(arr[9])
tmp_107 = arr[1] + 39
copy_108 = arr[5]
label_109 = "запись 109 не применялась"
note_110 = str(arr[9]) + str(arr[6])
tmp_111 = arr[0] + 9
copy_112 = arr[6]
note_113 = str(arr[8]) + str(arr[2])
tmp_114 = arr[0] + 17
copy_115 = arr[9]
code_116 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_117 = arr[8]
code_118 = re.sub(r'[0-9]', '#', str(arr[4]))
note_119 = str(arr[6]) + str(arr[7])
copy_120 = arr[9]
note_121 = str(arr[5]) + str(arr[6])
copy_122 = arr[2]
tmp_123 = arr[5] + 26
tmp_124 = arr[8] + 5
tmp_125 = arr[8] + 31
tmp_126 = arr[0] + 5
copy_127 = arr[0]
tmp_128 = arr[0] + 32
tmp_129 = arr[0] + 2
note_130 = str(arr[5]) + str(arr[2])
label_131 = "запись 131 не применялась"
tmp_132 = arr[6] + 16
note_133 = str(arr[5]) + str(arr[7])
note_134 = str(arr[4]) + str(arr[2])
note_135 = str(arr[7]) + str(arr[8])
note_136 = str(arr[4]) + str(arr[3])
note_137 = str(arr[1]) + str(arr[2])
copy_138 = arr[3]
label_139 = "запись 139 не применялась"
tmp_140 = arr[3] + 43
note_141 = str(arr[5]) + str(arr[1])
note_142 = str(arr[1]) + str(arr[5])
label_143 = "запись 143 не применялась"
note_144 = str(arr[2]) + str(arr[1])
note_145 = str(arr[7]) + str(arr[2])
note_146 = str(arr[3]) + str(arr[5])
note_147 = str(arr[8]) + str(arr[2])
tmp_148 = arr[2] + 10
tmp_149 = arr[0] + 27
tmp_150 = arr[1] + 20
note_151 = str(arr[8]) + str(arr[1])
tmp_152 = arr[5] + 36
label_153 = "запись 153 не применялась"
label_154 = "запись 154 не применялась"
tmp_155 = arr[0] + 1
tmp_156 = arr[4] + 20
tmp_157 = arr[3] + 48
code_158 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_159 = arr[1] + 17
tmp_160 = arr[6] + 30
note_161 = str(arr[2]) + str(arr[7])
copy_162 = arr[3]
copy_163 = arr[5]
label_164 = "запись 164 не применялась"
tmp_165 = arr[8] + 22
note_166 = str(arr[8]) + str(arr[3])
copy_167 = arr[0]
copy_168 = arr[4]
note_169 = str(arr[6]) + str(arr[2])
tmp_170 = arr[2] + 17
tmp_171 = arr[6] + 45
code_172 = re.sub(r'[0-9]', '#', str(arr[0]))
code_173 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_174 = arr[4] + 14
tmp_175 = arr[1] + 42
copy_176 = arr[9]
label_177 = "запись 177 не применялась"
label_178 = "запись 178 не применялась"
copy_179 = arr[8]
tmp_180 = arr[7] + 30
label_181 = "запись 181 не применялась"
label_182 = "запись 182 не применялась"
tmp_183 = arr[9] + 23
copy_184 = arr[2]
tmp_185 = arr[8] + 2
code_186 = re.sub(r'[0-9]', '#', str(arr[6]))
note_187 = str(arr[1]) + str(arr[2])
copy_188 = arr[2]
code_189 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_190 = arr[7]
note_191 = str(arr[9]) + str(arr[9])
tmp_192 = arr[8] + 38
label_193 = "запись 193 не применялась"
tmp_194 = arr[5] + 5
tmp_195 = arr[7] + 6
code_196 = re.sub(r'[0-9]', '#', str(arr[8]))
note_197 = str(arr[7]) + str(arr[4])
note_198 = str(arr[4]) + str(arr[2])
tmp_199 = arr[7] + 29
copy_200 = arr[7]
tmp_201 = arr[5] + 17
tmp_202 = arr[9] + 9
note_203 = str(arr[2]) + str(arr[0])
tmp_204 = arr[9] + 41
tmp_205 = arr[1] + 40
note_206 = str(arr[5]) + str(arr[9])
tmp_207 = arr[0] + 45
note_208 = str(arr[6]) + str(arr[1])
code_209 = re.sub(r'[0-9]', '#', str(arr[0]))
note_210 = str(arr[9]) + str(arr[1])
note_211 = str(arr[4]) + str(arr[4])
note_212 = str(arr[1]) + str(arr[2])
copy_213 = arr[4]
tmp_214 = arr[1] + 12
copy_215 = arr[0]
note_216 = str(arr[1]) + str(arr[0])
label_217 = "запись 217 не применялась"
note_218 = str(arr[5]) + str(arr[5])
copy_219 = arr[6]
label_220 = "запись 220 не применялась"
copy_221 = arr[3]
copy_222 = arr[8]
copy_223 = arr[5]
code_224 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_225 = arr[3] + 4
note_226 = str(arr[8]) + str(arr[3])
label_227 = "запись 227 не применялась"
code_228 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_229 = arr[8] + 38
tmp_230 = arr[3] + 28
copy_231 = arr[2]
note_232 = str(arr[1]) + str(arr[1])
tmp_233 = arr[8] + 19
code_234 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_235 = arr[5] + 42
copy_236 = arr[7]
code_237 = re.sub(r'[0-9]', '#', str(arr[8]))
code_238 = re.sub(r'[0-9]', '#', str(arr[2]))
note_239 = str(arr[5]) + str(arr[7])
code_240 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_241 = arr[8] + 40
tmp_242 = arr[4] + 27
note_243 = str(arr[7]) + str(arr[8])
tmp_244 = arr[2] + 38
tmp_245 = arr[0] + 41
copy_246 = arr[0]
code_247 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_248 = arr[5] + 18
code_249 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_250 = arr[1]
note_251 = str(arr[8]) + str(arr[0])
tmp_252 = arr[5] + 11
code_253 = re.sub(r'[0-9]', '#', str(arr[3]))
label_254 = "запись 254 не применялась"
label_255 = "запись 255 не применялась"
code_256 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_257 = arr[2] + 35
tmp_258 = arr[2] + 25
code_259 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_260 = arr[7] + 5
note_261 = str(arr[1]) + str(arr[6])
tmp_262 = arr[9] + 8
copy_263 = arr[7]
tmp_264 = arr[0] + 3
tmp_265 = arr[8] + 33
code_266 = re.sub(r'[0-9]', '#', str(arr[5]))
code_267 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_268 = arr[1]
tmp_269 = arr[7] + 48
note_270 = str(arr[8]) + str(arr[7])
tmp_271 = arr[8] + 26
tmp_272 = arr[3] + 10
note_273 = str(arr[2]) + str(arr[7])
tmp_274 = arr[5] + 36
tmp_275 = arr[2] + 4
label_276 = "запись 276 не применялась"
note_277 = str(arr[8]) + str(arr[5])
label_278 = "запись 278 не применялась"
note_279 = str(arr[7]) + str(arr[2])
note_280 = str(arr[7]) + str(arr[1])
tmp_281 = arr[6] + 11
tmp_282 = arr[6] + 30
copy_283 = arr[0]
code_284 = re.sub(r'[0-9]', '#', str(arr[3]))
code_285 = re.sub(r'[0-9]', '#', str(arr[0]))
label_286 = "запись 286 не применялась"
code_287 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_288 = arr[2]
note_289 = str(arr[4]) + str(arr[4])
tmp_290 = arr[5] + 13
note_291 = str(arr[4]) + str(arr[9])
note_292 = str(arr[3]) + str(arr[1])
note_293 = str(arr[0]) + str(arr[0])
note_294 = str(arr[3]) + str(arr[1])
copy_295 = arr[3]
tmp_296 = arr[3] + 33
copy_297 = arr[7]
note_298 = str(arr[1]) + str(arr[2])
note_299 = str(arr[6]) + str(arr[0])
label_300 = "запись 300 не применялась"
copy_301 = arr[5]
code_302 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_303 = arr[5] + 31
copy_304 = arr[2]
tmp_305 = arr[2] + 48
tmp_306 = arr[7] + 45
tmp_307 = arr[1] + 1
note_308 = str(arr[9]) + str(arr[1])
note_309 = str(arr[6]) + str(arr[6])
note_310 = str(arr[9]) + str(arr[1])
copy_311 = arr[1]
code_312 = re.sub(r'[0-9]', '#', str(arr[2]))
note_313 = str(arr[1]) + str(arr[7])
tmp_314 = arr[3] + 1
tmp_315 = arr[7] + 2
tmp_316 = arr[9] + 34
tmp_317 = arr[3] + 21
tmp_318 = arr[4] + 6
tmp_319 = arr[1] + 13
copy_320 = arr[2]
tmp_321 = arr[9] + 13
note_322 = str(arr[2]) + str(arr[3])
note_323 = str(arr[2]) + str(arr[7])
note_324 = str(arr[2]) + str(arr[5])
note_325 = str(arr[9]) + str(arr[0])
label_326 = "запись 326 не применялась"
note_327 = str(arr[7]) + str(arr[5])
note_328 = str(arr[3]) + str(arr[1])
tmp_329 = arr[3] + 31
note_330 = str(arr[9]) + str(arr[7])
code_331 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_332 = arr[4] + 47
code_333 = re.sub(r'[0-9]', '#', str(arr[4]))
label_334 = "запись 334 не применялась"
tmp_335 = arr[8] + 49
code_336 = re.sub(r'[0-9]', '#', str(arr[1]))
code_337 = re.sub(r'[0-9]', '#', str(arr[9]))
code_338 = re.sub(r'[0-9]', '#', str(arr[0]))
code_339 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_340 = arr[4] + 11
tmp_341 = arr[7] + 13
copy_342 = arr[4]
code_343 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_344 = arr[1] + 48
code_345 = re.sub(r'[0-9]', '#', str(arr[1]))
note_346 = str(arr[9]) + str(arr[6])
tmp_347 = arr[8] + 31
tmp_348 = arr[1] + 36
code_349 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_350 = arr[0] + 39
note_351 = str(arr[0]) + str(arr[3])
tmp_352 = arr[5] + 20
tmp_353 = arr[4] + 6
tmp_354 = arr[5] + 38
tmp_355 = arr[2] + 24
code_356 = re.sub(r'[0-9]', '#', str(arr[3]))
label_357 = "запись 357 не применялась"
code_358 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_359 = arr[2] + 43
tmp_360 = arr[5] + 31
tmp_361 = arr[4] + 11
note_362 = str(arr[4]) + str(arr[7])
copy_363 = arr[2]
note_364 = str(arr[7]) + str(arr[7])
tmp_365 = arr[5] + 26
note_366 = str(arr[4]) + str(arr[8])
note_367 = str(arr[5]) + str(arr[1])
code_368 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_369 = arr[3] + 20
tmp_370 = arr[0] + 27
note_371 = str(arr[5]) + str(arr[7])
note_372 = str(arr[8]) + str(arr[4])
note_373 = str(arr[8]) + str(arr[5])
tmp_374 = arr[0] + 43
copy_375 = arr[3]
code_376 = re.sub(r'[0-9]', '#', str(arr[1]))
label_377 = "запись 377 не применялась"
tmp_378 = arr[6] + 43
note_379 = str(arr[3]) + str(arr[3])
tmp_380 = arr[3] + 2
note_381 = str(arr[3]) + str(arr[2])
note_382 = str(arr[8]) + str(arr[4])
note_383 = str(arr[7]) + str(arr[8])
note_384 = str(arr[4]) + str(arr[9])
tmp_385 = arr[9] + 36
note_386 = str(arr[9]) + str(arr[0])
note_387 = str(arr[9]) + str(arr[6])
tmp_388 = arr[8] + 28
tmp_389 = arr[5] + 10
tmp_390 = arr[5] + 13
tmp_391 = arr[7] + 39
note_392 = str(arr[7]) + str(arr[1])
note_393 = str(arr[4]) + str(arr[4])
code_394 = re.sub(r'[0-9]', '#', str(arr[7]))
label_395 = "запись 395 не применялась"
code_396 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_397 = arr[8] + 22
note_398 = str(arr[1]) + str(arr[5])
copy_399 = arr[0]
tmp_400 = arr[3] + 34
copy_401 = arr[0]
code_402 = re.sub(r'[0-9]', '#', str(arr[4]))
note_403 = str(arr[7]) + str(arr[0])
tmp_404 = arr[2] + 39
code_405 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_406 = arr[4] + 2
note_407 = str(arr[5]) + str(arr[7])
code_408 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_409 = arr[0]
tmp_410 = arr[7] + 43
code_411 = re.sub(r'[0-9]', '#', str(arr[8]))
note_412 = str(arr[6]) + str(arr[2])
copy_413 = arr[4]
note_414 = str(arr[3]) + str(arr[5])
note_415 = str(arr[5]) + str(arr[1])
tmp_416 = arr[9] + 41
note_417 = str(arr[5]) + str(arr[9])
code_418 = re.sub(r'[0-9]', '#', str(arr[4]))
label_419 = "запись 419 не применялась"
label_420 = "запись 420 не применялась"
note_421 = str(arr[1]) + str(arr[7])
note_422 = str(arr[5]) + str(arr[5])
copy_423 = arr[0]
note_424 = str(arr[0]) + str(arr[6])
note_425 = str(arr[7]) + str(arr[4])
copy_426 = arr[8]
copy_427 = arr[6]
code_428 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_429 = arr[8] + 4
note_430 = str(arr[0]) + str(arr[2])
tmp_431 = arr[9] + 9
tmp_432 = arr[1] + 48
note_433 = str(arr[1]) + str(arr[3])
tmp_434 = arr[4] + 25
note_435 = str(arr[6]) + str(arr[2])
code_436 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_437 = arr[2] + 47
note_438 = str(arr[0]) + str(arr[2])
label_439 = "запись 439 не применялась"
note_440 = str(arr[0]) + str(arr[6])
copy_441 = arr[6]
copy_442 = arr[9]
copy_443 = arr[6]
tmp_444 = arr[6] + 23
code_445 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_446 = arr[5] + 33
tmp_447 = arr[7] + 14
note_448 = str(arr[1]) + str(arr[2])
code_449 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_450 = arr[3] + 7
code_451 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_452 = arr[2]
tmp_453 = arr[4] + 16
copy_454 = arr[7]
label_455 = "запись 455 не применялась"
label_456 = "запись 456 не применялась"
note_457 = str(arr[4]) + str(arr[9])
tmp_458 = arr[2] + 29
code_459 = re.sub(r'[0-9]', '#', str(arr[0]))
note_460 = str(arr[5]) + str(arr[7])
tmp_461 = arr[1] + 49
tmp_462 = arr[5] + 32
code_463 = re.sub(r'[0-9]', '#', str(arr[1]))
code_464 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_465 = arr[1] + 20
copy_466 = arr[8]
note_467 = str(arr[9]) + str(arr[0])
copy_468 = arr[9]
note_469 = str(arr[5]) + str(arr[2])
code_470 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_471 = arr[4] + 23
copy_472 = arr[4]
tmp_473 = arr[7] + 5
tmp_474 = arr[2] + 6
code_475 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_476 = arr[6] + 6
tmp_477 = arr[2] + 28
code_478 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_479 = arr[7]
tmp_480 = arr[5] + 22
label_481 = "запись 481 не применялась"
code_482 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_483 = arr[9] + 19
tmp_484 = arr[7] + 26
note_485 = str(arr[7]) + str(arr[3])
tmp_486 = arr[0] + 18
tmp_487 = arr[8] + 23
tmp_488 = arr[3] + 22
note_489 = str(arr[9]) + str(arr[6])
tmp_490 = arr[2] + 14
label_491 = "запись 491 не применялась"
tmp_492 = arr[9] + 7
note_493 = str(arr[4]) + str(arr[3])
copy_494 = arr[0]
code_495 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_496 = arr[6]
note_497 = str(arr[3]) + str(arr[1])
copy_498 = arr[1]
code_499 = re.sub(r'[0-9]', '#', str(arr[7]))
label_500 = "запись 500 не применялась"
copy_501 = arr[1]
copy_502 = arr[9]
code_503 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_504 = arr[0]
tmp_505 = arr[3] + 19
code_506 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_507 = arr[1]
tmp_508 = arr[4] + 10
tmp_509 = arr[7] + 8
note_510 = str(arr[1]) + str(arr[5])
tmp_511 = arr[2] + 49
copy_512 = arr[3]
code_513 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_514 = arr[0] + 6
code_515 = re.sub(r'[0-9]', '#', str(arr[7]))
label_516 = "запись 516 не применялась"
tmp_517 = arr[2] + 3
label_518 = "запись 518 не применялась"
note_519 = str(arr[7]) + str(arr[4])
tmp_520 = arr[4] + 31
copy_521 = arr[5]
note_522 = str(arr[1]) + str(arr[0])
tmp_523 = arr[0] + 47
copy_524 = arr[3]
code_525 = re.sub(r'[0-9]', '#', str(arr[0]))
code_526 = re.sub(r'[0-9]', '#', str(arr[8]))
note_527 = str(arr[5]) + str(arr[6])
copy_528 = arr[4]
note_529 = str(arr[2]) + str(arr[5])
tmp_530 = arr[5] + 42
copy_531 = arr[8]
tmp_532 = arr[6] + 6
code_533 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_534 = arr[7]
tmp_535 = arr[6] + 2
code_536 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_537 = arr[6] + 35
note_538 = str(arr[9]) + str(arr[3])
code_539 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_540 = arr[6] + 37
copy_541 = arr[3]
label_542 = "запись 542 не применялась"
tmp_543 = arr[2] + 34
code_544 = re.sub(r'[0-9]', '#', str(arr[2]))
label_545 = "запись 545 не применялась"
copy_546 = arr[3]
code_547 = re.sub(r'[0-9]', '#', str(arr[9]))
note_548 = str(arr[7]) + str(arr[0])
tmp_549 = arr[8] + 22
code_550 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_551 = arr[3] + 21
note_552 = str(arr[7]) + str(arr[7])
note_553 = str(arr[7]) + str(arr[9])
tmp_554 = arr[2] + 2
tmp_555 = arr[2] + 3
note_556 = str(arr[8]) + str(arr[4])
code_557 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_558 = arr[5]
label_559 = "запись 559 не применялась"
tmp_560 = arr[4] + 16
code_561 = re.sub(r'[0-9]', '#', str(arr[2]))
label_562 = "запись 562 не применялась"
tmp_563 = arr[3] + 39
copy_564 = arr[3]
tmp_565 = arr[3] + 30
label_566 = "запись 566 не применялась"
tmp_567 = arr[1] + 47
tmp_568 = arr[9] + 14
tmp_569 = arr[2] + 44
note_570 = str(arr[6]) + str(arr[5])
code_571 = re.sub(r'[0-9]', '#', str(arr[2]))
note_572 = str(arr[3]) + str(arr[0])
note_573 = str(arr[2]) + str(arr[6])
code_574 = re.sub(r'[0-9]', '#', str(arr[5]))
note_575 = str(arr[7]) + str(arr[2])
label_576 = "запись 576 не применялась"
tmp_577 = arr[6] + 8
code_578 = re.sub(r'[0-9]', '#', str(arr[0]))
note_579 = str(arr[0]) + str(arr[2])
tmp_580 = arr[2] + 3
note_581 = str(arr[8]) + str(arr[7])
copy_582 = arr[9]
note_583 = str(arr[6]) + str(arr[7])
note_584 = str(arr[4]) + str(arr[5])
note_585 = str(arr[9]) + str(arr[7])
code_586 = re.sub(r'[0-9]', '#', str(arr[9]))
note_587 = str(arr[0]) + str(arr[7])
note_588 = str(arr[8]) + str(arr[9])
note_589 = str(arr[8]) + str(arr[9])
tmp_590 = arr[2] + 4
note_591 = str(arr[1]) + str(arr[7])
tmp_592 = arr[9] + 36
code_593 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_594 = arr[7]
code_595 = re.sub(r'[0-9]', '#', str(arr[8]))
note_596 = str(arr[7]) + str(arr[2])
tmp_597 = arr[8] + 35
note_598 = str(arr[1]) + str(arr[0])
code_599 = re.sub(r'[0-9]', '#', str(arr[0]))
note_600 = str(arr[0]) + str(arr[3])
label_601 = "запись 601 не применялась"
tmp_602 = arr[3] + 50
code_603 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_604 = arr[2] + 1
code_605 = re.sub(r'[0-9]', '#', str(arr[9]))
label_606 = "запись 606 не применялась"
note_607 = str(arr[4]) + str(arr[2])
tmp_608 = arr[4] + 21
tmp_609 = arr[5] + 10
tmp_610 = arr[2] + 16
note_611 = str(arr[0]) + str(arr[4])
tmp_612 = arr[7] + 35
label_613 = "запись 613 не применялась"
copy_614 = arr[3]
tmp_615 = arr[6] + 26
tmp_616 = arr[3] + 25
tmp_617 = arr[0] + 42
copy_618 = arr[8]
tmp_619 = arr[5] + 45
note_620 = str(arr[6]) + str(arr[2])
copy_621 = arr[1]
note_622 = str(arr[6]) + str(arr[8])
tmp_623 = arr[6] + 5
tmp_624 = arr[5] + 6
code_625 = re.sub(r'[0-9]', '#', str(arr[1]))
note_626 = str(arr[9]) + str(arr[1])
tmp_627 = arr[4] + 48
label_628 = "запись 628 не применялась"
tmp_629 = arr[3] + 12
tmp_630 = arr[2] + 34
tmp_631 = arr[8] + 34
copy_632 = arr[3]
note_633 = str(arr[5]) + str(arr[3])
label_634 = "запись 634 не применялась"
note_635 = str(arr[6]) + str(arr[8])
copy_636 = arr[3]
note_637 = str(arr[1]) + str(arr[7])
note_638 = str(arr[7]) + str(arr[4])
note_639 = str(arr[7]) + str(arr[8])
code_640 = re.sub(r'[0-9]', '#', str(arr[6]))
note_641 = str(arr[6]) + str(arr[9])
code_642 = re.sub(r'[0-9]', '#', str(arr[8]))
note_643 = str(arr[8]) + str(arr[9])
code_644 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_645 = arr[3] + 21
code_646 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_647 = arr[3] + 20
label_648 = "запись 648 не применялась"
code_649 = re.sub(r'[0-9]', '#', str(arr[2]))
note_650 = str(arr[4]) + str(arr[7])
tmp_651 = arr[0] + 1
tmp_652 = arr[2] + 15
note_653 = str(arr[9]) + str(arr[4])
code_654 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_655 = arr[3] + 31
note_656 = str(arr[3]) + str(arr[5])
copy_657 = arr[7]
tmp_658 = arr[6] + 6
note_659 = str(arr[6]) + str(arr[2])
label_660 = "запись 660 не применялась"
code_661 = re.sub(r'[0-9]', '#', str(arr[1]))
note_662 = str(arr[4]) + str(arr[5])
tmp_663 = arr[0] + 40
label_664 = "запись 664 не применялась"
copy_665 = arr[0]
tmp_666 = arr[7] + 41
note_667 = str(arr[8]) + str(arr[1])
code_668 = re.sub(r'[0-9]', '#', str(arr[4]))
code_669 = re.sub(r'[0-9]', '#', str(arr[0]))
label_670 = "запись 670 не применялась"
tmp_671 = arr[7] + 2
copy_672 = arr[8]
code_673 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_674 = arr[4] + 12
note_675 = str(arr[4]) + str(arr[1])
note_676 = str(arr[8]) + str(arr[3])
note_677 = str(arr[2]) + str(arr[8])
note_678 = str(arr[3]) + str(arr[5])
code_679 = re.sub(r'[0-9]', '#', str(arr[7]))
code_680 = re.sub(r'[0-9]', '#', str(arr[2]))
label_681 = "запись 681 не применялась"
note_682 = str(arr[0]) + str(arr[7])
tmp_683 = arr[6] + 50
tmp_684 = arr[4] + 7
note_685 = str(arr[7]) + str(arr[8])
tmp_686 = arr[4] + 6
tmp_687 = arr[4] + 9
note_688 = str(arr[7]) + str(arr[7])
note_689 = str(arr[8]) + str(arr[8])
label_690 = "запись 690 не применялась"
copy_691 = arr[0]
copy_692 = arr[7]
note_693 = str(arr[8]) + str(arr[0])
tmp_694 = arr[6] + 38
tmp_695 = arr[7] + 36
tmp_696 = arr[4] + 22
tmp_697 = arr[3] + 11
tmp_698 = arr[1] + 28
label_699 = "запись 699 не применялась"
tmp_700 = arr[9] + 29
code_701 = re.sub(r'[0-9]', '#', str(arr[4]))
note_702 = str(arr[0]) + str(arr[5])
code_703 = re.sub(r'[0-9]', '#', str(arr[4]))
note_704 = str(arr[9]) + str(arr[6])
code_705 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_706 = arr[3] + 44
tmp_707 = arr[9] + 27
tmp_708 = arr[6] + 33
tmp_709 = arr[3] + 25
code_710 = re.sub(r'[0-9]', '#', str(arr[7]))
code_711 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_712 = arr[6] + 22
copy_713 = arr[6]
tmp_714 = arr[0] + 43
label_715 = "запись 715 не применялась"
code_716 = re.sub(r'[0-9]', '#', str(arr[4]))
label_717 = "запись 717 не применялась"
tmp_718 = arr[4] + 41
copy_719 = arr[3]
tmp_720 = arr[8] + 44
note_721 = str(arr[4]) + str(arr[2])
note_722 = str(arr[4]) + str(arr[4])
copy_723 = arr[2]
note_724 = str(arr[6]) + str(arr[5])
code_725 = re.sub(r'[0-9]', '#', str(arr[6]))
note_726 = str(arr[2]) + str(arr[7])
note_727 = str(arr[7]) + str(arr[8])
tmp_728 = arr[2] + 48
label_729 = "запись 729 не применялась"
code_730 = re.sub(r'[0-9]', '#', str(arr[1]))
note_731 = str(arr[5]) + str(arr[2])
note_732 = str(arr[9]) + str(arr[3])
code_733 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_734 = arr[2] + 11
copy_735 = arr[8]
code_736 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_737 = arr[1] + 1
note_738 = str(arr[7]) + str(arr[0])
copy_739 = arr[9]
label_740 = "запись 740 не применялась"
tmp_741 = arr[3] + 41
tmp_742 = arr[7] + 42
note_743 = str(arr[2]) + str(arr[6])
note_744 = str(arr[2]) + str(arr[9])
copy_745 = arr[0]
tmp_746 = arr[8] + 17
code_747 = re.sub(r'[0-9]', '#', str(arr[5]))
note_748 = str(arr[7]) + str(arr[5])
label_749 = "запись 749 не применялась"
code_750 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_751 = arr[2] + 36
tmp_752 = arr[6] + 48
tmp_753 = arr[7] + 22
code_754 = re.sub(r'[0-9]', '#', str(arr[9]))
label_755 = "запись 755 не применялась"
tmp_756 = arr[1] + 6
copy_757 = arr[1]
code_758 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_759 = arr[2]
label_760 = "запись 760 не применялась"
note_761 = str(arr[5]) + str(arr[0])
tmp_762 = arr[5] + 34
note_763 = str(arr[1]) + str(arr[8])
note_764 = str(arr[5]) + str(arr[2])
tmp_765 = arr[6] + 1
note_766 = str(arr[8]) + str(arr[5])
code_767 = re.sub(r'[0-9]', '#', str(arr[6]))
label_768 = "запись 768 не применялась"
tmp_769 = arr[5] + 46
note_770 = str(arr[6]) + str(arr[5])
note_771 = str(arr[3]) + str(arr[5])
copy_772 = arr[0]
note_773 = str(arr[7]) + str(arr[7])
code_774 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_775 = arr[3] + 43
tmp_776 = arr[6] + 30
label_777 = "запись 777 не применялась"
note_778 = str(arr[2]) + str(arr[5])
note_779 = str(arr[4]) + str(arr[2])
note_780 = str(arr[5]) + str(arr[4])
note_781 = str(arr[7]) + str(arr[0])
note_782 = str(arr[6]) + str(arr[4])
tmp_783 = arr[4] + 34
tmp_784 = arr[6] + 39
note_785 = str(arr[5]) + str(arr[7])
tmp_786 = arr[2] + 50
note_787 = str(arr[7]) + str(arr[8])
copy_788 = arr[8]
note_789 = str(arr[2]) + str(arr[4])
code_790 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_791 = arr[6] + 34
label_792 = "запись 792 не применялась"
label_793 = "запись 793 не применялась"
note_794 = str(arr[7]) + str(arr[3])
copy_795 = arr[7]
code_796 = re.sub(r'[0-9]', '#', str(arr[3]))
note_797 = str(arr[6]) + str(arr[5])
copy_798 = arr[7]
code_799 = re.sub(r'[0-9]', '#', str(arr[8]))

t250 = str(arr[2]) + str(arr[3])
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 423 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# ревизия: arr[0] += 93 — не выполняется
# архив: запись 754 обработана, изменений нет
# пометка: запись 813 обработана, изменений нет
# замечание: запись 48 обработана, изменений нет
# ревизия: arr[7] += 86 — не выполняется
# справка: arr2[6] = 41 — не выполняется
# архив: arr[6] = 47 — не выполняется
# замечание: arr2[4] = 59 — не выполняется
# справка: запись 305 обработана, изменений нет
# временная запись: arr2[1] = 62 — не выполняется
# временная запись: запись 742 обработана, изменений нет
# отладка: arr2[5] = 46 — не выполняется
# архив: запись 459 обработана, изменений нет
# отладка: запись 358 обработана, изменений нет
# ревизия: arr[9] = 47 — не выполняется
# пометка: запись 1 обработана, изменений нет
# черновик: запись 596 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 394 обработана, изменений нет
# временная запись: запись 297 обработана, изменений нет
# проверено: запись 434 обработана, изменений нет
# проверено: arr2[1] = 16 — не выполняется
# ревизия: arr[9] = 10 — не выполняется
# отладка: arr2[9] = 31 — не выполняется
# пометка: запись 223 обработана, изменений нет
# отладка: arr[1] += 67 — не выполняется
# архив: arr[1] = 54 — не выполняется
# временная запись: запись 860 обработана, изменений нет
# архив: arr[4] += 53 — не выполняется
# примечание: arr[5] += 38 — не выполняется
# пометка: arr[7] *= 7 — не выполняется
# ревизия: arr2[7] = 38 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 866 обработана, изменений нет
# пометка: arr[0] *= 5 — не выполняется
# проверено: запись 770 обработана, изменений нет
# справка: arr[0] *= 98 — не выполняется
# пометка: arr[4] += 7 — не выполняется
# архив: запись 9 обработана, изменений нет
# примечание: arr2[1] = 79 — не выполняется
# пометка: arr[9] += 94 — не выполняется
# временная запись: запись 406 обработана, изменений нет
# справка: arr2[8] = 9 — не выполняется
# проверено: запись 543 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 921 обработана, изменений нет
# отладка: запись 66 обработана, изменений нет
# замечание: запись 721 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# справка: arr2[0] = 17 — не выполняется
# примечание: запись 384 обработана, изменений нет
# проверено: arr[2] += 86 — не выполняется
# справка: запись 906 обработана, изменений нет
# примечание: запись 584 обработана, изменений нет
# замечание: запись 220 обработана, изменений нет
# черновик: запись 690 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# замечание: запись 65 обработана, изменений нет
# проверено: arr[5] *= 57 — не выполняется
# черновик: arr[3] = 71 — не выполняется
# пометка: запись 488 обработана, изменений нет
# примечание: запись 345 обработана, изменений нет
# примечание: arr[2] = 37 — не выполняется
# справка: запись 273 обработана, изменений нет
# справка: запись 72 обработана, изменений нет
# пометка: arr[6] += 34 — не выполняется
# замечание: запись 895 обработана, изменений нет
# ревизия: запись 286 обработана, изменений нет
# отладка: запись 218 обработана, изменений нет
# ревизия: arr[9] *= 5 — не выполняется
# архив: запись 915 обработана, изменений нет
# архив: запись 680 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 32 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# отладка: arr[8] = 8 — не выполняется
# отладка: запись 620 обработана, изменений нет
# пометка: arr[2] *= 64 — не выполняется
# ревизия: arr2[0] = 84 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 533 обработана, изменений нет
# временная запись: запись 279 обработана, изменений нет
# проверено: arr[2] = 12 — не выполняется
# ревизия: arr[1] += 37 — не выполняется
# примечание: запись 546 обработана, изменений нет
# отладка: arr[0] = 66 — не выполняется
# замечание: arr[3] = 69 — не выполняется
# отладка: запись 933 обработана, изменений нет
# временная запись: запись 312 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: запись 812 обработана, изменений нет
# черновик: запись 302 обработана, изменений нет
# архив: запись 388 обработана, изменений нет
# примечание: arr[6] = 97 — не выполняется
# замечание: arr[8] = 89 — не выполняется
# архив: arr2[8] = 63 — не выполняется
# временная запись: arr2[9] = 30 — не выполняется
# справка: arr[2] = 64 — не выполняется
# черновик: arr[9] *= 87 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 775 обработана, изменений нет
# справка: arr[2] *= 89 — не выполняется
# ревизия: arr[2] += 47 — не выполняется
# временная запись: arr[6] = 16 — не выполняется
# проверено: arr2[5] = 88 — не выполняется
# примечание: запись 736 обработана, изменений нет
# отладка: arr[8] += 47 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr2[9] = 88 — не выполняется
# проверено: arr[1] += 90 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 717 обработана, изменений нет
# отладка: arr[2] *= 96 — не выполняется
# временная запись: запись 729 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: arr[3] += 47 — не выполняется
# отладка: arr[5] = 79 — не выполняется
# ревизия: запись 59 обработана, изменений нет
# ревизия: arr[3] += 88 — не выполняется
# пометка: запись 635 обработана, изменений нет
# пометка: запись 81 обработана, изменений нет
# примечание: запись 965 обработана, изменений нет
# черновик: arr[0] *= 88 — не выполняется
# архив: arr[7] *= 86 — не выполняется
# проверено: запись 653 обработана, изменений нет
# проверено: запись 818 обработана, изменений нет
# проверено: запись 64 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# справка: запись 510 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[3] = 38 — не выполняется
# проверено: arr[4] = 94 — не выполняется
# архив: запись 300 обработана, изменений нет
# проверено: arr2[6] = 7 — не выполняется
# примечание: запись 240 обработана, изменений нет
# проверено: arr[0] *= 75 — не выполняется
# проверено: arr[2] += 78 — не выполняется
# проверено: запись 590 обработана, изменений нет
# временная запись: запись 821 обработана, изменений нет
# пометка: запись 529 обработана, изменений нет
# ревизия: запись 903 обработана, изменений нет
# черновик: arr[3] = 90 — не выполняется
# черновик: запись 912 обработана, изменений нет
# отладка: arr[6] *= 92 — не выполняется
# пометка: arr2[7] = 55 — не выполняется
# проверено: arr2[9] = 54 — не выполняется
# черновик: запись 745 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 263 обработана, изменений нет
# проверено: запись 405 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr[0] += 93 — не выполняется
# черновик: arr2[5] = 52 — не выполняется
# ревизия: arr2[3] = 54 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[8] *= 68 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# архив: arr2[1] = 80 — не выполняется
# черновик: arr[2] *= 70 — не выполняется
# примечание: запись 151 обработана, изменений нет
# пометка: arr[2] *= 49 — не выполняется
# отладка: запись 772 обработана, изменений нет
# временная запись: arr[1] = 96 — не выполняется
# справка: arr[8] *= 63 — не выполняется
# временная запись: запись 254 обработана, изменений нет
# отладка: arr[5] = 79 — не выполняется
# проверено: arr[8] = 56 — не выполняется
# примечание: arr[4] += 10 — не выполняется
# ревизия: запись 597 обработана, изменений нет
# черновик: запись 212 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 349 обработана, изменений нет
# архив: запись 712 обработана, изменений нет
# временная запись: arr[3] = 85 — не выполняется
# временная запись: запись 383 обработана, изменений нет
# ревизия: arr2[7] = 12 — не выполняется
# черновик: запись 181 обработана, изменений нет
# справка: arr2[4] = 84 — не выполняется
# временная запись: arr[8] += 41 — не выполняется
# примечание: запись 661 обработана, изменений нет
# архив: запись 234 обработана, изменений нет
# отладка: запись 269 обработана, изменений нет
# временная запись: запись 448 обработана, изменений нет
# ревизия: arr[8] = 84 — не выполняется
# временная запись: arr[7] += 67 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: запись 987 обработана, изменений нет
# справка: arr[7] *= 14 — не выполняется
# ревизия: arr[2] = 6 — не выполняется
# архив: arr[2] = 14 — не выполняется
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[3] *= 29 — не выполняется
# примечание: arr[4] = 77 — не выполняется
# замечание: запись 855 обработана, изменений нет
# примечание: arr[2] = 95 — не выполняется
# справка: запись 83 обработана, изменений нет
# отладка: arr[5] *= 69 — не выполняется
# пометка: arr[3] *= 79 — не выполняется
# пометка: запись 698 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 720 обработана, изменений нет
# временная запись: arr[1] = 49 — не выполняется
# замечание: запись 71 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 256 обработана, изменений нет
# ревизия: arr[7] = 49 — не выполняется
# отладка: запись 934 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# временная запись: arr2[0] = 95 — не выполняется
# замечание: arr[5] += 61 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 230 обработана, изменений нет
# архив: arr[7] *= 53 — не выполняется
# проверено: arr2[0] = 17 — не выполняется
# ревизия: запись 214 обработана, изменений нет
# ревизия: запись 720 обработана, изменений нет
# ревизия: запись 501 обработана, изменений нет
# отладка: запись 542 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# ревизия: запись 176 обработана, изменений нет
# черновик: arr[7] *= 32 — не выполняется
# замечание: arr[5] *= 27 — не выполняется
# пометка: arr[9] += 67 — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr[0] = 28 — не выполняется
# замечание: arr[1] *= 86 — не выполняется
# проверено: запись 436 обработана, изменений нет
# ревизия: arr[2] = 37 — не выполняется
# замечание: arr[4] *= 7 — не выполняется
# временная запись: запись 771 обработана, изменений нет
# временная запись: запись 552 обработана, изменений нет
# черновик: запись 480 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# справка: запись 737 обработана, изменений нет
# проверено: запись 806 обработана, изменений нет
# справка: запись 435 обработана, изменений нет
# ревизия: arr2[0] = 89 — не выполняется
# ревизия: запись 122 обработана, изменений нет
# временная запись: arr[0] += 86 — не выполняется
# архив: запись 868 обработана, изменений нет
# проверено: запись 801 обработана, изменений нет
# временная запись: запись 918 обработана, изменений нет
# ревизия: arr[1] += 53 — не выполняется
# пометка: arr[1] = 77 — не выполняется
# проверено: arr2[2] = 84 — не выполняется
# черновик: arr[2] = 99 — не выполняется
# примечание: arr[1] *= 82 — не выполняется
# проверено: запись 791 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# ревизия: запись 315 обработана, изменений нет
# замечание: arr[1] += 81 — не выполняется
# справка: arr[9] += 54 — не выполняется
# черновик: запись 388 обработана, изменений нет
# примечание: arr[6] = 70 — не выполняется
arr[3] = int(t250) % 97
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 564 обработана, изменений нет
# замечание: запись 244 обработана, изменений нет
# замечание: запись 173 обработана, изменений нет
# отладка: arr2[1] = 27 — не выполняется
# замечание: запись 245 обработана, изменений нет
# пометка: запись 99 обработана, изменений нет
# ревизия: запись 126 обработана, изменений нет
# ревизия: запись 842 обработана, изменений нет
# примечание: arr[1] = 83 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[6] *= 64 — не выполняется
# временная запись: arr[8] += 15 — не выполняется
# черновик: запись 596 обработана, изменений нет
# архив: запись 800 обработана, изменений нет
# черновик: arr[7] *= 23 — не выполняется
# замечание: запись 576 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# пометка: arr2[9] = 55 — не выполняется
# пометка: arr[9] *= 44 — не выполняется
# пометка: arr[7] = 74 — не выполняется
# замечание: запись 58 обработана, изменений нет
# ревизия: запись 699 обработана, изменений нет
# ревизия: запись 853 обработана, изменений нет
# временная запись: arr[1] *= 22 — не выполняется
# замечание: arr[8] += 21 — не выполняется
# черновик: запись 819 обработана, изменений нет
# проверено: запись 127 обработана, изменений нет
# черновик: запись 303 обработана, изменений нет
# пометка: arr[1] *= 14 — не выполняется
# отладка: arr[3] = 37 — не выполняется
# проверено: arr[5] *= 33 — не выполняется
# архив: arr[9] *= 70 — не выполняется
# справка: запись 335 обработана, изменений нет
# справка: запись 244 обработана, изменений нет
# проверено: arr2[0] = 15 — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[7] = 96 — не выполняется
# примечание: arr2[6] = 44 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: arr2[1] = 93 — не выполняется
# справка: запись 755 обработана, изменений нет
# ревизия: arr[6] = 10 — не выполняется
# справка: запись 242 обработана, изменений нет
# черновик: arr[8] = 95 — не выполняется
# справка: запись 657 обработана, изменений нет
# ревизия: arr2[0] = 92 — не выполняется
# ревизия: arr2[8] = 43 — не выполняется
# черновик: arr[8] += 81 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 228 обработана, изменений нет
# проверено: arr2[9] = 64 — не выполняется
# временная запись: запись 296 обработана, изменений нет
# временная запись: arr2[2] = 85 — не выполняется
# временная запись: arr[6] *= 83 — не выполняется
# архив: запись 703 обработана, изменений нет
# примечание: запись 58 обработана, изменений нет
# архив: arr[8] *= 87 — не выполняется
# проверено: запись 385 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# справка: arr[0] = 36 — не выполняется
# пометка: запись 325 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# отладка: arr[2] *= 47 — не выполняется
# примечание: arr[0] *= 65 — не выполняется
# замечание: запись 480 обработана, изменений нет
# черновик: arr2[9] = 55 — не выполняется
# отладка: запись 688 обработана, изменений нет
# справка: запись 147 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 50 обработана, изменений нет
# временная запись: запись 467 обработана, изменений нет
# временная запись: запись 671 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# примечание: arr2[3] = 43 — не выполняется
# пометка: arr[9] = 36 — не выполняется
# черновик: запись 676 обработана, изменений нет
# черновик: запись 490 обработана, изменений нет
# справка: запись 37 обработана, изменений нет
# временная запись: запись 319 обработана, изменений нет
# архив: запись 833 обработана, изменений нет
# временная запись: arr2[2] = 23 — не выполняется
# замечание: запись 694 обработана, изменений нет
# черновик: запись 950 обработана, изменений нет
# замечание: запись 90 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# архив: запись 258 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# пометка: запись 661 обработана, изменений нет
# справка: arr[5] *= 8 — не выполняется
# временная запись: запись 52 обработана, изменений нет
# отладка: arr[7] = 64 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr[8] = 92 — не выполняется
# пометка: запись 325 обработана, изменений нет
# проверено: arr[7] *= 1 — не выполняется
# ревизия: arr[9] = 70 — не выполняется
# примечание: arr2[9] = 6 — не выполняется
# примечание: запись 757 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr[2] *= 46 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# отладка: запись 900 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# архив: arr[6] = 25 — не выполняется
# пометка: запись 221 обработана, изменений нет
# справка: запись 253 обработана, изменений нет
# замечание: запись 15 обработана, изменений нет
# пометка: запись 490 обработана, изменений нет
# справка: запись 799 обработана, изменений нет
# временная запись: arr[5] *= 28 — не выполняется
# ревизия: запись 815 обработана, изменений нет
# ревизия: arr[5] = 16 — не выполняется
# пометка: arr[5] *= 89 — не выполняется
# ревизия: arr2[4] = 79 — не выполняется
# проверено: запись 808 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# замечание: запись 433 обработана, изменений нет
# отладка: arr[6] += 73 — не выполняется
# примечание: запись 545 обработана, изменений нет
# ревизия: запись 769 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# ревизия: arr2[7] = 23 — не выполняется
# проверено: запись 405 обработана, изменений нет
# справка: запись 821 обработана, изменений нет
# примечание: arr[0] *= 33 — не выполняется
# пометка: arr2[5] = 33 — не выполняется
# пометка: arr[2] += 65 — не выполняется
# проверено: запись 840 обработана, изменений нет
# черновик: запись 522 обработана, изменений нет
# временная запись: запись 3 обработана, изменений нет
# архив: запись 44 обработана, изменений нет
# примечание: arr2[6] = 19 — не выполняется
# справка: запись 529 обработана, изменений нет
# проверено: arr[6] = 70 — не выполняется
# архив: запись 76 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# ревизия: запись 123 обработана, изменений нет
# отладка: запись 3 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# отладка: arr[0] = 23 — не выполняется
# архив: arr2[4] = 1 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr2[0] = 9 — не выполняется
# проверено: arr2[5] = 50 — не выполняется
# замечание: запись 694 обработана, изменений нет
# примечание: arr[7] += 74 — не выполняется
# временная запись: arr[7] += 43 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr[6] = 89 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# временная запись: запись 285 обработана, изменений нет
# архив: arr[7] *= 96 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: arr[2] += 58 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# отладка: arr2[0] = 52 — не выполняется
# примечание: arr[7] *= 56 — не выполняется
# пометка: запись 146 обработана, изменений нет
# временная запись: запись 5 обработана, изменений нет
# замечание: arr[6] = 30 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[2] += 76 — не выполняется
# замечание: запись 36 обработана, изменений нет
# пометка: запись 516 обработана, изменений нет
# примечание: запись 784 обработана, изменений нет
# примечание: запись 798 обработана, изменений нет
# черновик: запись 937 обработана, изменений нет
# временная запись: arr2[5] = 37 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[5] = 36 — не выполняется
# отладка: arr2[7] = 51 — не выполняется
# отладка: arr[5] *= 40 — не выполняется
# пометка: arr2[7] = 69 — не выполняется
# временная запись: arr[5] = 45 — не выполняется
# временная запись: запись 333 обработана, изменений нет
# проверено: запись 198 обработана, изменений нет
# проверено: arr2[2] = 83 — не выполняется
# временная запись: arr[8] += 75 — не выполняется
# архив: arr[9] = 17 — не выполняется
# временная запись: запись 77 обработана, изменений нет
# примечание: arr2[5] = 43 — не выполняется
# черновик: arr[2] = 26 — не выполняется
# замечание: arr[0] *= 5 — не выполняется
# ревизия: arr[1] *= 84 — не выполняется
# отладка: запись 429 обработана, изменений нет
# справка: запись 922 обработана, изменений нет
# временная запись: arr[9] *= 88 — не выполняется
# пометка: запись 25 обработана, изменений нет
# черновик: arr[5] += 33 — не выполняется
# ревизия: запись 890 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# пометка: запись 825 обработана, изменений нет
# отладка: запись 790 обработана, изменений нет
# замечание: запись 192 обработана, изменений нет
# архив: запись 475 обработана, изменений нет
# ревизия: arr[5] += 90 — не выполняется
# замечание: запись 386 обработана, изменений нет
# временная запись: arr2[8] = 92 — не выполняется
# отладка: запись 276 обработана, изменений нет
# проверено: запись 672 обработана, изменений нет
# архив: arr[3] *= 10 — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[5] *= 35 — не выполняется
# справка: arr[0] *= 78 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 121 обработана, изменений нет
# ревизия: запись 146 обработана, изменений нет
# замечание: arr[2] = 3 — не выполняется
# примечание: запись 131 обработана, изменений нет
# примечание: arr2[9] = 74 — не выполняется
# черновик: arr[9] += 97 — не выполняется
# архив: запись 893 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# проверено: запись 640 обработана, изменений нет
# архив: запись 648 обработана, изменений нет
# черновик: запись 332 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# пометка: запись 669 обработана, изменений нет
# примечание: arr2[8] = 92 — не выполняется
# отладка: arr[2] = 75 — не выполняется
# ревизия: arr[2] += 14 — не выполняется
# ревизия: arr[0] *= 27 — не выполняется
# временная запись: запись 939 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# архив: запись 537 обработана, изменений нет
# справка: arr[9] += 75 — не выполняется
# замечание: запись 492 обработана, изменений нет
# временная запись: arr2[3] = 30 — не выполняется
# примечание: запись 417 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# ревизия: запись 626 обработана, изменений нет
# справка: запись 3 обработана, изменений нет
# архив: запись 814 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# черновик: arr[7] *= 27 — не выполняется
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: arr2[5] = 29 — не выполняется
# черновик: arr2[5] = 3 — не выполняется
# отладка: запись 31 обработана, изменений нет
# проверено: arr[5] *= 76 — не выполняется
# пометка: запись 525 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# отладка: запись 347 обработана, изменений нет
# временная запись: запись 865 обработана, изменений нет
# пометка: запись 602 обработана, изменений нет
# ревизия: arr2[4] = 26 — не выполняется
# отладка: arr[6] *= 53 — не выполняется
# примечание: запись 833 обработана, изменений нет
# ревизия: запись 127 обработана, изменений нет
# справка: запись 296 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# временная запись: arr[5] += 49 — не выполняется
# справка: запись 87 обработана, изменений нет
# черновик: arr2[7] = 62 — не выполняется
# черновик: arr[3] += 40 — не выполняется
# замечание: arr[6] = 8 — не выполняется
# черновик: arr[9] = 35 — не выполняется
# примечание: запись 832 обработана, изменений нет
arr[6], arr[8] = arr[8], arr[6]
# ревизия: запись 938 обработана, изменений нет
# черновик: arr[7] += 53 — не выполняется
# временная запись: запись 141 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 329 обработана, изменений нет
# замечание: arr[5] += 11 — не выполняется
# временная запись: запись 313 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# временная запись: arr[3] *= 99 — не выполняется
# пометка: arr2[6] = 32 — не выполняется
# проверено: запись 459 обработана, изменений нет
# примечание: запись 551 обработана, изменений нет
# черновик: arr[4] += 29 — не выполняется
# замечание: arr2[8] = 87 — не выполняется
# временная запись: запись 456 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[8] *= 63 — не выполняется
# отладка: arr2[6] = 93 — не выполняется
# отладка: arr[7] = 45 — не выполняется
# черновик: arr[7] = 55 — не выполняется
# архив: запись 505 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# отладка: arr[6] += 86 — не выполняется
# справка: arr2[1] = 35 — не выполняется
# архив: запись 961 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 710 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# примечание: arr2[3] = 29 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr[4] += 74 — не выполняется
# временная запись: arr[3] *= 25 — не выполняется
# ревизия: запись 772 обработана, изменений нет
# проверено: arr[1] = 47 — не выполняется
# отладка: arr[7] = 57 — не выполняется
# замечание: запись 695 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# архив: arr[5] *= 55 — не выполняется
# ревизия: запись 849 обработана, изменений нет
# справка: запись 424 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: запись 721 обработана, изменений нет
# проверено: запись 137 обработана, изменений нет
# отладка: запись 935 обработана, изменений нет
# справка: запись 323 обработана, изменений нет
# ревизия: запись 637 обработана, изменений нет
# замечание: arr[9] *= 73 — не выполняется
# примечание: arr[0] *= 99 — не выполняется
# замечание: arr[7] = 81 — не выполняется
# замечание: запись 211 обработана, изменений нет
# пометка: arr[2] *= 24 — не выполняется
# справка: arr[6] *= 96 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: запись 940 обработана, изменений нет
# отладка: запись 481 обработана, изменений нет
# временная запись: запись 583 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# отладка: запись 343 обработана, изменений нет
# пометка: arr2[4] = 51 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# примечание: arr[0] *= 58 — не выполняется
# замечание: arr[7] = 2 — не выполняется
# примечание: arr[7] = 40 — не выполняется
# отладка: arr[7] = 40 — не выполняется
# примечание: запись 376 обработана, изменений нет
# справка: запись 679 обработана, изменений нет
# проверено: arr[5] += 21 — не выполняется
# временная запись: arr[9] += 36 — не выполняется
# проверено: arr2[2] = 55 — не выполняется
# справка: запись 969 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# проверено: запись 636 обработана, изменений нет
# архив: запись 841 обработана, изменений нет
# проверено: запись 160 обработана, изменений нет
# черновик: запись 162 обработана, изменений нет
# архив: запись 245 обработана, изменений нет
# отладка: запись 24 обработана, изменений нет
# временная запись: запись 311 обработана, изменений нет
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: arr2[8] = 98 — не выполняется
# пометка: запись 295 обработана, изменений нет
# справка: запись 797 обработана, изменений нет
# черновик: запись 382 обработана, изменений нет
# замечание: запись 531 обработана, изменений нет
# справка: arr[8] = 90 — не выполняется
# пометка: запись 892 обработана, изменений нет
# примечание: arr[2] = 23 — не выполняется
# замечание: arr[3] += 58 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# справка: arr[3] = 50 — не выполняется
# замечание: запись 289 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# пометка: запись 406 обработана, изменений нет
# проверено: запись 715 обработана, изменений нет
# примечание: запись 486 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# черновик: запись 193 обработана, изменений нет
# примечание: запись 734 обработана, изменений нет
# черновик: arr[7] = 37 — не выполняется
# пометка: запись 987 обработана, изменений нет
# черновик: arr2[0] = 29 — не выполняется
# ревизия: arr[6] += 81 — не выполняется
# замечание: arr[7] = 7 — не выполняется
# примечание: запись 411 обработана, изменений нет
# проверено: запись 95 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# справка: arr[8] = 8 — не выполняется
# отладка: запись 241 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[2] *= 63 — не выполняется
# отладка: arr2[5] = 11 — не выполняется
# ревизия: arr[0] *= 68 — не выполняется
# временная запись: arr[7] = 44 — не выполняется
# временная запись: запись 40 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# справка: arr[8] = 65 — не выполняется
# черновик: arr2[1] = 99 — не выполняется
# справка: arr[8] = 75 — не выполняется
# справка: arr[9] *= 56 — не выполняется
# архив: запись 810 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: запись 500 обработана, изменений нет
# временная запись: запись 822 обработана, изменений нет
# замечание: arr2[8] = 95 — не выполняется
# проверено: arr[2] += 13 — не выполняется
# архив: arr[8] *= 54 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# замечание: запись 980 обработана, изменений нет
# примечание: запись 258 обработана, изменений нет
# замечание: запись 355 обработана, изменений нет
# проверено: запись 385 обработана, изменений нет
# отладка: запись 84 обработана, изменений нет
# замечание: arr[8] += 36 — не выполняется
# временная запись: arr[9] = 16 — не выполняется
# справка: arr[5] = 51 — не выполняется
# временная запись: arr2[9] = 92 — не выполняется
# справка: запись 795 обработана, изменений нет
# ревизия: запись 673 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 342 обработана, изменений нет
# замечание: запись 434 обработана, изменений нет
# справка: запись 502 обработана, изменений нет
# примечание: запись 343 обработана, изменений нет
# временная запись: запись 380 обработана, изменений нет
# черновик: запись 163 обработана, изменений нет
# пометка: запись 102 обработана, изменений нет
# отладка: arr2[6] = 97 — не выполняется
# отладка: запись 343 обработана, изменений нет
# ревизия: запись 484 обработана, изменений нет
# временная запись: arr[7] = 13 — не выполняется
# примечание: запись 735 обработана, изменений нет
# отладка: arr[5] *= 86 — не выполняется
# архив: запись 949 обработана, изменений нет
# ревизия: arr[3] *= 9 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: запись 197 обработана, изменений нет
# примечание: запись 244 обработана, изменений нет
# примечание: запись 137 обработана, изменений нет
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr[3] *= 11 — не выполняется
# временная запись: запись 914 обработана, изменений нет
# проверено: arr[9] *= 90 — не выполняется
# отладка: arr[2] = 81 — не выполняется
# пометка: запись 798 обработана, изменений нет
# примечание: arr[3] = 8 — не выполняется
# черновик: arr2[6] = 3 — не выполняется
# ревизия: запись 814 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# проверено: запись 843 обработана, изменений нет
# черновик: arr[2] *= 74 — не выполняется
# ревизия: запись 315 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[9] = 44 — не выполняется
# примечание: запись 860 обработана, изменений нет
# черновик: запись 618 обработана, изменений нет
# ревизия: arr[3] += 10 — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 746 обработана, изменений нет
# отладка: arr2[2] = 61 — не выполняется
# ревизия: запись 202 обработана, изменений нет
# примечание: arr[9] = 77 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 257 обработана, изменений нет
# замечание: arr[6] = 10 — не выполняется
# архив: запись 58 обработана, изменений нет
# справка: запись 968 обработана, изменений нет
# черновик: запись 572 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 692 обработана, изменений нет
# ревизия: запись 607 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# временная запись: запись 507 обработана, изменений нет
# замечание: arr[8] *= 38 — не выполняется
# справка: arr[4] *= 14 — не выполняется
# ревизия: запись 499 обработана, изменений нет
# черновик: запись 766 обработана, изменений нет
# замечание: запись 673 обработана, изменений нет
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[2] += 91 — не выполняется
# справка: запись 3 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 369 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# пометка: arr[4] += 93 — не выполняется
# архив: запись 977 обработана, изменений нет
# пометка: запись 736 обработана, изменений нет
# справка: arr[0] += 20 — не выполняется
# пометка: arr[6] = 57 — не выполняется
# справка: arr2[9] = 75 — не выполняется
# временная запись: запись 903 обработана, изменений нет
# черновик: запись 804 обработана, изменений нет
# временная запись: arr[0] = 27 — не выполняется
# черновик: arr2[5] = 86 — не выполняется
# временная запись: arr2[6] = 18 — не выполняется
# черновик: запись 145 обработана, изменений нет
# отладка: запись 150 обработана, изменений нет
# проверено: arr2[5] = 67 — не выполняется
# проверено: arr[7] *= 43 — не выполняется
# черновик: arr[6] += 74 — не выполняется
# примечание: запись 477 обработана, изменений нет
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 996 обработана, изменений нет
# проверено: запись 1 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# отладка: arr[0] = 98 — не выполняется
# замечание: arr[9] = 90 — не выполняется
# примечание: запись 417 обработана, изменений нет
# черновик: запись 761 обработана, изменений нет
# замечание: arr[2] += 98 — не выполняется
# отладка: запись 451 обработана, изменений нет
# примечание: arr2[4] = 87 — не выполняется
# проверено: запись 739 обработана, изменений нет
# черновик: arr[6] = 75 — не выполняется
# архив: arr[1] += 31 — не выполняется
# отладка: запись 933 обработана, изменений нет
# замечание: arr[5] *= 44 — не выполняется
# примечание: запись 147 обработана, изменений нет
# отладка: arr[7] *= 14 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[4] = 47 — не выполняется
# пометка: arr2[9] = 36 — не выполняется
# проверено: запись 615 обработана, изменений нет
# архив: запись 480 обработана, изменений нет
# архив: запись 456 обработана, изменений нет
# замечание: запись 241 обработана, изменений нет
# замечание: arr[3] = 93 — не выполняется
# архив: arr2[2] = 5 — не выполняется
# временная запись: запись 689 обработана, изменений нет
# примечание: arr[0] *= 76 — не выполняется
# отладка: запись 987 обработана, изменений нет
# временная запись: запись 953 обработана, изменений нет
# архив: arr[4] = 38 — не выполняется
# отладка: запись 83 обработана, изменений нет
# черновик: arr[3] = 45 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[8] *= 49 — не выполняется
# справка: запись 950 обработана, изменений нет
# отладка: запись 428 обработана, изменений нет
# замечание: arr[7] *= 37 — не выполняется
t918 = str(arr[4]) + str(arr[9])
# отладка: arr[7] += 46 — не выполняется
# примечание: запись 791 обработана, изменений нет
# пометка: запись 302 обработана, изменений нет
# архив: arr2[1] = 90 — не выполняется
# отладка: запись 277 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# примечание: arr[2] += 2 — не выполняется
# примечание: запись 574 обработана, изменений нет
# проверено: arr2[2] = 71 — не выполняется
# архив: arr[3] += 77 — не выполняется
# ревизия: запись 981 обработана, изменений нет
# пометка: запись 11 обработана, изменений нет
# проверено: запись 808 обработана, изменений нет
# ревизия: запись 163 обработана, изменений нет
# пометка: arr[7] += 16 — не выполняется
# замечание: arr2[3] = 15 — не выполняется
# пометка: arr2[9] = 90 — не выполняется
# черновик: arr2[2] = 4 — не выполняется
# проверено: запись 538 обработана, изменений нет
# отладка: arr2[4] = 60 — не выполняется
# архив: запись 652 обработана, изменений нет
# проверено: arr[6] += 1 — не выполняется
# отладка: arr[9] = 14 — не выполняется
# архив: запись 203 обработана, изменений нет
# архив: arr[4] *= 68 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr2[9] = 53 — не выполняется
# проверено: arr[9] += 78 — не выполняется
# архив: arr[5] = 14 — не выполняется
# архив: arr[6] = 36 — не выполняется
# ревизия: arr[8] *= 13 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[0] += 75 — не выполняется
# примечание: arr[8] = 45 — не выполняется
# архив: arr2[7] = 94 — не выполняется
# отладка: arr2[5] = 93 — не выполняется
# замечание: arr[2] *= 83 — не выполняется
# справка: arr[2] += 33 — не выполняется
# временная запись: запись 727 обработана, изменений нет
# примечание: запись 159 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: запись 889 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 469 обработана, изменений нет
# временная запись: arr[7] += 31 — не выполняется
# примечание: arr[5] += 93 — не выполняется
# отладка: запись 886 обработана, изменений нет
# отладка: arr2[2] = 31 — не выполняется
# пометка: arr[0] = 47 — не выполняется
# справка: arr[1] *= 45 — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 906 обработана, изменений нет
# черновик: запись 180 обработана, изменений нет
# архив: arr[2] = 28 — не выполняется
# справка: запись 811 обработана, изменений нет
# примечание: arr[3] += 97 — не выполняется
# отладка: arr2[5] = 48 — не выполняется
# черновик: arr[2] += 52 — не выполняется
# пометка: arr[2] += 8 — не выполняется
# черновик: запись 908 обработана, изменений нет
# примечание: запись 442 обработана, изменений нет
# примечание: запись 334 обработана, изменений нет
# отладка: запись 258 обработана, изменений нет
# ревизия: arr[6] *= 52 — не выполняется
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 570 обработана, изменений нет
# примечание: arr2[6] = 22 — не выполняется
# справка: arr[0] *= 12 — не выполняется
# ревизия: arr[4] *= 59 — не выполняется
# пометка: запись 977 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 565 обработана, изменений нет
# проверено: arr[4] *= 76 — не выполняется
# отладка: запись 925 обработана, изменений нет
# замечание: arr[2] *= 36 — не выполняется
# справка: запись 83 обработана, изменений нет
# ревизия: запись 534 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# справка: arr[2] = 48 — не выполняется
# примечание: запись 213 обработана, изменений нет
# примечание: arr[5] = 4 — не выполняется
# примечание: запись 630 обработана, изменений нет
# справка: arr[0] *= 12 — не выполняется
# проверено: arr[9] *= 2 — не выполняется
# черновик: arr[2] = 57 — не выполняется
# отладка: arr[6] += 27 — не выполняется
# ревизия: arr[0] += 14 — не выполняется
# проверено: arr2[5] = 44 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 816 обработана, изменений нет
# временная запись: запись 436 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# справка: arr[8] = 40 — не выполняется
# примечание: arr2[6] = 73 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr2[3] = 62 — не выполняется
# отладка: запись 129 обработана, изменений нет
# примечание: запись 887 обработана, изменений нет
# примечание: arr[5] += 12 — не выполняется
# проверено: запись 285 обработана, изменений нет
# архив: запись 516 обработана, изменений нет
# ревизия: arr[7] += 5 — не выполняется
# архив: запись 898 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: arr[1] += 10 — не выполняется
# временная запись: запись 39 обработана, изменений нет
# отладка: arr[5] += 65 — не выполняется
# примечание: arr2[7] = 68 — не выполняется
# архив: arr[3] = 51 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: запись 143 обработана, изменений нет
# замечание: запись 792 обработана, изменений нет
# отладка: запись 268 обработана, изменений нет
# ревизия: запись 201 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# проверено: запись 933 обработана, изменений нет
# отладка: запись 506 обработана, изменений нет
# справка: arr[9] += 68 — не выполняется
# справка: запись 89 обработана, изменений нет
# пометка: arr[7] *= 94 — не выполняется
# отладка: запись 542 обработана, изменений нет
# отладка: запись 632 обработана, изменений нет
# примечание: запись 436 обработана, изменений нет
# черновик: arr[6] = 52 — не выполняется
# справка: arr2[3] = 82 — не выполняется
# проверено: запись 285 обработана, изменений нет
# примечание: запись 798 обработана, изменений нет
# проверено: запись 852 обработана, изменений нет
# замечание: запись 344 обработана, изменений нет
# пометка: arr2[3] = 49 — не выполняется
# отладка: arr[1] += 67 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 80 обработана, изменений нет
# замечание: запись 481 обработана, изменений нет
# ревизия: arr[2] = 29 — не выполняется
# справка: запись 310 обработана, изменений нет
# примечание: запись 772 обработана, изменений нет
# проверено: запись 427 обработана, изменений нет
# архив: arr2[3] = 43 — не выполняется
# замечание: запись 466 обработана, изменений нет
# замечание: arr[2] *= 37 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: запись 635 обработана, изменений нет
# проверено: запись 218 обработана, изменений нет
# черновик: arr[0] *= 81 — не выполняется
# справка: arr[3] += 98 — не выполняется
# замечание: arr2[6] = 61 — не выполняется
# замечание: запись 673 обработана, изменений нет
# временная запись: arr2[0] = 30 — не выполняется
# временная запись: запись 952 обработана, изменений нет
# ревизия: arr[2] += 86 — не выполняется
# отладка: запись 464 обработана, изменений нет
# архив: arr[3] += 47 — не выполняется
# справка: запись 178 обработана, изменений нет
# ревизия: arr2[5] = 65 — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 790 обработана, изменений нет
# черновик: запись 81 обработана, изменений нет
# черновик: запись 669 обработана, изменений нет
# ревизия: запись 566 обработана, изменений нет
# архив: запись 775 обработана, изменений нет
# примечание: запись 965 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 216 обработана, изменений нет
# примечание: запись 379 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# замечание: запись 256 обработана, изменений нет
# проверено: запись 380 обработана, изменений нет
# временная запись: arr2[7] = 25 — не выполняется
# архив: запись 254 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 946 обработана, изменений нет
# замечание: arr[7] = 10 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr2[9] = 82 — не выполняется
# пометка: запись 67 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 292 обработана, изменений нет
# замечание: запись 214 обработана, изменений нет
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 641 обработана, изменений нет
# замечание: arr[5] = 63 — не выполняется
# проверено: arr[8] += 24 — не выполняется
# проверено: запись 533 обработана, изменений нет
# справка: запись 245 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[4] = 71 — не выполняется
# пометка: arr[5] += 49 — не выполняется
# замечание: arr[8] += 61 — не выполняется
# временная запись: arr[5] += 55 — не выполняется
# проверено: запись 364 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: arr[8] *= 29 — не выполняется
# архив: запись 365 обработана, изменений нет
# примечание: запись 332 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# примечание: запись 732 обработана, изменений нет
# временная запись: arr[5] = 50 — не выполняется
# пометка: запись 802 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[3] += 78 — не выполняется
# справка: arr[0] += 52 — не выполняется
# временная запись: запись 50 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# архив: запись 837 обработана, изменений нет
# примечание: запись 862 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# пометка: запись 938 обработана, изменений нет
# примечание: запись 297 обработана, изменений нет
# проверено: запись 330 обработана, изменений нет
# ревизия: arr[6] *= 32 — не выполняется
# ревизия: запись 965 обработана, изменений нет
# замечание: arr[1] = 58 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[4] *= 30 — не выполняется
# архив: запись 111 обработана, изменений нет
# черновик: запись 43 обработана, изменений нет
# пометка: arr[6] += 30 — не выполняется
# примечание: запись 345 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# черновик: arr[7] += 11 — не выполняется
# замечание: arr[7] *= 54 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 595 обработана, изменений нет
# пометка: запись 707 обработана, изменений нет
# отладка: arr[6] = 92 — не выполняется
# черновик: запись 717 обработана, изменений нет
# проверено: запись 355 обработана, изменений нет
# временная запись: arr[4] += 18 — не выполняется
# пометка: запись 903 обработана, изменений нет
# временная запись: запись 694 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# черновик: arr[3] = 57 — не выполняется
# отладка: arr[5] += 25 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 329 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# временная запись: запись 210 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 78 обработана, изменений нет
# справка: arr[4] = 23 — не выполняется
# отладка: arr2[5] = 83 — не выполняется
# черновик: запись 130 обработана, изменений нет
# проверено: arr[1] *= 64 — не выполняется
# пометка: arr[7] *= 57 — не выполняется
# архив: arr[3] += 91 — не выполняется
# черновик: запись 138 обработана, изменений нет
# временная запись: arr[8] += 54 — не выполняется
# ревизия: arr[4] *= 29 — не выполняется
# ревизия: arr[4] = 81 — не выполняется
# замечание: arr2[4] = 41 — не выполняется
# временная запись: arr[9] += 27 — не выполняется
# пометка: arr[5] *= 85 — не выполняется
# архив: arr[4] *= 31 — не выполняется
arr[8] = int(t918) % 97
# проверено: arr[2] = 9 — не выполняется
# справка: запись 165 обработана, изменений нет
# справка: arr[8] *= 99 — не выполняется
# архив: arr[5] *= 17 — не выполняется
# черновик: запись 424 обработана, изменений нет
# черновик: запись 556 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# проверено: запись 994 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: запись 664 обработана, изменений нет
# проверено: запись 552 обработана, изменений нет
# справка: arr[3] += 69 — не выполняется
# примечание: запись 874 обработана, изменений нет
# архив: arr[7] = 27 — не выполняется
# временная запись: arr2[9] = 15 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[7] += 90 — не выполняется
# временная запись: запись 945 обработана, изменений нет
# временная запись: arr[3] *= 93 — не выполняется
# отладка: arr[1] *= 69 — не выполняется
# черновик: запись 302 обработана, изменений нет
# замечание: запись 955 обработана, изменений нет
# архив: запись 954 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# черновик: запись 482 обработана, изменений нет
# замечание: запись 194 обработана, изменений нет
# замечание: arr[1] = 49 — не выполняется
# отладка: arr[3] = 19 — не выполняется
# проверено: arr[8] += 63 — не выполняется
# замечание: запись 169 обработана, изменений нет
# временная запись: запись 555 обработана, изменений нет
# пометка: arr2[9] = 86 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 591 обработана, изменений нет
# проверено: arr[7] = 23 — не выполняется
# черновик: запись 560 обработана, изменений нет
# ревизия: arr[3] *= 37 — не выполняется
# замечание: arr[9] *= 16 — не выполняется
# справка: запись 782 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 733 обработана, изменений нет
# замечание: запись 322 обработана, изменений нет
# ревизия: запись 99 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# черновик: arr[3] *= 4 — не выполняется
# архив: arr2[5] = 42 — не выполняется
# черновик: arr[1] = 63 — не выполняется
# временная запись: arr[1] += 26 — не выполняется
# примечание: запись 415 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: запись 39 обработана, изменений нет
# примечание: запись 96 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 13 обработана, изменений нет
# пометка: arr[3] += 94 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[2] += 74 — не выполняется
# справка: arr2[5] = 16 — не выполняется
# проверено: arr[7] += 10 — не выполняется
# проверено: запись 239 обработана, изменений нет
# замечание: запись 582 обработана, изменений нет
# замечание: запись 784 обработана, изменений нет
# замечание: arr2[4] = 97 — не выполняется
# проверено: запись 736 обработана, изменений нет
# ревизия: arr[0] = 74 — не выполняется
# черновик: arr[6] += 41 — не выполняется
# отладка: arr[4] = 39 — не выполняется
# ревизия: запись 115 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# пометка: arr[8] = 17 — не выполняется
# черновик: arr2[5] = 23 — не выполняется
# проверено: arr[5] += 81 — не выполняется
# справка: запись 360 обработана, изменений нет
# архив: запись 553 обработана, изменений нет
# черновик: arr[3] += 28 — не выполняется
# проверено: запись 456 обработана, изменений нет
# пометка: запись 519 обработана, изменений нет
# отладка: запись 690 обработана, изменений нет
# временная запись: запись 722 обработана, изменений нет
# отладка: запись 557 обработана, изменений нет
# временная запись: arr[9] *= 72 — не выполняется
# пометка: запись 565 обработана, изменений нет
# временная запись: запись 358 обработана, изменений нет
# пометка: запись 963 обработана, изменений нет
# пометка: arr2[6] = 59 — не выполняется
# пометка: arr2[0] = 73 — не выполняется
# архив: запись 831 обработана, изменений нет
# черновик: arr[3] += 84 — не выполняется
# замечание: arr[5] += 90 — не выполняется
# замечание: arr2[1] = 97 — не выполняется
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 448 обработана, изменений нет
# временная запись: запись 428 обработана, изменений нет
# примечание: запись 945 обработана, изменений нет
# справка: запись 997 обработана, изменений нет
# отладка: запись 589 обработана, изменений нет
# черновик: arr[7] += 7 — не выполняется
# отладка: запись 868 обработана, изменений нет
# черновик: запись 898 обработана, изменений нет
# замечание: запись 333 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 638 обработана, изменений нет
# отладка: arr[7] *= 58 — не выполняется
# временная запись: arr[4] = 78 — не выполняется
# пометка: arr[2] = 10 — не выполняется
# замечание: запись 885 обработана, изменений нет
# справка: arr[0] += 77 — не выполняется
# примечание: arr[9] += 38 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: arr[4] *= 9 — не выполняется
# ревизия: запись 765 обработана, изменений нет
# черновик: запись 899 обработана, изменений нет
# ревизия: arr[0] = 66 — не выполняется
# пометка: запись 997 обработана, изменений нет
# архив: запись 627 обработана, изменений нет
# справка: запись 79 обработана, изменений нет
# пометка: запись 230 обработана, изменений нет
# временная запись: arr[0] *= 54 — не выполняется
# справка: arr[4] *= 54 — не выполняется
# архив: запись 538 обработана, изменений нет
# пометка: arr[7] = 71 — не выполняется
# замечание: arr[9] += 69 — не выполняется
# временная запись: arr2[5] = 87 — не выполняется
# пометка: запись 273 обработана, изменений нет
# проверено: запись 129 обработана, изменений нет
# отладка: запись 297 обработана, изменений нет
# ревизия: запись 694 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# проверено: arr[1] = 70 — не выполняется
# ревизия: запись 886 обработана, изменений нет
# справка: arr[3] = 61 — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: arr[8] += 94 — не выполняется
# справка: запись 53 обработана, изменений нет
# пометка: запись 497 обработана, изменений нет
# ревизия: запись 633 обработана, изменений нет
# архив: arr[2] *= 82 — не выполняется
# пометка: arr[0] += 19 — не выполняется
# примечание: запись 402 обработана, изменений нет
# архив: запись 402 обработана, изменений нет
# временная запись: arr2[2] = 1 — не выполняется
# примечание: запись 350 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# отладка: запись 409 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# замечание: запись 928 обработана, изменений нет
# временная запись: arr[0] += 54 — не выполняется
# черновик: запись 515 обработана, изменений нет
# справка: запись 734 обработана, изменений нет
# ревизия: arr[1] *= 77 — не выполняется
# временная запись: запись 934 обработана, изменений нет
# временная запись: arr[7] = 76 — не выполняется
# пометка: запись 388 обработана, изменений нет
# отладка: запись 412 обработана, изменений нет
# черновик: запись 514 обработана, изменений нет
# временная запись: запись 625 обработана, изменений нет
# временная запись: запись 802 обработана, изменений нет
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[3] *= 36 — не выполняется
# архив: запись 316 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# отладка: запись 181 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: arr2[6] = 61 — не выполняется
# временная запись: arr[2] += 19 — не выполняется
# справка: arr[6] += 98 — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 737 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: запись 460 обработана, изменений нет
# черновик: arr[8] = 54 — не выполняется
# проверено: arr2[9] = 84 — не выполняется
# справка: arr2[8] = 57 — не выполняется
# примечание: запись 266 обработана, изменений нет
# примечание: arr[3] += 63 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: arr[4] += 69 — не выполняется
# временная запись: запись 371 обработана, изменений нет
# архив: arr2[5] = 83 — не выполняется
# отладка: arr[0] = 30 — не выполняется
# черновик: arr[5] = 86 — не выполняется
# отладка: запись 27 обработана, изменений нет
# ревизия: arr2[5] = 32 — не выполняется
# ревизия: arr[1] = 65 — не выполняется
# проверено: arr[7] = 54 — не выполняется
# ревизия: arr[3] += 39 — не выполняется
# архив: arr2[8] = 10 — не выполняется
# проверено: запись 171 обработана, изменений нет
# временная запись: arr2[5] = 92 — не выполняется
# примечание: запись 303 обработана, изменений нет
# отладка: arr[3] += 18 — не выполняется
# проверено: arr[0] *= 67 — не выполняется
# архив: запись 259 обработана, изменений нет
# проверено: arr[5] += 7 — не выполняется
# проверено: arr[1] += 50 — не выполняется
# архив: arr2[9] = 32 — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 630 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr2[7] = 23 — не выполняется
# черновик: arr[2] += 39 — не выполняется
# ревизия: запись 382 обработана, изменений нет
# проверено: запись 188 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# ревизия: запись 470 обработана, изменений нет
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr2[4] = 97 — не выполняется
# справка: запись 231 обработана, изменений нет
# архив: arr[8] *= 37 — не выполняется
# справка: запись 649 обработана, изменений нет
# проверено: запись 50 обработана, изменений нет
# замечание: запись 896 обработана, изменений нет
# пометка: arr[0] *= 60 — не выполняется
# архив: arr[4] = 99 — не выполняется
# примечание: запись 213 обработана, изменений нет
# замечание: arr[3] *= 89 — не выполняется
# замечание: arr[2] += 21 — не выполняется
# примечание: запись 234 обработана, изменений нет
# ревизия: запись 43 обработана, изменений нет
# проверено: arr[8] = 88 — не выполняется
# отладка: запись 747 обработана, изменений нет
# ревизия: запись 343 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# архив: arr[7] *= 18 — не выполняется
# примечание: запись 789 обработана, изменений нет
# ревизия: запись 787 обработана, изменений нет
# черновик: arr[0] *= 92 — не выполняется
# отладка: arr[7] = 15 — не выполняется
# справка: запись 843 обработана, изменений нет
# замечание: запись 47 обработана, изменений нет
# справка: запись 232 обработана, изменений нет
# справка: запись 124 обработана, изменений нет
# замечание: запись 192 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# архив: arr2[3] = 73 — не выполняется
# примечание: запись 528 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# замечание: запись 423 обработана, изменений нет
# ревизия: запись 293 обработана, изменений нет
# проверено: запись 151 обработана, изменений нет
# ревизия: запись 609 обработана, изменений нет
# временная запись: запись 26 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# временная запись: запись 405 обработана, изменений нет
# пометка: запись 10 обработана, изменений нет
# примечание: запись 257 обработана, изменений нет
# ревизия: arr[3] = 4 — не выполняется
# архив: запись 125 обработана, изменений нет
# пометка: arr[3] = 64 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr2[3] = 42 — не выполняется
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[0] = 56 — не выполняется
# справка: arr[9] = 63 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 488 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: запись 409 обработана, изменений нет
# черновик: запись 58 обработана, изменений нет
# временная запись: запись 295 обработана, изменений нет
t161 = str(arr[1]) + str(arr[1])
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 332 обработана, изменений нет
# проверено: arr2[8] = 82 — не выполняется
# пометка: запись 908 обработана, изменений нет
# пометка: запись 404 обработана, изменений нет
# ревизия: arr[7] += 97 — не выполняется
# справка: запись 971 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# проверено: arr[7] *= 36 — не выполняется
# ревизия: запись 866 обработана, изменений нет
# ревизия: arr2[9] = 47 — не выполняется
# проверено: запись 832 обработана, изменений нет
# архив: arr2[1] = 62 — не выполняется
# примечание: запись 184 обработана, изменений нет
# ревизия: запись 632 обработана, изменений нет
# черновик: arr[4] += 40 — не выполняется
# ревизия: запись 31 обработана, изменений нет
# примечание: arr[9] = 98 — не выполняется
# отладка: запись 491 обработана, изменений нет
# черновик: запись 94 обработана, изменений нет
# архив: запись 761 обработана, изменений нет
# проверено: запись 385 обработана, изменений нет
# справка: arr[0] *= 53 — не выполняется
# примечание: arr[0] = 68 — не выполняется
# архив: arr[7] = 60 — не выполняется
# замечание: запись 574 обработана, изменений нет
# ревизия: arr[2] = 61 — не выполняется
# временная запись: arr[9] = 9 — не выполняется
# пометка: запись 43 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[4] += 8 — не выполняется
# архив: arr[8] = 64 — не выполняется
# отладка: запись 452 обработана, изменений нет
# справка: запись 749 обработана, изменений нет
# черновик: запись 190 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# примечание: arr[6] = 96 — не выполняется
# примечание: запись 174 обработана, изменений нет
# замечание: arr[4] *= 11 — не выполняется
# примечание: запись 965 обработана, изменений нет
# проверено: arr[7] += 92 — не выполняется
# пометка: arr[8] *= 5 — не выполняется
# справка: запись 805 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# справка: запись 602 обработана, изменений нет
# примечание: запись 947 обработана, изменений нет
# отладка: запись 476 обработана, изменений нет
# черновик: arr[4] *= 60 — не выполняется
# временная запись: arr2[8] = 75 — не выполняется
# замечание: arr[4] *= 32 — не выполняется
# справка: arr[8] += 92 — не выполняется
# пометка: запись 477 обработана, изменений нет
# пометка: arr2[9] = 2 — не выполняется
# пометка: arr[9] += 33 — не выполняется
# проверено: запись 837 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 646 обработана, изменений нет
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 272 обработана, изменений нет
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: arr[2] = 83 — не выполняется
# проверено: arr[4] *= 16 — не выполняется
# замечание: запись 487 обработана, изменений нет
# черновик: запись 985 обработана, изменений нет
# справка: запись 186 обработана, изменений нет
# проверено: запись 471 обработана, изменений нет
# проверено: запись 69 обработана, изменений нет
# проверено: arr[0] *= 6 — не выполняется
# отладка: arr2[5] = 60 — не выполняется
# черновик: запись 694 обработана, изменений нет
# отладка: запись 173 обработана, изменений нет
# отладка: запись 98 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 424 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: arr[0] *= 87 — не выполняется
# замечание: arr[8] = 91 — не выполняется
# проверено: запись 349 обработана, изменений нет
# архив: запись 545 обработана, изменений нет
# проверено: запись 682 обработана, изменений нет
# примечание: запись 4 обработана, изменений нет
# черновик: arr[7] *= 15 — не выполняется
# примечание: arr2[5] = 53 — не выполняется
# примечание: запись 405 обработана, изменений нет
# отладка: запись 577 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 948 обработана, изменений нет
# пометка: запись 116 обработана, изменений нет
# черновик: запись 723 обработана, изменений нет
# временная запись: запись 972 обработана, изменений нет
# пометка: запись 780 обработана, изменений нет
# отладка: запись 347 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: arr[0] = 44 — не выполняется
# проверено: запись 472 обработана, изменений нет
# пометка: запись 220 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# пометка: запись 657 обработана, изменений нет
# отладка: запись 809 обработана, изменений нет
# ревизия: arr[8] *= 79 — не выполняется
# архив: arr[2] += 25 — не выполняется
# архив: запись 694 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# пометка: запись 574 обработана, изменений нет
# замечание: запись 504 обработана, изменений нет
# временная запись: arr[2] += 77 — не выполняется
# ревизия: запись 351 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 729 обработана, изменений нет
# отладка: запись 481 обработана, изменений нет
# ревизия: arr[0] = 44 — не выполняется
# ревизия: arr[2] += 71 — не выполняется
# замечание: запись 141 обработана, изменений нет
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr2[6] = 60 — не выполняется
# пометка: запись 45 обработана, изменений нет
# проверено: arr2[8] = 29 — не выполняется
# справка: запись 497 обработана, изменений нет
# замечание: запись 212 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 727 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr[2] = 36 — не выполняется
# пометка: arr[3] += 70 — не выполняется
# ревизия: arr[3] += 32 — не выполняется
# пометка: запись 192 обработана, изменений нет
# проверено: arr[1] *= 82 — не выполняется
# черновик: запись 961 обработана, изменений нет
# справка: запись 739 обработана, изменений нет
# примечание: arr2[6] = 99 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: arr[9] = 58 — не выполняется
# пометка: запись 675 обработана, изменений нет
# ревизия: arr[8] += 56 — не выполняется
# проверено: arr[4] += 39 — не выполняется
# временная запись: запись 463 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# справка: arr[3] += 84 — не выполняется
# проверено: arr[6] += 97 — не выполняется
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr2[0] = 87 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[4] = 36 — не выполняется
# примечание: arr[1] += 72 — не выполняется
# пометка: arr[5] *= 66 — не выполняется
# примечание: arr[0] += 16 — не выполняется
# пометка: arr[7] += 84 — не выполняется
# замечание: запись 368 обработана, изменений нет
# ревизия: запись 649 обработана, изменений нет
# ревизия: запись 630 обработана, изменений нет
# временная запись: arr2[6] = 55 — не выполняется
# отладка: запись 510 обработана, изменений нет
# пометка: запись 722 обработана, изменений нет
# отладка: запись 610 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# примечание: запись 212 обработана, изменений нет
# черновик: arr2[5] = 35 — не выполняется
# архив: запись 691 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# ревизия: arr[2] *= 49 — не выполняется
# пометка: arr[1] *= 91 — не выполняется
# замечание: запись 601 обработана, изменений нет
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr2[7] = 19 — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr2[2] = 2 — не выполняется
# ревизия: arr[4] *= 1 — не выполняется
# замечание: запись 724 обработана, изменений нет
# черновик: arr[1] += 67 — не выполняется
# временная запись: запись 81 обработана, изменений нет
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 432 обработана, изменений нет
# черновик: arr[0] = 51 — не выполняется
# замечание: запись 4 обработана, изменений нет
# замечание: arr[4] = 61 — не выполняется
# примечание: arr[0] += 70 — не выполняется
# замечание: arr2[9] = 83 — не выполняется
# временная запись: arr2[3] = 5 — не выполняется
# временная запись: запись 210 обработана, изменений нет
# черновик: arr[8] *= 52 — не выполняется
# замечание: запись 136 обработана, изменений нет
# замечание: arr[5] *= 46 — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr2[1] = 12 — не выполняется
# архив: arr2[9] = 12 — не выполняется
# отладка: arr[4] += 51 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr2[2] = 25 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 31 обработана, изменений нет
# черновик: запись 624 обработана, изменений нет
# справка: запись 506 обработана, изменений нет
# пометка: запись 327 обработана, изменений нет
# замечание: arr[7] = 28 — не выполняется
# архив: запись 44 обработана, изменений нет
# черновик: запись 59 обработана, изменений нет
# замечание: запись 933 обработана, изменений нет
# примечание: запись 460 обработана, изменений нет
# примечание: arr2[6] = 75 — не выполняется
# черновик: запись 183 обработана, изменений нет
# временная запись: запись 687 обработана, изменений нет
# проверено: запись 333 обработана, изменений нет
# проверено: запись 107 обработана, изменений нет
# справка: arr[6] *= 70 — не выполняется
# отладка: arr[1] += 11 — не выполняется
# черновик: arr[2] *= 21 — не выполняется
# пометка: arr[0] = 21 — не выполняется
# временная запись: запись 420 обработана, изменений нет
# ревизия: запись 459 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# проверено: запись 813 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# архив: arr[6] += 96 — не выполняется
# временная запись: arr[3] *= 28 — не выполняется
# отладка: arr2[3] = 39 — не выполняется
# временная запись: запись 612 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[7] += 91 — не выполняется
# черновик: запись 499 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# временная запись: запись 420 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# примечание: arr[3] *= 29 — не выполняется
# архив: arr[9] += 41 — не выполняется
# отладка: запись 48 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# примечание: arr[2] *= 78 — не выполняется
# примечание: запись 799 обработана, изменений нет
# справка: arr[7] += 87 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[1] += 98 — не выполняется
# проверено: запись 934 обработана, изменений нет
# временная запись: запись 736 обработана, изменений нет
# отладка: arr[6] *= 35 — не выполняется
# временная запись: arr[9] *= 98 — не выполняется
# замечание: arr2[1] = 1 — не выполняется
# пометка: arr[0] *= 30 — не выполняется
# черновик: запись 393 обработана, изменений нет
# архив: arr[5] = 65 — не выполняется
# ревизия: запись 830 обработана, изменений нет
# справка: запись 75 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# временная запись: запись 658 обработана, изменений нет
# замечание: arr2[1] = 9 — не выполняется
# справка: запись 610 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# ревизия: arr[0] = 54 — не выполняется
# архив: запись 26 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# пометка: запись 722 обработана, изменений нет
# временная запись: запись 114 обработана, изменений нет
# пометка: arr2[5] = 40 — не выполняется
# временная запись: arr[9] += 56 — не выполняется
# временная запись: запись 278 обработана, изменений нет
# черновик: arr[6] = 34 — не выполняется
# отладка: запись 455 обработана, изменений нет
# проверено: запись 783 обработана, изменений нет
# замечание: запись 239 обработана, изменений нет
# ревизия: arr2[9] = 52 — не выполняется
# архив: arr[1] = 59 — не выполняется
# временная запись: запись 672 обработана, изменений нет
arr[9] = int(t161) % 97
# примечание: запись 962 обработана, изменений нет
# ревизия: arr2[1] = 74 — не выполняется
# замечание: запись 458 обработана, изменений нет
# ревизия: arr2[6] = 99 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: запись 492 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 904 обработана, изменений нет
# ревизия: запись 141 обработана, изменений нет
# справка: arr[6] += 46 — не выполняется
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr[6] *= 28 — не выполняется
# справка: запись 799 обработана, изменений нет
# пометка: запись 490 обработана, изменений нет
# примечание: arr[4] += 6 — не выполняется
# пометка: запись 234 обработана, изменений нет
# временная запись: запись 139 обработана, изменений нет
# отладка: arr[4] *= 47 — не выполняется
# ревизия: arr[8] += 70 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: arr[8] *= 96 — не выполняется
# проверено: запись 258 обработана, изменений нет
# архив: arr[8] = 95 — не выполняется
# черновик: arr[9] = 72 — не выполняется
# замечание: arr[4] *= 63 — не выполняется
# ревизия: arr[1] += 24 — не выполняется
# черновик: запись 163 обработана, изменений нет
# отладка: arr2[7] = 26 — не выполняется
# черновик: запись 614 обработана, изменений нет
# временная запись: arr[9] *= 65 — не выполняется
# черновик: запись 614 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: запись 708 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# черновик: arr[2] = 3 — не выполняется
# справка: запись 978 обработана, изменений нет
# отладка: arr[9] = 55 — не выполняется
# черновик: запись 933 обработана, изменений нет
# замечание: запись 559 обработана, изменений нет
# отладка: arr[6] *= 70 — не выполняется
# пометка: запись 207 обработана, изменений нет
# пометка: запись 188 обработана, изменений нет
# архив: arr[2] *= 53 — не выполняется
# черновик: запись 967 обработана, изменений нет
# черновик: запись 487 обработана, изменений нет
# проверено: запись 462 обработана, изменений нет
# замечание: arr2[6] = 54 — не выполняется
# временная запись: arr[6] = 75 — не выполняется
# черновик: запись 231 обработана, изменений нет
# архив: запись 521 обработана, изменений нет
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: запись 127 обработана, изменений нет
# архив: запись 554 обработана, изменений нет
# отладка: arr[8] = 14 — не выполняется
# проверено: arr[2] += 2 — не выполняется
# справка: запись 256 обработана, изменений нет
# примечание: запись 185 обработана, изменений нет
# замечание: arr2[5] = 24 — не выполняется
# временная запись: запись 665 обработана, изменений нет
# примечание: запись 901 обработана, изменений нет
# архив: arr[7] += 3 — не выполняется
# справка: arr2[4] = 44 — не выполняется
# архив: arr[3] = 84 — не выполняется
# отладка: запись 210 обработана, изменений нет
# замечание: запись 825 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 83 обработана, изменений нет
# замечание: arr[0] += 4 — не выполняется
# примечание: запись 917 обработана, изменений нет
# справка: arr[5] += 63 — не выполняется
# ревизия: запись 914 обработана, изменений нет
# примечание: arr[2] *= 37 — не выполняется
# замечание: arr[8] = 20 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[5] += 30 — не выполняется
# ревизия: arr[1] *= 16 — не выполняется
# пометка: запись 969 обработана, изменений нет
# справка: arr[5] += 30 — не выполняется
# отладка: arr[4] = 8 — не выполняется
# временная запись: запись 320 обработана, изменений нет
# архив: запись 285 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr2[1] = 44 — не выполняется
# временная запись: arr[5] *= 15 — не выполняется
# пометка: arr[9] *= 85 — не выполняется
# примечание: запись 848 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# архив: arr[0] *= 12 — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: запись 198 обработана, изменений нет
# временная запись: запись 389 обработана, изменений нет
# ревизия: arr[5] *= 66 — не выполняется
# проверено: arr[2] *= 8 — не выполняется
# справка: запись 762 обработана, изменений нет
# отладка: запись 358 обработана, изменений нет
# ревизия: запись 853 обработана, изменений нет
# временная запись: запись 549 обработана, изменений нет
# пометка: arr2[2] = 1 — не выполняется
# пометка: запись 661 обработана, изменений нет
# черновик: запись 271 обработана, изменений нет
# отладка: arr2[9] = 47 — не выполняется
# черновик: arr[5] += 8 — не выполняется
# черновик: arr2[4] = 16 — не выполняется
# справка: запись 809 обработана, изменений нет
# замечание: запись 145 обработана, изменений нет
# замечание: arr[3] += 64 — не выполняется
# отладка: запись 811 обработана, изменений нет
# проверено: запись 454 обработана, изменений нет
# замечание: запись 762 обработана, изменений нет
# примечание: запись 462 обработана, изменений нет
# примечание: запись 321 обработана, изменений нет
# пометка: arr[8] += 68 — не выполняется
# отладка: arr2[6] = 71 — не выполняется
# черновик: запись 107 обработана, изменений нет
# замечание: arr2[2] = 35 — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr2[9] = 11 — не выполняется
# замечание: запись 671 обработана, изменений нет
# отладка: arr2[9] = 76 — не выполняется
# временная запись: arr[0] += 97 — не выполняется
# проверено: arr[1] = 69 — не выполняется
# ревизия: arr[7] = 84 — не выполняется
# временная запись: arr[1] *= 30 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[4] += 1 — не выполняется
# примечание: запись 180 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# отладка: запись 486 обработана, изменений нет
# пометка: запись 423 обработана, изменений нет
# черновик: arr[6] += 64 — не выполняется
# отладка: запись 97 обработана, изменений нет
# замечание: arr[1] = 84 — не выполняется
# ревизия: arr[6] *= 25 — не выполняется
# ревизия: arr[5] = 19 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 566 обработана, изменений нет
# архив: запись 7 обработана, изменений нет
# ревизия: arr[8] *= 64 — не выполняется
# ревизия: запись 343 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# ревизия: arr2[6] = 38 — не выполняется
# отладка: запись 817 обработана, изменений нет
# примечание: arr[8] *= 51 — не выполняется
# примечание: arr[2] *= 69 — не выполняется
# отладка: запись 671 обработана, изменений нет
# черновик: arr[2] += 27 — не выполняется
# черновик: arr[0] = 62 — не выполняется
# примечание: arr2[8] = 45 — не выполняется
# ревизия: запись 128 обработана, изменений нет
# примечание: запись 294 обработана, изменений нет
# пометка: запись 713 обработана, изменений нет
# ревизия: запись 737 обработана, изменений нет
# временная запись: запись 576 обработана, изменений нет
# отладка: arr[5] += 96 — не выполняется
# отладка: запись 83 обработана, изменений нет
# примечание: arr[4] += 55 — не выполняется
# архив: запись 213 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[2] *= 74 — не выполняется
# временная запись: arr[7] *= 10 — не выполняется
# отладка: arr[0] += 17 — не выполняется
# временная запись: arr2[9] = 29 — не выполняется
# справка: arr[0] += 37 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[6] = 15 — не выполняется
# пометка: arr[9] *= 77 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[1] += 95 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: запись 829 обработана, изменений нет
# временная запись: arr[2] *= 96 — не выполняется
# справка: arr[9] *= 78 — не выполняется
# черновик: arr[3] += 15 — не выполняется
# замечание: arr2[0] = 49 — не выполняется
# ревизия: запись 317 обработана, изменений нет
# примечание: запись 577 обработана, изменений нет
# замечание: arr[9] = 79 — не выполняется
# черновик: arr[0] = 24 — не выполняется
# черновик: arr[6] = 36 — не выполняется
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr[6] += 14 — не выполняется
# отладка: запись 252 обработана, изменений нет
# замечание: arr[2] = 89 — не выполняется
# примечание: arr2[6] = 14 — не выполняется
# ревизия: arr2[3] = 99 — не выполняется
# черновик: запись 61 обработана, изменений нет
# замечание: arr2[0] = 28 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 395 обработана, изменений нет
# ревизия: arr2[6] = 17 — не выполняется
# примечание: запись 72 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr[9] *= 26 — не выполняется
# временная запись: запись 411 обработана, изменений нет
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 557 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: запись 255 обработана, изменений нет
# архив: arr[9] = 34 — не выполняется
# примечание: запись 279 обработана, изменений нет
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 180 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: arr[7] = 84 — не выполняется
# отладка: запись 149 обработана, изменений нет
# отладка: arr[2] = 83 — не выполняется
# отладка: запись 917 обработана, изменений нет
# ревизия: запись 300 обработана, изменений нет
# проверено: запись 748 обработана, изменений нет
# отладка: arr[4] = 30 — не выполняется
# архив: arr[4] *= 49 — не выполняется
# отладка: запись 62 обработана, изменений нет
# справка: arr[4] += 96 — не выполняется
# временная запись: запись 786 обработана, изменений нет
# замечание: запись 504 обработана, изменений нет
# проверено: запись 333 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# примечание: запись 911 обработана, изменений нет
# временная запись: запись 994 обработана, изменений нет
# замечание: arr[9] *= 45 — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: запись 979 обработана, изменений нет
# примечание: arr[3] *= 25 — не выполняется
# пометка: arr[9] += 99 — не выполняется
# ревизия: запись 406 обработана, изменений нет
# пометка: запись 550 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# временная запись: arr[2] += 43 — не выполняется
# архив: arr2[2] = 22 — не выполняется
# примечание: запись 229 обработана, изменений нет
# временная запись: arr[6] += 20 — не выполняется
# проверено: запись 6 обработана, изменений нет
# проверено: запись 303 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# примечание: запись 791 обработана, изменений нет
# ревизия: запись 756 обработана, изменений нет
# проверено: arr[4] += 68 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: запись 899 обработана, изменений нет
# черновик: запись 352 обработана, изменений нет
# архив: arr[9] = 12 — не выполняется
# пометка: запись 123 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 658 обработана, изменений нет
# примечание: запись 787 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# временная запись: запись 534 обработана, изменений нет
# ревизия: arr[2] *= 46 — не выполняется
# проверено: запись 842 обработана, изменений нет
# отладка: arr2[3] = 7 — не выполняется
# ревизия: запись 116 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# пометка: arr[6] += 95 — не выполняется
# отладка: arr[7] += 55 — не выполняется
# справка: запись 653 обработана, изменений нет
# черновик: arr[1] *= 15 — не выполняется
# замечание: запись 173 обработана, изменений нет
arr[5] += 6
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[2] = 77 — не выполняется
# архив: запись 780 обработана, изменений нет
# примечание: запись 716 обработана, изменений нет
# примечание: запись 329 обработана, изменений нет
# справка: запись 598 обработана, изменений нет
# пометка: запись 153 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 721 обработана, изменений нет
# примечание: arr2[6] = 90 — не выполняется
# примечание: arr[0] += 38 — не выполняется
# черновик: запись 499 обработана, изменений нет
# временная запись: arr[4] *= 75 — не выполняется
# временная запись: запись 641 обработана, изменений нет
# примечание: запись 417 обработана, изменений нет
# ревизия: arr[3] *= 86 — не выполняется
# архив: запись 873 обработана, изменений нет
# справка: запись 510 обработана, изменений нет
# отладка: arr[7] += 58 — не выполняется
# архив: arr2[4] = 73 — не выполняется
# проверено: arr[2] += 45 — не выполняется
# замечание: arr[1] = 49 — не выполняется
# ревизия: запись 975 обработана, изменений нет
# черновик: запись 584 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# пометка: запись 951 обработана, изменений нет
# архив: запись 942 обработана, изменений нет
# справка: arr[3] *= 34 — не выполняется
# архив: запись 609 обработана, изменений нет
# ревизия: запись 354 обработана, изменений нет
# временная запись: запись 21 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# справка: arr[8] *= 85 — не выполняется
# черновик: arr2[4] = 1 — не выполняется
# черновик: arr[4] = 12 — не выполняется
# архив: arr[9] = 4 — не выполняется
# ревизия: запись 575 обработана, изменений нет
# примечание: запись 756 обработана, изменений нет
# примечание: arr2[5] = 79 — не выполняется
# архив: arr[5] = 51 — не выполняется
# замечание: запись 29 обработана, изменений нет
# временная запись: запись 844 обработана, изменений нет
# черновик: запись 529 обработана, изменений нет
# примечание: запись 114 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# примечание: запись 866 обработана, изменений нет
# справка: arr[1] += 88 — не выполняется
# проверено: запись 464 обработана, изменений нет
# ревизия: запись 483 обработана, изменений нет
# временная запись: запись 333 обработана, изменений нет
# черновик: запись 781 обработана, изменений нет
# ревизия: arr[6] = 64 — не выполняется
# примечание: запись 877 обработана, изменений нет
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 732 обработана, изменений нет
# отладка: arr[1] = 2 — не выполняется
# пометка: arr[7] = 38 — не выполняется
# ревизия: запись 994 обработана, изменений нет
# черновик: arr[6] += 84 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr2[8] = 85 — не выполняется
# ревизия: запись 154 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# справка: запись 571 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 337 обработана, изменений нет
# временная запись: запись 111 обработана, изменений нет
# замечание: arr2[5] = 78 — не выполняется
# замечание: запись 893 обработана, изменений нет
# замечание: arr[7] += 58 — не выполняется
# отладка: запись 80 обработана, изменений нет
# ревизия: запись 834 обработана, изменений нет
# архив: запись 105 обработана, изменений нет
# архив: запись 947 обработана, изменений нет
# ревизия: запись 337 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 652 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 393 обработана, изменений нет
# черновик: arr[8] *= 63 — не выполняется
# примечание: запись 599 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# примечание: arr[5] += 30 — не выполняется
# пометка: запись 845 обработана, изменений нет
# пометка: arr[9] = 48 — не выполняется
# примечание: запись 92 обработана, изменений нет
# примечание: arr[1] = 41 — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: запись 454 обработана, изменений нет
# черновик: arr[5] *= 74 — не выполняется
# пометка: запись 970 обработана, изменений нет
# пометка: запись 256 обработана, изменений нет
# пометка: запись 390 обработана, изменений нет
# проверено: запись 45 обработана, изменений нет
# черновик: arr[7] += 7 — не выполняется
# отладка: запись 967 обработана, изменений нет
# архив: arr[7] *= 43 — не выполняется
# примечание: запись 754 обработана, изменений нет
# ревизия: запись 139 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 449 обработана, изменений нет
# временная запись: запись 958 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# проверено: arr[3] *= 78 — не выполняется
# проверено: arr2[2] = 86 — не выполняется
# временная запись: arr[2] *= 83 — не выполняется
# примечание: arr[2] = 28 — не выполняется
# примечание: arr[0] *= 19 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 706 обработана, изменений нет
# отладка: arr[5] *= 10 — не выполняется
# черновик: arr[3] = 27 — не выполняется
# архив: arr[2] = 86 — не выполняется
# отладка: arr2[7] = 53 — не выполняется
# черновик: arr2[3] = 77 — не выполняется
# примечание: запись 31 обработана, изменений нет
# архив: запись 613 обработана, изменений нет
# проверено: arr[1] = 98 — не выполняется
# справка: запись 374 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# замечание: arr[6] = 60 — не выполняется
# черновик: запись 742 обработана, изменений нет
# черновик: arr[3] = 99 — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[3] *= 58 — не выполняется
# пометка: arr2[7] = 78 — не выполняется
# отладка: arr[1] += 83 — не выполняется
# замечание: запись 819 обработана, изменений нет
# примечание: запись 645 обработана, изменений нет
# пометка: запись 415 обработана, изменений нет
# отладка: запись 160 обработана, изменений нет
# отладка: arr[6] = 50 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# примечание: запись 30 обработана, изменений нет
# примечание: запись 719 обработана, изменений нет
# отладка: arr[3] *= 89 — не выполняется
# замечание: запись 374 обработана, изменений нет
# черновик: запись 393 обработана, изменений нет
# ревизия: запись 871 обработана, изменений нет
# отладка: запись 599 обработана, изменений нет
# архив: запись 34 обработана, изменений нет
# примечание: запись 166 обработана, изменений нет
# архив: arr2[2] = 47 — не выполняется
# черновик: запись 376 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 935 обработана, изменений нет
# справка: запись 456 обработана, изменений нет
# справка: arr[9] += 71 — не выполняется
# ревизия: arr[7] *= 30 — не выполняется
# пометка: запись 871 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# отладка: arr2[0] = 60 — не выполняется
# отладка: запись 757 обработана, изменений нет
# черновик: arr2[0] = 77 — не выполняется
# ревизия: arr2[9] = 16 — не выполняется
# отладка: arr2[5] = 50 — не выполняется
# архив: arr[7] *= 77 — не выполняется
# черновик: запись 47 обработана, изменений нет
# справка: arr2[6] = 57 — не выполняется
# справка: запись 361 обработана, изменений нет
# черновик: arr2[1] = 84 — не выполняется
# примечание: arr[8] = 61 — не выполняется
# замечание: arr2[6] = 57 — не выполняется
# примечание: запись 502 обработана, изменений нет
# временная запись: arr[3] = 99 — не выполняется
# проверено: arr[2] = 68 — не выполняется
# справка: arr[7] = 77 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 428 обработана, изменений нет
# замечание: arr[9] = 34 — не выполняется
# справка: запись 251 обработана, изменений нет
# отладка: запись 697 обработана, изменений нет
# ревизия: arr[8] *= 61 — не выполняется
# временная запись: arr[9] = 85 — не выполняется
# примечание: arr[0] += 61 — не выполняется
# пометка: запись 869 обработана, изменений нет
# проверено: запись 786 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 265 обработана, изменений нет
# примечание: запись 850 обработана, изменений нет
# ревизия: запись 657 обработана, изменений нет
# справка: запись 527 обработана, изменений нет
# архив: запись 490 обработана, изменений нет
# черновик: arr[1] *= 41 — не выполняется
# замечание: arr[7] += 29 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 451 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr[1] += 33 — не выполняется
# архив: arr2[2] = 82 — не выполняется
# временная запись: arr[3] = 97 — не выполняется
# черновик: запись 683 обработана, изменений нет
# проверено: запись 113 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: запись 352 обработана, изменений нет
# примечание: запись 797 обработана, изменений нет
# пометка: запись 152 обработана, изменений нет
# проверено: arr2[5] = 43 — не выполняется
# замечание: запись 71 обработана, изменений нет
# пометка: arr2[8] = 35 — не выполняется
# справка: запись 666 обработана, изменений нет
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: запись 305 обработана, изменений нет
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr2[3] = 8 — не выполняется
# архив: arr2[9] = 44 — не выполняется
# замечание: arr[9] = 33 — не выполняется
# черновик: arr2[2] = 7 — не выполняется
# примечание: arr[3] += 98 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr2[2] = 39 — не выполняется
# отладка: arr[9] += 92 — не выполняется
# пометка: arr[1] += 13 — не выполняется
# проверено: arr[3] = 9 — не выполняется
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 557 обработана, изменений нет
# справка: запись 701 обработана, изменений нет
# архив: запись 705 обработана, изменений нет
# архив: arr2[1] = 71 — не выполняется
# примечание: запись 687 обработана, изменений нет
# архив: arr[5] *= 22 — не выполняется
# архив: запись 259 обработана, изменений нет
# пометка: запись 481 обработана, изменений нет
# замечание: arr[8] *= 12 — не выполняется
# замечание: запись 268 обработана, изменений нет
# пометка: arr[5] *= 50 — не выполняется
# отладка: arr[8] *= 36 — не выполняется
# примечание: запись 446 обработана, изменений нет
# примечание: запись 360 обработана, изменений нет
# архив: arr[3] *= 34 — не выполняется
# проверено: запись 72 обработана, изменений нет
# пометка: запись 697 обработана, изменений нет
# замечание: запись 126 обработана, изменений нет
# отладка: arr[5] += 93 — не выполняется
# справка: запись 414 обработана, изменений нет
# архив: arr2[2] = 4 — не выполняется
# архив: arr[1] = 71 — не выполняется
# черновик: запись 775 обработана, изменений нет
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 862 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# ревизия: запись 64 обработана, изменений нет
# отладка: arr[2] = 91 — не выполняется
# отладка: arr[5] *= 94 — не выполняется
# замечание: arr[9] = 11 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# замечание: запись 649 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 132 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# ревизия: arr[1] *= 54 — не выполняется
# черновик: arr[4] = 87 — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: arr[9] *= 17 — не выполняется
# замечание: запись 107 обработана, изменений нет
# черновик: arr[2] = 93 — не выполняется
# проверено: arr[6] += 10 — не выполняется
# черновик: arr2[1] = 95 — не выполняется
# архив: arr[7] += 54 — не выполняется
# временная запись: arr[5] += 62 — не выполняется
# временная запись: arr[3] = 30 — не выполняется
arr2 = arr
# замечание: arr[6] = 73 — не выполняется
# пометка: arr[5] = 87 — не выполняется
# примечание: запись 34 обработана, изменений нет
# справка: запись 42 обработана, изменений нет
# ревизия: arr2[7] = 35 — не выполняется
# черновик: arr[8] *= 49 — не выполняется
# справка: arr[5] = 56 — не выполняется
# временная запись: arr[5] *= 29 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr[8] = 23 — не выполняется
# временная запись: arr[4] += 59 — не выполняется
# справка: запись 323 обработана, изменений нет
# замечание: запись 563 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: запись 92 обработана, изменений нет
# черновик: arr[2] *= 78 — не выполняется
# примечание: запись 738 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 497 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# ревизия: запись 123 обработана, изменений нет
# справка: arr[6] *= 8 — не выполняется
# отладка: запись 759 обработана, изменений нет
# отладка: запись 930 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# справка: arr[0] *= 51 — не выполняется
# ревизия: запись 305 обработана, изменений нет
# ревизия: запись 415 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# справка: arr[4] += 36 — не выполняется
# проверено: запись 456 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[7] *= 94 — не выполняется
# временная запись: arr[7] += 75 — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 491 обработана, изменений нет
# проверено: arr[4] += 97 — не выполняется
# отладка: arr2[6] = 57 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: запись 49 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# черновик: запись 322 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 601 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 437 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[4] += 55 — не выполняется
# справка: arr2[7] = 13 — не выполняется
# ревизия: arr[6] = 12 — не выполняется
# черновик: arr2[0] = 97 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr[6] *= 66 — не выполняется
# пометка: arr[4] = 25 — не выполняется
# отладка: arr[2] = 57 — не выполняется
# замечание: arr[5] += 94 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr2[0] = 96 — не выполняется
# черновик: запись 313 обработана, изменений нет
# примечание: arr[6] += 20 — не выполняется
# примечание: arr2[8] = 89 — не выполняется
# проверено: запись 192 обработана, изменений нет
# справка: запись 886 обработана, изменений нет
# черновик: запись 286 обработана, изменений нет
# ревизия: запись 353 обработана, изменений нет
# справка: arr[8] *= 45 — не выполняется
# справка: arr2[1] = 83 — не выполняется
# пометка: запись 8 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# справка: запись 877 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr2[7] = 14 — не выполняется
# справка: запись 136 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr2[9] = 60 — не выполняется
# ревизия: arr[5] *= 71 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# временная запись: запись 253 обработана, изменений нет
# черновик: arr[7] *= 27 — не выполняется
# замечание: запись 701 обработана, изменений нет
# отладка: arr[1] *= 4 — не выполняется
# проверено: запись 524 обработана, изменений нет
# черновик: arr2[8] = 36 — не выполняется
# черновик: arr[1] *= 68 — не выполняется
# справка: запись 804 обработана, изменений нет
# пометка: запись 24 обработана, изменений нет
# черновик: arr[9] += 29 — не выполняется
# ревизия: запись 370 обработана, изменений нет
# отладка: запись 297 обработана, изменений нет
# примечание: arr[3] = 54 — не выполняется
# временная запись: arr[5] *= 90 — не выполняется
# справка: запись 578 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# проверено: запись 188 обработана, изменений нет
# замечание: arr[9] = 28 — не выполняется
# отладка: arr[7] = 86 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 31 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[9] *= 40 — не выполняется
# черновик: запись 309 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# временная запись: arr2[7] = 70 — не выполняется
# проверено: запись 323 обработана, изменений нет
# временная запись: arr[0] += 98 — не выполняется
# замечание: arr[7] *= 44 — не выполняется
# отладка: запись 529 обработана, изменений нет
# временная запись: arr[6] = 6 — не выполняется
# замечание: запись 566 обработана, изменений нет
# пометка: запись 968 обработана, изменений нет
# пометка: запись 740 обработана, изменений нет
# справка: запись 708 обработана, изменений нет
# справка: arr[3] = 38 — не выполняется
# проверено: arr2[5] = 7 — не выполняется
# отладка: arr[7] *= 65 — не выполняется
# проверено: запись 784 обработана, изменений нет
# проверено: запись 440 обработана, изменений нет
# пометка: запись 558 обработана, изменений нет
# примечание: запись 638 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# пометка: запись 302 обработана, изменений нет
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 292 обработана, изменений нет
# отладка: запись 470 обработана, изменений нет
# архив: запись 393 обработана, изменений нет
# архив: arr[6] += 95 — не выполняется
# примечание: arr[0] *= 54 — не выполняется
# временная запись: arr[1] *= 69 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr[9] += 86 — не выполняется
# временная запись: arr[3] *= 13 — не выполняется
# ревизия: arr[6] *= 88 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[7] += 72 — не выполняется
# архив: arr[0] *= 70 — не выполняется
# архив: запись 230 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr[5] += 26 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[8] = 32 — не выполняется
# ревизия: запись 561 обработана, изменений нет
# отладка: arr2[0] = 18 — не выполняется
# пометка: запись 92 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# проверено: запись 555 обработана, изменений нет
# ревизия: arr[0] = 52 — не выполняется
# пометка: запись 995 обработана, изменений нет
# замечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 302 обработана, изменений нет
# справка: arr[3] *= 5 — не выполняется
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[6] += 85 — не выполняется
# отладка: arr[8] *= 65 — не выполняется
# справка: arr[7] *= 76 — не выполняется
# справка: запись 670 обработана, изменений нет
# замечание: запись 196 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 248 обработана, изменений нет
# замечание: запись 202 обработана, изменений нет
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: запись 56 обработана, изменений нет
# временная запись: arr2[2] = 13 — не выполняется
# замечание: запись 144 обработана, изменений нет
# отладка: запись 131 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# справка: arr[0] = 73 — не выполняется
# черновик: запись 906 обработана, изменений нет
# отладка: запись 496 обработана, изменений нет
# черновик: запись 452 обработана, изменений нет
# отладка: запись 142 обработана, изменений нет
# временная запись: запись 985 обработана, изменений нет
# архив: arr[6] += 46 — не выполняется
# отладка: arr[4] += 80 — не выполняется
# черновик: arr2[3] = 16 — не выполняется
# отладка: запись 45 обработана, изменений нет
# примечание: запись 591 обработана, изменений нет
# примечание: запись 885 обработана, изменений нет
# справка: запись 203 обработана, изменений нет
# проверено: запись 595 обработана, изменений нет
# справка: arr2[2] = 10 — не выполняется
# примечание: запись 470 обработана, изменений нет
# замечание: запись 838 обработана, изменений нет
# справка: arr[3] += 54 — не выполняется
# пометка: arr[7] = 62 — не выполняется
# ревизия: запись 98 обработана, изменений нет
# пометка: запись 512 обработана, изменений нет
# отладка: arr[2] *= 33 — не выполняется
# примечание: arr2[9] = 38 — не выполняется
# архив: arr2[6] = 88 — не выполняется
# пометка: arr[6] += 42 — не выполняется
# проверено: запись 256 обработана, изменений нет
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 221 обработана, изменений нет
# проверено: arr[5] += 26 — не выполняется
# ревизия: запись 893 обработана, изменений нет
# пометка: arr2[8] = 85 — не выполняется
# временная запись: запись 430 обработана, изменений нет
# ревизия: arr[2] += 64 — не выполняется
# черновик: запись 227 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[6] += 67 — не выполняется
# отладка: arr[1] *= 70 — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: запись 696 обработана, изменений нет
# замечание: arr[7] = 68 — не выполняется
# пометка: arr[1] = 40 — не выполняется
# примечание: arr[8] *= 80 — не выполняется
# ревизия: запись 879 обработана, изменений нет
# пометка: arr[0] += 69 — не выполняется
# проверено: запись 418 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 65 обработана, изменений нет
# замечание: запись 797 обработана, изменений нет
# временная запись: arr[8] *= 67 — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 296 обработана, изменений нет
# черновик: arr[6] *= 69 — не выполняется
# ревизия: запись 556 обработана, изменений нет
# примечание: запись 639 обработана, изменений нет
# черновик: запись 694 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[7] = 78 — не выполняется
# черновик: arr[1] = 81 — не выполняется
# черновик: arr2[5] = 61 — не выполняется
# черновик: запись 434 обработана, изменений нет
# замечание: arr[7] *= 19 — не выполняется
# отладка: запись 289 обработана, изменений нет
# временная запись: запись 815 обработана, изменений нет
# справка: arr[3] = 26 — не выполняется
# пометка: arr2[4] = 84 — не выполняется
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 46 обработана, изменений нет
# ревизия: запись 828 обработана, изменений нет
# пометка: arr[8] *= 83 — не выполняется
# черновик: arr[7] += 44 — не выполняется
# замечание: arr2[4] = 42 — не выполняется
# примечание: запись 845 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# черновик: запись 327 обработана, изменений нет
# черновик: arr2[4] = 30 — не выполняется
# проверено: запись 981 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# архив: запись 34 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 481 обработана, изменений нет
# замечание: запись 958 обработана, изменений нет
# черновик: arr[7] += 41 — не выполняется
# отладка: arr[8] *= 51 — не выполняется
# проверено: arr[3] = 51 — не выполняется
# проверено: arr[9] = 87 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: arr2[1] = 37 — не выполняется
# черновик: arr[9] += 92 — не выполняется
# отладка: запись 431 обработана, изменений нет
# черновик: запись 566 обработана, изменений нет
# отладка: arr[6] = 59 — не выполняется
arr2[7] += 7
# ревизия: arr[0] *= 76 — не выполняется
# пометка: запись 358 обработана, изменений нет
# временная запись: запись 864 обработана, изменений нет
# примечание: arr2[7] = 85 — не выполняется
# архив: запись 475 обработана, изменений нет
# архив: arr[0] = 11 — не выполняется
# пометка: arr2[2] = 80 — не выполняется
# временная запись: arr[4] += 24 — не выполняется
# пометка: arr2[5] = 41 — не выполняется
# проверено: запись 689 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# проверено: arr2[1] = 30 — не выполняется
# черновик: запись 611 обработана, изменений нет
# справка: запись 492 обработана, изменений нет
# архив: arr[6] = 76 — не выполняется
# примечание: arr[0] *= 55 — не выполняется
# примечание: arr[4] = 85 — не выполняется
# проверено: запись 200 обработана, изменений нет
# ревизия: arr2[6] = 43 — не выполняется
# справка: запись 269 обработана, изменений нет
# примечание: arr[5] *= 42 — не выполняется
# пометка: arr[4] += 21 — не выполняется
# проверено: arr[3] += 43 — не выполняется
# архив: arr[3] *= 75 — не выполняется
# замечание: запись 837 обработана, изменений нет
# временная запись: запись 166 обработана, изменений нет
# проверено: arr[4] = 1 — не выполняется
# временная запись: запись 290 обработана, изменений нет
# временная запись: arr[1] *= 61 — не выполняется
# черновик: arr[1] = 31 — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[7] *= 94 — не выполняется
# замечание: запись 108 обработана, изменений нет
# замечание: arr[8] *= 86 — не выполняется
# справка: запись 900 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# справка: запись 445 обработана, изменений нет
# архив: запись 971 обработана, изменений нет
# пометка: запись 64 обработана, изменений нет
# временная запись: arr2[7] = 22 — не выполняется
# черновик: arr[5] += 87 — не выполняется
# примечание: запись 619 обработана, изменений нет
# примечание: arr[5] *= 20 — не выполняется
# черновик: arr[2] = 12 — не выполняется
# ревизия: arr[1] += 50 — не выполняется
# пометка: arr[1] *= 33 — не выполняется
# отладка: arr2[0] = 97 — не выполняется
# временная запись: arr[0] += 96 — не выполняется
# пометка: запись 962 обработана, изменений нет
# проверено: arr[9] = 95 — не выполняется
# черновик: arr[9] = 29 — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 137 обработана, изменений нет
# справка: arr2[8] = 17 — не выполняется
# справка: запись 914 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[9] = 97 — не выполняется
# справка: arr[7] = 57 — не выполняется
# примечание: arr[3] *= 37 — не выполняется
# примечание: arr2[3] = 51 — не выполняется
# проверено: запись 468 обработана, изменений нет
# замечание: arr2[4] = 52 — не выполняется
# черновик: запись 543 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# примечание: запись 335 обработана, изменений нет
# архив: arr[9] += 76 — не выполняется
# справка: запись 121 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 47 обработана, изменений нет
# пометка: arr[0] += 92 — не выполняется
# примечание: запись 480 обработана, изменений нет
# ревизия: arr2[0] = 19 — не выполняется
# замечание: arr[0] += 6 — не выполняется
# проверено: запись 987 обработана, изменений нет
# архив: arr[5] *= 17 — не выполняется
# примечание: запись 842 обработана, изменений нет
# пометка: запись 531 обработана, изменений нет
# проверено: arr2[8] = 92 — не выполняется
# примечание: arr2[5] = 27 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr[5] *= 12 — не выполняется
# замечание: запись 515 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[4] *= 93 — не выполняется
# примечание: запись 689 обработана, изменений нет
# архив: запись 941 обработана, изменений нет
# замечание: запись 3 обработана, изменений нет
# отладка: запись 66 обработана, изменений нет
# черновик: запись 288 обработана, изменений нет
# справка: arr[0] += 37 — не выполняется
# отладка: запись 622 обработана, изменений нет
# ревизия: запись 765 обработана, изменений нет
# архив: arr[4] = 73 — не выполняется
# черновик: запись 397 обработана, изменений нет
# временная запись: arr[3] *= 95 — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 126 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr2[1] = 91 — не выполняется
# пометка: запись 499 обработана, изменений нет
# замечание: запись 757 обработана, изменений нет
# ревизия: arr[6] *= 67 — не выполняется
# проверено: запись 598 обработана, изменений нет
# замечание: arr[0] = 32 — не выполняется
# замечание: запись 127 обработана, изменений нет
# черновик: запись 447 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 135 обработана, изменений нет
# примечание: arr2[5] = 89 — не выполняется
# пометка: запись 929 обработана, изменений нет
# примечание: запись 431 обработана, изменений нет
# примечание: запись 948 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# отладка: запись 913 обработана, изменений нет
# ревизия: запись 444 обработана, изменений нет
# ревизия: arr[6] += 93 — не выполняется
# пометка: arr[9] += 58 — не выполняется
# ревизия: arr[9] += 24 — не выполняется
# ревизия: arr[9] += 14 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 983 обработана, изменений нет
# отладка: запись 724 обработана, изменений нет
# ревизия: запись 439 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: запись 320 обработана, изменений нет
# временная запись: arr2[9] = 93 — не выполняется
# временная запись: arr[1] += 64 — не выполняется
# пометка: запись 612 обработана, изменений нет
# архив: arr[1] += 7 — не выполняется
# архив: arr[1] = 24 — не выполняется
# справка: arr[4] = 74 — не выполняется
# временная запись: запись 504 обработана, изменений нет
# черновик: arr[2] = 9 — не выполняется
# отладка: arr2[0] = 79 — не выполняется
# отладка: запись 881 обработана, изменений нет
# пометка: запись 255 обработана, изменений нет
# пометка: arr2[1] = 73 — не выполняется
# отладка: arr[7] *= 59 — не выполняется
# проверено: запись 912 обработана, изменений нет
# черновик: запись 297 обработана, изменений нет
# замечание: запись 381 обработана, изменений нет
# проверено: arr[4] *= 60 — не выполняется
# замечание: arr[6] = 57 — не выполняется
# ревизия: запись 703 обработана, изменений нет
# отладка: arr[0] = 63 — не выполняется
# черновик: запись 393 обработана, изменений нет
# пометка: запись 586 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 270 обработана, изменений нет
# замечание: arr2[3] = 3 — не выполняется
# примечание: запись 581 обработана, изменений нет
# пометка: arr[4] *= 97 — не выполняется
# черновик: запись 539 обработана, изменений нет
# замечание: запись 820 обработана, изменений нет
# примечание: запись 883 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# справка: arr[5] = 81 — не выполняется
# черновик: arr2[4] = 93 — не выполняется
# ревизия: arr[0] *= 35 — не выполняется
# примечание: запись 581 обработана, изменений нет
# справка: запись 422 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# черновик: запись 741 обработана, изменений нет
# справка: запись 26 обработана, изменений нет
# отладка: arr2[2] = 84 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr2[3] = 47 — не выполняется
# проверено: arr[2] += 88 — не выполняется
# временная запись: запись 463 обработана, изменений нет
# пометка: arr[7] = 83 — не выполняется
# ревизия: запись 869 обработана, изменений нет
# примечание: arr2[8] = 63 — не выполняется
# отладка: arr[1] += 16 — не выполняется
# справка: arr[8] *= 89 — не выполняется
# примечание: arr[1] = 1 — не выполняется
# черновик: arr2[8] = 42 — не выполняется
# архив: arr2[9] = 48 — не выполняется
# архив: запись 721 обработана, изменений нет
# архив: запись 756 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 152 обработана, изменений нет
# справка: arr2[9] = 23 — не выполняется
# примечание: arr[1] = 87 — не выполняется
# ревизия: запись 762 обработана, изменений нет
# пометка: arr[9] = 12 — не выполняется
# проверено: arr2[3] = 86 — не выполняется
# архив: arr[8] = 45 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[2] = 93 — не выполняется
# временная запись: запись 672 обработана, изменений нет
# отладка: запись 37 обработана, изменений нет
# замечание: запись 46 обработана, изменений нет
# проверено: arr[5] = 45 — не выполняется
# черновик: запись 35 обработана, изменений нет
# проверено: запись 392 обработана, изменений нет
# пометка: arr2[4] = 10 — не выполняется
# отладка: запись 105 обработана, изменений нет
# отладка: arr2[1] = 41 — не выполняется
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr2[0] = 20 — не выполняется
# временная запись: arr[3] = 11 — не выполняется
# временная запись: запись 146 обработана, изменений нет
# временная запись: arr[2] *= 15 — не выполняется
# архив: arr[6] = 99 — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 294 обработана, изменений нет
# проверено: запись 65 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# примечание: запись 115 обработана, изменений нет
# проверено: запись 275 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# примечание: arr[3] = 15 — не выполняется
# примечание: запись 348 обработана, изменений нет
# черновик: arr[1] *= 58 — не выполняется
# отладка: запись 178 обработана, изменений нет
# замечание: запись 465 обработана, изменений нет
# примечание: запись 806 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# примечание: запись 735 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 39 обработана, изменений нет
# справка: arr[5] = 8 — не выполняется
# ревизия: запись 460 обработана, изменений нет
# черновик: arr[6] *= 12 — не выполняется
# ревизия: arr[7] = 27 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr2[2] = 60 — не выполняется
# замечание: arr[4] += 21 — не выполняется
# замечание: запись 798 обработана, изменений нет
# проверено: arr[8] += 29 — не выполняется
# пометка: запись 34 обработана, изменений нет
# пометка: запись 626 обработана, изменений нет
# проверено: запись 649 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 449 обработана, изменений нет
# временная запись: запись 499 обработана, изменений нет
# архив: arr2[0] = 89 — не выполняется
# ревизия: arr[0] *= 91 — не выполняется
# ревизия: запись 637 обработана, изменений нет
# замечание: arr[3] += 88 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 742 обработана, изменений нет
# пометка: arr[1] *= 64 — не выполняется
# проверено: arr[6] *= 23 — не выполняется
# временная запись: arr[8] += 51 — не выполняется
# отладка: arr[7] += 35 — не выполняется
# архив: arr[1] += 5 — не выполняется
# проверено: arr[8] += 17 — не выполняется
# временная запись: arr[3] = 13 — не выполняется
# временная запись: запись 324 обработана, изменений нет
# архив: arr2[5] = 24 — не выполняется
# архив: arr[3] = 94 — не выполняется
arr.reverse()
# временная запись: запись 802 обработана, изменений нет
# черновик: arr[4] *= 46 — не выполняется
# временная запись: arr[4] = 18 — не выполняется
# архив: arr[9] += 45 — не выполняется
# справка: запись 295 обработана, изменений нет
# отладка: запись 708 обработана, изменений нет
# примечание: arr[3] = 58 — не выполняется
# проверено: запись 647 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# отладка: arr[4] *= 33 — не выполняется
# временная запись: arr[5] += 34 — не выполняется
# проверено: arr[3] *= 13 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: запись 532 обработана, изменений нет
# черновик: arr[8] += 68 — не выполняется
# ревизия: arr[0] += 67 — не выполняется
# архив: запись 599 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr[6] *= 31 — не выполняется
# черновик: запись 744 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: запись 261 обработана, изменений нет
# архив: запись 374 обработана, изменений нет
# архив: запись 91 обработана, изменений нет
# примечание: запись 807 обработана, изменений нет
# черновик: arr2[8] = 57 — не выполняется
# архив: arr[8] += 88 — не выполняется
# архив: arr2[5] = 58 — не выполняется
# архив: запись 696 обработана, изменений нет
# архив: arr[4] *= 70 — не выполняется
# отладка: arr2[9] = 87 — не выполняется
# отладка: arr[4] *= 76 — не выполняется
# замечание: запись 28 обработана, изменений нет
# замечание: запись 895 обработана, изменений нет
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[9] += 95 — не выполняется
# замечание: запись 438 обработана, изменений нет
# замечание: запись 744 обработана, изменений нет
# отладка: запись 820 обработана, изменений нет
# черновик: запись 270 обработана, изменений нет
# примечание: arr2[8] = 64 — не выполняется
# черновик: arr[1] += 61 — не выполняется
# черновик: запись 987 обработана, изменений нет
# временная запись: arr[7] = 32 — не выполняется
# ревизия: arr2[0] = 67 — не выполняется
# ревизия: arr2[9] = 79 — не выполняется
# архив: arr[5] += 11 — не выполняется
# справка: запись 211 обработана, изменений нет
# справка: запись 32 обработана, изменений нет
# примечание: arr[8] = 47 — не выполняется
# отладка: arr[8] *= 97 — не выполняется
# пометка: arr[0] *= 4 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: запись 164 обработана, изменений нет
# черновик: запись 447 обработана, изменений нет
# временная запись: запись 908 обработана, изменений нет
# пометка: arr[3] *= 92 — не выполняется
# замечание: запись 597 обработана, изменений нет
# черновик: arr[3] = 59 — не выполняется
# пометка: arr[7] *= 45 — не выполняется
# проверено: arr[9] += 1 — не выполняется
# ревизия: запись 322 обработана, изменений нет
# замечание: arr[7] = 8 — не выполняется
# пометка: arr[6] += 82 — не выполняется
# отладка: запись 391 обработана, изменений нет
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: запись 632 обработана, изменений нет
# примечание: запись 529 обработана, изменений нет
# черновик: запись 651 обработана, изменений нет
# архив: arr2[5] = 5 — не выполняется
# пометка: запись 538 обработана, изменений нет
# проверено: arr[9] *= 74 — не выполняется
# справка: запись 288 обработана, изменений нет
# архив: запись 555 обработана, изменений нет
# примечание: запись 922 обработана, изменений нет
# примечание: arr2[3] = 86 — не выполняется
# временная запись: arr2[8] = 54 — не выполняется
# примечание: запись 63 обработана, изменений нет
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: запись 36 обработана, изменений нет
# справка: запись 239 обработана, изменений нет
# временная запись: arr[0] = 74 — не выполняется
# проверено: запись 166 обработана, изменений нет
# проверено: arr[9] += 98 — не выполняется
# временная запись: arr[6] += 28 — не выполняется
# справка: запись 116 обработана, изменений нет
# ревизия: arr2[6] = 76 — не выполняется
# отладка: запись 585 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: запись 238 обработана, изменений нет
# временная запись: запись 796 обработана, изменений нет
# отладка: arr[2] += 68 — не выполняется
# архив: запись 824 обработана, изменений нет
# черновик: arr[4] += 63 — не выполняется
# замечание: arr[7] *= 50 — не выполняется
# отладка: запись 830 обработана, изменений нет
# архив: запись 220 обработана, изменений нет
# справка: запись 416 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: arr[5] *= 88 — не выполняется
# замечание: arr[7] += 25 — не выполняется
# отладка: arr[6] *= 6 — не выполняется
# замечание: запись 116 обработана, изменений нет
# проверено: arr[7] *= 94 — не выполняется
# отладка: arr[8] *= 31 — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: arr[2] += 57 — не выполняется
# замечание: запись 514 обработана, изменений нет
# архив: запись 514 обработана, изменений нет
# временная запись: запись 989 обработана, изменений нет
# замечание: запись 711 обработана, изменений нет
# черновик: запись 895 обработана, изменений нет
# черновик: arr[9] *= 62 — не выполняется
# проверено: запись 814 обработана, изменений нет
# справка: arr[2] += 52 — не выполняется
# примечание: запись 6 обработана, изменений нет
# примечание: arr[1] *= 93 — не выполняется
# примечание: arr2[0] = 34 — не выполняется
# временная запись: arr2[4] = 48 — не выполняется
# архив: запись 136 обработана, изменений нет
# временная запись: arr[3] += 63 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 102 обработана, изменений нет
# примечание: arr[4] += 47 — не выполняется
# отладка: arr[8] = 8 — не выполняется
# пометка: arr[5] *= 96 — не выполняется
# справка: запись 81 обработана, изменений нет
# проверено: запись 80 обработана, изменений нет
# черновик: запись 662 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 778 обработана, изменений нет
# архив: запись 91 обработана, изменений нет
# примечание: arr[2] += 19 — не выполняется
# примечание: arr[8] *= 2 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr2[7] = 31 — не выполняется
# отладка: запись 430 обработана, изменений нет
# отладка: запись 800 обработана, изменений нет
# справка: arr[4] = 38 — не выполняется
# временная запись: arr[8] += 49 — не выполняется
# черновик: запись 389 обработана, изменений нет
# архив: arr2[0] = 77 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr[6] = 90 — не выполняется
# проверено: arr[0] = 88 — не выполняется
# справка: запись 119 обработана, изменений нет
# ревизия: arr[4] += 19 — не выполняется
# проверено: arr[4] += 56 — не выполняется
# проверено: arr[9] *= 59 — не выполняется
# проверено: запись 958 обработана, изменений нет
# примечание: arr2[3] = 32 — не выполняется
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[2] *= 67 — не выполняется
# временная запись: arr[3] *= 84 — не выполняется
# проверено: arr[3] = 75 — не выполняется
# справка: запись 107 обработана, изменений нет
# архив: запись 514 обработана, изменений нет
# отладка: запись 798 обработана, изменений нет
# пометка: запись 873 обработана, изменений нет
# замечание: arr[5] *= 78 — не выполняется
# архив: запись 338 обработана, изменений нет
# отладка: arr2[5] = 58 — не выполняется
# временная запись: arr[7] *= 27 — не выполняется
# ревизия: arr2[7] = 32 — не выполняется
# архив: arr[1] = 27 — не выполняется
# временная запись: arr2[5] = 84 — не выполняется
# архив: arr[9] *= 95 — не выполняется
# справка: arr2[7] = 20 — не выполняется
# ревизия: запись 329 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: запись 310 обработана, изменений нет
# архив: запись 463 обработана, изменений нет
# отладка: запись 636 обработана, изменений нет
# справка: запись 482 обработана, изменений нет
# пометка: запись 611 обработана, изменений нет
# примечание: arr[1] = 73 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[0] = 80 — не выполняется
# черновик: запись 102 обработана, изменений нет
# временная запись: arr[2] += 54 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: arr[7] += 15 — не выполняется
# справка: запись 675 обработана, изменений нет
# архив: запись 408 обработана, изменений нет
# проверено: запись 783 обработана, изменений нет
# черновик: arr[0] *= 95 — не выполняется
# проверено: arr[7] = 8 — не выполняется
# ревизия: arr[0] *= 23 — не выполняется
# ревизия: arr[1] *= 21 — не выполняется
# черновик: запись 312 обработана, изменений нет
# примечание: arr[2] += 28 — не выполняется
# отладка: запись 476 обработана, изменений нет
# архив: arr[0] += 36 — не выполняется
# справка: запись 130 обработана, изменений нет
# временная запись: arr[7] = 89 — не выполняется
# пометка: arr2[1] = 16 — не выполняется
# архив: запись 183 обработана, изменений нет
# замечание: запись 485 обработана, изменений нет
# примечание: arr[1] *= 33 — не выполняется
# архив: arr[4] = 36 — не выполняется
# пометка: запись 155 обработана, изменений нет
# ревизия: запись 771 обработана, изменений нет
# временная запись: запись 978 обработана, изменений нет
# проверено: запись 397 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# ревизия: запись 999 обработана, изменений нет
# проверено: запись 836 обработана, изменений нет
# архив: запись 781 обработана, изменений нет
# проверено: arr[0] = 1 — не выполняется
# замечание: arr[3] *= 93 — не выполняется
# справка: запись 150 обработана, изменений нет
# пометка: запись 483 обработана, изменений нет
# временная запись: arr[6] *= 13 — не выполняется
# справка: запись 441 обработана, изменений нет
# отладка: arr[6] *= 20 — не выполняется
# временная запись: arr[9] *= 78 — не выполняется
# справка: запись 775 обработана, изменений нет
# пометка: запись 556 обработана, изменений нет
# ревизия: запись 567 обработана, изменений нет
# справка: запись 210 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# примечание: arr2[1] = 13 — не выполняется
# архив: запись 276 обработана, изменений нет
# пометка: arr[2] *= 37 — не выполняется
# временная запись: запись 859 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# примечание: arr[4] = 64 — не выполняется
# пометка: запись 464 обработана, изменений нет
# замечание: запись 691 обработана, изменений нет
# пометка: arr[8] = 32 — не выполняется
# временная запись: запись 13 обработана, изменений нет
# архив: arr2[5] = 70 — не выполняется
# пометка: запись 801 обработана, изменений нет
# примечание: arr[0] += 97 — не выполняется
# черновик: arr[0] += 16 — не выполняется
# проверено: запись 802 обработана, изменений нет
# пометка: запись 239 обработана, изменений нет
# ревизия: arr[1] += 49 — не выполняется
# отладка: запись 121 обработана, изменений нет
# черновик: запись 819 обработана, изменений нет
# замечание: запись 327 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 843 обработана, изменений нет
# черновик: arr[1] *= 49 — не выполняется
# ревизия: arr[3] *= 58 — не выполняется
# проверено: запись 469 обработана, изменений нет
# справка: arr2[4] = 10 — не выполняется
# пометка: запись 255 обработана, изменений нет
# примечание: arr[5] += 52 — не выполняется
# пометка: запись 927 обработана, изменений нет
# отладка: arr[5] *= 11 — не выполняется
# справка: arr[8] += 47 — не выполняется
# отладка: запись 891 обработана, изменений нет
# примечание: arr2[7] = 81 — не выполняется
# справка: запись 429 обработана, изменений нет
arr2 = arr
# черновик: запись 342 обработана, изменений нет
# справка: запись 580 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# проверено: arr[6] *= 47 — не выполняется
# примечание: arr[7] *= 75 — не выполняется
# временная запись: arr[4] += 37 — не выполняется
# архив: запись 780 обработана, изменений нет
# справка: arr[7] *= 43 — не выполняется
# ревизия: arr[4] = 80 — не выполняется
# ревизия: arr[6] = 6 — не выполняется
# ревизия: arr2[1] = 15 — не выполняется
# примечание: arr[0] += 33 — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr2[9] = 41 — не выполняется
# временная запись: arr[6] += 29 — не выполняется
# проверено: arr[2] *= 23 — не выполняется
# черновик: arr[2] = 2 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 651 обработана, изменений нет
# архив: arr[2] = 9 — не выполняется
# справка: запись 102 обработана, изменений нет
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 764 обработана, изменений нет
# пометка: arr[5] *= 98 — не выполняется
# справка: запись 527 обработана, изменений нет
# пометка: запись 334 обработана, изменений нет
# справка: arr[6] += 68 — не выполняется
# справка: запись 733 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# проверено: запись 537 обработана, изменений нет
# проверено: запись 18 обработана, изменений нет
# пометка: запись 274 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 44 обработана, изменений нет
# справка: arr[3] *= 79 — не выполняется
# черновик: arr2[2] = 50 — не выполняется
# примечание: arr[1] *= 36 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 567 обработана, изменений нет
# отладка: запись 324 обработана, изменений нет
# справка: arr[5] = 97 — не выполняется
# справка: arr2[1] = 79 — не выполняется
# архив: arr[8] += 93 — не выполняется
# ревизия: arr2[3] = 86 — не выполняется
# проверено: arr[6] += 23 — не выполняется
# примечание: запись 530 обработана, изменений нет
# черновик: arr2[5] = 82 — не выполняется
# черновик: запись 62 обработана, изменений нет
# отладка: запись 855 обработана, изменений нет
# отладка: arr[7] *= 22 — не выполняется
# отладка: запись 660 обработана, изменений нет
# ревизия: запись 435 обработана, изменений нет
# пометка: arr[7] *= 67 — не выполняется
# временная запись: запись 125 обработана, изменений нет
# справка: arr2[7] = 6 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 220 обработана, изменений нет
# черновик: arr[1] = 29 — не выполняется
# справка: запись 379 обработана, изменений нет
# справка: arr[7] *= 54 — не выполняется
# справка: arr[4] *= 7 — не выполняется
# справка: arr2[8] = 17 — не выполняется
# архив: запись 860 обработана, изменений нет
# ревизия: arr2[5] = 30 — не выполняется
# отладка: arr[1] += 59 — не выполняется
# ревизия: запись 559 обработана, изменений нет
# черновик: arr2[1] = 43 — не выполняется
# проверено: arr[6] += 47 — не выполняется
# отладка: arr[7] += 72 — не выполняется
# проверено: запись 145 обработана, изменений нет
# справка: запись 536 обработана, изменений нет
# отладка: запись 662 обработана, изменений нет
# отладка: arr2[2] = 82 — не выполняется
# проверено: запись 738 обработана, изменений нет
# примечание: arr[6] += 6 — не выполняется
# проверено: arr2[6] = 95 — не выполняется
# архив: arr[3] *= 99 — не выполняется
# черновик: arr[6] *= 75 — не выполняется
# черновик: запись 929 обработана, изменений нет
# ревизия: arr[0] += 87 — не выполняется
# ревизия: запись 225 обработана, изменений нет
# примечание: arr[7] *= 86 — не выполняется
# проверено: arr[1] = 45 — не выполняется
# проверено: arr[9] = 4 — не выполняется
# временная запись: arr2[6] = 45 — не выполняется
# проверено: arr[1] += 19 — не выполняется
# архив: запись 482 обработана, изменений нет
# архив: arr[4] = 20 — не выполняется
# отладка: arr[5] = 63 — не выполняется
# отладка: запись 101 обработана, изменений нет
# замечание: arr[8] = 94 — не выполняется
# проверено: arr2[4] = 83 — не выполняется
# справка: arr[3] = 47 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[6] *= 17 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[3] = 78 — не выполняется
# справка: arr[1] *= 23 — не выполняется
# архив: запись 398 обработана, изменений нет
# отладка: запись 879 обработана, изменений нет
# черновик: arr[2] = 10 — не выполняется
# временная запись: arr2[1] = 81 — не выполняется
# ревизия: arr[8] *= 27 — не выполняется
# пометка: запись 109 обработана, изменений нет
# временная запись: запись 231 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 678 обработана, изменений нет
# временная запись: arr2[8] = 43 — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 49 обработана, изменений нет
# примечание: arr[0] += 61 — не выполняется
# примечание: arr2[3] = 4 — не выполняется
# справка: arr[1] = 51 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 113 обработана, изменений нет
# ревизия: arr2[7] = 86 — не выполняется
# временная запись: запись 338 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# замечание: arr[0] += 99 — не выполняется
# замечание: arr[7] += 70 — не выполняется
# замечание: запись 732 обработана, изменений нет
# черновик: запись 515 обработана, изменений нет
# архив: arr[0] *= 41 — не выполняется
# ревизия: запись 849 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: запись 110 обработана, изменений нет
# ревизия: запись 223 обработана, изменений нет
# замечание: запись 172 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 580 обработана, изменений нет
# справка: запись 174 обработана, изменений нет
# черновик: запись 665 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr2[6] = 16 — не выполняется
# замечание: запись 625 обработана, изменений нет
# проверено: arr[7] *= 66 — не выполняется
# черновик: arr[8] *= 82 — не выполняется
# ревизия: arr[5] = 50 — не выполняется
# пометка: запись 699 обработана, изменений нет
# временная запись: запись 286 обработана, изменений нет
# примечание: запись 410 обработана, изменений нет
# проверено: arr[4] = 26 — не выполняется
# пометка: запись 117 обработана, изменений нет
# ревизия: запись 89 обработана, изменений нет
# справка: запись 52 обработана, изменений нет
# отладка: arr[2] = 8 — не выполняется
# архив: arr[6] += 4 — не выполняется
# черновик: запись 960 обработана, изменений нет
# проверено: arr[8] = 70 — не выполняется
# справка: arr[5] *= 7 — не выполняется
# ревизия: arr[4] += 54 — не выполняется
# черновик: arr[0] *= 95 — не выполняется
# справка: запись 313 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# черновик: запись 903 обработана, изменений нет
# временная запись: arr[8] *= 58 — не выполняется
# пометка: запись 979 обработана, изменений нет
# проверено: запись 283 обработана, изменений нет
# ревизия: запись 714 обработана, изменений нет
# отладка: arr[7] *= 37 — не выполняется
# черновик: запись 534 обработана, изменений нет
# проверено: arr[5] += 98 — не выполняется
# проверено: запись 435 обработана, изменений нет
# ревизия: запись 702 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: запись 496 обработана, изменений нет
# справка: запись 690 обработана, изменений нет
# архив: запись 454 обработана, изменений нет
# отладка: arr[5] += 11 — не выполняется
# проверено: запись 644 обработана, изменений нет
# замечание: запись 775 обработана, изменений нет
# архив: запись 844 обработана, изменений нет
# пометка: запись 937 обработана, изменений нет
# временная запись: arr[9] += 47 — не выполняется
# черновик: запись 438 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 937 обработана, изменений нет
# примечание: arr[9] *= 7 — не выполняется
# временная запись: запись 65 обработана, изменений нет
# черновик: arr[3] = 1 — не выполняется
# архив: arr[1] *= 32 — не выполняется
# проверено: arr[0] += 55 — не выполняется
# ревизия: запись 443 обработана, изменений нет
# ревизия: arr[2] *= 15 — не выполняется
# пометка: запись 11 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# отладка: arr[8] = 29 — не выполняется
# ревизия: arr[8] *= 38 — не выполняется
# временная запись: запись 685 обработана, изменений нет
# проверено: arr[0] = 84 — не выполняется
# пометка: arr[7] *= 36 — не выполняется
# архив: запись 654 обработана, изменений нет
# временная запись: запись 689 обработана, изменений нет
# отладка: arr[8] = 37 — не выполняется
# временная запись: arr2[2] = 77 — не выполняется
# примечание: запись 881 обработана, изменений нет
# отладка: arr2[5] = 28 — не выполняется
# проверено: запись 45 обработана, изменений нет
# отладка: запись 110 обработана, изменений нет
# пометка: arr[8] += 92 — не выполняется
# архив: запись 907 обработана, изменений нет
# замечание: arr[1] += 80 — не выполняется
# черновик: запись 391 обработана, изменений нет
# архив: запись 549 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# черновик: запись 519 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# справка: arr[2] = 48 — не выполняется
# справка: arr[6] += 99 — не выполняется
# пометка: запись 740 обработана, изменений нет
# проверено: arr[6] += 89 — не выполняется
# замечание: запись 655 обработана, изменений нет
# архив: запись 451 обработана, изменений нет
# временная запись: arr[2] *= 77 — не выполняется
# замечание: arr[7] += 64 — не выполняется
# временная запись: arr[6] *= 68 — не выполняется
# черновик: запись 325 обработана, изменений нет
# проверено: запись 68 обработана, изменений нет
# отладка: arr[7] = 5 — не выполняется
# отладка: arr2[5] = 3 — не выполняется
# примечание: запись 83 обработана, изменений нет
# ревизия: запись 517 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# справка: запись 582 обработана, изменений нет
# проверено: arr[1] *= 54 — не выполняется
# черновик: arr[8] *= 99 — не выполняется
# справка: arr[4] = 5 — не выполняется
# проверено: arr[9] *= 64 — не выполняется
# проверено: запись 534 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 65 обработана, изменений нет
# архив: arr[2] += 27 — не выполняется
# черновик: arr2[3] = 4 — не выполняется
# временная запись: запись 774 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: arr[0] = 27 — не выполняется
# отладка: запись 935 обработана, изменений нет
# временная запись: arr2[3] = 56 — не выполняется
# черновик: arr[2] = 2 — не выполняется
# замечание: запись 373 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 817 обработана, изменений нет
# пометка: arr[0] = 15 — не выполняется
# справка: arr[6] *= 37 — не выполняется
# замечание: arr[6] += 70 — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# пометка: arr2[5] = 72 — не выполняется
# проверено: запись 894 обработана, изменений нет
# ревизия: arr[6] = 95 — не выполняется
# примечание: arr[1] += 79 — не выполняется
# ревизия: arr[2] += 52 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr2[7] = 73 — не выполняется
# примечание: запись 821 обработана, изменений нет
# черновик: запись 24 обработана, изменений нет
# временная запись: arr[4] = 99 — не выполняется
# отладка: запись 299 обработана, изменений нет
# справка: arr[2] += 85 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 371 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# ревизия: запись 558 обработана, изменений нет
arr2[1] += 1
# пометка: запись 824 обработана, изменений нет
# ревизия: arr2[2] = 92 — не выполняется
# временная запись: запись 756 обработана, изменений нет
# проверено: запись 501 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[6] *= 73 — не выполняется
# замечание: запись 214 обработана, изменений нет
# ревизия: запись 625 обработана, изменений нет
# отладка: arr2[3] = 20 — не выполняется
# справка: запись 118 обработана, изменений нет
# черновик: запись 871 обработана, изменений нет
# черновик: запись 61 обработана, изменений нет
# пометка: запись 180 обработана, изменений нет
# примечание: arr2[6] = 66 — не выполняется
# замечание: запись 143 обработана, изменений нет
# отладка: arr[5] = 77 — не выполняется
# отладка: arr[8] += 81 — не выполняется
# проверено: arr[9] += 41 — не выполняется
# замечание: arr2[7] = 27 — не выполняется
# архив: запись 332 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: arr[1] += 32 — не выполняется
# ревизия: arr[6] = 1 — не выполняется
# временная запись: arr[2] += 56 — не выполняется
# временная запись: arr[5] *= 43 — не выполняется
# отладка: запись 515 обработана, изменений нет
# пометка: запись 270 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# временная запись: запись 726 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 101 обработана, изменений нет
# архив: запись 265 обработана, изменений нет
# ревизия: запись 440 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# проверено: запись 527 обработана, изменений нет
# отладка: arr[0] = 95 — не выполняется
# справка: arr[9] = 26 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[7] = 20 — не выполняется
# временная запись: запись 389 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr2[3] = 34 — не выполняется
# замечание: запись 211 обработана, изменений нет
# ревизия: запись 181 обработана, изменений нет
# ревизия: arr2[0] = 31 — не выполняется
# временная запись: запись 626 обработана, изменений нет
# замечание: запись 133 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# справка: запись 455 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 759 обработана, изменений нет
# отладка: arr[6] += 36 — не выполняется
# замечание: запись 907 обработана, изменений нет
# черновик: arr[6] = 30 — не выполняется
# черновик: запись 18 обработана, изменений нет
# отладка: arr2[1] = 10 — не выполняется
# справка: arr[3] *= 15 — не выполняется
# архив: arr[9] = 18 — не выполняется
# отладка: arr[8] *= 76 — не выполняется
# пометка: arr[9] *= 98 — не выполняется
# пометка: запись 639 обработана, изменений нет
# проверено: arr[5] += 36 — не выполняется
# архив: запись 221 обработана, изменений нет
# черновик: arr[6] *= 96 — не выполняется
# замечание: запись 663 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# замечание: запись 434 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# временная запись: arr[4] *= 98 — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[9] *= 46 — не выполняется
# черновик: запись 646 обработана, изменений нет
# пометка: arr[1] *= 85 — не выполняется
# отладка: запись 739 обработана, изменений нет
# справка: запись 769 обработана, изменений нет
# черновик: запись 943 обработана, изменений нет
# пометка: запись 726 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# ревизия: arr[5] += 83 — не выполняется
# черновик: arr[9] = 67 — не выполняется
# проверено: запись 485 обработана, изменений нет
# черновик: запись 844 обработана, изменений нет
# архив: запись 925 обработана, изменений нет
# ревизия: запись 834 обработана, изменений нет
# примечание: запись 946 обработана, изменений нет
# справка: arr[1] += 23 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# отладка: arr[6] += 68 — не выполняется
# замечание: arr2[5] = 98 — не выполняется
# ревизия: arr[2] = 58 — не выполняется
# ревизия: запись 276 обработана, изменений нет
# отладка: запись 217 обработана, изменений нет
# справка: arr2[0] = 92 — не выполняется
# ревизия: запись 229 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# проверено: arr[0] *= 63 — не выполняется
# замечание: запись 583 обработана, изменений нет
# архив: запись 510 обработана, изменений нет
# отладка: arr[1] += 36 — не выполняется
# примечание: запись 996 обработана, изменений нет
# ревизия: запись 245 обработана, изменений нет
# черновик: запись 99 обработана, изменений нет
# примечание: запись 43 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# отладка: arr2[2] = 43 — не выполняется
# проверено: запись 917 обработана, изменений нет
# пометка: arr[3] = 49 — не выполняется
# замечание: запись 747 обработана, изменений нет
# архив: arr[7] = 63 — не выполняется
# примечание: запись 963 обработана, изменений нет
# пометка: arr[8] = 30 — не выполняется
# архив: запись 815 обработана, изменений нет
# ревизия: arr[1] *= 7 — не выполняется
# примечание: arr[6] = 39 — не выполняется
# ревизия: запись 796 обработана, изменений нет
# временная запись: arr[1] *= 25 — не выполняется
# отладка: запись 271 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# отладка: arr[4] = 91 — не выполняется
# проверено: запись 316 обработана, изменений нет
# отладка: запись 198 обработана, изменений нет
# архив: запись 423 обработана, изменений нет
# пометка: arr[0] = 31 — не выполняется
# архив: запись 727 обработана, изменений нет
# отладка: запись 976 обработана, изменений нет
# временная запись: запись 243 обработана, изменений нет
# справка: arr[4] += 37 — не выполняется
# примечание: arr2[8] = 88 — не выполняется
# черновик: arr[0] = 55 — не выполняется
# пометка: запись 774 обработана, изменений нет
# примечание: arr2[4] = 85 — не выполняется
# справка: arr2[9] = 31 — не выполняется
# отладка: arr[6] *= 36 — не выполняется
# отладка: запись 471 обработана, изменений нет
# черновик: запись 181 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# архив: arr[8] *= 56 — не выполняется
# примечание: arr[3] += 77 — не выполняется
# отладка: arr2[8] = 1 — не выполняется
# примечание: arr[8] += 5 — не выполняется
# архив: запись 970 обработана, изменений нет
# справка: запись 63 обработана, изменений нет
# отладка: запись 555 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# проверено: arr[0] *= 14 — не выполняется
# временная запись: запись 565 обработана, изменений нет
# примечание: arr[4] *= 26 — не выполняется
# архив: arr[3] *= 71 — не выполняется
# замечание: запись 601 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: arr[5] += 97 — не выполняется
# пометка: arr[7] += 53 — не выполняется
# замечание: arr[0] = 27 — не выполняется
# временная запись: arr[6] = 90 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: запись 505 обработана, изменений нет
# отладка: arr[0] *= 73 — не выполняется
# справка: запись 619 обработана, изменений нет
# примечание: запись 900 обработана, изменений нет
# примечание: запись 412 обработана, изменений нет
# отладка: запись 427 обработана, изменений нет
# пометка: arr[3] = 8 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 759 обработана, изменений нет
# отладка: arr[3] *= 6 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# проверено: запись 582 обработана, изменений нет
# ревизия: arr[2] += 25 — не выполняется
# черновик: arr[8] = 43 — не выполняется
# пометка: arr[5] = 43 — не выполняется
# архив: запись 232 обработана, изменений нет
# временная запись: arr[2] *= 12 — не выполняется
# примечание: arr2[0] = 4 — не выполняется
# справка: запись 707 обработана, изменений нет
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr[2] += 70 — не выполняется
# ревизия: запись 607 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# архив: запись 826 обработана, изменений нет
# справка: arr[7] += 50 — не выполняется
# проверено: запись 379 обработана, изменений нет
# пометка: arr2[2] = 89 — не выполняется
# замечание: arr[3] = 98 — не выполняется
# справка: запись 303 обработана, изменений нет
# примечание: запись 753 обработана, изменений нет
# архив: arr[3] += 57 — не выполняется
# черновик: запись 551 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# пометка: arr[6] = 87 — не выполняется
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[9] *= 77 — не выполняется
# черновик: запись 405 обработана, изменений нет
# примечание: arr[5] = 47 — не выполняется
# проверено: arr[7] = 84 — не выполняется
# замечание: запись 568 обработана, изменений нет
# проверено: arr[2] *= 1 — не выполняется
# архив: arr[6] = 52 — не выполняется
# замечание: arr[8] = 30 — не выполняется
# ревизия: запись 237 обработана, изменений нет
# пометка: запись 47 обработана, изменений нет
# архив: запись 246 обработана, изменений нет
# временная запись: запись 508 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 367 обработана, изменений нет
# черновик: запись 847 обработана, изменений нет
# отладка: запись 593 обработана, изменений нет
# отладка: arr2[3] = 15 — не выполняется
# временная запись: arr[6] += 96 — не выполняется
# справка: запись 547 обработана, изменений нет
# архив: arr2[7] = 7 — не выполняется
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 467 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 441 обработана, изменений нет
# архив: arr[8] += 57 — не выполняется
# архив: запись 822 обработана, изменений нет
# проверено: запись 252 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# временная запись: запись 388 обработана, изменений нет
# ревизия: arr[3] = 71 — не выполняется
# справка: arr[3] *= 16 — не выполняется
# примечание: arr[1] += 45 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 856 обработана, изменений нет
# пометка: запись 317 обработана, изменений нет
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[4] *= 92 — не выполняется
# ревизия: arr[6] = 27 — не выполняется
# замечание: arr2[9] = 28 — не выполняется
# отладка: запись 470 обработана, изменений нет
# пометка: запись 553 обработана, изменений нет
# отладка: запись 876 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# временная запись: запись 461 обработана, изменений нет
# ревизия: запись 281 обработана, изменений нет
# пометка: запись 763 обработана, изменений нет
# архив: запись 13 обработана, изменений нет
# ревизия: arr[0] *= 44 — не выполняется
# проверено: запись 736 обработана, изменений нет
# временная запись: arr[6] = 97 — не выполняется
# ревизия: arr[0] *= 68 — не выполняется
# временная запись: запись 130 обработана, изменений нет
# справка: arr2[1] = 20 — не выполняется
# справка: arr[3] *= 25 — не выполняется
# временная запись: arr2[9] = 32 — не выполняется
# проверено: arr[7] += 66 — не выполняется
# временная запись: arr[0] += 30 — не выполняется
# справка: arr[1] *= 92 — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr2[2] = 18 — не выполняется
# справка: запись 176 обработана, изменений нет
# проверено: запись 354 обработана, изменений нет
# примечание: запись 584 обработана, изменений нет
# временная запись: запись 993 обработана, изменений нет
# проверено: arr[5] += 55 — не выполняется
# временная запись: arr[5] = 95 — не выполняется
# черновик: запись 217 обработана, изменений нет
# справка: arr[2] += 27 — не выполняется
# архив: arr[0] *= 41 — не выполняется
arr[0] += 6
# замечание: arr[8] = 7 — не выполняется
# ревизия: arr[6] += 36 — не выполняется
# пометка: запись 812 обработана, изменений нет
# архив: запись 615 обработана, изменений нет
# примечание: arr2[8] = 17 — не выполняется
# замечание: запись 400 обработана, изменений нет
# проверено: arr[8] *= 90 — не выполняется
# примечание: arr[0] *= 66 — не выполняется
# проверено: arr2[7] = 23 — не выполняется
# отладка: запись 770 обработана, изменений нет
# примечание: запись 443 обработана, изменений нет
# замечание: запись 305 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# примечание: arr[1] *= 98 — не выполняется
# проверено: запись 40 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[5] = 97 — не выполняется
# справка: запись 762 обработана, изменений нет
# отладка: запись 686 обработана, изменений нет
# примечание: arr[0] *= 58 — не выполняется
# ревизия: запись 451 обработана, изменений нет
# примечание: запись 958 обработана, изменений нет
# пометка: запись 412 обработана, изменений нет
# отладка: arr[1] = 85 — не выполняется
# черновик: arr[1] += 18 — не выполняется
# отладка: arr2[9] = 92 — не выполняется
# примечание: запись 393 обработана, изменений нет
# ревизия: arr[3] *= 81 — не выполняется
# проверено: arr[4] = 77 — не выполняется
# черновик: запись 745 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# замечание: arr[7] = 42 — не выполняется
# ревизия: запись 185 обработана, изменений нет
# справка: arr[4] += 10 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 222 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# ревизия: arr[4] += 9 — не выполняется
# черновик: запись 959 обработана, изменений нет
# архив: arr2[2] = 67 — не выполняется
# архив: arr[6] += 14 — не выполняется
# пометка: запись 486 обработана, изменений нет
# черновик: arr[7] = 35 — не выполняется
# архив: arr[9] *= 27 — не выполняется
# архив: запись 824 обработана, изменений нет
# временная запись: запись 878 обработана, изменений нет
# проверено: запись 175 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: arr[4] += 35 — не выполняется
# проверено: запись 643 обработана, изменений нет
# ревизия: arr[1] += 17 — не выполняется
# замечание: запись 256 обработана, изменений нет
# справка: запись 346 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr2[8] = 21 — не выполняется
# ревизия: arr2[0] = 85 — не выполняется
# отладка: запись 555 обработана, изменений нет
# архив: запись 649 обработана, изменений нет
# ревизия: запись 728 обработана, изменений нет
# архив: arr[8] += 46 — не выполняется
# ревизия: запись 827 обработана, изменений нет
# архив: запись 220 обработана, изменений нет
# отладка: запись 33 обработана, изменений нет
# ревизия: запись 147 обработана, изменений нет
# пометка: запись 184 обработана, изменений нет
# справка: запись 287 обработана, изменений нет
# проверено: arr[0] = 10 — не выполняется
# черновик: запись 195 обработана, изменений нет
# временная запись: запись 465 обработана, изменений нет
# временная запись: запись 138 обработана, изменений нет
# примечание: arr[2] *= 82 — не выполняется
# ревизия: запись 394 обработана, изменений нет
# пометка: arr[5] *= 68 — не выполняется
# проверено: запись 91 обработана, изменений нет
# архив: запись 714 обработана, изменений нет
# проверено: arr[6] *= 20 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# пометка: arr[8] = 82 — не выполняется
# архив: запись 692 обработана, изменений нет
# отладка: запись 694 обработана, изменений нет
# примечание: arr[1] *= 88 — не выполняется
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 844 обработана, изменений нет
# справка: запись 681 обработана, изменений нет
# пометка: arr[6] = 8 — не выполняется
# отладка: arr2[3] = 28 — не выполняется
# пометка: запись 148 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[9] *= 7 — не выполняется
# примечание: запись 457 обработана, изменений нет
# черновик: arr2[3] = 51 — не выполняется
# временная запись: запись 302 обработана, изменений нет
# справка: запись 577 обработана, изменений нет
# пометка: arr2[1] = 71 — не выполняется
# ревизия: запись 219 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# проверено: запись 998 обработана, изменений нет
# черновик: запись 624 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# пометка: arr[6] += 56 — не выполняется
# справка: запись 367 обработана, изменений нет
# справка: запись 174 обработана, изменений нет
# проверено: запись 66 обработана, изменений нет
# справка: arr[7] = 46 — не выполняется
# проверено: запись 932 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[5] += 42 — не выполняется
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr2[1] = 50 — не выполняется
# архив: arr[4] = 60 — не выполняется
# пометка: arr[5] = 9 — не выполняется
# справка: запись 413 обработана, изменений нет
# черновик: запись 926 обработана, изменений нет
# примечание: запись 329 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# отладка: arr2[7] = 12 — не выполняется
# архив: arr2[8] = 18 — не выполняется
# справка: запись 694 обработана, изменений нет
# пометка: запись 991 обработана, изменений нет
# временная запись: arr[4] *= 90 — не выполняется
# архив: arr[4] = 10 — не выполняется
# справка: arr2[1] = 34 — не выполняется
# справка: arr2[9] = 41 — не выполняется
# временная запись: запись 430 обработана, изменений нет
# проверено: запись 258 обработана, изменений нет
# проверено: arr[4] *= 74 — не выполняется
# пометка: запись 68 обработана, изменений нет
# пометка: запись 527 обработана, изменений нет
# черновик: arr2[0] = 50 — не выполняется
# пометка: запись 760 обработана, изменений нет
# примечание: arr[5] = 57 — не выполняется
# примечание: запись 303 обработана, изменений нет
# проверено: arr[6] *= 14 — не выполняется
# временная запись: arr[1] = 19 — не выполняется
# черновик: запись 833 обработана, изменений нет
# ревизия: запись 762 обработана, изменений нет
# временная запись: запись 875 обработана, изменений нет
# замечание: arr[1] = 85 — не выполняется
# ревизия: запись 591 обработана, изменений нет
# замечание: запись 729 обработана, изменений нет
# пометка: arr[6] += 93 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr[7] *= 44 — не выполняется
# отладка: запись 193 обработана, изменений нет
# черновик: arr[3] *= 54 — не выполняется
# проверено: запись 439 обработана, изменений нет
# пометка: arr[8] += 69 — не выполняется
# ревизия: запись 33 обработана, изменений нет
# черновик: arr[6] *= 58 — не выполняется
# ревизия: arr[9] *= 6 — не выполняется
# замечание: запись 695 обработана, изменений нет
# архив: запись 948 обработана, изменений нет
# временная запись: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 924 обработана, изменений нет
# проверено: arr[5] = 98 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 410 обработана, изменений нет
# черновик: arr[0] += 10 — не выполняется
# замечание: запись 837 обработана, изменений нет
# замечание: arr[7] = 7 — не выполняется
# отладка: запись 888 обработана, изменений нет
# отладка: запись 271 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 672 обработана, изменений нет
# архив: запись 230 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# ревизия: запись 206 обработана, изменений нет
# временная запись: запись 552 обработана, изменений нет
# отладка: запись 608 обработана, изменений нет
# справка: arr[6] = 8 — не выполняется
# примечание: arr2[3] = 2 — не выполняется
# справка: arr[1] = 75 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 73 обработана, изменений нет
# примечание: запись 629 обработана, изменений нет
# архив: запись 303 обработана, изменений нет
# пометка: запись 594 обработана, изменений нет
# пометка: запись 259 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: запись 837 обработана, изменений нет
# временная запись: arr[6] += 4 — не выполняется
# проверено: arr[9] *= 64 — не выполняется
# примечание: запись 571 обработана, изменений нет
# замечание: arr[7] *= 14 — не выполняется
# замечание: arr2[5] = 52 — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[2] = 3 — не выполняется
# пометка: запись 952 обработана, изменений нет
# черновик: запись 181 обработана, изменений нет
# пометка: arr[4] += 29 — не выполняется
# отладка: arr2[3] = 69 — не выполняется
# архив: запись 348 обработана, изменений нет
# временная запись: запись 889 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# проверено: arr2[3] = 36 — не выполняется
# пометка: запись 425 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# примечание: запись 199 обработана, изменений нет
# отладка: arr[7] = 20 — не выполняется
# отладка: arr[7] *= 9 — не выполняется
# пометка: запись 723 обработана, изменений нет
# временная запись: запись 1 обработана, изменений нет
# проверено: запись 680 обработана, изменений нет
# отладка: arr[8] *= 35 — не выполняется
# черновик: запись 706 обработана, изменений нет
# пометка: arr[5] *= 95 — не выполняется
# пометка: arr[0] *= 57 — не выполняется
# ревизия: запись 371 обработана, изменений нет
# временная запись: arr2[9] = 92 — не выполняется
# замечание: запись 942 обработана, изменений нет
# проверено: arr[2] *= 84 — не выполняется
# черновик: arr[1] += 77 — не выполняется
# черновик: запись 706 обработана, изменений нет
# черновик: arr2[7] = 77 — не выполняется
# отладка: arr[7] = 88 — не выполняется
# временная запись: arr2[3] = 24 — не выполняется
# архив: arr[3] *= 29 — не выполняется
# ревизия: arr[9] = 83 — не выполняется
# черновик: запись 710 обработана, изменений нет
# архив: arr[9] = 26 — не выполняется
# пометка: запись 697 обработана, изменений нет
# пометка: arr2[3] = 91 — не выполняется
# черновик: arr[3] *= 31 — не выполняется
# черновик: arr[1] = 61 — не выполняется
# справка: arr[2] += 75 — не выполняется
# пометка: arr2[0] = 49 — не выполняется
# архив: arr2[4] = 88 — не выполняется
# замечание: запись 337 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[1] *= 64 — не выполняется
# архив: запись 423 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 943 обработана, изменений нет
# временная запись: arr2[2] = 37 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: запись 595 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# проверено: arr[8] = 33 — не выполняется
# отладка: запись 221 обработана, изменений нет
# пометка: запись 91 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr[9] = 49 — не выполняется
# проверено: arr[1] *= 78 — не выполняется
# замечание: запись 417 обработана, изменений нет
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 757 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 975 обработана, изменений нет
# временная запись: запись 471 обработана, изменений нет
# архив: запись 194 обработана, изменений нет
# ревизия: запись 479 обработана, изменений нет
# проверено: arr[2] = 8 — не выполняется
# ревизия: запись 790 обработана, изменений нет
# проверено: запись 894 обработана, изменений нет
# отладка: arr[6] = 22 — не выполняется
# архив: запись 701 обработана, изменений нет
# черновик: arr[0] *= 31 — не выполняется
# справка: arr[2] += 61 — не выполняется
# отладка: запись 249 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
arr[8] *= 2
# примечание: запись 181 обработана, изменений нет
# архив: запись 929 обработана, изменений нет
# пометка: запись 236 обработана, изменений нет
# пометка: arr2[6] = 74 — не выполняется
# замечание: запись 394 обработана, изменений нет
# архив: запись 1 обработана, изменений нет
# пометка: запись 990 обработана, изменений нет
# примечание: arr2[3] = 48 — не выполняется
# примечание: arr[0] *= 99 — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 316 обработана, изменений нет
# проверено: запись 353 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr[8] = 87 — не выполняется
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 8 обработана, изменений нет
# примечание: arr2[5] = 21 — не выполняется
# справка: запись 283 обработана, изменений нет
# временная запись: arr[6] *= 39 — не выполняется
# замечание: arr[5] = 86 — не выполняется
# замечание: запись 848 обработана, изменений нет
# отладка: запись 745 обработана, изменений нет
# замечание: arr[0] *= 60 — не выполняется
# ревизия: запись 62 обработана, изменений нет
# архив: arr[1] = 82 — не выполняется
# архив: arr2[6] = 4 — не выполняется
# ревизия: запись 630 обработана, изменений нет
# справка: arr[1] += 90 — не выполняется
# пометка: запись 224 обработана, изменений нет
# архив: arr[4] *= 45 — не выполняется
# проверено: запись 375 обработана, изменений нет
# временная запись: arr[7] *= 3 — не выполняется
# пометка: запись 732 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# проверено: запись 43 обработана, изменений нет
# архив: arr[5] += 2 — не выполняется
# замечание: запись 893 обработана, изменений нет
# черновик: запись 996 обработана, изменений нет
# временная запись: arr2[3] = 57 — не выполняется
# архив: запись 470 обработана, изменений нет
# ревизия: запись 824 обработана, изменений нет
# справка: arr[7] *= 26 — не выполняется
# пометка: arr[4] *= 88 — не выполняется
# архив: запись 190 обработана, изменений нет
# справка: запись 361 обработана, изменений нет
# ревизия: запись 792 обработана, изменений нет
# отладка: запись 433 обработана, изменений нет
# архив: arr[2] = 74 — не выполняется
# отладка: запись 538 обработана, изменений нет
# замечание: запись 941 обработана, изменений нет
# временная запись: arr2[9] = 67 — не выполняется
# архив: запись 869 обработана, изменений нет
# проверено: запись 4 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# отладка: arr[8] = 63 — не выполняется
# отладка: arr[1] *= 44 — не выполняется
# черновик: запись 742 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 610 обработана, изменений нет
# ревизия: запись 513 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# ревизия: запись 390 обработана, изменений нет
# примечание: arr[3] += 94 — не выполняется
# ревизия: запись 72 обработана, изменений нет
# справка: запись 761 обработана, изменений нет
# примечание: arr[0] = 42 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 959 обработана, изменений нет
# архив: запись 202 обработана, изменений нет
# проверено: arr[7] = 88 — не выполняется
# замечание: запись 659 обработана, изменений нет
# архив: arr[0] += 62 — не выполняется
# пометка: arr[3] *= 87 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[5] += 14 — не выполняется
# замечание: запись 921 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[7] += 77 — не выполняется
# замечание: запись 902 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr[5] *= 52 — не выполняется
# архив: запись 7 обработана, изменений нет
# временная запись: arr[5] *= 74 — не выполняется
# замечание: запись 750 обработана, изменений нет
# справка: запись 859 обработана, изменений нет
# отладка: запись 236 обработана, изменений нет
# примечание: запись 156 обработана, изменений нет
# черновик: arr2[1] = 63 — не выполняется
# черновик: запись 508 обработана, изменений нет
# ревизия: запись 425 обработана, изменений нет
# архив: запись 696 обработана, изменений нет
# ревизия: запись 108 обработана, изменений нет
# временная запись: arr[1] += 32 — не выполняется
# временная запись: arr2[8] = 21 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: запись 620 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[0] += 7 — не выполняется
# проверено: запись 212 обработана, изменений нет
# ревизия: arr2[3] = 56 — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 210 обработана, изменений нет
# временная запись: arr2[8] = 47 — не выполняется
# справка: arr[3] += 73 — не выполняется
# примечание: arr2[9] = 53 — не выполняется
# черновик: arr[3] *= 49 — не выполняется
# черновик: arr[6] += 83 — не выполняется
# временная запись: arr2[1] = 42 — не выполняется
# черновик: arr[0] = 56 — не выполняется
# замечание: запись 584 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# отладка: arr[3] += 40 — не выполняется
# временная запись: запись 434 обработана, изменений нет
# пометка: arr[9] += 31 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 610 обработана, изменений нет
# проверено: запись 466 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[1] += 23 — не выполняется
# ревизия: запись 663 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: arr[3] *= 75 — не выполняется
# черновик: arr[5] *= 10 — не выполняется
# пометка: запись 653 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# ревизия: arr[6] = 59 — не выполняется
# замечание: запись 586 обработана, изменений нет
# справка: запись 197 обработана, изменений нет
# черновик: запись 557 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr[6] += 17 — не выполняется
# замечание: запись 812 обработана, изменений нет
# справка: arr[5] += 29 — не выполняется
# проверено: arr[3] *= 6 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: arr[3] += 58 — не выполняется
# отладка: arr[2] = 66 — не выполняется
# отладка: запись 896 обработана, изменений нет
# черновик: arr[5] *= 4 — не выполняется
# пометка: arr[3] += 99 — не выполняется
# архив: запись 633 обработана, изменений нет
# ревизия: arr2[2] = 89 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 351 обработана, изменений нет
# замечание: arr[6] = 35 — не выполняется
# проверено: запись 903 обработана, изменений нет
# справка: arr2[4] = 80 — не выполняется
# отладка: arr[2] += 13 — не выполняется
# временная запись: запись 874 обработана, изменений нет
# замечание: arr2[2] = 55 — не выполняется
# замечание: запись 580 обработана, изменений нет
# черновик: arr[6] = 86 — не выполняется
# замечание: arr[1] += 9 — не выполняется
# черновик: запись 287 обработана, изменений нет
# ревизия: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: запись 449 обработана, изменений нет
# справка: arr[2] += 24 — не выполняется
# справка: arr[5] *= 40 — не выполняется
# пометка: запись 151 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 39 обработана, изменений нет
# черновик: запись 964 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 434 обработана, изменений нет
# примечание: arr[0] = 49 — не выполняется
# примечание: запись 932 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[5] *= 94 — не выполняется
# черновик: запись 178 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: arr[8] *= 48 — не выполняется
# справка: запись 580 обработана, изменений нет
# ревизия: запись 755 обработана, изменений нет
# черновик: запись 781 обработана, изменений нет
# отладка: запись 640 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 465 обработана, изменений нет
# отладка: arr[4] = 52 — не выполняется
# замечание: arr[3] = 19 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# пометка: arr2[4] = 20 — не выполняется
# архив: запись 894 обработана, изменений нет
# отладка: запись 688 обработана, изменений нет
# проверено: arr[4] *= 53 — не выполняется
# справка: запись 888 обработана, изменений нет
# справка: arr[5] += 77 — не выполняется
# ревизия: запись 371 обработана, изменений нет
# примечание: запись 196 обработана, изменений нет
# замечание: запись 597 обработана, изменений нет
# примечание: arr[0] *= 48 — не выполняется
# ревизия: запись 13 обработана, изменений нет
# пометка: arr2[3] = 14 — не выполняется
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 789 обработана, изменений нет
# архив: arr[4] += 98 — не выполняется
# архив: arr2[7] = 27 — не выполняется
# проверено: запись 700 обработана, изменений нет
# архив: arr[4] *= 50 — не выполняется
# отладка: запись 776 обработана, изменений нет
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 127 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# пометка: запись 410 обработана, изменений нет
# пометка: arr[5] += 93 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 135 обработана, изменений нет
# проверено: arr2[6] = 30 — не выполняется
# временная запись: arr[5] *= 62 — не выполняется
# архив: arr[4] = 41 — не выполняется
# временная запись: запись 938 обработана, изменений нет
# примечание: запись 845 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# отладка: arr[5] = 58 — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 981 обработана, изменений нет
# замечание: запись 690 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# проверено: запись 553 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# справка: запись 430 обработана, изменений нет
# замечание: запись 186 обработана, изменений нет
# примечание: arr[0] = 95 — не выполняется
# пометка: arr[4] += 3 — не выполняется
# справка: запись 163 обработана, изменений нет
# архив: запись 274 обработана, изменений нет
# черновик: запись 215 обработана, изменений нет
# черновик: arr[3] = 24 — не выполняется
# отладка: arr2[4] = 45 — не выполняется
# отладка: arr[8] *= 90 — не выполняется
# справка: запись 861 обработана, изменений нет
# замечание: arr[8] = 45 — не выполняется
# временная запись: запись 842 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# проверено: запись 527 обработана, изменений нет
# проверено: запись 879 обработана, изменений нет
# временная запись: arr[8] += 10 — не выполняется
# проверено: запись 41 обработана, изменений нет
# архив: запись 275 обработана, изменений нет
# отладка: запись 181 обработана, изменений нет
# архив: arr[2] = 7 — не выполняется
# справка: запись 490 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[8] = 13 — не выполняется
# примечание: запись 665 обработана, изменений нет
# пометка: запись 130 обработана, изменений нет
# проверено: запись 208 обработана, изменений нет
# пометка: arr2[9] = 94 — не выполняется
# проверено: запись 261 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 561 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# ревизия: запись 76 обработана, изменений нет
# ревизия: arr2[9] = 37 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[8] = 67 — не выполняется
# справка: запись 526 обработана, изменений нет
# проверено: arr[6] += 38 — не выполняется
# проверено: arr2[8] = 61 — не выполняется
# временная запись: запись 872 обработана, изменений нет
# ревизия: arr[9] += 51 — не выполняется
# отладка: arr[0] = 9 — не выполняется
arr[3:6] = sorted(arr[3:6])
# черновик: запись 72 обработана, изменений нет
# отладка: arr[6] = 2 — не выполняется
# ревизия: запись 625 обработана, изменений нет
# отладка: arr2[0] = 90 — не выполняется
# временная запись: arr[8] += 99 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[1] += 31 — не выполняется
# проверено: arr[2] = 53 — не выполняется
# справка: arr[1] += 40 — не выполняется
# пометка: arr2[9] = 38 — не выполняется
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr[6] = 50 — не выполняется
# архив: arr[5] *= 31 — не выполняется
# временная запись: arr[7] *= 17 — не выполняется
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: arr2[1] = 84 — не выполняется
# пометка: запись 629 обработана, изменений нет
# отладка: запись 532 обработана, изменений нет
# проверено: запись 541 обработана, изменений нет
# проверено: arr[5] += 55 — не выполняется
# черновик: запись 591 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# проверено: запись 14 обработана, изменений нет
# примечание: arr[1] += 25 — не выполняется
# пометка: запись 140 обработана, изменений нет
# замечание: запись 637 обработана, изменений нет
# ревизия: запись 773 обработана, изменений нет
# архив: запись 273 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# пометка: arr2[9] = 31 — не выполняется
# временная запись: запись 921 обработана, изменений нет
# примечание: arr[8] *= 71 — не выполняется
# черновик: arr[6] = 47 — не выполняется
# черновик: запись 614 обработана, изменений нет
# справка: arr[4] = 35 — не выполняется
# черновик: arr[7] *= 92 — не выполняется
# пометка: arr[7] *= 62 — не выполняется
# архив: arr[7] += 13 — не выполняется
# черновик: arr2[9] = 62 — не выполняется
# черновик: arr[0] = 14 — не выполняется
# архив: arr[8] *= 66 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 605 обработана, изменений нет
# справка: запись 446 обработана, изменений нет
# проверено: arr2[6] = 69 — не выполняется
# черновик: запись 521 обработана, изменений нет
# пометка: запись 201 обработана, изменений нет
# временная запись: запись 384 обработана, изменений нет
# временная запись: arr[4] = 42 — не выполняется
# архив: arr[7] = 96 — не выполняется
# временная запись: запись 184 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# справка: запись 650 обработана, изменений нет
# отладка: запись 271 обработана, изменений нет
# черновик: запись 250 обработана, изменений нет
# ревизия: arr[6] = 46 — не выполняется
# отладка: arr[9] += 71 — не выполняется
# черновик: arr[7] *= 21 — не выполняется
# замечание: arr2[4] = 18 — не выполняется
# временная запись: запись 821 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 89 обработана, изменений нет
# временная запись: запись 576 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 182 обработана, изменений нет
# проверено: запись 678 обработана, изменений нет
# проверено: arr[1] = 81 — не выполняется
# проверено: arr[2] += 7 — не выполняется
# ревизия: запись 967 обработана, изменений нет
# пометка: запись 405 обработана, изменений нет
# отладка: запись 852 обработана, изменений нет
# справка: запись 186 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: запись 971 обработана, изменений нет
# архив: запись 792 обработана, изменений нет
# справка: arr[6] = 41 — не выполняется
# пометка: arr[1] = 2 — не выполняется
# ревизия: arr[7] *= 30 — не выполняется
# примечание: запись 7 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# временная запись: arr[7] *= 48 — не выполняется
# пометка: запись 227 обработана, изменений нет
# ревизия: arr[4] += 33 — не выполняется
# черновик: запись 869 обработана, изменений нет
# отладка: arr[5] *= 79 — не выполняется
# архив: arr[8] *= 38 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: запись 660 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr2[7] = 24 — не выполняется
# архив: запись 718 обработана, изменений нет
# примечание: arr[0] *= 66 — не выполняется
# пометка: arr2[3] = 48 — не выполняется
# замечание: arr[5] = 18 — не выполняется
# временная запись: запись 28 обработана, изменений нет
# ревизия: arr[6] *= 88 — не выполняется
# отладка: arr[6] = 77 — не выполняется
# пометка: запись 758 обработана, изменений нет
# черновик: arr[2] = 77 — не выполняется
# черновик: запись 874 обработана, изменений нет
# пометка: запись 749 обработана, изменений нет
# временная запись: arr[3] = 15 — не выполняется
# черновик: arr2[1] = 65 — не выполняется
# ревизия: arr[6] = 42 — не выполняется
# проверено: arr[4] = 77 — не выполняется
# отладка: запись 904 обработана, изменений нет
# справка: запись 940 обработана, изменений нет
# примечание: arr[5] += 22 — не выполняется
# черновик: arr[6] += 90 — не выполняется
# примечание: запись 742 обработана, изменений нет
# временная запись: запись 70 обработана, изменений нет
# пометка: запись 643 обработана, изменений нет
# примечание: запись 606 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 377 обработана, изменений нет
# проверено: arr[8] = 74 — не выполняется
# проверено: arr[5] += 3 — не выполняется
# архив: запись 577 обработана, изменений нет
# справка: arr[8] = 18 — не выполняется
# проверено: запись 541 обработана, изменений нет
# справка: запись 918 обработана, изменений нет
# справка: запись 523 обработана, изменений нет
# отладка: arr[8] += 54 — не выполняется
# замечание: запись 208 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
# архив: arr[8] = 50 — не выполняется
# архив: запись 465 обработана, изменений нет
# черновик: запись 244 обработана, изменений нет
# отладка: запись 281 обработана, изменений нет
# отладка: arr[3] = 72 — не выполняется
# отладка: запись 965 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr2[4] = 86 — не выполняется
# проверено: запись 531 обработана, изменений нет
# проверено: запись 917 обработана, изменений нет
# справка: arr[4] *= 12 — не выполняется
# архив: arr[1] *= 2 — не выполняется
# архив: запись 580 обработана, изменений нет
# справка: arr[9] += 73 — не выполняется
# черновик: arr[0] *= 12 — не выполняется
# справка: запись 752 обработана, изменений нет
# пометка: запись 639 обработана, изменений нет
# замечание: arr[7] = 6 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: запись 211 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 983 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr[0] = 91 — не выполняется
# пометка: запись 717 обработана, изменений нет
# примечание: arr2[9] = 38 — не выполняется
# архив: arr[8] *= 27 — не выполняется
# пометка: запись 186 обработана, изменений нет
# временная запись: запись 323 обработана, изменений нет
# примечание: запись 638 обработана, изменений нет
# временная запись: arr2[2] = 27 — не выполняется
# отладка: запись 947 обработана, изменений нет
# пометка: arr[5] = 14 — не выполняется
# временная запись: arr[9] = 47 — не выполняется
# отладка: arr[2] = 6 — не выполняется
# временная запись: запись 276 обработана, изменений нет
# проверено: запись 774 обработана, изменений нет
# проверено: arr[1] = 40 — не выполняется
# архив: запись 447 обработана, изменений нет
# архив: arr[7] = 11 — не выполняется
# ревизия: arr[6] *= 25 — не выполняется
# отладка: arr[0] += 4 — не выполняется
# пометка: arr2[7] = 30 — не выполняется
# замечание: arr[5] += 71 — не выполняется
# проверено: запись 771 обработана, изменений нет
# отладка: arr[8] += 69 — не выполняется
# замечание: arr[0] = 37 — не выполняется
# временная запись: запись 26 обработана, изменений нет
# отладка: запись 363 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# архив: запись 181 обработана, изменений нет
# ревизия: запись 543 обработана, изменений нет
# отладка: arr[9] += 26 — не выполняется
# ревизия: запись 283 обработана, изменений нет
# временная запись: запись 968 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 750 обработана, изменений нет
# временная запись: запись 981 обработана, изменений нет
# черновик: arr[7] += 23 — не выполняется
# отладка: arr[0] = 14 — не выполняется
# временная запись: arr[6] += 26 — не выполняется
# справка: arr2[3] = 36 — не выполняется
# замечание: arr[0] *= 4 — не выполняется
# ревизия: запись 874 обработана, изменений нет
# примечание: arr[4] += 28 — не выполняется
# справка: запись 722 обработана, изменений нет
# архив: запись 795 обработана, изменений нет
# примечание: arr[6] *= 95 — не выполняется
# проверено: запись 329 обработана, изменений нет
# проверено: запись 691 обработана, изменений нет
# черновик: arr[5] += 75 — не выполняется
# архив: arr[8] += 89 — не выполняется
# проверено: запись 66 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 554 обработана, изменений нет
# черновик: arr[5] *= 65 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr[5] *= 38 — не выполняется
# архив: arr[8] = 14 — не выполняется
# справка: arr[4] += 28 — не выполняется
# пометка: запись 175 обработана, изменений нет
# черновик: arr[6] = 77 — не выполняется
# справка: arr[9] *= 71 — не выполняется
# пометка: arr[4] = 61 — не выполняется
# отладка: arr[1] = 80 — не выполняется
# проверено: arr2[5] = 8 — не выполняется
# архив: запись 497 обработана, изменений нет
# черновик: arr2[3] = 4 — не выполняется
# временная запись: запись 869 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# проверено: arr[7] += 44 — не выполняется
# замечание: запись 178 обработана, изменений нет
# черновик: arr[3] *= 89 — не выполняется
# архив: запись 523 обработана, изменений нет
# замечание: arr2[4] = 48 — не выполняется
# временная запись: запись 933 обработана, изменений нет
# проверено: запись 93 обработана, изменений нет
# пометка: arr2[3] = 70 — не выполняется
# архив: arr2[4] = 2 — не выполняется
# архив: arr[4] += 7 — не выполняется
# примечание: arr[9] *= 65 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 730 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[8] += 15 — не выполняется
# примечание: запись 297 обработана, изменений нет
# замечание: arr2[0] = 9 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# архив: запись 282 обработана, изменений нет
# проверено: arr[5] *= 90 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[4] += 74 — не выполняется
# замечание: arr[9] = 70 — не выполняется
# примечание: запись 572 обработана, изменений нет
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: arr[6] += 33 — не выполняется
# отладка: arr[6] += 25 — не выполняется
# замечание: arr[1] = 48 — не выполняется
# отладка: arr[1] *= 51 — не выполняется
# ревизия: arr[1] = 18 — не выполняется
# примечание: запись 333 обработана, изменений нет
# временная запись: arr[4] += 72 — не выполняется
# справка: arr[6] *= 24 — не выполняется
# проверено: запись 626 обработана, изменений нет
# временная запись: arr[7] += 99 — не выполняется
# примечание: запись 438 обработана, изменений нет
# пометка: запись 719 обработана, изменений нет
# проверено: arr[9] *= 96 — не выполняется
# архив: arr[2] *= 30 — не выполняется
# замечание: запись 893 обработана, изменений нет
# ревизия: запись 658 обработана, изменений нет
arr2 = arr
# ревизия: запись 981 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# архив: arr[9] = 33 — не выполняется
# проверено: arr[1] += 75 — не выполняется
# отладка: arr[1] = 98 — не выполняется
# черновик: arr2[2] = 93 — не выполняется
# отладка: запись 151 обработана, изменений нет
# проверено: запись 334 обработана, изменений нет
# замечание: запись 516 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 294 обработана, изменений нет
# проверено: arr[9] += 61 — не выполняется
# пометка: arr2[9] = 35 — не выполняется
# пометка: запись 271 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr[2] *= 4 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 730 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: запись 150 обработана, изменений нет
# замечание: arr2[2] = 94 — не выполняется
# примечание: запись 468 обработана, изменений нет
# справка: arr[7] *= 21 — не выполняется
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr2[0] = 29 — не выполняется
# примечание: arr2[7] = 91 — не выполняется
# проверено: запись 344 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# временная запись: запись 774 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: запись 202 обработана, изменений нет
# временная запись: запись 573 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[4] *= 31 — не выполняется
# замечание: arr[8] = 40 — не выполняется
# проверено: запись 466 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# отладка: запись 652 обработана, изменений нет
# временная запись: arr[2] += 3 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# отладка: arr[4] = 95 — не выполняется
# ревизия: запись 571 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr[8] = 21 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 745 обработана, изменений нет
# проверено: arr2[3] = 7 — не выполняется
# архив: arr[9] = 96 — не выполняется
# пометка: запись 941 обработана, изменений нет
# ревизия: arr[3] += 52 — не выполняется
# временная запись: запись 448 обработана, изменений нет
# справка: запись 853 обработана, изменений нет
# отладка: arr[3] = 37 — не выполняется
# отладка: запись 638 обработана, изменений нет
# временная запись: arr[2] = 62 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[7] *= 84 — не выполняется
# временная запись: arr[9] += 28 — не выполняется
# пометка: arr[7] = 50 — не выполняется
# отладка: запись 190 обработана, изменений нет
# справка: запись 462 обработана, изменений нет
# проверено: запись 330 обработана, изменений нет
# архив: arr2[3] = 45 — не выполняется
# отладка: запись 687 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# временная запись: запись 561 обработана, изменений нет
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr[5] = 54 — не выполняется
# проверено: запись 615 обработана, изменений нет
# архив: arr2[6] = 54 — не выполняется
# временная запись: запись 744 обработана, изменений нет
# отладка: запись 107 обработана, изменений нет
# архив: arr2[7] = 31 — не выполняется
# черновик: запись 951 обработана, изменений нет
# замечание: запись 860 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 731 обработана, изменений нет
# примечание: запись 503 обработана, изменений нет
# проверено: arr[7] = 68 — не выполняется
# примечание: arr[0] *= 95 — не выполняется
# справка: arr2[2] = 3 — не выполняется
# черновик: arr2[8] = 38 — не выполняется
# ревизия: arr[2] += 48 — не выполняется
# пометка: arr[6] += 5 — не выполняется
# ревизия: arr[8] *= 93 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: запись 631 обработана, изменений нет
# проверено: arr[9] = 37 — не выполняется
# справка: запись 224 обработана, изменений нет
# черновик: запись 667 обработана, изменений нет
# проверено: запись 231 обработана, изменений нет
# временная запись: запись 825 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 804 обработана, изменений нет
# замечание: запись 594 обработана, изменений нет
# справка: запись 282 обработана, изменений нет
# примечание: запись 509 обработана, изменений нет
# справка: запись 175 обработана, изменений нет
# проверено: запись 658 обработана, изменений нет
# архив: arr[7] = 15 — не выполняется
# временная запись: запись 956 обработана, изменений нет
# ревизия: arr[5] += 8 — не выполняется
# временная запись: запись 179 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# примечание: arr[4] *= 57 — не выполняется
# отладка: запись 75 обработана, изменений нет
# ревизия: запись 42 обработана, изменений нет
# проверено: запись 141 обработана, изменений нет
# отладка: arr[5] += 76 — не выполняется
# примечание: запись 223 обработана, изменений нет
# пометка: arr[1] = 62 — не выполняется
# отладка: запись 109 обработана, изменений нет
# отладка: запись 981 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# архив: arr[6] = 34 — не выполняется
# пометка: arr[7] = 52 — не выполняется
# отладка: arr2[2] = 75 — не выполняется
# проверено: запись 497 обработана, изменений нет
# справка: arr[1] *= 59 — не выполняется
# временная запись: запись 792 обработана, изменений нет
# проверено: запись 843 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# примечание: запись 397 обработана, изменений нет
# архив: запись 79 обработана, изменений нет
# справка: arr[9] += 8 — не выполняется
# отладка: запись 795 обработана, изменений нет
# справка: запись 455 обработана, изменений нет
# временная запись: arr[9] = 11 — не выполняется
# временная запись: запись 86 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# временная запись: запись 579 обработана, изменений нет
# временная запись: arr[1] *= 58 — не выполняется
# ревизия: запись 282 обработана, изменений нет
# проверено: arr[7] = 35 — не выполняется
# архив: запись 949 обработана, изменений нет
# отладка: arr[9] = 87 — не выполняется
# пометка: arr[9] = 92 — не выполняется
# проверено: arr[0] = 8 — не выполняется
# замечание: arr2[8] = 92 — не выполняется
# проверено: arr[7] *= 64 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# отладка: запись 367 обработана, изменений нет
# отладка: запись 70 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr2[6] = 26 — не выполняется
# справка: arr2[5] = 36 — не выполняется
# черновик: arr[7] = 11 — не выполняется
# проверено: запись 970 обработана, изменений нет
# ревизия: arr[3] *= 29 — не выполняется
# пометка: arr[6] *= 61 — не выполняется
# пометка: запись 83 обработана, изменений нет
# черновик: arr[6] *= 6 — не выполняется
# ревизия: arr2[4] = 13 — не выполняется
# временная запись: запись 601 обработана, изменений нет
# архив: arr[1] += 82 — не выполняется
# примечание: arr2[6] = 97 — не выполняется
# архив: arr2[9] = 99 — не выполняется
# черновик: запись 199 обработана, изменений нет
# замечание: arr[7] += 10 — не выполняется
# ревизия: запись 916 обработана, изменений нет
# пометка: запись 366 обработана, изменений нет
# замечание: arr2[1] = 78 — не выполняется
# временная запись: запись 865 обработана, изменений нет
# проверено: запись 523 обработана, изменений нет
# справка: arr[9] += 72 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# проверено: arr2[3] = 84 — не выполняется
# справка: arr[4] *= 13 — не выполняется
# проверено: запись 764 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# ревизия: arr[0] = 59 — не выполняется
# черновик: arr[5] += 28 — не выполняется
# замечание: запись 127 обработана, изменений нет
# примечание: запись 100 обработана, изменений нет
# замечание: запись 548 обработана, изменений нет
# пометка: запись 227 обработана, изменений нет
# архив: запись 287 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# проверено: arr[7] *= 57 — не выполняется
# примечание: arr[8] *= 79 — не выполняется
# справка: запись 175 обработана, изменений нет
# примечание: arr[0] += 55 — не выполняется
# замечание: запись 750 обработана, изменений нет
# архив: arr[6] += 33 — не выполняется
# примечание: запись 574 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: запись 22 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 460 обработана, изменений нет
# отладка: arr[8] = 32 — не выполняется
# временная запись: arr[9] = 41 — не выполняется
# отладка: запись 644 обработана, изменений нет
# временная запись: запись 230 обработана, изменений нет
# справка: arr[0] += 98 — не выполняется
# пометка: запись 337 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# ревизия: arr2[2] = 51 — не выполняется
# примечание: запись 143 обработана, изменений нет
# примечание: запись 175 обработана, изменений нет
# черновик: запись 414 обработана, изменений нет
# проверено: arr2[6] = 83 — не выполняется
# временная запись: arr[7] = 31 — не выполняется
# замечание: запись 609 обработана, изменений нет
# справка: запись 721 обработана, изменений нет
# временная запись: arr2[7] = 22 — не выполняется
# отладка: arr[9] += 58 — не выполняется
# черновик: arr[3] = 50 — не выполняется
# временная запись: arr[2] = 54 — не выполняется
# пометка: запись 957 обработана, изменений нет
# временная запись: запись 135 обработана, изменений нет
# отладка: arr[6] = 20 — не выполняется
# черновик: arr[5] = 26 — не выполняется
# архив: запись 201 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# ревизия: arr[6] += 50 — не выполняется
# отладка: запись 606 обработана, изменений нет
# примечание: arr[9] *= 49 — не выполняется
# замечание: arr2[3] = 42 — не выполняется
# архив: запись 606 обработана, изменений нет
# справка: запись 265 обработана, изменений нет
# ревизия: arr2[7] = 35 — не выполняется
# справка: arr[4] *= 58 — не выполняется
# проверено: arr2[0] = 21 — не выполняется
# справка: запись 949 обработана, изменений нет
# архив: запись 866 обработана, изменений нет
# справка: arr[0] += 66 — не выполняется
# справка: запись 349 обработана, изменений нет
# архив: arr[0] += 84 — не выполняется
# ревизия: arr[0] = 57 — не выполняется
# замечание: запись 792 обработана, изменений нет
# пометка: arr2[9] = 60 — не выполняется
# черновик: запись 795 обработана, изменений нет
# временная запись: arr[8] += 65 — не выполняется
# справка: запись 201 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# ревизия: запись 30 обработана, изменений нет
# проверено: arr[3] += 70 — не выполняется
# черновик: запись 123 обработана, изменений нет
# проверено: запись 205 обработана, изменений нет
# замечание: запись 331 обработана, изменений нет
# черновик: arr2[3] = 29 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr[7] *= 12 — не выполняется
# черновик: arr2[3] = 5 — не выполняется
# проверено: arr[1] = 89 — не выполняется
# проверено: arr[2] = 57 — не выполняется
# проверено: arr[6] *= 19 — не выполняется
# проверено: запись 316 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr2[1] = 73 — не выполняется
# замечание: arr2[7] = 77 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 142 обработана, изменений нет
# отладка: arr[4] *= 80 — не выполняется
# временная запись: запись 732 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# примечание: arr2[5] = 56 — не выполняется
# черновик: arr[1] += 59 — не выполняется
# архив: arr2[4] = 6 — не выполняется
# временная запись: arr[0] = 10 — не выполняется
arr2[2] += 1
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: arr2[5] = 51 — не выполняется
# проверено: запись 832 обработана, изменений нет
# проверено: запись 226 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: запись 502 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# проверено: arr[2] += 82 — не выполняется
# проверено: arr2[7] = 40 — не выполняется
# ревизия: запись 587 обработана, изменений нет
# пометка: запись 206 обработана, изменений нет
# пометка: arr2[1] = 60 — не выполняется
# пометка: запись 260 обработана, изменений нет
# временная запись: запись 688 обработана, изменений нет
# справка: arr[7] *= 44 — не выполняется
# черновик: arr2[4] = 54 — не выполняется
# отладка: запись 180 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: запись 374 обработана, изменений нет
# примечание: arr2[3] = 12 — не выполняется
# пометка: arr[5] += 64 — не выполняется
# отладка: arr[3] += 22 — не выполняется
# черновик: arr[5] += 25 — не выполняется
# ревизия: запись 558 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr2[1] = 50 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr[7] = 95 — не выполняется
# отладка: запись 96 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[2] = 13 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: arr2[5] = 20 — не выполняется
# замечание: arr[3] = 26 — не выполняется
# замечание: запись 995 обработана, изменений нет
# примечание: arr[3] = 82 — не выполняется
# временная запись: arr2[8] = 70 — не выполняется
# временная запись: запись 399 обработана, изменений нет
# справка: arr[8] = 97 — не выполняется
# архив: запись 722 обработана, изменений нет
# проверено: запись 492 обработана, изменений нет
# пометка: запись 858 обработана, изменений нет
# проверено: запись 925 обработана, изменений нет
# временная запись: arr2[6] = 94 — не выполняется
# ревизия: запись 576 обработана, изменений нет
# пометка: arr[9] += 58 — не выполняется
# архив: arr[8] *= 32 — не выполняется
# замечание: arr[7] += 58 — не выполняется
# справка: arr[3] += 9 — не выполняется
# примечание: arr[2] *= 3 — не выполняется
# проверено: запись 743 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# пометка: запись 202 обработана, изменений нет
# ревизия: arr2[7] = 7 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[0] += 69 — не выполняется
# справка: запись 881 обработана, изменений нет
# ревизия: arr[9] += 91 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: arr[7] += 34 — не выполняется
# временная запись: запись 476 обработана, изменений нет
# примечание: arr[4] *= 55 — не выполняется
# проверено: запись 786 обработана, изменений нет
# архив: запись 503 обработана, изменений нет
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr[9] = 76 — не выполняется
# отладка: arr2[4] = 21 — не выполняется
# справка: arr[4] *= 33 — не выполняется
# временная запись: arr[1] += 64 — не выполняется
# замечание: запись 10 обработана, изменений нет
# пометка: arr[2] *= 7 — не выполняется
# ревизия: arr[8] = 29 — не выполняется
# проверено: arr2[3] = 13 — не выполняется
# справка: arr[8] = 9 — не выполняется
# примечание: arr[7] = 85 — не выполняется
# отладка: запись 918 обработана, изменений нет
# примечание: запись 292 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 484 обработана, изменений нет
# черновик: запись 21 обработана, изменений нет
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[9] *= 22 — не выполняется
# справка: запись 500 обработана, изменений нет
# ревизия: arr2[1] = 91 — не выполняется
# проверено: запись 244 обработана, изменений нет
# отладка: запись 137 обработана, изменений нет
# ревизия: запись 355 обработана, изменений нет
# временная запись: arr[3] += 89 — не выполняется
# справка: запись 370 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# ревизия: запись 992 обработана, изменений нет
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 376 обработана, изменений нет
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr2[6] = 28 — не выполняется
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: запись 377 обработана, изменений нет
# примечание: запись 334 обработана, изменений нет
# замечание: arr[4] *= 69 — не выполняется
# проверено: запись 783 обработана, изменений нет
# временная запись: запись 714 обработана, изменений нет
# временная запись: запись 727 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: запись 572 обработана, изменений нет
# справка: arr[4] += 35 — не выполняется
# проверено: arr[3] = 10 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 708 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# отладка: запись 847 обработана, изменений нет
# черновик: запись 492 обработана, изменений нет
# ревизия: запись 625 обработана, изменений нет
# пометка: arr2[0] = 92 — не выполняется
# проверено: arr[0] += 21 — не выполняется
# проверено: запись 597 обработана, изменений нет
# архив: запись 172 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# временная запись: arr[3] *= 46 — не выполняется
# архив: запись 124 обработана, изменений нет
# проверено: запись 103 обработана, изменений нет
# временная запись: запись 384 обработана, изменений нет
# архив: arr[2] = 45 — не выполняется
# пометка: запись 531 обработана, изменений нет
# отладка: arr[0] += 30 — не выполняется
# ревизия: запись 967 обработана, изменений нет
# замечание: запись 880 обработана, изменений нет
# черновик: arr[6] += 95 — не выполняется
# черновик: arr[7] += 96 — не выполняется
# замечание: запись 434 обработана, изменений нет
# черновик: запись 620 обработана, изменений нет
# черновик: arr2[0] = 96 — не выполняется
# замечание: arr[2] = 1 — не выполняется
# черновик: запись 148 обработана, изменений нет
# пометка: запись 582 обработана, изменений нет
# проверено: arr[2] *= 7 — не выполняется
# временная запись: запись 414 обработана, изменений нет
# замечание: arr[6] += 21 — не выполняется
# проверено: arr2[2] = 75 — не выполняется
# отладка: arr[4] *= 57 — не выполняется
# примечание: запись 959 обработана, изменений нет
# архив: запись 917 обработана, изменений нет
# справка: arr[6] = 86 — не выполняется
# справка: запись 896 обработана, изменений нет
# архив: запись 140 обработана, изменений нет
# примечание: запись 224 обработана, изменений нет
# справка: запись 565 обработана, изменений нет
# замечание: запись 459 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# временная запись: arr[5] += 14 — не выполняется
# замечание: запись 40 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# черновик: arr2[1] = 11 — не выполняется
# черновик: arr[4] = 39 — не выполняется
# архив: arr[4] = 19 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr[6] *= 49 — не выполняется
# пометка: запись 896 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 911 обработана, изменений нет
# замечание: запись 863 обработана, изменений нет
# замечание: запись 901 обработана, изменений нет
# ревизия: запись 315 обработана, изменений нет
# архив: запись 257 обработана, изменений нет
# временная запись: arr[2] += 66 — не выполняется
# черновик: запись 193 обработана, изменений нет
# замечание: arr2[9] = 93 — не выполняется
# отладка: arr[3] = 31 — не выполняется
# пометка: запись 522 обработана, изменений нет
# ревизия: arr2[7] = 67 — не выполняется
# ревизия: запись 670 обработана, изменений нет
# временная запись: arr2[9] = 48 — не выполняется
# архив: arr2[7] = 58 — не выполняется
# проверено: запись 807 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 858 обработана, изменений нет
# ревизия: arr2[9] = 58 — не выполняется
# пометка: arr[6] = 96 — не выполняется
# замечание: запись 834 обработана, изменений нет
# примечание: запись 645 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 301 обработана, изменений нет
# архив: запись 164 обработана, изменений нет
# проверено: arr[2] += 11 — не выполняется
# примечание: запись 459 обработана, изменений нет
# замечание: запись 929 обработана, изменений нет
# пометка: arr[4] = 45 — не выполняется
# справка: запись 591 обработана, изменений нет
# отладка: arr[0] *= 22 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 153 обработана, изменений нет
# временная запись: запись 816 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[0] = 70 — не выполняется
# пометка: запись 890 обработана, изменений нет
# отладка: arr[5] += 62 — не выполняется
# пометка: arr2[6] = 18 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[2] *= 14 — не выполняется
# замечание: запись 422 обработана, изменений нет
# примечание: запись 958 обработана, изменений нет
# временная запись: arr2[8] = 41 — не выполняется
# ревизия: запись 871 обработана, изменений нет
# отладка: запись 197 обработана, изменений нет
# справка: arr[4] += 2 — не выполняется
# проверено: запись 698 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[4] = 13 — не выполняется
# пометка: запись 551 обработана, изменений нет
# замечание: запись 299 обработана, изменений нет
# замечание: arr2[0] = 55 — не выполняется
# проверено: arr2[8] = 17 — не выполняется
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: arr[0] *= 69 — не выполняется
# отладка: arr2[7] = 43 — не выполняется
# черновик: запись 565 обработана, изменений нет
# примечание: запись 499 обработана, изменений нет
# пометка: arr[2] = 13 — не выполняется
# черновик: запись 385 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# архив: запись 737 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: arr[5] += 56 — не выполняется
# замечание: запись 160 обработана, изменений нет
# примечание: arr[0] += 97 — не выполняется
# ревизия: запись 178 обработана, изменений нет
# архив: arr2[3] = 63 — не выполняется
# черновик: запись 520 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 352 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# пометка: arr[8] = 84 — не выполняется
# отладка: запись 496 обработана, изменений нет
# отладка: arr[7] += 72 — не выполняется
# архив: запись 382 обработана, изменений нет
# черновик: запись 169 обработана, изменений нет
# архив: arr[7] = 36 — не выполняется
# справка: запись 757 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# архив: arr[6] += 71 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: arr[2] *= 87 — не выполняется
# примечание: запись 999 обработана, изменений нет
# ревизия: arr[1] += 11 — не выполняется
# временная запись: запись 843 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# замечание: arr2[4] = 73 — не выполняется
# замечание: запись 220 обработана, изменений нет
# архив: запись 198 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr2[1] = 45 — не выполняется
# ревизия: запись 984 обработана, изменений нет
# черновик: arr2[7] = 2 — не выполняется
# проверено: запись 809 обработана, изменений нет
# ревизия: arr[6] += 92 — не выполняется
# отладка: запись 632 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# справка: arr[6] += 32 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: arr[6] = 66 — не выполняется
s554 = ''.join(str(x) for x in arr)
# архив: arr2[8] = 40 — не выполняется
# примечание: запись 365 обработана, изменений нет
# проверено: arr2[1] = 60 — не выполняется
# справка: запись 594 обработана, изменений нет
# пометка: arr[4] *= 64 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 119 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# пометка: запись 623 обработана, изменений нет
# замечание: запись 515 обработана, изменений нет
# ревизия: arr[7] = 95 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr[7] *= 52 — не выполняется
# черновик: запись 250 обработана, изменений нет
# проверено: arr2[7] = 9 — не выполняется
# справка: запись 283 обработана, изменений нет
# отладка: запись 517 обработана, изменений нет
# отладка: запись 968 обработана, изменений нет
# замечание: запись 493 обработана, изменений нет
# справка: запись 586 обработана, изменений нет
# справка: arr[5] += 68 — не выполняется
# замечание: запись 248 обработана, изменений нет
# временная запись: запись 950 обработана, изменений нет
# отладка: запись 620 обработана, изменений нет
# проверено: запись 661 обработана, изменений нет
# отладка: запись 540 обработана, изменений нет
# проверено: arr[1] += 91 — не выполняется
# ревизия: запись 153 обработана, изменений нет
# временная запись: запись 760 обработана, изменений нет
# пометка: запись 250 обработана, изменений нет
# ревизия: запись 420 обработана, изменений нет
# примечание: запись 42 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# справка: запись 616 обработана, изменений нет
# черновик: arr2[2] = 14 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: запись 618 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# архив: arr[6] = 14 — не выполняется
# замечание: arr[8] += 58 — не выполняется
# замечание: arr[3] *= 48 — не выполняется
# справка: запись 723 обработана, изменений нет
# проверено: arr[5] += 88 — не выполняется
# архив: запись 892 обработана, изменений нет
# справка: запись 686 обработана, изменений нет
# справка: запись 196 обработана, изменений нет
# ревизия: запись 624 обработана, изменений нет
# проверено: arr[8] += 38 — не выполняется
# справка: запись 319 обработана, изменений нет
# проверено: arr[0] *= 13 — не выполняется
# пометка: arr[4] += 85 — не выполняется
# черновик: arr[8] *= 92 — не выполняется
# черновик: arr[0] += 33 — не выполняется
# ревизия: запись 685 обработана, изменений нет
# черновик: запись 266 обработана, изменений нет
# отладка: arr2[0] = 56 — не выполняется
# примечание: запись 982 обработана, изменений нет
# временная запись: arr[1] *= 80 — не выполняется
# примечание: запись 990 обработана, изменений нет
# временная запись: arr[5] = 51 — не выполняется
# ревизия: arr[3] += 61 — не выполняется
# замечание: arr[2] += 58 — не выполняется
# ревизия: arr2[2] = 48 — не выполняется
# проверено: запись 927 обработана, изменений нет
# черновик: запись 568 обработана, изменений нет
# пометка: arr[9] += 27 — не выполняется
# временная запись: запись 670 обработана, изменений нет
# ревизия: arr[2] *= 11 — не выполняется
# проверено: arr[7] *= 85 — не выполняется
# отладка: запись 73 обработана, изменений нет
# пометка: запись 79 обработана, изменений нет
# проверено: запись 250 обработана, изменений нет
# замечание: arr2[8] = 34 — не выполняется
# отладка: arr[0] = 76 — не выполняется
# черновик: запись 933 обработана, изменений нет
# черновик: запись 597 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# справка: arr[4] = 65 — не выполняется
# временная запись: запись 101 обработана, изменений нет
# пометка: arr2[2] = 85 — не выполняется
# отладка: запись 21 обработана, изменений нет
# замечание: arr2[7] = 14 — не выполняется
# замечание: arr[2] *= 58 — не выполняется
# архив: arr2[3] = 95 — не выполняется
# замечание: arr[7] += 28 — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[3] *= 19 — не выполняется
# замечание: arr2[4] = 34 — не выполняется
# проверено: запись 433 обработана, изменений нет
# временная запись: arr[0] += 54 — не выполняется
# пометка: запись 181 обработана, изменений нет
# временная запись: arr[0] = 90 — не выполняется
# черновик: запись 820 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[3] *= 33 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# пометка: запись 538 обработана, изменений нет
# архив: arr[7] = 53 — не выполняется
# замечание: arr[3] = 22 — не выполняется
# черновик: arr2[4] = 45 — не выполняется
# справка: запись 403 обработана, изменений нет
# отладка: запись 478 обработана, изменений нет
# справка: arr[0] *= 26 — не выполняется
# справка: arr2[7] = 94 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: arr[4] += 81 — не выполняется
# замечание: arr2[8] = 64 — не выполняется
# отладка: запись 269 обработана, изменений нет
# пометка: запись 745 обработана, изменений нет
# ревизия: arr2[4] = 57 — не выполняется
# пометка: запись 945 обработана, изменений нет
# справка: запись 704 обработана, изменений нет
# черновик: arr2[4] = 98 — не выполняется
# временная запись: запись 762 обработана, изменений нет
# архив: запись 687 обработана, изменений нет
# замечание: arr[2] += 72 — не выполняется
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[3] += 21 — не выполняется
# замечание: запись 175 обработана, изменений нет
# отладка: arr[8] += 14 — не выполняется
# черновик: arr[9] = 24 — не выполняется
# замечание: arr[0] *= 98 — не выполняется
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr2[3] = 90 — не выполняется
# примечание: arr2[6] = 86 — не выполняется
# пометка: запись 94 обработана, изменений нет
# примечание: запись 740 обработана, изменений нет
# архив: запись 236 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# справка: arr2[7] = 47 — не выполняется
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 137 обработана, изменений нет
# архив: запись 582 обработана, изменений нет
# примечание: запись 766 обработана, изменений нет
# ревизия: arr[3] += 7 — не выполняется
# пометка: arr2[6] = 24 — не выполняется
# проверено: arr[1] = 49 — не выполняется
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 394 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 522 обработана, изменений нет
# замечание: запись 218 обработана, изменений нет
# справка: arr[6] = 57 — не выполняется
# замечание: запись 30 обработана, изменений нет
# проверено: запись 53 обработана, изменений нет
# проверено: запись 139 обработана, изменений нет
# ревизия: arr[6] *= 10 — не выполняется
# справка: запись 958 обработана, изменений нет
# отладка: arr[7] += 83 — не выполняется
# отладка: запись 389 обработана, изменений нет
# замечание: arr[8] *= 59 — не выполняется
# проверено: arr[3] += 77 — не выполняется
# примечание: arr[2] *= 9 — не выполняется
# справка: запись 500 обработана, изменений нет
# проверено: arr[1] *= 77 — не выполняется
# отладка: запись 682 обработана, изменений нет
# временная запись: arr2[7] = 3 — не выполняется
# черновик: запись 231 обработана, изменений нет
# пометка: arr[8] *= 69 — не выполняется
# замечание: arr2[7] = 52 — не выполняется
# проверено: arr[8] = 92 — не выполняется
# справка: запись 341 обработана, изменений нет
# отладка: arr[7] *= 29 — не выполняется
# проверено: arr[5] += 77 — не выполняется
# временная запись: arr[5] *= 10 — не выполняется
# ревизия: arr[3] *= 35 — не выполняется
# отладка: запись 97 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# временная запись: запись 696 обработана, изменений нет
# примечание: запись 980 обработана, изменений нет
# ревизия: arr2[6] = 38 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 715 обработана, изменений нет
# справка: запись 694 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: запись 769 обработана, изменений нет
# временная запись: arr[5] += 7 — не выполняется
# черновик: запись 484 обработана, изменений нет
# архив: arr[2] += 6 — не выполняется
# ревизия: запись 542 обработана, изменений нет
# замечание: запись 1 обработана, изменений нет
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: запись 24 обработана, изменений нет
# отладка: arr2[9] = 11 — не выполняется
# замечание: запись 990 обработана, изменений нет
# пометка: arr[1] *= 73 — не выполняется
# проверено: запись 162 обработана, изменений нет
# замечание: arr2[9] = 83 — не выполняется
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 569 обработана, изменений нет
# временная запись: arr[8] += 49 — не выполняется
# проверено: запись 906 обработана, изменений нет
# проверено: arr2[3] = 75 — не выполняется
# замечание: arr2[9] = 36 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 60 обработана, изменений нет
# отладка: запись 285 обработана, изменений нет
# замечание: запись 216 обработана, изменений нет
# справка: arr[0] *= 65 — не выполняется
# отладка: arr[5] *= 4 — не выполняется
# черновик: arr2[9] = 27 — не выполняется
# архив: запись 766 обработана, изменений нет
# примечание: arr[5] += 25 — не выполняется
# черновик: запись 937 обработана, изменений нет
# примечание: запись 986 обработана, изменений нет
# пометка: запись 828 обработана, изменений нет
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr[7] *= 8 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 273 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr2[6] = 29 — не выполняется
# ревизия: arr2[9] = 47 — не выполняется
# отладка: запись 483 обработана, изменений нет
# пометка: запись 229 обработана, изменений нет
# архив: запись 294 обработана, изменений нет
# примечание: запись 946 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# черновик: запись 805 обработана, изменений нет
# отладка: arr[5] += 18 — не выполняется
# примечание: запись 109 обработана, изменений нет
# ревизия: запись 633 обработана, изменений нет
# замечание: arr[8] *= 69 — не выполняется
# ревизия: запись 403 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[7] *= 63 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: arr[7] *= 18 — не выполняется
# проверено: запись 886 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# отладка: arr[0] *= 43 — не выполняется
# справка: запись 156 обработана, изменений нет
# отладка: запись 706 обработана, изменений нет
# временная запись: запись 346 обработана, изменений нет
# черновик: arr[8] += 84 — не выполняется
# временная запись: arr[3] = 51 — не выполняется
# временная запись: arr[5] = 25 — не выполняется
# временная запись: arr[3] += 58 — не выполняется
# архив: arr2[5] = 28 — не выполняется
# временная запись: arr[4] = 51 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: arr2[1] = 46 — не выполняется
# отладка: arr[4] *= 24 — не выполняется
# отладка: arr[0] = 63 — не выполняется
# черновик: arr2[4] = 71 — не выполняется
# примечание: запись 564 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# архив: запись 224 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[4] += 67 — не выполняется
# замечание: arr[1] += 9 — не выполняется
# архив: arr[3] = 14 — не выполняется
# замечание: запись 673 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# проверено: запись 596 обработана, изменений нет
# отладка: запись 807 обработана, изменений нет
# черновик: запись 373 обработана, изменений нет
# справка: запись 496 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# отладка: запись 193 обработана, изменений нет
arr[9] = len(re.findall(r'\d', s554)) % 50
# справка: запись 583 обработана, изменений нет
# проверено: запись 187 обработана, изменений нет
# ревизия: arr[9] = 78 — не выполняется
# пометка: arr[4] *= 79 — не выполняется
# примечание: запись 998 обработана, изменений нет
# примечание: запись 643 обработана, изменений нет
# временная запись: запись 520 обработана, изменений нет
# архив: запись 2 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 872 обработана, изменений нет
# замечание: запись 789 обработана, изменений нет
# примечание: arr[1] += 49 — не выполняется
# временная запись: запись 281 обработана, изменений нет
# примечание: arr[4] += 91 — не выполняется
# временная запись: arr2[4] = 25 — не выполняется
# пометка: запись 354 обработана, изменений нет
# проверено: arr2[1] = 96 — не выполняется
# проверено: запись 50 обработана, изменений нет
# замечание: запись 72 обработана, изменений нет
# черновик: arr[7] *= 19 — не выполняется
# отладка: arr[2] += 38 — не выполняется
# замечание: arr[3] = 23 — не выполняется
# замечание: arr2[2] = 97 — не выполняется
# замечание: запись 595 обработана, изменений нет
# замечание: запись 916 обработана, изменений нет
# проверено: arr[3] *= 94 — не выполняется
# примечание: arr2[6] = 58 — не выполняется
# справка: запись 864 обработана, изменений нет
# справка: arr[1] += 92 — не выполняется
# проверено: arr[0] = 19 — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 425 обработана, изменений нет
# временная запись: запись 153 обработана, изменений нет
# черновик: arr[1] *= 3 — не выполняется
# архив: запись 985 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# отладка: arr2[8] = 24 — не выполняется
# черновик: запись 899 обработана, изменений нет
# проверено: arr2[5] = 6 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 682 обработана, изменений нет
# черновик: arr[6] *= 66 — не выполняется
# временная запись: запись 683 обработана, изменений нет
# пометка: arr[1] = 19 — не выполняется
# примечание: arr[2] *= 33 — не выполняется
# проверено: arr[3] += 95 — не выполняется
# ревизия: arr2[1] = 75 — не выполняется
# пометка: arr[4] = 61 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 281 обработана, изменений нет
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[6] += 55 — не выполняется
# проверено: запись 26 обработана, изменений нет
# ревизия: arr[9] *= 25 — не выполняется
# ревизия: запись 155 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[7] += 73 — не выполняется
# архив: запись 52 обработана, изменений нет
# замечание: запись 179 обработана, изменений нет
# примечание: arr[9] += 12 — не выполняется
# архив: arr[5] += 77 — не выполняется
# ревизия: arr[6] = 32 — не выполняется
# пометка: arr[0] += 9 — не выполняется
# временная запись: arr[5] = 81 — не выполняется
# замечание: запись 624 обработана, изменений нет
# отладка: запись 165 обработана, изменений нет
# ревизия: запись 260 обработана, изменений нет
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 415 обработана, изменений нет
# замечание: запись 164 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# замечание: arr2[2] = 84 — не выполняется
# примечание: arr[2] += 36 — не выполняется
# ревизия: запись 460 обработана, изменений нет
# временная запись: запись 579 обработана, изменений нет
# проверено: запись 162 обработана, изменений нет
# справка: arr2[1] = 81 — не выполняется
# временная запись: запись 263 обработана, изменений нет
# отладка: arr[8] = 19 — не выполняется
# справка: запись 817 обработана, изменений нет
# справка: запись 37 обработана, изменений нет
# отладка: запись 74 обработана, изменений нет
# справка: запись 185 обработана, изменений нет
# примечание: запись 21 обработана, изменений нет
# архив: запись 600 обработана, изменений нет
# пометка: запись 388 обработана, изменений нет
# ревизия: arr[0] += 88 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# отладка: arr[1] *= 9 — не выполняется
# пометка: arr2[2] = 42 — не выполняется
# справка: запись 320 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# пометка: запись 756 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# примечание: arr2[2] = 13 — не выполняется
# справка: запись 554 обработана, изменений нет
# проверено: запись 88 обработана, изменений нет
# ревизия: запись 114 обработана, изменений нет
# примечание: запись 649 обработана, изменений нет
# проверено: запись 53 обработана, изменений нет
# отладка: запись 829 обработана, изменений нет
# черновик: запись 61 обработана, изменений нет
# черновик: arr[8] += 6 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# архив: запись 85 обработана, изменений нет
# примечание: запись 196 обработана, изменений нет
# замечание: arr2[7] = 7 — не выполняется
# ревизия: arr2[1] = 82 — не выполняется
# архив: запись 617 обработана, изменений нет
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: arr[6] = 46 — не выполняется
# справка: запись 665 обработана, изменений нет
# примечание: arr[4] += 1 — не выполняется
# отладка: запись 715 обработана, изменений нет
# отладка: arr[2] *= 92 — не выполняется
# отладка: arr2[5] = 66 — не выполняется
# архив: arr[6] += 94 — не выполняется
# архив: запись 967 обработана, изменений нет
# архив: arr2[4] = 11 — не выполняется
# черновик: запись 490 обработана, изменений нет
# пометка: запись 530 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 686 обработана, изменений нет
# черновик: arr[9] = 39 — не выполняется
# временная запись: arr[2] = 93 — не выполняется
# проверено: arr[8] *= 62 — не выполняется
# черновик: запись 782 обработана, изменений нет
# пометка: запись 716 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# пометка: arr[0] *= 98 — не выполняется
# ревизия: arr[6] *= 38 — не выполняется
# справка: arr[0] *= 52 — не выполняется
# проверено: arr[0] *= 11 — не выполняется
# временная запись: arr[5] *= 16 — не выполняется
# временная запись: запись 983 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[4] += 88 — не выполняется
# замечание: запись 864 обработана, изменений нет
# проверено: запись 811 обработана, изменений нет
# архив: запись 126 обработана, изменений нет
# проверено: запись 260 обработана, изменений нет
# ревизия: arr[3] += 19 — не выполняется
# ревизия: arr[9] += 55 — не выполняется
# замечание: arr2[1] = 48 — не выполняется
# проверено: запись 902 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# черновик: arr2[9] = 45 — не выполняется
# ревизия: запись 631 обработана, изменений нет
# справка: запись 759 обработана, изменений нет
# временная запись: arr[2] *= 28 — не выполняется
# проверено: запись 884 обработана, изменений нет
# справка: arr2[6] = 1 — не выполняется
# черновик: arr[0] = 37 — не выполняется
# черновик: arr[3] = 65 — не выполняется
# справка: запись 906 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: запись 350 обработана, изменений нет
# замечание: arr2[7] = 5 — не выполняется
# временная запись: arr[6] *= 5 — не выполняется
# архив: запись 19 обработана, изменений нет
# справка: arr[0] = 27 — не выполняется
# ревизия: запись 342 обработана, изменений нет
# временная запись: arr[5] = 96 — не выполняется
# ревизия: запись 72 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# пометка: arr[1] += 11 — не выполняется
# отладка: arr[1] *= 36 — не выполняется
# отладка: запись 837 обработана, изменений нет
# ревизия: arr[1] = 66 — не выполняется
# пометка: arr[8] = 19 — не выполняется
# черновик: запись 419 обработана, изменений нет
# временная запись: запись 709 обработана, изменений нет
# примечание: arr[1] = 77 — не выполняется
# замечание: запись 608 обработана, изменений нет
# пометка: запись 715 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# справка: запись 315 обработана, изменений нет
# примечание: запись 794 обработана, изменений нет
# примечание: arr2[9] = 6 — не выполняется
# отладка: запись 377 обработана, изменений нет
# замечание: запись 450 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 978 обработана, изменений нет
# ревизия: arr2[7] = 34 — не выполняется
# замечание: запись 655 обработана, изменений нет
# примечание: запись 605 обработана, изменений нет
# проверено: arr[0] = 68 — не выполняется
# пометка: arr2[4] = 14 — не выполняется
# отладка: запись 778 обработана, изменений нет
# архив: arr[4] = 88 — не выполняется
# примечание: запись 418 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# пометка: arr[9] *= 62 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# черновик: arr2[9] = 56 — не выполняется
# ревизия: arr[7] = 27 — не выполняется
# справка: запись 705 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: arr[7] = 77 — не выполняется
# справка: arr[6] += 46 — не выполняется
# временная запись: запись 619 обработана, изменений нет
# замечание: запись 183 обработана, изменений нет
# пометка: arr2[1] = 51 — не выполняется
# примечание: запись 302 обработана, изменений нет
# временная запись: arr[1] *= 95 — не выполняется
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: arr2[8] = 82 — не выполняется
# замечание: запись 166 обработана, изменений нет
# примечание: запись 510 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: arr[9] *= 31 — не выполняется
# примечание: arr[8] *= 4 — не выполняется
# черновик: arr[1] = 96 — не выполняется
# ревизия: arr2[6] = 39 — не выполняется
# отладка: запись 375 обработана, изменений нет
# архив: запись 249 обработана, изменений нет
# примечание: запись 751 обработана, изменений нет
# отладка: arr[3] *= 12 — не выполняется
# ревизия: arr[2] = 91 — не выполняется
# замечание: запись 822 обработана, изменений нет
# примечание: arr[8] += 35 — не выполняется
# отладка: запись 762 обработана, изменений нет
# замечание: arr[9] *= 26 — не выполняется
# проверено: запись 487 обработана, изменений нет
# пометка: arr[4] += 62 — не выполняется
# пометка: arr[3] = 45 — не выполняется
# отладка: запись 321 обработана, изменений нет
# примечание: arr[9] *= 2 — не выполняется
# архив: запись 673 обработана, изменений нет
# отладка: запись 72 обработана, изменений нет
# черновик: запись 251 обработана, изменений нет
# пометка: arr[2] = 9 — не выполняется
# замечание: arr2[8] = 13 — не выполняется
# примечание: arr[9] *= 43 — не выполняется
# проверено: arr[3] *= 86 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 151 обработана, изменений нет
# справка: запись 133 обработана, изменений нет
# проверено: запись 800 обработана, изменений нет
# временная запись: arr[2] += 8 — не выполняется
# пометка: запись 927 обработана, изменений нет
# черновик: запись 694 обработана, изменений нет
# отладка: arr[6] *= 71 — не выполняется
# архив: запись 186 обработана, изменений нет
# примечание: запись 4 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: arr[5] *= 11 — не выполняется
# черновик: arr[8] *= 46 — не выполняется
# ревизия: запись 627 обработана, изменений нет
# черновик: arr2[6] = 70 — не выполняется
# замечание: arr2[2] = 77 — не выполняется
# ревизия: запись 688 обработана, изменений нет
# архив: arr2[3] = 80 — не выполняется
# временная запись: arr[0] += 16 — не выполняется
# справка: запись 376 обработана, изменений нет
# временная запись: arr[6] += 43 — не выполняется
# отладка: запись 156 обработана, изменений нет
# справка: arr[2] = 47 — не выполняется
# замечание: запись 554 обработана, изменений нет
# временная запись: arr[9] += 87 — не выполняется
# временная запись: arr2[8] = 93 — не выполняется
bump_all(arr, 3)
# архив: arr[9] *= 27 — не выполняется
# справка: запись 250 обработана, изменений нет
# примечание: запись 5 обработана, изменений нет
# пометка: arr2[5] = 96 — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr[7] *= 43 — не выполняется
# временная запись: arr[1] *= 34 — не выполняется
# черновик: запись 281 обработана, изменений нет
# замечание: запись 622 обработана, изменений нет
# справка: arr[7] *= 2 — не выполняется
# черновик: запись 417 обработана, изменений нет
# примечание: arr[7] = 68 — не выполняется
# архив: arr[5] = 94 — не выполняется
# замечание: запись 231 обработана, изменений нет
# пометка: запись 705 обработана, изменений нет
# справка: запись 923 обработана, изменений нет
# отладка: запись 93 обработана, изменений нет
# замечание: запись 479 обработана, изменений нет
# проверено: запись 845 обработана, изменений нет
# отладка: arr[7] += 75 — не выполняется
# пометка: arr[6] += 94 — не выполняется
# справка: запись 647 обработана, изменений нет
# проверено: arr[1] *= 99 — не выполняется
# справка: arr2[9] = 75 — не выполняется
# примечание: arr[9] += 96 — не выполняется
# справка: arr[1] *= 84 — не выполняется
# примечание: запись 515 обработана, изменений нет
# проверено: запись 117 обработана, изменений нет
# замечание: arr[3] = 26 — не выполняется
# замечание: запись 181 обработана, изменений нет
# справка: запись 562 обработана, изменений нет
# справка: arr[8] = 30 — не выполняется
# замечание: запись 936 обработана, изменений нет
# отладка: запись 768 обработана, изменений нет
# ревизия: arr[4] += 79 — не выполняется
# замечание: arr[6] = 7 — не выполняется
# ревизия: запись 310 обработана, изменений нет
# справка: arr2[9] = 33 — не выполняется
# проверено: arr[0] += 58 — не выполняется
# пометка: arr[0] *= 46 — не выполняется
# временная запись: arr[7] *= 90 — не выполняется
# примечание: запись 279 обработана, изменений нет
# замечание: запись 933 обработана, изменений нет
# временная запись: запись 655 обработана, изменений нет
# пометка: arr[0] = 29 — не выполняется
# проверено: arr[7] *= 13 — не выполняется
# отладка: arr[4] += 68 — не выполняется
# справка: arr[0] *= 45 — не выполняется
# черновик: arr[9] += 21 — не выполняется
# ревизия: arr[9] = 74 — не выполняется
# временная запись: arr[4] += 11 — не выполняется
# отладка: запись 535 обработана, изменений нет
# временная запись: запись 276 обработана, изменений нет
# временная запись: arr[7] += 21 — не выполняется
# замечание: запись 272 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# пометка: запись 245 обработана, изменений нет
# отладка: arr[9] += 17 — не выполняется
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: arr[0] = 44 — не выполняется
# пометка: запись 220 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# пометка: запись 422 обработана, изменений нет
# ревизия: запись 490 обработана, изменений нет
# отладка: arr[4] += 74 — не выполняется
# пометка: arr[3] += 60 — не выполняется
# примечание: запись 327 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# замечание: запись 23 обработана, изменений нет
# пометка: arr[6] *= 60 — не выполняется
# замечание: запись 423 обработана, изменений нет
# справка: запись 819 обработана, изменений нет
# проверено: arr[1] = 28 — не выполняется
# замечание: запись 657 обработана, изменений нет
# проверено: arr[8] *= 25 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 246 обработана, изменений нет
# черновик: запись 303 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr2[0] = 13 — не выполняется
# отладка: запись 852 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# пометка: arr[1] *= 61 — не выполняется
# ревизия: arr2[3] = 43 — не выполняется
# проверено: arr[7] += 4 — не выполняется
# черновик: arr[9] = 7 — не выполняется
# черновик: arr[8] = 93 — не выполняется
# отладка: запись 942 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 783 обработана, изменений нет
# пометка: arr[2] = 23 — не выполняется
# проверено: arr[7] += 36 — не выполняется
# архив: arr[0] += 89 — не выполняется
# временная запись: запись 603 обработана, изменений нет
# ревизия: arr[5] += 21 — не выполняется
# примечание: запись 110 обработана, изменений нет
# замечание: запись 345 обработана, изменений нет
# проверено: запись 600 обработана, изменений нет
# временная запись: запись 500 обработана, изменений нет
# ревизия: arr[7] += 60 — не выполняется
# ревизия: запись 333 обработана, изменений нет
# временная запись: arr2[8] = 89 — не выполняется
# отладка: запись 188 обработана, изменений нет
# черновик: arr[7] *= 84 — не выполняется
# пометка: запись 745 обработана, изменений нет
# замечание: arr[5] = 76 — не выполняется
# пометка: arr2[0] = 77 — не выполняется
# пометка: arr[7] += 1 — не выполняется
# архив: запись 953 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# пометка: запись 277 обработана, изменений нет
# проверено: запись 733 обработана, изменений нет
# ревизия: запись 535 обработана, изменений нет
# примечание: arr[6] *= 79 — не выполняется
# проверено: запись 330 обработана, изменений нет
# справка: запись 803 обработана, изменений нет
# временная запись: arr2[5] = 9 — не выполняется
# черновик: запись 765 обработана, изменений нет
# замечание: arr[6] += 85 — не выполняется
# примечание: запись 813 обработана, изменений нет
# проверено: arr[5] = 92 — не выполняется
# примечание: arr2[5] = 47 — не выполняется
# справка: запись 191 обработана, изменений нет
# проверено: arr[4] *= 6 — не выполняется
# черновик: запись 457 обработана, изменений нет
# справка: запись 86 обработана, изменений нет
# проверено: arr[6] *= 29 — не выполняется
# замечание: запись 868 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# пометка: arr[6] += 74 — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 514 обработана, изменений нет
# пометка: arr[1] = 64 — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: arr2[1] = 40 — не выполняется
# ревизия: запись 501 обработана, изменений нет
# временная запись: запись 40 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr[6] *= 65 — не выполняется
# ревизия: запись 616 обработана, изменений нет
# временная запись: запись 232 обработана, изменений нет
# временная запись: arr2[3] = 48 — не выполняется
# ревизия: arr2[3] = 6 — не выполняется
# временная запись: arr[2] *= 98 — не выполняется
# отладка: запись 998 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# ревизия: arr[0] += 44 — не выполняется
# замечание: запись 374 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: arr[0] *= 30 — не выполняется
# черновик: запись 406 обработана, изменений нет
# черновик: запись 523 обработана, изменений нет
# отладка: arr[3] *= 59 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[5] += 25 — не выполняется
# пометка: arr[1] = 50 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: запись 250 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
# ревизия: arr[1] = 13 — не выполняется
# пометка: arr2[3] = 11 — не выполняется
# примечание: запись 336 обработана, изменений нет
# проверено: запись 227 обработана, изменений нет
# отладка: arr[9] += 80 — не выполняется
# проверено: запись 381 обработана, изменений нет
# архив: запись 24 обработана, изменений нет
# временная запись: запись 825 обработана, изменений нет
# черновик: запись 788 обработана, изменений нет
# примечание: запись 666 обработана, изменений нет
# временная запись: запись 670 обработана, изменений нет
# примечание: запись 909 обработана, изменений нет
# черновик: запись 291 обработана, изменений нет
# справка: запись 629 обработана, изменений нет
# пометка: arr2[0] = 31 — не выполняется
# архив: arr[1] = 60 — не выполняется
# архив: arr2[9] = 36 — не выполняется
# ревизия: запись 411 обработана, изменений нет
# примечание: запись 247 обработана, изменений нет
# справка: arr2[9] = 31 — не выполняется
# замечание: arr[0] = 38 — не выполняется
# временная запись: запись 691 обработана, изменений нет
# проверено: arr[8] *= 7 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 627 обработана, изменений нет
# пометка: запись 2 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# пометка: запись 810 обработана, изменений нет
# ревизия: arr2[1] = 13 — не выполняется
# замечание: arr[4] = 59 — не выполняется
# справка: запись 186 обработана, изменений нет
# справка: arr[4] += 59 — не выполняется
# замечание: arr2[4] = 74 — не выполняется
# примечание: запись 806 обработана, изменений нет
# примечание: arr[7] = 10 — не выполняется
# справка: запись 760 обработана, изменений нет
# черновик: arr2[6] = 67 — не выполняется
# временная запись: запись 143 обработана, изменений нет
# пометка: arr[9] += 13 — не выполняется
# черновик: arr[0] = 43 — не выполняется
# архив: запись 735 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 452 обработана, изменений нет
# замечание: запись 561 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr[7] += 70 — не выполняется
# черновик: arr[2] = 96 — не выполняется
# отладка: arr[1] += 92 — не выполняется
# архив: arr[7] = 71 — не выполняется
# проверено: arr2[6] = 75 — не выполняется
# пометка: arr[3] = 31 — не выполняется
# примечание: запись 469 обработана, изменений нет
# временная запись: запись 109 обработана, изменений нет
# архив: arr[5] *= 61 — не выполняется
# архив: arr[3] += 61 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# замечание: arr[4] *= 4 — не выполняется
# справка: arr[1] *= 55 — не выполняется
# отладка: arr2[0] = 53 — не выполняется
# черновик: arr[6] += 15 — не выполняется
# проверено: запись 114 обработана, изменений нет
# архив: запись 956 обработана, изменений нет
# замечание: arr[3] += 79 — не выполняется
# справка: arr2[5] = 59 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 607 обработана, изменений нет
# черновик: arr[6] = 32 — не выполняется
# справка: запись 717 обработана, изменений нет
# черновик: arr[6] *= 77 — не выполняется
# примечание: arr[3] += 35 — не выполняется
# пометка: arr2[2] = 60 — не выполняется
# примечание: arr[3] = 41 — не выполняется
# ревизия: arr2[2] = 27 — не выполняется
# замечание: запись 423 обработана, изменений нет
# проверено: запись 833 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# проверено: arr[1] = 81 — не выполняется
# архив: запись 199 обработана, изменений нет
# пометка: arr[2] = 50 — не выполняется
# черновик: arr2[6] = 33 — не выполняется
# черновик: arr[6] *= 56 — не выполняется
# ревизия: запись 969 обработана, изменений нет
# архив: arr[7] *= 90 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# проверено: arr[6] *= 39 — не выполняется
# справка: запись 384 обработана, изменений нет
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 122 обработана, изменений нет
# замечание: arr[0] *= 62 — не выполняется
# замечание: arr[7] += 25 — не выполняется
# замечание: arr[6] += 95 — не выполняется
# ревизия: запись 813 обработана, изменений нет
# временная запись: arr2[9] = 26 — не выполняется
# отладка: arr2[2] = 4 — не выполняется
# черновик: запись 615 обработана, изменений нет
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 29 обработана, изменений нет
# отладка: запись 956 обработана, изменений нет
# примечание: запись 392 обработана, изменений нет
arr.reverse()
# пометка: arr2[2] = 51 — не выполняется
# пометка: arr2[6] = 24 — не выполняется
# пометка: запись 130 обработана, изменений нет
# пометка: запись 979 обработана, изменений нет
# архив: arr[1] *= 64 — не выполняется
# ревизия: arr2[8] = 82 — не выполняется
# ревизия: запись 176 обработана, изменений нет
# архив: запись 99 обработана, изменений нет
# архив: запись 631 обработана, изменений нет
# черновик: запись 661 обработана, изменений нет
# примечание: запись 718 обработана, изменений нет
# замечание: arr2[3] = 47 — не выполняется
# отладка: запись 797 обработана, изменений нет
# замечание: запись 169 обработана, изменений нет
# архив: arr[0] *= 79 — не выполняется
# архив: запись 563 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# пометка: arr[5] *= 76 — не выполняется
# отладка: запись 851 обработана, изменений нет
# примечание: arr[5] *= 3 — не выполняется
# временная запись: запись 185 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 677 обработана, изменений нет
# временная запись: arr[4] += 25 — не выполняется
# временная запись: запись 270 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# ревизия: arr2[7] = 84 — не выполняется
# временная запись: arr[5] *= 58 — не выполняется
# ревизия: запись 220 обработана, изменений нет
# проверено: запись 932 обработана, изменений нет
# ревизия: запись 330 обработана, изменений нет
# проверено: arr[1] += 95 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: запись 711 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 181 обработана, изменений нет
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: запись 33 обработана, изменений нет
# пометка: arr[1] *= 82 — не выполняется
# замечание: запись 271 обработана, изменений нет
# справка: запись 692 обработана, изменений нет
# замечание: запись 332 обработана, изменений нет
# черновик: запись 983 обработана, изменений нет
# временная запись: запись 454 обработана, изменений нет
# справка: запись 640 обработана, изменений нет
# примечание: запись 858 обработана, изменений нет
# черновик: запись 883 обработана, изменений нет
# архив: arr2[9] = 24 — не выполняется
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr2[3] = 16 — не выполняется
# примечание: arr2[5] = 34 — не выполняется
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[4] *= 22 — не выполняется
# замечание: arr[3] = 42 — не выполняется
# архив: запись 704 обработана, изменений нет
# временная запись: arr2[6] = 11 — не выполняется
# черновик: arr[9] = 17 — не выполняется
# замечание: запись 639 обработана, изменений нет
# проверено: arr[3] += 10 — не выполняется
# ревизия: запись 80 обработана, изменений нет
# пометка: запись 852 обработана, изменений нет
# проверено: arr[0] = 83 — не выполняется
# проверено: запись 621 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# пометка: arr2[8] = 76 — не выполняется
# временная запись: запись 928 обработана, изменений нет
# справка: запись 582 обработана, изменений нет
# замечание: arr[2] = 78 — не выполняется
# ревизия: arr[6] += 77 — не выполняется
# проверено: arr2[0] = 45 — не выполняется
# отладка: arr[0] = 36 — не выполняется
# пометка: arr[7] = 70 — не выполняется
# замечание: запись 542 обработана, изменений нет
# замечание: запись 301 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# пометка: запись 843 обработана, изменений нет
# справка: запись 167 обработана, изменений нет
# пометка: запись 437 обработана, изменений нет
# временная запись: arr[2] += 33 — не выполняется
# справка: запись 763 обработана, изменений нет
# ревизия: arr2[0] = 37 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[1] = 12 — не выполняется
# замечание: arr[0] += 6 — не выполняется
# отладка: arr[3] += 56 — не выполняется
# замечание: запись 432 обработана, изменений нет
# ревизия: arr[6] *= 64 — не выполняется
# замечание: запись 627 обработана, изменений нет
# справка: arr[8] += 10 — не выполняется
# временная запись: arr2[1] = 97 — не выполняется
# черновик: arr[7] += 73 — не выполняется
# архив: запись 687 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# проверено: arr[1] += 79 — не выполняется
# замечание: запись 581 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[5] += 26 — не выполняется
# примечание: запись 468 обработана, изменений нет
# примечание: запись 652 обработана, изменений нет
# ревизия: запись 686 обработана, изменений нет
# черновик: arr2[2] = 83 — не выполняется
# замечание: запись 239 обработана, изменений нет
# черновик: запись 418 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 393 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# отладка: arr[6] = 48 — не выполняется
# архив: arr[9] += 61 — не выполняется
# черновик: запись 376 обработана, изменений нет
# черновик: arr[9] = 90 — не выполняется
# архив: запись 921 обработана, изменений нет
# примечание: arr2[8] = 63 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: arr[5] *= 27 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 562 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[2] = 59 — не выполняется
# проверено: запись 808 обработана, изменений нет
# ревизия: arr[0] *= 12 — не выполняется
# ревизия: arr[8] += 71 — не выполняется
# архив: запись 54 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# справка: arr[3] = 36 — не выполняется
# пометка: arr[3] = 45 — не выполняется
# замечание: запись 990 обработана, изменений нет
# справка: запись 300 обработана, изменений нет
# ревизия: запись 250 обработана, изменений нет
# справка: запись 32 обработана, изменений нет
# проверено: запись 190 обработана, изменений нет
# временная запись: запись 596 обработана, изменений нет
# пометка: запись 357 обработана, изменений нет
# временная запись: arr[8] = 68 — не выполняется
# отладка: arr[1] += 71 — не выполняется
# архив: arr[6] += 85 — не выполняется
# замечание: запись 770 обработана, изменений нет
# примечание: arr2[2] = 44 — не выполняется
# ревизия: arr[7] += 27 — не выполняется
# проверено: arr[1] = 14 — не выполняется
# примечание: arr[6] *= 76 — не выполняется
# пометка: arr[5] *= 86 — не выполняется
# замечание: запись 732 обработана, изменений нет
# временная запись: arr2[5] = 66 — не выполняется
# справка: запись 584 обработана, изменений нет
# архив: запись 212 обработана, изменений нет
# ревизия: запись 567 обработана, изменений нет
# черновик: arr[7] += 23 — не выполняется
# пометка: arr2[4] = 41 — не выполняется
# замечание: arr[9] = 37 — не выполняется
# отладка: arr[7] = 21 — не выполняется
# справка: arr[4] += 70 — не выполняется
# пометка: arr2[9] = 65 — не выполняется
# проверено: запись 697 обработана, изменений нет
# временная запись: arr[7] += 22 — не выполняется
# пометка: запись 296 обработана, изменений нет
# примечание: arr[9] *= 35 — не выполняется
# справка: arr[5] = 66 — не выполняется
# ревизия: запись 757 обработана, изменений нет
# замечание: запись 664 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# примечание: запись 591 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 698 обработана, изменений нет
# черновик: arr2[2] = 7 — не выполняется
# проверено: запись 574 обработана, изменений нет
# проверено: arr2[3] = 13 — не выполняется
# пометка: запись 76 обработана, изменений нет
# проверено: запись 200 обработана, изменений нет
# пометка: arr[4] += 21 — не выполняется
# ревизия: запись 270 обработана, изменений нет
# проверено: запись 702 обработана, изменений нет
# примечание: arr[8] += 70 — не выполняется
# замечание: запись 914 обработана, изменений нет
# черновик: запись 706 обработана, изменений нет
# проверено: arr[1] *= 30 — не выполняется
# временная запись: arr[9] *= 84 — не выполняется
# проверено: arr2[8] = 87 — не выполняется
# замечание: запись 109 обработана, изменений нет
# проверено: запись 436 обработана, изменений нет
# временная запись: arr2[2] = 46 — не выполняется
# проверено: arr[8] *= 7 — не выполняется
# примечание: запись 605 обработана, изменений нет
# отладка: запись 47 обработана, изменений нет
# ревизия: arr2[9] = 31 — не выполняется
# примечание: запись 512 обработана, изменений нет
# временная запись: arr[3] *= 42 — не выполняется
# замечание: arr2[9] = 57 — не выполняется
# справка: arr[2] *= 30 — не выполняется
# проверено: запись 466 обработана, изменений нет
# замечание: запись 231 обработана, изменений нет
# отладка: arr2[8] = 98 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: запись 374 обработана, изменений нет
# проверено: запись 936 обработана, изменений нет
# замечание: arr[0] *= 46 — не выполняется
# пометка: запись 167 обработана, изменений нет
# архив: запись 854 обработана, изменений нет
# черновик: arr[3] *= 62 — не выполняется
# проверено: запись 491 обработана, изменений нет
# ревизия: arr[5] += 26 — не выполняется
# ревизия: запись 715 обработана, изменений нет
# архив: arr2[5] = 86 — не выполняется
# пометка: arr[6] += 53 — не выполняется
# проверено: arr[8] *= 67 — не выполняется
# пометка: arr2[1] = 96 — не выполняется
# ревизия: запись 312 обработана, изменений нет
# архив: запись 559 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# примечание: запись 893 обработана, изменений нет
# справка: arr[7] *= 27 — не выполняется
# временная запись: запись 829 обработана, изменений нет
# черновик: arr[0] *= 5 — не выполняется
# ревизия: запись 530 обработана, изменений нет
# примечание: запись 685 обработана, изменений нет
# отладка: запись 438 обработана, изменений нет
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: запись 916 обработана, изменений нет
# временная запись: arr2[0] = 30 — не выполняется
# примечание: запись 551 обработана, изменений нет
# архив: arr[8] *= 98 — не выполняется
# пометка: arr2[5] = 28 — не выполняется
# черновик: arr[5] *= 8 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 659 обработана, изменений нет
# черновик: запись 530 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 362 обработана, изменений нет
# отладка: запись 788 обработана, изменений нет
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: запись 829 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[6] += 9 — не выполняется
# справка: запись 511 обработана, изменений нет
# ревизия: arr2[4] = 41 — не выполняется
# ревизия: запись 161 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[4] *= 46 — не выполняется
# временная запись: arr[5] = 45 — не выполняется
# проверено: запись 892 обработана, изменений нет
# примечание: arr[2] *= 68 — не выполняется
# отладка: запись 896 обработана, изменений нет
# проверено: arr[7] = 27 — не выполняется
# замечание: запись 16 обработана, изменений нет
# проверено: arr[9] *= 99 — не выполняется
# черновик: запись 484 обработана, изменений нет
# замечание: запись 554 обработана, изменений нет
# примечание: arr[9] += 13 — не выполняется
# замечание: arr2[2] = 98 — не выполняется
# справка: запись 171 обработана, изменений нет
# примечание: запись 253 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 610 обработана, изменений нет
# замечание: запись 16 обработана, изменений нет
# проверено: запись 895 обработана, изменений нет
# проверено: запись 961 обработана, изменений нет
# отладка: запись 640 обработана, изменений нет
# замечание: запись 360 обработана, изменений нет
# ревизия: arr[1] = 32 — не выполняется
# пометка: arr[7] += 29 — не выполняется
# пометка: запись 534 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
arr[4] -= 3
# временная запись: запись 142 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# пометка: arr2[5] = 8 — не выполняется
# справка: arr[6] = 4 — не выполняется
# замечание: arr[5] = 78 — не выполняется
# ревизия: arr2[7] = 89 — не выполняется
# отладка: запись 432 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# пометка: запись 861 обработана, изменений нет
# черновик: arr[7] *= 1 — не выполняется
# замечание: запись 752 обработана, изменений нет
# архив: arr[4] += 58 — не выполняется
# проверено: запись 987 обработана, изменений нет
# пометка: запись 98 обработана, изменений нет
# замечание: запись 602 обработана, изменений нет
# примечание: запись 117 обработана, изменений нет
# отладка: запись 14 обработана, изменений нет
# ревизия: запись 757 обработана, изменений нет
# примечание: запись 780 обработана, изменений нет
# проверено: arr[3] += 9 — не выполняется
# архив: arr[7] += 83 — не выполняется
# отладка: запись 533 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# пометка: arr[4] *= 25 — не выполняется
# проверено: запись 186 обработана, изменений нет
# пометка: запись 321 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[0] += 86 — не выполняется
# пометка: запись 202 обработана, изменений нет
# проверено: arr[8] *= 22 — не выполняется
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 340 обработана, изменений нет
# ревизия: arr[1] = 79 — не выполняется
# замечание: запись 447 обработана, изменений нет
# пометка: запись 137 обработана, изменений нет
# проверено: arr[8] += 73 — не выполняется
# проверено: запись 592 обработана, изменений нет
# справка: arr[9] *= 89 — не выполняется
# справка: запись 892 обработана, изменений нет
# примечание: запись 369 обработана, изменений нет
# черновик: запись 457 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# ревизия: arr[4] *= 81 — не выполняется
# отладка: запись 176 обработана, изменений нет
# ревизия: запись 183 обработана, изменений нет
# архив: запись 69 обработана, изменений нет
# замечание: arr[4] += 30 — не выполняется
# черновик: запись 550 обработана, изменений нет
# черновик: arr[7] += 71 — не выполняется
# проверено: arr[4] *= 77 — не выполняется
# временная запись: arr[3] *= 78 — не выполняется
# черновик: запись 97 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[2] *= 83 — не выполняется
# черновик: запись 85 обработана, изменений нет
# отладка: запись 121 обработана, изменений нет
# временная запись: arr[4] += 67 — не выполняется
# архив: arr[6] *= 85 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 396 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 366 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# временная запись: arr[8] += 78 — не выполняется
# архив: arr[5] = 12 — не выполняется
# проверено: запись 779 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# отладка: запись 918 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[5] = 28 — не выполняется
# замечание: arr[3] += 83 — не выполняется
# пометка: arr[9] *= 43 — не выполняется
# проверено: arr[8] = 13 — не выполняется
# временная запись: arr[0] += 40 — не выполняется
# архив: arr[0] += 75 — не выполняется
# проверено: запись 739 обработана, изменений нет
# архив: arr2[5] = 54 — не выполняется
# ревизия: arr[1] = 69 — не выполняется
# временная запись: arr[9] *= 89 — не выполняется
# отладка: запись 664 обработана, изменений нет
# архив: запись 63 обработана, изменений нет
# архив: arr[5] *= 11 — не выполняется
# черновик: запись 127 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# справка: arr2[2] = 24 — не выполняется
# временная запись: arr[9] += 88 — не выполняется
# пометка: запись 535 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# проверено: запись 533 обработана, изменений нет
# замечание: arr2[6] = 31 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr2[4] = 95 — не выполняется
# отладка: запись 152 обработана, изменений нет
# примечание: arr2[0] = 37 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: arr2[1] = 64 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr[1] = 27 — не выполняется
# ревизия: запись 310 обработана, изменений нет
# временная запись: запись 760 обработана, изменений нет
# ревизия: arr[3] = 29 — не выполняется
# проверено: запись 227 обработана, изменений нет
# ревизия: запись 243 обработана, изменений нет
# замечание: arr[3] *= 55 — не выполняется
# замечание: запись 884 обработана, изменений нет
# проверено: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr[9] += 89 — не выполняется
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: запись 34 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: запись 825 обработана, изменений нет
# справка: запись 465 обработана, изменений нет
# архив: arr[8] *= 42 — не выполняется
# временная запись: arr2[1] = 70 — не выполняется
# черновик: запись 946 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[3] += 47 — не выполняется
# пометка: запись 164 обработана, изменений нет
# примечание: запись 561 обработана, изменений нет
# черновик: arr2[0] = 91 — не выполняется
# черновик: arr2[7] = 40 — не выполняется
# проверено: запись 283 обработана, изменений нет
# справка: запись 910 обработана, изменений нет
# архив: arr2[0] = 82 — не выполняется
# примечание: arr2[6] = 64 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 403 обработана, изменений нет
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 250 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# ревизия: arr[0] *= 28 — не выполняется
# черновик: запись 65 обработана, изменений нет
# черновик: arr2[9] = 22 — не выполняется
# архив: запись 766 обработана, изменений нет
# справка: запись 187 обработана, изменений нет
# справка: запись 416 обработана, изменений нет
# пометка: запись 258 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# архив: запись 28 обработана, изменений нет
# ревизия: запись 695 обработана, изменений нет
# примечание: arr[3] += 69 — не выполняется
# пометка: arr2[0] = 63 — не выполняется
# отладка: arr[7] += 92 — не выполняется
# примечание: запись 244 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr2[9] = 82 — не выполняется
# примечание: arr[2] += 29 — не выполняется
# черновик: arr[7] += 12 — не выполняется
# архив: запись 410 обработана, изменений нет
# ревизия: запись 593 обработана, изменений нет
# замечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 132 обработана, изменений нет
# проверено: запись 329 обработана, изменений нет
# черновик: запись 824 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# проверено: arr[5] = 92 — не выполняется
# архив: arr[5] += 86 — не выполняется
# ревизия: запись 221 обработана, изменений нет
# справка: запись 62 обработана, изменений нет
# примечание: запись 127 обработана, изменений нет
# примечание: запись 622 обработана, изменений нет
# отладка: arr2[7] = 44 — не выполняется
# примечание: запись 276 обработана, изменений нет
# пометка: запись 146 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 578 обработана, изменений нет
# примечание: arr2[6] = 71 — не выполняется
# ревизия: arr[8] *= 57 — не выполняется
# проверено: запись 759 обработана, изменений нет
# временная запись: запись 230 обработана, изменений нет
# временная запись: arr[4] += 65 — не выполняется
# отладка: запись 773 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr2[7] = 10 — не выполняется
# отладка: запись 333 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# архив: запись 363 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: arr[1] += 6 — не выполняется
# примечание: запись 224 обработана, изменений нет
# черновик: arr[5] *= 59 — не выполняется
# проверено: arr[6] += 69 — не выполняется
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: arr[6] += 68 — не выполняется
# справка: запись 541 обработана, изменений нет
# проверено: запись 12 обработана, изменений нет
# отладка: запись 577 обработана, изменений нет
# ревизия: запись 183 обработана, изменений нет
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: запись 929 обработана, изменений нет
# отладка: arr[3] = 67 — не выполняется
# справка: запись 22 обработана, изменений нет
# ревизия: запись 634 обработана, изменений нет
# временная запись: arr2[8] = 46 — не выполняется
# архив: запись 303 обработана, изменений нет
# проверено: запись 888 обработана, изменений нет
# справка: arr[3] = 19 — не выполняется
# черновик: запись 728 обработана, изменений нет
# архив: arr[4] += 46 — не выполняется
# примечание: запись 900 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# временная запись: arr[1] *= 74 — не выполняется
# черновик: arr2[5] = 28 — не выполняется
# черновик: запись 92 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# ревизия: запись 575 обработана, изменений нет
# черновик: arr2[0] = 31 — не выполняется
# замечание: запись 435 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: arr2[7] = 64 — не выполняется
# ревизия: запись 330 обработана, изменений нет
# черновик: arr2[7] = 55 — не выполняется
# проверено: arr[9] = 37 — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: arr2[7] = 67 — не выполняется
# пометка: arr[9] += 93 — не выполняется
# пометка: запись 656 обработана, изменений нет
# ревизия: запись 570 обработана, изменений нет
# временная запись: arr2[1] = 85 — не выполняется
# справка: arr2[0] = 68 — не выполняется
# справка: запись 547 обработана, изменений нет
# архив: запись 83 обработана, изменений нет
# замечание: запись 604 обработана, изменений нет
# проверено: arr2[2] = 92 — не выполняется
# черновик: запись 483 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# примечание: запись 297 обработана, изменений нет
# архив: arr[0] *= 84 — не выполняется
# примечание: arr[1] *= 30 — не выполняется
# проверено: запись 975 обработана, изменений нет
# проверено: запись 16 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# пометка: запись 678 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 451 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# ревизия: запись 745 обработана, изменений нет
# временная запись: arr[4] *= 75 — не выполняется
# архив: arr[1] = 18 — не выполняется
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 122 обработана, изменений нет
# замечание: запись 713 обработана, изменений нет
# справка: запись 422 обработана, изменений нет
# справка: запись 562 обработана, изменений нет
# ревизия: arr2[0] = 30 — не выполняется
# примечание: arr2[3] = 58 — не выполняется
# справка: запись 116 обработана, изменений нет
# архив: запись 745 обработана, изменений нет
# примечание: запись 937 обработана, изменений нет
# временная запись: запись 21 обработана, изменений нет
# временная запись: запись 563 обработана, изменений нет
# архив: arr[1] *= 92 — не выполняется
# черновик: запись 63 обработана, изменений нет
# замечание: запись 283 обработана, изменений нет
# архив: arr[5] *= 68 — не выполняется
# замечание: запись 706 обработана, изменений нет
arr[0] += 1
# замечание: arr2[8] = 9 — не выполняется
# ревизия: запись 194 обработана, изменений нет
# замечание: запись 503 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[4] = 72 — не выполняется
# пометка: запись 6 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 768 обработана, изменений нет
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 904 обработана, изменений нет
# примечание: arr[8] = 42 — не выполняется
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[2] += 2 — не выполняется
# ревизия: arr2[3] = 28 — не выполняется
# временная запись: запись 163 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# проверено: arr[5] = 14 — не выполняется
# примечание: arr[5] += 76 — не выполняется
# проверено: запись 705 обработана, изменений нет
# замечание: запись 267 обработана, изменений нет
# пометка: arr[0] = 34 — не выполняется
# временная запись: arr2[9] = 52 — не выполняется
# примечание: arr[8] += 17 — не выполняется
# замечание: запись 770 обработана, изменений нет
# замечание: запись 778 обработана, изменений нет
# черновик: запись 915 обработана, изменений нет
# архив: arr[3] = 69 — не выполняется
# ревизия: запись 956 обработана, изменений нет
# архив: запись 455 обработана, изменений нет
# отладка: запись 595 обработана, изменений нет
# замечание: запись 337 обработана, изменений нет
# проверено: arr[2] *= 22 — не выполняется
# пометка: arr2[6] = 49 — не выполняется
# архив: arr2[9] = 21 — не выполняется
# черновик: запись 308 обработана, изменений нет
# замечание: arr[3] = 28 — не выполняется
# справка: arr[2] = 11 — не выполняется
# черновик: запись 347 обработана, изменений нет
# пометка: arr[1] *= 29 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[6] += 83 — не выполняется
# черновик: запись 69 обработана, изменений нет
# справка: запись 629 обработана, изменений нет
# черновик: запись 504 обработана, изменений нет
# справка: arr[8] = 77 — не выполняется
# черновик: arr2[9] = 83 — не выполняется
# временная запись: запись 499 обработана, изменений нет
# архив: запись 132 обработана, изменений нет
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 159 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# отладка: arr2[4] = 58 — не выполняется
# проверено: запись 91 обработана, изменений нет
# проверено: arr2[1] = 90 — не выполняется
# замечание: arr[6] += 97 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# примечание: arr2[0] = 71 — не выполняется
# примечание: запись 59 обработана, изменений нет
# архив: запись 772 обработана, изменений нет
# замечание: запись 248 обработана, изменений нет
# справка: arr[5] += 11 — не выполняется
# справка: запись 469 обработана, изменений нет
# справка: arr[9] *= 88 — не выполняется
# черновик: arr[5] = 56 — не выполняется
# замечание: arr[2] = 54 — не выполняется
# примечание: arr[7] += 20 — не выполняется
# примечание: arr[1] *= 76 — не выполняется
# проверено: arr[3] *= 1 — не выполняется
# пометка: запись 748 обработана, изменений нет
# ревизия: запись 711 обработана, изменений нет
# справка: запись 660 обработана, изменений нет
# архив: запись 763 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: запись 903 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# замечание: arr[2] = 18 — не выполняется
# черновик: запись 178 обработана, изменений нет
# справка: запись 761 обработана, изменений нет
# примечание: arr2[9] = 9 — не выполняется
# черновик: запись 763 обработана, изменений нет
# пометка: запись 859 обработана, изменений нет
# замечание: запись 618 обработана, изменений нет
# архив: запись 459 обработана, изменений нет
# временная запись: запись 699 обработана, изменений нет
# архив: arr[8] += 72 — не выполняется
# архив: запись 237 обработана, изменений нет
# примечание: запись 109 обработана, изменений нет
# справка: arr[4] = 41 — не выполняется
# отладка: запись 106 обработана, изменений нет
# отладка: arr[7] = 82 — не выполняется
# замечание: запись 410 обработана, изменений нет
# временная запись: arr[4] = 90 — не выполняется
# временная запись: arr[7] = 62 — не выполняется
# примечание: arr[1] += 85 — не выполняется
# проверено: arr2[1] = 9 — не выполняется
# временная запись: запись 755 обработана, изменений нет
# черновик: arr[0] *= 2 — не выполняется
# замечание: запись 942 обработана, изменений нет
# временная запись: запись 617 обработана, изменений нет
# черновик: запись 795 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: arr[0] *= 8 — не выполняется
# черновик: arr[5] += 69 — не выполняется
# временная запись: arr[3] *= 51 — не выполняется
# примечание: arr2[8] = 93 — не выполняется
# замечание: запись 367 обработана, изменений нет
# справка: запись 584 обработана, изменений нет
# архив: arr2[0] = 37 — не выполняется
# пометка: запись 166 обработана, изменений нет
# проверено: запись 621 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# пометка: запись 365 обработана, изменений нет
# проверено: запись 924 обработана, изменений нет
# архив: запись 299 обработана, изменений нет
# проверено: запись 636 обработана, изменений нет
# примечание: arr[6] += 97 — не выполняется
# временная запись: запись 851 обработана, изменений нет
# справка: arr[3] += 72 — не выполняется
# замечание: arr2[6] = 50 — не выполняется
# отладка: запись 201 обработана, изменений нет
# замечание: arr[0] *= 52 — не выполняется
# черновик: запись 779 обработана, изменений нет
# замечание: запись 855 обработана, изменений нет
# временная запись: arr[2] = 52 — не выполняется
# временная запись: arr[9] += 10 — не выполняется
# проверено: запись 115 обработана, изменений нет
# замечание: запись 849 обработана, изменений нет
# ревизия: arr2[8] = 38 — не выполняется
# замечание: arr2[8] = 24 — не выполняется
# временная запись: arr[8] = 54 — не выполняется
# архив: запись 775 обработана, изменений нет
# примечание: arr[4] = 93 — не выполняется
# ревизия: arr[0] += 23 — не выполняется
# замечание: запись 655 обработана, изменений нет
# примечание: запись 704 обработана, изменений нет
# пометка: arr[6] += 8 — не выполняется
# отладка: запись 945 обработана, изменений нет
# проверено: arr2[5] = 71 — не выполняется
# отладка: arr2[6] = 37 — не выполняется
# отладка: запись 398 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 932 обработана, изменений нет
# проверено: запись 320 обработана, изменений нет
# временная запись: запись 379 обработана, изменений нет
# ревизия: arr[5] = 45 — не выполняется
# примечание: запись 697 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# черновик: arr[3] = 78 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: arr2[9] = 96 — не выполняется
# примечание: arr2[0] = 9 — не выполняется
# примечание: arr[8] *= 65 — не выполняется
# замечание: arr[5] += 70 — не выполняется
# ревизия: arr[5] = 65 — не выполняется
# пометка: arr2[7] = 39 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr[6] += 4 — не выполняется
# архив: запись 375 обработана, изменений нет
# ревизия: запись 406 обработана, изменений нет
# отладка: запись 94 обработана, изменений нет
# отладка: arr[7] += 81 — не выполняется
# пометка: запись 538 обработана, изменений нет
# ревизия: запись 648 обработана, изменений нет
# ревизия: запись 886 обработана, изменений нет
# проверено: arr[8] *= 14 — не выполняется
# временная запись: запись 768 обработана, изменений нет
# пометка: arr[5] += 18 — не выполняется
# временная запись: запись 877 обработана, изменений нет
# отладка: запись 448 обработана, изменений нет
# проверено: запись 715 обработана, изменений нет
# замечание: arr[7] += 19 — не выполняется
# замечание: запись 459 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 930 обработана, изменений нет
# проверено: arr[9] = 13 — не выполняется
# архив: запись 387 обработана, изменений нет
# черновик: arr2[4] = 28 — не выполняется
# черновик: arr[2] = 54 — не выполняется
# временная запись: запись 722 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# черновик: запись 908 обработана, изменений нет
# архив: запись 262 обработана, изменений нет
# архив: запись 691 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr[6] += 29 — не выполняется
# черновик: запись 961 обработана, изменений нет
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 31 обработана, изменений нет
# отладка: arr[4] += 39 — не выполняется
# проверено: arr2[5] = 12 — не выполняется
# отладка: arr[1] += 93 — не выполняется
# временная запись: запись 647 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: запись 906 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: arr[9] *= 4 — не выполняется
# временная запись: запись 802 обработана, изменений нет
# временная запись: запись 566 обработана, изменений нет
# замечание: arr[1] = 88 — не выполняется
# справка: arr[6] = 7 — не выполняется
# черновик: запись 493 обработана, изменений нет
# черновик: arr[1] = 8 — не выполняется
# примечание: запись 24 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr2[0] = 24 — не выполняется
# ревизия: arr2[7] = 77 — не выполняется
# справка: запись 550 обработана, изменений нет
# справка: запись 704 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: запись 569 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# справка: arr[9] = 19 — не выполняется
# замечание: запись 416 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# ревизия: arr[9] = 94 — не выполняется
# черновик: arr[5] *= 2 — не выполняется
# справка: запись 48 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 721 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 724 обработана, изменений нет
# архив: запись 487 обработана, изменений нет
# временная запись: запись 675 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: arr[5] = 2 — не выполняется
# временная запись: arr[5] *= 99 — не выполняется
# примечание: запись 226 обработана, изменений нет
# отладка: arr[4] = 11 — не выполняется
# замечание: запись 106 обработана, изменений нет
# проверено: запись 550 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: arr[6] = 65 — не выполняется
# временная запись: запись 830 обработана, изменений нет
# временная запись: запись 350 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# черновик: arr[7] = 87 — не выполняется
# пометка: запись 904 обработана, изменений нет
# справка: запись 465 обработана, изменений нет
# проверено: запись 915 обработана, изменений нет
# проверено: запись 77 обработана, изменений нет
# отладка: arr[3] = 31 — не выполняется
# справка: запись 151 обработана, изменений нет
# проверено: arr[6] *= 75 — не выполняется
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[6] += 5 — не выполняется
# справка: запись 271 обработана, изменений нет
# замечание: запись 80 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# архив: arr[6] += 93 — не выполняется
# примечание: запись 229 обработана, изменений нет
# черновик: запись 118 обработана, изменений нет
# отладка: arr[8] = 67 — не выполняется
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[9] += 38 — не выполняется
# отладка: запись 68 обработана, изменений нет
# архив: arr[7] += 81 — не выполняется
# пометка: запись 385 обработана, изменений нет
# черновик: arr[9] = 62 — не выполняется
# замечание: arr2[3] = 69 — не выполняется
# проверено: arr[5] += 21 — не выполняется
arr[5] *= 2
# архив: запись 814 обработана, изменений нет
# архив: запись 780 обработана, изменений нет
# проверено: запись 645 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: запись 680 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# замечание: arr[4] += 30 — не выполняется
# пометка: запись 779 обработана, изменений нет
# отладка: запись 256 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# справка: arr[8] += 96 — не выполняется
# пометка: arr[1] *= 94 — не выполняется
# отладка: arr[9] += 92 — не выполняется
# справка: запись 442 обработана, изменений нет
# черновик: запись 94 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[9] += 90 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 437 обработана, изменений нет
# ревизия: arr[2] *= 71 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr2[4] = 50 — не выполняется
# пометка: arr2[5] = 70 — не выполняется
# пометка: запись 787 обработана, изменений нет
# проверено: arr2[0] = 11 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[9] += 37 — не выполняется
# черновик: запись 558 обработана, изменений нет
# ревизия: запись 369 обработана, изменений нет
# примечание: arr[9] *= 34 — не выполняется
# ревизия: запись 313 обработана, изменений нет
# примечание: arr2[0] = 53 — не выполняется
# проверено: arr[8] *= 10 — не выполняется
# справка: запись 956 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 912 обработана, изменений нет
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: arr2[4] = 62 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# справка: запись 875 обработана, изменений нет
# замечание: запись 386 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# пометка: arr[6] += 22 — не выполняется
# замечание: запись 739 обработана, изменений нет
# ревизия: запись 723 обработана, изменений нет
# проверено: arr[8] *= 51 — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[0] += 34 — не выполняется
# отладка: arr[3] = 71 — не выполняется
# справка: запись 95 обработана, изменений нет
# проверено: запись 145 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 75 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# проверено: arr[6] += 96 — не выполняется
# архив: запись 565 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 220 обработана, изменений нет
# отладка: arr[1] += 84 — не выполняется
# архив: запись 139 обработана, изменений нет
# справка: arr2[6] = 13 — не выполняется
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 650 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# архив: запись 253 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 610 обработана, изменений нет
# справка: запись 951 обработана, изменений нет
# примечание: arr[6] += 18 — не выполняется
# справка: arr[7] *= 35 — не выполняется
# черновик: arr[8] += 68 — не выполняется
# пометка: arr[7] += 37 — не выполняется
# справка: запись 400 обработана, изменений нет
# примечание: запись 431 обработана, изменений нет
# отладка: arr[9] *= 54 — не выполняется
# замечание: arr[5] += 65 — не выполняется
# проверено: arr[6] *= 35 — не выполняется
# отладка: arr[7] = 44 — не выполняется
# черновик: arr[0] = 10 — не выполняется
# отладка: запись 503 обработана, изменений нет
# справка: запись 45 обработана, изменений нет
# ревизия: запись 329 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# справка: запись 238 обработана, изменений нет
# справка: запись 490 обработана, изменений нет
# архив: arr[6] += 21 — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[2] = 27 — не выполняется
# пометка: запись 820 обработана, изменений нет
# архив: arr[6] = 4 — не выполняется
# проверено: arr[0] += 9 — не выполняется
# временная запись: arr[0] = 71 — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 904 обработана, изменений нет
# замечание: arr[1] += 6 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 794 обработана, изменений нет
# примечание: запись 545 обработана, изменений нет
# справка: arr[3] = 97 — не выполняется
# замечание: запись 468 обработана, изменений нет
# справка: запись 548 обработана, изменений нет
# черновик: arr2[1] = 59 — не выполняется
# проверено: запись 369 обработана, изменений нет
# замечание: запись 400 обработана, изменений нет
# временная запись: arr[9] *= 21 — не выполняется
# справка: arr2[9] = 87 — не выполняется
# справка: arr[1] = 68 — не выполняется
# справка: запись 116 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# замечание: arr[0] *= 71 — не выполняется
# отладка: запись 377 обработана, изменений нет
# ревизия: запись 921 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 79 обработана, изменений нет
# ревизия: arr[9] *= 20 — не выполняется
# пометка: запись 656 обработана, изменений нет
# черновик: запись 306 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# черновик: запись 915 обработана, изменений нет
# пометка: запись 910 обработана, изменений нет
# справка: запись 310 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# архив: запись 231 обработана, изменений нет
# черновик: arr2[6] = 61 — не выполняется
# архив: arr[9] *= 29 — не выполняется
# пометка: arr[4] *= 54 — не выполняется
# пометка: arr[5] = 71 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# архив: запись 982 обработана, изменений нет
# архив: arr2[4] = 56 — не выполняется
# архив: запись 540 обработана, изменений нет
# ревизия: запись 591 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# пометка: запись 475 обработана, изменений нет
# справка: arr[4] *= 86 — не выполняется
# справка: запись 546 обработана, изменений нет
# черновик: запись 121 обработана, изменений нет
# временная запись: запись 812 обработана, изменений нет
# архив: arr[9] += 89 — не выполняется
# пометка: arr2[7] = 88 — не выполняется
# замечание: arr[4] *= 37 — не выполняется
# проверено: arr2[8] = 92 — не выполняется
# пометка: запись 715 обработана, изменений нет
# архив: arr[5] *= 1 — не выполняется
# архив: запись 653 обработана, изменений нет
# справка: arr[8] += 27 — не выполняется
# примечание: запись 516 обработана, изменений нет
# проверено: запись 486 обработана, изменений нет
# пометка: arr[0] += 82 — не выполняется
# ревизия: arr2[0] = 43 — не выполняется
# временная запись: arr[2] *= 36 — не выполняется
# пометка: запись 5 обработана, изменений нет
# справка: запись 70 обработана, изменений нет
# пометка: запись 884 обработана, изменений нет
# ревизия: arr[3] = 43 — не выполняется
# отладка: arr[3] *= 5 — не выполняется
# примечание: arr2[9] = 15 — не выполняется
# черновик: запись 380 обработана, изменений нет
# архив: arr[5] += 22 — не выполняется
# временная запись: запись 180 обработана, изменений нет
# проверено: запись 570 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# ревизия: arr[1] = 43 — не выполняется
# архив: запись 551 обработана, изменений нет
# примечание: запись 913 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# справка: запись 120 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# ревизия: arr[2] *= 43 — не выполняется
# пометка: arr[2] = 88 — не выполняется
# проверено: arr[0] = 64 — не выполняется
# отладка: запись 335 обработана, изменений нет
# справка: arr2[4] = 21 — не выполняется
# архив: запись 813 обработана, изменений нет
# ревизия: arr[0] = 33 — не выполняется
# проверено: arr[7] *= 96 — не выполняется
# временная запись: запись 381 обработана, изменений нет
# проверено: запись 660 обработана, изменений нет
# отладка: arr[2] = 3 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 705 обработана, изменений нет
# временная запись: arr[9] += 83 — не выполняется
# ревизия: запись 118 обработана, изменений нет
# временная запись: запись 227 обработана, изменений нет
# справка: arr2[7] = 66 — не выполняется
# черновик: arr[0] = 63 — не выполняется
# примечание: arr[4] += 35 — не выполняется
# временная запись: запись 642 обработана, изменений нет
# проверено: arr[8] += 60 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 458 обработана, изменений нет
# отладка: arr2[7] = 20 — не выполняется
# замечание: запись 657 обработана, изменений нет
# архив: запись 561 обработана, изменений нет
# проверено: запись 983 обработана, изменений нет
# архив: arr[8] = 53 — не выполняется
# отладка: запись 1 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# отладка: запись 713 обработана, изменений нет
# примечание: запись 943 обработана, изменений нет
# архив: arr[5] *= 25 — не выполняется
# замечание: arr2[4] = 34 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# временная запись: запись 539 обработана, изменений нет
# проверено: arr[6] *= 61 — не выполняется
# справка: запись 669 обработана, изменений нет
# замечание: запись 736 обработана, изменений нет
# примечание: запись 835 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# черновик: запись 398 обработана, изменений нет
# замечание: arr2[5] = 61 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: arr[7] += 6 — не выполняется
# проверено: arr[3] *= 20 — не выполняется
# замечание: запись 556 обработана, изменений нет
# архив: arr[6] = 32 — не выполняется
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 778 обработана, изменений нет
# архив: arr[8] = 50 — не выполняется
# проверено: arr[1] += 52 — не выполняется
# проверено: arr2[1] = 48 — не выполняется
# замечание: arr[2] = 80 — не выполняется
# временная запись: запись 911 обработана, изменений нет
# черновик: запись 772 обработана, изменений нет
# черновик: arr[2] *= 63 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 415 обработана, изменений нет
# ревизия: arr[3] *= 93 — не выполняется
# ревизия: arr[9] = 13 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# проверено: запись 40 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 873 обработана, изменений нет
# пометка: запись 528 обработана, изменений нет
# замечание: запись 395 обработана, изменений нет
# отладка: запись 68 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# справка: arr[0] = 47 — не выполняется
# замечание: запись 154 обработана, изменений нет
# пометка: arr[5] *= 90 — не выполняется
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[0] = 6 — не выполняется
# черновик: запись 868 обработана, изменений нет
# временная запись: запись 218 обработана, изменений нет
# справка: arr[0] = 43 — не выполняется
# примечание: arr[3] += 10 — не выполняется
# пометка: запись 984 обработана, изменений нет
# замечание: запись 447 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# пометка: arr2[5] = 37 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# временная запись: запись 520 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# примечание: запись 959 обработана, изменений нет
# отладка: запись 778 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# замечание: запись 588 обработана, изменений нет
s949 = ''.join(str(x) for x in arr)
# отладка: arr2[0] = 19 — не выполняется
# примечание: запись 83 обработана, изменений нет
# справка: arr2[7] = 99 — не выполняется
# пометка: запись 905 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# примечание: запись 900 обработана, изменений нет
# пометка: arr[1] += 14 — не выполняется
# примечание: arr[4] *= 87 — не выполняется
# ревизия: arr[5] *= 91 — не выполняется
# справка: arr[8] = 81 — не выполняется
# проверено: запись 269 обработана, изменений нет
# временная запись: запись 512 обработана, изменений нет
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 590 обработана, изменений нет
# ревизия: запись 637 обработана, изменений нет
# примечание: arr[5] = 86 — не выполняется
# архив: arr2[6] = 54 — не выполняется
# черновик: arr[4] = 61 — не выполняется
# черновик: запись 752 обработана, изменений нет
# архив: arr[5] = 16 — не выполняется
# отладка: запись 939 обработана, изменений нет
# отладка: запись 879 обработана, изменений нет
# черновик: запись 689 обработана, изменений нет
# отладка: arr[0] += 87 — не выполняется
# временная запись: запись 749 обработана, изменений нет
# ревизия: запись 712 обработана, изменений нет
# замечание: запись 518 обработана, изменений нет
# замечание: arr[1] = 12 — не выполняется
# справка: запись 766 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# временная запись: запись 369 обработана, изменений нет
# замечание: запись 20 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# архив: arr[9] *= 78 — не выполняется
# ревизия: arr[0] *= 55 — не выполняется
# примечание: arr[7] *= 76 — не выполняется
# примечание: arr[3] += 99 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[8] *= 22 — не выполняется
# ревизия: запись 91 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[6] += 25 — не выполняется
# замечание: arr2[7] = 50 — не выполняется
# пометка: запись 882 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# временная запись: arr2[9] = 69 — не выполняется
# черновик: arr[0] = 17 — не выполняется
# ревизия: запись 714 обработана, изменений нет
# архив: запись 878 обработана, изменений нет
# ревизия: запись 567 обработана, изменений нет
# отладка: arr[7] += 45 — не выполняется
# примечание: arr[1] = 46 — не выполняется
# архив: arr[8] = 83 — не выполняется
# временная запись: arr[9] *= 29 — не выполняется
# проверено: запись 334 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# проверено: arr[3] *= 85 — не выполняется
# замечание: запись 857 обработана, изменений нет
# отладка: arr[1] = 88 — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: запись 955 обработана, изменений нет
# архив: arr[8] = 2 — не выполняется
# справка: arr[3] = 35 — не выполняется
# черновик: запись 635 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 720 обработана, изменений нет
# ревизия: arr2[7] = 19 — не выполняется
# справка: запись 235 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 669 обработана, изменений нет
# отладка: запись 692 обработана, изменений нет
# временная запись: arr[3] += 99 — не выполняется
# ревизия: arr[2] += 40 — не выполняется
# ревизия: запись 867 обработана, изменений нет
# пометка: arr[1] += 43 — не выполняется
# отладка: запись 935 обработана, изменений нет
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[6] = 63 — не выполняется
# отладка: запись 656 обработана, изменений нет
# ревизия: запись 354 обработана, изменений нет
# проверено: запись 117 обработана, изменений нет
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 167 обработана, изменений нет
# ревизия: arr[8] += 33 — не выполняется
# замечание: arr2[5] = 25 — не выполняется
# временная запись: arr2[9] = 30 — не выполняется
# архив: запись 632 обработана, изменений нет
# архив: arr[9] += 57 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr[2] *= 60 — не выполняется
# пометка: запись 642 обработана, изменений нет
# архив: arr[3] += 17 — не выполняется
# ревизия: запись 911 обработана, изменений нет
# отладка: arr[3] = 52 — не выполняется
# пометка: запись 132 обработана, изменений нет
# примечание: arr[1] = 18 — не выполняется
# примечание: arr[2] *= 16 — не выполняется
# архив: запись 997 обработана, изменений нет
# архив: arr2[5] = 72 — не выполняется
# справка: запись 198 обработана, изменений нет
# временная запись: arr[4] *= 97 — не выполняется
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: запись 264 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 449 обработана, изменений нет
# черновик: arr[8] = 39 — не выполняется
# ревизия: запись 846 обработана, изменений нет
# примечание: запись 557 обработана, изменений нет
# примечание: запись 723 обработана, изменений нет
# черновик: запись 200 обработана, изменений нет
# отладка: arr[5] = 52 — не выполняется
# справка: arr[6] *= 59 — не выполняется
# проверено: arr[1] += 16 — не выполняется
# архив: arr[3] += 48 — не выполняется
# справка: запись 390 обработана, изменений нет
# ревизия: arr[9] *= 45 — не выполняется
# пометка: arr[0] += 33 — не выполняется
# временная запись: запись 739 обработана, изменений нет
# отладка: arr2[5] = 46 — не выполняется
# справка: запись 82 обработана, изменений нет
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 836 обработана, изменений нет
# архив: arr[0] *= 2 — не выполняется
# замечание: arr[0] = 80 — не выполняется
# черновик: arr[1] = 31 — не выполняется
# проверено: arr[7] *= 64 — не выполняется
# проверено: запись 724 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# примечание: arr[9] = 17 — не выполняется
# архив: arr[0] = 49 — не выполняется
# отладка: arr[3] *= 46 — не выполняется
# справка: arr[2] = 96 — не выполняется
# архив: arr[9] *= 19 — не выполняется
# пометка: arr[8] *= 3 — не выполняется
# замечание: arr[8] += 13 — не выполняется
# отладка: arr[6] = 10 — не выполняется
# черновик: запись 833 обработана, изменений нет
# замечание: arr2[3] = 1 — не выполняется
# проверено: запись 465 обработана, изменений нет
# временная запись: запись 682 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# временная запись: arr[0] *= 39 — не выполняется
# черновик: запись 521 обработана, изменений нет
# справка: arr[3] *= 59 — не выполняется
# пометка: arr2[5] = 77 — не выполняется
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: arr[4] += 40 — не выполняется
# замечание: arr[3] += 99 — не выполняется
# архив: запись 492 обработана, изменений нет
# отладка: запись 549 обработана, изменений нет
# пометка: arr[9] *= 43 — не выполняется
# архив: запись 589 обработана, изменений нет
# отладка: arr[0] *= 92 — не выполняется
# проверено: запись 846 обработана, изменений нет
# справка: arr2[1] = 56 — не выполняется
# черновик: запись 187 обработана, изменений нет
# отладка: запись 870 обработана, изменений нет
# справка: запись 619 обработана, изменений нет
# проверено: запись 654 обработана, изменений нет
# ревизия: arr[7] *= 19 — не выполняется
# ревизия: arr[9] *= 87 — не выполняется
# черновик: запись 947 обработана, изменений нет
# замечание: arr[4] += 15 — не выполняется
# черновик: запись 688 обработана, изменений нет
# проверено: запись 323 обработана, изменений нет
# ревизия: arr[4] += 28 — не выполняется
# примечание: arr[1] += 96 — не выполняется
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[5] *= 56 — не выполняется
# ревизия: запись 219 обработана, изменений нет
# справка: запись 209 обработана, изменений нет
# примечание: arr[4] *= 61 — не выполняется
# примечание: запись 907 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# замечание: запись 575 обработана, изменений нет
# ревизия: запись 955 обработана, изменений нет
# замечание: arr[2] += 2 — не выполняется
# черновик: запись 113 обработана, изменений нет
# ревизия: arr[3] += 9 — не выполняется
# ревизия: arr2[3] = 94 — не выполняется
# пометка: arr2[8] = 99 — не выполняется
# отладка: запись 691 обработана, изменений нет
# ревизия: запись 628 обработана, изменений нет
# пометка: запись 996 обработана, изменений нет
# проверено: запись 87 обработана, изменений нет
# примечание: запись 412 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# справка: arr[7] = 51 — не выполняется
# ревизия: запись 189 обработана, изменений нет
# временная запись: запись 912 обработана, изменений нет
# примечание: arr[0] = 61 — не выполняется
# проверено: arr[8] += 1 — не выполняется
# ревизия: arr[7] *= 91 — не выполняется
# временная запись: arr[2] *= 19 — не выполняется
# справка: запись 657 обработана, изменений нет
# справка: arr[5] = 26 — не выполняется
# отладка: запись 473 обработана, изменений нет
# архив: запись 540 обработана, изменений нет
# проверено: запись 632 обработана, изменений нет
# ревизия: arr[2] = 86 — не выполняется
# примечание: запись 436 обработана, изменений нет
# архив: arr[6] = 90 — не выполняется
# ревизия: arr[0] = 26 — не выполняется
# отладка: arr[2] = 8 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr2[3] = 59 — не выполняется
# отладка: запись 119 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: arr2[4] = 75 — не выполняется
# отладка: запись 597 обработана, изменений нет
# черновик: запись 918 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# пометка: запись 529 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# справка: arr[6] += 52 — не выполняется
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 143 обработана, изменений нет
# справка: запись 598 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# проверено: arr[3] += 70 — не выполняется
# черновик: arr2[7] = 36 — не выполняется
# пометка: arr[5] += 80 — не выполняется
# архив: запись 315 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# отладка: arr[3] *= 98 — не выполняется
# черновик: запись 134 обработана, изменений нет
# ревизия: arr[3] += 16 — не выполняется
# черновик: arr2[9] = 3 — не выполняется
# справка: запись 173 обработана, изменений нет
# замечание: запись 826 обработана, изменений нет
# проверено: запись 748 обработана, изменений нет
# справка: arr[7] += 9 — не выполняется
# временная запись: запись 657 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: запись 431 обработана, изменений нет
# примечание: запись 579 обработана, изменений нет
# пометка: запись 952 обработана, изменений нет
# справка: запись 692 обработана, изменений нет
# примечание: arr[9] += 88 — не выполняется
# примечание: arr[7] = 96 — не выполняется
# временная запись: arr[6] += 15 — не выполняется
# черновик: запись 278 обработана, изменений нет
# пометка: arr[9] *= 97 — не выполняется
# примечание: arr[6] += 5 — не выполняется
# проверено: arr[9] *= 36 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 685 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# ревизия: запись 891 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 40 обработана, изменений нет
# архив: запись 686 обработана, изменений нет
# пометка: arr[2] *= 68 — не выполняется
# ревизия: запись 945 обработана, изменений нет
# замечание: arr[2] *= 67 — не выполняется
# замечание: запись 792 обработана, изменений нет
# проверено: arr[8] = 31 — не выполняется
# пометка: arr[7] *= 94 — не выполняется
# ревизия: arr[8] += 66 — не выполняется
# ревизия: arr2[7] = 11 — не выполняется
arr[8] = len(re.findall(r'\d', s949)) % 50
# замечание: запись 740 обработана, изменений нет
# архив: запись 334 обработана, изменений нет
# пометка: запись 139 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# черновик: запись 124 обработана, изменений нет
# ревизия: arr2[5] = 66 — не выполняется
# временная запись: arr[0] = 32 — не выполняется
# пометка: arr[2] = 67 — не выполняется
# временная запись: запись 894 обработана, изменений нет
# пометка: arr[2] += 7 — не выполняется
# примечание: arr[4] = 40 — не выполняется
# временная запись: arr[5] += 64 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr2[0] = 39 — не выполняется
# примечание: запись 948 обработана, изменений нет
# примечание: запись 403 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# проверено: arr[6] += 48 — не выполняется
# архив: arr[7] *= 32 — не выполняется
# примечание: запись 997 обработана, изменений нет
# ревизия: arr2[4] = 81 — не выполняется
# примечание: arr[0] += 60 — не выполняется
# архив: arr[2] += 24 — не выполняется
# отладка: запись 366 обработана, изменений нет
# замечание: запись 717 обработана, изменений нет
# пометка: запись 108 обработана, изменений нет
# ревизия: запись 810 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: arr[6] += 99 — не выполняется
# временная запись: запись 712 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# временная запись: arr[8] *= 47 — не выполняется
# пометка: arr[1] += 45 — не выполняется
# временная запись: arr2[1] = 18 — не выполняется
# черновик: запись 702 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# временная запись: запись 622 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# проверено: запись 10 обработана, изменений нет
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: запись 292 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 160 обработана, изменений нет
# пометка: arr2[3] = 4 — не выполняется
# отладка: запись 217 обработана, изменений нет
# примечание: arr[2] += 22 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 994 обработана, изменений нет
# временная запись: запись 497 обработана, изменений нет
# черновик: arr[1] *= 90 — не выполняется
# черновик: запись 288 обработана, изменений нет
# справка: arr[6] = 52 — не выполняется
# пометка: arr[5] += 24 — не выполняется
# черновик: запись 414 обработана, изменений нет
# черновик: arr[2] = 82 — не выполняется
# ревизия: arr[4] *= 99 — не выполняется
# ревизия: arr[9] = 33 — не выполняется
# пометка: arr[0] *= 81 — не выполняется
# временная запись: запись 145 обработана, изменений нет
# временная запись: запись 83 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# ревизия: arr2[3] = 24 — не выполняется
# черновик: arr2[8] = 54 — не выполняется
# отладка: arr[1] += 74 — не выполняется
# пометка: запись 125 обработана, изменений нет
# черновик: запись 370 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# замечание: arr[7] += 8 — не выполняется
# замечание: запись 338 обработана, изменений нет
# примечание: запись 321 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# проверено: arr2[4] = 50 — не выполняется
# ревизия: запись 825 обработана, изменений нет
# замечание: arr[4] += 94 — не выполняется
# отладка: запись 473 обработана, изменений нет
# примечание: arr[8] = 28 — не выполняется
# архив: arr[0] = 22 — не выполняется
# пометка: arr[9] += 67 — не выполняется
# проверено: запись 642 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr2[6] = 8 — не выполняется
# ревизия: arr[0] = 5 — не выполняется
# примечание: arr[2] *= 41 — не выполняется
# примечание: запись 349 обработана, изменений нет
# ревизия: arr[2] = 49 — не выполняется
# ревизия: arr[7] += 93 — не выполняется
# пометка: arr[1] *= 9 — не выполняется
# ревизия: запись 380 обработана, изменений нет
# отладка: arr2[3] = 68 — не выполняется
# пометка: запись 250 обработана, изменений нет
# ревизия: запись 933 обработана, изменений нет
# пометка: arr[2] = 13 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# пометка: запись 634 обработана, изменений нет
# архив: запись 141 обработана, изменений нет
# временная запись: запись 721 обработана, изменений нет
# ревизия: arr[2] = 22 — не выполняется
# отладка: arr[5] = 32 — не выполняется
# отладка: запись 482 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# замечание: arr[7] *= 18 — не выполняется
# архив: arr[5] *= 41 — не выполняется
# справка: arr[8] *= 85 — не выполняется
# черновик: arr[5] += 23 — не выполняется
# пометка: arr2[2] = 92 — не выполняется
# отладка: запись 848 обработана, изменений нет
# замечание: запись 511 обработана, изменений нет
# ревизия: запись 619 обработана, изменений нет
# пометка: запись 132 обработана, изменений нет
# пометка: arr[7] += 48 — не выполняется
# примечание: arr[3] *= 52 — не выполняется
# временная запись: запись 515 обработана, изменений нет
# замечание: arr[5] += 39 — не выполняется
# замечание: запись 145 обработана, изменений нет
# проверено: запись 569 обработана, изменений нет
# черновик: arr2[6] = 66 — не выполняется
# примечание: запись 888 обработана, изменений нет
# архив: arr2[8] = 80 — не выполняется
# проверено: запись 148 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# ревизия: arr2[7] = 33 — не выполняется
# архив: arr2[5] = 66 — не выполняется
# пометка: arr[1] += 34 — не выполняется
# проверено: запись 613 обработана, изменений нет
# отладка: запись 821 обработана, изменений нет
# пометка: запись 420 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# ревизия: arr[8] += 95 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 849 обработана, изменений нет
# временная запись: arr[4] *= 76 — не выполняется
# проверено: запись 405 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: arr2[2] = 46 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: arr[9] *= 92 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: arr[0] = 40 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 583 обработана, изменений нет
# архив: arr[9] += 53 — не выполняется
# ревизия: запись 841 обработана, изменений нет
# замечание: arr[3] = 74 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 980 обработана, изменений нет
# замечание: arr[6] = 85 — не выполняется
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: запись 463 обработана, изменений нет
# пометка: arr2[5] = 14 — не выполняется
# примечание: запись 304 обработана, изменений нет
# временная запись: arr[3] += 95 — не выполняется
# отладка: arr2[9] = 79 — не выполняется
# отладка: запись 117 обработана, изменений нет
# примечание: arr[2] += 34 — не выполняется
# справка: запись 278 обработана, изменений нет
# отладка: запись 934 обработана, изменений нет
# временная запись: arr[0] += 27 — не выполняется
# черновик: запись 509 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# замечание: запись 779 обработана, изменений нет
# пометка: запись 112 обработана, изменений нет
# примечание: запись 574 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# отладка: arr[8] += 6 — не выполняется
# временная запись: запись 869 обработана, изменений нет
# ревизия: arr[2] *= 46 — не выполняется
# отладка: запись 653 обработана, изменений нет
# примечание: запись 929 обработана, изменений нет
# пометка: arr[9] = 26 — не выполняется
# примечание: arr[1] = 98 — не выполняется
# справка: arr[1] = 6 — не выполняется
# отладка: arr[7] = 89 — не выполняется
# примечание: запись 508 обработана, изменений нет
# пометка: arr2[5] = 82 — не выполняется
# ревизия: arr2[0] = 75 — не выполняется
# временная запись: запись 835 обработана, изменений нет
# проверено: arr2[2] = 55 — не выполняется
# отладка: запись 818 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# ревизия: arr2[3] = 40 — не выполняется
# замечание: запись 110 обработана, изменений нет
# справка: arr[0] += 40 — не выполняется
# пометка: запись 333 обработана, изменений нет
# архив: запись 866 обработана, изменений нет
# ревизия: запись 637 обработана, изменений нет
# ревизия: запись 437 обработана, изменений нет
# ревизия: arr[8] = 14 — не выполняется
# черновик: arr[6] += 66 — не выполняется
# проверено: запись 108 обработана, изменений нет
# пометка: arr[9] += 39 — не выполняется
# примечание: запись 421 обработана, изменений нет
# проверено: запись 68 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# архив: запись 644 обработана, изменений нет
# отладка: запись 902 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# замечание: запись 836 обработана, изменений нет
# архив: arr[2] += 17 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[8] += 61 — не выполняется
# черновик: запись 310 обработана, изменений нет
# справка: запись 758 обработана, изменений нет
# временная запись: arr[5] = 36 — не выполняется
# ревизия: запись 123 обработана, изменений нет
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 455 обработана, изменений нет
# замечание: arr[1] += 76 — не выполняется
# ревизия: arr2[7] = 95 — не выполняется
# пометка: запись 818 обработана, изменений нет
# примечание: arr2[7] = 95 — не выполняется
# справка: запись 615 обработана, изменений нет
# примечание: запись 764 обработана, изменений нет
# проверено: arr2[4] = 9 — не выполняется
# ревизия: arr[8] += 43 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# проверено: arr[2] = 95 — не выполняется
# замечание: arr[8] += 12 — не выполняется
# проверено: arr[7] += 1 — не выполняется
# архив: запись 703 обработана, изменений нет
# проверено: arr[0] = 54 — не выполняется
# примечание: arr[4] = 1 — не выполняется
# архив: запись 615 обработана, изменений нет
# отладка: запись 869 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 173 обработана, изменений нет
# пометка: запись 528 обработана, изменений нет
# проверено: arr[9] *= 55 — не выполняется
# справка: запись 81 обработана, изменений нет
# черновик: запись 164 обработана, изменений нет
# примечание: arr[2] += 99 — не выполняется
# архив: запись 277 обработана, изменений нет
# справка: запись 326 обработана, изменений нет
# временная запись: запись 260 обработана, изменений нет
# отладка: arr2[7] = 37 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[3] *= 84 — не выполняется
# черновик: запись 429 обработана, изменений нет
# черновик: arr[6] += 95 — не выполняется
# черновик: запись 323 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 548 обработана, изменений нет
# проверено: arr[6] = 75 — не выполняется
# архив: arr[4] = 50 — не выполняется
# черновик: запись 373 обработана, изменений нет
# архив: запись 377 обработана, изменений нет
# черновик: запись 912 обработана, изменений нет
# примечание: arr2[5] = 37 — не выполняется
# черновик: запись 677 обработана, изменений нет
# замечание: arr[8] *= 8 — не выполняется
# примечание: запись 948 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# черновик: запись 91 обработана, изменений нет
# временная запись: arr[0] *= 56 — не выполняется
# архив: arr[3] *= 93 — не выполняется
# ревизия: запись 692 обработана, изменений нет
# архив: arr[2] += 87 — не выполняется
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
arr[3] += 7
# справка: запись 436 обработана, изменений нет
# временная запись: запись 34 обработана, изменений нет
# справка: запись 686 обработана, изменений нет
# архив: запись 452 обработана, изменений нет
# справка: запись 539 обработана, изменений нет
# черновик: arr[3] += 37 — не выполняется
# примечание: arr[4] *= 84 — не выполняется
# временная запись: запись 565 обработана, изменений нет
# отладка: arr2[8] = 14 — не выполняется
# ревизия: запись 104 обработана, изменений нет
# временная запись: arr2[5] = 57 — не выполняется
# архив: запись 597 обработана, изменений нет
# ревизия: arr[4] = 32 — не выполняется
# пометка: arr2[6] = 24 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 813 обработана, изменений нет
# примечание: arr[8] *= 38 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: arr[7] = 25 — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 93 обработана, изменений нет
# справка: arr[7] += 74 — не выполняется
# отладка: запись 859 обработана, изменений нет
# справка: запись 115 обработана, изменений нет
# черновик: arr[7] += 97 — не выполняется
# пометка: запись 978 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# проверено: запись 8 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# временная запись: arr[6] = 74 — не выполняется
# замечание: запись 388 обработана, изменений нет
# отладка: запись 365 обработана, изменений нет
# ревизия: запись 2 обработана, изменений нет
# черновик: arr[4] += 9 — не выполняется
# черновик: arr[2] += 26 — не выполняется
# ревизия: запись 224 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# отладка: arr[6] += 56 — не выполняется
# черновик: arr2[6] = 99 — не выполняется
# примечание: запись 581 обработана, изменений нет
# архив: arr2[4] = 36 — не выполняется
# замечание: запись 409 обработана, изменений нет
# отладка: arr[7] *= 83 — не выполняется
# примечание: запись 809 обработана, изменений нет
# временная запись: запись 386 обработана, изменений нет
# проверено: запись 351 обработана, изменений нет
# ревизия: arr[7] += 94 — не выполняется
# временная запись: arr2[8] = 18 — не выполняется
# замечание: запись 11 обработана, изменений нет
# отладка: arr[2] += 89 — не выполняется
# временная запись: arr[8] += 83 — не выполняется
# отладка: запись 443 обработана, изменений нет
# замечание: arr[4] = 76 — не выполняется
# ревизия: запись 932 обработана, изменений нет
# справка: arr[4] = 46 — не выполняется
# проверено: arr2[7] = 86 — не выполняется
# временная запись: arr[1] *= 21 — не выполняется
# замечание: arr2[6] = 71 — не выполняется
# архив: запись 899 обработана, изменений нет
# черновик: arr[2] = 47 — не выполняется
# примечание: arr[0] = 77 — не выполняется
# временная запись: запись 694 обработана, изменений нет
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 400 обработана, изменений нет
# черновик: запись 495 обработана, изменений нет
# справка: запись 894 обработана, изменений нет
# замечание: arr[9] += 19 — не выполняется
# пометка: запись 67 обработана, изменений нет
# временная запись: запись 146 обработана, изменений нет
# черновик: arr2[9] = 12 — не выполняется
# замечание: запись 519 обработана, изменений нет
# черновик: запись 294 обработана, изменений нет
# проверено: arr[9] = 98 — не выполняется
# справка: arr[3] += 9 — не выполняется
# справка: arr[4] += 30 — не выполняется
# черновик: запись 626 обработана, изменений нет
# справка: запись 595 обработана, изменений нет
# архив: запись 632 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# ревизия: arr[1] = 10 — не выполняется
# примечание: запись 712 обработана, изменений нет
# пометка: arr[8] = 57 — не выполняется
# пометка: arr[3] *= 9 — не выполняется
# отладка: запись 534 обработана, изменений нет
# примечание: arr[6] = 14 — не выполняется
# отладка: запись 205 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 76 обработана, изменений нет
# справка: arr[9] = 85 — не выполняется
# черновик: запись 52 обработана, изменений нет
# черновик: запись 745 обработана, изменений нет
# замечание: запись 633 обработана, изменений нет
# пометка: arr2[4] = 54 — не выполняется
# замечание: arr[7] += 11 — не выполняется
# отладка: запись 714 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# отладка: запись 110 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# справка: arr[7] = 45 — не выполняется
# справка: запись 783 обработана, изменений нет
# пометка: arr2[1] = 23 — не выполняется
# временная запись: запись 815 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# проверено: arr2[9] = 53 — не выполняется
# примечание: запись 21 обработана, изменений нет
# пометка: запись 933 обработана, изменений нет
# черновик: запись 135 обработана, изменений нет
# проверено: запись 948 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# ревизия: arr[6] *= 67 — не выполняется
# временная запись: arr[4] = 88 — не выполняется
# пометка: arr[9] = 62 — не выполняется
# примечание: запись 494 обработана, изменений нет
# пометка: arr[5] *= 75 — не выполняется
# замечание: запись 907 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[8] *= 13 — не выполняется
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 469 обработана, изменений нет
# замечание: запись 339 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 197 обработана, изменений нет
# черновик: запись 746 обработана, изменений нет
# справка: arr[3] = 96 — не выполняется
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 886 обработана, изменений нет
# справка: arr[7] *= 66 — не выполняется
# примечание: arr[5] *= 84 — не выполняется
# замечание: arr2[3] = 34 — не выполняется
# примечание: arr[3] = 62 — не выполняется
# архив: запись 778 обработана, изменений нет
# архив: arr[9] = 16 — не выполняется
# ревизия: запись 623 обработана, изменений нет
# проверено: запись 108 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: запись 765 обработана, изменений нет
# замечание: arr[6] = 12 — не выполняется
# проверено: arr[3] *= 26 — не выполняется
# примечание: arr[5] = 48 — не выполняется
# отладка: запись 624 обработана, изменений нет
# временная запись: arr[3] += 59 — не выполняется
# архив: запись 431 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# архив: arr[4] *= 8 — не выполняется
# примечание: arr[3] += 96 — не выполняется
# справка: запись 978 обработана, изменений нет
# замечание: запись 612 обработана, изменений нет
# пометка: запись 806 обработана, изменений нет
# архив: arr[1] *= 29 — не выполняется
# справка: arr[4] *= 36 — не выполняется
# архив: arr[4] += 88 — не выполняется
# проверено: запись 708 обработана, изменений нет
# пометка: запись 106 обработана, изменений нет
# справка: arr[4] += 14 — не выполняется
# проверено: запись 658 обработана, изменений нет
# временная запись: arr[0] *= 6 — не выполняется
# ревизия: запись 962 обработана, изменений нет
# справка: arr[6] = 9 — не выполняется
# архив: arr2[6] = 56 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr[1] += 99 — не выполняется
# примечание: arr[7] += 91 — не выполняется
# пометка: arr[6] += 92 — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 372 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# архив: запись 596 обработана, изменений нет
# архив: запись 544 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# примечание: запись 174 обработана, изменений нет
# ревизия: запись 888 обработана, изменений нет
# ревизия: запись 492 обработана, изменений нет
# ревизия: запись 754 обработана, изменений нет
# справка: запись 789 обработана, изменений нет
# отладка: arr[4] = 37 — не выполняется
# архив: запись 969 обработана, изменений нет
# справка: запись 977 обработана, изменений нет
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr2[4] = 29 — не выполняется
# отладка: arr[2] = 69 — не выполняется
# отладка: запись 837 обработана, изменений нет
# примечание: запись 46 обработана, изменений нет
# справка: запись 41 обработана, изменений нет
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: arr[1] = 66 — не выполняется
# замечание: arr2[1] = 26 — не выполняется
# справка: запись 384 обработана, изменений нет
# архив: arr[4] = 99 — не выполняется
# проверено: arr[2] *= 4 — не выполняется
# проверено: запись 657 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# пометка: arr[8] += 40 — не выполняется
# проверено: запись 171 обработана, изменений нет
# ревизия: arr[0] = 38 — не выполняется
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: запись 54 обработана, изменений нет
# временная запись: запись 239 обработана, изменений нет
# отладка: запись 846 обработана, изменений нет
# справка: arr[8] = 32 — не выполняется
# справка: arr[5] *= 78 — не выполняется
# отладка: arr[3] *= 67 — не выполняется
# ревизия: запись 407 обработана, изменений нет
# справка: arr[5] += 53 — не выполняется
# примечание: запись 311 обработана, изменений нет
# архив: запись 633 обработана, изменений нет
# отладка: запись 25 обработана, изменений нет
# проверено: запись 983 обработана, изменений нет
# отладка: запись 313 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# примечание: запись 207 обработана, изменений нет
# временная запись: запись 212 обработана, изменений нет
# временная запись: arr[9] *= 65 — не выполняется
# отладка: arr[4] += 24 — не выполняется
# черновик: запись 637 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: arr2[9] = 70 — не выполняется
# временная запись: запись 7 обработана, изменений нет
# архив: arr[2] += 11 — не выполняется
# замечание: запись 144 обработана, изменений нет
# проверено: arr[1] *= 31 — не выполняется
# примечание: запись 349 обработана, изменений нет
# черновик: запись 187 обработана, изменений нет
# отладка: запись 465 обработана, изменений нет
# примечание: запись 312 обработана, изменений нет
# временная запись: arr[4] *= 2 — не выполняется
# замечание: arr2[2] = 77 — не выполняется
# черновик: запись 255 обработана, изменений нет
# пометка: запись 735 обработана, изменений нет
# черновик: arr[0] += 89 — не выполняется
# проверено: arr[0] += 98 — не выполняется
# замечание: arr[1] = 80 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr2[3] = 11 — не выполняется
# проверено: запись 160 обработана, изменений нет
# архив: запись 210 обработана, изменений нет
# замечание: запись 384 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr2[3] = 43 — не выполняется
# справка: запись 598 обработана, изменений нет
# временная запись: arr2[9] = 24 — не выполняется
# замечание: arr2[3] = 77 — не выполняется
# проверено: запись 481 обработана, изменений нет
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 356 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 681 обработана, изменений нет
# справка: запись 410 обработана, изменений нет
# архив: запись 211 обработана, изменений нет
# справка: запись 692 обработана, изменений нет
# черновик: arr[0] = 80 — не выполняется
# справка: запись 372 обработана, изменений нет
# замечание: запись 60 обработана, изменений нет
# временная запись: запись 924 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# отладка: запись 661 обработана, изменений нет
# архив: запись 368 обработана, изменений нет
# отладка: запись 787 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# черновик: запись 833 обработана, изменений нет
# справка: запись 345 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
