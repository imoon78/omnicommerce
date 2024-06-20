import streamlit as st
import urllib3

st.header = "유사상품 추천"

prd_no = st.text_input("유사상품 추천 TEST", placeholder="상품번호를 입력하세요")
st.write("입력된 상품번호 : ", prd_no)


try:
    http = urllib3.PoolManager()

    oriImage = ""

    if prd_no != "":
        oridata = http.request("GET", "http://apix.halfclub.com/searches/prdList/?keyword=" + prd_no + "&siteCd=1&device=mc").json()
        #st.json(oridata)

        oriImage = oridata["data"]["result"]["hits"]["hits"][0]["_source"]["appPrdImgUrl"]
        st.image(oriImage)

        data = http.request("GET", "http://develop-api.halfclub.com/searches/recommProducts/?prdNo=" + prd_no).json()
        
        recommend_list = data["data"]["productDTOList"]
        #st.json(recommend_list)
        result_container = st.container()
        recognition_result_container = result_container.columns(4)

        i=0
        for recommend in recommend_list:
            try:
                recognition_result_container[i%4].image(recommend["productImage"]["basicExtUrl"], caption=recommend["productImage"]["prdNo"])
                i=i+1
            except Exception as ex:
                st.text(ex)
        st.json(recommend_list)
except Exception as ex:
    st.text(ex)


