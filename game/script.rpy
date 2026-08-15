# 너에게 물주는 법 - 메인 스크립트 (정의 + start 라벨)
# 국제농업전문고등학교 전학생 김남주의 이야기
#
# 스토리 라벨은 아래 파일들로 분리되어 있음
#   prologue.rpy       – 프롤로그
#   chapter1.rpy       – 챕터 1 인트로
#   event_umbrella.rpy – 이벤트 씬 1 (비 오는 날, 우산)
#   chapter2.rpy       – 챕터 2 인트로
#   event_barn.rpy     – 이벤트 씬 2 (학년 통합 축산 실습)
#   event_storage.rpy  – 이벤트 씬 4 (창고, 축제 준비)
#   event_maid_cafe.rpy – 이벤트 씬 6 (농업축제 메이드 카페)
#   event_fireworks.rpy – 이벤트 씬 6.5 (축제 후반, 불꽃놀이)
#   chapter3.rpy       – 챕터 3 인트로
#   event_library.rpy  – 이벤트 씬 5 (도서관과 밤의 해안가)
#   chapter4.rpy       – 챕터 4 인트로 + 학기말 공동 실습 평가 (온실)
#   event_coastal.rpy  – 이벤트 씬 3 (학교 앞 해변)
#   epilogue.rpy       – 에필로그 방학식 + 해피/새드 엔딩 분기

# ===== 캐릭터 정의 =====
default player_surname = "김"
default player_name = "남주"
define p = Character('[player_name]', color="#000000")
define h = Character('하린', color="#000000")
define y = Character('연희', color="#000000")
define u = Character('유나', color="#000000")
define t = Character('담임', color="#000000")
define teach = Character('교사', color="#000000")
define stu = Character('학생', color="#000000")
define aide = Character('학생회 진행 보조', color="#000000")
define lib = Character('사서', color="#000000")
define sen = Character('선배', color="#000000")
define unknown = Character('???', color="#000000")
define narrator = Character(None, what_italic=True)

# ===== 이미지 정의 =====
# 캐릭터 스탠딩 (원본 크기가 제각각이라 화면 세로 ~1000px 기준으로 개별 zoom)
image harin neutral = Transform("images/Seo_harin_1.png", zoom=0.33)
image yeonhee neutral = Transform("images/Kang_yeonhee_1.png", zoom=0.22)
image yuna neutral = Transform("images/Cha_yuna_1.png", zoom=0.3)
image namjoo neutral = Transform("images/Kim_nam_joo_1.png", zoom=0.33)

# 배경
image bg classroom = "images/school_classroom_1.png"
image bg school_gate_day = "images/school_playground_1.png"
image bg school_gate_sunset = "images/school_playground_sunset_1.png"
image bg dark_playground = "images/school_dark_playground_1.png"
image bg cafeteria = "images/Snack_bar_1.png"
image bg coastal_road = "images/coast_road_1.png"
image bg school_beach = "images/coast_road_1.png"
image bg practice_room = "images/school_practice_room_1.png"
image bg rooftop = "images/school_rooftop_coast_view_1.png"
image bg infirmary = "images/school_infirmary_1.png"
image bg infirmary_sunset = "images/school_infirmary_sunset_1.png"
image bg storage_room = "images/school_storage_room_1.png"
image bg festival = "images/School_Festival_1.png"
image bg gym= "images/school_gym_1.png"
image bg gym_2 = "images/school_gym_2.png"
image bg gym_sunset = "images/school_gym_sunset_1.png"
image bg gym_sunset_2 = "images/school_gym_sunset_2.png"
image bg school_whole = "images/school_whole_1.png"
image bg school_festival_hallway = "images/school_festival_hallway_1.png"
image bg school_library = "images/school_library_1.png"
image bg school_playground_sunset__rain_1 = "images/school_playground_sunset__rain_1.png"
image bg maid_cafe = "images/maid cafe classroom_1.jpg"
image bg school_fireworks = "images/school_fireworks_1.png"
image bg coastal_road_night = "images/coast_road_night_1.png"

# 인물별 이벤트 CG
image cg maid_harin = "images/event_maid_cafe classroom_Seo_harin_1.jpg"
image cg maid_yeonhee = "images/event_maid_cafe classroom_Kang_yeonhee_1.jpg"
image cg maid_yuna = "images/event_maid_cafe classroom_Cha_yuna_1.jpg"
image cg ocean_harin = "images/event_ocean_Seo_harin_1.jpg"
image cg ocean_yeonhee = "images/event_ocean_Kang_yeonhee_1.jpg"
image cg ocean_yuna = "images/event_ocean_Cha_yuna_1.jpg"
image cg fireworks_harin = "images/event_school_fireworks_Seo_harin_1.jpg"
image cg fireworks_yeonhee = "images/event_school_fireworks_Kang_yeonhee_1.jpg"
image cg fireworks_yuna = "images/event_school_fireworks_Cha_yuna_1.jpg"

# ===== 상태 변수 =====
# 엔딩 분기 판정용 (UI 표시는 하지 않음)
default harin_affection = 0
default yeonhee_affection = 0
default yuna_affection = 0


# 챕터별 선택한 이벤트 상대 (기록용)
default umbrella_partner = None    # 이벤트 1 – 비 오는 날, 우산
default coastal_partner = None     # 이벤트 3 – 학교 앞 해변
default barn_partner = None        # 이벤트 2 – 학년 통합 축산 실습
default storage_partner = None     # 이벤트 4 – 창고, 축제 준비
default maid_partner = None        # 이벤트 6 – 농업축제 메이드 카페
default fireworks_partner = None   # 이벤트 6.5 – 축제 후반, 불꽃놀이
default library_partner = None     # 이벤트 5 – 도서관과 밤의 해안가
default greenhouse_partner = None  # 챕터 4 – 학기말 공동 실습 평가 (온실)
default ending_promise_partner = None  # 이벤트 3에서 방학식 이후 약속을 받은 상대

# 기획서의 해피 엔딩/약속 분기 기준
define ending_affection_requirement = 6
define ending_route_choice_requirement = 3


# =========================================================
# 시작
# =========================================================
label start:
    stop music fadeout 1.0
    scene black
    with fade

    centered "{color=#ffffff}{size=+8}너에게 물주는 법{/size}\n\n{size=-4}국제농업전문고등학교 전학생의 이야기{/size}{/color}"
    with dissolve

    pause 1.0

    jump prologue
