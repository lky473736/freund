# freund
(project) Implementing a GPT model with dimensional speech recognition  

> freund는 독일어로 친구라는 의미입니다. 친구처럼 쉽게 이야기를 전할 수 있는 AI을 만들고자 하는 이 프로젝트의 제목은 제 푸른 다짐입니다.  

GPT-3에게 음성 인식을 통하여 직접 질문 가능한 프로그램을 구현하는 프로젝트입니다. Django, Flask를 이용해 웹 프레임을 구축하고 OpenAI의 whisper 모델을 활용해 음성인식 후 가상화 레이어로 전처리된 보이스 데이터를 Llama 3 혹은 GPT-3 개조 버젼에 대입합니다.  

* 현재 구현 완료 예상 기간은 6월 초이며, agile 방식을 따릅니다.
* 본 문서의 commit message는 영어로 작성합니다. 프로젝트를 진행하면서 업로드 될 소논문 또한 영어로 작성합니다.

> [!NOTE]
> <b>현재 진행 상태 : 프로토타입 완성 (terminal / 추후 llama.cpp의 속도 개선 및 입출력 방향성 생각해야함)</b>


<hr>

> "Freund" means "friend" in German. It is my commitment to make AI that can tell stories as easily as friends.

It is a project to implement a program that can ask questions directly to GPT-3 through voice recognition. Building a web frame using Django and Flask, and using OpenAI's whisper model, voice recognition and pre-processing voice data with a virtualization layer are substituted into the Llama 3 or GPT-3 modified version.

The current implementation completion period is early June and follows the agile method.