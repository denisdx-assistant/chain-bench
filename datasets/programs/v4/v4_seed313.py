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
arr[5] = 2
arr[7] += 31
arr[6], arr[2] = arr[2], arr[6]
arr[1] += 1
arr[3], arr[8] = arr[8], arr[3]
arr[5] += 3
arr[7] *= 1
arr[1], arr[4] = arr[4], arr[1]
"""

TRAP_0 = "arr[3] = 276"
TRAP_1 = "arr[8] = 335"
TRAP_2 = "arr[3] = 953"
TRAP_3 = "arr[7] = 997"
TRAP_4 = "arr[0] = 987"
TRAP_5 = "arr[5] = 883"
TRAP_6 = "arr[6] = 149"
TRAP_7 = "arr[7] = 900"
TRAP_8 = "arr[4] = 138"
TRAP_9 = "arr[9] = 274"
TRAP_10 = "arr[9] = 593"
TRAP_11 = "arr[1] = 682"
TRAP_12 = "arr[1] = 600"
TRAP_13 = "arr[2] = 277"
TRAP_14 = "arr[6] = 604"
TRAP_15 = "arr[7] = 847"
TRAP_16 = "arr[8] = 805"
TRAP_17 = "arr[1] = 372"
TRAP_18 = "arr[0] = 100"
TRAP_19 = "arr[2] = 511"
TRAP_20 = "arr[0] = 289"
TRAP_21 = "arr[9] = 801"
TRAP_22 = "arr[8] = 754"
TRAP_23 = "arr[9] = 168"
TRAP_24 = "arr[3] = 821"
TRAP_25 = "arr[6] = 709"
TRAP_26 = "arr[9] = 552"
TRAP_27 = "arr[3] = 685"
TRAP_28 = "arr[8] = 218"
TRAP_29 = "arr[9] = 657"
TRAP_30 = "arr[9] = 719"
TRAP_31 = "arr[8] = 887"
TRAP_32 = "arr[4] = 837"
TRAP_33 = "arr[5] = 650"
TRAP_34 = "arr[9] = 522"
TRAP_35 = "arr[3] = 336"
TRAP_36 = "arr[3] = 108"
TRAP_37 = "arr[5] = 274"
TRAP_38 = "arr[8] = 584"
TRAP_39 = "arr[7] = 402"
TRAP_40 = "arr[9] = 400"
TRAP_41 = "arr[8] = 522"
TRAP_42 = "arr[6] = 183"
TRAP_43 = "arr[5] = 359"
TRAP_44 = "arr[2] = 458"
TRAP_45 = "arr[1] = 380"
TRAP_46 = "arr[2] = 374"
TRAP_47 = "arr[5] = 655"
TRAP_48 = "arr[0] = 185"
TRAP_49 = "arr[4] = 555"
TRAP_50 = "arr[7] = 209"
TRAP_51 = "arr[4] = 716"
TRAP_52 = "arr[2] = 359"
TRAP_53 = "arr[0] = 884"
TRAP_54 = "arr[4] = 889"
TRAP_55 = "arr[0] = 989"
TRAP_56 = "arr[0] = 919"
TRAP_57 = "arr[7] = 199"
TRAP_58 = "arr[5] = 150"
TRAP_59 = "arr[7] = 796"
TRAP_60 = "arr[7] = 311"
TRAP_61 = "arr[1] = 128"
TRAP_62 = "arr[7] = 714"
TRAP_63 = "arr[5] = 561"
TRAP_64 = "arr[3] = 327"
TRAP_65 = "arr[0] = 194"
TRAP_66 = "arr[5] = 932"
TRAP_67 = "arr[6] = 329"
TRAP_68 = "arr[1] = 840"
TRAP_69 = "arr[1] = 368"
TRAP_70 = "arr[5] = 598"
TRAP_71 = "arr[8] = 787"
TRAP_72 = "arr[0] = 752"
TRAP_73 = "arr[2] = 278"
TRAP_74 = "arr[9] = 421"
TRAP_75 = "arr[9] = 156"
TRAP_76 = "arr[3] = 491"
TRAP_77 = "arr[3] = 714"
TRAP_78 = "arr[9] = 765"
TRAP_79 = "arr[8] = 277"
TRAP_80 = "arr[0] = 626"
TRAP_81 = "arr[5] = 640"
TRAP_82 = "arr[7] = 682"
TRAP_83 = "arr[3] = 380"
TRAP_84 = "arr[1] = 597"
TRAP_85 = "arr[7] = 372"
TRAP_86 = "arr[8] = 753"
TRAP_87 = "arr[8] = 820"
TRAP_88 = "arr[5] = 985"
TRAP_89 = "arr[3] = 602"
TRAP_90 = "arr[7] = 551"
TRAP_91 = "arr[1] = 692"
TRAP_92 = "arr[8] = 414"
TRAP_93 = "arr[1] = 171"
TRAP_94 = "arr[7] = 201"
TRAP_95 = "arr[7] = 550"
TRAP_96 = "arr[7] = 343"
TRAP_97 = "arr[8] = 558"
TRAP_98 = "arr[6] = 218"
TRAP_99 = "arr[4] = 237"
TRAP_100 = "arr[1] = 673"
TRAP_101 = "arr[8] = 297"
TRAP_102 = "arr[3] = 645"
TRAP_103 = "arr[5] = 465"
TRAP_104 = "arr[5] = 871"
TRAP_105 = "arr[3] = 894"
TRAP_106 = "arr[3] = 861"
TRAP_107 = "arr[3] = 266"
TRAP_108 = "arr[3] = 632"
TRAP_109 = "arr[4] = 776"
TRAP_110 = "arr[5] = 381"
TRAP_111 = "arr[4] = 300"
TRAP_112 = "arr[1] = 882"
TRAP_113 = "arr[9] = 141"
TRAP_114 = "arr[9] = 453"
TRAP_115 = "arr[9] = 318"
TRAP_116 = "arr[2] = 797"
TRAP_117 = "arr[6] = 371"
TRAP_118 = "arr[1] = 360"
TRAP_119 = "arr[4] = 139"
TRAP_120 = "arr[6] = 384"
TRAP_121 = "arr[2] = 456"
TRAP_122 = "arr[8] = 449"
TRAP_123 = "arr[7] = 636"
TRAP_124 = "arr[2] = 328"
TRAP_125 = "arr[8] = 996"
TRAP_126 = "arr[3] = 248"
TRAP_127 = "arr[7] = 372"
TRAP_128 = "arr[9] = 391"
TRAP_129 = "arr[7] = 855"
TRAP_130 = "arr[1] = 740"
TRAP_131 = "arr[3] = 310"
TRAP_132 = "arr[9] = 972"
TRAP_133 = "arr[7] = 595"
TRAP_134 = "arr[6] = 844"
TRAP_135 = "arr[3] = 118"
TRAP_136 = "arr[6] = 336"
TRAP_137 = "arr[4] = 621"
TRAP_138 = "arr[4] = 687"
TRAP_139 = "arr[1] = 667"
TRAP_140 = "arr[5] = 933"
TRAP_141 = "arr[7] = 442"
TRAP_142 = "arr[1] = 403"
TRAP_143 = "arr[8] = 191"
TRAP_144 = "arr[5] = 446"
TRAP_145 = "arr[4] = 154"
TRAP_146 = "arr[6] = 313"
TRAP_147 = "arr[4] = 335"
TRAP_148 = "arr[8] = 345"
TRAP_149 = "arr[9] = 159"

arr = [19, 6, 22, 14, 16, 28, 1, 7, 27, 5]

code_0 = re.sub(r'[0-9]', '#', str(arr[9]))
note_1 = str(arr[3]) + str(arr[7])
code_2 = re.sub(r'[0-9]', '#', str(arr[0]))
code_3 = re.sub(r'[0-9]', '#', str(arr[6]))
note_4 = str(arr[8]) + str(arr[0])
copy_5 = arr[3]
note_6 = str(arr[9]) + str(arr[5])
copy_7 = arr[2]
code_8 = re.sub(r'[0-9]', '#', str(arr[3]))
note_9 = str(arr[9]) + str(arr[0])
note_10 = str(arr[2]) + str(arr[1])
tmp_11 = arr[5] + 40
tmp_12 = arr[5] + 30
note_13 = str(arr[8]) + str(arr[8])
note_14 = str(arr[6]) + str(arr[1])
label_15 = "запись 15 не применялась"
code_16 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_17 = arr[2] + 46
label_18 = "запись 18 не применялась"
tmp_19 = arr[3] + 18
tmp_20 = arr[0] + 32
copy_21 = arr[4]
tmp_22 = arr[6] + 49
tmp_23 = arr[2] + 12
code_24 = re.sub(r'[0-9]', '#', str(arr[8]))
note_25 = str(arr[4]) + str(arr[0])
copy_26 = arr[6]
note_27 = str(arr[3]) + str(arr[8])
code_28 = re.sub(r'[0-9]', '#', str(arr[3]))
code_29 = re.sub(r'[0-9]', '#', str(arr[0]))
code_30 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_31 = arr[7]
note_32 = str(arr[0]) + str(arr[4])
code_33 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_34 = arr[2] + 39
note_35 = str(arr[5]) + str(arr[8])
label_36 = "запись 36 не применялась"
tmp_37 = arr[8] + 12
code_38 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_39 = arr[1]
code_40 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_41 = arr[5] + 8
copy_42 = arr[2]
copy_43 = arr[2]
code_44 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_45 = arr[9] + 29
code_46 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_47 = arr[1]
tmp_48 = arr[6] + 20
note_49 = str(arr[7]) + str(arr[1])
code_50 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_51 = arr[1] + 14
tmp_52 = arr[7] + 29
copy_53 = arr[8]
note_54 = str(arr[7]) + str(arr[3])
code_55 = re.sub(r'[0-9]', '#', str(arr[9]))
code_56 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_57 = arr[3] + 26
note_58 = str(arr[7]) + str(arr[1])
note_59 = str(arr[8]) + str(arr[4])
tmp_60 = arr[1] + 46
tmp_61 = arr[5] + 37
copy_62 = arr[6]
note_63 = str(arr[4]) + str(arr[7])
note_64 = str(arr[4]) + str(arr[4])
tmp_65 = arr[7] + 48
copy_66 = arr[1]
label_67 = "запись 67 не применялась"
note_68 = str(arr[2]) + str(arr[7])
tmp_69 = arr[7] + 8
label_70 = "запись 70 не применялась"
label_71 = "запись 71 не применялась"
code_72 = re.sub(r'[0-9]', '#', str(arr[2]))
code_73 = re.sub(r'[0-9]', '#', str(arr[0]))
note_74 = str(arr[7]) + str(arr[8])
note_75 = str(arr[2]) + str(arr[6])
tmp_76 = arr[6] + 38
copy_77 = arr[5]
tmp_78 = arr[6] + 21
tmp_79 = arr[8] + 35
code_80 = re.sub(r'[0-9]', '#', str(arr[0]))
code_81 = re.sub(r'[0-9]', '#', str(arr[4]))
code_82 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_83 = arr[6] + 30
code_84 = re.sub(r'[0-9]', '#', str(arr[4]))
note_85 = str(arr[1]) + str(arr[3])
tmp_86 = arr[1] + 21
copy_87 = arr[9]
note_88 = str(arr[1]) + str(arr[7])
tmp_89 = arr[1] + 41
note_90 = str(arr[5]) + str(arr[9])
code_91 = re.sub(r'[0-9]', '#', str(arr[0]))
code_92 = re.sub(r'[0-9]', '#', str(arr[8]))
label_93 = "запись 93 не применялась"
note_94 = str(arr[9]) + str(arr[4])
note_95 = str(arr[9]) + str(arr[2])
tmp_96 = arr[8] + 45
label_97 = "запись 97 не применялась"
note_98 = str(arr[6]) + str(arr[8])
code_99 = re.sub(r'[0-9]', '#', str(arr[8]))
code_100 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_101 = arr[3] + 17
tmp_102 = arr[7] + 26
note_103 = str(arr[2]) + str(arr[9])
label_104 = "запись 104 не применялась"
note_105 = str(arr[2]) + str(arr[7])
code_106 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_107 = arr[0] + 36
note_108 = str(arr[0]) + str(arr[0])
tmp_109 = arr[6] + 15
tmp_110 = arr[2] + 49
note_111 = str(arr[5]) + str(arr[7])
tmp_112 = arr[1] + 27
note_113 = str(arr[8]) + str(arr[8])
note_114 = str(arr[9]) + str(arr[0])
tmp_115 = arr[8] + 38
tmp_116 = arr[6] + 49
copy_117 = arr[0]
note_118 = str(arr[4]) + str(arr[6])
tmp_119 = arr[2] + 37
tmp_120 = arr[1] + 45
code_121 = re.sub(r'[0-9]', '#', str(arr[8]))
note_122 = str(arr[6]) + str(arr[0])
note_123 = str(arr[0]) + str(arr[8])
label_124 = "запись 124 не применялась"
code_125 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_126 = arr[9]
copy_127 = arr[6]
tmp_128 = arr[7] + 32
tmp_129 = arr[9] + 8
copy_130 = arr[5]
tmp_131 = arr[5] + 39
tmp_132 = arr[2] + 23
tmp_133 = arr[7] + 50
code_134 = re.sub(r'[0-9]', '#', str(arr[1]))
code_135 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_136 = arr[4]
tmp_137 = arr[2] + 18
label_138 = "запись 138 не применялась"
note_139 = str(arr[4]) + str(arr[9])
tmp_140 = arr[4] + 38
copy_141 = arr[6]
tmp_142 = arr[5] + 41
tmp_143 = arr[9] + 37
note_144 = str(arr[1]) + str(arr[9])
code_145 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_146 = arr[5] + 9
copy_147 = arr[7]
note_148 = str(arr[0]) + str(arr[2])
note_149 = str(arr[8]) + str(arr[6])
tmp_150 = arr[4] + 26
tmp_151 = arr[4] + 21
note_152 = str(arr[9]) + str(arr[4])
code_153 = re.sub(r'[0-9]', '#', str(arr[9]))
code_154 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_155 = arr[4]
note_156 = str(arr[6]) + str(arr[8])
note_157 = str(arr[8]) + str(arr[3])
note_158 = str(arr[3]) + str(arr[4])
note_159 = str(arr[6]) + str(arr[2])
note_160 = str(arr[8]) + str(arr[1])
tmp_161 = arr[6] + 8
note_162 = str(arr[0]) + str(arr[2])
tmp_163 = arr[1] + 25
copy_164 = arr[3]
tmp_165 = arr[1] + 40
label_166 = "запись 166 не применялась"
code_167 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_168 = arr[8]
code_169 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_170 = arr[3]
tmp_171 = arr[0] + 28
note_172 = str(arr[7]) + str(arr[1])
note_173 = str(arr[9]) + str(arr[9])
code_174 = re.sub(r'[0-9]', '#', str(arr[6]))
code_175 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_176 = arr[2] + 1
tmp_177 = arr[4] + 39
label_178 = "запись 178 не применялась"
tmp_179 = arr[4] + 50
code_180 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_181 = arr[4]
code_182 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_183 = arr[6]
tmp_184 = arr[2] + 33
note_185 = str(arr[3]) + str(arr[2])
note_186 = str(arr[6]) + str(arr[9])
copy_187 = arr[6]
note_188 = str(arr[4]) + str(arr[9])
note_189 = str(arr[0]) + str(arr[7])
code_190 = re.sub(r'[0-9]', '#', str(arr[9]))
note_191 = str(arr[1]) + str(arr[6])
note_192 = str(arr[5]) + str(arr[9])
note_193 = str(arr[8]) + str(arr[3])
tmp_194 = arr[2] + 17
note_195 = str(arr[4]) + str(arr[4])
code_196 = re.sub(r'[0-9]', '#', str(arr[6]))
note_197 = str(arr[7]) + str(arr[0])
note_198 = str(arr[5]) + str(arr[8])
tmp_199 = arr[0] + 31
copy_200 = arr[4]
label_201 = "запись 201 не применялась"
tmp_202 = arr[1] + 43
copy_203 = arr[5]
note_204 = str(arr[7]) + str(arr[7])
note_205 = str(arr[8]) + str(arr[3])
code_206 = re.sub(r'[0-9]', '#', str(arr[5]))
note_207 = str(arr[3]) + str(arr[1])
note_208 = str(arr[4]) + str(arr[2])
note_209 = str(arr[3]) + str(arr[1])
note_210 = str(arr[5]) + str(arr[2])
label_211 = "запись 211 не применялась"
label_212 = "запись 212 не применялась"
note_213 = str(arr[2]) + str(arr[6])
tmp_214 = arr[6] + 20
tmp_215 = arr[5] + 24
copy_216 = arr[6]
tmp_217 = arr[0] + 20
tmp_218 = arr[0] + 49
note_219 = str(arr[0]) + str(arr[7])
note_220 = str(arr[0]) + str(arr[0])
tmp_221 = arr[5] + 40
note_222 = str(arr[1]) + str(arr[7])
tmp_223 = arr[7] + 13
label_224 = "запись 224 не применялась"
code_225 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_226 = arr[9] + 20
copy_227 = arr[2]
tmp_228 = arr[0] + 19
copy_229 = arr[3]
code_230 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_231 = arr[8] + 35
code_232 = re.sub(r'[0-9]', '#', str(arr[2]))
code_233 = re.sub(r'[0-9]', '#', str(arr[8]))
note_234 = str(arr[5]) + str(arr[5])
tmp_235 = arr[9] + 7
copy_236 = arr[9]
tmp_237 = arr[4] + 8
tmp_238 = arr[3] + 48
note_239 = str(arr[1]) + str(arr[3])
note_240 = str(arr[0]) + str(arr[9])
note_241 = str(arr[1]) + str(arr[9])
tmp_242 = arr[3] + 25
note_243 = str(arr[5]) + str(arr[3])
copy_244 = arr[8]
copy_245 = arr[9]
code_246 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_247 = arr[9] + 48
copy_248 = arr[4]
copy_249 = arr[1]
code_250 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_251 = arr[9] + 46
code_252 = re.sub(r'[0-9]', '#', str(arr[4]))
note_253 = str(arr[1]) + str(arr[3])
code_254 = re.sub(r'[0-9]', '#', str(arr[4]))
note_255 = str(arr[0]) + str(arr[1])
code_256 = re.sub(r'[0-9]', '#', str(arr[6]))
note_257 = str(arr[1]) + str(arr[2])
code_258 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_259 = arr[1]
code_260 = re.sub(r'[0-9]', '#', str(arr[9]))
label_261 = "запись 261 не применялась"
note_262 = str(arr[1]) + str(arr[5])
tmp_263 = arr[2] + 16
code_264 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_265 = arr[2] + 31
code_266 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_267 = arr[1] + 31
tmp_268 = arr[9] + 29
note_269 = str(arr[5]) + str(arr[6])
note_270 = str(arr[2]) + str(arr[9])
note_271 = str(arr[7]) + str(arr[6])
code_272 = re.sub(r'[0-9]', '#', str(arr[2]))
code_273 = re.sub(r'[0-9]', '#', str(arr[0]))
note_274 = str(arr[2]) + str(arr[9])
tmp_275 = arr[2] + 23
tmp_276 = arr[4] + 38
copy_277 = arr[8]
tmp_278 = arr[2] + 21
tmp_279 = arr[8] + 48
copy_280 = arr[3]
code_281 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_282 = arr[0] + 11
code_283 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_284 = arr[8] + 18
note_285 = str(arr[1]) + str(arr[1])
copy_286 = arr[0]
note_287 = str(arr[7]) + str(arr[7])
tmp_288 = arr[3] + 11
note_289 = str(arr[3]) + str(arr[4])
label_290 = "запись 290 не применялась"
note_291 = str(arr[7]) + str(arr[0])
note_292 = str(arr[7]) + str(arr[1])
tmp_293 = arr[1] + 17
label_294 = "запись 294 не применялась"
code_295 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_296 = arr[6] + 18
note_297 = str(arr[4]) + str(arr[3])
note_298 = str(arr[1]) + str(arr[4])
tmp_299 = arr[0] + 47
note_300 = str(arr[1]) + str(arr[7])
copy_301 = arr[4]
tmp_302 = arr[0] + 2
tmp_303 = arr[2] + 44
tmp_304 = arr[8] + 35
tmp_305 = arr[3] + 49
tmp_306 = arr[8] + 12
code_307 = re.sub(r'[0-9]', '#', str(arr[2]))
note_308 = str(arr[8]) + str(arr[6])
code_309 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_310 = arr[9]
tmp_311 = arr[4] + 33
label_312 = "запись 312 не применялась"
code_313 = re.sub(r'[0-9]', '#', str(arr[8]))
note_314 = str(arr[2]) + str(arr[6])
code_315 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_316 = arr[1] + 26
tmp_317 = arr[9] + 30
copy_318 = arr[8]
tmp_319 = arr[0] + 7
note_320 = str(arr[0]) + str(arr[0])
tmp_321 = arr[7] + 5
code_322 = re.sub(r'[0-9]', '#', str(arr[3]))
code_323 = re.sub(r'[0-9]', '#', str(arr[1]))
label_324 = "запись 324 не применялась"
note_325 = str(arr[8]) + str(arr[6])
tmp_326 = arr[6] + 7
tmp_327 = arr[9] + 12
code_328 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_329 = arr[9] + 29
note_330 = str(arr[7]) + str(arr[9])
tmp_331 = arr[9] + 1
tmp_332 = arr[7] + 22
note_333 = str(arr[8]) + str(arr[6])
tmp_334 = arr[7] + 10
tmp_335 = arr[4] + 10
tmp_336 = arr[5] + 23
note_337 = str(arr[8]) + str(arr[1])
copy_338 = arr[4]
tmp_339 = arr[4] + 32
copy_340 = arr[2]
note_341 = str(arr[6]) + str(arr[0])
tmp_342 = arr[2] + 8
tmp_343 = arr[5] + 46
code_344 = re.sub(r'[0-9]', '#', str(arr[1]))
note_345 = str(arr[7]) + str(arr[7])
code_346 = re.sub(r'[0-9]', '#', str(arr[5]))
note_347 = str(arr[0]) + str(arr[9])
code_348 = re.sub(r'[0-9]', '#', str(arr[8]))
code_349 = re.sub(r'[0-9]', '#', str(arr[3]))
note_350 = str(arr[6]) + str(arr[1])
note_351 = str(arr[7]) + str(arr[8])
tmp_352 = arr[7] + 38
note_353 = str(arr[6]) + str(arr[7])
tmp_354 = arr[2] + 22
note_355 = str(arr[3]) + str(arr[1])
copy_356 = arr[1]
note_357 = str(arr[7]) + str(arr[5])
note_358 = str(arr[5]) + str(arr[8])
tmp_359 = arr[7] + 21
note_360 = str(arr[2]) + str(arr[8])
note_361 = str(arr[8]) + str(arr[9])
note_362 = str(arr[2]) + str(arr[4])
tmp_363 = arr[2] + 42
note_364 = str(arr[3]) + str(arr[6])
note_365 = str(arr[0]) + str(arr[9])
tmp_366 = arr[2] + 40
note_367 = str(arr[6]) + str(arr[9])
code_368 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_369 = arr[2] + 38
tmp_370 = arr[9] + 4
tmp_371 = arr[5] + 44
copy_372 = arr[3]
note_373 = str(arr[2]) + str(arr[2])
note_374 = str(arr[8]) + str(arr[6])
code_375 = re.sub(r'[0-9]', '#', str(arr[9]))
code_376 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_377 = arr[1]
code_378 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_379 = arr[1] + 10
code_380 = re.sub(r'[0-9]', '#', str(arr[5]))
label_381 = "запись 381 не применялась"
note_382 = str(arr[3]) + str(arr[6])
note_383 = str(arr[5]) + str(arr[4])
note_384 = str(arr[3]) + str(arr[0])
tmp_385 = arr[9] + 36
note_386 = str(arr[9]) + str(arr[5])
label_387 = "запись 387 не применялась"
tmp_388 = arr[3] + 3
tmp_389 = arr[3] + 46
tmp_390 = arr[6] + 5
copy_391 = arr[2]
copy_392 = arr[2]
note_393 = str(arr[2]) + str(arr[0])
note_394 = str(arr[8]) + str(arr[6])
copy_395 = arr[6]
note_396 = str(arr[8]) + str(arr[3])
code_397 = re.sub(r'[0-9]', '#', str(arr[6]))
code_398 = re.sub(r'[0-9]', '#', str(arr[5]))
note_399 = str(arr[8]) + str(arr[3])
tmp_400 = arr[1] + 16
code_401 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_402 = arr[4] + 33
tmp_403 = arr[1] + 47
label_404 = "запись 404 не применялась"
copy_405 = arr[3]
tmp_406 = arr[4] + 45
code_407 = re.sub(r'[0-9]', '#', str(arr[4]))
code_408 = re.sub(r'[0-9]', '#', str(arr[6]))
note_409 = str(arr[2]) + str(arr[7])
note_410 = str(arr[8]) + str(arr[8])
copy_411 = arr[6]
tmp_412 = arr[3] + 39
label_413 = "запись 413 не применялась"
code_414 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_415 = arr[2] + 2
tmp_416 = arr[9] + 2
tmp_417 = arr[6] + 36
label_418 = "запись 418 не применялась"
note_419 = str(arr[6]) + str(arr[9])
tmp_420 = arr[0] + 41
note_421 = str(arr[9]) + str(arr[5])
code_422 = re.sub(r'[0-9]', '#', str(arr[1]))
note_423 = str(arr[4]) + str(arr[8])
code_424 = re.sub(r'[0-9]', '#', str(arr[8]))
note_425 = str(arr[9]) + str(arr[9])
note_426 = str(arr[7]) + str(arr[7])
note_427 = str(arr[4]) + str(arr[4])
label_428 = "запись 428 не применялась"
tmp_429 = arr[0] + 15
copy_430 = arr[3]
tmp_431 = arr[8] + 15
tmp_432 = arr[2] + 46
tmp_433 = arr[7] + 13
code_434 = re.sub(r'[0-9]', '#', str(arr[1]))
label_435 = "запись 435 не применялась"
code_436 = re.sub(r'[0-9]', '#', str(arr[3]))
note_437 = str(arr[4]) + str(arr[3])
tmp_438 = arr[3] + 22
tmp_439 = arr[4] + 48
note_440 = str(arr[6]) + str(arr[4])
tmp_441 = arr[2] + 44
code_442 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_443 = arr[3] + 34
copy_444 = arr[0]
label_445 = "запись 445 не применялась"
tmp_446 = arr[8] + 49
tmp_447 = arr[8] + 14
copy_448 = arr[2]
copy_449 = arr[5]
tmp_450 = arr[2] + 2
copy_451 = arr[4]
code_452 = re.sub(r'[0-9]', '#', str(arr[1]))
code_453 = re.sub(r'[0-9]', '#', str(arr[7]))
label_454 = "запись 454 не применялась"
tmp_455 = arr[5] + 20
tmp_456 = arr[8] + 27
code_457 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_458 = arr[1] + 16
tmp_459 = arr[0] + 40
copy_460 = arr[6]
tmp_461 = arr[4] + 1
note_462 = str(arr[0]) + str(arr[5])
copy_463 = arr[5]
tmp_464 = arr[1] + 17
copy_465 = arr[0]
code_466 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_467 = arr[6] + 25
copy_468 = arr[5]
label_469 = "запись 469 не применялась"
code_470 = re.sub(r'[0-9]', '#', str(arr[0]))
code_471 = re.sub(r'[0-9]', '#', str(arr[5]))
note_472 = str(arr[0]) + str(arr[9])
copy_473 = arr[6]
note_474 = str(arr[4]) + str(arr[4])
copy_475 = arr[2]
note_476 = str(arr[3]) + str(arr[1])
label_477 = "запись 477 не применялась"
code_478 = re.sub(r'[0-9]', '#', str(arr[0]))
note_479 = str(arr[8]) + str(arr[4])
label_480 = "запись 480 не применялась"
code_481 = re.sub(r'[0-9]', '#', str(arr[8]))
label_482 = "запись 482 не применялась"
code_483 = re.sub(r'[0-9]', '#', str(arr[2]))
label_484 = "запись 484 не применялась"
note_485 = str(arr[0]) + str(arr[5])
note_486 = str(arr[1]) + str(arr[0])
code_487 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_488 = arr[7]
tmp_489 = arr[1] + 15
code_490 = re.sub(r'[0-9]', '#', str(arr[9]))
note_491 = str(arr[1]) + str(arr[9])
label_492 = "запись 492 не применялась"
note_493 = str(arr[4]) + str(arr[8])
copy_494 = arr[4]
note_495 = str(arr[9]) + str(arr[5])
tmp_496 = arr[9] + 34
tmp_497 = arr[6] + 32
tmp_498 = arr[0] + 23
copy_499 = arr[6]
note_500 = str(arr[3]) + str(arr[8])
code_501 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_502 = arr[0] + 10
code_503 = re.sub(r'[0-9]', '#', str(arr[0]))
note_504 = str(arr[0]) + str(arr[2])
copy_505 = arr[6]
note_506 = str(arr[7]) + str(arr[1])
copy_507 = arr[9]
code_508 = re.sub(r'[0-9]', '#', str(arr[9]))
code_509 = re.sub(r'[0-9]', '#', str(arr[3]))
label_510 = "запись 510 не применялась"
note_511 = str(arr[7]) + str(arr[2])
code_512 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_513 = arr[9]
tmp_514 = arr[0] + 8
tmp_515 = arr[7] + 24
code_516 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_517 = arr[7] + 50
tmp_518 = arr[1] + 44
note_519 = str(arr[3]) + str(arr[6])
code_520 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_521 = arr[3] + 9
tmp_522 = arr[5] + 35
tmp_523 = arr[8] + 41
tmp_524 = arr[9] + 4
note_525 = str(arr[5]) + str(arr[1])
tmp_526 = arr[6] + 25
tmp_527 = arr[8] + 35
note_528 = str(arr[9]) + str(arr[5])
tmp_529 = arr[1] + 22
tmp_530 = arr[5] + 43
tmp_531 = arr[0] + 39
code_532 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_533 = arr[2]
copy_534 = arr[0]
note_535 = str(arr[1]) + str(arr[0])
tmp_536 = arr[9] + 45
label_537 = "запись 537 не применялась"
code_538 = re.sub(r'[0-9]', '#', str(arr[1]))
code_539 = re.sub(r'[0-9]', '#', str(arr[0]))
note_540 = str(arr[7]) + str(arr[4])
copy_541 = arr[7]
label_542 = "запись 542 не применялась"
code_543 = re.sub(r'[0-9]', '#', str(arr[7]))
code_544 = re.sub(r'[0-9]', '#', str(arr[5]))
note_545 = str(arr[8]) + str(arr[0])
note_546 = str(arr[9]) + str(arr[9])
label_547 = "запись 547 не применялась"
copy_548 = arr[1]
copy_549 = arr[0]
note_550 = str(arr[0]) + str(arr[6])
note_551 = str(arr[1]) + str(arr[8])
tmp_552 = arr[3] + 18
copy_553 = arr[8]
tmp_554 = arr[9] + 20
copy_555 = arr[0]
copy_556 = arr[6]
tmp_557 = arr[4] + 29
tmp_558 = arr[0] + 2
tmp_559 = arr[9] + 18
tmp_560 = arr[2] + 7
code_561 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_562 = arr[6] + 4
copy_563 = arr[9]
label_564 = "запись 564 не применялась"
note_565 = str(arr[4]) + str(arr[3])
tmp_566 = arr[8] + 27
note_567 = str(arr[3]) + str(arr[1])
code_568 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_569 = arr[9] + 40
note_570 = str(arr[0]) + str(arr[5])
note_571 = str(arr[1]) + str(arr[3])
note_572 = str(arr[6]) + str(arr[7])
label_573 = "запись 573 не применялась"
code_574 = re.sub(r'[0-9]', '#', str(arr[2]))
note_575 = str(arr[6]) + str(arr[8])
note_576 = str(arr[1]) + str(arr[7])
code_577 = re.sub(r'[0-9]', '#', str(arr[8]))
label_578 = "запись 578 не применялась"
tmp_579 = arr[7] + 39
label_580 = "запись 580 не применялась"
note_581 = str(arr[8]) + str(arr[2])
copy_582 = arr[7]
note_583 = str(arr[7]) + str(arr[9])
label_584 = "запись 584 не применялась"
code_585 = re.sub(r'[0-9]', '#', str(arr[1]))
note_586 = str(arr[9]) + str(arr[4])
code_587 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_588 = arr[3] + 13
tmp_589 = arr[0] + 15
note_590 = str(arr[1]) + str(arr[9])
code_591 = re.sub(r'[0-9]', '#', str(arr[3]))
note_592 = str(arr[1]) + str(arr[2])
tmp_593 = arr[2] + 5
label_594 = "запись 594 не применялась"
copy_595 = arr[7]
copy_596 = arr[5]
label_597 = "запись 597 не применялась"
code_598 = re.sub(r'[0-9]', '#', str(arr[5]))
note_599 = str(arr[4]) + str(arr[2])
note_600 = str(arr[7]) + str(arr[9])
tmp_601 = arr[4] + 43
copy_602 = arr[0]
tmp_603 = arr[4] + 32
note_604 = str(arr[1]) + str(arr[3])
tmp_605 = arr[2] + 22
note_606 = str(arr[8]) + str(arr[9])
note_607 = str(arr[0]) + str(arr[4])
label_608 = "запись 608 не применялась"
note_609 = str(arr[0]) + str(arr[9])
code_610 = re.sub(r'[0-9]', '#', str(arr[5]))
code_611 = re.sub(r'[0-9]', '#', str(arr[1]))
label_612 = "запись 612 не применялась"
code_613 = re.sub(r'[0-9]', '#', str(arr[4]))
label_614 = "запись 614 не применялась"
tmp_615 = arr[8] + 42
tmp_616 = arr[0] + 24
tmp_617 = arr[3] + 22
tmp_618 = arr[3] + 29
tmp_619 = arr[0] + 8
tmp_620 = arr[7] + 5
tmp_621 = arr[7] + 40
note_622 = str(arr[7]) + str(arr[5])
code_623 = re.sub(r'[0-9]', '#', str(arr[4]))
note_624 = str(arr[5]) + str(arr[3])
tmp_625 = arr[3] + 29
code_626 = re.sub(r'[0-9]', '#', str(arr[0]))
code_627 = re.sub(r'[0-9]', '#', str(arr[3]))
label_628 = "запись 628 не применялась"
code_629 = re.sub(r'[0-9]', '#', str(arr[2]))
code_630 = re.sub(r'[0-9]', '#', str(arr[2]))
note_631 = str(arr[5]) + str(arr[5])
tmp_632 = arr[1] + 12
tmp_633 = arr[4] + 10
note_634 = str(arr[4]) + str(arr[9])
tmp_635 = arr[7] + 45
tmp_636 = arr[4] + 38
note_637 = str(arr[3]) + str(arr[1])
note_638 = str(arr[8]) + str(arr[3])
tmp_639 = arr[2] + 42
tmp_640 = arr[8] + 37
code_641 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_642 = arr[0]
copy_643 = arr[1]
note_644 = str(arr[5]) + str(arr[5])
tmp_645 = arr[3] + 34
copy_646 = arr[7]
code_647 = re.sub(r'[0-9]', '#', str(arr[0]))
note_648 = str(arr[9]) + str(arr[2])
label_649 = "запись 649 не применялась"
tmp_650 = arr[4] + 27
note_651 = str(arr[7]) + str(arr[5])
tmp_652 = arr[5] + 32
code_653 = re.sub(r'[0-9]', '#', str(arr[8]))
code_654 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_655 = arr[8]
code_656 = re.sub(r'[0-9]', '#', str(arr[3]))
note_657 = str(arr[6]) + str(arr[5])
tmp_658 = arr[6] + 50
copy_659 = arr[1]
tmp_660 = arr[8] + 28
copy_661 = arr[6]
code_662 = re.sub(r'[0-9]', '#', str(arr[0]))
note_663 = str(arr[2]) + str(arr[3])
copy_664 = arr[0]
note_665 = str(arr[9]) + str(arr[7])
copy_666 = arr[7]
note_667 = str(arr[9]) + str(arr[0])
code_668 = re.sub(r'[0-9]', '#', str(arr[9]))
code_669 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_670 = arr[3] + 43
copy_671 = arr[7]
copy_672 = arr[5]
copy_673 = arr[8]
note_674 = str(arr[6]) + str(arr[7])
tmp_675 = arr[0] + 31
label_676 = "запись 676 не применялась"
label_677 = "запись 677 не применялась"
label_678 = "запись 678 не применялась"
tmp_679 = arr[4] + 21
copy_680 = arr[1]
label_681 = "запись 681 не применялась"
copy_682 = arr[0]
note_683 = str(arr[7]) + str(arr[5])
tmp_684 = arr[0] + 10
note_685 = str(arr[9]) + str(arr[3])
code_686 = re.sub(r'[0-9]', '#', str(arr[3]))
note_687 = str(arr[1]) + str(arr[1])
copy_688 = arr[8]
tmp_689 = arr[5] + 41
copy_690 = arr[6]
note_691 = str(arr[8]) + str(arr[6])
copy_692 = arr[6]
label_693 = "запись 693 не применялась"
tmp_694 = arr[0] + 19
note_695 = str(arr[1]) + str(arr[5])
code_696 = re.sub(r'[0-9]', '#', str(arr[1]))
note_697 = str(arr[3]) + str(arr[8])
note_698 = str(arr[6]) + str(arr[1])
note_699 = str(arr[7]) + str(arr[2])
tmp_700 = arr[1] + 36
tmp_701 = arr[0] + 42
copy_702 = arr[8]
label_703 = "запись 703 не применялась"
code_704 = re.sub(r'[0-9]', '#', str(arr[4]))
note_705 = str(arr[6]) + str(arr[0])
note_706 = str(arr[9]) + str(arr[2])
code_707 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_708 = arr[4] + 9
note_709 = str(arr[1]) + str(arr[0])
tmp_710 = arr[5] + 49
copy_711 = arr[9]
tmp_712 = arr[2] + 27
code_713 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_714 = arr[8] + 46
copy_715 = arr[1]
tmp_716 = arr[9] + 15
tmp_717 = arr[9] + 40
tmp_718 = arr[7] + 20
tmp_719 = arr[6] + 30
tmp_720 = arr[2] + 34
copy_721 = arr[4]
note_722 = str(arr[8]) + str(arr[0])
note_723 = str(arr[0]) + str(arr[4])
tmp_724 = arr[0] + 40
code_725 = re.sub(r'[0-9]', '#', str(arr[5]))
code_726 = re.sub(r'[0-9]', '#', str(arr[7]))
code_727 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_728 = arr[9] + 28
tmp_729 = arr[4] + 3
note_730 = str(arr[4]) + str(arr[8])
label_731 = "запись 731 не применялась"
note_732 = str(arr[6]) + str(arr[6])
tmp_733 = arr[1] + 13
note_734 = str(arr[1]) + str(arr[2])
tmp_735 = arr[6] + 38
tmp_736 = arr[2] + 1
copy_737 = arr[2]
copy_738 = arr[2]
label_739 = "запись 739 не применялась"
code_740 = re.sub(r'[0-9]', '#', str(arr[9]))
code_741 = re.sub(r'[0-9]', '#', str(arr[3]))
code_742 = re.sub(r'[0-9]', '#', str(arr[1]))
code_743 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_744 = arr[6]
note_745 = str(arr[0]) + str(arr[8])
code_746 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_747 = arr[1] + 39
code_748 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_749 = arr[2] + 18
note_750 = str(arr[8]) + str(arr[0])
note_751 = str(arr[8]) + str(arr[2])
label_752 = "запись 752 не применялась"
label_753 = "запись 753 не применялась"
copy_754 = arr[9]
code_755 = re.sub(r'[0-9]', '#', str(arr[9]))
code_756 = re.sub(r'[0-9]', '#', str(arr[2]))
label_757 = "запись 757 не применялась"
tmp_758 = arr[3] + 34
tmp_759 = arr[4] + 49
note_760 = str(arr[6]) + str(arr[7])
code_761 = re.sub(r'[0-9]', '#', str(arr[6]))
label_762 = "запись 762 не применялась"
tmp_763 = arr[9] + 10
tmp_764 = arr[5] + 9
tmp_765 = arr[4] + 25
tmp_766 = arr[1] + 4
code_767 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_768 = arr[2]
note_769 = str(arr[5]) + str(arr[4])
note_770 = str(arr[2]) + str(arr[3])
tmp_771 = arr[1] + 31
code_772 = re.sub(r'[0-9]', '#', str(arr[1]))
code_773 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_774 = arr[6] + 13
tmp_775 = arr[7] + 42
note_776 = str(arr[6]) + str(arr[6])
tmp_777 = arr[8] + 38
code_778 = re.sub(r'[0-9]', '#', str(arr[8]))
note_779 = str(arr[0]) + str(arr[9])
copy_780 = arr[2]
tmp_781 = arr[3] + 4
note_782 = str(arr[3]) + str(arr[8])
copy_783 = arr[5]
code_784 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_785 = arr[7] + 21
code_786 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_787 = arr[5] + 49
tmp_788 = arr[9] + 43
tmp_789 = arr[5] + 40
code_790 = re.sub(r'[0-9]', '#', str(arr[6]))
label_791 = "запись 791 не применялась"
code_792 = re.sub(r'[0-9]', '#', str(arr[7]))
code_793 = re.sub(r'[0-9]', '#', str(arr[0]))
code_794 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_795 = arr[6] + 14
tmp_796 = arr[9] + 21
code_797 = re.sub(r'[0-9]', '#', str(arr[9]))
note_798 = str(arr[6]) + str(arr[4])
copy_799 = arr[7]

t83 = str(arr[3]) + str(arr[9])
# архив: запись 862 обработана, изменений нет
# замечание: запись 772 обработана, изменений нет
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 176 обработана, изменений нет
# ревизия: запись 71 обработана, изменений нет
# проверено: запись 780 обработана, изменений нет
# временная запись: запись 780 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# отладка: запись 276 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# временная запись: запись 395 обработана, изменений нет
# отладка: arr[3] += 21 — не выполняется
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr[4] = 1 — не выполняется
# проверено: arr[7] *= 36 — не выполняется
# временная запись: запись 365 обработана, изменений нет
# временная запись: arr2[2] = 8 — не выполняется
# справка: arr[7] += 70 — не выполняется
# замечание: запись 831 обработана, изменений нет
# отладка: arr2[6] = 81 — не выполняется
# справка: arr[3] = 52 — не выполняется
# архив: запись 193 обработана, изменений нет
# отладка: arr[3] += 84 — не выполняется
# ревизия: запись 367 обработана, изменений нет
# замечание: запись 170 обработана, изменений нет
# замечание: arr[5] = 79 — не выполняется
# проверено: запись 943 обработана, изменений нет
# временная запись: arr[3] *= 80 — не выполняется
# примечание: запись 637 обработана, изменений нет
# примечание: arr[6] *= 13 — не выполняется
# черновик: запись 252 обработана, изменений нет
# замечание: запись 575 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr2[5] = 76 — не выполняется
# архив: arr[3] = 53 — не выполняется
# архив: запись 183 обработана, изменений нет
# отладка: запись 884 обработана, изменений нет
# черновик: arr2[7] = 88 — не выполняется
# временная запись: запись 758 обработана, изменений нет
# пометка: arr[3] += 78 — не выполняется
# отладка: запись 699 обработана, изменений нет
# черновик: запись 103 обработана, изменений нет
# архив: arr[7] += 77 — не выполняется
# пометка: запись 702 обработана, изменений нет
# ревизия: запись 626 обработана, изменений нет
# архив: запись 721 обработана, изменений нет
# отладка: запись 673 обработана, изменений нет
# временная запись: arr2[3] = 2 — не выполняется
# отладка: запись 670 обработана, изменений нет
# примечание: arr[7] += 25 — не выполняется
# замечание: arr2[0] = 52 — не выполняется
# примечание: запись 487 обработана, изменений нет
# отладка: arr[3] += 73 — не выполняется
# примечание: запись 273 обработана, изменений нет
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr[4] *= 44 — не выполняется
# проверено: arr[5] = 4 — не выполняется
# временная запись: arr[0] += 58 — не выполняется
# замечание: запись 375 обработана, изменений нет
# черновик: arr[7] = 34 — не выполняется
# замечание: запись 842 обработана, изменений нет
# замечание: запись 679 обработана, изменений нет
# пометка: arr[6] *= 80 — не выполняется
# пометка: arr2[5] = 36 — не выполняется
# черновик: запись 599 обработана, изменений нет
# пометка: запись 641 обработана, изменений нет
# временная запись: arr[4] *= 46 — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 625 обработана, изменений нет
# примечание: arr[9] = 89 — не выполняется
# архив: arr[8] = 45 — не выполняется
# ревизия: arr2[4] = 12 — не выполняется
# черновик: arr[7] *= 90 — не выполняется
# примечание: запись 174 обработана, изменений нет
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr[1] *= 85 — не выполняется
# замечание: arr[6] = 76 — не выполняется
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 141 обработана, изменений нет
# архив: arr[3] *= 74 — не выполняется
# черновик: arr[5] += 50 — не выполняется
# временная запись: запись 300 обработана, изменений нет
# временная запись: запись 762 обработана, изменений нет
# черновик: запись 961 обработана, изменений нет
# черновик: arr[7] += 95 — не выполняется
# пометка: запись 567 обработана, изменений нет
# черновик: arr[1] = 34 — не выполняется
# отладка: arr[1] *= 63 — не выполняется
# ревизия: arr2[8] = 53 — не выполняется
# архив: arr[3] *= 8 — не выполняется
# примечание: запись 98 обработана, изменений нет
# ревизия: запись 443 обработана, изменений нет
# архив: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 972 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# ревизия: arr[2] = 91 — не выполняется
# временная запись: arr[9] += 62 — не выполняется
# примечание: arr[0] += 83 — не выполняется
# проверено: arr2[9] = 74 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: arr[3] += 5 — не выполняется
# отладка: arr[0] = 44 — не выполняется
# примечание: arr[7] = 44 — не выполняется
# пометка: запись 224 обработана, изменений нет
# архив: запись 288 обработана, изменений нет
# справка: запись 299 обработана, изменений нет
# проверено: запись 203 обработана, изменений нет
# черновик: arr2[7] = 90 — не выполняется
# замечание: запись 303 обработана, изменений нет
# архив: запись 756 обработана, изменений нет
# ревизия: arr2[8] = 71 — не выполняется
# ревизия: arr[3] *= 35 — не выполняется
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: запись 625 обработана, изменений нет
# проверено: запись 875 обработана, изменений нет
# временная запись: запись 829 обработана, изменений нет
# временная запись: запись 374 обработана, изменений нет
# проверено: arr[4] = 85 — не выполняется
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: запись 590 обработана, изменений нет
# пометка: запись 689 обработана, изменений нет
# пометка: запись 283 обработана, изменений нет
# временная запись: arr[1] += 54 — не выполняется
# отладка: запись 47 обработана, изменений нет
# ревизия: запись 999 обработана, изменений нет
# пометка: запись 58 обработана, изменений нет
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: запись 710 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# примечание: запись 587 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# проверено: arr2[7] = 80 — не выполняется
# отладка: запись 710 обработана, изменений нет
# примечание: arr2[1] = 55 — не выполняется
# отладка: arr2[7] = 99 — не выполняется
# замечание: запись 384 обработана, изменений нет
# примечание: запись 911 обработана, изменений нет
# временная запись: arr[6] *= 62 — не выполняется
# временная запись: arr[8] *= 56 — не выполняется
# замечание: запись 708 обработана, изменений нет
# примечание: запись 158 обработана, изменений нет
# справка: arr[8] += 68 — не выполняется
# примечание: запись 734 обработана, изменений нет
# черновик: arr[9] = 92 — не выполняется
# проверено: запись 39 обработана, изменений нет
# примечание: arr2[3] = 56 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# архив: arr[0] *= 23 — не выполняется
# архив: arr[8] *= 28 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 468 обработана, изменений нет
# справка: arr[8] *= 84 — не выполняется
# отладка: запись 917 обработана, изменений нет
# замечание: запись 195 обработана, изменений нет
# пометка: запись 631 обработана, изменений нет
# замечание: arr[0] *= 43 — не выполняется
# проверено: запись 920 обработана, изменений нет
# ревизия: arr[5] += 49 — не выполняется
# справка: запись 8 обработана, изменений нет
# замечание: запись 738 обработана, изменений нет
# архив: arr[0] *= 34 — не выполняется
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 945 обработана, изменений нет
# черновик: запись 749 обработана, изменений нет
# архив: arr[7] += 25 — не выполняется
# архив: запись 344 обработана, изменений нет
# справка: arr[5] *= 31 — не выполняется
# временная запись: запись 597 обработана, изменений нет
# проверено: arr2[6] = 20 — не выполняется
# ревизия: запись 920 обработана, изменений нет
# архив: запись 648 обработана, изменений нет
# проверено: arr[7] = 43 — не выполняется
# пометка: запись 985 обработана, изменений нет
# справка: arr[7] = 79 — не выполняется
# справка: запись 189 обработана, изменений нет
# замечание: arr[9] += 86 — не выполняется
# ревизия: arr[1] *= 24 — не выполняется
# временная запись: arr2[8] = 47 — не выполняется
# архив: arr[2] = 2 — не выполняется
# черновик: arr[2] += 11 — не выполняется
# черновик: запись 281 обработана, изменений нет
# замечание: запись 999 обработана, изменений нет
# справка: запись 977 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# справка: запись 534 обработана, изменений нет
# пометка: запись 795 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 850 обработана, изменений нет
# замечание: arr[1] *= 27 — не выполняется
# отладка: запись 423 обработана, изменений нет
# ревизия: arr[3] *= 26 — не выполняется
# примечание: запись 297 обработана, изменений нет
# примечание: arr[9] = 78 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 540 обработана, изменений нет
# примечание: запись 70 обработана, изменений нет
# справка: запись 216 обработана, изменений нет
# примечание: arr[2] = 55 — не выполняется
# архив: запись 811 обработана, изменений нет
# черновик: запись 333 обработана, изменений нет
# черновик: arr[5] = 53 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 745 обработана, изменений нет
# проверено: arr[1] += 66 — не выполняется
# проверено: arr[7] += 4 — не выполняется
# справка: запись 790 обработана, изменений нет
# проверено: arr[8] = 23 — не выполняется
# отладка: запись 730 обработана, изменений нет
# проверено: запись 731 обработана, изменений нет
# пометка: запись 78 обработана, изменений нет
# справка: запись 805 обработана, изменений нет
# черновик: arr[8] *= 30 — не выполняется
# проверено: arr[4] = 25 — не выполняется
# архив: arr2[3] = 86 — не выполняется
# примечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 761 обработана, изменений нет
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: arr[3] += 50 — не выполняется
# отладка: запись 439 обработана, изменений нет
# справка: запись 920 обработана, изменений нет
# временная запись: запись 897 обработана, изменений нет
# примечание: запись 101 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# примечание: запись 696 обработана, изменений нет
# справка: запись 898 обработана, изменений нет
# проверено: arr[4] *= 7 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr2[1] = 86 — не выполняется
# архив: arr[1] = 17 — не выполняется
# справка: запись 130 обработана, изменений нет
# черновик: arr2[5] = 8 — не выполняется
# справка: запись 474 обработана, изменений нет
# справка: arr2[5] = 25 — не выполняется
# архив: запись 791 обработана, изменений нет
# временная запись: запись 103 обработана, изменений нет
# проверено: запись 739 обработана, изменений нет
# временная запись: arr[9] += 37 — не выполняется
# черновик: arr[4] = 69 — не выполняется
# черновик: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 950 обработана, изменений нет
# примечание: arr[7] += 13 — не выполняется
# пометка: arr2[3] = 27 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# справка: arr2[8] = 6 — не выполняется
# ревизия: запись 194 обработана, изменений нет
# пометка: запись 905 обработана, изменений нет
# примечание: arr[4] *= 26 — не выполняется
# отладка: запись 753 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# замечание: arr[3] = 84 — не выполняется
# отладка: arr[5] = 17 — не выполняется
# отладка: запись 933 обработана, изменений нет
# пометка: arr2[5] = 90 — не выполняется
# отладка: запись 942 обработана, изменений нет
# пометка: запись 323 обработана, изменений нет
# пометка: arr[0] += 1 — не выполняется
# замечание: запись 956 обработана, изменений нет
# проверено: запись 858 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[0] += 10 — не выполняется
# архив: запись 969 обработана, изменений нет
# ревизия: arr2[9] = 16 — не выполняется
# проверено: запись 581 обработана, изменений нет
# черновик: запись 492 обработана, изменений нет
# примечание: arr[6] += 78 — не выполняется
# отладка: arr2[9] = 18 — не выполняется
# архив: запись 256 обработана, изменений нет
# отладка: запись 81 обработана, изменений нет
# временная запись: запись 298 обработана, изменений нет
# замечание: arr2[6] = 2 — не выполняется
# проверено: arr[1] *= 24 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: arr[8] += 59 — не выполняется
# отладка: запись 203 обработана, изменений нет
# пометка: arr2[1] = 38 — не выполняется
# ревизия: запись 708 обработана, изменений нет
# справка: запись 564 обработана, изменений нет
# отладка: запись 233 обработана, изменений нет
# ревизия: запись 356 обработана, изменений нет
# справка: arr[8] += 59 — не выполняется
# примечание: arr[8] += 2 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr[8] += 41 — не выполняется
# черновик: запись 82 обработана, изменений нет
# справка: запись 544 обработана, изменений нет
# пометка: arr2[9] = 83 — не выполняется
# примечание: запись 254 обработана, изменений нет
# отладка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
arr[1] = int(t83) % 97
# черновик: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 432 обработана, изменений нет
# архив: запись 122 обработана, изменений нет
# черновик: запись 766 обработана, изменений нет
# справка: arr[5] = 24 — не выполняется
# временная запись: arr[1] = 64 — не выполняется
# отладка: arr[2] = 81 — не выполняется
# архив: arr[6] += 69 — не выполняется
# черновик: запись 496 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# примечание: запись 146 обработана, изменений нет
# отладка: запись 261 обработана, изменений нет
# временная запись: запись 906 обработана, изменений нет
# замечание: запись 454 обработана, изменений нет
# проверено: запись 393 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: arr2[5] = 36 — не выполняется
# отладка: запись 200 обработана, изменений нет
# замечание: запись 98 обработана, изменений нет
# архив: arr[8] *= 75 — не выполняется
# проверено: запись 625 обработана, изменений нет
# архив: запись 438 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# примечание: arr[3] += 41 — не выполняется
# черновик: arr2[8] = 53 — не выполняется
# черновик: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr[8] = 20 — не выполняется
# временная запись: запись 210 обработана, изменений нет
# ревизия: запись 951 обработана, изменений нет
# примечание: запись 363 обработана, изменений нет
# примечание: arr[0] = 33 — не выполняется
# отладка: запись 784 обработана, изменений нет
# примечание: arr2[8] = 60 — не выполняется
# архив: arr2[3] = 36 — не выполняется
# черновик: запись 66 обработана, изменений нет
# архив: запись 659 обработана, изменений нет
# замечание: запись 813 обработана, изменений нет
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 914 обработана, изменений нет
# проверено: запись 8 обработана, изменений нет
# отладка: arr[0] += 78 — не выполняется
# ревизия: arr[7] += 22 — не выполняется
# пометка: запись 615 обработана, изменений нет
# примечание: arr[3] *= 44 — не выполняется
# справка: запись 60 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# черновик: запись 23 обработана, изменений нет
# пометка: запись 815 обработана, изменений нет
# пометка: arr[9] *= 84 — не выполняется
# замечание: arr[7] += 6 — не выполняется
# справка: запись 338 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# справка: запись 677 обработана, изменений нет
# отладка: arr[8] += 61 — не выполняется
# примечание: arr[9] *= 17 — не выполняется
# справка: arr[6] = 85 — не выполняется
# архив: запись 668 обработана, изменений нет
# черновик: arr[9] *= 70 — не выполняется
# архив: arr2[9] = 67 — не выполняется
# проверено: запись 8 обработана, изменений нет
# архив: arr2[5] = 2 — не выполняется
# справка: запись 23 обработана, изменений нет
# примечание: запись 252 обработана, изменений нет
# ревизия: arr[6] = 31 — не выполняется
# черновик: arr[8] = 37 — не выполняется
# справка: запись 871 обработана, изменений нет
# архив: arr[1] = 23 — не выполняется
# временная запись: запись 717 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: запись 756 обработана, изменений нет
# архив: arr[9] += 27 — не выполняется
# черновик: запись 36 обработана, изменений нет
# справка: arr[2] += 43 — не выполняется
# пометка: запись 14 обработана, изменений нет
# отладка: запись 753 обработана, изменений нет
# пометка: запись 311 обработана, изменений нет
# черновик: arr[0] = 46 — не выполняется
# черновик: запись 975 обработана, изменений нет
# отладка: arr[0] += 91 — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[6] = 32 — не выполняется
# проверено: запись 684 обработана, изменений нет
# пометка: arr[5] = 85 — не выполняется
# справка: arr[2] *= 8 — не выполняется
# временная запись: arr[3] = 60 — не выполняется
# отладка: arr2[9] = 54 — не выполняется
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# архив: arr[6] *= 7 — не выполняется
# временная запись: запись 796 обработана, изменений нет
# временная запись: запись 554 обработана, изменений нет
# архив: arr[3] += 66 — не выполняется
# замечание: запись 217 обработана, изменений нет
# временная запись: arr[9] += 19 — не выполняется
# отладка: запись 73 обработана, изменений нет
# временная запись: запись 550 обработана, изменений нет
# ревизия: arr[7] = 27 — не выполняется
# замечание: запись 195 обработана, изменений нет
# проверено: запись 164 обработана, изменений нет
# временная запись: arr[1] *= 20 — не выполняется
# архив: arr[6] *= 1 — не выполняется
# справка: arr2[5] = 1 — не выполняется
# ревизия: arr[7] *= 75 — не выполняется
# проверено: запись 316 обработана, изменений нет
# примечание: запись 695 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: arr2[8] = 32 — не выполняется
# замечание: запись 394 обработана, изменений нет
# пометка: arr[0] = 97 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[2] *= 8 — не выполняется
# пометка: arr[2] = 77 — не выполняется
# архив: запись 655 обработана, изменений нет
# черновик: запись 51 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# проверено: запись 191 обработана, изменений нет
# примечание: arr[0] += 9 — не выполняется
# справка: запись 726 обработана, изменений нет
# примечание: запись 632 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# отладка: arr[2] *= 35 — не выполняется
# примечание: arr[7] *= 76 — не выполняется
# справка: arr[8] += 38 — не выполняется
# замечание: запись 957 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# временная запись: arr[4] = 10 — не выполняется
# архив: arr2[0] = 34 — не выполняется
# временная запись: arr[7] += 89 — не выполняется
# архив: arr2[1] = 84 — не выполняется
# замечание: arr[5] = 6 — не выполняется
# черновик: запись 255 обработана, изменений нет
# замечание: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: запись 254 обработана, изменений нет
# архив: arr2[3] = 41 — не выполняется
# справка: запись 307 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr[2] *= 16 — не выполняется
# отладка: arr[6] = 46 — не выполняется
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[6] = 31 — не выполняется
# проверено: запись 815 обработана, изменений нет
# примечание: arr2[7] = 70 — не выполняется
# ревизия: запись 33 обработана, изменений нет
# проверено: arr2[7] = 35 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[2] = 49 — не выполняется
# проверено: arr[6] += 96 — не выполняется
# примечание: запись 902 обработана, изменений нет
# архив: запись 856 обработана, изменений нет
# архив: arr2[1] = 7 — не выполняется
# черновик: запись 904 обработана, изменений нет
# справка: запись 861 обработана, изменений нет
# примечание: arr[2] = 36 — не выполняется
# черновик: arr[9] += 21 — не выполняется
# временная запись: arr[0] = 52 — не выполняется
# примечание: arr[7] = 83 — не выполняется
# замечание: arr[8] = 55 — не выполняется
# замечание: запись 280 обработана, изменений нет
# примечание: запись 792 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# временная запись: запись 104 обработана, изменений нет
# пометка: arr[6] *= 98 — не выполняется
# временная запись: arr[3] *= 28 — не выполняется
# черновик: arr2[9] = 71 — не выполняется
# справка: arr[1] = 48 — не выполняется
# проверено: arr[9] *= 97 — не выполняется
# примечание: arr[6] *= 94 — не выполняется
# проверено: запись 218 обработана, изменений нет
# проверено: arr2[6] = 68 — не выполняется
# ревизия: arr[0] *= 70 — не выполняется
# справка: запись 682 обработана, изменений нет
# справка: arr[0] += 10 — не выполняется
# черновик: запись 242 обработана, изменений нет
# справка: arr2[3] = 57 — не выполняется
# справка: запись 904 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[0] *= 66 — не выполняется
# примечание: запись 48 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# черновик: arr[2] = 88 — не выполняется
# пометка: запись 159 обработана, изменений нет
# ревизия: arr[3] = 55 — не выполняется
# отладка: arr[3] *= 99 — не выполняется
# пометка: arr[7] = 65 — не выполняется
# отладка: arr2[5] = 80 — не выполняется
# ревизия: arr[7] = 96 — не выполняется
# проверено: arr2[8] = 91 — не выполняется
# черновик: arr[1] *= 79 — не выполняется
# проверено: запись 796 обработана, изменений нет
# замечание: запись 393 обработана, изменений нет
# замечание: запись 688 обработана, изменений нет
# отладка: запись 75 обработана, изменений нет
# справка: запись 932 обработана, изменений нет
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 656 обработана, изменений нет
# временная запись: arr[1] *= 83 — не выполняется
# справка: arr[3] += 23 — не выполняется
# временная запись: arr2[7] = 41 — не выполняется
# примечание: запись 952 обработана, изменений нет
# черновик: запись 517 обработана, изменений нет
# архив: запись 444 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# архив: arr[3] *= 24 — не выполняется
# примечание: arr[3] = 50 — не выполняется
# справка: запись 874 обработана, изменений нет
# примечание: arr[4] = 78 — не выполняется
# временная запись: запись 965 обработана, изменений нет
# замечание: arr[1] = 49 — не выполняется
# временная запись: запись 445 обработана, изменений нет
# черновик: запись 156 обработана, изменений нет
# отладка: arr2[3] = 81 — не выполняется
# архив: arr[3] += 78 — не выполняется
# пометка: arr2[4] = 42 — не выполняется
# архив: запись 602 обработана, изменений нет
# временная запись: запись 209 обработана, изменений нет
# примечание: запись 832 обработана, изменений нет
# черновик: arr[8] *= 69 — не выполняется
# отладка: запись 950 обработана, изменений нет
# ревизия: запись 716 обработана, изменений нет
# отладка: arr2[1] = 74 — не выполняется
# замечание: arr[5] += 7 — не выполняется
# проверено: arr[1] = 35 — не выполняется
# отладка: запись 597 обработана, изменений нет
# временная запись: запись 800 обработана, изменений нет
# архив: arr[8] = 70 — не выполняется
# проверено: arr2[8] = 36 — не выполняется
# архив: arr[6] = 52 — не выполняется
# пометка: запись 792 обработана, изменений нет
# временная запись: arr[8] += 51 — не выполняется
# замечание: arr2[7] = 49 — не выполняется
# замечание: запись 315 обработана, изменений нет
# ревизия: arr[8] += 45 — не выполняется
# ревизия: arr[8] += 65 — не выполняется
# временная запись: запись 664 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: запись 200 обработана, изменений нет
# архив: arr[4] = 5 — не выполняется
# черновик: запись 545 обработана, изменений нет
# отладка: запись 832 обработана, изменений нет
# черновик: arr2[8] = 57 — не выполняется
# отладка: запись 111 обработана, изменений нет
# пометка: arr[0] += 56 — не выполняется
# архив: arr2[6] = 23 — не выполняется
# замечание: arr[5] *= 27 — не выполняется
# черновик: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr[4] += 85 — не выполняется
# справка: запись 661 обработана, изменений нет
# отладка: запись 912 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: запись 355 обработана, изменений нет
# пометка: запись 728 обработана, изменений нет
# архив: arr2[2] = 98 — не выполняется
# отладка: запись 48 обработана, изменений нет
# архив: arr2[9] = 93 — не выполняется
# проверено: запись 399 обработана, изменений нет
# ревизия: arr2[5] = 34 — не выполняется
# справка: запись 673 обработана, изменений нет
# черновик: arr[8] += 99 — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 889 обработана, изменений нет
# ревизия: запись 86 обработана, изменений нет
# временная запись: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: запись 535 обработана, изменений нет
# временная запись: запись 857 обработана, изменений нет
# замечание: arr[7] += 65 — не выполняется
# временная запись: arr[7] += 87 — не выполняется
# временная запись: arr2[7] = 29 — не выполняется
# временная запись: запись 53 обработана, изменений нет
# отладка: запись 691 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# примечание: запись 381 обработана, изменений нет
# проверено: запись 338 обработана, изменений нет
# черновик: запись 874 обработана, изменений нет
# черновик: arr[7] = 71 — не выполняется
# ревизия: запись 527 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr[7] = 19 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[0] += 99 — не выполняется
# проверено: arr[2] *= 92 — не выполняется
# отладка: arr[4] += 32 — не выполняется
# замечание: запись 463 обработана, изменений нет
# черновик: запись 717 обработана, изменений нет
# временная запись: arr2[5] = 36 — не выполняется
# ревизия: запись 938 обработана, изменений нет
# замечание: arr[9] += 48 — не выполняется
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr2[5] = 50 — не выполняется
# замечание: запись 803 обработана, изменений нет
# справка: запись 495 обработана, изменений нет
# временная запись: запись 573 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# замечание: запись 634 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 552 обработана, изменений нет
t601 = str(arr[4]) + str(arr[3])
# проверено: arr[5] += 55 — не выполняется
# пометка: arr2[0] = 24 — не выполняется
# справка: запись 891 обработана, изменений нет
# справка: arr[3] = 10 — не выполняется
# примечание: запись 51 обработана, изменений нет
# примечание: arr[3] = 97 — не выполняется
# замечание: arr[9] *= 73 — не выполняется
# справка: запись 548 обработана, изменений нет
# черновик: запись 64 обработана, изменений нет
# архив: arr[4] = 59 — не выполняется
# замечание: запись 951 обработана, изменений нет
# временная запись: arr[6] *= 20 — не выполняется
# ревизия: запись 574 обработана, изменений нет
# ревизия: arr[9] += 22 — не выполняется
# проверено: arr[3] = 18 — не выполняется
# примечание: запись 459 обработана, изменений нет
# архив: запись 944 обработана, изменений нет
# пометка: arr[5] *= 18 — не выполняется
# проверено: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# справка: arr[4] += 84 — не выполняется
# временная запись: запись 647 обработана, изменений нет
# временная запись: arr[1] = 10 — не выполняется
# справка: запись 579 обработана, изменений нет
# отладка: запись 256 обработана, изменений нет
# ревизия: запись 666 обработана, изменений нет
# проверено: запись 534 обработана, изменений нет
# замечание: arr[2] += 4 — не выполняется
# архив: запись 498 обработана, изменений нет
# черновик: arr[6] *= 88 — не выполняется
# пометка: arr[5] += 14 — не выполняется
# черновик: запись 262 обработана, изменений нет
# справка: arr2[5] = 86 — не выполняется
# отладка: запись 85 обработана, изменений нет
# временная запись: arr[1] *= 82 — не выполняется
# временная запись: arr[6] *= 4 — не выполняется
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 541 обработана, изменений нет
# временная запись: arr[0] *= 43 — не выполняется
# примечание: arr[1] = 16 — не выполняется
# примечание: запись 717 обработана, изменений нет
# примечание: arr[6] = 30 — не выполняется
# примечание: запись 639 обработана, изменений нет
# справка: запись 955 обработана, изменений нет
# примечание: запись 219 обработана, изменений нет
# пометка: запись 944 обработана, изменений нет
# ревизия: запись 588 обработана, изменений нет
# пометка: arr[1] *= 2 — не выполняется
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr2[9] = 21 — не выполняется
# пометка: запись 472 обработана, изменений нет
# примечание: запись 601 обработана, изменений нет
# архив: запись 995 обработана, изменений нет
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 582 обработана, изменений нет
# временная запись: arr[3] = 10 — не выполняется
# черновик: запись 636 обработана, изменений нет
# архив: запись 519 обработана, изменений нет
# отладка: запись 420 обработана, изменений нет
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# ревизия: arr[3] = 90 — не выполняется
# пометка: arr[8] += 67 — не выполняется
# архив: arr[1] = 98 — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: arr[3] = 60 — не выполняется
# временная запись: arr2[2] = 89 — не выполняется
# пометка: запись 278 обработана, изменений нет
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# справка: запись 71 обработана, изменений нет
# замечание: запись 38 обработана, изменений нет
# временная запись: запись 346 обработана, изменений нет
# примечание: запись 73 обработана, изменений нет
# проверено: запись 45 обработана, изменений нет
# замечание: запись 7 обработана, изменений нет
# проверено: arr[8] *= 80 — не выполняется
# проверено: запись 778 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# архив: запись 92 обработана, изменений нет
# отладка: arr[7] *= 98 — не выполняется
# проверено: запись 974 обработана, изменений нет
# временная запись: arr2[8] = 13 — не выполняется
# черновик: запись 244 обработана, изменений нет
# примечание: запись 788 обработана, изменений нет
# отладка: arr2[3] = 27 — не выполняется
# справка: запись 760 обработана, изменений нет
# пометка: arr[3] = 56 — не выполняется
# ревизия: запись 58 обработана, изменений нет
# замечание: arr[2] *= 45 — не выполняется
# замечание: запись 264 обработана, изменений нет
# черновик: arr[7] = 68 — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[2] = 26 — не выполняется
# замечание: запись 332 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 152 обработана, изменений нет
# пометка: arr[7] *= 65 — не выполняется
# примечание: запись 411 обработана, изменений нет
# отладка: запись 618 обработана, изменений нет
# примечание: запись 510 обработана, изменений нет
# архив: запись 491 обработана, изменений нет
# справка: arr[2] += 32 — не выполняется
# проверено: arr[0] = 85 — не выполняется
# архив: запись 42 обработана, изменений нет
# черновик: arr2[7] = 20 — не выполняется
# пометка: запись 17 обработана, изменений нет
# черновик: запись 897 обработана, изменений нет
# примечание: arr2[2] = 1 — не выполняется
# пометка: запись 34 обработана, изменений нет
# ревизия: запись 679 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# справка: arr[9] += 27 — не выполняется
# примечание: запись 596 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: запись 13 обработана, изменений нет
# примечание: arr[9] *= 38 — не выполняется
# примечание: arr[6] = 41 — не выполняется
# архив: запись 986 обработана, изменений нет
# черновик: arr2[4] = 33 — не выполняется
# примечание: запись 612 обработана, изменений нет
# черновик: arr2[6] = 10 — не выполняется
# архив: запись 964 обработана, изменений нет
# проверено: arr2[1] = 71 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[9] *= 2 — не выполняется
# архив: запись 60 обработана, изменений нет
# отладка: запись 807 обработана, изменений нет
# временная запись: arr2[9] = 13 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr2[7] = 6 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr2[7] = 67 — не выполняется
# справка: arr[7] = 26 — не выполняется
# черновик: запись 960 обработана, изменений нет
# замечание: запись 72 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# пометка: arr2[0] = 22 — не выполняется
# замечание: запись 864 обработана, изменений нет
# временная запись: запись 495 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# отладка: arr2[4] = 48 — не выполняется
# проверено: запись 694 обработана, изменений нет
# пометка: arr[3] = 78 — не выполняется
# замечание: запись 415 обработана, изменений нет
# архив: запись 782 обработана, изменений нет
# примечание: arr[9] += 6 — не выполняется
# справка: запись 474 обработана, изменений нет
# ревизия: arr2[4] = 82 — не выполняется
# проверено: запись 873 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 952 обработана, изменений нет
# отладка: запись 69 обработана, изменений нет
# черновик: запись 582 обработана, изменений нет
# проверено: запись 921 обработана, изменений нет
# замечание: arr2[1] = 91 — не выполняется
# временная запись: запись 121 обработана, изменений нет
# черновик: arr[5] = 75 — не выполняется
# замечание: запись 516 обработана, изменений нет
# примечание: запись 276 обработана, изменений нет
# проверено: arr[4] += 95 — не выполняется
# пометка: arr[0] *= 23 — не выполняется
# отладка: arr2[0] = 86 — не выполняется
# временная запись: arr[1] += 16 — не выполняется
# ревизия: arr2[9] = 89 — не выполняется
# справка: запись 775 обработана, изменений нет
# ревизия: arr[4] = 83 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# проверено: запись 260 обработана, изменений нет
# справка: arr[4] *= 82 — не выполняется
# пометка: arr[5] = 98 — не выполняется
# временная запись: запись 868 обработана, изменений нет
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 169 обработана, изменений нет
# проверено: arr[0] *= 28 — не выполняется
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# архив: запись 694 обработана, изменений нет
# справка: arr[2] += 40 — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: arr[7] *= 85 — не выполняется
# замечание: запись 576 обработана, изменений нет
# проверено: arr2[2] = 92 — не выполняется
# пометка: запись 758 обработана, изменений нет
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 865 обработана, изменений нет
# архив: arr2[5] = 34 — не выполняется
# черновик: запись 963 обработана, изменений нет
# архив: arr[5] += 73 — не выполняется
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[6] += 84 — не выполняется
# замечание: arr[4] += 71 — не выполняется
# архив: запись 212 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 801 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# справка: запись 160 обработана, изменений нет
# отладка: запись 120 обработана, изменений нет
# замечание: arr[4] = 93 — не выполняется
# ревизия: запись 155 обработана, изменений нет
# замечание: arr[4] = 19 — не выполняется
# отладка: arr[3] += 25 — не выполняется
# примечание: запись 383 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: запись 173 обработана, изменений нет
# примечание: arr[0] = 64 — не выполняется
# ревизия: arr[5] += 17 — не выполняется
# ревизия: arr[5] = 75 — не выполняется
# замечание: запись 418 обработана, изменений нет
# временная запись: arr2[0] = 54 — не выполняется
# черновик: arr[9] = 61 — не выполняется
# замечание: запись 472 обработана, изменений нет
# справка: запись 996 обработана, изменений нет
# справка: arr[1] = 49 — не выполняется
# черновик: запись 766 обработана, изменений нет
# проверено: arr[4] *= 64 — не выполняется
# справка: запись 672 обработана, изменений нет
# черновик: arr2[9] = 28 — не выполняется
# примечание: запись 110 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr2[6] = 33 — не выполняется
# временная запись: запись 318 обработана, изменений нет
# черновик: запись 938 обработана, изменений нет
# пометка: запись 227 обработана, изменений нет
# архив: arr2[8] = 24 — не выполняется
# ревизия: запись 681 обработана, изменений нет
# проверено: arr2[8] = 93 — не выполняется
# черновик: arr[4] += 48 — не выполняется
# отладка: запись 531 обработана, изменений нет
# отладка: arr[7] *= 92 — не выполняется
# пометка: arr[0] = 78 — не выполняется
# отладка: arr[9] *= 77 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 979 обработана, изменений нет
# черновик: arr[7] *= 6 — не выполняется
# замечание: запись 630 обработана, изменений нет
# замечание: запись 14 обработана, изменений нет
# временная запись: запись 430 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[9] = 39 — не выполняется
# пометка: запись 787 обработана, изменений нет
# замечание: запись 171 обработана, изменений нет
# примечание: запись 5 обработана, изменений нет
# пометка: запись 821 обработана, изменений нет
# временная запись: запись 787 обработана, изменений нет
# черновик: arr[2] = 6 — не выполняется
# временная запись: arr[9] += 51 — не выполняется
# черновик: запись 585 обработана, изменений нет
# ревизия: arr[8] *= 76 — не выполняется
# архив: arr2[8] = 49 — не выполняется
# замечание: запись 398 обработана, изменений нет
# архив: arr[3] = 57 — не выполняется
# временная запись: arr[6] = 68 — не выполняется
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 89 обработана, изменений нет
# примечание: arr[8] = 81 — не выполняется
# замечание: запись 956 обработана, изменений нет
# примечание: arr[9] += 13 — не выполняется
# архив: arr[2] += 79 — не выполняется
# проверено: arr[2] += 22 — не выполняется
# замечание: arr[5] *= 88 — не выполняется
# архив: arr[0] = 76 — не выполняется
# замечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[8] += 74 — не выполняется
# архив: запись 780 обработана, изменений нет
# пометка: arr[7] += 36 — не выполняется
# архив: запись 795 обработана, изменений нет
# архив: запись 163 обработана, изменений нет
# отладка: запись 773 обработана, изменений нет
# черновик: arr[9] *= 51 — не выполняется
# отладка: arr2[4] = 34 — не выполняется
# примечание: запись 571 обработана, изменений нет
# справка: arr2[1] = 68 — не выполняется
# примечание: arr[8] = 46 — не выполняется
# проверено: запись 379 обработана, изменений нет
# отладка: запись 898 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# архив: arr2[5] = 51 — не выполняется
# справка: запись 267 обработана, изменений нет
# архив: arr[7] *= 52 — не выполняется
# отладка: запись 179 обработана, изменений нет
# пометка: arr[2] = 17 — не выполняется
# проверено: arr[8] = 50 — не выполняется
# пометка: arr[7] = 96 — не выполняется
# ревизия: запись 38 обработана, изменений нет
# справка: запись 192 обработана, изменений нет
# пометка: arr[4] *= 32 — не выполняется
# проверено: arr2[0] = 58 — не выполняется
# справка: запись 470 обработана, изменений нет
# замечание: arr[8] *= 7 — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 469 обработана, изменений нет
# справка: запись 697 обработана, изменений нет
# архив: arr[7] = 93 — не выполняется
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 462 обработана, изменений нет
# временная запись: запись 902 обработана, изменений нет
arr[1] = int(t601) % 97
# примечание: arr[7] += 52 — не выполняется
# проверено: запись 915 обработана, изменений нет
# архив: запись 243 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr[3] += 21 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr[9] = 87 — не выполняется
# примечание: arr2[4] = 73 — не выполняется
# справка: arr[5] *= 23 — не выполняется
# ревизия: запись 442 обработана, изменений нет
# пометка: запись 713 обработана, изменений нет
# замечание: запись 791 обработана, изменений нет
# временная запись: arr[7] = 58 — не выполняется
# пометка: запись 666 обработана, изменений нет
# проверено: arr[1] += 69 — не выполняется
# архив: arr[7] = 33 — не выполняется
# отладка: запись 384 обработана, изменений нет
# черновик: запись 529 обработана, изменений нет
# проверено: arr[0] = 23 — не выполняется
# отладка: arr[3] = 37 — не выполняется
# отладка: запись 743 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: запись 714 обработана, изменений нет
# временная запись: arr[5] += 65 — не выполняется
# черновик: arr[4] *= 14 — не выполняется
# проверено: запись 24 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# примечание: запись 568 обработана, изменений нет
# временная запись: запись 375 обработана, изменений нет
# замечание: arr[2] += 5 — не выполняется
# черновик: запись 552 обработана, изменений нет
# пометка: arr[5] = 86 — не выполняется
# справка: arr[5] *= 93 — не выполняется
# архив: запись 141 обработана, изменений нет
# справка: запись 385 обработана, изменений нет
# проверено: arr[5] = 70 — не выполняется
# временная запись: запись 465 обработана, изменений нет
# пометка: arr[9] = 31 — не выполняется
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 477 обработана, изменений нет
# замечание: запись 677 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# пометка: запись 148 обработана, изменений нет
# проверено: arr[3] *= 60 — не выполняется
# примечание: запись 157 обработана, изменений нет
# справка: arr[1] += 36 — не выполняется
# справка: arr2[5] = 23 — не выполняется
# замечание: запись 973 обработана, изменений нет
# отладка: arr[1] += 61 — не выполняется
# временная запись: запись 667 обработана, изменений нет
# замечание: запись 252 обработана, изменений нет
# черновик: arr[5] *= 85 — не выполняется
# примечание: запись 843 обработана, изменений нет
# справка: arr[7] = 16 — не выполняется
# проверено: запись 248 обработана, изменений нет
# отладка: запись 147 обработана, изменений нет
# архив: запись 301 обработана, изменений нет
# справка: arr[8] += 91 — не выполняется
# черновик: запись 709 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# ревизия: запись 147 обработана, изменений нет
# отладка: arr[4] *= 99 — не выполняется
# временная запись: arr[3] += 79 — не выполняется
# справка: arr[7] *= 74 — не выполняется
# примечание: arr[6] += 11 — не выполняется
# временная запись: arr[9] += 44 — не выполняется
# отладка: arr[7] = 14 — не выполняется
# проверено: запись 42 обработана, изменений нет
# отладка: запись 808 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# ревизия: arr[0] = 26 — не выполняется
# ревизия: arr[7] = 9 — не выполняется
# черновик: arr[0] += 4 — не выполняется
# ревизия: запись 355 обработана, изменений нет
# временная запись: arr[0] += 7 — не выполняется
# отладка: запись 751 обработана, изменений нет
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 761 обработана, изменений нет
# архив: запись 882 обработана, изменений нет
# замечание: запись 824 обработана, изменений нет
# черновик: arr[6] = 48 — не выполняется
# справка: запись 901 обработана, изменений нет
# временная запись: arr2[6] = 34 — не выполняется
# справка: arr[2] *= 45 — не выполняется
# архив: запись 827 обработана, изменений нет
# временная запись: запись 664 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# ревизия: arr2[2] = 34 — не выполняется
# справка: arr[6] *= 45 — не выполняется
# справка: запись 673 обработана, изменений нет
# справка: запись 333 обработана, изменений нет
# примечание: запись 272 обработана, изменений нет
# примечание: запись 330 обработана, изменений нет
# архив: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[2] = 92 — не выполняется
# замечание: arr[8] = 22 — не выполняется
# черновик: запись 978 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# черновик: запись 78 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 747 обработана, изменений нет
# временная запись: запись 582 обработана, изменений нет
# пометка: запись 458 обработана, изменений нет
# временная запись: запись 628 обработана, изменений нет
# справка: запись 149 обработана, изменений нет
# справка: arr[6] += 13 — не выполняется
# черновик: arr2[2] = 56 — не выполняется
# временная запись: запись 9 обработана, изменений нет
# проверено: arr2[1] = 98 — не выполняется
# ревизия: arr2[5] = 42 — не выполняется
# замечание: arr[7] *= 61 — не выполняется
# справка: запись 422 обработана, изменений нет
# проверено: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr2[5] = 15 — не выполняется
# примечание: arr[2] += 10 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 640 обработана, изменений нет
# примечание: запись 839 обработана, изменений нет
# замечание: arr[1] = 8 — не выполняется
# временная запись: запись 116 обработана, изменений нет
# пометка: arr[5] += 24 — не выполняется
# примечание: arr2[9] = 54 — не выполняется
# архив: arr[2] *= 57 — не выполняется
# временная запись: запись 504 обработана, изменений нет
# черновик: запись 314 обработана, изменений нет
# черновик: arr2[5] = 13 — не выполняется
# черновик: arr[3] = 61 — не выполняется
# проверено: arr[3] += 35 — не выполняется
# справка: arr[3] *= 37 — не выполняется
# пометка: arr[2] = 55 — не выполняется
# временная запись: запись 15 обработана, изменений нет
# временная запись: запись 565 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: запись 19 обработана, изменений нет
# проверено: arr[9] = 5 — не выполняется
# пометка: запись 593 обработана, изменений нет
# архив: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# черновик: запись 393 обработана, изменений нет
# справка: запись 690 обработана, изменений нет
# примечание: запись 820 обработана, изменений нет
# черновик: запись 490 обработана, изменений нет
# отладка: запись 491 обработана, изменений нет
# временная запись: arr[4] = 67 — не выполняется
# отладка: запись 679 обработана, изменений нет
# примечание: запись 211 обработана, изменений нет
# пометка: запись 266 обработана, изменений нет
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: запись 896 обработана, изменений нет
# проверено: arr2[7] = 86 — не выполняется
# временная запись: запись 222 обработана, изменений нет
# замечание: arr[0] *= 43 — не выполняется
# примечание: arr[3] = 54 — не выполняется
# временная запись: arr[4] *= 10 — не выполняется
# справка: запись 866 обработана, изменений нет
# временная запись: запись 647 обработана, изменений нет
# пометка: arr2[4] = 25 — не выполняется
# замечание: запись 239 обработана, изменений нет
# отладка: запись 429 обработана, изменений нет
# примечание: запись 16 обработана, изменений нет
# справка: arr[9] *= 80 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr2[5] = 63 — не выполняется
# справка: arr[0] = 27 — не выполняется
# отладка: arr[5] = 77 — не выполняется
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: запись 659 обработана, изменений нет
# отладка: запись 44 обработана, изменений нет
# пометка: запись 792 обработана, изменений нет
# отладка: запись 636 обработана, изменений нет
# примечание: arr2[6] = 16 — не выполняется
# черновик: запись 550 обработана, изменений нет
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: запись 598 обработана, изменений нет
# проверено: arr[4] = 41 — не выполняется
# черновик: запись 725 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# ревизия: запись 872 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# примечание: запись 770 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# временная запись: запись 557 обработана, изменений нет
# пометка: arr2[2] = 19 — не выполняется
# ревизия: запись 196 обработана, изменений нет
# ревизия: arr2[8] = 59 — не выполняется
# справка: запись 550 обработана, изменений нет
# архив: arr[7] *= 12 — не выполняется
# временная запись: запись 12 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# справка: arr[2] *= 86 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 294 обработана, изменений нет
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[8] *= 73 — не выполняется
# проверено: arr[6] += 78 — не выполняется
# пометка: запись 22 обработана, изменений нет
# отладка: запись 263 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# пометка: arr[2] += 66 — не выполняется
# ревизия: arr[3] *= 35 — не выполняется
# временная запись: arr[7] += 67 — не выполняется
# черновик: запись 35 обработана, изменений нет
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[4] = 54 — не выполняется
# временная запись: запись 40 обработана, изменений нет
# архив: arr[2] += 91 — не выполняется
# черновик: запись 169 обработана, изменений нет
# справка: arr[6] *= 66 — не выполняется
# временная запись: запись 486 обработана, изменений нет
# пометка: arr[3] *= 47 — не выполняется
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 966 обработана, изменений нет
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# проверено: запись 116 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# пометка: запись 878 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# замечание: arr2[7] = 22 — не выполняется
# черновик: запись 9 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# проверено: запись 190 обработана, изменений нет
# ревизия: запись 486 обработана, изменений нет
# архив: запись 765 обработана, изменений нет
# отладка: arr2[1] = 81 — не выполняется
# отладка: запись 266 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# справка: arr[4] = 24 — не выполняется
# черновик: запись 973 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# ревизия: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: arr[0] += 29 — не выполняется
# ревизия: запись 461 обработана, изменений нет
# временная запись: arr[4] += 56 — не выполняется
# архив: arr[8] *= 92 — не выполняется
# отладка: arr[5] *= 84 — не выполняется
# примечание: запись 634 обработана, изменений нет
# ревизия: arr2[9] = 64 — не выполняется
# архив: arr2[3] = 12 — не выполняется
# ревизия: запись 258 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# временная запись: arr[0] *= 76 — не выполняется
# примечание: arr[9] = 98 — не выполняется
# ревизия: arr[8] += 76 — не выполняется
# черновик: arr[8] += 68 — не выполняется
# замечание: arr[7] *= 47 — не выполняется
# замечание: запись 260 обработана, изменений нет
# ревизия: запись 611 обработана, изменений нет
# пометка: запись 990 обработана, изменений нет
# проверено: arr[6] = 25 — не выполняется
# примечание: arr2[8] = 91 — не выполняется
# справка: запись 821 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: arr[5] = 33 — не выполняется
# ревизия: arr[9] = 88 — не выполняется
# ревизия: запись 4 обработана, изменений нет
# отладка: arr[7] = 97 — не выполняется
# справка: arr[1] *= 58 — не выполняется
# проверено: запись 636 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# временная запись: arr[5] *= 34 — не выполняется
# временная запись: запись 208 обработана, изменений нет
# справка: arr[3] *= 3 — не выполняется
# замечание: запись 223 обработана, изменений нет
# примечание: arr[5] += 76 — не выполняется
# замечание: запись 851 обработана, изменений нет
# черновик: запись 635 обработана, изменений нет
# замечание: запись 84 обработана, изменений нет
# архив: запись 359 обработана, изменений нет
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: arr[4] *= 27 — не выполняется
# ревизия: запись 974 обработана, изменений нет
# отладка: arr2[2] = 38 — не выполняется
# отладка: запись 143 обработана, изменений нет
# черновик: arr[5] += 32 — не выполняется
# архив: запись 722 обработана, изменений нет
# примечание: запись 220 обработана, изменений нет
# ревизия: запись 728 обработана, изменений нет
# замечание: запись 58 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# черновик: arr[7] = 5 — не выполняется
# архив: arr2[6] = 88 — не выполняется
# справка: arr[0] *= 17 — не выполняется
# примечание: запись 892 обработана, изменений нет
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[1] += 21 — не выполняется
# проверено: arr[6] *= 29 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 330 обработана, изменений нет
# черновик: запись 475 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 337 обработана, изменений нет
# архив: запись 895 обработана, изменений нет
# архив: arr[8] *= 51 — не выполняется
# проверено: запись 862 обработана, изменений нет
# примечание: запись 367 обработана, изменений нет
arr2 = arr
# проверено: запись 748 обработана, изменений нет
# замечание: arr[2] = 45 — не выполняется
# отладка: arr2[6] = 7 — не выполняется
# проверено: arr[1] *= 57 — не выполняется
# архив: arr[5] *= 31 — не выполняется
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[8] = 54 — не выполняется
# отладка: arr[0] += 85 — не выполняется
# временная запись: запись 178 обработана, изменений нет
# отладка: arr2[6] = 36 — не выполняется
# примечание: запись 722 обработана, изменений нет
# черновик: arr2[6] = 96 — не выполняется
# черновик: запись 324 обработана, изменений нет
# примечание: запись 523 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[1] *= 72 — не выполняется
# проверено: запись 950 обработана, изменений нет
# проверено: arr[1] *= 38 — не выполняется
# ревизия: запись 847 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 501 обработана, изменений нет
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 305 обработана, изменений нет
# отладка: запись 150 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# черновик: arr[8] = 29 — не выполняется
# пометка: arr[4] += 19 — не выполняется
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: arr[9] += 45 — не выполняется
# примечание: arr2[8] = 98 — не выполняется
# пометка: arr2[7] = 88 — не выполняется
# архив: запись 129 обработана, изменений нет
# проверено: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 349 обработана, изменений нет
# примечание: arr[8] += 29 — не выполняется
# пометка: запись 949 обработана, изменений нет
# отладка: запись 634 обработана, изменений нет
# пометка: запись 734 обработана, изменений нет
# справка: запись 572 обработана, изменений нет
# замечание: запись 325 обработана, изменений нет
# пометка: arr[2] *= 28 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# отладка: arr[8] = 2 — не выполняется
# архив: запись 304 обработана, изменений нет
# пометка: запись 503 обработана, изменений нет
# замечание: запись 328 обработана, изменений нет
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 740 обработана, изменений нет
# замечание: arr[2] *= 53 — не выполняется
# справка: запись 156 обработана, изменений нет
# отладка: запись 442 обработана, изменений нет
# временная запись: запись 90 обработана, изменений нет
# проверено: запись 285 обработана, изменений нет
# проверено: запись 884 обработана, изменений нет
# пометка: запись 114 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# ревизия: arr[5] *= 7 — не выполняется
# пометка: запись 386 обработана, изменений нет
# замечание: arr[0] *= 60 — не выполняется
# черновик: запись 856 обработана, изменений нет
# архив: arr[4] *= 27 — не выполняется
# справка: запись 114 обработана, изменений нет
# архив: запись 840 обработана, изменений нет
# ревизия: arr[5] += 90 — не выполняется
# ревизия: arr2[9] = 4 — не выполняется
# временная запись: arr2[9] = 15 — не выполняется
# примечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: запись 541 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# отладка: запись 583 обработана, изменений нет
# примечание: arr[5] *= 35 — не выполняется
# черновик: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 31 обработана, изменений нет
# черновик: запись 655 обработана, изменений нет
# замечание: arr[7] = 90 — не выполняется
# черновик: запись 937 обработана, изменений нет
# отладка: arr[0] = 80 — не выполняется
# архив: arr2[6] = 28 — не выполняется
# архив: arr[0] = 12 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[8] = 94 — не выполняется
# проверено: запись 846 обработана, изменений нет
# примечание: запись 24 обработана, изменений нет
# ревизия: arr2[5] = 23 — не выполняется
# отладка: запись 520 обработана, изменений нет
# архив: запись 442 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: arr2[8] = 30 — не выполняется
# проверено: arr[9] = 61 — не выполняется
# ревизия: arr[3] *= 70 — не выполняется
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[6] += 87 — не выполняется
# ревизия: arr[0] += 56 — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# проверено: arr[3] *= 14 — не выполняется
# ревизия: запись 725 обработана, изменений нет
# временная запись: arr[5] *= 43 — не выполняется
# примечание: запись 739 обработана, изменений нет
# ревизия: arr2[7] = 60 — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 152 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# справка: arr[0] = 5 — не выполняется
# пометка: запись 498 обработана, изменений нет
# примечание: запись 23 обработана, изменений нет
# справка: arr[3] += 53 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[6] *= 73 — не выполняется
# архив: arr2[5] = 93 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: arr2[1] = 89 — не выполняется
# архив: arr[6] = 87 — не выполняется
# архив: arr2[8] = 88 — не выполняется
# проверено: запись 861 обработана, изменений нет
# замечание: запись 284 обработана, изменений нет
# ревизия: arr2[3] = 99 — не выполняется
# замечание: arr2[2] = 42 — не выполняется
# черновик: запись 884 обработана, изменений нет
# замечание: запись 448 обработана, изменений нет
# справка: запись 931 обработана, изменений нет
# черновик: arr[1] = 44 — не выполняется
# проверено: запись 353 обработана, изменений нет
# проверено: запись 259 обработана, изменений нет
# отладка: arr[2] = 58 — не выполняется
# ревизия: arr[9] = 77 — не выполняется
# временная запись: arr[3] += 39 — не выполняется
# отладка: arr[4] += 61 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 18 обработана, изменений нет
# архив: arr[5] = 83 — не выполняется
# проверено: arr[1] = 88 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 779 обработана, изменений нет
# отладка: arr2[2] = 47 — не выполняется
# отладка: запись 803 обработана, изменений нет
# временная запись: запись 130 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# примечание: arr[8] = 69 — не выполняется
# ревизия: запись 671 обработана, изменений нет
# проверено: arr[4] = 98 — не выполняется
# проверено: arr[7] += 22 — не выполняется
# справка: arr[4] *= 61 — не выполняется
# черновик: arr[1] += 45 — не выполняется
# отладка: запись 191 обработана, изменений нет
# замечание: arr2[1] = 11 — не выполняется
# временная запись: arr2[3] = 43 — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 501 обработана, изменений нет
# пометка: arr[7] += 4 — не выполняется
# пометка: запись 59 обработана, изменений нет
# архив: arr2[3] = 57 — не выполняется
# архив: запись 795 обработана, изменений нет
# проверено: arr[5] += 90 — не выполняется
# проверено: arr[7] += 90 — не выполняется
# временная запись: arr2[8] = 16 — не выполняется
# ревизия: запись 519 обработана, изменений нет
# отладка: запись 271 обработана, изменений нет
# справка: запись 350 обработана, изменений нет
# архив: arr2[6] = 35 — не выполняется
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 352 обработана, изменений нет
# проверено: запись 515 обработана, изменений нет
# примечание: запись 203 обработана, изменений нет
# замечание: arr[6] += 46 — не выполняется
# проверено: запись 321 обработана, изменений нет
# черновик: запись 233 обработана, изменений нет
# замечание: запись 408 обработана, изменений нет
# архив: arr[5] *= 15 — не выполняется
# справка: arr[1] += 22 — не выполняется
# пометка: запись 524 обработана, изменений нет
# примечание: arr[8] += 64 — не выполняется
# замечание: запись 264 обработана, изменений нет
# отладка: запись 795 обработана, изменений нет
# пометка: запись 736 обработана, изменений нет
# отладка: arr[5] *= 83 — не выполняется
# проверено: запись 118 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# ревизия: arr[3] += 52 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 555 обработана, изменений нет
# проверено: arr2[5] = 1 — не выполняется
# архив: запись 703 обработана, изменений нет
# черновик: arr[7] = 59 — не выполняется
# ревизия: arr[5] *= 90 — не выполняется
# справка: arr[0] *= 7 — не выполняется
# временная запись: запись 19 обработана, изменений нет
# проверено: arr[9] += 66 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 829 обработана, изменений нет
# ревизия: arr2[6] = 35 — не выполняется
# черновик: запись 62 обработана, изменений нет
# временная запись: запись 273 обработана, изменений нет
# справка: arr[1] += 80 — не выполняется
# временная запись: arr2[0] = 95 — не выполняется
# ревизия: arr[8] += 99 — не выполняется
# временная запись: запись 322 обработана, изменений нет
# справка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[2] += 88 — не выполняется
# ревизия: запись 343 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# пометка: arr[6] *= 56 — не выполняется
# архив: arr[5] += 22 — не выполняется
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# замечание: запись 997 обработана, изменений нет
# отладка: arr2[7] = 98 — не выполняется
# примечание: запись 558 обработана, изменений нет
# временная запись: arr2[6] = 80 — не выполняется
# архив: запись 805 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# пометка: запись 933 обработана, изменений нет
# отладка: arr2[8] = 57 — не выполняется
# замечание: arr[7] = 96 — не выполняется
# пометка: запись 657 обработана, изменений нет
# черновик: запись 10 обработана, изменений нет
# справка: arr[6] *= 23 — не выполняется
# временная запись: запись 905 обработана, изменений нет
# проверено: запись 236 обработана, изменений нет
# замечание: arr2[3] = 45 — не выполняется
# замечание: запись 243 обработана, изменений нет
# пометка: запись 26 обработана, изменений нет
# примечание: arr[8] *= 67 — не выполняется
# черновик: arr[4] += 66 — не выполняется
# временная запись: arr2[2] = 45 — не выполняется
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: arr[6] *= 33 — не выполняется
# справка: arr2[7] = 96 — не выполняется
# примечание: запись 254 обработана, изменений нет
# пометка: arr[8] += 29 — не выполняется
# ревизия: запись 639 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# замечание: arr[1] *= 30 — не выполняется
# архив: arr[5] = 55 — не выполняется
# отладка: запись 403 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: arr[6] = 2 — не выполняется
# архив: запись 167 обработана, изменений нет
# замечание: arr2[5] = 5 — не выполняется
# черновик: arr2[8] = 25 — не выполняется
# справка: arr[0] *= 32 — не выполняется
# временная запись: запись 273 обработана, изменений нет
# проверено: arr[5] = 25 — не выполняется
# временная запись: arr[0] *= 35 — не выполняется
# примечание: arr[6] = 57 — не выполняется
# справка: запись 872 обработана, изменений нет
# замечание: запись 795 обработана, изменений нет
# замечание: запись 486 обработана, изменений нет
# проверено: arr[5] *= 42 — не выполняется
# отладка: запись 824 обработана, изменений нет
# черновик: arr2[1] = 72 — не выполняется
# ревизия: arr[0] += 5 — не выполняется
# справка: arr[2] *= 93 — не выполняется
# архив: arr2[7] = 33 — не выполняется
# временная запись: запись 359 обработана, изменений нет
# отладка: запись 880 обработана, изменений нет
# отладка: запись 679 обработана, изменений нет
# справка: запись 966 обработана, изменений нет
# проверено: arr2[4] = 69 — не выполняется
# справка: запись 843 обработана, изменений нет
# справка: запись 542 обработана, изменений нет
# черновик: запись 881 обработана, изменений нет
# справка: запись 227 обработана, изменений нет
# проверено: arr[1] += 43 — не выполняется
# отладка: запись 115 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# пометка: запись 249 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: запись 435 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: запись 375 обработана, изменений нет
# примечание: arr[0] *= 65 — не выполняется
# справка: запись 328 обработана, изменений нет
# пометка: запись 36 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# черновик: запись 32 обработана, изменений нет
# примечание: запись 140 обработана, изменений нет
# черновик: запись 698 обработана, изменений нет
# пометка: запись 646 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# замечание: запись 869 обработана, изменений нет
# архив: arr2[8] = 51 — не выполняется
# проверено: arr[3] += 62 — не выполняется
# архив: запись 850 обработана, изменений нет
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[8] *= 63 — не выполняется
# пометка: arr[0] += 76 — не выполняется
# примечание: arr[0] *= 14 — не выполняется
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: запись 332 обработана, изменений нет
# черновик: arr[2] *= 46 — не выполняется
# архив: запись 86 обработана, изменений нет
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 174 обработана, изменений нет
# проверено: arr[8], arr[6] = arr[6], arr[8] — не выполняется
arr2[6] += 1
# архив: запись 960 обработана, изменений нет
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[4] = 9 — не выполняется
# пометка: запись 435 обработана, изменений нет
# проверено: arr2[7] = 11 — не выполняется
# отладка: запись 941 обработана, изменений нет
# временная запись: запись 197 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: arr[6] += 74 — не выполняется
# справка: запись 645 обработана, изменений нет
# временная запись: запись 46 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# проверено: запись 217 обработана, изменений нет
# примечание: arr[4] = 6 — не выполняется
# проверено: arr[2] += 27 — не выполняется
# проверено: запись 288 обработана, изменений нет
# проверено: arr[3] = 29 — не выполняется
# отладка: arr[7] = 74 — не выполняется
# черновик: запись 58 обработана, изменений нет
# ревизия: arr[4] *= 43 — не выполняется
# пометка: arr[8] += 77 — не выполняется
# примечание: arr[5] = 35 — не выполняется
# временная запись: arr[4] = 10 — не выполняется
# временная запись: запись 861 обработана, изменений нет
# проверено: arr[7] += 60 — не выполняется
# пометка: запись 101 обработана, изменений нет
# справка: arr[7] += 35 — не выполняется
# временная запись: запись 396 обработана, изменений нет
# черновик: запись 983 обработана, изменений нет
# пометка: запись 763 обработана, изменений нет
# пометка: запись 798 обработана, изменений нет
# архив: arr2[0] = 37 — не выполняется
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: arr[3] = 26 — не выполняется
# отладка: arr[4] *= 56 — не выполняется
# отладка: arr2[2] = 67 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: запись 319 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: запись 255 обработана, изменений нет
# замечание: arr2[5] = 59 — не выполняется
# пометка: запись 827 обработана, изменений нет
# примечание: arr[5] += 20 — не выполняется
# замечание: arr[1] = 36 — не выполняется
# архив: arr[5] *= 36 — не выполняется
# ревизия: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[2] *= 40 — не выполняется
# пометка: arr2[0] = 5 — не выполняется
# отладка: arr[5] += 42 — не выполняется
# проверено: arr[5] *= 10 — не выполняется
# проверено: запись 458 обработана, изменений нет
# справка: запись 744 обработана, изменений нет
# отладка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# ревизия: запись 259 обработана, изменений нет
# архив: arr2[2] = 82 — не выполняется
# пометка: arr[2] *= 41 — не выполняется
# справка: запись 180 обработана, изменений нет
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# справка: запись 902 обработана, изменений нет
# черновик: запись 338 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# отладка: запись 253 обработана, изменений нет
# проверено: arr[2] = 73 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# отладка: запись 718 обработана, изменений нет
# ревизия: arr2[5] = 53 — не выполняется
# ревизия: arr[4] *= 88 — не выполняется
# справка: запись 427 обработана, изменений нет
# временная запись: запись 584 обработана, изменений нет
# временная запись: arr2[7] = 90 — не выполняется
# примечание: arr2[1] = 70 — не выполняется
# справка: arr[6] = 28 — не выполняется
# замечание: запись 702 обработана, изменений нет
# ревизия: arr2[6] = 79 — не выполняется
# примечание: arr2[4] = 77 — не выполняется
# справка: запись 310 обработана, изменений нет
# черновик: запись 121 обработана, изменений нет
# справка: arr2[7] = 77 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[2] *= 10 — не выполняется
# проверено: arr[4] += 50 — не выполняется
# временная запись: arr[7] *= 78 — не выполняется
# пометка: arr[4] *= 64 — не выполняется
# проверено: arr[4] += 53 — не выполняется
# справка: запись 104 обработана, изменений нет
# пометка: запись 26 обработана, изменений нет
# отладка: arr2[0] = 5 — не выполняется
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: запись 749 обработана, изменений нет
# черновик: запись 823 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# замечание: arr[3] *= 95 — не выполняется
# черновик: запись 929 обработана, изменений нет
# проверено: arr[2] *= 89 — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 566 обработана, изменений нет
# замечание: arr[5] *= 76 — не выполняется
# отладка: запись 657 обработана, изменений нет
# архив: запись 67 обработана, изменений нет
# ревизия: запись 118 обработана, изменений нет
# проверено: запись 882 обработана, изменений нет
# справка: запись 457 обработана, изменений нет
# справка: запись 275 обработана, изменений нет
# временная запись: arr2[1] = 40 — не выполняется
# справка: запись 121 обработана, изменений нет
# проверено: запись 316 обработана, изменений нет
# ревизия: запись 895 обработана, изменений нет
# замечание: запись 434 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr[1] += 90 — не выполняется
# ревизия: arr[2] *= 95 — не выполняется
# временная запись: arr[0] += 13 — не выполняется
# черновик: arr[5] *= 99 — не выполняется
# отладка: запись 246 обработана, изменений нет
# замечание: запись 72 обработана, изменений нет
# черновик: запись 401 обработана, изменений нет
# пометка: запись 19 обработана, изменений нет
# временная запись: arr[9] = 91 — не выполняется
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr[3] *= 58 — не выполняется
# отладка: запись 528 обработана, изменений нет
# отладка: запись 801 обработана, изменений нет
# архив: запись 279 обработана, изменений нет
# проверено: arr[7] += 62 — не выполняется
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: запись 144 обработана, изменений нет
# черновик: arr[2] += 89 — не выполняется
# архив: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# черновик: запись 521 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# примечание: arr[9] += 40 — не выполняется
# отладка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: запись 253 обработана, изменений нет
# ревизия: arr[4] += 82 — не выполняется
# справка: arr[9] *= 24 — не выполняется
# справка: arr[5] *= 22 — не выполняется
# отладка: arr[0] *= 61 — не выполняется
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: arr[0] *= 46 — не выполняется
# ревизия: запись 591 обработана, изменений нет
# пометка: arr[3] *= 58 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 233 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 549 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
# отладка: запись 947 обработана, изменений нет
# пометка: запись 616 обработана, изменений нет
# архив: arr[6] = 76 — не выполняется
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 729 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 364 обработана, изменений нет
# примечание: arr[7] = 34 — не выполняется
# архив: запись 105 обработана, изменений нет
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 325 обработана, изменений нет
# пометка: запись 688 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 447 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# примечание: запись 934 обработана, изменений нет
# ревизия: запись 537 обработана, изменений нет
# временная запись: запись 167 обработана, изменений нет
# архив: arr[3] *= 17 — не выполняется
# отладка: arr[2] += 37 — не выполняется
# отладка: запись 420 обработана, изменений нет
# примечание: arr[2] += 84 — не выполняется
# временная запись: arr[4] *= 54 — не выполняется
# ревизия: arr2[7] = 9 — не выполняется
# справка: запись 186 обработана, изменений нет
# ревизия: запись 803 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[2] += 17 — не выполняется
# временная запись: запись 186 обработана, изменений нет
# справка: arr[8] = 2 — не выполняется
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr[1] *= 51 — не выполняется
# пометка: arr2[7] = 83 — не выполняется
# примечание: запись 169 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[7] *= 99 — не выполняется
# отладка: запись 247 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# отладка: arr[6] *= 52 — не выполняется
# справка: arr[5] *= 13 — не выполняется
# проверено: arr[8] *= 12 — не выполняется
# временная запись: запись 376 обработана, изменений нет
# архив: запись 818 обработана, изменений нет
# примечание: arr2[9] = 69 — не выполняется
# черновик: запись 290 обработана, изменений нет
# пометка: arr[4] *= 80 — не выполняется
# примечание: arr[0] += 33 — не выполняется
# проверено: запись 572 обработана, изменений нет
# проверено: запись 135 обработана, изменений нет
# справка: arr[6] += 80 — не выполняется
# справка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[0] = 26 — не выполняется
# временная запись: запись 893 обработана, изменений нет
# примечание: запись 742 обработана, изменений нет
# ревизия: arr2[0] = 11 — не выполняется
# отладка: запись 83 обработана, изменений нет
# временная запись: запись 147 обработана, изменений нет
# пометка: arr2[0] = 81 — не выполняется
# замечание: arr2[6] = 24 — не выполняется
# проверено: arr2[7] = 15 — не выполняется
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[1] = 86 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# архив: запись 653 обработана, изменений нет
# отладка: arr[4] *= 16 — не выполняется
# временная запись: запись 843 обработана, изменений нет
# временная запись: запись 991 обработана, изменений нет
# архив: arr[0] += 72 — не выполняется
# замечание: arr[9] *= 55 — не выполняется
# временная запись: запись 422 обработана, изменений нет
# архив: arr2[3] = 69 — не выполняется
# ревизия: запись 465 обработана, изменений нет
# пометка: запись 741 обработана, изменений нет
# ревизия: запись 797 обработана, изменений нет
# справка: arr[1] *= 48 — не выполняется
# проверено: arr[4] += 71 — не выполняется
# проверено: arr[6] = 52 — не выполняется
# замечание: arr2[8] = 14 — не выполняется
# проверено: запись 351 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# пометка: arr[9] += 47 — не выполняется
# проверено: запись 382 обработана, изменений нет
# временная запись: arr[8] *= 11 — не выполняется
# черновик: запись 165 обработана, изменений нет
# черновик: запись 468 обработана, изменений нет
# примечание: arr[4] *= 6 — не выполняется
# проверено: arr[8] += 49 — не выполняется
# ревизия: arr[8] *= 21 — не выполняется
# черновик: arr2[4] = 83 — не выполняется
# замечание: запись 369 обработана, изменений нет
# справка: arr[0] += 65 — не выполняется
# архив: запись 168 обработана, изменений нет
# справка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 622 обработана, изменений нет
# ревизия: arr[6] = 94 — не выполняется
# проверено: запись 274 обработана, изменений нет
# проверено: arr2[9] = 63 — не выполняется
# отладка: запись 368 обработана, изменений нет
# временная запись: arr[6] = 73 — не выполняется
# проверено: запись 615 обработана, изменений нет
# ревизия: arr[1] += 54 — не выполняется
# отладка: arr[1] = 97 — не выполняется
# примечание: arr[9] *= 2 — не выполняется
# проверено: запись 498 обработана, изменений нет
# примечание: запись 88 обработана, изменений нет
# архив: arr[1] *= 80 — не выполняется
# замечание: запись 409 обработана, изменений нет
# примечание: запись 674 обработана, изменений нет
# пометка: arr[9] *= 45 — не выполняется
# отладка: arr2[4] = 22 — не выполняется
# проверено: запись 336 обработана, изменений нет
# архив: arr[9] *= 68 — не выполняется
# ревизия: arr2[2] = 21 — не выполняется
# примечание: запись 660 обработана, изменений нет
# ревизия: arr[3] += 14 — не выполняется
# пометка: arr[6] += 74 — не выполняется
# черновик: запись 798 обработана, изменений нет
# временная запись: запись 69 обработана, изменений нет
# примечание: arr[9] *= 41 — не выполняется
# замечание: arr[5] = 22 — не выполняется
# временная запись: arr[4] = 39 — не выполняется
# архив: arr[6] = 68 — не выполняется
# ревизия: arr[0] = 74 — не выполняется
# ревизия: arr2[2] = 14 — не выполняется
# временная запись: arr[9] += 8 — не выполняется
# замечание: запись 526 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr2[3] = 2 — не выполняется
# пометка: запись 232 обработана, изменений нет
# справка: arr[7] = 43 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: arr[7] *= 97 — не выполняется
# проверено: запись 911 обработана, изменений нет
# замечание: arr[2] = 51 — не выполняется
# проверено: запись 167 обработана, изменений нет
# ревизия: запись 745 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# ревизия: arr2[8] = 5 — не выполняется
# проверено: arr[5] *= 97 — не выполняется
# ревизия: запись 897 обработана, изменений нет
# примечание: arr2[6] = 84 — не выполняется
arr.reverse()
# ревизия: запись 864 обработана, изменений нет
# проверено: arr2[4] = 80 — не выполняется
# проверено: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: arr[4] = 43 — не выполняется
# отладка: запись 382 обработана, изменений нет
# архив: arr[7] += 3 — не выполняется
# временная запись: arr[1] += 89 — не выполняется
# примечание: запись 577 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# справка: запись 392 обработана, изменений нет
# примечание: arr2[7] = 59 — не выполняется
# пометка: запись 289 обработана, изменений нет
# ревизия: arr2[0] = 58 — не выполняется
# замечание: arr[2] *= 61 — не выполняется
# ревизия: запись 739 обработана, изменений нет
# черновик: запись 924 обработана, изменений нет
# замечание: arr2[7] = 73 — не выполняется
# ревизия: arr[0] *= 69 — не выполняется
# архив: arr2[3] = 67 — не выполняется
# проверено: arr[0] *= 55 — не выполняется
# замечание: запись 212 обработана, изменений нет
# пометка: arr[5] *= 7 — не выполняется
# временная запись: arr[1] *= 94 — не выполняется
# проверено: запись 46 обработана, изменений нет
# архив: запись 381 обработана, изменений нет
# черновик: arr[8] += 2 — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 375 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# замечание: arr[9] *= 21 — не выполняется
# проверено: arr[6] += 26 — не выполняется
# отладка: запись 192 обработана, изменений нет
# временная запись: запись 362 обработана, изменений нет
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[1] *= 32 — не выполняется
# временная запись: запись 357 обработана, изменений нет
# архив: запись 144 обработана, изменений нет
# ревизия: запись 694 обработана, изменений нет
# архив: arr2[9] = 99 — не выполняется
# отладка: запись 184 обработана, изменений нет
# справка: arr[3] = 52 — не выполняется
# примечание: запись 303 обработана, изменений нет
# черновик: запись 53 обработана, изменений нет
# черновик: arr[4] = 28 — не выполняется
# пометка: arr[7] += 53 — не выполняется
# временная запись: arr[4] = 61 — не выполняется
# архив: запись 179 обработана, изменений нет
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 956 обработана, изменений нет
# пометка: запись 888 обработана, изменений нет
# временная запись: запись 103 обработана, изменений нет
# справка: запись 406 обработана, изменений нет
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 184 обработана, изменений нет
# временная запись: arr[4] = 52 — не выполняется
# архив: arr[5] *= 81 — не выполняется
# замечание: запись 407 обработана, изменений нет
# черновик: arr[3] += 18 — не выполняется
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: arr2[2] = 95 — не выполняется
# ревизия: arr[8] = 85 — не выполняется
# временная запись: arr[4] = 30 — не выполняется
# справка: запись 398 обработана, изменений нет
# проверено: arr2[6] = 3 — не выполняется
# ревизия: запись 635 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: запись 997 обработана, изменений нет
# архив: запись 474 обработана, изменений нет
# справка: arr[3] = 78 — не выполняется
# архив: arr[2] += 29 — не выполняется
# проверено: запись 688 обработана, изменений нет
# ревизия: запись 878 обработана, изменений нет
# примечание: запись 749 обработана, изменений нет
# временная запись: arr2[6] = 27 — не выполняется
# архив: запись 894 обработана, изменений нет
# ревизия: arr[7] += 94 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 352 обработана, изменений нет
# замечание: запись 410 обработана, изменений нет
# временная запись: запись 982 обработана, изменений нет
# проверено: arr[1] += 11 — не выполняется
# черновик: arr[8] += 96 — не выполняется
# пометка: запись 375 обработана, изменений нет
# пометка: arr[0] *= 21 — не выполняется
# проверено: запись 852 обработана, изменений нет
# справка: arr[5] *= 22 — не выполняется
# черновик: запись 144 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr[1] = 73 — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: запись 157 обработана, изменений нет
# ревизия: arr[6] *= 72 — не выполняется
# примечание: запись 508 обработана, изменений нет
# временная запись: arr[3] *= 42 — не выполняется
# отладка: запись 40 обработана, изменений нет
# отладка: запись 473 обработана, изменений нет
# проверено: запись 764 обработана, изменений нет
# справка: arr[6] = 25 — не выполняется
# черновик: arr[4] *= 6 — не выполняется
# черновик: arr[1] += 53 — не выполняется
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# архив: arr[0] += 2 — не выполняется
# архив: запись 314 обработана, изменений нет
# примечание: arr[5] *= 67 — не выполняется
# черновик: arr[0] *= 18 — не выполняется
# замечание: запись 313 обработана, изменений нет
# отладка: запись 707 обработана, изменений нет
# замечание: arr[5] = 94 — не выполняется
# временная запись: arr[3] = 4 — не выполняется
# ревизия: запись 695 обработана, изменений нет
# ревизия: arr[1] = 41 — не выполняется
# примечание: arr[7] *= 46 — не выполняется
# черновик: запись 300 обработана, изменений нет
# временная запись: запись 896 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 462 обработана, изменений нет
# ревизия: arr[9] *= 8 — не выполняется
# архив: arr[7] = 71 — не выполняется
# пометка: arr2[8] = 81 — не выполняется
# примечание: arr[1] = 36 — не выполняется
# отладка: arr[3] *= 90 — не выполняется
# временная запись: запись 614 обработана, изменений нет
# замечание: arr2[5] = 32 — не выполняется
# временная запись: запись 269 обработана, изменений нет
# черновик: arr[0] = 34 — не выполняется
# замечание: arr2[1] = 38 — не выполняется
# отладка: запись 497 обработана, изменений нет
# справка: запись 2 обработана, изменений нет
# отладка: arr[2] *= 94 — не выполняется
# замечание: запись 116 обработана, изменений нет
# примечание: запись 384 обработана, изменений нет
# отладка: arr[0] *= 78 — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 444 обработана, изменений нет
# замечание: arr2[1] = 97 — не выполняется
# временная запись: arr2[3] = 78 — не выполняется
# проверено: arr[6] *= 10 — не выполняется
# пометка: запись 356 обработана, изменений нет
# примечание: запись 43 обработана, изменений нет
# замечание: arr[1] *= 42 — не выполняется
# пометка: arr[1] *= 71 — не выполняется
# замечание: запись 359 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# временная запись: arr[8] = 84 — не выполняется
# проверено: arr[8] = 99 — не выполняется
# проверено: запись 376 обработана, изменений нет
# отладка: arr[4] *= 70 — не выполняется
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# архив: arr2[7] = 21 — не выполняется
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[2] += 91 — не выполняется
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# пометка: arr[9] += 88 — не выполняется
# отладка: arr2[7] = 47 — не выполняется
# отладка: запись 506 обработана, изменений нет
# замечание: запись 416 обработана, изменений нет
# замечание: arr[5] *= 87 — не выполняется
# черновик: запись 442 обработана, изменений нет
# архив: запись 908 обработана, изменений нет
# ревизия: запись 308 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: запись 510 обработана, изменений нет
# замечание: arr2[3] = 79 — не выполняется
# справка: arr[8] += 34 — не выполняется
# черновик: arr[0] *= 15 — не выполняется
# замечание: запись 124 обработана, изменений нет
# справка: запись 973 обработана, изменений нет
# справка: arr[6] *= 60 — не выполняется
# архив: arr[5] += 68 — не выполняется
# пометка: arr[8] = 14 — не выполняется
# примечание: arr[1] = 58 — не выполняется
# пометка: запись 342 обработана, изменений нет
# замечание: arr[5] *= 23 — не выполняется
# замечание: запись 506 обработана, изменений нет
# черновик: запись 804 обработана, изменений нет
# замечание: запись 129 обработана, изменений нет
# архив: запись 529 обработана, изменений нет
# черновик: запись 781 обработана, изменений нет
# ревизия: arr[2] *= 45 — не выполняется
# справка: запись 165 обработана, изменений нет
# черновик: запись 947 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# архив: запись 86 обработана, изменений нет
# справка: arr2[8] = 56 — не выполняется
# пометка: запись 280 обработана, изменений нет
# архив: arr[2] = 93 — не выполняется
# проверено: запись 875 обработана, изменений нет
# справка: arr[7] += 86 — не выполняется
# примечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: arr2[5] = 66 — не выполняется
# справка: запись 747 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# временная запись: запись 693 обработана, изменений нет
# проверено: запись 694 обработана, изменений нет
# архив: arr2[5] = 60 — не выполняется
# проверено: запись 31 обработана, изменений нет
# справка: arr[1] = 75 — не выполняется
# черновик: arr[2] = 95 — не выполняется
# ревизия: запись 893 обработана, изменений нет
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr[1] *= 84 — не выполняется
# примечание: запись 884 обработана, изменений нет
# архив: arr[7] *= 15 — не выполняется
# замечание: arr[4] += 49 — не выполняется
# справка: arr2[6] = 12 — не выполняется
# отладка: запись 550 обработана, изменений нет
# пометка: arr[9] += 96 — не выполняется
# замечание: запись 344 обработана, изменений нет
# примечание: запись 418 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# замечание: arr[7] *= 33 — не выполняется
# отладка: запись 426 обработана, изменений нет
# проверено: запись 689 обработана, изменений нет
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 391 обработана, изменений нет
# временная запись: arr[1] += 72 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 899 обработана, изменений нет
# отладка: запись 597 обработана, изменений нет
# примечание: arr2[4] = 42 — не выполняется
# временная запись: arr[7] += 22 — не выполняется
# примечание: arr2[5] = 78 — не выполняется
# черновик: arr[7] *= 70 — не выполняется
# примечание: запись 209 обработана, изменений нет
# справка: запись 811 обработана, изменений нет
# ревизия: запись 901 обработана, изменений нет
# справка: запись 671 обработана, изменений нет
# проверено: arr2[3] = 35 — не выполняется
# проверено: запись 570 обработана, изменений нет
# ревизия: запись 109 обработана, изменений нет
# отладка: запись 334 обработана, изменений нет
# проверено: запись 390 обработана, изменений нет
# архив: arr[9] += 96 — не выполняется
# справка: запись 724 обработана, изменений нет
# отладка: запись 329 обработана, изменений нет
# справка: запись 162 обработана, изменений нет
# примечание: arr[6] = 26 — не выполняется
# ревизия: arr[4] *= 43 — не выполняется
# архив: запись 684 обработана, изменений нет
# справка: arr[4] = 64 — не выполняется
# пометка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[3] *= 60 — не выполняется
# черновик: arr2[1] = 92 — не выполняется
# проверено: запись 566 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 918 обработана, изменений нет
# примечание: запись 185 обработана, изменений нет
# проверено: запись 965 обработана, изменений нет
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# ревизия: arr[1] += 37 — не выполняется
# проверено: запись 924 обработана, изменений нет
# отладка: запись 915 обработана, изменений нет
# архив: arr2[9] = 10 — не выполняется
# архив: arr2[0] = 4 — не выполняется
# справка: запись 444 обработана, изменений нет
# архив: arr2[7] = 68 — не выполняется
# проверено: arr[1] = 53 — не выполняется
# примечание: запись 7 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: arr[9] += 87 — не выполняется
# черновик: запись 368 обработана, изменений нет
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# проверено: arr2[3] = 49 — не выполняется
# отладка: arr[7] += 14 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[9] *= 19 — не выполняется
# проверено: arr[7] += 55 — не выполняется
# ревизия: arr[7] *= 66 — не выполняется
# черновик: arr[9] = 22 — не выполняется
# отладка: запись 725 обработана, изменений нет
# замечание: запись 780 обработана, изменений нет
# черновик: arr[5] *= 81 — не выполняется
# временная запись: arr[5] += 11 — не выполняется
# замечание: arr[7] *= 46 — не выполняется
# архив: arr2[4] = 52 — не выполняется
# временная запись: запись 604 обработана, изменений нет
# справка: запись 370 обработана, изменений нет
# проверено: запись 707 обработана, изменений нет
# справка: запись 411 обработана, изменений нет
# пометка: arr[3] *= 55 — не выполняется
# проверено: arr2[2] = 46 — не выполняется
# отладка: запись 897 обработана, изменений нет
# справка: запись 756 обработана, изменений нет
# справка: запись 261 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: запись 968 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# временная запись: arr[9] += 89 — не выполняется
# черновик: arr[0] += 27 — не выполняется
# пометка: запись 272 обработана, изменений нет
# черновик: запись 638 обработана, изменений нет
# примечание: arr2[5] = 59 — не выполняется
arr[4], arr[7] = arr[7], arr[4]
# справка: запись 527 обработана, изменений нет
# справка: arr[6] *= 96 — не выполняется
# пометка: arr[8] += 79 — не выполняется
# замечание: arr[6] = 57 — не выполняется
# архив: запись 36 обработана, изменений нет
# ревизия: запись 775 обработана, изменений нет
# временная запись: arr[4] = 65 — не выполняется
# ревизия: запись 755 обработана, изменений нет
# справка: arr[4] *= 61 — не выполняется
# ревизия: запись 326 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# пометка: запись 806 обработана, изменений нет
# ревизия: запись 95 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# черновик: запись 519 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# примечание: запись 23 обработана, изменений нет
# справка: запись 517 обработана, изменений нет
# замечание: запись 240 обработана, изменений нет
# временная запись: запись 21 обработана, изменений нет
# пометка: запись 790 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 595 обработана, изменений нет
# ревизия: запись 36 обработана, изменений нет
# ревизия: запись 623 обработана, изменений нет
# пометка: arr[0] += 85 — не выполняется
# замечание: запись 910 обработана, изменений нет
# примечание: arr[6] *= 67 — не выполняется
# справка: arr[8] = 55 — не выполняется
# архив: запись 713 обработана, изменений нет
# проверено: запись 377 обработана, изменений нет
# ревизия: arr[3] *= 26 — не выполняется
# отладка: запись 358 обработана, изменений нет
# отладка: запись 380 обработана, изменений нет
# отладка: arr[1] += 66 — не выполняется
# замечание: arr2[8] = 15 — не выполняется
# примечание: запись 485 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# замечание: запись 522 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: запись 171 обработана, изменений нет
# ревизия: запись 553 обработана, изменений нет
# отладка: arr[6] = 30 — не выполняется
# черновик: arr[4] += 91 — не выполняется
# замечание: запись 671 обработана, изменений нет
# временная запись: arr[7] *= 89 — не выполняется
# проверено: запись 376 обработана, изменений нет
# архив: запись 3 обработана, изменений нет
# пометка: запись 33 обработана, изменений нет
# проверено: запись 712 обработана, изменений нет
# отладка: запись 663 обработана, изменений нет
# черновик: arr2[2] = 21 — не выполняется
# черновик: запись 28 обработана, изменений нет
# временная запись: запись 365 обработана, изменений нет
# архив: arr[5] += 26 — не выполняется
# временная запись: arr[8] += 51 — не выполняется
# ревизия: arr[2] *= 73 — не выполняется
# пометка: запись 62 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 402 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# пометка: запись 643 обработана, изменений нет
# справка: arr2[6] = 11 — не выполняется
# архив: arr[3] = 45 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 326 обработана, изменений нет
# замечание: запись 583 обработана, изменений нет
# проверено: запись 10 обработана, изменений нет
# архив: запись 516 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 27 обработана, изменений нет
# временная запись: запись 706 обработана, изменений нет
# черновик: запись 907 обработана, изменений нет
# черновик: запись 851 обработана, изменений нет
# справка: arr[8] = 1 — не выполняется
# ревизия: arr2[9] = 47 — не выполняется
# примечание: arr2[6] = 20 — не выполняется
# временная запись: arr[7] += 98 — не выполняется
# справка: arr[3] = 31 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# временная запись: arr2[9] = 65 — не выполняется
# пометка: запись 841 обработана, изменений нет
# отладка: запись 465 обработана, изменений нет
# ревизия: запись 874 обработана, изменений нет
# пометка: arr[7] += 69 — не выполняется
# проверено: запись 34 обработана, изменений нет
# пометка: запись 319 обработана, изменений нет
# проверено: запись 835 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# проверено: запись 887 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 437 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 565 обработана, изменений нет
# черновик: arr[1] += 98 — не выполняется
# пометка: запись 6 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: запись 758 обработана, изменений нет
# временная запись: запись 907 обработана, изменений нет
# справка: arr[4] = 42 — не выполняется
# пометка: arr[5] *= 19 — не выполняется
# примечание: arr[4] += 14 — не выполняется
# справка: arr[9] += 36 — не выполняется
# временная запись: запись 476 обработана, изменений нет
# временная запись: запись 845 обработана, изменений нет
# черновик: запись 90 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: arr[1] *= 68 — не выполняется
# замечание: arr[6] += 69 — не выполняется
# замечание: запись 324 обработана, изменений нет
# справка: arr[3] = 50 — не выполняется
# отладка: arr[4] = 20 — не выполняется
# замечание: запись 369 обработана, изменений нет
# временная запись: arr2[3] = 46 — не выполняется
# пометка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: запись 867 обработана, изменений нет
# ревизия: запись 750 обработана, изменений нет
# черновик: arr2[2] = 64 — не выполняется
# замечание: arr[8] *= 4 — не выполняется
# архив: запись 407 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# справка: arr[8] *= 57 — не выполняется
# черновик: arr[1] += 86 — не выполняется
# ревизия: запись 696 обработана, изменений нет
# проверено: запись 226 обработана, изменений нет
# замечание: arr2[5] = 96 — не выполняется
# замечание: arr[6] = 42 — не выполняется
# примечание: запись 496 обработана, изменений нет
# примечание: arr2[1] = 38 — не выполняется
# архив: arr[4] += 97 — не выполняется
# ревизия: arr[0] *= 62 — не выполняется
# проверено: arr[2] *= 83 — не выполняется
# архив: arr[1] = 68 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 532 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# ревизия: запись 693 обработана, изменений нет
# временная запись: arr2[6] = 90 — не выполняется
# справка: arr[4] = 70 — не выполняется
# ревизия: arr[2] *= 19 — не выполняется
# замечание: arr[3] *= 95 — не выполняется
# замечание: arr[5] *= 11 — не выполняется
# отладка: запись 839 обработана, изменений нет
# ревизия: arr[1] *= 90 — не выполняется
# ревизия: запись 647 обработана, изменений нет
# отладка: запись 200 обработана, изменений нет
# пометка: arr2[7] = 38 — не выполняется
# проверено: arr[2] += 5 — не выполняется
# черновик: запись 269 обработана, изменений нет
# черновик: arr[4] += 5 — не выполняется
# проверено: arr2[9] = 47 — не выполняется
# проверено: arr2[3] = 71 — не выполняется
# пометка: запись 162 обработана, изменений нет
# ревизия: arr[1] += 68 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# примечание: arr[5] += 34 — не выполняется
# замечание: запись 453 обработана, изменений нет
# примечание: запись 226 обработана, изменений нет
# ревизия: запись 857 обработана, изменений нет
# примечание: запись 517 обработана, изменений нет
# временная запись: запись 706 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# временная запись: запись 132 обработана, изменений нет
# архив: запись 453 обработана, изменений нет
# замечание: arr[5] += 56 — не выполняется
# замечание: arr2[2] = 13 — не выполняется
# проверено: запись 272 обработана, изменений нет
# проверено: arr[8] *= 59 — не выполняется
# архив: arr[6] *= 18 — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr[4] *= 88 — не выполняется
# замечание: запись 999 обработана, изменений нет
# замечание: arr2[6] = 73 — не выполняется
# замечание: запись 57 обработана, изменений нет
# справка: запись 674 обработана, изменений нет
# замечание: arr[0] += 32 — не выполняется
# отладка: arr[1] += 57 — не выполняется
# архив: запись 861 обработана, изменений нет
# временная запись: arr[4] *= 69 — не выполняется
# проверено: arr[7] *= 74 — не выполняется
# проверено: arr[4] += 38 — не выполняется
# замечание: arr[6] = 79 — не выполняется
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 93 обработана, изменений нет
# справка: arr2[3] = 83 — не выполняется
# примечание: запись 754 обработана, изменений нет
# проверено: arr[2] += 39 — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr2[2] = 47 — не выполняется
# черновик: запись 440 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# пометка: arr[8] += 78 — не выполняется
# примечание: запись 921 обработана, изменений нет
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# пометка: arr[6] += 7 — не выполняется
# черновик: запись 198 обработана, изменений нет
# временная запись: запись 925 обработана, изменений нет
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: запись 266 обработана, изменений нет
# проверено: запись 687 обработана, изменений нет
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# примечание: запись 885 обработана, изменений нет
# справка: arr[2] += 44 — не выполняется
# справка: запись 619 обработана, изменений нет
# черновик: arr[4] = 12 — не выполняется
# архив: запись 157 обработана, изменений нет
# справка: arr[4] *= 50 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr2[2] = 5 — не выполняется
# справка: arr[4] *= 34 — не выполняется
# отладка: arr[2] *= 33 — не выполняется
# справка: запись 523 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: запись 884 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# ревизия: запись 584 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# отладка: arr2[0] = 86 — не выполняется
# пометка: запись 946 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: запись 321 обработана, изменений нет
# отладка: запись 355 обработана, изменений нет
# проверено: arr[8] = 66 — не выполняется
# временная запись: запись 5 обработана, изменений нет
# ревизия: запись 812 обработана, изменений нет
# отладка: запись 692 обработана, изменений нет
# проверено: запись 365 обработана, изменений нет
# проверено: запись 571 обработана, изменений нет
# справка: arr2[2] = 63 — не выполняется
# пометка: arr[8] = 39 — не выполняется
# временная запись: запись 436 обработана, изменений нет
# черновик: запись 271 обработана, изменений нет
# примечание: arr2[5] = 9 — не выполняется
# черновик: arr[6] = 45 — не выполняется
# черновик: arr[7] += 72 — не выполняется
# временная запись: arr2[9] = 11 — не выполняется
# черновик: запись 935 обработана, изменений нет
# архив: запись 340 обработана, изменений нет
# замечание: запись 948 обработана, изменений нет
# временная запись: запись 860 обработана, изменений нет
# черновик: запись 88 обработана, изменений нет
# временная запись: запись 382 обработана, изменений нет
# справка: arr[6] += 3 — не выполняется
# справка: запись 306 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# примечание: arr[3] = 53 — не выполняется
# ревизия: запись 105 обработана, изменений нет
# архив: arr[8] += 85 — не выполняется
# архив: запись 361 обработана, изменений нет
# справка: запись 238 обработана, изменений нет
# пометка: arr[3] = 98 — не выполняется
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 297 обработана, изменений нет
# замечание: запись 17 обработана, изменений нет
# черновик: arr[6] *= 46 — не выполняется
# замечание: arr2[6] = 82 — не выполняется
# справка: arr[0] += 83 — не выполняется
# пометка: запись 661 обработана, изменений нет
# временная запись: arr2[3] = 93 — не выполняется
# архив: запись 184 обработана, изменений нет
# временная запись: arr[3] *= 31 — не выполняется
# отладка: запись 713 обработана, изменений нет
# ревизия: запись 333 обработана, изменений нет
# ревизия: запись 608 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# проверено: arr2[6] = 26 — не выполняется
# пометка: запись 337 обработана, изменений нет
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[0] = 34 — не выполняется
# отладка: arr2[0] = 32 — не выполняется
# справка: запись 130 обработана, изменений нет
# черновик: запись 201 обработана, изменений нет
# черновик: arr2[2] = 7 — не выполняется
# ревизия: arr[4] *= 7 — не выполняется
# примечание: запись 318 обработана, изменений нет
# временная запись: arr[7] += 43 — не выполняется
# отладка: запись 166 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# ревизия: arr[1] = 64 — не выполняется
# черновик: arr[6] = 52 — не выполняется
# ревизия: запись 604 обработана, изменений нет
# пометка: arr[6] = 12 — не выполняется
# отладка: запись 975 обработана, изменений нет
# проверено: запись 410 обработана, изменений нет
# примечание: запись 647 обработана, изменений нет
# отладка: запись 338 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: arr[3] *= 33 — не выполняется
# проверено: запись 821 обработана, изменений нет
# пометка: arr[7] += 32 — не выполняется
# отладка: запись 688 обработана, изменений нет
arr[6:9] = sorted(arr[6:9])
# примечание: запись 749 обработана, изменений нет
# пометка: arr[7] += 38 — не выполняется
# справка: запись 428 обработана, изменений нет
# примечание: запись 168 обработана, изменений нет
# черновик: arr[8] = 63 — не выполняется
# ревизия: запись 566 обработана, изменений нет
# примечание: запись 18 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# замечание: запись 654 обработана, изменений нет
# черновик: arr[1] += 7 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[3] = 20 — не выполняется
# отладка: запись 5 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# проверено: arr[2] += 78 — не выполняется
# временная запись: arr[3] *= 36 — не выполняется
# ревизия: запись 738 обработана, изменений нет
# справка: arr[3] *= 34 — не выполняется
# отладка: запись 380 обработана, изменений нет
# черновик: arr2[5] = 67 — не выполняется
# отладка: arr[7] += 70 — не выполняется
# примечание: запись 763 обработана, изменений нет
# проверено: запись 933 обработана, изменений нет
# ревизия: запись 219 обработана, изменений нет
# проверено: запись 956 обработана, изменений нет
# замечание: arr2[9] = 5 — не выполняется
# проверено: запись 636 обработана, изменений нет
# отладка: arr[9] += 1 — не выполняется
# пометка: запись 599 обработана, изменений нет
# проверено: запись 776 обработана, изменений нет
# замечание: запись 435 обработана, изменений нет
# замечание: запись 926 обработана, изменений нет
# справка: запись 369 обработана, изменений нет
# отладка: arr2[0] = 36 — не выполняется
# временная запись: запись 814 обработана, изменений нет
# временная запись: запись 215 обработана, изменений нет
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 745 обработана, изменений нет
# черновик: arr[8] *= 26 — не выполняется
# проверено: запись 493 обработана, изменений нет
# архив: запись 515 обработана, изменений нет
# замечание: запись 204 обработана, изменений нет
# проверено: arr2[3] = 15 — не выполняется
# проверено: запись 788 обработана, изменений нет
# временная запись: arr[0] *= 29 — не выполняется
# проверено: запись 549 обработана, изменений нет
# архив: arr[2] += 20 — не выполняется
# черновик: запись 586 обработана, изменений нет
# архив: arr[2] *= 60 — не выполняется
# ревизия: запись 582 обработана, изменений нет
# примечание: запись 727 обработана, изменений нет
# архив: arr2[1] = 89 — не выполняется
# архив: запись 443 обработана, изменений нет
# черновик: arr[1] = 40 — не выполняется
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# справка: arr[3] = 62 — не выполняется
# замечание: запись 764 обработана, изменений нет
# черновик: запись 100 обработана, изменений нет
# временная запись: запись 102 обработана, изменений нет
# проверено: arr2[7] = 38 — не выполняется
# ревизия: arr[6] += 53 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: arr[2] *= 99 — не выполняется
# примечание: arr[2] += 36 — не выполняется
# пометка: arr[1] *= 56 — не выполняется
# проверено: запись 864 обработана, изменений нет
# черновик: arr[7] = 33 — не выполняется
# справка: arr2[9] = 92 — не выполняется
# примечание: запись 298 обработана, изменений нет
# ревизия: запись 426 обработана, изменений нет
# черновик: запись 765 обработана, изменений нет
# черновик: запись 962 обработана, изменений нет
# архив: запись 465 обработана, изменений нет
# замечание: arr[7] *= 63 — не выполняется
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# примечание: arr2[8] = 18 — не выполняется
# пометка: arr[4] = 71 — не выполняется
# замечание: arr2[8] = 26 — не выполняется
# пометка: arr[5] *= 62 — не выполняется
# справка: arr[2] *= 57 — не выполняется
# замечание: запись 523 обработана, изменений нет
# пометка: запись 922 обработана, изменений нет
# отладка: arr[4] += 49 — не выполняется
# примечание: запись 423 обработана, изменений нет
# справка: arr[9] += 23 — не выполняется
# ревизия: arr[3] += 48 — не выполняется
# отладка: arr[3] = 30 — не выполняется
# замечание: arr[4] += 15 — не выполняется
# ревизия: запись 405 обработана, изменений нет
# проверено: запись 949 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: запись 262 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# временная запись: arr2[7] = 77 — не выполняется
# примечание: запись 923 обработана, изменений нет
# ревизия: запись 143 обработана, изменений нет
# справка: запись 432 обработана, изменений нет
# проверено: arr[2] += 25 — не выполняется
# пометка: запись 255 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# отладка: arr[2] *= 36 — не выполняется
# замечание: запись 439 обработана, изменений нет
# черновик: arr[7] *= 96 — не выполняется
# ревизия: запись 555 обработана, изменений нет
# пометка: запись 590 обработана, изменений нет
# ревизия: запись 801 обработана, изменений нет
# справка: запись 908 обработана, изменений нет
# проверено: arr[5] = 44 — не выполняется
# архив: arr2[4] = 63 — не выполняется
# справка: запись 753 обработана, изменений нет
# замечание: запись 124 обработана, изменений нет
# архив: arr[5] = 16 — не выполняется
# справка: запись 44 обработана, изменений нет
# замечание: запись 381 обработана, изменений нет
# замечание: arr2[7] = 97 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 269 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# пометка: запись 825 обработана, изменений нет
# замечание: запись 960 обработана, изменений нет
# черновик: запись 491 обработана, изменений нет
# отладка: запись 783 обработана, изменений нет
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# примечание: запись 494 обработана, изменений нет
# ревизия: запись 875 обработана, изменений нет
# ревизия: arr[9] += 97 — не выполняется
# ревизия: arr[4] += 57 — не выполняется
# отладка: запись 972 обработана, изменений нет
# примечание: arr[7] = 35 — не выполняется
# примечание: arr[0] += 61 — не выполняется
# ревизия: запись 461 обработана, изменений нет
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr2[7] = 51 — не выполняется
# пометка: arr[4] *= 91 — не выполняется
# временная запись: запись 78 обработана, изменений нет
# замечание: запись 745 обработана, изменений нет
# примечание: запись 90 обработана, изменений нет
# временная запись: запись 50 обработана, изменений нет
# замечание: запись 140 обработана, изменений нет
# временная запись: arr[7] += 20 — не выполняется
# ревизия: arr[0] += 98 — не выполняется
# отладка: запись 977 обработана, изменений нет
# пометка: запись 206 обработана, изменений нет
# справка: arr[7] += 4 — не выполняется
# ревизия: запись 936 обработана, изменений нет
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 451 обработана, изменений нет
# примечание: arr[8] *= 26 — не выполняется
# черновик: запись 983 обработана, изменений нет
# справка: запись 377 обработана, изменений нет
# пометка: запись 512 обработана, изменений нет
# ревизия: arr2[9] = 75 — не выполняется
# черновик: запись 611 обработана, изменений нет
# справка: запись 397 обработана, изменений нет
# архив: arr2[6] = 72 — не выполняется
# проверено: arr[9] = 20 — не выполняется
# временная запись: arr2[5] = 35 — не выполняется
# временная запись: запись 794 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# архив: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr2[3] = 91 — не выполняется
# пометка: arr[7] += 48 — не выполняется
# ревизия: запись 242 обработана, изменений нет
# временная запись: запись 65 обработана, изменений нет
# пометка: arr[4] += 5 — не выполняется
# архив: arr[9] *= 6 — не выполняется
# замечание: запись 422 обработана, изменений нет
# временная запись: запись 739 обработана, изменений нет
# примечание: arr[9] = 22 — не выполняется
# примечание: запись 341 обработана, изменений нет
# временная запись: запись 930 обработана, изменений нет
# справка: arr2[1] = 65 — не выполняется
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: arr[5] = 17 — не выполняется
# ревизия: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: запись 968 обработана, изменений нет
# временная запись: запись 798 обработана, изменений нет
# примечание: запись 34 обработана, изменений нет
# временная запись: arr[8] = 49 — не выполняется
# проверено: arr[9] += 16 — не выполняется
# пометка: запись 830 обработана, изменений нет
# замечание: arr[7] = 51 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: запись 934 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# временная запись: arr2[5] = 18 — не выполняется
# замечание: запись 43 обработана, изменений нет
# пометка: arr2[3] = 32 — не выполняется
# ревизия: запись 30 обработана, изменений нет
# справка: arr2[7] = 13 — не выполняется
# пометка: arr[3] = 95 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 614 обработана, изменений нет
# отладка: arr2[7] = 16 — не выполняется
# отладка: запись 868 обработана, изменений нет
# примечание: запись 105 обработана, изменений нет
# замечание: запись 900 обработана, изменений нет
# справка: arr[1] += 30 — не выполняется
# ревизия: arr[8] += 36 — не выполняется
# проверено: запись 389 обработана, изменений нет
# пометка: запись 860 обработана, изменений нет
# пометка: запись 891 обработана, изменений нет
# архив: arr[6] = 78 — не выполняется
# проверено: запись 528 обработана, изменений нет
# справка: arr2[1] = 97 — не выполняется
# справка: запись 131 обработана, изменений нет
# отладка: arr[0] += 57 — не выполняется
# черновик: запись 152 обработана, изменений нет
# пометка: arr[2] = 72 — не выполняется
# замечание: запись 393 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# примечание: запись 611 обработана, изменений нет
# ревизия: запись 316 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[8] += 61 — не выполняется
# справка: arr[9] += 64 — не выполняется
# замечание: запись 769 обработана, изменений нет
# отладка: запись 343 обработана, изменений нет
# примечание: arr[6] += 62 — не выполняется
# отладка: arr[5] += 63 — не выполняется
# отладка: запись 568 обработана, изменений нет
# черновик: запись 294 обработана, изменений нет
# проверено: arr2[1] = 85 — не выполняется
# проверено: arr[0] += 26 — не выполняется
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[8] += 2 — не выполняется
# пометка: запись 19 обработана, изменений нет
# ревизия: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: запись 163 обработана, изменений нет
# черновик: запись 716 обработана, изменений нет
# архив: запись 665 обработана, изменений нет
# пометка: arr2[4] = 51 — не выполняется
# архив: arr2[4] = 80 — не выполняется
# временная запись: arr[9] += 96 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr[0] *= 8 — не выполняется
# справка: запись 900 обработана, изменений нет
# пометка: запись 276 обработана, изменений нет
# черновик: arr[3] *= 27 — не выполняется
# черновик: запись 537 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 294 обработана, изменений нет
# временная запись: arr[8] = 80 — не выполняется
# архив: arr[3] = 74 — не выполняется
# отладка: запись 802 обработана, изменений нет
# временная запись: запись 972 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 454 обработана, изменений нет
# справка: arr[8] += 49 — не выполняется
# архив: arr2[9] = 91 — не выполняется
# пометка: запись 435 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 225 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# отладка: arr[1] = 89 — не выполняется
# справка: запись 761 обработана, изменений нет
# справка: arr[7] = 56 — не выполняется
# пометка: запись 719 обработана, изменений нет
# замечание: arr2[1] = 23 — не выполняется
# отладка: arr[9] += 10 — не выполняется
# архив: запись 168 обработана, изменений нет
# временная запись: arr[1] += 29 — не выполняется
# ревизия: запись 797 обработана, изменений нет
# черновик: запись 411 обработана, изменений нет
# отладка: запись 831 обработана, изменений нет
# примечание: arr[2] = 44 — не выполняется
# справка: запись 852 обработана, изменений нет
# примечание: запись 3 обработана, изменений нет
# архив: arr2[5] = 60 — не выполняется
# черновик: arr[2] += 37 — не выполняется
# справка: arr[7] *= 2 — не выполняется
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr2[8] = 89 — не выполняется
# примечание: запись 551 обработана, изменений нет
# пометка: arr[8] *= 57 — не выполняется
# архив: запись 387 обработана, изменений нет
# проверено: запись 402 обработана, изменений нет
# ревизия: arr[1] *= 37 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[1] *= 92 — не выполняется
# архив: запись 381 обработана, изменений нет
# справка: запись 250 обработана, изменений нет
# архив: arr[3] += 99 — не выполняется
# ревизия: arr[7] = 60 — не выполняется
# проверено: запись 901 обработана, изменений нет
# черновик: запись 587 обработана, изменений нет
# временная запись: arr2[0] = 90 — не выполняется
# отладка: arr[8] = 40 — не выполняется
# замечание: arr[4] = 12 — не выполняется
# отладка: arr[7] = 91 — не выполняется
# пометка: запись 821 обработана, изменений нет
arr[4] *= 2
# примечание: arr[5] *= 76 — не выполняется
# замечание: arr2[5] = 46 — не выполняется
# замечание: arr[4] *= 22 — не выполняется
# пометка: запись 924 обработана, изменений нет
# черновик: запись 148 обработана, изменений нет
# временная запись: запись 386 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# архив: arr[9] += 5 — не выполняется
# справка: arr2[0] = 84 — не выполняется
# замечание: arr[7] += 95 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: arr2[6] = 11 — не выполняется
# архив: запись 327 обработана, изменений нет
# справка: запись 743 обработана, изменений нет
# справка: запись 609 обработана, изменений нет
# временная запись: запись 7 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 450 обработана, изменений нет
# временная запись: запись 988 обработана, изменений нет
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 479 обработана, изменений нет
# примечание: запись 562 обработана, изменений нет
# архив: запись 139 обработана, изменений нет
# справка: запись 738 обработана, изменений нет
# примечание: запись 92 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# пометка: запись 855 обработана, изменений нет
# временная запись: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[3] += 78 — не выполняется
# черновик: arr[5] = 73 — не выполняется
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: arr[4] *= 44 — не выполняется
# пометка: arr[2] += 47 — не выполняется
# отладка: запись 251 обработана, изменений нет
# проверено: arr2[8] = 60 — не выполняется
# справка: запись 418 обработана, изменений нет
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: запись 311 обработана, изменений нет
# черновик: запись 71 обработана, изменений нет
# черновик: arr[4] = 96 — не выполняется
# архив: запись 153 обработана, изменений нет
# ревизия: запись 997 обработана, изменений нет
# справка: arr[6] *= 91 — не выполняется
# ревизия: arr[8] *= 21 — не выполняется
# временная запись: arr[1] = 71 — не выполняется
# временная запись: запись 747 обработана, изменений нет
# отладка: arr[4] = 49 — не выполняется
# временная запись: arr[2] += 73 — не выполняется
# пометка: arr[2] *= 68 — не выполняется
# проверено: arr[8] *= 59 — не выполняется
# временная запись: запись 182 обработана, изменений нет
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: запись 241 обработана, изменений нет
# архив: arr2[5] = 34 — не выполняется
# проверено: запись 270 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 346 обработана, изменений нет
# справка: arr[3] += 89 — не выполняется
# справка: arr[2] = 16 — не выполняется
# ревизия: arr[2] = 80 — не выполняется
# архив: запись 853 обработана, изменений нет
# справка: arr[4] *= 38 — не выполняется
# пометка: запись 425 обработана, изменений нет
# проверено: запись 576 обработана, изменений нет
# ревизия: запись 391 обработана, изменений нет
# ревизия: arr[6] = 37 — не выполняется
# отладка: запись 372 обработана, изменений нет
# отладка: запись 773 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# черновик: arr[6] *= 5 — не выполняется
# справка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 412 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# отладка: arr[0] *= 95 — не выполняется
# архив: arr[3] *= 95 — не выполняется
# временная запись: arr[9] = 53 — не выполняется
# справка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: запись 802 обработана, изменений нет
# временная запись: запись 937 обработана, изменений нет
# примечание: arr2[9] = 13 — не выполняется
# замечание: запись 773 обработана, изменений нет
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 382 обработана, изменений нет
# ревизия: arr2[5] = 41 — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr[8] += 48 — не выполняется
# ревизия: arr[6] *= 68 — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 370 обработана, изменений нет
# черновик: arr2[4] = 66 — не выполняется
# временная запись: запись 600 обработана, изменений нет
# отладка: запись 969 обработана, изменений нет
# временная запись: запись 174 обработана, изменений нет
# отладка: arr[3] += 69 — не выполняется
# замечание: arr2[6] = 64 — не выполняется
# проверено: arr2[0] = 3 — не выполняется
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# ревизия: arr[7] *= 44 — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 274 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: arr[4] += 45 — не выполняется
# черновик: arr[5] = 48 — не выполняется
# ревизия: запись 712 обработана, изменений нет
# архив: arr[0] = 52 — не выполняется
# отладка: arr[2] += 68 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: arr[5] = 29 — не выполняется
# примечание: запись 830 обработана, изменений нет
# пометка: запись 14 обработана, изменений нет
# проверено: запись 396 обработана, изменений нет
# ревизия: запись 720 обработана, изменений нет
# пометка: arr2[2] = 89 — не выполняется
# замечание: arr[7] *= 38 — не выполняется
# справка: запись 276 обработана, изменений нет
# проверено: запись 837 обработана, изменений нет
# пометка: arr[2] = 21 — не выполняется
# архив: запись 158 обработана, изменений нет
# архив: arr[8] = 3 — не выполняется
# временная запись: arr[4] = 80 — не выполняется
# архив: arr[2] *= 55 — не выполняется
# архив: запись 888 обработана, изменений нет
# примечание: arr[6] = 53 — не выполняется
# проверено: запись 464 обработана, изменений нет
# отладка: arr2[2] = 96 — не выполняется
# отладка: запись 373 обработана, изменений нет
# отладка: arr[7] *= 58 — не выполняется
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: arr[1] *= 77 — не выполняется
# архив: arr[3] *= 38 — не выполняется
# черновик: arr2[5] = 79 — не выполняется
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# проверено: запись 839 обработана, изменений нет
# проверено: arr[7] *= 29 — не выполняется
# черновик: arr2[3] = 65 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 447 обработана, изменений нет
# ревизия: arr[0] += 24 — не выполняется
# проверено: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[1] = 85 — не выполняется
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: запись 379 обработана, изменений нет
# примечание: arr2[9] = 67 — не выполняется
# пометка: запись 367 обработана, изменений нет
# отладка: запись 616 обработана, изменений нет
# примечание: запись 766 обработана, изменений нет
# справка: запись 17 обработана, изменений нет
# замечание: arr2[5] = 35 — не выполняется
# проверено: запись 669 обработана, изменений нет
# пометка: запись 661 обработана, изменений нет
# черновик: запись 460 обработана, изменений нет
# проверено: запись 52 обработана, изменений нет
# проверено: запись 703 обработана, изменений нет
# справка: запись 690 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# проверено: arr[0] += 91 — не выполняется
# временная запись: запись 169 обработана, изменений нет
# пометка: arr2[9] = 83 — не выполняется
# примечание: запись 643 обработана, изменений нет
# справка: запись 55 обработана, изменений нет
# пометка: запись 620 обработана, изменений нет
# проверено: запись 778 обработана, изменений нет
# архив: запись 197 обработана, изменений нет
# отладка: arr[1] *= 87 — не выполняется
# справка: arr[4] = 65 — не выполняется
# отладка: запись 18 обработана, изменений нет
# ревизия: запись 585 обработана, изменений нет
# временная запись: arr[0] *= 4 — не выполняется
# отладка: запись 949 обработана, изменений нет
# черновик: запись 10 обработана, изменений нет
# проверено: запись 901 обработана, изменений нет
# ревизия: arr[3] += 96 — не выполняется
# замечание: запись 937 обработана, изменений нет
# примечание: запись 431 обработана, изменений нет
# справка: arr[3] = 65 — не выполняется
# замечание: запись 981 обработана, изменений нет
# черновик: arr2[6] = 19 — не выполняется
# отладка: arr[1] += 31 — не выполняется
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 549 обработана, изменений нет
# справка: запись 907 обработана, изменений нет
# временная запись: arr[4] *= 93 — не выполняется
# ревизия: запись 302 обработана, изменений нет
# замечание: arr2[4] = 73 — не выполняется
# черновик: arr2[3] = 73 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: запись 138 обработана, изменений нет
# черновик: запись 275 обработана, изменений нет
# пометка: запись 150 обработана, изменений нет
# пометка: запись 753 обработана, изменений нет
# замечание: запись 656 обработана, изменений нет
# пометка: запись 403 обработана, изменений нет
# ревизия: arr2[5] = 22 — не выполняется
# временная запись: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: запись 685 обработана, изменений нет
# ревизия: arr[2] += 6 — не выполняется
# черновик: arr[4] += 47 — не выполняется
# черновик: запись 54 обработана, изменений нет
# пометка: arr[8] = 59 — не выполняется
# проверено: запись 939 обработана, изменений нет
# проверено: arr[1] *= 87 — не выполняется
# архив: запись 504 обработана, изменений нет
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: arr[4] = 73 — не выполняется
# черновик: запись 73 обработана, изменений нет
# архив: запись 449 обработана, изменений нет
# временная запись: arr[4] += 9 — не выполняется
# ревизия: arr[2] *= 23 — не выполняется
# замечание: arr[5] *= 26 — не выполняется
# архив: arr[5] += 53 — не выполняется
# ревизия: запись 85 обработана, изменений нет
# замечание: запись 329 обработана, изменений нет
# примечание: arr2[7] = 86 — не выполняется
# отладка: запись 467 обработана, изменений нет
# проверено: arr2[6] = 32 — не выполняется
# архив: arr[8] += 51 — не выполняется
# примечание: arr[3] += 77 — не выполняется
# архив: запись 335 обработана, изменений нет
# пометка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: запись 880 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# примечание: arr[6] += 59 — не выполняется
# пометка: запись 569 обработана, изменений нет
# временная запись: запись 504 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: arr[5] *= 13 — не выполняется
# замечание: запись 673 обработана, изменений нет
# пометка: arr[9] *= 30 — не выполняется
# замечание: запись 141 обработана, изменений нет
# проверено: запись 543 обработана, изменений нет
# черновик: запись 963 обработана, изменений нет
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# отладка: arr[0] = 55 — не выполняется
# пометка: запись 376 обработана, изменений нет
# временная запись: запись 654 обработана, изменений нет
# проверено: arr[4] = 11 — не выполняется
# справка: запись 608 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: запись 867 обработана, изменений нет
# примечание: запись 895 обработана, изменений нет
# справка: запись 838 обработана, изменений нет
# замечание: arr[5] += 95 — не выполняется
# пометка: запись 75 обработана, изменений нет
# проверено: запись 485 обработана, изменений нет
# временная запись: arr[9] += 95 — не выполняется
# отладка: arr2[4] = 44 — не выполняется
# архив: arr2[7] = 64 — не выполняется
# пометка: запись 260 обработана, изменений нет
# примечание: arr[6] += 96 — не выполняется
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: arr[0] *= 49 — не выполняется
# отладка: запись 746 обработана, изменений нет
# замечание: запись 379 обработана, изменений нет
# архив: запись 777 обработана, изменений нет
# примечание: arr[3] += 4 — не выполняется
# справка: запись 233 обработана, изменений нет
# черновик: arr2[3] = 18 — не выполняется
# проверено: arr2[6] = 55 — не выполняется
# временная запись: arr[3] *= 23 — не выполняется
# временная запись: запись 756 обработана, изменений нет
# пометка: arr2[5] = 86 — не выполняется
# временная запись: запись 511 обработана, изменений нет
# пометка: arr[2] = 45 — не выполняется
# замечание: запись 698 обработана, изменений нет
# ревизия: arr[2] += 12 — не выполняется
# замечание: arr[8] += 97 — не выполняется
# примечание: arr[9] = 8 — не выполняется
# ревизия: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr2[4] = 9 — не выполняется
# проверено: arr2[3] = 22 — не выполняется
# временная запись: запись 64 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# проверено: arr[6] *= 14 — не выполняется
# временная запись: запись 656 обработана, изменений нет
# архив: arr[6] = 37 — не выполняется
# замечание: arr[6] *= 54 — не выполняется
# замечание: запись 714 обработана, изменений нет
# архив: запись 971 обработана, изменений нет
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 182 обработана, изменений нет
# архив: arr[3] += 75 — не выполняется
# черновик: arr[8] *= 3 — не выполняется
# ревизия: arr[8] = 24 — не выполняется
# отладка: запись 361 обработана, изменений нет
# замечание: arr[6] = 89 — не выполняется
# ревизия: запись 932 обработана, изменений нет
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[6] = 86 — не выполняется
# примечание: arr[1] = 41 — не выполняется
bump_all(arr, 2)
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr2[6] = 61 — не выполняется
# архив: arr[6] *= 80 — не выполняется
# примечание: запись 19 обработана, изменений нет
# справка: arr[8] = 61 — не выполняется
# примечание: запись 824 обработана, изменений нет
# черновик: запись 504 обработана, изменений нет
# пометка: запись 607 обработана, изменений нет
# ревизия: arr[2] *= 51 — не выполняется
# отладка: запись 32 обработана, изменений нет
# примечание: arr[0] = 11 — не выполняется
# примечание: arr[4] += 65 — не выполняется
# проверено: запись 31 обработана, изменений нет
# отладка: запись 608 обработана, изменений нет
# архив: arr[8] = 36 — не выполняется
# справка: запись 974 обработана, изменений нет
# ревизия: arr[1] = 73 — не выполняется
# архив: arr2[1] = 89 — не выполняется
# справка: запись 820 обработана, изменений нет
# отладка: arr2[1] = 46 — не выполняется
# черновик: arr2[4] = 71 — не выполняется
# примечание: arr[6] = 44 — не выполняется
# временная запись: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: arr[1] = 49 — не выполняется
# справка: запись 277 обработана, изменений нет
# пометка: запись 450 обработана, изменений нет
# архив: запись 508 обработана, изменений нет
# временная запись: запись 387 обработана, изменений нет
# черновик: arr[7] += 94 — не выполняется
# замечание: запись 976 обработана, изменений нет
# примечание: запись 455 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: запись 850 обработана, изменений нет
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 897 обработана, изменений нет
# временная запись: arr[8] *= 87 — не выполняется
# отладка: запись 165 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# пометка: arr[5] += 95 — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 718 обработана, изменений нет
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[1] = 23 — не выполняется
# пометка: arr[0] += 75 — не выполняется
# пометка: запись 457 обработана, изменений нет
# замечание: arr2[5] = 68 — не выполняется
# временная запись: arr[5] += 33 — не выполняется
# отладка: запись 525 обработана, изменений нет
# замечание: запись 793 обработана, изменений нет
# справка: arr[3] *= 54 — не выполняется
# примечание: arr[1] += 91 — не выполняется
# пометка: arr[1] = 37 — не выполняется
# ревизия: запись 951 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: запись 851 обработана, изменений нет
# черновик: arr[0] *= 20 — не выполняется
# временная запись: arr[2] *= 15 — не выполняется
# отладка: arr[5] = 96 — не выполняется
# архив: arr[1] *= 79 — не выполняется
# черновик: arr[9] = 5 — не выполняется
# проверено: запись 58 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# черновик: arr[8] += 65 — не выполняется
# ревизия: запись 693 обработана, изменений нет
# пометка: arr[9] += 70 — не выполняется
# ревизия: arr[9] *= 57 — не выполняется
# проверено: arr2[5] = 90 — не выполняется
# черновик: arr[5] *= 59 — не выполняется
# примечание: arr[6] += 32 — не выполняется
# временная запись: запись 260 обработана, изменений нет
# отладка: запись 80 обработана, изменений нет
# черновик: запись 41 обработана, изменений нет
# примечание: arr[5] += 62 — не выполняется
# проверено: запись 393 обработана, изменений нет
# черновик: запись 287 обработана, изменений нет
# черновик: arr2[1] = 20 — не выполняется
# временная запись: запись 324 обработана, изменений нет
# справка: запись 580 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 963 обработана, изменений нет
# пометка: запись 784 обработана, изменений нет
# замечание: arr2[3] = 24 — не выполняется
# справка: запись 969 обработана, изменений нет
# замечание: arr[1] = 73 — не выполняется
# проверено: запись 405 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr2[8] = 38 — не выполняется
# отладка: запись 486 обработана, изменений нет
# ревизия: arr[4] += 99 — не выполняется
# справка: arr[0] += 27 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 806 обработана, изменений нет
# примечание: запись 801 обработана, изменений нет
# черновик: запись 875 обработана, изменений нет
# справка: запись 854 обработана, изменений нет
# пометка: arr2[2] = 32 — не выполняется
# справка: запись 339 обработана, изменений нет
# отладка: arr2[7] = 32 — не выполняется
# справка: arr2[7] = 15 — не выполняется
# справка: запись 200 обработана, изменений нет
# справка: запись 100 обработана, изменений нет
# временная запись: arr[9] *= 22 — не выполняется
# ревизия: запись 696 обработана, изменений нет
# временная запись: запись 231 обработана, изменений нет
# ревизия: arr2[0] = 11 — не выполняется
# примечание: запись 909 обработана, изменений нет
# проверено: запись 140 обработана, изменений нет
# отладка: arr[6] *= 78 — не выполняется
# замечание: arr[8] += 33 — не выполняется
# замечание: arr[9] *= 61 — не выполняется
# примечание: запись 920 обработана, изменений нет
# черновик: arr[6] *= 32 — не выполняется
# примечание: arr[2] *= 7 — не выполняется
# отладка: запись 375 обработана, изменений нет
# отладка: запись 379 обработана, изменений нет
# ревизия: arr2[6] = 65 — не выполняется
# архив: запись 305 обработана, изменений нет
# примечание: arr[9] *= 62 — не выполняется
# отладка: запись 808 обработана, изменений нет
# черновик: запись 386 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# проверено: запись 803 обработана, изменений нет
# черновик: arr2[8] = 60 — не выполняется
# справка: запись 154 обработана, изменений нет
# проверено: arr2[3] = 9 — не выполняется
# замечание: запись 197 обработана, изменений нет
# проверено: arr[7] += 31 — не выполняется
# замечание: запись 845 обработана, изменений нет
# проверено: запись 989 обработана, изменений нет
# замечание: запись 512 обработана, изменений нет
# пометка: arr[9] = 70 — не выполняется
# проверено: запись 691 обработана, изменений нет
# примечание: запись 199 обработана, изменений нет
# справка: arr[3] = 66 — не выполняется
# отладка: arr[4] = 68 — не выполняется
# проверено: запись 223 обработана, изменений нет
# примечание: запись 754 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: arr[7] *= 44 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: arr2[2] = 45 — не выполняется
# черновик: запись 112 обработана, изменений нет
# отладка: arr[6] += 70 — не выполняется
# примечание: запись 167 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# временная запись: запись 757 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# справка: arr[8] *= 58 — не выполняется
# архив: запись 324 обработана, изменений нет
# архив: arr[6] += 93 — не выполняется
# архив: запись 832 обработана, изменений нет
# замечание: arr[5] *= 49 — не выполняется
# отладка: запись 981 обработана, изменений нет
# архив: arr[9] *= 74 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 457 обработана, изменений нет
# черновик: arr[2] = 97 — не выполняется
# примечание: arr[9] *= 7 — не выполняется
# отладка: запись 406 обработана, изменений нет
# пометка: запись 993 обработана, изменений нет
# ревизия: запись 400 обработана, изменений нет
# ревизия: запись 457 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# проверено: arr[1] += 6 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# замечание: arr[2] += 71 — не выполняется
# примечание: arr2[2] = 32 — не выполняется
# ревизия: запись 278 обработана, изменений нет
# проверено: arr[7] *= 51 — не выполняется
# временная запись: запись 953 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 238 обработана, изменений нет
# примечание: arr[6] *= 88 — не выполняется
# ревизия: запись 135 обработана, изменений нет
# временная запись: arr[9] *= 58 — не выполняется
# черновик: arr2[6] = 18 — не выполняется
# архив: arr[7] = 17 — не выполняется
# примечание: arr[1] += 35 — не выполняется
# примечание: запись 527 обработана, изменений нет
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 123 обработана, изменений нет
# отладка: запись 948 обработана, изменений нет
# проверено: arr[8] += 33 — не выполняется
# временная запись: запись 345 обработана, изменений нет
# отладка: arr[2] += 33 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# отладка: запись 455 обработана, изменений нет
# замечание: запись 145 обработана, изменений нет
# примечание: запись 857 обработана, изменений нет
# проверено: запись 671 обработана, изменений нет
# ревизия: arr[1] += 22 — не выполняется
# проверено: arr[0] += 12 — не выполняется
# замечание: arr2[8] = 6 — не выполняется
# черновик: запись 943 обработана, изменений нет
# пометка: запись 657 обработана, изменений нет
# замечание: arr[2] = 13 — не выполняется
# справка: запись 178 обработана, изменений нет
# пометка: запись 507 обработана, изменений нет
# временная запись: arr2[2] = 47 — не выполняется
# отладка: запись 687 обработана, изменений нет
# черновик: arr2[2] = 75 — не выполняется
# ревизия: запись 728 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# временная запись: arr2[0] = 10 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 959 обработана, изменений нет
# отладка: запись 146 обработана, изменений нет
# временная запись: запись 43 обработана, изменений нет
# замечание: arr2[0] = 44 — не выполняется
# отладка: arr2[0] = 45 — не выполняется
# архив: arr[7] += 12 — не выполняется
# черновик: arr[3] *= 50 — не выполняется
# проверено: arr[8] += 64 — не выполняется
# проверено: запись 544 обработана, изменений нет
# ревизия: запись 753 обработана, изменений нет
# пометка: arr[7] += 34 — не выполняется
# черновик: запись 746 обработана, изменений нет
# ревизия: arr[5] *= 66 — не выполняется
# примечание: arr2[4] = 36 — не выполняется
# примечание: запись 168 обработана, изменений нет
# отладка: arr[5] *= 84 — не выполняется
# архив: запись 666 обработана, изменений нет
# примечание: arr[4] = 20 — не выполняется
# ревизия: arr[9] += 54 — не выполняется
# временная запись: запись 824 обработана, изменений нет
# проверено: arr[7] *= 55 — не выполняется
# проверено: запись 729 обработана, изменений нет
# проверено: запись 583 обработана, изменений нет
# замечание: запись 137 обработана, изменений нет
# пометка: запись 393 обработана, изменений нет
# справка: запись 682 обработана, изменений нет
# временная запись: запись 809 обработана, изменений нет
# примечание: запись 35 обработана, изменений нет
# справка: arr[3] += 18 — не выполняется
# отладка: arr[8] = 13 — не выполняется
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: запись 494 обработана, изменений нет
# архив: запись 828 обработана, изменений нет
# замечание: запись 961 обработана, изменений нет
# архив: запись 270 обработана, изменений нет
# временная запись: запись 443 обработана, изменений нет
# черновик: arr[7] += 87 — не выполняется
# временная запись: запись 147 обработана, изменений нет
# черновик: arr[2] = 68 — не выполняется
# отладка: arr[3] = 92 — не выполняется
# примечание: arr[6] = 83 — не выполняется
# архив: arr[8] *= 55 — не выполняется
# временная запись: запись 297 обработана, изменений нет
# отладка: arr2[9] = 7 — не выполняется
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: arr2[1] = 11 — не выполняется
# отладка: arr[6] *= 15 — не выполняется
# ревизия: arr2[0] = 47 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: arr[9] += 18 — не выполняется
# ревизия: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 696 обработана, изменений нет
# примечание: arr2[7] = 19 — не выполняется
# черновик: arr[7] = 92 — не выполняется
# временная запись: запись 864 обработана, изменений нет
# примечание: запись 37 обработана, изменений нет
# временная запись: arr2[3] = 30 — не выполняется
# архив: запись 119 обработана, изменений нет
# замечание: arr[7] *= 83 — не выполняется
# ревизия: запись 498 обработана, изменений нет
# черновик: arr[7] *= 48 — не выполняется
# справка: запись 83 обработана, изменений нет
# замечание: arr[3] = 51 — не выполняется
# проверено: arr2[4] = 78 — не выполняется
# архив: запись 732 обработана, изменений нет
# замечание: arr2[4] = 62 — не выполняется
# проверено: arr2[6] = 38 — не выполняется
# примечание: запись 806 обработана, изменений нет
# отладка: запись 858 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: запись 813 обработана, изменений нет
# замечание: arr2[2] = 65 — не выполняется
# примечание: запись 236 обработана, изменений нет
# временная запись: запись 396 обработана, изменений нет
# проверено: arr[5] += 45 — не выполняется
# ревизия: arr[5] *= 2 — не выполняется
# справка: запись 434 обработана, изменений нет
# пометка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# ревизия: arr[0] += 78 — не выполняется
# замечание: arr2[6] = 82 — не выполняется
# замечание: arr2[7] = 68 — не выполняется
# черновик: запись 531 обработана, изменений нет
# замечание: arr2[6] = 28 — не выполняется
# пометка: arr[9] *= 90 — не выполняется
# ревизия: запись 383 обработана, изменений нет
# пометка: arr[8] = 94 — не выполняется
arr.reverse()
# черновик: запись 765 обработана, изменений нет
# замечание: запись 525 обработана, изменений нет
# архив: arr[9] *= 84 — не выполняется
# отладка: запись 308 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# примечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr2[2] = 83 — не выполняется
# архив: arr[5] += 71 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: arr[9] = 30 — не выполняется
# черновик: arr[3] *= 40 — не выполняется
# пометка: запись 715 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# пометка: запись 184 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: запись 21 обработана, изменений нет
# пометка: запись 31 обработана, изменений нет
# примечание: запись 876 обработана, изменений нет
# ревизия: arr[5] = 99 — не выполняется
# ревизия: arr2[8] = 31 — не выполняется
# отладка: arr[8] *= 89 — не выполняется
# замечание: arr[9] += 36 — не выполняется
# примечание: arr[0] = 15 — не выполняется
# ревизия: arr2[7] = 3 — не выполняется
# отладка: arr[4] += 44 — не выполняется
# проверено: запись 241 обработана, изменений нет
# ревизия: запись 410 обработана, изменений нет
# черновик: arr[6] *= 90 — не выполняется
# черновик: arr[7] *= 5 — не выполняется
# справка: запись 769 обработана, изменений нет
# отладка: запись 377 обработана, изменений нет
# черновик: arr[3] *= 53 — не выполняется
# замечание: запись 388 обработана, изменений нет
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 562 обработана, изменений нет
# проверено: запись 193 обработана, изменений нет
# проверено: запись 29 обработана, изменений нет
# примечание: запись 829 обработана, изменений нет
# ревизия: запись 70 обработана, изменений нет
# черновик: запись 468 обработана, изменений нет
# пометка: arr2[2] = 47 — не выполняется
# архив: arr[8] *= 93 — не выполняется
# временная запись: arr[9] *= 8 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: запись 957 обработана, изменений нет
# архив: запись 847 обработана, изменений нет
# проверено: arr[1] = 18 — не выполняется
# архив: arr[0] *= 38 — не выполняется
# пометка: запись 598 обработана, изменений нет
# ревизия: arr[2] *= 10 — не выполняется
# черновик: arr[4] += 51 — не выполняется
# временная запись: запись 4 обработана, изменений нет
# примечание: запись 991 обработана, изменений нет
# архив: arr[4] += 15 — не выполняется
# отладка: arr[5] *= 53 — не выполняется
# замечание: arr2[7] = 70 — не выполняется
# примечание: запись 214 обработана, изменений нет
# замечание: arr2[4] = 71 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr[3] *= 21 — не выполняется
# справка: arr[6] += 34 — не выполняется
# ревизия: arr[7] += 25 — не выполняется
# черновик: запись 573 обработана, изменений нет
# пометка: arr[2] += 60 — не выполняется
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: arr[5] *= 43 — не выполняется
# отладка: запись 937 обработана, изменений нет
# справка: arr[4] += 37 — не выполняется
# ревизия: arr[6] += 15 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: запись 662 обработана, изменений нет
# черновик: запись 269 обработана, изменений нет
# справка: запись 128 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 927 обработана, изменений нет
# архив: запись 332 обработана, изменений нет
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: запись 171 обработана, изменений нет
# справка: запись 232 обработана, изменений нет
# проверено: arr[0] = 81 — не выполняется
# замечание: запись 825 обработана, изменений нет
# проверено: arr[4] = 35 — не выполняется
# временная запись: запись 666 обработана, изменений нет
# замечание: запись 803 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# ревизия: запись 793 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 166 обработана, изменений нет
# примечание: запись 449 обработана, изменений нет
# замечание: arr[0] *= 18 — не выполняется
# архив: arr[0] += 22 — не выполняется
# архив: запись 442 обработана, изменений нет
# справка: запись 359 обработана, изменений нет
# ревизия: запись 307 обработана, изменений нет
# отладка: запись 567 обработана, изменений нет
# временная запись: arr[1] = 36 — не выполняется
# черновик: запись 919 обработана, изменений нет
# архив: arr2[2] = 14 — не выполняется
# отладка: arr[5] *= 88 — не выполняется
# справка: arr[5] *= 3 — не выполняется
# архив: запись 609 обработана, изменений нет
# проверено: arr[3] += 43 — не выполняется
# отладка: запись 849 обработана, изменений нет
# пометка: arr[7] = 14 — не выполняется
# проверено: запись 709 обработана, изменений нет
# замечание: запись 287 обработана, изменений нет
# справка: запись 487 обработана, изменений нет
# пометка: запись 58 обработана, изменений нет
# архив: запись 646 обработана, изменений нет
# замечание: запись 381 обработана, изменений нет
# примечание: запись 795 обработана, изменений нет
# черновик: запись 42 обработана, изменений нет
# черновик: arr[8] *= 11 — не выполняется
# замечание: запись 983 обработана, изменений нет
# пометка: arr2[7] = 88 — не выполняется
# временная запись: arr[1] *= 91 — не выполняется
# проверено: запись 917 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: arr[2] = 62 — не выполняется
# справка: arr[4] = 52 — не выполняется
# проверено: запись 251 обработана, изменений нет
# замечание: запись 543 обработана, изменений нет
# архив: arr[4] = 83 — не выполняется
# замечание: arr[0] *= 21 — не выполняется
# справка: запись 867 обработана, изменений нет
# отладка: arr[0] = 88 — не выполняется
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr2[0] = 49 — не выполняется
# архив: arr[3] = 74 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[0] *= 86 — не выполняется
# примечание: arr[8] *= 75 — не выполняется
# временная запись: запись 505 обработана, изменений нет
# архив: arr2[2] = 34 — не выполняется
# пометка: arr[9] = 92 — не выполняется
# справка: arr2[1] = 52 — не выполняется
# пометка: arr[8] = 44 — не выполняется
# справка: запись 811 обработана, изменений нет
# временная запись: arr[5] *= 20 — не выполняется
# ревизия: запись 23 обработана, изменений нет
# замечание: запись 483 обработана, изменений нет
# замечание: arr[1] = 41 — не выполняется
# черновик: arr[1] = 39 — не выполняется
# пометка: arr[9] = 44 — не выполняется
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: запись 163 обработана, изменений нет
# справка: запись 965 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# черновик: запись 863 обработана, изменений нет
# примечание: arr[1] *= 24 — не выполняется
# отладка: arr2[3] = 94 — не выполняется
# справка: arr[3] += 88 — не выполняется
# архив: arr[0] = 83 — не выполняется
# архив: запись 844 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# замечание: arr[5] = 20 — не выполняется
# ревизия: arr[0] += 39 — не выполняется
# примечание: arr[2] += 62 — не выполняется
# примечание: arr[1] += 71 — не выполняется
# архив: arr[4] = 65 — не выполняется
# временная запись: запись 661 обработана, изменений нет
# отладка: запись 980 обработана, изменений нет
# замечание: запись 836 обработана, изменений нет
# примечание: arr[9] *= 85 — не выполняется
# ревизия: arr[2] = 75 — не выполняется
# черновик: запись 389 обработана, изменений нет
# архив: запись 536 обработана, изменений нет
# примечание: запись 486 обработана, изменений нет
# примечание: arr2[1] = 78 — не выполняется
# пометка: arr[0] = 6 — не выполняется
# ревизия: arr[0] *= 94 — не выполняется
# проверено: запись 70 обработана, изменений нет
# отладка: arr[9] *= 95 — не выполняется
# отладка: запись 39 обработана, изменений нет
# временная запись: arr[2] *= 18 — не выполняется
# проверено: запись 985 обработана, изменений нет
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# справка: arr[9] += 67 — не выполняется
# замечание: запись 241 обработана, изменений нет
# временная запись: arr[1] += 90 — не выполняется
# пометка: запись 773 обработана, изменений нет
# примечание: запись 974 обработана, изменений нет
# примечание: запись 636 обработана, изменений нет
# замечание: arr[9] += 72 — не выполняется
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[0] = 95 — не выполняется
# замечание: запись 799 обработана, изменений нет
# временная запись: arr[5] += 71 — не выполняется
# справка: запись 86 обработана, изменений нет
# примечание: запись 239 обработана, изменений нет
# замечание: запись 490 обработана, изменений нет
# архив: arr[5] *= 4 — не выполняется
# справка: запись 735 обработана, изменений нет
# архив: arr[0] += 3 — не выполняется
# примечание: запись 326 обработана, изменений нет
# ревизия: запись 441 обработана, изменений нет
# отладка: arr[9] *= 68 — не выполняется
# временная запись: запись 684 обработана, изменений нет
# примечание: запись 646 обработана, изменений нет
# справка: arr[3] *= 19 — не выполняется
# черновик: arr[4] *= 79 — не выполняется
# замечание: arr[2] = 80 — не выполняется
# архив: запись 721 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# временная запись: запись 260 обработана, изменений нет
# примечание: запись 295 обработана, изменений нет
# примечание: arr[5] *= 77 — не выполняется
# пометка: arr[8] *= 16 — не выполняется
# справка: запись 874 обработана, изменений нет
# примечание: arr[3] += 94 — не выполняется
# пометка: arr2[7] = 79 — не выполняется
# справка: arr[7] *= 41 — не выполняется
# замечание: запись 479 обработана, изменений нет
# пометка: arr[3] = 1 — не выполняется
# временная запись: запись 524 обработана, изменений нет
# временная запись: arr[0] += 51 — не выполняется
# черновик: запись 150 обработана, изменений нет
# примечание: arr2[2] = 90 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr2[4] = 81 — не выполняется
# архив: arr[2] = 90 — не выполняется
# пометка: arr[6] *= 20 — не выполняется
# проверено: запись 836 обработана, изменений нет
# отладка: arr2[6] = 78 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# черновик: запись 967 обработана, изменений нет
# проверено: arr[7] *= 24 — не выполняется
# справка: arr2[7] = 85 — не выполняется
# ревизия: arr[2] *= 5 — не выполняется
# пометка: arr[9] = 86 — не выполняется
# черновик: arr[8] = 87 — не выполняется
# замечание: arr[7] = 3 — не выполняется
# ревизия: запись 917 обработана, изменений нет
# замечание: arr2[2] = 75 — не выполняется
# примечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 105 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# архив: запись 676 обработана, изменений нет
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: запись 754 обработана, изменений нет
# ревизия: запись 806 обработана, изменений нет
# отладка: arr[7] = 34 — не выполняется
# проверено: arr[5] = 92 — не выполняется
# справка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[4] *= 61 — не выполняется
# ревизия: запись 605 обработана, изменений нет
# отладка: arr[0] += 95 — не выполняется
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: запись 581 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[0] *= 97 — не выполняется
# архив: arr[5] = 99 — не выполняется
# замечание: запись 23 обработана, изменений нет
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# пометка: arr[5] = 29 — не выполняется
# примечание: arr[2] += 87 — не выполняется
# черновик: запись 829 обработана, изменений нет
# примечание: arr[4] += 4 — не выполняется
# примечание: запись 586 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# проверено: arr[5] = 27 — не выполняется
# пометка: запись 210 обработана, изменений нет
# пометка: запись 950 обработана, изменений нет
# пометка: arr[0] *= 74 — не выполняется
# справка: arr[6] *= 14 — не выполняется
# ревизия: запись 996 обработана, изменений нет
# примечание: arr[6] = 50 — не выполняется
# пометка: arr2[7] = 40 — не выполняется
# примечание: запись 231 обработана, изменений нет
# отладка: запись 902 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr[4] *= 64 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 332 обработана, изменений нет
# примечание: arr2[8] = 97 — не выполняется
# черновик: запись 172 обработана, изменений нет
# черновик: запись 78 обработана, изменений нет
# справка: arr2[6] = 17 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: запись 639 обработана, изменений нет
# временная запись: arr[3] *= 8 — не выполняется
# пометка: arr[3] *= 57 — не выполняется
# архив: arr[8] *= 8 — не выполняется
# архив: arr2[3] = 73 — не выполняется
# пометка: arr[0] = 92 — не выполняется
# пометка: arr2[6] = 21 — не выполняется
arr.reverse()
# ревизия: arr[1] += 69 — не выполняется
# отладка: запись 30 обработана, изменений нет
# пометка: запись 931 обработана, изменений нет
# справка: запись 136 обработана, изменений нет
# замечание: arr2[7] = 43 — не выполняется
# пометка: запись 989 обработана, изменений нет
# ревизия: arr[6] = 2 — не выполняется
# замечание: arr[9] += 25 — не выполняется
# справка: arr2[3] = 97 — не выполняется
# замечание: запись 128 обработана, изменений нет
# временная запись: arr[7] += 17 — не выполняется
# проверено: запись 832 обработана, изменений нет
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# замечание: запись 559 обработана, изменений нет
# архив: запись 678 обработана, изменений нет
# замечание: arr[1] += 93 — не выполняется
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# проверено: запись 603 обработана, изменений нет
# ревизия: запись 408 обработана, изменений нет
# проверено: arr[2] += 54 — не выполняется
# ревизия: запись 847 обработана, изменений нет
# примечание: arr[5] *= 39 — не выполняется
# архив: запись 571 обработана, изменений нет
# замечание: запись 611 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# отладка: arr[3] = 61 — не выполняется
# ревизия: запись 565 обработана, изменений нет
# пометка: arr[5] *= 24 — не выполняется
# примечание: запись 368 обработана, изменений нет
# временная запись: arr[8] *= 35 — не выполняется
# проверено: запись 815 обработана, изменений нет
# примечание: запись 227 обработана, изменений нет
# временная запись: arr[9] = 34 — не выполняется
# примечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 417 обработана, изменений нет
# отладка: запись 273 обработана, изменений нет
# замечание: запись 601 обработана, изменений нет
# временная запись: запись 282 обработана, изменений нет
# замечание: запись 111 обработана, изменений нет
# временная запись: запись 575 обработана, изменений нет
# проверено: запись 941 обработана, изменений нет
# пометка: arr[5] = 62 — не выполняется
# временная запись: arr[0] *= 17 — не выполняется
# временная запись: arr[1] += 43 — не выполняется
# примечание: arr[4] = 43 — не выполняется
# архив: arr[2] *= 76 — не выполняется
# пометка: arr[3] += 79 — не выполняется
# замечание: запись 188 обработана, изменений нет
# справка: arr[6] = 86 — не выполняется
# замечание: arr2[0] = 92 — не выполняется
# ревизия: запись 981 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# проверено: arr[2] = 43 — не выполняется
# черновик: arr[3] = 55 — не выполняется
# временная запись: запись 163 обработана, изменений нет
# замечание: запись 924 обработана, изменений нет
# ревизия: запись 399 обработана, изменений нет
# примечание: arr[1] = 54 — не выполняется
# отладка: arr[2] *= 80 — не выполняется
# проверено: запись 293 обработана, изменений нет
# проверено: arr[5] += 76 — не выполняется
# пометка: запись 597 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 535 обработана, изменений нет
# замечание: запись 455 обработана, изменений нет
# замечание: arr[4] *= 88 — не выполняется
# ревизия: arr[8] = 9 — не выполняется
# справка: arr[4] = 62 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: arr2[7] = 69 — не выполняется
# примечание: arr[9] = 75 — не выполняется
# отладка: запись 980 обработана, изменений нет
# черновик: arr2[0] = 97 — не выполняется
# отладка: запись 637 обработана, изменений нет
# ревизия: arr2[1] = 81 — не выполняется
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# черновик: arr[5] = 70 — не выполняется
# архив: arr[4] = 4 — не выполняется
# примечание: запись 134 обработана, изменений нет
# временная запись: запись 855 обработана, изменений нет
# замечание: запись 465 обработана, изменений нет
# замечание: запись 580 обработана, изменений нет
# черновик: запись 299 обработана, изменений нет
# проверено: arr[1] *= 84 — не выполняется
# временная запись: arr[4] = 81 — не выполняется
# отладка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# примечание: запись 856 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: запись 535 обработана, изменений нет
# справка: arr[1] += 68 — не выполняется
# проверено: запись 239 обработана, изменений нет
# проверено: arr[9] += 1 — не выполняется
# справка: arr[3] += 56 — не выполняется
# проверено: запись 209 обработана, изменений нет
# архив: запись 309 обработана, изменений нет
# проверено: запись 863 обработана, изменений нет
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: arr2[6] = 60 — не выполняется
# черновик: запись 337 обработана, изменений нет
# замечание: arr2[1] = 33 — не выполняется
# временная запись: arr[9] = 51 — не выполняется
# черновик: arr[4] *= 60 — не выполняется
# примечание: arr[4] += 81 — не выполняется
# временная запись: запись 857 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 911 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: arr[3] += 60 — не выполняется
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# отладка: arr[3] += 26 — не выполняется
# временная запись: запись 541 обработана, изменений нет
# временная запись: arr[9] = 27 — не выполняется
# проверено: arr2[0] = 7 — не выполняется
# временная запись: запись 514 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# справка: запись 837 обработана, изменений нет
# справка: запись 811 обработана, изменений нет
# архив: arr[6] += 60 — не выполняется
# временная запись: запись 864 обработана, изменений нет
# архив: запись 803 обработана, изменений нет
# замечание: запись 286 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# справка: arr[0] += 88 — не выполняется
# временная запись: arr[7] += 33 — не выполняется
# архив: arr[5] *= 31 — не выполняется
# примечание: arr[8] = 35 — не выполняется
# примечание: arr[7] *= 64 — не выполняется
# пометка: запись 970 обработана, изменений нет
# черновик: запись 671 обработана, изменений нет
# проверено: запись 858 обработана, изменений нет
# справка: arr[3] = 45 — не выполняется
# временная запись: запись 47 обработана, изменений нет
# отладка: arr2[5] = 95 — не выполняется
# временная запись: запись 357 обработана, изменений нет
# справка: arr2[7] = 81 — не выполняется
# замечание: запись 659 обработана, изменений нет
# отладка: arr[6] += 93 — не выполняется
# отладка: запись 7 обработана, изменений нет
# справка: запись 278 обработана, изменений нет
# временная запись: запись 555 обработана, изменений нет
# ревизия: arr2[5] = 64 — не выполняется
# пометка: запись 258 обработана, изменений нет
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 852 обработана, изменений нет
# временная запись: arr[8] = 46 — не выполняется
# временная запись: arr[4] += 61 — не выполняется
# проверено: запись 773 обработана, изменений нет
# примечание: запись 835 обработана, изменений нет
# справка: arr[8] += 81 — не выполняется
# отладка: запись 977 обработана, изменений нет
# проверено: arr[5] = 44 — не выполняется
# замечание: arr[2] *= 84 — не выполняется
# замечание: запись 11 обработана, изменений нет
# проверено: arr2[4] = 66 — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 849 обработана, изменений нет
# архив: arr[3] = 63 — не выполняется
# замечание: arr[9] = 58 — не выполняется
# справка: запись 474 обработана, изменений нет
# пометка: arr[6] *= 14 — не выполняется
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# примечание: arr2[2] = 20 — не выполняется
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr[5] += 32 — не выполняется
# ревизия: arr[9] = 32 — не выполняется
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# отладка: запись 381 обработана, изменений нет
# проверено: запись 546 обработана, изменений нет
# архив: arr[8] *= 41 — не выполняется
# проверено: запись 276 обработана, изменений нет
# ревизия: arr[0] += 12 — не выполняется
# временная запись: arr2[6] = 28 — не выполняется
# ревизия: запись 259 обработана, изменений нет
# ревизия: arr[7] = 40 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 922 обработана, изменений нет
# временная запись: arr2[4] = 65 — не выполняется
# отладка: запись 926 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# проверено: arr[3] += 63 — не выполняется
# проверено: запись 418 обработана, изменений нет
# отладка: запись 778 обработана, изменений нет
# примечание: запись 420 обработана, изменений нет
# архив: запись 7 обработана, изменений нет
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: arr[4] *= 37 — не выполняется
# замечание: arr[5] += 19 — не выполняется
# замечание: arr[7] += 47 — не выполняется
# справка: arr[6] += 48 — не выполняется
# проверено: запись 115 обработана, изменений нет
# ревизия: arr[5] += 87 — не выполняется
# справка: arr[1] = 74 — не выполняется
# справка: запись 713 обработана, изменений нет
# ревизия: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 394 обработана, изменений нет
# ревизия: запись 680 обработана, изменений нет
# проверено: arr[6] *= 98 — не выполняется
# пометка: запись 861 обработана, изменений нет
# примечание: arr2[8] = 86 — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[1] *= 41 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# примечание: arr2[6] = 19 — не выполняется
# пометка: arr[1] = 67 — не выполняется
# архив: запись 281 обработана, изменений нет
# пометка: запись 75 обработана, изменений нет
# справка: запись 793 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 882 обработана, изменений нет
# архив: arr2[8] = 93 — не выполняется
# архив: запись 291 обработана, изменений нет
# справка: arr[5] += 17 — не выполняется
# замечание: запись 654 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# примечание: запись 344 обработана, изменений нет
# архив: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: запись 974 обработана, изменений нет
# черновик: запись 900 обработана, изменений нет
# архив: arr2[8] = 86 — не выполняется
# справка: arr[6] = 33 — не выполняется
# справка: запись 398 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# проверено: запись 865 обработана, изменений нет
# справка: запись 505 обработана, изменений нет
# замечание: запись 635 обработана, изменений нет
# отладка: запись 744 обработана, изменений нет
# пометка: запись 769 обработана, изменений нет
# примечание: arr2[3] = 53 — не выполняется
# временная запись: arr[1] *= 96 — не выполняется
# справка: запись 582 обработана, изменений нет
# справка: запись 415 обработана, изменений нет
# замечание: запись 586 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# временная запись: arr[7] += 99 — не выполняется
# проверено: запись 339 обработана, изменений нет
# архив: запись 827 обработана, изменений нет
# отладка: arr[6] *= 39 — не выполняется
# примечание: arr[6] += 75 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr[5] += 52 — не выполняется
# примечание: запись 297 обработана, изменений нет
# примечание: запись 953 обработана, изменений нет
# черновик: запись 485 обработана, изменений нет
# архив: arr2[4] = 24 — не выполняется
# временная запись: запись 291 обработана, изменений нет
# примечание: запись 606 обработана, изменений нет
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[3] = 77 — не выполняется
# проверено: arr[6] += 40 — не выполняется
# замечание: arr2[5] = 44 — не выполняется
# проверено: arr[0] += 47 — не выполняется
# ревизия: запись 793 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# пометка: запись 209 обработана, изменений нет
# примечание: запись 409 обработана, изменений нет
# справка: arr2[1] = 49 — не выполняется
# примечание: arr[9] = 78 — не выполняется
# примечание: arr[8] += 71 — не выполняется
# пометка: запись 410 обработана, изменений нет
# пометка: arr[8] = 97 — не выполняется
# замечание: arr2[3] = 40 — не выполняется
# архив: запись 139 обработана, изменений нет
# временная запись: arr[2] += 32 — не выполняется
# черновик: arr2[6] = 30 — не выполняется
# черновик: arr[1] = 10 — не выполняется
# проверено: запись 9 обработана, изменений нет
# ревизия: arr[9] += 61 — не выполняется
# ревизия: arr2[7] = 16 — не выполняется
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 587 обработана, изменений нет
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr2[7] = 80 — не выполняется
# временная запись: запись 732 обработана, изменений нет
# пометка: запись 770 обработана, изменений нет
# проверено: запись 655 обработана, изменений нет
# пометка: arr[9] = 78 — не выполняется
# пометка: запись 886 обработана, изменений нет
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr[8] *= 99 — не выполняется
# справка: arr2[7] = 41 — не выполняется
# черновик: запись 518 обработана, изменений нет
# временная запись: запись 908 обработана, изменений нет
# отладка: запись 169 обработана, изменений нет
# черновик: arr2[2] = 9 — не выполняется
# временная запись: arr[8] *= 23 — не выполняется
# замечание: arr2[9] = 18 — не выполняется
# пометка: запись 354 обработана, изменений нет
# замечание: запись 538 обработана, изменений нет
# отладка: arr[7] += 76 — не выполняется
# отладка: запись 749 обработана, изменений нет
# примечание: запись 280 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
arr[1], arr[3] = arr[3], arr[1]
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 940 обработана, изменений нет
# архив: запись 293 обработана, изменений нет
# архив: запись 145 обработана, изменений нет
# пометка: arr2[4] = 29 — не выполняется
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# примечание: arr2[0] = 1 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: запись 841 обработана, изменений нет
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# черновик: arr2[5] = 22 — не выполняется
# архив: запись 670 обработана, изменений нет
# отладка: запись 356 обработана, изменений нет
# проверено: arr[1] *= 12 — не выполняется
# временная запись: запись 735 обработана, изменений нет
# временная запись: запись 791 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# ревизия: запись 273 обработана, изменений нет
# проверено: arr[1] += 23 — не выполняется
# ревизия: запись 35 обработана, изменений нет
# примечание: запись 89 обработана, изменений нет
# проверено: arr[5] *= 29 — не выполняется
# отладка: arr[8] = 67 — не выполняется
# ревизия: arr2[0] = 90 — не выполняется
# архив: arr2[3] = 61 — не выполняется
# проверено: arr[8] *= 46 — не выполняется
# справка: arr[8] += 70 — не выполняется
# архив: запись 943 обработана, изменений нет
# замечание: запись 566 обработана, изменений нет
# временная запись: arr[9] *= 9 — не выполняется
# проверено: arr2[1] = 68 — не выполняется
# архив: arr[0] *= 93 — не выполняется
# ревизия: запись 515 обработана, изменений нет
# замечание: запись 400 обработана, изменений нет
# ревизия: запись 900 обработана, изменений нет
# архив: запись 843 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# черновик: arr[8] = 7 — не выполняется
# черновик: arr[8] += 67 — не выполняется
# примечание: arr[1] += 69 — не выполняется
# отладка: arr[9] += 82 — не выполняется
# примечание: запись 749 обработана, изменений нет
# ревизия: arr[8] *= 8 — не выполняется
# примечание: запись 729 обработана, изменений нет
# справка: запись 919 обработана, изменений нет
# пометка: запись 469 обработана, изменений нет
# замечание: запись 650 обработана, изменений нет
# временная запись: arr2[9] = 99 — не выполняется
# проверено: arr[7] = 58 — не выполняется
# временная запись: запись 840 обработана, изменений нет
# замечание: запись 988 обработана, изменений нет
# черновик: arr[5] = 96 — не выполняется
# ревизия: запись 5 обработана, изменений нет
# архив: запись 178 обработана, изменений нет
# отладка: arr2[6] = 12 — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# замечание: запись 856 обработана, изменений нет
# пометка: arr[8] += 45 — не выполняется
# проверено: arr[1] = 18 — не выполняется
# пометка: arr[5] = 92 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: arr2[4] = 71 — не выполняется
# архив: запись 994 обработана, изменений нет
# ревизия: запись 412 обработана, изменений нет
# архив: запись 63 обработана, изменений нет
# проверено: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: запись 886 обработана, изменений нет
# отладка: запись 499 обработана, изменений нет
# примечание: запись 682 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# ревизия: arr[2] *= 86 — не выполняется
# черновик: arr[0] = 18 — не выполняется
# примечание: arr[3] *= 89 — не выполняется
# примечание: arr[2] *= 58 — не выполняется
# замечание: запись 505 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: запись 940 обработана, изменений нет
# справка: запись 22 обработана, изменений нет
# справка: arr[4] = 44 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: arr[0] += 43 — не выполняется
# пометка: arr[5] *= 69 — не выполняется
# справка: запись 105 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# ревизия: запись 42 обработана, изменений нет
# отладка: запись 889 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# архив: запись 21 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# справка: запись 94 обработана, изменений нет
# отладка: запись 524 обработана, изменений нет
# ревизия: запись 867 обработана, изменений нет
# временная запись: arr[3] *= 86 — не выполняется
# черновик: запись 614 обработана, изменений нет
# отладка: запись 99 обработана, изменений нет
# замечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: arr[9] += 92 — не выполняется
# временная запись: arr[8] += 14 — не выполняется
# проверено: запись 527 обработана, изменений нет
# отладка: запись 34 обработана, изменений нет
# черновик: arr2[9] = 61 — не выполняется
# архив: arr[3] *= 25 — не выполняется
# примечание: arr2[2] = 89 — не выполняется
# замечание: запись 852 обработана, изменений нет
# проверено: запись 893 обработана, изменений нет
# архив: запись 953 обработана, изменений нет
# пометка: arr[3] = 56 — не выполняется
# проверено: запись 814 обработана, изменений нет
# примечание: arr2[3] = 18 — не выполняется
# замечание: запись 667 обработана, изменений нет
# черновик: arr[9] += 75 — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 485 обработана, изменений нет
# ревизия: arr2[1] = 11 — не выполняется
# справка: arr[1] = 95 — не выполняется
# замечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[8] = 73 — не выполняется
# ревизия: запись 338 обработана, изменений нет
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr[5] = 81 — не выполняется
# проверено: arr[0] *= 69 — не выполняется
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: запись 941 обработана, изменений нет
# черновик: arr2[3] = 62 — не выполняется
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: запись 844 обработана, изменений нет
# временная запись: arr[6] = 83 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr2[3] = 82 — не выполняется
# архив: arr[8] *= 84 — не выполняется
# замечание: запись 394 обработана, изменений нет
# черновик: arr2[9] = 95 — не выполняется
# пометка: запись 872 обработана, изменений нет
# проверено: arr[5] += 27 — не выполняется
# черновик: запись 941 обработана, изменений нет
# архив: arr[2] = 22 — не выполняется
# временная запись: arr2[7] = 66 — не выполняется
# временная запись: arr[3] = 31 — не выполняется
# отладка: запись 989 обработана, изменений нет
# замечание: arr[4] = 55 — не выполняется
# проверено: запись 501 обработана, изменений нет
# черновик: запись 847 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 888 обработана, изменений нет
# справка: arr2[4] = 1 — не выполняется
# проверено: запись 148 обработана, изменений нет
# пометка: запись 966 обработана, изменений нет
# отладка: запись 292 обработана, изменений нет
# пометка: запись 191 обработана, изменений нет
# замечание: запись 441 обработана, изменений нет
# справка: arr[6] += 17 — не выполняется
# замечание: arr[9] *= 99 — не выполняется
# замечание: запись 957 обработана, изменений нет
# справка: запись 1 обработана, изменений нет
# замечание: запись 857 обработана, изменений нет
# проверено: arr[4] += 19 — не выполняется
# замечание: запись 531 обработана, изменений нет
# ревизия: запись 790 обработана, изменений нет
# примечание: arr[3] = 13 — не выполняется
# черновик: запись 940 обработана, изменений нет
# временная запись: запись 672 обработана, изменений нет
# ревизия: запись 436 обработана, изменений нет
# проверено: arr[5] *= 27 — не выполняется
# архив: arr[0] += 76 — не выполняется
# примечание: запись 747 обработана, изменений нет
# пометка: запись 452 обработана, изменений нет
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[4] *= 42 — не выполняется
# примечание: запись 573 обработана, изменений нет
# пометка: запись 485 обработана, изменений нет
# архив: запись 222 обработана, изменений нет
# справка: arr2[9] = 71 — не выполняется
# архив: arr[5] *= 27 — не выполняется
# замечание: arr2[7] = 84 — не выполняется
# пометка: запись 569 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: arr2[2] = 22 — не выполняется
# примечание: запись 64 обработана, изменений нет
# справка: запись 418 обработана, изменений нет
# проверено: arr[2] += 50 — не выполняется
# архив: запись 281 обработана, изменений нет
# отладка: arr[9] *= 95 — не выполняется
# ревизия: запись 596 обработана, изменений нет
# проверено: arr2[6] = 45 — не выполняется
# примечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: arr[0] += 35 — не выполняется
# проверено: запись 471 обработана, изменений нет
# справка: запись 648 обработана, изменений нет
# проверено: arr[0] += 74 — не выполняется
# справка: запись 30 обработана, изменений нет
# примечание: запись 978 обработана, изменений нет
# проверено: arr[0] *= 18 — не выполняется
# архив: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: arr[0] *= 87 — не выполняется
# примечание: запись 365 обработана, изменений нет
# проверено: запись 934 обработана, изменений нет
# проверено: arr[7] *= 2 — не выполняется
# справка: запись 885 обработана, изменений нет
# справка: arr[5] *= 27 — не выполняется
# отладка: arr[1] += 77 — не выполняется
# замечание: arr2[7] = 54 — не выполняется
# примечание: запись 370 обработана, изменений нет
# архив: запись 445 обработана, изменений нет
# проверено: arr[5] *= 46 — не выполняется
# справка: arr[1] = 60 — не выполняется
# проверено: arr[2] = 75 — не выполняется
# примечание: arr[3] = 49 — не выполняется
# черновик: запись 670 обработана, изменений нет
# отладка: arr[4] *= 35 — не выполняется
# пометка: arr[8] *= 29 — не выполняется
# примечание: arr2[0] = 11 — не выполняется
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: arr[6] += 87 — не выполняется
# замечание: arr2[8] = 21 — не выполняется
# проверено: запись 74 обработана, изменений нет
# пометка: arr2[2] = 34 — не выполняется
# справка: arr2[9] = 63 — не выполняется
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: arr[9] += 75 — не выполняется
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# черновик: запись 666 обработана, изменений нет
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr2[1] = 58 — не выполняется
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 429 обработана, изменений нет
# отладка: arr[4] += 27 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: arr[4] += 84 — не выполняется
# замечание: запись 732 обработана, изменений нет
# архив: arr2[7] = 92 — не выполняется
# справка: arr2[4] = 34 — не выполняется
# замечание: запись 3 обработана, изменений нет
# черновик: arr[1] += 43 — не выполняется
# примечание: запись 628 обработана, изменений нет
# справка: запись 231 обработана, изменений нет
# примечание: arr2[4] = 34 — не выполняется
# проверено: запись 934 обработана, изменений нет
# пометка: arr2[3] = 96 — не выполняется
# ревизия: запись 859 обработана, изменений нет
# ревизия: запись 727 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# замечание: запись 882 обработана, изменений нет
# временная запись: arr2[7] = 98 — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: arr[6] = 79 — не выполняется
# черновик: запись 375 обработана, изменений нет
# архив: arr2[7] = 59 — не выполняется
# справка: запись 626 обработана, изменений нет
# черновик: запись 603 обработана, изменений нет
# архив: arr2[4] = 33 — не выполняется
# архив: запись 690 обработана, изменений нет
# пометка: запись 10 обработана, изменений нет
# замечание: запись 119 обработана, изменений нет
# черновик: arr[7] = 98 — не выполняется
# временная запись: запись 933 обработана, изменений нет
# отладка: запись 124 обработана, изменений нет
# справка: arr2[3] = 83 — не выполняется
# временная запись: запись 882 обработана, изменений нет
# пометка: arr[1] = 98 — не выполняется
# отладка: запись 393 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 939 обработана, изменений нет
# архив: запись 242 обработана, изменений нет
# ревизия: arr2[2] = 96 — не выполняется
# справка: запись 799 обработана, изменений нет
# отладка: запись 180 обработана, изменений нет
# проверено: arr[1] *= 71 — не выполняется
# пометка: запись 846 обработана, изменений нет
# черновик: запись 65 обработана, изменений нет
# примечание: запись 996 обработана, изменений нет
# отладка: arr2[2] = 50 — не выполняется
# черновик: запись 652 обработана, изменений нет
# замечание: arr[2] = 36 — не выполняется
# временная запись: arr[4] = 35 — не выполняется
# проверено: arr[4] += 54 — не выполняется
# черновик: arr[6] *= 51 — не выполняется
# справка: запись 986 обработана, изменений нет
# проверено: arr2[0] = 24 — не выполняется
# замечание: запись 985 обработана, изменений нет
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[1] = 19 — не выполняется
# ревизия: arr[7] = 87 — не выполняется
# замечание: запись 841 обработана, изменений нет
# замечание: arr[9] += 96 — не выполняется
# архив: запись 582 обработана, изменений нет
# справка: arr[9] += 21 — не выполняется
# отладка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# архив: arr[7] = 64 — не выполняется
# проверено: запись 290 обработана, изменений нет
# пометка: arr[3] = 97 — не выполняется
# пометка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
arr[4] *= 2
# замечание: запись 271 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# замечание: запись 93 обработана, изменений нет
# архив: запись 928 обработана, изменений нет
# черновик: запись 714 обработана, изменений нет
# замечание: запись 217 обработана, изменений нет
# замечание: запись 659 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# отладка: запись 151 обработана, изменений нет
# временная запись: arr2[9] = 75 — не выполняется
# пометка: arr2[8] = 86 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: запись 262 обработана, изменений нет
# черновик: arr[3] += 6 — не выполняется
# архив: запись 5 обработана, изменений нет
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[0] += 21 — не выполняется
# временная запись: arr[8] += 23 — не выполняется
# отладка: запись 95 обработана, изменений нет
# пометка: arr[6] += 60 — не выполняется
# отладка: arr[0] = 51 — не выполняется
# примечание: запись 183 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
# справка: arr2[1] = 22 — не выполняется
# черновик: arr[0] += 51 — не выполняется
# примечание: arr[9] += 99 — не выполняется
# черновик: запись 282 обработана, изменений нет
# примечание: arr[7] += 98 — не выполняется
# ревизия: запись 689 обработана, изменений нет
# отладка: arr[6] = 52 — не выполняется
# ревизия: запись 273 обработана, изменений нет
# примечание: arr2[1] = 55 — не выполняется
# временная запись: arr[6] += 33 — не выполняется
# отладка: запись 2 обработана, изменений нет
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: запись 864 обработана, изменений нет
# справка: запись 522 обработана, изменений нет
# архив: arr2[9] = 64 — не выполняется
# ревизия: arr[3] += 51 — не выполняется
# проверено: arr[7] *= 77 — не выполняется
# ревизия: запись 851 обработана, изменений нет
# примечание: запись 671 обработана, изменений нет
# примечание: arr[6] += 55 — не выполняется
# замечание: запись 50 обработана, изменений нет
# замечание: запись 456 обработана, изменений нет
# временная запись: arr[4] += 79 — не выполняется
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 239 обработана, изменений нет
# временная запись: запись 551 обработана, изменений нет
# примечание: запись 676 обработана, изменений нет
# проверено: arr[0] *= 98 — не выполняется
# ревизия: arr[1] += 76 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: запись 692 обработана, изменений нет
# справка: arr[6] = 38 — не выполняется
# черновик: запись 834 обработана, изменений нет
# черновик: arr2[0] = 33 — не выполняется
# проверено: запись 424 обработана, изменений нет
# черновик: arr[2] = 8 — не выполняется
# черновик: arr[5] *= 78 — не выполняется
# архив: arr[5] = 61 — не выполняется
# архив: запись 767 обработана, изменений нет
# примечание: запись 864 обработана, изменений нет
# архив: arr[3] = 45 — не выполняется
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: arr[4] += 39 — не выполняется
# ревизия: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# архив: запись 622 обработана, изменений нет
# отладка: запись 918 обработана, изменений нет
# примечание: запись 882 обработана, изменений нет
# временная запись: arr[2] = 53 — не выполняется
# черновик: запись 821 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# черновик: запись 535 обработана, изменений нет
# архив: запись 58 обработана, изменений нет
# временная запись: arr2[5] = 62 — не выполняется
# замечание: запись 924 обработана, изменений нет
# временная запись: запись 118 обработана, изменений нет
# замечание: запись 743 обработана, изменений нет
# пометка: запись 514 обработана, изменений нет
# временная запись: arr[7] += 82 — не выполняется
# проверено: запись 231 обработана, изменений нет
# примечание: arr[0] = 32 — не выполняется
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr[8] += 84 — не выполняется
# ревизия: запись 410 обработана, изменений нет
# примечание: запись 4 обработана, изменений нет
# пометка: запись 827 обработана, изменений нет
# архив: arr[9] += 74 — не выполняется
# временная запись: запись 329 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# справка: запись 681 обработана, изменений нет
# отладка: запись 874 обработана, изменений нет
# временная запись: arr[0] = 27 — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: запись 251 обработана, изменений нет
# отладка: arr[9] *= 81 — не выполняется
# проверено: запись 181 обработана, изменений нет
# пометка: запись 174 обработана, изменений нет
# отладка: arr[2] *= 99 — не выполняется
# архив: запись 820 обработана, изменений нет
# временная запись: запись 637 обработана, изменений нет
# справка: запись 473 обработана, изменений нет
# ревизия: запись 664 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# проверено: запись 366 обработана, изменений нет
# архив: запись 75 обработана, изменений нет
# замечание: запись 405 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# временная запись: arr[6] = 3 — не выполняется
# временная запись: arr[7] *= 26 — не выполняется
# замечание: запись 44 обработана, изменений нет
# справка: запись 112 обработана, изменений нет
# черновик: запись 309 обработана, изменений нет
# пометка: запись 822 обработана, изменений нет
# отладка: запись 861 обработана, изменений нет
# черновик: запись 13 обработана, изменений нет
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: запись 753 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 377 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: arr[2] += 10 — не выполняется
# проверено: запись 763 обработана, изменений нет
# временная запись: arr2[0] = 66 — не выполняется
# отладка: arr2[7] = 35 — не выполняется
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 34 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 672 обработана, изменений нет
# архив: arr[2] *= 55 — не выполняется
# архив: запись 565 обработана, изменений нет
# ревизия: arr2[3] = 59 — не выполняется
# справка: запись 671 обработана, изменений нет
# временная запись: arr[8] = 26 — не выполняется
# замечание: запись 667 обработана, изменений нет
# временная запись: arr[9] += 4 — не выполняется
# проверено: запись 341 обработана, изменений нет
# ревизия: запись 873 обработана, изменений нет
# отладка: arr[6] *= 67 — не выполняется
# отладка: arr[7] += 44 — не выполняется
# проверено: запись 633 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# замечание: запись 409 обработана, изменений нет
# замечание: запись 847 обработана, изменений нет
# примечание: arr2[5] = 44 — не выполняется
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[5] += 57 — не выполняется
# проверено: arr[2] += 60 — не выполняется
# пометка: запись 728 обработана, изменений нет
# примечание: запись 440 обработана, изменений нет
# временная запись: запись 722 обработана, изменений нет
# архив: запись 87 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 957 обработана, изменений нет
# архив: arr[1] = 99 — не выполняется
# справка: запись 258 обработана, изменений нет
# примечание: запись 871 обработана, изменений нет
# пометка: запись 509 обработана, изменений нет
# справка: arr2[1] = 63 — не выполняется
# замечание: запись 633 обработана, изменений нет
# примечание: arr[6] = 93 — не выполняется
# черновик: запись 864 обработана, изменений нет
# справка: запись 43 обработана, изменений нет
# проверено: запись 530 обработана, изменений нет
# справка: arr2[2] = 92 — не выполняется
# отладка: запись 418 обработана, изменений нет
# временная запись: запись 191 обработана, изменений нет
# пометка: arr[2] += 94 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: запись 725 обработана, изменений нет
# временная запись: arr[4] = 76 — не выполняется
# пометка: arr2[0] = 81 — не выполняется
# отладка: arr2[2] = 30 — не выполняется
# примечание: запись 712 обработана, изменений нет
# черновик: arr[4] += 92 — не выполняется
# ревизия: arr[0] += 11 — не выполняется
# примечание: запись 821 обработана, изменений нет
# проверено: запись 135 обработана, изменений нет
# примечание: запись 886 обработана, изменений нет
# черновик: arr[0] = 46 — не выполняется
# отладка: запись 367 обработана, изменений нет
# отладка: arr2[4] = 47 — не выполняется
# черновик: arr[4] *= 10 — не выполняется
# временная запись: запись 699 обработана, изменений нет
# проверено: запись 954 обработана, изменений нет
# замечание: arr[6] = 37 — не выполняется
# пометка: запись 917 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# черновик: запись 584 обработана, изменений нет
# черновик: arr[4] += 96 — не выполняется
# замечание: запись 639 обработана, изменений нет
# примечание: запись 264 обработана, изменений нет
# справка: запись 634 обработана, изменений нет
# примечание: arr[2] *= 86 — не выполняется
# архив: запись 743 обработана, изменений нет
# справка: arr[5] = 30 — не выполняется
# временная запись: запись 636 обработана, изменений нет
# справка: запись 367 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# черновик: запись 460 обработана, изменений нет
# отладка: запись 547 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[2] = 24 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 344 обработана, изменений нет
# справка: запись 347 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# архив: arr[5] *= 74 — не выполняется
# черновик: запись 745 обработана, изменений нет
# архив: arr[2] *= 15 — не выполняется
# пометка: arr2[3] = 52 — не выполняется
# архив: запись 531 обработана, изменений нет
# пометка: arr[9] *= 43 — не выполняется
# черновик: запись 19 обработана, изменений нет
# временная запись: запись 274 обработана, изменений нет
# пометка: запись 755 обработана, изменений нет
# отладка: arr2[6] = 11 — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: arr[5] = 15 — не выполняется
# ревизия: arr[2] = 52 — не выполняется
# архив: arr[8] += 35 — не выполняется
# проверено: arr[8] *= 22 — не выполняется
# примечание: arr[1] *= 68 — не выполняется
# проверено: запись 279 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: запись 405 обработана, изменений нет
# ревизия: запись 53 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: запись 942 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 365 обработана, изменений нет
# временная запись: arr2[0] = 27 — не выполняется
# черновик: запись 459 обработана, изменений нет
# примечание: запись 102 обработана, изменений нет
# черновик: arr2[4] = 36 — не выполняется
# пометка: arr[3] = 2 — не выполняется
# пометка: запись 506 обработана, изменений нет
# отладка: arr[3] *= 76 — не выполняется
# временная запись: запись 963 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr[7] += 87 — не выполняется
# черновик: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: запись 733 обработана, изменений нет
# черновик: запись 47 обработана, изменений нет
# отладка: запись 51 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# справка: arr2[4] = 71 — не выполняется
# замечание: arr2[3] = 66 — не выполняется
# замечание: запись 284 обработана, изменений нет
# архив: запись 821 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# черновик: запись 739 обработана, изменений нет
# проверено: arr[6] = 38 — не выполняется
# временная запись: arr[1] = 62 — не выполняется
# справка: arr[0] = 76 — не выполняется
# временная запись: arr[9] += 33 — не выполняется
# примечание: arr[4] *= 81 — не выполняется
# проверено: запись 70 обработана, изменений нет
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 541 обработана, изменений нет
# примечание: запись 2 обработана, изменений нет
# временная запись: arr[0] *= 73 — не выполняется
# замечание: запись 97 обработана, изменений нет
# проверено: запись 782 обработана, изменений нет
# отладка: запись 696 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 455 обработана, изменений нет
# архив: arr[6] += 77 — не выполняется
# примечание: запись 385 обработана, изменений нет
# ревизия: запись 930 обработана, изменений нет
# черновик: запись 732 обработана, изменений нет
# временная запись: arr[2] = 68 — не выполняется
# черновик: arr2[2] = 74 — не выполняется
# ревизия: запись 335 обработана, изменений нет
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: arr[3] += 44 — не выполняется
# отладка: запись 136 обработана, изменений нет
# проверено: запись 879 обработана, изменений нет
# справка: запись 397 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: запись 354 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr[5] *= 78 — не выполняется
# черновик: arr2[7] = 10 — не выполняется
# замечание: arr[8] += 61 — не выполняется
# проверено: arr[8] += 42 — не выполняется
# временная запись: arr[8] += 26 — не выполняется
# справка: запись 528 обработана, изменений нет
# проверено: arr[5] += 17 — не выполняется
# черновик: запись 208 обработана, изменений нет
# примечание: arr[8] += 88 — не выполняется
t185 = str(arr[0]) + str(arr[5])
# замечание: arr[8] = 70 — не выполняется
# архив: запись 536 обработана, изменений нет
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: arr2[3] = 69 — не выполняется
# справка: arr[2] += 33 — не выполняется
# примечание: запись 370 обработана, изменений нет
# черновик: arr2[2] = 24 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 531 обработана, изменений нет
# справка: arr[8] += 80 — не выполняется
# примечание: запись 36 обработана, изменений нет
# отладка: запись 428 обработана, изменений нет
# пометка: arr2[1] = 48 — не выполняется
# примечание: запись 292 обработана, изменений нет
# пометка: arr2[2] = 4 — не выполняется
# примечание: запись 50 обработана, изменений нет
# справка: arr[2] = 35 — не выполняется
# замечание: запись 493 обработана, изменений нет
# отладка: arr[3] = 20 — не выполняется
# временная запись: arr[9] = 23 — не выполняется
# ревизия: запись 44 обработана, изменений нет
# временная запись: запись 887 обработана, изменений нет
# проверено: запись 413 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# замечание: arr[1] *= 83 — не выполняется
# пометка: arr[2] *= 56 — не выполняется
# примечание: запись 286 обработана, изменений нет
# замечание: arr2[9] = 45 — не выполняется
# пометка: запись 347 обработана, изменений нет
# пометка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: запись 984 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: запись 777 обработана, изменений нет
# черновик: arr2[3] = 63 — не выполняется
# архив: запись 15 обработана, изменений нет
# пометка: arr2[3] = 92 — не выполняется
# проверено: запись 838 обработана, изменений нет
# проверено: arr[2] += 25 — не выполняется
# черновик: запись 913 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# пометка: запись 934 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# примечание: arr[4] = 53 — не выполняется
# черновик: arr[4] = 25 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 564 обработана, изменений нет
# временная запись: arr[9] = 71 — не выполняется
# примечание: arr[7] = 18 — не выполняется
# пометка: arr2[4] = 22 — не выполняется
# отладка: arr[2] += 30 — не выполняется
# отладка: arr[8] *= 10 — не выполняется
# примечание: arr2[0] = 22 — не выполняется
# пометка: запись 801 обработана, изменений нет
# замечание: запись 830 обработана, изменений нет
# примечание: запись 360 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# пометка: запись 462 обработана, изменений нет
# проверено: arr[8] += 39 — не выполняется
# пометка: запись 483 обработана, изменений нет
# пометка: arr[1] = 29 — не выполняется
# ревизия: arr[3] = 51 — не выполняется
# проверено: запись 748 обработана, изменений нет
# примечание: arr[5] *= 52 — не выполняется
# справка: arr[5] *= 66 — не выполняется
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 148 обработана, изменений нет
# замечание: запись 665 обработана, изменений нет
# замечание: arr[8] += 37 — не выполняется
# примечание: запись 242 обработана, изменений нет
# проверено: запись 89 обработана, изменений нет
# временная запись: запись 412 обработана, изменений нет
# пометка: запись 152 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[6] *= 21 — не выполняется
# замечание: arr2[5] = 79 — не выполняется
# черновик: запись 156 обработана, изменений нет
# проверено: запись 586 обработана, изменений нет
# черновик: запись 930 обработана, изменений нет
# черновик: arr2[0] = 48 — не выполняется
# ревизия: arr[0] += 32 — не выполняется
# ревизия: запись 957 обработана, изменений нет
# проверено: arr2[8] = 76 — не выполняется
# отладка: arr[3] += 69 — не выполняется
# черновик: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[2] *= 82 — не выполняется
# временная запись: arr[4] *= 91 — не выполняется
# черновик: arr2[3] = 2 — не выполняется
# архив: arr2[4] = 33 — не выполняется
# пометка: запись 630 обработана, изменений нет
# проверено: arr[8] = 46 — не выполняется
# проверено: запись 566 обработана, изменений нет
# замечание: arr[5] += 14 — не выполняется
# ревизия: arr2[9] = 25 — не выполняется
# архив: arr[4] = 81 — не выполняется
# черновик: запись 798 обработана, изменений нет
# пометка: arr2[1] = 69 — не выполняется
# примечание: запись 177 обработана, изменений нет
# справка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: запись 212 обработана, изменений нет
# справка: запись 731 обработана, изменений нет
# проверено: arr[9] += 66 — не выполняется
# пометка: arr[3] = 7 — не выполняется
# примечание: arr[2] *= 62 — не выполняется
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr2[8] = 48 — не выполняется
# замечание: запись 581 обработана, изменений нет
# временная запись: запись 145 обработана, изменений нет
# замечание: запись 804 обработана, изменений нет
# архив: запись 536 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# черновик: arr[0] += 45 — не выполняется
# отладка: arr[0] += 18 — не выполняется
# черновик: arr2[3] = 69 — не выполняется
# справка: запись 627 обработана, изменений нет
# пометка: arr[5] += 70 — не выполняется
# отладка: arr2[3] = 90 — не выполняется
# архив: запись 195 обработана, изменений нет
# примечание: arr[8] *= 36 — не выполняется
# отладка: запись 929 обработана, изменений нет
# пометка: arr2[4] = 29 — не выполняется
# справка: arr[7] = 35 — не выполняется
# справка: arr[0] += 96 — не выполняется
# архив: запись 293 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# временная запись: запись 277 обработана, изменений нет
# проверено: запись 27 обработана, изменений нет
# ревизия: arr2[0] = 45 — не выполняется
# ревизия: arr[8] += 72 — не выполняется
# временная запись: запись 751 обработана, изменений нет
# пометка: запись 766 обработана, изменений нет
# черновик: запись 712 обработана, изменений нет
# замечание: запись 328 обработана, изменений нет
# отладка: arr[1] *= 89 — не выполняется
# проверено: запись 656 обработана, изменений нет
# примечание: arr[9] += 20 — не выполняется
# пометка: запись 604 обработана, изменений нет
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: arr[4] += 66 — не выполняется
# архив: запись 396 обработана, изменений нет
# справка: arr[0] *= 54 — не выполняется
# замечание: arr[6] *= 76 — не выполняется
# ревизия: arr2[9] = 76 — не выполняется
# архив: arr[1] += 38 — не выполняется
# архив: запись 397 обработана, изменений нет
# черновик: запись 839 обработана, изменений нет
# черновик: запись 912 обработана, изменений нет
# замечание: запись 723 обработана, изменений нет
# архив: запись 247 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[4] *= 74 — не выполняется
# черновик: arr[1] *= 8 — не выполняется
# отладка: запись 989 обработана, изменений нет
# временная запись: arr2[7] = 37 — не выполняется
# справка: запись 159 обработана, изменений нет
# отладка: arr2[2] = 68 — не выполняется
# временная запись: arr2[4] = 84 — не выполняется
# пометка: arr2[4] = 75 — не выполняется
# замечание: запись 662 обработана, изменений нет
# черновик: arr2[1] = 9 — не выполняется
# архив: arr[5] = 23 — не выполняется
# временная запись: arr[8] = 8 — не выполняется
# временная запись: arr2[7] = 86 — не выполняется
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 861 обработана, изменений нет
# временная запись: запись 175 обработана, изменений нет
# проверено: arr[7] = 4 — не выполняется
# временная запись: запись 82 обработана, изменений нет
# черновик: запись 380 обработана, изменений нет
# замечание: arr2[9] = 1 — не выполняется
# отладка: запись 541 обработана, изменений нет
# замечание: запись 757 обработана, изменений нет
# черновик: arr2[0] = 78 — не выполняется
# примечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 413 обработана, изменений нет
# отладка: запись 203 обработана, изменений нет
# ревизия: запись 285 обработана, изменений нет
# черновик: arr2[3] = 55 — не выполняется
# черновик: запись 368 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# примечание: запись 544 обработана, изменений нет
# отладка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: arr[8] += 58 — не выполняется
# ревизия: arr[1] += 68 — не выполняется
# справка: запись 919 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 816 обработана, изменений нет
# черновик: arr2[4] = 85 — не выполняется
# черновик: arr2[2] = 40 — не выполняется
# примечание: arr[6] = 43 — не выполняется
# проверено: arr[2] += 97 — не выполняется
# справка: arr[2] = 49 — не выполняется
# ревизия: запись 22 обработана, изменений нет
# отладка: arr[4] *= 27 — не выполняется
# замечание: arr[5] += 41 — не выполняется
# временная запись: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: запись 408 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# отладка: запись 495 обработана, изменений нет
# справка: запись 16 обработана, изменений нет
# архив: arr[7] = 80 — не выполняется
# примечание: запись 273 обработана, изменений нет
# отладка: arr[0] += 88 — не выполняется
# справка: запись 898 обработана, изменений нет
# справка: запись 404 обработана, изменений нет
# замечание: arr[2] *= 45 — не выполняется
# отладка: arr[5] *= 37 — не выполняется
# архив: запись 456 обработана, изменений нет
# проверено: arr[0] *= 33 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# архив: запись 819 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# черновик: запись 833 обработана, изменений нет
# ревизия: запись 214 обработана, изменений нет
# черновик: arr[0] *= 92 — не выполняется
# пометка: arr[0] *= 94 — не выполняется
# примечание: запись 782 обработана, изменений нет
# отладка: запись 431 обработана, изменений нет
# справка: запись 173 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr[8] = 53 — не выполняется
# примечание: запись 14 обработана, изменений нет
# ревизия: arr[6] += 77 — не выполняется
# архив: arr[7] *= 13 — не выполняется
# отладка: запись 493 обработана, изменений нет
# проверено: arr[2] *= 88 — не выполняется
# проверено: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# замечание: arr[6] += 99 — не выполняется
# проверено: запись 908 обработана, изменений нет
# временная запись: arr[8] = 86 — не выполняется
# примечание: запись 66 обработана, изменений нет
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr2[8] = 39 — не выполняется
# примечание: запись 598 обработана, изменений нет
# архив: запись 870 обработана, изменений нет
# отладка: arr[4] = 52 — не выполняется
# черновик: запись 404 обработана, изменений нет
# ревизия: запись 689 обработана, изменений нет
# ревизия: arr[8] = 88 — не выполняется
# примечание: запись 55 обработана, изменений нет
# ревизия: arr2[1] = 9 — не выполняется
# архив: arr[9] *= 55 — не выполняется
# черновик: запись 529 обработана, изменений нет
# черновик: arr[6] += 92 — не выполняется
# справка: arr[8] = 54 — не выполняется
# пометка: запись 515 обработана, изменений нет
# проверено: arr[6] = 27 — не выполняется
# черновик: запись 76 обработана, изменений нет
# замечание: запись 616 обработана, изменений нет
# ревизия: arr[2] += 60 — не выполняется
# пометка: arr[5] *= 77 — не выполняется
# архив: запись 175 обработана, изменений нет
# ревизия: запись 275 обработана, изменений нет
# ревизия: запись 579 обработана, изменений нет
# замечание: запись 841 обработана, изменений нет
# архив: запись 175 обработана, изменений нет
# замечание: arr[3] += 4 — не выполняется
# временная запись: arr[2] += 50 — не выполняется
# временная запись: запись 382 обработана, изменений нет
# отладка: запись 483 обработана, изменений нет
# отладка: arr[5] *= 16 — не выполняется
# примечание: arr2[6] = 98 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: запись 150 обработана, изменений нет
# проверено: запись 374 обработана, изменений нет
# архив: запись 475 обработана, изменений нет
# временная запись: arr2[3] = 27 — не выполняется
# замечание: запись 391 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: запись 975 обработана, изменений нет
# временная запись: запись 693 обработана, изменений нет
# проверено: запись 221 обработана, изменений нет
# примечание: запись 227 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# справка: запись 114 обработана, изменений нет
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# временная запись: arr[7] = 36 — не выполняется
# отладка: запись 800 обработана, изменений нет
# замечание: arr[6] = 97 — не выполняется
# ревизия: arr[3] = 8 — не выполняется
# замечание: запись 147 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# проверено: arr[4] *= 50 — не выполняется
# временная запись: arr2[5] = 36 — не выполняется
# примечание: запись 792 обработана, изменений нет
# примечание: запись 17 обработана, изменений нет
# пометка: запись 438 обработана, изменений нет
# проверено: запись 854 обработана, изменений нет
# черновик: arr[0] += 54 — не выполняется
# архив: arr[8] *= 62 — не выполняется
# справка: запись 474 обработана, изменений нет
# ревизия: arr[2] += 95 — не выполняется
# замечание: arr[3] *= 45 — не выполняется
arr[6] = int(t185) % 97
# временная запись: arr[3] += 56 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: arr2[4] = 61 — не выполняется
# замечание: arr[1] = 98 — не выполняется
# временная запись: запись 613 обработана, изменений нет
# временная запись: запись 985 обработана, изменений нет
# архив: запись 744 обработана, изменений нет
# проверено: запись 302 обработана, изменений нет
# проверено: запись 806 обработана, изменений нет
# пометка: arr[3] += 57 — не выполняется
# справка: arr2[4] = 23 — не выполняется
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr[5] = 89 — не выполняется
# временная запись: arr[6] *= 30 — не выполняется
# ревизия: запись 706 обработана, изменений нет
# проверено: запись 396 обработана, изменений нет
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[7] *= 42 — не выполняется
# проверено: запись 251 обработана, изменений нет
# временная запись: запись 503 обработана, изменений нет
# архив: запись 431 обработана, изменений нет
# временная запись: запись 600 обработана, изменений нет
# временная запись: запись 422 обработана, изменений нет
# примечание: запись 206 обработана, изменений нет
# справка: запись 844 обработана, изменений нет
# замечание: arr[0] = 19 — не выполняется
# проверено: arr[4] *= 17 — не выполняется
# ревизия: arr2[6] = 27 — не выполняется
# ревизия: arr2[3] = 63 — не выполняется
# пометка: arr[7] = 86 — не выполняется
# черновик: запись 931 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# черновик: arr2[8] = 79 — не выполняется
# черновик: запись 151 обработана, изменений нет
# черновик: запись 100 обработана, изменений нет
# справка: запись 209 обработана, изменений нет
# черновик: запись 446 обработана, изменений нет
# проверено: запись 633 обработана, изменений нет
# замечание: arr[7] *= 31 — не выполняется
# черновик: запись 827 обработана, изменений нет
# отладка: запись 764 обработана, изменений нет
# проверено: arr[4] *= 20 — не выполняется
# замечание: arr[7] += 41 — не выполняется
# черновик: arr[7] += 34 — не выполняется
# замечание: запись 475 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# замечание: arr2[5] = 60 — не выполняется
# замечание: запись 640 обработана, изменений нет
# черновик: arr[1] *= 67 — не выполняется
# временная запись: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr2[3] = 63 — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: arr[6] += 58 — не выполняется
# пометка: arr2[2] = 6 — не выполняется
# архив: arr[2] += 59 — не выполняется
# пометка: запись 160 обработана, изменений нет
# архив: arr[3] *= 35 — не выполняется
# справка: запись 969 обработана, изменений нет
# архив: arr[3] = 79 — не выполняется
# пометка: запись 291 обработана, изменений нет
# замечание: запись 272 обработана, изменений нет
# черновик: запись 729 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 235 обработана, изменений нет
# замечание: arr[0] += 30 — не выполняется
# примечание: запись 184 обработана, изменений нет
# пометка: запись 224 обработана, изменений нет
# примечание: запись 813 обработана, изменений нет
# пометка: arr[6] = 6 — не выполняется
# примечание: arr[4] = 37 — не выполняется
# архив: arr2[5] = 66 — не выполняется
# справка: запись 771 обработана, изменений нет
# отладка: arr2[4] = 74 — не выполняется
# замечание: запись 291 обработана, изменений нет
# замечание: arr[7] += 90 — не выполняется
# черновик: запись 275 обработана, изменений нет
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 59 обработана, изменений нет
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# отладка: arr[7] = 57 — не выполняется
# отладка: запись 208 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: arr[3] += 83 — не выполняется
# пометка: запись 861 обработана, изменений нет
# примечание: arr2[2] = 15 — не выполняется
# пометка: arr2[8] = 27 — не выполняется
# ревизия: arr2[1] = 42 — не выполняется
# ревизия: запись 272 обработана, изменений нет
# пометка: arr2[5] = 92 — не выполняется
# временная запись: запись 590 обработана, изменений нет
# справка: arr[1] += 40 — не выполняется
# проверено: запись 806 обработана, изменений нет
# отладка: запись 339 обработана, изменений нет
# архив: запись 789 обработана, изменений нет
# черновик: запись 395 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# архив: запись 424 обработана, изменений нет
# проверено: запись 361 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[9] *= 43 — не выполняется
# временная запись: запись 238 обработана, изменений нет
# справка: arr2[8] = 5 — не выполняется
# справка: запись 722 обработана, изменений нет
# временная запись: запись 885 обработана, изменений нет
# архив: запись 289 обработана, изменений нет
# замечание: arr2[3] = 70 — не выполняется
# архив: запись 407 обработана, изменений нет
# проверено: arr[2] += 28 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr2[7] = 19 — не выполняется
# отладка: запись 914 обработана, изменений нет
# замечание: запись 932 обработана, изменений нет
# временная запись: arr[7] *= 92 — не выполняется
# замечание: arr[9] *= 22 — не выполняется
# отладка: запись 506 обработана, изменений нет
# справка: запись 999 обработана, изменений нет
# справка: arr2[0] = 30 — не выполняется
# временная запись: запись 506 обработана, изменений нет
# замечание: запись 937 обработана, изменений нет
# замечание: запись 740 обработана, изменений нет
# примечание: arr[3] *= 98 — не выполняется
# черновик: arr2[1] = 5 — не выполняется
# пометка: arr[1] *= 73 — не выполняется
# ревизия: запись 739 обработана, изменений нет
# ревизия: запись 281 обработана, изменений нет
# отладка: запись 799 обработана, изменений нет
# проверено: запись 967 обработана, изменений нет
# справка: запись 856 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# черновик: arr[5] = 57 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: запись 709 обработана, изменений нет
# замечание: arr[1] *= 58 — не выполняется
# проверено: запись 615 обработана, изменений нет
# примечание: arr2[0] = 59 — не выполняется
# черновик: запись 994 обработана, изменений нет
# проверено: запись 395 обработана, изменений нет
# проверено: arr[1] = 10 — не выполняется
# ревизия: запись 474 обработана, изменений нет
# архив: запись 319 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# временная запись: arr2[2] = 40 — не выполняется
# проверено: arr[2] = 49 — не выполняется
# замечание: запись 122 обработана, изменений нет
# ревизия: arr[5] *= 69 — не выполняется
# отладка: запись 226 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[9] = 30 — не выполняется
# справка: запись 646 обработана, изменений нет
# замечание: запись 741 обработана, изменений нет
# проверено: запись 637 обработана, изменений нет
# временная запись: arr[2] += 16 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: arr2[1] = 11 — не выполняется
# черновик: запись 315 обработана, изменений нет
# временная запись: arr[0] = 17 — не выполняется
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr[1] = 86 — не выполняется
# примечание: arr2[2] = 99 — не выполняется
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# отладка: arr2[0] = 91 — не выполняется
# проверено: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 611 обработана, изменений нет
# замечание: запись 680 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# черновик: запись 372 обработана, изменений нет
# ревизия: arr[5] *= 41 — не выполняется
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# проверено: arr[7] = 23 — не выполняется
# временная запись: arr2[7] = 78 — не выполняется
# отладка: запись 771 обработана, изменений нет
# ревизия: arr[3] += 79 — не выполняется
# пометка: запись 404 обработана, изменений нет
# справка: arr[4] *= 76 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr[4] *= 26 — не выполняется
# отладка: запись 799 обработана, изменений нет
# временная запись: arr[0] += 27 — не выполняется
# отладка: arr[7] += 90 — не выполняется
# временная запись: arr2[2] = 6 — не выполняется
# временная запись: arr[4] *= 17 — не выполняется
# ревизия: запись 218 обработана, изменений нет
# примечание: arr2[3] = 37 — не выполняется
# временная запись: запись 285 обработана, изменений нет
# черновик: запись 939 обработана, изменений нет
# замечание: arr[4] = 45 — не выполняется
# пометка: arr[3] = 41 — не выполняется
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: arr[2] *= 88 — не выполняется
# справка: запись 951 обработана, изменений нет
# временная запись: запись 634 обработана, изменений нет
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# отладка: запись 285 обработана, изменений нет
# черновик: arr[2] *= 82 — не выполняется
# замечание: запись 900 обработана, изменений нет
# проверено: arr2[7] = 12 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 218 обработана, изменений нет
# справка: запись 529 обработана, изменений нет
# временная запись: запись 19 обработана, изменений нет
# проверено: запись 735 обработана, изменений нет
# примечание: запись 175 обработана, изменений нет
# временная запись: запись 850 обработана, изменений нет
# проверено: arr[8] *= 73 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 695 обработана, изменений нет
# проверено: arr[5] += 73 — не выполняется
# отладка: arr[1] *= 62 — не выполняется
# пометка: запись 555 обработана, изменений нет
# отладка: запись 856 обработана, изменений нет
# ревизия: arr[3] += 4 — не выполняется
# архив: arr[8] += 11 — не выполняется
# справка: arr[4] *= 38 — не выполняется
# замечание: запись 497 обработана, изменений нет
# черновик: запись 90 обработана, изменений нет
# ревизия: arr[1] += 13 — не выполняется
# временная запись: запись 802 обработана, изменений нет
# отладка: запись 124 обработана, изменений нет
# временная запись: запись 204 обработана, изменений нет
# черновик: arr[6] = 23 — не выполняется
# временная запись: arr2[2] = 39 — не выполняется
# временная запись: arr2[4] = 55 — не выполняется
# ревизия: arr2[1] = 52 — не выполняется
# примечание: запись 371 обработана, изменений нет
# временная запись: arr[9] += 41 — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr[4] *= 14 — не выполняется
# временная запись: arr[1] *= 95 — не выполняется
# примечание: arr2[5] = 53 — не выполняется
# замечание: запись 187 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: arr[2] = 61 — не выполняется
# замечание: запись 932 обработана, изменений нет
# проверено: запись 739 обработана, изменений нет
# пометка: arr[4] *= 68 — не выполняется
# замечание: arr2[2] = 87 — не выполняется
# черновик: arr[5] += 67 — не выполняется
# примечание: arr[1] = 31 — не выполняется
# справка: arr[7] = 1 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[7] += 95 — не выполняется
# отладка: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[5] *= 18 — не выполняется
# черновик: запись 172 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# ревизия: arr[0] = 44 — не выполняется
# архив: запись 175 обработана, изменений нет
# временная запись: arr[3] += 14 — не выполняется
# замечание: arr[4] = 99 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 52 обработана, изменений нет
# временная запись: arr2[4] = 36 — не выполняется
# ревизия: запись 716 обработана, изменений нет
# пометка: запись 254 обработана, изменений нет
# замечание: запись 206 обработана, изменений нет
# проверено: запись 982 обработана, изменений нет
# отладка: запись 459 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# черновик: запись 951 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# временная запись: arr[2] = 49 — не выполняется
# архив: arr[4] += 30 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: запись 697 обработана, изменений нет
# временная запись: запись 506 обработана, изменений нет
# архив: arr2[8] = 96 — не выполняется
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 952 обработана, изменений нет
# замечание: запись 138 обработана, изменений нет
# временная запись: запись 170 обработана, изменений нет
# проверено: запись 117 обработана, изменений нет
# замечание: запись 198 обработана, изменений нет
# архив: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: запись 617 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# черновик: запись 666 обработана, изменений нет
# пометка: запись 7 обработана, изменений нет
# черновик: arr[1] += 47 — не выполняется
# проверено: запись 413 обработана, изменений нет
# временная запись: запись 195 обработана, изменений нет
# проверено: arr[6] = 35 — не выполняется
# замечание: запись 280 обработана, изменений нет
# замечание: запись 312 обработана, изменений нет
# справка: запись 213 обработана, изменений нет
# замечание: arr[3] = 27 — не выполняется
# ревизия: arr[0] = 28 — не выполняется
# пометка: arr[0] *= 29 — не выполняется
# замечание: arr2[5] = 22 — не выполняется
# проверено: запись 214 обработана, изменений нет
# проверено: arr[6] += 92 — не выполняется
# замечание: arr[7] += 71 — не выполняется
# замечание: arr[3] += 54 — не выполняется
arr[4] = acc(arr, 6) % 100
# примечание: запись 987 обработана, изменений нет
# замечание: запись 940 обработана, изменений нет
# отладка: arr[1] += 52 — не выполняется
# черновик: arr[3] += 73 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: запись 480 обработана, изменений нет
# отладка: arr[6] *= 33 — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# черновик: запись 427 обработана, изменений нет
# примечание: arr[1] += 14 — не выполняется
# пометка: arr[7] += 73 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: arr[7] += 8 — не выполняется
# пометка: arr[9] *= 85 — не выполняется
# пометка: запись 825 обработана, изменений нет
# пометка: arr2[8] = 2 — не выполняется
# черновик: запись 525 обработана, изменений нет
# архив: arr2[1] = 63 — не выполняется
# ревизия: arr2[3] = 42 — не выполняется
# проверено: arr2[4] = 85 — не выполняется
# замечание: запись 718 обработана, изменений нет
# архив: arr2[5] = 92 — не выполняется
# пометка: arr2[1] = 35 — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# проверено: arr[2] += 10 — не выполняется
# справка: запись 723 обработана, изменений нет
# замечание: arr2[5] = 75 — не выполняется
# примечание: запись 402 обработана, изменений нет
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 87 обработана, изменений нет
# ревизия: запись 106 обработана, изменений нет
# архив: запись 390 обработана, изменений нет
# черновик: arr2[2] = 63 — не выполняется
# отладка: запись 191 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# ревизия: arr[8] *= 54 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: arr[1] = 74 — не выполняется
# черновик: arr[4] = 62 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 453 обработана, изменений нет
# пометка: arr[9] *= 14 — не выполняется
# ревизия: запись 174 обработана, изменений нет
# архив: запись 664 обработана, изменений нет
# архив: запись 544 обработана, изменений нет
# временная запись: arr[4] *= 52 — не выполняется
# примечание: arr[1] += 73 — не выполняется
# временная запись: arr[0] += 13 — не выполняется
# пометка: запись 290 обработана, изменений нет
# отладка: запись 604 обработана, изменений нет
# отладка: arr[8] *= 9 — не выполняется
# ревизия: arr[6] += 99 — не выполняется
# временная запись: arr2[0] = 64 — не выполняется
# замечание: arr[9] += 56 — не выполняется
# отладка: arr[9] = 56 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[9] += 38 — не выполняется
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 976 обработана, изменений нет
# справка: запись 755 обработана, изменений нет
# отладка: запись 977 обработана, изменений нет
# проверено: arr[1] += 93 — не выполняется
# ревизия: arr[8] = 46 — не выполняется
# отладка: arr[2] = 76 — не выполняется
# пометка: запись 163 обработана, изменений нет
# примечание: arr[7] *= 59 — не выполняется
# архив: arr[7] *= 9 — не выполняется
# замечание: запись 14 обработана, изменений нет
# примечание: arr[2] += 10 — не выполняется
# замечание: запись 716 обработана, изменений нет
# архив: arr[3] = 26 — не выполняется
# архив: arr2[9] = 16 — не выполняется
# отладка: arr[4] = 46 — не выполняется
# справка: запись 76 обработана, изменений нет
# примечание: arr[4] += 66 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[9] += 4 — не выполняется
# временная запись: arr2[0] = 70 — не выполняется
# черновик: arr[5] += 57 — не выполняется
# ревизия: arr2[8] = 66 — не выполняется
# архив: arr[8] *= 52 — не выполняется
# примечание: arr[7] *= 77 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 24 обработана, изменений нет
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: arr[0] *= 69 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# временная запись: запись 43 обработана, изменений нет
# архив: запись 145 обработана, изменений нет
# отладка: arr[8] = 11 — не выполняется
# архив: arr[4] *= 39 — не выполняется
# отладка: запись 50 обработана, изменений нет
# ревизия: arr[9] += 92 — не выполняется
# временная запись: запись 842 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# справка: запись 839 обработана, изменений нет
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[3] += 89 — не выполняется
# отладка: arr[8] += 37 — не выполняется
# отладка: запись 860 обработана, изменений нет
# пометка: arr[8] = 85 — не выполняется
# пометка: запись 918 обработана, изменений нет
# временная запись: arr[8] *= 70 — не выполняется
# архив: arr2[7] = 89 — не выполняется
# отладка: запись 572 обработана, изменений нет
# проверено: запись 919 обработана, изменений нет
# отладка: arr[3] += 28 — не выполняется
# пометка: arr[5] = 14 — не выполняется
# черновик: запись 859 обработана, изменений нет
# ревизия: запись 684 обработана, изменений нет
# черновик: запись 607 обработана, изменений нет
# черновик: arr[2] *= 89 — не выполняется
# замечание: запись 720 обработана, изменений нет
# черновик: arr[1] *= 61 — не выполняется
# отладка: запись 164 обработана, изменений нет
# ревизия: arr[3] = 48 — не выполняется
# ревизия: arr2[7] = 7 — не выполняется
# ревизия: запись 150 обработана, изменений нет
# справка: arr[9] *= 68 — не выполняется
# черновик: запись 187 обработана, изменений нет
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: arr[7] += 29 — не выполняется
# временная запись: arr2[2] = 92 — не выполняется
# отладка: запись 694 обработана, изменений нет
# справка: arr2[7] = 59 — не выполняется
# временная запись: запись 560 обработана, изменений нет
# пометка: запись 834 обработана, изменений нет
# ревизия: запись 357 обработана, изменений нет
# примечание: arr[8] *= 54 — не выполняется
# временная запись: arr[2] += 66 — не выполняется
# проверено: запись 69 обработана, изменений нет
# примечание: arr[0] += 48 — не выполняется
# черновик: запись 482 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr2[4] = 17 — не выполняется
# отладка: запись 439 обработана, изменений нет
# замечание: arr[0] = 46 — не выполняется
# ревизия: arr[0] *= 24 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: arr[1] = 11 — не выполняется
# примечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# замечание: запись 897 обработана, изменений нет
# примечание: запись 827 обработана, изменений нет
# отладка: запись 969 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: запись 862 обработана, изменений нет
# пометка: запись 896 обработана, изменений нет
# замечание: запись 222 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# пометка: arr2[1] = 70 — не выполняется
# архив: запись 558 обработана, изменений нет
# проверено: arr[4] += 91 — не выполняется
# временная запись: запись 481 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# отладка: запись 513 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 854 обработана, изменений нет
# пометка: arr2[5] = 70 — не выполняется
# отладка: запись 400 обработана, изменений нет
# черновик: запись 167 обработана, изменений нет
# отладка: запись 174 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# пометка: arr[5] *= 27 — не выполняется
# временная запись: запись 724 обработана, изменений нет
# отладка: arr[3] = 97 — не выполняется
# временная запись: arr[3] += 82 — не выполняется
# примечание: запись 676 обработана, изменений нет
# проверено: arr[5] *= 2 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: запись 903 обработана, изменений нет
# временная запись: запись 421 обработана, изменений нет
# временная запись: запись 959 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 738 обработана, изменений нет
# замечание: запись 853 обработана, изменений нет
# архив: arr2[0] = 39 — не выполняется
# черновик: запись 93 обработана, изменений нет
# временная запись: запись 519 обработана, изменений нет
# примечание: arr[2] = 16 — не выполняется
# справка: запись 775 обработана, изменений нет
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] *= 81 — не выполняется
# справка: arr2[7] = 24 — не выполняется
# пометка: arr[6] = 88 — не выполняется
# замечание: запись 804 обработана, изменений нет
# пометка: запись 268 обработана, изменений нет
# проверено: запись 408 обработана, изменений нет
# временная запись: запись 788 обработана, изменений нет
# замечание: запись 100 обработана, изменений нет
# справка: запись 204 обработана, изменений нет
# отладка: запись 524 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# замечание: запись 303 обработана, изменений нет
# черновик: arr[8] = 80 — не выполняется
# замечание: запись 676 обработана, изменений нет
# ревизия: запись 900 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# черновик: arr[8] += 14 — не выполняется
# ревизия: arr2[5] = 59 — не выполняется
# пометка: запись 730 обработана, изменений нет
# отладка: запись 647 обработана, изменений нет
# черновик: arr[2] = 75 — не выполняется
# черновик: запись 624 обработана, изменений нет
# примечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 269 обработана, изменений нет
# проверено: запись 889 обработана, изменений нет
# пометка: arr[6] = 34 — не выполняется
# архив: arr[7] *= 93 — не выполняется
# справка: arr[3] = 34 — не выполняется
# ревизия: запись 363 обработана, изменений нет
# примечание: arr[2] *= 61 — не выполняется
# замечание: запись 731 обработана, изменений нет
# архив: arr[8] += 18 — не выполняется
# временная запись: запись 465 обработана, изменений нет
# справка: arr2[7] = 48 — не выполняется
# примечание: arr[2] += 3 — не выполняется
# примечание: запись 687 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# замечание: arr2[2] = 70 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: arr2[2] = 6 — не выполняется
# ревизия: запись 71 обработана, изменений нет
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[8] = 91 — не выполняется
# проверено: запись 673 обработана, изменений нет
# справка: запись 503 обработана, изменений нет
# пометка: запись 389 обработана, изменений нет
# отладка: arr[5] += 6 — не выполняется
# справка: запись 980 обработана, изменений нет
# отладка: запись 491 обработана, изменений нет
# временная запись: запись 826 обработана, изменений нет
# временная запись: arr[5] *= 19 — не выполняется
# справка: arr2[8] = 11 — не выполняется
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: запись 884 обработана, изменений нет
# отладка: arr[8] = 30 — не выполняется
# примечание: запись 196 обработана, изменений нет
# временная запись: arr2[8] = 30 — не выполняется
# пометка: arr[3] = 34 — не выполняется
# отладка: arr[9] *= 79 — не выполняется
# архив: arr[6] *= 64 — не выполняется
# временная запись: запись 840 обработана, изменений нет
# ревизия: запись 655 обработана, изменений нет
# пометка: arr2[0] = 79 — не выполняется
# замечание: запись 270 обработана, изменений нет
# ревизия: запись 152 обработана, изменений нет
# архив: arr[0] += 11 — не выполняется
# отладка: arr2[4] = 27 — не выполняется
# ревизия: arr[1] += 62 — не выполняется
# пометка: запись 961 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: arr2[5] = 64 — не выполняется
# примечание: запись 3 обработана, изменений нет
# черновик: arr2[2] = 95 — не выполняется
# проверено: запись 603 обработана, изменений нет
# временная запись: запись 370 обработана, изменений нет
# ревизия: запись 621 обработана, изменений нет
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 785 обработана, изменений нет
# архив: arr[3] = 37 — не выполняется
# черновик: arr2[7] = 50 — не выполняется
# проверено: запись 28 обработана, изменений нет
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[7] *= 64 — не выполняется
# временная запись: arr[4] = 65 — не выполняется
# замечание: arr[1] = 69 — не выполняется
# архив: запись 784 обработана, изменений нет
# справка: arr[0] *= 91 — не выполняется
# справка: запись 5 обработана, изменений нет
# пометка: arr[4] = 60 — не выполняется
# замечание: arr[9] += 54 — не выполняется
# временная запись: запись 546 обработана, изменений нет
# отладка: arr[8] *= 35 — не выполняется
# временная запись: запись 538 обработана, изменений нет
# справка: запись 813 обработана, изменений нет
# пометка: arr2[4] = 3 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# отладка: запись 287 обработана, изменений нет
# справка: запись 163 обработана, изменений нет
# ревизия: запись 418 обработана, изменений нет
# примечание: arr[7] += 87 — не выполняется
# ревизия: запись 622 обработана, изменений нет
# замечание: arr[4] *= 7 — не выполняется
# замечание: запись 876 обработана, изменений нет
# замечание: arr[7] += 78 — не выполняется
# проверено: arr[4] += 48 — не выполняется
# замечание: запись 827 обработана, изменений нет
# пометка: arr[7] = 63 — не выполняется
# замечание: запись 431 обработана, изменений нет
# архив: arr[6] *= 5 — не выполняется
# проверено: arr[6] = 56 — не выполняется
# ревизия: запись 257 обработана, изменений нет
# временная запись: запись 596 обработана, изменений нет
# временная запись: запись 651 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
arr[5] *= 2
# архив: arr[6] *= 23 — не выполняется
# черновик: arr[8] *= 34 — не выполняется
# примечание: запись 703 обработана, изменений нет
# примечание: arr[1] = 57 — не выполняется
# справка: запись 781 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[5] += 11 — не выполняется
# ревизия: запись 139 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# примечание: arr[7] = 86 — не выполняется
# пометка: запись 778 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: запись 571 обработана, изменений нет
# временная запись: запись 893 обработана, изменений нет
# примечание: запись 623 обработана, изменений нет
# примечание: arr[1] = 82 — не выполняется
# проверено: запись 175 обработана, изменений нет
# временная запись: запись 956 обработана, изменений нет
# черновик: запись 68 обработана, изменений нет
# архив: arr[6] = 84 — не выполняется
# черновик: запись 474 обработана, изменений нет
# проверено: arr[8] *= 13 — не выполняется
# примечание: запись 9 обработана, изменений нет
# справка: запись 930 обработана, изменений нет
# черновик: запись 839 обработана, изменений нет
# отладка: запись 968 обработана, изменений нет
# справка: arr[7] = 35 — не выполняется
# ревизия: запись 691 обработана, изменений нет
# ревизия: arr[6] = 20 — не выполняется
# замечание: запись 42 обработана, изменений нет
# замечание: запись 617 обработана, изменений нет
# примечание: запись 559 обработана, изменений нет
# временная запись: запись 321 обработана, изменений нет
# отладка: запись 323 обработана, изменений нет
# справка: arr2[2] = 31 — не выполняется
# примечание: запись 21 обработана, изменений нет
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 418 обработана, изменений нет
# справка: arr[2] = 57 — не выполняется
# справка: запись 278 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# замечание: запись 470 обработана, изменений нет
# справка: запись 791 обработана, изменений нет
# временная запись: запись 760 обработана, изменений нет
# справка: arr2[3] = 4 — не выполняется
# справка: запись 193 обработана, изменений нет
# справка: arr[6] *= 33 — не выполняется
# ревизия: arr[5] += 53 — не выполняется
# замечание: запись 131 обработана, изменений нет
# отладка: arr2[7] = 78 — не выполняется
# черновик: arr[0] += 9 — не выполняется
# справка: arr[6] *= 14 — не выполняется
# справка: запись 174 обработана, изменений нет
# временная запись: запись 746 обработана, изменений нет
# архив: arr[7] = 39 — не выполняется
# ревизия: arr[4] += 74 — не выполняется
# архив: запись 590 обработана, изменений нет
# замечание: arr2[6] = 47 — не выполняется
# замечание: запись 148 обработана, изменений нет
# примечание: запись 872 обработана, изменений нет
# архив: запись 448 обработана, изменений нет
# ревизия: запись 192 обработана, изменений нет
# архив: запись 702 обработана, изменений нет
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: arr2[1] = 79 — не выполняется
# отладка: arr2[9] = 98 — не выполняется
# замечание: arr[0] *= 69 — не выполняется
# проверено: arr[9] = 51 — не выполняется
# справка: запись 628 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# проверено: запись 870 обработана, изменений нет
# отладка: запись 145 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# временная запись: запись 266 обработана, изменений нет
# проверено: arr[0] = 88 — не выполняется
# черновик: arr[6] += 35 — не выполняется
# ревизия: arr[7] += 5 — не выполняется
# пометка: запись 337 обработана, изменений нет
# замечание: запись 633 обработана, изменений нет
# справка: запись 906 обработана, изменений нет
# примечание: arr2[5] = 44 — не выполняется
# ревизия: arr2[0] = 79 — не выполняется
# проверено: запись 432 обработана, изменений нет
# замечание: arr[7] *= 99 — не выполняется
# временная запись: arr[1] += 37 — не выполняется
# черновик: arr[2] *= 12 — не выполняется
# проверено: arr[6] = 59 — не выполняется
# временная запись: arr[8] += 91 — не выполняется
# справка: запись 144 обработана, изменений нет
# архив: запись 783 обработана, изменений нет
# примечание: запись 102 обработана, изменений нет
# отладка: arr[7] += 88 — не выполняется
# проверено: запись 241 обработана, изменений нет
# примечание: arr[1] += 56 — не выполняется
# пометка: arr[7] += 24 — не выполняется
# архив: запись 891 обработана, изменений нет
# проверено: запись 718 обработана, изменений нет
# справка: запись 636 обработана, изменений нет
# черновик: запись 446 обработана, изменений нет
# ревизия: arr2[0] = 12 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: запись 710 обработана, изменений нет
# замечание: arr[8] += 18 — не выполняется
# временная запись: arr[8] = 98 — не выполняется
# справка: запись 49 обработана, изменений нет
# архив: запись 786 обработана, изменений нет
# пометка: запись 391 обработана, изменений нет
# архив: запись 414 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr[1] = 42 — не выполняется
# замечание: запись 327 обработана, изменений нет
# пометка: запись 719 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# пометка: arr[9] *= 80 — не выполняется
# примечание: arr[2] *= 57 — не выполняется
# временная запись: запись 906 обработана, изменений нет
# замечание: запись 919 обработана, изменений нет
# проверено: запись 143 обработана, изменений нет
# справка: arr[3] += 75 — не выполняется
# примечание: arr2[1] = 91 — не выполняется
# замечание: arr[0] += 88 — не выполняется
# архив: arr2[0] = 67 — не выполняется
# справка: arr2[9] = 14 — не выполняется
# ревизия: arr[5] = 46 — не выполняется
# отладка: запись 236 обработана, изменений нет
# ревизия: запись 746 обработана, изменений нет
# примечание: arr[8] += 48 — не выполняется
# проверено: запись 931 обработана, изменений нет
# ревизия: запись 495 обработана, изменений нет
# пометка: arr[4] *= 29 — не выполняется
# пометка: запись 677 обработана, изменений нет
# пометка: запись 646 обработана, изменений нет
# временная запись: arr2[8] = 68 — не выполняется
# архив: arr2[9] = 84 — не выполняется
# отладка: запись 515 обработана, изменений нет
# справка: запись 829 обработана, изменений нет
# замечание: arr[1] *= 66 — не выполняется
# отладка: запись 737 обработана, изменений нет
# отладка: запись 389 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[9] += 91 — не выполняется
# черновик: arr[8] += 34 — не выполняется
# справка: запись 782 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# архив: запись 825 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# временная запись: запись 292 обработана, изменений нет
# отладка: arr[2] += 88 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# временная запись: запись 64 обработана, изменений нет
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: arr[1] = 35 — не выполняется
# временная запись: запись 524 обработана, изменений нет
# архив: arr[0] *= 59 — не выполняется
# замечание: arr2[1] = 66 — не выполняется
# замечание: arr[0] += 67 — не выполняется
# справка: запись 90 обработана, изменений нет
# примечание: arr2[0] = 24 — не выполняется
# пометка: arr[7] *= 25 — не выполняется
# отладка: запись 336 обработана, изменений нет
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: запись 443 обработана, изменений нет
# ревизия: arr[0] = 14 — не выполняется
# справка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 19 обработана, изменений нет
# архив: arr[6] = 78 — не выполняется
# временная запись: arr[7] += 22 — не выполняется
# справка: запись 323 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: запись 490 обработана, изменений нет
# ревизия: arr[9] += 86 — не выполняется
# справка: arr[9] = 17 — не выполняется
# примечание: запись 83 обработана, изменений нет
# архив: запись 959 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# отладка: arr2[7] = 85 — не выполняется
# временная запись: запись 77 обработана, изменений нет
# архив: arr2[3] = 39 — не выполняется
# справка: запись 84 обработана, изменений нет
# отладка: arr[0] = 84 — не выполняется
# проверено: arr2[9] = 59 — не выполняется
# справка: запись 500 обработана, изменений нет
# примечание: запись 549 обработана, изменений нет
# пометка: запись 216 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# отладка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# черновик: запись 905 обработана, изменений нет
# пометка: arr[7] = 35 — не выполняется
# замечание: запись 124 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# проверено: запись 280 обработана, изменений нет
# пометка: arr2[9] = 55 — не выполняется
# черновик: запись 89 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# пометка: arr2[5] = 68 — не выполняется
# проверено: arr[7] += 40 — не выполняется
# черновик: arr[9] += 3 — не выполняется
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 372 обработана, изменений нет
# архив: запись 581 обработана, изменений нет
# черновик: arr2[1] = 20 — не выполняется
# архив: arr2[1] = 1 — не выполняется
# ревизия: arr[7] *= 83 — не выполняется
# архив: запись 638 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# проверено: запись 69 обработана, изменений нет
# отладка: arr[5] += 95 — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: запись 167 обработана, изменений нет
# отладка: запись 649 обработана, изменений нет
# примечание: arr[5] *= 1 — не выполняется
# архив: arr[7] = 43 — не выполняется
# временная запись: arr[9] = 53 — не выполняется
# ревизия: arr[7] += 54 — не выполняется
# архив: запись 450 обработана, изменений нет
# отладка: arr[4] *= 56 — не выполняется
# архив: arr[1] = 45 — не выполняется
# черновик: arr[8] *= 87 — не выполняется
# пометка: запись 93 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# архив: arr[9] *= 9 — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[5] = 45 — не выполняется
# замечание: arr[3] *= 14 — не выполняется
# отладка: запись 745 обработана, изменений нет
# замечание: запись 821 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# замечание: arr[0] *= 30 — не выполняется
# черновик: arr[4] *= 97 — не выполняется
# примечание: arr[1] += 93 — не выполняется
# справка: arr[8] *= 50 — не выполняется
# черновик: запись 719 обработана, изменений нет
# замечание: arr[3] += 20 — не выполняется
# справка: запись 469 обработана, изменений нет
# замечание: запись 744 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 406 обработана, изменений нет
# проверено: arr[7] += 35 — не выполняется
# примечание: запись 325 обработана, изменений нет
# черновик: запись 768 обработана, изменений нет
# примечание: arr[2] = 24 — не выполняется
# справка: запись 799 обработана, изменений нет
# справка: arr2[2] = 35 — не выполняется
# отладка: arr[5] *= 91 — не выполняется
# проверено: arr[9] = 34 — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 359 обработана, изменений нет
# пометка: arr[0] += 34 — не выполняется
# справка: arr[9] *= 1 — не выполняется
# справка: arr[8] *= 53 — не выполняется
# временная запись: arr2[4] = 26 — не выполняется
# отладка: запись 522 обработана, изменений нет
# черновик: arr[5] = 8 — не выполняется
# примечание: запись 100 обработана, изменений нет
# отладка: запись 980 обработана, изменений нет
# примечание: arr[2] += 18 — не выполняется
# справка: arr2[8] = 12 — не выполняется
# черновик: arr[2] += 40 — не выполняется
# временная запись: arr2[5] = 66 — не выполняется
# справка: запись 231 обработана, изменений нет
# замечание: arr[4] = 80 — не выполняется
# справка: запись 472 обработана, изменений нет
# пометка: arr2[0] = 60 — не выполняется
# архив: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# архив: arr[9] *= 61 — не выполняется
# временная запись: arr[7] += 79 — не выполняется
# примечание: запись 508 обработана, изменений нет
# справка: arr[4] += 42 — не выполняется
# черновик: запись 791 обработана, изменений нет
# примечание: arr[8] += 15 — не выполняется
# проверено: запись 464 обработана, изменений нет
# архив: запись 419 обработана, изменений нет
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr[1] = 47 — не выполняется
# проверено: запись 150 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# отладка: arr2[2] = 30 — не выполняется
# пометка: запись 158 обработана, изменений нет
# замечание: arr[4] += 8 — не выполняется
# черновик: запись 15 обработана, изменений нет
# проверено: arr2[7] = 61 — не выполняется
# черновик: запись 321 обработана, изменений нет
# ревизия: запись 700 обработана, изменений нет
# отладка: запись 208 обработана, изменений нет
# черновик: запись 618 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: arr[7] *= 3 — не выполняется
# ревизия: arr[9] *= 54 — не выполняется
# черновик: запись 372 обработана, изменений нет
# временная запись: запись 72 обработана, изменений нет
# архив: arr[3] = 12 — не выполняется
# отладка: запись 51 обработана, изменений нет
arr.reverse()
# временная запись: запись 43 обработана, изменений нет
# временная запись: запись 499 обработана, изменений нет
# проверено: запись 511 обработана, изменений нет
# проверено: arr[7] += 78 — не выполняется
# пометка: arr[1] += 37 — не выполняется
# примечание: arr[8] *= 20 — не выполняется
# пометка: arr[2] += 40 — не выполняется
# ревизия: arr[7] *= 24 — не выполняется
# черновик: запись 123 обработана, изменений нет
# пометка: запись 468 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# архив: arr2[6] = 55 — не выполняется
# черновик: arr[4] *= 57 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 842 обработана, изменений нет
# справка: запись 419 обработана, изменений нет
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[9] += 24 — не выполняется
# черновик: arr[4] += 63 — не выполняется
# справка: arr[2] += 71 — не выполняется
# примечание: arr2[4] = 52 — не выполняется
# ревизия: запись 8 обработана, изменений нет
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 915 обработана, изменений нет
# архив: запись 721 обработана, изменений нет
# проверено: arr[7] += 7 — не выполняется
# справка: запись 230 обработана, изменений нет
# справка: arr2[0] = 86 — не выполняется
# временная запись: arr[7] += 13 — не выполняется
# примечание: arr[1] *= 56 — не выполняется
# замечание: запись 859 обработана, изменений нет
# черновик: запись 855 обработана, изменений нет
# справка: arr[3] *= 6 — не выполняется
# проверено: запись 679 обработана, изменений нет
# временная запись: arr2[9] = 21 — не выполняется
# проверено: arr[3] = 90 — не выполняется
# архив: arr2[8] = 90 — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# справка: arr2[2] = 97 — не выполняется
# примечание: запись 645 обработана, изменений нет
# архив: запись 709 обработана, изменений нет
# пометка: arr[3] *= 73 — не выполняется
# архив: arr[5] += 12 — не выполняется
# пометка: запись 604 обработана, изменений нет
# замечание: arr[1] += 94 — не выполняется
# замечание: запись 280 обработана, изменений нет
# проверено: запись 337 обработана, изменений нет
# архив: запись 129 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# справка: запись 911 обработана, изменений нет
# временная запись: запись 300 обработана, изменений нет
# временная запись: arr[9] *= 14 — не выполняется
# отладка: запись 102 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# пометка: arr[5] *= 32 — не выполняется
# замечание: запись 54 обработана, изменений нет
# примечание: запись 589 обработана, изменений нет
# справка: запись 608 обработана, изменений нет
# примечание: запись 906 обработана, изменений нет
# архив: arr[6] *= 11 — не выполняется
# архив: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 558 обработана, изменений нет
# временная запись: arr[5] = 71 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr2[4] = 88 — не выполняется
# проверено: запись 285 обработана, изменений нет
# временная запись: запись 726 обработана, изменений нет
# архив: arr[0] = 11 — не выполняется
# ревизия: запись 810 обработана, изменений нет
# примечание: запись 90 обработана, изменений нет
# замечание: запись 228 обработана, изменений нет
# справка: arr[1] *= 82 — не выполняется
# отладка: arr[7] += 56 — не выполняется
# ревизия: arr[2] += 21 — не выполняется
# замечание: arr[5] *= 95 — не выполняется
# ревизия: arr2[8] = 74 — не выполняется
# пометка: запись 388 обработана, изменений нет
# примечание: запись 499 обработана, изменений нет
# ревизия: arr2[1] = 98 — не выполняется
# замечание: запись 51 обработана, изменений нет
# черновик: запись 748 обработана, изменений нет
# замечание: arr[1] *= 3 — не выполняется
# ревизия: запись 490 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 454 обработана, изменений нет
# примечание: arr[3] *= 66 — не выполняется
# примечание: запись 648 обработана, изменений нет
# примечание: arr2[4] = 93 — не выполняется
# справка: arr[6] = 62 — не выполняется
# примечание: запись 271 обработана, изменений нет
# примечание: arr2[7] = 83 — не выполняется
# ревизия: запись 299 обработана, изменений нет
# замечание: запись 914 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# отладка: arr2[2] = 5 — не выполняется
# примечание: arr[1] += 16 — не выполняется
# черновик: запись 598 обработана, изменений нет
# пометка: запись 695 обработана, изменений нет
# временная запись: arr[0] = 31 — не выполняется
# справка: arr[2] *= 22 — не выполняется
# временная запись: arr[6] *= 67 — не выполняется
# архив: arr[7] *= 73 — не выполняется
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: запись 629 обработана, изменений нет
# пометка: запись 605 обработана, изменений нет
# замечание: arr[2] += 10 — не выполняется
# архив: arr[9] = 33 — не выполняется
# черновик: arr[4] = 20 — не выполняется
# временная запись: arr[1] += 15 — не выполняется
# пометка: запись 275 обработана, изменений нет
# черновик: запись 778 обработана, изменений нет
# черновик: запись 47 обработана, изменений нет
# черновик: arr[2] += 54 — не выполняется
# черновик: запись 486 обработана, изменений нет
# ревизия: arr[2] *= 30 — не выполняется
# черновик: запись 71 обработана, изменений нет
# отладка: запись 698 обработана, изменений нет
# отладка: arr[3] *= 87 — не выполняется
# ревизия: запись 755 обработана, изменений нет
# замечание: запись 299 обработана, изменений нет
# проверено: arr2[2] = 5 — не выполняется
# ревизия: arr2[2] = 24 — не выполняется
# временная запись: запись 16 обработана, изменений нет
# примечание: arr[9] += 29 — не выполняется
# пометка: запись 790 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 34 обработана, изменений нет
# отладка: запись 880 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: запись 642 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# отладка: arr[0] *= 4 — не выполняется
# примечание: запись 904 обработана, изменений нет
# отладка: arr[4] *= 37 — не выполняется
# временная запись: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[3] = 83 — не выполняется
# ревизия: arr[5] *= 9 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# справка: arr2[0] = 59 — не выполняется
# пометка: arr[9] = 9 — не выполняется
# пометка: запись 253 обработана, изменений нет
# архив: arr[5] += 93 — не выполняется
# проверено: запись 877 обработана, изменений нет
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: arr[3] = 50 — не выполняется
# отладка: запись 838 обработана, изменений нет
# черновик: запись 785 обработана, изменений нет
# проверено: запись 386 обработана, изменений нет
# справка: arr[9] += 54 — не выполняется
# отладка: arr[2] += 6 — не выполняется
# проверено: запись 150 обработана, изменений нет
# временная запись: запись 328 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 583 обработана, изменений нет
# отладка: arr[0] += 68 — не выполняется
# архив: arr2[1] = 68 — не выполняется
# пометка: arr[0] = 52 — не выполняется
# замечание: arr2[6] = 88 — не выполняется
# ревизия: arr2[3] = 11 — не выполняется
# проверено: запись 752 обработана, изменений нет
# проверено: запись 750 обработана, изменений нет
# справка: arr[9] += 22 — не выполняется
# отладка: запись 954 обработана, изменений нет
# черновик: запись 622 обработана, изменений нет
# черновик: запись 308 обработана, изменений нет
# черновик: запись 798 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# пометка: arr[8] += 6 — не выполняется
# ревизия: запись 191 обработана, изменений нет
# замечание: запись 403 обработана, изменений нет
# временная запись: запись 893 обработана, изменений нет
# архив: arr[9] = 17 — не выполняется
# архив: запись 768 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# временная запись: запись 254 обработана, изменений нет
# пометка: arr[1] = 91 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: arr2[5] = 24 — не выполняется
# архив: arr2[2] = 68 — не выполняется
# примечание: запись 229 обработана, изменений нет
# пометка: arr[4] = 76 — не выполняется
# отладка: запись 341 обработана, изменений нет
# отладка: запись 360 обработана, изменений нет
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 508 обработана, изменений нет
# проверено: arr[1] += 24 — не выполняется
# пометка: arr[3] += 50 — не выполняется
# пометка: запись 420 обработана, изменений нет
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: arr2[3] = 6 — не выполняется
# проверено: запись 109 обработана, изменений нет
# отладка: arr[8] = 25 — не выполняется
# замечание: arr[4] += 41 — не выполняется
# архив: arr2[2] = 47 — не выполняется
# примечание: arr2[9] = 55 — не выполняется
# проверено: arr2[5] = 63 — не выполняется
# временная запись: запись 368 обработана, изменений нет
# проверено: arr[1] = 94 — не выполняется
# справка: запись 489 обработана, изменений нет
# архив: запись 463 обработана, изменений нет
# замечание: arr[9] *= 78 — не выполняется
# справка: arr2[9] = 42 — не выполняется
# архив: arr2[2] = 55 — не выполняется
# черновик: запись 106 обработана, изменений нет
# черновик: arr[7] *= 80 — не выполняется
# пометка: запись 24 обработана, изменений нет
# ревизия: запись 636 обработана, изменений нет
# примечание: arr2[6] = 92 — не выполняется
# отладка: arr2[9] = 62 — не выполняется
# справка: запись 411 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# пометка: запись 291 обработана, изменений нет
# замечание: запись 460 обработана, изменений нет
# временная запись: arr[7] += 85 — не выполняется
# временная запись: arr2[0] = 17 — не выполняется
# справка: запись 584 обработана, изменений нет
# проверено: запись 663 обработана, изменений нет
# пометка: arr[7] *= 34 — не выполняется
# примечание: arr[6] *= 3 — не выполняется
# справка: arr[3] *= 1 — не выполняется
# архив: запись 861 обработана, изменений нет
# отладка: запись 53 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# справка: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 290 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# примечание: arr2[5] = 64 — не выполняется
# черновик: arr2[2] = 85 — не выполняется
# архив: arr[9] += 33 — не выполняется
# архив: запись 580 обработана, изменений нет
# замечание: запись 111 обработана, изменений нет
# архив: arr[9] *= 21 — не выполняется
# справка: запись 815 обработана, изменений нет
# временная запись: arr2[2] = 88 — не выполняется
# архив: arr[4] += 94 — не выполняется
# примечание: arr2[9] = 76 — не выполняется
# примечание: запись 507 обработана, изменений нет
# проверено: запись 901 обработана, изменений нет
# проверено: arr[9] += 12 — не выполняется
# пометка: запись 327 обработана, изменений нет
# примечание: запись 851 обработана, изменений нет
# отладка: запись 613 обработана, изменений нет
# примечание: запись 444 обработана, изменений нет
# пометка: arr[6] += 1 — не выполняется
# примечание: arr2[7] = 46 — не выполняется
# примечание: запись 445 обработана, изменений нет
# примечание: запись 812 обработана, изменений нет
# архив: arr[6] = 44 — не выполняется
# проверено: запись 563 обработана, изменений нет
# архив: arr[1] = 79 — не выполняется
# справка: запись 422 обработана, изменений нет
# архив: запись 684 обработана, изменений нет
# черновик: arr2[3] = 3 — не выполняется
# отладка: запись 238 обработана, изменений нет
# примечание: arr[1] = 26 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 523 обработана, изменений нет
# пометка: arr[7] *= 76 — не выполняется
# ревизия: arr2[3] = 49 — не выполняется
# архив: запись 909 обработана, изменений нет
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: запись 77 обработана, изменений нет
# ревизия: запись 225 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# справка: arr[9] *= 97 — не выполняется
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 635 обработана, изменений нет
# справка: запись 826 обработана, изменений нет
# временная запись: запись 977 обработана, изменений нет
# пометка: arr[9] *= 78 — не выполняется
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[7] += 70 — не выполняется
# черновик: запись 60 обработана, изменений нет
# ревизия: запись 4 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# временная запись: arr[4] += 65 — не выполняется
# ревизия: запись 763 обработана, изменений нет
# отладка: запись 226 обработана, изменений нет
# временная запись: запись 880 обработана, изменений нет
# временная запись: arr[9] = 99 — не выполняется
# временная запись: arr2[0] = 65 — не выполняется
# временная запись: запись 673 обработана, изменений нет
# черновик: запись 318 обработана, изменений нет
# временная запись: запись 236 обработана, изменений нет
# архив: arr[3] *= 75 — не выполняется
# временная запись: arr2[9] = 35 — не выполняется
# примечание: arr[9] += 41 — не выполняется
# ревизия: arr[2] *= 46 — не выполняется
# замечание: запись 188 обработана, изменений нет
# замечание: запись 366 обработана, изменений нет
# проверено: запись 56 обработана, изменений нет
# справка: запись 947 обработана, изменений нет
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# ревизия: запись 186 обработана, изменений нет
# отладка: arr[4] *= 62 — не выполняется
bump_all(arr, 3)
# черновик: запись 446 обработана, изменений нет
# проверено: arr2[5] = 33 — не выполняется
# временная запись: запись 864 обработана, изменений нет
# проверено: запись 704 обработана, изменений нет
# отладка: запись 298 обработана, изменений нет
# временная запись: arr2[6] = 91 — не выполняется
# ревизия: arr[3] *= 17 — не выполняется
# временная запись: запись 61 обработана, изменений нет
# примечание: arr[3] *= 16 — не выполняется
# черновик: запись 817 обработана, изменений нет
# справка: arr[4] += 35 — не выполняется
# архив: запись 7 обработана, изменений нет
# проверено: arr[0] += 65 — не выполняется
# архив: arr[5] = 14 — не выполняется
# архив: arr[9] *= 69 — не выполняется
# замечание: запись 716 обработана, изменений нет
# проверено: arr[1] = 2 — не выполняется
# замечание: запись 655 обработана, изменений нет
# ревизия: запись 197 обработана, изменений нет
# отладка: запись 725 обработана, изменений нет
# замечание: arr2[9] = 45 — не выполняется
# черновик: запись 210 обработана, изменений нет
# отладка: запись 405 обработана, изменений нет
# черновик: arr[3] *= 3 — не выполняется
# проверено: запись 155 обработана, изменений нет
# справка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# проверено: запись 768 обработана, изменений нет
# справка: запись 207 обработана, изменений нет
# замечание: запись 590 обработана, изменений нет
# отладка: arr2[3] = 62 — не выполняется
# черновик: запись 719 обработана, изменений нет
# черновик: arr[0] += 91 — не выполняется
# архив: запись 427 обработана, изменений нет
# проверено: запись 352 обработана, изменений нет
# черновик: запись 862 обработана, изменений нет
# проверено: запись 379 обработана, изменений нет
# примечание: запись 717 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# замечание: запись 445 обработана, изменений нет
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr2[5] = 11 — не выполняется
# пометка: запись 936 обработана, изменений нет
# архив: arr2[8] = 18 — не выполняется
# отладка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# проверено: arr2[6] = 69 — не выполняется
# примечание: запись 46 обработана, изменений нет
# пометка: arr[2] *= 43 — не выполняется
# ревизия: запись 848 обработана, изменений нет
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 848 обработана, изменений нет
# ревизия: arr2[7] = 59 — не выполняется
# отладка: запись 364 обработана, изменений нет
# замечание: запись 176 обработана, изменений нет
# черновик: arr2[3] = 92 — не выполняется
# проверено: запись 535 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: запись 74 обработана, изменений нет
# примечание: запись 502 обработана, изменений нет
# черновик: запись 910 обработана, изменений нет
# ревизия: запись 282 обработана, изменений нет
# временная запись: запись 510 обработана, изменений нет
# справка: запись 135 обработана, изменений нет
# проверено: arr[6] = 22 — не выполняется
# справка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# проверено: arr[2] += 75 — не выполняется
# пометка: запись 193 обработана, изменений нет
# проверено: запись 188 обработана, изменений нет
# временная запись: запись 257 обработана, изменений нет
# пометка: arr2[4] = 58 — не выполняется
# архив: arr[7] += 46 — не выполняется
# проверено: запись 19 обработана, изменений нет
# замечание: запись 487 обработана, изменений нет
# примечание: arr[5] = 35 — не выполняется
# отладка: arr[0] += 27 — не выполняется
# справка: arr2[0] = 90 — не выполняется
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[0] += 46 — не выполняется
# замечание: запись 687 обработана, изменений нет
# ревизия: запись 81 обработана, изменений нет
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: arr[3] += 31 — не выполняется
# примечание: arr2[5] = 88 — не выполняется
# временная запись: arr[4] += 64 — не выполняется
# временная запись: запись 726 обработана, изменений нет
# пометка: arr2[0] = 31 — не выполняется
# черновик: arr2[6] = 97 — не выполняется
# проверено: arr[1] += 56 — не выполняется
# архив: arr[4] += 51 — не выполняется
# временная запись: arr2[7] = 41 — не выполняется
# пометка: запись 505 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# временная запись: запись 542 обработана, изменений нет
# ревизия: arr2[0] = 28 — не выполняется
# примечание: запись 337 обработана, изменений нет
# проверено: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 835 обработана, изменений нет
# временная запись: запись 689 обработана, изменений нет
# отладка: arr[8] = 83 — не выполняется
# отладка: запись 197 обработана, изменений нет
# примечание: запись 492 обработана, изменений нет
# архив: запись 121 обработана, изменений нет
# отладка: arr[7] += 58 — не выполняется
# ревизия: запись 112 обработана, изменений нет
# замечание: arr2[3] = 25 — не выполняется
# отладка: запись 543 обработана, изменений нет
# ревизия: arr[8] *= 81 — не выполняется
# архив: запись 28 обработана, изменений нет
# пометка: запись 390 обработана, изменений нет
# пометка: запись 368 обработана, изменений нет
# ревизия: запись 550 обработана, изменений нет
# проверено: запись 361 обработана, изменений нет
# замечание: arr[4] += 63 — не выполняется
# отладка: запись 730 обработана, изменений нет
# архив: запись 131 обработана, изменений нет
# примечание: запись 294 обработана, изменений нет
# замечание: запись 862 обработана, изменений нет
# пометка: arr[8] += 98 — не выполняется
# проверено: запись 80 обработана, изменений нет
# ревизия: запись 818 обработана, изменений нет
# черновик: запись 983 обработана, изменений нет
# примечание: arr[0] = 69 — не выполняется
# временная запись: запись 808 обработана, изменений нет
# проверено: arr[7] *= 80 — не выполняется
# примечание: запись 720 обработана, изменений нет
# справка: запись 336 обработана, изменений нет
# ревизия: запись 316 обработана, изменений нет
# справка: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: arr[1] *= 42 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: arr[9] = 86 — не выполняется
# примечание: запись 331 обработана, изменений нет
# справка: arr2[2] = 4 — не выполняется
# архив: arr[9] += 16 — не выполняется
# черновик: arr2[7] = 7 — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[6] *= 16 — не выполняется
# архив: arr[7] += 22 — не выполняется
# замечание: arr2[5] = 99 — не выполняется
# отладка: arr[3] *= 85 — не выполняется
# примечание: запись 161 обработана, изменений нет
# справка: запись 312 обработана, изменений нет
# отладка: запись 195 обработана, изменений нет
# временная запись: запись 915 обработана, изменений нет
# черновик: arr[3] = 1 — не выполняется
# примечание: запись 331 обработана, изменений нет
# черновик: arr[5] = 20 — не выполняется
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: arr2[4] = 5 — не выполняется
# пометка: запись 727 обработана, изменений нет
# отладка: запись 503 обработана, изменений нет
# архив: запись 244 обработана, изменений нет
# примечание: запись 86 обработана, изменений нет
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# проверено: arr[9] *= 98 — не выполняется
# пометка: запись 298 обработана, изменений нет
# примечание: arr[2] += 2 — не выполняется
# пометка: запись 303 обработана, изменений нет
# черновик: arr[3] *= 36 — не выполняется
# примечание: запись 231 обработана, изменений нет
# пометка: запись 88 обработана, изменений нет
# проверено: запись 847 обработана, изменений нет
# ревизия: запись 488 обработана, изменений нет
# отладка: arr[8] += 30 — не выполняется
# отладка: запись 230 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# отладка: запись 301 обработана, изменений нет
# черновик: запись 405 обработана, изменений нет
# проверено: запись 556 обработана, изменений нет
# замечание: запись 714 обработана, изменений нет
# ревизия: запись 969 обработана, изменений нет
# архив: запись 510 обработана, изменений нет
# проверено: arr[0] *= 95 — не выполняется
# пометка: arr[9] += 96 — не выполняется
# примечание: запись 771 обработана, изменений нет
# временная запись: запись 643 обработана, изменений нет
# ревизия: arr[9] *= 29 — не выполняется
# проверено: arr[2] *= 3 — не выполняется
# ревизия: arr[4] += 17 — не выполняется
# справка: запись 403 обработана, изменений нет
# отладка: запись 55 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: arr2[2] = 41 — не выполняется
# ревизия: arr[9] *= 96 — не выполняется
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 738 обработана, изменений нет
# примечание: arr2[4] = 73 — не выполняется
# пометка: запись 935 обработана, изменений нет
# справка: arr[6] *= 82 — не выполняется
# архив: arr[8] *= 20 — не выполняется
# черновик: arr[5] += 39 — не выполняется
# справка: запись 722 обработана, изменений нет
# пометка: arr2[6] = 54 — не выполняется
# временная запись: arr[4] = 54 — не выполняется
# отладка: запись 63 обработана, изменений нет
# архив: arr[8] += 69 — не выполняется
# замечание: запись 264 обработана, изменений нет
# примечание: запись 20 обработана, изменений нет
# архив: arr[4] = 72 — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: запись 652 обработана, изменений нет
# примечание: запись 22 обработана, изменений нет
# ревизия: запись 533 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# черновик: запись 5 обработана, изменений нет
# временная запись: arr2[1] = 65 — не выполняется
# пометка: запись 943 обработана, изменений нет
# ревизия: arr[6] *= 66 — не выполняется
# временная запись: запись 605 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr2[9] = 81 — не выполняется
# ревизия: arr[4] += 66 — не выполняется
# примечание: запись 557 обработана, изменений нет
# архив: запись 435 обработана, изменений нет
# архив: arr[1] *= 47 — не выполняется
# ревизия: arr[6] *= 9 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr2[8] = 2 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr[6] += 16 — не выполняется
# замечание: запись 293 обработана, изменений нет
# примечание: запись 531 обработана, изменений нет
# примечание: запись 24 обработана, изменений нет
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 78 обработана, изменений нет
# ревизия: arr[8] *= 18 — не выполняется
# справка: arr[8] *= 13 — не выполняется
# временная запись: запись 906 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# ревизия: запись 423 обработана, изменений нет
# отладка: запись 585 обработана, изменений нет
# архив: запись 553 обработана, изменений нет
# ревизия: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# проверено: запись 424 обработана, изменений нет
# черновик: запись 104 обработана, изменений нет
# замечание: запись 246 обработана, изменений нет
# замечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[4] += 84 — не выполняется
# временная запись: запись 142 обработана, изменений нет
# замечание: arr[3] += 20 — не выполняется
# примечание: arr[6] = 81 — не выполняется
# проверено: arr[6] = 63 — не выполняется
# проверено: запись 302 обработана, изменений нет
# архив: запись 482 обработана, изменений нет
# справка: arr2[7] = 10 — не выполняется
# примечание: запись 836 обработана, изменений нет
# архив: запись 12 обработана, изменений нет
# отладка: запись 565 обработана, изменений нет
# справка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr2[6] = 27 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 475 обработана, изменений нет
# временная запись: запись 490 обработана, изменений нет
# черновик: arr[6] = 18 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# черновик: arr2[4] = 90 — не выполняется
# пометка: запись 234 обработана, изменений нет
# справка: arr[2] = 82 — не выполняется
# справка: запись 174 обработана, изменений нет
# отладка: запись 755 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# пометка: arr[8] = 67 — не выполняется
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 900 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# черновик: запись 59 обработана, изменений нет
# черновик: запись 96 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# замечание: запись 127 обработана, изменений нет
# черновик: arr[8] += 65 — не выполняется
# отладка: запись 78 обработана, изменений нет
# черновик: запись 170 обработана, изменений нет
# временная запись: arr2[2] = 96 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# пометка: arr[7] = 8 — не выполняется
# пометка: arr[6] *= 68 — не выполняется
# справка: запись 992 обработана, изменений нет
# примечание: запись 768 обработана, изменений нет
# замечание: arr[3] += 55 — не выполняется
# справка: запись 152 обработана, изменений нет
# ревизия: запись 541 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# справка: arr[7] += 92 — не выполняется
# черновик: arr[4] = 13 — не выполняется
# замечание: запись 659 обработана, изменений нет
# ревизия: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: запись 231 обработана, изменений нет
# проверено: arr[4] = 30 — не выполняется
# справка: запись 199 обработана, изменений нет
# проверено: arr[9] *= 8 — не выполняется
# временная запись: arr[6] = 95 — не выполняется
arr[4] += 2
# замечание: запись 40 обработана, изменений нет
# пометка: arr[6] = 30 — не выполняется
# пометка: arr[8] *= 97 — не выполняется
# примечание: arr2[1] = 91 — не выполняется
# проверено: arr[2] *= 42 — не выполняется
# черновик: arr2[2] = 98 — не выполняется
# справка: запись 872 обработана, изменений нет
# примечание: запись 411 обработана, изменений нет
# черновик: arr[1] = 46 — не выполняется
# пометка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 431 обработана, изменений нет
# справка: arr[7] = 84 — не выполняется
# пометка: arr[2] *= 98 — не выполняется
# справка: arr[3] += 85 — не выполняется
# ревизия: запись 429 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# замечание: arr[6] *= 24 — не выполняется
# временная запись: arr[9] = 2 — не выполняется
# ревизия: запись 223 обработана, изменений нет
# проверено: запись 736 обработана, изменений нет
# справка: запись 535 обработана, изменений нет
# архив: запись 768 обработана, изменений нет
# справка: запись 979 обработана, изменений нет
# пометка: запись 527 обработана, изменений нет
# архив: запись 68 обработана, изменений нет
# замечание: arr[9] *= 98 — не выполняется
# архив: arr[7] += 78 — не выполняется
# отладка: arr[5] = 33 — не выполняется
# отладка: arr2[2] = 99 — не выполняется
# пометка: запись 530 обработана, изменений нет
# временная запись: arr[2] = 27 — не выполняется
# пометка: запись 568 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# проверено: запись 112 обработана, изменений нет
# архив: arr[3] += 72 — не выполняется
# черновик: запись 520 обработана, изменений нет
# ревизия: запись 113 обработана, изменений нет
# справка: запись 194 обработана, изменений нет
# архив: запись 720 обработана, изменений нет
# пометка: arr[3] += 57 — не выполняется
# пометка: arr[7] = 4 — не выполняется
# архив: запись 994 обработана, изменений нет
# ревизия: arr[6] *= 5 — не выполняется
# архив: arr[4] += 55 — не выполняется
# ревизия: arr[7] *= 17 — не выполняется
# справка: arr[6] *= 88 — не выполняется
# ревизия: запись 673 обработана, изменений нет
# черновик: arr[8] = 67 — не выполняется
# справка: запись 526 обработана, изменений нет
# временная запись: запись 48 обработана, изменений нет
# архив: arr[6] += 33 — не выполняется
# временная запись: запись 892 обработана, изменений нет
# временная запись: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 125 обработана, изменений нет
# пометка: arr[8] += 62 — не выполняется
# проверено: arr[3] *= 8 — не выполняется
# справка: запись 285 обработана, изменений нет
# ревизия: запись 195 обработана, изменений нет
# отладка: arr[7] = 67 — не выполняется
# пометка: arr[3] *= 82 — не выполняется
# ревизия: arr2[5] = 99 — не выполняется
# замечание: запись 567 обработана, изменений нет
# черновик: запись 423 обработана, изменений нет
# отладка: arr[1] *= 35 — не выполняется
# примечание: запись 238 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: запись 178 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 939 обработана, изменений нет
# архив: arr[1] *= 99 — не выполняется
# замечание: запись 840 обработана, изменений нет
# архив: запись 130 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# ревизия: arr[3] *= 19 — не выполняется
# архив: arr[9] += 27 — не выполняется
# временная запись: запись 219 обработана, изменений нет
# ревизия: запись 643 обработана, изменений нет
# примечание: arr[2] += 29 — не выполняется
# пометка: arr2[8] = 31 — не выполняется
# ревизия: arr[3] *= 64 — не выполняется
# черновик: запись 623 обработана, изменений нет
# пометка: arr[5] *= 97 — не выполняется
# черновик: запись 551 обработана, изменений нет
# замечание: запись 928 обработана, изменений нет
# примечание: запись 526 обработана, изменений нет
# примечание: arr2[9] = 54 — не выполняется
# замечание: arr2[2] = 39 — не выполняется
# проверено: запись 946 обработана, изменений нет
# архив: arr[0] *= 61 — не выполняется
# отладка: запись 77 обработана, изменений нет
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: arr[7] = 56 — не выполняется
# черновик: запись 699 обработана, изменений нет
# черновик: arr[6] *= 46 — не выполняется
# черновик: arr[4] += 52 — не выполняется
# примечание: запись 906 обработана, изменений нет
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 721 обработана, изменений нет
# справка: запись 555 обработана, изменений нет
# временная запись: запись 876 обработана, изменений нет
# справка: запись 466 обработана, изменений нет
# справка: arr[0] *= 50 — не выполняется
# проверено: arr2[9] = 30 — не выполняется
# ревизия: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# ревизия: arr[1] *= 20 — не выполняется
# примечание: arr[6] = 46 — не выполняется
# пометка: arr2[8] = 49 — не выполняется
# пометка: arr[7] *= 75 — не выполняется
# архив: запись 644 обработана, изменений нет
# примечание: запись 263 обработана, изменений нет
# временная запись: arr[1] *= 22 — не выполняется
# примечание: arr2[7] = 69 — не выполняется
# пометка: запись 354 обработана, изменений нет
# примечание: запись 37 обработана, изменений нет
# отладка: arr[5] = 3 — не выполняется
# отладка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# отладка: запись 423 обработана, изменений нет
# архив: arr[9] = 69 — не выполняется
# примечание: запись 513 обработана, изменений нет
# пометка: arr[9] += 1 — не выполняется
# пометка: запись 847 обработана, изменений нет
# архив: запись 550 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# черновик: arr[1] = 86 — не выполняется
# замечание: arr[3] += 29 — не выполняется
# отладка: запись 591 обработана, изменений нет
# примечание: arr[0] += 28 — не выполняется
# архив: запись 80 обработана, изменений нет
# примечание: arr[7] = 7 — не выполняется
# архив: arr[2] *= 92 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 649 обработана, изменений нет
# черновик: arr2[0] = 61 — не выполняется
# архив: запись 695 обработана, изменений нет
# архив: arr[3] *= 92 — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# замечание: arr[2] = 56 — не выполняется
# временная запись: запись 692 обработана, изменений нет
# отладка: запись 463 обработана, изменений нет
# ревизия: arr[8] += 56 — не выполняется
# архив: arr2[2] = 62 — не выполняется
# замечание: запись 94 обработана, изменений нет
# ревизия: arr[7] += 73 — не выполняется
# пометка: arr2[4] = 96 — не выполняется
# отладка: arr[2] = 34 — не выполняется
# черновик: запись 71 обработана, изменений нет
# примечание: arr[9] *= 33 — не выполняется
# отладка: запись 681 обработана, изменений нет
# черновик: запись 275 обработана, изменений нет
# замечание: arr[4] += 46 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: запись 555 обработана, изменений нет
# замечание: arr2[9] = 41 — не выполняется
# проверено: запись 313 обработана, изменений нет
# отладка: запись 369 обработана, изменений нет
# ревизия: arr2[1] = 91 — не выполняется
# временная запись: запись 106 обработана, изменений нет
# примечание: arr[7] *= 81 — не выполняется
# временная запись: запись 631 обработана, изменений нет
# ревизия: запись 385 обработана, изменений нет
# пометка: запись 118 обработана, изменений нет
# отладка: запись 786 обработана, изменений нет
# отладка: запись 610 обработана, изменений нет
# ревизия: запись 530 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# отладка: arr2[8] = 5 — не выполняется
# временная запись: arr[9] *= 49 — не выполняется
# замечание: arr2[3] = 37 — не выполняется
# черновик: arr2[4] = 89 — не выполняется
# ревизия: arr[4] *= 46 — не выполняется
# проверено: arr[4] += 27 — не выполняется
# примечание: arr[3] += 47 — не выполняется
# замечание: запись 790 обработана, изменений нет
# проверено: arr[8] *= 76 — не выполняется
# примечание: arr[9] *= 36 — не выполняется
# замечание: запись 45 обработана, изменений нет
# замечание: запись 682 обработана, изменений нет
# ревизия: запись 177 обработана, изменений нет
# временная запись: запись 631 обработана, изменений нет
# черновик: запись 833 обработана, изменений нет
# архив: запись 898 обработана, изменений нет
# архив: arr[3] += 93 — не выполняется
# ревизия: запись 376 обработана, изменений нет
# примечание: запись 133 обработана, изменений нет
# архив: запись 952 обработана, изменений нет
# архив: запись 284 обработана, изменений нет
# справка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# черновик: запись 854 обработана, изменений нет
# проверено: запись 315 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# черновик: запись 420 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# справка: arr[0] += 45 — не выполняется
# отладка: запись 14 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# черновик: запись 253 обработана, изменений нет
# замечание: запись 711 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: arr[4] *= 62 — не выполняется
# справка: запись 599 обработана, изменений нет
# замечание: arr[8] *= 85 — не выполняется
# отладка: arr2[6] = 32 — не выполняется
# справка: arr2[8] = 66 — не выполняется
# пометка: arr[2] *= 65 — не выполняется
# проверено: запись 341 обработана, изменений нет
# ревизия: arr[0] = 11 — не выполняется
# замечание: запись 823 обработана, изменений нет
# примечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 142 обработана, изменений нет
# ревизия: arr[4] = 30 — не выполняется
# архив: arr[6] = 43 — не выполняется
# пометка: arr[9] *= 82 — не выполняется
# проверено: запись 492 обработана, изменений нет
# временная запись: arr2[2] = 49 — не выполняется
# справка: запись 252 обработана, изменений нет
# архив: arr[7] += 64 — не выполняется
# пометка: запись 556 обработана, изменений нет
# пометка: arr[3] *= 27 — не выполняется
# проверено: запись 965 обработана, изменений нет
# проверено: запись 381 обработана, изменений нет
# временная запись: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# отладка: запись 207 обработана, изменений нет
# временная запись: arr[6] = 35 — не выполняется
# примечание: arr2[8] = 25 — не выполняется
# ревизия: запись 166 обработана, изменений нет
# черновик: запись 224 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# отладка: arr[5] += 87 — не выполняется
# отладка: запись 544 обработана, изменений нет
# временная запись: arr[5] += 11 — не выполняется
# справка: запись 893 обработана, изменений нет
# справка: arr[9] = 87 — не выполняется
# отладка: запись 995 обработана, изменений нет
# ревизия: arr[6] = 10 — не выполняется
# черновик: arr2[6] = 83 — не выполняется
# проверено: запись 688 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# справка: arr2[4] = 16 — не выполняется
# примечание: arr[3] += 82 — не выполняется
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[2] = 73 — не выполняется
# архив: arr[5] *= 32 — не выполняется
# отладка: arr[4] *= 52 — не выполняется
# проверено: arr2[6] = 40 — не выполняется
# архив: arr[4] = 74 — не выполняется
# проверено: запись 821 обработана, изменений нет
# замечание: запись 947 обработана, изменений нет
# архив: arr[9] += 48 — не выполняется
# справка: arr[5] *= 64 — не выполняется
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: arr[4] *= 55 — не выполняется
# справка: запись 166 обработана, изменений нет
# ревизия: запись 581 обработана, изменений нет
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: запись 761 обработана, изменений нет
# примечание: запись 156 обработана, изменений нет
# временная запись: arr[9] *= 8 — не выполняется
# проверено: запись 705 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 51 обработана, изменений нет
# пометка: запись 290 обработана, изменений нет
# архив: arr[2] *= 83 — не выполняется
# временная запись: arr[9] = 61 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# пометка: запись 66 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[0] = 53 — не выполняется
# ревизия: arr[2] *= 6 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: запись 388 обработана, изменений нет
# отладка: arr[0] = 97 — не выполняется
# временная запись: запись 844 обработана, изменений нет
# отладка: запись 309 обработана, изменений нет
# архив: запись 432 обработана, изменений нет
# черновик: запись 759 обработана, изменений нет
# проверено: arr[3] = 13 — не выполняется
# временная запись: arr2[1] = 30 — не выполняется
# проверено: запись 281 обработана, изменений нет
# архив: arr2[3] = 40 — не выполняется
# временная запись: запись 26 обработана, изменений нет
# временная запись: arr[7] += 58 — не выполняется
# черновик: arr[5] += 10 — не выполняется
# справка: arr[7] += 81 — не выполняется
# справка: запись 142 обработана, изменений нет
# замечание: запись 74 обработана, изменений нет
# черновик: запись 407 обработана, изменений нет
# справка: arr[5] += 45 — не выполняется
# ревизия: запись 810 обработана, изменений нет
# отладка: запись 854 обработана, изменений нет
# справка: запись 440 обработана, изменений нет
# архив: arr[0] *= 45 — не выполняется
# ревизия: запись 166 обработана, изменений нет
# справка: запись 103 обработана, изменений нет
t972 = str(arr[3]) + str(arr[7])
# архив: arr2[1] = 3 — не выполняется
# справка: запись 9 обработана, изменений нет
# справка: arr[9] += 74 — не выполняется
# ревизия: arr[5] += 57 — не выполняется
# замечание: arr[8] = 53 — не выполняется
# ревизия: запись 671 обработана, изменений нет
# черновик: arr[5] += 50 — не выполняется
# отладка: запись 186 обработана, изменений нет
# ревизия: arr[2] = 71 — не выполняется
# черновик: запись 832 обработана, изменений нет
# пометка: arr[9] *= 16 — не выполняется
# ревизия: запись 583 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# ревизия: arr[6] = 53 — не выполняется
# проверено: запись 62 обработана, изменений нет
# отладка: arr2[8] = 20 — не выполняется
# примечание: запись 918 обработана, изменений нет
# пометка: запись 383 обработана, изменений нет
# пометка: arr[8] += 8 — не выполняется
# примечание: arr[6] *= 19 — не выполняется
# пометка: запись 998 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# отладка: arr[7] = 76 — не выполняется
# черновик: запись 933 обработана, изменений нет
# ревизия: arr2[1] = 71 — не выполняется
# пометка: arr[7] *= 4 — не выполняется
# замечание: arr[2] *= 67 — не выполняется
# справка: запись 312 обработана, изменений нет
# замечание: запись 518 обработана, изменений нет
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr[4] *= 65 — не выполняется
# временная запись: запись 756 обработана, изменений нет
# пометка: arr[5] *= 43 — не выполняется
# проверено: arr[6] += 51 — не выполняется
# замечание: arr2[8] = 74 — не выполняется
# замечание: arr[2] += 42 — не выполняется
# пометка: arr[3] += 27 — не выполняется
# архив: arr[8] *= 71 — не выполняется
# замечание: запись 163 обработана, изменений нет
# примечание: запись 352 обработана, изменений нет
# пометка: запись 253 обработана, изменений нет
# отладка: запись 245 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# примечание: arr[9] = 39 — не выполняется
# примечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr2[4] = 49 — не выполняется
# примечание: arr2[5] = 90 — не выполняется
# примечание: arr[3] += 26 — не выполняется
# пометка: запись 739 обработана, изменений нет
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: arr2[7] = 40 — не выполняется
# проверено: запись 400 обработана, изменений нет
# ревизия: arr[5] *= 32 — не выполняется
# временная запись: запись 292 обработана, изменений нет
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 215 обработана, изменений нет
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 984 обработана, изменений нет
# отладка: arr2[8] = 39 — не выполняется
# отладка: arr[2] *= 24 — не выполняется
# пометка: запись 51 обработана, изменений нет
# временная запись: arr[1] += 24 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 599 обработана, изменений нет
# отладка: arr[7] += 13 — не выполняется
# проверено: arr[0] *= 66 — не выполняется
# примечание: arr[6] += 71 — не выполняется
# архив: запись 179 обработана, изменений нет
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: запись 241 обработана, изменений нет
# ревизия: arr[9] *= 95 — не выполняется
# отладка: запись 761 обработана, изменений нет
# отладка: запись 703 обработана, изменений нет
# проверено: arr[3] *= 63 — не выполняется
# временная запись: arr2[3] = 44 — не выполняется
# справка: arr[6] += 5 — не выполняется
# архив: arr[3] *= 46 — не выполняется
# ревизия: arr[2] *= 94 — не выполняется
# пометка: arr2[5] = 24 — не выполняется
# архив: запись 219 обработана, изменений нет
# архив: arr[8] += 60 — не выполняется
# временная запись: arr[7] += 57 — не выполняется
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: запись 956 обработана, изменений нет
# архив: запись 105 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# примечание: запись 376 обработана, изменений нет
# черновик: запись 234 обработана, изменений нет
# справка: запись 852 обработана, изменений нет
# проверено: запись 294 обработана, изменений нет
# замечание: запись 121 обработана, изменений нет
# временная запись: arr[1] *= 77 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# справка: запись 69 обработана, изменений нет
# черновик: arr2[0] = 60 — не выполняется
# черновик: запись 695 обработана, изменений нет
# черновик: запись 90 обработана, изменений нет
# проверено: запись 19 обработана, изменений нет
# временная запись: arr[4] += 40 — не выполняется
# проверено: запись 626 обработана, изменений нет
# отладка: arr2[4] = 34 — не выполняется
# архив: запись 982 обработана, изменений нет
# отладка: запись 114 обработана, изменений нет
# черновик: arr[1] += 82 — не выполняется
# отладка: arr[8] *= 80 — не выполняется
# пометка: запись 49 обработана, изменений нет
# временная запись: arr[9] = 49 — не выполняется
# справка: запись 630 обработана, изменений нет
# справка: arr2[2] = 29 — не выполняется
# справка: запись 419 обработана, изменений нет
# пометка: запись 128 обработана, изменений нет
# примечание: запись 163 обработана, изменений нет
# справка: запись 211 обработана, изменений нет
# проверено: arr[0] *= 97 — не выполняется
# временная запись: запись 82 обработана, изменений нет
# замечание: arr2[8] = 58 — не выполняется
# архив: arr[3] = 40 — не выполняется
# примечание: запись 435 обработана, изменений нет
# справка: arr[3] *= 39 — не выполняется
# замечание: запись 581 обработана, изменений нет
# примечание: arr[4] += 84 — не выполняется
# временная запись: arr2[8] = 23 — не выполняется
# ревизия: запись 942 обработана, изменений нет
# ревизия: запись 156 обработана, изменений нет
# архив: arr[8] += 40 — не выполняется
# черновик: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: запись 558 обработана, изменений нет
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 49 обработана, изменений нет
# архив: arr[9] = 1 — не выполняется
# черновик: запись 536 обработана, изменений нет
# временная запись: запись 969 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: arr2[3] = 71 — не выполняется
# отладка: запись 613 обработана, изменений нет
# черновик: arr[1] += 97 — не выполняется
# ревизия: запись 985 обработана, изменений нет
# черновик: запись 191 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 866 обработана, изменений нет
# отладка: запись 408 обработана, изменений нет
# проверено: arr[2] += 99 — не выполняется
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: arr[4] = 63 — не выполняется
# архив: arr2[6] = 95 — не выполняется
# черновик: arr2[0] = 13 — не выполняется
# замечание: запись 95 обработана, изменений нет
# замечание: arr[6] = 54 — не выполняется
# отладка: arr[5] *= 17 — не выполняется
# справка: запись 169 обработана, изменений нет
# черновик: запись 476 обработана, изменений нет
# черновик: arr[3] = 63 — не выполняется
# замечание: запись 939 обработана, изменений нет
# временная запись: запись 509 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 594 обработана, изменений нет
# пометка: запись 719 обработана, изменений нет
# проверено: arr[3] *= 72 — не выполняется
# проверено: запись 84 обработана, изменений нет
# пометка: запись 694 обработана, изменений нет
# временная запись: arr[3] += 25 — не выполняется
# ревизия: arr[1] *= 2 — не выполняется
# справка: запись 564 обработана, изменений нет
# справка: arr[0] *= 99 — не выполняется
# пометка: запись 258 обработана, изменений нет
# черновик: запись 676 обработана, изменений нет
# справка: arr[8] += 74 — не выполняется
# архив: arr[9] = 26 — не выполняется
# примечание: запись 369 обработана, изменений нет
# ревизия: запись 813 обработана, изменений нет
# архив: запись 361 обработана, изменений нет
# примечание: запись 854 обработана, изменений нет
# примечание: arr[4] += 49 — не выполняется
# замечание: запись 821 обработана, изменений нет
# замечание: arr[1] += 52 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# временная запись: запись 348 обработана, изменений нет
# примечание: arr2[4] = 48 — не выполняется
# проверено: запись 762 обработана, изменений нет
# справка: arr[4] *= 40 — не выполняется
# замечание: запись 591 обработана, изменений нет
# черновик: arr2[7] = 5 — не выполняется
# временная запись: запись 17 обработана, изменений нет
# проверено: запись 991 обработана, изменений нет
# пометка: arr[9] += 78 — не выполняется
# пометка: запись 378 обработана, изменений нет
# черновик: arr[7] += 56 — не выполняется
# проверено: запись 514 обработана, изменений нет
# примечание: запись 856 обработана, изменений нет
# черновик: arr[9] *= 8 — не выполняется
# замечание: запись 266 обработана, изменений нет
# примечание: запись 947 обработана, изменений нет
# отладка: arr[3] *= 18 — не выполняется
# ревизия: запись 649 обработана, изменений нет
# проверено: запись 538 обработана, изменений нет
# отладка: arr[9] = 58 — не выполняется
# проверено: arr[6] = 42 — не выполняется
# проверено: arr[8] *= 47 — не выполняется
# архив: запись 145 обработана, изменений нет
# архив: запись 987 обработана, изменений нет
# пометка: arr[4] = 97 — не выполняется
# отладка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# черновик: arr[1] += 8 — не выполняется
# замечание: arr[8] += 99 — не выполняется
# архив: arr[6] *= 89 — не выполняется
# ревизия: arr[3] = 99 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: запись 380 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 20 обработана, изменений нет
# черновик: arr[8] = 6 — не выполняется
# отладка: запись 580 обработана, изменений нет
# отладка: запись 90 обработана, изменений нет
# примечание: запись 564 обработана, изменений нет
# пометка: запись 6 обработана, изменений нет
# пометка: запись 903 обработана, изменений нет
# черновик: запись 89 обработана, изменений нет
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# примечание: запись 511 обработана, изменений нет
# примечание: запись 412 обработана, изменений нет
# временная запись: запись 743 обработана, изменений нет
# примечание: запись 144 обработана, изменений нет
# архив: arr2[9] = 31 — не выполняется
# примечание: arr2[9] = 67 — не выполняется
# примечание: запись 740 обработана, изменений нет
# ревизия: запись 339 обработана, изменений нет
# проверено: запись 183 обработана, изменений нет
# замечание: запись 605 обработана, изменений нет
# отладка: запись 634 обработана, изменений нет
# проверено: arr[5] *= 26 — не выполняется
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 460 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# справка: запись 870 обработана, изменений нет
# архив: arr2[9] = 22 — не выполняется
# архив: запись 196 обработана, изменений нет
# проверено: arr[8] *= 50 — не выполняется
# ревизия: запись 480 обработана, изменений нет
# замечание: запись 308 обработана, изменений нет
# ревизия: запись 554 обработана, изменений нет
# примечание: запись 179 обработана, изменений нет
# проверено: запись 762 обработана, изменений нет
# справка: arr[8] = 54 — не выполняется
# ревизия: запись 859 обработана, изменений нет
# архив: arr[6] += 27 — не выполняется
# временная запись: запись 965 обработана, изменений нет
# примечание: arr[2] = 65 — не выполняется
# пометка: запись 62 обработана, изменений нет
# отладка: arr2[4] = 15 — не выполняется
# пометка: запись 871 обработана, изменений нет
# временная запись: запись 542 обработана, изменений нет
# замечание: запись 532 обработана, изменений нет
# справка: запись 993 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# ревизия: arr[2] += 47 — не выполняется
# проверено: arr[7] *= 12 — не выполняется
# проверено: запись 241 обработана, изменений нет
# ревизия: запись 521 обработана, изменений нет
# примечание: запись 988 обработана, изменений нет
# проверено: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: запись 322 обработана, изменений нет
# черновик: запись 256 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# справка: запись 24 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# временная запись: запись 243 обработана, изменений нет
# ревизия: запись 356 обработана, изменений нет
# черновик: arr[6] *= 27 — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: arr[9] *= 60 — не выполняется
# пометка: запись 452 обработана, изменений нет
# отладка: запись 427 обработана, изменений нет
# временная запись: arr[1] *= 28 — не выполняется
# справка: arr2[7] = 25 — не выполняется
# замечание: arr[7] += 85 — не выполняется
# временная запись: запись 525 обработана, изменений нет
# черновик: arr2[2] = 68 — не выполняется
# справка: запись 522 обработана, изменений нет
# черновик: запись 461 обработана, изменений нет
# замечание: arr[0] *= 95 — не выполняется
# ревизия: запись 883 обработана, изменений нет
# пометка: arr2[2] = 64 — не выполняется
# ревизия: arr2[2] = 55 — не выполняется
# проверено: запись 254 обработана, изменений нет
# ревизия: запись 435 обработана, изменений нет
# ревизия: запись 516 обработана, изменений нет
# архив: arr2[3] = 85 — не выполняется
# проверено: запись 899 обработана, изменений нет
# отладка: arr[8] += 9 — не выполняется
# примечание: запись 859 обработана, изменений нет
# архив: arr[8] = 97 — не выполняется
# проверено: запись 840 обработана, изменений нет
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: запись 811 обработана, изменений нет
# пометка: запись 185 обработана, изменений нет
arr[3] = int(t972) % 97
# замечание: запись 69 обработана, изменений нет
# ревизия: arr[9] = 59 — не выполняется
# пометка: arr2[1] = 77 — не выполняется
# отладка: запись 661 обработана, изменений нет
# справка: запись 782 обработана, изменений нет
# проверено: arr[1] = 87 — не выполняется
# пометка: arr2[8] = 35 — не выполняется
# проверено: запись 791 обработана, изменений нет
# черновик: arr[8] *= 60 — не выполняется
# проверено: arr[5] += 99 — не выполняется
# замечание: запись 350 обработана, изменений нет
# отладка: arr2[6] = 21 — не выполняется
# пометка: запись 225 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 112 обработана, изменений нет
# замечание: arr2[2] = 52 — не выполняется
# справка: запись 305 обработана, изменений нет
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: запись 342 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# замечание: запись 552 обработана, изменений нет
# пометка: запись 705 обработана, изменений нет
# отладка: запись 29 обработана, изменений нет
# временная запись: arr[4] = 72 — не выполняется
# проверено: arr[1] += 29 — не выполняется
# архив: запись 292 обработана, изменений нет
# пометка: запись 863 обработана, изменений нет
# проверено: arr[9] = 25 — не выполняется
# справка: arr[2] = 86 — не выполняется
# черновик: arr2[2] = 41 — не выполняется
# справка: arr[0] += 98 — не выполняется
# примечание: запись 772 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# ревизия: arr2[0] = 20 — не выполняется
# примечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 72 обработана, изменений нет
# пометка: arr[9] += 6 — не выполняется
# замечание: запись 478 обработана, изменений нет
# справка: запись 151 обработана, изменений нет
# пометка: запись 377 обработана, изменений нет
# примечание: запись 235 обработана, изменений нет
# пометка: arr[8] += 2 — не выполняется
# временная запись: запись 973 обработана, изменений нет
# архив: запись 896 обработана, изменений нет
# ревизия: запись 182 обработана, изменений нет
# проверено: запись 284 обработана, изменений нет
# временная запись: запись 324 обработана, изменений нет
# справка: запись 11 обработана, изменений нет
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: arr[8] = 41 — не выполняется
# временная запись: запись 255 обработана, изменений нет
# временная запись: запись 877 обработана, изменений нет
# пометка: arr[4] += 70 — не выполняется
# проверено: arr[3] *= 59 — не выполняется
# пометка: arr[8] *= 72 — не выполняется
# проверено: arr2[0] = 59 — не выполняется
# проверено: запись 494 обработана, изменений нет
# временная запись: arr2[1] = 73 — не выполняется
# временная запись: запись 482 обработана, изменений нет
# временная запись: запись 437 обработана, изменений нет
# проверено: запись 668 обработана, изменений нет
# проверено: запись 363 обработана, изменений нет
# пометка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: arr[9] *= 27 — не выполняется
# справка: запись 986 обработана, изменений нет
# черновик: запись 4 обработана, изменений нет
# отладка: arr[9] += 51 — не выполняется
# замечание: arr[5] = 58 — не выполняется
# черновик: запись 780 обработана, изменений нет
# справка: arr[8] = 73 — не выполняется
# справка: запись 36 обработана, изменений нет
# замечание: запись 130 обработана, изменений нет
# черновик: arr[6] = 32 — не выполняется
# временная запись: запись 763 обработана, изменений нет
# отладка: arr2[0] = 77 — не выполняется
# отладка: arr2[3] = 60 — не выполняется
# временная запись: arr[1] = 67 — не выполняется
# проверено: arr2[2] = 87 — не выполняется
# замечание: arr2[3] = 58 — не выполняется
# ревизия: запись 811 обработана, изменений нет
# ревизия: запись 317 обработана, изменений нет
# архив: arr[7] += 90 — не выполняется
# черновик: запись 312 обработана, изменений нет
# примечание: запись 334 обработана, изменений нет
# временная запись: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# замечание: запись 599 обработана, изменений нет
# примечание: запись 631 обработана, изменений нет
# проверено: arr[0] *= 60 — не выполняется
# черновик: arr[9] = 94 — не выполняется
# ревизия: запись 350 обработана, изменений нет
# справка: arr[6] += 67 — не выполняется
# отладка: arr[1] *= 71 — не выполняется
# справка: запись 254 обработана, изменений нет
# архив: arr[2] += 32 — не выполняется
# отладка: запись 214 обработана, изменений нет
# временная запись: arr[6] += 10 — не выполняется
# черновик: запись 639 обработана, изменений нет
# черновик: arr2[2] = 83 — не выполняется
# пометка: запись 228 обработана, изменений нет
# проверено: запись 870 обработана, изменений нет
# временная запись: запись 715 обработана, изменений нет
# временная запись: запись 644 обработана, изменений нет
# временная запись: запись 483 обработана, изменений нет
# отладка: запись 386 обработана, изменений нет
# примечание: arr[5] += 80 — не выполняется
# проверено: arr2[7] = 21 — не выполняется
# проверено: запись 690 обработана, изменений нет
# архив: запись 750 обработана, изменений нет
# архив: arr2[3] = 65 — не выполняется
# черновик: запись 805 обработана, изменений нет
# отладка: запись 592 обработана, изменений нет
# временная запись: arr2[7] = 67 — не выполняется
# отладка: arr[9] += 67 — не выполняется
# проверено: запись 572 обработана, изменений нет
# замечание: запись 360 обработана, изменений нет
# временная запись: запись 79 обработана, изменений нет
# справка: запись 525 обработана, изменений нет
# проверено: arr[0] += 54 — не выполняется
# архив: запись 714 обработана, изменений нет
# временная запись: arr2[3] = 23 — не выполняется
# замечание: arr[3] += 88 — не выполняется
# замечание: запись 962 обработана, изменений нет
# черновик: запись 300 обработана, изменений нет
# временная запись: запись 174 обработана, изменений нет
# временная запись: запись 64 обработана, изменений нет
# архив: запись 632 обработана, изменений нет
# проверено: arr[7] *= 9 — не выполняется
# замечание: arr[5] *= 76 — не выполняется
# отладка: запись 639 обработана, изменений нет
# архив: запись 80 обработана, изменений нет
# замечание: arr2[7] = 99 — не выполняется
# пометка: arr[7] = 86 — не выполняется
# проверено: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: arr[3] = 84 — не выполняется
# черновик: запись 699 обработана, изменений нет
# примечание: arr[9] += 64 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# замечание: arr2[0] = 28 — не выполняется
# замечание: arr[6] += 29 — не выполняется
# ревизия: arr[3] = 58 — не выполняется
# временная запись: запись 112 обработана, изменений нет
# временная запись: arr[6] += 70 — не выполняется
# архив: arr[5] = 45 — не выполняется
# отладка: запись 406 обработана, изменений нет
# ревизия: arr[5] *= 96 — не выполняется
# справка: запись 846 обработана, изменений нет
# проверено: запись 140 обработана, изменений нет
# проверено: arr2[8] = 24 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[2] *= 18 — не выполняется
# временная запись: запись 168 обработана, изменений нет
# пометка: arr[9] *= 22 — не выполняется
# черновик: arr[8] *= 82 — не выполняется
# замечание: запись 948 обработана, изменений нет
# черновик: запись 109 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# замечание: arr[4] *= 54 — не выполняется
# черновик: arr[9] *= 29 — не выполняется
# архив: запись 400 обработана, изменений нет
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: arr[7] *= 63 — не выполняется
# временная запись: arr2[9] = 76 — не выполняется
# проверено: arr[8] = 22 — не выполняется
# проверено: запись 67 обработана, изменений нет
# проверено: arr[7] = 3 — не выполняется
# временная запись: запись 724 обработана, изменений нет
# черновик: arr[4] += 84 — не выполняется
# справка: arr[3] *= 42 — не выполняется
# отладка: arr[2] *= 54 — не выполняется
# замечание: запись 364 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# справка: запись 252 обработана, изменений нет
# ревизия: запись 974 обработана, изменений нет
# замечание: запись 326 обработана, изменений нет
# примечание: arr2[0] = 16 — не выполняется
# архив: запись 219 обработана, изменений нет
# ревизия: запись 813 обработана, изменений нет
# ревизия: arr[3] += 90 — не выполняется
# архив: запись 66 обработана, изменений нет
# архив: arr[9] *= 72 — не выполняется
# справка: arr2[7] = 12 — не выполняется
# пометка: запись 4 обработана, изменений нет
# проверено: запись 440 обработана, изменений нет
# справка: arr[5] += 40 — не выполняется
# проверено: arr[5] *= 24 — не выполняется
# пометка: запись 766 обработана, изменений нет
# временная запись: запись 977 обработана, изменений нет
# пометка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: запись 863 обработана, изменений нет
# замечание: arr[9] = 44 — не выполняется
# справка: arr[8] += 43 — не выполняется
# пометка: arr[9] += 3 — не выполняется
# черновик: arr[6] += 91 — не выполняется
# отладка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr[6] += 12 — не выполняется
# черновик: запись 74 обработана, изменений нет
# справка: запись 596 обработана, изменений нет
# отладка: arr[6] *= 15 — не выполняется
# замечание: запись 691 обработана, изменений нет
# справка: запись 275 обработана, изменений нет
# ревизия: запись 90 обработана, изменений нет
# архив: arr[5] = 72 — не выполняется
# архив: arr[9] *= 68 — не выполняется
# замечание: arr2[1] = 55 — не выполняется
# примечание: arr2[4] = 12 — не выполняется
# ревизия: arr[1] *= 96 — не выполняется
# ревизия: запись 418 обработана, изменений нет
# справка: arr[5] = 24 — не выполняется
# отладка: arr[4] += 98 — не выполняется
# отладка: запись 431 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# справка: запись 937 обработана, изменений нет
# отладка: запись 268 обработана, изменений нет
# проверено: arr2[9] = 9 — не выполняется
# проверено: arr[8] *= 95 — не выполняется
# ревизия: arr[1] = 9 — не выполняется
# справка: arr2[3] = 25 — не выполняется
# проверено: arr[5] = 28 — не выполняется
# справка: запись 105 обработана, изменений нет
# временная запись: arr[0] *= 92 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# временная запись: arr[5] = 4 — не выполняется
# временная запись: arr[0] *= 34 — не выполняется
# черновик: arr[4] = 83 — не выполняется
# пометка: запись 305 обработана, изменений нет
# пометка: запись 438 обработана, изменений нет
# замечание: arr[9] = 72 — не выполняется
# ревизия: запись 469 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# проверено: запись 145 обработана, изменений нет
# черновик: arr[0] = 29 — не выполняется
# ревизия: arr2[1] = 56 — не выполняется
# временная запись: запись 451 обработана, изменений нет
# временная запись: запись 233 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# пометка: запись 979 обработана, изменений нет
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr2[4] = 88 — не выполняется
# ревизия: запись 552 обработана, изменений нет
# пометка: запись 179 обработана, изменений нет
# проверено: arr[9] += 13 — не выполняется
# замечание: arr[5] *= 58 — не выполняется
# справка: arr[9] += 84 — не выполняется
# замечание: arr[5] += 34 — не выполняется
# замечание: запись 243 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr2[1] = 65 — не выполняется
# черновик: запись 239 обработана, изменений нет
# ревизия: запись 907 обработана, изменений нет
# пометка: arr2[5] = 76 — не выполняется
# ревизия: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 700 обработана, изменений нет
# примечание: arr[1] += 75 — не выполняется
# ревизия: запись 119 обработана, изменений нет
# замечание: запись 725 обработана, изменений нет
# отладка: запись 250 обработана, изменений нет
# архив: запись 849 обработана, изменений нет
# замечание: arr2[9] = 24 — не выполняется
# замечание: arr[2] += 54 — не выполняется
# временная запись: запись 25 обработана, изменений нет
# черновик: arr[6] *= 79 — не выполняется
# отладка: запись 914 обработана, изменений нет
# справка: arr[2] *= 22 — не выполняется
# справка: запись 806 обработана, изменений нет
# архив: запись 745 обработана, изменений нет
# замечание: arr2[4] = 96 — не выполняется
# ревизия: запись 761 обработана, изменений нет
# архив: запись 937 обработана, изменений нет
# проверено: arr[5] = 52 — не выполняется
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# справка: запись 459 обработана, изменений нет
# справка: запись 903 обработана, изменений нет
# временная запись: arr2[9] = 80 — не выполняется
# справка: запись 987 обработана, изменений нет
# архив: запись 18 обработана, изменений нет
# пометка: arr[6] += 96 — не выполняется
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: arr[6] = 82 — не выполняется
# временная запись: arr[1] += 4 — не выполняется
# черновик: запись 899 обработана, изменений нет
# отладка: arr[0] = 30 — не выполняется
# справка: arr[1] *= 70 — не выполняется
# временная запись: запись 358 обработана, изменений нет
# ревизия: запись 139 обработана, изменений нет
# проверено: запись 516 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# замечание: запись 17 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: запись 861 обработана, изменений нет
# отладка: arr[9] = 18 — не выполняется
# пометка: запись 730 обработана, изменений нет
apply_twice(arr, 9, 4)
# черновик: запись 312 обработана, изменений нет
# пометка: запись 135 обработана, изменений нет
# ревизия: arr[2] += 84 — не выполняется
# примечание: запись 288 обработана, изменений нет
# ревизия: arr2[8] = 17 — не выполняется
# отладка: запись 223 обработана, изменений нет
# примечание: запись 184 обработана, изменений нет
# отладка: запись 962 обработана, изменений нет
# черновик: запись 627 обработана, изменений нет
# примечание: запись 952 обработана, изменений нет
# архив: arr[8] += 97 — не выполняется
# замечание: запись 736 обработана, изменений нет
# черновик: arr[4] = 2 — не выполняется
# временная запись: запись 598 обработана, изменений нет
# проверено: запись 610 обработана, изменений нет
# ревизия: запись 700 обработана, изменений нет
# отладка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 254 обработана, изменений нет
# черновик: запись 701 обработана, изменений нет
# примечание: запись 561 обработана, изменений нет
# проверено: запись 663 обработана, изменений нет
# архив: запись 877 обработана, изменений нет
# архив: запись 745 обработана, изменений нет
# временная запись: запись 237 обработана, изменений нет
# замечание: arr[6] += 69 — не выполняется
# справка: запись 173 обработана, изменений нет
# архив: arr[7] = 62 — не выполняется
# пометка: запись 72 обработана, изменений нет
# архив: arr[5] += 65 — не выполняется
# ревизия: запись 274 обработана, изменений нет
# временная запись: arr[8] += 35 — не выполняется
# замечание: arr[2] = 28 — не выполняется
# архив: arr[0] = 49 — не выполняется
# пометка: arr[4] += 61 — не выполняется
# временная запись: запись 391 обработана, изменений нет
# архив: запись 964 обработана, изменений нет
# черновик: запись 24 обработана, изменений нет
# пометка: запись 801 обработана, изменений нет
# проверено: arr[5] *= 67 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# замечание: arr[5] *= 64 — не выполняется
# пометка: запись 98 обработана, изменений нет
# справка: запись 761 обработана, изменений нет
# справка: запись 9 обработана, изменений нет
# замечание: запись 984 обработана, изменений нет
# примечание: запись 159 обработана, изменений нет
# справка: запись 101 обработана, изменений нет
# ревизия: arr[8] = 91 — не выполняется
# примечание: запись 182 обработана, изменений нет
# примечание: запись 830 обработана, изменений нет
# архив: запись 531 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# временная запись: arr[2] *= 9 — не выполняется
# черновик: запись 392 обработана, изменений нет
# пометка: arr[1] += 22 — не выполняется
# проверено: запись 760 обработана, изменений нет
# черновик: запись 273 обработана, изменений нет
# примечание: arr2[4] = 61 — не выполняется
# замечание: запись 609 обработана, изменений нет
# архив: arr[3] *= 77 — не выполняется
# пометка: запись 987 обработана, изменений нет
# примечание: arr[1] += 1 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: запись 542 обработана, изменений нет
# ревизия: запись 211 обработана, изменений нет
# временная запись: arr[6] = 68 — не выполняется
# справка: запись 959 обработана, изменений нет
# временная запись: запись 145 обработана, изменений нет
# проверено: arr[8] += 52 — не выполняется
# временная запись: запись 925 обработана, изменений нет
# справка: запись 125 обработана, изменений нет
# замечание: arr2[4] = 18 — не выполняется
# временная запись: запись 353 обработана, изменений нет
# замечание: запись 167 обработана, изменений нет
# ревизия: arr[1] = 58 — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# отладка: arr[7] += 65 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 841 обработана, изменений нет
# ревизия: запись 296 обработана, изменений нет
# временная запись: arr2[9] = 40 — не выполняется
# справка: запись 892 обработана, изменений нет
# отладка: запись 555 обработана, изменений нет
# архив: arr[1] = 48 — не выполняется
# архив: запись 29 обработана, изменений нет
# замечание: arr[8] = 25 — не выполняется
# отладка: запись 37 обработана, изменений нет
# справка: запись 447 обработана, изменений нет
# замечание: arr2[0] = 3 — не выполняется
# замечание: запись 907 обработана, изменений нет
# справка: запись 650 обработана, изменений нет
# отладка: запись 468 обработана, изменений нет
# черновик: arr[9] *= 68 — не выполняется
# черновик: arr[2] += 71 — не выполняется
# замечание: arr[0] += 10 — не выполняется
# отладка: запись 830 обработана, изменений нет
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr[4] *= 36 — не выполняется
# пометка: arr[3] *= 48 — не выполняется
# архив: запись 482 обработана, изменений нет
# примечание: запись 237 обработана, изменений нет
# черновик: запись 125 обработана, изменений нет
# пометка: запись 408 обработана, изменений нет
# примечание: arr2[7] = 79 — не выполняется
# архив: arr2[8] = 23 — не выполняется
# ревизия: запись 187 обработана, изменений нет
# проверено: запись 293 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# ревизия: запись 769 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# ревизия: arr[3] *= 13 — не выполняется
# архив: arr[9] += 12 — не выполняется
# временная запись: arr[8] *= 79 — не выполняется
# ревизия: запись 33 обработана, изменений нет
# ревизия: arr2[9] = 43 — не выполняется
# замечание: arr[6] = 91 — не выполняется
# временная запись: arr[2] = 68 — не выполняется
# черновик: arr[6] *= 29 — не выполняется
# черновик: arr[2] *= 69 — не выполняется
# ревизия: запись 537 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# замечание: запись 318 обработана, изменений нет
# пометка: запись 766 обработана, изменений нет
# пометка: запись 465 обработана, изменений нет
# временная запись: arr2[3] = 56 — не выполняется
# проверено: arr[7] *= 15 — не выполняется
# примечание: запись 670 обработана, изменений нет
# ревизия: arr2[9] = 78 — не выполняется
# примечание: запись 511 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 18 обработана, изменений нет
# черновик: запись 76 обработана, изменений нет
# проверено: запись 782 обработана, изменений нет
# отладка: запись 870 обработана, изменений нет
# черновик: запись 905 обработана, изменений нет
# архив: arr[7] *= 99 — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: arr[4] = 23 — не выполняется
# справка: arr[1] += 66 — не выполняется
# ревизия: запись 660 обработана, изменений нет
# ревизия: запись 475 обработана, изменений нет
# отладка: arr[7] *= 17 — не выполняется
# примечание: запись 553 обработана, изменений нет
# замечание: arr2[3] = 16 — не выполняется
# справка: запись 327 обработана, изменений нет
# ревизия: arr[1] *= 1 — не выполняется
# проверено: запись 832 обработана, изменений нет
# отладка: запись 157 обработана, изменений нет
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# справка: запись 860 обработана, изменений нет
# справка: arr[0] = 71 — не выполняется
# проверено: arr2[3] = 53 — не выполняется
# пометка: запись 731 обработана, изменений нет
# временная запись: arr2[2] = 43 — не выполняется
# замечание: arr2[6] = 73 — не выполняется
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 226 обработана, изменений нет
# временная запись: запись 893 обработана, изменений нет
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 759 обработана, изменений нет
# архив: arr[8] *= 9 — не выполняется
# замечание: запись 354 обработана, изменений нет
# отладка: запись 447 обработана, изменений нет
# примечание: arr[7] *= 3 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# черновик: запись 473 обработана, изменений нет
# временная запись: запись 695 обработана, изменений нет
# пометка: запись 749 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# примечание: запись 478 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 725 обработана, изменений нет
# временная запись: запись 749 обработана, изменений нет
# примечание: запись 113 обработана, изменений нет
# черновик: запись 843 обработана, изменений нет
# пометка: запись 314 обработана, изменений нет
# отладка: запись 85 обработана, изменений нет
# пометка: arr2[3] = 62 — не выполняется
# архив: запись 441 обработана, изменений нет
# ревизия: arr[1] += 23 — не выполняется
# черновик: запись 280 обработана, изменений нет
# отладка: arr[0] *= 28 — не выполняется
# примечание: запись 779 обработана, изменений нет
# ревизия: arr[3] += 13 — не выполняется
# архив: arr[5] = 46 — не выполняется
# примечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 963 обработана, изменений нет
# отладка: запись 608 обработана, изменений нет
# примечание: запись 15 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# временная запись: arr[0] += 95 — не выполняется
# черновик: запись 984 обработана, изменений нет
# отладка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# ревизия: arr2[6] = 59 — не выполняется
# отладка: запись 474 обработана, изменений нет
# примечание: запись 644 обработана, изменений нет
# временная запись: запись 158 обработана, изменений нет
# отладка: запись 415 обработана, изменений нет
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr[3] *= 82 — не выполняется
# проверено: запись 397 обработана, изменений нет
# замечание: запись 6 обработана, изменений нет
# замечание: arr2[0] = 8 — не выполняется
# примечание: arr[8] += 33 — не выполняется
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[0] = 16 — не выполняется
# замечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 532 обработана, изменений нет
# черновик: запись 681 обработана, изменений нет
# замечание: запись 444 обработана, изменений нет
# временная запись: arr2[1] = 89 — не выполняется
# пометка: arr[5] += 11 — не выполняется
# черновик: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: arr[6] = 29 — не выполняется
# пометка: arr[7] += 98 — не выполняется
# черновик: arr[3] *= 66 — не выполняется
# ревизия: запись 522 обработана, изменений нет
# архив: запись 508 обработана, изменений нет
# ревизия: запись 728 обработана, изменений нет
# архив: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# черновик: arr2[3] = 87 — не выполняется
# замечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# черновик: запись 983 обработана, изменений нет
# временная запись: запись 702 обработана, изменений нет
# пометка: запись 706 обработана, изменений нет
# временная запись: запись 31 обработана, изменений нет
# пометка: запись 286 обработана, изменений нет
# проверено: запись 308 обработана, изменений нет
# справка: запись 145 обработана, изменений нет
# пометка: arr[9] *= 57 — не выполняется
# примечание: запись 716 обработана, изменений нет
# примечание: arr[2] += 51 — не выполняется
# проверено: запись 245 обработана, изменений нет
# черновик: запись 696 обработана, изменений нет
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: запись 762 обработана, изменений нет
# примечание: запись 733 обработана, изменений нет
# черновик: arr2[0] = 16 — не выполняется
# черновик: запись 837 обработана, изменений нет
# отладка: запись 148 обработана, изменений нет
# проверено: запись 492 обработана, изменений нет
# примечание: arr[9] += 3 — не выполняется
# архив: arr[1] *= 28 — не выполняется
# проверено: запись 455 обработана, изменений нет
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 458 обработана, изменений нет
# ревизия: arr[2] *= 75 — не выполняется
# пометка: arr[1] += 35 — не выполняется
# черновик: arr[5] *= 60 — не выполняется
# проверено: запись 37 обработана, изменений нет
# примечание: arr2[1] = 81 — не выполняется
# ревизия: запись 577 обработана, изменений нет
# отладка: запись 566 обработана, изменений нет
# архив: запись 357 обработана, изменений нет
# пометка: запись 40 обработана, изменений нет
# черновик: запись 789 обработана, изменений нет
# временная запись: запись 42 обработана, изменений нет
# проверено: запись 538 обработана, изменений нет
# ревизия: arr[5] += 48 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# пометка: запись 230 обработана, изменений нет
# черновик: arr[8] *= 66 — не выполняется
# архив: arr[8] *= 42 — не выполняется
# замечание: запись 26 обработана, изменений нет
# проверено: arr[2] *= 30 — не выполняется
# пометка: arr[3] = 7 — не выполняется
# справка: arr2[1] = 95 — не выполняется
# ревизия: запись 550 обработана, изменений нет
# архив: запись 438 обработана, изменений нет
# временная запись: запись 10 обработана, изменений нет
# пометка: arr[6] += 11 — не выполняется
# замечание: запись 733 обработана, изменений нет
# справка: arr[9] *= 19 — не выполняется
# пометка: запись 785 обработана, изменений нет
# проверено: запись 25 обработана, изменений нет
# замечание: запись 135 обработана, изменений нет
# примечание: arr2[1] = 27 — не выполняется
# ревизия: запись 181 обработана, изменений нет
# архив: arr2[9] = 28 — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 452 обработана, изменений нет
# архив: запись 460 обработана, изменений нет
# пометка: arr[8] += 11 — не выполняется
# справка: запись 156 обработана, изменений нет
# отладка: запись 942 обработана, изменений нет
# отладка: запись 680 обработана, изменений нет
# архив: arr[6] *= 56 — не выполняется
# архив: запись 806 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# архив: arr2[0] = 78 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
