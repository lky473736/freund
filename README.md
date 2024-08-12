# freund
(project) Implementing a GPT model with dimensional speech recognition  

> freund는 독일어로 친구라는 의미입니다. 친구처럼 쉽게 이야기를 전할 수 있는 AI을 만들고자 하는 이 프로젝트의 제목은 제 푸른 다짐입니다.  

음성 인식을 통하여 LLM 모델에게 직접 질문 가능한 프로그램을 구현하는 프로젝트입니다. Django, Flask를 이용해 웹 프레임을 구축하고 OpenAI의 whisper 모델을 활용해 음성인식 후 가상화 레이어로 전처리된 보이스 데이터를 Llama 3 혹은 GPT-3 개조 버젼에 대입 가능하게 설계되었습니다. 또한 직접 만든 transformer LLM 모델을 대입할 예정입니다.

* 현재 구현 완료 예상 기간은 올해 안까지이며, agile 방식을 따릅니다.
* **현재는 개발 정지 상태이며, 9월 이후에 다시 재개할 예정입니다.**
* 본 문서의 commit message는 영어로 작성합니다. 프로젝트를 진행하면서 업로드 될 소논문 또한 영어로 작성합니다.

> **전에 했던 내용 정리**

- freund의 프로토타입을 공개하였다. 이 프로토타입은 기존의 llama2를 gguf 형식으로 변환한 모델을 대입하였고, 엔비디아의 CUDA 서포트가 현재 내 맥북에서 제공되고 있지 않다는 한계점을 인식하여 llama.cpp를 활용하여 본 인터페이스를 구축하였다. 음성 인식은 여전히 whisper를 사용하였고, 한 터미널에서 사용자와 LLM이 상호작용할 수 있는 형식으로 구현되었다. 

- 하지만 한계가 있었는데, whisper는 GPU 가속화 엔진을 사용해야만 인식 속도가 빠르다는 이유로, 본 개발환경을 google colab으로 옮기려고 하였으나, colab 또한 기본 옵션과 pro옵션의 가격 및 성능 대비로 적합하지 않다고 생각하였다. 따라서 결국엔 whisper 대신에 CPU와 메모리의 리소스를 적절히 활용하는 whisper.cpp 모델을 적용하였다. 확실히 기존과 비교하였을 때 속도가 빠르면서 말하는 즉시 반응하는 모델엔 cpp로 작성된 concatanation code bunch가 좋다고 나는 주장하고 싶다. 또한 기존 whisper base 버전은 한국어를 인식을 할 수는 있으나, import 시 mac의 고유의 문제인 파일 확장자 오류가 발생하여 try-except문을 활용하여 이를 개선하였다. bin 파일을 적용하여 현재는 음성 인식이 무리 없이 동작한다.

- 추가적으로 터미널을 하나 더 열어 한 쪽에서는 현재 Ai의 상황을 보여주고, 한쪽에서는 질문과 답변을 보여주는 형식으로 업그레이드하였다. 따라서 동시에 터미널을 2개 열어서 사용자 친숙성을 높인 형식인데, 이를 나는 터미널 더블링이라고 이름을 붙였다. 본 방식을 구현하기 위해서 처음에는 shell 파일을 사용하여 동시에 두 파일을 열어 시스템이 multiprocess 되도록 하려고 했으나, 계속 한 터미널에서 두개의 파일이 동작되는 오류로 다른 방법을 생각해내었다. subprocess 모듈을 사용하여 애플스크립트를 대입하였고, 애플스크립트에서는 터미널을 열고 그 터미널에서 사용자의 질문과 LLM의 답변을 보여주는 process/printer/printer.py를 열게 하였다. 또한 env 환경변수 파일로 실시간으로 Token값과 word값을 조정하고 즉시 삭제하는 형식으로 현재 상태 및 질문과 답변을 업데이트 하도록 개발하였다.

- 다음 주차에 진행해야 할 점은 디렉토리 리팩토링 및 한국어 인식 가능 llama 파일을 찾는 것이다. bllossom이라고 하는 한국어 LLM 모델을 찾았으니 이를 대입해보는 것이 다음 주차의 첫번째 백로그라고 할 수 있겠다.


<hr>

> "Freund" means "friend" in German. It is my commitment to make AI that can tell stories as easily as friends.

It is a project to implement a program that can ask questions directly to GPT-3 through voice recognition. Building a web frame using Django and Flask, and using OpenAI's whisper model, voice recognition and pre-processing voice data with a virtualization layer are substituted into the Llama 3 or GPT-3 modified version.

The current implementation completion period is early June and follows the agile method.