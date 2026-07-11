# 너에게 물주는 법 - 메인 스크립트
# 국제농업전문고등학교 전학생 김남주의 이야기

# ===== 호감도 UI 설정 =====
init -1 python:
    # 히로인별 정보 (이름 / 호감도 UI 오른쪽 얼굴 이미지 / 호감도 변수명)
    heroine_data = {
        "harin":   {"name": "서하린", "head": "images/Seo_harin_head_1.png",   "var": "harin_affection"},
        "yeonhee": {"name": "강연희", "head": "images/Kang_yeonhee_head_1.png", "var": "yeonhee_affection"},
        "yuna":    {"name": "차유나", "head": "images/Cha_yuna_head_1.png",     "var": "yuna_affection"},
    }

    # 캐릭터가 말할 때마다 "현재 히로인"을 기록해두는 콜백.
    # 선택지가 뜨면 직전에 말한 히로인의 호감도가 왼쪽 위에 표시된다.
    def make_heroine_cb(key):
        def cb(event, **kwargs):
            if event == "begin":
                store.current_heroine = key
        return cb

# ===== 캐릭터 정의 =====
define p = Character('남주', color="#e6d8a3")
define h = Character('하린', color="#f7b8c9", callback=make_heroine_cb("harin"))
define y = Character('연희', color="#ffd977", callback=make_heroine_cb("yeonhee"))
define u = Character('유나', color="#a3c8ff", callback=make_heroine_cb("yuna"))
define t = Character('담임', color="#cccccc")
define sen = Character('선배', color="#a3c8ff")
define unknown = Character('???', color="#bbbbbb")
define narrator = Character(None, what_italic=True)

# ===== 이미지 정의 =====
# 캐릭터 스탠딩 (참고 이미지처럼 크게 보이도록 zoom 적용)
image harin neutral = Transform("images/Seo_harin_1.png", zoom=1.55)
image yeonhee neutral = Transform("images/Kang_yeonhee_1.png", zoom=1.55)
image yuna neutral = Transform("images/Cha_yuna_1.png", zoom=1.55)

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

# ===== 상태 변수 =====
default harin_affection = 0
default yeonhee_affection = 0
default yuna_affection = 0

# 선택지가 떴을 때 호감도를 표시할 현재 히로인 (말할 때 자동으로 설정됨)
default current_heroine = None

# True이면 선택지에서 히로인 3명의 호감도를 모두 표시 (히로인 선택 메뉴용)
default show_all_affection = False


# 챕터별 선택한 이벤트 상대 (기록용)
default umbrella_partner = None
default coastal_partner = None


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


# =========================================================
# 프롤로그
# =========================================================
label prologue:
    scene bg school_gate_day
    with fade
    play music "audio/title_music_1.mp3" fadein 2.0

    "{i}[[농작물이 부족해진 세상, 농사 전문 학교들이 하나 둘 생겨났고, 농업 인재의 가치가 올라갔다.]{/i}"
    "{i}[[그중에서도 국제농업전문고등학교는 실습 시설과 취업률이 뛰어나 가장 인기 있는 농업 전문 학교 중 하나가 되었다.]{/i}"

    "5월 초 맑음"
    "국제농업전문고등학교 정문 앞."

    p "(드디어 국제농업전문고등학교에 도착했다.)"
    p "(학기 일정이 한창일 때 전학을 오게 됐네.)"
    p "(늦게 들어왔지만…. 늦은 만큼 열심히 하면 잘 될 거야!)"

    scene bg classroom
    with fade

    "잠시 후"
    "교무실 앞 복도."

    p "(서류 제출도 끝났다. 선생님께서 학생회가 학교 안내를 해준다고 했는데… 어디 있지?)"

    show yuna neutral at center
    with dissolve

    sen "안녕, 네가 전학생이구나."
    sen "내 이름은 차유나야."
    p "안녕하세요. 김남주라고 합니다."
    u "인사는 끝났으니까 간단하게 학교시설들 위치를 알려 줄게."
    u "학교 규정은 첫 조회 때 설명할 테니 듣고, 5월 전학이니 실습 진도는 담임한테 따로 물어봐."

    hide yuna
    with dissolve

    p "(이후에 학교시설을 안내받았다.)"
    p "(학교시설을 안내받는 동안 말투는 차가웠다.)"
    p "(하지만 일 처리는 정확했다.)"
    p "(남에게 관심 없어 보이지만, 사실 필요한 건 다 보고 있다.)"
    p "(헤어지기 전에 감사인사를 했지만 돌아오는 대답은 없었다.)"

    # 교실 씬
    scene bg classroom
    with fade

    "2-B 교실."
    p "(교실 문을 열자, 시선이 나에게 쏠렸다.)"

    t "자, 모두 주목. 오늘 새친구가 전학을 왔어."
    t "자기소개 해줄래?"
    p "안녕, 내 이름은 김남주라고 해. 좀 늦게 왔지만 잘 부탁해."
    t "자, 자기소개도 끝났으니 자리는 저기 뒤에 남은 자리에 가서 앉아."
    t "조회 시작할게."

    scene black
    with fade
    pause 0.5

    scene bg classroom
    with fade

    p "(후... 다행히 학교규정은 생각보다 간단하네.)"

    "[[부스럭거리는 소리]"

    play music "audio/Kang_yeonhee_bgm.mp3" fadein 2.0
    show yeonhee neutral at center
    with dissolve

    y "안녕! 이름이… 남주? 맞지?! 내 이름은 강연희야! 편하게 연희라고 불러줘. 짝꿍이 됐으니까 잘 부탁해~"
    p "그래. 잘 지내보자."
    p "(인싸다. 음, 인싸야.)"

    y "우리학교는 왜 왔어?? 5월에 우리학교로 전학오는 사람 처음 봤어."

    menu:
        "말해준다.":
            p "1학년 때 진로에 대한 고민을 많이 했었어. 이때 식량 부족 문제를 다룬 수업과 뉴스를 보고 농업에 관심을 갖게 돼서 이 학교여서 전학을 오게 됐어."
            y "정말?? 우리학교 들어오기 쉽지 않았을 텐데 대단하다!"
            $ yeonhee_affection += 1

        "말해주지 않는다.":
            p "지금은 말하고 싶지 않아."
            y "아직 … 아직 어색하구나. 어쩔 수 없지."
            y "나중에 말해주면 좋겠다."
            $ yeonhee_affection -= 1

        "딴 이야기를 한다.":
            p "것보다 오늘 급식 뭔지 알아?"
            y "응? 아 오늘 급식 진짜 맛있는 거 나와."
            y "카레라이스랑 돈가스가 같이 나오는 날이야."
            y "오늘 같은 날에 전학을 오다니 부럽다~"

    hide yeonhee
    with dissolve

    "이후 약간의 대화가 이어지고 다음 수업을 들었다."

    # 매점 씬
    p "(아 아침밥을 안 먹었더니 배고파졌다.)"
    p "(그러고 보니 매점이 있었지? 잠시 매점 좀 가봐야겠다.)"

    scene bg cafeteria
    with fade

    p "(음 뭐가 좋으려나… 어! 저기 딱 하나 남은 삼각김밥 먹어야겠다.)"

    "[[손을 뻗는 순간, 누군가와 손이 닿았다.]"

    unknown "…앗."
    p "…앗."

    "[[잠시 정적이 있었다.]"
    "[[누군가가 손을 조심스레 뺐다. 얼굴도 살짝 붉었다.]"

    unknown "…죄, 죄송합니다."
    p "아니에요. 드시고 싶으시면 가져가셔도 돼요. 저는 다른 거 먹어도 됩니다."
    unknown "…정말로 먹어도 되나요?"
    p "당연하죠."
    unknown "고마워요. 혹시… 나이랑 이름 좀 알려주실 수 있나요?"

    p "(갑자기 왜 물어보는 거지? 알려줘서 나쁠 건 없으니… 상관없겠지?)"
    p "음, 네. 상관없어요. 이름은 김남주이고 2학년이에요."
    h "저는 1학년 서하린이라고 해요. 감사합니다. 나중에는 제가 양보해 드릴게요."

    p "(뭔가 많이 소심해 보인다. 그래도 아는 사람이 생겨서 다행인 거겠지?)"

    hide harin
    with dissolve

    "[[전학 첫날이 끝나간다.]"

    scene bg school_gate_sunset
    with fade

    p "(아… 힘들다. 오늘은 빨리 씻고 자야겠다.)"
    p "(학생회 선배, 옆자리 연희, 매점에서 마주친 하린… 그래도 새로 알게 된 사람들이 있으니 살짝 기대된다.)"

    "[[오늘의 하루가 끝나가는지 저녁바람이 불어오고 있다.]"
    "[[방학까지는 앞으로 두 달도 채 남지 않았다.]"
    "[[짧은 시간이지만 큰 변화가 생긴다고 남주는 생각치도 못하고 잠에 들었다.]"

    scene black
    with fade
    centered "— 프롤로그 끝 —"
    with dissolve
    pause 1.5

    jump chapter1_common


# =========================================================
# 챕터 1 – 새로운 시작 (공통부)
# =========================================================
label chapter1_common:
    scene black
    with fade
    centered "{size=+6}챕터 1{/size}\n\n새로운 시작"
    with dissolve
    pause 1.5

    scene bg classroom
    with fade

    "5월 학교 생활 적응"

    narrator "전학 온 지 며칠이 지났다."
    narrator "처음에는 모든 게 낯설었다."
    narrator "벽에 실습 일정, 학교 규정, 동아리 안내, 급식표 같은 것들이 빼곡하게 붙어 있었다."
    
    scene bg practice_room
    with fade

    p "생각보다 챙겨야 할 게 많네."

    narrator "농업 전문 학교라는 말은 알고 있었지만, 실제로 다녀보니 더 실감이 났다."
    narrator "처음에는 길을 잘못 들어 다른 반 실습실 앞까지 간 적도 있었다."
    narrator "그래도 조금씩 익숙해지고 있었다."

    scene bg classroom
    with fade

    narrator "아침에 교실에 들어가면 연희가 먼저 손을 흔들었다."
    narrator "말이 많긴 했지만, 덕분에 어색한 분위기가 조금은 풀렸다."
    narrator "점심시간에 매점 쪽을 지나가면 가끔 하린이 눈에 들어왔다."
    narrator "하린은 늘 조용했지만, 마주치면 작게 고개를 숙여 인사했다."
    narrator "복도 게시판 앞이나 학생회실 근처에서는 선배를 몇 번 마주쳤다."
    narrator "선배는 여전히 말수가 적었고 표정도 차분했지만, 필요한 일은 빠뜨리지 않는 사람이었다."

    narrator "낯선 교실. 낯선 실습복 냄새. 낯선 이름들."
    narrator "그런 것들이 하루하루 조금씩 익숙해졌다."

    narrator "조용히 고개를 숙이던 하린."
    narrator "밝게 먼저 말을 걸어오던 연희."
    narrator "말은 차가웠지만 해야 할 일은 정확히 챙기던 선배."

    narrator "아직은 전부 어색한 사이였다."

    narrator "그러던 어느 날이었다."
    narrator "수업이 끝나자마자 하늘이 무너지듯 비가 쏟아졌다."

    jump event_umbrella
