# 챕터 1 – 새로운 시작
# 5월 · 학교 생활 적응
# 챕터 1 인트로만 담당 (이벤트 씬 1은 event_umbrella.rpy로 분리)

label chapter1_common:
    stop music fadeout 1.5
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
    narrator "교실에 들어갈 때마다 시선이 따라오는 것 같았고 복도에서 마주치는 학생들의 얼굴도 쉽게 구분되지 않았다."
    narrator "실습실로 가는 길도 헷갈렸다."
    narrator "아침 조회가 끝나면 어디로 이동해야 하는지, 점심시간에는 어느 복도가 붐비는지, 방과 후에는 어떤 학생들이 남아 있는지 하나씩 익혀야 했다."
    narrator "나는 쉬는 시간마다 복도 게시판을 확인했다."
    narrator "실습 일정, 학교 규정, 동아리 안내, 급식표 같은 것들이 빼곡하게 붙어 있었다."

    p "생각보다 챙겨야 할 게 많네."

    scene bg practice_room
    with fade

    narrator "농업 전문 학교라는 말은 알고 있었지만, 실제로 다녀보니 더 실감이 났다."
    narrator "교실 수업만 있는 게 아니라, 실습장과 온실, 창고, 축산 실습장까지 오가야 했다."
    narrator "처음에는 길을 잘못 들어 다른 반 실습실 앞까지 간 적도 있었다."
    narrator "그때마다 나는 괜히 가방끈을 고쳐 잡고 다시 방향을 찾았다."
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
    narrator "하지만 이상하게도, 익숙해질수록 세 사람이 더 자주 머릿속에 걸렸다."

    narrator "조용히 고개를 숙이던 하린."
    narrator "밝게 먼저 말을 걸어오던 연희."
    narrator "말은 차가웠지만 해야 할 일은 정확히 챙기던 선배."

    narrator "아직은 전부 어색한 사이였다."
    narrator "하지만 완전히 모르는 사람이라고 하기에도 조금 애매해졌다."

    scene bg school_playground_sunset__rain_1
    with fade
    
    narrator "그러던 어느 날이었다."
    narrator "수업이 끝나자마자 하늘이 무너지듯 비가 쏟아졌다."

    jump event_umbrella
