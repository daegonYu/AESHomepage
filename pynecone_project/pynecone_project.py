"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
# import os,sys
# sys.path.append(os.path.dirname('/home/daegon/AES/'))
from matplotlib import pyplot as plt
import torch
from . import bert_scoring_model



class State(pc.State):      # 함수나 변수 전부 State. 으로 접근한다.
    """The app state."""

    # compute_processing: bool = False
    view_processing: bool = False
    text: str
    logical_point: int
    novelty_point: int
    persuasive_point: int 
    
    config_ = '/home/daegon/AES/models/chunk_model.bin1/config.json'    # config는 모두 같다.
    
    chunk_model_path = '/home/daegon/AES/models/chunk_model.bin4'; word_doc_model_path = '/home/daegon/AES/models/word_doc_model.bin4' 
    chunk_model_path = '/home/daegon/AES/models/chunk_model.bin5'; word_doc_model_path = '/home/daegon/AES/models/word_doc_model.bin5' 
    chunk_model_path = '/home/daegon/AES/models/chunk_model.bin6'; word_doc_model_path = '/home/daegon/AES/models/word_doc_model.bin6' 
        
    # '인공지능은 처음부터 먼 길을 왔으며 오늘날 ChatGPT와 같은 AI 모델은 한때 불가능하다고 생각했던 작업을 수행하는 데 도움이 됩니다. OpenAI에서 개발한 ChatGPT는 인간과 같은 응답 생성, 질문 응답 및 텍스트 완성을 포함하여 광범위한 작업을 수행할 수 있는 언어 모델입니다. 인간 언어를 이해하고 생성하는 능력을 갖춘 ChatGPT는 우리가 기술과 상호 작용하는 방식을 혁신할 수 있는 잠재력을 가지고 있습니다. ChatGPT의 가장 흥미로운 점 중 하나는 광범위한 응용 프로그램에서 사용할 수 있는 잠재력입니다.'
    input_sentence:list
      
    def set_text(self,text):
        # self.text = text    
        self.input_sentence = [text,""]
    
    def click_process(self):        # 버튼을 누르면 True로 변경
        self.view_processing = True
        

    def DLmodel_run(self):
        logical_model = bert_scoring_model.DocumentBertScoringModel(chunk_model_path=self.chunk_model_path, word_doc_model_path=self.word_doc_model_path, config=self.config_)
        novelty_model = bert_scoring_model.DocumentBertScoringModel(chunk_model_path=self.chunk_model_path, word_doc_model_path=self.word_doc_model_path, config=self.config_)
        persuasive_model = bert_scoring_model.DocumentBertScoringModel(chunk_model_path=self.chunk_model_path, word_doc_model_path=self.word_doc_model_path, config=self.config_)

        self.logical_point = logical_model.result_point(self.input_sentence, mode_='logical')
        self.novelty_point = novelty_model.result_point(self.input_sentence, mode_='novelty')
        self.persuasive_point = persuasive_model.result_point(self.input_sentence, mode_='persuasive')
        
        

def index():
    return pc.center(
        pc.vstack(
            pc.heading("여기서 자신의 에세이 점수를 측정할 수 있습니다!", font_size="2em"),
            pc.box("아래의 3가지 점수를 알 수 있어요.", font_size='1.5em'),
            pc.box("1) 논리성 ", font_size="1em"),
            pc.box("2) 참신성", font_size="1em"),
            pc.box("3) 설득력", font_size="1em"),
            
            pc.text_area(
                        # default_value=State.essay,
                        placeholder="Input your essay!",
                        width="100%",
                        on_blur= State.set_text          
                    ),
                    
            pc.button(
                "나의 글 점수 측정하기",
                on_click=State.click_process,
                width="100%",
            ),
            
            pc.cond(
                State.view_processing,
                pc.vstack(
                    pc.box(State.input_sentence[0]),
                    pc.box(State.input_sentence[0]),
                    pc.box(State.input_sentence[0])
                )
            ),
            
            pc.divider(), # 구분선
                        
                
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