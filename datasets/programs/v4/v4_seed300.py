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
arr[9], arr[2] = arr[2], arr[9]
arr[6] = 24
arr[2], arr[3] = arr[3], arr[2]
arr[9] = 50
arr[0], arr[1] = arr[1], arr[0]
arr[8] *= 33
arr[9] *= 2
arr[1] = 14
"""

TRAP_0 = "arr[6] = 409"
TRAP_1 = "arr[0] = 703"
TRAP_2 = "arr[2] = 148"
TRAP_3 = "arr[7] = 554"
TRAP_4 = "arr[0] = 732"
TRAP_5 = "arr[4] = 793"
TRAP_6 = "arr[3] = 798"
TRAP_7 = "arr[6] = 343"
TRAP_8 = "arr[6] = 292"
TRAP_9 = "arr[4] = 244"
TRAP_10 = "arr[8] = 435"
TRAP_11 = "arr[7] = 538"
TRAP_12 = "arr[3] = 478"
TRAP_13 = "arr[9] = 774"
TRAP_14 = "arr[6] = 255"
TRAP_15 = "arr[1] = 941"
TRAP_16 = "arr[0] = 374"
TRAP_17 = "arr[6] = 767"
TRAP_18 = "arr[3] = 709"
TRAP_19 = "arr[0] = 367"
TRAP_20 = "arr[9] = 480"
TRAP_21 = "arr[1] = 620"
TRAP_22 = "arr[9] = 169"
TRAP_23 = "arr[5] = 933"
TRAP_24 = "arr[0] = 280"
TRAP_25 = "arr[3] = 980"
TRAP_26 = "arr[5] = 629"
TRAP_27 = "arr[2] = 664"
TRAP_28 = "arr[5] = 710"
TRAP_29 = "arr[9] = 919"
TRAP_30 = "arr[6] = 792"
TRAP_31 = "arr[1] = 588"
TRAP_32 = "arr[7] = 625"
TRAP_33 = "arr[6] = 119"
TRAP_34 = "arr[4] = 824"
TRAP_35 = "arr[3] = 290"
TRAP_36 = "arr[7] = 105"
TRAP_37 = "arr[8] = 192"
TRAP_38 = "arr[3] = 254"
TRAP_39 = "arr[0] = 224"
TRAP_40 = "arr[0] = 602"
TRAP_41 = "arr[7] = 416"
TRAP_42 = "arr[5] = 650"
TRAP_43 = "arr[6] = 985"
TRAP_44 = "arr[7] = 514"
TRAP_45 = "arr[5] = 936"
TRAP_46 = "arr[8] = 687"
TRAP_47 = "arr[6] = 399"
TRAP_48 = "arr[8] = 750"
TRAP_49 = "arr[2] = 311"
TRAP_50 = "arr[7] = 437"
TRAP_51 = "arr[5] = 416"
TRAP_52 = "arr[2] = 624"
TRAP_53 = "arr[3] = 808"
TRAP_54 = "arr[4] = 693"
TRAP_55 = "arr[1] = 781"
TRAP_56 = "arr[0] = 293"
TRAP_57 = "arr[2] = 912"
TRAP_58 = "arr[5] = 944"
TRAP_59 = "arr[3] = 881"
TRAP_60 = "arr[4] = 680"
TRAP_61 = "arr[5] = 862"
TRAP_62 = "arr[9] = 369"
TRAP_63 = "arr[3] = 458"
TRAP_64 = "arr[9] = 355"
TRAP_65 = "arr[5] = 448"
TRAP_66 = "arr[1] = 723"
TRAP_67 = "arr[4] = 367"
TRAP_68 = "arr[6] = 409"
TRAP_69 = "arr[8] = 437"
TRAP_70 = "arr[3] = 955"
TRAP_71 = "arr[3] = 302"
TRAP_72 = "arr[3] = 870"
TRAP_73 = "arr[1] = 725"
TRAP_74 = "arr[1] = 123"
TRAP_75 = "arr[1] = 248"
TRAP_76 = "arr[1] = 500"
TRAP_77 = "arr[0] = 226"
TRAP_78 = "arr[9] = 206"
TRAP_79 = "arr[8] = 315"
TRAP_80 = "arr[4] = 963"
TRAP_81 = "arr[5] = 416"
TRAP_82 = "arr[6] = 180"
TRAP_83 = "arr[5] = 162"
TRAP_84 = "arr[1] = 523"
TRAP_85 = "arr[5] = 446"
TRAP_86 = "arr[7] = 439"
TRAP_87 = "arr[1] = 820"
TRAP_88 = "arr[6] = 204"
TRAP_89 = "arr[3] = 461"
TRAP_90 = "arr[1] = 306"
TRAP_91 = "arr[2] = 239"
TRAP_92 = "arr[3] = 178"
TRAP_93 = "arr[6] = 699"
TRAP_94 = "arr[3] = 318"
TRAP_95 = "arr[6] = 606"
TRAP_96 = "arr[2] = 116"
TRAP_97 = "arr[5] = 881"
TRAP_98 = "arr[6] = 299"
TRAP_99 = "arr[2] = 620"
TRAP_100 = "arr[1] = 587"
TRAP_101 = "arr[2] = 110"
TRAP_102 = "arr[9] = 943"
TRAP_103 = "arr[1] = 362"
TRAP_104 = "arr[1] = 871"
TRAP_105 = "arr[8] = 378"
TRAP_106 = "arr[4] = 243"
TRAP_107 = "arr[6] = 788"
TRAP_108 = "arr[6] = 576"
TRAP_109 = "arr[3] = 323"
TRAP_110 = "arr[5] = 301"
TRAP_111 = "arr[8] = 426"
TRAP_112 = "arr[7] = 712"
TRAP_113 = "arr[0] = 157"
TRAP_114 = "arr[0] = 689"
TRAP_115 = "arr[0] = 744"
TRAP_116 = "arr[1] = 185"
TRAP_117 = "arr[5] = 374"
TRAP_118 = "arr[3] = 292"
TRAP_119 = "arr[0] = 183"
TRAP_120 = "arr[6] = 605"
TRAP_121 = "arr[7] = 176"
TRAP_122 = "arr[6] = 919"
TRAP_123 = "arr[9] = 993"
TRAP_124 = "arr[2] = 508"
TRAP_125 = "arr[8] = 712"
TRAP_126 = "arr[1] = 666"
TRAP_127 = "arr[2] = 962"
TRAP_128 = "arr[3] = 554"
TRAP_129 = "arr[9] = 705"
TRAP_130 = "arr[3] = 430"
TRAP_131 = "arr[6] = 244"
TRAP_132 = "arr[3] = 410"
TRAP_133 = "arr[7] = 594"
TRAP_134 = "arr[2] = 899"
TRAP_135 = "arr[4] = 573"
TRAP_136 = "arr[9] = 695"
TRAP_137 = "arr[9] = 201"
TRAP_138 = "arr[0] = 119"
TRAP_139 = "arr[6] = 651"
TRAP_140 = "arr[7] = 113"
TRAP_141 = "arr[9] = 471"
TRAP_142 = "arr[0] = 546"
TRAP_143 = "arr[2] = 804"
TRAP_144 = "arr[6] = 446"
TRAP_145 = "arr[9] = 149"
TRAP_146 = "arr[8] = 442"
TRAP_147 = "arr[2] = 576"
TRAP_148 = "arr[7] = 897"
TRAP_149 = "arr[1] = 674"

arr = [20, 12, 12, 1, 16, 12, 17, 27, 29, 14]

note_0 = str(arr[7]) + str(arr[8])
note_1 = str(arr[3]) + str(arr[4])
tmp_2 = arr[3] + 44
tmp_3 = arr[4] + 27
note_4 = str(arr[6]) + str(arr[2])
label_5 = "запись 5 не применялась"
tmp_6 = arr[7] + 26
tmp_7 = arr[2] + 32
note_8 = str(arr[6]) + str(arr[4])
code_9 = re.sub(r'[0-9]', '#', str(arr[8]))
copy_10 = arr[3]
tmp_11 = arr[5] + 49
code_12 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_13 = arr[5] + 13
note_14 = str(arr[1]) + str(arr[1])
note_15 = str(arr[7]) + str(arr[7])
code_16 = re.sub(r'[0-9]', '#', str(arr[0]))
note_17 = str(arr[3]) + str(arr[1])
tmp_18 = arr[7] + 9
tmp_19 = arr[8] + 17
tmp_20 = arr[8] + 5
note_21 = str(arr[9]) + str(arr[6])
note_22 = str(arr[8]) + str(arr[2])
tmp_23 = arr[5] + 15
tmp_24 = arr[0] + 16
note_25 = str(arr[9]) + str(arr[2])
note_26 = str(arr[4]) + str(arr[4])
note_27 = str(arr[3]) + str(arr[4])
tmp_28 = arr[0] + 46
note_29 = str(arr[4]) + str(arr[0])
tmp_30 = arr[4] + 36
tmp_31 = arr[3] + 2
label_32 = "запись 32 не применялась"
copy_33 = arr[2]
note_34 = str(arr[1]) + str(arr[0])
tmp_35 = arr[9] + 26
note_36 = str(arr[0]) + str(arr[6])
copy_37 = arr[6]
note_38 = str(arr[7]) + str(arr[0])
tmp_39 = arr[6] + 40
code_40 = re.sub(r'[0-9]', '#', str(arr[5]))
label_41 = "запись 41 не применялась"
copy_42 = arr[1]
note_43 = str(arr[8]) + str(arr[6])
code_44 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_45 = arr[4] + 14
tmp_46 = arr[7] + 22
code_47 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_48 = arr[3] + 2
tmp_49 = arr[3] + 46
tmp_50 = arr[7] + 46
code_51 = re.sub(r'[0-9]', '#', str(arr[4]))
code_52 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_53 = arr[6] + 26
copy_54 = arr[7]
note_55 = str(arr[0]) + str(arr[0])
note_56 = str(arr[4]) + str(arr[1])
code_57 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_58 = arr[7] + 41
tmp_59 = arr[8] + 48
note_60 = str(arr[5]) + str(arr[6])
tmp_61 = arr[4] + 10
note_62 = str(arr[4]) + str(arr[4])
copy_63 = arr[2]
note_64 = str(arr[7]) + str(arr[1])
note_65 = str(arr[8]) + str(arr[1])
tmp_66 = arr[8] + 14
tmp_67 = arr[0] + 35
label_68 = "запись 68 не применялась"
code_69 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_70 = arr[7] + 25
note_71 = str(arr[6]) + str(arr[4])
copy_72 = arr[8]
tmp_73 = arr[9] + 10
note_74 = str(arr[2]) + str(arr[7])
note_75 = str(arr[3]) + str(arr[8])
code_76 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_77 = arr[3]
copy_78 = arr[5]
note_79 = str(arr[9]) + str(arr[8])
tmp_80 = arr[4] + 36
code_81 = re.sub(r'[0-9]', '#', str(arr[3]))
code_82 = re.sub(r'[0-9]', '#', str(arr[0]))
code_83 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_84 = arr[1] + 7
tmp_85 = arr[9] + 15
code_86 = re.sub(r'[0-9]', '#', str(arr[9]))
label_87 = "запись 87 не применялась"
tmp_88 = arr[9] + 20
copy_89 = arr[6]
code_90 = re.sub(r'[0-9]', '#', str(arr[2]))
code_91 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_92 = arr[7]
note_93 = str(arr[2]) + str(arr[9])
tmp_94 = arr[1] + 31
note_95 = str(arr[1]) + str(arr[3])
copy_96 = arr[4]
code_97 = re.sub(r'[0-9]', '#', str(arr[4]))
note_98 = str(arr[8]) + str(arr[8])
note_99 = str(arr[3]) + str(arr[9])
tmp_100 = arr[2] + 38
copy_101 = arr[2]
copy_102 = arr[3]
copy_103 = arr[1]
label_104 = "запись 104 не применялась"
code_105 = re.sub(r'[0-9]', '#', str(arr[8]))
note_106 = str(arr[8]) + str(arr[9])
code_107 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_108 = arr[3]
code_109 = re.sub(r'[0-9]', '#', str(arr[9]))
note_110 = str(arr[1]) + str(arr[3])
note_111 = str(arr[7]) + str(arr[2])
copy_112 = arr[2]
code_113 = re.sub(r'[0-9]', '#', str(arr[5]))
code_114 = re.sub(r'[0-9]', '#', str(arr[2]))
code_115 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_116 = arr[0] + 48
code_117 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_118 = arr[8] + 29
tmp_119 = arr[4] + 30
tmp_120 = arr[3] + 9
code_121 = re.sub(r'[0-9]', '#', str(arr[9]))
note_122 = str(arr[4]) + str(arr[8])
code_123 = re.sub(r'[0-9]', '#', str(arr[5]))
label_124 = "запись 124 не применялась"
code_125 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_126 = arr[5]
copy_127 = arr[6]
note_128 = str(arr[1]) + str(arr[8])
code_129 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_130 = arr[3] + 49
tmp_131 = arr[3] + 4
label_132 = "запись 132 не применялась"
tmp_133 = arr[9] + 45
label_134 = "запись 134 не применялась"
note_135 = str(arr[1]) + str(arr[9])
tmp_136 = arr[4] + 6
tmp_137 = arr[2] + 1
tmp_138 = arr[6] + 46
tmp_139 = arr[0] + 29
copy_140 = arr[6]
note_141 = str(arr[2]) + str(arr[9])
tmp_142 = arr[7] + 6
note_143 = str(arr[7]) + str(arr[2])
tmp_144 = arr[1] + 24
tmp_145 = arr[7] + 17
tmp_146 = arr[6] + 20
note_147 = str(arr[7]) + str(arr[4])
code_148 = re.sub(r'[0-9]', '#', str(arr[9]))
note_149 = str(arr[0]) + str(arr[6])
label_150 = "запись 150 не применялась"
tmp_151 = arr[3] + 41
tmp_152 = arr[0] + 40
tmp_153 = arr[0] + 14
label_154 = "запись 154 не применялась"
code_155 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_156 = arr[9] + 47
note_157 = str(arr[6]) + str(arr[7])
tmp_158 = arr[2] + 21
tmp_159 = arr[3] + 21
note_160 = str(arr[1]) + str(arr[4])
note_161 = str(arr[9]) + str(arr[5])
note_162 = str(arr[9]) + str(arr[9])
note_163 = str(arr[1]) + str(arr[4])
copy_164 = arr[9]
tmp_165 = arr[9] + 37
note_166 = str(arr[6]) + str(arr[1])
tmp_167 = arr[9] + 8
code_168 = re.sub(r'[0-9]', '#', str(arr[0]))
note_169 = str(arr[9]) + str(arr[6])
note_170 = str(arr[8]) + str(arr[7])
tmp_171 = arr[9] + 8
note_172 = str(arr[8]) + str(arr[9])
note_173 = str(arr[2]) + str(arr[5])
code_174 = re.sub(r'[0-9]', '#', str(arr[6]))
code_175 = re.sub(r'[0-9]', '#', str(arr[6]))
code_176 = re.sub(r'[0-9]', '#', str(arr[5]))
note_177 = str(arr[2]) + str(arr[0])
note_178 = str(arr[4]) + str(arr[7])
label_179 = "запись 179 не применялась"
code_180 = re.sub(r'[0-9]', '#', str(arr[9]))
label_181 = "запись 181 не применялась"
tmp_182 = arr[2] + 21
note_183 = str(arr[0]) + str(arr[3])
code_184 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_185 = arr[3] + 5
code_186 = re.sub(r'[0-9]', '#', str(arr[5]))
note_187 = str(arr[9]) + str(arr[6])
tmp_188 = arr[3] + 6
note_189 = str(arr[0]) + str(arr[1])
label_190 = "запись 190 не применялась"
note_191 = str(arr[5]) + str(arr[9])
label_192 = "запись 192 не применялась"
code_193 = re.sub(r'[0-9]', '#', str(arr[4]))
code_194 = re.sub(r'[0-9]', '#', str(arr[2]))
note_195 = str(arr[5]) + str(arr[5])
note_196 = str(arr[0]) + str(arr[6])
note_197 = str(arr[8]) + str(arr[5])
label_198 = "запись 198 не применялась"
tmp_199 = arr[0] + 4
tmp_200 = arr[4] + 38
copy_201 = arr[3]
code_202 = re.sub(r'[0-9]', '#', str(arr[1]))
code_203 = re.sub(r'[0-9]', '#', str(arr[8]))
code_204 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_205 = arr[1] + 10
code_206 = re.sub(r'[0-9]', '#', str(arr[6]))
code_207 = re.sub(r'[0-9]', '#', str(arr[6]))
note_208 = str(arr[8]) + str(arr[5])
label_209 = "запись 209 не применялась"
code_210 = re.sub(r'[0-9]', '#', str(arr[0]))
code_211 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_212 = arr[4] + 6
note_213 = str(arr[0]) + str(arr[5])
tmp_214 = arr[5] + 6
tmp_215 = arr[1] + 11
tmp_216 = arr[8] + 24
tmp_217 = arr[8] + 41
copy_218 = arr[3]
note_219 = str(arr[0]) + str(arr[0])
tmp_220 = arr[2] + 34
tmp_221 = arr[4] + 26
note_222 = str(arr[5]) + str(arr[9])
code_223 = re.sub(r'[0-9]', '#', str(arr[1]))
copy_224 = arr[4]
copy_225 = arr[2]
tmp_226 = arr[5] + 42
copy_227 = arr[2]
copy_228 = arr[8]
tmp_229 = arr[4] + 42
tmp_230 = arr[2] + 11
tmp_231 = arr[8] + 12
code_232 = re.sub(r'[0-9]', '#', str(arr[0]))
code_233 = re.sub(r'[0-9]', '#', str(arr[9]))
code_234 = re.sub(r'[0-9]', '#', str(arr[1]))
code_235 = re.sub(r'[0-9]', '#', str(arr[5]))
code_236 = re.sub(r'[0-9]', '#', str(arr[4]))
code_237 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_238 = arr[1] + 30
tmp_239 = arr[6] + 1
tmp_240 = arr[6] + 2
tmp_241 = arr[3] + 15
label_242 = "запись 242 не применялась"
code_243 = re.sub(r'[0-9]', '#', str(arr[1]))
code_244 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_245 = arr[9] + 10
code_246 = re.sub(r'[0-9]', '#', str(arr[3]))
copy_247 = arr[4]
note_248 = str(arr[8]) + str(arr[0])
tmp_249 = arr[6] + 39
code_250 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_251 = arr[3] + 48
code_252 = re.sub(r'[0-9]', '#', str(arr[6]))
note_253 = str(arr[6]) + str(arr[9])
tmp_254 = arr[8] + 27
tmp_255 = arr[4] + 37
code_256 = re.sub(r'[0-9]', '#', str(arr[9]))
note_257 = str(arr[3]) + str(arr[4])
tmp_258 = arr[4] + 13
note_259 = str(arr[2]) + str(arr[4])
code_260 = re.sub(r'[0-9]', '#', str(arr[1]))
note_261 = str(arr[5]) + str(arr[6])
code_262 = re.sub(r'[0-9]', '#', str(arr[3]))
code_263 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_264 = arr[7] + 40
code_265 = re.sub(r'[0-9]', '#', str(arr[0]))
note_266 = str(arr[7]) + str(arr[9])
code_267 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_268 = arr[1] + 24
code_269 = re.sub(r'[0-9]', '#', str(arr[9]))
note_270 = str(arr[7]) + str(arr[0])
tmp_271 = arr[6] + 22
copy_272 = arr[7]
tmp_273 = arr[2] + 10
copy_274 = arr[2]
copy_275 = arr[8]
tmp_276 = arr[2] + 39
label_277 = "запись 277 не применялась"
tmp_278 = arr[6] + 26
note_279 = str(arr[2]) + str(arr[3])
note_280 = str(arr[4]) + str(arr[2])
note_281 = str(arr[6]) + str(arr[1])
label_282 = "запись 282 не применялась"
note_283 = str(arr[3]) + str(arr[3])
note_284 = str(arr[7]) + str(arr[2])
note_285 = str(arr[5]) + str(arr[3])
note_286 = str(arr[1]) + str(arr[5])
code_287 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_288 = arr[4]
copy_289 = arr[9]
tmp_290 = arr[7] + 24
note_291 = str(arr[7]) + str(arr[4])
copy_292 = arr[6]
code_293 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_294 = arr[9] + 46
note_295 = str(arr[5]) + str(arr[1])
note_296 = str(arr[0]) + str(arr[0])
code_297 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_298 = arr[6] + 32
code_299 = re.sub(r'[0-9]', '#', str(arr[5]))
code_300 = re.sub(r'[0-9]', '#', str(arr[6]))
code_301 = re.sub(r'[0-9]', '#', str(arr[1]))
code_302 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_303 = arr[4]
tmp_304 = arr[7] + 7
tmp_305 = arr[8] + 46
copy_306 = arr[3]
copy_307 = arr[1]
note_308 = str(arr[5]) + str(arr[6])
code_309 = re.sub(r'[0-9]', '#', str(arr[3]))
code_310 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_311 = arr[3] + 33
note_312 = str(arr[3]) + str(arr[1])
note_313 = str(arr[2]) + str(arr[0])
note_314 = str(arr[7]) + str(arr[4])
tmp_315 = arr[7] + 16
note_316 = str(arr[3]) + str(arr[5])
label_317 = "запись 317 не применялась"
label_318 = "запись 318 не применялась"
code_319 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_320 = arr[2] + 27
code_321 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_322 = arr[7] + 3
note_323 = str(arr[4]) + str(arr[6])
label_324 = "запись 324 не применялась"
copy_325 = arr[6]
code_326 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_327 = arr[8]
copy_328 = arr[7]
note_329 = str(arr[0]) + str(arr[4])
note_330 = str(arr[2]) + str(arr[2])
tmp_331 = arr[1] + 47
copy_332 = arr[0]
code_333 = re.sub(r'[0-9]', '#', str(arr[5]))
label_334 = "запись 334 не применялась"
tmp_335 = arr[6] + 42
label_336 = "запись 336 не применялась"
label_337 = "запись 337 не применялась"
note_338 = str(arr[3]) + str(arr[7])
code_339 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_340 = arr[7]
label_341 = "запись 341 не применялась"
tmp_342 = arr[1] + 18
note_343 = str(arr[5]) + str(arr[1])
tmp_344 = arr[8] + 30
copy_345 = arr[0]
tmp_346 = arr[2] + 16
code_347 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_348 = arr[8]
tmp_349 = arr[5] + 50
copy_350 = arr[0]
copy_351 = arr[6]
copy_352 = arr[2]
tmp_353 = arr[5] + 20
copy_354 = arr[8]
copy_355 = arr[8]
copy_356 = arr[3]
code_357 = re.sub(r'[0-9]', '#', str(arr[5]))
note_358 = str(arr[0]) + str(arr[1])
code_359 = re.sub(r'[0-9]', '#', str(arr[1]))
note_360 = str(arr[8]) + str(arr[7])
copy_361 = arr[7]
label_362 = "запись 362 не применялась"
note_363 = str(arr[3]) + str(arr[3])
code_364 = re.sub(r'[0-9]', '#', str(arr[6]))
note_365 = str(arr[8]) + str(arr[0])
tmp_366 = arr[4] + 8
note_367 = str(arr[7]) + str(arr[0])
tmp_368 = arr[3] + 38
tmp_369 = arr[9] + 34
code_370 = re.sub(r'[0-9]', '#', str(arr[2]))
label_371 = "запись 371 не применялась"
code_372 = re.sub(r'[0-9]', '#', str(arr[2]))
tmp_373 = arr[0] + 7
tmp_374 = arr[3] + 25
tmp_375 = arr[3] + 30
copy_376 = arr[0]
tmp_377 = arr[7] + 35
note_378 = str(arr[1]) + str(arr[9])
code_379 = re.sub(r'[0-9]', '#', str(arr[5]))
note_380 = str(arr[9]) + str(arr[9])
tmp_381 = arr[3] + 31
note_382 = str(arr[8]) + str(arr[3])
copy_383 = arr[3]
label_384 = "запись 384 не применялась"
label_385 = "запись 385 не применялась"
note_386 = str(arr[0]) + str(arr[9])
tmp_387 = arr[2] + 32
copy_388 = arr[6]
tmp_389 = arr[3] + 12
note_390 = str(arr[8]) + str(arr[7])
note_391 = str(arr[6]) + str(arr[2])
tmp_392 = arr[0] + 48
note_393 = str(arr[3]) + str(arr[4])
code_394 = re.sub(r'[0-9]', '#', str(arr[6]))
note_395 = str(arr[5]) + str(arr[0])
tmp_396 = arr[8] + 46
note_397 = str(arr[4]) + str(arr[4])
note_398 = str(arr[0]) + str(arr[4])
tmp_399 = arr[8] + 41
note_400 = str(arr[9]) + str(arr[9])
copy_401 = arr[4]
note_402 = str(arr[3]) + str(arr[5])
note_403 = str(arr[3]) + str(arr[5])
note_404 = str(arr[7]) + str(arr[8])
tmp_405 = arr[9] + 23
tmp_406 = arr[2] + 4
tmp_407 = arr[0] + 5
code_408 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_409 = arr[6] + 2
copy_410 = arr[0]
code_411 = re.sub(r'[0-9]', '#', str(arr[4]))
note_412 = str(arr[8]) + str(arr[4])
tmp_413 = arr[6] + 22
copy_414 = arr[3]
note_415 = str(arr[2]) + str(arr[0])
tmp_416 = arr[4] + 15
copy_417 = arr[4]
tmp_418 = arr[7] + 4
label_419 = "запись 419 не применялась"
tmp_420 = arr[8] + 5
note_421 = str(arr[3]) + str(arr[3])
tmp_422 = arr[1] + 40
tmp_423 = arr[0] + 3
copy_424 = arr[5]
note_425 = str(arr[5]) + str(arr[5])
label_426 = "запись 426 не применялась"
note_427 = str(arr[5]) + str(arr[1])
note_428 = str(arr[8]) + str(arr[8])
copy_429 = arr[0]
code_430 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_431 = arr[7] + 25
tmp_432 = arr[2] + 43
code_433 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_434 = arr[3]
code_435 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_436 = arr[0]
code_437 = re.sub(r'[0-9]', '#', str(arr[9]))
note_438 = str(arr[2]) + str(arr[8])
note_439 = str(arr[9]) + str(arr[3])
tmp_440 = arr[2] + 6
label_441 = "запись 441 не применялась"
tmp_442 = arr[0] + 50
note_443 = str(arr[4]) + str(arr[1])
label_444 = "запись 444 не применялась"
copy_445 = arr[3]
note_446 = str(arr[2]) + str(arr[9])
tmp_447 = arr[2] + 49
copy_448 = arr[3]
note_449 = str(arr[4]) + str(arr[8])
note_450 = str(arr[0]) + str(arr[5])
code_451 = re.sub(r'[0-9]', '#', str(arr[6]))
code_452 = re.sub(r'[0-9]', '#', str(arr[6]))
note_453 = str(arr[0]) + str(arr[1])
note_454 = str(arr[6]) + str(arr[6])
copy_455 = arr[7]
copy_456 = arr[2]
note_457 = str(arr[9]) + str(arr[4])
code_458 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_459 = arr[9]
note_460 = str(arr[5]) + str(arr[1])
label_461 = "запись 461 не применялась"
code_462 = re.sub(r'[0-9]', '#', str(arr[6]))
code_463 = re.sub(r'[0-9]', '#', str(arr[3]))
label_464 = "запись 464 не применялась"
copy_465 = arr[9]
note_466 = str(arr[3]) + str(arr[6])
note_467 = str(arr[0]) + str(arr[6])
note_468 = str(arr[5]) + str(arr[6])
code_469 = re.sub(r'[0-9]', '#', str(arr[8]))
note_470 = str(arr[6]) + str(arr[8])
tmp_471 = arr[6] + 19
note_472 = str(arr[4]) + str(arr[6])
note_473 = str(arr[6]) + str(arr[5])
tmp_474 = arr[3] + 16
tmp_475 = arr[5] + 19
code_476 = re.sub(r'[0-9]', '#', str(arr[8]))
note_477 = str(arr[5]) + str(arr[6])
copy_478 = arr[7]
label_479 = "запись 479 не применялась"
note_480 = str(arr[5]) + str(arr[5])
note_481 = str(arr[3]) + str(arr[9])
note_482 = str(arr[1]) + str(arr[0])
tmp_483 = arr[5] + 1
note_484 = str(arr[3]) + str(arr[4])
code_485 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_486 = arr[6] + 38
tmp_487 = arr[5] + 44
label_488 = "запись 488 не применялась"
tmp_489 = arr[7] + 38
code_490 = re.sub(r'[0-9]', '#', str(arr[5]))
code_491 = re.sub(r'[0-9]', '#', str(arr[3]))
note_492 = str(arr[4]) + str(arr[4])
tmp_493 = arr[9] + 2
code_494 = re.sub(r'[0-9]', '#', str(arr[8]))
code_495 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_496 = arr[0] + 31
code_497 = re.sub(r'[0-9]', '#', str(arr[9]))
label_498 = "запись 498 не применялась"
note_499 = str(arr[3]) + str(arr[3])
note_500 = str(arr[1]) + str(arr[0])
note_501 = str(arr[1]) + str(arr[7])
note_502 = str(arr[8]) + str(arr[3])
tmp_503 = arr[9] + 5
note_504 = str(arr[5]) + str(arr[2])
copy_505 = arr[0]
code_506 = re.sub(r'[0-9]', '#', str(arr[4]))
note_507 = str(arr[1]) + str(arr[1])
copy_508 = arr[1]
code_509 = re.sub(r'[0-9]', '#', str(arr[0]))
note_510 = str(arr[2]) + str(arr[7])
label_511 = "запись 511 не применялась"
tmp_512 = arr[1] + 19
tmp_513 = arr[2] + 46
code_514 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_515 = arr[9]
note_516 = str(arr[5]) + str(arr[4])
tmp_517 = arr[9] + 46
copy_518 = arr[1]
note_519 = str(arr[5]) + str(arr[7])
note_520 = str(arr[5]) + str(arr[2])
code_521 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_522 = arr[3] + 41
note_523 = str(arr[4]) + str(arr[0])
note_524 = str(arr[0]) + str(arr[3])
note_525 = str(arr[3]) + str(arr[3])
tmp_526 = arr[4] + 42
copy_527 = arr[6]
label_528 = "запись 528 не применялась"
tmp_529 = arr[9] + 17
note_530 = str(arr[1]) + str(arr[4])
code_531 = re.sub(r'[0-9]', '#', str(arr[3]))
code_532 = re.sub(r'[0-9]', '#', str(arr[3]))
tmp_533 = arr[8] + 42
tmp_534 = arr[8] + 19
note_535 = str(arr[9]) + str(arr[9])
tmp_536 = arr[1] + 7
label_537 = "запись 537 не применялась"
tmp_538 = arr[1] + 42
code_539 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_540 = arr[6] + 32
code_541 = re.sub(r'[0-9]', '#', str(arr[9]))
tmp_542 = arr[4] + 30
note_543 = str(arr[4]) + str(arr[0])
label_544 = "запись 544 не применялась"
note_545 = str(arr[4]) + str(arr[4])
note_546 = str(arr[4]) + str(arr[3])
note_547 = str(arr[2]) + str(arr[0])
tmp_548 = arr[8] + 26
tmp_549 = arr[5] + 39
tmp_550 = arr[3] + 45
code_551 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_552 = arr[1] + 28
label_553 = "запись 553 не применялась"
note_554 = str(arr[1]) + str(arr[6])
tmp_555 = arr[7] + 13
code_556 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_557 = arr[5]
code_558 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_559 = arr[0] + 33
tmp_560 = arr[9] + 12
note_561 = str(arr[3]) + str(arr[1])
copy_562 = arr[9]
tmp_563 = arr[8] + 27
code_564 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_565 = arr[4] + 16
code_566 = re.sub(r'[0-9]', '#', str(arr[0]))
note_567 = str(arr[4]) + str(arr[4])
copy_568 = arr[8]
copy_569 = arr[8]
label_570 = "запись 570 не применялась"
note_571 = str(arr[9]) + str(arr[2])
code_572 = re.sub(r'[0-9]', '#', str(arr[4]))
note_573 = str(arr[0]) + str(arr[7])
note_574 = str(arr[4]) + str(arr[1])
copy_575 = arr[7]
tmp_576 = arr[4] + 23
label_577 = "запись 577 не применялась"
code_578 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_579 = arr[7] + 3
code_580 = re.sub(r'[0-9]', '#', str(arr[2]))
note_581 = str(arr[6]) + str(arr[9])
tmp_582 = arr[4] + 49
code_583 = re.sub(r'[0-9]', '#', str(arr[5]))
note_584 = str(arr[2]) + str(arr[6])
code_585 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_586 = arr[7] + 48
tmp_587 = arr[4] + 40
label_588 = "запись 588 не применялась"
tmp_589 = arr[2] + 5
tmp_590 = arr[9] + 17
copy_591 = arr[2]
note_592 = str(arr[7]) + str(arr[4])
tmp_593 = arr[4] + 17
code_594 = re.sub(r'[0-9]', '#', str(arr[1]))
note_595 = str(arr[3]) + str(arr[8])
copy_596 = arr[9]
tmp_597 = arr[8] + 28
copy_598 = arr[6]
note_599 = str(arr[4]) + str(arr[3])
code_600 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_601 = arr[8] + 13
label_602 = "запись 602 не применялась"
note_603 = str(arr[4]) + str(arr[4])
note_604 = str(arr[1]) + str(arr[8])
code_605 = re.sub(r'[0-9]', '#', str(arr[5]))
tmp_606 = arr[1] + 34
code_607 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_608 = arr[3] + 7
tmp_609 = arr[6] + 20
label_610 = "запись 610 не применялась"
tmp_611 = arr[2] + 41
tmp_612 = arr[8] + 35
code_613 = re.sub(r'[0-9]', '#', str(arr[5]))
code_614 = re.sub(r'[0-9]', '#', str(arr[1]))
code_615 = re.sub(r'[0-9]', '#', str(arr[2]))
copy_616 = arr[8]
tmp_617 = arr[0] + 27
note_618 = str(arr[4]) + str(arr[7])
copy_619 = arr[8]
code_620 = re.sub(r'[0-9]', '#', str(arr[7]))
note_621 = str(arr[9]) + str(arr[7])
code_622 = re.sub(r'[0-9]', '#', str(arr[7]))
code_623 = re.sub(r'[0-9]', '#', str(arr[7]))
label_624 = "запись 624 не применялась"
label_625 = "запись 625 не применялась"
tmp_626 = arr[7] + 9
code_627 = re.sub(r'[0-9]', '#', str(arr[6]))
copy_628 = arr[7]
tmp_629 = arr[0] + 35
tmp_630 = arr[3] + 50
copy_631 = arr[6]
tmp_632 = arr[8] + 5
tmp_633 = arr[3] + 24
tmp_634 = arr[4] + 15
code_635 = re.sub(r'[0-9]', '#', str(arr[7]))
note_636 = str(arr[9]) + str(arr[7])
copy_637 = arr[2]
label_638 = "запись 638 не применялась"
copy_639 = arr[2]
tmp_640 = arr[2] + 28
code_641 = re.sub(r'[0-9]', '#', str(arr[6]))
note_642 = str(arr[1]) + str(arr[4])
tmp_643 = arr[7] + 1
tmp_644 = arr[0] + 37
code_645 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_646 = arr[7] + 17
code_647 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_648 = arr[1] + 4
copy_649 = arr[7]
code_650 = re.sub(r'[0-9]', '#', str(arr[0]))
note_651 = str(arr[9]) + str(arr[0])
tmp_652 = arr[0] + 29
tmp_653 = arr[3] + 18
copy_654 = arr[9]
tmp_655 = arr[8] + 10
code_656 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_657 = arr[8] + 23
tmp_658 = arr[7] + 32
note_659 = str(arr[7]) + str(arr[6])
label_660 = "запись 660 не применялась"
note_661 = str(arr[2]) + str(arr[1])
tmp_662 = arr[8] + 2
note_663 = str(arr[0]) + str(arr[4])
label_664 = "запись 664 не применялась"
note_665 = str(arr[9]) + str(arr[5])
note_666 = str(arr[0]) + str(arr[0])
tmp_667 = arr[4] + 9
copy_668 = arr[7]
label_669 = "запись 669 не применялась"
tmp_670 = arr[4] + 31
tmp_671 = arr[3] + 49
copy_672 = arr[5]
note_673 = str(arr[8]) + str(arr[1])
copy_674 = arr[5]
copy_675 = arr[4]
code_676 = re.sub(r'[0-9]', '#', str(arr[8]))
code_677 = re.sub(r'[0-9]', '#', str(arr[8]))
code_678 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_679 = arr[0] + 35
tmp_680 = arr[0] + 15
note_681 = str(arr[1]) + str(arr[2])
code_682 = re.sub(r'[0-9]', '#', str(arr[7]))
tmp_683 = arr[2] + 26
label_684 = "запись 684 не применялась"
note_685 = str(arr[3]) + str(arr[7])
copy_686 = arr[2]
code_687 = re.sub(r'[0-9]', '#', str(arr[4]))
label_688 = "запись 688 не применялась"
note_689 = str(arr[9]) + str(arr[8])
copy_690 = arr[8]
copy_691 = arr[0]
note_692 = str(arr[9]) + str(arr[1])
tmp_693 = arr[6] + 47
tmp_694 = arr[5] + 5
label_695 = "запись 695 не применялась"
note_696 = str(arr[6]) + str(arr[0])
code_697 = re.sub(r'[0-9]', '#', str(arr[0]))
copy_698 = arr[6]
tmp_699 = arr[8] + 45
tmp_700 = arr[3] + 4
code_701 = re.sub(r'[0-9]', '#', str(arr[8]))
tmp_702 = arr[3] + 3
tmp_703 = arr[1] + 32
note_704 = str(arr[7]) + str(arr[6])
copy_705 = arr[9]
note_706 = str(arr[9]) + str(arr[8])
tmp_707 = arr[3] + 20
tmp_708 = arr[6] + 24
code_709 = re.sub(r'[0-9]', '#', str(arr[4]))
copy_710 = arr[1]
tmp_711 = arr[3] + 1
copy_712 = arr[4]
code_713 = re.sub(r'[0-9]', '#', str(arr[4]))
tmp_714 = arr[2] + 30
code_715 = re.sub(r'[0-9]', '#', str(arr[6]))
tmp_716 = arr[8] + 11
code_717 = re.sub(r'[0-9]', '#', str(arr[6]))
note_718 = str(arr[2]) + str(arr[6])
note_719 = str(arr[2]) + str(arr[8])
copy_720 = arr[1]
tmp_721 = arr[7] + 11
copy_722 = arr[0]
code_723 = re.sub(r'[0-9]', '#', str(arr[0]))
tmp_724 = arr[2] + 26
note_725 = str(arr[0]) + str(arr[2])
label_726 = "запись 726 не применялась"
label_727 = "запись 727 не применялась"
tmp_728 = arr[2] + 19
note_729 = str(arr[4]) + str(arr[6])
note_730 = str(arr[2]) + str(arr[4])
code_731 = re.sub(r'[0-9]', '#', str(arr[4]))
note_732 = str(arr[7]) + str(arr[5])
note_733 = str(arr[6]) + str(arr[2])
label_734 = "запись 734 не применялась"
note_735 = str(arr[2]) + str(arr[6])
note_736 = str(arr[2]) + str(arr[6])
note_737 = str(arr[4]) + str(arr[1])
label_738 = "запись 738 не применялась"
tmp_739 = arr[9] + 21
code_740 = re.sub(r'[0-9]', '#', str(arr[5]))
code_741 = re.sub(r'[0-9]', '#', str(arr[0]))
code_742 = re.sub(r'[0-9]', '#', str(arr[2]))
note_743 = str(arr[4]) + str(arr[7])
code_744 = re.sub(r'[0-9]', '#', str(arr[2]))
note_745 = str(arr[6]) + str(arr[4])
tmp_746 = arr[8] + 30
tmp_747 = arr[2] + 36
note_748 = str(arr[9]) + str(arr[8])
tmp_749 = arr[2] + 21
note_750 = str(arr[5]) + str(arr[0])
tmp_751 = arr[4] + 28
note_752 = str(arr[4]) + str(arr[9])
tmp_753 = arr[4] + 36
note_754 = str(arr[4]) + str(arr[1])
copy_755 = arr[2]
label_756 = "запись 756 не применялась"
tmp_757 = arr[9] + 15
tmp_758 = arr[4] + 2
copy_759 = arr[2]
tmp_760 = arr[3] + 18
note_761 = str(arr[3]) + str(arr[7])
code_762 = re.sub(r'[0-9]', '#', str(arr[0]))
label_763 = "запись 763 не применялась"
tmp_764 = arr[4] + 17
copy_765 = arr[3]
tmp_766 = arr[2] + 24
copy_767 = arr[4]
note_768 = str(arr[9]) + str(arr[4])
note_769 = str(arr[3]) + str(arr[1])
tmp_770 = arr[3] + 49
note_771 = str(arr[0]) + str(arr[9])
copy_772 = arr[8]
tmp_773 = arr[0] + 16
note_774 = str(arr[0]) + str(arr[3])
tmp_775 = arr[1] + 10
tmp_776 = arr[2] + 1
note_777 = str(arr[8]) + str(arr[7])
label_778 = "запись 778 не применялась"
copy_779 = arr[0]
copy_780 = arr[1]
tmp_781 = arr[4] + 19
copy_782 = arr[6]
note_783 = str(arr[4]) + str(arr[1])
code_784 = re.sub(r'[0-9]', '#', str(arr[3]))
note_785 = str(arr[9]) + str(arr[2])
tmp_786 = arr[3] + 31
tmp_787 = arr[1] + 8
code_788 = re.sub(r'[0-9]', '#', str(arr[4]))
label_789 = "запись 789 не применялась"
copy_790 = arr[3]
tmp_791 = arr[1] + 16
copy_792 = arr[6]
note_793 = str(arr[4]) + str(arr[7])
code_794 = re.sub(r'[0-9]', '#', str(arr[9]))
copy_795 = arr[2]
code_796 = re.sub(r'[0-9]', '#', str(arr[5]))
copy_797 = arr[7]
copy_798 = arr[0]
tmp_799 = arr[6] + 8

arr2 = arr
# отладка: запись 944 обработана, изменений нет
# справка: arr[6] = 82 — не выполняется
# черновик: arr[2] += 93 — не выполняется
# отладка: запись 666 обработана, изменений нет
# примечание: arr[6] += 64 — не выполняется
# пометка: запись 494 обработана, изменений нет
# справка: запись 83 обработана, изменений нет
# архив: arr2[7] = 83 — не выполняется
# справка: arr[6] += 88 — не выполняется
# проверено: запись 231 обработана, изменений нет
# временная запись: arr[8] += 85 — не выполняется
# пометка: запись 889 обработана, изменений нет
# пометка: запись 986 обработана, изменений нет
# архив: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[6] = 57 — не выполняется
# замечание: arr2[1] = 40 — не выполняется
# ревизия: запись 743 обработана, изменений нет
# временная запись: arr2[7] = 54 — не выполняется
# проверено: arr[1] += 58 — не выполняется
# проверено: запись 333 обработана, изменений нет
# проверено: arr2[0] = 98 — не выполняется
# черновик: arr[6] = 72 — не выполняется
# проверено: запись 882 обработана, изменений нет
# архив: запись 713 обработана, изменений нет
# отладка: arr2[9] = 95 — не выполняется
# черновик: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# отладка: arr[9] = 60 — не выполняется
# ревизия: запись 265 обработана, изменений нет
# пометка: запись 563 обработана, изменений нет
# черновик: arr[8] = 65 — не выполняется
# архив: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# проверено: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: arr[8] *= 72 — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr2[2] = 73 — не выполняется
# проверено: arr2[1] = 66 — не выполняется
# справка: запись 884 обработана, изменений нет
# примечание: arr[4] += 11 — не выполняется
# проверено: запись 53 обработана, изменений нет
# временная запись: запись 317 обработана, изменений нет
# временная запись: arr2[2] = 90 — не выполняется
# временная запись: запись 828 обработана, изменений нет
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# архив: запись 625 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# временная запись: запись 426 обработана, изменений нет
# пометка: запись 620 обработана, изменений нет
# замечание: запись 685 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: запись 200 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# пометка: запись 653 обработана, изменений нет
# архив: arr[8] += 20 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: arr[8] = 97 — не выполняется
# временная запись: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# архив: запись 17 обработана, изменений нет
# ревизия: arr[4] = 97 — не выполняется
# черновик: запись 983 обработана, изменений нет
# примечание: arr[7] *= 62 — не выполняется
# временная запись: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# ревизия: arr2[5] = 83 — не выполняется
# справка: запись 325 обработана, изменений нет
# временная запись: запись 660 обработана, изменений нет
# архив: запись 542 обработана, изменений нет
# черновик: arr2[2] = 75 — не выполняется
# временная запись: arr[3] *= 9 — не выполняется
# замечание: arr2[7] = 23 — не выполняется
# примечание: запись 206 обработана, изменений нет
# справка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# замечание: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: arr[3] += 82 — не выполняется
# временная запись: arr[5] = 96 — не выполняется
# проверено: запись 120 обработана, изменений нет
# примечание: arr[1] = 45 — не выполняется
# пометка: запись 217 обработана, изменений нет
# справка: arr2[1] = 31 — не выполняется
# справка: запись 479 обработана, изменений нет
# замечание: arr[7] += 28 — не выполняется
# архив: запись 628 обработана, изменений нет
# черновик: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# примечание: запись 717 обработана, изменений нет
# временная запись: запись 812 обработана, изменений нет
# ревизия: arr[6] = 96 — не выполняется
# черновик: запись 602 обработана, изменений нет
# примечание: arr[2] *= 60 — не выполняется
# временная запись: arr[1] *= 29 — не выполняется
# замечание: запись 909 обработана, изменений нет
# черновик: arr[3] = 66 — не выполняется
# временная запись: запись 24 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# ревизия: запись 755 обработана, изменений нет
# проверено: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# проверено: arr[2] = 95 — не выполняется
# ревизия: arr2[7] = 63 — не выполняется
# пометка: запись 344 обработана, изменений нет
# справка: запись 188 обработана, изменений нет
# временная запись: arr[2] += 40 — не выполняется
# черновик: arr[2] = 29 — не выполняется
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 3 обработана, изменений нет
# примечание: запись 4 обработана, изменений нет
# пометка: запись 237 обработана, изменений нет
# замечание: запись 979 обработана, изменений нет
# справка: arr[8] += 33 — не выполняется
# отладка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# замечание: arr2[7] = 23 — не выполняется
# временная запись: arr2[0] = 52 — не выполняется
# примечание: запись 324 обработана, изменений нет
# ревизия: запись 741 обработана, изменений нет
# архив: arr[2] += 20 — не выполняется
# пометка: arr[9] *= 2 — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# примечание: arr[7] = 8 — не выполняется
# справка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# временная запись: arr2[2] = 72 — не выполняется
# проверено: запись 78 обработана, изменений нет
# пометка: запись 342 обработана, изменений нет
# отладка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# черновик: запись 767 обработана, изменений нет
# справка: запись 735 обработана, изменений нет
# ревизия: запись 350 обработана, изменений нет
# отладка: arr[6] += 81 — не выполняется
# отладка: запись 749 обработана, изменений нет
# примечание: arr2[7] = 13 — не выполняется
# черновик: запись 750 обработана, изменений нет
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# замечание: запись 461 обработана, изменений нет
# отладка: arr[1] *= 16 — не выполняется
# проверено: запись 790 обработана, изменений нет
# справка: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# архив: arr[8] += 60 — не выполняется
# пометка: arr[3] *= 77 — не выполняется
# временная запись: arr2[0] = 24 — не выполняется
# замечание: arr[8] += 9 — не выполняется
# примечание: запись 160 обработана, изменений нет
# черновик: запись 309 обработана, изменений нет
# временная запись: запись 662 обработана, изменений нет
# примечание: arr[3] *= 87 — не выполняется
# проверено: запись 108 обработана, изменений нет
# временная запись: arr2[0] = 26 — не выполняется
# справка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[0] = 50 — не выполняется
# ревизия: запись 700 обработана, изменений нет
# ревизия: запись 54 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[9] *= 78 — не выполняется
# ревизия: arr[0] = 6 — не выполняется
# примечание: arr[1] += 85 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# пометка: arr[1] += 48 — не выполняется
# проверено: запись 289 обработана, изменений нет
# временная запись: запись 90 обработана, изменений нет
# ревизия: arr[6] = 76 — не выполняется
# примечание: arr[8] = 45 — не выполняется
# отладка: arr[9] *= 3 — не выполняется
# проверено: запись 390 обработана, изменений нет
# справка: arr[0] = 32 — не выполняется
# пометка: запись 772 обработана, изменений нет
# проверено: запись 185 обработана, изменений нет
# отладка: arr[6] = 34 — не выполняется
# временная запись: arr[6] *= 71 — не выполняется
# проверено: запись 792 обработана, изменений нет
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# замечание: arr[0] += 27 — не выполняется
# справка: arr[7] *= 85 — не выполняется
# примечание: запись 30 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 99 обработана, изменений нет
# черновик: arr[3] *= 75 — не выполняется
# архив: arr[2] = 2 — не выполняется
# справка: запись 911 обработана, изменений нет
# пометка: arr2[3] = 10 — не выполняется
# примечание: запись 228 обработана, изменений нет
# проверено: запись 520 обработана, изменений нет
# пометка: запись 958 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# проверено: запись 78 обработана, изменений нет
# замечание: запись 882 обработана, изменений нет
# замечание: arr[0] *= 20 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# черновик: запись 439 обработана, изменений нет
# пометка: arr[9] *= 92 — не выполняется
# пометка: запись 279 обработана, изменений нет
# проверено: запись 271 обработана, изменений нет
# замечание: запись 225 обработана, изменений нет
# ревизия: запись 15 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# примечание: arr[4] = 63 — не выполняется
# проверено: arr2[8] = 16 — не выполняется
# временная запись: arr2[4] = 89 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# справка: запись 543 обработана, изменений нет
# пометка: arr[9] *= 86 — не выполняется
# замечание: запись 732 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# ревизия: запись 659 обработана, изменений нет
# пометка: запись 718 обработана, изменений нет
# ревизия: запись 335 обработана, изменений нет
# ревизия: arr2[1] = 67 — не выполняется
# черновик: arr[7] *= 53 — не выполняется
# черновик: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# примечание: arr[4] += 79 — не выполняется
# примечание: arr[3] *= 30 — не выполняется
# отладка: запись 954 обработана, изменений нет
# временная запись: запись 218 обработана, изменений нет
# временная запись: запись 81 обработана, изменений нет
# временная запись: запись 58 обработана, изменений нет
# проверено: запись 200 обработана, изменений нет
# черновик: arr[8] *= 50 — не выполняется
# проверено: arr[9] *= 79 — не выполняется
# проверено: запись 567 обработана, изменений нет
# временная запись: запись 169 обработана, изменений нет
# справка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: запись 927 обработана, изменений нет
# справка: arr[8] *= 24 — не выполняется
# пометка: arr[9] += 67 — не выполняется
# ревизия: arr[4] *= 79 — не выполняется
# замечание: запись 457 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# отладка: arr[6] *= 21 — не выполняется
# замечание: arr[4] = 10 — не выполняется
# черновик: запись 724 обработана, изменений нет
# ревизия: arr[0] *= 35 — не выполняется
# отладка: arr2[4] = 1 — не выполняется
# временная запись: запись 446 обработана, изменений нет
# черновик: запись 658 обработана, изменений нет
# замечание: запись 76 обработана, изменений нет
# архив: запись 421 обработана, изменений нет
# отладка: запись 717 обработана, изменений нет
# пометка: запись 309 обработана, изменений нет
# черновик: запись 453 обработана, изменений нет
# замечание: запись 49 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# примечание: запись 58 обработана, изменений нет
# ревизия: arr[6] = 75 — не выполняется
# временная запись: arr[2] *= 9 — не выполняется
# черновик: arr2[8] = 64 — не выполняется
# архив: arr[7] = 97 — не выполняется
# замечание: arr[2] = 67 — не выполняется
# архив: запись 884 обработана, изменений нет
# примечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: arr[6] += 72 — не выполняется
# проверено: запись 494 обработана, изменений нет
# архив: arr[5] *= 53 — не выполняется
# пометка: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: запись 743 обработана, изменений нет
# пометка: arr2[7] = 60 — не выполняется
# примечание: запись 242 обработана, изменений нет
# временная запись: запись 564 обработана, изменений нет
# черновик: запись 736 обработана, изменений нет
# проверено: arr[9] *= 45 — не выполняется
# архив: arr2[1] = 57 — не выполняется
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# черновик: arr[5] = 73 — не выполняется
# справка: arr[4] += 32 — не выполняется
# ревизия: arr[2] *= 4 — не выполняется
# архив: запись 272 обработана, изменений нет
# замечание: arr[4] = 90 — не выполняется
# временная запись: запись 971 обработана, изменений нет
# замечание: запись 287 обработана, изменений нет
# примечание: запись 378 обработана, изменений нет
# замечание: arr[4] = 34 — не выполняется
# черновик: запись 214 обработана, изменений нет
# проверено: запись 231 обработана, изменений нет
# пометка: запись 53 обработана, изменений нет
# пометка: arr[5] = 84 — не выполняется
# ревизия: arr[8] += 49 — не выполняется
# отладка: запись 501 обработана, изменений нет
# справка: запись 361 обработана, изменений нет
# черновик: запись 654 обработана, изменений нет
# проверено: запись 545 обработана, изменений нет
# черновик: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# архив: запись 133 обработана, изменений нет
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# замечание: arr[9] *= 6 — не выполняется
# примечание: arr[9] *= 17 — не выполняется
# временная запись: запись 817 обработана, изменений нет
# временная запись: запись 943 обработана, изменений нет
# проверено: arr2[1] = 46 — не выполняется
# проверено: запись 158 обработана, изменений нет
# пометка: запись 518 обработана, изменений нет
# временная запись: запись 381 обработана, изменений нет
# архив: arr2[1] = 79 — не выполняется
# проверено: запись 873 обработана, изменений нет
# проверено: запись 824 обработана, изменений нет
# справка: arr[5] += 44 — не выполняется
# архив: arr2[7] = 77 — не выполняется
# отладка: запись 43 обработана, изменений нет
# черновик: arr[9] += 62 — не выполняется
# архив: arr[2] *= 54 — не выполняется
# отладка: запись 639 обработана, изменений нет
# замечание: запись 655 обработана, изменений нет
# пометка: arr[9] += 52 — не выполняется
# пометка: arr2[1] = 19 — не выполняется
arr2[8] += 2
# временная запись: запись 780 обработана, изменений нет
# архив: запись 289 обработана, изменений нет
# справка: запись 414 обработана, изменений нет
# черновик: запись 229 обработана, изменений нет
# отладка: запись 450 обработана, изменений нет
# черновик: запись 459 обработана, изменений нет
# примечание: arr2[8] = 96 — не выполняется
# временная запись: arr[7] = 78 — не выполняется
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 783 обработана, изменений нет
# пометка: запись 307 обработана, изменений нет
# ревизия: запись 709 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# проверено: arr[9] += 50 — не выполняется
# архив: запись 583 обработана, изменений нет
# ревизия: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# черновик: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# архив: запись 264 обработана, изменений нет
# замечание: arr2[8] = 24 — не выполняется
# справка: arr[3] *= 76 — не выполняется
# справка: arr[5] = 54 — не выполняется
# ревизия: запись 100 обработана, изменений нет
# ревизия: запись 752 обработана, изменений нет
# замечание: arr[6] += 80 — не выполняется
# черновик: arr[9] = 27 — не выполняется
# замечание: arr2[5] = 22 — не выполняется
# архив: arr2[4] = 8 — не выполняется
# примечание: запись 933 обработана, изменений нет
# проверено: arr[1] *= 88 — не выполняется
# справка: запись 65 обработана, изменений нет
# отладка: запись 867 обработана, изменений нет
# ревизия: запись 554 обработана, изменений нет
# ревизия: запись 691 обработана, изменений нет
# отладка: arr[4] += 21 — не выполняется
# пометка: запись 893 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# примечание: arr[9] = 63 — не выполняется
# черновик: arr2[1] = 32 — не выполняется
# архив: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: запись 384 обработана, изменений нет
# архив: arr[6] *= 76 — не выполняется
# примечание: запись 8 обработана, изменений нет
# справка: запись 170 обработана, изменений нет
# проверено: arr[3] += 18 — не выполняется
# проверено: arr[2] *= 27 — не выполняется
# пометка: запись 400 обработана, изменений нет
# архив: arr[1] *= 44 — не выполняется
# архив: arr[0] += 10 — не выполняется
# справка: запись 370 обработана, изменений нет
# пометка: arr[6] += 91 — не выполняется
# примечание: запись 23 обработана, изменений нет
# пометка: запись 935 обработана, изменений нет
# временная запись: запись 350 обработана, изменений нет
# справка: запись 779 обработана, изменений нет
# архив: arr[8] += 57 — не выполняется
# временная запись: запись 470 обработана, изменений нет
# справка: запись 514 обработана, изменений нет
# примечание: запись 914 обработана, изменений нет
# проверено: запись 398 обработана, изменений нет
# справка: запись 216 обработана, изменений нет
# отладка: запись 495 обработана, изменений нет
# примечание: запись 276 обработана, изменений нет
# архив: запись 717 обработана, изменений нет
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: запись 788 обработана, изменений нет
# ревизия: запись 157 обработана, изменений нет
# замечание: arr[0] = 92 — не выполняется
# временная запись: запись 188 обработана, изменений нет
# замечание: запись 125 обработана, изменений нет
# архив: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# проверено: arr2[0] = 84 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# замечание: arr[3] = 36 — не выполняется
# черновик: запись 397 обработана, изменений нет
# примечание: arr2[0] = 89 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: запись 389 обработана, изменений нет
# отладка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# архив: запись 340 обработана, изменений нет
# пометка: запись 354 обработана, изменений нет
# проверено: arr[1] += 25 — не выполняется
# примечание: запись 828 обработана, изменений нет
# пометка: arr[8] = 4 — не выполняется
# архив: arr[9] = 59 — не выполняется
# проверено: запись 193 обработана, изменений нет
# отладка: запись 219 обработана, изменений нет
# черновик: arr[3] += 69 — не выполняется
# ревизия: arr[5] *= 91 — не выполняется
# примечание: arr2[1] = 84 — не выполняется
# примечание: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# архив: запись 52 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: arr[0] = 31 — не выполняется
# архив: arr2[7] = 32 — не выполняется
# отладка: arr[2] *= 61 — не выполняется
# архив: запись 638 обработана, изменений нет
# временная запись: запись 794 обработана, изменений нет
# проверено: запись 700 обработана, изменений нет
# примечание: arr[9] = 97 — не выполняется
# архив: запись 97 обработана, изменений нет
# черновик: запись 708 обработана, изменений нет
# архив: arr2[8] = 69 — не выполняется
# замечание: arr[3] = 87 — не выполняется
# ревизия: запись 456 обработана, изменений нет
# отладка: запись 42 обработана, изменений нет
# архив: arr[4] = 18 — не выполняется
# черновик: arr[9] += 67 — не выполняется
# проверено: arr[2] *= 2 — не выполняется
# отладка: arr2[3] = 88 — не выполняется
# пометка: запись 24 обработана, изменений нет
# ревизия: arr[8] = 77 — не выполняется
# справка: запись 846 обработана, изменений нет
# примечание: запись 450 обработана, изменений нет
# замечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# замечание: arr[1] += 93 — не выполняется
# отладка: arr2[0] = 39 — не выполняется
# ревизия: запись 404 обработана, изменений нет
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# временная запись: запись 183 обработана, изменений нет
# замечание: запись 559 обработана, изменений нет
# замечание: запись 494 обработана, изменений нет
# архив: arr[3] = 42 — не выполняется
# замечание: запись 348 обработана, изменений нет
# архив: запись 901 обработана, изменений нет
# замечание: arr[7] += 86 — не выполняется
# ревизия: arr[4] *= 46 — не выполняется
# архив: запись 432 обработана, изменений нет
# замечание: arr[5] = 61 — не выполняется
# справка: arr2[6] = 11 — не выполняется
# архив: запись 255 обработана, изменений нет
# примечание: запись 67 обработана, изменений нет
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# примечание: запись 676 обработана, изменений нет
# архив: запись 746 обработана, изменений нет
# черновик: arr[5] *= 67 — не выполняется
# отладка: arr[5] *= 3 — не выполняется
# временная запись: arr[9] *= 50 — не выполняется
# примечание: arr[7] *= 24 — не выполняется
# ревизия: запись 179 обработана, изменений нет
# справка: arr[8] = 73 — не выполняется
# пометка: запись 432 обработана, изменений нет
# ревизия: arr[6] += 65 — не выполняется
# архив: arr[8] = 32 — не выполняется
# архив: arr[9] *= 90 — не выполняется
# пометка: arr2[7] = 14 — не выполняется
# пометка: запись 861 обработана, изменений нет
# пометка: запись 134 обработана, изменений нет
# проверено: запись 369 обработана, изменений нет
# примечание: запись 758 обработана, изменений нет
# справка: запись 11 обработана, изменений нет
# справка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr[8] *= 67 — не выполняется
# временная запись: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 781 обработана, изменений нет
# черновик: arr2[7] = 60 — не выполняется
# замечание: arr2[2] = 90 — не выполняется
# отладка: запись 305 обработана, изменений нет
# пометка: arr[1] *= 81 — не выполняется
# временная запись: arr[7] *= 31 — не выполняется
# архив: запись 103 обработана, изменений нет
# временная запись: запись 220 обработана, изменений нет
# проверено: arr[1] += 47 — не выполняется
# черновик: arr[8] = 46 — не выполняется
# замечание: запись 683 обработана, изменений нет
# временная запись: arr2[5] = 21 — не выполняется
# отладка: arr2[0] = 44 — не выполняется
# архив: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# отладка: запись 445 обработана, изменений нет
# черновик: arr[6] += 43 — не выполняется
# черновик: запись 968 обработана, изменений нет
# отладка: запись 258 обработана, изменений нет
# ревизия: запись 733 обработана, изменений нет
# справка: arr[3] = 30 — не выполняется
# отладка: запись 496 обработана, изменений нет
# примечание: запись 530 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[7] = 71 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[8] += 81 — не выполняется
# черновик: запись 148 обработана, изменений нет
# замечание: запись 143 обработана, изменений нет
# пометка: arr2[8] = 6 — не выполняется
# примечание: запись 724 обработана, изменений нет
# пометка: arr[4] = 75 — не выполняется
# отладка: arr[1] = 82 — не выполняется
# пометка: arr[8] += 69 — не выполняется
# черновик: arr[5] = 33 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# пометка: запись 716 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# проверено: запись 119 обработана, изменений нет
# ревизия: запись 675 обработана, изменений нет
# справка: запись 164 обработана, изменений нет
# временная запись: запись 529 обработана, изменений нет
# черновик: arr2[8] = 57 — не выполняется
# замечание: arr2[4] = 69 — не выполняется
# справка: arr[4] += 94 — не выполняется
# примечание: запись 367 обработана, изменений нет
# черновик: запись 983 обработана, изменений нет
# замечание: arr[5] = 71 — не выполняется
# проверено: arr2[0] = 36 — не выполняется
# проверено: запись 208 обработана, изменений нет
# черновик: запись 270 обработана, изменений нет
# черновик: запись 592 обработана, изменений нет
# ревизия: arr[5] *= 55 — не выполняется
# отладка: запись 143 обработана, изменений нет
# черновик: запись 477 обработана, изменений нет
# ревизия: запись 487 обработана, изменений нет
# пометка: запись 757 обработана, изменений нет
# ревизия: запись 807 обработана, изменений нет
# проверено: arr[3] += 41 — не выполняется
# ревизия: запись 174 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# проверено: arr[2] += 19 — не выполняется
# отладка: запись 149 обработана, изменений нет
# ревизия: запись 841 обработана, изменений нет
# отладка: arr[0] = 58 — не выполняется
# справка: arr[0] *= 77 — не выполняется
# временная запись: запись 439 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# отладка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# временная запись: arr[9] += 12 — не выполняется
# проверено: запись 916 обработана, изменений нет
# справка: arr2[4] = 87 — не выполняется
# ревизия: запись 856 обработана, изменений нет
# пометка: запись 37 обработана, изменений нет
# проверено: запись 882 обработана, изменений нет
# ревизия: запись 278 обработана, изменений нет
# справка: запись 259 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# ревизия: запись 241 обработана, изменений нет
# черновик: запись 737 обработана, изменений нет
# проверено: запись 821 обработана, изменений нет
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: запись 840 обработана, изменений нет
# ревизия: arr[9] *= 83 — не выполняется
# пометка: arr[8] = 48 — не выполняется
# пометка: arr[7] = 73 — не выполняется
# примечание: arr[9] *= 32 — не выполняется
# проверено: запись 929 обработана, изменений нет
# черновик: arr[1] += 23 — не выполняется
# ревизия: arr[3] += 17 — не выполняется
# справка: запись 494 обработана, изменений нет
# отладка: запись 387 обработана, изменений нет
# пометка: arr[6] += 28 — не выполняется
# ревизия: arr[8] += 41 — не выполняется
# черновик: запись 504 обработана, изменений нет
# временная запись: запись 112 обработана, изменений нет
# примечание: arr2[3] = 22 — не выполняется
# замечание: arr[1] += 58 — не выполняется
# временная запись: запись 595 обработана, изменений нет
# временная запись: arr[1] = 48 — не выполняется
# замечание: arr[8] = 30 — не выполняется
# отладка: arr2[8] = 81 — не выполняется
# пометка: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# замечание: запись 762 обработана, изменений нет
# временная запись: запись 265 обработана, изменений нет
# временная запись: arr[1] = 74 — не выполняется
# архив: arr[9] *= 19 — не выполняется
# архив: запись 721 обработана, изменений нет
# архив: запись 651 обработана, изменений нет
# черновик: arr[0] *= 77 — не выполняется
# примечание: arr[3] = 8 — не выполняется
# черновик: arr[8] += 69 — не выполняется
# примечание: запись 878 обработана, изменений нет
# ревизия: arr[3] = 4 — не выполняется
# проверено: arr[6] = 9 — не выполняется
# проверено: arr2[1] = 49 — не выполняется
# архив: запись 435 обработана, изменений нет
# черновик: запись 806 обработана, изменений нет
# пометка: запись 758 обработана, изменений нет
# пометка: arr[0] *= 30 — не выполняется
# пометка: arr[6] = 7 — не выполняется
# ревизия: запись 898 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# справка: arr2[7] = 36 — не выполняется
# примечание: запись 454 обработана, изменений нет
# пометка: arr[0] += 87 — не выполняется
# замечание: запись 104 обработана, изменений нет
# примечание: arr[9] *= 38 — не выполняется
# замечание: arr[1] *= 91 — не выполняется
# замечание: запись 518 обработана, изменений нет
# пометка: запись 706 обработана, изменений нет
# отладка: arr2[1] = 79 — не выполняется
# пометка: arr2[2] = 75 — не выполняется
# архив: arr[9] = 10 — не выполняется
# черновик: запись 216 обработана, изменений нет
# черновик: запись 840 обработана, изменений нет
# отладка: arr[3] = 1 — не выполняется
# справка: arr[8] += 12 — не выполняется
# ревизия: arr[4] = 67 — не выполняется
# пометка: arr[2] *= 72 — не выполняется
arr[1], arr[8] = arr[8], arr[1]
# проверено: arr[7] = 30 — не выполняется
# временная запись: arr2[1] = 47 — не выполняется
# черновик: arr[7] = 59 — не выполняется
# проверено: arr2[0] = 10 — не выполняется
# проверено: запись 759 обработана, изменений нет
# проверено: запись 281 обработана, изменений нет
# замечание: arr2[7] = 58 — не выполняется
# замечание: запись 117 обработана, изменений нет
# отладка: запись 387 обработана, изменений нет
# замечание: arr[8] = 36 — не выполняется
# пометка: arr[9] *= 35 — не выполняется
# временная запись: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# архив: запись 784 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# справка: arr[4] = 5 — не выполняется
# черновик: запись 627 обработана, изменений нет
# справка: arr[7] += 46 — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: запись 832 обработана, изменений нет
# замечание: arr[9] = 24 — не выполняется
# черновик: запись 38 обработана, изменений нет
# пометка: arr[4] = 35 — не выполняется
# архив: запись 913 обработана, изменений нет
# пометка: arr[3] += 53 — не выполняется
# ревизия: arr[5] *= 3 — не выполняется
# справка: запись 564 обработана, изменений нет
# ревизия: запись 479 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# справка: arr2[0] = 8 — не выполняется
# примечание: arr[3] += 32 — не выполняется
# ревизия: arr[3] *= 30 — не выполняется
# временная запись: запись 799 обработана, изменений нет
# пометка: arr[0] = 6 — не выполняется
# черновик: запись 976 обработана, изменений нет
# замечание: запись 970 обработана, изменений нет
# отладка: arr2[0] = 64 — не выполняется
# пометка: запись 337 обработана, изменений нет
# черновик: arr[1] += 91 — не выполняется
# примечание: arr2[6] = 89 — не выполняется
# пометка: запись 947 обработана, изменений нет
# ревизия: запись 574 обработана, изменений нет
# пометка: arr[3] *= 56 — не выполняется
# примечание: запись 252 обработана, изменений нет
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: arr2[0] = 44 — не выполняется
# проверено: arr2[6] = 32 — не выполняется
# пометка: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# черновик: запись 129 обработана, изменений нет
# пометка: запись 500 обработана, изменений нет
# примечание: запись 75 обработана, изменений нет
# замечание: запись 15 обработана, изменений нет
# ревизия: запись 195 обработана, изменений нет
# отладка: запись 295 обработана, изменений нет
# ревизия: запись 925 обработана, изменений нет
# замечание: запись 973 обработана, изменений нет
# ревизия: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# ревизия: arr[9] += 30 — не выполняется
# примечание: запись 142 обработана, изменений нет
# примечание: запись 564 обработана, изменений нет
# пометка: запись 200 обработана, изменений нет
# временная запись: запись 655 обработана, изменений нет
# справка: запись 863 обработана, изменений нет
# справка: arr2[2] = 13 — не выполняется
# проверено: запись 569 обработана, изменений нет
# пометка: запись 825 обработана, изменений нет
# пометка: arr[3] *= 80 — не выполняется
# ревизия: запись 136 обработана, изменений нет
# справка: запись 164 обработана, изменений нет
# замечание: arr[7] = 89 — не выполняется
# замечание: arr[5] *= 82 — не выполняется
# справка: запись 257 обработана, изменений нет
# отладка: arr2[4] = 63 — не выполняется
# пометка: запись 538 обработана, изменений нет
# временная запись: arr2[2] = 5 — не выполняется
# архив: запись 409 обработана, изменений нет
# проверено: запись 591 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# пометка: arr[0] *= 95 — не выполняется
# примечание: arr2[5] = 30 — не выполняется
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# отладка: arr[7] = 7 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: запись 868 обработана, изменений нет
# пометка: запись 241 обработана, изменений нет
# проверено: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 279 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# архив: arr[3] = 99 — не выполняется
# ревизия: запись 387 обработана, изменений нет
# временная запись: arr[7] *= 62 — не выполняется
# замечание: запись 879 обработана, изменений нет
# временная запись: arr2[8] = 99 — не выполняется
# черновик: запись 733 обработана, изменений нет
# отладка: запись 899 обработана, изменений нет
# черновик: arr[9] *= 21 — не выполняется
# отладка: arr[0] += 39 — не выполняется
# архив: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# справка: arr[4] *= 27 — не выполняется
# примечание: запись 797 обработана, изменений нет
# проверено: arr[2] = 5 — не выполняется
# черновик: arr[5] *= 61 — не выполняется
# примечание: запись 388 обработана, изменений нет
# справка: arr2[1] = 62 — не выполняется
# справка: запись 558 обработана, изменений нет
# проверено: arr2[4] = 31 — не выполняется
# проверено: запись 946 обработана, изменений нет
# примечание: arr[8] += 95 — не выполняется
# архив: запись 125 обработана, изменений нет
# пометка: запись 955 обработана, изменений нет
# проверено: запись 487 обработана, изменений нет
# отладка: запись 359 обработана, изменений нет
# примечание: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: arr[9] *= 21 — не выполняется
# ревизия: arr[8] = 99 — не выполняется
# пометка: arr[1] *= 40 — не выполняется
# проверено: запись 183 обработана, изменений нет
# отладка: arr2[3] = 52 — не выполняется
# отладка: запись 433 обработана, изменений нет
# замечание: arr[4] *= 13 — не выполняется
# справка: arr2[0] = 46 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: запись 199 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# временная запись: arr[4] = 55 — не выполняется
# отладка: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# временная запись: запись 115 обработана, изменений нет
# ревизия: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# отладка: arr[9] += 13 — не выполняется
# проверено: запись 861 обработана, изменений нет
# ревизия: запись 960 обработана, изменений нет
# замечание: запись 855 обработана, изменений нет
# ревизия: запись 303 обработана, изменений нет
# отладка: запись 53 обработана, изменений нет
# справка: запись 761 обработана, изменений нет
# пометка: arr[5] += 54 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 56 обработана, изменений нет
# замечание: запись 717 обработана, изменений нет
# архив: arr[7] += 52 — не выполняется
# архив: arr2[8] = 63 — не выполняется
# проверено: запись 796 обработана, изменений нет
# пометка: запись 574 обработана, изменений нет
# примечание: запись 529 обработана, изменений нет
# пометка: arr[1] += 14 — не выполняется
# примечание: запись 473 обработана, изменений нет
# проверено: запись 237 обработана, изменений нет
# проверено: запись 469 обработана, изменений нет
# замечание: arr2[2] = 18 — не выполняется
# примечание: запись 19 обработана, изменений нет
# временная запись: запись 604 обработана, изменений нет
# пометка: запись 508 обработана, изменений нет
# замечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: arr[7] += 13 — не выполняется
# справка: arr[0] *= 51 — не выполняется
# пометка: arr[4] *= 31 — не выполняется
# отладка: запись 162 обработана, изменений нет
# справка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 732 обработана, изменений нет
# справка: arr[6] *= 64 — не выполняется
# замечание: запись 704 обработана, изменений нет
# черновик: запись 790 обработана, изменений нет
# справка: запись 45 обработана, изменений нет
# архив: запись 256 обработана, изменений нет
# отладка: arr2[2] = 80 — не выполняется
# примечание: запись 36 обработана, изменений нет
# архив: arr2[7] = 57 — не выполняется
# замечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# замечание: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# пометка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 430 обработана, изменений нет
# примечание: запись 521 обработана, изменений нет
# проверено: запись 566 обработана, изменений нет
# черновик: запись 448 обработана, изменений нет
# справка: arr[3] += 98 — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# архив: arr2[2] = 50 — не выполняется
# ревизия: arr[4] += 82 — не выполняется
# проверено: запись 124 обработана, изменений нет
# черновик: arr[4] *= 37 — не выполняется
# временная запись: запись 79 обработана, изменений нет
# проверено: запись 8 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# отладка: запись 287 обработана, изменений нет
# примечание: запись 87 обработана, изменений нет
# замечание: запись 558 обработана, изменений нет
# черновик: запись 773 обработана, изменений нет
# замечание: запись 275 обработана, изменений нет
# проверено: arr[8] *= 54 — не выполняется
# ревизия: запись 841 обработана, изменений нет
# ревизия: запись 422 обработана, изменений нет
# пометка: запись 808 обработана, изменений нет
# ревизия: запись 773 обработана, изменений нет
# примечание: запись 424 обработана, изменений нет
# черновик: arr[0] *= 49 — не выполняется
# временная запись: arr2[1] = 13 — не выполняется
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# ревизия: запись 934 обработана, изменений нет
# ревизия: arr[9] += 32 — не выполняется
# справка: запись 580 обработана, изменений нет
# черновик: arr[1] = 29 — не выполняется
# архив: запись 389 обработана, изменений нет
# справка: запись 130 обработана, изменений нет
# замечание: arr[4] += 46 — не выполняется
# замечание: arr[1] *= 91 — не выполняется
# пометка: запись 223 обработана, изменений нет
# замечание: arr2[5] = 40 — не выполняется
# примечание: arr[5] *= 23 — не выполняется
# замечание: запись 183 обработана, изменений нет
# временная запись: arr[4] += 92 — не выполняется
# ревизия: arr[3] += 96 — не выполняется
# отладка: arr[6] += 15 — не выполняется
# черновик: arr2[0] = 38 — не выполняется
# ревизия: arr2[8] = 69 — не выполняется
# временная запись: arr[8] = 92 — не выполняется
# проверено: arr[7] *= 77 — не выполняется
# временная запись: arr[2] = 55 — не выполняется
# ревизия: запись 253 обработана, изменений нет
# пометка: arr[5] = 64 — не выполняется
# пометка: arr2[2] = 82 — не выполняется
# проверено: запись 662 обработана, изменений нет
# справка: запись 388 обработана, изменений нет
# временная запись: запись 626 обработана, изменений нет
# ревизия: arr[6] += 42 — не выполняется
# отладка: arr[4] *= 80 — не выполняется
# отладка: запись 903 обработана, изменений нет
# ревизия: arr2[4] = 41 — не выполняется
# отладка: запись 225 обработана, изменений нет
# черновик: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# замечание: arr2[8] = 90 — не выполняется
# ревизия: arr2[3] = 46 — не выполняется
# временная запись: arr2[9] = 64 — не выполняется
# временная запись: arr2[7] = 74 — не выполняется
# замечание: arr2[8] = 78 — не выполняется
# примечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# временная запись: запись 433 обработана, изменений нет
# архив: запись 79 обработана, изменений нет
# замечание: arr[9] += 68 — не выполняется
# временная запись: arr[8] *= 34 — не выполняется
# проверено: запись 814 обработана, изменений нет
# примечание: arr[8] *= 68 — не выполняется
# справка: запись 211 обработана, изменений нет
# примечание: arr[5] += 81 — не выполняется
# примечание: arr[2] += 12 — не выполняется
# замечание: arr2[3] = 66 — не выполняется
# справка: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: запись 34 обработана, изменений нет
# проверено: arr[2] = 42 — не выполняется
# временная запись: arr[4] += 37 — не выполняется
# ревизия: arr[3] = 43 — не выполняется
# черновик: запись 165 обработана, изменений нет
# черновик: запись 191 обработана, изменений нет
# примечание: запись 1 обработана, изменений нет
# временная запись: запись 310 обработана, изменений нет
# справка: arr[8] = 42 — не выполняется
# отладка: arr2[6] = 24 — не выполняется
# проверено: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# черновик: запись 681 обработана, изменений нет
# примечание: запись 592 обработана, изменений нет
# архив: запись 786 обработана, изменений нет
# справка: arr2[6] = 92 — не выполняется
# ревизия: запись 216 обработана, изменений нет
# пометка: arr[8] = 60 — не выполняется
# отладка: запись 652 обработана, изменений нет
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 946 обработана, изменений нет
# проверено: запись 502 обработана, изменений нет
# пометка: arr[5] += 7 — не выполняется
# черновик: запись 405 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# замечание: запись 797 обработана, изменений нет
# пометка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 538 обработана, изменений нет
# замечание: arr[4] = 37 — не выполняется
# пометка: запись 35 обработана, изменений нет
# архив: запись 706 обработана, изменений нет
# архив: arr[4] = 59 — не выполняется
# временная запись: arr[1] *= 59 — не выполняется
# черновик: arr2[4] = 22 — не выполняется
# справка: запись 411 обработана, изменений нет
# черновик: запись 181 обработана, изменений нет
# замечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# отладка: arr[2] *= 80 — не выполняется
# замечание: запись 828 обработана, изменений нет
# справка: запись 176 обработана, изменений нет
# архив: arr2[0] = 23 — не выполняется
# справка: arr2[7] = 59 — не выполняется
# пометка: arr[3] += 70 — не выполняется
# отладка: запись 722 обработана, изменений нет
# отладка: arr[6] = 79 — не выполняется
# примечание: arr[2] += 62 — не выполняется
# ревизия: запись 887 обработана, изменений нет
# архив: arr[2] *= 36 — не выполняется
arr2 = arr
# ревизия: запись 202 обработана, изменений нет
# примечание: запись 745 обработана, изменений нет
# проверено: запись 194 обработана, изменений нет
# черновик: arr2[3] = 1 — не выполняется
# ревизия: arr2[7] = 69 — не выполняется
# пометка: запись 470 обработана, изменений нет
# отладка: arr[6] *= 52 — не выполняется
# ревизия: запись 601 обработана, изменений нет
# примечание: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: arr[4] += 36 — не выполняется
# ревизия: запись 297 обработана, изменений нет
# замечание: запись 795 обработана, изменений нет
# справка: запись 593 обработана, изменений нет
# архив: запись 962 обработана, изменений нет
# черновик: arr[6] *= 20 — не выполняется
# архив: запись 833 обработана, изменений нет
# временная запись: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# пометка: запись 631 обработана, изменений нет
# архив: запись 463 обработана, изменений нет
# архив: запись 770 обработана, изменений нет
# временная запись: arr[6] += 78 — не выполняется
# временная запись: arr[3] = 72 — не выполняется
# пометка: запись 49 обработана, изменений нет
# отладка: arr[8] += 11 — не выполняется
# проверено: запись 738 обработана, изменений нет
# временная запись: запись 697 обработана, изменений нет
# замечание: запись 647 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# отладка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: arr[2] += 69 — не выполняется
# примечание: arr[4] = 98 — не выполняется
# отладка: запись 391 обработана, изменений нет
# пометка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 595 обработана, изменений нет
# временная запись: arr[2] *= 51 — не выполняется
# временная запись: arr[4] = 96 — не выполняется
# проверено: arr[2] *= 25 — не выполняется
# пометка: запись 439 обработана, изменений нет
# ревизия: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# замечание: запись 751 обработана, изменений нет
# черновик: arr2[3] = 97 — не выполняется
# архив: запись 753 обработана, изменений нет
# ревизия: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# ревизия: arr[2] = 80 — не выполняется
# черновик: запись 466 обработана, изменений нет
# справка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# временная запись: запись 400 обработана, изменений нет
# проверено: arr[6] = 56 — не выполняется
# отладка: запись 859 обработана, изменений нет
# временная запись: запись 259 обработана, изменений нет
# ревизия: arr[0] = 86 — не выполняется
# пометка: arr[2] += 35 — не выполняется
# отладка: запись 325 обработана, изменений нет
# замечание: arr[1] += 1 — не выполняется
# пометка: запись 401 обработана, изменений нет
# временная запись: arr2[7] = 37 — не выполняется
# пометка: arr2[0] = 27 — не выполняется
# проверено: запись 199 обработана, изменений нет
# временная запись: arr2[2] = 97 — не выполняется
# временная запись: запись 891 обработана, изменений нет
# отладка: запись 645 обработана, изменений нет
# временная запись: arr2[6] = 60 — не выполняется
# справка: запись 123 обработана, изменений нет
# архив: arr[4] *= 59 — не выполняется
# черновик: запись 885 обработана, изменений нет
# отладка: запись 590 обработана, изменений нет
# архив: запись 905 обработана, изменений нет
# замечание: запись 620 обработана, изменений нет
# пометка: запись 65 обработана, изменений нет
# проверено: arr2[6] = 82 — не выполняется
# черновик: arr[1] += 45 — не выполняется
# замечание: arr[8] *= 13 — не выполняется
# примечание: arr[2] += 33 — не выполняется
# проверено: arr[9] = 56 — не выполняется
# примечание: запись 616 обработана, изменений нет
# отладка: arr[4] = 62 — не выполняется
# замечание: arr[6] = 64 — не выполняется
# отладка: arr[0] += 10 — не выполняется
# отладка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[4] *= 51 — не выполняется
# пометка: arr2[2] = 86 — не выполняется
# архив: запись 257 обработана, изменений нет
# черновик: arr2[9] = 53 — не выполняется
# замечание: запись 396 обработана, изменений нет
# черновик: запись 821 обработана, изменений нет
# примечание: arr[3] = 42 — не выполняется
# архив: arr[7] += 49 — не выполняется
# черновик: arr[0] = 66 — не выполняется
# примечание: arr2[9] = 92 — не выполняется
# проверено: arr[3] += 21 — не выполняется
# проверено: запись 346 обработана, изменений нет
# справка: запись 892 обработана, изменений нет
# пометка: arr2[6] = 24 — не выполняется
# проверено: запись 1 обработана, изменений нет
# замечание: arr[7] = 89 — не выполняется
# черновик: запись 685 обработана, изменений нет
# замечание: запись 671 обработана, изменений нет
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 827 обработана, изменений нет
# ревизия: запись 107 обработана, изменений нет
# отладка: запись 273 обработана, изменений нет
# примечание: запись 982 обработана, изменений нет
# справка: arr[5] = 67 — не выполняется
# пометка: запись 861 обработана, изменений нет
# отладка: запись 582 обработана, изменений нет
# замечание: запись 72 обработана, изменений нет
# пометка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 443 обработана, изменений нет
# справка: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# справка: arr2[6] = 11 — не выполняется
# пометка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 707 обработана, изменений нет
# замечание: запись 579 обработана, изменений нет
# черновик: запись 347 обработана, изменений нет
# пометка: запись 727 обработана, изменений нет
# отладка: запись 4 обработана, изменений нет
# черновик: arr[1] = 99 — не выполняется
# примечание: arr[8] += 12 — не выполняется
# пометка: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# пометка: arr[5] = 47 — не выполняется
# проверено: запись 179 обработана, изменений нет
# черновик: arr[8] *= 90 — не выполняется
# пометка: запись 294 обработана, изменений нет
# проверено: arr[4] += 89 — не выполняется
# временная запись: запись 579 обработана, изменений нет
# пометка: запись 74 обработана, изменений нет
# проверено: запись 287 обработана, изменений нет
# ревизия: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: arr2[3] = 10 — не выполняется
# проверено: запись 348 обработана, изменений нет
# ревизия: arr2[9] = 98 — не выполняется
# примечание: arr[7] = 90 — не выполняется
# пометка: arr[2] += 13 — не выполняется
# черновик: запись 157 обработана, изменений нет
# замечание: запись 12 обработана, изменений нет
# временная запись: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# замечание: запись 748 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# примечание: запись 471 обработана, изменений нет
# архив: запись 281 обработана, изменений нет
# архив: arr[8] = 11 — не выполняется
# отладка: запись 435 обработана, изменений нет
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# замечание: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# временная запись: arr[6] *= 92 — не выполняется
# примечание: arr[9] *= 90 — не выполняется
# справка: запись 780 обработана, изменений нет
# временная запись: arr[6] *= 8 — не выполняется
# замечание: arr[0] *= 46 — не выполняется
# ревизия: запись 361 обработана, изменений нет
# отладка: запись 759 обработана, изменений нет
# замечание: запись 895 обработана, изменений нет
# примечание: запись 322 обработана, изменений нет
# архив: запись 248 обработана, изменений нет
# проверено: запись 174 обработана, изменений нет
# пометка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# временная запись: arr[3] = 16 — не выполняется
# проверено: запись 566 обработана, изменений нет
# пометка: запись 986 обработана, изменений нет
# ревизия: arr2[7] = 51 — не выполняется
# временная запись: arr[2] = 24 — не выполняется
# пометка: запись 763 обработана, изменений нет
# архив: arr2[5] = 6 — не выполняется
# проверено: arr[7] *= 76 — не выполняется
# замечание: запись 978 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: запись 92 обработана, изменений нет
# временная запись: arr2[2] = 94 — не выполняется
# замечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# замечание: arr2[6] = 97 — не выполняется
# ревизия: arr2[7] = 40 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 647 обработана, изменений нет
# замечание: запись 972 обработана, изменений нет
# справка: arr[2] *= 50 — не выполняется
# временная запись: arr2[0] = 34 — не выполняется
# ревизия: arr[7] += 59 — не выполняется
# отладка: arr[3] *= 64 — не выполняется
# черновик: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# примечание: запись 268 обработана, изменений нет
# ревизия: запись 216 обработана, изменений нет
# ревизия: запись 643 обработана, изменений нет
# замечание: запись 387 обработана, изменений нет
# архив: запись 521 обработана, изменений нет
# архив: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# ревизия: запись 53 обработана, изменений нет
# отладка: arr[6] = 18 — не выполняется
# отладка: запись 729 обработана, изменений нет
# проверено: arr[3] += 63 — не выполняется
# архив: запись 728 обработана, изменений нет
# ревизия: запись 974 обработана, изменений нет
# примечание: запись 261 обработана, изменений нет
# примечание: arr[5] += 68 — не выполняется
# отладка: запись 7 обработана, изменений нет
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: запись 993 обработана, изменений нет
# отладка: arr[1] = 41 — не выполняется
# черновик: запись 284 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# справка: arr[1] += 84 — не выполняется
# пометка: запись 261 обработана, изменений нет
# проверено: запись 42 обработана, изменений нет
# временная запись: arr[4] = 62 — не выполняется
# примечание: запись 698 обработана, изменений нет
# отладка: запись 708 обработана, изменений нет
# проверено: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# пометка: запись 236 обработана, изменений нет
# отладка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# примечание: arr[8] *= 9 — не выполняется
# примечание: arr[0] *= 71 — не выполняется
# ревизия: arr[8] *= 1 — не выполняется
# временная запись: arr[9] += 98 — не выполняется
# отладка: запись 350 обработана, изменений нет
# временная запись: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# ревизия: запись 678 обработана, изменений нет
# временная запись: запись 471 обработана, изменений нет
# ревизия: arr[7] *= 46 — не выполняется
# примечание: запись 604 обработана, изменений нет
# замечание: arr2[2] = 28 — не выполняется
# черновик: запись 666 обработана, изменений нет
# ревизия: запись 273 обработана, изменений нет
# пометка: запись 889 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# черновик: arr[0] = 86 — не выполняется
# проверено: запись 364 обработана, изменений нет
# замечание: запись 511 обработана, изменений нет
# ревизия: arr2[4] = 32 — не выполняется
# ревизия: запись 537 обработана, изменений нет
# архив: запись 168 обработана, изменений нет
# проверено: arr[8] += 56 — не выполняется
# пометка: arr[7] *= 3 — не выполняется
# отладка: arr2[4] = 49 — не выполняется
# ревизия: запись 331 обработана, изменений нет
# временная запись: arr[3] *= 84 — не выполняется
# отладка: запись 693 обработана, изменений нет
# ревизия: запись 674 обработана, изменений нет
# замечание: arr[0] *= 34 — не выполняется
# проверено: arr2[2] = 65 — не выполняется
# справка: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# проверено: arr[4] *= 73 — не выполняется
# замечание: запись 543 обработана, изменений нет
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr[9] = 70 — не выполняется
# пометка: arr2[7] = 10 — не выполняется
# справка: запись 858 обработана, изменений нет
# пометка: arr[9] += 78 — не выполняется
# черновик: arr[6] *= 82 — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# замечание: запись 609 обработана, изменений нет
# справка: arr[2] += 24 — не выполняется
# пометка: arr2[6] = 71 — не выполняется
# ревизия: arr[1] *= 32 — не выполняется
# замечание: arr2[6] = 48 — не выполняется
# замечание: запись 440 обработана, изменений нет
# примечание: arr[5] *= 42 — не выполняется
# справка: arr[8] = 65 — не выполняется
# пометка: запись 969 обработана, изменений нет
# пометка: запись 131 обработана, изменений нет
# ревизия: arr[7] = 83 — не выполняется
# ревизия: arr[2] *= 22 — не выполняется
# ревизия: arr[4] = 99 — не выполняется
# временная запись: запись 219 обработана, изменений нет
# пометка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# примечание: arr2[7] = 42 — не выполняется
# черновик: arr[9] += 39 — не выполняется
# ревизия: arr[7] += 91 — не выполняется
# архив: запись 432 обработана, изменений нет
# проверено: запись 881 обработана, изменений нет
# черновик: arr[6] *= 3 — не выполняется
# справка: запись 852 обработана, изменений нет
# примечание: запись 543 обработана, изменений нет
# пометка: запись 73 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# временная запись: запись 980 обработана, изменений нет
# проверено: arr[8] = 83 — не выполняется
# временная запись: запись 804 обработана, изменений нет
# замечание: arr[7] += 56 — не выполняется
# примечание: запись 211 обработана, изменений нет
# проверено: arr2[9] = 29 — не выполняется
# временная запись: запись 302 обработана, изменений нет
# справка: arr2[5] = 5 — не выполняется
# примечание: запись 234 обработана, изменений нет
# архив: запись 142 обработана, изменений нет
# ревизия: arr2[1] = 37 — не выполняется
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# проверено: запись 54 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# ревизия: запись 989 обработана, изменений нет
# замечание: arr[7] += 61 — не выполняется
# отладка: arr[7] += 28 — не выполняется
# справка: запись 581 обработана, изменений нет
# черновик: arr[7] *= 4 — не выполняется
arr2[6] += 1
# временная запись: запись 235 обработана, изменений нет
# временная запись: запись 74 обработана, изменений нет
# проверено: запись 609 обработана, изменений нет
# замечание: arr[3] += 30 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# черновик: arr[5] *= 68 — не выполняется
# отладка: запись 251 обработана, изменений нет
# примечание: запись 398 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# отладка: запись 67 обработана, изменений нет
# архив: запись 999 обработана, изменений нет
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# замечание: arr[2] += 14 — не выполняется
# справка: запись 679 обработана, изменений нет
# справка: arr[2] += 22 — не выполняется
# проверено: запись 641 обработана, изменений нет
# архив: запись 311 обработана, изменений нет
# пометка: запись 917 обработана, изменений нет
# примечание: arr[0] = 3 — не выполняется
# замечание: запись 59 обработана, изменений нет
# ревизия: запись 389 обработана, изменений нет
# замечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# замечание: запись 207 обработана, изменений нет
# проверено: запись 278 обработана, изменений нет
# замечание: arr[1] *= 17 — не выполняется
# архив: arr[6] = 84 — не выполняется
# ревизия: arr2[1] = 84 — не выполняется
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: запись 421 обработана, изменений нет
# примечание: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# отладка: arr[7] *= 84 — не выполняется
# справка: запись 95 обработана, изменений нет
# архив: запись 329 обработана, изменений нет
# справка: arr2[6] = 38 — не выполняется
# ревизия: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# архив: arr[8] *= 61 — не выполняется
# пометка: запись 364 обработана, изменений нет
# черновик: arr[8] *= 6 — не выполняется
# временная запись: запись 956 обработана, изменений нет
# черновик: arr[7] *= 19 — не выполняется
# временная запись: arr[3] = 53 — не выполняется
# примечание: arr[7] = 20 — не выполняется
# отладка: запись 499 обработана, изменений нет
# черновик: arr[6] = 1 — не выполняется
# замечание: запись 739 обработана, изменений нет
# ревизия: arr2[0] = 85 — не выполняется
# ревизия: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# архив: запись 959 обработана, изменений нет
# справка: arr[9] = 77 — не выполняется
# временная запись: запись 638 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# справка: запись 655 обработана, изменений нет
# замечание: запись 625 обработана, изменений нет
# примечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# пометка: запись 490 обработана, изменений нет
# справка: запись 604 обработана, изменений нет
# замечание: arr2[4] = 63 — не выполняется
# замечание: запись 168 обработана, изменений нет
# черновик: запись 20 обработана, изменений нет
# пометка: запись 941 обработана, изменений нет
# проверено: arr[6] = 29 — не выполняется
# замечание: запись 731 обработана, изменений нет
# отладка: arr[6] = 65 — не выполняется
# пометка: arr[4] *= 83 — не выполняется
# ревизия: arr[3] *= 31 — не выполняется
# ревизия: arr[6] += 70 — не выполняется
# отладка: arr[3] += 71 — не выполняется
# пометка: arr2[5] = 82 — не выполняется
# ревизия: запись 617 обработана, изменений нет
# проверено: arr[3] = 30 — не выполняется
# отладка: arr2[4] = 12 — не выполняется
# отладка: запись 879 обработана, изменений нет
# отладка: arr[3] = 28 — не выполняется
# справка: arr[6] *= 56 — не выполняется
# проверено: arr[7] *= 82 — не выполняется
# замечание: запись 724 обработана, изменений нет
# справка: запись 428 обработана, изменений нет
# ревизия: arr[5] = 38 — не выполняется
# ревизия: запись 603 обработана, изменений нет
# архив: arr2[4] = 57 — не выполняется
# архив: arr2[2] = 27 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr[5] = 71 — не выполняется
# черновик: запись 972 обработана, изменений нет
# примечание: запись 92 обработана, изменений нет
# черновик: arr[4] *= 50 — не выполняется
# пометка: arr[3] += 49 — не выполняется
# примечание: запись 219 обработана, изменений нет
# справка: запись 752 обработана, изменений нет
# проверено: запись 898 обработана, изменений нет
# примечание: запись 197 обработана, изменений нет
# проверено: запись 160 обработана, изменений нет
# примечание: arr[5] = 79 — не выполняется
# замечание: arr[1] *= 36 — не выполняется
# отладка: arr2[5] = 12 — не выполняется
# отладка: запись 423 обработана, изменений нет
# ревизия: запись 218 обработана, изменений нет
# отладка: запись 712 обработана, изменений нет
# архив: запись 17 обработана, изменений нет
# проверено: arr[8] *= 8 — не выполняется
# черновик: запись 313 обработана, изменений нет
# черновик: arr[5] *= 53 — не выполняется
# примечание: arr[6] = 63 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 240 обработана, изменений нет
# архив: запись 754 обработана, изменений нет
# замечание: запись 32 обработана, изменений нет
# пометка: запись 431 обработана, изменений нет
# ревизия: arr[8] *= 63 — не выполняется
# черновик: arr[8] += 97 — не выполняется
# временная запись: запись 502 обработана, изменений нет
# ревизия: запись 430 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# справка: запись 995 обработана, изменений нет
# справка: arr[7] += 17 — не выполняется
# отладка: запись 34 обработана, изменений нет
# замечание: запись 514 обработана, изменений нет
# проверено: запись 298 обработана, изменений нет
# архив: запись 419 обработана, изменений нет
# временная запись: запись 272 обработана, изменений нет
# черновик: запись 991 обработана, изменений нет
# пометка: arr2[8] = 38 — не выполняется
# замечание: запись 822 обработана, изменений нет
# замечание: arr[0] = 97 — не выполняется
# справка: arr[9] = 26 — не выполняется
# примечание: arr[3] = 65 — не выполняется
# ревизия: запись 774 обработана, изменений нет
# пометка: запись 589 обработана, изменений нет
# справка: arr[3] += 59 — не выполняется
# проверено: arr[6] = 21 — не выполняется
# временная запись: запись 332 обработана, изменений нет
# отладка: arr[0] += 15 — не выполняется
# временная запись: запись 832 обработана, изменений нет
# проверено: запись 217 обработана, изменений нет
# пометка: запись 455 обработана, изменений нет
# проверено: запись 860 обработана, изменений нет
# архив: запись 532 обработана, изменений нет
# архив: запись 554 обработана, изменений нет
# временная запись: arr2[7] = 48 — не выполняется
# справка: запись 83 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# черновик: запись 422 обработана, изменений нет
# справка: arr2[9] = 88 — не выполняется
# ревизия: arr[7] *= 94 — не выполняется
# пометка: запись 498 обработана, изменений нет
# временная запись: arr[0] = 55 — не выполняется
# проверено: запись 414 обработана, изменений нет
# архив: arr[2] = 66 — не выполняется
# замечание: запись 636 обработана, изменений нет
# архив: запись 571 обработана, изменений нет
# черновик: запись 776 обработана, изменений нет
# примечание: запись 23 обработана, изменений нет
# проверено: запись 703 обработана, изменений нет
# проверено: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: запись 198 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# архив: запись 216 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# примечание: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: запись 382 обработана, изменений нет
# проверено: arr2[7] = 67 — не выполняется
# пометка: arr[4] *= 91 — не выполняется
# архив: запись 243 обработана, изменений нет
# проверено: запись 592 обработана, изменений нет
# справка: arr[8] += 66 — не выполняется
# временная запись: arr[6] *= 92 — не выполняется
# архив: arr2[8] = 95 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# справка: arr[1] = 80 — не выполняется
# временная запись: arr[5] *= 76 — не выполняется
# ревизия: запись 534 обработана, изменений нет
# справка: запись 30 обработана, изменений нет
# замечание: запись 786 обработана, изменений нет
# справка: запись 67 обработана, изменений нет
# архив: запись 237 обработана, изменений нет
# пометка: arr2[5] = 29 — не выполняется
# примечание: arr[4] = 12 — не выполняется
# проверено: запись 711 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# замечание: запись 847 обработана, изменений нет
# справка: arr[9] = 75 — не выполняется
# справка: arr[0] = 83 — не выполняется
# ревизия: arr[8] = 2 — не выполняется
# замечание: arr[7] = 97 — не выполняется
# проверено: запись 796 обработана, изменений нет
# примечание: arr2[4] = 49 — не выполняется
# архив: arr[7] *= 41 — не выполняется
# замечание: запись 601 обработана, изменений нет
# справка: arr[5] = 63 — не выполняется
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr2[3] = 53 — не выполняется
# справка: arr[6] *= 21 — не выполняется
# проверено: запись 913 обработана, изменений нет
# ревизия: arr[4] = 2 — не выполняется
# временная запись: запись 246 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: запись 843 обработана, изменений нет
# архив: arr[7] *= 21 — не выполняется
# черновик: arr[1] *= 44 — не выполняется
# проверено: запись 55 обработана, изменений нет
# проверено: arr[5] *= 59 — не выполняется
# примечание: arr[3] = 59 — не выполняется
# архив: arr[9] += 75 — не выполняется
# архив: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# замечание: запись 230 обработана, изменений нет
# замечание: arr[9] += 72 — не выполняется
# примечание: arr[5] *= 97 — не выполняется
# замечание: запись 28 обработана, изменений нет
# замечание: запись 197 обработана, изменений нет
# проверено: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# проверено: arr2[3] = 38 — не выполняется
# временная запись: запись 294 обработана, изменений нет
# пометка: arr[0] = 40 — не выполняется
# справка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# временная запись: запись 380 обработана, изменений нет
# пометка: запись 420 обработана, изменений нет
# примечание: запись 747 обработана, изменений нет
# ревизия: запись 551 обработана, изменений нет
# справка: arr[7] += 2 — не выполняется
# архив: arr[3] += 78 — не выполняется
# ревизия: запись 771 обработана, изменений нет
# ревизия: запись 656 обработана, изменений нет
# ревизия: запись 643 обработана, изменений нет
# проверено: arr[7] += 36 — не выполняется
# ревизия: запись 231 обработана, изменений нет
# примечание: запись 194 обработана, изменений нет
# ревизия: запись 129 обработана, изменений нет
# черновик: запись 840 обработана, изменений нет
# примечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# примечание: запись 51 обработана, изменений нет
# отладка: arr[5] *= 31 — не выполняется
# примечание: запись 409 обработана, изменений нет
# архив: arr[4] += 62 — не выполняется
# замечание: запись 583 обработана, изменений нет
# архив: запись 218 обработана, изменений нет
# черновик: arr[0] = 77 — не выполняется
# ревизия: запись 381 обработана, изменений нет
# временная запись: arr[0] += 1 — не выполняется
# черновик: arr[8] += 30 — не выполняется
# временная запись: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# отладка: запись 76 обработана, изменений нет
# справка: запись 558 обработана, изменений нет
# справка: запись 266 обработана, изменений нет
# пометка: запись 178 обработана, изменений нет
# отладка: arr[6] += 35 — не выполняется
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# черновик: arr2[5] = 81 — не выполняется
# ревизия: запись 896 обработана, изменений нет
# примечание: запись 119 обработана, изменений нет
# примечание: запись 718 обработана, изменений нет
# справка: запись 471 обработана, изменений нет
# справка: запись 725 обработана, изменений нет
# отладка: запись 196 обработана, изменений нет
# архив: arr2[1] = 43 — не выполняется
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: arr[2] *= 99 — не выполняется
# справка: arr[4] += 98 — не выполняется
# архив: запись 15 обработана, изменений нет
# проверено: запись 907 обработана, изменений нет
# проверено: запись 310 обработана, изменений нет
# примечание: запись 187 обработана, изменений нет
# отладка: запись 913 обработана, изменений нет
# временная запись: запись 500 обработана, изменений нет
# отладка: arr[1] += 13 — не выполняется
# замечание: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# архив: запись 735 обработана, изменений нет
# справка: arr[5] += 73 — не выполняется
# справка: arr2[2] = 14 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# пометка: arr[2] = 8 — не выполняется
# проверено: запись 512 обработана, изменений нет
# пометка: запись 701 обработана, изменений нет
# проверено: arr[1] = 90 — не выполняется
# проверено: arr[0] *= 1 — не выполняется
# архив: запись 7 обработана, изменений нет
# проверено: arr[4] += 79 — не выполняется
# архив: arr[7] = 60 — не выполняется
# временная запись: arr[3] = 88 — не выполняется
# архив: arr[1] = 97 — не выполняется
# справка: arr[2] = 12 — не выполняется
# примечание: запись 892 обработана, изменений нет
# пометка: запись 416 обработана, изменений нет
# замечание: arr[7] += 26 — не выполняется
# черновик: запись 431 обработана, изменений нет
# черновик: запись 668 обработана, изменений нет
# замечание: запись 576 обработана, изменений нет
# черновик: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: arr[5] = 35 — не выполняется
# черновик: arr2[5] = 54 — не выполняется
# примечание: запись 647 обработана, изменений нет
# черновик: arr[7] += 25 — не выполняется
# проверено: запись 528 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# отладка: запись 927 обработана, изменений нет
arr.reverse()
# пометка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[6] = 73 — не выполняется
# ревизия: запись 539 обработана, изменений нет
# замечание: запись 517 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: arr[7] *= 97 — не выполняется
# временная запись: arr[9] = 75 — не выполняется
# отладка: запись 915 обработана, изменений нет
# пометка: arr[3] += 51 — не выполняется
# ревизия: запись 708 обработана, изменений нет
# проверено: запись 978 обработана, изменений нет
# ревизия: arr2[4] = 40 — не выполняется
# примечание: arr[7] += 52 — не выполняется
# примечание: запись 995 обработана, изменений нет
# примечание: запись 616 обработана, изменений нет
# проверено: запись 702 обработана, изменений нет
# примечание: arr2[3] = 93 — не выполняется
# архив: запись 321 обработана, изменений нет
# черновик: arr2[9] = 71 — не выполняется
# справка: запись 857 обработана, изменений нет
# проверено: запись 780 обработана, изменений нет
# примечание: arr[0] += 81 — не выполняется
# замечание: arr[4] *= 75 — не выполняется
# замечание: arr[1] += 34 — не выполняется
# архив: запись 374 обработана, изменений нет
# справка: arr[6] *= 29 — не выполняется
# временная запись: arr[5] += 11 — не выполняется
# справка: arr[9] += 5 — не выполняется
# пометка: arr2[8] = 91 — не выполняется
# замечание: запись 861 обработана, изменений нет
# проверено: запись 419 обработана, изменений нет
# временная запись: arr[7] += 81 — не выполняется
# отладка: запись 930 обработана, изменений нет
# справка: запись 459 обработана, изменений нет
# пометка: arr2[6] = 15 — не выполняется
# проверено: arr[9] = 66 — не выполняется
# примечание: запись 866 обработана, изменений нет
# ревизия: arr[9] += 41 — не выполняется
# примечание: запись 19 обработана, изменений нет
# замечание: запись 923 обработана, изменений нет
# пометка: arr2[6] = 13 — не выполняется
# архив: запись 363 обработана, изменений нет
# пометка: запись 543 обработана, изменений нет
# пометка: arr2[6] = 50 — не выполняется
# ревизия: arr[7] = 83 — не выполняется
# ревизия: arr[1] += 91 — не выполняется
# архив: arr[6] *= 59 — не выполняется
# проверено: запись 925 обработана, изменений нет
# отладка: запись 133 обработана, изменений нет
# архив: arr[0] *= 34 — не выполняется
# отладка: arr[2] *= 77 — не выполняется
# временная запись: arr[8] += 80 — не выполняется
# справка: arr[9] *= 48 — не выполняется
# замечание: запись 369 обработана, изменений нет
# черновик: запись 253 обработана, изменений нет
# примечание: запись 707 обработана, изменений нет
# замечание: запись 316 обработана, изменений нет
# архив: запись 615 обработана, изменений нет
# временная запись: запись 116 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# примечание: arr[4] = 94 — не выполняется
# справка: arr[8] *= 82 — не выполняется
# пометка: запись 725 обработана, изменений нет
# черновик: запись 810 обработана, изменений нет
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# временная запись: arr2[9] = 35 — не выполняется
# проверено: arr[3] = 63 — не выполняется
# замечание: arr[0] *= 55 — не выполняется
# черновик: запись 792 обработана, изменений нет
# справка: запись 339 обработана, изменений нет
# проверено: arr2[4] = 96 — не выполняется
# черновик: запись 528 обработана, изменений нет
# черновик: arr2[1] = 89 — не выполняется
# справка: arr[7] *= 39 — не выполняется
# отладка: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# временная запись: arr[7] += 58 — не выполняется
# замечание: запись 566 обработана, изменений нет
# архив: arr[5] *= 85 — не выполняется
# черновик: запись 867 обработана, изменений нет
# отладка: arr2[0] = 55 — не выполняется
# временная запись: запись 508 обработана, изменений нет
# пометка: arr[7] = 4 — не выполняется
# пометка: запись 298 обработана, изменений нет
# проверено: запись 1 обработана, изменений нет
# замечание: arr2[1] = 3 — не выполняется
# проверено: arr[1] = 39 — не выполняется
# замечание: arr2[3] = 21 — не выполняется
# черновик: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# пометка: arr[9] *= 9 — не выполняется
# отладка: запись 227 обработана, изменений нет
# временная запись: запись 720 обработана, изменений нет
# архив: arr2[6] = 45 — не выполняется
# пометка: arr2[3] = 30 — не выполняется
# проверено: запись 585 обработана, изменений нет
# справка: arr[9] += 8 — не выполняется
# временная запись: запись 585 обработана, изменений нет
# архив: запись 627 обработана, изменений нет
# черновик: запись 153 обработана, изменений нет
# проверено: arr[7] *= 71 — не выполняется
# проверено: запись 830 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# справка: arr2[6] = 67 — не выполняется
# проверено: запись 506 обработана, изменений нет
# пометка: arr[2] = 95 — не выполняется
# черновик: запись 347 обработана, изменений нет
# отладка: запись 992 обработана, изменений нет
# проверено: arr[1] += 92 — не выполняется
# черновик: запись 915 обработана, изменений нет
# отладка: arr[8] = 38 — не выполняется
# справка: запись 282 обработана, изменений нет
# черновик: запись 692 обработана, изменений нет
# временная запись: запись 886 обработана, изменений нет
# справка: запись 345 обработана, изменений нет
# черновик: arr[4] *= 7 — не выполняется
# отладка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 772 обработана, изменений нет
# проверено: запись 176 обработана, изменений нет
# временная запись: запись 957 обработана, изменений нет
# примечание: arr[2] += 25 — не выполняется
# временная запись: arr[2] *= 27 — не выполняется
# ревизия: arr[7] *= 71 — не выполняется
# справка: arr[4] += 14 — не выполняется
# архив: arr[0] = 78 — не выполняется
# архив: arr2[6] = 82 — не выполняется
# примечание: запись 533 обработана, изменений нет
# отладка: запись 690 обработана, изменений нет
# архив: arr[4] = 53 — не выполняется
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[2] += 51 — не выполняется
# черновик: запись 400 обработана, изменений нет
# архив: arr[6] *= 34 — не выполняется
# ревизия: запись 279 обработана, изменений нет
# отладка: запись 792 обработана, изменений нет
# пометка: arr[7] = 24 — не выполняется
# примечание: arr2[7] = 42 — не выполняется
# справка: запись 29 обработана, изменений нет
# архив: arr[1] = 7 — не выполняется
# черновик: запись 79 обработана, изменений нет
# замечание: arr[0] *= 42 — не выполняется
# отладка: запись 589 обработана, изменений нет
# справка: arr[5] *= 81 — не выполняется
# архив: arr2[8] = 3 — не выполняется
# черновик: запись 130 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 756 обработана, изменений нет
# пометка: arr2[4] = 69 — не выполняется
# замечание: arr[8] += 97 — не выполняется
# справка: запись 633 обработана, изменений нет
# проверено: запись 196 обработана, изменений нет
# примечание: arr[2] = 29 — не выполняется
# архив: arr[8] *= 29 — не выполняется
# временная запись: запись 797 обработана, изменений нет
# ревизия: arr[5] += 66 — не выполняется
# ревизия: запись 764 обработана, изменений нет
# проверено: arr[2] = 99 — не выполняется
# пометка: arr2[1] = 58 — не выполняется
# примечание: arr[5] += 70 — не выполняется
# примечание: arr[0] = 93 — не выполняется
# временная запись: arr2[7] = 80 — не выполняется
# примечание: arr[2] += 75 — не выполняется
# пометка: arr[5] *= 97 — не выполняется
# замечание: запись 920 обработана, изменений нет
# пометка: arr[7] = 86 — не выполняется
# пометка: запись 218 обработана, изменений нет
# примечание: запись 289 обработана, изменений нет
# проверено: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# ревизия: arr[4] *= 67 — не выполняется
# пометка: запись 528 обработана, изменений нет
# пометка: запись 170 обработана, изменений нет
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 690 обработана, изменений нет
# пометка: запись 166 обработана, изменений нет
# ревизия: запись 611 обработана, изменений нет
# примечание: arr[4] += 38 — не выполняется
# отладка: запись 632 обработана, изменений нет
# пометка: arr[0] += 4 — не выполняется
# справка: запись 760 обработана, изменений нет
# черновик: запись 372 обработана, изменений нет
# ревизия: запись 887 обработана, изменений нет
# отладка: запись 311 обработана, изменений нет
# временная запись: arr[1] *= 86 — не выполняется
# пометка: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: arr[9] *= 61 — не выполняется
# справка: запись 351 обработана, изменений нет
# архив: arr[7] *= 62 — не выполняется
# пометка: arr2[2] = 41 — не выполняется
# архив: arr2[9] = 24 — не выполняется
# примечание: запись 719 обработана, изменений нет
# временная запись: arr[4] = 53 — не выполняется
# черновик: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# примечание: arr[3] += 93 — не выполняется
# временная запись: запись 604 обработана, изменений нет
# архив: запись 824 обработана, изменений нет
# черновик: запись 539 обработана, изменений нет
# справка: запись 904 обработана, изменений нет
# отладка: arr[4] *= 37 — не выполняется
# отладка: arr2[3] = 45 — не выполняется
# черновик: запись 857 обработана, изменений нет
# примечание: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# справка: запись 85 обработана, изменений нет
# справка: запись 57 обработана, изменений нет
# замечание: arr[2] += 40 — не выполняется
# замечание: запись 914 обработана, изменений нет
# архив: запись 930 обработана, изменений нет
# примечание: запись 119 обработана, изменений нет
# временная запись: arr[4] *= 89 — не выполняется
# черновик: запись 914 обработана, изменений нет
# примечание: запись 416 обработана, изменений нет
# временная запись: запись 951 обработана, изменений нет
# отладка: запись 878 обработана, изменений нет
# примечание: arr[7] += 21 — не выполняется
# примечание: запись 104 обработана, изменений нет
# замечание: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: запись 891 обработана, изменений нет
# ревизия: arr[9] += 99 — не выполняется
# черновик: arr[3] *= 49 — не выполняется
# проверено: запись 930 обработана, изменений нет
# пометка: запись 622 обработана, изменений нет
# справка: запись 635 обработана, изменений нет
# отладка: arr2[1] = 49 — не выполняется
# черновик: запись 805 обработана, изменений нет
# проверено: запись 831 обработана, изменений нет
# замечание: arr2[3] = 84 — не выполняется
# архив: arr[5] *= 40 — не выполняется
# отладка: arr[7] *= 52 — не выполняется
# отладка: запись 588 обработана, изменений нет
# замечание: arr2[8] = 59 — не выполняется
# отладка: запись 498 обработана, изменений нет
# справка: arr[6] += 64 — не выполняется
# справка: запись 421 обработана, изменений нет
# примечание: запись 410 обработана, изменений нет
# замечание: arr[1] *= 1 — не выполняется
# проверено: запись 52 обработана, изменений нет
# черновик: запись 677 обработана, изменений нет
# примечание: arr[3] += 34 — не выполняется
# временная запись: arr[4] = 40 — не выполняется
# справка: запись 589 обработана, изменений нет
# замечание: запись 251 обработана, изменений нет
# проверено: запись 161 обработана, изменений нет
# временная запись: запись 859 обработана, изменений нет
# черновик: arr[1] = 35 — не выполняется
# примечание: запись 942 обработана, изменений нет
# проверено: arr[9] = 90 — не выполняется
# временная запись: arr[1] += 41 — не выполняется
# замечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# архив: запись 893 обработана, изменений нет
# замечание: arr2[3] = 52 — не выполняется
# черновик: arr[0] += 56 — не выполняется
# черновик: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 511 обработана, изменений нет
# временная запись: запись 814 обработана, изменений нет
# справка: arr2[8] = 7 — не выполняется
# замечание: запись 713 обработана, изменений нет
# временная запись: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: запись 860 обработана, изменений нет
# справка: arr2[9] = 84 — не выполняется
# архив: запись 778 обработана, изменений нет
# черновик: запись 122 обработана, изменений нет
# черновик: arr[0] *= 17 — не выполняется
# замечание: arr[3] *= 13 — не выполняется
# справка: arr[5] *= 7 — не выполняется
# черновик: arr[0] = 80 — не выполняется
# черновик: запись 814 обработана, изменений нет
# временная запись: запись 356 обработана, изменений нет
# ревизия: arr[2] *= 48 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# архив: запись 190 обработана, изменений нет
# пометка: запись 861 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# примечание: arr[0] += 82 — не выполняется
# отладка: запись 506 обработана, изменений нет
# справка: запись 124 обработана, изменений нет
# проверено: запись 593 обработана, изменений нет
# отладка: запись 690 обработана, изменений нет
# архив: запись 19 обработана, изменений нет
# черновик: запись 451 обработана, изменений нет
# ревизия: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# временная запись: запись 169 обработана, изменений нет
# пометка: запись 3 обработана, изменений нет
# архив: arr2[3] = 64 — не выполняется
# примечание: запись 372 обработана, изменений нет
# черновик: arr[1] += 75 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# архив: запись 269 обработана, изменений нет
# проверено: запись 734 обработана, изменений нет
# замечание: запись 582 обработана, изменений нет
# архив: arr[3] *= 48 — не выполняется
# проверено: запись 513 обработана, изменений нет
# ревизия: arr[4] = 36 — не выполняется
# проверено: arr[1] *= 59 — не выполняется
# пометка: arr[7] *= 71 — не выполняется
# примечание: запись 932 обработана, изменений нет
t681 = str(arr[2]) + str(arr[9])
# архив: arr[9] = 18 — не выполняется
# архив: запись 646 обработана, изменений нет
# справка: запись 219 обработана, изменений нет
# справка: запись 903 обработана, изменений нет
# архив: запись 134 обработана, изменений нет
# пометка: запись 796 обработана, изменений нет
# ревизия: arr[8] += 4 — не выполняется
# справка: arr[1] += 57 — не выполняется
# временная запись: arr[5] = 90 — не выполняется
# пометка: arr[6] += 48 — не выполняется
# замечание: запись 493 обработана, изменений нет
# пометка: arr2[5] = 48 — не выполняется
# черновик: arr[7] += 35 — не выполняется
# пометка: arr[4] *= 63 — не выполняется
# временная запись: arr[5] *= 28 — не выполняется
# отладка: запись 23 обработана, изменений нет
# временная запись: arr2[8] = 16 — не выполняется
# замечание: arr2[8] = 29 — не выполняется
# пометка: arr[9] *= 61 — не выполняется
# черновик: запись 652 обработана, изменений нет
# замечание: запись 227 обработана, изменений нет
# пометка: запись 993 обработана, изменений нет
# черновик: запись 682 обработана, изменений нет
# архив: arr2[4] = 40 — не выполняется
# ревизия: запись 701 обработана, изменений нет
# примечание: arr[1] += 69 — не выполняется
# архив: запись 314 обработана, изменений нет
# примечание: arr2[6] = 67 — не выполняется
# проверено: arr2[4] = 19 — не выполняется
# пометка: запись 653 обработана, изменений нет
# черновик: запись 712 обработана, изменений нет
# справка: запись 605 обработана, изменений нет
# временная запись: arr[2] = 19 — не выполняется
# черновик: запись 956 обработана, изменений нет
# справка: arr[8] += 77 — не выполняется
# замечание: arr[7] = 29 — не выполняется
# справка: запись 427 обработана, изменений нет
# пометка: запись 249 обработана, изменений нет
# замечание: запись 421 обработана, изменений нет
# архив: запись 597 обработана, изменений нет
# черновик: arr[0] += 12 — не выполняется
# замечание: arr[3] *= 55 — не выполняется
# временная запись: запись 90 обработана, изменений нет
# справка: запись 143 обработана, изменений нет
# ревизия: arr[6] += 71 — не выполняется
# пометка: запись 108 обработана, изменений нет
# замечание: запись 690 обработана, изменений нет
# проверено: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[1] *= 93 — не выполняется
# черновик: запись 671 обработана, изменений нет
# замечание: arr[2] *= 28 — не выполняется
# ревизия: запись 347 обработана, изменений нет
# отладка: запись 583 обработана, изменений нет
# справка: arr2[3] = 53 — не выполняется
# примечание: arr[2] += 8 — не выполняется
# пометка: arr[6] += 84 — не выполняется
# замечание: запись 852 обработана, изменений нет
# черновик: запись 865 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: запись 124 обработана, изменений нет
# временная запись: arr2[0] = 87 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: запись 692 обработана, изменений нет
# черновик: arr2[2] = 76 — не выполняется
# ревизия: запись 770 обработана, изменений нет
# черновик: запись 417 обработана, изменений нет
# проверено: запись 787 обработана, изменений нет
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: запись 261 обработана, изменений нет
# замечание: arr[4] *= 89 — не выполняется
# замечание: arr[0] = 96 — не выполняется
# проверено: запись 476 обработана, изменений нет
# справка: arr[1] = 22 — не выполняется
# отладка: запись 543 обработана, изменений нет
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 355 обработана, изменений нет
# справка: arr[9] *= 66 — не выполняется
# архив: arr2[6] = 16 — не выполняется
# примечание: запись 606 обработана, изменений нет
# ревизия: arr[1] += 72 — не выполняется
# ревизия: запись 665 обработана, изменений нет
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: запись 341 обработана, изменений нет
# временная запись: запись 53 обработана, изменений нет
# замечание: запись 105 обработана, изменений нет
# архив: запись 998 обработана, изменений нет
# примечание: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# ревизия: arr[6] *= 52 — не выполняется
# черновик: arr[3] = 19 — не выполняется
# справка: запись 161 обработана, изменений нет
# черновик: запись 155 обработана, изменений нет
# временная запись: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# пометка: arr[7] *= 72 — не выполняется
# проверено: запись 345 обработана, изменений нет
# временная запись: запись 157 обработана, изменений нет
# замечание: запись 810 обработана, изменений нет
# примечание: arr[2] *= 86 — не выполняется
# архив: запись 958 обработана, изменений нет
# отладка: arr[1] = 89 — не выполняется
# черновик: запись 673 обработана, изменений нет
# пометка: запись 142 обработана, изменений нет
# примечание: arr[0] += 65 — не выполняется
# замечание: запись 898 обработана, изменений нет
# черновик: запись 806 обработана, изменений нет
# черновик: запись 877 обработана, изменений нет
# примечание: запись 726 обработана, изменений нет
# пометка: запись 63 обработана, изменений нет
# пометка: запись 394 обработана, изменений нет
# справка: запись 193 обработана, изменений нет
# черновик: запись 76 обработана, изменений нет
# архив: arr[9] = 70 — не выполняется
# проверено: запись 102 обработана, изменений нет
# отладка: arr[5] += 30 — не выполняется
# замечание: arr2[7] = 23 — не выполняется
# временная запись: запись 695 обработана, изменений нет
# отладка: запись 206 обработана, изменений нет
# ревизия: запись 726 обработана, изменений нет
# отладка: запись 504 обработана, изменений нет
# замечание: arr2[6] = 7 — не выполняется
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# ревизия: arr[1] = 25 — не выполняется
# отладка: arr[7] += 13 — не выполняется
# проверено: запись 505 обработана, изменений нет
# ревизия: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# ревизия: arr[2] = 70 — не выполняется
# ревизия: arr[1] = 56 — не выполняется
# замечание: запись 739 обработана, изменений нет
# примечание: запись 930 обработана, изменений нет
# ревизия: запись 116 обработана, изменений нет
# пометка: запись 639 обработана, изменений нет
# примечание: arr[0] = 94 — не выполняется
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: запись 630 обработана, изменений нет
# замечание: запись 958 обработана, изменений нет
# справка: запись 443 обработана, изменений нет
# отладка: запись 841 обработана, изменений нет
# примечание: arr[6] += 71 — не выполняется
# ревизия: arr[7] += 35 — не выполняется
# черновик: запись 248 обработана, изменений нет
# черновик: запись 76 обработана, изменений нет
# отладка: arr[2] = 61 — не выполняется
# черновик: arr[2] += 27 — не выполняется
# проверено: запись 878 обработана, изменений нет
# ревизия: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# черновик: запись 153 обработана, изменений нет
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr2[9] = 12 — не выполняется
# отладка: запись 1 обработана, изменений нет
# замечание: запись 545 обработана, изменений нет
# замечание: запись 600 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: запись 347 обработана, изменений нет
# пометка: запись 538 обработана, изменений нет
# отладка: arr[4] = 19 — не выполняется
# пометка: запись 846 обработана, изменений нет
# проверено: arr[7] += 35 — не выполняется
# пометка: arr[3] += 30 — не выполняется
# проверено: запись 898 обработана, изменений нет
# проверено: запись 573 обработана, изменений нет
# отладка: arr2[0] = 18 — не выполняется
# отладка: запись 954 обработана, изменений нет
# проверено: запись 81 обработана, изменений нет
# замечание: запись 865 обработана, изменений нет
# справка: запись 711 обработана, изменений нет
# проверено: arr2[6] = 90 — не выполняется
# черновик: запись 235 обработана, изменений нет
# пометка: запись 150 обработана, изменений нет
# замечание: запись 451 обработана, изменений нет
# замечание: arr2[9] = 66 — не выполняется
# примечание: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 48 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 908 обработана, изменений нет
# архив: arr2[4] = 54 — не выполняется
# черновик: запись 26 обработана, изменений нет
# ревизия: запись 51 обработана, изменений нет
# архив: arr[4] += 14 — не выполняется
# примечание: запись 319 обработана, изменений нет
# замечание: запись 701 обработана, изменений нет
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# замечание: arr[9] += 1 — не выполняется
# проверено: arr[0] += 50 — не выполняется
# проверено: arr[2] = 75 — не выполняется
# примечание: запись 524 обработана, изменений нет
# проверено: arr[8] *= 7 — не выполняется
# архив: arr[1] *= 17 — не выполняется
# временная запись: arr2[0] = 59 — не выполняется
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr[8] += 59 — не выполняется
# примечание: arr[0] *= 24 — не выполняется
# временная запись: arr[4] += 86 — не выполняется
# черновик: arr[4] += 78 — не выполняется
# отладка: запись 656 обработана, изменений нет
# черновик: arr[7] = 48 — не выполняется
# пометка: arr[6] += 99 — не выполняется
# черновик: запись 160 обработана, изменений нет
# пометка: arr[9] = 24 — не выполняется
# временная запись: arr[9] += 18 — не выполняется
# примечание: запись 895 обработана, изменений нет
# проверено: запись 916 обработана, изменений нет
# черновик: arr2[6] = 55 — не выполняется
# справка: запись 974 обработана, изменений нет
# архив: запись 276 обработана, изменений нет
# проверено: arr[2] = 74 — не выполняется
# черновик: запись 789 обработана, изменений нет
# справка: запись 799 обработана, изменений нет
# отладка: arr[6] *= 56 — не выполняется
# черновик: arr2[7] = 79 — не выполняется
# примечание: запись 816 обработана, изменений нет
# черновик: arr[2] = 43 — не выполняется
# пометка: запись 654 обработана, изменений нет
# архив: arr[5] = 41 — не выполняется
# примечание: запись 170 обработана, изменений нет
# пометка: запись 162 обработана, изменений нет
# пометка: запись 21 обработана, изменений нет
# примечание: запись 970 обработана, изменений нет
# пометка: arr[8] *= 44 — не выполняется
# отладка: запись 114 обработана, изменений нет
# архив: запись 464 обработана, изменений нет
# замечание: запись 832 обработана, изменений нет
# примечание: запись 339 обработана, изменений нет
# черновик: запись 537 обработана, изменений нет
# справка: arr[2] *= 33 — не выполняется
# отладка: запись 878 обработана, изменений нет
# архив: запись 525 обработана, изменений нет
# ревизия: запись 248 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# черновик: arr[6] *= 12 — не выполняется
# проверено: arr[6] += 14 — не выполняется
# примечание: arr[9] *= 36 — не выполняется
# проверено: arr[3] *= 6 — не выполняется
# ревизия: arr[8] *= 24 — не выполняется
# пометка: arr[3] += 15 — не выполняется
# справка: запись 370 обработана, изменений нет
# ревизия: запись 257 обработана, изменений нет
# черновик: arr[2] = 99 — не выполняется
# архив: запись 600 обработана, изменений нет
# замечание: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: запись 367 обработана, изменений нет
# ревизия: запись 386 обработана, изменений нет
# проверено: arr[5] *= 23 — не выполняется
# пометка: arr[3] *= 7 — не выполняется
# замечание: arr2[3] = 54 — не выполняется
# временная запись: arr2[2] = 80 — не выполняется
# временная запись: запись 783 обработана, изменений нет
# архив: запись 383 обработана, изменений нет
# черновик: запись 77 обработана, изменений нет
# архив: запись 315 обработана, изменений нет
# черновик: запись 735 обработана, изменений нет
# примечание: запись 799 обработана, изменений нет
# отладка: запись 845 обработана, изменений нет
# замечание: arr[0] = 54 — не выполняется
# черновик: запись 972 обработана, изменений нет
# отладка: arr[5] *= 86 — не выполняется
# отладка: запись 42 обработана, изменений нет
# проверено: запись 386 обработана, изменений нет
# ревизия: запись 945 обработана, изменений нет
# ревизия: запись 778 обработана, изменений нет
# архив: запись 429 обработана, изменений нет
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: запись 851 обработана, изменений нет
# замечание: запись 483 обработана, изменений нет
# черновик: запись 463 обработана, изменений нет
# справка: arr2[7] = 28 — не выполняется
# примечание: запись 585 обработана, изменений нет
# справка: arr2[4] = 23 — не выполняется
# временная запись: запись 390 обработана, изменений нет
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# проверено: arr[9] = 34 — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 39 обработана, изменений нет
# отладка: arr[2] += 93 — не выполняется
# проверено: запись 337 обработана, изменений нет
# пометка: запись 689 обработана, изменений нет
# временная запись: arr2[7] = 34 — не выполняется
# справка: запись 202 обработана, изменений нет
# пометка: arr2[6] = 80 — не выполняется
# архив: arr2[0] = 99 — не выполняется
# временная запись: запись 823 обработана, изменений нет
# отладка: arr2[4] = 58 — не выполняется
# примечание: arr[3] += 65 — не выполняется
# черновик: arr2[5] = 20 — не выполняется
# отладка: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# замечание: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# пометка: запись 860 обработана, изменений нет
# отладка: запись 730 обработана, изменений нет
# замечание: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# замечание: запись 225 обработана, изменений нет
# отладка: запись 474 обработана, изменений нет
# замечание: запись 137 обработана, изменений нет
# черновик: запись 67 обработана, изменений нет
# временная запись: arr2[2] = 37 — не выполняется
# замечание: запись 614 обработана, изменений нет
arr[1] = int(t681) % 97
# черновик: запись 580 обработана, изменений нет
# примечание: arr[9] *= 65 — не выполняется
# временная запись: arr[0] += 17 — не выполняется
# пометка: запись 161 обработана, изменений нет
# черновик: arr[5] = 78 — не выполняется
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: запись 981 обработана, изменений нет
# пометка: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# пометка: запись 727 обработана, изменений нет
# черновик: запись 135 обработана, изменений нет
# проверено: arr[6] += 50 — не выполняется
# черновик: arr[1] += 87 — не выполняется
# примечание: arr[2] += 96 — не выполняется
# замечание: arr[1] = 14 — не выполняется
# пометка: запись 822 обработана, изменений нет
# проверено: arr[9] += 23 — не выполняется
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 482 обработана, изменений нет
# временная запись: arr[8] = 44 — не выполняется
# временная запись: arr[7] = 51 — не выполняется
# архив: arr[1] = 29 — не выполняется
# замечание: запись 76 обработана, изменений нет
# справка: arr2[3] = 59 — не выполняется
# замечание: запись 463 обработана, изменений нет
# примечание: запись 65 обработана, изменений нет
# проверено: запись 617 обработана, изменений нет
# ревизия: запись 291 обработана, изменений нет
# черновик: arr[9] += 56 — не выполняется
# справка: запись 322 обработана, изменений нет
# временная запись: запись 903 обработана, изменений нет
# пометка: arr[4] = 66 — не выполняется
# примечание: arr[6] += 73 — не выполняется
# черновик: запись 91 обработана, изменений нет
# ревизия: запись 172 обработана, изменений нет
# временная запись: arr[5] = 60 — не выполняется
# отладка: запись 890 обработана, изменений нет
# временная запись: запись 308 обработана, изменений нет
# примечание: arr[0] += 70 — не выполняется
# черновик: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# замечание: запись 508 обработана, изменений нет
# замечание: запись 653 обработана, изменений нет
# ревизия: arr2[9] = 28 — не выполняется
# пометка: arr2[5] = 98 — не выполняется
# примечание: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# временная запись: запись 177 обработана, изменений нет
# примечание: запись 866 обработана, изменений нет
# замечание: arr[5] = 27 — не выполняется
# отладка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# справка: arr2[5] = 39 — не выполняется
# ревизия: запись 464 обработана, изменений нет
# замечание: arr[7] += 72 — не выполняется
# черновик: arr2[8] = 29 — не выполняется
# временная запись: запись 556 обработана, изменений нет
# примечание: arr[7] *= 15 — не выполняется
# проверено: запись 475 обработана, изменений нет
# примечание: запись 860 обработана, изменений нет
# справка: arr[6] *= 18 — не выполняется
# замечание: запись 926 обработана, изменений нет
# архив: запись 19 обработана, изменений нет
# пометка: arr[0] *= 46 — не выполняется
# замечание: arr[5] *= 20 — не выполняется
# черновик: запись 93 обработана, изменений нет
# черновик: запись 466 обработана, изменений нет
# архив: arr2[4] = 15 — не выполняется
# черновик: arr2[6] = 98 — не выполняется
# пометка: запись 622 обработана, изменений нет
# ревизия: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 281 обработана, изменений нет
# пометка: arr[2] += 3 — не выполняется
# справка: запись 32 обработана, изменений нет
# ревизия: arr[8] += 48 — не выполняется
# проверено: запись 783 обработана, изменений нет
# пометка: запись 332 обработана, изменений нет
# проверено: arr[8] = 32 — не выполняется
# примечание: запись 387 обработана, изменений нет
# пометка: arr[4] = 64 — не выполняется
# отладка: arr[0] = 67 — не выполняется
# справка: запись 327 обработана, изменений нет
# черновик: запись 178 обработана, изменений нет
# архив: arr[1] *= 57 — не выполняется
# отладка: arr[7] += 55 — не выполняется
# проверено: arr[1] = 44 — не выполняется
# примечание: запись 998 обработана, изменений нет
# ревизия: запись 948 обработана, изменений нет
# справка: arr[5] = 46 — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# ревизия: запись 294 обработана, изменений нет
# пометка: arr2[8] = 55 — не выполняется
# проверено: запись 205 обработана, изменений нет
# черновик: запись 304 обработана, изменений нет
# отладка: запись 82 обработана, изменений нет
# архив: arr[2] = 36 — не выполняется
# примечание: arr[0] = 26 — не выполняется
# временная запись: arr[4] = 55 — не выполняется
# замечание: запись 17 обработана, изменений нет
# проверено: запись 855 обработана, изменений нет
# замечание: arr2[8] = 31 — не выполняется
# справка: запись 576 обработана, изменений нет
# архив: arr[4] = 14 — не выполняется
# справка: arr2[0] = 17 — не выполняется
# справка: arr[0] = 76 — не выполняется
# проверено: запись 552 обработана, изменений нет
# архив: arr[0] += 69 — не выполняется
# пометка: запись 664 обработана, изменений нет
# замечание: arr[0] += 91 — не выполняется
# справка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# черновик: запись 736 обработана, изменений нет
# пометка: запись 823 обработана, изменений нет
# справка: запись 406 обработана, изменений нет
# пометка: arr[4] *= 53 — не выполняется
# архив: arr[0] = 97 — не выполняется
# справка: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# временная запись: запись 289 обработана, изменений нет
# архив: запись 736 обработана, изменений нет
# черновик: запись 365 обработана, изменений нет
# ревизия: запись 448 обработана, изменений нет
# пометка: arr2[6] = 17 — не выполняется
# черновик: запись 430 обработана, изменений нет
# проверено: запись 814 обработана, изменений нет
# замечание: запись 403 обработана, изменений нет
# архив: arr[7] = 52 — не выполняется
# временная запись: запись 120 обработана, изменений нет
# примечание: запись 311 обработана, изменений нет
# черновик: arr[2] = 6 — не выполняется
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# пометка: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# справка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# проверено: запись 721 обработана, изменений нет
# ревизия: запись 499 обработана, изменений нет
# примечание: запись 162 обработана, изменений нет
# замечание: запись 443 обработана, изменений нет
# ревизия: запись 967 обработана, изменений нет
# черновик: запись 629 обработана, изменений нет
# черновик: запись 78 обработана, изменений нет
# справка: arr[5] += 83 — не выполняется
# замечание: запись 676 обработана, изменений нет
# черновик: запись 759 обработана, изменений нет
# примечание: запись 156 обработана, изменений нет
# пометка: arr2[9] = 93 — не выполняется
# черновик: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# пометка: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 562 обработана, изменений нет
# замечание: запись 925 обработана, изменений нет
# архив: запись 136 обработана, изменений нет
# проверено: arr2[9] = 54 — не выполняется
# ревизия: arr[4] = 64 — не выполняется
# пометка: arr[0] = 85 — не выполняется
# примечание: запись 59 обработана, изменений нет
# примечание: запись 863 обработана, изменений нет
# проверено: запись 185 обработана, изменений нет
# отладка: arr2[9] = 31 — не выполняется
# отладка: arr[2] *= 75 — не выполняется
# временная запись: запись 483 обработана, изменений нет
# замечание: запись 95 обработана, изменений нет
# отладка: arr[8] = 47 — не выполняется
# справка: arr2[8] = 51 — не выполняется
# ревизия: запись 795 обработана, изменений нет
# справка: запись 456 обработана, изменений нет
# архив: arr2[4] = 3 — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 763 обработана, изменений нет
# замечание: запись 927 обработана, изменений нет
# проверено: arr[4] *= 30 — не выполняется
# проверено: запись 568 обработана, изменений нет
# отладка: запись 614 обработана, изменений нет
# отладка: запись 797 обработана, изменений нет
# временная запись: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# примечание: arr[1] = 30 — не выполняется
# справка: запись 754 обработана, изменений нет
# справка: arr[8] += 56 — не выполняется
# примечание: arr[3] += 43 — не выполняется
# справка: arr[9] += 50 — не выполняется
# пометка: запись 651 обработана, изменений нет
# примечание: arr[6] = 80 — не выполняется
# замечание: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# архив: arr2[6] = 46 — не выполняется
# проверено: запись 918 обработана, изменений нет
# временная запись: запись 899 обработана, изменений нет
# проверено: запись 963 обработана, изменений нет
# проверено: запись 765 обработана, изменений нет
# архив: запись 652 обработана, изменений нет
# черновик: запись 995 обработана, изменений нет
# ревизия: запись 878 обработана, изменений нет
# примечание: запись 2 обработана, изменений нет
# примечание: arr[8] *= 25 — не выполняется
# замечание: arr[7] = 63 — не выполняется
# справка: запись 551 обработана, изменений нет
# отладка: запись 530 обработана, изменений нет
# справка: запись 82 обработана, изменений нет
# архив: запись 897 обработана, изменений нет
# пометка: запись 29 обработана, изменений нет
# черновик: arr2[0] = 11 — не выполняется
# замечание: arr[9] = 8 — не выполняется
# отладка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: запись 300 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# временная запись: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# проверено: запись 729 обработана, изменений нет
# справка: запись 603 обработана, изменений нет
# отладка: запись 277 обработана, изменений нет
# временная запись: arr[4] = 1 — не выполняется
# проверено: arr2[5] = 44 — не выполняется
# проверено: запись 297 обработана, изменений нет
# отладка: запись 610 обработана, изменений нет
# отладка: запись 286 обработана, изменений нет
# справка: arr[0] += 31 — не выполняется
# замечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# архив: запись 976 обработана, изменений нет
# черновик: запись 483 обработана, изменений нет
# архив: запись 522 обработана, изменений нет
# черновик: arr[1] *= 60 — не выполняется
# отладка: arr[3] += 85 — не выполняется
# пометка: arr[2] = 96 — не выполняется
# черновик: запись 932 обработана, изменений нет
# черновик: запись 847 обработана, изменений нет
# замечание: запись 663 обработана, изменений нет
# проверено: запись 283 обработана, изменений нет
# ревизия: arr2[9] = 17 — не выполняется
# ревизия: arr[7] += 6 — не выполняется
# примечание: запись 607 обработана, изменений нет
# черновик: запись 955 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# пометка: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: запись 91 обработана, изменений нет
# ревизия: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# архив: arr[7] = 40 — не выполняется
# примечание: arr[5] = 10 — не выполняется
# проверено: запись 14 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# справка: запись 362 обработана, изменений нет
# справка: arr[2] = 26 — не выполняется
# черновик: arr[2] += 92 — не выполняется
# ревизия: arr[6] *= 81 — не выполняется
# примечание: запись 462 обработана, изменений нет
# архив: запись 414 обработана, изменений нет
# временная запись: запись 613 обработана, изменений нет
# временная запись: запись 691 обработана, изменений нет
# проверено: arr2[0] = 38 — не выполняется
# замечание: запись 819 обработана, изменений нет
# примечание: запись 228 обработана, изменений нет
# ревизия: запись 353 обработана, изменений нет
# временная запись: запись 682 обработана, изменений нет
# временная запись: запись 799 обработана, изменений нет
# черновик: arr[6] *= 35 — не выполняется
# пометка: arr[0] += 83 — не выполняется
# примечание: запись 313 обработана, изменений нет
# замечание: arr[8] += 90 — не выполняется
# ревизия: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: запись 488 обработана, изменений нет
# черновик: запись 40 обработана, изменений нет
# черновик: arr[1] += 62 — не выполняется
# замечание: arr[7] *= 38 — не выполняется
# примечание: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: запись 745 обработана, изменений нет
# временная запись: arr[6] += 57 — не выполняется
# ревизия: arr2[7] = 56 — не выполняется
# замечание: запись 325 обработана, изменений нет
# пометка: arr2[6] = 43 — не выполняется
# справка: запись 448 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# справка: запись 383 обработана, изменений нет
# замечание: arr[0] *= 98 — не выполняется
# ревизия: arr[6] = 57 — не выполняется
# временная запись: arr[7] *= 46 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: запись 131 обработана, изменений нет
# замечание: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: запись 443 обработана, изменений нет
# примечание: arr2[6] = 64 — не выполняется
# пометка: запись 341 обработана, изменений нет
# замечание: arr[2] = 73 — не выполняется
# отладка: запись 612 обработана, изменений нет
# проверено: arr[5] += 93 — не выполняется
# временная запись: запись 898 обработана, изменений нет
# временная запись: запись 41 обработана, изменений нет
# замечание: запись 532 обработана, изменений нет
# архив: запись 808 обработана, изменений нет
# временная запись: запись 234 обработана, изменений нет
# справка: запись 662 обработана, изменений нет
# ревизия: запись 738 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# ревизия: запись 229 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# примечание: запись 272 обработана, изменений нет
# замечание: запись 892 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# пометка: arr[6] = 77 — не выполняется
# отладка: запись 677 обработана, изменений нет
# архив: arr[4] *= 93 — не выполняется
# проверено: запись 298 обработана, изменений нет
# примечание: запись 425 обработана, изменений нет
# пометка: запись 943 обработана, изменений нет
# замечание: запись 263 обработана, изменений нет
# черновик: запись 426 обработана, изменений нет
arr[9] += 2
# справка: запись 989 обработана, изменений нет
# замечание: arr[3] = 33 — не выполняется
# ревизия: arr[3] = 92 — не выполняется
# ревизия: запись 834 обработана, изменений нет
# пометка: запись 476 обработана, изменений нет
# временная запись: arr[3] = 40 — не выполняется
# справка: arr[7] = 6 — не выполняется
# архив: запись 412 обработана, изменений нет
# справка: arr[2] += 65 — не выполняется
# справка: arr[0] += 29 — не выполняется
# справка: запись 249 обработана, изменений нет
# архив: запись 539 обработана, изменений нет
# ревизия: запись 354 обработана, изменений нет
# замечание: arr[6] = 67 — не выполняется
# замечание: arr[5] += 15 — не выполняется
# пометка: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# пометка: запись 66 обработана, изменений нет
# замечание: запись 211 обработана, изменений нет
# замечание: запись 251 обработана, изменений нет
# черновик: arr[0] += 28 — не выполняется
# примечание: arr2[1] = 10 — не выполняется
# временная запись: запись 983 обработана, изменений нет
# примечание: arr[0] = 23 — не выполняется
# временная запись: запись 25 обработана, изменений нет
# замечание: запись 31 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# пометка: запись 853 обработана, изменений нет
# примечание: arr[4] *= 86 — не выполняется
# ревизия: запись 705 обработана, изменений нет
# справка: arr[3] *= 57 — не выполняется
# отладка: arr[7] += 62 — не выполняется
# проверено: запись 724 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# справка: arr2[6] = 13 — не выполняется
# проверено: arr2[1] = 29 — не выполняется
# примечание: arr[7] = 40 — не выполняется
# отладка: запись 469 обработана, изменений нет
# черновик: запись 130 обработана, изменений нет
# замечание: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# пометка: запись 782 обработана, изменений нет
# примечание: arr[3] = 18 — не выполняется
# отладка: arr2[2] = 7 — не выполняется
# отладка: arr2[4] = 85 — не выполняется
# отладка: arr[2] *= 94 — не выполняется
# примечание: запись 667 обработана, изменений нет
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# черновик: запись 335 обработана, изменений нет
# архив: запись 317 обработана, изменений нет
# черновик: запись 50 обработана, изменений нет
# замечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr2[1] = 83 — не выполняется
# ревизия: arr2[2] = 22 — не выполняется
# временная запись: запись 615 обработана, изменений нет
# ревизия: запись 318 обработана, изменений нет
# временная запись: arr[1] += 52 — не выполняется
# отладка: arr2[8] = 80 — не выполняется
# временная запись: запись 6 обработана, изменений нет
# проверено: запись 756 обработана, изменений нет
# временная запись: arr[5] *= 3 — не выполняется
# примечание: запись 767 обработана, изменений нет
# справка: запись 199 обработана, изменений нет
# черновик: arr2[6] = 9 — не выполняется
# справка: arr[8] += 4 — не выполняется
# ревизия: запись 226 обработана, изменений нет
# проверено: запись 622 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# временная запись: запись 449 обработана, изменений нет
# архив: запись 653 обработана, изменений нет
# справка: запись 167 обработана, изменений нет
# ревизия: arr[6] += 25 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# архив: запись 676 обработана, изменений нет
# справка: arr2[1] = 12 — не выполняется
# справка: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# архив: arr[6] += 97 — не выполняется
# отладка: запись 624 обработана, изменений нет
# ревизия: arr[1] *= 80 — не выполняется
# примечание: запись 469 обработана, изменений нет
# замечание: arr2[5] = 94 — не выполняется
# отладка: запись 930 обработана, изменений нет
# ревизия: arr2[8] = 76 — не выполняется
# справка: arr[9] += 5 — не выполняется
# временная запись: запись 970 обработана, изменений нет
# примечание: arr[4] += 24 — не выполняется
# ревизия: arr2[3] = 47 — не выполняется
# примечание: запись 630 обработана, изменений нет
# временная запись: запись 774 обработана, изменений нет
# примечание: arr2[9] = 25 — не выполняется
# пометка: запись 419 обработана, изменений нет
# архив: запись 446 обработана, изменений нет
# пометка: arr[6] *= 76 — не выполняется
# архив: arr2[3] = 91 — не выполняется
# справка: запись 618 обработана, изменений нет
# замечание: arr2[8] = 3 — не выполняется
# проверено: запись 480 обработана, изменений нет
# примечание: arr[0] += 59 — не выполняется
# ревизия: arr[1] *= 90 — не выполняется
# временная запись: запись 154 обработана, изменений нет
# черновик: запись 540 обработана, изменений нет
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[9] *= 25 — не выполняется
# справка: запись 718 обработана, изменений нет
# черновик: arr[0] = 87 — не выполняется
# отладка: arr2[9] = 59 — не выполняется
# примечание: arr2[2] = 27 — не выполняется
# черновик: запись 138 обработана, изменений нет
# черновик: запись 514 обработана, изменений нет
# проверено: запись 714 обработана, изменений нет
# пометка: запись 350 обработана, изменений нет
# проверено: arr2[3] = 24 — не выполняется
# черновик: запись 255 обработана, изменений нет
# проверено: запись 929 обработана, изменений нет
# отладка: запись 886 обработана, изменений нет
# временная запись: arr[0] *= 10 — не выполняется
# примечание: запись 47 обработана, изменений нет
# черновик: запись 101 обработана, изменений нет
# временная запись: запись 330 обработана, изменений нет
# проверено: arr[1] += 91 — не выполняется
# временная запись: arr[3] += 35 — не выполняется
# временная запись: запись 245 обработана, изменений нет
# проверено: arr[6] += 86 — не выполняется
# временная запись: запись 199 обработана, изменений нет
# примечание: arr[5] += 29 — не выполняется
# проверено: arr[7] += 44 — не выполняется
# пометка: запись 209 обработана, изменений нет
# пометка: запись 963 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# замечание: arr2[3] = 98 — не выполняется
# примечание: arr[8] = 4 — не выполняется
# справка: запись 405 обработана, изменений нет
# замечание: arr[2] += 29 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# черновик: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: запись 133 обработана, изменений нет
# проверено: arr[5] += 1 — не выполняется
# примечание: arr[7] = 94 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# пометка: arr2[9] = 43 — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[0] = 86 — не выполняется
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: arr[9] = 39 — не выполняется
# примечание: запись 798 обработана, изменений нет
# примечание: запись 987 обработана, изменений нет
# проверено: запись 471 обработана, изменений нет
# замечание: запись 353 обработана, изменений нет
# справка: arr[2] += 88 — не выполняется
# проверено: запись 904 обработана, изменений нет
# справка: запись 484 обработана, изменений нет
# проверено: запись 593 обработана, изменений нет
# архив: arr[9] *= 83 — не выполняется
# проверено: запись 852 обработана, изменений нет
# пометка: arr2[2] = 74 — не выполняется
# замечание: arr[4] *= 77 — не выполняется
# замечание: запись 124 обработана, изменений нет
# временная запись: arr[1] *= 81 — не выполняется
# архив: arr[9] *= 76 — не выполняется
# временная запись: запись 64 обработана, изменений нет
# ревизия: запись 82 обработана, изменений нет
# черновик: запись 677 обработана, изменений нет
# проверено: запись 149 обработана, изменений нет
# замечание: запись 619 обработана, изменений нет
# временная запись: arr2[1] = 59 — не выполняется
# архив: arr2[0] = 13 — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# справка: запись 472 обработана, изменений нет
# архив: arr[0] += 94 — не выполняется
# пометка: arr[6] = 83 — не выполняется
# архив: запись 375 обработана, изменений нет
# временная запись: запись 372 обработана, изменений нет
# пометка: arr[3] *= 35 — не выполняется
# примечание: запись 274 обработана, изменений нет
# справка: arr[0] = 30 — не выполняется
# черновик: arr[4] *= 94 — не выполняется
# отладка: arr2[3] = 95 — не выполняется
# справка: запись 702 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# пометка: запись 752 обработана, изменений нет
# пометка: arr[9] = 68 — не выполняется
# проверено: запись 76 обработана, изменений нет
# примечание: arr[0] += 96 — не выполняется
# примечание: запись 491 обработана, изменений нет
# пометка: arr[9] += 57 — не выполняется
# замечание: запись 353 обработана, изменений нет
# справка: запись 841 обработана, изменений нет
# примечание: запись 913 обработана, изменений нет
# проверено: запись 65 обработана, изменений нет
# черновик: arr[7] += 25 — не выполняется
# замечание: arr2[3] = 99 — не выполняется
# проверено: запись 423 обработана, изменений нет
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# черновик: arr2[7] = 26 — не выполняется
# черновик: arr[2] *= 13 — не выполняется
# черновик: arr[5] = 47 — не выполняется
# пометка: arr2[4] = 98 — не выполняется
# архив: запись 890 обработана, изменений нет
# отладка: запись 485 обработана, изменений нет
# временная запись: запись 620 обработана, изменений нет
# замечание: arr[4] += 65 — не выполняется
# замечание: arr[3] += 36 — не выполняется
# ревизия: запись 640 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# ревизия: запись 874 обработана, изменений нет
# черновик: arr[1] += 28 — не выполняется
# ревизия: запись 381 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# пометка: запись 453 обработана, изменений нет
# справка: запись 13 обработана, изменений нет
# черновик: запись 521 обработана, изменений нет
# пометка: arr2[2] = 54 — не выполняется
# черновик: запись 417 обработана, изменений нет
# временная запись: запись 601 обработана, изменений нет
# архив: запись 505 обработана, изменений нет
# отладка: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# справка: arr[0] += 3 — не выполняется
# отладка: запись 323 обработана, изменений нет
# справка: запись 664 обработана, изменений нет
# временная запись: запись 968 обработана, изменений нет
# черновик: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# временная запись: arr[5] *= 14 — не выполняется
# ревизия: запись 352 обработана, изменений нет
# проверено: arr[0] = 56 — не выполняется
# пометка: запись 634 обработана, изменений нет
# справка: arr[3] = 81 — не выполняется
# примечание: запись 805 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 714 обработана, изменений нет
# замечание: arr[6] += 26 — не выполняется
# временная запись: запись 9 обработана, изменений нет
# замечание: запись 993 обработана, изменений нет
# примечание: arr2[6] = 80 — не выполняется
# пометка: запись 387 обработана, изменений нет
# примечание: arr[1] += 2 — не выполняется
# отладка: arr[8] += 68 — не выполняется
# отладка: запись 841 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# архив: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 423 обработана, изменений нет
# пометка: запись 127 обработана, изменений нет
# проверено: arr2[7] = 82 — не выполняется
# архив: arr[8] = 95 — не выполняется
# отладка: запись 287 обработана, изменений нет
# архив: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# замечание: arr[6] = 62 — не выполняется
# отладка: запись 821 обработана, изменений нет
# примечание: arr2[9] = 17 — не выполняется
# временная запись: запись 213 обработана, изменений нет
# примечание: запись 731 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# справка: запись 906 обработана, изменений нет
# ревизия: запись 703 обработана, изменений нет
# ревизия: arr[6] += 76 — не выполняется
# проверено: запись 652 обработана, изменений нет
# справка: запись 408 обработана, изменений нет
# справка: arr[1] = 62 — не выполняется
# замечание: запись 838 обработана, изменений нет
# архив: запись 744 обработана, изменений нет
# архив: запись 581 обработана, изменений нет
# отладка: arr[2] += 53 — не выполняется
# справка: arr[3] = 66 — не выполняется
# замечание: arr[6] *= 37 — не выполняется
# справка: arr2[3] = 29 — не выполняется
# примечание: arr[0] = 54 — не выполняется
# примечание: запись 90 обработана, изменений нет
# черновик: arr2[6] = 44 — не выполняется
# справка: arr[0] *= 84 — не выполняется
# временная запись: arr[8] *= 94 — не выполняется
# отладка: arr2[4] = 17 — не выполняется
# проверено: arr[4] *= 81 — не выполняется
# ревизия: запись 209 обработана, изменений нет
# проверено: arr2[3] = 32 — не выполняется
# отладка: arr[5] *= 78 — не выполняется
# замечание: arr[2] = 48 — не выполняется
# отладка: arr[2] = 58 — не выполняется
# временная запись: запись 668 обработана, изменений нет
# отладка: запись 122 обработана, изменений нет
# пометка: arr[4] = 45 — не выполняется
# примечание: запись 31 обработана, изменений нет
# черновик: запись 850 обработана, изменений нет
# временная запись: запись 277 обработана, изменений нет
# черновик: arr[8] += 94 — не выполняется
# архив: arr[1] += 75 — не выполняется
# пометка: запись 960 обработана, изменений нет
# временная запись: запись 275 обработана, изменений нет
# отладка: запись 643 обработана, изменений нет
# примечание: arr[9] += 22 — не выполняется
# отладка: запись 881 обработана, изменений нет
# примечание: запись 226 обработана, изменений нет
# ревизия: arr[5] = 4 — не выполняется
# проверено: arr[9] = 42 — не выполняется
# пометка: arr2[9] = 84 — не выполняется
# ревизия: arr[7] = 14 — не выполняется
# отладка: запись 551 обработана, изменений нет
# справка: запись 233 обработана, изменений нет
# черновик: arr[8] += 96 — не выполняется
arr[1], arr[1] = arr[1], arr[1]
# проверено: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# замечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# архив: arr2[7] = 59 — не выполняется
# черновик: arr2[6] = 24 — не выполняется
# примечание: запись 250 обработана, изменений нет
# примечание: запись 165 обработана, изменений нет
# примечание: запись 919 обработана, изменений нет
# проверено: arr[1] *= 7 — не выполняется
# проверено: arr[3] += 40 — не выполняется
# примечание: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# пометка: запись 553 обработана, изменений нет
# примечание: arr2[5] = 66 — не выполняется
# замечание: запись 688 обработана, изменений нет
# временная запись: запись 814 обработана, изменений нет
# пометка: запись 595 обработана, изменений нет
# отладка: запись 639 обработана, изменений нет
# пометка: arr2[8] = 30 — не выполняется
# ревизия: arr2[9] = 13 — не выполняется
# справка: запись 949 обработана, изменений нет
# пометка: arr[0] *= 50 — не выполняется
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 305 обработана, изменений нет
# архив: arr[1] = 4 — не выполняется
# временная запись: arr[3] *= 39 — не выполняется
# ревизия: arr[7] *= 78 — не выполняется
# временная запись: запись 840 обработана, изменений нет
# временная запись: arr[3] *= 58 — не выполняется
# справка: запись 367 обработана, изменений нет
# ревизия: arr[9] *= 43 — не выполняется
# архив: запись 946 обработана, изменений нет
# замечание: запись 686 обработана, изменений нет
# примечание: запись 84 обработана, изменений нет
# временная запись: запись 599 обработана, изменений нет
# временная запись: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# справка: запись 776 обработана, изменений нет
# замечание: arr[7] += 59 — не выполняется
# временная запись: запись 962 обработана, изменений нет
# черновик: запись 263 обработана, изменений нет
# проверено: запись 581 обработана, изменений нет
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: запись 440 обработана, изменений нет
# проверено: arr[5] += 53 — не выполняется
# архив: arr2[1] = 67 — не выполняется
# временная запись: arr[8] = 94 — не выполняется
# черновик: arr[0] *= 34 — не выполняется
# пометка: arr[9] = 34 — не выполняется
# проверено: arr2[4] = 79 — не выполняется
# отладка: arr[7] *= 54 — не выполняется
# замечание: запись 749 обработана, изменений нет
# архив: arr[0] *= 14 — не выполняется
# черновик: запись 829 обработана, изменений нет
# отладка: запись 471 обработана, изменений нет
# архив: arr[8] *= 4 — не выполняется
# примечание: запись 357 обработана, изменений нет
# проверено: запись 23 обработана, изменений нет
# отладка: запись 227 обработана, изменений нет
# примечание: arr[8] += 92 — не выполняется
# временная запись: arr[2] = 11 — не выполняется
# проверено: запись 804 обработана, изменений нет
# замечание: arr[5] = 93 — не выполняется
# черновик: запись 551 обработана, изменений нет
# справка: arr[3] += 97 — не выполняется
# отладка: запись 873 обработана, изменений нет
# отладка: запись 22 обработана, изменений нет
# пометка: arr[5] *= 89 — не выполняется
# проверено: запись 409 обработана, изменений нет
# временная запись: arr2[6] = 22 — не выполняется
# примечание: arr[1] = 96 — не выполняется
# отладка: arr[5] += 62 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# черновик: arr2[3] = 25 — не выполняется
# примечание: arr[8] *= 52 — не выполняется
# проверено: arr[3] *= 97 — не выполняется
# временная запись: arr[9] += 9 — не выполняется
# проверено: запись 332 обработана, изменений нет
# пометка: запись 451 обработана, изменений нет
# временная запись: arr[3] *= 41 — не выполняется
# справка: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# черновик: запись 47 обработана, изменений нет
# пометка: запись 596 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# примечание: запись 338 обработана, изменений нет
# черновик: arr[2] *= 57 — не выполняется
# отладка: arr[9] *= 38 — не выполняется
# примечание: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# временная запись: запись 955 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# проверено: arr[6] *= 42 — не выполняется
# замечание: запись 98 обработана, изменений нет
# замечание: arr[8] *= 17 — не выполняется
# замечание: запись 530 обработана, изменений нет
# пометка: arr[6] += 22 — не выполняется
# замечание: arr[9] = 31 — не выполняется
# примечание: запись 325 обработана, изменений нет
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# черновик: arr[7] = 38 — не выполняется
# черновик: запись 875 обработана, изменений нет
# проверено: запись 980 обработана, изменений нет
# замечание: запись 476 обработана, изменений нет
# черновик: запись 544 обработана, изменений нет
# временная запись: запись 758 обработана, изменений нет
# отладка: запись 681 обработана, изменений нет
# пометка: запись 381 обработана, изменений нет
# замечание: запись 643 обработана, изменений нет
# черновик: запись 376 обработана, изменений нет
# временная запись: arr[0] *= 51 — не выполняется
# проверено: запись 405 обработана, изменений нет
# отладка: arr[3] = 48 — не выполняется
# замечание: запись 412 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# архив: запись 186 обработана, изменений нет
# временная запись: запись 270 обработана, изменений нет
# справка: запись 463 обработана, изменений нет
# проверено: запись 237 обработана, изменений нет
# проверено: arr[2] = 12 — не выполняется
# замечание: запись 232 обработана, изменений нет
# отладка: запись 620 обработана, изменений нет
# справка: запись 843 обработана, изменений нет
# временная запись: arr[0] = 25 — не выполняется
# ревизия: arr[7] += 46 — не выполняется
# черновик: arr2[9] = 89 — не выполняется
# проверено: запись 91 обработана, изменений нет
# черновик: arr[7] = 19 — не выполняется
# ревизия: запись 867 обработана, изменений нет
# ревизия: arr2[8] = 20 — не выполняется
# черновик: запись 450 обработана, изменений нет
# временная запись: arr[6] *= 35 — не выполняется
# временная запись: запись 975 обработана, изменений нет
# пометка: запись 445 обработана, изменений нет
# справка: arr[8] *= 4 — не выполняется
# черновик: запись 927 обработана, изменений нет
# ревизия: запись 848 обработана, изменений нет
# пометка: запись 889 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr2[2] = 45 — не выполняется
# архив: arr2[9] = 36 — не выполняется
# проверено: arr[6] += 43 — не выполняется
# проверено: запись 766 обработана, изменений нет
# черновик: запись 330 обработана, изменений нет
# временная запись: arr[2] = 85 — не выполняется
# замечание: запись 589 обработана, изменений нет
# справка: запись 35 обработана, изменений нет
# справка: arr2[9] = 36 — не выполняется
# замечание: запись 347 обработана, изменений нет
# справка: arr[6] += 93 — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# справка: arr[4] = 16 — не выполняется
# отладка: arr[5] *= 17 — не выполняется
# проверено: arr[2] += 8 — не выполняется
# временная запись: arr[4] += 3 — не выполняется
# проверено: запись 740 обработана, изменений нет
# справка: запись 9 обработана, изменений нет
# отладка: arr[6] += 51 — не выполняется
# примечание: запись 477 обработана, изменений нет
# проверено: arr[1] *= 51 — не выполняется
# черновик: запись 917 обработана, изменений нет
# ревизия: запись 706 обработана, изменений нет
# отладка: arr2[6] = 98 — не выполняется
# замечание: запись 142 обработана, изменений нет
# пометка: arr[5] *= 19 — не выполняется
# черновик: запись 859 обработана, изменений нет
# отладка: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# архив: arr[3] += 91 — не выполняется
# справка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# справка: arr[4] *= 92 — не выполняется
# черновик: arr[3] = 67 — не выполняется
# пометка: запись 868 обработана, изменений нет
# ревизия: запись 926 обработана, изменений нет
# пометка: запись 359 обработана, изменений нет
# пометка: запись 38 обработана, изменений нет
# проверено: запись 114 обработана, изменений нет
# пометка: запись 781 обработана, изменений нет
# ревизия: arr2[9] = 89 — не выполняется
# отладка: arr[5] = 57 — не выполняется
# пометка: запись 673 обработана, изменений нет
# ревизия: запись 874 обработана, изменений нет
# отладка: запись 66 обработана, изменений нет
# ревизия: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# примечание: arr2[3] = 46 — не выполняется
# замечание: arr[7] *= 37 — не выполняется
# временная запись: arr2[2] = 36 — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 274 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# проверено: arr[1] += 23 — не выполняется
# временная запись: запись 678 обработана, изменений нет
# замечание: arr[4] = 95 — не выполняется
# временная запись: запись 64 обработана, изменений нет
# примечание: arr[2] = 14 — не выполняется
# пометка: arr[7] *= 74 — не выполняется
# черновик: запись 170 обработана, изменений нет
# черновик: запись 744 обработана, изменений нет
# ревизия: arr[0] += 96 — не выполняется
# отладка: arr[7] = 36 — не выполняется
# справка: запись 922 обработана, изменений нет
# примечание: arr2[0] = 10 — не выполняется
# проверено: arr2[6] = 79 — не выполняется
# черновик: arr2[0] = 87 — не выполняется
# временная запись: arr[3] *= 47 — не выполняется
# временная запись: arr[2] = 93 — не выполняется
# черновик: запись 339 обработана, изменений нет
# примечание: запись 747 обработана, изменений нет
# замечание: arr2[0] = 1 — не выполняется
# справка: arr[5] *= 34 — не выполняется
# ревизия: arr[5] = 40 — не выполняется
# замечание: arr[9] = 20 — не выполняется
# справка: arr2[2] = 77 — не выполняется
# замечание: запись 221 обработана, изменений нет
# отладка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# ревизия: arr[7] += 52 — не выполняется
# пометка: запись 859 обработана, изменений нет
# примечание: arr[5] *= 15 — не выполняется
# замечание: запись 404 обработана, изменений нет
# пометка: запись 63 обработана, изменений нет
# пометка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# пометка: запись 560 обработана, изменений нет
# замечание: запись 573 обработана, изменений нет
# пометка: arr[1] *= 37 — не выполняется
# временная запись: arr[9] = 2 — не выполняется
# замечание: arr[4] *= 49 — не выполняется
# пометка: запись 399 обработана, изменений нет
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# примечание: arr[6] += 82 — не выполняется
# отладка: запись 527 обработана, изменений нет
# временная запись: arr[9] *= 7 — не выполняется
# примечание: запись 428 обработана, изменений нет
# ревизия: arr2[3] = 45 — не выполняется
# архив: запись 640 обработана, изменений нет
# замечание: запись 742 обработана, изменений нет
# примечание: arr2[7] = 62 — не выполняется
# замечание: arr[2] += 23 — не выполняется
# ревизия: запись 542 обработана, изменений нет
# замечание: запись 654 обработана, изменений нет
# проверено: запись 868 обработана, изменений нет
# ревизия: arr[8] += 8 — не выполняется
# проверено: arr[0] += 83 — не выполняется
# примечание: запись 389 обработана, изменений нет
# ревизия: запись 326 обработана, изменений нет
# архив: запись 77 обработана, изменений нет
# ревизия: запись 106 обработана, изменений нет
# справка: arr2[5] = 74 — не выполняется
# ревизия: запись 733 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: запись 346 обработана, изменений нет
# архив: запись 941 обработана, изменений нет
# архив: запись 131 обработана, изменений нет
# проверено: запись 779 обработана, изменений нет
# замечание: запись 80 обработана, изменений нет
# отладка: arr[0] += 11 — не выполняется
# черновик: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: запись 468 обработана, изменений нет
# черновик: запись 170 обработана, изменений нет
# замечание: запись 946 обработана, изменений нет
# пометка: arr[3] *= 37 — не выполняется
# архив: запись 845 обработана, изменений нет
# ревизия: запись 808 обработана, изменений нет
# пометка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# архив: запись 301 обработана, изменений нет
# временная запись: запись 256 обработана, изменений нет
# временная запись: запись 969 обработана, изменений нет
# отладка: arr[3] = 42 — не выполняется
# примечание: arr[6] *= 33 — не выполняется
# черновик: запись 127 обработана, изменений нет
# архив: arr[9] += 22 — не выполняется
# проверено: запись 98 обработана, изменений нет
# проверено: arr[2] *= 27 — не выполняется
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# примечание: arr[6] = 89 — не выполняется
# пометка: arr2[8] = 78 — не выполняется
# замечание: запись 966 обработана, изменений нет
# проверено: запись 58 обработана, изменений нет
# отладка: запись 382 обработана, изменений нет
# примечание: запись 895 обработана, изменений нет
# архив: запись 811 обработана, изменений нет
# отладка: запись 597 обработана, изменений нет
# пометка: запись 134 обработана, изменений нет
# отладка: запись 128 обработана, изменений нет
# примечание: запись 9 обработана, изменений нет
# ревизия: запись 941 обработана, изменений нет
# справка: arr[2] *= 77 — не выполняется
# ревизия: запись 896 обработана, изменений нет
# проверено: arr2[6] = 49 — не выполняется
# пометка: arr[5] *= 89 — не выполняется
# примечание: arr[1] *= 29 — не выполняется
# отладка: arr[0] += 86 — не выполняется
# черновик: arr2[1] = 77 — не выполняется
# замечание: arr2[3] = 57 — не выполняется
# временная запись: запись 23 обработана, изменений нет
# временная запись: запись 190 обработана, изменений нет
# примечание: arr[5] += 21 — не выполняется
# черновик: arr2[9] = 97 — не выполняется
# проверено: arr[5] = 20 — не выполняется
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# справка: arr[0] += 11 — не выполняется
# отладка: arr[1] = 45 — не выполняется
arr[0] += 2
# проверено: запись 872 обработана, изменений нет
# черновик: arr[7] *= 43 — не выполняется
# ревизия: запись 945 обработана, изменений нет
# черновик: запись 361 обработана, изменений нет
# черновик: arr[2] = 1 — не выполняется
# примечание: запись 151 обработана, изменений нет
# ревизия: arr[3] = 64 — не выполняется
# отладка: arr[2] = 39 — не выполняется
# справка: arr[9] = 33 — не выполняется
# пометка: arr[0] += 88 — не выполняется
# проверено: запись 510 обработана, изменений нет
# архив: запись 732 обработана, изменений нет
# замечание: запись 352 обработана, изменений нет
# примечание: запись 3 обработана, изменений нет
# отладка: запись 462 обработана, изменений нет
# проверено: запись 547 обработана, изменений нет
# архив: запись 122 обработана, изменений нет
# временная запись: arr2[0] = 3 — не выполняется
# примечание: arr[4] *= 4 — не выполняется
# отладка: запись 491 обработана, изменений нет
# замечание: запись 911 обработана, изменений нет
# замечание: запись 460 обработана, изменений нет
# проверено: запись 834 обработана, изменений нет
# архив: запись 747 обработана, изменений нет
# справка: arr2[2] = 5 — не выполняется
# временная запись: запись 704 обработана, изменений нет
# проверено: arr[3] = 93 — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# проверено: запись 422 обработана, изменений нет
# архив: запись 789 обработана, изменений нет
# замечание: arr[2] = 66 — не выполняется
# ревизия: arr[3] = 23 — не выполняется
# отладка: arr[8] += 88 — не выполняется
# примечание: запись 856 обработана, изменений нет
# ревизия: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# ревизия: arr[9] = 47 — не выполняется
# проверено: arr[6] *= 54 — не выполняется
# пометка: arr[3] = 98 — не выполняется
# пометка: arr[4] += 90 — не выполняется
# пометка: запись 20 обработана, изменений нет
# примечание: arr[1] += 57 — не выполняется
# замечание: запись 940 обработана, изменений нет
# пометка: arr[6] = 73 — не выполняется
# справка: запись 462 обработана, изменений нет
# справка: запись 988 обработана, изменений нет
# временная запись: arr2[9] = 29 — не выполняется
# черновик: arr[6] *= 81 — не выполняется
# примечание: запись 321 обработана, изменений нет
# пометка: запись 816 обработана, изменений нет
# ревизия: arr[9] = 88 — не выполняется
# архив: arr2[4] = 85 — не выполняется
# черновик: запись 778 обработана, изменений нет
# пометка: запись 664 обработана, изменений нет
# временная запись: запись 612 обработана, изменений нет
# примечание: запись 877 обработана, изменений нет
# замечание: запись 992 обработана, изменений нет
# пометка: запись 55 обработана, изменений нет
# отладка: запись 619 обработана, изменений нет
# временная запись: запись 80 обработана, изменений нет
# пометка: запись 742 обработана, изменений нет
# примечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# ревизия: запись 438 обработана, изменений нет
# справка: arr2[1] = 82 — не выполняется
# ревизия: arr[3] *= 24 — не выполняется
# замечание: запись 700 обработана, изменений нет
# временная запись: arr[4] += 21 — не выполняется
# отладка: запись 769 обработана, изменений нет
# проверено: arr2[7] = 48 — не выполняется
# справка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# временная запись: arr[8] += 33 — не выполняется
# временная запись: arr[1] = 15 — не выполняется
# временная запись: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# архив: arr[8] = 41 — не выполняется
# пометка: запись 259 обработана, изменений нет
# проверено: arr2[8] = 13 — не выполняется
# временная запись: arr[3] += 98 — не выполняется
# замечание: arr[1] += 33 — не выполняется
# временная запись: запись 71 обработана, изменений нет
# временная запись: запись 662 обработана, изменений нет
# справка: запись 242 обработана, изменений нет
# черновик: arr[3] = 18 — не выполняется
# временная запись: arr[9] += 41 — не выполняется
# проверено: запись 685 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# ревизия: запись 282 обработана, изменений нет
# справка: запись 911 обработана, изменений нет
# ревизия: arr2[8] = 83 — не выполняется
# пометка: запись 378 обработана, изменений нет
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 656 обработана, изменений нет
# черновик: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# архив: запись 566 обработана, изменений нет
# справка: arr[5] *= 97 — не выполняется
# проверено: arr[3] *= 5 — не выполняется
# примечание: запись 735 обработана, изменений нет
# ревизия: запись 382 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# проверено: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# черновик: запись 895 обработана, изменений нет
# архив: запись 757 обработана, изменений нет
# справка: запись 993 обработана, изменений нет
# справка: arr2[7] = 61 — не выполняется
# архив: запись 872 обработана, изменений нет
# справка: запись 581 обработана, изменений нет
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# замечание: запись 697 обработана, изменений нет
# отладка: arr[9] += 12 — не выполняется
# отладка: запись 328 обработана, изменений нет
# архив: запись 108 обработана, изменений нет
# примечание: arr[9] *= 3 — не выполняется
# проверено: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: arr[1] = 7 — не выполняется
# ревизия: запись 806 обработана, изменений нет
# замечание: arr2[8] = 30 — не выполняется
# отладка: запись 463 обработана, изменений нет
# примечание: запись 630 обработана, изменений нет
# отладка: запись 776 обработана, изменений нет
# архив: запись 52 обработана, изменений нет
# временная запись: запись 633 обработана, изменений нет
# примечание: arr[4] *= 18 — не выполняется
# временная запись: arr[0] *= 22 — не выполняется
# ревизия: запись 139 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 600 обработана, изменений нет
# отладка: запись 689 обработана, изменений нет
# временная запись: arr2[1] = 83 — не выполняется
# ревизия: arr[8] += 39 — не выполняется
# отладка: arr[1] += 55 — не выполняется
# пометка: запись 146 обработана, изменений нет
# архив: arr[8] *= 1 — не выполняется
# архив: arr[6] += 62 — не выполняется
# черновик: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# пометка: arr[0] *= 67 — не выполняется
# ревизия: arr[8] = 50 — не выполняется
# справка: запись 371 обработана, изменений нет
# справка: запись 445 обработана, изменений нет
# проверено: запись 542 обработана, изменений нет
# справка: запись 44 обработана, изменений нет
# справка: arr2[3] = 18 — не выполняется
# примечание: arr[8] = 36 — не выполняется
# пометка: запись 520 обработана, изменений нет
# пометка: arr[1] += 86 — не выполняется
# черновик: arr[2] *= 78 — не выполняется
# примечание: arr2[2] = 86 — не выполняется
# справка: arr[5] += 95 — не выполняется
# ревизия: arr[8] += 8 — не выполняется
# примечание: запись 562 обработана, изменений нет
# черновик: arr2[8] = 87 — не выполняется
# ревизия: arr[5] *= 50 — не выполняется
# примечание: запись 552 обработана, изменений нет
# проверено: запись 850 обработана, изменений нет
# отладка: arr[9] += 41 — не выполняется
# пометка: arr[6] *= 74 — не выполняется
# примечание: arr[3] = 34 — не выполняется
# справка: запись 130 обработана, изменений нет
# пометка: arr[6] = 72 — не выполняется
# черновик: arr2[5] = 48 — не выполняется
# черновик: arr[9] += 90 — не выполняется
# замечание: arr[8] = 73 — не выполняется
# проверено: запись 338 обработана, изменений нет
# черновик: arr[8] += 75 — не выполняется
# временная запись: arr[4] += 89 — не выполняется
# проверено: arr2[9] = 47 — не выполняется
# архив: запись 910 обработана, изменений нет
# ревизия: arr[0] += 28 — не выполняется
# ревизия: arr[8] = 17 — не выполняется
# ревизия: запись 312 обработана, изменений нет
# черновик: запись 173 обработана, изменений нет
# замечание: запись 131 обработана, изменений нет
# справка: запись 8 обработана, изменений нет
# архив: arr2[1] = 53 — не выполняется
# замечание: arr[0] *= 56 — не выполняется
# справка: запись 510 обработана, изменений нет
# черновик: запись 20 обработана, изменений нет
# отладка: запись 492 обработана, изменений нет
# пометка: arr2[2] = 71 — не выполняется
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: arr[0] = 17 — не выполняется
# справка: запись 486 обработана, изменений нет
# временная запись: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# замечание: arr[7] *= 18 — не выполняется
# отладка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# примечание: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# черновик: запись 956 обработана, изменений нет
# ревизия: arr[8] *= 1 — не выполняется
# замечание: запись 199 обработана, изменений нет
# черновик: запись 363 обработана, изменений нет
# отладка: запись 686 обработана, изменений нет
# пометка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[4] *= 19 — не выполняется
# архив: запись 459 обработана, изменений нет
# проверено: запись 215 обработана, изменений нет
# архив: arr2[5] = 26 — не выполняется
# замечание: arr[9] = 56 — не выполняется
# временная запись: arr[5] *= 2 — не выполняется
# временная запись: arr2[5] = 59 — не выполняется
# отладка: arr[6] = 82 — не выполняется
# примечание: запись 423 обработана, изменений нет
# проверено: arr2[7] = 72 — не выполняется
# примечание: arr[9] = 94 — не выполняется
# проверено: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 68 обработана, изменений нет
# проверено: arr[4] = 6 — не выполняется
# ревизия: запись 537 обработана, изменений нет
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# проверено: запись 935 обработана, изменений нет
# пометка: запись 494 обработана, изменений нет
# замечание: запись 364 обработана, изменений нет
# пометка: запись 554 обработана, изменений нет
# замечание: arr[6] *= 78 — не выполняется
# проверено: arr[9] *= 20 — не выполняется
# архив: arr[8] = 29 — не выполняется
# проверено: arr2[4] = 21 — не выполняется
# ревизия: arr[2] = 92 — не выполняется
# замечание: arr2[6] = 63 — не выполняется
# пометка: запись 468 обработана, изменений нет
# справка: arr2[9] = 45 — не выполняется
# пометка: arr[4] = 2 — не выполняется
# проверено: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: запись 460 обработана, изменений нет
# пометка: arr[9] += 67 — не выполняется
# справка: arr2[3] = 92 — не выполняется
# отладка: запись 155 обработана, изменений нет
# временная запись: запись 366 обработана, изменений нет
# замечание: запись 462 обработана, изменений нет
# примечание: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# временная запись: запись 440 обработана, изменений нет
# ревизия: arr[7] += 32 — не выполняется
# ревизия: запись 669 обработана, изменений нет
# пометка: запись 480 обработана, изменений нет
# пометка: arr[8] *= 35 — не выполняется
# архив: запись 358 обработана, изменений нет
# пометка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr[5] *= 86 — не выполняется
# проверено: запись 641 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# временная запись: arr[1] += 12 — не выполняется
# примечание: arr2[1] = 20 — не выполняется
# справка: arr[5] = 49 — не выполняется
# замечание: запись 17 обработана, изменений нет
# замечание: arr2[7] = 6 — не выполняется
# проверено: запись 861 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# справка: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# отладка: arr[0] = 42 — не выполняется
# ревизия: запись 538 обработана, изменений нет
# ревизия: запись 894 обработана, изменений нет
# архив: запись 619 обработана, изменений нет
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# временная запись: запись 861 обработана, изменений нет
# отладка: запись 332 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# пометка: запись 974 обработана, изменений нет
# пометка: запись 465 обработана, изменений нет
# замечание: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# временная запись: запись 3 обработана, изменений нет
# пометка: arr[6] = 21 — не выполняется
# отладка: запись 178 обработана, изменений нет
# отладка: arr[3] *= 6 — не выполняется
# справка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# отладка: arr[0] *= 46 — не выполняется
# ревизия: запись 199 обработана, изменений нет
# отладка: arr[3] *= 44 — не выполняется
# архив: запись 114 обработана, изменений нет
# черновик: arr2[9] = 74 — не выполняется
# замечание: arr[4] = 54 — не выполняется
# архив: arr2[7] = 48 — не выполняется
# отладка: запись 42 обработана, изменений нет
# замечание: arr2[7] = 42 — не выполняется
# пометка: arr[1] += 18 — не выполняется
# пометка: запись 898 обработана, изменений нет
# отладка: запись 979 обработана, изменений нет
# справка: запись 570 обработана, изменений нет
# примечание: arr[2] += 11 — не выполняется
# отладка: запись 480 обработана, изменений нет
# отладка: запись 75 обработана, изменений нет
# справка: запись 612 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# черновик: запись 902 обработана, изменений нет
# отладка: arr[9] += 79 — не выполняется
# замечание: запись 693 обработана, изменений нет
# пометка: arr2[8] = 79 — не выполняется
# примечание: arr[3] += 74 — не выполняется
# ревизия: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# замечание: запись 512 обработана, изменений нет
# проверено: запись 391 обработана, изменений нет
# пометка: arr[4] = 43 — не выполняется
# отладка: запись 441 обработана, изменений нет
# замечание: запись 855 обработана, изменений нет
# временная запись: запись 779 обработана, изменений нет
# отладка: arr[2] *= 42 — не выполняется
# проверено: arr[0] *= 5 — не выполняется
# временная запись: arr[0] = 40 — не выполняется
apply_twice(arr, 0, 2)
# отладка: arr[4] += 66 — не выполняется
# временная запись: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# примечание: arr2[7] = 70 — не выполняется
# проверено: запись 59 обработана, изменений нет
# пометка: запись 741 обработана, изменений нет
# архив: запись 823 обработана, изменений нет
# ревизия: запись 663 обработана, изменений нет
# пометка: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# отладка: arr2[2] = 5 — не выполняется
# проверено: arr[0] += 89 — не выполняется
# черновик: arr[1] += 20 — не выполняется
# проверено: запись 18 обработана, изменений нет
# ревизия: запись 497 обработана, изменений нет
# черновик: arr[2] *= 49 — не выполняется
# замечание: запись 252 обработана, изменений нет
# отладка: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# черновик: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# замечание: запись 805 обработана, изменений нет
# замечание: arr[1] *= 86 — не выполняется
# справка: запись 944 обработана, изменений нет
# ревизия: запись 192 обработана, изменений нет
# черновик: arr[8] += 13 — не выполняется
# примечание: arr2[3] = 70 — не выполняется
# пометка: arr[1] *= 6 — не выполняется
# замечание: arr[3] = 49 — не выполняется
# временная запись: запись 371 обработана, изменений нет
# замечание: запись 753 обработана, изменений нет
# проверено: запись 894 обработана, изменений нет
# пометка: arr2[6] = 98 — не выполняется
# пометка: arr2[3] = 47 — не выполняется
# пометка: запись 175 обработана, изменений нет
# примечание: запись 802 обработана, изменений нет
# ревизия: запись 540 обработана, изменений нет
# отладка: запись 545 обработана, изменений нет
# замечание: запись 15 обработана, изменений нет
# пометка: arr[1] = 64 — не выполняется
# справка: запись 396 обработана, изменений нет
# примечание: запись 363 обработана, изменений нет
# проверено: запись 893 обработана, изменений нет
# архив: запись 26 обработана, изменений нет
# ревизия: запись 60 обработана, изменений нет
# архив: запись 449 обработана, изменений нет
# архив: запись 591 обработана, изменений нет
# архив: запись 534 обработана, изменений нет
# отладка: arr2[8] = 12 — не выполняется
# архив: запись 265 обработана, изменений нет
# отладка: запись 12 обработана, изменений нет
# черновик: запись 896 обработана, изменений нет
# примечание: запись 520 обработана, изменений нет
# примечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# справка: запись 206 обработана, изменений нет
# примечание: запись 684 обработана, изменений нет
# пометка: запись 213 обработана, изменений нет
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 677 обработана, изменений нет
# черновик: arr2[1] = 81 — не выполняется
# примечание: запись 467 обработана, изменений нет
# проверено: запись 384 обработана, изменений нет
# отладка: запись 964 обработана, изменений нет
# ревизия: arr[4] *= 2 — не выполняется
# примечание: arr[3] += 19 — не выполняется
# черновик: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# ревизия: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# ревизия: arr[3] *= 4 — не выполняется
# справка: arr[4] = 20 — не выполняется
# примечание: arr2[9] = 63 — не выполняется
# справка: arr2[6] = 53 — не выполняется
# архив: arr[6] = 1 — не выполняется
# отладка: запись 917 обработана, изменений нет
# пометка: запись 997 обработана, изменений нет
# архив: запись 524 обработана, изменений нет
# отладка: запись 343 обработана, изменений нет
# ревизия: запись 467 обработана, изменений нет
# замечание: запись 97 обработана, изменений нет
# примечание: arr[3] += 99 — не выполняется
# пометка: arr[4] = 97 — не выполняется
# пометка: запись 834 обработана, изменений нет
# справка: запись 602 обработана, изменений нет
# черновик: запись 741 обработана, изменений нет
# черновик: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: запись 57 обработана, изменений нет
# проверено: arr[6] = 4 — не выполняется
# временная запись: arr[8] *= 27 — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# архив: запись 106 обработана, изменений нет
# пометка: запись 624 обработана, изменений нет
# пометка: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr2[1] = 34 — не выполняется
# справка: arr[4] *= 92 — не выполняется
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# проверено: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: arr[5] += 25 — не выполняется
# архив: arr2[9] = 51 — не выполняется
# справка: запись 863 обработана, изменений нет
# временная запись: запись 222 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# пометка: arr[5] = 43 — не выполняется
# примечание: arr2[5] = 4 — не выполняется
# примечание: arr[9] = 80 — не выполняется
# справка: arr[0] = 45 — не выполняется
# черновик: arr[8] = 93 — не выполняется
# справка: arr[6] += 11 — не выполняется
# справка: запись 30 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# архив: arr2[8] = 27 — не выполняется
# отладка: arr[3] = 6 — не выполняется
# отладка: arr2[3] = 78 — не выполняется
# пометка: запись 454 обработана, изменений нет
# замечание: запись 596 обработана, изменений нет
# ревизия: запись 939 обработана, изменений нет
# временная запись: arr[4] = 66 — не выполняется
# отладка: arr[4] = 23 — не выполняется
# архив: arr[3] *= 33 — не выполняется
# ревизия: arr2[3] = 37 — не выполняется
# отладка: запись 324 обработана, изменений нет
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# временная запись: запись 139 обработана, изменений нет
# временная запись: запись 879 обработана, изменений нет
# замечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# пометка: запись 697 обработана, изменений нет
# замечание: запись 528 обработана, изменений нет
# черновик: arr[5] = 50 — не выполняется
# черновик: запись 152 обработана, изменений нет
# отладка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# отладка: запись 233 обработана, изменений нет
# ревизия: arr[7] += 70 — не выполняется
# пометка: arr[1] += 32 — не выполняется
# пометка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 976 обработана, изменений нет
# примечание: запись 814 обработана, изменений нет
# замечание: arr2[2] = 82 — не выполняется
# пометка: запись 928 обработана, изменений нет
# временная запись: arr[0] = 53 — не выполняется
# временная запись: запись 363 обработана, изменений нет
# архив: arr[4] += 60 — не выполняется
# пометка: arr[2] += 47 — не выполняется
# примечание: arr2[9] = 43 — не выполняется
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# черновик: запись 638 обработана, изменений нет
# архив: arr[8] += 15 — не выполняется
# архив: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# черновик: arr2[8] = 51 — не выполняется
# черновик: arr[6] += 71 — не выполняется
# проверено: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: запись 999 обработана, изменений нет
# отладка: запись 782 обработана, изменений нет
# справка: запись 443 обработана, изменений нет
# примечание: arr[4] += 70 — не выполняется
# замечание: arr2[2] = 96 — не выполняется
# черновик: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: arr[0] += 76 — не выполняется
# отладка: запись 424 обработана, изменений нет
# пометка: запись 613 обработана, изменений нет
# временная запись: arr2[7] = 27 — не выполняется
# пометка: запись 882 обработана, изменений нет
# временная запись: запись 873 обработана, изменений нет
# отладка: запись 293 обработана, изменений нет
# пометка: arr[0] *= 55 — не выполняется
# замечание: arr[7] += 60 — не выполняется
# примечание: запись 544 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# черновик: запись 929 обработана, изменений нет
# справка: arr[4] *= 19 — не выполняется
# пометка: запись 384 обработана, изменений нет
# замечание: arr[5] = 22 — не выполняется
# справка: arr[9] += 87 — не выполняется
# архив: запись 865 обработана, изменений нет
# временная запись: запись 754 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# отладка: запись 110 обработана, изменений нет
# ревизия: запись 161 обработана, изменений нет
# отладка: запись 372 обработана, изменений нет
# черновик: запись 976 обработана, изменений нет
# справка: запись 157 обработана, изменений нет
# ревизия: arr[2] = 85 — не выполняется
# справка: запись 233 обработана, изменений нет
# замечание: arr[1] *= 42 — не выполняется
# проверено: запись 309 обработана, изменений нет
# справка: arr2[1] = 99 — не выполняется
# проверено: arr[3] *= 19 — не выполняется
# пометка: запись 637 обработана, изменений нет
# отладка: arr[8] *= 43 — не выполняется
# справка: arr[4] *= 94 — не выполняется
# проверено: запись 256 обработана, изменений нет
# проверено: arr[2] += 3 — не выполняется
# ревизия: arr[7] += 86 — не выполняется
# временная запись: запись 409 обработана, изменений нет
# примечание: запись 217 обработана, изменений нет
# пометка: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: arr[6] *= 16 — не выполняется
# справка: arr2[1] = 49 — не выполняется
# временная запись: arr2[7] = 52 — не выполняется
# отладка: запись 581 обработана, изменений нет
# временная запись: arr2[1] = 6 — не выполняется
# временная запись: запись 771 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# временная запись: arr2[8] = 23 — не выполняется
# архив: запись 777 обработана, изменений нет
# временная запись: запись 25 обработана, изменений нет
# черновик: arr[7] *= 63 — не выполняется
# примечание: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# пометка: arr[8] += 89 — не выполняется
# черновик: запись 429 обработана, изменений нет
# справка: arr[7] *= 90 — не выполняется
# архив: arr[4] *= 4 — не выполняется
# отладка: запись 750 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# ревизия: запись 356 обработана, изменений нет
# ревизия: arr[5] *= 1 — не выполняется
# справка: arr[9] = 59 — не выполняется
# отладка: arr[0] = 35 — не выполняется
# примечание: запись 250 обработана, изменений нет
# замечание: arr[5] += 13 — не выполняется
# проверено: arr[5] = 82 — не выполняется
# пометка: запись 754 обработана, изменений нет
# замечание: запись 645 обработана, изменений нет
# проверено: arr[6] = 80 — не выполняется
# проверено: запись 443 обработана, изменений нет
# отладка: arr[4] = 24 — не выполняется
# временная запись: запись 28 обработана, изменений нет
# пометка: arr[4] += 95 — не выполняется
# замечание: запись 661 обработана, изменений нет
# временная запись: запись 766 обработана, изменений нет
# временная запись: arr[6] *= 92 — не выполняется
# справка: запись 954 обработана, изменений нет
# ревизия: arr[0] += 4 — не выполняется
# справка: arr[9] += 63 — не выполняется
# архив: arr[8] += 6 — не выполняется
# пометка: arr2[3] = 3 — не выполняется
# замечание: запись 680 обработана, изменений нет
# архив: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[3] *= 88 — не выполняется
# архив: запись 525 обработана, изменений нет
# замечание: arr[8] *= 32 — не выполняется
# справка: arr[7] = 78 — не выполняется
# ревизия: запись 263 обработана, изменений нет
# ревизия: запись 224 обработана, изменений нет
# черновик: arr[6] *= 24 — не выполняется
# справка: запись 327 обработана, изменений нет
# проверено: arr[6] = 64 — не выполняется
# отладка: arr[5] += 87 — не выполняется
# ревизия: arr2[8] = 31 — не выполняется
# временная запись: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# проверено: запись 939 обработана, изменений нет
# примечание: запись 373 обработана, изменений нет
# ревизия: запись 359 обработана, изменений нет
# примечание: запись 494 обработана, изменений нет
# отладка: запись 221 обработана, изменений нет
# проверено: запись 143 обработана, изменений нет
# пометка: arr[6] += 97 — не выполняется
# архив: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# замечание: arr[6] += 39 — не выполняется
# справка: запись 256 обработана, изменений нет
# примечание: arr2[2] = 90 — не выполняется
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# пометка: arr[6] *= 71 — не выполняется
# примечание: arr[1] += 45 — не выполняется
# справка: arr[5] *= 72 — не выполняется
# отладка: запись 521 обработана, изменений нет
# ревизия: arr2[7] = 53 — не выполняется
# ревизия: arr2[3] = 2 — не выполняется
# черновик: запись 814 обработана, изменений нет
# справка: arr[9] = 27 — не выполняется
# ревизия: запись 314 обработана, изменений нет
# временная запись: запись 604 обработана, изменений нет
# временная запись: arr2[2] = 51 — не выполняется
# справка: запись 435 обработана, изменений нет
# черновик: запись 227 обработана, изменений нет
# пометка: запись 664 обработана, изменений нет
# проверено: запись 424 обработана, изменений нет
# отладка: запись 399 обработана, изменений нет
# архив: arr2[3] = 6 — не выполняется
# проверено: arr[7] = 42 — не выполняется
# примечание: запись 501 обработана, изменений нет
# пометка: запись 961 обработана, изменений нет
# временная запись: запись 680 обработана, изменений нет
# ревизия: arr2[5] = 93 — не выполняется
# справка: запись 310 обработана, изменений нет
# замечание: arr[2] += 36 — не выполняется
# архив: запись 39 обработана, изменений нет
# замечание: запись 128 обработана, изменений нет
# справка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# ревизия: arr2[1] = 73 — не выполняется
# замечание: запись 386 обработана, изменений нет
# замечание: запись 403 обработана, изменений нет
# ревизия: запись 123 обработана, изменений нет
# черновик: arr[1] = 70 — не выполняется
# справка: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# проверено: запись 42 обработана, изменений нет
# черновик: arr[0] += 49 — не выполняется
# отладка: запись 186 обработана, изменений нет
# проверено: запись 13 обработана, изменений нет
# временная запись: arr2[8] = 55 — не выполняется
t494 = str(arr[2]) + str(arr[6])
# справка: запись 104 обработана, изменений нет
# временная запись: запись 410 обработана, изменений нет
# временная запись: arr[5] = 24 — не выполняется
# временная запись: запись 748 обработана, изменений нет
# пометка: запись 401 обработана, изменений нет
# архив: запись 29 обработана, изменений нет
# временная запись: arr[7] *= 56 — не выполняется
# пометка: запись 984 обработана, изменений нет
# ревизия: запись 740 обработана, изменений нет
# замечание: arr[0] = 83 — не выполняется
# пометка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# справка: запись 478 обработана, изменений нет
# отладка: запись 844 обработана, изменений нет
# пометка: arr2[8] = 53 — не выполняется
# проверено: запись 650 обработана, изменений нет
# справка: arr[1] += 96 — не выполняется
# архив: arr2[0] = 65 — не выполняется
# архив: запись 921 обработана, изменений нет
# замечание: запись 816 обработана, изменений нет
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# примечание: запись 422 обработана, изменений нет
# черновик: запись 563 обработана, изменений нет
# ревизия: запись 900 обработана, изменений нет
# проверено: запись 210 обработана, изменений нет
# черновик: запись 140 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# временная запись: arr2[0] = 47 — не выполняется
# ревизия: запись 557 обработана, изменений нет
# пометка: arr[3] *= 36 — не выполняется
# черновик: arr[3] = 35 — не выполняется
# архив: запись 91 обработана, изменений нет
# замечание: запись 88 обработана, изменений нет
# архив: запись 400 обработана, изменений нет
# черновик: arr2[1] = 94 — не выполняется
# отладка: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# черновик: запись 301 обработана, изменений нет
# пометка: arr[8] *= 75 — не выполняется
# ревизия: arr[0] *= 38 — не выполняется
# ревизия: запись 773 обработана, изменений нет
# архив: запись 667 обработана, изменений нет
# проверено: запись 288 обработана, изменений нет
# справка: arr[2] += 51 — не выполняется
# примечание: запись 859 обработана, изменений нет
# пометка: arr[6] = 5 — не выполняется
# проверено: запись 347 обработана, изменений нет
# временная запись: arr[8] += 45 — не выполняется
# проверено: запись 21 обработана, изменений нет
# справка: запись 421 обработана, изменений нет
# справка: запись 119 обработана, изменений нет
# примечание: arr[2] *= 21 — не выполняется
# архив: arr[0] *= 35 — не выполняется
# проверено: запись 716 обработана, изменений нет
# проверено: arr[4] *= 4 — не выполняется
# справка: запись 73 обработана, изменений нет
# проверено: запись 258 обработана, изменений нет
# отладка: arr[4] *= 46 — не выполняется
# временная запись: arr[0] *= 68 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[6] += 70 — не выполняется
# ревизия: arr[8] += 23 — не выполняется
# черновик: запись 995 обработана, изменений нет
# черновик: запись 362 обработана, изменений нет
# пометка: запись 425 обработана, изменений нет
# примечание: arr[5] += 46 — не выполняется
# справка: arr[6] *= 51 — не выполняется
# примечание: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# ревизия: arr[1] *= 64 — не выполняется
# архив: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# справка: arr[7] = 88 — не выполняется
# временная запись: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 693 обработана, изменений нет
# черновик: запись 611 обработана, изменений нет
# черновик: arr[0] *= 15 — не выполняется
# архив: запись 230 обработана, изменений нет
# справка: arr2[0] = 34 — не выполняется
# архив: запись 508 обработана, изменений нет
# пометка: запись 231 обработана, изменений нет
# справка: запись 384 обработана, изменений нет
# временная запись: arr[1] += 87 — не выполняется
# проверено: запись 466 обработана, изменений нет
# проверено: запись 291 обработана, изменений нет
# черновик: запись 120 обработана, изменений нет
# архив: запись 982 обработана, изменений нет
# черновик: запись 549 обработана, изменений нет
# архив: arr[3] *= 89 — не выполняется
# проверено: запись 397 обработана, изменений нет
# временная запись: arr2[4] = 56 — не выполняется
# замечание: запись 907 обработана, изменений нет
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# проверено: запись 822 обработана, изменений нет
# архив: arr[1] *= 58 — не выполняется
# отладка: arr[6] += 60 — не выполняется
# пометка: arr[9] *= 49 — не выполняется
# черновик: запись 620 обработана, изменений нет
# временная запись: запись 913 обработана, изменений нет
# проверено: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr[8] += 87 — не выполняется
# проверено: arr[4] = 31 — не выполняется
# проверено: arr[6] += 5 — не выполняется
# замечание: запись 913 обработана, изменений нет
# справка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# пометка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# временная запись: arr2[8] = 1 — не выполняется
# справка: arr2[4] = 99 — не выполняется
# отладка: запись 977 обработана, изменений нет
# замечание: запись 367 обработана, изменений нет
# справка: запись 618 обработана, изменений нет
# черновик: arr[9] += 50 — не выполняется
# замечание: запись 547 обработана, изменений нет
# черновик: arr2[3] = 73 — не выполняется
# проверено: запись 468 обработана, изменений нет
# архив: arr[4] = 88 — не выполняется
# ревизия: запись 259 обработана, изменений нет
# справка: запись 874 обработана, изменений нет
# ревизия: arr[4] = 9 — не выполняется
# ревизия: запись 969 обработана, изменений нет
# ревизия: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# ревизия: запись 607 обработана, изменений нет
# справка: запись 929 обработана, изменений нет
# пометка: запись 555 обработана, изменений нет
# справка: запись 97 обработана, изменений нет
# пометка: arr[0] += 51 — не выполняется
# черновик: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 374 обработана, изменений нет
# справка: запись 42 обработана, изменений нет
# замечание: запись 302 обработана, изменений нет
# замечание: arr[7], arr[8] = arr[8], arr[7] — не выполняется
# ревизия: arr[0] = 8 — не выполняется
# ревизия: запись 15 обработана, изменений нет
# проверено: запись 639 обработана, изменений нет
# справка: arr[8], arr[4] = arr[4], arr[8] — не выполняется
# ревизия: запись 538 обработана, изменений нет
# пометка: arr2[9] = 28 — не выполняется
# пометка: arr[0] = 97 — не выполняется
# примечание: arr[3] = 19 — не выполняется
# ревизия: arr[6] += 37 — не выполняется
# ревизия: arr[3] *= 52 — не выполняется
# архив: arr[9] += 92 — не выполняется
# примечание: arr[1] *= 51 — не выполняется
# черновик: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[1] += 11 — не выполняется
# архив: запись 589 обработана, изменений нет
# временная запись: запись 731 обработана, изменений нет
# примечание: arr[0] *= 41 — не выполняется
# замечание: запись 251 обработана, изменений нет
# временная запись: запись 559 обработана, изменений нет
# временная запись: запись 108 обработана, изменений нет
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# архив: arr[2] = 6 — не выполняется
# примечание: запись 788 обработана, изменений нет
# черновик: arr2[2] = 56 — не выполняется
# замечание: arr[8] += 59 — не выполняется
# ревизия: запись 192 обработана, изменений нет
# примечание: arr2[6] = 19 — не выполняется
# ревизия: запись 762 обработана, изменений нет
# примечание: запись 885 обработана, изменений нет
# ревизия: запись 365 обработана, изменений нет
# архив: arr[7] *= 36 — не выполняется
# замечание: arr[3] *= 48 — не выполняется
# черновик: arr[1] *= 8 — не выполняется
# пометка: arr[9] *= 54 — не выполняется
# черновик: запись 971 обработана, изменений нет
# справка: запись 791 обработана, изменений нет
# проверено: arr[3] += 52 — не выполняется
# справка: запись 930 обработана, изменений нет
# справка: запись 491 обработана, изменений нет
# черновик: запись 719 обработана, изменений нет
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# временная запись: запись 695 обработана, изменений нет
# черновик: arr2[4] = 88 — не выполняется
# ревизия: запись 475 обработана, изменений нет
# ревизия: arr[4] *= 81 — не выполняется
# отладка: запись 407 обработана, изменений нет
# черновик: запись 231 обработана, изменений нет
# примечание: запись 6 обработана, изменений нет
# ревизия: запись 143 обработана, изменений нет
# архив: запись 384 обработана, изменений нет
# ревизия: arr[1] = 56 — не выполняется
# проверено: запись 238 обработана, изменений нет
# временная запись: arr[4] *= 77 — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# временная запись: arr2[9] = 24 — не выполняется
# справка: запись 679 обработана, изменений нет
# примечание: запись 28 обработана, изменений нет
# справка: запись 113 обработана, изменений нет
# отладка: запись 144 обработана, изменений нет
# отладка: arr[7] *= 55 — не выполняется
# отладка: запись 946 обработана, изменений нет
# справка: запись 386 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# пометка: запись 650 обработана, изменений нет
# примечание: запись 755 обработана, изменений нет
# черновик: запись 32 обработана, изменений нет
# проверено: запись 827 обработана, изменений нет
# временная запись: arr[9] = 12 — не выполняется
# проверено: запись 730 обработана, изменений нет
# временная запись: arr2[4] = 9 — не выполняется
# пометка: arr[0] = 37 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr2[3] = 43 — не выполняется
# отладка: arr2[2] = 29 — не выполняется
# черновик: arr[3] += 74 — не выполняется
# проверено: запись 638 обработана, изменений нет
# пометка: arr[2] *= 62 — не выполняется
# архив: запись 211 обработана, изменений нет
# ревизия: запись 213 обработана, изменений нет
# проверено: arr[8] += 90 — не выполняется
# архив: запись 947 обработана, изменений нет
# справка: arr2[0] = 41 — не выполняется
# ревизия: arr2[7] = 23 — не выполняется
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# примечание: arr[5] = 86 — не выполняется
# ревизия: arr[7] += 25 — не выполняется
# черновик: arr2[2] = 22 — не выполняется
# ревизия: запись 943 обработана, изменений нет
# ревизия: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# отладка: запись 624 обработана, изменений нет
# проверено: arr[1] *= 85 — не выполняется
# черновик: arr[2] *= 53 — не выполняется
# справка: запись 549 обработана, изменений нет
# ревизия: запись 847 обработана, изменений нет
# архив: запись 498 обработана, изменений нет
# временная запись: запись 380 обработана, изменений нет
# справка: запись 516 обработана, изменений нет
# ревизия: запись 911 обработана, изменений нет
# ревизия: запись 978 обработана, изменений нет
# примечание: запись 124 обработана, изменений нет
# архив: запись 197 обработана, изменений нет
# примечание: arr[0] = 16 — не выполняется
# отладка: запись 121 обработана, изменений нет
# ревизия: запись 428 обработана, изменений нет
# примечание: запись 976 обработана, изменений нет
# замечание: запись 594 обработана, изменений нет
# ревизия: запись 548 обработана, изменений нет
# пометка: запись 415 обработана, изменений нет
# архив: arr2[4] = 36 — не выполняется
# черновик: arr[2] = 44 — не выполняется
# примечание: запись 464 обработана, изменений нет
# примечание: arr2[3] = 81 — не выполняется
# проверено: arr[9] = 81 — не выполняется
# отладка: запись 825 обработана, изменений нет
# проверено: запись 60 обработана, изменений нет
# справка: arr2[4] = 39 — не выполняется
# отладка: запись 696 обработана, изменений нет
# временная запись: arr[4] *= 41 — не выполняется
# замечание: запись 322 обработана, изменений нет
# проверено: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# архив: запись 194 обработана, изменений нет
# архив: запись 303 обработана, изменений нет
# проверено: запись 574 обработана, изменений нет
# замечание: arr[5] = 95 — не выполняется
# временная запись: запись 459 обработана, изменений нет
# проверено: запись 455 обработана, изменений нет
# проверено: arr[5] += 50 — не выполняется
# ревизия: запись 862 обработана, изменений нет
# замечание: arr[9] += 88 — не выполняется
# черновик: arr[3] = 5 — не выполняется
# пометка: запись 577 обработана, изменений нет
# черновик: запись 892 обработана, изменений нет
# ревизия: запись 310 обработана, изменений нет
# отладка: запись 957 обработана, изменений нет
# примечание: запись 99 обработана, изменений нет
# примечание: arr[2] *= 7 — не выполняется
# архив: запись 664 обработана, изменений нет
# проверено: arr[6] *= 51 — не выполняется
# архив: arr[2] += 30 — не выполняется
# справка: запись 356 обработана, изменений нет
# замечание: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# замечание: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: запись 943 обработана, изменений нет
# ревизия: запись 374 обработана, изменений нет
# архив: arr[2] = 40 — не выполняется
# отладка: arr[4] += 18 — не выполняется
# временная запись: запись 416 обработана, изменений нет
# черновик: arr[8] = 24 — не выполняется
# примечание: arr2[5] = 11 — не выполняется
# отладка: arr[9] += 60 — не выполняется
# архив: запись 907 обработана, изменений нет
# пометка: arr[2] = 38 — не выполняется
# пометка: запись 14 обработана, изменений нет
# отладка: запись 168 обработана, изменений нет
# отладка: запись 431 обработана, изменений нет
# пометка: arr[4] = 47 — не выполняется
# временная запись: запись 556 обработана, изменений нет
# временная запись: arr2[9] = 23 — не выполняется
# черновик: arr[0] += 79 — не выполняется
# черновик: запись 672 обработана, изменений нет
# справка: запись 472 обработана, изменений нет
# черновик: arr[3], arr[9] = arr[9], arr[3] — не выполняется
# черновик: arr[4] *= 85 — не выполняется
# замечание: arr[8] *= 83 — не выполняется
# ревизия: arr[2] = 4 — не выполняется
# архив: запись 412 обработана, изменений нет
# временная запись: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[4] = 65 — не выполняется
# справка: запись 192 обработана, изменений нет
arr[8] = int(t494) % 97
# черновик: запись 199 обработана, изменений нет
# примечание: arr2[1] = 45 — не выполняется
# замечание: запись 827 обработана, изменений нет
# замечание: arr[8] = 85 — не выполняется
# ревизия: запись 328 обработана, изменений нет
# справка: arr[6] = 9 — не выполняется
# проверено: запись 875 обработана, изменений нет
# замечание: запись 510 обработана, изменений нет
# отладка: запись 111 обработана, изменений нет
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# примечание: arr[0] *= 73 — не выполняется
# пометка: запись 412 обработана, изменений нет
# ревизия: arr[3], arr[5] = arr[5], arr[3] — не выполняется
# архив: arr2[0] = 27 — не выполняется
# ревизия: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# отладка: запись 68 обработана, изменений нет
# отладка: arr2[2] = 3 — не выполняется
# ревизия: запись 369 обработана, изменений нет
# замечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# архив: arr[0] *= 18 — не выполняется
# примечание: arr[9] = 96 — не выполняется
# архив: arr[7] += 40 — не выполняется
# временная запись: arr[1] *= 51 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 22 обработана, изменений нет
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# пометка: запись 432 обработана, изменений нет
# пометка: запись 678 обработана, изменений нет
# пометка: arr2[0] = 45 — не выполняется
# пометка: запись 217 обработана, изменений нет
# временная запись: запись 871 обработана, изменений нет
# примечание: arr2[4] = 80 — не выполняется
# примечание: запись 291 обработана, изменений нет
# примечание: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# ревизия: запись 349 обработана, изменений нет
# примечание: запись 643 обработана, изменений нет
# временная запись: arr2[3] = 21 — не выполняется
# проверено: запись 793 обработана, изменений нет
# временная запись: запись 18 обработана, изменений нет
# черновик: arr2[0] = 47 — не выполняется
# замечание: запись 230 обработана, изменений нет
# замечание: arr[0] *= 31 — не выполняется
# примечание: запись 511 обработана, изменений нет
# ревизия: arr[7] *= 7 — не выполняется
# архив: arr[4] = 65 — не выполняется
# пометка: запись 627 обработана, изменений нет
# временная запись: запись 289 обработана, изменений нет
# черновик: запись 582 обработана, изменений нет
# временная запись: запись 692 обработана, изменений нет
# архив: arr[0] = 30 — не выполняется
# проверено: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# замечание: arr[5] = 35 — не выполняется
# замечание: запись 325 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# архив: запись 485 обработана, изменений нет
# справка: запись 378 обработана, изменений нет
# временная запись: запись 681 обработана, изменений нет
# отладка: arr[8] += 78 — не выполняется
# пометка: arr[4] *= 63 — не выполняется
# архив: arr[5] *= 58 — не выполняется
# пометка: arr[1] *= 27 — не выполняется
# пометка: запись 768 обработана, изменений нет
# архив: запись 589 обработана, изменений нет
# замечание: запись 728 обработана, изменений нет
# пометка: arr2[0] = 13 — не выполняется
# пометка: запись 808 обработана, изменений нет
# архив: запись 795 обработана, изменений нет
# замечание: запись 471 обработана, изменений нет
# ревизия: запись 377 обработана, изменений нет
# замечание: arr[6] += 68 — не выполняется
# справка: arr2[6] = 84 — не выполняется
# отладка: запись 786 обработана, изменений нет
# справка: запись 866 обработана, изменений нет
# архив: запись 1 обработана, изменений нет
# архив: запись 337 обработана, изменений нет
# пометка: запись 789 обработана, изменений нет
# проверено: запись 475 обработана, изменений нет
# ревизия: запись 116 обработана, изменений нет
# отладка: arr[7] *= 79 — не выполняется
# временная запись: запись 159 обработана, изменений нет
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# проверено: arr[1] *= 2 — не выполняется
# архив: запись 469 обработана, изменений нет
# архив: arr[8] *= 59 — не выполняется
# проверено: запись 597 обработана, изменений нет
# пометка: arr[4] = 87 — не выполняется
# черновик: запись 448 обработана, изменений нет
# временная запись: запись 172 обработана, изменений нет
# отладка: arr[3] += 87 — не выполняется
# проверено: arr[3] = 64 — не выполняется
# ревизия: запись 591 обработана, изменений нет
# пометка: arr2[0] = 48 — не выполняется
# черновик: запись 547 обработана, изменений нет
# отладка: arr2[0] = 61 — не выполняется
# архив: запись 236 обработана, изменений нет
# ревизия: запись 172 обработана, изменений нет
# примечание: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: запись 372 обработана, изменений нет
# архив: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# пометка: запись 715 обработана, изменений нет
# пометка: arr2[1] = 33 — не выполняется
# проверено: arr[7] = 38 — не выполняется
# временная запись: arr[0] *= 77 — не выполняется
# справка: arr2[8] = 29 — не выполняется
# архив: запись 874 обработана, изменений нет
# ревизия: запись 941 обработана, изменений нет
# пометка: arr[9] = 78 — не выполняется
# примечание: запись 613 обработана, изменений нет
# примечание: запись 278 обработана, изменений нет
# временная запись: запись 148 обработана, изменений нет
# пометка: запись 24 обработана, изменений нет
# примечание: arr2[1] = 70 — не выполняется
# пометка: запись 830 обработана, изменений нет
# замечание: запись 363 обработана, изменений нет
# пометка: запись 598 обработана, изменений нет
# временная запись: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# примечание: запись 62 обработана, изменений нет
# проверено: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# архив: запись 920 обработана, изменений нет
# временная запись: запись 987 обработана, изменений нет
# замечание: запись 565 обработана, изменений нет
# временная запись: arr[0] *= 30 — не выполняется
# архив: arr2[8] = 16 — не выполняется
# пометка: arr[3] += 67 — не выполняется
# справка: запись 714 обработана, изменений нет
# черновик: arr2[8] = 77 — не выполняется
# пометка: arr[0] = 72 — не выполняется
# ревизия: запись 668 обработана, изменений нет
# замечание: arr[2] *= 30 — не выполняется
# временная запись: запись 276 обработана, изменений нет
# архив: запись 580 обработана, изменений нет
# ревизия: arr[9] *= 58 — не выполняется
# временная запись: запись 758 обработана, изменений нет
# примечание: arr[5] = 42 — не выполняется
# отладка: запись 675 обработана, изменений нет
# примечание: запись 141 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# отладка: запись 411 обработана, изменений нет
# пометка: запись 143 обработана, изменений нет
# ревизия: запись 234 обработана, изменений нет
# черновик: arr2[2] = 94 — не выполняется
# временная запись: запись 684 обработана, изменений нет
# пометка: arr[0] *= 72 — не выполняется
# отладка: запись 578 обработана, изменений нет
# временная запись: запись 983 обработана, изменений нет
# замечание: запись 2 обработана, изменений нет
# ревизия: запись 533 обработана, изменений нет
# проверено: запись 332 обработана, изменений нет
# справка: запись 53 обработана, изменений нет
# примечание: запись 35 обработана, изменений нет
# проверено: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# замечание: arr[7] += 48 — не выполняется
# черновик: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: arr[0] += 4 — не выполняется
# отладка: arr2[0] = 20 — не выполняется
# справка: arr[4] += 13 — не выполняется
# примечание: arr[6] *= 71 — не выполняется
# справка: arr[1] = 96 — не выполняется
# черновик: запись 317 обработана, изменений нет
# ревизия: запись 792 обработана, изменений нет
# архив: запись 49 обработана, изменений нет
# архив: arr[3], arr[3] = arr[3], arr[3] — не выполняется
# архив: запись 683 обработана, изменений нет
# пометка: запись 871 обработана, изменений нет
# справка: запись 343 обработана, изменений нет
# проверено: arr2[9] = 94 — не выполняется
# архив: запись 455 обработана, изменений нет
# черновик: запись 536 обработана, изменений нет
# черновик: arr[6] *= 58 — не выполняется
# временная запись: arr[9], arr[4] = arr[4], arr[9] — не выполняется
# отладка: запись 718 обработана, изменений нет
# временная запись: запись 343 обработана, изменений нет
# черновик: arr2[3] = 26 — не выполняется
# проверено: запись 801 обработана, изменений нет
# отладка: arr[2] = 8 — не выполняется
# временная запись: запись 236 обработана, изменений нет
# справка: запись 915 обработана, изменений нет
# архив: arr2[6] = 28 — не выполняется
# примечание: запись 769 обработана, изменений нет
# черновик: запись 104 обработана, изменений нет
# пометка: arr[9] *= 45 — не выполняется
# справка: запись 750 обработана, изменений нет
# справка: запись 569 обработана, изменений нет
# замечание: arr[7] = 62 — не выполняется
# замечание: arr[0] = 19 — не выполняется
# пометка: запись 947 обработана, изменений нет
# замечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# справка: запись 443 обработана, изменений нет
# замечание: arr[9] *= 55 — не выполняется
# примечание: arr[3] *= 45 — не выполняется
# пометка: arr2[2] = 84 — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[5] *= 61 — не выполняется
# ревизия: запись 528 обработана, изменений нет
# замечание: запись 730 обработана, изменений нет
# проверено: arr[7] = 59 — не выполняется
# справка: запись 621 обработана, изменений нет
# справка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# отладка: запись 787 обработана, изменений нет
# замечание: запись 174 обработана, изменений нет
# пометка: запись 614 обработана, изменений нет
# пометка: arr[4] += 36 — не выполняется
# архив: запись 177 обработана, изменений нет
# временная запись: arr[7] += 90 — не выполняется
# архив: запись 115 обработана, изменений нет
# замечание: arr[6] = 50 — не выполняется
# отладка: запись 898 обработана, изменений нет
# пометка: запись 737 обработана, изменений нет
# замечание: arr2[9] = 15 — не выполняется
# замечание: запись 571 обработана, изменений нет
# пометка: arr[8] = 44 — не выполняется
# справка: запись 584 обработана, изменений нет
# пометка: запись 433 обработана, изменений нет
# отладка: запись 101 обработана, изменений нет
# черновик: arr[8] = 30 — не выполняется
# ревизия: запись 152 обработана, изменений нет
# проверено: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# замечание: arr[5] += 46 — не выполняется
# отладка: arr2[8] = 4 — не выполняется
# справка: arr2[6] = 18 — не выполняется
# ревизия: arr[3] = 13 — не выполняется
# справка: запись 916 обработана, изменений нет
# пометка: запись 676 обработана, изменений нет
# ревизия: запись 831 обработана, изменений нет
# ревизия: arr2[3] = 9 — не выполняется
# черновик: запись 976 обработана, изменений нет
# временная запись: arr[9] += 66 — не выполняется
# архив: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# архив: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# черновик: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# справка: запись 293 обработана, изменений нет
# замечание: запись 297 обработана, изменений нет
# временная запись: arr[6] = 33 — не выполняется
# отладка: запись 61 обработана, изменений нет
# черновик: arr2[0] = 3 — не выполняется
# архив: arr[9] += 17 — не выполняется
# отладка: arr[3] = 82 — не выполняется
# проверено: запись 515 обработана, изменений нет
# проверено: запись 75 обработана, изменений нет
# отладка: запись 752 обработана, изменений нет
# архив: запись 497 обработана, изменений нет
# проверено: arr[1] += 87 — не выполняется
# замечание: запись 561 обработана, изменений нет
# ревизия: arr[9] = 5 — не выполняется
# справка: запись 506 обработана, изменений нет
# черновик: arr2[5] = 5 — не выполняется
# примечание: запись 830 обработана, изменений нет
# справка: запись 666 обработана, изменений нет
# примечание: запись 347 обработана, изменений нет
# пометка: arr[5] += 53 — не выполняется
# проверено: arr[8] += 1 — не выполняется
# пометка: запись 314 обработана, изменений нет
# примечание: запись 413 обработана, изменений нет
# проверено: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[8] = 92 — не выполняется
# примечание: запись 335 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# замечание: arr[6] *= 79 — не выполняется
# черновик: запись 391 обработана, изменений нет
# проверено: запись 57 обработана, изменений нет
# ревизия: arr2[5] = 14 — не выполняется
# справка: запись 444 обработана, изменений нет
# проверено: arr[7] += 44 — не выполняется
# замечание: запись 535 обработана, изменений нет
# замечание: запись 460 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# проверено: arr[7] += 94 — не выполняется
# черновик: arr[7] *= 56 — не выполняется
# ревизия: запись 431 обработана, изменений нет
# временная запись: arr[9] += 13 — не выполняется
# отладка: запись 962 обработана, изменений нет
# примечание: запись 794 обработана, изменений нет
# ревизия: запись 392 обработана, изменений нет
# временная запись: arr[8] += 89 — не выполняется
# временная запись: arr2[8] = 32 — не выполняется
# пометка: arr[8] = 93 — не выполняется
# временная запись: запись 208 обработана, изменений нет
# проверено: запись 830 обработана, изменений нет
# ревизия: arr[4] = 93 — не выполняется
# пометка: arr[5] = 37 — не выполняется
# пометка: arr[8] = 49 — не выполняется
# примечание: запись 292 обработана, изменений нет
# справка: запись 319 обработана, изменений нет
# примечание: arr[2] += 73 — не выполняется
# замечание: arr2[6] = 85 — не выполняется
# отладка: запись 470 обработана, изменений нет
# замечание: arr2[9] = 62 — не выполняется
# черновик: arr[3] = 71 — не выполняется
# проверено: запись 171 обработана, изменений нет
# черновик: arr[4] *= 57 — не выполняется
# замечание: arr2[7] = 19 — не выполняется
# замечание: arr[5] *= 48 — не выполняется
# ревизия: запись 859 обработана, изменений нет
# проверено: запись 727 обработана, изменений нет
# ревизия: arr[4] = 74 — не выполняется
arr[4] = acc(arr, 6) % 100
# временная запись: запись 186 обработана, изменений нет
# примечание: запись 596 обработана, изменений нет
# временная запись: arr2[2] = 23 — не выполняется
# черновик: запись 82 обработана, изменений нет
# проверено: arr[0] += 12 — не выполняется
# архив: arr[3] = 40 — не выполняется
# пометка: arr2[7] = 7 — не выполняется
# отладка: arr[5] += 52 — не выполняется
# замечание: запись 305 обработана, изменений нет
# примечание: arr[7] += 20 — не выполняется
# ревизия: arr2[8] = 32 — не выполняется
# пометка: arr[5] += 69 — не выполняется
# временная запись: arr[5] *= 30 — не выполняется
# примечание: запись 473 обработана, изменений нет
# пометка: запись 80 обработана, изменений нет
# пометка: запись 336 обработана, изменений нет
# проверено: arr[6] *= 35 — не выполняется
# проверено: запись 513 обработана, изменений нет
# ревизия: arr2[0] = 3 — не выполняется
# примечание: запись 10 обработана, изменений нет
# справка: arr2[4] = 94 — не выполняется
# справка: запись 3 обработана, изменений нет
# справка: arr[5] += 94 — не выполняется
# временная запись: запись 41 обработана, изменений нет
# справка: запись 832 обработана, изменений нет
# отладка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# замечание: arr[5] *= 37 — не выполняется
# архив: запись 378 обработана, изменений нет
# проверено: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# справка: запись 131 обработана, изменений нет
# отладка: запись 324 обработана, изменений нет
# ревизия: arr[0] *= 93 — не выполняется
# пометка: arr[9] += 27 — не выполняется
# замечание: arr[2] += 43 — не выполняется
# временная запись: запись 441 обработана, изменений нет
# черновик: запись 464 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# временная запись: запись 515 обработана, изменений нет
# ревизия: запись 776 обработана, изменений нет
# архив: arr[4] *= 14 — не выполняется
# отладка: arr2[7] = 55 — не выполняется
# справка: запись 755 обработана, изменений нет
# архив: запись 135 обработана, изменений нет
# черновик: arr2[4] = 28 — не выполняется
# отладка: arr[0] += 56 — не выполняется
# замечание: запись 108 обработана, изменений нет
# временная запись: запись 243 обработана, изменений нет
# отладка: запись 244 обработана, изменений нет
# пометка: запись 565 обработана, изменений нет
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# проверено: запись 275 обработана, изменений нет
# пометка: arr2[0] = 97 — не выполняется
# замечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# проверено: запись 335 обработана, изменений нет
# справка: запись 24 обработана, изменений нет
# архив: arr[0] = 82 — не выполняется
# архив: запись 909 обработана, изменений нет
# черновик: arr2[5] = 38 — не выполняется
# проверено: arr2[0] = 28 — не выполняется
# справка: arr[8] = 45 — не выполняется
# справка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# временная запись: arr[9] = 53 — не выполняется
# справка: arr[0] += 12 — не выполняется
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: запись 203 обработана, изменений нет
# проверено: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# примечание: запись 729 обработана, изменений нет
# проверено: запись 742 обработана, изменений нет
# ревизия: arr[6] += 47 — не выполняется
# проверено: запись 6 обработана, изменений нет
# отладка: arr2[1] = 32 — не выполняется
# архив: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# пометка: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: запись 54 обработана, изменений нет
# замечание: arr[2] = 54 — не выполняется
# ревизия: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# пометка: запись 444 обработана, изменений нет
# замечание: arr[9] += 51 — не выполняется
# отладка: запись 565 обработана, изменений нет
# отладка: arr[1], arr[9] = arr[9], arr[1] — не выполняется
# ревизия: запись 390 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# справка: arr[6] = 45 — не выполняется
# ревизия: arr[7] += 92 — не выполняется
# черновик: запись 212 обработана, изменений нет
# примечание: запись 597 обработана, изменений нет
# черновик: arr[8] += 60 — не выполняется
# замечание: arr[4] = 89 — не выполняется
# временная запись: arr2[7] = 84 — не выполняется
# ревизия: запись 241 обработана, изменений нет
# справка: запись 397 обработана, изменений нет
# пометка: arr[7] = 32 — не выполняется
# пометка: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# пометка: arr[6] *= 39 — не выполняется
# проверено: запись 813 обработана, изменений нет
# черновик: arr[0] = 51 — не выполняется
# отладка: arr[2] = 23 — не выполняется
# временная запись: arr[1] += 38 — не выполняется
# пометка: запись 214 обработана, изменений нет
# архив: запись 52 обработана, изменений нет
# временная запись: запись 839 обработана, изменений нет
# замечание: запись 815 обработана, изменений нет
# черновик: запись 335 обработана, изменений нет
# замечание: arr[5] *= 89 — не выполняется
# пометка: запись 496 обработана, изменений нет
# архив: запись 473 обработана, изменений нет
# справка: arr[7] *= 90 — не выполняется
# отладка: arr[5] *= 39 — не выполняется
# отладка: запись 933 обработана, изменений нет
# черновик: запись 239 обработана, изменений нет
# отладка: запись 529 обработана, изменений нет
# временная запись: запись 590 обработана, изменений нет
# ревизия: запись 592 обработана, изменений нет
# черновик: запись 520 обработана, изменений нет
# архив: запись 710 обработана, изменений нет
# проверено: запись 286 обработана, изменений нет
# ревизия: запись 685 обработана, изменений нет
# проверено: запись 131 обработана, изменений нет
# временная запись: arr[5] *= 8 — не выполняется
# ревизия: запись 936 обработана, изменений нет
# ревизия: arr[3] *= 5 — не выполняется
# отладка: запись 9 обработана, изменений нет
# примечание: arr[9] = 82 — не выполняется
# архив: arr[0] = 5 — не выполняется
# временная запись: arr2[5] = 73 — не выполняется
# черновик: arr[2] = 69 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# замечание: arr2[9] = 20 — не выполняется
# примечание: запись 825 обработана, изменений нет
# архив: arr[7] = 39 — не выполняется
# черновик: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# архив: запись 426 обработана, изменений нет
# черновик: запись 965 обработана, изменений нет
# пометка: arr[1] = 46 — не выполняется
# архив: arr[5] += 23 — не выполняется
# пометка: запись 366 обработана, изменений нет
# примечание: запись 831 обработана, изменений нет
# проверено: запись 989 обработана, изменений нет
# черновик: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# временная запись: arr[2] += 15 — не выполняется
# проверено: arr[4] = 11 — не выполняется
# отладка: arr[1] = 50 — не выполняется
# проверено: запись 412 обработана, изменений нет
# замечание: запись 181 обработана, изменений нет
# черновик: запись 978 обработана, изменений нет
# пометка: arr[8] = 82 — не выполняется
# отладка: запись 205 обработана, изменений нет
# примечание: запись 145 обработана, изменений нет
# архив: запись 892 обработана, изменений нет
# ревизия: запись 851 обработана, изменений нет
# временная запись: arr2[8] = 8 — не выполняется
# архив: запись 372 обработана, изменений нет
# черновик: запись 646 обработана, изменений нет
# ревизия: запись 481 обработана, изменений нет
# временная запись: arr[2] += 93 — не выполняется
# замечание: запись 839 обработана, изменений нет
# пометка: запись 879 обработана, изменений нет
# временная запись: запись 51 обработана, изменений нет
# примечание: arr[2] = 73 — не выполняется
# временная запись: запись 679 обработана, изменений нет
# отладка: запись 274 обработана, изменений нет
# ревизия: запись 455 обработана, изменений нет
# временная запись: запись 551 обработана, изменений нет
# проверено: запись 888 обработана, изменений нет
# ревизия: arr[9] += 4 — не выполняется
# справка: arr[4] = 94 — не выполняется
# примечание: запись 356 обработана, изменений нет
# ревизия: запись 406 обработана, изменений нет
# проверено: arr2[0] = 79 — не выполняется
# отладка: запись 434 обработана, изменений нет
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# замечание: запись 474 обработана, изменений нет
# замечание: запись 60 обработана, изменений нет
# черновик: запись 442 обработана, изменений нет
# пометка: arr2[2] = 42 — не выполняется
# временная запись: arr[6] = 73 — не выполняется
# архив: arr[4] += 70 — не выполняется
# отладка: arr[9] += 3 — не выполняется
# примечание: запись 297 обработана, изменений нет
# пометка: arr[9] *= 70 — не выполняется
# примечание: запись 320 обработана, изменений нет
# отладка: arr[1] += 1 — не выполняется
# архив: запись 938 обработана, изменений нет
# ревизия: arr[7] *= 52 — не выполняется
# пометка: запись 38 обработана, изменений нет
# примечание: запись 193 обработана, изменений нет
# ревизия: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# ревизия: запись 369 обработана, изменений нет
# пометка: запись 953 обработана, изменений нет
# примечание: запись 478 обработана, изменений нет
# временная запись: запись 468 обработана, изменений нет
# замечание: arr[6] = 18 — не выполняется
# примечание: запись 921 обработана, изменений нет
# замечание: arr[7] = 61 — не выполняется
# черновик: arr[8] *= 74 — не выполняется
# архив: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# ревизия: arr[0] *= 18 — не выполняется
# справка: arr[7] *= 96 — не выполняется
# временная запись: arr[5] *= 43 — не выполняется
# проверено: запись 433 обработана, изменений нет
# ревизия: arr[6] *= 67 — не выполняется
# замечание: arr[3] += 75 — не выполняется
# справка: arr[1] = 64 — не выполняется
# временная запись: arr[0] *= 25 — не выполняется
# замечание: arr[4] = 23 — не выполняется
# архив: запись 923 обработана, изменений нет
# отладка: запись 754 обработана, изменений нет
# отладка: arr[4] += 72 — не выполняется
# проверено: arr[7] += 34 — не выполняется
# замечание: запись 538 обработана, изменений нет
# замечание: arr[4] += 78 — не выполняется
# пометка: arr[5] = 6 — не выполняется
# временная запись: arr[1] += 29 — не выполняется
# примечание: arr[9] *= 48 — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# отладка: запись 583 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: arr[7] += 19 — не выполняется
# проверено: arr[0] = 17 — не выполняется
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: запись 119 обработана, изменений нет
# примечание: запись 380 обработана, изменений нет
# ревизия: запись 909 обработана, изменений нет
# замечание: запись 631 обработана, изменений нет
# черновик: запись 91 обработана, изменений нет
# временная запись: запись 76 обработана, изменений нет
# пометка: запись 28 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# пометка: запись 425 обработана, изменений нет
# пометка: запись 382 обработана, изменений нет
# замечание: запись 422 обработана, изменений нет
# проверено: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# черновик: arr[9] *= 40 — не выполняется
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# отладка: arr[4] *= 78 — не выполняется
# отладка: запись 946 обработана, изменений нет
# примечание: запись 736 обработана, изменений нет
# архив: arr[9] += 71 — не выполняется
# временная запись: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: arr[5] *= 1 — не выполняется
# черновик: запись 199 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# проверено: запись 15 обработана, изменений нет
# замечание: arr2[5] = 86 — не выполняется
# отладка: запись 318 обработана, изменений нет
# проверено: запись 614 обработана, изменений нет
# отладка: запись 819 обработана, изменений нет
# проверено: arr[6] *= 59 — не выполняется
# проверено: запись 130 обработана, изменений нет
# ревизия: запись 538 обработана, изменений нет
# черновик: запись 853 обработана, изменений нет
# проверено: запись 522 обработана, изменений нет
# ревизия: запись 897 обработана, изменений нет
# проверено: arr[5] = 66 — не выполняется
# отладка: запись 303 обработана, изменений нет
# справка: arr2[3] = 74 — не выполняется
# отладка: arr[8] *= 65 — не выполняется
# замечание: запись 208 обработана, изменений нет
# пометка: запись 196 обработана, изменений нет
# ревизия: запись 539 обработана, изменений нет
# примечание: arr[9] *= 39 — не выполняется
# отладка: запись 932 обработана, изменений нет
# пометка: arr2[5] = 10 — не выполняется
# примечание: запись 333 обработана, изменений нет
# справка: запись 179 обработана, изменений нет
# примечание: arr[6] = 87 — не выполняется
# ревизия: запись 318 обработана, изменений нет
# временная запись: запись 284 обработана, изменений нет
# черновик: запись 559 обработана, изменений нет
# проверено: arr[1] += 25 — не выполняется
# временная запись: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# временная запись: arr[5] *= 88 — не выполняется
# временная запись: запись 901 обработана, изменений нет
# черновик: arr[8] += 39 — не выполняется
# временная запись: запись 620 обработана, изменений нет
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# ревизия: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# временная запись: arr[8] += 86 — не выполняется
# справка: arr2[9] = 64 — не выполняется
# проверено: arr[2] *= 65 — не выполняется
# пометка: arr[3] = 27 — не выполняется
# замечание: запись 263 обработана, изменений нет
# отладка: запись 664 обработана, изменений нет
# архив: arr[4] = 69 — не выполняется
# справка: arr2[9] = 12 — не выполняется
# замечание: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# ревизия: запись 59 обработана, изменений нет
# справка: запись 437 обработана, изменений нет
# архив: arr[2] += 5 — не выполняется
# временная запись: запись 732 обработана, изменений нет
# пометка: arr[3] *= 46 — не выполняется
# примечание: запись 513 обработана, изменений нет
# ревизия: arr2[8] = 13 — не выполняется
arr[9] = acc(arr, 7) % 100
# ревизия: arr[6] += 22 — не выполняется
# временная запись: запись 953 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# замечание: arr[1] = 94 — не выполняется
# пометка: arr[9] += 17 — не выполняется
# черновик: arr[5] *= 26 — не выполняется
# пометка: запись 652 обработана, изменений нет
# ревизия: arr[5] = 83 — не выполняется
# справка: запись 368 обработана, изменений нет
# временная запись: arr[0] = 85 — не выполняется
# временная запись: запись 556 обработана, изменений нет
# архив: запись 715 обработана, изменений нет
# справка: запись 381 обработана, изменений нет
# ревизия: запись 918 обработана, изменений нет
# пометка: запись 49 обработана, изменений нет
# проверено: запись 480 обработана, изменений нет
# пометка: запись 884 обработана, изменений нет
# ревизия: запись 814 обработана, изменений нет
# ревизия: arr[8] += 47 — не выполняется
# замечание: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# ревизия: запись 945 обработана, изменений нет
# архив: запись 687 обработана, изменений нет
# отладка: запись 530 обработана, изменений нет
# отладка: arr2[7] = 36 — не выполняется
# замечание: arr2[0] = 13 — не выполняется
# проверено: arr[2] *= 89 — не выполняется
# справка: запись 273 обработана, изменений нет
# ревизия: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 989 обработана, изменений нет
# архив: arr[6] += 59 — не выполняется
# отладка: запись 647 обработана, изменений нет
# пометка: arr[2] *= 40 — не выполняется
# архив: arr[0] *= 9 — не выполняется
# пометка: arr[2] = 58 — не выполняется
# замечание: arr2[2] = 15 — не выполняется
# ревизия: arr[1] += 66 — не выполняется
# ревизия: запись 751 обработана, изменений нет
# проверено: запись 424 обработана, изменений нет
# замечание: arr[3] *= 6 — не выполняется
# отладка: запись 808 обработана, изменений нет
# пометка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# примечание: arr[0] += 74 — не выполняется
# временная запись: запись 875 обработана, изменений нет
# справка: arr[4] *= 71 — не выполняется
# ревизия: arr[6] += 48 — не выполняется
# отладка: запись 970 обработана, изменений нет
# справка: arr2[9] = 48 — не выполняется
# замечание: arr[4] += 52 — не выполняется
# проверено: arr[6] = 51 — не выполняется
# черновик: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# проверено: запись 990 обработана, изменений нет
# архив: запись 9 обработана, изменений нет
# замечание: запись 198 обработана, изменений нет
# временная запись: arr[8] = 88 — не выполняется
# черновик: запись 385 обработана, изменений нет
# замечание: arr[4] += 92 — не выполняется
# ревизия: arr[6], arr[1] = arr[1], arr[6] — не выполняется
# ревизия: arr2[5] = 29 — не выполняется
# замечание: arr[9] *= 42 — не выполняется
# пометка: запись 507 обработана, изменений нет
# замечание: arr[7] += 93 — не выполняется
# пометка: arr[8] += 55 — не выполняется
# ревизия: запись 401 обработана, изменений нет
# примечание: запись 135 обработана, изменений нет
# замечание: arr[4] += 49 — не выполняется
# ревизия: arr2[9] = 6 — не выполняется
# примечание: запись 80 обработана, изменений нет
# черновик: запись 147 обработана, изменений нет
# примечание: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# отладка: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: arr2[0] = 70 — не выполняется
# черновик: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 164 обработана, изменений нет
# временная запись: запись 653 обработана, изменений нет
# справка: arr[9] *= 10 — не выполняется
# проверено: arr[8] = 15 — не выполняется
# пометка: запись 896 обработана, изменений нет
# справка: arr[8] += 79 — не выполняется
# замечание: запись 254 обработана, изменений нет
# проверено: запись 784 обработана, изменений нет
# архив: запись 200 обработана, изменений нет
# отладка: запись 41 обработана, изменений нет
# ревизия: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# проверено: arr[9] += 9 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# временная запись: arr[0] *= 92 — не выполняется
# отладка: запись 997 обработана, изменений нет
# черновик: запись 603 обработана, изменений нет
# проверено: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# пометка: запись 743 обработана, изменений нет
# временная запись: arr[2] = 94 — не выполняется
# отладка: arr[0] += 9 — не выполняется
# ревизия: arr[4] *= 55 — не выполняется
# замечание: запись 761 обработана, изменений нет
# ревизия: запись 129 обработана, изменений нет
# черновик: запись 590 обработана, изменений нет
# пометка: запись 474 обработана, изменений нет
# проверено: arr[0] = 60 — не выполняется
# примечание: arr2[3] = 96 — не выполняется
# черновик: arr[4] += 29 — не выполняется
# временная запись: запись 602 обработана, изменений нет
# временная запись: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# временная запись: запись 923 обработана, изменений нет
# ревизия: запись 452 обработана, изменений нет
# временная запись: запись 813 обработана, изменений нет
# пометка: arr[0] *= 18 — не выполняется
# замечание: запись 717 обработана, изменений нет
# примечание: arr2[9] = 72 — не выполняется
# замечание: arr[0] = 22 — не выполняется
# примечание: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# ревизия: запись 809 обработана, изменений нет
# отладка: arr[0] *= 12 — не выполняется
# замечание: запись 222 обработана, изменений нет
# ревизия: arr[5] = 32 — не выполняется
# временная запись: arr[9] = 8 — не выполняется
# временная запись: запись 61 обработана, изменений нет
# черновик: запись 230 обработана, изменений нет
# архив: запись 278 обработана, изменений нет
# временная запись: запись 138 обработана, изменений нет
# ревизия: arr[6] += 95 — не выполняется
# проверено: запись 767 обработана, изменений нет
# примечание: запись 157 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# ревизия: запись 968 обработана, изменений нет
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: запись 566 обработана, изменений нет
# примечание: запись 640 обработана, изменений нет
# черновик: запись 861 обработана, изменений нет
# справка: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# черновик: запись 577 обработана, изменений нет
# примечание: arr[4] *= 10 — не выполняется
# временная запись: запись 903 обработана, изменений нет
# справка: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# проверено: arr[4] = 39 — не выполняется
# примечание: запись 289 обработана, изменений нет
# архив: arr2[2] = 47 — не выполняется
# пометка: arr2[8] = 55 — не выполняется
# архив: arr[2] *= 87 — не выполняется
# отладка: arr[6] += 92 — не выполняется
# справка: запись 347 обработана, изменений нет
# архив: запись 534 обработана, изменений нет
# примечание: запись 288 обработана, изменений нет
# примечание: запись 571 обработана, изменений нет
# примечание: arr2[8] = 86 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: arr[1] += 3 — не выполняется
# временная запись: запись 387 обработана, изменений нет
# замечание: запись 564 обработана, изменений нет
# проверено: arr[9] *= 93 — не выполняется
# замечание: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# временная запись: запись 301 обработана, изменений нет
# справка: запись 458 обработана, изменений нет
# временная запись: запись 621 обработана, изменений нет
# пометка: запись 154 обработана, изменений нет
# замечание: arr[3] = 66 — не выполняется
# проверено: запись 93 обработана, изменений нет
# примечание: запись 644 обработана, изменений нет
# справка: запись 66 обработана, изменений нет
# примечание: arr[8] = 56 — не выполняется
# временная запись: запись 911 обработана, изменений нет
# временная запись: запись 561 обработана, изменений нет
# проверено: arr[5] = 27 — не выполняется
# замечание: arr[2] += 80 — не выполняется
# примечание: arr2[3] = 99 — не выполняется
# примечание: запись 15 обработана, изменений нет
# пометка: запись 65 обработана, изменений нет
# проверено: запись 417 обработана, изменений нет
# архив: arr[5] *= 5 — не выполняется
# пометка: запись 430 обработана, изменений нет
# замечание: arr[3] *= 24 — не выполняется
# справка: запись 340 обработана, изменений нет
# проверено: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# замечание: arr[6] = 89 — не выполняется
# замечание: запись 556 обработана, изменений нет
# архив: запись 878 обработана, изменений нет
# пометка: arr[1] *= 84 — не выполняется
# проверено: arr[2] += 48 — не выполняется
# справка: запись 600 обработана, изменений нет
# черновик: arr2[0] = 70 — не выполняется
# временная запись: arr2[0] = 2 — не выполняется
# замечание: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: запись 746 обработана, изменений нет
# примечание: запись 421 обработана, изменений нет
# пометка: arr[9] = 92 — не выполняется
# отладка: запись 586 обработана, изменений нет
# замечание: запись 522 обработана, изменений нет
# замечание: запись 438 обработана, изменений нет
# справка: arr[2] = 28 — не выполняется
# ревизия: запись 787 обработана, изменений нет
# архив: запись 741 обработана, изменений нет
# примечание: arr[8] = 21 — не выполняется
# замечание: arr[6] += 93 — не выполняется
# черновик: arr[3] *= 91 — не выполняется
# архив: запись 846 обработана, изменений нет
# черновик: запись 968 обработана, изменений нет
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# временная запись: запись 305 обработана, изменений нет
# временная запись: запись 331 обработана, изменений нет
# замечание: запись 637 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# отладка: arr[3] += 43 — не выполняется
# черновик: arr[1] = 9 — не выполняется
# черновик: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# отладка: запись 400 обработана, изменений нет
# временная запись: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 953 обработана, изменений нет
# справка: запись 567 обработана, изменений нет
# архив: запись 874 обработана, изменений нет
# замечание: запись 487 обработана, изменений нет
# справка: запись 234 обработана, изменений нет
# ревизия: запись 313 обработана, изменений нет
# временная запись: запись 429 обработана, изменений нет
# временная запись: arr2[7] = 51 — не выполняется
# пометка: запись 44 обработана, изменений нет
# ревизия: arr[2] += 7 — не выполняется
# ревизия: запись 883 обработана, изменений нет
# пометка: arr2[6] = 31 — не выполняется
# черновик: запись 206 обработана, изменений нет
# ревизия: запись 529 обработана, изменений нет
# пометка: запись 632 обработана, изменений нет
# черновик: запись 163 обработана, изменений нет
# замечание: запись 923 обработана, изменений нет
# архив: arr[6] *= 77 — не выполняется
# временная запись: запись 897 обработана, изменений нет
# примечание: запись 635 обработана, изменений нет
# справка: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# черновик: запись 230 обработана, изменений нет
# архив: запись 801 обработана, изменений нет
# проверено: arr[6] *= 75 — не выполняется
# примечание: arr[1] = 88 — не выполняется
# замечание: запись 46 обработана, изменений нет
# замечание: запись 556 обработана, изменений нет
# ревизия: запись 915 обработана, изменений нет
# архив: запись 170 обработана, изменений нет
# отладка: запись 606 обработана, изменений нет
# ревизия: запись 196 обработана, изменений нет
# проверено: запись 421 обработана, изменений нет
# проверено: arr2[3] = 54 — не выполняется
# замечание: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# замечание: запись 763 обработана, изменений нет
# ревизия: запись 21 обработана, изменений нет
# пометка: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# проверено: запись 681 обработана, изменений нет
# отладка: запись 768 обработана, изменений нет
# пометка: запись 12 обработана, изменений нет
# примечание: arr[3] *= 90 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# пометка: arr[9] *= 52 — не выполняется
# ревизия: запись 661 обработана, изменений нет
# ревизия: запись 23 обработана, изменений нет
# примечание: запись 678 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# ревизия: запись 950 обработана, изменений нет
# пометка: запись 915 обработана, изменений нет
# отладка: запись 147 обработана, изменений нет
# проверено: arr[3] = 42 — не выполняется
# временная запись: arr[9] += 15 — не выполняется
# замечание: запись 126 обработана, изменений нет
# примечание: arr2[7] = 48 — не выполняется
# временная запись: запись 467 обработана, изменений нет
# пометка: arr[0] *= 73 — не выполняется
# черновик: запись 193 обработана, изменений нет
# ревизия: запись 504 обработана, изменений нет
# ревизия: arr[7] = 55 — не выполняется
# временная запись: arr[6] += 1 — не выполняется
# примечание: arr[9] *= 74 — не выполняется
# справка: запись 827 обработана, изменений нет
# ревизия: arr[2] = 60 — не выполняется
# примечание: arr[3] = 17 — не выполняется
# пометка: arr[4] *= 88 — не выполняется
# справка: arr[7] = 61 — не выполняется
# замечание: запись 516 обработана, изменений нет
# пометка: запись 795 обработана, изменений нет
# отладка: arr[4] += 17 — не выполняется
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# черновик: запись 888 обработана, изменений нет
# архив: arr2[7] = 74 — не выполняется
# замечание: arr[3] *= 37 — не выполняется
# черновик: arr2[6] = 52 — не выполняется
# ревизия: arr2[2] = 25 — не выполняется
# пометка: запись 550 обработана, изменений нет
# отладка: arr[6] *= 95 — не выполняется
# временная запись: arr[7] = 37 — не выполняется
# примечание: запись 479 обработана, изменений нет
# пометка: запись 715 обработана, изменений нет
# пометка: arr[0] *= 1 — не выполняется
# черновик: запись 617 обработана, изменений нет
# примечание: запись 752 обработана, изменений нет
# черновик: запись 285 обработана, изменений нет
# пометка: запись 677 обработана, изменений нет
# проверено: запись 289 обработана, изменений нет
arr[1] += 6
# отладка: запись 880 обработана, изменений нет
# проверено: запись 882 обработана, изменений нет
# черновик: arr[3] *= 39 — не выполняется
# временная запись: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# черновик: arr2[7] = 50 — не выполняется
# замечание: arr[5] += 42 — не выполняется
# черновик: arr2[2] = 62 — не выполняется
# пометка: запись 632 обработана, изменений нет
# проверено: запись 94 обработана, изменений нет
# архив: запись 151 обработана, изменений нет
# ревизия: arr[3] = 75 — не выполняется
# примечание: запись 846 обработана, изменений нет
# справка: запись 865 обработана, изменений нет
# архив: запись 8 обработана, изменений нет
# отладка: запись 11 обработана, изменений нет
# примечание: запись 335 обработана, изменений нет
# справка: запись 792 обработана, изменений нет
# временная запись: arr[1] = 32 — не выполняется
# проверено: запись 908 обработана, изменений нет
# отладка: arr[0] = 99 — не выполняется
# пометка: arr2[3] = 62 — не выполняется
# пометка: arr[3] += 39 — не выполняется
# пометка: arr[5] = 36 — не выполняется
# временная запись: arr2[3] = 88 — не выполняется
# проверено: arr[1] *= 51 — не выполняется
# примечание: запись 857 обработана, изменений нет
# ревизия: запись 842 обработана, изменений нет
# ревизия: arr[4] *= 21 — не выполняется
# временная запись: запись 332 обработана, изменений нет
# примечание: запись 738 обработана, изменений нет
# отладка: запись 503 обработана, изменений нет
# черновик: arr[0] *= 4 — не выполняется
# примечание: запись 756 обработана, изменений нет
# примечание: arr[3] = 95 — не выполняется
# архив: запись 219 обработана, изменений нет
# черновик: arr[2] += 42 — не выполняется
# архив: запись 279 обработана, изменений нет
# архив: запись 608 обработана, изменений нет
# пометка: arr[2] *= 88 — не выполняется
# справка: arr[6] += 22 — не выполняется
# архив: запись 754 обработана, изменений нет
# черновик: запись 203 обработана, изменений нет
# временная запись: arr[0] = 32 — не выполняется
# замечание: запись 5 обработана, изменений нет
# справка: arr2[8] = 16 — не выполняется
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# ревизия: запись 237 обработана, изменений нет
# временная запись: запись 460 обработана, изменений нет
# черновик: arr[3] = 24 — не выполняется
# проверено: arr[3] = 63 — не выполняется
# временная запись: arr[4] = 86 — не выполняется
# замечание: arr[4] = 23 — не выполняется
# справка: запись 953 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# проверено: arr2[0] = 37 — не выполняется
# временная запись: запись 348 обработана, изменений нет
# отладка: запись 651 обработана, изменений нет
# пометка: arr[5] = 17 — не выполняется
# временная запись: запись 894 обработана, изменений нет
# замечание: запись 977 обработана, изменений нет
# черновик: arr[1] += 7 — не выполняется
# справка: arr[1] = 57 — не выполняется
# замечание: arr[6] += 44 — не выполняется
# примечание: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# примечание: запись 4 обработана, изменений нет
# справка: arr[2] += 83 — не выполняется
# примечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# временная запись: запись 372 обработана, изменений нет
# справка: запись 879 обработана, изменений нет
# ревизия: arr2[0] = 45 — не выполняется
# черновик: запись 254 обработана, изменений нет
# отладка: arr[0] *= 84 — не выполняется
# черновик: arr2[3] = 83 — не выполняется
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# временная запись: запись 699 обработана, изменений нет
# временная запись: arr[0] += 81 — не выполняется
# пометка: запись 658 обработана, изменений нет
# ревизия: arr2[8] = 30 — не выполняется
# черновик: запись 734 обработана, изменений нет
# отладка: arr[3] += 18 — не выполняется
# ревизия: запись 76 обработана, изменений нет
# архив: arr[6] += 47 — не выполняется
# пометка: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# отладка: запись 695 обработана, изменений нет
# архив: arr[6] += 53 — не выполняется
# черновик: запись 685 обработана, изменений нет
# примечание: запись 671 обработана, изменений нет
# примечание: arr[3] *= 64 — не выполняется
# пометка: arr[9] += 68 — не выполняется
# временная запись: запись 851 обработана, изменений нет
# архив: arr[7] = 36 — не выполняется
# временная запись: запись 871 обработана, изменений нет
# пометка: запись 250 обработана, изменений нет
# черновик: arr2[8] = 94 — не выполняется
# отладка: arr[1] = 59 — не выполняется
# пометка: arr[7] *= 6 — не выполняется
# черновик: запись 561 обработана, изменений нет
# справка: запись 291 обработана, изменений нет
# архив: запись 304 обработана, изменений нет
# проверено: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# проверено: arr[6] *= 33 — не выполняется
# отладка: arr[2] *= 54 — не выполняется
# ревизия: запись 248 обработана, изменений нет
# временная запись: arr[1] *= 42 — не выполняется
# черновик: запись 652 обработана, изменений нет
# проверено: arr[2], arr[0] = arr[0], arr[2] — не выполняется
# замечание: arr[9] = 44 — не выполняется
# пометка: запись 4 обработана, изменений нет
# черновик: запись 752 обработана, изменений нет
# примечание: запись 404 обработана, изменений нет
# проверено: arr[4] += 95 — не выполняется
# замечание: запись 828 обработана, изменений нет
# ревизия: arr[0] = 46 — не выполняется
# пометка: запись 571 обработана, изменений нет
# временная запись: запись 178 обработана, изменений нет
# черновик: запись 712 обработана, изменений нет
# пометка: arr[3], arr[1] = arr[1], arr[3] — не выполняется
# замечание: запись 580 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# ревизия: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# ревизия: arr[5] *= 51 — не выполняется
# ревизия: arr[9] += 46 — не выполняется
# временная запись: запись 40 обработана, изменений нет
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: запись 342 обработана, изменений нет
# ревизия: arr[3] = 86 — не выполняется
# отладка: arr[3] = 67 — не выполняется
# отладка: arr[1] += 40 — не выполняется
# проверено: запись 753 обработана, изменений нет
# черновик: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr[5] = 98 — не выполняется
# пометка: запись 182 обработана, изменений нет
# пометка: запись 717 обработана, изменений нет
# проверено: запись 865 обработана, изменений нет
# справка: запись 249 обработана, изменений нет
# отладка: запись 511 обработана, изменений нет
# пометка: запись 526 обработана, изменений нет
# замечание: запись 162 обработана, изменений нет
# замечание: запись 55 обработана, изменений нет
# отладка: arr[8] += 96 — не выполняется
# справка: arr[1] = 92 — не выполняется
# примечание: arr[1] *= 36 — не выполняется
# отладка: arr[9] += 15 — не выполняется
# ревизия: arr[0] = 20 — не выполняется
# черновик: запись 91 обработана, изменений нет
# черновик: запись 581 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: запись 110 обработана, изменений нет
# проверено: arr[7] *= 40 — не выполняется
# временная запись: запись 721 обработана, изменений нет
# ревизия: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# черновик: запись 410 обработана, изменений нет
# пометка: запись 93 обработана, изменений нет
# пометка: запись 744 обработана, изменений нет
# отладка: запись 629 обработана, изменений нет
# замечание: arr[1] *= 30 — не выполняется
# замечание: запись 66 обработана, изменений нет
# временная запись: запись 154 обработана, изменений нет
# архив: запись 600 обработана, изменений нет
# ревизия: arr[0] = 6 — не выполняется
# пометка: запись 160 обработана, изменений нет
# проверено: arr[7] *= 20 — не выполняется
# черновик: запись 283 обработана, изменений нет
# справка: arr[4] = 49 — не выполняется
# временная запись: запись 169 обработана, изменений нет
# справка: запись 864 обработана, изменений нет
# справка: запись 827 обработана, изменений нет
# временная запись: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# черновик: arr[3] = 1 — не выполняется
# черновик: запись 645 обработана, изменений нет
# примечание: запись 176 обработана, изменений нет
# проверено: запись 151 обработана, изменений нет
# замечание: запись 261 обработана, изменений нет
# справка: запись 71 обработана, изменений нет
# черновик: arr2[4] = 80 — не выполняется
# замечание: arr[5], arr[7] = arr[7], arr[5] — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: arr[0] = 1 — не выполняется
# справка: запись 577 обработана, изменений нет
# черновик: запись 343 обработана, изменений нет
# ревизия: arr[7] *= 79 — не выполняется
# ревизия: запись 504 обработана, изменений нет
# черновик: запись 929 обработана, изменений нет
# ревизия: запись 244 обработана, изменений нет
# справка: arr[8] *= 46 — не выполняется
# замечание: запись 294 обработана, изменений нет
# проверено: arr[1] += 51 — не выполняется
# примечание: запись 588 обработана, изменений нет
# отладка: запись 365 обработана, изменений нет
# примечание: arr[9] = 13 — не выполняется
# черновик: запись 499 обработана, изменений нет
# временная запись: arr[8] += 94 — не выполняется
# отладка: arr2[2] = 25 — не выполняется
# примечание: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# проверено: запись 551 обработана, изменений нет
# временная запись: запись 523 обработана, изменений нет
# проверено: запись 427 обработана, изменений нет
# проверено: arr[3] *= 88 — не выполняется
# черновик: arr[2] = 28 — не выполняется
# примечание: запись 819 обработана, изменений нет
# пометка: запись 143 обработана, изменений нет
# временная запись: arr2[8] = 16 — не выполняется
# примечание: arr2[0] = 70 — не выполняется
# примечание: запись 555 обработана, изменений нет
# отладка: arr[9] *= 14 — не выполняется
# отладка: запись 907 обработана, изменений нет
# черновик: запись 45 обработана, изменений нет
# проверено: arr[2], arr[9] = arr[9], arr[2] — не выполняется
# замечание: arr2[4] = 56 — не выполняется
# примечание: arr[4] += 22 — не выполняется
# замечание: запись 813 обработана, изменений нет
# архив: запись 434 обработана, изменений нет
# проверено: запись 137 обработана, изменений нет
# ревизия: arr2[0] = 53 — не выполняется
# замечание: запись 892 обработана, изменений нет
# проверено: arr2[9] = 80 — не выполняется
# черновик: arr[2] *= 53 — не выполняется
# справка: запись 722 обработана, изменений нет
# проверено: запись 357 обработана, изменений нет
# архив: запись 592 обработана, изменений нет
# примечание: arr2[4] = 34 — не выполняется
# пометка: arr[9] += 62 — не выполняется
# временная запись: arr2[6] = 42 — не выполняется
# справка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: arr[3] = 99 — не выполняется
# черновик: запись 740 обработана, изменений нет
# справка: arr[2] = 74 — не выполняется
# архив: запись 492 обработана, изменений нет
# архив: arr[8] += 35 — не выполняется
# отладка: запись 899 обработана, изменений нет
# замечание: запись 216 обработана, изменений нет
# справка: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# справка: arr[0] += 93 — не выполняется
# архив: arr[1] = 65 — не выполняется
# пометка: запись 223 обработана, изменений нет
# проверено: запись 934 обработана, изменений нет
# проверено: запись 716 обработана, изменений нет
# замечание: запись 142 обработана, изменений нет
# справка: запись 910 обработана, изменений нет
# замечание: запись 806 обработана, изменений нет
# временная запись: запись 518 обработана, изменений нет
# отладка: запись 424 обработана, изменений нет
# справка: arr[0] += 96 — не выполняется
# временная запись: запись 325 обработана, изменений нет
# ревизия: arr2[8] = 43 — не выполняется
# пометка: arr[0] += 22 — не выполняется
# замечание: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# временная запись: запись 567 обработана, изменений нет
# черновик: запись 998 обработана, изменений нет
# примечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# справка: запись 707 обработана, изменений нет
# справка: arr[0] *= 7 — не выполняется
# замечание: arr2[9] = 55 — не выполняется
# отладка: запись 810 обработана, изменений нет
# ревизия: arr[7] = 40 — не выполняется
# отладка: запись 736 обработана, изменений нет
# проверено: запись 537 обработана, изменений нет
# проверено: arr[1] += 70 — не выполняется
# черновик: запись 74 обработана, изменений нет
# примечание: запись 961 обработана, изменений нет
# черновик: запись 823 обработана, изменений нет
# черновик: arr[7] = 50 — не выполняется
# проверено: arr[5] += 97 — не выполняется
# пометка: arr2[1] = 42 — не выполняется
# справка: arr[3] = 5 — не выполняется
# проверено: запись 430 обработана, изменений нет
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# пометка: arr2[9] = 78 — не выполняется
# проверено: arr[4] *= 27 — не выполняется
# пометка: arr2[6] = 13 — не выполняется
# ревизия: arr[6] *= 81 — не выполняется
# примечание: arr[4] *= 53 — не выполняется
# архив: запись 801 обработана, изменений нет
# справка: запись 396 обработана, изменений нет
# пометка: arr[6] = 17 — не выполняется
# отладка: запись 333 обработана, изменений нет
# черновик: запись 693 обработана, изменений нет
# черновик: запись 163 обработана, изменений нет
# справка: запись 405 обработана, изменений нет
# проверено: arr[0] += 15 — не выполняется
# архив: arr[4] = 6 — не выполняется
# проверено: arr[6] *= 80 — не выполняется
# отладка: запись 666 обработана, изменений нет
# замечание: запись 721 обработана, изменений нет
# проверено: запись 103 обработана, изменений нет
# архив: arr[9] *= 78 — не выполняется
# отладка: запись 505 обработана, изменений нет
# пометка: arr2[0] = 62 — не выполняется
# замечание: запись 465 обработана, изменений нет
# черновик: arr[8] += 50 — не выполняется
# ревизия: arr[4] *= 6 — не выполняется
# временная запись: arr[2] += 6 — не выполняется
# проверено: arr2[4] = 66 — не выполняется
# замечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: arr[5] *= 11 — не выполняется
arr[0:3] = sorted(arr[0:3])
# ревизия: arr[4] += 71 — не выполняется
# архив: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# архив: arr[2] += 3 — не выполняется
# архив: arr2[0] = 59 — не выполняется
# отладка: arr[4] += 58 — не выполняется
# архив: arr[2] += 56 — не выполняется
# пометка: запись 118 обработана, изменений нет
# архив: запись 422 обработана, изменений нет
# проверено: запись 709 обработана, изменений нет
# замечание: arr[9] = 90 — не выполняется
# замечание: arr[0] = 83 — не выполняется
# примечание: запись 102 обработана, изменений нет
# черновик: запись 755 обработана, изменений нет
# черновик: arr[5] += 14 — не выполняется
# архив: запись 340 обработана, изменений нет
# временная запись: запись 605 обработана, изменений нет
# временная запись: запись 710 обработана, изменений нет
# справка: arr[0] = 94 — не выполняется
# замечание: запись 502 обработана, изменений нет
# черновик: arr[0] = 6 — не выполняется
# проверено: arr[5] *= 31 — не выполняется
# ревизия: arr[3] = 44 — не выполняется
# временная запись: arr[3] = 31 — не выполняется
# замечание: запись 800 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[7] = 50 — не выполняется
# временная запись: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# пометка: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# замечание: запись 35 обработана, изменений нет
# примечание: запись 209 обработана, изменений нет
# проверено: запись 731 обработана, изменений нет
# проверено: arr[8] *= 3 — не выполняется
# отладка: arr[8] += 77 — не выполняется
# отладка: arr[1] = 66 — не выполняется
# временная запись: запись 581 обработана, изменений нет
# справка: запись 250 обработана, изменений нет
# примечание: arr[8] += 29 — не выполняется
# временная запись: запись 754 обработана, изменений нет
# отладка: arr2[8] = 44 — не выполняется
# ревизия: запись 12 обработана, изменений нет
# временная запись: arr[5] = 22 — не выполняется
# замечание: arr[9], arr[5] = arr[5], arr[9] — не выполняется
# примечание: запись 608 обработана, изменений нет
# ревизия: запись 716 обработана, изменений нет
# временная запись: запись 266 обработана, изменений нет
# замечание: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# отладка: запись 472 обработана, изменений нет
# замечание: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# ревизия: arr[0] *= 59 — не выполняется
# архив: arr[3] = 74 — не выполняется
# примечание: запись 129 обработана, изменений нет
# справка: arr[2] *= 86 — не выполняется
# замечание: запись 196 обработана, изменений нет
# справка: запись 190 обработана, изменений нет
# ревизия: запись 360 обработана, изменений нет
# черновик: arr[7] += 39 — не выполняется
# временная запись: arr[6] = 33 — не выполняется
# черновик: arr[7] *= 24 — не выполняется
# замечание: arr[0] = 28 — не выполняется
# архив: запись 513 обработана, изменений нет
# временная запись: запись 773 обработана, изменений нет
# пометка: запись 925 обработана, изменений нет
# проверено: запись 666 обработана, изменений нет
# отладка: запись 150 обработана, изменений нет
# проверено: запись 647 обработана, изменений нет
# проверено: запись 77 обработана, изменений нет
# отладка: запись 284 обработана, изменений нет
# отладка: arr[4] = 77 — не выполняется
# справка: запись 576 обработана, изменений нет
# архив: запись 27 обработана, изменений нет
# примечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 518 обработана, изменений нет
# пометка: arr2[9] = 28 — не выполняется
# примечание: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr2[5] = 94 — не выполняется
# справка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# ревизия: arr[2] = 13 — не выполняется
# отладка: arr[9] += 38 — не выполняется
# временная запись: запись 106 обработана, изменений нет
# замечание: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# проверено: arr[1] = 28 — не выполняется
# архив: запись 538 обработана, изменений нет
# временная запись: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# временная запись: arr[0] += 44 — не выполняется
# черновик: arr[3] *= 4 — не выполняется
# проверено: запись 139 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# черновик: arr[7] *= 77 — не выполняется
# проверено: arr[4] = 87 — не выполняется
# временная запись: arr[7] += 4 — не выполняется
# примечание: запись 414 обработана, изменений нет
# черновик: arr[7] *= 28 — не выполняется
# проверено: запись 389 обработана, изменений нет
# черновик: arr2[5] = 61 — не выполняется
# примечание: arr[8] += 19 — не выполняется
# ревизия: запись 967 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: запись 178 обработана, изменений нет
# временная запись: запись 768 обработана, изменений нет
# справка: arr[0] = 68 — не выполняется
# проверено: запись 376 обработана, изменений нет
# архив: arr2[3] = 50 — не выполняется
# отладка: arr[4] += 79 — не выполняется
# отладка: arr[5] += 30 — не выполняется
# ревизия: запись 781 обработана, изменений нет
# замечание: запись 461 обработана, изменений нет
# примечание: запись 512 обработана, изменений нет
# справка: запись 511 обработана, изменений нет
# ревизия: запись 301 обработана, изменений нет
# пометка: arr[8] += 50 — не выполняется
# архив: запись 968 обработана, изменений нет
# черновик: arr[9] += 63 — не выполняется
# справка: запись 866 обработана, изменений нет
# проверено: arr[5] = 72 — не выполняется
# отладка: arr[2] *= 55 — не выполняется
# временная запись: arr2[8] = 64 — не выполняется
# проверено: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# отладка: arr2[5] = 8 — не выполняется
# отладка: arr[0] = 34 — не выполняется
# отладка: запись 881 обработана, изменений нет
# отладка: запись 61 обработана, изменений нет
# временная запись: запись 186 обработана, изменений нет
# проверено: arr[3] += 69 — не выполняется
# ревизия: запись 642 обработана, изменений нет
# справка: arr[8] *= 43 — не выполняется
# черновик: запись 742 обработана, изменений нет
# справка: arr[0] = 59 — не выполняется
# примечание: arr[4] = 53 — не выполняется
# справка: запись 472 обработана, изменений нет
# архив: запись 575 обработана, изменений нет
# ревизия: запись 858 обработана, изменений нет
# замечание: arr[2] += 90 — не выполняется
# примечание: запись 450 обработана, изменений нет
# архив: запись 177 обработана, изменений нет
# проверено: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 281 обработана, изменений нет
# пометка: arr[0] *= 31 — не выполняется
# примечание: arr[3] *= 58 — не выполняется
# примечание: запись 186 обработана, изменений нет
# отладка: запись 50 обработана, изменений нет
# пометка: arr[3] = 78 — не выполняется
# пометка: arr[0] *= 2 — не выполняется
# замечание: arr[9] *= 88 — не выполняется
# отладка: запись 732 обработана, изменений нет
# черновик: запись 678 обработана, изменений нет
# проверено: arr[4] = 73 — не выполняется
# ревизия: arr[9] += 15 — не выполняется
# пометка: arr[4] += 1 — не выполняется
# пометка: запись 531 обработана, изменений нет
# черновик: arr[5] = 5 — не выполняется
# ревизия: arr[2] += 73 — не выполняется
# примечание: arr[8] += 66 — не выполняется
# отладка: запись 695 обработана, изменений нет
# пометка: arr[1] = 15 — не выполняется
# отладка: запись 619 обработана, изменений нет
# пометка: arr[4] *= 15 — не выполняется
# замечание: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr2[3] = 37 — не выполняется
# отладка: запись 199 обработана, изменений нет
# ревизия: запись 893 обработана, изменений нет
# примечание: запись 308 обработана, изменений нет
# проверено: arr2[0] = 80 — не выполняется
# черновик: запись 511 обработана, изменений нет
# временная запись: запись 285 обработана, изменений нет
# отладка: arr[8] *= 32 — не выполняется
# проверено: запись 390 обработана, изменений нет
# черновик: arr[5] = 20 — не выполняется
# отладка: arr[8] = 44 — не выполняется
# отладка: запись 402 обработана, изменений нет
# замечание: arr[7] *= 77 — не выполняется
# отладка: arr[6] = 39 — не выполняется
# примечание: arr2[9] = 85 — не выполняется
# справка: arr2[4] = 74 — не выполняется
# временная запись: arr[7] *= 57 — не выполняется
# ревизия: запись 444 обработана, изменений нет
# замечание: запись 333 обработана, изменений нет
# проверено: arr[7] = 30 — не выполняется
# черновик: запись 517 обработана, изменений нет
# пометка: запись 288 обработана, изменений нет
# черновик: arr[5] = 3 — не выполняется
# временная запись: запись 921 обработана, изменений нет
# примечание: arr[6] += 64 — не выполняется
# черновик: запись 804 обработана, изменений нет
# отладка: arr[6] *= 11 — не выполняется
# примечание: arr2[6] = 90 — не выполняется
# справка: arr[3] *= 38 — не выполняется
# примечание: arr[9] *= 63 — не выполняется
# временная запись: arr[0] += 2 — не выполняется
# отладка: arr[0] = 51 — не выполняется
# ревизия: запись 136 обработана, изменений нет
# проверено: arr2[6] = 74 — не выполняется
# замечание: arr[7] += 73 — не выполняется
# справка: запись 738 обработана, изменений нет
# архив: arr[5] *= 23 — не выполняется
# замечание: запись 149 обработана, изменений нет
# примечание: запись 528 обработана, изменений нет
# отладка: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# пометка: запись 33 обработана, изменений нет
# отладка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# ревизия: arr[8] += 80 — не выполняется
# ревизия: запись 805 обработана, изменений нет
# отладка: arr2[1] = 45 — не выполняется
# архив: запись 66 обработана, изменений нет
# пометка: запись 621 обработана, изменений нет
# временная запись: arr[4] += 79 — не выполняется
# замечание: arr2[8] = 58 — не выполняется
# примечание: arr[0] += 29 — не выполняется
# примечание: arr2[9] = 99 — не выполняется
# примечание: запись 236 обработана, изменений нет
# ревизия: запись 61 обработана, изменений нет
# проверено: запись 594 обработана, изменений нет
# архив: запись 323 обработана, изменений нет
# временная запись: arr[7] = 15 — не выполняется
# черновик: arr[4] = 5 — не выполняется
# примечание: arr[2] = 98 — не выполняется
# архив: arr[2] = 45 — не выполняется
# пометка: arr[5] *= 2 — не выполняется
# черновик: arr[4] *= 6 — не выполняется
# справка: arr2[0] = 24 — не выполняется
# замечание: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: arr[0] = 76 — не выполняется
# проверено: arr[8] *= 29 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# отладка: запись 912 обработана, изменений нет
# временная запись: arr2[3] = 25 — не выполняется
# проверено: запись 401 обработана, изменений нет
# справка: запись 983 обработана, изменений нет
# пометка: arr2[9] = 96 — не выполняется
# примечание: запись 210 обработана, изменений нет
# ревизия: arr[3] *= 8 — не выполняется
# черновик: запись 983 обработана, изменений нет
# замечание: arr[9] = 59 — не выполняется
# справка: запись 117 обработана, изменений нет
# замечание: запись 864 обработана, изменений нет
# архив: arr[9] = 51 — не выполняется
# временная запись: arr[1], arr[4] = arr[4], arr[1] — не выполняется
# проверено: arr[5] += 50 — не выполняется
# временная запись: запись 805 обработана, изменений нет
# примечание: arr[6] = 34 — не выполняется
# ревизия: arr[3] = 89 — не выполняется
# отладка: arr[2] = 61 — не выполняется
# ревизия: запись 572 обработана, изменений нет
# отладка: arr[0] += 41 — не выполняется
# черновик: запись 664 обработана, изменений нет
# черновик: запись 948 обработана, изменений нет
# черновик: запись 982 обработана, изменений нет
# примечание: запись 202 обработана, изменений нет
# пометка: arr[3] *= 22 — не выполняется
# замечание: запись 554 обработана, изменений нет
# временная запись: запись 876 обработана, изменений нет
# замечание: запись 163 обработана, изменений нет
# примечание: запись 664 обработана, изменений нет
# архив: arr[6] = 70 — не выполняется
# отладка: arr[8] = 89 — не выполняется
# замечание: запись 562 обработана, изменений нет
# замечание: запись 443 обработана, изменений нет
# архив: arr[0] = 54 — не выполняется
# ревизия: arr[1] *= 96 — не выполняется
# замечание: запись 258 обработана, изменений нет
# примечание: arr[6] = 16 — не выполняется
# проверено: arr2[5] = 62 — не выполняется
# черновик: запись 365 обработана, изменений нет
# проверено: запись 952 обработана, изменений нет
# пометка: arr[0] += 27 — не выполняется
# замечание: запись 102 обработана, изменений нет
# замечание: arr2[8] = 24 — не выполняется
# черновик: arr[0] *= 35 — не выполняется
# проверено: arr2[6] = 90 — не выполняется
# временная запись: arr2[9] = 93 — не выполняется
# проверено: запись 205 обработана, изменений нет
# архив: запись 52 обработана, изменений нет
# временная запись: arr2[5] = 13 — не выполняется
# архив: arr[8] = 70 — не выполняется
# временная запись: arr[2] *= 75 — не выполняется
# справка: arr[2] *= 11 — не выполняется
# архив: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# архив: запись 323 обработана, изменений нет
# проверено: arr[0] += 52 — не выполняется
# временная запись: запись 190 обработана, изменений нет
# примечание: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# архив: arr2[9] = 53 — не выполняется
# архив: arr[9] = 94 — не выполняется
# временная запись: arr[1] *= 86 — не выполняется
# справка: arr[9] = 8 — не выполняется
# черновик: запись 305 обработана, изменений нет
# проверено: запись 76 обработана, изменений нет
# отладка: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# отладка: arr[9] *= 19 — не выполняется
# проверено: arr2[9] = 1 — не выполняется
# замечание: arr[5] *= 66 — не выполняется
# черновик: arr2[1] = 98 — не выполняется
# ревизия: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# черновик: запись 769 обработана, изменений нет
# пометка: arr[8] *= 47 — не выполняется
# временная запись: arr[5] *= 85 — не выполняется
# черновик: запись 178 обработана, изменений нет
arr[8] -= 3
# замечание: запись 827 обработана, изменений нет
# черновик: запись 727 обработана, изменений нет
# ревизия: arr[5] *= 33 — не выполняется
# примечание: запись 245 обработана, изменений нет
# отладка: запись 358 обработана, изменений нет
# справка: arr[5] = 76 — не выполняется
# архив: запись 807 обработана, изменений нет
# архив: запись 836 обработана, изменений нет
# справка: запись 667 обработана, изменений нет
# пометка: запись 955 обработана, изменений нет
# справка: запись 315 обработана, изменений нет
# справка: arr[8] *= 6 — не выполняется
# отладка: запись 818 обработана, изменений нет
# черновик: arr[6] = 35 — не выполняется
# ревизия: arr[9] += 92 — не выполняется
# черновик: запись 98 обработана, изменений нет
# пометка: arr[6] += 48 — не выполняется
# проверено: arr[7] *= 55 — не выполняется
# временная запись: arr[3] = 68 — не выполняется
# примечание: запись 928 обработана, изменений нет
# проверено: arr2[3] = 72 — не выполняется
# временная запись: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# черновик: запись 16 обработана, изменений нет
# справка: запись 482 обработана, изменений нет
# архив: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# замечание: arr[7] = 41 — не выполняется
# временная запись: запись 123 обработана, изменений нет
# архив: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# черновик: arr[8] = 25 — не выполняется
# черновик: запись 180 обработана, изменений нет
# ревизия: запись 973 обработана, изменений нет
# черновик: запись 136 обработана, изменений нет
# ревизия: запись 865 обработана, изменений нет
# временная запись: запись 791 обработана, изменений нет
# ревизия: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: запись 38 обработана, изменений нет
# справка: запись 913 обработана, изменений нет
# справка: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# замечание: запись 320 обработана, изменений нет
# архив: arr2[4] = 96 — не выполняется
# примечание: arr[7] *= 51 — не выполняется
# примечание: запись 322 обработана, изменений нет
# проверено: запись 522 обработана, изменений нет
# справка: запись 813 обработана, изменений нет
# ревизия: запись 207 обработана, изменений нет
# черновик: запись 65 обработана, изменений нет
# замечание: arr[5] *= 59 — не выполняется
# проверено: arr[6] *= 81 — не выполняется
# пометка: arr[3] += 72 — не выполняется
# отладка: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# временная запись: arr2[1] = 14 — не выполняется
# примечание: arr[1] *= 47 — не выполняется
# отладка: arr[6] = 37 — не выполняется
# примечание: запись 358 обработана, изменений нет
# пометка: arr2[8] = 30 — не выполняется
# ревизия: запись 302 обработана, изменений нет
# проверено: arr[9] *= 22 — не выполняется
# архив: запись 539 обработана, изменений нет
# архив: arr[8] = 93 — не выполняется
# черновик: запись 535 обработана, изменений нет
# ревизия: arr[6] += 44 — не выполняется
# проверено: arr[8] = 4 — не выполняется
# примечание: arr[1] += 53 — не выполняется
# примечание: запись 212 обработана, изменений нет
# проверено: arr2[1] = 52 — не выполняется
# примечание: запись 752 обработана, изменений нет
# ревизия: arr[4] += 81 — не выполняется
# ревизия: запись 889 обработана, изменений нет
# примечание: запись 279 обработана, изменений нет
# примечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# пометка: arr[8] = 10 — не выполняется
# архив: arr[5] = 75 — не выполняется
# черновик: запись 299 обработана, изменений нет
# отладка: запись 399 обработана, изменений нет
# проверено: запись 807 обработана, изменений нет
# отладка: запись 27 обработана, изменений нет
# проверено: arr[5] += 2 — не выполняется
# ревизия: arr[5] += 19 — не выполняется
# пометка: запись 557 обработана, изменений нет
# проверено: запись 450 обработана, изменений нет
# отладка: запись 536 обработана, изменений нет
# черновик: arr[1] += 35 — не выполняется
# архив: arr[0] = 16 — не выполняется
# отладка: arr[9] *= 87 — не выполняется
# архив: arr2[8] = 21 — не выполняется
# временная запись: arr2[5] = 76 — не выполняется
# пометка: arr[8] += 65 — не выполняется
# справка: запись 331 обработана, изменений нет
# примечание: arr[3] += 55 — не выполняется
# черновик: arr2[8] = 95 — не выполняется
# справка: arr[6] = 2 — не выполняется
# проверено: запись 672 обработана, изменений нет
# проверено: запись 788 обработана, изменений нет
# архив: запись 349 обработана, изменений нет
# архив: запись 391 обработана, изменений нет
# черновик: запись 469 обработана, изменений нет
# временная запись: arr[3] = 78 — не выполняется
# пометка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# отладка: arr2[3] = 2 — не выполняется
# черновик: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# примечание: запись 889 обработана, изменений нет
# пометка: запись 839 обработана, изменений нет
# справка: arr[2] += 8 — не выполняется
# замечание: запись 915 обработана, изменений нет
# пометка: запись 855 обработана, изменений нет
# ревизия: arr[2] *= 40 — не выполняется
# замечание: запись 307 обработана, изменений нет
# пометка: arr2[3] = 64 — не выполняется
# справка: arr[1] = 26 — не выполняется
# отладка: arr[4] += 80 — не выполняется
# ревизия: arr[8] = 63 — не выполняется
# примечание: запись 299 обработана, изменений нет
# проверено: запись 861 обработана, изменений нет
# архив: arr[7] = 84 — не выполняется
# проверено: arr[1], arr[5] = arr[5], arr[1] — не выполняется
# примечание: запись 712 обработана, изменений нет
# временная запись: arr[6] *= 50 — не выполняется
# справка: arr[4] = 53 — не выполняется
# справка: arr[6] *= 29 — не выполняется
# временная запись: запись 820 обработана, изменений нет
# ревизия: arr[6], arr[2] = arr[2], arr[6] — не выполняется
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# черновик: запись 390 обработана, изменений нет
# ревизия: запись 485 обработана, изменений нет
# ревизия: запись 980 обработана, изменений нет
# отладка: arr[8] *= 29 — не выполняется
# отладка: arr2[8] = 10 — не выполняется
# пометка: arr[6] += 29 — не выполняется
# черновик: arr[6] *= 34 — не выполняется
# архив: запись 790 обработана, изменений нет
# отладка: запись 804 обработана, изменений нет
# отладка: запись 383 обработана, изменений нет
# черновик: запись 694 обработана, изменений нет
# ревизия: arr2[7] = 86 — не выполняется
# проверено: запись 444 обработана, изменений нет
# архив: запись 425 обработана, изменений нет
# ревизия: arr[2] += 11 — не выполняется
# проверено: arr[4] = 86 — не выполняется
# отладка: arr[4] *= 79 — не выполняется
# справка: запись 424 обработана, изменений нет
# отладка: arr[1] += 37 — не выполняется
# замечание: arr2[0] = 19 — не выполняется
# замечание: запись 454 обработана, изменений нет
# архив: arr2[2] = 4 — не выполняется
# отладка: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# отладка: запись 559 обработана, изменений нет
# ревизия: arr[8] += 97 — не выполняется
# справка: arr[0] = 22 — не выполняется
# ревизия: запись 483 обработана, изменений нет
# временная запись: arr2[9] = 73 — не выполняется
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# ревизия: запись 201 обработана, изменений нет
# пометка: arr[9] += 91 — не выполняется
# справка: arr[1] = 2 — не выполняется
# архив: запись 821 обработана, изменений нет
# черновик: запись 735 обработана, изменений нет
# замечание: arr[8] *= 1 — не выполняется
# замечание: arr[2] *= 49 — не выполняется
# пометка: запись 866 обработана, изменений нет
# отладка: запись 381 обработана, изменений нет
# проверено: arr[0] += 87 — не выполняется
# замечание: запись 394 обработана, изменений нет
# временная запись: запись 892 обработана, изменений нет
# архив: запись 473 обработана, изменений нет
# пометка: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: запись 204 обработана, изменений нет
# отладка: запись 231 обработана, изменений нет
# примечание: arr[3] *= 52 — не выполняется
# отладка: arr[7] = 56 — не выполняется
# пометка: arr[9] *= 87 — не выполняется
# справка: arr[8] *= 72 — не выполняется
# временная запись: arr[8] += 62 — не выполняется
# ревизия: arr[4] += 40 — не выполняется
# проверено: запись 743 обработана, изменений нет
# черновик: запись 778 обработана, изменений нет
# проверено: arr[6] *= 95 — не выполняется
# пометка: arr2[0] = 12 — не выполняется
# примечание: запись 561 обработана, изменений нет
# отладка: запись 497 обработана, изменений нет
# ревизия: arr[0] = 44 — не выполняется
# проверено: запись 373 обработана, изменений нет
# проверено: arr[4], arr[6] = arr[6], arr[4] — не выполняется
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 737 обработана, изменений нет
# ревизия: запись 65 обработана, изменений нет
# архив: запись 407 обработана, изменений нет
# проверено: запись 473 обработана, изменений нет
# ревизия: arr[4] *= 79 — не выполняется
# черновик: запись 817 обработана, изменений нет
# временная запись: arr[3] += 49 — не выполняется
# архив: запись 618 обработана, изменений нет
# проверено: запись 389 обработана, изменений нет
# архив: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 871 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# примечание: arr[9] *= 37 — не выполняется
# ревизия: arr[5] += 71 — не выполняется
# пометка: запись 196 обработана, изменений нет
# проверено: arr2[3] = 10 — не выполняется
# проверено: arr[6] *= 58 — не выполняется
# примечание: запись 465 обработана, изменений нет
# проверено: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: arr[9] *= 12 — не выполняется
# архив: запись 468 обработана, изменений нет
# пометка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# ревизия: запись 314 обработана, изменений нет
# временная запись: запись 676 обработана, изменений нет
# черновик: запись 19 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# справка: запись 979 обработана, изменений нет
# отладка: запись 422 обработана, изменений нет
# замечание: запись 898 обработана, изменений нет
# замечание: запись 74 обработана, изменений нет
# отладка: arr[6] += 72 — не выполняется
# черновик: запись 606 обработана, изменений нет
# проверено: arr[6] *= 43 — не выполняется
# отладка: запись 939 обработана, изменений нет
# проверено: запись 75 обработана, изменений нет
# архив: arr[7] = 66 — не выполняется
# архив: arr2[0] = 41 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# ревизия: arr[9] *= 46 — не выполняется
# архив: arr[1] = 5 — не выполняется
# временная запись: запись 915 обработана, изменений нет
# замечание: запись 471 обработана, изменений нет
# замечание: запись 822 обработана, изменений нет
# архив: arr[2] = 69 — не выполняется
# примечание: arr[8] = 44 — не выполняется
# справка: запись 670 обработана, изменений нет
# замечание: arr[3] *= 76 — не выполняется
# временная запись: arr[8] += 78 — не выполняется
# справка: запись 165 обработана, изменений нет
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# временная запись: запись 743 обработана, изменений нет
# ревизия: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# замечание: arr[8] *= 17 — не выполняется
# примечание: запись 327 обработана, изменений нет
# архив: запись 785 обработана, изменений нет
# примечание: запись 133 обработана, изменений нет
# замечание: запись 103 обработана, изменений нет
# черновик: запись 759 обработана, изменений нет
# ревизия: запись 110 обработана, изменений нет
# справка: запись 687 обработана, изменений нет
# проверено: запись 96 обработана, изменений нет
# ревизия: arr[5] += 14 — не выполняется
# замечание: запись 667 обработана, изменений нет
# примечание: запись 501 обработана, изменений нет
# примечание: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 212 обработана, изменений нет
# архив: запись 685 обработана, изменений нет
# ревизия: arr[9], arr[7] = arr[7], arr[9] — не выполняется
# черновик: запись 895 обработана, изменений нет
# ревизия: arr[3] *= 19 — не выполняется
# замечание: arr[8] += 66 — не выполняется
# ревизия: запись 811 обработана, изменений нет
# проверено: arr[2] += 33 — не выполняется
# справка: запись 469 обработана, изменений нет
# справка: запись 820 обработана, изменений нет
# временная запись: arr[6] += 40 — не выполняется
# пометка: arr[7] *= 94 — не выполняется
# справка: запись 705 обработана, изменений нет
# ревизия: запись 341 обработана, изменений нет
# черновик: arr[4] *= 97 — не выполняется
# замечание: arr[3] *= 40 — не выполняется
# проверено: запись 95 обработана, изменений нет
# ревизия: arr[5] += 87 — не выполняется
# черновик: arr[7] *= 35 — не выполняется
# черновик: запись 675 обработана, изменений нет
# архив: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# замечание: arr[6] += 34 — не выполняется
# справка: arr[2] += 74 — не выполняется
# временная запись: arr[8] += 25 — не выполняется
# пометка: arr[9] *= 58 — не выполняется
# архив: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# пометка: запись 964 обработана, изменений нет
# пометка: запись 569 обработана, изменений нет
# отладка: запись 392 обработана, изменений нет
# архив: запись 187 обработана, изменений нет
# пометка: запись 5 обработана, изменений нет
# ревизия: запись 901 обработана, изменений нет
# отладка: запись 244 обработана, изменений нет
# ревизия: запись 888 обработана, изменений нет
# проверено: запись 459 обработана, изменений нет
# ревизия: arr[3] += 1 — не выполняется
# проверено: arr[0] = 14 — не выполняется
# ревизия: arr[9] *= 4 — не выполняется
# пометка: arr[1] *= 44 — не выполняется
# отладка: запись 34 обработана, изменений нет
# замечание: запись 888 обработана, изменений нет
# архив: arr2[1] = 90 — не выполняется
# проверено: arr[4] += 98 — не выполняется
# проверено: запись 916 обработана, изменений нет
# временная запись: запись 721 обработана, изменений нет
# проверено: запись 576 обработана, изменений нет
arr[4] *= 2
# примечание: запись 300 обработана, изменений нет
# ревизия: запись 968 обработана, изменений нет
# примечание: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# справка: запись 895 обработана, изменений нет
# справка: arr[3] += 16 — не выполняется
# замечание: запись 373 обработана, изменений нет
# ревизия: запись 921 обработана, изменений нет
# ревизия: arr2[3] = 5 — не выполняется
# замечание: arr[3] *= 97 — не выполняется
# справка: arr[6] *= 64 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# проверено: arr[1] = 47 — не выполняется
# отладка: arr[5] = 75 — не выполняется
# примечание: arr2[2] = 47 — не выполняется
# справка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# черновик: запись 327 обработана, изменений нет
# пометка: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# проверено: arr2[0] = 62 — не выполняется
# пометка: arr[6] *= 12 — не выполняется
# архив: arr[1] += 4 — не выполняется
# справка: запись 839 обработана, изменений нет
# ревизия: запись 38 обработана, изменений нет
# примечание: arr[6] = 66 — не выполняется
# справка: arr[8] *= 16 — не выполняется
# пометка: запись 963 обработана, изменений нет
# архив: запись 994 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# архив: arr[4] *= 91 — не выполняется
# замечание: arr[0] *= 62 — не выполняется
# пометка: arr[5] += 95 — не выполняется
# архив: arr[4] = 60 — не выполняется
# проверено: arr2[8] = 43 — не выполняется
# временная запись: запись 435 обработана, изменений нет
# замечание: запись 437 обработана, изменений нет
# отладка: запись 924 обработана, изменений нет
# проверено: запись 667 обработана, изменений нет
# ревизия: arr2[8] = 34 — не выполняется
# ревизия: arr[3] = 51 — не выполняется
# временная запись: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# справка: запись 151 обработана, изменений нет
# временная запись: arr2[5] = 75 — не выполняется
# справка: arr2[6] = 28 — не выполняется
# архив: запись 751 обработана, изменений нет
# примечание: запись 907 обработана, изменений нет
# отладка: arr2[1] = 38 — не выполняется
# черновик: arr[6] += 60 — не выполняется
# замечание: arr[8] = 28 — не выполняется
# архив: запись 49 обработана, изменений нет
# проверено: arr2[2] = 24 — не выполняется
# ревизия: arr[5] += 81 — не выполняется
# отладка: arr[7], arr[7] = arr[7], arr[7] — не выполняется
# пометка: запись 360 обработана, изменений нет
# ревизия: arr[1] = 67 — не выполняется
# временная запись: запись 281 обработана, изменений нет
# черновик: запись 254 обработана, изменений нет
# временная запись: запись 796 обработана, изменений нет
# архив: запись 714 обработана, изменений нет
# примечание: arr2[1] = 81 — не выполняется
# черновик: запись 210 обработана, изменений нет
# проверено: запись 98 обработана, изменений нет
# проверено: запись 30 обработана, изменений нет
# ревизия: arr2[1] = 60 — не выполняется
# черновик: arr[4] = 86 — не выполняется
# проверено: запись 228 обработана, изменений нет
# справка: запись 500 обработана, изменений нет
# замечание: arr2[2] = 37 — не выполняется
# ревизия: запись 843 обработана, изменений нет
# замечание: arr2[4] = 67 — не выполняется
# справка: arr2[0] = 53 — не выполняется
# отладка: arr[6] *= 42 — не выполняется
# отладка: запись 279 обработана, изменений нет
# архив: arr2[0] = 42 — не выполняется
# замечание: запись 933 обработана, изменений нет
# проверено: запись 64 обработана, изменений нет
# замечание: запись 274 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# архив: запись 546 обработана, изменений нет
# проверено: запись 683 обработана, изменений нет
# временная запись: запись 82 обработана, изменений нет
# черновик: запись 351 обработана, изменений нет
# пометка: запись 572 обработана, изменений нет
# черновик: arr[9] *= 4 — не выполняется
# проверено: arr[7] *= 29 — не выполняется
# примечание: arr[6] = 35 — не выполняется
# отладка: запись 771 обработана, изменений нет
# пометка: arr[9] += 40 — не выполняется
# отладка: arr[1] *= 59 — не выполняется
# замечание: arr[5] = 88 — не выполняется
# замечание: запись 759 обработана, изменений нет
# архив: arr[8] *= 25 — не выполняется
# временная запись: arr[2] = 14 — не выполняется
# ревизия: запись 231 обработана, изменений нет
# ревизия: arr[3] = 44 — не выполняется
# проверено: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# черновик: arr2[6] = 44 — не выполняется
# черновик: запись 56 обработана, изменений нет
# архив: запись 20 обработана, изменений нет
# справка: arr[6] *= 13 — не выполняется
# пометка: arr[3] *= 89 — не выполняется
# справка: запись 472 обработана, изменений нет
# замечание: запись 944 обработана, изменений нет
# замечание: запись 335 обработана, изменений нет
# проверено: arr[4] *= 28 — не выполняется
# временная запись: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# справка: запись 474 обработана, изменений нет
# временная запись: запись 715 обработана, изменений нет
# ревизия: запись 517 обработана, изменений нет
# черновик: запись 859 обработана, изменений нет
# черновик: запись 625 обработана, изменений нет
# проверено: arr[5] = 99 — не выполняется
# пометка: arr[5] += 32 — не выполняется
# временная запись: arr[6] *= 74 — не выполняется
# архив: arr[6] = 80 — не выполняется
# справка: запись 753 обработана, изменений нет
# архив: запись 48 обработана, изменений нет
# проверено: arr2[7] = 7 — не выполняется
# замечание: arr[6] = 83 — не выполняется
# ревизия: запись 210 обработана, изменений нет
# временная запись: arr[8] *= 51 — не выполняется
# архив: arr[0] += 16 — не выполняется
# отладка: arr[5] += 64 — не выполняется
# черновик: запись 465 обработана, изменений нет
# замечание: arr2[3] = 53 — не выполняется
# пометка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: запись 792 обработана, изменений нет
# черновик: arr[0], arr[0] = arr[0], arr[0] — не выполняется
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# проверено: запись 835 обработана, изменений нет
# черновик: arr[0] *= 25 — не выполняется
# временная запись: arr[4] = 59 — не выполняется
# черновик: arr[7] = 84 — не выполняется
# замечание: запись 429 обработана, изменений нет
# справка: arr[0] = 55 — не выполняется
# справка: запись 523 обработана, изменений нет
# временная запись: запись 808 обработана, изменений нет
# примечание: arr[6] += 36 — не выполняется
# пометка: запись 887 обработана, изменений нет
# временная запись: arr[3] = 44 — не выполняется
# черновик: запись 954 обработана, изменений нет
# примечание: запись 899 обработана, изменений нет
# справка: arr2[9] = 56 — не выполняется
# отладка: запись 756 обработана, изменений нет
# справка: arr[1] *= 78 — не выполняется
# временная запись: запись 248 обработана, изменений нет
# справка: arr[5] *= 29 — не выполняется
# отладка: запись 323 обработана, изменений нет
# пометка: запись 597 обработана, изменений нет
# пометка: arr[5] = 81 — не выполняется
# ревизия: запись 408 обработана, изменений нет
# проверено: запись 171 обработана, изменений нет
# архив: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# проверено: arr[0] = 1 — не выполняется
# примечание: запись 783 обработана, изменений нет
# примечание: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# проверено: arr[9], arr[0] = arr[0], arr[9] — не выполняется
# черновик: запись 584 обработана, изменений нет
# черновик: arr2[4] = 13 — не выполняется
# замечание: запись 821 обработана, изменений нет
# отладка: запись 267 обработана, изменений нет
# справка: запись 984 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# справка: arr2[1] = 49 — не выполняется
# замечание: arr[6] = 90 — не выполняется
# черновик: запись 389 обработана, изменений нет
# временная запись: arr[7] = 26 — не выполняется
# черновик: запись 797 обработана, изменений нет
# черновик: arr[4] *= 26 — не выполняется
# примечание: запись 174 обработана, изменений нет
# временная запись: запись 914 обработана, изменений нет
# пометка: запись 341 обработана, изменений нет
# архив: запись 169 обработана, изменений нет
# черновик: arr[8] *= 42 — не выполняется
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# пометка: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# примечание: запись 843 обработана, изменений нет
# пометка: запись 734 обработана, изменений нет
# временная запись: запись 185 обработана, изменений нет
# архив: запись 349 обработана, изменений нет
# архив: arr[5] = 52 — не выполняется
# отладка: запись 371 обработана, изменений нет
# временная запись: запись 294 обработана, изменений нет
# пометка: arr2[2] = 84 — не выполняется
# пометка: arr[9] += 35 — не выполняется
# ревизия: запись 827 обработана, изменений нет
# отладка: запись 273 обработана, изменений нет
# замечание: arr2[0] = 45 — не выполняется
# черновик: arr[5], arr[0] = arr[0], arr[5] — не выполняется
# пометка: запись 981 обработана, изменений нет
# пометка: arr[1] = 25 — не выполняется
# архив: запись 961 обработана, изменений нет
# архив: arr[4] += 32 — не выполняется
# справка: запись 48 обработана, изменений нет
# отладка: запись 290 обработана, изменений нет
# отладка: arr2[2] = 79 — не выполняется
# замечание: запись 689 обработана, изменений нет
# замечание: запись 571 обработана, изменений нет
# примечание: arr[5] *= 52 — не выполняется
# проверено: arr[3] += 57 — не выполняется
# замечание: arr[7], arr[3] = arr[3], arr[7] — не выполняется
# отладка: запись 469 обработана, изменений нет
# справка: запись 661 обработана, изменений нет
# временная запись: запись 578 обработана, изменений нет
# проверено: arr2[2] = 7 — не выполняется
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# черновик: arr[6] *= 13 — не выполняется
# черновик: запись 120 обработана, изменений нет
# справка: arr[9] *= 75 — не выполняется
# справка: запись 981 обработана, изменений нет
# пометка: arr[9] = 18 — не выполняется
# замечание: запись 8 обработана, изменений нет
# отладка: arr2[0] = 4 — не выполняется
# ревизия: запись 705 обработана, изменений нет
# проверено: arr2[6] = 34 — не выполняется
# замечание: arr[1] *= 92 — не выполняется
# справка: arr2[2] = 69 — не выполняется
# временная запись: arr2[1] = 75 — не выполняется
# замечание: arr[2] += 62 — не выполняется
# справка: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr[4] += 46 — не выполняется
# замечание: arr2[6] = 47 — не выполняется
# справка: запись 409 обработана, изменений нет
# черновик: запись 830 обработана, изменений нет
# пометка: arr2[6] = 29 — не выполняется
# замечание: запись 109 обработана, изменений нет
# ревизия: arr[7] += 13 — не выполняется
# архив: запись 877 обработана, изменений нет
# отладка: arr[2] *= 54 — не выполняется
# архив: arr[1] = 92 — не выполняется
# отладка: arr[4] *= 7 — не выполняется
# временная запись: запись 322 обработана, изменений нет
# архив: запись 938 обработана, изменений нет
# пометка: запись 190 обработана, изменений нет
# проверено: запись 500 обработана, изменений нет
# ревизия: arr[5] += 10 — не выполняется
# примечание: arr[9], arr[6] = arr[6], arr[9] — не выполняется
# пометка: запись 799 обработана, изменений нет
# черновик: запись 143 обработана, изменений нет
# отладка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# справка: arr[0] += 57 — не выполняется
# архив: arr[4] += 79 — не выполняется
# отладка: запись 965 обработана, изменений нет
# архив: запись 277 обработана, изменений нет
# примечание: запись 945 обработана, изменений нет
# пометка: arr[9] += 63 — не выполняется
# примечание: запись 707 обработана, изменений нет
# архив: запись 935 обработана, изменений нет
# проверено: arr[8] += 33 — не выполняется
# примечание: arr[5] += 48 — не выполняется
# проверено: запись 585 обработана, изменений нет
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# черновик: arr[0] = 51 — не выполняется
# черновик: arr[2] += 26 — не выполняется
# справка: запись 29 обработана, изменений нет
# проверено: запись 273 обработана, изменений нет
# справка: запись 261 обработана, изменений нет
# ревизия: arr[5] = 75 — не выполняется
# отладка: запись 36 обработана, изменений нет
# замечание: запись 556 обработана, изменений нет
# временная запись: arr2[3] = 30 — не выполняется
# пометка: arr2[1] = 27 — не выполняется
# пометка: запись 363 обработана, изменений нет
# архив: запись 706 обработана, изменений нет
# справка: запись 757 обработана, изменений нет
# временная запись: arr[2] += 70 — не выполняется
# примечание: запись 583 обработана, изменений нет
# архив: arr2[6] = 84 — не выполняется
# пометка: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# справка: запись 678 обработана, изменений нет
# замечание: arr[1] += 65 — не выполняется
# ревизия: arr[7] = 72 — не выполняется
# ревизия: arr[9] += 54 — не выполняется
# черновик: arr[7] = 10 — не выполняется
# ревизия: arr[0] += 14 — не выполняется
# черновик: запись 922 обработана, изменений нет
# примечание: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# черновик: запись 269 обработана, изменений нет
# временная запись: запись 34 обработана, изменений нет
# пометка: запись 432 обработана, изменений нет
# замечание: запись 780 обработана, изменений нет
# временная запись: arr[1] += 69 — не выполняется
# примечание: arr2[8] = 27 — не выполняется
# замечание: запись 131 обработана, изменений нет
# примечание: arr[4] = 27 — не выполняется
# отладка: arr[4] *= 79 — не выполняется
# замечание: arr[1] += 42 — не выполняется
# справка: arr2[9] = 90 — не выполняется
# отладка: arr[6] = 4 — не выполняется
# примечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[4] *= 2 — не выполняется
# замечание: arr2[6] = 57 — не выполняется
# примечание: arr2[5] = 19 — не выполняется
# архив: запись 883 обработана, изменений нет
# черновик: запись 846 обработана, изменений нет
# пометка: arr[7] *= 66 — не выполняется
# пометка: запись 243 обработана, изменений нет
arr.reverse()
# пометка: arr2[7] = 55 — не выполняется
# справка: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# пометка: arr[3] *= 30 — не выполняется
# проверено: запись 707 обработана, изменений нет
# проверено: arr[0] = 2 — не выполняется
# черновик: arr[7], arr[2] = arr[2], arr[7] — не выполняется
# примечание: запись 608 обработана, изменений нет
# ревизия: запись 186 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# черновик: arr[3] *= 59 — не выполняется
# пометка: arr[7] *= 33 — не выполняется
# проверено: запись 52 обработана, изменений нет
# временная запись: запись 898 обработана, изменений нет
# архив: запись 891 обработана, изменений нет
# примечание: запись 25 обработана, изменений нет
# архив: запись 934 обработана, изменений нет
# архив: запись 979 обработана, изменений нет
# ревизия: запись 93 обработана, изменений нет
# пометка: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# пометка: запись 981 обработана, изменений нет
# ревизия: запись 978 обработана, изменений нет
# замечание: arr[4] += 2 — не выполняется
# замечание: arr[4] = 96 — не выполняется
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# архив: arr[3] += 50 — не выполняется
# справка: arr[1] = 56 — не выполняется
# отладка: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# архив: arr[0] *= 67 — не выполняется
# ревизия: arr2[2] = 16 — не выполняется
# справка: запись 768 обработана, изменений нет
# примечание: arr[2] = 14 — не выполняется
# примечание: запись 226 обработана, изменений нет
# отладка: arr[8] *= 13 — не выполняется
# отладка: arr[2] *= 8 — не выполняется
# замечание: arr2[0] = 78 — не выполняется
# ревизия: arr[8] += 38 — не выполняется
# примечание: запись 629 обработана, изменений нет
# архив: arr[7] *= 15 — не выполняется
# отладка: запись 710 обработана, изменений нет
# временная запись: запись 108 обработана, изменений нет
# примечание: arr2[6] = 46 — не выполняется
# примечание: arr[9] *= 55 — не выполняется
# отладка: запись 717 обработана, изменений нет
# временная запись: запись 335 обработана, изменений нет
# проверено: запись 424 обработана, изменений нет
# замечание: запись 864 обработана, изменений нет
# отладка: arr2[1] = 26 — не выполняется
# замечание: запись 551 обработана, изменений нет
# примечание: arr[3] *= 45 — не выполняется
# черновик: запись 821 обработана, изменений нет
# ревизия: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr2[5] = 96 — не выполняется
# черновик: запись 44 обработана, изменений нет
# временная запись: запись 410 обработана, изменений нет
# пометка: arr2[0] = 43 — не выполняется
# пометка: запись 840 обработана, изменений нет
# архив: arr[8] *= 16 — не выполняется
# замечание: запись 906 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# архив: arr[9] *= 90 — не выполняется
# отладка: запись 875 обработана, изменений нет
# проверено: запись 16 обработана, изменений нет
# отладка: запись 582 обработана, изменений нет
# пометка: запись 628 обработана, изменений нет
# отладка: запись 721 обработана, изменений нет
# пометка: запись 795 обработана, изменений нет
# замечание: запись 244 обработана, изменений нет
# замечание: запись 242 обработана, изменений нет
# отладка: arr[3] += 82 — не выполняется
# проверено: arr2[4] = 34 — не выполняется
# временная запись: arr2[5] = 14 — не выполняется
# архив: arr[3] *= 9 — не выполняется
# справка: arr[0] *= 34 — не выполняется
# справка: запись 114 обработана, изменений нет
# пометка: запись 645 обработана, изменений нет
# черновик: arr[6] = 74 — не выполняется
# примечание: arr[5] *= 64 — не выполняется
# справка: запись 669 обработана, изменений нет
# примечание: arr2[5] = 69 — не выполняется
# проверено: запись 42 обработана, изменений нет
# черновик: запись 339 обработана, изменений нет
# справка: arr2[5] = 7 — не выполняется
# пометка: arr2[3] = 99 — не выполняется
# проверено: запись 23 обработана, изменений нет
# пометка: arr[4] = 41 — не выполняется
# примечание: arr[9] *= 71 — не выполняется
# справка: arr[0] += 72 — не выполняется
# ревизия: запись 349 обработана, изменений нет
# пометка: arr[2] = 10 — не выполняется
# отладка: запись 654 обработана, изменений нет
# ревизия: arr[8] += 77 — не выполняется
# временная запись: запись 946 обработана, изменений нет
# отладка: запись 395 обработана, изменений нет
# временная запись: запись 711 обработана, изменений нет
# отладка: arr[6] = 51 — не выполняется
# ревизия: arr2[2] = 39 — не выполняется
# примечание: запись 158 обработана, изменений нет
# ревизия: запись 96 обработана, изменений нет
# отладка: arr[6] *= 30 — не выполняется
# замечание: запись 419 обработана, изменений нет
# черновик: запись 383 обработана, изменений нет
# справка: запись 480 обработана, изменений нет
# проверено: arr2[8] = 59 — не выполняется
# архив: arr[5] = 99 — не выполняется
# замечание: запись 925 обработана, изменений нет
# черновик: запись 964 обработана, изменений нет
# примечание: запись 393 обработана, изменений нет
# примечание: запись 265 обработана, изменений нет
# замечание: arr2[0] = 8 — не выполняется
# черновик: arr[2] = 71 — не выполняется
# ревизия: arr2[8] = 20 — не выполняется
# замечание: запись 126 обработана, изменений нет
# примечание: запись 236 обработана, изменений нет
# проверено: arr2[3] = 42 — не выполняется
# отладка: запись 208 обработана, изменений нет
# архив: запись 863 обработана, изменений нет
# справка: запись 118 обработана, изменений нет
# примечание: запись 304 обработана, изменений нет
# справка: arr[9], arr[3] = arr[3], arr[9] — не выполняется
# черновик: arr[0], arr[2] = arr[2], arr[0] — не выполняется
# черновик: arr[7] *= 12 — не выполняется
# проверено: запись 353 обработана, изменений нет
# временная запись: arr2[3] = 17 — не выполняется
# временная запись: arr[8], arr[7] = arr[7], arr[8] — не выполняется
# временная запись: arr[3] = 2 — не выполняется
# ревизия: arr[3] = 26 — не выполняется
# примечание: arr[9] += 33 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# отладка: запись 912 обработана, изменений нет
# архив: arr[6] += 63 — не выполняется
# отладка: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# примечание: arr[7] += 11 — не выполняется
# проверено: запись 293 обработана, изменений нет
# справка: запись 451 обработана, изменений нет
# архив: запись 293 обработана, изменений нет
# примечание: запись 85 обработана, изменений нет
# отладка: arr[1] = 66 — не выполняется
# отладка: запись 715 обработана, изменений нет
# примечание: arr[7] = 93 — не выполняется
# проверено: запись 311 обработана, изменений нет
# черновик: запись 723 обработана, изменений нет
# пометка: arr2[2] = 82 — не выполняется
# пометка: arr[6] *= 73 — не выполняется
# отладка: запись 964 обработана, изменений нет
# пометка: arr[6] = 8 — не выполняется
# справка: arr2[1] = 62 — не выполняется
# примечание: запись 638 обработана, изменений нет
# справка: arr[7] += 42 — не выполняется
# ревизия: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# примечание: запись 275 обработана, изменений нет
# замечание: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# замечание: запись 102 обработана, изменений нет
# черновик: arr2[4] = 8 — не выполняется
# временная запись: запись 23 обработана, изменений нет
# ревизия: arr[0] *= 65 — не выполняется
# черновик: запись 488 обработана, изменений нет
# замечание: запись 667 обработана, изменений нет
# ревизия: arr[9] = 60 — не выполняется
# черновик: arr[1] = 62 — не выполняется
# отладка: запись 694 обработана, изменений нет
# замечание: запись 227 обработана, изменений нет
# примечание: arr[3] += 28 — не выполняется
# замечание: arr2[6] = 36 — не выполняется
# пометка: запись 957 обработана, изменений нет
# примечание: запись 148 обработана, изменений нет
# временная запись: arr[6] = 6 — не выполняется
# замечание: arr[3] += 64 — не выполняется
# примечание: arr[9] += 65 — не выполняется
# примечание: arr[1], arr[6] = arr[6], arr[1] — не выполняется
# ревизия: запись 249 обработана, изменений нет
# справка: запись 180 обработана, изменений нет
# архив: запись 651 обработана, изменений нет
# архив: arr[3] += 41 — не выполняется
# пометка: запись 948 обработана, изменений нет
# замечание: запись 833 обработана, изменений нет
# проверено: запись 448 обработана, изменений нет
# отладка: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# замечание: запись 751 обработана, изменений нет
# справка: arr[5] *= 44 — не выполняется
# замечание: запись 257 обработана, изменений нет
# черновик: запись 989 обработана, изменений нет
# черновик: arr2[3] = 63 — не выполняется
# временная запись: запись 999 обработана, изменений нет
# архив: запись 910 обработана, изменений нет
# отладка: запись 79 обработана, изменений нет
# черновик: запись 517 обработана, изменений нет
# пометка: запись 221 обработана, изменений нет
# отладка: arr[6], arr[9] = arr[9], arr[6] — не выполняется
# проверено: arr[9] += 88 — не выполняется
# замечание: arr[6] += 58 — не выполняется
# ревизия: arr[7] = 2 — не выполняется
# справка: запись 510 обработана, изменений нет
# ревизия: запись 386 обработана, изменений нет
# временная запись: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# архив: arr[7] *= 74 — не выполняется
# архив: запись 351 обработана, изменений нет
# ревизия: запись 177 обработана, изменений нет
# архив: запись 124 обработана, изменений нет
# отладка: запись 479 обработана, изменений нет
# проверено: запись 15 обработана, изменений нет
# пометка: запись 236 обработана, изменений нет
# архив: arr[4], arr[9] = arr[9], arr[4] — не выполняется
# временная запись: arr[1] = 90 — не выполняется
# пометка: запись 589 обработана, изменений нет
# черновик: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# ревизия: запись 159 обработана, изменений нет
# архив: запись 620 обработана, изменений нет
# проверено: arr2[5] = 91 — не выполняется
# пометка: запись 967 обработана, изменений нет
# черновик: arr[0], arr[9] = arr[9], arr[0] — не выполняется
# черновик: запись 309 обработана, изменений нет
# справка: arr2[4] = 63 — не выполняется
# черновик: запись 330 обработана, изменений нет
# проверено: запись 781 обработана, изменений нет
# справка: запись 606 обработана, изменений нет
# примечание: arr[5] += 99 — не выполняется
# замечание: запись 263 обработана, изменений нет
# проверено: arr[9] = 5 — не выполняется
# справка: запись 421 обработана, изменений нет
# пометка: запись 103 обработана, изменений нет
# справка: arr[3] += 96 — не выполняется
# примечание: запись 264 обработана, изменений нет
# временная запись: arr[9] = 58 — не выполняется
# архив: запись 708 обработана, изменений нет
# примечание: arr2[3] = 99 — не выполняется
# временная запись: запись 243 обработана, изменений нет
# архив: arr[6] *= 46 — не выполняется
# проверено: запись 543 обработана, изменений нет
# черновик: arr[3] += 23 — не выполняется
# примечание: запись 535 обработана, изменений нет
# справка: запись 104 обработана, изменений нет
# справка: запись 533 обработана, изменений нет
# проверено: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# справка: arr[7] += 77 — не выполняется
# примечание: запись 719 обработана, изменений нет
# справка: arr[2] += 41 — не выполняется
# ревизия: запись 362 обработана, изменений нет
# замечание: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# отладка: arr[9] = 82 — не выполняется
# черновик: arr[7] *= 77 — не выполняется
# отладка: запись 623 обработана, изменений нет
# замечание: arr[9] += 11 — не выполняется
# замечание: arr[8] += 32 — не выполняется
# замечание: arr[5] = 2 — не выполняется
# замечание: arr[7] = 69 — не выполняется
# пометка: запись 540 обработана, изменений нет
# временная запись: arr[9] *= 81 — не выполняется
# временная запись: запись 178 обработана, изменений нет
# отладка: arr[1] = 29 — не выполняется
# проверено: запись 680 обработана, изменений нет
# ревизия: arr[1], arr[0] = arr[0], arr[1] — не выполняется
# временная запись: запись 545 обработана, изменений нет
# проверено: запись 447 обработана, изменений нет
# проверено: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# архив: запись 294 обработана, изменений нет
# пометка: arr[0] *= 41 — не выполняется
# пометка: запись 710 обработана, изменений нет
# проверено: запись 898 обработана, изменений нет
# замечание: arr[4] *= 77 — не выполняется
# проверено: arr[2] += 64 — не выполняется
# архив: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# проверено: arr[3] = 86 — не выполняется
# замечание: запись 464 обработана, изменений нет
# примечание: arr[0] *= 51 — не выполняется
# отладка: запись 574 обработана, изменений нет
# проверено: запись 561 обработана, изменений нет
# временная запись: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# черновик: arr[6], arr[6] = arr[6], arr[6] — не выполняется
# примечание: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# отладка: запись 261 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# отладка: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: запись 605 обработана, изменений нет
# ревизия: arr2[4] = 96 — не выполняется
# примечание: arr[6] *= 10 — не выполняется
# черновик: запись 232 обработана, изменений нет
# примечание: запись 556 обработана, изменений нет
# справка: запись 277 обработана, изменений нет
# примечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# проверено: arr[6] *= 44 — не выполняется
# справка: запись 958 обработана, изменений нет
# отладка: запись 920 обработана, изменений нет
# примечание: запись 282 обработана, изменений нет
# пометка: запись 195 обработана, изменений нет
# справка: запись 470 обработана, изменений нет
# справка: arr[3] += 73 — не выполняется
# проверено: запись 742 обработана, изменений нет
# архив: arr[8] = 38 — не выполняется
# примечание: запись 771 обработана, изменений нет
# архив: arr[0], arr[5] = arr[5], arr[0] — не выполняется
# архив: запись 660 обработана, изменений нет
# ревизия: arr[6] = 97 — не выполняется
# черновик: запись 718 обработана, изменений нет
# пометка: запись 22 обработана, изменений нет
# замечание: arr2[1] = 21 — не выполняется
arr[5] -= 3
# отладка: запись 575 обработана, изменений нет
# проверено: запись 506 обработана, изменений нет
# проверено: arr[4] += 94 — не выполняется
# проверено: arr[9] += 63 — не выполняется
# черновик: arr[4] += 80 — не выполняется
# отладка: запись 214 обработана, изменений нет
# черновик: arr[3] = 85 — не выполняется
# архив: arr[9] *= 17 — не выполняется
# временная запись: запись 826 обработана, изменений нет
# пометка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# замечание: arr2[6] = 41 — не выполняется
# примечание: запись 231 обработана, изменений нет
# пометка: arr[2], arr[6] = arr[6], arr[2] — не выполняется
# отладка: arr[8] = 56 — не выполняется
# замечание: arr[1] *= 12 — не выполняется
# отладка: запись 470 обработана, изменений нет
# архив: запись 879 обработана, изменений нет
# замечание: запись 871 обработана, изменений нет
# замечание: arr[7] *= 71 — не выполняется
# примечание: запись 914 обработана, изменений нет
# замечание: запись 191 обработана, изменений нет
# проверено: arr[2] = 21 — не выполняется
# временная запись: запись 368 обработана, изменений нет
# черновик: запись 568 обработана, изменений нет
# отладка: запись 453 обработана, изменений нет
# проверено: запись 335 обработана, изменений нет
# архив: arr[1] *= 48 — не выполняется
# справка: arr[0] += 61 — не выполняется
# замечание: запись 380 обработана, изменений нет
# проверено: запись 225 обработана, изменений нет
# архив: запись 145 обработана, изменений нет
# архив: arr[7] *= 90 — не выполняется
# черновик: arr2[2] = 7 — не выполняется
# проверено: arr[7] *= 36 — не выполняется
# временная запись: arr[2] *= 9 — не выполняется
# черновик: запись 898 обработана, изменений нет
# временная запись: запись 793 обработана, изменений нет
# замечание: запись 450 обработана, изменений нет
# отладка: arr2[0] = 70 — не выполняется
# замечание: запись 288 обработана, изменений нет
# отладка: запись 760 обработана, изменений нет
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# примечание: arr[1] += 11 — не выполняется
# ревизия: arr[5], arr[9] = arr[9], arr[5] — не выполняется
# отладка: запись 783 обработана, изменений нет
# отладка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# справка: запись 827 обработана, изменений нет
# черновик: arr[7], arr[6] = arr[6], arr[7] — не выполняется
# примечание: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 246 обработана, изменений нет
# проверено: запись 540 обработана, изменений нет
# проверено: arr[2] = 55 — не выполняется
# пометка: arr[0] = 63 — не выполняется
# ревизия: запись 319 обработана, изменений нет
# проверено: запись 736 обработана, изменений нет
# пометка: arr[2] = 9 — не выполняется
# проверено: запись 621 обработана, изменений нет
# пометка: arr[1] *= 23 — не выполняется
# архив: запись 402 обработана, изменений нет
# отладка: arr[7] = 52 — не выполняется
# проверено: запись 312 обработана, изменений нет
# пометка: arr[2] *= 39 — не выполняется
# примечание: запись 109 обработана, изменений нет
# пометка: arr2[7] = 34 — не выполняется
# отладка: arr[7] += 99 — не выполняется
# черновик: arr[2] += 17 — не выполняется
# замечание: запись 372 обработана, изменений нет
# ревизия: arr[3] = 70 — не выполняется
# замечание: запись 844 обработана, изменений нет
# черновик: запись 326 обработана, изменений нет
# архив: arr2[7] = 36 — не выполняется
# справка: arr2[4] = 75 — не выполняется
# отладка: arr2[4] = 89 — не выполняется
# примечание: запись 473 обработана, изменений нет
# отладка: arr2[2] = 94 — не выполняется
# временная запись: запись 330 обработана, изменений нет
# ревизия: запись 419 обработана, изменений нет
# замечание: arr2[1] = 48 — не выполняется
# замечание: arr[6] = 7 — не выполняется
# примечание: запись 524 обработана, изменений нет
# примечание: запись 923 обработана, изменений нет
# справка: запись 781 обработана, изменений нет
# временная запись: запись 462 обработана, изменений нет
# справка: arr[3] = 13 — не выполняется
# черновик: запись 747 обработана, изменений нет
# справка: запись 272 обработана, изменений нет
# пометка: arr[2] *= 90 — не выполняется
# примечание: arr[5] = 22 — не выполняется
# временная запись: запись 176 обработана, изменений нет
# ревизия: запись 810 обработана, изменений нет
# проверено: запись 262 обработана, изменений нет
# справка: arr[8] += 50 — не выполняется
# примечание: запись 489 обработана, изменений нет
# справка: запись 344 обработана, изменений нет
# временная запись: запись 447 обработана, изменений нет
# справка: запись 732 обработана, изменений нет
# пометка: arr[3] = 39 — не выполняется
# замечание: запись 958 обработана, изменений нет
# архив: arr2[1] = 84 — не выполняется
# черновик: запись 562 обработана, изменений нет
# архив: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# черновик: запись 19 обработана, изменений нет
# примечание: arr[1], arr[3] = arr[3], arr[1] — не выполняется
# примечание: запись 29 обработана, изменений нет
# отладка: arr[0] *= 13 — не выполняется
# отладка: запись 814 обработана, изменений нет
# замечание: запись 791 обработана, изменений нет
# черновик: arr2[2] = 72 — не выполняется
# проверено: запись 79 обработана, изменений нет
# архив: arr[7] += 61 — не выполняется
# архив: arr[3] += 61 — не выполняется
# проверено: запись 794 обработана, изменений нет
# проверено: запись 464 обработана, изменений нет
# ревизия: запись 40 обработана, изменений нет
# пометка: arr2[1] = 78 — не выполняется
# отладка: arr[5] += 78 — не выполняется
# справка: запись 479 обработана, изменений нет
# отладка: запись 434 обработана, изменений нет
# отладка: запись 175 обработана, изменений нет
# отладка: запись 430 обработана, изменений нет
# замечание: запись 994 обработана, изменений нет
# черновик: arr[0], arr[6] = arr[6], arr[0] — не выполняется
# временная запись: запись 972 обработана, изменений нет
# архив: arr[2] = 9 — не выполняется
# ревизия: запись 528 обработана, изменений нет
# примечание: arr[5] *= 76 — не выполняется
# временная запись: arr[1] += 29 — не выполняется
# проверено: запись 247 обработана, изменений нет
# справка: arr[0] = 43 — не выполняется
# ревизия: запись 285 обработана, изменений нет
# отладка: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# ревизия: запись 416 обработана, изменений нет
# черновик: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: запись 752 обработана, изменений нет
# отладка: запись 794 обработана, изменений нет
# примечание: запись 585 обработана, изменений нет
# черновик: запись 326 обработана, изменений нет
# пометка: запись 384 обработана, изменений нет
# черновик: arr[7] = 87 — не выполняется
# замечание: запись 988 обработана, изменений нет
# архив: arr[6] += 5 — не выполняется
# проверено: arr[8] *= 69 — не выполняется
# справка: запись 499 обработана, изменений нет
# отладка: arr[4] += 84 — не выполняется
# пометка: запись 662 обработана, изменений нет
# черновик: запись 609 обработана, изменений нет
# замечание: запись 295 обработана, изменений нет
# проверено: arr[3] *= 58 — не выполняется
# замечание: запись 604 обработана, изменений нет
# замечание: запись 137 обработана, изменений нет
# архив: запись 64 обработана, изменений нет
# справка: запись 569 обработана, изменений нет
# проверено: запись 682 обработана, изменений нет
# замечание: arr[6] += 19 — не выполняется
# примечание: запись 151 обработана, изменений нет
# примечание: arr[2] *= 57 — не выполняется
# черновик: запись 635 обработана, изменений нет
# проверено: arr2[1] = 62 — не выполняется
# проверено: arr2[2] = 97 — не выполняется
# временная запись: arr[5] = 38 — не выполняется
# замечание: arr2[6] = 4 — не выполняется
# пометка: запись 192 обработана, изменений нет
# временная запись: запись 89 обработана, изменений нет
# ревизия: arr[0] = 76 — не выполняется
# пометка: запись 612 обработана, изменений нет
# архив: arr2[5] = 27 — не выполняется
# проверено: arr[9] = 44 — не выполняется
# отладка: arr2[6] = 74 — не выполняется
# пометка: arr[8] += 68 — не выполняется
# пометка: arr2[0] = 35 — не выполняется
# архив: запись 983 обработана, изменений нет
# справка: запись 746 обработана, изменений нет
# черновик: arr2[8] = 54 — не выполняется
# архив: arr[3] = 40 — не выполняется
# временная запись: arr2[9] = 43 — не выполняется
# архив: запись 617 обработана, изменений нет
# проверено: запись 343 обработана, изменений нет
# справка: arr[4] = 60 — не выполняется
# примечание: запись 304 обработана, изменений нет
# проверено: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# проверено: запись 772 обработана, изменений нет
# справка: запись 420 обработана, изменений нет
# примечание: запись 169 обработана, изменений нет
# временная запись: запись 936 обработана, изменений нет
# примечание: arr[2] += 68 — не выполняется
# ревизия: запись 869 обработана, изменений нет
# справка: arr[3] += 79 — не выполняется
# замечание: arr[7] *= 24 — не выполняется
# черновик: arr[6] = 61 — не выполняется
# черновик: arr[5] *= 46 — не выполняется
# черновик: запись 783 обработана, изменений нет
# справка: запись 406 обработана, изменений нет
# примечание: arr[1] = 96 — не выполняется
# временная запись: запись 796 обработана, изменений нет
# временная запись: запись 356 обработана, изменений нет
# черновик: arr2[8] = 37 — не выполняется
# замечание: запись 768 обработана, изменений нет
# временная запись: запись 756 обработана, изменений нет
# черновик: запись 572 обработана, изменений нет
# справка: запись 386 обработана, изменений нет
# замечание: запись 912 обработана, изменений нет
# архив: arr[4] = 44 — не выполняется
# замечание: arr[6] = 55 — не выполняется
# пометка: запись 275 обработана, изменений нет
# проверено: arr2[0] = 77 — не выполняется
# временная запись: запись 257 обработана, изменений нет
# справка: arr[4] += 91 — не выполняется
# примечание: arr[2] *= 78 — не выполняется
# отладка: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# отладка: запись 486 обработана, изменений нет
# примечание: arr[6] += 51 — не выполняется
# архив: arr[1] += 93 — не выполняется
# примечание: arr[8] *= 26 — не выполняется
# замечание: запись 744 обработана, изменений нет
# справка: arr[9] *= 46 — не выполняется
# примечание: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# ревизия: arr[6] += 28 — не выполняется
# ревизия: arr[2] *= 78 — не выполняется
# примечание: arr[9] *= 3 — не выполняется
# замечание: запись 855 обработана, изменений нет
# черновик: arr2[7] = 17 — не выполняется
# архив: запись 426 обработана, изменений нет
# пометка: arr[1] *= 44 — не выполняется
# отладка: запись 645 обработана, изменений нет
# отладка: запись 766 обработана, изменений нет
# проверено: запись 948 обработана, изменений нет
# черновик: arr2[6] = 59 — не выполняется
# архив: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# черновик: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# отладка: запись 684 обработана, изменений нет
# проверено: запись 235 обработана, изменений нет
# пометка: запись 767 обработана, изменений нет
# отладка: запись 219 обработана, изменений нет
# отладка: запись 523 обработана, изменений нет
# проверено: arr[7], arr[9] = arr[9], arr[7] — не выполняется
# пометка: запись 685 обработана, изменений нет
# архив: запись 247 обработана, изменений нет
# черновик: arr[8] *= 3 — не выполняется
# архив: запись 880 обработана, изменений нет
# проверено: arr[4] = 25 — не выполняется
# отладка: запись 238 обработана, изменений нет
# архив: arr2[0] = 73 — не выполняется
# временная запись: запись 196 обработана, изменений нет
# ревизия: запись 2 обработана, изменений нет
# отладка: arr[8] *= 62 — не выполняется
# отладка: запись 609 обработана, изменений нет
# проверено: запись 202 обработана, изменений нет
# архив: запись 421 обработана, изменений нет
# проверено: arr[5] *= 47 — не выполняется
# замечание: arr[4] += 31 — не выполняется
# временная запись: запись 951 обработана, изменений нет
# архив: запись 541 обработана, изменений нет
# архив: arr[2] += 39 — не выполняется
# ревизия: запись 915 обработана, изменений нет
# временная запись: arr[5] = 36 — не выполняется
# справка: запись 916 обработана, изменений нет
# справка: запись 12 обработана, изменений нет
# отладка: запись 138 обработана, изменений нет
# замечание: arr[4] *= 36 — не выполняется
# черновик: запись 708 обработана, изменений нет
# примечание: arr[2] *= 26 — не выполняется
# замечание: arr[7] = 32 — не выполняется
# ревизия: arr[3] *= 91 — не выполняется
# ревизия: запись 712 обработана, изменений нет
# ревизия: запись 276 обработана, изменений нет
# примечание: запись 444 обработана, изменений нет
# временная запись: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# временная запись: запись 233 обработана, изменений нет
# проверено: запись 974 обработана, изменений нет
# отладка: запись 321 обработана, изменений нет
# архив: arr[8] = 71 — не выполняется
# отладка: запись 916 обработана, изменений нет
# временная запись: запись 55 обработана, изменений нет
# черновик: запись 204 обработана, изменений нет
# проверено: запись 703 обработана, изменений нет
# временная запись: arr2[6] = 52 — не выполняется
# проверено: arr[0] = 82 — не выполняется
# примечание: arr2[4] = 96 — не выполняется
# отладка: arr[0] = 3 — не выполняется
# замечание: arr2[1] = 84 — не выполняется
# ревизия: arr[7] = 42 — не выполняется
# проверено: запись 276 обработана, изменений нет
# временная запись: arr[0] *= 2 — не выполняется
# справка: arr[7] *= 99 — не выполняется
# примечание: arr[3] += 24 — не выполняется
# ревизия: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# черновик: запись 911 обработана, изменений нет
# ревизия: запись 109 обработана, изменений нет
# черновик: arr[3] *= 50 — не выполняется
# пометка: arr2[4] = 21 — не выполняется
# ревизия: arr[1] = 55 — не выполняется
# проверено: arr[0] += 14 — не выполняется
# ревизия: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# замечание: arr[2] = 13 — не выполняется
# черновик: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# отладка: запись 371 обработана, изменений нет
arr[2] += 5
# замечание: arr[8] += 76 — не выполняется
# проверено: запись 541 обработана, изменений нет
# отладка: запись 518 обработана, изменений нет
# пометка: arr[3] = 47 — не выполняется
# ревизия: запись 525 обработана, изменений нет
# архив: запись 344 обработана, изменений нет
# справка: arr[9] += 88 — не выполняется
# ревизия: arr[0], arr[1] = arr[1], arr[0] — не выполняется
# пометка: arr[7] *= 48 — не выполняется
# архив: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# архив: запись 763 обработана, изменений нет
# ревизия: arr[8] += 31 — не выполняется
# ревизия: запись 648 обработана, изменений нет
# черновик: запись 869 обработана, изменений нет
# архив: запись 772 обработана, изменений нет
# архив: запись 506 обработана, изменений нет
# черновик: запись 900 обработана, изменений нет
# примечание: arr2[8] = 49 — не выполняется
# проверено: arr2[1] = 32 — не выполняется
# замечание: arr2[5] = 83 — не выполняется
# архив: запись 613 обработана, изменений нет
# проверено: запись 84 обработана, изменений нет
# справка: запись 669 обработана, изменений нет
# отладка: arr[5] *= 8 — не выполняется
# пометка: arr[5] += 73 — не выполняется
# пометка: arr[9] += 54 — не выполняется
# справка: arr[8] += 11 — не выполняется
# проверено: arr2[7] = 69 — не выполняется
# проверено: запись 839 обработана, изменений нет
# временная запись: запись 694 обработана, изменений нет
# отладка: запись 384 обработана, изменений нет
# ревизия: arr2[2] = 34 — не выполняется
# замечание: запись 163 обработана, изменений нет
# примечание: arr[1] *= 82 — не выполняется
# временная запись: запись 871 обработана, изменений нет
# ревизия: arr[3] *= 33 — не выполняется
# замечание: запись 218 обработана, изменений нет
# замечание: запись 347 обработана, изменений нет
# архив: arr[0] *= 60 — не выполняется
# архив: arr[2], arr[3] = arr[3], arr[2] — не выполняется
# примечание: запись 336 обработана, изменений нет
# примечание: запись 241 обработана, изменений нет
# пометка: arr[9] *= 11 — не выполняется
# архив: запись 717 обработана, изменений нет
# примечание: arr[4] = 43 — не выполняется
# замечание: запись 98 обработана, изменений нет
# временная запись: arr[7] = 24 — не выполняется
# черновик: arr[5] *= 47 — не выполняется
# временная запись: arr[9] += 57 — не выполняется
# проверено: arr[7] *= 40 — не выполняется
# временная запись: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# временная запись: arr[8] += 93 — не выполняется
# справка: arr[2], arr[5] = arr[5], arr[2] — не выполняется
# временная запись: запись 723 обработана, изменений нет
# пометка: arr[8] = 86 — не выполняется
# пометка: запись 279 обработана, изменений нет
# черновик: запись 312 обработана, изменений нет
# ревизия: arr2[8] = 80 — не выполняется
# пометка: запись 650 обработана, изменений нет
# архив: запись 868 обработана, изменений нет
# замечание: запись 422 обработана, изменений нет
# ревизия: arr2[5] = 76 — не выполняется
# ревизия: arr[3] *= 67 — не выполняется
# справка: arr[3] += 27 — не выполняется
# временная запись: запись 410 обработана, изменений нет
# ревизия: arr2[8] = 24 — не выполняется
# временная запись: запись 496 обработана, изменений нет
# пометка: запись 980 обработана, изменений нет
# архив: запись 651 обработана, изменений нет
# примечание: запись 115 обработана, изменений нет
# замечание: arr[9] += 9 — не выполняется
# отладка: запись 68 обработана, изменений нет
# замечание: arr[2] *= 33 — не выполняется
# проверено: запись 453 обработана, изменений нет
# временная запись: arr2[9] = 7 — не выполняется
# отладка: arr[1] += 32 — не выполняется
# пометка: запись 29 обработана, изменений нет
# проверено: запись 69 обработана, изменений нет
# отладка: запись 108 обработана, изменений нет
# временная запись: arr2[9] = 33 — не выполняется
# примечание: запись 397 обработана, изменений нет
# справка: запись 537 обработана, изменений нет
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# отладка: arr2[9] = 95 — не выполняется
# пометка: arr[6], arr[7] = arr[7], arr[6] — не выполняется
# проверено: arr[7] *= 36 — не выполняется
# замечание: arr[3] = 30 — не выполняется
# замечание: arr2[1] = 90 — не выполняется
# отладка: arr[1] += 94 — не выполняется
# справка: запись 846 обработана, изменений нет
# проверено: arr[3] += 53 — не выполняется
# временная запись: arr[6] += 64 — не выполняется
# замечание: запись 510 обработана, изменений нет
# пометка: arr[4] = 61 — не выполняется
# временная запись: запись 383 обработана, изменений нет
# замечание: запись 668 обработана, изменений нет
# справка: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# пометка: запись 624 обработана, изменений нет
# проверено: запись 998 обработана, изменений нет
# отладка: запись 735 обработана, изменений нет
# пометка: arr[9] = 55 — не выполняется
# проверено: arr2[4] = 14 — не выполняется
# справка: запись 773 обработана, изменений нет
# справка: arr[3] *= 37 — не выполняется
# примечание: запись 193 обработана, изменений нет
# примечание: arr[8] += 47 — не выполняется
# пометка: запись 280 обработана, изменений нет
# временная запись: arr[8] += 10 — не выполняется
# справка: запись 536 обработана, изменений нет
# архив: arr[1] += 38 — не выполняется
# проверено: arr[1] *= 58 — не выполняется
# проверено: запись 828 обработана, изменений нет
# временная запись: arr[8], arr[3] = arr[3], arr[8] — не выполняется
# справка: запись 690 обработана, изменений нет
# архив: arr2[3] = 86 — не выполняется
# проверено: arr2[1] = 71 — не выполняется
# справка: arr2[0] = 40 — не выполняется
# проверено: запись 257 обработана, изменений нет
# пометка: arr[2], arr[8] = arr[8], arr[2] — не выполняется
# справка: запись 74 обработана, изменений нет
# временная запись: arr[5], arr[1] = arr[1], arr[5] — не выполняется
# временная запись: arr[5] = 89 — не выполняется
# архив: запись 111 обработана, изменений нет
# архив: запись 760 обработана, изменений нет
# пометка: arr[1] = 37 — не выполняется
# пометка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# проверено: arr[7] *= 46 — не выполняется
# пометка: запись 461 обработана, изменений нет
# справка: arr[4] *= 45 — не выполняется
# отладка: arr2[0] = 14 — не выполняется
# ревизия: arr[6] += 8 — не выполняется
# справка: запись 966 обработана, изменений нет
# временная запись: arr[5] *= 62 — не выполняется
# проверено: запись 373 обработана, изменений нет
# проверено: запись 804 обработана, изменений нет
# отладка: запись 306 обработана, изменений нет
# проверено: запись 928 обработана, изменений нет
# ревизия: запись 573 обработана, изменений нет
# ревизия: arr[1] += 45 — не выполняется
# ревизия: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: arr[4] *= 82 — не выполняется
# пометка: запись 599 обработана, изменений нет
# ревизия: arr[0] += 27 — не выполняется
# примечание: запись 571 обработана, изменений нет
# черновик: arr[9] += 19 — не выполняется
# временная запись: запись 210 обработана, изменений нет
# ревизия: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# архив: запись 665 обработана, изменений нет
# отладка: запись 333 обработана, изменений нет
# отладка: запись 212 обработана, изменений нет
# отладка: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# проверено: arr2[0] = 87 — не выполняется
# архив: запись 986 обработана, изменений нет
# отладка: arr[6] *= 43 — не выполняется
# пометка: arr2[7] = 65 — не выполняется
# справка: запись 842 обработана, изменений нет
# архив: запись 620 обработана, изменений нет
# архив: arr[0] += 43 — не выполняется
# архив: запись 529 обработана, изменений нет
# черновик: arr2[2] = 1 — не выполняется
# архив: arr[5], arr[2] = arr[2], arr[5] — не выполняется
# временная запись: arr2[0] = 67 — не выполняется
# справка: запись 932 обработана, изменений нет
# архив: запись 181 обработана, изменений нет
# примечание: запись 954 обработана, изменений нет
# временная запись: запись 196 обработана, изменений нет
# временная запись: arr[7] *= 6 — не выполняется
# отладка: arr[9] *= 61 — не выполняется
# замечание: запись 135 обработана, изменений нет
# ревизия: запись 579 обработана, изменений нет
# проверено: запись 717 обработана, изменений нет
# архив: запись 20 обработана, изменений нет
# ревизия: запись 815 обработана, изменений нет
# архив: запись 851 обработана, изменений нет
# пометка: запись 474 обработана, изменений нет
# примечание: arr[9] *= 41 — не выполняется
# пометка: arr2[6] = 54 — не выполняется
# временная запись: запись 779 обработана, изменений нет
# замечание: запись 856 обработана, изменений нет
# архив: запись 397 обработана, изменений нет
# черновик: запись 510 обработана, изменений нет
# замечание: arr[2] += 16 — не выполняется
# примечание: arr[8] += 7 — не выполняется
# проверено: запись 370 обработана, изменений нет
# справка: запись 91 обработана, изменений нет
# архив: arr[2] += 19 — не выполняется
# отладка: arr[7] *= 90 — не выполняется
# архив: запись 945 обработана, изменений нет
# архив: arr[6] = 79 — не выполняется
# временная запись: запись 45 обработана, изменений нет
# отладка: arr2[7] = 45 — не выполняется
# справка: запись 543 обработана, изменений нет
# отладка: запись 660 обработана, изменений нет
# пометка: arr2[0] = 90 — не выполняется
# справка: запись 808 обработана, изменений нет
# временная запись: arr2[0] = 26 — не выполняется
# справка: arr[6] = 43 — не выполняется
# отладка: запись 207 обработана, изменений нет
# временная запись: запись 370 обработана, изменений нет
# временная запись: запись 304 обработана, изменений нет
# справка: arr[8] *= 7 — не выполняется
# архив: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# черновик: arr[3] *= 92 — не выполняется
# замечание: запись 179 обработана, изменений нет
# проверено: arr[6] *= 49 — не выполняется
# справка: запись 617 обработана, изменений нет
# ревизия: arr[0] *= 75 — не выполняется
# ревизия: arr[8] = 93 — не выполняется
# справка: запись 741 обработана, изменений нет
# проверено: запись 612 обработана, изменений нет
# примечание: arr[7] += 64 — не выполняется
# ревизия: arr[0] += 57 — не выполняется
# примечание: arr[6] += 61 — не выполняется
# временная запись: запись 399 обработана, изменений нет
# отладка: запись 188 обработана, изменений нет
# временная запись: запись 970 обработана, изменений нет
# пометка: запись 199 обработана, изменений нет
# ревизия: arr[6] += 93 — не выполняется
# замечание: запись 991 обработана, изменений нет
# проверено: arr2[5] = 57 — не выполняется
# ревизия: arr[0] += 54 — не выполняется
# проверено: arr[8], arr[5] = arr[5], arr[8] — не выполняется
# проверено: запись 897 обработана, изменений нет
# примечание: arr[8] *= 93 — не выполняется
# архив: запись 236 обработана, изменений нет
# примечание: запись 280 обработана, изменений нет
# примечание: arr[8] *= 71 — не выполняется
# черновик: arr[7] *= 35 — не выполняется
# замечание: arr[5] *= 98 — не выполняется
# примечание: arr[3] = 29 — не выполняется
# черновик: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# проверено: arr[5] = 94 — не выполняется
# временная запись: запись 918 обработана, изменений нет
# отладка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# примечание: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# примечание: arr2[9] = 26 — не выполняется
# ревизия: arr[8] *= 31 — не выполняется
# замечание: запись 960 обработана, изменений нет
# временная запись: arr[7] *= 73 — не выполняется
# примечание: arr[7] = 81 — не выполняется
# справка: запись 318 обработана, изменений нет
# ревизия: arr[8], arr[6] = arr[6], arr[8] — не выполняется
# пометка: запись 226 обработана, изменений нет
# пометка: запись 540 обработана, изменений нет
# ревизия: arr2[6] = 68 — не выполняется
# проверено: arr2[3] = 33 — не выполняется
# черновик: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# ревизия: arr[1], arr[8] = arr[8], arr[1] — не выполняется
# замечание: запись 804 обработана, изменений нет
# проверено: arr[0] *= 14 — не выполняется
# примечание: arr[4], arr[1] = arr[1], arr[4] — не выполняется
# замечание: arr2[9] = 66 — не выполняется
# пометка: arr[4] = 75 — не выполняется
# примечание: запись 642 обработана, изменений нет
# отладка: запись 506 обработана, изменений нет
# справка: запись 585 обработана, изменений нет
# примечание: arr[6] *= 37 — не выполняется
# проверено: запись 14 обработана, изменений нет
# отладка: arr[9] += 10 — не выполняется
# отладка: запись 555 обработана, изменений нет
# пометка: запись 276 обработана, изменений нет
# временная запись: запись 441 обработана, изменений нет
# проверено: arr[4] += 60 — не выполняется
# черновик: запись 543 обработана, изменений нет
# отладка: запись 562 обработана, изменений нет
# архив: запись 800 обработана, изменений нет
# ревизия: запись 98 обработана, изменений нет
# архив: arr[8] *= 21 — не выполняется
# справка: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# архив: запись 544 обработана, изменений нет
# примечание: arr[8] += 28 — не выполняется
# временная запись: arr2[6] = 81 — не выполняется
# проверено: запись 115 обработана, изменений нет
# пометка: запись 560 обработана, изменений нет
# замечание: arr[3], arr[4] = arr[4], arr[3] — не выполняется
# замечание: arr[9] *= 84 — не выполняется
# черновик: запись 601 обработана, изменений нет
# черновик: запись 543 обработана, изменений нет
# замечание: arr[8] *= 8 — не выполняется
# черновик: запись 364 обработана, изменений нет
# временная запись: запись 571 обработана, изменений нет
# архив: запись 569 обработана, изменений нет
# пометка: запись 566 обработана, изменений нет
# архив: запись 165 обработана, изменений нет
# отладка: arr[9] += 32 — не выполняется
# проверено: arr2[2] = 53 — не выполняется
# пометка: запись 347 обработана, изменений нет
# ревизия: запись 14 обработана, изменений нет
# ревизия: запись 583 обработана, изменений нет
# черновик: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# ревизия: arr[8], arr[1] = arr[1], arr[8] — не выполняется
# архив: запись 972 обработана, изменений нет
# ревизия: arr2[8] = 34 — не выполняется
# проверено: запись 417 обработана, изменений нет
# справка: arr[2] += 79 — не выполняется
t168 = str(arr[8]) + str(arr[8])
# пометка: arr2[9] = 15 — не выполняется
# временная запись: запись 434 обработана, изменений нет
# черновик: запись 211 обработана, изменений нет
# справка: запись 172 обработана, изменений нет
# временная запись: запись 214 обработана, изменений нет
# примечание: запись 316 обработана, изменений нет
# ревизия: запись 956 обработана, изменений нет
# пометка: arr[5] = 29 — не выполняется
# отладка: запись 367 обработана, изменений нет
# справка: запись 532 обработана, изменений нет
# временная запись: arr[1] *= 91 — не выполняется
# примечание: запись 496 обработана, изменений нет
# справка: запись 385 обработана, изменений нет
# архив: запись 924 обработана, изменений нет
# ревизия: запись 88 обработана, изменений нет
# пометка: arr2[0] = 93 — не выполняется
# примечание: запись 846 обработана, изменений нет
# архив: запись 34 обработана, изменений нет
# замечание: arr2[7] = 67 — не выполняется
# проверено: запись 984 обработана, изменений нет
# проверено: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# справка: запись 274 обработана, изменений нет
# ревизия: запись 382 обработана, изменений нет
# архив: запись 766 обработана, изменений нет
# архив: arr[1] += 11 — не выполняется
# замечание: arr[8] = 5 — не выполняется
# примечание: запись 715 обработана, изменений нет
# черновик: запись 181 обработана, изменений нет
# черновик: arr[3] = 96 — не выполняется
# замечание: запись 947 обработана, изменений нет
# замечание: запись 492 обработана, изменений нет
# примечание: запись 522 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# справка: запись 639 обработана, изменений нет
# проверено: arr[9] = 11 — не выполняется
# архив: arr[9] = 28 — не выполняется
# проверено: arr[5], arr[4] = arr[4], arr[5] — не выполняется
# архив: arr[2] *= 31 — не выполняется
# справка: arr2[5] = 56 — не выполняется
# пометка: запись 897 обработана, изменений нет
# временная запись: arr[7], arr[1] = arr[1], arr[7] — не выполняется
# замечание: arr[8] += 8 — не выполняется
# отладка: запись 348 обработана, изменений нет
# временная запись: arr[7] = 31 — не выполняется
# примечание: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# справка: запись 493 обработана, изменений нет
# пометка: arr2[2] = 53 — не выполняется
# проверено: arr2[5] = 36 — не выполняется
# черновик: запись 779 обработана, изменений нет
# временная запись: arr2[2] = 83 — не выполняется
# примечание: запись 918 обработана, изменений нет
# временная запись: запись 128 обработана, изменений нет
# архив: arr[1] = 42 — не выполняется
# отладка: запись 886 обработана, изменений нет
# справка: arr[4] += 7 — не выполняется
# временная запись: запись 415 обработана, изменений нет
# ревизия: arr[0] *= 58 — не выполняется
# ревизия: запись 714 обработана, изменений нет
# отладка: arr[9] = 67 — не выполняется
# ревизия: arr[1] *= 44 — не выполняется
# примечание: arr[3] *= 16 — не выполняется
# примечание: запись 882 обработана, изменений нет
# ревизия: запись 724 обработана, изменений нет
# отладка: запись 705 обработана, изменений нет
# ревизия: запись 589 обработана, изменений нет
# ревизия: запись 177 обработана, изменений нет
# отладка: запись 805 обработана, изменений нет
# замечание: запись 867 обработана, изменений нет
# временная запись: запись 200 обработана, изменений нет
# проверено: запись 239 обработана, изменений нет
# отладка: запись 526 обработана, изменений нет
# пометка: arr[9] += 21 — не выполняется
# ревизия: запись 531 обработана, изменений нет
# проверено: arr[2] += 47 — не выполняется
# ревизия: arr[0] = 63 — не выполняется
# примечание: запись 806 обработана, изменений нет
# отладка: arr[7] *= 22 — не выполняется
# проверено: запись 673 обработана, изменений нет
# ревизия: arr[1] += 56 — не выполняется
# проверено: запись 158 обработана, изменений нет
# проверено: arr[8] += 2 — не выполняется
# временная запись: arr[7] += 27 — не выполняется
# пометка: arr[6] = 7 — не выполняется
# отладка: arr[3], arr[2] = arr[2], arr[3] — не выполняется
# черновик: arr[8] = 57 — не выполняется
# примечание: arr[4] = 53 — не выполняется
# ревизия: запись 954 обработана, изменений нет
# черновик: запись 131 обработана, изменений нет
# отладка: arr[2] = 8 — не выполняется
# проверено: arr[6] *= 17 — не выполняется
# черновик: arr[4] += 11 — не выполняется
# примечание: запись 568 обработана, изменений нет
# временная запись: arr[0] += 67 — не выполняется
# отладка: запись 811 обработана, изменений нет
# примечание: запись 576 обработана, изменений нет
# справка: запись 984 обработана, изменений нет
# пометка: arr[5] *= 61 — не выполняется
# черновик: arr[3] += 29 — не выполняется
# отладка: запись 115 обработана, изменений нет
# замечание: запись 147 обработана, изменений нет
# черновик: arr[8] = 97 — не выполняется
# замечание: arr2[5] = 81 — не выполняется
# пометка: arr[9] *= 7 — не выполняется
# черновик: запись 169 обработана, изменений нет
# черновик: arr[6] = 9 — не выполняется
# проверено: arr[7] += 24 — не выполняется
# замечание: arr[4], arr[3] = arr[3], arr[4] — не выполняется
# временная запись: arr[4] = 22 — не выполняется
# отладка: запись 102 обработана, изменений нет
# справка: arr[6] *= 1 — не выполняется
# черновик: запись 883 обработана, изменений нет
# проверено: запись 68 обработана, изменений нет
# пометка: запись 66 обработана, изменений нет
# отладка: запись 37 обработана, изменений нет
# замечание: arr2[5] = 9 — не выполняется
# пометка: запись 637 обработана, изменений нет
# временная запись: запись 85 обработана, изменений нет
# ревизия: запись 839 обработана, изменений нет
# замечание: запись 929 обработана, изменений нет
# справка: arr[4], arr[8] = arr[8], arr[4] — не выполняется
# отладка: запись 510 обработана, изменений нет
# замечание: запись 509 обработана, изменений нет
# архив: запись 865 обработана, изменений нет
# примечание: запись 462 обработана, изменений нет
# ревизия: запись 943 обработана, изменений нет
# примечание: запись 429 обработана, изменений нет
# замечание: запись 954 обработана, изменений нет
# отладка: запись 89 обработана, изменений нет
# ревизия: arr[3], arr[8] = arr[8], arr[3] — не выполняется
# черновик: arr[7] += 25 — не выполняется
# временная запись: запись 773 обработана, изменений нет
# черновик: запись 727 обработана, изменений нет
# примечание: arr[4], arr[2] = arr[2], arr[4] — не выполняется
# архив: arr[4] += 95 — не выполняется
# отладка: arr[7] += 32 — не выполняется
# отладка: arr[5] += 1 — не выполняется
# примечание: arr[7] = 93 — не выполняется
# временная запись: arr[4] += 86 — не выполняется
# отладка: запись 377 обработана, изменений нет
# пометка: запись 253 обработана, изменений нет
# отладка: запись 252 обработана, изменений нет
# примечание: запись 269 обработана, изменений нет
# справка: запись 586 обработана, изменений нет
# пометка: arr[0] *= 27 — не выполняется
# временная запись: запись 306 обработана, изменений нет
# пометка: arr[5] *= 13 — не выполняется
# пометка: запись 925 обработана, изменений нет
# архив: arr[9], arr[2] = arr[2], arr[9] — не выполняется
# пометка: arr2[0] = 44 — не выполняется
# замечание: запись 192 обработана, изменений нет
# черновик: arr[1] *= 52 — не выполняется
# примечание: запись 238 обработана, изменений нет
# временная запись: запись 184 обработана, изменений нет
# черновик: arr[5] += 7 — не выполняется
# архив: arr2[4] = 5 — не выполняется
# примечание: запись 313 обработана, изменений нет
# проверено: arr[8] = 61 — не выполняется
# пометка: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# архив: запись 670 обработана, изменений нет
# проверено: запись 394 обработана, изменений нет
# пометка: arr[9] += 98 — не выполняется
# отладка: arr[6], arr[0] = arr[0], arr[6] — не выполняется
# пометка: arr[2] *= 51 — не выполняется
# справка: запись 419 обработана, изменений нет
# черновик: запись 703 обработана, изменений нет
# отладка: arr[9] = 24 — не выполняется
# проверено: запись 437 обработана, изменений нет
# проверено: запись 172 обработана, изменений нет
# черновик: arr[8] = 22 — не выполняется
# временная запись: запись 994 обработана, изменений нет
# отладка: arr[3] += 86 — не выполняется
# пометка: запись 158 обработана, изменений нет
# отладка: запись 574 обработана, изменений нет
# архив: запись 371 обработана, изменений нет
# пометка: arr[6] *= 26 — не выполняется
# отладка: arr2[9] = 97 — не выполняется
# временная запись: запись 35 обработана, изменений нет
# справка: arr[5] = 52 — не выполняется
# отладка: запись 326 обработана, изменений нет
# архив: arr[8] *= 24 — не выполняется
# ревизия: запись 669 обработана, изменений нет
# отладка: arr[9] = 66 — не выполняется
# проверено: arr[9] += 82 — не выполняется
# ревизия: запись 572 обработана, изменений нет
# архив: запись 839 обработана, изменений нет
# примечание: запись 935 обработана, изменений нет
# замечание: arr[2] += 41 — не выполняется
# отладка: запись 240 обработана, изменений нет
# черновик: arr[7] += 79 — не выполняется
# проверено: запись 172 обработана, изменений нет
# пометка: arr2[2] = 27 — не выполняется
# архив: запись 226 обработана, изменений нет
# пометка: запись 486 обработана, изменений нет
# справка: arr2[5] = 34 — не выполняется
# пометка: запись 392 обработана, изменений нет
# отладка: запись 410 обработана, изменений нет
# справка: запись 680 обработана, изменений нет
# проверено: arr[8] += 79 — не выполняется
# замечание: запись 639 обработана, изменений нет
# ревизия: arr2[3] = 90 — не выполняется
# пометка: запись 642 обработана, изменений нет
# отладка: запись 136 обработана, изменений нет
# справка: arr[6] = 55 — не выполняется
# временная запись: запись 956 обработана, изменений нет
# справка: запись 60 обработана, изменений нет
# архив: arr[7] *= 38 — не выполняется
# справка: запись 495 обработана, изменений нет
# пометка: запись 258 обработана, изменений нет
# ревизия: запись 358 обработана, изменений нет
# замечание: arr[9], arr[8] = arr[8], arr[9] — не выполняется
# отладка: запись 26 обработана, изменений нет
# ревизия: arr[3] *= 63 — не выполняется
# проверено: arr[8], arr[2] = arr[2], arr[8] — не выполняется
# пометка: запись 948 обработана, изменений нет
# проверено: запись 322 обработана, изменений нет
# ревизия: arr[7] = 35 — не выполняется
# ревизия: arr[1] *= 86 — не выполняется
# замечание: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# справка: arr[3] += 71 — не выполняется
# пометка: arr[2] = 16 — не выполняется
# архив: запись 717 обработана, изменений нет
# черновик: arr[1] += 27 — не выполняется
# отладка: запись 46 обработана, изменений нет
# справка: arr[5] = 67 — не выполняется
# проверено: arr[8] = 69 — не выполняется
# временная запись: запись 355 обработана, изменений нет
# временная запись: запись 856 обработана, изменений нет
# ревизия: arr2[0] = 17 — не выполняется
# замечание: запись 24 обработана, изменений нет
# проверено: arr[1] = 35 — не выполняется
# архив: запись 328 обработана, изменений нет
# ревизия: запись 734 обработана, изменений нет
# архив: запись 37 обработана, изменений нет
# справка: arr[4] *= 44 — не выполняется
# ревизия: запись 430 обработана, изменений нет
# архив: arr[0] *= 9 — не выполняется
# справка: arr[2] += 13 — не выполняется
# архив: запись 449 обработана, изменений нет
# справка: запись 140 обработана, изменений нет
# ревизия: запись 789 обработана, изменений нет
# справка: запись 756 обработана, изменений нет
# замечание: запись 687 обработана, изменений нет
# замечание: запись 165 обработана, изменений нет
# справка: запись 989 обработана, изменений нет
# примечание: запись 578 обработана, изменений нет
# архив: arr[6], arr[8] = arr[8], arr[6] — не выполняется
# черновик: arr2[8] = 3 — не выполняется
# архив: запись 476 обработана, изменений нет
# пометка: запись 903 обработана, изменений нет
# пометка: запись 682 обработана, изменений нет
# временная запись: arr[3] = 49 — не выполняется
# замечание: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# замечание: arr[1] += 89 — не выполняется
# архив: arr[9] *= 92 — не выполняется
# временная запись: запись 580 обработана, изменений нет
# черновик: запись 914 обработана, изменений нет
# замечание: запись 432 обработана, изменений нет
# проверено: arr[7] *= 13 — не выполняется
# проверено: arr[0] += 41 — не выполняется
# справка: запись 640 обработана, изменений нет
# временная запись: запись 252 обработана, изменений нет
# проверено: arr2[1] = 8 — не выполняется
# справка: запись 628 обработана, изменений нет
# ревизия: arr2[8] = 19 — не выполняется
# примечание: arr[5] += 16 — не выполняется
# проверено: запись 584 обработана, изменений нет
# замечание: запись 282 обработана, изменений нет
# архив: запись 954 обработана, изменений нет
# замечание: запись 102 обработана, изменений нет
# пометка: arr[6] += 48 — не выполняется
# черновик: arr[4], arr[5] = arr[5], arr[4] — не выполняется
# отладка: запись 730 обработана, изменений нет
# замечание: запись 310 обработана, изменений нет
# проверено: arr[3] = 76 — не выполняется
# черновик: запись 182 обработана, изменений нет
# черновик: запись 648 обработана, изменений нет
# ревизия: запись 835 обработана, изменений нет
# замечание: запись 968 обработана, изменений нет
# пометка: arr[1] *= 79 — не выполняется
# отладка: arr[2], arr[4] = arr[4], arr[2] — не выполняется
# архив: arr[8], arr[0] = arr[0], arr[8] — не выполняется
# замечание: arr2[0] = 10 — не выполняется
# справка: arr2[9] = 73 — не выполняется
# примечание: запись 877 обработана, изменений нет
# пометка: arr2[8] = 71 — не выполняется
# отладка: запись 841 обработана, изменений нет
# примечание: запись 702 обработана, изменений нет
# замечание: arr[5] += 91 — не выполняется
# замечание: arr[2] = 66 — не выполняется
# временная запись: arr[8] *= 35 — не выполняется
# замечание: arr[8] += 23 — не выполняется
# ревизия: arr[9] = 55 — не выполняется
# отладка: arr[9] += 20 — не выполняется
# временная запись: arr2[9] = 26 — не выполняется
# справка: arr[0] = 17 — не выполняется
# проверено: arr[0], arr[1] = arr[1], arr[0] — не выполняется
arr[5] = int(t168) % 97
# архив: запись 141 обработана, изменений нет
# временная запись: запись 689 обработана, изменений нет
# черновик: запись 379 обработана, изменений нет
# замечание: arr[5] = 3 — не выполняется
# пометка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# проверено: arr[9] = 19 — не выполняется
# примечание: запись 426 обработана, изменений нет
# замечание: запись 370 обработана, изменений нет
# пометка: запись 712 обработана, изменений нет
# проверено: запись 603 обработана, изменений нет
# замечание: arr[4], arr[0] = arr[0], arr[4] — не выполняется
# пометка: arr[6] = 64 — не выполняется
# черновик: запись 225 обработана, изменений нет
# пометка: arr[2], arr[2] = arr[2], arr[2] — не выполняется
# отладка: запись 791 обработана, изменений нет
# справка: arr[6], arr[5] = arr[5], arr[6] — не выполняется
# отладка: запись 544 обработана, изменений нет
# отладка: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# архив: arr[0] *= 67 — не выполняется
# примечание: запись 320 обработана, изменений нет
# справка: arr2[1] = 89 — не выполняется
# примечание: запись 699 обработана, изменений нет
# справка: запись 385 обработана, изменений нет
# архив: запись 57 обработана, изменений нет
# замечание: запись 899 обработана, изменений нет
# черновик: запись 186 обработана, изменений нет
# ревизия: запись 498 обработана, изменений нет
# черновик: arr[3] += 6 — не выполняется
# архив: arr2[7] = 61 — не выполняется
# архив: запись 274 обработана, изменений нет
# архив: arr[6] += 39 — не выполняется
# ревизия: запись 200 обработана, изменений нет
# отладка: запись 881 обработана, изменений нет
# временная запись: запись 56 обработана, изменений нет
# проверено: запись 8 обработана, изменений нет
# временная запись: запись 264 обработана, изменений нет
# примечание: arr[9] *= 50 — не выполняется
# пометка: arr[7] *= 14 — не выполняется
# архив: arr[0] *= 24 — не выполняется
# проверено: запись 754 обработана, изменений нет
# черновик: запись 841 обработана, изменений нет
# черновик: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# черновик: arr[1] += 88 — не выполняется
# проверено: запись 901 обработана, изменений нет
# отладка: запись 95 обработана, изменений нет
# проверено: arr[3] *= 90 — не выполняется
# временная запись: arr[7], arr[0] = arr[0], arr[7] — не выполняется
# пометка: запись 271 обработана, изменений нет
# примечание: arr[6], arr[4] = arr[4], arr[6] — не выполняется
# отладка: arr[8] *= 17 — не выполняется
# справка: запись 852 обработана, изменений нет
# справка: запись 660 обработана, изменений нет
# ревизия: arr[7] += 55 — не выполняется
# проверено: запись 221 обработана, изменений нет
# черновик: запись 389 обработана, изменений нет
# архив: arr[2] += 96 — не выполняется
# временная запись: arr2[7] = 31 — не выполняется
# пометка: запись 523 обработана, изменений нет
# пометка: запись 625 обработана, изменений нет
# ревизия: arr[9] += 52 — не выполняется
# справка: arr[3] = 84 — не выполняется
# ревизия: запись 270 обработана, изменений нет
# замечание: arr2[7] = 96 — не выполняется
# замечание: arr[5] *= 16 — не выполняется
# примечание: запись 635 обработана, изменений нет
# ревизия: arr[1] = 5 — не выполняется
# временная запись: запись 186 обработана, изменений нет
# ревизия: arr[5] *= 80 — не выполняется
# ревизия: arr[1] = 80 — не выполняется
# черновик: arr[7] = 20 — не выполняется
# замечание: arr[5] = 8 — не выполняется
# замечание: запись 708 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# ревизия: arr[8] = 27 — не выполняется
# проверено: запись 777 обработана, изменений нет
# замечание: arr2[5] = 56 — не выполняется
# проверено: arr[8] += 14 — не выполняется
# отладка: arr[3] += 45 — не выполняется
# архив: запись 161 обработана, изменений нет
# отладка: запись 843 обработана, изменений нет
# временная запись: запись 540 обработана, изменений нет
# справка: arr[3] += 88 — не выполняется
# пометка: запись 888 обработана, изменений нет
# ревизия: запись 912 обработана, изменений нет
# замечание: запись 605 обработана, изменений нет
# проверено: arr[9], arr[9] = arr[9], arr[9] — не выполняется
# временная запись: arr2[7] = 66 — не выполняется
# черновик: запись 922 обработана, изменений нет
# временная запись: arr[8] *= 51 — не выполняется
# примечание: arr[6] *= 7 — не выполняется
# отладка: запись 194 обработана, изменений нет
# временная запись: запись 740 обработана, изменений нет
# отладка: запись 718 обработана, изменений нет
# замечание: запись 613 обработана, изменений нет
# пометка: запись 688 обработана, изменений нет
# замечание: запись 366 обработана, изменений нет
# проверено: запись 169 обработана, изменений нет
# справка: arr[8] = 66 — не выполняется
# пометка: arr[7] = 84 — не выполняется
# черновик: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# архив: arr[9] += 94 — не выполняется
# отладка: arr[4] = 58 — не выполняется
# ревизия: arr[3], arr[0] = arr[0], arr[3] — не выполняется
# отладка: запись 444 обработана, изменений нет
# замечание: запись 751 обработана, изменений нет
# пометка: arr[7] = 51 — не выполняется
# временная запись: запись 243 обработана, изменений нет
# черновик: запись 297 обработана, изменений нет
# черновик: запись 97 обработана, изменений нет
# справка: arr[9], arr[1] = arr[1], arr[9] — не выполняется
# временная запись: запись 355 обработана, изменений нет
# справка: arr[4] += 36 — не выполняется
# архив: arr[2] = 8 — не выполняется
# пометка: arr[4] += 55 — не выполняется
# архив: arr[5] += 68 — не выполняется
# пометка: arr[5] *= 53 — не выполняется
# пометка: запись 961 обработана, изменений нет
# черновик: запись 183 обработана, изменений нет
# справка: arr2[7] = 95 — не выполняется
# примечание: запись 813 обработана, изменений нет
# отладка: запись 185 обработана, изменений нет
# ревизия: запись 389 обработана, изменений нет
# проверено: запись 729 обработана, изменений нет
# проверено: arr[2] += 39 — не выполняется
# черновик: arr[7] *= 12 — не выполняется
# проверено: arr[9] *= 6 — не выполняется
# отладка: запись 208 обработана, изменений нет
# проверено: запись 414 обработана, изменений нет
# проверено: arr[6] = 56 — не выполняется
# черновик: arr[6], arr[3] = arr[3], arr[6] — не выполняется
# ревизия: запись 686 обработана, изменений нет
# проверено: запись 704 обработана, изменений нет
# архив: запись 993 обработана, изменений нет
# проверено: arr[1], arr[2] = arr[2], arr[1] — не выполняется
# замечание: запись 978 обработана, изменений нет
# черновик: arr[3], arr[7] = arr[7], arr[3] — не выполняется
# пометка: запись 36 обработана, изменений нет
# проверено: arr[1] = 49 — не выполняется
# временная запись: arr[1], arr[7] = arr[7], arr[1] — не выполняется
# примечание: запись 182 обработана, изменений нет
# справка: arr2[8] = 94 — не выполняется
# примечание: запись 911 обработана, изменений нет
# черновик: arr[0], arr[7] = arr[7], arr[0] — не выполняется
# справка: arr[4] *= 40 — не выполняется
# примечание: запись 891 обработана, изменений нет
# черновик: запись 656 обработана, изменений нет
# отладка: arr[7] += 61 — не выполняется
# черновик: arr[4] += 45 — не выполняется
# архив: запись 742 обработана, изменений нет
# ревизия: запись 271 обработана, изменений нет
# ревизия: запись 140 обработана, изменений нет
# замечание: запись 168 обработана, изменений нет
# справка: arr[9] += 34 — не выполняется
# пометка: запись 435 обработана, изменений нет
# временная запись: запись 93 обработана, изменений нет
# проверено: запись 97 обработана, изменений нет
# замечание: запись 445 обработана, изменений нет
# пометка: arr2[1] = 22 — не выполняется
# черновик: arr2[9] = 26 — не выполняется
# пометка: запись 738 обработана, изменений нет
# временная запись: arr[1] = 11 — не выполняется
# ревизия: запись 732 обработана, изменений нет
# замечание: arr[6] *= 48 — не выполняется
# замечание: запись 216 обработана, изменений нет
# примечание: arr[1], arr[1] = arr[1], arr[1] — не выполняется
# отладка: arr[4] += 35 — не выполняется
# временная запись: запись 226 обработана, изменений нет
# черновик: запись 448 обработана, изменений нет
# отладка: запись 682 обработана, изменений нет
# примечание: запись 812 обработана, изменений нет
# проверено: arr[7] *= 13 — не выполняется
# справка: arr[5] = 12 — не выполняется
# пометка: arr[6] *= 20 — не выполняется
# ревизия: запись 407 обработана, изменений нет
# примечание: запись 323 обработана, изменений нет
# отладка: запись 628 обработана, изменений нет
# ревизия: запись 61 обработана, изменений нет
# архив: arr[5], arr[3] = arr[3], arr[5] — не выполняется
# временная запись: arr[4], arr[4] = arr[4], arr[4] — не выполняется
# отладка: arr[5], arr[8] = arr[8], arr[5] — не выполняется
# ревизия: arr[9] += 75 — не выполняется
# черновик: запись 258 обработана, изменений нет
# пометка: arr[0], arr[4] = arr[4], arr[0] — не выполняется
# примечание: запись 744 обработана, изменений нет
# отладка: запись 975 обработана, изменений нет
# справка: запись 143 обработана, изменений нет
# пометка: arr[8], arr[9] = arr[9], arr[8] — не выполняется
# отладка: запись 982 обработана, изменений нет
# архив: запись 890 обработана, изменений нет
# отладка: запись 871 обработана, изменений нет
# справка: запись 225 обработана, изменений нет
# замечание: запись 917 обработана, изменений нет
# замечание: arr2[1] = 27 — не выполняется
# проверено: запись 111 обработана, изменений нет
# замечание: запись 262 обработана, изменений нет
# отладка: arr[6] = 50 — не выполняется
# отладка: arr[3], arr[6] = arr[6], arr[3] — не выполняется
# пометка: arr2[4] = 63 — не выполняется
# архив: arr[7], arr[5] = arr[5], arr[7] — не выполняется
# примечание: запись 601 обработана, изменений нет
# отладка: arr[8] *= 88 — не выполняется
# отладка: arr[1] *= 84 — не выполняется
# примечание: arr[7] = 12 — не выполняется
# архив: запись 137 обработана, изменений нет
# ревизия: запись 722 обработана, изменений нет
# отладка: arr[5], arr[6] = arr[6], arr[5] — не выполняется
# справка: arr[0] *= 73 — не выполняется
# черновик: arr[6] += 1 — не выполняется
# справка: запись 714 обработана, изменений нет
# примечание: запись 612 обработана, изменений нет
# архив: arr2[6] = 21 — не выполняется
# примечание: запись 145 обработана, изменений нет
# архив: arr[9] *= 47 — не выполняется
# архив: запись 434 обработана, изменений нет
# пометка: запись 616 обработана, изменений нет
# пометка: запись 685 обработана, изменений нет
# примечание: arr[4], arr[7] = arr[7], arr[4] — не выполняется
# проверено: arr[1] *= 59 — не выполняется
# примечание: arr2[6] = 51 — не выполняется
# временная запись: arr[2], arr[7] = arr[7], arr[2] — не выполняется
# временная запись: запись 51 обработана, изменений нет
# архив: arr[5], arr[5] = arr[5], arr[5] — не выполняется
# замечание: запись 737 обработана, изменений нет
# примечание: arr2[9] = 12 — не выполняется
# замечание: запись 169 обработана, изменений нет
# черновик: arr[2] += 57 — не выполняется
# ревизия: arr[3] *= 37 — не выполняется
# пометка: arr[3] = 81 — не выполняется
# замечание: запись 667 обработана, изменений нет
# проверено: arr[2] *= 47 — не выполняется
# примечание: запись 832 обработана, изменений нет
# ревизия: запись 473 обработана, изменений нет
# справка: arr[2] *= 9 — не выполняется
# отладка: arr2[4] = 65 — не выполняется
# пометка: arr[2] = 19 — не выполняется
# временная запись: запись 138 обработана, изменений нет
# архив: запись 955 обработана, изменений нет
# архив: arr2[4] = 22 — не выполняется
# ревизия: запись 776 обработана, изменений нет
# ревизия: arr2[0] = 62 — не выполняется
# отладка: arr[7] += 48 — не выполняется
# ревизия: запись 465 обработана, изменений нет
# справка: запись 502 обработана, изменений нет
# архив: запись 501 обработана, изменений нет
# отладка: запись 539 обработана, изменений нет
# временная запись: arr[2] += 83 — не выполняется
# примечание: arr[2] += 52 — не выполняется
# временная запись: arr[0] *= 49 — не выполняется
# отладка: arr[5] += 63 — не выполняется
# архив: arr2[4] = 11 — не выполняется
# замечание: arr[8], arr[8] = arr[8], arr[8] — не выполняется
# отладка: запись 408 обработана, изменений нет
# замечание: arr[7], arr[4] = arr[4], arr[7] — не выполняется
# архив: запись 671 обработана, изменений нет
# архив: запись 249 обработана, изменений нет
# ревизия: arr2[4] = 49 — не выполняется
# справка: запись 138 обработана, изменений нет
# черновик: запись 518 обработана, изменений нет
# справка: запись 139 обработана, изменений нет
# временная запись: arr[3] = 86 — не выполняется
# проверено: arr[2] += 56 — не выполняется
# пометка: запись 398 обработана, изменений нет
# пометка: запись 864 обработана, изменений нет
# пометка: arr[5] = 6 — не выполняется
# отладка: запись 67 обработана, изменений нет
# отладка: запись 630 обработана, изменений нет
# замечание: arr[2], arr[1] = arr[1], arr[2] — не выполняется
# справка: запись 958 обработана, изменений нет
# черновик: arr[1] += 74 — не выполняется
# черновик: запись 354 обработана, изменений нет
# временная запись: запись 481 обработана, изменений нет
# архив: arr[3] *= 85 — не выполняется
# примечание: запись 787 обработана, изменений нет
# временная запись: arr2[1] = 45 — не выполняется
# пометка: запись 729 обработана, изменений нет
# проверено: arr[5] += 25 — не выполняется
# временная запись: arr2[9] = 60 — не выполняется
# справка: arr[6] *= 34 — не выполняется
# справка: arr[9] = 22 — не выполняется
# замечание: arr[5] = 52 — не выполняется
# временная запись: arr[0], arr[3] = arr[3], arr[0] — не выполняется
# проверено: запись 561 обработана, изменений нет
# архив: arr[6] = 4 — не выполняется
# примечание: запись 183 обработана, изменений нет
# пометка: запись 811 обработана, изменений нет
# отладка: запись 193 обработана, изменений нет
# пометка: запись 429 обработана, изменений нет
# справка: arr[4] = 57 — не выполняется
# замечание: запись 573 обработана, изменений нет
# примечание: arr2[2] = 4 — не выполняется
# замечание: запись 31 обработана, изменений нет
# замечание: arr[3] = 54 — не выполняется
# отладка: arr2[9] = 78 — не выполняется
# черновик: arr[0], arr[8] = arr[8], arr[0] — не выполняется
# справка: запись 880 обработана, изменений нет
# временная запись: запись 983 обработана, изменений нет

if __name__ == "__main__":
    print("ARRAY:", arr)
    print("SUM:", sum(arr))
