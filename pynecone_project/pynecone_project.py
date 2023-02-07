"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import os 

# docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

# 링크 걸기 예제
# pc.link(
#                 "Check out our docs!",
#                 href=docs_url,
#                 border="0.1em solid",
#                 padding="0.5em",
#                 border_radius="0.5em",
#                 _hover={
#                     "color": "rgb(107,99,246)",
#                 }

# pc.image(     # 이미지 삽입 예시
#                         src=State.image_url,
#                         height="25em",
#                         width="25em",
#                     )

class State(pc.State):      # 함수나 변수 전부 State. 으로 접근한다.
    """The app state."""

    point_processing = False
    essay = 3
    
    def get_point(self):
        # os.system('"ex.py"')
        pass
    
    def process_state(self):        # 버튼을 누르면 True로 변경
        self.point_processing = True



def index():
    return pc.center(
        pc.vstack(
            pc.heading("여기서 자신의 에세이 점수를 측정할 수 있습니다!", font_size="2em"),
            pc.box("아래의 3가지 점수를 알 수 있어요.", font_size='1.5em'),
            pc.box("1) 논리성 ", font_size="1em"),
            pc.box("2) 참신성", font_size="1em"),
            pc.box("3) 설득력", font_size="1em"),
            
            pc.input(placeholder="Input my text",on_blur=State.set_essay),  # set_변수명에 저장되는듯?
            pc.button(
                "나의 글 점수 측정하기",
                on_click=[State.process_state,State.get_point],
                width="100%",
            ),
            
            pc.divider(), # 구분선
            
            # 버튼 누르면 보여주기
            pc.cond(
                State.point_processing,     # 버튼 누르면 보임
                pc.circular_progress(is_indeterminate=True),    # 원형 진행바
                pc.cond(        # cond() 하나에 글 하나씩
                    State.point_processing,
                    pc.box("1) 논리성 : {}".format(State.essay), font_size="1em"),
                    # pc.box("2) 참신성 : ", font_size="1em"),
                    # pc.box("3) 설득력 : ", font_size="1em"),  
                ),
            ),                    
                
            bg="white",
            padding="3em",
            shadow="lg",
            border_radius="lg",
            spacing="1.5em",
            # padding_top="10%"     # 위에 패딩 주기
            ),
        
        # 배경
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
