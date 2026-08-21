# 프롤로그
# 5월 초 · 국제농업전문고등학교 정문 앞 → 교무실 → 교실 → 매점 → 하교

label prologue:
    scene bg school_gate_day
    with fade
    play music "audio/title_music_1.mp3" fadein 2.0

    $ player_surname = renpy.input("{color=#000000}성을 입력하세요.\n(입력 안하고 엔터를 누르면 \"김\"으로 설정됩니다){/color} ", default="", length=5)
    $ player_surname = player_surname.strip() or "김"
    $ player_name = renpy.input("{color=#000000}이름을 입력하세요.\n(입력 안하고 엔터를 누르면 \"남주\"로 설정됩니다){/color} ", default="", length=10)
    $ player_name = player_name.strip() or "남주"

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
    p "안녕하세요. [player_surname][player_name]라고 합니다."
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
    p "안녕, 내 이름은 [player_surname][player_name]라고 해. 좀 늦게 왔지만 잘 부탁해."
    t "자, 자기소개도 끝났으니 자리는 저기 뒤에 남은 자리에 가서 앉아."
    t "조회 시작할게."

    scene black
    with fade
    pause 0.5

    scene bg classroom
    with fade

    p "(후... 다행히 학교규정은 생각보다 간단하네.)"

    "[[부스럭거리는 소리]"

    show yeonhee neutral at center
    with dissolve

    y "안녕! 이름이… [player_name]? 맞지?! 내 이름은 강연희야! 편하게 연희라고 불러줘. 짝꿍이 됐으니까 잘 부탁해~"
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

    stop music fadeout 1.5
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
    p "음, 네. 상관없어요. 이름은 [player_surname][player_name]이고 2학년이에요."
    
    show harin neutral at center
    with dissolve
    
    
    h "저는 1학년 서하린이라고 해요. 감사합니다. 나중에는 제가 양보해 드릴게요."

    p "(뭔가 많이 소심해 보인다. 그래도 아는 사람이 생겨서 다행인 거겠지?)"

    "[[전학 첫날이 끝나간다.]"

    scene bg school_gate_sunset
    with fade
    play music "audio/title_music_1.mp3" fadein 2.0

    p "(아… 힘들다. 오늘은 빨리 씻고 자야겠다.)"
    p "(학생회 선배, 옆자리 연희, 매점에서 마주친 하린… 그래도 새로 알게 된 사람들이 있으니 살짝 기대된다.)"

    "[[오늘의 하루가 끝나가는지 저녁바람이 불어오고 있다.]"
    "[[방학까지는 앞으로 두 달도 채 남지 않았다.]"
    "[[짧은 시간이지만 큰 변화가 생긴다고 [player_name]는 생각치도 못하고 잠에 들었다.]"

    scene black
    with fade
    centered "{color=#ffffff}— 프롤로그 끝 —{/color}"
    with dissolve
    pause 1.5

    jump chapter1_common
