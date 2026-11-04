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
arr2[7] = 20
arr[2] *= 21
arr[2] *= 17
arr[5] = 21
arr[1] += 25
arr[3] += 8
arr2[2] = 20
arr[7] += 13
"""

TRAP_0 = "arr[3] = 945"
TRAP_1 = "arr[9] = 806"
TRAP_2 = "arr[0] = 270"
TRAP_3 = "arr[1] = 758"
TRAP_4 = "arr[9] = 276"
TRAP_5 = "arr[3] = 567"
TRAP_6 = "arr[2] = 302"
TRAP_7 = "arr[3] = 852"
TRAP_8 = "arr[3] = 813"
TRAP_9 = "arr[7] = 792"
TRAP_10 = "arr[1] = 905"
TRAP_11 = "arr[3] = 628"
TRAP_12 = "arr[4] = 895"
TRAP_13 = "arr[1] = 884"
TRAP_14 = "arr[9] = 618"
TRAP_15 = "arr[9] = 670"
TRAP_16 = "arr[5] = 529"
TRAP_17 = "arr[6] = 898"
TRAP_18 = "arr[0] = 469"
TRAP_19 = "arr[9] = 222"
TRAP_20 = "arr[1] = 975"
TRAP_21 = "arr[1] = 404"
TRAP_22 = "arr[0] = 441"
TRAP_23 = "arr[3] = 334"
TRAP_24 = "arr[7] = 395"
TRAP_25 = "arr[2] = 824"
TRAP_26 = "arr[3] = 948"
TRAP_27 = "arr[1] = 292"
TRAP_28 = "arr[5] = 895"
TRAP_29 = "arr[3] = 307"
TRAP_30 = "arr[3] = 941"
TRAP_31 = "arr[9] = 261"
TRAP_32 = "arr[1] = 528"
TRAP_33 = "arr[7] = 239"
TRAP_34 = "arr[7] = 688"
TRAP_35 = "arr[7] = 613"
TRAP_36 = "arr[0] = 294"
TRAP_37 = "arr[9] = 667"
TRAP_38 = "arr[4] = 706"
TRAP_39 = "arr[4] = 832"
TRAP_40 = "arr[3] = 546"
TRAP_41 = "arr[4] = 891"
TRAP_42 = "arr[8] = 639"
TRAP_43 = "arr[8] = 631"
TRAP_44 = "arr[7] = 686"
TRAP_45 = "arr[8] = 607"
TRAP_46 = "arr[2] = 765"
TRAP_47 = "arr[0] = 393"
TRAP_48 = "arr[3] = 461"
TRAP_49 = "arr[8] = 916"
TRAP_50 = "arr[3] = 326"
TRAP_51 = "arr[2] = 442"
TRAP_52 = "arr[9] = 946"
TRAP_53 = "arr[9] = 442"
TRAP_54 = "arr[5] = 808"
TRAP_55 = "arr[7] = 535"
TRAP_56 = "arr[7] = 792"
TRAP_57 = "arr[5] = 200"
TRAP_58 = "arr[2] = 250"
TRAP_59 = "arr[5] = 660"
TRAP_60 = "arr[5] = 279"
TRAP_61 = "arr[7] = 124"
TRAP_62 = "arr[7] = 500"
TRAP_63 = "arr[4] = 536"
TRAP_64 = "arr[6] = 187"
TRAP_65 = "arr[9] = 127"
TRAP_66 = "arr[8] = 718"
TRAP_67 = "arr[0] = 452"
TRAP_68 = "arr[2] = 103"
TRAP_69 = "arr[4] = 390"
TRAP_70 = "arr[0] = 432"
TRAP_71 = "arr[9] = 568"
TRAP_72 = "arr[5] = 781"
TRAP_73 = "arr[1] = 480"
TRAP_74 = "arr[9] = 419"
TRAP_75 = "arr[9] = 744"
TRAP_76 = "arr[6] = 950"
TRAP_77 = "arr[4] = 468"
TRAP_78 = "arr[0] = 178"
TRAP_79 = "arr[9] = 668"
TRAP_80 = "arr[8] = 117"
TRAP_81 = "arr[5] = 231"
TRAP_82 = "arr[7] = 555"
TRAP_83 = "arr[5] = 296"
TRAP_84 = "arr[5] = 217"
TRAP_85 = "arr[1] = 988"
TRAP_86 = "arr[4] = 327"
TRAP_87 = "arr[9] = 523"
TRAP_88 = "arr[3] = 342"
TRAP_89 = "arr[3] = 804"
TRAP_90 = "arr[0] = 732"
TRAP_91 = "arr[4] = 728"
TRAP_92 = "arr[3] = 230"
TRAP_93 = "arr[4] = 967"
TRAP_94 = "arr[7] = 800"
TRAP_95 = "arr[7] = 912"
TRAP_96 = "arr[6] = 843"
TRAP_97 = "arr[6] = 211"
TRAP_98 = "arr[1] = 470"
TRAP_99 = "arr[8] = 659"
TRAP_100 = "arr[0] = 380"
TRAP_101 = "arr[8] = 505"
TRAP_102 = "arr[1] = 871"
TRAP_103 = "arr[3] = 680"
TRAP_104 = "arr[7] = 300"
TRAP_105 = "arr[3] = 942"
TRAP_106 = "arr[9] = 859"
TRAP_107 = "arr[8] = 502"
TRAP_108 = "arr[6] = 413"
TRAP_109 = "arr[2] = 196"
TRAP_110 = "arr[9] = 897"
TRAP_111 = "arr[9] = 890"
TRAP_112 = "arr[1] = 625"
TRAP_113 = "arr[6] = 892"
TRAP_114 = "arr[1] = 413"
TRAP_115 = "arr[9] = 626"
TRAP_116 = "arr[9] = 515"
TRAP_117 = "arr[7] = 817"
TRAP_118 = "arr[6] = 869"
TRAP_119 = "arr[1] = 837"
TRAP_120 = "arr[8] = 489"
TRAP_121 = "arr[8] = 718"
TRAP_122 = "arr[9] = 754"
TRAP_123 = "arr[3] = 791"
TRAP_124 = "arr[8] = 932"
TRAP_125 = "arr[9] = 202"
TRAP_126 = "arr[6] = 803"
TRAP_127 = "arr[8] = 461"
TRAP_128 = "arr[1] = 463"
TRAP_129 = "arr[6] = 271"
TRAP_130 = "arr[0] = 889"
TRAP_131 = "arr[4] = 974"
TRAP_132 = "arr[8] = 184"
TRAP_133 = "arr[5] = 349"
TRAP_134 = "arr[4] = 555"
TRAP_135 = "arr[2] = 799"
TRAP_136 = "arr[7] = 698"
TRAP_137 = "arr[1] = 420"
TRAP_138 = "arr[1] = 560"
TRAP_139 = "arr[1] = 272"
TRAP_140 = "arr[5] = 638"
TRAP_141 = "arr[0] = 857"
TRAP_142 = "arr[7] = 117"
TRAP_143 = "arr[8] = 817"
TRAP_144 = "arr[7] = 190"
TRAP_145 = "arr[9] = 485"
TRAP_146 = "arr[2] = 139"
TRAP_147 = "arr[2] = 859"
TRAP_148 = "arr[9] = 503"
TRAP_149 = "arr[5] = 366"

arr = [21, 5, 22, 13, 2, 24, 5, 11, 8, 7]

note_0 = str(arr[8]) + str(arr[6])
code_1 = re.sub(r'[0-9]', '#', str(arr[4]))
note_2 = str(arr[9]) + str(arr[8])
tmp_3 = arr[0] + 16
copy_4 = arr[7]
note_5 = str(arr[0]) + str(arr[7])
code_6 = re.sub(r'[0-9]', '#', str(arr[0]))
code_7 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_8 = arr[4] + 37
copy_9 = arr[5]
code_10 = re.sub(r'[0-9]', '#', str(arr[4]))
code_11 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_12 = arr[4]
label_13 = "запись 13 не применялась"
tmp_14 = arr[8] + 7
code_15 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_16 = arr[9]
tmp_17 = arr[8] + 48
note_18 = str(arr[2]) + str(arr[2])
note_19 = str(arr[4]) + str(arr[9])
tmp_20 = arr[6] + 48
tmp_21 = arr[0] + 25
label_22 = "запись 22 не применялась"
tmp_23 = arr[5] + 2
note_24 = str(arr[8]) + str(arr[8])
label_25 = "запись 25 не применялась"
tmp_26 = arr[8] + 41
tmp_27 = arr[4] + 20
copy_28 = arr[5]
tmp_29 = arr[7] + 44
copy_30 = arr[8]
copy_31 = arr[9]
code_32 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_33 = arr[7] + 19
note_34 = str(arr[7]) + str(arr[2])
code_35 = re.sub(r'[0-9]', '#', str(arr[4]))
note_36 = str(arr[2]) + str(arr[3])
copy_37 = arr[8]
copy_38 = arr[6]
tmp_39 = arr[4] + 2
label_40 = "запись 40 не применялась"
note_41 = str(arr[0]) + str(arr[1])
note_42 = str(arr[9]) + str(arr[1])
code_43 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_44 = arr[3]
tmp_45 = arr[9] + 45
code_46 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_47 = arr[5]
tmp_48 = arr[2] + 7
tmp_49 = arr[1] + 48
code_50 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_51 = arr[2] + 40
note_52 = str(arr[7]) + str(arr[4])
code_53 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_54 = arr[6] + 16
label_55 = "запись 55 не применялась"
label_56 = "запись 56 не применялась"
copy_57 = arr[2]
note_58 = str(arr[9]) + str(arr[0])
copy_59 = arr[0]
copy_60 = arr[1]
note_61 = str(arr[9]) + str(arr[6])
code_62 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_63 = arr[4]
label_64 = "запись 64 не применялась"
note_65 = str(arr[2]) + str(arr[9])
tmp_66 = arr[4] + 9
label_67 = "запись 67 не применялась"
note_68 = str(arr[3]) + str(arr[7])
note_69 = str(arr[9]) + str(arr[5])
note_70 = str(arr[5]) + str(arr[3])
code_71 = re.sub(r'[0-9]', '#', str(arr[0]))
note_72 = str(arr[9]) + str(arr[8])
tmp_73 = arr[4] + 11
note_74 = str(arr[2]) + str(arr[1])
copy_75 = arr[7]
label_76 = "запись 76 не применялась"
code_77 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_78 = arr[9] + 14
note_79 = str(arr[6]) + str(arr[4])
code_80 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_81 = arr[9] + 4
copy_82 = arr[5]
note_83 = str(arr[1]) + str(arr[9])
copy_84 = arr[4]
copy_85 = arr[9]
note_86 = str(arr[4]) + str(arr[9])
note_87 = str(arr[6]) + str(arr[3])
tmp_88 = arr[1] + 27
tmp_89 = arr[3] + 8
note_90 = str(arr[6]) + str(arr[4])
note_91 = str(arr[9]) + str(arr[0])
tmp_92 = arr[0] + 15
note_93 = str(arr[1]) + str(arr[5])
code_94 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_95 = arr[1] + 16
code_96 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_97 = arr[0] + 42
label_98 = "запись 98 не применялась"
tmp_99 = arr[7] + 19
code_100 = re.sub(r'[0-9]', '#', str(arr[2]))
code_101 = re.sub(r'[0-9]', '#', str(arr[5]))
note_102 = str(arr[6]) + str(arr[6])
label_103 = "запись 103 не применялась"
tmp_104 = arr[3] + 47
note_105 = str(arr[1]) + str(arr[0])
code_106 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_107 = arr[8]
code_108 = re.sub(r'[0-9]', '#', str(arr[6]))
label_109 = "запись 109 не применялась"
note_110 = str(arr[5]) + str(arr[8])
copy_111 = arr[8]
note_112 = str(arr[6]) + str(arr[4])
tmp_113 = arr[6] + 9
copy_114 = arr[6]
copy_115 = arr[5]
code_116 = re.sub(r'[0-9]', '#', str(arr[7]))
note_117 = str(arr[6]) + str(arr[7])
tmp_118 = arr[7] + 31
code_119 = re.sub(r'[0-9]', '#', str(arr[1]))
note_120 = str(arr[6]) + str(arr[8])
tmp_121 = arr[9] + 38
copy_122 = arr[1]
tmp_123 = arr[8] + 40
note_124 = str(arr[9]) + str(arr[1])
note_125 = str(arr[7]) + str(arr[5])
note_126 = str(arr[2]) + str(arr[7])
label_127 = "запись 127 не применялась"
copy_128 = arr[8]
code_129 = re.sub(r'[0-9]', '#', str(arr[8]))
note_130 = str(arr[9]) + str(arr[1])
code_131 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_132 = arr[2] + 31
tmp_133 = arr[4] + 23
tmp_134 = arr[9] + 8
note_135 = str(arr[6]) + str(arr[9])
note_136 = str(arr[9]) + str(arr[9])
note_137 = str(arr[0]) + str(arr[0])
copy_138 = arr[4]
copy_139 = arr[6]
note_140 = str(arr[7]) + str(arr[1])
label_141 = "запись 141 не применялась"
tmp_142 = arr[6] + 25
note_143 = str(arr[8]) + str(arr[5])
tmp_144 = arr[4] + 28
tmp_145 = arr[4] + 11
code_146 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_147 = arr[6] + 5
tmp_148 = arr[2] + 15
tmp_149 = arr[3] + 1
code_150 = re.sub(r'[0-9]', '#', str(arr[0]))
note_151 = str(arr[1]) + str(arr[9])
tmp_152 = arr[4] + 37
label_153 = "запись 153 не применялась"
code_154 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_155 = arr[3]
label_156 = "запись 156 не применялась"
tmp_157 = arr[4] + 9
copy_158 = arr[0]
code_159 = re.sub(r'[0-9]', '#', str(arr[8]))
note_160 = str(arr[7]) + str(arr[0])
copy_161 = arr[9]
copy_162 = arr[1]
note_163 = str(arr[1]) + str(arr[0])
copy_164 = arr[2]
tmp_165 = arr[3] + 13
tmp_166 = arr[6] + 12
tmp_167 = arr[1] + 42
note_168 = str(arr[4]) + str(arr[6])
note_169 = str(arr[7]) + str(arr[3])
note_170 = str(arr[0]) + str(arr[6])
tmp_171 = arr[9] + 47
code_172 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_173 = arr[0] + 30
code_174 = re.sub(r'[0-9]', '#', str(arr[7]))
note_175 = str(arr[1]) + str(arr[1])
note_176 = str(arr[6]) + str(arr[4])
code_177 = re.sub(r'[0-9]', '#', str(arr[2]))
code_178 = re.sub(r'[0-9]', '#', str(arr[5]))
code_179 = re.sub(r'[0-9]', '#', str(arr[5]))
note_180 = str(arr[9]) + str(arr[8])
code_181 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_182 = arr[1] + 48
note_183 = str(arr[5]) + str(arr[5])
copy_184 = arr[4]
code_185 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_186 = arr[4]
copy_187 = arr[1]
tmp_188 = arr[9] + 2
note_189 = str(arr[2]) + str(arr[2])
code_190 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_191 = arr[9] + 22
tmp_192 = arr[7] + 34
tmp_193 = arr[2] + 28
tmp_194 = arr[9] + 2
label_195 = "запись 195 не применялась"
label_196 = "запись 196 не применялась"
note_197 = str(arr[7]) + str(arr[3])
label_198 = "запись 198 не применялась"
tmp_199 = arr[7] + 38
note_200 = str(arr[6]) + str(arr[2])
tmp_201 = arr[4] + 26
note_202 = str(arr[5]) + str(arr[2])
code_203 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_204 = arr[6] + 21
code_205 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_206 = arr[8] + 2
note_207 = str(arr[3]) + str(arr[9])
note_208 = str(arr[3]) + str(arr[2])
tmp_209 = arr[1] + 32
label_210 = "запись 210 не применялась"
copy_211 = arr[2]
tmp_212 = arr[7] + 8
tmp_213 = arr[9] + 37
note_214 = str(arr[2]) + str(arr[1])
code_215 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_216 = arr[5] + 49
tmp_217 = arr[9] + 47
code_218 = re.sub(r'[0-9]', '#', str(arr[6]))
note_219 = str(arr[8]) + str(arr[9])
note_220 = str(arr[8]) + str(arr[3])
tmp_221 = arr[4] + 31
note_222 = str(arr[9]) + str(arr[9])
tmp_223 = arr[9] + 22
copy_224 = arr[9]
tmp_225 = arr[0] + 2
note_226 = str(arr[4]) + str(arr[1])
code_227 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_228 = arr[8]
label_229 = "запись 229 не применялась"
tmp_230 = arr[3] + 39
note_231 = str(arr[6]) + str(arr[6])
tmp_232 = arr[1] + 2
note_233 = str(arr[2]) + str(arr[9])
note_234 = str(arr[4]) + str(arr[5])
copy_235 = arr[6]
note_236 = str(arr[6]) + str(arr[5])
copy_237 = arr[5]
tmp_238 = arr[5] + 7
note_239 = str(arr[2]) + str(arr[0])
tmp_240 = arr[2] + 41
code_241 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_242 = arr[8] + 11
label_243 = "запись 243 не применялась"
code_244 = re.sub(r'[0-9]', '#', str(arr[2]))
code_245 = re.sub(r'[0-9]', '#', str(arr[6]))
code_246 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_247 = arr[6]
copy_248 = arr[3]
code_249 = re.sub(r'[0-9]', '#', str(arr[4]))
code_250 = re.sub(r'[0-9]', '#', str(arr[1]))
note_251 = str(arr[8]) + str(arr[5])
code_252 = re.sub(r'[0-9]', '#', str(arr[4]))
note_253 = str(arr[3]) + str(arr[8])
label_254 = "запись 254 не применялась"
tmp_255 = arr[7] + 15
tmp_256 = arr[2] + 34
tmp_257 = arr[8] + 34
code_258 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_259 = arr[1] + 47
code_260 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_261 = arr[4] + 15
copy_262 = arr[7]
tmp_263 = arr[9] + 1
tmp_264 = arr[0] + 34
code_265 = re.sub(r'[0-9]', '#', str(arr[3]))
note_266 = str(arr[2]) + str(arr[0])
tmp_267 = arr[4] + 24
tmp_268 = arr[7] + 26
label_269 = "запись 269 не применялась"
code_270 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_271 = arr[1] + 12
tmp_272 = arr[7] + 46
copy_273 = arr[8]
note_274 = str(arr[2]) + str(arr[8])
copy_275 = arr[8]
copy_276 = arr[2]
label_277 = "запись 277 не применялась"
note_278 = str(arr[7]) + str(arr[0])
note_279 = str(arr[0]) + str(arr[7])
label_280 = "запись 280 не применялась"
copy_281 = arr[1]
tmp_282 = arr[0] + 27
code_283 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_284 = arr[3] + 16
label_285 = "запись 285 не применялась"
code_286 = re.sub(r'[0-9]', '#', str(arr[2]))
note_287 = str(arr[9]) + str(arr[1])
tmp_288 = arr[1] + 13
tmp_289 = arr[9] + 6
tmp_290 = arr[8] + 27
note_291 = str(arr[8]) + str(arr[3])
code_292 = re.sub(r'[0-9]', '#', str(arr[7]))
note_293 = str(arr[2]) + str(arr[8])
label_294 = "запись 294 не применялась"
code_295 = re.sub(r'[0-9]', '#', str(arr[3]))
code_296 = re.sub(r'[0-9]', '#', str(arr[6]))
note_297 = str(arr[7]) + str(arr[0])
tmp_298 = arr[6] + 28
note_299 = str(arr[2]) + str(arr[8])
note_300 = str(arr[9]) + str(arr[1])
note_301 = str(arr[7]) + str(arr[2])
copy_302 = arr[9]
note_303 = str(arr[9]) + str(arr[4])
tmp_304 = arr[3] + 7
label_305 = "запись 305 не применялась"
code_306 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_307 = arr[2]
label_308 = "запись 308 не применялась"
note_309 = str(arr[3]) + str(arr[8])
note_310 = str(arr[6]) + str(arr[8])
tmp_311 = arr[4] + 28
label_312 = "запись 312 не применялась"
code_313 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_314 = arr[7]
note_315 = str(arr[4]) + str(arr[2])
code_316 = re.sub(r'[0-9]', '#', str(arr[2]))
code_317 = re.sub(r'[0-9]', '#', str(arr[8]))
note_318 = str(arr[8]) + str(arr[1])
note_319 = str(arr[3]) + str(arr[9])
note_320 = str(arr[0]) + str(arr[1])
label_321 = "запись 321 не применялась"
tmp_322 = arr[8] + 1
note_323 = str(arr[3]) + str(arr[8])
tmp_324 = arr[7] + 14
tmp_325 = arr[3] + 44
code_326 = re.sub(r'[0-9]', '#', str(arr[8]))
note_327 = str(arr[9]) + str(arr[4])
note_328 = str(arr[0]) + str(arr[1])
note_329 = str(arr[5]) + str(arr[3])
note_330 = str(arr[3]) + str(arr[9])
tmp_331 = arr[0] + 2
copy_332 = arr[1]
label_333 = "запись 333 не применялась"
note_334 = str(arr[9]) + str(arr[0])
note_335 = str(arr[1]) + str(arr[1])
code_336 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_337 = arr[9] + 1
tmp_338 = arr[7] + 46
tmp_339 = arr[5] + 36
tmp_340 = arr[7] + 12
copy_341 = arr[8]
label_342 = "запись 342 не применялась"
copy_343 = arr[1]
label_344 = "запись 344 не применялась"
tmp_345 = arr[7] + 40
tmp_346 = arr[9] + 30
tmp_347 = arr[8] + 45
code_348 = re.sub(r'[0-9]', '#', str(arr[1]))
code_349 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_350 = arr[6]
note_351 = str(arr[8]) + str(arr[4])
note_352 = str(arr[5]) + str(arr[7])
copy_353 = arr[8]
tmp_354 = arr[9] + 12
tmp_355 = arr[2] + 19
code_356 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_357 = arr[1] + 28
copy_358 = arr[0]
tmp_359 = arr[7] + 1
note_360 = str(arr[1]) + str(arr[9])
note_361 = str(arr[1]) + str(arr[6])
copy_362 = arr[3]
note_363 = str(arr[7]) + str(arr[3])
code_364 = re.sub(r'[0-9]', '#', str(arr[1]))
label_365 = "запись 365 не применялась"
tmp_366 = arr[5] + 37
code_367 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_368 = arr[6]
tmp_369 = arr[9] + 7
label_370 = "запись 370 не применялась"
note_371 = str(arr[5]) + str(arr[5])
code_372 = re.sub(r'[0-9]', '#', str(arr[0]))
code_373 = re.sub(r'[0-9]', '#', str(arr[7]))
code_374 = re.sub(r'[0-9]', '#', str(arr[2]))
code_375 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_376 = arr[3] + 31
note_377 = str(arr[4]) + str(arr[5])
tmp_378 = arr[7] + 32
copy_379 = arr[8]
copy_380 = arr[3]
note_381 = str(arr[2]) + str(arr[8])
tmp_382 = arr[4] + 44
tmp_383 = arr[3] + 45
tmp_384 = arr[6] + 14
note_385 = str(arr[1]) + str(arr[8])
note_386 = str(arr[3]) + str(arr[7])
label_387 = "запись 387 не применялась"
tmp_388 = arr[1] + 40
code_389 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_390 = arr[2] + 41
label_391 = "запись 391 не применялась"
copy_392 = arr[6]
tmp_393 = arr[7] + 20
copy_394 = arr[9]
code_395 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_396 = arr[4] + 6
copy_397 = arr[0]
label_398 = "запись 398 не применялась"
note_399 = str(arr[4]) + str(arr[6])
tmp_400 = arr[3] + 38
label_401 = "запись 401 не применялась"
code_402 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_403 = arr[0] + 23
note_404 = str(arr[5]) + str(arr[2])
note_405 = str(arr[3]) + str(arr[3])
copy_406 = arr[5]
code_407 = re.sub(r'[0-9]', '#', str(arr[7]))
code_408 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_409 = arr[9] + 23
code_410 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_411 = arr[0] + 19
tmp_412 = arr[8] + 3
code_413 = re.sub(r'[0-9]', '#', str(arr[8]))
note_414 = str(arr[3]) + str(arr[6])
copy_415 = arr[4]
label_416 = "запись 416 не применялась"
tmp_417 = arr[3] + 18
copy_418 = arr[1]
label_419 = "запись 419 не применялась"
label_420 = "запись 420 не применялась"
tmp_421 = arr[9] + 50
code_422 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_423 = arr[3]
note_424 = str(arr[4]) + str(arr[1])
note_425 = str(arr[9]) + str(arr[2])
label_426 = "запись 426 не применялась"
code_427 = re.sub(r'[0-9]', '#', str(arr[7]))
note_428 = str(arr[6]) + str(arr[6])
note_429 = str(arr[9]) + str(arr[2])
tmp_430 = arr[2] + 44
copy_431 = arr[9]
tmp_432 = arr[5] + 29
note_433 = str(arr[8]) + str(arr[4])
tmp_434 = arr[1] + 14
code_435 = re.sub(r'[0-9]', '#', str(arr[6]))
label_436 = "запись 436 не применялась"
code_437 = re.sub(r'[0-9]', '#', str(arr[7]))
note_438 = str(arr[5]) + str(arr[2])
copy_439 = arr[1]
copy_440 = arr[4]
copy_441 = arr[3]
note_442 = str(arr[6]) + str(arr[6])
code_443 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_444 = arr[3]
tmp_445 = arr[8] + 42
note_446 = str(arr[0]) + str(arr[1])
note_447 = str(arr[8]) + str(arr[6])
note_448 = str(arr[3]) + str(arr[5])
note_449 = str(arr[0]) + str(arr[1])
note_450 = str(arr[6]) + str(arr[0])
note_451 = str(arr[3]) + str(arr[9])
tmp_452 = arr[1] + 38
copy_453 = arr[2]
tmp_454 = arr[3] + 16
label_455 = "запись 455 не применялась"
tmp_456 = arr[7] + 45
tmp_457 = arr[5] + 33
copy_458 = arr[2]
tmp_459 = arr[5] + 21
tmp_460 = arr[3] + 24
note_461 = str(arr[7]) + str(arr[6])
label_462 = "запись 462 не применялась"
copy_463 = arr[6]
note_464 = str(arr[1]) + str(arr[9])
note_465 = str(arr[8]) + str(arr[2])
label_466 = "запись 466 не применялась"
code_467 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_468 = arr[0] + 2
code_469 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_470 = arr[8] + 38
tmp_471 = arr[8] + 30
tmp_472 = arr[0] + 39
note_473 = str(arr[2]) + str(arr[7])
note_474 = str(arr[2]) + str(arr[9])
note_475 = str(arr[2]) + str(arr[2])
note_476 = str(arr[7]) + str(arr[8])
tmp_477 = arr[6] + 47
code_478 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_479 = arr[8] + 7
tmp_480 = arr[5] + 2
copy_481 = arr[1]
code_482 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_483 = arr[1]
tmp_484 = arr[8] + 20
code_485 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_486 = arr[8] + 13
label_487 = "запись 487 не применялась"
code_488 = re.sub(r'[0-9]', '#', str(arr[5]))
code_489 = re.sub(r'[0-9]', '#', str(arr[0]))
label_490 = "запись 490 не применялась"
tmp_491 = arr[6] + 50
label_492 = "запись 492 не применялась"
label_493 = "запись 493 не применялась"
label_494 = "запись 494 не применялась"
label_495 = "запись 495 не применялась"
note_496 = str(arr[4]) + str(arr[2])
copy_497 = arr[2]
label_498 = "запись 498 не применялась"
note_499 = str(arr[7]) + str(arr[0])
note_500 = str(arr[7]) + str(arr[3])
tmp_501 = arr[1] + 43
tmp_502 = arr[8] + 6
note_503 = str(arr[6]) + str(arr[4])
note_504 = str(arr[7]) + str(arr[9])
label_505 = "запись 505 не применялась"
note_506 = str(arr[1]) + str(arr[8])
note_507 = str(arr[3]) + str(arr[3])
code_508 = re.sub(r'[0-9]', '#', str(arr[9]))
note_509 = str(arr[4]) + str(arr[2])
tmp_510 = arr[3] + 45
code_511 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_512 = arr[2] + 16
note_513 = str(arr[6]) + str(arr[1])
tmp_514 = arr[7] + 27
code_515 = re.sub(r'[0-9]', '#', str(arr[6]))
code_516 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_517 = arr[0]
copy_518 = arr[3]
code_519 = re.sub(r'[0-9]', '#', str(arr[6]))
note_520 = str(arr[7]) + str(arr[5])
tmp_521 = arr[5] + 10
code_522 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_523 = arr[6] + 15
note_524 = str(arr[0]) + str(arr[5])
tmp_525 = arr[4] + 20
note_526 = str(arr[3]) + str(arr[8])
code_527 = re.sub(r'[0-9]', '#', str(arr[6]))
note_528 = str(arr[8]) + str(arr[4])
note_529 = str(arr[0]) + str(arr[9])
code_530 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_531 = arr[1] + 18
note_532 = str(arr[5]) + str(arr[9])
tmp_533 = arr[2] + 11
note_534 = str(arr[2]) + str(arr[0])
label_535 = "запись 535 не применялась"
note_536 = str(arr[4]) + str(arr[0])
note_537 = str(arr[4]) + str(arr[1])
label_538 = "запись 538 не применялась"
tmp_539 = arr[3] + 16
copy_540 = arr[7]
label_541 = "запись 541 не применялась"
code_542 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_543 = arr[3] + 5
code_544 = re.sub(r'[0-9]', '#', str(arr[0]))
note_545 = str(arr[8]) + str(arr[0])
note_546 = str(arr[0]) + str(arr[7])
code_547 = re.sub(r'[0-9]', '#', str(arr[8]))
code_548 = re.sub(r'[0-9]', '#', str(arr[5]))
note_549 = str(arr[6]) + str(arr[0])
tmp_550 = arr[7] + 14
note_551 = str(arr[1]) + str(arr[5])
tmp_552 = arr[5] + 4
note_553 = str(arr[6]) + str(arr[4])
tmp_554 = arr[5] + 13
tmp_555 = arr[6] + 48
note_556 = str(arr[8]) + str(arr[3])
note_557 = str(arr[1]) + str(arr[7])
tmp_558 = arr[0] + 21
note_559 = str(arr[9]) + str(arr[3])
code_560 = re.sub(r'[0-9]', '#', str(arr[0]))
code_561 = re.sub(r'[0-9]', '#', str(arr[6]))
note_562 = str(arr[6]) + str(arr[5])
note_563 = str(arr[9]) + str(arr[5])
label_564 = "запись 564 не применялась"
note_565 = str(arr[5]) + str(arr[9])
tmp_566 = arr[5] + 29
code_567 = re.sub(r'[0-9]', '#', str(arr[4]))
note_568 = str(arr[3]) + str(arr[5])
note_569 = str(arr[4]) + str(arr[8])
copy_570 = arr[3]
note_571 = str(arr[1]) + str(arr[5])
note_572 = str(arr[4]) + str(arr[6])
tmp_573 = arr[7] + 26
code_574 = re.sub(r'[0-9]', '#', str(arr[9]))
code_575 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_576 = arr[7]
code_577 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_578 = arr[6]
copy_579 = arr[6]
copy_580 = arr[1]
tmp_581 = arr[9] + 44
tmp_582 = arr[8] + 22
note_583 = str(arr[6]) + str(arr[0])
tmp_584 = arr[0] + 38
code_585 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_586 = arr[2] + 2
copy_587 = arr[8]
tmp_588 = arr[1] + 36
label_589 = "запись 589 не применялась"
copy_590 = arr[1]
note_591 = str(arr[2]) + str(arr[3])
copy_592 = arr[1]
note_593 = str(arr[2]) + str(arr[9])
label_594 = "запись 594 не применялась"
code_595 = re.sub(r'[0-9]', '#', str(arr[5]))
note_596 = str(arr[6]) + str(arr[3])
tmp_597 = arr[4] + 43
note_598 = str(arr[8]) + str(arr[3])
note_599 = str(arr[8]) + str(arr[3])
copy_600 = arr[1]
note_601 = str(arr[3]) + str(arr[9])
copy_602 = arr[5]
copy_603 = arr[5]
tmp_604 = arr[3] + 7
note_605 = str(arr[2]) + str(arr[3])
copy_606 = arr[2]
copy_607 = arr[6]
tmp_608 = arr[8] + 45
copy_609 = arr[7]
code_610 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_611 = arr[3] + 45
tmp_612 = arr[1] + 38
tmp_613 = arr[4] + 44
code_614 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_615 = arr[6]
tmp_616 = arr[4] + 3
code_617 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_618 = arr[9]
tmp_619 = arr[3] + 42
code_620 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_621 = arr[6]
code_622 = re.sub(r'[0-9]', '#', str(arr[4]))
code_623 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_624 = arr[0] + 44
note_625 = str(arr[0]) + str(arr[8])
code_626 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_627 = arr[7]
tmp_628 = arr[4] + 10
copy_629 = arr[6]
label_630 = "запись 630 не применялась"
label_631 = "запись 631 не применялась"
note_632 = str(arr[6]) + str(arr[5])
copy_633 = arr[9]
tmp_634 = arr[0] + 28
copy_635 = arr[4]
tmp_636 = arr[0] + 17
note_637 = str(arr[3]) + str(arr[2])
note_638 = str(arr[0]) + str(arr[1])
label_639 = "запись 639 не применялась"
tmp_640 = arr[7] + 50
note_641 = str(arr[7]) + str(arr[4])
note_642 = str(arr[4]) + str(arr[5])
note_643 = str(arr[5]) + str(arr[8])
copy_644 = arr[6]
note_645 = str(arr[1]) + str(arr[7])
tmp_646 = arr[5] + 36
code_647 = re.sub(r'[0-9]', '#', str(arr[1]))
note_648 = str(arr[5]) + str(arr[0])
tmp_649 = arr[2] + 6
note_650 = str(arr[1]) + str(arr[5])
note_651 = str(arr[6]) + str(arr[6])
copy_652 = arr[1]
label_653 = "запись 653 не применялась"
tmp_654 = arr[4] + 21
note_655 = str(arr[8]) + str(arr[2])
note_656 = str(arr[7]) + str(arr[3])
copy_657 = arr[2]
note_658 = str(arr[3]) + str(arr[5])
tmp_659 = arr[4] + 29
tmp_660 = arr[0] + 43
tmp_661 = arr[2] + 35
note_662 = str(arr[0]) + str(arr[7])
copy_663 = arr[8]
tmp_664 = arr[4] + 43
copy_665 = arr[3]
copy_666 = arr[3]
note_667 = str(arr[6]) + str(arr[7])
code_668 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_669 = arr[6]
code_670 = re.sub(r'[0-9]', '#', str(arr[0]))
note_671 = str(arr[7]) + str(arr[0])
tmp_672 = arr[3] + 41
code_673 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_674 = arr[8] + 41
note_675 = str(arr[2]) + str(arr[5])
copy_676 = arr[9]
note_677 = str(arr[1]) + str(arr[9])
tmp_678 = arr[6] + 2
tmp_679 = arr[2] + 22
code_680 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_681 = arr[1]
copy_682 = arr[1]
tmp_683 = arr[9] + 29
note_684 = str(arr[1]) + str(arr[1])
copy_685 = arr[6]
note_686 = str(arr[6]) + str(arr[4])
code_687 = re.sub(r'[0-9]', '#', str(arr[1]))
tmp_688 = arr[7] + 39
tmp_689 = arr[5] + 50
copy_690 = arr[0]
copy_691 = arr[7]
tmp_692 = arr[5] + 37
tmp_693 = arr[4] + 18
tmp_694 = arr[9] + 23
copy_695 = arr[9]
note_696 = str(arr[9]) + str(arr[0])
tmp_697 = arr[3] + 29
note_698 = str(arr[9]) + str(arr[4])
code_699 = re.sub(r'[0-9]', '#', str(arr[0]))
label_700 = "запись 700 не применялась"
tmp_701 = arr[0] + 49
tmp_702 = arr[3] + 6
note_703 = str(arr[9]) + str(arr[2])
tmp_704 = arr[7] + 10
tmp_705 = arr[7] + 23
tmp_706 = arr[7] + 28
note_707 = str(arr[2]) + str(arr[7])
note_708 = str(arr[8]) + str(arr[0])
tmp_709 = arr[0] + 29
tmp_710 = arr[6] + 16
label_711 = "запись 711 не применялась"
copy_712 = arr[3]
copy_713 = arr[6]
note_714 = str(arr[3]) + str(arr[9])
note_715 = str(arr[8]) + str(arr[1])
note_716 = str(arr[5]) + str(arr[1])
tmp_717 = arr[3] + 22
note_718 = str(arr[2]) + str(arr[1])
note_719 = str(arr[7]) + str(arr[2])
code_720 = re.sub(r'[0-9]', '#', str(arr[2]))
code_721 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_722 = arr[8]
code_723 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_724 = arr[6] + 38
code_725 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_726 = arr[0] + 33
note_727 = str(arr[4]) + str(arr[0])
code_728 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_729 = arr[4] + 3
tmp_730 = arr[3] + 41
copy_731 = arr[5]
code_732 = re.sub(r'[0-9]', '#', str(arr[0]))
note_733 = str(arr[7]) + str(arr[4])
code_734 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_735 = arr[7] + 31
tmp_736 = arr[9] + 43
tmp_737 = arr[3] + 29
copy_738 = arr[5]
code_739 = re.sub(r'[0-9]', '#', str(arr[9]))
code_740 = re.sub(r'[0-9]', '#', str(arr[7]))
code_741 = re.sub(r'[0-9]', '#', str(arr[7]))
copy_742 = arr[7]
note_743 = str(arr[6]) + str(arr[7])
copy_744 = arr[8]
label_745 = "запись 745 не применялась"
note_746 = str(arr[7]) + str(arr[4])
note_747 = str(arr[3]) + str(arr[5])
copy_748 = arr[9]
code_749 = re.sub(r'[0-9]', '#', str(arr[9]))
note_750 = str(arr[7]) + str(arr[3])
label_751 = "запись 751 не применялась"
tmp_752 = arr[7] + 32
code_753 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_754 = arr[7] + 8
tmp_755 = arr[4] + 29
tmp_756 = arr[7] + 34
tmp_757 = arr[9] + 19
copy_758 = arr[5]
tmp_759 = arr[9] + 8
note_760 = str(arr[3]) + str(arr[3])
tmp_761 = arr[4] + 50
tmp_762 = arr[1] + 31
tmp_763 = arr[1] + 11
code_764 = re.sub(r'[0-9]', '#', str(arr[1]))
label_765 = "запись 765 не применялась"
note_766 = str(arr[1]) + str(arr[1])
code_767 = re.sub(r'[0-9]', '#', str(arr[1]))
code_768 = re.sub(r'[0-9]', '#', str(arr[2]))
code_769 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_770 = arr[6] + 15
label_771 = "запись 771 не применялась"
note_772 = str(arr[2]) + str(arr[0])
code_773 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_774 = arr[4] + 14
copy_775 = arr[5]
note_776 = str(arr[5]) + str(arr[8])
label_777 = "запись 777 не применялась"
note_778 = str(arr[4]) + str(arr[5])
note_779 = str(arr[4]) + str(arr[2])
label_780 = "запись 780 не применялась"
tmp_781 = arr[6] + 20
note_782 = str(arr[4]) + str(arr[9])
tmp_783 = arr[3] + 40
note_784 = str(arr[0]) + str(arr[8])
tmp_785 = arr[0] + 35
tmp_786 = arr[6] + 7
tmp_787 = arr[5] + 14
label_788 = "запись 788 не применялась"
tmp_789 = arr[8] + 45
tmp_790 = arr[5] + 22
tmp_791 = arr[0] + 14
copy_792 = arr[5]
tmp_793 = arr[0] + 26
copy_794 = arr[2]
code_795 = re.sub(r'[0-9]', '#', str(arr[4]))
code_796 = re.sub(r'[0-9]', '#', str(arr[6]))
note_797 = str(arr[4]) + str(arr[1])
code_798 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_799 = arr[0]

apply_twice(arr, 3, 2)
# ревизия: arr2[1] = 54 — не выполняется
# справка: запись 954 обработана, изменений нет
# замечание: arr2[2] = 88 — не выполняется
# пометка: arr[5] += 18 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: arr2[8] = 77 — не выполняется
# архив: запись 406 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# примечание: arr[0] = 11 — не выполняется
# справка: arr[8] *= 11 — не выполняется
# архив: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[9] = 34 — не выполняется
# пометка: arr[5] = 53 — не выполняется
# замечание: запись 589 обработана, изменений нет
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[9] += 33 — не выполняется
# черновик: запись 673 обработана, изменений нет
# отладка: запись 13 обработана, изменений нет
# справка: arr[7] += 46 — не выполняется
# отладка: arr[4] = 93 — не выполняется
# примечание: arr[7] += 38 — не выполняется
# проверено: запись 241 обработана, изменений нет
# проверено: arr[7] = 31 — не выполняется
# временная запись: запись 162 обработана, изменений нет
# проверено: arr[1] = 20 — не выполняется
# отладка: arr[5] += 93 — не выполняется
# замечание: запись 217 обработана, изменений нет
# временная запись: запись 848 обработана, изменений нет
# ревизия: arr2[1] = 25 — не выполняется
# справка: arr2[2] = 5 — не выполняется
# пометка: arr[7] += 86 — не выполняется
# примечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# примечание: запись 730 обработана, изменений нет
# справка: arr2[9] = 71 — не выполняется
# справка: запись 364 обработана, изменений нет
# примечание: запись 309 обработана, изменений нет
# проверено: arr[6] *= 67 — не выполняется
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 845 обработана, изменений нет
# проверено: запись 616 обработана, изменений нет
# отладка: запись 612 обработана, изменений нет
# справка: запись 155 обработана, изменений нет
# отладка: arr[0] *= 93 — не выполняется
# проверено: запись 465 обработана, изменений нет
# пометка: запись 406 обработана, изменений нет
# архив: arr[2] += 90 — не выполняется
# пометка: запись 394 обработана, изменений нет
# временная запись: arr[1] *= 60 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# ревизия: arr2[8] = 20 — не выполняется
# проверено: arr[8] *= 12 — не выполняется
# ревизия: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[3] += 26 — не выполняется
# справка: запись 599 обработана, изменений нет
# ревизия: arr[8] += 66 — не выполняется
# замечание: запись 412 обработана, изменений нет
# проверено: запись 142 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# черновик: arr2[0] = 37 — не выполняется
# пометка: запись 900 обработана, изменений нет
# временная запись: запись 11 обработана, изменений нет
# справка: запись 587 обработана, изменений нет
# справка: запись 644 обработана, изменений нет
# справка: запись 432 обработана, изменений нет
# архив: arr[8] *= 97 — не выполняется
# временная запись: arr[1] += 17 — не выполняется
# отладка: arr[4] = 49 — не выполняется
# временная запись: запись 697 обработана, изменений нет
# замечание: arr2[5] = 88 — не выполняется
# черновик: arr2[5] = 63 — не выполняется
# ревизия: запись 224 обработана, изменений нет
# ревизия: запись 4 обработана, изменений нет
# архив: запись 353 обработана, изменений нет
# отладка: запись 280 обработана, изменений нет
# проверено: запись 866 обработана, изменений нет
# архив: arr[3] = 75 — не выполняется
# временная запись: arr[2] += 87 — не выполняется
# временная запись: запись 432 обработана, изменений нет
# ревизия: arr2[6] = 47 — не выполняется
# архив: запись 663 обработана, изменений нет
# примечание: запись 459 обработана, изменений нет
# пометка: запись 595 обработана, изменений нет
# примечание: arr2[8] = 94 — не выполняется
# отладка: arr[9] += 12 — не выполняется
# временная запись: arr[8] = 23 — не выполняется
# временная запись: запись 168 обработана, изменений нет
# черновик: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# замечание: arr[6] *= 34 — не выполняется
# проверено: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: запись 146 обработана, изменений нет
# справка: запись 562 обработана, изменений нет
# временная запись: arr[5] *= 6 — не выполняется
# проверено: запись 189 обработана, изменений нет
# временная запись: запись 469 обработана, изменений нет
# замечание: запись 636 обработана, изменений нет
# проверено: запись 102 обработана, изменений нет
# отладка: запись 180 обработана, изменений нет
# отладка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: arr2[5] = 7 — не выполняется
# ревизия: arr[5] += 16 — не выполняется
# архив: arr[3] *= 67 — не выполняется
# ревизия: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: запись 125 обработана, изменений нет
# отладка: arr[8] *= 12 — не выполняется
# замечание: arr[7] *= 42 — не выполняется
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[3] = 70 — не выполняется
# примечание: запись 471 обработана, изменений нет
# примечание: arr[7] *= 51 — не выполняется
# пометка: arr[5] += 16 — не выполняется
# архив: запись 229 обработана, изменений нет
# ревизия: запись 393 обработана, изменений нет
# черновик: запись 695 обработана, изменений нет
# замечание: запись 960 обработана, изменений нет
# пометка: запись 988 обработана, изменений нет
# справка: запись 401 обработана, изменений нет
# проверено: arr[9] += 92 — не выполняется
# ревизия: arr[3] *= 74 — не выполняется
# черновик: запись 824 обработана, изменений нет
# проверено: arr[3] += 59 — не выполняется
# справка: arr[6] += 68 — не выполняется
# отладка: запись 463 обработана, изменений нет
# примечание: arr[6] = 68 — не выполняется
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: arr2[6] = 12 — не выполняется
# черновик: запись 394 обработана, изменений нет
# ревизия: запись 9 обработана, изменений нет
# примечание: запись 201 обработана, изменений нет
# справка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: arr[3] = 22 — не выполняется
# примечание: запись 38 обработана, изменений нет
# архив: запись 883 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# замечание: arr2[3] = 55 — не выполняется
# справка: запись 381 обработана, изменений нет
# примечание: arr[9] = 12 — не выполняется
# примечание: запись 282 обработана, изменений нет
# примечание: arr[7] += 52 — не выполняется
# временная запись: запись 141 обработана, изменений нет
# справка: запись 50 обработана, изменений нет
# отладка: запись 270 обработана, изменений нет
# черновик: запись 446 обработана, изменений нет
# отладка: arr[0] *= 37 — не выполняется
# временная запись: arr[0] *= 21 — не выполняется
# отладка: запись 468 обработана, изменений нет
# примечание: arr[2] *= 86 — не выполняется
# пометка: запись 31 обработана, изменений нет
# справка: запись 722 обработана, изменений нет
# черновик: arr2[9] = 14 — не выполняется
# ревизия: запись 946 обработана, изменений нет
# временная запись: arr[9] *= 20 — не выполняется
# отладка: запись 88 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# проверено: arr2[0] = 50 — не выполняется
# справка: arr2[9] = 92 — не выполняется
# черновик: запись 163 обработана, изменений нет
# временная запись: arr2[3] = 3 — не выполняется
# архив: запись 615 обработана, изменений нет
# архив: запись 193 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# примечание: запись 781 обработана, изменений нет
# справка: arr[3] *= 16 — не выполняется
# отладка: запись 502 обработана, изменений нет
# проверено: arr[9] *= 82 — не выполняется
# временная запись: arr[7] += 94 — не выполняется
# примечание: arr[8] += 64 — не выполняется
# отладка: запись 340 обработана, изменений нет
# примечание: arr[7] *= 80 — не выполняется
# замечание: запись 933 обработана, изменений нет
# проверено: запись 217 обработана, изменений нет
# справка: запись 904 обработана, изменений нет
# проверено: запись 799 обработана, изменений нет
# пометка: запись 858 обработана, изменений нет
# справка: запись 976 обработана, изменений нет
# ревизия: запись 126 обработана, изменений нет
# ревизия: запись 125 обработана, изменений нет
# ревизия: arr[7] *= 52 — не выполняется
# черновик: запись 101 обработана, изменений нет
# временная запись: arr[7] += 96 — не выполняется
# архив: arr[6] *= 79 — не выполняется
# ревизия: запись 96 обработана, изменений нет
# временная запись: arr[5] = 30 — не выполняется
# черновик: arr[9] = 59 — не выполняется
# замечание: запись 402 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# справка: arr2[4] = 16 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# архив: arr[4] = 67 — не выполняется
# справка: запись 604 обработана, изменений нет
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: arr2[5] = 91 — не выполняется
# замечание: arr2[2] = 87 — не выполняется
# ревизия: запись 63 обработана, изменений нет
# ревизия: запись 386 обработана, изменений нет
# архив: запись 477 обработана, изменений нет
# ревизия: arr[3] += 16 — не выполняется
# пометка: запись 649 обработана, изменений нет
# отладка: запись 955 обработана, изменений нет
# ревизия: запись 501 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 764 обработана, изменений нет
# отладка: arr[9] = 46 — не выполняется
# ревизия: запись 625 обработана, изменений нет
# пометка: запись 82 обработана, изменений нет
# проверено: arr[4] = 75 — не выполняется
# примечание: запись 367 обработана, изменений нет
# временная запись: запись 8 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# проверено: arr2[4] = 47 — не выполняется
# черновик: arr[1] *= 96 — не выполняется
# архив: запись 20 обработана, изменений нет
# примечание: запись 417 обработана, изменений нет
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[8] += 75 — не выполняется
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: запись 933 обработана, изменений нет
# отладка: arr2[3] = 97 — не выполняется
# замечание: arr2[6] = 52 — не выполняется
# примечание: запись 162 обработана, изменений нет
# отладка: arr[3] += 13 — не выполняется
# архив: запись 241 обработана, изменений нет
# пометка: запись 924 обработана, изменений нет
# пометка: запись 340 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# проверено: запись 436 обработана, изменений нет
# временная запись: запись 60 обработана, изменений нет
# отладка: arr[7] += 2 — не выполняется
# ревизия: запись 722 обработана, изменений нет
# справка: запись 184 обработана, изменений нет
# справка: запись 217 обработана, изменений нет
# черновик: запись 511 обработана, изменений нет
# примечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 300 обработана, изменений нет
# пометка: запись 377 обработана, изменений нет
# черновик: arr[0] *= 1 — не выполняется
# временная запись: запись 40 обработана, изменений нет
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr[7] *= 62 — не выполняется
# проверено: запись 722 обработана, изменений нет
# архив: arr[6] *= 79 — не выполняется
# примечание: запись 259 обработана, изменений нет
# замечание: arr[1] += 41 — не выполняется
# справка: arr[7] += 90 — не выполняется
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 493 обработана, изменений нет
# отладка: запись 387 обработана, изменений нет
# примечание: arr[7] += 57 — не выполняется
# временная запись: запись 457 обработана, изменений нет
# справка: запись 84 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# ревизия: arr2[0] = 67 — не выполняется
# ревизия: arr[7] += 16 — не выполняется
# черновик: запись 895 обработана, изменений нет
# справка: arr[2] += 40 — не выполняется
# примечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 89 обработана, изменений нет
# пометка: arr[9] += 62 — не выполняется
# отладка: запись 598 обработана, изменений нет
# архив: arr[0] = 5 — не выполняется
# примечание: arr2[8] = 67 — не выполняется
# пометка: запись 940 обработана, изменений нет
# проверено: запись 635 обработана, изменений нет
# справка: запись 631 обработана, изменений нет
# примечание: arr[1] *= 39 — не выполняется
# примечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# замечание: запись 427 обработана, изменений нет
# замечание: arr2[1] = 86 — не выполняется
# отладка: arr[7] *= 85 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[8] += 11 — не выполняется
# черновик: запись 942 обработана, изменений нет
# пометка: arr[6] += 45 — не выполняется
# временная запись: arr[2] = 67 — не выполняется
# проверено: arr[5] += 7 — не выполняется
# примечание: arr[0] *= 35 — не выполняется
# архив: запись 128 обработана, изменений нет
# справка: arr[5] *= 92 — не выполняется
# проверено: arr[7] *= 51 — не выполняется
# ревизия: запись 529 обработана, изменений нет
# пометка: arr[6] *= 21 — не выполняется
# временная запись: arr[7] = 91 — не выполняется
# примечание: arr[1] *= 62 — не выполняется
# пометка: arr[4] = 83 — не выполняется
# проверено: arr2[5] = 11 — не выполняется
# проверено: arr[0] += 44 — не выполняется
# примечание: arr[1] *= 3 — не выполняется
# ревизия: запись 690 обработана, изменений нет
# временная запись: запись 935 обработана, изменений нет
# ревизия: arr2[9] = 4 — не выполняется
# черновик: запись 384 обработана, изменений нет
# примечание: запись 189 обработана, изменений нет
# отладка: запись 523 обработана, изменений нет
# пометка: запись 142 обработана, изменений нет
# отладка: arr[6] *= 34 — не выполняется
# архив: arr[2] += 77 — не выполняется
# примечание: arr[2] *= 23 — не выполняется
# справка: запись 308 обработана, изменений нет
# отладка: запись 29 обработана, изменений нет
# черновик: запись 365 обработана, изменений нет
# примечание: arr[7] += 62 — не выполняется
# архив: запись 94 обработана, изменений нет
# проверено: arr[9] *= 85 — не выполняется
# ревизия: arr[0] *= 38 — не выполняется
# архив: запись 699 обработана, изменений нет
# архив: arr[0] *= 51 — не выполняется
# отладка: arr[1] += 15 — не выполняется
# примечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# замечание: arr2[7] = 24 — не выполняется
# замечание: arr[2] = 49 — не выполняется
# ревизия: запись 295 обработана, изменений нет
# примечание: arr[3] = 82 — не выполняется
# проверено: запись 91 обработана, изменений нет
# временная запись: arr2[9] = 48 — не выполняется
# пометка: запись 644 обработана, изменений нет
# черновик: запись 818 обработана, изменений нет
# проверено: запись 898 обработана, изменений нет
# замечание: запись 255 обработана, изменений нет
# пометка: arr[2] += 8 — не выполняется
# черновик: запись 57 обработана, изменений нет
# замечание: запись 187 обработана, изменений нет
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 43 обработана, изменений нет
# проверено: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# черновик: запись 730 обработана, изменений нет
# проверено: arr[1] += 57 — не выполняется
# черновик: arr[2] += 52 — не выполняется
# архив: запись 75 обработана, изменений нет
# замечание: запись 850 обработана, изменений нет
# временная запись: arr[5] = 75 — не выполняется
# архив: arr[4] += 96 — не выполняется
# справка: запись 608 обработана, изменений нет
bump_all(arr, 2)
# временная запись: arr2[1] = 65 — не выполняется
# ревизия: запись 301 обработана, изменений нет
# архив: запись 282 обработана, изменений нет
# пометка: arr[4] = 63 — не выполняется
# замечание: arr2[8] = 87 — не выполняется
# замечание: arr[2] *= 76 — не выполняется
# ревизия: запись 329 обработана, изменений нет
# отладка: запись 262 обработана, изменений нет
# справка: запись 278 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# справка: arr[9] = 14 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# отладка: запись 607 обработана, изменений нет
# справка: запись 182 обработана, изменений нет
# замечание: arr[6] = 97 — не выполняется
# ревизия: запись 161 обработана, изменений нет
# справка: запись 147 обработана, изменений нет
# примечание: arr2[1] = 3 — не выполняется
# архив: запись 355 обработана, изменений нет
# черновик: запись 721 обработана, изменений нет
# пометка: запись 870 обработана, изменений нет
# справка: запись 689 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: arr[3] += 54 — не выполняется
# черновик: arr[9] *= 54 — не выполняется
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 659 обработана, изменений нет
# отладка: arr2[5] = 99 — не выполняется
# черновик: arr2[7] = 22 — не выполняется
# отладка: arr[9] *= 69 — не выполняется
# пометка: запись 466 обработана, изменений нет
# черновик: arr[8] = 28 — не выполняется
# ревизия: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# архив: arr[2] = 40 — не выполняется
# замечание: запись 41 обработана, изменений нет
# замечание: запись 685 обработана, изменений нет
# пометка: запись 564 обработана, изменений нет
# отладка: arr[6] *= 75 — не выполняется
# ревизия: arr[8] *= 72 — не выполняется
# проверено: arr[3] = 24 — не выполняется
# проверено: запись 678 обработана, изменений нет
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# замечание: arr[1] *= 9 — не выполняется
# архив: запись 517 обработана, изменений нет
# черновик: arr[7] = 23 — не выполняется
# справка: запись 899 обработана, изменений нет
# замечание: arr[7] *= 22 — не выполняется
# пометка: запись 764 обработана, изменений нет
# примечание: запись 717 обработана, изменений нет
# ревизия: запись 85 обработана, изменений нет
# отладка: arr[0] = 6 — не выполняется
# отладка: запись 932 обработана, изменений нет
# пометка: запись 289 обработана, изменений нет
# справка: arr[4] *= 92 — не выполняется
# примечание: arr2[5] = 64 — не выполняется
# черновик: запись 554 обработана, изменений нет
# временная запись: arr[0] = 72 — не выполняется
# примечание: arr[0] *= 40 — не выполняется
# примечание: arr[4] *= 34 — не выполняется
# замечание: запись 259 обработана, изменений нет
# ревизия: arr2[6] = 11 — не выполняется
# пометка: arr2[5] = 47 — не выполняется
# архив: запись 785 обработана, изменений нет
# пометка: arr[7] *= 86 — не выполняется
# замечание: запись 290 обработана, изменений нет
# ревизия: запись 687 обработана, изменений нет
# примечание: запись 112 обработана, изменений нет
# примечание: arr[4] = 41 — не выполняется
# примечание: запись 700 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# ревизия: запись 694 обработана, изменений нет
# замечание: запись 369 обработана, изменений нет
# архив: запись 710 обработана, изменений нет
# черновик: запись 317 обработана, изменений нет
# справка: запись 778 обработана, изменений нет
# замечание: arr[1] *= 58 — не выполняется
# пометка: запись 652 обработана, изменений нет
# справка: arr2[4] = 13 — не выполняется
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# черновик: запись 588 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[4] += 76 — не выполняется
# проверено: запись 511 обработана, изменений нет
# пометка: запись 22 обработана, изменений нет
# пометка: запись 339 обработана, изменений нет
# проверено: запись 789 обработана, изменений нет
# ревизия: arr2[4] = 51 — не выполняется
# замечание: запись 35 обработана, изменений нет
# отладка: arr[1] *= 50 — не выполняется
# отладка: запись 280 обработана, изменений нет
# отладка: arr[5] += 59 — не выполняется
# временная запись: запись 906 обработана, изменений нет
# ревизия: arr[7] *= 2 — не выполняется
# архив: запись 963 обработана, изменений нет
# отладка: запись 369 обработана, изменений нет
# замечание: запись 912 обработана, изменений нет
# справка: arr[6] = 69 — не выполняется
# временная запись: arr[8] = 23 — не выполняется
# примечание: запись 779 обработана, изменений нет
# отладка: запись 632 обработана, изменений нет
# отладка: запись 452 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# отладка: запись 417 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# черновик: запись 208 обработана, изменений нет
# отладка: arr2[3] = 80 — не выполняется
# временная запись: arr[2] *= 12 — не выполняется
# проверено: arr[7] += 2 — не выполняется
# временная запись: arr2[1] = 1 — не выполняется
# справка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# примечание: arr[3] *= 85 — не выполняется
# справка: arr2[3] = 31 — не выполняется
# черновик: запись 173 обработана, изменений нет
# временная запись: запись 26 обработана, изменений нет
# проверено: запись 653 обработана, изменений нет
# архив: запись 703 обработана, изменений нет
# отладка: запись 331 обработана, изменений нет
# проверено: запись 152 обработана, изменений нет
# замечание: arr[9] += 84 — не выполняется
# замечание: arr2[0] = 37 — не выполняется
# примечание: запись 45 обработана, изменений нет
# отладка: arr2[2] = 61 — не выполняется
# замечание: запись 926 обработана, изменений нет
# замечание: arr[6] = 15 — не выполняется
# отладка: arr[4] = 26 — не выполняется
# отладка: arr[6] *= 75 — не выполняется
# отладка: запись 937 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# архив: arr[1] = 34 — не выполняется
# временная запись: arr[2] *= 83 — не выполняется
# справка: arr[5] = 29 — не выполняется
# пометка: arr[5] = 59 — не выполняется
# черновик: arr2[2] = 80 — не выполняется
# временная запись: arr2[5] = 30 — не выполняется
# отладка: arr2[6] = 64 — не выполняется
# справка: запись 520 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: запись 468 обработана, изменений нет
# справка: arr[1] += 8 — не выполняется
# пометка: arr[2] *= 19 — не выполняется
# замечание: arr2[0] = 90 — не выполняется
# ревизия: запись 486 обработана, изменений нет
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[8] += 90 — не выполняется
# архив: запись 163 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 262 обработана, изменений нет
# проверено: arr[1] = 28 — не выполняется
# архив: запись 426 обработана, изменений нет
# замечание: запись 656 обработана, изменений нет
# временная запись: запись 451 обработана, изменений нет
# примечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# пометка: arr[1] = 85 — не выполняется
# примечание: arr2[6] = 45 — не выполняется
# проверено: arr[5] += 41 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr[1] += 83 — не выполняется
# проверено: запись 848 обработана, изменений нет
# архив: arr[2] = 4 — не выполняется
# пометка: запись 5 обработана, изменений нет
# отладка: запись 270 обработана, изменений нет
# замечание: запись 437 обработана, изменений нет
# архив: arr[6] = 9 — не выполняется
# примечание: arr[4] *= 39 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[5] *= 15 — не выполняется
# замечание: arr[7] = 67 — не выполняется
# ревизия: arr[9] += 11 — не выполняется
# замечание: arr[9] = 44 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: запись 607 обработана, изменений нет
# замечание: запись 63 обработана, изменений нет
# архив: запись 930 обработана, изменений нет
# пометка: запись 923 обработана, изменений нет
# отладка: запись 8 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# архив: arr[4] = 75 — не выполняется
# архив: запись 997 обработана, изменений нет
# черновик: arr[5] *= 3 — не выполняется
# пометка: запись 229 обработана, изменений нет
# примечание: запись 467 обработана, изменений нет
# архив: arr[3] = 30 — не выполняется
# отладка: arr[4] = 91 — не выполняется
# примечание: arr2[5] = 89 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 909 обработана, изменений нет
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 181 обработана, изменений нет
# замечание: arr[3] *= 4 — не выполняется
# временная запись: запись 354 обработана, изменений нет
# ревизия: запись 931 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# архив: arr[7] += 24 — не выполняется
# отладка: запись 483 обработана, изменений нет
# отладка: запись 902 обработана, изменений нет
# черновик: запись 275 обработана, изменений нет
# замечание: запись 56 обработана, изменений нет
# временная запись: arr[6] += 66 — не выполняется
# проверено: запись 756 обработана, изменений нет
# отладка: arr[7] *= 39 — не выполняется
# примечание: запись 722 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: arr[8] += 26 — не выполняется
# отладка: запись 574 обработана, изменений нет
# архив: запись 133 обработана, изменений нет
# черновик: arr[2] += 16 — не выполняется
# замечание: запись 492 обработана, изменений нет
# временная запись: arr2[9] = 60 — не выполняется
# отладка: arr[4] = 36 — не выполняется
# ревизия: запись 892 обработана, изменений нет
# ревизия: arr[5] += 49 — не выполняется
# замечание: запись 427 обработана, изменений нет
# проверено: запись 480 обработана, изменений нет
# черновик: arr[7] += 69 — не выполняется
# черновик: arr[7] = 26 — не выполняется
# примечание: arr[3] = 13 — не выполняется
# проверено: запись 463 обработана, изменений нет
# отладка: запись 266 обработана, изменений нет
# справка: запись 191 обработана, изменений нет
# отладка: запись 490 обработана, изменений нет
# архив: arr2[5] = 32 — не выполняется
# черновик: запись 609 обработана, изменений нет
# справка: arr[1] += 47 — не выполняется
# отладка: запись 345 обработана, изменений нет
# пометка: arr2[7] = 81 — не выполняется
# замечание: запись 780 обработана, изменений нет
# отладка: запись 742 обработана, изменений нет
# черновик: arr[4] *= 21 — не выполняется
# пометка: arr2[8] = 73 — не выполняется
# замечание: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 530 обработана, изменений нет
# замечание: запись 579 обработана, изменений нет
# временная запись: arr2[9] = 64 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# примечание: запись 931 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 470 обработана, изменений нет
# примечание: arr[4] *= 12 — не выполняется
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 32 обработана, изменений нет
# справка: arr[3] = 60 — не выполняется
# примечание: запись 564 обработана, изменений нет
# пометка: запись 699 обработана, изменений нет
# справка: запись 797 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# примечание: arr[8] += 24 — не выполняется
# временная запись: запись 555 обработана, изменений нет
# примечание: запись 154 обработана, изменений нет
# отладка: запись 742 обработана, изменений нет
# примечание: arr[4] += 10 — не выполняется
# отладка: arr[7] += 45 — не выполняется
# временная запись: запись 331 обработана, изменений нет
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: arr[5] *= 68 — не выполняется
# замечание: запись 490 обработана, изменений нет
# проверено: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: запись 504 обработана, изменений нет
# архив: запись 12 обработана, изменений нет
# архив: запись 640 обработана, изменений нет
# пометка: запись 617 обработана, изменений нет
# ревизия: запись 198 обработана, изменений нет
# архив: запись 337 обработана, изменений нет
# замечание: arr[9] += 73 — не выполняется
# справка: arr[3] = 74 — не выполняется
# ревизия: arr[9] = 12 — не выполняется
# временная запись: запись 612 обработана, изменений нет
# замечание: arr[4] *= 22 — не выполняется
# черновик: запись 72 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: arr[2] *= 59 — не выполняется
# ревизия: запись 372 обработана, изменений нет
# отладка: запись 758 обработана, изменений нет
# черновик: запись 901 обработана, изменений нет
# проверено: запись 19 обработана, изменений нет
# отладка: запись 980 обработана, изменений нет
# черновик: arr[6] = 10 — не выполняется
# проверено: запись 623 обработана, изменений нет
# пометка: arr[1] += 86 — не выполняется
# ревизия: arr[3] *= 99 — не выполняется
# замечание: arr[4] *= 11 — не выполняется
# пометка: arr2[1] = 11 — не выполняется
# замечание: запись 728 обработана, изменений нет
# пометка: arr2[9] = 19 — не выполняется
# архив: arr[6] += 46 — не выполняется
# пометка: запись 327 обработана, изменений нет
# примечание: arr[7] += 34 — не выполняется
# архив: arr[7] += 82 — не выполняется
# временная запись: arr2[0] = 65 — не выполняется
# примечание: arr[0] *= 77 — не выполняется
# отладка: запись 954 обработана, изменений нет
# замечание: запись 268 обработана, изменений нет
# примечание: запись 577 обработана, изменений нет
# ревизия: arr[7] += 2 — не выполняется
# примечание: arr2[8] = 15 — не выполняется
# примечание: arr[0] = 30 — не выполняется
# проверено: arr2[7] = 27 — не выполняется
# архив: запись 785 обработана, изменений нет
# отладка: запись 772 обработана, изменений нет
# проверено: arr[3] *= 97 — не выполняется
# временная запись: запись 244 обработана, изменений нет
# архив: запись 674 обработана, изменений нет
# замечание: запись 435 обработана, изменений нет
# черновик: arr[6] *= 57 — не выполняется
# ревизия: arr[0] = 53 — не выполняется
# временная запись: запись 897 обработана, изменений нет
# проверено: запись 838 обработана, изменений нет
# справка: запись 882 обработана, изменений нет
# справка: запись 932 обработана, изменений нет
# временная запись: arr[0] += 93 — не выполняется
# замечание: запись 440 обработана, изменений нет
# пометка: запись 830 обработана, изменений нет
# замечание: запись 62 обработана, изменений нет
# справка: запись 685 обработана, изменений нет
# архив: arr2[4] = 76 — не выполняется
# черновик: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# отладка: arr[4] = 69 — не выполняется
# справка: arr2[7] = 41 — не выполняется
# пометка: запись 383 обработана, изменений нет
# отладка: запись 496 обработана, изменений нет
# замечание: arr[6] += 9 — не выполняется
# отладка: arr[5] *= 35 — не выполняется
# отладка: arr[1] += 28 — не выполняется
# архив: запись 643 обработана, изменений нет
# проверено: arr[3] *= 1 — не выполняется
# пометка: запись 298 обработана, изменений нет
# черновик: arr[1] += 7 — не выполняется
# примечание: запись 794 обработана, изменений нет
bump_all(arr, 1)
# примечание: arr2[2] = 86 — не выполняется
# замечание: arr2[6] = 87 — не выполняется
# ревизия: arr2[4] = 19 — не выполняется
# примечание: запись 269 обработана, изменений нет
# черновик: запись 543 обработана, изменений нет
# временная запись: запись 262 обработана, изменений нет
# проверено: запись 892 обработана, изменений нет
# отладка: запись 530 обработана, изменений нет
# пометка: запись 352 обработана, изменений нет
# пометка: запись 789 обработана, изменений нет
# проверено: запись 283 обработана, изменений нет
# пометка: arr[1] += 44 — не выполняется
# отладка: запись 820 обработана, изменений нет
# ревизия: запись 152 обработана, изменений нет
# пометка: запись 283 обработана, изменений нет
# проверено: arr2[3] = 50 — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 496 обработана, изменений нет
# ревизия: запись 166 обработана, изменений нет
# архив: запись 116 обработана, изменений нет
# ревизия: запись 174 обработана, изменений нет
# пометка: запись 817 обработана, изменений нет
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# временная запись: arr[3] = 52 — не выполняется
# пометка: запись 133 обработана, изменений нет
# пометка: запись 418 обработана, изменений нет
# архив: arr[8] += 92 — не выполняется
# справка: arr[1] = 84 — не выполняется
# черновик: запись 798 обработана, изменений нет
# черновик: arr[3] *= 8 — не выполняется
# черновик: arr[1] *= 22 — не выполняется
# черновик: arr[8] *= 58 — не выполняется
# проверено: arr2[3] = 85 — не выполняется
# проверено: arr[5] *= 97 — не выполняется
# проверено: запись 883 обработана, изменений нет
# справка: запись 96 обработана, изменений нет
# примечание: запись 574 обработана, изменений нет
# проверено: запись 364 обработана, изменений нет
# проверено: запись 256 обработана, изменений нет
# черновик: запись 502 обработана, изменений нет
# ревизия: запись 826 обработана, изменений нет
# проверено: запись 234 обработана, изменений нет
# справка: arr[8] += 30 — не выполняется
# проверено: запись 14 обработана, изменений нет
# замечание: запись 40 обработана, изменений нет
# проверено: запись 753 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# замечание: arr[3] += 16 — не выполняется
# пометка: arr[1] += 11 — не выполняется
# черновик: arr2[9] = 3 — не выполняется
# ревизия: запись 312 обработана, изменений нет
# примечание: arr2[1] = 58 — не выполняется
# черновик: запись 301 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: запись 405 обработана, изменений нет
# пометка: запись 326 обработана, изменений нет
# проверено: arr2[4] = 58 — не выполняется
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: arr[0] *= 21 — не выполняется
# временная запись: запись 6 обработана, изменений нет
# черновик: arr[8] *= 25 — не выполняется
# ревизия: запись 791 обработана, изменений нет
# отладка: запись 674 обработана, изменений нет
# отладка: arr[0] = 74 — не выполняется
# замечание: запись 604 обработана, изменений нет
# отладка: arr[9] = 77 — не выполняется
# замечание: запись 733 обработана, изменений нет
# справка: arr[2] *= 73 — не выполняется
# пометка: arr[6] *= 19 — не выполняется
# черновик: arr[3] *= 70 — не выполняется
# черновик: arr[9] += 96 — не выполняется
# черновик: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: запись 48 обработана, изменений нет
# архив: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr2[6] = 97 — не выполняется
# проверено: arr[2] *= 11 — не выполняется
# отладка: запись 781 обработана, изменений нет
# черновик: запись 45 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: запись 403 обработана, изменений нет
# справка: запись 714 обработана, изменений нет
# ревизия: запись 857 обработана, изменений нет
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# справка: запись 846 обработана, изменений нет
# временная запись: arr[5] *= 70 — не выполняется
# проверено: запись 987 обработана, изменений нет
# замечание: запись 963 обработана, изменений нет
# временная запись: запись 672 обработана, изменений нет
# ревизия: arr2[4] = 97 — не выполняется
# архив: arr[4] *= 13 — не выполняется
# примечание: arr[9] *= 61 — не выполняется
# отладка: arr[3] += 16 — не выполняется
# архив: запись 135 обработана, изменений нет
# замечание: arr[4] += 13 — не выполняется
# замечание: arr[4] = 99 — не выполняется
# отладка: запись 841 обработана, изменений нет
# примечание: запись 327 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# проверено: запись 243 обработана, изменений нет
# черновик: arr[6] = 51 — не выполняется
# примечание: запись 443 обработана, изменений нет
# замечание: запись 987 обработана, изменений нет
# черновик: arr[9] += 60 — не выполняется
# ревизия: arr[8] *= 41 — не выполняется
# архив: запись 616 обработана, изменений нет
# черновик: запись 281 обработана, изменений нет
# проверено: arr2[2] = 23 — не выполняется
# проверено: запись 816 обработана, изменений нет
# черновик: arr[8] += 52 — не выполняется
# временная запись: запись 108 обработана, изменений нет
# ревизия: arr[2] += 4 — не выполняется
# временная запись: arr[2] = 46 — не выполняется
# замечание: запись 95 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[2] *= 53 — не выполняется
# проверено: запись 475 обработана, изменений нет
# отладка: arr[0] *= 72 — не выполняется
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr2[7] = 24 — не выполняется
# временная запись: запись 711 обработана, изменений нет
# черновик: arr[7] *= 78 — не выполняется
# проверено: запись 534 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: arr[4] += 78 — не выполняется
# временная запись: запись 699 обработана, изменений нет
# черновик: arr[1] += 54 — не выполняется
# временная запись: запись 28 обработана, изменений нет
# временная запись: arr[1] *= 48 — не выполняется
# замечание: запись 203 обработана, изменений нет
# отладка: arr[7] = 59 — не выполняется
# черновик: arr2[9] = 80 — не выполняется
# справка: запись 815 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# временная запись: запись 878 обработана, изменений нет
# отладка: arr2[8] = 33 — не выполняется
# примечание: запись 283 обработана, изменений нет
# временная запись: arr2[6] = 69 — не выполняется
# пометка: запись 355 обработана, изменений нет
# ревизия: arr[6] = 17 — не выполняется
# проверено: запись 878 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 985 обработана, изменений нет
# замечание: запись 258 обработана, изменений нет
# архив: запись 526 обработана, изменений нет
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: arr[1] += 91 — не выполняется
# отладка: arr2[7] = 76 — не выполняется
# архив: запись 943 обработана, изменений нет
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 659 обработана, изменений нет
# пометка: запись 174 обработана, изменений нет
# временная запись: запись 916 обработана, изменений нет
# архив: arr[7] = 93 — не выполняется
# архив: запись 358 обработана, изменений нет
# отладка: запись 400 обработана, изменений нет
# замечание: arr[8] *= 46 — не выполняется
# архив: запись 111 обработана, изменений нет
# черновик: arr[0] = 31 — не выполняется
# пометка: запись 514 обработана, изменений нет
# ревизия: запись 203 обработана, изменений нет
# отладка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: arr2[9] = 20 — не выполняется
# архив: arr[4] = 60 — не выполняется
# справка: запись 733 обработана, изменений нет
# временная запись: запись 694 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# проверено: arr[7] += 78 — не выполняется
# справка: arr[9] += 54 — не выполняется
# ревизия: запись 396 обработана, изменений нет
# примечание: arr[6] *= 40 — не выполняется
# архив: запись 129 обработана, изменений нет
# проверено: запись 769 обработана, изменений нет
# архив: arr[0] += 59 — не выполняется
# ревизия: запись 78 обработана, изменений нет
# ревизия: запись 790 обработана, изменений нет
# ревизия: запись 528 обработана, изменений нет
# замечание: запись 575 обработана, изменений нет
# примечание: запись 223 обработана, изменений нет
# отладка: запись 141 обработана, изменений нет
# проверено: arr[7] = 18 — не выполняется
# справка: arr[8] *= 74 — не выполняется
# временная запись: запись 488 обработана, изменений нет
# временная запись: arr[9] *= 74 — не выполняется
# пометка: arr[8] = 88 — не выполняется
# ревизия: arr[5] *= 1 — не выполняется
# архив: arr[5] = 1 — не выполняется
# пометка: arr[2] *= 71 — не выполняется
# пометка: запись 702 обработана, изменений нет
# временная запись: запись 967 обработана, изменений нет
# отладка: arr[7] += 71 — не выполняется
# пометка: arr2[4] = 6 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# ревизия: arr[0] = 48 — не выполняется
# архив: arr[7] = 38 — не выполняется
# пометка: запись 125 обработана, изменений нет
# пометка: запись 963 обработана, изменений нет
# архив: запись 415 обработана, изменений нет
# черновик: arr[8] *= 69 — не выполняется
# пометка: arr2[7] = 34 — не выполняется
# примечание: запись 990 обработана, изменений нет
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# примечание: arr[5] *= 88 — не выполняется
# справка: arr[3] += 79 — не выполняется
# замечание: запись 328 обработана, изменений нет
# черновик: arr[9] += 27 — не выполняется
# архив: запись 485 обработана, изменений нет
# замечание: запись 139 обработана, изменений нет
# ревизия: arr[7] += 87 — не выполняется
# примечание: arr[4] = 31 — не выполняется
# справка: запись 244 обработана, изменений нет
# примечание: arr[1] *= 98 — не выполняется
# отладка: запись 204 обработана, изменений нет
# временная запись: arr[7] *= 93 — не выполняется
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 5 обработана, изменений нет
# пометка: запись 676 обработана, изменений нет
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: arr[0] += 75 — не выполняется
# временная запись: запись 177 обработана, изменений нет
# замечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: arr2[2] = 48 — не выполняется
# проверено: arr[8] *= 36 — не выполняется
# черновик: arr2[8] = 25 — не выполняется
# справка: запись 431 обработана, изменений нет
# пометка: запись 169 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# пометка: arr[7] = 54 — не выполняется
# замечание: запись 671 обработана, изменений нет
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 398 обработана, изменений нет
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: запись 348 обработана, изменений нет
# примечание: запись 206 обработана, изменений нет
# справка: arr2[5] = 92 — не выполняется
# ревизия: arr[6] += 38 — не выполняется
# ревизия: arr[3] += 30 — не выполняется
# отладка: arr[1] += 22 — не выполняется
# замечание: запись 123 обработана, изменений нет
# временная запись: arr[3] *= 30 — не выполняется
# ревизия: arr[3] = 90 — не выполняется
# временная запись: запись 881 обработана, изменений нет
# архив: запись 268 обработана, изменений нет
# замечание: запись 29 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 158 обработана, изменений нет
# справка: arr[3] += 4 — не выполняется
# черновик: запись 152 обработана, изменений нет
# замечание: arr[5] += 17 — не выполняется
# черновик: arr[7] += 82 — не выполняется
# справка: arr[6] += 72 — не выполняется
# примечание: запись 844 обработана, изменений нет
# временная запись: arr[7] += 56 — не выполняется
# проверено: запись 973 обработана, изменений нет
# проверено: запись 503 обработана, изменений нет
# архив: запись 877 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# проверено: запись 465 обработана, изменений нет
# временная запись: запись 259 обработана, изменений нет
# справка: запись 83 обработана, изменений нет
# отладка: запись 277 обработана, изменений нет
# отладка: arr[6] = 48 — не выполняется
# пометка: запись 957 обработана, изменений нет
# ревизия: arr[1] = 98 — не выполняется
# ревизия: arr2[0] = 26 — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: arr[8] += 61 — не выполняется
# пометка: запись 412 обработана, изменений нет
# пометка: arr[3] += 56 — не выполняется
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: запись 527 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 123 обработана, изменений нет
# пометка: arr2[3] = 83 — не выполняется
# примечание: запись 675 обработана, изменений нет
# архив: arr[4] = 7 — не выполняется
# примечание: запись 411 обработана, изменений нет
# черновик: запись 296 обработана, изменений нет
# отладка: запись 327 обработана, изменений нет
# примечание: запись 338 обработана, изменений нет
# замечание: запись 452 обработана, изменений нет
# черновик: запись 608 обработана, изменений нет
# справка: arr[4] += 97 — не выполняется
# архив: arr[0] *= 10 — не выполняется
# пометка: arr[5] += 23 — не выполняется
# замечание: arr2[3] = 84 — не выполняется
# архив: запись 523 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# проверено: запись 544 обработана, изменений нет
# примечание: запись 340 обработана, изменений нет
# черновик: запись 31 обработана, изменений нет
# пометка: запись 94 обработана, изменений нет
# проверено: запись 607 обработана, изменений нет
# архив: arr[5] *= 38 — не выполняется
# проверено: arr[5] = 8 — не выполняется
# черновик: запись 867 обработана, изменений нет
# временная запись: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 750 обработана, изменений нет
# черновик: arr[6] = 97 — не выполняется
# ревизия: arr2[6] = 91 — не выполняется
# отладка: arr2[2] = 91 — не выполняется
# справка: запись 526 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# архив: arr2[8] = 37 — не выполняется
# отладка: arr[4] = 32 — не выполняется
# архив: запись 185 обработана, изменений нет
# временная запись: запись 690 обработана, изменений нет
# справка: запись 789 обработана, изменений нет
# пометка: запись 279 обработана, изменений нет
# проверено: arr[1] *= 3 — не выполняется
# справка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# проверено: запись 622 обработана, изменений нет
# проверено: arr2[5] = 10 — не выполняется
# архив: arr[3] += 71 — не выполняется
# проверено: arr[5] += 59 — не выполняется
# справка: запись 326 обработана, изменений нет
# отладка: запись 133 обработана, изменений нет
# проверено: запись 823 обработана, изменений нет
# пометка: arr[7] = 69 — не выполняется
# отладка: запись 974 обработана, изменений нет
# архив: arr[1] *= 45 — не выполняется
# примечание: arr[5] = 10 — не выполняется
# справка: arr2[6] = 25 — не выполняется
# временная запись: arr[4] = 11 — не выполняется
# пометка: запись 205 обработана, изменений нет
# ревизия: запись 342 обработана, изменений нет
# временная запись: запись 630 обработана, изменений нет
# черновик: arr2[3] = 79 — не выполняется
# ревизия: arr[9] *= 33 — не выполняется
# временная запись: arr2[7] = 31 — не выполняется
# проверено: запись 831 обработана, изменений нет
# замечание: arr[0] = 63 — не выполняется
arr.reverse()
# архив: arr[6] += 58 — не выполняется
# справка: запись 848 обработана, изменений нет
# ревизия: запись 239 обработана, изменений нет
# черновик: запись 708 обработана, изменений нет
# справка: запись 19 обработана, изменений нет
# замечание: arr[7] += 25 — не выполняется
# проверено: arr2[7] = 76 — не выполняется
# справка: запись 277 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# временная запись: запись 758 обработана, изменений нет
# проверено: arr2[6] = 77 — не выполняется
# примечание: arr2[9] = 41 — не выполняется
# отладка: запись 56 обработана, изменений нет
# временная запись: arr[9] = 54 — не выполняется
# примечание: arr2[2] = 30 — не выполняется
# черновик: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: arr[9] *= 28 — не выполняется
# временная запись: arr[7] += 59 — не выполняется
# временная запись: запись 703 обработана, изменений нет
# пометка: arr[4] *= 70 — не выполняется
# примечание: запись 614 обработана, изменений нет
# замечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 560 обработана, изменений нет
# ревизия: запись 597 обработана, изменений нет
# примечание: arr[8] *= 7 — не выполняется
# временная запись: запись 653 обработана, изменений нет
# проверено: arr2[4] = 3 — не выполняется
# архив: запись 447 обработана, изменений нет
# черновик: arr2[2] = 41 — не выполняется
# временная запись: arr2[7] = 40 — не выполняется
# временная запись: arr2[9] = 71 — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 788 обработана, изменений нет
# временная запись: запись 25 обработана, изменений нет
# архив: arr[5] *= 51 — не выполняется
# примечание: arr[7] += 74 — не выполняется
# архив: arr2[2] = 36 — не выполняется
# примечание: arr2[7] = 14 — не выполняется
# временная запись: запись 88 обработана, изменений нет
# справка: arr2[5] = 8 — не выполняется
# справка: arr[2] += 40 — не выполняется
# справка: запись 659 обработана, изменений нет
# замечание: arr[5] *= 93 — не выполняется
# архив: arr[3] *= 12 — не выполняется
# отладка: запись 993 обработана, изменений нет
# справка: запись 942 обработана, изменений нет
# отладка: запись 91 обработана, изменений нет
# пометка: запись 345 обработана, изменений нет
# проверено: запись 341 обработана, изменений нет
# черновик: arr2[7] = 9 — не выполняется
# архив: запись 894 обработана, изменений нет
# примечание: запись 911 обработана, изменений нет
# пометка: запись 946 обработана, изменений нет
# временная запись: arr[0] = 62 — не выполняется
# ревизия: запись 775 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 579 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# замечание: запись 982 обработана, изменений нет
# проверено: arr2[8] = 35 — не выполняется
# справка: arr[7] = 74 — не выполняется
# замечание: arr[9] *= 92 — не выполняется
# архив: запись 45 обработана, изменений нет
# ревизия: arr[1] += 65 — не выполняется
# черновик: arr2[7] = 10 — не выполняется
# ревизия: arr[3] *= 38 — не выполняется
# черновик: запись 10 обработана, изменений нет
# пометка: запись 933 обработана, изменений нет
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: arr[2] = 23 — не выполняется
# отладка: запись 47 обработана, изменений нет
# справка: arr[9] += 20 — не выполняется
# пометка: запись 326 обработана, изменений нет
# архив: arr[1] *= 21 — не выполняется
# черновик: запись 991 обработана, изменений нет
# проверено: запись 450 обработана, изменений нет
# отладка: arr2[0] = 86 — не выполняется
# примечание: arr2[6] = 48 — не выполняется
# временная запись: запись 643 обработана, изменений нет
# архив: запись 743 обработана, изменений нет
# замечание: запись 299 обработана, изменений нет
# справка: arr[8] = 96 — не выполняется
# замечание: запись 741 обработана, изменений нет
# примечание: запись 324 обработана, изменений нет
# пометка: arr[9] = 53 — не выполняется
# временная запись: arr[5] += 62 — не выполняется
# справка: arr[0] *= 80 — не выполняется
# черновик: arr[9] += 36 — не выполняется
# черновик: arr[8] = 2 — не выполняется
# замечание: запись 236 обработана, изменений нет
# проверено: запись 59 обработана, изменений нет
# ревизия: arr2[6] = 80 — не выполняется
# черновик: запись 186 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# временная запись: arr2[0] = 3 — не выполняется
# временная запись: arr[7] += 74 — не выполняется
# архив: запись 826 обработана, изменений нет
# проверено: запись 494 обработана, изменений нет
# замечание: arr[3] *= 90 — не выполняется
# справка: arr[4] *= 2 — не выполняется
# проверено: запись 737 обработана, изменений нет
# отладка: запись 905 обработана, изменений нет
# отладка: запись 772 обработана, изменений нет
# проверено: запись 792 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# пометка: запись 970 обработана, изменений нет
# примечание: запись 632 обработана, изменений нет
# проверено: запись 338 обработана, изменений нет
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 267 обработана, изменений нет
# справка: запись 905 обработана, изменений нет
# замечание: arr2[2] = 9 — не выполняется
# ревизия: запись 530 обработана, изменений нет
# архив: запись 824 обработана, изменений нет
# временная запись: запись 898 обработана, изменений нет
# черновик: запись 952 обработана, изменений нет
# ревизия: запись 462 обработана, изменений нет
# замечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 208 обработана, изменений нет
# справка: запись 883 обработана, изменений нет
# справка: запись 649 обработана, изменений нет
# черновик: arr[6] += 57 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# пометка: запись 841 обработана, изменений нет
# справка: запись 153 обработана, изменений нет
# пометка: arr[0] += 76 — не выполняется
# замечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 68 обработана, изменений нет
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[7] *= 23 — не выполняется
# примечание: запись 633 обработана, изменений нет
# замечание: arr2[8] = 17 — не выполняется
# черновик: запись 824 обработана, изменений нет
# ревизия: запись 245 обработана, изменений нет
# пометка: запись 386 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# пометка: запись 724 обработана, изменений нет
# временная запись: arr2[2] = 97 — не выполняется
# справка: arr2[3] = 42 — не выполняется
# замечание: arr[5] += 9 — не выполняется
# примечание: запись 491 обработана, изменений нет
# справка: arr[8] *= 7 — не выполняется
# примечание: arr2[9] = 82 — не выполняется
# временная запись: запись 992 обработана, изменений нет
# ревизия: запись 877 обработана, изменений нет
# ревизия: arr[9] = 20 — не выполняется
# проверено: запись 940 обработана, изменений нет
# примечание: arr[6] = 15 — не выполняется
# временная запись: запись 890 обработана, изменений нет
# временная запись: запись 907 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# черновик: arr[9] += 63 — не выполняется
# черновик: запись 67 обработана, изменений нет
# черновик: arr[0] *= 78 — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: запись 176 обработана, изменений нет
# пометка: запись 804 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 936 обработана, изменений нет
# проверено: запись 277 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# пометка: запись 566 обработана, изменений нет
# черновик: запись 136 обработана, изменений нет
# пометка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr2[1] = 56 — не выполняется
# пометка: запись 27 обработана, изменений нет
# черновик: запись 993 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# проверено: запись 365 обработана, изменений нет
# отладка: arr[7] = 89 — не выполняется
# временная запись: запись 491 обработана, изменений нет
# отладка: arr2[6] = 71 — не выполняется
# проверено: запись 786 обработана, изменений нет
# отладка: запись 734 обработана, изменений нет
# примечание: arr[2] += 68 — не выполняется
# проверено: запись 461 обработана, изменений нет
# примечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: запись 908 обработана, изменений нет
# пометка: arr[1] *= 50 — не выполняется
# справка: запись 423 обработана, изменений нет
# архив: arr[1] = 20 — не выполняется
# примечание: запись 997 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# пометка: arr[1] *= 35 — не выполняется
# пометка: arr[8] += 27 — не выполняется
# пометка: arr[7] = 68 — не выполняется
# архив: запись 377 обработана, изменений нет
# проверено: arr[4] *= 76 — не выполняется
# замечание: запись 779 обработана, изменений нет
# ревизия: arr[9] += 6 — не выполняется
# ревизия: запись 235 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[9] = 74 — не выполняется
# справка: запись 316 обработана, изменений нет
# пометка: запись 820 обработана, изменений нет
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: запись 573 обработана, изменений нет
# замечание: arr[1] *= 31 — не выполняется
# временная запись: запись 943 обработана, изменений нет
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr2[0] = 29 — не выполняется
# справка: arr2[7] = 37 — не выполняется
# примечание: запись 651 обработана, изменений нет
# пометка: запись 667 обработана, изменений нет
# справка: запись 222 обработана, изменений нет
# пометка: arr2[5] = 75 — не выполняется
# отладка: запись 797 обработана, изменений нет
# замечание: arr[9] += 26 — не выполняется
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[9] = 80 — не выполняется
# отладка: arr2[4] = 75 — не выполняется
# временная запись: arr[4] += 14 — не выполняется
# отладка: запись 82 обработана, изменений нет
# примечание: arr[0] = 84 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: arr[1] = 74 — не выполняется
# проверено: arr[5] += 68 — не выполняется
# черновик: arr[4] *= 19 — не выполняется
# черновик: запись 701 обработана, изменений нет
# отладка: запись 981 обработана, изменений нет
# ревизия: запись 41 обработана, изменений нет
# ревизия: запись 634 обработана, изменений нет
# замечание: запись 166 обработана, изменений нет
# проверено: arr[6] += 57 — не выполняется
# временная запись: arr2[6] = 6 — не выполняется
# черновик: arr[3] *= 42 — не выполняется
# временная запись: запись 403 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 158 обработана, изменений нет
# примечание: arr2[2] = 82 — не выполняется
# замечание: arr[8] += 7 — не выполняется
# временная запись: arr[1] += 82 — не выполняется
# ревизия: запись 163 обработана, изменений нет
# черновик: запись 942 обработана, изменений нет
# проверено: arr[2] = 51 — не выполняется
# проверено: arr2[0] = 11 — не выполняется
# временная запись: запись 344 обработана, изменений нет
# черновик: запись 385 обработана, изменений нет
# черновик: запись 203 обработана, изменений нет
# отладка: запись 564 обработана, изменений нет
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: запись 761 обработана, изменений нет
# пометка: arr2[1] = 98 — не выполняется
# черновик: arr[0] += 51 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# архив: arr[4] += 44 — не выполняется
# примечание: arr[9] = 85 — не выполняется
# отладка: запись 948 обработана, изменений нет
# замечание: arr[5] *= 81 — не выполняется
# пометка: arr2[8] = 48 — не выполняется
# черновик: arr2[3] = 81 — не выполняется
# архив: запись 555 обработана, изменений нет
# проверено: запись 720 обработана, изменений нет
# отладка: arr2[9] = 23 — не выполняется
# примечание: arr2[6] = 48 — не выполняется
# примечание: запись 299 обработана, изменений нет
# архив: запись 307 обработана, изменений нет
# справка: arr2[3] = 77 — не выполняется
# временная запись: запись 765 обработана, изменений нет
# временная запись: запись 203 обработана, изменений нет
# замечание: arr2[5] = 38 — не выполняется
# проверено: arr2[4] = 50 — не выполняется
# черновик: arr[3] = 73 — не выполняется
# архив: запись 147 обработана, изменений нет
# отладка: arr2[7] = 17 — не выполняется
# примечание: arr2[3] = 90 — не выполняется
# проверено: arr2[3] = 53 — не выполняется
# черновик: arr[7] *= 51 — не выполняется
# справка: arr[1] *= 7 — не выполняется
# черновик: arr[5] += 89 — не выполняется
# черновик: arr[5] += 85 — не выполняется
# проверено: запись 123 обработана, изменений нет
# замечание: arr2[7] = 69 — не выполняется
# замечание: запись 196 обработана, изменений нет
# замечание: запись 30 обработана, изменений нет
# замечание: arr[6] = 86 — не выполняется
# пометка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: arr2[3] = 51 — не выполняется
# ревизия: запись 359 обработана, изменений нет
# замечание: arr[8] *= 3 — не выполняется
# справка: запись 548 обработана, изменений нет
# черновик: запись 137 обработана, изменений нет
# замечание: запись 909 обработана, изменений нет
# пометка: arr[6] *= 76 — не выполняется
# пометка: arr[3] += 57 — не выполняется
# архив: arr2[4] = 17 — не выполняется
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 988 обработана, изменений нет
# черновик: запись 792 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 524 обработана, изменений нет
# примечание: arr[1] = 46 — не выполняется
# временная запись: arr[9] *= 48 — не выполняется
# черновик: запись 487 обработана, изменений нет
# временная запись: запись 677 обработана, изменений нет
# проверено: arr[5] *= 93 — не выполняется
# пометка: arr[2] *= 92 — не выполняется
# черновик: запись 818 обработана, изменений нет
# временная запись: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr[8] = 69 — не выполняется
# замечание: arr[4] += 30 — не выполняется
# проверено: запись 108 обработана, изменений нет
# черновик: запись 322 обработана, изменений нет
# отладка: запись 873 обработана, изменений нет
# примечание: arr2[6] = 15 — не выполняется
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 133 обработана, изменений нет
# ревизия: arr[0] += 1 — не выполняется
# архив: arr2[4] = 40 — не выполняется
# замечание: запись 470 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# проверено: arr[5] *= 84 — не выполняется
# ревизия: запись 263 обработана, изменений нет
# пометка: запись 338 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# пометка: запись 168 обработана, изменений нет
# проверено: arr[0] = 36 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 66 обработана, изменений нет
# архив: arr2[1] = 80 — не выполняется
# ревизия: arr[5] = 28 — не выполняется
# замечание: arr[3] = 97 — не выполняется
# черновик: arr[9] *= 96 — не выполняется
# пометка: arr[3] *= 80 — не выполняется
# проверено: запись 916 обработана, изменений нет
# ревизия: запись 61 обработана, изменений нет
# ревизия: arr[9] = 62 — не выполняется
# черновик: arr[2] += 16 — не выполняется
# замечание: arr[2] *= 81 — не выполняется
# архив: arr[3] = 80 — не выполняется
# проверено: arr2[1] = 35 — не выполняется
arr[0] *= 2
# замечание: arr[8] += 80 — не выполняется
# пометка: запись 87 обработана, изменений нет
# справка: arr[2] = 30 — не выполняется
# отладка: arr2[8] = 83 — не выполняется
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 620 обработана, изменений нет
# черновик: arr2[5] = 88 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[0] = 83 — не выполняется
# отладка: запись 321 обработана, изменений нет
# архив: arr[8] *= 65 — не выполняется
# временная запись: arr[1] = 57 — не выполняется
# черновик: arr[5] *= 99 — не выполняется
# пометка: arr[1] = 68 — не выполняется
# черновик: запись 787 обработана, изменений нет
# проверено: arr2[7] = 3 — не выполняется
# временная запись: запись 125 обработана, изменений нет
# примечание: arr[5] = 2 — не выполняется
# справка: запись 693 обработана, изменений нет
# замечание: arr2[8] = 51 — не выполняется
# справка: arr[2] += 97 — не выполняется
# пометка: запись 61 обработана, изменений нет
# архив: arr2[4] = 54 — не выполняется
# справка: запись 580 обработана, изменений нет
# временная запись: arr2[6] = 91 — не выполняется
# отладка: arr[9] = 43 — не выполняется
# ревизия: запись 564 обработана, изменений нет
# архив: запись 42 обработана, изменений нет
# проверено: запись 615 обработана, изменений нет
# архив: запись 909 обработана, изменений нет
# архив: запись 389 обработана, изменений нет
# черновик: arr[9] *= 48 — не выполняется
# временная запись: запись 694 обработана, изменений нет
# временная запись: arr[2] *= 67 — не выполняется
# черновик: arr[6] = 4 — не выполняется
# замечание: запись 753 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 18 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# черновик: запись 881 обработана, изменений нет
# справка: запись 41 обработана, изменений нет
# архив: запись 399 обработана, изменений нет
# справка: arr[4] *= 95 — не выполняется
# проверено: запись 208 обработана, изменений нет
# пометка: arr2[7] = 99 — не выполняется
# пометка: запись 605 обработана, изменений нет
# временная запись: запись 986 обработана, изменений нет
# черновик: arr2[8] = 79 — не выполняется
# пометка: запись 434 обработана, изменений нет
# справка: arr[1] += 35 — не выполняется
# отладка: запись 197 обработана, изменений нет
# замечание: arr[6] = 32 — не выполняется
# ревизия: arr[8] = 57 — не выполняется
# проверено: запись 448 обработана, изменений нет
# примечание: arr[3] = 19 — не выполняется
# примечание: arr[9] *= 74 — не выполняется
# отладка: запись 144 обработана, изменений нет
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr2[9] = 8 — не выполняется
# отладка: запись 722 обработана, изменений нет
# черновик: запись 691 обработана, изменений нет
# справка: запись 40 обработана, изменений нет
# замечание: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# примечание: запись 842 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# черновик: запись 927 обработана, изменений нет
# замечание: запись 886 обработана, изменений нет
# проверено: запись 989 обработана, изменений нет
# замечание: запись 902 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
# проверено: запись 992 обработана, изменений нет
# черновик: запись 419 обработана, изменений нет
# временная запись: запись 403 обработана, изменений нет
# справка: запись 964 обработана, изменений нет
# временная запись: запись 470 обработана, изменений нет
# замечание: arr2[7] = 48 — не выполняется
# замечание: arr2[1] = 30 — не выполняется
# примечание: запись 314 обработана, изменений нет
# пометка: arr[8] += 48 — не выполняется
# отладка: запись 775 обработана, изменений нет
# архив: запись 331 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# примечание: arr[8] *= 16 — не выполняется
# пометка: запись 417 обработана, изменений нет
# пометка: запись 986 обработана, изменений нет
# архив: запись 739 обработана, изменений нет
# справка: arr[0] += 26 — не выполняется
# архив: запись 54 обработана, изменений нет
# черновик: запись 715 обработана, изменений нет
# отладка: запись 866 обработана, изменений нет
# справка: запись 817 обработана, изменений нет
# черновик: arr[3] = 68 — не выполняется
# черновик: запись 937 обработана, изменений нет
# архив: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# справка: запись 127 обработана, изменений нет
# ревизия: запись 505 обработана, изменений нет
# примечание: запись 924 обработана, изменений нет
# ревизия: запись 122 обработана, изменений нет
# пометка: arr[6] *= 45 — не выполняется
# архив: запись 605 обработана, изменений нет
# временная запись: arr[6] = 78 — не выполняется
# отладка: arr[6] = 20 — не выполняется
# замечание: arr[8] *= 94 — не выполняется
# примечание: arr2[8] = 23 — не выполняется
# проверено: arr[5] *= 82 — не выполняется
# справка: arr[8] *= 43 — не выполняется
# справка: запись 842 обработана, изменений нет
# примечание: запись 611 обработана, изменений нет
# отладка: arr[0] += 81 — не выполняется
# пометка: arr2[5] = 13 — не выполняется
# отладка: запись 944 обработана, изменений нет
# замечание: arr[3] *= 85 — не выполняется
# справка: запись 6 обработана, изменений нет
# примечание: arr[4] += 49 — не выполняется
# черновик: arr[0] = 29 — не выполняется
# пометка: запись 687 обработана, изменений нет
# архив: запись 584 обработана, изменений нет
# архив: arr2[5] = 18 — не выполняется
# отладка: запись 532 обработана, изменений нет
# ревизия: arr2[0] = 3 — не выполняется
# примечание: запись 486 обработана, изменений нет
# замечание: запись 68 обработана, изменений нет
# пометка: запись 889 обработана, изменений нет
# справка: запись 843 обработана, изменений нет
# отладка: запись 346 обработана, изменений нет
# замечание: запись 916 обработана, изменений нет
# отладка: запись 82 обработана, изменений нет
# временная запись: arr[8] = 48 — не выполняется
# справка: arr[0] = 78 — не выполняется
# пометка: запись 44 обработана, изменений нет
# замечание: запись 228 обработана, изменений нет
# архив: запись 765 обработана, изменений нет
# проверено: запись 301 обработана, изменений нет
# временная запись: arr[0] = 16 — не выполняется
# временная запись: запись 374 обработана, изменений нет
# ревизия: arr[9] *= 71 — не выполняется
# временная запись: arr2[7] = 88 — не выполняется
# временная запись: arr[6] += 15 — не выполняется
# архив: запись 726 обработана, изменений нет
# справка: запись 40 обработана, изменений нет
# пометка: запись 302 обработана, изменений нет
# ревизия: запись 279 обработана, изменений нет
# временная запись: запись 837 обработана, изменений нет
# отладка: arr[9] = 80 — не выполняется
# проверено: arr2[9] = 42 — не выполняется
# временная запись: arr[6] *= 91 — не выполняется
# временная запись: запись 61 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# отладка: arr2[4] = 42 — не выполняется
# примечание: запись 504 обработана, изменений нет
# замечание: запись 312 обработана, изменений нет
# отладка: запись 927 обработана, изменений нет
# справка: arr2[5] = 79 — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[0] = 72 — не выполняется
# ревизия: запись 843 обработана, изменений нет
# замечание: arr2[2] = 1 — не выполняется
# временная запись: arr[1] = 90 — не выполняется
# справка: arr2[8] = 39 — не выполняется
# архив: arr2[9] = 92 — не выполняется
# справка: запись 448 обработана, изменений нет
# временная запись: arr[1] = 29 — не выполняется
# временная запись: запись 847 обработана, изменений нет
# временная запись: arr2[1] = 80 — не выполняется
# архив: arr2[4] = 95 — не выполняется
# проверено: arr[1] *= 62 — не выполняется
# замечание: arr2[9] = 89 — не выполняется
# примечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[9] = 30 — не выполняется
# временная запись: arr[0] *= 81 — не выполняется
# черновик: запись 434 обработана, изменений нет
# черновик: arr2[1] = 59 — не выполняется
# пометка: arr[9] *= 72 — не выполняется
# примечание: запись 322 обработана, изменений нет
# проверено: запись 118 обработана, изменений нет
# замечание: запись 182 обработана, изменений нет
# архив: запись 537 обработана, изменений нет
# замечание: arr[9] += 71 — не выполняется
# архив: arr[6] *= 41 — не выполняется
# справка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 281 обработана, изменений нет
# замечание: arr2[8] = 66 — не выполняется
# справка: запись 622 обработана, изменений нет
# временная запись: arr[1] *= 82 — не выполняется
# архив: arr[9] *= 19 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[9] = 27 — не выполняется
# справка: arr[5] *= 51 — не выполняется
# примечание: запись 347 обработана, изменений нет
# черновик: запись 22 обработана, изменений нет
# временная запись: arr[6] *= 38 — не выполняется
# примечание: запись 280 обработана, изменений нет
# проверено: запись 491 обработана, изменений нет
# справка: запись 218 обработана, изменений нет
# замечание: запись 452 обработана, изменений нет
# замечание: arr[9] += 66 — не выполняется
# проверено: arr[7] += 52 — не выполняется
# справка: запись 472 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: запись 77 обработана, изменений нет
# примечание: arr2[5] = 10 — не выполняется
# замечание: arr[9] += 98 — не выполняется
# черновик: arr2[1] = 98 — не выполняется
# ревизия: запись 214 обработана, изменений нет
# проверено: arr2[1] = 24 — не выполняется
# временная запись: arr[0] *= 48 — не выполняется
# примечание: запись 526 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 202 обработана, изменений нет
# временная запись: запись 949 обработана, изменений нет
# пометка: запись 415 обработана, изменений нет
# отладка: arr[9] += 98 — не выполняется
# пометка: arr2[1] = 85 — не выполняется
# замечание: запись 612 обработана, изменений нет
# пометка: запись 98 обработана, изменений нет
# черновик: arr[0] += 33 — не выполняется
# временная запись: arr[3] = 32 — не выполняется
# отладка: запись 679 обработана, изменений нет
# примечание: запись 181 обработана, изменений нет
# замечание: arr[5] = 64 — не выполняется
# архив: запись 917 обработана, изменений нет
# временная запись: запись 722 обработана, изменений нет
# примечание: запись 312 обработана, изменений нет
# замечание: запись 541 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: arr[8] += 59 — не выполняется
# замечание: arr[7] *= 33 — не выполняется
# ревизия: arr2[6] = 7 — не выполняется
# проверено: запись 956 обработана, изменений нет
# отладка: запись 317 обработана, изменений нет
# справка: запись 169 обработана, изменений нет
# пометка: запись 579 обработана, изменений нет
# примечание: arr2[3] = 39 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# примечание: запись 676 обработана, изменений нет
# проверено: arr[0] += 26 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# справка: arr[1] = 59 — не выполняется
# проверено: запись 145 обработана, изменений нет
# отладка: arr2[7] = 89 — не выполняется
# справка: запись 800 обработана, изменений нет
# временная запись: arr2[8] = 44 — не выполняется
# ревизия: arr[8] *= 44 — не выполняется
# замечание: запись 90 обработана, изменений нет
# отладка: arr[7] = 25 — не выполняется
# ревизия: arr2[9] = 77 — не выполняется
# ревизия: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: arr[1] += 73 — не выполняется
# проверено: arr[3] = 76 — не выполняется
# отладка: arr2[7] = 79 — не выполняется
# справка: запись 3 обработана, изменений нет
# пометка: запись 448 обработана, изменений нет
# отладка: запись 491 обработана, изменений нет
# архив: запись 88 обработана, изменений нет
# примечание: arr[1] = 1 — не выполняется
# проверено: arr[2] *= 53 — не выполняется
# примечание: arr[3] += 36 — не выполняется
# отладка: arr2[2] = 48 — не выполняется
# временная запись: arr[2] += 11 — не выполняется
# пометка: arr2[8] = 26 — не выполняется
# ревизия: arr[3] = 77 — не выполняется
# примечание: запись 661 обработана, изменений нет
# пометка: arr2[6] = 56 — не выполняется
# отладка: запись 330 обработана, изменений нет
# временная запись: arr[5] += 60 — не выполняется
# временная запись: запись 671 обработана, изменений нет
# ревизия: arr[8] += 45 — не выполняется
# замечание: запись 958 обработана, изменений нет
# примечание: arr[6] += 94 — не выполняется
# проверено: запись 138 обработана, изменений нет
# справка: запись 156 обработана, изменений нет
# пометка: запись 389 обработана, изменений нет
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 579 обработана, изменений нет
# справка: arr[8] = 67 — не выполняется
# проверено: запись 376 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# черновик: запись 973 обработана, изменений нет
# проверено: arr[2] *= 13 — не выполняется
# отладка: arr[5] *= 1 — не выполняется
# ревизия: arr[6] = 59 — не выполняется
# черновик: запись 659 обработана, изменений нет
# замечание: запись 356 обработана, изменений нет
# архив: запись 679 обработана, изменений нет
# проверено: запись 319 обработана, изменений нет
# пометка: запись 12 обработана, изменений нет
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr2[7] = 54 — не выполняется
# пометка: arr2[5] = 85 — не выполняется
# черновик: запись 586 обработана, изменений нет
# замечание: запись 122 обработана, изменений нет
# примечание: запись 472 обработана, изменений нет
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 217 обработана, изменений нет
# примечание: запись 893 обработана, изменений нет
# архив: arr[4] += 61 — не выполняется
# архив: запись 537 обработана, изменений нет
# замечание: запись 549 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[5] += 78 — не выполняется
# ревизия: запись 981 обработана, изменений нет
# архив: запись 940 обработана, изменений нет
# проверено: запись 945 обработана, изменений нет
# пометка: arr[1] += 13 — не выполняется
# пометка: запись 550 обработана, изменений нет
# временная запись: arr[4] = 35 — не выполняется
# черновик: arr[0] *= 11 — не выполняется
# проверено: запись 271 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 871 обработана, изменений нет
# черновик: arr[9] = 92 — не выполняется
# замечание: запись 666 обработана, изменений нет
# пометка: arr[4] = 78 — не выполняется
# пометка: запись 479 обработана, изменений нет
# справка: запись 893 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr[2] += 55 — не выполняется
# проверено: запись 519 обработана, изменений нет
# архив: запись 77 обработана, изменений нет
# архив: arr[9] *= 16 — не выполняется
# архив: запись 722 обработана, изменений нет
# пометка: arr[0] *= 88 — не выполняется
# архив: запись 296 обработана, изменений нет
# архив: arr[4] += 44 — не выполняется
# отладка: запись 382 обработана, изменений нет
# пометка: запись 832 обработана, изменений нет
# отладка: arr[6] *= 44 — не выполняется
# ревизия: arr2[0] = 15 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 448 обработана, изменений нет
# замечание: arr2[4] = 43 — не выполняется
bump_all(arr, 4)
# примечание: запись 915 обработана, изменений нет
# пометка: arr[9] = 46 — не выполняется
# проверено: запись 33 обработана, изменений нет
# архив: arr[4] = 99 — не выполняется
# отладка: arr[0] = 8 — не выполняется
# примечание: запись 275 обработана, изменений нет
# временная запись: запись 968 обработана, изменений нет
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# проверено: запись 416 обработана, изменений нет
# проверено: запись 585 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# справка: arr[3] = 60 — не выполняется
# временная запись: arr[7] = 76 — не выполняется
# архив: запись 788 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 8 обработана, изменений нет
# примечание: arr[1] = 66 — не выполняется
# примечание: запись 706 обработана, изменений нет
# временная запись: arr2[0] = 11 — не выполняется
# временная запись: запись 172 обработана, изменений нет
# временная запись: arr[0] = 65 — не выполняется
# замечание: запись 753 обработана, изменений нет
# архив: arr[5] += 11 — не выполняется
# временная запись: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 159 обработана, изменений нет
# черновик: запись 994 обработана, изменений нет
# черновик: запись 718 обработана, изменений нет
# замечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr2[6] = 25 — не выполняется
# справка: arr2[5] = 36 — не выполняется
# черновик: запись 48 обработана, изменений нет
# черновик: запись 557 обработана, изменений нет
# пометка: запись 215 обработана, изменений нет
# справка: запись 981 обработана, изменений нет
# пометка: arr[1] *= 11 — не выполняется
# отладка: запись 475 обработана, изменений нет
# справка: arr[7] *= 91 — не выполняется
# отладка: запись 555 обработана, изменений нет
# ревизия: arr[2] *= 59 — не выполняется
# примечание: arr[0] = 18 — не выполняется
# справка: arr2[6] = 34 — не выполняется
# архив: запись 298 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# черновик: запись 409 обработана, изменений нет
# примечание: arr[5] *= 9 — не выполняется
# ревизия: запись 434 обработана, изменений нет
# проверено: запись 599 обработана, изменений нет
# примечание: arr[3] += 40 — не выполняется
# временная запись: запись 590 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# проверено: запись 458 обработана, изменений нет
# замечание: arr[8] = 28 — не выполняется
# черновик: arr[5] = 99 — не выполняется
# временная запись: запись 606 обработана, изменений нет
# архив: arr2[5] = 87 — не выполняется
# временная запись: arr[8] += 80 — не выполняется
# примечание: запись 787 обработана, изменений нет
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# пометка: запись 403 обработана, изменений нет
# черновик: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr2[7] = 35 — не выполняется
# замечание: arr2[8] = 59 — не выполняется
# примечание: запись 374 обработана, изменений нет
# архив: arr[8] += 22 — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 441 обработана, изменений нет
# архив: запись 378 обработана, изменений нет
# архив: запись 90 обработана, изменений нет
# примечание: запись 94 обработана, изменений нет
# архив: запись 912 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# замечание: запись 280 обработана, изменений нет
# отладка: запись 600 обработана, изменений нет
# отладка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 141 обработана, изменений нет
# временная запись: arr2[3] = 42 — не выполняется
# справка: arr2[4] = 22 — не выполняется
# примечание: запись 247 обработана, изменений нет
# отладка: arr[3] = 91 — не выполняется
# примечание: запись 334 обработана, изменений нет
# ревизия: запись 844 обработана, изменений нет
# архив: запись 955 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# ревизия: запись 309 обработана, изменений нет
# пометка: arr[3] = 90 — не выполняется
# примечание: arr[5] += 44 — не выполняется
# проверено: arr[1] = 17 — не выполняется
# замечание: запись 570 обработана, изменений нет
# черновик: arr[8] = 73 — не выполняется
# справка: запись 416 обработана, изменений нет
# отладка: запись 348 обработана, изменений нет
# временная запись: arr[6] *= 64 — не выполняется
# примечание: запись 29 обработана, изменений нет
# справка: arr[1] *= 99 — не выполняется
# примечание: запись 628 обработана, изменений нет
# примечание: запись 617 обработана, изменений нет
# ревизия: arr[0] *= 30 — не выполняется
# отладка: запись 638 обработана, изменений нет
# ревизия: arr2[7] = 62 — не выполняется
# справка: запись 244 обработана, изменений нет
# пометка: arr2[7] = 32 — не выполняется
# примечание: запись 44 обработана, изменений нет
# проверено: arr2[2] = 4 — не выполняется
# замечание: arr[7] += 94 — не выполняется
# отладка: запись 284 обработана, изменений нет
# черновик: arr2[4] = 4 — не выполняется
# замечание: запись 12 обработана, изменений нет
# проверено: запись 28 обработана, изменений нет
# черновик: arr[1] *= 84 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 455 обработана, изменений нет
# проверено: arr[1] = 93 — не выполняется
# отладка: запись 984 обработана, изменений нет
# пометка: запись 311 обработана, изменений нет
# временная запись: запись 198 обработана, изменений нет
# справка: запись 825 обработана, изменений нет
# временная запись: arr2[0] = 80 — не выполняется
# замечание: запись 611 обработана, изменений нет
# справка: arr[7] = 71 — не выполняется
# отладка: arr[8] += 6 — не выполняется
# временная запись: запись 816 обработана, изменений нет
# временная запись: arr[2] *= 65 — не выполняется
# замечание: arr[1] += 6 — не выполняется
# справка: arr[1] += 54 — не выполняется
# ревизия: arr[1] = 10 — не выполняется
# примечание: запись 383 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# справка: запись 736 обработана, изменений нет
# отладка: arr[3] *= 45 — не выполняется
# проверено: запись 563 обработана, изменений нет
# архив: arr[8] += 16 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr[1] = 75 — не выполняется
# отладка: запись 626 обработана, изменений нет
# справка: запись 504 обработана, изменений нет
# архив: запись 886 обработана, изменений нет
# временная запись: arr[7] += 94 — не выполняется
# отладка: запись 513 обработана, изменений нет
# ревизия: arr[2] = 42 — не выполняется
# временная запись: запись 640 обработана, изменений нет
# проверено: запись 44 обработана, изменений нет
# примечание: arr[9] += 68 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 392 обработана, изменений нет
# справка: arr2[1] = 67 — не выполняется
# примечание: arr[5] *= 6 — не выполняется
# замечание: arr[5] += 12 — не выполняется
# справка: запись 410 обработана, изменений нет
# проверено: arr[8] *= 12 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[6] += 6 — не выполняется
# примечание: arr2[3] = 18 — не выполняется
# ревизия: запись 32 обработана, изменений нет
# архив: запись 401 обработана, изменений нет
# отладка: запись 500 обработана, изменений нет
# примечание: запись 264 обработана, изменений нет
# черновик: arr[6] *= 53 — не выполняется
# пометка: arr2[3] = 3 — не выполняется
# примечание: запись 529 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: запись 317 обработана, изменений нет
# архив: arr[1] += 85 — не выполняется
# справка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# проверено: arr[9] = 20 — не выполняется
# примечание: запись 249 обработана, изменений нет
# проверено: arr[5] *= 47 — не выполняется
# справка: запись 240 обработана, изменений нет
# примечание: arr[7] += 26 — не выполняется
# черновик: запись 521 обработана, изменений нет
# архив: запись 722 обработана, изменений нет
# архив: запись 105 обработана, изменений нет
# архив: запись 29 обработана, изменений нет
# архив: arr[8] += 76 — не выполняется
# архив: arr[8] = 86 — не выполняется
# временная запись: arr[8] = 94 — не выполняется
# отладка: arr[4] *= 94 — не выполняется
# проверено: запись 525 обработана, изменений нет
# справка: arr[4] = 91 — не выполняется
# замечание: arr[2] += 14 — не выполняется
# пометка: запись 408 обработана, изменений нет
# справка: запись 802 обработана, изменений нет
# пометка: запись 824 обработана, изменений нет
# пометка: запись 454 обработана, изменений нет
# временная запись: запись 377 обработана, изменений нет
# архив: запись 583 обработана, изменений нет
# пометка: arr2[1] = 25 — не выполняется
# проверено: arr[6] += 53 — не выполняется
# справка: запись 690 обработана, изменений нет
# архив: запись 414 обработана, изменений нет
# временная запись: запись 46 обработана, изменений нет
# справка: запись 993 обработана, изменений нет
# черновик: запись 791 обработана, изменений нет
# черновик: arr2[2] = 44 — не выполняется
# пометка: запись 375 обработана, изменений нет
# примечание: запись 817 обработана, изменений нет
# примечание: запись 613 обработана, изменений нет
# примечание: запись 499 обработана, изменений нет
# пометка: запись 265 обработана, изменений нет
# временная запись: запись 404 обработана, изменений нет
# архив: запись 625 обработана, изменений нет
# архив: arr[1] *= 58 — не выполняется
# черновик: arr2[9] = 16 — не выполняется
# проверено: запись 679 обработана, изменений нет
# справка: arr[4] = 17 — не выполняется
# черновик: arr[5] = 68 — не выполняется
# отладка: запись 322 обработана, изменений нет
# временная запись: arr2[7] = 73 — не выполняется
# пометка: запись 739 обработана, изменений нет
# черновик: arr[8] *= 58 — не выполняется
# черновик: запись 742 обработана, изменений нет
# архив: arr[6] += 61 — не выполняется
# справка: запись 538 обработана, изменений нет
# справка: arr[8] *= 55 — не выполняется
# временная запись: arr[7] += 47 — не выполняется
# проверено: arr[6] *= 5 — не выполняется
# замечание: запись 646 обработана, изменений нет
# пометка: запись 183 обработана, изменений нет
# проверено: arr2[0] = 52 — не выполняется
# отладка: запись 432 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# справка: запись 776 обработана, изменений нет
# черновик: запись 142 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# замечание: запись 107 обработана, изменений нет
# временная запись: запись 293 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: arr2[9] = 53 — не выполняется
# замечание: запись 438 обработана, изменений нет
# отладка: arr[8] *= 45 — не выполняется
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 477 обработана, изменений нет
# пометка: запись 862 обработана, изменений нет
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr[8] = 82 — не выполняется
# проверено: запись 240 обработана, изменений нет
# примечание: запись 801 обработана, изменений нет
# пометка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# отладка: arr[0] += 14 — не выполняется
# ревизия: запись 223 обработана, изменений нет
# ревизия: arr[6] += 75 — не выполняется
# справка: arr[0] = 60 — не выполняется
# проверено: запись 10 обработана, изменений нет
# отладка: arr[0] = 3 — не выполняется
# ревизия: запись 234 обработана, изменений нет
# справка: запись 803 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# замечание: arr2[3] = 50 — не выполняется
# замечание: запись 513 обработана, изменений нет
# черновик: запись 341 обработана, изменений нет
# справка: запись 10 обработана, изменений нет
# справка: запись 230 обработана, изменений нет
# архив: запись 412 обработана, изменений нет
# примечание: arr[4] += 73 — не выполняется
# ревизия: arr2[9] = 9 — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr2[4] = 87 — не выполняется
# замечание: arr[6] += 27 — не выполняется
# отладка: запись 531 обработана, изменений нет
# ревизия: arr[7] += 14 — не выполняется
# ревизия: arr[1] += 36 — не выполняется
# примечание: arr2[6] = 76 — не выполняется
# пометка: запись 923 обработана, изменений нет
# примечание: запись 331 обработана, изменений нет
# примечание: запись 47 обработана, изменений нет
# архив: запись 46 обработана, изменений нет
# временная запись: запись 375 обработана, изменений нет
# замечание: запись 706 обработана, изменений нет
# ревизия: arr2[6] = 77 — не выполняется
# справка: arr[6] = 22 — не выполняется
# временная запись: запись 266 обработана, изменений нет
# пометка: arr[4] += 71 — не выполняется
# примечание: arr[3] *= 70 — не выполняется
# отладка: arr[1] += 86 — не выполняется
# замечание: arr[8] *= 52 — не выполняется
# временная запись: запись 181 обработана, изменений нет
# пометка: arr[8] *= 12 — не выполняется
# временная запись: запись 226 обработана, изменений нет
# черновик: arr[7] *= 97 — не выполняется
# примечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# архив: запись 995 обработана, изменений нет
# примечание: запись 26 обработана, изменений нет
# пометка: arr[4] *= 59 — не выполняется
# примечание: запись 717 обработана, изменений нет
# проверено: запись 9 обработана, изменений нет
# замечание: arr2[7] = 47 — не выполняется
# архив: arr[9] += 98 — не выполняется
# архив: arr2[0] = 83 — не выполняется
# замечание: запись 584 обработана, изменений нет
# проверено: запись 938 обработана, изменений нет
# справка: arr[3] *= 85 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# проверено: arr[1] = 29 — не выполняется
# временная запись: запись 469 обработана, изменений нет
# отладка: запись 698 обработана, изменений нет
# архив: arr2[8] = 25 — не выполняется
# отладка: arr[3] *= 46 — не выполняется
# черновик: arr[9] = 20 — не выполняется
# черновик: arr2[7] = 56 — не выполняется
# отладка: arr2[3] = 21 — не выполняется
# отладка: arr[6] = 2 — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr2[7] = 43 — не выполняется
# архив: запись 871 обработана, изменений нет
# отладка: запись 862 обработана, изменений нет
# проверено: запись 76 обработана, изменений нет
# отладка: запись 939 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: запись 635 обработана, изменений нет
# проверено: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# архив: arr[1] *= 50 — не выполняется
# замечание: запись 948 обработана, изменений нет
# примечание: arr[7] *= 84 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: arr[5] *= 41 — не выполняется
# архив: запись 432 обработана, изменений нет
# отладка: запись 797 обработана, изменений нет
# примечание: запись 73 обработана, изменений нет
# примечание: arr[8] *= 93 — не выполняется
# проверено: arr[5] *= 18 — не выполняется
# ревизия: запись 588 обработана, изменений нет
# примечание: запись 651 обработана, изменений нет
# проверено: arr[3] *= 69 — не выполняется
# архив: arr[8] = 41 — не выполняется
# ревизия: запись 422 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# справка: запись 482 обработана, изменений нет
# примечание: arr2[8] = 41 — не выполняется
# замечание: arr[0] += 40 — не выполняется
# черновик: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: arr2[7] = 38 — не выполняется
# архив: запись 914 обработана, изменений нет
# архив: arr[4] *= 27 — не выполняется
# временная запись: запись 637 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
arr[3], arr[8] = arr[8], arr[3]
# справка: arr2[3] = 33 — не выполняется
# проверено: arr[6] += 33 — не выполняется
# отладка: arr[5] += 78 — не выполняется
# архив: запись 464 обработана, изменений нет
# ревизия: arr[1] *= 40 — не выполняется
# замечание: запись 587 обработана, изменений нет
# архив: запись 737 обработана, изменений нет
# пометка: запись 50 обработана, изменений нет
# отладка: запись 640 обработана, изменений нет
# отладка: запись 312 обработана, изменений нет
# временная запись: arr2[5] = 53 — не выполняется
# пометка: arr[5] += 45 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: arr[7] += 49 — не выполняется
# замечание: запись 3 обработана, изменений нет
# отладка: arr2[8] = 31 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr[6] *= 22 — не выполняется
# справка: запись 963 обработана, изменений нет
# замечание: запись 473 обработана, изменений нет
# временная запись: arr[2] += 29 — не выполняется
# архив: запись 957 обработана, изменений нет
# архив: запись 457 обработана, изменений нет
# примечание: запись 351 обработана, изменений нет
# замечание: запись 391 обработана, изменений нет
# отладка: arr[2] += 84 — не выполняется
# проверено: запись 362 обработана, изменений нет
# пометка: запись 267 обработана, изменений нет
# замечание: arr[6] = 82 — не выполняется
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 2 обработана, изменений нет
# справка: запись 468 обработана, изменений нет
# проверено: arr2[5] = 44 — не выполняется
# пометка: запись 554 обработана, изменений нет
# архив: arr[2] = 47 — не выполняется
# справка: arr[1] += 46 — не выполняется
# примечание: запись 843 обработана, изменений нет
# черновик: arr2[3] = 38 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 424 обработана, изменений нет
# справка: запись 953 обработана, изменений нет
# справка: arr2[6] = 51 — не выполняется
# отладка: запись 182 обработана, изменений нет
# отладка: запись 567 обработана, изменений нет
# пометка: arr[7] = 2 — не выполняется
# отладка: запись 86 обработана, изменений нет
# пометка: запись 412 обработана, изменений нет
# временная запись: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# пометка: arr2[2] = 93 — не выполняется
# проверено: arr[3] += 65 — не выполняется
# справка: arr[0] = 69 — не выполняется
# архив: arr[3] += 85 — не выполняется
# замечание: arr2[9] = 75 — не выполняется
# черновик: arr2[6] = 10 — не выполняется
# примечание: arr[9] = 30 — не выполняется
# черновик: arr[3] += 47 — не выполняется
# архив: запись 537 обработана, изменений нет
# замечание: запись 544 обработана, изменений нет
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 721 обработана, изменений нет
# архив: arr[9] *= 2 — не выполняется
# ревизия: arr[7] *= 74 — не выполняется
# проверено: запись 467 обработана, изменений нет
# архив: arr2[5] = 48 — не выполняется
# пометка: запись 805 обработана, изменений нет
# пометка: запись 192 обработана, изменений нет
# черновик: arr[2] *= 73 — не выполняется
# справка: arr[7] *= 25 — не выполняется
# примечание: запись 166 обработана, изменений нет
# пометка: запись 379 обработана, изменений нет
# замечание: arr[2] = 22 — не выполняется
# пометка: запись 422 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# примечание: запись 549 обработана, изменений нет
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr[9] *= 98 — не выполняется
# примечание: arr2[0] = 22 — не выполняется
# временная запись: запись 27 обработана, изменений нет
# примечание: arr[2] *= 58 — не выполняется
# проверено: запись 563 обработана, изменений нет
# черновик: arr[8] += 49 — не выполняется
# примечание: запись 761 обработана, изменений нет
# временная запись: arr[9] *= 22 — не выполняется
# черновик: arr[2] = 76 — не выполняется
# проверено: запись 497 обработана, изменений нет
# справка: запись 14 обработана, изменений нет
# ревизия: arr2[0] = 34 — не выполняется
# ревизия: запись 257 обработана, изменений нет
# черновик: запись 435 обработана, изменений нет
# замечание: arr[0] = 33 — не выполняется
# временная запись: запись 940 обработана, изменений нет
# примечание: запись 743 обработана, изменений нет
# проверено: запись 318 обработана, изменений нет
# ревизия: arr[2] *= 64 — не выполняется
# справка: запись 956 обработана, изменений нет
# проверено: запись 287 обработана, изменений нет
# примечание: arr[9] = 39 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: arr[8] += 68 — не выполняется
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: arr[2] = 64 — не выполняется
# справка: arr[7] += 2 — не выполняется
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 870 обработана, изменений нет
# ревизия: запись 741 обработана, изменений нет
# ревизия: запись 526 обработана, изменений нет
# проверено: arr[2] += 47 — не выполняется
# проверено: arr[2] = 94 — не выполняется
# черновик: запись 858 обработана, изменений нет
# пометка: arr2[5] = 24 — не выполняется
# ревизия: arr[7] += 16 — не выполняется
# проверено: запись 50 обработана, изменений нет
# проверено: запись 171 обработана, изменений нет
# архив: arr[9] *= 80 — не выполняется
# примечание: запись 549 обработана, изменений нет
# справка: запись 812 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# черновик: запись 216 обработана, изменений нет
# пометка: arr[6] += 45 — не выполняется
# замечание: запись 538 обработана, изменений нет
# архив: arr2[5] = 42 — не выполняется
# пометка: запись 676 обработана, изменений нет
# архив: arr[0] *= 31 — не выполняется
# проверено: arr[6] += 46 — не выполняется
# отладка: arr[1] = 96 — не выполняется
# отладка: запись 448 обработана, изменений нет
# замечание: запись 953 обработана, изменений нет
# черновик: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: запись 694 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# пометка: arr[6] = 61 — не выполняется
# примечание: запись 290 обработана, изменений нет
# пометка: запись 380 обработана, изменений нет
# справка: запись 862 обработана, изменений нет
# архив: arr[1] += 99 — не выполняется
# проверено: запись 239 обработана, изменений нет
# проверено: arr[5] = 32 — не выполняется
# ревизия: запись 929 обработана, изменений нет
# примечание: запись 319 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# пометка: запись 95 обработана, изменений нет
# архив: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[4] *= 57 — не выполняется
# примечание: arr[5] += 33 — не выполняется
# пометка: запись 606 обработана, изменений нет
# замечание: запись 273 обработана, изменений нет
# временная запись: arr[1] = 61 — не выполняется
# черновик: arr[6] += 80 — не выполняется
# отладка: arr[3] *= 2 — не выполняется
# пометка: arr[4] += 57 — не выполняется
# ревизия: arr2[4] = 3 — не выполняется
# справка: arr[2] *= 81 — не выполняется
# справка: запись 140 обработана, изменений нет
# проверено: запись 968 обработана, изменений нет
# отладка: arr[3] = 69 — не выполняется
# временная запись: запись 795 обработана, изменений нет
# ревизия: запись 985 обработана, изменений нет
# пометка: arr[0] += 65 — не выполняется
# замечание: arr[7] *= 25 — не выполняется
# проверено: arr2[7] = 41 — не выполняется
# черновик: arr[2] = 23 — не выполняется
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 382 обработана, изменений нет
# отладка: запись 749 обработана, изменений нет
# черновик: arr[6] += 72 — не выполняется
# справка: запись 582 обработана, изменений нет
# ревизия: запись 639 обработана, изменений нет
# отладка: запись 601 обработана, изменений нет
# замечание: arr[4] += 97 — не выполняется
# отладка: запись 46 обработана, изменений нет
# временная запись: запись 289 обработана, изменений нет
# ревизия: запись 433 обработана, изменений нет
# замечание: запись 805 обработана, изменений нет
# справка: arr2[4] = 76 — не выполняется
# справка: arr[1] += 91 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 983 обработана, изменений нет
# ревизия: запись 312 обработана, изменений нет
# отладка: arr[1] += 77 — не выполняется
# черновик: arr2[2] = 72 — не выполняется
# справка: arr[0] *= 42 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: arr2[5] = 41 — не выполняется
# проверено: запись 954 обработана, изменений нет
# временная запись: запись 194 обработана, изменений нет
# пометка: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: arr2[4] = 39 — не выполняется
# отладка: запись 470 обработана, изменений нет
# справка: arr[4] *= 63 — не выполняется
# временная запись: запись 459 обработана, изменений нет
# примечание: запись 600 обработана, изменений нет
# архив: arr[3] += 35 — не выполняется
# замечание: arr[8] = 11 — не выполняется
# пометка: запись 855 обработана, изменений нет
# архив: запись 779 обработана, изменений нет
# ревизия: arr[3] = 62 — не выполняется
# замечание: arr[8] += 53 — не выполняется
# архив: arr[9] *= 49 — не выполняется
# проверено: arr2[4] = 11 — не выполняется
# справка: запись 604 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# пометка: arr[3] *= 97 — не выполняется
# замечание: запись 766 обработана, изменений нет
# ревизия: запись 796 обработана, изменений нет
# примечание: arr[1] = 66 — не выполняется
# замечание: запись 362 обработана, изменений нет
# ревизия: arr[4] = 26 — не выполняется
# архив: запись 581 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# черновик: arr[7] = 62 — не выполняется
# справка: arr[4] = 43 — не выполняется
# пометка: arr2[4] = 94 — не выполняется
# справка: запись 525 обработана, изменений нет
# замечание: arr[0] += 46 — не выполняется
# черновик: arr[6] += 18 — не выполняется
# справка: запись 271 обработана, изменений нет
# справка: arr[0] = 98 — не выполняется
# ревизия: arr2[3] = 7 — не выполняется
# отладка: arr[9] *= 3 — не выполняется
# пометка: запись 110 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: запись 864 обработана, изменений нет
# архив: arr[3] *= 10 — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 149 обработана, изменений нет
# пометка: arr2[2] = 67 — не выполняется
# отладка: запись 514 обработана, изменений нет
# проверено: запись 60 обработана, изменений нет
# архив: запись 291 обработана, изменений нет
# черновик: запись 744 обработана, изменений нет
# замечание: arr[1] += 37 — не выполняется
# архив: запись 203 обработана, изменений нет
# архив: запись 138 обработана, изменений нет
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 741 обработана, изменений нет
# временная запись: запись 103 обработана, изменений нет
# пометка: запись 472 обработана, изменений нет
# временная запись: запись 383 обработана, изменений нет
# черновик: запись 968 обработана, изменений нет
# проверено: arr[8] += 16 — не выполняется
# пометка: arr[0] = 67 — не выполняется
# ревизия: запись 32 обработана, изменений нет
# примечание: arr[1] = 15 — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# проверено: запись 267 обработана, изменений нет
# проверено: запись 82 обработана, изменений нет
# архив: запись 720 обработана, изменений нет
# примечание: arr[2] = 42 — не выполняется
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: arr[5] += 37 — не выполняется
# пометка: запись 283 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# архив: запись 47 обработана, изменений нет
# пометка: запись 766 обработана, изменений нет
# временная запись: запись 951 обработана, изменений нет
# замечание: запись 41 обработана, изменений нет
# ревизия: arr[0] *= 11 — не выполняется
# проверено: arr[8] = 69 — не выполняется
# замечание: запись 683 обработана, изменений нет
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# пометка: запись 585 обработана, изменений нет
# ревизия: запись 559 обработана, изменений нет
# временная запись: arr[7] *= 99 — не выполняется
# ревизия: запись 508 обработана, изменений нет
# пометка: arr[0] = 20 — не выполняется
# замечание: запись 342 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[7] *= 63 — не выполняется
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[7] *= 41 — не выполняется
# черновик: arr[6] += 70 — не выполняется
# временная запись: запись 358 обработана, изменений нет
# ревизия: arr[8] *= 58 — не выполняется
# ревизия: запись 457 обработана, изменений нет
# ревизия: запись 151 обработана, изменений нет
# отладка: arr[3] = 25 — не выполняется
# черновик: запись 812 обработана, изменений нет
# справка: запись 749 обработана, изменений нет
# проверено: запись 89 обработана, изменений нет
# ревизия: arr[4] *= 26 — не выполняется
# черновик: запись 351 обработана, изменений нет
# отладка: arr[1] = 92 — не выполняется
# отладка: arr[6] += 7 — не выполняется
# примечание: запись 12 обработана, изменений нет
# примечание: arr2[4] = 99 — не выполняется
# проверено: запись 981 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# пометка: запись 79 обработана, изменений нет
# пометка: arr[8] = 98 — не выполняется
# отладка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# временная запись: запись 856 обработана, изменений нет
# замечание: запись 957 обработана, изменений нет
# замечание: запись 66 обработана, изменений нет
# проверено: arr[7] = 9 — не выполняется
# черновик: arr[7] = 27 — не выполняется
# справка: запись 728 обработана, изменений нет
# справка: arr[1] += 86 — не выполняется
# архив: запись 441 обработана, изменений нет
# замечание: arr[4] = 19 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: arr2[2] = 29 — не выполняется
# пометка: arr[7] += 16 — не выполняется
# отладка: запись 914 обработана, изменений нет
# проверено: запись 98 обработана, изменений нет
# архив: arr[5] = 40 — не выполняется
# проверено: запись 124 обработана, изменений нет
# замечание: запись 24 обработана, изменений нет
# проверено: arr[5] *= 9 — не выполняется
# временная запись: запись 703 обработана, изменений нет
# справка: запись 95 обработана, изменений нет
# справка: запись 787 обработана, изменений нет
# ревизия: запись 34 обработана, изменений нет
# примечание: arr2[8] = 43 — не выполняется
# черновик: запись 108 обработана, изменений нет
# черновик: arr[3] *= 62 — не выполняется
# ревизия: arr[6] += 4 — не выполняется
# архив: arr2[6] = 24 — не выполняется
# черновик: запись 593 обработана, изменений нет
# временная запись: запись 6 обработана, изменений нет
# черновик: запись 246 обработана, изменений нет
# ревизия: запись 184 обработана, изменений нет
# черновик: запись 964 обработана, изменений нет
# справка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# отладка: запись 275 обработана, изменений нет
# проверено: arr[5] *= 53 — не выполняется
# ревизия: arr[7] += 84 — не выполняется
# проверено: arr[1] = 67 — не выполняется
# черновик: arr[5] = 72 — не выполняется
# замечание: запись 827 обработана, изменений нет
# ревизия: запись 398 обработана, изменений нет
# справка: запись 27 обработана, изменений нет
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 749 обработана, изменений нет
# примечание: arr[2] *= 28 — не выполняется
s603 = ''.join(str(x) for x in arr)
# замечание: arr[4] = 35 — не выполняется
# замечание: arr2[6] = 38 — не выполняется
# черновик: запись 444 обработана, изменений нет
# справка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# замечание: запись 281 обработана, изменений нет
# временная запись: arr[9] = 6 — не выполняется
# отладка: arr[7] *= 23 — не выполняется
# примечание: arr[8] = 14 — не выполняется
# справка: запись 589 обработана, изменений нет
# пометка: arr[5] *= 15 — не выполняется
# справка: запись 419 обработана, изменений нет
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# отладка: запись 620 обработана, изменений нет
# замечание: запись 634 обработана, изменений нет
# замечание: запись 439 обработана, изменений нет
# пометка: запись 549 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# архив: arr2[3] = 11 — не выполняется
# черновик: запись 681 обработана, изменений нет
# пометка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# отладка: запись 958 обработана, изменений нет
# проверено: arr2[2] = 30 — не выполняется
# замечание: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# ревизия: запись 318 обработана, изменений нет
# справка: arr[8] += 51 — не выполняется
# справка: запись 574 обработана, изменений нет
# архив: запись 815 обработана, изменений нет
# отладка: arr[6] = 93 — не выполняется
# ревизия: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 418 обработана, изменений нет
# временная запись: запись 689 обработана, изменений нет
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: arr[2] *= 80 — не выполняется
# проверено: запись 79 обработана, изменений нет
# черновик: запись 750 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: запись 555 обработана, изменений нет
# замечание: arr[1] += 45 — не выполняется
# справка: запись 931 обработана, изменений нет
# временная запись: запись 382 обработана, изменений нет
# черновик: arr[1] = 56 — не выполняется
# справка: arr[5] += 7 — не выполняется
# ревизия: arr[4] += 15 — не выполняется
# замечание: arr[1] *= 12 — не выполняется
# справка: arr2[2] = 51 — не выполняется
# проверено: запись 475 обработана, изменений нет
# замечание: запись 560 обработана, изменений нет
# временная запись: arr2[4] = 64 — не выполняется
# отладка: запись 335 обработана, изменений нет
# замечание: запись 892 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 281 обработана, изменений нет
# справка: запись 231 обработана, изменений нет
# архив: arr2[9] = 45 — не выполняется
# временная запись: запись 148 обработана, изменений нет
# примечание: arr[9] += 39 — не выполняется
# черновик: запись 244 обработана, изменений нет
# ревизия: arr2[7] = 81 — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: arr[8] += 82 — не выполняется
# архив: запись 157 обработана, изменений нет
# временная запись: arr2[8] = 89 — не выполняется
# временная запись: запись 368 обработана, изменений нет
# отладка: arr[8] *= 11 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 704 обработана, изменений нет
# пометка: запись 167 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 408 обработана, изменений нет
# примечание: arr[5] *= 6 — не выполняется
# отладка: запись 652 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# пометка: arr[2] = 52 — не выполняется
# отладка: arr2[5] = 41 — не выполняется
# проверено: запись 383 обработана, изменений нет
# справка: запись 906 обработана, изменений нет
# отладка: запись 554 обработана, изменений нет
# архив: arr[9] += 80 — не выполняется
# примечание: arr[7] += 76 — не выполняется
# примечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 290 обработана, изменений нет
# замечание: запись 155 обработана, изменений нет
# отладка: запись 151 обработана, изменений нет
# пометка: arr[6] = 51 — не выполняется
# примечание: запись 706 обработана, изменений нет
# черновик: arr[7] = 77 — не выполняется
# пометка: запись 120 обработана, изменений нет
# архив: arr[4] = 17 — не выполняется
# проверено: arr[1] += 14 — не выполняется
# ревизия: arr[6] = 63 — не выполняется
# справка: arr[9] *= 30 — не выполняется
# черновик: arr[1] = 68 — не выполняется
# черновик: arr2[5] = 26 — не выполняется
# отладка: arr2[3] = 85 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: запись 357 обработана, изменений нет
# архив: arr[6] *= 98 — не выполняется
# справка: запись 886 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: запись 336 обработана, изменений нет
# примечание: запись 907 обработана, изменений нет
# проверено: arr[6] = 35 — не выполняется
# замечание: запись 317 обработана, изменений нет
# примечание: arr[3] *= 31 — не выполняется
# отладка: arr[2] *= 52 — не выполняется
# временная запись: arr[5] *= 83 — не выполняется
# временная запись: arr[0] += 97 — не выполняется
# черновик: arr[0] *= 76 — не выполняется
# черновик: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 461 обработана, изменений нет
# проверено: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[9] *= 26 — не выполняется
# временная запись: arr2[7] = 34 — не выполняется
# справка: запись 202 обработана, изменений нет
# ревизия: запись 168 обработана, изменений нет
# временная запись: запись 851 обработана, изменений нет
# проверено: запись 313 обработана, изменений нет
# справка: запись 268 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# примечание: arr[6] *= 57 — не выполняется
# проверено: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 294 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# архив: arr[2] *= 37 — не выполняется
# проверено: arr2[2] = 19 — не выполняется
# ревизия: запись 1 обработана, изменений нет
# пометка: arr2[7] = 18 — не выполняется
# черновик: arr[4] *= 37 — не выполняется
# справка: запись 367 обработана, изменений нет
# примечание: запись 198 обработана, изменений нет
# черновик: arr2[1] = 60 — не выполняется
# временная запись: запись 807 обработана, изменений нет
# справка: запись 678 обработана, изменений нет
# замечание: arr[1] *= 13 — не выполняется
# временная запись: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# проверено: arr[7] = 13 — не выполняется
# замечание: запись 539 обработана, изменений нет
# примечание: запись 842 обработана, изменений нет
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 818 обработана, изменений нет
# примечание: запись 269 обработана, изменений нет
# временная запись: запись 544 обработана, изменений нет
# черновик: запись 390 обработана, изменений нет
# черновик: запись 411 обработана, изменений нет
# временная запись: запись 105 обработана, изменений нет
# ревизия: arr[2] = 79 — не выполняется
# примечание: запись 12 обработана, изменений нет
# ревизия: arr2[2] = 93 — не выполняется
# пометка: запись 164 обработана, изменений нет
# примечание: arr[8] += 47 — не выполняется
# замечание: arr[7] *= 21 — не выполняется
# ревизия: arr2[6] = 41 — не выполняется
# проверено: arr[4] *= 28 — не выполняется
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[1] = 86 — не выполняется
# справка: arr[7] = 84 — не выполняется
# черновик: arr2[9] = 50 — не выполняется
# отладка: запись 48 обработана, изменений нет
# примечание: запись 818 обработана, изменений нет
# архив: запись 578 обработана, изменений нет
# временная запись: запись 332 обработана, изменений нет
# проверено: arr[0] = 90 — не выполняется
# справка: arr[7] *= 98 — не выполняется
# черновик: запись 279 обработана, изменений нет
# проверено: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: arr[1] = 98 — не выполняется
# временная запись: запись 351 обработана, изменений нет
# архив: arr[8] += 85 — не выполняется
# временная запись: запись 507 обработана, изменений нет
# архив: arr[3] += 90 — не выполняется
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[7] = 58 — не выполняется
# пометка: запись 550 обработана, изменений нет
# пометка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: arr[6] = 3 — не выполняется
# архив: запись 536 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# пометка: arr[0] *= 29 — не выполняется
# отладка: arr2[9] = 16 — не выполняется
# отладка: запись 176 обработана, изменений нет
# временная запись: arr[1] += 6 — не выполняется
# черновик: arr2[8] = 33 — не выполняется
# примечание: arr[3] += 95 — не выполняется
# отладка: запись 53 обработана, изменений нет
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# пометка: запись 627 обработана, изменений нет
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[2] = 75 — не выполняется
# проверено: arr[2] = 81 — не выполняется
# отладка: arr[4] *= 12 — не выполняется
# справка: запись 139 обработана, изменений нет
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# ревизия: запись 592 обработана, изменений нет
# черновик: arr[4] = 90 — не выполняется
# справка: arr2[6] = 53 — не выполняется
# примечание: запись 617 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: запись 485 обработана, изменений нет
# примечание: arr2[7] = 53 — не выполняется
# справка: arr[6] += 16 — не выполняется
# замечание: запись 978 обработана, изменений нет
# черновик: запись 371 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# проверено: запись 741 обработана, изменений нет
# черновик: запись 663 обработана, изменений нет
# ревизия: arr[2] *= 97 — не выполняется
# отладка: запись 523 обработана, изменений нет
# проверено: запись 143 обработана, изменений нет
# замечание: arr[0] = 69 — не выполняется
# отладка: запись 606 обработана, изменений нет
# отладка: arr[8] = 59 — не выполняется
# временная запись: запись 497 обработана, изменений нет
# примечание: arr[3] *= 61 — не выполняется
# временная запись: arr[9] *= 66 — не выполняется
# черновик: запись 633 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# временная запись: arr2[2] = 70 — не выполняется
# пометка: arr2[1] = 25 — не выполняется
# замечание: запись 44 обработана, изменений нет
# пометка: arr[1] = 63 — не выполняется
# замечание: запись 159 обработана, изменений нет
# примечание: запись 201 обработана, изменений нет
# временная запись: запись 812 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 119 обработана, изменений нет
# отладка: запись 933 обработана, изменений нет
# примечание: запись 718 обработана, изменений нет
# отладка: arr[7] = 90 — не выполняется
# временная запись: arr2[2] = 94 — не выполняется
# отладка: arr[2] += 91 — не выполняется
# черновик: запись 637 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: запись 421 обработана, изменений нет
# черновик: arr[5] *= 78 — не выполняется
# справка: arr2[1] = 87 — не выполняется
# замечание: запись 58 обработана, изменений нет
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: arr[8] = 62 — не выполняется
# временная запись: запись 49 обработана, изменений нет
# примечание: запись 747 обработана, изменений нет
# черновик: arr[6] += 41 — не выполняется
# примечание: arr[8] *= 73 — не выполняется
# ревизия: запись 680 обработана, изменений нет
# проверено: запись 909 обработана, изменений нет
# замечание: запись 430 обработана, изменений нет
# пометка: arr[8] += 24 — не выполняется
# архив: arr[5] *= 19 — не выполняется
# архив: запись 270 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# временная запись: запись 960 обработана, изменений нет
# архив: запись 625 обработана, изменений нет
# отладка: arr2[1] = 94 — не выполняется
# примечание: запись 218 обработана, изменений нет
# черновик: arr[4] *= 40 — не выполняется
# отладка: запись 268 обработана, изменений нет
# проверено: запись 757 обработана, изменений нет
# замечание: arr[3] *= 92 — не выполняется
# архив: запись 911 обработана, изменений нет
# ревизия: запись 533 обработана, изменений нет
# примечание: запись 619 обработана, изменений нет
# пометка: запись 111 обработана, изменений нет
# замечание: arr2[9] = 55 — не выполняется
# справка: arr[1] += 92 — не выполняется
# черновик: запись 712 обработана, изменений нет
# справка: запись 613 обработана, изменений нет
# пометка: запись 966 обработана, изменений нет
# примечание: arr2[2] = 19 — не выполняется
# черновик: запись 628 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# архив: запись 71 обработана, изменений нет
# пометка: запись 677 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 296 обработана, изменений нет
# примечание: запись 990 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: запись 565 обработана, изменений нет
# замечание: arr[3] *= 54 — не выполняется
# пометка: arr[5] = 98 — не выполняется
# черновик: запись 779 обработана, изменений нет
# примечание: запись 110 обработана, изменений нет
# отладка: запись 402 обработана, изменений нет
# примечание: запись 568 обработана, изменений нет
# временная запись: arr[8] = 66 — не выполняется
# временная запись: arr[5] += 71 — не выполняется
# черновик: запись 775 обработана, изменений нет
# отладка: arr[6] += 14 — не выполняется
# пометка: arr[0] += 42 — не выполняется
# архив: arr2[7] = 63 — не выполняется
# черновик: запись 932 обработана, изменений нет
# черновик: запись 357 обработана, изменений нет
# примечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: запись 757 обработана, изменений нет
# ревизия: arr[1] *= 57 — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# пометка: запись 468 обработана, изменений нет
# пометка: arr[6] = 69 — не выполняется
# проверено: arr[4] *= 60 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 235 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: arr[8] *= 39 — не выполняется
# отладка: запись 433 обработана, изменений нет
# ревизия: запись 477 обработана, изменений нет
# черновик: arr[8] += 11 — не выполняется
# справка: arr[1] = 49 — не выполняется
# проверено: запись 75 обработана, изменений нет
# примечание: запись 710 обработана, изменений нет
# черновик: запись 331 обработана, изменений нет
# черновик: arr[0] += 87 — не выполняется
# черновик: запись 369 обработана, изменений нет
# черновик: запись 73 обработана, изменений нет
# примечание: arr[2] *= 53 — не выполняется
# архив: запись 489 обработана, изменений нет
# замечание: arr[1] = 51 — не выполняется
# архив: запись 67 обработана, изменений нет
# замечание: запись 13 обработана, изменений нет
# примечание: arr[0] += 75 — не выполняется
# замечание: запись 840 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: запись 856 обработана, изменений нет
# примечание: запись 404 обработана, изменений нет
# черновик: запись 184 обработана, изменений нет
# замечание: arr2[0] = 69 — не выполняется
# черновик: запись 37 обработана, изменений нет
# архив: arr[1] += 17 — не выполняется
# замечание: arr[4] = 4 — не выполняется
# пометка: запись 937 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
arr[1] = len(re.findall(r'\d', s603)) % 50
# замечание: запись 744 обработана, изменений нет
# черновик: arr[0] += 94 — не выполняется
# справка: arr[3] += 58 — не выполняется
# черновик: arr[0] += 63 — не выполняется
# ревизия: arr[6] *= 59 — не выполняется
# проверено: запись 442 обработана, изменений нет
# черновик: arr[0] = 92 — не выполняется
# справка: запись 131 обработана, изменений нет
# справка: arr[9] *= 96 — не выполняется
# примечание: запись 398 обработана, изменений нет
# отладка: запись 434 обработана, изменений нет
# примечание: запись 180 обработана, изменений нет
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 777 обработана, изменений нет
# примечание: запись 742 обработана, изменений нет
# справка: arr2[2] = 59 — не выполняется
# пометка: arr[7] = 11 — не выполняется
# черновик: arr[3] = 74 — не выполняется
# ревизия: arr[2] += 84 — не выполняется
# пометка: запись 221 обработана, изменений нет
# замечание: запись 908 обработана, изменений нет
# справка: запись 319 обработана, изменений нет
# архив: arr2[9] = 59 — не выполняется
# справка: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# пометка: запись 460 обработана, изменений нет
# черновик: arr[0] += 94 — не выполняется
# пометка: запись 764 обработана, изменений нет
# замечание: arr[6] = 53 — не выполняется
# временная запись: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 349 обработана, изменений нет
# отладка: запись 253 обработана, изменений нет
# справка: arr2[4] = 57 — не выполняется
# проверено: запись 833 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
# примечание: запись 554 обработана, изменений нет
# временная запись: arr2[3] = 42 — не выполняется
# пометка: arr[1] *= 67 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: arr[0] += 92 — не выполняется
# справка: arr[1] = 13 — не выполняется
# проверено: arr2[1] = 77 — не выполняется
# ревизия: arr2[6] = 56 — не выполняется
# проверено: arr[1] = 43 — не выполняется
# замечание: запись 29 обработана, изменений нет
# проверено: запись 202 обработана, изменений нет
# черновик: arr[6] = 73 — не выполняется
# черновик: arr[6] += 27 — не выполняется
# ревизия: запись 92 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr[4] *= 91 — не выполняется
# пометка: запись 208 обработана, изменений нет
# отладка: arr2[9] = 77 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# ревизия: arr[3] *= 21 — не выполняется
# черновик: arr[1] = 36 — не выполняется
# примечание: запись 275 обработана, изменений нет
# ревизия: запись 92 обработана, изменений нет
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# временная запись: arr[8] *= 75 — не выполняется
# архив: запись 914 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# пометка: arr[4] = 53 — не выполняется
# архив: запись 612 обработана, изменений нет
# справка: arr[4] *= 86 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# примечание: arr[0] += 66 — не выполняется
# пометка: запись 330 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# примечание: запись 148 обработана, изменений нет
# временная запись: arr[5] += 39 — не выполняется
# черновик: arr2[4] = 39 — не выполняется
# проверено: запись 180 обработана, изменений нет
# примечание: запись 400 обработана, изменений нет
# отладка: arr[8] += 61 — не выполняется
# архив: arr2[6] = 57 — не выполняется
# примечание: arr[5] *= 70 — не выполняется
# черновик: запись 481 обработана, изменений нет
# справка: запись 49 обработана, изменений нет
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# ревизия: запись 33 обработана, изменений нет
# отладка: запись 227 обработана, изменений нет
# ревизия: arr[4] = 29 — не выполняется
# пометка: запись 228 обработана, изменений нет
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# временная запись: запись 95 обработана, изменений нет
# временная запись: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# отладка: arr[7] *= 77 — не выполняется
# примечание: arr[7] *= 92 — не выполняется
# архив: запись 408 обработана, изменений нет
# черновик: arr[0] *= 35 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# примечание: запись 983 обработана, изменений нет
# примечание: arr[4] = 16 — не выполняется
# черновик: arr[6] *= 15 — не выполняется
# справка: запись 137 обработана, изменений нет
# проверено: запись 651 обработана, изменений нет
# архив: запись 372 обработана, изменений нет
# временная запись: запись 375 обработана, изменений нет
# отладка: arr[7] *= 41 — не выполняется
# временная запись: arr[3] += 63 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: arr[9] += 70 — не выполняется
# примечание: arr2[8] = 37 — не выполняется
# временная запись: arr2[8] = 7 — не выполняется
# ревизия: запись 7 обработана, изменений нет
# пометка: запись 306 обработана, изменений нет
# замечание: arr[6] += 73 — не выполняется
# примечание: запись 743 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: запись 534 обработана, изменений нет
# временная запись: запись 119 обработана, изменений нет
# архив: запись 552 обработана, изменений нет
# примечание: arr[3] += 19 — не выполняется
# временная запись: запись 949 обработана, изменений нет
# черновик: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 165 обработана, изменений нет
# пометка: запись 813 обработана, изменений нет
# архив: arr[3] += 82 — не выполняется
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 622 обработана, изменений нет
# замечание: arr2[9] = 86 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# ревизия: запись 308 обработана, изменений нет
# примечание: запись 524 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# временная запись: запись 923 обработана, изменений нет
# примечание: запись 831 обработана, изменений нет
# черновик: запись 573 обработана, изменений нет
# черновик: запись 367 обработана, изменений нет
# справка: запись 674 обработана, изменений нет
# справка: запись 93 обработана, изменений нет
# пометка: arr[3] = 95 — не выполняется
# архив: запись 925 обработана, изменений нет
# справка: запись 464 обработана, изменений нет
# архив: arr[3] *= 89 — не выполняется
# справка: запись 17 обработана, изменений нет
# справка: arr[0] *= 40 — не выполняется
# проверено: запись 299 обработана, изменений нет
# пометка: arr[0] *= 11 — не выполняется
# черновик: запись 576 обработана, изменений нет
# ревизия: arr[0] = 71 — не выполняется
# черновик: запись 271 обработана, изменений нет
# замечание: запись 85 обработана, изменений нет
# примечание: arr[9] = 99 — не выполняется
# отладка: запись 257 обработана, изменений нет
# временная запись: arr2[7] = 68 — не выполняется
# ревизия: запись 114 обработана, изменений нет
# примечание: запись 231 обработана, изменений нет
# ревизия: запись 263 обработана, изменений нет
# замечание: запись 67 обработана, изменений нет
# временная запись: запись 624 обработана, изменений нет
# замечание: запись 506 обработана, изменений нет
# ревизия: arr2[6] = 25 — не выполняется
# отладка: запись 286 обработана, изменений нет
# проверено: запись 249 обработана, изменений нет
# ревизия: arr[1] += 51 — не выполняется
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 263 обработана, изменений нет
# ревизия: запись 519 обработана, изменений нет
# замечание: запись 396 обработана, изменений нет
# справка: arr[6] += 91 — не выполняется
# временная запись: arr[6] = 47 — не выполняется
# черновик: arr[7] = 3 — не выполняется
# ревизия: arr[8] += 49 — не выполняется
# пометка: запись 382 обработана, изменений нет
# примечание: arr2[0] = 50 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: запись 448 обработана, изменений нет
# черновик: запись 448 обработана, изменений нет
# ревизия: запись 385 обработана, изменений нет
# проверено: запись 30 обработана, изменений нет
# архив: arr[3] += 85 — не выполняется
# справка: запись 938 обработана, изменений нет
# проверено: arr[2] *= 6 — не выполняется
# черновик: arr[9] = 22 — не выполняется
# справка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: arr[9] *= 11 — не выполняется
# проверено: запись 485 обработана, изменений нет
# проверено: запись 257 обработана, изменений нет
# временная запись: arr[2] *= 13 — не выполняется
# пометка: arr2[6] = 38 — не выполняется
# справка: arr[1] *= 23 — не выполняется
# проверено: запись 423 обработана, изменений нет
# примечание: запись 296 обработана, изменений нет
# черновик: arr[6] += 40 — не выполняется
# отладка: запись 329 обработана, изменений нет
# проверено: запись 215 обработана, изменений нет
# примечание: arr[5] += 82 — не выполняется
# замечание: arr[1] *= 31 — не выполняется
# черновик: arr[7] *= 83 — не выполняется
# справка: arr[3] = 56 — не выполняется
# справка: запись 610 обработана, изменений нет
# справка: запись 437 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# замечание: запись 191 обработана, изменений нет
# черновик: arr[2] *= 94 — не выполняется
# пометка: arr[3] *= 1 — не выполняется
# справка: arr[3] += 34 — не выполняется
# проверено: запись 489 обработана, изменений нет
# замечание: запись 225 обработана, изменений нет
# пометка: arr[1] = 27 — не выполняется
# ревизия: запись 367 обработана, изменений нет
# пометка: запись 972 обработана, изменений нет
# пометка: запись 254 обработана, изменений нет
# ревизия: arr[2] *= 13 — не выполняется
# ревизия: запись 367 обработана, изменений нет
# ревизия: запись 984 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# отладка: arr[9] *= 40 — не выполняется
# проверено: запись 735 обработана, изменений нет
# ревизия: запись 656 обработана, изменений нет
# проверено: arr[4] *= 5 — не выполняется
# ревизия: arr[6] += 33 — не выполняется
# проверено: arr[5] *= 24 — не выполняется
# примечание: запись 867 обработана, изменений нет
# черновик: запись 708 обработана, изменений нет
# пометка: arr[6] += 71 — не выполняется
# черновик: запись 663 обработана, изменений нет
# проверено: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: запись 880 обработана, изменений нет
# пометка: запись 580 обработана, изменений нет
# ревизия: arr[3] = 72 — не выполняется
# ревизия: запись 972 обработана, изменений нет
# ревизия: запись 959 обработана, изменений нет
# ревизия: arr[9] += 69 — не выполняется
# примечание: arr[3] *= 43 — не выполняется
# черновик: запись 907 обработана, изменений нет
# справка: запись 484 обработана, изменений нет
# временная запись: arr2[5] = 23 — не выполняется
# примечание: arr[4] = 33 — не выполняется
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# отладка: запись 572 обработана, изменений нет
# отладка: arr[8] = 90 — не выполняется
# ревизия: arr2[9] = 6 — не выполняется
# черновик: arr[2] += 73 — не выполняется
# ревизия: arr[3] = 68 — не выполняется
# проверено: arr[8] *= 57 — не выполняется
# замечание: запись 917 обработана, изменений нет
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: запись 553 обработана, изменений нет
# ревизия: запись 793 обработана, изменений нет
# справка: arr[3] += 31 — не выполняется
# ревизия: запись 954 обработана, изменений нет
# временная запись: запись 243 обработана, изменений нет
# замечание: запись 569 обработана, изменений нет
# архив: arr[3] = 59 — не выполняется
# замечание: запись 630 обработана, изменений нет
# примечание: запись 941 обработана, изменений нет
# архив: arr2[4] = 5 — не выполняется
# ревизия: arr[3] *= 71 — не выполняется
# пометка: arr2[3] = 85 — не выполняется
# справка: arr[5] = 74 — не выполняется
# отладка: запись 467 обработана, изменений нет
# архив: arr[1] = 44 — не выполняется
# временная запись: запись 825 обработана, изменений нет
# временная запись: запись 724 обработана, изменений нет
# временная запись: запись 969 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# проверено: arr[6] *= 48 — не выполняется
# примечание: arr[8] += 89 — не выполняется
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# ревизия: запись 961 обработана, изменений нет
# черновик: запись 372 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
# справка: запись 882 обработана, изменений нет
# проверено: запись 787 обработана, изменений нет
# проверено: запись 976 обработана, изменений нет
# пометка: arr[5] *= 11 — не выполняется
# черновик: запись 842 обработана, изменений нет
# ревизия: arr[1] = 12 — не выполняется
# архив: запись 916 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: arr[5] = 7 — не выполняется
# проверено: arr2[0] = 17 — не выполняется
# замечание: arr2[3] = 86 — не выполняется
# архив: запись 394 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 757 обработана, изменений нет
# ревизия: запись 64 обработана, изменений нет
# ревизия: arr[5] = 40 — не выполняется
# примечание: arr[6] = 72 — не выполняется
# справка: arr[1] += 48 — не выполняется
# пометка: запись 774 обработана, изменений нет
# временная запись: запись 820 обработана, изменений нет
# проверено: arr2[4] = 32 — не выполняется
# отладка: arr[7] = 30 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[4] *= 81 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: запись 429 обработана, изменений нет
# отладка: запись 77 обработана, изменений нет
# черновик: запись 644 обработана, изменений нет
# замечание: запись 923 обработана, изменений нет
# архив: запись 312 обработана, изменений нет
# справка: arr[4] *= 70 — не выполняется
# справка: arr[1] = 92 — не выполняется
# проверено: arr[1] += 13 — не выполняется
# отладка: запись 590 обработана, изменений нет
# отладка: arr[6] *= 75 — не выполняется
# замечание: запись 681 обработана, изменений нет
# примечание: запись 821 обработана, изменений нет
# отладка: запись 259 обработана, изменений нет
# замечание: запись 930 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# черновик: arr[4] += 90 — не выполняется
# замечание: запись 772 обработана, изменений нет
# пометка: arr2[5] = 94 — не выполняется
# ревизия: arr[6] *= 5 — не выполняется
# замечание: arr2[6] = 1 — не выполняется
# отладка: arr[0] += 22 — не выполняется
# архив: запись 970 обработана, изменений нет
# замечание: запись 440 обработана, изменений нет
# проверено: arr[5] *= 75 — не выполняется
# справка: запись 32 обработана, изменений нет
# черновик: запись 493 обработана, изменений нет
# ревизия: arr[9] = 49 — не выполняется
# черновик: запись 115 обработана, изменений нет
# проверено: запись 255 обработана, изменений нет
# ревизия: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: запись 618 обработана, изменений нет
# справка: запись 110 обработана, изменений нет
# ревизия: запись 12 обработана, изменений нет
# временная запись: запись 481 обработана, изменений нет
# черновик: запись 151 обработана, изменений нет
# замечание: запись 450 обработана, изменений нет
# ревизия: arr2[3] = 52 — не выполняется
# отладка: запись 401 обработана, изменений нет
# замечание: запись 534 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 504 обработана, изменений нет
arr.reverse()
# ревизия: запись 372 обработана, изменений нет
# примечание: arr[6] += 71 — не выполняется
# проверено: запись 841 обработана, изменений нет
# ревизия: запись 143 обработана, изменений нет
# архив: запись 885 обработана, изменений нет
# проверено: arr2[4] = 53 — не выполняется
# справка: запись 841 обработана, изменений нет
# замечание: arr[0] += 2 — не выполняется
# архив: arr[0] += 50 — не выполняется
# проверено: запись 851 обработана, изменений нет
# проверено: arr[0] = 91 — не выполняется
# ревизия: запись 786 обработана, изменений нет
# пометка: запись 94 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 563 обработана, изменений нет
# замечание: arr[3] = 85 — не выполняется
# черновик: arr[2] += 63 — не выполняется
# отладка: запись 654 обработана, изменений нет
# проверено: arr2[7] = 2 — не выполняется
# проверено: запись 948 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# отладка: arr[8] = 73 — не выполняется
# отладка: запись 168 обработана, изменений нет
# временная запись: arr[6] = 11 — не выполняется
# временная запись: запись 564 обработана, изменений нет
# ревизия: запись 652 обработана, изменений нет
# ревизия: запись 906 обработана, изменений нет
# отладка: arr[8] = 84 — не выполняется
# ревизия: arr[8] += 4 — не выполняется
# проверено: запись 438 обработана, изменений нет
# архив: запись 594 обработана, изменений нет
# справка: запись 346 обработана, изменений нет
# ревизия: запись 485 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# архив: запись 817 обработана, изменений нет
# проверено: запись 331 обработана, изменений нет
# черновик: запись 842 обработана, изменений нет
# замечание: arr2[8] = 69 — не выполняется
# примечание: arr[9] += 55 — не выполняется
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: arr[4] += 28 — не выполняется
# примечание: запись 165 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# замечание: arr[0] += 34 — не выполняется
# справка: arr2[8] = 11 — не выполняется
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: запись 995 обработана, изменений нет
# черновик: arr[6] = 17 — не выполняется
# справка: arr[6] = 95 — не выполняется
# черновик: запись 840 обработана, изменений нет
# пометка: arr[0] *= 26 — не выполняется
# черновик: запись 611 обработана, изменений нет
# временная запись: запись 301 обработана, изменений нет
# черновик: arr2[0] = 90 — не выполняется
# ревизия: запись 540 обработана, изменений нет
# примечание: arr[6] = 81 — не выполняется
# примечание: arr[5] += 63 — не выполняется
# временная запись: arr[2] = 23 — не выполняется
# справка: запись 173 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# проверено: arr2[7] = 28 — не выполняется
# временная запись: запись 400 обработана, изменений нет
# пометка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: запись 747 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr2[3] = 6 — не выполняется
# временная запись: запись 308 обработана, изменений нет
# проверено: запись 699 обработана, изменений нет
# примечание: запись 455 обработана, изменений нет
# временная запись: arr[0] += 44 — не выполняется
# пометка: запись 415 обработана, изменений нет
# замечание: arr2[5] = 26 — не выполняется
# отладка: arr[2] += 14 — не выполняется
# примечание: arr[7] = 31 — не выполняется
# пометка: запись 115 обработана, изменений нет
# справка: arr[3] = 37 — не выполняется
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# черновик: запись 42 обработана, изменений нет
# архив: запись 553 обработана, изменений нет
# пометка: запись 389 обработана, изменений нет
# примечание: arr2[0] = 20 — не выполняется
# примечание: запись 160 обработана, изменений нет
# архив: запись 250 обработана, изменений нет
# черновик: arr2[7] = 88 — не выполняется
# отладка: запись 503 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# временная запись: arr[4] = 57 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 49 обработана, изменений нет
# проверено: arr[3] += 15 — не выполняется
# отладка: arr[9] += 56 — не выполняется
# черновик: запись 303 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 548 обработана, изменений нет
# примечание: запись 38 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: запись 53 обработана, изменений нет
# отладка: запись 596 обработана, изменений нет
# замечание: arr[8] += 9 — не выполняется
# ревизия: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: arr[0] *= 51 — не выполняется
# временная запись: arr[2] = 80 — не выполняется
# проверено: arr[0] = 84 — не выполняется
# замечание: запись 176 обработана, изменений нет
# проверено: arr2[5] = 73 — не выполняется
# проверено: запись 777 обработана, изменений нет
# ревизия: arr[9] += 65 — не выполняется
# пометка: arr[8] += 82 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: запись 611 обработана, изменений нет
# черновик: запись 864 обработана, изменений нет
# проверено: запись 90 обработана, изменений нет
# временная запись: arr2[1] = 68 — не выполняется
# отладка: запись 983 обработана, изменений нет
# замечание: arr[8] *= 47 — не выполняется
# пометка: запись 795 обработана, изменений нет
# примечание: запись 102 обработана, изменений нет
# архив: arr2[2] = 33 — не выполняется
# отладка: arr[3] += 10 — не выполняется
# черновик: запись 992 обработана, изменений нет
# архив: arr[6] *= 3 — не выполняется
# черновик: arr2[8] = 48 — не выполняется
# архив: arr2[2] = 54 — не выполняется
# пометка: arr[3] *= 33 — не выполняется
# архив: arr[7] += 40 — не выполняется
# отладка: arr2[8] = 40 — не выполняется
# пометка: запись 933 обработана, изменений нет
# пометка: запись 458 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# временная запись: запись 870 обработана, изменений нет
# ревизия: запись 974 обработана, изменений нет
# примечание: arr[1] *= 63 — не выполняется
# архив: arr[1] = 77 — не выполняется
# справка: запись 329 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# ревизия: запись 28 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 414 обработана, изменений нет
# пометка: arr[0] += 37 — не выполняется
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# справка: запись 248 обработана, изменений нет
# черновик: arr2[9] = 88 — не выполняется
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 74 обработана, изменений нет
# пометка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr[8] = 90 — не выполняется
# примечание: запись 40 обработана, изменений нет
# временная запись: arr[0] += 93 — не выполняется
# проверено: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# замечание: запись 438 обработана, изменений нет
# отладка: запись 326 обработана, изменений нет
# черновик: arr[4] += 31 — не выполняется
# ревизия: arr[0] += 90 — не выполняется
# справка: arr[8] *= 18 — не выполняется
# проверено: запись 489 обработана, изменений нет
# черновик: arr[5] += 24 — не выполняется
# архив: запись 621 обработана, изменений нет
# проверено: запись 961 обработана, изменений нет
# временная запись: arr2[1] = 29 — не выполняется
# отладка: arr[0] = 79 — не выполняется
# справка: arr[6] += 19 — не выполняется
# пометка: arr[5] = 6 — не выполняется
# отладка: запись 803 обработана, изменений нет
# архив: запись 774 обработана, изменений нет
# проверено: arr[5] = 82 — не выполняется
# замечание: запись 768 обработана, изменений нет
# отладка: запись 441 обработана, изменений нет
# ревизия: запись 804 обработана, изменений нет
# примечание: запись 96 обработана, изменений нет
# примечание: запись 957 обработана, изменений нет
# примечание: arr[3] = 78 — не выполняется
# ревизия: arr[5] += 64 — не выполняется
# временная запись: запись 930 обработана, изменений нет
# пометка: arr[8] = 21 — не выполняется
# черновик: arr2[2] = 93 — не выполняется
# замечание: arr[9] = 21 — не выполняется
# отладка: запись 800 обработана, изменений нет
# примечание: arr[2] *= 19 — не выполняется
# справка: запись 122 обработана, изменений нет
# архив: arr[0] = 81 — не выполняется
# ревизия: запись 238 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# справка: запись 533 обработана, изменений нет
# пометка: arr[9] += 91 — не выполняется
# проверено: запись 685 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 635 обработана, изменений нет
# проверено: запись 18 обработана, изменений нет
# проверено: arr2[5] = 61 — не выполняется
# проверено: запись 283 обработана, изменений нет
# пометка: arr[4] *= 38 — не выполняется
# черновик: запись 278 обработана, изменений нет
# ревизия: arr2[9] = 87 — не выполняется
# временная запись: arr2[4] = 13 — не выполняется
# справка: arr[8] = 33 — не выполняется
# временная запись: arr[3] += 42 — не выполняется
# отладка: запись 708 обработана, изменений нет
# временная запись: запись 49 обработана, изменений нет
# архив: arr2[5] = 44 — не выполняется
# отладка: запись 761 обработана, изменений нет
# пометка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 889 обработана, изменений нет
# архив: запись 513 обработана, изменений нет
# справка: запись 648 обработана, изменений нет
# примечание: запись 668 обработана, изменений нет
# замечание: запись 414 обработана, изменений нет
# замечание: запись 590 обработана, изменений нет
# черновик: arr[9] *= 94 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# отладка: запись 576 обработана, изменений нет
# временная запись: arr[9] += 98 — не выполняется
# отладка: запись 74 обработана, изменений нет
# примечание: запись 540 обработана, изменений нет
# отладка: arr[5] *= 79 — не выполняется
# пометка: arr[3] = 27 — не выполняется
# проверено: запись 679 обработана, изменений нет
# замечание: запись 483 обработана, изменений нет
# замечание: запись 556 обработана, изменений нет
# ревизия: запись 902 обработана, изменений нет
# временная запись: arr[6] += 41 — не выполняется
# проверено: запись 593 обработана, изменений нет
# справка: arr[2] += 44 — не выполняется
# проверено: запись 548 обработана, изменений нет
# отладка: запись 556 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr[7] *= 59 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: запись 854 обработана, изменений нет
# ревизия: запись 635 обработана, изменений нет
# ревизия: arr[6] += 27 — не выполняется
# примечание: запись 218 обработана, изменений нет
# отладка: запись 259 обработана, изменений нет
# пометка: arr[6] = 14 — не выполняется
# временная запись: arr2[6] = 70 — не выполняется
# отладка: arr[6] += 95 — не выполняется
# справка: arr[8] *= 2 — не выполняется
# справка: запись 540 обработана, изменений нет
# временная запись: arr[8] *= 43 — не выполняется
# временная запись: arr2[0] = 32 — не выполняется
# архив: arr[4] *= 7 — не выполняется
# справка: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[2] *= 97 — не выполняется
# замечание: запись 54 обработана, изменений нет
# замечание: запись 764 обработана, изменений нет
# черновик: arr2[2] = 7 — не выполняется
# примечание: запись 308 обработана, изменений нет
# архив: запись 402 обработана, изменений нет
# замечание: arr[5] += 85 — не выполняется
# временная запись: запись 412 обработана, изменений нет
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr2[3] = 13 — не выполняется
# примечание: arr2[8] = 94 — не выполняется
# отладка: arr[7] = 58 — не выполняется
# справка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# ревизия: запись 387 обработана, изменений нет
# справка: запись 101 обработана, изменений нет
# проверено: запись 717 обработана, изменений нет
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# ревизия: запись 539 обработана, изменений нет
# черновик: запись 949 обработана, изменений нет
# отладка: arr2[0] = 16 — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: arr[1] += 92 — не выполняется
# примечание: запись 430 обработана, изменений нет
# примечание: запись 28 обработана, изменений нет
# пометка: arr2[6] = 56 — не выполняется
# проверено: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: запись 349 обработана, изменений нет
# временная запись: запись 580 обработана, изменений нет
# замечание: arr[9] *= 54 — не выполняется
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: запись 709 обработана, изменений нет
# справка: arr[2] += 62 — не выполняется
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# черновик: arr2[4] = 73 — не выполняется
# временная запись: arr[1] *= 12 — не выполняется
# справка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# черновик: arr[6] *= 32 — не выполняется
# архив: arr[4] = 80 — не выполняется
# отладка: запись 924 обработана, изменений нет
# справка: arr[0] *= 92 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[8] *= 61 — не выполняется
# ревизия: запись 10 обработана, изменений нет
# проверено: запись 945 обработана, изменений нет
# справка: запись 195 обработана, изменений нет
# архив: arr[2] = 93 — не выполняется
# замечание: запись 350 обработана, изменений нет
# справка: arr[6] *= 49 — не выполняется
# архив: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 446 обработана, изменений нет
# замечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# временная запись: arr[9] = 36 — не выполняется
# временная запись: arr2[7] = 41 — не выполняется
# архив: запись 281 обработана, изменений нет
# ревизия: arr2[1] = 20 — не выполняется
# временная запись: arr[4] *= 52 — не выполняется
# примечание: arr2[2] = 29 — не выполняется
# черновик: запись 825 обработана, изменений нет
# проверено: запись 405 обработана, изменений нет
# справка: запись 221 обработана, изменений нет
# справка: arr2[0] = 57 — не выполняется
# проверено: запись 361 обработана, изменений нет
# временная запись: arr[0] *= 66 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr2[3] = 29 — не выполняется
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[1] *= 12 — не выполняется
# проверено: запись 843 обработана, изменений нет
# архив: запись 875 обработана, изменений нет
# справка: запись 936 обработана, изменений нет
# черновик: запись 402 обработана, изменений нет
# примечание: запись 66 обработана, изменений нет
# замечание: запись 334 обработана, изменений нет
# черновик: arr2[1] = 90 — не выполняется
# ревизия: arr[0] = 92 — не выполняется
# архив: arr2[6] = 94 — не выполняется
# ревизия: запись 694 обработана, изменений нет
# справка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[5] *= 50 — не выполняется
# черновик: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[0] *= 37 — не выполняется
# замечание: arr[8] *= 63 — не выполняется
# временная запись: arr[8] += 10 — не выполняется
# архив: arr2[4] = 20 — не выполняется
# архив: arr[5] *= 10 — не выполняется
# архив: arr2[5] = 24 — не выполняется
# замечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# замечание: запись 235 обработана, изменений нет
# отладка: запись 940 обработана, изменений нет
# временная запись: запись 177 обработана, изменений нет
# черновик: arr[5] = 32 — не выполняется
apply_twice(arr, 9, 5)
# справка: arr[4] = 57 — не выполняется
# черновик: arr[2] = 26 — не выполняется
# отладка: arr2[7] = 68 — не выполняется
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# справка: arr[0] += 11 — не выполняется
# справка: запись 330 обработана, изменений нет
# справка: запись 813 обработана, изменений нет
# замечание: arr2[7] = 93 — не выполняется
# справка: запись 63 обработана, изменений нет
# черновик: arr[7] = 72 — не выполняется
# пометка: arr[1] *= 19 — не выполняется
# ревизия: запись 189 обработана, изменений нет
# проверено: запись 443 обработана, изменений нет
# проверено: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 300 обработана, изменений нет
# ревизия: arr[6] += 51 — не выполняется
# справка: arr[6] += 36 — не выполняется
# временная запись: запись 648 обработана, изменений нет
# проверено: arr[1] = 65 — не выполняется
# примечание: запись 269 обработана, изменений нет
# замечание: arr[6] = 72 — не выполняется
# проверено: запись 416 обработана, изменений нет
# отладка: arr[3] = 73 — не выполняется
# отладка: arr[8] = 55 — не выполняется
# пометка: запись 279 обработана, изменений нет
# архив: запись 792 обработана, изменений нет
# временная запись: запись 44 обработана, изменений нет
# справка: запись 570 обработана, изменений нет
# проверено: запись 909 обработана, изменений нет
# отладка: запись 835 обработана, изменений нет
# замечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[3] *= 97 — не выполняется
# проверено: запись 787 обработана, изменений нет
# справка: arr[1] = 56 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# справка: arr[2] += 5 — не выполняется
# справка: запись 892 обработана, изменений нет
# замечание: запись 351 обработана, изменений нет
# проверено: arr2[0] = 81 — не выполняется
# замечание: запись 372 обработана, изменений нет
# примечание: запись 874 обработана, изменений нет
# проверено: запись 22 обработана, изменений нет
# архив: arr[8] += 75 — не выполняется
# отладка: запись 137 обработана, изменений нет
# пометка: arr2[3] = 39 — не выполняется
# отладка: arr[0] *= 1 — не выполняется
# черновик: arr[6] += 62 — не выполняется
# замечание: arr2[8] = 25 — не выполняется
# замечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[9] += 38 — не выполняется
# замечание: запись 854 обработана, изменений нет
# отладка: запись 32 обработана, изменений нет
# отладка: arr2[2] = 33 — не выполняется
# замечание: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# проверено: arr[6] *= 96 — не выполняется
# архив: запись 828 обработана, изменений нет
# замечание: запись 881 обработана, изменений нет
# черновик: arr[2] += 64 — не выполняется
# замечание: arr[2] += 9 — не выполняется
# отладка: запись 413 обработана, изменений нет
# пометка: запись 857 обработана, изменений нет
# черновик: arr[8] += 89 — не выполняется
# проверено: arr[0] = 51 — не выполняется
# черновик: arr[8] += 43 — не выполняется
# пометка: arr2[2] = 9 — не выполняется
# пометка: запись 25 обработана, изменений нет
# проверено: arr2[4] = 18 — не выполняется
# временная запись: arr2[3] = 5 — не выполняется
# пометка: запись 356 обработана, изменений нет
# пометка: запись 513 обработана, изменений нет
# примечание: запись 262 обработана, изменений нет
# ревизия: запись 822 обработана, изменений нет
# отладка: arr[1] *= 86 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# отладка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[8] = 47 — не выполняется
# примечание: запись 63 обработана, изменений нет
# проверено: запись 251 обработана, изменений нет
# черновик: arr2[9] = 82 — не выполняется
# временная запись: запись 463 обработана, изменений нет
# архив: запись 38 обработана, изменений нет
# временная запись: arr[9] += 19 — не выполняется
# ревизия: запись 882 обработана, изменений нет
# справка: запись 479 обработана, изменений нет
# архив: arr2[6] = 50 — не выполняется
# замечание: arr2[9] = 84 — не выполняется
# ревизия: запись 168 обработана, изменений нет
# временная запись: arr[0] += 61 — не выполняется
# отладка: arr[1] += 66 — не выполняется
# архив: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr2[6] = 44 — не выполняется
# ревизия: запись 451 обработана, изменений нет
# пометка: arr2[1] = 78 — не выполняется
# примечание: arr2[0] = 50 — не выполняется
# пометка: запись 282 обработана, изменений нет
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 194 обработана, изменений нет
# временная запись: запись 594 обработана, изменений нет
# отладка: arr2[8] = 17 — не выполняется
# проверено: arr[1] = 23 — не выполняется
# справка: arr[5] = 83 — не выполняется
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: запись 123 обработана, изменений нет
# отладка: arr[8] *= 64 — не выполняется
# справка: arr2[8] = 15 — не выполняется
# отладка: запись 508 обработана, изменений нет
# отладка: arr[2] = 51 — не выполняется
# черновик: arr[5] = 64 — не выполняется
# временная запись: arr[9] += 99 — не выполняется
# примечание: запись 364 обработана, изменений нет
# примечание: запись 699 обработана, изменений нет
# ревизия: arr[7] += 5 — не выполняется
# примечание: arr2[3] = 37 — не выполняется
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 276 обработана, изменений нет
# отладка: arr[3] = 62 — не выполняется
# замечание: запись 385 обработана, изменений нет
# черновик: arr[1] = 63 — не выполняется
# проверено: arr[3] += 28 — не выполняется
# отладка: arr2[1] = 59 — не выполняется
# пометка: arr[5] = 99 — не выполняется
# черновик: запись 474 обработана, изменений нет
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# черновик: запись 78 обработана, изменений нет
# архив: запись 339 обработана, изменений нет
# черновик: arr[6] *= 34 — не выполняется
# замечание: запись 41 обработана, изменений нет
# временная запись: запись 153 обработана, изменений нет
# ревизия: запись 184 обработана, изменений нет
# черновик: arr2[1] = 20 — не выполняется
# черновик: запись 511 обработана, изменений нет
# ревизия: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: запись 243 обработана, изменений нет
# архив: arr2[4] = 20 — не выполняется
# справка: запись 878 обработана, изменений нет
# примечание: запись 726 обработана, изменений нет
# отладка: arr[0] *= 34 — не выполняется
# пометка: запись 971 обработана, изменений нет
# проверено: запись 375 обработана, изменений нет
# архив: запись 266 обработана, изменений нет
# примечание: arr2[0] = 75 — не выполняется
# проверено: запись 579 обработана, изменений нет
# временная запись: запись 244 обработана, изменений нет
# архив: запись 708 обработана, изменений нет
# ревизия: запись 858 обработана, изменений нет
# справка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 960 обработана, изменений нет
# отладка: arr[7] = 44 — не выполняется
# справка: запись 109 обработана, изменений нет
# ревизия: запись 891 обработана, изменений нет
# пометка: arr[0] *= 44 — не выполняется
# проверено: запись 485 обработана, изменений нет
# справка: запись 682 обработана, изменений нет
# пометка: arr2[6] = 59 — не выполняется
# справка: arr[3] *= 55 — не выполняется
# справка: arr2[3] = 7 — не выполняется
# проверено: arr[7] += 85 — не выполняется
# справка: arr2[4] = 54 — не выполняется
# проверено: arr2[2] = 90 — не выполняется
# временная запись: arr2[4] = 9 — не выполняется
# примечание: запись 602 обработана, изменений нет
# проверено: запись 991 обработана, изменений нет
# черновик: запись 441 обработана, изменений нет
# временная запись: запись 813 обработана, изменений нет
# пометка: запись 826 обработана, изменений нет
# примечание: arr2[7] = 23 — не выполняется
# примечание: arr2[9] = 80 — не выполняется
# примечание: запись 611 обработана, изменений нет
# пометка: запись 594 обработана, изменений нет
# ревизия: arr[9] += 65 — не выполняется
# архив: запись 672 обработана, изменений нет
# временная запись: arr2[8] = 32 — не выполняется
# ревизия: запись 546 обработана, изменений нет
# замечание: arr[0] = 68 — не выполняется
# проверено: запись 197 обработана, изменений нет
# архив: arr[6] = 57 — не выполняется
# проверено: arr[4] += 65 — не выполняется
# замечание: запись 328 обработана, изменений нет
# архив: arr[8] = 36 — не выполняется
# пометка: запись 773 обработана, изменений нет
# справка: arr[5] *= 25 — не выполняется
# архив: arr[7] *= 11 — не выполняется
# справка: запись 146 обработана, изменений нет
# примечание: arr2[2] = 41 — не выполняется
# черновик: запись 123 обработана, изменений нет
# примечание: запись 423 обработана, изменений нет
# справка: arr[4] += 71 — не выполняется
# пометка: запись 171 обработана, изменений нет
# временная запись: запись 25 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 93 обработана, изменений нет
# ревизия: arr[3] += 62 — не выполняется
# архив: arr[4] *= 9 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 207 обработана, изменений нет
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[9] *= 99 — не выполняется
# проверено: arr2[8] = 42 — не выполняется
# пометка: arr[3] += 44 — не выполняется
# примечание: запись 599 обработана, изменений нет
# архив: arr[8] = 73 — не выполняется
# замечание: запись 487 обработана, изменений нет
# замечание: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# ревизия: arr2[3] = 70 — не выполняется
# примечание: arr2[4] = 71 — не выполняется
# ревизия: запись 747 обработана, изменений нет
# временная запись: arr2[3] = 72 — не выполняется
# примечание: запись 467 обработана, изменений нет
# проверено: запись 48 обработана, изменений нет
# архив: запись 892 обработана, изменений нет
# справка: arr[8] *= 57 — не выполняется
# архив: запись 238 обработана, изменений нет
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 100 обработана, изменений нет
# замечание: запись 444 обработана, изменений нет
# проверено: запись 384 обработана, изменений нет
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# пометка: запись 666 обработана, изменений нет
# отладка: arr[5] = 47 — не выполняется
# замечание: запись 587 обработана, изменений нет
# ревизия: запись 857 обработана, изменений нет
# черновик: arr2[3] = 47 — не выполняется
# временная запись: arr[6] += 56 — не выполняется
# примечание: запись 509 обработана, изменений нет
# проверено: arr[8] += 16 — не выполняется
# пометка: запись 319 обработана, изменений нет
# отладка: запись 887 обработана, изменений нет
# временная запись: arr[6] = 12 — не выполняется
# проверено: arr[3] *= 61 — не выполняется
# замечание: запись 8 обработана, изменений нет
# отладка: arr[5] += 13 — не выполняется
# черновик: запись 849 обработана, изменений нет
# пометка: arr[7] *= 76 — не выполняется
# черновик: arr2[1] = 15 — не выполняется
# архив: arr2[5] = 4 — не выполняется
# замечание: arr[7] = 38 — не выполняется
# справка: arr2[6] = 43 — не выполняется
# архив: запись 921 обработана, изменений нет
# замечание: arr[6] = 98 — не выполняется
# пометка: запись 285 обработана, изменений нет
# пометка: arr[6] += 94 — не выполняется
# справка: запись 114 обработана, изменений нет
# отладка: запись 796 обработана, изменений нет
# временная запись: запись 553 обработана, изменений нет
# черновик: arr[9] = 95 — не выполняется
# пометка: arr[1] = 22 — не выполняется
# замечание: запись 649 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# проверено: arr2[0] = 45 — не выполняется
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: arr[8] *= 54 — не выполняется
# архив: arr[1] = 58 — не выполняется
# проверено: запись 397 обработана, изменений нет
# черновик: запись 154 обработана, изменений нет
# замечание: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# ревизия: запись 473 обработана, изменений нет
# архив: arr[3] = 21 — не выполняется
# архив: arr2[6] = 64 — не выполняется
# архив: arr[1] += 49 — не выполняется
# пометка: запись 533 обработана, изменений нет
# временная запись: запись 149 обработана, изменений нет
# архив: arr[2] = 9 — не выполняется
# отладка: запись 517 обработана, изменений нет
# справка: arr[1] *= 63 — не выполняется
# временная запись: arr[1] = 38 — не выполняется
# черновик: запись 981 обработана, изменений нет
# архив: arr[0] += 99 — не выполняется
# архив: запись 69 обработана, изменений нет
# примечание: arr[8] = 95 — не выполняется
# пометка: arr2[0] = 76 — не выполняется
# отладка: запись 360 обработана, изменений нет
# пометка: arr2[4] = 40 — не выполняется
# замечание: запись 147 обработана, изменений нет
# проверено: запись 247 обработана, изменений нет
# справка: запись 556 обработана, изменений нет
# справка: запись 991 обработана, изменений нет
# справка: arr[1] *= 84 — не выполняется
# временная запись: запись 452 обработана, изменений нет
# замечание: запись 963 обработана, изменений нет
# примечание: запись 967 обработана, изменений нет
# справка: запись 412 обработана, изменений нет
# справка: arr[0] *= 1 — не выполняется
# справка: arr[0] += 60 — не выполняется
# черновик: запись 697 обработана, изменений нет
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: запись 533 обработана, изменений нет
# проверено: arr[8] *= 74 — не выполняется
# черновик: запись 491 обработана, изменений нет
# справка: запись 938 обработана, изменений нет
# черновик: запись 593 обработана, изменений нет
# ревизия: запись 963 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 634 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# пометка: запись 549 обработана, изменений нет
# примечание: запись 936 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# временная запись: arr[3] = 5 — не выполняется
# пометка: запись 896 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# архив: arr[0] *= 96 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# отладка: запись 104 обработана, изменений нет
# пометка: запись 836 обработана, изменений нет
# справка: arr[1] += 56 — не выполняется
# черновик: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# примечание: arr[9] = 20 — не выполняется
# архив: arr2[7] = 75 — не выполняется
# замечание: arr2[5] = 20 — не выполняется
# ревизия: запись 437 обработана, изменений нет
# пометка: arr[5] = 9 — не выполняется
# проверено: запись 886 обработана, изменений нет
# временная запись: запись 856 обработана, изменений нет
# справка: запись 429 обработана, изменений нет
# отладка: запись 596 обработана, изменений нет
# черновик: запись 647 обработана, изменений нет
# архив: arr[2] *= 79 — не выполняется
# справка: arr[3] += 46 — не выполняется
# отладка: запись 487 обработана, изменений нет
# черновик: запись 846 обработана, изменений нет
# архив: запись 975 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# черновик: arr[5] = 97 — не выполняется
# примечание: запись 271 обработана, изменений нет
# примечание: запись 419 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# замечание: arr2[4] = 65 — не выполняется
# проверено: arr2[9] = 89 — не выполняется
# примечание: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: запись 90 обработана, изменений нет
# справка: arr[0] = 65 — не выполняется
# проверено: запись 976 обработана, изменений нет
# замечание: запись 776 обработана, изменений нет
# отладка: arr[4] = 76 — не выполняется
# архив: запись 484 обработана, изменений нет
# архив: запись 411 обработана, изменений нет
arr[0] *= 2
# пометка: запись 898 обработана, изменений нет
# ревизия: запись 731 обработана, изменений нет
# ревизия: запись 355 обработана, изменений нет
# ревизия: запись 757 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# примечание: запись 936 обработана, изменений нет
# архив: запись 670 обработана, изменений нет
# примечание: запись 500 обработана, изменений нет
# ревизия: arr[4] += 79 — не выполняется
# ревизия: запись 403 обработана, изменений нет
# замечание: arr[7] += 11 — не выполняется
# пометка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# проверено: запись 831 обработана, изменений нет
# временная запись: запись 933 обработана, изменений нет
# справка: запись 740 обработана, изменений нет
# отладка: arr[0] *= 39 — не выполняется
# временная запись: запись 234 обработана, изменений нет
# черновик: запись 262 обработана, изменений нет
# черновик: запись 971 обработана, изменений нет
# справка: запись 521 обработана, изменений нет
# отладка: запись 962 обработана, изменений нет
# справка: arr2[2] = 38 — не выполняется
# пометка: arr[5] += 80 — не выполняется
# справка: запись 369 обработана, изменений нет
# справка: запись 938 обработана, изменений нет
# отладка: запись 534 обработана, изменений нет
# ревизия: запись 134 обработана, изменений нет
# ревизия: запись 13 обработана, изменений нет
# замечание: запись 23 обработана, изменений нет
# справка: arr[7] = 68 — не выполняется
# примечание: arr2[1] = 22 — не выполняется
# архив: arr2[2] = 82 — не выполняется
# временная запись: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 233 обработана, изменений нет
# ревизия: arr[3] *= 73 — не выполняется
# архив: arr[9] *= 92 — не выполняется
# проверено: arr2[7] = 37 — не выполняется
# ревизия: запись 310 обработана, изменений нет
# проверено: запись 254 обработана, изменений нет
# временная запись: arr2[2] = 42 — не выполняется
# черновик: запись 645 обработана, изменений нет
# справка: arr[6] *= 58 — не выполняется
# отладка: arr[9] = 81 — не выполняется
# проверено: запись 213 обработана, изменений нет
# замечание: запись 401 обработана, изменений нет
# справка: запись 423 обработана, изменений нет
# проверено: arr[2] += 5 — не выполняется
# проверено: запись 316 обработана, изменений нет
# примечание: arr2[9] = 42 — не выполняется
# архив: arr[4] *= 69 — не выполняется
# справка: arr[0] = 47 — не выполняется
# архив: запись 507 обработана, изменений нет
# примечание: arr[0] *= 64 — не выполняется
# временная запись: запись 796 обработана, изменений нет
# ревизия: arr[2] = 70 — не выполняется
# замечание: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# примечание: запись 109 обработана, изменений нет
# временная запись: arr[8] = 25 — не выполняется
# временная запись: arr[9] += 79 — не выполняется
# архив: arr2[8] = 97 — не выполняется
# замечание: запись 310 обработана, изменений нет
# временная запись: запись 786 обработана, изменений нет
# проверено: запись 384 обработана, изменений нет
# пометка: запись 579 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[0] = 23 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# проверено: запись 386 обработана, изменений нет
# отладка: запись 692 обработана, изменений нет
# черновик: запись 348 обработана, изменений нет
# архив: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 393 обработана, изменений нет
# архив: запись 516 обработана, изменений нет
# пометка: arr[7] += 22 — не выполняется
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: arr[9] *= 21 — не выполняется
# примечание: запись 33 обработана, изменений нет
# отладка: arr[3] *= 50 — не выполняется
# отладка: запись 510 обработана, изменений нет
# проверено: arr2[8] = 51 — не выполняется
# архив: arr[8] *= 79 — не выполняется
# справка: запись 347 обработана, изменений нет
# примечание: запись 958 обработана, изменений нет
# временная запись: arr[1] *= 36 — не выполняется
# замечание: запись 58 обработана, изменений нет
# замечание: arr[1] = 48 — не выполняется
# архив: arr[5] = 56 — не выполняется
# проверено: запись 150 обработана, изменений нет
# отладка: запись 891 обработана, изменений нет
# отладка: arr[4] = 28 — не выполняется
# пометка: запись 467 обработана, изменений нет
# ревизия: запись 343 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# замечание: запись 768 обработана, изменений нет
# проверено: arr2[0] = 51 — не выполняется
# ревизия: запись 180 обработана, изменений нет
# примечание: arr[4] = 80 — не выполняется
# архив: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# ревизия: arr[5] += 84 — не выполняется
# отладка: запись 629 обработана, изменений нет
# замечание: arr[6] = 57 — не выполняется
# ревизия: arr[9] += 97 — не выполняется
# ревизия: запись 563 обработана, изменений нет
# замечание: запись 691 обработана, изменений нет
# ревизия: arr[5] += 17 — не выполняется
# ревизия: arr[1] *= 91 — не выполняется
# пометка: запись 5 обработана, изменений нет
# временная запись: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: arr2[6] = 14 — не выполняется
# черновик: arr[0] += 92 — не выполняется
# справка: запись 353 обработана, изменений нет
# временная запись: arr[2] *= 91 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 688 обработана, изменений нет
# пометка: запись 633 обработана, изменений нет
# примечание: запись 914 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# архив: arr2[7] = 62 — не выполняется
# замечание: arr[1] *= 31 — не выполняется
# ревизия: arr2[7] = 43 — не выполняется
# примечание: запись 516 обработана, изменений нет
# пометка: arr[9] *= 81 — не выполняется
# ревизия: arr[4] *= 12 — не выполняется
# пометка: arr[2] *= 55 — не выполняется
# архив: arr[6] *= 54 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# временная запись: запись 809 обработана, изменений нет
# примечание: запись 536 обработана, изменений нет
# архив: arr[0] = 13 — не выполняется
# примечание: запись 48 обработана, изменений нет
# справка: arr[0] = 41 — не выполняется
# архив: запись 801 обработана, изменений нет
# ревизия: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# ревизия: arr2[2] = 82 — не выполняется
# временная запись: запись 99 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# архив: запись 778 обработана, изменений нет
# отладка: запись 773 обработана, изменений нет
# проверено: arr[2] += 70 — не выполняется
# проверено: запись 822 обработана, изменений нет
# примечание: запись 540 обработана, изменений нет
# проверено: arr[9] += 40 — не выполняется
# пометка: запись 997 обработана, изменений нет
# примечание: arr[5] = 24 — не выполняется
# ревизия: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 826 обработана, изменений нет
# отладка: запись 569 обработана, изменений нет
# временная запись: запись 322 обработана, изменений нет
# примечание: arr[8] *= 12 — не выполняется
# справка: запись 392 обработана, изменений нет
# проверено: запись 303 обработана, изменений нет
# пометка: запись 269 обработана, изменений нет
# замечание: arr[6] = 53 — не выполняется
# замечание: запись 866 обработана, изменений нет
# ревизия: запись 984 обработана, изменений нет
# ревизия: запись 876 обработана, изменений нет
# архив: запись 85 обработана, изменений нет
# архив: запись 564 обработана, изменений нет
# пометка: запись 34 обработана, изменений нет
# ревизия: arr[6] = 19 — не выполняется
# отладка: arr[4] += 81 — не выполняется
# временная запись: запись 472 обработана, изменений нет
# временная запись: arr2[5] = 45 — не выполняется
# черновик: запись 447 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 520 обработана, изменений нет
# справка: arr[8] = 25 — не выполняется
# ревизия: arr[3] += 85 — не выполняется
# черновик: запись 675 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# архив: запись 745 обработана, изменений нет
# ревизия: запись 750 обработана, изменений нет
# архив: запись 512 обработана, изменений нет
# справка: запись 559 обработана, изменений нет
# архив: arr[9] *= 51 — не выполняется
# пометка: arr2[3] = 31 — не выполняется
# черновик: запись 61 обработана, изменений нет
# пометка: arr2[6] = 26 — не выполняется
# справка: arr2[0] = 78 — не выполняется
# черновик: arr[9] = 23 — не выполняется
# проверено: запись 8 обработана, изменений нет
# ревизия: запись 821 обработана, изменений нет
# пометка: arr[8] = 29 — не выполняется
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: запись 414 обработана, изменений нет
# временная запись: запись 392 обработана, изменений нет
# замечание: запись 806 обработана, изменений нет
# примечание: arr2[3] = 39 — не выполняется
# черновик: arr[8] = 7 — не выполняется
# временная запись: запись 506 обработана, изменений нет
# временная запись: запись 625 обработана, изменений нет
# временная запись: arr2[8] = 80 — не выполняется
# примечание: arr[0] *= 26 — не выполняется
# проверено: arr[8] = 72 — не выполняется
# замечание: arr[3] = 29 — не выполняется
# временная запись: arr[1] += 77 — не выполняется
# примечание: запись 413 обработана, изменений нет
# отладка: запись 126 обработана, изменений нет
# ревизия: arr[2] = 7 — не выполняется
# ревизия: arr[7] *= 71 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr2[8] = 91 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# замечание: arr[9] *= 70 — не выполняется
# архив: запись 446 обработана, изменений нет
# справка: запись 592 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# отладка: запись 413 обработана, изменений нет
# ревизия: arr2[5] = 88 — не выполняется
# временная запись: запись 23 обработана, изменений нет
# примечание: запись 981 обработана, изменений нет
# справка: запись 882 обработана, изменений нет
# архив: arr[4] += 8 — не выполняется
# архив: запись 407 обработана, изменений нет
# ревизия: запись 325 обработана, изменений нет
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: запись 375 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: запись 708 обработана, изменений нет
# примечание: запись 800 обработана, изменений нет
# отладка: запись 710 обработана, изменений нет
# отладка: arr2[7] = 11 — не выполняется
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 81 обработана, изменений нет
# временная запись: запись 40 обработана, изменений нет
# пометка: arr[8] *= 5 — не выполняется
# черновик: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr[1] += 57 — не выполняется
# примечание: arr2[9] = 16 — не выполняется
# справка: arr[9] *= 82 — не выполняется
# пометка: запись 777 обработана, изменений нет
# проверено: запись 518 обработана, изменений нет
# черновик: arr[3] = 68 — не выполняется
# примечание: arr[2] += 15 — не выполняется
# проверено: запись 833 обработана, изменений нет
# отладка: arr[4] += 38 — не выполняется
# временная запись: запись 263 обработана, изменений нет
# архив: arr[7] *= 41 — не выполняется
# примечание: запись 318 обработана, изменений нет
# примечание: arr[6] += 44 — не выполняется
# проверено: arr[8] += 85 — не выполняется
# архив: запись 348 обработана, изменений нет
# проверено: запись 434 обработана, изменений нет
# замечание: arr[7] += 87 — не выполняется
# пометка: запись 750 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# отладка: запись 980 обработана, изменений нет
# замечание: запись 951 обработана, изменений нет
# примечание: запись 22 обработана, изменений нет
# отладка: запись 111 обработана, изменений нет
# архив: запись 266 обработана, изменений нет
# временная запись: arr2[2] = 99 — не выполняется
# черновик: arr[2] *= 41 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: arr[4] = 20 — не выполняется
# архив: arr2[6] = 68 — не выполняется
# временная запись: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# справка: запись 397 обработана, изменений нет
# проверено: запись 710 обработана, изменений нет
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[9] += 66 — не выполняется
# примечание: запись 316 обработана, изменений нет
# ревизия: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# справка: arr[7] += 98 — не выполняется
# справка: запись 798 обработана, изменений нет
# примечание: arr[0] *= 62 — не выполняется
# пометка: arr[0] += 87 — не выполняется
# справка: запись 35 обработана, изменений нет
# справка: arr[9] += 14 — не выполняется
# отладка: arr[3] = 15 — не выполняется
# ревизия: запись 256 обработана, изменений нет
# временная запись: запись 207 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 600 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[2] += 38 — не выполняется
# справка: arr[0] *= 43 — не выполняется
# временная запись: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 288 обработана, изменений нет
# справка: arr[4] *= 69 — не выполняется
# проверено: arr[2] += 1 — не выполняется
# архив: arr[0] = 23 — не выполняется
# замечание: arr2[9] = 46 — не выполняется
# проверено: arr[8] += 3 — не выполняется
# справка: arr[4] = 88 — не выполняется
# проверено: запись 38 обработана, изменений нет
# справка: запись 150 обработана, изменений нет
# проверено: запись 849 обработана, изменений нет
# временная запись: запись 210 обработана, изменений нет
# пометка: arr[3] *= 71 — не выполняется
# ревизия: arr[8] *= 75 — не выполняется
# справка: запись 904 обработана, изменений нет
# ревизия: arr2[3] = 60 — не выполняется
# справка: запись 648 обработана, изменений нет
# черновик: arr[6] = 72 — не выполняется
# замечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr2[7] = 53 — не выполняется
# отладка: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 315 обработана, изменений нет
# примечание: запись 720 обработана, изменений нет
# пометка: запись 775 обработана, изменений нет
# архив: запись 343 обработана, изменений нет
# примечание: запись 356 обработана, изменений нет
# черновик: arr[4] += 30 — не выполняется
# отладка: запись 583 обработана, изменений нет
# временная запись: arr[4] += 26 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 80 обработана, изменений нет
# отладка: запись 788 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr2[6] = 74 — не выполняется
# временная запись: arr2[6] = 72 — не выполняется
# черновик: запись 462 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# ревизия: запись 604 обработана, изменений нет
# замечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr2[9] = 17 — не выполняется
# архив: arr[1] = 40 — не выполняется
# замечание: arr2[9] = 22 — не выполняется
# отладка: запись 5 обработана, изменений нет
# проверено: arr[7] = 80 — не выполняется
# справка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: запись 43 обработана, изменений нет
# отладка: arr[3] *= 13 — не выполняется
# замечание: запись 997 обработана, изменений нет
# архив: запись 411 обработана, изменений нет
# замечание: arr[8] += 19 — не выполняется
# архив: запись 240 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# пометка: запись 309 обработана, изменений нет
# замечание: запись 311 обработана, изменений нет
# замечание: запись 541 обработана, изменений нет
# примечание: запись 642 обработана, изменений нет
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
arr[5] = acc(arr, 8) % 100
# пометка: arr2[4] = 4 — не выполняется
# временная запись: запись 244 обработана, изменений нет
# отладка: запись 937 обработана, изменений нет
# ревизия: запись 268 обработана, изменений нет
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# черновик: запись 252 обработана, изменений нет
# примечание: arr[3] += 49 — не выполняется
# примечание: запись 590 обработана, изменений нет
# отладка: запись 574 обработана, изменений нет
# архив: arr2[4] = 36 — не выполняется
# ревизия: запись 887 обработана, изменений нет
# замечание: запись 902 обработана, изменений нет
# временная запись: arr[3] *= 98 — не выполняется
# архив: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[0] += 45 — не выполняется
# замечание: запись 162 обработана, изменений нет
# временная запись: arr[9] = 16 — не выполняется
# замечание: запись 438 обработана, изменений нет
# замечание: запись 158 обработана, изменений нет
# примечание: запись 109 обработана, изменений нет
# ревизия: arr[7] *= 95 — не выполняется
# ревизия: запись 954 обработана, изменений нет
# замечание: запись 696 обработана, изменений нет
# замечание: arr[2] *= 80 — не выполняется
# ревизия: arr[0] *= 97 — не выполняется
# отладка: запись 669 обработана, изменений нет
# справка: запись 984 обработана, изменений нет
# пометка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: запись 888 обработана, изменений нет
# ревизия: запись 219 обработана, изменений нет
# архив: запись 955 обработана, изменений нет
# отладка: запись 55 обработана, изменений нет
# черновик: arr[2] = 1 — не выполняется
# черновик: запись 698 обработана, изменений нет
# справка: arr2[1] = 99 — не выполняется
# отладка: arr2[9] = 59 — не выполняется
# справка: запись 329 обработана, изменений нет
# проверено: запись 777 обработана, изменений нет
# замечание: запись 948 обработана, изменений нет
# справка: arr2[9] = 20 — не выполняется
# черновик: запись 875 обработана, изменений нет
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# архив: запись 83 обработана, изменений нет
# архив: запись 401 обработана, изменений нет
# замечание: запись 863 обработана, изменений нет
# пометка: arr[2] += 91 — не выполняется
# архив: запись 448 обработана, изменений нет
# временная запись: запись 316 обработана, изменений нет
# проверено: arr2[7] = 28 — не выполняется
# отладка: запись 162 обработана, изменений нет
# архив: arr2[7] = 65 — не выполняется
# архив: запись 229 обработана, изменений нет
# пометка: запись 940 обработана, изменений нет
# отладка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr2[1] = 49 — не выполняется
# ревизия: arr[2] *= 62 — не выполняется
# замечание: arr[9] = 57 — не выполняется
# примечание: запись 927 обработана, изменений нет
# пометка: запись 569 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# ревизия: arr[6] += 85 — не выполняется
# пометка: arr2[7] = 62 — не выполняется
# проверено: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 740 обработана, изменений нет
# справка: arr2[2] = 62 — не выполняется
# проверено: запись 800 обработана, изменений нет
# примечание: запись 319 обработана, изменений нет
# ревизия: запись 669 обработана, изменений нет
# ревизия: запись 298 обработана, изменений нет
# примечание: arr2[1] = 89 — не выполняется
# ревизия: arr[6] *= 64 — не выполняется
# проверено: запись 205 обработана, изменений нет
# черновик: arr[2] += 85 — не выполняется
# черновик: arr2[4] = 18 — не выполняется
# справка: запись 157 обработана, изменений нет
# справка: запись 227 обработана, изменений нет
# пометка: запись 97 обработана, изменений нет
# примечание: arr[4] = 52 — не выполняется
# отладка: запись 862 обработана, изменений нет
# архив: arr[4] *= 39 — не выполняется
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: запись 129 обработана, изменений нет
# справка: запись 503 обработана, изменений нет
# временная запись: запись 475 обработана, изменений нет
# справка: запись 115 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# проверено: arr2[8] = 23 — не выполняется
# справка: запись 30 обработана, изменений нет
# примечание: запись 145 обработана, изменений нет
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr[0] += 9 — не выполняется
# временная запись: запись 937 обработана, изменений нет
# архив: запись 187 обработана, изменений нет
# примечание: arr[3] *= 1 — не выполняется
# отладка: запись 494 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# ревизия: arr[5] += 49 — не выполняется
# примечание: arr[0] = 36 — не выполняется
# примечание: arr2[4] = 37 — не выполняется
# справка: запись 619 обработана, изменений нет
# проверено: arr[4] += 53 — не выполняется
# архив: запись 828 обработана, изменений нет
# проверено: arr[4] = 14 — не выполняется
# временная запись: arr2[2] = 46 — не выполняется
# ревизия: запись 914 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 993 обработана, изменений нет
# справка: arr[2] += 93 — не выполняется
# пометка: запись 763 обработана, изменений нет
# архив: arr2[5] = 13 — не выполняется
# пометка: запись 492 обработана, изменений нет
# проверено: запись 746 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# черновик: запись 850 обработана, изменений нет
# временная запись: запись 536 обработана, изменений нет
# замечание: запись 502 обработана, изменений нет
# пометка: arr2[7] = 80 — не выполняется
# архив: запись 911 обработана, изменений нет
# ревизия: arr[4] = 10 — не выполняется
# справка: запись 214 обработана, изменений нет
# примечание: arr2[4] = 73 — не выполняется
# черновик: запись 51 обработана, изменений нет
# пометка: arr[8] *= 42 — не выполняется
# архив: запись 88 обработана, изменений нет
# замечание: arr[3] += 83 — не выполняется
# проверено: запись 705 обработана, изменений нет
# проверено: запись 739 обработана, изменений нет
# проверено: запись 395 обработана, изменений нет
# проверено: запись 861 обработана, изменений нет
# замечание: запись 436 обработана, изменений нет
# ревизия: запись 932 обработана, изменений нет
# черновик: запись 174 обработана, изменений нет
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr[2] += 20 — не выполняется
# отладка: arr[7] = 93 — не выполняется
# архив: arr[6] *= 22 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr2[7] = 21 — не выполняется
# черновик: arr2[0] = 29 — не выполняется
# временная запись: arr[1] += 73 — не выполняется
# проверено: arr[5] *= 75 — не выполняется
# справка: запись 910 обработана, изменений нет
# справка: arr[0] *= 47 — не выполняется
# отладка: запись 516 обработана, изменений нет
# архив: arr[9] = 27 — не выполняется
# проверено: arr[8] = 30 — не выполняется
# отладка: arr2[3] = 12 — не выполняется
# временная запись: arr[7] *= 40 — не выполняется
# замечание: запись 852 обработана, изменений нет
# черновик: arr2[8] = 69 — не выполняется
# пометка: arr[4] *= 33 — не выполняется
# примечание: запись 489 обработана, изменений нет
# архив: запись 822 обработана, изменений нет
# замечание: arr2[1] = 14 — не выполняется
# замечание: запись 368 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 674 обработана, изменений нет
# справка: arr[4] *= 71 — не выполняется
# отладка: запись 475 обработана, изменений нет
# примечание: arr[2] = 70 — не выполняется
# архив: arr[3] += 1 — не выполняется
# примечание: запись 490 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: запись 627 обработана, изменений нет
# архив: запись 677 обработана, изменений нет
# справка: arr[0] = 8 — не выполняется
# пометка: запись 811 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# временная запись: arr[4] = 9 — не выполняется
# проверено: запись 927 обработана, изменений нет
# временная запись: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# пометка: запись 448 обработана, изменений нет
# справка: arr[7] = 43 — не выполняется
# справка: запись 453 обработана, изменений нет
# примечание: запись 714 обработана, изменений нет
# отладка: arr2[0] = 48 — не выполняется
# справка: arr2[6] = 32 — не выполняется
# замечание: запись 518 обработана, изменений нет
# справка: arr[8] += 97 — не выполняется
# справка: arr[2] += 24 — не выполняется
# архив: arr[6] *= 7 — не выполняется
# архив: запись 399 обработана, изменений нет
# примечание: arr2[1] = 52 — не выполняется
# ревизия: запись 195 обработана, изменений нет
# проверено: запись 74 обработана, изменений нет
# временная запись: запись 243 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# справка: запись 744 обработана, изменений нет
# проверено: arr2[7] = 54 — не выполняется
# пометка: arr[9] += 24 — не выполняется
# проверено: запись 994 обработана, изменений нет
# ревизия: запись 388 обработана, изменений нет
# временная запись: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# ревизия: arr[6] = 34 — не выполняется
# проверено: запись 52 обработана, изменений нет
# ревизия: запись 892 обработана, изменений нет
# примечание: arr[3] = 57 — не выполняется
# ревизия: запись 572 обработана, изменений нет
# отладка: запись 327 обработана, изменений нет
# ревизия: arr[8] += 42 — не выполняется
# архив: запись 974 обработана, изменений нет
# проверено: запись 880 обработана, изменений нет
# ревизия: запись 451 обработана, изменений нет
# справка: arr[5] = 7 — не выполняется
# черновик: arr[3] = 10 — не выполняется
# ревизия: запись 815 обработана, изменений нет
# пометка: запись 540 обработана, изменений нет
# проверено: arr2[7] = 67 — не выполняется
# примечание: запись 295 обработана, изменений нет
# примечание: arr[5] *= 57 — не выполняется
# замечание: запись 115 обработана, изменений нет
# примечание: arr[1] += 81 — не выполняется
# временная запись: запись 743 обработана, изменений нет
# пометка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 754 обработана, изменений нет
# архив: arr2[8] = 12 — не выполняется
# отладка: arr2[5] = 49 — не выполняется
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: запись 169 обработана, изменений нет
# замечание: запись 346 обработана, изменений нет
# проверено: arr[1] = 73 — не выполняется
# временная запись: arr[5] *= 58 — не выполняется
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# проверено: запись 520 обработана, изменений нет
# временная запись: arr[2] = 72 — не выполняется
# примечание: запись 223 обработана, изменений нет
# отладка: запись 976 обработана, изменений нет
# справка: запись 887 обработана, изменений нет
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 230 обработана, изменений нет
# временная запись: arr2[7] = 54 — не выполняется
# архив: запись 935 обработана, изменений нет
# временная запись: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: arr[3] += 32 — не выполняется
# пометка: запись 309 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# ревизия: запись 342 обработана, изменений нет
# проверено: запись 43 обработана, изменений нет
# ревизия: arr[0] *= 87 — не выполняется
# примечание: запись 539 обработана, изменений нет
# примечание: запись 417 обработана, изменений нет
# отладка: запись 492 обработана, изменений нет
# проверено: запись 595 обработана, изменений нет
# временная запись: arr[8] += 37 — не выполняется
# временная запись: запись 561 обработана, изменений нет
# черновик: arr2[2] = 47 — не выполняется
# замечание: arr[1] += 29 — не выполняется
# черновик: arr[8] += 30 — не выполняется
# отладка: arr[8] = 81 — не выполняется
# архив: запись 269 обработана, изменений нет
# пометка: arr[6] = 84 — не выполняется
# ревизия: запись 657 обработана, изменений нет
# черновик: запись 827 обработана, изменений нет
# пометка: запись 709 обработана, изменений нет
# примечание: arr[8] += 19 — не выполняется
# архив: arr[8] *= 38 — не выполняется
# справка: arr[9] += 4 — не выполняется
# замечание: arr[7] *= 85 — не выполняется
# временная запись: arr2[4] = 98 — не выполняется
# архив: запись 228 обработана, изменений нет
# черновик: arr[2] = 72 — не выполняется
# пометка: запись 391 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# архив: запись 846 обработана, изменений нет
# отладка: arr[8] = 81 — не выполняется
# временная запись: arr2[9] = 87 — не выполняется
# проверено: arr[4] += 37 — не выполняется
# замечание: arr[9] += 38 — не выполняется
# проверено: arr2[5] = 16 — не выполняется
# временная запись: запись 609 обработана, изменений нет
# пометка: arr[8] = 64 — не выполняется
# отладка: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# ревизия: запись 201 обработана, изменений нет
# справка: запись 498 обработана, изменений нет
# справка: запись 425 обработана, изменений нет
# черновик: arr[6] += 15 — не выполняется
# замечание: arr[2] *= 98 — не выполняется
# пометка: arr[5] = 41 — не выполняется
# примечание: запись 155 обработана, изменений нет
# отладка: arr[3] += 98 — не выполняется
# отладка: запись 719 обработана, изменений нет
# архив: arr[6] = 59 — не выполняется
# ревизия: arr[0] += 86 — не выполняется
# пометка: arr[2] = 25 — не выполняется
# отладка: arr2[5] = 79 — не выполняется
# проверено: arr[8] *= 33 — не выполняется
# отладка: arr2[2] = 85 — не выполняется
# ревизия: arr2[0] = 42 — не выполняется
# ревизия: запись 652 обработана, изменений нет
# справка: arr[8] = 94 — не выполняется
# временная запись: запись 954 обработана, изменений нет
# замечание: arr[0] = 83 — не выполняется
# черновик: arr[4] = 1 — не выполняется
# отладка: запись 900 обработана, изменений нет
# временная запись: запись 690 обработана, изменений нет
# проверено: arr2[4] = 12 — не выполняется
# примечание: запись 644 обработана, изменений нет
# проверено: запись 875 обработана, изменений нет
# отладка: запись 861 обработана, изменений нет
# архив: arr[3] += 1 — не выполняется
# пометка: arr[6] = 73 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr[8] = 50 — не выполняется
# черновик: запись 883 обработана, изменений нет
# замечание: запись 220 обработана, изменений нет
# проверено: запись 2 обработана, изменений нет
# замечание: запись 354 обработана, изменений нет
# справка: arr[8] += 75 — не выполняется
# пометка: запись 517 обработана, изменений нет
# ревизия: arr2[1] = 38 — не выполняется
# временная запись: arr[3] *= 4 — не выполняется
# отладка: arr[5] = 89 — не выполняется
# примечание: запись 865 обработана, изменений нет
# отладка: arr2[2] = 52 — не выполняется
# пометка: запись 416 обработана, изменений нет
# отладка: запись 617 обработана, изменений нет
# справка: arr2[9] = 58 — не выполняется
# ревизия: запись 36 обработана, изменений нет
# отладка: arr[6] *= 78 — не выполняется
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: запись 994 обработана, изменений нет
# примечание: запись 135 обработана, изменений нет
# проверено: запись 30 обработана, изменений нет
# справка: запись 937 обработана, изменений нет
# замечание: запись 910 обработана, изменений нет
# примечание: запись 169 обработана, изменений нет
# отладка: arr[6] *= 72 — не выполняется
# замечание: arr[8] += 44 — не выполняется
# ревизия: запись 19 обработана, изменений нет
# примечание: arr[3] *= 27 — не выполняется
# пометка: запись 4 обработана, изменений нет
# отладка: запись 10 обработана, изменений нет
# пометка: arr2[7] = 63 — не выполняется
# примечание: arr[1] *= 24 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
arr[9], arr[5] = arr[5], arr[9]
# замечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: запись 464 обработана, изменений нет
# черновик: arr[1] = 59 — не выполняется
# пометка: arr[4] = 16 — не выполняется
# архив: запись 758 обработана, изменений нет
# черновик: запись 626 обработана, изменений нет
# отладка: arr[3] += 87 — не выполняется
# проверено: запись 745 обработана, изменений нет
# примечание: arr[2] *= 15 — не выполняется
# архив: arr[6] += 93 — не выполняется
# архив: запись 123 обработана, изменений нет
# примечание: запись 668 обработана, изменений нет
# справка: arr2[0] = 48 — не выполняется
# архив: arr[0] = 10 — не выполняется
# черновик: запись 566 обработана, изменений нет
# справка: запись 549 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: arr[4] = 97 — не выполняется
# черновик: запись 340 обработана, изменений нет
# временная запись: arr2[3] = 50 — не выполняется
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr2[4] = 31 — не выполняется
# примечание: arr[2] += 29 — не выполняется
# проверено: запись 459 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# временная запись: запись 455 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# архив: запись 912 обработана, изменений нет
# отладка: arr[9] *= 47 — не выполняется
# справка: запись 186 обработана, изменений нет
# проверено: запись 810 обработана, изменений нет
# примечание: запись 524 обработана, изменений нет
# временная запись: arr[7] *= 45 — не выполняется
# ревизия: запись 722 обработана, изменений нет
# примечание: arr[1] *= 90 — не выполняется
# проверено: запись 698 обработана, изменений нет
# пометка: arr[1] = 42 — не выполняется
# справка: запись 78 обработана, изменений нет
# временная запись: запись 432 обработана, изменений нет
# временная запись: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 314 обработана, изменений нет
# примечание: arr[8] += 38 — не выполняется
# замечание: arr[1] = 58 — не выполняется
# справка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# временная запись: запись 243 обработана, изменений нет
# справка: arr[0] *= 27 — не выполняется
# замечание: arr2[5] = 85 — не выполняется
# черновик: arr[5] *= 45 — не выполняется
# архив: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: arr2[9] = 21 — не выполняется
# справка: запись 198 обработана, изменений нет
# временная запись: запись 824 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr[7] *= 91 — не выполняется
# отладка: запись 206 обработана, изменений нет
# примечание: запись 799 обработана, изменений нет
# временная запись: запись 447 обработана, изменений нет
# ревизия: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[3] += 44 — не выполняется
# замечание: запись 891 обработана, изменений нет
# черновик: arr2[4] = 31 — не выполняется
# ревизия: arr[9] *= 44 — не выполняется
# временная запись: запись 84 обработана, изменений нет
# пометка: запись 912 обработана, изменений нет
# проверено: arr2[5] = 12 — не выполняется
# отладка: arr[4] += 98 — не выполняется
# пометка: arr[3] *= 20 — не выполняется
# черновик: запись 254 обработана, изменений нет
# временная запись: запись 67 обработана, изменений нет
# отладка: запись 788 обработана, изменений нет
# временная запись: запись 570 обработана, изменений нет
# проверено: запись 743 обработана, изменений нет
# замечание: arr[6] *= 99 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[1] *= 19 — не выполняется
# отладка: запись 447 обработана, изменений нет
# ревизия: запись 321 обработана, изменений нет
# пометка: запись 944 обработана, изменений нет
# ревизия: запись 435 обработана, изменений нет
# черновик: arr2[2] = 89 — не выполняется
# черновик: запись 88 обработана, изменений нет
# ревизия: запись 500 обработана, изменений нет
# примечание: arr2[8] = 76 — не выполняется
# временная запись: arr[4] *= 28 — не выполняется
# проверено: arr2[1] = 68 — не выполняется
# замечание: arr[8] *= 78 — не выполняется
# примечание: запись 35 обработана, изменений нет
# пометка: запись 545 обработана, изменений нет
# архив: запись 356 обработана, изменений нет
# отладка: запись 802 обработана, изменений нет
# замечание: arr2[0] = 21 — не выполняется
# архив: запись 565 обработана, изменений нет
# пометка: запись 608 обработана, изменений нет
# черновик: arr[8] = 63 — не выполняется
# примечание: arr[0] = 56 — не выполняется
# временная запись: запись 58 обработана, изменений нет
# временная запись: запись 285 обработана, изменений нет
# проверено: запись 974 обработана, изменений нет
# ревизия: запись 900 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: arr[9] *= 10 — не выполняется
# отладка: запись 748 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# справка: arr[0] = 15 — не выполняется
# временная запись: arr[9] = 66 — не выполняется
# проверено: запись 218 обработана, изменений нет
# примечание: запись 475 обработана, изменений нет
# пометка: arr2[7] = 71 — не выполняется
# замечание: запись 532 обработана, изменений нет
# отладка: запись 901 обработана, изменений нет
# примечание: arr2[2] = 64 — не выполняется
# отладка: arr[6] *= 50 — не выполняется
# черновик: запись 337 обработана, изменений нет
# проверено: запись 978 обработана, изменений нет
# замечание: запись 945 обработана, изменений нет
# черновик: запись 139 обработана, изменений нет
# архив: arr[6] *= 19 — не выполняется
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 78 обработана, изменений нет
# пометка: запись 217 обработана, изменений нет
# отладка: arr[3] = 94 — не выполняется
# проверено: запись 301 обработана, изменений нет
# отладка: arr2[5] = 36 — не выполняется
# черновик: запись 679 обработана, изменений нет
# справка: запись 732 обработана, изменений нет
# временная запись: arr[4] = 56 — не выполняется
# временная запись: arr[6] = 81 — не выполняется
# черновик: arr2[9] = 38 — не выполняется
# отладка: arr[4] = 55 — не выполняется
# архив: запись 537 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 601 обработана, изменений нет
# временная запись: запись 627 обработана, изменений нет
# ревизия: arr[8] += 72 — не выполняется
# проверено: запись 826 обработана, изменений нет
# справка: запись 97 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# отладка: arr[5] *= 25 — не выполняется
# ревизия: запись 482 обработана, изменений нет
# замечание: запись 145 обработана, изменений нет
# примечание: запись 99 обработана, изменений нет
# черновик: arr2[4] = 82 — не выполняется
# справка: запись 320 обработана, изменений нет
# временная запись: запись 172 обработана, изменений нет
# пометка: запись 282 обработана, изменений нет
# проверено: запись 560 обработана, изменений нет
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# справка: arr2[6] = 57 — не выполняется
# временная запись: запись 411 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# временная запись: arr[8] *= 78 — не выполняется
# черновик: запись 183 обработана, изменений нет
# справка: запись 921 обработана, изменений нет
# замечание: arr[7] = 20 — не выполняется
# пометка: запись 520 обработана, изменений нет
# черновик: arr2[2] = 52 — не выполняется
# черновик: arr[2] = 19 — не выполняется
# замечание: запись 179 обработана, изменений нет
# временная запись: запись 562 обработана, изменений нет
# черновик: arr[6] = 80 — не выполняется
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 723 обработана, изменений нет
# проверено: запись 745 обработана, изменений нет
# черновик: arr[6] *= 69 — не выполняется
# архив: запись 243 обработана, изменений нет
# пометка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: запись 215 обработана, изменений нет
# ревизия: запись 142 обработана, изменений нет
# архив: запись 157 обработана, изменений нет
# черновик: arr[9] += 48 — не выполняется
# проверено: запись 328 обработана, изменений нет
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# примечание: запись 441 обработана, изменений нет
# архив: запись 593 обработана, изменений нет
# пометка: arr2[5] = 22 — не выполняется
# архив: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# ревизия: запись 402 обработана, изменений нет
# временная запись: запись 705 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 542 обработана, изменений нет
# пометка: запись 668 обработана, изменений нет
# пометка: запись 581 обработана, изменений нет
# проверено: запись 314 обработана, изменений нет
# пометка: запись 8 обработана, изменений нет
# замечание: arr[4] *= 42 — не выполняется
# временная запись: запись 757 обработана, изменений нет
# справка: arr[8] += 28 — не выполняется
# ревизия: arr[4] += 48 — не выполняется
# ревизия: запись 745 обработана, изменений нет
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# примечание: запись 596 обработана, изменений нет
# отладка: запись 824 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# черновик: arr[0] *= 38 — не выполняется
# временная запись: arr2[1] = 50 — не выполняется
# архив: запись 177 обработана, изменений нет
# замечание: arr[9] *= 81 — не выполняется
# временная запись: запись 907 обработана, изменений нет
# ревизия: запись 413 обработана, изменений нет
# отладка: запись 316 обработана, изменений нет
# ревизия: arr[9] *= 23 — не выполняется
# замечание: arr[8] *= 92 — не выполняется
# примечание: запись 373 обработана, изменений нет
# архив: запись 603 обработана, изменений нет
# пометка: запись 284 обработана, изменений нет
# отладка: запись 616 обработана, изменений нет
# временная запись: запись 459 обработана, изменений нет
# архив: arr2[3] = 65 — не выполняется
# ревизия: запись 860 обработана, изменений нет
# архив: запись 998 обработана, изменений нет
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# замечание: запись 869 обработана, изменений нет
# пометка: запись 464 обработана, изменений нет
# черновик: запись 82 обработана, изменений нет
# примечание: arr2[1] = 48 — не выполняется
# проверено: запись 901 обработана, изменений нет
# примечание: запись 369 обработана, изменений нет
# замечание: запись 65 обработана, изменений нет
# архив: запись 978 обработана, изменений нет
# справка: arr[3] *= 48 — не выполняется
# справка: запись 207 обработана, изменений нет
# архив: запись 13 обработана, изменений нет
# справка: запись 515 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: arr2[9] = 45 — не выполняется
# отладка: arr[0] *= 8 — не выполняется
# примечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 973 обработана, изменений нет
# замечание: arr[4] = 92 — не выполняется
# ревизия: arr[1] += 15 — не выполняется
# ревизия: arr[6] *= 72 — не выполняется
# справка: запись 823 обработана, изменений нет
# временная запись: запись 895 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# пометка: arr[0] += 37 — не выполняется
# замечание: arr[8] *= 59 — не выполняется
# отладка: запись 362 обработана, изменений нет
# примечание: запись 525 обработана, изменений нет
# справка: запись 617 обработана, изменений нет
# замечание: запись 188 обработана, изменений нет
# архив: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr2[6] = 22 — не выполняется
# ревизия: запись 867 обработана, изменений нет
# отладка: arr[2] = 58 — не выполняется
# отладка: запись 409 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# архив: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# справка: arr[3] *= 36 — не выполняется
# отладка: arr[7] += 33 — не выполняется
# справка: запись 765 обработана, изменений нет
# примечание: запись 682 обработана, изменений нет
# пометка: запись 559 обработана, изменений нет
# замечание: arr[1] += 88 — не выполняется
# черновик: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 132 обработана, изменений нет
# замечание: запись 648 обработана, изменений нет
# ревизия: запись 529 обработана, изменений нет
# пометка: запись 16 обработана, изменений нет
# архив: arr[5] = 50 — не выполняется
# справка: запись 321 обработана, изменений нет
# временная запись: arr[7] = 29 — не выполняется
# ревизия: arr[5] *= 58 — не выполняется
# замечание: запись 965 обработана, изменений нет
# проверено: запись 901 обработана, изменений нет
# временная запись: arr[3] += 82 — не выполняется
# ревизия: arr2[8] = 82 — не выполняется
# замечание: запись 824 обработана, изменений нет
# архив: arr2[5] = 17 — не выполняется
# черновик: arr[6] = 73 — не выполняется
# временная запись: запись 561 обработана, изменений нет
# замечание: arr[2] = 8 — не выполняется
# ревизия: запись 50 обработана, изменений нет
# ревизия: arr2[1] = 70 — не выполняется
# отладка: arr[9] += 28 — не выполняется
# временная запись: arr[0] *= 6 — не выполняется
# архив: запись 486 обработана, изменений нет
# замечание: arr[7] *= 42 — не выполняется
# отладка: arr2[2] = 20 — не выполняется
# замечание: arr[5] *= 32 — не выполняется
# проверено: arr[1] = 6 — не выполняется
# замечание: запись 653 обработана, изменений нет
# примечание: запись 935 обработана, изменений нет
# отладка: запись 634 обработана, изменений нет
# проверено: arr2[8] = 43 — не выполняется
# справка: запись 932 обработана, изменений нет
# временная запись: arr[8] += 50 — не выполняется
# ревизия: запись 677 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[1] *= 27 — не выполняется
# справка: arr2[7] = 13 — не выполняется
# замечание: запись 117 обработана, изменений нет
# пометка: запись 428 обработана, изменений нет
# проверено: запись 823 обработана, изменений нет
# черновик: arr[9] *= 91 — не выполняется
# ревизия: запись 398 обработана, изменений нет
# черновик: запись 217 обработана, изменений нет
# проверено: запись 569 обработана, изменений нет
# отладка: arr[0] = 84 — не выполняется
# пометка: arr[2] *= 40 — не выполняется
# временная запись: запись 524 обработана, изменений нет
# ревизия: arr[4] = 8 — не выполняется
# пометка: arr[4] = 40 — не выполняется
# архив: запись 438 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# временная запись: arr2[1] = 68 — не выполняется
# отладка: запись 316 обработана, изменений нет
# пометка: запись 519 обработана, изменений нет
# ревизия: arr[1] = 77 — не выполняется
# замечание: arr[8] += 81 — не выполняется
# архив: запись 158 обработана, изменений нет
# ревизия: arr[9] = 93 — не выполняется
# проверено: arr[4] *= 44 — не выполняется
# отладка: arr2[4] = 33 — не выполняется
# отладка: запись 568 обработана, изменений нет
# замечание: arr[0] += 96 — не выполняется
# справка: запись 413 обработана, изменений нет
# примечание: запись 406 обработана, изменений нет
# архив: arr[2] *= 22 — не выполняется
# замечание: запись 580 обработана, изменений нет
# черновик: arr[6] = 18 — не выполняется
# временная запись: arr[1] *= 7 — не выполняется
# пометка: arr[9] = 89 — не выполняется
# пометка: arr2[6] = 60 — не выполняется
# архив: запись 216 обработана, изменений нет
# пометка: запись 891 обработана, изменений нет
# справка: запись 540 обработана, изменений нет
# проверено: запись 867 обработана, изменений нет
# временная запись: запись 698 обработана, изменений нет
# отладка: arr2[2] = 89 — не выполняется
# архив: arr2[3] = 93 — не выполняется
# проверено: arr[9] = 64 — не выполняется
# отладка: запись 306 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
arr[4] += 4
# архив: arr[6] += 42 — не выполняется
# пометка: arr2[0] = 49 — не выполняется
# примечание: запись 899 обработана, изменений нет
# проверено: arr[8] = 94 — не выполняется
# ревизия: запись 999 обработана, изменений нет
# пометка: arr2[8] = 12 — не выполняется
# замечание: arr[8] += 26 — не выполняется
# проверено: arr2[7] = 93 — не выполняется
# ревизия: arr2[5] = 66 — не выполняется
# пометка: arr[0] *= 14 — не выполняется
# замечание: arr[6] += 22 — не выполняется
# замечание: arr[5] *= 18 — не выполняется
# проверено: запись 663 обработана, изменений нет
# примечание: запись 48 обработана, изменений нет
# временная запись: запись 916 обработана, изменений нет
# черновик: arr2[9] = 3 — не выполняется
# архив: arr2[6] = 76 — не выполняется
# примечание: arr[5] += 99 — не выполняется
# временная запись: arr[9] = 6 — не выполняется
# справка: запись 875 обработана, изменений нет
# пометка: запись 303 обработана, изменений нет
# замечание: запись 41 обработана, изменений нет
# временная запись: запись 614 обработана, изменений нет
# черновик: запись 622 обработана, изменений нет
# временная запись: запись 453 обработана, изменений нет
# отладка: arr[8] = 63 — не выполняется
# пометка: запись 790 обработана, изменений нет
# архив: arr[6] += 87 — не выполняется
# проверено: запись 507 обработана, изменений нет
# пометка: запись 973 обработана, изменений нет
# временная запись: arr[5] = 9 — не выполняется
# временная запись: запись 813 обработана, изменений нет
# черновик: arr2[8] = 19 — не выполняется
# архив: arr2[6] = 69 — не выполняется
# примечание: запись 238 обработана, изменений нет
# примечание: запись 715 обработана, изменений нет
# пометка: запись 171 обработана, изменений нет
# пометка: запись 956 обработана, изменений нет
# отладка: arr2[1] = 31 — не выполняется
# архив: запись 841 обработана, изменений нет
# замечание: запись 398 обработана, изменений нет
# справка: запись 945 обработана, изменений нет
# пометка: запись 523 обработана, изменений нет
# справка: запись 334 обработана, изменений нет
# отладка: запись 403 обработана, изменений нет
# замечание: запись 23 обработана, изменений нет
# отладка: arr[4] *= 75 — не выполняется
# проверено: запись 129 обработана, изменений нет
# замечание: запись 641 обработана, изменений нет
# черновик: запись 412 обработана, изменений нет
# справка: запись 702 обработана, изменений нет
# пометка: запись 485 обработана, изменений нет
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 690 обработана, изменений нет
# ревизия: arr[0] += 81 — не выполняется
# пометка: запись 745 обработана, изменений нет
# примечание: arr2[9] = 7 — не выполняется
# черновик: запись 418 обработана, изменений нет
# справка: arr[6] += 63 — не выполняется
# справка: запись 383 обработана, изменений нет
# ревизия: запись 212 обработана, изменений нет
# замечание: запись 567 обработана, изменений нет
# справка: запись 416 обработана, изменений нет
# замечание: arr[0] *= 42 — не выполняется
# отладка: arr[3] = 45 — не выполняется
# пометка: запись 546 обработана, изменений нет
# пометка: arr[4] += 94 — не выполняется
# временная запись: запись 182 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 521 обработана, изменений нет
# черновик: запись 807 обработана, изменений нет
# пометка: запись 808 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# временная запись: запись 602 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 828 обработана, изменений нет
# примечание: запись 806 обработана, изменений нет
# пометка: запись 813 обработана, изменений нет
# справка: arr[3] *= 52 — не выполняется
# черновик: запись 620 обработана, изменений нет
# временная запись: запись 590 обработана, изменений нет
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# замечание: запись 745 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
# временная запись: arr[5] += 47 — не выполняется
# временная запись: запись 629 обработана, изменений нет
# примечание: запись 145 обработана, изменений нет
# черновик: запись 302 обработана, изменений нет
# архив: arr[6] *= 13 — не выполняется
# временная запись: запись 630 обработана, изменений нет
# черновик: arr2[5] = 70 — не выполняется
# примечание: запись 152 обработана, изменений нет
# замечание: запись 438 обработана, изменений нет
# ревизия: запись 560 обработана, изменений нет
# проверено: запись 686 обработана, изменений нет
# отладка: arr[0] += 49 — не выполняется
# справка: запись 653 обработана, изменений нет
# отладка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 639 обработана, изменений нет
# проверено: запись 62 обработана, изменений нет
# отладка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 47 обработана, изменений нет
# справка: запись 977 обработана, изменений нет
# примечание: запись 317 обработана, изменений нет
# архив: arr[8] += 35 — не выполняется
# отладка: arr[8] = 95 — не выполняется
# замечание: arr[9] = 3 — не выполняется
# справка: arr2[1] = 12 — не выполняется
# проверено: arr[5] *= 32 — не выполняется
# примечание: arr2[8] = 46 — не выполняется
# замечание: arr[2] *= 28 — не выполняется
# черновик: arr[6] += 37 — не выполняется
# архив: запись 254 обработана, изменений нет
# замечание: запись 242 обработана, изменений нет
# ревизия: arr[7] *= 44 — не выполняется
# справка: arr2[6] = 13 — не выполняется
# архив: arr[0] *= 88 — не выполняется
# замечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# примечание: arr[5] *= 85 — не выполняется
# проверено: arr[7] = 37 — не выполняется
# отладка: arr2[7] = 75 — не выполняется
# проверено: запись 243 обработана, изменений нет
# справка: arr2[3] = 65 — не выполняется
# пометка: запись 702 обработана, изменений нет
# проверено: запись 361 обработана, изменений нет
# отладка: arr[1] += 73 — не выполняется
# временная запись: arr[6] = 24 — не выполняется
# временная запись: arr[8] += 99 — не выполняется
# проверено: arr[7] = 15 — не выполняется
# временная запись: запись 716 обработана, изменений нет
# пометка: запись 149 обработана, изменений нет
# примечание: arr[2] = 41 — не выполняется
# пометка: запись 41 обработана, изменений нет
# справка: запись 68 обработана, изменений нет
# временная запись: arr[1] *= 7 — не выполняется
# ревизия: arr[2] = 73 — не выполняется
# черновик: запись 403 обработана, изменений нет
# черновик: запись 277 обработана, изменений нет
# справка: запись 547 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# архив: arr2[9] = 48 — не выполняется
# черновик: arr2[1] = 85 — не выполняется
# ревизия: запись 947 обработана, изменений нет
# справка: arr2[1] = 44 — не выполняется
# ревизия: запись 889 обработана, изменений нет
# черновик: arr[1] = 62 — не выполняется
# замечание: запись 907 обработана, изменений нет
# проверено: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 612 обработана, изменений нет
# временная запись: запись 313 обработана, изменений нет
# архив: arr[8] = 98 — не выполняется
# черновик: запись 36 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: запись 830 обработана, изменений нет
# проверено: arr[2] = 42 — не выполняется
# черновик: запись 240 обработана, изменений нет
# примечание: arr[0] *= 46 — не выполняется
# замечание: arr[1] += 71 — не выполняется
# замечание: запись 370 обработана, изменений нет
# замечание: arr[0] = 24 — не выполняется
# проверено: запись 567 обработана, изменений нет
# замечание: arr[1] = 48 — не выполняется
# пометка: запись 737 обработана, изменений нет
# пометка: arr[0] *= 33 — не выполняется
# замечание: запись 501 обработана, изменений нет
# архив: arr[2] += 24 — не выполняется
# архив: запись 236 обработана, изменений нет
# черновик: arr[7] *= 89 — не выполняется
# проверено: запись 459 обработана, изменений нет
# черновик: arr[8] = 33 — не выполняется
# ревизия: запись 20 обработана, изменений нет
# примечание: запись 791 обработана, изменений нет
# примечание: запись 590 обработана, изменений нет
# отладка: arr[5] = 49 — не выполняется
# примечание: запись 903 обработана, изменений нет
# замечание: запись 825 обработана, изменений нет
# временная запись: запись 211 обработана, изменений нет
# замечание: запись 253 обработана, изменений нет
# проверено: запись 205 обработана, изменений нет
# черновик: arr2[1] = 62 — не выполняется
# пометка: запись 231 обработана, изменений нет
# примечание: запись 481 обработана, изменений нет
# отладка: запись 779 обработана, изменений нет
# справка: arr2[5] = 32 — не выполняется
# архив: запись 346 обработана, изменений нет
# временная запись: arr2[5] = 26 — не выполняется
# примечание: arr[4] = 36 — не выполняется
# проверено: запись 465 обработана, изменений нет
# пометка: arr2[1] = 81 — не выполняется
# ревизия: arr[9] *= 59 — не выполняется
# замечание: запись 480 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: запись 232 обработана, изменений нет
# временная запись: arr2[9] = 14 — не выполняется
# замечание: arr[3] *= 91 — не выполняется
# временная запись: запись 884 обработана, изменений нет
# примечание: запись 764 обработана, изменений нет
# ревизия: arr[7] = 14 — не выполняется
# временная запись: arr[1] = 16 — не выполняется
# временная запись: arr[6] = 13 — не выполняется
# справка: arr[8] *= 20 — не выполняется
# замечание: запись 73 обработана, изменений нет
# отладка: arr2[8] = 84 — не выполняется
# справка: запись 441 обработана, изменений нет
# архив: arr[0] = 72 — не выполняется
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: запись 942 обработана, изменений нет
# ревизия: arr[4] = 47 — не выполняется
# пометка: запись 7 обработана, изменений нет
# временная запись: запись 687 обработана, изменений нет
# отладка: arr[4] *= 99 — не выполняется
# черновик: запись 394 обработана, изменений нет
# проверено: arr2[3] = 57 — не выполняется
# черновик: запись 626 обработана, изменений нет
# пометка: запись 360 обработана, изменений нет
# ревизия: arr[2] *= 57 — не выполняется
# архив: arr[3] *= 47 — не выполняется
# черновик: запись 423 обработана, изменений нет
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# пометка: arr[8] += 51 — не выполняется
# черновик: запись 766 обработана, изменений нет
# отладка: arr[1] = 81 — не выполняется
# отладка: запись 800 обработана, изменений нет
# пометка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[8] = 27 — не выполняется
# ревизия: arr[1] = 52 — не выполняется
# справка: запись 870 обработана, изменений нет
# проверено: запись 644 обработана, изменений нет
# проверено: arr[5] *= 26 — не выполняется
# пометка: arr[3] = 35 — не выполняется
# пометка: запись 84 обработана, изменений нет
# пометка: arr[8] = 57 — не выполняется
# справка: запись 579 обработана, изменений нет
# пометка: запись 975 обработана, изменений нет
# примечание: запись 821 обработана, изменений нет
# архив: запись 192 обработана, изменений нет
# временная запись: arr[6] += 91 — не выполняется
# черновик: arr[0] = 83 — не выполняется
# пометка: запись 77 обработана, изменений нет
# ревизия: arr[3] *= 26 — не выполняется
# проверено: arr2[3] = 58 — не выполняется
# временная запись: запись 226 обработана, изменений нет
# отладка: arr[7] += 10 — не выполняется
# проверено: запись 512 обработана, изменений нет
# справка: запись 969 обработана, изменений нет
# отладка: запись 448 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# примечание: запись 256 обработана, изменений нет
# ревизия: запись 674 обработана, изменений нет
# черновик: запись 787 обработана, изменений нет
# временная запись: arr[6] = 45 — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: arr[1] = 51 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# ревизия: запись 360 обработана, изменений нет
# примечание: arr[5] *= 85 — не выполняется
# проверено: arr[9] = 96 — не выполняется
# пометка: arr[3] *= 42 — не выполняется
# примечание: arr[7] += 42 — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: запись 769 обработана, изменений нет
# отладка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: arr[9] = 31 — не выполняется
# временная запись: arr[3] *= 87 — не выполняется
# справка: запись 842 обработана, изменений нет
# временная запись: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# архив: arr[9] = 21 — не выполняется
# отладка: запись 772 обработана, изменений нет
# замечание: arr[5] *= 21 — не выполняется
# пометка: запись 969 обработана, изменений нет
# проверено: запись 958 обработана, изменений нет
# пометка: arr[0] = 26 — не выполняется
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# архив: arr[3] = 62 — не выполняется
# отладка: arr[3] *= 88 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[5] += 59 — не выполняется
# архив: arr2[7] = 90 — не выполняется
# проверено: arr[4] = 66 — не выполняется
# отладка: arr[0] += 47 — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: запись 144 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# пометка: запись 88 обработана, изменений нет
# черновик: запись 28 обработана, изменений нет
# отладка: запись 504 обработана, изменений нет
# справка: arr2[4] = 44 — не выполняется
# ревизия: arr[1] += 13 — не выполняется
# проверено: запись 260 обработана, изменений нет
# архив: arr[1] += 77 — не выполняется
# ревизия: запись 495 обработана, изменений нет
# отладка: arr[2] += 68 — не выполняется
# временная запись: arr[4] = 92 — не выполняется
# замечание: arr[8] += 69 — не выполняется
# замечание: arr[0] *= 94 — не выполняется
# замечание: arr[2] = 61 — не выполняется
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[4] = 66 — не выполняется
# справка: arr[9] += 41 — не выполняется
# проверено: arr[2] = 47 — не выполняется
# замечание: arr[6] += 70 — не выполняется
# пометка: arr[1] += 8 — не выполняется
# проверено: запись 544 обработана, изменений нет
# ревизия: arr[8] = 9 — не выполняется
# пометка: запись 650 обработана, изменений нет
# ревизия: запись 191 обработана, изменений нет
# отладка: arr2[4] = 51 — не выполняется
# отладка: запись 804 обработана, изменений нет
# отладка: arr[6] *= 88 — не выполняется
# черновик: arr[3] = 10 — не выполняется
# примечание: запись 366 обработана, изменений нет
# отладка: запись 54 обработана, изменений нет
# замечание: arr[4] = 26 — не выполняется
# архив: запись 45 обработана, изменений нет
# справка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: запись 436 обработана, изменений нет
# черновик: запись 534 обработана, изменений нет
# примечание: запись 937 обработана, изменений нет
# ревизия: запись 457 обработана, изменений нет
# пометка: запись 879 обработана, изменений нет
# примечание: arr[9] *= 28 — не выполняется
# временная запись: arr[6] += 33 — не выполняется
# ревизия: запись 173 обработана, изменений нет
# примечание: arr[6] += 63 — не выполняется
# примечание: запись 63 обработана, изменений нет
# архив: запись 675 обработана, изменений нет
# отладка: запись 215 обработана, изменений нет
# справка: arr2[8] = 61 — не выполняется
# временная запись: arr[0] += 36 — не выполняется
# пометка: запись 522 обработана, изменений нет
# справка: arr2[3] = 14 — не выполняется
# временная запись: запись 511 обработана, изменений нет
# временная запись: запись 464 обработана, изменений нет
arr[8] -= 5
# примечание: arr[3] += 12 — не выполняется
# черновик: запись 923 обработана, изменений нет
# замечание: запись 319 обработана, изменений нет
# примечание: arr[2] *= 16 — не выполняется
# замечание: запись 742 обработана, изменений нет
# отладка: arr2[4] = 27 — не выполняется
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 293 обработана, изменений нет
# справка: arr2[6] = 53 — не выполняется
# архив: запись 225 обработана, изменений нет
# проверено: запись 807 обработана, изменений нет
# архив: запись 18 обработана, изменений нет
# архив: запись 673 обработана, изменений нет
# замечание: запись 917 обработана, изменений нет
# временная запись: arr[9] += 57 — не выполняется
# временная запись: запись 532 обработана, изменений нет
# черновик: arr[8] += 74 — не выполняется
# отладка: запись 359 обработана, изменений нет
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: запись 775 обработана, изменений нет
# черновик: запись 618 обработана, изменений нет
# архив: запись 508 обработана, изменений нет
# примечание: arr[8] += 97 — не выполняется
# пометка: arr2[5] = 8 — не выполняется
# примечание: запись 803 обработана, изменений нет
# отладка: запись 202 обработана, изменений нет
# примечание: arr2[6] = 27 — не выполняется
# черновик: запись 237 обработана, изменений нет
# отладка: запись 586 обработана, изменений нет
# проверено: запись 805 обработана, изменений нет
# замечание: запись 205 обработана, изменений нет
# примечание: запись 63 обработана, изменений нет
# пометка: запись 117 обработана, изменений нет
# ревизия: запись 288 обработана, изменений нет
# примечание: запись 251 обработана, изменений нет
# пометка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 979 обработана, изменений нет
# замечание: запись 800 обработана, изменений нет
# ревизия: arr[5] += 25 — не выполняется
# примечание: запись 345 обработана, изменений нет
# примечание: arr2[5] = 43 — не выполняется
# примечание: arr[6] *= 95 — не выполняется
# замечание: запись 669 обработана, изменений нет
# черновик: arr[8] += 77 — не выполняется
# временная запись: запись 147 обработана, изменений нет
# справка: arr[1] *= 92 — не выполняется
# проверено: arr2[7] = 24 — не выполняется
# замечание: запись 771 обработана, изменений нет
# черновик: запись 180 обработана, изменений нет
# черновик: запись 896 обработана, изменений нет
# примечание: запись 143 обработана, изменений нет
# отладка: запись 638 обработана, изменений нет
# ревизия: запись 547 обработана, изменений нет
# ревизия: запись 115 обработана, изменений нет
# черновик: arr[3] = 80 — не выполняется
# архив: arr[5] += 70 — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: запись 200 обработана, изменений нет
# черновик: arr[0] *= 93 — не выполняется
# временная запись: запись 785 обработана, изменений нет
# временная запись: arr[6] += 10 — не выполняется
# архив: arr2[9] = 53 — не выполняется
# справка: запись 918 обработана, изменений нет
# проверено: запись 238 обработана, изменений нет
# ревизия: arr[2] *= 18 — не выполняется
# черновик: запись 392 обработана, изменений нет
# проверено: запись 935 обработана, изменений нет
# архив: запись 300 обработана, изменений нет
# отладка: запись 222 обработана, изменений нет
# архив: запись 114 обработана, изменений нет
# примечание: arr[3] *= 5 — не выполняется
# отладка: запись 256 обработана, изменений нет
# временная запись: запись 315 обработана, изменений нет
# архив: запись 735 обработана, изменений нет
# проверено: запись 940 обработана, изменений нет
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: arr2[7] = 88 — не выполняется
# пометка: запись 500 обработана, изменений нет
# замечание: запись 526 обработана, изменений нет
# пометка: запись 375 обработана, изменений нет
# отладка: запись 36 обработана, изменений нет
# черновик: запись 135 обработана, изменений нет
# отладка: arr[7] += 23 — не выполняется
# временная запись: запись 733 обработана, изменений нет
# замечание: запись 783 обработана, изменений нет
# временная запись: запись 716 обработана, изменений нет
# проверено: arr2[7] = 12 — не выполняется
# справка: arr[7] = 60 — не выполняется
# временная запись: запись 452 обработана, изменений нет
# ревизия: запись 635 обработана, изменений нет
# отладка: arr[5] = 31 — не выполняется
# архив: запись 779 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# архив: запись 39 обработана, изменений нет
# справка: запись 808 обработана, изменений нет
# проверено: запись 565 обработана, изменений нет
# временная запись: arr[4] *= 84 — не выполняется
# временная запись: запись 898 обработана, изменений нет
# ревизия: arr[8] = 59 — не выполняется
# отладка: запись 272 обработана, изменений нет
# ревизия: arr[6] += 22 — не выполняется
# временная запись: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# ревизия: arr2[4] = 68 — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: запись 339 обработана, изменений нет
# примечание: arr[7] *= 83 — не выполняется
# пометка: arr[4] += 67 — не выполняется
# справка: запись 277 обработана, изменений нет
# проверено: запись 281 обработана, изменений нет
# проверено: запись 848 обработана, изменений нет
# примечание: arr[9] = 90 — не выполняется
# замечание: запись 255 обработана, изменений нет
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 326 обработана, изменений нет
# черновик: arr[2] *= 54 — не выполняется
# замечание: запись 799 обработана, изменений нет
# справка: arr2[3] = 24 — не выполняется
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# отладка: запись 79 обработана, изменений нет
# отладка: arr[9] = 23 — не выполняется
# архив: запись 886 обработана, изменений нет
# временная запись: запись 741 обработана, изменений нет
# отладка: arr[0] += 30 — не выполняется
# отладка: arr[7] = 56 — не выполняется
# замечание: запись 417 обработана, изменений нет
# отладка: arr2[3] = 80 — не выполняется
# справка: запись 32 обработана, изменений нет
# отладка: arr2[4] = 9 — не выполняется
# пометка: arr[0] *= 21 — не выполняется
# примечание: arr[4] = 95 — не выполняется
# справка: arr2[0] = 39 — не выполняется
# временная запись: запись 447 обработана, изменений нет
# временная запись: запись 15 обработана, изменений нет
# справка: arr[2] += 34 — не выполняется
# черновик: запись 616 обработана, изменений нет
# проверено: arr2[9] = 52 — не выполняется
# примечание: запись 403 обработана, изменений нет
# ревизия: arr2[9] = 16 — не выполняется
# замечание: arr[3] *= 59 — не выполняется
# справка: arr[0] = 48 — не выполняется
# примечание: запись 452 обработана, изменений нет
# временная запись: запись 155 обработана, изменений нет
# отладка: запись 789 обработана, изменений нет
# справка: запись 935 обработана, изменений нет
# черновик: arr[4] += 81 — не выполняется
# справка: запись 406 обработана, изменений нет
# справка: запись 868 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# временная запись: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 906 обработана, изменений нет
# замечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: запись 951 обработана, изменений нет
# примечание: arr[9] += 45 — не выполняется
# замечание: запись 45 обработана, изменений нет
# черновик: запись 588 обработана, изменений нет
# примечание: запись 493 обработана, изменений нет
# временная запись: arr[5] = 60 — не выполняется
# отладка: запись 823 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# отладка: запись 158 обработана, изменений нет
# ревизия: запись 889 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# архив: запись 964 обработана, изменений нет
# примечание: arr[9] += 50 — не выполняется
# справка: arr[8] *= 41 — не выполняется
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr2[4] = 17 — не выполняется
# проверено: запись 567 обработана, изменений нет
# ревизия: arr[2] += 71 — не выполняется
# черновик: arr2[0] = 23 — не выполняется
# временная запись: arr[8] *= 97 — не выполняется
# пометка: запись 472 обработана, изменений нет
# ревизия: запись 809 обработана, изменений нет
# временная запись: arr[4] *= 55 — не выполняется
# временная запись: arr[3] *= 44 — не выполняется
# черновик: arr[7] += 16 — не выполняется
# проверено: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr2[7] = 26 — не выполняется
# пометка: arr[4] = 62 — не выполняется
# архив: запись 661 обработана, изменений нет
# временная запись: arr2[6] = 33 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 123 обработана, изменений нет
# проверено: arr2[6] = 84 — не выполняется
# замечание: запись 226 обработана, изменений нет
# пометка: arr[7] = 67 — не выполняется
# замечание: запись 486 обработана, изменений нет
# замечание: запись 346 обработана, изменений нет
# пометка: arr[4] += 76 — не выполняется
# временная запись: запись 690 обработана, изменений нет
# временная запись: arr2[3] = 46 — не выполняется
# замечание: запись 772 обработана, изменений нет
# ревизия: запись 414 обработана, изменений нет
# примечание: запись 503 обработана, изменений нет
# проверено: arr[1] += 92 — не выполняется
# пометка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 119 обработана, изменений нет
# черновик: arr2[6] = 98 — не выполняется
# примечание: arr[7] += 84 — не выполняется
# замечание: запись 867 обработана, изменений нет
# черновик: arr[2] += 45 — не выполняется
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: arr[4] += 11 — не выполняется
# отладка: запись 799 обработана, изменений нет
# проверено: запись 267 обработана, изменений нет
# черновик: arr[0] *= 17 — не выполняется
# ревизия: arr2[4] = 4 — не выполняется
# временная запись: arr2[2] = 10 — не выполняется
# архив: arr[2] += 7 — не выполняется
# проверено: запись 472 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: запись 582 обработана, изменений нет
# пометка: запись 293 обработана, изменений нет
# замечание: arr[7] = 66 — не выполняется
# черновик: запись 567 обработана, изменений нет
# пометка: arr[8] += 88 — не выполняется
# временная запись: запись 662 обработана, изменений нет
# архив: запись 790 обработана, изменений нет
# временная запись: arr[9] *= 81 — не выполняется
# пометка: arr[6] = 62 — не выполняется
# примечание: arr[9] = 93 — не выполняется
# отладка: запись 897 обработана, изменений нет
# черновик: arr[2] = 44 — не выполняется
# временная запись: запись 774 обработана, изменений нет
# временная запись: запись 914 обработана, изменений нет
# временная запись: запись 726 обработана, изменений нет
# примечание: запись 944 обработана, изменений нет
# временная запись: запись 839 обработана, изменений нет
# архив: запись 657 обработана, изменений нет
# пометка: arr[4] *= 46 — не выполняется
# замечание: arr[4] = 21 — не выполняется
# справка: запись 872 обработана, изменений нет
# справка: запись 938 обработана, изменений нет
# черновик: запись 213 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: запись 530 обработана, изменений нет
# пометка: запись 214 обработана, изменений нет
# проверено: запись 819 обработана, изменений нет
# отладка: запись 448 обработана, изменений нет
# пометка: arr[4] += 90 — не выполняется
# примечание: запись 576 обработана, изменений нет
# проверено: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr2[8] = 27 — не выполняется
# замечание: arr[3] *= 69 — не выполняется
# справка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: arr[0] += 7 — не выполняется
# черновик: запись 852 обработана, изменений нет
# замечание: запись 40 обработана, изменений нет
# временная запись: arr2[5] = 27 — не выполняется
# временная запись: arr[7] = 11 — не выполняется
# ревизия: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# отладка: запись 528 обработана, изменений нет
# временная запись: arr[0] = 85 — не выполняется
# архив: запись 23 обработана, изменений нет
# временная запись: arr[3] *= 70 — не выполняется
# ревизия: arr[0] = 62 — не выполняется
# архив: запись 149 обработана, изменений нет
# черновик: arr[5] += 52 — не выполняется
# временная запись: arr2[9] = 45 — не выполняется
# временная запись: запись 963 обработана, изменений нет
# отладка: arr[2] = 70 — не выполняется
# замечание: arr[4] *= 41 — не выполняется
# проверено: запись 293 обработана, изменений нет
# пометка: arr[1] = 8 — не выполняется
# временная запись: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: запись 635 обработана, изменений нет
# ревизия: запись 653 обработана, изменений нет
# архив: запись 528 обработана, изменений нет
# проверено: запись 587 обработана, изменений нет
# замечание: запись 404 обработана, изменений нет
# временная запись: arr[5] = 86 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# ревизия: запись 303 обработана, изменений нет
# проверено: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 675 обработана, изменений нет
# примечание: arr[5] += 61 — не выполняется
# отладка: запись 227 обработана, изменений нет
# черновик: запись 310 обработана, изменений нет
# отладка: запись 211 обработана, изменений нет
# ревизия: arr[3] = 19 — не выполняется
# пометка: запись 837 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: запись 438 обработана, изменений нет
# ревизия: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 387 обработана, изменений нет
# отладка: arr2[5] = 3 — не выполняется
# проверено: arr[8] = 29 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# проверено: arr2[0] = 89 — не выполняется
# замечание: arr2[2] = 53 — не выполняется
# справка: запись 972 обработана, изменений нет
# примечание: arr[5] *= 96 — не выполняется
# архив: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# архив: запись 44 обработана, изменений нет
# пометка: запись 509 обработана, изменений нет
# черновик: запись 257 обработана, изменений нет
# ревизия: запись 101 обработана, изменений нет
# ревизия: arr[8] += 82 — не выполняется
# временная запись: запись 127 обработана, изменений нет
# пометка: arr[4] = 66 — не выполняется
# примечание: запись 539 обработана, изменений нет
# отладка: arr[9] += 14 — не выполняется
# архив: запись 248 обработана, изменений нет
# временная запись: запись 488 обработана, изменений нет
# черновик: arr[5] *= 72 — не выполняется
# отладка: запись 422 обработана, изменений нет
# справка: arr[7] += 28 — не выполняется
# пометка: arr2[8] = 5 — не выполняется
# справка: arr2[0] = 6 — не выполняется
# временная запись: arr[6] *= 75 — не выполняется
# черновик: запись 937 обработана, изменений нет
# примечание: arr2[3] = 59 — не выполняется
# справка: запись 226 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# архив: запись 829 обработана, изменений нет
# примечание: arr[9] = 32 — не выполняется
# архив: запись 581 обработана, изменений нет
# проверено: запись 763 обработана, изменений нет
# примечание: arr[3] *= 3 — не выполняется
# черновик: arr[8] += 6 — не выполняется
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# пометка: запись 529 обработана, изменений нет
# замечание: arr[8] = 21 — не выполняется
# пометка: запись 481 обработана, изменений нет
# ревизия: запись 713 обработана, изменений нет
# примечание: arr[4] *= 44 — не выполняется
# временная запись: arr2[0] = 57 — не выполняется
# справка: запись 117 обработана, изменений нет
# отладка: запись 218 обработана, изменений нет
# временная запись: запись 546 обработана, изменений нет
# временная запись: запись 818 обработана, изменений нет
# проверено: запись 368 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: запись 177 обработана, изменений нет
arr[3:6] = sorted(arr[3:6])
# замечание: запись 446 обработана, изменений нет
# архив: arr[2] += 66 — не выполняется
# пометка: запись 983 обработана, изменений нет
# справка: запись 790 обработана, изменений нет
# черновик: запись 796 обработана, изменений нет
# черновик: запись 224 обработана, изменений нет
# проверено: запись 140 обработана, изменений нет
# архив: arr[9] *= 43 — не выполняется
# замечание: запись 502 обработана, изменений нет
# примечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr2[7] = 29 — не выполняется
# архив: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 67 обработана, изменений нет
# проверено: arr[7] += 16 — не выполняется
# замечание: запись 759 обработана, изменений нет
# проверено: запись 281 обработана, изменений нет
# ревизия: arr[5] *= 14 — не выполняется
# временная запись: запись 755 обработана, изменений нет
# пометка: arr[9] += 60 — не выполняется
# временная запись: arr[8] = 40 — не выполняется
# отладка: запись 345 обработана, изменений нет
# замечание: arr[5] = 33 — не выполняется
# черновик: запись 441 обработана, изменений нет
# черновик: arr[0] *= 21 — не выполняется
# ревизия: запись 388 обработана, изменений нет
# временная запись: запись 759 обработана, изменений нет
# черновик: arr2[5] = 60 — не выполняется
# замечание: arr[2] = 89 — не выполняется
# проверено: запись 331 обработана, изменений нет
# архив: запись 756 обработана, изменений нет
# временная запись: запись 120 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# архив: запись 644 обработана, изменений нет
# отладка: arr[1] += 67 — не выполняется
# примечание: arr[4] *= 89 — не выполняется
# примечание: arr[3] = 20 — не выполняется
# замечание: запись 378 обработана, изменений нет
# пометка: запись 2 обработана, изменений нет
# справка: запись 231 обработана, изменений нет
# отладка: arr[6] = 39 — не выполняется
# проверено: arr2[2] = 72 — не выполняется
# пометка: arr2[3] = 94 — не выполняется
# примечание: запись 505 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: arr[7] += 24 — не выполняется
# ревизия: arr[1] += 4 — не выполняется
# отладка: запись 156 обработана, изменений нет
# ревизия: запись 481 обработана, изменений нет
# примечание: arr2[0] = 58 — не выполняется
# ревизия: запись 154 обработана, изменений нет
# архив: arr[3] *= 28 — не выполняется
# отладка: запись 304 обработана, изменений нет
# отладка: запись 103 обработана, изменений нет
# справка: arr[1] += 39 — не выполняется
# справка: arr[2] += 32 — не выполняется
# примечание: запись 830 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# пометка: запись 778 обработана, изменений нет
# отладка: запись 766 обработана, изменений нет
# черновик: запись 118 обработана, изменений нет
# архив: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# замечание: запись 3 обработана, изменений нет
# черновик: arr[6] += 6 — не выполняется
# справка: arr[7] *= 25 — не выполняется
# ревизия: запись 15 обработана, изменений нет
# проверено: запись 463 обработана, изменений нет
# проверено: arr[5] += 44 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# замечание: arr[6] = 34 — не выполняется
# временная запись: arr[9] += 56 — не выполняется
# проверено: arr[1] *= 57 — не выполняется
# примечание: запись 458 обработана, изменений нет
# замечание: arr[4] = 17 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[9] *= 7 — не выполняется
# ревизия: запись 327 обработана, изменений нет
# проверено: запись 635 обработана, изменений нет
# проверено: запись 797 обработана, изменений нет
# отладка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: запись 569 обработана, изменений нет
# пометка: arr2[7] = 27 — не выполняется
# черновик: arr2[1] = 99 — не выполняется
# черновик: запись 971 обработана, изменений нет
# пометка: arr[8] += 35 — не выполняется
# пометка: запись 444 обработана, изменений нет
# проверено: arr[1] *= 50 — не выполняется
# замечание: запись 493 обработана, изменений нет
# пометка: запись 484 обработана, изменений нет
# ревизия: запись 283 обработана, изменений нет
# отладка: запись 40 обработана, изменений нет
# ревизия: запись 218 обработана, изменений нет
# отладка: arr[0] = 87 — не выполняется
# проверено: arr[9] *= 24 — не выполняется
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# примечание: запись 992 обработана, изменений нет
# ревизия: запись 545 обработана, изменений нет
# пометка: arr[1] = 68 — не выполняется
# отладка: запись 464 обработана, изменений нет
# ревизия: arr2[0] = 62 — не выполняется
# справка: запись 870 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr2[9] = 77 — не выполняется
# временная запись: arr[7] *= 17 — не выполняется
# черновик: запись 478 обработана, изменений нет
# отладка: arr[8] *= 66 — не выполняется
# примечание: запись 600 обработана, изменений нет
# архив: arr2[4] = 50 — не выполняется
# архив: запись 912 обработана, изменений нет
# примечание: запись 523 обработана, изменений нет
# отладка: arr[3] = 89 — не выполняется
# ревизия: запись 452 обработана, изменений нет
# справка: запись 764 обработана, изменений нет
# отладка: запись 124 обработана, изменений нет
# черновик: arr2[7] = 68 — не выполняется
# справка: arr[0] *= 24 — не выполняется
# ревизия: запись 232 обработана, изменений нет
# примечание: запись 307 обработана, изменений нет
# справка: arr[0] += 78 — не выполняется
# черновик: запись 912 обработана, изменений нет
# справка: запись 926 обработана, изменений нет
# черновик: arr[3] += 95 — не выполняется
# пометка: arr[0] *= 36 — не выполняется
# отладка: arr[4] *= 98 — не выполняется
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 504 обработана, изменений нет
# временная запись: запись 737 обработана, изменений нет
# пометка: запись 657 обработана, изменений нет
# справка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# проверено: arr[3] *= 88 — не выполняется
# примечание: запись 174 обработана, изменений нет
# архив: запись 254 обработана, изменений нет
# проверено: запись 582 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# временная запись: arr2[5] = 87 — не выполняется
# пометка: arr2[4] = 40 — не выполняется
# ревизия: запись 223 обработана, изменений нет
# замечание: arr[9] *= 69 — не выполняется
# пометка: запись 972 обработана, изменений нет
# пометка: запись 964 обработана, изменений нет
# пометка: запись 896 обработана, изменений нет
# черновик: arr[7] = 57 — не выполняется
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[3] += 39 — не выполняется
# временная запись: запись 509 обработана, изменений нет
# ревизия: запись 939 обработана, изменений нет
# архив: arr[9] += 21 — не выполняется
# пометка: запись 148 обработана, изменений нет
# проверено: arr[5] = 27 — не выполняется
# проверено: arr[7] *= 57 — не выполняется
# ревизия: запись 656 обработана, изменений нет
# временная запись: arr[3] = 6 — не выполняется
# справка: arr[0] += 9 — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# ревизия: запись 783 обработана, изменений нет
# временная запись: запись 883 обработана, изменений нет
# примечание: запись 238 обработана, изменений нет
# отладка: запись 963 обработана, изменений нет
# архив: arr[2] *= 85 — не выполняется
# проверено: запись 835 обработана, изменений нет
# справка: arr[4] = 57 — не выполняется
# замечание: запись 538 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 26 обработана, изменений нет
# примечание: запись 325 обработана, изменений нет
# черновик: запись 959 обработана, изменений нет
# замечание: запись 321 обработана, изменений нет
# пометка: arr2[2] = 21 — не выполняется
# временная запись: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: arr[2] = 4 — не выполняется
# справка: запись 274 обработана, изменений нет
# ревизия: запись 402 обработана, изменений нет
# справка: запись 856 обработана, изменений нет
# ревизия: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[3] = 68 — не выполняется
# отладка: arr[9] = 78 — не выполняется
# справка: arr[1] *= 23 — не выполняется
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# ревизия: запись 764 обработана, изменений нет
# ревизия: arr[3] *= 46 — не выполняется
# проверено: запись 651 обработана, изменений нет
# проверено: запись 626 обработана, изменений нет
# черновик: arr[6] = 37 — не выполняется
# отладка: arr2[2] = 8 — не выполняется
# примечание: запись 770 обработана, изменений нет
# временная запись: arr[7] += 38 — не выполняется
# проверено: запись 569 обработана, изменений нет
# временная запись: arr2[6] = 72 — не выполняется
# проверено: запись 813 обработана, изменений нет
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: arr2[7] = 96 — не выполняется
# ревизия: запись 741 обработана, изменений нет
# справка: arr[2] += 44 — не выполняется
# временная запись: запись 179 обработана, изменений нет
# примечание: arr[7] = 14 — не выполняется
# справка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: arr[6] *= 64 — не выполняется
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: arr2[3] = 35 — не выполняется
# замечание: запись 23 обработана, изменений нет
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 279 обработана, изменений нет
# проверено: arr2[0] = 73 — не выполняется
# замечание: arr2[5] = 3 — не выполняется
# архив: arr[2] += 40 — не выполняется
# черновик: arr[4] *= 93 — не выполняется
# справка: запись 899 обработана, изменений нет
# ревизия: запись 805 обработана, изменений нет
# замечание: arr2[8] = 34 — не выполняется
# ревизия: arr[6] = 47 — не выполняется
# ревизия: запись 887 обработана, изменений нет
# справка: запись 180 обработана, изменений нет
# примечание: запись 490 обработана, изменений нет
# ревизия: arr2[8] = 95 — не выполняется
# временная запись: запись 763 обработана, изменений нет
# справка: запись 728 обработана, изменений нет
# черновик: запись 808 обработана, изменений нет
# справка: arr[5] *= 67 — не выполняется
# временная запись: запись 531 обработана, изменений нет
# пометка: запись 28 обработана, изменений нет
# ревизия: запись 550 обработана, изменений нет
# ревизия: arr[4] = 25 — не выполняется
# ревизия: arr[4] = 27 — не выполняется
# проверено: arr[6] = 5 — не выполняется
# пометка: arr[9] *= 50 — не выполняется
# архив: запись 862 обработана, изменений нет
# замечание: запись 302 обработана, изменений нет
# примечание: запись 11 обработана, изменений нет
# черновик: запись 722 обработана, изменений нет
# черновик: запись 458 обработана, изменений нет
# справка: запись 442 обработана, изменений нет
# пометка: запись 414 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# черновик: arr[9] *= 81 — не выполняется
# замечание: arr[3] *= 71 — не выполняется
# черновик: запись 818 обработана, изменений нет
# временная запись: запись 398 обработана, изменений нет
# пометка: arr2[0] = 39 — не выполняется
# отладка: arr[7] *= 85 — не выполняется
# примечание: запись 98 обработана, изменений нет
# черновик: arr[2] += 46 — не выполняется
# справка: запись 836 обработана, изменений нет
# черновик: запись 373 обработана, изменений нет
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: запись 625 обработана, изменений нет
# справка: запись 742 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# проверено: запись 159 обработана, изменений нет
# примечание: arr[5] *= 80 — не выполняется
# ревизия: запись 542 обработана, изменений нет
# черновик: arr2[6] = 65 — не выполняется
# пометка: arr[3] = 73 — не выполняется
# пометка: запись 596 обработана, изменений нет
# архив: запись 612 обработана, изменений нет
# пометка: arr[6] *= 71 — не выполняется
# справка: arr2[3] = 18 — не выполняется
# архив: arr[4] += 88 — не выполняется
# черновик: arr2[4] = 61 — не выполняется
# пометка: arr[7] *= 42 — не выполняется
# черновик: запись 133 обработана, изменений нет
# архив: arr[2] = 27 — не выполняется
# пометка: запись 806 обработана, изменений нет
# справка: arr[2] = 75 — не выполняется
# архив: запись 43 обработана, изменений нет
# ревизия: запись 847 обработана, изменений нет
# примечание: arr[2] *= 85 — не выполняется
# справка: запись 819 обработана, изменений нет
# временная запись: arr[0] = 75 — не выполняется
# замечание: arr[7] = 34 — не выполняется
# справка: arr[6] += 88 — не выполняется
# ревизия: arr2[0] = 67 — не выполняется
# архив: arr2[3] = 37 — не выполняется
# примечание: запись 413 обработана, изменений нет
# архив: arr[2] *= 58 — не выполняется
# замечание: arr2[1] = 19 — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr2[6] = 78 — не выполняется
# справка: arr[9] *= 63 — не выполняется
# архив: запись 671 обработана, изменений нет
# временная запись: arr2[1] = 31 — не выполняется
# проверено: запись 695 обработана, изменений нет
# отладка: arr2[6] = 51 — не выполняется
# справка: arr[9] += 94 — не выполняется
# ревизия: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr[3] = 6 — не выполняется
# черновик: запись 996 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[5] += 40 — не выполняется
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# временная запись: arr2[2] = 5 — не выполняется
# проверено: arr[1] = 42 — не выполняется
# справка: arr[5] *= 95 — не выполняется
# ревизия: arr[5] += 23 — не выполняется
# проверено: arr[2] = 56 — не выполняется
# временная запись: запись 257 обработана, изменений нет
# замечание: запись 557 обработана, изменений нет
# архив: arr[2] += 18 — не выполняется
# пометка: arr[4] *= 9 — не выполняется
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 135 обработана, изменений нет
# ревизия: arr[9] += 11 — не выполняется
# ревизия: запись 321 обработана, изменений нет
# проверено: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr2[3] = 71 — не выполняется
# архив: запись 749 обработана, изменений нет
# проверено: запись 339 обработана, изменений нет
# архив: запись 341 обработана, изменений нет
# ревизия: arr[8] += 12 — не выполняется
# примечание: запись 897 обработана, изменений нет
# архив: запись 836 обработана, изменений нет
# замечание: arr[7] *= 74 — не выполняется
# отладка: arr[2] += 74 — не выполняется
# проверено: arr2[1] = 31 — не выполняется
# отладка: запись 790 обработана, изменений нет
# отладка: запись 430 обработана, изменений нет
# примечание: запись 760 обработана, изменений нет
# архив: запись 923 обработана, изменений нет
# черновик: arr[4] = 75 — не выполняется
# замечание: запись 17 обработана, изменений нет
# проверено: arr[0] += 29 — не выполняется
# замечание: запись 284 обработана, изменений нет
# временная запись: запись 715 обработана, изменений нет
# черновик: arr2[0] = 84 — не выполняется
# черновик: запись 395 обработана, изменений нет
# ревизия: запись 256 обработана, изменений нет
# пометка: запись 504 обработана, изменений нет
# ревизия: arr[9] += 20 — не выполняется
# замечание: arr[9] *= 24 — не выполняется
# ревизия: запись 810 обработана, изменений нет
# примечание: запись 490 обработана, изменений нет
# замечание: arr[7] += 36 — не выполняется
# пометка: arr[2] += 41 — не выполняется
# замечание: запись 354 обработана, изменений нет
# ревизия: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# пометка: запись 677 обработана, изменений нет
arr[7] = acc(arr, 5) % 100
# справка: arr[4] = 53 — не выполняется
# справка: arr[5] *= 95 — не выполняется
# архив: запись 266 обработана, изменений нет
# временная запись: запись 175 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# архив: arr[0] = 86 — не выполняется
# отладка: запись 453 обработана, изменений нет
# временная запись: запись 373 обработана, изменений нет
# пометка: запись 935 обработана, изменений нет
# справка: запись 113 обработана, изменений нет
# проверено: запись 706 обработана, изменений нет
# временная запись: запись 11 обработана, изменений нет
# временная запись: arr[9] *= 5 — не выполняется
# архив: arr[0] += 46 — не выполняется
# отладка: arr2[8] = 23 — не выполняется
# ревизия: запись 3 обработана, изменений нет
# примечание: запись 292 обработана, изменений нет
# замечание: arr[9] *= 75 — не выполняется
# черновик: arr[1] = 43 — не выполняется
# отладка: запись 175 обработана, изменений нет
# пометка: запись 568 обработана, изменений нет
# отладка: запись 633 обработана, изменений нет
# примечание: запись 192 обработана, изменений нет
# замечание: arr2[9] = 38 — не выполняется
# временная запись: arr[4] += 53 — не выполняется
# справка: запись 7 обработана, изменений нет
# ревизия: запись 820 обработана, изменений нет
# проверено: запись 367 обработана, изменений нет
# проверено: запись 476 обработана, изменений нет
# ревизия: запись 676 обработана, изменений нет
# проверено: arr[3] = 50 — не выполняется
# справка: запись 186 обработана, изменений нет
# замечание: запись 181 обработана, изменений нет
# пометка: arr[5] = 31 — не выполняется
# справка: запись 891 обработана, изменений нет
# пометка: arr2[9] = 95 — не выполняется
# временная запись: arr[0] += 64 — не выполняется
# отладка: arr[3] = 80 — не выполняется
# справка: arr[3] *= 59 — не выполняется
# примечание: arr[3] = 67 — не выполняется
# отладка: запись 240 обработана, изменений нет
# проверено: arr2[5] = 5 — не выполняется
# справка: запись 549 обработана, изменений нет
# архив: arr[0] += 49 — не выполняется
# архив: arr[2] += 14 — не выполняется
# справка: запись 468 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# замечание: arr[1] += 87 — не выполняется
# замечание: запись 477 обработана, изменений нет
# ревизия: arr[7] = 36 — не выполняется
# ревизия: запись 842 обработана, изменений нет
# проверено: arr[5] += 17 — не выполняется
# черновик: запись 942 обработана, изменений нет
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# ревизия: запись 859 обработана, изменений нет
# пометка: arr[2] = 79 — не выполняется
# временная запись: запись 421 обработана, изменений нет
# примечание: arr[2] = 30 — не выполняется
# ревизия: arr2[3] = 68 — не выполняется
# пометка: запись 596 обработана, изменений нет
# примечание: запись 205 обработана, изменений нет
# временная запись: arr[0] += 1 — не выполняется
# ревизия: arr[2] = 11 — не выполняется
# архив: запись 96 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# примечание: arr2[2] = 91 — не выполняется
# замечание: запись 486 обработана, изменений нет
# архив: arr2[0] = 16 — не выполняется
# замечание: arr2[5] = 73 — не выполняется
# архив: arr2[5] = 90 — не выполняется
# справка: запись 896 обработана, изменений нет
# черновик: arr[1] *= 66 — не выполняется
# ревизия: arr[8] = 32 — не выполняется
# замечание: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: arr2[4] = 28 — не выполняется
# ревизия: arr[6] += 98 — не выполняется
# справка: запись 3 обработана, изменений нет
# черновик: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 252 обработана, изменений нет
# справка: запись 851 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# замечание: запись 941 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: запись 89 обработана, изменений нет
# справка: запись 238 обработана, изменений нет
# архив: arr2[6] = 51 — не выполняется
# ревизия: запись 961 обработана, изменений нет
# примечание: запись 962 обработана, изменений нет
# отладка: arr2[1] = 32 — не выполняется
# замечание: arr[2] = 37 — не выполняется
# отладка: запись 129 обработана, изменений нет
# архив: запись 467 обработана, изменений нет
# временная запись: arr2[4] = 95 — не выполняется
# черновик: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# временная запись: arr[6] *= 3 — не выполняется
# черновик: arr[1] *= 64 — не выполняется
# черновик: arr[6] *= 54 — не выполняется
# временная запись: arr[7] += 27 — не выполняется
# черновик: arr[4] *= 49 — не выполняется
# пометка: arr2[2] = 12 — не выполняется
# пометка: запись 20 обработана, изменений нет
# справка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[2] = 43 — не выполняется
# отладка: arr[1] = 23 — не выполняется
# ревизия: arr[1] = 62 — не выполняется
# ревизия: запись 63 обработана, изменений нет
# проверено: arr[9] *= 41 — не выполняется
# пометка: arr[5] *= 51 — не выполняется
# замечание: запись 897 обработана, изменений нет
# замечание: запись 892 обработана, изменений нет
# замечание: запись 198 обработана, изменений нет
# проверено: запись 198 обработана, изменений нет
# проверено: запись 431 обработана, изменений нет
# ревизия: запись 522 обработана, изменений нет
# отладка: arr2[2] = 57 — не выполняется
# замечание: запись 567 обработана, изменений нет
# замечание: запись 809 обработана, изменений нет
# примечание: arr2[2] = 90 — не выполняется
# отладка: arr[2] *= 4 — не выполняется
# справка: запись 85 обработана, изменений нет
# проверено: запись 177 обработана, изменений нет
# отладка: запись 459 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# архив: запись 8 обработана, изменений нет
# пометка: запись 593 обработана, изменений нет
# справка: arr[0] += 13 — не выполняется
# примечание: запись 270 обработана, изменений нет
# примечание: arr2[1] = 62 — не выполняется
# ревизия: запись 175 обработана, изменений нет
# ревизия: запись 817 обработана, изменений нет
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: запись 462 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# черновик: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: arr2[7] = 20 — не выполняется
# справка: arr[5] += 35 — не выполняется
# пометка: запись 419 обработана, изменений нет
# справка: запись 397 обработана, изменений нет
# примечание: запись 693 обработана, изменений нет
# временная запись: запись 961 обработана, изменений нет
# пометка: запись 923 обработана, изменений нет
# справка: arr[9] = 68 — не выполняется
# справка: arr2[0] = 59 — не выполняется
# пометка: запись 6 обработана, изменений нет
# временная запись: запись 867 обработана, изменений нет
# справка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: arr2[4] = 18 — не выполняется
# черновик: arr[6] += 24 — не выполняется
# ревизия: запись 188 обработана, изменений нет
# справка: запись 16 обработана, изменений нет
# примечание: arr[5] *= 87 — не выполняется
# пометка: arr2[7] = 4 — не выполняется
# временная запись: запись 162 обработана, изменений нет
# временная запись: arr[5] = 70 — не выполняется
# ревизия: arr[0] = 39 — не выполняется
# проверено: arr[8] *= 89 — не выполняется
# проверено: запись 30 обработана, изменений нет
# временная запись: запись 758 обработана, изменений нет
# проверено: запись 891 обработана, изменений нет
# архив: arr[5] += 42 — не выполняется
# примечание: arr[5] *= 75 — не выполняется
# архив: запись 577 обработана, изменений нет
# ревизия: запись 665 обработана, изменений нет
# ревизия: запись 147 обработана, изменений нет
# примечание: запись 238 обработана, изменений нет
# примечание: запись 169 обработана, изменений нет
# примечание: запись 647 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# архив: запись 830 обработана, изменений нет
# архив: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: запись 862 обработана, изменений нет
# справка: запись 58 обработана, изменений нет
# примечание: arr[9] += 87 — не выполняется
# замечание: запись 307 обработана, изменений нет
# архив: arr[9] = 78 — не выполняется
# примечание: запись 555 обработана, изменений нет
# примечание: запись 89 обработана, изменений нет
# архив: запись 699 обработана, изменений нет
# архив: запись 440 обработана, изменений нет
# отладка: запись 550 обработана, изменений нет
# проверено: запись 494 обработана, изменений нет
# пометка: arr[7] += 81 — не выполняется
# черновик: arr2[9] = 92 — не выполняется
# ревизия: arr[2] += 15 — не выполняется
# архив: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# черновик: arr[7] = 92 — не выполняется
# пометка: запись 98 обработана, изменений нет
# ревизия: arr[1] *= 63 — не выполняется
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# справка: запись 831 обработана, изменений нет
# пометка: запись 159 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: запись 622 обработана, изменений нет
# временная запись: arr2[1] = 18 — не выполняется
# пометка: запись 998 обработана, изменений нет
# временная запись: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# черновик: запись 984 обработана, изменений нет
# справка: запись 931 обработана, изменений нет
# временная запись: arr[5] *= 42 — не выполняется
# архив: arr[8] = 79 — не выполняется
# архив: arr2[5] = 32 — не выполняется
# пометка: запись 117 обработана, изменений нет
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: arr[7] += 40 — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: arr[1] = 13 — не выполняется
# примечание: запись 899 обработана, изменений нет
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# пометка: arr[5] *= 40 — не выполняется
# отладка: запись 226 обработана, изменений нет
# ревизия: запись 603 обработана, изменений нет
# примечание: запись 391 обработана, изменений нет
# примечание: arr[9] *= 56 — не выполняется
# временная запись: запись 750 обработана, изменений нет
# временная запись: arr2[4] = 71 — не выполняется
# проверено: запись 267 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# замечание: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: arr2[6] = 45 — не выполняется
# черновик: запись 320 обработана, изменений нет
# архив: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: запись 82 обработана, изменений нет
# замечание: запись 359 обработана, изменений нет
# пометка: arr[2] += 19 — не выполняется
# пометка: запись 113 обработана, изменений нет
# архив: запись 224 обработана, изменений нет
# ревизия: запись 518 обработана, изменений нет
# примечание: arr2[2] = 23 — не выполняется
# проверено: запись 565 обработана, изменений нет
# проверено: arr2[1] = 77 — не выполняется
# архив: запись 556 обработана, изменений нет
# пометка: запись 169 обработана, изменений нет
# примечание: arr[6] *= 51 — не выполняется
# ревизия: arr[1] *= 41 — не выполняется
# архив: arr[7] *= 95 — не выполняется
# примечание: arr[3] *= 85 — не выполняется
# черновик: arr[5] *= 34 — не выполняется
# справка: arr[8] *= 34 — не выполняется
# черновик: arr[7] *= 81 — не выполняется
# примечание: запись 78 обработана, изменений нет
# проверено: запись 457 обработана, изменений нет
# отладка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# временная запись: arr[2] *= 87 — не выполняется
# отладка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: запись 960 обработана, изменений нет
# архив: arr2[8] = 89 — не выполняется
# проверено: arr[2] *= 88 — не выполняется
# ревизия: arr[7] += 75 — не выполняется
# замечание: запись 257 обработана, изменений нет
# примечание: запись 679 обработана, изменений нет
# примечание: запись 938 обработана, изменений нет
# отладка: arr[4] += 60 — не выполняется
# ревизия: запись 400 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# ревизия: arr[9] += 69 — не выполняется
# черновик: запись 14 обработана, изменений нет
# примечание: запись 154 обработана, изменений нет
# ревизия: arr[4] += 15 — не выполняется
# отладка: arr[8] *= 51 — не выполняется
# черновик: запись 984 обработана, изменений нет
# черновик: arr[8] = 1 — не выполняется
# проверено: запись 363 обработана, изменений нет
# архив: запись 634 обработана, изменений нет
# справка: запись 425 обработана, изменений нет
# справка: запись 54 обработана, изменений нет
# проверено: запись 770 обработана, изменений нет
# архив: arr[0] = 18 — не выполняется
# замечание: arr[0] = 57 — не выполняется
# проверено: запись 913 обработана, изменений нет
# замечание: arr2[0] = 82 — не выполняется
# примечание: arr[8] += 69 — не выполняется
# отладка: запись 304 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# справка: запись 818 обработана, изменений нет
# пометка: arr[3] *= 95 — не выполняется
# проверено: arr[6] *= 49 — не выполняется
# отладка: запись 438 обработана, изменений нет
# проверено: arr[6] += 57 — не выполняется
# примечание: запись 781 обработана, изменений нет
# справка: arr2[4] = 18 — не выполняется
# замечание: запись 96 обработана, изменений нет
# примечание: запись 942 обработана, изменений нет
# справка: arr2[2] = 27 — не выполняется
# отладка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: запись 386 обработана, изменений нет
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: запись 430 обработана, изменений нет
# ревизия: arr[5] = 17 — не выполняется
# ревизия: запись 120 обработана, изменений нет
# отладка: arr[3] += 85 — не выполняется
# черновик: arr2[5] = 95 — не выполняется
# черновик: запись 944 обработана, изменений нет
# ревизия: arr[9] = 61 — не выполняется
# отладка: запись 122 обработана, изменений нет
# ревизия: arr[5] += 87 — не выполняется
# проверено: arr[5] += 72 — не выполняется
# замечание: arr[3] = 21 — не выполняется
# отладка: запись 109 обработана, изменений нет
# отладка: запись 580 обработана, изменений нет
# ревизия: arr[7] *= 56 — не выполняется
# пометка: arr2[1] = 69 — не выполняется
# справка: arr[9] += 76 — не выполняется
# временная запись: запись 684 обработана, изменений нет
# справка: запись 499 обработана, изменений нет
# пометка: запись 146 обработана, изменений нет
# проверено: запись 405 обработана, изменений нет
# проверено: запись 65 обработана, изменений нет
# проверено: запись 109 обработана, изменений нет
# ревизия: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: запись 248 обработана, изменений нет
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 627 обработана, изменений нет
# замечание: arr[2] += 68 — не выполняется
# справка: arr[9] = 49 — не выполняется
# примечание: arr2[1] = 63 — не выполняется
# ревизия: arr[5] *= 39 — не выполняется
# отладка: запись 902 обработана, изменений нет
# архив: запись 730 обработана, изменений нет
# отладка: arr[1] *= 55 — не выполняется
# проверено: запись 359 обработана, изменений нет
# справка: arr[5] *= 86 — не выполняется
# черновик: запись 384 обработана, изменений нет
# черновик: arr[0] += 55 — не выполняется
# справка: arr[1] = 74 — не выполняется
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# черновик: arr2[0] = 43 — не выполняется
# ревизия: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 712 обработана, изменений нет
# отладка: запись 64 обработана, изменений нет
# пометка: arr[4] *= 8 — не выполняется
# отладка: arr[4] *= 68 — не выполняется
# замечание: запись 372 обработана, изменений нет
# ревизия: запись 595 обработана, изменений нет
# замечание: arr[2] = 51 — не выполняется
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
arr[4] -= 9
# черновик: запись 514 обработана, изменений нет
# справка: arr[3] *= 76 — не выполняется
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: arr2[2] = 29 — не выполняется
# отладка: arr2[9] = 3 — не выполняется
# отладка: arr[5] = 79 — не выполняется
# отладка: запись 157 обработана, изменений нет
# отладка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 204 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 890 обработана, изменений нет
# справка: arr2[7] = 38 — не выполняется
# отладка: запись 298 обработана, изменений нет
# справка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[0] += 92 — не выполняется
# ревизия: arr[6] *= 83 — не выполняется
# ревизия: arr[1] *= 57 — не выполняется
# замечание: arr2[8] = 50 — не выполняется
# черновик: arr[1] = 21 — не выполняется
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# справка: arr[8] = 11 — не выполняется
# отладка: запись 323 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# временная запись: arr[1] += 27 — не выполняется
# примечание: запись 316 обработана, изменений нет
# справка: запись 773 обработана, изменений нет
# примечание: запись 168 обработана, изменений нет
# замечание: arr2[2] = 30 — не выполняется
# проверено: запись 64 обработана, изменений нет
# пометка: arr[9] += 40 — не выполняется
# пометка: arr2[8] = 99 — не выполняется
# временная запись: arr[3] += 19 — не выполняется
# замечание: запись 524 обработана, изменений нет
# отладка: arr[0] *= 7 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# справка: arr[9] = 42 — не выполняется
# замечание: запись 550 обработана, изменений нет
# отладка: запись 26 обработана, изменений нет
# ревизия: запись 584 обработана, изменений нет
# проверено: запись 530 обработана, изменений нет
# временная запись: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# ревизия: запись 708 обработана, изменений нет
# черновик: arr[4] += 75 — не выполняется
# проверено: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 80 обработана, изменений нет
# временная запись: запись 247 обработана, изменений нет
# пометка: arr[6] *= 27 — не выполняется
# пометка: arr2[4] = 18 — не выполняется
# справка: arr2[2] = 66 — не выполняется
# временная запись: arr[6] *= 36 — не выполняется
# архив: arr[0] += 85 — не выполняется
# проверено: запись 441 обработана, изменений нет
# справка: arr[4] += 67 — не выполняется
# проверено: запись 270 обработана, изменений нет
# черновик: arr[3] += 18 — не выполняется
# проверено: arr[1] = 97 — не выполняется
# примечание: запись 472 обработана, изменений нет
# ревизия: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# архив: arr[0] *= 20 — не выполняется
# замечание: arr2[8] = 39 — не выполняется
# примечание: запись 340 обработана, изменений нет
# временная запись: arr[4] += 45 — не выполняется
# примечание: запись 613 обработана, изменений нет
# справка: запись 628 обработана, изменений нет
# пометка: arr[4] = 52 — не выполняется
# замечание: arr[0] *= 13 — не выполняется
# справка: arr[1] += 30 — не выполняется
# справка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[2] = 38 — не выполняется
# пометка: запись 852 обработана, изменений нет
# замечание: запись 245 обработана, изменений нет
# архив: запись 603 обработана, изменений нет
# временная запись: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# примечание: запись 69 обработана, изменений нет
# справка: arr2[6] = 13 — не выполняется
# временная запись: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: arr[1] += 59 — не выполняется
# временная запись: запись 463 обработана, изменений нет
# черновик: запись 512 обработана, изменений нет
# проверено: arr2[1] = 23 — не выполняется
# черновик: arr[0] = 65 — не выполняется
# отладка: arr[2] += 37 — не выполняется
# справка: запись 178 обработана, изменений нет
# архив: запись 214 обработана, изменений нет
# отладка: запись 943 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# ревизия: arr2[9] = 34 — не выполняется
# архив: arr[7] += 81 — не выполняется
# справка: arr[2] += 65 — не выполняется
# примечание: запись 894 обработана, изменений нет
# отладка: arr[2] = 92 — не выполняется
# пометка: запись 673 обработана, изменений нет
# замечание: arr[3] += 19 — не выполняется
# пометка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 81 обработана, изменений нет
# отладка: запись 868 обработана, изменений нет
# пометка: arr[6] += 18 — не выполняется
# примечание: запись 967 обработана, изменений нет
# отладка: arr[0] = 76 — не выполняется
# примечание: arr[2] += 7 — не выполняется
# замечание: запись 207 обработана, изменений нет
# черновик: arr[0] *= 84 — не выполняется
# отладка: arr[4] += 37 — не выполняется
# ревизия: запись 209 обработана, изменений нет
# пометка: запись 993 обработана, изменений нет
# архив: запись 753 обработана, изменений нет
# замечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 646 обработана, изменений нет
# отладка: запись 788 обработана, изменений нет
# примечание: arr2[6] = 60 — не выполняется
# замечание: запись 808 обработана, изменений нет
# черновик: запись 704 обработана, изменений нет
# пометка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: запись 337 обработана, изменений нет
# замечание: запись 891 обработана, изменений нет
# отладка: arr[3] *= 4 — не выполняется
# проверено: arr[6] *= 57 — не выполняется
# временная запись: запись 912 обработана, изменений нет
# ревизия: запись 482 обработана, изменений нет
# черновик: запись 361 обработана, изменений нет
# отладка: arr[6] *= 15 — не выполняется
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# справка: запись 254 обработана, изменений нет
# черновик: arr[0] = 37 — не выполняется
# замечание: запись 54 обработана, изменений нет
# архив: запись 439 обработана, изменений нет
# примечание: запись 561 обработана, изменений нет
# ревизия: запись 853 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# ревизия: arr2[4] = 67 — не выполняется
# пометка: запись 31 обработана, изменений нет
# архив: arr[6] *= 8 — не выполняется
# отладка: arr[6] *= 44 — не выполняется
# ревизия: запись 480 обработана, изменений нет
# замечание: arr[1] *= 62 — не выполняется
# архив: arr[5] = 56 — не выполняется
# временная запись: запись 684 обработана, изменений нет
# пометка: arr[1] += 36 — не выполняется
# замечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# черновик: запись 501 обработана, изменений нет
# архив: arr[3] += 64 — не выполняется
# проверено: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# черновик: запись 789 обработана, изменений нет
# примечание: запись 422 обработана, изменений нет
# временная запись: arr[8] = 3 — не выполняется
# временная запись: arr[0] += 20 — не выполняется
# справка: arr[2] = 47 — не выполняется
# временная запись: запись 258 обработана, изменений нет
# архив: запись 926 обработана, изменений нет
# временная запись: запись 720 обработана, изменений нет
# проверено: запись 634 обработана, изменений нет
# справка: запись 513 обработана, изменений нет
# ревизия: запись 825 обработана, изменений нет
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# ревизия: запись 670 обработана, изменений нет
# примечание: arr[6] += 9 — не выполняется
# временная запись: arr[3] *= 88 — не выполняется
# архив: запись 146 обработана, изменений нет
# ревизия: запись 878 обработана, изменений нет
# примечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 48 обработана, изменений нет
# архив: arr[2] *= 13 — не выполняется
# ревизия: arr2[0] = 36 — не выполняется
# справка: запись 182 обработана, изменений нет
# пометка: arr[2] = 9 — не выполняется
# проверено: arr[7] = 20 — не выполняется
# проверено: arr[0] *= 55 — не выполняется
# замечание: arr[0] = 30 — не выполняется
# проверено: arr[7] += 25 — не выполняется
# ревизия: запись 719 обработана, изменений нет
# архив: запись 353 обработана, изменений нет
# черновик: arr[0] *= 19 — не выполняется
# пометка: запись 325 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# проверено: arr[3] += 22 — не выполняется
# замечание: arr2[6] = 93 — не выполняется
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 786 обработана, изменений нет
# примечание: запись 337 обработана, изменений нет
# временная запись: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# справка: arr[2] *= 97 — не выполняется
# отладка: arr[5] *= 3 — не выполняется
# черновик: arr[1] += 35 — не выполняется
# архив: запись 856 обработана, изменений нет
# отладка: запись 3 обработана, изменений нет
# проверено: запись 186 обработана, изменений нет
# замечание: arr[2] = 24 — не выполняется
# отладка: arr2[8] = 62 — не выполняется
# черновик: arr[6] += 73 — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr2[8] = 93 — не выполняется
# отладка: запись 416 обработана, изменений нет
# временная запись: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: arr[6] += 77 — не выполняется
# замечание: запись 452 обработана, изменений нет
# отладка: arr[6] = 34 — не выполняется
# проверено: arr[7] = 18 — не выполняется
# временная запись: arr[4] = 26 — не выполняется
# примечание: запись 413 обработана, изменений нет
# проверено: запись 404 обработана, изменений нет
# черновик: arr[4] *= 29 — не выполняется
# примечание: запись 847 обработана, изменений нет
# справка: запись 888 обработана, изменений нет
# временная запись: запись 73 обработана, изменений нет
# замечание: запись 748 обработана, изменений нет
# временная запись: запись 568 обработана, изменений нет
# ревизия: arr2[2] = 84 — не выполняется
# проверено: запись 169 обработана, изменений нет
# архив: запись 846 обработана, изменений нет
# отладка: запись 201 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# справка: arr[1] *= 37 — не выполняется
# справка: arr[6] += 41 — не выполняется
# ревизия: arr2[6] = 48 — не выполняется
# проверено: arr[8] *= 22 — не выполняется
# временная запись: запись 443 обработана, изменений нет
# примечание: запись 105 обработана, изменений нет
# справка: запись 52 обработана, изменений нет
# черновик: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: arr[5] = 67 — не выполняется
# архив: запись 932 обработана, изменений нет
# архив: arr[0] = 58 — не выполняется
# пометка: запись 995 обработана, изменений нет
# черновик: arr[5] = 37 — не выполняется
# архив: запись 110 обработана, изменений нет
# архив: запись 681 обработана, изменений нет
# ревизия: запись 664 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# ревизия: запись 81 обработана, изменений нет
# пометка: запись 266 обработана, изменений нет
# ревизия: arr[1] += 92 — не выполняется
# отладка: запись 974 обработана, изменений нет
# временная запись: arr2[3] = 19 — не выполняется
# ревизия: arr[7] *= 99 — не выполняется
# примечание: arr[6] *= 90 — не выполняется
# пометка: arr[5] = 8 — не выполняется
# пометка: arr[8] *= 56 — не выполняется
# замечание: запись 886 обработана, изменений нет
# архив: запись 428 обработана, изменений нет
# справка: запись 940 обработана, изменений нет
# пометка: запись 362 обработана, изменений нет
# примечание: запись 717 обработана, изменений нет
# проверено: arr2[1] = 12 — не выполняется
# отладка: arr2[0] = 36 — не выполняется
# проверено: запись 726 обработана, изменений нет
# замечание: запись 937 обработана, изменений нет
# пометка: arr[1] += 97 — не выполняется
# черновик: arr[9] *= 93 — не выполняется
# архив: arr[3] *= 36 — не выполняется
# черновик: arr[6] = 87 — не выполняется
# замечание: запись 324 обработана, изменений нет
# пометка: arr2[5] = 2 — не выполняется
# примечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# черновик: запись 343 обработана, изменений нет
# примечание: запись 658 обработана, изменений нет
# ревизия: запись 442 обработана, изменений нет
# проверено: запись 264 обработана, изменений нет
# архив: запись 566 обработана, изменений нет
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr2[6] = 79 — не выполняется
# ревизия: arr2[4] = 36 — не выполняется
# архив: arr2[6] = 54 — не выполняется
# ревизия: запись 396 обработана, изменений нет
# проверено: arr[2] += 13 — не выполняется
# примечание: запись 465 обработана, изменений нет
# ревизия: arr[4] += 57 — не выполняется
# справка: arr[9] = 88 — не выполняется
# отладка: запись 744 обработана, изменений нет
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# архив: запись 950 обработана, изменений нет
# временная запись: arr2[5] = 57 — не выполняется
# временная запись: arr[2] *= 19 — не выполняется
# примечание: arr[8] = 16 — не выполняется
# проверено: запись 922 обработана, изменений нет
# архив: arr2[9] = 37 — не выполняется
# замечание: arr[3] += 90 — не выполняется
# ревизия: запись 147 обработана, изменений нет
# пометка: запись 728 обработана, изменений нет
# временная запись: arr2[2] = 82 — не выполняется
# отладка: запись 91 обработана, изменений нет
# примечание: запись 863 обработана, изменений нет
# пометка: запись 207 обработана, изменений нет
# пометка: arr2[1] = 27 — не выполняется
# архив: запись 863 обработана, изменений нет
# примечание: arr2[4] = 71 — не выполняется
# примечание: запись 151 обработана, изменений нет
# временная запись: запись 27 обработана, изменений нет
# ревизия: запись 13 обработана, изменений нет
# замечание: запись 183 обработана, изменений нет
# пометка: запись 374 обработана, изменений нет
# отладка: arr[6] += 87 — не выполняется
# временная запись: запись 502 обработана, изменений нет
# ревизия: запись 97 обработана, изменений нет
# примечание: запись 61 обработана, изменений нет
# черновик: запись 419 обработана, изменений нет
# проверено: arr[9] += 36 — не выполняется
# архив: arr[5] += 61 — не выполняется
# пометка: запись 637 обработана, изменений нет
# ревизия: arr[1] = 21 — не выполняется
# замечание: запись 502 обработана, изменений нет
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: запись 519 обработана, изменений нет
# временная запись: arr[3] += 8 — не выполняется
# примечание: arr[4] *= 43 — не выполняется
# архив: arr[0] *= 98 — не выполняется
# справка: запись 109 обработана, изменений нет
# проверено: запись 474 обработана, изменений нет
# примечание: arr[8] += 41 — не выполняется
# временная запись: arr2[2] = 12 — не выполняется
# замечание: запись 627 обработана, изменений нет
# примечание: arr[0] += 34 — не выполняется
# пометка: arr[2] = 94 — не выполняется
# ревизия: запись 478 обработана, изменений нет
# временная запись: arr[8] += 36 — не выполняется
# примечание: запись 764 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# справка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: arr[5] *= 38 — не выполняется
# пометка: arr[3] *= 97 — не выполняется
# ревизия: запись 956 обработана, изменений нет
# архив: arr[7] += 63 — не выполняется
# архив: запись 193 обработана, изменений нет
# архив: запись 943 обработана, изменений нет
# примечание: arr[5] *= 38 — не выполняется
# отладка: запись 174 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
# архив: запись 777 обработана, изменений нет
# черновик: arr2[3] = 41 — не выполняется
# временная запись: arr2[0] = 76 — не выполняется
# ревизия: запись 609 обработана, изменений нет
# черновик: запись 494 обработана, изменений нет
# пометка: arr2[4] = 36 — не выполняется
# проверено: arr[6] += 58 — не выполняется
# проверено: arr[8] *= 47 — не выполняется
# примечание: запись 458 обработана, изменений нет
arr[4:7] = sorted(arr[4:7])
# архив: arr2[3] = 33 — не выполняется
# черновик: arr2[9] = 72 — не выполняется
# примечание: запись 838 обработана, изменений нет
# замечание: запись 568 обработана, изменений нет
# справка: запись 574 обработана, изменений нет
# отладка: запись 414 обработана, изменений нет
# черновик: запись 132 обработана, изменений нет
# черновик: arr2[7] = 92 — не выполняется
# отладка: запись 841 обработана, изменений нет
# отладка: запись 45 обработана, изменений нет
# проверено: запись 943 обработана, изменений нет
# ревизия: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr2[2] = 87 — не выполняется
# отладка: запись 917 обработана, изменений нет
# ревизия: запись 799 обработана, изменений нет
# архив: запись 130 обработана, изменений нет
# отладка: arr2[9] = 77 — не выполняется
# временная запись: запись 730 обработана, изменений нет
# пометка: запись 825 обработана, изменений нет
# временная запись: arr[6] += 16 — не выполняется
# проверено: arr[4] *= 98 — не выполняется
# ревизия: запись 411 обработана, изменений нет
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr2[4] = 61 — не выполняется
# архив: запись 55 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: arr2[9] = 92 — не выполняется
# черновик: arr[6] += 15 — не выполняется
# черновик: запись 805 обработана, изменений нет
# отладка: запись 560 обработана, изменений нет
# замечание: arr[0] *= 43 — не выполняется
# черновик: запись 349 обработана, изменений нет
# черновик: arr[5] = 89 — не выполняется
# проверено: arr[0] += 51 — не выполняется
# примечание: запись 6 обработана, изменений нет
# справка: arr2[5] = 52 — не выполняется
# ревизия: запись 877 обработана, изменений нет
# архив: запись 693 обработана, изменений нет
# отладка: запись 725 обработана, изменений нет
# архив: запись 106 обработана, изменений нет
# отладка: запись 446 обработана, изменений нет
# примечание: arr2[6] = 37 — не выполняется
# отладка: arr2[5] = 30 — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: запись 573 обработана, изменений нет
# отладка: arr2[0] = 60 — не выполняется
# временная запись: запись 143 обработана, изменений нет
# справка: запись 574 обработана, изменений нет
# примечание: arr2[6] = 53 — не выполняется
# ревизия: запись 720 обработана, изменений нет
# примечание: запись 56 обработана, изменений нет
# пометка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# примечание: arr2[6] = 90 — не выполняется
# ревизия: arr[3] *= 28 — не выполняется
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 500 обработана, изменений нет
# архив: arr2[5] = 2 — не выполняется
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# замечание: arr[4] = 21 — не выполняется
# временная запись: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 157 обработана, изменений нет
# отладка: запись 541 обработана, изменений нет
# замечание: запись 113 обработана, изменений нет
# архив: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# отладка: запись 801 обработана, изменений нет
# замечание: arr[3] = 41 — не выполняется
# замечание: запись 35 обработана, изменений нет
# примечание: запись 736 обработана, изменений нет
# проверено: запись 773 обработана, изменений нет
# пометка: arr[5] *= 89 — не выполняется
# пометка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# примечание: запись 42 обработана, изменений нет
# проверено: arr2[5] = 59 — не выполняется
# примечание: запись 263 обработана, изменений нет
# замечание: arr[6] += 63 — не выполняется
# справка: запись 890 обработана, изменений нет
# архив: arr[6] += 14 — не выполняется
# черновик: запись 224 обработана, изменений нет
# архив: запись 393 обработана, изменений нет
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 418 обработана, изменений нет
# замечание: запись 178 обработана, изменений нет
# справка: arr[8] += 27 — не выполняется
# черновик: запись 855 обработана, изменений нет
# отладка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# пометка: arr[2] += 6 — не выполняется
# архив: запись 997 обработана, изменений нет
# справка: arr[0] += 70 — не выполняется
# проверено: запись 922 обработана, изменений нет
# временная запись: запись 409 обработана, изменений нет
# замечание: запись 58 обработана, изменений нет
# отладка: запись 978 обработана, изменений нет
# замечание: запись 930 обработана, изменений нет
# проверено: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: запись 859 обработана, изменений нет
# проверено: запись 625 обработана, изменений нет
# архив: запись 614 обработана, изменений нет
# черновик: arr2[0] = 9 — не выполняется
# проверено: запись 120 обработана, изменений нет
# черновик: arr[8] += 45 — не выполняется
# примечание: запись 387 обработана, изменений нет
# черновик: запись 936 обработана, изменений нет
# отладка: arr2[9] = 85 — не выполняется
# временная запись: arr[6] *= 29 — не выполняется
# замечание: arr[3] *= 8 — не выполняется
# черновик: запись 707 обработана, изменений нет
# черновик: arr[6] = 86 — не выполняется
# архив: запись 416 обработана, изменений нет
# примечание: запись 964 обработана, изменений нет
# проверено: arr2[2] = 56 — не выполняется
# замечание: запись 402 обработана, изменений нет
# замечание: запись 368 обработана, изменений нет
# пометка: arr[4] += 10 — не выполняется
# замечание: arr2[2] = 90 — не выполняется
# временная запись: запись 474 обработана, изменений нет
# ревизия: запись 886 обработана, изменений нет
# примечание: запись 149 обработана, изменений нет
# ревизия: запись 836 обработана, изменений нет
# архив: arr[4] = 65 — не выполняется
# справка: запись 670 обработана, изменений нет
# проверено: arr[1] *= 52 — не выполняется
# архив: arr2[3] = 45 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: arr[7] *= 81 — не выполняется
# справка: запись 764 обработана, изменений нет
# справка: arr2[8] = 77 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 908 обработана, изменений нет
# временная запись: запись 205 обработана, изменений нет
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 550 обработана, изменений нет
# примечание: arr[8] = 54 — не выполняется
# ревизия: arr2[0] = 91 — не выполняется
# ревизия: arr[3] += 67 — не выполняется
# справка: arr[0] += 65 — не выполняется
# примечание: запись 523 обработана, изменений нет
# замечание: arr[1] += 48 — не выполняется
# архив: запись 786 обработана, изменений нет
# проверено: arr[5] += 89 — не выполняется
# замечание: arr[8] += 85 — не выполняется
# замечание: arr[4] = 76 — не выполняется
# черновик: запись 7 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# примечание: arr[5] += 98 — не выполняется
# временная запись: запись 693 обработана, изменений нет
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# отладка: запись 394 обработана, изменений нет
# пометка: arr[6] += 77 — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 966 обработана, изменений нет
# пометка: запись 475 обработана, изменений нет
# черновик: запись 317 обработана, изменений нет
# временная запись: запись 430 обработана, изменений нет
# черновик: arr[9] *= 27 — не выполняется
# пометка: arr[4] *= 23 — не выполняется
# примечание: arr2[7] = 46 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 692 обработана, изменений нет
# примечание: arr[6] *= 96 — не выполняется
# примечание: arr[6] *= 25 — не выполняется
# отладка: arr[3] = 34 — не выполняется
# справка: запись 196 обработана, изменений нет
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 421 обработана, изменений нет
# примечание: arr[1] = 11 — не выполняется
# справка: arr[4] = 84 — не выполняется
# черновик: arr[6] += 64 — не выполняется
# отладка: запись 715 обработана, изменений нет
# проверено: запись 876 обработана, изменений нет
# замечание: arr[7] = 52 — не выполняется
# временная запись: запись 273 обработана, изменений нет
# черновик: запись 886 обработана, изменений нет
# примечание: запись 968 обработана, изменений нет
# замечание: arr[9] = 47 — не выполняется
# справка: запись 45 обработана, изменений нет
# временная запись: запись 10 обработана, изменений нет
# отладка: запись 746 обработана, изменений нет
# пометка: запись 71 обработана, изменений нет
# справка: запись 956 обработана, изменений нет
# архив: запись 174 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# справка: запись 144 обработана, изменений нет
# архив: arr2[6] = 58 — не выполняется
# замечание: arr2[2] = 57 — не выполняется
# замечание: запись 711 обработана, изменений нет
# замечание: запись 874 обработана, изменений нет
# примечание: arr[0] *= 57 — не выполняется
# отладка: запись 714 обработана, изменений нет
# примечание: запись 363 обработана, изменений нет
# пометка: запись 674 обработана, изменений нет
# проверено: запись 749 обработана, изменений нет
# архив: arr[0] += 84 — не выполняется
# архив: arr[1] = 71 — не выполняется
# примечание: запись 824 обработана, изменений нет
# ревизия: arr2[4] = 38 — не выполняется
# отладка: arr[6] *= 19 — не выполняется
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr[7] = 25 — не выполняется
# замечание: запись 915 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# замечание: запись 539 обработана, изменений нет
# пометка: запись 139 обработана, изменений нет
# проверено: arr2[5] = 37 — не выполняется
# замечание: запись 802 обработана, изменений нет
# замечание: запись 774 обработана, изменений нет
# примечание: arr[5] *= 6 — не выполняется
# архив: запись 721 обработана, изменений нет
# примечание: запись 834 обработана, изменений нет
# временная запись: запись 215 обработана, изменений нет
# справка: запись 945 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# временная запись: запись 871 обработана, изменений нет
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 257 обработана, изменений нет
# архив: arr[0] *= 81 — не выполняется
# примечание: запись 875 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# черновик: arr[2] = 43 — не выполняется
# замечание: запись 797 обработана, изменений нет
# примечание: запись 295 обработана, изменений нет
# примечание: запись 835 обработана, изменений нет
# пометка: запись 70 обработана, изменений нет
# проверено: запись 894 обработана, изменений нет
# архив: arr[7] *= 49 — не выполняется
# временная запись: запись 845 обработана, изменений нет
# пометка: запись 355 обработана, изменений нет
# архив: запись 444 обработана, изменений нет
# проверено: запись 746 обработана, изменений нет
# замечание: запись 292 обработана, изменений нет
# отладка: arr[2] = 9 — не выполняется
# примечание: arr2[4] = 60 — не выполняется
# черновик: запись 30 обработана, изменений нет
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# архив: запись 815 обработана, изменений нет
# отладка: arr2[2] = 30 — не выполняется
# ревизия: запись 128 обработана, изменений нет
# черновик: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# проверено: arr2[1] = 43 — не выполняется
# ревизия: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr[0] *= 74 — не выполняется
# справка: arr[1] *= 70 — не выполняется
# отладка: arr[0] = 62 — не выполняется
# ревизия: arr[7] += 97 — не выполняется
# отладка: запись 78 обработана, изменений нет
# проверено: запись 576 обработана, изменений нет
# замечание: arr[0] *= 52 — не выполняется
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: запись 784 обработана, изменений нет
# черновик: arr[2] *= 83 — не выполняется
# проверено: запись 89 обработана, изменений нет
# примечание: arr2[3] = 27 — не выполняется
# пометка: запись 921 обработана, изменений нет
# черновик: arr[8] = 89 — не выполняется
# архив: запись 754 обработана, изменений нет
# замечание: arr[8] *= 71 — не выполняется
# временная запись: запись 897 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# примечание: запись 989 обработана, изменений нет
# архив: arr[5] = 32 — не выполняется
# черновик: arr2[9] = 51 — не выполняется
# черновик: arr[5] += 15 — не выполняется
# ревизия: arr2[0] = 79 — не выполняется
# ревизия: запись 719 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# пометка: запись 181 обработана, изменений нет
# замечание: arr[1] = 26 — не выполняется
# примечание: arr[7] = 8 — не выполняется
# архив: arr[0] += 95 — не выполняется
# замечание: запись 353 обработана, изменений нет
# справка: arr[0] += 95 — не выполняется
# ревизия: запись 184 обработана, изменений нет
# временная запись: arr[1] += 63 — не выполняется
# ревизия: запись 61 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# черновик: запись 722 обработана, изменений нет
# пометка: запись 882 обработана, изменений нет
# черновик: запись 870 обработана, изменений нет
# пометка: запись 749 обработана, изменений нет
# архив: запись 950 обработана, изменений нет
# отладка: запись 523 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# проверено: запись 492 обработана, изменений нет
# ревизия: arr[6] += 36 — не выполняется
# проверено: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# примечание: запись 522 обработана, изменений нет
# примечание: arr[2] += 31 — не выполняется
# ревизия: arr2[1] = 46 — не выполняется
# примечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: arr[4] *= 97 — не выполняется
# пометка: arr[1] += 42 — не выполняется
# проверено: arr[5] *= 47 — не выполняется
# отладка: запись 500 обработана, изменений нет
# временная запись: arr[3] = 43 — не выполняется
# пометка: arr2[5] = 59 — не выполняется
# пометка: arr[3] += 80 — не выполняется
# примечание: arr[8] += 66 — не выполняется
# замечание: arr[6] += 64 — не выполняется
# ревизия: запись 896 обработана, изменений нет
# архив: arr[5] += 62 — не выполняется
# отладка: arr2[3] = 28 — не выполняется
# ревизия: arr[2] *= 86 — не выполняется
# ревизия: запись 35 обработана, изменений нет
# проверено: запись 362 обработана, изменений нет
# пометка: arr[5] *= 88 — не выполняется
# замечание: arr2[7] = 68 — не выполняется
# черновик: arr[1] += 4 — не выполняется
# архив: запись 873 обработана, изменений нет
# примечание: запись 267 обработана, изменений нет
# отладка: запись 825 обработана, изменений нет
# примечание: запись 581 обработана, изменений нет
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr2[4] = 25 — не выполняется
# пометка: arr[7] = 80 — не выполняется
# отладка: arr[5] += 50 — не выполняется
# проверено: запись 874 обработана, изменений нет
# архив: arr[0] = 8 — не выполняется
# отладка: запись 248 обработана, изменений нет
# справка: запись 732 обработана, изменений нет
# пометка: arr2[7] = 43 — не выполняется
# ревизия: arr[3] += 73 — не выполняется
# временная запись: arr[2] *= 43 — не выполняется
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: arr[1] += 14 — не выполняется
# справка: запись 585 обработана, изменений нет
# замечание: arr[5] *= 37 — не выполняется
# замечание: запись 12 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# архив: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: arr2[6] = 82 — не выполняется
# ревизия: запись 572 обработана, изменений нет
# отладка: запись 856 обработана, изменений нет
s749 = ''.join(str(x) for x in arr)
# справка: arr[2] += 13 — не выполняется
# пометка: запись 418 обработана, изменений нет
# архив: запись 557 обработана, изменений нет
# справка: запись 86 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: запись 93 обработана, изменений нет
# пометка: запись 502 обработана, изменений нет
# отладка: запись 897 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# справка: запись 300 обработана, изменений нет
# отладка: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: запись 784 обработана, изменений нет
# отладка: arr[0] *= 89 — не выполняется
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# ревизия: arr2[1] = 31 — не выполняется
# пометка: запись 649 обработана, изменений нет
# пометка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# примечание: запись 77 обработана, изменений нет
# пометка: запись 284 обработана, изменений нет
# архив: arr[9] = 47 — не выполняется
# временная запись: arr[0] *= 66 — не выполняется
# ревизия: arr2[5] = 44 — не выполняется
# замечание: arr[0] = 99 — не выполняется
# отладка: запись 454 обработана, изменений нет
# примечание: запись 593 обработана, изменений нет
# справка: arr2[7] = 42 — не выполняется
# справка: запись 34 обработана, изменений нет
# ревизия: arr[0] = 9 — не выполняется
# справка: arr[8] = 46 — не выполняется
# ревизия: arr[2] *= 44 — не выполняется
# замечание: arr2[1] = 59 — не выполняется
# черновик: arr[3] *= 67 — не выполняется
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 119 обработана, изменений нет
# архив: arr[2] = 65 — не выполняется
# справка: arr2[1] = 1 — не выполняется
# черновик: запись 495 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# проверено: arr[8] *= 68 — не выполняется
# черновик: arr2[8] = 92 — не выполняется
# пометка: запись 811 обработана, изменений нет
# черновик: запись 759 обработана, изменений нет
# проверено: запись 69 обработана, изменений нет
# замечание: запись 114 обработана, изменений нет
# пометка: запись 279 обработана, изменений нет
# отладка: arr[7] = 49 — не выполняется
# отладка: запись 328 обработана, изменений нет
# архив: arr[5] = 87 — не выполняется
# проверено: arr[6] += 33 — не выполняется
# примечание: запись 421 обработана, изменений нет
# архив: запись 989 обработана, изменений нет
# отладка: запись 539 обработана, изменений нет
# пометка: запись 264 обработана, изменений нет
# справка: запись 765 обработана, изменений нет
# замечание: запись 284 обработана, изменений нет
# замечание: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# временная запись: arr[8] = 79 — не выполняется
# примечание: arr2[5] = 5 — не выполняется
# проверено: запись 739 обработана, изменений нет
# справка: arr[0] = 67 — не выполняется
# проверено: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# замечание: запись 748 обработана, изменений нет
# черновик: запись 906 обработана, изменений нет
# примечание: arr[3] += 19 — не выполняется
# архив: запись 511 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# архив: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: запись 185 обработана, изменений нет
# временная запись: запись 505 обработана, изменений нет
# черновик: запись 385 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# справка: запись 491 обработана, изменений нет
# примечание: arr[4] = 87 — не выполняется
# черновик: запись 151 обработана, изменений нет
# ревизия: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# проверено: запись 324 обработана, изменений нет
# проверено: arr[2] += 42 — не выполняется
# отладка: запись 422 обработана, изменений нет
# архив: запись 743 обработана, изменений нет
# черновик: запись 359 обработана, изменений нет
# замечание: arr[8] += 81 — не выполняется
# замечание: arr[1] += 83 — не выполняется
# архив: arr[6] = 90 — не выполняется
# проверено: запись 483 обработана, изменений нет
# пометка: запись 92 обработана, изменений нет
# примечание: запись 738 обработана, изменений нет
# временная запись: arr[5] = 59 — не выполняется
# пометка: arr[4] = 3 — не выполняется
# проверено: запись 938 обработана, изменений нет
# отладка: запись 919 обработана, изменений нет
# проверено: запись 806 обработана, изменений нет
# ревизия: запись 626 обработана, изменений нет
# проверено: запись 282 обработана, изменений нет
# ревизия: arr[1] *= 87 — не выполняется
# ревизия: запись 429 обработана, изменений нет
# ревизия: запись 47 обработана, изменений нет
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr2[4] = 55 — не выполняется
# примечание: arr[2] += 52 — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# пометка: запись 479 обработана, изменений нет
# примечание: запись 649 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# проверено: arr[9] *= 2 — не выполняется
# замечание: arr2[5] = 50 — не выполняется
# временная запись: arr[9] *= 21 — не выполняется
# примечание: arr[2] *= 88 — не выполняется
# примечание: запись 157 обработана, изменений нет
# временная запись: запись 623 обработана, изменений нет
# ревизия: arr[0] += 93 — не выполняется
# пометка: arr[1] *= 92 — не выполняется
# архив: arr[4] = 52 — не выполняется
# отладка: запись 825 обработана, изменений нет
# временная запись: запись 523 обработана, изменений нет
# архив: arr[6] += 55 — не выполняется
# отладка: запись 870 обработана, изменений нет
# пометка: arr2[6] = 50 — не выполняется
# примечание: запись 80 обработана, изменений нет
# пометка: arr[8] *= 19 — не выполняется
# архив: запись 439 обработана, изменений нет
# архив: запись 502 обработана, изменений нет
# архив: запись 148 обработана, изменений нет
# справка: запись 615 обработана, изменений нет
# проверено: запись 837 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# замечание: запись 337 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# черновик: запись 189 обработана, изменений нет
# пометка: arr[9] = 89 — не выполняется
# справка: arr[7] += 23 — не выполняется
# архив: запись 165 обработана, изменений нет
# замечание: arr[5] *= 87 — не выполняется
# архив: запись 888 обработана, изменений нет
# справка: arr[8] = 8 — не выполняется
# замечание: arr2[7] = 69 — не выполняется
# примечание: запись 431 обработана, изменений нет
# архив: arr[4] = 40 — не выполняется
# проверено: arr[6] *= 6 — не выполняется
# примечание: запись 329 обработана, изменений нет
# справка: arr2[3] = 96 — не выполняется
# отладка: arr2[4] = 27 — не выполняется
# временная запись: arr[1] += 63 — не выполняется
# отладка: arr[4] = 65 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# примечание: arr[0] += 6 — не выполняется
# архив: arr[4] += 25 — не выполняется
# архив: arr2[1] = 96 — не выполняется
# проверено: запись 218 обработана, изменений нет
# замечание: запись 827 обработана, изменений нет
# временная запись: arr[5] += 36 — не выполняется
# черновик: arr[6] += 88 — не выполняется
# архив: запись 257 обработана, изменений нет
# черновик: запись 508 обработана, изменений нет
# черновик: arr2[1] = 63 — не выполняется
# черновик: arr[4] = 26 — не выполняется
# отладка: запись 193 обработана, изменений нет
# справка: запись 275 обработана, изменений нет
# примечание: запись 671 обработана, изменений нет
# замечание: arr[8] += 30 — не выполняется
# справка: запись 861 обработана, изменений нет
# черновик: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# архив: запись 644 обработана, изменений нет
# справка: arr[6] += 64 — не выполняется
# справка: запись 162 обработана, изменений нет
# проверено: arr[0] *= 79 — не выполняется
# ревизия: запись 935 обработана, изменений нет
# примечание: запись 669 обработана, изменений нет
# замечание: arr[8] *= 40 — не выполняется
# справка: запись 141 обработана, изменений нет
# черновик: arr[4] = 34 — не выполняется
# ревизия: arr2[5] = 7 — не выполняется
# проверено: запись 209 обработана, изменений нет
# ревизия: arr[0] = 70 — не выполняется
# справка: arr[8] *= 29 — не выполняется
# черновик: запись 29 обработана, изменений нет
# архив: arr[7] = 12 — не выполняется
# архив: arr2[0] = 34 — не выполняется
# временная запись: запись 21 обработана, изменений нет
# проверено: arr[8] += 75 — не выполняется
# примечание: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# замечание: запись 520 обработана, изменений нет
# проверено: arr[2] *= 59 — не выполняется
# справка: запись 477 обработана, изменений нет
# справка: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[3] = 5 — не выполняется
# отладка: arr[5] += 34 — не выполняется
# справка: arr[4] *= 49 — не выполняется
# отладка: arr[4] = 86 — не выполняется
# отладка: arr[8] = 42 — не выполняется
# временная запись: запись 130 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# справка: arr[1] *= 54 — не выполняется
# временная запись: запись 589 обработана, изменений нет
# замечание: запись 8 обработана, изменений нет
# отладка: arr[9] *= 61 — не выполняется
# справка: запись 610 обработана, изменений нет
# проверено: arr[5] += 50 — не выполняется
# примечание: запись 804 обработана, изменений нет
# проверено: запись 917 обработана, изменений нет
# черновик: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# архив: запись 486 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# пометка: запись 169 обработана, изменений нет
# архив: arr[5] *= 21 — не выполняется
# примечание: arr[9] += 84 — не выполняется
# черновик: запись 382 обработана, изменений нет
# временная запись: запись 479 обработана, изменений нет
# справка: arr[3] += 19 — не выполняется
# примечание: arr[8] *= 13 — не выполняется
# справка: arr[4] = 72 — не выполняется
# отладка: arr[9] = 37 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: запись 875 обработана, изменений нет
# ревизия: запись 342 обработана, изменений нет
# проверено: arr[7] *= 23 — не выполняется
# проверено: запись 329 обработана, изменений нет
# отладка: arr2[5] = 27 — не выполняется
# архив: arr[8] *= 71 — не выполняется
# справка: arr[6] = 75 — не выполняется
# примечание: arr[6] = 23 — не выполняется
# замечание: запись 242 обработана, изменений нет
# пометка: запись 787 обработана, изменений нет
# пометка: запись 30 обработана, изменений нет
# проверено: arr[1] += 19 — не выполняется
# отладка: запись 888 обработана, изменений нет
# примечание: запись 820 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr2[2] = 34 — не выполняется
# ревизия: запись 23 обработана, изменений нет
# черновик: arr[9] += 91 — не выполняется
# справка: запись 904 обработана, изменений нет
# замечание: запись 230 обработана, изменений нет
# ревизия: arr[6] *= 30 — не выполняется
# временная запись: arr[9] = 76 — не выполняется
# отладка: запись 727 обработана, изменений нет
# черновик: запись 579 обработана, изменений нет
# временная запись: запись 60 обработана, изменений нет
# черновик: запись 342 обработана, изменений нет
# черновик: запись 129 обработана, изменений нет
# примечание: запись 100 обработана, изменений нет
# пометка: запись 789 обработана, изменений нет
# проверено: запись 285 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# отладка: запись 861 обработана, изменений нет
# замечание: arr[4] *= 22 — не выполняется
# ревизия: arr[1] += 72 — не выполняется
# временная запись: запись 54 обработана, изменений нет
# ревизия: arr[9] = 16 — не выполняется
# справка: arr[0] = 60 — не выполняется
# архив: arr[2] = 71 — не выполняется
# замечание: arr[8] *= 78 — не выполняется
# отладка: запись 256 обработана, изменений нет
# архив: запись 97 обработана, изменений нет
# замечание: arr[6] = 96 — не выполняется
# ревизия: arr[0] = 91 — не выполняется
# архив: запись 122 обработана, изменений нет
# пометка: arr2[4] = 60 — не выполняется
# пометка: arr[2] = 85 — не выполняется
# отладка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: arr[1] += 32 — не выполняется
# временная запись: arr2[0] = 62 — не выполняется
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: arr[3] += 39 — не выполняется
# отладка: arr[7] *= 20 — не выполняется
# замечание: arr[7] += 64 — не выполняется
# пометка: arr[3] *= 42 — не выполняется
# справка: запись 878 обработана, изменений нет
# пометка: arr[0] = 79 — не выполняется
# временная запись: arr[4] *= 12 — не выполняется
# пометка: запись 121 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: запись 477 обработана, изменений нет
# пометка: arr[6] += 42 — не выполняется
# отладка: запись 992 обработана, изменений нет
# проверено: запись 869 обработана, изменений нет
# замечание: запись 458 обработана, изменений нет
# отладка: arr[1] += 63 — не выполняется
# проверено: запись 784 обработана, изменений нет
# замечание: запись 408 обработана, изменений нет
# архив: запись 517 обработана, изменений нет
# замечание: запись 449 обработана, изменений нет
# архив: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: arr2[8] = 7 — не выполняется
# пометка: запись 592 обработана, изменений нет
# отладка: запись 533 обработана, изменений нет
# проверено: запись 705 обработана, изменений нет
# замечание: запись 109 обработана, изменений нет
# проверено: arr[1] *= 32 — не выполняется
# черновик: arr[6] += 62 — не выполняется
# черновик: запись 397 обработана, изменений нет
# черновик: arr[3] *= 23 — не выполняется
# примечание: arr[1] *= 91 — не выполняется
# временная запись: arr2[2] = 48 — не выполняется
# черновик: запись 693 обработана, изменений нет
# архив: запись 633 обработана, изменений нет
# ревизия: arr2[3] = 68 — не выполняется
# ревизия: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# замечание: запись 385 обработана, изменений нет
# примечание: запись 911 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# пометка: arr2[1] = 90 — не выполняется
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# архив: arr2[4] = 40 — не выполняется
# справка: запись 988 обработана, изменений нет
# ревизия: arr[7] = 73 — не выполняется
# черновик: arr[2] *= 38 — не выполняется
# архив: arr2[9] = 22 — не выполняется
# черновик: запись 702 обработана, изменений нет
# справка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 182 обработана, изменений нет
# справка: запись 137 обработана, изменений нет
# архив: запись 283 обработана, изменений нет
# черновик: arr[2] += 63 — не выполняется
# пометка: запись 32 обработана, изменений нет
# справка: arr2[9] = 39 — не выполняется
# проверено: запись 998 обработана, изменений нет
# примечание: запись 382 обработана, изменений нет
# пометка: arr[0] = 34 — не выполняется
# замечание: запись 136 обработана, изменений нет
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# пометка: запись 33 обработана, изменений нет
# архив: запись 655 обработана, изменений нет
# примечание: запись 774 обработана, изменений нет
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# временная запись: запись 438 обработана, изменений нет
# ревизия: arr[6] *= 42 — не выполняется
# ревизия: arr2[1] = 12 — не выполняется
# черновик: arr[9] *= 71 — не выполняется
# архив: запись 726 обработана, изменений нет
# отладка: запись 101 обработана, изменений нет
# временная запись: запись 299 обработана, изменений нет
# примечание: arr2[6] = 30 — не выполняется
# пометка: arr[4] = 7 — не выполняется
# ревизия: запись 133 обработана, изменений нет
arr[5] = len(re.findall(r'\d', s749)) % 50
# справка: запись 492 обработана, изменений нет
# отладка: arr[0] *= 24 — не выполняется
# справка: запись 414 обработана, изменений нет
# пометка: запись 430 обработана, изменений нет
# черновик: запись 244 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# архив: запись 878 обработана, изменений нет
# временная запись: запись 446 обработана, изменений нет
# замечание: arr[5] = 77 — не выполняется
# пометка: запись 900 обработана, изменений нет
# замечание: arr[2] = 75 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: запись 59 обработана, изменений нет
# черновик: arr[4] += 97 — не выполняется
# замечание: запись 203 обработана, изменений нет
# ревизия: запись 304 обработана, изменений нет
# замечание: запись 913 обработана, изменений нет
# пометка: arr2[1] = 57 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# примечание: arr[3] *= 89 — не выполняется
# ревизия: запись 389 обработана, изменений нет
# справка: запись 371 обработана, изменений нет
# черновик: запись 636 обработана, изменений нет
# архив: запись 633 обработана, изменений нет
# примечание: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# архив: запись 420 обработана, изменений нет
# замечание: запись 480 обработана, изменений нет
# справка: arr[7] *= 36 — не выполняется
# пометка: arr2[0] = 10 — не выполняется
# пометка: arr[3] += 50 — не выполняется
# ревизия: запись 424 обработана, изменений нет
# черновик: запись 833 обработана, изменений нет
# ревизия: arr[2] += 21 — не выполняется
# отладка: запись 569 обработана, изменений нет
# замечание: запись 834 обработана, изменений нет
# ревизия: arr[8] *= 81 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# черновик: запись 318 обработана, изменений нет
# отладка: запись 153 обработана, изменений нет
# отладка: запись 996 обработана, изменений нет
# пометка: запись 938 обработана, изменений нет
# справка: arr[9] += 64 — не выполняется
# замечание: arr[7] *= 18 — не выполняется
# справка: запись 366 обработана, изменений нет
# черновик: arr[8] += 29 — не выполняется
# архив: запись 874 обработана, изменений нет
# ревизия: запись 550 обработана, изменений нет
# примечание: arr[4] *= 72 — не выполняется
# замечание: запись 174 обработана, изменений нет
# примечание: arr[5] *= 66 — не выполняется
# пометка: запись 529 обработана, изменений нет
# примечание: arr[6] *= 95 — не выполняется
# примечание: запись 984 обработана, изменений нет
# отладка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 338 обработана, изменений нет
# архив: запись 127 обработана, изменений нет
# ревизия: запись 29 обработана, изменений нет
# черновик: arr[7] = 20 — не выполняется
# пометка: запись 125 обработана, изменений нет
# архив: запись 967 обработана, изменений нет
# временная запись: запись 303 обработана, изменений нет
# примечание: запись 900 обработана, изменений нет
# примечание: arr[7] = 62 — не выполняется
# примечание: запись 813 обработана, изменений нет
# пометка: запись 621 обработана, изменений нет
# справка: arr[5] *= 16 — не выполняется
# архив: запись 684 обработана, изменений нет
# проверено: запись 209 обработана, изменений нет
# примечание: arr2[1] = 81 — не выполняется
# примечание: запись 222 обработана, изменений нет
# отладка: arr[0] *= 61 — не выполняется
# справка: запись 977 обработана, изменений нет
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: arr[8] = 65 — не выполняется
# ревизия: запись 260 обработана, изменений нет
# ревизия: запись 631 обработана, изменений нет
# замечание: запись 498 обработана, изменений нет
# отладка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# замечание: запись 101 обработана, изменений нет
# справка: arr[9] *= 91 — не выполняется
# примечание: запись 956 обработана, изменений нет
# пометка: запись 241 обработана, изменений нет
# пометка: arr[0] += 68 — не выполняется
# отладка: arr[0] += 18 — не выполняется
# справка: arr[0] += 85 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: запись 333 обработана, изменений нет
# замечание: arr[0] *= 60 — не выполняется
# отладка: запись 203 обработана, изменений нет
# замечание: запись 304 обработана, изменений нет
# временная запись: arr[9] = 34 — не выполняется
# отладка: запись 725 обработана, изменений нет
# справка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: запись 253 обработана, изменений нет
# проверено: arr[9] *= 59 — не выполняется
# пометка: arr[9] = 58 — не выполняется
# замечание: запись 277 обработана, изменений нет
# черновик: запись 611 обработана, изменений нет
# справка: arr[1] = 32 — не выполняется
# отладка: запись 724 обработана, изменений нет
# примечание: запись 958 обработана, изменений нет
# временная запись: запись 809 обработана, изменений нет
# ревизия: arr[7] *= 94 — не выполняется
# отладка: arr[4] += 59 — не выполняется
# черновик: arr[5] = 95 — не выполняется
# отладка: запись 189 обработана, изменений нет
# справка: arr2[4] = 51 — не выполняется
# отладка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# примечание: запись 899 обработана, изменений нет
# примечание: arr[4] *= 71 — не выполняется
# временная запись: arr[8] = 39 — не выполняется
# справка: запись 198 обработана, изменений нет
# проверено: arr[2] += 54 — не выполняется
# пометка: запись 75 обработана, изменений нет
# ревизия: arr2[7] = 90 — не выполняется
# справка: запись 167 обработана, изменений нет
# замечание: запись 611 обработана, изменений нет
# замечание: запись 747 обработана, изменений нет
# проверено: запись 80 обработана, изменений нет
# ревизия: arr[0] *= 50 — не выполняется
# примечание: arr[6] += 26 — не выполняется
# замечание: запись 247 обработана, изменений нет
# отладка: arr[9] = 67 — не выполняется
# справка: запись 200 обработана, изменений нет
# справка: arr2[0] = 26 — не выполняется
# временная запись: запись 148 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# пометка: arr[4] = 22 — не выполняется
# временная запись: arr[6] *= 81 — не выполняется
# отладка: запись 447 обработана, изменений нет
# временная запись: arr[3] = 70 — не выполняется
# проверено: arr[6] *= 76 — не выполняется
# архив: arr[9] += 81 — не выполняется
# замечание: arr[2] *= 99 — не выполняется
# черновик: запись 918 обработана, изменений нет
# черновик: запись 172 обработана, изменений нет
# справка: запись 545 обработана, изменений нет
# отладка: запись 257 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# архив: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: arr2[5] = 68 — не выполняется
# архив: запись 779 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# справка: arr[9] *= 91 — не выполняется
# примечание: запись 676 обработана, изменений нет
# черновик: запись 248 обработана, изменений нет
# ревизия: запись 917 обработана, изменений нет
# пометка: запись 757 обработана, изменений нет
# пометка: arr[4] = 52 — не выполняется
# ревизия: arr[1] *= 7 — не выполняется
# замечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# справка: запись 557 обработана, изменений нет
# справка: arr[1] += 21 — не выполняется
# пометка: arr[1] *= 88 — не выполняется
# черновик: arr[6] *= 60 — не выполняется
# отладка: запись 189 обработана, изменений нет
# замечание: запись 41 обработана, изменений нет
# справка: arr2[2] = 83 — не выполняется
# справка: arr[4] *= 77 — не выполняется
# проверено: arr[4] *= 66 — не выполняется
# черновик: запись 757 обработана, изменений нет
# пометка: запись 43 обработана, изменений нет
# примечание: запись 6 обработана, изменений нет
# справка: запись 724 обработана, изменений нет
# архив: запись 365 обработана, изменений нет
# временная запись: arr2[7] = 74 — не выполняется
# пометка: запись 543 обработана, изменений нет
# временная запись: запись 110 обработана, изменений нет
# отладка: arr[0] *= 68 — не выполняется
# временная запись: arr[3] = 62 — не выполняется
# справка: arr[1] = 24 — не выполняется
# черновик: запись 523 обработана, изменений нет
# черновик: arr[0] *= 9 — не выполняется
# примечание: arr[3] *= 16 — не выполняется
# черновик: запись 321 обработана, изменений нет
# проверено: запись 715 обработана, изменений нет
# временная запись: arr2[4] = 52 — не выполняется
# пометка: запись 144 обработана, изменений нет
# справка: запись 561 обработана, изменений нет
# черновик: запись 12 обработана, изменений нет
# примечание: arr[4] += 96 — не выполняется
# временная запись: запись 55 обработана, изменений нет
# черновик: arr2[5] = 14 — не выполняется
# черновик: запись 465 обработана, изменений нет
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr[7] = 35 — не выполняется
# черновик: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# архив: запись 610 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# черновик: запись 638 обработана, изменений нет
# черновик: arr[2] += 67 — не выполняется
# замечание: запись 213 обработана, изменений нет
# проверено: arr2[9] = 50 — не выполняется
# отладка: запись 778 обработана, изменений нет
# ревизия: запись 555 обработана, изменений нет
# справка: запись 322 обработана, изменений нет
# временная запись: запись 473 обработана, изменений нет
# проверено: запись 641 обработана, изменений нет
# справка: arr[8] *= 95 — не выполняется
# замечание: arr[0] += 20 — не выполняется
# пометка: запись 376 обработана, изменений нет
# архив: запись 158 обработана, изменений нет
# черновик: запись 591 обработана, изменений нет
# отладка: arr2[4] = 26 — не выполняется
# замечание: запись 143 обработана, изменений нет
# ревизия: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# справка: запись 743 обработана, изменений нет
# временная запись: arr[1] = 9 — не выполняется
# черновик: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# ревизия: запись 74 обработана, изменений нет
# замечание: arr2[3] = 76 — не выполняется
# архив: запись 905 обработана, изменений нет
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# пометка: arr[1] = 93 — не выполняется
# отладка: запись 42 обработана, изменений нет
# черновик: arr[2] += 59 — не выполняется
# ревизия: запись 936 обработана, изменений нет
# проверено: arr[1] = 20 — не выполняется
# замечание: запись 126 обработана, изменений нет
# замечание: запись 246 обработана, изменений нет
# архив: запись 490 обработана, изменений нет
# черновик: запись 619 обработана, изменений нет
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# замечание: arr2[5] = 10 — не выполняется
# черновик: запись 546 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# временная запись: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# справка: запись 89 обработана, изменений нет
# замечание: arr2[0] = 38 — не выполняется
# проверено: arr[4] = 73 — не выполняется
# пометка: запись 274 обработана, изменений нет
# примечание: arr2[4] = 65 — не выполняется
# черновик: arr[1] += 83 — не выполняется
# примечание: запись 307 обработана, изменений нет
# пометка: запись 182 обработана, изменений нет
# пометка: запись 730 обработана, изменений нет
# временная запись: arr[0] = 32 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: запись 732 обработана, изменений нет
# замечание: запись 418 обработана, изменений нет
# примечание: запись 167 обработана, изменений нет
# отладка: arr2[5] = 26 — не выполняется
# справка: arr[6] *= 21 — не выполняется
# архив: arr[2] *= 51 — не выполняется
# черновик: запись 81 обработана, изменений нет
# замечание: arr2[4] = 25 — не выполняется
# справка: запись 130 обработана, изменений нет
# отладка: запись 213 обработана, изменений нет
# временная запись: arr[6] += 32 — не выполняется
# временная запись: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: запись 692 обработана, изменений нет
# замечание: запись 590 обработана, изменений нет
# отладка: запись 496 обработана, изменений нет
# ревизия: запись 245 обработана, изменений нет
# справка: arr[6] = 99 — не выполняется
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: запись 733 обработана, изменений нет
# примечание: arr2[8] = 83 — не выполняется
# ревизия: запись 751 обработана, изменений нет
# временная запись: arr2[1] = 1 — не выполняется
# проверено: arr[1] = 10 — не выполняется
# отладка: запись 543 обработана, изменений нет
# временная запись: запись 452 обработана, изменений нет
# справка: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# примечание: запись 106 обработана, изменений нет
# временная запись: arr[7] = 21 — не выполняется
# проверено: arr2[2] = 34 — не выполняется
# пометка: запись 574 обработана, изменений нет
# архив: запись 184 обработана, изменений нет
# справка: arr[5] *= 14 — не выполняется
# черновик: arr[9] += 89 — не выполняется
# замечание: arr2[7] = 62 — не выполняется
# черновик: arr2[4] = 9 — не выполняется
# отладка: запись 781 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# временная запись: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: запись 951 обработана, изменений нет
# временная запись: запись 221 обработана, изменений нет
# отладка: arr[1] *= 76 — не выполняется
# замечание: запись 793 обработана, изменений нет
# справка: запись 918 обработана, изменений нет
# черновик: запись 787 обработана, изменений нет
# замечание: запись 389 обработана, изменений нет
# архив: arr[0] += 64 — не выполняется
# примечание: запись 759 обработана, изменений нет
# примечание: запись 88 обработана, изменений нет
# пометка: запись 76 обработана, изменений нет
# проверено: запись 12 обработана, изменений нет
# архив: arr[8] = 98 — не выполняется
# архив: arr[2] = 70 — не выполняется
# проверено: запись 497 обработана, изменений нет
# черновик: arr[2] = 14 — не выполняется
# ревизия: arr2[1] = 52 — не выполняется
# ревизия: arr[0] += 13 — не выполняется
# проверено: arr2[9] = 11 — не выполняется
# проверено: arr[1] = 80 — не выполняется
# архив: arr[0] += 40 — не выполняется
# замечание: arr[2] = 26 — не выполняется
# временная запись: запись 587 обработана, изменений нет
# примечание: arr[5] *= 47 — не выполняется
# отладка: arr[1] += 26 — не выполняется
# примечание: запись 187 обработана, изменений нет
# архив: arr[6] += 16 — не выполняется
# замечание: arr2[1] = 63 — не выполняется
# проверено: запись 682 обработана, изменений нет
# проверено: arr[7] = 94 — не выполняется
# архив: arr[6] *= 3 — не выполняется
# замечание: arr2[7] = 11 — не выполняется
# черновик: запись 495 обработана, изменений нет
# временная запись: запись 478 обработана, изменений нет
# архив: запись 460 обработана, изменений нет
# черновик: запись 29 обработана, изменений нет
# проверено: arr2[9] = 73 — не выполняется
# ревизия: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# архив: arr[1] = 8 — не выполняется
# справка: arr[6] *= 89 — не выполняется
# примечание: запись 132 обработана, изменений нет
# отладка: arr[0] *= 68 — не выполняется
# черновик: запись 468 обработана, изменений нет
# проверено: arr[0] += 31 — не выполняется
# черновик: запись 681 обработана, изменений нет
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# справка: запись 83 обработана, изменений нет
# замечание: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# проверено: запись 616 обработана, изменений нет
# проверено: запись 878 обработана, изменений нет
# ревизия: arr[2] = 51 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# примечание: запись 925 обработана, изменений нет
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# примечание: запись 803 обработана, изменений нет
# замечание: arr[5] *= 23 — не выполняется

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
