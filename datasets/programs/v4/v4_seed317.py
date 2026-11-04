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
arr2[7] = 59
arr[4] *= 27
arr2[5] = 5
arr[6], arr[5] = arr[5], arr[6]
arr[3] *= 54
arr[0] = 49
arr[7] = 45
arr[2] = 39
"""

TRAP_0 = "arr[7] = 653"
TRAP_1 = "arr[7] = 943"
TRAP_2 = "arr[4] = 260"
TRAP_3 = "arr[1] = 769"
TRAP_4 = "arr[5] = 839"
TRAP_5 = "arr[3] = 706"
TRAP_6 = "arr[1] = 319"
TRAP_7 = "arr[4] = 465"
TRAP_8 = "arr[0] = 164"
TRAP_9 = "arr[4] = 288"
TRAP_10 = "arr[7] = 750"
TRAP_11 = "arr[7] = 950"
TRAP_12 = "arr[1] = 759"
TRAP_13 = "arr[6] = 455"
TRAP_14 = "arr[7] = 170"
TRAP_15 = "arr[0] = 824"
TRAP_16 = "arr[6] = 224"
TRAP_17 = "arr[2] = 460"
TRAP_18 = "arr[8] = 809"
TRAP_19 = "arr[2] = 842"
TRAP_20 = "arr[3] = 130"
TRAP_21 = "arr[3] = 888"
TRAP_22 = "arr[6] = 756"
TRAP_23 = "arr[9] = 917"
TRAP_24 = "arr[2] = 813"
TRAP_25 = "arr[9] = 102"
TRAP_26 = "arr[5] = 626"
TRAP_27 = "arr[8] = 523"
TRAP_28 = "arr[1] = 335"
TRAP_29 = "arr[5] = 951"
TRAP_30 = "arr[5] = 406"
TRAP_31 = "arr[3] = 530"
TRAP_32 = "arr[8] = 923"
TRAP_33 = "arr[1] = 744"
TRAP_34 = "arr[4] = 147"
TRAP_35 = "arr[8] = 611"
TRAP_36 = "arr[0] = 226"
TRAP_37 = "arr[4] = 171"
TRAP_38 = "arr[6] = 458"
TRAP_39 = "arr[4] = 556"
TRAP_40 = "arr[0] = 203"
TRAP_41 = "arr[7] = 904"
TRAP_42 = "arr[4] = 140"
TRAP_43 = "arr[6] = 342"
TRAP_44 = "arr[0] = 463"
TRAP_45 = "arr[2] = 320"
TRAP_46 = "arr[2] = 258"
TRAP_47 = "arr[5] = 714"
TRAP_48 = "arr[9] = 744"
TRAP_49 = "arr[3] = 767"
TRAP_50 = "arr[9] = 910"
TRAP_51 = "arr[4] = 289"
TRAP_52 = "arr[8] = 385"
TRAP_53 = "arr[7] = 442"
TRAP_54 = "arr[9] = 826"
TRAP_55 = "arr[5] = 181"
TRAP_56 = "arr[1] = 547"
TRAP_57 = "arr[7] = 914"
TRAP_58 = "arr[9] = 115"
TRAP_59 = "arr[4] = 378"
TRAP_60 = "arr[3] = 921"
TRAP_61 = "arr[8] = 153"
TRAP_62 = "arr[0] = 450"
TRAP_63 = "arr[0] = 309"
TRAP_64 = "arr[5] = 445"
TRAP_65 = "arr[5] = 629"
TRAP_66 = "arr[1] = 169"
TRAP_67 = "arr[8] = 870"
TRAP_68 = "arr[4] = 271"
TRAP_69 = "arr[5] = 641"
TRAP_70 = "arr[4] = 294"
TRAP_71 = "arr[1] = 430"
TRAP_72 = "arr[2] = 501"
TRAP_73 = "arr[1] = 893"
TRAP_74 = "arr[0] = 645"
TRAP_75 = "arr[3] = 500"
TRAP_76 = "arr[9] = 759"
TRAP_77 = "arr[6] = 697"
TRAP_78 = "arr[3] = 273"
TRAP_79 = "arr[0] = 833"
TRAP_80 = "arr[2] = 705"
TRAP_81 = "arr[6] = 585"
TRAP_82 = "arr[7] = 930"
TRAP_83 = "arr[2] = 690"
TRAP_84 = "arr[8] = 379"
TRAP_85 = "arr[4] = 807"
TRAP_86 = "arr[8] = 680"
TRAP_87 = "arr[9] = 558"
TRAP_88 = "arr[2] = 964"
TRAP_89 = "arr[3] = 222"
TRAP_90 = "arr[9] = 214"
TRAP_91 = "arr[4] = 185"
TRAP_92 = "arr[2] = 927"
TRAP_93 = "arr[2] = 169"
TRAP_94 = "arr[8] = 170"
TRAP_95 = "arr[8] = 974"
TRAP_96 = "arr[2] = 824"
TRAP_97 = "arr[1] = 336"
TRAP_98 = "arr[8] = 181"
TRAP_99 = "arr[0] = 994"
TRAP_100 = "arr[8] = 903"
TRAP_101 = "arr[1] = 962"
TRAP_102 = "arr[7] = 219"
TRAP_103 = "arr[3] = 795"
TRAP_104 = "arr[6] = 890"
TRAP_105 = "arr[2] = 555"
TRAP_106 = "arr[6] = 195"
TRAP_107 = "arr[9] = 988"
TRAP_108 = "arr[2] = 544"
TRAP_109 = "arr[7] = 706"
TRAP_110 = "arr[2] = 253"
TRAP_111 = "arr[4] = 284"
TRAP_112 = "arr[6] = 265"
TRAP_113 = "arr[8] = 256"
TRAP_114 = "arr[2] = 422"
TRAP_115 = "arr[3] = 385"
TRAP_116 = "arr[4] = 216"
TRAP_117 = "arr[3] = 443"
TRAP_118 = "arr[0] = 426"
TRAP_119 = "arr[0] = 951"
TRAP_120 = "arr[7] = 868"
TRAP_121 = "arr[8] = 289"
TRAP_122 = "arr[5] = 774"
TRAP_123 = "arr[9] = 727"
TRAP_124 = "arr[6] = 642"
TRAP_125 = "arr[3] = 862"
TRAP_126 = "arr[5] = 835"
TRAP_127 = "arr[8] = 663"
TRAP_128 = "arr[4] = 740"
TRAP_129 = "arr[9] = 883"
TRAP_130 = "arr[9] = 370"
TRAP_131 = "arr[8] = 769"
TRAP_132 = "arr[3] = 457"
TRAP_133 = "arr[1] = 261"
TRAP_134 = "arr[0] = 212"
TRAP_135 = "arr[6] = 140"
TRAP_136 = "arr[3] = 891"
TRAP_137 = "arr[8] = 856"
TRAP_138 = "arr[6] = 849"
TRAP_139 = "arr[3] = 600"
TRAP_140 = "arr[5] = 927"
TRAP_141 = "arr[5] = 898"
TRAP_142 = "arr[2] = 803"
TRAP_143 = "arr[1] = 708"
TRAP_144 = "arr[7] = 509"
TRAP_145 = "arr[5] = 333"
TRAP_146 = "arr[8] = 520"
TRAP_147 = "arr[7] = 287"
TRAP_148 = "arr[1] = 171"
TRAP_149 = "arr[5] = 591"

arr = [15, 1, 23, 25, 13, 1, 7, 8, 18, 15]

note_0 = str(arr[6]) + str(arr[1])
note_1 = str(arr[8]) + str(arr[8])
code_2 = re.sub(r'[0-9]', '#', str(arr[8]))
label_3 = "запись 3 не применялась"
code_4 = re.sub(r'[0-9]', '#', str(arr[3]))
note_5 = str(arr[8]) + str(arr[3])
code_6 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_7 = arr[6] + 28
tmp_8 = arr[8] + 23
code_9 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_10 = arr[6] + 43
tmp_11 = arr[7] + 7
copy_12 = arr[0]
code_13 = re.sub(r'[0-9]', '#', str(arr[6]))
code_14 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_15 = arr[7] + 40
code_16 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_17 = arr[2] + 40
tmp_18 = arr[2] + 49
note_19 = str(arr[0]) + str(arr[8])
tmp_20 = arr[5] + 35
tmp_21 = arr[2] + 40
tmp_22 = arr[4] + 47
note_23 = str(arr[6]) + str(arr[7])
code_24 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_25 = arr[7] + 20
code_26 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_27 = arr[3] + 33
tmp_28 = arr[4] + 45
note_29 = str(arr[8]) + str(arr[7])
code_30 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_31 = arr[8] + 33
tmp_32 = arr[2] + 21
copy_33 = arr[9]
code_34 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_35 = arr[3] + 23
note_36 = str(arr[1]) + str(arr[1])
copy_37 = arr[4]
label_38 = "запись 38 не применялась"
tmp_39 = arr[4] + 10
copy_40 = arr[1]
code_41 = re.sub(r'[0-9]', '#', str(arr[7]))
note_42 = str(arr[6]) + str(arr[8])
code_43 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_44 = arr[9] + 12
tmp_45 = arr[0] + 48
tmp_46 = arr[5] + 1
tmp_47 = arr[1] + 9
tmp_48 = arr[9] + 39
tmp_49 = arr[3] + 14
code_50 = re.sub(r'[0-9]', '#', str(arr[9]))
code_51 = re.sub(r'[0-9]', '#', str(arr[1]))
code_52 = re.sub(r'[0-9]', '#', str(arr[3]))
note_53 = str(arr[4]) + str(arr[4])
copy_54 = arr[8]
tmp_55 = arr[4] + 42
code_56 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_57 = arr[8] + 8
copy_58 = arr[9]
tmp_59 = arr[0] + 21
code_60 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_61 = arr[4] + 2
code_62 = re.sub(r'[0-9]', '#', str(arr[6]))
label_63 = "запись 63 не применялась"
tmp_64 = arr[0] + 10
tmp_65 = arr[9] + 3
tmp_66 = arr[3] + 43
code_67 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_68 = arr[6] + 8
note_69 = str(arr[8]) + str(arr[5])
tmp_70 = arr[9] + 42
tmp_71 = arr[3] + 50
note_72 = str(arr[1]) + str(arr[4])
code_73 = re.sub(r'[0-9]', '#', str(arr[1]))
note_74 = str(arr[9]) + str(arr[5])
tmp_75 = arr[3] + 22
copy_76 = arr[2]
note_77 = str(arr[7]) + str(arr[9])
copy_78 = arr[4]
tmp_79 = arr[7] + 34
code_80 = re.sub(r'[0-9]', '#', str(arr[5]))
label_81 = "запись 81 не применялась"
copy_82 = arr[6]
note_83 = str(arr[4]) + str(arr[5])
label_84 = "запись 84 не применялась"
tmp_85 = arr[2] + 12
code_86 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_87 = arr[0] + 37
tmp_88 = arr[4] + 36
tmp_89 = arr[9] + 38
tmp_90 = arr[4] + 2
code_91 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_92 = arr[6] + 27
note_93 = str(arr[0]) + str(arr[8])
note_94 = str(arr[7]) + str(arr[7])
tmp_95 = arr[5] + 41
code_96 = re.sub(r'[0-9]', '#', str(arr[6]))
label_97 = "запись 97 не применялась"
note_98 = str(arr[5]) + str(arr[0])
code_99 = re.sub(r'[0-9]', '#', str(arr[5]))
code_100 = re.sub(r'[0-9]', '#', str(arr[0]))
code_101 = re.sub(r'[0-9]', '#', str(arr[4]))
code_102 = re.sub(r'[0-9]', '#', str(arr[3]))
code_103 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_104 = arr[2] + 42
note_105 = str(arr[8]) + str(arr[5])
note_106 = str(arr[6]) + str(arr[6])
tmp_107 = arr[9] + 35
tmp_108 = arr[0] + 48
tmp_109 = arr[4] + 2
tmp_110 = arr[3] + 35
tmp_111 = arr[7] + 31
tmp_112 = arr[9] + 28
label_113 = "запись 113 не применялась"
code_114 = re.sub(r'[0-9]', '#', str(arr[9]))
code_115 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_116 = arr[2] + 27
copy_117 = arr[6]
tmp_118 = arr[2] + 10
code_119 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_120 = arr[9]
tmp_121 = arr[7] + 25
code_122 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_123 = arr[2] + 30
copy_124 = arr[0]
note_125 = str(arr[0]) + str(arr[2])
copy_126 = arr[3]
copy_127 = arr[5]
note_128 = str(arr[5]) + str(arr[5])
note_129 = str(arr[8]) + str(arr[2])
note_130 = str(arr[0]) + str(arr[6])
copy_131 = arr[6]
note_132 = str(arr[9]) + str(arr[9])
copy_133 = arr[7]
tmp_134 = arr[4] + 34
tmp_135 = arr[5] + 35
label_136 = "запись 136 не применялась"
tmp_137 = arr[3] + 4
tmp_138 = arr[8] + 37
code_139 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_140 = arr[8] + 48
note_141 = str(arr[5]) + str(arr[3])
copy_142 = arr[7]
code_143 = re.sub(r'[0-9]', '#', str(arr[2]))
code_144 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_145 = arr[4] + 28
tmp_146 = arr[2] + 2
tmp_147 = arr[9] + 35
code_148 = re.sub(r'[0-9]', '#', str(arr[5]))
code_149 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_150 = arr[9] + 39
tmp_151 = arr[1] + 27
label_152 = "запись 152 не применялась"
label_153 = "запись 153 не применялась"
copy_154 = arr[2]
note_155 = str(arr[8]) + str(arr[1])
tmp_156 = arr[3] + 17
tmp_157 = arr[4] + 23
code_158 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_159 = arr[3]
code_160 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_161 = arr[6]
note_162 = str(arr[9]) + str(arr[6])
tmp_163 = arr[8] + 33
code_164 = re.sub(r'[0-9]', '#', str(arr[1]))
code_165 = re.sub(r'[0-9]', '#', str(arr[4]))
label_166 = "запись 166 не применялась"
code_167 = re.sub(r'[0-9]', '#', str(arr[3]))
code_168 = re.sub(r'[0-9]', '#', str(arr[7]))
code_169 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_170 = arr[6] + 23
label_171 = "запись 171 не применялась"
copy_172 = arr[5]
copy_173 = arr[2]
code_174 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_175 = arr[6] + 36
copy_176 = arr[9]
code_177 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_178 = arr[0] + 36
code_179 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_180 = arr[0] + 26
code_181 = re.sub(r'[0-9]', '#', str(arr[7]))
code_182 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_183 = arr[1] + 13
tmp_184 = arr[0] + 31
code_185 = re.sub(r'[0-9]', '#', str(arr[5]))
label_186 = "запись 186 не применялась"
label_187 = "запись 187 не применялась"
note_188 = str(arr[1]) + str(arr[6])
tmp_189 = arr[3] + 25
label_190 = "запись 190 не применялась"
note_191 = str(arr[8]) + str(arr[7])
tmp_192 = arr[6] + 34
copy_193 = arr[9]
tmp_194 = arr[4] + 6
tmp_195 = arr[4] + 21
label_196 = "запись 196 не применялась"
copy_197 = arr[6]
note_198 = str(arr[8]) + str(arr[8])
copy_199 = arr[8]
code_200 = re.sub(r'[0-9]', '#', str(arr[2]))
code_201 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_202 = arr[0] + 26
tmp_203 = arr[1] + 43
label_204 = "запись 204 не применялась"
code_205 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_206 = arr[5] + 3
label_207 = "запись 207 не применялась"
copy_208 = arr[4]
tmp_209 = arr[8] + 31
note_210 = str(arr[0]) + str(arr[0])
note_211 = str(arr[2]) + str(arr[9])
tmp_212 = arr[1] + 24
label_213 = "запись 213 не применялась"
tmp_214 = arr[7] + 46
tmp_215 = arr[8] + 38
label_216 = "запись 216 не применялась"
copy_217 = arr[3]
label_218 = "запись 218 не применялась"
note_219 = str(arr[2]) + str(arr[1])
copy_220 = arr[6]
tmp_221 = arr[5] + 3
tmp_222 = arr[4] + 21
copy_223 = arr[1]
note_224 = str(arr[1]) + str(arr[9])
code_225 = re.sub(r'[0-9]', '#', str(arr[5]))
code_226 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_227 = arr[9] + 20
code_228 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_229 = arr[8] + 41
note_230 = str(arr[4]) + str(arr[5])
tmp_231 = arr[9] + 18
label_232 = "запись 232 не применялась"
note_233 = str(arr[9]) + str(arr[3])
tmp_234 = arr[8] + 44
copy_235 = arr[4]
copy_236 = arr[1]
tmp_237 = arr[5] + 44
tmp_238 = arr[4] + 7
code_239 = re.sub(r'[0-9]', '#', str(arr[5]))
note_240 = str(arr[0]) + str(arr[8])
copy_241 = arr[9]
note_242 = str(arr[5]) + str(arr[1])
tmp_243 = arr[0] + 7
code_244 = re.sub(r'[0-9]', '#', str(arr[1]))
code_245 = re.sub(r'[0-9]', '#', str(arr[7]))
note_246 = str(arr[8]) + str(arr[9])
tmp_247 = arr[1] + 18
code_248 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_249 = arr[0] + 13
note_250 = str(arr[3]) + str(arr[4])
tmp_251 = arr[8] + 35
tmp_252 = arr[0] + 39
copy_253 = arr[6]
note_254 = str(arr[5]) + str(arr[5])
note_255 = str(arr[9]) + str(arr[8])
code_256 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_257 = arr[5] + 9
tmp_258 = arr[1] + 2
note_259 = str(arr[0]) + str(arr[6])
note_260 = str(arr[1]) + str(arr[8])
tmp_261 = arr[2] + 40
note_262 = str(arr[8]) + str(arr[7])
note_263 = str(arr[1]) + str(arr[7])
note_264 = str(arr[6]) + str(arr[8])
tmp_265 = arr[1] + 21
copy_266 = arr[1]
note_267 = str(arr[3]) + str(arr[3])
code_268 = re.sub(r'[0-9]', '#', str(arr[0]))
note_269 = str(arr[4]) + str(arr[0])
label_270 = "запись 270 не применялась"
code_271 = re.sub(r'[0-9]', '#', str(arr[0]))
note_272 = str(arr[9]) + str(arr[8])
tmp_273 = arr[4] + 6
code_274 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_275 = arr[4] + 8
tmp_276 = arr[6] + 11
tmp_277 = arr[3] + 34
label_278 = "запись 278 не применялась"
label_279 = "запись 279 не применялась"
note_280 = str(arr[6]) + str(arr[7])
tmp_281 = arr[9] + 47
copy_282 = arr[0]
note_283 = str(arr[7]) + str(arr[9])
note_284 = str(arr[2]) + str(arr[8])
code_285 = re.sub(r'[0-9]', '#', str(arr[7]))
note_286 = str(arr[8]) + str(arr[8])
copy_287 = arr[2]
label_288 = "запись 288 не применялась"
code_289 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_290 = arr[3] + 33
tmp_291 = arr[5] + 7
label_292 = "запись 292 не применялась"
label_293 = "запись 293 не применялась"
code_294 = re.sub(r'[0-9]', '#', str(arr[1]))
code_295 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_296 = arr[6] + 4
copy_297 = arr[6]
label_298 = "запись 298 не применялась"
label_299 = "запись 299 не применялась"
note_300 = str(arr[4]) + str(arr[1])
label_301 = "запись 301 не применялась"
code_302 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_303 = arr[8]
tmp_304 = arr[2] + 36
copy_305 = arr[2]
tmp_306 = arr[2] + 46
label_307 = "запись 307 не применялась"
note_308 = str(arr[4]) + str(arr[7])
code_309 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_310 = arr[6] + 32
tmp_311 = arr[9] + 41
note_312 = str(arr[0]) + str(arr[6])
code_313 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_314 = arr[3]
label_315 = "запись 315 не применялась"
note_316 = str(arr[4]) + str(arr[1])
tmp_317 = arr[5] + 15
tmp_318 = arr[7] + 21
tmp_319 = arr[0] + 24
code_320 = re.sub(r'[0-9]', '#', str(arr[1]))
note_321 = str(arr[6]) + str(arr[1])
tmp_322 = arr[4] + 50
label_323 = "запись 323 не применялась"
tmp_324 = arr[6] + 28
note_325 = str(arr[6]) + str(arr[9])
tmp_326 = arr[4] + 14
tmp_327 = arr[7] + 39
note_328 = str(arr[8]) + str(arr[2])
tmp_329 = arr[7] + 12
copy_330 = arr[0]
tmp_331 = arr[4] + 14
note_332 = str(arr[8]) + str(arr[5])
note_333 = str(arr[9]) + str(arr[0])
note_334 = str(arr[1]) + str(arr[7])
note_335 = str(arr[4]) + str(arr[9])
code_336 = re.sub(r'[0-9]', '#', str(arr[9]))
note_337 = str(arr[5]) + str(arr[4])
tmp_338 = arr[5] + 23
tmp_339 = arr[3] + 12
tmp_340 = arr[6] + 9
tmp_341 = arr[2] + 46
copy_342 = arr[4]
code_343 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_344 = arr[5] + 42
code_345 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_346 = arr[0]
code_347 = re.sub(r'[0-9]', '#', str(arr[6]))
label_348 = "запись 348 не применялась"
code_349 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_350 = arr[5]
note_351 = str(arr[9]) + str(arr[4])
copy_352 = arr[0]
code_353 = re.sub(r'[0-9]', '#', str(arr[1]))
note_354 = str(arr[8]) + str(arr[7])
code_355 = re.sub(r'[0-9]', '#', str(arr[1]))
code_356 = re.sub(r'[0-9]', '#', str(arr[2]))
note_357 = str(arr[8]) + str(arr[2])
copy_358 = arr[6]
tmp_359 = arr[1] + 15
code_360 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_361 = arr[9] + 5
note_362 = str(arr[4]) + str(arr[0])
note_363 = str(arr[9]) + str(arr[3])
tmp_364 = arr[2] + 38
tmp_365 = arr[1] + 5
code_366 = re.sub(r'[0-9]', '#', str(arr[5]))
code_367 = re.sub(r'[0-9]', '#', str(arr[1]))
label_368 = "запись 368 не применялась"
copy_369 = arr[9]
note_370 = str(arr[4]) + str(arr[0])
label_371 = "запись 371 не применялась"
note_372 = str(arr[6]) + str(arr[0])
copy_373 = arr[8]
label_374 = "запись 374 не применялась"
copy_375 = arr[2]
code_376 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_377 = arr[3]
label_378 = "запись 378 не применялась"
tmp_379 = arr[0] + 6
code_380 = re.sub(r'[0-9]', '#', str(arr[7]))
code_381 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_382 = arr[4] + 49
code_383 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_384 = arr[9] + 36
tmp_385 = arr[6] + 16
tmp_386 = arr[5] + 16
tmp_387 = arr[9] + 24
code_388 = re.sub(r'[0-9]', '#', str(arr[3]))
code_389 = re.sub(r'[0-9]', '#', str(arr[0]))
note_390 = str(arr[6]) + str(arr[7])
note_391 = str(arr[9]) + str(arr[3])
tmp_392 = arr[6] + 24
note_393 = str(arr[4]) + str(arr[8])
note_394 = str(arr[2]) + str(arr[3])
tmp_395 = arr[0] + 1
tmp_396 = arr[8] + 47
note_397 = str(arr[0]) + str(arr[5])
code_398 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_399 = arr[5]
tmp_400 = arr[4] + 6
tmp_401 = arr[7] + 17
tmp_402 = arr[1] + 4
tmp_403 = arr[8] + 3
copy_404 = arr[8]
note_405 = str(arr[2]) + str(arr[5])
code_406 = re.sub(r'[0-9]', '#', str(arr[5]))
note_407 = str(arr[6]) + str(arr[5])
code_408 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_409 = arr[2] + 28
tmp_410 = arr[9] + 34
code_411 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_412 = arr[4] + 7
copy_413 = arr[9]
tmp_414 = arr[6] + 12
tmp_415 = arr[1] + 11
copy_416 = arr[2]
tmp_417 = arr[9] + 41
note_418 = str(arr[0]) + str(arr[1])
note_419 = str(arr[7]) + str(arr[4])
code_420 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_421 = arr[2] + 50
code_422 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_423 = arr[4] + 40
copy_424 = arr[7]
code_425 = re.sub(r'[0-9]', '#', str(arr[6]))
code_426 = re.sub(r'[0-9]', '#', str(arr[0]))
code_427 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_428 = arr[9]
tmp_429 = arr[0] + 49
copy_430 = arr[5]
tmp_431 = arr[1] + 38
code_432 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_433 = arr[0] + 48
tmp_434 = arr[3] + 14
tmp_435 = arr[5] + 19
tmp_436 = arr[0] + 4
label_437 = "запись 437 не применялась"
code_438 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_439 = arr[6]
copy_440 = arr[7]
code_441 = re.sub(r'[0-9]', '#', str(arr[2]))
note_442 = str(arr[9]) + str(arr[1])
tmp_443 = arr[9] + 3
code_444 = re.sub(r'[0-9]', '#', str(arr[0]))
code_445 = re.sub(r'[0-9]', '#', str(arr[2]))
note_446 = str(arr[6]) + str(arr[8])
tmp_447 = arr[5] + 33
code_448 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_449 = arr[7] + 19
tmp_450 = arr[5] + 48
copy_451 = arr[5]
code_452 = re.sub(r'[0-9]', '#', str(arr[4]))
note_453 = str(arr[6]) + str(arr[7])
tmp_454 = arr[0] + 48
note_455 = str(arr[5]) + str(arr[4])
code_456 = re.sub(r'[0-9]', '#', str(arr[8]))
label_457 = "запись 457 не применялась"
note_458 = str(arr[1]) + str(arr[1])
code_459 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_460 = arr[5] + 7
tmp_461 = arr[0] + 1
label_462 = "запись 462 не применялась"
tmp_463 = arr[7] + 37
copy_464 = arr[9]
code_465 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_466 = arr[8]
copy_467 = arr[5]
copy_468 = arr[8]
note_469 = str(arr[1]) + str(arr[5])
copy_470 = arr[4]
label_471 = "запись 471 не применялась"
label_472 = "запись 472 не применялась"
note_473 = str(arr[3]) + str(arr[1])
code_474 = re.sub(r'[0-9]', '#', str(arr[7]))
note_475 = str(arr[6]) + str(arr[9])
note_476 = str(arr[9]) + str(arr[0])
note_477 = str(arr[1]) + str(arr[1])
code_478 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_479 = arr[4]
tmp_480 = arr[3] + 34
copy_481 = arr[3]
tmp_482 = arr[5] + 50
copy_483 = arr[0]
copy_484 = arr[4]
code_485 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_486 = arr[7] + 25
copy_487 = arr[1]
tmp_488 = arr[4] + 5
code_489 = re.sub(r'[0-9]', '#', str(arr[5]))
code_490 = re.sub(r'[0-9]', '#', str(arr[9]))
code_491 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_492 = arr[7] + 33
note_493 = str(arr[3]) + str(arr[3])
label_494 = "запись 494 не применялась"
note_495 = str(arr[0]) + str(arr[4])
tmp_496 = arr[4] + 27
note_497 = str(arr[4]) + str(arr[3])
label_498 = "запись 498 не применялась"
note_499 = str(arr[3]) + str(arr[5])
copy_500 = arr[3]
label_501 = "запись 501 не применялась"
tmp_502 = arr[1] + 31
copy_503 = arr[4]
tmp_504 = arr[4] + 24
tmp_505 = arr[0] + 1
code_506 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_507 = arr[8] + 18
note_508 = str(arr[2]) + str(arr[2])
label_509 = "запись 509 не применялась"
note_510 = str(arr[3]) + str(arr[4])
copy_511 = arr[1]
note_512 = str(arr[6]) + str(arr[1])
tmp_513 = arr[3] + 4
note_514 = str(arr[0]) + str(arr[5])
tmp_515 = arr[5] + 44
tmp_516 = arr[2] + 15
note_517 = str(arr[1]) + str(arr[3])
label_518 = "запись 518 не применялась"
code_519 = re.sub(r'[0-9]', '#', str(arr[3]))
label_520 = "запись 520 не применялась"
note_521 = str(arr[1]) + str(arr[3])
label_522 = "запись 522 не применялась"
tmp_523 = arr[4] + 13
note_524 = str(arr[2]) + str(arr[8])
code_525 = re.sub(r'[0-9]', '#', str(arr[4]))
note_526 = str(arr[6]) + str(arr[9])
code_527 = re.sub(r'[0-9]', '#', str(arr[9]))
label_528 = "запись 528 не применялась"
note_529 = str(arr[3]) + str(arr[8])
tmp_530 = arr[9] + 10
tmp_531 = arr[3] + 10
note_532 = str(arr[6]) + str(arr[7])
note_533 = str(arr[4]) + str(arr[8])
label_534 = "запись 534 не применялась"
label_535 = "запись 535 не применялась"
note_536 = str(arr[7]) + str(arr[9])
code_537 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_538 = arr[8] + 2
note_539 = str(arr[2]) + str(arr[7])
label_540 = "запись 540 не применялась"
tmp_541 = arr[5] + 7
tmp_542 = arr[7] + 7
tmp_543 = arr[3] + 42
tmp_544 = arr[7] + 10
copy_545 = arr[2]
note_546 = str(arr[5]) + str(arr[9])
tmp_547 = arr[2] + 7
note_548 = str(arr[2]) + str(arr[3])
code_549 = re.sub(r'[0-9]', '#', str(arr[5]))
label_550 = "запись 550 не применялась"
note_551 = str(arr[3]) + str(arr[0])
copy_552 = arr[9]
label_553 = "запись 553 не применялась"
note_554 = str(arr[8]) + str(arr[8])
code_555 = re.sub(r'[0-9]', '#', str(arr[8]))
code_556 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_557 = arr[5] + 16
tmp_558 = arr[0] + 43
tmp_559 = arr[1] + 47
code_560 = re.sub(r'[0-9]', '#', str(arr[7]))
note_561 = str(arr[9]) + str(arr[5])
tmp_562 = arr[7] + 12
note_563 = str(arr[2]) + str(arr[9])
note_564 = str(arr[6]) + str(arr[7])
copy_565 = arr[1]
note_566 = str(arr[3]) + str(arr[8])
code_567 = re.sub(r'[0-9]', '#', str(arr[2]))
note_568 = str(arr[3]) + str(arr[4])
tmp_569 = arr[5] + 30
code_570 = re.sub(r'[0-9]', '#', str(arr[6]))
note_571 = str(arr[3]) + str(arr[2])
tmp_572 = arr[3] + 37
code_573 = re.sub(r'[0-9]', '#', str(arr[0]))
note_574 = str(arr[9]) + str(arr[1])
label_575 = "запись 575 не применялась"
code_576 = re.sub(r'[0-9]', '#', str(arr[9]))
label_577 = "запись 577 не применялась"
tmp_578 = arr[1] + 23
code_579 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_580 = arr[5] + 16
code_581 = re.sub(r'[0-9]', '#', str(arr[6]))
code_582 = re.sub(r'[0-9]', '#', str(arr[5]))
code_583 = re.sub(r'[0-9]', '#', str(arr[1]))
note_584 = str(arr[2]) + str(arr[3])
copy_585 = arr[9]
tmp_586 = arr[2] + 30
tmp_587 = arr[7] + 49
tmp_588 = arr[1] + 22
tmp_589 = arr[8] + 31
note_590 = str(arr[4]) + str(arr[2])
copy_591 = arr[7]
tmp_592 = arr[5] + 29
tmp_593 = arr[0] + 19
tmp_594 = arr[2] + 18
tmp_595 = arr[6] + 18
code_596 = re.sub(r'[0-9]', '#', str(arr[1]))
note_597 = str(arr[0]) + str(arr[4])
code_598 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_599 = arr[9] + 40
code_600 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_601 = arr[8] + 34
copy_602 = arr[6]
tmp_603 = arr[9] + 33
tmp_604 = arr[3] + 24
tmp_605 = arr[5] + 40
tmp_606 = arr[7] + 22
tmp_607 = arr[0] + 47
label_608 = "запись 608 не применялась"
code_609 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_610 = arr[8] + 15
tmp_611 = arr[3] + 44
tmp_612 = arr[3] + 17
copy_613 = arr[4]
tmp_614 = arr[7] + 16
code_615 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_616 = arr[3]
tmp_617 = arr[1] + 40
tmp_618 = arr[4] + 22
code_619 = re.sub(r'[0-9]', '#', str(arr[6]))
note_620 = str(arr[6]) + str(arr[3])
label_621 = "запись 621 не применялась"
code_622 = re.sub(r'[0-9]', '#', str(arr[9]))
note_623 = str(arr[5]) + str(arr[4])
tmp_624 = arr[8] + 45
tmp_625 = arr[3] + 45
copy_626 = arr[8]
copy_627 = arr[2]
label_628 = "запись 628 не применялась"
tmp_629 = arr[4] + 31
label_630 = "запись 630 не применялась"
note_631 = str(arr[8]) + str(arr[6])
copy_632 = arr[4]
tmp_633 = arr[2] + 15
tmp_634 = arr[0] + 21
copy_635 = arr[2]
copy_636 = arr[0]
tmp_637 = arr[3] + 10
note_638 = str(arr[6]) + str(arr[8])
note_639 = str(arr[5]) + str(arr[0])
code_640 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_641 = arr[0] + 15
code_642 = re.sub(r'[0-9]', '#', str(arr[3]))
label_643 = "запись 643 не применялась"
note_644 = str(arr[1]) + str(arr[1])
tmp_645 = arr[4] + 2
copy_646 = arr[9]
note_647 = str(arr[0]) + str(arr[2])
note_648 = str(arr[2]) + str(arr[3])
note_649 = str(arr[6]) + str(arr[0])
tmp_650 = arr[1] + 6
tmp_651 = arr[4] + 4
label_652 = "запись 652 не применялась"
tmp_653 = arr[4] + 36
tmp_654 = arr[3] + 31
note_655 = str(arr[4]) + str(arr[6])
copy_656 = arr[8]
note_657 = str(arr[5]) + str(arr[5])
tmp_658 = arr[1] + 48
label_659 = "запись 659 не применялась"
code_660 = re.sub(r'[0-9]', '#', str(arr[4]))
code_661 = re.sub(r'[0-9]', '#', str(arr[2]))
label_662 = "запись 662 не применялась"
tmp_663 = arr[1] + 49
tmp_664 = arr[8] + 8
label_665 = "запись 665 не применялась"
tmp_666 = arr[8] + 16
note_667 = str(arr[2]) + str(arr[2])
note_668 = str(arr[6]) + str(arr[9])
code_669 = re.sub(r'[0-9]', '#', str(arr[1]))
code_670 = re.sub(r'[0-9]', '#', str(arr[0]))
code_671 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_672 = arr[6] + 44
tmp_673 = arr[0] + 40
code_674 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_675 = arr[0] + 48
code_676 = re.sub(r'[0-9]', '#', str(arr[3]))
code_677 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_678 = arr[7] + 6
tmp_679 = arr[9] + 40
label_680 = "запись 680 не применялась"
copy_681 = arr[9]
copy_682 = arr[0]
label_683 = "запись 683 не применялась"
note_684 = str(arr[9]) + str(arr[6])
copy_685 = arr[0]
tmp_686 = arr[9] + 50
note_687 = str(arr[3]) + str(arr[8])
note_688 = str(arr[5]) + str(arr[8])
label_689 = "запись 689 не применялась"
code_690 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_691 = arr[4]
tmp_692 = arr[9] + 50
copy_693 = arr[4]
copy_694 = arr[9]
tmp_695 = arr[2] + 30
label_696 = "запись 696 не применялась"
note_697 = str(arr[6]) + str(arr[0])
note_698 = str(arr[1]) + str(arr[5])
code_699 = re.sub(r'[0-9]', '#', str(arr[0]))
note_700 = str(arr[5]) + str(arr[2])
note_701 = str(arr[4]) + str(arr[8])
copy_702 = arr[9]
copy_703 = arr[0]
note_704 = str(arr[9]) + str(arr[1])
copy_705 = arr[5]
code_706 = re.sub(r'[0-9]', '#', str(arr[2]))
label_707 = "запись 707 не применялась"
code_708 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_709 = arr[0]
code_710 = re.sub(r'[0-9]', '#', str(arr[3]))
note_711 = str(arr[7]) + str(arr[7])
note_712 = str(arr[8]) + str(arr[3])
code_713 = re.sub(r'[0-9]', '#', str(arr[3]))
code_714 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_715 = arr[9]
copy_716 = arr[4]
code_717 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_718 = arr[2]
code_719 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_720 = arr[9]
tmp_721 = arr[6] + 50
tmp_722 = arr[5] + 41
tmp_723 = arr[0] + 48
note_724 = str(arr[9]) + str(arr[1])
copy_725 = arr[7]
note_726 = str(arr[2]) + str(arr[6])
note_727 = str(arr[9]) + str(arr[9])
note_728 = str(arr[0]) + str(arr[4])
tmp_729 = arr[9] + 12
tmp_730 = arr[0] + 7
tmp_731 = arr[2] + 16
code_732 = re.sub(r'[0-9]', '#', str(arr[4]))
label_733 = "запись 733 не применялась"
code_734 = re.sub(r'[0-9]', '#', str(arr[1]))
code_735 = re.sub(r'[0-9]', '#', str(arr[8]))
note_736 = str(arr[9]) + str(arr[2])
code_737 = re.sub(r'[0-9]', '#', str(arr[1]))
note_738 = str(arr[2]) + str(arr[8])
note_739 = str(arr[1]) + str(arr[1])
tmp_740 = arr[9] + 22
tmp_741 = arr[3] + 47
code_742 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_743 = arr[9]
code_744 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_745 = arr[0]
note_746 = str(arr[2]) + str(arr[2])
tmp_747 = arr[4] + 5
note_748 = str(arr[3]) + str(arr[1])
tmp_749 = arr[9] + 23
tmp_750 = arr[2] + 37
code_751 = re.sub(r'[0-9]', '#', str(arr[1]))
label_752 = "запись 752 не применялась"
tmp_753 = arr[9] + 36
label_754 = "запись 754 не применялась"
copy_755 = arr[6]
tmp_756 = arr[2] + 33
copy_757 = arr[3]
tmp_758 = arr[5] + 4
copy_759 = arr[6]
note_760 = str(arr[3]) + str(arr[1])
copy_761 = arr[6]
tmp_762 = arr[9] + 30
note_763 = str(arr[7]) + str(arr[4])
code_764 = re.sub(r'[0-9]', '#', str(arr[3]))
label_765 = "запись 765 не применялась"
note_766 = str(arr[7]) + str(arr[4])
tmp_767 = arr[4] + 8
code_768 = re.sub(r'[0-9]', '#', str(arr[0]))
note_769 = str(arr[9]) + str(arr[7])
tmp_770 = arr[7] + 22
copy_771 = arr[3]
tmp_772 = arr[6] + 34
copy_773 = arr[1]
note_774 = str(arr[5]) + str(arr[1])
copy_775 = arr[6]
code_776 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_777 = arr[0] + 23
note_778 = str(arr[0]) + str(arr[5])
code_779 = re.sub(r'[0-9]', '#', str(arr[3]))
code_780 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_781 = arr[4]
tmp_782 = arr[6] + 7
note_783 = str(arr[9]) + str(arr[4])
tmp_784 = arr[6] + 17
tmp_785 = arr[2] + 37
note_786 = str(arr[9]) + str(arr[5])
copy_787 = arr[1]
code_788 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_789 = arr[1] + 39
code_790 = re.sub(r'[0-9]', '#', str(arr[4]))
code_791 = re.sub(r'[0-9]', '#', str(arr[3]))
code_792 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_793 = arr[0] + 25
label_794 = "запись 794 не применялась"
note_795 = str(arr[9]) + str(arr[5])
tmp_796 = arr[4] + 15
note_797 = str(arr[3]) + str(arr[8])
tmp_798 = arr[1] + 37
note_799 = str(arr[2]) + str(arr[2])

arr.reverse()
# ревизия: запись 648 обработана, изменений нет
# справка: arr[5] = 26 — не выполняется
# замечание: запись 721 обработана, изменений нет
# пометка: запись 103 обработана, изменений нет
# ревизия: arr[0] *= 83 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 415 обработана, изменений нет
# отладка: arr[9] = 90 — не выполняется
# черновик: arr2[8] = 42 — не выполняется
# замечание: arr[2] += 38 — не выполняется
# ревизия: запись 886 обработана, изменений нет
# справка: arr[2] = 18 — не выполняется
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 358 обработана, изменений нет
# справка: запись 134 обработана, изменений нет
# справка: arr[3] = 88 — не выполняется
# ревизия: запись 428 обработана, изменений нет
# проверено: arr[6] += 32 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 103 обработана, изменений нет
# отладка: arr[8] *= 57 — не выполняется
# архив: запись 541 обработана, изменений нет
# примечание: запись 619 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# справка: запись 358 обработана, изменений нет
# ревизия: arr[3] *= 27 — не выполняется
# проверено: запись 705 обработана, изменений нет
# архив: arr2[2] = 65 — не выполняется
# справка: запись 128 обработана, изменений нет
# справка: arr[5] = 22 — не выполняется
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: arr[4] += 99 — не выполняется
# примечание: запись 721 обработана, изменений нет
# временная запись: arr2[8] = 78 — не выполняется
# примечание: запись 555 обработана, изменений нет
# отладка: arr[3] *= 49 — не выполняется
# отладка: запись 108 обработана, изменений нет
# замечание: arr2[3] = 26 — не выполняется
# отладка: запись 231 обработана, изменений нет
# замечание: запись 212 обработана, изменений нет
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# справка: запись 515 обработана, изменений нет
# черновик: arr[2] = 61 — не выполняется
# справка: запись 604 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# проверено: arr2[0] = 45 — не выполняется
# черновик: arr[5] += 4 — не выполняется
# отладка: запись 373 обработана, изменений нет
# примечание: arr2[7] = 85 — не выполняется
# временная запись: arr[3] *= 14 — не выполняется
# отладка: arr[3] = 38 — не выполняется
# временная запись: arr[3] += 57 — не выполняется
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 810 обработана, изменений нет
# примечание: arr[2] = 36 — не выполняется
# ревизия: arr[6] += 72 — не выполняется
# ревизия: запись 793 обработана, изменений нет
# черновик: arr2[3] = 61 — не выполняется
# архив: arr[6] += 57 — не выполняется
# справка: arr2[0] = 58 — не выполняется
# архив: запись 585 обработана, изменений нет
# пометка: arr[8] = 16 — не выполняется
# архив: запись 452 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: arr2[5] = 48 — не выполняется
# проверено: arr[3] = 56 — не выполняется
# примечание: запись 697 обработана, изменений нет
# отладка: arr[8] += 48 — не выполняется
# примечание: arr[4] += 13 — не выполняется
# замечание: запись 133 обработана, изменений нет
# пометка: запись 394 обработана, изменений нет
# черновик: arr[5] = 97 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[5] = 86 — не выполняется
# временная запись: запись 237 обработана, изменений нет
# справка: запись 930 обработана, изменений нет
# ревизия: arr[6] *= 76 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr2[7] = 65 — не выполняется
# черновик: arr[2] *= 56 — не выполняется
# пометка: запись 703 обработана, изменений нет
# черновик: arr[2] = 37 — не выполняется
# пометка: arr2[6] = 49 — не выполняется
# архив: arr[9] = 7 — не выполняется
# черновик: запись 371 обработана, изменений нет
# проверено: arr[6] = 96 — не выполняется
# отладка: arr[4] *= 41 — не выполняется
# черновик: запись 886 обработана, изменений нет
# примечание: запись 984 обработана, изменений нет
# примечание: запись 237 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# справка: запись 501 обработана, изменений нет
# пометка: arr[8] += 1 — не выполняется
# примечание: запись 867 обработана, изменений нет
# архив: arr[8] = 49 — не выполняется
# пометка: arr2[1] = 45 — не выполняется
# ревизия: arr[3] = 64 — не выполняется
# отладка: запись 283 обработана, изменений нет
# замечание: arr[6] = 69 — не выполняется
# пометка: arr2[1] = 4 — не выполняется
# замечание: запись 875 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# архив: запись 855 обработана, изменений нет
# временная запись: запись 537 обработана, изменений нет
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: arr2[2] = 33 — не выполняется
# временная запись: arr[1] += 16 — не выполняется
# отладка: arr[0] *= 81 — не выполняется
# проверено: arr[2] *= 86 — не выполняется
# проверено: запись 354 обработана, изменений нет
# примечание: запись 463 обработана, изменений нет
# черновик: arr2[9] = 77 — не выполняется
# черновик: arr[5] += 5 — не выполняется
# справка: запись 669 обработана, изменений нет
# ревизия: запись 20 обработана, изменений нет
# замечание: запись 70 обработана, изменений нет
# примечание: arr2[5] = 42 — не выполняется
# справка: запись 780 обработана, изменений нет
# примечание: arr[7] *= 76 — не выполняется
# справка: запись 806 обработана, изменений нет
# временная запись: запись 267 обработана, изменений нет
# отладка: arr[6] *= 30 — не выполняется
# замечание: запись 289 обработана, изменений нет
# черновик: запись 524 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# ревизия: запись 155 обработана, изменений нет
# замечание: arr[3] = 39 — не выполняется
# черновик: запись 131 обработана, изменений нет
# пометка: arr[6] += 28 — не выполняется
# отладка: arr[2] *= 50 — не выполняется
# черновик: arr[6] *= 12 — не выполняется
# замечание: запись 604 обработана, изменений нет
# проверено: запись 142 обработана, изменений нет
# примечание: arr[5] = 54 — не выполняется
# пометка: запись 911 обработана, изменений нет
# примечание: arr[0] += 60 — не выполняется
# пометка: запись 572 обработана, изменений нет
# отладка: запись 409 обработана, изменений нет
# примечание: запись 645 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 557 обработана, изменений нет
# пометка: запись 163 обработана, изменений нет
# замечание: arr2[4] = 80 — не выполняется
# примечание: запись 607 обработана, изменений нет
# примечание: arr2[5] = 16 — не выполняется
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 970 обработана, изменений нет
# справка: запись 471 обработана, изменений нет
# примечание: запись 69 обработана, изменений нет
# пометка: arr[2] = 8 — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[0] = 46 — не выполняется
# временная запись: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# проверено: запись 991 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[1] = 34 — не выполняется
# ревизия: arr2[4] = 84 — не выполняется
# пометка: запись 679 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 92 обработана, изменений нет
# временная запись: arr[4] = 25 — не выполняется
# проверено: запись 532 обработана, изменений нет
# примечание: arr[5] *= 30 — не выполняется
# отладка: arr[3] *= 71 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr2[4] = 65 — не выполняется
# примечание: запись 672 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# временная запись: запись 772 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# проверено: запись 76 обработана, изменений нет
# черновик: запись 606 обработана, изменений нет
# ревизия: запись 715 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# черновик: arr[5] = 21 — не выполняется
# проверено: запись 206 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# примечание: запись 905 обработана, изменений нет
# справка: arr[9] += 21 — не выполняется
# справка: запись 319 обработана, изменений нет
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# проверено: arr[6] += 2 — не выполняется
# отладка: запись 13 обработана, изменений нет
# ревизия: arr[9] = 60 — не выполняется
# замечание: запись 917 обработана, изменений нет
# ревизия: arr[7] = 22 — не выполняется
# справка: запись 586 обработана, изменений нет
# ревизия: arr[1] *= 59 — не выполняется
# справка: запись 909 обработана, изменений нет
# пометка: arr[9] *= 46 — не выполняется
# черновик: arr[8] = 81 — не выполняется
# черновик: запись 41 обработана, изменений нет
# ревизия: запись 77 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[6] = 59 — не выполняется
# проверено: запись 178 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# архив: запись 682 обработана, изменений нет
# проверено: запись 146 обработана, изменений нет
# ревизия: запись 829 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 771 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# отладка: запись 211 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# примечание: запись 98 обработана, изменений нет
# архив: arr2[2] = 66 — не выполняется
# черновик: запись 656 обработана, изменений нет
# замечание: запись 309 обработана, изменений нет
# черновик: arr2[6] = 83 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[5] *= 66 — не выполняется
# проверено: запись 320 обработана, изменений нет
# проверено: arr[8] *= 88 — не выполняется
# замечание: arr[1] += 91 — не выполняется
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: запись 927 обработана, изменений нет
# временная запись: запись 413 обработана, изменений нет
# пометка: arr[9] += 79 — не выполняется
# архив: запись 994 обработана, изменений нет
# замечание: запись 710 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# проверено: запись 447 обработана, изменений нет
# черновик: arr[6] += 56 — не выполняется
# пометка: arr[2] *= 72 — не выполняется
# примечание: запись 383 обработана, изменений нет
# справка: arr[4] = 41 — не выполняется
# справка: arr[3] = 24 — не выполняется
# архив: запись 162 обработана, изменений нет
# пометка: запись 1 обработана, изменений нет
# примечание: arr[1] *= 36 — не выполняется
# отладка: arr[4] = 10 — не выполняется
# отладка: запись 959 обработана, изменений нет
# примечание: arr[0] += 34 — не выполняется
# временная запись: запись 162 обработана, изменений нет
# проверено: arr[2] = 42 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 182 обработана, изменений нет
# черновик: запись 237 обработана, изменений нет
# черновик: запись 9 обработана, изменений нет
# архив: запись 643 обработана, изменений нет
# ревизия: запись 662 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: запись 673 обработана, изменений нет
# архив: запись 812 обработана, изменений нет
# архив: arr[8] *= 62 — не выполняется
# временная запись: запись 757 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# проверено: запись 798 обработана, изменений нет
# черновик: arr[6] += 28 — не выполняется
# черновик: запись 267 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: arr2[4] = 38 — не выполняется
# пометка: запись 946 обработана, изменений нет
# справка: запись 881 обработана, изменений нет
# пометка: arr[4] += 85 — не выполняется
# пометка: arr[0] *= 61 — не выполняется
# отладка: arr[9] += 55 — не выполняется
# примечание: arr[3] *= 48 — не выполняется
# временная запись: arr2[7] = 66 — не выполняется
# архив: запись 383 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# пометка: arr[5] = 31 — не выполняется
# временная запись: запись 153 обработана, изменений нет
# ревизия: arr2[8] = 44 — не выполняется
# пометка: запись 562 обработана, изменений нет
# пометка: запись 242 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 678 обработана, изменений нет
# временная запись: запись 638 обработана, изменений нет
# справка: запись 316 обработана, изменений нет
# пометка: запись 90 обработана, изменений нет
# временная запись: запись 282 обработана, изменений нет
# черновик: arr[8] = 98 — не выполняется
# ревизия: arr[0] *= 82 — не выполняется
# ревизия: запись 674 обработана, изменений нет
# справка: запись 710 обработана, изменений нет
# замечание: arr[2] = 64 — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr[7] += 5 — не выполняется
# архив: arr[9] *= 71 — не выполняется
# справка: запись 904 обработана, изменений нет
# пометка: запись 540 обработана, изменений нет
# замечание: arr2[6] = 97 — не выполняется
# архив: arr[0] *= 6 — не выполняется
# отладка: запись 970 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 623 обработана, изменений нет
# временная запись: arr[3] *= 62 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: запись 152 обработана, изменений нет
# ревизия: arr2[9] = 23 — не выполняется
# ревизия: запись 607 обработана, изменений нет
# черновик: arr[2] *= 5 — не выполняется
# ревизия: запись 848 обработана, изменений нет
# архив: запись 489 обработана, изменений нет
# проверено: arr2[6] = 75 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[4] *= 30 — не выполняется
# справка: arr[7] += 64 — не выполняется
# временная запись: запись 776 обработана, изменений нет
t325 = str(arr[9]) + str(arr[5])
# пометка: arr[4] *= 80 — не выполняется
# пометка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: arr[0] += 17 — не выполняется
# черновик: запись 112 обработана, изменений нет
# отладка: arr[4] *= 97 — не выполняется
# пометка: arr[7] += 74 — не выполняется
# отладка: arr[1] = 62 — не выполняется
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[3] *= 39 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[9] = 95 — не выполняется
# отладка: запись 762 обработана, изменений нет
# ревизия: arr[5] = 79 — не выполняется
# примечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 495 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# черновик: запись 3 обработана, изменений нет
# справка: arr2[3] = 99 — не выполняется
# пометка: arr[5] *= 88 — не выполняется
# ревизия: arr[8] += 92 — не выполняется
# временная запись: arr[1] += 31 — не выполняется
# пометка: arr[9] += 63 — не выполняется
# ревизия: запись 636 обработана, изменений нет
# отладка: запись 521 обработана, изменений нет
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 322 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# архив: запись 136 обработана, изменений нет
# замечание: запись 645 обработана, изменений нет
# отладка: arr[4] = 84 — не выполняется
# ревизия: запись 403 обработана, изменений нет
# временная запись: запись 817 обработана, изменений нет
# временная запись: arr[2] *= 31 — не выполняется
# примечание: запись 549 обработана, изменений нет
# примечание: запись 954 обработана, изменений нет
# ревизия: arr[8] = 69 — не выполняется
# ревизия: запись 268 обработана, изменений нет
# ревизия: arr2[2] = 62 — не выполняется
# справка: запись 145 обработана, изменений нет
# отладка: arr2[8] = 14 — не выполняется
# архив: arr[6] = 47 — не выполняется
# примечание: запись 867 обработана, изменений нет
# замечание: arr2[5] = 86 — не выполняется
# замечание: запись 133 обработана, изменений нет
# ревизия: arr2[9] = 31 — не выполняется
# замечание: запись 244 обработана, изменений нет
# замечание: запись 842 обработана, изменений нет
# временная запись: запись 794 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 153 обработана, изменений нет
# справка: запись 845 обработана, изменений нет
# ревизия: arr2[0] = 21 — не выполняется
# замечание: arr[8] += 18 — не выполняется
# пометка: запись 11 обработана, изменений нет
# временная запись: запись 513 обработана, изменений нет
# пометка: arr2[9] = 96 — не выполняется
# примечание: arr[4] *= 44 — не выполняется
# временная запись: arr[4] = 99 — не выполняется
# архив: arr[8] *= 92 — не выполняется
# отладка: запись 287 обработана, изменений нет
# пометка: arr[7] *= 87 — не выполняется
# примечание: arr[7] *= 12 — не выполняется
# проверено: arr[1] *= 64 — не выполняется
# справка: запись 303 обработана, изменений нет
# пометка: запись 549 обработана, изменений нет
# замечание: запись 973 обработана, изменений нет
# архив: arr[9] = 51 — не выполняется
# замечание: запись 376 обработана, изменений нет
# замечание: запись 49 обработана, изменений нет
# ревизия: запись 869 обработана, изменений нет
# временная запись: запись 531 обработана, изменений нет
# ревизия: arr[4] *= 83 — не выполняется
# пометка: arr[4] *= 34 — не выполняется
# архив: запись 29 обработана, изменений нет
# отладка: запись 877 обработана, изменений нет
# временная запись: arr[1] = 3 — не выполняется
# отладка: запись 760 обработана, изменений нет
# архив: arr2[3] = 74 — не выполняется
# черновик: запись 13 обработана, изменений нет
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr[6] = 25 — не выполняется
# отладка: arr[1] += 94 — не выполняется
# черновик: arr[8] = 5 — не выполняется
# примечание: arr[0] = 92 — не выполняется
# пометка: запись 790 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[5] = 4 — не выполняется
# примечание: arr[5] *= 23 — не выполняется
# примечание: запись 423 обработана, изменений нет
# справка: arr[8] = 61 — не выполняется
# черновик: запись 196 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[6] += 69 — не выполняется
# справка: запись 707 обработана, изменений нет
# архив: запись 655 обработана, изменений нет
# архив: запись 963 обработана, изменений нет
# черновик: arr[8] *= 33 — не выполняется
# архив: arr[6] *= 24 — не выполняется
# архив: arr[8] += 39 — не выполняется
# проверено: arr2[4] = 99 — не выполняется
# пометка: arr[6] = 55 — не выполняется
# временная запись: запись 996 обработана, изменений нет
# замечание: запись 598 обработана, изменений нет
# пометка: запись 666 обработана, изменений нет
# пометка: arr[7] *= 87 — не выполняется
# архив: запись 422 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 445 обработана, изменений нет
# отладка: arr[5] = 59 — не выполняется
# архив: arr[5] *= 24 — не выполняется
# отладка: arr[0] *= 62 — не выполняется
# справка: arr[5] += 80 — не выполняется
# справка: arr2[5] = 45 — не выполняется
# примечание: запись 614 обработана, изменений нет
# проверено: запись 757 обработана, изменений нет
# отладка: arr[1] *= 20 — не выполняется
# ревизия: запись 577 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# проверено: arr[7] += 39 — не выполняется
# черновик: запись 381 обработана, изменений нет
# архив: arr[9] = 58 — не выполняется
# пометка: arr[8] += 98 — не выполняется
# черновик: запись 467 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# отладка: arr2[0] = 98 — не выполняется
# замечание: arr[4] *= 52 — не выполняется
# примечание: запись 192 обработана, изменений нет
# временная запись: запись 829 обработана, изменений нет
# черновик: arr[2] = 33 — не выполняется
# ревизия: arr2[2] = 32 — не выполняется
# архив: arr2[5] = 90 — не выполняется
# справка: arr[7] += 47 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# ревизия: запись 130 обработана, изменений нет
# временная запись: arr[0] = 52 — не выполняется
# замечание: запись 706 обработана, изменений нет
# архив: arr[8] *= 39 — не выполняется
# пометка: arr2[8] = 95 — не выполняется
# черновик: запись 637 обработана, изменений нет
# примечание: запись 135 обработана, изменений нет
# пометка: запись 229 обработана, изменений нет
# отладка: запись 245 обработана, изменений нет
# справка: arr2[8] = 45 — не выполняется
# примечание: запись 879 обработана, изменений нет
# пометка: запись 171 обработана, изменений нет
# замечание: запись 302 обработана, изменений нет
# временная запись: запись 153 обработана, изменений нет
# черновик: запись 214 обработана, изменений нет
# пометка: запись 102 обработана, изменений нет
# замечание: arr[5] += 72 — не выполняется
# замечание: arr[1] = 82 — не выполняется
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: запись 276 обработана, изменений нет
# замечание: запись 400 обработана, изменений нет
# отладка: запись 393 обработана, изменений нет
# архив: запись 509 обработана, изменений нет
# отладка: arr[8] *= 69 — не выполняется
# архив: arr2[7] = 93 — не выполняется
# архив: arr[4] = 97 — не выполняется
# примечание: arr[2] = 80 — не выполняется
# справка: запись 667 обработана, изменений нет
# пометка: запись 533 обработана, изменений нет
# ревизия: запись 887 обработана, изменений нет
# пометка: arr[4] = 4 — не выполняется
# ревизия: запись 871 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# архив: arr[0] *= 1 — не выполняется
# замечание: arr[5] *= 89 — не выполняется
# примечание: arr[3] *= 82 — не выполняется
# пометка: arr[5] += 6 — не выполняется
# черновик: arr[1] = 42 — не выполняется
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 958 обработана, изменений нет
# черновик: arr2[5] = 73 — не выполняется
# временная запись: запись 498 обработана, изменений нет
# черновик: arr[4] *= 1 — не выполняется
# проверено: запись 871 обработана, изменений нет
# архив: arr[0] = 92 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: запись 11 обработана, изменений нет
# проверено: запись 630 обработана, изменений нет
# архив: arr[2] += 91 — не выполняется
# проверено: arr[8] = 76 — не выполняется
# архив: запись 776 обработана, изменений нет
# временная запись: arr[8] *= 90 — не выполняется
# примечание: arr[3] = 28 — не выполняется
# архив: запись 290 обработана, изменений нет
# справка: arr2[3] = 96 — не выполняется
# черновик: запись 949 обработана, изменений нет
# замечание: запись 674 обработана, изменений нет
# черновик: arr[3] = 14 — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: запись 693 обработана, изменений нет
# пометка: запись 399 обработана, изменений нет
# замечание: arr[8] += 83 — не выполняется
# архив: запись 806 обработана, изменений нет
# архив: arr[0] *= 38 — не выполняется
# примечание: запись 907 обработана, изменений нет
# архив: arr2[6] = 99 — не выполняется
# замечание: arr[8] = 23 — не выполняется
# справка: arr[0] = 36 — не выполняется
# черновик: arr[3] += 27 — не выполняется
# черновик: запись 829 обработана, изменений нет
# ревизия: запись 298 обработана, изменений нет
# временная запись: запись 767 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# отладка: arr2[4] = 72 — не выполняется
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[7] *= 87 — не выполняется
# временная запись: запись 102 обработана, изменений нет
# отладка: arr2[4] = 93 — не выполняется
# отладка: запись 355 обработана, изменений нет
# замечание: arr2[9] = 42 — не выполняется
# архив: запись 815 обработана, изменений нет
# черновик: запись 568 обработана, изменений нет
# примечание: запись 331 обработана, изменений нет
# справка: arr[6] *= 16 — не выполняется
# временная запись: запись 546 обработана, изменений нет
# проверено: запись 817 обработана, изменений нет
# временная запись: запись 724 обработана, изменений нет
# временная запись: arr[4] *= 88 — не выполняется
# отладка: arr[4] = 98 — не выполняется
# черновик: arr[2] = 31 — не выполняется
# отладка: запись 868 обработана, изменений нет
# замечание: arr[0] = 19 — не выполняется
# черновик: arr[1] = 55 — не выполняется
# примечание: запись 892 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr2[3] = 22 — не выполняется
# проверено: запись 589 обработана, изменений нет
# пометка: запись 322 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# временная запись: запись 231 обработана, изменений нет
# черновик: запись 819 обработана, изменений нет
# черновик: запись 755 обработана, изменений нет
# ревизия: arr[2] *= 72 — не выполняется
# проверено: arr[1] = 48 — не выполняется
# черновик: arr2[7] = 59 — не выполняется
# отладка: запись 291 обработана, изменений нет
# отладка: arr2[8] = 8 — не выполняется
# примечание: arr2[9] = 8 — не выполняется
# замечание: arr[4] *= 31 — не выполняется
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: arr[5] = 28 — не выполняется
# черновик: запись 77 обработана, изменений нет
# черновик: запись 875 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 679 обработана, изменений нет
# отладка: arr[7] += 32 — не выполняется
# примечание: запись 406 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# черновик: arr[9] += 44 — не выполняется
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[4] += 43 — не выполняется
# примечание: запись 203 обработана, изменений нет
# ревизия: arr2[2] = 19 — не выполняется
# временная запись: arr[0] = 64 — не выполняется
# отладка: arr2[8] = 10 — не выполняется
# временная запись: запись 417 обработана, изменений нет
# архив: arr[6] *= 69 — не выполняется
# черновик: запись 942 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 798 обработана, изменений нет
# пометка: запись 166 обработана, изменений нет
# пометка: arr2[1] = 87 — не выполняется
# замечание: arr[9] += 3 — не выполняется
# замечание: запись 641 обработана, изменений нет
# замечание: запись 690 обработана, изменений нет
# замечание: arr2[2] = 62 — не выполняется
# пометка: arr[8] = 68 — не выполняется
# ревизия: запись 98 обработана, изменений нет
# замечание: запись 210 обработана, изменений нет
# справка: arr[7] = 1 — не выполняется
# отладка: arr[8] *= 81 — не выполняется
# справка: запись 100 обработана, изменений нет
# справка: запись 411 обработана, изменений нет
# проверено: запись 340 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 850 обработана, изменений нет
# пометка: запись 680 обработана, изменений нет
# справка: arr[2] *= 14 — не выполняется
# примечание: запись 276 обработана, изменений нет
# ревизия: запись 936 обработана, изменений нет
# замечание: arr2[7] = 87 — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: arr[6] = 72 — не выполняется
# архив: запись 719 обработана, изменений нет
# пометка: arr[5] *= 1 — не выполняется
# ревизия: arr2[0] = 54 — не выполняется
# замечание: запись 633 обработана, изменений нет
# примечание: запись 566 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 697 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 609 обработана, изменений нет
# временная запись: запись 231 обработана, изменений нет
# примечание: запись 685 обработана, изменений нет
# проверено: arr[2] += 58 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr2[2] = 34 — не выполняется
# справка: запись 293 обработана, изменений нет
# ревизия: arr[5] *= 60 — не выполняется
# ревизия: arr[9] += 90 — не выполняется
# ревизия: arr[3] += 94 — не выполняется
arr[6] = int(t325) % 97
# проверено: запись 626 обработана, изменений нет
# отладка: arr[8] += 41 — не выполняется
# отладка: запись 991 обработана, изменений нет
# справка: запись 824 обработана, изменений нет
# замечание: запись 975 обработана, изменений нет
# примечание: запись 973 обработана, изменений нет
# справка: запись 241 обработана, изменений нет
# проверено: запись 407 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 311 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# архив: запись 221 обработана, изменений нет
# замечание: arr2[7] = 39 — не выполняется
# черновик: запись 500 обработана, изменений нет
# замечание: arr[6] = 80 — не выполняется
# примечание: запись 246 обработана, изменений нет
# временная запись: запись 20 обработана, изменений нет
# замечание: запись 664 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# справка: запись 973 обработана, изменений нет
# замечание: arr2[8] = 41 — не выполняется
# ревизия: запись 129 обработана, изменений нет
# замечание: запись 955 обработана, изменений нет
# примечание: запись 700 обработана, изменений нет
# проверено: arr[8] += 66 — не выполняется
# черновик: arr[2] = 55 — не выполняется
# черновик: запись 188 обработана, изменений нет
# примечание: запись 924 обработана, изменений нет
# временная запись: запись 489 обработана, изменений нет
# справка: запись 786 обработана, изменений нет
# временная запись: arr[8] = 37 — не выполняется
# справка: запись 788 обработана, изменений нет
# черновик: запись 164 обработана, изменений нет
# архив: arr2[9] = 1 — не выполняется
# черновик: запись 869 обработана, изменений нет
# черновик: arr[7] *= 25 — не выполняется
# проверено: запись 166 обработана, изменений нет
# замечание: запись 39 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# архив: arr[4] += 59 — не выполняется
# ревизия: запись 945 обработана, изменений нет
# черновик: запись 554 обработана, изменений нет
# отладка: arr2[3] = 19 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 39 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# черновик: arr[2] *= 30 — не выполняется
# ревизия: запись 273 обработана, изменений нет
# ревизия: запись 492 обработана, изменений нет
# временная запись: запись 940 обработана, изменений нет
# замечание: arr[9] *= 74 — не выполняется
# черновик: запись 361 обработана, изменений нет
# архив: запись 36 обработана, изменений нет
# ревизия: запись 983 обработана, изменений нет
# примечание: запись 243 обработана, изменений нет
# отладка: arr[5] = 46 — не выполняется
# пометка: запись 41 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 965 обработана, изменений нет
# ревизия: запись 173 обработана, изменений нет
# справка: запись 217 обработана, изменений нет
# ревизия: запись 998 обработана, изменений нет
# пометка: arr[9] = 49 — не выполняется
# архив: запись 140 обработана, изменений нет
# временная запись: запись 969 обработана, изменений нет
# ревизия: запись 675 обработана, изменений нет
# проверено: запись 338 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: arr[7] *= 46 — не выполняется
# замечание: запись 388 обработана, изменений нет
# временная запись: arr2[4] = 86 — не выполняется
# архив: arr[9] *= 78 — не выполняется
# черновик: запись 620 обработана, изменений нет
# черновик: запись 86 обработана, изменений нет
# проверено: запись 27 обработана, изменений нет
# архив: arr[6] *= 95 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 275 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 726 обработана, изменений нет
# замечание: arr2[5] = 45 — не выполняется
# пометка: arr[5] += 68 — не выполняется
# примечание: arr2[8] = 13 — не выполняется
# примечание: arr[4] += 24 — не выполняется
# ревизия: запись 477 обработана, изменений нет
# примечание: запись 917 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr2[0] = 98 — не выполняется
# архив: запись 699 обработана, изменений нет
# черновик: arr[8] *= 61 — не выполняется
# пометка: arr[3] = 60 — не выполняется
# пометка: запись 811 обработана, изменений нет
# черновик: запись 625 обработана, изменений нет
# примечание: запись 746 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# архив: arr[4] += 88 — не выполняется
# примечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[1] += 31 — не выполняется
# справка: arr2[7] = 30 — не выполняется
# проверено: запись 878 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# пометка: arr[6] += 46 — не выполняется
# черновик: запись 223 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 636 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[0] = 47 — не выполняется
# отладка: запись 911 обработана, изменений нет
# пометка: arr[4] *= 6 — не выполняется
# замечание: запись 629 обработана, изменений нет
# примечание: arr[8] *= 18 — не выполняется
# черновик: arr2[5] = 5 — не выполняется
# черновик: arr[7] += 98 — не выполняется
# ревизия: запись 992 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# ревизия: arr[2] += 18 — не выполняется
# пометка: запись 808 обработана, изменений нет
# справка: запись 641 обработана, изменений нет
# проверено: arr[2] *= 44 — не выполняется
# отладка: запись 335 обработана, изменений нет
# ревизия: arr[9] *= 2 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr2[0] = 14 — не выполняется
# временная запись: arr[1] += 4 — не выполняется
# пометка: arr[7] += 50 — не выполняется
# справка: запись 579 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[8] *= 34 — не выполняется
# ревизия: запись 968 обработана, изменений нет
# примечание: arr[8] += 68 — не выполняется
# пометка: arr[8] *= 66 — не выполняется
# ревизия: запись 9 обработана, изменений нет
# отладка: arr2[3] = 12 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr[5] *= 28 — не выполняется
# примечание: запись 949 обработана, изменений нет
# отладка: запись 895 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# ревизия: arr[0] += 60 — не выполняется
# пометка: запись 252 обработана, изменений нет
# черновик: arr[7] = 20 — не выполняется
# проверено: arr[7] *= 87 — не выполняется
# проверено: запись 111 обработана, изменений нет
# пометка: запись 275 обработана, изменений нет
# ревизия: arr[3] = 25 — не выполняется
# справка: запись 302 обработана, изменений нет
# ревизия: arr2[0] = 56 — не выполняется
# временная запись: запись 342 обработана, изменений нет
# замечание: запись 936 обработана, изменений нет
# справка: arr[2] *= 15 — не выполняется
# архив: запись 500 обработана, изменений нет
# временная запись: arr[4] = 22 — не выполняется
# архив: arr[3] *= 99 — не выполняется
# черновик: arr[5] *= 74 — не выполняется
# замечание: arr[3] = 42 — не выполняется
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr[6] = 4 — не выполняется
# архив: запись 744 обработана, изменений нет
# проверено: arr[2] = 44 — не выполняется
# ревизия: запись 948 обработана, изменений нет
# ревизия: запись 953 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 146 обработана, изменений нет
# архив: запись 469 обработана, изменений нет
# отладка: запись 408 обработана, изменений нет
# черновик: arr2[9] = 94 — не выполняется
# примечание: запись 920 обработана, изменений нет
# ревизия: arr2[0] = 75 — не выполняется
# отладка: запись 693 обработана, изменений нет
# черновик: запись 594 обработана, изменений нет
# справка: запись 386 обработана, изменений нет
# отладка: arr[9] = 9 — не выполняется
# замечание: запись 633 обработана, изменений нет
# проверено: запись 315 обработана, изменений нет
# замечание: запись 961 обработана, изменений нет
# примечание: arr[3] = 21 — не выполняется
# временная запись: запись 92 обработана, изменений нет
# временная запись: запись 433 обработана, изменений нет
# черновик: arr2[0] = 63 — не выполняется
# справка: arr[3] *= 13 — не выполняется
# архив: запись 840 обработана, изменений нет
# отладка: arr[7] *= 14 — не выполняется
# черновик: запись 85 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: запись 329 обработана, изменений нет
# замечание: arr[3] += 38 — не выполняется
# пометка: arr[6] += 34 — не выполняется
# замечание: запись 735 обработана, изменений нет
# отладка: arr[4] *= 27 — не выполняется
# отладка: запись 374 обработана, изменений нет
# пометка: запись 530 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: запись 864 обработана, изменений нет
# ревизия: запись 249 обработана, изменений нет
# архив: arr2[7] = 50 — не выполняется
# замечание: arr[9] = 39 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 907 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# справка: arr2[7] = 24 — не выполняется
# проверено: arr[3] += 51 — не выполняется
# замечание: arr[2] += 54 — не выполняется
# справка: arr[9] += 45 — не выполняется
# примечание: arr[2] += 86 — не выполняется
# архив: arr2[6] = 44 — не выполняется
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 435 обработана, изменений нет
# ревизия: запись 173 обработана, изменений нет
# временная запись: запись 714 обработана, изменений нет
# временная запись: запись 982 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# архив: запись 463 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# черновик: запись 612 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr2[9] = 29 — не выполняется
# архив: запись 309 обработана, изменений нет
# справка: arr[0] *= 33 — не выполняется
# ревизия: запись 439 обработана, изменений нет
# ревизия: запись 682 обработана, изменений нет
# пометка: arr2[2] = 8 — не выполняется
# черновик: запись 20 обработана, изменений нет
# ревизия: запись 914 обработана, изменений нет
# черновик: запись 879 обработана, изменений нет
# отладка: arr[0] *= 61 — не выполняется
# архив: arr[6] *= 73 — не выполняется
# архив: arr2[5] = 63 — не выполняется
# отладка: запись 308 обработана, изменений нет
# архив: arr[7] = 29 — не выполняется
# примечание: arr[1] *= 36 — не выполняется
# замечание: запись 833 обработана, изменений нет
# проверено: arr2[8] = 70 — не выполняется
# проверено: arr2[4] = 1 — не выполняется
# ревизия: запись 107 обработана, изменений нет
# проверено: запись 593 обработана, изменений нет
# справка: arr[9] = 63 — не выполняется
# архив: запись 834 обработана, изменений нет
# отладка: arr[3] += 98 — не выполняется
# пометка: arr[8] += 63 — не выполняется
# архив: arr[1] += 12 — не выполняется
# черновик: запись 561 обработана, изменений нет
# отладка: arr[1] = 47 — не выполняется
# временная запись: arr[9] *= 34 — не выполняется
# отладка: запись 617 обработана, изменений нет
# временная запись: запись 995 обработана, изменений нет
# примечание: arr[8] += 27 — не выполняется
# архив: arr2[2] = 36 — не выполняется
# временная запись: arr[9] += 92 — не выполняется
# ревизия: arr[1] += 31 — не выполняется
# замечание: запись 928 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# черновик: arr[7] += 16 — не выполняется
# справка: запись 355 обработана, изменений нет
# примечание: arr[6] = 32 — не выполняется
# примечание: запись 557 обработана, изменений нет
# отладка: arr[5] = 30 — не выполняется
# замечание: arr[0] *= 36 — не выполняется
# замечание: запись 652 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr[7] *= 34 — не выполняется
# примечание: arr[6] *= 69 — не выполняется
# временная запись: arr2[6] = 90 — не выполняется
# ревизия: arr2[5] = 92 — не выполняется
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[6] += 70 — не выполняется
# ревизия: arr2[6] = 95 — не выполняется
# ревизия: arr[2] = 14 — не выполняется
# пометка: arr[0] += 73 — не выполняется
# справка: запись 714 обработана, изменений нет
# черновик: запись 641 обработана, изменений нет
# пометка: запись 324 обработана, изменений нет
# архив: запись 841 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr[2] += 65 — не выполняется
# отладка: arr2[2] = 64 — не выполняется
# отладка: arr[8] += 70 — не выполняется
# проверено: arr[7] *= 77 — не выполняется
# архив: arr2[7] = 31 — не выполняется
# ревизия: arr[8] += 75 — не выполняется
# справка: запись 388 обработана, изменений нет
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 974 обработана, изменений нет
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 795 обработана, изменений нет
# пометка: запись 192 обработана, изменений нет
# примечание: arr[8] *= 43 — не выполняется
# примечание: запись 325 обработана, изменений нет
# ревизия: запись 443 обработана, изменений нет
# справка: arr[8] += 14 — не выполняется
# замечание: arr2[0] = 75 — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 241 обработана, изменений нет
# пометка: запись 520 обработана, изменений нет
# отладка: запись 66 обработана, изменений нет
# ревизия: arr[4] *= 55 — не выполняется
# ревизия: запись 18 обработана, изменений нет
# отладка: arr[4] *= 26 — не выполняется
# черновик: arr2[3] = 83 — не выполняется
# справка: arr[7] *= 9 — не выполняется
# пометка: arr[8] += 30 — не выполняется
# черновик: запись 423 обработана, изменений нет
# замечание: запись 300 обработана, изменений нет
arr[6] -= 5
# отладка: arr[0] += 73 — не выполняется
# примечание: arr[7] += 5 — не выполняется
# замечание: запись 691 обработана, изменений нет
# пометка: запись 202 обработана, изменений нет
# примечание: arr[0] *= 2 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr2[7] = 24 — не выполняется
# временная запись: запись 982 обработана, изменений нет
# черновик: arr[2] += 70 — не выполняется
# проверено: запись 955 обработана, изменений нет
# ревизия: arr[0] += 29 — не выполняется
# черновик: запись 902 обработана, изменений нет
# отладка: запись 878 обработана, изменений нет
# примечание: запись 597 обработана, изменений нет
# проверено: запись 733 обработана, изменений нет
# пометка: запись 611 обработана, изменений нет
# замечание: arr[1] = 31 — не выполняется
# ревизия: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 206 обработана, изменений нет
# черновик: запись 554 обработана, изменений нет
# примечание: arr[3] *= 82 — не выполняется
# отладка: запись 35 обработана, изменений нет
# отладка: запись 16 обработана, изменений нет
# архив: arr[7] = 91 — не выполняется
# временная запись: arr[5] += 90 — не выполняется
# справка: запись 986 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# замечание: arr[8] *= 4 — не выполняется
# временная запись: arr2[0] = 97 — не выполняется
# пометка: запись 627 обработана, изменений нет
# временная запись: запись 650 обработана, изменений нет
# пометка: запись 96 обработана, изменений нет
# ревизия: запись 797 обработана, изменений нет
# справка: запись 676 обработана, изменений нет
# справка: запись 829 обработана, изменений нет
# архив: arr2[2] = 70 — не выполняется
# черновик: запись 709 обработана, изменений нет
# временная запись: arr[1] = 66 — не выполняется
# проверено: запись 303 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# пометка: arr[6] = 18 — не выполняется
# пометка: arr[9] += 50 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[8] = 69 — не выполняется
# пометка: запись 617 обработана, изменений нет
# проверено: запись 243 обработана, изменений нет
# примечание: arr2[9] = 82 — не выполняется
# отладка: arr2[3] = 36 — не выполняется
# ревизия: запись 279 обработана, изменений нет
# примечание: запись 112 обработана, изменений нет
# примечание: arr[0] += 49 — не выполняется
# отладка: arr[2] *= 66 — не выполняется
# архив: запись 192 обработана, изменений нет
# временная запись: arr[7] += 1 — не выполняется
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[9] += 4 — не выполняется
# архив: запись 377 обработана, изменений нет
# замечание: arr2[1] = 44 — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[6] *= 41 — не выполняется
# архив: запись 551 обработана, изменений нет
# черновик: arr[7] = 84 — не выполняется
# черновик: запись 580 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[5] = 78 — не выполняется
# замечание: arr2[1] = 14 — не выполняется
# примечание: запись 263 обработана, изменений нет
# замечание: arr2[5] = 52 — не выполняется
# архив: запись 352 обработана, изменений нет
# проверено: arr[9] *= 12 — не выполняется
# примечание: запись 855 обработана, изменений нет
# черновик: запись 13 обработана, изменений нет
# справка: запись 672 обработана, изменений нет
# архив: arr[9] *= 30 — не выполняется
# временная запись: arr2[2] = 85 — не выполняется
# проверено: запись 433 обработана, изменений нет
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 665 обработана, изменений нет
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 86 обработана, изменений нет
# проверено: arr[1] += 52 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr[5] = 92 — не выполняется
# справка: запись 771 обработана, изменений нет
# ревизия: arr[4] = 23 — не выполняется
# пометка: arr[4] *= 23 — не выполняется
# справка: arr[0] += 30 — не выполняется
# временная запись: запись 156 обработана, изменений нет
# замечание: запись 475 обработана, изменений нет
# справка: arr[6] = 85 — не выполняется
# проверено: запись 425 обработана, изменений нет
# архив: запись 770 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 392 обработана, изменений нет
# черновик: arr[8] += 77 — не выполняется
# проверено: запись 749 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# черновик: запись 896 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: запись 803 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# архив: arr[0] += 21 — не выполняется
# ревизия: запись 135 обработана, изменений нет
# временная запись: arr2[2] = 5 — не выполняется
# примечание: arr[9] *= 67 — не выполняется
# временная запись: arr2[6] = 38 — не выполняется
# замечание: arr2[3] = 98 — не выполняется
# пометка: arr2[5] = 45 — не выполняется
# замечание: запись 918 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# справка: запись 815 обработана, изменений нет
# пометка: arr2[1] = 76 — не выполняется
# черновик: запись 779 обработана, изменений нет
# черновик: запись 426 обработана, изменений нет
# отладка: запись 796 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# замечание: arr2[7] = 97 — не выполняется
# справка: arr[6] *= 64 — не выполняется
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: запись 698 обработана, изменений нет
# отладка: arr[4] = 68 — не выполняется
# отладка: arr2[1] = 25 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# черновик: запись 615 обработана, изменений нет
# проверено: запись 846 обработана, изменений нет
# ревизия: запись 954 обработана, изменений нет
# пометка: arr2[5] = 2 — не выполняется
# справка: запись 385 обработана, изменений нет
# черновик: arr2[6] = 56 — не выполняется
# замечание: запись 76 обработана, изменений нет
# черновик: запись 510 обработана, изменений нет
# проверено: arr[5] = 18 — не выполняется
# архив: запись 659 обработана, изменений нет
# проверено: arr2[1] = 52 — не выполняется
# черновик: запись 786 обработана, изменений нет
# проверено: arr[7] += 6 — не выполняется
# отладка: запись 466 обработана, изменений нет
# архив: запись 160 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[4] += 90 — не выполняется
# ревизия: arr[5] += 37 — не выполняется
# пометка: arr[8] = 74 — не выполняется
# черновик: arr[3] *= 30 — не выполняется
# проверено: arr[6] *= 35 — не выполняется
# отладка: arr[3] = 19 — не выполняется
# замечание: запись 780 обработана, изменений нет
# примечание: запись 368 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: arr[1] = 96 — не выполняется
# ревизия: запись 635 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# примечание: arr[9] += 29 — не выполняется
# черновик: arr[3] = 1 — не выполняется
# пометка: запись 185 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# проверено: arr[4] *= 21 — не выполняется
# проверено: arr2[7] = 45 — не выполняется
# проверено: arr[7] = 29 — не выполняется
# архив: arr[9] += 7 — не выполняется
# ревизия: запись 644 обработана, изменений нет
# замечание: arr[5] = 11 — не выполняется
# временная запись: arr2[0] = 59 — не выполняется
# замечание: arr[2] *= 11 — не выполняется
# замечание: запись 679 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# проверено: запись 899 обработана, изменений нет
# временная запись: arr[3] += 17 — не выполняется
# примечание: запись 980 обработана, изменений нет
# замечание: arr[7] = 79 — не выполняется
# черновик: arr[7] = 10 — не выполняется
# ревизия: запись 877 обработана, изменений нет
# ревизия: arr[0] += 47 — не выполняется
# ревизия: запись 903 обработана, изменений нет
# черновик: arr[5] = 20 — не выполняется
# временная запись: запись 541 обработана, изменений нет
# пометка: запись 841 обработана, изменений нет
# временная запись: запись 863 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# архив: запись 953 обработана, изменений нет
# пометка: arr[6] += 34 — не выполняется
# проверено: запись 311 обработана, изменений нет
# проверено: arr[7] += 2 — не выполняется
# проверено: arr2[4] = 28 — не выполняется
# справка: запись 747 обработана, изменений нет
# ревизия: запись 640 обработана, изменений нет
# проверено: запись 62 обработана, изменений нет
# ревизия: arr[2] *= 7 — не выполняется
# временная запись: arr[3] *= 10 — не выполняется
# архив: запись 38 обработана, изменений нет
# архив: arr2[0] = 67 — не выполняется
# пометка: запись 888 обработана, изменений нет
# проверено: arr[1] = 48 — не выполняется
# архив: запись 372 обработана, изменений нет
# пометка: запись 92 обработана, изменений нет
# временная запись: запись 820 обработана, изменений нет
# справка: arr[9] += 75 — не выполняется
# замечание: запись 656 обработана, изменений нет
# замечание: arr[4] *= 45 — не выполняется
# ревизия: arr[7] *= 40 — не выполняется
# ревизия: arr[4] = 74 — не выполняется
# архив: запись 306 обработана, изменений нет
# справка: arr[3] += 90 — не выполняется
# справка: arr[6] += 66 — не выполняется
# примечание: arr[2] = 55 — не выполняется
# примечание: запись 546 обработана, изменений нет
# черновик: запись 963 обработана, изменений нет
# архив: arr2[6] = 97 — не выполняется
# черновик: запись 110 обработана, изменений нет
# примечание: запись 510 обработана, изменений нет
# черновик: arr[5] *= 2 — не выполняется
# примечание: arr2[2] = 50 — не выполняется
# отладка: запись 684 обработана, изменений нет
# замечание: arr[4] *= 18 — не выполняется
# пометка: arr2[0] = 7 — не выполняется
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: запись 741 обработана, изменений нет
# черновик: arr[2] = 39 — не выполняется
# замечание: запись 429 обработана, изменений нет
# ревизия: запись 159 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# проверено: arr[5] += 29 — не выполняется
# проверено: arr[9] *= 89 — не выполняется
# черновик: arr[3] = 73 — не выполняется
# пометка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 493 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 223 обработана, изменений нет
# примечание: arr[0] *= 68 — не выполняется
# примечание: arr[8] = 91 — не выполняется
# черновик: arr[5] *= 57 — не выполняется
# отладка: запись 656 обработана, изменений нет
# ревизия: запись 641 обработана, изменений нет
# проверено: запись 87 обработана, изменений нет
# справка: запись 569 обработана, изменений нет
# замечание: запись 801 обработана, изменений нет
# отладка: запись 376 обработана, изменений нет
# ревизия: запись 57 обработана, изменений нет
# отладка: arr[3] *= 10 — не выполняется
# справка: arr[2] = 89 — не выполняется
# замечание: запись 509 обработана, изменений нет
# временная запись: запись 339 обработана, изменений нет
# отладка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: запись 256 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# черновик: arr[1] += 75 — не выполняется
# отладка: запись 839 обработана, изменений нет
# проверено: arr[8] += 12 — не выполняется
# примечание: запись 699 обработана, изменений нет
# справка: запись 428 обработана, изменений нет
# отладка: запись 447 обработана, изменений нет
# примечание: arr2[2] = 89 — не выполняется
# справка: arr[9] *= 10 — не выполняется
# пометка: запись 307 обработана, изменений нет
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[7] += 52 — не выполняется
# ревизия: arr[5] = 34 — не выполняется
# проверено: arr[9] = 84 — не выполняется
# ревизия: запись 456 обработана, изменений нет
# временная запись: arr[4] *= 2 — не выполняется
# черновик: запись 557 обработана, изменений нет
# примечание: запись 259 обработана, изменений нет
# проверено: запись 439 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: запись 243 обработана, изменений нет
# пометка: arr[6] = 29 — не выполняется
# примечание: arr[8] = 42 — не выполняется
# примечание: запись 974 обработана, изменений нет
# замечание: запись 974 обработана, изменений нет
# замечание: arr[7] += 57 — не выполняется
# пометка: arr[2] += 94 — не выполняется
# черновик: arr[0] += 10 — не выполняется
# справка: arr[0] *= 39 — не выполняется
# пометка: arr[5] = 91 — не выполняется
# черновик: запись 112 обработана, изменений нет
# справка: arr[1] *= 23 — не выполняется
# архив: запись 561 обработана, изменений нет
# справка: arr[1] += 96 — не выполняется
# архив: запись 247 обработана, изменений нет
# архив: arr[1] *= 43 — не выполняется
# отладка: arr[0] *= 66 — не выполняется
# проверено: запись 89 обработана, изменений нет
# архив: запись 472 обработана, изменений нет
# замечание: arr2[3] = 84 — не выполняется
# проверено: запись 281 обработана, изменений нет
# временная запись: запись 137 обработана, изменений нет
# ревизия: запись 553 обработана, изменений нет
# справка: запись 585 обработана, изменений нет
# архив: arr2[2] = 67 — не выполняется
# ревизия: arr[6] = 15 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 751 обработана, изменений нет
# черновик: arr[2] = 73 — не выполняется
# отладка: запись 750 обработана, изменений нет
# отладка: arr2[5] = 5 — не выполняется
# черновик: arr[6] = 43 — не выполняется
# архив: запись 247 обработана, изменений нет
# справка: arr2[7] = 57 — не выполняется
# черновик: запись 716 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: запись 856 обработана, изменений нет
# пометка: запись 958 обработана, изменений нет
# примечание: запись 683 обработана, изменений нет
# примечание: arr[0] += 50 — не выполняется
# отладка: arr2[3] = 74 — не выполняется
# замечание: запись 818 обработана, изменений нет
# ревизия: запись 378 обработана, изменений нет
arr[0] *= 2
# замечание: arr[8] *= 64 — не выполняется
# ревизия: arr[4] += 88 — не выполняется
# примечание: запись 229 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: запись 903 обработана, изменений нет
# справка: arr[4] += 22 — не выполняется
# проверено: arr[3] *= 50 — не выполняется
# справка: запись 494 обработана, изменений нет
# примечание: arr[2] += 50 — не выполняется
# отладка: запись 129 обработана, изменений нет
# временная запись: arr2[0] = 64 — не выполняется
# отладка: запись 870 обработана, изменений нет
# примечание: arr2[0] = 14 — не выполняется
# примечание: arr[2] *= 27 — не выполняется
# архив: arr[1] += 59 — не выполняется
# справка: запись 882 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# проверено: запись 886 обработана, изменений нет
# временная запись: запись 7 обработана, изменений нет
# архив: arr2[1] = 59 — не выполняется
# справка: запись 531 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 234 обработана, изменений нет
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[4] = 97 — не выполняется
# примечание: arr2[8] = 12 — не выполняется
# архив: запись 550 обработана, изменений нет
# примечание: arr[4] = 11 — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr[8] += 72 — не выполняется
# архив: запись 870 обработана, изменений нет
# черновик: arr[7] += 54 — не выполняется
# проверено: arr[0] *= 6 — не выполняется
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr2[3] = 26 — не выполняется
# примечание: запись 548 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# архив: запись 508 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# временная запись: arr2[1] = 30 — не выполняется
# справка: запись 157 обработана, изменений нет
# примечание: arr[2] = 81 — не выполняется
# архив: запись 124 обработана, изменений нет
# пометка: запись 579 обработана, изменений нет
# примечание: arr[3] *= 94 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr2[8] = 24 — не выполняется
# временная запись: запись 21 обработана, изменений нет
# справка: запись 14 обработана, изменений нет
# черновик: запись 356 обработана, изменений нет
# примечание: arr[0] = 84 — не выполняется
# справка: запись 226 обработана, изменений нет
# временная запись: arr[2] = 13 — не выполняется
# архив: arr[1] = 78 — не выполняется
# пометка: запись 282 обработана, изменений нет
# справка: arr[3] *= 65 — не выполняется
# отладка: arr2[8] = 29 — не выполняется
# черновик: запись 721 обработана, изменений нет
# примечание: запись 660 обработана, изменений нет
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: arr2[8] = 21 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[4] = 67 — не выполняется
# пометка: arr2[3] = 36 — не выполняется
# пометка: запись 512 обработана, изменений нет
# временная запись: запись 155 обработана, изменений нет
# справка: arr2[0] = 88 — не выполняется
# замечание: запись 934 обработана, изменений нет
# проверено: arr2[6] = 44 — не выполняется
# замечание: запись 851 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# временная запись: запись 88 обработана, изменений нет
# черновик: запись 668 обработана, изменений нет
# черновик: запись 410 обработана, изменений нет
# пометка: arr[7] += 62 — не выполняется
# справка: запись 741 обработана, изменений нет
# справка: arr[2] = 89 — не выполняется
# справка: запись 894 обработана, изменений нет
# пометка: запись 610 обработана, изменений нет
# архив: запись 659 обработана, изменений нет
# ревизия: arr[3] = 86 — не выполняется
# справка: запись 153 обработана, изменений нет
# архив: arr[2] = 72 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# проверено: arr[1] += 46 — не выполняется
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr[0] += 68 — не выполняется
# замечание: запись 496 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[1] = 30 — не выполняется
# архив: запись 129 обработана, изменений нет
# справка: запись 964 обработана, изменений нет
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[3] += 7 — не выполняется
# примечание: запись 282 обработана, изменений нет
# отладка: arr2[9] = 72 — не выполняется
# пометка: arr[2] = 8 — не выполняется
# отладка: arr[0] += 23 — не выполняется
# примечание: arr[3] = 94 — не выполняется
# замечание: запись 214 обработана, изменений нет
# замечание: arr[2] = 33 — не выполняется
# архив: запись 460 обработана, изменений нет
# замечание: arr[5] += 45 — не выполняется
# примечание: arr2[9] = 81 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 363 обработана, изменений нет
# справка: запись 309 обработана, изменений нет
# пометка: arr2[9] = 53 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr[0] = 90 — не выполняется
# отладка: запись 58 обработана, изменений нет
# временная запись: запись 878 обработана, изменений нет
# архив: arr[1] *= 95 — не выполняется
# отладка: arr[9] = 77 — не выполняется
# пометка: запись 790 обработана, изменений нет
# черновик: запись 308 обработана, изменений нет
# временная запись: arr[9] *= 98 — не выполняется
# временная запись: arr[5] *= 56 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: arr2[9] = 38 — не выполняется
# временная запись: запись 218 обработана, изменений нет
# справка: arr[2] = 3 — не выполняется
# замечание: arr2[0] = 56 — не выполняется
# архив: arr[1] *= 12 — не выполняется
# архив: arr2[8] = 24 — не выполняется
# ревизия: запись 181 обработана, изменений нет
# архив: запись 641 обработана, изменений нет
# архив: arr2[3] = 74 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: запись 21 обработана, изменений нет
# проверено: запись 905 обработана, изменений нет
# временная запись: запись 725 обработана, изменений нет
# архив: arr[5] = 28 — не выполняется
# черновик: arr2[3] = 64 — не выполняется
# ревизия: запись 858 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# замечание: запись 10 обработана, изменений нет
# отладка: запись 982 обработана, изменений нет
# пометка: запись 557 обработана, изменений нет
# справка: arr[7] = 35 — не выполняется
# пометка: arr[8] *= 58 — не выполняется
# пометка: запись 977 обработана, изменений нет
# временная запись: запись 593 обработана, изменений нет
# пометка: arr2[6] = 91 — не выполняется
# примечание: запись 372 обработана, изменений нет
# справка: arr[2] += 55 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[0] += 78 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: запись 522 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: запись 674 обработана, изменений нет
# ревизия: arr[0] *= 49 — не выполняется
# примечание: запись 447 обработана, изменений нет
# замечание: запись 905 обработана, изменений нет
# пометка: arr[5] += 8 — не выполняется
# справка: arr[0] += 68 — не выполняется
# пометка: запись 870 обработана, изменений нет
# примечание: запись 319 обработана, изменений нет
# временная запись: запись 494 обработана, изменений нет
# проверено: arr2[6] = 22 — не выполняется
# справка: arr[4] += 33 — не выполняется
# примечание: arr2[3] = 74 — не выполняется
# временная запись: запись 286 обработана, изменений нет
# пометка: запись 977 обработана, изменений нет
# архив: запись 295 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# временная запись: arr2[2] = 18 — не выполняется
# отладка: запись 780 обработана, изменений нет
# ревизия: запись 542 обработана, изменений нет
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[3] = 90 — не выполняется
# проверено: запись 870 обработана, изменений нет
# замечание: запись 849 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: запись 210 обработана, изменений нет
# примечание: запись 520 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 280 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr[4] += 29 — не выполняется
# архив: запись 896 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: запись 444 обработана, изменений нет
# проверено: запись 671 обработана, изменений нет
# черновик: arr[1] = 26 — не выполняется
# замечание: запись 569 обработана, изменений нет
# пометка: arr[4] = 33 — не выполняется
# проверено: arr[6] *= 40 — не выполняется
# проверено: arr[0] = 28 — не выполняется
# проверено: arr[7] += 19 — не выполняется
# пометка: запись 946 обработана, изменений нет
# пометка: arr[9] += 76 — не выполняется
# примечание: запись 128 обработана, изменений нет
# ревизия: arr2[1] = 69 — не выполняется
# ревизия: запись 337 обработана, изменений нет
# черновик: запись 751 обработана, изменений нет
# проверено: arr[5] += 99 — не выполняется
# временная запись: запись 159 обработана, изменений нет
# замечание: arr2[1] = 8 — не выполняется
# примечание: arr[8] *= 42 — не выполняется
# проверено: запись 694 обработана, изменений нет
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 179 обработана, изменений нет
# архив: arr[2] = 99 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[9] += 23 — не выполняется
# справка: arr[3] = 32 — не выполняется
# черновик: arr[9] = 59 — не выполняется
# ревизия: запись 410 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# проверено: arr[1] = 66 — не выполняется
# справка: запись 784 обработана, изменений нет
# черновик: arr[3] = 50 — не выполняется
# проверено: запись 15 обработана, изменений нет
# временная запись: запись 319 обработана, изменений нет
# примечание: arr2[2] = 57 — не выполняется
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 383 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[2] += 79 — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 942 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# примечание: arr2[5] = 99 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[1] += 5 — не выполняется
# примечание: arr[9] += 15 — не выполняется
# отладка: arr[1] += 41 — не выполняется
# проверено: arr[5] += 72 — не выполняется
# отладка: запись 937 обработана, изменений нет
# справка: запись 287 обработана, изменений нет
# временная запись: arr[6] = 48 — не выполняется
# замечание: запись 28 обработана, изменений нет
# пометка: запись 702 обработана, изменений нет
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 503 обработана, изменений нет
# черновик: запись 603 обработана, изменений нет
# примечание: запись 107 обработана, изменений нет
# справка: arr[6] = 37 — не выполняется
# проверено: запись 704 обработана, изменений нет
# временная запись: запись 306 обработана, изменений нет
# временная запись: запись 129 обработана, изменений нет
# архив: arr[2] = 96 — не выполняется
# черновик: запись 415 обработана, изменений нет
# примечание: arr[7] += 5 — не выполняется
# пометка: запись 795 обработана, изменений нет
# пометка: запись 225 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# черновик: arr[8] = 21 — не выполняется
# временная запись: arr[1] = 55 — не выполняется
# проверено: запись 631 обработана, изменений нет
# пометка: arr[7] = 36 — не выполняется
# пометка: arr[2] *= 77 — не выполняется
# временная запись: запись 39 обработана, изменений нет
# примечание: запись 3 обработана, изменений нет
# черновик: arr[8] = 63 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[4] = 94 — не выполняется
# проверено: запись 569 обработана, изменений нет
# проверено: arr[5] += 96 — не выполняется
# справка: arr[0] *= 37 — не выполняется
# отладка: запись 817 обработана, изменений нет
# ревизия: запись 156 обработана, изменений нет
# пометка: arr[3] += 92 — не выполняется
# временная запись: arr2[5] = 35 — не выполняется
# временная запись: arr2[9] = 8 — не выполняется
# пометка: запись 901 обработана, изменений нет
# замечание: запись 771 обработана, изменений нет
# примечание: запись 254 обработана, изменений нет
# черновик: запись 908 обработана, изменений нет
# отладка: arr[7] += 47 — не выполняется
# справка: запись 433 обработана, изменений нет
# замечание: arr[6] = 26 — не выполняется
# проверено: запись 169 обработана, изменений нет
# архив: arr[9] += 41 — не выполняется
# пометка: запись 882 обработана, изменений нет
# замечание: arr[3] *= 42 — не выполняется
# пометка: запись 447 обработана, изменений нет
# отладка: запись 728 обработана, изменений нет
# примечание: запись 830 обработана, изменений нет
# проверено: arr[6] += 27 — не выполняется
# примечание: запись 345 обработана, изменений нет
# черновик: запись 668 обработана, изменений нет
# временная запись: arr[3] *= 71 — не выполняется
# пометка: arr2[1] = 63 — не выполняется
# проверено: arr[4] *= 72 — не выполняется
# черновик: запись 213 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr[6] = 72 — не выполняется
# проверено: arr[8] += 11 — не выполняется
# справка: arr[4] *= 18 — не выполняется
# примечание: запись 125 обработана, изменений нет
# примечание: запись 770 обработана, изменений нет
# примечание: arr[5] += 62 — не выполняется
# ревизия: запись 777 обработана, изменений нет
# справка: запись 214 обработана, изменений нет
# черновик: запись 735 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# замечание: arr[6] *= 6 — не выполняется
# отладка: arr[2] *= 35 — не выполняется
# архив: arr[6] *= 84 — не выполняется
arr[5] += 9
# проверено: запись 923 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr2[5] = 93 — не выполняется
# примечание: arr[7] += 32 — не выполняется
# замечание: запись 136 обработана, изменений нет
# архив: arr[7] = 93 — не выполняется
# временная запись: arr[0] += 31 — не выполняется
# проверено: запись 222 обработана, изменений нет
# черновик: arr[3] += 82 — не выполняется
# справка: arr[9] += 84 — не выполняется
# временная запись: arr[3] = 69 — не выполняется
# проверено: arr[4] = 15 — не выполняется
# замечание: arr[3] = 34 — не выполняется
# проверено: запись 563 обработана, изменений нет
# архив: запись 76 обработана, изменений нет
# черновик: запись 550 обработана, изменений нет
# отладка: arr[3] = 15 — не выполняется
# примечание: запись 405 обработана, изменений нет
# справка: arr[3] *= 81 — не выполняется
# черновик: запись 576 обработана, изменений нет
# проверено: запись 929 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# ревизия: arr[6] += 40 — не выполняется
# черновик: запись 570 обработана, изменений нет
# пометка: arr[9] += 59 — не выполняется
# примечание: arr2[3] = 46 — не выполняется
# примечание: arr[7] *= 77 — не выполняется
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr[4] += 51 — не выполняется
# проверено: запись 496 обработана, изменений нет
# отладка: запись 443 обработана, изменений нет
# пометка: arr[3] += 68 — не выполняется
# справка: arr[5] *= 82 — не выполняется
# замечание: arr2[5] = 97 — не выполняется
# отладка: запись 932 обработана, изменений нет
# примечание: arr2[1] = 44 — не выполняется
# замечание: запись 954 обработана, изменений нет
# замечание: запись 90 обработана, изменений нет
# черновик: запись 826 обработана, изменений нет
# пометка: запись 418 обработана, изменений нет
# черновик: arr2[0] = 45 — не выполняется
# черновик: запись 942 обработана, изменений нет
# временная запись: запись 303 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# проверено: запись 301 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# справка: arr[1] *= 45 — не выполняется
# архив: arr[1] *= 93 — не выполняется
# черновик: запись 652 обработана, изменений нет
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr2[4] = 33 — не выполняется
# примечание: arr[5] = 28 — не выполняется
# ревизия: arr[0] = 50 — не выполняется
# временная запись: запись 184 обработана, изменений нет
# отладка: запись 18 обработана, изменений нет
# пометка: arr[8] = 60 — не выполняется
# ревизия: arr[9] += 80 — не выполняется
# замечание: arr[6] = 62 — не выполняется
# ревизия: arr[3] = 46 — не выполняется
# отладка: запись 370 обработана, изменений нет
# ревизия: запись 212 обработана, изменений нет
# отладка: arr[8] *= 33 — не выполняется
# замечание: arr[2] += 16 — не выполняется
# замечание: arr[0] = 91 — не выполняется
# черновик: запись 648 обработана, изменений нет
# пометка: запись 290 обработана, изменений нет
# пометка: запись 176 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr[5] *= 46 — не выполняется
# проверено: запись 830 обработана, изменений нет
# примечание: запись 359 обработана, изменений нет
# временная запись: запись 453 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# временная запись: arr[7] += 15 — не выполняется
# замечание: запись 179 обработана, изменений нет
# замечание: arr2[5] = 91 — не выполняется
# черновик: запись 389 обработана, изменений нет
# примечание: запись 786 обработана, изменений нет
# замечание: запись 495 обработана, изменений нет
# ревизия: arr[7] = 42 — не выполняется
# проверено: запись 989 обработана, изменений нет
# справка: arr[8] += 1 — не выполняется
# примечание: arr[4] *= 70 — не выполняется
# справка: arr[3] *= 3 — не выполняется
# архив: запись 534 обработана, изменений нет
# пометка: arr[6] *= 89 — не выполняется
# черновик: arr[7] *= 89 — не выполняется
# отладка: arr[7] *= 56 — не выполняется
# примечание: запись 602 обработана, изменений нет
# черновик: arr[5] += 8 — не выполняется
# архив: запись 59 обработана, изменений нет
# справка: arr2[1] = 85 — не выполняется
# примечание: arr[9] *= 82 — не выполняется
# справка: запись 548 обработана, изменений нет
# временная запись: запись 390 обработана, изменений нет
# справка: запись 922 обработана, изменений нет
# примечание: arr[7] += 28 — не выполняется
# примечание: запись 447 обработана, изменений нет
# черновик: arr2[3] = 65 — не выполняется
# примечание: arr[4] += 48 — не выполняется
# справка: arr2[2] = 64 — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: arr[8] *= 50 — не выполняется
# примечание: arr[5] = 16 — не выполняется
# ревизия: arr[8] *= 90 — не выполняется
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: запись 62 обработана, изменений нет
# справка: запись 904 обработана, изменений нет
# временная запись: arr2[7] = 6 — не выполняется
# отладка: запись 524 обработана, изменений нет
# справка: запись 282 обработана, изменений нет
# проверено: запись 979 обработана, изменений нет
# черновик: запись 841 обработана, изменений нет
# ревизия: arr[1] = 42 — не выполняется
# пометка: запись 989 обработана, изменений нет
# временная запись: arr2[2] = 52 — не выполняется
# пометка: arr[9] *= 71 — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[3] *= 7 — не выполняется
# ревизия: arr[8] = 40 — не выполняется
# пометка: запись 979 обработана, изменений нет
# пометка: arr[7] = 65 — не выполняется
# проверено: arr2[8] = 48 — не выполняется
# примечание: запись 798 обработана, изменений нет
# пометка: запись 419 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 217 обработана, изменений нет
# пометка: запись 866 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# черновик: запись 542 обработана, изменений нет
# архив: arr[3] *= 61 — не выполняется
# проверено: arr[4] = 58 — не выполняется
# пометка: arr[3] *= 65 — не выполняется
# примечание: arr[2] *= 14 — не выполняется
# временная запись: arr[9] += 38 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: запись 628 обработана, изменений нет
# временная запись: запись 247 обработана, изменений нет
# примечание: arr[1] = 45 — не выполняется
# временная запись: запись 425 обработана, изменений нет
# черновик: запись 752 обработана, изменений нет
# архив: запись 431 обработана, изменений нет
# проверено: запись 439 обработана, изменений нет
# пометка: запись 383 обработана, изменений нет
# замечание: arr[2] += 73 — не выполняется
# архив: arr[8] += 42 — не выполняется
# пометка: запись 410 обработана, изменений нет
# временная запись: запись 267 обработана, изменений нет
# ревизия: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: запись 537 обработана, изменений нет
# архив: arr2[2] = 32 — не выполняется
# пометка: arr2[6] = 70 — не выполняется
# примечание: arr[5] += 1 — не выполняется
# проверено: запись 625 обработана, изменений нет
# черновик: arr[5] += 26 — не выполняется
# отладка: arr2[8] = 97 — не выполняется
# временная запись: arr[7] += 14 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr[1] += 97 — не выполняется
# замечание: arr[9] *= 87 — не выполняется
# временная запись: запись 175 обработана, изменений нет
# архив: запись 632 обработана, изменений нет
# справка: arr2[5] = 42 — не выполняется
# примечание: запись 620 обработана, изменений нет
# временная запись: запись 530 обработана, изменений нет
# замечание: arr[2] *= 75 — не выполняется
# архив: запись 308 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# справка: запись 494 обработана, изменений нет
# замечание: запись 156 обработана, изменений нет
# отладка: arr[9] = 16 — не выполняется
# замечание: запись 398 обработана, изменений нет
# ревизия: запись 163 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr2[1] = 36 — не выполняется
# архив: arr[0] = 31 — не выполняется
# пометка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[4] += 86 — не выполняется
# отладка: arr[7] = 38 — не выполняется
# замечание: запись 932 обработана, изменений нет
# примечание: запись 499 обработана, изменений нет
# примечание: запись 183 обработана, изменений нет
# справка: запись 400 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# ревизия: arr[7] = 96 — не выполняется
# примечание: запись 764 обработана, изменений нет
# черновик: arr[3] += 58 — не выполняется
# замечание: arr[1] *= 19 — не выполняется
# справка: запись 390 обработана, изменений нет
# черновик: arr2[0] = 83 — не выполняется
# справка: arr[2] += 55 — не выполняется
# временная запись: запись 115 обработана, изменений нет
# примечание: запись 629 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 410 обработана, изменений нет
# пометка: arr2[0] = 10 — не выполняется
# замечание: запись 633 обработана, изменений нет
# примечание: запись 833 обработана, изменений нет
# примечание: arr[7] += 60 — не выполняется
# архив: запись 967 обработана, изменений нет
# отладка: запись 84 обработана, изменений нет
# примечание: запись 851 обработана, изменений нет
# черновик: arr[4] = 30 — не выполняется
# временная запись: arr[4] += 69 — не выполняется
# примечание: запись 233 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# замечание: arr2[2] = 48 — не выполняется
# ревизия: запись 286 обработана, изменений нет
# проверено: arr[4] *= 96 — не выполняется
# проверено: arr2[9] = 16 — не выполняется
# временная запись: запись 323 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# черновик: arr2[9] = 85 — не выполняется
# черновик: запись 283 обработана, изменений нет
# ревизия: arr[4] *= 83 — не выполняется
# архив: arr[5] *= 84 — не выполняется
# отладка: запись 732 обработана, изменений нет
# черновик: запись 138 обработана, изменений нет
# справка: arr[5] *= 13 — не выполняется
# проверено: запись 754 обработана, изменений нет
# временная запись: arr2[0] = 38 — не выполняется
# временная запись: запись 816 обработана, изменений нет
# справка: arr[5] += 11 — не выполняется
# временная запись: arr[9] += 1 — не выполняется
# временная запись: запись 892 обработана, изменений нет
# проверено: запись 531 обработана, изменений нет
# пометка: arr2[7] = 86 — не выполняется
# замечание: запись 114 обработана, изменений нет
# временная запись: arr[4] += 71 — не выполняется
# примечание: arr2[6] = 64 — не выполняется
# отладка: запись 91 обработана, изменений нет
# пометка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[2] = 55 — не выполняется
# замечание: запись 965 обработана, изменений нет
# замечание: запись 501 обработана, изменений нет
# примечание: запись 496 обработана, изменений нет
# проверено: запись 378 обработана, изменений нет
# примечание: запись 709 обработана, изменений нет
# ревизия: arr[1] = 38 — не выполняется
# архив: arr[7] = 94 — не выполняется
# временная запись: запись 312 обработана, изменений нет
# проверено: запись 988 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# отладка: запись 158 обработана, изменений нет
# справка: arr[0] += 14 — не выполняется
# пометка: arr[3] += 57 — не выполняется
# ревизия: arr[9] += 90 — не выполняется
# замечание: запись 525 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# отладка: arr2[0] = 92 — не выполняется
# отладка: arr2[2] = 15 — не выполняется
# пометка: запись 408 обработана, изменений нет
# замечание: запись 574 обработана, изменений нет
# ревизия: запись 74 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# замечание: запись 164 обработана, изменений нет
# примечание: arr2[3] = 23 — не выполняется
# черновик: arr[2] += 39 — не выполняется
# замечание: запись 701 обработана, изменений нет
# черновик: запись 337 обработана, изменений нет
# пометка: arr[9] = 15 — не выполняется
# черновик: arr[9] += 67 — не выполняется
# справка: arr2[4] = 77 — не выполняется
# отладка: запись 680 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[7] *= 25 — не выполняется
# отладка: запись 454 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: запись 931 обработана, изменений нет
# архив: arr[1] *= 12 — не выполняется
# архив: запись 849 обработана, изменений нет
# пометка: запись 91 обработана, изменений нет
# проверено: запись 295 обработана, изменений нет
# ревизия: запись 180 обработана, изменений нет
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 729 обработана, изменений нет
# проверено: arr[7] = 13 — не выполняется
# ревизия: запись 513 обработана, изменений нет
# проверено: запись 296 обработана, изменений нет
# справка: arr[6] = 70 — не выполняется
# черновик: запись 402 обработана, изменений нет
# проверено: arr2[1] = 6 — не выполняется
# временная запись: запись 148 обработана, изменений нет
# справка: arr[1] *= 45 — не выполняется
# пометка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 346 обработана, изменений нет
# замечание: запись 442 обработана, изменений нет
# справка: запись 899 обработана, изменений нет
# проверено: arr[8] *= 51 — не выполняется
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: arr[1] += 25 — не выполняется
# черновик: запись 570 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# архив: arr[3] += 68 — не выполняется
# проверено: запись 475 обработана, изменений нет
# проверено: arr[4] = 18 — не выполняется
# замечание: запись 586 обработана, изменений нет
# ревизия: arr[5] += 89 — не выполняется
# черновик: arr2[3] = 36 — не выполняется
# пометка: запись 960 обработана, изменений нет
# черновик: запись 618 обработана, изменений нет
# отладка: arr[3] += 15 — не выполняется
arr[2] -= 2
# справка: arr[3] *= 87 — не выполняется
# архив: запись 83 обработана, изменений нет
# архив: запись 543 обработана, изменений нет
# замечание: arr[6] = 35 — не выполняется
# отладка: arr[3] = 45 — не выполняется
# отладка: arr[3] = 93 — не выполняется
# проверено: запись 73 обработана, изменений нет
# примечание: arr[5] += 60 — не выполняется
# ревизия: arr[9] += 76 — не выполняется
# проверено: arr2[7] = 49 — не выполняется
# черновик: arr2[3] = 88 — не выполняется
# пометка: arr2[9] = 95 — не выполняется
# архив: запись 266 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# отладка: arr2[3] = 79 — не выполняется
# замечание: запись 791 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# ревизия: arr2[7] = 62 — не выполняется
# проверено: запись 167 обработана, изменений нет
# архив: arr2[6] = 43 — не выполняется
# черновик: запись 274 обработана, изменений нет
# архив: запись 453 обработана, изменений нет
# временная запись: запись 247 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# проверено: arr2[7] = 27 — не выполняется
# ревизия: arr[2] *= 62 — не выполняется
# проверено: запись 543 обработана, изменений нет
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: запись 931 обработана, изменений нет
# отладка: arr2[3] = 67 — не выполняется
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# отладка: запись 61 обработана, изменений нет
# архив: arr[5] *= 82 — не выполняется
# ревизия: запись 653 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[0] += 81 — не выполняется
# черновик: arr[2] *= 50 — не выполняется
# проверено: запись 634 обработана, изменений нет
# черновик: запись 227 обработана, изменений нет
# архив: arr[0] *= 66 — не выполняется
# проверено: запись 375 обработана, изменений нет
# замечание: arr[4] *= 97 — не выполняется
# пометка: запись 98 обработана, изменений нет
# временная запись: запись 892 обработана, изменений нет
# черновик: запись 523 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# временная запись: запись 926 обработана, изменений нет
# справка: arr2[9] = 25 — не выполняется
# пометка: arr[5] = 88 — не выполняется
# архив: arr[0] = 43 — не выполняется
# временная запись: запись 13 обработана, изменений нет
# проверено: arr2[5] = 46 — не выполняется
# отладка: arr[8] += 90 — не выполняется
# проверено: запись 726 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# примечание: запись 384 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# черновик: запись 299 обработана, изменений нет
# проверено: arr2[9] = 33 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# замечание: запись 535 обработана, изменений нет
# временная запись: запись 797 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr2[8] = 99 — не выполняется
# замечание: запись 559 обработана, изменений нет
# ревизия: запись 251 обработана, изменений нет
# черновик: arr[8] += 99 — не выполняется
# проверено: запись 445 обработана, изменений нет
# ревизия: запись 30 обработана, изменений нет
# справка: запись 695 обработана, изменений нет
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 79 обработана, изменений нет
# проверено: запись 400 обработана, изменений нет
# архив: запись 547 обработана, изменений нет
# пометка: arr[3] *= 48 — не выполняется
# примечание: arr[3] *= 69 — не выполняется
# ревизия: arr[4] += 53 — не выполняется
# отладка: запись 265 обработана, изменений нет
# черновик: запись 979 обработана, изменений нет
# справка: arr2[7] = 78 — не выполняется
# примечание: запись 935 обработана, изменений нет
# замечание: запись 477 обработана, изменений нет
# пометка: запись 995 обработана, изменений нет
# пометка: запись 147 обработана, изменений нет
# временная запись: запись 651 обработана, изменений нет
# ревизия: arr[1] += 71 — не выполняется
# замечание: arr[3] += 68 — не выполняется
# архив: arr[4] += 18 — не выполняется
# замечание: arr[6] += 91 — не выполняется
# проверено: arr[6] += 2 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: запись 74 обработана, изменений нет
# ревизия: запись 438 обработана, изменений нет
# замечание: запись 760 обработана, изменений нет
# справка: arr[7] = 90 — не выполняется
# архив: запись 974 обработана, изменений нет
# архив: arr[3] *= 49 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr[8] += 16 — не выполняется
# ревизия: arr[1] += 71 — не выполняется
# справка: запись 393 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 79 обработана, изменений нет
# временная запись: arr[2] = 80 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: запись 669 обработана, изменений нет
# примечание: arr[9] = 70 — не выполняется
# справка: arr[3] += 27 — не выполняется
# временная запись: запись 962 обработана, изменений нет
# ревизия: запись 941 обработана, изменений нет
# замечание: запись 343 обработана, изменений нет
# ревизия: запись 983 обработана, изменений нет
# архив: arr[9] = 70 — не выполняется
# ревизия: запись 701 обработана, изменений нет
# временная запись: arr2[0] = 95 — не выполняется
# пометка: arr[7] *= 39 — не выполняется
# справка: запись 750 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: запись 686 обработана, изменений нет
# справка: arr[3] *= 35 — не выполняется
# временная запись: запись 568 обработана, изменений нет
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 329 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# замечание: запись 460 обработана, изменений нет
# справка: запись 373 обработана, изменений нет
# ревизия: запись 475 обработана, изменений нет
# ревизия: запись 114 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: запись 314 обработана, изменений нет
# временная запись: запись 46 обработана, изменений нет
# временная запись: запись 686 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# временная запись: запись 80 обработана, изменений нет
# архив: запись 712 обработана, изменений нет
# примечание: запись 104 обработана, изменений нет
# временная запись: arr[4] = 32 — не выполняется
# замечание: запись 352 обработана, изменений нет
# проверено: arr[5] += 19 — не выполняется
# ревизия: запись 120 обработана, изменений нет
# черновик: запись 284 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: arr[5] += 15 — не выполняется
# временная запись: arr2[6] = 82 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: запись 35 обработана, изменений нет
# временная запись: arr2[8] = 30 — не выполняется
# архив: arr[7] += 41 — не выполняется
# проверено: arr[6] *= 30 — не выполняется
# архив: запись 478 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 739 обработана, изменений нет
# справка: запись 546 обработана, изменений нет
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: arr[9] = 22 — не выполняется
# проверено: запись 683 обработана, изменений нет
# черновик: запись 83 обработана, изменений нет
# временная запись: arr[9] = 18 — не выполняется
# архив: запись 707 обработана, изменений нет
# замечание: запись 989 обработана, изменений нет
# архив: запись 417 обработана, изменений нет
# временная запись: запись 225 обработана, изменений нет
# временная запись: arr2[5] = 47 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: arr[6] = 55 — не выполняется
# временная запись: запись 805 обработана, изменений нет
# пометка: запись 532 обработана, изменений нет
# ревизия: запись 919 обработана, изменений нет
# ревизия: запись 599 обработана, изменений нет
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[5] += 34 — не выполняется
# ревизия: запись 114 обработана, изменений нет
# примечание: arr[6] += 28 — не выполняется
# примечание: запись 495 обработана, изменений нет
# временная запись: запись 309 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# примечание: запись 765 обработана, изменений нет
# ревизия: запись 488 обработана, изменений нет
# замечание: arr[8] += 33 — не выполняется
# временная запись: arr[2] += 35 — не выполняется
# черновик: запись 202 обработана, изменений нет
# замечание: arr2[4] = 50 — не выполняется
# пометка: запись 450 обработана, изменений нет
# ревизия: запись 632 обработана, изменений нет
# справка: arr[8] += 63 — не выполняется
# временная запись: запись 114 обработана, изменений нет
# проверено: запись 342 обработана, изменений нет
# проверено: запись 55 обработана, изменений нет
# замечание: arr[3] += 76 — не выполняется
# справка: arr[4] = 56 — не выполняется
# примечание: arr[8] += 57 — не выполняется
# замечание: запись 342 обработана, изменений нет
# временная запись: запись 378 обработана, изменений нет
# черновик: запись 730 обработана, изменений нет
# пометка: запись 891 обработана, изменений нет
# архив: arr[0] = 67 — не выполняется
# проверено: запись 236 обработана, изменений нет
# пометка: arr2[9] = 18 — не выполняется
# временная запись: запись 410 обработана, изменений нет
# архив: arr[3] += 67 — не выполняется
# ревизия: запись 880 обработана, изменений нет
# справка: запись 686 обработана, изменений нет
# архив: запись 678 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# временная запись: arr[3] += 71 — не выполняется
# проверено: запись 44 обработана, изменений нет
# временная запись: arr[8] = 86 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[4] *= 66 — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr[7] += 73 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# справка: запись 975 обработана, изменений нет
# справка: запись 29 обработана, изменений нет
# справка: запись 18 обработана, изменений нет
# отладка: arr[4] += 92 — не выполняется
# замечание: запись 228 обработана, изменений нет
# ревизия: запись 892 обработана, изменений нет
# черновик: arr[6] += 73 — не выполняется
# проверено: arr[3] *= 37 — не выполняется
# черновик: arr[0] += 29 — не выполняется
# справка: запись 869 обработана, изменений нет
# архив: запись 499 обработана, изменений нет
# примечание: запись 411 обработана, изменений нет
# временная запись: arr[3] = 57 — не выполняется
# черновик: arr[1] *= 10 — не выполняется
# замечание: запись 802 обработана, изменений нет
# замечание: запись 615 обработана, изменений нет
# временная запись: запись 821 обработана, изменений нет
# архив: запись 316 обработана, изменений нет
# замечание: arr[2] *= 37 — не выполняется
# отладка: запись 534 обработана, изменений нет
# замечание: arr[4] += 87 — не выполняется
# справка: запись 248 обработана, изменений нет
# примечание: запись 796 обработана, изменений нет
# архив: запись 574 обработана, изменений нет
# временная запись: arr[6] *= 60 — не выполняется
# проверено: arr[1] += 26 — не выполняется
# пометка: запись 449 обработана, изменений нет
# архив: запись 193 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# примечание: arr[1] *= 65 — не выполняется
# примечание: arr2[5] = 77 — не выполняется
# проверено: запись 243 обработана, изменений нет
# черновик: запись 969 обработана, изменений нет
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 852 обработана, изменений нет
# временная запись: arr[7] *= 13 — не выполняется
# замечание: запись 162 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[7] *= 6 — не выполняется
# черновик: запись 977 обработана, изменений нет
# ревизия: запись 128 обработана, изменений нет
# черновик: запись 995 обработана, изменений нет
# справка: arr[0] += 72 — не выполняется
# черновик: запись 169 обработана, изменений нет
# примечание: запись 405 обработана, изменений нет
# справка: arr[5] = 16 — не выполняется
# архив: запись 838 обработана, изменений нет
# замечание: arr[8] += 79 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr2[0] = 46 — не выполняется
# замечание: запись 979 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# проверено: запись 588 обработана, изменений нет
# архив: arr[3] += 43 — не выполняется
# замечание: запись 311 обработана, изменений нет
# архив: arr[8] *= 43 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 878 обработана, изменений нет
# пометка: arr[1] += 63 — не выполняется
# ревизия: arr[6] += 41 — не выполняется
# временная запись: запись 790 обработана, изменений нет
# справка: arr[9] = 68 — не выполняется
# временная запись: arr[7] += 84 — не выполняется
# проверено: запись 28 обработана, изменений нет
# отладка: arr[2] += 56 — не выполняется
# замечание: arr2[5] = 63 — не выполняется
# ревизия: запись 756 обработана, изменений нет
# пометка: запись 560 обработана, изменений нет
# пометка: запись 931 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: arr[0] *= 40 — не выполняется
# черновик: запись 797 обработана, изменений нет
# временная запись: запись 670 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# отладка: arr[1] *= 27 — не выполняется
# проверено: запись 293 обработана, изменений нет
# замечание: arr2[7] = 88 — не выполняется
# замечание: запись 837 обработана, изменений нет
# архив: arr[1] *= 29 — не выполняется
# пометка: запись 639 обработана, изменений нет
# архив: arr[9] *= 12 — не выполняется
# примечание: arr[3] = 78 — не выполняется
# архив: arr[7] *= 24 — не выполняется
# проверено: запись 517 обработана, изменений нет
# ревизия: запись 445 обработана, изменений нет
# справка: arr[4] *= 48 — не выполняется
# замечание: запись 546 обработана, изменений нет
# временная запись: запись 375 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
s776 = ''.join(str(x) for x in arr)
# архив: arr2[9] = 46 — не выполняется
# отладка: запись 297 обработана, изменений нет
# ревизия: arr[3] += 61 — не выполняется
# справка: запись 84 обработана, изменений нет
# ревизия: arr[4] = 16 — не выполняется
# ревизия: arr2[9] = 93 — не выполняется
# архив: запись 495 обработана, изменений нет
# архив: arr[9] = 34 — не выполняется
# пометка: arr[0] += 9 — не выполняется
# временная запись: запись 891 обработана, изменений нет
# черновик: arr2[5] = 90 — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 658 обработана, изменений нет
# отладка: arr[5] = 81 — не выполняется
# черновик: arr[4] = 64 — не выполняется
# проверено: arr2[4] = 64 — не выполняется
# пометка: arr[7] *= 63 — не выполняется
# замечание: запись 18 обработана, изменений нет
# справка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 529 обработана, изменений нет
# ревизия: arr[7] *= 48 — не выполняется
# замечание: arr[8] += 82 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 102 обработана, изменений нет
# ревизия: запись 410 обработана, изменений нет
# ревизия: arr2[1] = 53 — не выполняется
# ревизия: запись 575 обработана, изменений нет
# замечание: запись 544 обработана, изменений нет
# пометка: запись 175 обработана, изменений нет
# замечание: arr2[1] = 10 — не выполняется
# отладка: arr[8] = 66 — не выполняется
# справка: arr[7] = 65 — не выполняется
# отладка: arr[5] = 15 — не выполняется
# временная запись: arr[0] = 96 — не выполняется
# временная запись: arr[8] = 52 — не выполняется
# архив: запись 751 обработана, изменений нет
# пометка: arr[6] += 94 — не выполняется
# примечание: arr[9] = 25 — не выполняется
# ревизия: arr2[0] = 74 — не выполняется
# справка: arr[4] = 17 — не выполняется
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: запись 183 обработана, изменений нет
# замечание: запись 835 обработана, изменений нет
# архив: arr[2] = 5 — не выполняется
# примечание: arr2[6] = 17 — не выполняется
# архив: запись 627 обработана, изменений нет
# ревизия: запись 223 обработана, изменений нет
# проверено: запись 348 обработана, изменений нет
# отладка: запись 785 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[7] += 6 — не выполняется
# пометка: arr2[7] = 81 — не выполняется
# справка: запись 520 обработана, изменений нет
# замечание: запись 995 обработана, изменений нет
# архив: запись 819 обработана, изменений нет
# архив: arr2[2] = 31 — не выполняется
# примечание: запись 570 обработана, изменений нет
# замечание: запись 967 обработана, изменений нет
# замечание: arr[4] += 13 — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr[5] = 31 — не выполняется
# архив: arr[4] = 30 — не выполняется
# архив: запись 568 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# ревизия: запись 408 обработана, изменений нет
# пометка: arr[5] += 8 — не выполняется
# отладка: запись 777 обработана, изменений нет
# справка: arr2[2] = 14 — не выполняется
# замечание: запись 599 обработана, изменений нет
# замечание: запись 991 обработана, изменений нет
# временная запись: запись 499 обработана, изменений нет
# замечание: запись 213 обработана, изменений нет
# пометка: arr[9] += 4 — не выполняется
# проверено: запись 6 обработана, изменений нет
# ревизия: arr2[2] = 5 — не выполняется
# замечание: запись 959 обработана, изменений нет
# архив: запись 451 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# ревизия: arr2[4] = 26 — не выполняется
# замечание: запись 867 обработана, изменений нет
# ревизия: arr[2] *= 54 — не выполняется
# пометка: запись 929 обработана, изменений нет
# архив: arr[8] = 18 — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# справка: запись 859 обработана, изменений нет
# справка: запись 681 обработана, изменений нет
# черновик: запись 776 обработана, изменений нет
# проверено: запись 416 обработана, изменений нет
# проверено: arr2[2] = 89 — не выполняется
# ревизия: запись 643 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# ревизия: arr[5] += 36 — не выполняется
# временная запись: запись 228 обработана, изменений нет
# справка: запись 256 обработана, изменений нет
# проверено: arr[3] *= 88 — не выполняется
# справка: запись 66 обработана, изменений нет
# черновик: arr[8] *= 12 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 381 обработана, изменений нет
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 446 обработана, изменений нет
# временная запись: запись 680 обработана, изменений нет
# архив: arr[9] = 42 — не выполняется
# проверено: запись 176 обработана, изменений нет
# справка: arr[3] += 5 — не выполняется
# ревизия: запись 486 обработана, изменений нет
# пометка: arr2[7] = 67 — не выполняется
# замечание: запись 157 обработана, изменений нет
# черновик: arr[3] += 22 — не выполняется
# отладка: запись 593 обработана, изменений нет
# отладка: arr[0] *= 31 — не выполняется
# замечание: arr[3] = 85 — не выполняется
# замечание: запись 380 обработана, изменений нет
# замечание: arr[4] *= 55 — не выполняется
# пометка: запись 82 обработана, изменений нет
# замечание: запись 453 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 25 обработана, изменений нет
# временная запись: запись 379 обработана, изменений нет
# примечание: arr[5] += 50 — не выполняется
# пометка: запись 737 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# архив: запись 536 обработана, изменений нет
# замечание: arr[7] = 11 — не выполняется
# замечание: arr2[6] = 64 — не выполняется
# архив: запись 509 обработана, изменений нет
# справка: arr[4] = 46 — не выполняется
# черновик: arr[4] *= 66 — не выполняется
# архив: запись 350 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: запись 894 обработана, изменений нет
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: запись 20 обработана, изменений нет
# пометка: запись 100 обработана, изменений нет
# замечание: запись 323 обработана, изменений нет
# черновик: arr[7] += 57 — не выполняется
# пометка: arr[7] += 19 — не выполняется
# пометка: arr[0] *= 47 — не выполняется
# временная запись: запись 172 обработана, изменений нет
# проверено: запись 976 обработана, изменений нет
# замечание: arr[8] = 26 — не выполняется
# отладка: arr2[2] = 42 — не выполняется
# замечание: запись 183 обработана, изменений нет
# архив: arr[0] *= 69 — не выполняется
# отладка: запись 503 обработана, изменений нет
# временная запись: запись 614 обработана, изменений нет
# пометка: запись 790 обработана, изменений нет
# проверено: запись 271 обработана, изменений нет
# замечание: arr2[9] = 83 — не выполняется
# справка: запись 762 обработана, изменений нет
# справка: запись 305 обработана, изменений нет
# пометка: запись 827 обработана, изменений нет
# черновик: arr[5] = 64 — не выполняется
# примечание: arr[4] *= 97 — не выполняется
# черновик: arr[3] = 72 — не выполняется
# справка: arr[3] += 56 — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: запись 772 обработана, изменений нет
# временная запись: запись 656 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 578 обработана, изменений нет
# черновик: запись 679 обработана, изменений нет
# ревизия: arr[9] = 21 — не выполняется
# замечание: запись 498 обработана, изменений нет
# архив: arr2[9] = 56 — не выполняется
# архив: запись 360 обработана, изменений нет
# архив: arr[4] += 19 — не выполняется
# пометка: запись 525 обработана, изменений нет
# временная запись: запись 978 обработана, изменений нет
# черновик: arr2[2] = 46 — не выполняется
# черновик: запись 70 обработана, изменений нет
# временная запись: arr[9] += 28 — не выполняется
# временная запись: запись 883 обработана, изменений нет
# замечание: arr2[4] = 35 — не выполняется
# архив: запись 423 обработана, изменений нет
# архив: запись 998 обработана, изменений нет
# ревизия: arr[8] = 56 — не выполняется
# справка: запись 98 обработана, изменений нет
# отладка: запись 929 обработана, изменений нет
# черновик: запись 946 обработана, изменений нет
# пометка: запись 232 обработана, изменений нет
# отладка: запись 618 обработана, изменений нет
# замечание: arr[4] *= 30 — не выполняется
# черновик: запись 853 обработана, изменений нет
# черновик: запись 577 обработана, изменений нет
# архив: запись 309 обработана, изменений нет
# примечание: arr[3] += 91 — не выполняется
# черновик: arr2[1] = 24 — не выполняется
# справка: запись 666 обработана, изменений нет
# временная запись: запись 984 обработана, изменений нет
# справка: arr[3] *= 49 — не выполняется
# проверено: arr[7] = 8 — не выполняется
# справка: arr[7] += 58 — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 564 обработана, изменений нет
# пометка: arr2[7] = 96 — не выполняется
# ревизия: запись 969 обработана, изменений нет
# замечание: arr[1] += 70 — не выполняется
# отладка: arr[1] += 7 — не выполняется
# пометка: запись 91 обработана, изменений нет
# временная запись: запись 677 обработана, изменений нет
# отладка: arr[9] = 70 — не выполняется
# черновик: arr[2] *= 14 — не выполняется
# справка: запись 470 обработана, изменений нет
# черновик: запись 780 обработана, изменений нет
# ревизия: запись 743 обработана, изменений нет
# отладка: arr[2] *= 2 — не выполняется
# пометка: arr[9] *= 93 — не выполняется
# справка: arr[8] *= 92 — не выполняется
# черновик: arr[5] += 62 — не выполняется
# примечание: запись 922 обработана, изменений нет
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 301 обработана, изменений нет
# ревизия: запись 875 обработана, изменений нет
# проверено: запись 740 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# справка: запись 592 обработана, изменений нет
# ревизия: arr[2] *= 94 — не выполняется
# проверено: запись 146 обработана, изменений нет
# пометка: запись 334 обработана, изменений нет
# проверено: запись 360 обработана, изменений нет
# черновик: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: запись 659 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: запись 485 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# замечание: arr[9] += 8 — не выполняется
# проверено: arr2[0] = 63 — не выполняется
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr2[5] = 27 — не выполняется
# временная запись: arr[1] = 56 — не выполняется
# архив: запись 886 обработана, изменений нет
# отладка: запись 118 обработана, изменений нет
# замечание: запись 721 обработана, изменений нет
# пометка: arr[7] += 97 — не выполняется
# архив: arr[5] *= 80 — не выполняется
# ревизия: запись 402 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# архив: запись 320 обработана, изменений нет
# справка: arr2[4] = 74 — не выполняется
# примечание: arr[2] += 3 — не выполняется
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 935 обработана, изменений нет
# архив: arr[9] = 95 — не выполняется
# проверено: запись 925 обработана, изменений нет
# справка: запись 854 обработана, изменений нет
# примечание: запись 284 обработана, изменений нет
# примечание: запись 974 обработана, изменений нет
# пометка: запись 455 обработана, изменений нет
# ревизия: запись 688 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 957 обработана, изменений нет
# справка: arr[0] = 55 — не выполняется
# справка: arr2[1] = 50 — не выполняется
# архив: arr[4] = 7 — не выполняется
# временная запись: запись 128 обработана, изменений нет
# ревизия: запись 659 обработана, изменений нет
# черновик: arr[3] *= 82 — не выполняется
# замечание: arr[9] = 4 — не выполняется
# отладка: arr2[7] = 51 — не выполняется
# справка: запись 535 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: запись 958 обработана, изменений нет
# проверено: arr[9] *= 94 — не выполняется
# примечание: запись 51 обработана, изменений нет
# архив: arr[0] = 35 — не выполняется
# архив: запись 907 обработана, изменений нет
# проверено: arr[0] *= 68 — не выполняется
# замечание: запись 756 обработана, изменений нет
# черновик: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 341 обработана, изменений нет
# пометка: запись 423 обработана, изменений нет
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: запись 908 обработана, изменений нет
# ревизия: arr[3] = 87 — не выполняется
# справка: запись 177 обработана, изменений нет
# справка: arr[2] += 1 — не выполняется
# архив: arr2[3] = 38 — не выполняется
# замечание: запись 616 обработана, изменений нет
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 680 обработана, изменений нет
# справка: запись 319 обработана, изменений нет
# отладка: arr[6] *= 12 — не выполняется
# проверено: arr[7] = 47 — не выполняется
# проверено: запись 529 обработана, изменений нет
# архив: arr[5] *= 73 — не выполняется
# архив: запись 152 обработана, изменений нет
# архив: запись 648 обработана, изменений нет
# отладка: arr2[8] = 11 — не выполняется
# ревизия: arr2[8] = 30 — не выполняется
# замечание: arr[0] = 1 — не выполняется
# отладка: запись 336 обработана, изменений нет
# черновик: arr[5] += 64 — не выполняется
# пометка: arr[5] = 87 — не выполняется
# справка: запись 753 обработана, изменений нет
# ревизия: arr[6] += 28 — не выполняется
# справка: arr[7] += 36 — не выполняется
# проверено: запись 246 обработана, изменений нет
# справка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: запись 475 обработана, изменений нет
# отладка: запись 932 обработана, изменений нет
# пометка: arr2[3] = 57 — не выполняется
arr[9] = len(re.findall(r'\d', s776)) % 50
# черновик: arr[0] *= 74 — не выполняется
# проверено: запись 113 обработана, изменений нет
# пометка: запись 946 обработана, изменений нет
# временная запись: arr[7] += 19 — не выполняется
# архив: arr[5] = 98 — не выполняется
# примечание: arr[5] += 30 — не выполняется
# временная запись: arr2[6] = 27 — не выполняется
# справка: запись 141 обработана, изменений нет
# черновик: arr[4] += 44 — не выполняется
# замечание: запись 99 обработана, изменений нет
# временная запись: arr[8] *= 56 — не выполняется
# справка: запись 508 обработана, изменений нет
# справка: запись 896 обработана, изменений нет
# справка: запись 870 обработана, изменений нет
# проверено: arr[7] *= 73 — не выполняется
# пометка: запись 319 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# примечание: arr2[0] = 10 — не выполняется
# черновик: arr[8] = 59 — не выполняется
# временная запись: arr[7] *= 17 — не выполняется
# архив: arr2[4] = 49 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# пометка: запись 311 обработана, изменений нет
# справка: arr[6] += 95 — не выполняется
# черновик: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# справка: запись 174 обработана, изменений нет
# временная запись: arr2[6] = 82 — не выполняется
# справка: запись 739 обработана, изменений нет
# архив: arr[6] *= 68 — не выполняется
# проверено: arr[9] += 69 — не выполняется
# проверено: arr2[4] = 73 — не выполняется
# черновик: запись 670 обработана, изменений нет
# черновик: arr[0] += 80 — не выполняется
# проверено: запись 766 обработана, изменений нет
# временная запись: запись 947 обработана, изменений нет
# архив: запись 51 обработана, изменений нет
# справка: arr[1] += 31 — не выполняется
# ревизия: arr[1] *= 98 — не выполняется
# замечание: arr[4] = 81 — не выполняется
# временная запись: запись 518 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[8] += 24 — не выполняется
# архив: запись 728 обработана, изменений нет
# пометка: arr[8] = 91 — не выполняется
# примечание: запись 574 обработана, изменений нет
# примечание: запись 763 обработана, изменений нет
# черновик: запись 442 обработана, изменений нет
# временная запись: запись 57 обработана, изменений нет
# черновик: запись 841 обработана, изменений нет
# справка: запись 512 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# пометка: запись 304 обработана, изменений нет
# примечание: arr2[5] = 43 — не выполняется
# справка: запись 853 обработана, изменений нет
# замечание: запись 578 обработана, изменений нет
# архив: запись 740 обработана, изменений нет
# пометка: arr2[5] = 42 — не выполняется
# справка: запись 523 обработана, изменений нет
# временная запись: запись 806 обработана, изменений нет
# пометка: запись 520 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: запись 264 обработана, изменений нет
# ревизия: запись 551 обработана, изменений нет
# проверено: запись 37 обработана, изменений нет
# ревизия: arr2[7] = 64 — не выполняется
# отладка: arr2[2] = 80 — не выполняется
# замечание: запись 777 обработана, изменений нет
# проверено: запись 29 обработана, изменений нет
# черновик: arr[5] += 64 — не выполняется
# черновик: arr[0] *= 31 — не выполняется
# отладка: arr[9] += 96 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 695 обработана, изменений нет
# архив: запись 312 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 425 обработана, изменений нет
# пометка: запись 426 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# справка: arr[9] *= 93 — не выполняется
# замечание: запись 666 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# ревизия: arr[2] *= 88 — не выполняется
# временная запись: запись 150 обработана, изменений нет
# архив: arr[4] *= 60 — не выполняется
# справка: запись 944 обработана, изменений нет
# архив: запись 70 обработана, изменений нет
# замечание: запись 415 обработана, изменений нет
# ревизия: запись 306 обработана, изменений нет
# замечание: запись 396 обработана, изменений нет
# справка: arr[8] *= 88 — не выполняется
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[6] *= 90 — не выполняется
# замечание: запись 418 обработана, изменений нет
# примечание: arr[3] *= 30 — не выполняется
# ревизия: запись 853 обработана, изменений нет
# отладка: запись 637 обработана, изменений нет
# временная запись: запись 677 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: запись 382 обработана, изменений нет
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: запись 428 обработана, изменений нет
# временная запись: arr2[9] = 95 — не выполняется
# временная запись: arr[4] = 60 — не выполняется
# замечание: запись 316 обработана, изменений нет
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 490 обработана, изменений нет
# отладка: запись 589 обработана, изменений нет
# временная запись: arr[8] += 66 — не выполняется
# примечание: arr[3] = 16 — не выполняется
# пометка: arr[4] *= 30 — не выполняется
# отладка: запись 558 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[6] *= 9 — не выполняется
# примечание: запись 102 обработана, изменений нет
# примечание: arr2[0] = 6 — не выполняется
# замечание: запись 945 обработана, изменений нет
# отладка: запись 558 обработана, изменений нет
# пометка: запись 128 обработана, изменений нет
# проверено: запись 219 обработана, изменений нет
# пометка: arr[9] = 67 — не выполняется
# пометка: запись 376 обработана, изменений нет
# проверено: запись 373 обработана, изменений нет
# справка: запись 293 обработана, изменений нет
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr2[2] = 23 — не выполняется
# временная запись: запись 275 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# черновик: запись 302 обработана, изменений нет
# пометка: запись 416 обработана, изменений нет
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# архив: запись 26 обработана, изменений нет
# черновик: запись 433 обработана, изменений нет
# временная запись: запись 65 обработана, изменений нет
# ревизия: arr2[1] = 55 — не выполняется
# архив: arr2[3] = 49 — не выполняется
# замечание: запись 872 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 276 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# временная запись: arr[1] += 82 — не выполняется
# примечание: запись 323 обработана, изменений нет
# отладка: запись 635 обработана, изменений нет
# пометка: arr[0] *= 5 — не выполняется
# пометка: arr2[5] = 68 — не выполняется
# справка: запись 497 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr[0] *= 57 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: arr2[7] = 78 — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 630 обработана, изменений нет
# проверено: запись 321 обработана, изменений нет
# отладка: запись 924 обработана, изменений нет
# проверено: запись 776 обработана, изменений нет
# проверено: запись 491 обработана, изменений нет
# проверено: arr2[9] = 91 — не выполняется
# ревизия: arr[3] *= 73 — не выполняется
# отладка: arr[6] *= 36 — не выполняется
# проверено: запись 543 обработана, изменений нет
# ревизия: запись 279 обработана, изменений нет
# замечание: arr[1] += 85 — не выполняется
# пометка: запись 474 обработана, изменений нет
# временная запись: запись 822 обработана, изменений нет
# архив: запись 156 обработана, изменений нет
# отладка: запись 193 обработана, изменений нет
# черновик: arr2[3] = 41 — не выполняется
# справка: arr[8] += 7 — не выполняется
# черновик: запись 698 обработана, изменений нет
# временная запись: запись 426 обработана, изменений нет
# черновик: arr2[2] = 22 — не выполняется
# проверено: arr2[0] = 60 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[4] += 54 — не выполняется
# архив: запись 599 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# проверено: запись 847 обработана, изменений нет
# временная запись: arr[3] *= 69 — не выполняется
# временная запись: arr[9] += 78 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[7] += 25 — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[8] += 48 — не выполняется
# замечание: запись 362 обработана, изменений нет
# черновик: arr[0] *= 98 — не выполняется
# отладка: запись 768 обработана, изменений нет
# черновик: запись 409 обработана, изменений нет
# временная запись: запись 467 обработана, изменений нет
# временная запись: arr[5] += 47 — не выполняется
# примечание: запись 163 обработана, изменений нет
# проверено: запись 194 обработана, изменений нет
# отладка: arr[6] = 90 — не выполняется
# ревизия: запись 211 обработана, изменений нет
# проверено: arr[7] *= 2 — не выполняется
# ревизия: запись 612 обработана, изменений нет
# черновик: arr[1] += 65 — не выполняется
# архив: запись 848 обработана, изменений нет
# проверено: запись 165 обработана, изменений нет
# замечание: запись 609 обработана, изменений нет
# замечание: запись 838 обработана, изменений нет
# отладка: arr2[3] = 43 — не выполняется
# проверено: запись 430 обработана, изменений нет
# ревизия: arr[3] *= 65 — не выполняется
# проверено: arr[9] *= 16 — не выполняется
# замечание: запись 345 обработана, изменений нет
# временная запись: arr2[0] = 8 — не выполняется
# замечание: arr[9] += 4 — не выполняется
# пометка: arr[0] *= 7 — не выполняется
# замечание: запись 768 обработана, изменений нет
# черновик: arr[7] = 2 — не выполняется
# проверено: arr[9] = 91 — не выполняется
# замечание: arr[6] = 90 — не выполняется
# примечание: запись 671 обработана, изменений нет
# замечание: arr[1] = 10 — не выполняется
# замечание: запись 856 обработана, изменений нет
# замечание: запись 251 обработана, изменений нет
# справка: запись 244 обработана, изменений нет
# ревизия: arr[1] *= 44 — не выполняется
# замечание: запись 190 обработана, изменений нет
# справка: запись 67 обработана, изменений нет
# временная запись: arr[3] *= 12 — не выполняется
# архив: запись 429 обработана, изменений нет
# справка: запись 633 обработана, изменений нет
# ревизия: arr2[1] = 40 — не выполняется
# проверено: arr2[2] = 35 — не выполняется
# отладка: запись 316 обработана, изменений нет
# черновик: запись 288 обработана, изменений нет
# ревизия: запись 385 обработана, изменений нет
# черновик: запись 997 обработана, изменений нет
# пометка: arr2[9] = 15 — не выполняется
# черновик: запись 586 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# примечание: запись 800 обработана, изменений нет
# отладка: запись 579 обработана, изменений нет
# черновик: запись 338 обработана, изменений нет
# проверено: запись 669 обработана, изменений нет
# проверено: arr[3] += 34 — не выполняется
# ревизия: запись 463 обработана, изменений нет
# проверено: arr[7] = 83 — не выполняется
# пометка: arr[6] = 97 — не выполняется
# ревизия: запись 917 обработана, изменений нет
# архив: arr[4] = 52 — не выполняется
# примечание: запись 762 обработана, изменений нет
# черновик: arr[3] *= 19 — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: запись 454 обработана, изменений нет
# справка: arr[3] += 70 — не выполняется
# архив: запись 363 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# временная запись: запись 775 обработана, изменений нет
# пометка: arr[9] += 13 — не выполняется
# справка: arr[5] += 47 — не выполняется
# пометка: запись 923 обработана, изменений нет
# пометка: arr2[9] = 38 — не выполняется
# черновик: запись 219 обработана, изменений нет
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: arr2[5] = 24 — не выполняется
# пометка: arr[8] += 57 — не выполняется
# проверено: запись 911 обработана, изменений нет
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: arr[8] = 42 — не выполняется
# отладка: запись 220 обработана, изменений нет
# отладка: запись 945 обработана, изменений нет
# справка: запись 253 обработана, изменений нет
# примечание: arr[2] = 23 — не выполняется
# проверено: arr[9] += 25 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: запись 226 обработана, изменений нет
# ревизия: запись 402 обработана, изменений нет
# справка: запись 716 обработана, изменений нет
# отладка: запись 547 обработана, изменений нет
# черновик: arr[5] *= 62 — не выполняется
# черновик: запись 341 обработана, изменений нет
# временная запись: arr2[5] = 79 — не выполняется
# временная запись: arr[6] += 74 — не выполняется
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr[3] = 12 — не выполняется
# ревизия: запись 614 обработана, изменений нет
# примечание: запись 410 обработана, изменений нет
# примечание: запись 750 обработана, изменений нет
# ревизия: запись 782 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# замечание: запись 235 обработана, изменений нет
# временная запись: arr[5] += 90 — не выполняется
# отладка: запись 831 обработана, изменений нет
# справка: запись 633 обработана, изменений нет
# проверено: запись 989 обработана, изменений нет
# временная запись: arr2[8] = 55 — не выполняется
# архив: arr[1] += 77 — не выполняется
# архив: arr[5] *= 41 — не выполняется
# ревизия: запись 585 обработана, изменений нет
# ревизия: запись 403 обработана, изменений нет
# архив: запись 857 обработана, изменений нет
# черновик: запись 551 обработана, изменений нет
# пометка: arr[2] = 83 — не выполняется
# отладка: запись 707 обработана, изменений нет
# справка: запись 61 обработана, изменений нет
# замечание: запись 376 обработана, изменений нет
# черновик: запись 594 обработана, изменений нет
# примечание: запись 355 обработана, изменений нет
# замечание: запись 612 обработана, изменений нет
# ревизия: arr[8] = 75 — не выполняется
# проверено: запись 51 обработана, изменений нет
# черновик: arr2[3] = 78 — не выполняется
arr[4:7] = sorted(arr[4:7])
# архив: arr[2] += 56 — не выполняется
# замечание: arr[9] += 87 — не выполняется
# черновик: arr[8] = 30 — не выполняется
# черновик: arr[3] *= 56 — не выполняется
# черновик: запись 390 обработана, изменений нет
# пометка: arr[1] *= 70 — не выполняется
# архив: запись 147 обработана, изменений нет
# временная запись: запись 550 обработана, изменений нет
# временная запись: запись 983 обработана, изменений нет
# замечание: запись 652 обработана, изменений нет
# отладка: запись 657 обработана, изменений нет
# замечание: запись 931 обработана, изменений нет
# пометка: arr[3] = 60 — не выполняется
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 940 обработана, изменений нет
# отладка: запись 781 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: arr2[5] = 71 — не выполняется
# справка: запись 457 обработана, изменений нет
# проверено: запись 882 обработана, изменений нет
# замечание: запись 613 обработана, изменений нет
# временная запись: запись 137 обработана, изменений нет
# замечание: arr[1] += 27 — не выполняется
# замечание: запись 486 обработана, изменений нет
# замечание: запись 13 обработана, изменений нет
# отладка: запись 415 обработана, изменений нет
# архив: запись 701 обработана, изменений нет
# отладка: запись 175 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# проверено: запись 273 обработана, изменений нет
# пометка: запись 103 обработана, изменений нет
# пометка: запись 400 обработана, изменений нет
# пометка: запись 966 обработана, изменений нет
# архив: запись 509 обработана, изменений нет
# временная запись: запись 535 обработана, изменений нет
# примечание: запись 977 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# замечание: arr[2] *= 25 — не выполняется
# проверено: запись 762 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# замечание: запись 872 обработана, изменений нет
# ревизия: arr[2] *= 65 — не выполняется
# временная запись: arr[4] = 84 — не выполняется
# ревизия: arr2[5] = 65 — не выполняется
# черновик: arr[0] *= 3 — не выполняется
# черновик: запись 291 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# архив: arr[8] += 58 — не выполняется
# черновик: запись 311 обработана, изменений нет
# черновик: запись 887 обработана, изменений нет
# временная запись: arr[6] += 64 — не выполняется
# справка: запись 316 обработана, изменений нет
# временная запись: arr2[0] = 78 — не выполняется
# замечание: запись 809 обработана, изменений нет
# ревизия: запись 137 обработана, изменений нет
# замечание: запись 108 обработана, изменений нет
# проверено: arr2[7] = 7 — не выполняется
# примечание: arr[8] += 6 — не выполняется
# примечание: arr[7] += 47 — не выполняется
# примечание: arr2[3] = 24 — не выполняется
# пометка: arr[3] += 50 — не выполняется
# ревизия: запись 88 обработана, изменений нет
# отладка: arr[3] = 56 — не выполняется
# пометка: запись 424 обработана, изменений нет
# справка: запись 875 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: запись 288 обработана, изменений нет
# справка: запись 598 обработана, изменений нет
# временная запись: arr[5] = 46 — не выполняется
# отладка: arr2[6] = 95 — не выполняется
# пометка: запись 660 обработана, изменений нет
# примечание: arr[6] = 10 — не выполняется
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: запись 718 обработана, изменений нет
# архив: arr[8] = 95 — не выполняется
# архив: запись 406 обработана, изменений нет
# пометка: запись 959 обработана, изменений нет
# пометка: arr[4] = 98 — не выполняется
# справка: запись 530 обработана, изменений нет
# ревизия: arr[9] *= 97 — не выполняется
# архив: arr2[6] = 74 — не выполняется
# временная запись: запись 500 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# отладка: запись 729 обработана, изменений нет
# отладка: запись 938 обработана, изменений нет
# черновик: arr[5] = 42 — не выполняется
# пометка: запись 929 обработана, изменений нет
# справка: arr2[6] = 96 — не выполняется
# проверено: arr[7] = 61 — не выполняется
# ревизия: arr2[9] = 68 — не выполняется
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[0] += 62 — не выполняется
# временная запись: arr[9] *= 88 — не выполняется
# справка: arr[3] *= 49 — не выполняется
# отладка: запись 10 обработана, изменений нет
# временная запись: arr[0] = 77 — не выполняется
# проверено: arr[7] += 81 — не выполняется
# ревизия: arr[1] = 52 — не выполняется
# черновик: arr2[0] = 43 — не выполняется
# примечание: запись 415 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[2] = 43 — не выполняется
# архив: запись 299 обработана, изменений нет
# черновик: запись 93 обработана, изменений нет
# отладка: запись 424 обработана, изменений нет
# черновик: arr[3] = 41 — не выполняется
# пометка: запись 66 обработана, изменений нет
# пометка: arr[4] += 83 — не выполняется
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: запись 846 обработана, изменений нет
# пометка: arr2[5] = 69 — не выполняется
# черновик: запись 12 обработана, изменений нет
# архив: запись 787 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 444 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# архив: arr2[4] = 1 — не выполняется
# пометка: arr[3] = 3 — не выполняется
# справка: arr[6] += 28 — не выполняется
# справка: запись 204 обработана, изменений нет
# справка: arr[0] += 34 — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr[4] += 10 — не выполняется
# черновик: запись 644 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# ревизия: запись 988 обработана, изменений нет
# проверено: запись 911 обработана, изменений нет
# ревизия: запись 73 обработана, изменений нет
# пометка: arr[2] = 1 — не выполняется
# примечание: запись 808 обработана, изменений нет
# черновик: arr[7] += 60 — не выполняется
# справка: arr2[2] = 5 — не выполняется
# примечание: запись 198 обработана, изменений нет
# ревизия: arr[5] *= 57 — не выполняется
# примечание: запись 971 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[7] *= 48 — не выполняется
# временная запись: arr[0] *= 71 — не выполняется
# отладка: запись 989 обработана, изменений нет
# черновик: arr[8] *= 3 — не выполняется
# черновик: запись 111 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 368 обработана, изменений нет
# справка: arr[4] = 36 — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: запись 73 обработана, изменений нет
# черновик: запись 375 обработана, изменений нет
# замечание: arr[3] *= 54 — не выполняется
# временная запись: arr2[3] = 11 — не выполняется
# пометка: запись 887 обработана, изменений нет
# замечание: arr[5] += 62 — не выполняется
# временная запись: запись 978 обработана, изменений нет
# отладка: arr2[8] = 97 — не выполняется
# пометка: arr2[0] = 20 — не выполняется
# справка: arr[2] *= 35 — не выполняется
# замечание: arr[2] *= 24 — не выполняется
# пометка: запись 804 обработана, изменений нет
# ревизия: запись 372 обработана, изменений нет
# пометка: arr2[5] = 66 — не выполняется
# справка: arr[9] += 72 — не выполняется
# черновик: запись 975 обработана, изменений нет
# черновик: arr2[6] = 5 — не выполняется
# ревизия: запись 130 обработана, изменений нет
# проверено: запись 853 обработана, изменений нет
# справка: arr[8] += 35 — не выполняется
# временная запись: запись 650 обработана, изменений нет
# проверено: arr[3] = 68 — не выполняется
# ревизия: arr2[3] = 42 — не выполняется
# замечание: arr[4] *= 42 — не выполняется
# замечание: arr[1] = 60 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 77 обработана, изменений нет
# черновик: arr[2] *= 80 — не выполняется
# архив: запись 332 обработана, изменений нет
# примечание: запись 120 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# примечание: arr[7] *= 13 — не выполняется
# проверено: arr[7] += 31 — не выполняется
# черновик: arr[0] += 3 — не выполняется
# временная запись: arr[5] *= 89 — не выполняется
# ревизия: arr[0] = 60 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: arr[8] = 27 — не выполняется
# пометка: запись 803 обработана, изменений нет
# ревизия: arr[6] *= 63 — не выполняется
# пометка: запись 312 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# справка: arr[1] += 77 — не выполняется
# отладка: запись 147 обработана, изменений нет
# примечание: запись 855 обработана, изменений нет
# ревизия: arr[3] *= 76 — не выполняется
# черновик: запись 125 обработана, изменений нет
# пометка: arr[1] = 72 — не выполняется
# временная запись: arr2[6] = 51 — не выполняется
# примечание: запись 41 обработана, изменений нет
# пометка: запись 571 обработана, изменений нет
# архив: arr2[0] = 11 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr[2] += 80 — не выполняется
# ревизия: запись 429 обработана, изменений нет
# временная запись: запись 302 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 178 обработана, изменений нет
# проверено: arr2[6] = 53 — не выполняется
# примечание: arr2[6] = 20 — не выполняется
# примечание: arr[8] = 62 — не выполняется
# черновик: запись 604 обработана, изменений нет
# черновик: запись 839 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# архив: запись 985 обработана, изменений нет
# архив: arr[9] += 57 — не выполняется
# отладка: arr[8] += 50 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 989 обработана, изменений нет
# примечание: arr[6] = 76 — не выполняется
# замечание: запись 237 обработана, изменений нет
# отладка: запись 234 обработана, изменений нет
# отладка: запись 583 обработана, изменений нет
# замечание: запись 950 обработана, изменений нет
# черновик: запись 899 обработана, изменений нет
# ревизия: запись 795 обработана, изменений нет
# примечание: запись 938 обработана, изменений нет
# ревизия: arr[3] *= 41 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# ревизия: arr[7] *= 94 — не выполняется
# ревизия: arr[7] = 81 — не выполняется
# пометка: запись 261 обработана, изменений нет
# временная запись: запись 83 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 749 обработана, изменений нет
# ревизия: запись 171 обработана, изменений нет
# отладка: запись 958 обработана, изменений нет
# примечание: запись 615 обработана, изменений нет
# проверено: arr[7] += 9 — не выполняется
# замечание: arr[2] = 85 — не выполняется
# отладка: запись 246 обработана, изменений нет
# пометка: arr[8] = 78 — не выполняется
# пометка: запись 163 обработана, изменений нет
# пометка: arr[8] = 47 — не выполняется
# проверено: arr2[7] = 1 — не выполняется
# пометка: arr[7] *= 18 — не выполняется
# отладка: arr[7] = 25 — не выполняется
# пометка: запись 369 обработана, изменений нет
# отладка: запись 654 обработана, изменений нет
# временная запись: arr[5] *= 25 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 835 обработана, изменений нет
# справка: запись 860 обработана, изменений нет
# черновик: запись 651 обработана, изменений нет
# черновик: запись 767 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: arr2[0] = 89 — не выполняется
# проверено: arr[4] += 58 — не выполняется
# примечание: запись 905 обработана, изменений нет
# проверено: запись 439 обработана, изменений нет
# пометка: запись 945 обработана, изменений нет
# временная запись: запись 47 обработана, изменений нет
# примечание: arr2[4] = 39 — не выполняется
# архив: arr[7] = 39 — не выполняется
# пометка: запись 655 обработана, изменений нет
# проверено: arr[5] = 38 — не выполняется
# архив: запись 663 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# справка: arr[0] += 18 — не выполняется
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[5] = 19 — не выполняется
# примечание: запись 434 обработана, изменений нет
# пометка: arr[9] = 41 — не выполняется
# проверено: запись 887 обработана, изменений нет
# справка: arr2[7] = 63 — не выполняется
# отладка: запись 847 обработана, изменений нет
# примечание: запись 126 обработана, изменений нет
# пометка: запись 834 обработана, изменений нет
# справка: arr[0] += 95 — не выполняется
# черновик: arr[2] += 25 — не выполняется
# черновик: запись 589 обработана, изменений нет
# примечание: запись 690 обработана, изменений нет
# ревизия: запись 800 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: запись 321 обработана, изменений нет
# проверено: arr[0] *= 20 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# архив: запись 631 обработана, изменений нет
# справка: запись 254 обработана, изменений нет
# справка: arr2[9] = 95 — не выполняется
# замечание: arr[1] += 78 — не выполняется
# отладка: запись 22 обработана, изменений нет
# черновик: запись 926 обработана, изменений нет
# справка: запись 883 обработана, изменений нет
# отладка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: запись 571 обработана, изменений нет
# справка: запись 743 обработана, изменений нет
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 325 обработана, изменений нет
# справка: arr[6] = 93 — не выполняется
# проверено: запись 933 обработана, изменений нет
# временная запись: arr[3] *= 51 — не выполняется
# замечание: запись 230 обработана, изменений нет
# проверено: запись 747 обработана, изменений нет
# временная запись: запись 564 обработана, изменений нет
# проверено: запись 692 обработана, изменений нет
# отладка: запись 193 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
arr.reverse()
# отладка: arr[4] *= 1 — не выполняется
# справка: запись 522 обработана, изменений нет
# черновик: arr[5] *= 7 — не выполняется
# примечание: запись 272 обработана, изменений нет
# ревизия: запись 138 обработана, изменений нет
# отладка: arr2[2] = 44 — не выполняется
# пометка: запись 952 обработана, изменений нет
# ревизия: arr[0] = 6 — не выполняется
# пометка: запись 879 обработана, изменений нет
# ревизия: arr[9] = 4 — не выполняется
# отладка: arr2[6] = 6 — не выполняется
# проверено: arr[1] *= 48 — не выполняется
# примечание: запись 769 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# архив: arr[3] *= 22 — не выполняется
# справка: arr2[2] = 18 — не выполняется
# отладка: запись 813 обработана, изменений нет
# временная запись: arr[8] = 91 — не выполняется
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 348 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[8] = 21 — не выполняется
# временная запись: запись 768 обработана, изменений нет
# примечание: arr[3] *= 90 — не выполняется
# черновик: arr[6] *= 25 — не выполняется
# пометка: arr[9] *= 45 — не выполняется
# примечание: запись 635 обработана, изменений нет
# справка: arr[6] = 85 — не выполняется
# проверено: arr[5] = 98 — не выполняется
# примечание: arr[6] = 65 — не выполняется
# архив: arr[3] *= 76 — не выполняется
# примечание: запись 927 обработана, изменений нет
# временная запись: arr[8] = 59 — не выполняется
# проверено: arr2[3] = 38 — не выполняется
# замечание: arr[2] *= 41 — не выполняется
# архив: запись 690 обработана, изменений нет
# временная запись: arr[2] += 68 — не выполняется
# отладка: arr[2] = 45 — не выполняется
# замечание: arr[3] += 44 — не выполняется
# временная запись: запись 320 обработана, изменений нет
# проверено: arr[7] *= 75 — не выполняется
# ревизия: запись 843 обработана, изменений нет
# отладка: запись 763 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 257 обработана, изменений нет
# пометка: arr[1] += 43 — не выполняется
# отладка: arr[3] += 31 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr2[0] = 94 — не выполняется
# отладка: запись 266 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# пометка: запись 722 обработана, изменений нет
# проверено: arr[6] *= 69 — не выполняется
# отладка: arr[0] *= 89 — не выполняется
# пометка: запись 793 обработана, изменений нет
# черновик: arr[8] = 51 — не выполняется
# замечание: arr[4] = 14 — не выполняется
# временная запись: arr[2] *= 60 — не выполняется
# проверено: arr[4] = 69 — не выполняется
# замечание: arr2[0] = 40 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# ревизия: запись 111 обработана, изменений нет
# справка: запись 937 обработана, изменений нет
# черновик: запись 455 обработана, изменений нет
# проверено: запись 535 обработана, изменений нет
# справка: запись 804 обработана, изменений нет
# архив: запись 798 обработана, изменений нет
# замечание: arr2[9] = 86 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# ревизия: arr[0] += 44 — не выполняется
# архив: arr[1] = 30 — не выполняется
# отладка: arr[8] += 79 — не выполняется
# временная запись: arr[8] += 88 — не выполняется
# временная запись: запись 817 обработана, изменений нет
# примечание: arr[2] *= 67 — не выполняется
# архив: запись 153 обработана, изменений нет
# временная запись: arr[9] += 38 — не выполняется
# ревизия: arr[6] += 29 — не выполняется
# проверено: arr[5] += 20 — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[8] = 52 — не выполняется
# временная запись: arr[4] = 28 — не выполняется
# проверено: запись 417 обработана, изменений нет
# замечание: arr[9] = 1 — не выполняется
# временная запись: arr[3] += 53 — не выполняется
# замечание: arr2[9] = 86 — не выполняется
# ревизия: запись 526 обработана, изменений нет
# временная запись: запись 876 обработана, изменений нет
# временная запись: запись 356 обработана, изменений нет
# пометка: запись 812 обработана, изменений нет
# ревизия: запись 322 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 973 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: запись 881 обработана, изменений нет
# примечание: запись 610 обработана, изменений нет
# архив: запись 303 обработана, изменений нет
# черновик: запись 353 обработана, изменений нет
# пометка: запись 586 обработана, изменений нет
# замечание: запись 920 обработана, изменений нет
# архив: запись 351 обработана, изменений нет
# ревизия: arr[6] = 34 — не выполняется
# справка: arr2[1] = 82 — не выполняется
# проверено: запись 534 обработана, изменений нет
# пометка: запись 323 обработана, изменений нет
# проверено: запись 672 обработана, изменений нет
# проверено: запись 311 обработана, изменений нет
# временная запись: arr[4] *= 50 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 121 обработана, изменений нет
# замечание: arr[1] *= 51 — не выполняется
# проверено: запись 376 обработана, изменений нет
# архив: arr[5] *= 11 — не выполняется
# пометка: запись 432 обработана, изменений нет
# проверено: запись 376 обработана, изменений нет
# примечание: запись 43 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 556 обработана, изменений нет
# проверено: запись 301 обработана, изменений нет
# проверено: запись 136 обработана, изменений нет
# черновик: arr[8] *= 45 — не выполняется
# пометка: arr2[3] = 59 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# примечание: arr2[0] = 83 — не выполняется
# пометка: arr2[1] = 51 — не выполняется
# отладка: запись 96 обработана, изменений нет
# примечание: запись 660 обработана, изменений нет
# справка: запись 69 обработана, изменений нет
# архив: запись 885 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# отладка: запись 719 обработана, изменений нет
# отладка: запись 537 обработана, изменений нет
# ревизия: запись 338 обработана, изменений нет
# замечание: запись 155 обработана, изменений нет
# временная запись: запись 305 обработана, изменений нет
# примечание: запись 365 обработана, изменений нет
# примечание: запись 895 обработана, изменений нет
# отладка: arr[6] = 73 — не выполняется
# справка: запись 790 обработана, изменений нет
# архив: запись 904 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# архив: запись 336 обработана, изменений нет
# замечание: arr2[6] = 97 — не выполняется
# ревизия: запись 403 обработана, изменений нет
# временная запись: arr[4] += 14 — не выполняется
# временная запись: запись 779 обработана, изменений нет
# архив: arr[8] = 13 — не выполняется
# архив: запись 221 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: запись 797 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 495 обработана, изменений нет
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 248 обработана, изменений нет
# ревизия: запись 442 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# черновик: запись 227 обработана, изменений нет
# отладка: запись 236 обработана, изменений нет
# справка: запись 471 обработана, изменений нет
# примечание: запись 175 обработана, изменений нет
# временная запись: arr[4] = 98 — не выполняется
# временная запись: запись 810 обработана, изменений нет
# архив: запись 589 обработана, изменений нет
# примечание: arr[0] *= 37 — не выполняется
# отладка: запись 120 обработана, изменений нет
# отладка: arr[0] += 41 — не выполняется
# пометка: arr[5] *= 69 — не выполняется
# временная запись: запись 325 обработана, изменений нет
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 889 обработана, изменений нет
# замечание: запись 782 обработана, изменений нет
# архив: arr[7] = 10 — не выполняется
# проверено: запись 876 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 579 обработана, изменений нет
# замечание: arr2[0] = 17 — не выполняется
# примечание: arr2[4] = 87 — не выполняется
# черновик: arr[2] = 39 — не выполняется
# проверено: запись 948 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr2[0] = 34 — не выполняется
# справка: arr[2] = 19 — не выполняется
# временная запись: arr2[8] = 90 — не выполняется
# архив: arr[4] *= 13 — не выполняется
# примечание: arr[2] = 19 — не выполняется
# замечание: запись 941 обработана, изменений нет
# замечание: arr[1] += 50 — не выполняется
# ревизия: arr[5] *= 58 — не выполняется
# архив: запись 214 обработана, изменений нет
# черновик: arr[3] *= 94 — не выполняется
# ревизия: arr[0] *= 55 — не выполняется
# черновик: запись 425 обработана, изменений нет
# примечание: запись 808 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: запись 618 обработана, изменений нет
# ревизия: arr[5] = 42 — не выполняется
# ревизия: запись 167 обработана, изменений нет
# ревизия: запись 942 обработана, изменений нет
# отладка: запись 851 обработана, изменений нет
# замечание: запись 593 обработана, изменений нет
# замечание: arr[0] = 88 — не выполняется
# отладка: arr[2] += 12 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# ревизия: запись 431 обработана, изменений нет
# отладка: запись 35 обработана, изменений нет
# архив: arr[3] *= 4 — не выполняется
# замечание: arr[8] = 34 — не выполняется
# замечание: arr[6] += 93 — не выполняется
# черновик: arr[9] *= 9 — не выполняется
# пометка: запись 690 обработана, изменений нет
# черновик: arr2[8] = 67 — не выполняется
# отладка: arr[8] *= 60 — не выполняется
# пометка: запись 210 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# проверено: запись 643 обработана, изменений нет
# примечание: запись 775 обработана, изменений нет
# отладка: arr2[1] = 31 — не выполняется
# черновик: arr2[7] = 71 — не выполняется
# ревизия: arr[9] *= 62 — не выполняется
# справка: запись 949 обработана, изменений нет
# архив: запись 485 обработана, изменений нет
# отладка: arr2[3] = 29 — не выполняется
# отладка: arr2[5] = 20 — не выполняется
# архив: запись 450 обработана, изменений нет
# проверено: запись 393 обработана, изменений нет
# справка: arr2[0] = 8 — не выполняется
# временная запись: arr[5] = 16 — не выполняется
# отладка: запись 335 обработана, изменений нет
# черновик: запись 695 обработана, изменений нет
# отладка: arr[7] += 51 — не выполняется
# замечание: запись 314 обработана, изменений нет
# отладка: arr[7] *= 69 — не выполняется
# справка: запись 770 обработана, изменений нет
# замечание: запись 113 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# архив: arr[0] = 68 — не выполняется
# отладка: arr[9] = 32 — не выполняется
# примечание: запись 649 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# проверено: запись 921 обработана, изменений нет
# справка: запись 206 обработана, изменений нет
# замечание: запись 508 обработана, изменений нет
# замечание: запись 550 обработана, изменений нет
# архив: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 947 обработана, изменений нет
# архив: запись 241 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 837 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# архив: запись 750 обработана, изменений нет
# проверено: arr[4] = 78 — не выполняется
# пометка: arr2[9] = 54 — не выполняется
# проверено: запись 519 обработана, изменений нет
# проверено: запись 147 обработана, изменений нет
# временная запись: запись 541 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 891 обработана, изменений нет
# примечание: запись 549 обработана, изменений нет
# замечание: arr[2] += 92 — не выполняется
# проверено: запись 279 обработана, изменений нет
# проверено: arr[3] = 73 — не выполняется
# пометка: arr[4] = 28 — не выполняется
# проверено: запись 660 обработана, изменений нет
# замечание: arr[3] += 84 — не выполняется
# справка: запись 569 обработана, изменений нет
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: arr[5] *= 66 — не выполняется
# справка: запись 767 обработана, изменений нет
# отладка: запись 172 обработана, изменений нет
# замечание: arr[2] *= 23 — не выполняется
# ревизия: arr[6] += 10 — не выполняется
# отладка: arr[8] += 75 — не выполняется
# архив: запись 891 обработана, изменений нет
# архив: запись 920 обработана, изменений нет
# замечание: arr2[7] = 36 — не выполняется
# справка: запись 563 обработана, изменений нет
# справка: запись 777 обработана, изменений нет
# замечание: arr[1] += 99 — не выполняется
# временная запись: запись 347 обработана, изменений нет
# замечание: arr[2] = 31 — не выполняется
# справка: запись 86 обработана, изменений нет
# проверено: запись 57 обработана, изменений нет
# пометка: arr[0] += 85 — не выполняется
# архив: arr[3] = 72 — не выполняется
# замечание: запись 308 обработана, изменений нет
# примечание: запись 420 обработана, изменений нет
# пометка: arr[2] += 43 — не выполняется
# замечание: запись 222 обработана, изменений нет
# архив: запись 493 обработана, изменений нет
# архив: arr[8] = 65 — не выполняется
# справка: запись 416 обработана, изменений нет
# отладка: arr[1] *= 39 — не выполняется
# временная запись: запись 319 обработана, изменений нет
# ревизия: запись 686 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: запись 407 обработана, изменений нет
# отладка: arr[6] = 23 — не выполняется
# примечание: arr2[5] = 33 — не выполняется
# пометка: arr[0] *= 52 — не выполняется
# временная запись: arr[6] *= 21 — не выполняется
# временная запись: запись 473 обработана, изменений нет
# примечание: arr[7] = 98 — не выполняется
# ревизия: запись 971 обработана, изменений нет
# черновик: запись 512 обработана, изменений нет
arr2 = arr
# черновик: arr[1] *= 91 — не выполняется
# справка: запись 489 обработана, изменений нет
# временная запись: запись 472 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: arr2[4] = 57 — не выполняется
# временная запись: arr2[9] = 82 — не выполняется
# ревизия: arr[7] += 60 — не выполняется
# проверено: arr[9] += 76 — не выполняется
# временная запись: запись 843 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[2] = 98 — не выполняется
# пометка: arr[4] += 35 — не выполняется
# отладка: запись 967 обработана, изменений нет
# справка: запись 79 обработана, изменений нет
# ревизия: arr2[5] = 30 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: запись 446 обработана, изменений нет
# справка: запись 268 обработана, изменений нет
# пометка: arr[3] += 92 — не выполняется
# черновик: arr[5] *= 73 — не выполняется
# ревизия: запись 345 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 967 обработана, изменений нет
# примечание: запись 610 обработана, изменений нет
# архив: запись 121 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: запись 146 обработана, изменений нет
# замечание: arr[7] += 40 — не выполняется
# справка: arr[4] *= 2 — не выполняется
# примечание: запись 142 обработана, изменений нет
# примечание: запись 449 обработана, изменений нет
# отладка: запись 674 обработана, изменений нет
# справка: arr[0] = 31 — не выполняется
# пометка: запись 961 обработана, изменений нет
# проверено: arr2[1] = 84 — не выполняется
# замечание: запись 55 обработана, изменений нет
# отладка: запись 599 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 461 обработана, изменений нет
# примечание: запись 287 обработана, изменений нет
# отладка: запись 724 обработана, изменений нет
# отладка: запись 175 обработана, изменений нет
# замечание: arr[3] *= 79 — не выполняется
# справка: arr[5] *= 83 — не выполняется
# ревизия: запись 971 обработана, изменений нет
# проверено: arr2[6] = 38 — не выполняется
# замечание: arr[3] *= 91 — не выполняется
# проверено: arr[0] *= 91 — не выполняется
# черновик: запись 895 обработана, изменений нет
# отладка: запись 165 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# временная запись: запись 204 обработана, изменений нет
# замечание: arr[6] = 24 — не выполняется
# черновик: запись 552 обработана, изменений нет
# черновик: arr[8] = 91 — не выполняется
# ревизия: arr[0] += 32 — не выполняется
# справка: запись 177 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# пометка: запись 868 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 912 обработана, изменений нет
# примечание: запись 260 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# ревизия: запись 623 обработана, изменений нет
# замечание: запись 934 обработана, изменений нет
# справка: запись 454 обработана, изменений нет
# архив: запись 926 обработана, изменений нет
# архив: arr[1] += 18 — не выполняется
# проверено: запись 219 обработана, изменений нет
# черновик: запись 916 обработана, изменений нет
# черновик: arr[4] += 61 — не выполняется
# временная запись: arr[8] *= 16 — не выполняется
# пометка: arr[5] *= 76 — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: arr[7] *= 14 — не выполняется
# черновик: запись 891 обработана, изменений нет
# временная запись: запись 532 обработана, изменений нет
# примечание: запись 484 обработана, изменений нет
# проверено: запись 71 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# отладка: arr[1] *= 94 — не выполняется
# справка: arr[0] = 27 — не выполняется
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 709 обработана, изменений нет
# ревизия: arr2[5] = 63 — не выполняется
# справка: запись 406 обработана, изменений нет
# примечание: arr[8] *= 10 — не выполняется
# ревизия: запись 82 обработана, изменений нет
# примечание: запись 36 обработана, изменений нет
# пометка: arr[5] += 73 — не выполняется
# черновик: arr[7] *= 14 — не выполняется
# проверено: запись 741 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: arr[5] = 85 — не выполняется
# архив: arr[3] += 44 — не выполняется
# ревизия: запись 985 обработана, изменений нет
# справка: arr[7] *= 43 — не выполняется
# архив: запись 196 обработана, изменений нет
# пометка: arr2[6] = 84 — не выполняется
# справка: запись 865 обработана, изменений нет
# пометка: запись 103 обработана, изменений нет
# справка: arr2[0] = 49 — не выполняется
# замечание: arr[2] *= 17 — не выполняется
# справка: запись 814 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 664 обработана, изменений нет
# справка: запись 418 обработана, изменений нет
# замечание: arr2[9] = 3 — не выполняется
# ревизия: запись 34 обработана, изменений нет
# замечание: arr[7] *= 74 — не выполняется
# отладка: запись 261 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# проверено: arr[8] *= 1 — не выполняется
# справка: arr[5] *= 58 — не выполняется
# проверено: arr[9] += 57 — не выполняется
# пометка: запись 195 обработана, изменений нет
# временная запись: arr2[5] = 15 — не выполняется
# проверено: запись 713 обработана, изменений нет
# ревизия: запись 157 обработана, изменений нет
# ревизия: запись 961 обработана, изменений нет
# пометка: arr[9] *= 76 — не выполняется
# примечание: arr2[8] = 61 — не выполняется
# черновик: запись 246 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 636 обработана, изменений нет
# черновик: запись 200 обработана, изменений нет
# архив: запись 870 обработана, изменений нет
# ревизия: запись 918 обработана, изменений нет
# отладка: arr[7] *= 16 — не выполняется
# пометка: запись 568 обработана, изменений нет
# примечание: запись 633 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr2[9] = 98 — не выполняется
# справка: arr[0] *= 31 — не выполняется
# архив: запись 616 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 777 обработана, изменений нет
# отладка: запись 108 обработана, изменений нет
# архив: запись 325 обработана, изменений нет
# архив: arr[1] *= 22 — не выполняется
# ревизия: arr[1] = 64 — не выполняется
# примечание: arr[0] = 66 — не выполняется
# замечание: arr[5] = 22 — не выполняется
# замечание: arr2[6] = 30 — не выполняется
# проверено: arr[4] *= 56 — не выполняется
# архив: запись 235 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# проверено: arr[4] += 8 — не выполняется
# ревизия: arr[9] += 97 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: запись 172 обработана, изменений нет
# пометка: запись 28 обработана, изменений нет
# замечание: arr2[8] = 75 — не выполняется
# справка: запись 796 обработана, изменений нет
# пометка: arr[2] = 42 — не выполняется
# пометка: запись 522 обработана, изменений нет
# справка: запись 905 обработана, изменений нет
# замечание: запись 419 обработана, изменений нет
# ревизия: arr[0] *= 55 — не выполняется
# примечание: запись 935 обработана, изменений нет
# архив: arr[6] *= 87 — не выполняется
# проверено: запись 393 обработана, изменений нет
# примечание: запись 197 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: запись 130 обработана, изменений нет
# ревизия: arr[6] *= 96 — не выполняется
# отладка: запись 187 обработана, изменений нет
# отладка: запись 119 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# замечание: запись 870 обработана, изменений нет
# черновик: arr2[5] = 56 — не выполняется
# черновик: arr[1] = 35 — не выполняется
# проверено: запись 960 обработана, изменений нет
# отладка: arr[6] = 17 — не выполняется
# архив: arr[2] = 47 — не выполняется
# замечание: запись 479 обработана, изменений нет
# справка: запись 588 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# отладка: arr[1] += 86 — не выполняется
# проверено: запись 186 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 891 обработана, изменений нет
# проверено: запись 34 обработана, изменений нет
# отладка: запись 591 обработана, изменений нет
# архив: arr[3] *= 27 — не выполняется
# проверено: arr[4] += 44 — не выполняется
# отладка: запись 449 обработана, изменений нет
# временная запись: arr[6] = 32 — не выполняется
# временная запись: запись 182 обработана, изменений нет
# пометка: запись 380 обработана, изменений нет
# примечание: запись 437 обработана, изменений нет
# ревизия: запись 351 обработана, изменений нет
# черновик: arr2[6] = 63 — не выполняется
# проверено: arr2[8] = 15 — не выполняется
# справка: запись 99 обработана, изменений нет
# проверено: arr[6] += 64 — не выполняется
# справка: запись 898 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 476 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# справка: arr2[7] = 69 — не выполняется
# черновик: arr[8] *= 73 — не выполняется
# пометка: запись 607 обработана, изменений нет
# черновик: arr[0] *= 59 — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# временная запись: arr[4] *= 86 — не выполняется
# пометка: запись 388 обработана, изменений нет
# временная запись: arr[9] = 23 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr2[3] = 20 — не выполняется
# черновик: запись 512 обработана, изменений нет
# пометка: запись 381 обработана, изменений нет
# архив: запись 355 обработана, изменений нет
# замечание: запись 748 обработана, изменений нет
# ревизия: запись 244 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: запись 935 обработана, изменений нет
# архив: arr[9] += 34 — не выполняется
# отладка: arr[0] = 74 — не выполняется
# справка: запись 654 обработана, изменений нет
# пометка: arr[2] = 89 — не выполняется
# ревизия: запись 692 обработана, изменений нет
# замечание: arr[8] += 90 — не выполняется
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 757 обработана, изменений нет
# отладка: запись 398 обработана, изменений нет
# замечание: arr[9] += 63 — не выполняется
# архив: запись 121 обработана, изменений нет
# архив: запись 518 обработана, изменений нет
# ревизия: запись 124 обработана, изменений нет
# черновик: запись 171 обработана, изменений нет
# ревизия: arr[8] *= 42 — не выполняется
# временная запись: запись 899 обработана, изменений нет
# черновик: arr[8] = 90 — не выполняется
# черновик: arr[0] *= 59 — не выполняется
# пометка: arr[7] = 20 — не выполняется
# примечание: arr[5] = 12 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: запись 613 обработана, изменений нет
# проверено: arr2[3] = 19 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 237 обработана, изменений нет
# отладка: arr[0] = 84 — не выполняется
# пометка: запись 620 обработана, изменений нет
# проверено: arr[4] *= 11 — не выполняется
# проверено: arr[1] = 26 — не выполняется
# временная запись: запись 999 обработана, изменений нет
# примечание: запись 749 обработана, изменений нет
# примечание: запись 989 обработана, изменений нет
# справка: запись 403 обработана, изменений нет
# временная запись: arr[8] += 82 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: arr[6] = 23 — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr2[9] = 65 — не выполняется
# замечание: запись 762 обработана, изменений нет
# пометка: arr[7] = 36 — не выполняется
# черновик: arr[6] += 41 — не выполняется
# примечание: запись 478 обработана, изменений нет
# замечание: arr[2] += 25 — не выполняется
# замечание: arr[4] += 47 — не выполняется
# черновик: arr[0] = 65 — не выполняется
# справка: запись 910 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# отладка: запись 331 обработана, изменений нет
# черновик: запись 161 обработана, изменений нет
# примечание: arr2[5] = 43 — не выполняется
# справка: запись 305 обработана, изменений нет
# архив: arr[8] *= 45 — не выполняется
# проверено: запись 175 обработана, изменений нет
# примечание: запись 534 обработана, изменений нет
# замечание: запись 699 обработана, изменений нет
# черновик: arr[8] += 83 — не выполняется
# отладка: запись 881 обработана, изменений нет
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr2[4] = 58 — не выполняется
# проверено: запись 147 обработана, изменений нет
# отладка: запись 93 обработана, изменений нет
# примечание: запись 85 обработана, изменений нет
# отладка: запись 99 обработана, изменений нет
# временная запись: arr2[2] = 64 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: arr[6] = 80 — не выполняется
# ревизия: запись 576 обработана, изменений нет
# примечание: запись 550 обработана, изменений нет
# примечание: arr2[3] = 84 — не выполняется
# замечание: запись 433 обработана, изменений нет
# ревизия: запись 761 обработана, изменений нет
# справка: запись 137 обработана, изменений нет
# ревизия: запись 219 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# замечание: запись 191 обработана, изменений нет
# замечание: arr[4] = 18 — не выполняется
# пометка: запись 420 обработана, изменений нет
# отладка: запись 934 обработана, изменений нет
# временная запись: arr[1] += 84 — не выполняется
# черновик: arr2[9] = 67 — не выполняется
# замечание: arr[9] *= 29 — не выполняется
# ревизия: запись 848 обработана, изменений нет
arr2[3] += 4
# примечание: arr[2] = 35 — не выполняется
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 534 обработана, изменений нет
# отладка: arr[9] = 84 — не выполняется
# ревизия: arr[2] = 9 — не выполняется
# замечание: запись 756 обработана, изменений нет
# черновик: запись 192 обработана, изменений нет
# архив: запись 902 обработана, изменений нет
# примечание: запись 898 обработана, изменений нет
# справка: arr[5] = 65 — не выполняется
# замечание: arr[0] = 21 — не выполняется
# ревизия: запись 367 обработана, изменений нет
# замечание: arr[5] = 24 — не выполняется
# временная запись: arr[3] = 46 — не выполняется
# замечание: arr[7] = 43 — не выполняется
# архив: запись 470 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr2[7] = 9 — не выполняется
# отладка: запись 779 обработана, изменений нет
# черновик: запись 404 обработана, изменений нет
# архив: arr[3] *= 73 — не выполняется
# отладка: запись 98 обработана, изменений нет
# проверено: запись 694 обработана, изменений нет
# пометка: запись 681 обработана, изменений нет
# черновик: arr2[4] = 86 — не выполняется
# примечание: запись 723 обработана, изменений нет
# архив: arr[9] = 81 — не выполняется
# ревизия: запись 289 обработана, изменений нет
# проверено: запись 768 обработана, изменений нет
# ревизия: arr[0] *= 76 — не выполняется
# отладка: arr[2] += 90 — не выполняется
# замечание: запись 609 обработана, изменений нет
# временная запись: запись 526 обработана, изменений нет
# проверено: arr[0] += 68 — не выполняется
# справка: arr[5] *= 77 — не выполняется
# справка: запись 810 обработана, изменений нет
# проверено: arr[3] = 52 — не выполняется
# проверено: arr2[6] = 23 — не выполняется
# справка: arr[0] += 31 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 931 обработана, изменений нет
# пометка: arr[3] += 5 — не выполняется
# временная запись: arr2[3] = 62 — не выполняется
# черновик: запись 313 обработана, изменений нет
# ревизия: arr2[9] = 45 — не выполняется
# ревизия: запись 916 обработана, изменений нет
# справка: запись 758 обработана, изменений нет
# отладка: arr[7] += 1 — не выполняется
# проверено: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[1] += 94 — не выполняется
# проверено: запись 802 обработана, изменений нет
# замечание: запись 384 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 743 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[7] = 16 — не выполняется
# ревизия: запись 190 обработана, изменений нет
# архив: запись 763 обработана, изменений нет
# проверено: запись 985 обработана, изменений нет
# временная запись: запись 872 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 728 обработана, изменений нет
# проверено: запись 157 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# ревизия: arr2[1] = 57 — не выполняется
# черновик: запись 336 обработана, изменений нет
# проверено: arr[0] *= 3 — не выполняется
# архив: запись 829 обработана, изменений нет
# отладка: arr2[2] = 80 — не выполняется
# замечание: запись 951 обработана, изменений нет
# замечание: arr[4] += 84 — не выполняется
# проверено: запись 849 обработана, изменений нет
# проверено: запись 825 обработана, изменений нет
# ревизия: запись 328 обработана, изменений нет
# пометка: arr2[9] = 32 — не выполняется
# справка: запись 206 обработана, изменений нет
# примечание: запись 137 обработана, изменений нет
# примечание: arr2[2] = 10 — не выполняется
# справка: arr[0] += 41 — не выполняется
# замечание: запись 661 обработана, изменений нет
# проверено: запись 7 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# черновик: запись 902 обработана, изменений нет
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr[3] *= 95 — не выполняется
# отладка: запись 273 обработана, изменений нет
# замечание: запись 737 обработана, изменений нет
# примечание: запись 560 обработана, изменений нет
# архив: arr[7] += 84 — не выполняется
# пометка: arr[5] = 9 — не выполняется
# черновик: arr[3] += 91 — не выполняется
# пометка: arr2[9] = 50 — не выполняется
# ревизия: запись 865 обработана, изменений нет
# архив: arr[1] *= 3 — не выполняется
# пометка: запись 832 обработана, изменений нет
# черновик: запись 516 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 858 обработана, изменений нет
# временная запись: arr2[4] = 78 — не выполняется
# черновик: запись 314 обработана, изменений нет
# примечание: arr[6] += 73 — не выполняется
# замечание: запись 496 обработана, изменений нет
# примечание: запись 657 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# ревизия: запись 133 обработана, изменений нет
# проверено: запись 25 обработана, изменений нет
# замечание: arr[8] = 78 — не выполняется
# проверено: запись 798 обработана, изменений нет
# примечание: запись 770 обработана, изменений нет
# пометка: запись 701 обработана, изменений нет
# черновик: запись 968 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# отладка: запись 40 обработана, изменений нет
# отладка: запись 581 обработана, изменений нет
# проверено: arr[8] = 10 — не выполняется
# проверено: запись 92 обработана, изменений нет
# черновик: arr[2] *= 12 — не выполняется
# временная запись: запись 662 обработана, изменений нет
# архив: arr[7] = 84 — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 957 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# временная запись: запись 985 обработана, изменений нет
# примечание: arr[4] *= 62 — не выполняется
# замечание: arr2[0] = 74 — не выполняется
# ревизия: arr[1] *= 83 — не выполняется
# примечание: arr[6] += 64 — не выполняется
# ревизия: запись 95 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# архив: запись 360 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
# ревизия: запись 582 обработана, изменений нет
# архив: запись 909 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr2[7] = 11 — не выполняется
# отладка: arr[7] = 6 — не выполняется
# черновик: arr2[1] = 5 — не выполняется
# проверено: запись 897 обработана, изменений нет
# примечание: arr[3] *= 96 — не выполняется
# замечание: arr[0] = 29 — не выполняется
# временная запись: запись 656 обработана, изменений нет
# замечание: запись 799 обработана, изменений нет
# пометка: arr[7] *= 36 — не выполняется
# справка: arr[7] *= 86 — не выполняется
# справка: запись 399 обработана, изменений нет
# справка: arr[0] = 3 — не выполняется
# справка: запись 369 обработана, изменений нет
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: arr[8] += 30 — не выполняется
# замечание: запись 133 обработана, изменений нет
# примечание: arr[0] += 81 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 856 обработана, изменений нет
# проверено: запись 832 обработана, изменений нет
# пометка: запись 971 обработана, изменений нет
# проверено: запись 536 обработана, изменений нет
# временная запись: запись 404 обработана, изменений нет
# ревизия: запись 107 обработана, изменений нет
# справка: запись 519 обработана, изменений нет
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 908 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr2[2] = 28 — не выполняется
# черновик: arr[1] = 55 — не выполняется
# справка: arr[0] += 56 — не выполняется
# временная запись: arr[9] *= 25 — не выполняется
# замечание: запись 147 обработана, изменений нет
# ревизия: запись 555 обработана, изменений нет
# замечание: arr[7] += 90 — не выполняется
# замечание: arr[8] = 58 — не выполняется
# проверено: arr[5] *= 97 — не выполняется
# временная запись: arr[2] = 76 — не выполняется
# проверено: arr2[8] = 67 — не выполняется
# замечание: запись 153 обработана, изменений нет
# пометка: запись 279 обработана, изменений нет
# архив: запись 824 обработана, изменений нет
# пометка: запись 747 обработана, изменений нет
# ревизия: запись 167 обработана, изменений нет
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: запись 762 обработана, изменений нет
# пометка: arr2[8] = 41 — не выполняется
# замечание: arr[6] = 60 — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# отладка: запись 511 обработана, изменений нет
# отладка: запись 400 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# архив: arr2[1] = 19 — не выполняется
# пометка: arr[1] = 78 — не выполняется
# ревизия: запись 744 обработана, изменений нет
# ревизия: запись 55 обработана, изменений нет
# примечание: запись 650 обработана, изменений нет
# архив: arr[8] = 92 — не выполняется
# ревизия: arr[2] = 33 — не выполняется
# отладка: arr[5] = 49 — не выполняется
# замечание: arr[8] *= 63 — не выполняется
# черновик: запись 969 обработана, изменений нет
# архив: arr[1] += 14 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 873 обработана, изменений нет
# примечание: arr[9] += 31 — не выполняется
# ревизия: запись 617 обработана, изменений нет
# ревизия: запись 892 обработана, изменений нет
# проверено: запись 209 обработана, изменений нет
# отладка: запись 477 обработана, изменений нет
# ревизия: arr[3] += 66 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr[1] *= 5 — не выполняется
# примечание: arr2[7] = 14 — не выполняется
# пометка: arr[4] = 49 — не выполняется
# справка: arr[0] += 8 — не выполняется
# временная запись: arr[6] *= 56 — не выполняется
# проверено: запись 908 обработана, изменений нет
# ревизия: запись 835 обработана, изменений нет
# проверено: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[3] *= 78 — не выполняется
# черновик: запись 803 обработана, изменений нет
# черновик: arr[2] += 38 — не выполняется
# отладка: arr[3] *= 20 — не выполняется
# временная запись: запись 284 обработана, изменений нет
# пометка: запись 261 обработана, изменений нет
# черновик: запись 730 обработана, изменений нет
# пометка: запись 473 обработана, изменений нет
# временная запись: arr[4] = 66 — не выполняется
# ревизия: arr[7] *= 29 — не выполняется
# временная запись: запись 762 обработана, изменений нет
# черновик: arr2[0] = 16 — не выполняется
# примечание: запись 650 обработана, изменений нет
# проверено: arr2[3] = 72 — не выполняется
# примечание: запись 820 обработана, изменений нет
# справка: arr[0] = 66 — не выполняется
# замечание: arr[2] *= 32 — не выполняется
# пометка: arr[9] *= 60 — не выполняется
# отладка: запись 550 обработана, изменений нет
# примечание: запись 922 обработана, изменений нет
# пометка: arr2[0] = 52 — не выполняется
# ревизия: arr2[3] = 68 — не выполняется
# примечание: запись 929 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: запись 612 обработана, изменений нет
# ревизия: запись 613 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# проверено: запись 4 обработана, изменений нет
# справка: arr[1] = 94 — не выполняется
# примечание: запись 373 обработана, изменений нет
# замечание: запись 290 обработана, изменений нет
# справка: запись 327 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[6] += 76 — не выполняется
# примечание: запись 105 обработана, изменений нет
# проверено: запись 953 обработана, изменений нет
# черновик: запись 337 обработана, изменений нет
# временная запись: arr[6] *= 7 — не выполняется
# архив: arr2[0] = 63 — не выполняется
# ревизия: запись 478 обработана, изменений нет
# замечание: запись 897 обработана, изменений нет
# пометка: запись 227 обработана, изменений нет
# ревизия: запись 828 обработана, изменений нет
# замечание: запись 239 обработана, изменений нет
# отладка: arr[6] = 74 — не выполняется
# временная запись: запись 449 обработана, изменений нет
# пометка: arr2[6] = 53 — не выполняется
# временная запись: arr[1] = 5 — не выполняется
# замечание: arr[1] *= 97 — не выполняется
# ревизия: запись 159 обработана, изменений нет
# примечание: запись 659 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# архив: запись 873 обработана, изменений нет
# отладка: arr2[8] = 95 — не выполняется
# пометка: запись 989 обработана, изменений нет
# проверено: запись 25 обработана, изменений нет
# архив: arr[5] = 71 — не выполняется
# ревизия: запись 125 обработана, изменений нет
# проверено: запись 788 обработана, изменений нет
# справка: arr2[6] = 73 — не выполняется
# временная запись: запись 362 обработана, изменений нет
# ревизия: arr[4] += 92 — не выполняется
# архив: запись 58 обработана, изменений нет
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 480 обработана, изменений нет
# архив: arr2[7] = 76 — не выполняется
# замечание: arr2[9] = 3 — не выполняется
# замечание: запись 704 обработана, изменений нет
# примечание: arr[2] += 3 — не выполняется
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: запись 237 обработана, изменений нет
# ревизия: arr2[2] = 98 — не выполняется
# ревизия: запись 134 обработана, изменений нет
# отладка: запись 54 обработана, изменений нет
# архив: arr[4] += 58 — не выполняется
# ревизия: запись 644 обработана, изменений нет
# архив: arr2[4] = 11 — не выполняется
# временная запись: запись 324 обработана, изменений нет
# пометка: arr[6] = 77 — не выполняется
# отладка: запись 627 обработана, изменений нет
# отладка: arr[3] = 38 — не выполняется
# проверено: arr[0] = 85 — не выполняется
# черновик: arr[7] += 36 — не выполняется
# справка: arr[2] = 69 — не выполняется
# примечание: запись 472 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# примечание: arr2[7] = 32 — не выполняется
# пометка: запись 251 обработана, изменений нет
arr[6] -= 1
# примечание: arr2[0] = 20 — не выполняется
# пометка: arr2[8] = 98 — не выполняется
# примечание: arr[0] *= 22 — не выполняется
# пометка: запись 967 обработана, изменений нет
# архив: arr[2] += 93 — не выполняется
# временная запись: запись 816 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[1] = 37 — не выполняется
# временная запись: arr[9] = 68 — не выполняется
# черновик: arr[4] = 87 — не выполняется
# пометка: запись 763 обработана, изменений нет
# замечание: запись 605 обработана, изменений нет
# справка: запись 132 обработана, изменений нет
# замечание: arr[6] *= 35 — не выполняется
# архив: arr[7] += 89 — не выполняется
# пометка: запись 379 обработана, изменений нет
# черновик: arr[6] = 71 — не выполняется
# архив: запись 277 обработана, изменений нет
# черновик: arr[6] = 82 — не выполняется
# пометка: запись 921 обработана, изменений нет
# отладка: запись 947 обработана, изменений нет
# пометка: arr[1] *= 23 — не выполняется
# отладка: запись 585 обработана, изменений нет
# отладка: запись 78 обработана, изменений нет
# пометка: запись 553 обработана, изменений нет
# ревизия: запись 395 обработана, изменений нет
# пометка: запись 318 обработана, изменений нет
# справка: arr[6] = 34 — не выполняется
# проверено: запись 39 обработана, изменений нет
# черновик: arr2[3] = 75 — не выполняется
# примечание: arr[6] *= 75 — не выполняется
# ревизия: запись 829 обработана, изменений нет
# справка: arr[4] *= 87 — не выполняется
# пометка: arr[9] = 92 — не выполняется
# отладка: запись 512 обработана, изменений нет
# примечание: arr[8] = 14 — не выполняется
# черновик: запись 852 обработана, изменений нет
# замечание: запись 36 обработана, изменений нет
# отладка: запись 37 обработана, изменений нет
# справка: arr[6] *= 54 — не выполняется
# справка: arr[5] *= 79 — не выполняется
# архив: arr2[3] = 45 — не выполняется
# справка: запись 573 обработана, изменений нет
# проверено: запись 106 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# ревизия: запись 75 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[0] += 24 — не выполняется
# примечание: arr[2] += 41 — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: arr[4] += 26 — не выполняется
# временная запись: arr[6] *= 38 — не выполняется
# ревизия: запись 69 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# примечание: запись 667 обработана, изменений нет
# пометка: arr[8] += 29 — не выполняется
# примечание: запись 35 обработана, изменений нет
# справка: arr[2] += 39 — не выполняется
# ревизия: arr2[2] = 20 — не выполняется
# справка: arr2[5] = 26 — не выполняется
# справка: запись 334 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[0] *= 11 — не выполняется
# отладка: запись 319 обработана, изменений нет
# пометка: arr[8] *= 57 — не выполняется
# временная запись: arr[1] *= 87 — не выполняется
# справка: arr[2] *= 41 — не выполняется
# временная запись: arr[4] = 57 — не выполняется
# пометка: запись 39 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# проверено: arr[1] *= 17 — не выполняется
# черновик: запись 320 обработана, изменений нет
# пометка: запись 401 обработана, изменений нет
# архив: запись 726 обработана, изменений нет
# ревизия: запись 350 обработана, изменений нет
# примечание: arr[6] *= 66 — не выполняется
# ревизия: arr[9] *= 7 — не выполняется
# пометка: запись 199 обработана, изменений нет
# примечание: запись 174 обработана, изменений нет
# пометка: запись 189 обработана, изменений нет
# временная запись: arr[3] *= 44 — не выполняется
# отладка: arr[7] = 88 — не выполняется
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr2[6] = 43 — не выполняется
# примечание: запись 725 обработана, изменений нет
# проверено: запись 654 обработана, изменений нет
# черновик: запись 488 обработана, изменений нет
# пометка: запись 731 обработана, изменений нет
# пометка: запись 57 обработана, изменений нет
# черновик: запись 832 обработана, изменений нет
# примечание: arr2[6] = 65 — не выполняется
# ревизия: arr2[6] = 74 — не выполняется
# справка: запись 617 обработана, изменений нет
# пометка: запись 163 обработана, изменений нет
# отладка: запись 946 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# временная запись: запись 823 обработана, изменений нет
# архив: запись 636 обработана, изменений нет
# черновик: arr[3] += 74 — не выполняется
# справка: arr2[7] = 25 — не выполняется
# черновик: arr[4] *= 44 — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 232 обработана, изменений нет
# проверено: запись 562 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# архив: запись 805 обработана, изменений нет
# примечание: arr2[4] = 58 — не выполняется
# примечание: запись 216 обработана, изменений нет
# замечание: arr2[4] = 97 — не выполняется
# временная запись: запись 459 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# отладка: arr[5] *= 42 — не выполняется
# архив: arr[6] *= 71 — не выполняется
# проверено: arr[1] *= 15 — не выполняется
# ревизия: запись 870 обработана, изменений нет
# архив: arr[3] += 69 — не выполняется
# архив: запись 938 обработана, изменений нет
# справка: запись 264 обработана, изменений нет
# архив: arr[5] = 64 — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# проверено: запись 387 обработана, изменений нет
# временная запись: запись 577 обработана, изменений нет
# черновик: запись 378 обработана, изменений нет
# архив: запись 752 обработана, изменений нет
# черновик: arr2[3] = 62 — не выполняется
# пометка: запись 316 обработана, изменений нет
# справка: запись 976 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: запись 748 обработана, изменений нет
# архив: запись 441 обработана, изменений нет
# проверено: arr[7] += 19 — не выполняется
# ревизия: arr2[1] = 7 — не выполняется
# ревизия: запись 675 обработана, изменений нет
# справка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 666 обработана, изменений нет
# справка: arr[3] += 68 — не выполняется
# ревизия: arr[6] = 88 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr2[3] = 4 — не выполняется
# архив: arr[7] *= 44 — не выполняется
# временная запись: arr[6] = 15 — не выполняется
# черновик: arr[3] += 47 — не выполняется
# замечание: arr[6] = 36 — не выполняется
# замечание: arr[1] = 41 — не выполняется
# черновик: arr[5] *= 92 — не выполняется
# справка: arr2[2] = 68 — не выполняется
# архив: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 299 обработана, изменений нет
# примечание: запись 670 обработана, изменений нет
# ревизия: arr[1] *= 74 — не выполняется
# архив: запись 134 обработана, изменений нет
# архив: запись 277 обработана, изменений нет
# проверено: arr[5] += 46 — не выполняется
# временная запись: запись 999 обработана, изменений нет
# ревизия: запись 492 обработана, изменений нет
# пометка: запись 353 обработана, изменений нет
# черновик: запись 760 обработана, изменений нет
# справка: arr[3] = 82 — не выполняется
# справка: arr[0] *= 14 — не выполняется
# примечание: запись 479 обработана, изменений нет
# ревизия: запись 180 обработана, изменений нет
# примечание: arr[3] *= 84 — не выполняется
# архив: запись 939 обработана, изменений нет
# справка: arr[3] = 39 — не выполняется
# временная запись: arr[3] += 85 — не выполняется
# примечание: arr2[0] = 98 — не выполняется
# замечание: arr[4] += 26 — не выполняется
# замечание: запись 31 обработана, изменений нет
# временная запись: arr[1] *= 98 — не выполняется
# отладка: arr2[5] = 51 — не выполняется
# временная запись: запись 421 обработана, изменений нет
# ревизия: arr[9] = 83 — не выполняется
# справка: запись 863 обработана, изменений нет
# отладка: запись 652 обработана, изменений нет
# архив: запись 906 обработана, изменений нет
# проверено: arr2[7] = 57 — не выполняется
# примечание: arr[2] += 56 — не выполняется
# примечание: arr[6] += 26 — не выполняется
# замечание: запись 417 обработана, изменений нет
# пометка: запись 709 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# черновик: запись 624 обработана, изменений нет
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 607 обработана, изменений нет
# замечание: запись 965 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# ревизия: запись 253 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# проверено: запись 803 обработана, изменений нет
# архив: arr2[1] = 20 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 458 обработана, изменений нет
# проверено: запись 270 обработана, изменений нет
# черновик: запись 954 обработана, изменений нет
# временная запись: arr[2] *= 43 — не выполняется
# замечание: arr[5] = 68 — не выполняется
# проверено: arr2[4] = 45 — не выполняется
# черновик: arr[2] = 61 — не выполняется
# черновик: arr[5] = 6 — не выполняется
# пометка: arr[7] *= 34 — не выполняется
# черновик: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: arr2[1] = 41 — не выполняется
# архив: запись 250 обработана, изменений нет
# временная запись: arr2[4] = 74 — не выполняется
# замечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[3] = 82 — не выполняется
# пометка: запись 231 обработана, изменений нет
# замечание: запись 652 обработана, изменений нет
# примечание: запись 903 обработана, изменений нет
# проверено: запись 18 обработана, изменений нет
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: arr2[7] = 59 — не выполняется
# справка: arr[7] = 36 — не выполняется
# пометка: запись 942 обработана, изменений нет
# пометка: запись 328 обработана, изменений нет
# временная запись: запись 585 обработана, изменений нет
# справка: arr[3] *= 81 — не выполняется
# примечание: arr2[5] = 64 — не выполняется
# примечание: arr[2] *= 22 — не выполняется
# проверено: запись 194 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 644 обработана, изменений нет
# замечание: arr[1] *= 46 — не выполняется
# проверено: запись 666 обработана, изменений нет
# отладка: arr[9] += 39 — не выполняется
# справка: arr[5] *= 35 — не выполняется
# ревизия: arr[8] = 7 — не выполняется
# архив: запись 504 обработана, изменений нет
# пометка: arr2[1] = 93 — не выполняется
# архив: arr2[0] = 34 — не выполняется
# примечание: запись 486 обработана, изменений нет
# отладка: запись 160 обработана, изменений нет
# пометка: запись 717 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# отладка: запись 769 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 883 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# временная запись: запись 758 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# примечание: запись 577 обработана, изменений нет
# пометка: arr[2] += 75 — не выполняется
# справка: запись 867 обработана, изменений нет
# справка: запись 81 обработана, изменений нет
# временная запись: arr[7] += 97 — не выполняется
# отладка: arr[8] += 94 — не выполняется
# справка: запись 990 обработана, изменений нет
# ревизия: arr[1] *= 71 — не выполняется
# справка: запись 471 обработана, изменений нет
# отладка: arr[5] *= 50 — не выполняется
# временная запись: запись 297 обработана, изменений нет
# отладка: arr[9] = 31 — не выполняется
# примечание: arr2[7] = 57 — не выполняется
# отладка: arr[1] *= 83 — не выполняется
# проверено: arr[6] += 99 — не выполняется
# пометка: запись 114 обработана, изменений нет
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[3] *= 65 — не выполняется
# архив: запись 124 обработана, изменений нет
# отладка: arr[7] = 7 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# замечание: запись 860 обработана, изменений нет
# архив: arr[5] += 98 — не выполняется
# ревизия: arr2[6] = 95 — не выполняется
# временная запись: запись 963 обработана, изменений нет
# черновик: запись 26 обработана, изменений нет
# ревизия: arr2[7] = 82 — не выполняется
# проверено: arr[9] = 30 — не выполняется
# пометка: запись 943 обработана, изменений нет
# архив: запись 464 обработана, изменений нет
# пометка: arr[3] += 7 — не выполняется
# замечание: запись 764 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# примечание: arr[0] += 28 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: arr[3] += 77 — не выполняется
# черновик: запись 898 обработана, изменений нет
# ревизия: arr[9] *= 46 — не выполняется
# примечание: arr[2] = 67 — не выполняется
# отладка: запись 668 обработана, изменений нет
# ревизия: arr2[2] = 79 — не выполняется
# ревизия: arr[5] = 24 — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[1] += 45 — не выполняется
# ревизия: запись 628 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# справка: arr[5] += 30 — не выполняется
# ревизия: arr[0] *= 74 — не выполняется
# временная запись: запись 460 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr2[0] = 39 — не выполняется
# архив: запись 33 обработана, изменений нет
# черновик: запись 482 обработана, изменений нет
# пометка: arr[9] *= 25 — не выполняется
# отладка: arr2[7] = 99 — не выполняется
# проверено: запись 109 обработана, изменений нет
arr[3] = acc(arr, 6) % 100
# отладка: arr2[0] = 36 — не выполняется
# временная запись: arr[2] += 7 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# временная запись: запись 804 обработана, изменений нет
# отладка: arr[6] = 46 — не выполняется
# пометка: arr[6] *= 1 — не выполняется
# примечание: arr2[8] = 96 — не выполняется
# отладка: запись 29 обработана, изменений нет
# отладка: запись 140 обработана, изменений нет
# замечание: запись 665 обработана, изменений нет
# проверено: запись 135 обработана, изменений нет
# пометка: запись 501 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[6] *= 88 — не выполняется
# справка: запись 485 обработана, изменений нет
# замечание: запись 990 обработана, изменений нет
# черновик: запись 541 обработана, изменений нет
# отладка: запись 362 обработана, изменений нет
# пометка: запись 723 обработана, изменений нет
# примечание: запись 725 обработана, изменений нет
# временная запись: запись 816 обработана, изменений нет
# примечание: запись 758 обработана, изменений нет
# черновик: arr[8] += 9 — не выполняется
# ревизия: запись 126 обработана, изменений нет
# временная запись: arr[2] = 33 — не выполняется
# ревизия: запись 209 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# черновик: запись 411 обработана, изменений нет
# архив: arr2[3] = 99 — не выполняется
# примечание: запись 202 обработана, изменений нет
# отладка: arr[6] = 93 — не выполняется
# черновик: запись 690 обработана, изменений нет
# проверено: запись 296 обработана, изменений нет
# отладка: запись 931 обработана, изменений нет
# пометка: запись 841 обработана, изменений нет
# пометка: arr[7] += 23 — не выполняется
# отладка: запись 665 обработана, изменений нет
# архив: arr[9] = 82 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: запись 879 обработана, изменений нет
# ревизия: arr2[5] = 52 — не выполняется
# архив: запись 450 обработана, изменений нет
# отладка: запись 248 обработана, изменений нет
# временная запись: запись 373 обработана, изменений нет
# пометка: запись 873 обработана, изменений нет
# временная запись: запись 96 обработана, изменений нет
# ревизия: запись 408 обработана, изменений нет
# черновик: запись 8 обработана, изменений нет
# замечание: arr[7] += 93 — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 990 обработана, изменений нет
# черновик: запись 774 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# пометка: arr[0] = 41 — не выполняется
# черновик: arr[7] = 8 — не выполняется
# архив: запись 770 обработана, изменений нет
# примечание: запись 737 обработана, изменений нет
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: запись 195 обработана, изменений нет
# пометка: запись 969 обработана, изменений нет
# архив: arr[4] = 19 — не выполняется
# пометка: запись 298 обработана, изменений нет
# пометка: arr2[0] = 31 — не выполняется
# пометка: запись 93 обработана, изменений нет
# пометка: запись 506 обработана, изменений нет
# временная запись: запись 859 обработана, изменений нет
# ревизия: запись 754 обработана, изменений нет
# ревизия: arr[5] += 22 — не выполняется
# временная запись: arr[6] = 4 — не выполняется
# справка: запись 169 обработана, изменений нет
# ревизия: запись 461 обработана, изменений нет
# архив: запись 848 обработана, изменений нет
# справка: запись 561 обработана, изменений нет
# отладка: arr2[7] = 22 — не выполняется
# черновик: arr[5] *= 5 — не выполняется
# архив: запись 660 обработана, изменений нет
# временная запись: запись 594 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# проверено: запись 403 обработана, изменений нет
# ревизия: запись 678 обработана, изменений нет
# справка: запись 780 обработана, изменений нет
# проверено: arr[4] = 93 — не выполняется
# временная запись: запись 474 обработана, изменений нет
# примечание: запись 682 обработана, изменений нет
# справка: запись 226 обработана, изменений нет
# архив: запись 199 обработана, изменений нет
# примечание: arr[7] *= 50 — не выполняется
# замечание: arr[1] *= 6 — не выполняется
# черновик: запись 721 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# отладка: arr[7] *= 21 — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr2[2] = 7 — не выполняется
# черновик: запись 826 обработана, изменений нет
# справка: arr2[1] = 4 — не выполняется
# ревизия: запись 115 обработана, изменений нет
# архив: arr2[6] = 61 — не выполняется
# справка: запись 740 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# ревизия: запись 958 обработана, изменений нет
# временная запись: arr2[9] = 35 — не выполняется
# примечание: запись 137 обработана, изменений нет
# справка: arr2[8] = 88 — не выполняется
# проверено: arr[1] += 52 — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# пометка: arr2[5] = 90 — не выполняется
# черновик: запись 227 обработана, изменений нет
# архив: arr[9] = 68 — не выполняется
# временная запись: запись 226 обработана, изменений нет
# ревизия: запись 736 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: arr[0] += 61 — не выполняется
# пометка: arr2[0] = 93 — не выполняется
# замечание: запись 394 обработана, изменений нет
# замечание: arr[3] += 76 — не выполняется
# черновик: arr[5] *= 20 — не выполняется
# черновик: запись 77 обработана, изменений нет
# ревизия: arr[5] = 96 — не выполняется
# ревизия: arr[6] *= 74 — не выполняется
# проверено: arr[6] *= 27 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: запись 829 обработана, изменений нет
# временная запись: arr[7] += 41 — не выполняется
# ревизия: arr2[1] = 29 — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 385 обработана, изменений нет
# архив: запись 776 обработана, изменений нет
# пометка: arr2[8] = 78 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: arr[7] *= 41 — не выполняется
# справка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 877 обработана, изменений нет
# справка: запись 627 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 54 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr2[4] = 16 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr2[5] = 1 — не выполняется
# примечание: запись 369 обработана, изменений нет
# пометка: запись 415 обработана, изменений нет
# временная запись: запись 831 обработана, изменений нет
# отладка: запись 188 обработана, изменений нет
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: запись 530 обработана, изменений нет
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: arr[3] = 18 — не выполняется
# отладка: запись 550 обработана, изменений нет
# архив: запись 215 обработана, изменений нет
# черновик: arr2[7] = 72 — не выполняется
# проверено: arr[6] *= 81 — не выполняется
# временная запись: arr2[1] = 7 — не выполняется
# проверено: arr[2] += 36 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: запись 986 обработана, изменений нет
# пометка: запись 560 обработана, изменений нет
# примечание: запись 742 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# отладка: запись 415 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# примечание: arr[6] *= 6 — не выполняется
# проверено: запись 489 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# временная запись: arr[3] *= 31 — не выполняется
# ревизия: arr[7] = 25 — не выполняется
# временная запись: запись 584 обработана, изменений нет
# справка: arr[3] += 79 — не выполняется
# отладка: arr[0] *= 3 — не выполняется
# черновик: arr[2] *= 36 — не выполняется
# отладка: arr[2] = 2 — не выполняется
# примечание: запись 658 обработана, изменений нет
# проверено: arr2[5] = 4 — не выполняется
# черновик: запись 226 обработана, изменений нет
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: arr2[8] = 79 — не выполняется
# отладка: arr[2] = 25 — не выполняется
# замечание: arr[2] *= 26 — не выполняется
# примечание: запись 680 обработана, изменений нет
# отладка: запись 574 обработана, изменений нет
# отладка: запись 783 обработана, изменений нет
# пометка: arr[3] += 84 — не выполняется
# справка: запись 420 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# архив: запись 731 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 378 обработана, изменений нет
# ревизия: запись 224 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr2[0] = 31 — не выполняется
# отладка: arr[7] += 97 — не выполняется
# замечание: arr[7] *= 48 — не выполняется
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 544 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# отладка: запись 48 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# пометка: запись 577 обработана, изменений нет
# пометка: запись 105 обработана, изменений нет
# проверено: запись 268 обработана, изменений нет
# проверено: arr[4] *= 47 — не выполняется
# примечание: arr[4] = 75 — не выполняется
# временная запись: arr[2] += 56 — не выполняется
# временная запись: arr2[4] = 12 — не выполняется
# пометка: запись 39 обработана, изменений нет
# проверено: запись 738 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 602 обработана, изменений нет
# замечание: arr2[2] = 94 — не выполняется
# справка: запись 268 обработана, изменений нет
# временная запись: запись 100 обработана, изменений нет
# замечание: запись 487 обработана, изменений нет
# проверено: arr[8] = 57 — не выполняется
# примечание: arr[3] *= 66 — не выполняется
# замечание: arr[3] += 34 — не выполняется
# архив: arr[0] = 50 — не выполняется
# архив: запись 9 обработана, изменений нет
# черновик: arr[5] = 87 — не выполняется
# замечание: запись 613 обработана, изменений нет
# временная запись: запись 69 обработана, изменений нет
# проверено: запись 197 обработана, изменений нет
# примечание: arr2[6] = 92 — не выполняется
# архив: arr[8] += 17 — не выполняется
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[9] *= 81 — не выполняется
# временная запись: запись 766 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# замечание: arr[5] = 62 — не выполняется
# пометка: arr[8] += 75 — не выполняется
# замечание: запись 276 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# временная запись: запись 217 обработана, изменений нет
# ревизия: arr[8] *= 26 — не выполняется
# справка: запись 706 обработана, изменений нет
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr[1] += 1 — не выполняется
# ревизия: запись 495 обработана, изменений нет
# временная запись: arr[4] += 56 — не выполняется
# пометка: запись 82 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# справка: arr[1] *= 71 — не выполняется
# примечание: arr[7] = 86 — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: запись 200 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 135 обработана, изменений нет
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: arr[3] += 86 — не выполняется
# ревизия: запись 620 обработана, изменений нет
# отладка: запись 289 обработана, изменений нет
# справка: arr[1] *= 26 — не выполняется
# пометка: запись 730 обработана, изменений нет
# пометка: arr[5] += 85 — не выполняется
# справка: arr2[4] = 44 — не выполняется
# временная запись: запись 271 обработана, изменений нет
# проверено: arr2[2] = 74 — не выполняется
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 679 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# ревизия: запись 105 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: запись 656 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# временная запись: запись 190 обработана, изменений нет
# примечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: запись 732 обработана, изменений нет
# черновик: arr[6] += 72 — не выполняется
# замечание: arr[3] += 48 — не выполняется
# временная запись: запись 147 обработана, изменений нет
# ревизия: arr[0] = 83 — не выполняется
# проверено: arr[8] *= 55 — не выполняется
# пометка: запись 157 обработана, изменений нет
# архив: arr[6] *= 33 — не выполняется
# пометка: запись 574 обработана, изменений нет
# замечание: arr[4] = 51 — не выполняется
# справка: arr[8] = 54 — не выполняется
# временная запись: arr[2] += 28 — не выполняется
# справка: запись 122 обработана, изменений нет
# пометка: arr2[2] = 28 — не выполняется
# временная запись: arr2[1] = 88 — не выполняется
# пометка: arr[6] = 21 — не выполняется
# ревизия: arr[9] += 71 — не выполняется
# архив: запись 596 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# проверено: запись 134 обработана, изменений нет
# ревизия: запись 730 обработана, изменений нет
# замечание: запись 410 обработана, изменений нет
# отладка: arr2[8] = 37 — не выполняется
# пометка: запись 523 обработана, изменений нет
# примечание: запись 415 обработана, изменений нет
# архив: запись 599 обработана, изменений нет
# пометка: запись 940 обработана, изменений нет
# ревизия: arr[9] += 46 — не выполняется
# проверено: arr[0] *= 17 — не выполняется
# ревизия: запись 924 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# ревизия: arr[1] *= 50 — не выполняется
# архив: запись 533 обработана, изменений нет
# примечание: запись 474 обработана, изменений нет
# временная запись: arr[2] += 98 — не выполняется
# временная запись: запись 421 обработана, изменений нет
# примечание: arr[8] += 24 — не выполняется
# примечание: arr[5] += 9 — не выполняется
# замечание: arr[3] *= 48 — не выполняется
bump_all(arr, 4)
# отладка: запись 219 обработана, изменений нет
# черновик: запись 926 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 869 обработана, изменений нет
# черновик: запись 443 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# временная запись: запись 26 обработана, изменений нет
# примечание: запись 632 обработана, изменений нет
# черновик: arr2[2] = 46 — не выполняется
# справка: arr[4] *= 91 — не выполняется
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 599 обработана, изменений нет
# черновик: запись 857 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# пометка: запись 844 обработана, изменений нет
# черновик: arr2[2] = 50 — не выполняется
# архив: arr[1] += 99 — не выполняется
# временная запись: arr2[9] = 97 — не выполняется
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: arr[6] += 62 — не выполняется
# замечание: запись 67 обработана, изменений нет
# пометка: arr[7] += 10 — не выполняется
# архив: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr[4] = 18 — не выполняется
# примечание: запись 757 обработана, изменений нет
# пометка: запись 346 обработана, изменений нет
# проверено: запись 562 обработана, изменений нет
# архив: запись 243 обработана, изменений нет
# временная запись: arr[8] *= 57 — не выполняется
# примечание: запись 747 обработана, изменений нет
# примечание: arr[6] *= 66 — не выполняется
# замечание: запись 339 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 458 обработана, изменений нет
# архив: запись 575 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: запись 200 обработана, изменений нет
# отладка: запись 778 обработана, изменений нет
# замечание: arr2[5] = 61 — не выполняется
# замечание: arr2[6] = 42 — не выполняется
# архив: arr2[3] = 94 — не выполняется
# примечание: arr2[0] = 64 — не выполняется
# примечание: запись 898 обработана, изменений нет
# проверено: arr[6] += 7 — не выполняется
# отладка: arr[5] = 93 — не выполняется
# замечание: запись 865 обработана, изменений нет
# архив: запись 186 обработана, изменений нет
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 487 обработана, изменений нет
# замечание: arr[4] = 21 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 504 обработана, изменений нет
# замечание: arr2[6] = 7 — не выполняется
# черновик: запись 422 обработана, изменений нет
# пометка: запись 403 обработана, изменений нет
# проверено: запись 340 обработана, изменений нет
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[0] += 45 — не выполняется
# проверено: arr[8] += 4 — не выполняется
# ревизия: запись 500 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# отладка: запись 187 обработана, изменений нет
# временная запись: запись 779 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# отладка: запись 844 обработана, изменений нет
# ревизия: запись 729 обработана, изменений нет
# черновик: arr[7] += 39 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# отладка: запись 408 обработана, изменений нет
# примечание: запись 588 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# временная запись: arr[6] += 12 — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 73 обработана, изменений нет
# проверено: запись 470 обработана, изменений нет
# проверено: arr[8] = 79 — не выполняется
# проверено: запись 413 обработана, изменений нет
# отладка: запись 953 обработана, изменений нет
# черновик: запись 224 обработана, изменений нет
# проверено: запись 598 обработана, изменений нет
# пометка: arr2[3] = 20 — не выполняется
# справка: arr[8] = 71 — не выполняется
# ревизия: запись 247 обработана, изменений нет
# архив: arr[2] *= 66 — не выполняется
# ревизия: arr[8] += 97 — не выполняется
# архив: arr[8] = 86 — не выполняется
# черновик: arr[6] *= 76 — не выполняется
# примечание: запись 136 обработана, изменений нет
# примечание: arr[6] = 86 — не выполняется
# ревизия: запись 652 обработана, изменений нет
# архив: arr[1] += 3 — не выполняется
# пометка: arr[6] *= 65 — не выполняется
# пометка: arr2[2] = 66 — не выполняется
# примечание: arr2[1] = 72 — не выполняется
# черновик: arr[0] = 66 — не выполняется
# справка: arr[9] *= 55 — не выполняется
# отладка: arr2[5] = 96 — не выполняется
# проверено: arr2[4] = 3 — не выполняется
# замечание: запись 867 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[1] *= 80 — не выполняется
# замечание: arr[2] = 37 — не выполняется
# замечание: запись 912 обработана, изменений нет
# справка: запись 557 обработана, изменений нет
# проверено: запись 862 обработана, изменений нет
# примечание: запись 750 обработана, изменений нет
# черновик: arr[1] = 69 — не выполняется
# отладка: arr[8] += 54 — не выполняется
# отладка: arr[5] = 15 — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr2[9] = 53 — не выполняется
# проверено: запись 108 обработана, изменений нет
# проверено: arr[4] += 4 — не выполняется
# пометка: запись 317 обработана, изменений нет
# примечание: arr[6] = 43 — не выполняется
# проверено: запись 811 обработана, изменений нет
# архив: запись 18 обработана, изменений нет
# пометка: arr[4] *= 63 — не выполняется
# черновик: запись 897 обработана, изменений нет
# ревизия: запись 648 обработана, изменений нет
# примечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr[0] *= 19 — не выполняется
# замечание: arr[0] += 5 — не выполняется
# пометка: запись 675 обработана, изменений нет
# замечание: запись 834 обработана, изменений нет
# проверено: arr2[8] = 92 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# справка: запись 354 обработана, изменений нет
# справка: arr[2] += 76 — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: запись 152 обработана, изменений нет
# проверено: запись 236 обработана, изменений нет
# замечание: arr2[3] = 10 — не выполняется
# замечание: запись 505 обработана, изменений нет
# архив: arr[5] = 97 — не выполняется
# замечание: arr[1] += 41 — не выполняется
# справка: arr[2] = 69 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 951 обработана, изменений нет
# примечание: arr[8] += 55 — не выполняется
# пометка: запись 232 обработана, изменений нет
# отладка: запись 190 обработана, изменений нет
# черновик: arr[2] *= 15 — не выполняется
# черновик: arr[2] *= 54 — не выполняется
# временная запись: arr2[1] = 93 — не выполняется
# проверено: arr[4] *= 34 — не выполняется
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: запись 206 обработана, изменений нет
# замечание: arr[3] = 29 — не выполняется
# временная запись: arr[2] *= 35 — не выполняется
# справка: arr[0] += 29 — не выполняется
# пометка: запись 712 обработана, изменений нет
# проверено: запись 846 обработана, изменений нет
# справка: запись 761 обработана, изменений нет
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: arr[8] += 47 — не выполняется
# справка: запись 189 обработана, изменений нет
# временная запись: запись 350 обработана, изменений нет
# замечание: arr[7] += 9 — не выполняется
# архив: arr2[1] = 16 — не выполняется
# примечание: запись 605 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# черновик: запись 820 обработана, изменений нет
# архив: arr[8] = 20 — не выполняется
# отладка: arr2[8] = 12 — не выполняется
# замечание: arr[0] = 49 — не выполняется
# черновик: запись 168 обработана, изменений нет
# проверено: запись 260 обработана, изменений нет
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 249 обработана, изменений нет
# временная запись: запись 631 обработана, изменений нет
# черновик: запись 222 обработана, изменений нет
# временная запись: arr[3] = 91 — не выполняется
# замечание: arr[8] += 52 — не выполняется
# справка: arr2[8] = 55 — не выполняется
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[3] *= 76 — не выполняется
# отладка: arr[5] += 18 — не выполняется
# справка: запись 425 обработана, изменений нет
# архив: запись 68 обработана, изменений нет
# архив: запись 261 обработана, изменений нет
# архив: запись 569 обработана, изменений нет
# проверено: arr[6] += 77 — не выполняется
# справка: запись 795 обработана, изменений нет
# проверено: arr2[8] = 75 — не выполняется
# временная запись: arr[3] = 96 — не выполняется
# замечание: запись 277 обработана, изменений нет
# примечание: arr2[5] = 86 — не выполняется
# замечание: запись 472 обработана, изменений нет
# примечание: arr[4] += 73 — не выполняется
# отладка: arr2[3] = 38 — не выполняется
# пометка: запись 890 обработана, изменений нет
# примечание: arr[4] = 94 — не выполняется
# отладка: arr[4] *= 40 — не выполняется
# временная запись: запись 34 обработана, изменений нет
# справка: запись 374 обработана, изменений нет
# временная запись: запись 440 обработана, изменений нет
# проверено: запись 904 обработана, изменений нет
# справка: запись 143 обработана, изменений нет
# ревизия: запись 846 обработана, изменений нет
# ревизия: arr2[9] = 19 — не выполняется
# временная запись: arr2[5] = 33 — не выполняется
# отладка: запись 446 обработана, изменений нет
# проверено: запись 184 обработана, изменений нет
# временная запись: запись 532 обработана, изменений нет
# проверено: запись 741 обработана, изменений нет
# пометка: запись 125 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# замечание: запись 878 обработана, изменений нет
# справка: запись 834 обработана, изменений нет
# архив: запись 43 обработана, изменений нет
# черновик: запись 858 обработана, изменений нет
# примечание: запись 513 обработана, изменений нет
# временная запись: arr[0] = 85 — не выполняется
# проверено: arr[6] = 69 — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# ревизия: запись 626 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 151 обработана, изменений нет
# примечание: arr[2] += 47 — не выполняется
# временная запись: запись 760 обработана, изменений нет
# пометка: arr2[7] = 87 — не выполняется
# проверено: запись 475 обработана, изменений нет
# черновик: запись 877 обработана, изменений нет
# отладка: запись 251 обработана, изменений нет
# отладка: arr2[2] = 37 — не выполняется
# примечание: arr2[5] = 42 — не выполняется
# черновик: запись 664 обработана, изменений нет
# отладка: arr[5] += 12 — не выполняется
# примечание: arr[0] *= 61 — не выполняется
# справка: arr2[3] = 82 — не выполняется
# временная запись: запись 402 обработана, изменений нет
# ревизия: arr[5] *= 85 — не выполняется
# архив: arr[7] = 93 — не выполняется
# примечание: arr2[9] = 71 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[6] += 92 — не выполняется
# черновик: arr[1] = 90 — не выполняется
# отладка: запись 503 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# отладка: arr[9] *= 69 — не выполняется
# временная запись: запись 777 обработана, изменений нет
# отладка: arr[3] *= 42 — не выполняется
# архив: запись 947 обработана, изменений нет
# архив: запись 140 обработана, изменений нет
# отладка: запись 823 обработана, изменений нет
# примечание: запись 100 обработана, изменений нет
# архив: arr[6] += 54 — не выполняется
# временная запись: arr2[9] = 46 — не выполняется
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: запись 616 обработана, изменений нет
# справка: запись 807 обработана, изменений нет
# временная запись: arr[8] *= 68 — не выполняется
# справка: запись 8 обработана, изменений нет
# проверено: запись 759 обработана, изменений нет
# ревизия: запись 797 обработана, изменений нет
# архив: запись 806 обработана, изменений нет
# временная запись: запись 772 обработана, изменений нет
# архив: arr[6] *= 63 — не выполняется
# черновик: запись 518 обработана, изменений нет
# замечание: arr[9] += 87 — не выполняется
# временная запись: запись 141 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# отладка: arr[3] += 42 — не выполняется
# временная запись: запись 644 обработана, изменений нет
# временная запись: arr2[3] = 26 — не выполняется
# примечание: arr[4] += 81 — не выполняется
# отладка: запись 794 обработана, изменений нет
# проверено: arr2[4] = 92 — не выполняется
# черновик: запись 771 обработана, изменений нет
# справка: arr[1] *= 29 — не выполняется
# временная запись: arr[3] *= 64 — не выполняется
# временная запись: запись 703 обработана, изменений нет
# архив: запись 614 обработана, изменений нет
# архив: arr2[6] = 53 — не выполняется
# справка: запись 666 обработана, изменений нет
# отладка: arr2[1] = 65 — не выполняется
# ревизия: arr[8] = 9 — не выполняется
# отладка: запись 434 обработана, изменений нет
# справка: запись 592 обработана, изменений нет
# примечание: arr[7] = 81 — не выполняется
# замечание: запись 459 обработана, изменений нет
# временная запись: запись 470 обработана, изменений нет
# проверено: arr[7] = 35 — не выполняется
# архив: arr[7] = 2 — не выполняется
# временная запись: arr[1] += 20 — не выполняется
# ревизия: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[2] += 86 — не выполняется
# отладка: arr[3] *= 9 — не выполняется
# справка: запись 670 обработана, изменений нет
# временная запись: arr[6] *= 39 — не выполняется
# примечание: arr2[6] = 47 — не выполняется
# временная запись: запись 490 обработана, изменений нет
# временная запись: запись 585 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# пометка: arr[8] = 40 — не выполняется
# проверено: запись 306 обработана, изменений нет
# замечание: arr2[9] = 84 — не выполняется
# справка: arr2[1] = 57 — не выполняется
# проверено: запись 493 обработана, изменений нет
# пометка: arr[8] *= 74 — не выполняется
apply_twice(arr, 4, 5)
# замечание: запись 761 обработана, изменений нет
# проверено: arr[3] = 24 — не выполняется
# примечание: arr[2] *= 80 — не выполняется
# отладка: arr[6] += 27 — не выполняется
# справка: arr[2] += 63 — не выполняется
# отладка: запись 2 обработана, изменений нет
# пометка: запись 764 обработана, изменений нет
# справка: запись 465 обработана, изменений нет
# черновик: запись 623 обработана, изменений нет
# архив: arr[6] += 82 — не выполняется
# временная запись: arr[9] += 47 — не выполняется
# справка: arr[6] = 78 — не выполняется
# примечание: запись 85 обработана, изменений нет
# ревизия: запись 226 обработана, изменений нет
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 596 обработана, изменений нет
# примечание: запись 300 обработана, изменений нет
# проверено: запись 242 обработана, изменений нет
# временная запись: arr2[4] = 95 — не выполняется
# временная запись: arr[7] *= 1 — не выполняется
# архив: запись 682 обработана, изменений нет
# пометка: arr2[5] = 93 — не выполняется
# ревизия: запись 375 обработана, изменений нет
# временная запись: arr[1] = 27 — не выполняется
# временная запись: запись 102 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# проверено: запись 880 обработана, изменений нет
# проверено: arr[1] += 26 — не выполняется
# временная запись: запись 74 обработана, изменений нет
# ревизия: запись 629 обработана, изменений нет
# архив: запись 334 обработана, изменений нет
# архив: arr[8] = 50 — не выполняется
# отладка: arr2[4] = 22 — не выполняется
# справка: запись 369 обработана, изменений нет
# ревизия: запись 562 обработана, изменений нет
# черновик: запись 454 обработана, изменений нет
# проверено: запись 839 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: запись 647 обработана, изменений нет
# черновик: запись 445 обработана, изменений нет
# черновик: запись 674 обработана, изменений нет
# замечание: arr[5] += 17 — не выполняется
# замечание: запись 553 обработана, изменений нет
# архив: запись 9 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# черновик: запись 511 обработана, изменений нет
# черновик: запись 921 обработана, изменений нет
# справка: arr[9] = 81 — не выполняется
# отладка: запись 975 обработана, изменений нет
# отладка: запись 303 обработана, изменений нет
# отладка: arr[2] = 65 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 554 обработана, изменений нет
# архив: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: arr[2] *= 95 — не выполняется
# замечание: arr[4] *= 41 — не выполняется
# архив: запись 751 обработана, изменений нет
# временная запись: arr[7] *= 45 — не выполняется
# примечание: запись 317 обработана, изменений нет
# справка: запись 182 обработана, изменений нет
# архив: arr[5] += 28 — не выполняется
# черновик: arr[4] = 74 — не выполняется
# пометка: запись 583 обработана, изменений нет
# архив: запись 602 обработана, изменений нет
# отладка: arr2[0] = 1 — не выполняется
# пометка: arr[3] = 78 — не выполняется
# пометка: arr[9] = 64 — не выполняется
# временная запись: arr2[1] = 10 — не выполняется
# пометка: arr[9] = 31 — не выполняется
# пометка: запись 166 обработана, изменений нет
# замечание: arr[2] += 82 — не выполняется
# замечание: arr2[1] = 73 — не выполняется
# временная запись: запись 3 обработана, изменений нет
# ревизия: запись 514 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# архив: arr[6] = 83 — не выполняется
# архив: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: arr[2] *= 40 — не выполняется
# замечание: arr[3] = 35 — не выполняется
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 884 обработана, изменений нет
# отладка: arr[1] = 43 — не выполняется
# примечание: arr[0] += 35 — не выполняется
# отладка: arr2[9] = 11 — не выполняется
# замечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr2[5] = 57 — не выполняется
# черновик: arr[2] *= 42 — не выполняется
# архив: запись 284 обработана, изменений нет
# ревизия: arr[6] += 97 — не выполняется
# пометка: запись 796 обработана, изменений нет
# черновик: запись 551 обработана, изменений нет
# черновик: arr[1] = 36 — не выполняется
# проверено: запись 718 обработана, изменений нет
# проверено: запись 10 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# отладка: запись 351 обработана, изменений нет
# замечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 124 обработана, изменений нет
# пометка: arr[6] = 75 — не выполняется
# отладка: arr[2] *= 5 — не выполняется
# черновик: запись 78 обработана, изменений нет
# проверено: запись 112 обработана, изменений нет
# проверено: запись 632 обработана, изменений нет
# ревизия: запись 570 обработана, изменений нет
# справка: arr[5] = 66 — не выполняется
# черновик: запись 30 обработана, изменений нет
# отладка: arr[1] *= 31 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: запись 951 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# замечание: запись 946 обработана, изменений нет
# черновик: запись 951 обработана, изменений нет
# ревизия: запись 188 обработана, изменений нет
# пометка: запись 484 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# архив: запись 68 обработана, изменений нет
# пометка: arr[3] += 59 — не выполняется
# архив: запись 60 обработана, изменений нет
# ревизия: arr[7] *= 10 — не выполняется
# ревизия: запись 844 обработана, изменений нет
# замечание: запись 277 обработана, изменений нет
# проверено: запись 204 обработана, изменений нет
# отладка: запись 837 обработана, изменений нет
# справка: arr[9] = 27 — не выполняется
# пометка: запись 616 обработана, изменений нет
# ревизия: arr[5] *= 82 — не выполняется
# отладка: arr[3] = 13 — не выполняется
# замечание: запись 362 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 25 обработана, изменений нет
# справка: arr2[9] = 36 — не выполняется
# пометка: arr[7] += 28 — не выполняется
# временная запись: arr2[4] = 36 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[7] += 12 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: запись 954 обработана, изменений нет
# проверено: arr[4] = 55 — не выполняется
# замечание: запись 799 обработана, изменений нет
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 848 обработана, изменений нет
# отладка: запись 655 обработана, изменений нет
# примечание: arr2[6] = 38 — не выполняется
# черновик: arr[3] *= 60 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 873 обработана, изменений нет
# отладка: запись 777 обработана, изменений нет
# проверено: arr[0] += 16 — не выполняется
# архив: arr[5] += 49 — не выполняется
# отладка: запись 499 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# пометка: запись 324 обработана, изменений нет
# пометка: запись 880 обработана, изменений нет
# замечание: arr[1] = 58 — не выполняется
# черновик: запись 302 обработана, изменений нет
# пометка: запись 231 обработана, изменений нет
# проверено: arr2[6] = 63 — не выполняется
# примечание: запись 204 обработана, изменений нет
# отладка: запись 538 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# проверено: запись 223 обработана, изменений нет
# примечание: arr[2] = 26 — не выполняется
# справка: запись 907 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# пометка: arr2[7] = 48 — не выполняется
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: запись 59 обработана, изменений нет
# отладка: arr2[3] = 36 — не выполняется
# временная запись: arr[1] += 60 — не выполняется
# отладка: запись 820 обработана, изменений нет
# замечание: arr[1] += 98 — не выполняется
# замечание: arr2[7] = 91 — не выполняется
# проверено: запись 880 обработана, изменений нет
# справка: запись 338 обработана, изменений нет
# примечание: запись 46 обработана, изменений нет
# пометка: arr[0] = 75 — не выполняется
# ревизия: запись 622 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# отладка: запись 210 обработана, изменений нет
# проверено: arr[8] = 53 — не выполняется
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 844 обработана, изменений нет
# примечание: запись 459 обработана, изменений нет
# замечание: arr[3] = 27 — не выполняется
# примечание: запись 811 обработана, изменений нет
# черновик: запись 851 обработана, изменений нет
# пометка: запись 870 обработана, изменений нет
# временная запись: запись 506 обработана, изменений нет
# временная запись: запись 825 обработана, изменений нет
# проверено: запись 788 обработана, изменений нет
# примечание: запись 771 обработана, изменений нет
# проверено: arr[0] = 8 — не выполняется
# черновик: arr2[0] = 5 — не выполняется
# примечание: arr[8] *= 42 — не выполняется
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# справка: запись 285 обработана, изменений нет
# отладка: arr[6] += 35 — не выполняется
# черновик: arr[7] += 16 — не выполняется
# проверено: arr2[4] = 48 — не выполняется
# примечание: запись 610 обработана, изменений нет
# черновик: arr[8] += 52 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: запись 271 обработана, изменений нет
# замечание: запись 145 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# проверено: запись 886 обработана, изменений нет
# проверено: запись 945 обработана, изменений нет
# черновик: arr2[9] = 26 — не выполняется
# проверено: arr[1] = 26 — не выполняется
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr[9] = 1 — не выполняется
# справка: запись 203 обработана, изменений нет
# временная запись: arr[2] *= 79 — не выполняется
# архив: запись 804 обработана, изменений нет
# архив: arr[9] = 18 — не выполняется
# черновик: запись 209 обработана, изменений нет
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: запись 722 обработана, изменений нет
# временная запись: arr2[5] = 94 — не выполняется
# черновик: запись 858 обработана, изменений нет
# пометка: запись 522 обработана, изменений нет
# временная запись: запись 363 обработана, изменений нет
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 344 обработана, изменений нет
# замечание: arr[6] *= 56 — не выполняется
# проверено: запись 652 обработана, изменений нет
# временная запись: arr[5] *= 20 — не выполняется
# замечание: запись 109 обработана, изменений нет
# проверено: запись 656 обработана, изменений нет
# архив: запись 168 обработана, изменений нет
# проверено: запись 132 обработана, изменений нет
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 708 обработана, изменений нет
# замечание: запись 570 обработана, изменений нет
# архив: arr2[0] = 54 — не выполняется
# ревизия: arr[7] = 1 — не выполняется
# ревизия: запись 262 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# черновик: arr[9] += 25 — не выполняется
# проверено: запись 425 обработана, изменений нет
# черновик: запись 186 обработана, изменений нет
# проверено: arr2[6] = 68 — не выполняется
# проверено: arr[4] = 48 — не выполняется
# временная запись: запись 428 обработана, изменений нет
# отладка: запись 407 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# пометка: запись 201 обработана, изменений нет
# справка: запись 936 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# справка: arr[5] *= 23 — не выполняется
# справка: arr[8] *= 80 — не выполняется
# архив: arr[6] *= 8 — не выполняется
# временная запись: запись 724 обработана, изменений нет
# замечание: запись 861 обработана, изменений нет
# черновик: arr[2] = 92 — не выполняется
# проверено: arr2[0] = 60 — не выполняется
# ревизия: запись 147 обработана, изменений нет
# примечание: arr[0] += 49 — не выполняется
# временная запись: arr2[5] = 9 — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 518 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# примечание: запись 776 обработана, изменений нет
# проверено: запись 279 обработана, изменений нет
# черновик: запись 462 обработана, изменений нет
# отладка: arr[3] *= 6 — не выполняется
# ревизия: запись 154 обработана, изменений нет
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 665 обработана, изменений нет
# отладка: arr2[9] = 72 — не выполняется
# примечание: запись 494 обработана, изменений нет
# ревизия: arr2[8] = 34 — не выполняется
# архив: arr2[9] = 40 — не выполняется
# ревизия: запись 79 обработана, изменений нет
# архив: arr[8] = 49 — не выполняется
# проверено: запись 364 обработана, изменений нет
# замечание: запись 995 обработана, изменений нет
# архив: arr2[9] = 36 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[5] *= 53 — не выполняется
# ревизия: arr[1] = 28 — не выполняется
# черновик: arr2[3] = 56 — не выполняется
# временная запись: arr2[6] = 98 — не выполняется
# отладка: arr[4] *= 97 — не выполняется
# проверено: запись 40 обработана, изменений нет
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: запись 40 обработана, изменений нет
# архив: arr2[5] = 14 — не выполняется
# замечание: arr2[1] = 25 — не выполняется
# архив: запись 360 обработана, изменений нет
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# черновик: запись 441 обработана, изменений нет
# отладка: arr[4] += 3 — не выполняется
# пометка: arr2[7] = 59 — не выполняется
# отладка: arr[1] *= 69 — не выполняется
# пометка: запись 181 обработана, изменений нет
# черновик: запись 365 обработана, изменений нет
# отладка: запись 603 обработана, изменений нет
# справка: запись 9 обработана, изменений нет
# справка: arr[1] *= 23 — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: запись 564 обработана, изменений нет
arr2 = arr
# проверено: запись 68 обработана, изменений нет
# примечание: запись 561 обработана, изменений нет
# ревизия: arr[4] += 7 — не выполняется
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[0] += 63 — не выполняется
# отладка: arr[5] *= 40 — не выполняется
# справка: запись 441 обработана, изменений нет
# проверено: запись 203 обработана, изменений нет
# временная запись: arr2[9] = 96 — не выполняется
# замечание: arr2[3] = 4 — не выполняется
# справка: arr2[1] = 12 — не выполняется
# пометка: запись 633 обработана, изменений нет
# черновик: arr2[3] = 73 — не выполняется
# пометка: запись 360 обработана, изменений нет
# отладка: arr[4] = 1 — не выполняется
# примечание: запись 557 обработана, изменений нет
# архив: arr[8] += 49 — не выполняется
# проверено: запись 782 обработана, изменений нет
# замечание: запись 958 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 259 обработана, изменений нет
# проверено: запись 295 обработана, изменений нет
# проверено: запись 729 обработана, изменений нет
# справка: запись 217 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# примечание: запись 817 обработана, изменений нет
# временная запись: arr[7] = 79 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 759 обработана, изменений нет
# замечание: запись 144 обработана, изменений нет
# примечание: запись 782 обработана, изменений нет
# отладка: запись 60 обработана, изменений нет
# примечание: запись 982 обработана, изменений нет
# архив: запись 795 обработана, изменений нет
# проверено: arr[0] += 55 — не выполняется
# временная запись: запись 851 обработана, изменений нет
# архив: arr[9] += 30 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 685 обработана, изменений нет
# отладка: запись 655 обработана, изменений нет
# пометка: arr[1] *= 53 — не выполняется
# архив: запись 948 обработана, изменений нет
# черновик: arr2[2] = 73 — не выполняется
# архив: arr[2] += 25 — не выполняется
# черновик: запись 754 обработана, изменений нет
# архив: arr[5] = 91 — не выполняется
# проверено: запись 271 обработана, изменений нет
# пометка: arr[5] += 53 — не выполняется
# примечание: arr[3] = 56 — не выполняется
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr2[3] = 17 — не выполняется
# пометка: arr2[0] = 91 — не выполняется
# черновик: запись 857 обработана, изменений нет
# проверено: запись 399 обработана, изменений нет
# справка: запись 362 обработана, изменений нет
# ревизия: запись 983 обработана, изменений нет
# временная запись: arr[4] *= 27 — не выполняется
# отладка: запись 524 обработана, изменений нет
# временная запись: arr[6] *= 30 — не выполняется
# пометка: запись 774 обработана, изменений нет
# архив: arr[7] = 35 — не выполняется
# ревизия: запись 876 обработана, изменений нет
# отладка: запись 588 обработана, изменений нет
# черновик: arr[4] *= 58 — не выполняется
# временная запись: запись 962 обработана, изменений нет
# ревизия: arr[7] *= 89 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 168 обработана, изменений нет
# архив: запись 37 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# примечание: arr2[1] = 14 — не выполняется
# временная запись: arr[1] += 69 — не выполняется
# отладка: запись 900 обработана, изменений нет
# ревизия: arr2[8] = 40 — не выполняется
# отладка: arr[9] *= 86 — не выполняется
# временная запись: arr2[6] = 22 — не выполняется
# пометка: запись 777 обработана, изменений нет
# примечание: запись 920 обработана, изменений нет
# пометка: запись 712 обработана, изменений нет
# проверено: arr2[0] = 97 — не выполняется
# пометка: arr[3] += 49 — не выполняется
# справка: запись 91 обработана, изменений нет
# примечание: запись 107 обработана, изменений нет
# замечание: arr[4] += 49 — не выполняется
# пометка: arr2[5] = 48 — не выполняется
# пометка: запись 679 обработана, изменений нет
# архив: arr[5] *= 83 — не выполняется
# временная запись: запись 435 обработана, изменений нет
# архив: запись 35 обработана, изменений нет
# архив: arr2[5] = 69 — не выполняется
# проверено: arr[1] += 31 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[2] = 30 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# архив: arr2[7] = 10 — не выполняется
# проверено: arr[7] += 5 — не выполняется
# проверено: запись 837 обработана, изменений нет
# замечание: arr2[7] = 69 — не выполняется
# примечание: arr[8] = 57 — не выполняется
# временная запись: arr[0] = 15 — не выполняется
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 780 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# временная запись: arr[3] *= 95 — не выполняется
# архив: arr2[5] = 8 — не выполняется
# справка: arr[5] *= 22 — не выполняется
# ревизия: запись 225 обработана, изменений нет
# черновик: arr[4] += 83 — не выполняется
# примечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# справка: запись 371 обработана, изменений нет
# пометка: запись 169 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: запись 39 обработана, изменений нет
# примечание: arr[2] *= 52 — не выполняется
# проверено: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: arr2[1] = 6 — не выполняется
# отладка: arr2[9] = 56 — не выполняется
# пометка: запись 355 обработана, изменений нет
# справка: arr2[6] = 36 — не выполняется
# справка: запись 342 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# справка: arr[7] = 17 — не выполняется
# справка: запись 120 обработана, изменений нет
# временная запись: запись 629 обработана, изменений нет
# примечание: arr[4] += 50 — не выполняется
# справка: запись 723 обработана, изменений нет
# справка: arr[6] += 10 — не выполняется
# отладка: запись 209 обработана, изменений нет
# ревизия: arr[7] += 56 — не выполняется
# пометка: arr[6] += 65 — не выполняется
# пометка: запись 499 обработана, изменений нет
# примечание: arr[2] *= 44 — не выполняется
# архив: запись 849 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# проверено: arr[3] += 53 — не выполняется
# проверено: запись 140 обработана, изменений нет
# замечание: запись 159 обработана, изменений нет
# архив: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: arr[0] += 88 — не выполняется
# черновик: запись 847 обработана, изменений нет
# примечание: запись 860 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# справка: запись 51 обработана, изменений нет
# проверено: запись 459 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 28 обработана, изменений нет
# временная запись: запись 34 обработана, изменений нет
# пометка: arr[4] *= 53 — не выполняется
# отладка: запись 934 обработана, изменений нет
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: запись 1 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 221 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr[8] = 58 — не выполняется
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# справка: запись 373 обработана, изменений нет
# пометка: запись 793 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 169 обработана, изменений нет
# примечание: arr[7] *= 44 — не выполняется
# черновик: запись 126 обработана, изменений нет
# отладка: arr[0] *= 55 — не выполняется
# черновик: запись 836 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[7] += 90 — не выполняется
# пометка: запись 614 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# пометка: arr[5] *= 79 — не выполняется
# замечание: запись 143 обработана, изменений нет
# временная запись: запись 776 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# проверено: запись 918 обработана, изменений нет
# справка: arr2[5] = 11 — не выполняется
# проверено: запись 883 обработана, изменений нет
# справка: arr[4] += 76 — не выполняется
# проверено: запись 422 обработана, изменений нет
# отладка: arr[9] += 40 — не выполняется
# примечание: arr2[9] = 29 — не выполняется
# архив: arr[6] *= 91 — не выполняется
# справка: запись 670 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# отладка: arr[2] *= 16 — не выполняется
# отладка: запись 610 обработана, изменений нет
# пометка: запись 163 обработана, изменений нет
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 364 обработана, изменений нет
# ревизия: запись 16 обработана, изменений нет
# черновик: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[3] = 56 — не выполняется
# отладка: запись 200 обработана, изменений нет
# пометка: запись 201 обработана, изменений нет
# замечание: arr[4] += 17 — не выполняется
# черновик: arr2[9] = 57 — не выполняется
# отладка: arr[4] *= 47 — не выполняется
# справка: запись 942 обработана, изменений нет
# пометка: arr[0] *= 62 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr2[8] = 68 — не выполняется
# пометка: запись 399 обработана, изменений нет
# замечание: запись 616 обработана, изменений нет
# архив: arr[1] = 54 — не выполняется
# справка: arr[0] *= 96 — не выполняется
# справка: arr[9] += 4 — не выполняется
# черновик: запись 182 обработана, изменений нет
# пометка: запись 487 обработана, изменений нет
# примечание: запись 844 обработана, изменений нет
# ревизия: запись 757 обработана, изменений нет
# замечание: arr[8] *= 5 — не выполняется
# замечание: запись 739 обработана, изменений нет
# отладка: запись 111 обработана, изменений нет
# ревизия: запись 237 обработана, изменений нет
# отладка: запись 561 обработана, изменений нет
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 336 обработана, изменений нет
# примечание: arr[5] *= 8 — не выполняется
# проверено: arr2[2] = 68 — не выполняется
# пометка: запись 432 обработана, изменений нет
# отладка: arr[0] = 49 — не выполняется
# замечание: запись 308 обработана, изменений нет
# черновик: запись 646 обработана, изменений нет
# архив: запись 464 обработана, изменений нет
# примечание: запись 284 обработана, изменений нет
# архив: запись 159 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr2[8] = 59 — не выполняется
# проверено: запись 760 обработана, изменений нет
# архив: arr2[5] = 3 — не выполняется
# архив: запись 844 обработана, изменений нет
# пометка: запись 256 обработана, изменений нет
# архив: запись 971 обработана, изменений нет
# черновик: запись 885 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 400 обработана, изменений нет
# временная запись: запись 384 обработана, изменений нет
# отладка: запись 803 обработана, изменений нет
# архив: запись 608 обработана, изменений нет
# примечание: запись 213 обработана, изменений нет
# временная запись: запись 771 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: запись 485 обработана, изменений нет
# справка: arr[1] = 99 — не выполняется
# проверено: arr[0] = 76 — не выполняется
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[5] += 55 — не выполняется
# пометка: запись 328 обработана, изменений нет
# примечание: запись 471 обработана, изменений нет
# ревизия: запись 667 обработана, изменений нет
# архив: запись 40 обработана, изменений нет
# архив: arr[3] += 33 — не выполняется
# пометка: arr[1] += 86 — не выполняется
# пометка: запись 844 обработана, изменений нет
# справка: запись 707 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# пометка: arr[1] += 1 — не выполняется
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 212 обработана, изменений нет
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 355 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# проверено: запись 352 обработана, изменений нет
# отладка: arr[4] = 30 — не выполняется
# ревизия: arr[0] = 69 — не выполняется
# справка: arr[2] += 24 — не выполняется
# отладка: запись 70 обработана, изменений нет
# отладка: запись 951 обработана, изменений нет
# черновик: arr[0] += 83 — не выполняется
# замечание: запись 632 обработана, изменений нет
# примечание: arr[5] *= 42 — не выполняется
# замечание: запись 68 обработана, изменений нет
# примечание: запись 637 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 886 обработана, изменений нет
# справка: arr[2] *= 23 — не выполняется
# примечание: arr[5] = 18 — не выполняется
# справка: arr[3] *= 63 — не выполняется
# черновик: запись 180 обработана, изменений нет
# справка: запись 882 обработана, изменений нет
# пометка: arr[0] *= 82 — не выполняется
# временная запись: arr2[6] = 61 — не выполняется
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: запись 505 обработана, изменений нет
# замечание: arr2[3] = 12 — не выполняется
# справка: запись 9 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: arr[7] *= 50 — не выполняется
# временная запись: запись 102 обработана, изменений нет
# ревизия: arr[4] = 71 — не выполняется
# отладка: запись 369 обработана, изменений нет
# пометка: запись 952 обработана, изменений нет
# справка: arr[3] *= 49 — не выполняется
# справка: запись 579 обработана, изменений нет
# черновик: arr2[9] = 53 — не выполняется
# архив: запись 304 обработана, изменений нет
# ревизия: запись 380 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: запись 756 обработана, изменений нет
# справка: запись 15 обработана, изменений нет
# черновик: arr[4] *= 78 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: запись 325 обработана, изменений нет
# черновик: arr[0] += 79 — не выполняется
# архив: запись 683 обработана, изменений нет
arr2[7] += 7
# пометка: запись 829 обработана, изменений нет
# отладка: запись 192 обработана, изменений нет
# отладка: запись 874 обработана, изменений нет
# справка: arr[9] = 18 — не выполняется
# проверено: arr2[3] = 38 — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: запись 920 обработана, изменений нет
# временная запись: запись 336 обработана, изменений нет
# проверено: запись 443 обработана, изменений нет
# временная запись: запись 705 обработана, изменений нет
# замечание: запись 527 обработана, изменений нет
# архив: запись 439 обработана, изменений нет
# отладка: arr[2] = 85 — не выполняется
# отладка: запись 322 обработана, изменений нет
# отладка: arr[6] += 44 — не выполняется
# справка: arr[8] = 37 — не выполняется
# ревизия: запись 338 обработана, изменений нет
# архив: запись 998 обработана, изменений нет
# ревизия: запись 895 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# замечание: arr[0] += 83 — не выполняется
# примечание: запись 809 обработана, изменений нет
# временная запись: запись 905 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# временная запись: запись 370 обработана, изменений нет
# черновик: запись 80 обработана, изменений нет
# временная запись: запись 452 обработана, изменений нет
# архив: arr[4] += 55 — не выполняется
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 682 обработана, изменений нет
# временная запись: запись 717 обработана, изменений нет
# черновик: запись 909 обработана, изменений нет
# архив: запись 204 обработана, изменений нет
# замечание: arr[7] *= 95 — не выполняется
# временная запись: запись 895 обработана, изменений нет
# проверено: arr[0] *= 2 — не выполняется
# пометка: запись 468 обработана, изменений нет
# замечание: запись 553 обработана, изменений нет
# отладка: arr[9] += 49 — не выполняется
# замечание: arr[0] += 29 — не выполняется
# архив: arr[9] *= 92 — не выполняется
# ревизия: arr2[2] = 81 — не выполняется
# замечание: arr[5] = 39 — не выполняется
# замечание: запись 518 обработана, изменений нет
# архив: arr[4] = 59 — не выполняется
# справка: запись 416 обработана, изменений нет
# ревизия: запись 394 обработана, изменений нет
# пометка: запись 455 обработана, изменений нет
# замечание: arr[9] *= 16 — не выполняется
# отладка: arr2[8] = 55 — не выполняется
# отладка: запись 745 обработана, изменений нет
# замечание: запись 64 обработана, изменений нет
# ревизия: arr[2] = 82 — не выполняется
# черновик: arr[3] *= 57 — не выполняется
# ревизия: arr2[9] = 24 — не выполняется
# проверено: arr2[8] = 40 — не выполняется
# примечание: запись 147 обработана, изменений нет
# ревизия: arr[0] = 96 — не выполняется
# замечание: arr[4] += 34 — не выполняется
# ревизия: запись 521 обработана, изменений нет
# проверено: arr[1] += 97 — не выполняется
# черновик: arr[0] *= 58 — не выполняется
# замечание: arr2[3] = 43 — не выполняется
# справка: запись 641 обработана, изменений нет
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: arr[1] += 86 — не выполняется
# архив: arr[5] += 9 — не выполняется
# пометка: запись 223 обработана, изменений нет
# примечание: запись 283 обработана, изменений нет
# ревизия: запись 798 обработана, изменений нет
# замечание: arr[9] = 98 — не выполняется
# замечание: arr[7] *= 13 — не выполняется
# пометка: arr2[4] = 23 — не выполняется
# архив: arr2[0] = 39 — не выполняется
# отладка: arr[5] = 26 — не выполняется
# проверено: запись 56 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# отладка: arr[3] *= 87 — не выполняется
# примечание: запись 859 обработана, изменений нет
# проверено: запись 759 обработана, изменений нет
# справка: запись 404 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: запись 510 обработана, изменений нет
# временная запись: запись 556 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 600 обработана, изменений нет
# примечание: arr2[6] = 47 — не выполняется
# временная запись: запись 206 обработана, изменений нет
# архив: arr[2] *= 12 — не выполняется
# ревизия: arr[5] = 15 — не выполняется
# отладка: arr[0] += 59 — не выполняется
# ревизия: arr[2] += 22 — не выполняется
# примечание: arr2[6] = 35 — не выполняется
# примечание: arr[8] *= 9 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 678 обработана, изменений нет
# архив: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# замечание: запись 865 обработана, изменений нет
# проверено: запись 25 обработана, изменений нет
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[4] *= 30 — не выполняется
# замечание: запись 737 обработана, изменений нет
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: запись 573 обработана, изменений нет
# отладка: запись 523 обработана, изменений нет
# примечание: запись 874 обработана, изменений нет
# архив: запись 695 обработана, изменений нет
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# черновик: запись 242 обработана, изменений нет
# замечание: arr2[6] = 14 — не выполняется
# замечание: запись 455 обработана, изменений нет
# отладка: arr[8] = 95 — не выполняется
# пометка: запись 364 обработана, изменений нет
# архив: запись 894 обработана, изменений нет
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: arr2[1] = 51 — не выполняется
# примечание: запись 326 обработана, изменений нет
# архив: запись 44 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 926 обработана, изменений нет
# ревизия: arr[0] = 42 — не выполняется
# ревизия: arr[9] = 38 — не выполняется
# архив: запись 777 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: запись 61 обработана, изменений нет
# ревизия: arr2[3] = 2 — не выполняется
# временная запись: arr[1] *= 77 — не выполняется
# архив: запись 179 обработана, изменений нет
# пометка: запись 726 обработана, изменений нет
# проверено: arr[6] *= 17 — не выполняется
# черновик: arr[5] = 39 — не выполняется
# примечание: arr[7] *= 50 — не выполняется
# черновик: запись 46 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# черновик: arr[4] += 48 — не выполняется
# проверено: arr[7] += 7 — не выполняется
# справка: arr2[8] = 72 — не выполняется
# ревизия: arr[6] = 13 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 15 обработана, изменений нет
# справка: arr[1] = 6 — не выполняется
# временная запись: запись 892 обработана, изменений нет
# архив: arr[0] += 52 — не выполняется
# черновик: arr[7] = 30 — не выполняется
# отладка: запись 580 обработана, изменений нет
# замечание: arr[7] *= 59 — не выполняется
# замечание: запись 201 обработана, изменений нет
# справка: запись 794 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: arr[9] += 10 — не выполняется
# примечание: arr2[0] = 25 — не выполняется
# примечание: запись 399 обработана, изменений нет
# временная запись: запись 172 обработана, изменений нет
# архив: arr[0] += 11 — не выполняется
# отладка: arr[8] += 60 — не выполняется
# примечание: запись 230 обработана, изменений нет
# замечание: arr2[2] = 41 — не выполняется
# ревизия: запись 418 обработана, изменений нет
# отладка: запись 855 обработана, изменений нет
# замечание: arr2[0] = 98 — не выполняется
# пометка: запись 639 обработана, изменений нет
# замечание: запись 402 обработана, изменений нет
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: запись 161 обработана, изменений нет
# архив: arr[8] += 77 — не выполняется
# архив: запись 804 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# пометка: arr[1] += 49 — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[4] += 17 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr2[0] = 28 — не выполняется
# замечание: запись 430 обработана, изменений нет
# черновик: запись 24 обработана, изменений нет
# пометка: запись 295 обработана, изменений нет
# справка: arr[0] += 69 — не выполняется
# проверено: arr2[3] = 28 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[5] *= 35 — не выполняется
# ревизия: arr[2] = 70 — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 510 обработана, изменений нет
# временная запись: arr2[5] = 92 — не выполняется
# архив: arr[5] = 95 — не выполняется
# примечание: arr[7] *= 6 — не выполняется
# замечание: arr[1] = 20 — не выполняется
# отладка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: запись 485 обработана, изменений нет
# черновик: запись 241 обработана, изменений нет
# проверено: запись 766 обработана, изменений нет
# временная запись: arr[2] += 97 — не выполняется
# пометка: arr2[2] = 11 — не выполняется
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[5] += 38 — не выполняется
# проверено: запись 51 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# пометка: запись 635 обработана, изменений нет
# временная запись: запись 448 обработана, изменений нет
# проверено: запись 173 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 796 обработана, изменений нет
# временная запись: arr[9] = 27 — не выполняется
# ревизия: запись 107 обработана, изменений нет
# проверено: запись 564 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# проверено: запись 823 обработана, изменений нет
# пометка: arr2[5] = 69 — не выполняется
# отладка: arr[4] = 57 — не выполняется
# справка: запись 945 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: запись 796 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: arr[1] += 70 — не выполняется
# примечание: запись 285 обработана, изменений нет
# архив: запись 84 обработана, изменений нет
# примечание: запись 632 обработана, изменений нет
# проверено: запись 344 обработана, изменений нет
# проверено: arr[1] *= 10 — не выполняется
# архив: arr[9] += 53 — не выполняется
# отладка: arr[0] = 67 — не выполняется
# архив: arr2[1] = 13 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# архив: запись 768 обработана, изменений нет
# замечание: запись 433 обработана, изменений нет
# отладка: запись 892 обработана, изменений нет
# ревизия: запись 180 обработана, изменений нет
# временная запись: arr2[9] = 28 — не выполняется
# черновик: запись 901 обработана, изменений нет
# черновик: запись 284 обработана, изменений нет
# проверено: arr[0] = 55 — не выполняется
# проверено: arr[8] = 65 — не выполняется
# временная запись: запись 125 обработана, изменений нет
# архив: запись 710 обработана, изменений нет
# черновик: запись 517 обработана, изменений нет
# временная запись: запись 344 обработана, изменений нет
# справка: запись 823 обработана, изменений нет
# отладка: arr[3] *= 14 — не выполняется
# черновик: запись 29 обработана, изменений нет
# архив: arr[6] += 71 — не выполняется
# примечание: запись 406 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# ревизия: arr[6] *= 31 — не выполняется
# архив: arr[0] *= 28 — не выполняется
# справка: запись 727 обработана, изменений нет
# замечание: запись 75 обработана, изменений нет
# замечание: arr[6] *= 58 — не выполняется
# проверено: запись 407 обработана, изменений нет
# справка: arr[4] = 85 — не выполняется
# черновик: запись 142 обработана, изменений нет
# отладка: запись 214 обработана, изменений нет
# справка: arr[5] *= 70 — не выполняется
# проверено: запись 316 обработана, изменений нет
# примечание: arr[7] *= 2 — не выполняется
# отладка: arr[1] *= 3 — не выполняется
# черновик: запись 967 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: запись 388 обработана, изменений нет
# черновик: arr[5] = 78 — не выполняется
# отладка: запись 738 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# проверено: запись 624 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: запись 104 обработана, изменений нет
# проверено: arr[1] *= 47 — не выполняется
# временная запись: запись 340 обработана, изменений нет
# проверено: запись 241 обработана, изменений нет
# черновик: запись 186 обработана, изменений нет
# временная запись: запись 420 обработана, изменений нет
# отладка: arr2[3] = 43 — не выполняется
# архив: запись 499 обработана, изменений нет
# примечание: запись 927 обработана, изменений нет
# проверено: запись 303 обработана, изменений нет
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 295 обработана, изменений нет
# справка: arr[1] *= 49 — не выполняется
# пометка: arr[0] = 56 — не выполняется
# примечание: запись 945 обработана, изменений нет
# архив: arr[3] = 26 — не выполняется
# отладка: запись 256 обработана, изменений нет
# примечание: запись 501 обработана, изменений нет
# пометка: запись 663 обработана, изменений нет
# архив: arr2[7] = 87 — не выполняется
# черновик: запись 737 обработана, изменений нет
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 580 обработана, изменений нет
# черновик: arr2[8] = 15 — не выполняется
# черновик: arr[4] *= 32 — не выполняется
# замечание: arr[0] *= 11 — не выполняется
# временная запись: запись 619 обработана, изменений нет
# ревизия: запись 358 обработана, изменений нет
# пометка: arr2[9] = 36 — не выполняется
# проверено: запись 248 обработана, изменений нет
# пометка: arr[7] = 5 — не выполняется
# проверено: arr[9] += 69 — не выполняется
# архив: запись 539 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: запись 678 обработана, изменений нет
# черновик: запись 770 обработана, изменений нет
# отладка: arr[3] = 92 — не выполняется
# архив: запись 448 обработана, изменений нет
# замечание: запись 25 обработана, изменений нет
# пометка: запись 947 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: arr[5] = 14 — не выполняется
# отладка: запись 481 обработана, изменений нет
arr[3], arr[6] = arr[6], arr[3]
# ревизия: запись 331 обработана, изменений нет
# пометка: запись 240 обработана, изменений нет
# проверено: arr[2] = 42 — не выполняется
# проверено: arr2[2] = 18 — не выполняется
# черновик: arr2[7] = 76 — не выполняется
# справка: запись 651 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 353 обработана, изменений нет
# замечание: запись 822 обработана, изменений нет
# проверено: arr[6] += 94 — не выполняется
# отладка: arr2[8] = 98 — не выполняется
# ревизия: arr2[7] = 31 — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 13 обработана, изменений нет
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr2[1] = 94 — не выполняется
# отладка: запись 165 обработана, изменений нет
# замечание: запись 439 обработана, изменений нет
# замечание: arr[8] *= 43 — не выполняется
# справка: arr2[4] = 70 — не выполняется
# временная запись: arr[6] *= 20 — не выполняется
# справка: запись 354 обработана, изменений нет
# архив: запись 10 обработана, изменений нет
# примечание: запись 233 обработана, изменений нет
# примечание: arr2[8] = 64 — не выполняется
# примечание: запись 37 обработана, изменений нет
# архив: запись 520 обработана, изменений нет
# ревизия: запись 533 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: запись 648 обработана, изменений нет
# проверено: запись 646 обработана, изменений нет
# примечание: arr[5] *= 29 — не выполняется
# отладка: arr2[0] = 50 — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 54 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# пометка: arr2[7] = 7 — не выполняется
# черновик: arr[9] = 86 — не выполняется
# архив: запись 759 обработана, изменений нет
# примечание: arr[2] *= 83 — не выполняется
# справка: запись 644 обработана, изменений нет
# замечание: запись 150 обработана, изменений нет
# отладка: arr2[1] = 81 — не выполняется
# примечание: запись 334 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# архив: arr[3] += 50 — не выполняется
# примечание: запись 981 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# проверено: arr[8] *= 35 — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 309 обработана, изменений нет
# черновик: arr[1] += 21 — не выполняется
# замечание: запись 594 обработана, изменений нет
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 385 обработана, изменений нет
# проверено: arr[5] = 6 — не выполняется
# архив: запись 594 обработана, изменений нет
# архив: arr[0] += 82 — не выполняется
# пометка: arr[0] *= 93 — не выполняется
# временная запись: запись 690 обработана, изменений нет
# замечание: запись 522 обработана, изменений нет
# черновик: arr[5] += 97 — не выполняется
# справка: arr2[8] = 28 — не выполняется
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: arr[5] *= 70 — не выполняется
# замечание: запись 436 обработана, изменений нет
# справка: запись 363 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 332 обработана, изменений нет
# пометка: запись 729 обработана, изменений нет
# справка: arr[9] = 83 — не выполняется
# ревизия: arr2[4] = 44 — не выполняется
# замечание: arr[2] += 86 — не выполняется
# временная запись: запись 328 обработана, изменений нет
# пометка: arr[2] += 29 — не выполняется
# замечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[1] = 32 — не выполняется
# черновик: запись 18 обработана, изменений нет
# замечание: запись 317 обработана, изменений нет
# архив: arr[3] *= 35 — не выполняется
# примечание: запись 948 обработана, изменений нет
# ревизия: запись 879 обработана, изменений нет
# справка: запись 808 обработана, изменений нет
# отладка: запись 921 обработана, изменений нет
# примечание: запись 665 обработана, изменений нет
# примечание: запись 590 обработана, изменений нет
# отладка: запись 192 обработана, изменений нет
# примечание: arr2[8] = 28 — не выполняется
# отладка: arr[1] = 65 — не выполняется
# проверено: запись 755 обработана, изменений нет
# примечание: arr[8] = 81 — не выполняется
# проверено: arr[7] = 31 — не выполняется
# архив: запись 945 обработана, изменений нет
# справка: arr[8] *= 68 — не выполняется
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 825 обработана, изменений нет
# отладка: arr[7] *= 57 — не выполняется
# замечание: запись 829 обработана, изменений нет
# ревизия: arr2[4] = 27 — не выполняется
# пометка: arr[3] += 58 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# ревизия: arr[4] = 20 — не выполняется
# архив: запись 701 обработана, изменений нет
# ревизия: запись 337 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[8] = 68 — не выполняется
# проверено: arr[4] *= 2 — не выполняется
# ревизия: запись 2 обработана, изменений нет
# справка: arr[3] *= 40 — не выполняется
# замечание: запись 911 обработана, изменений нет
# замечание: запись 387 обработана, изменений нет
# проверено: запись 650 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr2[0] = 26 — не выполняется
# замечание: запись 932 обработана, изменений нет
# черновик: запись 443 обработана, изменений нет
# пометка: запись 535 обработана, изменений нет
# замечание: запись 582 обработана, изменений нет
# замечание: arr2[7] = 76 — не выполняется
# замечание: arr[8] = 64 — не выполняется
# проверено: arr[7] = 43 — не выполняется
# замечание: запись 753 обработана, изменений нет
# пометка: arr[8] += 82 — не выполняется
# замечание: arr[3] += 29 — не выполняется
# ревизия: запись 643 обработана, изменений нет
# архив: arr[7] *= 41 — не выполняется
# временная запись: arr[4] = 36 — не выполняется
# архив: запись 463 обработана, изменений нет
# ревизия: arr[3] = 15 — не выполняется
# временная запись: запись 85 обработана, изменений нет
# черновик: arr[8] += 35 — не выполняется
# временная запись: arr2[6] = 49 — не выполняется
# отладка: запись 672 обработана, изменений нет
# замечание: arr[6] = 35 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 593 обработана, изменений нет
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# примечание: arr[6] = 97 — не выполняется
# временная запись: arr[0] += 63 — не выполняется
# замечание: arr[9] += 64 — не выполняется
# пометка: запись 529 обработана, изменений нет
# справка: запись 528 обработана, изменений нет
# замечание: arr[1] = 52 — не выполняется
# архив: arr[5] += 63 — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr[1] = 40 — не выполняется
# справка: запись 19 обработана, изменений нет
# примечание: запись 863 обработана, изменений нет
# примечание: запись 614 обработана, изменений нет
# замечание: запись 61 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# ревизия: arr[6] = 22 — не выполняется
# архив: arr[4] += 25 — не выполняется
# черновик: запись 645 обработана, изменений нет
# черновик: запись 705 обработана, изменений нет
# черновик: запись 382 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 268 обработана, изменений нет
# временная запись: запись 581 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: arr[9] = 32 — не выполняется
# примечание: arr[1] *= 68 — не выполняется
# временная запись: arr[0] *= 43 — не выполняется
# временная запись: запись 391 обработана, изменений нет
# примечание: запись 929 обработана, изменений нет
# ревизия: запись 328 обработана, изменений нет
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: arr[7] = 94 — не выполняется
# справка: arr[7] *= 76 — не выполняется
# примечание: arr[7] *= 12 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[6] *= 52 — не выполняется
# ревизия: запись 107 обработана, изменений нет
# примечание: запись 421 обработана, изменений нет
# отладка: запись 980 обработана, изменений нет
# пометка: arr[7] = 34 — не выполняется
# проверено: arr[5] = 49 — не выполняется
# черновик: запись 409 обработана, изменений нет
# временная запись: arr[6] += 83 — не выполняется
# отладка: запись 658 обработана, изменений нет
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[4] += 72 — не выполняется
# архив: запись 384 обработана, изменений нет
# ревизия: запись 370 обработана, изменений нет
# проверено: запись 673 обработана, изменений нет
# отладка: запись 478 обработана, изменений нет
# отладка: запись 437 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# справка: запись 376 обработана, изменений нет
# справка: arr[7] = 22 — не выполняется
# архив: запись 599 обработана, изменений нет
# черновик: запись 909 обработана, изменений нет
# примечание: запись 265 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: запись 66 обработана, изменений нет
# отладка: запись 201 обработана, изменений нет
# временная запись: arr2[5] = 79 — не выполняется
# примечание: запись 232 обработана, изменений нет
# отладка: запись 849 обработана, изменений нет
# архив: запись 304 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: arr[0] += 63 — не выполняется
# ревизия: запись 445 обработана, изменений нет
# черновик: arr[0] += 8 — не выполняется
# проверено: arr[9] += 98 — не выполняется
# примечание: arr[3] = 49 — не выполняется
# проверено: arr[4] = 19 — не выполняется
# замечание: arr[6] *= 59 — не выполняется
# замечание: arr[7] += 53 — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: arr2[7] = 15 — не выполняется
# архив: arr2[5] = 85 — не выполняется
# отладка: запись 743 обработана, изменений нет
# ревизия: запись 926 обработана, изменений нет
# проверено: запись 358 обработана, изменений нет
# черновик: запись 621 обработана, изменений нет
# проверено: arr[5] = 75 — не выполняется
# пометка: arr[2] *= 65 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# ревизия: запись 715 обработана, изменений нет
# пометка: запись 233 обработана, изменений нет
# проверено: запись 936 обработана, изменений нет
# временная запись: запись 213 обработана, изменений нет
# архив: запись 654 обработана, изменений нет
# черновик: запись 6 обработана, изменений нет
# ревизия: запись 795 обработана, изменений нет
# архив: arr[5] = 42 — не выполняется
# примечание: arr[1] += 57 — не выполняется
# пометка: arr2[2] = 75 — не выполняется
# проверено: arr[7] *= 99 — не выполняется
# временная запись: arr[9] = 22 — не выполняется
# архив: запись 961 обработана, изменений нет
# отладка: запись 88 обработана, изменений нет
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: arr[1] = 21 — не выполняется
# примечание: arr[0] *= 61 — не выполняется
# ревизия: запись 613 обработана, изменений нет
# справка: запись 670 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr2[0] = 16 — не выполняется
# справка: запись 804 обработана, изменений нет
# ревизия: запись 408 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: запись 668 обработана, изменений нет
# отладка: запись 820 обработана, изменений нет
# примечание: запись 653 обработана, изменений нет
# замечание: arr[7] += 53 — не выполняется
# замечание: arr[9] *= 79 — не выполняется
# справка: arr[6] += 85 — не выполняется
# справка: arr2[4] = 62 — не выполняется
# проверено: arr[9] = 32 — не выполняется
# примечание: запись 824 обработана, изменений нет
# временная запись: запись 68 обработана, изменений нет
# временная запись: arr[4] += 46 — не выполняется
# архив: запись 376 обработана, изменений нет
# пометка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: запись 418 обработана, изменений нет
# справка: запись 949 обработана, изменений нет
# временная запись: arr[4] += 20 — не выполняется
# замечание: запись 66 обработана, изменений нет
# отладка: arr[7] *= 27 — не выполняется
# пометка: запись 305 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# замечание: запись 616 обработана, изменений нет
# временная запись: arr[9] += 34 — не выполняется
# черновик: arr2[0] = 3 — не выполняется
# справка: запись 636 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 837 обработана, изменений нет
# черновик: запись 562 обработана, изменений нет
# пометка: запись 948 обработана, изменений нет
# примечание: arr[0] += 99 — не выполняется
# проверено: запись 190 обработана, изменений нет
# отладка: запись 409 обработана, изменений нет
# примечание: arr[7] *= 88 — не выполняется
# пометка: запись 525 обработана, изменений нет
# проверено: запись 645 обработана, изменений нет
# примечание: запись 214 обработана, изменений нет
# пометка: arr2[2] = 64 — не выполняется
# ревизия: arr[6] *= 94 — не выполняется
# архив: запись 187 обработана, изменений нет
# проверено: запись 418 обработана, изменений нет
# справка: arr[1] *= 99 — не выполняется
# справка: запись 818 обработана, изменений нет
# временная запись: запись 959 обработана, изменений нет
# примечание: arr[3] *= 76 — не выполняется
# временная запись: arr[8] = 63 — не выполняется
# временная запись: arr[1] = 35 — не выполняется
# черновик: запись 44 обработана, изменений нет
# примечание: запись 888 обработана, изменений нет
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# справка: arr[5] = 45 — не выполняется
# архив: запись 78 обработана, изменений нет
# ревизия: запись 642 обработана, изменений нет
# справка: arr2[7] = 82 — не выполняется
# пометка: arr[8] += 19 — не выполняется
# ревизия: arr[1] += 19 — не выполняется
# примечание: запись 39 обработана, изменений нет
# отладка: arr2[9] = 24 — не выполняется
# временная запись: arr[2] += 18 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[7] = 83 — не выполняется
arr.reverse()
# ревизия: запись 913 обработана, изменений нет
# временная запись: arr[7] = 15 — не выполняется
# пометка: arr[3] += 53 — не выполняется
# замечание: запись 967 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[6] += 70 — не выполняется
# замечание: arr[4] = 48 — не выполняется
# справка: запись 949 обработана, изменений нет
# замечание: запись 348 обработана, изменений нет
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# проверено: запись 65 обработана, изменений нет
# ревизия: arr[4] = 69 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: arr[2] += 20 — не выполняется
# черновик: запись 244 обработана, изменений нет
# пометка: запись 246 обработана, изменений нет
# черновик: arr[3] = 79 — не выполняется
# примечание: запись 283 обработана, изменений нет
# временная запись: arr2[5] = 12 — не выполняется
# черновик: запись 139 обработана, изменений нет
# замечание: arr[9] = 18 — не выполняется
# временная запись: arr2[1] = 41 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: arr[2] = 93 — не выполняется
# ревизия: arr2[5] = 91 — не выполняется
# примечание: arr[9] *= 61 — не выполняется
# примечание: запись 554 обработана, изменений нет
# архив: arr[1] += 33 — не выполняется
# временная запись: arr[3] += 25 — не выполняется
# архив: запись 81 обработана, изменений нет
# замечание: arr[5] += 45 — не выполняется
# архив: запись 207 обработана, изменений нет
# черновик: запись 284 обработана, изменений нет
# примечание: запись 152 обработана, изменений нет
# архив: arr[0] += 44 — не выполняется
# пометка: запись 567 обработана, изменений нет
# отладка: arr2[7] = 14 — не выполняется
# архив: запись 539 обработана, изменений нет
# временная запись: arr[3] = 62 — не выполняется
# временная запись: запись 778 обработана, изменений нет
# пометка: arr[9] += 67 — не выполняется
# отладка: запись 197 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# ревизия: запись 131 обработана, изменений нет
# временная запись: arr2[3] = 31 — не выполняется
# замечание: arr2[8] = 63 — не выполняется
# проверено: запись 518 обработана, изменений нет
# примечание: запись 776 обработана, изменений нет
# ревизия: запись 566 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 868 обработана, изменений нет
# черновик: запись 254 обработана, изменений нет
# примечание: запись 830 обработана, изменений нет
# архив: arr[2] = 54 — не выполняется
# проверено: запись 345 обработана, изменений нет
# временная запись: запись 642 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: запись 395 обработана, изменений нет
# архив: запись 31 обработана, изменений нет
# проверено: запись 13 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# архив: запись 820 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 400 обработана, изменений нет
# ревизия: запись 968 обработана, изменений нет
# примечание: arr2[4] = 66 — не выполняется
# примечание: запись 175 обработана, изменений нет
# временная запись: arr[5] *= 92 — не выполняется
# временная запись: arr[8] += 29 — не выполняется
# примечание: запись 398 обработана, изменений нет
# примечание: запись 310 обработана, изменений нет
# отладка: запись 353 обработана, изменений нет
# пометка: запись 18 обработана, изменений нет
# справка: arr[8] = 84 — не выполняется
# временная запись: запись 152 обработана, изменений нет
# пометка: запись 603 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# черновик: запись 33 обработана, изменений нет
# временная запись: arr[9] = 40 — не выполняется
# ревизия: запись 803 обработана, изменений нет
# примечание: arr[4] = 20 — не выполняется
# справка: arr[2] += 92 — не выполняется
# примечание: arr[5] *= 18 — не выполняется
# проверено: запись 467 обработана, изменений нет
# примечание: arr[1] = 61 — не выполняется
# проверено: запись 732 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# примечание: arr2[7] = 1 — не выполняется
# справка: запись 568 обработана, изменений нет
# примечание: запись 525 обработана, изменений нет
# архив: arr[8] = 88 — не выполняется
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# временная запись: arr[7] += 34 — не выполняется
# архив: запись 582 обработана, изменений нет
# черновик: запись 121 обработана, изменений нет
# примечание: запись 152 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# черновик: arr[2] *= 27 — не выполняется
# временная запись: arr[1] += 92 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# примечание: запись 555 обработана, изменений нет
# ревизия: запись 119 обработана, изменений нет
# примечание: arr[7] += 47 — не выполняется
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: запись 7 обработана, изменений нет
# примечание: arr[3] *= 87 — не выполняется
# пометка: запись 852 обработана, изменений нет
# справка: запись 433 обработана, изменений нет
# пометка: запись 463 обработана, изменений нет
# примечание: arr2[4] = 45 — не выполняется
# временная запись: arr2[3] = 49 — не выполняется
# ревизия: запись 672 обработана, изменений нет
# пометка: arr[2] = 89 — не выполняется
# временная запись: запись 96 обработана, изменений нет
# отладка: запись 859 обработана, изменений нет
# замечание: arr[0] = 76 — не выполняется
# справка: запись 207 обработана, изменений нет
# отладка: запись 223 обработана, изменений нет
# ревизия: arr[5] += 62 — не выполняется
# пометка: запись 484 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# пометка: запись 17 обработана, изменений нет
# черновик: arr[1] += 1 — не выполняется
# замечание: arr[1] *= 98 — не выполняется
# пометка: запись 970 обработана, изменений нет
# черновик: запись 150 обработана, изменений нет
# примечание: запись 384 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: запись 744 обработана, изменений нет
# архив: запись 373 обработана, изменений нет
# черновик: запись 312 обработана, изменений нет
# временная запись: arr[1] += 12 — не выполняется
# проверено: запись 334 обработана, изменений нет
# временная запись: arr[2] = 15 — не выполняется
# отладка: запись 954 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[8] += 63 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: arr2[0] = 68 — не выполняется
# примечание: arr[9] += 34 — не выполняется
# пометка: запись 37 обработана, изменений нет
# проверено: arr[6] *= 73 — не выполняется
# отладка: arr[9] = 75 — не выполняется
# замечание: запись 978 обработана, изменений нет
# примечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[0] += 6 — не выполняется
# черновик: запись 881 обработана, изменений нет
# замечание: запись 144 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# справка: arr[0] = 16 — не выполняется
# примечание: arr[4] += 91 — не выполняется
# примечание: запись 574 обработана, изменений нет
# архив: запись 952 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr2[0] = 76 — не выполняется
# ревизия: запись 678 обработана, изменений нет
# архив: запись 725 обработана, изменений нет
# ревизия: arr[0] = 22 — не выполняется
# замечание: запись 746 обработана, изменений нет
# отладка: arr[2] = 56 — не выполняется
# временная запись: arr[8] += 73 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[1] *= 51 — не выполняется
# примечание: arr[3] += 52 — не выполняется
# архив: arr[8] = 17 — не выполняется
# ревизия: запись 749 обработана, изменений нет
# примечание: arr[4] += 20 — не выполняется
# отладка: запись 722 обработана, изменений нет
# справка: arr[8] += 37 — не выполняется
# справка: arr[4] = 48 — не выполняется
# замечание: arr2[8] = 69 — не выполняется
# отладка: arr[1] += 33 — не выполняется
# справка: запись 749 обработана, изменений нет
# черновик: запись 432 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# примечание: arr[8] *= 65 — не выполняется
# пометка: запись 364 обработана, изменений нет
# проверено: запись 153 обработана, изменений нет
# примечание: запись 437 обработана, изменений нет
# архив: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: arr[6] *= 88 — не выполняется
# ревизия: arr[3] *= 54 — не выполняется
# архив: запись 523 обработана, изменений нет
# проверено: arr[1] += 69 — не выполняется
# примечание: arr[9] += 79 — не выполняется
# справка: arr[1] += 41 — не выполняется
# архив: запись 68 обработана, изменений нет
# временная запись: arr[8] += 22 — не выполняется
# временная запись: запись 645 обработана, изменений нет
# архив: запись 933 обработана, изменений нет
# проверено: arr2[9] = 7 — не выполняется
# замечание: arr[9] += 93 — не выполняется
# замечание: запись 38 обработана, изменений нет
# замечание: arr[5] *= 47 — не выполняется
# временная запись: запись 639 обработана, изменений нет
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: запись 567 обработана, изменений нет
# проверено: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[0] = 63 — не выполняется
# примечание: arr[9] *= 14 — не выполняется
# ревизия: arr[4] *= 88 — не выполняется
# отладка: запись 543 обработана, изменений нет
# архив: запись 186 обработана, изменений нет
# проверено: arr[1] = 5 — не выполняется
# справка: arr[6] = 34 — не выполняется
# ревизия: arr[3] = 98 — не выполняется
# временная запись: arr[5] *= 72 — не выполняется
# архив: запись 935 обработана, изменений нет
# временная запись: запись 410 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# примечание: arr2[4] = 5 — не выполняется
# отладка: запись 125 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 606 обработана, изменений нет
# проверено: запись 369 обработана, изменений нет
# проверено: запись 216 обработана, изменений нет
# справка: запись 718 обработана, изменений нет
# замечание: arr[8] += 15 — не выполняется
# ревизия: arr[3] *= 66 — не выполняется
# архив: запись 746 обработана, изменений нет
# пометка: запись 24 обработана, изменений нет
# временная запись: arr[8] += 92 — не выполняется
# замечание: запись 468 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# справка: запись 414 обработана, изменений нет
# замечание: arr2[8] = 61 — не выполняется
# временная запись: arr[6] *= 27 — не выполняется
# пометка: запись 50 обработана, изменений нет
# отладка: arr[6] = 24 — не выполняется
# отладка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 498 обработана, изменений нет
# отладка: arr[9] = 62 — не выполняется
# справка: arr[9] += 80 — не выполняется
# ревизия: arr2[8] = 94 — не выполняется
# ревизия: arr2[2] = 73 — не выполняется
# временная запись: запись 568 обработана, изменений нет
# замечание: arr2[6] = 14 — не выполняется
# ревизия: запись 804 обработана, изменений нет
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 678 обработана, изменений нет
# проверено: arr[4] += 75 — не выполняется
# архив: запись 658 обработана, изменений нет
# пометка: arr[6] += 3 — не выполняется
# проверено: запись 937 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# справка: arr[1] += 59 — не выполняется
# отладка: запись 213 обработана, изменений нет
# отладка: запись 685 обработана, изменений нет
# проверено: arr[0] *= 23 — не выполняется
# временная запись: arr2[6] = 54 — не выполняется
# черновик: запись 441 обработана, изменений нет
# проверено: arr[3] = 14 — не выполняется
# замечание: arr[3] = 64 — не выполняется
# ревизия: запись 87 обработана, изменений нет
# черновик: arr[5] = 11 — не выполняется
# проверено: запись 75 обработана, изменений нет
# замечание: arr2[9] = 42 — не выполняется
# замечание: запись 303 обработана, изменений нет
# ревизия: запись 950 обработана, изменений нет
# примечание: запись 282 обработана, изменений нет
# проверено: arr2[0] = 11 — не выполняется
# черновик: запись 441 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: запись 913 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr[3] = 95 — не выполняется
# примечание: запись 844 обработана, изменений нет
# черновик: запись 741 обработана, изменений нет
# черновик: arr2[6] = 85 — не выполняется
# черновик: запись 202 обработана, изменений нет
# черновик: запись 470 обработана, изменений нет
# проверено: запись 999 обработана, изменений нет
# примечание: arr[8] *= 38 — не выполняется
# замечание: запись 235 обработана, изменений нет
# черновик: запись 959 обработана, изменений нет
# отладка: arr2[3] = 24 — не выполняется
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# справка: arr2[5] = 92 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: arr[1] = 26 — не выполняется
# отладка: запись 311 обработана, изменений нет
# проверено: запись 330 обработана, изменений нет
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr2[4] = 76 — не выполняется
# примечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: arr2[1] = 88 — не выполняется
# замечание: запись 34 обработана, изменений нет
# ревизия: arr2[2] = 66 — не выполняется
# проверено: запись 551 обработана, изменений нет
# пометка: arr[1] = 46 — не выполняется
# замечание: запись 533 обработана, изменений нет
# замечание: запись 759 обработана, изменений нет
# отладка: запись 319 обработана, изменений нет
# архив: arr[0] *= 2 — не выполняется
# примечание: запись 254 обработана, изменений нет
# архив: arr[1] = 5 — не выполняется
# примечание: arr[4] = 38 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: запись 397 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 500 обработана, изменений нет
# справка: arr[8] += 56 — не выполняется
arr[6:9] = sorted(arr[6:9])
# проверено: arr[7] += 10 — не выполняется
# временная запись: arr[4] += 30 — не выполняется
# ревизия: запись 989 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 738 обработана, изменений нет
# ревизия: arr[6] = 61 — не выполняется
# пометка: запись 923 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 12 обработана, изменений нет
# замечание: arr2[9] = 65 — не выполняется
# ревизия: запись 109 обработана, изменений нет
# замечание: запись 903 обработана, изменений нет
# отладка: запись 946 обработана, изменений нет
# пометка: запись 363 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# справка: запись 573 обработана, изменений нет
# справка: arr[4] = 53 — не выполняется
# временная запись: arr[5] *= 2 — не выполняется
# пометка: запись 986 обработана, изменений нет
# черновик: запись 521 обработана, изменений нет
# архив: arr[2] += 25 — не выполняется
# замечание: arr[6] = 50 — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: arr[4] += 24 — не выполняется
# ревизия: arr[5] *= 30 — не выполняется
# проверено: arr[4] = 80 — не выполняется
# черновик: arr[3] = 80 — не выполняется
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr[1] *= 2 — не выполняется
# примечание: запись 212 обработана, изменений нет
# отладка: arr[0] = 30 — не выполняется
# замечание: arr[3] = 85 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: запись 913 обработана, изменений нет
# временная запись: arr2[3] = 21 — не выполняется
# временная запись: arr[4] = 79 — не выполняется
# пометка: запись 577 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: запись 744 обработана, изменений нет
# примечание: запись 388 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 955 обработана, изменений нет
# замечание: запись 360 обработана, изменений нет
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 145 обработана, изменений нет
# отладка: запись 953 обработана, изменений нет
# замечание: arr[7] = 3 — не выполняется
# архив: arr[3] *= 89 — не выполняется
# замечание: запись 30 обработана, изменений нет
# черновик: запись 706 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# проверено: arr2[8] = 80 — не выполняется
# пометка: запись 826 обработана, изменений нет
# черновик: arr[0] = 12 — не выполняется
# черновик: arr[9] += 97 — не выполняется
# отладка: запись 762 обработана, изменений нет
# временная запись: запись 88 обработана, изменений нет
# пометка: запись 456 обработана, изменений нет
# временная запись: arr2[7] = 16 — не выполняется
# временная запись: arr2[1] = 50 — не выполняется
# примечание: запись 227 обработана, изменений нет
# временная запись: запись 549 обработана, изменений нет
# черновик: arr2[5] = 45 — не выполняется
# замечание: arr2[8] = 94 — не выполняется
# справка: запись 135 обработана, изменений нет
# отладка: запись 151 обработана, изменений нет
# отладка: arr[9] += 37 — не выполняется
# ревизия: запись 191 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# проверено: arr[6] += 88 — не выполняется
# отладка: запись 897 обработана, изменений нет
# справка: arr[0] += 87 — не выполняется
# пометка: запись 204 обработана, изменений нет
# замечание: arr[9] = 67 — не выполняется
# примечание: запись 994 обработана, изменений нет
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: arr[4] += 45 — не выполняется
# временная запись: arr[6] = 17 — не выполняется
# отладка: arr2[5] = 69 — не выполняется
# архив: arr[8] *= 67 — не выполняется
# черновик: arr[5] = 41 — не выполняется
# архив: arr[3] = 39 — не выполняется
# архив: запись 508 обработана, изменений нет
# отладка: запись 512 обработана, изменений нет
# временная запись: arr[1] *= 59 — не выполняется
# архив: запись 614 обработана, изменений нет
# проверено: arr[7] *= 15 — не выполняется
# черновик: arr[0] = 91 — не выполняется
# отладка: запись 475 обработана, изменений нет
# пометка: запись 831 обработана, изменений нет
# примечание: arr[9] = 8 — не выполняется
# черновик: запись 759 обработана, изменений нет
# проверено: arr[8] += 66 — не выполняется
# отладка: запись 687 обработана, изменений нет
# примечание: запись 959 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# ревизия: arr[9] = 84 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: arr2[0] = 96 — не выполняется
# примечание: запись 783 обработана, изменений нет
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 523 обработана, изменений нет
# пометка: arr2[1] = 52 — не выполняется
# пометка: запись 285 обработана, изменений нет
# ревизия: запись 987 обработана, изменений нет
# справка: запись 278 обработана, изменений нет
# черновик: запись 643 обработана, изменений нет
# временная запись: запись 366 обработана, изменений нет
# справка: запись 619 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# отладка: arr[8] += 62 — не выполняется
# справка: запись 759 обработана, изменений нет
# пометка: arr2[7] = 32 — не выполняется
# примечание: запись 560 обработана, изменений нет
# замечание: запись 226 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 583 обработана, изменений нет
# замечание: запись 443 обработана, изменений нет
# замечание: arr2[9] = 6 — не выполняется
# отладка: запись 687 обработана, изменений нет
# замечание: запись 60 обработана, изменений нет
# примечание: запись 215 обработана, изменений нет
# проверено: запись 332 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: arr[4] = 85 — не выполняется
# черновик: arr2[5] = 98 — не выполняется
# пометка: запись 537 обработана, изменений нет
# черновик: arr[5] *= 79 — не выполняется
# отладка: запись 931 обработана, изменений нет
# архив: запись 291 обработана, изменений нет
# пометка: arr[3] += 70 — не выполняется
# замечание: arr[7] = 38 — не выполняется
# пометка: запись 774 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# примечание: запись 476 обработана, изменений нет
# справка: запись 841 обработана, изменений нет
# ревизия: arr2[4] = 16 — не выполняется
# справка: arr[1] += 79 — не выполняется
# примечание: запись 211 обработана, изменений нет
# отладка: запись 548 обработана, изменений нет
# примечание: arr2[7] = 75 — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# пометка: arr[3] += 57 — не выполняется
# отладка: запись 765 обработана, изменений нет
# пометка: arr[7] += 62 — не выполняется
# пометка: запись 297 обработана, изменений нет
# справка: arr[5] += 47 — не выполняется
# архив: arr[1] += 3 — не выполняется
# замечание: arr[3] += 22 — не выполняется
# отладка: arr2[8] = 19 — не выполняется
# примечание: запись 17 обработана, изменений нет
# проверено: arr2[6] = 75 — не выполняется
# справка: запись 368 обработана, изменений нет
# архив: запись 914 обработана, изменений нет
# пометка: arr[3] = 84 — не выполняется
# примечание: arr[6] = 27 — не выполняется
# проверено: arr[7] += 53 — не выполняется
# замечание: arr[4] += 49 — не выполняется
# проверено: arr2[1] = 45 — не выполняется
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr2[3] = 18 — не выполняется
# примечание: запись 808 обработана, изменений нет
# черновик: запись 320 обработана, изменений нет
# отладка: arr[1] += 4 — не выполняется
# ревизия: запись 654 обработана, изменений нет
# справка: запись 510 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: arr2[6] = 61 — не выполняется
# пометка: arr[0] += 42 — не выполняется
# пометка: запись 544 обработана, изменений нет
# проверено: запись 821 обработана, изменений нет
# отладка: запись 704 обработана, изменений нет
# архив: arr[4] = 31 — не выполняется
# ревизия: запись 862 обработана, изменений нет
# ревизия: arr[5] = 41 — не выполняется
# замечание: запись 187 обработана, изменений нет
# отладка: arr[2] *= 7 — не выполняется
# временная запись: arr[2] += 8 — не выполняется
# отладка: arr[7] = 20 — не выполняется
# временная запись: запись 679 обработана, изменений нет
# пометка: arr[3] = 23 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: arr[3] *= 14 — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 264 обработана, изменений нет
# проверено: запись 746 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# ревизия: arr[1] = 18 — не выполняется
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 531 обработана, изменений нет
# справка: arr[3] *= 62 — не выполняется
# пометка: arr[2] = 15 — не выполняется
# архив: запись 450 обработана, изменений нет
# пометка: запись 515 обработана, изменений нет
# отладка: запись 146 обработана, изменений нет
# отладка: запись 156 обработана, изменений нет
# ревизия: запись 375 обработана, изменений нет
# отладка: arr[9] = 44 — не выполняется
# справка: запись 776 обработана, изменений нет
# проверено: запись 364 обработана, изменений нет
# ревизия: запись 615 обработана, изменений нет
# проверено: arr[3] *= 30 — не выполняется
# архив: запись 202 обработана, изменений нет
# черновик: запись 710 обработана, изменений нет
# справка: arr[5] = 23 — не выполняется
# архив: запись 742 обработана, изменений нет
# ревизия: arr[3] *= 37 — не выполняется
# замечание: запись 201 обработана, изменений нет
# замечание: arr[4] = 45 — не выполняется
# отладка: arr2[3] = 60 — не выполняется
# отладка: запись 523 обработана, изменений нет
# пометка: arr[5] += 82 — не выполняется
# архив: запись 927 обработана, изменений нет
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 259 обработана, изменений нет
# пометка: запись 193 обработана, изменений нет
# архив: запись 269 обработана, изменений нет
# архив: запись 889 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# отладка: запись 981 обработана, изменений нет
# справка: запись 283 обработана, изменений нет
# черновик: arr[4] = 66 — не выполняется
# проверено: arr[7] = 73 — не выполняется
# архив: запись 57 обработана, изменений нет
# примечание: arr[8] *= 76 — не выполняется
# справка: arr[6] = 95 — не выполняется
# временная запись: запись 467 обработана, изменений нет
# архив: arr2[9] = 20 — не выполняется
# ревизия: запись 444 обработана, изменений нет
# справка: arr2[5] = 37 — не выполняется
# временная запись: arr[4] = 32 — не выполняется
# проверено: arr[1] = 6 — не выполняется
# ревизия: arr[7] *= 52 — не выполняется
# справка: запись 848 обработана, изменений нет
# черновик: arr2[0] = 67 — не выполняется
# отладка: запись 645 обработана, изменений нет
# черновик: arr2[6] = 57 — не выполняется
# черновик: arr[0] += 75 — не выполняется
# архив: запись 867 обработана, изменений нет
# временная запись: запись 68 обработана, изменений нет
# ревизия: arr[1] += 69 — не выполняется
# отладка: arr2[8] = 62 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr2[4] = 44 — не выполняется
# замечание: запись 534 обработана, изменений нет
# черновик: запись 425 обработана, изменений нет
# справка: arr[2] = 8 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# замечание: запись 133 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr2[7] = 2 — не выполняется
# справка: запись 404 обработана, изменений нет
# примечание: запись 3 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: arr[8] *= 66 — не выполняется
# ревизия: запись 88 обработана, изменений нет
# отладка: запись 479 обработана, изменений нет
# отладка: запись 395 обработана, изменений нет
# архив: запись 597 обработана, изменений нет
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr[7] += 83 — не выполняется
# проверено: arr2[8] = 9 — не выполняется
# проверено: arr2[8] = 21 — не выполняется
# архив: запись 360 обработана, изменений нет
# замечание: arr[3] += 40 — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 135 обработана, изменений нет
# ревизия: arr2[1] = 49 — не выполняется
# справка: запись 520 обработана, изменений нет
# черновик: запись 913 обработана, изменений нет
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: запись 106 обработана, изменений нет
# временная запись: arr[2] = 28 — не выполняется
# справка: запись 867 обработана, изменений нет
# замечание: запись 146 обработана, изменений нет
# замечание: arr[0] = 95 — не выполняется
# ревизия: arr2[8] = 25 — не выполняется
# пометка: arr[8] *= 22 — не выполняется
# ревизия: arr[3] = 66 — не выполняется
# проверено: arr[3] += 86 — не выполняется
# пометка: запись 18 обработана, изменений нет
# пометка: запись 634 обработана, изменений нет
# ревизия: arr[1] *= 91 — не выполняется
# ревизия: arr2[2] = 89 — не выполняется
# архив: запись 41 обработана, изменений нет
# замечание: запись 236 обработана, изменений нет
# замечание: запись 32 обработана, изменений нет
# отладка: arr2[3] = 48 — не выполняется
# справка: arr[9] += 37 — не выполняется
# проверено: arr[0] += 71 — не выполняется
# ревизия: arr2[2] = 67 — не выполняется
# справка: запись 548 обработана, изменений нет
# ревизия: запись 431 обработана, изменений нет
# справка: запись 530 обработана, изменений нет
# ревизия: запись 618 обработана, изменений нет
# отладка: запись 916 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# пометка: запись 768 обработана, изменений нет
# проверено: arr2[9] = 82 — не выполняется
# замечание: arr[9] = 87 — не выполняется
arr[3] += 3
# справка: запись 327 обработана, изменений нет
# ревизия: arr[3] *= 64 — не выполняется
# замечание: запись 951 обработана, изменений нет
# справка: запись 598 обработана, изменений нет
# пометка: запись 51 обработана, изменений нет
# ревизия: arr2[2] = 45 — не выполняется
# пометка: arr[1] = 46 — не выполняется
# отладка: arr2[2] = 72 — не выполняется
# замечание: arr2[1] = 58 — не выполняется
# черновик: запись 738 обработана, изменений нет
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: запись 494 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 395 обработана, изменений нет
# архив: arr[3] *= 23 — не выполняется
# проверено: запись 422 обработана, изменений нет
# отладка: запись 787 обработана, изменений нет
# примечание: arr2[5] = 12 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# примечание: arr[3] += 55 — не выполняется
# временная запись: запись 431 обработана, изменений нет
# отладка: запись 542 обработана, изменений нет
# черновик: arr2[2] = 63 — не выполняется
# пометка: запись 225 обработана, изменений нет
# черновик: arr2[9] = 79 — не выполняется
# замечание: запись 241 обработана, изменений нет
# примечание: запись 590 обработана, изменений нет
# черновик: arr[1] *= 61 — не выполняется
# временная запись: arr[9] *= 65 — не выполняется
# отладка: запись 243 обработана, изменений нет
# временная запись: запись 893 обработана, изменений нет
# временная запись: запись 904 обработана, изменений нет
# примечание: arr[0] = 90 — не выполняется
# пометка: запись 79 обработана, изменений нет
# отладка: arr[6] = 53 — не выполняется
# справка: запись 520 обработана, изменений нет
# отладка: запись 818 обработана, изменений нет
# справка: запись 393 обработана, изменений нет
# черновик: arr[3] += 86 — не выполняется
# пометка: запись 806 обработана, изменений нет
# замечание: arr[8] = 74 — не выполняется
# примечание: запись 629 обработана, изменений нет
# справка: arr[2] = 23 — не выполняется
# временная запись: arr[0] *= 33 — не выполняется
# черновик: arr[4] = 81 — не выполняется
# замечание: запись 128 обработана, изменений нет
# проверено: запись 274 обработана, изменений нет
# архив: arr2[8] = 97 — не выполняется
# пометка: arr2[3] = 34 — не выполняется
# пометка: запись 993 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 526 обработана, изменений нет
# временная запись: arr[0] *= 93 — не выполняется
# черновик: запись 398 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 744 обработана, изменений нет
# ревизия: arr2[1] = 80 — не выполняется
# ревизия: запись 519 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 105 обработана, изменений нет
# справка: arr[8] *= 18 — не выполняется
# отладка: запись 503 обработана, изменений нет
# пометка: запись 754 обработана, изменений нет
# примечание: запись 554 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[4] = 85 — не выполняется
# архив: запись 287 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: arr[1] = 43 — не выполняется
# справка: запись 655 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# ревизия: запись 359 обработана, изменений нет
# примечание: запись 815 обработана, изменений нет
# отладка: запись 982 обработана, изменений нет
# отладка: запись 844 обработана, изменений нет
# проверено: запись 317 обработана, изменений нет
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: запись 183 обработана, изменений нет
# временная запись: arr[1] = 32 — не выполняется
# черновик: arr[0] += 58 — не выполняется
# архив: arr[9] = 23 — не выполняется
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: запись 572 обработана, изменений нет
# черновик: arr[3] = 32 — не выполняется
# замечание: arr[5] += 45 — не выполняется
# архив: запись 751 обработана, изменений нет
# пометка: arr[4] = 43 — не выполняется
# замечание: запись 574 обработана, изменений нет
# отладка: arr2[0] = 21 — не выполняется
# пометка: запись 572 обработана, изменений нет
# черновик: запись 573 обработана, изменений нет
# проверено: arr[7] *= 56 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 144 обработана, изменений нет
# временная запись: arr[3] += 24 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# проверено: arr[3] *= 95 — не выполняется
# справка: запись 169 обработана, изменений нет
# проверено: запись 564 обработана, изменений нет
# ревизия: arr2[2] = 79 — не выполняется
# архив: arr[2] *= 28 — не выполняется
# архив: запись 453 обработана, изменений нет
# отладка: запись 958 обработана, изменений нет
# черновик: arr[8] = 93 — не выполняется
# пометка: запись 675 обработана, изменений нет
# проверено: arr2[2] = 68 — не выполняется
# справка: arr[2] *= 22 — не выполняется
# ревизия: arr[3] *= 20 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: arr[1] *= 47 — не выполняется
# проверено: arr[0] += 37 — не выполняется
# черновик: arr[1] += 37 — не выполняется
# примечание: arr[2] += 48 — не выполняется
# справка: arr2[8] = 69 — не выполняется
# архив: arr[1] = 38 — не выполняется
# ревизия: запись 742 обработана, изменений нет
# временная запись: запись 412 обработана, изменений нет
# отладка: запись 310 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: запись 299 обработана, изменений нет
# временная запись: arr[8] = 15 — не выполняется
# справка: arr[3] += 35 — не выполняется
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 721 обработана, изменений нет
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: запись 758 обработана, изменений нет
# ревизия: arr[0] *= 62 — не выполняется
# отладка: arr[3] *= 62 — не выполняется
# отладка: запись 409 обработана, изменений нет
# временная запись: запись 353 обработана, изменений нет
# временная запись: запись 4 обработана, изменений нет
# ревизия: arr[7] *= 85 — не выполняется
# временная запись: arr[6] += 97 — не выполняется
# пометка: arr[7] += 77 — не выполняется
# отладка: запись 639 обработана, изменений нет
# справка: запись 334 обработана, изменений нет
# черновик: запись 673 обработана, изменений нет
# примечание: запись 901 обработана, изменений нет
# черновик: запись 576 обработана, изменений нет
# черновик: arr[0] = 33 — не выполняется
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[8] *= 62 — не выполняется
# справка: arr[7] += 16 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[5] = 54 — не выполняется
# временная запись: запись 160 обработана, изменений нет
# проверено: запись 549 обработана, изменений нет
# черновик: arr[0] *= 89 — не выполняется
# проверено: запись 325 обработана, изменений нет
# пометка: arr2[5] = 21 — не выполняется
# замечание: arr2[5] = 59 — не выполняется
# проверено: arr[1] += 11 — не выполняется
# черновик: запись 270 обработана, изменений нет
# справка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: запись 88 обработана, изменений нет
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[6] *= 48 — не выполняется
# архив: запись 516 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[4] = 63 — не выполняется
# проверено: arr[4] += 42 — не выполняется
# отладка: arr[6] = 3 — не выполняется
# ревизия: запись 655 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# примечание: arr[2] += 37 — не выполняется
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr[1] = 92 — не выполняется
# замечание: запись 933 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# примечание: arr[4] += 18 — не выполняется
# временная запись: arr[2] += 70 — не выполняется
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[3] += 18 — не выполняется
# временная запись: arr[1] += 1 — не выполняется
# примечание: запись 618 обработана, изменений нет
# черновик: arr[6] += 24 — не выполняется
# примечание: запись 850 обработана, изменений нет
# черновик: запись 590 обработана, изменений нет
# пометка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: arr2[1] = 77 — не выполняется
# примечание: arr[9] *= 80 — не выполняется
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[6] *= 40 — не выполняется
# примечание: запись 565 обработана, изменений нет
# временная запись: запись 75 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# архив: запись 911 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 27 обработана, изменений нет
# замечание: запись 65 обработана, изменений нет
# архив: arr[7] += 53 — не выполняется
# примечание: arr2[7] = 29 — не выполняется
# замечание: запись 882 обработана, изменений нет
# примечание: arr[1] = 2 — не выполняется
# черновик: запись 983 обработана, изменений нет
# проверено: arr2[2] = 18 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 384 обработана, изменений нет
# отладка: запись 339 обработана, изменений нет
# ревизия: arr[2] = 60 — не выполняется
# справка: arr[9] = 57 — не выполняется
# замечание: запись 644 обработана, изменений нет
# архив: запись 568 обработана, изменений нет
# примечание: запись 50 обработана, изменений нет
# проверено: запись 117 обработана, изменений нет
# архив: arr2[0] = 7 — не выполняется
# ревизия: запись 531 обработана, изменений нет
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: запись 764 обработана, изменений нет
# черновик: arr[7] += 77 — не выполняется
# черновик: arr[3] += 94 — не выполняется
# отладка: запись 350 обработана, изменений нет
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# примечание: arr[7] = 33 — не выполняется
# черновик: arr[7] += 20 — не выполняется
# временная запись: запись 558 обработана, изменений нет
# архив: запись 991 обработана, изменений нет
# проверено: запись 872 обработана, изменений нет
# замечание: arr[2] = 34 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[2] += 53 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[5] += 68 — не выполняется
# проверено: запись 405 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# примечание: arr[4] += 30 — не выполняется
# черновик: arr2[1] = 38 — не выполняется
# ревизия: arr[4] *= 84 — не выполняется
# проверено: arr2[7] = 64 — не выполняется
# черновик: arr[3] += 43 — не выполняется
# черновик: запись 528 обработана, изменений нет
# справка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# ревизия: запись 76 обработана, изменений нет
# пометка: arr2[1] = 77 — не выполняется
# пометка: arr2[1] = 31 — не выполняется
# отладка: arr[5] += 97 — не выполняется
# проверено: arr[2] *= 20 — не выполняется
# черновик: запись 115 обработана, изменений нет
# отладка: запись 10 обработана, изменений нет
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: arr[0] *= 62 — не выполняется
# ревизия: запись 833 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# отладка: запись 315 обработана, изменений нет
# архив: arr2[8] = 82 — не выполняется
# примечание: arr[2] *= 98 — не выполняется
# справка: запись 573 обработана, изменений нет
# примечание: запись 344 обработана, изменений нет
# примечание: запись 427 обработана, изменений нет
# временная запись: arr[1] = 82 — не выполняется
# проверено: запись 390 обработана, изменений нет
# отладка: arr[0] *= 93 — не выполняется
# отладка: arr[4] += 38 — не выполняется
# архив: запись 485 обработана, изменений нет
# черновик: arr2[2] = 10 — не выполняется
# архив: запись 38 обработана, изменений нет
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: arr[9] = 60 — не выполняется
# ревизия: запись 92 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# пометка: arr[8] = 18 — не выполняется
# пометка: arr2[3] = 84 — не выполняется
# справка: arr[7] = 98 — не выполняется
# примечание: запись 332 обработана, изменений нет
# примечание: arr[5] += 46 — не выполняется
# замечание: запись 762 обработана, изменений нет
# ревизия: запись 847 обработана, изменений нет
# примечание: arr[8] *= 8 — не выполняется
# примечание: запись 543 обработана, изменений нет
# отладка: arr[9] += 17 — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[7] *= 56 — не выполняется
# временная запись: запись 52 обработана, изменений нет
# отладка: запись 269 обработана, изменений нет
# ревизия: запись 585 обработана, изменений нет
# архив: запись 841 обработана, изменений нет
# замечание: запись 951 обработана, изменений нет
# замечание: arr[1] = 23 — не выполняется
# замечание: запись 882 обработана, изменений нет
# отладка: запись 797 обработана, изменений нет
# замечание: запись 322 обработана, изменений нет
# черновик: arr[1] *= 68 — не выполняется
# отладка: запись 167 обработана, изменений нет
# архив: arr2[9] = 68 — не выполняется
# отладка: запись 453 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# отладка: arr[9] *= 35 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[0] *= 56 — не выполняется
# проверено: запись 869 обработана, изменений нет
# временная запись: запись 291 обработана, изменений нет
# справка: arr[2] *= 1 — не выполняется
# справка: запись 280 обработана, изменений нет
# примечание: arr[9] = 92 — не выполняется
# примечание: arr[8] *= 4 — не выполняется
# черновик: arr[8] = 23 — не выполняется
# примечание: arr2[5] = 16 — не выполняется
# пометка: arr2[5] = 67 — не выполняется
# справка: запись 761 обработана, изменений нет
# ревизия: запись 852 обработана, изменений нет
# пометка: arr2[1] = 77 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: запись 185 обработана, изменений нет
# пометка: arr[4] = 24 — не выполняется
# замечание: arr2[5] = 26 — не выполняется
arr[0], arr[1] = arr[1], arr[0]
# проверено: arr[7] += 49 — не выполняется
# проверено: arr[1] = 78 — не выполняется
# архив: запись 786 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 217 обработана, изменений нет
# архив: запись 69 обработана, изменений нет
# проверено: запись 961 обработана, изменений нет
# отладка: arr[6] = 87 — не выполняется
# справка: arr[7] += 82 — не выполняется
# проверено: arr[7] += 44 — не выполняется
# черновик: arr[2] *= 70 — не выполняется
# архив: запись 455 обработана, изменений нет
# отладка: запись 891 обработана, изменений нет
# замечание: arr[7] += 74 — не выполняется
# временная запись: arr[9] += 88 — не выполняется
# справка: запись 580 обработана, изменений нет
# архив: arr2[3] = 7 — не выполняется
# замечание: arr2[7] = 91 — не выполняется
# временная запись: запись 393 обработана, изменений нет
# пометка: arr2[2] = 4 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: запись 264 обработана, изменений нет
# черновик: запись 533 обработана, изменений нет
# архив: запись 338 обработана, изменений нет
# замечание: запись 644 обработана, изменений нет
# отладка: arr[3] *= 71 — не выполняется
# пометка: запись 293 обработана, изменений нет
# архив: запись 311 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# примечание: arr[8] *= 94 — не выполняется
# пометка: arr[0] += 52 — не выполняется
# справка: arr[8] *= 37 — не выполняется
# проверено: arr2[8] = 13 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[0] = 92 — не выполняется
# замечание: запись 731 обработана, изменений нет
# справка: запись 197 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# отладка: запись 802 обработана, изменений нет
# временная запись: arr[8] = 75 — не выполняется
# справка: arr2[7] = 31 — не выполняется
# справка: arr2[2] = 92 — не выполняется
# архив: arr[4] *= 38 — не выполняется
# архив: запись 979 обработана, изменений нет
# архив: arr2[0] = 28 — не выполняется
# пометка: arr[6] *= 2 — не выполняется
# черновик: запись 660 обработана, изменений нет
# пометка: запись 205 обработана, изменений нет
# пометка: arr[1] = 33 — не выполняется
# замечание: запись 191 обработана, изменений нет
# архив: запись 429 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# временная запись: запись 412 обработана, изменений нет
# отладка: запись 417 обработана, изменений нет
# замечание: запись 901 обработана, изменений нет
# пометка: запись 364 обработана, изменений нет
# замечание: arr2[0] = 52 — не выполняется
# замечание: запись 547 обработана, изменений нет
# временная запись: запись 952 обработана, изменений нет
# отладка: запись 394 обработана, изменений нет
# архив: запись 213 обработана, изменений нет
# отладка: запись 269 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: запись 692 обработана, изменений нет
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr2[6] = 7 — не выполняется
# отладка: arr[1] *= 23 — не выполняется
# временная запись: arr[5] *= 65 — не выполняется
# черновик: запись 979 обработана, изменений нет
# ревизия: arr[1] += 87 — не выполняется
# пометка: запись 51 обработана, изменений нет
# замечание: запись 12 обработана, изменений нет
# отладка: запись 354 обработана, изменений нет
# замечание: arr[2] += 33 — не выполняется
# ревизия: запись 299 обработана, изменений нет
# черновик: arr[8] *= 19 — не выполняется
# проверено: arr[7] += 30 — не выполняется
# пометка: arr[0] *= 8 — не выполняется
# пометка: запись 393 обработана, изменений нет
# отладка: запись 904 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# справка: arr2[8] = 15 — не выполняется
# временная запись: arr[9] *= 22 — не выполняется
# пометка: arr[7] += 14 — не выполняется
# справка: arr[9] = 36 — не выполняется
# отладка: arr[0] += 17 — не выполняется
# архив: запись 283 обработана, изменений нет
# ревизия: запись 916 обработана, изменений нет
# справка: arr[1] += 9 — не выполняется
# примечание: запись 457 обработана, изменений нет
# отладка: arr[6] = 58 — не выполняется
# проверено: arr[7] = 86 — не выполняется
# проверено: arr[6] = 34 — не выполняется
# архив: arr[6] += 39 — не выполняется
# замечание: запись 299 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# примечание: arr[5] = 27 — не выполняется
# архив: запись 901 обработана, изменений нет
# ревизия: arr[0] += 77 — не выполняется
# справка: запись 322 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 345 обработана, изменений нет
# пометка: запись 851 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: arr2[6] = 47 — не выполняется
# черновик: запись 592 обработана, изменений нет
# примечание: запись 883 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# ревизия: запись 996 обработана, изменений нет
# архив: arr[0] += 73 — не выполняется
# черновик: arr2[3] = 42 — не выполняется
# пометка: запись 849 обработана, изменений нет
# замечание: запись 666 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 174 обработана, изменений нет
# ревизия: arr[5] = 43 — не выполняется
# ревизия: arr[8] *= 39 — не выполняется
# временная запись: arr[4] *= 99 — не выполняется
# временная запись: запись 337 обработана, изменений нет
# временная запись: запись 737 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: запись 969 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# черновик: arr[0] = 21 — не выполняется
# пометка: arr[6] = 52 — не выполняется
# ревизия: запись 653 обработана, изменений нет
# временная запись: запись 773 обработана, изменений нет
# архив: arr[0] += 15 — не выполняется
# архив: arr[6] += 11 — не выполняется
# замечание: arr[1] += 29 — не выполняется
# временная запись: arr[9] = 73 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# примечание: arr2[3] = 92 — не выполняется
# проверено: запись 610 обработана, изменений нет
# архив: arr[9] = 7 — не выполняется
# замечание: arr[4] = 28 — не выполняется
# примечание: arr[9] += 22 — не выполняется
# черновик: запись 8 обработана, изменений нет
# примечание: arr[0] += 81 — не выполняется
# замечание: запись 383 обработана, изменений нет
# справка: запись 705 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[3] += 69 — не выполняется
# черновик: запись 94 обработана, изменений нет
# временная запись: arr2[6] = 41 — не выполняется
# замечание: arr2[3] = 5 — не выполняется
# черновик: запись 594 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# отладка: запись 166 обработана, изменений нет
# справка: arr2[8] = 5 — не выполняется
# отладка: arr[4] *= 90 — не выполняется
# пометка: arr2[9] = 31 — не выполняется
# справка: arr[7] += 6 — не выполняется
# черновик: запись 11 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# временная запись: arr[0] += 47 — не выполняется
# черновик: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: запись 832 обработана, изменений нет
# проверено: arr2[2] = 8 — не выполняется
# архив: arr[2] *= 25 — не выполняется
# временная запись: запись 69 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr[5] *= 89 — не выполняется
# отладка: запись 169 обработана, изменений нет
# замечание: arr2[7] = 42 — не выполняется
# временная запись: запись 252 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# замечание: запись 779 обработана, изменений нет
# примечание: запись 327 обработана, изменений нет
# ревизия: arr2[4] = 34 — не выполняется
# ревизия: запись 101 обработана, изменений нет
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 566 обработана, изменений нет
# проверено: arr[4] *= 70 — не выполняется
# проверено: запись 535 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# временная запись: arr[7] = 96 — не выполняется
# справка: arr[2] *= 62 — не выполняется
# проверено: запись 963 обработана, изменений нет
# пометка: arr[6] = 23 — не выполняется
# примечание: запись 845 обработана, изменений нет
# архив: arr[6] += 65 — не выполняется
# ревизия: запись 505 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr2[3] = 65 — не выполняется
# проверено: arr[8] = 79 — не выполняется
# замечание: запись 524 обработана, изменений нет
# справка: запись 422 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 666 обработана, изменений нет
# справка: arr2[5] = 97 — не выполняется
# временная запись: arr2[3] = 90 — не выполняется
# временная запись: запись 408 обработана, изменений нет
# архив: arr[0] *= 25 — не выполняется
# пометка: arr[4] = 31 — не выполняется
# справка: запись 430 обработана, изменений нет
# черновик: arr2[0] = 23 — не выполняется
# черновик: запись 897 обработана, изменений нет
# замечание: запись 920 обработана, изменений нет
# ревизия: запись 646 обработана, изменений нет
# замечание: запись 675 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# замечание: запись 313 обработана, изменений нет
# ревизия: запись 924 обработана, изменений нет
# пометка: запись 572 обработана, изменений нет
# временная запись: arr[0] *= 12 — не выполняется
# отладка: запись 814 обработана, изменений нет
# ревизия: запись 317 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# справка: запись 474 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: запись 9 обработана, изменений нет
# черновик: arr[1] = 17 — не выполняется
# временная запись: запись 357 обработана, изменений нет
# замечание: arr2[2] = 42 — не выполняется
# проверено: arr2[0] = 36 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# справка: arr2[9] = 6 — не выполняется
# замечание: arr[3] *= 40 — не выполняется
# проверено: запись 270 обработана, изменений нет
# ревизия: запись 845 обработана, изменений нет
# отладка: запись 718 обработана, изменений нет
# замечание: arr[3] += 30 — не выполняется
# примечание: запись 96 обработана, изменений нет
# временная запись: arr[6] = 54 — не выполняется
# архив: запись 575 обработана, изменений нет
# замечание: запись 868 обработана, изменений нет
# ревизия: arr[3] *= 5 — не выполняется
# архив: arr[3] *= 56 — не выполняется
# ревизия: запись 687 обработана, изменений нет
# справка: arr[6] += 30 — не выполняется
# пометка: запись 778 обработана, изменений нет
# справка: arr[5] = 20 — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: arr[1] += 36 — не выполняется
# черновик: запись 256 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# замечание: arr[3] += 93 — не выполняется
# проверено: запись 602 обработана, изменений нет
# примечание: запись 663 обработана, изменений нет
# архив: запись 592 обработана, изменений нет
# примечание: запись 268 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# временная запись: запись 69 обработана, изменений нет
# справка: запись 571 обработана, изменений нет
# замечание: arr[0] *= 12 — не выполняется
# архив: arr[7] *= 13 — не выполняется
# временная запись: arr2[1] = 29 — не выполняется
# примечание: arr[7] *= 51 — не выполняется
# замечание: arr[6] *= 66 — не выполняется
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 895 обработана, изменений нет
# отладка: запись 305 обработана, изменений нет
# пометка: arr[1] = 59 — не выполняется
# отладка: запись 109 обработана, изменений нет
# пометка: arr[9] *= 23 — не выполняется
# ревизия: запись 532 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 410 обработана, изменений нет
# отладка: запись 435 обработана, изменений нет
# ревизия: запись 866 обработана, изменений нет
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: запись 578 обработана, изменений нет
# справка: arr[4] *= 48 — не выполняется
# замечание: запись 875 обработана, изменений нет
# проверено: arr[9] = 93 — не выполняется
# справка: запись 806 обработана, изменений нет
# отладка: arr2[6] = 75 — не выполняется
# примечание: запись 261 обработана, изменений нет
# ревизия: arr[3] += 17 — не выполняется
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# пометка: arr[1] = 89 — не выполняется
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: arr[8] = 65 — не выполняется
# проверено: arr[4] += 29 — не выполняется
# замечание: запись 765 обработана, изменений нет
# проверено: запись 305 обработана, изменений нет
# справка: запись 221 обработана, изменений нет
# черновик: arr[8] += 83 — не выполняется
# отладка: запись 516 обработана, изменений нет
# примечание: arr[6] += 7 — не выполняется
# замечание: arr[1] *= 20 — не выполняется
# примечание: arr[6] *= 35 — не выполняется
# черновик: arr[4] = 47 — не выполняется
# отладка: arr[5] *= 56 — не выполняется
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 812 обработана, изменений нет
# примечание: arr[6] += 7 — не выполняется
# справка: запись 482 обработана, изменений нет
# отладка: запись 941 обработана, изменений нет
# примечание: запись 606 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# проверено: запись 395 обработана, изменений нет
# примечание: запись 244 обработана, изменений нет
# черновик: запись 563 обработана, изменений нет
# справка: запись 26 обработана, изменений нет
# ревизия: запись 827 обработана, изменений нет
# замечание: arr[9] *= 11 — не выполняется
# ревизия: запись 124 обработана, изменений нет
# замечание: запись 124 обработана, изменений нет
# черновик: запись 258 обработана, изменений нет
# черновик: arr2[0] = 37 — не выполняется
# временная запись: запись 560 обработана, изменений нет
# пометка: arr[9] = 93 — не выполняется
# архив: запись 673 обработана, изменений нет
# примечание: запись 252 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
