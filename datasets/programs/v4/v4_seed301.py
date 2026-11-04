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
arr[4], arr[1] = arr[1], arr[4]
arr[8] += 7
arr2[8] = 3
arr[4] += 52
arr[7] *= 40
arr2[0] = 56
arr[7] = 13
arr[2] *= 39
"""

TRAP_0 = "arr[9] = 124"
TRAP_1 = "arr[9] = 424"
TRAP_2 = "arr[0] = 173"
TRAP_3 = "arr[5] = 268"
TRAP_4 = "arr[6] = 189"
TRAP_5 = "arr[0] = 562"
TRAP_6 = "arr[4] = 869"
TRAP_7 = "arr[6] = 885"
TRAP_8 = "arr[1] = 799"
TRAP_9 = "arr[0] = 972"
TRAP_10 = "arr[1] = 390"
TRAP_11 = "arr[6] = 868"
TRAP_12 = "arr[1] = 682"
TRAP_13 = "arr[4] = 686"
TRAP_14 = "arr[3] = 386"
TRAP_15 = "arr[8] = 529"
TRAP_16 = "arr[4] = 767"
TRAP_17 = "arr[2] = 692"
TRAP_18 = "arr[2] = 986"
TRAP_19 = "arr[6] = 890"
TRAP_20 = "arr[6] = 345"
TRAP_21 = "arr[1] = 574"
TRAP_22 = "arr[1] = 217"
TRAP_23 = "arr[9] = 843"
TRAP_24 = "arr[3] = 141"
TRAP_25 = "arr[4] = 390"
TRAP_26 = "arr[4] = 834"
TRAP_27 = "arr[9] = 818"
TRAP_28 = "arr[4] = 131"
TRAP_29 = "arr[9] = 519"
TRAP_30 = "arr[8] = 441"
TRAP_31 = "arr[6] = 824"
TRAP_32 = "arr[2] = 430"
TRAP_33 = "arr[4] = 264"
TRAP_34 = "arr[5] = 466"
TRAP_35 = "arr[2] = 424"
TRAP_36 = "arr[7] = 268"
TRAP_37 = "arr[7] = 230"
TRAP_38 = "arr[3] = 493"
TRAP_39 = "arr[8] = 960"
TRAP_40 = "arr[1] = 785"
TRAP_41 = "arr[9] = 160"
TRAP_42 = "arr[2] = 925"
TRAP_43 = "arr[0] = 677"
TRAP_44 = "arr[6] = 649"
TRAP_45 = "arr[3] = 662"
TRAP_46 = "arr[4] = 543"
TRAP_47 = "arr[8] = 866"
TRAP_48 = "arr[5] = 506"
TRAP_49 = "arr[3] = 449"
TRAP_50 = "arr[8] = 752"
TRAP_51 = "arr[2] = 591"
TRAP_52 = "arr[5] = 614"
TRAP_53 = "arr[6] = 886"
TRAP_54 = "arr[1] = 626"
TRAP_55 = "arr[7] = 523"
TRAP_56 = "arr[0] = 194"
TRAP_57 = "arr[8] = 900"
TRAP_58 = "arr[6] = 385"
TRAP_59 = "arr[9] = 209"
TRAP_60 = "arr[8] = 704"
TRAP_61 = "arr[0] = 922"
TRAP_62 = "arr[3] = 907"
TRAP_63 = "arr[4] = 228"
TRAP_64 = "arr[9] = 569"
TRAP_65 = "arr[6] = 510"
TRAP_66 = "arr[5] = 793"
TRAP_67 = "arr[0] = 465"
TRAP_68 = "arr[1] = 292"
TRAP_69 = "arr[3] = 864"
TRAP_70 = "arr[5] = 240"
TRAP_71 = "arr[5] = 688"
TRAP_72 = "arr[2] = 873"
TRAP_73 = "arr[0] = 829"
TRAP_74 = "arr[4] = 129"
TRAP_75 = "arr[4] = 984"
TRAP_76 = "arr[3] = 421"
TRAP_77 = "arr[4] = 788"
TRAP_78 = "arr[2] = 159"
TRAP_79 = "arr[3] = 590"
TRAP_80 = "arr[1] = 588"
TRAP_81 = "arr[0] = 627"
TRAP_82 = "arr[7] = 619"
TRAP_83 = "arr[2] = 415"
TRAP_84 = "arr[7] = 306"
TRAP_85 = "arr[3] = 196"
TRAP_86 = "arr[9] = 331"
TRAP_87 = "arr[4] = 990"
TRAP_88 = "arr[9] = 680"
TRAP_89 = "arr[3] = 508"
TRAP_90 = "arr[0] = 481"
TRAP_91 = "arr[8] = 770"
TRAP_92 = "arr[9] = 614"
TRAP_93 = "arr[2] = 127"
TRAP_94 = "arr[1] = 628"
TRAP_95 = "arr[7] = 727"
TRAP_96 = "arr[4] = 124"
TRAP_97 = "arr[4] = 907"
TRAP_98 = "arr[7] = 411"
TRAP_99 = "arr[9] = 433"
TRAP_100 = "arr[4] = 685"
TRAP_101 = "arr[1] = 717"
TRAP_102 = "arr[2] = 973"
TRAP_103 = "arr[2] = 431"
TRAP_104 = "arr[5] = 929"
TRAP_105 = "arr[6] = 957"
TRAP_106 = "arr[5] = 667"
TRAP_107 = "arr[9] = 601"
TRAP_108 = "arr[0] = 710"
TRAP_109 = "arr[7] = 697"
TRAP_110 = "arr[0] = 833"
TRAP_111 = "arr[0] = 772"
TRAP_112 = "arr[2] = 645"
TRAP_113 = "arr[6] = 609"
TRAP_114 = "arr[2] = 313"
TRAP_115 = "arr[3] = 733"
TRAP_116 = "arr[5] = 648"
TRAP_117 = "arr[8] = 624"
TRAP_118 = "arr[2] = 226"
TRAP_119 = "arr[1] = 929"
TRAP_120 = "arr[6] = 565"
TRAP_121 = "arr[5] = 257"
TRAP_122 = "arr[4] = 995"
TRAP_123 = "arr[1] = 475"
TRAP_124 = "arr[8] = 472"
TRAP_125 = "arr[5] = 991"
TRAP_126 = "arr[3] = 466"
TRAP_127 = "arr[4] = 767"
TRAP_128 = "arr[1] = 385"
TRAP_129 = "arr[2] = 139"
TRAP_130 = "arr[8] = 796"
TRAP_131 = "arr[7] = 396"
TRAP_132 = "arr[4] = 308"
TRAP_133 = "arr[6] = 560"
TRAP_134 = "arr[0] = 229"
TRAP_135 = "arr[1] = 827"
TRAP_136 = "arr[6] = 914"
TRAP_137 = "arr[5] = 512"
TRAP_138 = "arr[4] = 647"
TRAP_139 = "arr[9] = 286"
TRAP_140 = "arr[0] = 853"
TRAP_141 = "arr[0] = 274"
TRAP_142 = "arr[8] = 869"
TRAP_143 = "arr[8] = 848"
TRAP_144 = "arr[0] = 731"
TRAP_145 = "arr[4] = 688"
TRAP_146 = "arr[2] = 870"
TRAP_147 = "arr[2] = 285"
TRAP_148 = "arr[9] = 771"
TRAP_149 = "arr[6] = 527"

arr = [13, 21, 26, 30, 16, 18, 15, 21, 8, 22]

copy_0 = arr[9]
note_1 = str(arr[8]) + str(arr[3])
note_2 = str(arr[7]) + str(arr[4])
tmp_3 = arr[9] + 19
code_4 = re.sub(r'[0-9]', '#', str(arr[4]))
code_5 = re.sub(r'[0-9]', '#', str(arr[1]))
code_6 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_7 = arr[6] + 20
note_8 = str(arr[0]) + str(arr[4])
code_9 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_10 = arr[3] + 18
code_11 = re.sub(r'[0-9]', '#', str(arr[9]))
code_12 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_13 = arr[2] + 2
tmp_14 = arr[6] + 2
tmp_15 = arr[7] + 11
code_16 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_17 = arr[2] + 13
code_18 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_19 = arr[3]
tmp_20 = arr[5] + 37
copy_21 = arr[2]
tmp_22 = arr[4] + 14
copy_23 = arr[8]
copy_24 = arr[8]
code_25 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_26 = arr[7] + 38
note_27 = str(arr[8]) + str(arr[0])
tmp_28 = arr[3] + 43
note_29 = str(arr[8]) + str(arr[6])
note_30 = str(arr[2]) + str(arr[9])
tmp_31 = arr[9] + 33
tmp_32 = arr[6] + 28
code_33 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_34 = arr[3]
note_35 = str(arr[2]) + str(arr[9])
copy_36 = arr[5]
note_37 = str(arr[8]) + str(arr[1])
code_38 = re.sub(r'[0-9]', '#', str(arr[7]))
note_39 = str(arr[6]) + str(arr[9])
copy_40 = arr[6]
tmp_41 = arr[8] + 44
tmp_42 = arr[0] + 17
note_43 = str(arr[8]) + str(arr[3])
code_44 = re.sub(r'[0-9]', '#', str(arr[4]))
label_45 = "запись 45 не применялась"
label_46 = "запись 46 не применялась"
copy_47 = arr[8]
label_48 = "запись 48 не применялась"
note_49 = str(arr[3]) + str(arr[4])
code_50 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_51 = arr[8] + 28
code_52 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_53 = arr[3] + 50
label_54 = "запись 54 не применялась"
note_55 = str(arr[7]) + str(arr[7])
tmp_56 = arr[7] + 47
label_57 = "запись 57 не применялась"
tmp_58 = arr[2] + 48
tmp_59 = arr[7] + 2
note_60 = str(arr[2]) + str(arr[2])
code_61 = re.sub(r'[0-9]', '#', str(arr[1]))
code_62 = re.sub(r'[0-9]', '#', str(arr[8]))
label_63 = "запись 63 не применялась"
code_64 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_65 = arr[2] + 40
tmp_66 = arr[0] + 41
copy_67 = arr[8]
copy_68 = arr[5]
code_69 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_70 = arr[9]
code_71 = re.sub(r'[0-9]', '#', str(arr[1]))
note_72 = str(arr[6]) + str(arr[3])
code_73 = re.sub(r'[0-9]', '#', str(arr[0]))
note_74 = str(arr[9]) + str(arr[2])
tmp_75 = arr[7] + 35
label_76 = "запись 76 не применялась"
label_77 = "запись 77 не применялась"
code_78 = re.sub(r'[0-9]', '#', str(arr[1]))
note_79 = str(arr[0]) + str(arr[9])
code_80 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_81 = arr[8] + 7
copy_82 = arr[5]
note_83 = str(arr[8]) + str(arr[2])
code_84 = re.sub(r'[0-9]', '#', str(arr[3]))
note_85 = str(arr[3]) + str(arr[0])
code_86 = re.sub(r'[0-9]', '#', str(arr[3]))
label_87 = "запись 87 не применялась"
note_88 = str(arr[7]) + str(arr[5])
code_89 = re.sub(r'[0-9]', '#', str(arr[6]))
note_90 = str(arr[7]) + str(arr[1])
copy_91 = arr[5]
note_92 = str(arr[0]) + str(arr[2])
note_93 = str(arr[6]) + str(arr[0])
code_94 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_95 = arr[8]
copy_96 = arr[0]
note_97 = str(arr[5]) + str(arr[4])
copy_98 = arr[6]
label_99 = "запись 99 не применялась"
copy_100 = arr[8]
tmp_101 = arr[1] + 25
note_102 = str(arr[6]) + str(arr[1])
tmp_103 = arr[0] + 18
tmp_104 = arr[5] + 49
tmp_105 = arr[9] + 20
tmp_106 = arr[6] + 6
note_107 = str(arr[4]) + str(arr[2])
note_108 = str(arr[9]) + str(arr[9])
code_109 = re.sub(r'[0-9]', '#', str(arr[0]))
code_110 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_111 = arr[0] + 7
tmp_112 = arr[2] + 4
note_113 = str(arr[2]) + str(arr[6])
tmp_114 = arr[0] + 7
tmp_115 = arr[0] + 24
code_116 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_117 = arr[3] + 36
tmp_118 = arr[3] + 43
tmp_119 = arr[4] + 43
tmp_120 = arr[2] + 18
code_121 = re.sub(r'[0-9]', '#', str(arr[7]))
code_122 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_123 = arr[6] + 49
tmp_124 = arr[2] + 49
copy_125 = arr[3]
note_126 = str(arr[7]) + str(arr[9])
tmp_127 = arr[3] + 33
tmp_128 = arr[0] + 44
tmp_129 = arr[8] + 34
tmp_130 = arr[1] + 8
label_131 = "запись 131 не применялась"
tmp_132 = arr[1] + 23
copy_133 = arr[2]
code_134 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_135 = arr[9] + 16
tmp_136 = arr[6] + 26
note_137 = str(arr[8]) + str(arr[9])
label_138 = "запись 138 не применялась"
copy_139 = arr[8]
code_140 = re.sub(r'[0-9]', '#', str(arr[0]))
note_141 = str(arr[4]) + str(arr[4])
note_142 = str(arr[1]) + str(arr[0])
copy_143 = arr[7]
code_144 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_145 = arr[9] + 4
note_146 = str(arr[3]) + str(arr[7])
tmp_147 = arr[7] + 25
copy_148 = arr[3]
note_149 = str(arr[7]) + str(arr[8])
note_150 = str(arr[2]) + str(arr[7])
note_151 = str(arr[3]) + str(arr[2])
note_152 = str(arr[1]) + str(arr[0])
code_153 = re.sub(r'[0-9]', '#', str(arr[8]))
note_154 = str(arr[4]) + str(arr[0])
copy_155 = arr[1]
copy_156 = arr[3]
label_157 = "запись 157 не применялась"
copy_158 = arr[9]
tmp_159 = arr[6] + 25
note_160 = str(arr[9]) + str(arr[8])
copy_161 = arr[6]
label_162 = "запись 162 не применялась"
tmp_163 = arr[5] + 45
note_164 = str(arr[3]) + str(arr[2])
note_165 = str(arr[9]) + str(arr[7])
tmp_166 = arr[2] + 3
code_167 = re.sub(r'[0-9]', '#', str(arr[3]))
note_168 = str(arr[6]) + str(arr[7])
note_169 = str(arr[2]) + str(arr[2])
note_170 = str(arr[1]) + str(arr[5])
note_171 = str(arr[9]) + str(arr[1])
code_172 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_173 = arr[6] + 15
copy_174 = arr[1]
tmp_175 = arr[1] + 49
code_176 = re.sub(r'[0-9]', '#', str(arr[9]))
code_177 = re.sub(r'[0-9]', '#', str(arr[4]))
code_178 = re.sub(r'[0-9]', '#', str(arr[4]))
note_179 = str(arr[8]) + str(arr[4])
copy_180 = arr[8]
code_181 = re.sub(r'[0-9]', '#', str(arr[0]))
code_182 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_183 = arr[0] + 13
tmp_184 = arr[6] + 23
note_185 = str(arr[4]) + str(arr[9])
note_186 = str(arr[8]) + str(arr[1])
note_187 = str(arr[1]) + str(arr[1])
tmp_188 = arr[3] + 2
tmp_189 = arr[1] + 41
code_190 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_191 = arr[3]
code_192 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_193 = arr[7]
tmp_194 = arr[6] + 43
code_195 = re.sub(r'[0-9]', '#', str(arr[3]))
note_196 = str(arr[9]) + str(arr[0])
code_197 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_198 = arr[9]
tmp_199 = arr[8] + 9
note_200 = str(arr[7]) + str(arr[8])
note_201 = str(arr[7]) + str(arr[1])
note_202 = str(arr[4]) + str(arr[4])
code_203 = re.sub(r'[0-9]', '#', str(arr[0]))
note_204 = str(arr[2]) + str(arr[5])
note_205 = str(arr[5]) + str(arr[6])
note_206 = str(arr[1]) + str(arr[5])
tmp_207 = arr[8] + 31
note_208 = str(arr[2]) + str(arr[1])
code_209 = re.sub(r'[0-9]', '#', str(arr[4]))
note_210 = str(arr[8]) + str(arr[4])
tmp_211 = arr[0] + 13
code_212 = re.sub(r'[0-9]', '#', str(arr[8]))
code_213 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_214 = arr[4] + 31
copy_215 = arr[1]
note_216 = str(arr[7]) + str(arr[5])
tmp_217 = arr[0] + 3
tmp_218 = arr[9] + 7
copy_219 = arr[4]
code_220 = re.sub(r'[0-9]', '#', str(arr[8]))
label_221 = "запись 221 не применялась"
note_222 = str(arr[7]) + str(arr[6])
tmp_223 = arr[6] + 23
tmp_224 = arr[5] + 32
tmp_225 = arr[2] + 41
copy_226 = arr[8]
tmp_227 = arr[6] + 34
label_228 = "запись 228 не применялась"
tmp_229 = arr[9] + 38
label_230 = "запись 230 не применялась"
copy_231 = arr[2]
code_232 = re.sub(r'[0-9]', '#', str(arr[9]))
code_233 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_234 = arr[8]
code_235 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_236 = arr[3]
copy_237 = arr[6]
tmp_238 = arr[1] + 16
tmp_239 = arr[7] + 4
note_240 = str(arr[1]) + str(arr[2])
code_241 = re.sub(r'[0-9]', '#', str(arr[6]))
note_242 = str(arr[4]) + str(arr[1])
code_243 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_244 = arr[4]
code_245 = re.sub(r'[0-9]', '#', str(arr[8]))
code_246 = re.sub(r'[0-9]', '#', str(arr[4]))
code_247 = re.sub(r'[0-9]', '#', str(arr[8]))
label_248 = "запись 248 не применялась"
note_249 = str(arr[3]) + str(arr[6])
note_250 = str(arr[3]) + str(arr[1])
tmp_251 = arr[1] + 4
note_252 = str(arr[5]) + str(arr[1])
note_253 = str(arr[9]) + str(arr[1])
tmp_254 = arr[1] + 39
tmp_255 = arr[1] + 36
note_256 = str(arr[1]) + str(arr[3])
note_257 = str(arr[1]) + str(arr[5])
code_258 = re.sub(r'[0-9]', '#', str(arr[1]))
note_259 = str(arr[7]) + str(arr[9])
tmp_260 = arr[6] + 48
copy_261 = arr[2]
code_262 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_263 = arr[4] + 33
code_264 = re.sub(r'[0-9]', '#', str(arr[1]))
label_265 = "запись 265 не применялась"
tmp_266 = arr[8] + 49
code_267 = re.sub(r'[0-9]', '#', str(arr[3]))
code_268 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_269 = arr[2]
tmp_270 = arr[2] + 17
note_271 = str(arr[9]) + str(arr[8])
code_272 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_273 = arr[7]
note_274 = str(arr[0]) + str(arr[3])
note_275 = str(arr[6]) + str(arr[9])
tmp_276 = arr[5] + 39
code_277 = re.sub(r'[0-9]', '#', str(arr[9]))
note_278 = str(arr[0]) + str(arr[4])
copy_279 = arr[3]
tmp_280 = arr[2] + 9
tmp_281 = arr[3] + 44
tmp_282 = arr[8] + 34
code_283 = re.sub(r'[0-9]', '#', str(arr[8]))
label_284 = "запись 284 не применялась"
tmp_285 = arr[1] + 31
tmp_286 = arr[9] + 49
tmp_287 = arr[0] + 5
tmp_288 = arr[2] + 30
note_289 = str(arr[2]) + str(arr[6])
code_290 = re.sub(r'[0-9]', '#', str(arr[8]))
code_291 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_292 = arr[6] + 44
code_293 = re.sub(r'[0-9]', '#', str(arr[3]))
note_294 = str(arr[5]) + str(arr[7])
note_295 = str(arr[5]) + str(arr[4])
note_296 = str(arr[0]) + str(arr[8])
note_297 = str(arr[5]) + str(arr[6])
tmp_298 = arr[7] + 31
copy_299 = arr[6]
copy_300 = arr[4]
code_301 = re.sub(r'[0-9]', '#', str(arr[1]))
code_302 = re.sub(r'[0-9]', '#', str(arr[4]))
code_303 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_304 = arr[1] + 38
tmp_305 = arr[5] + 47
note_306 = str(arr[8]) + str(arr[7])
copy_307 = arr[4]
code_308 = re.sub(r'[0-9]', '#', str(arr[2]))
code_309 = re.sub(r'[0-9]', '#', str(arr[3]))
label_310 = "запись 310 не применялась"
note_311 = str(arr[4]) + str(arr[0])
label_312 = "запись 312 не применялась"
tmp_313 = arr[2] + 43
tmp_314 = arr[5] + 39
tmp_315 = arr[5] + 22
note_316 = str(arr[5]) + str(arr[9])
tmp_317 = arr[0] + 9
code_318 = re.sub(r'[0-9]', '#', str(arr[5]))
code_319 = re.sub(r'[0-9]', '#', str(arr[3]))
label_320 = "запись 320 не применялась"
tmp_321 = arr[2] + 25
label_322 = "запись 322 не применялась"
copy_323 = arr[0]
note_324 = str(arr[3]) + str(arr[2])
code_325 = re.sub(r'[0-9]', '#', str(arr[2]))
code_326 = re.sub(r'[0-9]', '#', str(arr[5]))
label_327 = "запись 327 не применялась"
note_328 = str(arr[7]) + str(arr[5])
tmp_329 = arr[5] + 34
tmp_330 = arr[1] + 27
note_331 = str(arr[0]) + str(arr[9])
note_332 = str(arr[5]) + str(arr[6])
tmp_333 = arr[0] + 36
tmp_334 = arr[7] + 41
tmp_335 = arr[6] + 50
code_336 = re.sub(r'[0-9]', '#', str(arr[7]))
note_337 = str(arr[2]) + str(arr[5])
code_338 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_339 = arr[6]
copy_340 = arr[1]
tmp_341 = arr[9] + 19
label_342 = "запись 342 не применялась"
code_343 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_344 = arr[9] + 35
note_345 = str(arr[3]) + str(arr[0])
note_346 = str(arr[8]) + str(arr[2])
copy_347 = arr[5]
tmp_348 = arr[0] + 37
tmp_349 = arr[5] + 43
tmp_350 = arr[9] + 30
tmp_351 = arr[4] + 28
label_352 = "запись 352 не применялась"
tmp_353 = arr[5] + 46
note_354 = str(arr[1]) + str(arr[4])
code_355 = re.sub(r'[0-9]', '#', str(arr[0]))
code_356 = re.sub(r'[0-9]', '#', str(arr[1]))
code_357 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_358 = arr[4] + 8
copy_359 = arr[5]
code_360 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_361 = arr[4] + 23
note_362 = str(arr[6]) + str(arr[8])
code_363 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_364 = arr[5] + 39
code_365 = re.sub(r'[0-9]', '#', str(arr[4]))
note_366 = str(arr[5]) + str(arr[4])
label_367 = "запись 367 не применялась"
tmp_368 = arr[2] + 23
tmp_369 = arr[4] + 43
label_370 = "запись 370 не применялась"
tmp_371 = arr[3] + 40
tmp_372 = arr[4] + 2
tmp_373 = arr[1] + 40
label_374 = "запись 374 не применялась"
tmp_375 = arr[1] + 28
tmp_376 = arr[1] + 7
tmp_377 = arr[9] + 8
note_378 = str(arr[1]) + str(arr[4])
note_379 = str(arr[0]) + str(arr[6])
note_380 = str(arr[8]) + str(arr[2])
copy_381 = arr[9]
code_382 = re.sub(r'[0-9]', '#', str(arr[3]))
note_383 = str(arr[6]) + str(arr[6])
tmp_384 = arr[3] + 38
copy_385 = arr[4]
tmp_386 = arr[4] + 13
code_387 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_388 = arr[5]
code_389 = re.sub(r'[0-9]', '#', str(arr[4]))
label_390 = "запись 390 не применялась"
tmp_391 = arr[6] + 45
code_392 = re.sub(r'[0-9]', '#', str(arr[3]))
note_393 = str(arr[4]) + str(arr[8])
tmp_394 = arr[1] + 18
note_395 = str(arr[9]) + str(arr[1])
copy_396 = arr[1]
tmp_397 = arr[4] + 20
tmp_398 = arr[6] + 8
tmp_399 = arr[1] + 17
note_400 = str(arr[9]) + str(arr[9])
label_401 = "запись 401 не применялась"
code_402 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_403 = arr[5] + 41
code_404 = re.sub(r'[0-9]', '#', str(arr[3]))
note_405 = str(arr[2]) + str(arr[8])
note_406 = str(arr[7]) + str(arr[4])
code_407 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_408 = arr[8] + 16
tmp_409 = arr[3] + 7
tmp_410 = arr[4] + 10
tmp_411 = arr[9] + 11
note_412 = str(arr[7]) + str(arr[3])
tmp_413 = arr[1] + 28
code_414 = re.sub(r'[0-9]', '#', str(arr[5]))
label_415 = "запись 415 не применялась"
note_416 = str(arr[8]) + str(arr[0])
note_417 = str(arr[3]) + str(arr[8])
note_418 = str(arr[6]) + str(arr[8])
code_419 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_420 = arr[5] + 28
note_421 = str(arr[1]) + str(arr[4])
label_422 = "запись 422 не применялась"
tmp_423 = arr[3] + 24
note_424 = str(arr[3]) + str(arr[1])
copy_425 = arr[2]
note_426 = str(arr[9]) + str(arr[1])
label_427 = "запись 427 не применялась"
note_428 = str(arr[0]) + str(arr[7])
note_429 = str(arr[3]) + str(arr[5])
code_430 = re.sub(r'[0-9]', '#', str(arr[8]))
note_431 = str(arr[7]) + str(arr[4])
note_432 = str(arr[3]) + str(arr[6])
code_433 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_434 = arr[7]
label_435 = "запись 435 не применялась"
tmp_436 = arr[8] + 36
note_437 = str(arr[0]) + str(arr[0])
code_438 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_439 = arr[9] + 4
note_440 = str(arr[9]) + str(arr[9])
copy_441 = arr[0]
copy_442 = arr[9]
code_443 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_444 = arr[3] + 36
tmp_445 = arr[5] + 33
label_446 = "запись 446 не применялась"
note_447 = str(arr[7]) + str(arr[3])
copy_448 = arr[3]
note_449 = str(arr[9]) + str(arr[4])
tmp_450 = arr[1] + 46
code_451 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_452 = arr[0] + 11
code_453 = re.sub(r'[0-9]', '#', str(arr[5]))
code_454 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_455 = arr[6] + 37
tmp_456 = arr[8] + 46
tmp_457 = arr[3] + 49
code_458 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_459 = arr[8] + 49
note_460 = str(arr[7]) + str(arr[7])
copy_461 = arr[0]
note_462 = str(arr[4]) + str(arr[9])
code_463 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_464 = arr[9]
code_465 = re.sub(r'[0-9]', '#', str(arr[4]))
code_466 = re.sub(r'[0-9]', '#', str(arr[8]))
code_467 = re.sub(r'[0-9]', '#', str(arr[1]))
note_468 = str(arr[5]) + str(arr[5])
note_469 = str(arr[5]) + str(arr[9])
note_470 = str(arr[7]) + str(arr[4])
copy_471 = arr[2]
copy_472 = arr[5]
label_473 = "запись 473 не применялась"
code_474 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_475 = arr[3]
tmp_476 = arr[9] + 47
copy_477 = arr[5]
code_478 = re.sub(r'[0-9]', '#', str(arr[2]))
note_479 = str(arr[0]) + str(arr[7])
tmp_480 = arr[8] + 23
label_481 = "запись 481 не применялась"
note_482 = str(arr[2]) + str(arr[3])
tmp_483 = arr[8] + 1
code_484 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_485 = arr[1] + 22
note_486 = str(arr[6]) + str(arr[6])
tmp_487 = arr[4] + 22
copy_488 = arr[0]
note_489 = str(arr[6]) + str(arr[5])
copy_490 = arr[6]
tmp_491 = arr[1] + 24
tmp_492 = arr[2] + 7
tmp_493 = arr[7] + 32
code_494 = re.sub(r'[0-9]', '#', str(arr[5]))
note_495 = str(arr[0]) + str(arr[6])
code_496 = re.sub(r'[0-9]', '#', str(arr[5]))
code_497 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_498 = arr[6]
note_499 = str(arr[2]) + str(arr[1])
note_500 = str(arr[2]) + str(arr[1])
tmp_501 = arr[5] + 14
tmp_502 = arr[9] + 4
note_503 = str(arr[5]) + str(arr[4])
tmp_504 = arr[1] + 45
note_505 = str(arr[1]) + str(arr[0])
tmp_506 = arr[4] + 30
code_507 = re.sub(r'[0-9]', '#', str(arr[9]))
code_508 = re.sub(r'[0-9]', '#', str(arr[2]))
code_509 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_510 = arr[2] + 28
code_511 = re.sub(r'[0-9]', '#', str(arr[2]))
note_512 = str(arr[6]) + str(arr[5])
copy_513 = arr[4]
tmp_514 = arr[4] + 42
code_515 = re.sub(r'[0-9]', '#', str(arr[1]))
note_516 = str(arr[0]) + str(arr[0])
label_517 = "запись 517 не применялась"
note_518 = str(arr[1]) + str(arr[3])
note_519 = str(arr[6]) + str(arr[8])
tmp_520 = arr[6] + 37
copy_521 = arr[1]
note_522 = str(arr[4]) + str(arr[9])
note_523 = str(arr[6]) + str(arr[5])
copy_524 = arr[5]
code_525 = re.sub(r'[0-9]', '#', str(arr[6]))
note_526 = str(arr[9]) + str(arr[1])
note_527 = str(arr[1]) + str(arr[4])
tmp_528 = arr[3] + 36
tmp_529 = arr[2] + 44
copy_530 = arr[1]
note_531 = str(arr[4]) + str(arr[2])
code_532 = re.sub(r'[0-9]', '#', str(arr[2]))
label_533 = "запись 533 не применялась"
copy_534 = arr[8]
code_535 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_536 = arr[8] + 15
note_537 = str(arr[3]) + str(arr[6])
copy_538 = arr[8]
tmp_539 = arr[7] + 39
tmp_540 = arr[5] + 16
code_541 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_542 = arr[7] + 7
label_543 = "запись 543 не применялась"
tmp_544 = arr[7] + 34
code_545 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_546 = arr[2] + 19
note_547 = str(arr[7]) + str(arr[3])
label_548 = "запись 548 не применялась"
note_549 = str(arr[8]) + str(arr[1])
code_550 = re.sub(r'[0-9]', '#', str(arr[6]))
label_551 = "запись 551 не применялась"
label_552 = "запись 552 не применялась"
tmp_553 = arr[2] + 31
tmp_554 = arr[8] + 20
tmp_555 = arr[3] + 50
note_556 = str(arr[3]) + str(arr[2])
tmp_557 = arr[9] + 41
tmp_558 = arr[3] + 16
code_559 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_560 = arr[8] + 46
note_561 = str(arr[8]) + str(arr[4])
code_562 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_563 = arr[2] + 7
copy_564 = arr[7]
copy_565 = arr[0]
code_566 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_567 = arr[4] + 9
copy_568 = arr[8]
note_569 = str(arr[6]) + str(arr[3])
tmp_570 = arr[6] + 50
note_571 = str(arr[9]) + str(arr[7])
copy_572 = arr[5]
label_573 = "запись 573 не применялась"
code_574 = re.sub(r'[0-9]', '#', str(arr[2]))
code_575 = re.sub(r'[0-9]', '#', str(arr[4]))
note_576 = str(arr[6]) + str(arr[1])
tmp_577 = arr[6] + 4
tmp_578 = arr[8] + 43
tmp_579 = arr[1] + 22
copy_580 = arr[1]
tmp_581 = arr[4] + 42
label_582 = "запись 582 не применялась"
tmp_583 = arr[4] + 31
note_584 = str(arr[7]) + str(arr[6])
tmp_585 = arr[8] + 47
tmp_586 = arr[0] + 15
label_587 = "запись 587 не применялась"
code_588 = re.sub(r'[0-9]', '#', str(arr[8]))
note_589 = str(arr[8]) + str(arr[1])
copy_590 = arr[8]
code_591 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_592 = arr[1] + 13
copy_593 = arr[7]
note_594 = str(arr[3]) + str(arr[5])
tmp_595 = arr[6] + 15
copy_596 = arr[9]
copy_597 = arr[0]
note_598 = str(arr[2]) + str(arr[5])
note_599 = str(arr[3]) + str(arr[4])
code_600 = re.sub(r'[0-9]', '#', str(arr[8]))
code_601 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_602 = arr[6] + 5
note_603 = str(arr[9]) + str(arr[5])
copy_604 = arr[2]
code_605 = re.sub(r'[0-9]', '#', str(arr[5]))
note_606 = str(arr[2]) + str(arr[1])
label_607 = "запись 607 не применялась"
note_608 = str(arr[5]) + str(arr[3])
label_609 = "запись 609 не применялась"
copy_610 = arr[0]
note_611 = str(arr[5]) + str(arr[5])
tmp_612 = arr[6] + 7
note_613 = str(arr[3]) + str(arr[8])
note_614 = str(arr[2]) + str(arr[6])
code_615 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_616 = arr[5]
code_617 = re.sub(r'[0-9]', '#', str(arr[0]))
note_618 = str(arr[3]) + str(arr[9])
note_619 = str(arr[9]) + str(arr[2])
code_620 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_621 = arr[2]
code_622 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_623 = arr[7]
copy_624 = arr[7]
code_625 = re.sub(r'[0-9]', '#', str(arr[0]))
label_626 = "запись 626 не применялась"
tmp_627 = arr[8] + 12
copy_628 = arr[8]
note_629 = str(arr[2]) + str(arr[4])
code_630 = re.sub(r'[0-9]', '#', str(arr[5]))
code_631 = re.sub(r'[0-9]', '#', str(arr[6]))
note_632 = str(arr[4]) + str(arr[4])
tmp_633 = arr[4] + 32
tmp_634 = arr[1] + 18
note_635 = str(arr[7]) + str(arr[0])
label_636 = "запись 636 не применялась"
note_637 = str(arr[9]) + str(arr[5])
note_638 = str(arr[3]) + str(arr[1])
code_639 = re.sub(r'[0-9]', '#', str(arr[2]))
label_640 = "запись 640 не применялась"
note_641 = str(arr[6]) + str(arr[6])
copy_642 = arr[5]
code_643 = re.sub(r'[0-9]', '#', str(arr[0]))
note_644 = str(arr[6]) + str(arr[9])
tmp_645 = arr[8] + 21
tmp_646 = arr[7] + 14
copy_647 = arr[0]
tmp_648 = arr[8] + 21
code_649 = re.sub(r'[0-9]', '#', str(arr[8]))
label_650 = "запись 650 не применялась"
label_651 = "запись 651 не применялась"
tmp_652 = arr[8] + 7
note_653 = str(arr[7]) + str(arr[6])
tmp_654 = arr[8] + 10
copy_655 = arr[3]
note_656 = str(arr[7]) + str(arr[5])
label_657 = "запись 657 не применялась"
tmp_658 = arr[8] + 30
tmp_659 = arr[0] + 3
tmp_660 = arr[2] + 23
note_661 = str(arr[1]) + str(arr[5])
note_662 = str(arr[5]) + str(arr[0])
tmp_663 = arr[9] + 41
label_664 = "запись 664 не применялась"
tmp_665 = arr[4] + 11
note_666 = str(arr[0]) + str(arr[4])
copy_667 = arr[4]
code_668 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_669 = arr[2] + 50
tmp_670 = arr[8] + 34
code_671 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_672 = arr[9] + 26
copy_673 = arr[0]
note_674 = str(arr[3]) + str(arr[1])
tmp_675 = arr[4] + 5
code_676 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_677 = arr[2] + 38
label_678 = "запись 678 не применялась"
note_679 = str(arr[7]) + str(arr[6])
note_680 = str(arr[6]) + str(arr[5])
tmp_681 = arr[5] + 9
tmp_682 = arr[5] + 4
label_683 = "запись 683 не применялась"
note_684 = str(arr[2]) + str(arr[3])
note_685 = str(arr[0]) + str(arr[8])
note_686 = str(arr[0]) + str(arr[2])
tmp_687 = arr[1] + 9
code_688 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_689 = arr[9] + 3
label_690 = "запись 690 не применялась"
tmp_691 = arr[1] + 10
note_692 = str(arr[1]) + str(arr[5])
tmp_693 = arr[4] + 48
label_694 = "запись 694 не применялась"
tmp_695 = arr[3] + 50
label_696 = "запись 696 не применялась"
tmp_697 = arr[3] + 23
tmp_698 = arr[1] + 8
note_699 = str(arr[3]) + str(arr[5])
tmp_700 = arr[9] + 1
code_701 = re.sub(r'[0-9]', '#', str(arr[0]))
code_702 = re.sub(r'[0-9]', '#', str(arr[4]))
note_703 = str(arr[3]) + str(arr[1])
note_704 = str(arr[7]) + str(arr[2])
note_705 = str(arr[9]) + str(arr[3])
copy_706 = arr[2]
code_707 = re.sub(r'[0-9]', '#', str(arr[6]))
code_708 = re.sub(r'[0-9]', '#', str(arr[5]))
note_709 = str(arr[1]) + str(arr[2])
copy_710 = arr[8]
copy_711 = arr[5]
copy_712 = arr[3]
tmp_713 = arr[9] + 47
note_714 = str(arr[9]) + str(arr[7])
note_715 = str(arr[3]) + str(arr[9])
note_716 = str(arr[2]) + str(arr[5])
code_717 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_718 = arr[6]
copy_719 = arr[0]
label_720 = "запись 720 не применялась"
code_721 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_722 = arr[1] + 30
code_723 = re.sub(r'[0-9]', '#', str(arr[7]))
label_724 = "запись 724 не применялась"
tmp_725 = arr[3] + 23
copy_726 = arr[8]
code_727 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_728 = arr[8] + 38
note_729 = str(arr[4]) + str(arr[0])
note_730 = str(arr[2]) + str(arr[6])
note_731 = str(arr[1]) + str(arr[4])
tmp_732 = arr[1] + 8
code_733 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_734 = arr[7] + 1
label_735 = "запись 735 не применялась"
note_736 = str(arr[4]) + str(arr[4])
copy_737 = arr[2]
note_738 = str(arr[5]) + str(arr[0])
note_739 = str(arr[1]) + str(arr[3])
tmp_740 = arr[1] + 45
copy_741 = arr[3]
tmp_742 = arr[2] + 4
tmp_743 = arr[7] + 39
tmp_744 = arr[3] + 8
label_745 = "запись 745 не применялась"
note_746 = str(arr[7]) + str(arr[2])
tmp_747 = arr[4] + 43
copy_748 = arr[5]
code_749 = re.sub(r'[0-9]', '#', str(arr[7]))
code_750 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_751 = arr[8]
tmp_752 = arr[4] + 1
tmp_753 = arr[0] + 36
tmp_754 = arr[0] + 38
code_755 = re.sub(r'[0-9]', '#', str(arr[7]))
note_756 = str(arr[2]) + str(arr[5])
note_757 = str(arr[2]) + str(arr[0])
note_758 = str(arr[7]) + str(arr[3])
note_759 = str(arr[2]) + str(arr[0])
tmp_760 = arr[8] + 24
note_761 = str(arr[8]) + str(arr[7])
code_762 = re.sub(r'[0-9]', '#', str(arr[7]))
note_763 = str(arr[2]) + str(arr[5])
note_764 = str(arr[3]) + str(arr[7])
copy_765 = arr[9]
code_766 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_767 = arr[4] + 36
copy_768 = arr[5]
tmp_769 = arr[7] + 14
tmp_770 = arr[7] + 16
tmp_771 = arr[3] + 12
code_772 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_773 = arr[3] + 23
note_774 = str(arr[9]) + str(arr[8])
copy_775 = arr[9]
note_776 = str(arr[0]) + str(arr[7])
copy_777 = arr[9]
note_778 = str(arr[2]) + str(arr[4])
note_779 = str(arr[2]) + str(arr[0])
note_780 = str(arr[0]) + str(arr[3])
copy_781 = arr[1]
tmp_782 = arr[9] + 11
note_783 = str(arr[2]) + str(arr[4])
copy_784 = arr[1]
tmp_785 = arr[4] + 9
tmp_786 = arr[5] + 18
code_787 = re.sub(r'[0-9]', '#', str(arr[0]))
note_788 = str(arr[3]) + str(arr[3])
code_789 = re.sub(r'[0-9]', '#', str(arr[8]))
code_790 = re.sub(r'[0-9]', '#', str(arr[5]))
note_791 = str(arr[3]) + str(arr[3])
label_792 = "запись 792 не применялась"
label_793 = "запись 793 не применялась"
tmp_794 = arr[3] + 44
copy_795 = arr[5]
note_796 = str(arr[4]) + str(arr[6])
code_797 = re.sub(r'[0-9]', '#', str(arr[2]))
code_798 = re.sub(r'[0-9]', '#', str(arr[0]))
label_799 = "запись 799 не применялась"

arr.reverse()
# ревизия: arr[8] = 87 — не выполняется
# замечание: arr[0] *= 65 — не выполняется
# проверено: запись 416 обработана, изменений нет
# справка: запись 645 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# замечание: запись 486 обработана, изменений нет
# замечание: arr[1] *= 89 — не выполняется
# проверено: запись 749 обработана, изменений нет
# замечание: запись 262 обработана, изменений нет
# архив: запись 494 обработана, изменений нет
# замечание: запись 374 обработана, изменений нет
# пометка: arr[1] += 19 — не выполняется
# временная запись: запись 395 обработана, изменений нет
# проверено: запись 697 обработана, изменений нет
# пометка: arr[9] = 68 — не выполняется
# пометка: запись 508 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 102 обработана, изменений нет
# черновик: arr[5] = 75 — не выполняется
# пометка: arr[5] += 7 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr2[9] = 27 — не выполняется
# отладка: arr[3] += 89 — не выполняется
# справка: arr[8] *= 47 — не выполняется
# отладка: arr[5] *= 85 — не выполняется
# замечание: arr[2] += 85 — не выполняется
# замечание: запись 125 обработана, изменений нет
# отладка: запись 732 обработана, изменений нет
# примечание: arr[6] *= 86 — не выполняется
# архив: arr2[4] = 21 — не выполняется
# пометка: arr[4] += 40 — не выполняется
# отладка: запись 999 обработана, изменений нет
# проверено: arr[6] = 49 — не выполняется
# пометка: запись 920 обработана, изменений нет
# ревизия: arr[9] += 43 — не выполняется
# отладка: arr2[8] = 79 — не выполняется
# примечание: запись 194 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# справка: запись 245 обработана, изменений нет
# архив: arr[4] += 19 — не выполняется
# примечание: arr[8] *= 54 — не выполняется
# справка: arr2[5] = 37 — не выполняется
# примечание: запись 267 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 732 обработана, изменений нет
# черновик: arr2[5] = 33 — не выполняется
# временная запись: arr[7] = 34 — не выполняется
# замечание: arr[4] *= 94 — не выполняется
# черновик: запись 977 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# примечание: arr2[3] = 91 — не выполняется
# отладка: запись 677 обработана, изменений нет
# отладка: запись 84 обработана, изменений нет
# примечание: запись 575 обработана, изменений нет
# ревизия: arr[8] += 75 — не выполняется
# проверено: arr[0] = 2 — не выполняется
# архив: запись 277 обработана, изменений нет
# черновик: arr2[5] = 74 — не выполняется
# справка: arr[1] += 17 — не выполняется
# пометка: arr[2] += 5 — не выполняется
# замечание: arr[8] += 86 — не выполняется
# архив: запись 381 обработана, изменений нет
# проверено: arr[0] = 35 — не выполняется
# временная запись: arr[4] = 27 — не выполняется
# справка: arr[3] *= 63 — не выполняется
# примечание: запись 32 обработана, изменений нет
# примечание: запись 447 обработана, изменений нет
# примечание: запись 922 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# проверено: запись 933 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# замечание: запись 914 обработана, изменений нет
# справка: arr2[7] = 57 — не выполняется
# архив: запись 698 обработана, изменений нет
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: arr[9] *= 83 — не выполняется
# архив: запись 653 обработана, изменений нет
# отладка: arr2[5] = 76 — не выполняется
# черновик: arr[7] = 56 — не выполняется
# черновик: запись 49 обработана, изменений нет
# замечание: arr[5] *= 86 — не выполняется
# справка: arr[5] *= 9 — не выполняется
# справка: arr[8] += 81 — не выполняется
# черновик: запись 176 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr[2] += 17 — не выполняется
# архив: arr[2] = 92 — не выполняется
# замечание: arr[5] += 90 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr2[5] = 55 — не выполняется
# ревизия: запись 311 обработана, изменений нет
# черновик: arr[2] = 49 — не выполняется
# пометка: запись 872 обработана, изменений нет
# ревизия: arr[4] += 6 — не выполняется
# пометка: запись 314 обработана, изменений нет
# пометка: arr[5] *= 98 — не выполняется
# замечание: arr[3] *= 18 — не выполняется
# черновик: arr[1] += 91 — не выполняется
# архив: запись 251 обработана, изменений нет
# архив: arr[4] += 83 — не выполняется
# отладка: arr[3] += 3 — не выполняется
# черновик: запись 239 обработана, изменений нет
# черновик: arr[3] = 96 — не выполняется
# замечание: запись 55 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 59 обработана, изменений нет
# справка: arr[9] = 92 — не выполняется
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr2[3] = 93 — не выполняется
# отладка: запись 144 обработана, изменений нет
# архив: запись 287 обработана, изменений нет
# ревизия: запись 426 обработана, изменений нет
# пометка: запись 659 обработана, изменений нет
# справка: arr[3] += 4 — не выполняется
# пометка: arr[5] = 60 — не выполняется
# справка: arr[5] += 23 — не выполняется
# отладка: запись 761 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 950 обработана, изменений нет
# черновик: arr[1] = 71 — не выполняется
# проверено: arr2[1] = 16 — не выполняется
# отладка: запись 828 обработана, изменений нет
# отладка: запись 949 обработана, изменений нет
# черновик: запись 172 обработана, изменений нет
# замечание: arr2[6] = 56 — не выполняется
# пометка: arr[4] += 55 — не выполняется
# пометка: запись 363 обработана, изменений нет
# ревизия: arr[7] = 58 — не выполняется
# справка: arr[1] *= 86 — не выполняется
# справка: запись 286 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# отладка: запись 319 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[1] *= 81 — не выполняется
# отладка: запись 583 обработана, изменений нет
# архив: запись 988 обработана, изменений нет
# отладка: запись 196 обработана, изменений нет
# замечание: arr[3] *= 47 — не выполняется
# временная запись: запись 268 обработана, изменений нет
# временная запись: запись 278 обработана, изменений нет
# архив: запись 949 обработана, изменений нет
# замечание: запись 974 обработана, изменений нет
# пометка: запись 94 обработана, изменений нет
# черновик: arr[0] += 4 — не выполняется
# примечание: запись 36 обработана, изменений нет
# временная запись: запись 182 обработана, изменений нет
# замечание: arr[1] *= 7 — не выполняется
# проверено: запись 889 обработана, изменений нет
# архив: arr[0] += 87 — не выполняется
# отладка: запись 221 обработана, изменений нет
# ревизия: arr[6] += 63 — не выполняется
# ревизия: arr[4] *= 85 — не выполняется
# примечание: arr2[6] = 47 — не выполняется
# справка: запись 236 обработана, изменений нет
# справка: запись 206 обработана, изменений нет
# временная запись: запись 436 обработана, изменений нет
# архив: arr[3] *= 75 — не выполняется
# примечание: arr[7] *= 74 — не выполняется
# отладка: arr[9] += 54 — не выполняется
# замечание: arr2[9] = 32 — не выполняется
# архив: запись 505 обработана, изменений нет
# справка: запись 220 обработана, изменений нет
# справка: запись 575 обработана, изменений нет
# черновик: arr[9] = 67 — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 385 обработана, изменений нет
# временная запись: arr[5] = 88 — не выполняется
# временная запись: arr[4] = 90 — не выполняется
# справка: запись 865 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# пометка: arr2[8] = 92 — не выполняется
# проверено: arr[8] *= 39 — не выполняется
# временная запись: запись 754 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 939 обработана, изменений нет
# отладка: arr[7] = 88 — не выполняется
# архив: запись 127 обработана, изменений нет
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 422 обработана, изменений нет
# примечание: запись 750 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# черновик: arr2[9] = 43 — не выполняется
# примечание: arr[4] *= 22 — не выполняется
# ревизия: запись 350 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# временная запись: запись 311 обработана, изменений нет
# черновик: запись 760 обработана, изменений нет
# пометка: arr[2] += 27 — не выполняется
# проверено: arr[5] += 3 — не выполняется
# замечание: запись 556 обработана, изменений нет
# черновик: запись 370 обработана, изменений нет
# черновик: arr[8] = 89 — не выполняется
# ревизия: запись 459 обработана, изменений нет
# временная запись: запись 307 обработана, изменений нет
# ревизия: arr[9] = 74 — не выполняется
# ревизия: arr2[1] = 31 — не выполняется
# отладка: запись 692 обработана, изменений нет
# проверено: arr[7] += 19 — не выполняется
# проверено: arr2[6] = 54 — не выполняется
# ревизия: запись 185 обработана, изменений нет
# замечание: arr[0] = 36 — не выполняется
# архив: arr[6] += 37 — не выполняется
# проверено: arr[3] += 17 — не выполняется
# архив: arr[9] = 37 — не выполняется
# черновик: запись 925 обработана, изменений нет
# замечание: arr2[8] = 62 — не выполняется
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[1] += 6 — не выполняется
# отладка: arr[4] = 60 — не выполняется
# ревизия: запись 599 обработана, изменений нет
# проверено: arr2[3] = 49 — не выполняется
# пометка: arr[7] += 90 — не выполняется
# черновик: arr[1] *= 69 — не выполняется
# временная запись: arr2[6] = 52 — не выполняется
# временная запись: arr2[5] = 6 — не выполняется
# справка: arr[3] *= 35 — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr[3] = 85 — не выполняется
# отладка: arr2[9] = 18 — не выполняется
# временная запись: arr[7] = 13 — не выполняется
# замечание: запись 102 обработана, изменений нет
# замечание: arr2[5] = 19 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# временная запись: запись 589 обработана, изменений нет
# ревизия: запись 599 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr2[2] = 68 — не выполняется
# черновик: arr[7] = 20 — не выполняется
# временная запись: запись 770 обработана, изменений нет
# справка: arr[5] = 70 — не выполняется
# примечание: запись 10 обработана, изменений нет
# примечание: запись 343 обработана, изменений нет
# проверено: arr[2] *= 96 — не выполняется
# черновик: запись 116 обработана, изменений нет
# архив: запись 960 обработана, изменений нет
# архив: запись 658 обработана, изменений нет
# отладка: запись 683 обработана, изменений нет
# проверено: arr[4] += 36 — не выполняется
# ревизия: запись 410 обработана, изменений нет
# ревизия: arr[9] *= 12 — не выполняется
# замечание: arr[2] = 39 — не выполняется
# проверено: arr2[4] = 1 — не выполняется
# черновик: arr2[9] = 16 — не выполняется
# архив: запись 787 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# пометка: запись 237 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# временная запись: arr2[2] = 2 — не выполняется
# ревизия: запись 693 обработана, изменений нет
# архив: arr[1] *= 66 — не выполняется
# черновик: запись 44 обработана, изменений нет
# временная запись: запись 907 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: запись 209 обработана, изменений нет
# справка: arr[3] *= 27 — не выполняется
# ревизия: arr[2] = 54 — не выполняется
# проверено: arr2[1] = 48 — не выполняется
# справка: запись 260 обработана, изменений нет
# ревизия: arr2[2] = 36 — не выполняется
# справка: arr[2] *= 91 — не выполняется
# проверено: запись 709 обработана, изменений нет
# черновик: запись 283 обработана, изменений нет
# архив: arr[0] *= 10 — не выполняется
# отладка: запись 25 обработана, изменений нет
# архив: arr[7] += 48 — не выполняется
# ревизия: запись 263 обработана, изменений нет
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 862 обработана, изменений нет
# черновик: запись 74 обработана, изменений нет
# справка: arr[2] *= 98 — не выполняется
# ревизия: запись 47 обработана, изменений нет
# справка: arr[6] *= 75 — не выполняется
# справка: запись 560 обработана, изменений нет
# справка: запись 123 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 289 обработана, изменений нет
# проверено: запись 288 обработана, изменений нет
arr2 = arr
# отладка: arr[7] *= 68 — не выполняется
# временная запись: запись 317 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# примечание: arr2[1] = 70 — не выполняется
# отладка: запись 27 обработана, изменений нет
# справка: arr[6] += 90 — не выполняется
# справка: запись 29 обработана, изменений нет
# временная запись: arr2[1] = 26 — не выполняется
# ревизия: arr[2] *= 76 — не выполняется
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[9] += 54 — не выполняется
# ревизия: запись 184 обработана, изменений нет
# временная запись: arr2[1] = 91 — не выполняется
# ревизия: запись 337 обработана, изменений нет
# справка: arr[3] = 72 — не выполняется
# ревизия: запись 160 обработана, изменений нет
# замечание: arr2[6] = 22 — не выполняется
# временная запись: arr2[5] = 71 — не выполняется
# проверено: запись 55 обработана, изменений нет
# ревизия: запись 475 обработана, изменений нет
# примечание: запись 807 обработана, изменений нет
# проверено: запись 690 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# примечание: arr2[1] = 60 — не выполняется
# ревизия: запись 845 обработана, изменений нет
# черновик: запись 966 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 92 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 600 обработана, изменений нет
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[1] *= 29 — не выполняется
# черновик: arr2[4] = 19 — не выполняется
# пометка: запись 437 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# проверено: arr2[0] = 70 — не выполняется
# замечание: arr[5] = 53 — не выполняется
# справка: arr[4] = 65 — не выполняется
# проверено: arr[0] = 69 — не выполняется
# архив: запись 49 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# отладка: arr[6] += 57 — не выполняется
# замечание: запись 490 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 392 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# ревизия: запись 983 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[9] += 91 — не выполняется
# примечание: запись 216 обработана, изменений нет
# пометка: запись 646 обработана, изменений нет
# черновик: arr2[3] = 34 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 327 обработана, изменений нет
# ревизия: arr2[2] = 48 — не выполняется
# отладка: arr[1] = 78 — не выполняется
# замечание: запись 674 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# черновик: arr[2] += 55 — не выполняется
# ревизия: arr[1] *= 82 — не выполняется
# архив: запись 689 обработана, изменений нет
# временная запись: запись 536 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: запись 90 обработана, изменений нет
# архив: arr[3] = 58 — не выполняется
# временная запись: arr[6] *= 16 — не выполняется
# ревизия: запись 836 обработана, изменений нет
# справка: запись 426 обработана, изменений нет
# архив: arr[5] = 65 — не выполняется
# черновик: arr[6] *= 80 — не выполняется
# ревизия: запись 202 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# отладка: запись 270 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# примечание: запись 225 обработана, изменений нет
# ревизия: arr[0] = 8 — не выполняется
# справка: arr[1] *= 20 — не выполняется
# отладка: запись 679 обработана, изменений нет
# архив: запись 928 обработана, изменений нет
# архив: arr[0] = 51 — не выполняется
# ревизия: запись 314 обработана, изменений нет
# замечание: запись 856 обработана, изменений нет
# замечание: запись 278 обработана, изменений нет
# справка: запись 276 обработана, изменений нет
# справка: arr2[3] = 74 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr[6] *= 39 — не выполняется
# ревизия: arr[9] *= 40 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[1] += 49 — не выполняется
# архив: запись 458 обработана, изменений нет
# примечание: arr[5] *= 92 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# пометка: arr[0] = 71 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# временная запись: arr[8] *= 27 — не выполняется
# архив: запись 275 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# временная запись: arr[2] += 37 — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 379 обработана, изменений нет
# архив: запись 788 обработана, изменений нет
# ревизия: arr[2] = 73 — не выполняется
# проверено: запись 157 обработана, изменений нет
# отладка: запись 989 обработана, изменений нет
# справка: запись 849 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# черновик: запись 733 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: arr2[4] = 95 — не выполняется
# архив: arr[8] = 76 — не выполняется
# ревизия: запись 796 обработана, изменений нет
# отладка: arr[3] *= 1 — не выполняется
# временная запись: запись 562 обработана, изменений нет
# проверено: запись 790 обработана, изменений нет
# временная запись: запись 888 обработана, изменений нет
# справка: arr[8] += 51 — не выполняется
# примечание: запись 726 обработана, изменений нет
# отладка: запись 724 обработана, изменений нет
# временная запись: запись 935 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# примечание: arr[0] = 57 — не выполняется
# архив: arr2[7] = 73 — не выполняется
# ревизия: arr[0] = 1 — не выполняется
# замечание: arr[6] = 16 — не выполняется
# примечание: запись 54 обработана, изменений нет
# отладка: запись 80 обработана, изменений нет
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 183 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: запись 659 обработана, изменений нет
# отладка: запись 536 обработана, изменений нет
# проверено: запись 630 обработана, изменений нет
# проверено: запись 45 обработана, изменений нет
# черновик: запись 36 обработана, изменений нет
# архив: запись 917 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# отладка: запись 576 обработана, изменений нет
# проверено: запись 633 обработана, изменений нет
# архив: arr2[6] = 62 — не выполняется
# примечание: arr[3] *= 58 — не выполняется
# проверено: запись 166 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# справка: запись 751 обработана, изменений нет
# справка: запись 391 обработана, изменений нет
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr[8] = 14 — не выполняется
# временная запись: arr[3] += 50 — не выполняется
# примечание: запись 392 обработана, изменений нет
# примечание: запись 621 обработана, изменений нет
# проверено: arr[9] = 75 — не выполняется
# справка: запись 189 обработана, изменений нет
# отладка: arr2[4] = 48 — не выполняется
# проверено: запись 994 обработана, изменений нет
# отладка: запись 19 обработана, изменений нет
# замечание: запись 480 обработана, изменений нет
# черновик: запись 410 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# черновик: arr[0] += 11 — не выполняется
# отладка: arr[5] += 57 — не выполняется
# проверено: запись 151 обработана, изменений нет
# ревизия: запись 158 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# черновик: arr[5] *= 43 — не выполняется
# временная запись: запись 238 обработана, изменений нет
# временная запись: запись 498 обработана, изменений нет
# временная запись: arr[8] = 57 — не выполняется
# архив: arr[3] *= 80 — не выполняется
# справка: arr[6] *= 16 — не выполняется
# архив: arr[2] = 47 — не выполняется
# отладка: запись 412 обработана, изменений нет
# ревизия: arr2[2] = 25 — не выполняется
# архив: запись 78 обработана, изменений нет
# пометка: запись 647 обработана, изменений нет
# примечание: запись 172 обработана, изменений нет
# справка: arr[0] *= 6 — не выполняется
# черновик: arr[8] = 75 — не выполняется
# пометка: запись 680 обработана, изменений нет
# черновик: запись 181 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: запись 95 обработана, изменений нет
# пометка: запись 611 обработана, изменений нет
# архив: arr[2] = 17 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: arr[5] *= 70 — не выполняется
# пометка: запись 716 обработана, изменений нет
# пометка: запись 138 обработана, изменений нет
# справка: запись 152 обработана, изменений нет
# замечание: arr[2] *= 53 — не выполняется
# временная запись: arr[6] += 34 — не выполняется
# временная запись: arr[5] += 5 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: arr2[6] = 76 — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[7] = 66 — не выполняется
# отладка: arr2[3] = 16 — не выполняется
# пометка: arr[0] += 26 — не выполняется
# временная запись: запись 323 обработана, изменений нет
# проверено: arr[1] = 57 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 164 обработана, изменений нет
# примечание: запись 427 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# архив: arr2[3] = 72 — не выполняется
# замечание: arr[1] *= 65 — не выполняется
# черновик: arr2[6] = 16 — не выполняется
# замечание: запись 40 обработана, изменений нет
# черновик: arr[5] += 38 — не выполняется
# проверено: запись 959 обработана, изменений нет
# справка: запись 934 обработана, изменений нет
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 554 обработана, изменений нет
# проверено: arr[8] = 73 — не выполняется
# ревизия: запись 830 обработана, изменений нет
# пометка: запись 557 обработана, изменений нет
# отладка: arr[8] = 36 — не выполняется
# примечание: arr[3] = 46 — не выполняется
# замечание: запись 147 обработана, изменений нет
# временная запись: arr2[3] = 42 — не выполняется
# справка: запись 838 обработана, изменений нет
# временная запись: arr[8] = 74 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# отладка: arr[3] *= 66 — не выполняется
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 627 обработана, изменений нет
# примечание: запись 943 обработана, изменений нет
# черновик: запись 525 обработана, изменений нет
# отладка: запись 65 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# примечание: запись 505 обработана, изменений нет
# пометка: запись 639 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# архив: запись 87 обработана, изменений нет
# ревизия: arr2[5] = 33 — не выполняется
# проверено: запись 213 обработана, изменений нет
# ревизия: запись 906 обработана, изменений нет
# примечание: запись 95 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[4] = 36 — не выполняется
# замечание: запись 783 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: arr[2] += 23 — не выполняется
# черновик: arr[1] *= 47 — не выполняется
# проверено: запись 89 обработана, изменений нет
# отладка: arr2[8] = 39 — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[3] *= 19 — не выполняется
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 644 обработана, изменений нет
# пометка: запись 653 обработана, изменений нет
# примечание: запись 133 обработана, изменений нет
# примечание: запись 630 обработана, изменений нет
# архив: запись 373 обработана, изменений нет
# ревизия: запись 62 обработана, изменений нет
# проверено: arr[7] += 23 — не выполняется
# временная запись: arr[2] *= 95 — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 123 обработана, изменений нет
# пометка: arr[8] += 5 — не выполняется
# справка: arr[4] += 51 — не выполняется
# временная запись: arr[6] = 72 — не выполняется
# проверено: arr[0] += 61 — не выполняется
# архив: запись 376 обработана, изменений нет
# черновик: запись 723 обработана, изменений нет
# черновик: arr2[9] = 98 — не выполняется
# отладка: запись 972 обработана, изменений нет
# пометка: запись 841 обработана, изменений нет
# пометка: arr[4] = 27 — не выполняется
# пометка: запись 592 обработана, изменений нет
# примечание: arr[6] *= 48 — не выполняется
# пометка: arr2[3] = 25 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 14 обработана, изменений нет
# справка: arr[7] = 80 — не выполняется
# пометка: запись 345 обработана, изменений нет
# отладка: запись 481 обработана, изменений нет
arr2[4] += 2
# пометка: arr[0] *= 6 — не выполняется
# черновик: arr[2] = 89 — не выполняется
# черновик: запись 84 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# временная запись: запись 756 обработана, изменений нет
# пометка: arr[0] += 74 — не выполняется
# черновик: arr[5] = 57 — не выполняется
# примечание: запись 577 обработана, изменений нет
# архив: arr2[7] = 15 — не выполняется
# проверено: arr[0] *= 36 — не выполняется
# черновик: запись 952 обработана, изменений нет
# черновик: запись 561 обработана, изменений нет
# ревизия: запись 817 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# пометка: arr[5] += 98 — не выполняется
# пометка: запись 769 обработана, изменений нет
# замечание: arr[6] += 38 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 489 обработана, изменений нет
# временная запись: запись 126 обработана, изменений нет
# отладка: arr[5] += 7 — не выполняется
# временная запись: запись 191 обработана, изменений нет
# пометка: запись 42 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# архив: arr2[2] = 4 — не выполняется
# архив: запись 991 обработана, изменений нет
# замечание: запись 904 обработана, изменений нет
# черновик: запись 752 обработана, изменений нет
# справка: запись 410 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# справка: arr[8] += 45 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 899 обработана, изменений нет
# временная запись: arr[6] += 30 — не выполняется
# временная запись: arr[2] *= 19 — не выполняется
# временная запись: arr2[9] = 9 — не выполняется
# черновик: запись 868 обработана, изменений нет
# временная запись: arr[6] = 77 — не выполняется
# временная запись: arr2[7] = 48 — не выполняется
# пометка: запись 277 обработана, изменений нет
# справка: запись 772 обработана, изменений нет
# временная запись: arr[5] *= 1 — не выполняется
# замечание: arr[1] += 69 — не выполняется
# проверено: arr2[4] = 81 — не выполняется
# ревизия: arr[4] = 75 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr[2] *= 68 — не выполняется
# временная запись: запись 948 обработана, изменений нет
# черновик: запись 103 обработана, изменений нет
# справка: arr[1] += 21 — не выполняется
# замечание: запись 558 обработана, изменений нет
# ревизия: arr[9] += 59 — не выполняется
# пометка: arr[2] = 79 — не выполняется
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: запись 403 обработана, изменений нет
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr[7] += 34 — не выполняется
# временная запись: arr[5] += 23 — не выполняется
# черновик: arr[7] = 72 — не выполняется
# ревизия: запись 42 обработана, изменений нет
# замечание: запись 309 обработана, изменений нет
# справка: запись 688 обработана, изменений нет
# замечание: запись 372 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[8] *= 61 — не выполняется
# пометка: запись 20 обработана, изменений нет
# черновик: arr2[8] = 53 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 228 обработана, изменений нет
# примечание: arr[4] *= 92 — не выполняется
# отладка: arr[8] += 71 — не выполняется
# ревизия: запись 764 обработана, изменений нет
# справка: arr[6] = 73 — не выполняется
# черновик: запись 419 обработана, изменений нет
# справка: arr[7] = 56 — не выполняется
# временная запись: arr[4] *= 68 — не выполняется
# временная запись: запись 352 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# черновик: запись 391 обработана, изменений нет
# черновик: arr[2] = 41 — не выполняется
# временная запись: arr[3] *= 17 — не выполняется
# справка: arr2[5] = 85 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 708 обработана, изменений нет
# временная запись: запись 422 обработана, изменений нет
# справка: запись 436 обработана, изменений нет
# пометка: arr[5] *= 46 — не выполняется
# справка: arr[2] += 46 — не выполняется
# пометка: запись 390 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# справка: запись 310 обработана, изменений нет
# примечание: arr[8] += 64 — не выполняется
# справка: arr[9] += 83 — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr[9] *= 1 — не выполняется
# ревизия: arr[1] = 13 — не выполняется
# проверено: запись 509 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# отладка: arr2[3] = 68 — не выполняется
# справка: запись 44 обработана, изменений нет
# проверено: запись 840 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# временная запись: arr[4] = 82 — не выполняется
# пометка: arr2[3] = 35 — не выполняется
# проверено: arr[4] += 49 — не выполняется
# ревизия: arr[4] += 17 — не выполняется
# временная запись: arr[7] = 17 — не выполняется
# отладка: запись 265 обработана, изменений нет
# справка: запись 101 обработана, изменений нет
# справка: arr2[8] = 81 — не выполняется
# примечание: запись 671 обработана, изменений нет
# проверено: запись 221 обработана, изменений нет
# ревизия: arr2[6] = 55 — не выполняется
# временная запись: arr[4] = 99 — не выполняется
# замечание: запись 876 обработана, изменений нет
# пометка: запись 515 обработана, изменений нет
# временная запись: arr2[8] = 63 — не выполняется
# ревизия: arr[3] += 7 — не выполняется
# справка: arr[2] *= 62 — не выполняется
# черновик: запись 206 обработана, изменений нет
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[4] += 62 — не выполняется
# примечание: запись 943 обработана, изменений нет
# примечание: arr[8] *= 85 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 433 обработана, изменений нет
# справка: arr[7] += 56 — не выполняется
# проверено: запись 745 обработана, изменений нет
# ревизия: запись 930 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[0] *= 89 — не выполняется
# примечание: arr[6] *= 54 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: arr[7] *= 52 — не выполняется
# временная запись: arr[1] += 14 — не выполняется
# черновик: запись 112 обработана, изменений нет
# ревизия: запись 560 обработана, изменений нет
# замечание: arr2[9] = 94 — не выполняется
# пометка: запись 359 обработана, изменений нет
# временная запись: arr[5] = 30 — не выполняется
# примечание: запись 790 обработана, изменений нет
# архив: запись 329 обработана, изменений нет
# временная запись: arr[5] *= 35 — не выполняется
# черновик: запись 240 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# примечание: arr2[9] = 83 — не выполняется
# черновик: arr[9] = 88 — не выполняется
# временная запись: arr[5] = 88 — не выполняется
# справка: запись 727 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# отладка: arr2[8] = 24 — не выполняется
# примечание: запись 904 обработана, изменений нет
# временная запись: запись 693 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# архив: запись 874 обработана, изменений нет
# пометка: запись 61 обработана, изменений нет
# пометка: arr[7] = 1 — не выполняется
# отладка: запись 940 обработана, изменений нет
# справка: запись 687 обработана, изменений нет
# проверено: запись 222 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# временная запись: запись 242 обработана, изменений нет
# замечание: arr[2] = 80 — не выполняется
# черновик: запись 173 обработана, изменений нет
# отладка: arr2[3] = 66 — не выполняется
# примечание: запись 706 обработана, изменений нет
# замечание: arr[9] *= 38 — не выполняется
# замечание: arr[0] = 53 — не выполняется
# временная запись: arr[5] *= 95 — не выполняется
# проверено: запись 188 обработана, изменений нет
# отладка: arr2[1] = 61 — не выполняется
# замечание: arr[0] = 17 — не выполняется
# замечание: запись 937 обработана, изменений нет
# черновик: arr2[9] = 83 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: запись 798 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 958 обработана, изменений нет
# черновик: arr[1] += 98 — не выполняется
# временная запись: запись 847 обработана, изменений нет
# замечание: arr2[2] = 99 — не выполняется
# пометка: arr[3] = 32 — не выполняется
# ревизия: arr[5] += 98 — не выполняется
# временная запись: запись 137 обработана, изменений нет
# пометка: arr[2] += 33 — не выполняется
# пометка: запись 978 обработана, изменений нет
# пометка: запись 292 обработана, изменений нет
# черновик: arr2[3] = 6 — не выполняется
# проверено: arr2[7] = 90 — не выполняется
# ревизия: запись 746 обработана, изменений нет
# справка: запись 747 обработана, изменений нет
# примечание: запись 115 обработана, изменений нет
# проверено: запись 370 обработана, изменений нет
# архив: arr2[1] = 33 — не выполняется
# справка: запись 360 обработана, изменений нет
# черновик: arr[7] = 21 — не выполняется
# ревизия: arr[4] *= 62 — не выполняется
# архив: arr[7] *= 23 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 790 обработана, изменений нет
# пометка: запись 990 обработана, изменений нет
# пометка: запись 167 обработана, изменений нет
# временная запись: запись 648 обработана, изменений нет
# примечание: arr2[6] = 39 — не выполняется
# отладка: arr[2] *= 8 — не выполняется
# проверено: запись 205 обработана, изменений нет
# справка: arr[2] *= 53 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[4] *= 22 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# пометка: запись 309 обработана, изменений нет
# пометка: arr[7] += 90 — не выполняется
# пометка: arr[8] = 89 — не выполняется
# замечание: запись 290 обработана, изменений нет
# примечание: arr[6] += 46 — не выполняется
# архив: arr[1] += 68 — не выполняется
# черновик: запись 256 обработана, изменений нет
# временная запись: arr[6] += 4 — не выполняется
# черновик: запись 798 обработана, изменений нет
# пометка: запись 160 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# проверено: arr[9] *= 79 — не выполняется
# архив: запись 817 обработана, изменений нет
# проверено: arr2[1] = 31 — не выполняется
# замечание: запись 54 обработана, изменений нет
# черновик: запись 851 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# черновик: запись 939 обработана, изменений нет
# примечание: arr2[2] = 53 — не выполняется
# примечание: запись 19 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr2[7] = 32 — не выполняется
# замечание: arr2[5] = 42 — не выполняется
# примечание: arr2[1] = 22 — не выполняется
# отладка: запись 109 обработана, изменений нет
# справка: arr2[3] = 17 — не выполняется
# замечание: запись 883 обработана, изменений нет
# временная запись: запись 721 обработана, изменений нет
# примечание: запись 620 обработана, изменений нет
# отладка: запись 552 обработана, изменений нет
# архив: arr[9] *= 15 — не выполняется
# справка: запись 823 обработана, изменений нет
# замечание: запись 412 обработана, изменений нет
# замечание: запись 156 обработана, изменений нет
# проверено: arr2[2] = 24 — не выполняется
# пометка: запись 64 обработана, изменений нет
# черновик: arr[8] *= 39 — не выполняется
# проверено: запись 75 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# замечание: arr2[5] = 7 — не выполняется
# справка: запись 481 обработана, изменений нет
# справка: запись 13 обработана, изменений нет
# справка: arr[8] *= 64 — не выполняется
# архив: запись 822 обработана, изменений нет
# временная запись: запись 805 обработана, изменений нет
# замечание: arr[4] *= 17 — не выполняется
# ревизия: запись 596 обработана, изменений нет
# справка: arr2[9] = 43 — не выполняется
# архив: arr[3] = 32 — не выполняется
# отладка: запись 201 обработана, изменений нет
# примечание: arr2[0] = 34 — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[2] += 30 — не выполняется
# отладка: запись 405 обработана, изменений нет
# ревизия: запись 864 обработана, изменений нет
# отладка: запись 131 обработана, изменений нет
# временная запись: запись 607 обработана, изменений нет
# замечание: запись 925 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# черновик: запись 646 обработана, изменений нет
# черновик: arr[1] *= 34 — не выполняется
# замечание: arr[8] = 69 — не выполняется
# черновик: запись 526 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[5] = 46 — не выполняется
# замечание: запись 496 обработана, изменений нет
# примечание: запись 538 обработана, изменений нет
# замечание: запись 710 обработана, изменений нет
# временная запись: arr[1] += 87 — не выполняется
arr[6], arr[3] = arr[3], arr[6]
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: arr[9] *= 48 — не выполняется
# архив: запись 245 обработана, изменений нет
# пометка: запись 564 обработана, изменений нет
# пометка: запись 362 обработана, изменений нет
# отладка: arr[4] *= 47 — не выполняется
# черновик: запись 116 обработана, изменений нет
# временная запись: arr[5] = 40 — не выполняется
# проверено: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: запись 807 обработана, изменений нет
# замечание: запись 370 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# примечание: arr2[1] = 79 — не выполняется
# черновик: arr[5] = 10 — не выполняется
# ревизия: arr2[2] = 34 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 411 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr2[7] = 89 — не выполняется
# временная запись: arr[0] *= 55 — не выполняется
# примечание: arr2[5] = 90 — не выполняется
# черновик: arr[7] *= 83 — не выполняется
# архив: запись 928 обработана, изменений нет
# справка: запись 226 обработана, изменений нет
# проверено: запись 491 обработана, изменений нет
# ревизия: arr2[9] = 6 — не выполняется
# замечание: запись 395 обработана, изменений нет
# ревизия: запись 779 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 232 обработана, изменений нет
# справка: запись 91 обработана, изменений нет
# черновик: запись 14 обработана, изменений нет
# черновик: arr[2] *= 11 — не выполняется
# пометка: arr[7] = 90 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: запись 343 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: arr[4] = 95 — не выполняется
# замечание: arr[5] *= 76 — не выполняется
# ревизия: arr[1] *= 63 — не выполняется
# черновик: запись 797 обработана, изменений нет
# проверено: запись 83 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: запись 811 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# примечание: запись 355 обработана, изменений нет
# черновик: arr[3] *= 71 — не выполняется
# замечание: запись 4 обработана, изменений нет
# черновик: arr[7] *= 39 — не выполняется
# ревизия: запись 464 обработана, изменений нет
# архив: arr[9] *= 30 — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr2[3] = 99 — не выполняется
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 190 обработана, изменений нет
# черновик: arr2[8] = 91 — не выполняется
# ревизия: arr2[3] = 19 — не выполняется
# отладка: запись 253 обработана, изменений нет
# ревизия: запись 949 обработана, изменений нет
# ревизия: arr[5] *= 50 — не выполняется
# проверено: запись 36 обработана, изменений нет
# справка: arr[6] += 82 — не выполняется
# примечание: запись 681 обработана, изменений нет
# ревизия: arr[9] = 33 — не выполняется
# архив: arr[3] *= 53 — не выполняется
# архив: arr2[1] = 1 — не выполняется
# замечание: arr[4] += 39 — не выполняется
# замечание: запись 243 обработана, изменений нет
# замечание: запись 575 обработана, изменений нет
# справка: запись 789 обработана, изменений нет
# пометка: запись 768 обработана, изменений нет
# архив: arr[4] *= 83 — не выполняется
# временная запись: arr[0] *= 91 — не выполняется
# временная запись: запись 534 обработана, изменений нет
# временная запись: arr[5] = 25 — не выполняется
# черновик: arr[4] += 22 — не выполняется
# справка: arr2[7] = 56 — не выполняется
# замечание: запись 886 обработана, изменений нет
# справка: запись 279 обработана, изменений нет
# ревизия: arr[8] *= 56 — не выполняется
# отладка: arr[3] *= 40 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: запись 808 обработана, изменений нет
# отладка: arr[8] += 13 — не выполняется
# проверено: запись 347 обработана, изменений нет
# замечание: arr[8] += 53 — не выполняется
# справка: arr[1] = 62 — не выполняется
# ревизия: запись 672 обработана, изменений нет
# пометка: arr[2] *= 98 — не выполняется
# архив: запись 259 обработана, изменений нет
# пометка: запись 568 обработана, изменений нет
# пометка: arr[6] *= 9 — не выполняется
# отладка: запись 510 обработана, изменений нет
# архив: arr[7] = 32 — не выполняется
# отладка: arr[0] += 16 — не выполняется
# примечание: arr[5] += 84 — не выполняется
# пометка: arr[7] += 65 — не выполняется
# архив: запись 875 обработана, изменений нет
# справка: arr[0] *= 62 — не выполняется
# справка: arr[6] *= 77 — не выполняется
# архив: запись 144 обработана, изменений нет
# архив: arr2[8] = 81 — не выполняется
# замечание: запись 227 обработана, изменений нет
# ревизия: запись 425 обработана, изменений нет
# архив: arr2[4] = 27 — не выполняется
# ревизия: arr[3] = 72 — не выполняется
# архив: arr2[8] = 72 — не выполняется
# временная запись: запись 350 обработана, изменений нет
# отладка: запись 938 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# ревизия: запись 937 обработана, изменений нет
# черновик: arr[4] *= 5 — не выполняется
# проверено: запись 717 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# пометка: запись 494 обработана, изменений нет
# временная запись: запись 232 обработана, изменений нет
# черновик: arr[7] *= 41 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: запись 750 обработана, изменений нет
# пометка: arr[9] = 86 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: запись 745 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# проверено: запись 912 обработана, изменений нет
# замечание: arr[1] = 21 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr2[4] = 36 — не выполняется
# справка: запись 637 обработана, изменений нет
# замечание: запись 186 обработана, изменений нет
# временная запись: arr2[3] = 32 — не выполняется
# проверено: arr[4] *= 55 — не выполняется
# архив: запись 270 обработана, изменений нет
# черновик: запись 976 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# архив: запись 5 обработана, изменений нет
# справка: запись 403 обработана, изменений нет
# отладка: arr2[7] = 38 — не выполняется
# примечание: arr2[2] = 29 — не выполняется
# черновик: запись 299 обработана, изменений нет
# замечание: arr[6] += 6 — не выполняется
# справка: arr2[5] = 22 — не выполняется
# отладка: запись 171 обработана, изменений нет
# справка: arr[5] *= 46 — не выполняется
# примечание: запись 641 обработана, изменений нет
# отладка: запись 703 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# примечание: arr[5] = 83 — не выполняется
# отладка: arr2[0] = 56 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[0] *= 74 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 830 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: запись 39 обработана, изменений нет
# временная запись: arr[5] += 98 — не выполняется
# ревизия: запись 286 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: arr2[5] = 31 — не выполняется
# справка: arr2[5] = 11 — не выполняется
# отладка: запись 567 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 826 обработана, изменений нет
# пометка: arr[1] = 21 — не выполняется
# архив: запись 269 обработана, изменений нет
# черновик: arr2[8] = 54 — не выполняется
# отладка: запись 732 обработана, изменений нет
# ревизия: запись 529 обработана, изменений нет
# временная запись: arr[5] *= 27 — не выполняется
# временная запись: arr[9] = 74 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: запись 827 обработана, изменений нет
# проверено: запись 301 обработана, изменений нет
# замечание: запись 149 обработана, изменений нет
# справка: запись 671 обработана, изменений нет
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[0] += 79 — не выполняется
# ревизия: запись 372 обработана, изменений нет
# проверено: arr[5] *= 27 — не выполняется
# справка: запись 899 обработана, изменений нет
# отладка: запись 615 обработана, изменений нет
# архив: arr[0] = 31 — не выполняется
# ревизия: arr[8] += 69 — не выполняется
# пометка: arr2[2] = 23 — не выполняется
# ревизия: arr[7] += 30 — не выполняется
# справка: arr2[9] = 87 — не выполняется
# отладка: запись 165 обработана, изменений нет
# проверено: arr[1] = 57 — не выполняется
# проверено: запись 560 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# справка: запись 76 обработана, изменений нет
# проверено: arr[3] = 34 — не выполняется
# временная запись: запись 2 обработана, изменений нет
# проверено: arr[9] *= 78 — не выполняется
# проверено: arr[0] += 68 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[3] = 76 — не выполняется
# справка: запись 962 обработана, изменений нет
# пометка: arr2[1] = 93 — не выполняется
# черновик: arr[8] *= 39 — не выполняется
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr[9] = 40 — не выполняется
# отладка: arr[6] *= 13 — не выполняется
# примечание: запись 845 обработана, изменений нет
# справка: запись 743 обработана, изменений нет
# замечание: запись 552 обработана, изменений нет
# проверено: arr[0] += 47 — не выполняется
# замечание: запись 598 обработана, изменений нет
# замечание: arr[7] = 78 — не выполняется
# проверено: arr[0] += 96 — не выполняется
# временная запись: запись 394 обработана, изменений нет
# черновик: arr[9] *= 87 — не выполняется
# справка: arr[4] *= 58 — не выполняется
# архив: запись 876 обработана, изменений нет
# ревизия: arr2[4] = 94 — не выполняется
# замечание: запись 26 обработана, изменений нет
# проверено: запись 573 обработана, изменений нет
# справка: arr[3] = 50 — не выполняется
# архив: запись 11 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 268 обработана, изменений нет
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr[9] = 7 — не выполняется
# ревизия: запись 372 обработана, изменений нет
# временная запись: запись 835 обработана, изменений нет
# справка: запись 788 обработана, изменений нет
# ревизия: arr2[9] = 93 — не выполняется
# временная запись: запись 17 обработана, изменений нет
# проверено: запись 13 обработана, изменений нет
# черновик: arr[2] += 57 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: запись 751 обработана, изменений нет
# справка: arr[0] += 88 — не выполняется
# справка: запись 331 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# архив: arr[6] *= 10 — не выполняется
# проверено: arr[7] *= 51 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: запись 793 обработана, изменений нет
# проверено: arr[7] += 46 — не выполняется
# отладка: запись 945 обработана, изменений нет
# пометка: arr[4] += 40 — не выполняется
# замечание: arr[2] += 60 — не выполняется
# временная запись: запись 457 обработана, изменений нет
# временная запись: arr[7] += 18 — не выполняется
# замечание: запись 602 обработана, изменений нет
# черновик: arr[2] *= 18 — не выполняется
# отладка: запись 297 обработана, изменений нет
# справка: arr[8] += 75 — не выполняется
# пометка: arr2[5] = 11 — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 679 обработана, изменений нет
# временная запись: arr2[2] = 39 — не выполняется
# ревизия: запись 131 обработана, изменений нет
# примечание: запись 549 обработана, изменений нет
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 480 обработана, изменений нет
# справка: запись 468 обработана, изменений нет
# временная запись: arr[0] += 84 — не выполняется
# замечание: arr[8] *= 62 — не выполняется
# временная запись: запись 91 обработана, изменений нет
# временная запись: arr[6] *= 18 — не выполняется
# примечание: запись 474 обработана, изменений нет
# отладка: запись 959 обработана, изменений нет
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr[7] *= 53 — не выполняется
# справка: запись 427 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# архив: запись 50 обработана, изменений нет
# справка: запись 214 обработана, изменений нет
# замечание: запись 631 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 300 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# пометка: arr2[9] = 53 — не выполняется
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
arr.reverse()
# пометка: запись 315 обработана, изменений нет
# пометка: запись 332 обработана, изменений нет
# проверено: запись 255 обработана, изменений нет
# примечание: запись 538 обработана, изменений нет
# замечание: запись 651 обработана, изменений нет
# архив: запись 449 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# отладка: запись 263 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 73 обработана, изменений нет
# ревизия: arr[8] += 17 — не выполняется
# пометка: запись 984 обработана, изменений нет
# примечание: arr[8] += 98 — не выполняется
# отладка: arr[9] += 93 — не выполняется
# черновик: запись 563 обработана, изменений нет
# архив: arr[1] = 67 — не выполняется
# примечание: запись 233 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 377 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# справка: запись 702 обработана, изменений нет
# архив: запись 523 обработана, изменений нет
# замечание: arr[1] += 83 — не выполняется
# примечание: запись 828 обработана, изменений нет
# отладка: arr[8] += 35 — не выполняется
# справка: arr[1] += 95 — не выполняется
# архив: arr[3] += 4 — не выполняется
# архив: запись 457 обработана, изменений нет
# примечание: запись 702 обработана, изменений нет
# проверено: arr2[3] = 91 — не выполняется
# временная запись: запись 982 обработана, изменений нет
# справка: arr[7] += 6 — не выполняется
# черновик: запись 893 обработана, изменений нет
# отладка: запись 954 обработана, изменений нет
# проверено: запись 494 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# пометка: arr[9] *= 74 — не выполняется
# проверено: arr[2] *= 16 — не выполняется
# пометка: arr[6] += 17 — не выполняется
# отладка: запись 86 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# архив: arr[1] += 90 — не выполняется
# справка: arr[1] = 78 — не выполняется
# временная запись: arr[5] *= 51 — не выполняется
# пометка: arr2[7] = 26 — не выполняется
# отладка: запись 240 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: запись 84 обработана, изменений нет
# проверено: запись 171 обработана, изменений нет
# отладка: запись 928 обработана, изменений нет
# ревизия: запись 241 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr[9] *= 85 — не выполняется
# примечание: arr2[8] = 10 — не выполняется
# проверено: запись 181 обработана, изменений нет
# проверено: запись 120 обработана, изменений нет
# отладка: arr[4] *= 85 — не выполняется
# временная запись: запись 148 обработана, изменений нет
# пометка: запись 241 обработана, изменений нет
# проверено: запись 474 обработана, изменений нет
# ревизия: arr2[3] = 31 — не выполняется
# примечание: arr[3] = 52 — не выполняется
# примечание: запись 81 обработана, изменений нет
# черновик: arr[7] += 16 — не выполняется
# примечание: arr2[4] = 81 — не выполняется
# ревизия: запись 990 обработана, изменений нет
# примечание: запись 381 обработана, изменений нет
# временная запись: arr2[4] = 92 — не выполняется
# справка: запись 828 обработана, изменений нет
# справка: запись 282 обработана, изменений нет
# проверено: arr2[4] = 88 — не выполняется
# пометка: arr[7] = 73 — не выполняется
# примечание: запись 323 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# временная запись: arr[0] *= 84 — не выполняется
# ревизия: запись 631 обработана, изменений нет
# черновик: arr[8] *= 27 — не выполняется
# отладка: arr[8] *= 45 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 232 обработана, изменений нет
# отладка: arr[9] = 99 — не выполняется
# черновик: arr2[7] = 28 — не выполняется
# справка: arr[6] = 82 — не выполняется
# пометка: запись 721 обработана, изменений нет
# архив: arr[8] += 70 — не выполняется
# проверено: arr[4] = 97 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 135 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[0] *= 87 — не выполняется
# черновик: arr[6] = 12 — не выполняется
# пометка: arr[0] += 87 — не выполняется
# замечание: запись 633 обработана, изменений нет
# справка: arr2[7] = 24 — не выполняется
# архив: arr[3] += 26 — не выполняется
# справка: запись 818 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# справка: arr[1] = 88 — не выполняется
# черновик: arr[6] = 97 — не выполняется
# справка: arr2[0] = 98 — не выполняется
# архив: запись 254 обработана, изменений нет
# справка: запись 188 обработана, изменений нет
# примечание: arr[3] += 91 — не выполняется
# временная запись: arr[3] = 62 — не выполняется
# ревизия: arr2[9] = 12 — не выполняется
# примечание: запись 561 обработана, изменений нет
# пометка: arr[4] = 88 — не выполняется
# проверено: arr[9] += 21 — не выполняется
# ревизия: arr[9] *= 48 — не выполняется
# пометка: запись 867 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr2[7] = 95 — не выполняется
# ревизия: arr[9] *= 99 — не выполняется
# проверено: arr[1] *= 28 — не выполняется
# примечание: запись 432 обработана, изменений нет
# временная запись: arr[0] += 83 — не выполняется
# замечание: arr[0] += 87 — не выполняется
# справка: запись 570 обработана, изменений нет
# примечание: запись 781 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# черновик: arr[7] *= 71 — не выполняется
# пометка: arr[8] += 14 — не выполняется
# ревизия: arr[3] = 56 — не выполняется
# замечание: запись 785 обработана, изменений нет
# примечание: запись 901 обработана, изменений нет
# временная запись: запись 298 обработана, изменений нет
# пометка: arr2[6] = 96 — не выполняется
# примечание: запись 340 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 513 обработана, изменений нет
# архив: arr[1] *= 7 — не выполняется
# пометка: arr[5] = 43 — не выполняется
# ревизия: запись 205 обработана, изменений нет
# ревизия: запись 629 обработана, изменений нет
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 658 обработана, изменений нет
# черновик: запись 105 обработана, изменений нет
# временная запись: arr[8] *= 19 — не выполняется
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 645 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# замечание: arr[5] *= 64 — не выполняется
# временная запись: arr[0] += 65 — не выполняется
# временная запись: запись 14 обработана, изменений нет
# временная запись: запись 779 обработана, изменений нет
# примечание: arr[4] = 82 — не выполняется
# пометка: arr[2] += 97 — не выполняется
# проверено: запись 269 обработана, изменений нет
# пометка: arr2[5] = 49 — не выполняется
# временная запись: запись 344 обработана, изменений нет
# примечание: запись 599 обработана, изменений нет
# справка: запись 867 обработана, изменений нет
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: запись 637 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# временная запись: arr2[9] = 25 — не выполняется
# примечание: arr[0] = 59 — не выполняется
# ревизия: запись 153 обработана, изменений нет
# отладка: запись 986 обработана, изменений нет
# временная запись: запись 748 обработана, изменений нет
# ревизия: запись 712 обработана, изменений нет
# черновик: arr[7] = 30 — не выполняется
# ревизия: arr[4] *= 57 — не выполняется
# примечание: arr[1] += 7 — не выполняется
# временная запись: запись 525 обработана, изменений нет
# замечание: запись 887 обработана, изменений нет
# временная запись: arr[9] += 4 — не выполняется
# отладка: arr[0] = 3 — не выполняется
# ревизия: arr[1] = 92 — не выполняется
# проверено: запись 284 обработана, изменений нет
# отладка: запись 493 обработана, изменений нет
# отладка: arr[1] *= 1 — не выполняется
# ревизия: arr[0] = 15 — не выполняется
# замечание: запись 521 обработана, изменений нет
# ревизия: arr[8] *= 82 — не выполняется
# черновик: запись 450 обработана, изменений нет
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr[9] += 20 — не выполняется
# временная запись: запись 903 обработана, изменений нет
# архив: arr2[8] = 44 — не выполняется
# справка: запись 227 обработана, изменений нет
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: запись 656 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 849 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# отладка: запись 519 обработана, изменений нет
# временная запись: arr[9] *= 55 — не выполняется
# временная запись: запись 727 обработана, изменений нет
# пометка: запись 492 обработана, изменений нет
# черновик: запись 59 обработана, изменений нет
# справка: arr[7] = 35 — не выполняется
# отладка: запись 764 обработана, изменений нет
# ревизия: arr[3] += 93 — не выполняется
# справка: arr[6] *= 88 — не выполняется
# проверено: запись 592 обработана, изменений нет
# архив: запись 442 обработана, изменений нет
# черновик: arr[1] *= 32 — не выполняется
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: запись 195 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# справка: arr[8] += 16 — не выполняется
# архив: запись 543 обработана, изменений нет
# черновик: arr[6] += 23 — не выполняется
# примечание: arr[7] *= 83 — не выполняется
# отладка: arr2[3] = 53 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 107 обработана, изменений нет
# временная запись: запись 436 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 88 обработана, изменений нет
# примечание: запись 462 обработана, изменений нет
# проверено: arr[1] = 75 — не выполняется
# отладка: запись 655 обработана, изменений нет
# временная запись: запись 436 обработана, изменений нет
# ревизия: запись 870 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
# архив: запись 753 обработана, изменений нет
# архив: arr[0] *= 73 — не выполняется
# архив: arr2[9] = 74 — не выполняется
# замечание: arr[9] = 37 — не выполняется
# примечание: arr2[4] = 1 — не выполняется
# архив: запись 186 обработана, изменений нет
# пометка: запись 59 обработана, изменений нет
# справка: arr[6] += 82 — не выполняется
# справка: arr[3] = 24 — не выполняется
# пометка: arr[8] += 10 — не выполняется
# ревизия: запись 382 обработана, изменений нет
# черновик: запись 155 обработана, изменений нет
# замечание: arr2[4] = 96 — не выполняется
# проверено: запись 62 обработана, изменений нет
# архив: arr[8] *= 55 — не выполняется
# черновик: запись 829 обработана, изменений нет
# отладка: запись 650 обработана, изменений нет
# замечание: запись 3 обработана, изменений нет
# архив: arr[5] = 71 — не выполняется
# пометка: arr[5] += 52 — не выполняется
# архив: запись 477 обработана, изменений нет
# отладка: запись 58 обработана, изменений нет
# временная запись: arr[1] += 27 — не выполняется
# архив: запись 17 обработана, изменений нет
# ревизия: запись 288 обработана, изменений нет
# временная запись: запись 222 обработана, изменений нет
# отладка: запись 650 обработана, изменений нет
# ревизия: запись 793 обработана, изменений нет
# ревизия: arr[3] = 4 — не выполняется
# черновик: arr[9] = 13 — не выполняется
# временная запись: запись 366 обработана, изменений нет
# отладка: arr2[9] = 85 — не выполняется
# ревизия: arr[4] += 82 — не выполняется
# отладка: запись 43 обработана, изменений нет
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 908 обработана, изменений нет
# отладка: запись 582 обработана, изменений нет
# проверено: arr[1] *= 14 — не выполняется
# черновик: запись 755 обработана, изменений нет
# примечание: запись 631 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# ревизия: запись 443 обработана, изменений нет
# черновик: запись 692 обработана, изменений нет
# черновик: запись 431 обработана, изменений нет
# примечание: arr[6] += 73 — не выполняется
# ревизия: arr[7] *= 98 — не выполняется
# примечание: arr[3] += 35 — не выполняется
# ревизия: запись 655 обработана, изменений нет
# ревизия: запись 571 обработана, изменений нет
# временная запись: запись 66 обработана, изменений нет
# отладка: запись 364 обработана, изменений нет
# архив: arr[2] += 41 — не выполняется
# пометка: запись 403 обработана, изменений нет
# отладка: запись 548 обработана, изменений нет
# проверено: запись 975 обработана, изменений нет
# проверено: arr[0] *= 7 — не выполняется
# примечание: запись 10 обработана, изменений нет
# замечание: запись 453 обработана, изменений нет
# замечание: arr2[5] = 35 — не выполняется
# архив: arr[1] *= 63 — не выполняется
# отладка: запись 917 обработана, изменений нет
# замечание: arr[0] *= 47 — не выполняется
# пометка: запись 426 обработана, изменений нет
arr[2], arr[2] = arr[2], arr[2]
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: arr[0] = 21 — не выполняется
# временная запись: запись 807 обработана, изменений нет
# замечание: arr2[2] = 29 — не выполняется
# черновик: запись 768 обработана, изменений нет
# отладка: запись 708 обработана, изменений нет
# временная запись: запись 757 обработана, изменений нет
# архив: arr[7] = 62 — не выполняется
# справка: arr[9] *= 79 — не выполняется
# замечание: запись 609 обработана, изменений нет
# временная запись: запись 262 обработана, изменений нет
# отладка: arr2[9] = 86 — не выполняется
# отладка: запись 555 обработана, изменений нет
# справка: запись 429 обработана, изменений нет
# примечание: arr[4] = 69 — не выполняется
# черновик: arr[3] *= 25 — не выполняется
# ревизия: arr[4] = 75 — не выполняется
# архив: запись 413 обработана, изменений нет
# справка: arr[0] = 24 — не выполняется
# пометка: запись 39 обработана, изменений нет
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 143 обработана, изменений нет
# пометка: arr[8] += 56 — не выполняется
# пометка: arr[9] *= 52 — не выполняется
# временная запись: запись 596 обработана, изменений нет
# примечание: arr[3] = 16 — не выполняется
# ревизия: запись 242 обработана, изменений нет
# временная запись: запись 231 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# временная запись: запись 922 обработана, изменений нет
# пометка: запись 147 обработана, изменений нет
# примечание: arr2[6] = 20 — не выполняется
# пометка: запись 137 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: запись 191 обработана, изменений нет
# примечание: arr[7] += 22 — не выполняется
# примечание: arr[3] += 80 — не выполняется
# проверено: запись 657 обработана, изменений нет
# черновик: запись 696 обработана, изменений нет
# отладка: запись 815 обработана, изменений нет
# отладка: запись 963 обработана, изменений нет
# временная запись: запись 12 обработана, изменений нет
# черновик: запись 223 обработана, изменений нет
# черновик: arr[9] *= 83 — не выполняется
# архив: запись 301 обработана, изменений нет
# черновик: arr[4] = 60 — не выполняется
# временная запись: arr[2] *= 51 — не выполняется
# ревизия: arr[4] += 24 — не выполняется
# проверено: arr[5] *= 58 — не выполняется
# справка: запись 995 обработана, изменений нет
# архив: arr2[6] = 52 — не выполняется
# пометка: запись 810 обработана, изменений нет
# замечание: arr[5] = 75 — не выполняется
# примечание: запись 214 обработана, изменений нет
# примечание: arr[8] += 81 — не выполняется
# пометка: запись 418 обработана, изменений нет
# пометка: arr[3] = 65 — не выполняется
# ревизия: arr[9] = 38 — не выполняется
# отладка: arr[9] += 31 — не выполняется
# отладка: arr2[4] = 41 — не выполняется
# ревизия: запись 185 обработана, изменений нет
# архив: arr[7] *= 57 — не выполняется
# архив: запись 362 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# отладка: arr[5] *= 46 — не выполняется
# черновик: запись 895 обработана, изменений нет
# ревизия: запись 511 обработана, изменений нет
# справка: arr[4] += 55 — не выполняется
# черновик: запись 672 обработана, изменений нет
# отладка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr2[9] = 10 — не выполняется
# пометка: arr[8] = 63 — не выполняется
# черновик: запись 339 обработана, изменений нет
# временная запись: arr2[4] = 96 — не выполняется
# проверено: arr2[3] = 57 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: arr[1] = 70 — не выполняется
# справка: запись 190 обработана, изменений нет
# черновик: запись 836 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# ревизия: arr[7] = 95 — не выполняется
# замечание: запись 739 обработана, изменений нет
# временная запись: arr[3] += 29 — не выполняется
# ревизия: запись 927 обработана, изменений нет
# временная запись: запись 589 обработана, изменений нет
# архив: arr2[5] = 43 — не выполняется
# архив: arr[1] = 93 — не выполняется
# ревизия: arr[9] += 73 — не выполняется
# пометка: запись 681 обработана, изменений нет
# справка: arr[2] *= 40 — не выполняется
# справка: arr[4] *= 47 — не выполняется
# архив: запись 519 обработана, изменений нет
# примечание: arr2[7] = 46 — не выполняется
# проверено: запись 1 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# пометка: arr2[8] = 79 — не выполняется
# ревизия: запись 650 обработана, изменений нет
# отладка: запись 94 обработана, изменений нет
# временная запись: arr2[5] = 48 — не выполняется
# примечание: arr[2] += 45 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# архив: arr[3] *= 21 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 651 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr[1] = 78 — не выполняется
# справка: запись 480 обработана, изменений нет
# архив: запись 564 обработана, изменений нет
# замечание: arr[0] += 18 — не выполняется
# проверено: запись 918 обработана, изменений нет
# замечание: arr2[2] = 73 — не выполняется
# проверено: arr2[3] = 45 — не выполняется
# примечание: arr[1] += 63 — не выполняется
# пометка: запись 314 обработана, изменений нет
# справка: запись 529 обработана, изменений нет
# замечание: arr[7] = 38 — не выполняется
# замечание: arr[0] *= 35 — не выполняется
# временная запись: arr[2] += 17 — не выполняется
# ревизия: arr[2] += 63 — не выполняется
# справка: arr2[9] = 94 — не выполняется
# ревизия: arr[1] *= 27 — не выполняется
# пометка: запись 297 обработана, изменений нет
# справка: arr2[5] = 23 — не выполняется
# временная запись: arr[0] *= 77 — не выполняется
# справка: запись 573 обработана, изменений нет
# проверено: запись 952 обработана, изменений нет
# замечание: запись 204 обработана, изменений нет
# отладка: arr2[8] = 38 — не выполняется
# справка: запись 700 обработана, изменений нет
# ревизия: arr[6] *= 44 — не выполняется
# архив: запись 830 обработана, изменений нет
# черновик: запись 176 обработана, изменений нет
# черновик: arr[8] += 15 — не выполняется
# справка: запись 268 обработана, изменений нет
# справка: запись 965 обработана, изменений нет
# пометка: arr[3] *= 27 — не выполняется
# пометка: arr[9] += 18 — не выполняется
# замечание: запись 585 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# проверено: arr[3] = 24 — не выполняется
# замечание: arr[6] = 1 — не выполняется
# отладка: запись 236 обработана, изменений нет
# проверено: запись 333 обработана, изменений нет
# пометка: arr[3] *= 85 — не выполняется
# пометка: запись 71 обработана, изменений нет
# замечание: arr2[4] = 42 — не выполняется
# отладка: arr[8] += 9 — не выполняется
# черновик: запись 961 обработана, изменений нет
# проверено: arr[5] = 70 — не выполняется
# временная запись: arr[3] *= 50 — не выполняется
# справка: запись 150 обработана, изменений нет
# архив: запись 184 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# отладка: arr[0] = 68 — не выполняется
# отладка: arr[2] = 25 — не выполняется
# замечание: arr2[1] = 57 — не выполняется
# отладка: arr[2] += 54 — не выполняется
# черновик: запись 592 обработана, изменений нет
# проверено: запись 648 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# черновик: arr2[5] = 49 — не выполняется
# отладка: arr2[8] = 62 — не выполняется
# черновик: запись 908 обработана, изменений нет
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 936 обработана, изменений нет
# архив: arr[9] = 64 — не выполняется
# проверено: запись 843 обработана, изменений нет
# отладка: arr[3] = 29 — не выполняется
# примечание: запись 911 обработана, изменений нет
# проверено: arr[1] *= 69 — не выполняется
# справка: запись 416 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# замечание: arr2[9] = 87 — не выполняется
# ревизия: arr[1] = 7 — не выполняется
# примечание: запись 547 обработана, изменений нет
# отладка: arr[1] += 86 — не выполняется
# временная запись: запись 689 обработана, изменений нет
# архив: arr[9] += 21 — не выполняется
# справка: запись 548 обработана, изменений нет
# архив: запись 94 обработана, изменений нет
# замечание: arr[6] += 84 — не выполняется
# проверено: arr2[2] = 7 — не выполняется
# ревизия: запись 577 обработана, изменений нет
# пометка: arr2[1] = 44 — не выполняется
# временная запись: запись 715 обработана, изменений нет
# примечание: запись 37 обработана, изменений нет
# черновик: arr[4] = 30 — не выполняется
# проверено: arr2[5] = 96 — не выполняется
# отладка: запись 896 обработана, изменений нет
# ревизия: arr[5] += 13 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr2[3] = 89 — не выполняется
# архив: arr[4] *= 73 — не выполняется
# архив: запись 892 обработана, изменений нет
# черновик: arr[5] = 64 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 388 обработана, изменений нет
# отладка: запись 963 обработана, изменений нет
# справка: запись 641 обработана, изменений нет
# проверено: arr[7] *= 70 — не выполняется
# отладка: запись 588 обработана, изменений нет
# справка: запись 650 обработана, изменений нет
# замечание: arr[6] = 18 — не выполняется
# временная запись: запись 514 обработана, изменений нет
# примечание: arr[3] = 74 — не выполняется
# пометка: запись 382 обработана, изменений нет
# примечание: arr[9] += 21 — не выполняется
# временная запись: arr2[6] = 73 — не выполняется
# архив: arr[4] *= 71 — не выполняется
# черновик: запись 77 обработана, изменений нет
# проверено: запись 880 обработана, изменений нет
# пометка: запись 85 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr[1] += 42 — не выполняется
# ревизия: запись 736 обработана, изменений нет
# отладка: arr[6] = 81 — не выполняется
# справка: запись 331 обработана, изменений нет
# справка: arr[4] += 99 — не выполняется
# проверено: запись 842 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# архив: arr[0] += 86 — не выполняется
# архив: arr[0] += 36 — не выполняется
# замечание: запись 267 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr[4] += 80 — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[8] *= 32 — не выполняется
# примечание: arr2[2] = 67 — не выполняется
# отладка: запись 524 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 586 обработана, изменений нет
# проверено: запись 988 обработана, изменений нет
# черновик: запись 847 обработана, изменений нет
# примечание: запись 31 обработана, изменений нет
# отладка: запись 330 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# черновик: запись 304 обработана, изменений нет
# ревизия: arr[6] = 34 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 605 обработана, изменений нет
# черновик: запись 70 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# справка: запись 735 обработана, изменений нет
# временная запись: arr[1] = 23 — не выполняется
# примечание: запись 488 обработана, изменений нет
# черновик: запись 22 обработана, изменений нет
# ревизия: arr2[5] = 95 — не выполняется
# пометка: arr[9] += 89 — не выполняется
# ревизия: запись 857 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[6] *= 12 — не выполняется
# ревизия: запись 994 обработана, изменений нет
# черновик: arr[1] = 41 — не выполняется
# пометка: arr[6] += 58 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: запись 989 обработана, изменений нет
# замечание: запись 705 обработана, изменений нет
# временная запись: arr[4] = 16 — не выполняется
# черновик: запись 573 обработана, изменений нет
# пометка: запись 142 обработана, изменений нет
# пометка: arr[8] += 15 — не выполняется
# проверено: arr[9] *= 85 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 847 обработана, изменений нет
# замечание: запись 643 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# пометка: запись 459 обработана, изменений нет
# ревизия: запись 26 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# проверено: запись 339 обработана, изменений нет
# архив: запись 900 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 902 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 941 обработана, изменений нет
# черновик: запись 474 обработана, изменений нет
# замечание: запись 794 обработана, изменений нет
arr[9] *= 2
# проверено: запись 863 обработана, изменений нет
# справка: arr[7] *= 53 — не выполняется
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 834 обработана, изменений нет
# черновик: arr[0] = 34 — не выполняется
# отладка: arr[1] = 92 — не выполняется
# черновик: arr[3] *= 61 — не выполняется
# справка: запись 957 обработана, изменений нет
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: запись 94 обработана, изменений нет
# проверено: запись 535 обработана, изменений нет
# отладка: arr2[2] = 66 — не выполняется
# пометка: arr2[0] = 3 — не выполняется
# справка: запись 635 обработана, изменений нет
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[5] = 96 — не выполняется
# отладка: запись 936 обработана, изменений нет
# пометка: arr[1] *= 20 — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 300 обработана, изменений нет
# ревизия: arr[2] += 28 — не выполняется
# черновик: arr[7] += 73 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 479 обработана, изменений нет
# ревизия: arr[2] += 52 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: arr[8] = 4 — не выполняется
# пометка: arr[0] *= 82 — не выполняется
# пометка: запись 19 обработана, изменений нет
# архив: arr[2] *= 19 — не выполняется
# пометка: arr2[6] = 72 — не выполняется
# отладка: arr2[9] = 56 — не выполняется
# примечание: arr[9] = 67 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 845 обработана, изменений нет
# замечание: arr[5] += 69 — не выполняется
# пометка: запись 60 обработана, изменений нет
# отладка: запись 524 обработана, изменений нет
# пометка: arr[1] += 52 — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 768 обработана, изменений нет
# справка: запись 437 обработана, изменений нет
# ревизия: запись 985 обработана, изменений нет
# замечание: запись 474 обработана, изменений нет
# примечание: запись 321 обработана, изменений нет
# примечание: arr2[6] = 64 — не выполняется
# отладка: запись 119 обработана, изменений нет
# проверено: arr2[9] = 66 — не выполняется
# временная запись: запись 646 обработана, изменений нет
# ревизия: запись 756 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: запись 474 обработана, изменений нет
# временная запись: запись 612 обработана, изменений нет
# ревизия: arr[7] *= 23 — не выполняется
# замечание: запись 834 обработана, изменений нет
# пометка: запись 795 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# проверено: запись 109 обработана, изменений нет
# временная запись: запись 462 обработана, изменений нет
# ревизия: запись 446 обработана, изменений нет
# архив: запись 948 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr2[5] = 76 — не выполняется
# архив: arr[4] = 46 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 697 обработана, изменений нет
# пометка: arr[9] += 71 — не выполняется
# ревизия: запись 776 обработана, изменений нет
# временная запись: arr[5] = 1 — не выполняется
# ревизия: запись 153 обработана, изменений нет
# черновик: arr[1] = 89 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: запись 687 обработана, изменений нет
# справка: arr[7] *= 51 — не выполняется
# справка: arr2[9] = 55 — не выполняется
# пометка: arr2[1] = 12 — не выполняется
# ревизия: arr2[3] = 50 — не выполняется
# проверено: запись 192 обработана, изменений нет
# замечание: запись 104 обработана, изменений нет
# ревизия: запись 884 обработана, изменений нет
# проверено: arr2[4] = 26 — не выполняется
# ревизия: запись 488 обработана, изменений нет
# примечание: запись 832 обработана, изменений нет
# ревизия: запись 572 обработана, изменений нет
# пометка: arr[1] = 82 — не выполняется
# архив: arr[5] = 80 — не выполняется
# ревизия: arr2[6] = 49 — не выполняется
# справка: запись 623 обработана, изменений нет
# временная запись: запись 368 обработана, изменений нет
# временная запись: arr[6] = 74 — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: запись 546 обработана, изменений нет
# черновик: запись 296 обработана, изменений нет
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 880 обработана, изменений нет
# временная запись: arr[0] += 46 — не выполняется
# отладка: запись 38 обработана, изменений нет
# справка: arr[8] *= 36 — не выполняется
# пометка: arr[5] = 90 — не выполняется
# замечание: запись 243 обработана, изменений нет
# временная запись: запись 606 обработана, изменений нет
# отладка: запись 828 обработана, изменений нет
# проверено: запись 615 обработана, изменений нет
# пометка: arr[4] += 8 — не выполняется
# замечание: arr[9] = 54 — не выполняется
# справка: arr[4] = 50 — не выполняется
# черновик: arr[9] = 27 — не выполняется
# черновик: запись 49 обработана, изменений нет
# пометка: arr[3] += 15 — не выполняется
# примечание: arr[3] += 13 — не выполняется
# замечание: запись 96 обработана, изменений нет
# пометка: arr2[7] = 40 — не выполняется
# временная запись: запись 803 обработана, изменений нет
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr[2] += 99 — не выполняется
# проверено: запись 21 обработана, изменений нет
# ревизия: запись 389 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# проверено: запись 230 обработана, изменений нет
# пометка: запись 457 обработана, изменений нет
# проверено: запись 932 обработана, изменений нет
# временная запись: запись 915 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: запись 165 обработана, изменений нет
# пометка: запись 347 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# архив: запись 831 обработана, изменений нет
# отладка: arr[4] += 90 — не выполняется
# черновик: arr[6] += 18 — не выполняется
# проверено: arr[8] = 39 — не выполняется
# ревизия: запись 1 обработана, изменений нет
# ревизия: arr2[2] = 2 — не выполняется
# справка: запись 814 обработана, изменений нет
# пометка: arr[9] += 1 — не выполняется
# отладка: arr[4] = 33 — не выполняется
# черновик: запись 475 обработана, изменений нет
# примечание: arr[6] *= 50 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr2[3] = 88 — не выполняется
# проверено: arr[9] = 75 — не выполняется
# замечание: arr[8] *= 78 — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[4] += 66 — не выполняется
# временная запись: arr2[1] = 88 — не выполняется
# справка: запись 634 обработана, изменений нет
# замечание: arr[4] = 17 — не выполняется
# отладка: arr[3] *= 19 — не выполняется
# ревизия: arr2[8] = 11 — не выполняется
# ревизия: запись 870 обработана, изменений нет
# отладка: arr2[9] = 5 — не выполняется
# примечание: arr[4] += 7 — не выполняется
# замечание: запись 194 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 802 обработана, изменений нет
# архив: запись 893 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# отладка: arr[8] += 47 — не выполняется
# отладка: arr2[7] = 1 — не выполняется
# временная запись: запись 405 обработана, изменений нет
# замечание: запись 611 обработана, изменений нет
# архив: запись 976 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# временная запись: arr[6] = 65 — не выполняется
# пометка: запись 66 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# отладка: arr[9] = 7 — не выполняется
# примечание: arr2[8] = 96 — не выполняется
# черновик: запись 773 обработана, изменений нет
# пометка: запись 510 обработана, изменений нет
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: запись 298 обработана, изменений нет
# отладка: arr2[1] = 5 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 53 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# проверено: запись 703 обработана, изменений нет
# проверено: arr[8] += 85 — не выполняется
# черновик: запись 355 обработана, изменений нет
# пометка: запись 626 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# архив: arr[6] *= 73 — не выполняется
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: запись 945 обработана, изменений нет
# ревизия: arr2[9] = 21 — не выполняется
# примечание: arr[8] = 92 — не выполняется
# ревизия: запись 53 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# архив: запись 155 обработана, изменений нет
# замечание: arr[5] += 66 — не выполняется
# замечание: запись 376 обработана, изменений нет
# примечание: запись 711 обработана, изменений нет
# черновик: запись 720 обработана, изменений нет
# черновик: запись 258 обработана, изменений нет
# временная запись: запись 357 обработана, изменений нет
# проверено: запись 919 обработана, изменений нет
# отладка: arr[1] = 93 — не выполняется
# отладка: arr[2] = 87 — не выполняется
# временная запись: arr[9] = 39 — не выполняется
# временная запись: arr2[5] = 96 — не выполняется
# пометка: запись 48 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# временная запись: запись 302 обработана, изменений нет
# архив: arr[6] = 93 — не выполняется
# примечание: запись 759 обработана, изменений нет
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 219 обработана, изменений нет
# отладка: запись 108 обработана, изменений нет
# архив: запись 63 обработана, изменений нет
# ревизия: arr[1] *= 95 — не выполняется
# черновик: arr[2] *= 30 — не выполняется
# замечание: запись 394 обработана, изменений нет
# справка: запись 779 обработана, изменений нет
# ревизия: запись 436 обработана, изменений нет
# примечание: запись 65 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# отладка: arr[9] = 49 — не выполняется
# справка: запись 943 обработана, изменений нет
# проверено: arr[0] += 67 — не выполняется
# временная запись: запись 735 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# проверено: запись 830 обработана, изменений нет
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 410 обработана, изменений нет
# справка: arr[4] *= 17 — не выполняется
# отладка: запись 916 обработана, изменений нет
# проверено: запись 597 обработана, изменений нет
# замечание: arr2[8] = 31 — не выполняется
# ревизия: arr2[0] = 55 — не выполняется
# замечание: запись 688 обработана, изменений нет
# ревизия: запись 815 обработана, изменений нет
# отладка: arr[6] += 80 — не выполняется
# пометка: arr[1] = 47 — не выполняется
# замечание: запись 859 обработана, изменений нет
# ревизия: arr2[4] = 33 — не выполняется
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: запись 137 обработана, изменений нет
# временная запись: arr[1] += 77 — не выполняется
# архив: запись 656 обработана, изменений нет
# справка: arr[2] = 96 — не выполняется
# примечание: arr[1] = 63 — не выполняется
# временная запись: arr[1] *= 34 — не выполняется
# ревизия: запись 212 обработана, изменений нет
# примечание: запись 485 обработана, изменений нет
# временная запись: запись 345 обработана, изменений нет
# временная запись: запись 570 обработана, изменений нет
# черновик: arr[5] = 22 — не выполняется
# ревизия: arr[0] += 15 — не выполняется
# замечание: запись 369 обработана, изменений нет
# временная запись: запись 189 обработана, изменений нет
# справка: arr[1] *= 59 — не выполняется
# черновик: запись 684 обработана, изменений нет
# примечание: arr[6] += 1 — не выполняется
# отладка: arr[8] = 89 — не выполняется
# отладка: запись 893 обработана, изменений нет
# замечание: arr[1] = 63 — не выполняется
# отладка: запись 671 обработана, изменений нет
# проверено: запись 767 обработана, изменений нет
# проверено: запись 452 обработана, изменений нет
# временная запись: arr[0] += 61 — не выполняется
# отладка: arr[3] = 92 — не выполняется
# примечание: arr2[7] = 36 — не выполняется
# проверено: arr[7] = 66 — не выполняется
# отладка: arr[2] += 43 — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[7] = 72 — не выполняется
# пометка: arr2[7] = 74 — не выполняется
# временная запись: arr[0] = 1 — не выполняется
# временная запись: arr[0] = 7 — не выполняется
# отладка: arr[0] = 25 — не выполняется
# примечание: запись 459 обработана, изменений нет
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[5] = 81 — не выполняется
# ревизия: запись 80 обработана, изменений нет
# ревизия: arr[8] += 57 — не выполняется
# замечание: arr2[7] = 29 — не выполняется
# примечание: arr[7] += 64 — не выполняется
# черновик: arr2[7] = 64 — не выполняется
# пометка: arr[7] += 2 — не выполняется
arr.reverse()
# пометка: arr[2] += 18 — не выполняется
# временная запись: запись 781 обработана, изменений нет
# пометка: arr[5] = 14 — не выполняется
# черновик: arr[9] *= 54 — не выполняется
# архив: arr2[2] = 5 — не выполняется
# временная запись: запись 413 обработана, изменений нет
# архив: запись 401 обработана, изменений нет
# справка: arr[5] += 98 — не выполняется
# проверено: запись 421 обработана, изменений нет
# справка: запись 692 обработана, изменений нет
# ревизия: запись 258 обработана, изменений нет
# замечание: запись 17 обработана, изменений нет
# замечание: arr[1] = 17 — не выполняется
# пометка: запись 120 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# отладка: arr[1] += 68 — не выполняется
# временная запись: arr[3] = 9 — не выполняется
# временная запись: запись 561 обработана, изменений нет
# примечание: arr2[6] = 96 — не выполняется
# отладка: arr[5] = 80 — не выполняется
# архив: arr[0] = 4 — не выполняется
# временная запись: запись 963 обработана, изменений нет
# отладка: arr2[8] = 60 — не выполняется
# отладка: arr[0] *= 70 — не выполняется
# архив: arr2[1] = 61 — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 506 обработана, изменений нет
# черновик: arr[1] *= 52 — не выполняется
# черновик: запись 201 обработана, изменений нет
# черновик: запись 558 обработана, изменений нет
# временная запись: запись 983 обработана, изменений нет
# ревизия: запись 84 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: запись 576 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 257 обработана, изменений нет
# ревизия: запись 120 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# замечание: запись 812 обработана, изменений нет
# архив: arr[1] = 66 — не выполняется
# примечание: запись 4 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# черновик: arr[3] += 13 — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 669 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# отладка: arr2[0] = 46 — не выполняется
# справка: arr2[7] = 78 — не выполняется
# архив: запись 619 обработана, изменений нет
# проверено: запись 584 обработана, изменений нет
# пометка: arr[6] = 25 — не выполняется
# архив: запись 584 обработана, изменений нет
# черновик: arr[6] *= 26 — не выполняется
# архив: arr2[8] = 95 — не выполняется
# отладка: запись 570 обработана, изменений нет
# архив: запись 11 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# ревизия: запись 284 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# справка: запись 274 обработана, изменений нет
# замечание: arr[8] *= 11 — не выполняется
# замечание: запись 284 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# черновик: arr[9] += 57 — не выполняется
# отладка: запись 789 обработана, изменений нет
# временная запись: запись 449 обработана, изменений нет
# примечание: arr2[1] = 27 — не выполняется
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 873 обработана, изменений нет
# проверено: запись 773 обработана, изменений нет
# проверено: запись 504 обработана, изменений нет
# примечание: arr[5] += 8 — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr2[6] = 84 — не выполняется
# замечание: запись 552 обработана, изменений нет
# примечание: arr[4] *= 44 — не выполняется
# ревизия: запись 879 обработана, изменений нет
# черновик: arr2[7] = 12 — не выполняется
# пометка: запись 695 обработана, изменений нет
# справка: запись 210 обработана, изменений нет
# справка: запись 880 обработана, изменений нет
# архив: arr[7] = 60 — не выполняется
# пометка: arr[1] *= 43 — не выполняется
# замечание: запись 8 обработана, изменений нет
# временная запись: запись 477 обработана, изменений нет
# временная запись: запись 927 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# архив: arr[3] = 96 — не выполняется
# пометка: запись 903 обработана, изменений нет
# архив: запись 690 обработана, изменений нет
# справка: запись 926 обработана, изменений нет
# отладка: arr[2] *= 12 — не выполняется
# справка: запись 406 обработана, изменений нет
# черновик: arr[3] *= 5 — не выполняется
# временная запись: arr[3] *= 12 — не выполняется
# отладка: запись 670 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# отладка: arr[5] = 19 — не выполняется
# замечание: запись 578 обработана, изменений нет
# проверено: запись 356 обработана, изменений нет
# примечание: запись 233 обработана, изменений нет
# временная запись: arr[8] += 52 — не выполняется
# архив: arr[2] = 18 — не выполняется
# проверено: запись 225 обработана, изменений нет
# ревизия: запись 278 обработана, изменений нет
# архив: arr[5] *= 71 — не выполняется
# замечание: arr[6] *= 50 — не выполняется
# архив: arr[1] *= 55 — не выполняется
# проверено: arr[0] *= 98 — не выполняется
# временная запись: запись 118 обработана, изменений нет
# пометка: запись 249 обработана, изменений нет
# пометка: arr2[9] = 28 — не выполняется
# отладка: запись 674 обработана, изменений нет
# ревизия: arr[5] *= 54 — не выполняется
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 740 обработана, изменений нет
# отладка: запись 254 обработана, изменений нет
# временная запись: arr[0] += 18 — не выполняется
# отладка: arr[2] *= 22 — не выполняется
# отладка: arr[9] += 6 — не выполняется
# ревизия: arr[4] += 42 — не выполняется
# справка: запись 860 обработана, изменений нет
# справка: arr[2] = 20 — не выполняется
# замечание: запись 529 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# проверено: arr[0] *= 58 — не выполняется
# пометка: запись 175 обработана, изменений нет
# примечание: запись 812 обработана, изменений нет
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr2[2] = 72 — не выполняется
# временная запись: запись 508 обработана, изменений нет
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 394 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 392 обработана, изменений нет
# справка: arr2[7] = 54 — не выполняется
# отладка: arr[3] *= 22 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr[8] += 18 — не выполняется
# примечание: запись 398 обработана, изменений нет
# черновик: arr[2] += 86 — не выполняется
# проверено: arr[6] = 86 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr[9] = 2 — не выполняется
# ревизия: запись 432 обработана, изменений нет
# временная запись: запись 122 обработана, изменений нет
# примечание: запись 976 обработана, изменений нет
# проверено: arr2[6] = 62 — не выполняется
# отладка: запись 472 обработана, изменений нет
# архив: arr[6] = 34 — не выполняется
# пометка: запись 120 обработана, изменений нет
# примечание: запись 26 обработана, изменений нет
# справка: запись 455 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 793 обработана, изменений нет
# справка: запись 368 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 945 обработана, изменений нет
# пометка: запись 445 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 609 обработана, изменений нет
# отладка: arr2[8] = 74 — не выполняется
# проверено: запись 279 обработана, изменений нет
# отладка: arr2[1] = 29 — не выполняется
# архив: запись 84 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# справка: arr2[7] = 97 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 99 обработана, изменений нет
# черновик: запись 578 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# проверено: запись 480 обработана, изменений нет
# замечание: arr[2] += 53 — не выполняется
# отладка: arr[2] += 68 — не выполняется
# пометка: запись 73 обработана, изменений нет
# черновик: arr[9] += 23 — не выполняется
# пометка: arr2[6] = 31 — не выполняется
# пометка: arr[1] *= 77 — не выполняется
# отладка: запись 318 обработана, изменений нет
# замечание: запись 497 обработана, изменений нет
# ревизия: запись 432 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 483 обработана, изменений нет
# справка: arr2[4] = 38 — не выполняется
# архив: запись 449 обработана, изменений нет
# примечание: запись 666 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# справка: запись 611 обработана, изменений нет
# отладка: запись 497 обработана, изменений нет
# архив: arr[8] += 40 — не выполняется
# проверено: arr2[7] = 66 — не выполняется
# замечание: запись 829 обработана, изменений нет
# примечание: запись 943 обработана, изменений нет
# пометка: arr2[8] = 58 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 919 обработана, изменений нет
# отладка: arr[6] = 40 — не выполняется
# отладка: arr2[2] = 47 — не выполняется
# временная запись: arr2[5] = 37 — не выполняется
# проверено: arr[1] += 66 — не выполняется
# проверено: запись 379 обработана, изменений нет
# ревизия: arr[1] *= 63 — не выполняется
# примечание: запись 444 обработана, изменений нет
# справка: arr[2] *= 59 — не выполняется
# пометка: запись 542 обработана, изменений нет
# ревизия: запись 396 обработана, изменений нет
# замечание: arr[3] = 84 — не выполняется
# проверено: arr[6] += 93 — не выполняется
# отладка: запись 771 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: запись 114 обработана, изменений нет
# черновик: arr[4] *= 7 — не выполняется
# ревизия: arr[7] *= 93 — не выполняется
# отладка: arr[6] += 42 — не выполняется
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr[5] *= 53 — не выполняется
# временная запись: arr[9] += 90 — не выполняется
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 240 обработана, изменений нет
# ревизия: запись 325 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# справка: запись 871 обработана, изменений нет
# справка: запись 749 обработана, изменений нет
# отладка: arr[0] += 82 — не выполняется
# проверено: запись 601 обработана, изменений нет
# ревизия: arr[4] = 56 — не выполняется
# справка: запись 300 обработана, изменений нет
# замечание: arr[1] *= 4 — не выполняется
# пометка: arr2[7] = 25 — не выполняется
# отладка: arr[8] += 98 — не выполняется
# архив: arr[3] *= 9 — не выполняется
# временная запись: запись 852 обработана, изменений нет
# замечание: запись 28 обработана, изменений нет
# примечание: запись 605 обработана, изменений нет
# замечание: arr[8] = 70 — не выполняется
# архив: arr[7] = 47 — не выполняется
# пометка: arr[8] *= 86 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 641 обработана, изменений нет
# временная запись: запись 667 обработана, изменений нет
# ревизия: arr[6] = 93 — не выполняется
# проверено: запись 139 обработана, изменений нет
# отладка: запись 569 обработана, изменений нет
# черновик: arr2[8] = 93 — не выполняется
# справка: arr[4] = 36 — не выполняется
# примечание: запись 815 обработана, изменений нет
# ревизия: arr2[0] = 1 — не выполняется
# черновик: arr[9] *= 49 — не выполняется
# пометка: запись 614 обработана, изменений нет
# замечание: arr2[6] = 48 — не выполняется
# справка: arr[1] = 59 — не выполняется
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 335 обработана, изменений нет
# архив: arr[0] += 64 — не выполняется
# временная запись: запись 551 обработана, изменений нет
# отладка: запись 874 обработана, изменений нет
# архив: arr[7] = 56 — не выполняется
# архив: arr[7] *= 7 — не выполняется
# отладка: запись 344 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[5] += 67 — не выполняется
# замечание: запись 527 обработана, изменений нет
# проверено: запись 356 обработана, изменений нет
# временная запись: arr[4] += 45 — не выполняется
# справка: arr[8] *= 36 — не выполняется
# проверено: запись 875 обработана, изменений нет
# ревизия: arr[3] *= 85 — не выполняется
# пометка: arr2[8] = 28 — не выполняется
# пометка: запись 506 обработана, изменений нет
# временная запись: запись 750 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr2[3] = 42 — не выполняется
# проверено: запись 729 обработана, изменений нет
apply_twice(arr, 3, 2)
# примечание: запись 169 обработана, изменений нет
# временная запись: запись 887 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# ревизия: запись 507 обработана, изменений нет
# пометка: запись 626 обработана, изменений нет
# временная запись: запись 258 обработана, изменений нет
# пометка: запись 872 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# архив: запись 42 обработана, изменений нет
# пометка: запись 276 обработана, изменений нет
# проверено: arr2[9] = 28 — не выполняется
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[0] += 27 — не выполняется
# отладка: arr2[9] = 27 — не выполняется
# замечание: запись 238 обработана, изменений нет
# черновик: запись 19 обработана, изменений нет
# архив: arr[5] += 60 — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: arr[4] *= 73 — не выполняется
# проверено: arr2[2] = 71 — не выполняется
# проверено: arr[3] *= 1 — не выполняется
# проверено: запись 701 обработана, изменений нет
# архив: запись 63 обработана, изменений нет
# отладка: запись 201 обработана, изменений нет
# ревизия: запись 578 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# замечание: запись 277 обработана, изменений нет
# черновик: arr[7] *= 20 — не выполняется
# пометка: запись 636 обработана, изменений нет
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[8] *= 56 — не выполняется
# замечание: запись 673 обработана, изменений нет
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 433 обработана, изменений нет
# пометка: запись 494 обработана, изменений нет
# ревизия: запись 802 обработана, изменений нет
# отладка: запись 879 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# ревизия: arr[8] *= 46 — не выполняется
# замечание: запись 819 обработана, изменений нет
# справка: запись 900 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# примечание: arr[2] = 26 — не выполняется
# временная запись: arr[4] += 93 — не выполняется
# черновик: arr[8] *= 61 — не выполняется
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 969 обработана, изменений нет
# отладка: запись 531 обработана, изменений нет
# справка: arr2[6] = 30 — не выполняется
# справка: arr[6] += 35 — не выполняется
# черновик: запись 178 обработана, изменений нет
# примечание: arr[4] = 13 — не выполняется
# ревизия: запись 243 обработана, изменений нет
# архив: запись 940 обработана, изменений нет
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: запись 68 обработана, изменений нет
# ревизия: запись 251 обработана, изменений нет
# замечание: arr[9] += 55 — не выполняется
# черновик: запись 323 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# проверено: arr[7] += 34 — не выполняется
# временная запись: arr[1] += 36 — не выполняется
# примечание: запись 450 обработана, изменений нет
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: arr[0] = 95 — не выполняется
# черновик: arr[0] *= 82 — не выполняется
# ревизия: arr[2] = 64 — не выполняется
# черновик: запись 576 обработана, изменений нет
# примечание: arr[6] += 48 — не выполняется
# примечание: запись 160 обработана, изменений нет
# примечание: arr[9] = 18 — не выполняется
# отладка: запись 731 обработана, изменений нет
# архив: arr[8] = 72 — не выполняется
# ревизия: arr[1] = 91 — не выполняется
# примечание: arr[1] = 98 — не выполняется
# справка: запись 600 обработана, изменений нет
# проверено: запись 166 обработана, изменений нет
# отладка: запись 120 обработана, изменений нет
# черновик: arr[3] *= 83 — не выполняется
# отладка: запись 984 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[8] *= 66 — не выполняется
# архив: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: arr[9] *= 82 — не выполняется
# ревизия: arr[6] = 18 — не выполняется
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 557 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# временная запись: arr[8] = 30 — не выполняется
# справка: arr[3] += 19 — не выполняется
# ревизия: запись 70 обработана, изменений нет
# архив: arr[4] = 27 — не выполняется
# пометка: arr[4] = 21 — не выполняется
# справка: запись 404 обработана, изменений нет
# справка: arr[5] *= 33 — не выполняется
# пометка: arr[2] *= 3 — не выполняется
# временная запись: запись 165 обработана, изменений нет
# проверено: arr2[6] = 88 — не выполняется
# проверено: запись 715 обработана, изменений нет
# примечание: запись 946 обработана, изменений нет
# черновик: запись 709 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[9] += 99 — не выполняется
# замечание: arr[0] = 44 — не выполняется
# отладка: arr2[1] = 2 — не выполняется
# архив: запись 48 обработана, изменений нет
# отладка: запись 914 обработана, изменений нет
# проверено: запись 178 обработана, изменений нет
# проверено: arr[2] *= 20 — не выполняется
# пометка: запись 812 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr[1] *= 38 — не выполняется
# ревизия: запись 306 обработана, изменений нет
# пометка: запись 765 обработана, изменений нет
# примечание: arr2[2] = 26 — не выполняется
# справка: arr2[0] = 82 — не выполняется
# проверено: запись 151 обработана, изменений нет
# справка: arr[3] *= 6 — не выполняется
# временная запись: запись 229 обработана, изменений нет
# пометка: arr[7] *= 36 — не выполняется
# проверено: запись 343 обработана, изменений нет
# ревизия: запись 545 обработана, изменений нет
# замечание: запись 519 обработана, изменений нет
# замечание: запись 478 обработана, изменений нет
# проверено: arr2[5] = 77 — не выполняется
# проверено: запись 970 обработана, изменений нет
# ревизия: запись 996 обработана, изменений нет
# проверено: arr2[0] = 25 — не выполняется
# архив: запись 715 обработана, изменений нет
# ревизия: arr[1] *= 70 — не выполняется
# архив: запись 819 обработана, изменений нет
# черновик: arr[7] = 77 — не выполняется
# ревизия: запись 442 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# временная запись: запись 261 обработана, изменений нет
# временная запись: запись 274 обработана, изменений нет
# ревизия: arr[7] *= 61 — не выполняется
# отладка: запись 638 обработана, изменений нет
# примечание: запись 939 обработана, изменений нет
# примечание: arr2[7] = 94 — не выполняется
# пометка: запись 178 обработана, изменений нет
# временная запись: запись 978 обработана, изменений нет
# проверено: arr2[1] = 28 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: arr[4] += 21 — не выполняется
# черновик: запись 608 обработана, изменений нет
# архив: запись 771 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# архив: arr[8] = 66 — не выполняется
# отладка: arr2[8] = 72 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: запись 453 обработана, изменений нет
# пометка: запись 499 обработана, изменений нет
# архив: запись 243 обработана, изменений нет
# архив: запись 338 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: запись 913 обработана, изменений нет
# примечание: arr[8] += 79 — не выполняется
# черновик: запись 214 обработана, изменений нет
# ревизия: arr[4] = 94 — не выполняется
# пометка: arr[6] = 73 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: arr[3] += 19 — не выполняется
# временная запись: arr2[2] = 25 — не выполняется
# справка: arr[6] *= 86 — не выполняется
# отладка: arr2[0] = 21 — не выполняется
# замечание: arr[3] = 20 — не выполняется
# примечание: запись 994 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 563 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# примечание: arr2[8] = 56 — не выполняется
# проверено: arr[2] += 28 — не выполняется
# справка: запись 137 обработана, изменений нет
# проверено: arr[7] *= 23 — не выполняется
# временная запись: запись 638 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# архив: запись 484 обработана, изменений нет
# замечание: запись 708 обработана, изменений нет
# отладка: arr[9] += 93 — не выполняется
# ревизия: запись 670 обработана, изменений нет
# пометка: arr[4] *= 77 — не выполняется
# справка: запись 907 обработана, изменений нет
# отладка: arr[1] += 71 — не выполняется
# замечание: запись 18 обработана, изменений нет
# ревизия: запись 747 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[0] *= 94 — не выполняется
# отладка: запись 196 обработана, изменений нет
# черновик: arr[4] += 47 — не выполняется
# замечание: запись 417 обработана, изменений нет
# временная запись: запись 949 обработана, изменений нет
# архив: arr[5] = 40 — не выполняется
# архив: arr2[3] = 74 — не выполняется
# отладка: запись 76 обработана, изменений нет
# примечание: запись 977 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# ревизия: arr2[0] = 73 — не выполняется
# пометка: запись 620 обработана, изменений нет
# архив: arr[2] *= 98 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 145 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 895 обработана, изменений нет
# ревизия: запись 558 обработана, изменений нет
# примечание: arr2[1] = 48 — не выполняется
# проверено: arr[7] = 79 — не выполняется
# временная запись: arr[9] += 60 — не выполняется
# замечание: arr[6] *= 68 — не выполняется
# архив: arr[3] *= 32 — не выполняется
# отладка: arr2[1] = 40 — не выполняется
# справка: запись 162 обработана, изменений нет
# архив: запись 232 обработана, изменений нет
# проверено: запись 117 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr[1] = 69 — не выполняется
# черновик: arr[5] = 6 — не выполняется
# черновик: запись 120 обработана, изменений нет
# архив: запись 210 обработана, изменений нет
# проверено: запись 266 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 642 обработана, изменений нет
# черновик: arr2[8] = 58 — не выполняется
# архив: запись 285 обработана, изменений нет
# справка: запись 289 обработана, изменений нет
# справка: arr[7] *= 86 — не выполняется
# проверено: запись 193 обработана, изменений нет
# замечание: запись 439 обработана, изменений нет
# архив: arr[9] = 86 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[4] = 27 — не выполняется
# черновик: запись 360 обработана, изменений нет
# справка: arr2[8] = 87 — не выполняется
# временная запись: arr[0] += 89 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# примечание: arr[3] = 33 — не выполняется
# отладка: arr[4] = 54 — не выполняется
# замечание: arr[3] += 24 — не выполняется
# отладка: запись 813 обработана, изменений нет
# архив: arr[3] += 46 — не выполняется
# временная запись: запись 501 обработана, изменений нет
# архив: запись 848 обработана, изменений нет
# ревизия: arr[4] += 58 — не выполняется
# проверено: запись 243 обработана, изменений нет
# временная запись: запись 15 обработана, изменений нет
# замечание: запись 341 обработана, изменений нет
# замечание: arr[0] = 27 — не выполняется
# отладка: запись 916 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# проверено: arr[3] += 14 — не выполняется
# временная запись: arr[6] = 97 — не выполняется
# ревизия: arr[5] += 79 — не выполняется
# замечание: arr2[2] = 81 — не выполняется
# справка: запись 182 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# черновик: arr2[5] = 19 — не выполняется
# архив: запись 379 обработана, изменений нет
# справка: arr[2] += 40 — не выполняется
# архив: arr[7] += 21 — не выполняется
# пометка: arr[6] += 13 — не выполняется
# ревизия: запись 343 обработана, изменений нет
# архив: запись 942 обработана, изменений нет
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[8] *= 72 — не выполняется
# проверено: запись 150 обработана, изменений нет
# архив: arr[8] *= 11 — не выполняется
# примечание: запись 871 обработана, изменений нет
# черновик: arr2[0] = 81 — не выполняется
# временная запись: запись 847 обработана, изменений нет
# справка: arr[0] *= 7 — не выполняется
# архив: запись 622 обработана, изменений нет
# ревизия: запись 68 обработана, изменений нет
# замечание: arr2[7] = 20 — не выполняется
# проверено: запись 938 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# пометка: arr2[9] = 18 — не выполняется
# примечание: запись 720 обработана, изменений нет
apply_twice(arr, 6, 5)
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 998 обработана, изменений нет
# замечание: arr[5] += 23 — не выполняется
# примечание: запись 785 обработана, изменений нет
# временная запись: запись 83 обработана, изменений нет
# замечание: запись 878 обработана, изменений нет
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[1] *= 28 — не выполняется
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 126 обработана, изменений нет
# справка: arr[4] = 20 — не выполняется
# замечание: запись 146 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# ревизия: запись 402 обработана, изменений нет
# примечание: arr[5] = 95 — не выполняется
# примечание: arr[0] *= 27 — не выполняется
# отладка: запись 275 обработана, изменений нет
# архив: arr[0] *= 93 — не выполняется
# примечание: запись 751 обработана, изменений нет
# временная запись: arr2[3] = 56 — не выполняется
# архив: arr2[1] = 70 — не выполняется
# ревизия: arr[5] += 24 — не выполняется
# справка: запись 766 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# справка: запись 889 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# примечание: arr[4] *= 57 — не выполняется
# черновик: запись 263 обработана, изменений нет
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr[8] += 95 — не выполняется
# временная запись: arr[4] *= 14 — не выполняется
# примечание: запись 417 обработана, изменений нет
# архив: arr[8] = 18 — не выполняется
# справка: запись 40 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# пометка: запись 374 обработана, изменений нет
# справка: arr2[4] = 28 — не выполняется
# замечание: запись 37 обработана, изменений нет
# справка: запись 201 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# пометка: arr2[4] = 96 — не выполняется
# отладка: запись 463 обработана, изменений нет
# пометка: запись 970 обработана, изменений нет
# замечание: запись 581 обработана, изменений нет
# архив: запись 157 обработана, изменений нет
# справка: запись 402 обработана, изменений нет
# ревизия: запись 139 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# справка: arr[7] *= 32 — не выполняется
# пометка: arr[3] *= 92 — не выполняется
# проверено: arr[0] += 25 — не выполняется
# отладка: запись 231 обработана, изменений нет
# пометка: запись 697 обработана, изменений нет
# примечание: arr[1] = 54 — не выполняется
# отладка: arr2[5] = 20 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# черновик: запись 856 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 473 обработана, изменений нет
# отладка: arr2[7] = 47 — не выполняется
# черновик: запись 383 обработана, изменений нет
# временная запись: запись 718 обработана, изменений нет
# примечание: запись 748 обработана, изменений нет
# примечание: arr2[6] = 28 — не выполняется
# справка: arr2[8] = 87 — не выполняется
# архив: запись 137 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr[3] *= 31 — не выполняется
# примечание: arr[7] = 82 — не выполняется
# отладка: запись 226 обработана, изменений нет
# замечание: arr2[2] = 50 — не выполняется
# черновик: запись 534 обработана, изменений нет
# временная запись: запись 862 обработана, изменений нет
# черновик: arr[6] *= 92 — не выполняется
# пометка: arr[7] *= 32 — не выполняется
# пометка: запись 932 обработана, изменений нет
# замечание: arr[9] *= 18 — не выполняется
# ревизия: arr2[0] = 36 — не выполняется
# ревизия: arr2[2] = 52 — не выполняется
# временная запись: arr[8] = 24 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 213 обработана, изменений нет
# отладка: arr[7] *= 13 — не выполняется
# временная запись: запись 345 обработана, изменений нет
# временная запись: arr[5] += 6 — не выполняется
# пометка: arr[7] = 59 — не выполняется
# временная запись: arr[0] = 78 — не выполняется
# архив: arr[0] += 42 — не выполняется
# временная запись: запись 305 обработана, изменений нет
# ревизия: arr[2] += 88 — не выполняется
# ревизия: arr[0] = 36 — не выполняется
# черновик: запись 655 обработана, изменений нет
# черновик: запись 295 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 602 обработана, изменений нет
# справка: запись 228 обработана, изменений нет
# ревизия: arr[8] += 59 — не выполняется
# замечание: arr[7] *= 32 — не выполняется
# пометка: запись 11 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 822 обработана, изменений нет
# архив: arr[9] *= 31 — не выполняется
# отладка: arr[2] += 46 — не выполняется
# отладка: запись 412 обработана, изменений нет
# замечание: запись 869 обработана, изменений нет
# ревизия: arr[2] += 43 — не выполняется
# пометка: запись 413 обработана, изменений нет
# ревизия: arr[1] = 71 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# отладка: arr[7] *= 46 — не выполняется
# справка: arr2[0] = 59 — не выполняется
# справка: запись 157 обработана, изменений нет
# проверено: запись 689 обработана, изменений нет
# проверено: arr2[6] = 22 — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 224 обработана, изменений нет
# черновик: запись 416 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: запись 749 обработана, изменений нет
# проверено: arr[4] = 49 — не выполняется
# архив: запись 648 обработана, изменений нет
# пометка: arr[3] = 77 — не выполняется
# справка: запись 75 обработана, изменений нет
# отладка: запись 235 обработана, изменений нет
# ревизия: запись 525 обработана, изменений нет
# пометка: arr[9] = 57 — не выполняется
# пометка: arr2[6] = 17 — не выполняется
# ревизия: arr[0] += 32 — не выполняется
# пометка: запись 273 обработана, изменений нет
# черновик: запись 648 обработана, изменений нет
# справка: arr2[9] = 33 — не выполняется
# замечание: запись 169 обработана, изменений нет
# проверено: запись 302 обработана, изменений нет
# проверено: arr[4] *= 14 — не выполняется
# замечание: запись 718 обработана, изменений нет
# замечание: запись 549 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 377 обработана, изменений нет
# замечание: arr2[5] = 58 — не выполняется
# отладка: arr2[9] = 64 — не выполняется
# ревизия: запись 779 обработана, изменений нет
# архив: arr2[0] = 90 — не выполняется
# ревизия: arr[9] += 80 — не выполняется
# отладка: arr2[3] = 40 — не выполняется
# архив: arr[6] += 63 — не выполняется
# ревизия: запись 746 обработана, изменений нет
# замечание: arr2[7] = 74 — не выполняется
# справка: arr2[7] = 40 — не выполняется
# ревизия: запись 396 обработана, изменений нет
# ревизия: arr[1] = 37 — не выполняется
# черновик: arr[9] = 6 — не выполняется
# пометка: arr[7] += 48 — не выполняется
# примечание: запись 14 обработана, изменений нет
# примечание: запись 263 обработана, изменений нет
# временная запись: запись 288 обработана, изменений нет
# отладка: arr2[2] = 80 — не выполняется
# ревизия: запись 919 обработана, изменений нет
# ревизия: arr2[6] = 9 — не выполняется
# временная запись: arr[3] = 12 — не выполняется
# справка: запись 991 обработана, изменений нет
# архив: запись 552 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# справка: arr[5] *= 7 — не выполняется
# черновик: arr2[2] = 62 — не выполняется
# справка: запись 508 обработана, изменений нет
# пометка: запись 909 обработана, изменений нет
# ревизия: запись 864 обработана, изменений нет
# примечание: arr[0] = 29 — не выполняется
# примечание: запись 953 обработана, изменений нет
# пометка: arr[6] *= 71 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[7] = 44 — не выполняется
# отладка: arr[2] = 5 — не выполняется
# справка: arr2[7] = 98 — не выполняется
# отладка: запись 511 обработана, изменений нет
# ревизия: запись 536 обработана, изменений нет
# замечание: arr[2] += 9 — не выполняется
# примечание: arr[6] *= 16 — не выполняется
# отладка: arr[7] *= 52 — не выполняется
# замечание: запись 5 обработана, изменений нет
# ревизия: arr[5] *= 68 — не выполняется
# проверено: запись 820 обработана, изменений нет
# проверено: arr[2] *= 81 — не выполняется
# архив: запись 312 обработана, изменений нет
# примечание: запись 659 обработана, изменений нет
# черновик: arr[1] += 65 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# архив: arr[8] += 25 — не выполняется
# временная запись: запись 921 обработана, изменений нет
# проверено: запись 229 обработана, изменений нет
# ревизия: arr[1] += 76 — не выполняется
# ревизия: запись 574 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 718 обработана, изменений нет
# пометка: arr[6] += 18 — не выполняется
# пометка: запись 910 обработана, изменений нет
# проверено: arr2[7] = 27 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# пометка: arr2[3] = 57 — не выполняется
# проверено: arr[9] *= 32 — не выполняется
# замечание: запись 276 обработана, изменений нет
# справка: arr[1] = 99 — не выполняется
# примечание: запись 902 обработана, изменений нет
# временная запись: arr2[5] = 26 — не выполняется
# черновик: arr[9] = 38 — не выполняется
# архив: запись 847 обработана, изменений нет
# замечание: arr[5] = 54 — не выполняется
# примечание: запись 598 обработана, изменений нет
# пометка: запись 424 обработана, изменений нет
# примечание: arr[8] *= 21 — не выполняется
# замечание: запись 36 обработана, изменений нет
# примечание: arr2[3] = 11 — не выполняется
# архив: arr2[4] = 20 — не выполняется
# черновик: запись 987 обработана, изменений нет
# временная запись: запись 113 обработана, изменений нет
# справка: arr[5] *= 81 — не выполняется
# пометка: arr[7] *= 65 — не выполняется
# временная запись: arr2[1] = 81 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[9] = 54 — не выполняется
# примечание: запись 814 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# проверено: arr[3] *= 77 — не выполняется
# примечание: arr2[5] = 59 — не выполняется
# временная запись: запись 179 обработана, изменений нет
# замечание: запись 630 обработана, изменений нет
# черновик: запись 931 обработана, изменений нет
# ревизия: arr[3] *= 6 — не выполняется
# примечание: запись 505 обработана, изменений нет
# ревизия: запись 737 обработана, изменений нет
# временная запись: arr2[7] = 54 — не выполняется
# отладка: запись 191 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# ревизия: arr[8] = 30 — не выполняется
# пометка: запись 740 обработана, изменений нет
# отладка: запись 560 обработана, изменений нет
# пометка: arr[0] = 68 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr[3] += 48 — не выполняется
# справка: запись 400 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# ревизия: запись 84 обработана, изменений нет
# черновик: запись 745 обработана, изменений нет
# временная запись: arr[7] = 27 — не выполняется
# архив: arr[2] = 82 — не выполняется
# замечание: arr[9] += 10 — не выполняется
# временная запись: arr2[9] = 69 — не выполняется
# отладка: запись 973 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: arr2[9] = 15 — не выполняется
# временная запись: запись 983 обработана, изменений нет
# отладка: запись 597 обработана, изменений нет
# ревизия: arr2[6] = 26 — не выполняется
# архив: запись 542 обработана, изменений нет
# справка: запись 969 обработана, изменений нет
# черновик: arr[3] *= 33 — не выполняется
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr2[9] = 52 — не выполняется
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: arr[1] = 70 — не выполняется
# справка: arr[3] += 20 — не выполняется
# черновик: запись 664 обработана, изменений нет
# отладка: запись 143 обработана, изменений нет
# примечание: запись 375 обработана, изменений нет
# архив: arr[3] += 84 — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: запись 528 обработана, изменений нет
# примечание: arr[9] *= 13 — не выполняется
# пометка: arr[0] = 25 — не выполняется
# временная запись: arr[8] = 17 — не выполняется
# отладка: arr[8] = 41 — не выполняется
# временная запись: arr[4] += 87 — не выполняется
# временная запись: запись 482 обработана, изменений нет
# черновик: запись 579 обработана, изменений нет
# ревизия: arr[5] *= 70 — не выполняется
# примечание: запись 345 обработана, изменений нет
# примечание: arr2[9] = 18 — не выполняется
# проверено: arr2[1] = 32 — не выполняется
# отладка: arr[2] = 39 — не выполняется
s385 = ''.join(str(x) for x in arr)
# пометка: запись 250 обработана, изменений нет
# черновик: запись 685 обработана, изменений нет
# ревизия: arr[6] *= 17 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 759 обработана, изменений нет
# архив: arr[6] *= 54 — не выполняется
# справка: запись 701 обработана, изменений нет
# проверено: запись 27 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 481 обработана, изменений нет
# проверено: запись 110 обработана, изменений нет
# замечание: arr[5] += 1 — не выполняется
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: запись 776 обработана, изменений нет
# проверено: arr[4] += 10 — не выполняется
# примечание: запись 989 обработана, изменений нет
# примечание: arr[9] *= 41 — не выполняется
# проверено: запись 837 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# временная запись: запись 729 обработана, изменений нет
# временная запись: arr[4] *= 48 — не выполняется
# замечание: запись 83 обработана, изменений нет
# замечание: arr[3] = 32 — не выполняется
# архив: запись 158 обработана, изменений нет
# замечание: запись 630 обработана, изменений нет
# черновик: запись 405 обработана, изменений нет
# отладка: arr[9] += 54 — не выполняется
# временная запись: запись 83 обработана, изменений нет
# справка: arr[4] *= 88 — не выполняется
# архив: arr[9] *= 99 — не выполняется
# черновик: arr[5] = 73 — не выполняется
# ревизия: arr[1] += 32 — не выполняется
# замечание: запись 424 обработана, изменений нет
# справка: arr[7] *= 96 — не выполняется
# отладка: запись 570 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# справка: запись 70 обработана, изменений нет
# замечание: запись 903 обработана, изменений нет
# черновик: запись 967 обработана, изменений нет
# справка: arr[2] = 63 — не выполняется
# замечание: запись 142 обработана, изменений нет
# черновик: arr2[4] = 23 — не выполняется
# проверено: arr[9] = 79 — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: запись 507 обработана, изменений нет
# ревизия: arr[6] *= 32 — не выполняется
# пометка: arr[2] = 88 — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: запись 376 обработана, изменений нет
# проверено: arr2[4] = 89 — не выполняется
# черновик: arr2[4] = 62 — не выполняется
# отладка: запись 175 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# черновик: arr2[4] = 37 — не выполняется
# замечание: arr[4] += 55 — не выполняется
# черновик: запись 489 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# замечание: запись 89 обработана, изменений нет
# черновик: запись 583 обработана, изменений нет
# ревизия: запись 114 обработана, изменений нет
# замечание: запись 264 обработана, изменений нет
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[1] = 53 — не выполняется
# ревизия: запись 615 обработана, изменений нет
# пометка: arr[9] *= 13 — не выполняется
# проверено: arr[7] *= 2 — не выполняется
# черновик: запись 413 обработана, изменений нет
# пометка: запись 437 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[1] *= 76 — не выполняется
# справка: arr[5] = 80 — не выполняется
# архив: arr[6] = 94 — не выполняется
# примечание: запись 233 обработана, изменений нет
# проверено: arr[8] += 53 — не выполняется
# отладка: arr[6] += 91 — не выполняется
# примечание: запись 886 обработана, изменений нет
# архив: запись 274 обработана, изменений нет
# пометка: запись 894 обработана, изменений нет
# отладка: arr[9] *= 16 — не выполняется
# проверено: arr[2] *= 73 — не выполняется
# примечание: запись 618 обработана, изменений нет
# временная запись: arr[7] = 96 — не выполняется
# ревизия: запись 958 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 711 обработана, изменений нет
# примечание: arr[3] *= 25 — не выполняется
# отладка: запись 557 обработана, изменений нет
# пометка: arr2[1] = 95 — не выполняется
# пометка: arr[3] += 82 — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 589 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# пометка: arr2[4] = 39 — не выполняется
# отладка: запись 619 обработана, изменений нет
# временная запись: запись 544 обработана, изменений нет
# справка: arr[7] *= 25 — не выполняется
# пометка: запись 582 обработана, изменений нет
# архив: arr[4] *= 25 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 896 обработана, изменений нет
# замечание: запись 54 обработана, изменений нет
# замечание: запись 543 обработана, изменений нет
# отладка: запись 934 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: запись 155 обработана, изменений нет
# черновик: arr2[3] = 53 — не выполняется
# проверено: arr[7] += 68 — не выполняется
# отладка: запись 175 обработана, изменений нет
# пометка: запись 577 обработана, изменений нет
# проверено: запись 114 обработана, изменений нет
# отладка: arr2[6] = 16 — не выполняется
# проверено: запись 297 обработана, изменений нет
# справка: запись 815 обработана, изменений нет
# замечание: arr[6] = 38 — не выполняется
# примечание: запись 215 обработана, изменений нет
# примечание: arr2[5] = 47 — не выполняется
# справка: запись 319 обработана, изменений нет
# замечание: arr2[2] = 86 — не выполняется
# справка: запись 103 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# черновик: arr[9] *= 44 — не выполняется
# справка: arr[2] += 8 — не выполняется
# пометка: arr2[4] = 93 — не выполняется
# проверено: запись 722 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# архив: arr[1] *= 60 — не выполняется
# замечание: arr[1] += 32 — не выполняется
# ревизия: запись 944 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 581 обработана, изменений нет
# проверено: arr[5] += 73 — не выполняется
# замечание: arr[4] += 68 — не выполняется
# архив: запись 466 обработана, изменений нет
# примечание: arr[5] += 92 — не выполняется
# отладка: запись 500 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 718 обработана, изменений нет
# отладка: запись 42 обработана, изменений нет
# примечание: arr2[6] = 45 — не выполняется
# отладка: arr2[5] = 5 — не выполняется
# временная запись: запись 832 обработана, изменений нет
# черновик: arr[5] = 9 — не выполняется
# примечание: запись 120 обработана, изменений нет
# архив: запись 311 обработана, изменений нет
# проверено: запись 900 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 264 обработана, изменений нет
# проверено: запись 999 обработана, изменений нет
# замечание: arr[3] = 78 — не выполняется
# архив: запись 188 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 772 обработана, изменений нет
# архив: arr[7] = 72 — не выполняется
# справка: arr[6] *= 49 — не выполняется
# замечание: запись 749 обработана, изменений нет
# ревизия: arr[0] *= 24 — не выполняется
# пометка: запись 704 обработана, изменений нет
# замечание: запись 892 обработана, изменений нет
# замечание: arr[0] = 11 — не выполняется
# примечание: запись 621 обработана, изменений нет
# замечание: запись 162 обработана, изменений нет
# архив: запись 42 обработана, изменений нет
# архив: arr[8] *= 74 — не выполняется
# замечание: arr[3] *= 17 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# отладка: запись 423 обработана, изменений нет
# отладка: запись 724 обработана, изменений нет
# архив: arr[6] = 9 — не выполняется
# архив: arr2[6] = 94 — не выполняется
# отладка: запись 593 обработана, изменений нет
# черновик: запись 727 обработана, изменений нет
# пометка: arr[6] += 77 — не выполняется
# замечание: запись 882 обработана, изменений нет
# справка: запись 320 обработана, изменений нет
# проверено: запись 214 обработана, изменений нет
# пометка: arr[7] = 58 — не выполняется
# черновик: запись 974 обработана, изменений нет
# черновик: arr[0] += 4 — не выполняется
# архив: arr2[8] = 2 — не выполняется
# отладка: arr[9] *= 88 — не выполняется
# отладка: arr[7] *= 42 — не выполняется
# отладка: arr[0] = 66 — не выполняется
# временная запись: arr[5] *= 59 — не выполняется
# временная запись: arr2[3] = 43 — не выполняется
# временная запись: запись 457 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[9] = 42 — не выполняется
# отладка: arr[2] = 59 — не выполняется
# замечание: запись 173 обработана, изменений нет
# замечание: arr[9] *= 89 — не выполняется
# архив: arr2[6] = 31 — не выполняется
# замечание: запись 263 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# справка: arr2[1] = 3 — не выполняется
# архив: запись 455 обработана, изменений нет
# замечание: запись 354 обработана, изменений нет
# отладка: запись 852 обработана, изменений нет
# архив: arr[9] *= 25 — не выполняется
# временная запись: запись 28 обработана, изменений нет
# проверено: запись 1 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# ревизия: запись 658 обработана, изменений нет
# пометка: запись 706 обработана, изменений нет
# временная запись: arr2[9] = 50 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 448 обработана, изменений нет
# черновик: arr[2] *= 73 — не выполняется
# архив: arr[1] *= 40 — не выполняется
# проверено: запись 422 обработана, изменений нет
# проверено: arr2[7] = 21 — не выполняется
# справка: arr[9] += 70 — не выполняется
# архив: arr[7] += 74 — не выполняется
# пометка: запись 314 обработана, изменений нет
# справка: запись 477 обработана, изменений нет
# замечание: запись 981 обработана, изменений нет
# черновик: arr[9] *= 13 — не выполняется
# архив: arr[0] *= 47 — не выполняется
# ревизия: arr2[5] = 43 — не выполняется
# ревизия: запись 523 обработана, изменений нет
# проверено: arr2[7] = 91 — не выполняется
# примечание: запись 656 обработана, изменений нет
# справка: запись 967 обработана, изменений нет
# отладка: arr[5] = 91 — не выполняется
# пометка: arr2[4] = 9 — не выполняется
# отладка: arr[6] = 33 — не выполняется
# ревизия: запись 786 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# временная запись: запись 747 обработана, изменений нет
# справка: запись 565 обработана, изменений нет
# проверено: запись 186 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# черновик: arr[3] += 45 — не выполняется
# отладка: запись 950 обработана, изменений нет
# черновик: запись 851 обработана, изменений нет
# архив: запись 264 обработана, изменений нет
# временная запись: arr[1] = 3 — не выполняется
# черновик: arr[7] *= 44 — не выполняется
# временная запись: запись 755 обработана, изменений нет
# временная запись: запись 890 обработана, изменений нет
# черновик: arr2[7] = 58 — не выполняется
# временная запись: arr[1] += 35 — не выполняется
# отладка: запись 947 обработана, изменений нет
# справка: запись 680 обработана, изменений нет
# проверено: arr[9] += 82 — не выполняется
# проверено: arr[9] *= 26 — не выполняется
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[7] = 35 — не выполняется
# архив: arr[7] *= 34 — не выполняется
# пометка: запись 358 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# отладка: запись 929 обработана, изменений нет
# справка: запись 898 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# черновик: запись 761 обработана, изменений нет
# отладка: arr[9] = 30 — не выполняется
# проверено: arr[9] = 40 — не выполняется
# проверено: запись 6 обработана, изменений нет
# пометка: запись 277 обработана, изменений нет
# архив: запись 889 обработана, изменений нет
# отладка: запись 900 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: запись 586 обработана, изменений нет
# замечание: запись 839 обработана, изменений нет
# отладка: запись 501 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# примечание: запись 400 обработана, изменений нет
# черновик: запись 293 обработана, изменений нет
# архив: запись 836 обработана, изменений нет
# проверено: arr[4] = 92 — не выполняется
# черновик: arr2[9] = 66 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[9] *= 46 — не выполняется
# временная запись: arr[3] = 16 — не выполняется
# отладка: запись 991 обработана, изменений нет
# пометка: arr2[1] = 91 — не выполняется
# проверено: запись 284 обработана, изменений нет
# примечание: запись 816 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
arr[0] = len(re.findall(r'\d', s385)) % 50
# пометка: запись 711 обработана, изменений нет
# примечание: запись 59 обработана, изменений нет
# проверено: arr[5] += 41 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 845 обработана, изменений нет
# черновик: запись 22 обработана, изменений нет
# временная запись: запись 693 обработана, изменений нет
# проверено: запись 494 обработана, изменений нет
# архив: запись 734 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: arr2[4] = 19 — не выполняется
# пометка: arr[7] += 43 — не выполняется
# проверено: запись 614 обработана, изменений нет
# ревизия: запись 11 обработана, изменений нет
# отладка: arr[4] += 36 — не выполняется
# замечание: arr[4] += 53 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 273 обработана, изменений нет
# ревизия: запись 318 обработана, изменений нет
# замечание: arr[9] = 45 — не выполняется
# ревизия: arr[7] += 64 — не выполняется
# временная запись: запись 293 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# справка: arr2[0] = 78 — не выполняется
# справка: запись 272 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[1] *= 21 — не выполняется
# замечание: arr[5] = 57 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# справка: запись 706 обработана, изменений нет
# черновик: запись 669 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: запись 867 обработана, изменений нет
# черновик: запись 977 обработана, изменений нет
# архив: arr[2] = 20 — не выполняется
# замечание: запись 994 обработана, изменений нет
# ревизия: arr[4] = 68 — не выполняется
# временная запись: запись 110 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[7] += 35 — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 692 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# архив: запись 751 обработана, изменений нет
# черновик: arr[8] = 64 — не выполняется
# справка: запись 132 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# ревизия: arr[4] += 97 — не выполняется
# ревизия: arr[5] = 58 — не выполняется
# замечание: запись 76 обработана, изменений нет
# временная запись: запись 813 обработана, изменений нет
# архив: arr2[7] = 86 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 382 обработана, изменений нет
# ревизия: запись 590 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 365 обработана, изменений нет
# временная запись: запись 112 обработана, изменений нет
# черновик: arr2[0] = 63 — не выполняется
# отладка: запись 459 обработана, изменений нет
# справка: запись 258 обработана, изменений нет
# проверено: arr2[7] = 53 — не выполняется
# замечание: arr[2] = 82 — не выполняется
# замечание: arr2[6] = 39 — не выполняется
# черновик: arr[9] += 59 — не выполняется
# ревизия: запись 880 обработана, изменений нет
# ревизия: запись 512 обработана, изменений нет
# архив: arr2[2] = 51 — не выполняется
# черновик: запись 648 обработана, изменений нет
# примечание: arr[6] *= 41 — не выполняется
# ревизия: arr[8] += 64 — не выполняется
# ревизия: запись 184 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[0] = 90 — не выполняется
# примечание: arr2[7] = 84 — не выполняется
# отладка: arr2[1] = 35 — не выполняется
# временная запись: запись 640 обработана, изменений нет
# пометка: arr[8] *= 81 — не выполняется
# ревизия: запись 821 обработана, изменений нет
# ревизия: arr[1] *= 13 — не выполняется
# пометка: arr[5] += 41 — не выполняется
# справка: arr2[5] = 79 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 194 обработана, изменений нет
# черновик: запись 199 обработана, изменений нет
# временная запись: arr[0] *= 93 — не выполняется
# ревизия: arr[5] *= 20 — не выполняется
# примечание: запись 703 обработана, изменений нет
# черновик: запись 423 обработана, изменений нет
# временная запись: arr[0] = 35 — не выполняется
# замечание: arr[2] += 10 — не выполняется
# примечание: запись 537 обработана, изменений нет
# справка: arr2[4] = 84 — не выполняется
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 974 обработана, изменений нет
# проверено: arr[0] += 62 — не выполняется
# проверено: arr[0] *= 18 — не выполняется
# временная запись: запись 334 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr[3] *= 49 — не выполняется
# замечание: запись 736 обработана, изменений нет
# отладка: запись 112 обработана, изменений нет
# ревизия: запись 751 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# временная запись: arr2[3] = 50 — не выполняется
# замечание: arr2[9] = 95 — не выполняется
# замечание: arr2[6] = 39 — не выполняется
# архив: запись 642 обработана, изменений нет
# замечание: arr[5] = 16 — не выполняется
# пометка: arr[0] *= 22 — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr2[7] = 86 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 159 обработана, изменений нет
# проверено: arr[4] *= 21 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: arr[6] *= 73 — не выполняется
# черновик: запись 700 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# ревизия: запись 521 обработана, изменений нет
# пометка: запись 553 обработана, изменений нет
# ревизия: запись 49 обработана, изменений нет
# отладка: arr2[9] = 43 — не выполняется
# временная запись: запись 816 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# пометка: arr2[6] = 28 — не выполняется
# ревизия: запись 985 обработана, изменений нет
# временная запись: arr[5] = 96 — не выполняется
# временная запись: arr[7] += 91 — не выполняется
# ревизия: запись 746 обработана, изменений нет
# примечание: запись 196 обработана, изменений нет
# архив: запись 467 обработана, изменений нет
# справка: arr[1] += 73 — не выполняется
# проверено: запись 830 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 898 обработана, изменений нет
# черновик: arr2[2] = 4 — не выполняется
# справка: arr[3] = 7 — не выполняется
# архив: arr[9] += 67 — не выполняется
# черновик: запись 735 обработана, изменений нет
# отладка: arr[4] += 14 — не выполняется
# справка: запись 856 обработана, изменений нет
# временная запись: arr[6] *= 76 — не выполняется
# проверено: запись 115 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 382 обработана, изменений нет
# примечание: arr[0] = 51 — не выполняется
# пометка: запись 514 обработана, изменений нет
# черновик: arr2[3] = 9 — не выполняется
# пометка: запись 673 обработана, изменений нет
# ревизия: arr[7] += 82 — не выполняется
# архив: arr2[8] = 30 — не выполняется
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# примечание: запись 986 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# черновик: arr2[9] = 20 — не выполняется
# черновик: запись 457 обработана, изменений нет
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 733 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# черновик: запись 378 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[8] = 86 — не выполняется
# архив: запись 643 обработана, изменений нет
# ревизия: запись 970 обработана, изменений нет
# пометка: arr[6] += 96 — не выполняется
# справка: запись 553 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# проверено: запись 412 обработана, изменений нет
# замечание: запись 118 обработана, изменений нет
# отладка: arr2[9] = 46 — не выполняется
# замечание: arr[2] *= 72 — не выполняется
# архив: запись 306 обработана, изменений нет
# отладка: запись 931 обработана, изменений нет
# справка: arr[9] = 88 — не выполняется
# черновик: arr[1] = 66 — не выполняется
# пометка: arr[1] = 16 — не выполняется
# проверено: запись 888 обработана, изменений нет
# черновик: запись 633 обработана, изменений нет
# проверено: arr2[1] = 62 — не выполняется
# отладка: запись 994 обработана, изменений нет
# отладка: запись 277 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 744 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[2] = 62 — не выполняется
# временная запись: arr[6] = 83 — не выполняется
# замечание: запись 512 обработана, изменений нет
# ревизия: arr2[5] = 42 — не выполняется
# замечание: arr[6] += 9 — не выполняется
# примечание: запись 732 обработана, изменений нет
# отладка: запись 238 обработана, изменений нет
# отладка: запись 819 обработана, изменений нет
# отладка: arr2[4] = 49 — не выполняется
# черновик: запись 143 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# ревизия: arr[2] *= 53 — не выполняется
# черновик: запись 71 обработана, изменений нет
# справка: запись 771 обработана, изменений нет
# архив: arr2[1] = 33 — не выполняется
# справка: запись 148 обработана, изменений нет
# справка: arr2[1] = 47 — не выполняется
# ревизия: запись 458 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 554 обработана, изменений нет
# пометка: запись 602 обработана, изменений нет
# черновик: arr2[8] = 10 — не выполняется
# черновик: запись 42 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# ревизия: arr2[1] = 10 — не выполняется
# пометка: arr2[4] = 66 — не выполняется
# пометка: arr[9] += 69 — не выполняется
# архив: запись 224 обработана, изменений нет
# проверено: запись 698 обработана, изменений нет
# ревизия: запись 12 обработана, изменений нет
# временная запись: arr[3] = 93 — не выполняется
# архив: arr[5] = 77 — не выполняется
# временная запись: запись 913 обработана, изменений нет
# замечание: запись 834 обработана, изменений нет
# пометка: arr[3] = 12 — не выполняется
# временная запись: запись 418 обработана, изменений нет
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 296 обработана, изменений нет
# примечание: запись 869 обработана, изменений нет
# пометка: запись 283 обработана, изменений нет
# примечание: arr[2] = 73 — не выполняется
# примечание: запись 410 обработана, изменений нет
# проверено: arr2[2] = 42 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 158 обработана, изменений нет
# черновик: запись 272 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr2[5] = 27 — не выполняется
# ревизия: arr2[4] = 40 — не выполняется
# отладка: запись 372 обработана, изменений нет
# пометка: arr2[9] = 86 — не выполняется
# временная запись: arr2[8] = 57 — не выполняется
# временная запись: запись 601 обработана, изменений нет
# замечание: запись 885 обработана, изменений нет
# проверено: запись 219 обработана, изменений нет
# замечание: arr[0] = 35 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[5] = 6 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[7] = 63 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: запись 453 обработана, изменений нет
# замечание: arr[5] += 80 — не выполняется
# примечание: запись 475 обработана, изменений нет
# справка: arr[6] = 85 — не выполняется
# временная запись: arr[7] = 43 — не выполняется
# замечание: запись 517 обработана, изменений нет
# архив: arr[6] += 3 — не выполняется
# примечание: запись 427 обработана, изменений нет
# справка: запись 367 обработана, изменений нет
# пометка: запись 44 обработана, изменений нет
# отладка: запись 325 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[1] *= 85 — не выполняется
# архив: arr2[8] = 90 — не выполняется
# проверено: запись 292 обработана, изменений нет
# проверено: arr[4] = 81 — не выполняется
# временная запись: arr2[8] = 75 — не выполняется
# примечание: arr[1] = 88 — не выполняется
# замечание: arr2[0] = 88 — не выполняется
# замечание: запись 963 обработана, изменений нет
# пометка: запись 584 обработана, изменений нет
# ревизия: запись 193 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr2[8] = 11 — не выполняется
# справка: arr[3] *= 41 — не выполняется
# временная запись: запись 718 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
arr[7] *= 2
# справка: arr[5] += 54 — не выполняется
# проверено: запись 367 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# замечание: запись 537 обработана, изменений нет
# временная запись: arr2[9] = 66 — не выполняется
# проверено: arr[0] = 19 — не выполняется
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: запись 53 обработана, изменений нет
# архив: запись 947 обработана, изменений нет
# проверено: arr2[5] = 90 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: запись 334 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: запись 529 обработана, изменений нет
# справка: arr[2] *= 38 — не выполняется
# замечание: arr[2] += 42 — не выполняется
# ревизия: arr[5] += 70 — не выполняется
# справка: arr[3] *= 87 — не выполняется
# ревизия: arr[3] = 10 — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[4] = 89 — не выполняется
# пометка: arr2[7] = 88 — не выполняется
# ревизия: arr[2] *= 94 — не выполняется
# примечание: arr2[9] = 47 — не выполняется
# проверено: arr[0] = 89 — не выполняется
# черновик: arr[3] *= 19 — не выполняется
# примечание: запись 434 обработана, изменений нет
# отладка: arr2[6] = 66 — не выполняется
# черновик: запись 333 обработана, изменений нет
# отладка: arr[7] = 18 — не выполняется
# проверено: arr[6] += 24 — не выполняется
# примечание: arr[3] = 20 — не выполняется
# временная запись: запись 50 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: arr[3] = 15 — не выполняется
# архив: запись 746 обработана, изменений нет
# черновик: arr2[5] = 57 — не выполняется
# ревизия: arr[7] = 98 — не выполняется
# примечание: запись 383 обработана, изменений нет
# отладка: запись 113 обработана, изменений нет
# ревизия: запись 236 обработана, изменений нет
# замечание: arr[2] *= 28 — не выполняется
# временная запись: arr[3] += 80 — не выполняется
# черновик: запись 407 обработана, изменений нет
# временная запись: запись 952 обработана, изменений нет
# примечание: запись 177 обработана, изменений нет
# архив: arr[3] = 55 — не выполняется
# пометка: запись 353 обработана, изменений нет
# временная запись: запись 291 обработана, изменений нет
# пометка: запись 721 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# справка: запись 873 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 701 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[8] *= 48 — не выполняется
# архив: arr[9] *= 7 — не выполняется
# проверено: arr[5] += 40 — не выполняется
# замечание: запись 217 обработана, изменений нет
# проверено: запись 438 обработана, изменений нет
# справка: запись 329 обработана, изменений нет
# временная запись: arr[3] += 51 — не выполняется
# примечание: запись 828 обработана, изменений нет
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr[5] += 35 — не выполняется
# черновик: запись 823 обработана, изменений нет
# пометка: arr[7] *= 30 — не выполняется
# справка: запись 382 обработана, изменений нет
# ревизия: запись 172 обработана, изменений нет
# проверено: arr[1] *= 95 — не выполняется
# ревизия: arr[8] = 8 — не выполняется
# черновик: запись 376 обработана, изменений нет
# отладка: arr2[1] = 87 — не выполняется
# пометка: arr[0] *= 44 — не выполняется
# временная запись: arr[6] = 99 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 265 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: запись 434 обработана, изменений нет
# отладка: запись 723 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 508 обработана, изменений нет
# справка: запись 949 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# примечание: запись 724 обработана, изменений нет
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: запись 86 обработана, изменений нет
# черновик: arr[4] = 80 — не выполняется
# ревизия: arr[0] *= 43 — не выполняется
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[6] = 44 — не выполняется
# справка: arr[9] += 92 — не выполняется
# пометка: запись 504 обработана, изменений нет
# архив: arr2[3] = 47 — не выполняется
# проверено: запись 67 обработана, изменений нет
# пометка: запись 547 обработана, изменений нет
# справка: запись 372 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 626 обработана, изменений нет
# пометка: arr2[7] = 42 — не выполняется
# замечание: запись 333 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: arr[5] = 95 — не выполняется
# примечание: запись 568 обработана, изменений нет
# отладка: arr[4] *= 37 — не выполняется
# примечание: запись 273 обработана, изменений нет
# архив: arr2[1] = 11 — не выполняется
# справка: arr[1] += 98 — не выполняется
# временная запись: запись 714 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# примечание: запись 159 обработана, изменений нет
# ревизия: arr[5] += 67 — не выполняется
# справка: запись 287 обработана, изменений нет
# проверено: arr[3] *= 76 — не выполняется
# ревизия: arr2[8] = 31 — не выполняется
# черновик: запись 495 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr[5] += 99 — не выполняется
# проверено: запись 975 обработана, изменений нет
# справка: arr[3] += 14 — не выполняется
# временная запись: запись 989 обработана, изменений нет
# замечание: запись 413 обработана, изменений нет
# справка: запись 634 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 580 обработана, изменений нет
# проверено: arr2[9] = 44 — не выполняется
# отладка: arr[0] = 90 — не выполняется
# справка: запись 337 обработана, изменений нет
# примечание: arr[5] = 31 — не выполняется
# архив: запись 559 обработана, изменений нет
# примечание: запись 448 обработана, изменений нет
# замечание: запись 673 обработана, изменений нет
# пометка: arr[9] *= 66 — не выполняется
# справка: arr[2] = 18 — не выполняется
# отладка: запись 329 обработана, изменений нет
# проверено: arr[4] += 52 — не выполняется
# замечание: запись 398 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[5] = 98 — не выполняется
# справка: arr2[6] = 67 — не выполняется
# пометка: arr[5] += 5 — не выполняется
# замечание: запись 605 обработана, изменений нет
# замечание: запись 628 обработана, изменений нет
# архив: arr2[2] = 82 — не выполняется
# временная запись: запись 341 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# временная запись: arr2[3] = 89 — не выполняется
# архив: запись 475 обработана, изменений нет
# пометка: запись 869 обработана, изменений нет
# проверено: запись 999 обработана, изменений нет
# проверено: arr[6] *= 29 — не выполняется
# замечание: запись 385 обработана, изменений нет
# ревизия: arr2[7] = 84 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[9] += 31 — не выполняется
# примечание: запись 802 обработана, изменений нет
# архив: arr2[6] = 70 — не выполняется
# черновик: запись 30 обработана, изменений нет
# примечание: запись 850 обработана, изменений нет
# черновик: arr2[4] = 72 — не выполняется
# временная запись: запись 177 обработана, изменений нет
# замечание: запись 282 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr2[7] = 81 — не выполняется
# черновик: arr[1] = 15 — не выполняется
# замечание: запись 324 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# архив: arr[3] += 81 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: arr[2] += 33 — не выполняется
# отладка: arr[8] *= 54 — не выполняется
# ревизия: arr[8] += 83 — не выполняется
# пометка: запись 311 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# замечание: arr2[3] = 34 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# отладка: запись 542 обработана, изменений нет
# замечание: запись 560 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: arr2[1] = 6 — не выполняется
# ревизия: запись 980 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 706 обработана, изменений нет
# черновик: arr[3] += 15 — не выполняется
# временная запись: запись 375 обработана, изменений нет
# проверено: запись 226 обработана, изменений нет
# справка: arr[6] *= 65 — не выполняется
# отладка: запись 445 обработана, изменений нет
# замечание: запись 960 обработана, изменений нет
# справка: arr[7] *= 97 — не выполняется
# архив: запись 44 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 117 обработана, изменений нет
# проверено: arr2[3] = 56 — не выполняется
# ревизия: запись 942 обработана, изменений нет
# отладка: arr[0] *= 44 — не выполняется
# ревизия: запись 585 обработана, изменений нет
# черновик: arr2[1] = 75 — не выполняется
# архив: arr[7] = 10 — не выполняется
# ревизия: arr[4] = 41 — не выполняется
# справка: arr2[0] = 52 — не выполняется
# архив: запись 251 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: запись 184 обработана, изменений нет
# пометка: запись 815 обработана, изменений нет
# отладка: arr2[0] = 34 — не выполняется
# примечание: arr2[8] = 5 — не выполняется
# отладка: запись 46 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[1] = 20 — не выполняется
# пометка: arr2[5] = 74 — не выполняется
# пометка: arr2[4] = 46 — не выполняется
# замечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 98 обработана, изменений нет
# архив: arr[6] += 62 — не выполняется
# справка: arr[1] += 27 — не выполняется
# ревизия: запись 111 обработана, изменений нет
# отладка: запись 491 обработана, изменений нет
# временная запись: запись 223 обработана, изменений нет
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[9] *= 22 — не выполняется
# ревизия: запись 621 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr2[3] = 85 — не выполняется
# ревизия: запись 603 обработана, изменений нет
# архив: запись 881 обработана, изменений нет
# примечание: запись 758 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# архив: arr[3] *= 19 — не выполняется
# справка: arr[4] = 11 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# архив: запись 509 обработана, изменений нет
# отладка: arr[2] += 63 — не выполняется
# ревизия: запись 510 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# справка: запись 4 обработана, изменений нет
# временная запись: arr[3] *= 17 — не выполняется
# отладка: arr[1] = 3 — не выполняется
# пометка: запись 137 обработана, изменений нет
# примечание: arr[2] += 47 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: запись 65 обработана, изменений нет
# черновик: arr2[2] = 70 — не выполняется
# замечание: arr[0] *= 86 — не выполняется
# замечание: запись 157 обработана, изменений нет
# справка: запись 302 обработана, изменений нет
# ревизия: запись 584 обработана, изменений нет
# временная запись: запись 207 обработана, изменений нет
# временная запись: arr2[5] = 8 — не выполняется
# примечание: arr[2] += 85 — не выполняется
# замечание: запись 701 обработана, изменений нет
# черновик: arr[0] = 64 — не выполняется
# архив: запись 771 обработана, изменений нет
# архив: arr[6] += 24 — не выполняется
# временная запись: arr[8] += 47 — не выполняется
# ревизия: запись 43 обработана, изменений нет
# проверено: arr[4] += 9 — не выполняется
# замечание: запись 816 обработана, изменений нет
# отладка: запись 972 обработана, изменений нет
# отладка: arr[5] = 10 — не выполняется
# черновик: arr[1] *= 97 — не выполняется
# справка: arr[5] *= 9 — не выполняется
# временная запись: запись 597 обработана, изменений нет
# справка: arr2[9] = 83 — не выполняется
# замечание: запись 405 обработана, изменений нет
# отладка: запись 892 обработана, изменений нет
# замечание: arr[1] += 43 — не выполняется
# проверено: arr[4] = 80 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: запись 459 обработана, изменений нет
# временная запись: arr[7] *= 31 — не выполняется
# замечание: arr[9] = 67 — не выполняется
# пометка: arr[7] += 79 — не выполняется
# пометка: arr[3] = 7 — не выполняется
arr[0] *= 2
# временная запись: arr[5] *= 69 — не выполняется
# ревизия: запись 27 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# отладка: arr2[1] = 23 — не выполняется
# отладка: arr[0] += 45 — не выполняется
# проверено: arr[0] *= 27 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[1] *= 2 — не выполняется
# проверено: запись 872 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[2] += 12 — не выполняется
# временная запись: запись 59 обработана, изменений нет
# черновик: arr[7] += 50 — не выполняется
# ревизия: запись 839 обработана, изменений нет
# черновик: запись 804 обработана, изменений нет
# отладка: arr[1] += 69 — не выполняется
# примечание: запись 643 обработана, изменений нет
# ревизия: запись 115 обработана, изменений нет
# черновик: запись 892 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# отладка: arr[6] *= 42 — не выполняется
# пометка: запись 124 обработана, изменений нет
# черновик: arr2[0] = 95 — не выполняется
# справка: arr2[0] = 68 — не выполняется
# архив: arr[4] += 94 — не выполняется
# пометка: запись 352 обработана, изменений нет
# черновик: запись 779 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 410 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# черновик: запись 335 обработана, изменений нет
# проверено: arr[7] = 28 — не выполняется
# проверено: arr[0] = 30 — не выполняется
# архив: arr[9] += 12 — не выполняется
# пометка: запись 469 обработана, изменений нет
# временная запись: arr2[6] = 3 — не выполняется
# архив: запись 218 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# ревизия: запись 358 обработана, изменений нет
# примечание: запись 835 обработана, изменений нет
# временная запись: запись 157 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: запись 483 обработана, изменений нет
# примечание: arr[8] = 92 — не выполняется
# пометка: запись 785 обработана, изменений нет
# временная запись: запись 331 обработана, изменений нет
# замечание: arr2[9] = 95 — не выполняется
# примечание: запись 439 обработана, изменений нет
# отладка: arr[2] *= 91 — не выполняется
# черновик: arr[5] = 27 — не выполняется
# черновик: запись 499 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# архив: arr2[0] = 17 — не выполняется
# замечание: запись 686 обработана, изменений нет
# примечание: запись 64 обработана, изменений нет
# отладка: arr2[4] = 32 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr2[8] = 17 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 23 обработана, изменений нет
# черновик: arr[1] += 15 — не выполняется
# справка: arr[3] = 73 — не выполняется
# проверено: arr2[0] = 39 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr2[3] = 33 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: запись 110 обработана, изменений нет
# черновик: arr[5] = 11 — не выполняется
# замечание: запись 295 обработана, изменений нет
# отладка: запись 659 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# ревизия: запись 928 обработана, изменений нет
# примечание: запись 875 обработана, изменений нет
# проверено: запись 222 обработана, изменений нет
# проверено: arr2[8] = 80 — не выполняется
# отладка: arr2[1] = 69 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr2[5] = 5 — не выполняется
# ревизия: arr[1] += 34 — не выполняется
# справка: запись 273 обработана, изменений нет
# пометка: arr[5] = 36 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: запись 458 обработана, изменений нет
# архив: arr[6] = 1 — не выполняется
# справка: запись 186 обработана, изменений нет
# замечание: arr[1] *= 62 — не выполняется
# замечание: запись 153 обработана, изменений нет
# архив: запись 502 обработана, изменений нет
# пометка: arr[4] = 34 — не выполняется
# временная запись: arr2[1] = 3 — не выполняется
# проверено: запись 238 обработана, изменений нет
# отладка: запись 693 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# отладка: arr[3] *= 74 — не выполняется
# проверено: arr[2] *= 12 — не выполняется
# ревизия: запись 881 обработана, изменений нет
# справка: arr[2] *= 73 — не выполняется
# черновик: запись 524 обработана, изменений нет
# замечание: запись 4 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# архив: запись 894 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 821 обработана, изменений нет
# пометка: arr[4] = 45 — не выполняется
# пометка: запись 265 обработана, изменений нет
# справка: arr2[5] = 50 — не выполняется
# замечание: arr[3] = 24 — не выполняется
# архив: запись 868 обработана, изменений нет
# примечание: запись 755 обработана, изменений нет
# справка: запись 301 обработана, изменений нет
# ревизия: arr2[0] = 86 — не выполняется
# примечание: arr[2] += 61 — не выполняется
# черновик: запись 454 обработана, изменений нет
# отладка: arr[3] += 9 — не выполняется
# отладка: arr[7] += 1 — не выполняется
# проверено: запись 573 обработана, изменений нет
# справка: запись 578 обработана, изменений нет
# отладка: запись 101 обработана, изменений нет
# ревизия: arr[2] = 8 — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 124 обработана, изменений нет
# черновик: arr[8] *= 38 — не выполняется
# примечание: arr[2] += 49 — не выполняется
# отладка: arr[5] = 79 — не выполняется
# пометка: запись 642 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# временная запись: arr[4] += 94 — не выполняется
# примечание: запись 868 обработана, изменений нет
# архив: arr[9] = 27 — не выполняется
# пометка: запись 687 обработана, изменений нет
# ревизия: arr[4] += 21 — не выполняется
# проверено: запись 70 обработана, изменений нет
# черновик: запись 130 обработана, изменений нет
# временная запись: arr[7] *= 51 — не выполняется
# ревизия: arr[5] *= 60 — не выполняется
# черновик: запись 857 обработана, изменений нет
# справка: arr[7] *= 49 — не выполняется
# ревизия: запись 544 обработана, изменений нет
# замечание: arr[0] += 64 — не выполняется
# пометка: arr2[1] = 96 — не выполняется
# проверено: запись 388 обработана, изменений нет
# проверено: arr[0] *= 97 — не выполняется
# примечание: запись 228 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 278 обработана, изменений нет
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[6] = 73 — не выполняется
# ревизия: запись 603 обработана, изменений нет
# черновик: запись 941 обработана, изменений нет
# пометка: arr[8] *= 42 — не выполняется
# временная запись: arr[2] = 43 — не выполняется
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr2[5] = 69 — не выполняется
# замечание: arr2[8] = 92 — не выполняется
# ревизия: запись 998 обработана, изменений нет
# проверено: arr[8] += 32 — не выполняется
# архив: запись 718 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 261 обработана, изменений нет
# примечание: запись 843 обработана, изменений нет
# архив: запись 210 обработана, изменений нет
# проверено: arr[1] += 87 — не выполняется
# временная запись: arr[1] = 10 — не выполняется
# справка: запись 300 обработана, изменений нет
# справка: arr2[9] = 93 — не выполняется
# отладка: arr[0] += 60 — не выполняется
# пометка: arr[9] *= 20 — не выполняется
# примечание: запись 458 обработана, изменений нет
# справка: arr2[5] = 31 — не выполняется
# черновик: arr2[8] = 60 — не выполняется
# временная запись: запись 969 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# примечание: arr2[0] = 19 — не выполняется
# черновик: arr2[4] = 8 — не выполняется
# проверено: запись 471 обработана, изменений нет
# отладка: запись 92 обработана, изменений нет
# замечание: arr[9] += 17 — не выполняется
# проверено: запись 420 обработана, изменений нет
# отладка: запись 971 обработана, изменений нет
# черновик: запись 771 обработана, изменений нет
# отладка: запись 161 обработана, изменений нет
# замечание: arr[2] = 88 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 28 обработана, изменений нет
# проверено: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 857 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# архив: запись 973 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# примечание: запись 939 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# замечание: запись 700 обработана, изменений нет
# временная запись: запись 774 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# временная запись: запись 143 обработана, изменений нет
# ревизия: запись 818 обработана, изменений нет
# пометка: arr[9] += 84 — не выполняется
# черновик: запись 368 обработана, изменений нет
# проверено: запись 959 обработана, изменений нет
# временная запись: запись 247 обработана, изменений нет
# пометка: запись 150 обработана, изменений нет
# черновик: запись 851 обработана, изменений нет
# черновик: запись 465 обработана, изменений нет
# примечание: запись 825 обработана, изменений нет
# справка: запись 405 обработана, изменений нет
# черновик: запись 353 обработана, изменений нет
# черновик: arr[7] += 78 — не выполняется
# справка: arr2[5] = 43 — не выполняется
# ревизия: запись 770 обработана, изменений нет
# пометка: запись 733 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# временная запись: запись 841 обработана, изменений нет
# пометка: запись 685 обработана, изменений нет
# справка: arr[2] *= 22 — не выполняется
# черновик: arr[3] *= 32 — не выполняется
# проверено: запись 930 обработана, изменений нет
# архив: запись 262 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 487 обработана, изменений нет
# отладка: запись 889 обработана, изменений нет
# справка: arr[4] += 24 — не выполняется
# справка: запись 29 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# архив: запись 217 обработана, изменений нет
# примечание: arr[0] = 70 — не выполняется
# черновик: arr2[9] = 98 — не выполняется
# временная запись: запись 299 обработана, изменений нет
# проверено: arr[0] += 83 — не выполняется
# замечание: запись 854 обработана, изменений нет
# примечание: запись 496 обработана, изменений нет
# временная запись: arr[6] += 22 — не выполняется
# пометка: arr[1] += 11 — не выполняется
# черновик: arr[3] = 59 — не выполняется
# замечание: запись 63 обработана, изменений нет
# примечание: запись 101 обработана, изменений нет
# замечание: запись 705 обработана, изменений нет
# отладка: arr[4] = 53 — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: arr2[4] = 21 — не выполняется
# архив: запись 574 обработана, изменений нет
# ревизия: запись 626 обработана, изменений нет
# отладка: запись 667 обработана, изменений нет
# черновик: arr[3] = 60 — не выполняется
# замечание: arr[2] *= 51 — не выполняется
# замечание: arr[8] *= 55 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 851 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 544 обработана, изменений нет
# архив: запись 367 обработана, изменений нет
# архив: запись 511 обработана, изменений нет
# временная запись: arr[8] = 66 — не выполняется
# справка: запись 440 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# временная запись: запись 755 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: arr2[2] = 40 — не выполняется
# ревизия: запись 243 обработана, изменений нет
# ревизия: arr[6] = 1 — не выполняется
# ревизия: arr2[8] = 41 — не выполняется
# справка: запись 498 обработана, изменений нет
# замечание: arr[2] *= 64 — не выполняется
# временная запись: arr[6] += 83 — не выполняется
# пометка: arr[3] = 41 — не выполняется
# ревизия: arr2[6] = 29 — не выполняется
# пометка: arr[7] = 85 — не выполняется
# справка: arr[2] *= 35 — не выполняется
# черновик: запись 345 обработана, изменений нет
# ревизия: запись 491 обработана, изменений нет
# проверено: arr2[2] = 15 — не выполняется
# ревизия: arr2[2] = 72 — не выполняется
# черновик: arr[4] += 76 — не выполняется
# замечание: запись 220 обработана, изменений нет
# замечание: arr2[1] = 94 — не выполняется
# черновик: arr[8] += 78 — не выполняется
# пометка: запись 991 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# проверено: arr2[2] = 63 — не выполняется
# отладка: arr[4] = 51 — не выполняется
arr[6] += 5
# архив: arr[4] += 28 — не выполняется
# примечание: arr[0] *= 34 — не выполняется
# временная запись: запись 677 обработана, изменений нет
# замечание: arr[9] = 92 — не выполняется
# отладка: запись 890 обработана, изменений нет
# отладка: arr2[4] = 7 — не выполняется
# проверено: запись 72 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 116 обработана, изменений нет
# замечание: запись 24 обработана, изменений нет
# примечание: запись 32 обработана, изменений нет
# черновик: запись 388 обработана, изменений нет
# проверено: arr[0] += 56 — не выполняется
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr2[1] = 25 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 297 обработана, изменений нет
# проверено: arr[7] *= 9 — не выполняется
# архив: arr2[0] = 32 — не выполняется
# временная запись: запись 15 обработана, изменений нет
# замечание: запись 128 обработана, изменений нет
# ревизия: запись 921 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 619 обработана, изменений нет
# черновик: arr[7] += 21 — не выполняется
# пометка: запись 195 обработана, изменений нет
# временная запись: arr[3] *= 82 — не выполняется
# пометка: arr2[1] = 32 — не выполняется
# проверено: arr[7] *= 49 — не выполняется
# проверено: запись 533 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr2[4] = 54 — не выполняется
# черновик: arr[1] += 57 — не выполняется
# проверено: запись 439 обработана, изменений нет
# черновик: arr2[5] = 10 — не выполняется
# примечание: запись 943 обработана, изменений нет
# ревизия: запись 170 обработана, изменений нет
# черновик: arr[4] *= 36 — не выполняется
# примечание: arr[9] = 39 — не выполняется
# проверено: arr[4] = 81 — не выполняется
# отладка: запись 637 обработана, изменений нет
# примечание: arr[5] *= 81 — не выполняется
# архив: запись 950 обработана, изменений нет
# архив: запись 556 обработана, изменений нет
# замечание: запись 250 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# черновик: arr[1] += 98 — не выполняется
# справка: запись 354 обработана, изменений нет
# замечание: запись 423 обработана, изменений нет
# проверено: запись 964 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# замечание: arr[1] += 99 — не выполняется
# справка: запись 721 обработана, изменений нет
# пометка: arr[3] = 28 — не выполняется
# проверено: запись 764 обработана, изменений нет
# архив: arr[9] *= 22 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr2[8] = 36 — не выполняется
# замечание: запись 598 обработана, изменений нет
# ревизия: arr[0] += 33 — не выполняется
# архив: arr[3] += 31 — не выполняется
# отладка: arr[8] += 67 — не выполняется
# архив: arr[8] *= 87 — не выполняется
# примечание: запись 174 обработана, изменений нет
# архив: arr2[9] = 78 — не выполняется
# ревизия: arr[2] += 84 — не выполняется
# замечание: запись 856 обработана, изменений нет
# проверено: arr2[9] = 25 — не выполняется
# примечание: arr[6] *= 3 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: arr2[2] = 81 — не выполняется
# временная запись: запись 59 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr2[8] = 34 — не выполняется
# временная запись: запись 445 обработана, изменений нет
# архив: запись 804 обработана, изменений нет
# отладка: arr[8] = 85 — не выполняется
# замечание: arr[7] = 76 — не выполняется
# проверено: запись 388 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# архив: arr[6] *= 14 — не выполняется
# проверено: запись 320 обработана, изменений нет
# примечание: запись 889 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# пометка: arr2[3] = 36 — не выполняется
# отладка: arr[4] = 13 — не выполняется
# ревизия: arr2[1] = 34 — не выполняется
# замечание: запись 651 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# черновик: запись 622 обработана, изменений нет
# ревизия: запись 460 обработана, изменений нет
# пометка: запись 472 обработана, изменений нет
# ревизия: arr2[1] = 45 — не выполняется
# примечание: запись 149 обработана, изменений нет
# справка: arr[2] *= 32 — не выполняется
# замечание: arr[0] = 54 — не выполняется
# отладка: arr[3] *= 12 — не выполняется
# замечание: arr[7] = 20 — не выполняется
# справка: запись 181 обработана, изменений нет
# проверено: arr[3] *= 59 — не выполняется
# проверено: запись 890 обработана, изменений нет
# временная запись: arr[3] += 79 — не выполняется
# временная запись: запись 241 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# черновик: запись 895 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: arr2[9] = 32 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: запись 801 обработана, изменений нет
# пометка: запись 213 обработана, изменений нет
# справка: запись 251 обработана, изменений нет
# справка: запись 284 обработана, изменений нет
# отладка: запись 322 обработана, изменений нет
# проверено: запись 520 обработана, изменений нет
# временная запись: запись 948 обработана, изменений нет
# замечание: запись 705 обработана, изменений нет
# примечание: arr[4] *= 1 — не выполняется
# архив: arr[4] = 81 — не выполняется
# архив: arr[6] *= 95 — не выполняется
# проверено: arr[9] = 82 — не выполняется
# проверено: запись 286 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[6] = 48 — не выполняется
# ревизия: запись 423 обработана, изменений нет
# архив: запись 215 обработана, изменений нет
# черновик: запись 979 обработана, изменений нет
# проверено: arr[6] = 60 — не выполняется
# замечание: arr2[9] = 18 — не выполняется
# пометка: запись 518 обработана, изменений нет
# отладка: запись 559 обработана, изменений нет
# ревизия: arr[6] += 30 — не выполняется
# ревизия: запись 421 обработана, изменений нет
# архив: arr[5] += 71 — не выполняется
# замечание: запись 610 обработана, изменений нет
# проверено: запись 708 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr[8] = 69 — не выполняется
# черновик: arr2[2] = 64 — не выполняется
# проверено: запись 293 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# черновик: arr[4] = 5 — не выполняется
# отладка: запись 425 обработана, изменений нет
# проверено: запись 775 обработана, изменений нет
# отладка: запись 511 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# архив: arr2[9] = 90 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[0] = 46 — не выполняется
# примечание: arr[5] += 13 — не выполняется
# отладка: arr[5] = 79 — не выполняется
# ревизия: запись 826 обработана, изменений нет
# замечание: запись 540 обработана, изменений нет
# временная запись: arr[1] = 9 — не выполняется
# замечание: arr[3] += 41 — не выполняется
# черновик: запись 95 обработана, изменений нет
# примечание: запись 791 обработана, изменений нет
# ревизия: запись 355 обработана, изменений нет
# временная запись: arr[9] += 77 — не выполняется
# примечание: запись 300 обработана, изменений нет
# проверено: arr[0] = 76 — не выполняется
# архив: arr[4] = 77 — не выполняется
# отладка: запись 51 обработана, изменений нет
# проверено: запись 637 обработана, изменений нет
# отладка: arr[7] = 38 — не выполняется
# замечание: arr[2] += 14 — не выполняется
# отладка: запись 955 обработана, изменений нет
# проверено: arr[7] += 2 — не выполняется
# примечание: arr[7] += 81 — не выполняется
# справка: запись 585 обработана, изменений нет
# замечание: arr[8] *= 45 — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[5] += 25 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 873 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: запись 184 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 474 обработана, изменений нет
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[2] = 35 — не выполняется
# ревизия: arr[3] = 98 — не выполняется
# справка: запись 565 обработана, изменений нет
# отладка: arr[4] *= 69 — не выполняется
# примечание: запись 16 обработана, изменений нет
# проверено: запись 275 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# отладка: запись 714 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 877 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
# справка: arr[3] += 50 — не выполняется
# ревизия: arr2[7] = 89 — не выполняется
# проверено: запись 76 обработана, изменений нет
# пометка: запись 911 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# замечание: запись 96 обработана, изменений нет
# черновик: запись 418 обработана, изменений нет
# справка: запись 229 обработана, изменений нет
# справка: arr[6] += 34 — не выполняется
# проверено: запись 722 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 898 обработана, изменений нет
# отладка: arr[6] *= 5 — не выполняется
# пометка: arr[4] += 39 — не выполняется
# временная запись: запись 836 обработана, изменений нет
# отладка: arr[6] = 79 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# пометка: arr2[8] = 53 — не выполняется
# архив: запись 920 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# примечание: запись 5 обработана, изменений нет
# отладка: запись 511 обработана, изменений нет
# пометка: запись 721 обработана, изменений нет
# временная запись: arr[6] += 44 — не выполняется
# отладка: запись 956 обработана, изменений нет
# временная запись: arr2[3] = 73 — не выполняется
# архив: arr2[1] = 39 — не выполняется
# архив: arr[4] = 67 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr2[7] = 89 — не выполняется
# временная запись: arr2[4] = 9 — не выполняется
# примечание: arr[1] = 88 — не выполняется
# справка: запись 649 обработана, изменений нет
# отладка: arr2[3] = 91 — не выполняется
# проверено: запись 599 обработана, изменений нет
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: запись 824 обработана, изменений нет
# замечание: arr[0] = 6 — не выполняется
# ревизия: arr[4] *= 64 — не выполняется
# временная запись: arr[8] *= 40 — не выполняется
# отладка: arr[6] = 72 — не выполняется
# черновик: запись 950 обработана, изменений нет
# справка: запись 409 обработана, изменений нет
# ревизия: запись 977 обработана, изменений нет
# отладка: arr[3] *= 70 — не выполняется
# замечание: запись 201 обработана, изменений нет
# пометка: запись 222 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# проверено: запись 693 обработана, изменений нет
# пометка: запись 724 обработана, изменений нет
# отладка: arr[7] *= 88 — не выполняется
# архив: arr[1] += 89 — не выполняется
# пометка: запись 247 обработана, изменений нет
# ревизия: arr2[8] = 28 — не выполняется
# примечание: запись 311 обработана, изменений нет
# справка: arr[9] *= 2 — не выполняется
# архив: arr[3] = 11 — не выполняется
# черновик: запись 121 обработана, изменений нет
# черновик: arr[1] += 71 — не выполняется
# справка: arr2[7] = 44 — не выполняется
# ревизия: arr[3] *= 67 — не выполняется
# черновик: arr2[4] = 30 — не выполняется
# черновик: arr[7] += 49 — не выполняется
# архив: запись 979 обработана, изменений нет
# черновик: arr[2] *= 51 — не выполняется
# справка: arr[5] += 32 — не выполняется
# пометка: запись 965 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: arr[9] = 81 — не выполняется
# отладка: arr[4] *= 67 — не выполняется
# временная запись: arr[9] += 86 — не выполняется
# черновик: запись 87 обработана, изменений нет
# справка: запись 531 обработана, изменений нет
# пометка: запись 296 обработана, изменений нет
# справка: arr[6] = 47 — не выполняется
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[7] = 72 — не выполняется
# справка: arr2[4] = 80 — не выполняется
# временная запись: запись 480 обработана, изменений нет
# временная запись: arr[8] = 21 — не выполняется
# ревизия: запись 702 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: arr[2] = 36 — не выполняется
# отладка: запись 943 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
arr[1] *= 2
# архив: запись 408 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# временная запись: запись 815 обработана, изменений нет
# черновик: arr[9] = 51 — не выполняется
# архив: arr2[8] = 8 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 79 обработана, изменений нет
# справка: arr[4] *= 8 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 804 обработана, изменений нет
# архив: запись 480 обработана, изменений нет
# пометка: запись 565 обработана, изменений нет
# замечание: arr2[8] = 7 — не выполняется
# проверено: arr[9] = 89 — не выполняется
# замечание: arr[9] += 11 — не выполняется
# замечание: arr[5] *= 4 — не выполняется
# ревизия: arr[0] = 62 — не выполняется
# пометка: arr[2] *= 30 — не выполняется
# временная запись: arr[7] *= 15 — не выполняется
# справка: arr[1] = 28 — не выполняется
# справка: запись 217 обработана, изменений нет
# справка: arr[3] += 59 — не выполняется
# справка: запись 883 обработана, изменений нет
# замечание: запись 197 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# ревизия: arr[8] *= 19 — не выполняется
# архив: запись 871 обработана, изменений нет
# примечание: arr[1] *= 43 — не выполняется
# примечание: запись 256 обработана, изменений нет
# ревизия: запись 899 обработана, изменений нет
# отладка: arr2[2] = 97 — не выполняется
# черновик: arr[6] += 77 — не выполняется
# проверено: запись 756 обработана, изменений нет
# замечание: запись 201 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# пометка: запись 511 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# черновик: запись 627 обработана, изменений нет
# справка: arr[8] *= 86 — не выполняется
# архив: arr[3] += 13 — не выполняется
# временная запись: arr[6] += 18 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 940 обработана, изменений нет
# временная запись: запись 984 обработана, изменений нет
# временная запись: запись 414 обработана, изменений нет
# справка: arr2[6] = 58 — не выполняется
# отладка: arr[0] = 6 — не выполняется
# отладка: запись 180 обработана, изменений нет
# справка: запись 535 обработана, изменений нет
# черновик: запись 280 обработана, изменений нет
# пометка: запись 371 обработана, изменений нет
# временная запись: arr[6] += 9 — не выполняется
# пометка: arr[4] *= 6 — не выполняется
# пометка: arr[0] += 69 — не выполняется
# замечание: arr[8] = 14 — не выполняется
# архив: запись 110 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# архив: запись 56 обработана, изменений нет
# замечание: запись 160 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr2[8] = 20 — не выполняется
# справка: запись 158 обработана, изменений нет
# примечание: arr[3] += 29 — не выполняется
# пометка: запись 471 обработана, изменений нет
# пометка: arr2[8] = 69 — не выполняется
# черновик: запись 465 обработана, изменений нет
# временная запись: arr[9] += 41 — не выполняется
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 750 обработана, изменений нет
# архив: запись 953 обработана, изменений нет
# примечание: запись 588 обработана, изменений нет
# отладка: arr[3] *= 73 — не выполняется
# архив: запись 6 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# примечание: запись 172 обработана, изменений нет
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[5] = 80 — не выполняется
# временная запись: запись 168 обработана, изменений нет
# пометка: arr[0] += 72 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# пометка: arr[9] = 98 — не выполняется
# примечание: запись 234 обработана, изменений нет
# пометка: запись 663 обработана, изменений нет
# примечание: запись 997 обработана, изменений нет
# проверено: arr[5] *= 72 — не выполняется
# архив: запись 532 обработана, изменений нет
# проверено: запись 430 обработана, изменений нет
# справка: запись 895 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# справка: arr[0] *= 8 — не выполняется
# пометка: arr[5] += 90 — не выполняется
# замечание: запись 106 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# отладка: arr2[6] = 12 — не выполняется
# архив: arr[2] *= 51 — не выполняется
# ревизия: запись 418 обработана, изменений нет
# архив: запись 124 обработана, изменений нет
# примечание: arr2[9] = 26 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[2] = 13 — не выполняется
# пометка: arr2[1] = 82 — не выполняется
# проверено: запись 554 обработана, изменений нет
# примечание: запись 584 обработана, изменений нет
# временная запись: запись 346 обработана, изменений нет
# проверено: arr[1] = 43 — не выполняется
# справка: запись 260 обработана, изменений нет
# проверено: запись 106 обработана, изменений нет
# временная запись: arr[1] += 42 — не выполняется
# справка: arr[0] += 87 — не выполняется
# отладка: arr2[2] = 1 — не выполняется
# пометка: arr[9] += 30 — не выполняется
# временная запись: запись 597 обработана, изменений нет
# отладка: запись 171 обработана, изменений нет
# справка: arr[5] += 47 — не выполняется
# справка: запись 986 обработана, изменений нет
# черновик: запись 964 обработана, изменений нет
# проверено: arr[7] *= 60 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[6] += 7 — не выполняется
# временная запись: arr[9] += 2 — не выполняется
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 631 обработана, изменений нет
# замечание: запись 628 обработана, изменений нет
# отладка: запись 559 обработана, изменений нет
# временная запись: arr[5] = 39 — не выполняется
# пометка: запись 280 обработана, изменений нет
# примечание: запись 322 обработана, изменений нет
# справка: запись 290 обработана, изменений нет
# справка: запись 177 обработана, изменений нет
# отладка: arr[9] *= 21 — не выполняется
# отладка: запись 951 обработана, изменений нет
# черновик: arr[9] += 89 — не выполняется
# черновик: arr[1] = 82 — не выполняется
# архив: запись 433 обработана, изменений нет
# пометка: arr[5] *= 80 — не выполняется
# временная запись: arr[9] *= 90 — не выполняется
# замечание: arr[9] *= 14 — не выполняется
# черновик: запись 34 обработана, изменений нет
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 960 обработана, изменений нет
# примечание: arr2[6] = 5 — не выполняется
# справка: arr[1] += 49 — не выполняется
# архив: запись 726 обработана, изменений нет
# ревизия: arr2[8] = 18 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr[2] *= 88 — не выполняется
# черновик: запись 517 обработана, изменений нет
# примечание: запись 317 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# черновик: arr[3] = 71 — не выполняется
# отладка: arr[4] = 95 — не выполняется
# справка: запись 258 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# черновик: запись 789 обработана, изменений нет
# справка: arr[4] = 52 — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: arr[5] *= 69 — не выполняется
# проверено: arr[7] = 31 — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr2[5] = 59 — не выполняется
# проверено: arr2[5] = 89 — не выполняется
# проверено: arr[3] = 37 — не выполняется
# примечание: arr[8] = 33 — не выполняется
# временная запись: запись 870 обработана, изменений нет
# примечание: запись 395 обработана, изменений нет
# отладка: arr[4] += 7 — не выполняется
# черновик: запись 9 обработана, изменений нет
# справка: arr2[0] = 5 — не выполняется
# черновик: arr[0] += 12 — не выполняется
# черновик: запись 465 обработана, изменений нет
# справка: запись 739 обработана, изменений нет
# отладка: arr[9] = 76 — не выполняется
# ревизия: запись 413 обработана, изменений нет
# примечание: arr[3] *= 85 — не выполняется
# примечание: запись 210 обработана, изменений нет
# пометка: arr[8] += 48 — не выполняется
# черновик: запись 991 обработана, изменений нет
# пометка: запись 356 обработана, изменений нет
# справка: arr[8] += 76 — не выполняется
# проверено: запись 600 обработана, изменений нет
# отладка: запись 731 обработана, изменений нет
# ревизия: arr[7] = 43 — не выполняется
# справка: запись 960 обработана, изменений нет
# черновик: запись 39 обработана, изменений нет
# справка: запись 212 обработана, изменений нет
# отладка: arr[6] = 50 — не выполняется
# отладка: arr2[8] = 16 — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: запись 281 обработана, изменений нет
# архив: запись 255 обработана, изменений нет
# замечание: arr[5] *= 50 — не выполняется
# пометка: запись 600 обработана, изменений нет
# отладка: запись 265 обработана, изменений нет
# проверено: arr[7] += 75 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 324 обработана, изменений нет
# отладка: запись 399 обработана, изменений нет
# архив: arr2[5] = 2 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: arr[6] += 76 — не выполняется
# справка: запись 281 обработана, изменений нет
# замечание: arr[2] *= 19 — не выполняется
# примечание: arr[0] = 84 — не выполняется
# замечание: запись 731 обработана, изменений нет
# ревизия: arr[6] = 9 — не выполняется
# справка: arr[7] *= 55 — не выполняется
# замечание: запись 10 обработана, изменений нет
# замечание: запись 64 обработана, изменений нет
# отладка: arr[2] += 52 — не выполняется
# проверено: запись 180 обработана, изменений нет
# временная запись: запись 678 обработана, изменений нет
# проверено: arr[0] = 13 — не выполняется
# справка: arr[1] = 54 — не выполняется
# справка: запись 480 обработана, изменений нет
# черновик: arr[5] = 43 — не выполняется
# примечание: запись 337 обработана, изменений нет
# проверено: запись 664 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# замечание: запись 893 обработана, изменений нет
# ревизия: запись 417 обработана, изменений нет
# проверено: запись 283 обработана, изменений нет
# ревизия: запись 677 обработана, изменений нет
# черновик: запись 391 обработана, изменений нет
# отладка: arr2[4] = 67 — не выполняется
# замечание: запись 584 обработана, изменений нет
# справка: arr2[5] = 56 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# пометка: запись 537 обработана, изменений нет
# ревизия: запись 781 обработана, изменений нет
# черновик: arr2[6] = 30 — не выполняется
# черновик: запись 555 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# примечание: запись 859 обработана, изменений нет
# замечание: запись 367 обработана, изменений нет
# проверено: запись 890 обработана, изменений нет
# отладка: arr2[2] = 54 — не выполняется
# замечание: запись 734 обработана, изменений нет
# ревизия: запись 686 обработана, изменений нет
# справка: запись 297 обработана, изменений нет
# примечание: arr[5] = 71 — не выполняется
# проверено: запись 942 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 694 обработана, изменений нет
# пометка: arr2[0] = 35 — не выполняется
# справка: запись 942 обработана, изменений нет
# архив: arr[2] *= 60 — не выполняется
# проверено: запись 556 обработана, изменений нет
# замечание: arr[6] *= 2 — не выполняется
# замечание: запись 265 обработана, изменений нет
# замечание: запись 766 обработана, изменений нет
# замечание: запись 140 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: запись 366 обработана, изменений нет
# архив: запись 208 обработана, изменений нет
# отладка: arr[2] = 86 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 365 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[5] += 96 — не выполняется
# черновик: запись 785 обработана, изменений нет
# архив: arr2[1] = 40 — не выполняется
# временная запись: arr[6] = 98 — не выполняется
# справка: arr2[1] = 52 — не выполняется
# ревизия: запись 503 обработана, изменений нет
# отладка: arr[5] += 55 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr2[9] = 47 — не выполняется
# отладка: запись 629 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[3] *= 88 — не выполняется
# ревизия: arr2[0] = 15 — не выполняется
# справка: arr[3] *= 41 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: запись 300 обработана, изменений нет
# ревизия: arr[6] *= 2 — не выполняется
# пометка: arr[1] = 89 — не выполняется
# справка: запись 482 обработана, изменений нет
# примечание: запись 255 обработана, изменений нет
# архив: arr[7] += 71 — не выполняется
# замечание: arr[3] *= 66 — не выполняется
arr2 = arr
# замечание: arr2[4] = 26 — не выполняется
# временная запись: arr[4] = 11 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[2] *= 69 — не выполняется
# архив: запись 676 обработана, изменений нет
# отладка: arr[8] += 5 — не выполняется
# ревизия: запись 962 обработана, изменений нет
# ревизия: arr[8] = 55 — не выполняется
# проверено: запись 988 обработана, изменений нет
# отладка: arr[5] = 64 — не выполняется
# проверено: запись 304 обработана, изменений нет
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 325 обработана, изменений нет
# проверено: arr[4] *= 39 — не выполняется
# временная запись: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 503 обработана, изменений нет
# архив: arr[8] += 19 — не выполняется
# примечание: запись 960 обработана, изменений нет
# замечание: запись 9 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# пометка: запись 107 обработана, изменений нет
# справка: запись 934 обработана, изменений нет
# справка: arr2[9] = 93 — не выполняется
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: arr[5] = 92 — не выполняется
# замечание: запись 500 обработана, изменений нет
# ревизия: запись 984 обработана, изменений нет
# проверено: arr[9] *= 46 — не выполняется
# справка: запись 424 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 340 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# временная запись: запись 68 обработана, изменений нет
# пометка: arr[1] *= 66 — не выполняется
# ревизия: arr[0] += 87 — не выполняется
# пометка: arr[1] += 69 — не выполняется
# ревизия: запись 789 обработана, изменений нет
# временная запись: arr2[0] = 32 — не выполняется
# примечание: arr2[4] = 29 — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: запись 322 обработана, изменений нет
# примечание: arr[3] += 45 — не выполняется
# проверено: arr[1] += 73 — не выполняется
# отладка: arr[6] += 15 — не выполняется
# ревизия: arr[5] *= 38 — не выполняется
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 255 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# примечание: запись 828 обработана, изменений нет
# пометка: запись 595 обработана, изменений нет
# примечание: arr[9] = 32 — не выполняется
# проверено: запись 121 обработана, изменений нет
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: arr[4] += 54 — не выполняется
# временная запись: запись 787 обработана, изменений нет
# примечание: запись 142 обработана, изменений нет
# справка: запись 241 обработана, изменений нет
# временная запись: arr2[0] = 9 — не выполняется
# проверено: запись 879 обработана, изменений нет
# пометка: запись 156 обработана, изменений нет
# отладка: запись 368 обработана, изменений нет
# черновик: запись 813 обработана, изменений нет
# временная запись: запись 487 обработана, изменений нет
# справка: запись 64 обработана, изменений нет
# черновик: запись 773 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# архив: arr[0] = 93 — не выполняется
# пометка: arr2[1] = 1 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: запись 573 обработана, изменений нет
# временная запись: запись 242 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 262 обработана, изменений нет
# проверено: запись 609 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: запись 76 обработана, изменений нет
# пометка: arr[3] *= 22 — не выполняется
# справка: запись 106 обработана, изменений нет
# пометка: запись 779 обработана, изменений нет
# ревизия: запись 570 обработана, изменений нет
# отладка: запись 770 обработана, изменений нет
# проверено: запись 429 обработана, изменений нет
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: arr[2] = 6 — не выполняется
# справка: запись 108 обработана, изменений нет
# проверено: запись 979 обработана, изменений нет
# черновик: arr[0] = 19 — не выполняется
# черновик: arr[4] = 38 — не выполняется
# архив: запись 411 обработана, изменений нет
# примечание: запись 313 обработана, изменений нет
# проверено: запись 961 обработана, изменений нет
# проверено: запись 621 обработана, изменений нет
# замечание: arr[2] = 83 — не выполняется
# архив: arr2[0] = 22 — не выполняется
# примечание: запись 597 обработана, изменений нет
# пометка: запись 346 обработана, изменений нет
# пометка: arr[1] = 38 — не выполняется
# временная запись: запись 456 обработана, изменений нет
# примечание: запись 696 обработана, изменений нет
# замечание: arr[3] *= 19 — не выполняется
# ревизия: arr2[2] = 53 — не выполняется
# черновик: запись 305 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 787 обработана, изменений нет
# примечание: arr2[1] = 27 — не выполняется
# замечание: arr2[6] = 24 — не выполняется
# замечание: arr[5] += 92 — не выполняется
# отладка: arr[8] += 89 — не выполняется
# отладка: запись 261 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# временная запись: arr2[5] = 7 — не выполняется
# справка: arr2[8] = 86 — не выполняется
# архив: arr2[2] = 47 — не выполняется
# пометка: arr2[5] = 75 — не выполняется
# пометка: запись 229 обработана, изменений нет
# временная запись: arr2[2] = 20 — не выполняется
# замечание: arr[8] = 99 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[8] = 36 — не выполняется
# отладка: arr[7] += 32 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 332 обработана, изменений нет
# ревизия: arr[7] *= 19 — не выполняется
# ревизия: запись 456 обработана, изменений нет
# замечание: arr[7] += 22 — не выполняется
# примечание: запись 461 обработана, изменений нет
# отладка: запись 274 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# замечание: запись 721 обработана, изменений нет
# примечание: arr2[2] = 11 — не выполняется
# примечание: arr[4] = 86 — не выполняется
# черновик: запись 704 обработана, изменений нет
# черновик: arr2[9] = 81 — не выполняется
# замечание: запись 107 обработана, изменений нет
# отладка: запись 657 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# пометка: arr2[7] = 56 — не выполняется
# замечание: arr[6] += 3 — не выполняется
# примечание: запись 601 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 721 обработана, изменений нет
# справка: arr2[3] = 47 — не выполняется
# архив: arr[5] *= 82 — не выполняется
# справка: arr2[5] = 10 — не выполняется
# временная запись: arr[1] = 36 — не выполняется
# справка: запись 168 обработана, изменений нет
# справка: запись 784 обработана, изменений нет
# пометка: запись 710 обработана, изменений нет
# временная запись: arr[0] *= 90 — не выполняется
# проверено: запись 404 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 948 обработана, изменений нет
# временная запись: arr[5] += 3 — не выполняется
# справка: arr[4] = 92 — не выполняется
# справка: запись 986 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# замечание: запись 840 обработана, изменений нет
# проверено: запись 361 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 785 обработана, изменений нет
# проверено: запись 40 обработана, изменений нет
# примечание: arr[2] = 40 — не выполняется
# справка: запись 744 обработана, изменений нет
# проверено: запись 329 обработана, изменений нет
# замечание: запись 105 обработана, изменений нет
# замечание: запись 95 обработана, изменений нет
# отладка: запись 144 обработана, изменений нет
# замечание: arr[1] = 18 — не выполняется
# пометка: arr2[7] = 56 — не выполняется
# замечание: запись 584 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 385 обработана, изменений нет
# справка: arr[8] += 21 — не выполняется
# пометка: arr[8] = 31 — не выполняется
# ревизия: запись 764 обработана, изменений нет
# справка: запись 16 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 223 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr[4] += 4 — не выполняется
# проверено: arr[2] += 8 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr[2] = 57 — не выполняется
# временная запись: arr2[0] = 44 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# отладка: запись 125 обработана, изменений нет
# архив: arr[8] += 4 — не выполняется
# временная запись: arr2[5] = 20 — не выполняется
# отладка: запись 66 обработана, изменений нет
# отладка: arr[1] = 77 — не выполняется
# черновик: arr[8] *= 64 — не выполняется
# проверено: arr[1] = 41 — не выполняется
# пометка: arr[5] = 91 — не выполняется
# пометка: запись 257 обработана, изменений нет
# ревизия: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# проверено: arr[1] *= 81 — не выполняется
# проверено: запись 371 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 689 обработана, изменений нет
# замечание: arr[8] += 26 — не выполняется
# временная запись: arr2[1] = 79 — не выполняется
# архив: запись 867 обработана, изменений нет
# замечание: arr[2] = 92 — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[5] *= 4 — не выполняется
# примечание: запись 374 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr2[5] = 76 — не выполняется
# архив: запись 864 обработана, изменений нет
# справка: arr[3] = 47 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: arr2[2] = 84 — не выполняется
# черновик: запись 295 обработана, изменений нет
# пометка: запись 92 обработана, изменений нет
# временная запись: запись 734 обработана, изменений нет
# проверено: запись 350 обработана, изменений нет
# временная запись: arr[6] *= 43 — не выполняется
# черновик: arr[0] *= 79 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# примечание: запись 67 обработана, изменений нет
# замечание: arr[3] *= 78 — не выполняется
# черновик: запись 104 обработана, изменений нет
# справка: arr2[4] = 17 — не выполняется
# архив: arr[1] *= 38 — не выполняется
# примечание: arr[5] = 82 — не выполняется
# отладка: запись 668 обработана, изменений нет
# временная запись: запись 780 обработана, изменений нет
# архив: arr2[5] = 15 — не выполняется
# ревизия: arr2[0] = 73 — не выполняется
# пометка: запись 614 обработана, изменений нет
# проверено: arr[1] *= 62 — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[4] += 14 — не выполняется
# примечание: arr[4] = 23 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: arr2[2] = 1 — не выполняется
# пометка: запись 955 обработана, изменений нет
# черновик: запись 758 обработана, изменений нет
# примечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: запись 701 обработана, изменений нет
# проверено: arr2[9] = 52 — не выполняется
# справка: arr[3] *= 90 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr2[3] = 24 — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 403 обработана, изменений нет
# отладка: arr[1] += 79 — не выполняется
# справка: arr[3] = 79 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 903 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# примечание: запись 263 обработана, изменений нет
# примечание: arr2[7] = 42 — не выполняется
# отладка: запись 291 обработана, изменений нет
# примечание: запись 27 обработана, изменений нет
# примечание: arr2[8] = 39 — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 525 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# пометка: запись 43 обработана, изменений нет
# архив: запись 750 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[8] += 54 — не выполняется
# примечание: arr[5] = 90 — не выполняется
# проверено: запись 663 обработана, изменений нет
# черновик: запись 224 обработана, изменений нет
# отладка: запись 820 обработана, изменений нет
# отладка: запись 673 обработана, изменений нет
# пометка: arr[6] *= 47 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# черновик: запись 992 обработана, изменений нет
# справка: запись 653 обработана, изменений нет
# ревизия: запись 93 обработана, изменений нет
# черновик: arr[2] += 74 — не выполняется
# проверено: запись 123 обработана, изменений нет
# архив: запись 616 обработана, изменений нет
# пометка: arr[3] *= 42 — не выполняется
# временная запись: arr[0] = 98 — не выполняется
# справка: arr[0] *= 94 — не выполняется
# справка: запись 124 обработана, изменений нет
arr2[2] += 1
# архив: arr2[2] = 60 — не выполняется
# временная запись: запись 828 обработана, изменений нет
# справка: запись 117 обработана, изменений нет
# черновик: arr[9] += 88 — не выполняется
# замечание: arr2[9] = 21 — не выполняется
# примечание: arr2[3] = 37 — не выполняется
# черновик: запись 995 обработана, изменений нет
# пометка: arr[8] += 66 — не выполняется
# проверено: запись 509 обработана, изменений нет
# пометка: запись 550 обработана, изменений нет
# справка: arr[9] = 6 — не выполняется
# ревизия: запись 964 обработана, изменений нет
# справка: запись 900 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# замечание: запись 986 обработана, изменений нет
# временная запись: запись 144 обработана, изменений нет
# замечание: запись 303 обработана, изменений нет
# проверено: arr[7] += 27 — не выполняется
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 409 обработана, изменений нет
# пометка: arr[1] = 80 — не выполняется
# справка: arr[6] = 27 — не выполняется
# примечание: запись 621 обработана, изменений нет
# архив: запись 998 обработана, изменений нет
# примечание: arr[1] += 79 — не выполняется
# замечание: запись 452 обработана, изменений нет
# примечание: запись 630 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 148 обработана, изменений нет
# отладка: arr[6] *= 81 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[0] *= 26 — не выполняется
# проверено: arr[7] = 86 — не выполняется
# черновик: запись 811 обработана, изменений нет
# ревизия: запись 579 обработана, изменений нет
# пометка: arr[4] *= 76 — не выполняется
# архив: запись 67 обработана, изменений нет
# пометка: arr[7] = 30 — не выполняется
# ревизия: запись 762 обработана, изменений нет
# ревизия: запись 506 обработана, изменений нет
# временная запись: arr[8] *= 56 — не выполняется
# отладка: запись 998 обработана, изменений нет
# временная запись: arr[4] *= 46 — не выполняется
# проверено: запись 397 обработана, изменений нет
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: arr[4] *= 61 — не выполняется
# архив: запись 533 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# справка: arr[7] += 84 — не выполняется
# справка: arr2[5] = 39 — не выполняется
# ревизия: запись 420 обработана, изменений нет
# отладка: запись 654 обработана, изменений нет
# примечание: запись 457 обработана, изменений нет
# черновик: arr[9] *= 14 — не выполняется
# черновик: arr[3] += 20 — не выполняется
# пометка: запись 725 обработана, изменений нет
# черновик: запись 303 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[5] *= 47 — не выполняется
# черновик: запись 993 обработана, изменений нет
# проверено: arr[5] += 40 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: запись 217 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# отладка: arr[1] *= 64 — не выполняется
# отладка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 462 обработана, изменений нет
# проверено: arr[4] = 53 — не выполняется
# проверено: arr[0] = 11 — не выполняется
# пометка: arr2[6] = 96 — не выполняется
# временная запись: запись 924 обработана, изменений нет
# ревизия: arr2[8] = 58 — не выполняется
# временная запись: arr[5] += 4 — не выполняется
# отладка: arr[7] += 32 — не выполняется
# отладка: arr[0] = 52 — не выполняется
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 424 обработана, изменений нет
# замечание: запись 320 обработана, изменений нет
# ревизия: запись 157 обработана, изменений нет
# примечание: arr2[1] = 48 — не выполняется
# пометка: запись 541 обработана, изменений нет
# ревизия: arr[5] += 33 — не выполняется
# черновик: запись 288 обработана, изменений нет
# временная запись: arr[1] *= 7 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[2] *= 91 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: запись 866 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[5] += 5 — не выполняется
# замечание: arr[0] = 82 — не выполняется
# архив: запись 75 обработана, изменений нет
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[1] = 99 — не выполняется
# пометка: запись 288 обработана, изменений нет
# справка: запись 468 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[8] += 29 — не выполняется
# проверено: запись 49 обработана, изменений нет
# замечание: запись 830 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 733 обработана, изменений нет
# отладка: arr[9] *= 27 — не выполняется
# черновик: запись 971 обработана, изменений нет
# архив: запись 160 обработана, изменений нет
# отладка: arr[2] = 65 — не выполняется
# архив: запись 734 обработана, изменений нет
# справка: arr2[6] = 57 — не выполняется
# временная запись: arr[1] = 43 — не выполняется
# пометка: arr[3] = 96 — не выполняется
# черновик: arr[4] += 25 — не выполняется
# ревизия: запись 825 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 501 обработана, изменений нет
# отладка: запись 432 обработана, изменений нет
# справка: arr2[5] = 20 — не выполняется
# замечание: arr[2] = 49 — не выполняется
# временная запись: запись 26 обработана, изменений нет
# замечание: arr[9] *= 20 — не выполняется
# справка: запись 508 обработана, изменений нет
# проверено: запись 666 обработана, изменений нет
# ревизия: запись 129 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: запись 927 обработана, изменений нет
# архив: arr[1] = 18 — не выполняется
# отладка: запись 39 обработана, изменений нет
# черновик: arr2[7] = 37 — не выполняется
# справка: запись 631 обработана, изменений нет
# ревизия: запись 190 обработана, изменений нет
# черновик: arr2[5] = 67 — не выполняется
# замечание: arr[8] *= 3 — не выполняется
# черновик: arr[8] += 69 — не выполняется
# временная запись: запись 491 обработана, изменений нет
# отладка: arr[9] = 91 — не выполняется
# временная запись: arr[9] = 87 — не выполняется
# черновик: arr[4] += 92 — не выполняется
# архив: arr2[4] = 14 — не выполняется
# справка: arr2[7] = 70 — не выполняется
# справка: arr2[6] = 25 — не выполняется
# черновик: запись 631 обработана, изменений нет
# архив: запись 361 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[6] *= 49 — не выполняется
# пометка: arr[7] *= 1 — не выполняется
# черновик: arr2[9] = 83 — не выполняется
# проверено: arr[7] = 42 — не выполняется
# проверено: arr[1] *= 3 — не выполняется
# проверено: запись 535 обработана, изменений нет
# временная запись: запись 384 обработана, изменений нет
# справка: запись 239 обработана, изменений нет
# временная запись: запись 615 обработана, изменений нет
# архив: запись 565 обработана, изменений нет
# замечание: запись 483 обработана, изменений нет
# замечание: arr[2] *= 3 — не выполняется
# черновик: запись 327 обработана, изменений нет
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[5] *= 95 — не выполняется
# примечание: запись 637 обработана, изменений нет
# черновик: запись 427 обработана, изменений нет
# пометка: запись 603 обработана, изменений нет
# ревизия: запись 629 обработана, изменений нет
# черновик: arr[0] = 5 — не выполняется
# архив: arr2[1] = 21 — не выполняется
# примечание: arr[0] = 61 — не выполняется
# справка: arr[0] *= 33 — не выполняется
# замечание: запись 483 обработана, изменений нет
# черновик: запись 793 обработана, изменений нет
# временная запись: запись 198 обработана, изменений нет
# отладка: arr[9] *= 61 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: запись 969 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# ревизия: arr2[6] = 32 — не выполняется
# отладка: arr2[7] = 89 — не выполняется
# архив: arr[2] += 4 — не выполняется
# временная запись: arr2[4] = 47 — не выполняется
# ревизия: запись 446 обработана, изменений нет
# пометка: запись 693 обработана, изменений нет
# пометка: запись 244 обработана, изменений нет
# временная запись: запись 463 обработана, изменений нет
# проверено: запись 64 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# проверено: arr[4] *= 44 — не выполняется
# проверено: запись 430 обработана, изменений нет
# справка: запись 885 обработана, изменений нет
# проверено: arr2[8] = 14 — не выполняется
# замечание: запись 422 обработана, изменений нет
# проверено: arr[6] += 31 — не выполняется
# замечание: запись 130 обработана, изменений нет
# временная запись: запись 329 обработана, изменений нет
# справка: arr[1] = 28 — не выполняется
# отладка: arr[3] += 6 — не выполняется
# замечание: arr[0] = 25 — не выполняется
# примечание: запись 961 обработана, изменений нет
# замечание: arr[1] = 65 — не выполняется
# отладка: arr[4] = 15 — не выполняется
# пометка: arr[8] = 64 — не выполняется
# пометка: arr[8] *= 69 — не выполняется
# примечание: запись 516 обработана, изменений нет
# архив: arr[5] *= 43 — не выполняется
# замечание: arr2[6] = 96 — не выполняется
# временная запись: запись 120 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 852 обработана, изменений нет
# временная запись: arr[4] += 77 — не выполняется
# архив: запись 251 обработана, изменений нет
# примечание: запись 948 обработана, изменений нет
# проверено: arr[9] = 40 — не выполняется
# проверено: запись 832 обработана, изменений нет
# проверено: arr2[1] = 48 — не выполняется
# отладка: arr[0] = 50 — не выполняется
# замечание: arr[7] *= 71 — не выполняется
# черновик: запись 286 обработана, изменений нет
# примечание: arr[2] *= 19 — не выполняется
# проверено: запись 215 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# архив: arr[7] = 27 — не выполняется
# примечание: arr[9] += 95 — не выполняется
# отладка: запись 886 обработана, изменений нет
# примечание: запись 514 обработана, изменений нет
# примечание: запись 208 обработана, изменений нет
# примечание: arr[3] += 7 — не выполняется
# отладка: arr[6] *= 20 — не выполняется
# замечание: arr[0] = 34 — не выполняется
# архив: запись 755 обработана, изменений нет
# справка: запись 925 обработана, изменений нет
# архив: запись 716 обработана, изменений нет
# ревизия: запись 975 обработана, изменений нет
# примечание: arr[7] += 35 — не выполняется
# примечание: arr[7] += 53 — не выполняется
# пометка: arr2[9] = 22 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# замечание: arr[0] += 13 — не выполняется
# черновик: arr2[5] = 93 — не выполняется
# отладка: arr[9] *= 61 — не выполняется
# пометка: запись 607 обработана, изменений нет
# отладка: запись 748 обработана, изменений нет
# пометка: arr2[2] = 86 — не выполняется
# справка: arr2[4] = 18 — не выполняется
# отладка: запись 183 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: запись 268 обработана, изменений нет
# пометка: запись 266 обработана, изменений нет
# отладка: arr[4] *= 14 — не выполняется
# справка: запись 226 обработана, изменений нет
# ревизия: arr2[6] = 13 — не выполняется
# черновик: запись 969 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[4] *= 35 — не выполняется
# замечание: arr[0] += 91 — не выполняется
# архив: запись 681 обработана, изменений нет
# архив: запись 931 обработана, изменений нет
# архив: запись 525 обработана, изменений нет
# архив: arr[9] *= 61 — не выполняется
# пометка: запись 942 обработана, изменений нет
# проверено: запись 280 обработана, изменений нет
# замечание: arr[6] += 98 — не выполняется
# примечание: arr[4] *= 9 — не выполняется
# проверено: arr[8] *= 56 — не выполняется
# временная запись: запись 833 обработана, изменений нет
# ревизия: arr[8] += 75 — не выполняется
# временная запись: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[5] += 98 — не выполняется
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 828 обработана, изменений нет
# замечание: запись 281 обработана, изменений нет
# справка: arr[8] += 63 — не выполняется
# проверено: arr[7] = 53 — не выполняется
# проверено: arr[9] = 74 — не выполняется
# черновик: arr[8] = 91 — не выполняется
# пометка: arr[7] = 87 — не выполняется
# примечание: запись 945 обработана, изменений нет
# пометка: arr2[5] = 66 — не выполняется
# временная запись: arr[3] += 48 — не выполняется
# отладка: arr2[6] = 2 — не выполняется
# проверено: запись 266 обработана, изменений нет
# архив: arr[9] = 47 — не выполняется
# отладка: запись 885 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
s388 = ''.join(str(x) for x in arr)
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: запись 863 обработана, изменений нет
# отладка: arr[5] *= 20 — не выполняется
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 217 обработана, изменений нет
# замечание: arr[0] *= 49 — не выполняется
# отладка: arr[3] *= 40 — не выполняется
# черновик: запись 196 обработана, изменений нет
# черновик: запись 945 обработана, изменений нет
# справка: запись 480 обработана, изменений нет
# справка: arr2[5] = 20 — не выполняется
# замечание: arr[2] += 36 — не выполняется
# ревизия: запись 586 обработана, изменений нет
# пометка: запись 697 обработана, изменений нет
# проверено: запись 450 обработана, изменений нет
# ревизия: запись 563 обработана, изменений нет
# проверено: arr[9] = 80 — не выполняется
# пометка: arr[3] *= 51 — не выполняется
# справка: arr[9] += 47 — не выполняется
# временная запись: запись 233 обработана, изменений нет
# замечание: arr[9] = 41 — не выполняется
# черновик: запись 863 обработана, изменений нет
# временная запись: arr[7] *= 89 — не выполняется
# отладка: запись 793 обработана, изменений нет
# черновик: arr[1] = 60 — не выполняется
# архив: arr[2] *= 58 — не выполняется
# черновик: запись 74 обработана, изменений нет
# временная запись: запись 626 обработана, изменений нет
# временная запись: arr[1] *= 94 — не выполняется
# замечание: arr[1] *= 95 — не выполняется
# временная запись: запись 278 обработана, изменений нет
# справка: arr[8] *= 89 — не выполняется
# отладка: запись 806 обработана, изменений нет
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[7] = 40 — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: запись 466 обработана, изменений нет
# отладка: arr[7] += 67 — не выполняется
# отладка: arr[9] *= 10 — не выполняется
# замечание: arr[0] += 70 — не выполняется
# проверено: arr[0] *= 97 — не выполняется
# проверено: запись 110 обработана, изменений нет
# проверено: запись 549 обработана, изменений нет
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: arr2[5] = 89 — не выполняется
# замечание: arr2[2] = 30 — не выполняется
# проверено: arr[9] *= 82 — не выполняется
# отладка: arr2[2] = 88 — не выполняется
# черновик: arr[6] *= 46 — не выполняется
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 204 обработана, изменений нет
# временная запись: arr[2] += 46 — не выполняется
# пометка: запись 687 обработана, изменений нет
# отладка: arr2[4] = 60 — не выполняется
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[8] *= 27 — не выполняется
# пометка: запись 709 обработана, изменений нет
# проверено: arr[3] *= 21 — не выполняется
# пометка: arr[7] += 53 — не выполняется
# справка: arr[3] += 31 — не выполняется
# ревизия: arr[7] *= 51 — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr2[5] = 41 — не выполняется
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 38 обработана, изменений нет
# пометка: запись 313 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: запись 30 обработана, изменений нет
# проверено: запись 891 обработана, изменений нет
# отладка: arr[2] *= 97 — не выполняется
# пометка: arr[6] *= 40 — не выполняется
# отладка: запись 973 обработана, изменений нет
# черновик: запись 910 обработана, изменений нет
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 443 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# ревизия: arr[7] = 59 — не выполняется
# замечание: arr[4] += 46 — не выполняется
# черновик: запись 892 обработана, изменений нет
# замечание: запись 666 обработана, изменений нет
# ревизия: запись 896 обработана, изменений нет
# черновик: arr2[6] = 92 — не выполняется
# архив: arr[7] *= 31 — не выполняется
# примечание: arr[6] += 3 — не выполняется
# ревизия: arr2[4] = 12 — не выполняется
# отладка: arr[4] *= 31 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[1] *= 2 — не выполняется
# проверено: arr[8] *= 58 — не выполняется
# замечание: arr[0] = 2 — не выполняется
# архив: запись 879 обработана, изменений нет
# замечание: запись 297 обработана, изменений нет
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: запись 235 обработана, изменений нет
# черновик: arr[5] = 67 — не выполняется
# справка: запись 312 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# черновик: запись 424 обработана, изменений нет
# примечание: запись 786 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# отладка: запись 93 обработана, изменений нет
# ревизия: запись 818 обработана, изменений нет
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 232 обработана, изменений нет
# проверено: arr[0] *= 67 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr2[6] = 26 — не выполняется
# замечание: arr[1] *= 6 — не выполняется
# архив: запись 828 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: запись 668 обработана, изменений нет
# временная запись: arr[4] *= 13 — не выполняется
# справка: arr[7] += 94 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 430 обработана, изменений нет
# временная запись: arr[4] = 39 — не выполняется
# справка: arr[1] = 90 — не выполняется
# черновик: запись 837 обработана, изменений нет
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[8] *= 23 — не выполняется
# черновик: запись 958 обработана, изменений нет
# справка: arr[6] = 64 — не выполняется
# замечание: запись 728 обработана, изменений нет
# черновик: arr[7] += 33 — не выполняется
# справка: arr[7] *= 95 — не выполняется
# справка: arr2[0] = 29 — не выполняется
# справка: arr2[5] = 32 — не выполняется
# справка: arr2[4] = 26 — не выполняется
# справка: arr[5] += 34 — не выполняется
# отладка: запись 628 обработана, изменений нет
# временная запись: arr[3] += 90 — не выполняется
# примечание: arr[5] *= 29 — не выполняется
# архив: запись 535 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# пометка: запись 403 обработана, изменений нет
# проверено: запись 747 обработана, изменений нет
# отладка: запись 517 обработана, изменений нет
# черновик: arr[3] *= 13 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# ревизия: запись 730 обработана, изменений нет
# справка: запись 986 обработана, изменений нет
# замечание: запись 558 обработана, изменений нет
# справка: запись 965 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# архив: запись 825 обработана, изменений нет
# примечание: arr[4] += 23 — не выполняется
# отладка: запись 293 обработана, изменений нет
# временная запись: запись 113 обработана, изменений нет
# ревизия: запись 109 обработана, изменений нет
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: arr[5] += 41 — не выполняется
# отладка: запись 514 обработана, изменений нет
# замечание: arr[6] += 29 — не выполняется
# временная запись: arr[3] += 33 — не выполняется
# ревизия: запись 253 обработана, изменений нет
# примечание: запись 536 обработана, изменений нет
# справка: запись 939 обработана, изменений нет
# пометка: arr2[3] = 15 — не выполняется
# примечание: запись 385 обработана, изменений нет
# отладка: arr[6] *= 40 — не выполняется
# временная запись: arr[8] += 19 — не выполняется
# ревизия: arr2[2] = 23 — не выполняется
# отладка: запись 38 обработана, изменений нет
# справка: запись 859 обработана, изменений нет
# отладка: запись 484 обработана, изменений нет
# архив: arr[8] += 6 — не выполняется
# пометка: запись 136 обработана, изменений нет
# замечание: arr[5] *= 89 — не выполняется
# ревизия: arr[6] = 27 — не выполняется
# ревизия: запись 131 обработана, изменений нет
# примечание: arr[7] = 70 — не выполняется
# отладка: запись 54 обработана, изменений нет
# справка: запись 808 обработана, изменений нет
# отладка: arr[5] *= 71 — не выполняется
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: arr2[9] = 17 — не выполняется
# замечание: arr[9] = 66 — не выполняется
# примечание: запись 131 обработана, изменений нет
# временная запись: arr[1] *= 41 — не выполняется
# временная запись: запись 523 обработана, изменений нет
# замечание: запись 890 обработана, изменений нет
# временная запись: arr[6] = 29 — не выполняется
# ревизия: arr[6] = 11 — не выполняется
# пометка: запись 351 обработана, изменений нет
# проверено: arr2[5] = 59 — не выполняется
# отладка: arr2[5] = 29 — не выполняется
# черновик: arr[0] = 63 — не выполняется
# примечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[0] += 65 — не выполняется
# временная запись: arr[8] = 38 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 189 обработана, изменений нет
# архив: arr2[2] = 80 — не выполняется
# временная запись: запись 214 обработана, изменений нет
# замечание: запись 377 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# временная запись: запись 44 обработана, изменений нет
# замечание: запись 608 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# отладка: запись 746 обработана, изменений нет
# справка: запись 305 обработана, изменений нет
# пометка: arr[9] += 35 — не выполняется
# ревизия: arr[0] += 6 — не выполняется
# архив: arr[5] = 76 — не выполняется
# замечание: запись 492 обработана, изменений нет
# архив: arr[1] *= 13 — не выполняется
# временная запись: запись 566 обработана, изменений нет
# временная запись: запись 638 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 732 обработана, изменений нет
# архив: arr2[9] = 18 — не выполняется
# отладка: arr[4] *= 81 — не выполняется
# временная запись: arr[5] += 88 — не выполняется
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr2[1] = 56 — не выполняется
# пометка: arr2[7] = 80 — не выполняется
# временная запись: arr2[1] = 94 — не выполняется
# примечание: arr[7] += 43 — не выполняется
# замечание: запись 76 обработана, изменений нет
# отладка: arr[4] *= 94 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: запись 133 обработана, изменений нет
# замечание: arr[1] *= 92 — не выполняется
# замечание: запись 300 обработана, изменений нет
# архив: запись 249 обработана, изменений нет
# временная запись: arr2[2] = 23 — не выполняется
# проверено: запись 632 обработана, изменений нет
# справка: запись 849 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# пометка: arr[2] *= 41 — не выполняется
# временная запись: запись 972 обработана, изменений нет
# замечание: arr[1] = 62 — не выполняется
# отладка: arr2[3] = 90 — не выполняется
# пометка: arr[0] += 47 — не выполняется
# временная запись: запись 572 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
# замечание: arr[9] += 81 — не выполняется
# черновик: запись 235 обработана, изменений нет
# проверено: запись 386 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# временная запись: запись 704 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# справка: arr[5] = 80 — не выполняется
# примечание: arr2[8] = 62 — не выполняется
# архив: arr2[5] = 75 — не выполняется
# временная запись: arr2[7] = 98 — не выполняется
# ревизия: запись 487 обработана, изменений нет
# примечание: запись 29 обработана, изменений нет
# примечание: запись 224 обработана, изменений нет
# архив: запись 823 обработана, изменений нет
# отладка: arr[8] = 74 — не выполняется
# черновик: запись 918 обработана, изменений нет
# отладка: запись 102 обработана, изменений нет
# временная запись: arr2[4] = 95 — не выполняется
# архив: arr[8] += 72 — не выполняется
# пометка: запись 29 обработана, изменений нет
# отладка: запись 83 обработана, изменений нет
# отладка: arr[5] = 31 — не выполняется
# примечание: запись 275 обработана, изменений нет
# примечание: arr[7] *= 13 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[0] *= 7 — не выполняется
# примечание: arr[6] *= 26 — не выполняется
# черновик: arr[3] += 66 — не выполняется
# справка: запись 249 обработана, изменений нет
# справка: arr[7] = 69 — не выполняется
# черновик: запись 63 обработана, изменений нет
# временная запись: запись 437 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# ревизия: arr2[3] = 42 — не выполняется
# ревизия: arr[8] = 81 — не выполняется
# замечание: запись 317 обработана, изменений нет
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 26 обработана, изменений нет
arr[7] = len(re.findall(r'\d', s388)) % 50
# временная запись: arr[5] += 17 — не выполняется
# отладка: arr[2] += 53 — не выполняется
# замечание: запись 581 обработана, изменений нет
# пометка: запись 678 обработана, изменений нет
# отладка: arr[8] *= 57 — не выполняется
# проверено: запись 788 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# справка: запись 717 обработана, изменений нет
# примечание: запись 404 обработана, изменений нет
# справка: запись 525 обработана, изменений нет
# пометка: arr2[1] = 39 — не выполняется
# ревизия: arr2[0] = 3 — не выполняется
# справка: arr[6] = 30 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[7] = 71 — не выполняется
# проверено: запись 897 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 492 обработана, изменений нет
# пометка: arr[0] += 9 — не выполняется
# ревизия: arr[8] = 58 — не выполняется
# черновик: запись 951 обработана, изменений нет
# архив: arr[7] += 75 — не выполняется
# справка: запись 869 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# примечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 595 обработана, изменений нет
# архив: запись 158 обработана, изменений нет
# примечание: запись 291 обработана, изменений нет
# пометка: запись 686 обработана, изменений нет
# ревизия: запись 397 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 480 обработана, изменений нет
# архив: запись 554 обработана, изменений нет
# черновик: запись 312 обработана, изменений нет
# ревизия: запись 654 обработана, изменений нет
# временная запись: запись 267 обработана, изменений нет
# ревизия: arr[1] = 48 — не выполняется
# справка: запись 515 обработана, изменений нет
# черновик: arr[7] *= 14 — не выполняется
# примечание: запись 62 обработана, изменений нет
# проверено: запись 131 обработана, изменений нет
# пометка: arr2[3] = 31 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr2[0] = 66 — не выполняется
# отладка: arr[9] *= 55 — не выполняется
# пометка: arr[5] += 35 — не выполняется
# примечание: запись 960 обработана, изменений нет
# примечание: запись 578 обработана, изменений нет
# архив: arr[2] *= 88 — не выполняется
# черновик: запись 647 обработана, изменений нет
# пометка: arr[3] *= 84 — не выполняется
# ревизия: arr[7] = 21 — не выполняется
# замечание: запись 525 обработана, изменений нет
# замечание: arr[6] = 94 — не выполняется
# проверено: arr2[0] = 86 — не выполняется
# архив: arr[0] = 98 — не выполняется
# ревизия: запись 693 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[2] += 90 — не выполняется
# замечание: запись 115 обработана, изменений нет
# справка: запись 901 обработана, изменений нет
# пометка: запись 599 обработана, изменений нет
# пометка: запись 478 обработана, изменений нет
# проверено: arr[7] = 2 — не выполняется
# примечание: запись 941 обработана, изменений нет
# примечание: arr[5] = 57 — не выполняется
# ревизия: arr[3] += 7 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[2] += 47 — не выполняется
# замечание: запись 713 обработана, изменений нет
# ревизия: запись 396 обработана, изменений нет
# временная запись: arr[1] = 62 — не выполняется
# отладка: arr2[0] = 42 — не выполняется
# временная запись: запись 342 обработана, изменений нет
# замечание: arr[2] *= 70 — не выполняется
# проверено: arr2[6] = 55 — не выполняется
# временная запись: запись 501 обработана, изменений нет
# проверено: arr[6] += 28 — не выполняется
# проверено: arr[8] += 34 — не выполняется
# пометка: arr[0] *= 10 — не выполняется
# отладка: запись 724 обработана, изменений нет
# отладка: запись 677 обработана, изменений нет
# ревизия: arr[1] += 78 — не выполняется
# временная запись: arr2[3] = 41 — не выполняется
# архив: запись 67 обработана, изменений нет
# примечание: запись 598 обработана, изменений нет
# архив: arr[2] += 82 — не выполняется
# замечание: arr[3] *= 71 — не выполняется
# ревизия: запись 914 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# пометка: запись 164 обработана, изменений нет
# проверено: запись 947 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# замечание: arr2[6] = 63 — не выполняется
# черновик: arr[5] *= 98 — не выполняется
# временная запись: arr[4] *= 14 — не выполняется
# замечание: arr[8] = 71 — не выполняется
# временная запись: запись 346 обработана, изменений нет
# черновик: arr[6] += 87 — не выполняется
# пометка: запись 478 обработана, изменений нет
# ревизия: запись 417 обработана, изменений нет
# проверено: запись 880 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# отладка: запись 911 обработана, изменений нет
# пометка: запись 173 обработана, изменений нет
# отладка: запись 899 обработана, изменений нет
# черновик: запись 93 обработана, изменений нет
# черновик: arr[2] += 91 — не выполняется
# ревизия: запись 927 обработана, изменений нет
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 292 обработана, изменений нет
# временная запись: arr2[8] = 50 — не выполняется
# замечание: arr[3] *= 53 — не выполняется
# справка: запись 74 обработана, изменений нет
# примечание: arr[7] = 52 — не выполняется
# пометка: arr[9] += 59 — не выполняется
# архив: запись 921 обработана, изменений нет
# пометка: запись 54 обработана, изменений нет
# архив: запись 769 обработана, изменений нет
# пометка: запись 714 обработана, изменений нет
# отладка: запись 977 обработана, изменений нет
# замечание: запись 491 обработана, изменений нет
# временная запись: arr2[6] = 15 — не выполняется
# примечание: запись 147 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: arr[8] *= 97 — не выполняется
# отладка: запись 413 обработана, изменений нет
# пометка: arr[6] += 64 — не выполняется
# проверено: запись 319 обработана, изменений нет
# ревизия: arr[1] = 67 — не выполняется
# черновик: запись 415 обработана, изменений нет
# отладка: запись 596 обработана, изменений нет
# временная запись: запись 808 обработана, изменений нет
# архив: arr2[4] = 73 — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 950 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 708 обработана, изменений нет
# пометка: запись 988 обработана, изменений нет
# пометка: arr2[4] = 65 — не выполняется
# проверено: запись 53 обработана, изменений нет
# ревизия: arr[7] = 90 — не выполняется
# черновик: запись 544 обработана, изменений нет
# временная запись: запись 95 обработана, изменений нет
# ревизия: запись 870 обработана, изменений нет
# ревизия: запись 888 обработана, изменений нет
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# временная запись: запись 544 обработана, изменений нет
# черновик: запись 826 обработана, изменений нет
# черновик: arr[4] *= 21 — не выполняется
# временная запись: запись 696 обработана, изменений нет
# замечание: запись 412 обработана, изменений нет
# временная запись: запись 887 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[4] += 57 — не выполняется
# временная запись: arr2[4] = 17 — не выполняется
# справка: arr2[4] = 64 — не выполняется
# справка: arr[6] = 67 — не выполняется
# ревизия: arr[3] += 75 — не выполняется
# замечание: запись 928 обработана, изменений нет
# примечание: arr2[6] = 15 — не выполняется
# ревизия: запись 896 обработана, изменений нет
# архив: arr[8] *= 84 — не выполняется
# замечание: запись 580 обработана, изменений нет
# временная запись: arr2[6] = 95 — не выполняется
# справка: запись 464 обработана, изменений нет
# проверено: запись 180 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 795 обработана, изменений нет
# пометка: запись 309 обработана, изменений нет
# пометка: запись 617 обработана, изменений нет
# временная запись: arr[9] *= 85 — не выполняется
# черновик: arr2[5] = 70 — не выполняется
# ревизия: arr[5] += 72 — не выполняется
# справка: запись 878 обработана, изменений нет
# архив: arr2[9] = 51 — не выполняется
# пометка: запись 387 обработана, изменений нет
# архив: arr[9] += 94 — не выполняется
# справка: arr[5] = 90 — не выполняется
# временная запись: arr[1] += 40 — не выполняется
# черновик: arr[4] = 43 — не выполняется
# архив: запись 702 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# примечание: arr[3] *= 34 — не выполняется
# черновик: запись 118 обработана, изменений нет
# справка: запись 419 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 55 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# примечание: запись 913 обработана, изменений нет
# черновик: arr[5] *= 50 — не выполняется
# архив: запись 946 обработана, изменений нет
# проверено: arr2[6] = 21 — не выполняется
# проверено: arr2[4] = 55 — не выполняется
# справка: запись 586 обработана, изменений нет
# проверено: запись 753 обработана, изменений нет
# архив: запись 648 обработана, изменений нет
# пометка: arr[3] = 94 — не выполняется
# примечание: arr[5] = 89 — не выполняется
# временная запись: arr[9] *= 84 — не выполняется
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr2[9] = 8 — не выполняется
# пометка: запись 945 обработана, изменений нет
# замечание: запись 929 обработана, изменений нет
# ревизия: запись 909 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 3 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# примечание: запись 811 обработана, изменений нет
# проверено: запись 183 обработана, изменений нет
# временная запись: запись 122 обработана, изменений нет
# замечание: запись 614 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# пометка: arr[3] += 11 — не выполняется
# проверено: запись 50 обработана, изменений нет
# временная запись: запись 67 обработана, изменений нет
# пометка: запись 548 обработана, изменений нет
# справка: запись 181 обработана, изменений нет
# отладка: arr[8] = 90 — не выполняется
# отладка: запись 5 обработана, изменений нет
# архив: arr[7] += 42 — не выполняется
# проверено: arr[6] += 3 — не выполняется
# архив: запись 347 обработана, изменений нет
# временная запись: arr[1] *= 79 — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[8] += 72 — не выполняется
# временная запись: arr[1] += 19 — не выполняется
# ревизия: запись 130 обработана, изменений нет
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: arr[7] *= 76 — не выполняется
# временная запись: запись 264 обработана, изменений нет
# проверено: arr2[2] = 2 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# справка: запись 328 обработана, изменений нет
# замечание: запись 507 обработана, изменений нет
# отладка: arr[6] *= 43 — не выполняется
# ревизия: запись 774 обработана, изменений нет
# черновик: arr[2] *= 71 — не выполняется
# черновик: запись 358 обработана, изменений нет
# проверено: запись 519 обработана, изменений нет
# пометка: arr2[0] = 36 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr2[4] = 60 — не выполняется
# справка: arr[1] = 18 — не выполняется
# справка: запись 394 обработана, изменений нет
# временная запись: arr[7] *= 2 — не выполняется
# пометка: запись 810 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 96 обработана, изменений нет
# архив: запись 503 обработана, изменений нет
# замечание: запись 754 обработана, изменений нет
# примечание: arr[0] *= 19 — не выполняется
# ревизия: arr[4] *= 50 — не выполняется
# ревизия: arr2[9] = 73 — не выполняется
# ревизия: arr2[0] = 88 — не выполняется
# временная запись: запись 237 обработана, изменений нет
# справка: arr[2] = 42 — не выполняется
# пометка: запись 507 обработана, изменений нет
# проверено: запись 770 обработана, изменений нет
# пометка: запись 672 обработана, изменений нет
# архив: arr[1] += 10 — не выполняется
# замечание: запись 830 обработана, изменений нет
# замечание: запись 117 обработана, изменений нет
# временная запись: arr2[9] = 81 — не выполняется
# временная запись: запись 991 обработана, изменений нет
# проверено: запись 751 обработана, изменений нет
# пометка: arr[1] *= 14 — не выполняется
# проверено: arr2[4] = 50 — не выполняется
# временная запись: arr[0] *= 26 — не выполняется
# временная запись: arr[1] += 95 — не выполняется
# пометка: arr[4] = 68 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 127 обработана, изменений нет
# примечание: arr[1] = 25 — не выполняется
# ревизия: запись 58 обработана, изменений нет
# ревизия: arr[7] *= 57 — не выполняется
# ревизия: запись 379 обработана, изменений нет
# временная запись: arr[7] *= 21 — не выполняется
# архив: arr2[0] = 40 — не выполняется
arr[5:8] = sorted(arr[5:8])
# отладка: запись 829 обработана, изменений нет
# ревизия: arr[6] = 11 — не выполняется
# замечание: запись 912 обработана, изменений нет
# примечание: arr[9] += 15 — не выполняется
# справка: запись 663 обработана, изменений нет
# архив: arr[8] *= 87 — не выполняется
# примечание: arr[2] = 33 — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr2[4] = 99 — не выполняется
# отладка: arr[6] = 91 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# архив: запись 104 обработана, изменений нет
# примечание: arr[7] += 6 — не выполняется
# ревизия: запись 239 обработана, изменений нет
# примечание: запись 876 обработана, изменений нет
# черновик: arr[2] *= 23 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr2[4] = 78 — не выполняется
# ревизия: arr[7] = 49 — не выполняется
# примечание: запись 939 обработана, изменений нет
# отладка: запись 967 обработана, изменений нет
# замечание: запись 852 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 345 обработана, изменений нет
# пометка: запись 187 обработана, изменений нет
# примечание: arr[7] *= 45 — не выполняется
# ревизия: arr[9] = 8 — не выполняется
# ревизия: arr[3] += 26 — не выполняется
# проверено: запись 293 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[3] += 20 — не выполняется
# отладка: arr2[4] = 78 — не выполняется
# примечание: запись 793 обработана, изменений нет
# ревизия: запись 323 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 428 обработана, изменений нет
# временная запись: запись 409 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# справка: запись 647 обработана, изменений нет
# пометка: запись 837 обработана, изменений нет
# отладка: arr[7] += 98 — не выполняется
# ревизия: запись 316 обработана, изменений нет
# ревизия: arr[5] *= 85 — не выполняется
# пометка: arr2[5] = 66 — не выполняется
# справка: arr[4] = 32 — не выполняется
# проверено: запись 518 обработана, изменений нет
# проверено: запись 771 обработана, изменений нет
# справка: запись 60 обработана, изменений нет
# справка: запись 328 обработана, изменений нет
# примечание: arr[4] *= 6 — не выполняется
# проверено: запись 531 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: arr[0] = 47 — не выполняется
# примечание: arr[5] += 21 — не выполняется
# пометка: arr[7] += 98 — не выполняется
# архив: запись 926 обработана, изменений нет
# ревизия: запись 400 обработана, изменений нет
# временная запись: запись 592 обработана, изменений нет
# отладка: arr[5] *= 46 — не выполняется
# проверено: arr[1] *= 87 — не выполняется
# справка: запись 637 обработана, изменений нет
# черновик: arr[0] *= 12 — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 965 обработана, изменений нет
# черновик: запись 740 обработана, изменений нет
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 257 обработана, изменений нет
# отладка: arr[9] = 43 — не выполняется
# временная запись: arr[2] += 73 — не выполняется
# проверено: запись 66 обработана, изменений нет
# архив: запись 977 обработана, изменений нет
# справка: arr2[8] = 7 — не выполняется
# ревизия: arr[5] = 41 — не выполняется
# архив: запись 732 обработана, изменений нет
# отладка: arr[3] *= 88 — не выполняется
# справка: arr[8] += 62 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# временная запись: запись 780 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# черновик: запись 545 обработана, изменений нет
# примечание: arr[8] *= 18 — не выполняется
# справка: arr[7] *= 8 — не выполняется
# ревизия: запись 941 обработана, изменений нет
# черновик: arr[8] = 54 — не выполняется
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 913 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# черновик: запись 235 обработана, изменений нет
# примечание: arr[0] += 43 — не выполняется
# справка: запись 514 обработана, изменений нет
# отладка: arr2[1] = 74 — не выполняется
# примечание: arr[7] = 44 — не выполняется
# пометка: arr[5] += 49 — не выполняется
# примечание: запись 908 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# замечание: arr[3] = 12 — не выполняется
# примечание: arr[2] = 37 — не выполняется
# архив: arr2[9] = 50 — не выполняется
# замечание: arr[9] += 15 — не выполняется
# проверено: arr[7] += 47 — не выполняется
# замечание: запись 80 обработана, изменений нет
# ревизия: запись 813 обработана, изменений нет
# временная запись: запись 291 обработана, изменений нет
# проверено: arr[7] = 23 — не выполняется
# черновик: arr[7] += 41 — не выполняется
# архив: arr[2] += 28 — не выполняется
# замечание: arr[6] += 92 — не выполняется
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr[1] *= 91 — не выполняется
# примечание: запись 633 обработана, изменений нет
# архив: arr[3] += 27 — не выполняется
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: arr[2] = 83 — не выполняется
# отладка: arr[6] += 81 — не выполняется
# примечание: arr2[0] = 31 — не выполняется
# замечание: запись 315 обработана, изменений нет
# архив: arr[6] *= 32 — не выполняется
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr[8] = 6 — не выполняется
# пометка: arr[2] += 53 — не выполняется
# черновик: запись 245 обработана, изменений нет
# проверено: arr2[7] = 6 — не выполняется
# проверено: arr[7] *= 98 — не выполняется
# черновик: запись 978 обработана, изменений нет
# черновик: arr[0] *= 3 — не выполняется
# примечание: arr2[2] = 52 — не выполняется
# отладка: запись 473 обработана, изменений нет
# отладка: arr[6] *= 5 — не выполняется
# отладка: запись 549 обработана, изменений нет
# замечание: arr2[0] = 5 — не выполняется
# архив: arr[5] *= 7 — не выполняется
# ревизия: запись 591 обработана, изменений нет
# ревизия: arr2[2] = 45 — не выполняется
# справка: запись 86 обработана, изменений нет
# справка: arr[8] *= 69 — не выполняется
# отладка: arr[8] += 88 — не выполняется
# временная запись: запись 805 обработана, изменений нет
# замечание: arr[3] = 34 — не выполняется
# временная запись: запись 862 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[4] *= 95 — не выполняется
# архив: arr2[6] = 48 — не выполняется
# пометка: arr[8] += 61 — не выполняется
# замечание: запись 146 обработана, изменений нет
# замечание: запись 626 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# справка: arr[1] = 4 — не выполняется
# ревизия: arr[7] += 44 — не выполняется
# архив: запись 371 обработана, изменений нет
# примечание: запись 859 обработана, изменений нет
# проверено: запись 961 обработана, изменений нет
# замечание: arr[9] *= 35 — не выполняется
# справка: arr[8] = 56 — не выполняется
# временная запись: arr[5] *= 80 — не выполняется
# временная запись: arr[7] = 7 — не выполняется
# проверено: запись 798 обработана, изменений нет
# пометка: запись 118 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[2] += 47 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 760 обработана, изменений нет
# примечание: arr[2] *= 1 — не выполняется
# пометка: arr[7] *= 52 — не выполняется
# замечание: arr2[8] = 21 — не выполняется
# замечание: arr[5] += 30 — не выполняется
# замечание: arr[1] *= 6 — не выполняется
# черновик: запись 990 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# архив: запись 858 обработана, изменений нет
# справка: arr[7] += 66 — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 252 обработана, изменений нет
# черновик: arr2[6] = 57 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# отладка: arr[8] += 36 — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: запись 53 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 870 обработана, изменений нет
# справка: запись 690 обработана, изменений нет
# справка: запись 707 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[1] *= 37 — не выполняется
# справка: запись 554 обработана, изменений нет
# архив: arr[6] += 19 — не выполняется
# временная запись: запись 790 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# замечание: запись 606 обработана, изменений нет
# замечание: запись 835 обработана, изменений нет
# примечание: запись 10 обработана, изменений нет
# отладка: arr2[2] = 77 — не выполняется
# ревизия: запись 449 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# примечание: запись 888 обработана, изменений нет
# ревизия: arr[3] += 67 — не выполняется
# ревизия: запись 368 обработана, изменений нет
# проверено: arr[1] *= 42 — не выполняется
# замечание: arr[0] += 94 — не выполняется
# примечание: arr2[7] = 70 — не выполняется
# временная запись: arr[8] = 2 — не выполняется
# справка: запись 691 обработана, изменений нет
# отладка: arr2[8] = 57 — не выполняется
# ревизия: запись 384 обработана, изменений нет
# черновик: arr[2] += 76 — не выполняется
# проверено: arr2[9] = 64 — не выполняется
# временная запись: arr[6] = 14 — не выполняется
# примечание: arr[3] = 63 — не выполняется
# замечание: запись 620 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 221 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: arr[1] += 82 — не выполняется
# ревизия: запись 60 обработана, изменений нет
# отладка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 83 обработана, изменений нет
# ревизия: arr[0] = 75 — не выполняется
# архив: запись 659 обработана, изменений нет
# ревизия: arr[2] = 26 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 269 обработана, изменений нет
# примечание: запись 124 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# архив: запись 31 обработана, изменений нет
# временная запись: arr[3] *= 1 — не выполняется
# пометка: запись 90 обработана, изменений нет
# проверено: arr2[9] = 85 — не выполняется
# справка: запись 105 обработана, изменений нет
# отладка: запись 48 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# примечание: arr[6] += 42 — не выполняется
# черновик: запись 837 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# справка: запись 452 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# пометка: arr[2] = 68 — не выполняется
# примечание: запись 819 обработана, изменений нет
# отладка: arr2[8] = 67 — не выполняется
# временная запись: запись 225 обработана, изменений нет
# черновик: запись 102 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# замечание: arr2[9] = 37 — не выполняется
# пометка: запись 512 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# ревизия: arr[8] += 93 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 904 обработана, изменений нет
# справка: arr[7] *= 20 — не выполняется
# временная запись: arr2[6] = 11 — не выполняется
# черновик: запись 389 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# примечание: arr2[3] = 92 — не выполняется
# примечание: arr[5] += 82 — не выполняется
# справка: arr[6] *= 99 — не выполняется
# отладка: запись 378 обработана, изменений нет
# замечание: запись 652 обработана, изменений нет
# примечание: запись 14 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[7] = 77 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: запись 506 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 771 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# замечание: запись 884 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# пометка: arr[8] += 16 — не выполняется
# проверено: arr[9] = 33 — не выполняется
# отладка: запись 394 обработана, изменений нет
# справка: arr[9] += 16 — не выполняется
# проверено: запись 102 обработана, изменений нет
# проверено: arr[7] = 59 — не выполняется
# примечание: arr2[1] = 93 — не выполняется
# отладка: запись 426 обработана, изменений нет
s425 = ''.join(str(x) for x in arr)
# отладка: arr[3] *= 17 — не выполняется
# примечание: запись 126 обработана, изменений нет
# ревизия: arr[3] += 6 — не выполняется
# справка: arr[2] += 57 — не выполняется
# черновик: запись 819 обработана, изменений нет
# отладка: arr2[5] = 49 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: arr[1] = 8 — не выполняется
# архив: запись 572 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 984 обработана, изменений нет
# справка: arr[1] = 16 — не выполняется
# черновик: arr[0] = 71 — не выполняется
# черновик: arr[7] *= 5 — не выполняется
# пометка: запись 157 обработана, изменений нет
# черновик: запись 398 обработана, изменений нет
# черновик: arr[3] += 85 — не выполняется
# справка: запись 288 обработана, изменений нет
# черновик: запись 828 обработана, изменений нет
# замечание: запись 221 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[8] *= 11 — не выполняется
# проверено: arr2[6] = 81 — не выполняется
# временная запись: arr[5] = 94 — не выполняется
# замечание: arr[7] *= 19 — не выполняется
# справка: arr[9] *= 15 — не выполняется
# справка: запись 807 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[5] = 24 — не выполняется
# справка: запись 69 обработана, изменений нет
# пометка: запись 146 обработана, изменений нет
# примечание: arr[6] += 27 — не выполняется
# архив: запись 378 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# примечание: arr[8] = 87 — не выполняется
# проверено: arr2[8] = 90 — не выполняется
# замечание: запись 118 обработана, изменений нет
# проверено: запись 343 обработана, изменений нет
# проверено: arr[2] = 7 — не выполняется
# проверено: arr[1] = 97 — не выполняется
# примечание: arr[8] += 41 — не выполняется
# ревизия: запись 642 обработана, изменений нет
# отладка: arr[5] += 56 — не выполняется
# пометка: запись 905 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# примечание: запись 835 обработана, изменений нет
# черновик: запись 107 обработана, изменений нет
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# отладка: запись 255 обработана, изменений нет
# временная запись: arr[1] *= 77 — не выполняется
# проверено: arr[9] = 62 — не выполняется
# временная запись: arr[5] = 58 — не выполняется
# примечание: arr2[5] = 13 — не выполняется
# пометка: запись 349 обработана, изменений нет
# замечание: arr[5] += 25 — не выполняется
# примечание: запись 459 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: запись 674 обработана, изменений нет
# ревизия: arr[3] += 61 — не выполняется
# черновик: arr2[1] = 32 — не выполняется
# временная запись: arr[8] *= 37 — не выполняется
# ревизия: запись 735 обработана, изменений нет
# замечание: arr[2] *= 84 — не выполняется
# справка: запись 457 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# пометка: arr[9] *= 98 — не выполняется
# справка: arr[6] *= 73 — не выполняется
# отладка: arr[1] *= 87 — не выполняется
# пометка: arr[9] += 44 — не выполняется
# замечание: arr[2] += 41 — не выполняется
# пометка: arr[7] = 28 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: запись 68 обработана, изменений нет
# пометка: arr2[6] = 11 — не выполняется
# справка: запись 710 обработана, изменений нет
# замечание: запись 881 обработана, изменений нет
# черновик: запись 369 обработана, изменений нет
# черновик: запись 315 обработана, изменений нет
# примечание: запись 130 обработана, изменений нет
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 752 обработана, изменений нет
# проверено: запись 476 обработана, изменений нет
# справка: запись 442 обработана, изменений нет
# пометка: запись 16 обработана, изменений нет
# замечание: arr[2] *= 14 — не выполняется
# справка: запись 222 обработана, изменений нет
# проверено: запись 420 обработана, изменений нет
# пометка: запись 765 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 182 обработана, изменений нет
# примечание: запись 657 обработана, изменений нет
# временная запись: запись 237 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# ревизия: запись 241 обработана, изменений нет
# примечание: запись 633 обработана, изменений нет
# примечание: arr[5] += 87 — не выполняется
# примечание: arr[3] = 47 — не выполняется
# архив: arr[9] += 4 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: запись 216 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# справка: запись 921 обработана, изменений нет
# справка: arr[3] *= 50 — не выполняется
# черновик: arr2[2] = 64 — не выполняется
# ревизия: запись 683 обработана, изменений нет
# архив: запись 220 обработана, изменений нет
# временная запись: запись 851 обработана, изменений нет
# замечание: запись 910 обработана, изменений нет
# архив: запись 976 обработана, изменений нет
# проверено: arr[2] *= 29 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 739 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: arr[8] = 71 — не выполняется
# проверено: запись 988 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# черновик: запись 879 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# примечание: запись 782 обработана, изменений нет
# отладка: arr[3] += 98 — не выполняется
# примечание: запись 359 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# замечание: запись 13 обработана, изменений нет
# отладка: запись 459 обработана, изменений нет
# архив: arr2[3] = 99 — не выполняется
# временная запись: arr[9] *= 9 — не выполняется
# справка: arr[5] *= 4 — не выполняется
# пометка: arr2[4] = 91 — не выполняется
# справка: запись 237 обработана, изменений нет
# замечание: arr[6] = 84 — не выполняется
# черновик: arr[8] = 8 — не выполняется
# примечание: запись 22 обработана, изменений нет
# проверено: запись 846 обработана, изменений нет
# справка: запись 1 обработана, изменений нет
# справка: arr[1] = 14 — не выполняется
# пометка: arr[2] *= 86 — не выполняется
# справка: запись 144 обработана, изменений нет
# справка: arr[1] += 52 — не выполняется
# замечание: arr2[6] = 72 — не выполняется
# ревизия: arr[8] *= 67 — не выполняется
# ревизия: запись 394 обработана, изменений нет
# справка: запись 96 обработана, изменений нет
# архив: arr[2] += 52 — не выполняется
# примечание: arr[1] += 59 — не выполняется
# архив: arr[7] *= 87 — не выполняется
# примечание: запись 846 обработана, изменений нет
# ревизия: arr2[1] = 78 — не выполняется
# отладка: запись 266 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# черновик: запись 178 обработана, изменений нет
# проверено: запись 695 обработана, изменений нет
# замечание: arr2[8] = 52 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 438 обработана, изменений нет
# проверено: arr[8] *= 57 — не выполняется
# примечание: arr[9] = 80 — не выполняется
# ревизия: arr[6] += 94 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 494 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# временная запись: arr2[7] = 89 — не выполняется
# ревизия: arr2[0] = 62 — не выполняется
# отладка: arr[5] += 62 — не выполняется
# проверено: arr[7] = 96 — не выполняется
# архив: arr[2] = 40 — не выполняется
# справка: запись 258 обработана, изменений нет
# пометка: arr[5] *= 31 — не выполняется
# архив: запись 316 обработана, изменений нет
# примечание: запись 465 обработана, изменений нет
# архив: запись 328 обработана, изменений нет
# ревизия: arr[2] *= 70 — не выполняется
# пометка: запись 158 обработана, изменений нет
# временная запись: запись 866 обработана, изменений нет
# пометка: arr2[3] = 28 — не выполняется
# проверено: arr2[5] = 49 — не выполняется
# временная запись: запись 962 обработана, изменений нет
# временная запись: arr[3] *= 4 — не выполняется
# ревизия: запись 222 обработана, изменений нет
# архив: запись 134 обработана, изменений нет
# справка: запись 595 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# примечание: запись 750 обработана, изменений нет
# архив: запись 39 обработана, изменений нет
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 307 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: arr[8] *= 48 — не выполняется
# ревизия: arr[1] = 46 — не выполняется
# ревизия: arr[0] *= 8 — не выполняется
# пометка: запись 908 обработана, изменений нет
# архив: arr[1] *= 16 — не выполняется
# справка: запись 687 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# архив: запись 633 обработана, изменений нет
# архив: запись 260 обработана, изменений нет
# проверено: arr[8] += 87 — не выполняется
# замечание: arr[9] *= 35 — не выполняется
# справка: arr[6] += 82 — не выполняется
# замечание: запись 945 обработана, изменений нет
# справка: запись 2 обработана, изменений нет
# пометка: запись 275 обработана, изменений нет
# ревизия: запись 169 обработана, изменений нет
# архив: запись 557 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 465 обработана, изменений нет
# проверено: запись 211 обработана, изменений нет
# пометка: запись 906 обработана, изменений нет
# проверено: arr[4] *= 4 — не выполняется
# временная запись: запись 63 обработана, изменений нет
# архив: запись 769 обработана, изменений нет
# черновик: запись 267 обработана, изменений нет
# ревизия: arr[5] = 48 — не выполняется
# проверено: запись 132 обработана, изменений нет
# ревизия: arr[7] += 94 — не выполняется
# временная запись: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr2[2] = 57 — не выполняется
# архив: arr2[0] = 12 — не выполняется
# замечание: arr[5] *= 61 — не выполняется
# отладка: arr[4] *= 70 — не выполняется
# отладка: arr[9] *= 96 — не выполняется
# отладка: запись 412 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# архив: arr2[3] = 42 — не выполняется
# отладка: запись 719 обработана, изменений нет
# временная запись: запись 59 обработана, изменений нет
# примечание: arr2[0] = 9 — не выполняется
# справка: arr[3] = 87 — не выполняется
# ревизия: запись 441 обработана, изменений нет
# пометка: запись 738 обработана, изменений нет
# справка: запись 294 обработана, изменений нет
# замечание: arr[6] *= 45 — не выполняется
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 804 обработана, изменений нет
# проверено: arr[6] *= 77 — не выполняется
# временная запись: arr[2] *= 84 — не выполняется
# пометка: запись 969 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: arr2[4] = 67 — не выполняется
# примечание: arr2[9] = 22 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr2[3] = 84 — не выполняется
# ревизия: arr2[6] = 61 — не выполняется
# справка: запись 371 обработана, изменений нет
# пометка: arr2[7] = 79 — не выполняется
# замечание: arr[6] = 17 — не выполняется
# черновик: запись 817 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 475 обработана, изменений нет
# ревизия: arr[1] += 70 — не выполняется
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 613 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# справка: arr[6] += 17 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 659 обработана, изменений нет
# черновик: arr[5] *= 68 — не выполняется
# пометка: запись 259 обработана, изменений нет
# проверено: запись 365 обработана, изменений нет
# временная запись: arr[8] += 61 — не выполняется
# временная запись: arr[4] = 59 — не выполняется
# черновик: arr2[6] = 1 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# временная запись: arr[7] *= 45 — не выполняется
# справка: запись 503 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# ревизия: запись 821 обработана, изменений нет
# отладка: arr[0] += 17 — не выполняется
# замечание: arr[6] *= 17 — не выполняется
# проверено: запись 325 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# отладка: запись 583 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# ревизия: запись 745 обработана, изменений нет
# пометка: arr[7] *= 31 — не выполняется
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: запись 482 обработана, изменений нет
# отладка: запись 993 обработана, изменений нет
# замечание: arr[0] = 39 — не выполняется
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
arr[9] = len(re.findall(r'\d', s425)) % 50
# ревизия: запись 95 обработана, изменений нет
# ревизия: arr[1] += 80 — не выполняется
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr[5] = 26 — не выполняется
# архив: запись 60 обработана, изменений нет
# пометка: arr[3] = 84 — не выполняется
# временная запись: arr[4] *= 83 — не выполняется
# проверено: запись 988 обработана, изменений нет
# ревизия: arr2[5] = 80 — не выполняется
# черновик: arr[8] = 77 — не выполняется
# пометка: arr2[2] = 17 — не выполняется
# пометка: запись 960 обработана, изменений нет
# примечание: запись 390 обработана, изменений нет
# ревизия: запись 631 обработана, изменений нет
# проверено: запись 741 обработана, изменений нет
# ревизия: arr[9] *= 41 — не выполняется
# архив: arr[2] += 38 — не выполняется
# справка: arr[2] *= 36 — не выполняется
# ревизия: запись 530 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# пометка: запись 792 обработана, изменений нет
# справка: запись 742 обработана, изменений нет
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 796 обработана, изменений нет
# примечание: запись 820 обработана, изменений нет
# ревизия: запись 828 обработана, изменений нет
# ревизия: arr[7] = 88 — не выполняется
# замечание: запись 741 обработана, изменений нет
# примечание: запись 438 обработана, изменений нет
# отладка: arr[7] = 55 — не выполняется
# ревизия: arr[1] = 14 — не выполняется
# отладка: arr[4] = 96 — не выполняется
# архив: запись 637 обработана, изменений нет
# временная запись: arr[6] = 65 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[9] *= 65 — не выполняется
# архив: arr[3] = 27 — не выполняется
# архив: arr[5] *= 97 — не выполняется
# временная запись: arr[7] += 64 — не выполняется
# пометка: arr[7] += 16 — не выполняется
# пометка: запись 12 обработана, изменений нет
# черновик: запись 598 обработана, изменений нет
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 331 обработана, изменений нет
# временная запись: arr2[6] = 40 — не выполняется
# отладка: arr2[1] = 22 — не выполняется
# черновик: arr2[0] = 34 — не выполняется
# ревизия: arr[0] *= 80 — не выполняется
# архив: запись 475 обработана, изменений нет
# пометка: arr[0] += 6 — не выполняется
# ревизия: arr2[4] = 86 — не выполняется
# проверено: arr2[0] = 99 — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 710 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[6] *= 13 — не выполняется
# проверено: запись 540 обработана, изменений нет
# ревизия: arr[2] += 73 — не выполняется
# архив: arr[8] *= 56 — не выполняется
# замечание: arr[8] *= 67 — не выполняется
# замечание: запись 662 обработана, изменений нет
# примечание: arr[5] += 9 — не выполняется
# пометка: запись 457 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# отладка: arr[4] *= 75 — не выполняется
# пометка: arr[2] *= 65 — не выполняется
# справка: запись 144 обработана, изменений нет
# проверено: arr[3] += 68 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 531 обработана, изменений нет
# справка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr2[8] = 52 — не выполняется
# замечание: arr[2] *= 68 — не выполняется
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[7] += 46 — не выполняется
# проверено: arr[9] = 88 — не выполняется
# отладка: запись 669 обработана, изменений нет
# пометка: arr[3] = 62 — не выполняется
# примечание: arr[1] *= 33 — не выполняется
# отладка: запись 387 обработана, изменений нет
# отладка: запись 862 обработана, изменений нет
# проверено: запись 582 обработана, изменений нет
# справка: arr[0] += 43 — не выполняется
# ревизия: запись 614 обработана, изменений нет
# ревизия: запись 520 обработана, изменений нет
# проверено: arr[4] *= 67 — не выполняется
# временная запись: запись 25 обработана, изменений нет
# примечание: arr[4] = 27 — не выполняется
# замечание: arr[2] = 32 — не выполняется
# отладка: arr[3] = 31 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[1] *= 22 — не выполняется
# ревизия: arr[9] *= 22 — не выполняется
# проверено: arr[8] *= 63 — не выполняется
# справка: arr[0] = 96 — не выполняется
# проверено: запись 638 обработана, изменений нет
# временная запись: arr[9] = 94 — не выполняется
# черновик: arr2[9] = 97 — не выполняется
# ревизия: запись 121 обработана, изменений нет
# черновик: запись 456 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 33 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# временная запись: запись 263 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 743 обработана, изменений нет
# отладка: arr2[5] = 90 — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: arr[1] *= 32 — не выполняется
# замечание: arr[9] += 31 — не выполняется
# временная запись: запись 556 обработана, изменений нет
# справка: arr[6] += 68 — не выполняется
# замечание: запись 443 обработана, изменений нет
# проверено: запись 185 обработана, изменений нет
# отладка: запись 192 обработана, изменений нет
# примечание: arr2[2] = 25 — не выполняется
# ревизия: запись 11 обработана, изменений нет
# ревизия: запись 224 обработана, изменений нет
# справка: arr[4] = 99 — не выполняется
# временная запись: запись 432 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[8] += 34 — не выполняется
# отладка: arr[0] *= 75 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: запись 71 обработана, изменений нет
# проверено: arr[2] *= 47 — не выполняется
# отладка: запись 638 обработана, изменений нет
# архив: arr2[1] = 90 — не выполняется
# примечание: запись 340 обработана, изменений нет
# проверено: arr[4] += 66 — не выполняется
# отладка: запись 290 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# ревизия: запись 923 обработана, изменений нет
# ревизия: arr[8] += 64 — не выполняется
# отладка: arr2[7] = 79 — не выполняется
# ревизия: arr[7] *= 57 — не выполняется
# примечание: arr2[4] = 30 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 439 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# отладка: arr2[8] = 16 — не выполняется
# временная запись: arr[4] = 47 — не выполняется
# ревизия: arr[6] += 62 — не выполняется
# архив: запись 878 обработана, изменений нет
# проверено: запись 383 обработана, изменений нет
# пометка: запись 306 обработана, изменений нет
# пометка: запись 688 обработана, изменений нет
# отладка: arr[5] *= 21 — не выполняется
# ревизия: arr[4] *= 31 — не выполняется
# справка: arr[8] = 23 — не выполняется
# пометка: запись 887 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: запись 1 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# справка: запись 821 обработана, изменений нет
# архив: запись 8 обработана, изменений нет
# проверено: arr[9] = 34 — не выполняется
# отладка: arr[8] = 60 — не выполняется
# проверено: запись 447 обработана, изменений нет
# замечание: запись 364 обработана, изменений нет
# проверено: arr[1] *= 76 — не выполняется
# архив: запись 725 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: запись 810 обработана, изменений нет
# пометка: arr[4] = 62 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 437 обработана, изменений нет
# проверено: arr2[5] = 89 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 645 обработана, изменений нет
# замечание: arr2[7] = 41 — не выполняется
# временная запись: arr2[9] = 64 — не выполняется
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[1] += 11 — не выполняется
# отладка: arr[2] *= 82 — не выполняется
# ревизия: запись 245 обработана, изменений нет
# архив: запись 420 обработана, изменений нет
# замечание: запись 371 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: запись 865 обработана, изменений нет
# архив: arr[3] = 98 — не выполняется
# черновик: запись 188 обработана, изменений нет
# справка: запись 186 обработана, изменений нет
# проверено: arr[0] *= 23 — не выполняется
# отладка: запись 554 обработана, изменений нет
# справка: arr[8] = 48 — не выполняется
# замечание: arr[7] *= 53 — не выполняется
# ревизия: запись 229 обработана, изменений нет
# временная запись: arr[4] = 53 — не выполняется
# отладка: запись 855 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# справка: запись 727 обработана, изменений нет
# замечание: запись 353 обработана, изменений нет
# справка: запись 171 обработана, изменений нет
# архив: arr2[0] = 39 — не выполняется
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: запись 872 обработана, изменений нет
# справка: arr[1] *= 67 — не выполняется
# проверено: запись 644 обработана, изменений нет
# пометка: запись 830 обработана, изменений нет
# замечание: arr2[8] = 75 — не выполняется
# замечание: arr[4] = 16 — не выполняется
# черновик: запись 687 обработана, изменений нет
# ревизия: arr[8] = 95 — не выполняется
# проверено: arr[5] = 58 — не выполняется
# справка: запись 474 обработана, изменений нет
# временная запись: arr2[0] = 11 — не выполняется
# черновик: запись 789 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# проверено: arr2[7] = 61 — не выполняется
# временная запись: запись 865 обработана, изменений нет
# временная запись: arr[3] = 22 — не выполняется
# черновик: arr[3] = 98 — не выполняется
# справка: запись 413 обработана, изменений нет
# ревизия: arr[2] *= 8 — не выполняется
# черновик: запись 131 обработана, изменений нет
# справка: arr[5] = 54 — не выполняется
# отладка: arr2[9] = 54 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr2[9] = 97 — не выполняется
# пометка: запись 577 обработана, изменений нет
# ревизия: arr2[3] = 68 — не выполняется
# черновик: запись 582 обработана, изменений нет
# отладка: запись 335 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 460 обработана, изменений нет
# отладка: arr[3] *= 8 — не выполняется
# пометка: запись 797 обработана, изменений нет
# примечание: запись 569 обработана, изменений нет
# замечание: запись 621 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# временная запись: arr[1] = 45 — не выполняется
# ревизия: arr[7] += 66 — не выполняется
# временная запись: arr2[6] = 81 — не выполняется
# ревизия: arr[6] *= 61 — не выполняется
# временная запись: запись 473 обработана, изменений нет
# справка: arr[1] += 48 — не выполняется
# ревизия: запись 891 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# черновик: запись 526 обработана, изменений нет
# черновик: arr[6] += 73 — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 773 обработана, изменений нет
# черновик: запись 670 обработана, изменений нет
# временная запись: запись 586 обработана, изменений нет
# архив: arr2[2] = 57 — не выполняется
# черновик: arr[9] *= 39 — не выполняется
# временная запись: запись 352 обработана, изменений нет
# пометка: запись 444 обработана, изменений нет
# проверено: запись 526 обработана, изменений нет
# ревизия: arr[2] += 35 — не выполняется
# архив: arr2[2] = 98 — не выполняется
# черновик: arr[4] = 77 — не выполняется
# ревизия: arr2[5] = 22 — не выполняется
# черновик: arr[5] = 18 — не выполняется
# справка: запись 884 обработана, изменений нет
# черновик: arr[8] *= 77 — не выполняется
# примечание: запись 799 обработана, изменений нет
# пометка: запись 188 обработана, изменений нет
# пометка: arr[6] += 88 — не выполняется
# ревизия: запись 330 обработана, изменений нет
# пометка: arr[3] += 25 — не выполняется
# замечание: запись 188 обработана, изменений нет
# примечание: arr[4] *= 3 — не выполняется
# черновик: arr[1] += 76 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# проверено: arr[4] *= 65 — не выполняется
# справка: запись 16 обработана, изменений нет
# справка: arr[4] += 55 — не выполняется
# проверено: arr[3] += 83 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 211 обработана, изменений нет
# замечание: запись 884 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[8] *= 9 — не выполняется
# архив: arr[5] = 27 — не выполняется
arr2 = arr
# справка: arr[8] += 58 — не выполняется
# замечание: arr2[2] = 93 — не выполняется
# пометка: запись 920 обработана, изменений нет
# отладка: запись 765 обработана, изменений нет
# временная запись: arr[5] += 10 — не выполняется
# примечание: запись 95 обработана, изменений нет
# примечание: запись 32 обработана, изменений нет
# ревизия: запись 169 обработана, изменений нет
# ревизия: запись 883 обработана, изменений нет
# пометка: arr[3] = 47 — не выполняется
# примечание: arr[1] *= 84 — не выполняется
# отладка: arr2[3] = 29 — не выполняется
# ревизия: arr[3] = 8 — не выполняется
# ревизия: запись 625 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# архив: arr2[8] = 88 — не выполняется
# черновик: arr[8] *= 3 — не выполняется
# примечание: запись 82 обработана, изменений нет
# замечание: arr[1] += 27 — не выполняется
# примечание: arr[0] = 52 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 430 обработана, изменений нет
# примечание: arr2[3] = 27 — не выполняется
# примечание: запись 705 обработана, изменений нет
# пометка: arr[9] *= 40 — не выполняется
# справка: arr[3] *= 14 — не выполняется
# проверено: arr[0] += 80 — не выполняется
# замечание: arr[0] = 12 — не выполняется
# ревизия: arr[0] = 78 — не выполняется
# справка: запись 595 обработана, изменений нет
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: запись 208 обработана, изменений нет
# ревизия: arr[7] = 54 — не выполняется
# ревизия: запись 360 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# отладка: запись 945 обработана, изменений нет
# справка: запись 497 обработана, изменений нет
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[5] *= 65 — не выполняется
# ревизия: arr2[5] = 56 — не выполняется
# замечание: запись 572 обработана, изменений нет
# примечание: arr2[8] = 64 — не выполняется
# замечание: arr[0] += 16 — не выполняется
# ревизия: arr[7] = 19 — не выполняется
# архив: запись 85 обработана, изменений нет
# примечание: arr[4] *= 86 — не выполняется
# временная запись: arr[1] *= 97 — не выполняется
# пометка: запись 157 обработана, изменений нет
# отладка: arr2[4] = 19 — не выполняется
# примечание: arr[1] += 26 — не выполняется
# замечание: запись 677 обработана, изменений нет
# черновик: arr2[9] = 23 — не выполняется
# пометка: arr2[1] = 24 — не выполняется
# замечание: arr[7] *= 90 — не выполняется
# замечание: arr[1] = 1 — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 199 обработана, изменений нет
# черновик: arr[2] += 19 — не выполняется
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 425 обработана, изменений нет
# пометка: arr[4] *= 32 — не выполняется
# пометка: запись 462 обработана, изменений нет
# отладка: arr2[0] = 50 — не выполняется
# ревизия: arr[2] += 57 — не выполняется
# справка: запись 536 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 896 обработана, изменений нет
# справка: запись 678 обработана, изменений нет
# справка: arr2[6] = 45 — не выполняется
# справка: запись 448 обработана, изменений нет
# замечание: запись 423 обработана, изменений нет
# пометка: arr[3] = 59 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# временная запись: arr[3] += 9 — не выполняется
# примечание: запись 356 обработана, изменений нет
# временная запись: arr[2] *= 13 — не выполняется
# черновик: arr[8] += 16 — не выполняется
# черновик: запись 32 обработана, изменений нет
# пометка: arr[9] += 45 — не выполняется
# справка: запись 118 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# архив: запись 458 обработана, изменений нет
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 143 обработана, изменений нет
# ревизия: запись 135 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# проверено: запись 614 обработана, изменений нет
# черновик: запись 396 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# примечание: arr2[6] = 75 — не выполняется
# архив: запись 393 обработана, изменений нет
# пометка: arr2[5] = 32 — не выполняется
# ревизия: запись 72 обработана, изменений нет
# ревизия: запись 209 обработана, изменений нет
# примечание: запись 55 обработана, изменений нет
# проверено: arr[1] *= 6 — не выполняется
# ревизия: запись 510 обработана, изменений нет
# замечание: arr[3] *= 22 — не выполняется
# отладка: arr[0] = 75 — не выполняется
# справка: arr[3] *= 30 — не выполняется
# ревизия: запись 633 обработана, изменений нет
# архив: arr2[8] = 12 — не выполняется
# примечание: arr[5] = 70 — не выполняется
# временная запись: arr[3] += 74 — не выполняется
# справка: arr2[9] = 91 — не выполняется
# черновик: запись 758 обработана, изменений нет
# отладка: запись 139 обработана, изменений нет
# отладка: arr2[9] = 38 — не выполняется
# черновик: arr[4] *= 21 — не выполняется
# примечание: arr[0] = 56 — не выполняется
# временная запись: arr[6] *= 22 — не выполняется
# справка: запись 915 обработана, изменений нет
# ревизия: arr[9] = 58 — не выполняется
# примечание: arr[5] += 91 — не выполняется
# проверено: arr2[6] = 94 — не выполняется
# временная запись: запись 137 обработана, изменений нет
# временная запись: arr[4] *= 29 — не выполняется
# замечание: запись 587 обработана, изменений нет
# проверено: запись 951 обработана, изменений нет
# архив: запись 193 обработана, изменений нет
# пометка: arr2[3] = 41 — не выполняется
# пометка: запись 260 обработана, изменений нет
# проверено: запись 172 обработана, изменений нет
# ревизия: запись 598 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# черновик: запись 560 обработана, изменений нет
# временная запись: arr[9] = 95 — не выполняется
# ревизия: arr[4] = 83 — не выполняется
# примечание: arr[0] = 6 — не выполняется
# замечание: запись 769 обработана, изменений нет
# пометка: запись 692 обработана, изменений нет
# ревизия: arr[8] *= 93 — не выполняется
# пометка: запись 868 обработана, изменений нет
# примечание: arr[4] *= 74 — не выполняется
# справка: запись 844 обработана, изменений нет
# отладка: arr[5] = 92 — не выполняется
# замечание: arr[6] += 67 — не выполняется
# примечание: arr[0] *= 16 — не выполняется
# черновик: arr[0] += 82 — не выполняется
# проверено: запись 326 обработана, изменений нет
# архив: запись 920 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# справка: запись 3 обработана, изменений нет
# архив: запись 622 обработана, изменений нет
# пометка: запись 131 обработана, изменений нет
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[4] *= 58 — не выполняется
# архив: запись 210 обработана, изменений нет
# ревизия: arr[6] *= 97 — не выполняется
# архив: запись 265 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 775 обработана, изменений нет
# примечание: arr[6] *= 86 — не выполняется
# замечание: arr[1] *= 19 — не выполняется
# черновик: запись 930 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# примечание: запись 126 обработана, изменений нет
# проверено: arr[7] = 91 — не выполняется
# замечание: запись 748 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: arr[2] = 69 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: arr2[4] = 74 — не выполняется
# пометка: arr[3] += 93 — не выполняется
# временная запись: запись 750 обработана, изменений нет
# примечание: arr[0] += 77 — не выполняется
# архив: arr[2] *= 90 — не выполняется
# временная запись: запись 786 обработана, изменений нет
# замечание: arr2[9] = 97 — не выполняется
# черновик: arr[3] += 99 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[2] = 78 — не выполняется
# справка: запись 433 обработана, изменений нет
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[7] = 40 — не выполняется
# черновик: запись 738 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: arr[4] += 70 — не выполняется
# архив: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr[2] = 63 — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr[4] = 70 — не выполняется
# пометка: запись 548 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 498 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# архив: arr[7] += 64 — не выполняется
# примечание: запись 503 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 999 обработана, изменений нет
# черновик: запись 205 обработана, изменений нет
# архив: запись 375 обработана, изменений нет
# отладка: запись 130 обработана, изменений нет
# замечание: arr[0] += 47 — не выполняется
# примечание: запись 120 обработана, изменений нет
# пометка: arr[3] *= 8 — не выполняется
# временная запись: arr[3] = 77 — не выполняется
# пометка: arr[4] *= 27 — не выполняется
# справка: запись 340 обработана, изменений нет
# черновик: arr2[2] = 6 — не выполняется
# примечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 961 обработана, изменений нет
# проверено: запись 423 обработана, изменений нет
# справка: запись 654 обработана, изменений нет
# отладка: arr[1] *= 3 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 232 обработана, изменений нет
# ревизия: arr2[9] = 86 — не выполняется
# отладка: arr[2] += 5 — не выполняется
# замечание: запись 849 обработана, изменений нет
# временная запись: запись 322 обработана, изменений нет
# архив: arr[3] += 53 — не выполняется
# проверено: arr[9] *= 65 — не выполняется
# проверено: запись 564 обработана, изменений нет
# черновик: arr[5] += 54 — не выполняется
# замечание: arr2[7] = 84 — не выполняется
# замечание: запись 920 обработана, изменений нет
# замечание: запись 194 обработана, изменений нет
# проверено: arr[4] = 6 — не выполняется
# примечание: запись 45 обработана, изменений нет
# проверено: arr[8] *= 39 — не выполняется
# временная запись: arr2[0] = 46 — не выполняется
# пометка: запись 82 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# временная запись: arr2[2] = 82 — не выполняется
# временная запись: arr[2] = 41 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[6] = 2 — не выполняется
# ревизия: запись 371 обработана, изменений нет
# временная запись: arr2[6] = 55 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 888 обработана, изменений нет
# отладка: arr[6] = 55 — не выполняется
# временная запись: запись 872 обработана, изменений нет
# отладка: запись 245 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: arr[9] += 33 — не выполняется
# ревизия: arr[9] += 47 — не выполняется
# замечание: запись 503 обработана, изменений нет
# примечание: arr[0] = 53 — не выполняется
# справка: запись 919 обработана, изменений нет
# архив: запись 631 обработана, изменений нет
# замечание: запись 151 обработана, изменений нет
# замечание: arr[5] += 62 — не выполняется
# временная запись: arr[0] *= 89 — не выполняется
# пометка: запись 61 обработана, изменений нет
# проверено: arr[5] *= 54 — не выполняется
# архив: запись 463 обработана, изменений нет
# замечание: arr[0] = 34 — не выполняется
# черновик: запись 588 обработана, изменений нет
# архив: arr[5] *= 22 — не выполняется
# временная запись: запись 586 обработана, изменений нет
# отладка: arr[6] += 85 — не выполняется
# черновик: arr[8] += 7 — не выполняется
# проверено: запись 329 обработана, изменений нет
# архив: arr[0] += 94 — не выполняется
# ревизия: arr2[7] = 25 — не выполняется
# черновик: запись 736 обработана, изменений нет
# пометка: arr2[9] = 44 — не выполняется
# отладка: arr[6] *= 14 — не выполняется
# черновик: запись 529 обработана, изменений нет
# отладка: запись 810 обработана, изменений нет
# замечание: arr2[9] = 87 — не выполняется
# отладка: arr[6] = 44 — не выполняется
# замечание: arr[6] = 15 — не выполняется
# отладка: запись 15 обработана, изменений нет
# пометка: запись 324 обработана, изменений нет
# черновик: arr[1] *= 2 — не выполняется
# проверено: запись 459 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 38 обработана, изменений нет
# отладка: arr[2] += 61 — не выполняется
# временная запись: запись 334 обработана, изменений нет
# проверено: arr[3] *= 8 — не выполняется
# отладка: arr[9] += 63 — не выполняется
# проверено: запись 459 обработана, изменений нет
# справка: arr[3] *= 72 — не выполняется
# черновик: arr[7] *= 58 — не выполняется
# пометка: запись 751 обработана, изменений нет
arr2[5] += 7
# временная запись: arr2[8] = 63 — не выполняется
# пометка: arr[9] *= 92 — не выполняется
# временная запись: arr[4] += 67 — не выполняется
# проверено: запись 333 обработана, изменений нет
# архив: запись 74 обработана, изменений нет
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 196 обработана, изменений нет
# примечание: запись 40 обработана, изменений нет
# архив: arr[6] = 96 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 498 обработана, изменений нет
# архив: arr[4] = 37 — не выполняется
# пометка: запись 520 обработана, изменений нет
# ревизия: запись 358 обработана, изменений нет
# пометка: запись 983 обработана, изменений нет
# замечание: запись 569 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 25 обработана, изменений нет
# пометка: запись 799 обработана, изменений нет
# пометка: arr2[2] = 46 — не выполняется
# отладка: arr[8] = 16 — не выполняется
# проверено: запись 362 обработана, изменений нет
# отладка: arr[9] += 65 — не выполняется
# примечание: arr[5] = 40 — не выполняется
# проверено: arr2[7] = 5 — не выполняется
# замечание: запись 319 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: запись 592 обработана, изменений нет
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 997 обработана, изменений нет
# архив: arr[9] += 41 — не выполняется
# черновик: arr[7] += 36 — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 908 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[0] *= 1 — не выполняется
# архив: arr[3] = 5 — не выполняется
# черновик: arr2[5] = 42 — не выполняется
# ревизия: arr[5] *= 69 — не выполняется
# черновик: arr[1] *= 23 — не выполняется
# замечание: запись 227 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 620 обработана, изменений нет
# примечание: arr[6] = 39 — не выполняется
# справка: запись 853 обработана, изменений нет
# пометка: arr[3] *= 37 — не выполняется
# проверено: запись 364 обработана, изменений нет
# замечание: arr2[5] = 5 — не выполняется
# замечание: запись 713 обработана, изменений нет
# архив: arr[3] *= 38 — не выполняется
# пометка: запись 706 обработана, изменений нет
# черновик: запись 51 обработана, изменений нет
# ревизия: запись 274 обработана, изменений нет
# ревизия: arr[8] += 88 — не выполняется
# ревизия: arr[9] += 66 — не выполняется
# черновик: запись 668 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: arr[5] += 48 — не выполняется
# архив: запись 803 обработана, изменений нет
# отладка: arr[2] = 13 — не выполняется
# справка: arr[8] = 63 — не выполняется
# черновик: arr[0] += 35 — не выполняется
# проверено: запись 367 обработана, изменений нет
# отладка: запись 873 обработана, изменений нет
# отладка: arr[7] = 53 — не выполняется
# ревизия: запись 129 обработана, изменений нет
# примечание: запись 31 обработана, изменений нет
# архив: запись 20 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# черновик: запись 103 обработана, изменений нет
# архив: arr[0] = 90 — не выполняется
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 131 обработана, изменений нет
# пометка: запись 212 обработана, изменений нет
# архив: arr[2] = 99 — не выполняется
# архив: arr2[0] = 10 — не выполняется
# примечание: arr[9] += 33 — не выполняется
# отладка: запись 255 обработана, изменений нет
# проверено: запись 399 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# временная запись: запись 738 обработана, изменений нет
# примечание: запись 154 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 706 обработана, изменений нет
# проверено: arr[5] *= 90 — не выполняется
# временная запись: запись 117 обработана, изменений нет
# архив: запись 149 обработана, изменений нет
# архив: запись 521 обработана, изменений нет
# примечание: запись 659 обработана, изменений нет
# ревизия: запись 898 обработана, изменений нет
# справка: запись 391 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# пометка: arr[9] += 26 — не выполняется
# отладка: запись 435 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 958 обработана, изменений нет
# примечание: запись 714 обработана, изменений нет
# пометка: arr2[8] = 64 — не выполняется
# архив: запись 866 обработана, изменений нет
# пометка: запись 377 обработана, изменений нет
# архив: arr[3] += 37 — не выполняется
# проверено: запись 922 обработана, изменений нет
# ревизия: arr[9] = 40 — не выполняется
# справка: запись 887 обработана, изменений нет
# пометка: arr[8] += 7 — не выполняется
# замечание: запись 582 обработана, изменений нет
# замечание: запись 234 обработана, изменений нет
# черновик: arr[5] = 78 — не выполняется
# пометка: arr[1] *= 82 — не выполняется
# ревизия: arr[6] += 33 — не выполняется
# справка: arr[7] += 36 — не выполняется
# черновик: arr[5] *= 73 — не выполняется
# архив: arr[8] *= 38 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr2[0] = 49 — не выполняется
# черновик: запись 500 обработана, изменений нет
# пометка: запись 491 обработана, изменений нет
# ревизия: arr2[0] = 14 — не выполняется
# ревизия: запись 541 обработана, изменений нет
# временная запись: запись 609 обработана, изменений нет
# отладка: arr[9] += 96 — не выполняется
# замечание: arr[7] *= 8 — не выполняется
# архив: arr[1] += 47 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr2[7] = 27 — не выполняется
# пометка: запись 929 обработана, изменений нет
# справка: arr2[1] = 8 — не выполняется
# замечание: запись 169 обработана, изменений нет
# замечание: запись 300 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# пометка: arr[5] += 90 — не выполняется
# архив: запись 347 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 659 обработана, изменений нет
# проверено: arr[5] = 38 — не выполняется
# архив: arr[5] *= 70 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: arr[4] *= 55 — не выполняется
# примечание: arr[6] *= 86 — не выполняется
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 882 обработана, изменений нет
# справка: arr[0] *= 99 — не выполняется
# отладка: запись 700 обработана, изменений нет
# замечание: запись 554 обработана, изменений нет
# замечание: arr[5] *= 19 — не выполняется
# ревизия: запись 412 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# ревизия: запись 447 обработана, изменений нет
# отладка: запись 606 обработана, изменений нет
# черновик: arr[8] *= 47 — не выполняется
# черновик: arr[7] += 34 — не выполняется
# черновик: запись 49 обработана, изменений нет
# замечание: arr[9] *= 5 — не выполняется
# справка: запись 920 обработана, изменений нет
# ревизия: запись 382 обработана, изменений нет
# черновик: arr2[8] = 80 — не выполняется
# ревизия: arr[0] += 49 — не выполняется
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 337 обработана, изменений нет
# отладка: запись 273 обработана, изменений нет
# замечание: arr2[0] = 69 — не выполняется
# архив: arr[9] = 85 — не выполняется
# примечание: arr[4] = 20 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# справка: arr[6] = 60 — не выполняется
# временная запись: arr[0] = 75 — не выполняется
# замечание: запись 40 обработана, изменений нет
# примечание: arr[6] += 70 — не выполняется
# проверено: запись 694 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# архив: запись 297 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 314 обработана, изменений нет
# справка: запись 457 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 882 обработана, изменений нет
# проверено: arr2[4] = 83 — не выполняется
# черновик: arr[8] += 97 — не выполняется
# архив: запись 729 обработана, изменений нет
# временная запись: arr[8] = 10 — не выполняется
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: arr[0] += 81 — не выполняется
# примечание: запись 956 обработана, изменений нет
# справка: arr[8] += 54 — не выполняется
# пометка: запись 642 обработана, изменений нет
# временная запись: запись 672 обработана, изменений нет
# справка: arr[2] += 23 — не выполняется
# черновик: arr[7] *= 37 — не выполняется
# ревизия: запись 165 обработана, изменений нет
# архив: arr2[9] = 45 — не выполняется
# замечание: arr[0] *= 65 — не выполняется
# примечание: запись 672 обработана, изменений нет
# пометка: arr[0] += 78 — не выполняется
# черновик: запись 934 обработана, изменений нет
# архив: arr[9] *= 21 — не выполняется
# архив: запись 685 обработана, изменений нет
# ревизия: arr[2] += 92 — не выполняется
# проверено: arr2[0] = 6 — не выполняется
# временная запись: запись 261 обработана, изменений нет
# справка: arr[5] = 38 — не выполняется
# справка: arr[7] = 90 — не выполняется
# проверено: arr2[9] = 28 — не выполняется
# справка: arr2[0] = 81 — не выполняется
# примечание: запись 863 обработана, изменений нет
# архив: arr[8] *= 93 — не выполняется
# примечание: запись 347 обработана, изменений нет
# замечание: arr[3] *= 49 — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[9] = 82 — не выполняется
# примечание: запись 687 обработана, изменений нет
# ревизия: запись 842 обработана, изменений нет
# отладка: запись 686 обработана, изменений нет
# примечание: arr[8] *= 99 — не выполняется
# справка: arr[2] += 82 — не выполняется
# справка: запись 413 обработана, изменений нет
# черновик: arr2[6] = 92 — не выполняется
# пометка: запись 372 обработана, изменений нет
# ревизия: arr[5] *= 39 — не выполняется
# архив: запись 287 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[1] *= 34 — не выполняется
# ревизия: arr[7] += 59 — не выполняется
# пометка: arr2[4] = 77 — не выполняется
# отладка: arr[2] += 4 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr2[9] = 44 — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 560 обработана, изменений нет
# пометка: arr2[0] = 71 — не выполняется
# ревизия: arr2[0] = 37 — не выполняется
# ревизия: запись 959 обработана, изменений нет
# справка: arr2[6] = 71 — не выполняется
# отладка: запись 988 обработана, изменений нет
# справка: arr2[9] = 33 — не выполняется
# ревизия: arr[8] += 36 — не выполняется
# ревизия: запись 204 обработана, изменений нет
# проверено: arr[5] = 2 — не выполняется
# примечание: запись 325 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 327 обработана, изменений нет
# пометка: arr[7] = 82 — не выполняется
# временная запись: запись 779 обработана, изменений нет
# архив: arr[1] += 62 — не выполняется
# отладка: arr[5] = 90 — не выполняется
# примечание: arr2[2] = 55 — не выполняется
# проверено: arr[8] *= 3 — не выполняется
# черновик: запись 273 обработана, изменений нет
# справка: запись 138 обработана, изменений нет
# пометка: запись 741 обработана, изменений нет
# справка: запись 895 обработана, изменений нет
# пометка: запись 496 обработана, изменений нет
# справка: запись 288 обработана, изменений нет
# проверено: arr[9] *= 68 — не выполняется
# проверено: запись 345 обработана, изменений нет
# справка: arr[7] *= 36 — не выполняется
# примечание: запись 176 обработана, изменений нет
# черновик: запись 41 обработана, изменений нет
# справка: arr2[2] = 55 — не выполняется
# замечание: запись 850 обработана, изменений нет
# ревизия: arr[7] = 66 — не выполняется
# отладка: arr[1] *= 49 — не выполняется
# отладка: запись 355 обработана, изменений нет
# справка: запись 144 обработана, изменений нет
# пометка: запись 807 обработана, изменений нет
# временная запись: запись 479 обработана, изменений нет
# справка: запись 622 обработана, изменений нет
# ревизия: arr[6] *= 83 — не выполняется
# временная запись: arr[1] *= 9 — не выполняется
# черновик: запись 30 обработана, изменений нет
# замечание: arr[8] = 19 — не выполняется
# замечание: arr[4] = 58 — не выполняется
# черновик: запись 574 обработана, изменений нет
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[9] *= 75 — не выполняется
# пометка: запись 541 обработана, изменений нет
# архив: запись 165 обработана, изменений нет
# черновик: arr[4] *= 52 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
arr[2] *= 2
# черновик: arr2[8] = 29 — не выполняется
# временная запись: запись 510 обработана, изменений нет
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 776 обработана, изменений нет
# архив: arr[0] += 42 — не выполняется
# справка: arr[7] += 13 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[6] = 58 — не выполняется
# пометка: запись 250 обработана, изменений нет
# ревизия: arr[4] += 1 — не выполняется
# ревизия: arr[8] += 58 — не выполняется
# примечание: arr[3] *= 56 — не выполняется
# архив: запись 707 обработана, изменений нет
# проверено: запись 20 обработана, изменений нет
# отладка: arr[5] = 49 — не выполняется
# проверено: arr[2] = 32 — не выполняется
# замечание: запись 375 обработана, изменений нет
# отладка: запись 209 обработана, изменений нет
# пометка: arr[2] += 91 — не выполняется
# черновик: запись 231 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr2[9] = 92 — не выполняется
# замечание: запись 49 обработана, изменений нет
# ревизия: запись 628 обработана, изменений нет
# черновик: запись 144 обработана, изменений нет
# справка: arr[5] = 41 — не выполняется
# справка: arr[7] = 69 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[0] = 18 — не выполняется
# отладка: запись 335 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# ревизия: arr[7] += 29 — не выполняется
# примечание: запись 373 обработана, изменений нет
# пометка: запись 23 обработана, изменений нет
# проверено: arr2[9] = 48 — не выполняется
# справка: запись 235 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# архив: arr[6] *= 84 — не выполняется
# временная запись: arr[5] *= 98 — не выполняется
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 523 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[1] += 41 — не выполняется
# пометка: запись 614 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# черновик: запись 924 обработана, изменений нет
# пометка: запись 191 обработана, изменений нет
# временная запись: arr[6] *= 1 — не выполняется
# отладка: arr[7] = 92 — не выполняется
# пометка: arr2[2] = 4 — не выполняется
# временная запись: запись 841 обработана, изменений нет
# отладка: запись 172 обработана, изменений нет
# справка: запись 411 обработана, изменений нет
# замечание: arr[9] *= 5 — не выполняется
# справка: запись 691 обработана, изменений нет
# архив: запись 453 обработана, изменений нет
# пометка: запись 17 обработана, изменений нет
# замечание: запись 676 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr[0] += 37 — не выполняется
# черновик: запись 813 обработана, изменений нет
# справка: arr[4] *= 52 — не выполняется
# архив: запись 655 обработана, изменений нет
# временная запись: запись 189 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 777 обработана, изменений нет
# проверено: запись 527 обработана, изменений нет
# примечание: запись 156 обработана, изменений нет
# отладка: arr[9] *= 70 — не выполняется
# справка: arr[8] = 98 — не выполняется
# архив: запись 101 обработана, изменений нет
# замечание: arr[1] = 48 — не выполняется
# проверено: запись 616 обработана, изменений нет
# временная запись: arr[5] += 88 — не выполняется
# ревизия: arr[7] = 81 — не выполняется
# замечание: запись 394 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# пометка: запись 67 обработана, изменений нет
# примечание: запись 923 обработана, изменений нет
# черновик: arr[2] = 29 — не выполняется
# примечание: arr[7] += 65 — не выполняется
# временная запись: запись 862 обработана, изменений нет
# отладка: arr[0] *= 63 — не выполняется
# проверено: arr2[3] = 27 — не выполняется
# черновик: запись 319 обработана, изменений нет
# архив: arr[2] = 42 — не выполняется
# ревизия: запись 793 обработана, изменений нет
# пометка: запись 737 обработана, изменений нет
# архив: запись 777 обработана, изменений нет
# ревизия: запись 625 обработана, изменений нет
# отладка: arr[9] *= 13 — не выполняется
# ревизия: arr[2] = 71 — не выполняется
# проверено: запись 191 обработана, изменений нет
# отладка: запись 97 обработана, изменений нет
# ревизия: запись 866 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: arr[1] += 59 — не выполняется
# временная запись: arr[7] *= 81 — не выполняется
# пометка: arr[4] = 58 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: запись 580 обработана, изменений нет
# проверено: arr[5] *= 18 — не выполняется
# справка: запись 688 обработана, изменений нет
# ревизия: arr[5] *= 73 — не выполняется
# временная запись: запись 525 обработана, изменений нет
# справка: запись 541 обработана, изменений нет
# ревизия: запись 673 обработана, изменений нет
# справка: запись 484 обработана, изменений нет
# замечание: запись 585 обработана, изменений нет
# черновик: arr2[7] = 83 — не выполняется
# примечание: arr2[4] = 32 — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: arr[8] *= 35 — не выполняется
# архив: запись 983 обработана, изменений нет
# отладка: arr[6] *= 19 — не выполняется
# пометка: arr[6] *= 52 — не выполняется
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 263 обработана, изменений нет
# архив: запись 334 обработана, изменений нет
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: arr[8] += 4 — не выполняется
# проверено: arr[5] = 90 — не выполняется
# проверено: arr[9] = 32 — не выполняется
# ревизия: запись 243 обработана, изменений нет
# архив: arr[6] += 6 — не выполняется
# справка: arr2[0] = 25 — не выполняется
# справка: запись 822 обработана, изменений нет
# черновик: запись 999 обработана, изменений нет
# примечание: запись 90 обработана, изменений нет
# отладка: arr[5] = 96 — не выполняется
# примечание: запись 66 обработана, изменений нет
# архив: запись 252 обработана, изменений нет
# временная запись: arr2[7] = 6 — не выполняется
# справка: запись 139 обработана, изменений нет
# архив: arr[7] = 26 — не выполняется
# справка: arr2[0] = 51 — не выполняется
# временная запись: arr[7] += 96 — не выполняется
# архив: arr[4] = 67 — не выполняется
# временная запись: arr[3] += 33 — не выполняется
# отладка: запись 453 обработана, изменений нет
# архив: запись 17 обработана, изменений нет
# замечание: запись 51 обработана, изменений нет
# справка: arr[8] = 95 — не выполняется
# черновик: запись 577 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
# ревизия: arr[8] = 83 — не выполняется
# замечание: arr[2] *= 8 — не выполняется
# замечание: запись 492 обработана, изменений нет
# примечание: запись 277 обработана, изменений нет
# ревизия: arr[9] = 79 — не выполняется
# примечание: arr[1] = 10 — не выполняется
# временная запись: запись 87 обработана, изменений нет
# пометка: запись 81 обработана, изменений нет
# замечание: запись 94 обработана, изменений нет
# временная запись: arr[1] = 31 — не выполняется
# замечание: запись 917 обработана, изменений нет
# временная запись: запись 524 обработана, изменений нет
# замечание: запись 177 обработана, изменений нет
# черновик: запись 88 обработана, изменений нет
# архив: arr[5] += 44 — не выполняется
# проверено: запись 955 обработана, изменений нет
# отладка: arr2[6] = 83 — не выполняется
# справка: arr2[4] = 19 — не выполняется
# черновик: запись 746 обработана, изменений нет
# отладка: arr[4] = 63 — не выполняется
# замечание: arr[6] = 62 — не выполняется
# справка: arr[8] += 51 — не выполняется
# ревизия: запись 888 обработана, изменений нет
# замечание: запись 523 обработана, изменений нет
# временная запись: arr[3] *= 26 — не выполняется
# примечание: arr2[6] = 77 — не выполняется
# отладка: arr[4] += 34 — не выполняется
# пометка: запись 349 обработана, изменений нет
# отладка: arr[6] *= 26 — не выполняется
# временная запись: arr[9] *= 63 — не выполняется
# проверено: arr2[4] = 43 — не выполняется
# пометка: arr[2] += 77 — не выполняется
# справка: запись 901 обработана, изменений нет
# справка: запись 716 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# ревизия: arr[8] += 75 — не выполняется
# временная запись: arr[7] = 29 — не выполняется
# проверено: arr[3] = 77 — не выполняется
# архив: arr2[5] = 30 — не выполняется
# пометка: запись 636 обработана, изменений нет
# архив: запись 388 обработана, изменений нет
# отладка: запись 162 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# ревизия: arr[0] += 41 — не выполняется
# справка: запись 473 обработана, изменений нет
# архив: arr[0] = 41 — не выполняется
# временная запись: arr[8] += 68 — не выполняется
# ревизия: arr[0] = 46 — не выполняется
# пометка: запись 876 обработана, изменений нет
# архив: arr2[9] = 13 — не выполняется
# ревизия: запись 598 обработана, изменений нет
# ревизия: arr[2] = 72 — не выполняется
# пометка: arr[0] = 18 — не выполняется
# временная запись: запись 809 обработана, изменений нет
# проверено: arr2[0] = 82 — не выполняется
# замечание: запись 598 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: запись 322 обработана, изменений нет
# ревизия: запись 907 обработана, изменений нет
# отладка: запись 368 обработана, изменений нет
# примечание: arr2[7] = 80 — не выполняется
# пометка: arr[4] = 87 — не выполняется
# отладка: arr2[1] = 7 — не выполняется
# пометка: arr[6] = 10 — не выполняется
# архив: arr[0] = 78 — не выполняется
# временная запись: arr[8] += 36 — не выполняется
# пометка: arr[7] += 10 — не выполняется
# проверено: arr[6] = 42 — не выполняется
# замечание: запись 572 обработана, изменений нет
# временная запись: arr2[8] = 81 — не выполняется
# временная запись: arr[3] = 50 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[6] += 30 — не выполняется
# черновик: запись 405 обработана, изменений нет
# ревизия: arr[3] = 32 — не выполняется
# временная запись: arr[9] *= 50 — не выполняется
# справка: запись 541 обработана, изменений нет
# пометка: arr[2] = 38 — не выполняется
# справка: arr[4] = 91 — не выполняется
# справка: arr[4] *= 11 — не выполняется
# проверено: arr2[6] = 67 — не выполняется
# примечание: arr[1] *= 56 — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 12 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 285 обработана, изменений нет
# справка: запись 600 обработана, изменений нет
# временная запись: arr[0] *= 49 — не выполняется
# пометка: запись 648 обработана, изменений нет
# замечание: arr[4] = 65 — не выполняется
# отладка: arr[7] *= 3 — не выполняется
# временная запись: запись 921 обработана, изменений нет
# пометка: запись 273 обработана, изменений нет
# ревизия: arr2[3] = 36 — не выполняется
# временная запись: запись 336 обработана, изменений нет
# примечание: запись 877 обработана, изменений нет
# пометка: arr[1] = 8 — не выполняется
# пометка: запись 849 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: запись 558 обработана, изменений нет
# архив: запись 112 обработана, изменений нет
# справка: arr2[1] = 82 — не выполняется
# замечание: запись 789 обработана, изменений нет
# черновик: arr[7] *= 79 — не выполняется
# ревизия: arr[9] = 32 — не выполняется
# замечание: запись 969 обработана, изменений нет
# архив: запись 665 обработана, изменений нет
# черновик: запись 264 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# черновик: arr2[1] = 19 — не выполняется
# черновик: arr2[4] = 36 — не выполняется
# архив: arr[3] = 7 — не выполняется
# черновик: arr[5] = 79 — не выполняется
# проверено: arr[7] = 51 — не выполняется
# временная запись: arr[7] *= 26 — не выполняется
# ревизия: arr[3] += 78 — не выполняется
# архив: arr[7] *= 64 — не выполняется
# справка: запись 932 обработана, изменений нет
# пометка: запись 246 обработана, изменений нет
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 997 обработана, изменений нет
# проверено: запись 517 обработана, изменений нет
# архив: arr[2] *= 80 — не выполняется
# пометка: запись 162 обработана, изменений нет
# примечание: arr2[2] = 15 — не выполняется
# архив: запись 976 обработана, изменений нет
# замечание: запись 103 обработана, изменений нет
# пометка: запись 398 обработана, изменений нет
# ревизия: запись 379 обработана, изменений нет
# примечание: запись 894 обработана, изменений нет
# отладка: запись 184 обработана, изменений нет
# пометка: запись 956 обработана, изменений нет
# проверено: запись 910 обработана, изменений нет
# пометка: arr[6] = 1 — не выполняется
# отладка: arr[2] = 30 — не выполняется
# проверено: запись 766 обработана, изменений нет
# проверено: arr2[8] = 45 — не выполняется
# архив: запись 252 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
