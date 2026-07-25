# 너에게 물주는 법 - 메인 스크립트 (정의 + start 라벨)
# 국제농업전문고등학교 전학생 김남주의 이야기
#
# 스토리 라벨은 아래 파일들로 분리되어 있음
#   prologue.rpy       – 프롤로그
#   chapter1.rpy       – 챕터 1 인트로
#   event_umbrella.rpy – 이벤트 씬 1 (비 오는 날, 우산)
#   event_coastal.rpy  – 이벤트 씬 3 (청소 후, 해안가 도로)
#   chapter2.rpy       – 챕터 2 인트로
#   event_barn.rpy     – 이벤트 씬 2 (학년 통합 축산 실습)
#   event_storage.rpy  – 이벤트 씬 4 (창고, 축제 준비)
#   event_maid_cafe.rpy – 이벤트 씬 6 (농업축제 메이드 카페)
#   chapter3.rpy       – 챕터 3 인트로
#   event_library.rpy  – 이벤트 씬 5 (도서관과 밤의 해안가)
#   chapter4.rpy       – 챕터 4 인트로 + 학기말 공동 실습 평가 (온실)
#   epilogue.rpy       – 에필로그 방학식 + 해피/새드 엔딩 분기

# ===== 캐릭터 정의 =====
define p = Character('남주', color="#e6d8a3")
define h = Character('하린', color="#f7b8c9")
define y = Character('연희', color="#ffd977")
define u = Character('유나', color="#a3c8ff")
define t = Character('담임', color="#cccccc")
define teach = Character('교사', color="#cccccc")
define stu = Character('학생', color="#cccccc")
define lib = Character('사서', color="#cccccc")
define sen = Character('선배', color="#a3c8ff")
define unknown = Character('???', color="#bbbbbb")
define narrator = Character(None, what_italic=True)

# ===== 이미지 정의 =====
# 캐릭터 스탠딩 (원본 크기가 제각각이라 화면 세로 ~1000px 기준으로 개별 zoom)
image harin neutral = Transform("images/Seo_harin_1.png", zoom=0.33)
image yeonhee neutral = Transform("images/Kang_yeonhee_1.png", zoom=0.22)
image yuna neutral = Transform("images/Cha_yuna_1.png", zoom=1.56)

# 배경
image bg classroom = "images/school_classroom_1.png"
image bg school_gate_day = "images/school_playground_1.png"
image bg school_gate_sunset = "images/school_playground_sunset_1.png"
image bg dark_playground = "images/school_dark_playground_1.png"
image bg cafeteria = "images/Snack_bar_1.png"
image bg coastal_road = "images/coast_road_1.png"
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

# ===== 상태 변수 =====
# 엔딩 분기 판정용 (UI 표시는 하지 않음)
default harin_affection = 0
default yeonhee_affection = 0
default yuna_affection = 0


# 챕터별 선택한 이벤트 상대 (기록용)
default umbrella_partner = None    # 이벤트 1 – 비 오는 날, 우산
default coastal_partner = None     # 이벤트 3 – 청소 후, 해안가 도로
default barn_partner = None        # 이벤트 2 – 학년 통합 축산 실습
default storage_partner = None     # 이벤트 4 – 창고, 축제 준비
default maid_partner = None        # 이벤트 6 – 농업축제 메이드 카페
default library_partner = None     # 이벤트 5 – 도서관과 밤의 해안가
default greenhouse_partner = None  # 챕터 4 – 학기말 공동 실습 평가 (온실)


# =========================================================
# 시작
# =========================================================
label start:
    stop music fadeout 1.0
    scene black
    with fade

    centered "{size=+8}너에게 물주는 법{/size}\n\n{size=-4}국제농업전문고등학교 전학생 김남주의 이야기{/size}"
    with dissolve

    pause 1.0

    jump prologue
