from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수를 불러옵니다.
load_dotenv()

# 환경 변수 읽기
openai_api_key = os.getenv("OPENAI_API_KEY")

print("API Key configured:", "OPENAI_API_KEY" in os.environ)

# 랭체인 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model='gpt-4o-mini')

def inverstment_report(symbol, company, stock):
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '''
            Want assistance provided by qualified individuals enabled with experience on understanding charts 
            using technical analysis tools while interpreting macroeconomic environment prevailing across world 
            consequently assisting customers acquire long term advantages requires clear verdicts 
            therefore seeking same through informed predictions written down precisely!
        '''),
            ('user', '''
                {company}에 주식을 투자하려고 합니다. 아래의 기본정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성하세요.
                
                -결론은 두괄식으로 말하고 일반인도 이해하기 쉽도록 설명해줘. 
                
                -긍정적인 결과일 경우 초록글씨로 부정적인 경우엔 빨간 글씨로 표시해
                
                -표를 작성할 경우엔 가독성이 있도록 문장 단위를 잘 끊어줘
                
                - 기본정보 : 
                {business_info}
                
                - 재무제표 :
                {financial_statements}
             ''')
        ]
    )
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    response = chain.invoke(
        {'company' : company,
         'business_info' : stock.get_basic_info(),
         'financial_statements': stock.get_financial_statement()
         })
    
    
    return response