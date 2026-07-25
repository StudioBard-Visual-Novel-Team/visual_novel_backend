# 이벤트 씬 5 – 도서관과 밤의 해안가
# 학교 도서관 → 가로등이 켜진 해안가 도로

label event_library:
    stop music fadeout 1.5
    scene bg school_library
    with fade

    narrator "기말고사를 앞둔 도서관은 평소보다 자리가 빨리 찼다."
    narrator "나는 전공 서적과 필기 노트를 들고 빈자리를 찾았다."
    narrator "창가 쪽에는 한 자리만 비어 있었다."
    narrator "그 옆에 앉아 있는 사람을 확인한 나는 조용히 다가갔다."

    menu:
        "옆자리에 앉을 상대를 고른다."
        "서하린의 옆자리에 앉는다.":
            $ library_partner = "harin"
            jump library_harin
        "강연희의 옆자리에 앉는다.":
            $ library_partner = "yeonhee"
            jump library_yeonhee
        "차유나 선배의 옆자리에 앉는다.":
            $ library_partner = "yuna"
            jump library_yuna


# ---------- 서하린 루트 ----------
label library_harin:
    show harin neutral at center
    with dissolve

    narrator "하린은 문제집을 펼쳐놓고 한 페이지를 오래 바라보고 있었다."

    p "여기 앉아도 돼?"
    h "네. 자리 비어 있어요."

    narrator "나는 맞은편 의자를 빼고 앉았다."
    narrator "잠시 동안 책장 넘기는 소리만 이어졌다."
    narrator "하린은 같은 문제를 몇 번 다시 읽다가 연필을 내려놓았다."

    p "안 풀리는 문제야?"
    h "계산은 했는데 답이 자꾸 다르게 나와요."

    narrator "하린은 문제집을 내 쪽으로 조금 밀었다."

    p "여기 단위를 바꾸는 부분이 빠졌네. 계산 자체는 맞았어."
    h "아…… 이것 때문이었어요? 계속 틀린 줄 알았어요."
    p "다음에는 오래 막혀 있지 말고 물어봐."
    h "선배도 공부하고 계셨으니까 방해하고 싶지 않았어요. 그래도 다음에는 물어볼게요."

    narrator "시간이 지나 사서 선생님이 폐관 시간을 알렸다."

    lib "이제 정리해주세요. 곧 문 닫습니다."

    narrator "우리는 책을 정리하고 도서관을 나왔다."

    hide harin
    with dissolve
    scene bg coastal_road
    with fade
    stop music fadeout 1.5
    play sound "audio/ocean_waves_1.mp3" fadein 2.0 loop
    play music "audio/ocean_waves_1.mp3" fadein 2.0
    show harin neutral at center
    with dissolve

    narrator "밖은 이미 어두워져 있었고, 가로등 불빛이 해안가 도로를 일정한 간격으로 비추고 있었다."

    p "집까지 같이 갈까? 중간까지는 같은 방향이야."

    narrator "하린은 내 옆에서 천천히 걸었다."
    narrator "파도 소리와 발걸음만 이어졌다."

    h "도서관에서는 말이 없어도 괜찮았어요. 같이 있는데 조용해도 불편하지 않았어요."

    menu:
        "나도 너랑 있으면 조용한 시간이 편해.":
            p "나도 너랑 있으면 조용한 시간이 편해. 계속 말을 해야 같이 있는 건 아니잖아."

            narrator "하린은 가로등 아래에서 나를 바라봤다."

            h "보통은 제가 조용하면 대화가 끝난 줄 알고 먼저 가요. 그래서 저도 뭔가 계속 말해야 하나 고민했고요."
            p "지금은 안 그래도 돼. 같이 걷고 있는 것만으로 충분하니까."

            narrator "하린은 바로 대답하지 않고 내 걸음에 속도를 맞췄다."

            h "그렇게 생각해주면 조금 안심돼요."

            $ harin_affection += 2

        "도서관에서는 원래 조용하니까.":
            p "도서관에서는 원래 조용하니까. 그래도 네 옆에 있는 게 불편하지는 않았어."
            h "그건 다행이에요. 저도 오히려 편했어요."
            p "다음에도 자리가 비어 있으면 근처에 앉자."
            h "그러면 선배 자리도 같이 잡아둘게요."

        "말이 없으면 조금 어색할 때도 있어.":
            p "말이 없으면 조금 어색할 때도 있어."

            narrator "하린은 시선을 도로 쪽으로 돌렸다."

            h "그러면 제가 말을 더 해야겠네요. 같이 있는 사람이 불편해하면 싫으니까요."
            p "항상 불편하다는 뜻은 아니야. 오늘은 괜찮았어."
            h "……그럼 다음에는 조금 더 말할게요."

            $ harin_affection -= 1

    # 공통 후속 내용
    narrator "가로등 하나를 지나자 주변이 잠시 어두워졌다."
    narrator "바다는 보이지 않았지만 파도 소리는 가까이 들렸다."

    h "이 길은 밤이 되면 가로등 사이만 보여서 혼자 걸을 때는 빨리 지나가요. 뒤도 잘 안 보고요."
    p "오늘은 천천히 걷네."
    h "오늘은 혼자가 아니니까요."

    narrator "우리는 다음 가로등까지 말없이 걸었다."

    h "다음에도 도서관에서 늦게 끝나면 같이 가도 돼요?"
    p "시간이 맞으면 같이 가자."

    narrator "하린은 그 말만으로도 충분한 듯 작게 고개를 끄덕였다."

    hide harin
    with dissolve
    jump library_end


# ---------- 강연희 루트 ----------
label library_yeonhee:
    show yeonhee neutral at center
    with dissolve

    narrator "연희는 문제집 위에 턱을 괴고 있었다."

    p "공부하고 있는 거 맞아?"
    y "당연하지. 지금 머릿속으로 열심히 풀고 있었어."
    p "문제집이 십 분째 같은 페이지인데?"
    y "집중하면 시간이 멈추기도 해. 여기부터 설명해줘. 대신 내가 영어 쪽 봐줄게."

    narrator "우리는 서로 문제집을 바꿔가며 공부했다."
    narrator "연희는 이해가 되지 않는 부분에서는 장난을 멈추고 설명을 들었다."
    narrator "시간이 지나 사서 선생님이 폐관 시간을 알렸다."

    lib "마무리하고 나가주세요."

    narrator "도서관을 나오자 바깥은 이미 어두웠다."

    hide yeonhee
    with dissolve
    scene bg coastal_road
    with fade
    stop music fadeout 1.5
    play sound "audio/ocean_waves_1.mp3" fadein 2.0 loop
    play music "audio/ocean_waves_1.mp3" fadein 2.0
    show yeonhee neutral at center
    with dissolve

    narrator "우리는 가로등이 켜진 해안가 도로를 걸었다."

    y "이 시간에 학교에서 나오니까 기분 이상하다. 너무 조용하잖아."

    narrator "연희는 처음에는 평소처럼 이것저것 이야기했지만, 잠시 후 말수가 줄었다."

    p "왜 갑자기 조용해졌어?"
    y "나도 가끔은 조용할 수 있어. 혼자 조용한 거랑 둘이 조용한 건 다르니까."

    narrator "연희는 앞을 보며 말했다."

    y "내가 말 안 하면 재미없어 보여?"

    menu:
        "말을 안 해도 너는 너잖아.":
            p "말을 안 해도 너는 너잖아. 평소처럼 분위기를 계속 띄우지 않아도 달라지는 건 없어."

            narrator "연희의 걸음이 조금 느려졌다."

            y "사람들은 내가 조용하면 무슨 일 있냐고 묻다가 같이 어색해져. 그래서 피곤해도 다시 말을 시작하는 편이야."
            p "나랑 있을 때는 그러지 않아도 돼."

            narrator "연희는 몇 걸음 동안 아무 말 없이 걸었다."

            y "지금처럼 있어도 괜찮다는 거지?"
            p "응."

            narrator "연희는 더 확인하지 않고 앞을 바라봤다."

            $ yeonhee_affection += 2

        "조용한 모습도 나쁘지는 않아.":
            p "조용한 모습도 나쁘지는 않아. 평소 모습도 괜찮고."
            y "대답을 안전하게 하네. 그럼 오늘은 반은 말하고 반은 조용히 걸을게."
            p "생각보다 체계적이네."
            y "난 원래 계획적인 사람이야."

            narrator "나는 처음 듣는 말이었지만 굳이 반박하지 않았다."

        "평소보다는 조금 어색하긴 해.":
            p "평소보다는 조금 어색하긴 해."

            narrator "연희는 잠시 입을 다물었다."

            y "역시 내가 조용하면 이상하구나. 그럼 평소처럼 하면 되지."

            narrator "연희는 다시 학교 이야기를 시작했다."
            narrator "말투는 밝았지만 이전보다 속도가 빨랐다."

            p "억지로 말 안 해도 돼."
            y "억지 아니야. 원래 내가 이렇잖아."

            $ yeonhee_affection -= 1

    # 공통 후속 내용
    narrator "가로등 불빛이 연희의 옆얼굴을 스쳐 지나갔다."

    y "사실 계속 말을 이어가는 것도 가끔은 피곤해. 조용해지면 사람들이 재미없어할까 봐 멈추는 타이밍을 놓칠 뿐이지."
    p "오늘은 빈틈을 채우지 않아도 돼."

    narrator "연희는 잠시 정말 아무 말도 하지 않았다."
    narrator "파도 소리와 두 사람의 발소리만 이어졌다."

    y "생각보다 안 어색하네."
    p "그러게."

    narrator "연희는 웃었지만 더는 장난으로 분위기를 바꾸지 않았다."
    narrator "그 뒤로도 가끔 말을 꺼냈지만, 침묵이 생길 때마다 서둘러 없애려 하지는 않았다."

    hide yeonhee
    with dissolve
    jump library_end


# ---------- 차유나 루트 ----------
label library_yuna:
    show yuna neutral at center
    with dissolve

    narrator "선배는 두꺼운 문제집과 학생회 자료를 함께 펼쳐놓고 있었다."

    p "여기 앉아도 될까요?"
    sen "자리 비어 있어."

    narrator "나는 선배의 맞은편에 앉았다."

    p "시험공부하면서 학생회 자료도 보세요?"
    sen "축제 정산이 아직 끝나지 않았어. 미루면 더 쌓여."
    p "그러다 공부할 시간이 없어지겠는데요."
    sen "내가 알아서 조절해."

    narrator "한동안 서로 말없이 공부했다."
    narrator "선배는 학생회 자료를 덮고 문제집을 보다가 한 문제에서 펜을 멈췄다."

    p "안 풀리세요? 제가 봐도 돼요?"

    narrator "선배는 잠시 망설이다가 문제집을 내 쪽으로 돌렸다."

    p "여기 조건을 반대로 보신 것 같아요."
    sen "……그러네."
    p "선배도 모르는 문제가 있네요."
    sen "당연히 있지. 필요하면 물어보기도 해."

    narrator "사서 선생님이 폐관 시간을 알렸다."

    lib "정리하고 나가주세요."

    narrator "우리는 책과 자료를 정리하고 도서관을 나왔다."

    hide yuna
    with dissolve
    scene bg coastal_road
    with fade
    stop music fadeout 1.5
    play sound "audio/ocean_waves_1.mp3" fadein 2.0 loop
    play music "audio/ocean_waves_1.mp3" fadein 2.0
    show yuna neutral at center
    with dissolve

    narrator "가로등이 켜진 해안가 도로에는 사람이 거의 없었다."
    narrator "우리는 나란히 걷기 시작했다."

    p "선배는 이런 침묵이 안 불편하세요?"
    sen "대부분은 내가 말이 없으면 불편해하더라."

    menu:
        "저는 말 없는 것도 대화의 일부라고 생각해서요.":
            p "저는 말 없는 것도 대화의 일부라고 생각해요. 같이 걷고 있다는 건 말하지 않아도 알 수 있으니까요."

            narrator "선배가 내 쪽을 바라봤다."

            sen "대부분은 침묵이 길어지면 먼저 화제를 찾더라. 불편해 보이는 사람도 많았고."
            p "할 말이 생기면 그때 하면 돼요. 지금도 불편하지 않고요."

            narrator "선배는 다시 앞을 바라봤다."

            sen "너는 생각보다 편한 사람이네."
            p "칭찬으로 들을게요."

            narrator "선배는 부정하지 않았다."

            $ yuna_affection += 2

        "사람마다 다르니까요.":
            p "사람마다 다르니까요. 저는 지금은 괜찮아요."
            sen "지금은이라는 말이 걸리네."
            p "계속 같이 있어봐야 알 수 있잖아요. 도서관에서 자리가 비면 또 앉을게요."
            sen "비어 있으면 앉아."

        "그건 조금 이해돼요.":
            p "그건 조금 이해돼요. 익숙하지 않은 사람은 불편할 수도 있으니까요."
            sen "굳이 설명하지 않아도 돼."

            narrator "선배는 그 뒤로 먼저 말을 꺼내지 않았다."
            narrator "몇 걸음 뒤 내가 공부 이야기를 꺼냈지만 대답은 짧았고 더 이어지지 않았다."

            $ yuna_affection -= 1

    # 공통 후속 내용
    narrator "가로등이 끝나는 구간에서 선배가 걸음을 조금 늦췄다."

    sen "아까 문제 봐준 건 고마워. 혼자 다시 확인했으면 시간이 더 걸렸을 거야."
    p "다음에도 막히는 게 있으면 말씀하세요."
    sen "필요하면."

    narrator "잠시 뒤 선배가 조용히 덧붙였다."

    sen "오늘은 혼자 하지 않았잖아. 네가 계속 옆에 있다면 다음에도 그럴 수 있겠지."
    p "시험 기간에는 도서관에 자주 올 거예요."
    sen "그럼 자리가 비어 있을 때 앉아."

    narrator "짧은 말이었지만 다음에도 함께 공부해도 된다는 뜻으로 들렸다."

    hide yuna
    with dissolve
    jump library_end


# ---------- 도서관/밤 해안가 이벤트 종료 ----------
label library_end:
    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene black
    with fade
    pause 1.0

    jump chapter4
