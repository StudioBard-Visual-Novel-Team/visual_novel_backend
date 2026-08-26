# 이벤트 씬 3 – 학교 앞 해변
# 챕터 4의 학기말 공동 실습 평가 이후, 같은 날 오후 진행

label event_coastal_intro:
    scene bg school_beach
    with fade
    stop music fadeout 1.5
    # play sound "audio/ocean_waves_1.mp3" fadein 2.0 loop
    # play music "audio/ocean_waves_1.mp3" fadein 2.0

    "같은 날 오후, 학교 앞 해변."

    narrator "준비해 온 수영복으로 갈아입은 학생들이 모래사장에 모였다."
    narrator "오전 내내 실습 평가를 치른 학생들은 가방과 수건을 내려놓으며 긴장을 풀었다."
    narrator "학생회 진행 보조가 안전선과 구급함의 위치를 안내했다."

    aide "물에 들어갈 때는 혼자 움직이지 말고, 안전선 밖으로 나가지 마세요. 몸이 불편하면 바로 학생회에 알려주세요."

    narrator "안내가 끝나자 연희는 가장 먼저 물가로 달려갔다."

    show yeonhee neutral at center
    with dissolve

    y "드디어 끝났다!"
    p "넘어지기 전에 천천히 가."

    hide yeonhee
    with dissolve

    narrator "연희는 뒤를 돌아 손을 흔든 뒤 얕은 물속으로 뛰어들었다."
    narrator "하린은 수건이 든 가방을 안고 바다와 학생들을 번갈아 바라봤다."
    narrator "잠시 머뭇거리던 하린은 가방을 내려놓고 파도가 닿는 곳으로 한 걸음 다가갔다."
    narrator "선배는 학생회 진행 보조에게 참가자 명단과 구급함을 전달했다."

    show yuna neutral at center
    with dissolve

    sen "인원 확인이 끝나면 알려줘. 안전선 쪽도 한 번씩 확인하고."
    
    hide yuna
    with dissolve

    aide "네. 선배도 이제 쉬세요."

    narrator "선배는 닫힌 파일을 내려다보다가 수건 위에 내려놓았다."
    narrator "파도가 모래사장 가까이 밀려왔다가 천천히 빠져나갔다."
    narrator "연희는 다른 학생들과 비치볼을 주고받기 시작했다. 하린은 사람들과 조금 떨어진 곳에서 발끝으로 바닷물을 건드리고 있었다."
    narrator "선배는 일을 넘기고도 파일 근처에 남아 해변을 살피고 있었다."
    narrator "나는 세 사람을 차례로 바라봤다."

    menu:
        "학교 앞 해변에서 함께할 상대를 고른다."
        "하린에게 다가간다.":
            $ coastal_partner = "harin"
            jump coastal_harin
        "연희와 함께 물에 들어간다.":
            $ coastal_partner = "yeonhee"
            jump coastal_yeonhee
        "선배에게 같이 걷자고 한다.":
            $ coastal_partner = "yuna"
            jump coastal_yuna


label coastal_harin:
    scene cg ocean_harin
    with dissolve
    pause

    narrator "나는 신발을 벗고 하린이 서 있는 물가로 다가갔다."
    narrator "하린은 발목까지 밀려온 파도를 내려다보다가 내 쪽으로 조금 자리를 내줬다."

    p "같이 있어도 돼?"
    h "네. 아직 깊은 곳까지는 못 갈 것 같지만요."
    p "여기까지만 있어도 돼."

    narrator "다음 파도가 다가오자 하린의 어깨가 작게 움츠러들었다. 그러나 이번에는 물러나지 않았다."
    narrator "하린은 파도가 닿지 않는 곳에 수건과 가방을 내려놓았다."
    narrator "한동안 발밑의 모래를 바라보던 하린은 샌들을 벗고 다시 물가로 걸어갔다."
    narrator "차가운 파도가 발끝을 덮자 하린의 발이 잠시 멈췄다."

    h "생각보다 차가워요."
    p "조금 있다가 들어가도 돼."
    h "아니에요. 바로 피하지 않고 조금 더 있어 볼게요."

    narrator "다음 파도가 발목까지 밀려왔다."
    narrator "하린은 물 위에 흔들리는 자신의 모습을 내려다보다가 작게 웃었다."
    narrator "그때 학생들이 사용하던 작은 비치볼 하나가 파도에 밀려 하린 쪽으로 떠내려왔다."

    stu "미안해! 공 좀 보내줄래?"

    narrator "하린은 주변을 둘러봤다."
    narrator "공은 파도에 밀려 조금씩 멀어지고 있었다. 하린은 잠시 망설였지만 곧 물속으로 몇 걸음 들어갔다."
    narrator "파도가 무릎 가까이 올라오자 하린은 몸의 균형을 잡고 비치볼을 붙잡았다."

    h "받으세요."

    narrator "하린이 공을 던지자 학생은 고맙다는 말을 남기고 돌아갔다."
    narrator "하린은 젖은 손을 내려다보다가 천천히 물 밖으로 나왔다."

    p "아까보다 깊은 곳까지 들어갔네."
    h "공이 더 멀리 가면 곤란할 것 같아서요."
    p "그래도 직접 갔잖아."
    h "생각할 시간이 길어지면 못 갔을지도 몰라요."
    p "먼저 움직인 건 잘한 거야."

    narrator "우리는 사람들이 적은 해변 끝으로 자리를 옮겼다."
    narrator "하린은 수건 위에 앉아 젖은 발을 모래 위로 뻗었다. 파도가 들어올 때마다 모래 위에 남은 발자국이 조금씩 흐려졌다."
    narrator "멀리서 학생들의 웃음소리와 공이 튀는 소리가 들렸다."
    narrator "하린은 파도에 지워지는 발자국을 바라봤다."

    h "전에는 저런 곳에 있으면 언제 빠져나와야 할지만 생각했어요."
    p "지금도 불편해?"
    h "조금은요. 그래도 아까는 도망가고 싶다는 생각보다 공을 잡아야겠다는 생각이 먼저 들었어요."
    p "그럼 전보다 나아진 거네."
    h "선배를 만나고 나서부터, 가끔은 먼저 해보고 싶다는 생각이 들어요."
    p "하고 싶은 게 생기면 해도 돼."
    h "시작하면 끝나는 것도 생기잖아요."
    h "좋은 일이 생기면 끝난 뒤가 먼저 걱정될 때가 있어요."
    p "오늘도 그래?"

    h "오늘이 즐거울수록 나중에 더 아쉬울 것 같아요."
    p "아쉬우면 다시 오면 돼."
    p "오늘 한 번 왔다고 마지막일 필요는 없잖아."
    h "선배는 다음이라는 말을 자연스럽게 하시네요."
    p "지킬 생각으로 하는 말이니까."

    python:
        _route_count = sum(1 for v in (
            umbrella_partner, barn_partner, storage_partner,
            maid_partner, library_partner, greenhouse_partner,
        ) if v == "harin")

    if harin_affection >= ending_affection_requirement and _route_count >= ending_route_choice_requirement:
        $ ending_promise_partner = "harin"

        h "선배는 오늘 본 바다도 나중에 기억하실 건가요?"
        p "하린이랑 같이 온 바다로 기억할 거야."
        narrator "하린은 파도 쪽으로 시선을 돌렸다."
        narrator "입술을 달싹이던 하린은 수건 끝을 정리하고 자리에서 일어났다."
        h "방학식 끝나고 만날까요?"
        p "어디로 가면 돼?"
        h "온실이요."
        p "온실?"
        h "둘이서 조용히 이야기할 수 있는 곳이 좋아서요."
        h "방울토마토 구역 앞에서 기다릴게요."
        p "방학식 끝나고 바로 갈게."
        h "이번에는 제가 먼저 기다리고 있을게요."
        p "너무 오래 기다리게 하지는 않을게."
        h "괜찮아요. 선배가 온다고 말씀해 주셨으니까요."
    else:
        h "오늘은 오래 기억날 것 같아요."
        p "나도."
        narrator "하린은 무언가 말하려다 가방의 지퍼를 잠갔다."
        h "같이 있어 주셔서 감사해요."
        p "나도 하린이랑 와서 좋았어."

    hide harin
    with dissolve
    jump coastal_end


label coastal_yeonhee:
    scene cg ocean_yeonhee
    with dissolve
    pause

    narrator "나는 연희가 사람들 사이로 들어가기 전에 이름을 불렀다."

    p "연희야."
    p "저쪽으로 같이 갈래?"
    y "둘이서?"
    p "응. 오늘은 너랑 따로 있고 싶어."
    narrator "연희는 잠시 말없이 나를 바라봤다."
    narrator "이내 연희는 수건이 든 가방을 들고 내 옆으로 다가왔다."
    y "그럼 재미없다고 먼저 돌아가면 안 된다?"
    p "내가 불렀는데 왜 먼저 가."
    y "좋아. 그 말 기억해둘게."

    narrator "우리는 신발과 수건을 모래사장에 내려놓고 사람이 적은 물가로 걸어갔다."
    narrator "연희는 발목까지 차오르는 물속에 먼저 들어갔다."

    y "생각보다 차갑다."
    p "추우면 조금만 들어가."

    narrator "연희는 대답 대신 발끝으로 물을 걷어찼다. 작은 물보라가 내 다리에 튀었다."

    p "지금 일부러 그랬지?"
    y "파도가 그런 건데?"

    narrator "연희는 모르는 척 바다 쪽으로 시선을 돌렸다."
    narrator "나는 발로 물을 밀어 연희 쪽으로 보냈다."
    narrator "연희는 팔을 들어 물을 막다가 뒤로 몇 걸음 물러났다."

    y "잠깐, 이렇게 나오겠다는 거지?"

    narrator "우리는 얕은 물 안에서 서로를 피해 움직였다."
    narrator "발이 물속으로 들어갈 때마다 작은 물보라가 주변으로 퍼졌다."
    narrator "연희는 내 옆을 지나가며 손으로 물을 밀었다. 나는 몸을 돌려 피했지만 셔츠 끝이 젖었다."

    p "이제 그만하자."
    y "먼저 시작한 사람이 할 말은 아닌데?"
    p "처음 시작한 건 너야."

    narrator "그때 조금 높은 파도가 연희의 다리를 덮었고, 젖은 모래가 발밑에서 밀리며 연희의 몸이 옆으로 기울었다."
    narrator "나는 가까이 다가가 연희의 팔을 붙잡았다."
    narrator "연희는 내 어깨에 손을 올리고 가까스로 균형을 잡았다."
    narrator "파도가 빠져나간 뒤에도 연희는 잠시 움직이지 않았다."

    p "괜찮아?"
    y "응. 다친 건 아니야."
    y "방금 건 못 본 걸로 해줘."
    p "여기에는 나밖에 없잖아."
    y "그러니까 너만 모른 척하면 돼."
    p "일단 나가서 쉬자."

    narrator "연희는 이번에는 장난치지 않고 고개를 끄덕였다."

    narrator "우리는 물 밖으로 나와 수건 위에 나란히 앉았다."
    narrator "다른 학생들의 목소리는 멀리서 희미하게 들렸다. 가까운 곳에는 파도가 모래를 쓸고 지나가는 소리만 이어졌다."
    narrator "연희는 조금 전까지 크게 웃던 모습과 달리 조용히 바다를 바라봤다."

    p "발은 괜찮아?"
    y "괜찮아. 조금 놀란 것뿐이야."
    p "그럼 잠깐 쉬었다가 가자."

    narrator "잠시 동안 두 사람 사이에 대화가 이어지지 않았다."
    narrator "바람이 불자 젖은 머리카락 몇 가닥이 연희의 뺨에 달라붙었다. 연희는 머리카락을 귀 뒤로 넘기고 내 쪽을 바라봤다."

    y "내가 조용하니까 어색해?"
    p "아니."
    p "계속 말하려고 애쓰지 않아도 돼."
    y "사람이 많으면 계속 뭔가 해야 할 것 같아."
    p "왜?"
    y "내가 먼저 말하지 않으면 분위기가 금방 가라앉잖아."
    p "가라앉아도 괜찮아."
    y "다들 즐거워 보이면 내가 잘하고 있는 것 같거든."
    p "여기서는 잘하려고 하지 않아도 돼."
    p "내가 같이 있고 싶어서 부른 거야."
    y "내가 재미있는 말을 안 해도?"
    p "연희가 조용하다고 다른 사람이 되는 건 아니잖아."
    y "그럼 오늘은 조금 조용히 있어볼게."
    p "그래."

    narrator "두 사람은 나란히 앉아 바다를 바라봤다."
    narrator "연희는 침묵을 채우려 하지 않았다. 물 위에 비친 햇빛이 흔들릴 때마다 연희의 시선도 천천히 움직였다."
    y "생각보다 안 불편하네."
    p "나는 처음부터 괜찮았어."

    python:
        _route_count = sum(1 for v in (
            umbrella_partner, barn_partner, storage_partner,
            maid_partner, library_partner, greenhouse_partner,
        ) if v == "yeonhee")

    if yeonhee_affection >= ending_affection_requirement and _route_count >= ending_route_choice_requirement:
        $ ending_promise_partner = "yeonhee"

        y "방학이 시작되면 지금처럼 매일 보지는 못하겠네."
        p "연락하면 볼 수 있어."
        y "내가 먼저 연락하지 않아도?"
        p "내가 먼저 할게."
        y "그럼 방학식 끝나고 바로 가지 마."
        p "교실에서 기다리면 돼?"
        y "응. 다른 애들이 모두 나간 뒤까지 기다려줘."
        p "할 말이 있어?"
        y "지금 말하면 또 웃으면서 넘길 것 같아."
        y "그날은 제대로 말할게."
        p "알았어. 기다릴게."
        y "이번에는 그 말 그대로 믿어볼게."
    else:
        y "생각보다 오래 쉬었네."
        p "이제 다시 들어갈까?"
        y "응. 이번에는 천천히 갈게."
        y "다음에도 기회가 있으면 둘이 놀자."

    hide yeonhee
    with dissolve
    jump coastal_end


label coastal_yuna:
    scene cg ocean_yuna
    with dissolve
    pause

    narrator "선배는 진행 보조에게 일을 넘기고도 수건 위의 파일을 바라보고 있었다."

    p "잠깐 걸으실래요?"
    sen "여기 있어도 바다는 보여."
    p "파일도 같이 보이잖아요."

    narrator "선배는 파일 위에 올려두었던 손을 내렸다."

    sen "멀리 가지는 마."
    p "안전선 안에서만 걸을게요."

    narrator "선배와 나는 물가를 따라 천천히 걸었다."
    narrator "차가운 파도가 발목에 닿자 선배의 발이 반걸음 뒤로 움직였다."

    p "차갑죠?"
    sen "생각보다 조금."

    narrator "나는 먼저 얕은 물 안으로 들어갔다."
    narrator "선배는 안전선과 구급함이 놓인 곳을 한 번 바라본 뒤 내 옆으로 걸어왔다."
    narrator "바람이 불어 안내 종이 몇 장이 날아갔지만, 가까이에 있던 학생들이 먼저 종이를 잡아왔다."
    stu "선배, 여기요."
    sen "고마워."

    narrator "학생은 종이를 진행 보조에게 건넨 뒤 다시 친구들에게 돌아갔다."
    narrator "선배는 멈춰 선 채 그 모습을 바라봤다."

    p "선배가 직접 가지 않아도 해결됐네요."
    sen "그러네."
    narrator "한동안 우리는 파도가 들어오고 나가는 모습을 바라봤다."
    p "아직도 일이 신경 쓰여요?"
    sen "내가 확인하지 않으면 빠진 게 생길 것 같아서."
    p "지금까지는 빠진 게 없잖아요."
    sen "그래도 직접 확인하는 편이 편해."
    p "선배가 계속 직접 하면 다른 사람은 맡을 기회가 없어요."
    narrator "선배는 젖은 모래 위에 남은 발자국을 내려다봤다."
    narrator "파도가 밀려와 두 사람의 발자국 일부를 지웠다."
    sen "오늘은 생각보다 많이 맡겼어."
    p "그래서 문제 생겼어요?"
    narrator "멀리서 진행 보조가 이상 없다는 표시로 손을 들어 보였다."
    narrator "선배도 짧게 손을 들어 답했다."
    sen "아니."

    narrator "우리는 수건이 놓인 자리로 돌아왔다. 선배는 가방 옆에 앉았지만 파일을 꺼내지 않았다."

    p "아무것도 안 하고 있으니까 불편하세요?"
    sen "조금."
    p "지금은 저랑 바다 보고 있잖아요."
    sen "그것도 일정에 포함되는 일이야?"
    p "일이 아니어도 같이 있을 수 있죠."

    narrator "선배는 파일을 다시 넣으려 손을 뻗다가 멈췄다. 대신 가방의 지퍼만 닫았다."

    python:
        _route_count = sum(1 for v in (
            umbrella_partner, barn_partner, storage_partner,
            maid_partner, library_partner, greenhouse_partner,
        ) if v == "yuna")

    if yuna_affection >= ending_affection_requirement and _route_count >= ending_route_choice_requirement:
        $ ending_promise_partner = "yuna"

        sen "방학식 날 일정 있어?"
        p "끝난 뒤에는 없습니다."
        sen "그러면 학생회실로 와."
        p "학생회 일 때문인가요?"
        sen "아무 일도 없어."
        p "그런데도요?"
        sen "일이 없어도 와줬으면 해."
        p "알겠습니다. 방학식 끝나고 갈게요."
        sen "먼저 가지 마."
        p "선배가 기다리라고 했으니 기다릴게요."
        sen "그날은 파일도 치워둘게."
    else:
        sen "잠깐 쉬는 것도 나쁘지는 않네."
        p "다음에도 같이 쉬어요."
        sen "기회가 있으면."

    hide yuna
    with dissolve
    jump coastal_end


label coastal_end:
    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene black
    with fade
    pause 1.0

    jump epilogue
