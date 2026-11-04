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
arr2[0] = 54
arr[6] *= 35
arr[1] += 40
arr[9] = 48
arr[5] = 17
arr[3] = 11
arr[1] += 51
arr2[6] = 44
"""

TRAP_0 = "arr[2] = 957"
TRAP_1 = "arr[7] = 640"
TRAP_2 = "arr[6] = 290"
TRAP_3 = "arr[5] = 544"
TRAP_4 = "arr[3] = 424"
TRAP_5 = "arr[0] = 897"
TRAP_6 = "arr[8] = 290"
TRAP_7 = "arr[8] = 941"
TRAP_8 = "arr[5] = 604"
TRAP_9 = "arr[1] = 664"
TRAP_10 = "arr[4] = 180"
TRAP_11 = "arr[0] = 151"
TRAP_12 = "arr[5] = 527"
TRAP_13 = "arr[9] = 829"
TRAP_14 = "arr[8] = 646"
TRAP_15 = "arr[1] = 770"
TRAP_16 = "arr[0] = 508"
TRAP_17 = "arr[1] = 924"
TRAP_18 = "arr[4] = 345"
TRAP_19 = "arr[2] = 664"
TRAP_20 = "arr[5] = 415"
TRAP_21 = "arr[1] = 449"
TRAP_22 = "arr[5] = 123"
TRAP_23 = "arr[0] = 714"
TRAP_24 = "arr[3] = 107"
TRAP_25 = "arr[4] = 181"
TRAP_26 = "arr[2] = 742"
TRAP_27 = "arr[6] = 369"
TRAP_28 = "arr[9] = 290"
TRAP_29 = "arr[0] = 940"
TRAP_30 = "arr[2] = 420"
TRAP_31 = "arr[3] = 479"
TRAP_32 = "arr[8] = 385"
TRAP_33 = "arr[1] = 488"
TRAP_34 = "arr[4] = 103"
TRAP_35 = "arr[1] = 552"
TRAP_36 = "arr[1] = 649"
TRAP_37 = "arr[9] = 710"
TRAP_38 = "arr[2] = 553"
TRAP_39 = "arr[0] = 352"
TRAP_40 = "arr[5] = 330"
TRAP_41 = "arr[8] = 700"
TRAP_42 = "arr[6] = 606"
TRAP_43 = "arr[5] = 104"
TRAP_44 = "arr[1] = 158"
TRAP_45 = "arr[2] = 475"
TRAP_46 = "arr[7] = 603"
TRAP_47 = "arr[7] = 701"
TRAP_48 = "arr[7] = 422"
TRAP_49 = "arr[7] = 115"
TRAP_50 = "arr[3] = 220"
TRAP_51 = "arr[1] = 316"
TRAP_52 = "arr[0] = 921"
TRAP_53 = "arr[8] = 669"
TRAP_54 = "arr[9] = 633"
TRAP_55 = "arr[1] = 324"
TRAP_56 = "arr[9] = 884"
TRAP_57 = "arr[1] = 683"
TRAP_58 = "arr[7] = 679"
TRAP_59 = "arr[8] = 173"
TRAP_60 = "arr[0] = 339"
TRAP_61 = "arr[1] = 682"
TRAP_62 = "arr[3] = 603"
TRAP_63 = "arr[6] = 691"
TRAP_64 = "arr[3] = 377"
TRAP_65 = "arr[6] = 709"
TRAP_66 = "arr[3] = 265"
TRAP_67 = "arr[4] = 346"
TRAP_68 = "arr[1] = 745"
TRAP_69 = "arr[0] = 936"
TRAP_70 = "arr[8] = 975"
TRAP_71 = "arr[0] = 363"
TRAP_72 = "arr[9] = 596"
TRAP_73 = "arr[0] = 730"
TRAP_74 = "arr[1] = 853"
TRAP_75 = "arr[3] = 864"
TRAP_76 = "arr[1] = 857"
TRAP_77 = "arr[5] = 598"
TRAP_78 = "arr[7] = 340"
TRAP_79 = "arr[6] = 215"
TRAP_80 = "arr[8] = 896"
TRAP_81 = "arr[4] = 108"
TRAP_82 = "arr[1] = 459"
TRAP_83 = "arr[3] = 621"
TRAP_84 = "arr[2] = 728"
TRAP_85 = "arr[6] = 285"
TRAP_86 = "arr[9] = 630"
TRAP_87 = "arr[6] = 166"
TRAP_88 = "arr[7] = 645"
TRAP_89 = "arr[6] = 304"
TRAP_90 = "arr[3] = 566"
TRAP_91 = "arr[4] = 577"
TRAP_92 = "arr[5] = 954"
TRAP_93 = "arr[6] = 373"
TRAP_94 = "arr[8] = 966"
TRAP_95 = "arr[3] = 368"
TRAP_96 = "arr[4] = 325"
TRAP_97 = "arr[1] = 297"
TRAP_98 = "arr[6] = 536"
TRAP_99 = "arr[1] = 796"
TRAP_100 = "arr[2] = 615"
TRAP_101 = "arr[8] = 737"
TRAP_102 = "arr[1] = 742"
TRAP_103 = "arr[2] = 184"
TRAP_104 = "arr[8] = 730"
TRAP_105 = "arr[0] = 634"
TRAP_106 = "arr[4] = 726"
TRAP_107 = "arr[6] = 236"
TRAP_108 = "arr[1] = 191"
TRAP_109 = "arr[8] = 337"
TRAP_110 = "arr[2] = 949"
TRAP_111 = "arr[0] = 294"
TRAP_112 = "arr[1] = 218"
TRAP_113 = "arr[6] = 273"
TRAP_114 = "arr[7] = 990"
TRAP_115 = "arr[5] = 929"
TRAP_116 = "arr[7] = 702"
TRAP_117 = "arr[3] = 788"
TRAP_118 = "arr[6] = 472"
TRAP_119 = "arr[2] = 615"
TRAP_120 = "arr[9] = 333"
TRAP_121 = "arr[3] = 472"
TRAP_122 = "arr[0] = 577"
TRAP_123 = "arr[7] = 103"
TRAP_124 = "arr[7] = 610"
TRAP_125 = "arr[7] = 593"
TRAP_126 = "arr[1] = 145"
TRAP_127 = "arr[2] = 678"
TRAP_128 = "arr[8] = 616"
TRAP_129 = "arr[8] = 243"
TRAP_130 = "arr[8] = 451"
TRAP_131 = "arr[1] = 482"
TRAP_132 = "arr[7] = 496"
TRAP_133 = "arr[2] = 221"
TRAP_134 = "arr[8] = 387"
TRAP_135 = "arr[7] = 440"
TRAP_136 = "arr[1] = 451"
TRAP_137 = "arr[2] = 507"
TRAP_138 = "arr[6] = 597"
TRAP_139 = "arr[8] = 974"
TRAP_140 = "arr[9] = 947"
TRAP_141 = "arr[5] = 346"
TRAP_142 = "arr[4] = 793"
TRAP_143 = "arr[3] = 612"
TRAP_144 = "arr[5] = 646"
TRAP_145 = "arr[6] = 920"
TRAP_146 = "arr[0] = 296"
TRAP_147 = "arr[8] = 536"
TRAP_148 = "arr[3] = 602"
TRAP_149 = "arr[9] = 430"

arr = [3, 10, 1, 5, 7, 29, 29, 8, 7, 8]

tmp_0 = arr[1] + 10
tmp_1 = arr[7] + 15
code_2 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_3 = arr[7] + 7
code_4 = re.sub(r'[0-9]', '#', str(arr[2]))
code_5 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_6 = arr[1]
tmp_7 = arr[3] + 49
code_8 = re.sub(r'[0-9]', '#', str(arr[2]))
code_9 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_10 = arr[1] + 35
note_11 = str(arr[5]) + str(arr[9])
tmp_12 = arr[4] + 25
note_13 = str(arr[9]) + str(arr[7])
tmp_14 = arr[5] + 41
code_15 = re.sub(r'[0-9]', '#', str(arr[1]))
note_16 = str(arr[4]) + str(arr[3])
tmp_17 = arr[9] + 49
copy_18 = arr[8]
tmp_19 = arr[4] + 35
code_20 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_21 = arr[9]
label_22 = "запись 22 не применялась"
code_23 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_24 = arr[3] + 43
copy_25 = arr[3]
copy_26 = arr[2]
note_27 = str(arr[4]) + str(arr[8])
tmp_28 = arr[9] + 10
tmp_29 = arr[5] + 46
label_30 = "запись 30 не применялась"
label_31 = "запись 31 не применялась"
note_32 = str(arr[8]) + str(arr[8])
copy_33 = arr[9]
tmp_34 = arr[9] + 35
note_35 = str(arr[4]) + str(arr[7])
tmp_36 = arr[9] + 50
tmp_37 = arr[1] + 2
code_38 = re.sub(r'[0-9]', '#', str(arr[7]))
note_39 = str(arr[5]) + str(arr[5])
copy_40 = arr[7]
code_41 = re.sub(r'[0-9]', '#', str(arr[6]))
note_42 = str(arr[1]) + str(arr[8])
tmp_43 = arr[8] + 23
tmp_44 = arr[8] + 22
code_45 = re.sub(r'[0-9]', '#', str(arr[2]))
label_46 = "запись 46 не применялась"
tmp_47 = arr[1] + 42
note_48 = str(arr[9]) + str(arr[1])
label_49 = "запись 49 не применялась"
copy_50 = arr[0]
code_51 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_52 = arr[8] + 42
note_53 = str(arr[3]) + str(arr[6])
note_54 = str(arr[2]) + str(arr[8])
code_55 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_56 = arr[5]
copy_57 = arr[5]
tmp_58 = arr[9] + 24
tmp_59 = arr[9] + 31
tmp_60 = arr[1] + 46
code_61 = re.sub(r'[0-9]', '#', str(arr[3]))
code_62 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_63 = arr[4] + 1
code_64 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_65 = arr[1]
copy_66 = arr[6]
copy_67 = arr[5]
note_68 = str(arr[1]) + str(arr[4])
tmp_69 = arr[0] + 45
note_70 = str(arr[8]) + str(arr[2])
note_71 = str(arr[6]) + str(arr[1])
tmp_72 = arr[8] + 6
note_73 = str(arr[0]) + str(arr[0])
code_74 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_75 = arr[0] + 20
note_76 = str(arr[5]) + str(arr[6])
tmp_77 = arr[1] + 7
note_78 = str(arr[7]) + str(arr[3])
tmp_79 = arr[5] + 40
tmp_80 = arr[3] + 6
note_81 = str(arr[5]) + str(arr[9])
code_82 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_83 = arr[6]
copy_84 = arr[8]
label_85 = "запись 85 не применялась"
tmp_86 = arr[2] + 34
note_87 = str(arr[4]) + str(arr[9])
tmp_88 = arr[9] + 21
tmp_89 = arr[9] + 4
label_90 = "запись 90 не применялась"
note_91 = str(arr[4]) + str(arr[2])
label_92 = "запись 92 не применялась"
tmp_93 = arr[8] + 30
copy_94 = arr[9]
note_95 = str(arr[7]) + str(arr[7])
tmp_96 = arr[1] + 25
note_97 = str(arr[0]) + str(arr[8])
code_98 = re.sub(r'[0-9]', '#', str(arr[5]))
note_99 = str(arr[7]) + str(arr[4])
note_100 = str(arr[2]) + str(arr[7])
copy_101 = arr[1]
copy_102 = arr[4]
note_103 = str(arr[9]) + str(arr[6])
tmp_104 = arr[1] + 10
note_105 = str(arr[5]) + str(arr[1])
code_106 = re.sub(r'[0-9]', '#', str(arr[4]))
label_107 = "запись 107 не применялась"
code_108 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_109 = arr[8]
tmp_110 = arr[3] + 39
copy_111 = arr[4]
code_112 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_113 = arr[1]
copy_114 = arr[0]
tmp_115 = arr[1] + 39
note_116 = str(arr[7]) + str(arr[9])
tmp_117 = arr[3] + 4
code_118 = re.sub(r'[0-9]', '#', str(arr[2]))
code_119 = re.sub(r'[0-9]', '#', str(arr[5]))
label_120 = "запись 120 не применялась"
code_121 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_122 = arr[4] + 6
copy_123 = arr[7]
tmp_124 = arr[0] + 26
label_125 = "запись 125 не применялась"
tmp_126 = arr[8] + 7
tmp_127 = arr[6] + 12
code_128 = re.sub(r'[0-9]', '#', str(arr[8]))
code_129 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_130 = arr[7]
code_131 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_132 = arr[6] + 36
code_133 = re.sub(r'[0-9]', '#', str(arr[2]))
note_134 = str(arr[2]) + str(arr[4])
code_135 = re.sub(r'[0-9]', '#', str(arr[7]))
note_136 = str(arr[1]) + str(arr[5])
copy_137 = arr[4]
note_138 = str(arr[7]) + str(arr[8])
note_139 = str(arr[7]) + str(arr[4])
note_140 = str(arr[0]) + str(arr[9])
code_141 = re.sub(r'[0-9]', '#', str(arr[0]))
note_142 = str(arr[8]) + str(arr[7])
code_143 = re.sub(r'[0-9]', '#', str(arr[9]))
label_144 = "запись 144 не применялась"
note_145 = str(arr[2]) + str(arr[3])
tmp_146 = arr[3] + 43
tmp_147 = arr[3] + 26
copy_148 = arr[6]
code_149 = re.sub(r'[0-9]', '#', str(arr[9]))
note_150 = str(arr[9]) + str(arr[6])
note_151 = str(arr[7]) + str(arr[7])
copy_152 = arr[7]
label_153 = "запись 153 не применялась"
code_154 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_155 = arr[9] + 32
tmp_156 = arr[0] + 11
note_157 = str(arr[8]) + str(arr[3])
tmp_158 = arr[3] + 25
tmp_159 = arr[0] + 16
note_160 = str(arr[3]) + str(arr[6])
tmp_161 = arr[3] + 25
note_162 = str(arr[8]) + str(arr[4])
code_163 = re.sub(r'[0-9]', '#', str(arr[9]))
note_164 = str(arr[8]) + str(arr[5])
tmp_165 = arr[1] + 15
note_166 = str(arr[3]) + str(arr[3])
note_167 = str(arr[1]) + str(arr[2])
label_168 = "запись 168 не применялась"
copy_169 = arr[9]
label_170 = "запись 170 не применялась"
code_171 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_172 = arr[4] + 18
tmp_173 = arr[3] + 36
tmp_174 = arr[5] + 29
tmp_175 = arr[0] + 39
tmp_176 = arr[5] + 27
tmp_177 = arr[7] + 22
note_178 = str(arr[2]) + str(arr[6])
code_179 = re.sub(r'[0-9]', '#', str(arr[8]))
note_180 = str(arr[0]) + str(arr[9])
code_181 = re.sub(r'[0-9]', '#', str(arr[3]))
note_182 = str(arr[4]) + str(arr[5])
copy_183 = arr[9]
label_184 = "запись 184 не применялась"
copy_185 = arr[5]
label_186 = "запись 186 не применялась"
label_187 = "запись 187 не применялась"
copy_188 = arr[2]
code_189 = re.sub(r'[0-9]', '#', str(arr[8]))
code_190 = re.sub(r'[0-9]', '#', str(arr[5]))
label_191 = "запись 191 не применялась"
note_192 = str(arr[2]) + str(arr[6])
note_193 = str(arr[7]) + str(arr[3])
copy_194 = arr[0]
copy_195 = arr[5]
tmp_196 = arr[7] + 29
note_197 = str(arr[6]) + str(arr[5])
note_198 = str(arr[6]) + str(arr[7])
code_199 = re.sub(r'[0-9]', '#', str(arr[9]))
note_200 = str(arr[7]) + str(arr[6])
note_201 = str(arr[3]) + str(arr[3])
tmp_202 = arr[1] + 16
label_203 = "запись 203 не применялась"
copy_204 = arr[0]
note_205 = str(arr[3]) + str(arr[1])
copy_206 = arr[5]
tmp_207 = arr[4] + 23
code_208 = re.sub(r'[0-9]', '#', str(arr[5]))
note_209 = str(arr[6]) + str(arr[7])
tmp_210 = arr[8] + 10
tmp_211 = arr[6] + 33
note_212 = str(arr[6]) + str(arr[9])
code_213 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_214 = arr[7] + 45
copy_215 = arr[0]
tmp_216 = arr[4] + 9
tmp_217 = arr[7] + 12
copy_218 = arr[8]
code_219 = re.sub(r'[0-9]', '#', str(arr[3]))
note_220 = str(arr[9]) + str(arr[4])
code_221 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_222 = arr[9] + 6
tmp_223 = arr[8] + 40
code_224 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_225 = arr[0]
copy_226 = arr[0]
tmp_227 = arr[7] + 3
tmp_228 = arr[1] + 32
note_229 = str(arr[0]) + str(arr[7])
code_230 = re.sub(r'[0-9]', '#', str(arr[1]))
note_231 = str(arr[4]) + str(arr[6])
code_232 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_233 = arr[1] + 6
copy_234 = arr[9]
note_235 = str(arr[1]) + str(arr[3])
code_236 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_237 = arr[1] + 42
tmp_238 = arr[7] + 49
tmp_239 = arr[1] + 6
tmp_240 = arr[2] + 5
note_241 = str(arr[7]) + str(arr[3])
tmp_242 = arr[7] + 50
tmp_243 = arr[2] + 12
tmp_244 = arr[0] + 17
label_245 = "запись 245 не применялась"
note_246 = str(arr[8]) + str(arr[3])
label_247 = "запись 247 не применялась"
note_248 = str(arr[2]) + str(arr[4])
note_249 = str(arr[9]) + str(arr[2])
label_250 = "запись 250 не применялась"
tmp_251 = arr[2] + 20
copy_252 = arr[0]
note_253 = str(arr[5]) + str(arr[2])
tmp_254 = arr[1] + 35
code_255 = re.sub(r'[0-9]', '#', str(arr[5]))
note_256 = str(arr[7]) + str(arr[2])
tmp_257 = arr[0] + 32
note_258 = str(arr[6]) + str(arr[3])
tmp_259 = arr[2] + 34
copy_260 = arr[9]
tmp_261 = arr[4] + 1
label_262 = "запись 262 не применялась"
code_263 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_264 = arr[0] + 11
tmp_265 = arr[4] + 14
code_266 = re.sub(r'[0-9]', '#', str(arr[8]))
note_267 = str(arr[5]) + str(arr[1])
tmp_268 = arr[4] + 7
note_269 = str(arr[0]) + str(arr[4])
code_270 = re.sub(r'[0-9]', '#', str(arr[1]))
note_271 = str(arr[5]) + str(arr[2])
label_272 = "запись 272 не применялась"
label_273 = "запись 273 не применялась"
note_274 = str(arr[7]) + str(arr[6])
tmp_275 = arr[2] + 19
tmp_276 = arr[4] + 32
tmp_277 = arr[4] + 5
note_278 = str(arr[0]) + str(arr[2])
label_279 = "запись 279 не применялась"
tmp_280 = arr[5] + 11
code_281 = re.sub(r'[0-9]', '#', str(arr[4]))
code_282 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_283 = arr[5] + 25
note_284 = str(arr[8]) + str(arr[3])
note_285 = str(arr[3]) + str(arr[3])
tmp_286 = arr[9] + 40
copy_287 = arr[7]
tmp_288 = arr[4] + 40
code_289 = re.sub(r'[0-9]', '#', str(arr[9]))
note_290 = str(arr[7]) + str(arr[7])
copy_291 = arr[5]
label_292 = "запись 292 не применялась"
tmp_293 = arr[8] + 29
note_294 = str(arr[0]) + str(arr[2])
label_295 = "запись 295 не применялась"
note_296 = str(arr[1]) + str(arr[8])
tmp_297 = arr[8] + 4
tmp_298 = arr[1] + 18
note_299 = str(arr[7]) + str(arr[9])
note_300 = str(arr[7]) + str(arr[2])
code_301 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_302 = arr[2] + 47
label_303 = "запись 303 не применялась"
label_304 = "запись 304 не применялась"
tmp_305 = arr[4] + 42
tmp_306 = arr[1] + 2
note_307 = str(arr[0]) + str(arr[3])
label_308 = "запись 308 не применялась"
code_309 = re.sub(r'[0-9]', '#', str(arr[9]))
label_310 = "запись 310 не применялась"
note_311 = str(arr[0]) + str(arr[3])
tmp_312 = arr[0] + 39
note_313 = str(arr[4]) + str(arr[0])
copy_314 = arr[9]
note_315 = str(arr[4]) + str(arr[4])
tmp_316 = arr[7] + 17
tmp_317 = arr[7] + 31
note_318 = str(arr[8]) + str(arr[9])
tmp_319 = arr[3] + 29
tmp_320 = arr[9] + 24
note_321 = str(arr[3]) + str(arr[0])
copy_322 = arr[3]
note_323 = str(arr[3]) + str(arr[2])
tmp_324 = arr[0] + 28
tmp_325 = arr[8] + 20
copy_326 = arr[6]
tmp_327 = arr[7] + 1
code_328 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_329 = arr[2] + 28
copy_330 = arr[8]
copy_331 = arr[4]
code_332 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_333 = arr[1] + 20
tmp_334 = arr[9] + 40
tmp_335 = arr[3] + 33
code_336 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_337 = arr[8] + 26
tmp_338 = arr[2] + 5
note_339 = str(arr[7]) + str(arr[0])
note_340 = str(arr[9]) + str(arr[2])
note_341 = str(arr[7]) + str(arr[3])
tmp_342 = arr[5] + 49
copy_343 = arr[0]
code_344 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_345 = arr[0] + 29
copy_346 = arr[1]
code_347 = re.sub(r'[0-9]', '#', str(arr[9]))
note_348 = str(arr[4]) + str(arr[4])
code_349 = re.sub(r'[0-9]', '#', str(arr[1]))
note_350 = str(arr[4]) + str(arr[3])
tmp_351 = arr[3] + 47
tmp_352 = arr[6] + 39
note_353 = str(arr[4]) + str(arr[8])
code_354 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_355 = arr[0] + 40
label_356 = "запись 356 не применялась"
note_357 = str(arr[7]) + str(arr[8])
note_358 = str(arr[8]) + str(arr[3])
copy_359 = arr[7]
tmp_360 = arr[0] + 27
tmp_361 = arr[1] + 24
copy_362 = arr[2]
tmp_363 = arr[0] + 48
tmp_364 = arr[5] + 39
code_365 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_366 = arr[4] + 43
note_367 = str(arr[2]) + str(arr[9])
note_368 = str(arr[1]) + str(arr[3])
note_369 = str(arr[9]) + str(arr[0])
code_370 = re.sub(r'[0-9]', '#', str(arr[3]))
label_371 = "запись 371 не применялась"
code_372 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_373 = arr[5] + 47
note_374 = str(arr[4]) + str(arr[0])
note_375 = str(arr[3]) + str(arr[9])
label_376 = "запись 376 не применялась"
tmp_377 = arr[4] + 16
tmp_378 = arr[3] + 12
note_379 = str(arr[4]) + str(arr[7])
code_380 = re.sub(r'[0-9]', '#', str(arr[6]))
label_381 = "запись 381 не применялась"
tmp_382 = arr[9] + 5
tmp_383 = arr[1] + 27
note_384 = str(arr[5]) + str(arr[0])
code_385 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_386 = arr[9] + 46
code_387 = re.sub(r'[0-9]', '#', str(arr[3]))
note_388 = str(arr[3]) + str(arr[9])
tmp_389 = arr[2] + 5
note_390 = str(arr[5]) + str(arr[8])
tmp_391 = arr[4] + 19
label_392 = "запись 392 не применялась"
tmp_393 = arr[9] + 49
copy_394 = arr[0]
label_395 = "запись 395 не применялась"
label_396 = "запись 396 не применялась"
tmp_397 = arr[2] + 32
note_398 = str(arr[7]) + str(arr[0])
tmp_399 = arr[6] + 11
tmp_400 = arr[0] + 6
code_401 = re.sub(r'[0-9]', '#', str(arr[2]))
note_402 = str(arr[0]) + str(arr[1])
note_403 = str(arr[5]) + str(arr[4])
note_404 = str(arr[5]) + str(arr[8])
tmp_405 = arr[1] + 2
note_406 = str(arr[8]) + str(arr[6])
tmp_407 = arr[4] + 3
code_408 = re.sub(r'[0-9]', '#', str(arr[8]))
note_409 = str(arr[8]) + str(arr[2])
copy_410 = arr[5]
copy_411 = arr[4]
note_412 = str(arr[0]) + str(arr[5])
note_413 = str(arr[4]) + str(arr[9])
note_414 = str(arr[9]) + str(arr[0])
code_415 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_416 = arr[9] + 8
code_417 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_418 = arr[5]
label_419 = "запись 419 не применялась"
note_420 = str(arr[6]) + str(arr[8])
tmp_421 = arr[2] + 35
copy_422 = arr[7]
tmp_423 = arr[7] + 23
code_424 = re.sub(r'[0-9]', '#', str(arr[2]))
label_425 = "запись 425 не применялась"
note_426 = str(arr[6]) + str(arr[5])
code_427 = re.sub(r'[0-9]', '#', str(arr[7]))
code_428 = re.sub(r'[0-9]', '#', str(arr[6]))
code_429 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_430 = arr[9]
tmp_431 = arr[9] + 30
code_432 = re.sub(r'[0-9]', '#', str(arr[6]))
code_433 = re.sub(r'[0-9]', '#', str(arr[6]))
code_434 = re.sub(r'[0-9]', '#', str(arr[1]))
note_435 = str(arr[9]) + str(arr[2])
note_436 = str(arr[1]) + str(arr[9])
code_437 = re.sub(r'[0-9]', '#', str(arr[2]))
note_438 = str(arr[1]) + str(arr[5])
code_439 = re.sub(r'[0-9]', '#', str(arr[9]))
note_440 = str(arr[2]) + str(arr[5])
code_441 = re.sub(r'[0-9]', '#', str(arr[6]))
code_442 = re.sub(r'[0-9]', '#', str(arr[1]))
code_443 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_444 = arr[4] + 12
tmp_445 = arr[2] + 5
tmp_446 = arr[1] + 13
tmp_447 = arr[1] + 30
tmp_448 = arr[5] + 3
tmp_449 = arr[7] + 11
note_450 = str(arr[2]) + str(arr[4])
note_451 = str(arr[5]) + str(arr[2])
code_452 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_453 = arr[7]
code_454 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_455 = arr[3]
tmp_456 = arr[6] + 44
tmp_457 = arr[8] + 12
code_458 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_459 = arr[2] + 43
code_460 = re.sub(r'[0-9]', '#', str(arr[7]))
note_461 = str(arr[0]) + str(arr[7])
copy_462 = arr[3]
copy_463 = arr[3]
note_464 = str(arr[6]) + str(arr[4])
label_465 = "запись 465 не применялась"
note_466 = str(arr[5]) + str(arr[1])
tmp_467 = arr[4] + 47
tmp_468 = arr[9] + 36
tmp_469 = arr[5] + 22
code_470 = re.sub(r'[0-9]', '#', str(arr[3]))
code_471 = re.sub(r'[0-9]', '#', str(arr[0]))
note_472 = str(arr[1]) + str(arr[0])
copy_473 = arr[3]
note_474 = str(arr[4]) + str(arr[7])
tmp_475 = arr[5] + 33
note_476 = str(arr[4]) + str(arr[3])
code_477 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_478 = arr[5]
tmp_479 = arr[1] + 21
note_480 = str(arr[6]) + str(arr[5])
copy_481 = arr[4]
note_482 = str(arr[7]) + str(arr[7])
tmp_483 = arr[3] + 47
note_484 = str(arr[8]) + str(arr[4])
tmp_485 = arr[4] + 48
code_486 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_487 = arr[6]
tmp_488 = arr[8] + 2
note_489 = str(arr[3]) + str(arr[8])
note_490 = str(arr[3]) + str(arr[3])
tmp_491 = arr[1] + 39
note_492 = str(arr[5]) + str(arr[4])
tmp_493 = arr[4] + 21
copy_494 = arr[3]
tmp_495 = arr[8] + 21
copy_496 = arr[5]
note_497 = str(arr[9]) + str(arr[3])
code_498 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_499 = arr[1]
note_500 = str(arr[2]) + str(arr[1])
tmp_501 = arr[0] + 21
note_502 = str(arr[7]) + str(arr[7])
note_503 = str(arr[1]) + str(arr[6])
tmp_504 = arr[5] + 27
note_505 = str(arr[4]) + str(arr[0])
code_506 = re.sub(r'[0-9]', '#', str(arr[1]))
code_507 = re.sub(r'[0-9]', '#', str(arr[8]))
note_508 = str(arr[0]) + str(arr[6])
note_509 = str(arr[6]) + str(arr[7])
copy_510 = arr[3]
copy_511 = arr[2]
label_512 = "запись 512 не применялась"
copy_513 = arr[1]
tmp_514 = arr[2] + 3
note_515 = str(arr[1]) + str(arr[9])
label_516 = "запись 516 не применялась"
tmp_517 = arr[4] + 11
copy_518 = arr[7]
code_519 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_520 = arr[6]
note_521 = str(arr[7]) + str(arr[6])
copy_522 = arr[9]
tmp_523 = arr[9] + 17
tmp_524 = arr[1] + 4
code_525 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_526 = arr[9]
copy_527 = arr[6]
tmp_528 = arr[4] + 21
tmp_529 = arr[3] + 46
copy_530 = arr[5]
note_531 = str(arr[1]) + str(arr[7])
note_532 = str(arr[4]) + str(arr[3])
tmp_533 = arr[4] + 32
tmp_534 = arr[3] + 11
copy_535 = arr[0]
code_536 = re.sub(r'[0-9]', '#', str(arr[4]))
note_537 = str(arr[5]) + str(arr[2])
note_538 = str(arr[6]) + str(arr[3])
code_539 = re.sub(r'[0-9]', '#', str(arr[1]))
note_540 = str(arr[5]) + str(arr[9])
label_541 = "запись 541 не применялась"
note_542 = str(arr[8]) + str(arr[3])
note_543 = str(arr[7]) + str(arr[2])
tmp_544 = arr[4] + 8
label_545 = "запись 545 не применялась"
note_546 = str(arr[8]) + str(arr[0])
note_547 = str(arr[2]) + str(arr[2])
note_548 = str(arr[8]) + str(arr[1])
tmp_549 = arr[8] + 6
note_550 = str(arr[2]) + str(arr[7])
code_551 = re.sub(r'[0-9]', '#', str(arr[1]))
note_552 = str(arr[7]) + str(arr[6])
label_553 = "запись 553 не применялась"
tmp_554 = arr[7] + 33
code_555 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_556 = arr[8] + 26
label_557 = "запись 557 не применялась"
tmp_558 = arr[7] + 5
tmp_559 = arr[1] + 22
code_560 = re.sub(r'[0-9]', '#', str(arr[3]))
note_561 = str(arr[1]) + str(arr[9])
copy_562 = arr[8]
code_563 = re.sub(r'[0-9]', '#', str(arr[3]))
note_564 = str(arr[6]) + str(arr[5])
note_565 = str(arr[1]) + str(arr[3])
copy_566 = arr[3]
label_567 = "запись 567 не применялась"
note_568 = str(arr[4]) + str(arr[6])
tmp_569 = arr[3] + 50
code_570 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_571 = arr[2]
code_572 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_573 = arr[5] + 8
note_574 = str(arr[4]) + str(arr[2])
tmp_575 = arr[8] + 32
tmp_576 = arr[2] + 18
code_577 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_578 = arr[2]
note_579 = str(arr[1]) + str(arr[7])
copy_580 = arr[2]
copy_581 = arr[8]
label_582 = "запись 582 не применялась"
note_583 = str(arr[6]) + str(arr[1])
copy_584 = arr[7]
tmp_585 = arr[9] + 13
label_586 = "запись 586 не применялась"
note_587 = str(arr[9]) + str(arr[0])
tmp_588 = arr[3] + 40
copy_589 = arr[3]
tmp_590 = arr[9] + 44
note_591 = str(arr[5]) + str(arr[4])
label_592 = "запись 592 не применялась"
tmp_593 = arr[2] + 12
tmp_594 = arr[6] + 9
copy_595 = arr[7]
note_596 = str(arr[8]) + str(arr[9])
label_597 = "запись 597 не применялась"
code_598 = re.sub(r'[0-9]', '#', str(arr[1]))
note_599 = str(arr[5]) + str(arr[9])
code_600 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_601 = arr[0]
copy_602 = arr[4]
code_603 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_604 = arr[0] + 11
tmp_605 = arr[6] + 20
label_606 = "запись 606 не применялась"
note_607 = str(arr[2]) + str(arr[3])
tmp_608 = arr[7] + 24
label_609 = "запись 609 не применялась"
code_610 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_611 = arr[5] + 45
label_612 = "запись 612 не применялась"
note_613 = str(arr[6]) + str(arr[5])
note_614 = str(arr[7]) + str(arr[8])
copy_615 = arr[9]
note_616 = str(arr[0]) + str(arr[2])
note_617 = str(arr[6]) + str(arr[3])
tmp_618 = arr[1] + 10
copy_619 = arr[0]
note_620 = str(arr[3]) + str(arr[1])
tmp_621 = arr[1] + 8
code_622 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_623 = arr[5] + 44
tmp_624 = arr[6] + 23
note_625 = str(arr[5]) + str(arr[0])
copy_626 = arr[8]
copy_627 = arr[7]
label_628 = "запись 628 не применялась"
code_629 = re.sub(r'[0-9]', '#', str(arr[7]))
code_630 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_631 = arr[5] + 27
code_632 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_633 = arr[2]
label_634 = "запись 634 не применялась"
tmp_635 = arr[8] + 48
tmp_636 = arr[4] + 18
tmp_637 = arr[8] + 3
tmp_638 = arr[6] + 48
code_639 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_640 = arr[0]
tmp_641 = arr[1] + 15
copy_642 = arr[9]
note_643 = str(arr[7]) + str(arr[1])
note_644 = str(arr[2]) + str(arr[2])
code_645 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_646 = arr[0] + 26
copy_647 = arr[2]
tmp_648 = arr[3] + 10
tmp_649 = arr[6] + 2
label_650 = "запись 650 не применялась"
note_651 = str(arr[8]) + str(arr[0])
copy_652 = arr[1]
note_653 = str(arr[0]) + str(arr[1])
code_654 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_655 = arr[5]
copy_656 = arr[8]
tmp_657 = arr[0] + 13
tmp_658 = arr[1] + 25
tmp_659 = arr[9] + 29
tmp_660 = arr[5] + 45
copy_661 = arr[4]
code_662 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_663 = arr[2]
tmp_664 = arr[9] + 46
note_665 = str(arr[3]) + str(arr[5])
code_666 = re.sub(r'[0-9]', '#', str(arr[7]))
code_667 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_668 = arr[9]
tmp_669 = arr[1] + 43
note_670 = str(arr[3]) + str(arr[7])
tmp_671 = arr[9] + 32
note_672 = str(arr[5]) + str(arr[8])
tmp_673 = arr[6] + 39
code_674 = re.sub(r'[0-9]', '#', str(arr[0]))
note_675 = str(arr[0]) + str(arr[4])
note_676 = str(arr[9]) + str(arr[5])
copy_677 = arr[8]
copy_678 = arr[2]
label_679 = "запись 679 не применялась"
note_680 = str(arr[3]) + str(arr[6])
code_681 = re.sub(r'[0-9]', '#', str(arr[2]))
code_682 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_683 = arr[8] + 24
code_684 = re.sub(r'[0-9]', '#', str(arr[2]))
label_685 = "запись 685 не применялась"
label_686 = "запись 686 не применялась"
copy_687 = arr[2]
tmp_688 = arr[9] + 24
note_689 = str(arr[8]) + str(arr[6])
code_690 = re.sub(r'[0-9]', '#', str(arr[1]))
code_691 = re.sub(r'[0-9]', '#', str(arr[3]))
label_692 = "запись 692 не применялась"
copy_693 = arr[8]
copy_694 = arr[3]
tmp_695 = arr[0] + 23
note_696 = str(arr[7]) + str(arr[3])
code_697 = re.sub(r'[0-9]', '#', str(arr[8]))
note_698 = str(arr[1]) + str(arr[8])
note_699 = str(arr[1]) + str(arr[4])
note_700 = str(arr[7]) + str(arr[6])
tmp_701 = arr[7] + 13
label_702 = "запись 702 не применялась"
label_703 = "запись 703 не применялась"
tmp_704 = arr[2] + 39
tmp_705 = arr[6] + 10
note_706 = str(arr[6]) + str(arr[6])
tmp_707 = arr[0] + 28
label_708 = "запись 708 не применялась"
code_709 = re.sub(r'[0-9]', '#', str(arr[5]))
note_710 = str(arr[0]) + str(arr[2])
note_711 = str(arr[0]) + str(arr[9])
note_712 = str(arr[4]) + str(arr[4])
tmp_713 = arr[2] + 3
code_714 = re.sub(r'[0-9]', '#', str(arr[5]))
code_715 = re.sub(r'[0-9]', '#', str(arr[4]))
code_716 = re.sub(r'[0-9]', '#', str(arr[9]))
code_717 = re.sub(r'[0-9]', '#', str(arr[5]))
code_718 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_719 = arr[2] + 49
label_720 = "запись 720 не применялась"
copy_721 = arr[7]
note_722 = str(arr[2]) + str(arr[0])
code_723 = re.sub(r'[0-9]', '#', str(arr[6]))
note_724 = str(arr[1]) + str(arr[3])
tmp_725 = arr[9] + 15
tmp_726 = arr[6] + 18
tmp_727 = arr[3] + 35
code_728 = re.sub(r'[0-9]', '#', str(arr[4]))
note_729 = str(arr[7]) + str(arr[4])
copy_730 = arr[3]
label_731 = "запись 731 не применялась"
label_732 = "запись 732 не применялась"
tmp_733 = arr[7] + 37
code_734 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_735 = arr[1]
note_736 = str(arr[7]) + str(arr[4])
code_737 = re.sub(r'[0-9]', '#', str(arr[8]))
label_738 = "запись 738 не применялась"
copy_739 = arr[2]
note_740 = str(arr[0]) + str(arr[5])
tmp_741 = arr[0] + 26
label_742 = "запись 742 не применялась"
copy_743 = arr[1]
note_744 = str(arr[7]) + str(arr[1])
tmp_745 = arr[8] + 4
tmp_746 = arr[9] + 2
note_747 = str(arr[4]) + str(arr[1])
note_748 = str(arr[3]) + str(arr[7])
code_749 = re.sub(r'[0-9]', '#', str(arr[9]))
note_750 = str(arr[0]) + str(arr[7])
tmp_751 = arr[8] + 34
tmp_752 = arr[1] + 45
note_753 = str(arr[9]) + str(arr[0])
note_754 = str(arr[8]) + str(arr[2])
tmp_755 = arr[2] + 18
tmp_756 = arr[3] + 44
tmp_757 = arr[8] + 12
label_758 = "запись 758 не применялась"
note_759 = str(arr[6]) + str(arr[2])
copy_760 = arr[4]
note_761 = str(arr[8]) + str(arr[4])
note_762 = str(arr[3]) + str(arr[2])
copy_763 = arr[9]
tmp_764 = arr[1] + 1
tmp_765 = arr[8] + 1
copy_766 = arr[7]
note_767 = str(arr[7]) + str(arr[4])
copy_768 = arr[9]
copy_769 = arr[3]
label_770 = "запись 770 не применялась"
code_771 = re.sub(r'[0-9]', '#', str(arr[8]))
code_772 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_773 = arr[3] + 16
copy_774 = arr[6]
copy_775 = arr[1]
copy_776 = arr[3]
tmp_777 = arr[6] + 48
tmp_778 = arr[1] + 17
note_779 = str(arr[1]) + str(arr[3])
code_780 = re.sub(r'[0-9]', '#', str(arr[3]))
note_781 = str(arr[0]) + str(arr[6])
note_782 = str(arr[7]) + str(arr[2])
copy_783 = arr[1]
note_784 = str(arr[9]) + str(arr[1])
label_785 = "запись 785 не применялась"
note_786 = str(arr[0]) + str(arr[5])
copy_787 = arr[9]
label_788 = "запись 788 не применялась"
note_789 = str(arr[8]) + str(arr[4])
code_790 = re.sub(r'[0-9]', '#', str(arr[4]))
note_791 = str(arr[0]) + str(arr[6])
code_792 = re.sub(r'[0-9]', '#', str(arr[5]))
note_793 = str(arr[4]) + str(arr[8])
code_794 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_795 = arr[4] + 46
tmp_796 = arr[1] + 10
copy_797 = arr[2]
code_798 = re.sub(r'[0-9]', '#', str(arr[2]))
label_799 = "запись 799 не применялась"

arr2 = arr
# временная запись: arr[7] += 72 — не выполняется
# проверено: arr[3] += 15 — не выполняется
# архив: запись 739 обработана, изменений нет
# архив: arr[3] = 61 — не выполняется
# отладка: arr[4] *= 86 — не выполняется
# проверено: запись 662 обработана, изменений нет
# примечание: запись 12 обработана, изменений нет
# примечание: arr[1] += 38 — не выполняется
# проверено: запись 977 обработана, изменений нет
# отладка: запись 655 обработана, изменений нет
# отладка: arr2[0] = 86 — не выполняется
# пометка: arr[2] += 43 — не выполняется
# ревизия: запись 557 обработана, изменений нет
# справка: arr[1] = 92 — не выполняется
# черновик: arr2[0] = 65 — не выполняется
# отладка: arr[3] += 23 — не выполняется
# отладка: запись 441 обработана, изменений нет
# пометка: arr[6] *= 75 — не выполняется
# черновик: запись 508 обработана, изменений нет
# черновик: запись 392 обработана, изменений нет
# примечание: запись 186 обработана, изменений нет
# проверено: запись 881 обработана, изменений нет
# архив: arr[0] = 26 — не выполняется
# черновик: запись 234 обработана, изменений нет
# архив: arr[5] += 65 — не выполняется
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 662 обработана, изменений нет
# примечание: запись 943 обработана, изменений нет
# проверено: запись 708 обработана, изменений нет
# ревизия: arr[4] += 95 — не выполняется
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[2] += 43 — не выполняется
# примечание: запись 398 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# примечание: запись 797 обработана, изменений нет
# примечание: запись 347 обработана, изменений нет
# справка: arr[7] *= 80 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 834 обработана, изменений нет
# пометка: запись 759 обработана, изменений нет
# примечание: arr2[2] = 67 — не выполняется
# отладка: arr[5] += 10 — не выполняется
# проверено: arr2[9] = 59 — не выполняется
# замечание: запись 181 обработана, изменений нет
# справка: запись 584 обработана, изменений нет
# проверено: запись 537 обработана, изменений нет
# примечание: arr[1] = 89 — не выполняется
# временная запись: запись 145 обработана, изменений нет
# замечание: запись 692 обработана, изменений нет
# черновик: arr[2] = 38 — не выполняется
# отладка: arr[2] *= 92 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: arr[2] = 36 — не выполняется
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: arr[4] *= 63 — не выполняется
# проверено: arr[3] = 90 — не выполняется
# ревизия: arr2[5] = 32 — не выполняется
# проверено: запись 392 обработана, изменений нет
# проверено: запись 512 обработана, изменений нет
# отладка: arr[2] *= 15 — не выполняется
# замечание: запись 257 обработана, изменений нет
# ревизия: запись 121 обработана, изменений нет
# отладка: arr2[1] = 53 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: arr[9] = 26 — не выполняется
# замечание: запись 505 обработана, изменений нет
# проверено: arr[0] *= 27 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 162 обработана, изменений нет
# пометка: arr2[6] = 56 — не выполняется
# отладка: arr[0] += 67 — не выполняется
# примечание: arr[4] *= 75 — не выполняется
# замечание: запись 310 обработана, изменений нет
# примечание: arr[5] *= 96 — не выполняется
# черновик: arr[6] *= 20 — не выполняется
# временная запись: arr[5] += 49 — не выполняется
# справка: запись 219 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# примечание: arr[3] = 62 — не выполняется
# ревизия: arr2[5] = 34 — не выполняется
# черновик: arr[1] += 6 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr[9] *= 45 — не выполняется
# справка: запись 950 обработана, изменений нет
# пометка: запись 546 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: запись 853 обработана, изменений нет
# отладка: arr2[8] = 4 — не выполняется
# замечание: запись 961 обработана, изменений нет
# замечание: arr[4] *= 92 — не выполняется
# справка: arr[0] *= 4 — не выполняется
# черновик: запись 348 обработана, изменений нет
# черновик: arr[6] = 14 — не выполняется
# замечание: запись 836 обработана, изменений нет
# ревизия: arr[8] *= 44 — не выполняется
# временная запись: запись 217 обработана, изменений нет
# ревизия: запись 513 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# ревизия: запись 303 обработана, изменений нет
# временная запись: arr2[3] = 88 — не выполняется
# архив: запись 854 обработана, изменений нет
# примечание: запись 271 обработана, изменений нет
# примечание: запись 747 обработана, изменений нет
# черновик: arr[7] += 81 — не выполняется
# замечание: запись 392 обработана, изменений нет
# пометка: arr[3] = 36 — не выполняется
# архив: arr[4] = 96 — не выполняется
# ревизия: запись 651 обработана, изменений нет
# временная запись: arr[3] = 74 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: запись 461 обработана, изменений нет
# временная запись: запись 868 обработана, изменений нет
# отладка: arr[3] *= 17 — не выполняется
# замечание: запись 542 обработана, изменений нет
# примечание: запись 402 обработана, изменений нет
# временная запись: запись 381 обработана, изменений нет
# справка: запись 607 обработана, изменений нет
# временная запись: arr2[5] = 73 — не выполняется
# архив: arr[0] += 36 — не выполняется
# примечание: arr[3] += 58 — не выполняется
# ревизия: arr[9] += 61 — не выполняется
# временная запись: arr[6] += 68 — не выполняется
# черновик: arr[6] *= 83 — не выполняется
# черновик: запись 787 обработана, изменений нет
# примечание: arr[7] *= 86 — не выполняется
# черновик: запись 478 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# черновик: запись 71 обработана, изменений нет
# пометка: arr[7] = 43 — не выполняется
# ревизия: arr[3] *= 59 — не выполняется
# проверено: запись 535 обработана, изменений нет
# замечание: arr2[7] = 2 — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# отладка: запись 179 обработана, изменений нет
# временная запись: запись 325 обработана, изменений нет
# замечание: arr[3] = 85 — не выполняется
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 509 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 87 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# черновик: запись 137 обработана, изменений нет
# справка: запись 981 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# отладка: запись 739 обработана, изменений нет
# ревизия: arr[7] *= 37 — не выполняется
# временная запись: arr2[7] = 35 — не выполняется
# архив: arr[1] *= 82 — не выполняется
# пометка: запись 413 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# пометка: arr[6] += 70 — не выполняется
# отладка: arr[3] += 60 — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 235 обработана, изменений нет
# временная запись: arr2[8] = 75 — не выполняется
# черновик: arr[7] *= 76 — не выполняется
# примечание: arr2[7] = 79 — не выполняется
# проверено: arr[9] *= 52 — не выполняется
# примечание: запись 596 обработана, изменений нет
# ревизия: запись 606 обработана, изменений нет
# ревизия: arr[3] *= 95 — не выполняется
# проверено: запись 105 обработана, изменений нет
# пометка: arr[6] += 99 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[6] = 84 — не выполняется
# ревизия: arr[2] = 46 — не выполняется
# временная запись: arr[9] = 6 — не выполняется
# черновик: arr2[9] = 86 — не выполняется
# ревизия: запись 2 обработана, изменений нет
# замечание: запись 692 обработана, изменений нет
# ревизия: arr2[0] = 58 — не выполняется
# ревизия: arr[4] = 87 — не выполняется
# примечание: arr[0] *= 24 — не выполняется
# замечание: arr2[4] = 20 — не выполняется
# архив: запись 673 обработана, изменений нет
# справка: запись 804 обработана, изменений нет
# черновик: arr[2] *= 64 — не выполняется
# пометка: запись 852 обработана, изменений нет
# ревизия: arr2[0] = 10 — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 208 обработана, изменений нет
# проверено: запись 330 обработана, изменений нет
# замечание: arr[9] += 76 — не выполняется
# замечание: arr[4] = 82 — не выполняется
# отладка: запись 141 обработана, изменений нет
# ревизия: запись 926 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# ревизия: arr[6] += 6 — не выполняется
# временная запись: запись 428 обработана, изменений нет
# справка: запись 846 обработана, изменений нет
# замечание: arr2[7] = 32 — не выполняется
# замечание: arr[4] += 9 — не выполняется
# замечание: запись 39 обработана, изменений нет
# проверено: arr[6] = 96 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: arr[8] *= 56 — не выполняется
# замечание: запись 321 обработана, изменений нет
# черновик: arr2[8] = 75 — не выполняется
# отладка: запись 715 обработана, изменений нет
# черновик: arr[9] = 23 — не выполняется
# архив: arr[6] = 35 — не выполняется
# примечание: запись 879 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# временная запись: запись 791 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# примечание: arr2[9] = 64 — не выполняется
# черновик: запись 729 обработана, изменений нет
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[6] += 21 — не выполняется
# архив: запись 760 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: запись 179 обработана, изменений нет
# пометка: arr2[9] = 95 — не выполняется
# отладка: запись 66 обработана, изменений нет
# ревизия: arr[3] += 55 — не выполняется
# проверено: запись 704 обработана, изменений нет
# пометка: запись 155 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# временная запись: arr[4] *= 12 — не выполняется
# отладка: arr[6] *= 64 — не выполняется
# временная запись: arr2[4] = 69 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 858 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# проверено: arr[5] *= 49 — не выполняется
# замечание: arr[1] *= 58 — не выполняется
# пометка: arr[9] *= 33 — не выполняется
# проверено: arr[1] += 10 — не выполняется
# пометка: запись 417 обработана, изменений нет
# замечание: arr[1] *= 38 — не выполняется
# примечание: запись 689 обработана, изменений нет
# черновик: запись 220 обработана, изменений нет
# примечание: arr[3] *= 44 — не выполняется
# отладка: arr[9] = 89 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# ревизия: arr[4] = 66 — не выполняется
# пометка: запись 229 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 529 обработана, изменений нет
# справка: arr[7] *= 75 — не выполняется
# справка: запись 377 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# архив: arr[0] *= 18 — не выполняется
# временная запись: запись 113 обработана, изменений нет
# замечание: запись 866 обработана, изменений нет
# архив: arr[3] += 42 — не выполняется
# временная запись: запись 84 обработана, изменений нет
# замечание: запись 872 обработана, изменений нет
# временная запись: arr[7] = 12 — не выполняется
# отладка: запись 696 обработана, изменений нет
# отладка: arr[9] = 50 — не выполняется
# черновик: arr[9] *= 96 — не выполняется
# архив: запись 692 обработана, изменений нет
# пометка: arr[0] *= 4 — не выполняется
# примечание: запись 891 обработана, изменений нет
# черновик: запись 888 обработана, изменений нет
# архив: arr[0] = 39 — не выполняется
# временная запись: запись 599 обработана, изменений нет
# примечание: arr[7] *= 58 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: запись 629 обработана, изменений нет
# ревизия: запись 174 обработана, изменений нет
# справка: arr[3] += 34 — не выполняется
# временная запись: запись 168 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 624 обработана, изменений нет
# архив: запись 859 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 281 обработана, изменений нет
# временная запись: arr2[3] = 12 — не выполняется
# отладка: arr[5] = 26 — не выполняется
# примечание: arr[6] *= 63 — не выполняется
# пометка: arr[5] += 60 — не выполняется
# черновик: arr[5] *= 86 — не выполняется
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 6 обработана, изменений нет
# справка: arr[2] += 8 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# архив: запись 816 обработана, изменений нет
# примечание: arr[6] *= 33 — не выполняется
# черновик: arr[1] += 21 — не выполняется
# проверено: arr[6] += 8 — не выполняется
# замечание: arr[1] += 50 — не выполняется
# пометка: запись 440 обработана, изменений нет
# архив: arr[4] = 92 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: arr[9] += 43 — не выполняется
# примечание: запись 677 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# ревизия: arr[3] += 73 — не выполняется
# архив: запись 108 обработана, изменений нет
# ревизия: запись 266 обработана, изменений нет
# архив: arr[0] += 80 — не выполняется
# замечание: запись 643 обработана, изменений нет
# справка: запись 698 обработана, изменений нет
# архив: arr2[5] = 4 — не выполняется
# примечание: запись 237 обработана, изменений нет
arr2[8] += 1
# архив: запись 519 обработана, изменений нет
# отладка: arr[2] += 95 — не выполняется
# проверено: запись 987 обработана, изменений нет
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 429 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
# проверено: arr[0] *= 87 — не выполняется
# архив: запись 681 обработана, изменений нет
# пометка: arr2[2] = 47 — не выполняется
# архив: arr[7] += 28 — не выполняется
# временная запись: arr[9] += 35 — не выполняется
# проверено: arr[8] += 88 — не выполняется
# замечание: arr[9] *= 76 — не выполняется
# отладка: запись 137 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr2[6] = 23 — не выполняется
# черновик: запись 309 обработана, изменений нет
# замечание: запись 386 обработана, изменений нет
# архив: запись 419 обработана, изменений нет
# архив: запись 764 обработана, изменений нет
# проверено: arr[7] = 27 — не выполняется
# архив: запись 138 обработана, изменений нет
# проверено: arr[3] += 32 — не выполняется
# ревизия: arr[1] += 61 — не выполняется
# архив: запись 377 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# отладка: arr2[7] = 29 — не выполняется
# примечание: запись 965 обработана, изменений нет
# примечание: запись 896 обработана, изменений нет
# архив: запись 507 обработана, изменений нет
# отладка: arr[0] += 87 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: запись 113 обработана, изменений нет
# справка: arr2[5] = 60 — не выполняется
# архив: запись 956 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# замечание: запись 572 обработана, изменений нет
# справка: запись 498 обработана, изменений нет
# черновик: arr[9] = 23 — не выполняется
# отладка: запись 998 обработана, изменений нет
# черновик: запись 202 обработана, изменений нет
# пометка: запись 452 обработана, изменений нет
# замечание: arr2[4] = 64 — не выполняется
# справка: запись 110 обработана, изменений нет
# пометка: arr[1] = 74 — не выполняется
# справка: запись 739 обработана, изменений нет
# примечание: arr[2] = 86 — не выполняется
# временная запись: запись 599 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# замечание: arr2[0] = 95 — не выполняется
# ревизия: запись 695 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr2[5] = 31 — не выполняется
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 445 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# ревизия: arr[6] += 2 — не выполняется
# пометка: запись 648 обработана, изменений нет
# пометка: запись 845 обработана, изменений нет
# справка: arr[8] *= 20 — не выполняется
# ревизия: запись 556 обработана, изменений нет
# справка: arr[7] = 13 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# примечание: arr[1] *= 57 — не выполняется
# отладка: запись 960 обработана, изменений нет
# пометка: запись 861 обработана, изменений нет
# отладка: arr[3] = 80 — не выполняется
# временная запись: запись 262 обработана, изменений нет
# временная запись: arr[4] = 10 — не выполняется
# отладка: запись 696 обработана, изменений нет
# черновик: запись 192 обработана, изменений нет
# проверено: arr[9] *= 7 — не выполняется
# пометка: запись 943 обработана, изменений нет
# замечание: arr[7] *= 54 — не выполняется
# справка: arr[6] += 98 — не выполняется
# замечание: запись 540 обработана, изменений нет
# замечание: arr[1] = 11 — не выполняется
# временная запись: arr2[3] = 85 — не выполняется
# примечание: arr[0] *= 47 — не выполняется
# архив: запись 153 обработана, изменений нет
# архив: arr[5] *= 80 — не выполняется
# отладка: запись 466 обработана, изменений нет
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 410 обработана, изменений нет
# черновик: arr[2] += 68 — не выполняется
# проверено: запись 484 обработана, изменений нет
# отладка: arr2[8] = 54 — не выполняется
# проверено: запись 581 обработана, изменений нет
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# ревизия: arr[7] *= 62 — не выполняется
# отладка: запись 71 обработана, изменений нет
# замечание: запись 205 обработана, изменений нет
# архив: arr[8] = 12 — не выполняется
# черновик: arr[0] *= 84 — не выполняется
# пометка: arr[4] *= 17 — не выполняется
# проверено: запись 61 обработана, изменений нет
# проверено: arr2[0] = 57 — не выполняется
# архив: запись 966 обработана, изменений нет
# замечание: запись 228 обработана, изменений нет
# архив: arr[0] = 46 — не выполняется
# замечание: arr[8] *= 12 — не выполняется
# примечание: arr2[3] = 22 — не выполняется
# временная запись: запись 707 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 340 обработана, изменений нет
# отладка: arr[7] *= 51 — не выполняется
# временная запись: запись 615 обработана, изменений нет
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 358 обработана, изменений нет
# архив: arr[1] *= 2 — не выполняется
# замечание: arr[5] = 47 — не выполняется
# примечание: запись 494 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# черновик: запись 167 обработана, изменений нет
# архив: arr[7] *= 38 — не выполняется
# проверено: запись 251 обработана, изменений нет
# архив: arr[7] = 85 — не выполняется
# примечание: запись 210 обработана, изменений нет
# архив: arr2[5] = 51 — не выполняется
# ревизия: запись 292 обработана, изменений нет
# отладка: запись 256 обработана, изменений нет
# пометка: запись 507 обработана, изменений нет
# замечание: arr2[9] = 56 — не выполняется
# черновик: arr[6] *= 24 — не выполняется
# справка: запись 453 обработана, изменений нет
# замечание: запись 187 обработана, изменений нет
# пометка: запись 429 обработана, изменений нет
# замечание: arr[8] = 79 — не выполняется
# справка: arr2[2] = 32 — не выполняется
# архив: arr[2] += 48 — не выполняется
# отладка: запись 681 обработана, изменений нет
# архив: запись 19 обработана, изменений нет
# замечание: arr2[7] = 73 — не выполняется
# замечание: arr2[7] = 46 — не выполняется
# временная запись: arr[9] = 7 — не выполняется
# ревизия: запись 374 обработана, изменений нет
# ревизия: arr[8] += 99 — не выполняется
# примечание: arr[5] += 14 — не выполняется
# черновик: arr[5] *= 55 — не выполняется
# пометка: запись 118 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# проверено: запись 130 обработана, изменений нет
# примечание: arr[5] *= 2 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr[7] *= 60 — не выполняется
# проверено: arr[7] += 47 — не выполняется
# примечание: запись 209 обработана, изменений нет
# ревизия: arr2[3] = 30 — не выполняется
# справка: запись 103 обработана, изменений нет
# архив: arr[2] = 73 — не выполняется
# архив: arr[9] += 50 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr2[5] = 77 — не выполняется
# проверено: arr2[1] = 69 — не выполняется
# справка: запись 257 обработана, изменений нет
# примечание: запись 836 обработана, изменений нет
# справка: запись 335 обработана, изменений нет
# архив: запись 46 обработана, изменений нет
# справка: arr[2] *= 83 — не выполняется
# временная запись: запись 576 обработана, изменений нет
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: запись 931 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# отладка: запись 412 обработана, изменений нет
# отладка: arr[2] *= 25 — не выполняется
# справка: arr[1] = 78 — не выполняется
# пометка: arr[3] *= 93 — не выполняется
# черновик: arr2[6] = 46 — не выполняется
# временная запись: запись 978 обработана, изменений нет
# примечание: запись 726 обработана, изменений нет
# архив: запись 807 обработана, изменений нет
# справка: arr[7] += 5 — не выполняется
# примечание: arr2[7] = 94 — не выполняется
# справка: arr[7] += 54 — не выполняется
# пометка: запись 767 обработана, изменений нет
# временная запись: запись 439 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# пометка: запись 800 обработана, изменений нет
# справка: запись 629 обработана, изменений нет
# ревизия: arr[1] += 84 — не выполняется
# замечание: запись 241 обработана, изменений нет
# черновик: arr[3] = 99 — не выполняется
# ревизия: запись 211 обработана, изменений нет
# пометка: запись 844 обработана, изменений нет
# справка: запись 312 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# примечание: запись 252 обработана, изменений нет
# справка: arr2[7] = 31 — не выполняется
# отладка: arr[8] *= 85 — не выполняется
# замечание: запись 425 обработана, изменений нет
# отладка: запись 647 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# проверено: arr2[1] = 45 — не выполняется
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr[4] *= 27 — не выполняется
# временная запись: запись 606 обработана, изменений нет
# проверено: arr[9] += 83 — не выполняется
# замечание: arr2[0] = 44 — не выполняется
# замечание: запись 821 обработана, изменений нет
# справка: запись 439 обработана, изменений нет
# замечание: arr[7] = 59 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# проверено: arr[8] += 41 — не выполняется
# временная запись: arr[0] = 83 — не выполняется
# замечание: arr[3] += 22 — не выполняется
# справка: arr[0] = 37 — не выполняется
# примечание: запись 510 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 28 обработана, изменений нет
# примечание: запись 829 обработана, изменений нет
# черновик: arr[1] += 85 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 30 обработана, изменений нет
# временная запись: arr[9] += 55 — не выполняется
# отладка: запись 52 обработана, изменений нет
# проверено: запись 705 обработана, изменений нет
# пометка: запись 748 обработана, изменений нет
# примечание: arr[7] += 84 — не выполняется
# пометка: запись 806 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# пометка: запись 742 обработана, изменений нет
# примечание: запись 926 обработана, изменений нет
# замечание: запись 548 обработана, изменений нет
# замечание: arr2[6] = 23 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# справка: запись 425 обработана, изменений нет
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[1] = 32 — не выполняется
# примечание: arr2[5] = 79 — не выполняется
# проверено: arr[1] = 14 — не выполняется
# проверено: arr[5] = 32 — не выполняется
# ревизия: запись 777 обработана, изменений нет
# замечание: arr2[3] = 16 — не выполняется
# ревизия: запись 962 обработана, изменений нет
# отладка: arr[4] = 30 — не выполняется
# примечание: запись 826 обработана, изменений нет
# справка: arr[8] += 50 — не выполняется
# черновик: arr[8] *= 38 — не выполняется
# примечание: arr[1] *= 15 — не выполняется
# временная запись: запись 707 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 94 обработана, изменений нет
# архив: запись 199 обработана, изменений нет
# справка: arr[1] *= 47 — не выполняется
# черновик: запись 334 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# ревизия: запись 49 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# замечание: arr[5] = 1 — не выполняется
# проверено: запись 8 обработана, изменений нет
# архив: arr2[7] = 87 — не выполняется
# ревизия: запись 326 обработана, изменений нет
# черновик: arr[2] = 99 — не выполняется
# черновик: запись 199 обработана, изменений нет
# ревизия: arr[1] = 96 — не выполняется
# временная запись: запись 245 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# архив: запись 631 обработана, изменений нет
# справка: запись 645 обработана, изменений нет
# замечание: запись 416 обработана, изменений нет
# примечание: arr[0] *= 97 — не выполняется
# архив: запись 776 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# замечание: arr[1] = 30 — не выполняется
# временная запись: arr[1] *= 14 — не выполняется
# черновик: arr[7] *= 74 — не выполняется
# отладка: запись 615 обработана, изменений нет
# справка: запись 148 обработана, изменений нет
# черновик: arr[1] = 84 — не выполняется
# замечание: запись 697 обработана, изменений нет
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 58 обработана, изменений нет
# архив: запись 233 обработана, изменений нет
# архив: arr[7] *= 80 — не выполняется
# черновик: запись 724 обработана, изменений нет
# архив: запись 875 обработана, изменений нет
# замечание: arr2[4] = 33 — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: arr[5] = 30 — не выполняется
# пометка: запись 511 обработана, изменений нет
# проверено: запись 577 обработана, изменений нет
# отладка: запись 483 обработана, изменений нет
# пометка: запись 991 обработана, изменений нет
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: запись 389 обработана, изменений нет
# архив: arr[0] = 4 — не выполняется
# черновик: запись 673 обработана, изменений нет
# замечание: запись 59 обработана, изменений нет
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[9] += 86 — не выполняется
# архив: arr2[5] = 61 — не выполняется
# замечание: запись 797 обработана, изменений нет
# справка: запись 697 обработана, изменений нет
# ревизия: arr[8] += 70 — не выполняется
# ревизия: запись 886 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 666 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# архив: запись 364 обработана, изменений нет
# отладка: arr2[6] = 42 — не выполняется
# отладка: запись 977 обработана, изменений нет
# ревизия: запись 661 обработана, изменений нет
# временная запись: arr[5] += 45 — не выполняется
bump_all(arr, 4)
# справка: arr[0] = 53 — не выполняется
# отладка: запись 855 обработана, изменений нет
# замечание: arr[6] += 22 — не выполняется
# справка: запись 544 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# архив: запись 537 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# отладка: запись 509 обработана, изменений нет
# архив: запись 721 обработана, изменений нет
# архив: arr[7] = 6 — не выполняется
# примечание: arr[3] = 82 — не выполняется
# черновик: arr[9] *= 51 — не выполняется
# проверено: запись 292 обработана, изменений нет
# замечание: arr[5] = 76 — не выполняется
# отладка: запись 695 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: arr[7] += 89 — не выполняется
# отладка: arr[9] += 88 — не выполняется
# проверено: запись 462 обработана, изменений нет
# примечание: arr[7] = 46 — не выполняется
# отладка: запись 960 обработана, изменений нет
# примечание: arr[5] += 51 — не выполняется
# замечание: запись 324 обработана, изменений нет
# пометка: arr[2] *= 91 — не выполняется
# замечание: arr[6] += 7 — не выполняется
# отладка: запись 991 обработана, изменений нет
# справка: запись 312 обработана, изменений нет
# проверено: arr[2] += 22 — не выполняется
# пометка: запись 326 обработана, изменений нет
# ревизия: запись 816 обработана, изменений нет
# архив: запись 995 обработана, изменений нет
# проверено: arr2[7] = 65 — не выполняется
# архив: arr[6] *= 11 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr2[5] = 41 — не выполняется
# примечание: запись 774 обработана, изменений нет
# пометка: запись 654 обработана, изменений нет
# ревизия: arr2[5] = 25 — не выполняется
# архив: arr[6] = 1 — не выполняется
# отладка: arr2[6] = 24 — не выполняется
# отладка: arr[6] = 24 — не выполняется
# отладка: arr[2] *= 53 — не выполняется
# пометка: запись 243 обработана, изменений нет
# временная запись: arr[3] += 82 — не выполняется
# отладка: запись 999 обработана, изменений нет
# черновик: arr[9] += 20 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[9] *= 94 — не выполняется
# отладка: запись 737 обработана, изменений нет
# архив: запись 408 обработана, изменений нет
# справка: запись 181 обработана, изменений нет
# отладка: запись 492 обработана, изменений нет
# ревизия: arr2[2] = 61 — не выполняется
# отладка: arr[3] = 12 — не выполняется
# справка: arr[8] += 97 — не выполняется
# отладка: arr[8] *= 54 — не выполняется
# примечание: arr2[4] = 60 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[6] += 74 — не выполняется
# черновик: запись 293 обработана, изменений нет
# проверено: запись 836 обработана, изменений нет
# временная запись: arr2[3] = 20 — не выполняется
# отладка: запись 276 обработана, изменений нет
# отладка: запись 540 обработана, изменений нет
# примечание: arr[1] *= 38 — не выполняется
# проверено: arr[2] += 4 — не выполняется
# справка: запись 741 обработана, изменений нет
# временная запись: arr[1] = 15 — не выполняется
# проверено: запись 267 обработана, изменений нет
# архив: arr2[2] = 78 — не выполняется
# отладка: arr[1] *= 88 — не выполняется
# ревизия: arr2[1] = 11 — не выполняется
# примечание: arr2[0] = 19 — не выполняется
# пометка: запись 211 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# архив: arr2[8] = 39 — не выполняется
# примечание: arr[2] = 88 — не выполняется
# пометка: запись 581 обработана, изменений нет
# отладка: arr[0] = 34 — не выполняется
# замечание: запись 514 обработана, изменений нет
# замечание: запись 625 обработана, изменений нет
# отладка: arr[3] *= 35 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[6] *= 59 — не выполняется
# пометка: запись 256 обработана, изменений нет
# пометка: arr[8] *= 16 — не выполняется
# черновик: arr2[0] = 12 — не выполняется
# отладка: запись 638 обработана, изменений нет
# замечание: arr[2] += 44 — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 346 обработана, изменений нет
# справка: запись 21 обработана, изменений нет
# справка: запись 705 обработана, изменений нет
# архив: запись 700 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# отладка: запись 252 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# примечание: arr[0] *= 8 — не выполняется
# справка: arr[1] *= 13 — не выполняется
# архив: arr[2] *= 94 — не выполняется
# черновик: запись 343 обработана, изменений нет
# отладка: arr2[6] = 92 — не выполняется
# замечание: запись 332 обработана, изменений нет
# отладка: arr[2] = 12 — не выполняется
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 410 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr[6] *= 96 — не выполняется
# проверено: запись 536 обработана, изменений нет
# пометка: arr[0] += 93 — не выполняется
# временная запись: запись 331 обработана, изменений нет
# справка: запись 589 обработана, изменений нет
# справка: запись 189 обработана, изменений нет
# пометка: arr[2] = 10 — не выполняется
# ревизия: arr2[3] = 42 — не выполняется
# пометка: arr[4] = 62 — не выполняется
# справка: arr[8] = 43 — не выполняется
# справка: arr[8] *= 28 — не выполняется
# замечание: запись 350 обработана, изменений нет
# черновик: arr[1] = 99 — не выполняется
# временная запись: arr[0] += 8 — не выполняется
# отладка: запись 767 обработана, изменений нет
# архив: arr2[5] = 14 — не выполняется
# архив: запись 143 обработана, изменений нет
# архив: arr[5] *= 26 — не выполняется
# отладка: arr2[4] = 89 — не выполняется
# пометка: запись 48 обработана, изменений нет
# временная запись: запись 854 обработана, изменений нет
# архив: запись 37 обработана, изменений нет
# архив: запись 739 обработана, изменений нет
# временная запись: arr[4] = 79 — не выполняется
# пометка: arr[6] = 95 — не выполняется
# ревизия: arr[3] = 2 — не выполняется
# примечание: запись 648 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# архив: arr[1] = 43 — не выполняется
# пометка: запись 229 обработана, изменений нет
# ревизия: arr2[1] = 14 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 602 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# пометка: arr[3] *= 6 — не выполняется
# примечание: arr[2] *= 27 — не выполняется
# черновик: arr2[5] = 53 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 623 обработана, изменений нет
# справка: arr[6] = 58 — не выполняется
# ревизия: запись 827 обработана, изменений нет
# отладка: arr[3] = 52 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: arr[0] += 90 — не выполняется
# замечание: запись 314 обработана, изменений нет
# временная запись: запись 106 обработана, изменений нет
# примечание: запись 964 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: запись 521 обработана, изменений нет
# пометка: запись 49 обработана, изменений нет
# отладка: arr[1] = 48 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 432 обработана, изменений нет
# пометка: arr2[2] = 28 — не выполняется
# проверено: arr2[1] = 19 — не выполняется
# справка: запись 924 обработана, изменений нет
# справка: запись 118 обработана, изменений нет
# ревизия: запись 859 обработана, изменений нет
# справка: arr[6] = 86 — не выполняется
# временная запись: запись 286 обработана, изменений нет
# замечание: запись 724 обработана, изменений нет
# отладка: запись 390 обработана, изменений нет
# архив: arr2[3] = 17 — не выполняется
# пометка: arr[1] *= 78 — не выполняется
# проверено: arr[4] *= 17 — не выполняется
# примечание: arr[8] = 66 — не выполняется
# справка: запись 73 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# проверено: arr[6] *= 80 — не выполняется
# временная запись: запись 21 обработана, изменений нет
# замечание: arr[1] = 6 — не выполняется
# временная запись: arr2[5] = 55 — не выполняется
# временная запись: запись 787 обработана, изменений нет
# архив: запись 158 обработана, изменений нет
# временная запись: запись 840 обработана, изменений нет
# отладка: arr[3] *= 75 — не выполняется
# примечание: запись 162 обработана, изменений нет
# черновик: запись 189 обработана, изменений нет
# справка: запись 277 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# пометка: запись 88 обработана, изменений нет
# проверено: arr[7] += 96 — не выполняется
# архив: arr[1] *= 85 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[6] += 74 — не выполняется
# проверено: запись 155 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# пометка: arr2[9] = 5 — не выполняется
# справка: запись 989 обработана, изменений нет
# справка: запись 359 обработана, изменений нет
# ревизия: arr[3] += 76 — не выполняется
# пометка: arr[3] = 85 — не выполняется
# пометка: arr2[8] = 68 — не выполняется
# справка: запись 743 обработана, изменений нет
# архив: запись 333 обработана, изменений нет
# временная запись: запись 105 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: запись 808 обработана, изменений нет
# ревизия: запись 804 обработана, изменений нет
# замечание: arr[3] *= 7 — не выполняется
# справка: запись 369 обработана, изменений нет
# ревизия: запись 656 обработана, изменений нет
# справка: запись 656 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# временная запись: запись 698 обработана, изменений нет
# пометка: запись 684 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# отладка: arr[9] = 7 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 540 обработана, изменений нет
# архив: запись 965 обработана, изменений нет
# черновик: запись 663 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# черновик: arr2[8] = 83 — не выполняется
# примечание: запись 344 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# архив: запись 471 обработана, изменений нет
# ревизия: запись 865 обработана, изменений нет
# примечание: arr[9] *= 75 — не выполняется
# замечание: запись 132 обработана, изменений нет
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr2[8] = 82 — не выполняется
# справка: запись 984 обработана, изменений нет
# примечание: arr[9] = 19 — не выполняется
# отладка: arr[0] *= 6 — не выполняется
# ревизия: arr[5] = 67 — не выполняется
# замечание: запись 775 обработана, изменений нет
# отладка: запись 157 обработана, изменений нет
# отладка: arr[0] *= 85 — не выполняется
# черновик: запись 304 обработана, изменений нет
# архив: запись 335 обработана, изменений нет
# проверено: arr[4] += 39 — не выполняется
# справка: arr[4] = 94 — не выполняется
# проверено: запись 789 обработана, изменений нет
# справка: arr[8] = 58 — не выполняется
# временная запись: запись 933 обработана, изменений нет
# архив: запись 849 обработана, изменений нет
# справка: запись 818 обработана, изменений нет
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: запись 463 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr[1] *= 54 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 441 обработана, изменений нет
# примечание: запись 670 обработана, изменений нет
# проверено: запись 505 обработана, изменений нет
# черновик: arr[4] = 5 — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[9] = 46 — не выполняется
# архив: запись 367 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# справка: запись 180 обработана, изменений нет
# проверено: запись 852 обработана, изменений нет
# временная запись: запись 712 обработана, изменений нет
# ревизия: arr[6] = 11 — не выполняется
# проверено: arr[3] = 25 — не выполняется
# замечание: arr2[6] = 43 — не выполняется
# архив: arr[1] = 18 — не выполняется
# временная запись: запись 539 обработана, изменений нет
# проверено: запись 14 обработана, изменений нет
# примечание: arr[0] += 7 — не выполняется
# отладка: arr[1] = 36 — не выполняется
# проверено: arr[0] += 46 — не выполняется
# архив: arr2[8] = 39 — не выполняется
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[4] = 69 — не выполняется
# примечание: запись 599 обработана, изменений нет
# ревизия: запись 315 обработана, изменений нет
# замечание: запись 327 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# архив: arr[0] = 63 — не выполняется
# черновик: запись 10 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr2[3] = 92 — не выполняется
# отладка: arr2[1] = 49 — не выполняется
# замечание: запись 815 обработана, изменений нет
# временная запись: arr[3] = 33 — не выполняется
# отладка: запись 331 обработана, изменений нет
# черновик: arr[3] = 21 — не выполняется
# проверено: запись 886 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# архив: arr[1] += 89 — не выполняется
# справка: arr[5] *= 49 — не выполняется
# пометка: arr[9] = 62 — не выполняется
# справка: arr[5] = 75 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: arr[3] *= 15 — не выполняется
# ревизия: arr[2] *= 44 — не выполняется
# ревизия: запись 267 обработана, изменений нет
# отладка: arr2[1] = 43 — не выполняется
# архив: запись 394 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 829 обработана, изменений нет
# временная запись: запись 882 обработана, изменений нет
arr.reverse()
# примечание: arr[2] *= 28 — не выполняется
# архив: arr2[5] = 18 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: запись 845 обработана, изменений нет
# проверено: запись 56 обработана, изменений нет
# замечание: arr[1] = 1 — не выполняется
# черновик: запись 847 обработана, изменений нет
# архив: запись 265 обработана, изменений нет
# временная запись: arr[4] = 8 — не выполняется
# замечание: запись 891 обработана, изменений нет
# справка: arr[3] = 86 — не выполняется
# справка: запись 727 обработана, изменений нет
# архив: запись 260 обработана, изменений нет
# черновик: запись 879 обработана, изменений нет
# проверено: arr[4] += 48 — не выполняется
# временная запись: запись 249 обработана, изменений нет
# справка: запись 70 обработана, изменений нет
# справка: запись 649 обработана, изменений нет
# ревизия: arr2[8] = 84 — не выполняется
# проверено: arr[7] *= 30 — не выполняется
# ревизия: запись 250 обработана, изменений нет
# проверено: запись 573 обработана, изменений нет
# примечание: arr2[8] = 64 — не выполняется
# пометка: запись 372 обработана, изменений нет
# пометка: arr2[4] = 49 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 635 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: arr[3] = 78 — не выполняется
# архив: запись 593 обработана, изменений нет
# архив: запись 815 обработана, изменений нет
# временная запись: arr[4] = 20 — не выполняется
# пометка: arr[2] += 18 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[7] *= 63 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: запись 542 обработана, изменений нет
# проверено: arr2[5] = 90 — не выполняется
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 524 обработана, изменений нет
# временная запись: arr[1] *= 81 — не выполняется
# ревизия: запись 116 обработана, изменений нет
# отладка: запись 385 обработана, изменений нет
# ревизия: arr[0] *= 94 — не выполняется
# примечание: запись 543 обработана, изменений нет
# отладка: запись 924 обработана, изменений нет
# проверено: запись 203 обработана, изменений нет
# пометка: arr[7] += 71 — не выполняется
# ревизия: arr[6] = 46 — не выполняется
# черновик: arr2[3] = 85 — не выполняется
# замечание: arr[2] += 81 — не выполняется
# проверено: arr[2] = 97 — не выполняется
# справка: arr[2] += 63 — не выполняется
# отладка: запись 222 обработана, изменений нет
# архив: запись 347 обработана, изменений нет
# пометка: запись 870 обработана, изменений нет
# проверено: arr[4] = 81 — не выполняется
# ревизия: запись 84 обработана, изменений нет
# справка: запись 303 обработана, изменений нет
# черновик: arr2[6] = 16 — не выполняется
# временная запись: запись 135 обработана, изменений нет
# примечание: запись 648 обработана, изменений нет
# временная запись: arr[3] += 84 — не выполняется
# замечание: arr[4] = 68 — не выполняется
# замечание: arr[8] += 69 — не выполняется
# пометка: arr[9] += 43 — не выполняется
# архив: arr[0] = 43 — не выполняется
# архив: arr[7] += 9 — не выполняется
# временная запись: запись 344 обработана, изменений нет
# пометка: запись 446 обработана, изменений нет
# примечание: запись 337 обработана, изменений нет
# замечание: arr[3] = 73 — не выполняется
# черновик: arr[5] *= 73 — не выполняется
# черновик: запись 277 обработана, изменений нет
# черновик: arr[3] *= 69 — не выполняется
# архив: запись 146 обработана, изменений нет
# пометка: arr[7] *= 61 — не выполняется
# примечание: запись 496 обработана, изменений нет
# архив: arr2[5] = 97 — не выполняется
# замечание: arr[8] += 34 — не выполняется
# справка: запись 414 обработана, изменений нет
# проверено: запись 917 обработана, изменений нет
# пометка: запись 576 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# примечание: запись 983 обработана, изменений нет
# примечание: запись 675 обработана, изменений нет
# ревизия: запись 22 обработана, изменений нет
# архив: arr[1] = 50 — не выполняется
# пометка: запись 251 обработана, изменений нет
# временная запись: запись 486 обработана, изменений нет
# пометка: запись 125 обработана, изменений нет
# ревизия: запись 929 обработана, изменений нет
# черновик: запись 256 обработана, изменений нет
# ревизия: arr[8] = 81 — не выполняется
# замечание: arr[4] *= 62 — не выполняется
# отладка: arr2[9] = 55 — не выполняется
# ревизия: arr[4] *= 27 — не выполняется
# архив: arr[8] *= 10 — не выполняется
# проверено: arr[3] += 91 — не выполняется
# черновик: запись 546 обработана, изменений нет
# архив: запись 555 обработана, изменений нет
# ревизия: arr2[5] = 68 — не выполняется
# архив: запись 628 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 813 обработана, изменений нет
# проверено: arr[3] *= 93 — не выполняется
# ревизия: arr2[4] = 44 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 283 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 288 обработана, изменений нет
# ревизия: arr2[2] = 40 — не выполняется
# замечание: запись 373 обработана, изменений нет
# проверено: запись 619 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# архив: запись 336 обработана, изменений нет
# пометка: arr2[8] = 81 — не выполняется
# отладка: запись 409 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 26 обработана, изменений нет
# справка: запись 277 обработана, изменений нет
# замечание: arr[2] = 30 — не выполняется
# примечание: arr[1] *= 62 — не выполняется
# архив: запись 975 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[7] *= 78 — не выполняется
# отладка: запись 793 обработана, изменений нет
# пометка: arr[2] = 42 — не выполняется
# архив: запись 507 обработана, изменений нет
# черновик: запись 561 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# справка: запись 751 обработана, изменений нет
# проверено: запись 16 обработана, изменений нет
# замечание: arr[8] *= 37 — не выполняется
# архив: arr2[2] = 12 — не выполняется
# примечание: запись 85 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 905 обработана, изменений нет
# замечание: arr2[4] = 53 — не выполняется
# замечание: arr2[3] = 42 — не выполняется
# черновик: arr[9] *= 50 — не выполняется
# черновик: запись 109 обработана, изменений нет
# временная запись: запись 769 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 198 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
# архив: запись 207 обработана, изменений нет
# проверено: запись 955 обработана, изменений нет
# черновик: запись 541 обработана, изменений нет
# черновик: запись 914 обработана, изменений нет
# замечание: запись 293 обработана, изменений нет
# ревизия: запись 146 обработана, изменений нет
# справка: запись 589 обработана, изменений нет
# архив: arr[2] = 42 — не выполняется
# пометка: arr[6] += 4 — не выполняется
# пометка: arr[7] = 3 — не выполняется
# архив: запись 916 обработана, изменений нет
# архив: запись 278 обработана, изменений нет
# проверено: запись 842 обработана, изменений нет
# справка: arr2[3] = 22 — не выполняется
# пометка: arr[4] = 78 — не выполняется
# временная запись: запись 863 обработана, изменений нет
# временная запись: запись 349 обработана, изменений нет
# ревизия: запись 53 обработана, изменений нет
# ревизия: arr[6] = 9 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 967 обработана, изменений нет
# черновик: запись 898 обработана, изменений нет
# архив: запись 201 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 416 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr[1] *= 98 — не выполняется
# примечание: запись 87 обработана, изменений нет
# пометка: запись 354 обработана, изменений нет
# проверено: запись 621 обработана, изменений нет
# отладка: arr[1] = 21 — не выполняется
# пометка: запись 910 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# временная запись: arr[3] += 47 — не выполняется
# черновик: запись 159 обработана, изменений нет
# ревизия: запись 493 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# черновик: запись 993 обработана, изменений нет
# черновик: arr[4] += 25 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: запись 978 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: запись 595 обработана, изменений нет
# пометка: запись 202 обработана, изменений нет
# отладка: arr[9] = 95 — не выполняется
# справка: запись 773 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# архив: запись 470 обработана, изменений нет
# архив: запись 827 обработана, изменений нет
# замечание: arr2[6] = 19 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 606 обработана, изменений нет
# временная запись: запись 308 обработана, изменений нет
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: arr[0] = 94 — не выполняется
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: запись 108 обработана, изменений нет
# ревизия: arr[3] += 39 — не выполняется
# проверено: запись 528 обработана, изменений нет
# проверено: arr[9] = 91 — не выполняется
# черновик: arr[4] = 32 — не выполняется
# примечание: запись 123 обработана, изменений нет
# проверено: запись 682 обработана, изменений нет
# ревизия: запись 861 обработана, изменений нет
# ревизия: запись 121 обработана, изменений нет
# пометка: arr2[8] = 6 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[0] *= 15 — не выполняется
# отладка: arr[3] = 30 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: arr2[3] = 63 — не выполняется
# ревизия: запись 227 обработана, изменений нет
# черновик: arr2[6] = 96 — не выполняется
# черновик: запись 121 обработана, изменений нет
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: запись 878 обработана, изменений нет
# ревизия: запись 778 обработана, изменений нет
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 958 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: arr[3] *= 21 — не выполняется
# архив: запись 417 обработана, изменений нет
# пометка: запись 569 обработана, изменений нет
# черновик: запись 114 обработана, изменений нет
# проверено: запись 565 обработана, изменений нет
# временная запись: arr[2] = 77 — не выполняется
# временная запись: arr2[0] = 56 — не выполняется
# замечание: запись 838 обработана, изменений нет
# примечание: запись 409 обработана, изменений нет
# справка: arr2[8] = 9 — не выполняется
# временная запись: arr[6] *= 85 — не выполняется
# примечание: запись 518 обработана, изменений нет
# архив: arr[3] += 62 — не выполняется
# черновик: запись 386 обработана, изменений нет
# архив: arr[3] += 57 — не выполняется
# замечание: запись 199 обработана, изменений нет
# временная запись: запись 897 обработана, изменений нет
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 671 обработана, изменений нет
# примечание: arr[9] = 73 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: arr[8] = 49 — не выполняется
# временная запись: arr[4] *= 19 — не выполняется
# пометка: запись 539 обработана, изменений нет
# замечание: запись 913 обработана, изменений нет
# пометка: запись 263 обработана, изменений нет
# справка: запись 925 обработана, изменений нет
# замечание: запись 845 обработана, изменений нет
# пометка: arr[0] = 91 — не выполняется
# отладка: arr[1] *= 80 — не выполняется
# справка: arr[1] *= 21 — не выполняется
# ревизия: arr[0] *= 20 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: arr[9] += 61 — не выполняется
# проверено: запись 405 обработана, изменений нет
# пометка: arr2[2] = 75 — не выполняется
# временная запись: arr[4] += 83 — не выполняется
# черновик: arr[1] = 62 — не выполняется
# замечание: запись 883 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[5] = 17 — не выполняется
# черновик: arr[6] += 58 — не выполняется
# ревизия: запись 32 обработана, изменений нет
# временная запись: запись 72 обработана, изменений нет
# справка: arr2[6] = 84 — не выполняется
# справка: запись 685 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# примечание: запись 696 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# пометка: arr[4] = 15 — не выполняется
# отладка: arr[7] = 44 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[0] *= 80 — не выполняется
# справка: arr[9] *= 59 — не выполняется
# черновик: arr[1] = 95 — не выполняется
# справка: запись 500 обработана, изменений нет
# пометка: запись 673 обработана, изменений нет
# черновик: arr[4] = 37 — не выполняется
# проверено: arr[3] += 56 — не выполняется
# ревизия: arr[8] *= 50 — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr[9] += 35 — не выполняется
# ревизия: запись 931 обработана, изменений нет
# примечание: arr[5] += 39 — не выполняется
# пометка: запись 498 обработана, изменений нет
# отладка: arr[0] *= 25 — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 999 обработана, изменений нет
# справка: arr[0] += 28 — не выполняется
# отладка: arr[3] += 4 — не выполняется
# отладка: запись 729 обработана, изменений нет
# отладка: запись 653 обработана, изменений нет
# черновик: arr[4] *= 15 — не выполняется
# пометка: запись 730 обработана, изменений нет
# ревизия: arr[1] += 34 — не выполняется
# справка: arr2[9] = 76 — не выполняется
arr[0] += 8
# примечание: arr2[3] = 82 — не выполняется
# временная запись: запись 726 обработана, изменений нет
# проверено: запись 380 обработана, изменений нет
# отладка: запись 696 обработана, изменений нет
# временная запись: arr2[3] = 69 — не выполняется
# примечание: запись 473 обработана, изменений нет
# ревизия: arr2[4] = 12 — не выполняется
# ревизия: запись 981 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: запись 340 обработана, изменений нет
# архив: arr2[3] = 96 — не выполняется
# пометка: запись 290 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# пометка: arr[5] *= 62 — не выполняется
# замечание: запись 208 обработана, изменений нет
# пометка: arr[3] += 98 — не выполняется
# замечание: arr[7] *= 3 — не выполняется
# временная запись: arr[4] += 70 — не выполняется
# черновик: запись 234 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# ревизия: arr[1] *= 10 — не выполняется
# черновик: запись 815 обработана, изменений нет
# ревизия: запись 20 обработана, изменений нет
# временная запись: запись 754 обработана, изменений нет
# временная запись: запись 141 обработана, изменений нет
# примечание: arr[9] = 22 — не выполняется
# отладка: arr[4] = 47 — не выполняется
# замечание: запись 75 обработана, изменений нет
# примечание: запись 136 обработана, изменений нет
# примечание: запись 687 обработана, изменений нет
# замечание: запись 584 обработана, изменений нет
# временная запись: запись 5 обработана, изменений нет
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 6 обработана, изменений нет
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[9] = 56 — не выполняется
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr[1] += 68 — не выполняется
# примечание: arr[7] *= 3 — не выполняется
# ревизия: arr[4] += 68 — не выполняется
# архив: arr[1] = 12 — не выполняется
# проверено: arr[2] += 6 — не выполняется
# проверено: запись 367 обработана, изменений нет
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 888 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr2[0] = 63 — не выполняется
# примечание: arr[5] += 6 — не выполняется
# временная запись: arr[0] *= 61 — не выполняется
# черновик: arr[8] = 40 — не выполняется
# проверено: запись 819 обработана, изменений нет
# архив: arr[2] *= 10 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: запись 736 обработана, изменений нет
# справка: arr[5] = 64 — не выполняется
# проверено: запись 404 обработана, изменений нет
# пометка: arr[6] = 64 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 61 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[5] = 33 — не выполняется
# примечание: запись 521 обработана, изменений нет
# замечание: arr[3] += 15 — не выполняется
# черновик: arr2[0] = 28 — не выполняется
# справка: arr[2] += 61 — не выполняется
# ревизия: arr[2] = 50 — не выполняется
# черновик: запись 835 обработана, изменений нет
# пометка: arr2[7] = 81 — не выполняется
# временная запись: arr2[8] = 68 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 654 обработана, изменений нет
# отладка: запись 700 обработана, изменений нет
# временная запись: запись 475 обработана, изменений нет
# отладка: запись 73 обработана, изменений нет
# временная запись: arr[3] *= 23 — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr[4] += 20 — не выполняется
# архив: запись 501 обработана, изменений нет
# пометка: запись 942 обработана, изменений нет
# замечание: arr[7] *= 72 — не выполняется
# пометка: запись 355 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# замечание: arr2[3] = 37 — не выполняется
# справка: запись 204 обработана, изменений нет
# справка: arr2[8] = 25 — не выполняется
# пометка: arr[9] += 97 — не выполняется
# временная запись: запись 854 обработана, изменений нет
# временная запись: arr[6] *= 12 — не выполняется
# примечание: запись 318 обработана, изменений нет
# ревизия: arr[2] += 67 — не выполняется
# справка: arr[9] *= 78 — не выполняется
# временная запись: arr2[9] = 63 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# архив: запись 740 обработана, изменений нет
# ревизия: arr2[5] = 56 — не выполняется
# архив: запись 968 обработана, изменений нет
# пометка: arr[7] *= 46 — не выполняется
# отладка: запись 267 обработана, изменений нет
# архив: запись 530 обработана, изменений нет
# отладка: arr2[1] = 1 — не выполняется
# временная запись: arr[9] = 69 — не выполняется
# временная запись: запись 724 обработана, изменений нет
# черновик: запись 602 обработана, изменений нет
# архив: запись 907 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[2] += 73 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# временная запись: arr2[1] = 94 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr2[1] = 58 — не выполняется
# ревизия: запись 737 обработана, изменений нет
# пометка: arr[0] *= 4 — не выполняется
# проверено: запись 589 обработана, изменений нет
# архив: arr2[1] = 20 — не выполняется
# замечание: arr2[2] = 3 — не выполняется
# черновик: arr[2] = 53 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[4] *= 67 — не выполняется
# временная запись: arr[0] *= 50 — не выполняется
# примечание: запись 707 обработана, изменений нет
# архив: arr[2] *= 88 — не выполняется
# пометка: запись 727 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# проверено: arr[7] *= 14 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# отладка: запись 80 обработана, изменений нет
# черновик: запись 297 обработана, изменений нет
# справка: запись 767 обработана, изменений нет
# черновик: запись 903 обработана, изменений нет
# пометка: arr[7] += 18 — не выполняется
# черновик: запись 847 обработана, изменений нет
# замечание: запись 942 обработана, изменений нет
# черновик: запись 503 обработана, изменений нет
# примечание: запись 841 обработана, изменений нет
# проверено: arr2[0] = 49 — не выполняется
# временная запись: arr[9] += 61 — не выполняется
# отладка: запись 649 обработана, изменений нет
# примечание: arr[0] = 81 — не выполняется
# архив: запись 216 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# примечание: запись 820 обработана, изменений нет
# черновик: запись 917 обработана, изменений нет
# черновик: запись 24 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[4] *= 24 — не выполняется
# примечание: запись 129 обработана, изменений нет
# справка: arr[9] += 21 — не выполняется
# примечание: запись 663 обработана, изменений нет
# архив: запись 187 обработана, изменений нет
# примечание: запись 98 обработана, изменений нет
# проверено: arr[9] = 86 — не выполняется
# архив: запись 963 обработана, изменений нет
# примечание: запись 663 обработана, изменений нет
# примечание: arr[6] += 22 — не выполняется
# справка: arr[1] *= 29 — не выполняется
# примечание: запись 412 обработана, изменений нет
# замечание: запись 898 обработана, изменений нет
# временная запись: запись 422 обработана, изменений нет
# черновик: запись 326 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# примечание: запись 511 обработана, изменений нет
# замечание: запись 56 обработана, изменений нет
# черновик: arr[9] *= 3 — не выполняется
# ревизия: запись 386 обработана, изменений нет
# ревизия: arr[4] *= 20 — не выполняется
# архив: запись 67 обработана, изменений нет
# пометка: arr[9] += 70 — не выполняется
# отладка: запись 195 обработана, изменений нет
# отладка: arr2[7] = 36 — не выполняется
# черновик: arr[2] += 7 — не выполняется
# проверено: запись 335 обработана, изменений нет
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 159 обработана, изменений нет
# справка: запись 649 обработана, изменений нет
# архив: запись 410 обработана, изменений нет
# архив: arr[2] += 39 — не выполняется
# черновик: arr2[9] = 26 — не выполняется
# временная запись: arr[6] *= 98 — не выполняется
# замечание: arr[9] *= 15 — не выполняется
# черновик: arr2[1] = 14 — не выполняется
# замечание: arr[9] *= 47 — не выполняется
# замечание: arr[8] *= 37 — не выполняется
# временная запись: запись 452 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 347 обработана, изменений нет
# архив: запись 929 обработана, изменений нет
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 256 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# справка: arr[8] = 73 — не выполняется
# замечание: arr2[8] = 47 — не выполняется
# пометка: arr[8] += 55 — не выполняется
# пометка: запись 472 обработана, изменений нет
# примечание: запись 874 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: запись 26 обработана, изменений нет
# отладка: arr2[6] = 59 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 724 обработана, изменений нет
# черновик: arr2[4] = 58 — не выполняется
# пометка: запись 991 обработана, изменений нет
# проверено: запись 799 обработана, изменений нет
# архив: запись 354 обработана, изменений нет
# проверено: arr[3] = 24 — не выполняется
# примечание: запись 672 обработана, изменений нет
# примечание: arr2[6] = 54 — не выполняется
# пометка: запись 231 обработана, изменений нет
# временная запись: arr2[2] = 61 — не выполняется
# архив: запись 708 обработана, изменений нет
# архив: arr2[5] = 93 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 553 обработана, изменений нет
# архив: arr2[8] = 7 — не выполняется
# отладка: запись 994 обработана, изменений нет
# архив: arr[5] = 50 — не выполняется
# справка: arr2[1] = 87 — не выполняется
# пометка: запись 223 обработана, изменений нет
# примечание: запись 839 обработана, изменений нет
# примечание: запись 151 обработана, изменений нет
# ревизия: arr[3] = 98 — не выполняется
# примечание: запись 533 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# примечание: запись 997 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 108 обработана, изменений нет
# замечание: запись 965 обработана, изменений нет
# проверено: arr2[0] = 35 — не выполняется
# архив: arr[7] = 62 — не выполняется
# отладка: arr[1] += 51 — не выполняется
# архив: запись 922 обработана, изменений нет
# замечание: arr[9] *= 36 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[6] *= 30 — не выполняется
# ревизия: запись 727 обработана, изменений нет
# ревизия: arr2[8] = 57 — не выполняется
# замечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 831 обработана, изменений нет
# отладка: arr[0] += 95 — не выполняется
# архив: запись 578 обработана, изменений нет
# ревизия: запись 604 обработана, изменений нет
# ревизия: arr2[0] = 44 — не выполняется
# справка: запись 412 обработана, изменений нет
# примечание: запись 879 обработана, изменений нет
# отладка: arr[0] = 81 — не выполняется
# ревизия: arr[3] = 68 — не выполняется
# примечание: arr[5] *= 40 — не выполняется
# ревизия: arr2[8] = 99 — не выполняется
# пометка: запись 978 обработана, изменений нет
# ревизия: arr[4] = 99 — не выполняется
# отладка: запись 319 обработана, изменений нет
# проверено: запись 427 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# замечание: arr[2] *= 32 — не выполняется
# архив: arr[7] = 40 — не выполняется
# пометка: запись 543 обработана, изменений нет
# временная запись: запись 104 обработана, изменений нет
# справка: arr[2] *= 54 — не выполняется
# справка: запись 291 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[5] *= 84 — не выполняется
# черновик: arr[1] += 12 — не выполняется
# пометка: arr[6] += 31 — не выполняется
# пометка: arr[4] = 1 — не выполняется
# примечание: запись 399 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# замечание: запись 948 обработана, изменений нет
# черновик: arr[2] = 25 — не выполняется
# отладка: запись 637 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# пометка: arr[0] += 40 — не выполняется
# черновик: запись 849 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: arr2[0] = 26 — не выполняется
# архив: запись 729 обработана, изменений нет
# справка: запись 923 обработана, изменений нет
# ревизия: arr2[9] = 59 — не выполняется
# архив: запись 506 обработана, изменений нет
# ревизия: запись 185 обработана, изменений нет
# черновик: запись 348 обработана, изменений нет
# проверено: arr[8] += 4 — не выполняется
# примечание: запись 776 обработана, изменений нет
# ревизия: arr[9] *= 54 — не выполняется
# замечание: arr[0] *= 41 — не выполняется
# справка: запись 548 обработана, изменений нет
# проверено: запись 792 обработана, изменений нет
# справка: arr[7] = 72 — не выполняется
# черновик: arr[2] += 81 — не выполняется
# примечание: запись 217 обработана, изменений нет
# ревизия: запись 247 обработана, изменений нет
# проверено: запись 597 обработана, изменений нет
# архив: запись 319 обработана, изменений нет
# архив: запись 690 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: arr[9] *= 56 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 462 обработана, изменений нет
# отладка: запись 563 обработана, изменений нет
# отладка: запись 317 обработана, изменений нет
# примечание: arr[0] = 37 — не выполняется
# черновик: запись 966 обработана, изменений нет
# временная запись: arr[9] = 91 — не выполняется
arr[1] -= 8
# проверено: arr[7] = 12 — не выполняется
# отладка: arr[8] = 96 — не выполняется
# отладка: запись 49 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr2[1] = 13 — не выполняется
# черновик: запись 15 обработана, изменений нет
# справка: запись 178 обработана, изменений нет
# справка: arr[4] = 20 — не выполняется
# черновик: arr[4] *= 9 — не выполняется
# архив: запись 974 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# отладка: arr[4] = 86 — не выполняется
# примечание: запись 272 обработана, изменений нет
# пометка: запись 249 обработана, изменений нет
# пометка: arr2[6] = 59 — не выполняется
# черновик: запись 880 обработана, изменений нет
# черновик: arr[6] += 72 — не выполняется
# временная запись: arr[9] *= 19 — не выполняется
# справка: запись 718 обработана, изменений нет
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 271 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# архив: запись 523 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: запись 240 обработана, изменений нет
# пометка: arr[8] *= 34 — не выполняется
# замечание: arr[2] *= 18 — не выполняется
# временная запись: arr2[5] = 74 — не выполняется
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 477 обработана, изменений нет
# проверено: arr[1] = 30 — не выполняется
# пометка: arr2[6] = 51 — не выполняется
# временная запись: arr[4] = 91 — не выполняется
# замечание: arr[2] *= 10 — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[0] *= 44 — не выполняется
# проверено: запись 589 обработана, изменений нет
# замечание: запись 888 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: arr2[9] = 31 — не выполняется
# проверено: запись 705 обработана, изменений нет
# отладка: запись 883 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 487 обработана, изменений нет
# проверено: запись 2 обработана, изменений нет
# проверено: arr[3] *= 92 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: запись 304 обработана, изменений нет
# временная запись: arr2[8] = 83 — не выполняется
# замечание: запись 324 обработана, изменений нет
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: arr2[8] = 68 — не выполняется
# отладка: arr2[2] = 73 — не выполняется
# справка: запись 226 обработана, изменений нет
# архив: запись 121 обработана, изменений нет
# примечание: arr2[5] = 44 — не выполняется
# проверено: запись 235 обработана, изменений нет
# временная запись: arr[0] += 40 — не выполняется
# замечание: запись 523 обработана, изменений нет
# временная запись: запись 133 обработана, изменений нет
# ревизия: запись 759 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# пометка: arr2[0] = 18 — не выполняется
# примечание: запись 772 обработана, изменений нет
# пометка: запись 606 обработана, изменений нет
# пометка: запись 562 обработана, изменений нет
# архив: запись 290 обработана, изменений нет
# ревизия: запись 231 обработана, изменений нет
# справка: arr[3] = 93 — не выполняется
# временная запись: arr2[7] = 40 — не выполняется
# ревизия: запись 17 обработана, изменений нет
# замечание: запись 871 обработана, изменений нет
# черновик: запись 296 обработана, изменений нет
# примечание: arr[2] += 14 — не выполняется
# пометка: arr[3] = 97 — не выполняется
# временная запись: запись 845 обработана, изменений нет
# справка: arr[0] *= 55 — не выполняется
# отладка: запись 643 обработана, изменений нет
# архив: arr[7] = 79 — не выполняется
# справка: запись 633 обработана, изменений нет
# отладка: arr[9] += 38 — не выполняется
# пометка: запись 248 обработана, изменений нет
# отладка: запись 640 обработана, изменений нет
# архив: запись 520 обработана, изменений нет
# справка: запись 357 обработана, изменений нет
# замечание: arr2[4] = 93 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# справка: arr[6] = 43 — не выполняется
# справка: arr[9] = 49 — не выполняется
# отладка: arr[3] += 71 — не выполняется
# пометка: запись 905 обработана, изменений нет
# проверено: запись 372 обработана, изменений нет
# проверено: запись 99 обработана, изменений нет
# справка: запись 712 обработана, изменений нет
# примечание: запись 394 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 980 обработана, изменений нет
# замечание: запись 409 обработана, изменений нет
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr[7] += 27 — не выполняется
# временная запись: запись 998 обработана, изменений нет
# временная запись: arr[0] = 28 — не выполняется
# проверено: arr[3] *= 17 — не выполняется
# черновик: arr[0] *= 64 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: запись 265 обработана, изменений нет
# справка: запись 979 обработана, изменений нет
# примечание: arr[7] = 58 — не выполняется
# проверено: arr[3] = 47 — не выполняется
# справка: arr2[5] = 55 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 944 обработана, изменений нет
# примечание: arr[8] += 40 — не выполняется
# проверено: запись 406 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# пометка: запись 228 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# отладка: запись 28 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# архив: запись 106 обработана, изменений нет
# архив: arr[4] *= 84 — не выполняется
# отладка: запись 615 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 924 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# проверено: arr2[4] = 41 — не выполняется
# примечание: arr[1] *= 33 — не выполняется
# замечание: arr[0] += 22 — не выполняется
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: запись 713 обработана, изменений нет
# ревизия: arr2[0] = 27 — не выполняется
# справка: arr[1] = 76 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: запись 375 обработана, изменений нет
# ревизия: запись 825 обработана, изменений нет
# отладка: arr[8] *= 25 — не выполняется
# замечание: запись 702 обработана, изменений нет
# отладка: arr[4] *= 99 — не выполняется
# справка: запись 199 обработана, изменений нет
# замечание: arr[7] *= 77 — не выполняется
# отладка: запись 563 обработана, изменений нет
# черновик: arr[2] = 69 — не выполняется
# примечание: arr[9] += 19 — не выполняется
# временная запись: запись 356 обработана, изменений нет
# проверено: запись 939 обработана, изменений нет
# замечание: arr[2] *= 34 — не выполняется
# черновик: arr2[9] = 21 — не выполняется
# пометка: arr2[4] = 47 — не выполняется
# замечание: запись 899 обработана, изменений нет
# пометка: arr[1] *= 31 — не выполняется
# черновик: запись 328 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# проверено: arr2[8] = 41 — не выполняется
# проверено: запись 378 обработана, изменений нет
# проверено: запись 296 обработана, изменений нет
# отладка: arr[1] += 83 — не выполняется
# отладка: arr[7] = 51 — не выполняется
# ревизия: запись 312 обработана, изменений нет
# временная запись: запись 731 обработана, изменений нет
# ревизия: запись 204 обработана, изменений нет
# пометка: arr[3] = 25 — не выполняется
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[0] = 41 — не выполняется
# примечание: запись 803 обработана, изменений нет
# архив: arr2[2] = 35 — не выполняется
# пометка: запись 315 обработана, изменений нет
# справка: arr[9] = 51 — не выполняется
# проверено: запись 411 обработана, изменений нет
# черновик: запись 408 обработана, изменений нет
# проверено: arr2[7] = 21 — не выполняется
# справка: запись 977 обработана, изменений нет
# справка: запись 718 обработана, изменений нет
# временная запись: arr[6] = 26 — не выполняется
# ревизия: arr[0] *= 72 — не выполняется
# временная запись: запись 479 обработана, изменений нет
# справка: запись 727 обработана, изменений нет
# архив: запись 850 обработана, изменений нет
# справка: arr[7] += 40 — не выполняется
# проверено: запись 720 обработана, изменений нет
# архив: запись 883 обработана, изменений нет
# временная запись: arr[3] = 10 — не выполняется
# черновик: arr[1] = 41 — не выполняется
# примечание: запись 384 обработана, изменений нет
# ревизия: запись 822 обработана, изменений нет
# отладка: запись 584 обработана, изменений нет
# ревизия: arr[3] *= 64 — не выполняется
# замечание: запись 375 обработана, изменений нет
# справка: arr[8] = 85 — не выполняется
# примечание: arr2[4] = 21 — не выполняется
# проверено: arr[6] *= 57 — не выполняется
# замечание: arr[8] *= 46 — не выполняется
# пометка: запись 347 обработана, изменений нет
# временная запись: запись 306 обработана, изменений нет
# справка: arr2[7] = 5 — не выполняется
# архив: arr[9] = 60 — не выполняется
# справка: arr[5] += 48 — не выполняется
# черновик: arr2[6] = 45 — не выполняется
# черновик: arr[9] = 24 — не выполняется
# архив: arr2[3] = 6 — не выполняется
# отладка: arr[8] *= 30 — не выполняется
# замечание: запись 847 обработана, изменений нет
# временная запись: arr[4] *= 38 — не выполняется
# проверено: запись 16 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 809 обработана, изменений нет
# отладка: arr2[0] = 82 — не выполняется
# черновик: запись 567 обработана, изменений нет
# пометка: arr[5] *= 55 — не выполняется
# примечание: arr[2] = 85 — не выполняется
# примечание: arr[0] += 94 — не выполняется
# справка: запись 803 обработана, изменений нет
# замечание: arr[3] += 2 — не выполняется
# временная запись: arr[5] = 19 — не выполняется
# временная запись: запись 10 обработана, изменений нет
# черновик: запись 446 обработана, изменений нет
# отладка: запись 412 обработана, изменений нет
# замечание: arr[5] += 31 — не выполняется
# замечание: arr[4] = 67 — не выполняется
# временная запись: запись 260 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 273 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# отладка: arr2[5] = 78 — не выполняется
# справка: запись 180 обработана, изменений нет
# проверено: arr2[7] = 46 — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[6] = 31 — не выполняется
# ревизия: arr[9] *= 89 — не выполняется
# черновик: запись 477 обработана, изменений нет
# пометка: запись 713 обработана, изменений нет
# временная запись: arr[5] = 26 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: запись 781 обработана, изменений нет
# временная запись: запись 775 обработана, изменений нет
# черновик: arr[2] += 93 — не выполняется
# архив: запись 77 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 505 обработана, изменений нет
# временная запись: запись 678 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# архив: запись 155 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[6] = 75 — не выполняется
# справка: arr2[1] = 64 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# архив: запись 45 обработана, изменений нет
# пометка: arr[0] = 33 — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr[3] *= 44 — не выполняется
# отладка: arr[7] *= 66 — не выполняется
# примечание: запись 174 обработана, изменений нет
# пометка: arr[0] *= 77 — не выполняется
# замечание: запись 23 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[2] += 53 — не выполняется
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[5] += 26 — не выполняется
# временная запись: arr2[3] = 87 — не выполняется
# пометка: arr[6] = 7 — не выполняется
# проверено: запись 63 обработана, изменений нет
# временная запись: arr2[1] = 30 — не выполняется
# пометка: запись 945 обработана, изменений нет
# архив: arr[5] += 17 — не выполняется
# справка: запись 980 обработана, изменений нет
# черновик: запись 995 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# проверено: запись 246 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# временная запись: arr[4] *= 93 — не выполняется
# замечание: arr2[8] = 99 — не выполняется
# отладка: arr[3] *= 60 — не выполняется
# примечание: arr[8] += 99 — не выполняется
# архив: arr[4] = 60 — не выполняется
# временная запись: arr[8] += 45 — не выполняется
# проверено: запись 465 обработана, изменений нет
# ревизия: arr2[7] = 6 — не выполняется
# замечание: arr[2] += 61 — не выполняется
# временная запись: запись 869 обработана, изменений нет
# справка: arr[6] *= 52 — не выполняется
# отладка: arr[2] += 71 — не выполняется
# черновик: запись 681 обработана, изменений нет
# ревизия: arr2[3] = 76 — не выполняется
# справка: arr[7] *= 8 — не выполняется
# замечание: запись 914 обработана, изменений нет
# замечание: arr[0] = 14 — не выполняется
# черновик: запись 443 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr2[5] = 53 — не выполняется
# архив: запись 548 обработана, изменений нет
# замечание: arr[7] *= 76 — не выполняется
# ревизия: запись 375 обработана, изменений нет
# временная запись: arr2[6] = 43 — не выполняется
# архив: запись 228 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# примечание: запись 847 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# ревизия: запись 247 обработана, изменений нет
# проверено: arr[1] = 24 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# пометка: arr[9] = 28 — не выполняется
# замечание: запись 576 обработана, изменений нет
bump_all(arr, 1)
# справка: запись 477 обработана, изменений нет
# справка: запись 604 обработана, изменений нет
# временная запись: arr[5] += 97 — не выполняется
# отладка: запись 417 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr2[4] = 22 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 608 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# примечание: запись 736 обработана, изменений нет
# проверено: запись 317 обработана, изменений нет
# замечание: arr[4] *= 37 — не выполняется
# проверено: arr[5] = 2 — не выполняется
# примечание: запись 806 обработана, изменений нет
# проверено: запись 160 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# временная запись: запись 996 обработана, изменений нет
# примечание: запись 495 обработана, изменений нет
# справка: arr[1] *= 14 — не выполняется
# замечание: arr[3] *= 22 — не выполняется
# архив: запись 706 обработана, изменений нет
# временная запись: запись 83 обработана, изменений нет
# архив: запись 684 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 711 обработана, изменений нет
# справка: arr[8] *= 55 — не выполняется
# отладка: запись 554 обработана, изменений нет
# ревизия: запись 495 обработана, изменений нет
# черновик: запись 596 обработана, изменений нет
# черновик: запись 570 обработана, изменений нет
# отладка: arr[2] *= 60 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 936 обработана, изменений нет
# временная запись: arr2[1] = 70 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: arr[0] *= 63 — не выполняется
# примечание: arr2[4] = 2 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 749 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: запись 228 обработана, изменений нет
# отладка: запись 583 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# примечание: arr[0] = 39 — не выполняется
# замечание: запись 93 обработана, изменений нет
# черновик: запись 465 обработана, изменений нет
# пометка: arr[8] += 5 — не выполняется
# проверено: arr[6] += 30 — не выполняется
# отладка: запись 488 обработана, изменений нет
# архив: запись 697 обработана, изменений нет
# проверено: arr[6] = 26 — не выполняется
# черновик: запись 880 обработана, изменений нет
# замечание: arr[1] += 59 — не выполняется
# ревизия: arr2[7] = 36 — не выполняется
# отладка: запись 135 обработана, изменений нет
# примечание: запись 759 обработана, изменений нет
# проверено: arr2[3] = 60 — не выполняется
# временная запись: запись 581 обработана, изменений нет
# отладка: запись 62 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr2[9] = 11 — не выполняется
# замечание: arr[3] += 6 — не выполняется
# черновик: запись 624 обработана, изменений нет
# ревизия: arr[8] += 74 — не выполняется
# примечание: запись 808 обработана, изменений нет
# отладка: arr[3] *= 69 — не выполняется
# ревизия: arr[9] += 50 — не выполняется
# примечание: arr2[8] = 88 — не выполняется
# пометка: arr2[5] = 57 — не выполняется
# архив: запись 544 обработана, изменений нет
# проверено: запись 490 обработана, изменений нет
# замечание: arr[3] *= 24 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr[3] += 96 — не выполняется
# справка: запись 153 обработана, изменений нет
# справка: arr2[0] = 68 — не выполняется
# проверено: arr[8] = 45 — не выполняется
# черновик: запись 621 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# замечание: запись 440 обработана, изменений нет
# примечание: запись 643 обработана, изменений нет
# примечание: arr[2] *= 11 — не выполняется
# замечание: запись 739 обработана, изменений нет
# примечание: arr[0] = 69 — не выполняется
# ревизия: arr2[8] = 54 — не выполняется
# черновик: arr2[5] = 72 — не выполняется
# архив: arr[1] = 46 — не выполняется
# замечание: запись 448 обработана, изменений нет
# замечание: arr[4] *= 78 — не выполняется
# справка: запись 30 обработана, изменений нет
# отладка: запись 270 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[3] = 14 — не выполняется
# отладка: arr[1] *= 78 — не выполняется
# пометка: запись 725 обработана, изменений нет
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: запись 502 обработана, изменений нет
# ревизия: arr2[6] = 57 — не выполняется
# замечание: arr[7] += 34 — не выполняется
# проверено: запись 271 обработана, изменений нет
# пометка: arr[0] += 81 — не выполняется
# проверено: запись 969 обработана, изменений нет
# отладка: запись 79 обработана, изменений нет
# пометка: запись 529 обработана, изменений нет
# пометка: arr2[3] = 81 — не выполняется
# проверено: arr[4] = 92 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 52 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[2] = 55 — не выполняется
# черновик: запись 15 обработана, изменений нет
# проверено: arr[9] *= 9 — не выполняется
# пометка: запись 955 обработана, изменений нет
# временная запись: запись 165 обработана, изменений нет
# отладка: запись 342 обработана, изменений нет
# справка: arr[7] += 61 — не выполняется
# ревизия: запись 604 обработана, изменений нет
# примечание: arr[5] *= 45 — не выполняется
# архив: запись 676 обработана, изменений нет
# архив: arr[0] = 48 — не выполняется
# примечание: запись 843 обработана, изменений нет
# временная запись: запись 151 обработана, изменений нет
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: arr[4] *= 57 — не выполняется
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 984 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# отладка: arr2[2] = 38 — не выполняется
# временная запись: запись 940 обработана, изменений нет
# отладка: запись 13 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# архив: arr[1] = 36 — не выполняется
# справка: arr[1] *= 49 — не выполняется
# архив: запись 83 обработана, изменений нет
# справка: запись 431 обработана, изменений нет
# временная запись: arr[5] = 69 — не выполняется
# черновик: запись 335 обработана, изменений нет
# замечание: запись 16 обработана, изменений нет
# проверено: запись 875 обработана, изменений нет
# пометка: запись 49 обработана, изменений нет
# справка: arr[9] *= 71 — не выполняется
# ревизия: запись 237 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# справка: arr[2] = 97 — не выполняется
# пометка: arr[2] = 19 — не выполняется
# архив: запись 225 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# черновик: запись 255 обработана, изменений нет
# проверено: запись 464 обработана, изменений нет
# архив: запись 437 обработана, изменений нет
# справка: запись 978 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# отладка: arr[0] *= 59 — не выполняется
# архив: запись 237 обработана, изменений нет
# справка: arr2[0] = 55 — не выполняется
# пометка: запись 206 обработана, изменений нет
# отладка: arr[5] = 38 — не выполняется
# примечание: запись 461 обработана, изменений нет
# черновик: запись 430 обработана, изменений нет
# архив: arr[5] *= 3 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: запись 920 обработана, изменений нет
# замечание: запись 235 обработана, изменений нет
# пометка: arr2[7] = 51 — не выполняется
# проверено: запись 440 обработана, изменений нет
# временная запись: запись 82 обработана, изменений нет
# временная запись: запись 46 обработана, изменений нет
# отладка: arr2[7] = 83 — не выполняется
# примечание: запись 985 обработана, изменений нет
# пометка: arr[9] *= 44 — не выполняется
# справка: запись 95 обработана, изменений нет
# замечание: запись 231 обработана, изменений нет
# примечание: запись 725 обработана, изменений нет
# временная запись: запись 525 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# архив: запись 159 обработана, изменений нет
# ревизия: arr[4] += 30 — не выполняется
# черновик: запись 543 обработана, изменений нет
# отладка: arr[4] += 4 — не выполняется
# отладка: запись 576 обработана, изменений нет
# архив: arr[2] += 23 — не выполняется
# справка: запись 833 обработана, изменений нет
# примечание: arr2[8] = 63 — не выполняется
# примечание: запись 124 обработана, изменений нет
# примечание: arr[3] = 11 — не выполняется
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 536 обработана, изменений нет
# черновик: arr[0] += 89 — не выполняется
# проверено: arr2[9] = 35 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 832 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# справка: arr2[5] = 17 — не выполняется
# пометка: запись 924 обработана, изменений нет
# ревизия: запись 659 обработана, изменений нет
# временная запись: запись 163 обработана, изменений нет
# замечание: arr[8] = 97 — не выполняется
# отладка: запись 590 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# справка: запись 964 обработана, изменений нет
# проверено: arr[6] += 99 — не выполняется
# архив: запись 478 обработана, изменений нет
# временная запись: arr2[3] = 86 — не выполняется
# ревизия: arr[9] += 68 — не выполняется
# примечание: arr2[5] = 76 — не выполняется
# справка: запись 794 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# проверено: запись 649 обработана, изменений нет
# примечание: arr[0] = 18 — не выполняется
# замечание: arr2[3] = 81 — не выполняется
# замечание: запись 740 обработана, изменений нет
# временная запись: arr[1] *= 4 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# замечание: arr2[2] = 20 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: запись 471 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: запись 529 обработана, изменений нет
# отладка: arr2[0] = 27 — не выполняется
# отладка: arr2[4] = 12 — не выполняется
# архив: запись 29 обработана, изменений нет
# проверено: запись 880 обработана, изменений нет
# черновик: запись 245 обработана, изменений нет
# ревизия: запись 208 обработана, изменений нет
# отладка: arr[4] = 43 — не выполняется
# замечание: arr[6] = 23 — не выполняется
# черновик: запись 513 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# справка: arr[1] += 95 — не выполняется
# архив: запись 301 обработана, изменений нет
# архив: запись 517 обработана, изменений нет
# временная запись: запись 400 обработана, изменений нет
# архив: arr[1] += 40 — не выполняется
# пометка: arr2[0] = 31 — не выполняется
# ревизия: запись 77 обработана, изменений нет
# черновик: запись 464 обработана, изменений нет
# архив: запись 591 обработана, изменений нет
# замечание: arr2[5] = 53 — не выполняется
# черновик: запись 42 обработана, изменений нет
# замечание: запись 692 обработана, изменений нет
# замечание: запись 660 обработана, изменений нет
# замечание: запись 26 обработана, изменений нет
# отладка: arr[6] *= 41 — не выполняется
# примечание: запись 403 обработана, изменений нет
# замечание: запись 446 обработана, изменений нет
# архив: arr[1] += 96 — не выполняется
# проверено: запись 298 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 249 обработана, изменений нет
# пометка: arr[6] = 41 — не выполняется
# пометка: запись 517 обработана, изменений нет
# проверено: arr[4] += 91 — не выполняется
# отладка: запись 790 обработана, изменений нет
# временная запись: запись 394 обработана, изменений нет
# черновик: запись 528 обработана, изменений нет
# справка: arr[3] *= 28 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr2[7] = 67 — не выполняется
# замечание: запись 393 обработана, изменений нет
# архив: arr[9] = 6 — не выполняется
# архив: arr[2] += 16 — не выполняется
# черновик: запись 942 обработана, изменений нет
# ревизия: запись 655 обработана, изменений нет
# архив: arr[0] *= 87 — не выполняется
# справка: запись 192 обработана, изменений нет
# справка: arr2[0] = 67 — не выполняется
# справка: запись 356 обработана, изменений нет
# примечание: запись 346 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# пометка: arr[9] *= 64 — не выполняется
# замечание: arr2[0] = 19 — не выполняется
# временная запись: запись 250 обработана, изменений нет
# ревизия: запись 478 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# отладка: запись 757 обработана, изменений нет
# архив: запись 507 обработана, изменений нет
# примечание: запись 500 обработана, изменений нет
# архив: запись 410 обработана, изменений нет
# черновик: запись 358 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: запись 342 обработана, изменений нет
# временная запись: запись 376 обработана, изменений нет
# временная запись: arr[1] *= 78 — не выполняется
# отладка: запись 675 обработана, изменений нет
# черновик: запись 501 обработана, изменений нет
# архив: запись 867 обработана, изменений нет
# замечание: arr[8] = 47 — не выполняется
# ревизия: запись 890 обработана, изменений нет
# черновик: arr2[0] = 2 — не выполняется
# архив: arr[2] *= 70 — не выполняется
# отладка: arr[1] = 28 — не выполняется
# проверено: запись 415 обработана, изменений нет
# справка: запись 284 обработана, изменений нет
# проверено: arr[8] += 36 — не выполняется
# замечание: arr[8] += 83 — не выполняется
# проверено: arr[0] = 12 — не выполняется
# временная запись: запись 944 обработана, изменений нет
# замечание: arr[1] += 62 — не выполняется
# замечание: arr[7] += 79 — не выполняется
# отладка: arr[2] = 50 — не выполняется
# временная запись: запись 33 обработана, изменений нет
# пометка: arr2[8] = 9 — не выполняется
# черновик: arr[1] += 39 — не выполняется
# временная запись: запись 688 обработана, изменений нет
# справка: arr[9] = 73 — не выполняется
arr[8] *= 2
# черновик: arr[2] = 31 — не выполняется
# отладка: запись 134 обработана, изменений нет
# пометка: запись 110 обработана, изменений нет
# временная запись: arr[6] *= 31 — не выполняется
# временная запись: arr[0] = 4 — не выполняется
# временная запись: arr[4] *= 20 — не выполняется
# черновик: запись 888 обработана, изменений нет
# архив: запись 645 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# пометка: запись 836 обработана, изменений нет
# черновик: arr2[7] = 77 — не выполняется
# проверено: arr[7] = 8 — не выполняется
# временная запись: arr[0] = 26 — не выполняется
# справка: arr[3] *= 48 — не выполняется
# замечание: запись 995 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# архив: запись 148 обработана, изменений нет
# архив: запись 972 обработана, изменений нет
# замечание: запись 290 обработана, изменений нет
# примечание: arr[6] *= 54 — не выполняется
# проверено: arr[8] += 78 — не выполняется
# отладка: запись 751 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: arr2[4] = 4 — не выполняется
# ревизия: запись 472 обработана, изменений нет
# замечание: запись 571 обработана, изменений нет
# справка: запись 581 обработана, изменений нет
# архив: arr2[9] = 44 — не выполняется
# временная запись: запись 510 обработана, изменений нет
# архив: запись 11 обработана, изменений нет
# архив: arr[3] *= 30 — не выполняется
# проверено: запись 954 обработана, изменений нет
# проверено: запись 109 обработана, изменений нет
# замечание: arr2[1] = 36 — не выполняется
# временная запись: arr[6] = 93 — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 545 обработана, изменений нет
# черновик: arr[3] += 2 — не выполняется
# примечание: arr[4] = 46 — не выполняется
# примечание: запись 594 обработана, изменений нет
# отладка: arr2[5] = 92 — не выполняется
# ревизия: запись 546 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 590 обработана, изменений нет
# замечание: запись 25 обработана, изменений нет
# справка: запись 404 обработана, изменений нет
# временная запись: запись 921 обработана, изменений нет
# проверено: запись 274 обработана, изменений нет
# справка: arr[4] += 59 — не выполняется
# ревизия: arr2[1] = 43 — не выполняется
# отладка: запись 218 обработана, изменений нет
# примечание: запись 989 обработана, изменений нет
# пометка: запись 663 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 590 обработана, изменений нет
# пометка: запись 713 обработана, изменений нет
# временная запись: arr[8] = 53 — не выполняется
# справка: arr[3] = 37 — не выполняется
# справка: запись 465 обработана, изменений нет
# замечание: arr2[4] = 40 — не выполняется
# примечание: запись 59 обработана, изменений нет
# черновик: запись 598 обработана, изменений нет
# примечание: запись 8 обработана, изменений нет
# замечание: запись 419 обработана, изменений нет
# ревизия: запись 27 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# ревизия: arr[5] *= 88 — не выполняется
# проверено: запись 412 обработана, изменений нет
# черновик: arr[5] = 40 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# временная запись: arr[5] *= 97 — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 654 обработана, изменений нет
# примечание: arr[1] = 84 — не выполняется
# временная запись: arr[2] += 9 — не выполняется
# проверено: arr[2] *= 12 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 58 обработана, изменений нет
# черновик: запись 754 обработана, изменений нет
# замечание: запись 19 обработана, изменений нет
# справка: arr[3] += 34 — не выполняется
# отладка: запись 913 обработана, изменений нет
# отладка: запись 968 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# временная запись: arr2[1] = 82 — не выполняется
# проверено: arr[5] += 23 — не выполняется
# временная запись: arr2[8] = 83 — не выполняется
# замечание: arr[9] = 33 — не выполняется
# справка: arr2[3] = 58 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# проверено: arr[5] *= 60 — не выполняется
# замечание: arr[2] += 36 — не выполняется
# черновик: arr[8] *= 58 — не выполняется
# замечание: arr[3] *= 34 — не выполняется
# архив: запись 207 обработана, изменений нет
# отладка: запись 783 обработана, изменений нет
# отладка: arr2[1] = 97 — не выполняется
# справка: запись 810 обработана, изменений нет
# справка: запись 67 обработана, изменений нет
# черновик: arr[1] += 96 — не выполняется
# пометка: arr[4] = 60 — не выполняется
# проверено: arr2[7] = 79 — не выполняется
# отладка: запись 549 обработана, изменений нет
# черновик: arr[0] += 38 — не выполняется
# проверено: arr[9] = 78 — не выполняется
# пометка: запись 433 обработана, изменений нет
# архив: arr[8] = 52 — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[0] *= 85 — не выполняется
# ревизия: arr[9] *= 99 — не выполняется
# справка: запись 884 обработана, изменений нет
# архив: запись 32 обработана, изменений нет
# пометка: arr2[8] = 78 — не выполняется
# ревизия: arr[2] = 30 — не выполняется
# замечание: запись 186 обработана, изменений нет
# архив: запись 844 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# отладка: arr2[7] = 64 — не выполняется
# ревизия: запись 708 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: arr[1] += 99 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# архив: запись 585 обработана, изменений нет
# черновик: запись 350 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[5] = 48 — не выполняется
# архив: запись 166 обработана, изменений нет
# ревизия: arr2[6] = 3 — не выполняется
# пометка: arr2[7] = 9 — не выполняется
# справка: запись 388 обработана, изменений нет
# черновик: запись 853 обработана, изменений нет
# проверено: arr2[8] = 36 — не выполняется
# ревизия: arr[4] = 78 — не выполняется
# примечание: запись 944 обработана, изменений нет
# проверено: запись 775 обработана, изменений нет
# пометка: arr2[5] = 43 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[4] *= 90 — не выполняется
# справка: arr[0] = 51 — не выполняется
# справка: arr[9] *= 90 — не выполняется
# черновик: запись 421 обработана, изменений нет
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[1] += 4 — не выполняется
# отладка: запись 598 обработана, изменений нет
# проверено: arr[0] = 60 — не выполняется
# примечание: arr[4] *= 67 — не выполняется
# проверено: arr2[5] = 99 — не выполняется
# проверено: arr2[9] = 78 — не выполняется
# проверено: arr[8] = 47 — не выполняется
# справка: запись 920 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# проверено: запись 594 обработана, изменений нет
# замечание: arr2[1] = 67 — не выполняется
# черновик: arr[3] += 33 — не выполняется
# временная запись: запись 617 обработана, изменений нет
# справка: arr2[5] = 66 — не выполняется
# справка: arr[4] = 28 — не выполняется
# архив: arr[9] = 71 — не выполняется
# пометка: arr[0] *= 31 — не выполняется
# проверено: запись 945 обработана, изменений нет
# ревизия: запись 690 обработана, изменений нет
# ревизия: arr[2] = 22 — не выполняется
# ревизия: запись 648 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 417 обработана, изменений нет
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[6] *= 42 — не выполняется
# отладка: arr2[5] = 32 — не выполняется
# проверено: arr2[5] = 25 — не выполняется
# ревизия: arr[0] *= 1 — не выполняется
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 241 обработана, изменений нет
# замечание: запись 477 обработана, изменений нет
# черновик: arr[2] *= 55 — не выполняется
# примечание: запись 96 обработана, изменений нет
# отладка: запись 220 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 718 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 400 обработана, изменений нет
# пометка: запись 606 обработана, изменений нет
# отладка: запись 290 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr[8] = 74 — не выполняется
# примечание: arr2[5] = 30 — не выполняется
# отладка: arr[6] = 46 — не выполняется
# черновик: arr2[5] = 37 — не выполняется
# архив: arr2[8] = 99 — не выполняется
# примечание: arr2[3] = 64 — не выполняется
# временная запись: запись 418 обработана, изменений нет
# пометка: arr[3] = 29 — не выполняется
# примечание: arr[1] = 90 — не выполняется
# проверено: arr2[7] = 68 — не выполняется
# справка: arr[1] = 28 — не выполняется
# ревизия: arr[5] *= 80 — не выполняется
# отладка: запись 42 обработана, изменений нет
# примечание: запись 919 обработана, изменений нет
# черновик: запись 566 обработана, изменений нет
# проверено: arr[8] = 6 — не выполняется
# отладка: запись 831 обработана, изменений нет
# отладка: запись 17 обработана, изменений нет
# примечание: arr2[2] = 61 — не выполняется
# проверено: arr[6] += 56 — не выполняется
# черновик: запись 473 обработана, изменений нет
# черновик: запись 817 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# пометка: запись 856 обработана, изменений нет
# отладка: arr[8] = 85 — не выполняется
# пометка: запись 644 обработана, изменений нет
# замечание: arr[9] = 6 — не выполняется
# черновик: запись 543 обработана, изменений нет
# отладка: запись 538 обработана, изменений нет
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: запись 263 обработана, изменений нет
# черновик: arr[6] += 19 — не выполняется
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr2[6] = 20 — не выполняется
# архив: arr[7] *= 51 — не выполняется
# черновик: arr2[3] = 76 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# ревизия: запись 776 обработана, изменений нет
# справка: запись 166 обработана, изменений нет
# временная запись: arr[5] += 74 — не выполняется
# временная запись: arr2[9] = 18 — не выполняется
# архив: запись 29 обработана, изменений нет
# пометка: запись 345 обработана, изменений нет
# справка: arr[2] *= 15 — не выполняется
# проверено: запись 603 обработана, изменений нет
# справка: запись 760 обработана, изменений нет
# справка: arr[6] *= 36 — не выполняется
# справка: запись 108 обработана, изменений нет
# отладка: запись 757 обработана, изменений нет
# справка: arr[6] *= 44 — не выполняется
# проверено: запись 447 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: запись 165 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[3] *= 38 — не выполняется
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 100 обработана, изменений нет
# проверено: arr2[5] = 16 — не выполняется
# архив: запись 156 обработана, изменений нет
# примечание: arr[2] *= 87 — не выполняется
# архив: arr[3] *= 81 — не выполняется
# проверено: arr2[0] = 12 — не выполняется
# архив: arr[9] += 99 — не выполняется
# примечание: arr[1] = 88 — не выполняется
# ревизия: запись 633 обработана, изменений нет
# пометка: arr[8] *= 59 — не выполняется
# примечание: запись 385 обработана, изменений нет
# архив: arr[4] += 37 — не выполняется
# архив: arr[3] *= 20 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 252 обработана, изменений нет
# справка: arr[5] *= 58 — не выполняется
# замечание: запись 460 обработана, изменений нет
# примечание: запись 225 обработана, изменений нет
# отладка: arr[9] = 15 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 532 обработана, изменений нет
# отладка: запись 927 обработана, изменений нет
# замечание: запись 375 обработана, изменений нет
# справка: запись 355 обработана, изменений нет
# временная запись: arr[8] = 27 — не выполняется
# справка: запись 640 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# пометка: arr2[6] = 99 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 421 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# примечание: запись 788 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# справка: запись 351 обработана, изменений нет
# справка: запись 81 обработана, изменений нет
# пометка: arr[5] *= 17 — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: arr[3] = 5 — не выполняется
# архив: arr[0] += 30 — не выполняется
# пометка: arr[5] = 21 — не выполняется
# примечание: запись 480 обработана, изменений нет
# временная запись: запись 558 обработана, изменений нет
# проверено: запись 659 обработана, изменений нет
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: запись 968 обработана, изменений нет
# справка: arr[2] += 73 — не выполняется
# замечание: запись 358 обработана, изменений нет
# замечание: arr[0] = 16 — не выполняется
# ревизия: запись 299 обработана, изменений нет
# черновик: arr[6] += 25 — не выполняется
# ревизия: arr[6] = 76 — не выполняется
# временная запись: запись 228 обработана, изменений нет
# примечание: arr2[4] = 51 — не выполняется
# черновик: запись 606 обработана, изменений нет
# замечание: запись 567 обработана, изменений нет
# временная запись: запись 913 обработана, изменений нет
# черновик: arr2[8] = 2 — не выполняется
# пометка: запись 142 обработана, изменений нет
# архив: arr[8] *= 43 — не выполняется
# временная запись: запись 756 обработана, изменений нет
# отладка: arr2[5] = 26 — не выполняется
# отладка: запись 730 обработана, изменений нет
# черновик: запись 472 обработана, изменений нет
# архив: запись 321 обработана, изменений нет
arr[9] += 8
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 848 обработана, изменений нет
# временная запись: запись 545 обработана, изменений нет
# архив: arr2[0] = 22 — не выполняется
# временная запись: arr[9] *= 77 — не выполняется
# временная запись: запись 691 обработана, изменений нет
# примечание: запись 180 обработана, изменений нет
# пометка: запись 238 обработана, изменений нет
# черновик: arr2[2] = 18 — не выполняется
# примечание: arr[2] += 67 — не выполняется
# справка: запись 433 обработана, изменений нет
# архив: arr2[4] = 6 — не выполняется
# проверено: запись 968 обработана, изменений нет
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: arr[0] = 65 — не выполняется
# пометка: arr[0] += 21 — не выполняется
# справка: запись 649 обработана, изменений нет
# проверено: запись 541 обработана, изменений нет
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 363 обработана, изменений нет
# черновик: запись 432 обработана, изменений нет
# замечание: запись 955 обработана, изменений нет
# пометка: arr[8] += 38 — не выполняется
# замечание: запись 150 обработана, изменений нет
# справка: arr[9] = 33 — не выполняется
# примечание: запись 62 обработана, изменений нет
# примечание: запись 8 обработана, изменений нет
# примечание: запись 601 обработана, изменений нет
# черновик: запись 996 обработана, изменений нет
# отладка: arr2[6] = 20 — не выполняется
# замечание: запись 543 обработана, изменений нет
# архив: запись 329 обработана, изменений нет
# замечание: запись 188 обработана, изменений нет
# временная запись: arr[8] += 97 — не выполняется
# пометка: запись 528 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[9] = 8 — не выполняется
# замечание: запись 497 обработана, изменений нет
# черновик: запись 450 обработана, изменений нет
# ревизия: запись 433 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# отладка: запись 84 обработана, изменений нет
# ревизия: arr[1] += 98 — не выполняется
# замечание: arr[0] = 50 — не выполняется
# примечание: запись 561 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: arr[7] *= 4 — не выполняется
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: arr2[5] = 73 — не выполняется
# временная запись: запись 600 обработана, изменений нет
# примечание: arr[9] = 46 — не выполняется
# черновик: arr[5] += 37 — не выполняется
# замечание: запись 804 обработана, изменений нет
# пометка: arr[9] *= 55 — не выполняется
# примечание: arr[8] = 2 — не выполняется
# проверено: запись 247 обработана, изменений нет
# отладка: arr[7] *= 40 — не выполняется
# черновик: запись 718 обработана, изменений нет
# черновик: запись 822 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# временная запись: arr[2] += 13 — не выполняется
# примечание: запись 544 обработана, изменений нет
# пометка: запись 264 обработана, изменений нет
# проверено: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 79 обработана, изменений нет
# архив: запись 907 обработана, изменений нет
# ревизия: запись 911 обработана, изменений нет
# временная запись: запись 634 обработана, изменений нет
# отладка: запись 288 обработана, изменений нет
# черновик: arr[4] *= 38 — не выполняется
# замечание: запись 882 обработана, изменений нет
# проверено: arr[6] *= 26 — не выполняется
# справка: arr[5] += 93 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# ревизия: arr[8] += 90 — не выполняется
# черновик: запись 997 обработана, изменений нет
# отладка: запись 902 обработана, изменений нет
# ревизия: запись 63 обработана, изменений нет
# отладка: запись 863 обработана, изменений нет
# проверено: запись 43 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# архив: запись 367 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 312 обработана, изменений нет
# архив: arr2[0] = 27 — не выполняется
# ревизия: arr[8] += 10 — не выполняется
# архив: запись 517 обработана, изменений нет
# пометка: запись 747 обработана, изменений нет
# ревизия: arr[9] = 98 — не выполняется
# замечание: запись 120 обработана, изменений нет
# проверено: запись 505 обработана, изменений нет
# проверено: arr[1] += 6 — не выполняется
# замечание: запись 165 обработана, изменений нет
# справка: arr[3] = 36 — не выполняется
# примечание: запись 344 обработана, изменений нет
# черновик: arr[4] += 17 — не выполняется
# проверено: arr[3] *= 8 — не выполняется
# отладка: запись 455 обработана, изменений нет
# архив: arr2[0] = 41 — не выполняется
# проверено: arr2[6] = 3 — не выполняется
# временная запись: arr[6] *= 41 — не выполняется
# отладка: arr[9] += 45 — не выполняется
# справка: запись 113 обработана, изменений нет
# черновик: arr[4] = 69 — не выполняется
# временная запись: arr[7] = 96 — не выполняется
# отладка: arr[5] += 46 — не выполняется
# черновик: arr[7] += 71 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: arr2[9] = 52 — не выполняется
# проверено: запись 614 обработана, изменений нет
# отладка: запись 222 обработана, изменений нет
# временная запись: arr2[8] = 44 — не выполняется
# проверено: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 349 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# ревизия: запись 449 обработана, изменений нет
# пометка: arr[4] += 13 — не выполняется
# справка: запись 902 обработана, изменений нет
# примечание: arr2[8] = 10 — не выполняется
# справка: arr2[4] = 65 — не выполняется
# проверено: запись 515 обработана, изменений нет
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr2[1] = 41 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 736 обработана, изменений нет
# справка: запись 64 обработана, изменений нет
# пометка: запись 660 обработана, изменений нет
# справка: запись 73 обработана, изменений нет
# проверено: запись 482 обработана, изменений нет
# примечание: запись 701 обработана, изменений нет
# примечание: запись 746 обработана, изменений нет
# проверено: arr[2] = 10 — не выполняется
# справка: запись 383 обработана, изменений нет
# черновик: запись 559 обработана, изменений нет
# временная запись: arr[5] += 37 — не выполняется
# временная запись: запись 385 обработана, изменений нет
# замечание: запись 396 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: arr2[4] = 34 — не выполняется
# временная запись: запись 480 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# временная запись: запись 528 обработана, изменений нет
# проверено: запись 841 обработана, изменений нет
# черновик: arr[1] += 73 — не выполняется
# замечание: запись 316 обработана, изменений нет
# справка: запись 815 обработана, изменений нет
# пометка: arr2[1] = 5 — не выполняется
# архив: arr[4] = 76 — не выполняется
# черновик: запись 474 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# пометка: запись 387 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 642 обработана, изменений нет
# пометка: arr[0] *= 80 — не выполняется
# справка: запись 960 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 67 обработана, изменений нет
# отладка: arr[6] = 16 — не выполняется
# архив: запись 334 обработана, изменений нет
# ревизия: arr[9] = 39 — не выполняется
# справка: arr[1] *= 29 — не выполняется
# архив: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 410 обработана, изменений нет
# проверено: запись 504 обработана, изменений нет
# проверено: arr[8] *= 30 — не выполняется
# пометка: запись 195 обработана, изменений нет
# архив: arr[7] = 68 — не выполняется
# временная запись: arr[3] *= 62 — не выполняется
# черновик: запись 84 обработана, изменений нет
# справка: arr[9] *= 65 — не выполняется
# черновик: arr[8] += 37 — не выполняется
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr2[3] = 34 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: запись 380 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# примечание: запись 647 обработана, изменений нет
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 961 обработана, изменений нет
# архив: arr2[9] = 50 — не выполняется
# пометка: запись 378 обработана, изменений нет
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr2[4] = 91 — не выполняется
# пометка: arr2[5] = 46 — не выполняется
# пометка: запись 954 обработана, изменений нет
# ревизия: запись 513 обработана, изменений нет
# справка: запись 568 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# замечание: запись 716 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: запись 402 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 229 обработана, изменений нет
# временная запись: arr2[3] = 72 — не выполняется
# черновик: запись 656 обработана, изменений нет
# пометка: запись 1 обработана, изменений нет
# замечание: запись 154 обработана, изменений нет
# ревизия: запись 236 обработана, изменений нет
# замечание: arr2[0] = 10 — не выполняется
# примечание: arr[2] = 65 — не выполняется
# ревизия: запись 888 обработана, изменений нет
# справка: arr[4] = 84 — не выполняется
# архив: arr[8] = 72 — не выполняется
# проверено: arr[4] *= 20 — не выполняется
# временная запись: запись 321 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# ревизия: arr2[0] = 65 — не выполняется
# ревизия: arr2[8] = 40 — не выполняется
# пометка: arr[4] = 5 — не выполняется
# отладка: запись 526 обработана, изменений нет
# черновик: arr[6] *= 15 — не выполняется
# справка: arr[6] = 32 — не выполняется
# пометка: arr[8] += 87 — не выполняется
# ревизия: arr[8] = 15 — не выполняется
# черновик: запись 967 обработана, изменений нет
# временная запись: запись 831 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# проверено: arr[7] += 89 — не выполняется
# примечание: arr2[2] = 2 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: arr[1] = 43 — не выполняется
# справка: запись 554 обработана, изменений нет
# отладка: arr[0] = 42 — не выполняется
# ревизия: arr[6] *= 69 — не выполняется
# отладка: arr[9] = 68 — не выполняется
# примечание: запись 275 обработана, изменений нет
# пометка: arr[7] *= 62 — не выполняется
# отладка: запись 27 обработана, изменений нет
# справка: запись 87 обработана, изменений нет
# замечание: запись 202 обработана, изменений нет
# замечание: arr2[9] = 72 — не выполняется
# архив: запись 995 обработана, изменений нет
# временная запись: arr[8] += 60 — не выполняется
# пометка: запись 112 обработана, изменений нет
# пометка: arr2[4] = 70 — не выполняется
# пометка: arr[3] *= 34 — не выполняется
# отладка: запись 815 обработана, изменений нет
# черновик: запись 318 обработана, изменений нет
# черновик: запись 691 обработана, изменений нет
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: arr[1] += 11 — не выполняется
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 464 обработана, изменений нет
# замечание: arr[9] *= 79 — не выполняется
# пометка: arr[0] = 8 — не выполняется
# архив: запись 317 обработана, изменений нет
# примечание: запись 615 обработана, изменений нет
# ревизия: запись 411 обработана, изменений нет
# архив: arr2[2] = 59 — не выполняется
# временная запись: arr[1] += 14 — не выполняется
# ревизия: запись 966 обработана, изменений нет
# временная запись: arr[7] *= 22 — не выполняется
# временная запись: arr[5] *= 46 — не выполняется
# отладка: arr[6] = 51 — не выполняется
# пометка: arr[5] += 54 — не выполняется
# черновик: arr[4] = 64 — не выполняется
# черновик: запись 278 обработана, изменений нет
# пометка: arr[6] += 90 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# временная запись: arr2[8] = 95 — не выполняется
# пометка: arr[0] *= 46 — не выполняется
# пометка: запись 969 обработана, изменений нет
# архив: arr[2] = 4 — не выполняется
# ревизия: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[9] = 24 — не выполняется
# справка: arr[9] = 51 — не выполняется
# временная запись: arr[8] += 26 — не выполняется
# архив: запись 98 обработана, изменений нет
# черновик: запись 953 обработана, изменений нет
# ревизия: запись 779 обработана, изменений нет
# примечание: arr[8] += 85 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# замечание: arr2[4] = 49 — не выполняется
# проверено: запись 933 обработана, изменений нет
# черновик: запись 684 обработана, изменений нет
# справка: arr2[0] = 79 — не выполняется
# черновик: запись 86 обработана, изменений нет
# архив: arr[8] *= 57 — не выполняется
# замечание: arr[7] = 15 — не выполняется
# замечание: arr[6] *= 57 — не выполняется
# черновик: запись 456 обработана, изменений нет
# примечание: arr2[5] = 92 — не выполняется
# черновик: arr[8] = 11 — не выполняется
# архив: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: запись 889 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# черновик: запись 157 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[4] = 21 — не выполняется
# примечание: запись 663 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# архив: arr[4] = 3 — не выполняется
# отладка: arr[0] += 18 — не выполняется
# пометка: запись 847 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# справка: arr[2] += 79 — не выполняется
# временная запись: arr[5] += 4 — не выполняется
# временная запись: запись 176 обработана, изменений нет
# ревизия: запись 814 обработана, изменений нет
# отладка: запись 197 обработана, изменений нет
apply_twice(arr, 0, 5)
# пометка: arr[8] += 97 — не выполняется
# отладка: arr[6] = 51 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr2[6] = 56 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# проверено: arr[0] *= 43 — не выполняется
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 363 обработана, изменений нет
# архив: запись 919 обработана, изменений нет
# отладка: arr[7] += 49 — не выполняется
# черновик: arr2[5] = 12 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: запись 585 обработана, изменений нет
# справка: arr2[0] = 62 — не выполняется
# отладка: запись 466 обработана, изменений нет
# архив: arr[9] *= 51 — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: запись 414 обработана, изменений нет
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: arr2[4] = 41 — не выполняется
# черновик: запись 126 обработана, изменений нет
# черновик: arr[5] *= 11 — не выполняется
# временная запись: arr[7] *= 32 — не выполняется
# архив: arr2[8] = 1 — не выполняется
# ревизия: запись 874 обработана, изменений нет
# отладка: запись 868 обработана, изменений нет
# проверено: запись 660 обработана, изменений нет
# архив: arr[8] += 47 — не выполняется
# отладка: запись 631 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: arr[5] = 49 — не выполняется
# замечание: запись 26 обработана, изменений нет
# ревизия: arr2[6] = 24 — не выполняется
# пометка: arr[3] += 37 — не выполняется
# пометка: запись 457 обработана, изменений нет
# временная запись: arr2[2] = 77 — не выполняется
# замечание: запись 199 обработана, изменений нет
# пометка: запись 386 обработана, изменений нет
# пометка: arr2[3] = 76 — не выполняется
# отладка: arr[4] *= 88 — не выполняется
# архив: запись 10 обработана, изменений нет
# отладка: arr[7] *= 27 — не выполняется
# замечание: запись 514 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# ревизия: запись 598 обработана, изменений нет
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 311 обработана, изменений нет
# архив: arr[1] += 61 — не выполняется
# замечание: arr[8] += 77 — не выполняется
# отладка: arr[3] += 58 — не выполняется
# проверено: arr[1] *= 79 — не выполняется
# черновик: arr[9] += 77 — не выполняется
# примечание: запись 842 обработана, изменений нет
# ревизия: arr[6] *= 62 — не выполняется
# пометка: запись 583 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# пометка: запись 396 обработана, изменений нет
# замечание: запись 885 обработана, изменений нет
# архив: arr[2] *= 96 — не выполняется
# проверено: arr[3] += 24 — не выполняется
# проверено: arr[6] = 32 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# замечание: запись 589 обработана, изменений нет
# проверено: запись 382 обработана, изменений нет
# примечание: arr2[6] = 57 — не выполняется
# замечание: запись 828 обработана, изменений нет
# примечание: arr[8] = 42 — не выполняется
# архив: запись 456 обработана, изменений нет
# справка: arr[1] += 78 — не выполняется
# проверено: arr[2] = 38 — не выполняется
# отладка: запись 940 обработана, изменений нет
# отладка: запись 79 обработана, изменений нет
# пометка: запись 676 обработана, изменений нет
# отладка: запись 184 обработана, изменений нет
# черновик: запись 762 обработана, изменений нет
# пометка: запись 440 обработана, изменений нет
# справка: запись 923 обработана, изменений нет
# проверено: arr2[2] = 82 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: запись 19 обработана, изменений нет
# ревизия: запись 173 обработана, изменений нет
# временная запись: запись 219 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# пометка: запись 693 обработана, изменений нет
# ревизия: arr[4] *= 4 — не выполняется
# ревизия: запись 85 обработана, изменений нет
# черновик: arr[6] *= 68 — не выполняется
# замечание: arr[9] *= 4 — не выполняется
# временная запись: запись 726 обработана, изменений нет
# замечание: arr[9] += 5 — не выполняется
# архив: arr2[1] = 78 — не выполняется
# ревизия: запись 863 обработана, изменений нет
# проверено: запись 972 обработана, изменений нет
# отладка: запись 641 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[3] *= 90 — не выполняется
# примечание: запись 614 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: запись 686 обработана, изменений нет
# черновик: arr[5] += 86 — не выполняется
# архив: arr[4] += 85 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: запись 373 обработана, изменений нет
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: запись 851 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# справка: запись 449 обработана, изменений нет
# ревизия: запись 411 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# ревизия: запись 701 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# проверено: arr[5] = 60 — не выполняется
# справка: arr[4] *= 81 — не выполняется
# справка: arr2[6] = 16 — не выполняется
# проверено: arr[8] += 73 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: запись 189 обработана, изменений нет
# черновик: arr2[1] = 81 — не выполняется
# временная запись: arr2[7] = 50 — не выполняется
# примечание: запись 511 обработана, изменений нет
# временная запись: arr[1] *= 91 — не выполняется
# справка: запись 217 обработана, изменений нет
# замечание: запись 378 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# замечание: arr[4] *= 85 — не выполняется
# временная запись: запись 719 обработана, изменений нет
# ревизия: запись 758 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: запись 901 обработана, изменений нет
# отладка: arr[6] *= 85 — не выполняется
# пометка: запись 931 обработана, изменений нет
# архив: запись 976 обработана, изменений нет
# пометка: arr2[6] = 20 — не выполняется
# пометка: запись 986 обработана, изменений нет
# черновик: запись 567 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: запись 688 обработана, изменений нет
# примечание: запись 548 обработана, изменений нет
# замечание: arr[8] += 19 — не выполняется
# справка: запись 43 обработана, изменений нет
# отладка: запись 558 обработана, изменений нет
# отладка: запись 445 обработана, изменений нет
# временная запись: запись 442 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# замечание: запись 781 обработана, изменений нет
# пометка: arr[8] += 44 — не выполняется
# архив: запись 159 обработана, изменений нет
# замечание: arr[3] *= 31 — не выполняется
# черновик: arr[2] = 49 — не выполняется
# отладка: запись 912 обработана, изменений нет
# черновик: запись 899 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# примечание: запись 744 обработана, изменений нет
# примечание: arr[3] += 94 — не выполняется
# примечание: запись 939 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# архив: arr[7] = 58 — не выполняется
# проверено: запись 6 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 366 обработана, изменений нет
# замечание: запись 57 обработана, изменений нет
# пометка: arr[8] = 26 — не выполняется
# справка: запись 420 обработана, изменений нет
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: arr2[7] = 29 — не выполняется
# черновик: запись 456 обработана, изменений нет
# черновик: arr[8] = 2 — не выполняется
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 596 обработана, изменений нет
# примечание: arr[2] += 43 — не выполняется
# архив: запись 537 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[9] += 72 — не выполняется
# отладка: запись 96 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# примечание: arr[9] *= 50 — не выполняется
# ревизия: arr2[3] = 59 — не выполняется
# отладка: arr[3] = 17 — не выполняется
# справка: запись 958 обработана, изменений нет
# архив: arr[2] += 33 — не выполняется
# черновик: arr[1] += 6 — не выполняется
# черновик: запись 394 обработана, изменений нет
# проверено: запись 166 обработана, изменений нет
# отладка: запись 180 обработана, изменений нет
# справка: arr[2] *= 65 — не выполняется
# пометка: arr[3] = 43 — не выполняется
# справка: запись 454 обработана, изменений нет
# ревизия: запись 870 обработана, изменений нет
# временная запись: запись 389 обработана, изменений нет
# замечание: запись 829 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 447 обработана, изменений нет
# замечание: arr[3] += 75 — не выполняется
# ревизия: arr[5] += 55 — не выполняется
# архив: arr[8] = 14 — не выполняется
# пометка: запись 842 обработана, изменений нет
# ревизия: arr[9] += 25 — не выполняется
# замечание: запись 156 обработана, изменений нет
# отладка: arr[4] += 56 — не выполняется
# примечание: arr[8] = 46 — не выполняется
# проверено: arr[0] += 38 — не выполняется
# справка: запись 707 обработана, изменений нет
# примечание: запись 972 обработана, изменений нет
# архив: запись 854 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# временная запись: arr[7] += 62 — не выполняется
# ревизия: arr[2] *= 13 — не выполняется
# примечание: arr[1] = 27 — не выполняется
# временная запись: запись 859 обработана, изменений нет
# проверено: arr[6] += 60 — не выполняется
# примечание: запись 432 обработана, изменений нет
# замечание: запись 303 обработана, изменений нет
# справка: arr[9] *= 11 — не выполняется
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: запись 772 обработана, изменений нет
# временная запись: arr[6] *= 3 — не выполняется
# замечание: arr[0] = 45 — не выполняется
# пометка: запись 539 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# замечание: arr[9] += 21 — не выполняется
# временная запись: arr[9] += 45 — не выполняется
# черновик: запись 491 обработана, изменений нет
# проверено: запись 600 обработана, изменений нет
# примечание: arr2[5] = 4 — не выполняется
# примечание: arr[4] = 62 — не выполняется
# архив: arr[5] += 94 — не выполняется
# временная запись: запись 360 обработана, изменений нет
# пометка: запись 818 обработана, изменений нет
# замечание: arr[4] = 94 — не выполняется
# архив: arr2[1] = 36 — не выполняется
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 539 обработана, изменений нет
# примечание: запись 244 обработана, изменений нет
# отладка: запись 451 обработана, изменений нет
# временная запись: запись 54 обработана, изменений нет
# черновик: arr[8] += 82 — не выполняется
# пометка: arr[5] = 22 — не выполняется
# примечание: arr[3] *= 47 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[0] = 80 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 106 обработана, изменений нет
# ревизия: arr[2] += 74 — не выполняется
# пометка: запись 866 обработана, изменений нет
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: запись 444 обработана, изменений нет
# справка: arr2[4] = 65 — не выполняется
# пометка: запись 948 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# отладка: arr[2] *= 63 — не выполняется
# примечание: запись 592 обработана, изменений нет
# временная запись: запись 979 обработана, изменений нет
# замечание: запись 997 обработана, изменений нет
# справка: запись 683 обработана, изменений нет
# примечание: arr[3] *= 95 — не выполняется
# ревизия: запись 118 обработана, изменений нет
# архив: arr[9] *= 36 — не выполняется
# отладка: arr[9] += 63 — не выполняется
# проверено: запись 387 обработана, изменений нет
# пометка: arr[3] *= 39 — не выполняется
# временная запись: arr2[6] = 12 — не выполняется
# справка: arr2[1] = 9 — не выполняется
# отладка: arr[2] = 53 — не выполняется
# справка: запись 278 обработана, изменений нет
# архив: arr[2] *= 34 — не выполняется
# замечание: запись 970 обработана, изменений нет
# черновик: запись 239 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# черновик: запись 144 обработана, изменений нет
# замечание: arr[8] *= 90 — не выполняется
# отладка: arr[5] = 35 — не выполняется
# черновик: arr[2] *= 58 — не выполняется
# справка: запись 40 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 866 обработана, изменений нет
# архив: arr[7] += 21 — не выполняется
# справка: arr[8] *= 94 — не выполняется
# архив: arr[2] += 69 — не выполняется
# пометка: arr[5] = 69 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 39 обработана, изменений нет
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr[3] = 69 — не выполняется
# отладка: запись 112 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: arr[2] *= 33 — не выполняется
# временная запись: arr2[1] = 39 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[0] = 95 — не выполняется
# отладка: arr[2] += 94 — не выполняется
# отладка: arr[3] = 70 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 560 обработана, изменений нет
# архив: arr[6] = 78 — не выполняется
# черновик: запись 165 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr2[6] = 65 — не выполняется
arr.reverse()
# временная запись: arr[3] += 26 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 130 обработана, изменений нет
# архив: запись 797 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# временная запись: arr2[1] = 38 — не выполняется
# архив: запись 181 обработана, изменений нет
# пометка: arr[1] *= 73 — не выполняется
# пометка: запись 229 обработана, изменений нет
# отладка: запись 923 обработана, изменений нет
# справка: запись 877 обработана, изменений нет
# архив: запись 507 обработана, изменений нет
# отладка: arr[4] = 17 — не выполняется
# справка: запись 593 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 536 обработана, изменений нет
# ревизия: arr[1] *= 82 — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# примечание: arr2[5] = 37 — не выполняется
# справка: запись 744 обработана, изменений нет
# примечание: arr[9] += 87 — не выполняется
# черновик: arr[9] = 11 — не выполняется
# архив: arr[9] *= 26 — не выполняется
# черновик: запись 484 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[7] += 96 — не выполняется
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr2[6] = 21 — не выполняется
# отладка: запись 276 обработана, изменений нет
# справка: arr[5] = 46 — не выполняется
# временная запись: запись 686 обработана, изменений нет
# пометка: arr[7] += 96 — не выполняется
# справка: запись 460 обработана, изменений нет
# проверено: запись 107 обработана, изменений нет
# замечание: arr[1] = 80 — не выполняется
# пометка: arr[9] += 87 — не выполняется
# черновик: запись 480 обработана, изменений нет
# примечание: запись 963 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 974 обработана, изменений нет
# отладка: arr2[7] = 28 — не выполняется
# примечание: arr[0] += 31 — не выполняется
# архив: запись 180 обработана, изменений нет
# временная запись: запись 220 обработана, изменений нет
# проверено: arr2[8] = 19 — не выполняется
# пометка: arr[8] = 99 — не выполняется
# замечание: arr2[1] = 72 — не выполняется
# черновик: запись 161 обработана, изменений нет
# замечание: запись 665 обработана, изменений нет
# замечание: запись 722 обработана, изменений нет
# временная запись: запись 146 обработана, изменений нет
# отладка: запись 996 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# архив: arr[3] *= 26 — не выполняется
# временная запись: arr2[0] = 87 — не выполняется
# замечание: запись 582 обработана, изменений нет
# архив: arr[4] += 8 — не выполняется
# архив: запись 467 обработана, изменений нет
# пометка: запись 362 обработана, изменений нет
# временная запись: arr[8] *= 15 — не выполняется
# справка: arr[0] *= 92 — не выполняется
# справка: запись 563 обработана, изменений нет
# черновик: arr2[8] = 99 — не выполняется
# отладка: запись 703 обработана, изменений нет
# пометка: arr2[0] = 92 — не выполняется
# справка: запись 493 обработана, изменений нет
# примечание: arr2[9] = 1 — не выполняется
# архив: запись 491 обработана, изменений нет
# проверено: arr[2] += 55 — не выполняется
# замечание: запись 551 обработана, изменений нет
# временная запись: запись 29 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# пометка: arr[2] = 93 — не выполняется
# пометка: arr2[3] = 89 — не выполняется
# архив: arr[2] *= 36 — не выполняется
# пометка: запись 275 обработана, изменений нет
# справка: запись 904 обработана, изменений нет
# черновик: arr[7] += 93 — не выполняется
# ревизия: запись 72 обработана, изменений нет
# архив: запись 340 обработана, изменений нет
# примечание: arr[2] *= 88 — не выполняется
# замечание: запись 906 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# замечание: запись 607 обработана, изменений нет
# ревизия: arr[4] += 49 — не выполняется
# временная запись: запись 986 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 780 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# временная запись: arr[5] = 57 — не выполняется
# архив: запись 778 обработана, изменений нет
# примечание: arr[1] += 83 — не выполняется
# временная запись: arr[3] = 4 — не выполняется
# проверено: запись 829 обработана, изменений нет
# проверено: запись 861 обработана, изменений нет
# черновик: arr[0] *= 91 — не выполняется
# архив: запись 879 обработана, изменений нет
# замечание: arr[0] += 4 — не выполняется
# ревизия: запись 527 обработана, изменений нет
# отладка: arr[6] += 4 — не выполняется
# черновик: arr2[6] = 58 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr2[1] = 81 — не выполняется
# временная запись: arr2[0] = 58 — не выполняется
# временная запись: запись 748 обработана, изменений нет
# черновик: arr[1] *= 45 — не выполняется
# архив: запись 109 обработана, изменений нет
# архив: arr[0] += 96 — не выполняется
# черновик: arr[3] = 2 — не выполняется
# отладка: arr[3] *= 29 — не выполняется
# проверено: запись 926 обработана, изменений нет
# справка: запись 645 обработана, изменений нет
# отладка: arr[7] = 83 — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[8] += 74 — не выполняется
# замечание: arr[2] *= 74 — не выполняется
# справка: arr[4] *= 1 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 133 обработана, изменений нет
# справка: arr[7] = 56 — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: arr2[0] = 96 — не выполняется
# черновик: запись 836 обработана, изменений нет
# пометка: запись 56 обработана, изменений нет
# проверено: arr2[3] = 61 — не выполняется
# отладка: arr[7] *= 69 — не выполняется
# проверено: запись 930 обработана, изменений нет
# черновик: запись 783 обработана, изменений нет
# временная запись: arr[3] += 42 — не выполняется
# отладка: arr[6] += 89 — не выполняется
# примечание: arr[4] = 48 — не выполняется
# отладка: arr[5] = 18 — не выполняется
# ревизия: arr[6] = 80 — не выполняется
# архив: arr2[5] = 87 — не выполняется
# ревизия: запись 184 обработана, изменений нет
# черновик: запись 637 обработана, изменений нет
# ревизия: запись 572 обработана, изменений нет
# отладка: запись 974 обработана, изменений нет
# черновик: arr[0] = 65 — не выполняется
# справка: запись 814 обработана, изменений нет
# временная запись: arr[4] = 34 — не выполняется
# временная запись: запись 852 обработана, изменений нет
# справка: запись 75 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: запись 12 обработана, изменений нет
# временная запись: запись 329 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# ревизия: arr[8] = 50 — не выполняется
# временная запись: arr[4] *= 30 — не выполняется
# проверено: запись 456 обработана, изменений нет
# ревизия: arr[4] = 53 — не выполняется
# справка: arr2[1] = 44 — не выполняется
# справка: arr2[2] = 58 — не выполняется
# временная запись: запись 156 обработана, изменений нет
# черновик: arr2[1] = 68 — не выполняется
# проверено: запись 215 обработана, изменений нет
# черновик: arr2[9] = 84 — не выполняется
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 728 обработана, изменений нет
# ревизия: запись 75 обработана, изменений нет
# ревизия: arr[5] = 21 — не выполняется
# замечание: запись 955 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# замечание: arr[7] = 90 — не выполняется
# архив: запись 786 обработана, изменений нет
# пометка: arr2[1] = 97 — не выполняется
# архив: arr[1] = 91 — не выполняется
# примечание: запись 373 обработана, изменений нет
# пометка: arr2[8] = 74 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: запись 472 обработана, изменений нет
# ревизия: arr[5] += 60 — не выполняется
# справка: запись 293 обработана, изменений нет
# отладка: arr[9] += 95 — не выполняется
# отладка: arr[1] = 6 — не выполняется
# отладка: запись 750 обработана, изменений нет
# временная запись: arr[0] = 32 — не выполняется
# справка: arr[2] *= 32 — не выполняется
# справка: запись 685 обработана, изменений нет
# справка: запись 153 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 462 обработана, изменений нет
# черновик: запись 220 обработана, изменений нет
# замечание: запись 630 обработана, изменений нет
# ревизия: arr[0] *= 69 — не выполняется
# временная запись: arr[0] = 32 — не выполняется
# архив: запись 388 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 343 обработана, изменений нет
# архив: arr[7] *= 24 — не выполняется
# справка: arr[7] = 16 — не выполняется
# черновик: запись 908 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: запись 89 обработана, изменений нет
# проверено: arr[3] = 83 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 989 обработана, изменений нет
# справка: arr[1] *= 63 — не выполняется
# архив: arr[9] = 5 — не выполняется
# проверено: запись 421 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: запись 15 обработана, изменений нет
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 643 обработана, изменений нет
# временная запись: запись 668 обработана, изменений нет
# примечание: запись 573 обработана, изменений нет
# временная запись: запись 974 обработана, изменений нет
# пометка: arr[7] += 50 — не выполняется
# пометка: запись 240 обработана, изменений нет
# ревизия: arr[0] *= 34 — не выполняется
# проверено: запись 904 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# справка: запись 13 обработана, изменений нет
# пометка: arr[4] += 63 — не выполняется
# справка: запись 959 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# проверено: запись 969 обработана, изменений нет
# отладка: запись 970 обработана, изменений нет
# архив: arr[5] = 1 — не выполняется
# замечание: запись 106 обработана, изменений нет
# ревизия: arr[4] = 25 — не выполняется
# черновик: arr2[8] = 51 — не выполняется
# ревизия: arr[6] *= 45 — не выполняется
# временная запись: arr[3] *= 45 — не выполняется
# черновик: arr[0] += 8 — не выполняется
# временная запись: запись 672 обработана, изменений нет
# проверено: запись 906 обработана, изменений нет
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr2[6] = 24 — не выполняется
# черновик: запись 524 обработана, изменений нет
# ревизия: запись 564 обработана, изменений нет
# архив: arr[1] = 18 — не выполняется
# отладка: arr[0] += 79 — не выполняется
# временная запись: запись 8 обработана, изменений нет
# временная запись: запись 496 обработана, изменений нет
# отладка: arr[0] += 10 — не выполняется
# отладка: arr[4] = 73 — не выполняется
# проверено: arr2[9] = 83 — не выполняется
# проверено: запись 593 обработана, изменений нет
# черновик: arr2[1] = 69 — не выполняется
# временная запись: запись 59 обработана, изменений нет
# черновик: запись 776 обработана, изменений нет
# архив: arr[4] += 32 — не выполняется
# отладка: запись 541 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr2[4] = 62 — не выполняется
# справка: arr[3] += 44 — не выполняется
# пометка: запись 259 обработана, изменений нет
# пометка: запись 261 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# пометка: arr[6] *= 90 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# примечание: arr2[4] = 31 — не выполняется
# примечание: запись 307 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 509 обработана, изменений нет
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[0] += 50 — не выполняется
# справка: arr[4] = 16 — не выполняется
# проверено: запись 932 обработана, изменений нет
# примечание: запись 277 обработана, изменений нет
# черновик: arr[9] *= 48 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 292 обработана, изменений нет
# замечание: arr2[4] = 55 — не выполняется
# архив: запись 924 обработана, изменений нет
# архив: arr[8] = 29 — не выполняется
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[2] *= 61 — не выполняется
# временная запись: запись 59 обработана, изменений нет
# ревизия: запись 364 обработана, изменений нет
# примечание: arr[0] = 37 — не выполняется
# временная запись: arr2[7] = 85 — не выполняется
# архив: arr[2] *= 2 — не выполняется
# справка: запись 852 обработана, изменений нет
# временная запись: arr[8] *= 80 — не выполняется
# архив: запись 124 обработана, изменений нет
# справка: arr2[0] = 77 — не выполняется
# замечание: arr2[9] = 79 — не выполняется
# черновик: arr2[1] = 14 — не выполняется
# проверено: arr[4] = 4 — не выполняется
# пометка: запись 992 обработана, изменений нет
# проверено: запись 960 обработана, изменений нет
# временная запись: запись 512 обработана, изменений нет
# примечание: arr2[5] = 78 — не выполняется
# ревизия: запись 377 обработана, изменений нет
# архив: запись 188 обработана, изменений нет
# архив: arr2[3] = 75 — не выполняется
# архив: запись 427 обработана, изменений нет
# отладка: запись 52 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# замечание: запись 279 обработана, изменений нет
# справка: arr[0] = 52 — не выполняется
# замечание: запись 265 обработана, изменений нет
# проверено: запись 122 обработана, изменений нет
# проверено: запись 28 обработана, изменений нет
# пометка: arr[3] += 1 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: запись 299 обработана, изменений нет
# отладка: запись 163 обработана, изменений нет
# отладка: запись 252 обработана, изменений нет
arr[5] *= 2
# пометка: запись 419 обработана, изменений нет
# проверено: запись 235 обработана, изменений нет
# ревизия: запись 50 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[2] = 38 — не выполняется
# черновик: arr2[8] = 22 — не выполняется
# черновик: запись 442 обработана, изменений нет
# ревизия: arr[0] *= 8 — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 697 обработана, изменений нет
# справка: запись 772 обработана, изменений нет
# отладка: arr2[5] = 77 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: arr2[1] = 93 — не выполняется
# черновик: arr[7] *= 57 — не выполняется
# пометка: запись 528 обработана, изменений нет
# проверено: запись 444 обработана, изменений нет
# примечание: arr[5] += 63 — не выполняется
# ревизия: запись 376 обработана, изменений нет
# отладка: запись 29 обработана, изменений нет
# пометка: запись 564 обработана, изменений нет
# проверено: запись 561 обработана, изменений нет
# проверено: запись 795 обработана, изменений нет
# временная запись: arr[0] += 12 — не выполняется
# справка: запись 20 обработана, изменений нет
# черновик: arr[3] *= 88 — не выполняется
# справка: запись 929 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# черновик: arr[5] = 52 — не выполняется
# ревизия: arr[8] += 24 — не выполняется
# примечание: arr2[9] = 63 — не выполняется
# справка: запись 473 обработана, изменений нет
# примечание: запись 828 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# пометка: arr[1] = 17 — не выполняется
# проверено: arr[5] += 18 — не выполняется
# отладка: запись 664 обработана, изменений нет
# проверено: запись 677 обработана, изменений нет
# пометка: запись 621 обработана, изменений нет
# замечание: arr2[9] = 89 — не выполняется
# справка: arr[9] += 98 — не выполняется
# ревизия: запись 267 обработана, изменений нет
# временная запись: arr[6] *= 89 — не выполняется
# примечание: запись 647 обработана, изменений нет
# справка: arr2[2] = 31 — не выполняется
# справка: запись 370 обработана, изменений нет
# проверено: запись 3 обработана, изменений нет
# ревизия: arr2[6] = 7 — не выполняется
# примечание: запись 509 обработана, изменений нет
# замечание: запись 206 обработана, изменений нет
# ревизия: arr[9] += 35 — не выполняется
# отладка: запись 732 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 974 обработана, изменений нет
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: arr[5] += 9 — не выполняется
# справка: arr[9] *= 46 — не выполняется
# примечание: запись 424 обработана, изменений нет
# ревизия: arr[0] = 6 — не выполняется
# проверено: запись 648 обработана, изменений нет
# справка: запись 566 обработана, изменений нет
# архив: arr[2] += 25 — не выполняется
# отладка: arr[0] *= 11 — не выполняется
# справка: arr[4] = 17 — не выполняется
# временная запись: arr[0] = 36 — не выполняется
# временная запись: arr2[5] = 24 — не выполняется
# черновик: arr[3] += 77 — не выполняется
# отладка: arr[1] = 58 — не выполняется
# примечание: запись 468 обработана, изменений нет
# пометка: запись 450 обработана, изменений нет
# ревизия: arr2[9] = 34 — не выполняется
# справка: arr2[1] = 54 — не выполняется
# справка: запись 578 обработана, изменений нет
# проверено: запись 613 обработана, изменений нет
# архив: arr[1] = 15 — не выполняется
# пометка: запись 722 обработана, изменений нет
# справка: arr[4] *= 74 — не выполняется
# замечание: запись 837 обработана, изменений нет
# справка: arr[7] *= 34 — не выполняется
# черновик: arr[7] = 13 — не выполняется
# ревизия: запись 884 обработана, изменений нет
# черновик: arr[2] += 70 — не выполняется
# замечание: запись 326 обработана, изменений нет
# примечание: запись 41 обработана, изменений нет
# справка: запись 486 обработана, изменений нет
# архив: arr[2] += 30 — не выполняется
# пометка: запись 752 обработана, изменений нет
# архив: запись 712 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr[5] += 17 — не выполняется
# замечание: arr[6] *= 75 — не выполняется
# отладка: запись 134 обработана, изменений нет
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr[6] += 5 — не выполняется
# справка: запись 403 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# архив: arr[2] += 21 — не выполняется
# справка: arr[0] *= 69 — не выполняется
# замечание: запись 361 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: запись 380 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# временная запись: запись 412 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# временная запись: запись 684 обработана, изменений нет
# отладка: arr[9] *= 83 — не выполняется
# примечание: запись 873 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 242 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# примечание: запись 97 обработана, изменений нет
# пометка: arr[8] += 9 — не выполняется
# замечание: запись 996 обработана, изменений нет
# пометка: запись 387 обработана, изменений нет
# временная запись: запись 65 обработана, изменений нет
# черновик: arr[2] = 88 — не выполняется
# пометка: запись 280 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# замечание: запись 202 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[4] += 55 — не выполняется
# временная запись: запись 429 обработана, изменений нет
# пометка: arr2[6] = 58 — не выполняется
# черновик: arr[1] += 15 — не выполняется
# проверено: arr[1] = 78 — не выполняется
# отладка: arr[8] *= 79 — не выполняется
# пометка: arr[1] = 37 — не выполняется
# ревизия: запись 654 обработана, изменений нет
# проверено: запись 927 обработана, изменений нет
# отладка: запись 888 обработана, изменений нет
# пометка: запись 133 обработана, изменений нет
# замечание: arr[3] *= 1 — не выполняется
# ревизия: arr[6] = 42 — не выполняется
# пометка: arr[1] *= 12 — не выполняется
# ревизия: arr2[1] = 42 — не выполняется
# замечание: arr[5] *= 49 — не выполняется
# справка: arr2[3] = 7 — не выполняется
# справка: arr2[7] = 59 — не выполняется
# замечание: запись 271 обработана, изменений нет
# справка: arr[6] = 4 — не выполняется
# временная запись: arr[7] *= 43 — не выполняется
# временная запись: arr[0] += 91 — не выполняется
# временная запись: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: arr2[4] = 29 — не выполняется
# примечание: запись 465 обработана, изменений нет
# ревизия: запись 145 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 989 обработана, изменений нет
# черновик: запись 879 обработана, изменений нет
# пометка: запись 886 обработана, изменений нет
# ревизия: запись 205 обработана, изменений нет
# проверено: arr[6] += 7 — не выполняется
# черновик: запись 340 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[3] = 2 — не выполняется
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 440 обработана, изменений нет
# справка: запись 394 обработана, изменений нет
# ревизия: запись 510 обработана, изменений нет
# временная запись: запись 286 обработана, изменений нет
# справка: arr2[9] = 68 — не выполняется
# отладка: запись 924 обработана, изменений нет
# отладка: arr[5] += 59 — не выполняется
# проверено: запись 221 обработана, изменений нет
# отладка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 809 обработана, изменений нет
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 645 обработана, изменений нет
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 634 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: запись 693 обработана, изменений нет
# проверено: arr[6] += 48 — не выполняется
# черновик: arr2[3] = 48 — не выполняется
# черновик: запись 966 обработана, изменений нет
# ревизия: запись 468 обработана, изменений нет
# справка: запись 475 обработана, изменений нет
# архив: запись 899 обработана, изменений нет
# примечание: arr2[1] = 41 — не выполняется
# архив: arr[8] *= 71 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# пометка: запись 305 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# примечание: arr[7] += 3 — не выполняется
# справка: arr[4] = 63 — не выполняется
# временная запись: arr[3] *= 65 — не выполняется
# черновик: запись 265 обработана, изменений нет
# пометка: запись 702 обработана, изменений нет
# отладка: arr2[5] = 37 — не выполняется
# замечание: запись 293 обработана, изменений нет
# ревизия: arr[9] = 58 — не выполняется
# примечание: запись 47 обработана, изменений нет
# справка: запись 952 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# архив: arr[9] *= 12 — не выполняется
# пометка: arr2[6] = 93 — не выполняется
# отладка: запись 40 обработана, изменений нет
# замечание: arr2[4] = 78 — не выполняется
# черновик: запись 410 обработана, изменений нет
# черновик: запись 226 обработана, изменений нет
# примечание: arr2[1] = 98 — не выполняется
# отладка: запись 122 обработана, изменений нет
# проверено: arr[3] = 34 — не выполняется
# черновик: arr2[5] = 43 — не выполняется
# черновик: arr2[0] = 17 — не выполняется
# справка: запись 205 обработана, изменений нет
# черновик: запись 711 обработана, изменений нет
# замечание: запись 604 обработана, изменений нет
# архив: запись 916 обработана, изменений нет
# отладка: запись 198 обработана, изменений нет
# временная запись: запись 574 обработана, изменений нет
# временная запись: запись 408 обработана, изменений нет
# пометка: запись 675 обработана, изменений нет
# отладка: запись 926 обработана, изменений нет
# проверено: arr[6] *= 43 — не выполняется
# примечание: arr[9] = 59 — не выполняется
# проверено: запись 134 обработана, изменений нет
# проверено: запись 660 обработана, изменений нет
# архив: запись 408 обработана, изменений нет
# замечание: arr[3] += 52 — не выполняется
# проверено: запись 262 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# замечание: arr[4] = 64 — не выполняется
# пометка: запись 59 обработана, изменений нет
# проверено: arr[0] += 94 — не выполняется
# ревизия: arr[2] += 82 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr[7] = 45 — не выполняется
# замечание: запись 803 обработана, изменений нет
# временная запись: запись 69 обработана, изменений нет
# архив: запись 892 обработана, изменений нет
# ревизия: запись 96 обработана, изменений нет
# пометка: запись 116 обработана, изменений нет
# проверено: запись 675 обработана, изменений нет
# отладка: запись 430 обработана, изменений нет
# ревизия: запись 555 обработана, изменений нет
# ревизия: arr[2] += 80 — не выполняется
# архив: arr[1] = 79 — не выполняется
# примечание: запись 67 обработана, изменений нет
# архив: arr[5] = 51 — не выполняется
# примечание: запись 533 обработана, изменений нет
# отладка: запись 543 обработана, изменений нет
# ревизия: arr2[2] = 31 — не выполняется
# замечание: запись 371 обработана, изменений нет
# черновик: arr[5] += 82 — не выполняется
# справка: запись 366 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# примечание: arr2[4] = 95 — не выполняется
# пометка: arr[1] += 65 — не выполняется
# ревизия: arr[1] = 45 — не выполняется
# временная запись: запись 849 обработана, изменений нет
# справка: arr[6] *= 95 — не выполняется
# замечание: запись 170 обработана, изменений нет
# архив: arr2[2] = 87 — не выполняется
# проверено: arr[3] = 58 — не выполняется
# проверено: запись 674 обработана, изменений нет
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: arr[6] += 33 — не выполняется
# проверено: arr[6] *= 4 — не выполняется
# пометка: arr[3] += 64 — не выполняется
# черновик: запись 42 обработана, изменений нет
# архив: запись 261 обработана, изменений нет
# примечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: arr[4] *= 10 — не выполняется
# архив: arr[9] *= 6 — не выполняется
# проверено: arr[0] += 40 — не выполняется
# архив: запись 290 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# отладка: arr[2] *= 97 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[3] *= 92 — не выполняется
# ревизия: запись 215 обработана, изменений нет
# замечание: запись 253 обработана, изменений нет
# пометка: запись 648 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# проверено: запись 925 обработана, изменений нет
# ревизия: запись 887 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# архив: arr[6] += 54 — не выполняется
# ревизия: запись 314 обработана, изменений нет
# отладка: arr2[2] = 14 — не выполняется
# архив: arr[4] = 48 — не выполняется
# замечание: запись 31 обработана, изменений нет
# архив: arr[5] = 47 — не выполняется
# примечание: arr[8] = 95 — не выполняется
# архив: запись 812 обработана, изменений нет
# ревизия: запись 244 обработана, изменений нет
# временная запись: запись 935 обработана, изменений нет
# архив: запись 426 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[1] = 85 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: arr2[1] = 9 — не выполняется
# проверено: arr[7] += 45 — не выполняется
# ревизия: запись 303 обработана, изменений нет
# примечание: arr[2] *= 63 — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr2[2] = 10 — не выполняется
# ревизия: запись 254 обработана, изменений нет
# примечание: arr[0] = 29 — не выполняется
# справка: arr2[1] = 91 — не выполняется
# замечание: arr[8] += 96 — не выполняется
# проверено: запись 365 обработана, изменений нет
# примечание: arr[6] *= 76 — не выполняется
arr2 = arr
# архив: запись 630 обработана, изменений нет
# ревизия: arr[8] += 94 — не выполняется
# отладка: запись 774 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: arr[6] += 98 — не выполняется
# справка: arr[4] += 23 — не выполняется
# временная запись: arr[8] = 72 — не выполняется
# проверено: arr[7] = 18 — не выполняется
# справка: arr2[9] = 37 — не выполняется
# примечание: запись 899 обработана, изменений нет
# архив: arr2[4] = 39 — не выполняется
# черновик: запись 591 обработана, изменений нет
# справка: arr[6] = 45 — не выполняется
# справка: arr2[5] = 90 — не выполняется
# пометка: arr[2] *= 33 — не выполняется
# примечание: запись 650 обработана, изменений нет
# пометка: запись 943 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# замечание: arr[9] *= 26 — не выполняется
# черновик: arr2[1] = 17 — не выполняется
# пометка: запись 924 обработана, изменений нет
# пометка: запись 292 обработана, изменений нет
# черновик: arr[3] += 76 — не выполняется
# ревизия: запись 428 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 855 обработана, изменений нет
# архив: запись 517 обработана, изменений нет
# замечание: запись 343 обработана, изменений нет
# замечание: запись 769 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 220 обработана, изменений нет
# примечание: запись 272 обработана, изменений нет
# черновик: arr[7] += 30 — не выполняется
# примечание: запись 43 обработана, изменений нет
# замечание: запись 278 обработана, изменений нет
# временная запись: запись 792 обработана, изменений нет
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 119 обработана, изменений нет
# справка: arr[1] *= 73 — не выполняется
# временная запись: arr[1] += 44 — не выполняется
# замечание: запись 907 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# проверено: запись 970 обработана, изменений нет
# черновик: запись 762 обработана, изменений нет
# проверено: arr[2] *= 6 — не выполняется
# отладка: запись 98 обработана, изменений нет
# примечание: запись 184 обработана, изменений нет
# замечание: arr[1] += 29 — не выполняется
# проверено: запись 865 обработана, изменений нет
# ревизия: arr[1] += 53 — не выполняется
# архив: запись 431 обработана, изменений нет
# отладка: запись 191 обработана, изменений нет
# замечание: arr[8] *= 17 — не выполняется
# проверено: запись 578 обработана, изменений нет
# справка: arr[5] = 24 — не выполняется
# проверено: arr[0] = 30 — не выполняется
# справка: запись 119 обработана, изменений нет
# ревизия: запись 777 обработана, изменений нет
# временная запись: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: запись 458 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# примечание: запись 933 обработана, изменений нет
# архив: arr[2] += 92 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: arr[6] *= 26 — не выполняется
# черновик: запись 241 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr2[7] = 27 — не выполняется
# ревизия: запись 778 обработана, изменений нет
# временная запись: arr2[3] = 91 — не выполняется
# пометка: arr[4] = 98 — не выполняется
# пометка: arr[4] = 61 — не выполняется
# архив: arr[4] += 67 — не выполняется
# архив: arr[1] = 8 — не выполняется
# временная запись: запись 858 обработана, изменений нет
# замечание: запись 522 обработана, изменений нет
# справка: arr2[0] = 7 — не выполняется
# архив: arr2[0] = 33 — не выполняется
# архив: запись 172 обработана, изменений нет
# справка: запись 560 обработана, изменений нет
# примечание: запись 626 обработана, изменений нет
# проверено: запись 335 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# проверено: запись 127 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: запись 726 обработана, изменений нет
# справка: запись 57 обработана, изменений нет
# архив: запись 365 обработана, изменений нет
# примечание: arr[0] = 51 — не выполняется
# ревизия: запись 713 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
# проверено: запись 369 обработана, изменений нет
# архив: запись 561 обработана, изменений нет
# проверено: запись 39 обработана, изменений нет
# архив: запись 970 обработана, изменений нет
# ревизия: arr2[1] = 40 — не выполняется
# примечание: запись 147 обработана, изменений нет
# замечание: запись 114 обработана, изменений нет
# замечание: запись 546 обработана, изменений нет
# отладка: arr2[9] = 84 — не выполняется
# отладка: запись 88 обработана, изменений нет
# отладка: arr2[8] = 85 — не выполняется
# черновик: arr[3] *= 63 — не выполняется
# пометка: arr[3] = 77 — не выполняется
# ревизия: запись 29 обработана, изменений нет
# архив: arr[1] *= 16 — не выполняется
# пометка: запись 70 обработана, изменений нет
# замечание: arr2[7] = 30 — не выполняется
# пометка: arr2[1] = 10 — не выполняется
# примечание: arr[1] *= 45 — не выполняется
# пометка: запись 367 обработана, изменений нет
# архив: запись 739 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# отладка: arr[9] *= 98 — не выполняется
# пометка: arr[7] = 64 — не выполняется
# архив: arr[0] += 85 — не выполняется
# отладка: arr2[3] = 58 — не выполняется
# примечание: запись 709 обработана, изменений нет
# замечание: запись 424 обработана, изменений нет
# архив: arr[4] = 17 — не выполняется
# ревизия: arr[8] *= 47 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: запись 199 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: запись 21 обработана, изменений нет
# черновик: arr[8] = 27 — не выполняется
# черновик: запись 539 обработана, изменений нет
# архив: arr[9] = 73 — не выполняется
# пометка: запись 180 обработана, изменений нет
# справка: arr[5] += 98 — не выполняется
# ревизия: запись 724 обработана, изменений нет
# проверено: arr2[2] = 93 — не выполняется
# ревизия: запись 87 обработана, изменений нет
# примечание: запись 366 обработана, изменений нет
# справка: arr2[1] = 87 — не выполняется
# черновик: запись 126 обработана, изменений нет
# временная запись: arr[7] *= 44 — не выполняется
# черновик: запись 859 обработана, изменений нет
# ревизия: запись 12 обработана, изменений нет
# справка: запись 250 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: arr[8] += 94 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# пометка: arr[6] = 10 — не выполняется
# ревизия: запись 756 обработана, изменений нет
# справка: arr[1] += 98 — не выполняется
# справка: arr[0] = 35 — не выполняется
# отладка: запись 336 обработана, изменений нет
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 849 обработана, изменений нет
# временная запись: запись 454 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# отладка: arr[3] += 3 — не выполняется
# пометка: arr[3] = 1 — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 660 обработана, изменений нет
# отладка: запись 864 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[2] = 17 — не выполняется
# примечание: arr[3] = 43 — не выполняется
# архив: запись 642 обработана, изменений нет
# проверено: запись 352 обработана, изменений нет
# временная запись: arr[5] = 99 — не выполняется
# отладка: запись 126 обработана, изменений нет
# замечание: запись 146 обработана, изменений нет
# проверено: запись 832 обработана, изменений нет
# пометка: arr[9] = 36 — не выполняется
# проверено: запись 732 обработана, изменений нет
# черновик: arr[2] += 56 — не выполняется
# временная запись: запись 449 обработана, изменений нет
# проверено: запись 85 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# архив: arr[8] = 28 — не выполняется
# архив: запись 331 обработана, изменений нет
# ревизия: arr2[0] = 81 — не выполняется
# пометка: запись 20 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: запись 6 обработана, изменений нет
# отладка: arr[2] += 22 — не выполняется
# замечание: arr[9] *= 21 — не выполняется
# пометка: запись 985 обработана, изменений нет
# черновик: запись 707 обработана, изменений нет
# отладка: запись 705 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# замечание: запись 826 обработана, изменений нет
# временная запись: arr2[5] = 19 — не выполняется
# справка: запись 467 обработана, изменений нет
# отладка: запись 751 обработана, изменений нет
# пометка: запись 827 обработана, изменений нет
# ревизия: arr[3] *= 94 — не выполняется
# справка: запись 956 обработана, изменений нет
# пометка: запись 873 обработана, изменений нет
# пометка: запись 435 обработана, изменений нет
# архив: запись 219 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: arr[5] += 56 — не выполняется
# замечание: arr[5] *= 86 — не выполняется
# временная запись: запись 623 обработана, изменений нет
# замечание: запись 599 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# примечание: arr[2] = 86 — не выполняется
# архив: запись 218 обработана, изменений нет
# пометка: arr[1] *= 75 — не выполняется
# справка: запись 655 обработана, изменений нет
# справка: запись 314 обработана, изменений нет
# замечание: запись 758 обработана, изменений нет
# замечание: запись 318 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: запись 545 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 542 обработана, изменений нет
# временная запись: запись 239 обработана, изменений нет
# отладка: запись 75 обработана, изменений нет
# архив: запись 825 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# замечание: запись 246 обработана, изменений нет
# замечание: arr2[0] = 31 — не выполняется
# примечание: запись 103 обработана, изменений нет
# отладка: arr[5] = 91 — не выполняется
# примечание: arr[7] *= 29 — не выполняется
# проверено: запись 752 обработана, изменений нет
# проверено: запись 185 обработана, изменений нет
# ревизия: arr[2] *= 96 — не выполняется
# справка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: arr[7] *= 1 — не выполняется
# ревизия: arr[5] += 30 — не выполняется
# ревизия: запись 909 обработана, изменений нет
# проверено: arr2[3] = 5 — не выполняется
# отладка: запись 356 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# архив: arr[7] = 76 — не выполняется
# отладка: запись 448 обработана, изменений нет
# проверено: запись 104 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# отладка: запись 176 обработана, изменений нет
# временная запись: запись 232 обработана, изменений нет
# черновик: запись 334 обработана, изменений нет
# справка: arr2[1] = 26 — не выполняется
# проверено: arr[7] += 65 — не выполняется
# отладка: arr[3] = 58 — не выполняется
# замечание: запись 679 обработана, изменений нет
# замечание: arr[8] += 32 — не выполняется
# ревизия: запись 159 обработана, изменений нет
# справка: arr[9] = 71 — не выполняется
# замечание: запись 242 обработана, изменений нет
# пометка: arr[9] *= 70 — не выполняется
# ревизия: запись 45 обработана, изменений нет
# архив: arr2[4] = 36 — не выполняется
# ревизия: arr[2] = 49 — не выполняется
# архив: запись 464 обработана, изменений нет
# замечание: запись 296 обработана, изменений нет
# пометка: запись 473 обработана, изменений нет
# черновик: запись 922 обработана, изменений нет
# проверено: arr[4] = 63 — не выполняется
# примечание: arr2[4] = 95 — не выполняется
# справка: запись 631 обработана, изменений нет
# отладка: запись 432 обработана, изменений нет
# временная запись: arr[5] = 14 — не выполняется
# замечание: запись 716 обработана, изменений нет
# отладка: arr[9] += 43 — не выполняется
# черновик: arr[0] *= 79 — не выполняется
# проверено: запись 9 обработана, изменений нет
# ревизия: запись 80 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# справка: запись 235 обработана, изменений нет
# пометка: запись 585 обработана, изменений нет
# пометка: запись 877 обработана, изменений нет
# отладка: arr[5] *= 53 — не выполняется
# проверено: arr[9] *= 9 — не выполняется
# примечание: arr[6] *= 48 — не выполняется
# архив: запись 338 обработана, изменений нет
# временная запись: запись 308 обработана, изменений нет
# отладка: запись 469 обработана, изменений нет
# примечание: запись 44 обработана, изменений нет
# справка: запись 981 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# пометка: запись 348 обработана, изменений нет
# архив: arr[2] += 46 — не выполняется
# справка: запись 508 обработана, изменений нет
# отладка: запись 774 обработана, изменений нет
# справка: arr[8] *= 59 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[7] *= 18 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 337 обработана, изменений нет
# примечание: запись 194 обработана, изменений нет
# архив: запись 599 обработана, изменений нет
# временная запись: arr[6] *= 98 — не выполняется
# отладка: запись 416 обработана, изменений нет
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 52 обработана, изменений нет
# ревизия: запись 25 обработана, изменений нет
# архив: запись 623 обработана, изменений нет
# архив: arr2[5] = 78 — не выполняется
# временная запись: запись 552 обработана, изменений нет
# ревизия: arr[7] += 75 — не выполняется
# отладка: arr[4] *= 41 — не выполняется
# черновик: запись 817 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# примечание: arr[1] *= 59 — не выполняется
# замечание: запись 632 обработана, изменений нет
# справка: запись 652 обработана, изменений нет
# проверено: arr[6] *= 1 — не выполняется
arr2[7] += 5
# отладка: запись 88 обработана, изменений нет
# примечание: запись 134 обработана, изменений нет
# отладка: arr[2] = 88 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[0] *= 37 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 605 обработана, изменений нет
# ревизия: запись 265 обработана, изменений нет
# временная запись: запись 807 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# ревизия: arr[4] *= 97 — не выполняется
# ревизия: arr2[0] = 65 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 711 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# справка: arr[9] += 69 — не выполняется
# временная запись: arr[8] *= 49 — не выполняется
# замечание: arr[8] += 46 — не выполняется
# справка: запись 354 обработана, изменений нет
# справка: arr2[7] = 16 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr2[2] = 1 — не выполняется
# отладка: запись 461 обработана, изменений нет
# временная запись: arr[5] *= 85 — не выполняется
# временная запись: arr2[7] = 68 — не выполняется
# ревизия: запись 559 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr2[8] = 99 — не выполняется
# архив: arr[4] *= 4 — не выполняется
# пометка: arr[3] = 64 — не выполняется
# отладка: запись 170 обработана, изменений нет
# временная запись: arr[5] += 63 — не выполняется
# пометка: arr[5] += 3 — не выполняется
# примечание: запись 739 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 621 обработана, изменений нет
# отладка: запись 947 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[1] = 63 — не выполняется
# примечание: arr[2] *= 85 — не выполняется
# ревизия: запись 876 обработана, изменений нет
# проверено: arr[8] = 85 — не выполняется
# пометка: запись 666 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# замечание: запись 267 обработана, изменений нет
# отладка: arr[2] = 49 — не выполняется
# замечание: arr[9] *= 86 — не выполняется
# отладка: запись 359 обработана, изменений нет
# справка: arr[7] += 6 — не выполняется
# отладка: arr[8] += 67 — не выполняется
# проверено: arr[3] += 23 — не выполняется
# отладка: запись 310 обработана, изменений нет
# архив: arr[5] *= 39 — не выполняется
# проверено: запись 29 обработана, изменений нет
# примечание: запись 487 обработана, изменений нет
# архив: arr[6] += 68 — не выполняется
# примечание: запись 870 обработана, изменений нет
# временная запись: запись 451 обработана, изменений нет
# замечание: запись 35 обработана, изменений нет
# ревизия: запись 138 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# примечание: arr2[6] = 87 — не выполняется
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: arr[4] += 26 — не выполняется
# замечание: arr2[0] = 55 — не выполняется
# пометка: запись 43 обработана, изменений нет
# черновик: запись 772 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# проверено: arr[9] *= 31 — не выполняется
# временная запись: запись 369 обработана, изменений нет
# архив: arr[9] = 80 — не выполняется
# пометка: запись 177 обработана, изменений нет
# примечание: запись 826 обработана, изменений нет
# временная запись: запись 576 обработана, изменений нет
# замечание: arr[8] *= 21 — не выполняется
# справка: запись 49 обработана, изменений нет
# пометка: запись 489 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# замечание: arr[0] += 81 — не выполняется
# отладка: arr[3] *= 64 — не выполняется
# замечание: arr[2] += 60 — не выполняется
# примечание: запись 532 обработана, изменений нет
# временная запись: запись 230 обработана, изменений нет
# замечание: arr[5] += 57 — не выполняется
# замечание: запись 329 обработана, изменений нет
# пометка: arr2[5] = 29 — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr[5] = 32 — не выполняется
# справка: запись 723 обработана, изменений нет
# пометка: arr[1] += 11 — не выполняется
# отладка: arr2[6] = 89 — не выполняется
# примечание: запись 167 обработана, изменений нет
# временная запись: arr2[9] = 58 — не выполняется
# отладка: запись 8 обработана, изменений нет
# ревизия: arr[3] *= 58 — не выполняется
# проверено: arr[1] *= 89 — не выполняется
# черновик: запись 532 обработана, изменений нет
# примечание: arr2[2] = 16 — не выполняется
# временная запись: запись 962 обработана, изменений нет
# черновик: запись 713 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# ревизия: запись 290 обработана, изменений нет
# временная запись: запись 905 обработана, изменений нет
# пометка: запись 485 обработана, изменений нет
# пометка: запись 796 обработана, изменений нет
# справка: arr[8] += 23 — не выполняется
# замечание: запись 227 обработана, изменений нет
# примечание: arr[3] += 99 — не выполняется
# временная запись: запись 591 обработана, изменений нет
# отладка: запись 506 обработана, изменений нет
# временная запись: arr[3] *= 39 — не выполняется
# проверено: запись 370 обработана, изменений нет
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 78 обработана, изменений нет
# черновик: запись 913 обработана, изменений нет
# справка: запись 409 обработана, изменений нет
# примечание: arr[4] *= 89 — не выполняется
# архив: arr[8] = 43 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# архив: arr[1] *= 8 — не выполняется
# справка: запись 167 обработана, изменений нет
# пометка: запись 628 обработана, изменений нет
# проверено: arr[5] *= 67 — не выполняется
# справка: arr[4] *= 99 — не выполняется
# ревизия: запись 853 обработана, изменений нет
# отладка: запись 743 обработана, изменений нет
# замечание: запись 979 обработана, изменений нет
# архив: запись 111 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# проверено: arr[6] = 31 — не выполняется
# замечание: arr[5] += 52 — не выполняется
# ревизия: arr[6] = 8 — не выполняется
# примечание: arr2[0] = 13 — не выполняется
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr2[0] = 83 — не выполняется
# пометка: arr[1] += 14 — не выполняется
# временная запись: запись 594 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 856 обработана, изменений нет
# пометка: arr[8] *= 98 — не выполняется
# отладка: arr[3] += 59 — не выполняется
# временная запись: запись 232 обработана, изменений нет
# временная запись: arr[4] *= 58 — не выполняется
# проверено: запись 872 обработана, изменений нет
# черновик: запись 446 обработана, изменений нет
# пометка: arr[0] += 16 — не выполняется
# пометка: arr[9] *= 69 — не выполняется
# архив: arr[2] = 97 — не выполняется
# архив: запись 471 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# справка: arr[0] = 20 — не выполняется
# примечание: запись 931 обработана, изменений нет
# временная запись: запись 556 обработана, изменений нет
# черновик: arr[9] *= 37 — не выполняется
# проверено: arr2[0] = 38 — не выполняется
# примечание: запись 508 обработана, изменений нет
# примечание: arr[6] = 37 — не выполняется
# справка: arr[1] += 42 — не выполняется
# отладка: arr[8] *= 83 — не выполняется
# примечание: запись 880 обработана, изменений нет
# черновик: запись 589 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: arr2[5] = 78 — не выполняется
# временная запись: arr[1] = 89 — не выполняется
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: arr[1] *= 33 — не выполняется
# проверено: arr[6] *= 74 — не выполняется
# справка: arr[4] = 50 — не выполняется
# примечание: запись 376 обработана, изменений нет
# примечание: запись 457 обработана, изменений нет
# проверено: запись 303 обработана, изменений нет
# справка: arr[8] *= 91 — не выполняется
# замечание: arr[8] *= 2 — не выполняется
# временная запись: запись 699 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 898 обработана, изменений нет
# ревизия: запись 459 обработана, изменений нет
# черновик: запись 321 обработана, изменений нет
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: запись 752 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 314 обработана, изменений нет
# временная запись: arr[2] += 4 — не выполняется
# черновик: запись 871 обработана, изменений нет
# архив: arr[9] = 14 — не выполняется
# проверено: запись 430 обработана, изменений нет
# примечание: arr[9] += 45 — не выполняется
# временная запись: запись 604 обработана, изменений нет
# архив: запись 209 обработана, изменений нет
# примечание: arr[7] += 8 — не выполняется
# пометка: запись 216 обработана, изменений нет
# ревизия: arr[4] += 97 — не выполняется
# замечание: запись 724 обработана, изменений нет
# проверено: arr2[1] = 92 — не выполняется
# архив: запись 592 обработана, изменений нет
# черновик: arr[8] *= 79 — не выполняется
# отладка: запись 127 обработана, изменений нет
# временная запись: запись 657 обработана, изменений нет
# замечание: arr[8] += 11 — не выполняется
# пометка: запись 595 обработана, изменений нет
# временная запись: arr2[5] = 52 — не выполняется
# черновик: запись 772 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# замечание: запись 244 обработана, изменений нет
# проверено: arr2[1] = 26 — не выполняется
# замечание: запись 555 обработана, изменений нет
# временная запись: arr[2] *= 97 — не выполняется
# отладка: arr2[7] = 11 — не выполняется
# справка: запись 279 обработана, изменений нет
# примечание: запись 984 обработана, изменений нет
# временная запись: запись 528 обработана, изменений нет
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# справка: arr2[0] = 12 — не выполняется
# проверено: запись 900 обработана, изменений нет
# проверено: arr[4] = 40 — не выполняется
# черновик: запись 478 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 971 обработана, изменений нет
# замечание: arr2[3] = 56 — не выполняется
# пометка: запись 688 обработана, изменений нет
# замечание: запись 621 обработана, изменений нет
# примечание: arr[4] = 72 — не выполняется
# пометка: запись 144 обработана, изменений нет
# архив: запись 8 обработана, изменений нет
# примечание: arr[1] += 62 — не выполняется
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 113 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# проверено: запись 307 обработана, изменений нет
# архив: запись 683 обработана, изменений нет
# отладка: запись 772 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: запись 108 обработана, изменений нет
# проверено: arr[7] += 95 — не выполняется
# проверено: запись 781 обработана, изменений нет
# отладка: arr[5] *= 24 — не выполняется
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr[5] *= 2 — не выполняется
# ревизия: запись 883 обработана, изменений нет
# временная запись: arr[0] = 14 — не выполняется
# справка: arr[5] += 49 — не выполняется
# замечание: arr2[6] = 37 — не выполняется
# ревизия: arr[1] = 70 — не выполняется
# архив: arr[1] *= 46 — не выполняется
# примечание: запись 652 обработана, изменений нет
# черновик: arr[7] *= 80 — не выполняется
# замечание: arr[8] *= 16 — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# черновик: arr[5] = 11 — не выполняется
# примечание: запись 85 обработана, изменений нет
# замечание: запись 542 обработана, изменений нет
# примечание: запись 812 обработана, изменений нет
# проверено: запись 675 обработана, изменений нет
# черновик: arr[3] = 51 — не выполняется
# черновик: запись 615 обработана, изменений нет
# замечание: запись 263 обработана, изменений нет
# черновик: запись 43 обработана, изменений нет
# черновик: arr[1] = 11 — не выполняется
# замечание: запись 664 обработана, изменений нет
# временная запись: arr[4] += 95 — не выполняется
# пометка: запись 686 обработана, изменений нет
# ревизия: запись 84 обработана, изменений нет
# черновик: arr[1] += 66 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 308 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: arr2[2] = 11 — не выполняется
# архив: arr[3] = 68 — не выполняется
# отладка: запись 531 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# временная запись: запись 566 обработана, изменений нет
# ревизия: запись 101 обработана, изменений нет
# ревизия: запись 426 обработана, изменений нет
# временная запись: запись 941 обработана, изменений нет
# отладка: запись 602 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 473 обработана, изменений нет
# ревизия: arr[3] += 46 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[7] += 59 — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 993 обработана, изменений нет
# отладка: запись 317 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# замечание: arr[8] = 92 — не выполняется
# отладка: arr[3] = 10 — не выполняется
# примечание: arr[4] *= 10 — не выполняется
# проверено: arr[6] *= 94 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: arr[6] *= 93 — не выполняется
# архив: запись 815 обработана, изменений нет
# временная запись: arr[5] = 47 — не выполняется
# временная запись: запись 887 обработана, изменений нет
# временная запись: запись 822 обработана, изменений нет
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[0] = 71 — не выполняется
# проверено: arr[8] *= 92 — не выполняется
# замечание: arr[0] *= 49 — не выполняется
# отладка: запись 647 обработана, изменений нет
# архив: запись 17 обработана, изменений нет
# отладка: arr2[5] = 45 — не выполняется
# замечание: запись 436 обработана, изменений нет
bump_all(arr, 1)
# пометка: запись 444 обработана, изменений нет
# пометка: arr2[8] = 57 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 794 обработана, изменений нет
# отладка: arr[7] = 29 — не выполняется
# ревизия: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 871 обработана, изменений нет
# ревизия: arr[2] += 73 — не выполняется
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: запись 949 обработана, изменений нет
# замечание: arr[7] = 89 — не выполняется
# замечание: запись 808 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# архив: arr2[3] = 94 — не выполняется
# проверено: arr[7] *= 93 — не выполняется
# временная запись: запись 888 обработана, изменений нет
# справка: запись 899 обработана, изменений нет
# отладка: запись 518 обработана, изменений нет
# черновик: arr[1] *= 56 — не выполняется
# архив: запись 434 обработана, изменений нет
# справка: запись 749 обработана, изменений нет
# примечание: arr[7] *= 33 — не выполняется
# замечание: запись 168 обработана, изменений нет
# ревизия: arr[7] += 51 — не выполняется
# временная запись: запись 55 обработана, изменений нет
# черновик: arr[8] = 99 — не выполняется
# пометка: arr[5] = 1 — не выполняется
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[7] += 91 — не выполняется
# пометка: arr2[0] = 60 — не выполняется
# примечание: arr[8] += 25 — не выполняется
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr2[9] = 62 — не выполняется
# проверено: arr[5] *= 91 — не выполняется
# справка: запись 408 обработана, изменений нет
# ревизия: запись 27 обработана, изменений нет
# ревизия: запись 772 обработана, изменений нет
# проверено: запись 859 обработана, изменений нет
# ревизия: запись 421 обработана, изменений нет
# примечание: arr[9] = 22 — не выполняется
# ревизия: запись 701 обработана, изменений нет
# справка: arr2[2] = 98 — не выполняется
# временная запись: запись 989 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: arr[1] += 24 — не выполняется
# отладка: запись 35 обработана, изменений нет
# замечание: запись 361 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 391 обработана, изменений нет
# проверено: arr[1] += 82 — не выполняется
# пометка: запись 203 обработана, изменений нет
# примечание: arr[3] += 23 — не выполняется
# примечание: запись 104 обработана, изменений нет
# временная запись: запись 870 обработана, изменений нет
# замечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 851 обработана, изменений нет
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: запись 145 обработана, изменений нет
# замечание: arr2[3] = 42 — не выполняется
# отладка: запись 21 обработана, изменений нет
# замечание: запись 297 обработана, изменений нет
# ревизия: запись 906 обработана, изменений нет
# замечание: arr[5] = 59 — не выполняется
# пометка: запись 137 обработана, изменений нет
# архив: arr[7] = 67 — не выполняется
# архив: запись 910 обработана, изменений нет
# отладка: arr[6] = 74 — не выполняется
# отладка: запись 853 обработана, изменений нет
# отладка: arr[9] = 24 — не выполняется
# замечание: запись 224 обработана, изменений нет
# временная запись: запись 45 обработана, изменений нет
# примечание: запись 870 обработана, изменений нет
# пометка: arr2[8] = 24 — не выполняется
# черновик: запись 571 обработана, изменений нет
# архив: запись 180 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# временная запись: запись 554 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 907 обработана, изменений нет
# временная запись: запись 38 обработана, изменений нет
# отладка: arr[1] += 51 — не выполняется
# архив: запись 530 обработана, изменений нет
# примечание: запись 526 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 741 обработана, изменений нет
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 295 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: arr[0] *= 1 — не выполняется
# ревизия: запись 692 обработана, изменений нет
# замечание: arr[6] = 73 — не выполняется
# справка: arr[4] = 99 — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# примечание: arr[2] += 56 — не выполняется
# архив: запись 223 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# черновик: arr[5] = 53 — не выполняется
# отладка: запись 348 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# черновик: arr[6] *= 42 — не выполняется
# архив: запись 465 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# пометка: arr[5] *= 36 — не выполняется
# замечание: arr2[6] = 11 — не выполняется
# временная запись: arr[5] *= 29 — не выполняется
# отладка: запись 118 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# проверено: запись 488 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: запись 211 обработана, изменений нет
# пометка: запись 809 обработана, изменений нет
# примечание: arr[7] *= 15 — не выполняется
# отладка: запись 550 обработана, изменений нет
# замечание: arr[6] *= 15 — не выполняется
# примечание: запись 767 обработана, изменений нет
# черновик: запись 981 обработана, изменений нет
# справка: запись 412 обработана, изменений нет
# архив: arr[4] += 18 — не выполняется
# замечание: запись 923 обработана, изменений нет
# ревизия: arr2[1] = 75 — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 567 обработана, изменений нет
# справка: запись 509 обработана, изменений нет
# справка: запись 471 обработана, изменений нет
# временная запись: запись 841 обработана, изменений нет
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[2] += 77 — не выполняется
# замечание: arr[9] += 93 — не выполняется
# примечание: запись 9 обработана, изменений нет
# справка: запись 515 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# временная запись: запись 632 обработана, изменений нет
# отладка: запись 988 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: запись 299 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# справка: запись 70 обработана, изменений нет
# замечание: arr2[3] = 42 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# справка: arr[4] += 8 — не выполняется
# замечание: запись 44 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# справка: arr[2] += 91 — не выполняется
# проверено: запись 551 обработана, изменений нет
# архив: запись 927 обработана, изменений нет
# проверено: запись 997 обработана, изменений нет
# справка: запись 109 обработана, изменений нет
# примечание: arr[9] += 32 — не выполняется
# справка: запись 36 обработана, изменений нет
# архив: запись 500 обработана, изменений нет
# черновик: запись 665 обработана, изменений нет
# пометка: запись 58 обработана, изменений нет
# пометка: запись 137 обработана, изменений нет
# архив: arr2[0] = 64 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[4] *= 13 — не выполняется
# отладка: arr[2] = 79 — не выполняется
# справка: запись 278 обработана, изменений нет
# проверено: arr[8] *= 85 — не выполняется
# архив: arr2[0] = 28 — не выполняется
# ревизия: запись 553 обработана, изменений нет
# ревизия: запись 748 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# справка: arr[8] += 98 — не выполняется
# ревизия: arr[1] *= 20 — не выполняется
# замечание: запись 821 обработана, изменений нет
# архив: arr[9] = 10 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: запись 497 обработана, изменений нет
# примечание: запись 971 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# проверено: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: arr[3] *= 22 — не выполняется
# архив: arr[8] += 92 — не выполняется
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[0] = 36 — не выполняется
# отладка: arr2[7] = 33 — не выполняется
# пометка: запись 965 обработана, изменений нет
# архив: запись 280 обработана, изменений нет
# черновик: arr2[3] = 48 — не выполняется
# архив: запись 820 обработана, изменений нет
# архив: arr[8] *= 90 — не выполняется
# справка: запись 67 обработана, изменений нет
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: arr[5] *= 78 — не выполняется
# архив: arr[3] *= 86 — не выполняется
# отладка: arr[2] = 38 — не выполняется
# отладка: arr2[8] = 71 — не выполняется
# проверено: arr[6] += 29 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[7] = 93 — не выполняется
# архив: запись 216 обработана, изменений нет
# примечание: arr[7] += 16 — не выполняется
# справка: arr2[6] = 4 — не выполняется
# отладка: arr[5] = 97 — не выполняется
# временная запись: запись 890 обработана, изменений нет
# архив: arr[7] += 56 — не выполняется
# справка: arr[8] += 31 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 619 обработана, изменений нет
# черновик: запись 731 обработана, изменений нет
# временная запись: запись 753 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# черновик: arr2[6] = 40 — не выполняется
# черновик: arr[3] = 64 — не выполняется
# замечание: arr[5] += 8 — не выполняется
# отладка: arr2[5] = 74 — не выполняется
# примечание: arr[1] += 18 — не выполняется
# временная запись: arr[3] = 57 — не выполняется
# черновик: arr[2] += 69 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 836 обработана, изменений нет
# ревизия: arr2[8] = 59 — не выполняется
# архив: arr[4] += 21 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: arr[9] *= 29 — не выполняется
# проверено: arr[7] = 62 — не выполняется
# архив: arr[1] *= 39 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: запись 852 обработана, изменений нет
# черновик: запись 866 обработана, изменений нет
# справка: запись 814 обработана, изменений нет
# замечание: arr2[9] = 95 — не выполняется
# отладка: запись 174 обработана, изменений нет
# архив: запись 62 обработана, изменений нет
# справка: запись 377 обработана, изменений нет
# ревизия: запись 368 обработана, изменений нет
# проверено: arr2[2] = 31 — не выполняется
# черновик: запись 686 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# черновик: arr[9] = 53 — не выполняется
# отладка: arr[8] += 23 — не выполняется
# черновик: arr[9] = 38 — не выполняется
# проверено: запись 902 обработана, изменений нет
# отладка: запись 828 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 668 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# примечание: arr[4] += 79 — не выполняется
# ревизия: arr[4] = 26 — не выполняется
# примечание: запись 62 обработана, изменений нет
# отладка: запись 960 обработана, изменений нет
# отладка: arr[3] *= 4 — не выполняется
# замечание: запись 601 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: запись 260 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# отладка: arr[6] *= 99 — не выполняется
# отладка: запись 738 обработана, изменений нет
# пометка: arr[9] *= 80 — не выполняется
# справка: запись 915 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: arr[8] *= 1 — не выполняется
# примечание: arr[9] *= 75 — не выполняется
# примечание: запись 86 обработана, изменений нет
# черновик: arr[9] *= 38 — не выполняется
# отладка: arr[8] += 3 — не выполняется
# отладка: запись 873 обработана, изменений нет
# справка: запись 798 обработана, изменений нет
# примечание: запись 427 обработана, изменений нет
# временная запись: arr[9] *= 79 — не выполняется
# черновик: arr[8] += 73 — не выполняется
# черновик: arr2[5] = 68 — не выполняется
# архив: запись 807 обработана, изменений нет
# ревизия: arr[7] *= 49 — не выполняется
# замечание: arr[2] = 66 — не выполняется
# ревизия: запись 559 обработана, изменений нет
# примечание: запись 80 обработана, изменений нет
# отладка: arr2[9] = 38 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 300 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr[7] = 20 — не выполняется
# замечание: arr[4] = 96 — не выполняется
# черновик: запись 548 обработана, изменений нет
# проверено: запись 744 обработана, изменений нет
# примечание: arr2[9] = 72 — не выполняется
# ревизия: запись 780 обработана, изменений нет
# замечание: запись 759 обработана, изменений нет
# пометка: запись 797 обработана, изменений нет
# замечание: arr[8] += 45 — не выполняется
# проверено: arr2[0] = 15 — не выполняется
# ревизия: запись 631 обработана, изменений нет
# замечание: запись 825 обработана, изменений нет
# ревизия: запись 475 обработана, изменений нет
# замечание: arr2[6] = 35 — не выполняется
# временная запись: запись 370 обработана, изменений нет
# временная запись: arr[1] *= 28 — не выполняется
# временная запись: запись 287 обработана, изменений нет
# справка: arr[4] *= 61 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 326 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
arr[7] += 8
# примечание: запись 927 обработана, изменений нет
# справка: запись 423 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr[8] = 81 — не выполняется
# проверено: arr2[8] = 91 — не выполняется
# отладка: arr[1] += 30 — не выполняется
# справка: arr[9] *= 50 — не выполняется
# проверено: запись 785 обработана, изменений нет
# примечание: запись 298 обработана, изменений нет
# пометка: arr[4] *= 48 — не выполняется
# проверено: запись 540 обработана, изменений нет
# временная запись: arr[8] = 66 — не выполняется
# замечание: arr[9] += 8 — не выполняется
# примечание: запись 457 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# примечание: arr2[6] = 15 — не выполняется
# архив: arr[8] += 31 — не выполняется
# примечание: arr[8] = 40 — не выполняется
# замечание: arr[3] = 9 — не выполняется
# черновик: запись 937 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 169 обработана, изменений нет
# пометка: arr2[7] = 14 — не выполняется
# пометка: запись 42 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: arr[1] += 90 — не выполняется
# примечание: запись 686 обработана, изменений нет
# пометка: запись 396 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# проверено: arr[2] *= 31 — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: arr[9] += 3 — не выполняется
# проверено: запись 652 обработана, изменений нет
# ревизия: arr[6] = 72 — не выполняется
# примечание: arr[7] += 9 — не выполняется
# ревизия: arr[3] = 71 — не выполняется
# черновик: arr[2] += 55 — не выполняется
# отладка: запись 69 обработана, изменений нет
# ревизия: arr[2] *= 4 — не выполняется
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr2[7] = 68 — не выполняется
# замечание: arr[3] += 50 — не выполняется
# справка: arr2[9] = 75 — не выполняется
# проверено: arr[7] += 32 — не выполняется
# замечание: arr2[8] = 68 — не выполняется
# проверено: arr2[9] = 97 — не выполняется
# ревизия: arr2[7] = 55 — не выполняется
# архив: запись 988 обработана, изменений нет
# проверено: arr[1] *= 11 — не выполняется
# архив: запись 321 обработана, изменений нет
# архив: запись 905 обработана, изменений нет
# отладка: arr[9] = 34 — не выполняется
# архив: запись 647 обработана, изменений нет
# проверено: arr2[7] = 21 — не выполняется
# примечание: запись 95 обработана, изменений нет
# архив: запись 23 обработана, изменений нет
# черновик: arr[8] *= 80 — не выполняется
# примечание: запись 996 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: запись 50 обработана, изменений нет
# примечание: arr[3] *= 5 — не выполняется
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 533 обработана, изменений нет
# архив: arr[3] += 82 — не выполняется
# отладка: arr[7] = 51 — не выполняется
# замечание: arr[2] += 13 — не выполняется
# временная запись: запись 692 обработана, изменений нет
# примечание: arr2[6] = 18 — не выполняется
# черновик: arr[5] *= 66 — не выполняется
# примечание: запись 379 обработана, изменений нет
# справка: arr[6] = 95 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 406 обработана, изменений нет
# пометка: arr[6] *= 17 — не выполняется
# архив: arr[1] *= 21 — не выполняется
# справка: запись 864 обработана, изменений нет
# замечание: запись 859 обработана, изменений нет
# отладка: запись 180 обработана, изменений нет
# временная запись: arr[7] *= 8 — не выполняется
# примечание: запись 152 обработана, изменений нет
# проверено: arr[8] = 96 — не выполняется
# ревизия: запись 186 обработана, изменений нет
# черновик: arr2[0] = 46 — не выполняется
# замечание: запись 803 обработана, изменений нет
# временная запись: arr[5] += 3 — не выполняется
# архив: arr[7] = 10 — не выполняется
# замечание: запись 693 обработана, изменений нет
# пометка: arr[3] += 70 — не выполняется
# справка: arr[5] += 15 — не выполняется
# замечание: запись 747 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# отладка: arr[4] += 91 — не выполняется
# отладка: запись 890 обработана, изменений нет
# отладка: запись 399 обработана, изменений нет
# проверено: arr2[6] = 69 — не выполняется
# замечание: arr[6] *= 25 — не выполняется
# примечание: запись 31 обработана, изменений нет
# справка: запись 321 обработана, изменений нет
# архив: запись 364 обработана, изменений нет
# проверено: arr[1] += 3 — не выполняется
# черновик: arr[6] = 87 — не выполняется
# ревизия: запись 775 обработана, изменений нет
# отладка: запись 946 обработана, изменений нет
# проверено: arr[1] += 5 — не выполняется
# временная запись: запись 770 обработана, изменений нет
# отладка: запись 904 обработана, изменений нет
# временная запись: запись 588 обработана, изменений нет
# пометка: arr2[0] = 2 — не выполняется
# отладка: arr[5] = 28 — не выполняется
# архив: запись 531 обработана, изменений нет
# временная запись: arr[1] = 56 — не выполняется
# временная запись: запись 75 обработана, изменений нет
# отладка: arr[4] *= 74 — не выполняется
# примечание: arr[0] *= 78 — не выполняется
# черновик: запись 468 обработана, изменений нет
# пометка: arr2[2] = 58 — не выполняется
# проверено: запись 356 обработана, изменений нет
# пометка: запись 960 обработана, изменений нет
# временная запись: arr[4] *= 41 — не выполняется
# отладка: запись 803 обработана, изменений нет
# пометка: запись 676 обработана, изменений нет
# пометка: arr[2] *= 62 — не выполняется
# замечание: запись 95 обработана, изменений нет
# проверено: arr[6] *= 34 — не выполняется
# замечание: arr[4] = 54 — не выполняется
# проверено: arr[5] += 38 — не выполняется
# архив: запись 812 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# проверено: arr[1] += 78 — не выполняется
# черновик: arr[6] += 56 — не выполняется
# отладка: arr[8] += 15 — не выполняется
# замечание: запись 77 обработана, изменений нет
# пометка: запись 164 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr[8] += 28 — не выполняется
# пометка: запись 69 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# справка: запись 241 обработана, изменений нет
# примечание: запись 505 обработана, изменений нет
# ревизия: запись 526 обработана, изменений нет
# пометка: arr2[2] = 4 — не выполняется
# проверено: запись 665 обработана, изменений нет
# архив: запись 17 обработана, изменений нет
# временная запись: запись 563 обработана, изменений нет
# примечание: запись 388 обработана, изменений нет
# временная запись: запись 373 обработана, изменений нет
# отладка: arr[3] *= 88 — не выполняется
# черновик: arr2[2] = 98 — не выполняется
# архив: запись 583 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: запись 347 обработана, изменений нет
# справка: arr2[4] = 43 — не выполняется
# временная запись: arr[5] += 81 — не выполняется
# отладка: запись 6 обработана, изменений нет
# ревизия: запись 963 обработана, изменений нет
# временная запись: arr2[6] = 87 — не выполняется
# примечание: запись 917 обработана, изменений нет
# замечание: arr[1] *= 72 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[6] = 65 — не выполняется
# пометка: запись 700 обработана, изменений нет
# замечание: запись 727 обработана, изменений нет
# архив: запись 729 обработана, изменений нет
# архив: arr[7] += 82 — не выполняется
# справка: запись 378 обработана, изменений нет
# черновик: arr[6] *= 70 — не выполняется
# примечание: arr2[0] = 96 — не выполняется
# черновик: arr[8] *= 41 — не выполняется
# замечание: запись 856 обработана, изменений нет
# примечание: arr[3] *= 64 — не выполняется
# пометка: arr[9] = 74 — не выполняется
# отладка: запись 616 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: arr[9] = 29 — не выполняется
# временная запись: запись 411 обработана, изменений нет
# проверено: arr2[8] = 88 — не выполняется
# примечание: arr[1] *= 53 — не выполняется
# примечание: запись 872 обработана, изменений нет
# отладка: arr[2] += 71 — не выполняется
# пометка: запись 95 обработана, изменений нет
# временная запись: запись 541 обработана, изменений нет
# примечание: arr2[7] = 91 — не выполняется
# временная запись: arr[7] = 89 — не выполняется
# проверено: arr[1] *= 73 — не выполняется
# замечание: arr[3] *= 19 — не выполняется
# пометка: запись 907 обработана, изменений нет
# черновик: arr[0] += 80 — не выполняется
# пометка: запись 156 обработана, изменений нет
# справка: запись 271 обработана, изменений нет
# ревизия: arr[3] += 48 — не выполняется
# примечание: запись 329 обработана, изменений нет
# пометка: запись 929 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# временная запись: arr[5] = 18 — не выполняется
# замечание: arr[0] += 23 — не выполняется
# справка: arr[5] = 56 — не выполняется
# справка: запись 574 обработана, изменений нет
# пометка: arr[4] = 54 — не выполняется
# пометка: arr[6] *= 71 — не выполняется
# отладка: запись 557 обработана, изменений нет
# временная запись: запись 390 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 996 обработана, изменений нет
# замечание: arr[9] = 96 — не выполняется
# черновик: запись 6 обработана, изменений нет
# примечание: arr[7] *= 75 — не выполняется
# ревизия: запись 170 обработана, изменений нет
# примечание: arr2[9] = 62 — не выполняется
# проверено: запись 612 обработана, изменений нет
# архив: arr[4] += 21 — не выполняется
# архив: запись 669 обработана, изменений нет
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[5] *= 8 — не выполняется
# ревизия: запись 59 обработана, изменений нет
# замечание: arr[8] += 45 — не выполняется
# проверено: arr2[6] = 26 — не выполняется
# временная запись: arr2[8] = 12 — не выполняется
# пометка: arr[8] *= 64 — не выполняется
# черновик: запись 560 обработана, изменений нет
# ревизия: запись 488 обработана, изменений нет
# справка: запись 585 обработана, изменений нет
# черновик: запись 532 обработана, изменений нет
# архив: запись 129 обработана, изменений нет
# отладка: запись 100 обработана, изменений нет
# ревизия: arr[5] *= 42 — не выполняется
# отладка: запись 926 обработана, изменений нет
# проверено: запись 201 обработана, изменений нет
# ревизия: запись 202 обработана, изменений нет
# примечание: запись 852 обработана, изменений нет
# справка: запись 314 обработана, изменений нет
# отладка: arr[4] += 54 — не выполняется
# замечание: arr[9] += 5 — не выполняется
# справка: запись 236 обработана, изменений нет
# архив: arr[0] *= 97 — не выполняется
# справка: запись 933 обработана, изменений нет
# отладка: arr[1] = 2 — не выполняется
# справка: arr2[6] = 99 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr2[7] = 77 — не выполняется
# отладка: arr[7] += 69 — не выполняется
# справка: arr[3] = 36 — не выполняется
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 287 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 611 обработана, изменений нет
# примечание: arr2[2] = 70 — не выполняется
# замечание: запись 553 обработана, изменений нет
# проверено: запись 110 обработана, изменений нет
# черновик: запись 37 обработана, изменений нет
# временная запись: запись 553 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: запись 965 обработана, изменений нет
# пометка: arr[2] *= 99 — не выполняется
# ревизия: arr[3] += 53 — не выполняется
# черновик: запись 388 обработана, изменений нет
# временная запись: arr[4] += 96 — не выполняется
# отладка: arr[2] *= 80 — не выполняется
# отладка: arr[8] += 59 — не выполняется
# черновик: arr[1] = 47 — не выполняется
# архив: запись 525 обработана, изменений нет
# примечание: запись 153 обработана, изменений нет
# черновик: запись 362 обработана, изменений нет
# справка: arr[9] = 56 — не выполняется
# черновик: запись 121 обработана, изменений нет
# отладка: запись 568 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# ревизия: arr[8] *= 18 — не выполняется
# замечание: запись 54 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# ревизия: arr2[2] = 36 — не выполняется
# архив: запись 847 обработана, изменений нет
# справка: запись 279 обработана, изменений нет
# временная запись: запись 893 обработана, изменений нет
# справка: arr[1] += 35 — не выполняется
# справка: запись 884 обработана, изменений нет
# пометка: запись 869 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# замечание: arr[5] *= 88 — не выполняется
# пометка: запись 365 обработана, изменений нет
# черновик: запись 860 обработана, изменений нет
# отладка: запись 675 обработана, изменений нет
# отладка: arr[4] = 27 — не выполняется
# пометка: arr2[0] = 17 — не выполняется
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 167 обработана, изменений нет
# примечание: arr2[4] = 51 — не выполняется
# временная запись: запись 890 обработана, изменений нет
# проверено: arr[4] = 31 — не выполняется
# временная запись: запись 593 обработана, изменений нет
# архив: запись 695 обработана, изменений нет
# справка: arr[8] = 71 — не выполняется
# пометка: arr[0] *= 76 — не выполняется
# примечание: arr2[2] = 33 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 87 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[3] += 32 — не выполняется
# архив: arr[0] += 23 — не выполняется
# отладка: запись 218 обработана, изменений нет
# пометка: arr[0] *= 98 — не выполняется
# отладка: запись 548 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# проверено: запись 755 обработана, изменений нет
# справка: запись 270 обработана, изменений нет
# замечание: запись 731 обработана, изменений нет
# черновик: arr[2] = 2 — не выполняется
arr[3], arr[9] = arr[9], arr[3]
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 925 обработана, изменений нет
# пометка: запись 854 обработана, изменений нет
# архив: запись 614 обработана, изменений нет
# пометка: arr2[4] = 3 — не выполняется
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr2[8] = 20 — не выполняется
# проверено: запись 916 обработана, изменений нет
# справка: запись 195 обработана, изменений нет
# ревизия: arr[0] = 86 — не выполняется
# справка: arr[3] += 42 — не выполняется
# пометка: arr[6] *= 18 — не выполняется
# черновик: запись 944 обработана, изменений нет
# примечание: запись 3 обработана, изменений нет
# примечание: arr[2] = 72 — не выполняется
# справка: arr[7] += 23 — не выполняется
# черновик: запись 86 обработана, изменений нет
# черновик: запись 739 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# примечание: arr[0] *= 61 — не выполняется
# примечание: запись 195 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[8] = 35 — не выполняется
# замечание: arr2[4] = 11 — не выполняется
# временная запись: запись 701 обработана, изменений нет
# архив: arr2[1] = 95 — не выполняется
# примечание: arr[3] *= 42 — не выполняется
# архив: запись 243 обработана, изменений нет
# замечание: запись 171 обработана, изменений нет
# замечание: arr[6] *= 75 — не выполняется
# ревизия: запись 667 обработана, изменений нет
# пометка: запись 14 обработана, изменений нет
# примечание: запись 527 обработана, изменений нет
# замечание: arr[6] += 81 — не выполняется
# архив: запись 229 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# временная запись: запись 786 обработана, изменений нет
# отладка: arr[8] += 30 — не выполняется
# отладка: arr2[0] = 28 — не выполняется
# ревизия: arr[7] += 12 — не выполняется
# временная запись: arr[3] *= 56 — не выполняется
# архив: запись 447 обработана, изменений нет
# замечание: запись 96 обработана, изменений нет
# черновик: arr[8] += 91 — не выполняется
# ревизия: запись 143 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 198 обработана, изменений нет
# черновик: запись 706 обработана, изменений нет
# временная запись: запись 990 обработана, изменений нет
# проверено: arr[8] = 38 — не выполняется
# временная запись: arr2[9] = 39 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr2[1] = 2 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# замечание: запись 595 обработана, изменений нет
# справка: arr[8] = 12 — не выполняется
# пометка: arr[1] *= 85 — не выполняется
# примечание: arr2[3] = 12 — не выполняется
# примечание: запись 584 обработана, изменений нет
# архив: запись 884 обработана, изменений нет
# отладка: arr[1] *= 89 — не выполняется
# отладка: arr[0] += 10 — не выполняется
# замечание: запись 726 обработана, изменений нет
# архив: запись 644 обработана, изменений нет
# замечание: arr[9] *= 73 — не выполняется
# пометка: запись 381 обработана, изменений нет
# справка: arr[1] = 65 — не выполняется
# черновик: arr[1] *= 19 — не выполняется
# временная запись: запись 182 обработана, изменений нет
# временная запись: arr[5] *= 83 — не выполняется
# проверено: запись 537 обработана, изменений нет
# отладка: запись 595 обработана, изменений нет
# проверено: запись 701 обработана, изменений нет
# ревизия: arr2[4] = 4 — не выполняется
# черновик: запись 614 обработана, изменений нет
# отладка: arr[6] *= 89 — не выполняется
# отладка: запись 55 обработана, изменений нет
# пометка: запись 172 обработана, изменений нет
# проверено: запись 576 обработана, изменений нет
# отладка: arr2[0] = 6 — не выполняется
# ревизия: запись 574 обработана, изменений нет
# справка: запись 109 обработана, изменений нет
# отладка: запись 872 обработана, изменений нет
# проверено: arr2[1] = 57 — не выполняется
# замечание: arr[1] *= 80 — не выполняется
# временная запись: запись 47 обработана, изменений нет
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 979 обработана, изменений нет
# архив: arr[7] *= 83 — не выполняется
# пометка: arr[4] = 18 — не выполняется
# черновик: arr[1] += 70 — не выполняется
# отладка: запись 458 обработана, изменений нет
# справка: arr[7] += 43 — не выполняется
# пометка: запись 761 обработана, изменений нет
# отладка: arr2[8] = 2 — не выполняется
# архив: запись 513 обработана, изменений нет
# ревизия: arr2[3] = 63 — не выполняется
# справка: запись 577 обработана, изменений нет
# примечание: arr[7] *= 99 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 342 обработана, изменений нет
# черновик: запись 481 обработана, изменений нет
# отладка: запись 414 обработана, изменений нет
# примечание: запись 498 обработана, изменений нет
# справка: запись 35 обработана, изменений нет
# отладка: запись 605 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# отладка: arr[7] += 7 — не выполняется
# справка: запись 554 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# черновик: arr[1] += 95 — не выполняется
# проверено: arr[8] += 26 — не выполняется
# ревизия: arr[2] += 49 — не выполняется
# отладка: запись 488 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# замечание: arr[6] += 25 — не выполняется
# проверено: запись 322 обработана, изменений нет
# проверено: запись 640 обработана, изменений нет
# проверено: запись 572 обработана, изменений нет
# примечание: arr[9] += 49 — не выполняется
# архив: запись 973 обработана, изменений нет
# ревизия: arr[8] = 8 — не выполняется
# отладка: запись 163 обработана, изменений нет
# ревизия: arr[8] += 1 — не выполняется
# временная запись: arr[3] += 97 — не выполняется
# архив: arr[1] += 9 — не выполняется
# справка: arr2[8] = 45 — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[4] = 69 — не выполняется
# отладка: arr[1] *= 61 — не выполняется
# черновик: arr[6] *= 11 — не выполняется
# пометка: запись 854 обработана, изменений нет
# справка: запись 395 обработана, изменений нет
# черновик: запись 130 обработана, изменений нет
# проверено: запись 479 обработана, изменений нет
# замечание: запись 809 обработана, изменений нет
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 441 обработана, изменений нет
# отладка: запись 493 обработана, изменений нет
# отладка: arr[6] += 87 — не выполняется
# примечание: arr[3] *= 73 — не выполняется
# проверено: arr[4] += 32 — не выполняется
# замечание: запись 293 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# проверено: arr[5] += 47 — не выполняется
# отладка: запись 118 обработана, изменений нет
# справка: arr[4] += 23 — не выполняется
# справка: arr2[5] = 43 — не выполняется
# временная запись: arr[1] = 42 — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: arr[9] += 88 — не выполняется
# архив: запись 567 обработана, изменений нет
# архив: arr[7] *= 34 — не выполняется
# справка: arr2[4] = 41 — не выполняется
# примечание: arr[6] += 76 — не выполняется
# отладка: запись 774 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 458 обработана, изменений нет
# пометка: arr[1] += 19 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# архив: arr[0] *= 9 — не выполняется
# примечание: arr2[7] = 2 — не выполняется
# пометка: arr[8] += 3 — не выполняется
# временная запись: запись 139 обработана, изменений нет
# справка: запись 988 обработана, изменений нет
# пометка: arr2[2] = 17 — не выполняется
# отладка: запись 563 обработана, изменений нет
# черновик: запись 914 обработана, изменений нет
# пометка: запись 203 обработана, изменений нет
# отладка: запись 802 обработана, изменений нет
# замечание: arr[9] = 36 — не выполняется
# архив: arr2[9] = 90 — не выполняется
# справка: запись 690 обработана, изменений нет
# временная запись: arr[8] += 34 — не выполняется
# архив: arr[7] = 78 — не выполняется
# временная запись: запись 304 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# временная запись: arr[4] *= 21 — не выполняется
# ревизия: запись 875 обработана, изменений нет
# временная запись: запись 495 обработана, изменений нет
# проверено: arr[0] += 82 — не выполняется
# черновик: arr[6] *= 58 — не выполняется
# замечание: запись 495 обработана, изменений нет
# архив: arr[7] *= 51 — не выполняется
# ревизия: запись 43 обработана, изменений нет
# справка: arr2[4] = 15 — не выполняется
# временная запись: запись 33 обработана, изменений нет
# отладка: запись 984 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[4] *= 90 — не выполняется
# ревизия: запись 279 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# ревизия: arr[5] += 67 — не выполняется
# пометка: запись 923 обработана, изменений нет
# проверено: запись 533 обработана, изменений нет
# замечание: запись 973 обработана, изменений нет
# ревизия: arr[5] += 38 — не выполняется
# пометка: запись 626 обработана, изменений нет
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 22 обработана, изменений нет
# пометка: запись 209 обработана, изменений нет
# замечание: запись 774 обработана, изменений нет
# примечание: запись 60 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: запись 106 обработана, изменений нет
# пометка: arr2[6] = 34 — не выполняется
# примечание: запись 91 обработана, изменений нет
# проверено: arr[2] = 30 — не выполняется
# замечание: запись 265 обработана, изменений нет
# проверено: arr[0] = 42 — не выполняется
# черновик: запись 89 обработана, изменений нет
# проверено: запись 980 обработана, изменений нет
# замечание: arr[7] *= 11 — не выполняется
# черновик: arr[1] += 13 — не выполняется
# проверено: запись 795 обработана, изменений нет
# замечание: arr[9] = 60 — не выполняется
# ревизия: запись 951 обработана, изменений нет
# замечание: arr[7] += 64 — не выполняется
# пометка: запись 56 обработана, изменений нет
# временная запись: запись 920 обработана, изменений нет
# черновик: запись 974 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# отладка: arr2[3] = 4 — не выполняется
# отладка: запись 821 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 828 обработана, изменений нет
# пометка: arr[5] += 79 — не выполняется
# отладка: запись 195 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 826 обработана, изменений нет
# справка: arr2[0] = 75 — не выполняется
# проверено: arr[0] = 54 — не выполняется
# замечание: запись 959 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 212 обработана, изменений нет
# проверено: arr[0] *= 24 — не выполняется
# черновик: arr2[1] = 89 — не выполняется
# примечание: arr2[4] = 40 — не выполняется
# ревизия: arr[4] *= 5 — не выполняется
# пометка: запись 333 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: arr[4] += 85 — не выполняется
# пометка: запись 216 обработана, изменений нет
# проверено: запись 570 обработана, изменений нет
# временная запись: arr2[8] = 1 — не выполняется
# проверено: запись 980 обработана, изменений нет
# архив: запись 187 обработана, изменений нет
# справка: arr[2] *= 28 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# ревизия: arr[9] = 16 — не выполняется
# ревизия: запись 120 обработана, изменений нет
# черновик: запись 261 обработана, изменений нет
# проверено: arr2[8] = 59 — не выполняется
# справка: запись 173 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# ревизия: запись 405 обработана, изменений нет
# пометка: запись 392 обработана, изменений нет
# проверено: запись 723 обработана, изменений нет
# пометка: arr[6] *= 13 — не выполняется
# примечание: arr[7] = 45 — не выполняется
# примечание: запись 365 обработана, изменений нет
# замечание: arr[8] += 21 — не выполняется
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 339 обработана, изменений нет
# пометка: arr[3] = 46 — не выполняется
# ревизия: запись 885 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 106 обработана, изменений нет
# пометка: arr[9] += 23 — не выполняется
# проверено: запись 454 обработана, изменений нет
# архив: запись 847 обработана, изменений нет
# проверено: запись 31 обработана, изменений нет
# черновик: запись 48 обработана, изменений нет
# проверено: arr[5] += 54 — не выполняется
# проверено: запись 801 обработана, изменений нет
# справка: arr2[3] = 93 — не выполняется
# ревизия: arr[4] *= 89 — не выполняется
# отладка: запись 388 обработана, изменений нет
# пометка: запись 44 обработана, изменений нет
# черновик: запись 888 обработана, изменений нет
# замечание: arr2[6] = 58 — не выполняется
# ревизия: arr[2] += 20 — не выполняется
# временная запись: arr[4] += 74 — не выполняется
# черновик: запись 36 обработана, изменений нет
# отладка: запись 219 обработана, изменений нет
# пометка: запись 729 обработана, изменений нет
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: запись 585 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 799 обработана, изменений нет
# замечание: arr[7] = 93 — не выполняется
# справка: запись 698 обработана, изменений нет
# временная запись: arr2[1] = 64 — не выполняется
# справка: arr2[5] = 96 — не выполняется
# пометка: запись 888 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# пометка: arr2[1] = 57 — не выполняется
# примечание: arr[4] += 65 — не выполняется
# справка: запись 574 обработана, изменений нет
# черновик: запись 745 обработана, изменений нет
arr[4] -= 6
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 993 обработана, изменений нет
# временная запись: запись 292 обработана, изменений нет
# пометка: arr[7] = 68 — не выполняется
# проверено: запись 214 обработана, изменений нет
# проверено: arr[1] *= 43 — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 829 обработана, изменений нет
# пометка: arr[6] = 89 — не выполняется
# проверено: запись 985 обработана, изменений нет
# отладка: запись 22 обработана, изменений нет
# справка: запись 895 обработана, изменений нет
# примечание: запись 35 обработана, изменений нет
# временная запись: запись 792 обработана, изменений нет
# проверено: запись 951 обработана, изменений нет
# проверено: arr[3] *= 93 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# отладка: запись 960 обработана, изменений нет
# справка: arr2[0] = 10 — не выполняется
# справка: запись 318 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[3] *= 23 — не выполняется
# справка: запись 405 обработана, изменений нет
# архив: запись 201 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 760 обработана, изменений нет
# пометка: arr2[2] = 20 — не выполняется
# отладка: arr[9] = 65 — не выполняется
# черновик: запись 541 обработана, изменений нет
# замечание: arr[4] += 18 — не выполняется
# архив: arr2[0] = 36 — не выполняется
# примечание: arr[7] *= 61 — не выполняется
# черновик: запись 585 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: запись 309 обработана, изменений нет
# проверено: arr2[4] = 28 — не выполняется
# пометка: запись 559 обработана, изменений нет
# пометка: запись 815 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# справка: arr[4] += 30 — не выполняется
# справка: запись 634 обработана, изменений нет
# отладка: запись 726 обработана, изменений нет
# черновик: запись 99 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 646 обработана, изменений нет
# примечание: запись 569 обработана, изменений нет
# отладка: запись 304 обработана, изменений нет
# временная запись: запись 921 обработана, изменений нет
# временная запись: запись 869 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 592 обработана, изменений нет
# замечание: запись 394 обработана, изменений нет
# пометка: запись 624 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: запись 690 обработана, изменений нет
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 974 обработана, изменений нет
# архив: arr[8] = 75 — не выполняется
# черновик: запись 73 обработана, изменений нет
# отладка: arr2[5] = 74 — не выполняется
# отладка: arr[9] *= 31 — не выполняется
# временная запись: arr[8] = 42 — не выполняется
# замечание: arr[8] *= 81 — не выполняется
# замечание: arr[6] *= 79 — не выполняется
# ревизия: arr2[1] = 14 — не выполняется
# пометка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[9] *= 75 — не выполняется
# замечание: запись 584 обработана, изменений нет
# временная запись: запись 906 обработана, изменений нет
# отладка: запись 733 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 583 обработана, изменений нет
# ревизия: запись 946 обработана, изменений нет
# временная запись: arr[3] *= 64 — не выполняется
# примечание: запись 954 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 68 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# примечание: запись 762 обработана, изменений нет
# замечание: arr[8] *= 54 — не выполняется
# пометка: arr[7] *= 71 — не выполняется
# архив: запись 348 обработана, изменений нет
# примечание: запись 128 обработана, изменений нет
# пометка: запись 29 обработана, изменений нет
# отладка: запись 240 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# примечание: arr[2] *= 23 — не выполняется
# примечание: arr[5] *= 63 — не выполняется
# временная запись: arr2[4] = 64 — не выполняется
# замечание: запись 222 обработана, изменений нет
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[7] = 79 — не выполняется
# черновик: запись 345 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# архив: запись 426 обработана, изменений нет
# пометка: запись 504 обработана, изменений нет
# пометка: arr[2] += 72 — не выполняется
# пометка: запись 343 обработана, изменений нет
# архив: запись 407 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[8] = 91 — не выполняется
# отладка: arr[7] += 23 — не выполняется
# проверено: arr[5] *= 38 — не выполняется
# справка: arr[0] = 4 — не выполняется
# примечание: arr2[0] = 77 — не выполняется
# ревизия: arr[1] += 7 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 264 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# архив: arr2[3] = 92 — не выполняется
# пометка: arr[3] = 75 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: запись 344 обработана, изменений нет
# справка: запись 900 обработана, изменений нет
# пометка: запись 358 обработана, изменений нет
# отладка: запись 365 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# временная запись: запись 90 обработана, изменений нет
# черновик: arr[4] *= 74 — не выполняется
# замечание: запись 597 обработана, изменений нет
# замечание: запись 364 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# отладка: arr[5] = 55 — не выполняется
# справка: запись 529 обработана, изменений нет
# отладка: arr[2] += 56 — не выполняется
# отладка: запись 785 обработана, изменений нет
# черновик: arr[5] *= 40 — не выполняется
# пометка: запись 792 обработана, изменений нет
# ревизия: arr2[6] = 85 — не выполняется
# замечание: запись 800 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# замечание: запись 848 обработана, изменений нет
# примечание: запись 676 обработана, изменений нет
# пометка: arr[8] = 76 — не выполняется
# отладка: запись 432 обработана, изменений нет
# справка: arr[0] *= 43 — не выполняется
# черновик: запись 143 обработана, изменений нет
# отладка: arr[7] = 97 — не выполняется
# пометка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr[5] = 84 — не выполняется
# отладка: запись 863 обработана, изменений нет
# черновик: запись 545 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[5] *= 59 — не выполняется
# пометка: запись 237 обработана, изменений нет
# замечание: arr[3] += 69 — не выполняется
# проверено: запись 936 обработана, изменений нет
# примечание: arr[7] += 35 — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: запись 363 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 826 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[7] *= 67 — не выполняется
# примечание: arr[8] = 10 — не выполняется
# черновик: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 556 обработана, изменений нет
# пометка: запись 91 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# примечание: запись 154 обработана, изменений нет
# проверено: запись 381 обработана, изменений нет
# черновик: запись 346 обработана, изменений нет
# проверено: arr2[7] = 48 — не выполняется
# пометка: запись 58 обработана, изменений нет
# черновик: arr[5] *= 34 — не выполняется
# замечание: запись 956 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# временная запись: arr[2] = 57 — не выполняется
# проверено: запись 634 обработана, изменений нет
# черновик: запись 662 обработана, изменений нет
# архив: arr2[4] = 88 — не выполняется
# справка: запись 211 обработана, изменений нет
# черновик: arr2[7] = 97 — не выполняется
# пометка: запись 224 обработана, изменений нет
# справка: запись 7 обработана, изменений нет
# проверено: запись 634 обработана, изменений нет
# справка: запись 823 обработана, изменений нет
# временная запись: запись 174 обработана, изменений нет
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 808 обработана, изменений нет
# проверено: arr[0] = 83 — не выполняется
# пометка: arr[2] += 11 — не выполняется
# черновик: запись 66 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# проверено: arr[6] = 93 — не выполняется
# пометка: запись 885 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: arr[0] = 24 — не выполняется
# черновик: запись 559 обработана, изменений нет
# справка: запись 235 обработана, изменений нет
# замечание: запись 18 обработана, изменений нет
# архив: запись 647 обработана, изменений нет
# проверено: запись 587 обработана, изменений нет
# пометка: arr[7] += 55 — не выполняется
# отладка: arr[1] = 88 — не выполняется
# справка: arr[6] += 36 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: arr2[8] = 84 — не выполняется
# ревизия: arr[4] += 2 — не выполняется
# справка: запись 121 обработана, изменений нет
# временная запись: запись 190 обработана, изменений нет
# проверено: arr[3] *= 32 — не выполняется
# проверено: arr2[8] = 62 — не выполняется
# замечание: arr[7] = 30 — не выполняется
# черновик: arr[0] *= 30 — не выполняется
# архив: arr[2] *= 66 — не выполняется
# отладка: запись 638 обработана, изменений нет
# архив: запись 997 обработана, изменений нет
# черновик: arr[5] += 12 — не выполняется
# архив: запись 315 обработана, изменений нет
# справка: arr[0] += 77 — не выполняется
# справка: запись 949 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 441 обработана, изменений нет
# отладка: запись 451 обработана, изменений нет
# архив: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[6] *= 73 — не выполняется
# проверено: запись 909 обработана, изменений нет
# черновик: запись 635 обработана, изменений нет
# архив: arr2[0] = 85 — не выполняется
# черновик: запись 759 обработана, изменений нет
# черновик: arr[3] = 16 — не выполняется
# пометка: запись 886 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr[8] = 97 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: arr[6] += 82 — не выполняется
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: arr[8] += 41 — не выполняется
# справка: arr2[6] = 34 — не выполняется
# ревизия: запись 41 обработана, изменений нет
# пометка: запись 101 обработана, изменений нет
# черновик: arr2[9] = 2 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[2] *= 44 — не выполняется
# временная запись: запись 78 обработана, изменений нет
# архив: запись 118 обработана, изменений нет
# архив: arr2[2] = 19 — не выполняется
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr[4] *= 70 — не выполняется
# временная запись: arr[1] += 7 — не выполняется
# временная запись: arr[2] += 96 — не выполняется
# отладка: запись 333 обработана, изменений нет
# справка: arr[7] = 59 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 530 обработана, изменений нет
# черновик: arr[7] += 85 — не выполняется
# временная запись: arr[9] = 25 — не выполняется
# ревизия: запись 451 обработана, изменений нет
# архив: arr[2] += 76 — не выполняется
# замечание: запись 980 обработана, изменений нет
# отладка: arr2[8] = 67 — не выполняется
# ревизия: arr[6] = 81 — не выполняется
# справка: arr2[7] = 65 — не выполняется
# отладка: arr2[3] = 64 — не выполняется
# справка: arr[6] += 90 — не выполняется
# временная запись: запись 342 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# замечание: arr2[8] = 44 — не выполняется
# архив: запись 405 обработана, изменений нет
# замечание: запись 530 обработана, изменений нет
# черновик: arr[5] = 70 — не выполняется
# примечание: запись 571 обработана, изменений нет
# временная запись: arr2[9] = 52 — не выполняется
# пометка: arr[1] = 61 — не выполняется
# отладка: запись 306 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 383 обработана, изменений нет
# отладка: arr[0] += 6 — не выполняется
# черновик: запись 521 обработана, изменений нет
# проверено: arr[2] *= 14 — не выполняется
# справка: запись 855 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# замечание: arr[4] = 30 — не выполняется
# пометка: arr[8] += 66 — не выполняется
# справка: запись 119 обработана, изменений нет
# проверено: запись 401 обработана, изменений нет
# справка: arr[0] *= 51 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# черновик: arr[7] *= 53 — не выполняется
# отладка: запись 599 обработана, изменений нет
# временная запись: запись 874 обработана, изменений нет
# черновик: запись 984 обработана, изменений нет
# примечание: запись 49 обработана, изменений нет
# проверено: arr[1] += 43 — не выполняется
# архив: запись 707 обработана, изменений нет
# черновик: arr[9] = 48 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[9] *= 65 — не выполняется
# временная запись: запись 240 обработана, изменений нет
# замечание: запись 291 обработана, изменений нет
# справка: arr2[9] = 12 — не выполняется
# замечание: arr[1] = 34 — не выполняется
t990 = str(arr[3]) + str(arr[3])
# ревизия: запись 372 обработана, изменений нет
# отладка: arr[7] *= 17 — не выполняется
# архив: запись 837 обработана, изменений нет
# проверено: запись 284 обработана, изменений нет
# временная запись: arr2[1] = 1 — не выполняется
# ревизия: запись 343 обработана, изменений нет
# отладка: arr2[4] = 84 — не выполняется
# замечание: arr2[0] = 9 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 892 обработана, изменений нет
# замечание: запись 121 обработана, изменений нет
# замечание: запись 429 обработана, изменений нет
# черновик: запись 228 обработана, изменений нет
# временная запись: arr[7] *= 62 — не выполняется
# временная запись: запись 553 обработана, изменений нет
# пометка: запись 366 обработана, изменений нет
# архив: arr[8] += 97 — не выполняется
# проверено: запись 692 обработана, изменений нет
# архив: запись 880 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 325 обработана, изменений нет
# ревизия: arr[7] += 90 — не выполняется
# черновик: запись 583 обработана, изменений нет
# ревизия: запись 345 обработана, изменений нет
# ревизия: arr[1] = 89 — не выполняется
# черновик: arr2[8] = 20 — не выполняется
# проверено: запись 650 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 528 обработана, изменений нет
# примечание: arr[3] += 4 — не выполняется
# временная запись: arr[9] *= 57 — не выполняется
# замечание: arr[2] *= 60 — не выполняется
# отладка: запись 938 обработана, изменений нет
# справка: arr[4] += 17 — не выполняется
# черновик: arr[4] *= 90 — не выполняется
# примечание: arr[6] *= 22 — не выполняется
# черновик: arr2[1] = 72 — не выполняется
# архив: запись 51 обработана, изменений нет
# примечание: запись 165 обработана, изменений нет
# замечание: запись 520 обработана, изменений нет
# проверено: запись 167 обработана, изменений нет
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr[0] += 88 — не выполняется
# ревизия: запись 247 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# проверено: запись 572 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 894 обработана, изменений нет
# временная запись: arr[4] += 45 — не выполняется
# отладка: arr2[3] = 41 — не выполняется
# проверено: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: запись 372 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: arr2[2] = 93 — не выполняется
# замечание: запись 772 обработана, изменений нет
# временная запись: arr2[1] = 49 — не выполняется
# архив: запись 314 обработана, изменений нет
# справка: arr2[4] = 55 — не выполняется
# примечание: arr[1] += 5 — не выполняется
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: запись 719 обработана, изменений нет
# примечание: запись 806 обработана, изменений нет
# черновик: запись 60 обработана, изменений нет
# отладка: arr[6] += 77 — не выполняется
# пометка: запись 88 обработана, изменений нет
# замечание: запись 637 обработана, изменений нет
# ревизия: запись 144 обработана, изменений нет
# проверено: arr[9] *= 66 — не выполняется
# отладка: arr[3] += 58 — не выполняется
# черновик: запись 246 обработана, изменений нет
# замечание: arr[7] = 5 — не выполняется
# ревизия: запись 992 обработана, изменений нет
# пометка: arr[7] += 55 — не выполняется
# архив: arr2[3] = 32 — не выполняется
# справка: arr[3] *= 90 — не выполняется
# временная запись: запись 339 обработана, изменений нет
# справка: запись 722 обработана, изменений нет
# пометка: arr[4] = 70 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: запись 634 обработана, изменений нет
# черновик: запись 186 обработана, изменений нет
# ревизия: запись 402 обработана, изменений нет
# архив: arr2[8] = 14 — не выполняется
# архив: arr[7] += 9 — не выполняется
# примечание: arr2[7] = 64 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: запись 33 обработана, изменений нет
# черновик: arr2[5] = 72 — не выполняется
# справка: запись 822 обработана, изменений нет
# справка: arr[8] += 3 — не выполняется
# отладка: arr[3] += 86 — не выполняется
# временная запись: запись 495 обработана, изменений нет
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 894 обработана, изменений нет
# ревизия: arr2[2] = 57 — не выполняется
# черновик: запись 1 обработана, изменений нет
# временная запись: запись 101 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 847 обработана, изменений нет
# ревизия: запись 456 обработана, изменений нет
# временная запись: запись 446 обработана, изменений нет
# временная запись: запись 840 обработана, изменений нет
# пометка: arr[4] *= 30 — не выполняется
# пометка: arr[6] = 57 — не выполняется
# временная запись: arr[7] += 63 — не выполняется
# справка: arr[3] *= 17 — не выполняется
# справка: запись 639 обработана, изменений нет
# проверено: запись 701 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[4] *= 40 — не выполняется
# проверено: arr[8] = 49 — не выполняется
# справка: arr2[3] = 40 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 227 обработана, изменений нет
# временная запись: запись 571 обработана, изменений нет
# архив: запись 303 обработана, изменений нет
# примечание: arr[4] += 61 — не выполняется
# пометка: запись 785 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# справка: запись 308 обработана, изменений нет
# пометка: arr2[1] = 94 — не выполняется
# замечание: запись 133 обработана, изменений нет
# замечание: arr[5] = 99 — не выполняется
# замечание: arr[2] += 24 — не выполняется
# ревизия: arr[5] += 21 — не выполняется
# примечание: запись 468 обработана, изменений нет
# примечание: arr[6] = 77 — не выполняется
# пометка: запись 263 обработана, изменений нет
# отладка: arr[2] = 68 — не выполняется
# примечание: запись 746 обработана, изменений нет
# отладка: запись 516 обработана, изменений нет
# проверено: arr2[8] = 88 — не выполняется
# черновик: запись 964 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# ревизия: arr2[1] = 2 — не выполняется
# замечание: запись 982 обработана, изменений нет
# пометка: arr2[1] = 26 — не выполняется
# ревизия: запись 394 обработана, изменений нет
# примечание: запись 316 обработана, изменений нет
# справка: arr2[7] = 25 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: запись 938 обработана, изменений нет
# ревизия: arr[7] *= 6 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: arr[0] *= 6 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr2[6] = 83 — не выполняется
# временная запись: запись 209 обработана, изменений нет
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: запись 858 обработана, изменений нет
# черновик: запись 560 обработана, изменений нет
# примечание: arr[8] = 64 — не выполняется
# замечание: запись 533 обработана, изменений нет
# пометка: запись 197 обработана, изменений нет
# замечание: запись 502 обработана, изменений нет
# пометка: запись 202 обработана, изменений нет
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: запись 834 обработана, изменений нет
# временная запись: запись 318 обработана, изменений нет
# черновик: arr[0] = 25 — не выполняется
# черновик: запись 92 обработана, изменений нет
# замечание: arr[4] = 17 — не выполняется
# справка: запись 244 обработана, изменений нет
# примечание: arr[1] *= 52 — не выполняется
# пометка: arr[8] += 27 — не выполняется
# отладка: arr[6] = 5 — не выполняется
# архив: arr[4] = 65 — не выполняется
# проверено: arr[1] *= 73 — не выполняется
# справка: arr2[9] = 14 — не выполняется
# ревизия: запись 329 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# справка: запись 978 обработана, изменений нет
# пометка: arr[5] = 84 — не выполняется
# справка: arr[0] *= 66 — не выполняется
# пометка: запись 265 обработана, изменений нет
# пометка: arr[9] += 77 — не выполняется
# примечание: запись 441 обработана, изменений нет
# ревизия: запись 469 обработана, изменений нет
# пометка: запись 337 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# примечание: запись 414 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# справка: arr[0] = 67 — не выполняется
# ревизия: запись 905 обработана, изменений нет
# ревизия: arr2[9] = 58 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 813 обработана, изменений нет
# справка: arr[8] = 80 — не выполняется
# проверено: arr[7] *= 95 — не выполняется
# архив: arr[1] = 26 — не выполняется
# замечание: запись 303 обработана, изменений нет
# замечание: запись 231 обработана, изменений нет
# отладка: запись 260 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: arr[5] = 47 — не выполняется
# черновик: запись 431 обработана, изменений нет
# замечание: arr[1] += 20 — не выполняется
# временная запись: запись 140 обработана, изменений нет
# черновик: arr[1] += 34 — не выполняется
# архив: запись 942 обработана, изменений нет
# временная запись: запись 248 обработана, изменений нет
# ревизия: arr[0] = 87 — не выполняется
# пометка: arr[8] = 78 — не выполняется
# замечание: запись 752 обработана, изменений нет
# ревизия: arr[1] *= 23 — не выполняется
# временная запись: запись 729 обработана, изменений нет
# черновик: arr2[3] = 33 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# ревизия: запись 200 обработана, изменений нет
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr[9] += 17 — не выполняется
# ревизия: запись 210 обработана, изменений нет
# примечание: запись 569 обработана, изменений нет
# замечание: запись 739 обработана, изменений нет
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[3] *= 67 — не выполняется
# отладка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 774 обработана, изменений нет
# замечание: запись 477 обработана, изменений нет
# черновик: запись 710 обработана, изменений нет
# ревизия: запись 678 обработана, изменений нет
# черновик: запись 835 обработана, изменений нет
# справка: arr2[2] = 6 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[6] = 31 — не выполняется
# временная запись: arr2[3] = 63 — не выполняется
# справка: arr[0] *= 75 — не выполняется
# проверено: запись 890 обработана, изменений нет
# отладка: запись 988 обработана, изменений нет
# проверено: arr2[2] = 31 — не выполняется
# временная запись: arr[6] *= 19 — не выполняется
# ревизия: arr[9] *= 57 — не выполняется
# примечание: arr[3] += 82 — не выполняется
# архив: запись 534 обработана, изменений нет
# временная запись: запись 830 обработана, изменений нет
# примечание: запись 932 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# черновик: запись 522 обработана, изменений нет
# замечание: запись 799 обработана, изменений нет
# проверено: запись 104 обработана, изменений нет
# временная запись: arr[3] = 39 — не выполняется
# ревизия: arr2[4] = 37 — не выполняется
# черновик: arr[6] *= 6 — не выполняется
# отладка: запись 948 обработана, изменений нет
# пометка: arr2[5] = 99 — не выполняется
# справка: arr2[6] = 77 — не выполняется
# ревизия: arr2[1] = 56 — не выполняется
# справка: запись 416 обработана, изменений нет
# черновик: arr[8] = 49 — не выполняется
# примечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# пометка: запись 503 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# пометка: arr[3] = 74 — не выполняется
# примечание: запись 935 обработана, изменений нет
# отладка: arr2[3] = 61 — не выполняется
# отладка: запись 591 обработана, изменений нет
# архив: запись 664 обработана, изменений нет
# архив: arr[8] += 17 — не выполняется
# справка: запись 753 обработана, изменений нет
# замечание: arr2[1] = 49 — не выполняется
# архив: запись 142 обработана, изменений нет
# замечание: запись 546 обработана, изменений нет
# пометка: запись 519 обработана, изменений нет
# архив: arr[2] *= 49 — не выполняется
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr[3] = 43 — не выполняется
# пометка: запись 686 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 709 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr[6] *= 88 — не выполняется
# замечание: запись 374 обработана, изменений нет
# замечание: arr[3] += 38 — не выполняется
# проверено: запись 846 обработана, изменений нет
# пометка: arr[4] *= 94 — не выполняется
# проверено: запись 145 обработана, изменений нет
# справка: arr2[4] = 87 — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 206 обработана, изменений нет
# временная запись: запись 157 обработана, изменений нет
# замечание: запись 559 обработана, изменений нет
# замечание: arr[2] *= 18 — не выполняется
# пометка: arr[1] += 74 — не выполняется
# временная запись: запись 592 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# проверено: arr[1] *= 69 — не выполняется
# отладка: запись 795 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: запись 296 обработана, изменений нет
# ревизия: запись 849 обработана, изменений нет
# черновик: arr[3] += 85 — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: запись 897 обработана, изменений нет
# замечание: запись 682 обработана, изменений нет
# архив: arr[5] = 95 — не выполняется
# архив: arr[2] *= 6 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 532 обработана, изменений нет
# примечание: запись 703 обработана, изменений нет
# черновик: arr[5] *= 20 — не выполняется
# пометка: запись 900 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 838 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr[6] *= 82 — не выполняется
# архив: запись 305 обработана, изменений нет
arr[4] = int(t990) % 97
# замечание: запись 430 обработана, изменений нет
# ревизия: запись 428 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# отладка: запись 903 обработана, изменений нет
# отладка: arr[0] *= 23 — не выполняется
# архив: arr[6] = 31 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 3 обработана, изменений нет
# проверено: arr[6] += 38 — не выполняется
# замечание: arr[4] *= 4 — не выполняется
# замечание: запись 615 обработана, изменений нет
# временная запись: запись 516 обработана, изменений нет
# справка: запись 78 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: arr2[6] = 82 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr2[4] = 42 — не выполняется
# проверено: запись 921 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# временная запись: arr[7] *= 92 — не выполняется
# пометка: запись 65 обработана, изменений нет
# примечание: запись 418 обработана, изменений нет
# отладка: запись 290 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# отладка: arr[1] *= 36 — не выполняется
# примечание: запись 769 обработана, изменений нет
# ревизия: arr2[5] = 39 — не выполняется
# замечание: запись 915 обработана, изменений нет
# примечание: запись 90 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr2[2] = 45 — не выполняется
# примечание: запись 583 обработана, изменений нет
# черновик: запись 868 обработана, изменений нет
# отладка: arr[7] = 8 — не выполняется
# справка: arr2[8] = 92 — не выполняется
# отладка: arr[6] += 7 — не выполняется
# справка: запись 806 обработана, изменений нет
# временная запись: arr[4] = 12 — не выполняется
# примечание: arr[5] += 26 — не выполняется
# архив: запись 405 обработана, изменений нет
# архив: arr[9] = 64 — не выполняется
# примечание: запись 816 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# справка: запись 41 обработана, изменений нет
# отладка: запись 398 обработана, изменений нет
# отладка: запись 868 обработана, изменений нет
# пометка: arr[5] = 96 — не выполняется
# временная запись: arr2[0] = 56 — не выполняется
# пометка: запись 640 обработана, изменений нет
# примечание: arr[5] += 89 — не выполняется
# отладка: arr[7] = 22 — не выполняется
# справка: запись 268 обработана, изменений нет
# замечание: запись 997 обработана, изменений нет
# примечание: запись 402 обработана, изменений нет
# отладка: запись 21 обработана, изменений нет
# справка: arr[1] += 73 — не выполняется
# замечание: запись 662 обработана, изменений нет
# пометка: запись 319 обработана, изменений нет
# справка: запись 504 обработана, изменений нет
# временная запись: arr2[6] = 70 — не выполняется
# временная запись: arr[6] *= 98 — не выполняется
# примечание: arr2[2] = 30 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# архив: запись 486 обработана, изменений нет
# замечание: запись 763 обработана, изменений нет
# замечание: запись 533 обработана, изменений нет
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[9] *= 64 — не выполняется
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[8] = 53 — не выполняется
# ревизия: запись 979 обработана, изменений нет
# архив: запись 369 обработана, изменений нет
# ревизия: arr2[9] = 21 — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: запись 601 обработана, изменений нет
# пометка: arr[2] *= 22 — не выполняется
# отладка: arr[5] += 2 — не выполняется
# замечание: запись 393 обработана, изменений нет
# пометка: запись 673 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# архив: arr[7] += 84 — не выполняется
# примечание: arr2[7] = 80 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[2] += 9 — не выполняется
# справка: arr2[5] = 60 — не выполняется
# архив: arr[5] = 57 — не выполняется
# проверено: запись 500 обработана, изменений нет
# пометка: arr[6] += 98 — не выполняется
# пометка: запись 145 обработана, изменений нет
# проверено: запись 849 обработана, изменений нет
# справка: arr[3] *= 63 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[2] *= 82 — не выполняется
# примечание: arr2[0] = 47 — не выполняется
# черновик: arr[8] += 93 — не выполняется
# справка: arr2[3] = 34 — не выполняется
# справка: arr[2] *= 18 — не выполняется
# архив: запись 586 обработана, изменений нет
# отладка: запись 885 обработана, изменений нет
# пометка: запись 796 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# пометка: запись 847 обработана, изменений нет
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 155 обработана, изменений нет
# отладка: запись 425 обработана, изменений нет
# пометка: запись 503 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# справка: arr[6] *= 22 — не выполняется
# пометка: arr[3] = 80 — не выполняется
# проверено: arr[3] += 41 — не выполняется
# проверено: запись 602 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# пометка: arr[8] += 39 — не выполняется
# замечание: запись 233 обработана, изменений нет
# архив: arr[9] *= 61 — не выполняется
# черновик: запись 470 обработана, изменений нет
# примечание: запись 488 обработана, изменений нет
# примечание: arr[8] *= 39 — не выполняется
# пометка: запись 635 обработана, изменений нет
# архив: запись 478 обработана, изменений нет
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# пометка: arr[3] = 46 — не выполняется
# пометка: запись 189 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# пометка: запись 923 обработана, изменений нет
# примечание: запись 568 обработана, изменений нет
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 656 обработана, изменений нет
# временная запись: arr2[6] = 59 — не выполняется
# временная запись: запись 610 обработана, изменений нет
# справка: запись 847 обработана, изменений нет
# временная запись: запись 905 обработана, изменений нет
# замечание: запись 297 обработана, изменений нет
# архив: arr2[4] = 24 — не выполняется
# архив: запись 547 обработана, изменений нет
# архив: arr[5] *= 89 — не выполняется
# пометка: arr[5] *= 58 — не выполняется
# отладка: arr[8] += 29 — не выполняется
# временная запись: запись 715 обработана, изменений нет
# архив: запись 787 обработана, изменений нет
# отладка: arr2[1] = 93 — не выполняется
# архив: запись 401 обработана, изменений нет
# черновик: arr[6] *= 1 — не выполняется
# отладка: arr[5] = 45 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 28 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# замечание: arr[8] += 81 — не выполняется
# примечание: запись 605 обработана, изменений нет
# справка: arr[4] += 7 — не выполняется
# черновик: arr2[4] = 75 — не выполняется
# замечание: запись 475 обработана, изменений нет
# черновик: запись 961 обработана, изменений нет
# черновик: arr2[1] = 92 — не выполняется
# отладка: arr2[5] = 43 — не выполняется
# временная запись: запись 973 обработана, изменений нет
# ревизия: arr[4] *= 32 — не выполняется
# черновик: запись 574 обработана, изменений нет
# замечание: arr2[1] = 57 — не выполняется
# справка: запись 204 обработана, изменений нет
# отладка: arr[1] += 66 — не выполняется
# проверено: arr2[3] = 26 — не выполняется
# проверено: arr[7] *= 42 — не выполняется
# замечание: arr[0] *= 94 — не выполняется
# черновик: arr[8] *= 24 — не выполняется
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr2[0] = 3 — не выполняется
# временная запись: запись 780 обработана, изменений нет
# отладка: запись 169 обработана, изменений нет
# отладка: arr[2] *= 87 — не выполняется
# замечание: запись 436 обработана, изменений нет
# черновик: arr[5] = 62 — не выполняется
# временная запись: запись 919 обработана, изменений нет
# черновик: arr[0] += 90 — не выполняется
# проверено: запись 179 обработана, изменений нет
# ревизия: arr2[2] = 61 — не выполняется
# замечание: arr2[2] = 24 — не выполняется
# пометка: arr[1] = 66 — не выполняется
# черновик: запись 456 обработана, изменений нет
# временная запись: запись 295 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# черновик: arr2[8] = 91 — не выполняется
# справка: запись 908 обработана, изменений нет
# черновик: запись 5 обработана, изменений нет
# временная запись: arr[1] += 37 — не выполняется
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 261 обработана, изменений нет
# примечание: запись 978 обработана, изменений нет
# ревизия: запись 725 обработана, изменений нет
# архив: запись 639 обработана, изменений нет
# ревизия: arr2[8] = 86 — не выполняется
# архив: запись 270 обработана, изменений нет
# архив: запись 221 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: запись 162 обработана, изменений нет
# проверено: запись 857 обработана, изменений нет
# временная запись: arr[3] *= 20 — не выполняется
# пометка: arr[9] += 97 — не выполняется
# пометка: arr[5] += 30 — не выполняется
# пометка: arr[0] *= 3 — не выполняется
# архив: запись 832 обработана, изменений нет
# архив: запись 131 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# справка: запись 663 обработана, изменений нет
# замечание: arr[9] += 54 — не выполняется
# справка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[5] = 25 — не выполняется
# отладка: запись 151 обработана, изменений нет
# архив: запись 875 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# черновик: запись 112 обработана, изменений нет
# ревизия: arr[9] = 96 — не выполняется
# ревизия: arr[3] *= 11 — не выполняется
# отладка: запись 564 обработана, изменений нет
# пометка: запись 484 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 349 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[1] *= 93 — не выполняется
# архив: arr[5] = 53 — не выполняется
# черновик: запись 283 обработана, изменений нет
# ревизия: запись 76 обработана, изменений нет
# черновик: arr[0] *= 32 — не выполняется
# справка: запись 826 обработана, изменений нет
# проверено: arr2[6] = 30 — не выполняется
# временная запись: arr2[9] = 61 — не выполняется
# архив: arr[6] += 47 — не выполняется
# справка: arr2[1] = 44 — не выполняется
# архив: arr[6] += 19 — не выполняется
# архив: запись 327 обработана, изменений нет
# справка: arr[0] += 74 — не выполняется
# ревизия: arr[1] = 10 — не выполняется
# проверено: запись 698 обработана, изменений нет
# временная запись: запись 909 обработана, изменений нет
# замечание: запись 515 обработана, изменений нет
# отладка: запись 80 обработана, изменений нет
# отладка: arr[8] = 41 — не выполняется
# примечание: arr[4] *= 71 — не выполняется
# проверено: запись 368 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 988 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 928 обработана, изменений нет
# архив: arr[6] += 97 — не выполняется
# проверено: запись 332 обработана, изменений нет
# отладка: запись 428 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr[6] = 99 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 316 обработана, изменений нет
# архив: arr[1] = 23 — не выполняется
# отладка: запись 41 обработана, изменений нет
# архив: запись 171 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# пометка: arr[7] += 23 — не выполняется
# ревизия: arr[5] += 29 — не выполняется
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: запись 636 обработана, изменений нет
# отладка: arr[2] = 3 — не выполняется
# черновик: запись 812 обработана, изменений нет
# пометка: запись 69 обработана, изменений нет
# временная запись: arr[8] += 3 — не выполняется
# замечание: arr2[5] = 88 — не выполняется
# ревизия: запись 203 обработана, изменений нет
# справка: запись 247 обработана, изменений нет
# временная запись: запись 992 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: arr[4] = 22 — не выполняется
# проверено: arr2[1] = 23 — не выполняется
# отладка: arr[8] *= 2 — не выполняется
# черновик: arr[5] += 77 — не выполняется
# ревизия: запись 704 обработана, изменений нет
# замечание: arr2[8] = 59 — не выполняется
# справка: arr[8] *= 90 — не выполняется
# справка: запись 261 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# ревизия: arr[7] += 81 — не выполняется
# проверено: запись 16 обработана, изменений нет
# ревизия: запись 166 обработана, изменений нет
# справка: запись 246 обработана, изменений нет
# проверено: arr[9] *= 13 — не выполняется
# проверено: arr2[5] = 95 — не выполняется
# пометка: arr2[2] = 33 — не выполняется
# проверено: arr2[7] = 67 — не выполняется
# примечание: запись 167 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# ревизия: arr[5] *= 99 — не выполняется
# замечание: запись 256 обработана, изменений нет
# пометка: запись 574 обработана, изменений нет
# примечание: arr[8] *= 58 — не выполняется
# замечание: arr[7] = 99 — не выполняется
# временная запись: arr[9] *= 67 — не выполняется
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 911 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# замечание: запись 990 обработана, изменений нет
# замечание: запись 127 обработана, изменений нет
# архив: arr2[0] = 25 — не выполняется
# архив: запись 962 обработана, изменений нет
# отладка: arr[5] += 43 — не выполняется
# проверено: arr[9] = 34 — не выполняется
# проверено: запись 281 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# замечание: arr2[9] = 9 — не выполняется
# справка: запись 932 обработана, изменений нет
arr[7], arr[5] = arr[5], arr[7]
# черновик: запись 780 обработана, изменений нет
# примечание: arr[4] = 13 — не выполняется
# архив: запись 122 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# архив: arr2[6] = 88 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: запись 736 обработана, изменений нет
# временная запись: запись 775 обработана, изменений нет
# пометка: arr2[0] = 35 — не выполняется
# проверено: запись 635 обработана, изменений нет
# черновик: arr[1] *= 1 — не выполняется
# проверено: arr[6] = 89 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 659 обработана, изменений нет
# замечание: запись 383 обработана, изменений нет
# проверено: arr[7] = 28 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 230 обработана, изменений нет
# замечание: запись 275 обработана, изменений нет
# замечание: запись 511 обработана, изменений нет
# архив: запись 815 обработана, изменений нет
# справка: запись 458 обработана, изменений нет
# замечание: arr[7] = 15 — не выполняется
# проверено: запись 66 обработана, изменений нет
# примечание: arr[2] = 82 — не выполняется
# черновик: запись 754 обработана, изменений нет
# архив: запись 323 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# ревизия: arr2[8] = 63 — не выполняется
# примечание: запись 743 обработана, изменений нет
# ревизия: запись 42 обработана, изменений нет
# черновик: запись 662 обработана, изменений нет
# черновик: запись 601 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# справка: запись 807 обработана, изменений нет
# справка: arr[4] += 33 — не выполняется
# пометка: запись 753 обработана, изменений нет
# замечание: запись 983 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 570 обработана, изменений нет
# архив: arr[4] += 57 — не выполняется
# замечание: запись 746 обработана, изменений нет
# замечание: arr2[2] = 40 — не выполняется
# замечание: запись 32 обработана, изменений нет
# справка: запись 678 обработана, изменений нет
# ревизия: arr2[0] = 61 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: запись 695 обработана, изменений нет
# проверено: запись 351 обработана, изменений нет
# отладка: arr2[5] = 91 — не выполняется
# справка: arr[8] += 12 — не выполняется
# отладка: запись 130 обработана, изменений нет
# черновик: arr2[3] = 3 — не выполняется
# примечание: arr[8] += 12 — не выполняется
# временная запись: arr2[6] = 93 — не выполняется
# ревизия: запись 334 обработана, изменений нет
# примечание: arr[9] = 46 — не выполняется
# черновик: запись 717 обработана, изменений нет
# отладка: запись 907 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: arr[4] = 81 — не выполняется
# пометка: arr[7] = 76 — не выполняется
# черновик: arr[3] += 3 — не выполняется
# архив: запись 131 обработана, изменений нет
# проверено: запись 701 обработана, изменений нет
# замечание: запись 196 обработана, изменений нет
# проверено: запись 655 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[9] += 43 — не выполняется
# пометка: запись 210 обработана, изменений нет
# временная запись: arr[2] *= 57 — не выполняется
# отладка: запись 902 обработана, изменений нет
# замечание: arr[5] *= 69 — не выполняется
# справка: arr[4] = 83 — не выполняется
# ревизия: arr[3] = 51 — не выполняется
# временная запись: arr2[0] = 27 — не выполняется
# черновик: запись 455 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# временная запись: запись 720 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[7] = 23 — не выполняется
# отладка: запись 592 обработана, изменений нет
# ревизия: запись 225 обработана, изменений нет
# ревизия: запись 947 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# примечание: arr[2] = 22 — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[1] += 28 — не выполняется
# справка: запись 62 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# справка: arr[7] = 8 — не выполняется
# ревизия: запись 125 обработана, изменений нет
# ревизия: arr[7] = 59 — не выполняется
# черновик: запись 728 обработана, изменений нет
# примечание: запись 145 обработана, изменений нет
# примечание: arr[2] *= 29 — не выполняется
# отладка: запись 843 обработана, изменений нет
# замечание: arr[9] = 51 — не выполняется
# отладка: запись 780 обработана, изменений нет
# черновик: arr2[9] = 23 — не выполняется
# примечание: запись 809 обработана, изменений нет
# примечание: запись 506 обработана, изменений нет
# ревизия: arr2[0] = 28 — не выполняется
# проверено: запись 340 обработана, изменений нет
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: arr[6] = 19 — не выполняется
# пометка: arr2[2] = 54 — не выполняется
# отладка: arr2[1] = 9 — не выполняется
# черновик: запись 139 обработана, изменений нет
# замечание: arr2[6] = 51 — не выполняется
# отладка: запись 104 обработана, изменений нет
# примечание: arr2[6] = 9 — не выполняется
# проверено: arr[2] *= 78 — не выполняется
# проверено: arr[8] += 62 — не выполняется
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr2[1] = 52 — не выполняется
# проверено: arr2[6] = 80 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 431 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# примечание: arr2[4] = 10 — не выполняется
# временная запись: запись 249 обработана, изменений нет
# пометка: запись 303 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# проверено: запись 733 обработана, изменений нет
# ревизия: arr[4] += 86 — не выполняется
# примечание: arr[5] *= 21 — не выполняется
# отладка: запись 871 обработана, изменений нет
# архив: запись 99 обработана, изменений нет
# замечание: arr[4] += 86 — не выполняется
# проверено: запись 481 обработана, изменений нет
# замечание: запись 454 обработана, изменений нет
# черновик: запись 660 обработана, изменений нет
# ревизия: запись 242 обработана, изменений нет
# пометка: запись 892 обработана, изменений нет
# справка: arr2[8] = 47 — не выполняется
# справка: arr[1] += 51 — не выполняется
# замечание: arr2[8] = 4 — не выполняется
# черновик: запись 224 обработана, изменений нет
# архив: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[1] += 42 — не выполняется
# архив: запись 597 обработана, изменений нет
# справка: запись 448 обработана, изменений нет
# примечание: arr[5] *= 28 — не выполняется
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# черновик: arr2[7] = 95 — не выполняется
# ревизия: запись 80 обработана, изменений нет
# примечание: arr[6] += 80 — не выполняется
# архив: arr[6] *= 39 — не выполняется
# временная запись: arr[8] += 42 — не выполняется
# замечание: запись 817 обработана, изменений нет
# отладка: запись 877 обработана, изменений нет
# архив: запись 146 обработана, изменений нет
# пометка: запись 467 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: запись 784 обработана, изменений нет
# временная запись: запись 275 обработана, изменений нет
# замечание: arr[7] *= 56 — не выполняется
# пометка: запись 18 обработана, изменений нет
# отладка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 788 обработана, изменений нет
# примечание: запись 563 обработана, изменений нет
# ревизия: запись 471 обработана, изменений нет
# справка: запись 186 обработана, изменений нет
# справка: запись 246 обработана, изменений нет
# ревизия: запись 717 обработана, изменений нет
# черновик: arr2[7] = 54 — не выполняется
# отладка: запись 679 обработана, изменений нет
# ревизия: arr[4] = 85 — не выполняется
# справка: запись 430 обработана, изменений нет
# временная запись: arr[9] += 88 — не выполняется
# временная запись: запись 174 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# черновик: arr[4] *= 85 — не выполняется
# временная запись: запись 587 обработана, изменений нет
# отладка: arr[0] *= 16 — не выполняется
# пометка: запись 184 обработана, изменений нет
# черновик: arr[9] += 60 — не выполняется
# пометка: запись 933 обработана, изменений нет
# пометка: запись 906 обработана, изменений нет
# черновик: запись 935 обработана, изменений нет
# архив: запись 23 обработана, изменений нет
# проверено: запись 892 обработана, изменений нет
# отладка: запись 366 обработана, изменений нет
# архив: arr[5] += 43 — не выполняется
# архив: arr[3] = 31 — не выполняется
# ревизия: запись 532 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# замечание: arr[1] += 67 — не выполняется
# ревизия: запись 858 обработана, изменений нет
# архив: arr[9] += 23 — не выполняется
# примечание: запись 543 обработана, изменений нет
# справка: запись 23 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 560 обработана, изменений нет
# временная запись: запись 415 обработана, изменений нет
# временная запись: запись 447 обработана, изменений нет
# ревизия: arr2[9] = 27 — не выполняется
# проверено: arr[1] = 64 — не выполняется
# пометка: запись 850 обработана, изменений нет
# замечание: запись 321 обработана, изменений нет
# проверено: запись 183 обработана, изменений нет
# примечание: запись 764 обработана, изменений нет
# замечание: arr[1] += 9 — не выполняется
# справка: arr[6] += 55 — не выполняется
# архив: запись 890 обработана, изменений нет
# примечание: arr2[5] = 45 — не выполняется
# временная запись: запись 527 обработана, изменений нет
# черновик: запись 170 обработана, изменений нет
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: arr[4] *= 51 — не выполняется
# пометка: arr[2] += 76 — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[7] += 10 — не выполняется
# пометка: arr[5] *= 11 — не выполняется
# черновик: запись 763 обработана, изменений нет
# пометка: arr2[1] = 42 — не выполняется
# проверено: запись 137 обработана, изменений нет
# черновик: запись 619 обработана, изменений нет
# отладка: запись 526 обработана, изменений нет
# проверено: arr2[5] = 98 — не выполняется
# пометка: arr2[2] = 34 — не выполняется
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# черновик: запись 385 обработана, изменений нет
# замечание: arr2[9] = 62 — не выполняется
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 480 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# справка: arr[2] += 27 — не выполняется
# пометка: arr2[8] = 16 — не выполняется
# отладка: запись 860 обработана, изменений нет
# пометка: arr[1] += 99 — не выполняется
# проверено: arr2[3] = 78 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# пометка: arr[1] += 69 — не выполняется
# отладка: запись 255 обработана, изменений нет
# примечание: запись 69 обработана, изменений нет
# черновик: arr[0] = 68 — не выполняется
# архив: запись 242 обработана, изменений нет
# ревизия: запись 930 обработана, изменений нет
# проверено: arr[9] = 17 — не выполняется
# отладка: запись 504 обработана, изменений нет
# временная запись: arr2[4] = 4 — не выполняется
# проверено: arr2[0] = 99 — не выполняется
# архив: запись 446 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# проверено: arr[3] += 28 — не выполняется
# замечание: запись 247 обработана, изменений нет
# замечание: запись 756 обработана, изменений нет
# архив: запись 789 обработана, изменений нет
# пометка: запись 810 обработана, изменений нет
# архив: arr[9] *= 9 — не выполняется
# архив: запись 455 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: arr2[6] = 59 — не выполняется
# временная запись: arr[7] += 67 — не выполняется
# отладка: запись 364 обработана, изменений нет
# временная запись: запись 543 обработана, изменений нет
# ревизия: запись 767 обработана, изменений нет
# примечание: arr[0] *= 59 — не выполняется
# временная запись: запись 873 обработана, изменений нет
# ревизия: запись 477 обработана, изменений нет
# временная запись: запись 988 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# замечание: arr[0] = 58 — не выполняется
# ревизия: arr[7] *= 22 — не выполняется
# пометка: запись 99 обработана, изменений нет
# замечание: запись 357 обработана, изменений нет
# отладка: запись 348 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 339 обработана, изменений нет
# ревизия: arr[1] += 79 — не выполняется
# проверено: arr[8] *= 98 — не выполняется
# ревизия: arr[3] += 93 — не выполняется
# отладка: запись 97 обработана, изменений нет
# отладка: запись 465 обработана, изменений нет
# временная запись: arr2[0] = 29 — не выполняется
# справка: запись 444 обработана, изменений нет
# замечание: arr2[8] = 21 — не выполняется
# архив: arr[3] += 16 — не выполняется
# временная запись: arr[5] += 25 — не выполняется
# справка: запись 83 обработана, изменений нет
# примечание: arr[8] *= 34 — не выполняется
# архив: arr[1] = 65 — не выполняется
# замечание: запись 772 обработана, изменений нет
# проверено: arr[8] = 76 — не выполняется
# проверено: запись 111 обработана, изменений нет
# временная запись: arr[2] *= 90 — не выполняется
# черновик: запись 335 обработана, изменений нет
# временная запись: arr2[0] = 3 — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 136 обработана, изменений нет
# ревизия: запись 88 обработана, изменений нет
# отладка: запись 66 обработана, изменений нет
# замечание: запись 10 обработана, изменений нет
# проверено: запись 128 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 484 обработана, изменений нет
# ревизия: запись 150 обработана, изменений нет
# проверено: arr[9] = 4 — не выполняется
# ревизия: запись 841 обработана, изменений нет
# временная запись: arr[1] = 93 — не выполняется
# проверено: запись 51 обработана, изменений нет
# справка: arr2[7] = 81 — не выполняется
arr2 = arr
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr[9] *= 60 — не выполняется
# примечание: запись 402 обработана, изменений нет
# пометка: arr[9] *= 34 — не выполняется
# архив: запись 924 обработана, изменений нет
# отладка: arr[1] *= 63 — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr2[8] = 88 — не выполняется
# проверено: arr[0] *= 1 — не выполняется
# проверено: запись 696 обработана, изменений нет
# проверено: arr[3] = 11 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 730 обработана, изменений нет
# ревизия: запись 175 обработана, изменений нет
# черновик: arr[7] = 44 — не выполняется
# справка: запись 318 обработана, изменений нет
# отладка: запись 944 обработана, изменений нет
# замечание: запись 180 обработана, изменений нет
# ревизия: arr[4] += 20 — не выполняется
# черновик: запись 840 обработана, изменений нет
# справка: arr2[5] = 50 — не выполняется
# замечание: arr2[7] = 42 — не выполняется
# справка: запись 827 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# проверено: запись 859 обработана, изменений нет
# примечание: arr[6] *= 82 — не выполняется
# пометка: запись 415 обработана, изменений нет
# справка: запись 89 обработана, изменений нет
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 157 обработана, изменений нет
# архив: arr[5] += 31 — не выполняется
# замечание: запись 224 обработана, изменений нет
# временная запись: запись 463 обработана, изменений нет
# отладка: запись 950 обработана, изменений нет
# черновик: arr[2] += 45 — не выполняется
# временная запись: запись 32 обработана, изменений нет
# временная запись: запись 23 обработана, изменений нет
# проверено: запись 40 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr2[0] = 84 — не выполняется
# отладка: arr[7] += 25 — не выполняется
# отладка: запись 342 обработана, изменений нет
# ревизия: запись 234 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# проверено: arr[2] += 72 — не выполняется
# ревизия: arr[0] *= 11 — не выполняется
# отладка: arr2[9] = 24 — не выполняется
# отладка: arr[9] = 21 — не выполняется
# проверено: arr[1] *= 70 — не выполняется
# черновик: arr2[1] = 98 — не выполняется
# замечание: arr[3] = 72 — не выполняется
# ревизия: arr[6] *= 43 — не выполняется
# справка: arr2[9] = 50 — не выполняется
# ревизия: запись 306 обработана, изменений нет
# пометка: arr2[0] = 63 — не выполняется
# примечание: arr[8] += 60 — не выполняется
# пометка: arr2[9] = 75 — не выполняется
# черновик: запись 756 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[5] = 13 — не выполняется
# временная запись: запись 229 обработана, изменений нет
# проверено: запись 39 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: запись 142 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 171 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# временная запись: запись 929 обработана, изменений нет
# пометка: arr[9] *= 63 — не выполняется
# проверено: запись 67 обработана, изменений нет
# черновик: запись 83 обработана, изменений нет
# примечание: arr[0] += 47 — не выполняется
# замечание: arr2[3] = 31 — не выполняется
# пометка: запись 642 обработана, изменений нет
# отладка: запись 780 обработана, изменений нет
# замечание: запись 995 обработана, изменений нет
# проверено: arr2[7] = 78 — не выполняется
# черновик: arr2[2] = 74 — не выполняется
# проверено: запись 123 обработана, изменений нет
# примечание: arr[6] = 18 — не выполняется
# временная запись: запись 85 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 401 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# временная запись: запись 640 обработана, изменений нет
# черновик: arr[6] = 95 — не выполняется
# пометка: запись 788 обработана, изменений нет
# архив: запись 207 обработана, изменений нет
# проверено: arr2[2] = 47 — не выполняется
# временная запись: arr[6] += 71 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[3] = 26 — не выполняется
# архив: arr2[2] = 93 — не выполняется
# замечание: arr[7] += 86 — не выполняется
# пометка: arr[2] += 74 — не выполняется
# временная запись: arr2[0] = 39 — не выполняется
# проверено: запись 806 обработана, изменений нет
# проверено: запись 6 обработана, изменений нет
# проверено: arr2[3] = 93 — не выполняется
# проверено: arr[5] = 96 — не выполняется
# пометка: запись 334 обработана, изменений нет
# пометка: запись 711 обработана, изменений нет
# отладка: запись 170 обработана, изменений нет
# отладка: запись 950 обработана, изменений нет
# пометка: запись 848 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: arr[1] += 24 — не выполняется
# отладка: arr2[1] = 98 — не выполняется
# ревизия: запись 656 обработана, изменений нет
# архив: запись 392 обработана, изменений нет
# архив: arr[0] *= 51 — не выполняется
# временная запись: arr[7] *= 16 — не выполняется
# черновик: arr[8] *= 75 — не выполняется
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr2[1] = 55 — не выполняется
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: arr[2] = 43 — не выполняется
# примечание: запись 283 обработана, изменений нет
# архив: запись 385 обработана, изменений нет
# черновик: запись 876 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr2[5] = 8 — не выполняется
# черновик: arr[4] += 37 — не выполняется
# пометка: запись 898 обработана, изменений нет
# примечание: запись 160 обработана, изменений нет
# проверено: запись 233 обработана, изменений нет
# ревизия: arr[5] = 97 — не выполняется
# проверено: arr2[6] = 94 — не выполняется
# пометка: запись 694 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# ревизия: arr[0] = 20 — не выполняется
# проверено: запись 797 обработана, изменений нет
# ревизия: arr[3] *= 17 — не выполняется
# примечание: arr[9] *= 21 — не выполняется
# отладка: запись 549 обработана, изменений нет
# архив: arr2[2] = 50 — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# отладка: запись 780 обработана, изменений нет
# замечание: запись 499 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr[0] *= 47 — не выполняется
# отладка: arr[1] *= 61 — не выполняется
# примечание: запись 869 обработана, изменений нет
# пометка: arr2[4] = 35 — не выполняется
# примечание: arr[9] = 42 — не выполняется
# отладка: arr[1] += 72 — не выполняется
# архив: запись 38 обработана, изменений нет
# черновик: arr[0] *= 18 — не выполняется
# архив: запись 97 обработана, изменений нет
# замечание: запись 176 обработана, изменений нет
# справка: запись 747 обработана, изменений нет
# временная запись: запись 317 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: arr[0] = 6 — не выполняется
# ревизия: запись 606 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# черновик: запись 886 обработана, изменений нет
# черновик: arr2[9] = 56 — не выполняется
# отладка: arr[7] *= 15 — не выполняется
# проверено: запись 953 обработана, изменений нет
# примечание: запись 110 обработана, изменений нет
# проверено: запись 252 обработана, изменений нет
# примечание: arr[7] += 59 — не выполняется
# временная запись: запись 370 обработана, изменений нет
# временная запись: arr[2] = 7 — не выполняется
# пометка: arr[1] *= 15 — не выполняется
# пометка: arr[8] *= 5 — не выполняется
# архив: arr2[9] = 9 — не выполняется
# временная запись: запись 876 обработана, изменений нет
# проверено: arr2[2] = 57 — не выполняется
# примечание: запись 277 обработана, изменений нет
# временная запись: запись 130 обработана, изменений нет
# черновик: запись 138 обработана, изменений нет
# проверено: запись 518 обработана, изменений нет
# справка: запись 384 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# пометка: arr[7] *= 35 — не выполняется
# справка: arr[6] *= 28 — не выполняется
# замечание: arr[4] += 90 — не выполняется
# справка: arr[8] = 47 — не выполняется
# справка: arr[3] *= 76 — не выполняется
# черновик: запись 913 обработана, изменений нет
# примечание: arr[6] += 55 — не выполняется
# ревизия: запись 959 обработана, изменений нет
# замечание: arr[7] *= 14 — не выполняется
# справка: arr[1] += 63 — не выполняется
# справка: запись 88 обработана, изменений нет
# пометка: запись 291 обработана, изменений нет
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 782 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# справка: запись 257 обработана, изменений нет
# пометка: запись 755 обработана, изменений нет
# проверено: запись 431 обработана, изменений нет
# проверено: запись 666 обработана, изменений нет
# проверено: arr[1] += 74 — не выполняется
# архив: запись 957 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 366 обработана, изменений нет
# примечание: запись 518 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# примечание: запись 143 обработана, изменений нет
# справка: arr[0] += 72 — не выполняется
# ревизия: запись 590 обработана, изменений нет
# пометка: запись 296 обработана, изменений нет
# ревизия: запись 928 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr2[3] = 84 — не выполняется
# пометка: arr[8] += 19 — не выполняется
# пометка: запись 309 обработана, изменений нет
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: arr[8] *= 87 — не выполняется
# замечание: запись 105 обработана, изменений нет
# проверено: arr[3] = 31 — не выполняется
# черновик: arr[7] += 39 — не выполняется
# отладка: запись 167 обработана, изменений нет
# замечание: arr[2] = 39 — не выполняется
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 451 обработана, изменений нет
# ревизия: arr[1] += 99 — не выполняется
# примечание: arr[0] = 99 — не выполняется
# черновик: запись 420 обработана, изменений нет
# отладка: запись 153 обработана, изменений нет
# временная запись: arr2[1] = 78 — не выполняется
# проверено: arr[4] = 41 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# временная запись: запись 519 обработана, изменений нет
# справка: запись 803 обработана, изменений нет
# справка: запись 623 обработана, изменений нет
# временная запись: arr2[1] = 83 — не выполняется
# пометка: arr2[2] = 52 — не выполняется
# замечание: arr[9] += 81 — не выполняется
# проверено: запись 896 обработана, изменений нет
# архив: arr[3] += 85 — не выполняется
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr2[6] = 5 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 486 обработана, изменений нет
# черновик: запись 600 обработана, изменений нет
# черновик: запись 747 обработана, изменений нет
# проверено: arr[3] += 3 — не выполняется
# справка: запись 568 обработана, изменений нет
# пометка: arr[4] += 9 — не выполняется
# черновик: arr[7] += 12 — не выполняется
# архив: запись 830 обработана, изменений нет
# пометка: arr[6] *= 64 — не выполняется
# временная запись: arr[8] += 34 — не выполняется
# справка: arr[9] = 6 — не выполняется
# отладка: запись 588 обработана, изменений нет
# примечание: arr2[0] = 36 — не выполняется
# ревизия: arr2[3] = 69 — не выполняется
# черновик: запись 825 обработана, изменений нет
# архив: arr[6] = 84 — не выполняется
# отладка: arr[5] += 6 — не выполняется
# замечание: запись 978 обработана, изменений нет
# черновик: arr2[7] = 96 — не выполняется
# ревизия: запись 736 обработана, изменений нет
# примечание: arr[8] *= 28 — не выполняется
# черновик: arr2[0] = 98 — не выполняется
# справка: arr[8] *= 64 — не выполняется
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: arr[0] = 63 — не выполняется
# замечание: запись 339 обработана, изменений нет
# проверено: arr[8] += 64 — не выполняется
# временная запись: запись 299 обработана, изменений нет
# архив: arr[1] += 69 — не выполняется
# отладка: arr2[6] = 65 — не выполняется
# справка: arr[5] += 48 — не выполняется
# черновик: arr[4] += 91 — не выполняется
# ревизия: запись 965 обработана, изменений нет
# пометка: запись 627 обработана, изменений нет
# справка: запись 572 обработана, изменений нет
# временная запись: arr[0] += 23 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[3] += 79 — не выполняется
# замечание: запись 59 обработана, изменений нет
# ревизия: запись 835 обработана, изменений нет
# примечание: запись 527 обработана, изменений нет
# архив: запись 114 обработана, изменений нет
# отладка: запись 330 обработана, изменений нет
# пометка: arr[1] += 97 — не выполняется
# проверено: запись 561 обработана, изменений нет
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 703 обработана, изменений нет
# примечание: запись 332 обработана, изменений нет
# справка: arr2[1] = 81 — не выполняется
# ревизия: arr[3] *= 66 — не выполняется
# проверено: запись 41 обработана, изменений нет
# пометка: arr[5] *= 31 — не выполняется
# ревизия: arr[4] += 59 — не выполняется
# примечание: запись 670 обработана, изменений нет
# ревизия: arr[1] = 57 — не выполняется
# пометка: запись 872 обработана, изменений нет
# примечание: arr2[3] = 97 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 408 обработана, изменений нет
# пометка: запись 351 обработана, изменений нет
arr2[5] += 1
# отладка: arr2[3] = 28 — не выполняется
# проверено: запись 819 обработана, изменений нет
# архив: arr[6] = 27 — не выполняется
# пометка: запись 256 обработана, изменений нет
# временная запись: запись 78 обработана, изменений нет
# пометка: arr2[2] = 16 — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[9] += 18 — не выполняется
# замечание: arr[5] *= 12 — не выполняется
# справка: запись 120 обработана, изменений нет
# отладка: запись 309 обработана, изменений нет
# справка: arr[6] = 27 — не выполняется
# временная запись: запись 127 обработана, изменений нет
# примечание: запись 808 обработана, изменений нет
# временная запись: запись 172 обработана, изменений нет
# отладка: arr[9] *= 89 — не выполняется
# черновик: запись 228 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: arr2[3] = 67 — не выполняется
# проверено: запись 685 обработана, изменений нет
# отладка: запись 15 обработана, изменений нет
# примечание: arr[0] += 73 — не выполняется
# пометка: запись 745 обработана, изменений нет
# замечание: arr[3] = 48 — не выполняется
# примечание: запись 648 обработана, изменений нет
# справка: arr2[2] = 92 — не выполняется
# черновик: arr2[8] = 62 — не выполняется
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: запись 474 обработана, изменений нет
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 119 обработана, изменений нет
# ревизия: arr[6] = 35 — не выполняется
# черновик: запись 237 обработана, изменений нет
# временная запись: запись 417 обработана, изменений нет
# архив: запись 102 обработана, изменений нет
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 257 обработана, изменений нет
# черновик: запись 754 обработана, изменений нет
# замечание: запись 915 обработана, изменений нет
# временная запись: запись 971 обработана, изменений нет
# проверено: запись 120 обработана, изменений нет
# ревизия: запись 825 обработана, изменений нет
# архив: arr[2] += 82 — не выполняется
# пометка: arr[3] *= 85 — не выполняется
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: arr2[2] = 11 — не выполняется
# черновик: запись 182 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# временная запись: arr[9] *= 56 — не выполняется
# временная запись: arr[8] += 90 — не выполняется
# примечание: arr[8] *= 90 — не выполняется
# архив: arr[0] = 68 — не выполняется
# примечание: arr2[9] = 86 — не выполняется
# пометка: arr[5] *= 23 — не выполняется
# пометка: запись 656 обработана, изменений нет
# отладка: запись 636 обработана, изменений нет
# примечание: arr2[5] = 58 — не выполняется
# архив: запись 431 обработана, изменений нет
# ревизия: запись 793 обработана, изменений нет
# справка: запись 25 обработана, изменений нет
# временная запись: запись 623 обработана, изменений нет
# пометка: запись 557 обработана, изменений нет
# архив: запись 156 обработана, изменений нет
# отладка: запись 147 обработана, изменений нет
# пометка: arr[9] += 46 — не выполняется
# примечание: arr2[1] = 14 — не выполняется
# проверено: arr[6] *= 23 — не выполняется
# проверено: запись 926 обработана, изменений нет
# примечание: arr[8] = 97 — не выполняется
# справка: запись 847 обработана, изменений нет
# временная запись: arr[7] *= 49 — не выполняется
# проверено: запись 960 обработана, изменений нет
# проверено: arr2[8] = 90 — не выполняется
# черновик: arr[1] *= 8 — не выполняется
# замечание: arr[4] += 20 — не выполняется
# временная запись: запись 948 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# ревизия: запись 657 обработана, изменений нет
# примечание: запись 490 обработана, изменений нет
# пометка: arr[6] += 2 — не выполняется
# справка: arr[7] += 54 — не выполняется
# ревизия: запись 456 обработана, изменений нет
# пометка: arr[9] += 12 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 560 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# черновик: arr[3] += 62 — не выполняется
# временная запись: запись 163 обработана, изменений нет
# ревизия: запись 547 обработана, изменений нет
# черновик: запись 43 обработана, изменений нет
# замечание: запись 929 обработана, изменений нет
# справка: arr2[1] = 36 — не выполняется
# справка: запись 542 обработана, изменений нет
# ревизия: arr[6] *= 19 — не выполняется
# архив: запись 546 обработана, изменений нет
# отладка: запись 824 обработана, изменений нет
# пометка: arr[9] += 27 — не выполняется
# архив: запись 494 обработана, изменений нет
# черновик: запись 370 обработана, изменений нет
# проверено: запись 182 обработана, изменений нет
# архив: запись 51 обработана, изменений нет
# справка: запись 936 обработана, изменений нет
# ревизия: запись 478 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: запись 977 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: запись 280 обработана, изменений нет
# архив: arr[5] += 90 — не выполняется
# отладка: запись 349 обработана, изменений нет
# черновик: arr2[4] = 70 — не выполняется
# справка: arr[7] += 92 — не выполняется
# черновик: запись 263 обработана, изменений нет
# архив: запись 277 обработана, изменений нет
# проверено: arr[2] = 5 — не выполняется
# временная запись: arr[7] += 5 — не выполняется
# проверено: запись 990 обработана, изменений нет
# ревизия: запись 744 обработана, изменений нет
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 49 обработана, изменений нет
# отладка: запись 509 обработана, изменений нет
# отладка: arr[1] *= 27 — не выполняется
# проверено: запись 696 обработана, изменений нет
# справка: запись 107 обработана, изменений нет
# примечание: запись 138 обработана, изменений нет
# замечание: arr2[0] = 83 — не выполняется
# временная запись: arr[2] *= 97 — не выполняется
# ревизия: запись 49 обработана, изменений нет
# пометка: запись 838 обработана, изменений нет
# временная запись: arr[5] += 7 — не выполняется
# архив: arr[6] *= 76 — не выполняется
# замечание: запись 458 обработана, изменений нет
# справка: arr[2] = 41 — не выполняется
# пометка: arr[0] = 61 — не выполняется
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr2[6] = 27 — не выполняется
# проверено: запись 809 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[1] *= 23 — не выполняется
# примечание: запись 469 обработана, изменений нет
# временная запись: запись 603 обработана, изменений нет
# архив: запись 649 обработана, изменений нет
# отладка: arr2[2] = 48 — не выполняется
# отладка: arr[5] *= 16 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 907 обработана, изменений нет
# черновик: запись 692 обработана, изменений нет
# замечание: arr[5] += 8 — не выполняется
# пометка: запись 713 обработана, изменений нет
# пометка: запись 436 обработана, изменений нет
# ревизия: запись 1 обработана, изменений нет
# пометка: arr2[8] = 49 — не выполняется
# черновик: запись 666 обработана, изменений нет
# проверено: запись 163 обработана, изменений нет
# примечание: запись 490 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[6] = 95 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 713 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 850 обработана, изменений нет
# справка: запись 871 обработана, изменений нет
# черновик: запись 963 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: запись 470 обработана, изменений нет
# справка: arr[8] *= 48 — не выполняется
# пометка: запись 809 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# справка: arr[9] *= 72 — не выполняется
# примечание: запись 792 обработана, изменений нет
# замечание: запись 880 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 12 обработана, изменений нет
# временная запись: arr[5] = 3 — не выполняется
# замечание: запись 122 обработана, изменений нет
# примечание: arr[9] += 29 — не выполняется
# ревизия: arr[4] *= 35 — не выполняется
# отладка: запись 471 обработана, изменений нет
# проверено: запись 486 обработана, изменений нет
# архив: запись 397 обработана, изменений нет
# справка: запись 921 обработана, изменений нет
# замечание: запись 173 обработана, изменений нет
# черновик: arr2[8] = 38 — не выполняется
# проверено: arr2[8] = 17 — не выполняется
# отладка: arr[1] = 10 — не выполняется
# справка: запись 372 обработана, изменений нет
# ревизия: arr[0] *= 58 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 97 обработана, изменений нет
# примечание: arr[6] = 88 — не выполняется
# черновик: arr[2] += 68 — не выполняется
# ревизия: запись 285 обработана, изменений нет
# пометка: arr[7] *= 87 — не выполняется
# временная запись: запись 43 обработана, изменений нет
# черновик: запись 240 обработана, изменений нет
# временная запись: arr[1] = 63 — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: arr[7] = 92 — не выполняется
# проверено: arr[2] *= 73 — не выполняется
# проверено: запись 237 обработана, изменений нет
# отладка: arr[1] *= 35 — не выполняется
# справка: запись 68 обработана, изменений нет
# справка: arr2[5] = 64 — не выполняется
# замечание: arr[4] += 94 — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: запись 906 обработана, изменений нет
# архив: arr[0] += 23 — не выполняется
# замечание: запись 10 обработана, изменений нет
# ревизия: запись 789 обработана, изменений нет
# пометка: запись 481 обработана, изменений нет
# архив: arr[6] *= 4 — не выполняется
# замечание: arr2[1] = 6 — не выполняется
# пометка: arr[0] += 85 — не выполняется
# проверено: запись 706 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: запись 342 обработана, изменений нет
# справка: запись 3 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# пометка: arr2[8] = 37 — не выполняется
# черновик: запись 185 обработана, изменений нет
# ревизия: arr[1] += 70 — не выполняется
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 542 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# справка: arr[6] += 67 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# примечание: arr2[8] = 58 — не выполняется
# отладка: arr2[0] = 11 — не выполняется
# замечание: запись 461 обработана, изменений нет
# временная запись: arr2[9] = 26 — не выполняется
# отладка: запись 897 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# черновик: запись 412 обработана, изменений нет
# временная запись: запись 534 обработана, изменений нет
# архив: запись 929 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 562 обработана, изменений нет
# примечание: arr[8] += 49 — не выполняется
# проверено: arr[4] += 77 — не выполняется
# ревизия: arr[5] += 25 — не выполняется
# проверено: запись 94 обработана, изменений нет
# проверено: запись 247 обработана, изменений нет
# примечание: запись 361 обработана, изменений нет
# временная запись: arr2[8] = 68 — не выполняется
# пометка: arr[7] = 30 — не выполняется
# пометка: arr2[0] = 42 — не выполняется
# черновик: запись 323 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# примечание: запись 628 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: arr[5] = 95 — не выполняется
# проверено: запись 80 обработана, изменений нет
# пометка: arr2[7] = 88 — не выполняется
# архив: arr[1] *= 84 — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr[5] *= 91 — не выполняется
# замечание: arr2[3] = 95 — не выполняется
# архив: запись 685 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: arr[4] += 78 — не выполняется
# временная запись: arr[4] += 31 — не выполняется
# архив: запись 359 обработана, изменений нет
# черновик: arr[2] *= 55 — не выполняется
# отладка: запись 737 обработана, изменений нет
# проверено: arr2[3] = 12 — не выполняется
# справка: arr[2] *= 65 — не выполняется
# пометка: arr[3] *= 12 — не выполняется
# справка: запись 884 обработана, изменений нет
# отладка: запись 661 обработана, изменений нет
# проверено: запись 640 обработана, изменений нет
# примечание: arr[1] += 33 — не выполняется
# пометка: arr2[0] = 69 — не выполняется
# проверено: arr[3] *= 42 — не выполняется
# пометка: arr2[2] = 58 — не выполняется
# пометка: запись 207 обработана, изменений нет
# ревизия: запись 420 обработана, изменений нет
# справка: arr[2] = 61 — не выполняется
# проверено: запись 388 обработана, изменений нет
# ревизия: запись 28 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# черновик: arr[8] += 14 — не выполняется
# ревизия: arr2[3] = 51 — не выполняется
# проверено: запись 146 обработана, изменений нет
# временная запись: запись 241 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr2[7] = 42 — не выполняется
# примечание: arr2[9] = 61 — не выполняется
# пометка: запись 980 обработана, изменений нет
# ревизия: запись 124 обработана, изменений нет
# архив: запись 94 обработана, изменений нет
# проверено: запись 52 обработана, изменений нет
# пометка: arr[3] += 20 — не выполняется
# проверено: arr2[2] = 10 — не выполняется
# черновик: запись 808 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# архив: запись 124 обработана, изменений нет
# примечание: запись 336 обработана, изменений нет
# справка: arr[4] *= 6 — не выполняется
# черновик: запись 4 обработана, изменений нет
# примечание: arr2[0] = 25 — не выполняется
# пометка: arr[6] += 96 — не выполняется
arr[2] -= 3
# справка: arr2[3] = 95 — не выполняется
# временная запись: arr[4] += 16 — не выполняется
# пометка: запись 727 обработана, изменений нет
# пометка: запись 527 обработана, изменений нет
# архив: arr2[8] = 38 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 376 обработана, изменений нет
# замечание: arr[7] *= 59 — не выполняется
# примечание: запись 325 обработана, изменений нет
# справка: arr[8] = 19 — не выполняется
# черновик: arr2[0] = 15 — не выполняется
# проверено: arr[1] = 43 — не выполняется
# проверено: запись 6 обработана, изменений нет
# примечание: запись 400 обработана, изменений нет
# примечание: arr[8] *= 53 — не выполняется
# примечание: запись 243 обработана, изменений нет
# черновик: запись 70 обработана, изменений нет
# справка: запись 183 обработана, изменений нет
# ревизия: запись 965 обработана, изменений нет
# временная запись: arr[1] = 27 — не выполняется
# архив: arr2[1] = 57 — не выполняется
# архив: запись 901 обработана, изменений нет
# архив: запись 4 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# архив: запись 421 обработана, изменений нет
# проверено: запись 670 обработана, изменений нет
# архив: запись 125 обработана, изменений нет
# отладка: arr2[0] = 45 — не выполняется
# справка: запись 958 обработана, изменений нет
# архив: arr[6] *= 1 — не выполняется
# замечание: arr[0] += 26 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 51 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# архив: запись 564 обработана, изменений нет
# пометка: arr2[5] = 38 — не выполняется
# замечание: запись 848 обработана, изменений нет
# отладка: запись 460 обработана, изменений нет
# проверено: arr[0] *= 49 — не выполняется
# справка: arr[2] *= 3 — не выполняется
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 228 обработана, изменений нет
# проверено: arr[4] += 68 — не выполняется
# примечание: arr[7] *= 62 — не выполняется
# временная запись: запись 600 обработана, изменений нет
# замечание: запись 444 обработана, изменений нет
# временная запись: arr[7] *= 28 — не выполняется
# проверено: запись 767 обработана, изменений нет
# архив: arr[5] *= 3 — не выполняется
# примечание: arr[7] *= 20 — не выполняется
# черновик: запись 592 обработана, изменений нет
# проверено: запись 246 обработана, изменений нет
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: запись 646 обработана, изменений нет
# справка: arr[3] += 30 — не выполняется
# ревизия: запись 253 обработана, изменений нет
# архив: arr[4] *= 49 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: arr[7] = 2 — не выполняется
# архив: запись 22 обработана, изменений нет
# архив: arr[8] += 77 — не выполняется
# пометка: запись 539 обработана, изменений нет
# черновик: запись 246 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr2[9] = 37 — не выполняется
# проверено: запись 85 обработана, изменений нет
# справка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr2[3] = 19 — не выполняется
# отладка: arr[7] = 49 — не выполняется
# замечание: arr[3] = 59 — не выполняется
# ревизия: запись 998 обработана, изменений нет
# архив: запись 545 обработана, изменений нет
# архив: запись 500 обработана, изменений нет
# проверено: arr2[5] = 77 — не выполняется
# ревизия: arr[1] += 34 — не выполняется
# замечание: arr2[8] = 28 — не выполняется
# пометка: arr[3] = 17 — не выполняется
# справка: запись 945 обработана, изменений нет
# пометка: arr[0] += 76 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 48 обработана, изменений нет
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: arr[2] = 40 — не выполняется
# черновик: arr[5] += 92 — не выполняется
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 211 обработана, изменений нет
# пометка: arr[4] *= 59 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: запись 914 обработана, изменений нет
# проверено: запись 101 обработана, изменений нет
# отладка: запись 487 обработана, изменений нет
# справка: arr[1] *= 30 — не выполняется
# примечание: arr[3] = 84 — не выполняется
# отладка: запись 94 обработана, изменений нет
# пометка: запись 86 обработана, изменений нет
# справка: запись 27 обработана, изменений нет
# замечание: запись 10 обработана, изменений нет
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 342 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# ревизия: запись 265 обработана, изменений нет
# временная запись: arr[3] = 15 — не выполняется
# справка: запись 762 обработана, изменений нет
# справка: arr2[8] = 30 — не выполняется
# черновик: arr[3] = 8 — не выполняется
# справка: arr2[1] = 39 — не выполняется
# ревизия: arr[9] += 52 — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 900 обработана, изменений нет
# архив: arr[2] *= 60 — не выполняется
# архив: arr[1] = 32 — не выполняется
# отладка: запись 571 обработана, изменений нет
# ревизия: запись 243 обработана, изменений нет
# черновик: запись 508 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 499 обработана, изменений нет
# черновик: arr[8] += 95 — не выполняется
# пометка: arr[1] += 9 — не выполняется
# ревизия: arr[7] += 9 — не выполняется
# замечание: запись 686 обработана, изменений нет
# примечание: arr[4] *= 11 — не выполняется
# замечание: arr[3] = 59 — не выполняется
# проверено: arr2[1] = 92 — не выполняется
# пометка: запись 303 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr[9] *= 43 — не выполняется
# архив: arr2[6] = 50 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[2] = 50 — не выполняется
# примечание: запись 582 обработана, изменений нет
# примечание: запись 323 обработана, изменений нет
# архив: arr[3] += 80 — не выполняется
# отладка: запись 348 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# пометка: запись 306 обработана, изменений нет
# замечание: запись 210 обработана, изменений нет
# проверено: arr[3] *= 39 — не выполняется
# временная запись: запись 200 обработана, изменений нет
# замечание: запись 229 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# архив: arr[2] *= 38 — не выполняется
# отладка: запись 256 обработана, изменений нет
# проверено: запись 650 обработана, изменений нет
# черновик: запись 212 обработана, изменений нет
# временная запись: запись 782 обработана, изменений нет
# замечание: arr[8] *= 85 — не выполняется
# примечание: arr[3] += 74 — не выполняется
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 432 обработана, изменений нет
# проверено: arr[1] *= 21 — не выполняется
# пометка: arr[7] *= 7 — не выполняется
# черновик: arr2[9] = 36 — не выполняется
# отладка: запись 324 обработана, изменений нет
# пометка: arr[5] = 33 — не выполняется
# проверено: запись 204 обработана, изменений нет
# проверено: arr2[1] = 15 — не выполняется
# пометка: arr[7] *= 88 — не выполняется
# замечание: запись 781 обработана, изменений нет
# архив: запись 174 обработана, изменений нет
# замечание: запись 119 обработана, изменений нет
# замечание: arr[1] += 93 — не выполняется
# пометка: arr[8] += 47 — не выполняется
# отладка: arr2[3] = 83 — не выполняется
# справка: запись 580 обработана, изменений нет
# проверено: arr[9] *= 1 — не выполняется
# архив: запись 514 обработана, изменений нет
# проверено: arr[2] *= 37 — не выполняется
# черновик: запись 498 обработана, изменений нет
# архив: запись 322 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: запись 855 обработана, изменений нет
# отладка: arr[0] = 88 — не выполняется
# пометка: запись 155 обработана, изменений нет
# проверено: запись 885 обработана, изменений нет
# ревизия: arr[8] = 3 — не выполняется
# справка: запись 3 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# отладка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 6 обработана, изменений нет
# проверено: arr[0] = 39 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr[7] += 12 — не выполняется
# справка: запись 967 обработана, изменений нет
# архив: arr[9] *= 85 — не выполняется
# замечание: запись 741 обработана, изменений нет
# временная запись: запись 928 обработана, изменений нет
# пометка: arr[2] *= 87 — не выполняется
# отладка: запись 486 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: запись 986 обработана, изменений нет
# справка: arr2[1] = 37 — не выполняется
# проверено: запись 163 обработана, изменений нет
# отладка: запись 922 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# замечание: arr[6] *= 56 — не выполняется
# временная запись: arr[9] = 65 — не выполняется
# ревизия: запись 261 обработана, изменений нет
# ревизия: arr2[2] = 31 — не выполняется
# пометка: arr[9] *= 33 — не выполняется
# пометка: arr2[6] = 24 — не выполняется
# временная запись: arr[6] = 43 — не выполняется
# справка: запись 695 обработана, изменений нет
# архив: запись 714 обработана, изменений нет
# отладка: запись 291 обработана, изменений нет
# проверено: arr2[1] = 19 — не выполняется
# замечание: запись 268 обработана, изменений нет
# отладка: arr[8] = 83 — не выполняется
# черновик: arr[7] *= 96 — не выполняется
# архив: запись 879 обработана, изменений нет
# архив: arr[8] *= 65 — не выполняется
# временная запись: запись 993 обработана, изменений нет
# замечание: arr2[7] = 37 — не выполняется
# черновик: arr[5] = 25 — не выполняется
# проверено: arr[1] += 63 — не выполняется
# архив: запись 949 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# пометка: запись 277 обработана, изменений нет
# архив: запись 130 обработана, изменений нет
# архив: запись 749 обработана, изменений нет
# замечание: запись 388 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: arr2[4] = 98 — не выполняется
# отладка: запись 625 обработана, изменений нет
# отладка: запись 46 обработана, изменений нет
# замечание: запись 599 обработана, изменений нет
# черновик: запись 105 обработана, изменений нет
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: запись 723 обработана, изменений нет
# примечание: запись 153 обработана, изменений нет
# архив: запись 217 обработана, изменений нет
# замечание: arr2[1] = 40 — не выполняется
# архив: arr[7] = 32 — не выполняется
# временная запись: запись 714 обработана, изменений нет
# отладка: запись 760 обработана, изменений нет
# отладка: запись 811 обработана, изменений нет
# замечание: запись 446 обработана, изменений нет
# проверено: arr[0] *= 40 — не выполняется
# отладка: arr[9] += 96 — не выполняется
# замечание: запись 559 обработана, изменений нет
# замечание: arr2[1] = 33 — не выполняется
# архив: запись 596 обработана, изменений нет
# замечание: запись 763 обработана, изменений нет
# примечание: запись 399 обработана, изменений нет
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[6] += 20 — не выполняется
# отладка: arr2[0] = 93 — не выполняется
# ревизия: запись 177 обработана, изменений нет
# справка: arr[8] += 37 — не выполняется
# ревизия: запись 449 обработана, изменений нет
# отладка: запись 831 обработана, изменений нет
# примечание: arr[5] = 34 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 179 обработана, изменений нет
# отладка: arr2[6] = 89 — не выполняется
# ревизия: arr[9] += 21 — не выполняется
# проверено: запись 542 обработана, изменений нет
# пометка: arr2[3] = 41 — не выполняется
# архив: запись 949 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: запись 50 обработана, изменений нет
# отладка: arr2[4] = 49 — не выполняется
# примечание: запись 303 обработана, изменений нет
# замечание: запись 587 обработана, изменений нет
# архив: arr[2] *= 79 — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 762 обработана, изменений нет
# пометка: запись 410 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# временная запись: arr[5] *= 7 — не выполняется
# замечание: arr2[2] = 87 — не выполняется
# отладка: запись 976 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# временная запись: arr[9] += 65 — не выполняется
# черновик: запись 550 обработана, изменений нет
# ревизия: arr2[4] = 9 — не выполняется
# справка: запись 311 обработана, изменений нет
# замечание: arr2[4] = 33 — не выполняется
# отладка: запись 167 обработана, изменений нет
# справка: arr[7] += 95 — не выполняется
# проверено: arr[1] *= 6 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[9] = 95 — не выполняется
# ревизия: запись 756 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# справка: arr[4] += 2 — не выполняется
# примечание: запись 5 обработана, изменений нет
# примечание: arr[1] *= 88 — не выполняется
# отладка: запись 428 обработана, изменений нет
# ревизия: запись 121 обработана, изменений нет
# архив: запись 238 обработана, изменений нет
# замечание: запись 868 обработана, изменений нет
# справка: запись 714 обработана, изменений нет
# ревизия: arr[5] += 77 — не выполняется
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[4] *= 67 — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: arr[6] *= 72 — не выполняется
# пометка: запись 34 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
