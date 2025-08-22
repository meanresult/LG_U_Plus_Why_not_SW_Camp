import streamlit as st # streamlit UI 랑 Stockinfo 만들거임 ㅋ ㅋ ㅋㅋ 
from search import stock_search
from stock_info import StockInfo
from report_service import inverstment_report


class SearchResult:
    def __init__(self, item):
        self.item = item
        
    @property
    def symbol(self):
        return self.item['Symbol']
    @property
    def name(self):
        return self.item['Name']
    def __str__(self):
        return f'{self.symbol}: {self.name}'

st.title('LLM으로 만드는 투자 보고서 생성 서비스')
search_query = st.text_input('회사명','Apple')

#종목검색결과 리스트
hits_list = stock_search(search_query)['hits']
# print(hits_list)
SearchResults = [SearchResult(hit) for hit in hits_list]

selected = st.selectbox('검색 결과 목록', SearchResults)

st.header(f'{selected}')
stock = StockInfo(selected.symbol) # 이게 ticket 심부름꾼
st.write(stock.get_basic_info()) # 기본정보
st.write(stock.get_financial_statement()) # 재무정보 
st.write(inverstment_report(selected.symbol, selected.name, stock))

